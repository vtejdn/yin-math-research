"""Exact word problem, product tables, and bounded unique-product tests.

Run with Python 3.10+ and assertions enabled: python -B verify.py
No third-party libraries, downloaded files, or temporary scripts are needed.
"""
from collections import Counter
from functools import lru_cache
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from pathlib import Path
import argparse


POSITIVE = "abcdefg"
LETTERS = POSITIVE + POSITIVE.upper()
TRIANGLES = ("acb", "add", "afg", "bbf", "cef", "cdg", "eeg")
RELATORS = ("abaaBaaBB", "abbbabbbbAb")
IMAGES = {
    "a": "a", "b": "b", "c": "AB", "d": "baaBB",
    "e": "babb", "f": "BB", "g": "bbA",
}
EXPECTED_BALLS = (1, 5, 17, 53, 161, 467, 1311, 3637, 9929)
DEFAULT_CASES = ((1, 8), (2, 7), (3, 6), (4, 4), (4, 5))


def inverse(word):
    return word[::-1].swapcase()


def free_reduce(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == letter.swapcase():
            stack.pop()
        else:
            stack.append(letter)
    return "".join(stack)


def make_rules():
    rules = {}
    completion = {}

    def put(left, right):
        assert left not in rules or rules[left] == right
        rules[left] = right

    for letter in LETTERS:
        put(letter + letter.swapcase(), "")
    for triangle in TRIANGLES:
        for offset in range(3):
            x, y, z = triangle[offset:] + triangle[:offset]
            put(x + y, z.upper())
            put(inverse(x + y), z)
            assert (x, z) not in completion or completion[x, z] == y
            completion[x, z] = y
    for x, y in product(POSITIVE, repeat=2):
        if x == y:
            continue
        common = [z for z in POSITIVE
                  if (x, z) in completion and (y, z) in completion]
        assert len(common) == 1
        z = common[0]
        put(x.upper() + y, completion[x, z] + completion[y, z].upper())
    assert len(rules) == 98
    return rules


RULES = make_rules()


@lru_cache(maxsize=None)
def normal_form(word):
    """Deterministic leftmost reduction; termination is proved in C105v2."""
    for position in range(len(word) - 1):
        replacement = RULES.get(word[position:position + 2])
        if replacement is not None:
            return normal_form(
                word[:position] + replacement + word[position + 2:])
    return word


def check_presentation_and_overlaps():
    critical = 0
    for letters in product(LETTERS, repeat=3):
        word = "".join(letters)
        left, right = RULES.get(word[:2]), RULES.get(word[1:])
        if left is not None and right is not None:
            critical += 1
            assert normal_form(left + word[2]) == normal_form(word[0] + right)
    for triangle in TRIANGLES:
        substituted = "".join(IMAGES[letter] for letter in triangle)
        target = RELATORS[0] if triangle == "add" else (
            "b" + RELATORS[1] + "B" if triangle == "eeg" else "")
        assert free_reduce(substituted) == free_reduce(target)
        assert normal_form(triangle) == ""
    for generator, word in IMAGES.items():
        assert normal_form(word) == generator
    assert all(normal_form(relator) == "" for relator in RELATORS)
    print("Rules and joined three-letter overlaps:", len(RULES), critical,
          flush=True)


def word_balls():
    """Breadth-first search in the exact group, with shortest abAB words."""
    representatives = {"": ""}
    frontier = [""]
    balls = {0: ("",)}
    for radius in range(1, len(EXPECTED_BALLS)):
        following = []
        for element in frontier:
            for letter in "abAB":
                target = normal_form(element + letter)
                if target not in representatives:
                    representatives[target] = representatives[element] + letter
                    following.append(target)
        frontier = following
        balls[radius] = tuple(representatives.values())
        assert len(balls[radius]) == EXPECTED_BALLS[radius]
        assert len({normal_form(word) for word in balls[radius]}) == len(balls[radius])
    print("Ball sizes, radii zero through eight:",
          [len(balls[r]) for r in range(len(EXPECTED_BALLS))], flush=True)
    return balls


def load_appendix_input():
    """One explicit retained cross-J dependency, independent of the cwd."""
    filename = Path(__file__).resolve().parent.parent / "Yin_J_A0004" / "verify.py"
    spec = spec_from_file_location("gardam_appendix_j4", filename)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_appendix_partition():
    source = load_appendix_input()
    assert source.RELATORS == RELATORS
    edges = source.cayley_edges()
    coarse = source.partition(edges, source.relation_basis(edges))
    exact = {}
    for i, left in enumerate(source.ROWS):
        for j, right in enumerate(source.COLS):
            exact.setdefault(normal_form(left + right), []).append((i, j))
    assert len({normal_form(word) for word in source.ROWS}) == 32
    assert len({normal_form(word) for word in source.COLS}) == 28
    assert {frozenset(bucket) for bucket in coarse} == {
        frozenset(bucket) for bucket in exact.values()}
    assert len(exact) == 336
    histogram = dict(sorted(Counter(map(len, exact.values())).items()))
    assert histogram == {2: 230, 3: 53, 4: 26, 5: 10, 6: 8,
                         7: 6, 10: 1, 11: 1, 12: 1}
    print("Exact appendix buckets and histogram:", len(exact), histogram,
          flush=True)


MONOMIALS = tuple("".join(letters) for size in range(1, 5)
                  for letters in product("ab", repeat=size))


def sorting_key(word):
    """A finite deterministic heuristic; no order on the group is assumed."""
    coefficients = {"": 1}
    for letter in word:
        following = coefficients.copy()
        for monomial, coefficient in coefficients.items():
            limit = 4 - len(monomial)
            if letter.islower():
                limit = min(1, limit)
            for power in range(1, limit + 1):
                term = monomial + letter.lower() * power
                sign = (-1) ** power if letter.isupper() else 1
                following[term] = following.get(term, 0) + coefficient * sign
        coefficients = following
    return tuple(coefficients.get(term, 0) for term in MONOMIALS), word


def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask -= bit


def unique_product_test(left_words, right_words):
    """Find a nonempty rectangle with no singleton product, or exhaust all.

    Rows and columns have independent arbitrary finite orders. Every candidate
    has unique maximal indices, which bound all subsequent partner choices.
    Memoization is reset for each pair of maxima.
    """
    rows = sorted(left_words, key=sorting_key)
    columns = sorted(right_words, key=sorting_key)
    nr, nc = len(rows), len(columns)
    buckets = {}
    for i, left in enumerate(rows):
        for j, right in enumerate(columns):
            buckets.setdefault(normal_form(left + right), []).append((i, j))
    partners = {}
    row_compatible = [0] * nr
    column_compatible = [0] * nc
    for bucket in buckets.values():
        for cell in bucket:
            i, j = cell
            others = tuple(other for other in bucket if other != cell)
            partners[cell] = others
            if others:
                row_compatible[i] |= 1 << j
                column_compatible[j] |= 1 << i

    states = seeds = 0
    for maximum_row in range(nr):
        for maximum_column in range(nc):
            if not any(i <= maximum_row and j <= maximum_column
                       for i, j in partners[maximum_row, maximum_column]):
                continue
            seeds += 1
            allowed_rows = (2 << maximum_row) - 1
            allowed_columns = (2 << maximum_column) - 1
            seen = set()
            pending = [(1 << maximum_row, 1 << maximum_column)]

            while pending:
                row_mask, column_mask = pending.pop()
                state = row_mask, column_mask
                if state in seen:
                    continue
                seen.add(state)
                states += 1
                selected_rows = tuple(bits(row_mask))
                selected_columns = tuple(bits(column_mask))
                possible_rows, possible_columns = allowed_rows, allowed_columns
                for i in selected_rows:
                    possible_columns &= row_compatible[i]
                for j in selected_columns:
                    possible_rows &= column_compatible[j]
                if row_mask & ~possible_rows or column_mask & ~possible_columns:
                    continue

                forced_rows, forced_columns = row_mask, column_mask
                choice = None
                impossible = False
                for i in selected_rows:
                    for j in selected_columns:
                        alternatives = partners[i, j]
                        if any(row_mask >> u & 1 and column_mask >> v & 1
                               for u, v in alternatives):
                            continue
                        options = tuple((u, v) for u, v in alternatives
                                        if possible_rows >> u & 1
                                        and possible_columns >> v & 1)
                        if not options:
                            impossible = True
                            break
                        if len(options) == 1:
                            u, v = options[0]
                            forced_rows |= 1 << u
                            forced_columns |= 1 << v
                        elif choice is None or len(options) < len(choice):
                            choice = options
                    if impossible:
                        break
                if impossible:
                    continue
                forced = forced_rows, forced_columns
                if forced != state:
                    pending.append(forced)
                elif choice is None:
                    return ([rows[i] for i in selected_rows],
                            [columns[j] for j in selected_columns]), seeds, states
                else:
                    # Reverse push preserves the natural deterministic DFS order.
                    pending.extend((row_mask | (1 << u), column_mask | (1 << v))
                                   for u, v in reversed(choice))
    return None, seeds, states


def verify(cases):
    check_presentation_and_overlaps()
    balls = word_balls()
    check_appendix_partition()
    for left_radius, right_radius in cases:
        survivor, seeds, states = unique_product_test(
            balls[left_radius], balls[right_radius])
        assert survivor is None, (left_radius, right_radius, survivor)
        print("Excluded every nonempty NUP rectangle:",
              (left_radius, right_radius), "maxima", seeds, "states", states,
              flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pair", nargs=2, type=int, metavar=("R", "S"),
                        help="check one chosen radius pair instead of the retained ranges")
    arguments = parser.parse_args()
    cases = (tuple(arguments.pair),) if arguments.pair is not None else DEFAULT_CASES
    assert all(0 <= r <= 8 and 0 <= s <= 8 for r, s in cases)
    verify(cases)

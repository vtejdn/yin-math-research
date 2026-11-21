"""Fixed-depth nonbacktracking endpoint capacities for the Gardam triples.

Python 3.10+, standard library; writes no files. Depths are fixed at 16/17.
"""
from collections import Counter
from functools import lru_cache
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import argparse


SOURCE = Path(__file__).resolve().parent.parent / "Yin_J_A0006" / "verify.py"
SPEC = spec_from_file_location("gardam_triples_j6", SOURCE)
assert SPEC is not None and SPEC.loader is not None
J6 = module_from_spec(SPEC)
SPEC.loader.exec_module(J6)
J5 = J6.J5
TRIPLES = tuple(J6.TABLES)
EXPECTED = {
    "L": {1: 126397, 2: 2238, 3: 66},
    "R": {1: 250257, 2: 5577, 3: 244},
}
CACHE_LIMIT = 50000
PAIR_STEPS = 8


@lru_cache(maxsize=CACHE_LIMIT)
def normal_form(word):
    """The same leftmost rules as J5, iterated with a bounded result cache."""
    while True:
        for position in range(len(word) - 1):
            replacement = J5.RULES.get(word[position:position + 2])
            if replacement is not None:
                word = word[:position] + replacement + word[position + 2:]
                break
        else:
            return word


def endpoint_histogram(triple, root):
    """Count paths by (endpoint, final color), then accumulate by endpoint.

    Each two-edge step starts on the left:
       v --color i--> p_i v --color k--> p_k^-1 p_i v.
    The final color prevents immediate reversal across the next pair.
    """
    normal_form.cache_clear()
    multipliers = {
        (i, k): normal_form(triple[k].upper() + triple[i])
        for i in range(3) for k in range(3) if i != k
    }
    if root == "L":
        frontier = {("", -1): 1}
        accumulated = Counter({"": 1})
        short_step = 3  # Even lengths at most six.
    else:
        assert root == "R"
        frontier = {(color.upper(), i): 1 for i, color in enumerate(triple)}
        accumulated = Counter({color.upper(): 1 for color in triple})
        short_step = 2  # Odd lengths at most five.
    short_endpoints = None

    for step in range(1, PAIR_STEPS + 1):
        following = {}
        for (word, last), count in frontier.items():
            for first in range(3):
                if first == last:
                    continue
                for second in range(3):
                    if second == first:
                        continue
                    target = normal_form(multipliers[first, second] + word)
                    key = target, second
                    following[key] = following.get(key, 0) + count
        frontier = following
        for (word, last), count in frontier.items():
            accumulated[word] += count
        expected_layer = 6 * 4 ** (step - 1) if root == "L" else 3 * 4 ** step
        expected_total = 2 * 4 ** step - 1 if root == "L" else 4 ** (step + 1) - 1
        assert sum(frontier.values()) == expected_layer
        assert sum(accumulated.values()) == expected_total
        if step == short_step:
            assert all(count == 1 for count in accumulated.values())
            short_endpoints = frozenset(accumulated)

    assert short_endpoints is not None
    assert len(short_endpoints) == (127 if root == "L" else 63)
    assert all(accumulated[word] == 1 for word in short_endpoints)
    histogram = dict(sorted(Counter(accumulated.values()).items()))
    assert histogram == EXPECTED[root]
    endpoint_count = sum(histogram.values())
    path_count = sum(multiplicity * count for multiplicity, count in histogram.items())
    assert endpoint_count == (128701 if root == "L" else 256078)
    assert path_count == (131071 if root == "L" else 262143)
    assert normal_form.cache_info().currsize <= CACHE_LIMIT
    normal_form.cache_clear()
    return histogram, endpoint_count, path_count


def capacity_bound(histogram, root):
    """Arithmetic in the proved path-count and forced-singleton inequalities."""
    if root == "L":
        required_paths = 1 + 3 * sum(2 ** j for j in range(8))
        forced_singletons = 1 + 3 * sum(2 ** j for j in range(3))
        assert (required_paths, forced_singletons) == (766, 22)
    else:
        required_paths = 3 * sum(2 ** j for j in range(9))
        forced_singletons = 3 * sum(2 ** j for j in range(3))
        assert (required_paths, forced_singletons) == (1533, 21)
    assert max(histogram) == 3
    # M <= 2|B| + number_of_triple_endpoints - forced_singletons.
    numerator = required_paths - histogram[3] + forced_singletons
    bound = (numerator + 1) // 2
    assert bound == (361 if root == "L" else 655)
    return required_paths, forced_singletons, bound


def verify(triples):
    J5.check_presentation_and_overlaps()
    J5.normal_form.cache_clear()
    for triple in triples:
        for root in ("L", "R"):
            histogram, endpoints, paths = endpoint_histogram(triple, root)
            required, forced, bound = capacity_bound(histogram, root)
            print(triple, root, "histogram", histogram,
                  "endpoints", endpoints, "paths", paths,
                  "required", required, "forced singletons", forced,
                  "support bound", bound, flush=True)
    assert 361 % 2 == 1 and 361 < 655
    print("Pair-fiber parity also excludes right-support size 361.", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--triple", choices=TRIPLES,
                        help="check one retained triple instead of all seven")
    args = parser.parse_args()
    verify((args.triple,) if args.triple else TRIPLES)

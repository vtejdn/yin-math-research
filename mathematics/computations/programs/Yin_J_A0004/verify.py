"""Check all subrectangles of the Gardam-lattice witness in MS26b, Appendix A."""
from collections import Counter


def words(text):
    return tuple("" if word == "1" else word for word in text.split())


ROWS = words("""
    1 a A b ab aB Ab bb
    aba abb aBB AbA Abb abaa abab abbA
    abbb AbAb Abbb aabaa abaab bbAA ababb abbAA
    abbAb abbbb AbAA AbAbb bbAAB abaabb abbAbb AbAAb
""")
COLS = words("""
    1 A b B ab AA bA bb
    BA bAA bbA bbb Bab BBAB bbAA abbab
    AbAA BAbAA BBAAA BBABA BBBAB abbbbb babbab bbAbAA
    BBBAAA BBBABA BBABab bAbAA
""")
RELATORS = ("abaaBaaBB", "abbbabbbbAb")
GENERATORS = ((-8, (1, 2, 0, 3)), (1, (0, 3, 1, 2)))


def cayley_edges():
    """Right multiplication in the image in C42 x S4, then inverse edges."""
    identity = (0, (0, 1, 2, 3))
    states = [identity]
    position = {identity: 0}
    edges = []
    for residue, perm in states:
        neighbors = []
        for offset, generator in GENERATORS:
            image = tuple(perm[i] for i in generator)
            target = ((residue + offset) % 42, image)
            if target not in position:
                position[target] = len(states)
                states.append(target)
            neighbors.append(position[target])
        edges.append(neighbors + [-1, -1])
    for v, neighbors in enumerate(edges):
        for i, target in enumerate(neighbors[:2]):
            assert edges[target][i+2] == -1
            edges[target][i+2] = v
    return edges


def walk(edges, start, word):
    """Return the endpoint and the mod-two chain of the unoriented traversal."""
    vertex = start
    chain = 0
    for letter in word:
        direction = "abAB".index(letter)
        target = edges[vertex][direction]
        base = vertex if direction < 2 else target
        chain ^= 1 << (2 * base + direction % 2)
        vertex = target
    return vertex, chain


def relation_basis(edges):
    basis = {}
    for vertex in range(len(edges)):
        for relator in RELATORS:
            target, vector = walk(edges, vertex, relator)
            assert target == vertex
            while vector:
                pivot = vector.bit_length() - 1
                if pivot not in basis:
                    basis[pivot] = vector
                    break
                vector ^= basis[pivot]
    return sorted(basis.items(), reverse=True)


def partition(edges, basis):
    def signature(word):
        vertex, vector = walk(edges, 0, word)
        for pivot, row in basis:
            if vector & (1 << pivot):
                vector ^= row
        return vertex, vector

    assert len(set(map(signature, ROWS))) == len(ROWS) == 32
    assert len(set(map(signature, COLS))) == len(COLS) == 28
    buckets = {}
    for i, left in enumerate(ROWS):
        for j, right in enumerate(COLS):
            buckets.setdefault(signature(left + right), []).append((i, j))
    return list(buckets.values())


ROW_BITS = (1 << len(ROWS)) - 1
ALL_BITS = (1 << (len(ROWS) + len(COLS))) - 1


def cell_mask(i, j):
    return (1 << i) | (1 << (len(ROWS) + j))


def possible_supports(buckets):
    """Enumerate rectangles with two nonempty sides and no singleton bucket."""
    groups = [[cell_mask(i, j) for i, j in bucket] for bucket in buckets]
    answers = []

    def visit(present, absent):
        while True:
            allowed = ALL_BITS ^ absent
            if not (allowed & ROW_BITS) or not (allowed >> len(ROWS)):
                return
            add = remove = score = preferred = 0
            for group in groups:
                missing = [cell & ~present for cell in group if not cell & absent]
                if len(missing) == 1:
                    m = missing[0]
                    if m == 0:
                        return
                    if m.bit_count() == 1:
                        remove |= m
                    elif score < 2:
                        score, preferred = 2, m
                elif len(missing) == 2:
                    m, n = missing
                    if m == 0:
                        add |= n
                    if n == 0:
                        add |= m
                    if m and n and min(m.bit_count(), n.bit_count()) == 1 and score < 3:
                        score, preferred = 3, m if m.bit_count() == 1 else n
                elif len(missing) > 2 and missing.count(0) == 1 and score < 4:
                    score = 4
                    preferred = next(m for m in missing if m)
            if add & remove or present & remove or absent & add:
                return
            if not (add or remove):
                break
            present |= add
            absent |= remove
        undecided = ALL_BITS & ~(present | absent)
        if not undecided:
            answers.append(present)
            return
        candidates = (preferred & undecided) or undecided
        bit = candidates & -candidates
        visit(present | bit, absent)
        visit(present, absent | bit)

    visit(0, 0)
    return sorted(answers)


# For each surviving row set, three two-cell buckets identify consecutive
# ratios with opposite signs. The resulting cancellation is inside the triple.
CERTIFICATES = (
    (tuple(range(32)),
     ((0, 6), (3, 1), (7, 8)),
     (((0, 13), (3, 20)), ((23, 13), (19, 20)), ((23, 6), (19, 1)))),
    ((0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 17, 18, 26, 27, 31),
     ((0, 6), (3, 1), (7, 8)),
     (((0, 13), (3, 20)), ((26, 13), (31, 20)), ((26, 6), (31, 1)))),
    ((4, 8, 9, 13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25, 28, 29, 30),
     ((4, 2), (9, 0), (16, 3)),
     (((4, 16), (9, 17)), ((23, 16), (19, 17)), ((23, 2), (19, 0)))),
)


def check_ratio_path(triple, pairs):
    (i, j), (k, l), _ = triple
    cursor = ("row", i, k)
    for (u, v), (w, z) in pairs:
        row = ("row", u, w)
        col = ("column", z, v)
        assert cursor in (row, col)
        cursor = col if cursor == row else row
    assert cursor == ("column", l, j) and len(pairs) % 2 == 1


def verify():
    edges = cayley_edges()
    basis = relation_basis(edges)
    buckets = partition(edges, basis)
    assert len(edges) == 168 and len(basis) == 161
    histogram = dict(sorted(Counter(map(len, buckets)).items()))
    assert histogram == {2: 230, 3: 53, 4: 26, 5: 10, 6: 8, 7: 6, 10: 1, 11: 1, 12: 1}
    answers = possible_supports(buckets)
    expected = []
    for rows, triple, pairs in CERTIFICATES:
        required = (ALL_BITS ^ ROW_BITS) | sum(1 << i for i in rows)
        expected.append(required)
        restricted = {frozenset((i, j) for i, j in group if i in rows) for group in buckets}
        assert all(frozenset(block) in restricted for block in (triple, *pairs))
        check_ratio_path(triple, pairs)
    assert answers == sorted(expected)
    print("Quotient vertices, relator-chain rank, product buckets:", len(edges), len(basis), len(buckets))
    print("Bucket sizes and frequencies:", histogram)
    print("Nonempty surviving support sizes:", [(len(rows), len(COLS)) for rows, _, _ in CERTIFICATES])
    print("Every surviving rectangle has a verified three-pair contradiction.")


if __name__ == "__main__":
    verify()

"""Verify the five-channel certificates from the explicit ordered edge lifts."""

from collections import Counter
from itertools import permutations, product


CERTIFICATES = """01342 12034 1 32 8 4
01342 12340 1 32 3 32
01342 12403 1 32 2 736
01342 23014 7 996 1 96
01342 23140 2 352 1 96
01342 23401 2 224 1 96
02143 12340 1 32 2 480
02143 13204 1 32 1 32
02143 13420 1 192 11 52
12340 01342 7 993 11 133
12340 01423 7 993 5 993
12340 02143 7 993 5 993
12340 02431 11 5 10 486
12340 03412 7 997 4 228
12340 04132 11 5 5 484
12340 12403 8 33 12 425
12340 13042 8 37 11 37
12340 14023 6 488 9 204
12340 20413 6 456 10 490
01243 12340 0 0 3 32
01243 13420 0 0 1 160
02341 10432 0 0 4 420
02341 12034 0 0 5 996
02341 12340 0 0 6 48
02341 13042 0 0 1 100
02341 13204 0 0 6 40
02341 13420 0 0 4 228
02341 14023 0 0 7 488
02341 14230 0 0 8 2
10342 02143 0 0 9 329
10342 02314 0 0 10 1001
10342 02431 0 0 8 5
10342 12034 0 0 8 4
10342 12340 0 0 9 113
10342 12403 0 0 9 233
10342 23014 0 0 8 5
10342 23140 0 0 11 49
10342 23401 0 0 10 490"""


def compose(a, b):
    return tuple(a[j] for j in b)


def groups_and_orbits():
    perms = list(permutations(range(5)))
    index = {p: i for i, p in enumerate(perms)}
    table = [[index[compose(a, b)] for b in perms] for a in perms]
    inverse = [row.index(0) for row in table]
    odd = [sum(p[i] > p[j] for i in range(5) for j in range(i + 1, 5)) % 2 for p in perms]
    covered = set()
    for x, y in product(range(120), repeat=2):
        if (x, y) in covered or odd[y]:
            continue
        orbit = {(table[table[h][x]][inverse[h]], table[table[h][y]][inverse[h]])
                 for h in range(120)}
        covered.update(orbit)
        elements = [0]
        seen = {0}
        for i in elements:
            for g in (x, y):
                h = table[i][g]
                if h not in seen:
                    seen.add(h)
                    elements.append(h)
        if len(seen) == (120 if odd[x] else 60):
            assert len(orbit) == 120
            yield perms[x], perms[y], len(seen)


def matching_flows(x, y):
    flows = set()
    for choices in product(range(4), repeat=5):
        rows = []
        edges = 0
        for j, term in enumerate(choices):
            row = j
            if term & 1:
                edges |= 1 << (5 + j)
                row = y[row]
            if term & 2:
                edges |= 1 << row
                row = x[row]
            rows.append(row)
        if len(set(rows)) == 5:
            flows.add(edges)
    return flows


def verify(flows, n, first, mask):
    second = (7 if n == 25 else 10) * first % n
    exponents = [first] * 5 + [second] * 5
    for j in range(10):
        if mask & (1 << j):
            exponents[j] -= n
    costs = [sum(value for j, value in enumerate(exponents) if flow & (1 << j))
             for flow in flows]
    low, high = min(costs), max(costs)
    assert costs.count(low) == 1 or costs.count(high) == 1
    assert 4 * (high - low) < 5 * n
    return high - low


def main():
    certs = {}
    for line in CERTIFICATES.splitlines():
        x, y, *values = line.split()
        key = (tuple(map(int, x)), tuple(map(int, y)))
        assert key not in certs
        certs[key] = list(map(int, values))
    counts = Counter()
    maxima = {}
    for x, y, size in groups_and_orbits():
        c25, mask25, c26, mask26 = certs.pop((x, y))
        flows = matching_flows(x, y)
        for n, c, mask in ((25, c25, mask25), (26, c26, mask26)):
            if n == 25 and size == 120:
                assert c == mask == 0
                continue
            width = verify(flows, n, c, mask)
            key = n, size
            counts[key] += 1
            maxima[key] = max(maxima.get(key, 0), width)
    assert not certs
    assert counts == {(25, 60): 19, (26, 60): 19, (26, 120): 19}
    assert maxima == {(25, 60): 23, (26, 60): 29, (26, 120): 31}
    for key in sorted(counts):
        print(key, "orbits", counts[key], "largest spread", maxima[key])


if __name__ == "__main__":
    main()

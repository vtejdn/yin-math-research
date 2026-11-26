"""Check the two-step transfer support for all ordered generating pairs of A5."""

from collections import Counter
from itertools import permutations


def alternating_table():
    elements = []
    for perm in permutations(range(5)):
        inversions = sum(perm[i] > perm[j] for i in range(5) for j in range(i + 1, 5))
        if inversions % 2 == 0:
            elements.append(perm)
    index = {perm: i for i, perm in enumerate(elements)}
    assert elements[0] == tuple(range(5)) and len(elements) == 60
    return [[index[tuple(left[i] for i in right)] for right in elements] for left in elements]


def powers(table, element):
    result = [0]
    value = element
    while value != 0:
        result.append(value)
        value = table[value][element]
    return result


def generates(table, a, b):
    queue = [0]
    seen = {0}
    for vertex in queue:
        for generator in (a, b):
            target = table[vertex][generator]
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return len(queue) == len(table)


def main():
    table = alternating_table()
    cyclic = [powers(table, g) for g in range(60)]
    counts = Counter()
    for x in range(60):
        x_inverse = cyclic[x][-1]
        fourth = cyclic[x][4 % len(cyclic[x])]
        for y in range(60):
            if not generates(table, x, y):
                continue
            key = (len(cyclic[x]), len(cyclic[y]))
            counts[key, "generate"] += 1
            orbit = [y]
            for _ in range(3):
                orbit.append(table[table[x][orbit[-1]]][x_inverse])
            if not generates(table, orbit[0], orbit[1]):
                continue
            counts[key, "adjacent"] += 1
            c0, c1, c2, c3 = (cyclic[element] for element in orbit)
            assert set(c0) & set(c1) == {0}
            right = {table[table[a][b]][fourth] for a in c2 for b in c3}
            full = all(table[a][b] in right for a in c1[1:] for b in c0[1:])
            if full:
                counts[key, "full"] += 1
            has_sign = any(
                all(table[c1[sign]][b] in right for b in c0[1:])
                and all(table[a][c0[sign]] in right for a in c1[1:])
                for sign in (1, -1)
            )
            if has_sign:
                counts[key, "sign"] += 1
                if 0 in right:
                    counts[key, "sign and identity"] += 1

    columns = ("generate", "adjacent", "full", "sign", "sign and identity")
    rows = {key: tuple(counts[key, c] for c in columns) for key, c in counts}
    expected = {
        (2, 3): (120, 120, 0, 0, 0), (2, 5): (240, 240, 0, 0, 0),
        (3, 2): (120, 0, 0, 0, 0), (3, 3): (120, 0, 0, 0, 0),
        (3, 5): (480, 480, 0, 240, 0), (5, 2): (240, 0, 0, 0, 0),
        (5, 3): (480, 240, 0, 240, 0), (5, 5): (480, 480, 0, 240, 0),
    }
    assert rows == expected
    print("orders:", ", ".join(columns))
    for key, row in sorted(rows.items()):
        print(key, row)
    totals = tuple(map(sum, zip(*rows.values())))
    assert totals == (2280, 1560, 0, 720, 0)
    print("total", totals)


if __name__ == "__main__":
    main()

"""Check the primitive-25 simple character certificates with exact integers."""
OFFSETS = (0, 1, 7, 8)
# Keys (x,y) stand for X^4+x X^3+y X^2+x X+1.
# Values are the first orbit coordinates and the cyclic shift exponent.
QUARTIC = {
    7: {
        (2, 4): ((0, 1, 1, 0), 0),
        (4, 0): ((0, 5, 1, 0), 0),
        (4, 3): ((0, 0, 4, 1), 1),
        (5, 5): ((0, 1, 2, 1), 0),
        (6, 5): ((0, 3, 2, 0), 0),
    },
    43: {
        (3, 21): ((0, 1, 0, 0), 0),
        (7, 26): ((-1, 1, 0, 0), 0),
        (19, 42): ((-3, 1, 0, 0), 0),
        (24, 12): ((0, 1, 0, 0), 0),
        (33, 38): ((0, 1, 0, 0), 0),
    },
}
# Keys are the linear coefficients of monic reciprocal quadratics at 149.
QUADRATIC = {
    39: ((6, 1), 0), 49: ((-2, 1), 1), 55: ((3, 1), 0),
    75: ((5, 1), 0), 90: ((-4, 1), 0), 97: ((2, 1), 0),
    106: ((1, 1), 1), 120: ((2, 1), 0), 129: ((-3, 1), 0),
    134: ((1, 1), 0),
}


def data(p):
    if p in QUARTIC:
        return [((1, x, y, x, 1), v, a) for (x, y), (v, a) in QUARTIC[p].items()]
    if p == 149:
        return [((1, x, 1), v, a) for x, (v, a) in QUADRATIC.items()]
    assert p == 101
    return [((-r % p, 1), (1,), 0) for r in range(1, p)
            if pow(r, 25, p) == 1 and pow(r, 5, p) != 1]


def product_mod(f, g, p):
    h = [0] * (len(f) + len(g) - 1)
    for i, x in enumerate(f):
        for j, y in enumerate(g):
            h[i + j] = (h[i + j] + x * y) % p
    return h


def optimal_dual(costs, penalty):
    """Find a matching and dual prices by successive shortest augmentations."""
    n = len(costs)
    u, v = [0] * (n + 1), [0] * (n + 1)
    owner, prev = [0] * (n + 1), [0] * (n + 1)
    for i in range(1, n + 1):
        owner[0], row = i, 0
        gaps, used = [None] * (n + 1), set()
        while True:
            used.add(row)
            col = owner[row]
            for j in range(1, n + 1):
                if j not in used:
                    reduced = costs[col - 1].get(j - 1, penalty) - u[col] - v[j]
                    if gaps[j] is None or reduced < gaps[j]:
                        gaps[j], prev[j] = reduced, row
            new_row = min((j for j in range(1, n + 1) if j not in used),
                          key=gaps.__getitem__)
            delta = gaps[new_row]
            for j in used:
                u[owner[j]] += delta
                v[j] -= delta
            for j in range(1, n + 1):
                if j not in used:
                    gaps[j] -= delta
            row = new_row
            if not owner[row]:
                break
        while row:
            owner[row], row = owner[prev[row]], prev[row]
    return [i - 1 for i in owner[1:]], u[1:], v[1:]


def verify(p, f, vector, a):
    d = len(f) - 1
    assert len(vector) == d and any(x % p for x in vector)
    e = [x % p for x in vector]
    while len(e) < 25 + d:
        start = len(e) - d
        e.append(-sum(f[j] * e[start + j] for j in range(d)) % p)
    assert e[25:] == e[:d]
    modulus = 25 * p
    b = [((7 * a * p + 25 * x + modulus // 2) % modulus) - modulus // 2 for x in e[:25]]
    width = 25 * abs(a) * p + sum(map(abs, b))
    assert 2 * width * 505 <= 236*625 * p
    costs = [{(i + k) % 25: (j % 2) * a * p + (j // 2) * b[i]
              for j, k in enumerate(OFFSETS)} for i in range(25)]
    penalty = 51 * max(abs(x) for row in costs for x in row.values()) + 1
    owner, u, v = optimal_dual(costs, penalty)
    assert set(owner) == set(range(25))
    assert all(costs[i][row] == u[i] + v[row] for row, i in enumerate(owner))
    assert all(c >= u[i] + v[j] for i, row in enumerate(costs) for j, c in row.items())
    tight = [{j for j, c in row.items() if c == u[i] + v[j]}
             for i, row in enumerate(costs)]
    reach = [{owner[j] for j in row} for row in tight]
    for k in range(25):
        for i in range(25):
            if k in reach[i]:
                reach[i].update(reach[k])
    blocks = {tuple(j for j in sorted(targets) if i in reach[j])
              for i, targets in enumerate(reach)}
    for block in blocks:
        assert len(block) in (1, 2)
        if len(block) == 2:
            rows = {j for j, i in enumerate(owner) if i in block}
            assert all(rows <= tight[i] for i in block)
            offsets = [sorted((j - i) % 25 for j in rows) for i in block]
            assert sorted(offsets) == [[0, 1], [7, 8]]
    return width


def main():
    expected = {7: (5, 959), 43: (5, 5925), 101: (20, 14750), 149: (10, 21100)}
    for p, (number, largest_width) in expected.items():
        rows, product, widths = data(p), [1], []
        assert len(rows) == number
        for f, vector, a in rows:
            degree = len(f) - 1
            assert pow(p, degree, 25) == 1
            assert all(pow(p, i, 25) != 1 for i in range(1, degree))
            product = product_mod(product, f, p)
            widths.append(verify(p, f, vector, a))
        assert product == [int(i % 5 == 0) for i in range(21)]
        assert max(widths) == largest_width
        print(f"p={p}: all {number} factors checked, maximum block width {max(widths)}")


if __name__ == "__main__":
    main()

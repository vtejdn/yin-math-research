"""Check the five-coordinate certificates for the noncyclic order-twenty marking."""

from itertools import product


def matching_flows():
    flows = set()
    for choices in product(range(4), repeat=5):
        rows = set()
        used = 0
        for column, choice in enumerate(choices):
            row = column
            if choice & 1:
                used |= 1 << (5 + column)
                row = (row + 2) % 5
            if choice & 2:
                used |= 1 << row
                row = (row + 1) % 5
            rows.add(row)
        if len(rows) == 5:
            flows.add(used)
    assert len(flows) == 24
    return flows


# Fields are the primitive roots, cyclic character (a,b), multiplier,
# and the two expected extremal costs.
CERTIFICATES = {
    11: [((3, 4), -1, -2, 1, -80, 25),
         ((5, 9), -1, 3, 2, -55, 55)],
    41: [((10, 37), -1, -2, 1, -260, 55),
         ((16, 18), -1, -2, 5, -260, 55)],
    61: [((9, 34), 0, 5, 10, -350, 45),
         ((20, 58), -1, -2, 1, -350, 45)],
    101: [((36, 87), 0, 0, 1, -360, 360),
          ((84, 95), 0, 0, 5, -360, 360)],
}


def check(flows, prime, a, b, orbit, lower, upper):
    assert (b - 2 * a) % 5 == 0
    period = 10 * prime
    weights = [prime * a] * 5
    for entry in orbit:
        weights.append((prime * b + 10 * entry + period // 2) % period - period // 2)
    costs = [sum(weight for edge, weight in enumerate(weights) if mask & (1 << edge))
             for mask in flows]
    assert (min(costs), max(costs)) == (lower, upper)
    assert costs.count(lower) == costs.count(upper) == 1
    assert 4 * (upper - lower) < 5 * period
    return upper - lower


def main():
    flows = matching_flows()
    ternary = (0, 0, 1, 1, 1)
    assert sum(ternary) % 3 == 0 and any(ternary)
    print(3, check(flows, 3, -1, -2, ternary, -20, 5))
    for prime, records in CERTIFICATES.items():
        checked = []
        widths = []
        for roots, a, b, multiplier, lower, upper in records:
            for root in roots:
                orbit = tuple(multiplier * pow(root, i, prime) % prime for i in range(5))
                widths.append(check(flows, prime, a, b, orbit, lower, upper))
                checked.append(root)
        assert sorted(checked) == [r for r in range(2, prime) if pow(r, 5, prime) == 1]
        print(prime, max(widths))


if __name__ == "__main__":
    main()

"""Verify both ten-site networks at the exceptional fifth-orbit primes."""

from fractions import Fraction


# Each split row gives the roots, the abelian weights, the multiplier on the
# fifth-root orbit, the change by one period at index zero, and the two costs.
SPLIT = {
    2: {
        11: [((3, 4), -1, -2, 1, 0, -160, 50),
             ((5, 9), -1, 3, 1, 0, -165, 55)],
        41: [((10, 37), 0, -5, 6, 1, -115, 525),
             ((16, 18), 0, -5, 6, 1, -135, 545)],
        61: [((9, 34), -1, -2, 43, 1, -710, 100),
             ((20, 58), 0, -5, 10, 1, -150, 760)],
        101: [((36, 87), -1, -2, 71, 1, -1240, 230),
              ((84, 95), -1, -2, 3, 0, -1270, 260)],
    },
    3: {
        11: [((3, 4), 0, -5, 1, 1, -50, 160),
             ((5, 9), 0, -5, 1, 0, -95, 95)],
        41: [((10, 37), 0, -5, 3, 0, -245, 245),
             ((16, 18), 0, -5, 6, 0, -245, 245)],
        61: [((9, 34), 0, -5, 10, 0, -405, 405),
             ((20, 58), 0, -5, 10, 0, -375, 375)],
        101: [((36, 87), 0, -5, 10, 0, -545, 545),
              ((84, 95), 0, -5, 26, 0, -545, 545)],
    },
}
TERNARY = {
    2: (0, -5, (1, 1, 1, 2, 1), 1, -15, 45),
    3: (-1, 2, (0, 0, 0, 1, 2), 0, -40, 10),
}


def matching_flows(step):
    flows = []
    for mask in range(1 << 10):
        second = tuple((mask >> i) & 1 for i in range(10))
        for initial in (0, 1):
            previous = initial
            first = []
            for i in range(10):
                current = previous + second[(i - step) % 10] - second[i]
                if current not in (0, 1):
                    break
                first.append(current)
                previous = current
            if len(first) == 10 and previous == initial:
                flows.append((tuple(first), second))
    assert len(set(flows)) == len(flows) == {2: 248, 3: 216}[step]
    return flows


def check(step, flows, prime, a, b, orbit, correction, lower, upper):
    assert (b - step * a) % 5 == 0
    assert len(orbit) == 5 and any(orbit) and sum(orbit) % prime == 0
    period = 10 * prime
    weights = []
    for i in range(10):
        exponent = (1 if i % 2 == 0 else -1) * orbit[i % 5]
        value = prime * b + 10 * exponent
        weights.append((value + period // 2) % period - period // 2)
    weights[0] += correction * period
    costs = [prime * a * sum(first) + sum(w * n for w, n in zip(weights, second))
             for first, second in flows]
    assert (min(costs), max(costs)) == (lower, upper)
    assert costs.count(lower) == costs.count(upper) == 1
    ratio = Fraction(upper - lower, 10 * period)
    assert ratio <= Fraction(1, 5)
    return upper - lower, ratio


def main():
    for step, primes in SPLIT.items():
        flows = matching_flows(step)
        width, ratio = check(step, flows, 3, *TERNARY[step])
        widths = {3: width}
        ratios = [ratio]
        for prime, records in primes.items():
            values = []
            seen = []
            for roots, a, b, multiplier, correction, lower, upper in records:
                for root in roots:
                    orbit = tuple(multiplier * pow(root, i, prime) % prime for i in range(5))
                    width, ratio = check(step, flows, prime, a, b, orbit, correction, lower, upper)
                    seen.append(root)
                    values.append(width)
                    ratios.append(ratio)
            assert sorted(seen) == [r for r in range(2, prime) if pow(r, 5, prime) == 1]
            widths[prime] = max(values)
        assert len(ratios) == 17
        print(f"step {step}: {len(flows)} flows, {len(ratios)} cases, widths {widths}, max {max(ratios)}")


if __name__ == "__main__":
    main()

"""Verify the finite split-prime and mixed-phase certificates for order five."""
from itertools import permutations
from math import isqrt


def primes_to(limit):
    prime = bytearray([1]) * (limit + 1)
    prime[:2] = bytes(2)
    for k in range(2, isqrt(limit) + 1):
        if prime[k]:
            for j in range(k * k, limit + 1, k):
                prime[j] = 0
    return [k for k in range(2, limit + 1) if prime[k]]


def fifth_root(p):
    for x in range(2, p):
        r = pow(x, (p - 1) // 5, p)
        if r != 1:
            return r
    raise AssertionError("no primitive fifth root")


def has_age_one(p, r):
    root_powers = [pow(r, i, p) for i in range(5)]
    for c in range(1, p):
        if sum(c * x % p for x in root_powers) == p:
            return True
    return False


def data(p, r):
    if p == 11:
        return 1, 2, 307
    if p == 41:
        return 2, 6, 1061
    if p == 61 and r in (9, 34):
        return 1, 5, 1161
    if p == 61 and r in (20, 58):
        return 2, 10, 1639
    if p == 101:
        return 1, 38, 2198
    raise AssertionError((p, r))


def check_mixed(p, r):
    a, c, expected_width = data(p, r)
    modulus = 25 * p
    for short_a in range(-6, 7):
        for multiplier in range(1, p):
            positive = [(7 * short_a * p + 25 * multiplier * pow(r, i, p)) % modulus
                        for i in range(5)]
            assert 0 not in positive
            for t_width in (sum(positive), 5 * modulus - sum(positive)):
                width = 5 * abs(short_a) * p + t_width
                assert 4 * width >= 125 * p
    b = [(7 * a * p + 25 * c * pow(r, i, p)) % modulus for i in range(5)]
    b = [v if 2 * v < modulus else v - modulus for v in b]
    width = 5 * a * p + sum(map(abs, b))
    assert width == expected_width and 4 * width < 125 * p
    assert 2 * width * 1375 <= 614 * 125 * p
    costs = {}
    for rows in permutations(range(5)):
        arrows = tuple((row - i) % 5 for i, row in enumerate(rows))
        if 4 not in arrows:
            costs[arrows] = sum((k % 2) * a * p + (k // 2) * b[i]
                                for i, k in enumerate(arrows))
    minimum = min(costs.values())
    opt = [arrows for arrows, cost in costs.items() if cost == minimum]
    if p in (61, 101):
        assert len(opt) == 1
        return
    assert len(opt) == 2
    differing = [set(pair) for pair in zip(*opt) if pair[0] != pair[1]]
    assert len(differing) == 2 and {0, 1} in differing and {2, 3} in differing


def main():
    primes = [p for p in primes_to(18**4) if p % 5 == 1]
    residual = [p for p in primes if not has_age_one(p, fifth_root(p))]
    assert len(primes) == 2491 and residual == [11, 41, 61, 101]
    for p in residual:
        root = fifth_root(p)
        for j in range(1, 5):
            check_mixed(p, pow(root, j, p))
    print("2491 split primes; four age-one exceptions; all 16 marked checks pass.")


if __name__ == "__main__":
    main()

"""Verify the eighth-root module estimates for the cyclic marking (1,6)."""

from fractions import Fraction
from math import isqrt


def odd_primes(limit):
    flags = bytearray([1]) * (limit + 1)
    for n in range(2, isqrt(limit) + 1):
        if flags[n]:
            flags[n * n::n] = bytes((limit - n * n) // n + 1)
    return [p for p in range(3, limit + 1, 2) if flags[p]]


def primitive_eighth_root(prime):
    for a in range(2, prime):
        root = pow(a, (prime - 1) // 8, prime)
        if pow(root, 4, prime) == prime - 1:
            return root
    raise AssertionError(prime)


def quartic_factors(prime):
    # x^4+1 modulo x^2-a*x+b has coefficients a^3-2ab and b^2-a^2b+1.
    factors = [(a, b) for b in range(1, prime) for a in range(prime)
               if (a**3 - 2*a*b) % prime == 0 and (b*b - a*a*b + 1) % prime == 0]
    assert len(factors) == 2
    return factors


def middle(value, prime):
    return 3 * prime < 8 * (value % prime) < 5 * prime


def remaining_modules():
    split, quadratic = [], []
    split_primes = quadratic_primes = 0
    for p in odd_primes(16**4):
        if p % 8 == 1:
            split_primes += 1
            r = primitive_eighth_root(p)
            powers = [pow(r, i, p) for i in range(4)]
            # The four negatives are in the same symmetric interval.
            if not any(all(middle(c*j, p) for j in powers)
                       for c in range(3*p//8 + 1, 5*p//8 + 1)):
                split.append((p, r))
        elif p*p <= 16**4:
            quadratic_primes += 1
            for a, b in quartic_factors(p):
                interval = range(3*p//8 + 1, 5*p//8 + 1)
                if not any(middle(a*y - b*x, p) and middle(a*(a*y-b*x) - b*y, p)
                           for x in interval for y in interval):
                    quadratic.append((p, a, b))
    assert (split_primes, quadratic_primes, len(split), len(quadratic)) == (1614, 43, 41, 14)
    return split, quadratic


def flows():
    found = []
    for mask in range(256):
        n = [(mask >> i) & 1 for i in range(8)]
        for initial in (0, 1):
            m = []
            previous = initial
            for i in range(8):
                previous += n[(i-6) % 8] - n[i]
                if previous not in (0, 1):
                    break
                m.append(previous)
            if len(m) != 8 or previous != initial:
                continue
            singletons = {n[(i-6) % 8] + 2*m[i] for i in range(8)
                          if 1 - n[i] + n[(i-6) % 8] == 1}
            found.append((sum(m), tuple(i for i in range(8) if n[i]), singletons))
    assert len(found) == 96
    return found


def certify(prime, orbit_lists, possible):
    period = 16 * prime
    covered = {}
    for a in range(9):
        for orbit in orbit_lists:
            weights = [(6*a*prime + 16*entry + period//2) % period - period//2
                       for entry in orbit]
            base = [a*prime*count + sum(weights[i] for i in used)
                    for count, used, _ in possible]
            for change in (0, 1, -1):
                costs = [v + (change*period if 0 in flow[1] else 0)
                         for v, flow in zip(base, possible)]
                low, high = min(costs), max(costs)
                if 48*(high-low) > 11*8*period:
                    continue
                for end in (low, high):
                    if costs.count(end) != 1:
                        continue
                    singletons = possible[costs.index(end)][2]
                    for missing in (1, 2):  # input hypothesis may omit A or D
                        if missing not in singletons:
                            covered.setdefault(missing, Fraction(high-low, 8*period))
                if len(covered) == 2:
                    return max(covered.values())
    raise AssertionError((prime, covered))


def main():
    split, quadratic = remaining_modules()
    possible = flows()
    ratios = []
    for p, root in split:
        for exponent in (1, 3, 5, 7):
            r = pow(root, exponent, p)
            powers = [pow(r, j, p) for j in range(8)]
            orbits = [tuple(c*v % p for v in powers) for c in range(1, p)]
            ratios.append(certify(p, orbits, possible))
    for p, a, b in quadratic:
        orbits = []
        for x in range(p):
            for y in range(p):
                if x or y:
                    values = [x, y]
                    while len(values) < 8:
                        values.append((a*values[-1] - b*values[-2]) % p)
                    assert all((values[i+4]+values[i]) % p == 0 for i in range(4))
                    orbits.append(values)
        ratios.append(certify(p, orbits, possible))
    assert len(ratios) == 178 and max(ratios) == Fraction(11, 48)
    print("1614 split primes, 86 quadratic factors; 164 split and 14 quadratic residual markings.")
    print("96 edge-set pairs; both possible missing corners certified; maximum 11/48.")


if __name__ == "__main__":
    main()

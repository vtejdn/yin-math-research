"""Check the quartic order-25 periods and the positive orbit certificates."""
from math import isqrt


CUTOFF = 18**5
PERIOD_POLYNOMIAL = [1, 10, 5, -10, 0, 1]  # ascending powers


def verify_period_polynomial():
    """Form the product over the five cosets in Z[C25][Y], then impose Phi_25."""
    subgroup = (1, 7, 18, 24)
    seen = set()
    coefficients = [[1] + [0] * 24]
    for k in range(1, 25):
        if k % 5 == 0 or k in seen:
            continue
        coset = [(k * h) % 25 for h in subgroup]
        seen.update(coset)
        product = [[0] * 25 for _ in range(len(coefficients) + 1)]
        for degree, vector in enumerate(coefficients):
            for i, value in enumerate(vector):
                product[degree + 1][i] += value
                for n in coset:
                    product[degree][(i + n) % 25] -= value
        coefficients = product
    assert len(coefficients) == 6 and len(seen) == 20
    for vector, expected in zip(coefficients, PERIOD_POLYNOMIAL):
        reduced = [vector[i] - vector[20 + i % 5] for i in range(20)]
        assert reduced == [expected] + [0] * 19


def trim(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    return poly


def divide(poly, divisor, p):
    """Division by a monic polynomial in ascending coefficient order."""
    assert divisor[-1] == 1
    remainder = poly.copy()
    quotient = [0] * max(0, len(poly) - len(divisor) + 1)
    for i in reversed(range(len(quotient))):
        factor = remainder.pop()
        quotient[i] = factor
        for j, coeff in enumerate(divisor[:-1]):
            remainder[i + j] = (remainder[i + j] - factor * coeff) % p
    return trim(quotient), trim(remainder)


def monic(poly, p):
    scale = pow(poly[-1], -1, p)
    return [v * scale % p for v in poly]


def gcd(first, second, p):
    while second:
        second = monic(second, p)
        first, second = second, divide(first, second, p)[1]
    return monic(first, p)


def power_of_shift(shift, exponent, modulus, p):
    def multiply(first, second):
        product = [0] * (len(first) + len(second) - 1)
        for i, x in enumerate(first):
            for j, y in enumerate(second):
                product[i + j] += x * y
        return divide(trim([c % p for c in product]), modulus, p)[1]

    base = [shift, 1]
    result = [1]
    while exponent:
        if exponent % 2:
            result = multiply(result, base)
        base = multiply(base, base)
        exponent //= 2
    return result


def roots(poly, p):
    if len(poly) == 2:
        return [-poly[0] % p]
    for shift in range(p):
        power = power_of_shift(shift, (p - 1) // 2, poly, p) or [0]
        power[0] = (power[0] - 1) % p
        factor = gcd(poly, trim(power), p)
        if 1 < len(factor) < len(poly):
            quotient, remainder = divide(poly, factor, p)
            assert not remainder
            return roots(factor, p) + roots(quotient, p)
    raise AssertionError(("no proper split", p, poly))


def quartic_primes():
    prime = bytearray([1]) * (CUTOFF + 1)
    prime[:2] = bytes(2)
    for i in range(2, isqrt(CUTOFF) + 1):
        if prime[i]:
            count = (CUTOFF - i * i) // i + 1
            prime[i * i::i] = bytes(count)
    return [p for p in range(2, CUTOFF + 1) if prime[p] and p % 25 in (7, 18)]


def verify_multiplier(p):
    poly = [c % p for c in PERIOD_POLYNOMIAL]
    values = roots(poly, p)
    assert len(values) == len(set(values)) == 5
    for x in values:
        assert x and sum(c * pow(x, i, p) for i, c in enumerate(poly)) % p == 0
    for m in range(1, (p + 1) // 2):
        c = p - m
        if sum(c * x % p for x in values) == p:
            assert 4 * c > 3 * p
            return True
    return False


def verify_functional(p, factor, initial):
    cyclotomic = [int(i % 5 == 0) for i in range(21)]
    assert len(factor) == 5 and not divide(cyclotomic, factor, p)[1]
    assert pow(p, 2, 25) == 24
    orbit = list(initial)
    for i in range(25):
        orbit.append(-sum(factor[j] * orbit[i + j] for j in range(4)) % p)
    assert orbit[25:] == list(initial)
    assert all(0 < e < p for e in orbit[:25])
    assert all(sum(orbit[i:25:5]) == p for i in range(5))


def main():
    verify_period_polynomial()
    primes = quartic_primes()
    assert len(primes) == 14140 and primes[0] == 7
    exceptions = [p for p in primes if p != 7 and not verify_multiplier(p)]
    assert exceptions == [43, 157]
    verify_functional(43, [1, 3, 21, 3, 1], [1, 3, 2, 11])
    verify_functional(157, [1, 6, 45, 6, 1], [1, 7, 19, 2])
    print("14140 quartic primes through 18^5; 7 set aside; "
          "14137 trace witnesses; 43 and 157 verified by recurrence.")


if __name__ == "__main__":
    main()

"""Test the order-three upper bound and the remaining order-24 simple markings."""
from itertools import product

from verify_middle_terms import frequency, phase_norms


def residue(poly, factor, p):
    values = poly.copy()
    d = len(factor) - 1
    for i in range(len(values) - 1, d - 1, -1):
        for j in range(d):
            values[i - d + j] = (values[i - d + j] - values[i] * factor[j]) % p
    return tuple(v % p for v in values[:d])


def marked_factors(p):
    phi = [1, 0, 0, 0, -1, 0, 0, 0, 1]
    degree = next(k for k in range(1, 9) if pow(p, k, 24) == 1)
    factors = []
    whole = [1]
    for coefficients in product(range(p), repeat=degree):
        factor = coefficients + (1,)
        if any(residue(phi, factor, p)):
            continue
        factors.append(factor)
        updated = [0] * (len(whole) + degree)
        for i, a in enumerate(whole):
            for j, b in enumerate(factor):
                updated[i + j] = (updated[i + j] + a * b) % p
        whole = updated
    assert whole == [v % p for v in phi]
    assert len(factors) * degree == 8
    return factors


def isolated(p, factor, steps):
    path = [0]
    for k in steps:
        path.append((path[-1] + 4 * k - 3) % 24)
    a, b, c, d = path
    chosen = residue(frequency(24, path), factor, p)
    if not any(chosen):
        return False
    for i in range(b % 4, 24, 4):
        for j in range(c % 4, 24, 4):
            if (i, j) != (b, c) and residue(frequency(24, (a, i, j, d)), factor, p) == chosen:
                return False
    return True


def main():
    for path in ((0, 1, 1, 2), (0, 2, 2, 1)):
        values = phase_norms(3, 1, [1, 1, 1], path)
        assert set(values) == {1, 3, 9, 12}
        print(f"r=3, {path}: {values}")
    for p in (7, 73, 97, 193):
        factors = marked_factors(p)
        for factor in factors:
            for full in (1, 5):
                triples = (s for s in product(range(1, 6), repeat=3) if s.count(full) >= 2)
                assert any(isolated(p, factor, steps) for steps in triples), (p, factor, full)
        print(f"p={p}: {len(factors)} factors, both full-block choices certified.")
    for factor in marked_factors(5):
        assert not any(isolated(5, factor, steps) for steps in product(range(6), repeat=3))
    print("p=5: on all four quadratics, no three-step path has an isolated nonconstant frequency.")


if __name__ == "__main__":
    main()

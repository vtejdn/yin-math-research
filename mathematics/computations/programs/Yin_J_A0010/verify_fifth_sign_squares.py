"""Classify bidegree-(2,2) two-point constraints on five sign squares."""

from collections import Counter
from functools import lru_cache, reduce
from itertools import combinations, product
from math import gcd

PRIME = 101
ROOT = 36
POWERS = tuple(pow(ROOT, i, PRIME) for i in range(5))
assert pow(ROOT, 5, PRIME) == 1 and len(set(POWERS)) == 5
MONOMIALS = tuple(product(range(3), repeat=2))
CORNERS = tuple(i for i, (a, b) in enumerate(MONOMIALS) if a != 1 and b != 1)
PAIRS = tuple(combinations(range(4), 2))

# A row entry (a,k) is the algebraic integer a*zeta^k.
SQUARES = tuple(
    tuple(
        tuple((sx**a * sy**b, i*(a+2*b) % 5) for a, b in MONOMIALS)
        for sx, sy in product((1, -1), repeat=2)
    )
    for i in range(5)
)
JET = (
    SQUARES[0][0],
    tuple((a, 0) for a, b in MONOMIALS),
    tuple((b, 0) for a, b in MONOMIALS),
)
ZERO = (0, 0, 0, 0, 0)
ONE = (1, 0, 0, 0, 0)


def reduced(coeffs):
    """Canonical representative of an element of Z[zeta_5], last entry zero."""
    return tuple(value - coeffs[4] for value in coeffs)


def add_monomial_multiple(target, source, scalar, exponent):
    for i, value in enumerate(source):
        target[(i + exponent) % 5] += scalar * value


def multiply(left, right):
    values = [0] * 5
    for i, scalar in enumerate(left):
        if scalar:
            add_monomial_multiple(values, right, scalar, i)
    return reduced(values)


def conjugate(value, degree):
    result = [0] * 5
    for i, component in enumerate(value):
        result[(degree * i) % 5] = component
    return reduced(result)


def eval_row(row, vector):
    result = [0] * 5
    for (scalar, exponent), entry in zip(row, vector):
        add_monomial_multiple(result, entry, scalar, exponent)
    return reduced(result)


@lru_cache(None)
def mod_row(row):
    return tuple(scalar * POWERS[exponent] % PRIME for scalar, exponent in row)


def modular_pivots(rows):
    matrix = [list(mod_row(row)) for row in rows]
    indices = list(range(len(rows)))
    columns = []
    for j in range(9):
        n = len(columns)
        pivot = next((i for i in range(n, len(rows)) if matrix[i][j]), None)
        if pivot is None:
            continue
        matrix[n], matrix[pivot] = matrix[pivot], matrix[n]
        indices[n], indices[pivot] = indices[pivot], indices[n]
        factor = pow(matrix[n][j], -1, PRIME)
        for i in range(n + 1, len(rows)):
            multiplier = matrix[i][j] * factor % PRIME
            if multiplier:
                for k in range(j, 9):
                    matrix[i][k] = (matrix[i][k] - multiplier * matrix[n][k]) % PRIME
        columns.append(j)
    return indices[:len(columns)], columns


def cofactor_vector(rows, columns, free):
    """A signed minor vector for M[:, columns + free] over the cyclotomic ring."""
    active = sorted([*columns, free])
    wedge = {0: ONE}
    for row in rows:
        new = {}
        for mask, coeff in wedge.items():
            for j, column in enumerate(active):
                scalar, exponent = row[column]
                if not scalar or (mask >> j) & 1:
                    continue
                target = new.setdefault(mask | (1 << j), [0] * 5)
                if (mask >> (j + 1)).bit_count() % 2:
                    scalar = -scalar
                add_monomial_multiple(target, coeff, scalar, exponent)
        wedge = new
    full = (1 << len(active)) - 1
    vector = [ZERO] * 9
    for j, column in enumerate(active):
        minor = reduced(wedge.get(full ^ (1 << j), ZERO))
        vector[column] = tuple((-x if j % 2 else x) for x in minor)
    assert vector[free] != ZERO
    return vector


def exact_kernel(rows, row_indices, columns):
    # The selected pivot minor is nonzero mod 101, hence nonzero in characteristic
    # zero. Signed cofactors give a basis of the selected row kernel over Q(zeta).
    selected = [rows[i] for i in row_indices]
    basis = [cofactor_vector(selected, columns, j) for j in range(9) if j not in columns]
    # Intersect with all remaining exact row kernels, even if the reduction
    # has smaller rank than the characteristic-zero system.
    for i, row in enumerate(rows):
        if i in row_indices or not basis:
            continue
        residuals = [eval_row(row, v) for v in basis]
        pivot = next((j for j, value in enumerate(residuals) if value != ZERO), None)
        if pivot is None:
            continue
        chosen, factor = basis[pivot], residuals[pivot]
        others = []
        for j, v in enumerate(basis):
            if j == pivot:
                continue
            value = residuals[j]
            new = []
            for component, ref in zip(v, chosen):
                first = multiply(factor, component)
                second = multiply(value, ref)
                new.append(tuple(a-b for a, b in zip(first, second)))
            others.append(new)
        basis = others
    assert all(eval_row(row, v) == ZERO for row in rows for v in basis)
    return basis


def projective_key(vector):
    """Scale by conjugates of the first nonzero entry, then use an integer gcd."""
    first = next(entry for entry in vector if entry != ZERO)
    factor = ONE
    for degree in (2, 3, 4):
        factor = multiply(factor, conjugate(first, degree))
    norm = multiply(factor, first)
    assert norm[0] > 0 and all(value == 0 for value in norm[1:])
    key = tuple(x for entry in vector for x in multiply(factor, entry)[:4])
    divisor = reduce(gcd, key, 0)
    return tuple(x // divisor for x in key)


def prototype_orbit():
    """The fifth-root rotations, and the order-preserving exchange of the axes."""
    sqrt5 = reduced((1, 2, 0, 0, 2))
    assert multiply(sqrt5, sqrt5) == (5, 0, 0, 0, 0)
    keys = set()
    for sign in (1, -1):
        middle = tuple(sign*x for x in sqrt5)
        normalized = {
            (0, 0): (-1, 0, 0, 0, 0), (0, 1): middle, (0, 2): (-2, 0, 0, 0, 0),
            (2, 0): (2, 0, 0, 0, 0), (2, 1): tuple(-x for x in middle), (2, 2): ONE,
        }
        # The displayed normalized prototype uses x^2=y^4 on the five sign
        # squares. Return to (x,y)=(+/-z,+/-z^2) by reversing the first axis.
        base = {(2-a, b): value for (a, b), value in normalized.items()}
        for phase in range(5):
            rotated = {}
            for (a, b), entry in base.items():
                value = [0] * 5
                add_monomial_multiple(value, entry, 1, phase*(a + 2*b) % 5)
                rotated[a, b] = reduced(value)
            keys.add(projective_key([rotated.get(m, ZERO) for m in MONOMIALS]))
            # x^2 f(y,1/x) sends an exponent pair (a,b) to (2-b,a).
            swapped = {(2-b, a): value for (a, b), value in rotated.items()}
            keys.add(projective_key([swapped.get(m, ZERO) for m in MONOMIALS]))
    assert len(keys) == 20
    return keys


def run(jets):
    start = int(jets)
    counts, reduced_ranks, exact_ranks, points = Counter(), Counter(), Counter(), Counter()
    parity = {}
    for choices in product(PAIRS, repeat=5-start):
        rows = list(JET) if jets else []
        for square, pair in zip(SQUARES[start:], choices):
            rows.extend(square[i] for i in pair)
        indices, columns = modular_pivots(rows)
        reduced_ranks[len(columns)] += 1
        if len(columns) == 9:
            continue
        basis = exact_kernel(rows, indices, columns)
        exact_ranks[9 - len(basis)] += 1
        if not basis or any(all(v[i] == ZERO for v in basis) for i in CORNERS):
            counts["no full corners"] += 1
            continue
        # Over an infinite field the union of the four coordinate hyperplanes
        # covers a kernel only when one hyperplane contains the whole kernel.
        assert len(basis) == 1
        v = basis[0]
        even_x = all(v[i] == ZERO for i, (a, b) in enumerate(MONOMIALS) if a == 1)
        even_y = all(v[i] == ZERO for i, (a, b) in enumerate(MONOMIALS) if b == 1)
        assert even_x or even_y
        key = projective_key(v)
        points[key] += 1
        parity[key] = (even_x, even_y)
        counts["full corners"] += 1

    if jets:
        assert reduced_ranks == {8: 2, 9: 1294}
        assert exact_ranks == {8: 2}
        assert counts == {"no full corners": 2}
    else:
        assert reduced_ranks == {7: 4, 8: 220, 9: 7552}
        assert exact_ranks == {7: 4, 8: 220}
        assert counts == {"no full corners": 104, "full corners": 120}
        assert len(points) == 20 and set(points.values()) == {6}
        assert set(points) == prototype_orbit()
        assert Counter(parity.values()) == {(True, False): 10, (False, True): 10}
    print("jet" if jets else "pair", "modular ranks", sorted(reduced_ranks.items()))
    print("exact ranks of modular survivors", sorted(exact_ranks.items()))
    print("survivors", sorted(counts.items()), "projective points", len(points),
          "multiplicities", dict(Counter(points.values())))
    print("point parities (even x, even y)", dict(Counter(parity.values())))


if __name__ == "__main__":
    run(False)
    run(True)

"""Norms of the four-term relations; coefficients are in ascending order."""
from itertools import product


def times_x(column, phi):
    return [a - column[-1] * b for a, b in zip([0] + column[:-1], phi)]


def determinant(rows):
    """Fraction-free elimination, with row swaps and exact division."""
    n = len(rows)
    previous = sign = 1
    for j in range(n - 1):
        pivot = next((i for i in range(j, n) if rows[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            rows[j], rows[pivot] = rows[pivot], rows[j]
            sign = -sign
        diagonal = rows[j][j]
        for i in range(j + 1, n):
            for k in range(j + 1, n):
                numerator = diagonal * rows[i][k] - rows[i][j] * rows[j][k]
                rows[i][k], remainder = divmod(numerator, previous)
                assert not remainder
        previous = diagonal
    return sign * rows[-1][-1]


def norm(phi, exponents):
    degree = len(phi) - 1
    power = [1] + [0] * (degree - 1)
    vector = [0] * degree
    for i in range(max(exponents) + 1):
        coefficient = exponents.count(i)
        vector = [x + coefficient * y for x, y in zip(vector, power)]
        power = times_x(power, phi)
    columns = []
    for _ in range(degree):
        columns.append(vector)
        vector = times_x(vector, phi)
    return abs(determinant([list(row) for row in zip(*columns)]))


def main():
    cases = [
        (3, [1, 1, 1], 1, {1, 4, 7, 16}),
        (8, [1, 0, 0, 0, 1], 4, {8}),
        (24, [1, 0, 0, 0, -1, 0, 0, 0, 1], 4, {1, 4, 16, 25, 64, 73, 97, 193, 196}),
    ]
    for r, phi, step, expected in cases:
        exponent_sets = [range(j % step, r, step) for j in (1, 2, 3)]
        values = [norm(phi, (0,) + rest) for rest in product(*exponent_sets)]
        assert len(values) == (r // step) ** 3
        assert set(values) == expected
        print(f"r={r}: {len(values)} choices, norms {sorted(expected)}")


if __name__ == "__main__":
    main()

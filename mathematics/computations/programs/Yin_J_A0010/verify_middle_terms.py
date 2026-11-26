"""Check the isolated three-block coefficient at orders six and twelve."""
from itertools import product

from verify_four_terms import determinant, times_x


def norm(phi, coefficients):
    degree = len(phi) - 1
    column = [0] * degree
    for c in reversed(coefficients):
        column = times_x(column, phi)
        column[0] += c
    columns = []
    for _ in range(degree):
        columns.append(column)
        column = times_x(column, phi)
    return abs(determinant([list(row) for row in zip(*columns)]))


def frequency(r, path):
    result = [0] * r
    for index in path:
        result[-index % r] += 1
    return result


def phase_norms(r, step, phi, target):
    first, left, right, last = target
    selected = frequency(r, target)
    values = [norm(phi, selected)]
    mids = product(range(left % step, r, step), range(right % step, r, step))
    for i, j in mids:
        if (i, j) == (left, right):
            continue
        competing = frequency(r, (first, i, j, last))
        values.append(norm(phi, [a - b for a, b in zip(selected, competing)]))
    assert len(values) == 9
    return values


def main():
    cases = [
        (6, 2, [1, -1, 1], [(0, 1, 0, 1), (1, 0, 1, 0)], {3, 9, 12}, 3),
        (12, 4, [1, 0, -1, 0, 1], [(0, 1, 2, 3), (0, 5, 10, 3)], {9, 36}, 9),
    ]
    for r, step, phi, paths, expected, index in cases:
        assert norm(phi, [1, 0, 0, 0, -1]) == index
        for path in paths:
            assert all((j - i + 3) % step == 0 for i, j in zip(path, path[1:]))
            values = phase_norms(r, step, phi, path)
            assert set(values) == expected
            print(f"r={r}, {path}: {values}; norm of 1-X^4 is {index}")


if __name__ == "__main__":
    main()

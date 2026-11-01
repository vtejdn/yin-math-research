"""Exact finite checks for Miy26-U005 and Miy26-U006; Python standard library."""

from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb


def words(alphabet, maximum):
    return [w for n in range(maximum + 1) for w in product(alphabet, repeat=n)]


def wick(w, v):
    out = defaultdict(int)
    for k in range(len(w) + 1):
        suffix = tuple(-a for a in reversed(w[k:]))
        if v[:len(suffix)] == suffix:
            out[w[:k] + v[len(suffix):]] += 1
    return {w: a for w, a in out.items() if a}


def right_annihilate(polynomial, letter):
    return {w[:-1]: a for w, a in polynomial.items() if w and w[-1] == letter}


def subtract(left, right):
    out = defaultdict(int, left)
    for w, a in right.items():
        out[w] -= a
    return {w: a for w, a in out.items() if a}


def matvec(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def determinant(matrix):
    matrix = [[F(a) for a in row] for row in matrix]
    result = F(1)
    for i in range(len(matrix)):
        pivot = next((j for j in range(i, len(matrix)) if matrix[j][i]), None)
        if pivot is None:
            return F(0)
        if pivot != i:
            matrix[pivot], matrix[i] = matrix[i], matrix[pivot]
            result = -result
        a = matrix[i][i]
        result *= a
        for j in range(i + 1, len(matrix)):
            ratio = matrix[j][i] / a
            for h in range(i + 1, len(matrix)):
                matrix[j][h] -= ratio * matrix[i][h]
    return result


counts = defaultdict(int)

for d in (1, 2):
    alphabet = tuple(range(1, d + 1)) + tuple(range(-d, 0))
    for w in words(alphabet, 4):
        for v in words(alphabet, 3):
            for i in range(1, d + 1):
                left = right_annihilate(wick(w, v), -i)
                right = wick(w, v[:-1]) if v and v[-1] == -i else {}
                suffix = (-i,) + tuple(-a for a in reversed(v))
                expected = {w[:-len(suffix)]: 1} if w[-len(suffix):] == suffix else {}
                assert subtract(left, right) == expected, (d, w, v, i)
                counts["mixed_word_commutator"] += 1
    for w in words(tuple(range(1, d + 1)), 4):
        for v in words(tuple(range(1, d + 1)), 3):
            assert wick(w, v) == {w + v: 1}
            counts["holomorphic_restriction"] += 1

for k in range(1, 5):
    alphabet = tuple(range(1, k + 1))
    for lam in map(F, (-2, -1, 0, F(1, 2), 2)):
        for t in map(F, (-1, 0, F(1, 2), 2)):
            coefficients = {(): 1 / (lam - 1)}
            shell = {0: coefficients[()] ** 2}
            for n in range(1, 7):
                shell[n] = F(0)
                for w in product(alphabet, repeat=n):
                    run = 1
                    while run < n and w[run - 1] < w[run]:
                        run += 1
                    rec = sum(t ** h * coefficients[w[h:]] for h in range(1, run + 1)) / (lam - 1)
                    ascents = sum(w[i] < w[i + 1] for i in range(n - 1))
                    closed = t ** n * lam ** ascents / (lam - 1) ** (n + 1)
                    assert rec == closed, (k, lam, t, w)
                    coefficients[w] = rec
                    shell[n] += rec ** 2
                    counts["random_walk_coefficients"] += 1
            transfer = [[t ** 2 * (lam ** 2 if i < j else 1) / (lam - 1) ** 2
                         for j in range(k)] for i in range(k)]
            v = [F(1)] * k
            for n in range(1, 7):
                assert shell[n] == t ** 2 * sum(v) / (lam - 1) ** 4
                v = matvec(transfer, v)
                counts["random_walk_shells"] += 1

for k in range(1, 7):
    for a in range(k + 2):
        matrix = [[a if i < j else 1 for j in range(k)] for i in range(k)]
        for x in range(k + 1):
            xi_minus_m = [[(x if i == j else 0) - matrix[i][j] for j in range(k)] for i in range(k)]
            det = determinant(xi_minus_m)
            assert (1 - a) * det == (x - 1 + a) ** k - a * x ** k
            counts["characteristic_grid"] += 1
            if a == 1:
                assert det == x ** (k - 1) * (x - k)
                counts["characteristic_unit_radius"] += 1
    for b in (F(0), F(1, 2), F(1), F(2)):
        a = b ** k
        matrix = [[a if i < j else 1 for j in range(k)] for i in range(k)]
        v = [b ** (k - 1 - i) for i in range(k)]
        rho = sum(b ** j for j in range(k))
        assert matvec(matrix, v) == [rho * z for z in v]
        counts["perron_eigenvector"] += 1
    matrix = [[1 if i >= j else 0 for j in range(k)] for i in range(k)]
    v = [F(1)] * k
    for power in range(11):
        assert sum(v) == comb(power + k, k - 1)
        v = matvec(matrix, v)
        counts["zero_parameter_jordan_growth"] += 1

print("Arithmetic: exact integers and fractions; no random seed or tolerance")
for key, value in counts.items():
    print(f"{key}: {value} passed")
print("TOTAL:", sum(counts.values()), "passed")
print("Scope: stated finite word lengths and parameter grids only; no analytic-limit or Brown-measure proof")

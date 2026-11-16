"""Exact eight-by-twelve and twelve-by-twelve Nielsen–Soelberg product tables."""

from collections import Counter, defaultdict
from fractions import Fraction


ID = (0, 0, 0, 1, 1)
X = (1, 0, 0, 1, -1)
Y = (0, 1, 0, -1, 1)
A_WORDS = ("", "x", "X", "yxyx", "xY", "Xy", "yxyxY", "xYx")
B_WORDS = ("", "X", "XX", "xy", "y", "YXX", "XYXX", "yxy")


def mul(g, h):
    p, q, c, i, j = g
    r, s, d, k, l = h
    return p + i*r, q + j*s, c + i*j*d + p*j*s, i*k, j*l


def inverse(g):
    p, q, c, i, j = g
    return -i*p, -j*q, i*j*(p*q-c), i, j


def word(letters):
    generators = {"x": X, "X": inverse(X), "y": Y, "Y": inverse(Y)}
    value = ID
    for letter in letters:
        value = mul(value, generators[letter])
    return value


def fibers(left, right):
    result = defaultdict(list)
    for i, a in enumerate(left, 1):
        for j, b in enumerate(right, 1):
            result[mul(a, b)].append((i, j))
    return result


def matrix(equations, right, size):
    result = []
    for cells in equations:
        row = [0] * size
        for i, j in cells:
            row[i-1] += right[j-1]
        result.append(row)
    return result


def independent_rows(rows):
    basis = {}
    selected = []
    for i, input_row in enumerate(rows):
        row = list(map(Fraction, input_row))
        for k in sorted(basis):
            scale = row[k]
            row = [v - scale*w for v, w in zip(row, basis[k])]
        pivot = next((k for k, v in enumerate(row) if v), None)
        if pivot is not None:
            basis[pivot] = [v / row[pivot] for v in row]
            selected.append(i)
    return selected


def determinant(square):
    rows = [list(map(Fraction, row)) for row in square]
    value = 1
    for k in range(len(rows)):
        j = next((i for i in range(k, len(rows)) if rows[i][k]), None)
        if j is None:
            return 0
        if j != k:
            value = -value
            rows[k], rows[j] = rows[j], rows[k]
        pivot = rows[k][k]
        value *= pivot
        for i in range(k+1, len(rows)):
            ratio = rows[i][k] / pivot
            rows[i] = [u - ratio*v for u, v in zip(rows[i], rows[k])]
    return value


def main():
    assert word("yxyxxyxy") == word("xYxYxyxy") == ID
    a = list(map(word, A_WORDS))
    b = list(map(word, B_WORDS))
    assert Counter(map(len, fibers(a,b).values())) == {2:29, 3:2}
    w = word("yxy")
    wb = list(dict.fromkeys(v for g in b for v in (g, mul(g,w))))
    raw = fibers(a, wb)
    assert len(a) == 8 and len(wb) == 12
    assert Counter(map(len, raw.values())) == {2:32, 3:8, 4:2}
    multi = sorted(v for v in raw.values() if len(v) >= 3)
    for k, cells in enumerate(multi,1):
        print(k, cells)
    rows = matrix(multi, [1]*12, 8)
    selected = [0,1,2,3,4,5,6,8]
    assert determinant([rows[i] for i in selected]) == -1
    left = (1,1,1,1,1,-1,1,-1)
    right = (-6,3,-13,10,3,-6,7,19,2,4,8,16)
    def coeff(cells): return sum(left[i-1]*right[j-1] for i,j in cells)
    assert all(coeff(cells)==0 for cells in multi) and coeff(raw[ID])==-19

    wa = list(dict.fromkeys(v for g in a for v in (g, mul(w,g))))
    both = fibers(wa,wb)
    assert len(wa)==12 and Counter(map(len,both.values()))=={2:37,3:10,4:5,5:4}
    rows = matrix(sorted(v for v in both.values() if len(v)>=3),[1]*12,12)
    chosen = independent_rows(rows)
    assert len(chosen)==12
    print("12x12 selected multiterm rows (1-based):", [i+1 for i in chosen])
    print("12x12 minor at right coefficients one:", determinant([rows[i] for i in chosen]))


if __name__ == "__main__":
    main()

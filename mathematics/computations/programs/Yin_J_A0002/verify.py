"""Check three product fibers in a finite image of Nielsen and Soelberg's G3."""

# Each S3 factor acts on Z/3 as z -> u + e*z, with e in {1,-1}.
# The fifth coordinate is additive in Z/4.
IDENTITY = (0, 1, 0, 1, 0)
X = (1, 1, 0, -1, 0)
Y = (0, -1, 1, 1, 1)


def multiply(left, right):
    u, e, v, f, t = left
    r, j, s, k, q = right
    return ((u + e * r) % 3, e * j, (v + f * s) % 3, f * k, (t + q) % 4)


def inverse(value):
    u, e, v, f, t = value
    return ((-e * u) % 3, e, (-f * v) % 3, f, (-t) % 4)


def word(letters):
    values = {"x": X, "y": Y, "X": inverse(X), "Y": inverse(Y)}
    result = IDENTITY
    for letter in letters:
        result = multiply(result, values[letter])
    return result


# The relators (i,j,k,l) impose a_i b_j = a_k b_l in (4.1) and (4.2).
RELATORS = [
    (1,1,2,2), (1,2,2,3), (1,3,3,2), (1,4,2,5), (1,6,2,7),
    (1,8,4,2), (2,1,5,5), (2,4,5,8), (2,6,5,3), (2,8,5,7),
    (3,3,6,6), (4,1,7,5), (4,3,8,6), (5,1,8,2),
]
ROWS = ["", "x", "X", "yxyx", "xY", "Xy", "yxyxY", "xYx"]
COLS = ["", "X", "XX", "xy", "y", "YXX", "XYXX", "yxy"]
REQUIRED = [((1,5),(3,4)), ((6,2),(7,1)), ((6,5),(7,4))]


def main():
    rows, cols = list(map(word, ROWS)), list(map(word, COLS))
    assert rows[0] == cols[0] == IDENTITY
    cells = {
        (i, j): multiply(row, col)
        for i, row in enumerate(rows, 1)
        for j, col in enumerate(cols, 1)
    }
    for i, j, k, l in RELATORS:
        assert cells[i, j] == cells[k, l], (i, j, k, l)
    print("All fourteen product relations and both identity assignments hold.")
    for pair in REQUIRED:
        target = cells[pair[0]]
        fiber = [cell for cell, value in cells.items() if value == target]
        assert set(fiber) == set(pair), (target, fiber)
        print(target, fiber)


if __name__ == "__main__":
    main()

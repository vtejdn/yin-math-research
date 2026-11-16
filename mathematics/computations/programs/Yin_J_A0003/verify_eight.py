"""Check a three-parameter family on the eight-by-twelve product table."""
from collections import Counter

from verify import fibers, mul, word


def main():
    rows = [word(s) for s in ("", "x", "X", "yxyx", "xY", "Xy", "yxyxY", "xYx")]
    base = [word(s) for s in ("", "X", "XX", "xy", "y", "YXX", "XYXX", "yxy")]
    w = word("yxy")
    cols = list(dict.fromkeys(h for b in base for h in (b, mul(b, w))))
    groups = fibers(rows, cols)
    # Tuples specify (sign, exponent of c, exponent of e, exponent of r).
    u = [(1,0,0,0),(-1,0,0,1),(-1,0,0,-1),(1,0,0,0),
         (1,0,0,0),(1,0,0,0),(-1,0,0,-1),(-1,0,0,1)]
    v = [(1,0,0,0),(1,1,0,0),(1,0,0,-1),(1,0,1,2),(1,1,0,3),(1,0,1,1),
         (1,0,0,2),(1,1,0,2),(1,0,0,1),(1,1,0,1),(1,0,1,0),(1,0,1,-1)]

    def coefficient(cells):
        terms = Counter()
        for i, j in cells:
            left, right = u[i-1], v[j-1]
            exponents = tuple(a+b for a, b in zip(left[1:], right[1:]))
            terms[exponents] += left[0]*right[0]
        return {key: count for key, count in terms.items() if count}

    doubles = [cells for cells in groups.values() if len(cells) == 2]
    assert len(doubles) == 32 and all(not coefficient(cells) for cells in doubles)
    high = sorted(cells for cells in groups.values() if len(cells) >= 3)
    expected = [
        {(1,0,0):1, (0,1,3):-1, (0,0,-1):1},
        {(0,1,-1):1, (1,0,4):-1},
        {(0,0,2):1, (1,0,-1):-1},
        {(1,0,3):1, (0,0,-2):-1, (0,1,2):1},
        {(1,0,0):1, (0,0,3):-1, (0,1,3):-1},
        {(1,0,3):1, (0,0,-2):-1, (0,1,-2):-1},
        {(0,0,3):-1},
        {(0,1,-2):-1},
        {(0,0,2):1, (0,1,2):1, (1,0,-1):-1},
        {(0,0,-1):1, (0,1,-1):1, (1,0,4):-1},
    ]
    assert [coefficient(cells) for cells in high] == expected
    varying = [i for i, cells in enumerate(high, 1) if len(coefficient(cells)) == len(cells)]
    assert varying == [1, 4, 5, 6, 9, 10]
    print("All 32 double equations vanish identically on the family.")
    print("Verified all ten Laurent sums. Distinct terms in triples", varying)


if __name__ == "__main__":
    main()

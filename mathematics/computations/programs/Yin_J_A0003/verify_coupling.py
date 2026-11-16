"""Check the coupled Laurent certificate in the original-first 12-by-12 table."""

from collections import Counter
from fractions import Fraction
from itertools import combinations
from typing import NamedTuple

from verify import A_WORDS, B_WORDS, fibers, mul, word


F = ((1, 12), (3, 11), (12, 10))
G = ((3, 12), (6, 3), (7, 2))
T = ((1, 2), (2, 3), (3, 1), (5, 12), (12, 5))
FIVE = (
    ((6, 2), (7, 1)),
    ((1, 1), (2, 2)),
    ((3, 5), (6, 1)),
    ((2, 1), (5, 5)),
    ((2, 11), (5, 10)),
)
VERTICES = tuple(f"{side}{i}" for side in "uv" for i in range(1, 13))


class Monomial(NamedTuple):
    sign: int
    powers: tuple

    def times(self, other):
        return Monomial(self.sign * other.sign,
                        tuple(a+b for a, b in zip(self.powers, other.powers)))

    def over(self, other):
        return Monomial(self.sign * other.sign,
                        tuple(a-b for a, b in zip(self.powers, other.powers)))

    def negative(self):
        return Monomial(-self.sign, self.powers)

    def evaluate(self, values):
        result = Fraction(self.sign)
        for value, power in zip(values, self.powers):
            result *= Fraction(value) ** power
        return result


def terms(fiber, chart):
    return [chart[f"u{i}"].times(chart[f"v{j}"]) for i, j in fiber]


def collect(monomials):
    result = Counter()
    for m in monomials:
        result[m.powers] += m.sign
    return {p: c for p, c in result.items() if c}


def solve_by_unit_pivots(doubles, free):
    one = Monomial(1, (0,)*len(free))
    chart = {"u1": one, "v1": one}
    for k, name in enumerate(free):
        chart[name] = Monomial(1, tuple(int(i == k) for i in range(len(free))))
    # A double fiber with three known vertices determines its fourth uniquely.
    while len(chart) < len(VERTICES):
        old_size = len(chart)
        for (i, j), (k, l) in doubles:
            names = [f"u{i}", f"v{j}", f"u{k}", f"v{l}"]
            assert len(set(names)) == 4
            missing = [p for p, name in enumerate(names) if name not in chart]
            if len(missing) == 1:
                p = missing[0]
                other_pair = names[2:] if p < 2 else names[:2]
                same_pair = names[:2] if p < 2 else names[2:]
                partner = next(name for name in same_pair if name != names[p])
                numerator = chart[other_pair[0]].times(chart[other_pair[1]])
                chart[names[p]] = numerator.negative().over(chart[partner])
        assert len(chart) > old_size, "Some other variable still needs a free value"
    assert all(not collect(terms(f, chart)) for f in doubles)
    return chart


def check_certificate(chart):
    # G/u7 + F/v11 - T = v12/v11 as an identity of Laurent polynomials.
    target = chart["v12"].over(chart["v11"])
    expression = [m.over(chart["u7"]) for m in terms(G, chart)]
    expression.extend(m.over(chart["v11"]) for m in terms(F, chart))
    expression.extend(m.negative() for m in terms(T, chart))
    assert collect(expression) == {target.powers: target.sign}


def check_minimality():
    variable_names = ("u2", "u3", "u5", "u6", "u12", "v3", "v10", "v12")
    examples = (
        ("-1/2", 1, "1/2", -1, -2, 3, 1, 1),
        ("-1/4", "1/2", "1/4", "-1/2", "-3/2", 5, 1, 1),
        ("-1/2", "-1/2", "1/2", "-1/2", "-1/2", 3, 1, 1),
        ("-1/2", "1/2", "-1/6", "-1/2", "5/6", 6, -3, 2),
        ("-1/2", "1/2", "1/2", "-1/2", "-1/2", 5, 3, 1),
    )
    omitted_values = (-1, "1/2", -1, "-2/3", 1)
    for omitted, example, expected in zip(FIVE, examples, omitted_values):
        values = dict.fromkeys(VERTICES, Fraction(1))
        values["v2"] = Fraction(2)
        values.update(zip(variable_names, map(Fraction, example)))
        assert all(values.values())
        for f in (*FIVE, F, G, T):
            value = sum(values[f"u{i}"] * values[f"v{j}"] for i, j in f)
            assert value == (Fraction(expected) if f == omitted else 0)


def main():
    a, b = list(map(word, A_WORDS)), list(map(word, B_WORDS))
    w = word("yxy")
    left = list(dict.fromkeys(a + [mul(w, g) for g in a]))
    right = list(dict.fromkeys(b + [mul(g, w) for g in b]))
    assert len(left) == len(right) == 12
    table = set(tuple(f) for f in fibers(left, right).values())
    assert Counter(map(len, table)) == {2: 37, 3: 10, 4: 5, 5: 4}
    assert {F, G, T, *FIVE} <= table
    doubles = sorted(f for f in table if len(f) == 2)
    free = ("u7", "u12", "v8", "v10", "v11", "v12")
    chart = solve_by_unit_pivots(doubles, free)
    check_certificate(chart)
    for f in (F, G, T):
        powers = [m.powers for m in terms(f, chart)]
        assert len(set(powers)) == len(f)
    nonproportional = Counter()
    for f in table:
        if len(f) >= 3 and len({m.powers for m in terms(f, chart)}) == len(f):
            nonproportional[len(f)] += 1
    assert nonproportional == {3: 8, 4: 5, 5: 2}

    # Specialize (a,b,c,x,y,z) to (1,b,c,1,1,1) for each pair.
    examples = [(-2, 2, -1), (-2, 1, 1), (-1, 2, 1)]
    for (f, g), (b_value, c_value, remaining) in zip(combinations((F, G, T), 2), examples):
        values = (1, b_value, c_value, 1, 1, 1)
        sums = {h: sum(m.evaluate(values) for m in terms(h, chart)) for h in (F, G, T)}
        assert sums[f] == sums[g] == 0
        assert sums[next(h for h in (F, G, T) if h not in (f, g))] == remaining

    # Recompute the identity on the larger torus cut out by just five doubles.
    forced = {"u1", "v1", "u2", "u3", "u5", "u6", "v10"}
    larger = solve_by_unit_pivots(FIVE, tuple(v for v in VERTICES if v not in forced))
    check_certificate(larger)
    check_minimality()
    print("37 double fibers give six free normalized coordinates.")
    print("Every pair of the three fibers cancels on this torus.")
    print("The terms of each selected fiber have pairwise distinct exponents.")
    print("Five double fibers suffice for the three-fiber Laurent identity.")
    print("Deleting any one of these eight equations gives a full-support rational solution.")


if __name__ == "__main__":
    main()

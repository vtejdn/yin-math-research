"""Exact finite checks for Miy23 Proposition 4.5; no analytic norm claims.

Run from the repository root with Python 3.10+; standard library only.
Polynomial coefficients are integer dictionaries indexed by (output word, q degree).
Words are stored in displayed left-to-right order, opposite the source's position
labels j_n,...,j_1. No q value, floating-point approximation, or support truncation
is used.
"""

from functools import lru_cache
from itertools import permutations, product


def clean(poly):
    return {key: value for key, value in poly.items() if value}


def add(target, source, sign=1, shift=0):
    for (word, degree), value in source.items():
        key = (word, degree + shift)
        target[key] = target.get(key, 0) + sign * value


def gaussian(letter, poly):
    result = {}
    for (word, degree), value in poly.items():
        key = ((letter,) + word, degree)
        result[key] = result.get(key, 0) + value
        for pos, other in enumerate(word):
            if letter == other:
                key = (word[:pos] + word[pos + 1 :], degree + pos)
                result[key] = result.get(key, 0) + value
    return clean(result)


@lru_cache(maxsize=None)
def recursive_dual(letter, word):
    """Derive D(jw)=A_j D(w)+delta(i,j)P(w)-D(l_j w)."""
    if not word:
        return {}
    first, rest = word[0], word[1:]
    result = gaussian(first, recursive_dual(letter, rest))
    if not rest and letter == first:
        result[((), 0)] = result.get(((), 0), 0) + 1
    for pos, other in enumerate(rest):
        if first == other:
            add(result, recursive_dual(letter, rest[:pos] + rest[pos + 1 :]), -1, pos)
    return clean(result)


@lru_cache(maxsize=None)
def partitions(n):
    """B(n+1): return pivot k and ordered partners p_1,...,p_(k-1)."""
    return tuple(
        (k, partners)
        for k in range(1, (n + 1) // 2 + 1)
        for partners in permutations(range(k + 1, n + 1), k - 1)
    )


def singleton_positions(n, k, partners):
    return tuple(pos for pos in range(k + 1, n + 1) if pos not in partners)


def drawing_crossings(n, k, partners):
    """Count horizontal/vertical intersections in the prescribed drawing."""
    arcs = ((0, k, 1),) + tuple(
        (low, high, low + 1) for low, high in enumerate(partners, 1)
    )
    verticals = [(endpoint, height) for low, high, height in arcs for endpoint in (low, high)]
    verticals += [(pos, n + 2) for pos in singleton_positions(n, k, partners)]
    return sum(
        low < x < high and vertical_height > horizontal_height
        for low, high, horizontal_height in arcs
        for x, vertical_height in verticals
    )


def closed_crossings(k, partners):
    return sum(pos - k for pos in partners) + sum(
        partners[a] > partners[b]
        for a in range(len(partners))
        for b in range(a + 1, len(partners))
    )


def usual_crossings(k, partners):
    arcs = ((0, k),) + tuple(enumerate(partners, 1))
    return sum(
        a < c < b < d or c < a < d < b
        for index, (a, b) in enumerate(arcs)
        for c, d in arcs[index + 1 :]
    )


def partition_dual(letter, word):
    n = len(word)
    result = {}
    for k, partners in partitions(n):
        if word[n - k] != letter:
            continue
        if any(word[n - low] != word[n - high] for low, high in enumerate(partners, 1)):
            continue
        output = tuple(word[n - pos] for pos in reversed(singleton_positions(n, k, partners)))
        key = (output, drawing_crossings(n, k, partners))
        result[key] = result.get(key, 0) + (-1) ** (k - 1)
    return clean(result)


def apply_partition_dual(letter, poly):
    result = {}
    for (word, degree), coefficient in poly.items():
        add(result, partition_dual(letter, word), coefficient, degree)
    return clean(result)


def one_variable_closed_dual(n):
    """Proposition 3.3, with P_q(N,K) expanded as a product of q-integers."""
    result = {}
    for k in range(1, (n + 1) // 2 + 1):
        scalar = {0: 1}
        for a in range(k - 1):
            factor_length = n - k - a
            multiplied = {}
            for degree, coefficient in scalar.items():
                for added_degree in range(factor_length):
                    target = degree + added_degree
                    multiplied[target] = multiplied.get(target, 0) + coefficient
            scalar = multiplied
        shift = k * (k - 1) // 2
        output = (0,) * (n - 2 * k + 1)
        for degree, coefficient in scalar.items():
            key = (output, degree + shift)
            result[key] = result.get(key, 0) + (-1) ** (k - 1) * coefficient
    return clean(result)


def assert_equal(actual, expected, context):
    if actual != expected:
        raise AssertionError((context, actual, expected))


def main():
    partition_checks = 0
    deletion_checks = 0
    insertion_checks = 0
    counts = []
    for n in range(1, 11):
        counts.append(len(partitions(n)))
        for k, partners in partitions(n):
            cross = drawing_crossings(n, k, partners)
            assert_equal(cross, closed_crossings(k, partners), ("cross", n, k, partners))
            partition_checks += 1
            singles = singleton_positions(n, k, partners)
            for removed in singles:
                new_partners = tuple(pos - (pos > removed) for pos in partners)
                assert (k, new_partners) in partitions(n - 1)
                reduced_cross = drawing_crossings(n - 1, k, new_partners)
                number_to_left = sum(pos > removed for pos in singles)
                assert_equal(reduced_cross + n - removed, cross + number_to_left,
                             ("delete", n, k, partners, removed))
                deletion_checks += 1
            # Here the old partition is B(n+1); the source's induction variable
            # is n+1, so insertion contributes n+1-inserted crossings.
            for inserted in range(1, k + 1):
                new_partners = list(pos + 1 for pos in partners)
                new_partners.insert(inserted - 1, n + 2)
                new_partners = tuple(new_partners)
                assert (k + 1, new_partners) in partitions(n + 2)
                assert_equal(drawing_crossings(n + 2, k + 1, new_partners),
                             cross + n + 1 - inserted,
                             ("insert", n, k, partners, inserted))
                insertion_checks += 1

    formula_checks = 0
    commutator_checks = 0
    for alphabet_size, maximum_length in ((2, 8), (3, 6)):
        for length in range(maximum_length + 1):
            for word in product(range(alphabet_size), repeat=length):
                for letter in range(alphabet_size):
                    candidate = partition_dual(letter, word)
                    assert_equal(candidate, recursive_dual(letter, word),
                                 ("partition-recursion", alphabet_size, letter, word))
                    formula_checks += 1
                    for gaussian_letter in range(alphabet_size):
                        left = apply_partition_dual(letter, gaussian(gaussian_letter, {(word, 0): 1}))
                        add(left, gaussian(gaussian_letter, candidate), -1)
                        expected = {((), 0): 1} if not word and letter == gaussian_letter else {}
                        assert_equal(clean(left), expected,
                                     ("commutator", alphabet_size, letter, gaussian_letter, word))
                        commutator_checks += 1

    # The published Example 4.4 has two ordinary crossings but four prescribed
    # crossings. This is a deliberate negative control against the wrong rule.
    assert_equal(usual_crossings(3, (5, 4)), 2, "ordinary crossing negative control")
    assert_equal(drawing_crossings(5, 3, (5, 4)), 4, "prescribed crossing negative control")
    # The published endpoint counterexamples use quotient-null input tensors.
    symmetric_defect = dict(partition_dual(0, (0, 1)))
    add(symmetric_defect, partition_dual(0, (1, 0)), -1)
    assert_equal(clean(symmetric_defect), {((1,), 0): -1}, "q=1 quotient obstruction")
    assert_equal(partition_dual(0, (0, 0)), {((0,), 0): 1}, "q=-1 quotient obstruction")

    one_variable_checks = 0
    for n in range(33):
        assert_equal(one_variable_closed_dual(n), recursive_dual(0, (0,) * n),
                     ("one-variable Proposition 3.3", n))
        one_variable_checks += 1
    degree_six_e3 = {
        degree: coefficient
        for (word, degree), coefficient in recursive_dual(0, (0,) * 6).items()
        if len(word) == 3
    }
    assert_equal(degree_six_e3, {1: -1, 2: -1, 3: -1, 4: -1},
                 "Example 3.1 corrected coefficient of e3 in D(e6)")
    published_degree_six_e3 = {1: -1, 3: -1, 4: -1}
    assert degree_six_e3 != published_degree_six_e3

    print("Exact integer polynomials in q; standard library")
    print(f"B(n+1) counts, n=1..10: {counts}")
    print(f"Drawing versus closed crossing formula: {partition_checks} passed")
    print(f"Singleton-deletion exponent identities: {deletion_checks} passed")
    print(f"Pair-insertion exponent identities: {insertion_checks} passed")
    print(f"Partition versus independently recursive dual: {formula_checks} passed")
    print(f"Direct commutator identities: {commutator_checks} passed")
    print("Three negative/boundary controls passed (one crossing comparison, two quotient obstructions)")
    print(f"One-variable Proposition 3.3 versus recursion, n=0..32: {one_variable_checks} passed")
    print("Example 3.1 source typo confirmed: e3 coefficient in D(e6) is -q-q^2-q^3-q^4")
    print("PASS: finite algebraic checks only; no all-degree or analytic boundedness certification")


if __name__ == "__main__":
    main()

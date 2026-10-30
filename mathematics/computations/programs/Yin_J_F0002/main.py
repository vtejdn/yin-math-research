"""Exact finite word-action checks for Miy22, Lemmas 3.2 and 3.3.

The full algebraic Fock space is represented by finite dictionaries. No word
produced during an action is discarded, so there is no matrix truncation edge.
The universal proofs and limits of this finite check are in the companion note.
"""

from collections import defaultdict
from functools import cache
from itertools import groupby, product


def combine(*terms):
    """Return an integer linear combination of finitely supported vectors."""
    result = defaultdict(int)
    for scalar, vector in terms:
        for word, coefficient in vector.items():
            result[word] += scalar * coefficient
    return {word: value for word, value in result.items() if value}


def basis(word):
    return {word: 1}


def s_action(letter, vector):
    result = defaultdict(int)
    for word, coefficient in vector.items():
        result[(letter,) + word] += coefficient
        if word and word[0] == letter:
            result[word[1:]] += coefficient
    return {word: value for word, value in result.items() if value}


def right_action(letter, vector, *, annihilate):
    result = defaultdict(int)
    for word, coefficient in vector.items():
        if annihilate:
            if word and word[-1] == letter:
                result[word[:-1]] += coefficient
        else:
            result[word + (letter,)] += coefficient
    return {word: value for word, value in result.items() if value}


def vacuum_projection(vector):
    coefficient = vector.get((), 0)
    return {(): coefficient} if coefficient else {}


def chebyshev_action(letter, degree, vector):
    """Evaluate U_0=1, U_1=s, U_(k+1)=s U_k-U_(k-1) on a vector."""
    if degree == 0:
        return dict(vector)
    previous = dict(vector)
    current = s_action(letter, vector)
    for _ in range(1, degree):
        previous, current = current, combine(
            (1, s_action(letter, current)), (-1, previous)
        )
    return current


@cache
def u_basis_items(operator_word, input_word):
    # Run blocks are multiplied from left to right, so act right to left.
    blocks = [(letter, len(tuple(run))) for letter, run in groupby(operator_word)]
    vector = basis(input_word)
    for letter, degree in reversed(blocks):
        vector = chebyshev_action(letter, degree, vector)
    return tuple(sorted(vector.items()))


def u_action(operator_word, vector):
    return combine(*(
        (coefficient, dict(u_basis_items(operator_word, word)))
        for word, coefficient in vector.items()
    ))


def commutator(letter, operator_word, input_word, *, annihilate):
    vector = basis(input_word)
    return combine(
        (1, right_action(letter, u_action(operator_word, vector),
                         annihilate=annihilate)),
        (-1, u_action(operator_word, right_action(letter, vector,
                                                annihilate=annihilate))),
    )


@cache
def annihilator_commutator_items(letter, operator_word, input_word):
    return tuple(sorted(commutator(letter, operator_word, input_word,
                                   annihilate=True).items()))


def require_equal(actual, expected, context):
    if actual != expected:
        raise AssertionError(f"{context}: actual={actual}, expected={expected}")


def main():
    alphabet = (1, 2)
    words = [word for length in range(5) for word in product(alphabet, repeat=length)]
    counts = defaultdict(int)

    # These baseline actions are independent of the proposed suffix formula.
    for operator_word in words:
        require_equal(u_action(operator_word, basis(())), basis(operator_word),
                      ("vacuum basis", operator_word))
        counts["vacuum basis"] += 1

    for letter in alphabet:
        for generator in alphabet:
            for word in words:
                actual = dict(annihilator_commutator_items(letter, (generator,), word))
                expected = basis(()) if letter == generator and word == () else {}
                require_equal(actual, expected, ("basic commutator", letter, generator, word))
                counts["basic commutator"] += 1

            for degree in range(1, 7):
                operator_word = (generator,) * degree
                for word in words:
                    actual = dict(annihilator_commutator_items(letter, operator_word, word))
                    expected = {}
                    if letter == generator:
                        for split in range(1, degree + 1):
                            term = chebyshev_action(generator, degree - split, basis(word))
                            term = vacuum_projection(term)
                            term = chebyshev_action(generator, split - 1, term)
                            expected = combine((1, expected), (1, term))
                    require_equal(actual, expected,
                                  ("Lemma 3.2", letter, generator, degree, word))
                    counts["Lemma 3.2"] += 1

        for operator_word in words:
            for word in words:
                actual = dict(annihilator_commutator_items(letter, operator_word, word))
                # For v=p i w^rev, the surviving vector is e_p.
                suffix = (letter,) + tuple(reversed(word))
                if len(operator_word) >= len(suffix) and operator_word[-len(suffix):] == suffix:
                    expected = basis(operator_word[:-len(suffix)])
                else:
                    expected = {}
                require_equal(actual, expected, ("Lemma 3.3", letter, operator_word, word))
                counts["Lemma 3.3"] += 1

                creation = commutator(letter, operator_word, word, annihilate=False)
                require_equal(creation, combine((-1, actual)),
                              ("right creation sign", letter, operator_word, word))
                counts["right creation sign"] += 1

                # Coefficients are real integers. Testing the transpose checks
                # [r_i^*, U_v]^* = [r_i^*, U_(v^rev)] on these entries.
                for output_word in words:
                    other = dict(annihilator_commutator_items(
                        letter, tuple(reversed(operator_word)), output_word
                    ))
                    require_equal(actual.get(output_word, 0), other.get(word, 0),
                                  ("adjoint sign", letter, operator_word, word, output_word))
                    counts["adjoint sign entries"] += 1

    print("Arithmetic: exact Python integers; finite word dictionaries; no truncation")
    print("Alphabet: (1, 2); operator/input words: all lengths 0 through 4")
    print("Lemma 3.2 degrees: 1 through 6; adjoint output words: lengths 0 through 4")
    for label, count in counts.items():
        print(f"PASS {label}: {count}")
    print(f"PASS total equalities: {sum(counts.values())}")
    print("No universal identity, norm estimate, or closure theorem is certified by this finite run.")


if __name__ == "__main__":
    main()

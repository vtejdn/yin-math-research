"""Finite exact check of Miy23 Proposition 5.1, independent polynomial recurrence."""
from fractions import Fraction
from functools import lru_cache
from itertools import product


def add(out, key, value):
    out[key] = out.get(key, 0) + value
    if not out[key]:
        del out[key]


def partitions(n):
    for pivot in range(1, n + 1):
        def extend(pos, available, pairs):
            if pos == pivot:
                paired = {a for pair in pairs for a in pair}
                singles = set(range(n + 1)) - paired
                cross = sum(a < s < b for a, b in pairs for s in singles)
                for a, b in pairs:
                    for c, d in pairs:
                        if a < c:
                            cross += int(a < c < b) + int(a < d < b)
                left = tuple(sorted((s for s in singles if s > pivot), reverse=True))
                right = tuple(sorted((s for s in singles if s < pivot), reverse=True))
                exponent = cross - len(right)
                assert exponent >= 0
                yield pairs, left, right, exponent
                return
            yield from extend(pos + 1, available, pairs)
            for partner in available:
                yield from extend(pos + 1, available - {partner}, pairs + ((pos, partner),))
        yield from extend(1, set(range(pivot + 1, n + 1)), ((0, pivot),))


def check(q, max_degree=6):
    @lru_cache(None)
    def wick(word):
        if not word:
            return {(): Fraction(1)}
        lead, tail = word[0], word[1:]
        result = {(lead,) + monomial: coefficient for monomial, coefficient in wick(tail).items()}
        for k, letter in enumerate(tail):
            if lead == letter:
                for monomial, coefficient in wick(tail[:k] + tail[k + 1:]).items():
                    add(result, monomial, -q**k * coefficient)
        return result

    checked = 0
    for n in range(1, max_degree + 1):
        all_parts = list(partitions(n))
        for word in product(range(2), repeat=n):
            for target in range(2):
                lhs = {}
                for monomial, coefficient in wick(word).items():
                    for k, letter in enumerate(monomial):
                        if letter == target:
                            add(lhs, (monomial[:k], monomial[k + 1:]), coefficient)
                rhs = {}
                labels = (target,) + tuple(reversed(word))
                for pairs, left, right, exponent in all_parts:
                    if any(labels[a] != labels[b] for a, b in pairs):
                        continue
                    weight = (-1)**(len(pairs) - 1) * q**exponent
                    left_word = tuple(labels[s] for s in left)
                    right_word = tuple(labels[s] for s in right)
                    for a, coefficient_a in wick(left_word).items():
                        for b, coefficient_b in wick(right_word).items():
                            add(rhs, (a, b), weight * coefficient_a * coefficient_b)
                assert lhs == rhs, (q, word, target, lhs, rhs)
                checked += 1
    return checked


if __name__ == '__main__':
    total = 0
    for parameter in (Fraction(0), Fraction(2, 7), Fraction(-1, 3)):
        count = check(parameter)
        total += count
        print(f'q={parameter}: {count} exact derivative identities passed')
    print(f'TOTAL: {total}; binary words, lengths 1 through 6, both derivatives')

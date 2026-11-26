"""Exact simple-cycle norms and missing-corner counts on the (1,6) network."""

from collections import Counter
from math import isqrt


def projected_cycles():
    values = Counter()
    for root in range(16):
        def extend(path, seen, second):
            source = path[-1]
            for step in (1, -1, 6, -6):
                target = (source + step) % 16
                if target == root:
                    if len(path) < 3 or path[1] >= source:
                        continue
                elif target <= root or target in seen:
                    continue
                coeff = second.copy()
                if step == 6:
                    coeff[source] += 1
                elif step == -6:
                    coeff[target] -= 1
                if target == root:
                    values[tuple(coeff[i] - coeff[i+8] for i in range(8))] += 1
                else:
                    extend(path + [target], seen | {target}, coeff)
        extend([root], {root}, [0] * 16)
    return values


def norms(values):
    modulus = 7340033
    root = 5712452
    assert all(modulus % j for j in range(2, isqrt(modulus) + 1))
    assert pow(root, 8, modulus) == modulus - 1
    modes = [[pow(root, j*k, modulus) for j in range(8)] for k in range(1, 16, 2)]
    result = set()
    for coeff in values:
        if not any(coeff):
            continue
        value = 1
        for mode in modes:
            value = value * sum(c*r for c, r in zip(coeff, mode)) % modulus
        # Fourier Parseval and AM-GM bound the positive integral norm by 32^4.
        assert 0 < value <= 32**4 < modulus
        result.add(value)
    return result


def through_site_counts():
    counts = Counter()
    for subset in range(1 << 16):
        n = [(subset >> i) & 1 for i in range(16)]
        for initial in (0, 1):
            m = []
            previous = initial
            for i in range(16):
                previous += n[(i-6) % 16] - n[i]
                if previous not in (0, 1):
                    break
                m.append(previous)
            if len(m) != 16 or previous != initial:
                continue
            through_t = sum(n[i] == n[(i-6) % 16] == 1 and m[i] == m[i-1] == 0
                            for i in range(16))
            through_s = sum(n[i] == n[(i-6) % 16] == 0 and m[i] == m[i-1] == 1
                            for i in range(16))
            counts[min(through_t, through_s)] += 1
    return counts


def main():
    cycles = projected_cycles()
    assert (sum(cycles.values()), cycles[(0,)*8], len(cycles)-1) == (15691, 91, 4213)
    values = norms(cycles)
    assert (len(values), max(values)) == (58, 3298)
    counts = through_site_counts()
    assert counts == {0: 896, 1: 1024, 2: 736, 3: 224, 4: 32}
    print("15691 cycles, 91 zero reductions, 4213 distinct nonzero vectors.")
    print("58 nonzero norms, maximum 3298.")
    print("2912 flows; smaller through-site counts:", sorted(counts.items()))


if __name__ == "__main__":
    main()

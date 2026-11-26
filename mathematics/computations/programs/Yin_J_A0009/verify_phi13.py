"""Exact cycle norms and finite-character tests on thirteen channels."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import isqrt
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Yin_J_A0008"))
from verify_coupled import optimal_dual
from verify_matching_spread import is_prime
from verify_periods import divide, gcd, trim


N = 13
OFFSETS = (0, 1, 10, 11)
PHI = [1] * N


def cycle_projections():
    graph = [[((i + step) % N, step) for step in (1, -1, 10, -10)]
             for i in range(N)]
    representatives = set()
    universal = total = 0
    labels = [0] * N

    def visit(start, node, path):
        nonlocal total, universal
        for other, step in graph[node]:
            if other < start or other in path[1:]:
                continue
            closing = other == start
            if closing and (len(path) < 3 or path[1] >= node):
                continue
            index = node if step == 10 else other
            if abs(step) == 10:
                labels[index] = 1 if step == 10 else -1
            if closing:
                word = tuple(labels)
                total += 1
                universal += int(len(set(word)) == 1)
                reverse = tuple(-x for x in word)
                representatives.add(min(v[j:] + v[:j] for v in (word, reverse)
                                        for j in range(N)))
            else:
                visit(start, other, path + [other])
            if abs(step) == 10:
                labels[index] = 0

    for start in range(N):
        visit(start, start, [start])
    assert (total, universal, len(representatives)) == (2940, 2, 226)
    return representatives


def verify_norms():
    q, root = 10000121, 8593675
    assert is_prime(q) and root != 1 and pow(root, N, q) == 1
    assert q * 12**6 > 169**6
    norms = set()
    for word in cycle_projections():
        norm = 1
        for k in range(1, N):
            value = sum(x * pow(root, k * j, q) for j, x in enumerate(word))
            norm = norm * value % q
        assert (norm == 0) == (len(set(word)) == 1)
        norms.add(norm)
    assert len(norms) == 31 and max(norms) == 7111
    factors = set()
    for n in norms - {0}:
        for d in range(2, isqrt(n) + 1):
            if n % d == 0:
                factors.add(d)
                while n % d == 0:
                    n //= d
        if n > 1:
            factors.add(n)
    assert max(factors) == 3433
    return factors


def marked_factors(p, degree):
    """Split the factors using the traces of powers of a primitive root."""
    factors = [PHI]
    for j in range(1, N):
        if all(len(f) == degree + 1 for f in factors):
            break
        trace = [0] * N
        for k in range(degree):
            trace[j * pow(p, k, N) % N] += 1
        new = []
        for f in factors:
            for c in range(p):
                if len(f) == degree + 1:
                    break
                trace[0] = -c % p
                part = gcd(f, trim([x % p for x in trace]), p)
                if 1 < len(part) < len(f):
                    f, remainder = divide(f, part, p)
                    assert not remainder
                    new.append(part)
            new.append(f)
        factors = new
    whole = [1]
    assert len(factors) == 12 // degree
    for f in factors:
        assert len(f) == degree + 1 and f[-1] == 1
        new = [0] * (len(whole) + degree)
        for i, a in enumerate(whole):
            for j, b in enumerate(f):
                new[i + j] = (new[i + j] + a * b) % p
        whole = new
    assert whole == PHI
    return factors


def extremum(costs, sign):
    costs = [{j: sign * w for j, w in row.items()} for row in costs]
    largest = max(abs(w) for row in costs for w in row.values())
    owner, left, right = optimal_dual(costs, (2 * N + 1) * largest + 1)
    assert sorted(owner) == list(range(N))
    assert all(costs[i][j] == left[i] + right[j] for j, i in enumerate(owner))
    assert all(left[i] + right[j] <= w for i, row in enumerate(costs)
               for j, w in row.items())
    tight = [{j for j, w in row.items() if left[i] + right[j] == w}
             for i, row in enumerate(costs)]
    reach = [{owner[j] for j in row} for row in tight]
    for k in range(N):
        for targets in reach:
            if k in targets:
                targets.update(reach[k])
    blocks = {tuple(sorted(j for j in targets if i in reach[j]))
              for i, targets in enumerate(reach)}
    full = True
    for block in blocks:
        if len(block) == 1:
            continue
        rows = {j for j, i in enumerate(owner) if i in block}
        offsets = sorted(sorted((j - i) % N for j in rows) for i in block)
        if len(block) != 2 or offsets != [[0, 1], [10, 11]] or not all(rows <= tight[i] for i in block):
            full = False
            break
    return sign * (sum(left) + sum(right)), full


def initial_vectors(p, degree):
    for a in range(1, min(5, p)):
        yield (a,) + (1,) * (degree - 1)
    for a in range(1, min(8, p)):
        for b in range(1, min(6, p)):
            yield tuple((a + b * j) % p for j in range(degree))
    if p**degree <= 20000:
        yield from product(range(p), repeat=degree)


def certify(p, factor, initial, a, lower_index=None):
    if not any(initial):
        return None
    d = len(initial)
    orbit = list(initial)
    for i in range(N):
        orbit.append(-sum(factor[j] * orbit[i + j] for j in range(d)) % p)
    assert orbit[N:] == list(initial)
    if a == 0 and all(orbit[:N]) and 884 * sum(orbit[:N]) <= 217 * N * p:
        return "positive", Fraction(2 * sum(orbit[:N]), N * p)
    modulus = 26 * p if a else p
    base = a * p
    weights = [((10 * base + (26 if a else 1) * x + modulus // 2) % modulus)
               - modulus // 2 for x in orbit[:N]]
    if lower_index is not None:
        assert p == 3 and a == 1 and weights[lower_index] == 30
        weights[lower_index] -= modulus
    costs = [{(i + k) % N: (base if k in (1, 11) else 0) +
              (w if k in (10, 11) else 0) for k in OFFSETS}
             for i, w in enumerate(weights)]
    low, left_full = extremum(costs, 1)
    high, right_full = extremum(costs, -1)
    if lower_index is not None:
        assert (low, high, left_full, right_full) == (-130, 91, True, True)
    if (left_full or right_full) and 884 * (high - low) <= 217 * N * modulus:
        return "matched", Fraction(2 * (high - low), N * modulus)
    return None


def main():
    factors = verify_norms()
    limit = max(max(factors), 13 * 224)
    counts = Counter()
    worst = (Fraction(0), 0)
    primes = 0
    for p in range(2, limit + 1):
        if p == 13 or not is_prime(p):
            continue
        primes += 1
        degree = next(n for n in range(1, 13) if pow(p, n, N) == 1)
        for factor in marked_factors(p, degree):
            if p == 2:
                initial = (0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1)
                method, bound = certify(p, factor, initial, 1)
                assert method == "matched"
                worst = max(worst, (bound, p))
                counts[degree, "matched"] += 1
                continue
            if p == 3 and factor in ([2, 2, 0, 1], [2, 0, 1, 1]):
                index = 3 if factor[1] == 2 else 11
                method, bound = certify(p, factor, (0, 0, 1), 1, index)
                assert method == "matched"
                worst = max(worst, (bound, p))
                counts[degree, "matched"] += 1
                continue
            found = None
            for a in (0, 1, -1, 2, -2, 3, -3):
                for initial in initial_vectors(p, degree):
                    found = certify(p, factor, initial, a)
                    if found:
                        break
                if found:
                    break
            assert found, (p, factor)
            method, bound = found
            worst = max(worst, (bound, p))
            counts[degree, method] += 1
    expected = {1: (0, 480), 2: (18, 216), 3: (36, 280),
                4: (65, 178), 6: (103, 43), 12: (167, 1)}
    actual = {d: (counts[d, "positive"], counts[d, "matched"]) for d in expected}
    assert primes == 480 and sum(counts.values()) == 1587 and actual == expected
    assert worst == (Fraction(11788, 24011), 1847)
    print("Cycle norms: 2940 cycles, 226 classes, maximum 7111, largest prime factor 3433.")
    print(f"{primes} primes; {sum(counts.values())} marked factors. "
          f"By degree (positive, matched): {actual}")
    print(f"Maximum finite bound {worst[0]} at p={worst[1]}.")


if __name__ == "__main__":
    main()

"""Check the large exceptional split primes of the 26-channel cycle computation."""
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "Yin_J_A0008"))
from verify_coupled import optimal_dual
from verify_matching_spread import is_prime


N = 26
OFFSETS = (0, 1, 10, 11)


def roots_of_order_26(p):
    for base in range(2, p):
        root = pow(base, (p - 1) // N, p)
        if pow(root, 13, p) == p - 1 and pow(root, 2, p) != 1:
            break
    else:
        raise AssertionError(("no primitive root", p))
    roots = sorted(pow(root, j, p) for j in range(1, N, 2) if j != 13)
    assert len(set(roots)) == 12
    assert all(pow(x, 13, p) == p - 1 and pow(x, 2, p) != 1 for x in roots)
    return roots


def extremum(costs, sign):
    signed = [{row: sign * cost for row, cost in edges.items()} for edges in costs]
    largest = max(abs(value) for edges in signed for value in edges.values())
    owner, left, right = optimal_dual(signed, (2 * N + 1) * largest + 1)
    assert sorted(owner) == list(range(N))
    assert all(signed[i][j] == left[i] + right[j] for j, i in enumerate(owner))
    assert all(left[i] + right[j] <= cost for i, edges in enumerate(signed)
               for j, cost in edges.items())
    tight = [{j for j, cost in edges.items() if left[i] + right[j] == cost}
             for i, edges in enumerate(signed)]
    reach = [{owner[j] for j in edges} for edges in tight]
    for k in range(N):
        for vertices in reach:
            if k in vertices:
                vertices.update(reach[k])
    full = True
    for i in range(N):
        block = {j for j in reach[i] if i in reach[j]}
        if len(block) == 1:
            continue
        if len(block) != 2:
            full = False
            break
        rows = {row for row, column in enumerate(owner) if column in block}
        offsets = sorted(sorted((row - j) % N for row in rows) for j in block)
        if offsets != [[0, 1], [10, 11]] or any(not rows <= tight[j] for j in block):
            full = False
            break
    score = sum(costs[i][j] for j, i in enumerate(owner))
    assert score == sign * (sum(left) + sum(right))
    return score, full


def candidate(p, orbit, scale, lift):
    weights = [(scale * x + p // 2) % p - p // 2 for x in orbit]
    weights[0] += lift * p
    costs = [{(i + j) % N: (w if j in (10, 11) else 0) for j in OFFSETS}
             for i, w in enumerate(weights)]
    low, low_full = extremum(costs, 1)
    high, high_full = extremum(costs, -1)
    if (low_full or high_full) and 40 * (high - low) <= 9 * N * p:
        return Fraction(2 * (high - low), N * p)
    return None


def first_certificate(p, root):
    orbit = [pow(root, i, p) for i in range(N)]
    for scale in range(1, 13):
        for lift in (1, -1):
            bound = candidate(p, orbit, scale, lift)
            if bound is not None:
                return scale, bound
    raise AssertionError(("no certificate", p, root))


def main():
    source = Path(__file__).with_name("verify_phi26_cycles.mjs")
    data = subprocess.check_output(["node", str(source), "--split-exceptions"], text=True)
    primes = json.loads(data)
    assert len(primes) == 20 and primes == sorted(set(primes))
    assert (primes[0], primes[-1]) == (736399, 1799617)
    counts = Counter()
    worst = (Fraction(0), 0, 0)
    for p in primes:
        assert p > 725546 and p % 26 == 1 and is_prime(p)
        for root in roots_of_order_26(p):
            scale, bound = first_certificate(p, root)
            counts[scale] += 1
            worst = max(worst, (bound, p, root))
    assert counts.total() == len(primes) * 12
    assert counts == {1: 84, 2: 38, 3: 54, 4: 18, 5: 22, 6: 8, 7: 10,
                      8: 2, 10: 2, 12: 2}
    assert worst == (Fraction(4304409, 9573187), 736399, 375441)
    print(f"{len(primes)} primes, {counts.total()} markings")
    print("First witnesses", sorted(counts.items()))
    print("Largest bound and marking", *worst)


if __name__ == "__main__":
    main()

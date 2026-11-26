"""Check both assignment bounds for the split order-25 character orbits."""

from math import isqrt

from verify_coupled import OFFSETS, optimal_dual


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def primitive_roots_25(p):
    for base in range(2, p):
        root = pow(base, (p - 1) // 25, p)
        if pow(root, 5, p) != 1:
            roots = sorted(pow(root, i, p) for i in range(25) if i % 5)
            assert len(set(roots)) == 20
            assert all(pow(r, 25, p) == 1 and pow(r, 5, p) != 1 for r in roots)
            return roots
    raise AssertionError("No primitive root")


def extremum(costs, sign):
    signed = [{row: sign * value for row, value in entries.items()}
              for entries in costs]
    largest = max(abs(value) for entries in signed for value in entries.values())
    owner, column_price, row_price = optimal_dual(signed, 51 * largest + 1)
    assert sorted(owner) == list(range(25))
    assert all(signed[i][j] == column_price[i] + row_price[j]
               for j, i in enumerate(owner))
    assert all(column_price[i] + row_price[j] <= value
               for i, entries in enumerate(signed) for j, value in entries.items())
    tight = [{j for j, value in entries.items()
              if value == column_price[i] + row_price[j]}
             for i, entries in enumerate(signed)]
    reach = [{owner[j] for j in rows} for rows in tight]
    for middle in range(25):
        for reachable in reach:
            if middle in reachable:
                reachable.update(reach[middle])
    blocks = {tuple(sorted(j for j in reach[i] if i in reach[j]))
              for i in range(25)}
    full_endpoint = True
    for block in blocks:
        if len(block) == 1:
            continue
        rows = {j for j, i in enumerate(owner) if i in block}
        offsets = [sorted((j - i) % 25 for j in rows) for i in block]
        if (len(block) != 2 or not all(rows <= tight[i] for i in block)
                or sorted(offsets) != [[0, 1], [7, 8]]):
            full_endpoint = False
            break
    score = sum(costs[i][j] for j, i in enumerate(owner))
    return score, full_endpoint


def certificate(p, root, scale):
    weights = [(scale * pow(root, i, p) + p // 2) % p - p // 2 for i in range(25)]
    costs = [{(i + k) % 25: (w if k >= 7 else 0) for k in OFFSETS}
             for i, w in enumerate(weights)]
    low, low_full = extremum(costs, 1)
    high, high_full = extremum(costs, -1)
    return low, high, sum(map(abs, weights)), low_full or high_full


def main():
    assert certificate(151, 9, 4) == (-335, 486, 997, True)
    prime_count = markings = raw_over_threshold = 0
    largest_scale = 0
    for p in range(26, 100001, 25):
        if not is_prime(p):
            continue
        prime_count += 1
        for root in primitive_roots_25(p):
            for scale in (1, 2, 3):
                low, high, raw, full = certificate(p, root, scale)
                if full and 4 * (high - low) < 25 * p:
                    largest_scale = max(largest_scale, scale)
                    raw_over_threshold += 4 * raw >= 25 * p
                    markings += 1
                    break
            else:
                raise AssertionError((p, root))
    assert (prime_count, markings, largest_scale, raw_over_threshold) == (486, 9720, 3, 2866)
    print(f"{prime_count} split primes; {markings} marked roots; "
          f"{raw_over_threshold} first certificates beyond the raw column bound")


if __name__ == "__main__":
    main()

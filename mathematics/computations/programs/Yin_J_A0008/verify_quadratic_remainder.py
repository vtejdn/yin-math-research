"""Certify both matching bounds for quadratic order-25 markings above 100,000."""
from collections import Counter
from concurrent.futures import ProcessPoolExecutor

from verify_quadratic_spread import INITIAL_PAIRS, certificate, is_prime, marked_traces


LOWER = 100_000
UPPER = 2_300_650
PAIRS = INITIAL_PAIRS + ((3, 4),)


def verify_prime(p):
    counts = Counter()
    fifth_pair = []
    for trace in marked_traces(p):
        for pair in PAIRS:
            if certificate(p, trace, pair):
                counts[pair] += 1
                if pair == PAIRS[-1]:
                    fifth_pair.append((p, trace))
                break
        else:
            raise AssertionError(("no successful functional", p, trace))
    assert counts.total() == 10
    return counts, fifth_pair


def main():
    primes = [p for p in range(LOWER + 24, UPPER + 1, 25) if is_prime(p)]
    assert (len(primes), primes[0], primes[-1]) == (7978, 100049, 2300399)
    counts = Counter()
    fifth_pair = []
    with ProcessPoolExecutor(max_workers=4) as pool:
        for result, exceptional in pool.map(verify_prime, primes, chunksize=16):
            counts.update(result)
            fifth_pair.extend(exceptional)
    assert [counts[pair] for pair in PAIRS] == [39228, 39193, 1304, 54, 1]
    assert counts.total() == 10 * len(primes) == 79780 and len(fifth_pair) == 1
    print(f"{len(primes)} primes, {counts.total()} marked quadratics")
    print("First successful initial pairs", [(pair, counts[pair]) for pair in PAIRS])
    print("Fifth initial pair used at", fifth_pair)


if __name__ == "__main__":
    main()

"""Check matched endpoints for all split prime divisors of the nonzero cycle norms."""
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
import json
import os
from pathlib import Path
import subprocess

from verify_matching_spread import certificate, is_prime, primitive_roots_25


def verify_prime(p):
    assert p > 100000 and p % 25 == 1 and is_prime(p)
    found = Counter()
    for root in primitive_roots_25(p):
        for c in range(1, 5):
            low, high, _, full = certificate(p, root, c)
            if full and 4 * (high - low) < 25 * p:
                found[c] += 1
                break
        else:
            raise AssertionError(("no certificate", p, root))
    assert sum(found.values()) == 20
    return found


def main():
    source = Path(__file__).with_name("verify_cycle_norms.mjs")
    process = subprocess.run(["node", str(source), "--split-exceptions"], check=True,
                             capture_output=True, text=True)
    primes = json.loads(process.stdout)
    assert len(primes) == 5426 and sorted(set(primes)) == primes
    counts = Counter()
    with ProcessPoolExecutor(max_workers=min(8, os.cpu_count() or 1)) as pool:
        for frequencies in pool.map(verify_prime, primes, chunksize=16):
            counts.update(frequencies)
    assert sum(counts.values()) == 108520
    assert counts == {1: 101922, 2: 6354, 3: 240, 4: 4}
    print(f"{len(primes)} split norm primes; 108520 marked roots; "
          f"first successful multipliers: {sorted(counts.items())}.")


if __name__ == "__main__":
    main()

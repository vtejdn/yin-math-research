"""Check all nonsplit quadratic order-25 markings through 100,000."""
from verify_matching_spread import OFFSETS, extremum, is_prime


INITIAL_PAIRS = ((1, 1), (2, 1), (3, 1), (2, 3))


def trace_power(y, exponent, p):
    """Return T_exponent(y) by doubling consecutive traces."""
    a, b = 2, y % p
    for bit in bin(exponent)[2:]:
        odd = (a * b - y) % p
        if bit == "0":
            a, b = (a * a - 2) % p, odd
        else:
            a, b = odd, (b * b - 2) % p
    return a


def marked_traces(p):
    for y in range(p):
        v = trace_power(y, (p + 1) // 25, p)
        if trace_power(v, 25, p) == 2 and trace_power(v, 5, p) != 2:
            break
    else:
        raise AssertionError(("no primitive trace", p))
    traces = sorted(trace_power(v, k, p) for k in range(1, 13) if k % 5)
    assert len(traces) == len(set(traces)) == 10
    for t in traces:
        assert trace_power(t, 25, p) == 2 and trace_power(t, 5, p) != 2
    return traces


def certificate(p, trace, initial):
    values = list(initial)
    for i in range(25):
        values.append((trace * values[i + 1] - values[i]) % p)
    assert values[25:] == list(initial)
    weights = [(v + p // 2) % p - p // 2 for v in values[:25]]
    costs = [{(i + k) % 25: (w if k >= 7 else 0) for k in OFFSETS}
             for i, w in enumerate(weights)]
    lower, lower_full = extremum(costs, 1)
    upper, upper_full = extremum(costs, -1)
    return (lower_full or upper_full) and 4 * (upper - lower) < 25 * p


def main():
    counts = [0] * len(INITIAL_PAIRS)
    primes = [p for p in range(24, 100001, 25) if is_prime(p)]
    assert len(primes) == 463
    for p in primes:
        for t in marked_traces(p):
            for i, pair in enumerate(INITIAL_PAIRS):
                if certificate(p, t, pair):
                    counts[i] += 1
                    break
            else:
                raise AssertionError(("no successful functional", p, t))
    assert counts == [2267, 2283, 78, 2]
    print(f"{len(primes)} quadratic primes, {sum(counts)} marked traces; "
          f"first successful functionals {counts}")


if __name__ == "__main__":
    main()

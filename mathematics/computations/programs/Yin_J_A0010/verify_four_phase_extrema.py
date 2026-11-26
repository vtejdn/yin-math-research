"""Check the four-channel extremal sets for the order-sixteen marking."""

from itertools import product


def matchings():
    flows = {}
    for paths in product(range(4), repeat=4):
        first_edges = set()
        second_edges = set()
        outputs = []
        intermediate = [[] for _ in range(4)]
        for i, path in enumerate(paths):
            j = i
            if path & 1:
                second_edges.add(i)
                j = (j + 2) % 4
            intermediate[j].append(path)
            if path & 2:
                first_edges.add(j)
                j = (j + 1) % 4
            outputs.append(j)
        if len(set(outputs)) != 4:
            continue
        key = (frozenset(first_edges), frozenset(second_edges))
        singletons = flows.setdefault(key, set())
        for ports in intermediate:
            if len(ports) == 1:
                singletons.add(ports[0])
    assert len(flows) == 16
    return flows


def main():
    flows = matchings()
    # A zero root entry denotes the irreducible quadratic in characteristic three.
    cases = [(3, 0, 1, 1), (5, 2, 1, 2), (5, 3, 1, 3),
             (13, 5, 4, 7), (13, 8, 4, 6),
             (17, 4, 6, 7), (17, 13, 6, 10)]
    for prime, root, a, b in cases:
        if root:
            assert root * root % prime == prime - 1 and a * root % prime == b
        weights = [(6 * prime + 16 * j + 8 * prime) % (16 * prime) - 8 * prime
                   for j in (a, b, -a, -b)]
        costs = {key: prime * len(key[0]) + sum(weights[i] for i in key[1])
                 for key in flows}
        low, high = min(costs.values()), max(costs.values())
        min_flow, = (key for key, cost in costs.items() if cost == low)
        max_flow, = (key for key, cost in costs.items() if cost == high)
        assert flows[min_flow] <= {1, 3}  # A or C at a one-port site
        assert flows[max_flow] <= {0, 2}  # B or D at a one-port site
        assert (low, high) == ((-44, 24) if prime == 5 else (-8 * prime, 4 * prime))
        print(prime, root, weights, low, high)


if __name__ == "__main__":
    main()

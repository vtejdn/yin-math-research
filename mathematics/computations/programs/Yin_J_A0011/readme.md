---
author: Yin
---

# Five-channel permutation certificates at cyclic orders twenty-five and twenty-six

## Scope and reproduction

Run `python -B verify_five_channels.py` with assertions enabled in this directory.
The [exact verifier](verify_five_channels.py) uses the Python standard library and writes no output files.
It enumerates all ordered generating pairs in the alternating group on five points and all ordered generating pairs in the symmetric group with odd first and even second mark, up to simultaneous relabeling of the five points.
For each stored choice of the cyclic character and individual edge lifts it enumerates all 1024 site choices, retains the perfect matchings and checks both extremal costs.
At a successful endpoint all optimal matchings use the same set of first and second permutation edges.
It reports the largest verified spread in each family.

## Six and seven channels

Run `node verify_seven_channels.mjs` in this directory.
The [six- and seven-point verifier](verify_seven_channels.mjs) constructs the symmetric groups, enumerates transitive ordered pairs up to simultaneous conjugation, and checks solvability directly when their order is below 60.
For each larger image it verifies a finite certificate for the [six- and seven-point bounds](../../../claims/Yin_C_A0306_v1.md#statement).
Adding `--certificates` prints the two one-line permutations, group order, multiplier, edge mask, selected end and spread for every tested representative.
The first block of mask bits belongs to the first mark and the second block to the second mark, both in site order starting at zero.
Three order-25 certificates also give the nonidentity return permutation on a single zero-cost circuit.
The largest spreads for six points are 37 and 38 at orders 25 and 26, and for seven points they are 43 and 45.
The computation uses only standard Node.js and does not write files.

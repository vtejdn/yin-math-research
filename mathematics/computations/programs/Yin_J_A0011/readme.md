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

## Small nonsolvable images at cyclic order sixteen

Run `node verify_small_permutations_sixteen.mjs` from this directory; append `--witnesses` to print each original marked permutation pair, the selected action, weights, mask, optimal anchor, spread and number of local rank corrections.
The [native verifier](verify_small_permutations_sixteen.mjs) uses standard Node.js and writes no files.
It checks the 38 five-site and 258 six-site marked pairs of image order at least sixty with even second mark, and all 114 simultaneous-conjugacy representatives generating the seven-point linear group of order 168.
The [group-rank theorem](../../../claims/Yin_C_A0341_v1.md#actions-and-finite-certificates) specifies the additional actions on factorizations of the six-point complete graph, partitions into triples, and conjugate cyclic subgroups, and derives the regular bound from the certificates.

## The normalizer of the linear group of order 168

Run `node verify_linear_normalizer_sixteen.mjs` from this directory; `--witnesses` prints a record for each of the 69 marked normalizer classes.
The [normalizer verifier](verify_linear_normalizer_sixteen.mjs) reuses the preceding permutation and endpoint functions, enumerates all eight-site normalizing permutations, and realizes the final marked class on fourteen Klein four subgroups.
There are 336 normalizing permutations, 168 even ones, and all 69 classes meet the bound \(15/32\).
The fourteen-site action has 2928 pairs of used edge sets, four minimizing pairs, and spread 52 for the prescribed lift.
The [normal-subgroup result](../../../claims/Yin_C_A0341_v2.md#the-conjugation-action-on-eight-cyclic-subgroups) applies the calculation to the action inside any quotient containing that normal subgroup.

## All three alternating-group normalizer extensions

Run `node verify_alternating_normalizer_sixteen.mjs` from this directory; `--witnesses` prints one certificate for each of the 209 original ten-site generating classes.
The [verifier](verify_alternating_normalizer_sixteen.mjs) acts on the ten partitions of six letters into two triples, constructs the full 1440-element normalizer, and checks its three index-two extensions of the alternating subgroup.
It tests witness costs on all feasible matching flows, allowing a rank-one local change at each possibly singular singleton at the cheaper end.
The three cosets give 53, 78 and 78 classes.
Two in the last coset use the twelve-site permutation action induced from the six-letter action of the alternating subgroup.
The [normal alternating subgroup theorem](../../../claims/Yin_C_A0341_v3.md#ordinary-and-induced-actions-for-every-marking) gives the regular bound \(19/40\).

---
author: Yin
---

# Split primes and coordinate matchings at the order-25 marking

## Question and scope

The two finite calculations test which marked cyclic characters give the support and width required by the order-25 rank estimates.
The five-coordinate test covers split primes up to \(18^4\) and the twenty-five-coordinate test covers each primitive fifth root at \(11,41,61\).

## Files

The [five-coordinate verifier](verify.py) sieves the split primes and tests weighted matchings.
The [twenty-five-coordinate verifier](verify_slices.py) finds a perfect matching by augmenting paths and partitions the matched support graph by mutual reachability.

## Reproduction

From this directory run `python -B verify.py` and `python -B verify_slices.py` with assertions enabled.
Both programs use Python 3's standard library and integer arithmetic, read no data files and print the results.

For every prime \(p\) congruent to one modulo five and at most \(18^4\), a sieve of integer multiples supplies the primes in the finite interval.
Powers of a primitive fifth root give the five frequencies.
The first loop checks all nonzero multipliers unless it has already found a word of positive residues summing to \(p\).
Choosing a different primitive root permutes the five positions in this sum.
For each exceptional prime all four primitive roots are checked separately in the matching computation.
The program also checks both single-sign choices for the five weights at every nonzero multiplier and every cyclic shift exponent from \(-6\) through \(6\).
A larger absolute exponent already exceeds the desired width by itself.
It verifies the mixed-sign phase width and the claimed numerical bound by integer cross multiplication, and enumerates the 120 row permutations, retaining the minimum among those whose five offsets belong to the four permitted translations.

For each of \(p=11,41,61\), the second program tests all four nonidentity fifth roots in \(\mathbb F_p\).
Centered residues give the block widths and the surviving row offsets at parameter zero.

## Results and limits

The first computation found 2491 split primes, four exceptions \(11,41,61,101\) to the positive-sum test, and successful weighted matching checks for all sixteen exceptional markings.
The [five-coordinate argument](../../../claims/Yin_C_A0215_v1.md#minimum-matchings-and-the-full-rank-specialization) gives the group-rank inference from the finite arithmetic and matchings.
Each of the twelve twenty-five-coordinate graphs has thirteen singleton components and six two-column components with the two required offset pairs.
The executed block-width sums were \(45,147,213\), respectively.
The [slice-transfer proof](../../../claims/Yin_C_A0216_v1.md#twelve-zero-parameter-certificates) uses these finite checks for a regular-rank bound.

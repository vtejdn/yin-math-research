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

## Coupled orbits at four primes

Run `python -B verify_coupled.py` from this directory with assertions enabled.
The [coupled-orbit verifier](verify_coupled.py) includes all its input data, uses Python 3 without external packages and writes no output files.
At each prime it verifies factor coverage by exact polynomial multiplication and the Frobenius order, constructs every weight list by recurrence from one functional on the marked simple quotient, and checks periodicity.
It finds a matching and two integer price lists, then directly verifies a tight matching and nonnegative reduced costs on all actual arrows.
It verifies mutual reachability, every diagonal block type, the total degree and the common numerical bound by integer comparisons.
The executed counts for primes \(7,43,101,149\) were \(5,5,20,10\) factors, with maximum block-width sums \(959,5925,14750,21100\) respectively.
The [four-prime proof](../../../claims/Yin_C_A0217_v1.md#verifying-full-rank-away-from-zero) explains how the second choice of row and column powers supplies the full-rank specialization required by the degree estimate.

## Both matching costs at split primes

Run `python -B verify_matching_spread.py` from this directory with assertions enabled.
The [split-prime verifier](verify_matching_spread.py) imports the integer assignment routine from the coupled-orbit verifier.
For each split prime through 100000 it generates all twenty primitive roots of order 25 and checks the lower and upper prices on every actual edge.
At least one of the two directed graphs must yield a block triangular invertible endpoint.
All 9720 marked roots at the 486 primes passed, using only the multipliers one, two and three.
For 2866 first successful multipliers the sum of the original block-column widths alone does not give a strict half bound.
The [output-degree interpolation](../../../claims/Yin_C_A0219_v1.md#interpolation-with-different-output-degrees) gives the regular-rank estimate from the two matching costs.

## Quartic periods through the size cutoff

Run `python -B verify_periods.py` with assertions enabled in this directory.
The [period verifier](verify_periods.py) uses standard-library integer arithmetic, reads no inputs and writes no files.
It expands the product over five Gaussian periods in the twenty-fifth cyclotomic ring to recover their quintic polynomial.
It sieves the primes congruent to 7 or 18 modulo 25 through \(18^5=1889568\), setting aside 7 for the coupled-orbit calculation above.
At each remaining prime, deterministic polynomial splitting produces five distinct roots and the verifier checks their number and their values by substitution.
It searches positive multipliers from \(p-1\) down through those strictly above \(p/2\), stopping at the first with period sum \(p\) and checking that every witness found exceeds \(3p/4\).
Of the 14140 primes in range, 14137 have this trace witness.
At the two exceptions \(43,157\) it checks the displayed irreducible quartic factors by cyclotomic divisibility and the Frobenius order, and verifies positivity and all five sums by exact recurrence.
The [quartic character proof](../../../claims/Yin_C_A0220_v1.md#the-five-periods-of-the-trace) identifies these finite lists as actual representations of the marked group and supplies the rank estimate.

## Quadratic matching spread through one hundred thousand

Run `python -B verify_quadratic_spread.py` with assertions enabled in this directory.
The [quadratic verifier](verify_quadratic_spread.py) uses Python 3 integer arithmetic and reuses the primal and dual matching checks from the split-prime and coupled-orbit verifiers.
For each of the 463 primes congruent to 24 modulo 25 through 100000 it checks exact order 25 and obtains all ten distinct traces of inverse pairs of primitive roots.
For each trace it tests four initial pairs in order, constructs the 25 weights by recurrence, and checks the two matching costs and an invertible endpoint.
The four initial pairs first succeed on 2267, 2283, 78 and 2 traces respectively, accounting for all 4630 marked traces.
The [matching estimate](../../../claims/Yin_C_A0221_v1.md#both-matching-costs-for-the-ten-traces) deduces a strict half bound from each successful pair.

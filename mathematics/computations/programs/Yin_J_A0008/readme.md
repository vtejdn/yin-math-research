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

## Quadratic markings through 2300650

Run `python -B verify_quadratic_remainder.py` with assertions enabled in this directory using Python 3.10 or later.
The [interval verifier](verify_quadratic_remainder.py) reuses the exact arithmetic, primal and dual assignments, and endpoint checks of the quadratic verifier above.
It checks each prime congruent to 24 modulo 25 in the interval from 100001 through 2300650 and all ten marked quadratic factors at each prime.
For each trace it tries the five initial pairs `(1,1), (2,1), (3,1), (2,3), (3,4)` in order, using four processes on independent primes.
The 7978 primes from 100049 to 2300399 give 79780 successful markings, with first-success counts 39228, 39193, 1304, 54 and 1.
The sole fifth-pair marking has prime 1749499 and trace 728242, with matching costs \(-4290984,4290984\) and both endpoints invertible.
The [regular nullity estimate](../../../claims/Yin_C_A0228_v1.md#extension-of-the-quadratic-certificate) uses the two certified matching costs of that same character.

## Norms of simple circulation cycles

Run `node verify_cycle_norms.mjs` in this directory using Node.js.
The [native verifier](verify_cycle_norms.mjs) uses the built-in assertion library, reads no files and prints the exact counts and maximum.
It enumerates the underlying undirected simple cycles on the 25 vertices with two edge types of steps one and seven.
An integer mask pair records the signed seven-step edges.
The arithmetic uses integer Number operands below the exact-integer limit for the two modular products, with BigInt for the final Chinese remainder reconstruction.
All 2303657 cycles give 92032 projection classes up to translation and reversal.
There is one zero projection and 31 further cycles whose coefficients are constant on each residue class modulo five.
The maximum nonzero cyclotomic norm is 5314180901.
The [circulation proof](../../../claims/Yin_C_A0225_v1.md#the-norm-calculation-and-the-cycles-descending-modulo-five) bounds every integer norm before reconstruction and gives the field and matching implications.
This computation inspects all simple cycles and does not require that a specified cycle occur in an optimal matching.

## Split factors of the nonzero cycle norms

Run `python -B verify_exceptional_split.py` with assertions enabled in this directory using Python 3 and Node.js.
The [exceptional-prime verifier](verify_exceptional_split.py) calls the native cycle verifier with `--split-exceptions` and consumes the resulting list of primes through its standard output.
It creates no data files.
Trial division of the 10234 distinct nonzero norms gives 5931 distinct prime factors.
Exactly 5426 exceed 100000 and are congruent to one modulo 25; the largest is 2227495051.
The Python verifier checks primality and all twenty marked roots at each prime.
It uses the [matching and dual-price checks](verify_matching_spread.py), distributing independent primes over at most eight worker processes.
Among the 108520 marked roots, the first successful multipliers \(1,2,3,4\) occur respectively \(101922,6354,240,4\) times.
The [rank calculation for these factors](../../../claims/Yin_C_A0227_v1.md#the-finite-endpoint-certificates) uses the verified strict spread and invertible endpoint for each individual marking.

## Five coordinates at noncyclic order twenty

Run `python -B verify_noncyclic_twenty.py` with assertions enabled in this directory.
The [integer verifier](verify_noncyclic_twenty.py) uses Python 3's standard library and writes no files.
It checks the degree-four ternary orbit and all sixteen marked split roots at the four exceptional primes of the original positive-sum sieve.
The five-point permutations have steps one and two.
Among the 24 different pairs of used edge sets the minimizer and maximizer of each prescribed cost are both unique.
The largest certified spreads at \(3,11,41,61,101\) are respectively \(25,110,315,395,720\).
The [order-twenty group-ring application](../../../claims/Yin_C_A0313_v3.md#the-remaining-seventeen-marked-representations) uses the two independent binary signs in choosing its cyclic character.

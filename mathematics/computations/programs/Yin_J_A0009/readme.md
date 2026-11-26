---
author: Yin
---

# Character and matching certificates for the critical order-26 marking

## Question and scope

For the marked degrees \(1,10\) modulo 26, test the finite arithmetic underlying regular-rank estimates for the four-site rectangle.
The thirteen-coordinate calculation covers all simple quotients in the component of \(\Phi_{13}\).
The twenty-six-coordinate calculations treat the nonperiodic cycle ties and the remaining finite simple factors of \(\Phi_{26}\).

## Files

The [thirteen-coordinate verifier](verify_phi13.py) computes the norms of the simple-cycle polynomials and checks the finite-field characters, matching costs and tight endpoints at the remaining primes.
It reuses exact polynomial division and greatest common divisors, trial primality, and the matching engine from [J_A0008](../Yin_J_A0008/readme.md).

## Reproduction

Run `python -B verify_phi13.py` from this directory with assertions enabled using Python 3.8 or later.
The program uses standard-library integer and rational arithmetic, reads the sibling program's Python modules and writes no files.

## Results and limits

The cycle calculation visits 2940 simple undirected cycles in the thirteen-point graph, yielding 226 signed projection classes up to rotation and reversal.
Only two projections have zero norm.
The maximum nonzero norm is 7111, and the largest prime factor is 3433.
The finite-field calculation checks every prime \(p\le3433\) apart from the impossible characteristic 13, factoring \(\Phi_{13}\) modulo \(p\) and verifying that the monic factors of the Frobenius degree have product \(\Phi_{13}\).
The 480 primes yield the following 1587 verified markings.

| Factor degree | Positive orbit | Matched endpoint |
| --- | --- | --- |
| 1 | 0 | 480 |
| 2 | 18 | 216 |
| 3 | 36 | 280 |
| 4 | 65 | 178 |
| 6 | 103 | 43 |
| 12 | 167 | 1 |

For every matching certificate the program verifies two primal matchings and dual price lists, compares the resulting spread by integers and checks the strongly connected components at one endpoint.
It verifies both modified ternary lifts separately, including their lower and upper costs \(-130,91\).
The maximum finite estimate is \(11788/24011\) at \(p=1847\).
The [thirteenth cyclotomic proof](../../../claims/Yin_C_A0230_v1.md#cycle-norms-and-an-injective-specialization-at-large-primes) supplies the regular-rank argument, including the treatment of every larger prime.

## Folded norms of the twenty-six-coordinate graph

Run `node verify_phi26_cycles.mjs` from this directory with Node.js 18 or later.
The [cycle verifier](verify_phi26_cycles.mjs) enumerates 4004289 undirected simple cycles with steps one and ten.
Folding opposite coordinates and removing common content leaves 30967 nonzero classes up to rotation and sign.
Among the other cycles, 1509 have zero folded coefficients and 106 have a nonzero constant folded coefficient.
The two-prime integer reconstruction gives 1957 distinct positive normalized norms and largest norm 2800409.
The option `--split-exceptions` prints the twenty split prime divisors above 725546 as a JSON array for the next verifier.
The [antiperiodic lift proof](../../../claims/Yin_C_A0233_v1.md#a-short-lift-on-the-selected-line) explains why the 106 additional cycles cannot have zero integer cost for its selected character.

## Large split norm divisors on twenty-six channels

Run `python -B verify_phi26_exceptional_split.py` in this directory with assertions enabled, Python 3.10 or later, and Node.js.
The [split-prime verifier](verify_phi26_exceptional_split.py) obtains all twenty primes from the cycle program's `--split-exceptions` output, tests primality and verifies all twelve marked roots at each prime.
It tries multipliers 1 through 12, changing just the zeroth centered representative by adding or subtracting one copy of the prime.
Both matching costs must have exact primal and dual certificates, and at least one endpoint must pass the invertible-component check for that same lift.
All 240 markings passed, with first-success counts 84, 38, 54, 18, 22, 8, 10, 2, 0, 2, 0 and 2 in multiplier order.
The [regular nullity bound](../../../claims/Yin_C_A0234_v1.md#a-change-at-one-coordinate-and-both-matching-costs) has its largest computed value 4304409/9573187 at prime 736399 and root 375441.

## All simple factors on twenty-six coordinates through 725547

Run `node verify_phi26_remainder.mjs` from this directory using Node.js 18 or later.
The [interval verifier](verify_phi26_remainder.mjs) and its [finite-field polynomial routines](phi26_factors.mjs) use only native JavaScript and the built-in assertion library.
They read no data files and write no files.
All modular products and orbit sums use integer operands within the exact integer range; the program also checks the returned integer dual prices against every allowed arrow.

The sieve includes every prime at most 725547.
At odd primes other than 13 the factors have the Frobenius degree and their product is checked against the full twenty-sixth cyclotomic polynomial.
The exceptional characteristics two and thirteen are checked on their unique simple factors.
The 194945 marked factors at 58457 primes were certified as follows.

| Factor degree | Alternating signs | Matched endpoint |
| --- | --- | --- |
| 1 | 453 | 58144 |
| 2 | 4 | 29234 |
| 3 | 49 | 38919 |
| 4 | 4 | 29201 |
| 6 | 1 | 19427 |
| 12 | 19506 | 3 |

Each alternating-sign certificate uses a genuine orbit with absolute weight sum at most \(3p\) on its first thirteen coordinates.
Each matched certificate uses the same lifted orbit for the two exact matching extrema and the endpoint check, and satisfies \(884(U-L)\le217\cdot26m\) at its \(m\) true phases.
The [finite-interval proof](../../../claims/Yin_C_A0235_v1.md#full-matched-endpoints-and-coverage) gives the corresponding regular nullity bound.

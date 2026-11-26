---
author: Yin
---

# Coupled orbit matchings for the two remaining prime classes

## Coupled character orbits at four primes

At 2026-11-26T10:24 UTC the fixed proof received the following inspection.
A reviewer outside development independently checked the whole proof, reran the native verifier and reconstructed the character coordinates in each polynomial quotient.
Shortest paths in the residual graphs verified the matching bounds and their tight components independently of the price computation.
The five, five, twenty and ten factors cover all four characteristics including inverse generator markings.
The width maxima 959, 5925, 14750 and 21100 give a common upper bound of 236 over 505 with the stated coefficient hypotheses.

## Two matching bounds for interpolation

At 2026-11-26T10:29 UTC the fixed proof received the following inspection.
A reviewer outside development checked the full proof and reran the native verifier.
The lower prices make every entry polynomial, while the independent upper prices compare all output degrees with the chosen input degrees.
Surjective evaluation onto the direct sum has a bounded right inverse, so the codimension calculation is valid for closed ranges even if the fiber operators have nonclosed images.
An independently implemented shortest-augmenting-path calculation reproduced 486 split primes, 9720 roots and 2866 first certificates for which the original column widths fail the strict threshold.
The respective counts using first multipliers one, two and three were 9158, 536 and 26.
For the example at 151 the costs were minus 335 and 486, with original width sum 997.

## All quadratic traces through one hundred thousand

At 2026-11-26T10:35 UTC the fixed proof received the following inspection.
A reviewer outside development checked the whole proof and reran the native verifier.
In an independent enumeration the trace polynomial was evaluated at every field element, followed by residual graph checks for both extrema in the matching problem.
This gave exactly ten traces at each of 463 primes and reproduced the first-success counts 2267, 2283, 78 and 2.
The last initial pair was needed at the traces 5023 modulo 8599 and 19068 modulo 41999.
The reviewer checked the genuine representations, the strict interpolation bound, and the distinct upper bounds on the prime in the linear and quadratic cases.
A trivial commutator abelianization satisfies the remaining prime restrictions vacuously.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Coupled character orbits at four primes](#coupled-character-orbits-at-four-primes) | independently reviewed |
| [Two matching bounds for interpolation](#two-matching-bounds-for-interpolation) | independently reviewed |
| [All quadratic traces through one hundred thousand](#all-quadratic-traces-through-one-hundred-thousand) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Coupled character orbits at four primes](#coupled-character-orbits-at-four-primes) | [Statement](../../claims/Yin_C_A0217_v1.md#statement) | All four residual primes and the half-rank consequence. |
| [Coupled character orbits at four primes](#coupled-character-orbits-at-four-primes) | [Characters from a single coupled orbit](../../claims/Yin_C_A0217_v1.md#characters-from-a-single-coupled-orbit) | The marked quotient, orbit recurrence, genuine twists and column widths. |
| [Coupled character orbits at four primes](#coupled-character-orbits-at-four-primes) | [Verifying full rank away from zero](../../claims/Yin_C_A0217_v1.md#verifying-full-rank-away-from-zero) | Integer prices, tight components and the order of the group factors. |
| [Coupled character orbits at four primes](#coupled-character-orbits-at-four-primes) | [Factor coverage and numerical bounds](../../claims/Yin_C_A0217_v1.md#factor-coverage-and-numerical-bounds) | All forty factors and the common upper bound. |
| [Coupled character orbits at four primes](#coupled-character-orbits-at-four-primes) | [Supporting argument](../../claims/Yin_C_A0212_v1.md#finiteness-and-the-cyclic-module) | Split group and cyclic module. |
| [Coupled character orbits at four primes](#coupled-character-orbits-at-four-primes) | [Supporting argument](../../claims/Yin_C_A0216_v1.md#the-remaining-prime-divisors) | The whole commutator abelianization at half nullity. |
| [Coupled character orbits at four primes](#coupled-character-orbits-at-four-primes) | [Supporting argument](../../claims/Yin_C_A0204_v1.md#the-bound-using-individual-column-widths) | Actual regular-rank inequality at the unitary twists. |
| [Coupled character orbits at four primes](#coupled-character-orbits-at-four-primes) | [Supporting argument](../../computations/programs/Yin_J_A0008/verify_coupled.py) | Inputs, exact product and matching certificates. |
| [Two matching bounds for interpolation](#two-matching-bounds-for-interpolation) | [Statement](../../claims/Yin_C_A0219_v1.md#statement) | Finite-trace operator pencils and the split-prime application. |
| [Two matching bounds for interpolation](#two-matching-bounds-for-interpolation) | [Lower and upper potentials](../../claims/Yin_C_A0219_v1.md#lower-and-upper-potentials) | Independent dual prices and prescribed exponent bounds. |
| [Two matching bounds for interpolation](#two-matching-bounds-for-interpolation) | [Interpolation with different output degrees](../../claims/Yin_C_A0219_v1.md#interpolation-with-different-output-degrees) | Choice of degree spaces, bounded right inverse and codimension of the range constraint. |
| [Two matching bounds for interpolation](#two-matching-bounds-for-interpolation) | [Split primes and a strict improvement over column widths](../../claims/Yin_C_A0219_v1.md#split-primes-and-a-strict-improvement-over-column-widths) | Endpoint factorizations and the exact count through one hundred thousand. |
| [Two matching bounds for interpolation](#two-matching-bounds-for-interpolation) | [Supporting argument](../../claims/Yin_C_A0204_v1.md#the-bound-using-individual-column-widths) | Regular absorption with a common auxiliary dimension. |
| [Two matching bounds for interpolation](#two-matching-bounds-for-interpolation) | [Supporting argument](../../claims/Yin_C_A0217_v1.md#characters-from-a-single-coupled-orbit) | All split marked character orbits. |
| [Two matching bounds for interpolation](#two-matching-bounds-for-interpolation) | [Supporting argument](../../computations/programs/Yin_J_A0008/verify_matching_spread.py) | Both extremal costs, support components and split-prime coverage. |
| [All quadratic traces through one hundred thousand](#all-quadratic-traces-through-one-hundred-thousand) | [Statement](../../claims/Yin_C_A0221_v1.md#statement) | Quadratic exclusion in the finite interval and both remaining prime ranges. |
| [All quadratic traces through one hundred thousand](#all-quadratic-traces-through-one-hundred-thousand) | [Enumerating the marked quadratic traces](../../claims/Yin_C_A0221_v1.md#enumerating-the-marked-quadratic-traces) | All ten traces, their orders, recurrence and absorbed representations. |
| [All quadratic traces through one hundred thousand](#all-quadratic-traces-through-one-hundred-thousand) | [Both matching costs for the ten traces](../../claims/Yin_C_A0221_v1.md#both-matching-costs-for-the-ten-traces) | The endpoint certificate, extremal costs and the four initial pairs. |
| [All quadratic traces through one hundred thousand](#all-quadratic-traces-through-one-hundred-thousand) | [Bounds on remaining primes](../../claims/Yin_C_A0221_v1.md#bounds-on-remaining-primes) | Split and quadratic size constraints and the trivial commutator abelianization. |
| [All quadratic traces through one hundred thousand](#all-quadratic-traces-through-one-hundred-thousand) | [Supporting argument](../../claims/Yin_C_A0219_v1.md#interpolation-with-different-output-degrees) | The matching spread controls regular nullity. |
| [All quadratic traces through one hundred thousand](#all-quadratic-traces-through-one-hundred-thousand) | [Supporting argument](../../claims/Yin_C_A0219_v1.md#split-primes-and-a-strict-improvement-over-column-widths) | Split characteristics through the same cutoff. |
| [All quadratic traces through one hundred thousand](#all-quadratic-traces-through-one-hundred-thousand) | [Supporting argument](../../claims/Yin_C_A0220_v1.md#statement) | Exclusion of both quartic congruence classes. |
| [All quadratic traces through one hundred thousand](#all-quadratic-traces-through-one-hundred-thousand) | [Supporting argument](../../claims/Yin_C_A0218_v1.md#numerical-consequence-for-the-twenty-fifth-component) | Upper bounds from the sizes of simple factors. |
| [All quadratic traces through one hundred thousand](#all-quadratic-traces-through-one-hundred-thousand) | [Supporting argument](../../computations/programs/Yin_J_A0008/verify_quadratic_spread.py) | All ten marked traces and exact certificates at every quadratic prime in the interval. |

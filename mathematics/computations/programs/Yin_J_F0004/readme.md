---
author: Yin
---
# ms23-wick-derivatives

Context: [original integration finding](../../../audits/reviews/Yin_R_F0057_v1.md#ms23-integration-review-finding); [original derivative finding](../../../audits/reviews/Yin_R_F0057_v1.md#ms23-u004-corrected-finding); [MS23-U004](../../../audits/literature/MS23/Yin_U004.md#ms23-u004); [MS23 source units](../../../audits/literature/MS23/readme.md).

## Question and scope

756 exact binary-word free-derivative identities at q=0,2/7,-1/3 and lengths1--6, preserving the corrected Kronecker factor and finite range.

Target: [MS23-U004](../../../audits/literature/MS23/Yin_U004.md#ms23-u004), Proposition 5.1 and Example 5.2 in the 36-page published MS23 edition identified there.

### Scope and Independent Calculations

For every binary word of length 1–6, both free difference quotients and each $q\in\{0,2/7,-1/3\}$, compare coefficients of pairs of free monomials from two calculations:

1. Construct the Wick polynomial by q-Gaussian recurrence, with the required Kronecker delta in every contraction, and differentiate by Leibniz.
2. Enumerate $C(n+1)$ singleton/pair diagrams, count rectangular horizontal/vertical intersections independently, subtract the number of right singletons and sum the tensor products of Wick polynomials.

Every exponent `cross - len(right)` is asserted nonnegative before applying color constraints.
Coefficients are exact rationals; no intermediate degree or support is truncated.
Finite agreement supplements the all-degree induction in MS23-U004 without proving arbitrary words or parameters.
It establishes no infinite-series convergence, closability, q-Fock positivity, conjugate-variable norm or dual boundedness.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Exact finite-check program. |

## Reproduction

From the repository root:

```powershell
python mathematics/computations/programs/Yin_J_F0004/main.py
```

Only standard-library `fractions`, `functools` and `itertools` are needed.
The formula and enumeration are implemented directly, without input files or random seeds.
Arithmetic is `fractions.Fraction`, without floating tolerance.
The command uses a suitable available Python interpreter and is a present reproduction instruction, not a newly recorded run.
The program prints its finite result; no saved output or input dataset is required.

## Results and limits

All $3\cdot2\sum_{n=1}^6 2^n=756$ identities passed, with 252 at each q and no suppressed discrepancy.
Negative q tests crossing-power signs.
Degree three includes Example 5.2's contraction $-q\delta_{i,j_2}\delta_{j_3,j_1}1\otimes1$.
The recurrence corrects p. 6's missing Kronecker delta, required by Gaussian action and printed correctly on p. 27.

## Inspection summary

`ms23_estimates` executed the stated exact comparisons for Yin on 2026-09-09.
The independent constructions here are polynomial differentiation and geometric enumeration; this statement does not infer a separately performed review.

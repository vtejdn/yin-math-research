---
author: Yin
---
# dr97-tree-commutator

Context: [DR97 source units](../../../audits/literature/DR97/readme.md); [DR97-U002](../../../audits/literature/DR97/Yin_U002_v1.md#dr97-u002).

## Question and scope

Finite free-group endpoint/suffix and auxiliary scalar-column comparisons; preserve the explicitly weaker scalar-column evidence and absence of rationality/convergence certification.

Target: [DR97-U002](../../../audits/literature/DR97/Yin_U002_v1.md#dr97-u002), the edge cancellation identity in DR97 Proposition 5, pp. 617–618, and the auxiliary scalar column on p. 617.

### Scope and Mathematical Reduction

For free groups of ranks 0, 1 and 2, enumerate reduced coefficient words $h$ of lengths 0–5 and outward tree edges whose farther endpoint has length 1–4.
The direct calculation translates both endpoints by $h$, reduces them by a stack algorithm and selects the farther endpoint to apply $P^{-1}$.
An independent expression removes the suffix $(gx)^{-1}$ from $h$ and computes the residual multiplied on the right by $\bar x-1$.
Comparing signed integer dictionaries checks sign, suffix orientation, complete cancellation and multiplication order.

The extra scalar column checks $[P^{-1},h]q=-h$, using the source's zero action on $q$.
Rank zero has no edges and one scalar-column check.
The identity and total cancellation are included; no support truncation occurs during multiplication or reduction.
Linearity extends these finite basis checks to finite-support linear combinations on the same enumerated coefficient support, without an all-word conclusion.
The universal proof and restricted-support injectivity argument remain in DR97-U002.
This computation does not establish finite-rank equivalence, infinite-series operations, a norm bound, analytic realization or the Malcev–Neumann theorem.

## Files

| File | Role |
| --- | --- |
| [main.py](main.py) | Exact finite-check program. |

## Reproduction

From the repository root:

```powershell
python mathematics/computations/programs/Yin_J_F0001/main.py
```

Only the Python standard library is required, with exact integers and reduced words represented by tuples of signed generator labels.
There are no input files, random seeds, floating tolerances or intermediate cutoffs.
The command uses a suitable available Python interpreter and is a present reproduction instruction, not a newly recorded run.
The program prints its finite result; no saved output or input dataset is required.

## Results and limits

All 78,185 equalities passed: 77,688 edge identities and 497 scalar-column checks.
There were 1,892 nonzero edge defects, so the comparison includes nontrivial cancellation as well as vanishing cases.

| Rank | Coefficient words | Outward edges | Edge identities |
| --- | ---: | ---: | ---: |
| 0 | 1 | 0 | 0 |
| 1 | 11 | 8 | 88 |
| 2 | 485 | 160 | 77,600 |

## Inspection summary

On 2026-09-08 root wrote and ran the script; `dr97_analytic` independently read it against DR97-U002, derived the counts and reproduced the same result.
The reviewer checked that the endpoint calculation is independent of the suffix formula and that no intermediate word is truncated.
The scalar-column checks verify a prescribed expression and reduction of an already reduced word; they supply weaker independent evidence than the endpoint/suffix comparisons.
This is supplementary finite exact evidence, not a rationality, boundedness or convergence proof, formal verification or external review.

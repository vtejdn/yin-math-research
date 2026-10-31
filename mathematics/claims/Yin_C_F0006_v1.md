---
author: Yin
---

# Transfer under specified rational changes of generators

## Current assessment
[Selected decision](#decision-isolated-review-20261022)

## Rational Changes of Generators

<a id="statement"></a>

<a id="yin_c_f0006"></a>
## Yin_C_F0006: Transfer of the Original Rationality Criterion

Goal: [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001).
Date: 2026-09-08.
Provenance: project deduction, with examples specialized from [Miy22](../literature/pdf/Miy22.pdf).
Assessment: [selected assessment](#decision-isolated-review-20261022); [independent audit](../audits/reviews/Yin_R_F0062_v1.md#coordinate-transfer-finding).

Statement: for any tuple satisfying [Yin_C_F0001](Yin_C_F0001_v1.md#yin_c_f0001), the following coordinatewise Mobius maps, polynomial shears, and invertible affine linear changes preserve the truth of Yin_C_F0001, provided the transformed coordinates are normal and each stipulated denominator is boundedly invertible.
The maps below are bijections on eligible bounded dual systems, preserve the finite-rank class, and preserve the original bounded scalar division closure.
No arbitrary analytic change of variables is asserted to have these properties.

The proof uses the bounded polynomial/inverse rules from [Yin_C_F0002](Yin_C_F0002_v1.md#yin_c_f0002).
The known semicircular criterion for all bounded dual systems is the audited [Miy22-U003](../audits/literature/Miy22/Yin_U003.md#miy22-u003); its use in examples is a source specialization, not an independent reproving of Miy22.


Write `R_a` for bounded right multiplication by a, so `R_a` commutes with all left multipliers.
The elementary identity

\[
R_a P_\Omega R_b=\Theta(a\otimes b)
\]

uses traciality.
Right coefficients, rather than left coefficients, are essential: left coefficients need not commute with the other generators.

## Coordinatewise Mobius Transformations

Let `Y_j=(a_j X_j+b_j)(c_j X_j+d_j)^{-1}`, with scalar coefficients, `Delta_j=a_j d_j-b_j c_j != 0`, and `h_j=c_j X_j+d_j` invertible in M.
Put

\[
E_i=\Delta_i^{-1}R_{h_i}D_iR_{h_i}.
\]

The inverse rule gives

\[
[D_i,Y_j]=\delta_{ij}\Delta_j h_j^{-1}P_\Omega h_j^{-1}.
\]

Indeed `a_j-c_j Y_j=Delta_j h_j^{-1}`.
Moreover `R_h h^{-1}P h^{-1}R_h=P`: the first vacuum vector becomes 1, and the second functional is `zeta -> tau(h^{-1} zeta h)=tau(zeta)`.
Hence `[E_i,Y_j]=delta_ij P`.

For every bounded f,

\[
[E_i,f]=\Delta_i^{-1}R_{h_i}[D_i,f]R_{h_i},
\]

so their ranks are equal.
The inverse Mobius transformation is `X_j=(d_jY_j-b_j)(a_j-c_jY_j)^{-1}`, whose denominator is already boundedly invertible.
Thus the original scalar division closures are equal.
Normality of each X_j gives normality of each Y_j by continuous functional calculus, and W*(X)=W*(Y).

The transformation on bounded dual systems is bijective: its inverse is `D_i=Delta_i R_{h_i^{-1}}E_iR_{h_i^{-1}}`, obtained from the inverse Mobius coefficients.
Consequently Yin_C_F0001 for X is equivalent to Yin_C_F0001 for Y at its full quantifier over dual systems, without a separate dual-uniqueness assumption.

For example, from a standard free semicircular tuple S, `U_j=(S_j-i)(S_j+i)^{-1}` gives a tuple of unitaries that are not Haar; the exact criterion follows from Miy22 with `E_j=(2i)^{-1}R_{S_j+i}r_j^*R_{S_j+i}`.
This is a concrete non-Haar normal test class.

## Polynomial Shears

Let `Y_1=X_1+p(X_2,...,X_d)` and `Y_j=X_j` for `j>=2`.
Expand the finite polynomial derivative as

\[
\partial_k p(X)=\sum_{\ell}a_{k\ell}\otimes b_{k\ell}\quad(k\ge2).
\]

Define

\[
E_1=D_1,\qquad
E_k=D_k-\sum_\ell R_{a_{k\ell}}D_1R_{b_{k\ell}}\quad(k\ge2).
\]

Since `[D_1,Y_1]=P` and `[D_1,Y_j]=0` for `j>=2`, the displayed elementary identity cancels `[D_k,p]` exactly and gives `[E_k,Y_j]=delta_kj P`.
Every E-commutator is a finite linear combination of right-multiplied D-commutators.
Conversely, `D_1=E_1` and the displayed formula solves D_k by a finite sum of right-multiplied E-commutators.
Hence the two finite-rank sets agree.
Here even the polynomial algebras agree, since the inverse shear subtracts the same p.
The construction is invertible on all eligible dual systems.

Whenever the new generators are normal this transports Yin_C_F0001.
A readily usable class is selfadjoint X and selfadjoint p.
For instance `Y_1=S_1+S_2^2-1`, `Y_2=S_2` (and other S unchanged) is a nonfree selfadjoint tuple satisfying Yin_C_F0001 by Miy22.
Nonfreeness is witnessed by `tau(Y_1(Y_2^2-1))=1`, while both factors are centered.
Its explicit dual is `E_1=r_1^*`, `E_2=r_2^*-R_{S_2}r_1^*-r_1^*R_{S_2}`.
Repeated normality-preserving shears, invertible linear changes, and coordinatewise Mobius maps provide further verified test classes.


## Invertible Affine Linear Changes

For columns Y=A X+b, with A in GL_d(C) and b in C^d, put E=A^{-T}D.
Entrywise E_i=sum_l (A^{-1})_{li}D_l, so [E_i,Y_j]=sum_l (A^{-1})_{li}A_{jl}P=delta_ij P.
The inverse map is D=A^T E.
Finite-rank conditions agree in both directions, and both polynomial algebras agree.
Retain only changes for which every Y_j is normal; real A and b suffice when every X_j is selfadjoint.
These formulas also verify the linear changes used in the composition statement above.

## Scope

These operations can be composed while their stated conditions continue to hold.
They give concrete non-Haar normal examples and nonfree selfadjoint examples, without asserting that every tuple admitting a bounded dual system can be reached this way.
Arbitrary norm-convergent sums of finite-rank defects can have infinite rank; analytic transport requires another argument.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:20 |
| status | proved |
| reason | Select the actual previously adopted finding explicitly, preserving its original date, complete checked mathematical scope and retained limits while declaring its actual known or genuinely unestablished relationship. The statement, argument, dependencies and mathematical assessment are unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#coordinatewise-mobius-transformations) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Actual complete finding](../audits/reviews/Yin_R_F0062_v1.md#coordinate-transfer-finding) | Complete coordinatewise Mobius, polynomial shear and inverse-transpose affine changes, their bounded inverse substitutions and finite-rank classes, both concrete non-Haar/nonfree examples and finite composition limits. Normality and bounded denominator hypotheses remain explicit; no general tuple classification or infinite analytic composition. |


### Decision isolated-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:48 |
| status | proved |
| reason | Adopt the actually performed context-isolated independent whole-argument finding after its complete comparison with the old review; fixed mathematics and historical decisions remain at their original scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#coordinatewise-mobius-transformations) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New isolated finding](../audits/reviews/Yin_R_F0062_v1.md#coordinate-transfers) | Complete coordinatewise Mobius, polynomial shear and inverse-transpose affine transfers, all eligible bounded duals, bounded scalar closures, concrete examples and finite-composition limits. |

## Historical assessments


<a id="decision-candidate-0002"></a>
### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#coordinatewise-mobius-transformations) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0062_v1.md#coordinate-transfer-finding) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).



These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0062_v1.md#coordinate-transfer-finding).

Material covered by that review: [Exact material](Yin_C_F0006_v1.md).

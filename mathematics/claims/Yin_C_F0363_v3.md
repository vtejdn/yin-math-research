---
author: Yin
---

# Fixed-dimensional Schur restoration under independent panel draws

<a id="statement"></a>
## Product sampling of the exposed column

Use the [coefficient span, projection bounds and Fourier hypotheses](Yin_C_F0363_v2.md#statement) for a fixed \(m\) and fixed finite number of nodes.
Conditional on the history, the joint law of the \(2m\) blocks of the *actual column* \(g\) is the product of its panel marginal laws.
The panels exhaust the column, or all remaining coordinates are included in the history and the conditional product requirement holds after this inclusion.
Each panel is drawn from its indicated raw-coordinate law, with conditionally independent entries when the disjoint-basis Fourier input requires them.
The unchanged coefficients, errors, lower-degree polynomials and normalization constants are measurable with respect to this same history.
Each difference vector in the hypotheses is formed from two independent copies of its own panel marginal.
In particular an iid fresh Wigner strict-upper physical column split over deterministic disjoint coordinate sets meets this sampling condition.

Then for \(s\) prescribed nodes and fixed \(C_0\), the probability of simultaneous modulus at most \(C_0|c_z|\) of the \(m\)-direction Schur statistics is
\[
                 O(n^{-s/2^{2m+1}})+O(e^{-cn})
\]
conditionally on every admissible history.
As in the [cyclic-pencil applicability statement](Yin_C_F0363_v2.md#scope), this controls individual transitions given an initial determinant comparison, regularity and the specified uniform guards.

<a id="argument"></a>
## The product cube and the two-panel estimates

Use the [polarized determinant recursion](Yin_C_F0363_v2.md#argument) on independent draws of the conditional panel differences.
For each \(q\), the detectable linear functional of the last pair evaluates to \(U_{q-1,z}\) at the specified invertible matrix \(B_z\).
The two-panel bound after projection removes the terms involving an earlier vector paired with the final panel.
Induction bounds the smallness probability of the complete difference on \(s\) nodes by \(O(n^{-s/2})+O(e^{-cn})\).
For the original small-ratio event, take two independent copies per panel.
Conditional independence makes their joint law the Cartesian product so that the repeated Cauchy--Schwarz inequality raises the event probability to \(2^{2m}\).
The full difference on that cube cancels the lower degrees and equals \(2^m c_z U_{m,z}\) at each node.
Taking the root gives the assertion.

<a id="failure"></a>
## Dependence between the actual panels

Panel marginal bounds by themselves would not justify this final resampling.
For \(m=1\) take two equal panels of length \(l\), each marginal a vector \(x\) of independent fair signs, and set \(g=(x,x)\).
With the off-diagonal identity blocks and zero diagonal blocks of \(K\), \(g^{\mathsf T}Kg=2l\) for every realization.
Subtracting the constant \(2l\) yields an identically zero statistic.
The off-diagonal kernel is an isometry; the usual independent-copy sign differences in its individual panels have the spread and Fourier estimates of the [bounded sign argument](Yin_C_F0351_v5.md#sign-flag-area).
The example violates the conditional product law of the actual panels and supplies no counterexample for the original Wigner application.

## Current assessment
[Selected decision](#decision-panel-product-reviewed)

## Assessment history

### Decision panel-product-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:36 |
| status | open |
| reason | The conditional product law of the actual panels is explicit and gives the Cartesian resampling inequality used in the fixed-dimensional lemma. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Conditional product theorem](#statement) | Exact additional sampling requirement and quantitative conclusion. |
| argument | [Full proof](#argument) | Polarization under the stated resampling law. |
| support | [Dependent-panel failure](#failure) | The separate panel marginal estimates do not imply the product condition. |
| support | [Coefficient and spread hypotheses](Yin_C_F0363_v2.md#statement) | Invertible matrix in the coefficient span, projected output and Fourier conditions. |

### Decision panel-product-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:48 |
| status | proved |
| reason | The actual joint product sampling permits the full Cartesian cube; the polarized determinant recursion proves the fixed-dimensional probability bound under its stated spread conditions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact theorem](#statement) | The actual joint product sampling permits the full Cartesian cube; the polarized determinant recursion proves the fixed-dimensional probability bound under its stated spread conditions. |
| argument | [Complete argument](#argument) | The hypotheses, parameter scope and conclusions of the fixed proof. |
| review | [Independent whole-proof assessment](../audits/reviews/Yin_R_F0371_v3.md#panel-product-whole-proof) | The stated mathematical scope and remaining restrictions. |

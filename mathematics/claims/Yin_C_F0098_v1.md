---
author: Yin
---

# Weighted or permutation-invariant recognizable q-circular coefficients give bounded scalar reconstruction

## Current assessment
[Selected decision](#decision-isolated-review-2026-10-22)

## 5. A sufficient weighted coefficient condition with bounded reconstruction

<a id="statement"></a>
<a id="yin_c_f0098"></a>

<a id="weighted-recognizable-reconstruction"></a>

The original equation (2.1) is the [KM26 homogeneous scalar norm input](../audits/literature/KM26/Yin_U001.md#km26-u001).
The original equation (3.3) and coefficient conventions are retained in [L_F0024 Section 3](../ledger/Yin_L_F0024_v1.md#3-actual-q-holomorphic-coefficient-geometry): the q-symmetrizer norm is at most [n]_(|q|)! and then (1-|q|)^(-n).
These are the same original accepted norm and elementary coefficient inputs reviewed in the original joint recurrence/reconstruction finding, not new assumptions.

This is a proof draft for a restricted coefficient statement.
Let c be a finite q-circular system, r=|q|, and let \(\alpha_w\) be recognizable.
Assume

\[
\sum_w |\alpha_w|^2(1-r)^{-|w|}<\infty.
\tag{5.1}
\]

Then the homogeneous series \(\sum_w\alpha_wc_w\) converges in operator norm, and its sum belongs to

\[
\operatorname{Div}_{\mathcal M}\mathbb C\langle c_1,\ldots,c_d\rangle,
\qquad \mathcal M=W^*(c).
\tag{5.2}
\]

Here (5.1) is stronger than actual q-L2 summability in general; no converse is asserted.

To prove the assertion, put \(s=(1-r)^{-1/2}\) and \(\beta_w=s^{|w|}\alpha_w\).
The sequence beta remains recognizable.
Yin_C_F0015's scalar finite-state argument gives

\[
\sum_{|w|=n}|\beta_w|^2\le C\rho^{2n},\qquad 0<\rho<1.
\]

By (3.3), this dominates the q-energy of the original homogeneous block.
Equation (2.1) then gives absolute operator-norm convergence by degree.

For scalar reconstruction, choose a reachable and observable realization \(\alpha_w=\lambda A_w\gamma\).
As in Yin_C_F0017 Section 4, every matrix entry of A_w is a finite linear combination of the padded coefficients \(\alpha_{uwv}\), with u,v in fixed finite sets.
For fixed u,v,

\[
\sum_w s^{2|w|}|\alpha_{uwv}|^2
\le s^{-2(|u|+|v|)}\sum_z s^{2|z|}|\alpha_z|^2<\infty.
\]

Thus (5.1) holds entry by entry for the matrices A_w.
Each entry is recognizable, so the previous scalar estimates prove

\[
\sum_{n\ge0}\left\|\sum_{|w|=n}(A_w)_{ij}c_w\right\|<\infty.
\]

With \(T=\sum_iA_i\otimes c_i\), multiplicativity of c_w identifies these sums with the entries of \(T^n\).
Therefore \(\sum_n\|T^n\|<\infty\), and \((I-T)^{-1}\) is bounded.
Yin_C_F0017 Section 5's small-power Schur elimination gives \((I-T)^{-1}\in M_N(\operatorname{Div}_{\mathcal M}\mathbb C\langle c\rangle)\).
The scalar output \(\lambda(I-T)^{-1}\gamma\) equals the norm sum and proves (5.2).
The zero series is immediate.
This uses scalar estimates on finitely many matrix entries, not an unverified operator-coefficient Haagerup inequality.

## 6. A symmetric coefficient subclass where actual L2 suffices

<a id="symmetric-recognizable-subclass"></a>

There is a sharper proof draft, valid also for negative q.
Suppose alpha is recognizable and invariant under permutation of the letters within each word:

\[
\alpha_{i_1\cdots i_n}
=\alpha_{i_{\pi(1)}\cdots i_{\pi(n)}}
\quad(\pi\in S_n).
\tag{6.1}
\]

A finite realization with commuting state matrices A_i is a sufficient way to ensure (6.1).
The physical variables c_i are not required to commute.

Assume the specified holomorphic series is square summable in its actual q-inner product:

\[
\sum_n\left\|\sum_{|w|=n}\alpha_wc_w\right\|_2^2<\infty.
\tag{6.2}
\]

Then the same bounded scalar reconstruction conclusion (5.2) follows.

Indeed, (6.1) makes every xi_n in (3.1) invariant under all tensor permutations, so

\[
P_q^{(n)}\xi_n=[n]_q!\xi_n,
\qquad
e_n=[n]_q!\sum_{|w|=n}|\alpha_w|^2.
\tag{6.3}
\]

By the bounds in [C_F0097, equation (4.3)](Yin_C_F0097_v1.md#one-state-energy-obstruction), condition (6.2) is equivalent to

\[
\sum_w |\alpha_w|^2(1-q)^{-|w|}<\infty.
\tag{6.4}
\]

Apply Yin_C_F0015's scalar energy argument after rescaling each letter by \((1-q)^{-1/2}\).
It gives exponential decay of the weighted ordinary energy; (6.3) and the bounded factors kappa_n give exponential decay of the actual q-energy.
Equation (2.1) gives norm convergence.

For the complete matrix inverse, again use the minimal-realization identity expressing each \((A_w)_{ij}\) as a finite linear combination of \(\alpha_{uwv}\).
Each padded coefficient sequence remains permutation invariant in the middle word w and satisfies the weighted summability (6.4).
Thus every matrix-entry sequence has the same exponential q-energy bound.
The construction and scalar elimination of Section 5 now apply verbatim.
No assertion that an arbitrary affiliated rational evaluation has this Taylor series is used.

For example, one-state coefficients \(\alpha_w=t_{i_1}\cdots t_{i_n}\) satisfy

\[
\sum_{|w|=n}|\alpha_w|^2=\left(\sum_i|t_i|^2\right)^n.
\]

The displayed series is q-square-summable precisely when \(\sum_i|t_i|^2<1-q\), and its bounded sum is \((1-\sum_i t_ic_i)^{-1}\).
This example specifies the Taylor branch and makes no claim about affiliated inverses outside that branch.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:15 |
| status | proved |
| reason | Adopt the exact actual original finding at its disclosed unknown initial-context relationship. Preserve mathematical status, statement, selected proof, dependencies and historical decisions; no new mathematical proof version or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0098) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0109_v1.md#outcome-and-boundaries) | Both original weighted and symmetric recognizable q-circular reconstruction proofs, actual bounded matrix inverse and scalar elimination, with all coefficient/evaluation limits. Actual original finding with unknown initial-context relationship; original date and accepted inputs preserved. |


### Decision isolated-review-2026-10-22

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:39 |
| status | proved |
| reason | Adopt the new isolated complete finding on the unchanged fixed mathematics and its actual necessary interfaces. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0098) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New isolated complete finding](../audits/reviews/Yin_R_F0108_v1.md#isolated-q-reconstruction-finding) | Complete Sections 5 and 6 weighted and symmetric recognizable q-circular reconstruction, both bounded matrix inverses and scalar elimination, including negative q and all coefficient/Taylor-branch limits; no separate recurrence-obstruction review. |

The statement, selected fixed argument and mathematical scope are unchanged.
The separate reviewing agent formed all assigned initial findings from the complete mathematics before reading the old conclusions, then compared the necessary original findings and limitations.
Original dates, historical unknown relationships, source depths and any negative finding or repair attribution remain at their responsible retained homes.
This decision selects the new applicable finding without retroactively changing an earlier assessment.

## Historical assessments


These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0098) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0109_v1.md#original-f0059-account) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0109_v1.md#original-f0059-account).

Material covered by that review: [Exact material](Yin_C_F0097_v1.md), [Exact material](Yin_C_F0098_v1.md), [Exact material](../ledger/Yin_L_F0024_v1.md) (together retain the original whole-source scope).

---
author: Yin
---

# R-diagonal holomorphic spectrum inclusion and equal polynomial hulls

## Current assessment
[Selected decision](#decision-isolated-whole-review-2026-10-22)

## Yin_C_F0093: Holomorphic Spectral Comparison for Free R-Diagonal Families

<a id="yin_c_f0093"></a>

Provenance: project deduction, 2026-09-11.
Initial assessment: proof draft, awaiting separate review.
Current assessments are recorded in the [selected assessment](#current-assessment).
No novelty claim is made.
Proof dependencies: [Yin_C_F0017](Yin_C_F0017_v1.md#yin_c_f0017), [Miy22-U002](../audits/literature/Miy22/Yin_U002.md#miy22-u002), [Miy26-U005](../audits/literature/Miy26/Yin_U005.md#miy26-u005), and the usual Banach-algebra spectral-radius and polynomial spectral-mapping theorems already used in Miy26-U003.

### Statement

Let \(b_1,\ldots,b_d\), \(1\le d<\infty\), be free identically distributed bounded R-diagonal elements in \((\mathcal M,\tau)\), normalized by \(\|b_i\|_2=1\).
Let \(c_1,\ldots,c_d\) be a standard free circular family in a finite faithful tracial von Neumann algebra \((\mathcal N,\varphi)\), so \(\varphi(c_i^*c_j)=\delta_{ij}\).
For every scalar noncommutative polynomial \(P\) with no adjoint indeterminates,

\[
\sigma_{\mathcal M}(P(b))
\subseteq\sigma_{\mathcal N}(P(c))
=\sigma_{B(\mathcal F(\mathbb C^d))}(P(l)).
\tag{2}
\]

For every scalar one-variable polynomial \(q\),

\[
r_{\mathcal M}(q(P(b)))=r_{\mathcal N}(q(P(c))).
\tag{3}
\]

In particular, the two compact spectral sets in the first inclusion have the same polynomial hull, where for a compact \(K\subset\mathbb C\)

\[
\widehat K=\{z\in\mathbb C:
 |q(z)|\le\sup_{w\in K}|q(w)|
 \text{ for every }q\in\mathbb C[z]\}.
\tag{4}
\]

The inclusion (2) can be strict: take \(d=1\), \(b_1\) a Haar unitary and \(P(z)=z\).
No freeness, R-diagonality or tracial property is asserted for the creation operators themselves.

<a id="yin_c_f0093-proof"></a>
### Proof

**Step 1: identify the coefficient geometry.**
The word calculation in Yin_C_F0017 gives

\[
\tau(b_v^*b_w)=\delta_{v,w}
=\varphi(c_v^*c_w)
\tag{5}
\]

for all positive words, including the empty word.
These are bases of the respective closed holomorphic subspaces, not of their whole tracial \(L^2\) spaces.
For every holomorphic polynomial \(Q\), (5) identifies the \(L^2\) norms of \(Q(b)\), \(Q(c)\) and its formal coefficient vector.

**Step 2: build the inverse from the circular resolvent.**
Suppose \(\lambda\notin\sigma(P(c))\).
By Miy26-U005,

\[
B=\lambda-P(l)
\]

has a bounded inverse on full Fock space.
Write \(a_0=P(0)\).
The vacuum coefficient of \((a_0-P(l))\xi\) is zero for every \(\xi\), so that operator cannot be onto.
Consequently \(\lambda-a_0\ne0\).

Set \(B^{-1}\Omega=\sum_w\alpha_w e_w\).
This coefficient sequence is square summable.
Comparing coefficients in \(BB^{-1}\Omega=\Omega\) determines it uniquely by length, because the constant coefficient \(\lambda-a_0\) is nonzero.
It is therefore the formal expansion of

\[
(\lambda-P(z))^{-1}
\]

at zero.
This is a scalar rational series regular at zero.
The rational-series/recognizability equivalence in Miy22-U002 gives finite residual dimension for \(\alpha\).

Yin_C_F0017 now supplies an element

\[
f=\sum_w\alpha_w b_w
\in\operatorname{Div}_{\mathcal M}\mathbb C\langle b\rangle
\subseteq\mathcal M,
\tag{6}
\]

whose homogeneous partial sums converge both in norm and in \(L^2\).
Multiplication on the left by the bounded polynomial \(\lambda-P(b)\) preserves \(L^2\) convergence.
In the holomorphic word basis its coefficients are the finite convolution of those of \(\lambda-P\) and \(f\).
The formal inverse identity makes them the coefficients of \(1\), hence

\[
(\lambda-P(b))f=1.
\]

The same argument on the right, using bounded right multiplication and the other formal inverse identity, gives \(f(\lambda-P(b))=1\).
Thus \(\lambda\notin\sigma(P(b))\), proving (2).
No inverse that was initially only an affiliated operator has been used in a bounded-commutator identity.

**Step 3: compare powers without assuming reverse spectral inclusion.**
From the homogeneous estimate in Yin_C_F0017, there is \(C\ge1\), depending on the common distribution, such that for every holomorphic polynomial \(Q\) of degree at most \(N\),

\[
\begin{aligned}
\|Q(b)\|
&\le C\sum_{m=0}^{N}\sqrt{m+1}\,\|Q_m(b)\|_2\\
&\le C\left(\frac{(N+1)(N+2)}2\right)^{1/2}\|Q(b)\|_2\\
&\le C(N+2)\|Q(b)\|_2.
\end{aligned}
\tag{7}
\]

Orthogonality of the homogeneous terms justifies the middle bound.
For \(k=\deg Q\), the degree of \(Q^n\) is at most \(nk\).
Combining (7) with \(\|Q(b)^n\|_2\le\|Q(b)^n\|\) and the Banach-algebra spectral-radius formula gives

\[
r(Q(b))=\lim_{n\to\infty}\|Q(b)^n\|_2^{1/n}.
\tag{8}
\]

Constants, the zero polynomial and nilpotent evaluations satisfy the same conclusion by these inequalities.
Apply the same estimate to the circular family and use (5) for \(Q^n\).
The two \(L^2\) norms are exactly equal for every \(n\), so \(r(Q(b))=r(Q(c))\).
Choosing \(Q=q\circ P\) proves (3).
Finally spectral mapping identifies \(r(q(P(b)))\) with \(\max_{z\in\sigma(P(b))}|q(z)|\), and likewise for \(c\).
Definition (4) then proves equality of the polynomial hulls.
QED.

<a id="yin_c_f0093-review"></a>
### Review and boundary checks

The author's self-check verified normalization, the constant polynomial and \(\lambda=P(0)\) cases, both inverse identities, the distinction between the positive-word subspace and full \(L^2\), and the subexponential factor in (7).
The Haar singleton checks the direction of inclusion and shows why equal spectral radii, even after every scalar polynomial test, do not identify the full spectrum.
This is a complete candidate proof, but a separate review was pending at the initial checkpoint.
No numerical experiment or formal verification is claimed.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:54 |
| status | proved |
| reason | Adopt the exact actual original finding at its complete reviewed scope while preserving the mathematical assessment, fixed argument, dependencies and historical decisions. The original initial context-isolation fact remains unknown; no new or redated review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0093-proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0105_v1.md#obligations-and-decisive-checks) | Actual original complete C_F0093 finding at its disclosed accepted-input scope and unknown initial-context relationship; historical source precision and limits remain at this retained original finding. |


### Decision isolated-whole-review-2026-10-22

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:21 |
| status | proved |
| reason | Adopt the actual new isolated whole-proof finding for the unchanged fixed statement and selected argument; retain all original assessments, source depths and useful negative boundaries at their historical scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#yin_c_f0093-proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New whole-proof finding](../audits/reviews/Yin_R_F0105_v1.md#fresh-c42-whole) | Actual isolated whole-proof inspection at this exact fixed input, including all necessary accepted-input applicability and stated limits; historical findings remain separately unknown. |

## Historical assessments


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
| argument | [Exact material](#yin_c_f0093-proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0105_v1.md#obligations-and-decisive-checks) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

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
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0105_v1.md#obligations-and-decisive-checks).

Material covered by that review: [Exact material](Yin_C_F0093_v1.md), [Exact material](Yin_C_F0094_v1.md), [Exact material](../ledger/Yin_L_F0023_v1.md) (together retain the original whole-source scope).

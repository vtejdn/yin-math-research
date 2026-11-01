---
author: Yin
---

# Normal one-dimensional commutative algebras admit positive bounded denominators

## Current assessment
[Selected decision](#decision-isolated-review-2026-10-22)

## Yin_C_F0090: Local Discrete Valuations and a Positive Denominator

<a id="statement"></a>
<a id="yin_c_f0090"></a>

Date: 2026-09-11.
Agent contribution: root (the coordinating agent).
Record kind: Claim/proof module for [Yin_T_F0003](../tasks/Yin_T_F0003_v1.md#yin_t_f0003) and [Yin_S_F0013](../strategies/Yin_S_F0013.md#s_f0013).
Provenance: project deduction from standard localization.
Initial assessment: complete proof draft, self-checked, awaiting independent review; the [selected assessment](#decision-candidate-0002) records the current assessment.
No optional Role or novelty claim is assigned.

### Statement and conventions

Let \(K\) be a nonempty compact Hausdorff space, let \(\mu\) be a regular Borel probability measure with full support, and put \(\mathcal M=L^\infty(K,\mu)\).
Let \(A\subset C(K)\) be a unital complex subalgebra closed under complex conjugation.
Assume that \(A\), as an abstract commutative ring, is a Noetherian integrally closed domain of Krull dimension at most one.
Then

\[
\operatorname{Div}_{L^0(\mathcal M)}A\cap\mathcal M
=\operatorname{Div}_{\mathcal M}A.
\tag{46.1}
\]

More concretely, every element of the left side has the form \(vQ^{-1}\), where \(v,Q\in A\) and \(Q=\sum_{j=1}^n|q_j|^2\) is strictly positive everywhere on \(K\).
Thus it also has a continuous representative.
The algebra \(A\) need not be a principal ideal ring or the polynomial algebra in a single coordinate.

The statement can be used in the joint spectral representation of a commuting normal tuple when its adjoint-closed evaluated polynomial algebra satisfies these ring hypotheses.
It does not silently adjoin adjoints to an unstarred algebra.
Scalar division closure follows [MSY23 Definition 4.10](../audits/literature/MSY23/Yin_U003.md#definitions-47-and-410-two-closures-in-one-ambient-algebra).
An integrally closed domain contains every element of its fraction field integral over it.
The local discrete valuation characterization, with the field exception preserved, is the accepted [The26b interface](../audits/literature/The26b/Yin_U001.md#local-valuation-interface).
Ring normality and operator normality are different notions.

### Reuse and source boundary

[Yin_C_F0087](Yin_C_F0087_v1.md#yin_c_f0087) supplies global principal-ideal cancellation; [Yin_C_F0088](Yin_C_F0088_v1.md#yin_c_f0088) isolates the singular cusp obstruction.
Existing ledger/audit/local-source searches for Dedekind domains, discrete valuations and denominator ideals gave no suitable registered local-to-global criterion.
A primary-source search then located The26b tags 034X and 00PD.
Their exact statements were checked and accepted as external inputs.
Searches concerning locally bounded rational functions also located real-algebraic work, but no theorem from those uninspected leads is used.
The local deduction here combines essential boundedness for an arbitrary full-support measure with one positive invertible denominator; historical novelty is not asserted.

<a id="yin_c_f0090-p1"></a>
### Proof Yin_C_F0090-P1

Full support makes \(C(K)\to L^\infty(K,\mu)\) injective, since a nonzero continuous function is bounded away from zero on a nonempty open set of positive measure.
By Yin_C_F0087's commutative fraction calculation, write a bounded \(f\) in the left side as

\[
f=pq^{-1},\qquad p,q\in A,\qquad q\ne0\quad\mu\text{-almost everywhere}.
\tag{46.2}
\]

Let \(r=p/q\) in the abstract fraction field of \(A\).
This does not embed that entire field in \(L^0(\mathcal M)\): other nonzero elements of \(A\) may vanish on sets of positive measure.
Only the displayed denominator is already admissible.
If \(p=0\), the result is immediate; assume \(r\ne0\).

For \(x\in K\), evaluation has maximal kernel \(\mathfrak m_x=\{a\in A:a(x)=0\}\).
If this kernel is zero, the complex-algebra evaluation isomorphism \(A\cong\mathbb C\) forces \(A=\mathbb C1\), settling the claim.
Otherwise The26b tag 034X makes \(A_{\mathfrak m_x}\) a discrete valuation ring.

We claim \(r\in A_{\mathfrak m_x}\).
If not, tag 00PD gives

\[
r=u\pi^{-k},\qquad k\ge1,
\tag{46.3}
\]

where \(u\) is a unit and \(\pi\) generates the maximal ideal of this local ring.
Represent \(u,\pi\) by local fractions with denominators nonzero at \(x\).
They are continuous on a neighborhood \(U\) of \(x\), with \(u(x)\ne0\), \(\pi(x)=0\).
These local denominators are not asserted to be invertible as affiliated operators globally.

Choose \(L>\|f\|_\infty\).
Shrink \(U\) so that \(|u|>c>0\) and \(|\pi|^k<c/L\) there.
Clearing local denominators in \(r\pi^k=u\) gives

\[
(p/q)\pi^k=u
\]

pointwise on \(U\cap\{q\ne0\}\).
Here \(u\ne0\) forces \(\pi\ne0\), so \(|p/q|>L\).
Full support gives \(\mu(U)>0\), and (46.2) makes the omitted zero set null, contradicting the essential bound.
Thus \(r\in A_{\mathfrak m_x}\) for every \(x\).
This argument includes atoms and isolated support points.

For each \(x\), local membership yields \(q_x,p_x\in A\) with \(q_x(x)\ne0\) and \(q_xr=p_x\) in the abstract fraction field.
Compactness supplies a finite subcover from the open sets \(\{q_x\ne0\}\), say \(q_1,\ldots,q_n\), with corresponding \(p_j\).
Put

\[
Q=\sum_jq_j^*q_j\in A,\qquad v=\sum_jq_j^*p_j\in A.
\tag{46.4}
\]

Adjoint closure is used exactly in this step.
The continuous \(Q\) is strictly positive on compact \(K\), so \(Q^{-1}\in C(K)\subset\mathcal M\).
From \(p_jq=q_jp\) in \(A\), using the valid affiliated inverse \(q^{-1}\) gives \(p_j=q_jf\), regardless of kernels of the individual \(q_j\).
Thus \(Qf=v\), and \(f=vQ^{-1}\in\operatorname{Div}_{\mathcal M}A\).
The opposite inclusion follows from preservation of bounded inverses in \(L^0(\mathcal M)\).
QED.

### Checks and limits

The proof distinguishes the abstract fraction field, valid affiliated denominators and local fractions on neighborhoods.
It checks scalar/zero cases, atoms, the nonzero-maximal-ideal exception and the positive denominator.
Only the discrete valuation condition at evaluation ideals is actually needed.
The stated global ring condition is sufficient.

Yin_C_F0088 shows why a singular one-dimensional algebra cannot simply replace the normal-domain hypothesis.
Normality alone in higher dimension gives no discrete valuation local ring at a support point.
Neither this argument nor Yin_C_F0087 proves stability under noncommutative free products.
At authorship, computation, formal verification and independent review were not performed.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:05 |
| status | proved |
| reason | Adopt the exact actual original finding and disclosed unknown initial-context relationship, preserving the mathematical assessment, fixed statement and argument, dependencies and historical decisions. No new review or mathematical proof version is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0090-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0091_v1.md#obligations-and-decisive-checks) | Whole C_F0090 local discrete-valuation and positive-denominator theorem, including source tags and all ring/measure/denominator limits. Actual original finding with unknown initial-context arrangement; historical date and accepted-input depth unchanged. |


### Decision isolated-review-2026-10-22

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:39 |
| status | proved |
| reason | Adopt the new isolated complete finding on the unchanged fixed mathematics and its actual necessary interfaces. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0090-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New isolated complete finding](../audits/reviews/Yin_R_F0091_v1.md#isolated-local-valuation-finding) | Whole fixed local-valuation theorem and positive-denominator construction, exact source hypotheses, field/atomic exceptions and original scalar closure limits. |

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

Recorded review label: independently reviewed.

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

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0090-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0091_v1.md#original-normal-curve-account) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0091_v1.md#original-normal-curve-account).

Material covered by that review: [Exact material](Yin_C_F0090_v1.md), [Exact material](Yin_C_F0091_v1.md) (together retain the original whole-source scope).

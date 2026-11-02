---
author: Yin
---

# Two projections can have a bounded affiliated rational expression outside their C*-algebra

## Current assessment
[Selected decision](#decision-isolated-review-2026-10-22)

## 3. Why arbitrary two projections do not suffice

<a id="statement"></a>
<a id="yin_c_f0099"></a>

The original shared [question and closure convention](../ledger/Yin_L_F0025_v1.md#1-question-source-reuse-and-accepted-inputs) fixes A=C<p,q>, M=W*(p,q) and the equality of the affiliated bounded intersection with scalar division closure inside M.
The original [generic matrix setting and rational-expression induction](../ledger/Yin_L_F0025_v1.md#2-algebra-and-the-generic-matrix-model) fixes T=1-p-q+pq+qp, b=pq(1-p), s(t)=sqrt(t(1-t)), the four character projections and the matrix normal form cited by the original equation numbers below.
Those are unchanged parts of R_F0067's original combined-file input, made explicit here without adding a hypothesis or enlarging the theorem.

### 3.1 An explicit finite tracial model

Let \(\mu\) be normalized Lebesgue measure on \((0,1/2)\), and set
\[
 \mathcal M=\mathbb C\oplus M_2(L^\infty((0,1/2),\mu)),\qquad
 \tau(c,F)=\tfrac12c+\tfrac12\int\operatorname{tr}_2(F(t))\,d\mu(t).
 \tag{8}
\]
This is a faithful normal tracial state.
Define
\[
 p=1\oplus\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
 q=0\oplus\begin{pmatrix}t&s(t)\\s(t)&1-t\end{pmatrix}.
 \tag{9}
\]
The two entries are projections, and they generate \(\mathcal M\): the central parameter is \(0\oplus tI_2\); its zero spectral projection isolates the scalar summand, while on the remaining part the polar decomposition of \(b=sE_{12}\) gives the matrix unit \(E_{12}\).
Bounded Borel functions of \(t\) and these matrix units generate the generic summand.

Let
\[
 x=p+b+b^*+2T(1-p)\in A.
 \tag{10}
\]
Its atomic value is 1 and its generic matrix is
\[
 x(t)=\begin{pmatrix}1&s(t)\\s(t)&2t\end{pmatrix},
 \qquad\det x(t)=t(1+t)>0.
 \tag{11}
\]
Thus \(x\) is positive and injective, hence invertible in \(L^0(\mathcal M)\).
Its inverse is unbounded near \(t=0\).
Nevertheless
\[
 f=px^{-1}p
   =1\oplus\begin{pmatrix}2/(1+t)&0\\0&0\end{pmatrix}
 \tag{12}
\]
is bounded, with norm 2, and belongs to \(\operatorname{Div}_{L^0(\mathcal M)}A\).

### 3.2 Exclusion from the bounded division closure

Every polynomial \(a(p,q)\) in this model has a generic matrix function continuous on \([0,1/2]\), and its scalar coordinate equals the \((1,1)\) entry of that function at 0.
This is true on the generators and is preserved by their algebraic operations.
Full support makes the essential generic norm equal to the uniform norm of a continuous representative.
Therefore every element of \(C^*(p,q)\) retains this endpoint matching condition under norm limits.

The generic continuous representative in (12) has \((1,1)\) value 2 at 0, whereas the scalar coordinate is 1.
Hence \(f\notin C^*(p,q)\).
The unital C*-algebra \(C^*(p,q)\) is closed under inverses that exist in \(\mathcal M\): for \(y\) invertible in \(\mathcal M\), the positive element \(y^*y\) is bounded below, and continuous functional calculus gives \((y^*y)^{-1}y^*\in C^*(p,q)\).
Consequently
\[
 f\notin\operatorname{Div}_{\mathcal M}A,
 \qquad
 \operatorname{Div}_{L^0(\mathcal M)}A\cap\mathcal M
   \supsetneqq\operatorname{Div}_{\mathcal M}A.
 \tag{13}
\]
Equivalently, the endpoint projection is an explicit bounded affiliated rational expression:
\[
 e_{10}=2(1+T)^{-1}p-px^{-1}p=1\oplus0,
 \tag{14}
\]
and it also violates endpoint matching.
Its construction uses an **unbounded** intermediate inverse \(x^{-1}\).

This pair is not free.
For example \(\tau(p)=3/4\), \(\tau(q)=1/4\), but \(\tau(pq)=1/16\ne3/16=\tau(p)\tau(q)\).
Thus (13) does not refute the two-free-projection result or general free-product stability.
The obstruction is a surviving single character at an endpoint of the generic support.


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
| argument | [Exact material](#32-exclusion-from-the-bounded-division-closure) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0107_v1.md#3-arbitrary-pair-counterexample) | Complete arbitrary-two-projection counterexample, actual affiliated inverse and C*-endpoint exclusion, with the original shared matrix setting. Actual original finding with unknown initial-context relationship; original date and accepted inputs preserved. |


### Decision isolated-review-2026-10-22

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:40 |
| status | proved |
| reason | Adopt the new isolated complete finding on the unchanged fixed mathematics and its actual necessary interfaces. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#32-exclusion-from-the-bounded-division-closure) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New isolated complete finding](../audits/reviews/Yin_R_F0107_v1.md#isolated-two-projection-counterexample) | Whole arbitrary-pair counterexample with the actual common matrix setting, affiliated unbounded inverse, bounded output, C*-endpoint exclusion and strict bounded scalar-closure separation. |

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
| argument | [Exact material](#32-exclusion-from-the-bounded-division-closure) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0107_v1.md#original-f0067-account) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0107_v1.md#original-f0067-account).

Material covered by that review: [Exact material](Yin_C_F0099_v1.md), [Exact material](Yin_C_F0100_v1.md), [Exact material](../ledger/Yin_L_F0025_v1.md) (together retain the original whole-source scope).

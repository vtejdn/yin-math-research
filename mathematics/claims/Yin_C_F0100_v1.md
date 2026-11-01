---
author: Yin
---

# Two free projections with arbitrary traces satisfy the bounded division-closure equality

## Current assessment
[Selected decision](#decision-isolated-review-2026-10-22)

## 4. Positive result for two freely independent projections

<a id="statement"></a>
<a id="yin_c_f0100"></a>

The original shared [question and closure convention](../ledger/Yin_L_F0025_v1.md#1-question-source-reuse-and-accepted-inputs) fixes A=C<p,q>, M=W*(p,q) and the equality of the affiliated bounded intersection with scalar division closure inside M.
The original [generic matrix setting and rational-expression induction](../ledger/Yin_L_F0025_v1.md#2-algebra-and-the-generic-matrix-model) fixes T=1-p-q+pq+qp, b=pq(1-p), s(t)=sqrt(t(1-t)), the four character projections and the matrix normal form cited by the original equation numbers below.
Those are unchanged parts of R_F0067's original combined-file input, made explicit here without adding a hypothesis or enlarging the theorem.

**Candidate statement.**
If \(p,q\) are freely independent projections with arbitrary traces in a faithful tracial W*-probability space and \(\mathcal M=W^*(p,q)\), then (1) holds.
The proof below is complete as a draft and awaits independent review.
It includes nonuniform and irrational Bernoulli trace parameters.

### 4.1 What freeness supplies at the endpoints

Set \(\alpha=\tau(p)\), \(\beta=\tau(q)\).
If either trace is 0 or 1, faithfulness makes the corresponding projection scalar; \(A\) is then finite-dimensional and the conclusion is immediate, also covered by Yin_C_F0087.
Assume \(0<\alpha,\beta<1\).

The checked free-product law in Collins–Kemp equations (1.5)–(1.7) gives generic support
\[
 K=[r_-,r_+],\qquad
 r_\pm=\alpha+\beta-2\alpha\beta
       \pm2\sqrt{\alpha\beta(1-\alpha)(1-\beta)}.
 \tag{15}
\]
The generic parameter measure is diffuse and has positive density in the interior of this nondegenerate interval.
Applying the same source's mass-at-1 formula to the four pairs of projections and their complements gives
\[
 \tau(e_{10})=(\alpha-\beta)_+,\quad
 \tau(e_{01})=(\beta-\alpha)_+,\quad
 \tau(e_{11})=(\alpha+\beta-1)_+,\quad
 \tau(e_{00})=(1-\alpha-\beta)_+.
 \tag{16}
\]
These substitutions preserve freeness.
Since \(r_-=(\sqrt{\alpha(1-\beta)}-\sqrt{\beta(1-\alpha)})^2\), \(r_-=0\) exactly when \(\alpha=\beta\).
Likewise \(r_+=1\) exactly when \(\alpha+\beta=1\).
It follows that at either endpoint there is at most one nonzero character projection, and any such character is separated from the generic support by a positive gap.
In the endpoint-touching cases the corresponding characters vanish.

### 4.2 Constructing the endpoint projections with bounded inverses

Suppose first that \(e_{10}\ne0\).
Equation (16) gives \(e_{01}=0\), and (15) gives \(r_->0\).
Use the element \(x\) in [C_F0099, Section 3.1, equation (10)](Yin_C_F0099_v1.md#31-an-explicit-finite-tracial-model).
On the generic part its determinant \(t(1+t)\) is bounded away from zero on \(K\), while its entries are continuous.
On all present character blocks its values are nonzero:
\[
 x|_{e_{10}}=1,\qquad x|_{e_{11}}=1,\qquad x|_{e_{00}}=2.
\]
The only character with value zero would be \(e_{01}\), which is absent.
Hence \(x^{-1}\in\mathcal M\).
Also \((1+T)^{-1}\in\mathcal M\).
Computing as in [C_F0099, Sections 3.1–3.2, equations (11)–(14)](Yin_C_F0099_v1.md#31-an-explicit-finite-tracial-model) now proves
\[
 e_{10}=2(1+T)^{-1}p-px^{-1}p
   \in\operatorname{Div}_{\mathcal M}A.
 \tag{17}
\]
This is a finite scalar rational expression in the original \(p,q\).
A spectral gap alone was not used as a substitute for such an expression.

For the other nonzero characters, apply (17) to the following pairs.
Each pair generates exactly the same algebra \(A\), and its hypotheses follow from (15)–(16).

| Desired character | Pair substituted into (17) | Central parameter |
| --- | --- | --- |
| \(e_{01}\) | \((q,p)\) | \(T\) |
| \(e_{11}\) | \((p,1-q)\) | \(1-T\) |
| \(e_{00}\) | \((1-p,q)\) | \(1-T\) |

Zero characters need no expression.
Therefore all four \(e_{ij}\), and \(e=1-\sum e_{ij}\), belong to \(\operatorname{Div}_{\mathcal M}A\).

### 4.3 Boundedness removes every pole in the generic coefficients

Let \(f\in\operatorname{Div}_{L^0(\mathcal M)}A\cap\mathcal M\).
Its generic component has form (6).
Each matrix entry is essentially bounded.
A rational function with a pole at a point of \(K\) is unbounded on every punctured support neighborhood of that point.
The positive density in the interior of \(K\) converts that into essential unboundedness.
Thus the reduced rational functions \(a,h\) have no poles on \(K\).

For \(c,d\), the weight \(s(t)\) is nonzero away from 0 and 1, so the same conclusion holds at all other support points.
At 0 a pole of an ordinary rational function has an integer order \(k\ge1\); its weighted entry behaves as a nonzero constant times \(t^{1/2-k}\), which diverges.
At 1 the corresponding behavior is \((1-t)^{1/2-k}\).
Hence boundedness of the off-diagonal entries also excludes poles of \(c,d\) at an endpoint touched by \(K\).

Consequently there is a polynomial \(Q\in\mathbb C[t]\) with no zeros on \(K\), and polynomials \(A_0,C_0,D_0,H_0\), such that
\[
 a=A_0/Q,\quad c=C_0/Q,\quad d=D_0/Q,\quad h=H_0/Q.
 \tag{18}
\]
Choose a common product of the denominators after cancellation.
This is the one-variable pole-exclusion mechanism of Yin_C_F0087/Yin_C_F0090 with the additional half-order endpoint check; an arbitrary matrix coefficient estimate would not suffice.

### 4.4 Returning to the original bounded scalar closure

Let
\[
 n=e\bigl(A_0(T)p+H_0(T)(1-p)+C_0(T)b+D_0(T)b^*\bigr),
 \qquad d_0=eQ(T)+(1-e).
 \tag{19}
\]
Both belong to \(\operatorname{Div}_{\mathcal M}A\), because \(e\) was explicitly reconstructed there.
The operator \(d_0\) has the nonvanishing scalar value \(Q(t)\) on the generic part and value 1 on every character.
Compactness of \(K\) gives a bounded inverse \(d_0^{-1}\in\mathcal M\).
Equations (6) and (18) yield
\[
 ef=nd_0^{-1}\in\operatorname{Div}_{\mathcal M}A.
 \tag{20}
\]
This patches possible zeros of \(Q\) on character points outside \(K\); it does not assume that \(Q(T)\) is globally invertible.

Finally each character component of \(f\) equals \(\lambda_{ij}e_{ij}\) for a complex number \(\lambda_{ij}\).
Summing (20) and these finitely many scalar components proves the nontrivial inclusion in (1).
The reverse inclusion follows because every bounded inverse remains an inverse in \(L^0(\mathcal M)\).
This completes the candidate proof.


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
| argument | [Exact material](#42-constructing-the-endpoint-projections-with-bounded-inverses) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0107_v1.md#6-pole-exclusion-and-final-reconstruction) | Complete two-free-projection proof for all traces, including central character extraction, all endpoint cases, rational induction, pole exclusion and original scalar reconstruction. Actual original finding with unknown initial-context relationship; original date and accepted inputs preserved. |


### Decision isolated-review-2026-10-22

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:40 |
| status | proved |
| reason | Adopt the new isolated complete finding on the unchanged fixed mathematics and its actual necessary interfaces. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#42-constructing-the-endpoint-projections-with-bounded-inverses) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New isolated complete finding](../audits/reviews/Yin_R_F0107_v1.md#isolated-free-projection-equality) | Whole free-two-projection equality for all traces, full shared rational induction, every endpoint/character case, explicit bounded scalar extraction, half-order pole exclusion and original scalar reconstruction. |

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
| argument | [Exact material](#42-constructing-the-endpoint-projections-with-bounded-inverses) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0107_v1.md#original-f0067-account) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0107_v1.md#original-f0067-account).

Material covered by that review: [Exact material](Yin_C_F0099_v1.md), [Exact material](Yin_C_F0100_v1.md), [Exact material](../ledger/Yin_L_F0025_v1.md) (together retain the original whole-source scope).

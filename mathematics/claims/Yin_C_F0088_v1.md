---
author: Yin
---

# Cusp obstruction even inside the generated C*-algebra

## Current assessment
[Selected decision](#decision-isolated-whole-review-2026-10-22)

## Yin_C_F0088: A Cusp Coordinate Obstruction Inside the Generated C*-Algebra

<a id="yin_c_f0088"></a>

Provenance: project operator-algebra specialization of the classical cusp normalization mechanism; no novelty claim.
Candidate proof version: **Yin_C_F0088-P1** below.
Initial mathematical status: proof draft; review status: awaiting independent review.
The source comparison and its verification limit are recorded after the proof; no unverified external theorem is a proof premise.

### Statement

Let \(\mathcal M=L^\infty([0,1],dt)\), let \(a(t)=t\), and set \(X=(a^2,a^3)\).
Then
\[
W^*(X)=W^*(a)=\mathcal M,
\qquad C^*(X)=C^*(a)=C([0,1]),
\tag{11}
\]
and
\[
\operatorname{Div}_{L^0(\mathcal M)}\mathcal A_X
=\operatorname{Div}_{L^0(\mathcal M)}\mathbb C[a].
\tag{12}
\]
Nevertheless
\[
a\in\operatorname{Div}_{L^0(\mathcal M)}\mathcal A_X\cap C^*(X),
\qquad
a\notin\operatorname{Div}_{\mathcal M}\mathcal A_X.
\tag{13}
\]
Thus (B) can fail even when the particular bounded rational element lies in the generated \(C^*\)-algebra.
This tuple is commuting and algebraically dependent.
It is **not** an example under the full free-coordinate dual hypotheses; Yin_C_F0012 retains that distinct role.

### Yin_C_F0088-P1: proof

The continuous functional calculus gives \(a=\sqrt{a^2}\), proving the \(C^*\) equality in (11), and hence the \(W^*\) equality.
The bounded multiplication operator \(a^2\) has zero kernel since \(t^2>0\) almost everywhere.
Its affiliated inverse is multiplication by \(t^{-2}\), so
\[
a=a^3(a^2)^{-1}
\tag{14}
\]
in \(L^0(\mathcal M)\).
Minimality of the two affiliated division closures now gives (12).

The evaluated polynomial algebra \(\mathcal A_X\) is identified with \(\mathbb C[t^2,t^3]\), whose polynomials have no degree-one coefficient.
By the [elementary commutative fraction argument in Yin_C_F0087-P1, (5)](Yin_C_F0087_v1.md#yin_c_f0087-p1-proof), now with ambient algebra \(\mathcal M\), every element of \(\operatorname{Div}_{\mathcal M}\mathcal A_X\) has the form
\[
\frac{p(t)}{q(t)},\qquad p,q\in\mathbb C[t^2,t^3],
\qquad q^{-1}\in L^\infty([0,1]).
\tag{15}
\]
Continuity of \(q\) and full support of Lebesgue measure imply that \(q\) has no zero on \([0,1]\).
Indeed, any zero would give sets of positive measure where \(|q|\) is arbitrarily small.
In particular, \(q(0)\ne0\).

If (15) equalled \(a(t)=t\) almost everywhere, the polynomial identity \(p(t)=tq(t)\) would hold on all of \([0,1]\), and hence as a polynomial identity.
Its left side has zero coefficient at degree one, whereas its right side has degree-one coefficient \(q(0)\ne0\).
This contradiction proves (13).
Equivalently, all fractions in (15) have derivative zero at the origin, while \(a'(0)=1\).

Finally, the relation \(X_1X_2=X_2X_1\) excludes simultaneous bounded dual relations \([D_i,X_j]=\delta_{ij}P_\Omega\).
Applying \([D_1,\cdot]\) to that relation would give \([P_\Omega,X_2]=0\); evaluation at \(\Omega\) would force \(a^3\) to be scalar, a contradiction.
No maximal-Delta or free-field assertion is used here.

### Source attribution and self-check boundary

The underlying coordinate ring \(\mathbb C[t^2,t^3]\subset\mathbb C[t]\) is the standard cuspidal example, not a new algebraic construction.
A primary-source search found David Eisenbud, *Commutative Algebra with a View Toward Algebraic Geometry*, Section 4.3, **Normalization in the Analytic Case**, describing \(\mathbb C[x,y]/(y^2-x^3)\) and the bounded but nonregular function \(y/x\).
The [academic-hosted source](https://www.math.ens.psl.eu/~benoist/refs/Eisenbud.pdf) was available in the search engine's parsed Section 4.3 excerpt; opening the entire PDF exceeded the web tool's content limit.
That source is a checked identification of the classical mechanism at excerpt scope, not an imported normalization theorem or a complete source audit.
The complete concrete operator/fraction argument above supplies the conclusion without that theorem.

The author checked full support at the endpoint, the precise bounded inverse requirement, the difference between a.e. and polynomial equality, both generated-algebra equalities, and the absence of a full two-coordinate dual system.
These are author checks, not independent review or formal verification.


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
| argument | [Exact material](#yin_c_f0088-p1-proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0088_v1.md#yin_c_f0088-the-endpoint-cusp-obstruction) | Actual original complete C_F0088 finding at its disclosed accepted-input scope and unknown initial-context relationship; historical source precision and limits remain at this retained finding. |


### Decision isolated-whole-review-2026-10-22

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:10 |
| status | proved |
| reason | Adopt the actual new isolated whole-proof finding for the unchanged fixed statement and argument; retain prior assessments at their real dates and original relationships. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#yin_c_f0088-p1-proof) | Original explicitly selected complete argument at its unchanged mathematical scope. |
| review | [New whole-proof review](../audits/reviews/Yin_R_F0088_v1.md#fresh-c88-whole) | New isolated whole-proof inspection at the exact fixed input and accepted-source boundaries; original historical findings remain separately unknown. |

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
| argument | [Exact material](#yin_c_f0088-p1-proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Same original finding](../audits/reviews/Yin_R_F0088_v1.md#yin_c_f0088-the-endpoint-cusp-obstruction) | Original selected finding; its actual scope and limits remain in the cited review. |

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

Review: [Original C87 finding](../audits/reviews/Yin_R_F0088_v1.md#yin_c_f0087-fraction-collapse-and-principal-ideal-cancellation), [Original C88 finding](../audits/reviews/Yin_R_F0088_v1.md#yin_c_f0088-the-endpoint-cusp-obstruction), [Original C89 finding](../audits/reviews/Yin_R_F0089_v1.md#historical-finite-index-transfer), [Original coordinate observation](../audits/reviews/Yin_R_F0090_v1.md#original-coordinate-paragraph).

Material covered by that review: [Exact material](Yin_C_F0087_v1.md), [Exact material](Yin_C_F0088_v1.md), [Exact material](Yin_C_F0089_v1.md), [Exact material](../ledger/Yin_L_F0020_v1.md) (together retain the original whole-source scope).

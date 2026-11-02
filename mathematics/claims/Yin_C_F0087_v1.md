---
author: Yin
---

# Principal-ideal bounded descent; every single bounded operator

## Current assessment
[Selected decision](#decision-isolated-whole-review-2026-10-22)

## Yin_C_F0087: Principal Numerator-Denominator Ideals Give Descent

<a id="yin_c_f0087"></a>

Provenance: project deduction using the [checked classical principal-ideal input](../audits/literature/Hun74/Yin_U006.md#exact-retained-statement-and-proof-inspection-depth).
Candidate proof version: **Yin_C_F0087-P1** below.
Initial mathematical status: proof draft; review status: awaiting independent review.
Definition uses: scalar division closure in the [rationality conventions](../ledger/Yin_L_F0013_v1.md#rationality-conventions), and principal ideals in [Hun74 III.3 at the recorded source scope](../audits/literature/Hun74/Yin_U006.md#exact-retained-statement-and-proof-inspection-depth).

### Statement

Let \(A\subseteq B\subseteq S\) be associative unital complex algebras with common identity.
Assume that \(A\) is commutative and that
\[
pA+qA\text{ is principal whenever }p,q\in A
\text{ and }q\text{ is invertible in }S.
\tag{1}
\]
No commutativity of \(B\) or \(S\), domain assumption on \(A\), topology, or direct-finiteness assumption is required.
Then
\[
\operatorname{Div}_S A\cap B=\operatorname{Div}_B A.
\tag{2}
\]

In particular, (1) holds if every finitely generated ideal of \(A\) is principal, including when \(A\) is a commutative principal ideal ring.
For **every** element \(a\) of **every** unital complex algebra \(B\subseteq S\),
\[
\operatorname{Div}_S\mathbb C[a]\cap B
=\operatorname{Div}_B\mathbb C[a].
\tag{3}
\]
Thus, for an arbitrary bounded operator \(a\in\mathcal M\),
\[
\boxed{\operatorname{Div}_{L^0(\mathcal M)}\mathbb C[a]\cap\mathcal M
=\operatorname{Div}_{\mathcal M}\mathbb C[a].}
\tag{4}
\]
Equation (4) needs no normality, dual system, injectivity, tracial law regularity, or positive-power-subspace assumption.
It includes a single circular or R-diagonal operator, with the unstarred algebra \(\mathbb C[a]\).
It does not identify that algebra with \(\mathbb C\langle a,a^*\rangle\).

### Yin_C_F0087-P1: proof

Let \(\Sigma=A\cap S^\times\).
Commutativity of \(A\) implies that its elements and the inverses of elements of \(\Sigma\) commute inside \(S\).
The set
\[
Q=\{p q^{-1}:p\in A,\ q\in\Sigma\}
\tag{5}
\]
is a unital subalgebra of \(S\): sums and products have the usual common-denominator formulas.
If \(x=pq^{-1}\) is a unit of \(S\), then \(p=xq\) is a unit of \(S\), and \(x^{-1}=qp^{-1}\in Q\).
Therefore \(Q\) is division closed in \(S\); conversely, every element in (5) is an allowed division expression.
Hence \(Q=\operatorname{Div}_S A\).
This proof does not require \(A\) to be a domain or \(S\) to be commutative.

Take \(f=pq^{-1}\in Q\cap B\).
By (1), choose \(d\in A\) with \(pA+qA=dA\).
There are \(u,v,\alpha,\beta\in A\) such that
\[
p=du,\qquad q=dv,\qquad d=\alpha p+\beta q.
\tag{6}
\]
Since \(d\) and \(v\) commute and \(dv=q\) is a unit in \(S\), **both factors are units in \(S\)**.
Explicitly, \(v q^{-1}\) is a two-sided inverse of \(d\), and \(q^{-1}d\) is a two-sided inverse of \(v\).
These identities use the commutation of \(q^{-1}\) with \(d,v\); invertibility of a noncommuting product would not by itself suffice in a general ring.

Cancel the unit \(d\) in (6).
We obtain
\[
\alpha u+\beta v=1,\qquad f=uv^{-1}.
\tag{7}
\]
Multiplying the first identity by \(v^{-1}\) gives
\[
v^{-1}=\alpha f+\beta\in B.
\tag{8}
\]
Thus \(v\in A\) has its inverse in \(B\), and \(f=uv^{-1}\in\operatorname{Div}_B A\).
The opposite inclusion in (2) follows because every inverse that exists in \(B\) remains an inverse in \(S\).

For (3), the evaluation homomorphism \(\mathbb C[z]\to\mathbb C[a]\) is onto.
The inverse image of an ideal of \(\mathbb C[a]\) is an ideal of the PID \(\mathbb C[z]\), so its generator maps to a generator of the original ideal.
Consequently \(\mathbb C[a]\) is a principal ideal ring even if evaluation has a nonzero kernel.
Apply (2), then take \(B=\mathcal M\), \(S=L^0(\mathcal M)\) for (4).

A concrete single-operator implementation is to reduce \(f=p(a)q(a)^{-1}\) by the polynomial gcd and choose Bezout coefficients \(\alpha p+\beta q=1\).
Equation (8) becomes
\[
q(a)^{-1}=\alpha(a)f+\beta(a).
\tag{9}
\]
The denominator is first required to be invertible in \(S\), not merely a nonzero polynomial.
If gcd cancellation removes a factor, the commuting-unit-factor calculation above proves that the reduced denominator stays invertible.
In the finite von Neumann setting this is precisely the regular-denominator condition.
Nonzero polynomials can evaluate to zero divisors, so the proof does not identify the affiliated closure with the entire abstract field \(\mathbb C(z)\).

### Scope and checks

The proof includes scalar \(a\), nilpotent matrices, nontrivial idempotents, and operators with a kernel.
For example, when \(a^2=a\), the polynomial \(z\) is not an eligible denominator if \(a\ne1\); the theorem does not invert it.
When \(f=0\), choose \(p=0,q=1\), and the conclusion is immediate.
The algebraic proof also permits \(B\) to be noncommutative.

For one R-diagonal element this settles property (B) outright.
Yin_C_F0021 still has separate content: it starts only with an \(L^2\) vector in the positive-power subspace and proves boundedness as well as norm approximation.
Yin_C_F0087 begins with an already bounded element.
In particular, Yin_C_F0019's unbounded \(L^2\) inverse is consistent with Yin_C_F0087.


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
| argument | [Exact material](#yin_c_f0087-p1-proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0088_v1.md#yin_c_f0087-fraction-collapse-and-principal-ideal-cancellation) | Actual original complete C_F0087 finding at its disclosed accepted-input scope and unknown initial-context relationship; historical source precision and limits remain at this retained finding. |


### Decision isolated-whole-review-2026-10-22

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:10 |
| status | proved |
| reason | Adopt the actual new isolated whole-proof finding for the unchanged fixed statement and argument; retain prior assessments at their real dates and original relationships. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#yin_c_f0087-p1-proof) | Original explicitly selected complete argument at its unchanged mathematical scope. |
| review | [New whole-proof review](../audits/reviews/Yin_R_F0088_v1.md#fresh-c87-whole) | New isolated whole-proof inspection at the exact fixed input and accepted-source boundaries; original historical findings remain separately unknown. |

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
| argument | [Exact material](#yin_c_f0087-p1-proof) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Same original finding](../audits/reviews/Yin_R_F0088_v1.md#yin_c_f0087-fraction-collapse-and-principal-ideal-cancellation) | Original selected finding; its actual scope and limits remain in the cited review. |

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

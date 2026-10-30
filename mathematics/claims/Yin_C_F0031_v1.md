---
author: Yin
---

# Closable finite-rank extension and regular-factor cancellation

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Closable Finite-Range Operators and Regular-Factor Cancellation

<a id="statement"></a>

<a id="yin_c_f0031"></a>
## Yin_C_F0031: Finite-Rank Closure and Dense-Restriction Cancellation

- Role: lemma.
- Date: 2026-09-10.
- Proof development: another AI agent.
- Origin: agent-proposed shared-lemma extraction, explicitly authorized by the user as part of the five-module batch.
- Authorization: [approved extraction batch](../ledger/Yin_L_F0014_v1.md#authorization).
- Proof version: [yin_c_f0031-p1](#yin_c_f0031-p1), candidate complete proof draft.
- Review: author self-check completed; separate independent review pending.
  The [selected assessment](#decision-candidate-0002) records the mathematical and review assessments.

## 1. Statement and Conventions

Let \(H\) be a complex Hilbert space with inner product linear in its second variable.
Let \(\mathcal E\subseteq H\) be a dense complex-linear subspace, and let \(T:\mathcal E\to H\) be complex-linear and closable.
The rank of a map on a specified domain means the complex dimension of its image on that domain.
In particular, saying that \(T\) has finite rank initially asserts only that \(T(\mathcal E)\) is finite dimensional.

**Finite-rank closure.**
If \(\dim T(\mathcal E)=r<\infty\), then the Hilbert-space closure \(\overline T\) is an everywhere-defined bounded operator with

\[
\operatorname{Ran}\overline T=T(\mathcal E),
\qquad \operatorname{rank}\overline T=r.
\tag{1}
\]

It is the unique bounded extension of \(T\) to \(H\).

**Dense-restriction cancellation.**
If \(\mathcal F\subseteq\mathcal E\) is a complex-linear subspace dense in \(H\) and \(\dim T(\mathcal F)=r<\infty\), then

\[
\overline T=\overline{T|_{\mathcal F}}\in B(H),
\qquad
T(\mathcal F)=T(\mathcal E)=\operatorname{Ran}\overline T,
\qquad \operatorname{rank}\overline T=r.
\tag{2}
\]

No graph-density assumption on \(\mathcal F\) is part of the premise.

**Regular-factor cancellation.**
Let \(Y,Y'\in B(H)\) satisfy

\[
Y\text{ is injective},\qquad
\overline{Y'H}=H,\qquad
Y'\mathcal E\subseteq\mathcal E.
\tag{3}
\]

Define the densely defined operator

\[
S:\mathcal E\to H,\qquad Sz=Y\,T(Y'z).
\tag{4}
\]

Then \(S\) has finite rank on \(\mathcal E\) if and only if \(T\) does.
When either finite-rank condition holds, both closures are bounded finite-rank operators and

\[
\overline S=Y\,\overline T\,Y',
\qquad
\operatorname{rank}S
=\operatorname{rank}\overline S
=\operatorname{rank}T
=\operatorname{rank}\overline T.
\tag{5}
\]

The hypotheses only require injectivity of the left factor and dense range of the right factor.
Bounded inverses, closed ranges, or quantitative lower bounds for these factors are not assumed.
The explicit inclusion in (3) makes every input in (4) an element of the domain of \(T\).

<a id="yin_c_f0031-p1"></a>
## 2. Proof Version yin_c_f0031-p1

Disposition: candidate complete proof, awaiting separate review.
This proof uses the Hilbert-space and finite-dimensional facts listed in Section 5.

### 2.1. A closable finite-range map is bounded on its domain

Put \(W=T(\mathcal E)\), with \(\dim W=r<\infty\).
The case \(r=0\) gives the zero operator on the dense domain, whose closure is the zero operator on \(H\).
Suppose \(r>0\), and choose an orthonormal basis \(w_1,\ldots,w_r\) of \(W\).

Closability of \(T\) implies that \(\operatorname{Dom}T^*\) is dense in \(H\).
Let \(P_W\) be the orthogonal projection onto \(W\).
The space \(P_W(\operatorname{Dom}T^*)\) is a linear subspace of the finite-dimensional space \(W\).
It is dense in \(W\): approximate any \(w\in W\) by vectors in \(\operatorname{Dom}T^*\) and apply the continuous projection.
Every linear subspace of a finite-dimensional space is closed, so

\[
P_W(\operatorname{Dom}T^*)=W.
\tag{6}
\]

For each \(j\), choose \(\eta_j\in\operatorname{Dom}T^*\) with \(P_W\eta_j=w_j\).
Since \(Tz\in W\), the adjoint convention gives

\[
\langle w_j,Tz\rangle
=\langle \eta_j,Tz\rangle
=\langle T^*\eta_j,z\rangle
\qquad(z\in\mathcal E).
\tag{7}
\]

Define on all of \(H\)

\[
Bz=\sum_{j=1}^r w_j\langle T^*\eta_j,z\rangle.
\tag{8}
\]

This operator is bounded, has range in \(W\), and obeys the explicit estimate

\[
\|Bz\|^2
\leq
\left(\sum_{j=1}^r\|T^*\eta_j\|^2\right)\|z\|^2.
\tag{9}
\]

Equation (7) shows that \(Bz=Tz\) for \(z\in\mathcal E\).
The graph of \(T\) is therefore contained in the closed graph of \(B\).
Conversely, for any \(z\in H\), choose \(z_n\in\mathcal E\) with \(z_n\to z\).
Then \(Tz_n=Bz_n\to Bz\), so \((z,Bz)\) lies in the closure of the graph of \(T\).
Thus \(\overline T=B\).

The inclusion \(B(H)\subseteq W\) and the equality \(B(\mathcal E)=T(\mathcal E)=W\) prove the range and rank assertions in (1).
Any two bounded extensions coincide on the dense subspace \(\mathcal E\), hence on all of \(H\).
This proves uniqueness.

### 2.2. Cancellation of a Hilbert-dense restriction

The restriction \(T|_{\mathcal F}\) is densely defined and closable.
Indeed its graph is contained in the graph of \(T\), and its graph closure is contained in the graph of the operator \(\overline T\).
Apply Section 2.1 to this restriction.
Its closure is a bounded operator \(B\) defined on all of \(H\), with range \(T(\mathcal F)\) and rank \(r\).

The graph of \(B\) is contained in the graph of \(\overline T\).
For every \(z\in H\), that inclusion supplies the pair \((z,Bz)\) in the latter graph.
Since \(\overline T\) is single-valued, it has no different value at any \(z\), and its domain is already all of \(H\).
Consequently \(\overline T=B\).
The inclusions

\[
T(\mathcal F)\subseteq T(\mathcal E)
\subseteq B(H)=T(\mathcal F)
\tag{10}
\]

prove (2).
Graph density of \(\mathcal F\) is a conclusion of this argument, not an assumption or an inference from Hilbert density alone.

### 2.3. Cancellation of bounded outer factors

First, \(Y'\mathcal E\) is dense in \(H\).
For any \(z\in H\), approximating \(z\) by vectors of \(\mathcal E\) shows that \(Y'z\) belongs to the closure of \(Y'\mathcal E\).
The dense-range hypothesis on \(Y'\) then gives that this closure is all of \(H\).
The domain inclusion in (3) makes \(Y'\mathcal E\) an eligible subspace \(\mathcal F\) in Section 2.2.

Suppose \(S(\mathcal E)\) has dimension \(r<\infty\).
Injectivity of \(Y\) gives a linear isomorphism from \(T(Y'\mathcal E)\) onto \(S(\mathcal E)\).
Therefore

\[
\dim T(Y'\mathcal E)=r.
\tag{11}
\]

Section 2.2 now makes \(\overline T\) bounded on all of \(H\), with rank \(r\) and range \(T(Y'\mathcal E)\).
Equation (4) is the restriction of the bounded operator \(Y\overline T Y'\) to the dense domain \(\mathcal E\).
The graph approximation used in Section 2.1 therefore gives

\[
\overline S=Y\overline T Y'.
\tag{12}
\]

This also proves closability of \(S\) in the finite-rank situation; it was not imposed as an extra premise.

Conversely, suppose \(T\) has finite rank.
Section 2.1 gives its bounded closure \(B=\overline T\).
Because \(Y'\mathcal E\) is dense, \(B(Y'\mathcal E)\) is dense in \(B(H)\).
It is a linear subspace of the finite-dimensional space \(B(H)\), so it equals \(B(H)\).
Thus

\[
S(\mathcal E)=YB(Y'\mathcal E)=YB(H).
\tag{13}
\]

Injectivity of \(Y\) preserves its dimension, giving \(\operatorname{rank}S=\operatorname{rank}B\).
The same argument with the dense domain \(\mathcal E\) shows that the closure in (12) has this identical finite rank.
Together with (1), these observations prove every equality in (5).

## 3. Left-Module and Defect Applications

For a finite von Neumann algebra acting by left multiplication on \(H=L^2(M,\tau)\), let \(\mathcal E\subseteq H\) be a dense left \(M\)-module.
If \(y,y'\in M\) are regular multipliers, their left actions are injective and have dense range.
Apply Section 1 with \(Y=\lambda(y)\) and \(Y'=\lambda(y')\).
Left-module invariance supplies \(y'\mathcal E\subseteq\mathcal E\).
Hence a closable defect \(T:\mathcal E\to H\) has finite rank if and only if

\[
z\longmapsto yT(y'z)
\tag{14}
\]

does, with identical finite numerical ranks and the bounded closures in (5).
Only the displayed operator properties of regular multipliers are used here; the construction of affiliated fractions is a separate input for consumers.
There is no right-\(M\)-module assumption.

In particular, suppose two closable defects \(T_1,T_2:\mathcal E\to H\) satisfy

\[
yT_2(y'z)=xT_1(x'z)
\qquad(z\in\mathcal E),
\tag{15}
\]

where \(x,y,x',y'\in M\) are regular.
If one defect has finite rank, its corresponding bounded outer product does too.
Cancellation makes the other defect bounded finite rank.
Applying (5) to both sides of (15) gives equality of the two finite numerical ranks.
This is the intended interface for comparing common-denominator defects.
The identity (15) itself must be proved by the consuming argument.

## 4. Boundary Conditions

Zero rank is included throughout; no nonzero range vector or orthonormal basis is selected in that case.
The zero Hilbert space also satisfies the statements.
No separability assumption is needed.

Closability is essential: finite-dimensional range by itself does not bound an arbitrary linear map on a dense domain.
The density of the tested restriction and the factor conditions in (3) are used explicitly.
Without injectivity of the left factor it may erase a range; without dense range of the right factor it may fail to test a portion of the operator.
Without \(Y'\mathcal E\subseteq\mathcal E\), formula (4) is not an operator on the stated domain.

The lemma does not assert that every closable operator is bounded, that arbitrary Hilbert-dense subspaces are graph cores, or that multiplying an arbitrary closable operator by bounded factors always preserves closability.
It proves the closures and rank equalities only under its stated finite-rank conditions.

## 5. Dependencies, Provenance, and Proof-Version Use

**Actual proof dependencies of yin_c_f0031-p1.**
The proof uses the Hilbert adjoint criterion that a densely defined operator is closable if and only if its adjoint domain is dense, the defining adjoint pairing, elementary graph-closure properties, orthogonal projection onto a finite-dimensional subspace, and elementary finite-dimensional linear algebra.
It uses continuity of bounded Hilbert-space operators and closedness of their graphs.
No project claim or literature theorem about free probability, free fields, normal tuples, affiliated fractions, or dual systems is a premise of Sections 1–2.
The application in Section 3 checks the abstract operator and domain assumptions directly.

**Extraction provenance.**
The source is [Yin_C_F0029, Section 5](Yin_C_F0029_v1.md#yin_c_f0029), specifically the paragraphs “Finite-rank extension” and “Cancellation.”
The preceding defect-adjoint calculation there supplies closability in that original application; this extracted lemma instead states closability as a hypothesis.
The present version spells out the intermediate dense-restriction argument and the exact numerical-rank consequences.
This records the origin of the proof and is not a logical dependency on the conclusion of Yin_C_F0029.

**Intended consumers.**
The candidate fraction module Yin_C_F0034 may invoke (1) to bound a closable finite-rank defect and (3)–(5) or (15) to compare fraction choices.
A future lemma-based proof version of Yin_C_F0029 may replace its corresponding Section 5 argument with this interface.
These are intended proof-version relationships, not edits to the original proof or activation of new dependencies in its historical record.
Any consumer must verify its dense domain, closability, multiplier hypotheses, and input-domain inclusion before invoking the lemma.

**Version and review disposition.**
Version yin_c_f0031-p1 is the initial extracted proof written under the approved batch.
The original Yin_C_F0029 artifact and its prior review remain unchanged and continue to record their own complete proof.
No previous review is relabeled as a review of this extraction.
Separate review of this exact module and of any new consuming proof remains pending.
No numerical computation, proof-assistant verification, external human review, publication, or novelty assessment is claimed.


## Assessment history


### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

Recorded review label: independently reviewed.
Role designation: lemma.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0031-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0012_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:45 |
| status | proved |
| reason | Select the actual retained finding scopes and their known mathematical-development relationships, preserving status, authorized role, exact statement/proof/dependency selections and all historical decisions. No new mathematical review is asserted. |

Role designation: lemma.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#yin_c_f0031-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Retained finding](../audits/reviews/Yin_R_F0012_v1.md#finite-rank-lemma-finding) | Actual original complete or auxiliary scope stated by that finding; unchanged versions and original source-depth/nonconclusion boundaries. |

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
Role designation: lemma.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0012_v1.md).

Material covered by that review: [Exact material](Yin_C_F0031_v1.md).

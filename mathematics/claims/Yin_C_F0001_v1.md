---
author: Yin
---

# Normal-generator scalar rationality under bounded duals

## Current assessment
[Selected decision](#decision-isolated-main-review-adoption)

## Rationality under Bounded Dual Systems

<a id="statement"></a>

This module contains the user-approved conjecture.
The supporting [Yin_C_F0002 proof](Yin_C_F0002_v1.md#yin_c_f0002) establishes the derivative interface and the rational-to-finite-rank implication.
[Yin_C_F0012](Yin_C_F0012_v1.md#yin_c_f0012) refutes the converse with two selfadjoint generators; the original statement below is preserved unchanged.
The [Unt20 reading](../audits/literature/Unt20/Yin_U001_v1.md#unt20-u001) supplies the proposed reconstruction route [Yin_S_F0001](../strategies/Yin_S_F0001.md#s_f0001).

<a id="yin_c_f0001"></a>
## Yin_C_F0001: Rationality Criterion for Normal Generators

Goal: [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001).

Project origin: a user-proposed conjecture refined in discussion and approved on 2026-09-08; no established deduction or novelty claim was asserted at that checkpoint.

Current assessment: [selected assessment](#decision-isolated-main-review-adoption): **refuted**.
[Yin_C_F0012](Yin_C_F0012_v1.md#yin_c_f0012) supplies the counterexample to the bounded scalar converse, and the [original-contract contributor audit](../audits/reviews/Yin_R_F0054_v1.md#completion-finding-and-verification-boundaries) checks every original hypothesis.
Yin_C_F0002's forward implication remains valid.

### Statement and Scope

For every integer \(d\geq 1\), let \((M,\tau)\) be a finite von Neumann algebra with a faithful normal tracial state, normalized by \(\tau(1)=1\).
Let

\[
X=(X_1,\ldots,X_d)\in M^d,\qquad
X_jX_j^*=X_j^*X_j\quad(1\leq j\leq d),\qquad
M=W^*(X_1,\ldots,X_d).
\]

No mutual commutativity or free independence of the generators is assumed.

Put \(H=L^2(M,\tau)\), \(\Omega=\widehat{1}\), and let \(P_\Omega\) be the orthogonal projection of H onto \(\mathbb C\Omega\).
Represent M faithfully on H by left multiplication:

\[
\lambda(a)\widehat b=\widehat{ab}\qquad(a,b\in M).
\]

Suppose there exists a tuple \(D=(D_1,\ldots,D_d)\in B(H)^d\) satisfying

\[
[D_i,\lambda(X_j)]=\delta_{ij}P_\Omega
\qquad(1\leq i,j\leq d),\qquad [S,T]=ST-TS.
\]

Such a tuple is called a **bounded dual system** here.
The dual operators need not be selfadjoint or normal, need not lie in \(\lambda(M)\), and are not required to satisfy \(D_i\Omega=0\).

Define the unital algebra and its scalar division closure by

\[
A_X=\mathbb C\langle X_1,\ldots,X_d\rangle,
\qquad \mathcal R_X=\operatorname{Div}_M(A_X).
\]

Here A_X contains polynomials in the listed generators only: their adjoints are not automatically adjoined.
The algebra \(\operatorname{Div}_M(A_X)\) is the smallest unital subalgebra of M containing A_X and containing \(a^{-1}\) whenever it contains a and a is invertible in M.
Equivalently, its elements are obtained by finitely many algebraic operations and inversions, with every inverted element invertible in M and every intermediate expression in M.
No topological closure is taken.
Matrix rational closure and division closure in the affiliated-operator algebra are not substituted for this definition.

**Conjecture.** For every setting above, every bounded dual system D satisfying the displayed relations, and every \(f\in M\),

\[
\boxed{
f\in\mathcal R_X
\quad\Longleftrightarrow\quad
\operatorname{rank}[D_i,\lambda(f)]<\infty
\ \text{for all }1\leq i\leq d.
}
\]

Rank means \(\dim_{\mathbb C}\operatorname{Ran}[D_i,\lambda(f)]\), the ordinary Hilbert-space operator rank.
No common numerical bound on these finite ranks is prescribed.
The element f need not be selfadjoint or normal.
All operators in the commutators are bounded, so the commutators are defined on all of H.

### Dependencies and Reference Context

[Yin_C_F0002](Yin_C_F0002_v1.md#yin_c_f0002) is an audited partial input: it realizes the derivatives by dual commutators and proves that every bounded scalar rational expression has finite-rank commutators.
The reverse implication is false by Yin_C_F0012.
Other [related source audits](../tasks/Yin_T_F0001_v1.md#related-records) remain contextual until their exact applicability is recorded.

### Argument or Exact Gap

Yin_C_F0002 proves the forward implication by the polynomial identity and the bounded inverse rule.
Yin_C_F0012 settles the alternative in [Yin_T_F0001's completion criteria](../tasks/Yin_T_F0001_v1.md#completion-criteria) by refutation: for h with law 4t³ dt and a free standard semicircular b, the tuple (h,hbh) generates M and has explicitly bounded duals.
The witness b has commutator ranks (2,1), but distance(b,C*(h,hbh))>=1.
Since the bounded scalar division closure lies in that C*-algebra, b is outside R_X.
This is exclusion of every admissible scalar expression, not only an unbounded chosen pencil.

### Checks and Supporting Evidence

Initial setup fixed notation and scope without new mathematical evidence.
The subsequent [Yin_C_F0002 finding](../audits/reviews/Yin_R_F0001_v1.md#complete-derivative-finding) verifies the derivative interface and forward direction at its recorded contributor self-review scope.
Its Haar example concerns two different derivative domains; it is not a counterexample to this conjecture.
No computation, formal verification, or novelty assessment is claimed.

### Review and Corrections

- 2026-09-08: initial registration of the approved normal-generator conjecture as Yin_C_F0001.
  Mathematical review remains unperformed; a check of the goal documentation is not a proof review.
- 2026-09-08, subsequent reading: Unt20's proposed reconstruction paths were mapped at the user's request.
  The source's incomplete L2/derivation setting is not substituted for this statement; Yin_C_F0001 and its assessment are unchanged.
- 2026-09-08, subsequent formula audit: Yin_C_F0002 establishes the precise dual-system derivative correspondence, bounded rational rule, finite-factor equivalence, and domain boundary.
  The mathematical statement of Yin_C_F0001 is unchanged and remains open.
- 2026-09-08, proposed modification assessed: [Yin_C_F0003](Yin_C_F0003_v1.md#yin_c_f0003) tests replacing the polynomial algebra by C<X,X*> while retaining all hypotheses.
  A checked disk-Cauchy counterexample refutes that variant's forward implication.
  It is not adopted; Yin_C_F0001's exact statement and open status are unchanged.
  The Haar derivative-domain example does not distinguish the two division closures, since U*=U^{-1} is already in the original one.

- 2026-09-08, authorized route exploration: [Yin_C_F0004](Yin_C_F0004_v1.md#yin_c_f0004) proves the one-generator case and coordinate-subalgebra corollary; [Yin_C_F0005](Yin_C_F0005_v1.md#yin_c_f0005) proves the general finite-rank-to-affiliated-field implication and scalar common kernel; [Yin_C_F0006](Yin_C_F0006_v1.md#yin_c_f0006) gives exact transfer families.
  The bounded scalar converse for all normal tuples remains open.
  The user next requested the full MSY23 source audit MSY23 free-field and Atiyah source audit to study its linearization techniques before pursuing bounded descent.

- 2026-09-09, autonomous exploration and subsequent careful re-audit: Yin_C_F0012 refutes this unchanged statement.
  Two saved complete-chain reviews, a fresh adversarial review of the analytic construction, and the original-contract completion audit verify the result.
  Earlier dated open assessments above describe their historical checkpoints; the current assessment is refuted.
  No replacement conjecture has been adopted.


## Assessment history


### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | refuted |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](Yin_C_F0012_v1.md#yin_c_f0012) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](Yin_C_F0002_v1.md#yin_c_f0002) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0054_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original review classification and limitations: independently reviewed counterexample

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision candidate-0004

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T02:52 |
| status | refuted |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](Yin_C_F0012_v1.md#yin_c_f0012) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](Yin_C_F0002_v1.md#yin_c_f0002) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0054_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-scopes

| Field | Value |
| --- | --- |
| date | 2026-10-20T21:28 |
| status | refuted |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Original statement](#statement) | The original normal-generator bounded-dual scalar rationality conjecture remains unchanged; the converse is false. |
| argument | [Complete counterexample](Yin_C_F0012_v1.md#1-an-explicit-tracial-fock-model) | The selfadjoint sandwich counterexample, all original hypotheses and scalar-division nonmembership; the valid forward direction is contextual, not a premise of this refutation. |
| review | [Finding](../audits/reviews/Yin_R_F0054_v1.md#completion-finding-and-verification-boundaries) | Actual 2026-09-09 contributor integration of the complete counterexample against the original conjecture; self-review, preserving every original inverse-domain and hypothesis boundary. |


### Decision isolated-main-review-adoption

The new main-example finding was formed from the fixed original mathematics before the old unknown-relationship findings were read as audit objects.
This decision adopts that actual new inspection without changing the original conjecture, proof or historical decisions.

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:41 |
| status | refuted |
| reason | The new isolated R_F0056 finding checks the complete original setting and main counterexample, including the exact bounded scalar division closure; no Section 8 strengthening or new Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Original statement](#statement) | The original universally quantified normal-generator bounded-dual scalar-rationality conjecture, with its exact bounded intermediate-expression closure, remains unchanged. |
| argument | [Complete main counterexample](Yin_C_F0012_v1.md#1-an-explicit-tracial-fock-model) | Complete unchanged Sections 1–7, standard model, bounded duals, actual finite ranks, generation and full scalar-closure nonmembership; the valid forward implication is contextual, not a premise. |
| review | [New isolated main finding](../audits/reviews/Yin_R_F0056_v1.md#main-counterexample-finding) | Actual new independent review of the complete original statement and main Sections 1–7; exact source depth, accidental fixed-dependency scope exposure and Section 8 exclusions remain in the finding. |

## Historical assessments


These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | refuted |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

Original review classification and limitations: independently reviewed counterexample

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0054_v1.md).

Material covered by that review: [Exact material](Yin_C_F0002_v1.md); [Exact material](Yin_C_F0001_v1.md); [Exact material](Yin_C_F0012_v1.md).

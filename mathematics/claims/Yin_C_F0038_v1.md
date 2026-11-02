---
author: Yin
---

# All-M selfadjoint duals yield L1 conjugates and dense adjoint modules

## Current assessment
[Selected decision](#decision-isolated-whole-review-2026-10-22)

## Yin_C_F0038: All-Bounded-Vector Selfadjoint Duals Have Automatic Adjoint Test Modules

<a id="statement"></a>
<a id="yin_c_f0038"></a>

Provenance: project deduction; root proposed the L1-density route, and another AI agent supplied the normalization, normal-functional construction and complete scalar-pairing argument.
Authorization: the human authorized ordinary density and adjoint-domain research.
No mathematical Role is assigned.
Mathematical assessment at authorship: proof draft; complete candidate below.
Review assessment at authorship: self-reviewed; independent review pending.
Current candidate proof: [yin_c_f0038-p1](#yin_c_f0038-p1).

Let \((\mathcal M,\tau)\) be a finite von Neumann algebra with faithful normal probability trace, and put \(H=L^2(\mathcal M,\tau)\), \(\Omega=1\), and \(P=P_\Omega\).
Use the inner product linear in its second variable.
Let \(X=(X_1,\ldots,X_d)\) be bounded **selfadjoint** generators of \(\mathcal M\), and suppose closable linear operators \(D_{i,0}:\mathcal M\to H\), with domain exactly the bounded-vector space \(\mathcal M\Omega\), satisfy
\[
[D_{i,0},X_j]a=\delta_{ij}Pa\qquad(a\in\mathcal M).
\tag{45.1}
\]
No bounded reference dual and no invariant subspace inside \(\operatorname{Dom}D_{i,0}^*\) are assumed.

For \(\eta_i=D_{i,0}\Omega\in H\), define on \(\mathcal M\)
\[
D_{i,0}^0(a)=D_{i,0}(a)-a\eta_i.
\]
There is a selfadjoint \(\xi_i\in L^1(\mathcal M,\tau)\) such that
\[
\tau(D_{i,0}^0a)=\tau(\xi_i a)\qquad(a\in\mathcal M).
\tag{45.2}
\]
Every bounded \(p\in\mathcal M\) with \(p\xi_i\in H\) belongs to \(\operatorname{Dom}D_{i,0}^*\), and
\[
D_{i,0}^*p=p\xi_i-D_{i,0}^0p+p\eta_i^*.
\tag{45.3}
\]
In particular, putting
\[
h_i=(1+\xi_i^2)^{-1/2}\in\mathcal M,
\qquad V_i=\mathcal M h_i,
\tag{45.4}
\]
gives a dense left \(\mathcal M\)-module in the adjoint domain.
Hence Yin_C_F0030, equivalently the all-\(\mathcal M\) specialization of Yin_C_F0029, applies under (45.1) and closability alone.
This supplies the full affiliated finite-defect criterion and its specified closed-domain bounded-element consequence.

This assertion does not claim \(\xi_i\in L^2\), finite Fisher information, or \(\Omega\in\operatorname{Dom}D_{i,0}^*\).
It removes the separate adjoint-module assumption for these selfadjoint all-bounded-vector duals.
It does not yet remove it for arbitrary dense left-module domains or for general normal tuples.

### Dependencies and Source Interface

The L1 norm identity and completeness are [AP18 Theorem 7.4.5](../audits/literature/AP18/Yin_U003.md#l1-predual-interface).
Standard affiliated spectral calculus gives (45.4).
The polynomial vacuum formula follows from the generator product rule already checked in [Yin_C_F0002](Yin_C_F0002_v1.md#yin_c_f0002); the proof below spells out the needed tracial and star identities, without requiring a separately assumed well-defined difference quotient on a quotient algebra.
Kaplansky density applies because the tuple is selfadjoint and generates \(\mathcal M\).
The final criterion uses [Yin_C_F0029-P2](Yin_C_F0029_v1.md#yin_c_f0029-p2).
Yin_C_F0037 and a bounded reference dual are not dependencies.

<a id="yin_c_f0038-p1"></a>
### Proof yin_c_f0038-p1

Fix \(i\), and write \(D_0=D_{i,0}\), \(\eta=D_0\Omega\), and \(D_0^0(a)=D_0(a)-a\eta\).
Closed graph, applied to \(D_0:(\mathcal M,\|\cdot\|)\to H\), gives a finite bound \(c\) for this map, exactly as in the orbit-map argument of Yin_C_F0036.
The normalized map is also bounded between these spaces because \(\|a\eta\|_2\leq\|a\|\|\eta\|_2\).
No closability of the difference \(D_0^0\) is assumed or needed here.

Since \(D_0\) is closable, choose \(v_n\in\operatorname{Dom}D_0^*\) tending to \(\Omega\) in \(H\).
Put
\[
\ell_n(a)=\langle v_n,D_0a\rangle
=\langle D_0^*v_n,a\rangle
=\tau(\zeta_n a),
\qquad \zeta_n=(D_0^*v_n)^*\in H\subset L^1(\mathcal M).
\]
The functional norm satisfies
\[
\|\ell_n-\ell_m\|\leq c\|v_n-v_m\|_2.
\]
By the accepted L1 duality norm identity, \(\zeta_n\) is Cauchy in L1, and completeness gives a limit \(\zeta\in L^1\).
Taking limits proves
\[
\tau(D_0a)=\tau(\zeta a)\qquad(a\in\mathcal M).
\]
Traciality for the L1-bounded product gives \(\tau(a\eta)=\tau(\eta a)\).
Hence \(\xi=\zeta-\eta\in L^1\) represents \(\tau(D_0^0a)\), establishing (45.2) before any L2 assertion about \(\xi\).

For a formal polynomial \(q\) in the selfadjoint symbols, evaluate its algebraic free difference quotient \(\partial_iq=\sum_\alpha a_\alpha\otimes b_\alpha\) at \(X\).
The product rule and (45.1) give
\[
D_0^0q(X)=\sum_\alpha a_\alpha(X)\tau(b_\alpha(X)),
\qquad
\tau(D_0^0q(X))=(\tau\otimes\tau)((\partial_iq)(X)).
\tag{45.5}
\]
These equalities hold for each formal representative directly; no injectivity of polynomial evaluation is presumed.
Since the generators are selfadjoint, star reverses the two tensor legs of the derivative while taking their adjoints.
Therefore \(\tau(D_0^0(q(X)^*))=\overline{\tau(D_0^0q(X))}\).
Uniqueness of L1 densities, together with ultraweak density of the evaluated starred polynomial algebra, now gives \(\xi=\xi^*\).

For evaluated polynomials \(p,q\), the same product rule gives
\[
\tau(\xi p^*q)
=\tau(D_0^0(p^*q))
=\tau((D_0^0p)^*q)+\tau(p^*D_0^0q).
\tag{45.6}
\]
For precision, the derivative of \(p^*\) is obtained by flipping and taking adjoints of the derivative of \(p\); contracting its first tensor leg by \(\tau\) produces \((D_0^0p)^*\).
This supplies the first term in (45.6) and fixes the normalization and adjoint orientation.

We extend (45.6) to all bounded \(p,q\).
Uniformly bounded strongly convergent inputs \(a_\alpha\to a\) have \(D_0a_\alpha\rightharpoonup D_0a\): test against the dense space \(\operatorname{Dom}D_0^*\) and use the norm bound \(c\) to extend from those tests.
The term \(a_\alpha\eta\) converges strongly, so the normalized map has the same weak convergence property.

For fixed polynomial \(p\), choose uniformly bounded polynomials \(q_\alpha\to q\) strongly by Kaplansky density.
In (45.6), the derivative term passes by that weak convergence, the L1 term passes because \(\xi p^*\) defines a normal functional, and the remaining Hilbert pairing passes by strong convergence.
This gives (45.6) for polynomial \(p\) and arbitrary \(q\in\mathcal M\).
Next approximate arbitrary \(p\in\mathcal M\) by uniformly bounded polynomials converging strongly together with their adjoints.
For the now-fixed \(q\), the same weak-strong pairing and normal L1 pairing give (45.6) in full generality.
The two limits are taken successively, so no weak-weak product limit is used.

If \(p\xi\in H\), selfadjointness of \(\xi\) converts (45.6) into the actual Hilbert-space identity
\[
\langle p,D_0^0q\rangle
=\langle p\xi-D_0^0p,q\rangle
\qquad(q\in\mathcal M).
\]
Adding back the right multiplier gives
\[
\langle p,D_0q\rangle
=\langle p\xi-D_0^0p+p\eta^*,q\rangle,
\]
because \(\langle p,q\eta\rangle=\langle p\eta^*,q\rangle\).
Every vector on the right is in \(H\), and the tested domain is exactly \(\mathcal M\).
This proves the genuine adjoint-domain inclusion and (45.3), rather than only a polynomial-core adjoint identity.

The bounded spectral function \(h=(1+\xi^2)^{-1/2}\) is regular, and \(h\xi\) is bounded.
Consequently every \(p=ah\), \(a\in\mathcal M\), has \(p\xi\in\mathcal M\subset H\).
Its right-multiplication range is dense since \(h\) is positive and injective, and density of \(\mathcal M\) in \(H\) implies that \(\mathcal M h\) is dense.
This proves (45.4).
Applying Yin_C_F0029 with \(\mathcal E=\mathcal M\) and these explicit \(V_i\) proves the final criterion statement.


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
| argument | [Exact material](#yin_c_f0038-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0066_v1.md#yin_c_f0038-l1-density-and-an-actual-adjoint-test-module) | Actual original complete C_F0038 finding at its disclosed accepted-input scope and unknown initial-context relationship; historical source precision and limits remain at this retained original finding. |


### Decision isolated-whole-review-2026-10-22

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:21 |
| status | proved |
| reason | Adopt the actual new isolated whole-proof finding for the unchanged fixed statement and selected argument; retain all original assessments, source depths and useful negative boundaries at their historical scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#yin_c_f0038-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New whole-proof finding](../audits/reviews/Yin_R_F0066_v1.md#fresh-c45-whole) | Actual isolated whole-proof inspection at this exact fixed input, including all necessary accepted-input applicability and stated limits; historical findings remain separately unknown. |

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
| argument | [Exact material](#yin_c_f0038-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0066_v1.md#yin_c_f0038-l1-density-and-an-actual-adjoint-test-module) | Original selected finding; its actual scope and limits remain in the cited review. |

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

Review: [Exact material](../audits/reviews/Yin_R_F0066_v1.md#yin_c_f0038-l1-density-and-an-actual-adjoint-test-module).

The original whole-source review included the bounded-reference comparison, the normal starred-commutator argument and the selfadjoint L1-density construction.
Its accompanying source context and complete original scope remain in the cited finding.

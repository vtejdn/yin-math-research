---
author: Yin
---

# Bare polynomial-core duals on real polynomial spectral graphs restore both all-M domains

## Current assessment
[Selected decision](#decision-isolated-review-2026-10-22)

## Polynomial-Core Normal Duals: Rigidity and Polynomial Spectral Graphs

<a id="statement"></a>

Registration checkpoint, 2026-09-11: Section 3 is now ordinary Claim Yin_C_F0040, proved after [root's independent review](../audits/reviews/Yin_R_F0070_v1.md#original-f0055-account).
No mathematical Role is assigned.
The author's original unnumbered/candidate-stage descriptions below are preserved as history; current assessments are recorded in the [selected assessment](#current-assessment).

Date: 2026-09-11.
Human author: Yin.
Proof development: another AI agent.
Authorization: the user selected the first two groups of research questions and Group III question 7, with polynomial dual domains the first priority; the coordinating agent assigned this bounded first-stage investigation under the normal-domain investigation.
Record kind: substantive exploration and complete unnumbered proof candidate.
No Claim ID, Role designation, lemma extraction, or main-theorem designation is made here.
At that authoring checkpoint, the coordinating agent was responsible for arranging independent review and recording the adoption decision.

The earlier proofs Yin_C_F0025-Yin_C_F0028 and Yin_C_F0039 remain unchanged.
This record proposes a new sufficient geometric case for the **bare starred polynomial core**, not a resolution for arbitrary normal spectra.

## 1. Exact Question and Reuse Check

Let \((\mathcal M,\tau)\) be finite tracial with faithful normal probability trace, \(H=L^2(\mathcal M,\tau)\), \(\Omega=1\), and \(P=P_\Omega\).
Inner products are linear in the second variable.
A bounded normal tuple \(X\) generates \(\mathcal M\).
Distinguish
\[
\mathcal P_X=\mathbb C\langle X,X^*\rangle,
\qquad \mathcal A_X=\mathbb C\langle X\rangle.
\]
Assume \(D_{i,0}:\mathcal P_X\to H\) satisfies
\[
\Omega\in\operatorname{Dom}D_{i,0}^*,\qquad
[D_{i,0},X_j]=\delta_{ij}P,
\qquad [D_{i,0},X_j^*]\text{ has a compact bounded extension}.
\tag{1}
\]
The target is whether every
\[
f\in\operatorname{Div}_{L^0(\mathcal M)}\mathcal A_X\cap\mathcal M
\]
has bounded finite-rank representatives for
\[
\beta_i^f(p,q)=\langle D_{i,0}^*p,fq\rangle-
\langle f^*p,D_{i,0}q\rangle,
\qquad p,q\in\mathcal P_X.
\tag{2}
\]
No left \(\mathcal M\)-module domain is assumed.

The following existing inputs were read before proof development:

- [Yin_C_F0025](Yin_C_F0025_v1.md#yin_c_f0025): (1) implies closability, compact-to-Hilbert-Schmidt upgrade, the unique normal spectral-phase formula, maximal Delta, and the reverse implication from bounded finite-rank weak forms to affiliated rationality.
- [Yin_C_F0026](Yin_C_F0026_v1.md#yin_c_f0026): the arbitrary-denominator counterexample has a **noncompact** extra starred commutator and does not meet (1).
- [Yin_C_F0027](Yin_C_F0027_v1.md#yin_c_f0027): bounded rational forward calculus; two uniform polynomial \(\infty\)-to-2 bounds restore the actual closed operator and actual adjoint on all of \(\mathcal M\).
- [Yin_C_F0028](Yin_C_F0028_v1.md#yin_c_f0028): the full one-coordinate question is already solved, even under merely bounded starred commutators.
- [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001): the exact starred-core derivation and vacuum-adjoint interface, with Hilbert tensor codomain.
- [Dab10-U002](../audits/literature/Dab10/Yin_U002.md#dab10-u002): selfadjoint finite-Fisher contractions and their actual adjoints have \(\infty\)-to-2 bounds.
- [Yin_C_F0039's analytic-arc verification](Yin_C_F0039_v1.md#analytic-arc-application): a kernel holomorphic near a compact real square has a bounded-Borel projective tensor expansion, by finite interval partitions and summable Taylor coefficients.
  Its previous all-\(\mathcal M\) domain premise is **not** imported into the present statement.

Consequently the selfadjoint polynomial-core problem is already covered: normalize (1), identify the ordinary free difference quotients and their conjugates, and apply Dab10 followed by Yin_C_F0027.
The new issue concerns non-selfadjoint normal coordinates.

A bounded external search for unitary/normal conjugate-variable contraction estimates did not supply a theorem directly covering arbitrary normal starred cores.
A Cauchy-transform search also located nonhomogeneous T1/curvature methods, but their growth and truncation assumptions were not verified in this setting and they are not proof dependencies.
The decisive construction below instead uses the already audited inputs just listed.
No exhaustive novelty search or assertion of global openness is made.

## 2. Rigidity of the Exact Compact-Core Hypothesis

Suppose \(D_{i,0}\) and \(\widetilde D_{i,0}\) both meet (1) for the same tuple.
Yin_C_F0025 gives nonatomic coordinate laws \(\mu_j\) and the fixed Hilbert-Schmidt commutators
\[
[D_{i,0},X_j^*]=[\widetilde D_{i,0},X_j^*]
=\delta_{ij}\Theta(k_j),
\quad
k_j(z,w)=\frac{\bar z-\bar w}{z-w}
\quad(z\ne w).
\tag{3}
\]
The diagonal is null.
Here \(\Theta(a\otimes b)=aPb\), extended from the Hilbert tensor product to Hilbert-Schmidt operators.

Their difference commutes on the core with every starred generator.
Induction on words therefore gives
\[
(D_{i,0}-\widetilde D_{i,0})p=p\eta_i,
\qquad \eta_i=(D_{i,0}-\widetilde D_{i,0})\Omega\in H.
\tag{4}
\]
In particular normalized core duals are unique.
Right multiplication \(p\mapsto p\eta_i\) has adjoint \(p\mapsto p\eta_i^*\) on the polynomial core.
Its contribution to (2) vanishes by traciality:
\[
\langle p\eta_i^*,fq\rangle
=\tau(\eta_i p^*fq)
=\tau(p^*fq\eta_i)
=\langle f^*p,q\eta_i\rangle.
\tag{5}
\]
Thus the weak forms depend only on the tuple under the exact compact hypothesis.
An attempted counterexample obtained by adding a differential operator commuting with the unstarred coordinates must fail compactness, or merely change the harmless right-multiplication term in (4).
This is a useful reduction, not a proof of the forward implication.

<a id="yin_c_f0040"></a>
## 3. Yin_C_F0040: Polynomial Spectral Graphs

Suppose in addition that, for each \(i\),
\[
X_i=S_i+\mathrm i g_i(S_i),
\qquad S_i=S_i^*\in\mathcal M,
\qquad g_i\in\mathbb R[t].
\tag{6}
\]
No free independence, smallness of coefficients, bounded dual reference, or initial all-\(\mathcal M\) domain is assumed.

**Candidate conclusion.**
Under (1) and (6), the actual closures satisfy
\[
\mathcal M\subseteq
\operatorname{Dom}\overline{D_{i,0}}
\cap\operatorname{Dom}D_{i,0}^*.
\tag{7}
\]
Consequently Yin_C_F0024 applies to their restrictions to \(\mathcal M\).
In particular, for bounded \(f\), affiliated rationality over the **unstarred** \(\mathcal A_X\) is equivalent to bounded finite rank of all forms (2), and the full affiliated bounded-fraction criterion is available.

The proof derives finite Fisher information for the auxiliary selfadjoint tuple \(S\), then reconstructs the original dual's two core estimates.
It does not assert that \(S_i\) belongs to the unstarred rational field of \(X\), nor that the bounded division closures in \(\mathcal M\) and \(L^0(\mathcal M)\) agree.

### 3.1. Normalize and change the derivative coordinates

As in Yin_C_F0025, first subtract \(pD_{i,0}\Omega\), which preserves (1) and (2), and relabel the normalized operators.
Their Hilbert-Schmidt commutators give derivations
\[
\partial_i:\mathcal P_X\to H\otimes_2 H,
\quad \partial_iX_j=\delta_{ij}1\otimes1,
\quad 1\otimes1\in\operatorname{Dom}\partial_i^*,
\quad D_{i,0}=(\mathrm{id}\otimes\tau)\partial_i.
\tag{8}
\]
Since \(S_i=(X_i+X_i^*)/2\), and \(g_i\) is polynomial,
\[
\mathcal P_X=\mathbb C\langle S_1,\ldots,S_d\rangle=:\mathcal P_S,
\qquad W^*(S)=\mathcal M.
\tag{9}
\]

For bounded functions \(a,b\) of \(S_i\), define an **inner** bimodule map
\[
I_{a\otimes b}(u\otimes v)=ua\otimes bv.
\tag{10}
\]
It commutes with all outer left and right \(\mathcal M\) actions; therefore its composition with a derivation is again a derivation.
This inner action, rather than outer multiplication of the derivative, is essential.

Let \(I_i\) be a compact real interval containing \(\sigma(S_i)\), and put
\[
h_i(s,t)=\begin{cases}(g_i(s)-g_i(t))/(s-t),&s\ne t,\\g_i'(s),&s=t,\end{cases}
\quad J_i(s,t)=1+\mathrm i h_i(s,t),
\quad K_i(s,t)=J_i(s,t)^{-1}.
\tag{11}
\]
The divided difference \(h_i\) is a polynomial in two variables, real on \(I_i^2\); hence \(|J_i|\ge1\) there.
Formula (3) evaluated on the graph gives
\[
k_{X_i}(r_i(s),r_i(t))=
\frac{1-\mathrm i h_i(s,t)}{1+\mathrm i h_i(s,t)},
\qquad r_i(s)=s+\mathrm i g_i(s).
\]
Therefore, as Hilbert tensor vectors,
\[
\partial_i S_j=\delta_{ij}K_i(S_i\otimes1,1\otimes S_i).
\tag{12}
\]
Null diagonal conventions cause no change: the graph map is injective and Yin_C_F0025 has already supplied atomlessness.

The polynomial inner multiplier \(I_{J_i}\) is a finite sum of maps (10).
Set
\[
\delta_i=I_{J_i}\partial_i.
\tag{13}
\]
It is a derivation on \(\mathcal P_S\), and (12) gives \(\delta_iS_j=\delta_{ij}1\otimes1\).
Hence it is the ordinary evaluated free difference quotient on the selfadjoint generators.

### 3.2. The new derivatives have conjugate variables

For completeness the required adjoint-domain check does not assume a reality condition on \(\partial_i\).
Whenever \(a,b\in\mathcal P_X\), expanding \(\partial_i(a^*pb^*)\) and taking \(\tau\otimes\tau\) shows that
\[
p\longmapsto\langle a\otimes b,\partial_i p\rangle
\]
is bounded in \(\|p\|_2\).
The middle product-rule term is the displayed functional.
The other terms have respective bounds
\[
\|\partial_i(a^*)\|_2\|b\|\|p\|_2,
\qquad
\|a\|\|\partial_i(b^*)\|_2\|p\|_2,
\]
and the vacuum-adjoint term has bound \(\|a\|\|b\|\|\partial_i^*(1\otimes1)\|_2\|p\|_2\).
This proves
\[
\mathcal P_X\otimes_{\mathbb C}\mathcal P_X
\subseteq\operatorname{Dom}\partial_i^*.
\tag{14}
\]
All these estimates are ordinary Hilbert tensor pairings; they do not require bounded tensor factors for \(\partial_i(a^*)\).

Since \(J_i\) is polynomial in \(S_i\), the vector \(I_{J_i}^*(1\otimes1)\) lies in the domain (14).
Thus
\[
\zeta_i:=\partial_i^*I_{J_i}^*(1\otimes1)\in H,
\qquad
1\otimes1\in\operatorname{Dom}\delta_i^*.
\tag{15}
\]
These are the ordinary L2 conjugate variables for the selfadjoint tuple \(S\).
The audited finite-Fisher interface applies; there is no new hypothesis of freeness of their joint law.

Write \(E_{i,0}=(\mathrm{id}\otimes\tau)\delta_i\) and \(E_i=\overline{E_{i,0}}\).
Dab10-U002 and its closed-domain argument give
\[
\mathcal M\subseteq\operatorname{Dom}E_i\cap\operatorname{Dom}E_i^*,
\quad
\|E_i a\|_2\le c_i\|a\|,
\quad \|E_i^*a\|_2\le c_i'\|a\|
\quad(a\in\mathcal M),
\tag{16}
\]
with, for example, \(c_i=4\|\zeta_i\|_2\) and \(c_i'=5\|\zeta_i\|_2\).

### 3.3. Recover both original core estimates

Because \(J_i\) has no zero on the compact real square, \(K_i=1/J_i\) is holomorphic on a complex neighborhood of that square.
Apply the finite-partition Taylor argument already proved in Yin_C_F0039 to obtain bounded functions \(a_{in},b_{in}\) of \(S_i\) with
\[
K_i(s,t)=\sum_n a_{in}(s)b_{in}(t),
\qquad L_i:=\sum_n\|a_{in}\|\|b_{in}\|<\infty.
\tag{17}
\]
These coefficients can be bounded Borel functions; polynomial membership is no longer needed, because (16) has been obtained first.
The sum defines an inner bounded bimodule map \(I_{K_i}\) on the entire coarse Hilbert space.
The commuting spectral calculus for the two inner actions gives \(I_{K_i}I_{J_i}=I\); consequently
\[
\partial_i=I_{K_i}\delta_i\quad\text{on }\mathcal P_S.
\tag{18}
\]

For right multiplication \(\rho(a)u=ua\), the Hilbert-Schmidt identification satisfies
\[
\Theta(I_{a\otimes b}v)=\rho(a)\Theta(v)\rho(b).
\tag{19}
\]
For \(p\in\mathcal P_S\), \(\Theta(\delta_i p)=[E_i,p]\) is bounded and finite rank.
The projective sum (17) converges in Hilbert-Schmidt norm after applying it to this operator.
Applying the resulting identity to \(\Omega\) gives
\[
D_{i,0}p
=\sum_n\bigl(E_i(p b_{in})-pE_i(b_{in})\bigr)a_{in}.
\tag{20}
\]
Every input of \(E_i\) in this formula is bounded and is therefore in its **actual** domain by (16).
The identity \([E_i,p]b=E_i(pb)-pE_i b\) is justified by the bounded polynomial commutator and its closed-domain extension.
Hence
\[
\|D_{i,0}p\|_2\le2c_iL_i\|p\|.
\tag{21}
\]

Put \(T_{i,p^*}=\Theta(\partial_i(p^*))\) and \(\xi_i=D_{i,0}^*\Omega\).
Yin_C_F0025's actual polynomial adjoint formula says
\[
D_{i,0}^*p=p\xi_i-T_{i,p^*}^*\Omega.
\tag{22}
\]
Taking adjoints of (19) and the projective sum gives
\[
T_{i,p^*}^*\Omega
=\sum_n\bigl(pE_i^*(a_{in}^*)-E_i^*(p a_{in}^*)\bigr)b_{in}^*.
\tag{23}
\]
Here \([E_i,p^*]^*=-[E_i^*,p]\); all displayed adjoint inputs again belong to \(\mathcal M\).
Thus
\[
\|D_{i,0}^*p\|_2
\le\bigl(\|\xi_i\|_2+2c_i'L_i\bigr)\|p\|.
\tag{24}
\]
This explicitly proves the second estimate; it is not inferred from (21) alone.

If the originally specified dual was not normalized, add back \(p\eta_i\), with \(\eta_i=D_{i,0}^{\mathrm{original}}\Omega\).
Its adjoint on the core is \(p\eta_i^*\), and each has \(\infty\)-to-2 norm at most \(\|\eta_i\|_2\).
Therefore both estimates remain valid for the original operators.

Yin_C_F0027 now applies to the actual closures of those original polynomial-core operators, proving (7) and their all-\(\mathcal M\) generator identities.
Yin_C_F0024 gives affiliated rationality implying the bounded finite-rank closed-domain commutator, hence the representative (2).
Yin_C_F0025 gives the reverse weak-form implication.
This completes the candidate proof.

## 4. Concrete Coverage and the Remaining Boundary

The candidate covers tuples
\[
X_i=S_i+\mathrm i\varepsilon_i S_i^2
\quad\text{and, more generally,}\quad
X_i=S_i+\mathrm i g_i(S_i),\quad g_i\in\mathbb R[t],
\]
for arbitrary real coefficients and arbitrary joint law satisfying (1).
Nonzero quadratic terms give genuinely noncircular normal spectral arcs.
Nondegenerate coordinatewise affine changes preserve the hypotheses and conclusion after the corresponding scalar rescaling of each dual.

In the quadratic case the multiplier is particularly explicit:
\[
K_i(s,t)=\frac1{1+\mathrm i\varepsilon_i(s+t)}
=\int_0^\infty e^{-u}
e^{-\mathrm i\varepsilon_ius}e^{-\mathrm i\varepsilon_iut}\,du.
\]
The integral is a projective tensor Bochner integral of norm at most one; it provides a direct check of the signs and of the absence of a smallness condition.
The general proof uses the countable sum (17).

This new sufficient case does not cover a general analytic arc automatically.
For \(X_i=r_i(S_i)\), merely knowing \(S_i\in W^*(X_i)\) does not put it in the original polynomial domain.
Nor does projective summability of an arbitrary phase ensure that the tensor tested against \(\partial_i^*\) lies in its adjoint domain.
The polynomial graph assumption addresses both obligations through (9) and (14)-(15).

The full circle case, arbitrary normal planar spectra, and a direct proof of the forward implication without the two core estimates remain separate questions.
A counterexample under (1) cannot be obtained solely from the noncompact differential perturbation used in Yin_C_F0026.
The new proof does not convert bounded affiliated outputs into bounded inverse matrix representations, which Yin_C_F0012 already excludes in general.

## 5. Review Handoff

Author checks completed: equality of the two **starred** polynomial algebras, inner versus outer multiplier placement, polynomial divided-difference cancellation, polynomial-tensor adjoint tests without a reality premise, finite-Fisher applicability after the change of variables, order of right multipliers in (19)-(23), actual domains of all transformed expressions, both independent core estimates, and restoration of the originally specified normalization.

Independent review is requested for the complete proof in Section 3, especially the adjoint-domain estimate (14), the operator-adjoint sign in (23), and the application of Yin_C_F0027 to the actual original closure.
No numerical experiment, proof-assistant verification, external human review, or historical-priority claim is made.
Until that review, the candidate is not registered or promoted.


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
| argument | [Exact material](#31-normalize-and-change-the-derivative-coordinates) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0070_v1.md#review-outcome) | Complete Section 3 polynomial-spectral-graph proof at the exact compact starred-core/vacuum premises, with Section 2 rigidity as an internal observation and the original unstarred algebra preserved. Actual original finding with unknown initial-context arrangement; historical date and accepted-input depth unchanged. |


### Decision isolated-review-2026-10-22

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:39 |
| status | proved |
| reason | Adopt the new isolated complete finding on the unchanged fixed mathematics and its actual necessary interfaces. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#31-normalize-and-change-the-derivative-coordinates) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New isolated complete finding](../audits/reviews/Yin_R_F0070_v1.md#isolated-polynomial-graph-finding) | Complete Section 2 rigidity and Section 3 polynomial-spectral-graph proof, inner multipliers, actual adjoints, both core estimates and equality with the original closure, retaining the original unstarred algebra. |

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
| argument | [Exact material](#31-normalize-and-change-the-derivative-coordinates) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0070_v1.md#original-f0055-account) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0070_v1.md#original-f0055-account).

Material covered by that review: [Exact material](Yin_C_F0040_v1.md).

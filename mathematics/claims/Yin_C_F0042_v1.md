---
author: Yin
---

# Embedded analytic spectral arcs restore both original all-M domains from the bare polynomial core

## Current assessment
[Selected decision](#decision-isolated-complete-theorem-and-example-adoption)

## Embedded Analytic Spectral Arcs from the Original Polynomial Core

<a id="statement"></a>

Date: 2026-09-11.
Human author: Yin.
Proof development: another AI agent.
Record kind: substantive research and complete proof under the separate normal-domain investigation, principally the polynomial-domain question.
Registered as ordinary Claim Yin_C_F0042 after [independent complete review](../audits/reviews/Yin_R_F0072_v1.md#5-geometric-and-goal-boundaries); no mathematical Role is assigned.
Provenance: project deduction using the inputs below, with no novelty assertion.
The new approximation source is indexed as [GW25-U001](../audits/literature/GW25/Yin_U001.md#gw25-u001).
The previous [Yin_C_F0041 spectral-graph proof](Yin_C_F0041_v1.md#yin_c_f0041) is preserved.

<a id="yin_c_f0042"></a>
## 1. Statement and Reuse Boundary

Let (M,tau) be a finite von Neumann algebra with faithful normal tracial state, H=L2(M), Omega=1, and inner product linear in its second variable.
Let the bounded normal tuple X generate M, and retain the two different algebras
\[
\mathcal P_X=\mathbb C\langle X,X^*\rangle,
\qquad \mathcal A_X=\mathbb C\langle X\rangle.
\]
Assume exactly the compact polynomial-core hypotheses of [Yin_C_F0025](Yin_C_F0025_v1.md#yin_c_f0025): the operators D_i0 have domain P_X, Omega belongs to Dom(D_i0*), and
\[
[D_{i0},X_j]=\delta_{ij}P_\Omega,
\qquad [D_{i0},X_j^*]\text{ has a compact bounded extension}.
\tag{1}
\]
Assume, for each coordinate,
\[
X_j=r_j(S_j),\qquad S_j=S_j^*,\qquad \sigma(S_j)\subseteq I_j=[a_j,b_j],
\tag{2}
\]
where I_j is nondegenerate and r_j is holomorphic and injective on an open neighborhood of I_j, with nonzero derivative there.
In particular the entire compact arc r_j(I_j), rather than only individual local graph charts, is available.

**Conclusion:** for the originally specified operators,
\[
M\subseteq\operatorname{Dom}\overline{D_{i0}}
       \cap\operatorname{Dom}D_{i0}^*.
\tag{3}
\]
Consequently the full Yin_C_F0024 affiliated-fraction criterion and the equivalence with bounded finite-rank representatives of Yin_C_F0025's polynomial weak forms apply, with the original unstarred A_X.
No claim that S_j belongs to that rational algebra is made.

The local reuse search covered Yin_C_F0025, Yin_C_F0027, Yin_C_F0040, Yin_C_F0041, [Yin_C_F0039's analytic-arc multiplier construction](Yin_C_F0039_v1.md#analytic-arc-application), [Dab10-U002](../audits/literature/Dab10/Yin_U002.md#dab10-u002), and [Tre17-U001](../audits/literature/Tre17/Yin_U001.md#tre17-u001).
Yin_C_F0039 had a larger domain premise, and Yin_C_F0041 used the special inclusion P_S contained in P_X.
Neither supplied the missing graph-domain approximation for a general analytic arc.
The new step below supplies it before reusing their estimates.

## 2. Additional Accepted Approximation Input

The only new complex-approximation input is the classical polynomial form of Runge's theorem: a function holomorphic near a planar compact set with connected complement admits uniform polynomial approximations on that compact set.
The exact statement was read in the primary published article by Adi Glucksam and Benjamin Weiss, *Measurable Entire Functions II*, International Mathematics Research Notices 2025(21), rnaf330, [Theorem 2 in Section 3](https://academic.oup.com/imrn/article/2025/21/rnaf330/8307121), DOI 10.1093/imrn/rnaf330.
The article was published on 31 October 2025 and attributes this statement to Runge (1885).

This is acceptance of the established Runge theorem, not a full audit of that unrelated paper or a new proof of Runge.
The same statement was checked in Arun Debray's [author-hosted course notes](https://www.math.purdue.edu/~adebray/lecture_notes/116notes.pdf), dated 21 August 2015, Theorem 6.4, printed p. 16.
The elementary facts about holomorphic inverse functions, Jordan domains, and Cauchy's integral formula used below are the usual complex-analysis foundations.
The operator graph and tensor conclusions are proved here; they are not asserted by either approximation source.

For one coordinate, shrink the univalence neighborhood if necessary and take nested filled Bernstein ellipses B_1,B_2 for I, with
\[
I\subset\operatorname{int}B_1\subset B_1
\subset\operatorname{int}B_2\subset B_2\subset U,
\]
where U is an open set on which r is holomorphic and injective.
Let h be the holomorphic inverse on r(U), Gamma=r(I), K=r(B_2), and gamma=r(boundary B_1), positively oriented.
The map r is a homeomorphism on a neighborhood of B_2.
Its image K is the filled Jordan domain bounded by r(boundary B_2), and has connected complement.
The compact Gamma is inside gamma, at a strictly positive distance from it.

Runge therefore gives scalar polynomials p_n with
\[
\varepsilon_n:=\sup_K|p_n-h|\longrightarrow0.
\tag{4}
\]
No rate of convergence is required.
For e_n=p_n-h, Cauchy's formula gives, for z,w in Gamma, including the removable diagonal,
\[
e_n^{[1]}(z,w)
=\frac1{2\pi\mathrm i}\int_\gamma
       \frac{e_n(\zeta)}{(\zeta-z)(\zeta-w)}\,d\zeta.
\]
Hence
\[
\sup_{\Gamma^2}|p_n^{[1]}-h^{[1]}|
\le\frac{\operatorname{length}(\gamma)}
          {2\pi\operatorname{dist}(\gamma,\Gamma)^2}\varepsilon_n
\longrightarrow0.
\tag{5}
\]
This controls difference quotients even when the straight chord between two points leaves the arc neighborhood.
Uniform approximation only on Gamma, without this interior contour control, would not give (5).

## 3. The Closed Coarse Derivative and Graph Approximation

Normalize each original operator on P_X by subtracting p maps to p eta_i, where eta_i=D_i0 Omega, and write N_i0 for the normalized operator.
Yin_C_F0025 proves closability of both D_i0 and N_i0, and supplies a coarse derivation
\[
\partial_{i0}:\mathcal P_X\longrightarrow H\otimes_2H,
\quad \partial_{i0}X_j=\delta_{ij}1\otimes1,
\quad 1\otimes1\in\operatorname{Dom}\partial_{i0}^*,
\quad N_{i0}=C\partial_{i0},
\tag{6}
\]
where C=id tensor tau is the bounded Hilbert-space contraction.
Its polynomial-tensor adjoint estimate is
\[
\|\partial_{i0}^*(u\otimes v)\|_2
\le\|u\|\|v\|\|\xi_i\|_2
 +\|\partial_{i0}(u^*)\|_2\|v\|
 +\|u\|\|\partial_{i0}(v^*)\|_2,
\quad \xi_i=\partial_{i0}^*(1\otimes1),
\tag{7}
\]
for u,v in P_X, as proved by the Leibniz/vacuum-adjoint argument in Yin_C_F0040.
In particular P_X algebraically tensor P_X is contained in the adjoint domain and is dense in the Hilbert tensor product.
Thus partial_i0 is closable.
Denote its actual closure by partial_i^c; its adjoint equals partial_i0*.

For the polynomials from (4) associated to coordinate j, the polynomial product rule gives
\[
\partial_{i0}p_n(X_j)
=\delta_{ij}\,p_n^{[1]}(X_j\otimes1,1\otimes X_j)(1\otimes1).
\tag{8}
\]
The two displayed spectral actions commute and are normal.
The normal spectral theorem, (4), and (5) imply operator-norm convergence p_n(X_j) to S_j and Hilbert tensor convergence of (8) to
\[
\delta_{ij}K_j(S_j\otimes1,1\otimes S_j)(1\otimes1),
\qquad
K_j(s,t)=\frac{s-t}{r_j(s)-r_j(t)}
\tag{9}
\]
with diagonal value 1/r_j'(s).
This uses h(r_j(s))=s.
Closedness puts S_j in Dom(partial_i^c) with derivative (9).

Starred approximants are also controlled; no reality of partial_i0 is assumed.
Yin_C_F0025's normal spectral phase gives, off the null spectral diagonal,
\[
\partial_{i0}\bigl(p_n(X_j)^*\bigr)(z,w)
=\delta_{ij}\frac{\overline{p_n(z)}-\overline{p_n(w)}}{z-w}
=\delta_{ij}\overline{p_n^{[1]}(z,w)}
                         \frac{\bar z-\bar w}{z-w}.
\tag{10}
\]
The phase has absolute value one.
By (5), this tends uniformly off the diagonal to the same K_j kernel, because h is real on Gamma.
The diagonal has zero product spectral measure by Yin_C_F0025's atomlessness.
Also p_n(X_j)* tends in norm to S_j.
Thus the starred approximants converge to the same closed-derivative value.

For completeness this extends to the algebra generated by P_X and P_S without invoking an unproved Leibniz rule for arbitrary graph-domain elements.
In any fixed word in X,X*,S, replace each S_j by p_n(X_j), or by its adjoint when obtaining the adjoint word.
The resulting q_n belong to P_X, converge in operator norm, and are uniformly bounded.
Expanding the finite polynomial product rule, each derivative term converges in Hilbert tensor norm by (8)-(10).
Indeed, if a_n,b_n converge in operator norm and v_n converges in the Hilbert tensor product, then
\[
\|a_n\cdot v_n\cdot b_n-a\cdot v\cdot b\|_2\longrightarrow0
\]
by the bounded outer bimodule actions and a three-term difference estimate.
Closedness supplies a unique value for each evaluated word, even when it has more than one polynomial presentation.
The resulting restriction is a derivation and respects the adjoint-word approximation just described.

In particular P_S is contained in the domain of every partial_i^c.
Let
\[
\partial_i^S=\partial_i^c|_{\mathcal P_S},
\qquad F_{i0}^{\mathrm{nor}}=C\partial_i^S.
\tag{11}
\]
Since S_j=h_j(X_j) and X_j=r_j(S_j), W*(S)=M, so P_S is dense in H.
Each normalized graph approximation also gives
\[
F_{i0}^{\mathrm{nor}}\subseteq\overline{N_{i0}}.
\tag{12}
\]
Only the graph approximations above are used to prove this inclusion.
There is no assertion that the closure of the contraction C partial_i0 equals C partial_i^c on every possible domain.

The adjoint relation is precise: restriction and closure give
\[
(\partial_i^S)^*\supseteq(\partial_i^c)^*
=\partial_{i0}^*,
\qquad (\partial_i^S)^*(1\otimes1)=\xi_i.
\tag{13}
\]
Thus the new derivative inherits the actual vacuum-adjoint vector.
Likewise (12) implies that the original normalized vacuum adjoint belongs to the adjoint of F_i0^nor; it agrees with xi_i by C*Omega=1 tensor 1.

## 4. Selfadjoint Free Difference Quotients on the New Core

Define the continuous divided difference
\[
J_i(s,t)=r_i^{[1]}(s,t),\qquad K_i=J_i^{-1}.
\tag{14}
\]
Injectivity and the nonvanishing derivative imply J_i is nonzero on I_i squared, including its diagonal.
Holomorphic removability across the diagonal and compactness give a complex neighborhood of the square on which both J_i and K_i are holomorphic and bounded.
No positive-real-part hypothesis or bound |J_i|>=1 is required; all constants may depend on the arc.

Use the inner bimodule maps
\[
I_{a\otimes b}(u\otimes v)=ua\otimes bv.
\]
The two inner spectral actions of S_i commute.
Hence I_Ji is bounded, commutes with all outer M-bimodule actions, and has inverse I_Ki.
Put
\[
\delta_i=I_{J_i}\partial_i^S.
\tag{15}
\]
Equations (9) and (14) give delta_i(S_j)=delta_ij 1 tensor 1.
As a well-defined derivation on the selfadjoint polynomial algebra P_S, it is the canonical evaluated free difference quotient.
The existence of its conjugate variable is proved next, rather than inferred from boundedness of I_Ji.

Let t_n(s) be the affinely rescaled Chebyshev polynomial on I_i.
Its norm is at most one and its derivative norm is at most 2n^2/(b_i-a_i).
From (9) and the product rule on P_S,
\[
\partial_i^S v(S_i)=v^{[1]}(S_i\otimes1,1\otimes S_i)K_i(1\otimes1),
\quad
\|\partial_i^S v(S_i)\|_2
\le\|v'\|_{\infty,I_i}\|K_i(1\otimes1)\|_2.
\tag{16}
\]
The ordinary real mean-value estimate is used for v on the parameter interval, not for functions on the curved arc.

The derivation/vacuum-adjoint proof of (7) applies anew to partial_i^S, using (13) and u,v in P_S.
Consequently
\[
\|(\partial_i^S)^*(t_m(S_i)\otimes t_n(S_i))\|_2
\le C_i(1+m^2+n^2).
\tag{17}
\]
Tre17-U001, exactly as used in Yin_C_F0041, supplies a two-variable Chebyshev expansion for J_i with coefficients c_mn satisfying
\[
J_i(s,t)=\sum_{m,n\ge0}c_{mn}t_m(s)t_n(t),
\qquad \sum_{m,n}|c_{mn}|(1+m^2+n^2)<\infty.
\tag{18}
\]
Its geometric coefficient estimate applies on a sufficiently small polyellipse inside the holomorphic neighborhood of I_i squared.
Conjugate the coefficients for I_Ji*(1 tensor 1); the t_n are selfadjoint when evaluated at S_i.
Formula (17) shows convergence both of these tensor partial sums and of their adjoint images.
Since (partial_i^S)* is closed,
\[
I_{J_i}^*(1\otimes1)\in\operatorname{Dom}(\partial_i^S)^*,
\qquad
\zeta_i=(\partial_i^S)^*I_{J_i}^*(1\otimes1)
\tag{19}
\]
is an L2 conjugate variable for S_i.
This verifies the selfadjoint finite-Fisher hypotheses for the tuple S.
No original adjoint is replaced by a formal derivative in this step.

## 5. Reconstruction and Both Actual Domain Estimates

Let E_i be the closure of (id tensor tau) delta_i on P_S.
The accepted Dab10-U002 contraction estimates, in the form already checked in Yin_C_F0040 and Yin_C_F0041, give
\[
M\subseteq\operatorname{Dom}E_i\cap\operatorname{Dom}E_i^*,
\quad \|E_i x\|_2\le c_i\|x\|,
\quad \|E_i^*x\|_2\le c_i'\|x\|\quad(x\in M).
\tag{20}
\]
For example the retained constants 4||zeta_i||_2 and 5||zeta_i||_2 suffice.
These are statements about the actual closed operator and its Hilbert adjoint.

The same analytic coefficient theorem gives
\[
K_i(s,t)=\sum_r a_r(s)b_r(t),\qquad
L_i=\sum_r\|a_r\|_{\infty,I_i}\|b_r\|_{\infty,I_i}<\infty,
\tag{21}
\]
where the factors are scalar multiples of rescaled Chebyshev polynomials.
Since partial_i^S=I_Ki delta_i, the already checked inner-multiplier reconstruction gives, for p in P_S,
\[
F_{i0}^{\mathrm{nor}}p
=\sum_r\bigl(E_i(p b_r)-pE_i(b_r)\bigr)a_r,
\quad
\|F_{i0}^{\mathrm{nor}}p\|_2\le2c_iL_i\|p\|.
\tag{22}
\]
All bounded factors in this formula lie in the actual domain in (20).
The series converges absolutely in H by (20)-(21).
This is the same Hilbert-Schmidt/inner-action identity as Yin_C_F0041 (16), with the new J_i and K_i; no commutation between different coordinates is assumed.

There is also a separate adjoint estimate.
On P_S the polynomial commutator of F_i0^nor is Theta(partial_i^S p), since contraction of the derivation's Leibniz rule gives this identity directly.
With xi_i=(F_i0^nor)*Omega, the polynomial adjoint argument gives
\[
(F_{i0}^{\mathrm{nor}})^*p
=p\xi_i-\Theta(\partial_i^S(p^*))^*\Omega.
\]
The adjoint inner-multiplier identity checked in Yin_C_F0041 gives
\[
\Theta(\partial_i^S(p^*))^*\Omega
=\sum_r\bigl(pE_i^*(a_r^*)-E_i^*(p a_r^*)\bigr)b_r^*.
\]
It follows that
\[
\|(F_{i0}^{\mathrm{nor}})^*p\|_2
\le(\|\xi_i\|_2+2c_i'L_i)\|p\|.
\tag{23}
\]
The order of the right factors and the sign come from [E_i,p*]*=-[E_i*,p].
The vacuum adjoint and these polynomial adjoints exist by (12)-(13) and the bounded commutators; they are not assumed in (23).

Restore the original normalization by defining on P_S
\[
F_{i0}p=F_{i0}^{\mathrm{nor}}p+p\eta_i.
\tag{24}
\]
For the norm-convergent approximants q_n from Section 3, q_n eta_i tends in H to p eta_i.
Since D_i0 q_n=N_i0 q_n+q_n eta_i, the same graph limits prove
\[
F_{i0}\subseteq D_i:=\overline{D_{i0}}.
\tag{25}
\]
In particular F_i0 is closable.
The adjoint contribution of right multiplication is p eta_i*, by traciality, and both it and p eta_i have norm at most ||eta_i||_2 ||p||.
Thus (22)-(23) give both infinity-to-2 bounds for F_i0 and its actual polynomial adjoint, with enlarged constants.
Their vacuum vector is the restriction of the original D_i0*Omega, as is also immediate from (25).

## 6. Equality with the Original Closure

Put T_i=closure(F_i0).
We have T_i contained in D_i by (25).
The weak closed-graph/Kaplansky argument of Yin_C_F0027 now applies to the dense star algebra P_S and the two estimates just proved.
Explicitly, for x in M take a uniformly operator-norm-bounded net p_alpha in P_S tending to x in L2.
A weakly convergent subnet of the bounded F_i0 p_alpha values, together with weak closedness of the graph of T_i, puts x in Dom(T_i).
Repeating with F_i0* gives x in Dom(F_i0*).
The bounds extend to all M by weak lower semicontinuity.
Therefore
\[
M\subseteq\operatorname{Dom}T_i\cap\operatorname{Dom}F_{i0}^*.
\tag{26}
\]
This argument does not require P_S contained in P_X.
It only required the graph inclusion (25), which was obtained by explicit approximation.

For each p in the original P_X, (26) gives p in Dom(T_i).
Since T_i is contained in D_i, their values there agree, so
\[
T_i p=D_i p=D_{i0}p.
\]
Thus D_i0 is contained in T_i as a graph.
Taking closures and combining with T_i contained in D_i proves
\[
\overline{D_{i0}}=T_i=\overline{F_{i0}},
\qquad D_{i0}^*=F_{i0}^*.
\tag{27}
\]
Equations (26)-(27) prove (3) for the actual originally specified operators and actual adjoints.
The original generator identities extend to M by Yin_C_F0027's bounded-set weak continuity argument.
The resulting operator restrictions satisfy Yin_C_F0024, while Yin_C_F0025 provides its original polynomial weak-form interpretation and reverse implication.
The rational algebra throughout remains A_X.

## 7. Geometric Reach and Review Handoff

This permits an embedded analytic arc whose tangent rotates too far for any affine projection to be injective.
For example r(z)=exp((1/10+i)z) on I=[0,3pi/2] is injective on a thin complex rectangle around I: any nonzero period has real part of absolute value at least 2pi/(1+1/100), larger than the width of a suitable rectangle.
Its tangent argument along I varies through 3pi/2.
For any nonzero complex alpha, the derivative of Re(alpha r(t)) therefore takes both positive and negative values.
Such a projection is not monotone and hence not injective on I.
This logarithmic spiral arc is not a global real graph after an affine rotation, but satisfies the geometric hypothesis here.
This example distinguishes the geometric scopes; it does not assert the dual hypotheses for an unspecified tuple on that arc.

Whole circles, noninjective parametrizations, arcs with vanishing parametrization derivative, arbitrary planar spectra, and patchwise charts without a single holomorphic inverse are not established by this proof.
The new analytic input is exactly (4)-(5); the new operator-domain input is the construction of (25) before the two-core closure comparison.
In particular local charts were not silently identified with elements of the original polynomial algebra.

Author checks cover coarse closability, the starred approximants, finite product estimates, inherited vacuum adjoints, nonvanishing of the divided-difference multiplier, weighted adjoint convergence, both reconstruction estimates, restoration of normalization, and both graph inclusions in (27).
The candidate is ready for an independent full review.
No formal verification, numerical evidence, general-normal resolution, or novelty claim is made.


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
| argument | [Exact material](#3-the-closed-coarse-derivative-and-graph-approximation) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0072_v1.md#5-geometric-and-goal-boundaries) | Whole seven-section globally parametrized embedded analytic-arc theorem, Runge/coarse graph approximation, original closure/adjoint equality and geometric example. Actual original finding with unknown initial-context relationship; original date and accepted inputs preserved. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the new isolated independent finding only for Sections 1–6 and the original closure/adjoint theorem chain. Section 7 geometric example continues to rely on the complete original finding at its disclosed unknown relationship; it is not newly independently reviewed here. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#3-the-closed-coarse-derivative-and-graph-approximation) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0072_v1.md#current-isolated-finding) | Sections 1–6 only: exact analytic-arc hypotheses, Runge and coarse graph approximation, conjugate reconstruction, both original closure inclusions and actual adjoints. Section 7's logarithmic-spiral example is excluded from this independent finding and retains the original finding's support. |
| review | [Retained original geometric finding](../audits/reviews/Yin_R_F0072_v1.md#5-geometric-and-goal-boundaries) | Original Section 7 logarithmic-spiral example and geometric reach, retained at the original unknown relationship and date; this row supplies no new independent inspection of that example. |


### Decision isolated-complete-theorem-and-example-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:43 |
| status | proved |
| reason | Adopt the complete main theorem and the separately independently inspected geometric example at their distinct exact scopes; preserve the prior partial adoption, all historical decisions, accepted source depths and conditional geometric limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact retained material](#3-the-closed-coarse-derivative-and-graph-approximation) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Complete Sections1–6 independent finding](../audits/reviews/Yin_R_F0072_v1.md#current-isolated-finding) | Exact analytic-univalent-arc hypotheses, closed coarse graph approximation, conjugate reconstruction, both original closure inclusions and actual adjoints; the complete main-theorem initial judgment preceded the old R35 account as recorded in this finding. |
| review | [Complete Section7 independent example finding](../audits/reviews/Yin_R_F0071_v1.md#isolated-spiral-example-finding) | Exact logarithmic-spiral univalence rectangle, nonzero derivative and noninjectivity of every affine real projection, with its conditional tuple/dual interpretation and geometric exclusions; complete initial2026-10-22T22:34 before the old R35 example finding. |

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
| argument | [Exact material](#3-the-closed-coarse-derivative-and-graph-approximation) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0072_v1.md#5-geometric-and-goal-boundaries) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0072_v1.md#5-geometric-and-goal-boundaries).

Material covered by that review: [Exact material](Yin_C_F0042_v1.md).

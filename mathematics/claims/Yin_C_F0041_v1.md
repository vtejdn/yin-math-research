---
author: Yin
---

# Analytic spectral graphs restore both original all-M domains from bare polynomial-core duals

## Current assessment
[Selected decision](#decision-isolated-current-review-20261022)

## Analytic Spectral Graphs from the Bare Polynomial Domain

<a id="statement"></a>

Record kind: complete proof and substantive extension of Yin_C_F0040.
Date: 2026-09-11.
Human author: Yin.
Proof development: root.
Goal: the separate normal-domain investigation.
Registered as ordinary Claim Yin_C_F0041 after [independent review](../audits/reviews/Yin_R_F0074_v1.md#outcome-and-limits); no mathematical Role is assigned.
Provenance: project deduction using the accepted inputs below, without a novelty assertion.
The prior [Yin_C_F0040 proof](Yin_C_F0040_v1.md#yin_c_f0040) remains unchanged.

<a id="yin_c_f0041"></a>
## 1. Exact statement and dependence on the previous argument

Use Yin_C_F0025's exact compact polynomial-core hypotheses in a finite faithful tracial von Neumann algebra (M,tau), with H=L2(M), Omega=1, and inner product linear in the second argument.
A bounded normal tuple X generates M.
Write

\[
\mathcal P_X=\mathbb C\langle X,X^*\rangle,
\qquad \mathcal A_X=\mathbb C\langle X\rangle.
\]

For each i an operator D_i0 has domain P_X Omega, with

\[
\Omega\in\operatorname{Dom}D_{i0}^*,\quad
[D_{i0},X_j]=\delta_{ij}P_\Omega,\quad
[D_{i0},X_j^*]\text{ extending to a compact bounded operator}.
\tag{1}
\]

Assume additionally

\[
X_i=S_i+\mathrm i g_i(S_i),\qquad S_i=S_i^*,
\tag{2}
\]

where g_i is real-valued on a nondegenerate compact real interval I_i containing sigma(S_i), and extends holomorphically to an open neighborhood of I_i.
There is no smallness or freeness assumption.
Intervals can be enlarged slightly inside that neighborhood when useful.

**Conclusion.**
For the originally given operators,

\[
M\subseteq\operatorname{Dom}\overline{D_{i0}}
\cap\operatorname{Dom}D_{i0}^*.
\tag{3}
\]

The full affiliated-fraction criterion of Yin_C_F0024 then applies to these actual closures, with the original unstarred algebra A_X.
In particular, for every bounded f in M, membership in Div_{L0(M)} A_X is equivalent to bounded finite-rank representatives of all Yin_C_F0025 polynomial weak commutator forms.

The point requiring a new proof is that P_S=C<S> is contained in P_X, because S_i=Re(X_i), but need not equal it when g_i is not polynomial.
We first restore both domains for the restriction to P_S and then prove that its closure is exactly the closure of the original operator on the larger core.
We do not assert that S_i belongs to the unstarred rational algebra of X.

Inputs already checked before this proof: Yin_C_F0025's spectral phase and polynomial adjoint formulas; Yin_C_F0040 Sections 3.1-3.3 for inner multipliers and reconstruction; Dab10-U002 for the selfadjoint finite-Fisher contractions and both actual domain estimates; Yin_C_F0027 Section 5 for weak closed graphs and Kaplansky density.
The additional accepted approximation input is [Tre17-U001](../audits/literature/Tre17/Yin_U001.md#tre17-u001), Lemma 5.1.
No bounded matrix-inverse representation is inferred from a bounded affiliated output.

## 2. Restrict to the auxiliary selfadjoint polynomial algebra

Initially normalize D_i0 by subtracting p maps to p D_i0(Omega), as in Yin_C_F0025.
Both the normalized core operator and its original counterpart are closable by the polynomial-adjoint argument there.
The normalization is restored in Section 5.

The normal spectral rigidity in Yin_C_F0025 supplies coarse derivations partial_i on P_X, with

\[
\partial_iX_j=\delta_{ij}1\otimes1,\quad
1\otimes1\in\operatorname{Dom}\partial_i^*,\quad
D_{i0}=(\mathrm{id}\otimes\tau)\partial_i.
\tag{4}
\]

Here partial_i* in (4) initially refers to P_X.
Restrict partial_i and D_i0 to P_S and write F_i0=D_i0|P_S.
Since every X_i is a function of S_i and S_i is in P_X, W*(S)=M.
Thus P_S is dense in H, and all restricted adjoints are ordinary single-valued Hilbert adjoints.

Set

\[
h_i(s,t)=g_i^{[1]}(s,t),\quad
J_i(s,t)=1+\mathrm i h_i(s,t),\quad K_i=J_i^{-1}.
\tag{5}
\]

The divided difference is holomorphic across its diagonal.
It is real on I_i squared, so |J_i|>=1 there and J_i and K_i are holomorphic on some complex neighborhood of that square.
Yin_C_F0025's normal phase gives

\[
\partial_i S_j=\delta_{ij}K_i(S_i\otimes1,1\otimes S_i).
\tag{6}
\]

The diagonal is null by the already established atomlessness; defining the kernel there by continuity also gives the same tensor vector.
In particular the Hilbert tensor norm of K_i is at most one.

For functions a,b of S_i, use the inner bimodule action

\[
I_{a\otimes b}(u\otimes v)=ua\otimes bv.
\tag{7}
\]

The two inner spectral actions commute.
Each I_Ji is bounded and commutes with the outer M-bimodule actions.
Therefore

\[
\delta_i=I_{J_i}\partial_i|_{\mathcal P_S}
\tag{8}
\]

is a derivation with delta_i(S_j)=delta_ij 1 tensor 1.
It is the ordinary evaluated free difference quotient on the selfadjoint tuple S.
The next step proves its vacuum-adjoint condition, rather than assuming that an arbitrary bounded multiplier preserves an adjoint domain.

## 3. The analytic multiplier lies in the required adjoint domain

Fix i and write I_i=[a,b].
Let

\[
t_n(s)=T_n\!\left(\frac{2s-a-b}{b-a}\right).
\]

On I_i, ||t_n||_infinity<=1 and ||t_n'||_infinity<=2n^2/(b-a).
The latter follows from T_n'=n U_{n-1} and |sin(n theta)/sin(theta)|<=n, including endpoint limits; n=0 gives derivative zero.

For any polynomial v in one variable, (6) and the product rule give

\[
\partial_i v(S_i)=v^{[1]}(S_i\otimes1,1\otimes S_i)K_i,
\quad
\|\partial_i v(S_i)\|_2
\le\|v'\|_{\infty,I_i}\|K_i\|_2.
\tag{9}
\]

These are commuting two-variable spectral multipliers on the tensor vector; no noncommutative operator-Lipschitz estimate is assumed.
Thus the derivative norms of t_n(S_i), and of their adjoints, grow at most quadratically in n.

Write partial for the restriction partial_i|P_S and xi=partial*(1 tensor 1), which exists by (4).
The polynomial-tensor adjoint estimate already proved in Yin_C_F0040 Section 3.2 reads

\[
\|\partial^*(u\otimes v)\|_2
\le \|u\|\|v\|\|\xi\|_2
 +\|\partial(u^*)\|_2\|v\|
 +\|u\|\|\partial(v^*)\|_2,
\qquad u,v\in\mathcal P_S.
\tag{10}
\]

It follows by expanding partial(u* p v*) against the vacuum tensor and bounding the other two Leibniz terms; it does not assume reality of partial.
Consequently

\[
\|\partial^*(t_m(S_i)\otimes t_n(S_i))\|_2
\le C_i(1+m^2+n^2).
\tag{11}
\]

Tre17 Lemma 5.1, after affine rescaling and selection of two Bernstein ellipses sufficiently close to the interval, supplies

\[
J_i(s,t)=\sum_{m,n\ge0}c_{mn}t_m(s)t_n(t),\qquad
\sum_{m,n}|c_{mn}|(1+m^2+n^2)<\infty.
\tag{12}
\]

Indeed the coefficients decay geometrically in m+n on a smaller fixed polyellipse; the polynomial weight is summable against that decay.
This uses only a neighborhood of the compact square, not the stronger isotropic assumption in Tre17's main theorem.

The polynomial partial sums for I_Ji*(1 tensor 1) converge in H tensor_2 H; by (11)-(12) their partial*-images converge absolutely in H.
Since partial* is closed,

\[
I_{J_i}^*(1\otimes1)\in\operatorname{Dom}\partial^*.
\tag{13}
\]

Conjugating the coefficients in (12) causes no change to the estimates because the t_n are real on I_i.
Therefore zeta_i=partial* I_Ji*(1 tensor 1) is an L2 conjugate variable for S.
This establishes the selfadjoint finite-Fisher hypothesis on the smaller polynomial algebra, without putting g_i(S_i) into that algebra.

## 4. Both estimates for the restricted original dual

Let E_i be the closure of (id tensor tau) delta_i.
The accepted Dab10-U002/Yin_C_F0040 interface gives actual domains and constants

\[
M\subseteq\operatorname{Dom}E_i\cap\operatorname{Dom}E_i^*,\qquad
\|E_i x\|_2\le c_i\|x\|,\quad
\|E_i^*x\|_2\le c_i'\|x\|\quad(x\in M).
\tag{14}
\]

For example c_i=4||zeta_i||_2 and c_i'=5||zeta_i||_2 are sufficient with the retained source convention.

The same analytic coefficient input applied to K_i gives a projective expansion

\[
K_i(s,t)=\sum_r a_r(s)b_r(t),\qquad
L_i=\sum_r\|a_r\|\|b_r\|<\infty.
\tag{15}
\]

These factors may be taken as scalar multiples of the t_n polynomials; only boundedness is needed after (14).
The inner maps satisfy I_Ki I_Ji=I, so partial_i|P_S=I_Ki delta_i.

The operator identity Theta(I_(a tensor b)v)=rho(a)Theta(v)rho(b), with rho(a)xi=xi a, now gives exactly the Yin_C_F0040 reconstruction on p in P_S:

\[
F_{i0}p=\sum_r\bigl(E_i(p b_r)-pE_i(b_r)\bigr)a_r,
\qquad \|F_{i0}p\|_2\le2c_iL_i\|p\|.
\tag{16}
\]

All inputs of E_i in this sum are bounded and hence in its actual domain.
Its polynomial commutators extend to the whole closed domain; convergence of (15) is in projective norm and hence in the required Hilbert-Schmidt pairing.

The adjoint here must be that of the restricted operator F_i0, not silently the adjoint of D_i0.
Its polynomial adjoint formula follows from the bounded polynomial commutators and the inherited vacuum adjoint.
Put xi_i=F_i0* Omega and T_(p*)=Theta(partial_i(p*)).
Then

\[
F_{i0}^*p=p\xi_i-T_{p^*}^*\Omega,
\quad
T_{p^*}^*\Omega
=\sum_r\bigl(pE_i^*(a_r^*)-E_i^*(p a_r^*)\bigr)b_r^*.
\tag{17}
\]

The adjoint sign is [E_i,p*]*=-[E_i*,p], and the order of right factors is the one in Yin_C_F0040.
Thus separately

\[
\|F_{i0}^*p\|_2
\le(\|\xi_i\|_2+2c_i'L_i)\|p\|.
\tag{18}
\]

Adding back the original right-multiplication term p eta_i contributes p eta_i* to this polynomial adjoint and at most ||eta_i||_2 ||p|| to each bound.
Equations (16) and (18) therefore hold with enlarged constants for the restrictions of the originally specified operators as well.

## 5. Return to the original larger core without identifying the algebras

Let F_i0 now denote the restriction of the original, possibly unnormalized D_i0 to P_S, and set T_i=closure(F_i0).
The Yin_C_F0027 weak-graph argument uses only that P_S is a weakly dense star algebra and that the two bounds just proved hold on it.
In detail, for x in M choose a uniformly operator-norm-bounded Kaplansky net p_alpha in P_S converging to x in L2.
Boundedness of F_i0 p_alpha gives a weakly convergent subnet; weak closedness of graph(T_i) puts x in Dom(T_i).
Repeating this with F_i0* and its bound puts x in Dom(F_i0*).
The weak lower norm bound retains the two infinity-to-2 estimates on all M.

Now let D_i=closure(D_i0) on the originally specified P_X.
The inclusion F_i0 subset D_i0 gives T_i subset D_i.
For p in P_X, we also have p in M subset Dom(T_i).
Since T_i and D_i agree on Dom(T_i),

\[
T_i p=D_i p=D_{i0}p.
\]

Thus D_i0 subset T_i as graphs.
Taking closures and combining the two graph inclusions proves

\[
\overline{D_{i0}}=T_i=\overline{D_{i0}|_{\mathcal P_S}},\qquad
D_{i0}^*=F_{i0}^*.
\tag{19}
\]

This is the step that replaces the false equality P_X=P_S.
It uses closability of the original D_i0, already supplied by (1), and actual inclusion of M in the smaller graph domain.
It does not presume norm approximation inside an unspecified graph norm or that the larger core is an adjoint core.

Equation (19) proves (3) for the original operators and their actual adjoints.
Their original generator identities extend from P_X to M by the bounded-set weak continuity argument of Yin_C_F0027 Section 5.
Yin_C_F0024 now supplies the full affiliated-fraction criterion, and Yin_C_F0025 supplies the reverse weak-form implication.
No change to A_X has occurred.

## 6. Scope and review handoff

This covers every coordinatewise real-analytic spectral graph in (2), including nonpolynomial g_i and arbitrary real coefficients in the earlier polynomial case.
Nondegenerate coordinatewise complex affine changes are permitted with the corresponding dual rescaling.
It does not cover every embedded analytic arc: a global graph after affine rotation is an additional geometric premise.
Full-circle cores, arbitrary planar spectra and arbitrary dense left-module domains remain separate questions.

The two new obligations resolved by this candidate are weighted analytic convergence inside the restricted derivation-adjoint domain, and equality of the two actual operator closures despite different polynomial algebras.
Yin_C_F0040 is a proof source, not extraction provenance for newly registered lemmas; no lemma extraction or theorem Role is performed.

Author checks cover the compact-core normal phase, the change of restricted adjoint, the Chebyshev derivative weight, analytic nonvanishing of J, convergence under the closed adjoint, both infinity-to-2 estimates, unnormalized duals and both graph inclusions in (19).
Independent complete review is required before registration.
No numerical experiment, formal verification, or novelty claim is made.


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
| argument | [Exact material](#2-restrict-to-the-auxiliary-selfadjoint-polynomial-algebra) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0074_v1.md#outcome-and-limits) | Whole six-section analytic real-graph theorem, new restricted-adjoint approximation, two original-closure inclusions and exact unstarred criterion. Actual original finding with unknown initial-context relationship; original date and accepted inputs preserved. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the separate isolated current finding on the unchanged fixed statement and proof, with exact conditions and scope. Preserve historical findings, relationships, source depths and dates; no new mathematical proof version is introduced. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-restrict-to-the-auxiliary-selfadjoint-polynomial-algebra) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0074_v1.md#current-isolated-finding) | Whole six-section analytic real-graph theorem, new restricted-adjoint approximation, two original-closure inclusions and exact unstarred criterion. |

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
| argument | [Exact material](#2-restrict-to-the-auxiliary-selfadjoint-polynomial-algebra) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0074_v1.md#outcome-and-limits) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0074_v1.md#outcome-and-limits).

Material covered by that review: [Exact material](Yin_C_F0041_v1.md).

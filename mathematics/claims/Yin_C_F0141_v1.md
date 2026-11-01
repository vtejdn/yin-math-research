---
author: Yin
---
# Actual ACSY vacua restore both domains for polynomial linear coordinate changes

Human author: Yin.
The acsy_to_full_domain agent developed the represented-relation argument, weighted target-core approximation and canonical-domain restoration.
Root supplied the pseudoinverse observation eliminating an unnecessary Hilbert-space injectivity premise and requested explicit identification of the h-coordinate canonical core.
This complete candidate has not yet received independent review.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let (M,tau) be finite with faithful normal probability trace, H=L2(M,tau), Omega=1, P=P_Omega.
Let h,S be bounded selfadjoint generators with a joint L2 conjugate system xi_h,xi_S.
Write A_0=C<h,S>, and let partial_h,partial_S be the represented selfadjoint free difference quotients.

Let
\[
 F(s,t)=\sum_{j=1}^m a_j(s)b_j(t)
\]
be a complex polynomial, with scalar polynomial factors a_j,b_j, and set
\[
 Y=\sum_{j=1}^m a_j(h)S b_j(h),\qquad
 X=(h,Y),\qquad A_X=\mathbb C\langle h,Y,Y^*\rangle.
 \tag{1}
\]
Let mu be the spectral law of h.
Assume explicitly that
\[
 W^*(h,Y)=M,\qquad
 F(s,t)\ne0\quad\hbox{for }(\mu\otimes\mu)\hbox{-almost every }(s,t).
 \tag{2}
\]

Suppose A(X): on A_X there are outer Hilbert-space-tensor derivations delta_h,delta_Y with
\[
 \delta_h h=1\otimes1,\quad\delta_hY=0,\qquad
 \delta_Yh=0,\quad\delta_YY=1\otimes1,
\]
and both actual vacuum-adjoint vectors belong to H.

Then their canonical contractions
\[
 Q_h=(\mathrm{id}\otimes\tau)\delta_h,\qquad
 Q_Y=(\mathrm{id}\otimes\tau)\delta_Y
\]
are closable and satisfy
\[
 M\Omega\subseteq
 \operatorname{Dom}\overline{Q_i}
 \cap\operatorname{Dom}Q_i^*
 \quad(i=h,Y).
 \tag{3}
\]
Their closures have the original operator-first coordinate commutators on all M Omega; negating them gives the generator-first condition S(X), and therefore F(X).

Here S means existence of densely defined duals with both actual domains containing M Omega, whereas F means existence of arbitrary linear full-M duals without an adjoint-domain premise.
No converse F-to-A or general nonnormal equivalence is asserted.

If v=delta_Y*(1 tensor 1), then
\[
 \|\overline{Q_Y}a\|_2\le4\|v\|_2\|a\|,\qquad
 \|Q_Y^*a\|_2\le5\|v\|_2\|a\|,
 \qquad a\in M.
 \tag{4}
\]
The assumptions do not require 1/F to belong to L2(mu tensor mu).
They also do not require the multiplier F(L_h,R_h) on H to be injective.
The given target derivations are unique at their prescribed generator values under (2).

## Argument

### 1. Exact reference interfaces and the two coefficient actions

The original selfadjoint pair supplies the specified closures
\[
 E=\overline{(\mathrm{id}\otimes\tau)\partial_S},\qquad
 B_h=\overline{(\mathrm{id}\otimes\tau)\partial_h},
\]
with both actual M domains and operator-norm-to-L2 bounds, by [Dab10-U002, Sections 1-3](../audits/literature/Dab10/Yin_U002.md#dab10-u002).
In particular [B_h,h]=P on M and [B_h,Y]=Theta(partial_hY) there.

For a finite tensor beta=sum c_l tensor d_l in C[h] tensor C[h], [C_F0139, finite-coefficient part](Yin_C_F0139_v1.md#statement) supplies the represented derivation I_beta partial_S and its contraction T_beta, with
\[
 v_\beta=\sum_l c_l^*\xi_Sd_l^*,\qquad
 \|T_\beta p\|_2,\ \|T_{\beta^\#}p\|_2
 \le4\|v_\beta\|_2\|p\|,
 \tag{5}
\]
and the actual core adjoint
\[
 T_\beta^*q=qv_\beta-T_{\beta^\#}q.
 \tag{6}
\]
Here beta# is flip-star and v_(beta#)=v_beta*.
Only this finite-coefficient theorem is used below.
Its measurable-coefficient conclusion, which requires beta itself to be coarse L2, is not being applied.

Distinguish the inner action
\[
 I_F(u\otimes w)=\sum_j u a_j(h)\otimes b_j(h)w
\]
from the outer action
\[
 J_F(u\otimes w)=\sum_j a_j(h)u\otimes w b_j(h).
 \tag{7}
\]
Both are bounded, and I_F commutes with the outer bimodule actions.
They agree on the marginal subspace L2(W*(h)) bar tensor L2(W*(h)), where both are scalar multiplication by F.

The universal Hilbert--Schmidt identification is Theta(u tensor w)(a)=u tau(wa).
Its unitary extension, outer compatibility and Theta(zeta)1=(id tensor tau)zeta are the exact interfaces recorded in [C_F0070](Yin_C_F0070_v1.md#statement-and-interfaces).
No normal-coordinate theorem from that material is imported.

### 2. The represented star relation fixes the starred derivative

Put F#(s,t)=overline{F(t,s)}.
Define the bounded two-sided maps on M
\[
 {\cal L}_F(a)=\sum_j a_j(h)a b_j(h),\qquad
 {\cal L}_{F^\#}(a)=\sum_j b_j(h)^*a a_j(h)^* .
\]
They commute because all coefficients are functions of the same selfadjoint h.
Since Y=L_F(S) and Y*=L_(F#)(S), the represented relation
\[
 {\cal L}_F(Y^*)={\cal L}_{F^\#}(Y)
 \tag{8}
\]
holds.

Apply the target Y-derivation.
It vanishes on all polynomial coefficients in h, so
\[
 J_F\,\delta_Y(Y^*)=F^\#.
 \tag{9}
\]
The right side is its marginal Hilbert tensor.

The operator J_F is injective on the entire coarse Hilbert space.
Indeed mu(B)=0 implies the spectral projection 1_B(h)=0 by faithfulness.
Every spectral measure of h on H is therefore absolutely continuous with respect to mu.
On elementary coarse vectors the joint outer spectral measure is a product of two such measures, and the kernel projection of J_F kills each elementary vector by (2).
Density proves injectivity.

The conditional-expectation projection onto L2(W*(h)) is a W*(h)-bimodule map.
Its tensor square commutes with J_F and fixes F#.
Injectivity in (9) then implies that delta_Y(Y*) lies in the marginal tensor subspace.
Consequently
\[
 \delta_Y(Y^*)=k,\qquad
 k(s,t)=F^\#(s,t)/F(s,t)\in L^2(\mu\otimes\mu).
 \tag{10}
\]

The derivations I_F delta_Y and partial_S agree on h,Y,Y*: their values are respectively zero,F,F#.
Thus
\[
 \partial_S|_{A_X}=I_F\delta_Y.
 \tag{11}
\]

The same represented relation proves uniqueness at either set of coordinate values.
The difference epsilon of two such derivations vanishes on h and Y.
Applying it to (8) gives J_F epsilon(Y*)=0, hence epsilon(Y*)=0.
The three generators of A_X then determine epsilon=0.

### 3. The actual vacuum supplies the missing spectral graph norm

Let v=delta_Y*(1 tensor 1).
Since delta_Y vanishes on polynomial functions of h, the Leibniz rule and actual vacuum pairing give
\[
 \delta_Y^*(a_j(h)^*\otimes b_j(h)^*)
       =a_j(h)^*v b_j(h)^*.
\]
Pair (11) against 1 tensor 1 and use density of A_X from (2).
This yields
\[
 \xi_S=\overline F(L_h,R_h)v.
 \tag{12}
\]
Here L_h,R_h are commuting bounded selfadjoint operators on H; overline F is the pointwise complex conjugate function.

Let nu_xi be their finite joint spectral vector measure at xi_S.
Define beta=1/F off the zero set of F and beta=0 on that set.
The bounded normal operator B=overline F(L_h,R_h) may have a kernel.
Equation (12) nevertheless implies that xi_S has zero joint spectral mass on F=0, and closed joint spectral calculus gives
\[
 v_{\min}:=\overline\beta(L_h,R_h)\xi_S
 =1_{\{F\ne0\}}(L_h,R_h)v,\qquad
 \|v_{\min}\|_2\le\|v\|_2 .
 \tag{13}
\]
In particular beta is in L2(nu_xi).
No injectivity of B is inferred from its different coarse representation.

Define the finite positive measure
\[
 \lambda=(|F|^2+|F^\#|^2)(\mu\otimes\mu)+\nu_{\xi}.
 \tag{14}
\]
Equations (2), (10) and (13) say precisely that beta belongs to L2(lambda): the three squared integrals are 1, ||k||2^2 and ||v_min||2^2.
On the compact real spectral square, scalar polynomials in s,t are dense in L2(lambda).
Choose finite polynomial tensors beta_n converging to beta there.
Then
\[
 F\beta_n\to1,\qquad F^\#\beta_n\to k
 \quad\hbox{in coarse }L^2,\qquad
 v_n:=\overline{\beta_n}(L_h,R_h)\xi_S\to v_{\min}
 \quad\hbox{in }H.
 \tag{15}
\]
No assertion that beta_n itself converges in coarse L2 is needed.

### 4. Target-core convergence restores the Y contraction and its adjoint

Let delta_n=I_(beta_n)partial_S on A_0.
Restricted to A_X, its values on h,Y,Y* are respectively 0,F beta_n,F# beta_n.
By (15), these converge to the prescribed values of delta_Y.
The Leibniz rule on each fixed target word, with bounded outer factors, gives
\[
 \delta_n(p)\longrightarrow\delta_Y(p)
 \quad\hbox{in }H\bar\otimes H,\qquad p\in A_X.
 \tag{16}
\]
The actual vacuum vectors of delta_n are v_n.
Passing to the limit in their vacuum pairings shows that v_min is an actual vacuum for delta_Y.
Density gives
\[
 v_{\min}=v.
 \tag{17}
\]
Thus the apparent kernel component in (12) is eliminated by target-core convergence, rather than by an injectivity assumption on H.

Let delta_Y#(p)=(delta_Y(p*)) dagger, with dagger the coarse flip-star.
For each n, the same operation sends delta_n to the derivation with coefficient beta_n#.
Equation (16) at p* therefore gives convergence of these conjugate derivations on every p in A_X; their vacua v_n* converge to v*.

Put F_0=(id tensor tau)delta_Y# on A_X.
Passing to the limit in (5) yields
\[
 \|Q_Yp\|_2,\ \|F_0p\|_2\le4\|v\|_2\|p\|.
\]
For fixed p,q in A_X, pass to the limit in the actual adjoint pairings (6).
This proves actual core-adjoint membership and formula
\[
 Q_Y^*q=qv-F_0q,\qquad
 \|Q_Y^*q\|_2\le5\|v\|_2\|q\|.
 \tag{18}
\]
In particular Q_Y is closable.

Take uniformly bounded Kaplansky approximants from the target star algebra A_X for any a in M.
The two bounds and weak closed graphs place a in the domains of K=overline{Q_Y} and K*=Q_Y*, with (4).
Applying the same graph argument to hp_n and Yp_n passes the canonical commutators to M:
\[
 [K,h]=0,\qquad [K,Y]=P.
 \tag{19}
\]
For later use, the identical argument at every fixed p in A_X gives
\[
 [K,p](a)=\Theta(\delta_Yp)(a),\qquad a\in M.
 \tag{20}
\]
The Hilbert--Schmidt right side is a bounded operator, so this graph passage is legitimate for arbitrary bounded a.

### 5. The h correction is the given canonical core

Let
\[
 C=\partial_hY=\sum_{\ell=1}^r c_\ell\otimes d_\ell
 \quad(c_\ell,d_\ell\in A_0).
\]
This finite tensor need not have its factors in A_X, but all factors are bounded elements of M.
The map
\[
 \theta_h=\partial_h|_{A_X}-I_C\delta_Y
\]
is a Hilbert-valued represented outer derivation on A_X.
It takes h to 1 tensor 1 and Y to zero.
By the uniqueness proved after (11),
\[
 \theta_h=\delta_h.
 \tag{21}
\]
Thus no change of the supplied h-coordinate canonical core is hidden in the correction.

Define on M
\[
 {\cal Q}_C(K)(a)=\sum_\ell K(a d_\ell)c_\ell,\qquad
 \eta={\cal Q}_C(K)(1)=\sum_\ell K(d_\ell)c_\ell,\qquad
 \widetilde Q_h=B_h-{\cal Q}_C(K)+\rho(\eta).
 \tag{22}
\]
Right multiplication by the H vector eta is restricted to the domain M.
All terms are genuine H values, and each map is bounded from M with its operator norm to H.

Equation (20), applied at d_ell in M, gives
\[
 (\mathrm{id}\otimes\tau)I_C\delta_Y(p)
 =\sum_\ell\Theta(\delta_Yp)(d_\ell)c_\ell
 ={\cal Q}_C(K)(p)-p\eta,\qquad p\in A_X.
\]
The trace equality tau(d_ell w)=tau(w d_ell) fixes the inner coefficient order.
Together with (21), this proves that \widetilde Q_h restricts to the original Q_h on A_X.

Every q in M belongs to the actual adjoint domain of the domain-M map \widetilde Q_h, with
\[
 \widetilde Q_h^*q
 =B_h^*q-\sum_\ell(K^*(q c_\ell^*))d_\ell^*
       +q\eta^* .
 \tag{23}
\]
All products are in H by the already established full domains of K,K* and the reference B_h,B_h*.
The finite coefficient norm bounds also give a uniform operator-norm-to-L2 bound for Q_h on its core.
Hence Q_h is closable; its closure contains M by the Kaplansky weak-graph argument, while its actual adjoint contains M by (23).
This proves its part of (3).

Finally [B_h,Y]=Theta(C) and [Q_C(K),Y]=Q_C(P)=Theta(C) on M.
Also [Q_C(K),h]=0, while rho(eta) commutes with all left multipliers on M.
Thus the corrected closure satisfies
\[
 [\overline{Q_h},h]=P,\qquad
 [\overline{Q_h},Y]=0
 \quad\hbox{on }M.
\]
The original core commutators also pass directly by its uniform bound and closed graph.
Together with (19), negating the two canonical closures gives S(X).

## Scope

The proof uses only finite kernel-coefficient estimates, followed by convergence on the target star algebra.
It never asserts that 1/F is a Hilbert tensor on the original reference core.
The actual target vacuum controls the additional joint spectral norm needed for the approximation.

The generation and coarse nonvanishing assumptions in (2) remain part of the statement.
Coarse nonvanishing is automatic for a nonzero polynomial F and diffuse mu, but no such observation silently replaces those assumptions here.
The theorem treats polynomial expressions linear in the distinguished reference coordinate S, with coefficients depending on h.
It does not address a nonlinear inverse Jacobian involving S itself or an arbitrary A-only reference tuple.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T18:02 |
| status | open |
| reason | Complete target-core approximation proof of A-to-S for polynomial linear coordinate changes, with the supplied actual vacua, both canonical closures, full adjoint domains and explicit generation/coarse-nonvanishing hypotheses. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Canonical full-domain conclusion](#statement) | A-to-S-to-F, both supplied canonical closures and actual adjoints, the Y quantitative bounds and uniqueness at prescribed coordinate values. |
| argument | [Complete argument](#argument) | Five sections: represented star relation, minimal spectral inverse, three-measure target-core approximation, both Y domains and identification of the h canonical core. |
| dependency | [Selfadjoint reference contractions](../audits/literature/Dab10/Yin_U002.md#dab10-u002) | Represented difference quotients and specified B_h closure/adjoint on M with uniform bounds and canonical commutators. |
| dependency | [Finite kernel coefficient estimates](Yin_C_F0139_v1.md#statement) | Only finite coefficients, both 4-times contraction bounds, their actual vacuum and core adjoint identity. The coarse-L2 measurable theorem is not applied. |
| dependency | [Hilbert--Schmidt tensor interface](Yin_C_F0070_v1.md#statement-and-interfaces) | Only the universal tensor identification, outer compatibility and vacuum contraction, without normal-coordinate hypotheses. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T18:12 |
| status | proved |
| reason | Complete independent review verified the arbitrary supplied derivations, represented star relation, spectral pseudoinverse, three-measure target-core approximation, both canonical domains and the h correction without domain enlargement. No converse or unrestricted implication is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Canonical full-domain conclusion](#statement) | A-to-S-to-F, both supplied canonical closures and actual adjoints, the Y quantitative bounds and uniqueness at prescribed coordinate values. |
| argument | [Complete argument](#argument) | Five sections: represented star relation, minimal spectral inverse, three-measure target-core approximation, both Y domains and identification of the h canonical core. |
| dependency | [Selfadjoint reference contractions](../audits/literature/Dab10/Yin_U002.md#dab10-u002) | Represented difference quotients and specified B_h closure/adjoint on M with uniform bounds and canonical commutators. |
| dependency | [Finite kernel coefficient estimates](Yin_C_F0139_v1.md#statement) | Only finite coefficients, both 4-times contraction bounds, their actual vacuum and core adjoint identity. The coarse-L2 measurable theorem is not applied. |
| dependency | [Hilbert--Schmidt tensor interface](Yin_C_F0070_v1.md#statement-and-interfaces) | Only the universal tensor identification, outer compatibility and vacuum contraction, without normal-coordinate hypotheses. |
| review | [Independent complete review](../audits/reviews/Yin_R_F0148_v1.md#conclusion) | Entire fixed statement, all five proof sections, all three direct inputs, actual domains and the exact coordinate-class scope. |


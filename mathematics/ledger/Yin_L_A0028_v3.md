---
author: Yin
---
# Albert-form identification and a valuation limitation for the Promislow problem

This development serves [T_A0001](../tasks/Yin_T_A0001_v1.md#contract) through [route seven](../strategies/Yin_S_A0007.md).
Its fixed input is the actual rational descent calculation in [L_A0028_v2](../ledger/Yin_L_A0028_v2.md).
The question is whether the displayed global quadratic form can be proved anisotropic by passing to a valued extension.
The calculations below identify an explicit biquaternion Albert form and exclude a broad class of such valued-extension certificates.
They neither prove global anisotropy nor construct a rational isotropic vector over the original field.

## The exact quadratic form

Use algebraically independent U, V, T over the complex numbers, and put
\[
 L=\mathbb C(U,V,T),\qquad W=\frac{T^2}{UV},\qquad
 d=\frac{4(V-W)}{(1-V)(1-W)},\qquad e=\frac{4U}{1-U}.
\]
The form from L_A0028_v2 is
\[
 Q=d(H_1^2-UH_2^2)-U(R_1^2-VR_2^2)+e(S_1^2-WS_2^2).
 \tag{19}
\]
All displayed coefficients and denominators are nonzero in L.
The earlier fixed argument proves that anisotropy of Q over L is equivalent to excluding the complete mixed norm equation in the actual Promislow crossed product, and hence to its rational rank-divisibility conclusion.
That equivalence is an input here; none of the extensions below changes its original coefficient field.

## An explicit Albert-form identification

Let \((a,b)_L\) denote the quaternion algebra with generators i and j satisfying \(i^2=a\), \(j^2=b\), and \(ij=-ji\).
Form the biquaternion algebra
\[
 \mathcal B=(U,d)_L\otimes_L(UV,e)_L.
 \tag{20}
\]
Its Albert form, with the convention checked in [Lew06, Section 1.2, p. 47](../literature/pdf/Lew06.pdf#page=7), is
\[
 \phi_{\mathcal B}=\langle U,d,-Ud,-UV,-e,UV e\rangle.
\]
Write \(\iota\in\mathbb C\) for a fixed square root of minus one, to avoid confusing it with either quaternion generator.
The invertible L-linear substitution
\[
 (X_1,X_2,X_3,X_4,X_5,X_6)
 =\left(\iota R_1,H_1,H_2,\iota R_2,\iota S_1,
          \frac{\iota T}{UV}S_2\right)
 \tag{21}
\]
gives \(\phi_{\mathcal B}(X)=Q(H_1,H_2,R_1,R_2,S_1,S_2)\) term by term.
In particular, the last term becomes \(-eT^2S_2^2/(UV)=-eWS_2^2\).
Thus Q is an Albert form of the explicit algebra (20), rather than only a six-dimensional form analogous to one.
By the statement of Lew06, Theorem 6(1), which is an accepted external input here, Q is anisotropic if and only if \(\mathcal B\) is a division algebra.
The source statement, characteristic restriction and form convention have been checked; its original proof has not been re-audited.
This supplies another exact formulation of the remaining problem, not an independent proof of division.
No isomorphism between \(\mathcal B\) and the original crossed product is asserted solely from these equivalent division conditions.

## Every henselian valued extension with quadratically closed residue loses anisotropy

Let E contain L as a field, with a henselian valuation v and residue field k of characteristic different from two.
Assume every nonzero element of k is a square in k.
The valuation may have arbitrary rank and arbitrary ordered value group.
The only henselian property used is that a simple residue root of a monic polynomial lifts to a root in the valuation ring.
In particular, a valuation unit whose residue is a nonzero square has a square root in E.

Under these hypotheses Q is isotropic over E.
Here are explicit nonzero vectors for the three exhaustive cases.

If \(v(U)>0\), then \(1-U\) has residue one and therefore has a square root \(r\in E\).
Set
\[
 H_1=H_2=R_2=S_2=0,\qquad R_1=2,\qquad S_1=r.
\]
Then
\[
 Q=-4U+e(1-U)=0.
 \tag{22}
\]

If \(v(U)<0\), then \(1-U^{-1}\) has residue one and has a nonzero square root \(r\in E\).
Since
\[
 e=-\frac4{1-U^{-1}},
\]
the element \(E_0:=2\iota/r\) satisfies \(E_0^2=e\).
Set
\[
 H_1=H_2=R_1=S_1=0,\qquad
 R_2=\frac{TE_0}{UV},\qquad S_2=1.
\]
Then
\[
 Q=UV\frac{T^2e}{U^2V^2}-eW=0.
 \tag{23}
\]

If \(v(U)=0\), then U is a unit and its nonzero residue is a square by the residue-field hypothesis.
Lift a square root to \(r\in E\), so \(r^2=U\).
Set
\[
 H_1=r,\qquad H_2=1,\qquad R_1=R_2=S_1=S_2=0.
\]
Then
\[
 Q=d(r^2-U)=0.
 \tag{24}
\]
Every displayed vector has a coordinate equal to one or two, so it is nonzero.
No condition on the relative values of V, T or d is needed.
The argument includes a trivial valuation only when its residue-field hypothesis is met; it does not treat the original rational field as quadratically closed.

More generally, for a henselian valued extension without the square-residue assumption, the same proof still excludes anisotropy whenever \(v(U)\ne0\), or when \(v(U)=0\) and the residue of U is a square.
Consequently a valued-extension anisotropy proof must at least preserve U as a valuation unit with nonsquare residue.
This necessary condition is not a sufficient anisotropy criterion.

The square roots above cannot be silently replaced by rational functions in L.
Indeed, U is nonsquare by its valuation at U = 0, and \(1-U\) is nonsquare by its valuation at U = 1.
Also e is nonsquare, since its valuation at U = 0 is one.
All these discrete polynomial valuations of a nonzero square are even.
Thus the particular vectors (22)--(24) do not descend to L.
This proves a limitation of the valued-extension strategy, not isotropy over L and not failure of the actual group conjecture.

The first two formulas need no residue-field assumption at all and show that both the U-adic and the U-inverse-adic completion tests necessarily admit isotropic vectors.
For example, the required root in \(\mathbb C(V,T)((U))\) is the ordinary binomial series \((1-U)^{1/2}\).
At U inverse, use \((1-U^{-1})^{1/2}\) instead.
These explicit completions are different from the earlier y = 1 matrix lifting, but have the same critical limitation: a square root created by completion can destroy the rational obstruction.

## Source comparison for the actual virtually abelian algebra

The public arXiv v1 of [CG23](../literature/pdf/CG23--arxiv-v1.pdf) was obtained and checked against its title, authors and 24-page extent.
The inspected passages are Section 3.1, pp. 4--5, and Proposition 5.1 with its proof, pp. 10--11.
In Section 3.1 the authors first invoke Kropholler--Linnell--Moody's domain result for torsion-free virtually abelian groups, and then work with the resulting Ore division algebra.
Proposition 3.3 identifies that algebra with the actual division and regular closures over the complex numbers.
Proposition 5.1 describes the four-dimensional translation-field module and its sixteen-dimensional algebra over the fixed center in the Promislow case.
These are directly relevant known-coverage and presentation comparisons; their division premise is not used in (19)--(24).
The source therefore does not supply the independent exclusion of the mixed norm equation sought here merely by renaming its Ore field.
No full-paper audit or audit of its cited K-theoretic input is claimed.

## Remaining global question

The new identification makes the target explicit as division of (20), and the valuation calculation rules out certificates through every henselian valued extension satisfying the stated residue hypothesis.
The global form (19) remains unresolved by this argument.
A next valuation attempt must retain a nonsquare residue of U, and then independently control the other four coordinates rather than discard them.
Alternatively, a genuinely global rational argument must exclude all mixed norm solutions or all decomposable invariant bivectors from L_A0028_v2.
Known division coverage of the Promislow group remains comparison; no new group class or completion of T_A0001 is claimed.

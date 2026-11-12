---
author: Yin
---
# Coefficient potentials on the normal hopping defect

This argument serves [T_A0001](../tasks/Yin_T_A0001_v1.md#contract) and [S_A0006](../strategies/Yin_S_A0006.md).
The question is whether a coefficient-algebra potential that need not commute with normal homogeneous compressed hopping can remove its defect through an independently certified pivot.
The starting inputs are [C_A0008 v1](../claims/Yin_C_A0008_v1.md#argument), the [existing zero-defect criterion](../claims/Yin_C_A0005_v1.md#compressed-transport-certificate), and the [affiliated graded companion argument](../ledger/Yin_L_A0007_v1.md#a-companion-reduction-for-one-sided-graded-polynomials).
The coefficient-potential theorem retains the actual common hopping kernel and does not assume that its trace is an integer.

## Statement

Let \(\mathcal M\) be a finite von Neumann algebra with faithful normal finite trace \(\tau\), equipped with trace-preserving automorphisms \(\alpha_\theta\).
Let \(p\in\mathcal M\) be a projection fixed by every \(\alpha_\theta\), and let \(K\in p\mathcal Mp\) satisfy \(\alpha_\theta(K)=e^{i\theta}K\).
Assume that
\[
\delta:=P_{\ker(K|_p)}=P_{\ker(K^*|_p)}.
\tag{1}
\]
Normality of \(K\) suffices, but equality of these two kernels is the actual hypothesis used below.
Let \(V=V^*\in p\mathcal Mp\) be fixed by the action, with no commutation assumption between \(V\) and \(K\).
Define
\[
R:=K+K^*+V,\qquad D:=\delta V\delta|_\delta,\qquad
q:=P_{\ker(D|_\delta)},\qquad q_0:=\delta\wedge P_{\ker(V|_p)}.
\tag{2}
\]
Corner traces are not renormalized.
The conclusion is
\[
\boxed{\tau(q_0)\le \tau(P_{\ker(R|_p)})\le\tau(q).}
\tag{3}
\]
In particular:

- If \(D\) is injective, then \(P_{\ker(R|_p)}=0\).
  Only its actual affiliated inverse is needed; a bounded inverse is unnecessary.
- If \(V\ge0\) or \(V\le0\), then
  \[
  \boxed{P_{\ker(R|_p)}=\delta\wedge P_{\ker(V|_p)}=q.}
  \tag{4}
  \]
- More generally, (4) holds whenever \(Vq=0\), even if \(V\) is indefinite.

For an actual cyclic group extension and the height action, \(p\) and \(V\) are coefficient-algebra operators.
The projection \(\delta\) is fixed by the action, since multiplication of \(K\) by a nonzero scalar does not change its kernel.
It consequently lies in the coefficient algebra, as do \(q,q_0\).
No group torsion hypothesis, coefficient division-ring hypothesis or integer trace for these projections is needed in (3)--(4).

The finite-matrix consequence gives the complete kernels (13)--(15) under the independently specified Gram inverse hypothesis.
The finite-star potentials (16)--(21) remove the residual for every nonzero real parameter through a cyclically injective compression, including genuinely noncommuting examples.
The actual measurable example (22)--(23) shows that the common-kernel equality need not hold for an indefinite potential; it is outside the finite group-ring Task.

## Argument

### Affiliated rank proof

Write \(r:=p-\delta\).
Both \(K\delta\) and \(K^*\delta\) vanish, so \(K=rKr\).
On the \(r\)-corner its initial and final supports are both \(r\).
Finite-trace polar decomposition therefore makes \(K_r:=K|_r\) an actual unit in \(L^0(r\mathcal Mr)\), the algebra of closed densely defined affiliated operators.
It need not have a bounded inverse.
All products in that algebra below are the closed affiliated products.
If \(r=0\), (3) is the identity for \(R=V=D\); otherwise use the following block calculation relative to \(p=\delta+r\).

Put \(B:=\delta Vr\) and \(E:=rVr\).
The right multiplier
\[
L:=\begin{pmatrix}\delta&0\\0&(K_r^*)^{-1}\end{pmatrix}
\tag{5}
\]
is an independently known affiliated unit.
Its inverse is \(\operatorname{diag}(\delta,K_r^*)\).
The lower diagonal block of \(L\) has degree one.
Direct ordered multiplication gives
\[
RL=
\underbrace{\begin{pmatrix}D&0\\B^*&r\end{pmatrix}}_{A_0}
+
\underbrace{\begin{pmatrix}0&B(K_r^*)^{-1}\\0&E(K_r^*)^{-1}\end{pmatrix}}_{A_1}
+
\underbrace{\begin{pmatrix}0&0\\0&K_r(K_r^*)^{-1}\end{pmatrix}}_{A_2}.
\tag{6}
\]
The three summands have degrees zero, one and two.
The [singular constant-coefficient rank bound](../ledger/Yin_L_A0008_v1.md#a-unit-completion-instead-of-assuming-an-invertible-extreme-coefficient) applies in the finite algebra \(p\mathcal Mp\), after normalization of its trace if \(p\ne0\), and gives
\[
\operatorname{rk}(RL)\ge\operatorname{rk}(A_0).
\tag{7}
\]
Its proved unit-completion argument uses the relative inverse of \(A_0\) and support projections; it does not assume \(D\) invertible or a division coefficient algebra.
The degree-zero elementary unit
\[
\begin{pmatrix}\delta&0\\-B^*&r\end{pmatrix}
\]
on the right of \(A_0\) gives \(\operatorname{diag}(D,r)\).
Consequently
\[
\operatorname{rk}(R)=\operatorname{rk}(RL)
\ge \operatorname{rk}(D)+\tau(r)
=\tau(p)-\tau(q),
\tag{8}
\]
which proves the upper bound in (3).
The [affiliated rank-invariance argument](../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement) justifies the first equality without applying \(L^{-1}\) to arbitrary Hilbert-space vectors.
The lower bound follows from the actual bounded equations \(Kq_0=K^*q_0=Vq_0=0\).

If \(V\ge0\), the equality
\[
\langle Dx,x\rangle=\|V^{1/2}x\|^2\qquad(x\in\delta L^2(\mathcal M))
\tag{9}
\]
identifies \(\ker D\) exactly with \(\delta L^2(\mathcal M)\cap\ker V\).
Thus \(q=q_0\le P_{\ker R}\); equality of traces in (3) and faithfulness give the actual projection equality (4).
Apply the same reasoning to \(-V\) for the negative case.
If only \(Vq=0\) is assumed, then \(q\le P_{\ker R}\), and (3) again gives equality.
This is an exact kernel assertion, rather than a conclusion about an unspecified isomorphic module.

### The requested Schur pivot and the unbounded-domain boundary

Suppose \(D\) is injective.
Since \(D\) is selfadjoint in a finite corner, it has an actual affiliated inverse, whether or not it is bounded.
Eliminating the \(\delta\)-corner by elementary affiliated units gives the remaining operator
\[
S:=K_r+K_r^*+E-B^*D^{-1}B
\quad\hbox{in }L^0(r\mathcal Mr).
\tag{10}
\]
The effective coefficient \(E-B^*D^{-1}B\) is selfadjoint and fixed by the height action.
It can be unbounded.
More explicitly, the affiliated unit
\[
U:=\begin{pmatrix}\delta&-D^{-1}B\\0&r\end{pmatrix}
\]
satisfies \(U^*RU=\operatorname{diag}(D,S)\), by the ordered two-sided inverse identities for \(D\).
Multiplication on the right by \((K_r^*)^{-1}\) gives
\[
S(K_r^*)^{-1}
=r+(E-B^*D^{-1}B)(K_r^*)^{-1}
 +K_r(K_r^*)^{-1}.
\tag{11}
\]
This is a degree-zero, degree-one, degree-two polynomial whose constant term is the identity of its corner.
The [affiliated graded companion criterion](../ledger/Yin_L_A0007_v1.md#a-companion-reduction-for-one-sided-graded-polynomials) proves that (11), hence \(S\), is an affiliated unit.
The Schur elimination therefore proves that \(R\) is an affiliated unit.
It proves zero kernel of the original bounded \(R\); no domain-restricted kernel-vector substitution is needed.

The source of the graded criterion is the [domain-correct finite-eigenspace bound](../audits/literature/MSY23/Yin_U006.md#lemma-519-domain-repair).
Distinct eigenspaces of a closed affiliated operator have an injective bounded sum map, because actual eigenvectors belong to every power domain and the finite Vandermonde argument applies to them.
Polar decomposition bounds the sum of their traces.
A homogeneous nonzero eigenvalue orbit then has zero common trace.
The companion construction makes (11) a Schur complement of a homogeneous matrix shifted by its identity, using only triangular units and its already justified constant identity.
This is the existing graded argument at its actual affiliated scope, not an unbounded extension of the bounded graph recurrence by assertion.

When \(D^{-1}\) is bounded, (10) is a bounded Schur complement, but \(K_r^{-1}\) can still be unbounded.
The [bounded finite-layer proof](../claims/Yin_C_A0004_v3.md#height-layer-certificate) does not itself justify this case: its closed graph construction requires bounded outer inverses.
Equations (6)--(11) supply the valid affiliated alternative.
They also show that the proposed extension is already covered by the old graded and singular-coefficient mechanisms after retaining the normal hopping defect.
The additional useful interface is the coefficient compression \(D\), not a new general rank principle.

## Complete finite-matrix consequence

Let \(G=N\rtimes_\sigma\langle t\rangle\) and let \(A\in M_{m,d}(\mathcal N(N))\) be a bounded finite coefficient matrix with complete kernel projection \(p\).
Put \(B_A:=A^*A\), and use the unnormalized matrix traces.
Assume independently that \(B_A\) has a bounded inverse on \(1-p\).
Let \(X:=p+(B_A|_{1-p})^{-1}\), understood as a bounded block operator on \(p+(1-p)\).
Then \(B_AX=XB_A=1-p\) and \(pX=Xp=p\).
The explicit finite star and polynomial \(X\) in [C_A0008, (8)--(11)](../claims/Yin_C_A0008_v1.md#gram-and-normalization-units-before-using-the-residual) satisfy these premises with no new inverse.

Write \(T:=(t+t^{-1})I\), let \(\Psi=\Psi^*\) be a bounded coefficient matrix, and suppose \(K:=ptp|_p\) satisfies (1).
Use \(V:=p\Psi p|_p\) in the theorem and set
\[
\mathcal H_\Psi:=
\begin{pmatrix}T+\Psi&B_A\\B_A&0\end{pmatrix}.
\tag{12}
\]
If \(\delta V\delta\) is injective, then the complete kernel is
\[
\boxed{P_{\ker\mathcal H_\Psi}
=\begin{pmatrix}0&0\\0&p\end{pmatrix},
\qquad \dim_G\ker\mathcal H_\Psi=(\operatorname{Tr}_d\otimes\tau_G)(p).}
\tag{13}
\]
Indeed the lower equation forces \(x=px\), the compressed upper equation gives \(Rx=0\), and hence \(x=0\) and \(y=py\).
This is an actual bounded kernel calculation after the residual injectivity has been proved.

If instead \(V\ge0\) or \(V\le0\), put
\[
k:=\delta\wedge P_{\ker(V|_p)},\qquad S_0:=T+\Psi.
\]
Formula (4) gives the complete bounded parametrization
\[
\ker\mathcal H_\Psi
=\left\{\binom{x}{-XS_0x+z}:
x\in k\ell^2(G)^d,\ z\in p\ell^2(G)^d\right\}.
\tag{14}
\]
The inverse reads \(x\) and the lower \(p\)-coordinate.
Since \(pS_0k=0\), the two graph summands are orthogonal.
In particular, with
\[
F_k:=\binom{k}{-XS_0k},\qquad
D_k:=F_k^*F_k=k+kS_0X^2S_0k\ge k,
\]
the exact orthogonal projection is
\[
\boxed{P_{\ker\mathcal H_\Psi}
=F_k(D_k)^{-1}_kF_k^*
 +\begin{pmatrix}0&0\\0&p\end{pmatrix},\qquad
\dim_G\ker\mathcal H_\Psi=(\operatorname{Tr}_d\otimes\tau_G)(p)
+(\operatorname{Tr}_d\otimes\tau_G)(k).}
\tag{15}
\]
The inverse is bounded on the \(k\)-corner, and the first term is zero when \(k=0\).
Every map in (14)--(15) is bounded; no affiliated Schur inverse is substituted into a Hilbert-space parametrization.

## An actual noncommuting finite-star potential

Let \(H\) be an arbitrary torsion-free group and \(u,v\in H\), allowing equality and identity values.
Keep the complete finite construction of C_A0008:
\[
c:=1+u+v,\qquad C:=c^*c/9,\qquad
N:=H*F(z_1,\ldots,z_6),\qquad G:=N\rtimes_\sigma\langle t\rangle.
\]
Here \(\sigma(z_j)=z_jw_j\), with the six ordered \(w_j\) specified there.
To distinguish the old frame from the new potential, write \(F\) for the nine-by-one isometric frame called \(V\) in C_A0008.
Thus \(p=FF^*\), \(F^*KF=Ct\), and
\[
e:=P_{\ker_H c},\qquad \delta=FeF^*.
\]
Choose any index \(j\), put \(z:=z_j\), and define
\[
W:=(1-z)^*(1-z)=2-z-z^{-1},\qquad
\Psi_\lambda:=\lambda FWF^*,\qquad \lambda\in\mathbb R.
\tag{16}
\]
These are actual finite coefficient group-ring matrices.
The element \(z\) has infinite order, and the bilateral-shift argument proves \(\ker(1-z)=0\), hence \(\ker W=0\), independently of \(c\).
The inverse of \(W\) is affiliated and unbounded; its cyclic Fourier multiplier vanishes at \(1\) but on a Haar-null set.
For every nonzero \(\lambda\), the potential is semidefinite and its restriction to the \(p\)-corner is injective.
More specifically, for \(x\in e\ell^2(G)\),
\[
\langle eWe\,x,x\rangle=\|(1-z)x\|^2,
\tag{17}
\]
so the defect pivot \(eWe|_e\) is injective without computing \(e\), using \(c^{-1}\), or asserting a lower spectral bound for \(eWe\).
Its affiliated inverse is independently certified by (17).

With the same finite \(B_A\) from C_A0008, the eighteen-square family
\[
\mathcal H_\lambda:=
\begin{pmatrix}T+\Psi_\lambda&B_A\\B_A&0\end{pmatrix}
\in M_{18}(\mathbb CG)
\tag{18}
\]
therefore has
\[
\boxed{\begin{aligned}
\lambda\ne0:\quad&
P_{\ker\mathcal H_\lambda}=\operatorname{diag}(0,p),\qquad
\dim_G\ker\mathcal H_\lambda=1,\\
\lambda=0:\quad&
\dim_G\ker\mathcal H_0=1+\dim_H\ker c.
\end{aligned}}
\tag{19}
\]
The zero-potential projection is the already retained complete graph projection of C_A0008.
The probability-normalized zero atoms are respectively \(1/18\) and \((1+\dim_H\ker c)/18\).
There is no smallness or dominance condition on the nonzero parameter.

Suppose at least one of \(u,v\) is nonidentity and choose \(j\) so that \(w:=w_j\ne1\).
Then the compressed potential does not commute with the hopping.
Indeed
\[
[W,Ct]=(WC-C\sigma(W))t,
\qquad
WC-C\sigma(W)=-zC-z^{-1}C+Czw+Cw^{-1}z^{-1}.
\tag{20}
\]
In the free-product normal form, the coefficient of \(z\) on the right is \(-C_1\), where \(C_1:=\tau_H(C)\ge1/3\).
None of the other three terms contributes to that group word when \(w\ne1\).
Thus (20) is nonzero even if some of the six original labels coincide.
This verifies noncommutation using actual group-ring coefficients, independently of the unresolved kernel \(e\).

### Screening the old direct tests

Take \(\lambda=1/10\) and \(w_j\ne1\).
The scalar compression of the residual is
\[
\widehat R_\lambda=C(t+t^{-1})+\lambda(2-z-z^{-1}).
\tag{21}
\]
Its support contains \(1,z,t\), with positive coefficients at \(1,t\), and \(tzt^{-1}=zw\ne z\).
Consequently its support is not contained in a cyclic subgroup or a translate of one.
Its coefficient absolute-value sum is \(2+4\lambda\); every coefficient of \(C\) is nonnegative and their sum is one.
No single coefficient of (21) strictly dominates the others.
These are only the direct cyclic-support and coefficient-dominance screens, not exclusions of every possible factorization.

The residual also has positive and negative quadratic forms, so the direct injective-positive-real-part test on the residual does not apply.
To see this without its full spectrum, restrict trial vectors to the subgroup \(L:=H\times\mathbb Z\).
The vectors \(z^{\pm1}\xi\) are orthogonal to \(\xi\) for \(\xi\) supported on \(L\), since \(z\notin L\).
The potential therefore contributes exactly \(2\lambda\|\xi\|^2\) to such quadratic forms.
The canonical product trace on \(L\) permits independent spectral localization of \(C\) and the height shift.
Since \(\|C\|\ge\tau_H(C)\ge1/3>\lambda\), coefficient vectors near the upper spectral edge of \(C\) and height Fourier vectors near \(\theta=\pi\) give negative quadratic forms for (21).
Vectors localized near \(\theta=0\) give positive ones.
For a selfadjoint operator with both signs, no scalar phase has an injective nonnegative real part: a phase with nonzero real part retains one of the signs, while a purely imaginary phase has zero real part.

The successful certificate is instead the normal-defect split, the cyclically certified potential compression (17), and the existing affiliated graded criterion.
When \(e=0\) is already known, this reduces immediately to the old zero-defect mechanism.
When \(e\) is unresolved, (17) supplies the missing pivot without settling \(e\).
The auxiliary spectral projections and support-corner inverses are used only in the actual affiliated algebra; their membership in the coefficient rational closure is not asserted.
Once the scalar group-ring element (21) has been proved affiliated-invertible, its inverse belongs to the ambient rational closure by its definition.
No new group-wide Atiyah class follows.

## Why arbitrary indefinite potentials require the upper bound

Formula (4) does not extend to every selfadjoint \(V\).
There is an actual compressed-hopping counterexample over a torsion-free group, using a coefficient spectral projection outside the group ring.
Let
\[
G:=\langle a,t\mid tat^{-1}=a^{-1}\rangle
\cong\mathbb Z\rtimes_{-1}\mathbb Z,\qquad N:=\langle a\rangle.
\]
This semidirect product is torsion-free by its infinite cyclic quotient and torsion-free kernel.
Identify \(\mathcal N(N)\) with \(L^\infty(\mathbb T)\) and let \(q_+\) be the upper-semicircle indicator, with endpoints immaterial.
Then \(\tau(q_+)=1/2\) and \(\sigma(q_+)=1-q_+\).
On the corner defined by \(p:=\operatorname{diag}(1,q_+)\), take
\[
K:=ptp|_p=\begin{pmatrix}t&0\\0&0\end{pmatrix},
\qquad
V:=\begin{pmatrix}0&q_+\\q_+&0\end{pmatrix},
\qquad
S:=t+t^{-1}.
\tag{22}
\]
The operator \(K\) is normal, \(\delta=\operatorname{diag}(0,q_+)\), and \(\delta V\delta=0\).
The potential is selfadjoint and indefinite, and \(\ker K\cap\ker V=0\).
Nevertheless, the exact bounded equations give
\[
\ker(K+K^*+V)
=\left\{\binom{x}{-Sx}:x\in(1-q_+)\ell^2(G)\right\}.
\tag{23}
\]
Indeed the lower equation says \(q_+x=0\), and \(S(1-q_+)=q_+S\) makes the upper equation uniquely determine the lower \(q_+\)-coordinate as \(-Sx\).
This graph is closed and equivariantly isomorphic to \(1-q_+\), so its unnormalized kernel trace is \(1/2\), attaining the upper bound in (3) while the common-kernel lower bound is zero.
Its complete projection is \(F(F^*F)^{-1}_{1-q_+}F^*\), where \(F:=\binom{1-q_+}{-S(1-q_+)}\) and \(F^*F\ge1-q_+\).
The spectral projection \(q_+\) is neither a scalar group-ring projection nor a rational-function projection over \(\mathbb C[a^{\pm1}]\).
Thus (22) is an exact boundary example for the operator theorem, not a finite group-ring counterexample to the Task.

## What remains unresolved

The new exact bound controls the residual by the actual coefficient pivot \(\delta V\delta\).
For semidefinite potentials its precise remaining kernel is \(\delta\cap\ker V\).
A potential that annihilates \(\delta\) leaves that defect untouched; in the finite star, taking the frame potential \(W=C\) gives \(e\wedge\ker C=e\).
Hence positivity alone supplies no arithmetic for the unresolved coefficient kernel.
The cyclic energy potential (16) eliminates the defect only because its own injectivity is independently proved.
The zero-parameter family still retains \(\ker(1+u+v)\), and no uniform inverse bound or zero-parameter limiting argument has been obtained.
Neither the defect-pivot theorem nor the finite family supplies a zero-parameter injectivity conclusion or a whole-group Atiyah property.

## Assessment history

### Decision reviewed-defect-potential

| Field | Value |
| --- | --- |
| date | 2026-11-11T18:02 |
| status | proved |
| reason | Independent whole-artifact review supports the common-hopping-defect rank bound, exact semidefinite kernel formula, domain-safe affiliated Schur elimination and finite noncommuting potential construction, with all stated counterexamples and zero-parameter limitations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Complete action-fixed-corner theorem, defect-compression bounds, exact semidefinite conclusions, finite-matrix applications and indefinite boundary example. |
| argument | [Argument](#argument) | All formulas (1)--(23), graded and singular-coefficient interfaces, actual affiliated domains, bounded graph projections, cyclic potential pivot, direct screens and limits. |
| review | [Independent whole-artifact finding](../audits/reviews/Yin_R_A0030_v1.md#whole-artifact-finding) | Complete v2 statement and affected proof chain, including the action-invariance clarification and exact source/domain scope. |

## Current assessment

[Selected decision](#decision-reviewed-defect-potential)


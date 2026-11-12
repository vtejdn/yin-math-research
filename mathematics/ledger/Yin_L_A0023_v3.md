---
author: Yin
---
# Vertex-local rotations and expected-kernel support

This development serves [route five](../strategies/Yin_S_A0005.md) under the [A0001 contract](../tasks/Yin_T_A0001_v1.md#contract).
The question is whether an additive selfadjoint enlargement outside the [word-chain family](../ledger/Yin_L_A0023_v2.md) can remove its edge-valued kernel annihilators while retaining an independently certified rank or nullity correction.
The target interface is the full expected support of a finite polynomial kernel witness required by [C_A0007 v4](../claims/Yin_C_A0007_v4.md#statement).
The complete kernel calculations and support corrections below are separate from their eventual formal review.

## Inputs and outcome

Work in the actual free amalgam
\[
G=F(z,a,b)=G_1*_{H}G_2,
\qquad G_1=F(z,a),\quad G_2=F(z,b),\quad H=\langle z\rangle.
\]
Write \(E_H\) for canonical coefficient expectation, amplified entrywise, and use unnormalized matrix traces throughout.
The input is exactly the eight-square matrix \(K\) in [L_A0023 v2, equation (6)](../ledger/Yin_L_A0023_v2.md#an-explicit-additive-eight-square-matrix), with its proved complete kernel, unit triangular auxiliary inverse and nullity two.
Its coordinates are numbered \(0,\ldots,7\), in the order \((y_0,y_1,y_2,y_3,t_1,t_2,\lambda_1,\lambda_2)\).
Put \(A=a-1\), \(B=b-1\), \(\partial=(A\ B)\) and \(s=Aa+Bb\), as in that input.
No arbitrary free-variable or torsion-free injectivity assertion is added here.

Four vertex-local polynomial unitary rotations, each using one new zero coordinate, produce an additive twelve-square matrix \(\widehat K\) with
\[
\nu(\widehat K)=6,\qquad \operatorname{rk}(\widehat K)=6.
\tag{1}
\]
Its complete polynomial kernel is free of rank five, and a displayed finite basis has expected-Gram rank eleven.
That is the maximal expected support, for both finite polynomial witnesses and the actual analytic kernel projection.
The multiplier-coordinate annihilators disappear; exactly the terminal relation \(y_1-t_2=0\) remains.
The calculation therefore improves the realization beyond the word-chain support deficit without supplying a full-support witness in all twelve coordinates.

A constant compression by that single terminal relation has size eleven and nullity seven, so its exact nullity correction is \(+1\).
The compressed matrix has a finite witness of full expected support and therefore falls within the C_A0007 v4 interface.
The correction is independently computable here from the free-boundary rank and two unit product constraints.
This is an exact calibration over a free group, with no new group coverage or all-matrix transfer theorem.

## The four rotations and additivity

Let \(I=\{2,3,6,7\}\), introduce a new coordinate \(z_i\) for each \(i\in I\), and set
\[
g_2=a,\qquad g_3=b,\qquad g_6=b,\qquad g_7=a.
\]
On the coordinate pair \((i,z_i)\), let
\[
U_i=\frac1{\sqrt2}
\begin{pmatrix}1&-g_i\\g_i^*&1\end{pmatrix},
\qquad
U_i^*=\frac1{\sqrt2}
\begin{pmatrix}1&g_i\\-g_i^*&1\end{pmatrix}.
\tag{2}
\]
Both products \(U_i^*U_i\) and \(U_iU_i^*\) equal the identity by the group-unitary equations \(g_i^*g_i=g_ig_i^*=1\).
The four disjoint rotations define a finite group-ring unitary \(U\) on twelve coordinates.
Define
\[
\widehat K=U^*(K\oplus0_4)U.
\tag{3}
\]
Its inverse change of variables is exactly \(U\); no unknown matrix is inverted.
The input's independently invertible four-square product-chain block supplies the rank of \(K\), while (2) and the four zero blocks give (1) directly.

The four selected old coordinates have zero mutual matrix entries, including their diagonal entries.
Every nonzero entry incident to coordinate \(2\) belongs to \(\mathbb CG_1\), and the same holds for coordinate \(7\).
Every nonzero entry incident to coordinates \(3\) and \(6\) belongs to \(\mathbb CG_2\).
Concretely these rows of \(K\) are
\[
\begin{aligned}
K_{2,\bullet}&=(0,A^*,0,0,0,-A^*,0,0),\\
K_{3,\bullet}&=(0,B^*,0,0,0,-B^*,0,0),\\
K_{6,\bullet}&=(-b,0,0,0,1,0,0,0),\\
K_{7,\bullet}&=(0,0,0,0,-a,1,0,0).
\end{aligned}
\tag{4}
\]
Each affected entry is consequently multiplied on just one side by a coefficient from the same vertex ring.
There are no entries between different rotated pairs at which two different vertex factors could multiply.
The entries between unrotated coordinates remain unchanged and additive.
Thus (3) is a finite selfadjoint sum \(\widehat K_1+\widehat K_2\), with \(\widehat K_j\in M_{12}(\mathbb CG_j)\).
This argument checks the simultaneous rotations, rather than assuming that separately allowable rotations remain allowable after composition.

## Complete kernel and finite witnesses

The complete analytic kernel of the input is
\[
\left\{(f,abf,af+\eta,bf+\theta,bf,abf,0,0)^{\mathsf T}:
 f\in\ell^2(G),\ (\eta,\theta)\in\ker\partial\right\}.
\tag{5}
\]
Therefore the complete analytic kernel of (3) consists of \(U^*(v,h_2,h_3,h_6,h_7)^{\mathsf T}\), with \(v\) as in (5) and arbitrary \(h_i\in\ell^2(G)\).
For example its two multiplier pairs are
\[
(x_6,z_6)=2^{-1/2}(b h_6,h_6),
\qquad
(x_7,z_7)=2^{-1/2}(a h_7,h_7),
\tag{6}
\]
and its two other rotated pairs are
\[
\begin{aligned}
(x_2,z_2)&=2^{-1/2}(af+\eta+a h_2,-f-a^*\eta+h_2),\\
(x_3,z_3)&=2^{-1/2}(bf+\theta+b h_3,-f-b^*\theta+h_3).
\end{aligned}
\tag{7}
\]
The unrotated coordinates are \((x_0,x_1,x_4,x_5)=(f,abf,bf,abf)\).
Equations (5)--(7) are both necessary and sufficient because (2) is an actual bounded unitary change of variables.

The input proves that its complete polynomial kernel is generated by \((1,ab,a,b,b,ab,0,0)^{\mathsf T}\).
Since both \(U\) and \(U^*\) are finite, the complete polynomial kernel of (3) is generated by the five columns
\[
\begin{aligned}
w_0={}&e_0+(e_1+e_5)ab+2^{-1/2}e_2a
 +(2^{-1/2}e_3+e_4)b
 -2^{-1/2}(e_{z_2}+e_{z_3}),\\
w_i={}&2^{-1/2}(e_i g_i+e_{z_i}),\qquad i\in I.
\end{aligned}
\tag{8}
\]
Here \(e_j\) and \(e_{z_i}\) are the twelve constant coordinate columns.
Every polynomial kernel vector is \(w_0f+\sum_{i\in I}w_i h_i\) with coefficients in \(\mathbb CG\), and this representation is unique by applying \(U\) and using the input's complete polynomial kernel.
The formula is a complete kernel calculation, not a count of selected columns.
With \(W=(w_0\ w_2\ w_3\ w_6\ w_7)\), unitarity also gives
\[
W^*W=\operatorname{diag}(6,1,1,1,1).
\tag{9}
\]
Thus the analytic span of its polynomial kernel has dimension five, whereas the full analytic kernel has dimension six.
The surviving extra dimension is the transported free-boundary component in (5).

## Exact expected support

The words \(1,a,b,ab\) lie in distinct cosets \(Hu\), and each \(g_i\notin H\).
Put
\[
v_1=e_0-2^{-1/2}(e_{z_2}+e_{z_3}),
\quad v_a=2^{-1/2}e_2,
\quad v_b=2^{-1/2}e_3+e_4,
\quad v_{ab}=e_1+e_5.
\]
Exact coefficient extraction in (8) yields the constant positive matrix
\[
C:=E_H(WW^*)
=v_1v_1^*+v_av_a^*+v_bv_b^*+v_{ab}v_{ab}^*
 +\frac12\sum_{i\in I}(e_ie_i^*+e_{z_i}e_{z_i}^*).
\tag{10}
\]
The last sum is strictly positive on the eight rotated coordinates.
Together with it, \(v_1\), \(v_b\) and \(v_{ab}\) supply respectively the independent directions \(e_0\), \(e_4\) and \(e_1+e_5\).
Consequently
\[
\ker_{\mathbb C^{12}} C=\mathbb C(e_1-e_5),\qquad
\operatorname{supp}C=q:=I_{12}-\tfrac12(e_1-e_5)(e_1-e_5)^*,
\qquad \operatorname{rk}C=11.
\tag{11}
\]
This verifies that both multiplier pairs now have full expected support, although their unrotated predecessors vanished identically on the entire kernel.

Let \(p=P_{\ker\widehat K}\).
The complete kernel formulas imply \(p\le q\).
Equations (8)--(9) give \(WW^*\le6p\), and hence \(C\le6E_H(p)\).
Bimodularity gives \(E_H(p)\le q\), while (10)--(11) give the reverse support inclusion.
Therefore
\[
\operatorname{supp}E_H(p)=q.
\tag{12}
\]
Every finite polynomial kernel witness is annihilated by \(e_1^*-e_5^*\), so no different finite witness for (3) can have expected-Gram rank twelve.
The failure is exactly one edge direction, and is not caused by incomplete enumeration of polynomial columns.

## The terminal sum and difference, including a coupled-rotation obstruction

Change the two terminal coordinates by the constant unitary basis
\[
p_+=2^{-1/2}(y_1+t_2),\qquad q_-=2^{-1/2}(y_1-t_2).
\tag{13}
\]
Before the rotations, the quadratic form of \(K\) can be written as
\[
2\operatorname{Re}\bigl((y_1-t_2)^*r y
 +\lambda_1^*(t_1-by_0)
 +\lambda_2^*(t_2-at_1)\bigr),
\qquad r y=-sy_0+Ay_2+By_3.
\tag{14}
\]
Thus \(p_+\) couples only to \(\lambda_2\), whereas \(q_-\) retains the mixed boundary row \(r\) and a constant \(\lambda_2\) coupling.
Rotating only \(p_+\) cannot remove the kernel equation \(q_-=0\).

A larger coordinated family also has a concrete obstruction.
Start after the multiplier rotations in (2), optionally also applying the displayed \((y_2,z_2)\) and \((y_3,z_3)\) rotations.
Allow an arbitrary finite polynomial unitary \(V\) over \(\mathbb CG_1\) on the coordinates \(q_-,p_+,\lambda_2,z_7\) and any further zero coordinates, while fixing all other coordinates.
Suppose the resulting congruence remains additive in the two vertex rings.
Let \(u_j\in\mathbb CG_1\) be the entries of the row \(e_{q_-}^*V\).
The untouched old \(y_3\) row is \(\sqrt2 B^*e_{q_-}^*\) before its rotation, and one output row is a nonzero constant multiple of \(B^*e_{q_-}^*\) after the displayed \((y_3,z_3)\) rotation.
That row has no other entry meeting the coordinates on which \(V\) acts.
Therefore additivity requires every \(B^*u_j\) to lie in \(\mathbb CG_1+\mathbb CG_2\).

For \(u\in\mathbb CG_1\), reduced-word normal form gives the exact implication
\[
(b^{-1}-1)u\in\mathbb CG_1+\mathbb CG_2
\quad\Longleftrightarrow\quad u\in\mathbb CH.
\tag{15}
\]
Indeed every group term \(g\in G_1\setminus H\) in \(u\) produces a distinct reduced word \(b^{-1}g\) outside both vertex groups, with the same nonzero coefficient.
It cannot cancel with a term of \(-u\), with \(b^{-1}h\) for \(h\in H\), or with another such distinct reduced word.
The converse follows because \(b^{-1}H\subset G_2\).
Consequently \(e_{q_-}^*V\) is an edge-ring row.
It is nonzero and satisfies \((e_{q_-}^*V)(e_{q_-}^*V)^*=1\) by unitarity.
Every transformed analytic kernel vector is annihilated by this row, because every original kernel vector has \(q_-=0\).
Thus even the coordinated rotation involving the formerly zero multiplier and its new free coordinate retains a nonzero edge-valued kernel annihilator.

The symmetric statement holds for vertex-two rotations that leave a corresponding vertex-one boundary row available, by replacing \(B^*\) with \(A^*\).
This excludes the stated coupled families only.
It does not rule out arbitrary simultaneous operations that also alter both boundary rows, other invertible auxiliary couplings, or a different additive realization.

## A single support compression and its exact correction

The constant projection \(q\) in (11) commutes with \(U\), because the four rotations fix \(y_1\) and \(t_2\).
Thus compression commutes with the known unitary change of variables.
Choose the constant orthonormal coordinate \(p_+\) in (13) on the terminal support, so the unrotated compressed matrix has seven coordinates, plus four independent zeros.
Setting \(q_-=0\) in (14) leaves only
\[
2\operatorname{Re}\bigl(\lambda_1^*(t_1-by_0)
 +\lambda_2^*(p_+/\sqrt2-at_1)\bigr).
\tag{16}
\]
The coordinates \(y_2,y_3\) are now free.
On \((y_0,p_+,t_1)\), the constraint row matrix is
\[
R=\begin{pmatrix}-b&0&1\\0&1/\sqrt2&-a\end{pmatrix}.
\tag{17}
\]
Its submatrix on columns \((t_1,p_+)\) is
\[
\begin{pmatrix}1&0\\-a&1/\sqrt2\end{pmatrix},
\qquad
\begin{pmatrix}1&0\\\sqrt2a&\sqrt2\end{pmatrix}
\tag{18}
\]
for the matrix and its explicit finite inverse, respectively.
Therefore \(R\) is surjective, \(R^*\) is injective, and the selfadjoint off-diagonal matrix with blocks \(R,R^*\) has rank four.
Its complete kernel has \(\lambda_1=\lambda_2=0\), \(t_1=by_0\), \(p_+=\sqrt2ab y_0\), and free \(y_2,y_3\).
Including the four added zeros gives
\[
\operatorname{rk}(q\widehat Kq)=4,
\qquad \nu_q(q\widehat Kq)=11-4=7
=\nu(\widehat K)+1.
\tag{19}
\]
Here \(\nu_q\) is the unnormalized kernel dimension in the eleven-coordinate corner, rather than the twelve-coordinate kernel dimension after adjoining a zero on \(1-q\).
The original witness \(W\) lies in this corner and remains a kernel witness after compression.
Equations (10)--(11), expressed in the constant eleven-coordinate orthonormal basis, give its full-support expected Gram.
Constant compression also preserves the two-vertex additivity, so C_A0007 v4 applies to this compressed matrix.

This correction is fully certified, but its justification uses the already known free-boundary rank encoded by \(K\) and the explicit unit pivots (18).
It supplies no general formula for compressing an unknown group-ring matrix by the deficient support of a polynomial witness.
In particular, neither the existence of the rotations nor full expected support after compression determines the discarded rank for an arbitrary input.

## Continuation boundary

The local rotations genuinely repair the multiplier support defect and keep complete kernel transport, finite coefficients and additivity.
They leave exactly one expected-support defect, whose terminal nature and persistence under the specified coupled vertex rotations are proved above.
The remaining step for a new transfer mechanism is either an additive operation that removes this last edge annihilator with a separately known correction, or a general independently controlled formula for the rank lost at such a support compression.
The free-group example supplies the correction only because its underlying boundary row already has certified rank one.
No reduction of arbitrary torsion-free groups to amalgams with controlled vertices, and no finite-witness realization for arbitrary task matrices, is established.

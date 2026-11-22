---
author: Yin
---

# A Hardy projection test on the cyclic restriction of a group kernel

## Statement

Let \(H=\langle z\rangle\cong\mathbb Z\) be a subgroup of \(G\), and let \(P\in M_n(\mathcal N(G))\) be an orthogonal projection.
Use the coordinate isometry \(J:\ell^2(H)^n\to\ell^2(G)^n\), put \(S=J^*PJ=E_H(P)\), and let \(Q=s(S)\) denote its support projection.
Write \(D\) for the projection onto the nonnegative powers of \(z\), acting on each edge coordinate.
Then
\[
 Q\in M_n(\mathbb C(z))
 \quad\Longleftrightarrow\quad
 \dim_{\mathbb C}\{PJ D\eta:\ \eta\in\ell^2(H)^n,\ PJ\eta=0\}<\infty.       \tag{1}
\]
In the finite case the ordinary operator rank of \([D,Q]\) is exactly twice this dimension.
If \(P\) is the kernel projection of bounded group-ring rows \(A\), the vectors tested on the right are precisely those with \(J\eta\in\overline{\operatorname{ran}A^*}\).
The criterion applies directly to the stacked graph rows of [C7 v13](Yin_C_A0007_v13.md#two-rows-on-the-support-of-their-common-kernel).
That result gives the separate vertex rank conditions needed for integrality once its expected graph support is rational.

## Proof of the cyclic criterion

On \(\ell^2(H)\) put \(Z=\lambda(z)\) and \(B=D Z^*\), where the sign is chosen so that \([B,Z]=P_{\delta_e}\).
Indeed \(D-ZDZ^*\) projects onto exponent zero.
This is an everywhere-defined bounded dual for the normal Haar generator in the operator-first convention.
The [normal dual criterion, C_F0068 Part C, (D4)](Yin_C_F0068_v1.md#dual-specializations) identifies bounded rational functions of \(Z\) by finite rank of their commutator with \(B\).
Here the scalar division closure is exactly \(\mathbb C(z)\), by the circle functional calculus: a nonzero Laurent polynomial has a zero set of Haar measure zero.
For a bounded edge function \(h\), \([B,h]=[D,h] Z^*\).
Applied to the finitely many entries this gives rationality of \(Q\) exactly when \([D,Q]\) has finite rank.
The scalar theorem uses only the cyclic regular representation, independently of any dual on the ambient group.

Now \(\ker(PJ)=\ker S=(1-Q)\ell^2(H)^n\), since \(S=(PJ)^*(PJ)\).
The map \(PJ\) kills \(1-Q\) and is one-to-one on \(Q\ell^2(H)^n\).
It therefore preserves the algebraic dimension of the range of \(QD(1-Q)\).
The two off-diagonal blocks of \([D,Q]\) relative to \(Q\) and \(1-Q\) are this operator and its adjoint, up to sign.
They have the same finite rank or are both of infinite rank, and their ranges belong to orthogonal summands.
This proves (1) and the rank formula without taking an inverse of \(S\) on its support.

## A noncentral cyclic edge with nonrational expected graph entries

Take \(G_1=\langle z,w\mid zw=wz\rangle\), \(G_2=F(z,s)\), and \(G=G_1*_{H}G_2\), so the edge is noncentral in \(G_2\).
This is the torsion-free group \(\mathbb Z^2*\mathbb Z\).
Use \(u=1-z\), \(f=(1-z)(1+w)\), and the two-row matrix and constant matrix
\[
  A_0=\begin{pmatrix}-f&1&0\\-z&0&1\end{pmatrix},\qquad
  C=\begin{pmatrix}1&0&0\\0&0&0\end{pmatrix}.
\]
Split the input into vertex matrices by taking \(Y_1=u A_0+C\) and
\[
  Y_2=-C+\begin{pmatrix}-suz&0&su\\0&0&0\end{pmatrix}.
\]
Their sum is \(\left(\begin{smallmatrix}1&s\\0&1\end{smallmatrix}\right)(u I_2) A_0\).
The first factor is boundedly invertible and \(A_0\) is onto, while \(u\) has dense nonclosed range and zero kernel.
Hence \(Y_1+Y_2\) has nonclosed range and its kernel is the range of the column \((1,f,z)^t\).
On that kernel \(Y_1 x=Cx\).
Thus the common kernel of the graph rows \((Y_1,-I_2),(Y_2,I_2)\) is the closed range of \(V=(1,f,z,1,0)^t\).
Its projection is \(P=V(3+f^*f)^{-1}V^*\), computed in the first vertex.

The edge expectation integrates the independent Haar phase \(w\).
For almost every \(z\), the span of the vectors \(V(z,w)\) as \(w\) varies essentially is the span of \(e_2\) and \(v(z)=(1,0,z,1,0)^t\), because \(1-z\ne0\).
The positive fiber weight \((3+|f|^2)^{-1}\) does not change that span.
Therefore \(Q=e_2e_2^*+vv^*/3\).
The only nonconstant entries of \(Q\) are \(z/3\) in positions \((3,1),(3,4)\) and their adjoints.
Since \([D,Z]\) has rank one, the two blocks connecting coordinate 3 with coordinates 1 and 4 have rank one each and disjoint coordinate ranges.
Thus \(\operatorname{rank}[D,Q]=2\) and the space in (1) has dimension one.

In contrast, put \(t=|1-z|^2=2-z-z^{-1}\) on the circle.
Integrating the first diagonal entry gives
\[
              S_{11}(z)=\int_{\mathbb T}\frac{dw}{3+t(2+w+w^{-1})}
                         =\frac{1}{\sqrt{9+12t}} ,
\]
where \(dw\) is normalized Haar measure.
The integral follows from the constant Fourier coefficient of \((A+B\cos\theta)^{-1}\), equal to \((A^2-B^2)^{-1/2}\) for \(A>|B|\), by the substitution \(\tan(\theta/2)\).
The reciprocal square \(33-12(z+z^{-1})\) has a pole of order one at zero, precluding a square in \(\mathbb C(z)\).
Equality with a rational function almost everywhere on the circle would give the corresponding squared rational identity.
Thus \([D,S_{11}]\) has infinite rank by the same cyclic criterion.
There is no uniform positive lower bound for \(S\) on its support: \(e_2\) belongs to the support almost everywhere but its quadratic form tends to zero as \(z\) tends to one, since \(|f|^2\le4|1-z|^2\).
This example singles out the kernel-supported test (1) even though the expectation has nonrational entries and its nonzero spectrum approaches zero.
It gives a calibration of the criterion, leaving the finite-dimensionality in (1) for arbitrary finite input unresolved.

## Assessment history

### Decision hardy-test-on-edge-kernel

| Field | Value |
| --- | --- |
| date | 2026-11-22T04:54 |
| status | proved |
| reason | Independent review verifies the full statement and argument under the specified assumptions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | An ordinary finite-rank test on the cyclic restriction of a kernel, including its exact dimension and a nonrational expectation example. |
| argument | [Proof](#proof-of-the-cyclic-criterion) | One-generator bounded dual, the off-support block identity and the noncentral graph with a gapless expected projection. |
| review | [Whole finding](../audits/reviews/Yin_R_A0157_v1.md#whole-finding) | Independent whole-argument finding at the stated scope. |

## Current assessment

[Selected decision](#decision-hardy-test-on-edge-kernel)

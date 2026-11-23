---
author: Yin
---

# Testing half-dimensional Schur kernels by finite sums of group elements

## Statement

Let \(N=\mathcal N(G)\) have its canonical tracial state \(\tau\), let \(U=\mathcal U(G)\) be its affiliated algebra, and let \(D_j=D_j(G)\) be the [scalar inverse layers](Yin_C_A0124_v1.md#statement) starting at \(D_0=\mathbb CG\).
Use unnormalized matrix traces for von Neumann dimensions.
For a projection \(P\in N\) assume that its normalized center-valued trace is \(\tfrac12 1\), and put \(Q=1-P\).
This assumption holds in a factor whenever \(\tau(P)=1/2\).
For \(b\in\mathbb CG\) let \(d(b)\) be the trace dimension of the kernel of \(QbP\) on the domain \(P\), and put
\[
 d_k=\inf_{\lvert\operatorname{supp} b\rvert\le k}d(b).
\]
Then \(d_0=1/2\) and \(d_{k+1}\le d_k-d_k^2\).
In particular \(d_k\le1/(k+2)\).
Some \(b\in\ell^1(G)\) attains \(d(b)=0\), and such elements form a dense \(G_\delta\) in that Banach algebra.

Now assume \(P\) is the kernel projection of \(S=d-ca^{-1}b_0\) for \(A=\left(\begin{smallmatrix}a&b_0\\c&d\end{smallmatrix}\right)\) over \(\mathbb CG\), with \(a\) an affiliated unit.
For each finite-support \(b\), \(d(b)\) is the ordinary kernel dimension of an explicit positive three-by-three matrix over \(\mathbb CG\).
If some \(d(b)=0\), then \(D_2(G)\) contains algebraic matrix units for a unital copy of \(M_2(\mathbb C)\), with first diagonal unit \(P\).
This exact implication uses only the scalar condition \(\tau(P)=1/2\).
Under the center-valued hypothesis, if every finite-support mixer has positive defect, the indicated three-by-three family has arbitrarily small strictly positive kernel dimensions.
Thus a uniform positive lower bound on its nonzero nullities forces the finite-support exact case.

For arbitrary \(G\) and a Schur kernel with scalar trace \(1/2\), the same matrix units exist in \(D_2(H)\) for \(H=G*\langle t\rangle\).
In particular \([1]=2[P]\) in \(K_0(D_2(H))\).
When \(G\) is torsion-free, so is \(H\).
Excluding a unital \(M_2(\mathbb C)\) in these second layers, or proving nondivisibility of their unit class by two, would rule out every such original Schur kernel.

## Reduction of the defect with one more group element

For \(T=QbP\), let \(e\le P\) be its kernel projection within \(P\) and let \(f\le Q\) be the projection orthogonal to its image within \(Q\).
Write \(Z\) for the normalized center-valued trace.
Polar decomposition gives \(Z(P-e)=Z(Q-f)\), hence \(Z(e)=Z(f)\).
The closed convex hull in \(L^2(N,\tau)\) of \(\{g e g^*:g\in G\}\) contains \(Z(e)\).
Indeed its point of minimal norm is fixed by conjugation by every group element.
It is a positive contraction in \(N\), since the operator-norm unit ball is closed under \(L^2\) limits, and commutation with all of \(G\) makes it central.
Pairing with every bounded central element is constant throughout the hull, which identifies this point as \(Z(e)\).
Consequently
\[
 \sup_{g\in G}\operatorname{rk}_G(fge)
 \ \ge\ \sup_{g\in G}\tau(fg e g^*)
 \ \ge\ \tau\big(Z(f)Z(e)\big)
 \ =\ \tau\big(Z(e)^2\big)\ \ge\ d(b)^2 .
\]
The first inequality uses that \(fge\) is a contraction, so its squared \(L^2\) norm is at most its image rank.

Use the domain coordinates \((P-e,e)\) and the range coordinates \((Q-f,f)\).
For \(z\ne0\), multiply the second output row of \(Q(b+zg)P\) by \(1/z\).
As \(z\to0\), the resulting operators converge in norm to a lower triangular block matrix with diagonal blocks \(T_{11}\) and \(fge\).
Here \(T_{11}\) has full initial and final support in its two corners and has an affiliated inverse between them.
Eliminating the lower-left block with this inverse gives the limit rank \(\operatorname{rk}_G T+\operatorname{rk}_G(fge)\).
Image rank is lower semicontinuous under norm convergence, by spectral truncation away from zero.
Thus with arbitrarily small nonzero \(z\) the new defect is at most \(d(b)-\operatorname{rk}_G(fge)\) plus any prescribed positive error.
The support gains at most one group element.
Taking the two infima and using monotonicity of \(s-s^2\) on \([0,1/2]\) gives the asserted recurrence.
Whenever the defects are positive, reciprocation gives \(1/d_{k+1}\ge1/d_k+1\), proving the bound.

## Exact mixing with absolutely summable coefficients

In \(\ell^1(G)\) each set of \(b\) for which \(\operatorname{rk}_G(QbP)>1/2-\epsilon\) is open by rank lower semicontinuity.
For density, first choose \(c\) of finite support whose compression rank exceeds the same threshold, using the preceding bound.
For any \(b\in\ell^1(G)\) apply the [polynomial rank bound](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) to the bounded linear pencil \(QcP+wQbP\) at \(w=0\).
Outside a countable exceptional set its rank is at least its rank at zero.
Taking \(w\) arbitrarily large gives \(Q(b+w^{-1}c)P\) of the required rank with arbitrarily small perturbation in the \(\ell^1\) norm.
The Baire category theorem applied to thresholds tending to \(1/2\) gives the assertion.
This allows an infinite group support for \(b\).

## Group-ring witnesses and the exact projection

Put \(x=S^*S\) and \(u_b=x^2+b^*x^2 b\).
The affiliated positive \(u_b\in D_1\) for \(b\in\mathbb CG\) has kernel projection equal to that of \(QbP\) within \(P\).
Indeed a vector in its kernel right \(U\)-module satisfies \(x\xi=0\) and \(x b\xi=0\), by vanishing of a sum of two squares.
These conditions amount to \(\xi=P\xi\) and \(QbP\xi=0\).
Use the group-ring matrix
\[
 K_b=\begin{pmatrix}
  a&0&b_0\\c&0&d\\0&a&b_0 b\\0&c&d b
 \end{pmatrix}.
\]
In its kernel over \(U\), projection onto the third coordinate \(\xi\) is an isomorphism onto the right \(U\)-module just computed.
The first and third equations uniquely prescribe the other coordinates as \(-a^{-1}b_0\xi\) and \(-a^{-1}b_0b\xi\).
The two remaining equations are \(S\xi=0\) and \(Sb\xi=0\).
The kernel projections of bounded group-ring matrices compute these same module dimensions, so \(\dim_G\ker(K_b^*K_b)=d(b)\).

If every finite-support mixer has positive defect under the center-valued hypothesis, the bound on \(d_k\) gives the asserted strictly positive nullities tending to zero.

## Algebraic matrix units from a single inverse

Suppose now that \(\tau(P)=1/2\) and that \(d(b)=0\) for some \(b\in\mathbb CG\).
Let \(V=(x,xb)^{\mathsf T}\), so \(V^*V=u_b\) is an affiliated unit.
Write \(L=u_b^{-1}V^*\).
Then \(LV=1\) and \(VL\) is the final support projection of \(V\), by polar decomposition.
Both entries of \(V\) have image in \(Q\), so \(VL\le\operatorname{diag}(Q,Q)\).
Its unnormalized trace is one because \(V\) has full initial support.
The trace of \(\operatorname{diag}(Q,Q)\) is also one, hence \(VL=\operatorname{diag}(Q,Q)\).
The upper-left corner gives \(Q=xu_b^{-1}x\), so both \(Q\) and \(P\) lie in \(D_2\).

Let \(e_2=(0,1)^{\mathsf T}\) denote the second coordinate inclusion, and set
\[
                F=L e_2=u_b^{-1}b^*x,\qquad T=xbP .
\]
The second column of \(VL\) gives \(xF=0\) and \(xbF=Q\).
Consequently \(PF=F=FQ\), using \(xQ=x\) on the right of the formula for \(F\).
Also \(QT=T=TP\), and \(TF=xbF=Q\).
Since \(xP=0\), one has \(VP=e_2 T\), and multiplying by \(L\) gives \(FT=P\).
Thus \(P,Q,T,F\) are the two diagonal and the lower-left and upper-right algebraic matrix units, all obtained at depth two with the single additional inverse \(u_b^{-1}\).
They yield \([1]=2[P]\) in \(K_0(D_2)\).
A unital homomorphism from this ring to an odd-size matrix ring over a division ring would make two complementary idempotents have equal integer rank, which their odd total dimension excludes.

## Free cyclic extension at depth two

Embed \(G\) in \(H=G*\langle t\rangle\).
By the [coset and free-conjugate computation](Yin_C_A0124_v1.md#free-conjugates-and-sums-of-positive-operators), the kernel projection of the extended \(S\) is still \(P\), and \(P,t^*Pt\) are free with scalar traces \(1/2\).
The kernel of \(QtP\) within \(P\) is the meet of those two projections, whose trace is \((1/2+1/2-1)_+=0\).
Taking \(b=t\) in the single-inverse construction puts the matrix units in \(D_2(H)\).
Free product normal form preserves torsion-freeness.
This conclusion does not require a bound on small positive nullities or specialization of the expression back to \(G\).
For [A0001](../tasks/Yin_T_A0001_v1.md#contract) it remains open whether torsion-freeness and group-ring scalar injectivity exclude the resulting matrix units.

The [first version](Yin_C_A0125_v1.md#algebraic-matrix-units) used another inverse on the \(P\) corner to construct the off-diagonal units in \(D_3\).
The identity \(VL=\operatorname{diag}(Q,Q)\) supplies these units in \(D_2\) and applies directly to the cyclic extension with only the original scalar half-trace hypothesis.

## Assessment history

### Decision half-kernel-mixing

| Field | Value |
| --- | --- |
| date | 2026-11-23T06:25 |
| status | proved |
| reason | The independent whole-argument finding verifies the stated hypotheses, conclusions and limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite-support alternatives, inverse depth and free extension. |
| argument | [Defect recurrence](#reduction-of-the-defect-with-one-more-group-element) | Quantitative finite-support approximation and the hypotheses on the center. |
| argument | [Group-ring witnesses](#group-ring-witnesses-and-the-exact-projection) | Positive three-by-three nullity tests. |
| argument | [Matrix units](#algebraic-matrix-units-from-a-single-inverse) | One Gram inverse gives the projection and parity obstruction. |
| argument | [Free extension](#free-cyclic-extension-at-depth-two) | A single translate gives the depth-two obstruction upstairs. |
| review | [Independent finding](../audits/reviews/Yin_R_A0163_v1.md#original-group-test-and-depth-two) | Whole argument at the stated scope. |

## Current assessment

[Selected decision](#decision-half-kernel-mixing)

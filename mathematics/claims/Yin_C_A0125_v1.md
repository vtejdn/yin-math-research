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
If some \(d(b)=0\), then \(P\in D_2(G)\) and \(D_3(G)\) contains algebraic matrix units for a unital copy of \(M_2(\mathbb C)\), with first diagonal unit \(P\).
Otherwise the indicated three-by-three family has arbitrarily small strictly positive kernel dimensions.
In particular a uniform positive lower bound on its nonzero nullities forces the first alternative.
This result assumes no group class beyond the center-valued condition on the particular projection.

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

Put \(x=S^*S\) and \(u_b=x^2+b^*xb\).
The affiliated positive \(u_b\in D_1\) for \(b\in\mathbb CG\) has kernel projection equal to that of \(QbP\) within \(P\).
Indeed a vector in its kernel right \(U\)-module satisfies \(x\xi=0\) and \(S b\xi=0\), by vanishing of a sum of two squares.
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

If \(d(b)=0\), replace \(b\) by \(b+\lambda 1\), with \(|\lambda|>\|b\|\), so \(b\) is boundedly invertible in \(N\) and \(QbP\) is unchanged.
This replacement may add the identity to the support.
Then \(b^*xb\) has rank \(1/2\), and \(u_b\) is an affiliated unit.
Apply the [two Schur eliminations](Yin_C_A0124_v1.md#the-kernel-projection-and-its-approximants) inside \(G\) to \(\left(\begin{smallmatrix}u_b&x\\x&1\end{smallmatrix}\right)\).
They give a positive contraction \(B=1-xu_b^{-1}x\) of rank \(1/2\) with \(BP=PB=P\).
Thus \(B=P\), giving the asserted second-layer formula.
If every finite-support mixer has positive defect, the bound on \(d_k\) produces the asserted strictly positive nullities tending to zero in this same group.

## Algebraic matrix units

For an exact finite-support mixer set \(T=QbP\in D_2\).
Its initial support is \(P\) and its final support, contained in \(Q\), has the same trace as \(Q\) and so equals \(Q\).
The positive \(J=T^*T+Q\) is an affiliated unit and \(F=J^{-1}T^*\in D_3\).
On the \(P\) corner \(J\) is \(T^*T\), and on the \(Q\) corner \(J\) is the identity.
Polar decomposition, or inversion between the two full corners, gives \(FT=P\) and \(TF=Q\).
Therefore \(P,Q,T,F\) are respectively the diagonal units and the lower-left and upper-right algebraic matrix units.
They give \([1]=2[P]\) in \(K_0(D_3)\) and in \(K_0(\bigcup_jD_j)\).
A unital representation of \(D_3\) in an odd-size matrix ring over a division ring would make the two complementary images isomorphic of equal integer dimension and is incompatible with this conclusion.
Whether torsion-freeness and injectivity of all nonzero group-ring scalars impose the required parity or the preceding positive-nullity gap remains open for [A0001](../tasks/Yin_T_A0001_v1.md#contract).

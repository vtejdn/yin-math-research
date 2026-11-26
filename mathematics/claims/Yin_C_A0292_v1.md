---
author: Yin
---

# The two double poles force diagonal or unipotent factors and a power reversal at a common pole

## Statement

Use the [order-24 half-rank hypotheses and notation](Yin_C_A0290_v1.md#statement), and suppose the denominator pencil \(Q(z)=Cz+D\) has a double determinant zero \(\alpha\) on the circle.
Then the numerator pencil \(P(z)=Az+B\) has a double determinant zero \(\beta\) on the circle.
The leading second-order Laurent matrices of \(M=PQ^{-1}\) at \(\alpha\) and of \(M^{-1}\) at \(\beta\) are proportional nonzero rank-one matrices.

If \(\alpha\ne\beta\), write \(u=(z-\beta)/(z-\alpha)\).
There is a constant basis in which
\[
                M(z)=\begin{pmatrix}1&0\\0&u\end{pmatrix}
                     E\begin{pmatrix}1&0\\0&u\end{pmatrix}
\]
with \(E\) invertible and both its diagonal entries nonzero.
If \(\alpha=\beta\), write \(u=(z-\alpha)^{-1}\) and \(N=e_{12}\).
In a constant basis there is an invertible \(E\) and there are nonzero complex numbers \(\lambda,\mu\) such that
\[
                    M(z)=(I+\lambda uN)E(I+\mu uN),\qquad E_{21}\ne0 .
\]
In this case \(\det M=\det E\) is a root of unity, and some element of \(H\) conjugates a nonzero even power of \(s\) to its inverse.
In particular the common double zero requires a Klein bottle subgroup in \(H\).

## A scalar compression still detects a double pole

Let \(x,y\) generate disjoint infinite cyclic subgroups, meaning that their intersection is trivial.
For a rational row \(a(z)\) and column \(b(z)\), put \(X=a(x)b(y)\) and let \(D_X\) be its singular value tail as in the [two-factor estimates](Yin_C_A0290_v1.md#singular-value-bounds-for-two-cyclic-factors).
The upper bound \(D_X(v)=O(v^{-2/3})\) holds when both factors have only poles of order at most one on the circle, by the same two end cutoffs, rank bound, and rectangular Hilbert-Schmidt integral.
For example the rectangular matrices may be padded by zero rows or columns for this upper estimate, whose proof uses no inverses.

Suppose \(a\) has a pole of order two and the values of \(b\) span the constant column space on a compact regular arc of positive length.
Then \(D_X(v)\ge c v^{-1/2}\) for all sufficiently large \(v\).
For the proof use the ordinary trace on all matrix corners, without a dimensional normalization.
Let \(D\) be the bounded column \(b(y)\) cut down to that arc on its right.
The numerical matrix \(\int DD^*\) is at least \(\varepsilon I\) for some \(\varepsilon>0\), since a constant vector annihilating its range would annihilate the column on the whole arc.
For the high right singular projection \(e=1_{(h,\infty)}(|a(x)|)\), two-factor trace factorization gives
\[
       {\rm Tr}(eDD^*e)\ge\varepsilon\,{\rm Tr}(e),\qquad
       0\le eDD^*e\le \|D\|^2 e.
\]
Thus at least \(\varepsilon\,{\rm Tr}(e)/(2\|D\|^2)\) of this projection has \(eDD^*e\) above \(\varepsilon/2\), by splitting its trace at that level.
The singular values of \(eD\) are the square roots of its nonzero left squared singular values.
The contraction obtained from the polar decomposition of the row \(a(x)\) and its inverse on \(e\) takes \(a(x)D\) to \(h eD\).
Also \(a(x)D\) is a right projection cutoff of \(X\).
Bounded multiplication on either side controls singular values as in the two-factor estimates, so \(D_X(h\sqrt{\varepsilon/2})\ge\varepsilon\,{\rm Tr}(e)/(2\|D\|^2)\).
The double pole bounds \({\rm Tr}(e)\) below by a constant times \(h^{-1/2}\).
Adjoints give the corresponding result for a double pole on the right and rows spanning the constant dual space on a regular arc.

Write \(R,S\) for the leading second-order matrices of \(M,M^{-1}\), respectively.
They have rank one by the [rank-one adjugate calculation](Yin_C_A0290_v1.md#applying-the-four-step-identity).
Choose a nonzero constant row \(\ell\) and column \(v\) with \(\ell R=0,\ Rv=0\).
The scalar compression \(\ell M(t_1)M(t_0)v\) has only simple poles in each of its two factors.
Its counterpart \(\ell M^{-1}(t_0)M^{-1}(t_1)v\) has identical singular value distribution since \(W^{-1}=s^{-4}s^2 W s^{-2}\) for \(W=M(t_1)M(t_0)\).
If \(\ell S\ne0\), the inverse row has a double pole and the inverse column values span \(\mathbb C^2\) on each regular arc.
Indeed failure to span would give a constant point correspondence for \(M^{-1}\), and hence for \(M\), violating the [constant point criterion](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer).
If \(Sv\ne0\), apply the same argument to adjoints: a constant row-line correspondence for \(M^{-1}\) would send the constant kernel line of its output covector to the constant kernel line of its input covector.
Either case gives the incompatible exponents \(2/3\) and \(1/2\).
Thus \(\ell S=0,\ Sv=0\), so the leading matrices have the same image and kernel and are proportional.

## The two rational forms

In the case \(\alpha\ne\beta\), \(M=X_0+X_1u+X_2u^2\) because its only possible pole on the Riemann sphere is \(\alpha\) and its order there is two.
Also \(\det M=\kappa u^2\) for a nonzero scalar \(\kappa\).
Here \(X_0=M(\beta)\) has rank one by invertibility of \(Q(\beta)\), and \(X_2\) is proportional to \(R\).
The adjugate formula makes \(S\) proportional to \({\rm adj}(X_0)\).
If \(X_0\) were nilpotent then \(X_2\) would be proportional to \(X_0\); a projective span of at most two constant matrices gives a constant point correspondence by normalizing an invertible member and taking an eigenline of the other matrix.
Thus \(X_0\) is diagonalizable of rank one, and in its eigenbasis \(X_0={\rm diag}(a,0)\), \(X_2={\rm diag}(0,d)\) with \(ad\ne0\).
The coefficients of \(u\) and \(u^3\) in \(\det M\) force the two diagonal entries of \(X_1\) to vanish.
This yields the stated diagonal factorization with \(\det E=\kappa\).

For \(\alpha=\beta\) one has \(M=E+Uu+Ru^2\) and \(\det M=\Delta=\det E\ne0\).
The coefficient of \(u^2\) in \({\rm adj}(M)/\Delta\) is \({\rm adj}(R)/\Delta\), so \({\rm adj}(R)\) is proportional to \(R\).
A rank-one matrix with this property has trace zero by the two-by-two adjugate identity, and in a constant basis \(R=rN\) with \(r\ne0\).
Write \(E=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\).
The vanishing cubic determinant coefficient gives \(U_{21}=0\).
One has \(c\ne0\), since otherwise \(M\) would be upper triangular with a constant invariant line.
Set \(p=U_{11}\) and \(q=U_{22}\).
The vanishing quadratic and linear determinant coefficients give \(pq=rc\) and \(cU_{12}=pd+qa\).
Substituting \(\lambda=p/c\), \(\mu=q/c\) gives precisely the asserted unipotent factorization and \(\lambda\mu\ne0\).

## A group element reverses a power in the common-root case

Put \(u_i=(t_i-\alpha)^{-1}\).
The product of two neighboring factors \(I+hN,I+kN\) is \(I+(h+k)N\) even for noncommuting \(h,k\).
The outside upper unitriangular factors do not affect the lower left entry.
Multiplication of \(M(t_1)M(t_0)\) and \(M^{-1}(t_0)M^{-1}(t_1)\), respectively, gives
\[
 X=W_{21}=c(a+d)+c^2(\mu u_1+\lambda u_0),\qquad
                  (W^{-1})_{21}=-X/\Delta^2 .
\]
The second formula uses \(E^{-1}_{21}=-c/\Delta\) and \({\rm tr}(E^{-1})=(a+d)/\Delta\).
Here \(X\ne0\).
For example multiplication on the left by \(t_1-\alpha\) and on the right by \(t_0-\alpha\) gives a polynomial on the four distinct group labels \(t_1^i t_0^j\), \(i,j\in\{0,1\}\).
If all coefficients vanished, the mixed coefficient would first give \(a+d=0\), and the two linear coefficients would then force \(\lambda=\mu=0\).

With \(v=s^{-2}\), the middle identity gives \(vXv=\gamma X\), where \(\gamma=-\Delta^{-2}\).
The singular value distribution of \(X\) is invariant under multiplication by \(|\gamma|\).
Since \(X\) is nonzero and affiliated in a finite algebra, its tail tends to zero at infinity and is positive at some level, so \(|\gamma|=1\).
The nonzero bounded partial isometry \(U\) in the polar decomposition of \(X\) therefore satisfies \(vUv=\gamma U\).
Its Fourier coefficients belong to \(\ell^2(H)\).
On each orbit of the permutation \(h\mapsto v h v\), their moduli are constant.
Choose an orbit carrying a nonzero coefficient.
It is finite of some length \(m\), giving \(\gamma^m=1\) and \(v^m h v^m=h\) for a group element \(h\) in that orbit.
It follows that \(\Delta\) is a root of unity and \(h\) reverses \(s^{2m}\) by conjugation.
The infinite-order elements \(s^{2m}\) and \(h\) generate a Klein bottle group: every word reduces to \((s^{2m})^j h^k\), and \(h^k=(s^{2m})^{-j}\) forces \(j=0\) after conjugation by \(h\), followed by \(k=0\) by torsion-freeness.

## Assessment history

### Decision the-two-double-poles-and-their-residue-lines

| Field | Value |
| --- | --- |
| date | 2026-11-26T15:12 |
| status | proved |
| reason | Singular-value comparisons and the matrix coefficient identities yield the stated normal forms and reversal condition. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Residue lines, both rational forms and the group condition. |
| argument | [A scalar compression still detects a double pole](#a-scalar-compression-still-detects-a-double-pole) | The rectangular tail comparison and constant subspaces. |
| argument | [The two rational forms](#the-two-rational-forms) | Distinct and coincident root calculations. |
| argument | [A group element reverses a power in the common-root case](#a-group-element-reverses-a-power-in-the-common-root-case) | Bounded polar coefficients and the exact reversal relation. |
| review | [The two double poles and their residue lines](../audits/reviews/Yin_R_A0214_v1.md#the-two-double-poles-and-their-residue-lines) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-two-double-poles-and-their-residue-lines)

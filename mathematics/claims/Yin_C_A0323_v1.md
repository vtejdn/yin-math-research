---
author: Yin
---

# A bounded positive scalar denominator for fractional four-site kernels

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular scalar group-ring injectivity.
Let \(K=P(t)-sQ(t)\) for complex two-square pencils \(P(z)=Az+B,\ Q(z)=Cz+D\), and suppose its regular nullity \(\delta\) is noninteger.
For almost every constant column line in \(\mathbb C^2\), choose a unit spanning vector \(b\) and a unit vector \(c\) perpendicular to it.
Put \(L=Kb,\ R=Kc,\ a=L^*L\).
Then \(a\in\mathbb CH\) is positive and boundedly invertible in \(C_r^*(H)\).
The positive scalar
\[
                    D_K=R^*R-(L^*R)^*a^{-1}(L^*R)\ \in C_r^*(H)
\]
has regular nullity \(\delta\).
In particular this single inverse in the formula has a spectral gap at zero, independently of whether \(K\) has closed range.
The closed-range properties of \(K\) and \(D_K\) are equivalent.

If \(K\) has closed range, there is a scalar projection of trace \(\delta\) in \(C_r^*(H)\), Murray-von Neumann equivalent to its kernel projection after embedding the scalar corner in the two-square algebra.
Consequently the absence of nontrivial scalar projections in \(C_r^*(H)\) implies that every closed-range rectangle on the indicated marks has integer regular rank.
This test requires no window or cyclic character.
For a rectangle having a common bounded inverse on its range as in the [four-position calculation](Yin_C_A0316_v1.md#one-bounded-inverse-on-the-range-for-every-quotient), closed range is automatic.

The column estimate also has the following form for arbitrary unitary representations.
Suppose both pencils are rationally invertible, their four-square assembly is invertible, and \(M=PQ^{-1}\) has no constant point correspondence, meaning no fixed input line maps to a fixed output line over \(\mathbb C(z)\).
There is at most one pair \((z_0,\lambda)\in\mathbb T^2\) for which \(P(\lambda)=z_0Q(\lambda)\).
For almost every column line, chosen from the coefficients alone, let \(K_\pi\) use the two generators in a unitary representation \(\pi\).
Its column \(K_\pi b\) fails to be bounded below precisely when that scalar pair exists and there are unit vectors \(\xi_j\) satisfying
\[
              \|(\pi(s)-z_0)\xi_j\|+\|(\pi(t)-\lambda)\xi_j\|\longrightarrow0 .
\]
If this condition holds, every constant column fails to be bounded below in that representation.
If the numerical pair is absent, the lower bound for any such chosen unit \(b\) is uniform over all pairs of unitary operators in all Hilbert spaces.

## A numerical pencil on each column line

For \(b\in\mathbb C^2\), put
\[
                    F_b(z)=\big[(B-zD)b\ \ (A-zC)b\big].
\]
For every finite \(z\) the block row \([B-zD,\ A-zC]\) has rank two by the invertible assembly.
If \(\det F_b(z)=0\) for all \(b\), there exist scalars \(\alpha,\beta\) and an invertible numerical matrix \(G_0\) such that
\[
                     B-zD=\alpha G_0,\qquad A-zC=\beta G_0 .
\]
Indeed if one matrix is invertible its left inverse turns the other into a map preserving every complex line, hence a scalar.
If both were singular the full row rank would force them to have distinct nonzero image lines.
A vector outside their two kernel lines would give independent images, contradicting the determinant condition.
The two scalars cannot both vanish.

At such a \(z\), the homogeneous pencil values \(P_{u,v}=u B+v A,\ Q_{u,v}=u D+v C\) satisfy \(P_{u,v}=zQ_{u,v}\) at the unique point \([u:v]\) determined by \(u\alpha+v\beta=0\).
The matrix \(Q_{u,v}\) is invertible there, since stacking \(P_{u,v},Q_{u,v}\) gives a full-column-rank matrix by assembly.
Different \(z\)'s with the determinant condition would give distinct such points.
If there were two, denote their values by \(z_i,Q_i\) for \(i=1,2\).
Interpolation in the two independent projective directions expresses the transfer as
\[
       (z_1 l_1 I+z_2 l_2 Q_2 Q_1^{-1})
                       (l_1 I+l_2 Q_2 Q_1^{-1})^{-1}
\]
for scalar linear forms \(l_1,l_2\).
Any eigenline of \(Q_2Q_1^{-1}\) would be a constant invariant line, contrary to the assumed absence of a constant point correspondence.
Thus at most one \(z\) can make the determinant vanish in every direction.

We choose \(b\) so that all zeros of \(\det F_b\) on the unit circle have this all-directions property.
In an affine chart \(b=(1,u)^{\mathsf T}\) the determinant is a polynomial of degree at most two in each of \(u,z\), and is not identically zero in both variables by the previous paragraph.
Divide its coefficient polynomials in \(z\) by their common polynomial gcd.
For the resulting polynomial, at each \(z\) its finite \(u\)-roots form a finite set.
Apart from finitely many \(z\)'s on the circle, these roots, if any, are locally holomorphic functions of \(z\): use the linear or quadratic formula off zeros of the leading coefficient and discriminant, taking the repeated root directly for an identically zero discriminant.
For a constant polynomial in \(u\) primitivity leaves no zeros.
The resulting countable union of smooth real arcs and finitely many exceptional finite sets has area zero in the \(u\)-plane.
Adjoining the one omitted chart point still gives measure zero on the projective line.
Every \(b\) outside this set has the required property, and \(\det F_b\) is a nonzero polynomial.

## The column in a unitary representation

Write \(S,T\) for the two unitaries, including the regular pair as one choice.
One has the exact column action
\[
                 K_\pi b\,\xi=F_b(S)(\xi,T\xi)^{\mathsf T}.
\]
Here the entries of \(F_b(S)\) are linear in \(S\), and \(T\) occurs to their right in the second coordinate.
If the determinant has no circle zero, \(F_b(S)\) has a bounded inverse by the spectral calculus of \(S\).

Suppose instead that unit vectors \(\xi_j\) give \(K_\pi b\,\xi_j\to0\).
Multiplying the displayed equation by the bounded adjugate of \(F_b(S)\) makes \((\det F_b)(S)\) tend to zero on both \(\xi_j\) and \(T\xi_j\).
Its only circle zero must be the single point \(z_0\) above.
On any closed arc away from \(z_0\) the modulus of the determinant has a positive lower bound.
The spectral mass of either sequence outside any fixed neighborhood of \(z_0\) consequently tends to zero.
It follows that \((S-z_0)\xi_j,(S-z_0)T\xi_j\to0\).
We can replace \(S\) by \(z_0\) in \(F_b(S)\) on these vectors with norm error tending to zero.
Using \(G_0b\ne0\), we obtain \(\alpha\xi_j+\beta T\xi_j\to0\).
The case \(\beta=0\) is impossible.
Thus \(\lambda=-\alpha/\beta\) has modulus one, \(P(\lambda)=z_0Q(\lambda)\), and \(T\xi_j-\lambda\xi_j\to0\).

Conversely the two approximate eigenvector conditions at a common scalar pair make \(K_\pi b\,\xi_j\to0\) for every constant \(b\), by direct substitution, including the product \(ST\).
When no such numerical pair exists, a failure of uniformity over unitary pairs would give a sequence of pairs and unit vectors with column norms tending to zero.
Their Hilbert direct sum contradicts the statement just proved for the two direct-sum unitaries.

## Reduction to one scalar in the reduced group algebra

For noninteger \(\delta\), the [four-column and singular-block reductions](Yin_C_A0184_v1.md#the-four-group-elements-and-the-trace-bound) give regular pencils and invertible assembly.
The group is noncyclic, and [constant point correspondence](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer) would force integer regular rank.
Moreover \(H\) is nonamenable by scalar injectivity and the [amenable Ore argument](Yin_C_A0211_v1.md#right-fractions-for-commensurable-amenable-subgroups).
For the regular representation even an existing common numerical pair cannot give the two approximate eigenvectors.
Indeed pointwise absolute values of those vectors would be almost invariant under both left translations, by the reverse triangle inequality for complex numbers and the unit moduli.
Their squared absolute values would give almost invariant probability densities in \(\ell^1(H)\), and a weak-star accumulation point of the associated means would be an invariant mean.
The column \(L=Kb\) is therefore bounded below, and the canonical faithful regular representation gives \(a=L^*L\) a bounded inverse in \(C_r^*(H)\).

Put \(d=R^*R,\ e=L^*R\).
In the constant orthonormal basis \((b,c)\), the Gram matrix of \(K\) is \(\left(\begin{smallmatrix}a&e\\e^*&d\end{smallmatrix}\right)\).
Congruence by the bounded invertible matrix \(\left(\begin{smallmatrix}1&-a^{-1}e\\0&1\end{smallmatrix}\right)\) gives \({\rm diag}(a,D_K)\).
In particular \(D_K\) is positive, its kernel has dimension \(\delta\), and its range is closed precisely when that Gram matrix has closed range.
A bounded operator and its positive Gram matrix have closed range simultaneously, by their common positive lower bound on the orthogonal complement of the kernel, squared for the Gram matrix.

If this range is closed, zero is isolated from the positive spectrum of \(D_K\).
Continuous functional calculus gives \(p=\mathbf 1_{\{0\}}(D_K)\in C_r^*(H)\).
The invertible congruence and the constant change of basis carry \(0\oplus p\) onto the kernel space of \(K\).
The range projection is equivalent to \(0\oplus p\) over \(M_2(C_r^*(H))\): the image of an orthogonal projection \(q\) under a bounded invertible \(J\) is represented by the polar partial isometry
\[
                       Jq(qJ^*Jq+I-q)^{-1/2}.
\]
It follows that \(\tau(p)=\delta\in(0,1)\), proving the scalar projection obstruction.

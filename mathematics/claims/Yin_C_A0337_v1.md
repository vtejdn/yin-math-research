---
author: Yin
---

# A trace parameter classifies constant Hermitian forms for the two exceptional transfer prototypes

## Statement

In either normalized [exceptional order-twenty prototype](Yin_C_A0336_v1.md#a-circle-valued-scalar-square-of-the-transfer), write
\[
 s_0=\sigma\sqrt5,\quad q(z)=z^2-s_0z+2,\quad p(z)=2z^2-s_0z+1,
 \qquad M=(Az+B)(Cz+D)^{-1},\qquad M^2=(p/q)I .
\]
Use the zero-trace transfer, with \(\det(Cz+D)\) proportional to \(q\), and assume its three projective numerator coefficients are linearly independent.
The latter is necessary for fractional regular rank by the [constant point correspondence test](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer).
Use the ordinary two-dimensional trace and set
\[
                      d={\rm Tr}\big(M(0)M(\infty)\big)
                         ={\rm Tr}\big(BD^{-1}AC^{-1}\big).
\]
The domain for \(d\) is \(\mathbb C\setminus\{1/2,2,5/2\}\).
Every value in this domain is realized by a numerical prototype with all four corners and the assembled coefficient block invertible and with no constant point correspondence.

There exists a constant positive definite Hermitian matrix \(G\) such that \(M(z)^*G M(z)=G\) for every \(|z|=1\) if and only if \(d\) is real and \(2<d<5/2\).
There exists a constant Hermitian matrix of signature \((1,1)\) satisfying the same equations if and only if \(d\) is real and \(d<1/2\).
In all remaining cases no nonzero constant Hermitian matrix satisfies them.
In the admissible cases the real line of invariant Hermitian matrices is unique.
Accordingly the [unitary similarity group-return obstruction](Yin_C_A0336_v2.md#a-necessary-group-relation-for-a-unitary-twisted-transfer) applies to the positive interval, without an additional simultaneous unitarization test.
The range of examples here is a numerical realization, not a construction of a group supporting a half-dimensional kernel.

## From the boundary equation to three traceless matrices

Write \(N=qM=N_0+zN_1+z^2N_2\).
Its coefficients are traceless and \(N(z)^2=p(z)q(z)I\).
On traceless complex two-square matrices use the nondegenerate symmetric bilinear form \(\langle X,Y\rangle={\rm Tr}(XY)/2\).
Then \(XY+YX=2\langle X,Y\rangle I\), by polarization of Cayley--Hamilton.
Since \(N_0=2M(0)\) and \(N_2=M(\infty)\), one has \(\langle N_0,N_2\rangle=d\).
Comparison of the other coefficients in \(N^2=pqI\) gives
\[
  \langle N_0,N_0\rangle=\langle N_2,N_2\rangle=2,\qquad
  \langle N_0,N_1\rangle=\langle N_1,N_2\rangle=-3s_0/2,\qquad
  \langle N_1,N_1\rangle=10-2d .
\]
As \(p(z)=z^2\overline{q(z)}\) on the circle, unitarity for a Hermitian form is equivalent to
\[
                  z^2 N(z)^*G=G N(z)\qquad (|z|=1).
\]
Indeed \(M^{-1}=qM/p\), and right multiplication by \(M^{-1}\) in the original equation requires no invertibility of \(G\).
Equating the coefficients shows that
\[
       X=N_0+N_2,\qquad Y=i(N_0-N_2),\qquad Z=N_1
\]
are all selfadjoint for \(G\), meaning \(X^*G=GX\) and likewise for the other two.
Their Gram matrix is
\[
  \begin{pmatrix}
      4+2d&0&-3s_0\\
      0&2d-4&0\\
      -3s_0&0&10-2d
  \end{pmatrix}.
\]
The block on \(X,Z\) has determinant \(4(d-1/2)(5/2-d)\).
The three coefficients form a basis precisely when the displayed Gram matrix is nonsingular, because the ambient traceless space has complex dimension three and its bilinear form is nondegenerate.
This explains the three excluded parameter values.

## Signature and simultaneous similarity

A rank-one invariant Hermitian form would have an invariant kernel line for \(X,Y,Z\).
Their complex span is the whole traceless matrix space, so there is no such line.
If \(G\) is definite, constant similarity and a change of sign make \(G\) the identity.
On the real space of traceless Hermitian matrices the bilinear form is real positive definite of dimension three.
For \(G={\rm diag}(1,-1)\) the selfadjoint traceless matrices instead have the form
\[
                        \begin{pmatrix}a&b\\-\bar b&-a\end{pmatrix}
                  \quad (a\in\mathbb R,\ b\in\mathbb C).
\]
They have real signature \((1,2)\), since the square coefficient is \(a^2-|b|^2\).
In either case complex independence makes \(X,Y,Z\) a real basis of the respective three-dimensional space.
Consequently the Gram matrix must be real and have the corresponding signature, and in particular \(d\) is real.

Conversely a real Gram matrix of either required signature can be diagonalized over \(\mathbb R\), giving real linear combinations \(X_1,X_2,X_3\) of the original basis with square \(I,I,I\) or \(I,-I,-I\) and products anticommuting at distinct indices.
Put \(X_1={\rm diag}(1,-1)\) by a similarity.
The second matrix is purely off-diagonal and a diagonal similarity puts its off-diagonal entries equal to \(1,1\) in the definite case and \(1,-1\) in the other case.
The third is also purely off-diagonal.
Anticommutation with the second and its prescribed square make it, up to sign, the matrix with off-diagonal entries \(i,-i\) in the definite case or \(i,i\) in the other case.
Thus the three are simultaneously selfadjoint for the required Hermitian form.
Any two invertible invariant forms give, by taking the inverse of one times the other, a matrix commuting with all the traceless matrices, hence a scalar.
Hermiticity forces the scalar to be real.

The \(X,Z\) block is positive definite for \(1/2<d<5/2\), and indefinite for \(d<1/2\) or \(d>5/2\).
Adding the \(Y\)-direction of square \(2d-4\) gives the positive interval \(2<d<5/2\) and the signature-\((1,2)\) interval \(d<1/2\).
All other real values in the domain give signature \((2,1)\).

## Realizing the parameters by regular linear pencils

For any \(d\) outside the three excluded values, take a basis of traceless complex matrices \(X,Y,Z\) having the indicated Gram matrix.
Such a basis exists by diagonalizing nondegenerate symmetric forms over \(\mathbb C\): the usual three Pauli matrices are orthonormal for the trace pairing.
Put \(N_0=(X-iY)/2,\ N_1=Z,\ N_2=(X+iY)/2\).
The Gram identities give \(N(z)^2=p(z)q(z)I\) and \(M=N/q\).
For an explicit example without a constant invariant Hermitian form, take \(d=1\), write \(T_1,T_2,T_3\) for the standard Hermitian Pauli matrices with \(T_3={\rm diag}(1,-1)\), and use
\[
          X=\sqrt6\,T_1,\qquad Y=i\sqrt2\,T_2,\qquad
          Z=-3s_0 T_1/\sqrt6+T_3/\sqrt2 .
\]

To recover linear pencils, let \(\beta_1,\beta_2\) be the two distinct zeros of \(q\).
The two nonzero nilpotents \(N(\beta_i)\) are not proportional: comparing the independent \(N_j\)-coefficients of the two evaluations rules this out.
Rank-one nilpotents have their image equal to their kernel and are determined up to scalar by that line.
Hence the two kernel lines \(l_1,l_2\) are distinct.
Let \(\Pi_i\) be projection onto \(l_i\) along the other line and set
\[
              Q(z)=(z-\beta_2)\Pi_1+(z-\beta_1)\Pi_2,\qquad P(z)=M(z)Q(z).
\]
The image of \(Q(\beta_i)\) is \(l_i\).
Therefore \(P\) has no finite pole, and its growth is at most linear at infinity, so it is a linear polynomial.
One has \(\det Q=q,\ \det P=-p\); both leading and both constant matrices are invertible.

For assembly invertibility let \(R_i=N(\beta_i)/q'(\beta_i)\) be the residues.
They have distinct image lines and distinct kernel lines.
The difference \(M(z)-M(w)\) at two different regular finite parameters is a sum of the two \(R_i\) with nonzero scalar coefficients by partial fractions, hence invertible: a vector annihilated by their sum is in both kernels.
The two corresponding graph planes are complementary, and the assembly sends the two complementary scalar graph columns \((zI,I)^{\mathsf T},(wI,I)^{\mathsf T}\) onto them, up to coordinate order.
This proves that the assembly is invertible.
Finally a constant point correspondence would put all \(N_j v\) on a single line for a nonzero \(v\), impossible since the traceless matrices send \(v\) onto all of \(\mathbb C^2\).
Thus these examples satisfy the stated numerical hypotheses.

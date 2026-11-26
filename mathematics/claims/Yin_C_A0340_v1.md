---
author: Yin
---

# An arithmetic obstruction and an injective determinant-zero witness at order twenty

## Statement

Use the two normalized exceptional order-twenty determinant lines up to the [two mark orientations and five phase rotations](Yin_C_A0336_v1.md#the-coefficient-lines).
Assume \(H=\langle g,h\rangle\) is torsion-free and scalar-injective in the regular representation, and the rectangle has nullity \(1/2\).
Put \(M=PQ^{-1},\ U=g^{-1}M(h)\) and \(d=\operatorname{tr}(M(0)M(\infty))\), with ordinary two-square trace.
If \(r(U)\le1\), there is an explicit injective two-square matrix \(A_+\) over the index-two sign subgroup \(F\), supported on at most eight group elements, whose Fuglede--Kadison determinant vanishes.
In particular its positive singular-value distribution has an infinite logarithmic integral at zero.
The same consequence holds for \(r(U^{-1})\le1\) after reversing both marks and taking the inverse transfer.

When \(H\) is sofic, a half kernel at a normalized exceptional input with arbitrary complex coefficients forces all of the following.

* The numerical parameter \(d\) is algebraic over \(\mathbb Q\).
* No algebraic conjugate of \(d\) lies in the real interval \((2,5/2)\).
* Both \(r(U)>1\) and \(r(U^{-1})>1\). The same inequalities hold after every coefficient-field embedding of the normalized group-ring rectangle, with the corresponding embedded transfer.

In particular, if \(H\) is sofic and \(d\) is transcendental or has a conjugate in that interval, a half kernel in the order-twenty problem must be detected by the [index-four character test](Yin_C_A0336_v1.md#statement) whenever the normalized parameter is applicable.
The argument imposes these restrictions on the given two-square family and leaves the general Atiyah question open.

## From the fourth regular moment to the determinant

Under the radius hypothesis the [central-trace argument](Yin_C_A0339_v1.md#statement) gives unnormalized traces \(\operatorname{Tr}(U^2)=0,\ \operatorname{Tr}(U^4)=2\).
Use the trace normalized on the two matrix coordinates and put \(W=U^2\).
Its Brown measure is a probability in the closed unit disk since \(r(U)\le1\), and its first two complex moments are zero and one.
The integral of \({\rm Re}\,z^2\) thus equals one, the maximum on the disk, attained only at \(z=1,-1\).
The first moment forces equal masses at those points.
The logarithmic potential identity gives \(\log\Delta(W+I)=-\infty\).
Here one uses the bounded-operator support and moment identities and the defining potential formula for Brown measure. [Hall and Kemp, Section 2.3](https://doi.org/10.1016/j.aim.2019.106771) [Haagerup and Schultz, Theorem 2.7](https://arxiv.org/pdf/math/0605251#page=10)

In contrast, \(W+I\) is injective: its kernel splits into the two eigenspaces of \(U\) at \(i,-i\), both zero by the [three-parameter budget](Yin_C_A0329_v1.md#statement) because the eigenspaces at \(1,-1\) already exhaust one unit of dimension.
Write \(h_1=ghg^{-1}\) and use the [linear left denominator](Yin_C_A0333_v1.md#an-eight-label-matrix-on-the-actual-sign-subgroup) \(D_L,N_L\) with \(D_LP=N_LQ\).
Take
\[
       A_+=N_L(h_1)P(h)+D_L(h_1)g^2Q(h)
            =D_L(h_1)g^2(W+I)Q(h).
\]
Both exterior cyclic factors are boundedly invertible, since their determinants are nonzero constant multiples of the same quadratic with roots outside the unit circle.
The support is contained in \(h_1^i h^j,h_1^ig^2h^j\), \(0\le i,j\le1\).
All these words are in \(F\).
Injectivity and the logarithmic determinant pass to \(F\) by equality of regular spectral distributions on a subgroup.
The determinant of \(A_+\) is zero by multiplicativity with invertible factors.
For \(F_A(s)\) the normalized trace of the spectral projection of \(|A_+|\) on \((0,s]\), the logarithmic integral statement is exactly
\[
               \int_0^1\frac{F_A(s)}s\,ds=\infty .
\]
This follows by integration of the nonnegative function \(\log^-(t)\) against the singular-value distribution.
In particular \(\sum_{k\ge1}F_A(2^{-k})=\infty\), independently of the normalization of the matrix trace.

For the inverse put \(g'=g^{-1},\ h'=h^{-1},\ M'(y)=M(y^{-1})^{-1}\).
The marked subgroup and signs are the same, and \(g'^{-1}M'(h')=gM(h)^{-1}\) is conjugate to \(U^{-1}\) by \(g\).
The two cyclic pencils are \(yQ(y^{-1}),yP(y^{-1})\).
The normalized scalar square \(b(y)\) obeys \(b(y^{-1})=1/b(y)\), so the inverse transfer has the same prototype up to a common nonzero determinant factor.
The eigenspace at one has the same dimension as before, giving the other radius test.

## Coefficient embeddings at a half kernel

Write the finite group-ring rectangle in the normalized coordinates. Its field of coefficients can be enlarged to include \(s_0=\sigma\sqrt5\) and \(d\).
For sofic \(H\), its regular rank is unchanged under any two complex embeddings of this field. [Jaikin-Zapirain, Corollary 1.7](https://matematicas.uam.es/~andrei.jaikin/preprints/sac.pdf)
The [prototype identities and independence of the three traceless coefficients](Yin_C_A0337_v1.md#from-the-boundary-equation-to-three-traceless-matrices) are algebraic equations and nonvanishing minors.
They persist under such embeddings, with a possible change of the sign of \(s_0\).
For a real parameter in \((2,5/2)\), the [constant positive form](Yin_C_A0337_v1.md#signature-and-simultaneous-similarity) makes \(U\) similar by a constant matrix to a unitary.
This contradicts the [forward power bound exclusion](Yin_C_A0339_v1.md#statement).

If \(d\) is transcendental choose another transcendental real number \(d'\in(2,5/2)\) and embed by \(d\mapsto d'\) fixing the algebraic numbers.
Such a map extends to the finite set of numerical coefficients: extend a transcendence basis of \(\overline{\mathbb Q}(d)\) in the generated field to algebraically independent target elements over \(\overline{\mathbb Q}(d')\), then extend the embedding across the algebraic part in \(\mathbb C\).
For an algebraic \(d\), any conjugate can similarly be reached by first extending the chosen number-field embedding to the algebraic closure of \(\mathbb Q\).
These arguments prove the two arithmetic restrictions without requiring embeddings to respect complex conjugation.

## Algebraic representatives and the sofic determinant bound

For algebraic \(d\) the transfer is conjugate by a constant numerical matrix, up to an overall sign, to a transfer with algebraic linear-pencil coefficients.
Indeed the nondegenerate Gram matrix of its three numerator coefficients is over \(\overline{\mathbb Q}\).
Diagonalization over this algebraically closed field gives a basis with the same Gram matrix in the three-dimensional space of traceless algebraic two-square matrices.
To compare the two realizations, make identical algebraic linear combinations so that the bases have squares \(I\) and pairwise anticommute.
In each realization put the first two matrices by simultaneous complex similarity into the diagonal Pauli matrix and the off-diagonal swap, in that order.
The third is then the remaining Pauli matrix up to sign.
If the signs disagree, negating the full triple and conjugating by the third Pauli matrix adjusts the third sign while restoring the first two.
Undo the linear combinations to obtain the assertion for \(M\).
The [two distinct residue lines](Yin_C_A0337_v1.md#realizing-the-parameters-by-regular-linear-pencils) in the algebraic realization and their projections have algebraic coordinates, yielding algebraic \(P,Q\) with invertible assembly.
A constant conjugacy commutes with both translations.
An overall minus sign preserves the spectral radii and, by the sign character, the half kernel.

If either tested radius were at most one, apply the first part to this algebraic realization in the corresponding orientation.
Its \(A_+\) has algebraic coefficients by the displayed group-ring formula, also in the inverse orientation.
Multiply by a nonzero positive integer to make all coefficients algebraic integers and form the positive square \(A_+^*A_+\) after this scaling.
It is injective, and its logarithmic determinant is still \(-\infty\).
The determinant bound for positive matrices over algebraic integer group rings of sofic groups gives a finite lower bound, a contradiction. [Knebusch, Definition 2.5 and Theorem 4.4](https://arxiv.org/pdf/0804.0530#page=6)
One may apply that theorem on \(H\) itself, where the regular logarithmic determinant agrees with that on \(F\).
This proves both strict radius inequalities, and rank independence applies the same argument after each coefficient embedding.

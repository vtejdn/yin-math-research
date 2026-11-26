---
author: Yin
---

# Scattering matrices eliminate the exceptional order-twenty determinant lines

## Statement

Let \(H=\langle g,h\rangle\) be torsion-free and suppose every nonzero scalar of \(\mathbb CH\) acts injectively in the regular representation.
Use one of the two [normalized order-twenty orientations](Yin_C_A0336_v1.md#the-coefficient-lines), so that \(h\) has infinite order and there are actual characters at all \(y\in\mu_{10},\ x=\pm y^2\), with \(x=\chi(g)\), \(y=\chi(h)\).
For either sign \(s_0=\pm\sqrt5\) put
\[
 q(y)=y^2-s_0y+2,\qquad p(y)=2y^2-s_0y+1,\qquad B(y)=p(y)/q(y).
\]
A normalized traceless transfer \(M(y)=N(y)/q(y)\) with \(\deg N\le2\), three independent numerator coefficients and \(M^2=BI\) cannot have \(\dim_H\ker(M(h)-gI)=1/2\).
Here the two coordinate traces are added.
Consequently, for *every* half-nullity rectangle at the original [noncyclic order-twenty marking](Yin_C_A0333_v1.md#statement), some scalar character of the joint sign kernel detects rank at least three on its four-square commutator.
The commutator has inner rank at least three over that subgroup ring and exactly two over its second actual scalar inverse layer by the [sign-square reduction](Yin_C_A0336_v1.md#statement).
This conclusion uses the regular representation of the given group and requires no approximation hypothesis.

## Which group words can contribute to the trace

Write \(\tau\) for the scalar regular trace and abbreviate the cyclic operator \(f(h)\) by \(f\).
All rational functions used in the scattering matrices below have no poles on the circle, so their Laurent coefficients are absolutely summable.
In particular \(\tau f\) is their circle mean with normalized Haar measure.

Suppose throughout that the nullity is \(1/2\).
Then \(H\) has finite abelianization by the [integer-character theorem](Yin_C_A0179_v1.md#statement), since its abelianization is finitely generated.
We claim that
\[
 \langle h\rangle\cap g\langle h\rangle g^{-1}=\{1\},\qquad
                      g^{-1}h^i g^{-1}h^j\ne1\quad(i,j\in\mathbb Z).
\]
For the first, a nontrivial intersection makes both generators, hence the group, commensurate \(\langle h\rangle\).
For \(v h^r v^{-1}=h^s\), \(r,s\ne0\), the ratio \(s/r\) is independent of the powers chosen by raising the two relations to a common multiple.
These ratios give a homomorphism \(H\to\mathbb Q^\times\) by composing after matching intermediate exponents.
Finite abelianization implies its image lies in \(\{1,-1\}\).
In particular \(g\) normalizes \(\langle h^m\rangle\) for some \(m>0\).
For the second claim, a two-step return gives \(a^2=h^{i-j}\) for \(a=g^{-1}h^i\).
This power commutes with \(a,h\), which generate the group.
If \(i=j\), torsion-freeness gives \(a=1\), making \(H\) cyclic in contradiction to its marked quotient.
Otherwise we again have a nontrivial cyclic subgroup \(\langle h^m\rangle\) normalized by \(g\).

In either case such normalization forces the original two-square rank to be integral.
Indeed the Laurent ring \(T=\mathbb C[h^{\pm m}]\) is preserved under conjugation by \(g,h\).
Any rational function in \(h\) has a denominator in \(T\): replace each nonzero Laurent denominator \(r(h)\) by \(\prod_{\omega^m=1}r(\omega h)\), which is nonzero and invariant under \(h\mapsto\omega h\).
Any finite rational expression formed by sums and products of elements of \(\mathbb C(h)\) and group translations consequently has the form \(z^{-1}u\) for some \(0\ne z\in T,\ u\in\mathbb CH\).
Indeed commute the denominators to the left through each group word and take the product of the finitely many resulting denominators in \(T\).
At least one off-diagonal entry of \(M\) is a nonzero cyclic rational function by independence of the three traceless coefficients.
Use it as an affiliated pivot for \(M(h)-gI\).
The remaining Schur scalar is such a finite expression, with the cyclic pivot inverse still in \(\mathbb C(h)\).
By scalar injectivity it has rank zero or one, contradicting the assumed half kernel and proving both claims.

Consequently \(\tau(g^{-1}f g k)=\tau(g f g^{-1}k)=(\tau f)(\tau k)\) for any absolutely summable cyclic coefficients \(f,k\).
Also \(\tau(g^{-1}f g^{-1} k)=\tau(g f g k)=0\) by the two-step assertion and inversion.
These formulas follow by expanding the absolutely convergent Laurent series in the regular trace.

## Centering a constant indefinite form

Let \(d=\operatorname{tr}(M(0)M(\infty))\).
A half kernel forces \(d\) real by the [Clifford parameter bound](Yin_C_A0342_v1.md#the-generalized-zero-space-at-infinity).
The [Gram classification](Yin_C_A0337_v1.md#signature-and-simultaneous-similarity) rules out \(d=1/2,2,5/2\) by independence.
For \(2<d<5/2\) the transfer is similar by a constant matrix to a unitary on the circle, so the [forward power bound](Yin_C_A0339_v1.md#statement) excludes the half kernel.
For \(d<1/2\) use a constant similarity so that \(M^*JM=J\) on the circle for \(J=\operatorname{diag}(1,-1)\).
In the other two intervals \(1/2<d<2\) and \(5/2<d\), the Gram matrix of the three traceless matrices \(X,Y,Z\) in that classification has signature \((2,1)\).
The matrix for \(iX,iY,iZ\) has signature \((1,2)\), so the same real diagonalization and Pauli basis argument makes these three selfadjoint for \(J\) after constant similarity.
It makes \(X,Y,Z\) skew-adjoint for \(J\), changing the boundary coefficient identity to \(y^2N(y)^*J=-JN(y)\).
Thus \(M^*JM=-J\).
Constant similarity preserves all nullities.

Write \(M=\left(\begin{smallmatrix}a&b\\c&-a\end{smallmatrix}\right)\).
For \(M^*JM=J\) one has \(|a|^2=1+|c|^2\) and \(b/a=-\overline{c/a}\) on the circle.
For \(M^*JM=-J\) one has \(|c|^2=1+|a|^2\).
In the positive-sign case one can arrange \(\tau(c/a)=0\) by constant conjugation preserving \(J\); in the negative-sign case one can arrange \(\tau(a/c)=0\).

For a proof, use the disk of matrices
\[
   C_z=(1-|z|^2)^{-1/2}
           \begin{pmatrix}1&-z\\-\bar z&1\end{pmatrix},\qquad |z|<1 .
\]
The top-left and bottom-left entries of \(C_z M C_z^{-1}\), respectively, are
\[
 a_z=\frac{(1+|z|^2)a+b\bar z-cz}{1-|z|^2},
 \qquad c_z=\frac{c-2a\bar z-b\bar z^2}{1-|z|^2}.
\]
Minimize the circle mean of \(\log|a_z|\) in the positive-sign case, or \(\log|c_z|\) in the negative-sign case.
The entries being logged have modulus at least one since \(C_z\) preserves \(J\).
At every boundary point \(\xi\), the numerator being used vanishes at that point for all \(y\) only if \(c(y)\xi^2-2a(y)\xi-b(y)=0\) for all \(y\).
This would give a common invariant line \(\mathbb C(\xi,1)^{\mathsf T}\), impossible since the numerator coefficients span the traceless matrices.
For each \(\xi\) the numerator therefore stays away from zero on a positive-length arc of \(y\)'s when \(z\) tends to \(\xi\).
The mean tends to infinity since the other logarithms are nonnegative.
The mean is continuous inside the disk and attains a minimum.
Every matrix in \(SU(1,1)\) has the form of a diagonal unitary times \(C_z\), by writing its first row as \((\alpha,\beta)\) with \(|\alpha|^2-|\beta|^2=1\) and \(z=-\beta/\alpha\).
Diagonal unitary conjugation fixes both moduli, so the minimizing basis minimizes over this entire group.
In this basis vary again by \(C_{tw}\) for real \(t\) near zero.
In the positive-sign case the derivative of the mean at zero is the mean of \(\operatorname{Re}((b\bar w-cw)/a)=-2\operatorname{Re}(w c/a)\).
In the negative-sign case it is the mean of \(-2\operatorname{Re}(\bar w a/c)\).
The differentiation is uniform on the compact circle since the denominators have modulus at least one there.
Vanishing for every \(w\) proves the two mean identities.

## Positive-sign scattering

Use \(M^*JM=J\) in the centered basis.
Writing \(M(u,v)^{\mathsf T}=(u',v')^{\mathsf T}\), solve for the positive-metric scattering matrix that maps \((u,v')\) to \((u',v)\):
\[
       S=\frac1a\begin{pmatrix}B&-b\\ c&-1\end{pmatrix},
       \qquad W=\operatorname{diag}(g^{-1},g)S(h).
\]
Here \(a^2+bc=B\), and the preserved form gives \(\|u\|^2+\|v'\|^2=\|u'\|^2+\|v\|^2\).
The finite numerical scattering matrix is unitary at every circle point, hence both \(S(h)\) and \(W\) are unitary in the regular algebra.
For \(\lambda=\pm1\), the substitution \((u,v)\mapsto(u,\lambda gv)\) identifies the eigenspace \(\ker(M(h)-\lambda gI)\) with \(\ker(W-\lambda I)\).
Indeed \(W(u,\lambda gv)^{\mathsf T}=\lambda(u,\lambda gv)^{\mathsf T}\) says \(u'=\lambda gu\) and the recovered second input is \(v\).
The actual sign on \(g\) fixing \(h\) gives both input eigenspaces dimension \(1/2\).

Write \(\operatorname{Tr}\) for \(\tau\) composed with ordinary two-coordinate trace.
In \(\operatorname{Tr}(W^2)\) the two squares of the diagonal entries have trace zero by the same-sign two-step formulas.
The off-diagonal terms contribute \(2\tau(-b/a)\tau(c/a)=0\) by centering.
The spectral measure of the unitary \(W^2\), normalized to mass one, has an atom of mass at least \(1/2\) at one, and its mean is zero.
Taking real parts forces the other half of the mass to lie at \(-1\).
Thus \(W^4=I\) by faithfulness.
This identity is in the matrix algebra of absolutely summable group coefficients: all factors lie there and the regular representation on that algebra is faithful by evaluation on the vector at the identity.
We may therefore apply every actual character of \(H\).

At a character \((x,y)\), the numerical unitary \(W(x,y)\) has determinant \(-1\) since \(\det S=(bc-B)/a^2=-1\).
If \(x^2\ne B(y)\), then \(M(y)\) has neither eigenvalue \(x\) nor \(-x\).
By the same scattering identity, \(W(x,y)\) has neither eigenvalue \(1\) nor \(-1\).
Its eigenvalues are fourth roots of unity, and determinant \(-1\) now forces it to equal \(iI\) or \(-iI\) by normality.
In particular \(b(y)=c(y)=0\).
Among \(y\in\mu_{10}\) at least four distinct values have \(y^4\ne B(y)\): the equation \(y^4q(y)=p(y)\) is a nonzero polynomial equation of degree six and \(q\) does not vanish on the circle.
Since \(x^2=y^4\) at the marked characters, both numerators of \(b,c\), of degrees at most two, vanish identically.
This contradicts independence of the numerator coefficients.

## Negative-sign scattering

Use \(M^*JM=-J\) in the centered basis.
Now the scattering matrix maps \((v,v')\) to \((u,u')\) and equals
\[
 S=\begin{pmatrix}A&P\\Q&A\end{pmatrix}
   =\frac1c\begin{pmatrix}a&1\\B&a\end{pmatrix}.
\]
It is pointwise unitary since the sign reversal gives \(\|v\|^2+\|v'\|^2=\|u\|^2+\|u'\|^2\).
Let \(J_g=\left(\begin{smallmatrix}0&g^{-1}\\g&0\end{smallmatrix}\right)\) and \(V=J_gS(h)^*J_gS(h)\), a product of two selfadjoint unitaries.
The \(\lambda\)-eigenspace of \(J_g\) consists of the graph pairs \((v,\lambda gv)\), for \(\lambda=\pm1\).
Within this graph the \(\lambda\)-eigenspace of \(S^*J_g S\) has dimension \(1/2\): the condition on the image graph is \(u'=\lambda gu\), while \(v'=\lambda gv\) holds on the input.
In detail the resulting maps between \((v,\lambda gv)\) and the original eigenvectors \((u,v)\) are bounded module maps inverse to one another, since \(u=c(h)^{-1}(\lambda g+a(h))v\).
The two graph subspaces are orthogonal for the two signs, so the \(+1\) eigenspace of \(V\) has dimension at least one.
Expanding the two diagonal entries gives
\[
 \operatorname{Tr}(V)=
 \tau(g^{-1}A^*g A)+\tau(g A^*g^{-1} A)
 +\tau(g^{-1}P^*g^{-1}Q)+\tau(g Q^*gP)=0 .
\]
Indeed the first two terms are \(|\tau A|^2=0\) and the other two are same-sign two-step traces.
The preceding unit-circle argument implies \(V^2=I\).
Thus \(J_g\) and \(S^*J_g S\) commute.
This absolutely summable identity again holds at every character.

At \((x,y)\) the positive graph of \(J_x\) is the line through \((1,x)\).
Commutation of the two numerical selfadjoint involutions makes this line an eigenspace for \(S(y)^*J_xS(y)\), so \(S(y)\) maps it onto the positive or the negative graph of \(J_x\).
The first alternative gives \(\det(M(y)-xI)=0\) by scattering, hence \(x^2=B(y)\).
The second gives \(\det(M(y)-\operatorname{diag}(-x,x))=0\), since \(v'=xv\) and \(u'=-xu\).
This equation is \(-B(y)-2a(y)x-x^2=0\).
If \(x^2\ne B(y)\), apply it at the two actual characters \((x,y),(-x,y)\).
It gives \(a(y)=0\) and \(x^2=-B(y)\).
It follows that \(B(y)^2=y^8\) at all ten values \(y\in\mu_{10}\).
But the remainder of \(p(y)^2-y^8q(y)^2\) modulo \(y^{10}-1\) is
\[
       -8+8y^2-4s_0y^3+4y^4-4y^8+4s_0 y^9 ,
\]
which is nonzero and has degree less than ten.
The contradiction exhausts the remaining signs and proves the character assertion by the sign-square reduction.

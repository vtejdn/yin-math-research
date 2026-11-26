---
author: Yin
---

# A Schur kernel boundary and two-sided multiplication by group-ring elements

For [A0001](../tasks/Yin_T_A0001_v1.md#contract), let \(A=\mathbb CG\) and let \(U\) be the algebra of affiliated operators in the regular representation.
Assume every nonzero scalar of \(A\) is a unit of \(U\).
Write \(M=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\), \(a\ne0\), \(y=ca^{-1}\), \(z=a^{-1}b\), \(S=d-yb\) and \(p\) for the orthogonal kernel projection of \(S\).
The calculations concern the possibility that \(S\ne0\) and \(p\ne0\).

## The four terms before word expansion

For \(f\in A\) put \(B_f(l,r)=lf\otimes r-l\otimes fr\) in \(U\otimes_{\mathbb C} U\).
Using \(ya=c,\ az=b,\ dp=czp\) gives
\[
 S\otimes p=B_d(1,p)-B_b(y,p)-B_c(1,zp)+B_a(y,zp).
\]
For a chosen group word \(w=g_1\cdots g_k\), expand \(B_w(l,r)\) as the sum of \(B_{g_i}(l g_1\cdots g_{i-1},g_{i+1}\cdots g_k r)\).
Extend linearly over the group support of each coefficient.
A negative generator contributes the negative of the corresponding positive-generator term with the two end factors translated by the inverse.
This gives the [finite-rank commutator boundary](../claims/Yin_C_A0131_v1.md#balancing-and-ordinary-finite-rank) after common regularization on the outside of the finitely many factors.
The rank-one tensor on the left is nonzero over \(\mathbb C\) when \(S,p\ne0\).

Keep every prefix of \(d,c\) based at \(1\) and of \(b,a\) based at \(y\), including initial and terminal vertices, in the first-coordinate space.
In the second-coordinate space keep every suffix of \(d,b\) acting on \(p\) and of \(c,a\) acting on \(zp\), again including the endpoints.
A local right map \(F\) on the first complex span is linear, takes its values in \(A\), and respects the indicated generator steps.
The equality of endpoints \(ya=c\) gives \(F(y)a=F(1)c\).
Writing \(u=F(1)\), this forces \(F(y)=uy\in A\), and every other prefix value is fixed by these two anchors.
Conversely any \(u\in A\) with \(uy\in A\) gives the local map by left multiplication, on all of \(A+yA\).
Thus the maps with nonzero first anchor are exactly the common left multiples \(uc=va\) with \(u\ne0,\ v\in A\).
For such a map \(uS=ud-vb\in A\), and \((uS)p=0\) would force \(S=0\).

A local left map on the second complex span respects left multiplication along the suffix steps.
Its anchor values \(k=F'(p)\), \(l=F'(zp)\) satisfy \(al=bk,\ cl=dk\).
Thus \(l=zk\) and \(Sk=0\).
If \(S\ne0\), a nonzero \(k\in A\) would be a unit, so both anchors and all suffix values vanish.
These restrictions use the specified full endpoint spans.
Collecting cancelling tensor terms, changing the realization or choosing a different tuple can change the spaces and their linear relations.
The derivation therefore gives no general obstruction to local maps for other witnesses.

## A certificate using both sides

For an input of size two, a simpler constant change of row and column already gives integral rank whenever the union of the group supports of all entries has at most three elements.
Write \(M=A_0g_0+A_1g_1+A_2g_2\) with complex coefficient matrices, allowing zeros to pad shorter lists.
Choose a nonzero \(v\in\mathbb C^2\) at which \(\det[A_1v,A_2v]=0\).
Such a vector exists because this is a homogeneous quadratic in two complex coordinates, including the case of the zero polynomial.
A nonzero row \(u\) annihilates both columns, so \(uMv\) is zero or a single nonzero group monomial.
Complete \(u,v\) to invertible constant row and column changes making this entry the first pivot.
If it is a monomial, the Schur complement remains in the original group ring, so scalar injectivity computes its rank.
If it vanishes, a permutation makes the matrix triangular. When both diagonal entries are nonzero they are affiliated units. When either vanishes the matrix has rank zero or one by a nonzero scalar entry or vanishing of all entries.
This argument settles three group elements with unrestricted coefficient matrices, whereas the [half-rank cost bound](../claims/Yin_C_A0168_v2.md#free-shortened-subgroup-and-three-labels) also covers some four-element supports.

If some \(u,v\in A\setminus\{0\}\) satisfy \(uSv\in A\), then \(S=0\) or \(S\) is an affiliated unit.
Indeed left and right multiplication by the units \(u,v\) preserves the regular rank.
In particular a group-ring certificate is
\[
 a=hk,\qquad uc=l k,\qquad bv=h m,\qquad h,k,l,m\in A .
\]
Here \(h,k\ne0\), and evaluating the single inverse as \(a^{-1}=k^{-1}h^{-1}\) gives \(uSv=udv-lm\).
The two factors on the outside of \(S\) can clear its product while each canonical prefix or suffix construction still has no nonzero polynomial map.

For a comparison with the [polynomial zero-pair criterion](../claims/Yin_C_A0113_v1.md#two-integral-ranks-with-no-finite-zero-pair), let \(G=F(x,y)\times\langle t\rangle\), \(r=(x-1,y-1)\), \(w=r^*\) and take \(M=wr+tE_{22}\), where \(E_{22}\) is the constant second diagonal matrix unit.
For nonzero group-ring rows \(U_0\) and columns \(V_0\), their lowest Laurent coefficients in \(t\), say \(U_i,V_j\), have \(U_iw\ne0\) and \(rV_j\ne0\).
This follows by the finite-chain leaf argument on the free-group tree and its adjoint.
The coefficient of degree \(i+j\) in \(U_0MV_0\) is their nonzero product, so this matrix admits no polynomial zero pair.
Nevertheless its entries satisfy \(a=w_1r_1,\ c=w_2r_1,\ b=w_1r_2\) and \(d=w_2r_2+t\).
The preceding certificate gives \(S=t\) with \(u=v=1\).
Clearing \(ca^{-1}\) on the left or \(a^{-1}b\) on the right by one nonzero polynomial multiplier would give a row or column combination of the original matrix vanishing at its first coordinate, which the zero-pair test excludes here.
This example establishes a distinction from the zero-pair test even when the Schur scalar itself lies in the group ring.

## A scalar for which both outside multipliers are essential

Work in \(A=\mathbb C F(x,y)\) and put \(k=x-2,\ f=x-3,\ h=y-2,\ m=y-3\).
The matrix \(a=hk,\ b=m,\ c=f,\ d=0\) has
\[
 S=-(f/k)(m/h),\qquad k S h=-fm .
\]
Each displayed ratio is computed in the bounded functions of its own cyclic generator and is a bounded unit, since the denominators and numerators have no zero on the circle.

Suppose \(U_0(f/k)(m/h)=W\) with \(U_0,W\in A\).
Then \(E=U_0(f/k)=W(h/m)\) has Fourier support in a finite union of left cosets of \(\langle x\rangle\) and in a finite union of left cosets of \(\langle y\rangle\).
Each pair of these cosets intersects in at most one point, hence \(E\in A\).
Grouping \(Ek=U_0 f\) by the left cosets of \(\langle x\rangle\) and using coprimality of \(k,f\) in the cyclic Laurent ring gives \(E\in A f\).
Grouping \(E m=W h\) by the left cosets of \(\langle y\rangle\) similarly gives \(E\in A h\).
The intersection \(A f\cap A h\) is zero.
Indeed a relation \(L(x-3)+N(y-2)=0\) assigns a finite chain of weighted oriented edges to the free-group Cayley tree, with the two endpoint coefficients of each occupied edge both nonzero.
A leaf of the finite supporting forest contradicts such a relation.
Consequently \(E=U_0=0\).

For right multiplication the same argument starts with \(E'=(m/h)V_0=(k/f)W\) if \((f/k)(m/h)V_0=W\).
Finite unions of right cosets imply \(E'\in A\).
Coprimality on the two cyclic subgroups gives \(E'\in mA\cap kA=0\), by the left Cayley tree leaf argument.
Hence \(V_0=0\).
Thus two outside multipliers can be necessary for a Schur scalar even on a free group.
This comparison tests single-sided scalar clearing. The preceding central-variable matrix tests the absence of a polynomial zero pair.
Neither comparison establishes that a two-sided certificate exists in general.

---
author: Yin
---

# A scalar character detects a strict first-inverse rank drop at the order-twenty marking

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free and suppose every nonzero \(\mathbb CH\)-scalar acts injectively in the regular representation.
Suppose \(K=P(t)-sQ(t)\), with \(P(z)=Az+B,\ Q(z)=Cz+D\) complex two-square pencils, has regular nullity \(1/2\) for unnormalized matrix trace.
Assume \(H\) has a marked quotient \(C_5\times C_2^2\) whose characters on \((s,t)\) take the values \((\epsilon z,\eta z^2)\) for \(z^5=1\) and independent signs \(\epsilon,\eta\).
This includes the [remaining noncyclic marking of order twenty](Yin_C_A0311_v1.md#the-noncyclic-quotient-of-order-twenty) after the permitted symmetries.
One of the two sign directions has a character at which the corresponding signed pair of pencils are both invertible.
For that direction the signed direct sum has inner rank four over \(\mathbb CH\) and exactly three after adjoining one actual group-ring scalar inverse.

Let \(F\) be the index-two kernel of this sign.
There is a matrix \(R\in M_2(\mathbb CF)\) on at most eight specified group elements with inner rank two over \(\mathbb CF\) and regular rank one.
A scalar character of \(F\) sees \(R\) as invertible.
For each entry \(a\) with nonzero value at this character the inner rank is exactly one inside \(U(F)\) after adjoining \(a^{-1}\) alone.
The map from the universal algebra adjoining this same inverse to its actual image in \(U(F)\) has an explicit nonzero kernel element.
The assertions concern consequences of a hypothetical half kernel.

## Adjacent nonzero values on the five sign squares

For a nonzero complex polynomial \(f(x,y)\) of bidegree at most \((2,2)\), two adjacent vertices of at least one of the five sign squares above give nonzero values.
Otherwise each square has two opposite zeros, which can be written as \((z,\tau_z z^2),(-z,-\tau_z z^2)\) with \(\tau_z=\pm1\).
The parts of \(f\) of even and odd total degree must both vanish on the first point in each pair.
The monomials \(1,x^2,y^2,x^2 y^2,xy\) give the even equation
\[
             a+bz^2+cz^4+dz+e\tau_z z^3=0 .
\]
Multiplication by \(z^{-3}\) and summation over the fifth roots gives \(e\sum_z\tau_z=0\).
The sum of five signs is nonzero, so \(e=0\), and independence of four cyclic characters forces \(a=b=c=d=0\).
The odd monomials \(x,xy^2,y,x^2y\) give \(uz+v+\tau_z(wz^2+kz^4)=0\).
Squaring the equality after moving one summand across yields
\[
             v^2+(2uv-2wk)z+u^2z^2-k^2z^3-w^2z^4=0 .
\]
All five coefficients vanish, so \(u=v=w=k=0\), a contradiction.

Take \(f(x,y)=\det(P(y)-xQ(y))\).
It is nonzero since its leading coefficient in \(x\) is \(\det Q(y)\), nonzero by the [regular-pencil reduction](Yin_C_A0184_v1.md#singular-cyclic-blocks).
Use the orientation \((g,h)=(s,t)\) for an edge changing \(x\).
For an edge changing \(y\) take the adjoint, with \((g,h)=(t^{-1},s^{-1})\) and pencils \(B^*-D^*z,\ C^*z-A^*\).
Indeed the resulting rectangle is exactly \(K^*\), and specialization at a unitary character conjugate-transposes the original matrix.
The same regular-pencil reduction and [invertible assembly](Yin_C_A0184_v1.md#statement) apply to the oriented rectangle.
Write \(P,Q\) for its pencils and \(f\) for their determinant as above.
There is now an actual character \(\chi\) with \(x=\chi(g),\ y=\chi(h)\) and \(f(x,y)f(-x,y)\ne0\).
The two signed matrices each have nullity \(1/2\) by the sign twist and by equality of nullities of a square matrix and its adjoint.
Their direct sum has numerical rank four at \(\chi\), so its group-ring inner rank is four.
The [simultaneous signed-kernel factorization](Yin_C_A0330_v1.md#the-common-kernel-coordinate-and-the-inner-rank) gives inner rank three over one actual scalar inverse.

## An eight-label matrix on the actual sign subgroup

Write \(T=\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\) for the oriented assembly and \(T^{-1}=\left(\begin{smallmatrix}E&F_0\\J&L\end{smallmatrix}\right)\).
For \(D_L(z)=E-zJ,\ N_L(z)=zL-F_0\), the [left-denominator identity](Yin_C_A0304_v1.md#a-bounded-left-inverse-for-the-two-outer-polynomial-pencils) gives \(D_LP=N_LQ\).
In addition \(\det D_L(z)=\det Q(z)/\det T\).
Indeed left multiplication of \(\left(\begin{smallmatrix}P(z)&I\\Q(z)&0\end{smallmatrix}\right)\) by \(T^{-1}\) gives \(\left(\begin{smallmatrix}zI&E\\I&J\end{smallmatrix}\right)\).
Subtract \(z\) times the lower block row from the upper one and compare the determinants by block swaps.
Put \(h_1=ghg^{-1},\ U=g^{-1}P(h)Q(h)^{-1}\).
The matrix
\[
 R=N_L(h_1)P(h)-D_L(h_1)g^2Q(h)
   =D_L(h_1)g^2(U^2-I)Q(h)
\]
is supported on \(h_1^i h^j,\ h_1^i g^2h^j\) for \(i,j\in\{0,1\}\), all in \(F\).
The identity follows from \(g^2 U^2Q(h)=(PQ^{-1})(h_1)P(h)\).
The exterior factors are affiliated units since \(g,h\) have infinite order and the two one-variable determinants are regular.
The kernel of \(U^2-I\) splits as the direct sum of the \(+1,-1\) eigenspaces by the two linear interpolation polynomials.
Each has dimension \(1/2\) by the invertible coordinate \(Q(h)\).
Thus \(R\) has regular rank one, also over \(F\) by the trace-preserving inclusion on subgroup elements.

Evaluate the two-pencil formula for \(R\) at commuting numerical \(x,y\), substituting \(h_1=h=y,\ g^2=x^2\).
For \(\det Q(y)\ne0\), put \(M=P(y)Q(y)^{-1}\).
Then \(R(x,y)=D_L(y)(M^2-x^2I)Q(y)\), so
\[
               \det R(x,y)=\frac{f(x,y)f(-x,y)}{\det T}.
\]
Both sides are polynomials, hence this holds at every \(x,y\), including the roots of \(\det Q\).
The chosen character restricts to a character \(\psi\) on \(F\) with \(\det\psi(R)\ne0\).
Consequently every group-ring factorization of \(R\) needs at least two columns.

## A character that fails to extend across one actual inverse

Permute rows and columns of \(R\) to put an entry \(a\) with \(\psi(a)\ne0\) in the upper left and write the other entries as \(b,c,d\) in row order.
The scalar hypothesis passes to \(F\), so \(a\) is an affiliated unit.
Elimination over \(U(F)\) gives \(d-ca^{-1}b=0\) because \(R\) has regular rank one and the pivot already has rank one.
Thus \(R=\binom{a}{c}(1,\ a^{-1}b)\) after the permutations, an inner factorization of rank one in the actual ring \(\mathbb CF[a^{-1}]\subset U(F)\).
In the universal ring \(\mathbb CF\langle X\rangle/(aX=Xa=1)\), the character extends by \(X\mapsto\psi(a)^{-1}\).
There \(d-cXb\) has value \(\det\psi(R)/\psi(a)\ne0\), taking the determinant after the chosen permutations.
This element maps to zero in the actual ring.
In particular \(\psi\) cannot extend to that ring, although it is nonzero at the denominator.

For any nonzero constant row and column \(u,v\), the scalar \(uRv\) can be put in the pivot position by constant changes of bases.
If it were a unit in \(\ell^1(F)\), its value under \(\psi\) would be nonzero and \(\psi\) would extend across its actual inverse by the bounded character on \(\ell^1(F)\).
The contradiction excludes every such unit.
In particular no scalar compression can have one collected group coefficient strictly larger in modulus than the sum of all others, since the geometric series would invert that compression in \(\ell^1(F)\).

## Assessment history

### Decision a-strict-first-inverse-rank-drop-at-order-twenty

| Field | Value |
| --- | --- |
| date | 2026-11-26T17:52 |
| status | proved |
| reason | A true edge character forces full group-ring inner rank while the actual affiliated factorization uses a single scalar inverse. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The signed four-square and subgroup two-square rank drops. |
| argument | [Adjacent nonzero values on the five sign squares](#adjacent-nonzero-values-on-the-five-sign-squares) | The five-character interpolation and the adjoint orientation. |
| argument | [An eight-label matrix on the actual sign subgroup](#an-eight-label-matrix-on-the-actual-sign-subgroup) | The polynomial determinant and the regular rank. |
| argument | [A character that fails to extend across one actual inverse](#a-character-that-fails-to-extend-across-one-actual-inverse) | The two distinct localization maps and the compression test. |
| review | [A strict first-inverse rank drop at order twenty](../audits/reviews/Yin_R_A0230_v1.md#a-strict-first-inverse-rank-drop-at-order-twenty) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-a-strict-first-inverse-rank-drop-at-order-twenty)

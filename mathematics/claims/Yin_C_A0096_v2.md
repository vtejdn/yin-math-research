---
author: Yin
---
# Single-parameter coefficient transfer with a degree bound

This version sharpens the single-parameter case of the [finite direct-power coefficient transfer](Yin_C_A0096_v1.md#a-bound-for-the-direct-power-needed-by-a-prescribed-size).
It also specifies classes for which the square \(G^2\) alone suffices.
The signed zero-product constructions and the all-arity equivalences remain in [v1](Yin_C_A0096_v1.md#statement).
No assertion that \(G^2\) suffices for every matrix polynomial of arbitrary degree is made here.

## Statement

Let \(G\) be torsion-free.
Rational Atiyah on a group means integral regular rank for every finite rectangular matrix over its rational group ring, with the unnormalized matrix trace.
Assume first rational Atiyah on \(G\), and let
\[
 D=\operatorname{Div}_{U(G)}(\mathbb Q[G]).
\]
The [division-closure criterion used in v1](Yin_C_A0096_v1.md#alternation-in-actual-affiliated-rings) makes \(D\) a division ring in the actual affiliated algebra.
Ranks of affiliated matrices below mean the traces of their range projections; they agree with the usual regular ranks for bounded group-ring matrices.
The formal variable \(T\) is central.

Let
\[
 P(T)\in M_{m,n}(D[T]),\qquad \deg P\le h,\qquad
 r=\operatorname{rank}_{D(T)}P,
 \tag{1}
\]
Here \(m,n\) are positive integers, \(h\) is a nonnegative integer, and \(D(T)\) is the formal division ring of fractions of \(D[T]\).
If rational Atiyah holds on \(G^{rh+1}\), then for every \(\lambda\in\mathbb C\)
\[
 \operatorname{rk}_G P(\lambda)\in\{0,1,\ldots,r\}.
 \tag{2}
\]
The rank equals \(r\) outside a set of at most \(rh\) complex parameters.
Thus rational Atiyah on \(G^{\min(m,n)h+1}\) is a uniform sufficient hypothesis before the generic rank is computed.
The cases \(r=0\) and \(h=0\) require only the original rational hypothesis on \(G\).
The conclusion includes every singular parameter, not only generic evaluations.

Under rational Atiyah on \(G^2\), the following further conclusions hold.

1. Every \(x\in D\) is either a scalar multiple of the identity or has no complex point spectrum.
   Consequently every nonzero element \(a+\lambda b\), with \(a,b\in D\) and \(\lambda\in\mathbb C\), is an affiliated unit.
2. For a nonscalar \(x\in D\), evaluation embeds the field \(\mathbb C(T)\) into \(U(G)\) by \(T\mapsto x\).
   Every finite rectangular matrix over this actual field \(\mathbb C(x)\) has integer affiliated rank.
   This covers arbitrary matrix rational functions of one such element, with arbitrary complex scalar coefficients.
3. If \(A,B\in M_{m,n}(D)\), \(\operatorname{rank}_D B\le1\), and \(q(T)\in\mathbb C[T]\) is any polynomial, then
   \[
   \operatorname{rk}_G\bigl(A+q(\lambda)B\bigr)\in\mathbb Z
   \quad\text{for every }\lambda\in\mathbb C.
   \tag{3}
   \]
   Neither the matrix size nor the degree of \(q\) is restricted.
4. More generally, take a polynomial diagonal form of \(P(T)\) over \(D[T]\).
   If each nonzero diagonal polynomial factors in \(D[T]\) into polynomials whose coefficient lists have complex linear span of dimension at most two in \(U(G)\), then (2) follows already from the square hypothesis.
   A factorization into degree-one polynomials is a sufficient special case.
   The factorization or coefficient-span certificate is an additional input, not a consequence of rational Atiyah.

The square hypothesis supplies the rational hypothesis on \(G\) by coordinate inclusion.
None of these statements identifies \(D\cap\mathbb C\) with \(\mathbb Q\).

## Argument

### The square test for a scalar affiliated element

Write \(D_2\) for the division closure of \(\mathbb Q[G^2]\) in \(U(G^2)\).
Under rational Atiyah on \(G^2\), it is a division ring.
Both coordinate copies of \(D\) lie in \(D_2\), with their actual inverses, by the [coordinate-affiliation interface in v1](Yin_C_A0096_v1.md#alternation-in-actual-affiliated-rings).
For \(x\in D\), consider
\[
 \Delta_x=x\otimes1-1\otimes x\in D_2.
 \tag{4}
\]
Its vanishing implies that \(x\) is a complex scalar.
Indeed put \(c=(1+xx^*)^{-1/2}\), a bounded affiliated unit for which \(cx\) is bounded.
Left multiplication of (4) by \(c\otimes c\) gives
\[
 (cx)\otimes c=c\otimes(cx).
 \tag{5}
\]
Apply the bounded operators to the identity vector in the Hilbert tensor product.
For two Hilbert-space vectors \(v,w\), with \(w\ne0\), the equality \(v\otimes w=w\otimes v\) implies \(v=\alpha w\) for a scalar \(\alpha\).
This follows, for example, by applying to the second coordinate a continuous linear functional that takes value one on \(w\).
The faithful \(L^2\) representation therefore gives \(cx=\alpha c\), and cancellation in the affiliated algebra gives \(x=\alpha I\).
The converse is immediate.

If \(x\) is nonscalar and \(e=P_{\ker(x-\lambda)}\), then
\[
 \Delta_x(e\otimes e)=0.
 \tag{6}
\]
Here \((x-\lambda)e=0\) is an affiliated identity, so the tensor calculation uses the stated closed-product convention.
The nonzero \(\Delta_x\) is a unit in \(D_2\).
Thus \(e\otimes e=0\), and its product trace \(\tau(e)^2\) forces \(e=0\).
In a finite tracial algebra, an affiliated operator with zero kernel has dense range and an affiliated inverse.
This proves the point-spectrum assertion.

For \(a+\lambda b\), the case \(b=0\) uses the division property of \(D\).
Otherwise
\[
 a+\lambda b=b(b^{-1}a+\lambda).
 \tag{7}
\]
The last factor is either zero or a unit by the preceding assertion, including when \(b^{-1}a\) is scalar.
This also treats every complex linear combination of a list of at most two elements of \(D\).

### One rational affiliated generator

Let \(x\in D\) be nonscalar.
For every nonzero polynomial \(f\in\mathbb C[T]\), scalar factorization gives
\[
 f(x)=c\prod_{j=1}^d(x-\lambda_j),\qquad c\ne0.
 \tag{8}
\]
Every factor is an affiliated unit by the square test.
In particular \(f(x)\ne0\), so evaluation on \(\mathbb C[T]\) is injective.
These evaluated polynomials commute, and their nonzero inverses commute with them.
Evaluation therefore embeds \(\mathbb C(T)\) as a commutative division subring of \(U(G)\).
Gaussian operations over this field reduce every finite matrix over it to an identity block and zero blocks.
The same operations are actual invertible affiliated operations, so the regular rank is the size of that identity block.
If \(x\) is scalar instead, every defined matrix rational function of \(x\) is an ordinary complex matrix and also has integer rank.
This proof does not cover expressions using additional independent elements such as \(x^*\) unless they already belong to \(\mathbb C(x)\).

### Polynomial diagonalization over the central variable

Set \(R=D[T]\) and \(F=D(T)\).
The ring \(R\) admits both left and right Euclidean division by degree: the leading coefficient of every nonzero polynomial is a unit of \(D\), and \(T\) commutes with it.
In particular \(R\) is an Ore domain and its left and right fraction constructions give \(F\).
For the needed diagonalization, one can work directly with the Euclidean algorithm.

Move a nonzero entry of a nonzero matrix to the first position.
If an entry in its column has a nonzero remainder on left division by the pivot, a row subtraction and interchange replace the pivot by one of strictly smaller degree.
Right division and column operations do the same for entries in its row.
There can be only finitely many strict decreases in the pivot degree.
When the remainders vanish, clear the pivot column and row by polynomial elementary operations.
Continue on the remaining submatrix.
This produces polynomial matrices with polynomial inverses,
\[
 U\in\operatorname{GL}_m(R),\qquad V\in\operatorname{GL}_n(R),
 \qquad
 UPV=\operatorname{diag}(f_1,\ldots,f_r,0),
 \tag{9}
\]
where each \(f_i\ne0\).
The number of nonzero diagonal entries is the fraction-field rank \(r\).
No commutative determinant or divisibility ordering among the \(f_i\) is being used.

Regard \(P:R^n\to R^m\) as a map of right \(R\)-modules.
Right division by a nonzero \(f\) gives
\[
 \dim_D(R/fR)=\deg f.
 \tag{10}
\]
Indeed representatives of degree strictly smaller than \(\deg f\) give a right \(D\)-basis, and their independence follows by the degree of a nonzero product \(fg\).
The diagonal form consequently identifies the right \(D\)-dimension of the torsion submodule of \(\operatorname{coker}P\) as
\[
 \dim_D\operatorname{tors}(\operatorname{coker}P)
 =\sum_{i=1}^r\deg f_i.
 \tag{11}
\]
The other summand is the free right \(R\)-module \(R^{m-r}\).

### The degree bound without a determinant

Suppose \(r>0\).
Let \(\mathcal V=\operatorname{im}(P:F^n\to F^m)\), and choose \(r\) coordinate rows for which the projection
\(\pi:F^m\to F^r\) is injective on \(\mathcal V\).
Such rows exist by finite-dimensional row and column elimination over the division ring \(F\).
Choose \(r\) columns of \(\pi P\) giving a square matrix
\[
 B(T)\in M_r(R),\qquad \deg B\le h,
 \tag{12}
\]
invertible over \(F\).

The torsion classes in \(R^m/\operatorname{im}P\) are exactly the classes represented by \(\mathcal V\cap R^m\).
One implication follows by multiplying a torsion equation by the inverse of its nonzero annihilating polynomial in \(F\).
For the other, write a vector in \(\mathcal V\cap R^m\) as \(Py\), \(y\in F^n\), and use a common right Ore denominator to put \(ys\in R^n\) for a nonzero \(s\in R\).
Its class is then killed on the right by \(s\).

The map induced by \(\pi\) restricts to an injection
\[
 \operatorname{tors}(\operatorname{coker}P)
 \longrightarrow \operatorname{coker}(\pi P).
 \tag{13}
\]
To check this, take \(x\in\mathcal V\cap R^m\) whose image is zero.
There is \(y\in R^n\) with \(\pi x=\pi Py\).
Both \(x\) and \(Py\) lie in \(\mathcal V\), so injectivity of \(\pi|_{\mathcal V}\) gives \(x=Py\).
Since the selected columns of \(B\) are columns of \(\pi P\), there is also a surjection
\[
 \operatorname{coker}B\longrightarrow\operatorname{coker}(\pi P).
 \tag{14}
\]

For \(k\ge0\), let \(R_{\le k}\) denote the right \(D\)-space of polynomials of degree at most \(k\).
Multiplication by \(B\) is injective and maps \(R_{\le k}^r\) into \(R_{\le k+h}^r\).
The image has dimension \(r(k+1)\), whereas the target has dimension \(r(k+h+1)\).
It follows that the image of \(R_{\le k+h}^r\) in \(\operatorname{coker}B\) has dimension at most \(rh\).
These images increase and exhaust the cokernel.
Therefore
\[
 \dim_D\operatorname{coker}B\le rh,\qquad
 \sum_{i=1}^r\deg f_i\le rh.
 \tag{15}
\]
The last inequality follows from (11)--(14).
This estimate uses the degrees of the original selected submatrix, not the possibly larger degrees of its elementary reduction matrices.

### Specialization at every complex parameter

Assume rational Atiyah on \(G^J\), where \(J=rh+1\).
It holds on each coordinate subgroup \(G^j\), \(1\le j\le J\), with the same regular trace.
The [alternating tensor test of v1](Yin_C_A0096_v1.md#alternation-in-actual-affiliated-rings) says that every nonzero complex linear combination of at most \(J\) elements of \(D\) is an affiliated unit.
A dependent coefficient list is reduced to a complex basis from that same list.

For every \(\lambda\in\mathbb C\), the value \(f_i(\lambda)\) is a complex linear combination of at most \(\deg f_i+1\le rh+1\) elements of \(D\).
It is therefore either zero or a unit.
Evaluation is a ring homomorphism \(R\to U(G)\), since \(\lambda\) is central.
The polynomial inverses of \(U,V\) in (9) evaluate to actual affiliated inverses at every parameter.
Thus
\[
 \operatorname{rk}_G P(\lambda)
 =\#\{i:f_i(\lambda)\ne0\}.
 \tag{16}
\]
This proves (2), including at exceptional parameters.

A nonzero degree-\(d\) polynomial with coefficients in the complex vector space \(U(G)\) can vanish at at most \(d\) distinct scalar parameters.
Otherwise the scalar Vandermonde equations force every coefficient to vanish.
Combining this fact with (15)--(16) proves the bound \(rh\) for the set where the rank is smaller than \(r\).
If \(r=0\), the original matrix is zero because \(R\) embeds in \(F\).
If \(h=0\), it is already a matrix over \(D\), with rank \(r\) at every parameter.
These observations establish the stated degenerate cases.

Under rational Atiyah on \(G^2\), the same specialization argument works whenever each \(f_i\) has the factorization in assertion 4.
The square test makes each evaluated factor either zero or a unit.
Evaluation preserves the order of factors, and their product is consequently zero or a unit.
This proves that assertion without assuming that general polynomials over \(D\) split into linear factors.

### A rank-one parameter channel of arbitrary degree

Assume rational Atiyah on \(G^2\).
It suffices to treat \(A+sB\) for an arbitrary \(s\in\mathbb C\).
For \(B=0\) the result is immediate, so write \(B=uv\) with a nonzero column \(u\) and nonzero row \(v\) over \(D\).
Reduce \(A\), using invertible matrices over \(D\), to a rectangular identity block of size \(r=\operatorname{rank}_D A\) padded by zeros.
Apply the same changes to \(u,v\), and write them as
\[
 u=\binom{u_1}{u_0},\qquad v=(v_1\ v_0),
 \tag{17}
\]
according to the identity block and its complementary rows and columns.
An empty complementary block counts as zero.
For \(s=0\) the rank is \(r\).

Suppose \(s\ne0\).
If \(u_0\ne0\) and \(v_0\ne0\), operations over \(D\) on the complementary coordinates put each into its first coordinate with coefficient one.
After discarding zero complementary rows and columns, the active matrix is
\[
 \begin{pmatrix}
 I_r+s u_1v_1&s u_1\\
 s v_1&s
 \end{pmatrix}.
 \tag{18}
\]
Subtract \(u_1\) times its last row from the first \(r\) rows, and then subtract \(s v_1\) times those rows from its last row.
This gives \(\operatorname{diag}(I_r,s)\), of rank \(r+1\).

If \(u_0\ne0\) and \(v_0=0\), the corresponding active matrix is
\(\binom{I_r+s u_1v_1}{s v_1}\).
Subtracting \(u_1\) times the last row gives an identity block and hence rank \(r\).
The case \(u_0=0,\ v_0\ne0\) follows by the analogous column operation on
\((I_r+s u_1v_1\ \ s u_1)\).

If \(u_0=v_0=0\), the only nonzero block is \(I_r+s u_1v_1\).
The two Schur eliminations of
\[
 \begin{pmatrix}I_r&u_1\\-s v_1&1\end{pmatrix}
\]
give the exact rank identity
\[
 \operatorname{rk}(I_r+s u_1v_1)+1
 =r+\operatorname{rk}(1+s v_1u_1).
 \tag{19}
\]
The scalar on the right is either zero or a unit by the square test.
The rank is therefore \(r-1\) or \(r\).
All operations used are invertible in the actual affiliated algebra.
This proves (3) on substituting \(s=q(\lambda)\), for every degree and every complex parameter.

### Why an arbitrary companion matrix is not covered by the scalar square test

Consider, already in the bounded monic case,
\[
 P(T)=T^hI_n+A_{h-1}T^{h-1}+\cdots+A_0,\qquad
 A_j\in M_n(\mathbb Q[G]),\qquad h\ge1.
 \tag{20}
\]
Its usual companion \(C\in M_{hn}(\mathbb Q[G])\) has identity blocks on the superdiagonal and last row
\((-A_0,\ldots,-A_{h-1})\).
At a scalar \(\lambda\), the bounded map
\[
 \xi\longmapsto(\xi,\lambda\xi,\ldots,\lambda^{h-1}\xi)
 \tag{21}
\]
is an isomorphism from \(\ker P(\lambda)\) onto \(\ker(C-\lambda I)\), with inverse the first coordinate.
It preserves their regular dimensions; there is no factor of \(h\) in this unnormalized nullity identity.

However, the tensor difference of \(C\) is a matrix over \(D_2\), not an element of the division ring \(D_2\).
A nonzero matrix over a division ring can have a kernel.
For example, the constant companion
\[
 C=\begin{pmatrix}0&2\\1&0\end{pmatrix}
\]
has eigenvalues \(\pm\sqrt2\), and \(C\otimes I_2-I_2\otimes C\) is a nonzero rational matrix with a two-dimensional kernel.
Cyclicity of this companion does not change that fact.
Thus (4)--(6) cannot be applied to a general companion by calling it a scalar rational affiliated element.

Even a normal-operator trace identity alone leaves room for fractional eigenvalue masses.
For a selfadjoint affiliated matrix \(C\) with unnormalized spectral measure \(\mu\), the spectral theorem gives
\[
 \operatorname{Tr}\bigl(P_{\ker(C\otimes I-I\otimes C)}\bigr)
 =(\mu\otimes\mu)\{(s,t):s=t\}
 =\sum_\lambda\mu(\{\lambda\})^2.
 \tag{22}
\]
A numerical list of four masses \(1/2\) has total mass two and squared sum one.
Both numbers are integers, although the individual masses are fractional.
This is the same type of moment limitation recorded in [C97](Yin_C_A0097_v1.md#argument).
It is a numerical or operator-probability calibration, not an exhibited rational group-ring matrix or companion satisfying all the square hypotheses.
It pinpoints why integrality of the tensor-difference rank, by itself, does not prove integrality of each spectral mass.

The degree-bound proof instead controls the scalar polynomials left by genuine polynomial row and column operations.
The additional factorization and rank-one-channel assertions specify when those scalar tests can be completed using two group coordinates.
Their hypotheses have not been established for arbitrary matrix polynomials.

## Assessment history

### Decision univariate-degree

| Field | Value |
| --- | --- |
| date | 2026-11-21T05:07 |
| status | proved |
| reason | The independent inspection verifies the stated deductions and the applicability of the identified inputs at the recorded scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A degree and generic-rank bound for all complex parameters and the four square cases. |
| argument | [Proof](#argument) | Right polynomial modules, evaluation in the affiliated algebra, the square tests and companion comparisons. |
| review | [Whole finding](../audits/reviews/Yin_R_A0132_v2.md#whole-finding) | Full inspection with its stated dependency and example limits. |

## Current assessment

[Selected decision](#decision-univariate-degree)

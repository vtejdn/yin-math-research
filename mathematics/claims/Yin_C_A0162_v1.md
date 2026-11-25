---
author: Yin
---

# Rational specializations of maximal rank and a pencil singular at every algebraic number

## Statement

Let \(G\) be a finitely generated discrete group, let \(U_G\) be its ring of affiliated operators, and write \(D_k(G)\) for the division closure of \(kG\) in \(U_G\).
Use the canonical group trace and the unnormalized matrix trace for ranks.
Suppose that applying any automorphism of \(\mathbb C\) fixing \(\mathbb Q\) to the coefficients of a complex group-ring matrix preserves its rank.
This hypothesis holds for sofic \(G\). [Coefficient invariance](Yin_C_A0159_v1.md#a-field-controlling-ranks)

Assume that for every \(m\) and every rectangular matrix \(P(z)\) over \((\mathbb QG)[z_1,\ldots,z_m]\) in commuting variables, some \(q\in\mathbb Q^m\) attains the maximum of \(\operatorname{rk}_G P(z)\) over \(\mathbb C^m\).
Then the following are equivalent.

1. \(D_{\mathbb C}(G)\) is von Neumann regular.
2. \(D_{\mathbb Q}(G)\) is von Neumann regular.
3. Every rectangular matrix \(X\) over \(\mathbb ZG\) has a matrix \(Y\) over \(D_{\mathbb Q}(G)\) with \(XYX=X\).

Thus, under rational attainment of these maxima, the central group generators in the [countable coefficient test](Yin_C_A0159_v1.md#statement) can all be omitted.
For torsion-free \(G\) this gives a test for sufficiency of the [unrestricted finite-rank equation](../tasks/Yin_T_A0003_v3.md#contract).
It suffices for rational attainment that, for each fixed \(P\), its ranks at rational points strictly below its complex maximum stay a positive distance from that maximum.
In particular it suffices that for each \(P\) there is an integer \(d\ge1\) with \(\operatorname{rk}_G P(q)\in d^{-1}\mathbb Z\) for all \(q\in\mathbb Q^m\).
The gap or denominator may depend on the entire polynomial matrix.

For an individual \(X\) over \(\mathbb QG\), suppose an inner inverse has a realization \(Y=\alpha(t)L(t)^{-1}\beta(t)\) over the group algebra with coefficients in \(\mathbb Q(t_1,\ldots,t_m)\), for algebraically independent real \(t_i\).
Then descent of this realization to \(\mathbb Q\) needs rational attainment only for its square pivot \(L\), after clearing scalar denominators as below.
This restriction on specialization already has content for the ordinary group trace of a finitely generated amenable group.
For \(H=(C_2^3)\wr\mathbb Z\) there exist \(A,B\in M_2(\mathbb ZH)\) such that
\[
 A+\lambda B\text{ is invertible in }M_2(U_H)
 \quad\Longleftrightarrow\quad
 \lambda\text{ is transcendental over }\mathbb Q .
\]
The same pencil is an affiliated unit when its parameter is a new central infinite cyclic generator.
This example concerns specialization of a fixed pivot in a group with torsion.
It leaves open the existence of other inner inverses and the deletion question for torsion-free groups.

## Argument

### Rational attainment and descent of an inner inverse

For each \(P\) in the statement, every rank sublevel is [Zariski closed](Yin_C_A0128_v1.md#statement).
Hence its complex maximum \(R\) is also the supremum over \(\mathbb Q^m\), by Zariski density.
If every rank below \(R\) at a rational point is at most \(R-\delta\) for some \(\delta>0\), this proper closed sublevel cannot contain all rational points.
Uniformly bounded denominators give only finitely many possible rational-point ranks since the matrix size bounds the rank.

Choose algebraically independent real numbers \(t_1,t_2,\ldots\) and let \(K=\mathbb Q(t_1,t_2,\ldots)\).
Every polynomial matrix \(P\) over \(\mathbb QG\) in the first \(m\) variables has its maximum rank at \(t=(t_1,\ldots,t_m)\).
Indeed, the points of smaller rank lie in a countable union of proper closed subvarieties, as do the tuples algebraically dependent over \(\mathbb Q\).
There is a complex point outside both unions, and an automorphism of \(\mathbb C\) fixing \(\mathbb Q\) carries that tuple to \(t\).
The rank-invariance hypothesis gives the assertion.

By the [countable coefficient theorem](Yin_C_A0159_v1.md#transporting-inner-inverses-between-coefficient-fields), regularity of \(D_{\mathbb C}(G)\) is equivalent to regularity of \(D_K(G)\).
Suppose \(X\in M_{a,b}(\mathbb QG)\) has an inner inverse over \(D_K(G)\).
Linearizing the rational expressions for its entries and taking the direct sum of their pivots gives a realization \(Y=\alpha(t)L(t)^{-1}\beta(t)\) with \(L(t)\) an affiliated unit of size \(h\). [Rational linearization](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations)
All three matrices can be taken polynomial over \(\mathbb QG\) in finitely many variables.
Indeed, for a common scalar polynomial denominator \(d\) of their coefficients, replace \(\alpha,L,\beta\) by \(d\alpha,d^2L,d\beta\), respectively.
Their value for \(Y\) is unchanged because \(d(t)\ne0\).

Consider the polynomial matrix
\[
 J(z)=\begin{pmatrix}L(z)&\beta(z)X\\ X\alpha(z)&X\end{pmatrix}.
\]
Its Schur complement at \(t\) is \(X-XYX=0\), so its rank there is \(h\).
The preceding maximum-rank observation gives \(\operatorname{rk}_G J(z)\le h\) at every \(z\).
Choose \(q\in\mathbb Q^m\) at which \(L(q)\) has full rank.
At this point the same Schur complement vanishes, and \(\alpha(q)L(q)^{-1}\beta(q)\) is an inner inverse over \(D_{\mathbb Q}(G)\) by [Gram elimination for matrix inverses](Yin_C_A0132_v1.md#argument).
This proves the individual assertion and descends regularity from \(D_K(G)\) to \(D_{\mathbb Q}(G)\) by the [rectangular matrix criterion](Yin_C_A0159_v1.md#a-field-controlling-ranks).
That criterion and multiplication of each input by a common nonzero integer also equate conditions 2 and 3.

### Extending an inner inverse from a rational point

Assume condition 2 and take a matrix over \(KG\).
After multiplication by a nonzero scalar denominator it has the form \(X=P(t)\) for a rectangular polynomial matrix \(P\) as above.
Choose \(q\in\mathbb Q^m\) of maximal rank and put \(X_0=P(q)\), so \(\operatorname{rk}_G X_0=\operatorname{rk}_G X=r\).
Over \(D_{\mathbb Q}(G)\) choose a reflexive inner inverse \(Y_0\) of \(X_0\), satisfying both \(X_0Y_0X_0=X_0\) and \(Y_0X_0Y_0=Y_0\).
Starting with any inner inverse \(Y'\), one may take \(Y_0=Y'X_0Y'\).

Set \(V(z)=I+(P(z)-X_0)Y_0\), square on the output coordinates of \(P\).
Write \(Y_0=\alpha_0 L_0^{-1}\beta_0\) with a constant group-ring pivot \(L_0\) of full rank and with \(\alpha_0,\beta_0\) over \(\mathbb QG\).
The polynomial matrix
\[
 \begin{pmatrix}L_0&\beta_0\\-(P(z)-X_0)\alpha_0&I\end{pmatrix}
\]
has Schur complement \(V(z)\) and full rank at \(q\), where \(V(q)=I\).
It therefore has full rank at \(t\).
Consequently \(V(t)\) is an affiliated unit with inverse over \(D_K(G)\).

Put \(e=X_0Y_0\) and \(Y=Y_0V(t)^{-1}\).
The identities \(e^2=e\) and \(Y_0e=Y_0\) give \(V(t)e=XY_0\), whence \(YXY=Y\).
Moreover \(\operatorname{rk}_G Y=\operatorname{rk}_G Y_0=r\) by invertibility of \(V(t)\) and reflexivity at \(q\).
The idempotent \(XY\) has rank \(r\), since \(YXY=Y\), and its image lies in the image of \(X\).
Multiplication by \(XY\) splits the image module of \(X\) over \(U_G\) into the image of \(XY\) and a complementary finitely generated projective module.
The latter has dimension zero by the rank equality, hence vanishes by faithfulness of the trace.
Thus \(XY\) acts identically on the image of \(X\), giving \(XYX=X\).
This transfers an inner inverse through a point of maximal rank, as in the [torus-fiber criterion](Yin_C_A0132_v1.md#argument), using only rational coefficients from that point.
The rectangular criterion gives regularity of \(D_K(G)\), as required.

### The integral pencil on lamplighter intervals

Fourier transform on the lamps gives the regular representation over configurations \(\omega\in(\widehat{C_2^3})^{\mathbb Z}\) with independent uniform letters and fibers \(\ell^2(\mathbb Z)\).
The shift acts by translation of the height coordinate and each lamp acts diagonally by its character at that height. [Regular crossed-product representation](Yin_C_A0138_v1.md#argument)
If \(e_1,e_2,e_3\) generate the lamps at height zero, the indicator of a single letter \((\varepsilon_1,\varepsilon_2,\varepsilon_3)\in\{\pm1\}^3\) is represented by \(\prod_{j=1}^3(1+\varepsilon_j e_j)/8\).
The translated indicators select letters at neighboring heights.

Designate one letter as a delimiter.
Assign to four other letters, respectively, the four operations on an integer polynomial \(p\)
\[
 p\longmapsto zp,\qquad p\longmapsto p+1,\qquad
 p\longmapsto p-1,\qquad p\longmapsto p+z .
\]
Each of the three remaining letters acts as the identity.
Write the operation at a nondelimiter \(s\) as \(p\mapsto u_s(z)p+v_s(z)\).
For input coordinates \((a_i,c_i)_{i\in\mathbb Z}\), define the two output coordinates at height \(i\) by
\[
 \begin{aligned}
  &\begin{cases}
  a_i-zc_i,&\omega_i\text{ is a delimiter},\\
  a_i-u_{\omega_i}(z)a_{i-1}-v_{\omega_i}(z)c_i,&\text{otherwise},
  \end{cases}\\[2mm]
  &\begin{cases}
  a_i,&\omega_{i+1}\text{ is a delimiter},\\
  c_{i+1}-c_i,&\text{otherwise}.
  \end{cases}
 \end{aligned}
\]
Each coefficient is a linear polynomial times a one-site indicator or a sum of such terms, with at most one shift of the input.
Multiplication of both rows by \(8\) therefore gives a pencil \(A+zB\) with \(A,B\in M_2(\mathbb ZH)\).

Almost every configuration has infinitely many delimiters in each direction.
The rows involving an interval starting at one delimiter and ending just before the next use only inputs in that same interval.
The second rows identify all \(c_i\) there with one scalar \(c\) and require the last \(a_i\) to vanish.
The first rows start with \(a_i=zc\) and recursively apply the listed operations to the coefficient of \(c\).
Thus for the intervening word \(w\) the block kernel has dimension one if \(p_w(z)=0\) and zero otherwise, where \(p_w\) is obtained by starting at \(p=z\) and reading \(w\) in increasing height.
This also covers consecutive delimiters, for which \(p_w=z\).

Every \(p_w\) has positive degree and positive leading coefficient, since each of the five operations preserves these two properties.
Conversely fix any \(a_dz^d+\cdots+a_0\in\mathbb Z[z]\) with \(d\ge1\) and \(a_d>0\).
Starting from \(z\), add \(z\) exactly \(a_d-1\) times and then add the integer \(a_{d-1}\) by steps of \(+1\) or \(-1\).
For each remaining coefficient in descending order, multiply by \(z\) and add that integer in the same way.
The resulting finite word realizes the prescribed polynomial.

At a transcendental \(\lambda\) every interval block has zero kernel, hence the direct integral has zero kernel and the square matrix is an affiliated unit.
At an algebraic \(\lambda\) choose a word realizing a nonconstant polynomial vanishing at \(\lambda\).
The cylinder on which height zero is a delimiter followed by this word and a second delimiter has positive Bernoulli measure.
On the chosen interval there is a kernel vector with \(c_0=1\), so the kernel projection has strictly positive diagonal entry on the second coordinate at height zero throughout that cylinder.
The canonical group trace integrates these diagonal entries, giving strictly positive kernel dimension.
Finally, Fourier transform on a new central infinite cyclic factor evaluates the parameter at Haar-distributed points of the circle.
Only countably many of these points are algebraic, so the resulting pencil has full rank for the product trace.

Ara and Claramunt also use cylinder and shift matrices to construct lamplighter operators with prescribed families of kernel *dimensions*. [AC21, Theorem 4.5](https://doi.org/10.1007/s10801-021-01044-8)
Here the single integral pencil realizes the algebraic numbers as its singular *parameters*.

## Assessment history

### Decision rational-specialization

| Field | Value |
| --- | --- |
| date | 2026-11-25T13:34 |
| status | proved |
| reason | Maximal-rank fibers transfer inner inverses between coefficient fields, and the interval recursion realizes all algebraic exceptions in a single integral pencil. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Conditional rational coefficient descent and an integral pencil with exactly the algebraic singular parameters. |
| argument | [Argument](#argument) | Generic and specialized Schur ranks, continuation of a reflexive inner inverse, and the finite word recursion. |
| dependency | [Coefficient theorem](Yin_C_A0159_v1.md#statement) | Transfer to the countable transcendental coefficient field and the rectangular regularity criterion. |
| dependency | [Rank sublevels](Yin_C_A0128_v1.md#statement) | Generic maximal rank and Zariski density. |
| dependency | [Rational linearization](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) | Realizations of rational entries. |
| dependency | [Matrix inverses and fibers](Yin_C_A0132_v1.md#argument) | Inverses over the division closure and the maximal-rank construction. |
| dependency | [Crossed-product trace](Yin_C_A0138_v1.md#argument) | Regular trace on lamplighter fibers. |
| review | [Rational specialization](../audits/reviews/Yin_R_A0173_v1.md#rational-specialization) | Independent review of the complete statement and proof. |

## Current assessment

[Selected decision](#decision-rational-specialization)

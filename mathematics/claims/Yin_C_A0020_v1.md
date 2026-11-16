---
author: Yin
---
# Coefficient collisions localize a four-coset half-rank pair to a group with finite abelianization

## Statement

Let \(G\) be torsion-free. Suppose nonzero \(a,b\in\mathbb C[G]\) satisfy \(ab=0\) and both have regular rank \(1/2\), using the unnormalized trace convention of [A0001](../tasks/Yin_T_A0001_v1.md#contract).
Suppose \(\operatorname{supp}a\) occupies four **right** cosets \(Hx_i\) and \(\operatorname{supp}b\) occupies four **left** cosets \(y_jK\), for infinite cyclic groups \(H=\langle h\rangle\) and \(K=\langle k\rangle\).
Thus it is the two supports of \(a^*\) and \(b\) that have left-coset covers, as in the [joint Fourier estimate](../ledger/Yin_L_A0036_v1.md).

Divide the four left Laurent coefficients of \(a=\sum_i f_i(h)x_i\) by their common gcd, and the four right coefficients of \(b=\sum_j y_jg_j(k)\) by theirs.
For the resulting pair let \(A,B\) be its actual supports, and put
\[
              D=\langle (A^{-1}A)\cap(BB^{-1})\rangle .
\]
The new pair again has zero product and both ranks \(1/2\).
For any \(x_0\in A,y_0\in B\) it satisfies
\[
     A\subset x_0D,\qquad B\subset Dy_0,\qquad
     D=\langle A^{-1}A\rangle=\langle BB^{-1}\rangle,\qquad
     |D/[D,D]|<\infty .                                                \tag{1}
\]
Each factor is the only annihilator of the other supported inside its own support, up to a scalar, on the indicated multiplication side.
The group in (1) is computed after division of the gcds; adjoining redundant exterior Laurent multiples can change the original support differences.

## Argument

### Primitivity and coefficient collisions

A nonzero Laurent polynomial in an infinite-order element acts injectively with dense range: on each regular cyclic copy its Fourier multiplier is nonzero almost everywhere.
It is therefore invertible in the affiliated ring \(\mathcal U(G)\), so removing the exterior gcds preserves ranks and the zero product.
All four occupied cosets on each side persist.
In what follows \(a,b\) denote these primitive factors.

Apply the [four-column relation](Yin_C_A0021_v1.md#the-four-column-relation) first to \(a\) acting on the four left \(K\)-cosets of \(b\).
The finite vectors in that window annihilated by \(a\) form \(b\mathbb C[K]\), since its Laurent column is primitive.
If \(z=bp(k)\ne0\) is supported in \(B\), the exponent interval of \(g_jp\) lies inside that of \(g_j\) in each occupied coset.
The smallest and largest exponents of a product of nonzero Laurent polynomials are additive, so \(\min\operatorname{supp}p\ge0\) and \(\max\operatorname{supp}p\le0\).
Thus \(p\) is constant.
Applying the same argument to \(b^*a^*=0\) gives scalar uniqueness for left annihilators of \(b\) supported in \(A\).

The coefficient at \(w\in G\) in \(ab\) is \(\sum_{xy=w}a_x b_y=0\).
Whenever \(xy=x'y'\) in this sum, \(x^{-1}x'=yy'^{-1}\in D\).
Define a graph on \(A\) by joining distinct \(x,x'\) whenever such a collision occurs; define the column graph on \(B\) by the corresponding pairs \(y,y'\).
Every coefficient sum draws all its rows from one row component. Keeping only the terms of \(a\) in any row component therefore still gives a left annihilator of \(b\).
Scalar uniqueness makes the row graph connected; the same argument gives connectedness of the column graph.
Following paths shows \(A\subset x_0D\), \(B\subset Dy_0\). The reverse subgroup inclusions in (1) follow from the definition of \(D\).

### Ranks of the extreme degree terms

For any epimorphism \(\chi:D\to\mathbb Z\) with kernel \(N\), and any nonzero finite \(s\in\mathbb C[D]\), write \(s_+,s_-\) for its maximal and minimal degree parts. Then
\[
                r_D(s)\ge \max\{r_D(s_+),r_D(s_-)\}.                    \tag{2}
\]
Here is a direct regular-representation proof.
Choose \(t\in D\) of degree one and restrict the input to the height layers \(t^jN\), \(1\le j\le M\).
If the degrees of \(s\) range from \(m\) to \(n\), the output lies in \(M+n-m\) consecutive layers.
On each input layer use the orthogonal complement of the kernel of \(s_+\) into layer \(j+n\).
Its right \(N\)-dimension is \(r_D(s_+)\): after a degree shift the multiplier belongs to \(\mathbb C[N]\), and changing layers conjugates its coefficients by a trace-preserving group automorphism of \(N\).
The restriction of \(s\) to the sum of these \(M\) subspaces is injective, since the highest nonzero input component has a nonzero image in its highest output layer.
Its closed range has \(N\)-dimension \(M r_D(s_+)\).
The trace over the output layers of the compression of the global range projection of \(s\) is \((M+n-m)r_D(s)\), by invariance of its diagonal.
That compression dominates the restricted range projection.
Divide by \(M\) and let \(M\to\infty\); reversing the grading gives the other bound.

### The small product at maximal degree

Normalize the factors to \(x_0^{-1}a,\ by_0^{-1}\in\mathbb C[D]\).
Their ranks in \(D\) are still \(1/2\): the group trace agrees with that on \(G\) by decomposition into regular copies.
Each support contains the identity and generates \(D\).
The first support is covered by at most four right cosets of \(H_0=D\cap x_0^{-1}Hx_0\), the second by at most four left cosets of \(K_0=D\cap y_0Ky_0^{-1}\).
Indeed, intersecting any occupied coset with \(D\) gives a full coset of the intersected subgroup before retaining the actual support points.

If \(\chi:D\to\mathbb Z\) were onto, both supports would have different maximal and minimal degrees.
If \(\chi(H_0)=0\), every occupied row coset has constant degree.
At least one of the two extreme parts of the first factor then occupies at most two cosets, since the two sets of cosets are nonempty, disjoint and together use at most four.
A nonzero element on at most two right cosets has rank strictly larger than \(1/2\), by applying the [cyclic-coset estimate](Yin_C_A0019_v1.md#consequences-for-group-ring-products) to its adjoint.
For a trivial \(H_0\), the same assertion holds: a support of size one or two lies in one right coset of an infinite cyclic subgroup in the two-point case, and a monomial is a unit.
This contradicts (2); similarly \(\chi(K_0)\ne0\).
The restriction of \(\chi\) to each of these cyclic groups is now injective. Each individual coset contributes at most one support point to each extreme degree.
Both maximal degree parts consequently have at most four terms.
Their product is zero because it is the top homogeneous part of the zero product.
Nielsen and Soelberg's Theorem 1.4 for **nonempty subsets of a torsion-free group** gives a uniquely represented product for this pair of supports: absence of such a product would require the sum of their cardinalities to be at least 16.
Its coefficient is a single product of nonzero complex numbers.
This contradiction excludes the epimorphism. The finite generation of \(D\) now gives the last assertion of (1) by the structure theorem for finitely generated abelian groups.
The [author manuscript of Nielsen and Soelberg, Theorem 1.4, pp. 2–3](https://mathdept.byu.edu/~pace/KaplanskyConjecture_web.pdf) supplies the finite-set input; its computer-assisted bound is used as a published theorem.

## A finite test on the product table

There is also a direct check using only the finite support table \(A\times B\to AB\).
Assign real weights \(u_x,v_y\) subject to \(u_x+v_y=u_{x'}+v_{y'}\) whenever \(xy=x'y'\).
Let \(A_+\), \(B_+\) be the rows and columns of maximal weight on their respective sides.
If one pair in \(A_+\times B_+\) represents a product, every other pair representing it attains the same maximal sum and belongs to the same rectangle.
Consequently the two extreme subfactors have zero product.
In particular every such grading of a zero product satisfies \(|A_+|+|B_+|\ge16\), and the same holds for the two minima.
The weights need not extend to a homomorphism of groups. For constant weights this recovers the cardinality test of Nielsen and Soelberg.

Finiteness of the abelianization alone need not settle any of these coefficient equations.
The four-coset half-rank question still requires an exclusion or construction when the primitive difference group has finite abelianization and the product table admits no small exposed rectangle.

## Assessment history

### Decision primitive-four-coset

| Field | Value |
| --- | --- |
| date | 2026-11-17T00:05 |
| status | proved |
| reason | The independent review verified the argument under its stated hypotheses. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Support rigidity and finite abelianization of the primitive collision subgroup, with the finite table test. |
| argument | [Proof](#argument) | Complete proof and the stated limitations for A0001. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0051_v1.md#whole-argument-finding) | Independent mathematical review of this fixed result. |

## Current assessment

[Selected decision](#decision-primitive-four-coset)

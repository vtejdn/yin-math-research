---
author: Yin
---

# A two-by-two Schur obstruction over the commutator subgroup at cyclic order twenty-five

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with abelianization \(C_{25}\) marked by \(1,7\), and assume every nonzero complex group-ring scalar is injective in the regular representation.
Put \(N=[H,H]\), \(A=\mathbb CN\), and use the unnormalized matrix trace for regular rank.
Suppose the two-by-two four-site matrix \(K=B+At-s(D+Ct)\), with complex two-by-two corner matrices (where the corner \(A\) in this formula denotes a complex matrix), has rank \(3/2\).
There is a matrix \(R\in M_{14}(\mathbb CN)\) of rank exactly \(3/2\) such that
\[
                 uRv\ne0\qquad
 (0\ne u\in(\mathbb CN)^{1\times14},\quad 0\ne v\in(\mathbb CN)^{14\times1}).
\]
For **every** scalar entry chosen as a pivot, some two-by-two entry submatrix through that pivot has rank \(1+r\) with \(0<r\le1/2\) over \(N\).
Its scalar Schur complement uses one inverse of an actual nonzero element of \(\mathbb CN\) and has rank \(r\).
Thus integrality for two-by-two matrices over \(N\) excludes the given rectangle over \(H\).
If \(N\) has no strictly positive first Schur rank below \(1/2\), every nonzero entry of the remaining Schur block has rank exactly \(1/2\).

Each row \(uR\), for nonzero \(u\) as above, has fourteen entries freely generating a unital complex associative algebra and right-linearly independent over \(\mathbb CN\).
The entries of each column \(Rv\) for nonzero \(v\) satisfy the left-handed conclusions.
The span of the 196 entries of \(R\) has complex dimension at least 27.
The construction also gives a support test for the same two-by-two reduction over \(H''\).
In particular the descent applies when the commutator subgroup is perfect.

## The companion over the actual commutator subgroup

Take \(\chi:H\to C_{25}\) with \(\chi(s)=4,\chi(t)=3\), a unit multiple of the given marking, so that \(\ker\chi=N\).
Use the polynomial
\[
                  Q(z)=B+z^3At-z^4sD-z^7sCt .
\]
The four corners are invertible and \(\dim_H\ker Q(\omega)=1/2\) for each \(\omega^{25}=1\) by the [order-25 endpoint and phase calculation](Yin_C_A0201_v1.md#statement).
Its degree-seven coefficient \(Q_7=-sCt\) is a group translation times an invertible constant matrix.
Form the fourteen-dimensional block companion \(T\) with \(I_2\) on its superdiagonal and with last row blocks \(-Q_7^{-1}Q_j\), \(0\le j<7\).
For zero-based block indices \(i,j\), every term in \(T_{ij}\) has \(\chi\)-degree \(-1-i+j\).
This is zero on the superdiagonal and \(j-7\) in the last row.
Choose \(h_i\in H\) of degree \(i\), set \(D_0=\operatorname{diag}(h_iI_2)\) and \(T'=D_0TD_0^{-1}\).
Every entry of \(T'\) is homogeneous of degree \(-1\), hence \(R=(T')^{25}-I_{14}\) belongs to \(M_{14}(\mathbb CN)\).
This is the [companion change of subgroup coordinates](Yin_C_A0199_v1.md#subgroup-coordinates-and-the-odd-dimensional-norm) with the order set to 25.

Over \(H\), projection to the first block of an \(\omega\)-eigenvector of \(T\) identifies the eigenmodule with \(\ker Q(\omega)\), since the successive blocks are \(\omega^j\) times the first.
Conjugation preserves these dimensions for \(T'\).
On \(\ker R\) the interpolation polynomials \(e_\omega(x)=25^{-1}\sum_{j=0}^{24}\omega^{-j}x^j\) decompose the identity into the distinct root eigenspaces.
Consequently \(\operatorname{rk}_H R=14-25/2=3/2\), also its rank over \(N\) by decomposition along right cosets.

If \(Rw=0\) for a nonzero polynomial column \(w\) over \(\mathbb CH\), some \(e_\omega(T')w\) would be a nonzero polynomial column in that eigenspace.
Its nonzero coordinate is an affiliated unit by the scalar hypothesis, so the column would generate an affiliated module of dimension one in an eigenspace of dimension \(1/2\).
The same argument applied to \((T')^*\) excludes nonzero polynomial rows killed on the right by \(R\), since square matrices \(T'-\omega I\) and their adjoints have the same nullity.
This uses the [finite-support eigenvector argument](Yin_C_A0197_v1.md#the-companion-and-a-column-over-the-original-group-ring).
In particular \(R\) has neither kind of polynomial kernel over \(\mathbb CN\).

## Polynomial rows and columns at rank below two

More generally let \(A=\mathbb CN\) have regular scalar injectivity, and let \(R\) be any square polynomial matrix of size \(l\ge2\) and rank \(\rho<2\) with zero polynomial row and column kernels.
Use affiliated right modules, on which rank and nullity are additive.
For nonzero polynomial \(u,v\), the row \(uR\) and column \(Rv\) both have rank one since each has a nonzero group-ring coordinate.
It follows that \(\operatorname{im}R\cap\ker u\) has dimension \(\rho-1<1\).
If \(uRv=0\), this intersection would contain the entire dimension-one image of the column \(Rv\).
Therefore \(uRv\ne0\).

It follows that the \(l\) entries of \(uR\) give an injective right \(A\)-module map \(A^l\to A\).
Its image is a proper right ideal, since a right-module isomorphism \(A^l\simeq A\) would give \(\mathbb C^l\simeq\mathbb C\) upon tensoring with the augmentation module.
Any noncommutative polynomial relation among the entries then has zero constant term.
Grouping by first letters and applying right independence gives a relation of smaller degree for each first letter, so induction proves algebraic freeness.
The column proof uses the opposite algebra.

For any nonzero finite-dimensional spaces \(E\) of polynomial rows and \(F\) of polynomial columns one has
\[
             \dim_{\mathbb C}\operatorname{span}\{uRv:u\in E,\ v\in F\}
                      \ \ge\ \dim_{\mathbb C}E+\dim_{\mathbb C}F-1.
\]
Indeed the kernel of the linear map on \(E\otimes F\) avoids every nonzero decomposable tensor.
The projective dimension bound applied to the Segre variety gives the inequality, as in the [finite-dimensional two-sided test](Yin_C_A0113_v1.md#the-two-by-two-schur-complement).
Constant rows and columns give the stated bound 27 for \(l=14\).
If \(\Sigma\) is the union of the entry supports of \(R\), rows and columns supported in finite nonempty \(X,Y\subseteq N\) give
\[
                     |X\Sigma Y|\ \ge\ l|X|+l|Y|-1 .
\]

## A single inverse and exact coordinate ranks

Every entry of the companion remainder is nonzero by taking coordinate rows and columns in the preceding result.
Permute a chosen entry \(a\) into the upper left position and write \(R=\left(\begin{smallmatrix}a&b_0\\c_0&d_0\end{smallmatrix}\right)\).
Elimination over \(U(N)\) gives \(1+\operatorname{rk}(d_0-c_0a^{-1}b_0)=3/2\).
Any nonzero entry \(S=d-ca^{-1}b\) of this remaining block has rank at most its total rank \(1/2\) because coordinate inclusion and projection do not increase rank.
There is at least one such entry, yielding a two-by-two polynomial submatrix \(J=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\) of rank \(1+\operatorname{rk}S\).
This argument requires no equality between the maximum scalar entry rank and the rank of a matrix over the affiliated algebra.

For this \(J\) one can determine the exact ranks of the canonical entries in the [finite-rank Schur certificate](Yin_C_A0167_v2.md#a-pencil-for-the-particular-schur-scalar).
In fact take any two-by-two polynomial \(J\) in a group with regular scalar injectivity and \(0<\operatorname{rk}S<1\).
The two rows \((a,c)\) and \((a,b)\), here regarded simply as pairs of coefficients, are both linearly independent over \(\mathbb C\).
Indeed \(c=\lambda a\) or \(b=\lambda a\) would make \(S\) a group-ring scalar.
Set \(y=ca^{-1}\), \(z=a^{-1}b\), and let \(p\) be the right kernel projection of \(S\).
For any nonzero scalar pair \((\lambda,\mu)\), \(\lambda+\mu y=(\lambda a+\mu c)a^{-1}\) is an affiliated unit and \(\lambda p+\mu zp=a^{-1}(\lambda a+\mu b)p\) has rank \(\tau(p)>0\).
Thus both families \(1,y\) and \(p,zp\) are complex-linearly independent.
At a group element \(g\ne e\), the canonical coefficient tensor on those two families has scalar matrix \(\left(\begin{smallmatrix}d_g&-c_g\\-b_g&a_g\end{smallmatrix}\right)\).
Its tensor rank is exactly \(\operatorname{rank}_{\mathbb C}J_g\), and multiplication by the common affiliated units clearing the outer legs preserves that rank in the bounded finite-rank witness.
This calculation concerns the specified witness.
The [minimal affine representation formula](Yin_C_F0371_v1.md#ranks) for unique certificate coordinates has additional dual-system hypotheses.

## Testing descent one more step

More generally compress \(R\) to \(J=(u_i R v_j)_{i,j=1,2}\) by arbitrary pairs of nonzero polynomial rows and columns over \(N\).
Every entry of \(J\) is nonzero and \(\operatorname{rk}J\le3/2\).
If a Schur entry is nonzero, its rank again belongs to \((0,1/2]\).
Let \(M=N/H''\) in additive notation.
Group translations multiplying the two rows on the left and the two columns on the right put \(J\) over \(\mathbb CH''\) exactly when each entry support projects to a singleton \(\gamma_{ij}\) of \(M\) and
\[
                        \gamma_{11}+\gamma_{22}=\gamma_{12}+\gamma_{21}.
\]
Indeed this identity is equivalent to \(\gamma_{ij}=x_i+y_j\) for two row and two column classes in \(M\).
Lifts of their negatives clear all four degrees, and any such clearing conversely supplies the classes.
This is the two-by-two instance of the [support subgroup test](Yin_C_A0207_v1.md#statement).
Right-coset replication preserves the rank after clearing.
For a matrix of rank \(>1\) passing this test, elimination over \(U(H'')\) gives the positive Schur rank there with the same value.
When \(M=0\) the test holds for every qualifying corner.
For a nontrivial \(M\) the construction gives a sufficient test on specific corners and does not supply a corner satisfying the support condition.

## Assessment history

### Decision rank-below-two-on-the-commutator-subgroup

| Field | Value |
| --- | --- |
| date | 2026-11-26T11:08 |
| status | proved |
| reason | Independent review verified the companion rank, the two-sided nonvanishing and the actual two-by-two Schur descent. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Half nullity, ranks of entries, growth and the perfect case. |
| argument | [The companion over the actual commutator subgroup](#the-companion-over-the-actual-commutator-subgroup) | The marking, change of coordinates, eigenspaces and subgroup trace. |
| argument | [Polynomial rows and columns at rank below two](#polynomial-rows-and-columns-at-rank-below-two) | Two-sided nonvanishing, free row and column algebras and Segre bound. |
| argument | [A single inverse and exact coordinate ranks](#a-single-inverse-and-exact-coordinate-ranks) | All pivots, true Schur entries and the ranks of the specified tensors. |
| argument | [Testing descent one more step](#testing-descent-one-more-step) | The four support classes and the criterion for clearing them. |
| review | [Rank below two on the commutator subgroup](../audits/reviews/Yin_R_A0194_v1.md#rank-below-two-on-the-commutator-subgroup) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-rank-below-two-on-the-commutator-subgroup)

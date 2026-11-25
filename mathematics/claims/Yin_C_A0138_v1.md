---
author: Yin
---

# Testing matrix kernels by scalar kernels in one lamplighter extension

## Statement

Let \(G\) be a countable group, let \(L=C_2\wr\mathbb Z\) be the lamplighter group with shift \(t\), and write \(U_H=L^0(\mathcal N(H))\) and \(D_H=\operatorname{Div}_{U_H}(\mathbb CH)\).
For each \(m\)-by-\(k\) matrix \(X\) over \(\mathbb CG\), \(k\ge1\), there is an explicit positive scalar \(a_X\in\mathbb C[G\times L]\) such that
\[
 p_{\ker X}\in M_k(D_G)\quad\Longleftrightarrow\quad p_{\ker a_X}\in D_{G\times L}.
\]
Thus for a fixed finitely generated torsion-free \(G\), complete deletion of the local condition in [equation (1)](../tasks/Yin_T_A0003_v3.md#contract) is equivalent to the scalar kernel test on this family in \(G\times L\), with the same two-generator auxiliary group \(L\) at every width.
The input \(X\) may have arbitrarily many columns.

Restriction to any lamp configuration of least period \(q\), retaining the shift through one period as an infinite-order central variable, induces a unital \(*\)-homomorphism
\[
 D_{G\times L}\longrightarrow M_q(D_{G\times\mathbb Z}).
\]
In particular \(D_{G\times L}\cap U_G=D_G\).
For scalar coefficients Ara and Claramunt constructed the periodic-orbit quotient of the regular closure onto \(M_q(\mathbb C(z))\) in Theorem 4.11 of [Approximating the group algebra of the lamplighter by infinite matrix products](https://doi.org/10.1515/forum-2020-0141).
Here the transfer argument allows arbitrary group coefficients and gives the scalar kernel test above.

## Argument

### Finite-height relations at a periodic configuration

Fourier transform on the lamp subgroup identifies its group algebra with the locally constant complex functions on \(\Omega=\{0,1\}^{\mathbb Z}\).
In the regular representation of \(G\times L\), the resulting crossed product acts on \(L^2(\Omega;\ell^2(\mathbb Z;\ell^2(G)))\) for the Bernoulli measure with two equal weights.
At a configuration \(\omega\), a cylinder function acts at height \(j\) by its value at the translate of \(\omega\) by \(j\), and \(t\) shifts height by one.
These formulas follow from the regular representation by Fourier transforming the lamps and indexing their characters relative to the current height.
Every group-algebra matrix acts fiberwise by a finite-band matrix with locally constant coefficients.
At a configuration of period \(q\), grouping the heights \(qn,\ldots,qn+q-1\) gives a matrix over \(\mathbb C[G\times\mathbb Z]\).
The \(q\)-th power of the height shift is the central translation \(z\) in this group algebra.
Write a prime for this evaluation, including its entrywise amplification.

Let \(K\) be any rectangular group-algebra matrix and let \(F\) be a bounded row or matrix of the same input width with finite height propagation and locally constant coefficients in \(\mathcal N(G)\).
Then
\[
                     \ker K\subseteq\ker F\quad\Longrightarrow\quad
                     \ker K'\subseteq\ker F'.
\]
Indeed the Hilbert kernel of \(K'\) is the closed span of its vectors supported on finitely many periods, by [finite-coset localization](Yin_C_A0119_v1.md#exact-solutions-supported-on-finitely-many-cosets) for the normal subgroup \(G\le G\times\mathbb Z\).
If \(F'\) were nonzero on that kernel, boundedness would give a finite-height kernel vector \(\xi\) with \(F'\xi\ne0\).
Only finitely many lamp bits enter the computation of the two output vectors, since the input has finite height support and both matrices have finite propagation.
On the corresponding cylinder through the periodic configuration, the constant field with value \(\xi\) gives exactly the same two outputs.
The cylinder has positive measure, so extending this field by zero yields a vector of \(\ker K\) with nonzero image under \(F\).
This proves the implication.
Taking \(F=I\) shows that every square group-algebra matrix invertible over the global affiliated ring remains invertible after periodic evaluation, since Hilbert injectivity suffices for a square matrix in a finite von Neumann algebra.

### Evaluation of rational expressions

Each scalar rational expression defined over the global affiliated ring has a realization \(\alpha B^{-1}\beta\) with group-algebra coefficients and a globally invertible square group-algebra matrix \(B\).
The usual block diagonal, triangular and bordered constructions also realize every intermediate sum, product and inversion. [Domain-preserving realizations](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations)
All their pivots remain affiliated units at the periodic configuration by the preceding argument.
Consequently the specialized expression is defined, and its value has entries in \(D_{G\times\mathbb Z}\) by [scalar Gram elimination for matrices](Yin_C_A0132_v1.md#argument).

To verify independence of the expression, take \(K=[B,-\beta]\) and \(F=[\alpha,0]\).
Over either affiliated ring, the solutions of \(K(v,w)^{\mathsf T}=0\) are exactly \((B^{-1}\beta w,w)\).
For bounded matrices \(K,F\), vanishing of \(F\) on the affiliated kernel is equivalent to vanishing on the Hilbert kernel, because the affiliated kernel is generated by the Hilbert kernel projection.
Thus \(\alpha B^{-1}\beta=0\) globally implies the corresponding periodic value is zero by the transfer of kernel inclusions.
Applying this to the difference of two expressions proves well-definedness.
The group-algebra evaluation respects the involution and every legal rational operation, proving the homomorphism assertion.

If an expression represents \(u\in U_G\) in the global algebra, take the bounded left denominator \(s=(1+uu^*)^{-1/2}\) and \(d=su\in\mathcal N(G)\).
Use \(F=[s\alpha,-d]\) in the same implication.
Its periodic coefficients use \(s,d\) diagonally on all \(q\) heights, so \(s\) is still an affiliated unit and the periodic value of the expression is \(uI_q\).
Hence \(u\in D_{G\times\mathbb Z}\cap U_G=D_G\), by [evaluation at almost every central character](Yin_C_A0132_v1.md#argument).
The reverse inclusion follows from the inclusion of subgroup affiliated rings.

### Encoding the input columns

In \(\Omega\) let \(e\) indicate the cylinder with a \(1\) at position zero and zeros at positions \(1,\ldots,k-1\).
The first \(k\) translates \(t^iet^{-i}\), \(0\le i<k\), are pairwise orthogonal because two starts of this word cannot be less than \(k\) positions apart.
Thus \(E_{ij}=t^i e t^{-j}\) are group-algebra matrix units for \(0\le i,j<k\), commuting with \(U_G\).
Put \(f=\sum_iE_{ii}\), \(T=X^*X\), and set
\[
                   a_X=1-f+\sum_{i,j}T_{ij}E_{ij}.
\]
The normal matrix-unit inclusion into the corner with identity \(f\) sends \(T\) to the displayed sum and carries its kernel projection to \(\sum_{ij}(p_{\ker X})_{ij}E_{ij}\).
On the complementary corner \(a_X\) is the identity.
This proves positivity, identifies the global scalar kernel projection, and gives the forward implication in the statement.

For the converse choose the periodic configuration obtained by repeating the defining word of \(e\).
Index heights so that \(e\) selects residue zero.
On this orbit \(E_{ij}\) is the ordinary \((i,j)\) matrix unit, since shifting residue zero to \(i\) or \(j\) within the chosen period contributes no power of \(z\).
In particular \(a_X'=T\).
If \(p=p_{\ker a_X}\in D_{G\times L}\), then \(a_X+p\) is an affiliated unit and \((a_X+p)^{-1}\) belongs to the same division closure.
The periodic images satisfy \(p'=p'^*=p'^2\), \(Tp'=0\) and \(T+p'\) is an affiliated unit.
These identities force \(p'=p_{\ker T}\): the orthogonal part of \(\ker T\) outside \(p'\) is killed by \(T+p'\).
Every entry of \(p'\) therefore belongs to \(D_{G\times\mathbb Z}\cap U_G=D_G\).
The [matrix kernel characterization of complete deletion](Yin_C_A0137_v1.md#the-number-of-auxiliary-vectors) now gives the conclusion for equation (1).

The auxiliary group here has torsion.
Replacing its lamp group by \(\mathbb Z\) makes this periodic specialization fail even for a single unit: in \(\mathbb Z\wr\mathbb Z\) the difference of the lamps at positions zero and \(q\) is injective, because their quotient has infinite order and acts by bilateral shifts on its cosets.
At every \(q\)-periodic character configuration the difference vanishes.
The scalar test above therefore supplies a reduction for torsion-free \(G\), while the sufficiency of (1) for all such \(G\) remains open in this investigation.

## Assessment history

### Decision periodic-scalar-test

| Field | Value |
| --- | --- |
| date | 2026-11-25T10:18 |
| status | proved |
| reason | Transfer of finite-height kernel relations to a periodic configuration detects the encoded matrix kernel exactly. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Scalar encoding at every width, the periodic homomorphism and descent of constant operators. |
| argument | [Argument](#argument) | Finite-height kernel transfer, rational expression evaluation and the height tower. |
| dependency | [Finite-coset kernels](Yin_C_A0119_v1.md#exact-solutions-supported-on-finitely-many-cosets) | Density of exact finite-height solutions in the periodic model. |
| dependency | [Matrix realizations](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) | Legal scalar gates and invertible polynomial realizations. |
| dependency | [Central descent](Yin_C_A0132_v1.md#argument) | Matrix inverse closure and restriction of constant operators. |
| dependency | [Matrix-size criterion](Yin_C_A0137_v1.md#the-number-of-auxiliary-vectors) | Equivalence of complete deletion to all finite matrix tests. |
| review | [Periodic scalar tests](../audits/reviews/Yin_R_A0168_v1.md#periodic-scalar-tests) | Whole statement and proof at the scope of the recorded independent review. |

## Current assessment

[Selected decision](#decision-periodic-scalar-test)

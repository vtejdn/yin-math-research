---
author: Yin
---

# Vertex commutators bound the nullity of a matrix over an amalgam

## Statement

Let \(G=G_1*_H G_2\) be an amalgam of countable discrete groups, and write \(U_K=L^0(\mathcal N(K))\) for the ring of affiliated operators with the canonical group trace.
For a rectangular matrix \(A\) over \(U_K\), let \(\nu_K(A)\) be the trace of its kernel projection, using the unnormalized matrix trace.
Let \(A_i\in M_{m,n}(U_{G_i})\) and \(B\in M_{m,n}(U_H)\).
In each vertex choose a unitary \(u_i\in\mathcal N(G_i)\) commuting with \(\mathcal N(H)\), allowing independent choices in the two vertices.
Use \(u_iA_iu_i^*\) for entrywise conjugation and put \(\Delta_i=A_i-u_i A_i u_i^*\).
Then
\[
               2\nu_G(A_1+A_2+B)
                       \leq \nu_{G_1}(\Delta_1)+\nu_{G_2}(\Delta_2).
               \tag{1}
\]
In particular two injective differences imply injectivity for every affiliated edge perturbation \(B\), and two differences of full row rank imply full row rank for the sum.
For square matrices two injective differences make every such sum an affiliated unit.
When \(H=\langle h\rangle\) is cyclic, one may take \(u_1=u_2=h\), or use elements of the larger vertex centralizers of \(H\).

Write \(D_K=\operatorname{Div}_{U_K}(\mathbb CK)\).
When \(A_i\) have entries in \(D_{G_i}\) and \(B\) has entries in \(D_H\), the full-row-rank conclusion gives the entire kernel projection of \(A_1+A_2+B\) over \(D_G\), including when \(n>m\).
For scalar group-ring inputs one obtains a conclusion for every additive element under the following two vertex hypotheses.

1. Every nonzero element of \(\mathbb CG_i\) acts injectively in the regular representation.
2. Every element of \(G_i\setminus H\) has infinite conjugacy orbit under the centralizer \(C_{G_i}(H)\).

Under these hypotheses, every nonzero \(a_1+a_2\) with \(a_i\in\mathbb CG_i\) is a unit of \(U_G\).
The sum is zero precisely when \(a_1=-a_2\in\mathbb CH\).
For infinite cyclic \(H\), the second hypothesis holds in particular if every element outside \(H\) has infinite conjugacy orbit under \(h\), as is the case for a malnormal cyclic subgroup.
If each \(D_{G_i}\) is a division ring, the same orbit condition and \(D_{G_1}\cap U_H=D_{G_2}\cap U_H\) suffice for the analogous conclusion for all \(a_i\in D_{G_i}\).
Their sum is then zero precisely when \(a_1=-a_2\) belongs to this common intersection.

## Argument

### Comparing the ranks of two conjugate graph rows

Absorb \(B\) into \(A_1\) by putting \(Y_1=A_1+B\), \(Y_2=A_2\), and \(Y=Y_1+Y_2\).
Each \(u_i\) commutes with \(U_H\) by spectral calculus, so \(Y_i-u_iY_i u_i^*=\Delta_i\), even for singular or unbounded \(B\).
Let \(R_1=(Y_1,-I_m)\), \(R_2=(Y_2,I_m)\), and let \(P\) be the common kernel projection of these two graph rows.
Their right null module over \(U_G\) consists of the pairs \((v,Y_1v)\) with \(Yv=0\).
Projection onto the first \(n\) coordinates is therefore an isomorphism of this module onto the right null module of \(Y\), with inverse \(v\mapsto(v,Y_1v)\).
The polar decomposition of that coordinate projection restricted to \(P\) identifies its initial and final projections with \(P\) and the kernel projection of \(Y\), respectively, so \(\tau(P)=\nu_G(Y)\).
Here and below \(\tau\) denotes the unnormalized matrix trace with the canonical group trace in the relevant size.
These module calculations use closed affiliated sums and products.

Let \(Q=s(E_H(P))\) for the entrywise trace-preserving conditional expectation.
The [two-row rank identity](Yin_C_A0007_v13.md#two-rows-on-the-support-of-their-common-kernel) gives
\[
                 \nu_G(Y)=\tau(Q)-\sum_{i=1}^2\operatorname{rk}_{G_i}(R_iQ),
                 \tag{2}
\]
where rank is the trace of the range projection.
To use the bounded-row identity for an affiliated row \(R_i\), multiply on the left by \((I_m+R_iR_i^*)^{-1/2}\) in its vertex.
The product is bounded and the multiplier is a unit in \(M_m(U_{G_i})\), so the right null module of \(R_i\) and the ranks after restriction to \(Q\) agree with those for the bounded row.

Let \(R'_i=u_iR_iu_i^*\), with diagonal copies of \(u_i\) in the input and output sizes.
The edge projection \(Q\) commutes with the input copy of \(u_i\), so \(R'_i Q\) has the same rank as \(R_iQ\).
Let \(C_i\) be the kernel projection of the matrix obtained by stacking \(R_i\) and \(R'_i\).
Its right null module is the graph of \(Y_i\), with the appropriate sign on the last coordinate, over the kernel of \(\Delta_i\).
Indeed the graph equations agree on exactly those \(v\) for which \(Y_iv=u_iY_i u_i^*v\).
The same coordinate argument gives \(\tau(C_i)=\nu_{G_i}(\Delta_i)\).
Restricting the two stacked rows to \(Q\) gives a matrix of rank \(\tau(Q)-\tau(Q\wedge C_i)\), since its kernel inside \(Q\) is \(Q\wedge C_i\).
Its rank is at most the sum of the ranks of its two rows.
Thus
\[
        2\operatorname{rk}_{G_i}(R_iQ)\ \geq\ \tau(Q)-\tau(Q\wedge C_i).
\]
Substitution into (2) gives the sharper bound
\[
       2\nu_G(Y)\leq \tau(Q\wedge C_1)+\tau(Q\wedge C_2)
                  \leq \nu_{G_1}(\Delta_1)+\nu_{G_2}(\Delta_2).
\]
The last expression uses only the two vertices.
For the assertion about row rank, apply (1) to \(Y^*\), whose vertex differences are \(\Delta_i^*\).
For full row rank, \(YY^*\) is an affiliated unit and the kernel projection is \(I_n-Y^*(YY^*)^{-1}Y\).
When \(Y\) is rational over the group algebra this formula is rational by [matrix Gram elimination](Yin_C_A0132_v1.md#argument).
For a square injective matrix, polar decomposition in the finite algebra gives full range support as well, hence an affiliated inverse.

### Additive scalar elements

For any scalar \(a_i\in\mathbb CG_i\), commuting with all of \(C_{G_i}(H)\) makes its coefficients constant along all conjugacy orbits of that centralizer.
Finite support and the orbit hypothesis then put \(a_i\) in \(\mathbb CH\).
If both \(a_i\) lie outside \(\mathbb CH\), choose \(u_i\in C_{G_i}(H)\) such that \(a_i-u_i a_i u_i^*\ne0\).
These differences lie in their vertex group rings and are injective by the first hypothesis.
Inequality (1) gives an affiliated inverse for the sum.
If one summand belongs to \(\mathbb CH\), the sum belongs to the other vertex group ring and again is injective unless it is zero.
In that event both summands belong to \(\mathbb CH\).
For a malnormal infinite cyclic \(H\), a finite orbit under conjugation by \(h\) would make the group element centralize a nonzero power of \(h\), which is impossible outside \(H\) by malnormality.

For rational affiliated \(a_i\), the nonzero differences obtained with group centralizer elements belong to \(D_{G_i}\) and are injective under the division-ring hypothesis.
If \(a_i\) commutes with all the centralizer elements, its bounded transform \(a_i(1+a_i^*a_i)^{-1/2}\) does as well.
Its square-summable Fourier coefficients vanish on the infinite centralizer orbits, so the transform belongs to \(\mathcal N(H)\).
Inverting the bounded transform gives \(a_i\in D_{G_i}\cap U_H\).
The assumed equality of the two intersections puts this summand in the other vertex division ring, where the zero-or-unit conclusion follows.
This last transfer is automatic for the group-ring case by uniqueness of Fourier coefficients.
Linearizing a longer group word generally produces a matrix, to which (1) applies using the corresponding matrix differences.

### A double with no amenable action free on the edge

Let \(V=\ker(\operatorname{SL}_3(\mathbb Z)\to\operatorname{SL}_3(\mathbb F_3))\), \(h=I+3E_{12}\), \(g=I+3E_{23}\), and \(H=\langle h\rangle\).
The [congruence-group double](Yin_C_A0121_v1.md#the-obstruction-to-an-amenable-action) \(G=V_1*_H V_2\) is torsion-free and admits no amenable action on a nonempty discrete set on which \(H\) acts freely.
Let \(g_i\) denote the copy of \(g\) in \(V_i\).
Direct multiplication gives \(hgh^{-1}g^{-1}=I+9E_{13}\), which has infinite order.
Thus \(g-hgh^{-1}=(1-(I+9E_{13}))g\) is an affiliated unit, since translation by an infinite-order element has no nonzero fixed vector in the regular representation and its difference from the identity has dense range.

For any \(u\in U_{V_1}\), \(v\in U_{V_2}\), and \(B\in M_2(U_H)\), the matrix
\[
              \begin{pmatrix}g_1+g_2&u\\v&g_1+g_2\end{pmatrix}+B
\]
is an affiliated unit over \(G\).
Use the upper triangular matrix with diagonal \(g_1,g_1\) and off-diagonal entry \(u\) in the first vertex, and the lower triangular matrix with diagonal \(g_2,g_2\) and off-diagonal entry \(v\) in the second.
Their differences under \(h\)-conjugation are triangular with affiliated units on the diagonal, so (1) applies.
For \(B=0\), taking \(u,v\) to be sums of the elements of finite generating sets of the respective vertices makes the support of this matrix generate the whole double.
The example needs no assumption on the division closures of the congruence groups.

## Assessment history

### Decision vertex-conjugations

| Field | Value |
| --- | --- |
| date | 2026-11-25T11:41 |
| status | proved |
| reason | An edge projection sees the same rank for a graph row and its vertex conjugate, while stacking the two rows detects their conjugation difference. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The nullity bound, the rational wide-matrix consequence, scalar inputs and the congruence-group example. |
| argument | [Argument](#argument) | The affiliated two-row identity, intersections with conjugate graph kernels, Fourier support and the explicit triangular example. |
| dependency | [Graph rows](Yin_C_A0007_v13.md#two-rows-on-the-support-of-their-common-kernel) | Two vertex rows at the support of their expected common kernel. |
| dependency | [Rational matrix inverse](Yin_C_A0132_v1.md#argument) | A full-row-rank matrix has a rational orthogonal kernel projection. |
| dependency | [Congruence-group double](Yin_C_A0121_v1.md#the-obstruction-to-an-amenable-action) | Torsion-freeness and the obstruction to an amenable action free on the cyclic edge. |
| review | [Vertex conjugations](../audits/reviews/Yin_R_A0171_v1.md#vertex-conjugations) | Independent review of the complete statement and proof. |

## Current assessment

[Selected decision](#decision-vertex-conjugations)

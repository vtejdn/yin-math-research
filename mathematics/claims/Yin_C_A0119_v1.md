---
author: Yin
---
# Rational cyclic kernel support from a coamenable subgroup

## Statement

Let \(G\) be a discrete group and \(H=\langle z\rangle\cong\mathbb Z\).
Suppose there is a subgroup \(K\le G\) such that the left action of \(G\) on \(X=G/K\) is amenable and the restricted action of \(H\) on \(X\) is free.
The first condition means that for each finite \(S\subset G\) there are finite nonempty \(F\subset X\) with \(\sum_{s\in S}|sF\mathbin{\triangle} F|/|F|\) arbitrarily small.
The second means \(H\cap tKt^{-1}=\{1\}\) for every \(t\in G\).
In particular these conditions hold if a homomorphism onto an amenable group is injective on \(H\), by taking \(K\) to be its kernel.
It suffices that the image of \(z\) have infinite order, equivalently that the restriction to \(H\) have finite kernel, since \(H\) is infinite cyclic.

For each \(A\in M_{m,n}(\mathbb CG)\), let \(P\) be the kernel projection of left convolution on \(\ell^2(G)^n\), and let \(E_H\) be the canonical entrywise trace-preserving expectation onto \(\mathcal N(H)\).
Then
\[
       Q=s(E_H(P))\in M_n(\mathbb C(z)),\qquad
       (\operatorname{Tr}_n\otimes\tau_H)(Q)
         =\operatorname{rank}_{\mathbb C(z)}Q .
\]
Rational functions here act by Fourier multiplication on the circle, with \(z\) the coordinate character.
The conclusion concerns the support projection of the expectation.

If \(G=G_1*_H G_2\) and each vertex group has integer von Neumann kernel dimensions for all finite complex group-ring matrices, then so does \(G\).
This implication uses the [two-vertex graph formula](Yin_C_A0007_v13.md#two-rows-on-the-support-of-their-common-kernel) and the stated hypothesis on the action on \(X\).
It applies to every rectangular matrix and, for torsion-free vertices, gives the [A0001 conclusion](../tasks/Yin_T_A0001_v1.md#contract) for this amalgam.

## Argument

### Exact solutions supported on finitely many cosets

The finite-propagation argument for [ordinary amenable kernel localization](Yin_C_A0001_v2.md#rational-kernel-localization) uses ordinary finite supports.
Here a single coset \(xK\) can support arbitrary square-summable functions, and dimensions of spaces on finitely many such cosets are measured with the canonical trace of \(K\).
Let \(C_F\) denote the coordinate projection onto the union of the cosets in \(F\subset X\), amplified over the input or output coordinates as appropriate.
Every coset \(xK\) is a copy of the right regular \(K\)-space by \(k\mapsto xk\).
For a right-\(G\)-invariant closed space with projection \(B\) and finite \(F\), this identification gives
\[
   \operatorname{tr}_K(C_F B C_F)
     =\sum_{xK\in F}\sum_j\langle B\delta_{x,j},\delta_{x,j}\rangle
     =|F|\,\operatorname{tr}_G(B).
\]
Indeed right translation takes \(\delta_{e,j}\) to \(\delta_{x,j}\) and commutes with \(B\).
The trace on the left is the unnormalized matrix trace over the \(|F|\) cosets and all coordinates.

Choose a finite \(S\subset G\) containing \(1\) and the supports of all entries of \(A\).
Put \(O=SF\) and \(I=\bigcap_{s\in S}sF\), so \(I\subset F\subset O\).
For an output coset in \(I\), every input coset that can contribute to it belongs to \(F\), since left convolution by \(s\) carries \(xK\) to \(sxK\).
Consequently \(C_I A C_F=C_I A\), and \(A C_F=C_O A C_F\).
On the finite right \(K\)-module over \(F\), let \(D_F=\overline{\operatorname{ran}(C_F P)}\).
Its projection is the support of the positive contraction \(C_F P C_F\), so
\[
       \dim_K D_F\ \ge\ \operatorname{tr}_K(C_F P C_F)
             = |F|\operatorname{tr}_G(P).
\]
Since \(C_I A C_F P=C_I AP=0\), the map \(A\) on \(D_F\) takes values in the \(m\) output coordinates on \(O\setminus I\).
Its kernel \(U_F\) consists of exact solutions supported over \(F\), and polar decomposition bounds the codimension of this kernel by the dimension of that output module.
Thus \(\dim_K U_F\ge |F|\operatorname{tr}_G(P)-m|O\setminus I|\).

Let \(W\) be the closed linear span of all right \(G\)-translates of exact solutions supported on finitely many left \(K\)-cosets.
Right translations commute with \(A\), so \(W\subseteq\ker A\).
The projection onto \(U_F\) is dominated by both \(C_F\) and \(P_W\), hence also by \(C_F P_W C_F\).
The trace calculation gives
\[
   0\le \operatorname{tr}_G(P)-\operatorname{tr}_G(P_W)
      \le m\,\frac{|O\setminus I|}{|F|}
      \le m\sum_{s\in S}\frac{|sF\mathbin{\triangle}F|}{|F|}.
\]
Taking the infimum over \(F\) gives equality of the two traces, and faithfulness gives \(W=\ker A\).
When \(K\) is normal, each translate is again supported on finitely many left \(K\)-cosets, so the solutions with that support property are themselves dense.

### Restriction to the cyclic subgroup

Let \(J:\ell^2(H)^n\to\ell^2(G)^n\) extend by zero.
Compression gives \(E_H(P)=J^*PJ\), as is seen first on group elements and then by normality.
Since \(J^*PJ=(J^*P)(J^*P)^*\), its support projects onto \(\overline{J^*(\ker A)}\).
A translate of a left coset has the form \(xKt\).
For \(h_1,h_2\in H\cap xKt\), the element \(h_1^{-1}h_2\) lies in \(H\cap t^{-1}Kt=\{1\}\).
The restriction to \(H\) of each translated solution in the preceding spanning family is therefore a vector of Laurent polynomials.
Call the collection of these restrictions \(\mathcal V\).
Its closed complex linear span is \(\operatorname{ran}Q\), and \(\mathcal V\) is invariant under integral shifts along \(H\), since restriction commutes with its right translations.

Choose columns \(v_1,\ldots,v_r\) from \(\mathcal V\) forming a basis for its span in \(\mathbb C(z)^n\).
If \(r=0\), the restriction span is zero and \(Q=0\).
Otherwise put \(V=(v_1,\ldots,v_r)\) and denote conjugate transpose with \(z^*=z^{-1}\) by \(V^*\).
A nonzero \(r\)-minor shows that \(V\) has full column rank off a finite subset of the circle.
Thus
\[
        Q_0=V(V^*V)^{-1}V^*
\]
is a rational matrix and agrees almost everywhere with the orthogonal projection onto the column space of \(V\).
It defines a bounded Fourier multiplier.
For each \(v\in\mathcal V\), the rational identity \(Q_0v=v\) gives \(\operatorname{ran}Q\subseteq\operatorname{ran}Q_0\) by closure.
Conversely the shift invariance puts all Laurent polynomial combinations of the columns of \(V\) in \(\operatorname{ran}Q\).
Laurent polynomial columns are dense in \(L^2(\mathbb T)^r\), and multiplication by \(V\) is bounded, so \(\operatorname{ran}Q\) contains the closed range of this multiplier.
Its range projection is \(Q_0\) by the fiberwise formula.
This proves \(Q=Q_0\), and integrating the almost everywhere rank \(r\) gives the asserted trace.

### Amalgams and arbitrary rectangular matrices

First take an additive rectangular matrix \(Y=Y_1+Y_2\) with \(Y_j\) over \(\mathbb CG_j\).
Apply the support result to the single finite matrix obtained by stacking \(R_1=(Y_1,-I_m)\) above \(R_2=(Y_2,I_m)\).
Its kernel is the graph used in [C_A0007_v13](Yin_C_A0007_v13.md#two-rows-on-the-support-of-their-common-kernel), so the graph formula gives
\[
    \nu_G(Y)= \operatorname{tr}_H(Q)
           -\operatorname{rk}_{G_1}(R_1 Q)-\operatorname{rk}_{G_2}(R_2 Q).
\]
Each bounded rational entry of \(Q\) has a reduced denominator with no circle zero, since a pole makes its essential supremum infinite.
Take a common polynomial denominator \(\Delta(z)\) with no circle zero.
Right multiplication by \(\Delta I\) preserves the respective ranges, since it is boundedly invertible.
The ranks in the formula are consequently those of the finite vertex matrices \(R_j(Q\Delta)\).
Vertex integrality for arbitrary finite complex matrices makes both ranks integers, as the rank is the input size minus nullity.
The graph trace is the integer computed above.

For a general \(m\)-by-\(n\) matrix \(T\) over \(\mathbb CG\), write each entry as a finite complex linear combination of words in the two vertex groups.
If a term in position \((i,j)\) has at least two letters, write that term as \(uv\) with the coefficient included in its first letter \(u\), and put \(D=T-e_iuv e_j^{\mathsf T}\).
Adjoin one row and column to get
\[
        L=\begin{pmatrix}D&e_i u\\ -v e_j^{\mathsf T}&1\end{pmatrix}.
\]
The bottom equation for \((x,y)\in\ker L\) is \(y=v x_j\), and substitution into the top equation gives \(Tx=0\).
The bounded equivariant graph map \(x\mapsto(x,v x_j)\) from \(\ker T\) onto \(\ker L\) has the first-coordinate projection as its bounded inverse, so their dimensions agree by polar decomposition.
The sum over the displayed word terms of their lengths in excess of one decreases by one per replacement, with constants contributing zero.
After finitely many replacements all entries are sums of constants and single vertex letters, hence the final matrix is additive and has the original nullity.
For torsion-free vertex groups the amalgam is torsion-free, since every finite-order element acting on the Bass–Serre tree fixes a vertex and lies in a conjugate of a vertex group.
For input over a smaller conjugation-stable field \(k\), the linearization stays over \(k\), but the coefficients of the Laurent restrictions of square-summable solutions can be complex.
Applying vertex integrality solely over \(k\) by this argument requires separate descent of the graph support to \(k(z)\), as in the [cyclic denominator calculation](Yin_C_A0007_v13.md#clearing-cyclic-denominators-in-the-vertex-matrices).

### A noncentral edge in a double of the Promislow group

Let \(P_0=\langle a,b\mid b^{-1}a^2b=a^{-2},\ a^{-1}b^2a=b^{-2}\rangle\), and form \(G=P_0*_{\langle b\rangle}P_0\) by identifying the two copies of \(b\).
The [translation subgroup](../ledger/Yin_L_A0024_v1.md#fixed-setting-and-proposed-test) has index four and is free abelian of rank three on \(a^2,b^2,(ab)^2\).
Hence \(P_0\) is amenable, \(b\) has infinite order, and \(\langle b\rangle\) has infinite index.
The relation \(a^{-1}b^2a=b^{-2}\) shows the edge is noncentral.
The two relators give \(4[a]=4[b]=0\) in the abelianization, so every homomorphism \(P_0\to\mathbb Z\) vanishes.
The two vertex groups generate the double, so all its homomorphisms to \(\mathbb Z\) vanish as well.
The fold \(G\to P_0\) restricting to the identity on both copies is an amenable quotient injective on the edge.
The already established [complex matrix integrality for each Promislow vertex](Yin_C_A0013_v1.md#the-complete-task-interface-and-its-remaining-generalization-gap) therefore gives integrality for every finite matrix on this double by the graph calculation.

Write \(K\) for the fold kernel.
It meets every conjugate vertex group trivially by normality and injectivity of the fold on each vertex group.
It acts freely without inversions on the Bass–Serre tree, whose vertices are the cosets of the two vertex groups and whose edges are the cosets of \(\langle b\rangle\).
Quotienting by \(K\) gives one vertex of each type and edges indexed by \(P_0/\langle b\rangle\), all joining the two vertices.
The tree is the universal cover of that graph with deck group \(K\).
A spanning tree consists of one edge, so the other edges give a free basis of \(K\) of countably infinite rank.
In particular the double already belongs to the [free-by-elementary amenable class](../ledger/Yin_L_A0001_v1.md#known-positive-results).

Take two free basis elements \(u,v\in K\) and the row \(\partial=(u-1,\ v-1)\).
Its range is dense in \(\ell^2(G)\), since a vector orthogonal to the range of \(u-1\) is invariant along the infinite left \(u\)-orbits and hence vanishes in \(\ell^2\).
Thus \(\dim_G\ker\partial=2-1=1\).
On each right coset of \(\langle u,v\rangle\), a finitely supported solution gives a finite edge chain with zero boundary on the Cayley tree for \(u,v\).
A nonempty finite forest has a leaf, where the boundary coefficient of the unique incident edge cannot vanish, so every such chain is zero.
This is the same [free-row obstruction](Yin_C_A0007_v6.md#a-full-support-additive-realization) within the fold kernel.
Solutions supported on finitely many fold-kernel cosets are dense despite the absence of any nonzero solution of finite ordinary support.
The general cyclic-edge problem in [strategy S_A0005](../strategies/Yin_S_A0005.md) still includes cases for which such an action has not been established, and the argument takes vertex integrality as an input.

## Assessment history

### Decision coamenable-cyclic-edge

| Field | Value |
| --- | --- |
| date | 2026-11-22T04:54 |
| status | proved |
| reason | Independent review verifies the full statement and argument under the specified assumptions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Rational expected kernel support for a cyclic subgroup acting freely on an amenable coset space, and complex-coefficient permanence for such amalgams. |
| argument | [Proof](#argument) | Relative kernel localization, Laurent restriction, the vertex rank identity, word linearization and the fold-kernel example. |
| review | [Whole finding](../audits/reviews/Yin_R_A0156_v1.md#whole-finding) | Independent whole-argument finding at the stated scope. |

## Current assessment

[Selected decision](#decision-coamenable-cyclic-edge)

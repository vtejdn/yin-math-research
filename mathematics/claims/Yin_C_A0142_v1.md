---
author: Yin
---

# Rational recovery of the zero atom for matrices over a free product with amalgamation

## Statement

Let \(G=G_1*_{H}G_2\) be a countable discrete group and put \(U_K=L^0(\mathcal N(K))\), \(D_K=\operatorname{Div}_{U_K}(\mathbb CK)\).
Suppose \(D_{G_1},D_{G_2}\) are von Neumann regular.
Then \(D_G\) is von Neumann regular under either of the following hypotheses.

1. The edge group \(H\) is finite, including the trivial group in an ordinary free product.
2. \(D_H\) is semisimple Artinian and there is a coamenable subgroup \(K\le G\) such that \(H\) acts freely on \(G/K\).
   Here coamenability means that the action of \(G\) on \(G/K\) admits Følner sets for every finite subset of \(G\), and freeness means \(H\cap gKg^{-1}=\{1\}\) for all \(g\in G\).

For finitely generated \(G\) with either hypothesis, [equation (1)](../tasks/Yin_T_A0003_v3.md#contract) alone therefore characterizes membership in \(D_G\).
In particular this conclusion holds for an amalgam of finitely generated torsion-free vertex groups satisfying the unrestricted criterion over a cyclic edge whose generator has infinite order in some amenable quotient of \(G\).
The vertex hypothesis concerns ordinary inversion in their division closures and permits zero divisors there.

For an additive matrix \(X=X_1+X_2\), \(X_i\in M_{m,n}(\mathbb CG_i)\), set \(L_1=[X_1,-I_m]\), \(L_2=[X_2,I_m]\), stack these rows into \(L\), and set \(A=L^*L\) of size \(N=n+m\).
Write \(E_H\) for entrywise trace-preserving conditional expectation onto the edge and let \(Q\) be the support of the limit \(E_H(\lim_{s\downarrow0}s(A+sI)^{-1})\).
The inner limit is strong and equals \(p_{\ker L}\).
At every edge projection \(Q_0\in M_N(D_H)\) with the same maximal value of
\[
 \operatorname{tr}_H(Q_0)-\operatorname{rk}_{G_1}(L_1Q_0)-\operatorname{rk}_{G_2}(L_2Q_0)
\]
as \(Q\), let \(b_i=s((L_iQ_0)^*L_iQ_0)\), \(W=[b_1,b_2]\), and \(P_d=\operatorname{diag}(b_1,b_2)\).
Under either hypothesis such a maximizer exists in \(M_N(D_H)\), and
\[
      \operatorname{CT}_{z=0}\big[z(A+zI)^{-1}\big]
        =Q_0-W(W^*W+I_{2N}-P_d)^{-1}W^*
        \ \in M_N(D_G).
\]
Here \(\operatorname{CT}\) extracts the constant coefficient in \(M_N(U_G((z)))\).
Taking the first \(n\) coordinates of the graph recovers \(p_{\ker X}\) by the formula below.
For every group-ring matrix \(Y\) over these groups the formal matrix \(z(Y^*Y+zI)^{-1}\) consequently has scalar rational expressions whose inverses are all defined at \(z=0\).

## Argument

### Recovering the atom from its expected support

For a bounded positive operator the spectral theorem gives the strong limit in the statement.
In the formal Laurent ring, splitting off the kernel gives the inverse
\[
 (A+zI)^{-1}=z^{-1}p_{\ker A}
      +\sum_{j\ge0}(-z)^j(A^{[-1]})^{j+1},
\]
where \(A^{[-1]}\) is the inverse between supports.
Thus the constant coefficient of the scaled resolvent is exactly the same orthogonal projection as its strong limit.
The coefficients take values in the affiliated ring, with no convergence assumption on the Laurent expansion. [Formal resolvent identity](Yin_C_A0141_v1.md#realizing-every-element-of-the-regular-closure)

Put \(p=p_{\ker L}\).
For any edge projection \(Q_0\), the projection onto the common kernel inside \(Q_0\) is \(p\wedge Q_0\), and \(b_i\) is the orthogonal complement inside \(Q_0\) of the \(i\)-th restricted kernel.
The dimension identity for two projections therefore gives the exact difference
\[
 \operatorname{tr}_G p-
 \left(\operatorname{tr}_H Q_0-\sum_i\operatorname{rk}_{G_i}(L_iQ_0)\right)
 =\operatorname{tr}_G(p-p\wedge Q_0)+\operatorname{tr}_G(b_1\wedge b_2).
\]
The [free projection theorem on the support of the expectation](Yin_C_A0007_v13.md#two-rows-on-the-support-of-their-common-kernel) gives equality in the maximization at \(Q=s(E_H(p))\).
Its analytic input is the zero-atom theorem for operator-valued free additive convolution applied to the complementary vertex projections after restricting to the expected support. [Belinschi, Bercovici and Liu, Theorems 3.2 and 3.5](../audits/literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface)
Faithfulness now gives \(p\le Q_0\) and \(b_1\wedge b_2=0\) for every maximizer.
In particular \(W\) is injective on \(P_d U_G^{2N}\), since a cancellation between its two coordinates belongs to the intersection of the two ranges.
It follows that \(W^*W+I_{2N}-P_d\) is an affiliated unit.
The expression \(W(W^*W+I_{2N}-P_d)^{-1}W^*\) is the orthogonal projection onto the sum of these two affiliated column modules.
Indeed it is selfadjoint and idempotent, fixes \(W\), and has image in \(WU_G^{2N}\).
This projection is \(b_1\vee b_2=Q_0-p\), proving the formula.

### Rationality of the edge and vertex projections

For finite \(H\) the entire edge von Neumann algebra is \(\mathbb CH\).
For hypothesis 2, the [finite-coset localization argument](Yin_C_A0119_v1.md#exact-solutions-supported-on-finitely-many-cosets) shows that \(\ker L\) is the closed span of translates of vectors supported on finitely many \(K\)-cosets.
Extension by zero from \(\ell^2(H)^N\) has adjoint restriction to \(H\), and compression of \(p\) by these maps is \(E_H(p)\).
Thus \(Q\) is the projection onto the closed span of the restrictions of that generating family.
Freeness of the \(H\)-action makes the intersection of \(H\) with each translated coset \(gKx\) have at most one point: the quotient of two such points belongs to \(H\cap x^{-1}Kx\).
Each restricted column therefore lies in \((\mathbb CH)^N\).
All their right \(H\)-translates belong to the restriction family, since the kernel commutes with right translation.

Their right \(D_H\)-span is a submodule of \(D_H^N\), hence finitely generated by semisimplicity.
A finite subfamily of the original columns generates this span, by collecting the columns used to express a finite set of generators.
Let \(V\) be the group-ring matrix of that subfamily, using the zero projection for an empty family.
The closed range of \(V\) lies in \(Q\), since the right translates of each selected column span its range after closure.
Conversely the range projection \(s(VV^*)\) fixes each original restricted column in \(U_H^N\) by the finite generation.
Applying this equality to the trace vector shows that the closed restriction span is contained in the closed range of \(V\).
The projection onto that range belongs to \(M_N(D_H)\) by matrix regularity, which proves \(Q\in M_N(D_H)\).
For a cyclic edge generated by \(h\) with infinite-order image in an amenable quotient, take its kernel as \(K\); \(D_H=\mathbb C(h)\) in this case.

Each \(L_i Q_0\) has entries in \(D_{G_i}\) by the subgroup inclusions.
For a regular division-closed \(*\)-subring the range and kernel projections of its finite matrices belong to the same matrix ring, by taking an inner inverse and forming the orthogonal projection using scalar Gram inversion. [Matrix regularity and relative inverses](../audits/literature/JZ19/Yin_U001.md#regular-closure-definitions)
It follows that \(b_i\in M_N(D_{G_i})\).
All entries on the right of the atom formula now lie in \(D_G\), including the inverse of the displayed affiliated unit by [matrix Gram elimination](Yin_C_A0132_v1.md#argument).

### From graph matrices to the group algebra

Projection \(\Pi\) onto the first \(n\) coordinates maps the graph \(\ker L\) bijectively onto \(\ker X\) with bounded inverse \(v\mapsto(v,X_1v)\).
Consequently
\[
 p_{\ker X}=\Pi p\,(p\Pi^*\Pi p+I_N-p)^{-1}p\Pi^* .
\]
The denominator is an affiliated unit, and the same projection identity applies with \(W=\Pi p\).
For an arbitrary group-ring matrix, [word linearization](Yin_C_A0119_v1.md#amalgams-and-arbitrary-rectangular-matrices) produces an additive matrix by adjoining graph coordinates one product at a time.
At every step deletion of the last input coordinate is a bijection of Hilbert kernels with bounded inverse.
The projection identity just proved transports rationality back through the finitely many coordinate deletions.
Thus every group-ring matrix has its kernel projection over \(D_G\).
The [finite-support characterization of regularity](Yin_C_A0132_v1.md#consequences-for-the-unrestricted-equation) gives regularity for countable \(G\), and the [unrestricted criterion for a finite marking](Yin_C_A0131_v1.md#which-rationality-is-detected) gives complete deletion for finitely generated \(G\).
Finally put \(T=Y^*Y\), \(h=p_{\ker Y}\) and \(C(z)=T+h+z(I-h)\).
The positive matrix \(C(0)\) is injective, so the inverse of \(C(z)\) is a formal power series obtained by scalar Gram inversion with \(z^*=z\).
Indeed the leading Gram blocks of \(C(z)^*C(z)\) have invertible constant terms and may be eliminated successively.
On the two supports this gives
\[
      z(T+zI)^{-1}=h+z(I-h)C(z)^{-1}(I-h).
\]
Expansion of the constant entries from \(D_G\) gives the asserted expressions over the group algebra, all defined at zero.

## Assessment history

### Decision free-amalgam-atoms

| Field | Value |
| --- | --- |
| date | 2026-11-25T10:44 |
| status | proved |
| reason | The maximizing edge projection makes the two vertex range modules independent and gives the full kernel projection by an affiliated Gram inverse. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Regularity under the two edge hypotheses, the zero-atom formula and specialization at zero. |
| argument | [Argument](#argument) | Free convolution, rational expected support, word linearization and recovery of a regular expression for the resolvent. |
| dependency | [Two vertex rows](Yin_C_A0007_v13.md#two-rows-on-the-support-of-their-common-kernel) | The maximal-rank formula at the support of the expected kernel. |
| dependency | [Free additive convolution](../audits/literature/BBL21/Yin_U001.md#bbl21-u001) | Operator-valued zero-atom theorem at the bounded-inverse interface. |
| dependency | [Finite-coset localization](Yin_C_A0119_v1.md#exact-solutions-supported-on-finitely-many-cosets) | Kernel restriction to finitely many edge coordinates and word linearization for arbitrary group-ring matrices. |
| dependency | [Complete deletion](Yin_C_A0131_v1.md#which-rationality-is-detected) | Link from regularity to the finite-marking commutator criterion. |
| dependency | [Finite support and matrix inverses](Yin_C_A0132_v1.md#consequences-for-the-unrestricted-equation) | Matrix Gram pivots and the countable-group regularity test. |
| dependency | [Matrix regularity](../audits/literature/JZ19/Yin_U001.md#jz19-u001) | Relative inverses over regular subrings. |
| dependency | [Formal resolvent](Yin_C_A0141_v1.md#realizing-every-element-of-the-regular-closure) | The constant coefficient of the scaled resolvent. |
| review | [Free convolution atoms](../audits/reviews/Yin_R_A0169_v1.md#free-convolution-atoms) | Independent proof review at the specified scope. |

## Current assessment

[Selected decision](#decision-free-amalgam-atoms)

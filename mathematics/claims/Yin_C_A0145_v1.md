---
author: Yin
---

# Regular division closures for fundamental groups of graphs of groups

## Statement

Let \(G\) be the fundamental group of a finite connected graph of countable discrete groups with injective edge maps.
Write \(U_J=L^0(\mathcal N(J))\) and \(D_J=\operatorname{Div}_{U_J}(\mathbb CJ)\) for any subgroup \(J\).
Suppose that every vertex group \(V\) has von Neumann regular \(D_V\).
For every edge group \(C\), suppose that \(D_C\) is semisimple Artinian and that there is a nonempty \(G\)-set \(X_C\) with the following properties.

1. For every finite \(S\subset G\) and every \(\varepsilon>0\), some nonempty finite \(F\subset X_C\) satisfies \(\sum_{s\in S}|sF\mathbin{\triangle}F|<\varepsilon |F|\).
2. The stabilizer in \(C\) of each point of \(X_C\) is finite.

The two images of an edge group in \(G\) are conjugate, so either image gives the same condition.
The action may depend on the edge and may have several orbits.
Then \(D_G\) is von Neumann regular.
In particular, for finitely generated torsion-free \(G\), an affiliated element belongs to \(D_G\) exactly when it satisfies the [unrestricted finite-rank equation (1)](../tasks/Yin_T_A0003_v3.md#contract).
The vertex hypothesis allows zero divisors in \(D_V\).

A finite edge satisfies the hypotheses with a one-point action, since \(D_C=\mathbb C[C]\) is semisimple Artinian.
For an infinite cyclic edge \(C=\langle h\rangle\), one has \(D_C=\mathbb C(h)\), and the stabilizer condition says that every \(h\)-orbit is infinite.
An amenable quotient of \(G\) in which the image of \(h\) has infinite order supplies such an action by left translation.
When the vertex groups are torsion-free, so is \(G\), since every finite-order element fixes a vertex of the Bass–Serre tree.

## Argument

### Restrictions of a group-ring kernel to an edge

Fix one edge \(C\), put \(X=X_C\), and let \(P\) be the kernel projection of \(A\in M_{m,n}(\mathbb CG)\).
We show that \(s(E_C(P))\in M_n(D_C)\), where \(E_C\) is the trace-preserving expectation onto \(\mathcal N(C)\) applied to each entry and \(s\) denotes the support of a positive operator.
Take a finite set \(S\subset G\) containing the identity and the supports of the entries of \(A\).
For each \(\varepsilon>0\), choose a Følner set as in the statement.
The sum of its boundary sizes and its cardinality both decompose over the \(G\)-orbits of \(X\).
Hence some nonempty component \(F\) in a single orbit has boundary ratio less than \(\varepsilon\), with the same sum over \(S\).
Choose a base point of each orbit and identify that orbit with \(G/K\) for its point stabilizer \(K\).
The orbit giving this estimate may vary with \(\varepsilon\).

Let \(W\) be the closed span of the right \(G\)-translates of exact solutions of \(A\xi=0\) supported on finitely many left \(K\)-cosets, allowing the stabilizers from all these orbits.
For one such \(F\subset G/K\), write \(C_F\) for projection onto its cosets, \(O=SF\) and \(I=\bigcap_{s\in S}sF\).
The [finite-coset dimension estimate](Yin_C_A0119_v1.md#exact-solutions-supported-on-finitely-many-cosets) applies on this single orbit.
Indeed \(\overline{\operatorname{ran} C_F P}\) has right \(K\)-dimension at least \(|F|\operatorname{tr}_G P\), by the trace of \(C_F P C_F\).
Its image under \(A\) is supported on \(O\setminus I\), so its exact solutions have \(K\)-dimension at least \(|F|\operatorname{tr}_G P-m|O\setminus I|\).
Their projection is dominated by \(C_F P_W C_F\), whose \(K\)-trace is \(|F|\operatorname{tr}_G P_W\), since \(P_W\) commutes with right translations.
With the unnormalized matrix trace this gives
\[
  0\le \operatorname{tr}_G(P-P_W)
      \le m\,\frac{|O\setminus I|}{|F|}
      \le m\,\frac{\sum_{s\in S}|sF\mathbin{\triangle}F|}{|F|}.
\]
The same \(W\) works for every chosen orbit, and letting \(\varepsilon\) tend to zero gives \(W=\ker A\).

A translate of a supporting coset has the form \(xKg\).
If \(h_0\in C\cap xKg\), then \(C\cap xKg\subset h_0(C\cap g^{-1}Kg)\), which is finite by the stabilizer hypothesis at \(g^{-1}K\).
Restriction to \(C\) therefore turns every column in the spanning family for \(W\) into a vector in \((\mathbb CC)^n\).
For the extension by zero \(J:\ell^2(C)^n\to\ell^2(G)^n\), the identity \(E_C(P)=J^*PJ\) shows that its support projects onto \(\overline{J^*(\ker A)}\).
The closed span of the restricted columns is this space, and their family is invariant under right translations by \(C\).
Their right \(D_C\)-span is a submodule of the finite-length module \(D_C^n\), so a finite subfamily generates it.
Form the matrix \(V\) of these columns, with range projection zero for the empty family.
By regularity its range projection belongs to \(M_n(D_C)\).
It fixes every restricted column, and its range is the closed span of the right translates of the chosen columns.
Thus it equals \(s(E_C(P))\). [Rationality of the edge projection](Yin_C_A0142_v1.md#rationality-of-the-edge-and-vertex-projections)

The same conclusion applies to a matrix over \(\mathbb CJ\) for \(C\le J\le G\).
Decomposition over the right cosets of \(J\) identifies its kernel projection over \(G\) with the image of its kernel projection over \(J\).
The two expectations onto \(C\) agree on \(\mathcal N(J)\).
This allows every intermediate group in the graph construction to use the original \(G\)-action.

### Recovering a kernel from two free subalgebras

We recall the part of the [two-row argument](Yin_C_A0142_v1.md#recovering-the-atom-from-its-expected-support) that also applies to matrix algebras.
Suppose \(A_1,A_2\) are finite tracial von Neumann algebras free over \(B\) in a common finite tracial algebra, with trace-preserving expectation \(E_B\).
For \(Y=Y_1+Y_2\) with \(Y_i\in M_{m,n}(A_i)\), put \(L_1=[Y_1,-I_m]\), \(L_2=[Y_2,I_m]\), and let \(P\) project onto their common kernel.
Write \(Q=s(E_B(P))\) and \(b_i=s((L_iQ)^*L_iQ)\).
Then \(P\le Q\), and the [free projection identity](Yin_C_A0007_v13.md#free-vertex-projections-with-a-common-kernel-of-full-expected-support), applied to the full kernel projections of \(L_iQ\), gives \(b_1\wedge b_2=0\).
Within \(Q\) the orthogonal complement of \(P\) is \(b_1\vee b_2\).
Consequently, with \(W_0=[b_1,b_2]\) and \(P_0=\operatorname{diag}(b_1,b_2)\), one has
\[
 P=Q-W_0(W_0^*W_0+I-P_0)^{-1}W_0^* .
\]
Indeed \(W_0\) is injective on \(P_0\), and the subtracted term is the range projection of \(W_0\).
If the restricted rows \(L_iQ\) are over regular division-closed vertex rings, their support projections \(b_i\) are over those rings by [matrix regularity](../audits/literature/JZ19/Yin_U001.md#regular-closure-definitions).
When \(Q\) and these rings have entries in the ambient division closure, the displayed inverse has entries there by [matrix Gram elimination](Yin_C_A0132_v1.md#argument).
The formula then recovers \(P\) in that division closure.

Projection \(\Pi\) onto the first \(n\) coordinates maps this graph kernel bijectively onto \(\ker Y\) with bounded inverse \(x\mapsto(x,Y_1x)\).
The range projection of \(\Pi P\) is therefore
\[
 p_{\ker Y}=\Pi P(P\Pi^*\Pi P+I-P)^{-1}P\Pi^*.
\]
The same identity applies whenever a coordinate deletion is bijective on a kernel with bounded inverse.

### Amalgams and the HNN matrix construction

Choose a maximal tree in the finite underlying graph.
Adjoining a new vertex and a tree edge produces a free product with amalgamation \(J=J_1*_{C}J_2\).
For additive group-ring matrices, the two vertex von Neumann algebras are free over \(\mathcal N(C)\).
The stacked matrix of the rows \(L_1,L_2\) is over \(\mathbb CJ\), so the edge restriction proved above puts \(Q\) in the matrix ring over \(D_C\).
This ring embeds in both vertex matrix rings over \(D_{J_i}\), which are regular by induction.
The two formulas above give \(p_{\ker Y}\) over \(D_J\).

Each remaining edge produces an HNN extension of the current group \(V\), for which we use the convention
\[
 J=\langle V,t\mid t\,\iota_2(c)\,t^{-1}=\iota_1(c),\ c\in C\rangle,
 \qquad C_i=\iota_i(C).
\]
In \(M_2(\mathcal N(J))\) put \(T=\operatorname{diag}(1,t^{-1})\) and take
\[
 A_1=M_2(\mathcal N(V)),\qquad
 A_2=T M_2(\mathcal N(C_1))T^*,\qquad
 B=\operatorname{diag}(\mathcal N(C_1),\mathcal N(C_2)).
\]
These algebras give Ueda's tracial amalgamated free product model \(M_2(\mathcal N(J))=A_1*_{B}A_2\).
In Ueda's convention take \(D=\mathcal N(C_1)\) and \(\theta(\iota_1(c))=\iota_2(c)\), so the stable unitary satisfies \(t\theta(d)t^{-1}=d\).
The reduced HNN algebra is the group von Neumann algebra here by the group HNN normal form. [Ueda, arXiv v4, §2.1, Proposition 2.1](https://arxiv.org/pdf/math/0601706)

Use the two algebraic subrings \(M_2(\mathbb CV)\) and \(T M_2(\mathbb CC_1)T^*\).
They generate \(M_2(\mathbb CJ)\) algebraically, since \(Te_{12}T^*=t e_{12}\) and \((t e_{12}) e_{21}=t e_{11}\), and the first subring supplies all standard matrix units and \((\mathbb CV)e_{11}\).
Their regular coefficient rings are \(M_2(D_V)\) and \(T M_2(D_{C_1})T^*\), respectively, and both have entries in \(D_J\).

Apply the two-row construction to an additive rectangular matrix over these algebraic subrings.
Upon reordering coordinates the common kernel projection \(P\) acts on two blocks of \(N=n+m\) coordinates, and is the kernel projection of the stacked matrix over \(\mathbb CJ\) with \(2N\) input coordinates.
The trace-preserving expectation onto the amplified \(B\) discards the off-diagonal blocks and applies the group expectation \(E_{C_i}\) to diagonal block \(i\).
For the coordinate projection \(e_i\), put \(H_i=E_{C_i}(P)\), taking the expectation of the full matrix entrywise.
The edge restriction gives \(r_i=s(H_i)\in M_{2N}(D_{C_i})\) for each \(i\).
The supports of \(e_iH_i e_i\) and \(e_i r_i e_i\) coincide, because a vector \(v\in e_i\ell^2(J)^{2N}\) satisfies \(\langle H_i v,v\rangle=0\) exactly when \(r_i v=0\).
Regularity of \(D_{C_i}\) now puts the support \(q_i\) of that diagonal block in \(M_N(D_{C_i})\).
It follows that \(Q=\operatorname{diag}(q_1,q_2)\) is over both regular coefficient rings after amplification, since \(tD_{C_2}t^{-1}=D_{C_1}\).
The two-row and graph projection formulas give \(p_{\ker Y}\) with entries in \(D_J\).

### Arbitrary matrices and completion of the induction

In each of the two constructions, every entry of a matrix over the algebraically generated ring is a finite sum of products of elements from the two subrings.
For an entry containing a product \(uv\) in position \((i,j)\), put \(Z=Y-e_iuv e_j^*\), where \(e_i,e_j\) are coordinate columns, and replace \(Y\) by
\[
 \begin{pmatrix} Z&e_i u\\ -v e_j^*&1\end{pmatrix}.
\]
The last equation forces \(y=vx_j\) and the remaining equations say \(Yx=0\).
Splitting off the first factor of each word decreases the total number of multiplications in the chosen words until all entries are additive.
All factors are bounded, so deletion of the added coordinate maps kernels bijectively with bounded inverse at each step.
For the HNN construction a coordinate here is one two-dimensional matrix block.
Starting with the additive kernel projection and applying the graph projection formula at each deletion yields the kernel projection of the initial matrix over \(D_J\). [Group-ring word linearization](Yin_C_A0119_v1.md#amalgams-and-arbitrary-rectangular-matrices)

For the HNN step in particular, take an arbitrary \(X\in M_{m,n}(\mathbb CJ)\) and apply this argument to the block matrix with entries \(X_{ij}I_2\).
After reordering, its kernel projection is \(p_{\ker X}\oplus p_{\ker X}\), so taking one diagonal corner gives \(p_{\ker X}\) over \(D_J\).
In both steps all finite group-ring kernel projections are therefore over \(D_J\), which gives regularity of \(D_J\) by the [finite-support characterization](Yin_C_A0132_v1.md#consequences-for-the-unrestricted-equation).
Induction over the tree edges and then the other edges proves the assertion for \(G\).
The [finite-marking equivalence](Yin_C_A0131_v1.md#which-rationality-is-detected) gives the stated criterion for each affiliated element.

The same regularity conclusion holds for a connected graph with countable fundamental group under the same edge hypotheses.
Fix a base vertex and a maximal tree.
Each finite group-ring matrix uses only finitely many vertex groups, edge letters and paths in that tree.
Its entries therefore lie in the group algebra of the fundamental group of a finite connected subgraph containing the relevant tree paths.
Restriction of each required \(G\)-action to this subgroup still satisfies the two hypotheses.
The finite-graph conclusion gives its kernel projection there, and extension over right cosets gives the same kernel projection in \(G\).
The finite-support characterization applies once more.

For finite edges, Sánchez-Peralta proves the strong Atiyah conjecture from the strong Atiyah conjecture at the vertices and a finite least common multiple of the orders of the finite subgroups of \(G\).
The present argument gives regularity from regular vertex division closures, allows unbounded orders of finite subgroups, and includes the infinite edges satisfying the action and ring hypotheses. [Sánchez-Peralta, Theorems 1.1 and 1.2](https://doi.org/10.1007/s00039-025-00710-4)

## Assessment history

### Decision graph-regularity

| Field | Value |
| --- | --- |
| date | 2026-11-25T11:08 |
| status | proved |
| reason | Finite edge stabilizers give the rational expected support needed for the free product and HNN recovery formulas. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Regular vertex division closures, finite stabilizers on amenable edge actions, and deletion for finitely generated groups. |
| argument | [Argument](#argument) | Coset restrictions, the two-row formula, the HNN matrix model and induction over finite subgraphs. |
| dependency | [Coset restriction](Yin_C_A0119_v1.md#exact-solutions-supported-on-finitely-many-cosets) | Finite support and the kernel dimension bound on one orbit. |
| dependency | [Expected support and graph projections](Yin_C_A0142_v1.md#argument) | Free vertex rows and compression after linearization. |
| dependency | [Free projection identity](Yin_C_A0007_v13.md#free-vertex-projections-with-a-common-kernel-of-full-expected-support) | Disjoint initial supports at the full expected support. |
| dependency | [Matrix inverse closure](Yin_C_A0132_v1.md#argument) | Gram inversion and regularity from group-ring kernel projections. |
| dependency | [Finite marking](Yin_C_A0131_v1.md#which-rationality-is-detected) | Regularity implies deletion of the local condition. |
| dependency | [Ueda's matrix model](../audits/literature/Ued08/Yin_U001.md#ued08-u001) | Section 2.1, Proposition 2.1 for reduced HNN extensions. |
| review | [Graphs of groups](../audits/reviews/Yin_R_A0170_v1.md#graphs-of-groups) | Independent review of the complete statement and argument. |

## Current assessment

[Selected decision](#decision-graph-regularity)

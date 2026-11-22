---
author: Yin
---
# Independent review of rational cyclic kernel support from a coamenable subgroup

## Whole finding

At 2026-11-22T04:44 UTC I independently checked the whole statement and argument of C_A0119_v1 for Yin.
I had the fixed proof and its indicated obligations, took no part in developing it, and received no development dialogue, author explanation or previous verdict on this proof.
I checked the previously proved graph identity and Promislow vertex result at their points of application.
The coamenable action gives the asserted rational projection for every finite rectangular complex group-ring matrix, and the graph identity gives the stated conditional permanence result.

For each left coset \(xK\), the isometry \(\delta_k\mapsto\delta_{xk}\) intertwines right \(K\)-translations.
The matrix trace over finitely many such copies adds the diagonal coefficients at their representatives, and right \(G\)-invariance of the global projection makes each coordinate's diagonal constant.
For a point of \(I=\bigcap_{s\in S}sF\), all possible input cosets \(s^{-1}xK\) belong to \(F\).
Thus the image of \(D_F=\overline{C_F\ker A}\) under \(A\) lies in the \(m|SF\setminus I|\) output copies of \(\ell^2(K)\).
The positive contraction \(C_FPC_F\) is dominated by its range projection, and polar decomposition of \(A|_{D_F}\) bounds the dimension lost in passing to its kernel by that output dimension.
Writing \(p_F\) for this kernel projection gives \(p_F=C_Fp_FC_F\le C_FP_WC_F\), since its vectors belong to the global span \(W\) of right translates.
The boundary splits into \(SF\setminus F\) and \(F\setminus I\), bounded together by \(\sum_s|sF\triangle F|\).
The Følner estimate and faithfulness now identify \(W\) with the entire kernel even for nonnormal \(K\).
If \(K\) is normal, right translation takes a left \(K\)-coset to another one, so the finite-coset solutions themselves form a dense linear space.

The stabilizer in \(H\) of \(tK\) is \(H\cap tKt^{-1}\).
After a right translation, two points \(h_i=xk_it\) of \(H\) in the translated coset satisfy \(h_1^{-1}h_2=t^{-1}k_1^{-1}k_2t\), so freeness at \(t^{-1}K\) forces equality.
Every generating vector therefore restricts to a finite Laurent column.
With extension by zero \(J\), the support of \((J^*P)(J^*P)^*\) is the projection onto the closure of these restrictions' linear span.
For a rational basis selected from them, a nonzero maximal minor makes the Gram matrix invertible almost everywhere, and its projection formula defines a multiplier of norm at most one.
This multiplier fixes every restricted column by rational linear dependence.
In the other direction right \(H\)-translation preserves the restricted family, so its closed span contains the images under the basis matrix of all Laurent polynomial columns, hence the closure of the whole multiplier range.
Its projection is the same fiberwise Gram projection, including the zero projection for the empty basis.
The unnormalized trace is the integral of the constant almost everywhere rank.

Stacking the two vertex rows gives a finite matrix over \(G\) with exactly the full graph as kernel.
The signs give \(y=Y_1x=-Y_2x\), as required in C_A0007_v13, and the edge trace uses \(m+n\) input coordinates.
After cancellation a rational pole on the circle would contradict essential boundedness.
The common denominator is therefore invertible as a multiplier, and composing \(R_jQ\) on the right with this multiplier preserves its range even for a noncentral edge.
Both cleared ranks are the numbers of input coordinates minus the corresponding vertex nullities.
For a word of length \(d\ge2\), writing its first weighted letter as \(u\) leaves a suffix \(v\) of length \(d-1\).
Eliminating the new coordinate \(y=vx_j\) gives precisely the original rectangular equation, with bounded equivariant inverse given by coordinate projection on the graph.
The excess length drops from \(d-1\) to \(d-2\), and iteration preserves nullity for the entire matrix.
The resulting proof uses complex vertex integrality because the coefficients of arbitrary restricted solution vectors can be complex.

In the double, \(\langle b^2\rangle\) has infinite index in the rank-three translation subgroup, and \(b^2\ne b^{-2}\) verifies noncentrality.
The presentation makes the abelianization finite, whereas the fold onto the virtually abelian vertex embeds \(\langle b\rangle\).
For a finite orbit in the amalgam tree, the center of its finite spanning subtree is a vertex or an edge whose endpoints have different types, so the finite-order element fixes a vertex.
The kernel of the fold meets every conjugate vertex stabilizer trivially.
Its quotient of the tree has two vertices and one edge for each coset of \(\langle b\rangle\) in the fold image, by the coset description and normality of the kernel.
Choosing one edge to join the two vertices leaves countably infinitely many free generators. [Serre, *Trees*, I §§3.3 and 4.1, Theorems 4, 4′ and 7](https://doi.org/10.1007/978-3-642-61856-7).
The torsion-free double consequently belongs to the known free-by-elementary amenable class.
For two free generators, the adjoint of the first difference has zero kernel on each infinite orbit, so the row has rank one and nullity one.
A finitely supported nonzero chain on any right coset of the free subgroup would have a nonzero coefficient at a leaf in its boundary.
This example distinguishes finite coset support from finite ordinary support and supplies no general existence theorem for a coamenable action free on the edge.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0119_v1.md#statement) | Both action hypotheses, the amenable quotient criterion, complex rational support, its unnormalized trace, and the conditional arbitrary-matrix amalgam conclusion. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0119_v1.md#argument) | Whole argument, including the relative Følner estimate for nonnormal subgroups, cyclic compression, graph ranks, finite word elimination and the Promislow example. |
| [Whole finding](#whole-finding) | [Graph-rank identity](../../claims/Yin_C_A0007_v13.md#two-rows-on-the-support-of-their-common-kernel) | The common-kernel graph, its dimension and both vertex ranks on its complete expected support. |
| [Whole finding](#whole-finding) | [Cyclic denominators](../../claims/Yin_C_A0007_v13.md#clearing-cyclic-denominators-in-the-vertex-matrices) | Order of multiplication and the coefficient field required for each cleared vertex matrix. |
| [Whole finding](#whole-finding) | [Translation subgroup](../../ledger/Yin_L_A0024_v1.md#fixed-setting-and-proposed-test) | Fixed presentation, torsion-freeness and rank-three translation subgroup of index four. |
| [Whole finding](#whole-finding) | [Vertex integrality](../../claims/Yin_C_A0013_v1.md#the-complete-task-interface-and-its-remaining-generalization-gap) | Existing all-matrix, complex-coefficient conclusion for the Promislow vertices. |
| [Whole finding](#whole-finding) | [Known positive results](../../ledger/Yin_L_A0001_v1.md#known-positive-results) | The established torsion-free free-by-elementary amenable class already covers the double. |

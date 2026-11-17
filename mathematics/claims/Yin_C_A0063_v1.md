---
author: Yin
---

# Central two-group signatures for loop pairings invisible in first homology

## Statement

Let \(X\) be a connected aspherical complex formed by coning two connected rooted graphs \(A,B\) to a rose, as in the [homology matching test](Yin_C_A0055_v1.md#statement).
Let \(G=\pi_1 X\), let \(\eta:G\to Q\) be a known quotient, and choose root paths on both sides.
For every \(q\in Q\) choose a homomorphism \(\psi_q:\pi_1(B,b_0)\to P\) into one finite two-group \(P\).
Only the indices actually used by a finite list of witnesses have to be specified, the rest may have trivial maps.

Suppose an \(A\)-path \(x\to x'\) reads the word of a closed \(B\)-path \(C\) at \(b\).
Write \(g_x,h_b\) for the root labels in \(G\) and \(l_b\) for the chosen path in \(B\) from \(b_0\) to \(b\).
If \(\psi_q(l_b C l_b^{-1})\) is central in \(P\) and has square one for \(q=\eta(g_xh_b^{-1})\), assign this value to the corresponding equality edge.
Then every cycle of such edges has product one, including after transporting their endpoints by common readable steps.
Every two pairings saturating the same vertices have equal products of their edge values, for any number of right-side base vertices.
The same assertions apply to explicit proofs using conjugates of relators from both graphs whenever the individual opposite-side factors evaluated as below lie in this central subgroup.
These tests concern signatures of relator witnesses even when \(G\) has no finite quotient by \(P\).

The test can detect incompatible pairings even if all opposite-loop vectors of those pairings vanish in first homology over the integers and the [first-homology signature equalities](Yin_C_A0055_v1.md#certificates-using-several-graph-relations) hold for every filling.
The example below has torsion-free group, separated designated roots and complete erasure of its left color \(3\), with a cone complex failing asphericity and vertex types different from the four-line prescription.

## Lifting independent maps from translated right-side graphs

Let \(X_A\) be the complex with only the \(A\)-cone attached and set \(G_A=\pi_1 X_A\), \(N=\ker(G_A\to G)\).
The inverse image \(Y\) of \(X_A\) in \(\widetilde X\) is connected because \(G_A\to G\) is surjective, and \(\pi_1Y=N\).
Choose paths in \(Y\) from its basepoint to the lifts of the \(B\)-root at all \(g\in G\), with associated elements \(s_g\in G_A\) lifting \(g\).
They can be chosen as lifts of rose words since the rose already surjects onto \(G_A\).
This gives the homomorphisms from the individual \(\pi_1(B)\)'s into \(N\) by lifting the \(B\)-loop at the selected vertex and transporting back along that path.

The complex \(\widetilde X\) is obtained from \(Y\) by attaching the translated \(B\)-cones.
Relative cellular homology and the long exact sequence of this pair give
\[
      \bigoplus_{g\in G} H_1(B;\mathbb F_2)\ \simeq\ H_1(Y;\mathbb F_2).
\]
Indeed \(H_1(\widetilde X)=H_2(\widetilde X)=0\), and each relative cone contributes the first homology of its base to relative degree two.
Also \(H_2(Y;\mathbb F_2)=0\), since \(Y\) is a subcomplex of the contractible two-dimensional \(\widetilde X\) and degree-two cycles there are already zero chains.
Over the field this gives \(H^2(Y;\mathbb F_2)=0\).

We show that arbitrary prescribed homomorphisms from all the based translated copies of \(\pi_1(B)\) to a finite two-group \(P\) extend simultaneously to a homomorphism \(\rho:N\to P\).
The extension also follows from Stallings's mod-\(p\) lower central series theorem at \(p=2\), as restated by Cochran and Harvey. [Sta65](https://doi.org/10.1016/0021-8693%2865%2990017-7) [CH08, Theorem 1.1, p. 678](../literature/pdf/CH08.pdf#page=2)
Indeed the map from the free product of the based translated groups to \(N\) induces the displayed isomorphism on first homology, and \(H_2(N;\mathbb F_2)=0\) since attaching cells of dimension at least three to \(Y\) gives a classifying space for \(N\).
The two groups therefore have isomorphic finite-stage mod-two lower central quotients, and every homomorphism into a finite two-group factors through such a stage.
Induct on \(|P|\), with the trivial case immediate.
Choose a central subgroup \(Z\) of order two. First extend all prescriptions modulo \(Z\) by induction.
Represent the resulting homomorphism by edge transports on \(Y\), for instance using paths in a spanning tree to define transports.
Lift those transports arbitrarily to \(P\), using inverse values on reversed edges.
Around each two-cell the error lies in \(Z\), giving a cellular two-cochain with constant coefficients.
As \(H^2(Y;\mathbb F_2)=0\) and \(Y\) has dimension at most two, it is a coboundary.
Correcting the lifts by the corresponding one-cochain removes every error, since \(Z\) is central, yielding a lift to \(P\) on \(\pi_1Y\).
On each based translate this lift and its prescribed homomorphism agree modulo \(Z\), so their pointwise discrepancy is a homomorphism to \(Z\).
The direct-sum isomorphism in first homology extends all of these discrepancies to a single homomorphism \(N\to Z\).
Multiplying the lift by this central correction realizes the exact prescriptions.
Cellular cochains here may be arbitrary functions, including when the deck set is infinite.

## Evaluating an equality certificate

Apply the lifting assertion with prescription \(\psi_{\eta(g)}\) on the copy indexed by \(g\).
Let \(v_x\in G_A\) be the label of a path in \(A\) from its root to \(x\), independent of the path because the \(A\)-cone is already attached.
For a true equality \(g_x=g_{x'}\) the element \(v_{x'}v_x^{-1}\) lies in \(N\).
For the displayed copy this element in \(G_A\) is
\[
 (v_x \bar l_b^{-1})\,\overline{l_b C l_b^{-1}}\,(v_x\bar l_b^{-1})^{-1},
\]
where bars in this formula denote labels in \(G_A\).
Its conjugating element differs from \(s_{g_xh_b^{-1}}\) by left multiplication by an element of \(N\).
Centrality makes that extra conjugation immaterial after applying \(\rho\), so the value is exactly the assigned one.
After a common right step labelled \(t\), the displacement in \(G_A\) is \((v_{x'}t)(v_xt)^{-1}=v_{x'}v_x^{-1}\).
Along any auxiliary cycle these displacements telescope when multiplied in reverse traversal order.
Their images belong to the central subgroup of exponent two, so reversal, order and orientation no longer affect the result.
The symmetric difference of two matchings saturating the same set has even incidence at every vertex, and decomposes into cycles, proving the comparison.

For a path certificate given as a product of conjugates \(u_j R_j^{\pm1}u_j^{-1}\) in the free rose group, each \(A\)-relator is already trivial in \(G_A\).
For a \(B\)-relator at \(b_j\), base it by \(l_{b_j}\) in \(\pi_1 B\) and take the assignment at the quotient index \(\eta(g_x\bar u_j h_{b_j}^{-1})\), using the image of \(u_j\) in \(G\) for this index.
The preceding conjugation calculation applies to each factor.
When each assigned value is central of square one, their product therefore gives the signature of the displacement.
It is computable from the paths, finite group maps and equality of the supplied indices in \(Q\), without constructing \(\rho\).
A list that does not meet the centrality assumption is not tested by this recipe.

## Two pairings of commutator copies

Take two simple cycles of length \(m\ge3\) wedged at the root of \(B\), with positive words \(U,V\), using their own pairwise distinct rose letters at all positions.
Give the wedge root color zero. Give the first interior vertex \(b_1\) of \(U\) color one and every other interior vertex on both cycles color two.
Assign each signed letter its resulting increment to \(C_7\); the disjoint letter sets make this consistent.
Set \(W=UVU^{-1}V^{-1}\). Let \(W'\) be its cyclic shift starting at \(b_1\) on the forward traversal of \(U\), so \(W\) and \(W'\) are closed readings in \(B\) at different phases.

Build \(A\) with a private letter \(r\) of color three from its root to \(x_1\), with three successive arcs \(x_1\to x_2\to x_3\to x_4\) reading \(W\), and a fourth arc \(x_1\to x_4\) reading \(W'\).
Take all interior vertices fresh.
The first letters of \(W,W'\) are different, as are their terminal letters, and the splices \(WW\) are reduced, giving an immersed graph.
Its core cycle has length \(16m\), while \(B\) has girth \(m\).
The resulting group equals the group obtained by coning just \(B\): the relators \(U,V\) already kill \(W,W'\) and the single \(A\)-core relator.
Eliminating one private letter from each of \(U,V\) yields a free group with the stated \(C_7\) quotient.
The right root is unique in its color. Each non-root left label involves the free letter \(r\) once, so the left root also has a unique label.

On the long three-arc path, color three occurs thirteen times, once at each of its macro-vertices between successive traversals of \(U^{\pm1},V^{\pm1}\), including the two ends.
The \(W'\)-arc starts at the \(B\)-phase of color one. In a full cyclic traversal of \(W\) that phase occurs exactly twice, on the forward and reverse traversals of \(U\), so this arc adds exactly one interior vertex of color three.
All fourteen labels equal \(r\), since each of the two contributing right-side phases is a return to the actual starting vertex of that closed word in \(B\).
Thus the entire color erases in this cone group.

On the four marked \(x_i\) one pairing uses two \(W\)-copies, and the other uses one \(W\)-copy and one \(W'\)-copy.
They extend to full pairings by using identical pairs on the ten other vertices. The obstruction below already occurs on the four marked vertices.
All four witnessed first-homology vectors are zero, even with their actual deck indices.
More generally every translated \(A\)-cycle maps to zero as an integral Cayley edge chain, since \(W\) is the commutator of two closed Cayley paths, and \(W'\) is its conjugate.
All translated \(B\)-cycle chains are independent there: the complex coning only \(B\) is aspherical by the two free edge eliminations, and its universal-cover relative sequence identifies precisely those \(B\)-summands with the first homology of the Cayley graph.
These two facts imply first-homology consistency for all versions of the comparison in [C55](Yin_C_A0055_v1.md#certificates-using-several-graph-relations): a sum of \(A\)-cycle chains is zero, so any equal sum of \(B\)-cycle chains has zero total in every translated summand.

For the central test take \(P\) to be the upper unitriangular \(3\)-by-\(3\) matrices over \(\mathbb F_2\).
At quotient index three send the two generators \(U,V\) of \(\pi_1 B\) to \(I+E_{12},I+E_{23}\), respectively. At every other index use the trivial homomorphism.
The commutator at index three has nonidentity central value \(I+E_{13}\), of order two.
Each \(W\)-edge has this index and each \(W'\)-edge has index \(3-1=2\), so the two pairing totals on the four vertices differ.
The cone complex is therefore not aspherical.
This illustrates the additional test on a whole alternating cycle of certificates.
Its agreement on a single collection of disjoint pairs without alternative certificates would not prove or disprove a complete pairing in the specified four-line groups.

## Assessment history

### Decision central-two-group-signatures

| Field | Value |
| --- | --- |
| date | 2026-11-17T10:53 |
| status | proved |
| reason | Independent review verified the extension of the prescribed finite two-group maps, the central displacement test, and the commutator example that distinguishes two full pairings. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Consistency of central square-one signatures on an aspherical cone and detection of incompatible pairings beyond first homology in the stated example. |
| argument | [Proof](#lifting-independent-maps-from-translated-right-side-graphs) | Direct central lifting, based conjugators, common-step transport, matching comparison and the nonaspherical example with torsion-free group. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0099_v1.md#whole-argument-finding) | Independent review of the extension, certificate identities, and the precise group and complex hypotheses in the example. |

## Current assessment

[Selected decision](#decision-central-two-group-signatures)

---
author: Yin
---

# Counting the independent cycles in a two-coordinate kernel test

## Statement

Let \(U=\mathcal U(G)\) and let \(L\) be a finite rectangular matrix over \(\mathbb CG\).
Use the bipartite support graph with one edge per group term of every entry, so distinct terms at the same position give parallel edges.
For two distinguished input coordinates write \(h,b\) for the joint and separate regular rank increments in the [two-coordinate test](Yin_C_A0255_v1.md#statement).
If \(b>h\), both coordinates lie in one connected component and either individual coordinate image of \(\ker_U L\) has dimension strictly between zero and one.

Fix any spanning tree on this component and apply the [tree normalization](Yin_C_A0207_v1.md#localization-and-the-weighted-matching).
Write the resulting matrix as \(K_0+\sum_{g\ne1}K_g g\) with complex coefficient matrices.
Make a list with each \(g\ne1\) occurring \(\operatorname{rank}_{\mathbb C}K_g\) times.
Some pencil of columns \(c_i g_i-d_i\) on precisely this list, allowing zero columns, must have noninteger regular rank.
The list length is at most the cycle rank \(c=|E|-|V|+1\) of the component.
In particular the following cases exclude \(b>h\).

* The displayed group labels generate a torsion-free group satisfying complex strong Atiyah, in particular an infinite cyclic group or the trivial group.
  Thus at most one independent cycle on the component suffices for exclusion in any torsion-free group.
* Suppose \(G\) is torsion-free with regular scalar group-ring injectivity.
  A list of length at most two excludes the strict inequality, so every such witness needs at least three independent cycles in its distinguished component.
  Arbitrary length on two labels up to inversion also excludes it when one orientation class occurs only once.
  On a list of length three, the only case left has three labels distinct up to inversion, every pair freely generating a free group of rank two, and no integer character of the subgroup of all three that vanishes on two and is nonzero on the third.
  The character deletion test below can also be applied to longer lists.

There is a corresponding restriction on each of the two [local relation matrices for a traceless system](Yin_C_A0254_v1.md#the-original-group-ring-matrices).
Choose the first-leg basis to contain \(x_1,x_2\) and the second-leg basis to contain \(y_1^*,y_2^*\), so its two constant columns or rows are coordinate vectors.
On each side separately the two distinguished vertices must belong to one component, and that distinguished component must fail the applicable list exclusions above.

For torsion-free \(G\) there is also a coefficient-dependent test on square minors with any number of independent cycles, using neither scalar injectivity nor a character of the group.
It suffices that the competing directed cycles inside each strongly connected part of a chosen matching are single cycles and that none of their ordered products is resonant, in the precise sense below.

## Reducing a support component to a list of rank-one coefficients

Disconnected components give independent matrix equations and independent kernel coordinates.
If the distinguished coordinates lie in different components, their joint projected image is the product of the two individual images; the image on summing them has dimension at most this joint dimension.
If one individual image is zero, then \(b=h\).
If one is all of \(U\), then \(b=1\le h\).
These observations prove the first assertion.

For a connected component let \(p_v\) be the group product on the tree path to \(v\), using inverse labels backwards.
The gauge multiplying row \(i\) by \(p_i\) and column \(j\) by \(p_j^{-1}\) makes every tree term constant and preserves the rank.
All nonconstant terms are consequently contributed by the \(c\) non-tree edges.
A single group term carries a coefficient supported at one matrix position.
Summing ordinary ranks at each resulting group element thus gives at most \(c\), even after collisions or cancellations.
The dimension of an individual kernel coordinate is unchanged by the gauge: its image is just multiplied by a group unit.
The joint dimension is likewise unchanged.
The sum of the images of two coordinates need not be preserved by their different column gauges; the reduction uses the individual fractional dimension already obtained.

Here is the linearization for any matrix \(K=K_0+P\operatorname{diag}(g_1,\ldots,g_d)Q\) with \(K_0,P,Q\) constant, obtained from rank factorizations of its nonconstant coefficients.
The matrix
\[
    \begin{pmatrix}K_0&P\operatorname{diag}(g_1,\ldots,g_d)\\-Q&I_d\end{pmatrix}
\]
has regular rank \(d+\operatorname{rk}_G K\) by eliminating the constant identity.
Its first columns are constant.
Quotient the complex output space by their span and apply this constant quotient map to the last \(d\) columns.
The remaining matrix has columns of the form \(c_i g_i-d_i\), and its rank differs from \(\operatorname{rk}_G K\) by an integer.
This includes the empty list.

For a fractional individual coordinate image, adjoining its coordinate row to the component increases rank by its dimension, by restricting the row to the kernel.
After the tree gauge its row can be made the same constant coordinate row by an additional group-unit row multiplication.
Consequently at least one of the gauged component and its enlargement has noninteger rank, and both have the same nonconstant coefficient list.
The linearization proves the claim.
The argument for a fractional added coordinate column is the transposed construction, or one can apply the same row argument to the adjoint with inverse labels.
For the local matrices both individual increases and the increase from adjoining the two together equal \(1/2\).
If the two vertices lay in different components the increases would instead add to one.

When the label subgroup satisfies the stated integrality hypothesis, coset replication computes the same ranks inside \(G\).
Generally, a noninteger pencil on the list gives an ordinary rank-one commutator sum with at most one rank-one input for each occurrence by the [prescribed-list theorem](Yin_C_A0167_v2.md#statement).
Zero inputs may be removed and inverse labels combined without increasing total rank.
The [two- and three-input exclusions](Yin_C_A0166_v2.md#statement) now give the asserted budget and pair restrictions under regular scalar injectivity.
For an integer character on the label subgroup nonzero on a single occurrence and zero on every other label, [deletion of the isolated occurrence](Yin_C_A0167_v2.md#deleting-a-label-separated-by-a-character) preserves the existence of a noninteger pencil.
One may repeat this test on the remaining subgroup and list.

## Cycles in a matched minor

Consider a square submatrix with a specified perfect matching of nonzero monomial terms.
Order the positions along the matching and use a group monomial and a nonzero scalar on each row to make its matched term \(1\).
For each remaining term of entry \((i,j)\) draw a directed edge \(i\to j\), labeled by its coefficient and group element after this normalization.
Allow loops and parallel edges.
Suppose each strongly connected component is a single vertex with no internal edge, or its internal edges form exactly one directed cycle, including a possible loop.
A permutation gives block triangular form.
On a cycle of length \(t\), write the successive internal terms as \(a_i u_i\) in cyclic order.
The block equations are \(x_i=-a_i u_i x_{i+1}\).
The kernel is isomorphic, by its first coordinate, to that of
\[
                 1-(-1)^t(a_1\cdots a_t)\,u_1\cdots u_t .
\]
For a torsion-free group this scalar is an affiliated unit unless both the group product is the identity and \((-1)^t\prod_i a_i=1\).
Indeed any nonidentity product acts as a bilateral shift on its cyclic cosets.
The exceptional case is called resonant here and has a one-coordinate kernel on that diagonal block.
No resonance on any block therefore makes the entire square minor an affiliated unit.
This argument does not count the kernel of a triangular matrix by adding kernels of singular diagonal blocks.

If each of the two local relation matrices admits such a nonresonant minor of size its free inner rank, their original regular ranks both reach their free inner ranks, contradicting the [required rank loss](Yin_C_A0254_v1.md#numerical-labels-and-the-free-inner-rank-loss).
More generally a minor of size a known upper bound for the regular rank certifies that exact integer rank.
Such minors for the original component and its coordinate-row enlargement therefore exclude a fractional increment.
A matching size upper bound can for example be obtained from any vertex cover of the positions: splitting a matrix into the part on the selected rows and the remaining part on the selected columns gives a factorization through their total number.

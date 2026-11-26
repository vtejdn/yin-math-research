---
author: Yin
---

# Testing a kernel coordinate by one additional group translation

## Statement

Let \(G\) be a discrete group and \(L\) a finite matrix over \(\mathbb CG\).
Fix an input coordinate \(i\) and let \(pU\) be the image of the affiliated kernel of \(L\) on this coordinate, where \(U=\mathcal U(G)\), \(p\) is its orthogonal support projection, and \(\alpha=\tau(p)\).
For \(g\in G\) add one input \(y\) and the single equation \(y=gx_i\), retaining the rows of \(L\) with zero final column.
On the two distinguished coordinates \(x_i,y\) write \(h_g,b_g\) for the joint and separate rank increments of the [original group-ring test](Yin_C_A0255_v1.md#statement).
Then
\[
  h_g=\alpha,\qquad
  b_g-h_g=\alpha-\tau(p\wedge gpg^{-1})
       \ \ge\ \tfrac12\|gp-pg\|_2^2 .
\]
In particular \(b_g>h_g\) exactly when \(gpg^{-1}\ne p\).
For any generating list of \(G\), one of its entries gives a positive difference if \(p\) is noncentral.
For the center-valued trace \(Z\),
\[
                 \sup_{g\in G}(b_g-h_g)\ge\|p-Z(p)\|_2^2.
\]
In an ICC group this lower bound is \(\alpha(1-\alpha)\).
Each positive difference gives an actual two-square matrix algebra on a scalar regular-closure corner of trace \(2(b_g-h_g)\).

More particularly, suppose \(a,b\in G\) freely generate a free group \(F\) on these two generators and that \(C_F(h)\) is cyclic or trivial for every \(h\in G\setminus\{1\}\).
This applies to \(G=K*F\) with any discrete \(K\).
For at least one \(g\in\{a,b\}\) one has
\[
                  b_g-h_g\ge(1-\sqrt3/2)\alpha(1-\alpha).
\]
The original matrix may involve both \(a\) and \(b\).

For any input \(X\) of noninteger regular rank \(\rho\) on \(m\) columns, one can take \(L\) to be a column prefix of \(X\), and \(i\) its last column, with \(\min(\alpha,1-\alpha)\ge\Delta\), where \(\Delta=\operatorname{dist}(\rho,\mathbb Z)/m\).
Thus in an ICC group the single-row extensions of this one prefix have supremum at least \(\Delta(1-\Delta)\); in the two-generator conjugation test the lower bound \((1-\sqrt3/2)\Delta(1-\Delta)\) is attained or exceeded by one of the two named choices.

## Keeping the given matrix as a block

The enlarged polynomial matrix is
\[
                    L_g=\begin{pmatrix}L&0\\-g\,w_i&1\end{pmatrix}
\]
with \(w_i\) the constant coordinate row.
Projection of its kernel to the distinguished coordinates gives the graph \(\{(v,gv):v\in pU\}\).
This module has dimension \(\alpha\), and the sum of the separate images is \(pU+gpU\), giving the formula for \(b_g-h_g\) by dimension additivity.
The positive compression \(p(gpg^{-1})p\) dominates the meet, giving the squared Hilbert norm estimate by expanding \(\|p-gpg^{-1}\|_2^2\).
Equality \(b_g=h_g\) forces \(p\wedge gpg^{-1}=p=gpg^{-1}\) by equal traces and faithfulness.
Commutation with every generator is exactly centrality.

The image of \((1-p)gp\) has dimension \(b_g-h_g\), by projecting the sum of the two coordinate images modulo \(pU\).
The original kernel projection and the support of its coordinate image belong to the matrix and scalar regular closures by [matrix regularity](Yin_C_A0255_v1.md#the-two-images-of-the-same-kernel).
The relative inverse identifies the initial and final supports of \((1-p)gp\), lying respectively under \(p,1-p\).
Together they yield the stated corner of twice the difference, as in the [Schur shear calculation](Yin_C_A0257_v1.md#kernel-images-and-the-positive-polynomial-test).

The closed \(L^2\)-convex hull of the conjugates of \(p\) contains \(Z(p)\): its minimum-norm point is invariant, and its pairing with every central vector agrees with that of \(p\). [Central averaging](Yin_C_A0232_v1.md#a-finite-column-attaining-the-rank)
Consequently \(\inf_g\tau(pgpg^{-1})\le\tau(pZ(p))=\|Z(p)\|_2^2\), proving the supremum bound.
If \(G\) is ICC its center is scalar.
For the prefix assertion let \(r_j\in[0,1]\) be the successive single-column rank increases of \(X\).
The triangle inequality modulo \(\mathbb Z\) gives \(\sum_j\operatorname{dist}(r_j,\mathbb Z)\ge\operatorname{dist}(\rho,\mathbb Z)\).
Choose a position with distance at least \(\Delta\).
The kernel of projection from the prefix kernel to this last coordinate is the preceding prefix kernel, so its image has dimension \(1-r_j\) by rank-nullity.
This gives all stated estimates for \(X\).

## Two fixed choices in the marked group

Identify the conjugation action on \(L^2(\mathcal N(G))\ominus\mathbb C1\) with the permutation action on \(\ell^2(G\setminus\{1\})\) in the group basis.
The graph of each \(F\)-orbit with unoriented \(a,b\) edges is four-regular, counting loops and multiplicities.
It has at most one independent cycle: a reduced based closed walk reads a freely reduced word in the orbit stabilizer, and its word determines its path.
This embeds its fundamental group in a cyclic group or the trivial group.
Any finite induced subgraph on a vertex set \(D\) therefore has at most \(|D|\) internal edges, so at least \(2|D|\) edges leave \(D\).

Let \(P\) be the average of conjugation by \(a,b,a^{-1},b^{-1}\) on this orbit space.
For a nonnegative finitely supported function \(f\), integrate the edge boundary inequality for superlevel sets of \(f^2\).
It gives \(\sum_{\{u,v\}}|f(u)^2-f(v)^2|\ge2\|f\|_2^2\).
Cauchy-Schwarz bounds the square of the left side by the product of the sums of \((f(u)-f(v))^2\) and \((f(u)+f(v))^2\) over edges.
Those two sums are \(4(\|f\|_2^2-\langle Pf,f\rangle)\) and \(4(\|f\|_2^2+\langle Pf,f\rangle)\), respectively.
Thus \(\langle Pf,f\rangle\le(\sqrt3/2)\|f\|_2^2\).
Replacing a complex function by its pointwise absolute value and using density extends this upper bound to the full orbit space and orthogonal sums of orbits.

Apply the estimate to \(f=p-\alpha 1\) in the group trace Hilbert space, with \(\|f\|_2^2=\alpha(1-\alpha)\).
The average of \(\|gpg^{-1}-p\|_2^2\) for \(g=a,b\) equals \(2(\|f\|_2^2-\langle Pf,f\rangle)\), since inverse generators give identical norms.
At least one of the two translations therefore gives the required bound by the first part.

For \(G=K*F\), the free factor \(F\) is malnormal by free-product normal form: conjugating a nonidentity element of \(F\) by a word outside \(F\) retains a syllable from \(K\).
Thus if a nontrivial \(u\in F\) commutes with \(h\), then \(h\in F\).
For \(1\ne h\in F\) its centralizer in \(F\) is cyclic: on its Cayley tree a commuting element preserves the translation axis of \(h\), acts there by a translation and is determined by the image of one vertex.
This proves the orbit hypothesis.

## Assessment history

### Decision a-coordinate-and-a-translated-copy

| Field | Value |
| --- | --- |
| date | 2026-11-26T13:44 |
| status | proved |
| reason | Whole-proof review verified the original polynomial graph, the quantitative excess and the fixed-generator estimate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The coordinate excess, one-generator test, prefix estimate and the two prescribed choices. |
| argument | [Keeping the given matrix as a block](#keeping-the-given-matrix-as-a-block) | Graph kernel, trace and commutator estimates, central average and prefix increment. |
| argument | [Two fixed choices in the marked group](#two-fixed-choices-in-the-marked-group) | The orbit graph and cyclic stabilizers, edge boundary and free-product application. |
| review | [A coordinate and a translated copy](../audits/reviews/Yin_R_A0206_v1.md#a-coordinate-and-a-translated-copy) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-a-coordinate-and-a-translated-copy)

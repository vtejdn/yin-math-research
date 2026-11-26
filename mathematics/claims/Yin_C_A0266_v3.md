---
author: Yin
---

# The complete bipartite obstruction at four independent support cycles

## Statement

Let \(G\) be torsion-free with regular scalar group-ring injectivity.
For any connected component of the bipartite term graph of a matrix over \(\mathbb CG\), count parallel edges separately and put \(c=|E|-|V|+1\).
If \(c\le3\), its regular rank is an integer.
If \(c\le4\), a noninteger rank is possible only if the term graph has \(K_{3,3}\) as a graph minor.
In that case there is a matrix over this same group of the form
\[
                  C=\begin{pmatrix}u-1&v-1\\ w-1&z-1\end{pmatrix},
             \qquad u,v,w,z\in\mathbb C^\times G ,
\]
of noninteger regular rank, differing by an integer from the original component rank.
Here \(\mathbb C^\times G\) denotes the nonzero scalar multiples of individual group translations.

Consequently a [two-coordinate test](Yin_C_A0255_v1.md#statement) with \(b>h\) needs at least four independent cycles in its distinguished component.
If it has at most four, that component must have a \(K_{3,3}\) minor; in particular a planar component cannot give a strict test in this range.
For a [traceless system](Yin_C_A0254_v1.md#statement), the same requirements apply on each side to the component containing its two coordinate vertices in bases adapted to the output vectors.
These statements complement the [two-cycle bound without scalar injectivity](Yin_C_A0266_v2.md#statement).

If \(G\) is also ICC, the existence of a strict test whose distinguished component has at most four independent cycles is equivalent to the existence of a noninteger rank for one of the displayed two-square matrices over this very group.
Given such a matrix with regular nullity \(\delta\), the converse uses an explicit four-square matrix on eleven monomial terms and admits \(\sup_{g\in G}(b_g-h_g)\ge\delta(1-\delta)\).

## Reducing the branch vertices

Remove leaf pivots and isolated vertices as in the [two-cycle elimination](Yin_C_A0266_v2.md#eliminating-rows-with-two-group-terms).
Each pivot changes rank by an integer and leaves the other entries unchanged.
It suffices to consider connected components with minimum degree at least two.
For cycle rank \(c\) their total degree excess \(\sum(\deg(v)-2)\) is \(2c-2\).
Pass to the adjoint matrix if necessary so that the sum over the row vertices is at most \(c-1\).
Passing to the adjoint preserves regular rank and the unoriented term graph.
If the original pruning splits the graph, the cycle ranks of the remaining components sum to at most the original \(c\).

Solve every degree-two row by the scalar group-monomial propagation proved in the same elimination.
The columns in each connected system of these binary equations use one root variable, with each original variable equal to a scalar group monomial times this variable or fixed to zero.
The rows of degree at least three now give a matrix \(T\) on these free root variables.
Its rank differs from that of the original matrix by an integer: the binary subsystem has integer rank and the next rank increment is the rank on its kernel under the explicit parametrization.
Each row of \(T\) has at most as many terms as its original row, including after cancellation.

The term graph of \(T\) is a minor of the initial graph.
For each free root contract the variable vertices and the intervening binary rows of their chosen spanning tree to its root vertex.
Delete the remaining binary rows and any variables pinned to zero.
An edge from a higher-degree row to a variable is thereby redirected to its root; its term is multiplied by the corresponding monomial.
Collection of equal group terms at the same position is achieved on the graph by deleting redundant parallel edges or all cancelled edges.
This explanation uses the labels for the algebraic calculation and only the underlying graph for the minor assertion.

A one-row matrix has integer regular rank, since each nonzero scalar is an affiliated unit.
A two-row matrix with at least one row of at most three terms also has integer rank.
A zero row can be omitted.
If the small row occupies only one column, pivot on that scalar using its affiliated inverse; outside that column the other row stays unchanged and is still over the group ring.
If the small row occupies two or more columns, one entry must be a monomial, because two entries having at least two terms each require at least four terms.
Pivoting on a monomial keeps all residual entries in the group ring and leaves just one row.

When \(c\le3\), the row excess is at most two.
There is at most one higher-degree row, or exactly two each of degree three.
The preceding cases prove integrality.
For \(c=4\) the row excess is at most three.
If there are two higher-degree rows, at least one has degree three and the same proof applies.
The remaining possibility has exactly three rows of degree three before propagation, leaving three rows of at most three terms each in \(T\).

## The only three-row pattern left

Suppose a matrix \(T\) with three rows of at most three terms each has noninteger rank.
It cannot have a zero row or a row or nonzero column with only one occupied position.
Indeed a singleton pivot uses a scalar affiliated inverse with no change to entries in the other rows and columns, leaving at most two rows of at most three terms each.
Discard zero columns.
Call a column full if it has nonzero entries in all three rows.
Every monomial entry must lie in a full column: otherwise its group-ring invertible pivot leaves one other row unaffected outside this column.
The remaining two-row matrix still has a row with at most three terms, giving integer rank.

Each row has at least two positions, so each has a monomial and there is a full column.
If there are exactly two full columns, no row can have an entry elsewhere: that entry would need at least two terms in addition to the two full-column terms.
Thus there are just two columns and a monomial pivot leaves only one column over the group ring, which has integer rank.
If there is exactly one full column, each row uses one monomial there and its remaining two terms at one other position.
These three other positions cannot all use the same column, as it would also be full.
Some other column therefore has a single occupied position, already excluded.
This leaves three full columns, exhausting all nine terms.
Every one of the nine positions is a monomial and their graph is \(K_{3,3}\).

Normalize each entry of the first column to one by left row multiplication by a scalar group monomial, then each entry of the first row to one by right column multiplication of the same kind.
The remaining four entries are again nonzero scalar group monomials.
A constant identity pivot at the top left leaves exactly the displayed \(C\).
If the original component has noninteger rank there can be only one such surviving core, since each requires four independent cycles.
This proves the rank and graph assertions.

## Returning to the two distinguished coordinates

For \(b>h\) the two input vertices belong to the same component and either individual coordinate has a fractional image on the kernel by the [coordinate image test](Yin_C_A0266_v1.md#reducing-a-support-component-to-a-list-of-rank-one-coefficients).
Appending its coordinate row to that component therefore leaves at least one of the original or enlarged ranks noninteger.
A new leaf preserves cycle rank, and attaching leaves cannot create a \(K_{3,3}\) minor: in any model by disjoint connected branch sets, removing the leaf from its branch set preserves connectivity and all required adjacencies, unless the leaf alone was a branch set, which cannot have degree three.
The same argument applies to a distinguished coordinate column in the local relation test or a distinguished row on its other side.
Planarity is preserved under graph minors, and \(K_{3,3}\) is nonplanar by the simple planar bipartite edge bound \(|E|\le2|V|-4\).

Conversely, suppose the displayed \(C\) has noninteger regular rank.
All four entries are nonzero, since a zero entry would allow a singleton pivot or a zero row, giving integer rank under scalar injectivity.
Its rank exceeds one and is less than two, so \(0<\delta<1\).
Complete it to the three-square with first row and column all ones and remaining block \(\left(\begin{smallmatrix}u&v\\w&z\end{smallmatrix}\right)\).
Its kernel is parametrized by that of \(C\) on the last two coordinates, since the first coordinate is minus their sum.
Projection of this kernel to either of its last two coordinates is injective: setting one to zero forces the other to be killed by a nonzero entry of \(C\).
Its coordinate image projection \(p\) therefore has trace \(\delta\).
Attach the [single translation equation](Yin_C_A0264_v1.md#keeping-the-given-matrix-as-a-block) \(y=gx_2\) to the three-square.
This gives the claimed four-square with eleven terms and four cycles.
For ICC \(G\), the bound \(\sup_g(b_g-h_g)\ge\delta(1-\delta)>0\) proves the reverse implication for this original group.

## Assessment history

### Decision support-cycles-and-the-complete-bipartite-minor

| Field | Value |
| --- | --- |
| date | 2026-11-26T13:44 |
| status | proved |
| reason | Independent inspection of the fixed versions verified the cycle budgets, matching hypotheses, surviving binomial core and same-group converse. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Integer ranks through three cycles under scalar injectivity, the necessary minor at four, and the ICC converse. |
| argument | [Reducing the branch vertices](#reducing-the-branch-vertices) | Leaf pivots, binary propagation, graph contractions and low-excess rows. |
| argument | [The only three-row pattern left](#the-only-three-row-pattern-left) | The only possible noninteger three-row survivor and the four binomial entries. |
| argument | [Returning to the two distinguished coordinates](#returning-to-the-two-distinguished-coordinates) | The distinguished component and the converse construction in the original ICC group. |
| argument | [Earlier fixed argument](Yin_C_A0266_v1.md#reducing-a-support-component-to-a-list-of-rank-one-coefficients) | Tree normalization of the labels and the prescribed-list reduction. |
| argument | [Earlier fixed argument](Yin_C_A0266_v1.md#cycles-in-a-matched-minor) | Invertible triangular blocks and the torsion-free matching condition. |
| argument | [Earlier fixed argument](Yin_C_A0266_v2.md#eliminating-rows-with-two-group-terms) | Reduction to a residual trinomial. |
| argument | [Earlier fixed argument](Yin_C_A0266_v2.md#comparing-the-coordinate-tests) | Comparison of group-ring trinomials with two-cycle coordinate tests. |
| review | [Support cycles and the complete bipartite minor](../audits/reviews/Yin_R_A0206_v1.md#support-cycles-and-the-complete-bipartite-minor) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-support-cycles-and-the-complete-bipartite-minor)

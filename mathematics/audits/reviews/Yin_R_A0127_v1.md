---
author: Yin
---

# Independent review of the complex rank of sparse relations

At 2026-11-17T06:40 UTC an agent outside the development of Yin_C_A0091_v1 reviewed its complete statement, argument and cone-filling example for Sheng Yin.
The reviewer had independently reviewed the related short-cycle bound in Yin_C_A0090_v1 and received no development dialogue, author explanation or earlier verdict on Yin_C_A0091_v1.
The source inspection covered the Cayley-graph identification and compression argument on pp. 600–601 of [Lyons–Pichot–Vassout](../../literature/pdf/LPV08.pdf#page=6) and the finite-type cellular conventions in Definitions 1.29–1.30 of [Lück](../../literature/pdf/Luc02--book-manuscript.pdf#page=46).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0091_v1.md#statement) | The two simultaneous unnormalized trace estimates, finite-matrix regular rank, infinite-subgroup Betti bound and tests for erasure. |
| [Whole-argument finding](#whole-argument-finding) | [Argument](../../claims/Yin_C_A0091_v1.md#argument) | Fixed-tuple surplus, cycle-length bound, single-edge deletions and independence over the two coefficient fields. |
| [Whole-argument finding](#whole-argument-finding) | [Compression](../../claims/Yin_C_A0091_v1.md#compression-to-the-finite-edge-set) | Equivariant coset projections, finite trace, group-ring columns and reduced first homology for finitely generated groups. |
| [Whole-argument finding](#whole-argument-finding) | [Cone fillings](../../claims/Yin_C_A0091_v1.md#what-the-independent-cycles-force-in-cone-fillings) | Binary restriction rank, multiplicities over actual Cayley edges, two polygons and disjoint translates. |
| [Whole-argument finding](#whole-argument-finding) | [Original coarse populations](../../claims/Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings) | The side, color and finite neutral marking on which the erasure hypothesis is imposed. |
| [Whole-argument finding](#whole-argument-finding) | [Sampling surplus](../../claims/Yin_C_A0088_v1.md#sampling-inverse-pairs-and-counting-nonisolated-vertices) | The random sum of the retained degrees less twice the number of nonisolated vertices. |
| [Whole-argument finding](#whole-argument-finding) | [Positive-probability event](../../claims/Yin_C_A0088_v1.md#a-finite-length-and-a-positive-fraction-of-alphabets) | Strict probability of the surplus event and the stationary directed-edge entropy estimate. |

## Whole-argument finding

The stated trace bounds and cone-filling inequality follow under their respective hypotheses.
On the fixed erased tuple, C88 gives normalized expected surplus greater than \(1/16\), with upper bound 124.
Since \(1/32+124/4000<1/16\), the event \(2e-2v_0\ge v/32\) has probability greater than \(1/4000\).
All further choices of cycles and both trace estimates use that one sampled alphabet.

While the surplus is at least \(v/64\), there are at most \(v\) nonisolated vertices, so the average degree is at least \(2+1/64\).
In the simple case leaf pruning retains this lower bound, and the stationary directed-edge walk gives mean nonbacktracking entropy at least \(\log(65/64)\) per step by convexity of \(d\log(d-1)\).
There are at most \(n\) possible endpoints, so for \(j=\lceil\log n/\log(65/64)\rceil+1\) the absence of a cycle of length at most \(2j+2\) contradicts the entropy bound.
A loop or a parallel pair supplies the short cycle directly in the multigraph case.
Deleting a single cycle edge in the unpruned graph loses at most two units of surplus, including when the deletion isolates vertices.
The number of steps to pass below \(v/64\) is thus greater than \(v/128\).
Each earliest pivot in a nontrivial linear combination occurs once with coefficient \(+1\) or \(-1\) in its own cycle and disappears from all later ones.
This gives independence over \(\mathbb C\) and after reduction modulo two.

The Cayley edge coordinates are indexed by starting vertex and formally positive letter, even for loops, involutions and equal values of distinct letters.
Translating a short cycle's starting vertex to the identity gives the oriented edge chain of a cyclically reduced null word in \(K\), so the original chain belongs to the range of its coset's copy of \(P_H\).
Choosing another coset representative has no effect on the projection because the range is invariant under all left translations by \(K\).
Before identifying the cosets, every independent supported chain fixed by the projection gives an eigenvector with eigenvalue one in the finite compression.
Its trace is at least the number of such chains by positivity.
The diagonal bound in the other direction is \(\sum_t e_t p_t\le v_0\sum_t p_t\), because each positive type starts at most once at each vertex.
There is one positive coordinate per formal pair and no factor of two or \(1/62\) in this trace.
For the full finite-cycle projection, the original graph gives \(e-v_0+\#\pi_0(B)\ge v/64\) independent fixed vectors.
Division by \(v_0\le v\) gives the bounds \(1/128\) and \(1/64\) on the same event, proving each stated exclusion criterion by contraposition.

For each of the finitely many marked short null words, the integer chain at the identity gives a column whose left translates are precisely the values of its right-convolution operator on coordinate basis vectors.
The projection onto the combined closed image is \(P_H\), and group inversion on every coordinate is unitary and fixes the identity vectors used for the trace.
The adjoint \(\partial_1^*\) takes vertex differences along the marked edges, so its kernel consists of square-summable constants on the connected graph and vanishes for infinite \(K\).
The edge kernel therefore has von Neumann dimension \(62-1\).
Attaching one orbit of two-cells for each finite relator expresses all finitely supported cycles as linear combinations of finite cellular boundaries.
Taking the closure of the union of their spans over finite relator lists gives the range of \(P_\infty\), including for a redundant marking or an infinite list of relators.
Lyons–Pichot–Vassout use the Hilbert orthogonal complement of these closed finite cycles in the square-summable cycles to compute the first group \(L^2\)-Betti number for finitely generated groups.
Lück's cited definitions specify the finite-type cellular convention.
Subtracting \(\operatorname{Tr}_K(P_\infty)\) therefore gives the claimed upper bound for infinite \(K\).

For the binary count, group the triangles of each finite filling by their actual translated cone.
The cancellation of the radial edges within each cone leaves a binary cycle in its source graph, and the sum of the images of those cycles is the prescribed boundary.
Independence of the filled boundaries implies independence of any such chosen preimages, with no injectivity assumption on the map out of the direct sum.
Restriction of their span to the off-alphabet edges has kernel bounded in dimension by the total sparse-subgraph cycle rank.
At each off-alphabet image edge with \(m_e>0\), the restricted coefficients lie in the binary parity kernel of dimension \(m_e-1\).
Adding these dimensions over edges and applying rank-nullity proves the inequality, counting contacts from different copies separately.

In the example a free basis after elimination is \(a_1,\ldots,a_m,b_1,\ldots,b_{m-1},d\).
The internal vertices of the two paths from \(1\) to \(c=a_1\cdots a_m\) are their distinct proper prefix words in this basis, so their union gives the asserted simple cycle.
The vertices of its translates by different powers of \(d\) are disjoint by the free product normal form.
The two polygons meet exactly along the \(c\)-edge, and two translates of the same polygon could share an edge of a given type only if their translating elements agreed, since that type occurs there exactly once.
The example realizes cancellation between different copies and is used only to delimit what the cycle count by itself implies.

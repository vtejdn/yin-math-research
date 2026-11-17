---
author: Yin
---
# Forcing original cone equalities and testing proposed erasures against asphericity

In the [four-line construction](../claims/Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings), each of the three forward colors \(3,5,6\) has \(n/7-4\) vertex occurrences on either side.
Erasure in the original group requires even multiplicity at every *individual* group label over that color.
The following construction achieves all these equalities in the group actually presented by the cones and retains the type counts, character, large girth, connectedness and binary zero product.
Its cone group has torsion, and the original root-separation condition also fails.
A separate necessary test using asphericity restricts which pairings could survive in a genuine Ope26f tuple.

## A matching prescription that forces the equalities in its own group

Keep the four lines, the complete type-and-color populations on both sides, and the inverse pairing from the four-line construction.
Among the chosen rose generators write \(x,y,z\) for the three oriented active letters of changes \(1,2,4\) respectively.
All other generators \(t\) have change zero.
Choose one of them \(h\).
Use \(L=\lfloor c\log n\rfloor\ge3\) with the small positive \(c\) of the [four-line switching estimate](../claims/Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts).
Before completing any bijections, prescribe the following pairwise vertex-disjoint simple cycles on the second side:
\[
 \begin{array}{ll}
     t^{L},\quad t^{L+1} & \text{for every generator \(t\) of change zero},\\
     h^L x^7,\quad h^L y^{-1}x^2,\quad h^L z^{-1}x^4 .&
 \end{array}                                                           \tag{1}
\]
There is one cycle for each indicated word.
They all have zero total change in \(C_7\) and are cyclically reduced as rose words.
To embed one of them, write its letters in cyclic order and propagate the colors from an initial zero.
A vertex between successive letters \(a,b\) needs the two distinct outgoing stubs \(\bar a,b\).
Every such pair occurs in a positive fraction of second-side types, by the projective line and extra-set rules.
Every full type has a linear number of copies in each of the seven colors, including after the bounded four-line adjustments.
The alphabet is fixed, so all required turn-and-color pools have size at least \(c' n\) for one \(c'>0\) and sufficiently large admissible \(n\).
Choose every cyclic vertex fresh across all words, using a total of \(O(L)\) vertices.
Matching the indicated stubs prescribes disjoint entries within their inverse-pair color blocks.
In particular a cycle reading \(t^L\) uses two distinct stubs at each of its vertices, since no signed letter equals its inverse.
Choose all remaining bijections independently and uniformly on the unused stubs of each block.

The actual cone group is \(C_7\) for **every** such completion.
Coning the first two cycles for \(t\) makes both \(t^L\) and \(t^{L+1}\) trivial, hence \(t=1\).
The three remaining cycles impose \(x^7=1,\ y=x^2,\ z=x^4\).
All generators are therefore powers of \(x\) and the group has order dividing seven.
The prescribed increments of all edges ensure that every cone relation maps to zero in \(C_7\).
The image of \(x\) is a generator.
This proves the isomorphism inside the original presentation.

Connected completions of girth at least \(L\) exist for every sufficiently large admissible \(n\).
Here are the extra bounds needed in the presence of (1).
Each block has size \(N+O(1)\) with \(N=(129/16513)n/7\), and at most \(O(L)\) of its pairs have been reserved.
The expected number of edges on short cycles avoiding all prescribed vertices is \(n^{\gamma+o(1)}\) or less for some \(\gamma<1\), by the same cycle counting with denominator \(N-O(L)-j\) for cycle length \(j<L\).
Short cycles meeting a prescribed vertex use only edges in the radius-\(L\) neighborhoods of the \(O(L)\) prescribed vertices.
The bounded degree \(132\) gives \(O(L\,132^{L+1})=n^{\gamma_1+o(1)}\) edges there for \(\gamma_1=c\log132<1\).
Thus at least half the completions have at most \(n^{\gamma'}\) bad edges for some fixed \(\max(\gamma,\gamma_1)<\gamma'<1\).
Every short cycle contains an unreserved edge because the prescribed subgraph is a disjoint union of cycles of length at least \(L\).
Choose such an edge and switch it with a distant nonbad unreserved edge in the same block.
The bad, reserved and near-edge exclusions together use \(o(n)\) choices, and the [switching argument](../claims/Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts) strictly decreases the number of bad edges.
Reversibility and at most \(O(n^2)\) choices per switch give probability at least \(\exp(-o(n))\) of girth at least \(L\) under the reserved law.

In the girth-conditioned reserved law the conditional cost of a further unreserved matching pair after \(s\) other unreserved prescriptions is at most \((N-O(L)-s-O(132^{2L+2}))^{-1}\), by the same distant switch which now also avoids (1).
If a \(j\)-vertex set fails to double upon adjoining its neighbors, some \(2j\)-vertex set contains at least \(\lceil129j/2\rceil\) distinct edges.
At most \(2j\) can be reserved, since the reserved graph has degree at most two.
For \(j\le\rho n\) and fixed small enough \(\rho>0\), use the bound \(2/N\) for each of at least \(\lceil129j/2\rceil-2j\) unreserved prescriptions.
There are at most \((Cn/j)^{2j}\) choices of the larger set and at most \((Cj)^s\) choices of an \(s\)-subset of potential edges in it for \(s=\lceil129j/2\rceil-2j\).
The latter follows by choosing \(s\) among \(O(j^2)\) possible labeled edges.
This gives the summable bound \([C'(j/n)^{60.5}]^j\) for sufficiently small \(\rho\) and excludes all such small components with probability tending to one.
For partitions with smaller part between \(\rho n\) and \(n/2\), the [unconditioned four-line entropy estimate](../claims/Yin_C_A0051_v1.md#connectedness-collection-and-the-erasure-threshold) gives probability \(\exp(-\Omega(n))\) of a partition without a crossing edge.
The prescribed pairs cost at most \(\exp(O(L\log n))\) as a conditioning factor, because each compatible prescription before reserving costs at least \(1/n\) in probability.
The subsequent girth conditioning costs only \(\exp(o(n))\).
This still excludes macroscopic disconnected pieces, proving the claimed existence on both sides.

Take roots in color zero in such a completion.
Every forward group label is exactly its color, so the two collected factors are the indicator sums of \(K=\{0,1,2,4\}\) and \(-K\).
They are nonzero and their product in \(\mathbb F_2[C_7]\) is zero, since the difference multiplicities of \(K\) are four at zero and two elsewhere.
In particular every left occurrence of color 3 is paired inside one actual group-label class, simultaneously with the other erased colors on both sides.
Every connected side also has \(n/7+3\) occurrences of the root label, so root separation fails.
The two disjoint cycles for \(t\) explicitly violate the ordinary-arrangement condition: traverse them in opposite senses, respectively \(L+1\) and \(L\) times, and pair corresponding inverse occurrences across the annulus.
No matched occurrences use the same underlying edge.
Thus even logarithmic girth, the exact source types, and the original binary cancellation leave room for full erasure if these geometric safeguards are removed.

## A homological rejection test under the source safeguards

Now assume the source cone complex \(X\) is aspherical, as it is for the [tuples certified by Ope26f](../literature/pdf/Ope26f.pdf#page=23).
Let \(R\) be the rose and let \(\widetilde R\) be its full preimage in the universal cover \(\widetilde X\), the Cayley graph for the given generators of \(G\).
For each graph component \(Y\), its entire cone lifts to copies of that cone indexed by \(G\).
In the relative cellular chains of \((\widetilde X,\widetilde R)\) their contributions split as a direct sum.
The degree-two relative homology of a lifted cone is \(H_1(Y;\mathbb F_2)\).
Since \(H_2(\widetilde X;\mathbb F_2)=0\), the connecting map
\[
       \bigoplus_{Y,g\in G}H_1(Y;\mathbb F_2)
                     \longrightarrow H_1(\widetilde R;\mathbb F_2)
\]
is injective.
On each summand it is induced by the group-label map of that copy into the Cayley graph.
In particular the cycle chains of any subgraph of any one side map injectively, since a subgraph includes injectively on first homology and both spaces in that latter comparison are graphs.

Take the subgraph \(Y_3\) on the left vertices of color 3 and the edges of change zero between them.
For a proposed partition of these vertices into equal-label classes, close it under common readable letters within this subgraph.
Fold the resulting parallel copies of each directed label with a common initial class, keeping the reversed copies of each edge consistent, to give a quotient graph \(Z_3\).
If the proposed equalities hold in the original group, the map \(Y_3\to\widetilde R\) factors through \(Z_3\).
Thus \(H_1(Y_3;\mathbb F_2)\to H_1(Z_3;\mathbb F_2)\) must be injective.
Equivalently the ordinary edge boundary must be injective on \(\ker(C_1(Y_3)\to C_1(Z_3))\), since any nonzero cycle in this kernel would map to the zero Cayley edge chain.
The boundary takes this edge kernel into \(\ker(C_0(Y_3)\to C_0(Z_3))\).
If \(E,V\) and \(E',V'\) denote the two respective edge and vertex counts, a necessary condition is
\[
                               E-E'\le V-V'.                             \tag{2}
\]
The full binary boundary test can be stronger than the dimension count.
It can be applied to several colors and both sides at once: take their disjoint subgraphs, fold only proposed group equalities including any comparisons between the two rooted copies, and use the direct-sum injection above.
This is a finite obstruction in addition to the [synchronization and root-separation tests](../claims/Yin_C_A0045_v1.md#synchronous-components-and-protected-vertices).
It tests proposed equalities in the aspherical original cone presentation.

For the four-line assignment, every line has at least 126 inactive ordinary points.
Indeed a selected line meets just three active intersections.
Any other line through two intersections sharing a line index would be that selected line, so it can contain at most two of the six intersections.
Let \(m_C\) be the number of occurrences in a folded vertex class \(C\), and \(m_{C,D}\) the number on ordinary line \(D\) in that class.
Each inactive point of \(D\) gives \(m_{C,D}\) signed stubs of that letter whenever \(m_{C,D}>0\), all collapsing to one at \(C\).
Counting repeats first within each ordinary line only understates the total, since the same point can occur on several lines.
Counting both orientations of collapsed edges gives
\[
       126 \sum_{C,D}(m_{C,D}-1)_+
                \ \le\ 2(E-E')\ \le\ 2\sum_C(m_C-1).                  \tag{3}
\]
The folds of signed stubs count doubled unoriented edge losses even in the presence of loop edges, since the inverse letters are distinct.
In any perfect pairing witnessing erasure of the \(M=n/7-4\) left occurrences in color 3, the number of pairs whose endpoints have the same ordinary line is at most \(\sum_{C,D}(m_{C,D}-1)_+\), taking the actual label classes \(C\).
By (3) it is at most \(M/63\).
In particular a same-type duplication of all the vertices of this color cannot produce the required original-group equalities in an aspherical realization.
The same reasoning applies separately to the two other even forward colors and to the second side.

## How many different copied words are needed?

Suppose a proposed surgery witnesses each paired equality by a based freely reduced null word read along the left graph from one member of the pair to the other.
If all the words used have length at least three, at least 8193 distinct words, counted up to word inversion, are required just for the complete pairing of color 3 in this four-line model.
This applies in particular to words copied from immersed cycles of length at least the girth on the other side.
Different cyclic rotations are counted as different words if they have different based readings.

To see the bound, choose an orientation of one word \(W\) of length at least three and orient each of its assigned pairs to read that word.
Of its first two turns at least one uses an ordinary stub: if one turn has two extra stubs, its outgoing letter is extra, so the incoming stub for the next turn is ordinary.
The two stubs of the chosen turn are distinct by free reduction.
The prefix ending at that turn is a partial injection on vertices and determines its color from the starting color 3.
For two ordinary stubs the allowed line is unique, giving at most \(n/(7v)+6\) possible turn vertices of that color, including the empty-extra adjustment if it is one of the selected lines.
For an ordinary and a specified extra the number is exactly \(np^2/7\).
No vertex with extras was adjusted.
For admissible \(n\ge14v^2\) one has \(np^2/7-n/(7v)=128n/(7v^2)\ge256\).
Thus at most \(np^2/7\) starting vertices in color 3 can read \(W\).
The \(M/2\) disjoint pairs require at least
\[
                       \left\lceil\frac{1-28/n}{2p^2}\right\rceil=8193
\]
words at these \(n\), since \(1/(2p^2)=16513^2/(2\cdot129^2)\) is between \(8192.99\) and \(8193\).
This bound does not address shorter *derived* trivial words in the original group, which need not themselves label graph cycles.
Construction (1) deliberately creates such words and loses the source safeguards.
The three tests do not exhibit an original torsion-free, root-separated matching with complete erasure of color 3.

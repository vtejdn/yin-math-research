---
author: Yin
---

# A linear survivor bound and disjoint short relations in an erased color

## Statement

Take a connected [four-line tuple with the exact coarse type populations](Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings) and its original group \(G\).
Use the forward labels on either side and fix \(c\in\{3,5,6\}\).
Write \(M=n/7-4\) for the number of occurrences in that color, \(f\) for the number of distinct group labels there and \(o\) for the number with odd multiplicity.
Thus \(o\) is the number of labels surviving collection over \(\mathbb F_2\).
Let \(V\) be the vertex set of the [neutral-edge Cayley graph of odd stub counts](Yin_C_A0085_v1.md#statement) and \(v=|V|\).
It uses \(D=8252\) neutral ordinary–ordinary inverse pairs.

1. If the two-graph cone complex is aspherical, then \(v>31M/4125\).
   If in addition **every** 62-pair subalphabet of these neutral pairs freely generates its marked subgroup in \(G\), then
   \[
                      v>\frac{31}{53}M,\qquad
                      o>\frac{8}{23}v>\frac{M}{5}.
   \]
   These are deterministic bounds on an individual tuple satisfying the indicated conditions.
   They hold simultaneously for all six choices of side and forward color on that event in the four-line law and its fixed thirteen-position refinement. [Subalphabet and geometry events](Yin_C_A0088_v1.md#a-finite-length-and-a-positive-fraction-of-alphabets)
2. Suppose instead that the entire color erases in the original group.
   Draw one 62-pair neutral alphabet uniformly without replacement on this **fixed** tuple and put
   \[
                     H=2\left\lceil\frac{\log n}{\log(65/64)}\right\rceil+4 .
   \]
   With probability greater than \(1/4000\), the edges retained by this **same** alphabet contain at least \(\lceil v/(15872 H)\rceil\) pairwise vertex-disjoint simple cycles, each of length at most \(H\).
   They give nonempty cyclically reduced rose words trivial in \(G\), and their particular cycle chains are linearly independent in the first binary homology of the Cayley graph.
   With asphericity their number is \(\Omega(n/\log n)\) and their unique classes in the direct sum of translated graph homologies are linearly independent.
   The argument gives no distinction between their unbased words or between their classes modulo translation.
   Independently of the alphabet draw, full erasure forces at least \(\lceil f/2\rceil\) distinct unoriented Cayley edges to be images of two distinct source edges carrying the same ordinary outgoing stub at that label in the same side graph.
   These folds may use active letters or other letters outside the sampled alphabet.

The second part requires no free-subalphabet assumption, and its bound in terms of \(v\) holds without asphericity.
Both results use the original equality fibers, including labels which disappear from the group-ring support.

## Folding all neutral occurrences before reducing modulo two

Put \(p=129/16513\).
For each true label \(g\) and neutral signed letter \(s\), let \(k_{g,s}\) be the number of vertices in its fiber carrying \(s\).
Its parity indicates the corresponding directed edge in the graph on \(V\).
Set the degree \(d_g\) to zero at any label outside \(V\), so that
\[
                \sum_{g\in V}d_g=\sum_{g,s}(k_{g,s}\bmod2).
\]
The total before parity reduction is
\[
             B=\sum_{g,s} k_{g,s}=16504\,p\,n/7-504 .
\]
Indeed the balanced count per signed stub at one coarse color is \(pn/7\).
Exactly the 504 private points of the four selected lines lose one occurrence apiece in this color, while the other neutral points keep the original count.
The same equality holds after projecting the more finely prescribed states. [Line and stub counts](Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings) · [Summation over finer states](Yin_C_A0065_v1.md#exact-type-counts-and-the-thirteen-coordinate-histograms)

Take the graph \(Y\) with the \(M\) occurrences as vertices and **all** their neutral ordinary–ordinary edges.
It is a subgraph of the chosen side since these stubs preserve the color and their inverses are also neutral.
Map \(Y\) to the labelled Cayley multigraph \(\widetilde R\) by actual root labels, with image \(Y'\).
The image has \(f\) vertices; edges with the same starting label and same signed stub are identified and the covering involution identifies their reverse descriptions.
The fixed-side \(H_1\) injects into \(H_1(\widetilde R;\mathbb F_2)\) under asphericity, by the [relative homology of the lifted graph cones](../ledger/Yin_L_A0052_v1.md#a-homological-rejection-test-under-the-source-safeguards).
Inclusion of a subgraph in a graph is injective on \(H_1\), even if the subgraph has several components.
It follows that \(\partial\) maps the kernel of \(C_1(Y)\to C_1(Y')\) injectively into the kernel of \(C_0(Y)\to C_0(Y')\), with binary cellular chains.
Indeed a cycle in the former kernel would give a cycle of \(Y\) mapping to the zero edge chain in \(\widetilde R\).
All these chain maps onto the image graph are surjective degree by degree.
Hence if \(E,E'\) are the unoriented edge counts, then
\[
            \sum_{g,s}(k_{g,s}-1)_+=2(E-E')\le2(M-f).
\]
This counts two signed ends also when an image edge is a loop, since a rose generator and its formal inverse are different signed letters.
In particular the estimate controls losses before parity reduction, including at labels with every stub count even.

For any integer \(k\ge0\), \(k\bmod2\ge k-2(k-1)_+\).
Consequently
\[
                  \sum_{g\in V}d_g\ \ge\ B-4M+4f\ >\ 124M+4f .        \tag{1}
\]
For the strict inequality use \(n/7=M+4\) and \(16504\cdot129/16513>128\).
The maximum degree is 16504 and \(f\ge v\), so \(16500v>124M\).
This proves the unconditional size conclusion under asphericity.

Under complete erasure every one of the \(f\) labels has two different vertex occurrences.
Their ordinary lines share a point \(s\), so both outgoing \(s\)-stubs at these two vertices project to the same directed Cayley edge.
The source edges are distinct since the two ends of one edge have inverse formal signed labels.
Each unoriented image edge can account for at most its two endpoint labels, proving the separate \(\lceil f/2\rceil\) bound without using asphericity.
It counts folds in the full side map and does not place them along any individual cycle or filling disk.

## Averaging the local degrees when the subalphabets are free

For one uniform sample of \(s=62\) inverse pairs let \(d'_g\) be the retained degree.
Set \(N=D-s+1=8191\) and define the real convex function on \([0,\infty)\)
\[
                  \phi(x)=sx/D-2+2(1-x/N)_+^s .
\]
The expected retained degree is \(s d_g/D\), since each signed end is retained with probability \(s/D\).
At most \(d_g\) distinct inverse pairs meet \(g\).
If \(d_g<N\), the probability that none is drawn is at least \(\prod_{j=0}^{s-1}(1-d_g/(D-j))\ge(1-d_g/N)^s\).
For larger degrees the zero lower bound suffices.
This gives
\[
   \mathbb E\big[d'_g-2\mathbf1_{\{d'_g>0\}}\big]\ \ge\ \phi(d_g).
\]
On a free sampled alphabet the retained Cayley subgraph is a forest, so the sum of the random left-hand integrands is nonpositive. [C88, the nonisolated-vertex count](Yin_C_A0088_v1.md#sampling-inverse-pairs-and-counting-nonisolated-vertices)
Thus \(v^{-1}\sum_{g\in V}\phi(d_g)\le0\) under the stated freeness hypothesis.

The function is increasing for \(x\ge124\).
Indeed \(2D(N-124)^{61}<N^{62}\) gives \(\phi'(124)>0\), and convexity follows from that of the positive-part power.
The following rational comparisons use \(s=62\):
\[
               \phi(124)>-3/10,\qquad
               \phi(249)>4/25,\qquad
               \phi(216)>0.
\]
For exact arithmetic, the sign of \(\phi(x)-a/b\) at each of these integer \(x\)'s is the sign of
\[
          \big(bs x-(2b+a)D\big)N^{62}+2bD(N-x)^{62}
\]
with \((x,a,b)=(124,-3,10),(249,4,25),(216,0,1)\), respectively; all three integers are positive.
Jensen's inequality and \(\phi(216)>0\) imply \(\sum_{g\in V}d_g<216v\).
Combining with (1) and \(f\ge v\) gives \(v>124M/212=31M/53\).
Every odd label is in \(V\), with degree at least 124, and the other vertices of \(V\) have degree at least 249. [Degree bounds from the four ordinary lines](Yin_C_A0085_v1.md#the-neutral-degrees-on-the-four-lines)
It follows that \(0>(4/25)(v-o)-(3/10)o\), giving \(o>8v/23\).
Finally \(248/1219>1/5\), which yields the claimed linear number of survivors.

## Packing cycles with one sampled alphabet

Assume full erasure and use the same 62-pair sampling on the fixed tuple.
By [C88's excess estimate](Yin_C_A0088_v1.md#a-finite-length-and-a-positive-fraction-of-alphabets), with probability greater than \(1/4000\) the sampled subgraph has surplus
\[
           S=2|E_{\rm samp}|-2|\{g:d'_g>0\}|\ \ge\ v/32 .
\]
Work with one alphabet on this event, deleting isolated vertices from the counts.
As long as \(S\ge v/64\), the remaining nonisolated graph has average degree at least \(2+1/64\), since it has at most \(v\) vertices.
It contains a simple cycle of length at most \(H\).
Loops or two different parallel edges give lengths one or two.
In a simple graph one may prune vertices of degree at most one to find a core of at least this average and minimum degree two.
The proof of [C88's short-cycle bound](Yin_C_A0088_v1.md#a-finite-length-and-a-positive-fraction-of-alphabets) then applies with \(65/64\) replacing \(33/32\): the entropy of \(j\) nonbacktracking continuations conditional on a uniform initial directed edge is at least \(j\log(65/64)\).
For \(j=\lceil \log n/\log(65/64)\rceil+1\) this exceeds \(\log n\), so two continuations must collide if there has been no earlier cycle, giving length at most \(2j+2=H\).
Only the resulting cycle need be removed from the original remaining graph.

Delete its vertices and incident edges, and drop any new isolated vertices.
The sampled maximum degree is at most \(124\), so there are at most \(124H\) lost edges and the surplus falls by at most \(248H\) in this step.
The initial surplus was at least \(v/32\).
Thus more than \(v/(64\cdot248H)\) steps are needed to fall strictly below \(v/64\), and the process terminates since it deletes at least one vertex at each step.
The recorded cycles are pairwise vertex-disjoint and all use the originally selected alphabet.
Each is a nonzero finite binary cycle chain in \(\widetilde R\), and graph cycles have no two-boundaries there.
Their disjoint edge supports prove linear independence, including cycles of length one or two.
The signed reading around each cycle is cyclically reduced by local injectivity of the signed Cayley steps, and it is trivial in \(G\) by closure.

With asphericity, the lifted two-complex \(\widetilde X\) is contractible, so its relative sequence with \(\widetilde R\) actually gives an isomorphism
\[
 \bigoplus_{h\in G}\big(H_1(A;\mathbb F_2)_h\oplus H_1(B;\mathbb F_2)_h\big)
                      \ \xrightarrow{\ \partial\ }\ H_1(\widetilde R;\mathbb F_2).
\]
Here \(A,B\) denote the two original connected side graphs. [Deck-indexed cone calculation](Yin_C_A0066_v1.md#the-finite-tensor-calculation)
The inverse images of the packed cycles are therefore independent in this full direct sum; they may involve overlapping translated summands.
The deterministic lower bound \(v>31M/4125\) makes the packing of order at least \(n/\log n\).
The probability in the packing statement is over alphabets on a given erased tuple and gives no probability that such a tuple occurs in the source matching law.

## Assessment history

### Decision linear-survival-and-cycle-packing

| Field | Value |
| --- | --- |
| date | 2026-11-17T14:37 |
| status | proved |
| reason | Independent review verifies the folding inequality, survivor constants, and the exact independence of the packed cycles. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Linear lower bound on surviving true labels under sparse freeness and disjoint short cycles on one alphabet under erasure. |
| argument | [Proof](#folding-all-neutral-occurrences-before-reducing-modulo-two) | Folded chain counts, sampling of neutral stubs, convex degree estimates and packing under the marked cone relations. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0126_v1.md#whole-argument-finding) | Independent review of the argument and its stated scope. |

## Current assessment

[Selected decision](#decision-linear-survival-and-cycle-packing)

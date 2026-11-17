---
author: Yin
---

# A sparse-alphabet forest test excludes complete color erasure

## Statement

Fix a connected four-line tuple with the [specified original vertex types, inverse pairs and coarse counts](Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings), and work in its actual cone group.
Take either side, in forward coordinates, and any \(c\in\{3,5,6\}\).
There are \(D=(16513-6-3)/2=8252\) neutral ordinary–ordinary inverse pairs after removing the six signed active points and the three ordinary partners of extra letters.
No restriction on the side, translation index, number of relators or matching witnesses is imposed.

1. If every subalphabet formed by 62 of these inverse pairs freely generates its marked free subgroup, the color cannot erase.
   More quantitatively, at least \(1/17\) of the actual labels with nonempty odd ordinary-stub set have odd vertex multiplicity in the color.
   If every nonempty cyclically reduced trivial word has length at least \(l\ge3\), the number of distinct odd labels is at least \(119^{\lfloor(l-1)/2\rfloor}/17\).
2. On **any** fully erased tuple, a uniformly chosen 62-pair neutral subalphabet has probability greater than \(1/4000\) of admitting a nonempty cyclically reduced trivial word of length at most
   \[
                2\left\lceil \log n/\log(33/32)\right\rceil+4.          \tag{1}
   \]
   The probability concerns only the alphabet draw on the given tuple.
   Thus an upper bound \(1/4000\) on the proportion of alphabets with such a short relation suffices to exclude full erasure, even if some small subalphabets are not free.

These conclusions hold simultaneously for the six indicated colors under their stated alphabet hypothesis.
The needed freeness and marked systole hold with probability tending to one under the strengthened bounded-pattern estimates for the four-line and fixed thirteen-position laws, as described below.
This supplies a deterministic way to certify an individual tuple and a necessary collection of short relations in any remaining exception.
It does not assert that every tuple satisfying only torsion-freeness, root separation and the exact types passes the finite short-relation test.

## The graph of odd stub counts

For each true label \(g\) of the selected color let \(O_g\) be the set of ordinary signed stubs occurring an odd number of times at vertices with that label.
Let \(V\) be the finite set of \(g\)'s with \(O_g\ne\varnothing\).
An odd number of projective lines has odd incidence on every test line, so at odd vertex multiplicity \(|O_g|\ge129\) by point–line counting, and every odd label lies in \(V\).
At even vertex multiplicity, \(O_g\) is an even sum of lines.
A nonzero such sum has at least \(2\cdot128=256\) points.
To recall the argument, it meets every line evenly.
If its weight is less than 256 some line is empty by counting all incidences.
Choose that line as infinity.
The homogeneous degree-127 sum of the corresponding 127th powers of linear forms over \(\mathbb F_{128}\) gives the evaluation of the even line sum, because the constant terms of the line indicators cancel.
It vanishes identically on the empty line as a polynomial there, since its restriction has degree less than 128.
Dividing by the coordinate of that line shows that its affine evaluation is represented in degree at most 126.
A nonzero polynomial of total degree at most 126 on \(\mathbb F_{128}^2\) has at most \(126\cdot128\) zeros, a contradiction.
This is the even line-code estimate in [the ordinary-stub calculation](Yin_C_A0085_v1.md#statement).
The conclusion uses membership in the span of projective lines and would not follow from even intersections alone.

For a neutral ordinary \(s\), the true multiplicities of its outgoing stub at \(g\) and of the reverse stub at \(gs\) agree by the inverse matching.
Retain this unoriented Cayley edge precisely when these multiplicities are odd.
The resulting finite labeled multigraph has all its endpoints in \(V\); its degree \(d_g\) at \(g\) equals the number of its neutral signed stubs in \(O_g\), counting both ends of a loop.
Hence \(d_g\ge247\) at an even vertex count and \(d_g\ge120\) at an odd count after discarding at most nine ordinary stubs.
The graph is nonempty because the total number of occurrences of each private ordinary stub in the color is odd by the exact type adjustment. [Private edge counts](Yin_C_A0078_v1.md#a-finite-cycle-from-the-four-private-lines)

## Sampling inverse pairs and counting nonisolated vertices

Select \(s=62\) distinct inverse pairs uniformly without replacement from the \(D\) possibilities and keep just their edges.
Write \(d'_g\) for the new degree.
Then \(\mathbb E d'_g=sd_g/D\).
At most \(d_g\) different pairs meet \(g\), so for \(d_g\le280\) the probability that \(g\) becomes isolated is at least
\[
          \prod_{j=0}^{s-1}\left(1-\frac{280}{D-j}\right)
               \ \ge\ (1-280/8191)^{62}>7/64 .
\]
The strict inequality can be checked by \(64\cdot7911^{62}>7\cdot8191^{62}\).
For \(247\le d_g\le280\) it follows that
\[
 \mathbb E\big[d'_g-2\,\mathbf1_{\{d'_g>0\}}\big]
       \ge 62\cdot247/8252-2+14/64 > 1/16 .
\]
For \(d_g\ge281\), \(62\cdot281/8252-2>1/16\) already.
At every other vertex the integrand is at least \(-1\).

Let \(y\) be the fraction of odd labels among \(V\), and let \(X\) be the sum of the integrands divided by \(|V|\).
Then \(\mathbb E X\ge(1-y)/16-y\), strictly if \(y<1\).
On a freely generating alphabet the retained graph is a forest: a cycle would give a nonempty cyclically reduced null word, since inverse readings in a Cayley graph uniquely reverse the same edge.
In a forest the number of edges is at most the number of **nonisolated** vertices.
Thus if all sampled alphabets are free, \(X\le0\) for every draw, and \(y\ge1/17\).
Keeping the isolated-vertex probability in this argument is what allows a 62-pair alphabet to suffice.
Under the systole assumption an ordinary breadth-first exploration from any vertex of the full odd-stub graph branches without identifications through radius \(\lfloor(l-1)/2\rfloor\), in the sense that all nonbacktracking paths up to this radius with one initial point have distinct endpoints.
The minimum degree 120 then gives the asserted lower bound on \(|V|\) and on the number of survivors.

## A finite length and a positive fraction of alphabets

If the entire color erases, \(y=0\) and \(\mathbb E X>1/16\).
Always \(X\le124\), so \(\Pr(X\ge1/32)>1/4000\), since \(1/32+124/4000<1/16\).
On this event the nonisolated subgraph has average degree at least \(2+1/32\).
Deleting isolated or degree-one vertices preserves a nonempty core of at least that average degree and minimum degree at least two; the positive surplus \(2|E|-2|V|\) cannot decrease during the deletions.
Loops or parallel edges give a length-one or length-two cycle at once.

For a simple core of average degree \(\bar d\) and minimum degree two, start with a uniform directed edge and at each vertex choose uniformly among nonbacktracking continuations.
The directed-edge distribution stays uniform, and the conditional entropy per continuation is \(\sum_x d_x\log(d_x-1)/\sum_x d_x\ge\log(\bar d-1)\) by convexity of \(d\log(d-1)\) on \(d\ge2\).
The entropy of \(j\) successive choices given the initial edge is therefore at least \(j\log(\bar d-1)\).
If there is no cycle of length at most \(2j+2\), distinct such paths from a fixed initial edge have distinct endpoints.
Their conditional entropy is then at most \(\log |V|\le\log n\).
Taking \(j=\lceil\log n/\log(33/32)\rceil+1\) gives a contradiction and proves (1).
All cyclic reductions and lengths here use the selected original rose generators.

For instance the test still excludes erasure if every short relation seen by these alphabets must use both members of one of at most four specified pairs of *different inverse pairs*.
For each prescribed two-element set the chance of inclusion is \(62\cdot61/(8252\cdot8251)\).
Four times this probability is below \(1/4000\).
The statement assumes the claimed coverage of all short relations on the particular tuple.

Finally, the original four-line law has simultaneous freeness for every 62-pair subalphabet by [C59](Yin_C_A0059_v1.md#statement).
For the law with fixed nonregular lamp states, each neutral letter stays in one fine state, every allowed turn on the selected signed ordinary points has the same limiting weight \(1/129\), and all affected type counts differ by bounded constants.
On a fixed 62-pair alphabet the sum of turn weights of reduced words of length \(h\) is at most \(124(123/129)^{h-1}\).
This gives the strict word-bin saving in the [restricted stage and capped-picture argument](Yin_C_A0059_v1.md#bounded-path-systems-with-some-comparisons-replaced-by-an-alphabet-restriction).
The side-specific fixed-state factors in this very law are bounded as in [C78](Yin_C_A0078_v1.md#excluding-private-relations-with-few-changes-of-line), so the same proof excludes null words on that alphabet with conditional probability tending to one.
There are a fixed finite number of alphabet choices, independent of \(n\).
Intersecting these events and the [marked systole event](Yin_C_A0071_v1.md#short-words-separating-original-labels) gives the polynomial survivor bound on those realizations.
This argument does not condition the law on the exceptional event of a complete erasure.

## Assessment history

### Decision neutral-alphabet-surplus

| Field | Value |
| --- | --- |
| date | 2026-11-17T14:37 |
| status | proved |
| reason | Independent review verifies the individual-tuple test, its constants and the stated matching-law applications. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Sparse free alphabets exclude erasure and short relations must occur in a positive proportion of alphabets under full erasure. |
| argument | [Proof](#the-graph-of-odd-stub-counts) | Local degree and isolation estimates, forest counts, finite short-cycle bound and transfer to the two matching laws. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0124_v1.md#whole-argument-finding) | Independent review of the argument and its stated scope. |

## Current assessment

[Selected decision](#decision-neutral-alphabet-surplus)

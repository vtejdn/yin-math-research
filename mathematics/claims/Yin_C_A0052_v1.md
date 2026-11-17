---
author: Yin
---

# Deciding the six color erasures in the original group of a supplied pattern-free matching

## Statement

Fix the parameters of the [four-line matching model](Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings) and the pattern-free criterion of [Mghirbi and Douglas, Definition 3.3 and Proposition 4.4](https://arxiv.org/html/2611.04599v1#S4.SS3).
Suppose the two explicit connected matching graphs on \(n\) vertices per side meet this criterion at scale \(L=\lfloor c_0\log n\rfloor\), have diameter at most \(dL\), and have their designated roots in color zero.
Take fixed constants, or certified rational upper bounds for \(d,c_0,16/(13\varepsilon)\), throughout the complexity assertion.
There is a deterministic algorithm polynomial in \(n\) that performs the following operations in the *original cone group* \(G\).

1. For all vertices in color \(3\) on the first side, determine their actual group-label multiplicities. If they are all even, output a perfect pairing together with finite proofs from the original loop relations for every pair. Otherwise output an odd equality class and the exhaustive test separating it from the other classes.
2. Decide joint extension to all the other even colors \(\{5,6\}\) on the first side and \(\{1,2,4\}\) on the second side, where the second side uses inverse labels. Every correct pairing in the first color extends if each of the other five lists is entirely even after collection. No new relations are imposed when extending.
3. The same algorithm can compute all actual product fibers and both collected supports on that tuple. The complete input includes the labelled bijections, not only the seven occurrence counts. With fixed rational comparison data the pattern-free conditions themselves can be checked in polynomial time at these logarithmic scales.

Here the polynomial degree depends on the fixed geometric constants and alphabet, with no claim of practical efficiency for the source sizes.
The applicable pattern-free event has probability tending to one after girth conditioning in the four-line law by its diameter and bounded-pattern estimates at the fixed tuple of bounds in the criterion. [Four-line geometry](Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts) · [Choice of bounds](https://arxiv.org/html/2611.04599v1#S3.SS2)
The conclusions hold deterministically on that event even if a supplied tuple was chosen for exceptional collisions.

## Bounded certificates in the cone presentation

Use the rose's free generating letters.
For vertices \(x,x'\) on the same side, the word of any graph path \(x\to x'\) represents \(g_x^{-1}g_{x'}\) with forward path labels.
Choose a shortest path of length at most \(dL\) and freely and cyclically reduce its label to \(w\).
Triviality is unchanged by cyclic reduction since it changes the represented element by conjugation.
The empty result answers yes immediately.
Otherwise, if \(w=1\) in \(G\), the free outer disk case of [Mghirbi and Douglas, Lemmas 4.2–4.3 and Proposition 4.4](https://arxiv.org/html/2611.04599v1#S4.SS1) gives a capped picture for \(w\) with total inner boundary length
\[
                      H\le K|w|,\qquad K=16/(13\varepsilon).
\]
Every inner disk reads a nonempty cyclically immersed closed walk in one of the two input graphs.
Girth bounds its length below by \(L\).
Thus \(H\le KdL\) and the number of inner disks is at most \(Kd\), independent of \(n\).
A spherical picture of inverse-letter arcs between those disks and an exterior disk reading \(w^{-1}\) proves the converse directly in the presentation, since \(w\) then belongs to the original normal closure.
Each of its inner walks can also be written using the fundamental walks of a spanning tree.
This certificate bound uses the free outer disk of a cyclically reduced *word*.
The separation assertion for two specified graph roots alone gives no such decision test.

## Enumerating the witnesses

Enumerate up to \(\lfloor Kd\rfloor\) closed walks subject to the total length bound, allowing all starting vertices, orientations and starting positions.
An upper bound on the number of ordered choices is a fixed power of \(2n\), times \(132^{\lceil KdL\rceil}\) and a fixed power of \(1+L\), since outgoing degree is at most \(132\).
This is polynomial in \(n\).
Append the outer boundary word to each candidate.
To obtain a connected picture, discard any component of the disk-and-arc incidence graph disjoint from the outer disk, removing its disks and arcs from the sphere.
The remaining picture has the same outer word.

For \(k\) inner disks, choose \(k\) inverse-letter matches forming a tree on the \(k+1\) named disks.
There are at most a fixed power of the total number \(M\) of boundary occurrences for these choices and their order, since \(k\le Kd\).
Contract the tree edges successively by thickening one connecting arc and combining the two disks into one disk.
In cyclic word notation the two matched letters are deleted and the two complementary words joined in their respective cyclic orders.
For an existing picture the result is a single disk with the unused occurrences paired by noncrossing arcs in its complementary disk, so its cyclic word freely reduces to the empty word.
Conversely make a disk with exactly this spliced boundary by joining the named disks by the chosen tree of bands.
A regular neighborhood of that tree of disks and bands is a disk, with precisely the spliced cyclic order, because every band joins distinct current components.
If the spliced word freely reduces to the empty word, draw the inverse-letter pairs from the reduction in the complementary disk, then restore the tree arcs.
This supplies an actual spherical picture.
Free reduction takes linear time in \(M\).
There is no need to enumerate arbitrary permutations of \(M\) occurrences.
Recording the walks, tree matches and the final free reduction gives a checkable positive answer.
Exhausting these finitely bounded choices gives a correct negative answer under the geometric hypothesis.

## From one even color to both factors

Partition the first list in color \(3\) by the preceding equality test.
Pair arbitrarily within each even equality class and retain the associated word certificates.
An odd equality class leaves one copy of that group element in the binary support, so erasure of that color is then impossible.
On each side distinct colors cannot represent the same group element, since the given character maps their labels to different elements of \(C_7\).
The two factors collect their multiplicities separately.
Consequently the five remaining lists can be tested independently once equality is taken in the same original presentation.
Adding pair relations would change the group in which the remaining equalities are tested.
This supplies the missing negative decision in the earlier [normal-closure enumeration](Yin_C_A0045_v1.md#synchronous-components-and-protected-vertices) for these pattern-free inputs.

For all product fibers, take shortest root paths of length at most \(dL\).
Equality between two products \(g_xh_y^{-1},g_{x'}h_{y'}^{-1}\) tests a word of length at most \(4dL\).
Use the same enumeration with \(4d\) in the bound.
Even comparing every pair of the \(n^2\) occurrences keeps the total polynomial.
For checking the input hypotheses, inspect adjacency, girth, diameters, roots and types directly.
In the bounded-pattern condition of Definition 3.3 the number of paths and number of interval pairs are fixed constants and the total length is \(O(L)\).
Enumerate the paths from their possible starts, choose interval endpoints among \(O(L)\) positions, and test their orientation, pairing, distinct-edge and coverage conditions.
As above, the bounded path count, bounded degree and \(L=O(\log n)\) give a polynomial bound.
Parameters for this check can be supplied as integer cutoffs and exact rational thresholds at the chosen scale.
The test accepts the exclusion of forbidden patterns only after exhausting those choices.
It is an algorithm for a specified finite tuple.
Deciding whether some size admits the requested six erasures would require additional information across tuples and sizes.

## Assessment history

### Decision supplied-matching

| Field | Value |
| --- | --- |
| date | 2026-11-17T09:38 |
| status | proved |
| reason | Independent review checks completeness of the tree and disk certificates, polynomial bounds with fixed parameters, and the applicability of the geometric promise. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact erasure decisions, extensions, and product fibers on a supplied pattern-free tuple. |
| argument | [Proof](#bounded-certificates-in-the-cone-presentation) | Bounded certificates, enumeration and the simultaneous decision. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0083_v1.md#whole-argument-finding) | Independent review of the entire decision procedure and its hypotheses. |

## Current assessment

[Selected decision](#decision-supplied-matching)

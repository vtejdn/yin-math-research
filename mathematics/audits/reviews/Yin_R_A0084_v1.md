---
author: Yin
---

# Forced equalities, homology of folds, and the cost of copied null words

A separate reviewing agent inspected fixed L_A0052_v1 for Yin on 2026-11-17T01:32 UTC.
The reviewer did not develop its reserved-cycle construction, relative chain obstruction or copied-word count, and received or consulted no L_A0052 development discussion, author explanation or prior verdict.
Earlier contributions by this reviewer to the distinct synchronization tests and planted matching estimates are inputs at their established scopes.
This review checks the new arguments and their use of those inputs.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Reserved matching prescription](../../ledger/Yin_L_A0052_v1.md#a-matching-prescription-that-forces-the-equalities-in-its-own-group) | Realizing all cyclic words in the given types, identifying the actual cone group, connected high-girth completions, the two collected factors and the specific failed safeguards. |
| [Whole-argument finding](#whole-argument-finding) | [Aspherical folding test](../../ledger/Yin_L_A0052_v1.md#a-homological-rejection-test-under-the-source-safeguards) | Relative homology injection, finite graph chain test, joint applications and line-type bound for a perfect pairing. |
| [Whole-argument finding](#whole-argument-finding) | [Copied-word count](../../ledger/Yin_L_A0052_v1.md#how-many-different-copied-words-are-needed) | Turn bound, partial injectivity, numerical ceiling and the restriction to based words of length at least three. |
| [Whole-argument finding](#whole-argument-finding) | [Four-line count data](../../claims/Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings) | Three active inverse pairs, exact color totals, bounded empty-extra corrections and six active intersection points. |
| [Whole-argument finding](#whole-argument-finding) | [Unreserved switch estimates](../../claims/Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts) | Block-size and distance bounds and their use after reserving only \(O(L)\) pairs. |
| [Whole-argument finding](#whole-argument-finding) | [Four-line cut estimate](../../claims/Yin_C_A0051_v1.md#connectedness-collection-and-the-erasure-threshold) | Exponential unconditioned cost of a macroscopic disconnected cut. |

## Whole-argument finding

The review checks the ordinary two-disk arrangement and its distinct-underlying-edge condition against [Ope26f, pp. 14–15](../../literature/pdf/Ope26f.pdf#page=14).
The cone construction, contractible universal cover and root protection used for safeguarded tuples are those of [Ope26f, §§5–6](../../literature/pdf/Ope26f.pdf#page=20).

Each reserved word is cyclically reduced, closes in color and has at least \(L\) letters.
The turn pools on the second side are positive for every required pair, including an extra and its ordinary inverse, and remain linear in each color under the bounded four-line adjustments.
All cyclic vertices can therefore be chosen distinct, both within and across words.
The chosen alphabet is fixed independently of \(n\), giving \(O(L)\) prescribed matching pairs in total.
A power \(t^L\) in a simple cycle uses the incoming and outgoing signed stubs \( \bar t,t\) at its vertices, which are distinct.
The two consecutive powers kill every inactive generator in the original presentation.
The remaining relations give \(x^7=1,\ y=x^2,\ z=x^4\).
Since the actual word increments define a surjection to \(C_7\), additional relations from completing the matchings cannot make the cone group smaller than \(C_7\).

For cycles avoiding prescribed vertices the number of available stubs in each block differs from the original by \(O(L)\).
All short cycles touching those vertices have edges in the union of \(O(L)\) radius-\(L\) neighborhoods, of size \(n^{c\log132+o(1)}=o(n)\).
Because the prescribed subgraph is a disjoint union of long simple cycles, at least one edge of every bad cycle is unreserved.
A distant nonbad unreserved switch in the same block therefore preserves the prescriptions and reduces the total number of bad edges.
The sublinear number of necessary switches with a polynomial number of choices per switch costs \(\exp(o(n))\) in counting reverse neighborhoods.
Under the resulting girth condition, the one-pair upper bound still holds after subtracting the reserved budget from each block size.
The reserve subgraph has maximum degree two, so a set of \(2j\) vertices contains at most \(2j\) reserved edges.
The small-set expansion estimate can use the remaining \(\lceil129j/2\rceil-2j\) prescribed edges, giving exponent at least \(60.5j\) in \(j/n\).
For a macroscopic cut, prescribing the \(O(L)\) pairs first has probability at least \(n^{-O(L)}\) in the original four-line law, and logarithmic girth adds only a subexponential conditioning cost in that reserved law.
The strict exponential cut bound thus survives, giving connected completions on both sides.

With roots at zero, equality of the group itself with \(C_7\) makes each forward color a single group label.
The two factors are nonzero, and their coefficient counts at level seven are \(4,2,2,2,2,2,2\) in their product, all zero modulo two.
This achieves exactly the indicated erasures on both sides.
The repeated root label contradicts root separation, the group has torsion, and the two disjoint \(t\)-cycles yield an ordinary reduced annular pairing after their indicated repetitions.
The construction therefore supplies no torsion-free counterexample.

For an aspherical cone complex, the relative cells over the preimage of the rose split into copies of the relative cone cells, one copy for each component and deck translate.
Different bases can meet in the lifted rose without changing this relative direct sum.
The degree-two relative homology of each cone copy is \(H_1(Y;\mathbb F_2)\).
Contractibility gives \(H_2(\widetilde X;\mathbb F_2)=0\), hence injectivity of the connecting map to the homology of the lifted rose.
Since a graph has no boundaries in degree one, a nonzero cycle chain in a subgraph cannot map to a zero Cayley edge chain.
If proposed equalities hold, equal initial group labels and common edge labels force the folded identifications, so the Cayley chain map does factor through the specified fold.
The edge- and vertex-chain maps onto the folded graph are surjective, with respective kernel dimensions \(E-E'\) and \(V-V'\).
Restriction of the boundary to the edge kernel must inject into the vertex kernel, proving the inequality.
Disjoint subgraphs in one copy inject together, and separate copies have the direct-sum injection already established.

Each of the four selected lines misses all but its three active intersection points.
An unselected line contains at most two active intersections because their line-index pairs would otherwise include two with a common index and determine that selected line.
At any folded class, repeats within each ordinary line contribute at least \(126(m_{C,D}-1)_+\) lost signed stubs.
Summing the within-line repeats does not overcount the total loss for a fixed signed letter, even if several lines at the same vertex class carry it.
Every quotient edge accounts for both signed orientations, also for a loop, so the total loss is \(2(E-E')\).
This gives the printed bound, and the number of matched same-line pairs is bounded by \(\sum_{C,D}(m_{C,D}-1)_+\), hence by \(M/63\).
The necessary fold criteria do not assert realizability of a pairing passing them.

For a based freely reduced word of length at least three, the two stubs in each of its first two turns are distinct.
If the first turn is extra–extra, the inverse of its outgoing letter is ordinary in the following turn.
That ordinary-containing turn has a prescribed color, and the prefix map from starting vertices is injective on its domain by the inverse matching.
An ordinary–ordinary turn fixes its line, allowing at most \(n/(7v)+6\) vertices after the empty-extra correction.
An ordinary–extra turn has exactly \(np^2/7\) possible vertices.
The changes of empty-extra types do not affect it.
Since the difference \(np^2/7-n/(7v)=128n/(7v^2)\) is at least \(256\), the latter count bounds both cases.
Taking one orientation of each word up to inversion still gives one distinct possible start for each assigned pair.
The lower bound on the number of word classes before taking the ceiling is \(8192.992218\ldots\) at \(n=14v^2\) and increases to \(8192.992278\ldots\).
Thus \(8193\) is the asserted lower bound at every admissible size in scope.
It leaves possible certificates by shorter freely reduced null words and supplies no actual erasure for a safeguarded torsion-free matching.
The review supports the complete fixed ledger at these stated scopes.

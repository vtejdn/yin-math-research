---
author: Yin
---

# Private-line boundaries and words with few changes of line

At 2026-11-17T04:29 UTC a separate agent reviewed the fixed [C78](../../claims/Yin_C_A0078_v1.md) for Sheng Yin.
The reviewer developed the earlier C51 coarse construction, previously reviewed the C65 state law, and worked on separate central tests for exchanges of blocks.
The reviewer did not develop C78 and received no proof-development dialogue, author explanations or prior verdict for its argument.
The review used the stated fixed bounded-pattern and capped-picture inputs and inspected the affected grid and stage steps in the original source.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0078_v1.md#statement) | All partial true pairings in three colors on either side, deterministic private-word alternative, probabilistic size and conditional entropy improvement, and single-label comparison. |
| [Whole-argument finding](#whole-argument-finding) | [Private-line cycle](../../claims/Yin_C_A0078_v1.md#a-finite-cycle-from-the-four-private-lines) | Exact odd counts, labelled edge conventions, four boundary identities, pairing of private trails and a reduced circular witness. |
| [Whole-argument finding](#whole-argument-finding) | [Few changes of line](../../claims/Yin_C_A0078_v1.md#excluding-private-relations-with-few-changes-of-line) | Variable grid, sparse switch enumeration, exponential bin saving, pattern and capped-picture transfer, and extraction of a fixed linear cutoff. |
| [Whole-argument finding](#whole-argument-finding) | [Entropy of branching](../../claims/Yin_C_A0078_v1.md#branching-at-labels-in-all-four-private-boundaries) | Endpoint graph, directed-edge stationarity, size-biased branching entropy, girth and exponent in the stated bound. |
| [Whole-argument finding](#whole-argument-finding) | [Exact masks](../../claims/Yin_C_A0078_v1.md#what-the-exact-vertex-populations-permit) | Four and only four odd masks, optimal two differing pairs in the torsion comparison, and scope for the actual four-line groups. |
| [Whole-argument finding](#whole-argument-finding) | [C51 line and color allocation](../../claims/Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings) | Line incidence, inverse pairing and the coarse population change. |
| [Whole-argument finding](#whole-argument-finding) | [C65 fine populations](../../claims/Yin_C_A0065_v1.md#exact-type-counts-and-the-thirteen-coordinate-histograms) | Parity and the lifted population change. |
| [Whole-argument finding](#whole-argument-finding) | [C59 restricted stages](../../claims/Yin_C_A0059_v1.md#bounded-path-systems-with-some-comparisons-replaced-by-an-alphabet-restriction) | Negative rate from the multiplicity stages and the unrestricted budget. |
| [Whole-argument finding](#whole-argument-finding) | [outer segment](../../claims/Yin_C_A0059_v1.md#capped-pictures-with-an-outer-segment-in-the-chosen-letters) | Bounded interval cuts and the single outer-language segment. |
| [Whole-argument finding](#whole-argument-finding) | [side-dependent stage factors](../../claims/Yin_C_A0065_v1.md#safeguarded-realizations) | Fixed-state embedding factors. |
| [Whole-argument finding](#whole-argument-finding) | [L52 torsion realization](../../ledger/Yin_L_A0052_v1.md#a-matching-prescription-that-forces-the-equalities-in-its-own-group) | All occurrences at a fixed forward color have the same original label, with the specified losses of safeguards. |

## Whole-argument finding

The source comparison covers alignment, word propagation and bin multiplicity bounds at the changed scale. [Ope26f, (3.5)–(3.12)](../../literature/pdf/Ope26f.pdf#page=10)

At the stated admissible sizes \(np/7\) and every unmodified coarse line population \(n/(7v)\) are even.
Each private signed point belongs to exactly one of the changed lines and loses one vertex in each outside color under consideration.
Its inverse lies on that same line, so a chosen orientation counts once each of an odd number of edges in the color.
Keeping the rose labels on the Cayley edges makes the projected binary chain nonempty even if distinct generators have the same group value.
At one occurrence, the whole selected line contributes an odd number of outgoing stubs, namely one or 129.
Removing the three intersections with the other selected lines gives the stated boundary formula at every group element after summation.
Every intersection occurs twice across the four equations.
Any label perfectly paired with equal active masks has both even total multiplicity and even count of each individual active letter, hence none of the four boundaries there is odd.

A simple cycle in one private chain support is already a null reading with one circular run, including a loop or parallel edges in the labelled graph.
Otherwise pairing edge ends in each finite forest leaves one unmatched end at each odd-degree vertex in that forest.
The resulting trails are nonempty simple paths since they do not repeat edges and a forest has no nonempty closed trail.
Thus the compressed multigraph has one incident end of a given color at each of its corresponding boundary vertices, never two.
It is nonempty and its degrees are two or four by the boundary identity.
A simple cycle uses at most \(|Z|\) edges and consecutive edges have different colors.
Each path word is reduced, and different private alphabets are disjoint even after inversion, so their cyclic concatenation is reduced and nonempty.
This proves the deterministic alternative also if some projected generator is trivial.

For any prescribed \(1\le k_L=o(L)\), the chosen \(N,R\) tend to infinity.
The integer-offset pigeonhole bound in Ope26f holds for this \(N\) without change, with grid size \(L/(uR)\) and distance to integer shifts bounded by \(R/N\).
Since \(N^{d+1}\le\sqrt{L/(k_L+1)}\), one has \(s\ge\sqrt{L(k_L+1)}\).
Also \(s/L\le1/R\to0\) and \(k_L/s\to0\).
Consequently the covered substring losses are \(o(s)\) and the total chain-end, rounding, propagation and bin costs are \(o(L)\), including when \(k_L/L\) tends to zero very slowly.
In particular the total block-bin cost is \(O((L/s)\log(s+1))\).

A cut of a circular word has at most one extra linear run.
Within a full block, the first letter has at most 504 possibilities, a continuation without changing line at most 125, and a switch at most 378.
At most \(k_L\) positions of the latter kind contribute only \(\exp(o(h))\) to the factor beyond \(125^h\) because \(k_L/h\to0\).
The reduced-turn weight is \(1/129\) throughout, including at switches, since all letters and inverses are ordinary and the required stubs are distinct.
This leaves a fixed exponential saving from \(125/129<1\).
Dividing that first-moment bound by the minimum positive word weight in a specified bin gives the asserted restricted bin count, with the harmless additive one in the exponent.
There is no need to cut the source comparison at each switch.
Restricting a full word on a distinguished outer-contact interval restricts its subwords as required, including in reverse orientation.

In the C59 stage proof the restricted bin count is used only where a dominant block has a restricted unmatched occurrence.
The other blocks use the original squared-weight or self-link estimates.
The negative exponent per unit length stays strictly below zero before the bounded pattern parameters and their offset count are fixed.
The larger alignment scale above still gives all their errors \(o(L)\).
The product of the stage bounds then has a negative linear exponent for \(b\le\varepsilon H\), so one of the boundedly many stages has exponentially small expected count, even after the \(\exp(o(L))\) union over patterns.
Under fixed side-dependent states only the bounded whole-chain powers and \(\exp(o(L))\) corrections enter.
On the diameter event the capped-picture argument charges the entire outer reading as one restricted segment.
Its extracted clusters have a bounded number of inherited intervals, independent of the number of switches within them.
This yields an \(\exp(-\Omega(L))\) bound on the *intersection with the diameter event* for each prescribed sublinear cutoff.
The diagonal argument to a fixed positive fraction is valid: sizes at which \(\lfloor L/j\rfloor\) fails the \(\exp(-\sqrt L)\) bound can be chosen with distinct increasing \(L\ge j^2\), making those cutoffs and the value one elsewhere a single deterministic \(o(L)\) sequence.
Its exponential estimate contradicts infinitely many such failures.
The probability of the diameter complement need only vanish, and no exponential bound for that complement is used.

On the resulting event every monochromatic support is acyclic and every cycle of the endpoint multigraph has more than \(\lfloor\gamma L\rfloor\) edges.
This gives \(|Z|>\lfloor\gamma L\rfloor\) simultaneously for all pertinent pairings, since the group event depends on none of their choices.
In a complete pairing each label in this set admits at least one differing active letter, giving the claimed pigeonhole count for a single letter.
In the directed nonbacktracking walk, each edge has \(\deg(v)-1\) allowed predecessors at its tail with equal transition weights \(1/(\deg(v)-1)\), so the uniform directed-edge law is stationary even without connectedness.
The head has degree four with probability \(4z_4/(2z+2z_4)\), hence each step has this probability times \(\log 3\) as its mean conditional entropy.
Given the initial edge, two different continuations of length \(q=\lfloor\lfloor\gamma L\rfloor/2\rfloor\) cannot reach the same endpoint since a repeat or divergence followed by a meeting gives a cycle of length at most \(2q\).
Therefore conditional entropy for the \(q\)-step path is at most \(\log z\).
The chain rule gives exactly the exponent \(q\,2\rho/(1+\rho)\), including the degree-two case \(\rho=0\).

Finally any three distinct active intersection points include a pair incident to the same selected line in the \(K_4\) indexing, since a matching on four indices has at most two edges.
Any other projective line carrying that pair would have to be this selected line.
Thus the four distinct triple masks at the selected lines are the only odd masks, since every unmodified line has even population.
Each differing pair can repair at most two odd masks, while within-mask matching followed by two cross-mask pairs attains the lower bound if the group labels coincide.
L52 supplies exactly this coincidence in its high-girth \(C_7\) realization and also states its failed root/asphericity safeguards.
The complete C78 argument is supported at these scopes.
It imposes failures of common readability on a proposed erasing pairing and does not demonstrate such an erasure on a safeguarded source tuple.

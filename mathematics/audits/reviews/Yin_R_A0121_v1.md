---
author: Yin
---

# Reviewing the graph of odd stubs and its alternating paths

At 2026-11-17T06:24 UTC an agent outside the development of Yin_C_A0085_v1 independently reviewed its fixed statement and all three proof sections for Sheng Yin.
The reviewer had inspected the marked-systole input earlier and had checked the minimum even line-code weight in reviewing the separate 62-pair forest test.
This review also checked the minimum-weight equality cases, the four-line exclusions and the alternating paths directly.
No proof-development dialogue, author explanation or previous verdict on this claim was supplied.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0085_v1.md#statement) | Exact-stub degree and distinct-label bounds, odd alternating transports for arbitrary partial true-label matchings, and disjointness under the infinite-order hypothesis. |
| [Whole-argument finding](#whole-argument-finding) | [Projective incidence](../../claims/Yin_C_A0085_v1.md#projective-incidence-at-an-individual-group-element) | Polynomial proof of the even hull minimum, its equality cases, the minimum odd word and exclusion of weight 131. |
| [Whole-argument finding](#whole-argument-finding) | [Neutral degrees](../../claims/Yin_C_A0085_v1.md#the-neutral-degrees-on-the-four-lines) | Location of the excluded active and mixed points, degree improvements, odd private totals and nonbacktracking paths. |
| [Whole-argument finding](#whole-argument-finding) | [Alternating paths](../../claims/Yin_C_A0085_v1.md#alternating-paths-across-odd-edges) | Two odd lists and partial internal matchings, parity of cross-list paths, signed pigeonhole and selection on infinite cyclic cosets. |
| [Whole-argument finding](#whole-argument-finding) | [Four-line types](../../claims/Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings) | Projective incidences, inverse pairing, selected private stubs and exact forward-color counts. |
| [Whole-argument finding](#whole-argument-finding) | [Fine-state sums](../../claims/Yin_C_A0065_v1.md#exact-type-counts-and-the-thirteen-coordinate-histograms) | Recovering the required coarse private counts on both sides. |
| [Whole-argument finding](#whole-argument-finding) | [Private counts at actual labels](../../claims/Yin_C_A0078_v1.md#a-finite-cycle-from-the-four-private-lines) | Odd number of occurrences of a private signed stub in each indicated color. |
| [Whole-argument finding](#whole-argument-finding) | [Short-words input](../../claims/Yin_C_A0071_v1.md#short-words-separating-original-labels) | Logarithmic lower bound for the marked systole on the pattern event of the fixed matching law. |

## Whole-argument finding

The full argument verifies the stated graph and path conclusions.
For \(q=128\), any two line indicators have binary inner product one, including for identical lines.
The support of an even sum meets every line evenly, and if its positive weight is at most \(2q\), some line is empty since \(2q(q+1)<2(q^2+q+1)\).
Taking it to be \(Z=0\), the projective line indicator formula is independent of the choice of homogeneous representative by the \((q-1)\)-st power.
The constant terms cancel, and restriction of the homogeneous degree-\((q-1)\) sum to \((X,1,0)\) vanishes as a polynomial by its \(q\) roots.
After removing a factor \(Z\) the affine evaluation has degree at most \(q-2\).
Factoring the empty horizontal restrictions of a polynomial of total degree \(d<q\) bounds its zero count by \(sq+(q-s)(d-s)\le dq\).
It follows that the positive weight is at least \(2q\).

At equality, if every affine line met the support, even incidence would give exactly two points per line in every parallel class.
The \(q+1\) lines through a support point could then account for just \(q+1\) other points, contradicting \(2q-1>q+1\).
In a direction with \(s\) empty lines one has \(1\le s\le q-2\), because \(2q\) support points need at least two nonempty parallel lines.
Factoring the \(s\) linear factors gives at least \(s+2\) support points on each remaining line, forcing \(s=q-2\).
Both remaining affine lines are full and share only their deleted point at infinity after projective closure.
Hence the minimum even support is the symmetric difference of two distinct projective lines.
The cited classical classification is also stated with its textbook locator, Assmus–Key Theorem 6.4.2, in [Key, McDonough and Mavron, Result 2](https://users.aber.ac.uk/tpd/papers/hall-even-order-codes-postprint.pdf).
The degree estimates here follow from the preceding direct proof.

An odd word meets every line, so incidence counting gives at least 129 support points.
At weight 129, a missing point on a line through two support points would require at least 128 other points off the line, which exceeds the available 127.
Thus a minimum odd word is a line.
At weight 131 the symmetric difference with any line is nonempty and even, hence has size at least 256.
Every line would consequently meet the odd support in at most two points and, by parity, exactly one, contradicting a line through two support points.

An unselected line contains at most two active intersections, and at most one of the three active intersections outside any given selected line.
Indeed any two of that latter triple are on one of the other selected lines.
A symmetric difference of two lines therefore contains at most four active points whether zero, one or two of those lines are selected.
Removing also the three mixed points leaves at least 249 neutral stubs for weight 256.
All larger even weights are at least 258 and allow removal of all nine excluded points.
For minimum odd weight a selected line loses only its three active intersections, and any other line loses at most two active and three mixed points.
Larger odd weights start at 133, again leaving at least 124 neutral stubs.

The true-label inverse matching preserves parity of each retained signed end, so its image graph has the claimed degrees even with loops or parallel edges.
The private-stub total \(n(129/16513)/7-1\) is odd and applies on either side after summing the finer states, ensuring a nonempty graph.
Distinct nonbacktracking paths from a common vertex have distinct reduced words, since each signed letter specifies its next edge uniquely.
If two paths of length at most \(r\) reached one endpoint, free and cyclic reduction of their difference would give a nonempty cyclically reduced trivial word of length at most \(2r\).
The resulting tree count is \(1+\Delta\sum_{j=0}^{r-1}(\Delta-1)^j\), with \(\Delta=124\) in general and 249 under erasure.
A logarithmic marked systole supplies the indicated positive power of \(n\).

For each retained edge the two lists have the same odd size and the actual letter matching is a bijection between their separate copies.
The partial pairing within each list uses its entries in twos, leaving an odd number of degree-one endpoints on each side.
Every component with endpoints is an alternating path, and paths ending twice in a single list remove two endpoints from that list.
An odd number therefore have one endpoint on each side.
At each such endpoint the vertex is unmatched or its true-label partner lacks the required signed letter, since otherwise it would have an internal edge in the list.
The separate-list argument also applies when the two group labels agree.

Under complete erasure the sum of neutral degrees is at least \(249|V_c|\).
One of the 16504 signed letters occurs at that many incidences divided by 16504, with a different initial label for each incidence of this fixed letter.
For infinite-order \(t\) the finite sets of selected edges lie along disjoint two-sided paths \(g\langle t\rangle\).
Alternating their edges into two classes selects at least half without shared endpoint labels.
The associated alternating paths therefore use disjoint sets of actual vertices, giving the stated \(249|V_c|/(2\cdot16504)\) lower bound.
The argument counts paths that may change to a partner and yields the claimed endpoint defects for each supplied partial or complete matching.

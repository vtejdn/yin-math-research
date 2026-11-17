---
author: Yin
---

# A graph of odd stubs in each original-group color fiber

## Statement

Fix a connected realization with the [four selected lines of \(\mathrm{PG}(2,128)\), inverse pairing, and coarse type counts](Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings).
This includes the [thirteen-position counts](Yin_C_A0065_v1.md#exact-type-counts-and-the-thirteen-coordinate-histograms) after summing over the finer states.
Use the forward vertex labels on either side, and fix \(c\in\{3,5,6\}\).
At each original group element \(g\) over \(c\), let \(m_g\) be the vertex multiplicity and \(O_g\) the set of ordinary signed letters carried by an odd number of these vertices.
Call a signed letter neutral here if it is ordinary, its inverse is ordinary and its coarse increment is zero.
There are \(16504\) such signed letters in \(8252\) inverse pairs.

Construct a graph \(D_c\) with vertex set \(V_c=\{g:O_g\ne\varnothing\}\) inside the labelled Cayley multigraph of the original group.
Retain the edge from \(g\) to \(gt\) for each neutral \(t\in O_g\), with its reverse taken as the same unoriented edge.
This gives a nonempty finite graph, and the degree at \(g\), counting the two ends of a loop, is the number of neutral letters in \(O_g\).
Every surviving group label over \(c\) belongs to \(V_c\).
The local bounds are
\[
 \begin{array}{c|cc}
 & |O_g| & \deg_{D_c}(g)\\ \hline
 m_g\text{ odd}&\ge129&\ge124\\
 m_g\text{ even},\ O_g\ne\varnothing&\ge256&\ge249 .
 \end{array}                                                        \tag{1}
\]
In particular, full erasure of this color requires a finite nonempty subgraph of the actual neutral-letter Cayley graph with minimum degree at least \(249\).
This necessity applies regardless of the number or form of the relators used to certify equalities.

If the marking has no nonempty cyclically reduced trivial word of length at most \(2r\), with \(r\ge1\), then
\[
          |V_c|\ \ge\ 1+\Delta\sum_{j=0}^{r-1}(\Delta-1)^j,           \tag{2}
\]
where one may take \(\Delta=124\) always and \(\Delta=249\) under full erasure.
In particular there are at least \(n^\epsilon\) such distinct original labels for some fixed \(\epsilon>0\) on the marked-systole event at logarithmic scale in the four-line law.
This statement holds simultaneously on either side and in all three indicated colors.

For **any** partial matching by original-group equalities in color \(c\), each edge \(g\xrightarrow{t}gt\) of \(D_c\) forces an odd number of alternating paths between the two lists of vertices carrying its endpoint stubs.
Each path counted here starts with a carrier at \(g\) and ends with one at \(gt\), with each endpoint either unmatched or paired with a vertex missing the corresponding signed letter.
In particular, under full erasure and for any complete matching, one fixed neutral \(t\) gives at least \(249|V_c|/(2\cdot16504)\) vertex-disjoint such paths with distinct endpoint labels across the selected paths, provided the original neutral generators have infinite order.
They connect genuine failures of common readability at **both** ends of actual \(t\)-edges.
The alternating paths may change to the partner inside a group-label class between successive edge readings.

## Projective incidence at an individual group element

Put \(q=128\), and write \(f_g\) for the binary indicator of \(O_g\) on the \(v=q^2+q+1\) ordinary points.
Every occurrence contributes precisely the incidence vector of its ordinary line, irrespective of the extras it carries.
Thus \(f_g\) is a sum of \(m_g\) line indicators.
Its dot product with the indicator of every projective line is \(m_g\bmod 2\), since two different lines meet once and a line has odd cardinality \(q+1\).
Its own weight also has parity \(m_g\bmod2\).
For even \(m_g\) this puts \(f_g\) in the intersection of the line code with its dual, called the hull.
The hull minimum weight and its equality cases for a Desarguesian plane are classical. [Assmus–Key, *Designs and their Codes*, Chapter 6](https://www.cambridge.org/core/books/abs/designs-and-their-codes/codes-from-planes/AEE7B7CBEC1C84DD84729D4A1F8AF8B4)
Here is a direct binary proof, including the equality cases needed for the six active points.

Assume \(m_g\) is even, \(f_g\ne0\), and its weight \(w\le 2q\).
Some projective line avoids its support, since otherwise even intersection gives \(w(q+1)\ge2v>2q(q+1)\).
Take that line to be \(Z=0\) in homogeneous coordinates over \(\mathbb F_q\).
For a line with defining form \(\ell\), the indicator on projective points is \(1-\ell^{q-1}\), evaluated on any vector representing the point.
The even number of constants cancels in characteristic two, so \(f_g\) is represented by a homogeneous polynomial \(P(X,Y,Z)\) of degree \(q-1\), the sum of the \(\ell^{q-1}\) from its occurrences.
Since \(P(X,1,0)\) vanishes at all \(q\) field elements and has degree below \(q\), it is the zero polynomial.
By homogeneity this annihilates every term of \(P\) without a factor \(Z\).
Therefore \(P(X,Y,1)\) has total degree at most \(q-2\) and is nonzero on exactly \(w\) affine points.

A nonzero bivariate polynomial of degree \(d<q\) has at most \(dq\) zeros on \(\mathbb F_q^2\).
Indeed, factor off the \(s\) distinct horizontal lines on which its restriction vanishes identically.
On each other horizontal line the remaining nonzero restriction has at most \(d-s\) zeros, giving a total at most \(sq+(q-s)(d-s)\le dq\).
The affine polynomial therefore gives \(w\ge 2q\).
At equality, some affine line avoids its support.
Otherwise every parallel class would consist of \(q\) lines each containing exactly two support points, by the even intersection property and the total weight.
Then the \(q+1\) lines through any support point would contain exactly \(q+1\) other support points altogether, whereas \(2q-1>q+1\).
Use an empty affine line as the horizontal direction, with \(1\le s\le q-2\) empty lines parallel to it.
Factoring those lines shows that each of the remaining horizontal lines contains at least \(s+2\) support points.
Hence \(2q\ge(q-s)(s+2)=2q+s(q-2-s)\), forcing \(s=q-2\).
The support is the union of two full parallel affine lines, or equivalently the symmetric difference of two projective lines.

If \(m_g\) is odd, \(O_g\) meets all lines and \(w(q+1)\ge v\), so \(w\ge q+1\).
Equality forces \(O_g\) to be a projective line: take the line through two support points and, if it is not all in the support, take a missing point on it.
The other \(q\) lines through the missing point would need \(q\) distinct support points off the first line, where at most \(q-1\) are available.
Weight \(q+3=131\) is impossible.
Otherwise adding any single line vector gives a nonzero even word of weight at least \(2q\), so each line would meet \(O_g\) in at most \((131+129-256)/2=2\) points.
All intersections would then have size one, contradicting the line through two support points.

## The neutral degrees on the four lines

The only excluded ordinary points are the six intersections of the four selected lines and the three ordinary points paired with extras.
For an even word of weight strictly larger than 256 the weight is at least 258, hence at least 249 ordinary points remain after these exclusions.
At weight 256 use the symmetric difference just proved.
Two selected lines retain four active points in their difference, since their common intersection cancels.
A nonselected line contains at most two active points: any three of the six pairs of line indices contain two pairs sharing an index, and the corresponding intersections determine that selected line.
Moreover, outside one specified selected line the three active points come from pairs of the remaining three indices, so a nonselected line contains at most one of them.
Thus the difference of a selected and a nonselected line, or of two nonselected lines, also includes at most four active points.
Removing these and at most three mixed ordinary points leaves at least \(256-7=249\).
For an odd word of minimum weight the selected lines lose three active points and contain no mixed ordinary points; any other line loses at most two active and three mixed ordinary points.
The neutral count is at least 124.
All larger odd weights are at least 133 and give the same bound after at most nine exclusions.

The stub matching is an actual bijection between occurrences of \(t\) at a group-label fiber \(g\) and occurrences of its inverse at the fiber \(gt\): traverse the graph edge and then its inverse.
Thus membership in the odd set agrees at these two signed ends.
Neutral increments preserve \(c\), proving that \(D_c\) and the degrees in (1) are as stated.
For any private point on a selected line the number of its stubs in color \(c\) is \(n(129/v)/7-1\), an odd integer at the admissible sizes.
At least one group-label fiber has an odd number of them, proving nonemptiness. [Coarse private-stub counts](Yin_C_A0078_v1.md#a-finite-cycle-from-the-four-private-lines)

Under the short-word hypothesis, two distinct nonbacktracking paths of lengths at most \(r\) from one vertex cannot end at the same vertex.
Their concatenation after reversing the second path freely reduces to a nonempty null word of length at most \(2r\), because there is a unique path from the start with any given word in the labelled Cayley graph.
Cyclic reduction gives the forbidden cyclic word.
Counting the paths by successive choices proves (2).
In a pattern-free four-line realization at \(L=\lfloor c_0\log n\rfloor\), the marked systole is at least \(c_*L\); take, for example, \(r=\lfloor c_*L/3\rfloor\) for large \(n\).
The same geometric input holds in the fixed thirteen-position law by its bounded-pattern comparison. [Marked systole and finite-state transfer](Yin_C_A0071_v1.md#short-words-separating-original-labels)
This gives the asserted positive power of \(n\) for that event by (2).

## Alternating paths across odd edges

For one oriented edge of \(D_c\), make two vertex lists: the carriers of \(t\) at \(g\) and the carriers of \(\bar t\) at \(gt\).
Use separate copies of the lists, even if group elements happen to agree.
Their cardinalities are the same odd integer.
Join corresponding entries by the actual \(t\)-edge bijection.
Inside each list add a partial matching edge when two of its members are paired to each other by the given original-label matching.
Each list member now has one crossing edge and at most one internal edge.
Every degree-one endpoint is a carrier whose true partner is missing from that list, either because it is unmatched or because the partner has the same original label and lacks the required letter.
The number of these endpoints in the first list is odd, because the internal edges use members in twos.
Paths with both ends in the first list consume two of them, while paths with both ends in the second list consume none.
An odd number of the alternating paths therefore join the two different lists.
This assertion is simultaneous for any actual pairing, including one obtained by splicing prescribed matches on finitely many marked blocks.

Under full erasure the total count of neutral signed incidences in \(D_c\) is at least \(249|V_c|\).
Some fixed \(t\) then has at least \(249|V_c|/16504\) different initial labels for these edges.
If \(t\) has infinite order, its oriented edges lie along disjoint translates of the two-sided path on \(\langle t\rangle\).
At least half of this finite collection can be selected with no shared endpoint, by splitting each path into the two alternating edge classes.
Choosing one crossing path in the preceding two-list construction for each selected edge yields the asserted vertex-disjoint transports.
On a pattern-free torsion-free realization at large \(L\), the marked systole ensures nontriviality of each rose generator and torsion-freeness gives infinite order.
The transported defects use a neutral signed letter, whereas the [private-line boundary argument](Yin_C_A0078_v1.md#statement) concerns a fixed active signed letter.
Neither the counting of defects nor a path that changes to a partner constructs a single word that exchanges the ends of two independent marked blocks.

## Assessment history

### Decision odd-stub-degrees

| Field | Value |
| --- | --- |
| date | 2026-11-17T14:37 |
| status | proved |
| reason | The reviewed argument verifies the incidence bounds and the stated scope of alternating paths. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Odd-stub graphs in true color fibers, local neutral degrees and alternating transports. |
| argument | [Proof](#projective-incidence-at-an-individual-group-element) | Binary line weights and equality cases, neutral incidences, marked growth and transport under an arbitrary pairing. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0121_v1.md#whole-argument-finding) | Independent review of the argument and its stated scope. |

## Current assessment

[Selected decision](#decision-odd-stub-degrees)

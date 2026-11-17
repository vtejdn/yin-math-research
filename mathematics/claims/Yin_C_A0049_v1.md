---
author: Yin
---
# Almost every pair lies in a whole group-product fiber of the simultaneous-step graph

## Statement

Take the two graphs of Ope26f, with \(n\) prescribed-type vertices on each side, conditioned on the logarithmic girth event.
Use either the [original uniform matching law](Yin_C_A0041_v1.md#statement) or the [balanced planted \(C_7\) law](../ledger/Yin_L_A0047_v1.md#the-bounded-pattern-estimate-with-the-seven-colors), with their respective choices of girth scale \(L\).
Fix \(x\) on side \(A\) and \(y\) on side \(B\) before sampling.
Use their components for the following comparison.
Any choice of reference root in each component gives forward path labels \(g_u,h_v\) in the cone group \(G_n\).
Moving the reference roots does not change which products \(g_u h_v^{-1}\) are equal, since the whole list is multiplied by common group elements on the left and right.

With probability tending to one the following equivalence holds for this fixed pair and *all* pairs \((x',y')\) in the same two graph components:
\[
  g_xh_y^{-1}=g_{x'}h_{y'}^{-1}
    \quad\Longleftrightarrow\quad
  (x',y')\text{ is reachable from }(x,y)\text{ by simultaneous steps}. \tag{1}
\]
The error bound tends to zero uniformly over the two prescribed vertices.
Consequently, with probability tending to one along a deterministic \(o(n^2)\) error bound, both graphs are connected and all but \(o(n^2)\) of the vertex pairs belong to product fibers consisting of a single simultaneous component.
The exceptional pairs are counted by their total cardinality, including all vertices in every affected fiber.
These probability statements persist under further conditioning on the source's high-probability topological safeguards in the specified law.
They do not assert (1) simultaneously at every pair.

Writing \(A_*,B_*\) for the actual supports after collection in \(\mathbb F_2[G_n]\), with the inverse convention already incorporated into \(B_*\), yields
\[
       \frac{|A_*B_*|}{n^2}\ \longrightarrow\
           \frac{1-128/16513-3(129/16513)^2}{2}
              \qquad\text{in probability}.                              \tag{2}
\]
Here \(A_*B_*\) counts distinct elements represented by some surviving support pair, even though their group-ring product vanishes in characteristic two.

## A bounded pattern with one prescribed interval on each side

The [source estimate, Proposition 3.1, pp. 7–14](../literature/pdf/Ope26f.pdf#page=7), permits one prescribed interval.
We first establish its variant with up to two, of which at most one is on each side, starting at \(x\) or \(y\) as appropriate.
An interval can equivalently be read toward its prescribed endpoint by reversing it and updating its comparison orientations.
Within fixed bounds \(K,C,I\) there are at most \(K\) paths, total length \(L\le H\le CL\), at most \(I\) comparison interval pairs, and at most \(\epsilon H\) unpaired occurrences.
All other paths are cyclically immersed and the source reduction condition (3.1) is retained.
The event of such a system still has probability \(o(1)\), with \(\epsilon>0\) chosen before \(K,C,I\).

To check the change, let \(s\le2\) be the number of intervals in the putative bounded system.
The image graph has at most \(2s\) leaves.
The source's bounded core-rank argument uses only girth and the total number of edges, giving boundedly many branching marks after the at most four leaves and all endpoints are marked.
All chains still have constant traversal multiplicity, with the same bound \(m_*\le2(C+K)\) from (3.2).
The abstract pattern enumeration has polynomial cost in \(L\) for these fixed bounds, including the two root designations.
For an image vertex \(z\), let \(a(z)\) be the number of interval endpoints there, counted with multiplicity.
Pairing successive traversal incidences off the endpoints gives
\[
  2\max_{e\ni z}m_e\ \le\ \sum_{\text{half-edges at }z}m_e+a(z).
\]
Summing and using \(\sum_z a(z)=2s\) gives \(\sum_j V_j\le H+s\) for the source multiplicity stages.
Set \(k_1=s\) and \(k_j=0\) for \(j>1\).
The \(s\) fixed initial vertices of stage one are distinct whenever both are present, since they lie on opposite sides.
Each has at most one possible image and is marked.
This gives the factor \(n^{V_j-E_j-k_j}\) in the original model and \(\sum_j(V_j-E_j-k_j)\le0\), since \(\sum_j E_j=H\).
Later stages require no root saving.

The internal turn comparisons, aligned chain blocks, self-links, bins and numerical selection of a small stage in source (3.5)–(3.12) use the bounded chain count, multiplicities, word comparisons and the preceding exponent sum.
Adding a second endpoint pair changes only the bounded number of marks and interval cuts.
It leaves the good-block turn estimate, the upper bound on multiplicities and the proportions of unpaired positions unchanged.
Thus the numerical product of stage bounds has logarithm at most \(-\delta H/2+a_0 b+o(L)\), where \(b\) is the number of unpaired positions and \(\delta,a_0\) are the source word constants.
The choice of \(\epsilon\) in the source, the stage selection and its final union bound then give the asserted \(o(1)\).
In the planted law a stage gains at most the additional factor \(7^{b_j+E_j-V_j+k_j}\), where \(b_j\) counts its connected components.
As in the [planted proof](../ledger/Yin_L_A0047_v1.md#the-bounded-pattern-estimate-with-the-seven-colors), this is bounded independently of \(n\), because the stages consist of boundedly many whole chains and now \(k_1\le2\).
All vertex-image and switching estimates used here are upper bounds uniform in the prescribed names and their types or colors.

## Localizing a two-break spherical arrangement

Allow one exterior boundary of an arrangement to consist of the concatenation of an immersed interval \(P_A\) from \(x\) on the first side and the reverse of an immersed interval \(P_B\) from \(y\) on the second.
It has at most two breaks and at least one positive-length ordinary cyclic boundary is required.
An empty interval can be omitted.
All arcs must pair inverse signed letters on distinct underlying edges, as in source Definition 4.1.
We show that such an arrangement is absent with probability \(1-o(1)\).

On the source diameter event the closing construction in Lemma 4.2 applies separately to any immersed segment on either side.
Choose the same kind of cutoff \(UL\) as in Proposition 4.5.
Keep a short interval intact and split each longer interval separately in its linear order, closing its segments with at most \(D_0L\) added unpaired edges per segment.
Do the same splitting and closing for the long ordinary paths; \(D_0\) denotes the source's uniform closure constant.
With original length \(H_0\), total added length is bounded by \(3D_0H_0/U\).
The number \(N'\) of resulting pieces satisfies \(N'L\le H_0+2L\le3H_0\), because only the two intact short intervals can fall below \(L\) in original length, while an ordinary boundary contributes at least \(L\).

Lemma 4.3 gives at most \(aN'\) comparison intervals in pairs for an absolute constant \(a\) also in this setting.
In its disk-and-band Euler count the number of disk monogons is at most two since each must use a break.
Thus (4.1) still bounds non-good gaps linearly in the number of disks, including the repeated-edge disk digon bound.
Cut at both breaks and at their opposite good gaps as well as at the ordinary indexing and splitting gaps.
The good-gap involution yields \(O(N')\) runs just as in that lemma; an internally self-paired run contradicts immersion or would have a fixed occurrence.
Replacing the exterior disk locally by the pieces in its consecutive sectors, now cut at both breaks, preserves planarity of the piece graph.

By recursive planar separation, delete at most \(\eta N'\) pieces to leave clusters of at most \(K\) pieces, where \(K\) depends only on \(\eta\).
At most \(3\eta U H_0\) original positions are lost; at most that many surviving positions lose their partners.
All retained interval pairs remain whole.
Take \(3D_0/U<\epsilon/100\) with \(U\ge3\), then \(3\eta U<\min(1/40,\epsilon/100)\), and take \(C_2\) with \(3a/C_2<1/40\).
The retained length is at least \(39H_0/40\).
Clusters exceeding the unpaired fraction \(\epsilon\) cost less than \(H_0/50\) in length.
Those exceeding \(C_2 H_Z/L\) interval pairs at cluster length \(H_Z\) cost less than \(H_0/40\).
Clusters of length below \(L\) consist entirely of intact short intervals and have combined length \(h<2L\).
Because the original boundaries also contained an ordinary cyclic path, \(h\le H_0-L\) and \(h<2H_0/3\).
After these three exclusions a positive amount of admissible cluster length remains.
The surviving cluster has \(L\le H_Z\le K(U+D_0)L\), at most \(\lceil C_2 K(U+D_0)\rceil\) interval pairs, and satisfies the reduction condition.
Every retained open interval is an entire unsplit interval with the designated endpoint on its own side.
This contradicts the preceding bounded-pattern estimate off an event of probability \(o(1)\), in the same quantifier order as [Ope26f, §§4.1–4.4](../literature/pdf/Ope26f.pdf#page=15).

## From a product equality to the arrangement

Simultaneous steps preserve \(g_xh_y^{-1}\).
Conversely suppose equality holds for some \((x',y')\) outside the simultaneous component of the prescribed pair.
Equality means that a path \(P_A:x\to x'\) and a path \(P_B:y\to y'\) have the same group label.
The concatenated rose word \(P_AP_B^{-1}\) admits a disk cone picture: apply the ordinary rose-with-relator-disks argument of source Lemma 5.2 to this null word, preserving its two specified lifts on the outer boundary.
Among such pictures with these four endpoints, allowing either lifted path to vary on its own side, minimize the total boundary length.
Tighten each interval relative to its endpoints and each inner disk cyclically; any constant inner disk can be removed.
There must remain an ordinary inner disk.
Otherwise \(P_A,P_B\) have the same freely reduced word in the rose, and lifting its consecutive letters gives a simultaneous path between the designated pairs.
This also covers an empty tightened interval, since an immersed path with trivial free word is empty.

The band cancellations of [Ope26f, §5.3](../literature/pdf/Ope26f.pdf#page=22) apply to the paired letter occurrences outside the cone disks.
Two equal underlying edges on inner boundaries allow the ordinary same-cone surgery.
If one is exterior, splicing the inner closed path into that interval changes only that side's lifted path between its original endpoints.
If both are exterior they lie on the *same* interval because the two graphs are disjoint, even though they map to the same rose.
Between the two inverse occurrences along that interval lies a break-free subpath.
The complementary subdisk retained after cancelling the band has the spliced interval with its original endpoints and the other interval unchanged, as in the exterior-twice case of the source surgery.
The same-side splicing reduces the boundary length and does not identify the two members of either prescribed endpoint pair by fiat.
Thus minimality excludes every such unreduced arc.
The minimized picture has the two-break exterior and at least one ordinary disk, and gives precisely the excluded arrangement.
The argument tests the two-root arrangement afresh; the original one-root separation statement alone does not imply (1).

## Quenched projections and the size of the represented product set

Count all vertex pairs on the connected event.
The event that a prescribed pair is in a fiber containing another simultaneous component is exactly the failure just bounded.
Uniformity, linearity of expectation and Markov's inequality give an \(o(n^2)\) count in probability, or a deterministic \(o(n^2)\) upper bound with probability tending to one.
The original and planted connectedness and root-separation conclusions hold with probability tending to one in their respective girth-conditioned laws, so intersecting or conditioning on those events preserves this assertion.
No independence of different prescribed-pair tests has been used.

On a fixed connected tuple let \(E_{\rm comp}\) and \(E_{\rm prod}\) average a function uniformly on each simultaneous component and on each actual product fiber, respectively.
The former is the long-time averaging projection of the [symmetric lazy common-step walk](Yin_C_A0047_v1.md#the-fixed-graph-walk).
The exceptional fibers form a union of whole components and have vertex-pair fraction \(e_n=o(1)\) in probability.
Outside them the two averages coincide.
For any bounded observable \(f\), with uniform probability on vertex pairs, this proves
\[
       \|E_{\rm comp}f-E_{\rm prod}f\|_2
                         \ \le\ 2\sqrt{e_n}\,\|f\|_\infty .
\]
It also gives normalized trace difference at most \(e_n\) for the two nested averaging projections.

On the source's ordinary-arrangement prohibition the simultaneous graph is a forest: a reduced cycle would project immersively to the disjoint sides, giving two ordinary boundaries with an annular reduced pairing.
The degree of \((u,v)\) is one plus 128 for equal ordinary line types plus two when both extra types are nonempty.
The exact proportions from §2.1 give mean degree \(1+128/16513+3(129/16513)^2\).
Subtracting half the total degree from \(n^2\) therefore counts the components.
Identifying components in actual product fibers loses at most the number of exceptional vertex pairs, which is \(o(n^2)\) in probability.
Deleting repeated-label occurrences before forming \(A_*,B_*\) can remove at most another \(o(n^2)\) represented products: on either side \(n-o(n)\) singleton occurrences survive by the [original](Yin_C_A0040_v1.md#distinct-labels-away-from-the-roots) and [planted](../ledger/Yin_L_A0047_v1.md#occurrence-counts-and-the-actual-characteristic-two-supports) one-root bounds.
This gives (2).
The comparison controls the typical mass of whole product fibers in the two matching laws; it does not identify all word equalities of any specific finite matching, nor say what happens on an exceptional matching conditioned on erasing a color.

## Assessment history

### Decision two-prescribed-vertices

| Field | Value |
| --- | --- |
| date | 2026-11-17T08:44 |
| status | proved |
| reason | The review checked the two prescribed paths, surgery with four fixed endpoints, probability quantifiers and the use of the forest count. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Typical equality between the simultaneous component and the whole product fiber, and the size of the represented product set in both laws. |
| argument | [Proof](#a-bounded-pattern-with-one-prescribed-interval-on-each-side) | Complete argument under the stated hypotheses. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0080_v1.md#whole-argument-finding) | Review of the entire argument with its stated dependencies. |

## Current assessment

[Selected decision](#decision-two-prescribed-vertices)

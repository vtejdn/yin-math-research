---
author: Yin
---
# Two prescribed vertices and typical purity of a product fiber

A separate reviewing agent checked the entire [fixed Claim](../../claims/Yin_C_A0049_v1.md) for Yin on 2026-11-17T00:40 UTC.
The reviewer had worked on the common-step walk and the [finite cross-side forest count](../../ledger/Yin_L_A0050_v1.md#forest-and-return-probability).
That earlier count supplies an input to the product-set asymptotic.
The reviewer did not develop the two-interval probability estimate, planar localization, equality-of-paths argument or typical purity conclusion.
The intended target and earlier forest dependency were known, but no substantive development of the two-root proof, author explanations, exploration notes or prior verdict on it were supplied.
The previously inspected one-root source and original and planted matching estimates were reused, and the source's exact cuts and disk surgeries were reread for the two-break check.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0049_v1.md#statement) | Uniform fixed-pair conclusion, typical mass of whole fibers, both matching laws, conditioning and actual represented-product limit. |
| [Whole-argument finding](#whole-argument-finding) | [Two prescribed paths](../../claims/Yin_C_A0049_v1.md#a-bounded-pattern-with-one-prescribed-interval-on-each-side) | Endpoint multiplicities, saved root choices, string estimates and stage selection. |
| [Whole-argument finding](#whole-argument-finding) | [Localizing the arrangement](../../claims/Yin_C_A0049_v1.md#localizing-a-two-break-spherical-arrangement) | Both cuts, monogon and interval counts, planar separation, length losses and the two short intervals. |
| [Whole-argument finding](#whole-argument-finding) | [Equality and minimal diagrams](../../claims/Yin_C_A0049_v1.md#from-a-product-equality-to-the-arrangement) | Existence of an inner disk, all four endpoints and reducedness after same-lift band surgery. |
| [Whole-argument finding](#whole-argument-finding) | [Averaging and count](../../claims/Yin_C_A0049_v1.md#quenched-projections-and-the-size-of-the-represented-product-set) | Uniform pair averaging, mass of impure fibers, projection comparison and collection losses, using the earlier exact forest count. |

## Whole-argument finding

Left multiplication of all forward labels by a common element on each side changes every product by the same left and right multipliers, so the prescribed-pair test does not depend on the other reference roots.
Failure is witnessed by two paths from the fixed vertices whose group labels agree while their two endpoints cannot be reached by one common sequence of steps.
Only the two initial vertices need be fixed for the probability bound.

For the bounded-pattern argument, up to \(s\le2\) open intervals give at most \(2s\) leaves and \(2s\) endpoint incidences, with multiplicity even when endpoints repeat.
The core cycle-rank bound, bounded number of chains and edge-traversal bound use only the girth, length, path count and bounded number of marks.
Every incidence on a maximal-multiplicity half-edge must be paired with a different half-edge or an interval endpoint.
After summation the excess in \(\sum_j V_j\) over \(H\) is at most \(s\).
The first stage contains the entire image, with one prescribed marked vertex per nonempty interval.
When both are present they lie on disjoint sides, giving two distinct saved choices.
Reversing the reading of the second interval can put this mark at its starting end and only changes the orientations of its comparison strings.
Thus \(\sum_j(V_j-E_j-k_j)\le0\) without assuming independence of the stages.
The turn, alignment, self-link, bin and unpaired-position estimates of [Ope26f, (3.5)–(3.12)](../../literature/pdf/Ope26f.pdf#page=10) depend on bounded chain data and leave the same exponential saving with the additional fixed endpoint marks.
In the planted model the extra factor is a fixed power of seven bounded by the stage cycle rank plus at most two prescribed vertices.
It is absorbed in \(\exp(o(L))\).
Both counts are uniform in the names of the two prescribed vertices.

Splitting a long exterior path at its own break-free segments preserves the closing bound for that side.
Only an entire unsplit short interval can retain an open endpoint or contribute less than \(L\) original length.
Consequently \(N'L\le H_0+2L\) and the added length is at most \(3D_0H_0/U\).
In the disk-and-band Euler calculation of [source Lemma 4.3](../../literature/pdf/Ope26f.pdf#page=16), a monogon requires a break, so its count grows from at most one to at most two.
The repeated-edge digons still use degree-one gaps.
Cutting at both breaks and at each opposite good gap keeps the cut set stable under the good-gap involution.
Thus reversing a run maps it to another whole run and internal self-pairing remains impossible by immersion or a fixed occurrence.
These modifications give \(O(N')\) interval pairs with each pair contained in its two pieces.
Replacing consecutive sectors of one disk by separate vertices preserves planarity at the two breaks.

The separator deletes at most \(3\eta UH_0\) original positions and costs at most the same number of partners among surviving positions.
The specified constants give retained total length at least \(39H_0/40\); excess-unpaired and excess-interval clusters together lose at most \(H_0/50+H_0/40\).
Short clusters consist of parts of the at most two intact intervals and have total length \(h<2L\) with \(h\le H_0-L\), because there is an original ordinary boundary of length at least \(L\).
For \(H_0<3L\) use the second bound, and for \(H_0\ge3L\) use the first, to obtain \(h<2H_0/3\).
The remaining length is positive and yields a cluster satisfying the bounded-pattern cutoffs fixed before taking \(n\to\infty\).
If a short interval survives in that cluster it retains its own designated endpoint.

The null rose word \(P_AP_B^{-1}\) gives a disk picture by the source's relative rose-with-disks construction, with the two specified lifts carried on separate arcs of its exterior.
Keep the four endpoints fixed while minimizing total boundary length.
After relative tightening, a picture with no inner disk would have the same freely reduced word on both sides, hence would supply simultaneous steps reaching the two endpoints.
The failure assumption therefore forces an ordinary disk to remain.
For inner-inner and inner-self bands, the modifications in [Ope26f §5.3](../../literature/pdf/Ope26f.pdf#page=22) preserve the disk-domain failure and shorten the picture.
For an exterior-inner band, its graph edge lies in one side, so inserting the matching inner path changes only that interval between its prescribed endpoints.
For an exterior-exterior band both occurrences of the same lifted edge necessarily lie on one interval because the two graphs are disjoint.
In its linear order they enclose a break-free subpath between inverse traversals of that edge.
The complementary exterior arc contains the other interval and both break points.
The retained complementary disk consequently gives the spliced same-side path with its two old endpoints and the entire opposite interval with its two old endpoints.
The contractions remove two occurrences as in the source's exterior-twice row, contradicting minimality even when an interval becomes empty.
Thus the minimized picture gives precisely the reduced two-break arrangement already probabilistically excluded.

For each prescribed pair the bound controls existence of *any* extra component in its fiber.
Every point of an impure fiber is a failing test point on connected sides.
Linearity of expectation, uniformity and Markov's inequality therefore bound the total cardinality of whole impure fibers by \(o(n^2)\) in probability, with a deterministic subquadratic threshold available.
Further conditioning on events already of probability tending to one preserves the conclusion in the respective laws.
The two averaging operators coincide off this exceptional mass and have pointwise difference at most \(2\|f\|_\infty\), giving the stated \(L^2\) bound.
Their ranges are nested and the difference is supported on the exceptional coordinates, so its normalized trace is at most the same mass fraction.
The finite forest formula gives \(n^2(1-128/16513-3(129/16513)^2)/2\) simultaneous components.
Passing to true product fibers loses at most the number of exceptional pairs.
Both original and planted single-vertex estimates leave \(n-o(n)\) singleton group labels on each connected side, so discarding all other occurrence pairs can remove at most \(o(n^2)\) distinct represented products.
This yields (2) for the actual supports.
The review verifies the two-root extension and its new consequences in both laws, using the source's one-root probabilistic and geometric machinery at its stated scope.

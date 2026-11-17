---
author: Yin
---

# The four-line construction with nonzero projected factors

An agent outside the development of the proof independently reviewed the fixed statement and all four proof sections of Yin_C_A0051_v1 for Sheng Yin at 2026-11-17T00:56 UTC.
The reviewer received no development discussion, summary of the proposed reasoning, author explanation or prior conclusion about the four-line construction.
The reviewer read the cited mathematical inputs and checked their applicability to the modified matching law.
The review used the earlier balanced-model results at the interfaces identified below.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0051_v1.md#statement) | The specified inverse pairing, admissible sizes, quotient, two histograms, conditional probability assertions, deterministic erasure implication and uniform product bound. |
| [Whole-argument finding](#whole-argument-finding) | [Four lines and matchings](../../claims/Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings) | Partition of all letters, preservation of both full type totals and exact block bijections, descent to the cone group, reflection and convolution. |
| [Whole-argument finding](#whole-argument-finding) | [Geometric safeguards](../../claims/Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts) | Switching before and after girth conditioning, expansion, multiplicity-stage bounds, uniformity for a prescribed vertex and deterministic source conclusions. |
| [Whole-argument finding](#whole-argument-finding) | [Connectedness and collection](../../claims/Yin_C_A0051_v1.md#connectedness-collection-and-the-erasure-threshold) | Large cuts, probability of repeated labels, parity and occupancy after collection, projected lifting and the two-sided erasure bound. |
| [Whole-argument finding](#whole-argument-finding) | [Product fibers and coefficients](../../claims/Yin_C_A0051_v1.md#product-fibers-and-complex-coefficients-in-the-four-line-law) | Transfer of two-root purity, represented-set limit, deletion-stable odd indices and the simultaneous lower bound for all permitted coefficients. |
| [Whole-argument finding](#whole-argument-finding) | [Balanced switching](../../ledger/Yin_L_A0047_v1.md#girth-local-expansion-and-the-cost-of-a-matching-prescription) | Same-block transpositions, reverse counting, local expansion and diameter estimates. |
| [Whole-argument finding](#whole-argument-finding) | [Balanced rooted stages](../../ledger/Yin_L_A0047_v1.md#the-bounded-pattern-estimate-with-the-seven-colors) | Propagation of colors, turn counts and the power of seven remaining after imposing the edges. |
| [Whole-argument finding](#whole-argument-finding) | [Balanced cut entropy](../../ledger/Yin_L_A0047_v1.md#connectedness-and-the-other-finite-quotients) | Strict loss for binary cuts of macroscopic density. |
| [Whole-argument finding](#whole-argument-finding) | [Singleton criterion](../../claims/Yin_C_A0040_v1.md#distinct-labels-away-from-the-roots) | Root-independent ambiguity and averaging over individual prescribed vertices. |
| [Whole-argument finding](#whole-argument-finding) | [Seven-class lifting test](../../claims/Yin_C_A0042_v1.md#statement) | Exact lift of the projected equations with two four-element odd masks and seven occupied classes on each side. |
| [Whole-argument finding](#whole-argument-finding) | [Isolated component count](../../claims/Yin_C_A0047_v1.md#the-fixed-graph-walk) | Deterministic exceptional fraction from the two sides' uncolored type counts. |
| [Whole-argument finding](#whole-argument-finding) | [Two-root stages](../../claims/Yin_C_A0049_v1.md#a-bounded-pattern-with-one-prescribed-interval-on-each-side) | Distinct root savings, deterministic passage from a merged fiber to a two-break arrangement and uniform averaging. |
| [Whole-argument finding](#whole-argument-finding) | [Represented product count](../../claims/Yin_C_A0049_v1.md#quenched-projections-and-the-size-of-the-represented-product-set) | Forest component count and losses from merged fibers and repeated vertices. |
| [Whole-argument finding](#whole-argument-finding) | [Deletion entropy gap](../../claims/Yin_C_A0050_v1.md#a-uniform-gap-under-deletions) | Stability of the zero-defect entropy gap for finite binary tables under convergent weights. |
| [Whole-argument finding](#whole-argument-finding) | [Full group-product bound](../../claims/Yin_C_A0050_v1.md#actual-product-fibers-after-edge-removal) | Deterministic inequality for arbitrary unit coefficients after redistribution over repetitions. |

## Whole-argument finding

The four selected lines have six distinct intersections and 126 private points apiece.
After setting aside the three ordinary partners for the extras, 16,000 exterior ordinary letters remain, so all zero-increment pairings can be made.
The three nonzero-increment pairs exhaust the six intersections, and translation by the indicated increment sends each incident pair of line indices to the required other pair.
This verifies the equality of the two sizes of each matching block, including those on the second side, whose extra types have different frequencies.
Every realized edge has the prescribed color displacement and one displacement generates \(C_7\), proving that the surjection survives the cone relations.
The ordered-difference multiplicities of \(K\) are \(4,2,2,2,2,2,2\) starting at zero.
Reflection on the second side consequently gives corrections \(+84\) and \(-14\) to \(n^2/7\), with both occurrence parity indicators nonzero.

The number of distant edges available in a switched block is linear in \(n\), even after its bounded change in size.
Both the bad-edge exclusions in the initial repair and the radius-\(2L\) exclusions in the conditional switch are sublinear.
For \(O(L)\) prescriptions the accumulated relative error has logarithm \(o(L)\).
For expansion through size \(\rho n\), the prescribed edges instead use at most a third of a block, leaving the \(2/N\) bound needed in the summable small-set estimate.
In a multiplicity stage every positive unrestricted turn count grows linearly in \(n\), and changing the color counts by bounded integers adds no structurally absent turn.
Each component's first chosen color determines the rest, so over \(O(L)\) vertices the perturbation costs \(\exp(O(L/n))\) in addition to the bounded factor \(7^{b_j+E_j-V_j+k_j}\).
The root-image bounds hold uniformly for the designated names.
These checks preserve the exponential saving of the source stage calculation for fixed pattern bounds and permit its deterministic diameter, arrangement and cone arguments.
I checked the allowed involution, the uncolored turn weights, the probability estimates used in the transfer, and the hypotheses of the deterministic implications in [Ope26f, §§2–6](../../literature/pdf/Ope26f.pdf#page=4).
The source's deterministic planar and cone-picture results are used at those hypotheses.
This review did not independently reconstruct their internal topology proofs.

A macroscopic cut would retain positive density on both sides in a convergent subsequence of its finite histograms.
At zero entropy loss all line types sharing an ordinary point carry one cut bit at any fixed color, and the increment \(1\) forces the bit to agree across colors.
This excludes the proposed cut in the balanced limit.
The strict gap survives the bounded changes of counts and the subexponential cost of girth conditioning.
Uniform separation for one specified root bounds the expected number of repeated vertices by \(o(n)\), giving the claimed simultaneous class bounds after collection.
Deleting the omitted occurrences loses \(o(n^2)\) pairs, while parity in each product class is unchanged by convolution of the two reduced histograms.
The two four-element masks and the seven occupied classes meet the cited lifting criterion for the projected equations.

Two-sided erasure forces at least \(r=3n/7-12\) repeated vertices per side.
Of the \(n^2-(n-r)^2\) or more pairs meeting these vertices, at most \(0.009n^2\) can lie outside isolated simultaneous edges.
At any remaining such pair, changing only the repeated coordinate keeps the group product and leaves the component, because the other endpoint on the edge differs in both coordinates.
The limiting lower fraction \(1-16/49-0.009>0.6644\) proves the stated strict bound for all sufficiently large admissible \(n\).
This is an implication for a fixed connected tuple with both erasures.

For purity the two prescribed roots belong to disjoint sides, and both still contribute their distinct stage-one image savings.
The modified stage estimates therefore allow the existing deterministic two-break argument and bound the expected *mass* of impure pairs by \(o(n^2)\).
On the forest event the original degree total is exact, so merging impure components and collecting repeated vertices leave the same normalized represented-set limit.
For deletion stability the variables of the finite joint-table problem lie in a fixed compact product of simplexes.
The perturbed block masses stay bounded away from zero after division by \(n\), so the marginal constraints, violation density and entropy exponent pass to the balanced limit.
At zero defect, a nonnegative entropy exponent would force one bit per planted color, and iteration through the odd order of every retained displacement then forces each assigned bit to vanish.
This gives a strict uniform gap and hence exponentially small deletion failure after girth conditioning.
The deterministic product estimate then applies on one event for all rings and all unit coefficients in the statement.
In particular ramified valuation rings modulo four still satisfy \(2\ne0\), and marked lifts are units there.

The complete stated construction and its projected-lifting and full-product consequences are supported at the indicated scopes.
The review establishes neither existence of a tuple realizing the simultaneous erasures nor a result for arbitrary supports of a torsion-free group.

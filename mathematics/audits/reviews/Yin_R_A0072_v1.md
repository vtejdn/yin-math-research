---
author: Yin
---
# Fixed finite targets for source matchings and a planted cyclic quotient

A separate reviewing agent inspected the complete fixed [Claim](../../claims/Yin_C_A0041_v1.md) and the [planted matching argument](../../ledger/Yin_L_A0047_v1.md) for Yin on 2026-11-16T18:15 UTC.
The reviewer did not develop either entropy or matching argument or receive substantive development discussion, author explanations, exploration notes or prior verdicts on them.
The subset of Ope26f used for the change of law was read directly, including the prescribed type counts, conditional switching, bounded-chain analysis, stage realization count, arrangement reduction and final deterministic interfaces.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |
| [Planted quotient finding](#planted-quotient-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0041_v1.md#statement) | Probability of a nontrivial finite target, bounded lists, conditioned law and existence on the stated source realizations. |
| [Whole-argument finding](#whole-argument-finding) | [Vertex colors](../../claims/Yin_C_A0041_v1.md#a-finite-target-as-a-vertex-coloring) | Necessary and sufficient transport on all components and the one-side necessary condition. |
| [Whole-argument finding](#whole-argument-finding) | [Entropy loss](../../claims/Yin_C_A0041_v1.md#strict-entropy-loss) | Feasible histogram count, strictness for nontrivial target maps and uniformity in \(n\) for each fixed target. |
| [Whole-argument finding](#whole-argument-finding) | [Girth and realizations](../../claims/Yin_C_A0041_v1.md#girth-conditioning-and-the-torsion-free-realizations) | Subexponential girth cost, further conditioning, abelianization consequence and source interfaces. |
| [Whole-argument finding](#whole-argument-finding) | [Voltage cover](../../claims/Yin_C_A0041_v1.md#a-cyclic-voltage-cover-that-forces-torsion) | Exact order-seven obstruction and the trivial-cover alternative when all loop voltages vanish. |
| [Planted quotient finding](#planted-quotient-finding) | [Model](../../ledger/Yin_L_A0047_v1.md#a-different-choice-of-matchings) | Exact balance, admissible sizes, descended surjection, existence claims and scope of factorization through it. |
| [Planted quotient finding](#planted-quotient-finding) | [Switching and expansion](../../ledger/Yin_L_A0047_v1.md#girth-local-expansion-and-the-cost-of-a-matching-prescription) | Reverse repair count and the uniform conditional prescription estimate within the same block. |
| [Planted quotient finding](#planted-quotient-finding) | [Bounded-pattern transfer](../../ledger/Yin_L_A0047_v1.md#the-bounded-pattern-estimate-with-the-seven-colors) | Stage-count correction, turn weights, pattern enumeration and application of the deterministic source geometry. |
| [Planted quotient finding](#planted-quotient-finding) | [Connectedness and other targets](../../ledger/Yin_L_A0047_v1.md#connectedness-and-the-other-finite-quotients) | Additional markings, equality case, exclusion of macroscopic cuts and nonfactoring maps. |
| [Planted quotient finding](#planted-quotient-finding) | [Support counts](../../ledger/Yin_L_A0047_v1.md#occurrence-counts-and-the-actual-characteristic-two-supports) | Root shifts and inverse orientation, \(o(n)\) ambiguous vertices, exact occurrence histograms, parity and projected sign lift. |

## Whole-argument finding

Coning every graph component kills its closed-walk labels normally in the rose group.
For a fixed map from the rose group to \(Q\), triviality of all these loop images is precisely what makes colors obtained by path transport well defined on each component.
Conversely a product of increments fixing a color under the right regular action is the identity of \(Q\).
Restricting attention to one graph is sufficient for an upper probability bound.

For a feasible histogram, a fixed coloring allows exactly the product of the within-color factorials for each inverse-pair matching.
Distinct inverse pairs are independent before conditioning.
Counting vertex colorings by type and using the uniform factorial estimate gives the proposed exponent \(F_0-F_1\) and a polynomial factor for histograms.
Concavity bounds \(2F_1\) below by the degree-weighted type entropies, hence by \(129 F_0\).
Equality of the two exponents thus forces every type and label class to be monochromatic.
All types are linked by common ordinary projective-plane letters, so monochromaticity for every label class makes the whole side monochromatic.
Compatibility then forces every generator image to be the identity, ruling out equality on the feasible compact set for a nontrivial map.
The fixed alphabet gives finitely many assignments for each fixed target, and a finite list is enough for any fixed order bound.

The source's short-cycle count and same-inverse-pair switch apply to the stated independent uniform matching model.
Markov bounds the distance of at least half its tuples from the girth event by \(n^{\gamma'}\) switches, since a switch with a nonbad distant edge strictly reduces the bad-edge count.
The reverse neighborhoods have at most \(\exp(O(n^{\gamma'}\log n))=\exp(o(n))\) tuples, yielding the required lower bound on girth probability.
The later diameter and arrangement conditions cost a further factor tending to one.
The cone and zero-product conclusions here use [Ope26f, Propositions 4.5 and 5.1, Corollary 5.3 and §6](../../literature/pdf/Ope26f.pdf#page=18) within that source law.
The finite-generation argument for the abelianization excludes a free part and any seven-primary part when a \(C_7\) quotient is absent.
For the deterministic voltage cover, a closed base walk with nontrivial voltage lifts after seven repetitions, so its element has order dividing seven and its image has order exactly seven.
If all voltages of loops vanish, path transport trivializes the seven sheets on each component, which leaves the original normal subgroup of relations unchanged.

## Planted quotient finding

The divisibility requirement on \(n\) permits equal color counts within *each* full type on both sides.
Consequently every prescribed ordered color-label class has \(n\rho/7\) available vertices and its required inverse class on the opposite end of the same matching has that size.
Sampling independent block bijections gives a valid original matching tuple with the indicated voltage.
Every graph loop therefore maps to zero in \(C_7\), and the surjection already defined on the rose descends after coning.

The unconditioned cycle count replaces the target size \(n\rho\) by \(N=n\rho/7\), so the chosen smaller positive girth constant gives a sublinear expectation.
The repair switch removes one bad edge and adds no short cycle by the original distance argument if the second edge is distant, nonbad and in the **same** color block.
The constants ensure \(O(d_*^{2L+2})=o(n)\) excluded by distance, leaving order \(n\) choices.
The reverse-count proof again gives girth probability at least \(\exp(-o(n))\).
In the girth-conditioned switching experiment with \(s\) prescribed pairs, at most \(s\) more choices are forbidden.
The output identifies its predecessor once the extra pair is specified, exactly as in [Ope26f, Lemma 2.2](../../literature/pdf/Ope26f.pdf#page=5).
Iteration at \(E=O(L)\) gives \(N^{-E}\exp(o(L))\), uniformly in the feasible prescriptions.
For small-set expansion one may take \(\varepsilon\) so that \(r=\lceil129k/2\rceil\le N/3\).
Counting possible \(2k\)-sets and unordered edge prescriptions as in source Lemma 2.3 leaves \([C'(k/n)^{62.5}]^k\).
Its sum below \(\sqrt n\) tends to zero by the geometric bound with ratio \(O(n^{-31.25})\), and above \(\sqrt n\) by decreasing \(\varepsilon\).
This gives the needed doubling and the geodesic packing diameter bound.

The extra factor \(7^{E_j}\) in the conditional cost is potentially exponential in the source length \(L\).
For a fixed stage label assignment, compatible colors on \(\Delta_j\) are determined by one starting color per component, or do not exist.
In [Ope26f, (3.10), pp. 12–13](../../literature/pdf/Ope26f.pdf#page=12), all \(V_j-k_j\) unfixed stage vertex counts, both internal turn counts and ordinary upper bounds, are divided by seven for a prescribed color.
This follows from the exact type balance before vertex images are required to be injective.
The prescribed root still costs at most one choice, regardless of its name and color.
The combined factor is therefore at most \(7^{b_j+E_j-V_j+k_j}\).
Its exponent is the first Betti number of the stage graph plus \(k_j\le1\), bounded by the source's bounded cycle rank for the full image graph.
Thus it adds only \(O_{K,C,I}(1)\) to the exponent.
The permitted stage strings are bounded by the original count (3.11), since ignoring colors enlarges their set and the within-color turn weights obey the same bounds.
The number of stages is bounded for fixed \(K,C,I\), so multiplying the numerical stage expectation bounds still gives the exponential saving in (3.12) needed for summing enlarged patterns.
No independence across stages or after girth conditioning is used.
The source's subsequent deterministic choice of a single fixed triple of pattern constants and its cone-picture arguments then apply to the planted tuple.
This review checks the change of law and its interfaces, using the source pattern combinatorics and deterministic topological theorems at their stated scope.

The type-color first moment for an additional marking has the same entropy gap, now conditional on each planted color.
Equality makes the additional symbol a function \(f(c)\) of just the planted color because types at a fixed color share ordinary letters.
For a cut the function is constant by surjectivity of \(\eta\), excluding equality at cut densities in \([\varepsilon,1/2]\).
This excludes large disconnected components with exponentially high probability; small components are already excluded by expansion.
For an additional group target, iteration of the compatibility condition forces \(f(c)=f(c)\theta(W)\) for every \(W\in\ker\eta\), so all zero-loss maps factor through the planted quotient.
The finite union and the subexponential conditioning cost preserve the exclusion of other specified finite targets.

On connected sides the two prescribed roots see exactly \(n/7\) occurrences of each color, since root translation and negation on the second side permute colors.
The same bounds on a stage realization for any predetermined root give uniform \(o(1)\) failure of separation from all other vertices at that root.
Summing these probabilities over vertices and using Markov bounds the number of ambiguous vertices by \(o(n)\) in probability.
Removing them while passing to collected supports leaves \(n/7-o(n)\) to \(n/7\) distinct group labels in every color, and each count has the parity of \(n/7\), which is even.
The exact occurrence product count \(n^2/7\) per class precedes collection.
Convolution of the two surviving support histograms gives \(n^2/7-o(n^2)\) cells per quotient class and a multiple of four.
Pairing opposite signs in each occupied class gives the claimed integral solution of the projected equations on the surviving occurrence indices.
The planted family realizes a genuine quotient and the source's characteristic-two product in torsion-free groups, while those integral signs solve only the quotient equations.

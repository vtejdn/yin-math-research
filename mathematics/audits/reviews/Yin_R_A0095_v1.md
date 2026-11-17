---
author: Yin
---

# Free subgroups and prescribed path languages in the matching models

At 2026-11-17T02:20 UTC an agent outside the development of Yin_C_A0059_v1 independently reviewed the fixed statement and all four proof sections for Sheng Yin.
The reviewer had previously checked the four-line matching and the free-outer-disk interface.
The present review checked the new restricted-word count, geometric localization, subgroup metric, explicit bounds and immersed-graph extension without receiving development dialogue, author explanations or prior findings about this argument.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0059_v1.md#statement) | Simultaneous inverse-closed subalphabets, unrestricted word length, metric comparison, explicit thresholds, fixed language and the separate model events. |
| [Whole-argument finding](#whole-argument-finding) | [Bounded systems](../../claims/Yin_C_A0059_v1.md#bounded-path-systems-with-some-comparisons-replaced-by-an-alphabet-restriction) | First- and second-power word counts, distinguished and unrestricted occurrences, all link-component cases, stage selection and colored embedding. |
| [Whole-argument finding](#whole-argument-finding) | [Capped pictures](../../claims/Yin_C_A0059_v1.md#capped-pictures-with-an-outer-segment-in-the-chosen-letters) | Exterior contacts, interval and separator bounds, extraction of an excluded cluster, injectivity, and recovery of the metric bound after reduction. |
| [Whole-argument finding](#whole-argument-finding) | [Letter thresholds](../../claims/Yin_C_A0059_v1.md#which-choices-of-letters-are-covered) | Turn sums for the mixed letters, rational positive test vectors, submatrices, endpoint distinctions and convolution on cosets. |
| [Whole-argument finding](#whole-argument-finding) | [Fixed turn graph](../../claims/Yin_C_A0059_v1.md#a-fixed-finite-graph-of-permitted-turns) | Counting paths with multiplicity, subwords and reversal, the cut for a wholly readable boundary, metric comparison and fixed-before-sampling quantifiers. |
| [Whole-argument finding](#whole-argument-finding) | [Four-line matching law](../../claims/Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts) | Girth conditioning, uniform matching-block cost, positive refined turn counts and finite-color propagation. |
| [Whole-argument finding](#whole-argument-finding) | [Fine matching laws](../../ledger/Yin_L_A0053_v1.md#matching-safeguards-and-the-relative-mod-two-quotient) | Fixed finite-color stage corrections at the scales of the refined models. |
| [Whole-argument finding](#whole-argument-finding) | [Fourteen-color quotient exclusion](../../claims/Yin_C_A0054_v1.md#excluding-all-orders-with-prescribed-simple-composition-factors) | The event excluding an order-21 quotient over the prescribed \(C_7\) in the indicated exceptional law. |

## Whole-argument finding

For spectral radius below one, summing positive word weights on the restricted alphabet gives exponential decay in length, including when the restriction has only finitely many positive-weight words.
For length \(s+O(1)\) each positive word in bin \(d\) has weight greater than \(e^{-d-1}\), giving the stated first-power bin saving.
The additional distinguished endpoints introduce boundedly many cuts for fixed pattern parameters.
Away from cuts, each unmatched full-block occurrence is either restricted throughout or costs its length in unrestricted positions.
The exceptional charge \(O(s+L/s)\) is \(o(L)\) under the source's grid choice.

In a link component with \(2z>S_U\), one restricted occurrence of a multiplicity-\(z\) block constrains its underlying word at all \(z\) active stages, including stages at which some linked blocks are absent.
The counting takes projections of complete admissible *word assignments* and does not require extending a partial graph embedding.
The restricted-root cost \(z(d_{i_*}-\xi's)\) cancels its \(zd_{i_*}\) embedding term and retains the other blocks' negative bin costs.
Without a self-link or such a restriction, at least \(2z-S_U\) occurrences of that block lack distinct partners on other blocks and are charged to the bad budget.
The self-link and \(2z\le S_U\) cases keep their original negative exponent.
Thus the numerical product of the stage bounds retains a definite saving per unit length after the unrestricted budget is made small.
One small stage and a subexponential union bound suffice, with no independence between the stages.
I checked these interfaces against [Ope26f, (3.5)–(3.12), pp. 9–14](../../literature/pdf/Ope26f.pdf#page=9).

The embedding probability on each fixed finite-color model is changed by the propagated color choice per stage component, the saving per unprescribed vertex and the loss per edge.
The combined color factor is bounded because the stages consist of boundedly many whole chains.
The bounded changes of positive type counts add \(\exp(o(L))\), while prohibited turns remain absent.
The proof first fixes the turn-dependent unrestricted fraction, then the finite pattern bounds and finally the size.
The number of subalphabets is fixed across sizes, so the simultaneous statement follows by a finite union, and intersection with the fourteen-color quotient exclusion preserves conditional probability tending to one.

For the disk step each split inner piece has at least \(L\) original positions, hence \(k'\le H/L\).
Cutting the exterior into at most two pieces leaves at most \(6(k'+2)\le18H/L\) interval pairs.
Every surviving graph-to-restricted-exterior interval retains a word on the chosen letters, and graph-to-graph intervals keep the distinct-edge condition.
Closures, deleted partners and contacts with the arbitrary segment account for all unrestricted positions.
The two exclusion budgets consume at most \(H/16+v/\varepsilon\) and \(H/16\) of retained cluster length.
At \(v\le\varepsilon H/8\) their sum is strictly below \(15H/16\), leaving a forbidden cluster at the previously fixed bounds.
I checked the source's free minimal picture, interval lemma, closure and separator constants at the points used here. [Mghirbi and Douglas, §§3.4–4.3](../../literature/pdf/MD26.pdf#page=13)

For \(v=0\) this rules out all nonempty cyclically reduced null words on the selected letters.
An arc joining two occurrences of the surviving restricted segment cuts off a subpicture on the side avoiding the arbitrary segment.
Its intervening word is trivial, while a nonempty reduced restricted subword survives by injectivity, and an empty one would require adjacent inverse letters.
Thus each surviving restricted occurrence uses an inner or arbitrary occurrence, giving the metric bound after restoring the equal number of letters trimmed from the two reduced segments.
If a segment disappears during trimming, either the original restricted length was already no larger than the comparison length or the remaining restricted word must be empty by injectivity.
The coset decomposition restricts regular convolution to copies of the free-subgroup representation and preserves the canonical trace.

The three row-sum types account separately for ordinary letters with ordinary inverse, ordinary letters with extra inverse, and extra letters.
For each displayed positive vector \(v\), I evaluated \(v-Mv\) with common denominator \(129\cdot16513\).
The minima of its three numerators are \(167700,\ 1755819,\ 2247327\), respectively, for the three ordered cases in the claim.
The strict weighted norm bounds extend to principal submatrices.
With no mixed pair the maximum row sum at 64 ordinary pairs is \(127/129\).
These computations verify both thresholds as sufficient conditions.

For a fixed finite immersed graph every readable reduced word has a nonbacktracking lift, and summing over paths only overcounts its nonnegative weight.
At spectral radius below one this yields the same bin saving.
Readability is preserved under reversal and trimming either end, and marking the linear start even on a wholly readable exterior keeps contact intervals inside actual readable words.
The disk and metric conclusions therefore also hold for all readable words and for based reduced loops in each chosen component.
The probability statement extends to a preassigned finite list of immersed graphs.
It gives no sampling-uniform assertion for a turn graph chosen from a realized relation and no conclusion for subalphabets of spectral radius at least one.

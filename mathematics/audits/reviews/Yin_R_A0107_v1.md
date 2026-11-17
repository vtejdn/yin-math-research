---
author: Yin
---

# Distinct original labels on paths with identical six-vertex pairing signatures

At 2026-11-17T03:52 UTC an agent outside the development of Yin_C_A0071_v1 independently reviewed its statement and three proof sections for Sheng Yin.
The reviewer previously inspected the marked systole argument, the mixed tensor and the common-complement matching lemma.
No development dialogue, author explanation or previous finding on C71 was supplied.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0071_v1.md#statement) | Within-path separation, equal internal signatures, all fixed fine states, selected and raw coincidence probabilities, and the separate full-matching hypothesis. |
| [Whole-argument finding](#whole-argument-finding) | [Short words](../../claims/Yin_C_A0071_v1.md#short-words-separating-original-labels) | Pattern-free hypotheses, order of choosing \(c_0,c_*,\lambda\), injectivity on the short ball and separation from inverses. |
| [Whole-argument finding](#whole-argument-finding) | [Two blocks](../../claims/Yin_C_A0071_v1.md#constructing-both-blocks-in-one-matching-law) | Choice of neutral alphabets, disjoint open lifts, conditioning losses, simultaneous C65 safeguards, true labels and the mixed rank-one tensor. |
| [Whole-argument finding](#whole-argument-finding) | [Choosing blocks](../../claims/Yin_C_A0071_v1.md#choosing-blocks-with-small-coincidence-probability) | Multiplicities of undirected label pairs, Hall capacities, heavy-atom estimate and the sampling space for both bounds. |
| [Whole-argument finding](#whole-argument-finding) | [Geometric input](../../claims/Yin_C_A0065_v1.md#safeguarded-realizations) | Nonregular state sizes and transfer of girth, diameter and bounded-pattern estimates for this same matching law. |
| [Whole-argument finding](#whole-argument-finding) | [Systole input](../../ledger/Yin_L_A0054_v1.md#the-geometric-input-and-its-application-to-the-planted-laws) | Free-boundary length bound for a fixed pattern-free tuple. |
| [Whole-argument finding](#whole-argument-finding) | [Mixed tensor](../../claims/Yin_C_A0066_v1.md#a-grid-of-actual-commutators-in-a-four-line-tuple) | Based commutator with both translated cycle classes at coarse index three. |
| [Whole-argument finding](#whole-argument-finding) | [Matching extension](../../claims/Yin_C_A0070_v1.md#extending-witnessed-matchings-on-even-blocks) | One common complementary matching conditional on a full matching of the color. |

## Whole-argument finding

After the trial exponent \(a\) is fixed, one can select a positive \(c_0\) meeting the girth conditions for both C65 and the trial estimates.
For that choice, the degree, component diameter and vertex-count bounds together with the rooted pattern exclusion supply the fixed triple in Definition 3.3 of Mghirbi and Douglas.
Proposition 4.4 then gives a positive marked systole constant \(c_*=13\varepsilon/16\), since a reduced free-boundary filling of a nonempty cyclically reduced null word must use at least one inner graph loop of length at least \(L\).
Only after fixing these constants does the proof choose \(\lambda\).
The bound \(2\ell<c_*L\) eventually holds even with the floor in \(L\).
Consequently two words of length at most \(\ell\) with the same group image were freely equal, by cyclic reduction of their difference.
Positive words in the two distinct generators are pairwise distinct and cannot equal the identity or one another's inverses.
This short-ball event covers any admissible choice made from the end letters of the neutral cycles.

The neutral cycle searches take place at the designated zero state, while all sampling of the two-block words on the left uses neutral pools internal to states above \(3\).
Before girth conditioning these pools are still uniform after the cycles and alphabet have been chosen from the zero-state data.
The spacer makes \(W\) cyclically reduced, and excluding both end-letter pairs of \(W\) from the connector alphabet protects both splices of \(W^5uW^5\).
For its length bound \(H\), the number of available trials per word times \(300^{-H}\) exceeds \(n^{1-\delta/2}\).
Indeed \(b+80a\log(300)/\log64<0.055\delta\), and \(\lambda(\log2+\log300)<\delta/8\).
Marking failures as well as successes keeps the paths disjoint within the fixed exposure budget.
The union bound over \(D\) words and the fixed number of states preserves the required failure exponent, and the cost of girth conditioning has logarithm \(O(n^{3a/8}\log n)\), absorbed already by the slower cycle failure exponent \(n^{a/2}\).
Thus the needed paths and the stated geometric, coarse-kernel and relator-index conclusions hold together on one conditioned tuple.

The positive connector length and simplicity give twelve distinct marks on each path.
All six original labels within a half agree, as the repeated word is a cone relation, while crossing the connector multiplies the actual label on the right by a nonidentity group element.
The connector has trivial fine-state increment.
In both halves the same two cycle classes enter at coarse index \(3\), even though their actual base labels can differ.
Every internal displacement is a product of conjugates of full-relation-subgroup commutators and vanishes in its ordinary abelianization.
Three odd endpoint indices among the six give total tensor \(T_0\) for each of the fifteen matchings.
Simplicity makes each of the two defining binary cycle classes nonzero, so \(T_0\) has rank one.
If a full true matching exists, the even blocks can all be matched internally using a common complementary matching.
No equality edge can join the two halves of the same path.

For a fixed fine state and realized tuple, a label pair determines its connector value up to inversion.
Short-ball injectivity, positivity and the choice of exactly \(h\) paths per connector bound the edge multiplicity by \(h\).
There are no loops.
For \(s\) labels the number of internal edges is at most \(h\min(D,\binom{s}{2})\le hs\sqrt{D/2}\).
Every subset of rows with these \(s\) endpoints therefore has enough neighboring slots at capacity \(\lceil h\sqrt{D/2}\rceil\), as required by [Hall's theorem](../../literature/pdf/Hal35.pdf#page=1).
Assigning one endpoint to each row bounds the largest chosen-label mass by the claimed ratio, and the sum of squared masses is no larger.
With both endpoints retained, each row contributes at most one incidence to any single atom.
The total mass on \(s\) atoms is at most \(1/2+\binom{s}{2}/(2D)\), counting an extra incidence only on edges internal to those atoms.
With \(s=\lfloor D^{1/3}\rfloor\), the heavy atoms contribute at most half that bound to the sum of squares, and all remaining atoms contribute at most \(1/(s+1)\).
This yields the unselected \(1/4+O(D^{-1/3})\) estimate.

Both coincidence bounds use independent uniform sampling of blocks with replacement on the fixed realized tuple.
The proof requires separation of the two labels of each path and the stated pair multiplicity control, and it allows repeated labels across different paths.

---
author: Yin
---
# Independent review of sparse-alphabet probability certificates

## Inputs and arrangement

At 2026-11-21T04:43 UTC an agent outside the development of L_A0064_v1 completed a review of all six sections for Yin.
The reviewer received the saved ledger and the scope of the assignment, with no development discussion or prior verdict on this ledger.
The reviewer consulted C_A0091, C_A0092 and the earlier review of C_A0092 for the input hypotheses and the direction of the probability comparison.
The earlier claims enter at their stated conclusions.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Alphabet law](../../ledger/Yin_L_A0064_v1.md#scope-and-the-exact-alphabet-law) | Fixed-tuple sampling, the complete covering family and the implication for color erasure. |
| [Whole finding](#whole-finding) | [Forest and common cores](../../ledger/Yin_L_A0064_v1.md#a-forest-bound-and-common-core-caps) | Induced-forest inequality, choice of edges, clustering and exact shared-pair example. |
| [Whole finding](#whole-finding) | [Sliding triples](../../ledger/Yin_L_A0064_v1.md#a-strict-improvement-at-the-required-threshold) | Path bound, simple union bound, binary-run recurrence and exact probability comparison. |
| [Whole finding](#whole-finding) | [Fractional covers](../../ledger/Yin_L_A0064_v1.md#fractional-covers-by-contained-cores) | Pointwise fractional core certificate, pair-weight threshold, first moment and weighted tail. |
| [Whole finding](#whole-finding) | [Row bases](../../ledger/Yin_L_A0064_v1.md#a-grouped-row-basis-certificate) | Neutral restriction, direct sum, injectivity, disjoint label blocks and their three numerical thresholds. |
| [Whole finding](#whole-finding) | [Restrictions and realizations](../../ledger/Yin_L_A0064_v1.md#necessary-restrictions-and-the-limits-of-local-contact-tests) | Both lower bounds, the two triangular presentations, the lift and signs of the four cycles, and limits for original tuples. |
| [Whole finding](#whole-finding) | [C92 statement](../../claims/Yin_C_A0092_v1.md#statement) | Covering list, neutral minimal supports and the upper event in assertion 4. |
| [Whole finding](#whole-finding) | [C91 statement](../../claims/Yin_C_A0091_v1.md#statement) | Strict lower probability under erasure for the same fixed tuple and alphabet draw. |

## Whole finding

The conditional bounds and both geometric examples hold at the scopes stated in the saved ledger.
For a fixed tuple satisfying C92's hypotheses, the certificates bound the probability that at least one covering configuration has a nonzero output supported on the sampled alphabet.
An upper bound of \(1/4000\) for that event contradicts C91 under full color erasure.
A lower bound for the same event gives no converse about regular rank.

For each draw the forest expression counts the components of the marked subforest, so it dominates the indicator of a nonempty marked set.
Conditioning on a common pair leaves \(s-2\) uniform choices from \(D-2\) labels, giving (6).
Every realized support contributes covered core weight at least one under (9).
For the alternative integer-weight bound, choosing one summand from each factor records one subset with its exact size and weight.
For disjoint nonempty feasible sets \(A,B\), conditioning on \(A\subseteq S\) replaces the successive factors \((s-j)/(D-j)\) for sampling \(B\) by the strictly smaller \((s-|A|-j)/(D-|A|-j)\) whenever their union fits.
If only the two sets individually fit, their joint probability can be zero while both individual probabilities are positive.

I independently checked the exact comparisons in (7), (8), (11), (13), (14) and (15) using binomial coefficients and integer arithmetic.
For a separate derivation of (8), a valid string of length 621 with \(k\) ones in \(r\) runs has \(k-r\) double runs.
The number of such strings is \(\binom r{k-r}\binom{622-k}{r}\), since the runs occupy distinct gaps among the zeros.
Summing over \(r,k\), weighting by \(\binom{7631}{62-k}\) for the inactive labels, dividing by \(\binom{8252}{62}\) and taking the complement gives probability approximately \(0.000248247806468378\).
This is below the forest upper bound \(619q_3-618q_4\), which is itself below \(1/4000\).
Both the simple union bound for this family and the Bonferroni lower bound for the 619 disjoint triples exceed \(1/4000\).
Five distinct pair supports also exceed that threshold by the stated lower bound.

The coordinate copies in the direct sum stay distinct even when labels agree across configurations.
A nonzero supported vector has a nonzero supported component in some configuration, proving the claimed equivalence.
Each full-rank block must meet the sampled alphabet on that event.
Inclusion-exclusion gives the probability of meeting all blocks, and a choice of one label per disjoint block gives the second bound in (13).
The calculation uses a rank test on the entire direct sum.

In the two presentations each \(a_i\) is a free face of its own triangular cell.
Collapsing those cells leaves a rose, which proves asphericity and freeness.
For the disjoint triples, all three edge labels of a triangle occur in every nonzero scalar multiple of its cycle, and no other selected triangle uses any of them.
For the four-triangle presentation, the eliminated generator is \(a_i=c_{i+1}c_i^{-1}\).
Right multiplication takes \(x_i\) along \(a_i\) to \(x_{i-1}\) and along \(c_i\) from there to \(c_1\).
With all spokes oriented toward \(c_1\), the coefficient on the \(c_i\) spoke is \(\lambda_i-\lambda_{i-1}\).
Thus all four coefficients agree when every outside edge cancels, and omitting any triangle forces every coefficient to vanish.
The sum with all coefficients one retains the four distinct \(a_i\) edges.

The triangle examples establish these phenomena for the indicated selected lifted cones in aspherical presentations with free groups.
Their girth is three.
The sliding triples are an abstract support family.
The original four-line population and pattern hypotheses still have to supply a bound for their own complete covering family before these certificates can exclude erasure there.

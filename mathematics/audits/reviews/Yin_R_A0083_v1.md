---
author: Yin
---

# Deciding erasure on a supplied four-line matching

At 2026-11-17T01:34 UTC an agent outside the development of Yin_C_A0052_v1 independently reviewed its statement and all three proof sections for Sheng Yin.
The reviewer received the fixed claim and its direct inputs, with no development dialogue, proposed proof summary, author explanations or earlier findings on this claim.
The reviewer had independently reviewed the four-line matching law used as a hypothesis.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0052_v1.md#statement) | Decision and certificates for the six lists, the original supports and their product fibers, fixed comparison parameters and the four-line event. |
| [Whole-argument finding](#whole-argument-finding) | [Certificate bound](../../claims/Yin_C_A0052_v1.md#bounded-certificates-in-the-cone-presentation) | Comparison words, cyclic reduction, total cone length, girth and number of disks. |
| [Whole-argument finding](#whole-argument-finding) | [Witness enumeration](../../claims/Yin_C_A0052_v1.md#enumerating-the-witnesses) | Walk counts, connected picture, both directions of the tree-splicing test and polynomial running time. |
| [Whole-argument finding](#whole-argument-finding) | [Six classes and products](../../claims/Yin_C_A0052_v1.md#from-one-even-color-to-both-factors) | Independent pairings in the fixed group, exhaustive product comparisons and verification of the geometric input conditions. |
| [Whole-argument finding](#whole-argument-finding) | [Four-line matchings](../../claims/Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings) | Color homomorphism, admissible sizes and the reflected second factor. |
| [Whole-argument finding](#whole-argument-finding) | [Four-line geometry](../../claims/Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts) | Diameter and single-rooted-interval pattern estimates at fixed bounds after logarithmic girth conditioning. |

## Whole-argument finding

For a same-side comparison the shortest connecting path represents the quotient of the two forward labels, and inversion preserves equality on the second side.
Free reduction and conjugation preserve triviality, including the case of an empty reduced word.
For a nonempty cyclically reduced null word of length \(m\), the free outer boundary gives a reduced picture whose *sum of inner walk lengths* is at most \(16m/(13\varepsilon)\).
This is the quantity needed to enumerate the boundary words.
Each reduced inner walk has length at least \(L\), so for \(m\le dL\) the number of disks is bounded independently of \(n\).
I checked the statement about free outer boundaries, the reducedness conditions and the direction of the length bound in [Mghirbi and Douglas, arXiv:2611.04599v1, Lemmas 4.2–4.3 and Proposition 4.4](https://arxiv.org/html/2611.04599v1#S4.SS3).
The geometric estimate is an external input here.

Discarding incidence components disjoint from the outer disk preserves every pairing among the remaining occurrences.
For a connected picture with \(k\) inner disks, a spanning tree chooses \(k\) disjoint pairs of inverse-letter occurrences between disks.
Thickening its bands yields one disk with the concatenated, spliced cyclic boundary.
In its complementary disk the remaining arcs give a noncrossing inverse-letter matching, equivalent to free triviality by removing innermost pairs.
Conversely the prescribed tree of oriented disks and bands can be realized as a disk with that cyclic order, and a free reduction draws the remaining matching in its complement.
The reconstructed picture gives a proof from the given closed walks even if it is unreduced.
Those walks belong to the normal closure of the fundamental loops of the original graphs.

For bounded \(k\) the walks have at most \((2n)^k\) choices of starts, a polynomial in \(L\) choices of lengths and at most \(132^{O(L)}\) choices of traversals in total.
The \(O(L)\) named occurrences give at most \(O(L)^{2k}\) ordered choices of the tree endpoint pairs, with a linear free reduction per spliced word.
These bounds are polynomial in \(n\) when \(L=O(\log n)\) and the geometric parameters and alphabet are fixed.
They cover all witnesses promised by the length bound, so exhaustive failure separates unequal labels.
Up to \(n^4\) comparisons of words of length at most \(4dL\) still have polynomial cost and identify all original product fibers.

The character separates different quotient colors, and pairing inside an equality class removes all its terms precisely when its multiplicity is even.
Reflection changes the three even colors on the second side to \(\{1,2,4\}\).
Choices of witnesses for one list leave the presentation and the other lists fixed.
Thus six independent multiplicity tests in the same group give the asserted joint-extension decision.

For the geometric test the size bound \(\log_2(2n)\le\lambda L\) holds for all sufficiently large \(n\) after choosing a fixed \(\lambda>1/(c_0\log 2)\).
With integer cutoffs and rational comparison data one can check this inequality, the degree, girth and diameter bounds, and enumerate all bounded path systems with their intervals, comparison orientations and distinct-edge conditions.
Their total length is \(O(L)\), and the numbers of paths and interval pairs are fixed, giving polynomial cost also for verifying exclusion.
The transferred probability assertion uses the four-line law's diameter constant and admissible unpaired fraction, followed by the fixed bounds of [Definition 3.3](https://arxiv.org/html/2611.04599v1#S3.SS2).
The geometric test and the word decisions are deterministic for every matching satisfying these hypotheses, regardless of how it was selected.

The argument supports the stated polynomial-time procedure on the explicit tuple and the high-probability qualification for the indicated law.
No instance was supplied or run in this review, and the decision for a specified matching leaves open existence of a matching with simultaneous erasure across sizes.

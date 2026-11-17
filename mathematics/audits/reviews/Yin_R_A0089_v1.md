---
author: Yin
---

# Disjoint open lifts of an opposite-side cycle in the four-line laws

A separate reviewing agent inspected the fixed C_A0053_v1 for Yin on 2026-11-17T01:49 UTC.
The reviewer had previously developed the 21- and 28-color refinements in L_A0053 and other relevant matching inputs.
The reviewer did not develop the new cycle search, copy count or conditioning comparison and received no development dialogue, explanation of this proof or prior verdict before inspecting the fixed Claim.
This review checks the existing histogram and safeguard inputs at the scope of their use here.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0053_v1.md#statement) | Both sides, all fine bins over three forward colors, specified fixed and variable girth constants, and original-group disjoint pairs. |
| [Whole-argument finding](#whole-argument-finding) | [Unconditioned exposure law](../../claims/Yin_C_A0053_v1.md#the-unconditioned-exposure-law) | Usable signed stubs, exact ordinary-line intersections, historical exclusions and uniform positive turn probability. |
| [Whole-argument finding](#whole-argument-finding) | [Short closed word](../../claims/Yin_C_A0053_v1.md#finding-a-short-closed-word-on-one-side) | Tree construction, abort probability, distinct inverse-pair connectors, cycle simplicity, exposure budget and exponential failure. |
| [Whole-argument finding](#whole-argument-finding) | [Disjoint open paths](../../claims/Yin_C_A0053_v1.md#reading-the-same-word-on-disjoint-open-paths) | Independence of the selected word from the opposite-side matchings, conditional success, vertex disjointness and all-bin intersection. |
| [Whole-argument finding](#whole-argument-finding) | [Conditioning](../../claims/Yin_C_A0053_v1.md#conditioning-and-what-is-paired) | Comparison with quantitative girth-event cost, geometric safeguards, connectivity, actual cone relations and remaining unpaired labels. |
| [Whole-argument finding](#whole-argument-finding) | [Exponents near one](../../claims/Yin_C_A0053_v1.md#exponents-arbitrarily-close-to-one) | Budget, root and connector bounds, mean count, dependence on fixed \(\delta\), and dominance over girth-conditioning costs. |
| [Whole-argument finding](#whole-argument-finding) | [Four-line type data](../../claims/Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings) | Active pairs, prescribed totals, bounded changes per block and type. |
| [Whole-argument finding](#whole-argument-finding) | [Four-line switching proof](../../claims/Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts) | Short-cycle upper bound and reverse switch neighborhood sufficient for the quantitative conditional comparison. |
| [Whole-argument finding](#whole-argument-finding) | [Order-28 data](../../ledger/Yin_L_A0053_v1.md#exact-refinement-with-two-binary-coordinates) | Coarse and fine increments, unchanged usable-letter pairs and positive bin frequencies. |
| [Whole-argument finding](#whole-argument-finding) | [Refined safeguards](../../ledger/Yin_L_A0053_v1.md#matching-safeguards-and-the-relative-mod-two-quotient) | Independent uniform block law and passage to connected torsion-free tuples. |
| [Whole-argument finding](#whole-argument-finding) | [Order-21 variant](../../ledger/Yin_L_A0053_v1.md#a-smaller-quotient-of-odd-order-even-when-the-relative-mod-two-test-is-trivial) | Three fine coordinates, same usable ordinary labels and the relevant surviving odd subbins. |

## Whole-argument finding

At most nine ordinary points are excluded from any line for this purpose, so 120 usable signed stubs is a valid uniform lower bound in all three laws.
Distinct usable points specify a unique line and therefore \(n/(dv)+O(1)\) candidate vertices of the specified color among \(np/d+O(1)\) possible partners.
This ratio tends to \(1/129\), leaving the claimed \(1/300\) bound after removing a sublinear number of touched vertices.
The still-unmatched bijection in a block is uniform conditional on an adaptive exposure history, provided the next stub choice uses only that history and the fixed type data.
A vertex outside the touched set has no exposed matching stub, so a fresh partner carrying the next required letter really does leave that stub available.

While the tree grows, revealing a new edge to its own current tree closes a simple cycle consisting of that edge and the unique tree path.
Immersion makes its word cyclically reduced, including the possible one- and two-edge cycles before girth conditioning.
Otherwise arriving at an already touched external vertex counts as a failed child choice.
At least 37 such failures are needed to abort a growing internal vertex, since it needs only 64 successes in 100 trials and has at least 119 free usable stubs after arrival.
Conditional multiplicative bounds summed over the possible locations of those 37 failures justify the error estimate without independent exploration steps.

At completed leaves, a common ordered pair of usable labels in distinct inverse pairs occurs on a fixed positive fraction by the finite alphabet.
The two disjoint sublists prevent a two-edge connector from returning to its own leaf.
Exposures from the first sublist that reach fresh designated partners have a uniformly positive conditional probability, and an earlier tree hit already gives a cycle.
The selected \(\bar s\) stubs are unused and remain available on failure of previous second-sublist attempts: first-sublist exposures use a different matching, and failures in the second sublist do not touch those designated stubs.
The second-stage probability of success in an otherwise complete tree is therefore \(\Omega(M^2/n)\), and the two tree branches and connector give cycle length at most \(2R+2\).
One needs only that the probability of a completed tree or an early cycle tends to one, because an early cycle is already a success.
There is no subtraction of an abort probability from the small connector success probability.

The initial cycle trials spend at most \(O(n^{15/16})\) exposures and yield total failure at most \(\exp(-\Omega(n^{3/16}))\).
The selected cycle word depends only on one unconditioned side.
For any such word of length \(h\), each disjoint open-path attempt on the opposite side therefore succeeds with conditional probability at least \(300^{-h}\).
Bernoulli domination of the successive indicators is valid from these conditional lower bounds.
All failed attempts are included in the touched set, so successful paths have disjoint vertices and distinct endpoints.
The quantity \(15/16-\log(300)/(2\log(64))\) is approximately \(0.251765\), leaving room for the logarithmic trial-length denominator and the \(n^{0.24}\) mean used for the \(n^{1/5}\) conclusion.
A finite union of the marginal estimates covers each fine bin and both choices of side without claiming reverse-search independence.

At \(c_0=1/1000\) the values of \(c_0\log(2d|T|/p)\) for \(d=7,21,28\) are at most \(0.018590\).
Markov's inequality and the reverse switch count thus give a conditioning divisor no smaller than \(\exp(-O(n^{0.05}\log n))\), which preserves the unconditional stretched-exponential success.
The event is existence of the words and disjoint paths in the sampled graphs; when restricting it to girth-\(\ge L\) graphs, every witnessing cycle automatically has length at least \(L\).
The further high-probability connectivity and safeguards events are imposed only after this comparison.
The reference root on each side is outside the designated bins.
After coning, a word read round a cycle is the identity in the **original** group, so its path between the two open endpoints proves equality of their root labels on the same connected side, also after the inverse-label convention.

For the variable exponent the cycle search spends \(O(n^{1-b})\) exposures and has abort error \(O(n^{a-37b})=o(1)\) per trial.
Its number of trials times the per-trial cycle probability has order \(n^{a-b}\).
For the path search the exponent lost from one, apart from a vanishing error, is \(b+2a\log(300)/\log(64)\), approximately \(0.405367\delta<\delta/2\).
The resulting lower-tail bound and the cycle failure exponent \(a-b=a/2\) dominate the conditioning cost \(O(n^{3a/8}\log n)\) in the logarithm for each fixed \(\delta>0\).
This proves the stronger statement with a \(\delta\)-dependent girth scale.

The complete Claim holds on the three specified laws.
The result counts disjoint vertex pairs, which can share a group label across different pairs.
It is compatible with a sublinear number of repeated vertices and with the odd refined subcounts protecting the designated coarse colors from complete erasure.
It supplies neither a positive limiting paired fraction nor a vanishing complex product.

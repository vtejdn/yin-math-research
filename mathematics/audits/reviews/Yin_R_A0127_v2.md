---
author: Yin
---

# Independent review of the probability of short sparse relations after erasure

At 2026-11-21T06:36 UTC a reviewer outside the development of Yin_C_A0091_v2 checked its full statement and argument for Sheng Yin.
The reviewer received the target and its numerical scope, read the proof and its dependencies directly, and used the earlier review of v1 for the scope of the existing trace and homology identifications.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0091_v2.md#statement) | Strict fixed-tuple probability, simultaneous traces on the sampled marking, and avoidance of any fourteen prescribed types. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0091_v2.md#argument) | Neutral degree, surplus, extremal truncated expectation, conditional sampling and complete-cover consequences. |
| [Whole finding](#whole-finding) | [Four-line populations](../../claims/Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings) | Four selected lines, neutral inverse pairing and the coarse private-point counts. |
| [Whole finding](#whole-finding) | [Incidence estimate](../../claims/Yin_C_A0085_v1.md#projective-incidence-at-an-individual-group-element) | Even incidence vectors of weight 256 and their classification as differences of two lines. |
| [Whole finding](#whole-finding) | [Neutral degree](../../claims/Yin_C_A0085_v1.md#the-neutral-degrees-on-the-four-lines) | At most seven removed points at weight 256, inverse matching of endpoints and a nonempty odd-stub graph. |
| [Whole finding](#whole-finding) | [Short pivot cycles](../../claims/Yin_C_A0091_v1.md#argument) | Deterministic consequence of the stated surplus, including the cycle cutoff and number of independent chains. |
| [Whole finding](#whole-finding) | [Finite edge compression](../../claims/Yin_C_A0091_v1.md#compression-to-the-finite-edge-set) | Unnormalized traces, finite group-ring matrix and first Betti number for an infinite subgroup. |
| [Whole finding](#whole-finding) | [Earlier finding](Yin_R_A0127_v1.md#whole-argument-finding) | Existing review of the deterministic projection and homology arguments used from v1. |
| [Whole finding](#whole-finding) | [Bounded cone cover](../../claims/Yin_C_A0092_v1.md#the-number-of-cones-required-at-the-c_a0091-scale) | One covering list for the cutoff, chosen on the fixed tuple before sampling. |
| [Whole finding](#whole-finding) | [Minimal supports](../../claims/Yin_C_A0092_v1.md#exact-alphabet-probabilities-and-a-usable-conditional-threshold) | Implication from nonzero short-relation rank to the presence of a covered support, and the probability of containing a prescribed support. |

## Whole finding

Under the specified four-line counts and full erasure of the chosen forward color, the probability that a uniformly sampled 62-pair alphabet satisfies both trace inequalities strictly exceeds \(\rho=0.04283973615\ldots\).
For each prescribed set of at most fourteen types there is such an alphabet avoiding it.
The support and transversal conclusions hold for a covering family on the same tuple.

The neutral degree estimate applies to every vertex in the defined set \(V\).
The private-stub population \(n(129/16513)/7-1\) is odd, so \(V\) is nonempty.
The degree-\(126\) polynomial on the affine complement of an empty projective line gives the even weight lower bound \(256\).
At equality, even intersections force an empty affine line, since otherwise each line through a support point contains precisely one of the other 255 support points and there are only 129 such lines.
With \(t\) empty parallel lines, polynomial division gives \(256\ge(128-t)(t+2)\) and \(1\le t\le126\).
Thus \(t=126\), and the two full affine lines give a projective symmetric difference.
Two selected lines contain four active points in their difference, a nonselected line meets at most one of the three active points outside a given selected line, and any nonselected line contains at most two active points.
Excluding up to three further mixed ordinary points leaves at least \(249\) signed stubs.
Weights above \(256\) are even, so removing all nine exceptional points still gives degree at least \(249\).

Each occupied formal pair contributes one or two stubs, and its multiplicity remains fixed when sampling without replacement.
For \(h=\min(2,f)\) the only negative one-step increment is at zero.
Turning an existing single into a double therefore increases or preserves \(h\) on every draw.
For \(125\le m\le249\) occupied pairs, one may consequently check exactly \(249-m\) doubles.
At total degree 249, replacing two singles by a double and a zero has conditional mean increment \((2\Pr(Y=0)-\Pr(Y=3))/2\) when exactly one is chosen.
The other sampled pairs number 61 and are uniform on the remaining 8250 types.
Degree three requires one double and one single or three singles.
Writing \(2a+b=247\) for the remaining weights gives \(ab\le247^2/8\), and the downward ratios of the zero-population binomial coefficients are at most \(61/(8003-60)<1/130\).
The resulting upper bound on \(\Pr(Y=3)/\Pr(Y=0)\) is below \(1.581\), giving the required sign throughout the replacement sequence.
For \(m\ge249\) the all-single pattern bounds the expectation from below at that \(m\).
Adding an occupied pair to it has nonnegative conditional increment because \(\Pr(Y=1)/\Pr(Y=0)=61m/(8191-m)>1\) when the denominator event has positive probability, and only the event \(Y=0\) could decrease \(h\).
These comparisons exhaust all possible patterns since degree at least 249 requires at least 125 occupied pairs.

Exact rational evaluation of the four hypergeometric probabilities for 249 singles gives \(\mu=0.11559073054769\ldots\) and \(\rho>428/10000\).
Linearity of expectation gives this lower bound \(\mu\) on the mean of the vertex average \(U\), including when sampled degrees at different vertices are dependent.
On the complement of the surplus event \(U\le X<1/32\), and everywhere \(U\le2\).
When the complement has positive probability the resulting upper bound on the mean is strict, giving the strict probability claim.
The case of a null complement follows directly from \(\rho<1\).

Given surplus at least \(v/32\), deleting a single pivot edge costs at most two units of surplus.
Until the surplus drops below \(v/64\), the average degree on the nonisolated graph is at least \(2+1/64\), which gives a cycle of length at most \(H\) by the nonbacktracking count in v1.
The \(\lceil v/128\rceil\) pivot chains are independent, and the original cycle space has dimension \(e-v_0+\#\pi_0\ge v/64\).
For either projection its compression to the original edge set fixes the corresponding supported chains and has trace at most \(v_0\operatorname{Tr}_{K_S}P\), also for edges in different left cosets.
Using \(v_0\le v\) proves the two trace inequalities on this one alphabet.
The short chains and their translates are the columns and translates generating the closed image of the finite group-ring matrix.
For infinite \(K_S\), the edge kernel has dimension \(62-1\), and quotienting by the closure of finite cycles gives the first reduced Betti number.
The Cayley-graph identification and finite-type cellular conventions used here agree with the source texts. [Lyons–Pichot–Vassout, pp. 600–601](../../literature/pdf/LPV08.pdf#page=6) · [Lück, Definitions 1.29–1.30](../../literature/pdf/Luc02--book-manuscript.pdf#page=46)

Deleting fourteen types costs at most 28 signed stubs per vertex.
For the remaining degree \(u\ge221\), the mean sampled degree is \(62u/8238\) and the probability of isolation is at least \(\binom{8238-u}{62}/\binom{8238}{62}\), with the stated zero convention.
The consecutive difference of the resulting surplus bound is strictly positive because the avoidance ratio on the other 61 draws is at most \(1/(1+61u/8237)<1/2\) whenever it is positive.
Exact rational comparison at \(u=221\) gives \(\phi(221)-1/32=0.0001924390669755\ldots>0\).
Thus some remaining 62-set realizes the required surplus for each prescribed exclusion.

In a complete covering list, a nonzero short-relation matrix requires a nonzero neutral output in a covering configuration, whose label set contains a minimal one.
The probability of containing a prescribed \(j\)-set is \(q_j=\binom{62}{j}/\binom{8252}{j}\).
Integer comparison gives \(771q_2\le\rho<772q_2\) and \(106045q_3\le\rho<106046q_3\).
A transversal of size at most fourteen would miss the entire alphabet of a successful draw that avoids it, contradicting the inclusion of a covered support in that alphabet.
Applying the exclusion criterion to an individual tuple still requires an upper bound for its complete covering family.

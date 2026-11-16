---
author: Yin
---
# Connectivity, collision counts and the explicit character bound

A separate reviewing agent checked the entire [fixed Claim](../../claims/Yin_C_A0040_v1.md) for Yin on 2026-11-16T18:15 UTC.
The reviewer did not develop this proof or the related finite-target entropy argument and received no substantive development discussion, exploration notes, author explanations or previous verdict on them.
The source model, matching switch, small-set expansion and the prescribed-root separation interface were checked in the cited copy of Ope26f.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0040_v1.md#statement) | Connectivity in the prescribed random law, support sizes in probability, the two notions of count and explicit exponential rate for \(C_7\). |
| [Whole-argument finding](#whole-argument-finding) | [Cut estimate](../../claims/Yin_C_A0040_v1.md#the-probability-of-a-cut) | Conditional probability for matchings, incidence variance, two entropy regimes, connectivity and nonzero character bound. |
| [Whole-argument finding](#whole-argument-finding) | [Collisions and supports](../../claims/Yin_C_A0040_v1.md#distinct-labels-away-from-the-roots) | Uniform single-vertex failure, averaging, support parity, and actual-versus-occurrence totals. |
| [Whole-argument finding](#whole-argument-finding) | [Girth event](../../claims/Yin_C_A0041_v1.md#girth-conditioning-and-the-torsion-free-realizations) | The subexponential lower bound on girth probability needed to transfer the exponential estimates. |

## Whole-argument finding

For fixed vertex colors and a feasible inverse-pair permutation rule, each matching independently contributes the stated ratio of factorials.
The two ends have the same entropy, so summing over all signed labels counts each matching twice.
Dropping the extra labels from the entropy loss gives a valid upper probability bound.
For ordinary points, equal line sizes and projective-plane incidence give the displayed mean and variance formula since the incidence product acts as \(qI\) on centered vectors.
The elementary bounds \(-\log x\ge 1-x\) and \(\sum_i m_i^2\le\max_i m_i\) then give (2).

For a binary partition of smaller density \(\theta\ge p^2\), the surplus in the exponent divided by \(\theta\) is at least \((129/2)(1-128/129^2)-1-2\log(1/p)>4\).
For \(\theta<p^2\), every ordinary point has smaller-global-class fraction at most \(\theta/p\), and averaging gives entropy at least \(\theta\log(1/\theta)/2\).
Subtracting the global binary entropy again leaves more than \(4\theta\).
The multinomial count at a fixed histogram and the polynomially many histograms therefore rule out all macroscopic closed cuts after girth conditioning.
The small-set doubling event of [Ope26f, Lemma 2.3, pp. 6–7](../../literature/pdf/Ope26f.pdf#page=6) rules out the complementary size regime.
A smallest component of a disconnected graph would give one of those cuts, proving connectivity on both sides with the claimed probability.

For a nonzero character to \(C_7\), a label with nonzero increment forces each of its \(np\) matching edges to touch the complement of the most common color.
A vertex accounts for at most two such endpoints, hence \(\theta\ge p/2\).
Splitting the off-majority mass evenly among six colors gives the upper entropy \(\theta(1+\log(6/\theta))\).
The difference is therefore at least \(\theta[(129/2)(1-128/129^2)-1-\log(12/p)]>50\theta\), with \(p=129/16513\).
The fixed \(7^{8258}\) possible generator assignments and the factor \(\exp(o(n))\) from girth conditioning preserve the bound \(\exp(-25pn+o(n))\).

The cone group is independent of the choice of roots because every component is coned.
Within a component equality of two path labels relative to a fixed root is equivalent to a trivial group label between the two vertices, a root-independent relation.
The source's rooted separation applies with an initial vertex prescribed in advance by [Ope26f, Propositions 4.5 and 5.1](../../literature/pdf/Ope26f.pdf#page=18).
Within each of the finitely many full vertex types the girth-conditioned law is invariant under vertex renaming, giving uniform \(o(1)\) ambiguity probability after checking one representative per type.
Expectation and Markov's inequality give \(o(n)\) ambiguous vertices in probability, without requiring simultaneous separation at every possible root.
On a connected side every other vertex contributes a distinct singleton label to the factor, giving support size \(n-o(n)\) in probability.
Collecting in characteristic two removes an even number of occurrences, so the support size is even, and a separated root gives a nonzero identity coefficient.

For the trivial character, all \(n^2\) vertex pairs on connected sides lie above the identity.
The actual number of pairs of surviving support labels is the product of the two actual cardinalities, hence \(n^2-o(n^2)\) in probability.
Further conditioning on an event already of probability \(1-o(1)\) preserves these conclusions.
The deterministic torsion-freeness and survival of the prescribed roots are used at the scope established by the source cone argument.

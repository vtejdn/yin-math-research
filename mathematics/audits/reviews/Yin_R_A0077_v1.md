---
author: Yin
---

# Character ratios forced by isolated simultaneous edges

A separate reviewing agent checked fixed C_A0046_v1 for Yin on 2026-11-17T00:33 UTC.
The reviewer did not develop C_A0046 or receive its proof-development discussion, author explanations or a prior verdict.
The reviewer developed the earlier full-alphabet entropy argument in C_A0041, here used as an established input, and a separate same-side synchronous forest calculation.
The latter supplies no step in C_A0046.
This inspection checks the use of the entropy estimate on the smaller alphabet and the new isolated-edge, lattice and coarsening arguments.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0046_v1.md#statement) | Isolated-component equations on the full vertex lists, complex equivalence, probability and conditional transfer. |
| [Whole-argument finding](#whole-argument-finding) | [Isolated edges](../../claims/Yin_C_A0046_v1.md#isolated-edges-and-their-bipartite-graphs) | Characterization of entire two-vertex components, both endpoint counts, connectedness, and direction of ratios. |
| [Whole-argument finding](#whole-argument-finding) | [Cycle lattices](../../claims/Yin_C_A0046_v1.md#the-two-cycle-lattices) | Necessity in commutative rings with unit variables, complex character extension, and obstruction at odd index. |
| [Whole-argument finding](#whole-argument-finding) | [Odd indices](../../claims/Yin_C_A0046_v1.md#odd-indices-in-the-original-matching-ensemble) | Mod-two rank, restricted incidence connectivity, strict entropy gap and preservation under the stated conditionings. |
| [Whole-argument finding](#whole-argument-finding) | [Actual product fibers](../../claims/Yin_C_A0046_v1.md#what-survives-collection-of-the-actual-products) | Connected spanning hypothesis for complete occurrence fibers, local loss bound, and distribution of coefficients over repeated labels. |
| [Whole-argument finding](#whole-argument-finding) | [Entropy input](../../claims/Yin_C_A0041_v1.md#strict-entropy-loss) | Multinomial count and compactness at fixed alphabets. |
| [Whole-argument finding](#whole-argument-finding) | [Girth conditioning](../../claims/Yin_C_A0041_v1.md#girth-conditioning-and-the-torsion-free-realizations) | Subexponential cost of logarithmic girth and the source's subsequent high-probability geometric events. |
| [Whole-argument finding](#whole-argument-finding) | [Connectivity input](../../claims/Yin_C_A0040_v1.md#the-probability-of-a-cut) | Identification of the full vertex lists with the root components with probability tending to one. |

## Whole-argument finding

The [source type data](../../literature/pdf/Ope26f.pdf#page=4) specify the ordinary and extra letter intersections, inverse-pair bijections and independent unconditioned matching law used here.
Of \(16513\) ordinary letters, three are paired to extras, leaving \(16510/2=8255\) retained inverse pairs.
When a signed extra is shared, the two vertices share both extras of the first side's pair as well as an ordinary point.
For a single common ordinary letter the lines must be distinct and their extra parts cannot both be nonempty.
Applying this test at each end makes the stated edge an isolated component.
Conversely the absence of side loops and parallel edges ensures that a two-vertex component has a single edge, so degree one at both ends gives exactly that test.

Given an initial fixed vertex and a signed ordinary letter, the wrong line occurs with proportion \(1/129\) on the other side.
The proportions with nonempty extra part are \(p\) and \(3p/2\) on the two sides.
The inverse-label matching sends the variable vertex bijectively to the opposite letter class, allowing the same estimates without an independence assumption at the other end.
Both parts therefore have minimum degree at least \((1-2/129-3p)m>m/2\).
Any two vertices in one part share a neighbor, and the other part has no isolated vertex.
Consequently all \(A\)-edge ratios at that letter are constant, and every \(B\)-edge ratio is the negative inverse.
The second-side group labels invert upon forming the factor; its vertex coefficients still move in the forward direction along the simultaneous edge.

Cycle products give characters trivial on \(\Lambda_A\) and equal to the parity sign on \(\Lambda_B\) for the same vector of \(A\)-ratios.
They agree on the intersection precisely when the displayed parity vanishes there.
Smith coordinates give the extension to \(\mathbb Z^r\) over \(\mathbb C^\times\), and path transport on each connected component separately proves sufficiency.
Necessity only uses commutative units.
For finite odd indices their product \(d\) annihilates both finite quotients, so \(d e_t\) in the intersection forces \(1=-1\).
Modulo \(4\mathcal O_L\), \(2\ne0\) for every finite \(L/\mathbb Q_2\); thus the conclusion is unchanged by ramification.

Binary annihilators of all closed walks are exactly the assignments whose edge increments can be integrated on the retained graph, whether connected or not.
The entropy count simply omits the unused independent matching blocks; the original type partitions and their positive weights remain intact.
Every type still carries at least 126 retained letters.
For any two distinct ordinary lines there are retained points on each away from their common point.
The third line through those two points connects their colors even if their original point of intersection was deleted.
Zero entropy loss would thus force a constant binary color and the zero binary assignment.
Compactness for each nonzero assignment, then a finite union, gives the strict exponential loss.
Dividing by the girth probability \(\exp(-o(n))\) and by further conditional probabilities \(1-o(1)\) preserves an exponential bound.
The separate identification with connected full sides uses only its stated probability tending to one.

If complete occurrence fibers retain connected spanning bipartite graphs, they give the same ratios, and the strict local loss threshold leaves minimum degree greater than half.
On an odd-multiplicity group label one may retain its coefficient and insert cancelling unit pairs, and on an even-multiplicity label use only cancelling pairs.
These realize the prescribed reductions without changing either projected factor.
No bound on mergers of different simultaneous components into one actual group-product fiber is established.
The proof supports the full statement at the component-equation level and the expressly conditional transfer to the group-product equations.

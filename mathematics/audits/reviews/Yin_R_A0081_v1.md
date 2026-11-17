---
author: Yin
---

# Stability of the cycle-lattice obstruction under merged product fibers

A separate reviewing agent inspected the fixed C_A0050_v1 for Yin on 2026-11-17T00:39 UTC.
The same reviewer checked the final strengthened product-support inequality and the C_A0049 implication on 2026-11-17T00:43 UTC.
The reviewer did not participate in this Claim's proof development or receive its development dialogue, author explanations or previous verdicts.
The reviewer previously developed the full-alphabet entropy and girth inputs in C_A0041 and L_A0047 and independently checked the exact, undeleted lattice and isolated-edge result in C_A0046.
Here the review checks the new joint-table estimate for violations, uniformity over arbitrary deletions, conversion of impure occurrence mass to matching-edge loss, and the actual coefficient obstruction.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0050_v1.md#statement) | Both matching laws, exponential stability of the odd indices, and deterministic and probabilistic conclusions for exact collected supports. |
| [Whole-argument finding](#whole-argument-finding) | [Approximate color equations](../../claims/Yin_C_A0050_v1.md#approximate-binary-color-equations) | Equivalence to arbitrary post-sampling deletions, exact joint-table matching probability, type-color entropy and number of violations. |
| [Whole-argument finding](#whole-argument-finding) | [Uniform gap](../../claims/Yin_C_A0050_v1.md#a-uniform-gap-under-deletions) | Compactness for positive defect budget and the argument using odd orders of the retained planted displacements. |
| [Whole-argument finding](#whole-argument-finding) | [Removal of edges](../../claims/Yin_C_A0050_v1.md#actual-product-fibers-after-edge-removal) | Purity and the complete two-term equations, both pruning thresholds, lattice contradiction for commutative unit coefficients, and redistribution over repeated labels. |
| [Whole-argument finding](#whole-argument-finding) | [Positive density](../../claims/Yin_C_A0050_v1.md#positive-density-for-the-actual-collected-supports) | The deterministic sum of impure occurrences and nonzero product count, uniform lower bound on product support, high-probability combination and ramified scope. |
| [Whole-argument finding](#whole-argument-finding) | [Two-root purity input](../../claims/Yin_C_A0049_v1.md#statement) | Connectedness and convergence to zero in probability of the fraction of all occurrences in merged fibers in these same two laws. |
| [Whole-argument finding](#whole-argument-finding) | [Exact incidence input](../../claims/Yin_C_A0046_v1.md#isolated-edges-and-their-bipartite-graphs) | Full bipartite graph's minimum degree and forward orientation of both vertex-coefficient ratios. |
| [Whole-argument finding](#whole-argument-finding) | [Original law](../../claims/Yin_C_A0041_v1.md#girth-conditioning-and-the-torsion-free-realizations) | Subexponential cost of conditioning on logarithmic girth. |
| [Whole-argument finding](#whole-argument-finding) | [Planted law](../../ledger/Yin_L_A0047_v1.md#girth-local-expansion-and-the-cost-of-a-matching-prescription) | Balanced color block sizes and subexponential girth conditioning in that law. |

## Whole-argument finding

For each retained matching edge, mod-two orientation has no effect on its assigned letter bit.
A nonzero annihilator of the remaining signed closed walks allows integration of the bits separately on each remaining connected component.
The only failed edge equations can then be deleted edges.
Conversely deleting the violated equations makes the bit assignment annihilate every remaining closed walk.
Integer diagonal form makes this equivalent to failure of finite odd index after the allowed deletions.
No independence of deleted edges from the sampled graph is needed.

In a block of size \(N\), the multinomial allocations of named source vertices to destination bits number \(\prod (Nu_i)!/\prod (NJ_{ij})!\).
There are then \(\prod (Nv_j)!\) bijections to the named destinations.
Division by \(N!\) gives the printed table probability with its required marginals.
The logarithmic exponent for each block is minus \(N\) times the mutual information, including on simplex faces, while choosing vertex colors gives the type-entropy exponent.
Both the polynomial number of joint histograms and the finite number of bit assignments are independent of which deletions will be made.
At zero defect the bit on one end uniquely determines the other in each matching block.
The resulting half sum over both signed letters bounds the type entropy with coefficient at least \(126/2=63\).
Equality of the net exponent to zero would make every refined type and every retained letter monochromatic at each planted color.
Deleting the three ordinary points paired to extras leaves the type-incidence graph connected by the third-line argument in C_A0046.
Therefore only the planted color can determine the bit.
Iterating its translation by \(\eta(t)\) an odd number of times around that letter's orbit forces \(s_t=0\), without a generation hypothesis on the retained letters.
Continuity and compactness now bound the exponent strictly below zero on a sufficiently small fixed neighborhood \(D_s\le\varepsilon\) for every \(s\ne0\).
The subexponential girth cost in either law preserves an exponential bound.

Each bipartite edge removed because of impurity corresponds to an isolated simultaneous-step component in an impure occurrence fiber, and these components have disjoint occurrence vertices.
Each edge removed because its whole product fiber has a nonzero coefficient determines a distinct group product, including when considering different oriented letter pairs.
The total number of removed edges is therefore at most \(J+|\operatorname{supp}(ab)|\), with no need to estimate sizes of the impure fibers separately.
At a fixed letter discarding vertices incident to at least \(M/8\) removed edges costs at most \(16h_t/M\) vertices across the two parts.
The two bounds on \(\delta\) respectively keep the total corresponding side-edge deletions within \(\varepsilon n\) and the number of discarded vertices at each letter within \(M/8\).
A remaining vertex has lost fewer than \(M/8\) edges directly and at most \(M/8\) possible partners through vertex deletion, keeping degree greater than \(M/2\).
The surviving parts are nonempty and connected, by common neighbors in a part of size at most \(M\).
Every retained matching edge on either original side therefore has its letter's constant coefficient ratio, inverting it in reverse orientation.
The product of the two odd lattice indices annihilates both quotient lattices.
The resulting odd powers of the two ratios are both one, contradicting their product \(-1\) when \(2\ne0\) in the commutative coefficient ring.

Purity here means one entire simultaneous component in a group-product fiber of the original occurrence rectangle.
Each surviving pure isolated component has zero group coefficient by the second removal rule, giving the required two-term ratio exactly.
The contradiction proves the strict deterministic inequality whenever the tuple has the deletion property.
Reinstating each coefficient on an odd class once and adding cancelling unit pairs, also on classes with even multiplicity, takes arbitrary unit coefficients on the binary-collected supports to occurrences without changing the product or its support.
This step preserves all group-ring coefficients, including over rings with nontrivial zero divisors.

The fixed C_A0049 statement counts the total number of occurrences in impure fibers, precisely \(J\) in this theorem.
It gives \(J/n^2\to0\) in probability and full-side connectedness in both prescribed girth-conditioned laws.
Intersecting \(J\le\delta n^2/2\) and connectedness with the exponential deletion event costs only \(o(1)\), without independence of the events.
The single resulting event depends on the graphs alone.
The strict inequality then gives the stated bound with \(c_*=\delta/2\) for all commutative rings with \(1\ne-1\) and all their unit coefficient choices together, taking the smaller constants for the two laws.
In particular it applies to arbitrary nonzero complex coefficients and to residue-one lifts in \(\mathcal O_L/4\mathcal O_L\) for finite \(L/\mathbb Q_2\), where \(v_L(2)<v_L(4)\) and the specified coefficients are units.
This review checks the applicability of the fixed C_A0049 purity result at that interface, without undertaking a second review of its two-root arrangement theorem.
The complete strengthened argument is supported for these supports and ensembles, leaving products on other supports and general analytic ranks undetermined.

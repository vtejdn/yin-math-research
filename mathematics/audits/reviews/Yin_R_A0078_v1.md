---
author: Yin
---
# Common-step return probabilities and binary homology in the seven-sheeted cover

A separate agent reviewed the complete [fixed Claim](../../claims/Yin_C_A0047_v1.md) for Yin on 2026-11-17T00:34 UTC.
The reviewer shared the Task context, had worked on a different letter-ratio argument for isolated edges and on the earlier singleton estimate, and took no part in developing this Claim.
The fixed proof and its stated inputs were inspected without author explanations, development notes, proof-generation discussion or previous verdict on this argument.
The earlier singleton estimate and the planted finite-target estimate are used at their previously reviewed scopes.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0047_v1.md#statement) | Fixed-graph limits, finite survival certificates and exclusion of relative two-group quotients in the planted law. |
| [Whole-argument finding](#whole-argument-finding) | [Fixed-graph walk](../../claims/Yin_C_A0047_v1.md#the-fixed-graph-walk) | Transition symmetry, component limit, type count, isolated edges and scope of a product equality. |
| [Whole-argument finding](#whole-argument-finding) | [Erasure test](../../claims/Yin_C_A0047_v1.md#a-finite-test-for-complete-erasure-of-a-color) | Binary homology of the cover, two enclosing fiber partitions, odd bins, moment identity and one-sided detection probability. |
| [Whole-argument finding](#whole-argument-finding) | [Relative two-group refinements](../../claims/Yin_C_A0047_v1.md#why-every-relative-two-group-refinement-can-disappear) | Simple binary quotient modules, explicit splitting, fixed finite targets and exclusion of all finite two-group quotients of the kernel. |
| [Whole-argument finding](#whole-argument-finding) | [Singletons](../../claims/Yin_C_A0040_v1.md#distinct-labels-away-from-the-roots) | Existing upper bound in probability for occurrences meeting an ambiguous factor vertex. |
| [Whole-argument finding](#whole-argument-finding) | [Cubic factors](../../claims/Yin_C_A0042_v1.md#separating-the-cubic-factors) | Factor degrees of \(X^7-1\) over \(\mathbb F_2\). |
| [Whole-argument finding](#whole-argument-finding) | [Factorization in the planted law](../../claims/Yin_C_A0044_v1.md#connectedness-and-factorization-through-the-finite-quotient) | The preassigned targets \(C_{14}\) and \(\operatorname{AGL}(1,8)\), under the stated conditioning. |
| [Whole-argument finding](#whole-argument-finding) | [Planted counts](../../claims/Yin_C_A0044_v1.md#the-histogram-after-collecting-actual-group-labels) | Existing parity and lower occupancy estimates when the vector test gives zero. |

## Whole-argument finding

The lazy matrix is half the identity plus half a symmetric stochastic matrix, so its eigenvalues lie in \([0,1]\).
Its positive transitions generate exactly the simultaneous components, which identifies the eigenspace at one and gives the stated limiting kernel entries and unnormalized trace.
Independent uniform sampling of the two vertices uses line equality with probability \(1/16513\), and adds two common extras with probability \(3(129/16513)^2/2\).
Every degree-one vertex outside an isolated edge consumes an incidence of a higher-degree vertex.
Including those higher-degree vertices themselves bounds the exceptional fraction by \(130/16513+6(129/16513)^2=0.00823875\ldots\).
The earlier \(o(n)\) ambiguous-vertex counts affect at most \(o(n^2)\) pairs in probability and at most that many additional matched partners on isolated edges.
No converse to product constancy on a component enters the return-probability argument.

The stated presentation-cover calculation computes first homology with binary coefficients of the connected seven-sheeted cover.
Tree collapse gives the ordinary graph cycle space, and lifting the finitely many fundamental relators at every starting color accounts for their conjugates before taking homology.
This identifies the finite cycle quotient with the mod-two abelianization of \(K\).
For fixed \(c\), changing \(s(c)\) subtracts the same vector in that abelianization from every recorded label.
Thus equality of recorded vectors tests equality in \(E\) within that class.
For product fibers the component gives an inner bound and the \(E\)-fiber an outer bound.
When both are the same two pairs with distinct row labels modulo \(E\), cancellation in the group makes the two column labels distinct too.
An additional occurrence of any one label with its old partner would be a third pair in the same fiber, so in this case the two terms also survive collection.

In an odd bin at least one original label has odd multiplicity, and distinct bins provide distinct such labels.
Binary character orthogonality kills precisely the cross terms between different bins in the real second moment.
For each integer multiplicity \(m\ge0\), \(m^2-2m+\mathbf1_{\mathrm{odd}}(m)\ge0\), giving the asserted lower bound, including bins of size zero, one and two.
In the random compression, even bins never affect output parity.
For a fixed odd bin, a union bound over the other odd bins loses at most \((s-1)2^{-r}\), proving one-sided detection with the specified probability.
For the four example vectors each nonzero linear form has two occurrences of each value, while the zero form places all four in one even bin.

If \(V\ne0\), its finite-dimensional cyclic module has a nonzero simple quotient.
The irreducible factors of \(X^7-1\) give a trivial binary line or a binary three-space with the full order-seven scalar action.
The quotient kernel in \(E\) is invariant under conjugation, so division by it preserves a surjection onto the required extension.
For a lift \(t\) of the chosen generator, \(t^{14}=1\) because \(t^7\) belongs to an elementary abelian two-group.
The element \(t^8\) still maps to the same generator and has order exactly seven.
The split extension is then one of the two claimed fixed abstract groups, with nontrivial image of \(K\).
The planted factorization theorem excludes that event with exponentially high probability under girth conditioning.
Finally every nontrivial finite two-group admits an order-two quotient, whereas a homomorphism \(K\to C_2\) factors through \(V\).
This explains the uniform exclusion without a union bound over growing group orders.
An odd quotient bin certifies survival, while a zero test on the planted examples is compatible with many distinct surviving labels.
These results leave the full group-product fiber partition and the original complex lifting problem unresolved.

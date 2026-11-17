---
author: Yin
---

# Central signatures of opposite-side loop certificates

At 2026-11-17T02:47 UTC an agent outside the development of Yin_C_A0063_v1 independently reviewed the statement, both general proof sections and the commutator example for Sheng Yin.
The reviewer read the fixed claim and the earlier homology criterion without receiving development dialogue, author explanations or a prior finding on this argument.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0063_v1.md#statement) | Asphericity, independent prescriptions into a finite two-group, central elements of square one, cycles and pairings, and the example's scope. |
| [Whole-argument finding](#whole-argument-finding) | [Extension of prescriptions](../../claims/Yin_C_A0063_v1.md#lifting-independent-maps-from-translated-right-side-graphs) | The intermediate cover and its homology and cohomology, lifting over a central order-two kernel and independent correction on every based translate. |
| [Whole-argument finding](#whole-argument-finding) | [Certificate evaluation](../../claims/Yin_C_A0063_v1.md#evaluating-an-equality-certificate) | Deck index and conjugator for one loop or a product of relators, common-step transport, cycle telescoping and matching comparison. |
| [Whole-argument finding](#whole-argument-finding) | [Commutator pairings](../../claims/Yin_C_A0063_v1.md#two-pairings-of-commutator-copies) | Immersion, free group and root separation, complete color count, homology of all fillings, matrix commutator values and failure of asphericity. |
| [Whole-argument finding](#whole-argument-finding) | [Earlier homological test](../../claims/Yin_C_A0055_v1.md#certificates-using-several-graph-relations) | Actual opposite-side contributions of a multiple-relator certificate and why the integral chain calculations in this example imply the earlier comparisons. |

## Whole-argument finding

The rose surjects onto both groups, so the pullback of \(X_A\) in the universal cover of \(X\) is connected, with fundamental group \(N\).
Asphericity makes that cover contractible.
The connecting map from the relative second homology of the added cones identifies the direct sum of the translated \(H_1(B;\mathbb F_2)\) with \(H_1(Y;\mathbb F_2)\).
It is precisely the map on abelianizations induced by the transported loop maps, since changing a base path by conjugation has no effect on first homology.
In the cellular chain complex of the two-dimensional contractible cover the second boundary is injective, so its restriction to the subcomplex \(Y\) is injective as well.
The resulting \(H^2(Y;\mathbb F_2)=0\) applies to arbitrary cellular cochains, including for infinitely many translates.

At 2026-11-17T03:01 UTC a second reviewer, isolated from development and prior findings, independently verified for the added Stallings argument that the free-product map induces the displayed first-homology isomorphism and that attaching cells of dimension at least three gives a surjection from \(H_2(Y;\mathbb F_2)=0\) onto \(H_2(N;\mathbb F_2)\).
Stallings's theorem identifies the finite-stage lower \(2\)-central quotients without a finite-generation hypothesis, so the prescribed map extends through the stage at which the target's lower \(2\)-central series is trivial. [Cochran and Harvey, Theorem 1.1, p. 678](https://math.rice.edu/~shelly/publications/Stallings_p.pdf#page=2)

Induction along a central order-two subgroup \(Z\le P\) first extends all the maps to \(P/Z\).
A choice of lifts for the edge transports then gives a central relator error on each two-cell.
The vanishing of second cohomology makes this two-cochain a coboundary, and multiplying the lifted edge transports by the correcting one-cochain removes all errors at once.
The discrepancy between the resulting homomorphism and the desired one on each based copy takes values in \(Z\) and is a homomorphism by centrality.
The homology direct sum extends the entire family of discrepancies to one character \(N\to Z\), so the final correction preserves all the specified values.
This verifies the extension directly for every finite two-group without an assumption on the size of the deck set.

For a copied loop its displacement in \(G_A\) is \(v_x\overline C v_x^{-1}=v_{x'}v_x^{-1}\).
The conjugator taking the based word \(l_b C l_b^{-1}\) to this displacement maps to \(g_xh_b^{-1}\), and comparison with its chosen lift changes it only by conjugation in \(N\).
The prescribed value is central in \(P\), so applying the extension gives the same value after that conjugation.
Common right multiplication at both endpoints preserves the displacement.
Displacements around a cycle telescope in reverse traversal order, and for central involutory values orientation and ordering have no effect.
Two finite matchings on the same saturated vertices differ by cycles, including parallel edges with different witnesses.
For a product certificate each \(A\)-relator disappears already in \(G_A\), while the conjugator for a \(B\)-factor maps to \(g_x\bar u_jh_{b_j}^{-1}\).
This gives exactly the stated index and evaluation under the individual centrality and square-one assumptions.

In the example, distinct letters and the two distinct end phases give an immersion and the single \(A\)-core cycle has length \(16m\).
The two relations \(U,V\) alone eliminate one free generator each, leave the private letter \(r\) free and imply the full \(A\)-core relation.
The single-cone presentation complex collapses to a graph by these two free faces, whereas the two-cone presentation has the extra redundant relation.
The \(B\)-root is alone at color zero and all other left labels include \(r\) once, giving the stated root separation.
The three successive commutators have thirteen macro-endpoints including both ends.
The shifted arc meets its starting color exactly once in its interior because the phase \(b_1\) has two visits per cyclic traversal.
All fourteen occurrences have the same label \(r\), so the entire left color erases.

The integral lifted Cayley chain of \(W\) is zero since \(U\) and \(V\) are already closed there, and the same holds after conjugation or translation.
All translated \(A\)-cycles consequently have zero Cayley chain.
The single-cone relative sequence gives injectivity for the translated \(B\)-cycle summands, so two fillings of the same comparison cannot leave different total first-homology signatures.
The four displayed central-test witnesses themselves have zero integral class in \(B\).
In the unitriangular group their index-three commutator is \(I+E_{13}\), a nonidentity central involution.
The shifted copy is evaluated at index two and gives the identity.
The two matchings of the four marked vertices therefore have different products.
Those four vertices alone furnish the obstruction, irrespective of the common pairing of the ten remaining vertices.

The argument establishes the aspherical consistency test and its strict improvement on the first-homology comparison in this example.
The example's group is free, but the specified two-cone complex fails asphericity and its vertex types differ from the four-line prescription.
It gives no realization of color-three erasure in the four-line groups.

---
author: Yin
---

# What simultaneous readable words preserve on independent commutator blocks

At 2026-11-17T03:54 UTC an agent outside the development of Yin_C_A0075_v1 independently reviewed its statement and the arguments on deck indices, forest offsets and the three-block construction for Sheng Yin.
The same reviewer independently checked the added common-word cycle and its statement at 2026-11-17T03:56 UTC.
The reviewer had previously examined the mixed central group, the six-vertex block construction and the C72 bridge and trial estimates.
The current review received no development dialogue, author explanations or prior verdict on C75 and checked the three-block extension directly.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0075_v1.md#statement) | General common-word criterion, parity classes of marked tuples, matching consistency, the specific three-block realization and cycle-length restrictions. |
| [Whole-argument finding](#whole-argument-finding) | [Deck indices](../../claims/Yin_C_A0075_v1.md#two-start-labels-in-a-common-coarse-color) | Equality of coarse first-coordinate maps, their restriction to \(\Phi\), the equal-deck conjugation argument and the distinct-deck direct-sum argument. |
| [Whole-argument finding](#whole-argument-finding) | [Parity and offsets](../../claims/Yin_C_A0075_v1.md#what-a-cross-block-bridge-and-its-transports-can-decide) | Separation of marked tuples by parity, arbitrary intermediate vertices and the consistency of proposed elementary-abelian edge values on a forest. |
| [Whole-argument finding](#whole-argument-finding) | [Cyclic reading](../../claims/Yin_C_A0075_v1.md#a-common-word-cycling-among-blocks) | Torsion-freeness, ordered transport and central offsets, fourth-power identity and the rank obstruction for a two-block exchange. |
| [Whole-argument finding](#whole-argument-finding) | [Three disjoint blocks](../../claims/Yin_C_A0075_v1.md#genuine-bridges-between-disjoint-six-vertex-blocks) | Free and cyclic reduction, eighteen distinct marks, orientations and lamp changes of the two bridges, actual group labels, conditional extension and simultaneous probability estimate. |
| [Whole-argument finding](#whole-argument-finding) | [Mixed homomorphism](../../claims/Yin_C_A0066_v1.md#the-finite-tensor-calculation) | The first two coordinates, the central exponent-two kernel and triviality on the fixed rooted \(A\)-loop group. |
| [Whole-argument finding](#whole-argument-finding) | [Actual deck summands](../../claims/Yin_C_A0055_v1.md#from-cycles-in-the-lifted-rose-to-vertex-potentials) | Deck-equivariant relative boundary on lifts of graph homology. |
| [Whole-argument finding](#whole-argument-finding) | [All-position bridges](../../claims/Yin_C_A0072_v1.md#reading-prescribed-state-changes-and-parallel-bridges) | Neutral independent commutators, the bridge word in the two-action law and fresh sampling after exposing the cycle searches. |

## Whole-argument finding

Conjugation by a rose word translates the full relation homology by its actual group element, since changes of connecting paths induce inner automorphisms of \(N\).
Two rose words of the same coarse color therefore induce identical first two coordinates after summing over the fibers of \(G\to Q\) and deleting the identity \(A\)-summand.
The two resulting homomorphisms \(N\to P\) differ pointwise by a central element.
Their difference is consequently itself a homomorphism into an elementary abelian group, so it kills the full subgroup \(\Phi=[N,N]N^2\).
Each individual map takes \(\Phi\) to central values.

The common reading \(w\) is in \(N\), because it differs from the given null word \(p_x\) by a based graph loop.
After basing at either start, its image in \(P\) equals the corresponding given tensor since the rooted \(A\)-loop is killed.
When \(g_x=g_y\), the change of conjugator is in \(N\), so the two values are conjugate and central and hence equal.
When \(g_x\ne g_y\), the rooted-loop identity first gives \(g_x[w]\in H_1(A)_1\), where \(g_x\) acts by left deck translation and \([p_x]=0\).
The second identity similarly gives \(g_y[w]\in H_1(A)_1\).
Thus \([w]\) lies in two distinct actual summands indexed by \(g_x^{-1}\) and \(g_y^{-1}\), and their intersection is zero.
It follows that \(w\in\Phi\), where the same-coarse-color maps already agree.
This step uses distinct actual deck labels before the projection to the coarse quotient.

In a block of type \(T\) the subpath between marked indices \(i,i'\) has central value \((i-i')T\), taken modulo two.
A single word moving two marked coordinates must give equal values.
For independent types this forces both changes of parity to vanish even if the path visits unmarked vertices in between.
The four parity classes are all represented, and restriction to two coordinates at a time gives at least \(2^k\) distinct components among the marked tuples of \(k\) independent types.
In a forest of proposed identifications, offsets on the blocks solve the prescribed edge equations recursively.
Adding these offsets to the internal potentials preserves every permitted transport returning to the same two blocks and makes the total on a saturated set independent of its matching.
This computation gives consistency for the stated central values alone.

If the same word maps a mark in each block to the next block cyclically, the common group labels obey \(g_{i+1}=g_i\pi(w)\).
Closing the list and using torsion-freeness gives \(\pi(w)=1\), so all \(g_i\) agree even when the outgoing and incoming marks differ within a block.
With that common label the comparison elements \(n_i\) are defined inside \(P\).
Triviality of the rooted \(A\)-loops gives \(c_{i+1}n_{i+1}=n_i v\) in the stated order, with \(c_i\) central, hence \(v^l=\prod_i c_i\).
Every fourth power in \(P\) is the identity and the square of \((a,b,c)\) is the pure tensor \(a\otimes b\) in the central coordinate.
The resulting sum vanishes if \(4\mid l\) and has rank at most one if \(l\equiv2\pmod4\), excluding a two-block exchange whose changes have rank-two sum.

In the thirteen-coordinate model each unguarded commutator is cyclically reduced, so its positive and negative fifth powers have the required lengths.
The fresh neutral letter in \(D'=vDv^{-1}\) preserves the full lamp increment and prevents cancellation with the adjoining powers in the displayed word.
In a simple open lift the two positive-length bridge intervals separate three sets of six marks.
From the first middle mark to its adjacent outer mark one reads the reverse of the displayed inverse bridge, hence \(D'\), and from the last middle mark one reads \(D'\) forward to the other outer block.
Both starts have the same fine state and both destinations differ from that state by one in every visible coordinate.
The internal values of the two outer blocks are of type \(T_2\), independent of the middle type \(T_1\).
All eighteen marks have the same original group label because every power and both conjugated bridges are cone relations.
The two remote bridge endpoints lie in different outer blocks, so no internal \(T_2\) subpath comparison between them is asserted.

The extra word has length at most \(CR+C'\) with the constants fixed by the lamp modulus before \(a\) is selected.
Adding it to the list prior to the open trials keeps \(O(n^{a/4})\) words and the \(O(n^{1-a/2})\) exposure budget.
Shrinking \(a\) to cover the increased \(C\) gives conditional lower comparison mean above \(n^{1-\delta/2}\) for each word, including through the neutral guards.
The inverse girth probability has logarithm \(O(n^{3a/8}\log n)\), absorbed by the cycle and later trial failure exponents.
The three-block configurations therefore coexist with the C65 safeguards on the same matching tuple.
The construction supplies a subset of the color, and extension to a full true matching retains its stated existence hypothesis.

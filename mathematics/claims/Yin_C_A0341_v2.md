---
author: Yin
---

# Excluding a normal linear group of order 168 in an arbitrary quotient

## Statement

Let \(H=\langle s,t\rangle\) satisfy the [cyclic order-sixteen hypotheses](Yin_C_A0341_v1.md#statement) of degrees \(1,6\).
If any quotient \(J\) of \(H\) has a normal subgroup isomorphic to \({\rm GL}_3(\mathbb F_2)\), every noninteger regular nullity of a complex two-square rectangle \(B+At-s(D+Ct)\) is at most \(15/32\).
The quotient \(J\) may be infinite and the hypothesis does not require a retraction onto its normal subgroup.

In particular, at a half kernel no quotient has a normal subgroup \(S^k\) for \(S=A_5\) or \(S={\rm GL}_3(\mathbb F_2)\) and \(k=1,3,5\).
The result for one normal copy of \(A_5\) is the [five-point conjugation test](Yin_C_A0341_v1.md#consequences-for-quotients-and-subgroups).

## The conjugation action on eight cyclic subgroups

Write \(G={\rm GL}_3(\mathbb F_2)\) in its faithful action on the seven nonzero vectors.
Its order is \(7\cdot6\cdot4=168\), by choosing the three ordered basis images.
Let \(G_8\) be its action by conjugation on the cyclic groups of order seven inside \(G\).
The [normalizer verifier](../computations/programs/Yin_J_A0011/verify_linear_normalizer_sixteen.mjs) constructs two explicit linear generators.
In the binary polynomial coordinates modulo \(X^3+X+1\), they are the map adding the second coordinate to the first and multiplication by \(X\); closure has order 168.
Within this group it enumerates all eight cyclic subgroups of order seven, builds their conjugation permutations, and checks that \(G_8\) has order 168.
In particular its action is faithful.

If \(G\) is normal in \(J\), conjugation by \(J\) permutes those eight subgroups and gives a genuine permutation image containing \(G_8\).
It lies in \(N_{S_8}(G_8)\).
The program enumerates all \(8!\) permutations \(h\); membership in the normalizer is equivalent to conjugating both generators into \(G_8\) since the conjugated group has the same cardinality.
There are 336 such permutations, with even part exactly \(G_8\).
Thus the image of \(J\) on these eight objects is \(G_8\) or this normalizer in its entirety.
This recovers both possibilities for the induced group action without an assumption about the other normal subgroups of \(J\).

For the first case the [seven-site and eight-site linear-group certificates](Yin_C_A0341_v1.md#actions-and-finite-certificates) give \(13/28\) whenever \(\delta>7/16\), where \(\delta\) denotes the original fractional nullity.
For the second case, the sign and corner argument of the [actual permutation endpoint test](Yin_C_A0341_v1.md#the-endpoint-test-with-one-possible-singular-corner) allows us to suppose that \(t\) is even, \(B,C\) are invertible and only one of \(A,D\) may have rank one in place of full rank.

## The marked normalizer and the fourteen Klein subgroups

The verifier enumerates every generating pair of the 336-element permutation group with even second mark, taking one representative up to simultaneous conjugation of the action.
Of the 69 classes, 68 already have the eight-site certificate from the [two-end test](Yin_C_A0341_v1.md#the-endpoint-test-with-one-possible-singular-corner).
In the remaining class, form the conjugation action on all Klein four subgroups in the even 168-element subgroup.
The program finds these by taking a pair of different commuting involutions and identifying its subgroup by the unordered triple of nonidentity elements.
The 21 involutions supply 14 distinct subgroups.
The entire normalizer permutes them because its even subgroup is normal.

On the fourteen sites use the displayed group permutations from the verifier and the sixteenth-root character of marked weights \(2,12\).
Subtract sixteen on the first and second edges indicated by masks \(16\) and \(16059\), respectively, numbering bits from zero by initial site.
For clarity, all matchings in this action can be recovered without checking \(4^{14}\) path choices.
Write \(x,y\) for the first and second permutations and \(m_i,n_i\) for the used first and second edges.
For each binary second-edge mask and each cycle of \(x\), try the two possible predecessor values of \(m\), then use
\[
                   m_i-m_{x^{-1}(i)}=n_{y^{-1}(i)}-n_i .
\]
Accept binary periodic solutions on each cycle and combine those independent choices.
The [local matching counts](Yin_C_A0293_v1.md#integer-lifts-on-individual-permutation-edges) show that this gives precisely the possible pairs of used edge sets, even with multiple matchings per pair.

There are 2928 pairs, spread 52, and four minimizing pairs.
At the minimizing anchor with joint mask \(12505116\), the cheaper of the two complementary ends uses zero potentially singular pivots.
The verifier checks from the differences with every other minimum that the recurrent tight edges are disjoint directed simple cycles with nonzero cyclic degree or a nonidentity image word in the actual permutation action, as required in the endpoint test.
This gives \(2\cdot52/(16\cdot14)=13/28\) for the last marked class.
The largest bound over the 69 classes is \(60/(16\cdot8)=15/32\).
Together with \(13/28\) for \(G_8\) and the initial \(7/16\) cutoff, this proves the first assertion.

Finally assume a half kernel and a normal product \(S^k\) of the indicated type in \(J\).
Its simple direct factors are its minimal nontrivial normal subgroups.
Indeed a normal subgroup projecting nontrivially to one simple nonabelian factor contains that factor, by taking its commutators with elements supported on the factor.
Thus \(J\) permutes the \(k\) factors by conjugation.
For odd \(k\le5\) this action gives a homomorphism of \(H\) into \(S_6\).
By the [index and permutation conclusion](Yin_C_A0341_v1.md#consequences-for-quotients-and-subgroups), its image is a cyclic group of order dividing sixteen.
All nontrivial orbits then have even length.
At least one factor is fixed since \(k\) is odd, giving a normal copy of \(S\) in \(J\), which has been excluded for both choices of \(S\).

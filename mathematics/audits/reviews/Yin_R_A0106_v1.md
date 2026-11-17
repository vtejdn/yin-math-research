---
author: Yin
---

# Matchings on marked commutator paths and their common extension

At 2026-11-17T03:30 UTC an agent outside the development of Yin_C_A0070_v1 independently reviewed its fixed statement and both proof sections for Sheng Yin.
The reviewer had previously checked the two-family tensor calculation and the disjoint cycle and path trials used in C66.
The review checked the repeated-word estimates, counting and extension on the current fixed inputs without receiving development dialogue, author explanations or a previous finding on this claim.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0070_v1.md#statement) | Fixed parameters, simultaneous fine bins, number of vertices and matchings, rank and homology, quotient safeguards and the conditional full-color extension. |
| [Whole-argument finding](#whole-argument-finding) | [Extension of matchings](../../claims/Yin_C_A0070_v1.md#extending-witnessed-matchings-on-even-blocks) | The odd-index parity calculation, alternating paths including edges crossing the marked boundary, common complement, and central comparison with a supplied full matching. |
| [Whole-argument finding](#whole-argument-finding) | [Repeated commutators](../../claims/Yin_C_A0070_v1.md#repeated-paths-with-independent-mixed-signatures-in-the-even-bins) | Cyclic reduction of each word, length and exposure budgets, conditioning, preservation of the deck indices, rank and multiplicity. |
| [Whole-argument finding](#whole-argument-finding) | [Cycle and path trials](../../claims/Yin_C_A0066_v1.md#a-grid-of-actual-commutators-in-a-four-line-tuple) | Independent neutral pools, disjoint cycles on the two sides and the index-three tensor of each double-family commutator. |
| [Whole-argument finding](#whole-argument-finding) | [Tensor convention](../../claims/Yin_C_A0066_v1.md#the-finite-tensor-calculation) | Central displacements, base paths and the domain of the balanced-word formula. |
| [Whole-argument finding](#whole-argument-finding) | [Fine counts and geometry](../../claims/Yin_C_A0054_v1.md#a-planted-binary-coordinate-which-does-not-certify-any-of-the-six-colors) | Actual \(C_{14}\) planting, even bins over left color \(3\), original group factors and typical surviving labels. |
| [Whole-argument finding](#whole-argument-finding) | [Small-target and perfection input](../../claims/Yin_C_A0061_v1.md#statement) | Applicability of the bounded-perturbation theorem to the fixed \(C_{14}\) planting and the scope of its perfect-kernel assertion. |

## Whole-argument finding

The spacer excludes the possible end cancellations not only inside \(W_i\) but also at the junction of its last and first letters.
Thus the length bound \(s(8R+12)\) applies to a freely reduced word that can be tested by fresh open paths, for fixed odd \(s=2m-1\).
The cycle search uses only the zero fine bin on each side, so the neutral pools for subsequent trials in the two left bins above \(3\) remain independent of the searches before girth conditioning.
At \(b=a/2\), the cycle success count has lower mean of order \(n^{a-b}\), which dominates \(k=\lfloor n^{a/4}\rfloor\).
Dividing the open trials among the \(k\) powers costs \(a/4\) in the exponent.
With the length and trial budget included, the total loss in that exponent is \(\delta[3/(256s)+\log(300)/(8\log64)]+o(1)<\delta/2\).
The conditional success bound remains valid after earlier failed trials because all touched vertices are marked and only \(O(n^{1-b})\) stubs have been exposed.
Binomial lower domination and a union bound therefore produce at least \(h\) disjoint simple paths per word in each bin.
The cost of girth conditioning has logarithm \(O(n^{3a/8}\log n)\), negligible against the cycle and open-path failure exponents \(n^{a/2}\) and \(n^{1-\delta/2}\).
The additional geometry, finite-target and perfection events concern the same bounded perturbation and can be intersected after conditioning.
In particular perfection concerns the kernel of the planted map onto \(C_{14}\).
At 2026-11-17T03:32 UTC the same reviewer independently checked the added corollary for quotients over the specified \(C_7\).
The image of the perfect planted kernel lies in the solvable kernel of the refinement and remains perfect, so the terminating derived series forces that image to be trivial.
The quotient therefore factors through \(C_{14}\) without an order bound, and its bins over color \(3\) have even size because they collect entire planted bins of even size.
The same parity conclusion follows for bounded-order maps by their separate factorization through \(C_{14}\), keeping the coarse color as a coordinate.

Each successful path supplies \(2m\) distinct marked vertices with the same original label.
With coherent root paths along it, the based subpath displacements are products of conjugates of commutators in the full relation group, so their first homology vanishes before quotienting deck indices.
In the mixed test both translated cycles occur at coarse index three throughout, since the words and spacers have neutral increments.
An internal pair contributes \((j-i)T_i\), and summing over a perfect matching counts each of the \(m\) odd endpoint indices once.
Each block contribution is therefore \(T_i\), independent of the matching.
There are \(h\) such blocks per \(i\), with \(h\) odd, so the total is \(\sum_i u_i\otimes v_i\).
Disjoint cycles within each side supply independent homology lists, making this diagonal sum have rank \(k\).
Each of the \(kh\) disjoint labeled blocks allows \((2m-1)!!\) choices, giving exactly the claimed lower bound on the union.

For the extension, take any full matching \(M\) and one reference matching \(P_0\) of the marked set \(Z\).
In their union, counted with multiplicity, only the outside vertices have degree one.
Every path component has two outside endpoints, including the case of a single outside edge of \(M\), and all remaining components are cycles inside \(Z\).
Transitivity of actual label equality along each such path pairs its two endpoints even when their original partners belonged to \(Z\).
The resulting outside matching depends only on \(M,P_0\) and extends every internal choice.
If constituent edges have central values of exponent two from the same displacement homomorphism, path values add and cycle values sum to zero.
The outside total is therefore \(T(M)+T(P_0)\), and every internal choice with total \(T(P_0)\) restores \(T(M)\).
Ordinary free-word concatenations can acquire fixed-root factors outside the balanced syntactic form, but these factors have trivial image under the displacement homomorphism.
For a supplied list of true equalities without witnesses the same graph construction pairs the complement by existence alone.

The high-probability assertion gives alternatives on the marked subset.
A complete matching of the whole color is a separate hypothesis in the extension argument, and the rank \(k\) is asserted for the common marked total.

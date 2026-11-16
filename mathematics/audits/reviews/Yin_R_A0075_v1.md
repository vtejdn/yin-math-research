---
author: Yin
---
# Matching presentations over a prescribed finite quotient

A separate reviewing agent inspected the complete [fixed Claim](../../claims/Yin_C_A0044_v1.md) for Yin on 2026-11-16T18:28 UTC.
The reviewer had previously checked the seven-color construction, including the source's switching and bounded-pattern inputs, in the [planted-quotient finding](Yin_R_A0072_v1.md#planted-quotient-finding).
The reviewer did not develop either construction or receive substantive development discussion, author explanations, exploration notes or prior verdicts on the present proof.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0044_v1.md#statement) | Arbitrary fixed finite quotient with a chosen surjection, finite target list, the characteristic-two witnesses and simultaneous integral projection signs. |
| [Whole-argument finding](#whole-argument-finding) | [Prescribed colors](../../claims/Yin_C_A0044_v1.md#matching-within-the-prescribed-color-classes) | Exact type counts, independent matching blocks, ordered path transport and the descended surjection. |
| [Whole-argument finding](#whole-argument-finding) | [Girth and patterns](../../claims/Yin_C_A0044_v1.md#girth-conditioning-and-bounded-patterns) | Denominator and girth constants for fixed \(m\), uniform prescription bounds and cancellation of the color factors in the stage count. |
| [Whole-argument finding](#whole-argument-finding) | [Connectedness and factorization](../../claims/Yin_C_A0044_v1.md#connectedness-and-factorization-through-the-finite-quotient) | Entropy equality, left cancellation for nonabelian targets, large cuts, small components and uniqueness. |
| [Whole-argument finding](#whole-argument-finding) | [Collected support histogram](../../claims/Yin_C_A0044_v1.md#the-histogram-after-collecting-actual-group-labels) | Nonabelian root shifts, uniform collision probability, exact and asymptotic counts, parity and integral signs after projection. |

## Whole-argument finding

At multiples of \(2v^2m\) every prescribed full type can be divided equally among all \(m\) colors.
For each oriented letter, right multiplication by its increment permutes the color set bijectively.
Consequently the \(m\) independent bijections on blocks of size \(n\rho/m\) combine into one of the permitted original matchings and are consistent with inverse reading.
A path of label \(W\) starting at color \(c\) ends at \(c\eta(W)\) in the order of traversal.
In particular every loop has trivial image, so the normal subgroup killed by coning lies in \(\ker\eta\) and the induced quotient map is onto.

The modification in the expected short-cycle count is the replacement of the linear block size \(n\rho\) by \(N=n\rho/m\).
The smaller fixed girth constant makes both the resulting expectation and the number of edges in the forbidden distance balls sublinear.
The repair switch stays in the same block, side and inverse pair.
It preserves the prescribed increments even for nonabelian \(P\).
The subexponential reverse-neighborhood bound, using \(O(n^2)\) possible transpositions per step for this fixed alphabet and \(P\), therefore survives.
With \(s\) earlier prescriptions the denominator \(N-s-O(132^{2L+2})\) also gives \(N^{-E}\exp(o(L))\) for \(E=O(L)\).
For small cuts the choice \(\lceil129k/2\rceil\le N/3\) permits the same uniform bound \(2/N\) per edge and the stated exponent \(62.5\).

For a fixed stage label string, transport from one color per component determines all vertex colors in their actual order.
A failed cycle compatibility only removes assignments.
Each unfixed vertex count decreases by a factor \(m\), including the internal-turn upper bound, by exact balance within every type.
The prescribed root costs at most one image, independently of its color.
The factor relative to the original stage bound is thus at most \(m^{E_j-V_j+b_j+k_j}\).
Here \(E_j-V_j+b_j\) is the cycle rank of the stage graph and is bounded by that of the whole image pattern for fixed pattern parameters.
Since \(m\) is fixed this factor is absorbed in the error in (3.10).
The number of permitted word strings is bounded by the original (3.11) and the number of stages remains bounded.
These are precisely the changes needed in the source bounded-pattern estimate.
The previously inspected [Ope26f geometric reduction and cone conclusions](../../literature/pdf/Ope26f.pdf#page=18) then supply torsion-freeness, the finite two-dimensional classifying space, separation at the prescribed roots and the characteristic-two zero product.

A second marking contributes the same histogram and matching entropies per planted color.
Zero exponent forces all refined types and all matching classes to be monochromatic.
Overlap of ordinary lines makes the additional marking at any vertex a function \(f(c)\) of just its planted color.
For a cut, \(f\) is invariant under the right action of the generators of \(P\), hence constant.
Thus compactness excludes positive-density closed cuts, and the small-set argument excludes the remaining possible disconnected components.
For an additional target map \(\theta\) the equation is \(f(c\eta(W))=f(c)\theta(W)\).
For \(W\in\ker\eta\) left cancellation forces \(\theta(W)=1\), giving exactly the factorization obstruction required for the compactness argument.
The union is finite since both the target list and the rank of the free group are fixed.
The homomorphism factoring a descended map through \(\pi_n\) is unique by surjectivity, also for nonabelian targets.

The first root shift gives \(c_A^{-1}c\), whereas the inverted second path label gives \(c^{-1}c_B\).
Each bijects the color set with \(P\).
At a fixed product \(g\in P\), choosing the first class \(i\) fixes the second class as \(i^{-1}g\); hence there are exactly \(m(n/m)^2\) occurrence pairs.
Uniform rooted separation in the graph law implies that the expected number of vertices sharing a group label with another vertex in their component is \(o(n)\).
Markov's inequality permits a deterministic \(o(n)\) error with probability tending to one.
Thus on connected sides each quotient class retains between \(n/m-o(n)\) and \(n/m\) distinct group labels after binary collection.
Its count remains even since deletion subtracts an even number in each class.
Using these actual counts in the ordered product formula gives \(n^2/m-o(n^2)\) cells above each quotient product, a multiple of four.
The signs assigned in opposite pairs on each true support within each \(P\)-class make each projected factor itself zero in \(\mathbb Z[P]\), so this *one* assignment works simultaneously for all homomorphisms in the assertion.
The original coefficient equations in the finer group are not addressed by that last calculation.

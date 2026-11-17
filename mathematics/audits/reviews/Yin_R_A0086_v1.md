---
author: Yin
---
# Filling length, closed range and ranks on balls of fixed radius

A separate agent reviewed the complete [fixed ledger](../../ledger/Yin_L_A0054_v1.md) for Yin on 2026-11-17T01:34 UTC.
The reviewer had worked on the earlier four-line matching law used as an input and did not develop the present geometric transfer or rank arguments.
The fixed ledger and its direct inputs were inspected without prior conclusions, author explanations or development dialogue about this argument.
Published structural theorems were checked for their statements and applicability.
Their original proofs were not re-audited.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../ledger/Yin_L_A0054_v1.md#linear-fillings-and-complex-operator-ranks-in-the-matching-groups) | All three laws, geometric bounds, closed-range integrality, fixed-matrix limit and short-factor uncertainty over fields. |
| [Whole-argument finding](#whole-argument-finding) | [Geometric input](../../ledger/Yin_L_A0054_v1.md#the-geometric-input-and-its-application-to-the-planted-laws) | Pattern-freeness at fixed bounds, the linear filling constant, marked systole and finite search. |
| [Whole-argument finding](#whole-argument-finding) | [Integral traces](../../ledger/Yin_L_A0054_v1.md#from-hyperbolicity-to-integral-traces) | Torsion-free hyperbolic assembly, matrix trace and closed-range functional calculus. |
| [Whole-argument finding](#whole-argument-finding) | [Fixed matrix](../../ledger/Yin_L_A0054_v1.md#the-rank-seen-by-a-fixed-matrix) | Local moment lower bound, inner-rank upper bound, uniform scalar limit and finite support versus analytic rank. |
| [Whole-argument finding](#whole-argument-finding) | [Small annihilator](../../ledger/Yin_L_A0054_v1.md#lifting-a-small-algebraic-annihilator) | Collision components, ordered tree transport, cycle length and transfer to an ordered free group. |
| [Whole-argument finding](#whole-argument-finding) | [Balanced planted pattern estimate](../../ledger/Yin_L_A0047_v1.md#the-bounded-pattern-estimate-with-the-seven-colors) | Rooted-pattern estimate at the specified fixed bounds for the balanced matching law. |
| [Whole-argument finding](#whole-argument-finding) | [Four-line geometric inputs](../../claims/Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts) | Degree, diameter and bounded-pattern hypotheses for the modified law. |
| [Whole-argument finding](#whole-argument-finding) | [Assembly trace](../literature/BCM04/Yin_U001.md#assembly-trace) | Range of the canonical \(K_0\) trace and specialization of the denominators to one. |
| [Whole-argument finding](#whole-argument-finding) | [Universal field](../literature/Lin93/Yin_U001.md#hughes-lewin-and-universality) | Identification of the free group's universal field with its actual affiliated division closure. |

## Whole-argument finding

The finite pattern conditions use \(2n\) total vertices, \(L\ge3\) and minimum degree at least five, all satisfied eventually.
The stated choice of \(\lambda\) bounds \(\log_2(2n)/L\), and the diameter estimate supplies the necessary fixed \(d\).
Each matching law chooses the positive error tolerance before the finite pattern bounds, so one can insert the specific triple required by the criterion without changing that tolerance.
Intersecting these events preserves conditional probability tending to one.
For a nonempty cyclically reduced trivial word the reduced cone picture cannot omit all inner disks, since that would give a free trivialization.
Each nonempty immersed cyclic inner boundary has length at least the graph girth.
The free outer-disk estimate and its area convention therefore give both \(H_0\le16|W|/(13\epsilon)\) and the lower marked-systole bound.
The finite linear filling theorem gives word-hyperbolicity of each individual finitely presented group. [MD26, Definition 3.3 and Lemma 3.5](../../literature/pdf/MD26.pdf#page=10) [MD26, reduced pictures and Theorem B](../../literature/pdf/MD26.pdf#page=13)

Distinct representatives in a ball of radius strictly less than half the systole cannot agree, since their difference reduces to a nontrivial conjugate of a cyclically reduced word below the systole.
For the effective search the finite presentation and an effective upper filling constant give a finite face bound for the specific outer word.
Counting edge occurrences on the outer boundary and on the at most \(A\) relator faces gives at most \((h+mA)/2\) unoriented edges, including an outer bridge traversed twice.
This allows enumeration of finite planar diagrams, independently of a usable running time.

Reduced assembly surjectivity applies to a finitely generated hyperbolic group with trivial coefficients.
The trace comparison then has values in \(\mathbb Z\) because every finite subgroup of the torsion-free group has order one.
The trace on a matrix projection representing a \(K_0\) class uses the unnormalized matrix trace.
A closed-range regular matrix has a spectral gap away from zero on its initial space.
Continuous functional calculus of \(A^*A\) puts the kernel projection in the reduced matrix \(C^*\)-algebra, where the trace comparison applies.
For a nonzero scalar the proper kernel projection has trace zero by integrality and faithfulness. [Lafforgue, stated hyperbolic assembly theorem](../../literature/pdf/Laf12.pdf#page=1) [BCM04, Theorem 6.3](../../literature/pdf/BCM04--author.pdf#page=19)

For fixed degree \(k\), every monomial in the moment polynomial has word length at most \(2kR\).
Eventually its regular traces agree over the free group and the quotient because every nontrivial word appearing there remains nontrivial.
The common trace increases to the free support trace as \(k\) grows, after taking the limit inferior in the quotients.
In the other direction the free group algebra is a semifir and its inner rank is preserved in its universal field.
The identification of that very field with the affiliated division closure lets ordinary reduction over the field compute the free regular rank.
A factorization over the free group algebra with that middle size descends to every quotient even when the rational row operations themselves have no specialization there.
This establishes the exact upper bound and the claimed convergence. [Lewin, §II](../../literature/pdf/Lew74.pdf#page=2) [Cohn, Theorem 7.5.13(f) and Corollary 7.5.14](../../literature/pdf/Coh06.pdf#page=474)

At fixed radius a unit sphere of coefficient vectors is compact and every point is a nonzero free scalar of rank one.
The increasing moment traces are continuous at a common norm bound, with constant limit one, so the convergence is uniform on that sphere.
The resulting choice of \(k\) works simultaneously for all coefficients once the quotient systole exceeds \(2kR\).
An annihilator on \(s\) group elements has range dimension at least \(1/s\) by the operator-norm versus \(\ell^1\) bound and trace of its initial support, independently of the distances of those elements.

For the stronger field-independent result, each coefficient fiber lies entirely within one column collision component.
Along a directed edge the multiplier of the column label is on the left.
Following a tree path therefore multiplies the edge words in reverse chronological order.
For a nontree edge and the returning tree segment the length is at most \(2R|Q|\), including parallel edges, and the product fixes its starting column under left translation.
Below the marked systole the word must already be trivial in the free group, so every nontree edge is consistent with the tree lifts.
Product images of different original fibers are distinct even after right normalization by the base column, and the factor labels themselves remain distinct within each side.
Thus a nonzero zero product would transfer to the free group algebra, contradicting its unique least product for a bi-order over any field.
Translations and reversal of the factor order preserve the asserted scope.
The convergence concerns fixed matrices or fixed support radii, and closed-range integrality alone leaves the general Atiyah question open.

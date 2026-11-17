---
author: Yin
---
# Pairing alternatives and the role of root separation in class erasure

A separate reviewing agent inspected the entire [fixed Claim](../../claims/Yin_C_A0045_v1.md) for Yin on 2026-11-17T00:35 UTC.
The reviewer had worked on a different test involving the cross-side simultaneous-step walk and had inspected the source's geometric interfaces in earlier assignments.
The reviewer did not develop the same-side forest argument, the pairing and torsion-free-quotient criterion, or the two-graph example, and received no development discussion, exploration notes, author explanation or prior verdict on those arguments.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0045_v1.md#statement) | Finite pairing alternatives, the universal torsion-free quotient, and the two-sided auxiliary example with the indicated geometric and algebraic limits. |
| [Whole-argument finding](#whole-argument-finding) | [Synchronous pairs](../../claims/Yin_C_A0045_v1.md#synchronous-components-and-protected-vertices) | Ratio invariance, ordinary two-disk obstruction, finite matching and closure tests, and predetermined-root limitations. |
| [Whole-argument finding](#whole-argument-finding) | [Torsion-free quotients](../../claims/Yin_C_A0045_v1.md#the-universal-torsion-free-quotient-for-one-pairing-alternative) | Both directions of the exact consistency criterion and enumeration of finite negative certificates for all alternatives. |
| [Whole-argument finding](#whole-argument-finding) | [Two-sided example](../../claims/Yin_C_A0045_v1.md#a-connected-aspherical-example-with-paired-erasures-on-both-sides) | Girth, immersion, topology, rooted arrangement prohibition, true and occurrence colors, and the nonzero original product. |

## Whole-argument finding

Right multiplication by a common letter preserves \(g_xg_y^{-1}\) in its given order, and immersion makes each letter a partial bijection.
Off-diagonal ordered pairs thus stay off the diagonal.
In particular a component containing a known unequal pair cannot realize any equal pair.
When the same first coordinate occurs twice on a component, cancellation on the left proves equality of the two second labels.
The case of a common second coordinate follows by cancellation on the right.

A nonempty cyclically reduced closed walk in that pair graph would project to cyclically immersed paths on both coordinates, since an inverse reading at a vertex would have to undo the unique preceding edge.
Using opposite orientations on two ordinary disks, the occurrences can be paired in their matching annular order.
At the same synchronized step the underlying edges differ because the distinct initial vertices read the same signed letter.
Thus every paired occurrence satisfies the distinct-edge condition, contradicting precisely [Ope26f, Definition 4.1](../../literature/pdf/Ope26f.pdf#page=14).
Excluding cycles gives the tree assertion, including isolated vertices.

Even multiplicity of every true label over an erased color is equivalent to a perfect pairing by equal labels, with the empty and odd-cardinality cases as stated.
For a specific pairing, equality in the original group is exactly membership of every specified difference in \(N\); separations are additional constraints.
Fundamental closed walks of both graphs in spanning trees normally generate \(N\), giving the enumeration for positive membership.
Symmetry, transitivity, simultaneous edge moves and previously proved equalities are sound finite rejections when a protected pair is forced equal.
Positive passage through those finite tests is only necessary.

For a torsion-free quotient imposing the chosen equalities, the ascending iterated root closures are killed by every map to a torsion-free group.
Their union is normal and root-closed, so its own quotient is torsion-free.
The universal quotient itself witnesses sufficiency whenever the whole root closure preserves the designated character and avoids every protected difference.
Failure gives either a word of nonzero color in the closure or a protected difference in it.
Finite words, conjugations, powers and free reductions can be dovetailed recursively at all finite stages, and every member of the union has a finite witnessed derivation.
There are finitely many perfect-pairing choices, so if all fail, enumeration can eventually exhibit all their failures.
This checks the distinction between equality in the original group and consistency after further quotienting.

In the example the words \(W_k\) have the indicated length, zero color and one occurrence of the private generator \(b_k\).
The only closed core relations are the three cycle words up to normal closure, and elimination of their private generators gives a free group.
The relative rose-with-disks model admits one elementary collapse for each such generator, establishing the stated asphericity.
The fresh edge labels give immersion at the roots, and the \(c_k\)-runs have distinct incoming and outgoing signed letters at their interiors.
No pendant addition creates a new cycle.
On each arm the bridge endpoint and final endpoint have the same group label by \(W_k=1\), whereas the intermediate colors \(k+d_k\) are all retained colors.
The sets of fresh leaves change only the desired surviving parities or add two occurrences of a retained color, so the connected sides can have equal even size.
They give exactly the claimed masks after inversion on the second side.

Every ordinary boundary in a reduced arrangement must stay in the first core and traverse some private \(b_k\)-edge, since the core with those three edges deleted is a tree.
If the exceptional path stays in the core, no different underlying edge with that signed generator can be used for pairing.
If it enters a pendant tree from its prescribed root, its bridge is crossed exactly once because an immersed path cannot return to the attachment vertex through the same tree.
That bridge's fresh letter is unavailable on any ordinary boundary or another part of the same immersed path.
The second side is itself a tree, so an exceptional path from its root has the same bridge obstruction.
This verifies the prohibition even with the exceptional interval allowed and required pairing of every occurrence.
In the free group, non-root labels on the second side contain a private uncancelled letter absent from the first side, and first-side core non-root labels are nonidentity.
Only the two roots therefore contribute to the identity coefficient of the original product, which equals one over \(\mathbb F_2\).
The example separates the root geometry from the source's type-driven cancellation and supplies no example satisfying both.

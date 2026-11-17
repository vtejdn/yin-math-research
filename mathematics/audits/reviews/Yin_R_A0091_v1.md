---
author: Yin
---
# Grading copied relators in the universal-cover homology calculation

A separate agent inspected the complete [fixed Claim](../../claims/Yin_C_A0055_v1.md) for Yin on 2026-11-17T02:08 UTC.
The reviewer previously worked on the relative-cone homology injection used as an input in L_A0052 and did not develop the vertex-potential theorem or its countermodel.
The reviewer shared the Task context and inspected the fixed proof and its direct inputs without prior review conclusions, proof-generation dialogue or author explanations on this Claim.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0055_v1.md#statement) | Opposite-side vectors, propagation, parity on auxiliary cycles, comparison of saturated matchings and finite check on supplied data. |
| [Whole-argument finding](#whole-argument-finding) | [Relative cycles and potentials](../../claims/Yin_C_A0055_v1.md#from-cycles-in-the-lifted-rose-to-vertex-potentials) | Full translated relative summands, Cayley-chain equality, synchronization and potential construction. |
| [Whole-argument finding](#whole-argument-finding) | [Several graph relations](../../claims/Yin_C_A0055_v1.md#certificates-using-several-graph-relations) | Ordering and grading of conjugate relators, cancellation of stem edges, change of witness and separation of the two sides. |
| [Whole-argument finding](#whole-argument-finding) | [Graded countermodel](../../claims/Yin_C_A0055_v1.md#a-graded-obstruction-invisible-at-the-trivial-quotient) | Its actual cone group, erasing matchings, two protected roots, complete ungraded propagated test, synchronous acyclicity and independence of the two fixed lifts. |
| [Whole-argument finding](#whole-argument-finding) | [Relative cone input](../../ledger/Yin_L_A0052_v1.md#a-homological-rejection-test-under-the-source-safeguards) | Injection from first homology of every translated coned graph into first homology of the lifted rose for the aspherical complex. |
| [Whole-argument finding](#whole-argument-finding) | [Synchronous graph input](../../claims/Yin_C_A0045_v1.md#synchronous-components-and-protected-vertices) | Relation of a cyclically reduced simultaneous walk to its two projected cyclic readings. |

## Whole-argument finding

The graded cycle and matching invariants follow with the claimed positions of the deck indices.
Each cone lifts to copies indexed by \(G\), even though the image of its boundary in the Cayley graph may identify vertices.
Their relative degree-two cycle spaces are in direct sum.
Since the universal cover is contractible, the connecting map into the ordinary cycle space of the Cayley graph is injective.
Translating the copy of the \(B\)-cone by \(g_xh_y^{-1}\) takes the start of its loop to \(g_x\).
The corresponding \(A\)-path reads the same successive Cayley edges.
For a common-step propagation, the added backward and forward Cayley edges coincide as unoriented edges since the original two vertices have identical labels.
They cancel in the binary chain.

An auxiliary edge set with even degrees sums to a closed chain in the fixed copy of \(A\).
Its image equals the sum of chains from the specified translated copies of \(B\).
Injectivity and the distinct side summands force the sum in each \(B\)-summand to be zero.
Grouping deck indices in \(Q\) preserves this conclusion.
Tree integration recovers potentials in every component, and summing their endpoint values on a matching depends only on its saturated vertices.
For an explicit certificate involving conjugates, every factor is already trivial in \(G\), so its traversed stem starts at \(g_x\) and ends at \(g_x\pi(u_j)\).
The two traversals of the stem cancel, leaving the conjugated cycle in the summand at \(g_x\pi(u_j)h_{y_j}^{-1}\) for a \(B\)-relator.
All \(A\)-relators have zero projection to the opposite-side summands.
Taking the two parallel edges from different witnesses gives their asserted proof independence.
For supplied quotient colors the finite checks require that equality of the finitely many indices that occur be supplied or decidable.
This is immediate for the concrete cyclic quotient in the example.
An arbitrary quotient specified only by words need not provide that decision procedure.

For the countermodel \(W'=U^{-1}WU\) in the free group, so the \(A\) core relator becomes trivial after killing \(W\).
The single occurrence of \(f\) in the latter relator leaves a free group after elimination.
The roots remain separated: the \(A\)-bridge contributes the private free letter \(r\) to every nonroot label, and on \(B\) only its root has color zero.
Along \(U\) the interior color is two before the last letter and along \(V\) the same is true after starting at color one, also for \(m=2\).
The three copies based at \(x_1,x_2,x_3\) and the rotated copy based at \(x_1\) have endpoints of color three.
Their interiors create no additional vertex of this color.
Every \(x_j\) has actual label \(r\).

The \(W'\)-pair at \(x_1,x_4\) cannot propagate, since their outgoing label sets are disjoint.
For the three \(W\)-pairs the common steps trace corresponding positions on consecutive arcs, with only the outgoing choice at the first end and only the incoming choice at the last end.
Thus each interior word position gives a three-vertex path in the auxiliary graph, and the endpoint edges give a four-cycle, up to repetitions of the same witness.
All these edges have the same ungraded vector and hence sum to zero on every cycle.
The two exhibited perfect matchings nevertheless have different sums with \(C_7\)-indices, because the rotated loop starts at \(B\)-color one and the other three loops start at zero.
The component core words cannot give a synchronized cross-side cycle since the \(A\)-core has both signs, and the \(B\)-core has only one sign in either direction.
Within one side the unique oriented marker per traversal determines the cyclic phase, and the signed \(a\)-counts distinguish opposite orientations, ruling out off-diagonal synchronous cycles.
In the \(B\)-only cone model the relator containing the free edge \(f\) gives an aspherical complex.
Its injection separates the three deck translates indexed by \(r,rU^{-1},1\), since their seven-colors are \(3,2,0\).
This proves independent images of the two fixed rooted lifts in the example, while the contradiction involving other deck translates detects nonasphericity of the combined complex.
The result gives a necessary test for the source matching problem and does not certify original-word equality or supply a fully erased source realization.

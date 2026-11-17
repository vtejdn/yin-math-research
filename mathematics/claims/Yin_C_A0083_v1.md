---
author: Yin
---

# Exact four-line types with an erased color and separated common-word actions

## Statement

In the [thirteen-position construction](Yin_C_A0065_v1.md#statement) fix \(k\ge1\), the given inverse pairing, the two fine-state type tables and both designated coarse-zero root states.
There are connected completions with exactly these tables, logarithmic girth, the original quotient masks \(D=\{0,1,2,4\},-D\), and full erasure of left color \(3\) in the presented group.
Each of the thirteen side and translation positions is necessary in any full erasing certificate, with at least \(2k\) pairs using each position.
On twelve actual color-\(3\) marks there are two independent six-vertex blocks with a verified common homomorphism into a finite two-group.
All \(6!\) wholly crossing matchings extend to the entire color and, in the first construction, **each crossing pair requires all thirteen positions in every proof**.
Nevertheless no common readable word interchanges any two marks of the two blocks in opposite directions, even permitting unchanged parities.
A second designated pair of blocks can have the very same thirteen original state coordinates and again have no such exchange.
For any other pair of blocks with a rank-two sum of internal parity changes detected in the same two-group, a simultaneous odd exchange is also impossible.

Here the cone group is exactly \(C_7\).
The nonzero binary factors and their zero product are in the presented group, but the group has torsion and the roots are not separated.
The complex also fails the source asphericity condition.
Accordingly these are counterexamples to forcing the indicated exchange using only the complete pairing, the prescribed types and state counts, logarithmic girth and the exhibited central data.
They leave open the implication for safeguarded torsion-free realizations.
The [torsion-free comparison with a different character and types](Yin_C_A0079_v1.md#keeping-the-old-factors-while-adjoining-trees) has a different scope.

## An additional finite action with the original vertex types

Use the [two coset actions](Yin_C_A0065_v1.md#two-actions-with-different-point-stabilizers) and keep the right side unchanged.
On the left attach to each state a coordinate in \(P\times C_3\), where \(P=U\times V\times(U\otimes V)\) for \(U=V=\mathbb F_2^2\), with the multiplication of [C66](Yin_C_A0066_v1.md#the-finite-tensor-calculation).
Choose five distinct ordinary inverse pairs outside the four selected lines, disjoint from the mixed pairs; they have trivial increments in C65.
Choose orientations and name them \(a_1,a_2,b_1,b_2,e\).
At coarse color \(3\), \(a_i,b_i\) multiply the new \(P\)-coordinate on the right by the basis vectors on the two respective axes, and \(e\) adds one to the \(C_3\)-coordinate.
At all other coarse colors these extra actions are trivial.
All other letters leave both new coordinates unchanged. Reverse letters act by inverse permutations.
The new state action is transitive: the old rotation and the two mixed letters still generate the original transitive coset action without changing the added coordinates, and at color \(3\) the designated five letters generate the new fiber.

Take sizes for which the balanced populations on the newly split states are integral, for instance sufficiently large multiples of \(2\cdot7(4k+1)^{13}\cdot |P|\cdot 3\cdot16513^2\).
Place each of C65's bounded left-side corrections entirely on the identity sheet in the new coordinates.
For the active intersection pairs, and for private-point pairs touching a changed type, the new coordinates do not move, so the old matching-block equalities still hold on that sheet.
The five new pairs meet no changed line; their blocks are exactly balanced and their permutations preserve sizes.
All other stub equalities are unchanged by the equal splitting and these corrections.
The total at each original fine state and type is exactly the prescribed one.
Every allowed two-stub turn needed below occurs with positive linear population at each specified state, by the [four-line turn count](Yin_C_A0072_v1.md#a-closed-graph-loop-changing-a-single-lamp).

Let \(F\) be the free rose group and \(N_0\) the kernel of its character onto \(C_7\).
For a word of coarse increment zero starting at coarse zero, the successive updates of \(P\) multiply to a definite element \(\rho(w)\), independently of the initial lamp, \(P\) or \(C_3\) coordinate.
This defines a homomorphism \(N_0\to P\) since the coarse state returns to zero.
Every rooted left graph loop at the designated root is killed by \(\rho\), since that root's \(P\)-coordinate returns to itself under right multiplication.
We will have \(N_0=\ker(F\to G)\), so this is an actual displacement homomorphism on the full relation subgroup of the constructed tuple.
It is not an assertion that all prescribed homomorphisms extend, as in an aspherical cone.

## Prescribing the relators and the marked paths

Put \(L=\lfloor c\log n\rfloor\) for a sufficiently small fixed \(c>0\).
Reserve disjoint simple cycles reading \(s^L,s^{L+1}\) for every generator of zero coarse change, as in [L52](../ledger/Yin_L_A0052_v1.md#a-matching-prescription-that-forces-the-equalities-in-its-own-group).
For either of the two nontrivial mixed lamps put those cycles on **its own side** in the designated coarse-zero coset, which its lamp fixes.
All other zero-increment generators can use the right base state, where their C65 actions are trivial.
On the right also reserve the three cycles \(h^Lx^7,\ h^Ly^{-1}x^2,\ h^Lz^{-1}x^4\) from L52, using a neutral ordinary \(h\) and the pure rotation increments \(x,y,z\) of respective sizes \(1,2,4\).
All three words close at the chosen right state.
These cycles force all neutral generators to die, \(y=x^2,z=x^4\), and \(x^7=1\).
The coarse character always descends onto \(C_7\), so the resulting cone group is exactly this quotient for every completion.

Choose an odd \(q\ge L\) with \(q\le L+2\).
Reserve additional disjoint cycles for the two \(a_i^q\) on the left and the two \(b_i^q\) on the right, in states above coarse zero where all their increments vanish.
Define \(M_i=[a_i^q,b_i^q]\), cyclically reduced words trivial in the cone group.
At coarse \(3\) their original lamp increments vanish.
Their action on the \(P\)-coordinate is multiplication by the independent central tensors \(E_{11},E_{22}\), since \(q\) is odd.
These are also their based displacement values under \(\rho\), since rebasing conjugates the central value by a \(P\)-coordinate and leaves it unchanged.

Let \(J\) be a product of thirteen conjugates of the two mixed generators, using pure rotations of respective shifts \(j-3\) to cover all visible side and index choices \(j\) as in [C72](Yin_C_A0072_v1.md#reading-prescribed-state-changes-and-parallel-bridges).
Reading \(J\) from coarse color \(3\) adds one to each visible lamp, and changes neither of the two new coordinates.
Its coarse increment is zero.
Use the two path words
\[
                     M_1^5\, J e\, M_2^5,\qquad M_1^5\, e\, M_2^5 .
\]
Use the reduced form of \(J\); it uses only mixed and rotation letters and remains nonempty by its state action.
Juxtaposition with the other displayed segments is free of cancellation because the five chosen pairs are distinct and exterior.
Reserve a simple path on distinct fresh vertices for each word, starting at a state over coarse color \(3\).
Mark both endpoints of each commutator copy to give six marks per block.
All the cycle and path prescriptions together have \(O(L)\) vertices, constants depending on the fixed alphabet and \(k\).
They can be embedded at fresh vertices of the required types by their positive turn pools.
No reserved stub is matched twice.

## Completions, crossing matchings and the missing safeguards

To justify connected high-girth completions, complete the remaining within-block bijections independently.
All block sizes are linear, the degree bound is \(132\), and the reserved subgraph has degree at most two and has no cycle of length below \(L\).
For \(c\) sufficiently small, the [reserved switching argument](../ledger/Yin_L_A0052_v1.md#a-matching-prescription-that-forces-the-equalities-in-its-own-group) applies on both sides with their respective fixed numbers of states.
In detail, cycles of length below \(L\) avoiding the \(O(L)\) reserved vertices have a sublinear expected total of bad edges by the linear block-size estimate.
Edges within distance \(L\) of the reserved set number \(O(L132^{L+1})=o(n)\).
Each short cycle contains an unreserved edge, and in its linear-size block all exclusions for a distant switch cost \(o(n)\) for \(132^{2L+2}=o(n)\).
The bounded inverse count gives girth-event probability \(\exp(-o(n))\).
In the conditioned law the cost of each new unreserved pair, after \(s\) further prescriptions, is at most \((N-O(L)-s-O(132^{2L+2}))^{-1}\) in a block of size \(N\).
The small-cut argument in L52 consequently still applies, since the reserved subgraph contributes at most \(2j\) edges to a set of \(2j\) vertices.
For cuts with both sides of linear size use the [strict transitive-state cut estimate](Yin_C_A0065_v1.md#safeguarded-realizations) independently on each graph, prior to reserving or conditioning.
The cost of reserving all prescribed edges is at most \(\exp(O(L\log n))\) as a factor on failure probabilities, and the subsequent girth cost is subexponential.
This yields completions with both graphs connected and the required girth.

Choose roots in the designated zero states.
All forward original labels now equal their coarse colors.
The exact original counts give the forward masks \(D\) on both sides, the actual masks \(D,-D\) after inversion, and the binary product is zero by the difference counts in C51.
Color \(3\) is completely erased, and the original C65 state coordinates still enforce all thirteen [necessary positions for a full erasure](Yin_C_A0065_v1.md#counting-the-relator-terms-of-an-arbitrary-certificate).
On the first marked path, all twelve labels agree and every crossing pair changes all thirteen old lamp coordinates, forcing all thirteen even for that one pair in every proof.
For both paths the \(P\)-value of every mark relative to the first is central.
Numbering the marks \(0,\ldots,5\), their potentials have respective increments \(iE_{11}\) and \(jE_{22}\) from each block's initial value.
Every matching of the twelve marks has actual witnesses along the prescribed path and total \(E_{11}+E_{22}\), of rank two.
The six occurrences of each constant offset cancel.
All crossing choices extend using one common matching on the complement since every remaining label count is even.

On either marked path the outer \(C_3\) coordinates of the two blocks differ by one.
Any word taking a mark back to coarse \(3\) has a single \(C_3\) translation starting at that color, independent of the mark, even if it visits other colors in between.
A bidirectional exchange would require both \(+1\) and \(-1\) in \(C_3\).
This excludes every such word, even on the second path where the two original thirteen-coordinate states agree.
More generally all coarse-\(3\) starts have the same original label, so their cyclic exchanges necessarily satisfy the [square-rank condition](Yin_C_A0075_v1.md#a-common-word-cycling-among-blocks) for this particular \(\rho\), by its elementary displacement identity without assuming asphericity.
There can be no simultaneous odd exchange for a pair of blocks having a rank-two sum detected by \(\rho\).

The root label occurs \(n/7+3\) times on each side, and the group has order seven.
The two disjoint power cycles already give the same forbidden annulus as in L52.
Thus the example tests deductions from the local type, state, pairing and girth premises while explicitly losing the root-separation, torsion-free and asphericity safeguards of the original problem.

## Assessment history

### Decision exact-types-full-erasure-comparison

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:46 |
| status | proved |
| reason | Independent review verified the original type tables, the finite action, completion with logarithmic girth, all thirteen positions and loss of the geometric safeguards. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Full erasure with both prescribed masks and verified independent block values in the comparison whose cone group is exactly C7. |
| argument | [Proof](#an-additional-finite-action-with-the-original-vertex-types) | Simultaneous finite actions, reserved relations and paths, connected completions, exchange exclusion and actual cone group. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0119_v1.md#whole-argument-finding) | Independent review of the argument and its stated scope. |

## Current assessment

[Selected decision](#decision-exact-types-full-erasure-comparison)

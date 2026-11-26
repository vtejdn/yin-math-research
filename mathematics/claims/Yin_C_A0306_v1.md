---
author: Yin
---

# All permutation images on at most seven points at cyclic orders twenty-five and twenty-six

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with a marked cyclic quotient of order \(n=25\) or \(26\), of degrees \((1,7)\) or \((1,10)\), respectively.
Suppose \(H\) acts transitively on \(d=6\) or \(7\) points, with permutation image of order at least 60.
Assume that \(t\) acts evenly and, when \(n=25\), that \(s\) acts evenly.
For \(K=B+At-s(D+Ct)\) with complex \(h\)-square corners all invertible and \(\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) invertible, the following bounds hold with unnormalized coordinate trace:
\[
\begin{array}{c|cc}
 & d=6 & d=7\\ \hline
 n=25 &37h/150&43h/175\\
 n=26 &38h/156&45h/182 .
\end{array}
\]
At \(n=26\) these bounds do not require torsion-freeness.
They include the simple group \({\rm GL}_3(\mathbb F_2)\) of order 168 in its natural action on the seven nonzero vectors, for every ordered generating pair used as the images of \(s,t\).
Indeed this group acts evenly: the elementary additions generate it by row reduction and each swaps two disjoint pairs of nonzero vectors.
In particular the bounds include its order-three second marks.

Now suppose \(H\) is torsion-free with regular injectivity for nonzero complex group-ring scalars and admits an abelian quotient of order 25 or 26.
If a complex two-square four-site rectangle has regular rank \(3/2\), every homomorphism \(H\to S_7\) has cyclic image.
Among subgroups of index between two and seven there is just the unique index-five subgroup at order 25, or the unique index-two subgroup at order 26.
The result tests genuine finite permutation images in the perfect-commutator branches without requiring scalar specialization of an affiliated inverse.

## Two optimal sets of permutation edges

Use the [integer lifts on permutation edges](Yin_C_A0293_v1.md#integer-lifts-on-individual-permutation-edges) on \(d\) sites.
Write \(x,y\) for the two permutations and \(k=7,10\) for the respective second cyclic degrees.
From site \(v\) draw edges \(v\to x(v)\) and \(v\to y(v)\) for the group translations \(s,t\), respectively.
Choose edge exponents congruent to \(c,kc\bmod n\), accordingly.
At every \(n\)-th root of the parameter \(z\) the weighted permutation factors give a genuine unitary twist and the nullity is \(d\dim_H\ker K\).
A scalar cost is the sum of the exponents of the edges used in a perfect block matching of the Laurent pencil.
Each input may first take the \(t\)-edge, then may take the \(s\)-edge from its intermediate vertex.

The resulting two sets of used edges mark an integral circulation, meaning that at every vertex as many marked edges enter as leave.
Conversely every such union of edges is attained: at each intermediate site its incoming columns and outgoing rows have the same count by conservation, and can be matched in any bijection.
Every marked edge carries one unit.
The total matching cost thus depends only on the circulation.
If an extremum is attained at a unique circulation the [invertible port blocks](Yin_C_A0293_v1.md#invertibility-when-the-extremum-has-unique-edge-sets) give a full-rank specialization.
We also use an extremum with exactly two circulations, where their difference traverses a single cycle whose ordered group word is nonidentity in the permutation image.

Here are the details for this second criterion.
Reverse exponents if necessary to use the minimum.
Choose one optimal circulation and reverse its marked edges, inverting their group translations and negating their costs.
All directed cycles in the resulting orientation have nonnegative cost, since flipping a negative cycle would improve the optimum.
Integer vertex potentials from shortest paths make all costs nonnegative.
Every directed simple cycle among the zero-cost edges produces another optimal circulation by flipping its edges.
Conversely, the difference to another optimum decomposes into directed simple zero-cost cycles by flow conservation.
Thus if there are exactly two optima, the only recurrent zero-cost edges form one directed simple cycle, precisely the difference of their masks in this orientation.

Apply the [local port reversal](Yin_C_A0226_v1.md#reversing-the-edges-of-a-minimum-circulation).
It applies to arbitrary permutations here: each site has one incoming and one outgoing edge of each label, including possible loops.
Writing \(X,Y\) for the outgoing \(t,s\) values and \(T,S\) for the respective incoming values, the local conditions are \(S=BX+AT,\ Y=DX+CT\).
The invertibility of the four corners and their assembly makes every two ports determine the other two; each individual transition block in any such local solution is invertible by the same two-port property.
Reversing a circulation preserves the count of two incoming and two outgoing ports per site, and at \(z\ne0\) is an invertible change of the local transport equations.
After the vertex potentials these equations are polynomial in \(z\).
At zero use the component order of the zero-cost edges.
Outside the sole directed cycle the homogeneous equations determine each new state from previously determined states.
On its internal port the return equation is \(\xi=Vg\xi\), with \(V\) an invertible constant matrix and \(g\) the product of the group letters read in reverse chronological order.
If its permutation is nonidentity, \(g\ne1\) in \(H\) and torsion-freeness gives infinite order.
The bilateral shift on the cyclic cosets then makes \(I-Vg\) injective, since \(\det(I-zV)\) has only finitely many zeros on the circle.
This proves injectivity of the whole zero evaluation.
The [generic rank argument for the port system](Yin_C_A0226_v1.md#why-each-recurrent-component-has-a-single-cycle) supplies a nonzero parameter with full rank for the original matching pencil.
For either criterion a certified spread \(w\) therefore gives \(dn\dim_H\ker K\le h w\) by [two-end matching interpolation](Yin_C_A0219_v1.md#statement).

## Exhausting the six- and seven-point actions

The [native certificate verifier](../computations/programs/Yin_J_A0011/verify_seven_channels.mjs) constructs \(S_d\) as permutations with ordinary composition.
It takes every conjugacy class of \(x\) and then every orbit of the even \(y\)'s under the centralizer of \(x\).
This is exhaustive up to simultaneous conjugation, which preserves the tested conditions.
It checks transitivity by closing one point under the two permutations, and determines group order by closing the identity under right multiplication.
For each transitive group below order 60 it computes successive derived subgroups by generating from all commutators until it reaches the trivial subgroup.
Thus all those omitted from the numerical bound are solvable.
No classification of transitive finite groups is used.

For every retained pair the program enumerates all \(4^d\) assignments of the two possible steps and keeps precisely those reaching distinct final sites.
It enumerates their distinct circulation masks before computing extremal costs.
The [reproduction instructions](../computations/programs/Yin_J_A0011/readme.md#six-and-seven-channels) give an option to print the chosen multiplier \(c\), a bit mask for subtracting \(n\) from the standard lifts of the \(2d\) edge costs, and the certified extremum for every representative.
Here are the orbit counts and largest verified spreads; the pairs of numbers within a cell are count and spread.

| Sites | Permutation image order | Order 25 | Order 26 |
| --- | ---: | ---: | ---: |
| 6 | 60 | 19, 37 | 19, 38 |
| 6 | 72 | 0 | 8, 38 |
| 6 | 120 | 0 | 19, 38 |
| 6 | 360 | 106, 37 | 106, 38 |
| 6 | 720 | 0 | 106, 38 |
| 7 | 168 | 114, 43 | 114, 45 |
| 7 | 2520 | 916, 43 | 916, 45 |
| 7 | 5040 | 0 | 1030, 45 |

All order-26 endpoints used a unique optimal circulation, as did all but three order-25 endpoints.
For the latter three, in one-line permutation notation on the digits starting at zero, the checked data are:

| \(x\) | \(y\) | \(c\) | Edge mask | Spread | Cycle permutation |
| --- | --- | ---: | ---: | ---: | --- |
| 023451 | 130542 | 3 | 3776 | 37 | 413520 |
| 0134562 | 1243650 | 1 | 128 | 31 | 0354162 |
| 0134562 | 2340156 | 2 | 13184 | 41 | 0561234 |

The verifier checks both optimal masks and follows their directed difference starting at its least vertex.
At each edge it acts on all digits by the permutation or its inverse according to the direction.
This checks the return word on the actual finite image as well as verifying that no differing edge is left outside the circuit.
The bounds in the statement now follow.

## Subgroups of small index

At half rank the [corner and marking theorem](Yin_C_A0201_v1.md#statement) gives the indicated marks and invertibility, and every solvable image factors through \(C_n\) by the [solvable quotient exclusions](Yin_C_A0237_v1.md#statement); the noncyclic abelian quotient at order 25 was also excluded there.
On any orbit of a permutation image under consideration, its sign is a character of \(H\).
For \(n=25\) both marks are therefore even.
For \(n=26\) the second mark is even.
Orbits of size at most five have cyclic image by the [five-point theorem](Yin_C_A0293_v1.md#statement).
On any orbit of size six or seven, a group of order below 60 is solvable by the enumeration and a group of order at least 60 satisfies the stated numerical bound.
At \(h=2\) all four bounds are strictly less than \(1/2\).
Thus every orbit action has cyclic image.
The entire permutation image embeds in their product, so is abelian and factors through \(C_n\).
Finally the action on the cosets of any subgroup of index at most seven is transitive.
A transitive cyclic permutation group acts regularly, so the subgroup is the inverse image of the unique subgroup of that index in \(C_n\).
This proves the assertions, including the existence and uniqueness at the one indicated nontrivial index.

## Assessment history

### Decision all-actions-on-six-and-seven-points

| Field | Value |
| --- | --- |
| date | 2026-11-26T15:55 |
| status | proved |
| reason | The verified matching bounds exclude all noncyclic permutation images through degree seven under the half-kernel assumptions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The verified matching bounds exclude all noncyclic permutation images through degree seven under the half-kernel assumptions. |
| argument | [Two optimal sets of permutation edges](#two-optimal-sets-of-permutation-edges) | Two optimal sets of permutation edges. |
| argument | [Exhausting the six- and seven-point actions](#exhausting-the-six--and-seven-point-actions) | Exhausting the six- and seven-point actions. |
| argument | [Subgroups of small index](#subgroups-of-small-index) | Subgroups of small index. |
| review | [All actions on six and seven points](../audits/reviews/Yin_R_A0218_v1.md#all-actions-on-six-and-seven-points) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-all-actions-on-six-and-seven-points)

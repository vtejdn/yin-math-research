---
author: Yin
---

# Small nonsolvable permutation images at the cyclic marking of order sixteen

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regularly injective nonzero group-ring scalars and a cyclic quotient of order sixteen with marked degrees \(1,6\).
For a complex two-square rectangle \(K=B+At-s(D+Ct)\) of noninteger rank, use the unnormalized regular nullity \(\delta\).
Then \(\delta\le19/40\) in each of the following cases.

* \(H\) has a nonsolvable permutation image on at most six points.
* \(H\) maps onto \({\rm GL}_3(\mathbb F_2)\), of order 168.
* Some quotient of \(H\) contains a normal subgroup isomorphic to \(A_5\).

In particular the estimate applies to every marked surjection onto \(A_5,S_5,A_6,S_6\) or \({\rm GL}_3(\mathbb F_2)\), without specifying the orders of the two images.
When \(\delta=1/2\), all homomorphisms from \(H\) to \(S_6\) have cyclic image; the only proper subgroups of index at most six are the unique ones of indices two and four.
These restrictions concern the [perfect-commutator branch](Yin_C_A0328_v5.md#statement) as well.

## The endpoint test with one possible singular corner

It suffices to consider \(\delta>7/16\).
The [corner bounds](Yin_C_A0328_v1.md#degree-lost-at-singular-extreme-corners) then give \(B,C\) invertible and at least one of \(A,D\) invertible.
The other is nonzero: if \(A=0\) the inverse transfer is affine in the cyclic parameter, and if \(D=0\) the transfer is affine in its inverse.
Its numerical values in a span of dimension two would give a constant point correspondence and force integer rank. [Nonzero corner test](Yin_C_A0328_v4.md#statement)
The assembly \({\cal P}=\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) is invertible at noninteger rank by the [four-column reduction](Yin_C_A0184_v1.md#statement).

If \(t\) acts oddly in a permutation representation, its sign character is independent of the cyclic order-sixteen character: the latter has its only binary character positive on \(t\).
Together they surject onto \(C_{16}\times C_2\), of order 32 and exponent sixteen.
The [boundary-order calculation](Yin_C_A0198_v1.md#the-two-boundary-orders) gives a lift whose width \(d\) satisfies \(4d<16\), or \(4d=16\) with both exponents nonzero.
These give \(\delta\le3/8\) and \(\delta\le7/16\), respectively, by the [one-unit mixed-end improvement](Yin_C_A0197_v1.md#a-common-deficit-at-the-roots-of-unity).
Thus the assumed range only requires representations with \(t\) acting evenly.

In any permutation action on \(d\) sites let \(x,y\) be the permutations given by \(s,t\).
For an integer \(c\) attach to each \(s\)-edge an exponent congruent to \(c\bmod16\), and to each \(t\)-edge one congruent to \(6c\bmod16\).
At each \(z^{16}=1\) the weighted permutations are the given representation tensored by a character of \(H\).
With the original regular translations retained, the resulting rectangle has nullity \(d\delta\) by [regular absorption](Yin_C_A0194_v1.md#normal-form-for-a-pair-of-unitary-matrices).

Each block matching is a path choice at every column, taking an optional \(t\)-edge and then an optional \(s\)-edge, with the final rows distinct.
Its cost is the sum of the weights on its two sets of used edges, and these are exactly the binary circulations. [Path counts](Yin_C_A0293_v1.md#integer-lifts-on-individual-permutation-edges)
Take a minimum circulation \(F\).
Its complement is a maximum, since their costs sum to the cost of all edges.
Write \(D_*\) for the spread of the two costs.
Let \(q\) be the lesser of the numbers of sites at which \(F\) uses both incident \(s\)-edges and neither \(t\)-edge, or both incident \(t\)-edges and neither \(s\)-edge.
As in the [local rank correction](Yin_C_A0328_v4.md#the-two-possible-reversal-counts), reversing the occupied edges of \(F\) uses a pivot in \(D\) at the first kind and in \(A\) at the second.
The complement exchanges these counts, so choose the corresponding end, negating all weights in the maximum case.
At at most \(q\) sites change the possibly singular corner by a rank-one perturbation to a unit.
The change can be small enough that the local assembly remains invertible.
The resulting local port equations are solvable for the new incoming pair.
Each modified evaluation has nullity at least \(d\delta-q\) at the sixteen true phases, since at each changed site the two rectangles differ by one translated block of rank one.

To check full generic rank after the perturbation, reverse the occupied edges of \(F\) in the minimum case and negate their weights.
There is no negative directed residual cycle by optimality.
Shortest-path weights at the vertices make every residual exponent nonnegative.
The edges in recurrent zero-cost components are precisely the union, over all minimizing circulations \(F'\), of their symmetric differences with \(F\), oriented in this residual graph.
Indeed each such difference is a circulation of zero cost and decomposes into directed zero-cost cycles; conversely flipping a simple directed zero-cost cycle of unit edges gives another minimum.
This includes loops and parallel edges.
In the complementary maximum case the corresponding edges and cycles are reversed, giving inverse group words.

The certificates below either have a unique optimal edge-set pair or give a union of vertex-disjoint directed simple cycles.
On each such cycle its reverse-chronological word in \(s^{\pm1},t^{\pm1}\) has nonzero degree modulo sixteen or acts nontrivially in the selected permutation action.
Its original translation therefore has infinite order by torsion-freeness.
The local return equation has the form \((I-Vg)\xi=0\) with \(V\) numerical and \(g\) that translation, so it is injective by the cyclic Fourier calculus, including for singular \(V\).
Substitution in component order gives full rank of the modified port matrix at zero, hence at a nonzero parameter by the generic polynomial rank estimate.
The modified rectangle has full rank there since the port transformations are reversible at nonzero parameters. [Single-cycle endpoint](Yin_C_A0306_v1.md#two-optimal-sets-of-permutation-edges)
Thus the [matching spread inequality](Yin_C_A0219_v1.md#statement) yields
\[
                       16d\,\delta\le2D_*+16q .
\]

## Actions and finite certificates

The [native verifier](../computations/programs/Yin_J_A0011/verify_small_permutations_sixteen.mjs) first takes every transitive pair on five and six sites with even second permutation.
It uses one first permutation of each cycle type and every allowed second permutation.
For simultaneous conjugacy it labels each graph by traversal from a chosen root, assigning new labels in the order of the first and second arrows from each visited site.
Taking the least resulting paired permutation code over all roots gives the same code precisely for isomorphic transitive marked actions.
Group order is computed by closure in the permutations; below order sixty the verifier directly computes derived subgroups to check solvability.
For seven sites it separately generates the 168 invertible three-dimensional linear transformations over \(\mathbb F_2\) on the seven nonzero vectors and includes every ordered pair generating the whole group up to this same equivalence.

The additional actions used in the enumeration are all obtained from the actual image.
On six points the action on the fifteen perfect matchings of the complete graph permutes the six partitions of its entire edge set into five such matchings.
Another action is on the ten unordered partitions of the original six points into two triples.
For \(S_5\) use conjugation on its six cyclic subgroups of order five.
For \({\rm GL}_3(\mathbb F_2)\) similarly use conjugation on its eight cyclic subgroups of order seven.
The verifier enumerates these sets before forming the two induced permutations.
No extension of a numerical representation through an affiliated inverse is required.

Here is the number of representatives using each action.
The last column is the largest \((2D_*+16q)/(16d)\) in the row, where \(d\) is the dimension of the action selected for that representative.

| Original sites | Order | Pairs | Original action | Six factorizations | Two triples | Cyclic subgroups | Largest bound |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 5 | 60 | 19 | 19 | 0 | 0 | 0 | \(19/40\) |
| 5 | 120 | 19 | 15 | 0 | 0 | 4 | \(19/40\) |
| 6 | 60 | 19 | 18 | 1 | 0 | 0 | \(11/24\) |
| 6 | 72 | 8 | 8 | 0 | 0 | 0 | \(11/24\) |
| 6 | 120 | 19 | 19 | 0 | 0 | 0 | \(11/24\) |
| 6 | 360 | 106 | 91 | 5 | 10 | 0 | \(19/40\) |
| 6 | 720 | 106 | 84 | 18 | 4 | 0 | \(19/40\) |
| 7 | 168 | 114 | 106 | 0 | 0 | 8 | \(13/28\) |

The program checks all \(4^d\) path choices in each selected action and deduplicates the used edge sets.
It tries the cost residues \(c,6c\bmod16\), changing selected edge lifts by minus sixteen and explicitly testing the two cost extrema.
For a tied minimum it checks every recurrent cycle in the union of the minimizing differences for the selected anchor, composing the actual permutations and summing the signed degrees in traversal order.
The integer test for every witness is \(40(2D_*+16q)\le19\cdot16d\); the optional witness output records the lifts, extreme circulation, repair count and spread.

## Consequences for quotients and subgroups

A nonsolvable permutation image on at most six points has a nonsolvable orbit image, since it embeds in the product of the orbit images.
Degrees at most four are solvable by the normal series of \(S_4\) through \(A_4\) and its Klein four subgroup.
The degree-five and degree-six nonsolvable orbit images therefore occur in the table.
Their second permutations are even in the range \(\delta>7/16\) by the sign argument, also applied to the orbit action itself.
The seven-point action used above is faithful for \({\rm GL}_3(\mathbb F_2)\).
This proves the first two bounds.

If an arbitrary quotient \(J\) contains a normal copy \(T\) of \(A_5\), conjugation permutes the five Sylow two-subgroups of \(T\).
In the natural five-letter model these are the Klein four subgroups fixing one letter: every involution is a double transposition with a unique fixed letter, and each such subgroup has the maximal possible two-power order four.
They are conjugate and exhaust the Sylow subgroups.
The action restricted to \(T\) is its faithful natural action, so the five-point image of \(J\) is nonsolvable.
This gives the third bound regardless of the size or centralizer of \(T\) in \(J\).

At a half kernel the [metabelian obstruction](Yin_C_A0328_v5.md#statement) gives \(H'\) perfect and \(H_{\rm ab}=C_{16}\).
A homomorphism \(H\to S_6\) now has solvable image by the first bound; its image is consequently abelian, hence cyclic and factors through \(C_{16}\).
For a subgroup of index \(d\le6\) its coset action is transitive, and a cyclic transitive permutation group acts regularly.
Thus the subgroup is normal and is the inverse image of the unique subgroup of \(C_{16}\) of the corresponding index.
The nontrivial divisors of sixteen at most six are two and four, and both subgroups exist by the cyclic quotient.

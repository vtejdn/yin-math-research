---
author: Yin
---

# True small permutation quotients obstruct all four-sign rectangles at noncyclic order twenty

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular scalar group-ring injectivity and a quotient \(Q=C_5\times C_2^2\) marked by \((1,e_1),(2,e_2)\) for a binary basis.
For a complex two-square rectangle \(K=B+At-s(D+Ct)\) of noninteger rank write \(\delta=\dim_H\ker K\), with unnormalized coordinate trace.
A nonsolvable permutation image of \(H\) on at most six points gives \(\delta\le7/15\).
A surjection onto \({\rm GL}_3(\mathbb F_2)\) gives \(\delta\le16/35\).
In particular the first estimate applies if any quotient of \(H\) has a normal subgroup isomorphic to \(A_5\), by its action on the five Sylow two-subgroups of that normal copy. [Five-point normal subgroup argument](Yin_C_A0341_v1.md#consequences-for-quotients-and-subgroups)

Both estimates use the regular operators of the original group and every genuine marked image, without a condition on the numerical character ranks of the index-four commutator.
They therefore apply also to the [rank-three or rank-four character case](Yin_C_A0343_v3.md#statement).
Combining the first bound with the [solvable-image gap](Yin_C_A0321_v1.md#statement), every nonabelian permutation image on at most six points gives \(\delta\le19/40\).
At a half kernel all homomorphisms \(H\to S_6\) have abelian image, and the proper subgroups of index at most six are exactly three of index two, one of index four and one of index five.
Each is normal.

## Two independently signed phases on the same network

For any integer pair \((a,b)\) with \(b\equiv2a\bmod5\), \(Q\) has a character with values \(z^a,z^b\) on \(s,t\) for every \(z^{10}=1\).
The fifth-primary coordinate gives the congruence and the two binary coordinates make the parities independent. [Full marking lattice](Yin_C_A0311_v1.md#the-noncyclic-quotient-of-order-twenty)
In particular, the signs of either permutation in an auxiliary action can be arbitrary.
If \(\delta>2/5\), all four corners are invertible by the [mixed order-ten endpoint comparisons](Yin_C_A0321_v1.md#reducing-a-large-fractional-nullity-to-the-split-module), and noninteger rank makes the assembly \(\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) invertible.
It suffices to consider this range, since both asserted bounds exceed \(2/5\).

More generally use any \(h\)-square coefficients with these five numerical invertibilities.
Let \(x,y\) be the permutations of the two marks on \(d\) sites.
Lift each first-edge cost to an integer \(a_i\equiv a\bmod10\) and each second-edge cost to \(b_i\equiv b\bmod10\).
At \(z^{10}=1\) the weighted permutations are the given action tensored with the marked character.
The map still carries the original translations \(s,t\) on its two kinds of edges, and by [regular absorption](Yin_C_A0194_v1.md#normal-form-for-a-pair-of-unitary-matrices) its nullity at each of the ten phases is \(d\delta\), now with \(\delta\) the nullity of the \(h\)-square rectangle.

Choose an optimal circulation of minimum cost in the unit-capacity graph on \(i\to x(i)\), \(i\to y(i)\), and let \(D_*\) be the difference of maximum and minimum cost.
The possible circulations are precisely the pairs of used edge sets of perfect block matchings. [Permutation edge sets](Yin_C_A0293_v1.md#integer-lifts-on-individual-permutation-edges)
Reverse the occupied edges.
Shortest-path potentials make all residual exponents nonnegative, and the recurrent zero-cost edges are the union of the symmetric differences with every minimizing circulation in this orientation. [Recurrent differences](Yin_C_A0341_v1.md#the-endpoint-test-with-one-possible-singular-corner)
If the union is empty the endpoint has full rank.
It also has full rank if its recurrent components are disjoint directed simple cycles and their return words have infinite order in \(H\).
Indeed every choice of two local incoming ports is solvable by the five invertibilities, and a cycle gives the single equation \((I-Vg)\xi=0\) for a numerical matrix \(V\) and the reverse-chronological product \(g\) of the original group translations.
Infinite order gives injectivity by the bilateral shift model since \(\det(I-zV)\) has constant term one.
Substitution in component order then gives injectivity at the zero endpoint and full generic rank. [Single-cycle argument](Yin_C_A0306_v1.md#two-optimal-sets-of-permutation-edges)

For such a circuit write \(i_s,i_t\) for its two signed exponent sums in the unweighted letters.
The return word is nonidentity if the composed permutation is nonidentity, or its \(Q\)-degree is nonzero:
\[
                    i_s\not\equiv0\bmod2,\quad
                    i_t\not\equiv0\bmod2,\quad\text{or}\quad
                    i_s+2i_t\not\equiv0\bmod5 .
\]
Torsion-freeness then gives infinite order.
The [matching spread inequality](Yin_C_A0219_v1.md#statement), applied at the actual ten phases, gives \(10d\delta\le hD_*\).

## Six-site images and the seven-point linear group

The [integer verifier](../computations/programs/Yin_J_A0011/verify_small_permutations_twenty.mjs) forms every transitive marked pair on five and six sites, using one first permutation per cycle type, all second permutations and the [rooted traversal criterion](Yin_C_A0341_v1.md#actions-and-finite-certificates) for simultaneous conjugacy.
It checks directly by successive derived subgroups that all generated groups below order sixty are solvable.
Each nonsolvable permutation image on at most six sites has a nonsolvable transitive orbit image, since it embeds into the product of the orbit images; degrees at most four give subgroups of the solvable \(S_4\).
The same verifier includes every generating pair of \({\rm GL}_3(\mathbb F_2)\) in its faithful action on the seven nonzero vectors, up to simultaneous conjugacy.
There are no restrictions on the orders or parities of the marks.

The following counts specify the representations used.
For five sites, the alternative action is conjugation on the six order-five cyclic subgroups.
For six sites it is the action on the six one-factorizations of the complete graph.
For the seven-point linear group it is conjugation on the eight order-seven cyclic subgroups. [Constructions of the finite actions](Yin_C_A0341_v1.md#actions-and-finite-certificates)

| Sites | Image order | Marked pairs | Original action | Alternative action | Largest \(D_*/d\) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 5 | 60 | 19 | 14 | 5 | \(7/3\) |
| 5 | 120 | 57 | 47 | 10 | \(7/3\) |
| 6 | 60 | 19 | 19 | 0 | \(7/3\) |
| 6 | 72 | 24 | 22 | 2 | \(7/3\) |
| 6 | 120 | 57 | 57 | 0 | \(7/3\) |
| 6 | 360 | 106 | 103 | 3 | \(7/3\) |
| 6 | 720 | 318 | 300 | 18 | \(7/3\) |
| 7 | 168 | 114 | 106 | 8 | \(16/7\) |

For every selected action the verifier enumerates all \(4^d\) path assignments, choosing an optional second edge and then an optional first edge for each input, and requiring distinct output sites.
It deduplicates the occupied edge-set pairs and checks the costs against all of them.
The complement of each circulation has cost equal to the sum of all edge weights minus its cost, so one minimum determines the spread.
For a tied optimum the code checks the entire recurrent union of differences against both original finite images as above.
The witnessed values yield \(\delta\le7h/30\) in the five- and six-site rows and \(\delta\le8h/35\) in the linear row, giving the stated two-square bounds.

Finally at a half kernel \(H_{\rm ab}=Q\) and \(H'\) is perfect by the [order-twenty theorem](Yin_C_A0321_v1.md#statement).
The bounds just proved force each image on at most six points to be solvable, and hence to factor through \(Q\).
The coset action of a subgroup of index at most six is transitive.
A transitive abelian permutation group acts regularly, so the subgroup is normal and corresponds to a subgroup of \(Q\) of that index.
There are three kernels of surjections to \(C_2\), the unique fifth-primary subgroup of index four, and the unique binary subgroup of index five.
These exhaust all proper possibilities up to index six.

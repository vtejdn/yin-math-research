---
author: Yin
---

# Seven-point permutation quotients at noncyclic order twenty

## Statement

Let \(H=\langle s,t\rangle\) satisfy the [noncyclic order-twenty marked hypotheses](Yin_C_A0346_v1.md#statement).
If \(H\) has any nonsolvable permutation image on at most seven points, every complex two-square rectangle of noninteger rank has regular nullity at most \(7/15\).
The same bound holds whenever any quotient of \(H\) contains a normal subgroup isomorphic to \(A_7\).
These conclusions apply irrespective of the five index-four character ranks.

A nonabelian permutation image on at most seven points gives the bound \(19/40\), by including [nonabelian solvable quotients](Yin_C_A0321_v1.md#statement).
In particular a half kernel forces every homomorphism \(H\to S_7\) to factor through \(H_{\rm ab}=C_5\times C_2^2\).
There is no subgroup of index seven, and the proper subgroups of index up to seven are exactly the five normal subgroups of indices \(2,2,2,4,5\) identified in the [six-site result](Yin_C_A0346_v1.md#six-site-images-and-the-seven-point-linear-group).

## A genuine exterior-square representation at selected phases

It suffices to treat transitive seven-point actions with nonsolvable image: a smaller nonsolvable orbit is already covered, and a group acting on a union of solvable orbit images embeds in their solvable product.
Let \(x,y\) be the marked seven-point permutations.
For an action degree \(d\) the [network estimate](Yin_C_A0346_v1.md#two-independently-signed-phases-on-the-same-network) gives \(10d\delta\le hD\) for \(h\)-square invertible corners and an invertible assembly when its endpoint test holds with cost spread \(D\).
These numerical conditions hold for the two-square application as soon as \(\delta>2/5\).

Use the given seven-site representation or the action on its 21 unordered pairs of sites.
For the latter there are two choices.
The plain action always uses unsigned permutation matrices.
For the other choice, at any \(z^{10}=1\) use the plain action if \(z^5=1\) and the second exterior power of the original permutation representation if \(z^5=-1\).
In the exterior basis \(e_i\wedge e_j,\ i<j\), a permutation \(u\) of seven sites transports the unordered pair to its image with sign \((-1)^{\epsilon_u(i,j)}\), where \(\epsilon_u(i,j)=1\) if \(u(i)>u(j)\) and zero otherwise.
Thus the edge weight \(z^{5\epsilon_u(i,j)}\) realizes exactly that selected representation at every allowed phase.
The choice is made for the entire representation at each phase.
There is no premise that individual edge signs are independent.

Tensor with an actual scalar character of values \(z^a,z^b\) for \(b\equiv2a\bmod5\), and conjugate by the site diagonal with entries \(z^{v_i}\).
In the signed pair construction the edge lifts are then congruent to
\[
             a+5\epsilon_x(i)+v_{x(i)}-v_i,\qquad
             b+5\epsilon_y(i)+v_{y(i)}-v_i \pmod{10}
\]
on the two kinds of edges, now indexing the selected sites by \(i\).
The unsigned constructions omit the two \(\epsilon\) terms.
Consequently the ten particular evaluations absorb in the regular representation exactly as before, including the original translations on every edge.
At general \(z\ne0\) these integer lifts are used as an ordinary Laurent deformation.

## Checking optimality and the recurrent group words

The [native verifier](../computations/programs/Yin_J_A0011/verify_seven_permutations_twenty.mjs) takes all seven-point transitive marked pairs, using one representative of each first-permutation cycle type, every second permutation and rooted simultaneous-conjugacy reduction.
It computes image order by closure under both generators and checks solvability of each omitted image of order below sixty by its derived subgroups.
For the remaining groups the numbers of marked classes receiving their first successful certificate from each action are as follows.

| Image order | Classes | Given seven sites | Unsigned pairs | Exterior pairs |
| ---: | ---: | ---: | ---: | ---: |
| 168 | 114 | 51 | 45 | 18 |
| 2520 | 916 | 362 | 426 | 128 |
| 5040 | 3090 | 1154 | 1467 | 469 |

For each candidate gauge the program uses centered representatives of the displayed residues.
The gauge is selected by local changes that try to reduce the sum of absolute edge weights.
The mathematical check on the resulting integer weights is independent of that search.

Start at the empty circulation of the graph with two directed edges from every site.
In the residual graph an occupied edge is reversed with negative cost.
Whenever a negative-cost directed cycle is found, reversing its occupancy preserves conservation and strictly lowers the integer cost, so the algorithm terminates.
The certificate supplies a feasible binary occupancy and integer distances satisfying
\[
                  w_{\rm res}(u,v)+d_u-d_v\ge0
\]
on all residual edges.
These inequalities certify optimality: the difference from any other feasible circulation is a sum of directed residual cycles with nonnegative cost.
If \(L\) is the certified minimum, the complement circulation has maximum cost equal to the sum of all edge costs minus \(L\).
The verifier checks that three times the resulting spread is at most seven times the action degree.

At each zero reduced-cost edge use its actual orientation and corresponding original mark or inverse.
Mutual reachability identifies all recurrent components.
The verifier requires each such component to be a directed simple cycle and checks its signed \(C_5\times C_2^2\) word degree or its reverse-chronological permutation word as in the [ten-phase endpoint proof](Yin_C_A0346_v1.md#two-independently-signed-phases-on-the-same-network).
Even in the exterior action, detection by the underlying unsigned permutation suffices: the latter is an actual action of \(H\) on its unordered pairs.
Torsion-freeness gives infinite order for the detected word.
After solving the local port equations at the chosen minimum the zero endpoint has full rank, so the two-end matching estimate applies.
All 4120 certificates have \(D/d\le 7/3\), with maximum \(49/21\).
Hence \(\delta\le7h/30\), giving \(7/15\) for \(h=2\).

## Recovering seven points from a normal alternating subgroup

Every automorphism of \(A_7\) preserves its three-cycles.
In fact the two possible cycle types of order three are a single three-cycle and a product of two disjoint three-cycles.
Their conjugacy classes in \(A_7\) have sizes 70 and 280: the \(S_7\)-centralizers have orders 72 and 18, respectively, and both contain an odd permutation (exchange two unused points in the first case and exchange the triples in the second).
The cyclic subgroups generated by single three-cycles can therefore be recognized intrinsically.
In the original model each corresponds to its supporting three-element set.

Two distinct such cyclic subgroups commute exactly when their triples are disjoint, since a commuting permutation must preserve the support of the other three-cycle.
Two different triples share two points exactly when there is one common triple disjoint from both: the complement of their union has size three precisely in that case, and otherwise has size at most two.
Thus the graph joining triples sharing two points is also intrinsic.
Its cliques of size five are precisely the five triples through each pair of points.
Indeed starting with \(\{a,b,c\}\) and \(\{a,b,d\}\), any member missing \(a\) or \(b\) confines such a clique to the four triples within \(\{a,b,c,d\}\); otherwise all members contain \(\{a,b\}\).
Two of the recovered pairs intersect exactly when their triple cliques intersect.
In this pair graph the cliques of size six are precisely the stars through a single point, since pairwise intersecting two-element sets with no common point form a triangle.
These seven stars recover the original seven-letter action equivariantly.

Consequently conjugation by any group containing a normal \(A_7\) permutes these seven intrinsic objects, with nonsolvable image since the restriction to \(A_7\) is its natural faithful action.
A quotient of \(H\) with such a normal subgroup therefore gives the required nonsolvable seven-site representation of \(H\).
Finally at a half kernel the perfect commutator and the abelianization from the [order-twenty solvable-image theorem](Yin_C_A0321_v1.md#statement) force every now-solvable \(S_7\) image to factor through \(C_5\times C_2^2\).
A transitive abelian permutation group has degree equal to its order, so no transitive seven-site representation remains.

## Assessment history

### Decision exterior-square-certificates-on-seven-points

| Field | Value |
| --- | --- |
| date | 2026-11-26T18:53 |
| status | proved |
| reason | The seven-point action and the ordinary and exterior-square pair actions give a strict bound for all nonsolvable images on up to seven points. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The seven-point action and the ordinary and exterior-square pair actions give a strict bound for all nonsolvable images on up to seven points. |
| argument | [A genuine exterior-square representation at selected phases](#a-genuine-exterior-square-representation-at-selected-phases) | A genuine exterior-square representation at selected phases. |
| argument | [Checking optimality and the recurrent group words](#checking-optimality-and-the-recurrent-group-words) | Checking optimality and the recurrent group words. |
| argument | [Recovering seven points from a normal alternating subgroup](#recovering-seven-points-from-a-normal-alternating-subgroup) | Recovering seven points from a normal alternating subgroup. |
| dependency | [Earlier result, version 1](Yin_C_A0346_v1.md#statement) | True sign lifts and the complete permutation witnesses give strict bounds in all the specified small nonsolvable images. |
| review | [Five and six point actions with independent signs](../audits/reviews/Yin_R_A0238_v1.md#five-and-six-point-actions-with-independent-signs) | Independent inspection at the scope used. |
| review | [Exterior-square certificates on seven points](../audits/reviews/Yin_R_A0238_v1.md#exterior-square-certificates-on-seven-points) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-exterior-square-certificates-on-seven-points)

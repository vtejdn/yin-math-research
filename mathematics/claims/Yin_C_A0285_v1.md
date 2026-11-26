---
author: Yin
---

# Counting free coordinates in a finite strip or a finite permutation action

## Statement

Let \(X\in M_r(\mathbb CG)\), and write \(\delta=\dim_G\ker(I-X)\) with the unnormalized coordinate trace.
For \(m\ge1\) form a graph on triples \((h,j,g)\) with \(0\le h\le m,\ 1\le j\le r,\ g\in G\).
For each \(x\) in the support of \(X_{ij}\), join \((h,j,g)\) to \((h+1,i,xg)\) whenever \(h<m\), and allow paths in either direction.
For each \(i\), partition \(0,\ldots,m\) by putting \(h,k\) together when \((h,i,1)\) and \((k,i,1)\) belong to the same connected component.
If every class in all these partitions has at most \(c\) elements, then
\[
                         \delta\le\frac{rc}{m+1}.
\]
For \(r=3,\ m=6\), a half-kernel therefore requires a path between two different levels at the same identity and coordinate, staying within these seven levels.
This test allows arbitrarily many group relations of zero net height.
It applies to the [four-binomial obstruction](Yin_C_A0266_v3.md#the-only-three-row-pattern-left) at arbitrary coefficient moduli by gauging any chosen monomial matching of its three-square lift to the identity.

There is a second bound when \(G\) acts on a finite set \(\Omega\) of size \(N\).
Take the directed graph on \((j,v)\), \(v\in\Omega\), with arrows \((j,v)\to(i,xv)\) for the same support labels.
If deleting \(b\) vertices leaves an acyclic directed graph, then \(\delta\le b/N\).
These assertions require neither scalar group-ring injectivity nor a character of \(G\).

## Comparing the copies of an eigenvector

On the finite strip take the closed space \(\mathcal L\) of strings satisfying \(f_{h+1}=X f_h\) for every \(h<m\), and let \(Q\) be its orthogonal projection.
This is the range of \(v\mapsto(v,Xv,\ldots,X^m v)\); the inverse on its image reads the zeroth coordinate.
Equivariance and polar decomposition give \(\operatorname{Tr}_G Q=r\).
Every strip equation uses only one graph component for its output and all its inputs.
Thus coordinate restriction to a component and to its complement preserves \(\mathcal L\), and \(Q\) has zero matrix coefficients between different components.

Let \(Jv=(v,\ldots,v)/\sqrt{m+1}\).
For \(v\in\ker(I-X)\) the isometry \(J\) takes \(v\) into \(\mathcal L\); hence the positive contraction \(J^*QJ\) dominates the projection onto this kernel.
At the root of input coordinate \(i\), its diagonal is \((m+1)^{-1}\|\sum_h Q e_{h,i,1}\|^2\), where the \(e\)'s denote basis vectors.
Group the sum by the indicated partition.
Different classes give orthogonal vectors and each class contributes at most \(c\sum_{h\text{ in class}}\|Qe_{h,i,1}\|^2\).
Summing over \(i\) proves the strip bound.
A quotient group may be used to certify the absence of such a path, since applying the quotient to all group coordinates preserves every edge.

For the finite-action bound twist the original regular representation by its permutation representation on \(\ell^2(\Omega)\).
The basis map \(\delta_v\otimes\delta_g\mapsto\delta_{g^{-1}v}\otimes\delta_g\) turns each diagonal translation into \(N\) copies of its original translation and fixes each basis vector with group coordinate one.
Spectral calculus and the sum of the root diagonals therefore give twisted nullity \(N\delta\).
On the complement of the deleted vertices the principal block of the twisted \(I-X\) is triangular with identity diagonal in a topological ordering.
It has a bounded inverse by finite back substitution.
The full operator thus has rank at least \(rN-b\), proving the bound.

## A marking in alternating quotients at arbitrary moduli

For each odd \(N\ge9\) take \(\Omega=\{0,\ldots,N-1\}\), \(\gamma=(0\,1\,\cdots\,N-1)\), \(c=(N-3\ N-2\ N-1)\) and \(\beta=\gamma c\), composing right to left.
Consider a gauged three-square matrix \(I-X\) in which the six off-diagonal entries of \(X\) are nonzero monomials, with zero diagonal.
Suppose a permutation action of \(G\) takes five of the corresponding labels to \(\gamma\) and the sixth to \(\beta\).
For all six complex coefficients one has
\[
                           \dim_G\ker(I-X)\le4/N<1/2 .
\]
In the directed graph remove the three vertices with permutation coordinate zero and the source state of the exceptional position at coordinate \(N-1\).
Each surviving \(\gamma\) edge increases the permutation coordinate.
The exceptional permutation agrees with \(\gamma\) except that it sends \(N-3\) to \(N-1\), \(N-2\) to zero and \(N-1\) to \(N-2\).
After the four deletions, every surviving arrow increases the coordinate.
The finite-action estimate applies with \(b=4\).

This finite labeling generates \(A_N\), even in the subgroup of closed support products of the base.
To see this, begin at the target of the exceptional edge in the contracted three-vertex graph.
There are a directed two-cycle and a directed three-cycle based there avoiding the exceptional edge, giving \(\gamma^2,\gamma^3\).
The two-cycle through the exceptional edge then gives a product of \(\gamma,\beta\), hence also \(\beta\) in the closed-product subgroup.
Diagonal matching edges have identity labels, so these contracted paths lift to closed bipartite support walks with the same products in the convolution convention.
The closed-product subgroup contains \(c=\gamma^{-1}\beta\) and all its conjugates by \(\gamma\).
The consecutive triples generate \(A_N\): the two triples on four consecutive points generate \(A_4\), since their subgroup is transitive and its order is divisible by three.
For each subsequent point, 2-transitivity of the alternating group on the preceding points conjugates the last triple to every triple containing that point.
Together with the old alternating group these generate the next one because every even permutation is a product of three-cycles.
Both original permutations are even, which proves equality.
Thus the particular finite certificate uses a perfect quotient with trivial abelianization, and its small rank bound holds for all actual group labels lifting the indicated six permutations.

## Assessment history

### Decision finite-strips-and-alternating-permutation-labels

| Field | Value |
| --- | --- |
| date | 2026-11-26T14:38 |
| status | proved |
| reason | The strip projection and the invertible triangular minor bound the actual regular nullity for arbitrary coefficients. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The strip estimate and the finite-action bound. |
| argument | [Comparing the copies of an eigenvector](#comparing-the-copies-of-an-eigenvector) | Dimensions of the solution strings and the acyclic principal block. |
| argument | [A marking in alternating quotients at arbitrary moduli](#a-marking-in-alternating-quotients-at-arbitrary-moduli) | The four deletions, the two based cycles and generation of the alternating group. |
| review | [Finite strips and alternating permutation labels](../audits/reviews/Yin_R_A0210_v1.md#finite-strips-and-alternating-permutation-labels) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-finite-strips-and-alternating-permutation-labels)

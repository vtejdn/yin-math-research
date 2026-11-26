---
author: Yin
---

# Two independent support cycles and the kernel of a scalar trinomial

## Statement

Let \(G\) be torsion-free and let \(D_G^{(3)}\) be the supremum of the regular kernel dimensions of nonzero complex group-ring scalars supported on at most three group elements.
Write \(B_G^{(2)}\) for the supremum of \((b-h)_+\) in the [two-coordinate polynomial matrix test](Yin_C_A0255_v1.md#statement) over finite matrices whose two distinguished columns are in a connected component with at most two independent cycles in the [bipartite graph of group terms](Yin_C_A0266_v1.md#statement).
Different terms at one matrix position are parallel edges.
Either supremum includes zero.
Then
\[
           B_G^{(2)}\le D_G^{(3)}\le\tfrac13 .
\]
If \(G\) is ICC, the additional inequality
\[
           D_G^{(3)}(1-D_G^{(3)})\le B_G^{(2)}
\]
holds.
In particular a positive two-cycle test in this same ICC group exists precisely when a nonzero scalar trinomial has a positive regular kernel there.
Over all torsion-free groups the two suprema are equal:
\[
               \sup_G B_G^{(2)}=\sup_G D_G^{(3)} .
\]
Every positive example on the scalar side gives its exact value of \(b-h\) on a two-by-two matrix with five group terms in a torsion-free free cyclic extension.

In the [three traceless commutator equations](Yin_C_A0254_v1.md#statement), each of the two local relation matrices has both its distinguished vertices in a single component when the bases contain the two corresponding output vectors.
That component must have at least three independent cycles on each side, without a scalar injectivity premise.
For larger cycle counts the earlier [list reduction](Yin_C_A0266_v1.md#reducing-a-support-component-to-a-list-of-rank-one-coefficients) and [ordered matching test](Yin_C_A0266_v1.md#cycles-in-a-matched-minor) remain applicable.

## Eliminating rows with two group terms

For any connected component of cycle rank at most two, its matrix rank equals \(n-\delta\) for an integer \(n\) and either \(\delta=0\) or \(\delta\) the nullity of one nonzero scalar on three sites in \(G\).
First remove isolated vertices and pivot on any leaf, counting edges with multiplicity.
The pivot is a scalar multiple of a group unit.
The residual matrix is just the matrix with the two endpoints deleted: the pivot row or the pivot column has no other term, so elimination causes no change in any remaining entry.
Each pivot contributes one to rank.
The total cycle rank cannot increase on deleting edges and vertices.

In the remaining graph every nonisolated component has minimum degree at least two.
For such a connected component of cycle rank \(c\) the sum of \(\deg(v)-2\) over all its vertices equals \(2c-2\).
Thus \(c\) equals one or two, and there is at most one component with \(c=2\).
If all rows have degree two, view them as equations on affiliated scalar column variables.
A row with terms at columns \(i,j\) gives \(x_j=m x_i\) for a nonzero complex multiple \(m\) of a group element, also permitting \(i=j\).
In each component of this graph on the column variables choose a spanning tree.
Every variable is then a scalar group monomial times a single root variable.
Every remaining row on this component gives \((1-\lambda g)x=0\) after a monomial change, for \(\lambda\ne0\).
Its coefficient is zero or an affiliated unit: for \(g\ne1\), the element \(g\) acts as a bilateral shift on its cyclic cosets.
Hence each root variable is either free or zero, so the matrix has integer rank.
This argument permits several parallel constraints on a pair and free column variables with no constraint.
The same rank assertion holds if all columns have degree two, by passing to the adjoint matrix.

The only remaining case has \(c=2\) and exactly one degree-three vertex on each side.
Indeed if degrees above two occur on both sides then they consume the entire excess two.
Delete the unique degree-three row and solve the remaining degree-two rows as above.
The solutions are parametrized by independent free root variables, with each original coordinate zero or a monomial times one of these variables.
On substituting in the deleted row, there are at most three surviving terms.
If these meet at least two free variables, at least one variable occurs just once and its monomial coefficient makes the row surjective.
If no term remains, the row has rank zero.
Otherwise a single free variable has a coefficient \(T\) supported on at most three group elements.
A zero coefficient makes no change to rank, and a nonzero coefficient contributes exactly \(1-\dim_G\ker T\), by restricting the deleted row to the already parametrized kernel.
Nonzero one- and two-site coefficients have zero kernel in a torsion-free group.
This proves the rank formula, including all components left after the leaf pivots.
For three distinct sites the [cyclic spectral inertia bound](Yin_C_A0009_v2.md#statement) gives \(\delta\le1/3\) for arbitrary complex nonzero coefficients.
It applies to the single scalar after the root-variable reduction.

## Comparing the coordinate tests

The joint increment \(h\) is the rank difference after attaching the two individual constant coordinate rows.
These add leaves to the component and preserve its cycle rank.
Other components make equal contributions to the two ranks.
The component rank formula gives \(h\) as an integer plus a difference of two numbers in \([0,D_G^{(3)}]\).
Consequently \(\operatorname{dist}(h,\mathbb Z)\le D_G^{(3)}\).
If \(b>h\), the bounds \(b\le1,\ b\le2h\) give \(0<h<1\) and \(b-h\le\min(h,1-h)\).
This proves the upper bound.
For a single distinguished row or column the same rank-difference argument excludes an increment of \(1/2\) on such a component.
The two distinguished vertices on each side of a traceless system already belong to the same component by the [joint half increment](Yin_C_A0266_v1.md#reducing-a-support-component-to-a-list-of-rank-one-coefficients), proving the stated cycle requirement.

Conversely take \(0\ne T\in\mathbb CG\) supported on at most three group elements and suppose its kernel projection \(p\) has trace \(\delta>0\).
Its three sites are distinct, since a nonzero shorter scalar has zero kernel.
Use
\[
                       L_g=\begin{pmatrix}T&0\\-g&1\end{pmatrix}
\]
with the two column coordinates distinguished.
The graph is connected, with five edges, four vertices and cycle rank two.
By the [single translated coordinate formula](Yin_C_A0264_v1.md#keeping-the-given-matrix-as-a-block), \(h=\delta\) and \(b-h=\delta-\tau(p\wedge gpg^{-1})\).
For ICC \(G\) its supremum over \(g\in G\) is at least \(\delta(1-\delta)\).
Taking suprema proves the lower bound for the original group, since \(x(1-x)\) is increasing on \([0,1/3]\).

In the torsion-free group \(G*\langle x\rangle\) take \(g=x\).
The original kernel projection is preserved by regular subgroup inclusion and is free from its conjugate by \(x\), by free product normal form.
Their traces sum to at most \(2/3\); the [free projection intersection formula](../audits/literature/CK14/Yin_U001.md#ck14-u001) gives zero meet.
The displayed matrix therefore realizes \(b-h=\delta\) exactly in this group.
Together with the upper bound this proves the equality of the unrestricted suprema.

---
author: Yin
---

# Two coordinate rank increments and matrix units in the original group

## Statement

Let \(G\) be discrete, \(U=\mathcal U(G)\), \(R\) the actual star-regular closure of \(\mathbb CG\) in \(U\), and use the unnormalized matrix trace for regular rank.
Fix \(d\ge2\).
For a rectangular \(L\) over \(\mathbb CG\) with at least \(d\) columns, let \(w_1,\ldots,w_d\) select distinct individual input coordinates and form the two real numbers
\[
 h=\operatorname{rk}\begin{pmatrix}L\\ w_1\\ \vdots\\ w_d\end{pmatrix}-\operatorname{rk}L,\qquad
 b=\operatorname{rk}\begin{pmatrix} I_d\otimes L\\ w_1\ \cdots\ w_d\end{pmatrix}
                                   -d\operatorname{rk}L .
\]
Then \(0\le b\le\min(1,dh)\).
Put \(\epsilon=dh-b\).
There is a projection \(e\in R\) with
\[
              \tau(e)\ \ge\ \max\{0,b-(d-1)\epsilon\}
                       = d\,\max\{0,b-(d-1)h\}.
\]
Whenever the right side is positive, \(eRe\) contains an algebraic \(M_d(\mathbb C)\) with identity \(e\).
For exact equality \(b=dh>0\) the construction gives \(\tau(e)=b\).

Conversely, if \(eRe\) contains such matrix units for a nonzero projection \(e\), a polynomial \(L\) and coordinate rows as above can be chosen with \(h=\tau(e)/d\) and \(b=\tau(e)\).
Thus the supremum over all polynomial tests of \(d\,\max(0,b-(d-1)h)\) is precisely the supremum of the traces of scalar corners carrying \(d\)-square units, taking zero when none exists.
In particular \(b=1,\ dh=1\) is an exact test for the unital matrix algebra in the original scalar regular closure.
For \(d=2\), absence of any strict inequality \(b>h\) is equivalent to **every projection of \(R\) being central in \(\mathcal N(G)\)**.

Consequently \(b\le h\) for all two-coordinate tests characterizes complex strong Atiyah for each individual torsion-free ICC group, and for each individual torsion-free amenable group.
More generally this same-group characterization holds for a torsion-free group whenever \(R\) has no nontrivial central projections.
Across torsion-free groups it suffices to impose the inequality just on finitely generated torsion-free ICC groups.
The test uses only regular ranks of bounded polynomial matrices without requiring a rational value for \(\operatorname{rk}L\).

## The two images of the same kernel

Let \(P\) be the projection onto \(\ker L\), viewed on right affiliated modules, and set \(A_i=w_iP\).
All matrix kernel and image projections and Moore–Penrose inverses used here lie in the corresponding matrices over \(R\), by [matrix regularity](../audits/literature/JZ19/Yin_U001.md#jz19-u001).
The two rank increments are the ranks of the stacked \(A_i\) on one copy of the kernel and of the single row of the \(A_i\) on \(d\) independent copies, by rank-nullity on the restricted kernels.
Let \(D\le P\) be the initial projection of the stacked map, so \(\operatorname{Tr}(D)=h\) and \(A_iD=A_i\).
The row \(V=(A_1,\ldots,A_d)\) on \(D^{\oplus d}\) has rank \(b\).
Its kernel within this domain is a finitely generated projective \(K\) with projection in the matrix regular closure and dimension \(dh-b\).
This proves the initial bounds.

For \(1\le i\le d\) let \(K_i\) be the submodule of \(K\) where the first \(i-1\) blocks vanish, and put \(K_{d+1}=0\).
Let \(D_i\le D\) be the image projection of the \(i\)-th block coordinate on \(K_i\).
These projections lie over \(R\), by intersection and matrix image in the affiliated algebra.
The kernel of this coordinate on \(K_i\) is \(K_{i+1}\).
Therefore \(\sum_i\operatorname{Tr}(D_i)=\epsilon\).
Remove their join from \(D\), obtaining \(F=D-\bigvee_iD_i\) with \(\operatorname{Tr}(F)\ge h-\epsilon\).
The restriction of \(V\) to \(F^{\oplus d}\) is injective: for a kernel vector, the first coordinate is in both \(F\) and \(D_1\), and once it vanishes the second belongs also to \(D_2\); continuing forces every coordinate to vanish.

Set \(X=V(I_d\otimes F)\), \(Y=X^\dagger\) and \(e=XY\).
Then \(YX=I_d\otimes F\), \(\tau(e)=d\operatorname{Tr}(F)\le b\), and \(X(E_{ij}\otimes F)Y\) give matrix units summing to \(e\) whenever \(F\ne0\).
Here \(E_{ij}\) are the ordinary scalar matrix units of size \(d\).
This gives the trace bound and equality when \(\epsilon=0\).

## Realizing a corner by polynomial equations

Start with unital algebraic matrix units in \(eRe\).
Orthogonalize their diagonal idempotents inside the corner by their increasing range flag as in the [matrix-unit orthogonalization](Yin_C_A0243_v1.md#making-the-diagonal-projections-orthogonal), obtaining \(v_{ij}\) with mutually orthogonal \(v_{ii}=p_i\) summing to \(e\).
Each \(p_i\) has trace \(a=\tau(e)/d\).
The column \(C=(v_{i1})_{i=1}^d\) has kernel \((1-p_1)U\), and its individual coordinate images are exactly \(p_iU\).
Its image projection \(P_C\) has entries in \(R\) and trace \(a\).
Apply the [polynomial graph construction](Yin_C_A0158_v1.md#group-ring-equations-for-a-regular-closure-matrix) to \(I_d-P_C\).
For an arbitrary discrete \(G\), each of its finitely many entries uses finitely many group elements and relative inverse operations and hence belongs to \(R_H\) for one finitely generated subgroup \(H\).
Subgroup inclusion preserves relative inverses by regular coset decomposition, so the polynomial graph equations constructed over \(H\) have the same affiliated solution description over \(U\).
It gives a finite group-ring system \(L\) whose kernel projected to \(d\) distinct distinguished coordinates is precisely \(P_C U^d\).
The joint image has dimension \(a\), while the sum of the individual images on independent inputs is \(eU\).
Thus \(h=a,\ b=da\), proving the converse and the supremum identity.

## Central projections and the two-coordinate inequality

If a projection \(p\in R\) fails to be central in \(\mathcal N(G)\), some group unitary \(g\) satisfies \(x=(1-p)gp\ne0\).
Indeed otherwise every \(g\) and its inverse would preserve \(p\), forcing commutation.
The relative inverse \(x^\dagger\) belongs to \(R\), and its initial and final supports are nonzero orthogonal projections below \(p\) and \(1-p\).
They and \(x,x^\dagger\) give two-square matrix units in their sum corner.
Conversely any nonzero two-square system after diagonal orthogonalization gives projections that fail to commute with its off-diagonal units and hence are noncentral in \(\mathcal N(G)\).
A projection central in \(\mathcal N(G)\) commutes with every affiliated operator.
These observations and the preceding equivalence prove the stated centrality characterization.

A nonzero singular member of the actual division closure has a nontrivial kernel projection in \(R\).
If the only central projections of \(R\) are zero and one, \(b\le h\) therefore forces the actual division closure to be a skew field.
The [complex strong Atiyah criterion](../tasks/Yin_T_A0001_v1.md#starting-references) gives the assertion for torsion-free groups; in the reverse direction a star-closed skew field is already star-regular.
An ICC group has scalar center, and for a torsion-free amenable group the [center of its star-regular closure](Yin_C_A0158_v1.md#central-cuts-in-a-torsion-free-amenable-group) is a field.
For the needed projection conclusion in a group of arbitrary cardinality, a central projection in \(R\) lies in \(R_H\) for some finitely generated torsion-free amenable \(H\) by the same finite-expression argument and is central in \(R_H\), where it is zero or one.
For the universal assertion, any failure has a finitely generated witness; its nonzero singular scalar remains singular and nonzero under inclusion into its torsion-free wreath product by \(\mathbb Z\), which is finitely generated and ICC by the [lamp and shift calculation](Yin_C_A0017_v2.md#copies-in-the-regular-representation).

## Assessment history

### Decision coordinate-increments-and-a-scalar-matrix-corner

| Field | Value |
| --- | --- |
| date | 2026-11-26T13:07 |
| status | proved |
| reason | Independent review verified the corner estimate, polynomial realization and both directions of the centrality characterization. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The corner size bound, exact converse and two-coordinate centrality test. |
| argument | [The two images of the same kernel](#the-two-images-of-the-same-kernel) | Leading-coordinate filtration, dimension losses and rectangular inverse. |
| argument | [Realizing a corner by polynomial equations](#realizing-a-corner-by-polynomial-equations) | The module of a column of matrix units recovered by polynomial coordinates. |
| argument | [Central projections and the two-coordinate inequality](#central-projections-and-the-two-coordinate-inequality) | Same-group centrality equivalence and transfer of the universal test to ICC groups. |
| review | [Coordinate increments and a scalar matrix corner](../audits/reviews/Yin_R_A0203_v1.md#coordinate-increments-and-a-scalar-matrix-corner) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-coordinate-increments-and-a-scalar-matrix-corner)

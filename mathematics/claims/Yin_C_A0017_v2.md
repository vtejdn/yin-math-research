---
author: Yin
---
# Scalar nullity gaps and exact powers in torsion-free wreath products

The [fixed-group dichotomy](Yin_C_A0017_v1.md#using-global-generation) uses journal KLS17 Theorem 3.7(3).
The following test varies the ambient group in the universal [A0001 question](../tasks/Yin_T_A0001_v1.md#contract) and uses the product trace to produce exact powers of a single nullity.
It requires neither a generation statement in \(G_0\) nor dimension-flatness.

## Statement

For a discrete group \(H\), put \(U_H=\mathcal U(H)\), \(D_H=D(\mathbb C[H],U_H)\), and write \(\nu_H\) for the regular kernel dimension with the canonical trace and unnormalized matrix trace.
Use the scalar quantity
\[
g(H)=\inf\bigl(\{1\}\cup\{\nu_H(d):0\le d\in D_H,\ 0<\nu_H(d)<1\}\bigr).
\]
For every nontrivial finitely generated torsion-free \(K\), let
\[
        W_K=K\wr\mathbb Z
        =\left(\bigoplus_{j\in\mathbb Z}K_j\right)\rtimes\langle t\rangle,
        \qquad tK_jt^{-1}=K_{j+1}.
\]
The following are equivalent.

1. Every finite matrix over the complex group ring of every torsion-free discrete group has integral regular rank.
2. For every such \(K\), \(g(W_K)>0\), with the lower bound allowed to depend on \(K\).
3. For every such \(K\), the strictly positive nullities of positive finite group-ring matrices over \(W_K\), in all sizes, have a positive lower bound depending on \(K\).

Each \(W_K\) is itself finitely generated, torsion-free and ICC.
The same equivalences hold on restricting item 1 to amenable torsion-free groups and testing only amenable \(K\) in items 2 and 3.

More precisely, suppose \(a\in D_K\) is nonzero and singular in \(U_K\), and set \(\alpha=\nu_K(a)\in(0,1)\).
There are bounded positive scalar elements \(S_n\in D_{W_K}\) of nullity exactly \(\alpha^n\) for every \(n\ge1\).
There are also positive matrices over \(\mathbb C[W_K]\) with precisely those nullities, of size \(1+nh\) for a fixed \(h\) depending on a chosen scalar realization.
If \(a\in\mathbb C[K]\), there is a separate construction of positive scalars already in the group ring with the same nullities.
If that \(a\) has a nonzero finitely supported kernel vector of minimum support size \(s\), then the minimum support size of a nonzero kernel vector of the resulting \(S_n\) is exactly \(s^n\), even though \(S_n\) itself has at most \(n|\operatorname{supp}(a^*a)|\) terms.

## Copies in the regular representation

Let \(B=\bigoplus_j K_j\).
A generating set for \(K_0\) together with \(t\) generates \(W_K\).
A finite-order element has zero height and each of its finitely many lamp coordinates has finite order in \(K\), hence is trivial.
Conjugation by \(t^k\) gives infinitely many distinct translates of any nonidentity finite lamp configuration.
For an element \(bt^m\) of nonzero height, conjugation by a fixed nonidentity lamp at site \(j\) changes the base component at \(j\) and \(j+m\).
Infinitely many such pairs can be chosen disjoint from each other and from the support of \(b\), proving the ICC assertion.
For amenable \(K\), \(B\) is a directed union of finite products of amenable groups, and \(W_K\) is an amenable extension of \(B\) by \(\mathbb Z\).

The identity coefficient gives the product trace on any finite set of distinct lamp copies, by the direct product law and the trace-preserving inclusion of a subgroup von Neumann algebra.
The subgroup inclusion extends to affiliated rings and preserves kernel and range projections, as is also seen by decomposing the regular representation into copies indexed by right cosets.
Since every inverse gate of a finite expression for \(a\) in \(D_K\) remains an actual inverse, this inclusion takes \(D_K\) into \(D_{W_K}\).
These facts use the actual group coefficients, extending the [independent lamp coordinates](Yin_C_A0005_v2.md#exact-group-ring-admissibility-and-its-limitations) from coefficient projections to rational inputs.

## Exact scalar powers

The ring \(D_K\) is closed under adjoints, by taking adjoints in finite expressions with actual inverse gates.
For \(H=a^*a\) use
\[
       b=1-(1+H)^{-1}\in D_K .
\]
Positive affiliated functional calculus gives \(0\le b\le1\) and \(1_{\{0\}}(b)=1_{\{0\}}(H)=1_{\{0\}}(|a|)\).
The inverse of \(1+H\) exists in \(U_K\) before applying division closure.
Put \(b_j=t^jbt^{-j}\) and \(S_n=\sum_{j=0}^{n-1}b_j\).
The positive summands act in distinct coordinates and commute.
A vector is in the kernel of the sum exactly when it is killed by every \(b_j^{1/2}\), by its quadratic form.
The commuting kernel projections therefore give
\[
          P_{\ker S_n}=\prod_{j=0}^{n-1}P_{\ker b_j},
          \qquad \nu_{W_K}(S_n)=\alpha^n .
\]
The kernel projections are used only for this trace computation in the von Neumann algebra.
If \(a\in\mathbb C[K]\), one may instead take \(b=a^*a\) directly, so each \(S_n\) has finite support.

## Group-ring matrices with the same nullities

Use the [finite Schur realization for a defined rational expression](Yin_C_A0012_v1.md#rational-expressions-and-explicit-polynomial-schur-realizations) with constant group-ring coefficients to write \(b=d-cL^{-1}e\), where \(L\) is \(h\)-by-\(h\) and invertible in \(M_h(U_K)\).
Conjugating every block by \(t^j\) gives \(d_j,c_j,L_j,e_j\).
With \(\mathcal L_n=\operatorname{diag}(L_0,\ldots,L_{n-1})\), let \(C_n\) be the horizontal concatenation of the \(c_j\) and \(E_n\) the vertical concatenation of the \(e_j\), in site order.
Take
\[
         Q_n=\begin{pmatrix}\sum_{j=0}^{n-1}d_j&C_n\\E_n&\mathcal L_n\end{pmatrix}.
\]
All entries are in \(\mathbb C[W_K]\) and all diagonal denominator blocks are actual affiliated units.
The upper triangular left multiplier with off-diagonal block \(-C_n\mathcal L_n^{-1}\) clears the top-right block, and the lower triangular right multiplier with off-diagonal block \(-\mathcal L_n^{-1}E_n\) clears the bottom-left block, giving \(\operatorname{diag}(S_n,\mathcal L_n)\).
Equivalently the kernel is the graph \(v\mapsto(v,-\mathcal L_n^{-1}E_nv)\) over \(\ker S_n\) on affiliated modules.
These transformations preserve the unnormalized kernel dimension.
Consequently \(Q_n^*Q_n\) is a positive finite group-ring matrix of size \(1+nh\) and nullity \(\alpha^n\).
The coefficients of all \(Q_n\) are determined by the one realization and the shifts.

## Minimum support of an annihilator

Take \(0\ne a\in\mathbb C[K]\) and use the scalar group-ring construction \(S_n=\sum_j a_j^*a_j\), where \(a_j=t^jat^{-j}\) and the sum ranges over \(0\le j<n\).
Suppose a nonzero \(z\in\mathbb C[K]\) satisfies \(az=0\), and let \(s\) be the smallest possible cardinality of its support.
Then \(s\ge2\) since a nonzero scalar multiple of a group element is a unit.
The translated copies of a minimizing \(z\) in the \(n\) distinct sites multiply to a nonzero element killed by all \(a_j\) and having support \(s^n\), by uniqueness of the coordinate tuple.

Conversely, choose any nonzero finitely supported \(x\) killed by \(S_n\).
The quadratic form of \(S_n\) gives \(a_jx=0\) for every \(j\).
Restriction to a right coset of \(K_0\times\cdots\times K_{n-1}\) on which \(x\) is nonzero reduces to a nonzero finite array on \(K^n\) with these same equations.
For any fixed values of the other coordinates, a nonzero slice in the first coordinate is a finite kernel vector for \(a\) and has at least \(s\) nonzero entries.
Choose one such slice.
At each of its at least \(s\) first-coordinate positions the slice in the remaining coordinates is nonzero and satisfies their \(n-1\) equations.
Induction gives at least \(s^{n-1}\) entries in each of these disjoint slices, proving the lower bound.
The sum defining \(S_n\) has at most \(n|\operatorname{supp}(a^*a)|\) terms.
For amenable \(K\), a nonzero regular scalar kernel supplies the initial finite kernel vector by [finite-support localization](Yin_C_A0001_v2.md#statement).
Thus mere existence of finite witnesses is compatible with this exact exponential growth in their minimum size.

## Consequence for A0001

If item 1 holds then \(D_{W_K}\) is a division ring by the torsion-free group-ring rank criterion, so \(g(W_K)=1\), and positive matrix nullities are integers. [Lück and Linnell, Theorem 2.3(3)](https://arxiv.org/pdf/1602.06906v3#page=10)
If item 1 fails, pass to the torsion-free finitely generated subgroup \(K\) generated by the supports of the exceptional matrix.
Restriction to right cosets preserves its regular rank, and the trivial group has integral ranks.
The same rank criterion implies that \(D_K\) is not a division ring.
Its published right-multiplication formulation transfers to the present left convention by transposing the matrix and applying the trace-preserving group anti-isomorphism \(g\mapsto g^{-1}\) to its entries.
Its actual inverse closure ensures a nonzero element \(a\) without a \(U_K\)-inverse.
Faithfulness and finiteness give \(0<\nu_K(a)<1\), so the constructions above violate both items 2 and 3 in the one group \(W_K\).
They also give a dense set of matrix nullities after taking finite direct sums, since multiples of \(\alpha^n\) approximate every nonnegative real as \(n\) grows.
For the amenable statement, subgroups preserve amenability and the wreath-product construction stays in the same class.

In particular an independent group-dependent lower bound on this test family would suffice for the full conjecture.
A bound decreasing with matrix size, support or rational expression length needs quantitative comparison with \(\alpha^n\).
For example, if independently proved positive lower bounds \(\epsilon_n\) on the nonzero nullities of these particular matrices satisfy \(\limsup_n\epsilon_n^{1/n}=1\), no \(\alpha\in(0,1)\) can produce them.
This is a criterion for further estimates and supplies no such lower bound.
The construction changes \(K\) to \(W_K\) and makes no assertion that \(G_0(D_{W_K})\) is cyclic or that KLS17's implication holds in either group.

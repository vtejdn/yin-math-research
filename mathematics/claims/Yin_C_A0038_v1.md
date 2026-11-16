---
author: Yin
---
# Lifting a characteristic-two group-ring zero product with fixed supports

## Statement

Let \(A,B\) be finite nonempty sets of distinct elements of a discrete group \(G\).
For \(w\in AB\) write \(F_w=\{(x,y)\in A\times B:xy=w\}\).
Suppose each \(|F_w|\) is even, so the two all-ones factors on these supports have zero product over \(\mathbb F_2\).
Choose \(x_0\in A,y_0\in B\), and normalize the coefficients there to one.

1. The given point lifts to a full-support zero product over \(\mathbb Z/4\) if and only if every union of whole fibers which has even degree at every vertex of the bipartite graph on \(A\sqcup B\) has a number of cells divisible by four.
2. At every subsequent level the lift of a specified solution modulo \(2^n\) to one modulo \(2^{n+1}\) is governed by the same binary incidence matrix, with a right-hand side computed from the specified solution.
   Lifts modulo \(2^n\) for arbitrarily large \(n\), whether initially given compatibly or not, imply a full-support complex zero product on exactly \(A,B\).
   For torsion-free \(G\) this would refute [A0001](../tasks/Yin_T_A0001_v1.md#contract) already for a scalar operator.
3. For the source construction Ope26f there is also a sufficient system on graph vertices and simultaneous-step components.
   Its first right-hand side has a formula in terms of an orientation of the label pairs and the prescribed vertex types.
   No orientation makes the resulting pair function a sum of a row function and a column function pointwise on the full prescribed type family.

These statements use one residue characteristic and impose no amenability hypothesis.
The [rank transfer across increasing characteristics](Yin_C_A0029_v1.md#statement) controls prescribed limiting ranks on fixed amenable supports.

## The incidence matrix and lifting

Write the group-ring coefficient polynomials as \(P_w(U,V)=\sum_{(x,y)\in F_w}U_xV_y\).
Let \(D\) over \(\mathbb F_2\) have one row per product and one column per row or column vertex.
Its entry is the number of cells of the fiber incident to that vertex, reduced modulo two.
Each fiber is a partial matching by group cancellation.
For the normalized system remove the columns indexed by \(x_0,y_0\).
This leaves the column space unchanged, since the sum of the \(A\)-columns, and separately the sum of the \(B\)-columns, is zero by evenness of every fiber.
Thus both normalizations can be imposed simultaneously.
Over every ring \(\mathbb Z/2^n\), odd coordinates are units, so rescaling the two coefficient vectors separately also gives these normalizations.

An odd lift modulo four has \(U_x=1+2s_x,\ V_y=1+2t_y\).
Expansion gives
\[
      D(s,t)_w=|F_w|/2\pmod 2.                                         \tag{1}
\]
For a set \(W\subset AB\) of fibers the sum of its incidence rows is zero precisely when every vertex has even degree in \(\bigcup_{w\in W}F_w\).
This remains true with the two columns deleted by the column relations just verified.
Binary linear duality says that (1) is solvable exactly when every such row dependence annihilates its right-hand side.
This is the stated divisibility by four.
The dependence can also be certified from a homomorphism on \(G\), by taking \(W\) to be the preimage in \(AB\) of any selected set of quotient products and verifying the two parity conditions on that union.
The whole rectangle alone never obstructs this lift, since even degree at every vertex makes both side sizes even and their product divisible by four.

For \(n\ge1\), take integer representatives \(u,v\) of a normalized solution modulo \(2^n\) reducing to the all-ones point.
All the \(P_w(u,v)\) are multiples of \(2^n\).
Set \(U=u+2^ns,\ V=v+2^nt\).
Since \(2n\ge n+1\) and the old coordinates are odd, the complete condition is
\[
      D(s,t)_w=-P_w(u,v)/2^n\pmod 2.                                  \tag{2}
\]
Changing representatives merely translates the correction variables.
Surjectivity of the normalized \(D\) suffices at every level.
More generally, normalize first and select a subset of equations whose incidence rows are independent.
If every omitted equation is in the ideal of the selected equations over \(\mathbb Z_{(2)}\) in the normalized Laurent polynomial ring, solving the selected equations at each level suffices.
Indeed the selected matrix is surjective onto its row-indexed target, and every inverse used in the indicated polynomial identities is a unit on odd inputs.
An implication proved only after division by two does not give this conclusion.
Linear dependencies among the rows alone do not imply the needed polynomial identities.

The solutions of the normalized full system reducing to the fixed point form a finitely branching tree under reduction.
If its levels are nonempty at arbitrarily large depths, choose a child with descendants at arbitrarily large depths, repeatedly starting at the fixed root.
The resulting branch gives odd coefficients in \(\mathbb Z_2\) annihilating every \(P_w\), since \(\bigcap_n2^n\mathbb Z_2=0\).
The field generated over \(\mathbb Q\) by the finitely many coordinates in \(\mathbb Q_2\) embeds abstractly in \(\mathbb C\).
Indeed one can send a finite transcendence basis to algebraically independent complex numbers and extend across the resulting finite algebraic extension.
All coordinates survive, giving \(a,b\in\mathbb C[G]\) on the prescribed supports with \(ab=0\).
The nonzero vector \(b\delta_e\) lies in \(\ker\lambda_G(a)\), and \(a\delta_e\ne0\).
The kernel projection and its complement are therefore both nonzero, so faithfulness of the finite trace gives \(0<\tau_G(p_a)<1\).

A failed row-dependence test also excludes a lift of this residue point modulo four over the integers of an unramified finite extension of \(\mathbb Q_2\).
In that ring the element \(2\) generates the maximal ideal, and the same row dependence gives \(0=1\) in the residue field.
In a ramified extension, a coordinate congruent to one modulo the maximal ideal need not have the form \(1+2s\).
Failure of (1) does not decide existence of a general characteristic-zero solution.

## A three-fiber obstruction

Take \(G=(\mathbb Z/2)^3\) additively and \(A=B=\{0,e_1,e_2,e_3\}\) for a basis \(e_1,e_2,e_3\).
The fiber of zero consists of four diagonal pairs.
The other six fibers are the two orderings of each pair of distinct vertices, since all their unordered sums are different.
Choose the three off-diagonal fibers for the three unordered pairs in \(\{0,e_1,e_2\}\).
Their six cells have degree two at each chosen vertex on each side and degree zero elsewhere.
As \(6\not\equiv0\bmod4\), (1) fails on this actual all-even table.
Equivalently the three double equations require three nonzero ratios \(U_i/V_i\) to be pairwise negatives of each other, which is impossible over \(\mathbb C\).
This finite group calibrates the lifting obstruction and has torsion.

## The simultaneous-step system in Ope26f

In [Ope26f, pp. 2–4](../literature/pdf/Ope26f.pdf#page=2), the two supports in formula (1.1) are initially given as sums over vertex occurrences \(x,y\) in specified root components, with labels \(g_x,h_y^{-1}\).
The authors prove that no non-root vertex of either selected component contributes to the identity of its factor.
Their factor-survival argument requires no distinction between the labels of two non-root vertices.
To apply (1) to the actual supports of the two \(\mathbb F_2[G]\) elements, first collect equal group labels on each side, keep their odd-multiplicity classes and form their actual group-product fibers.

There is a different sufficient test using the two occurrence sets as the variables.
Index equations by the connected components \(C\) of the simultaneous-step graph on their product.
Each \(C\) has even cardinality by the source's odd-degree argument and maps to a single group product.
The expansions (1)–(2) and the finite-tree proof still hold with \(C\) in place of \(F_w\), counting every incidence with its multiplicity, since they used only even cardinality and the sums of the corresponding bilinear terms.
Lifting all these equations to every level again gives a complex group-ring zero product, since collecting equal products sums equations over whole components and the two unique root coefficients survive.
Other group labels can merge or acquire nonzero coefficients after lifting, so this conclusion on occurrences does not prescribe the two supports after collection.
An obstruction for the component equations alone need not obstruct the coarser group-product equations.

Orient each inverse pair of signed labels by selecting one of its members in a set \(T_+\).
Let \(I_t(x)\) indicate that vertex \(x\) has outgoing label \(t\), and let \(E_x\) indicate a nonempty extra part in its prescribed type.
Define over \(\mathbb F_2\)
\[
       W_{xy}=\sum_{t\in T_+} I_t(x)I_t(y)+E_x E_y .
\]
Each unoriented simultaneous-step edge in a component is counted exactly once at the endpoint reading its chosen signed label, with the same count convention for a loop.
The ordinary projective lines of a vertex pair meet in one point, or in 129 points when identical.
The extra intersection has size \(2E_xE_y\), since a nonempty extra set has size two on the first side and is the set of all three extras on the second side.
Hence \((\deg(x,y)-1)/2\equiv E_xE_y\bmod2\).
Subtracting \(\sum_{(x,y)\in C}(\deg(x,y)-1)/2\) from the number of edges of \(C\) gives \(|C|/2\) by the degree sum.
Thus \(\sum_{(x,y)\in C}W_{xy}=|C|/2\bmod 2\), the desired right-hand side.

If \(W_{xy}=s_x+t_y\) pointwise on all types, their vertex functions would provide a matching-independent solution of (1) on every component.
This ansatz already fails on the empty-extra types.
Choose one vertex of each such type on each side and index by its ordinary line.
For distinct lines \(L,M\), the entry \(W_{LM}\) is the selection bit for their unique intersection point, and is symmetric in \(L,M\).
Additive separation would imply \(s_L+t_L=c\) independent of \(L\), so \(W_{LM}=c+t_L+t_M\).
For a given ordinary point any three distinct incident lines give the same value for all three off-diagonal entries.
Their three \(t\)-values must then agree, and that point's selection bit must be \(c\).
All ordinary points would have the same selection bit, impossible since some ordinary letters form inverse pairs and exactly one of each pair belongs to \(T_+\).

This excludes the pointwise orientation construction on the full prescribed type family.
The source gives the component parities for characteristic two, while the test modulo four also needs the incidences of vertices in unions of components or in actual product fibers.
The argument does not decide whether the selected graph components or the merged group table pass that test.
It tests a different condition from the [complex rank calculation for weighted common-label degrees](../ledger/Yin_L_A0034_v1.md#rank-on-all-prescribed-types).

## Assessment history

### Decision binary-lifting

| Field | Value |
| --- | --- |
| date | 2026-11-17T01:56 |
| status | proved |
| reason | Independent mathematical review covers the statement, argument and their stated limitations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Unramified lifting of the fixed characteristic-two point, the implication of arbitrarily deep lifts and the stated graph-type obstruction. |
| argument | [Proof](#the-incidence-matrix-and-lifting) | Complete argument with its actual hypotheses and scope. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0069_v1.md#whole-argument-finding) | Independent review of the proof and its direct inputs. |

## Current assessment

[Selected decision](#decision-binary-lifting)

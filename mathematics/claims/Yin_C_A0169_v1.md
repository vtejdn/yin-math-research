---
author: Yin
---

# Subgroup descent in the affiliated division closure of a free group

## Statement

For a discrete group \(K\), let \(U(K)\) be its affiliated algebra in the left regular representation and \(D(K)\) the scalar division closure of \(\mathbb CK\) in \(U(K)\).
For every subgroup \(J\) of a free group \(F\), under the canonical subgroup embeddings,
\[
                       D(F)\cap U(J)=D(J).
\]
Each element of this intersection already belongs to \(D(J_0)\) for a finitely generated subgroup \(J_0\le J\).

Consequently, in a torsion-free ambient group the [order-two character endpoint](Yin_C_A0168_v1.md#statement) cannot occur when the shortened subgroup \(K\) is free.
Precisely, assume a character is trivial on \(K\) and sends the appended label \(s\) to \(-1\), with integral ranks for the shortened pencils required there.
No pencil \(L\) on the longer list and constant output column \(\alpha\) can have \(\operatorname{rk}[L,\alpha]-\operatorname{rk}L=1/2\).
This eliminates that endpoint even when \(K\cap g^{-1}Kg\) is infinitely generated.

## Finite index and free factors

For a subgroup inclusion, the subgroup's regular operators act identically on its right cosets, giving the normal trace-preserving embedding and its extension to affiliated algebras.
Spectral supports and actual inverses are preserved and reflected.
In particular \(D(J)\subset D(F)\cap U(J)\).

First let \(H\le F\) have finite index \(n\).
Use representatives \(s_1=1,\ldots,s_n\) of the left cosets, and identify \(\ell^2(F)\) with \(n\) copies of \(\ell^2(H)\) by \(\delta_{s_i h}\leftrightarrow\delta_h\) in copy \(i\).
Each translation by \(g\in F\) becomes a permutation matrix with entries given by translations by \(s_j^{-1}g s_i\in H\) where \(g s_i H=s_jH\).
This gives a normal unital embedding of \(\mathcal N(F)\) into \(M_n(\mathcal N(H))\), and the same identification by spectral calculus embeds \(U(F)\) into \(M_n(U(H))\).
The subgroup \(H\) is free, as follows from its covering graph of the basis rose.
Thus \(D(H)\) is a division ring by the [free-group result](../audits/literature/Lin00/Yin_U004.md#the-division-ring-and-free-field-assertions-are-separate).
Any matrix over \(D(H)\) which is invertible over \(U(H)\) has its inverse over \(D(H)\), since singularity over this division ring would give a nonzero kernel column that survives over \(U(H)\).
It follows by induction over scalar inversions that every member of \(D(F)\) maps into \(M_n(D(H))\).
For \(x\in U(H)\) its copy on \(\ell^2(H)\) reduces the embedded operator and recovers \(x\) as the first diagonal entry.
For bounded subgroup operators this follows directly by translation, and for the affiliated case it follows by spectral truncation and polar decomposition.
Consequently \(D(F)\cap U(H)=D(H)\).

Next let \(H\) be free of finite rank and let \(J_0\) be a free factor.
Choose a basis of \(H\) extending a basis of \(J_0\). A trivial factor gives the scalars.
For \(X=H,J_0\) write \(P_X\) for the rooted tree unitary sending a non-root vertex to its last edge on the path from the identity and the root to the auxiliary scalar coordinate.
Write \(\widehat a_X\) for the edge amplification of a bounded coefficient followed by direct sum with \(I_{\mathbb C}\), in the [fraction-test conventions of Lin00](../audits/literature/Lin00/Yin_U001.md#lin00-fraction-tests).
The Cayley subtree on \(J_0\) is convex in the tree of \(H\).
Thus \(P_H\) and \(P_H^{-1}\) restrict to \(P_{J_0}\) and \(P_{J_0}^{-1}\) between the subgroup vertex space and its edge space enlarged by the same scalar coordinate.
Both subspaces reduce the respective vertex and edge actions of all coefficients in \(\mathcal N(J_0)\).
For edges this follows first from permutation by \(J_0\) and its inverses on the subtree and its complement, then by normality on the edge summands. The scalar action is the identity in both tests.

Let \(x\in D(H)\cap U(J_0)\) and take bounded left and right fractions \(x=s^{-1}a=bt^{-1}\) with \(a,b,s,t\in\mathcal N(J_0)\) and affiliated-unit denominators.
Such fractions exist by the [bounded fraction construction](../audits/literature/Lin00/Yin_U001.md#bounded-fractions-and-common-denominators), and remain legitimate in \(H\).
By [Linnell, Theorem 1.1](https://arxiv.org/pdf/math/9907075#page=3), both bounded defects
\[
 \widehat s_H P_H b-\widehat a_H P_H t,\qquad
 sP_H^{-1}\widehat b_H-aP_H^{-1}\widehat t_H
\]
have finite rank for this pair, because the theorem gives the tests for every pair in \(H\).
Their restrictions to the two indicated subspaces are exactly the corresponding two defects for \(J_0\), hence both have finite rank.
The converse direction for a single legitimate pair on \(J_0\) now puts \(x\) in \(D(J_0)\).

For a finitely generated \(J_0\le F\) with \(F\) free of finite rank, take the union of based loops reading a finite generating set in the Schreier cover \(J_0\backslash F\) of the finite basis rose.
The resulting finite connected labelled graph has based loop subgroup \(J_0\), since all its loops lie in \(J_0\) and the chosen ones generate it.
For every positive basis letter, the existing edges specify a partial permutation of the vertex set.
Pair the missing outgoing and incoming slots to complete a permutation, giving a finite connected cover on the same vertices.
Its based subgroup \(H\) has finite index in \(F\).
A spanning tree in the original graph is still spanning in the completion, so its non-tree edges give a subset of the basis arising from all non-tree edges of the cover.
This makes \(J_0\) a free factor of \(H\).
The two preceding arguments give the required intersection for \(J_0\).

## Bounded Fourier coefficients and a finite subgraph

For the moment suppose \(F\) has finite rank and \(J\le F\) is arbitrary.
Let \(u\in D(F)\cap\mathcal N(J)\).
By Linnell's bounded intersection in [Theorem 1.1](../audits/literature/Lin00/Yin_U001.md#lin00-fraction-tests), \(u\) belongs to the scalar inverse closure of \(\mathbb CF\) in its reduced group \(C^*\)-algebra.
The [Duchamp-Reutenauer Fourier-series criterion](../audits/literature/DR97/Yin_U003.md#statement-and-hypotheses) makes the series of Fourier coefficients on reduced basis words, extended by zero on nonreduced words, recognizable.
By the [finite-alphabet residual criterion](../audits/literature/DR97/Yin_U001.md#statements-and-their-precise-scope), all its prefix residuals lie in a fixed finite-dimensional vector space.
The Fourier support lies in \(J\), by the subgroup expectation.

If \(w\) is a prefix of a supported word, its residual \(v\mapsto\widehat u(wv)\), with the stated zero extension, is nonzero.
A nonzero coefficient forces the group element represented by \(v\) to lie in \(w^{-1}J\).
Prefixes visiting different vertices \(Jw\) in the Schreier graph have disjoint inverse cosets \(w^{-1}J\), and hence their residuals have disjoint word supports.
Any such family of nonzero residuals is linearly independent.
Only finitely many vertices are therefore visited by prefixes of all supported words.
The basis alphabet is finite, so the union of the corresponding paths is a finite connected based subgraph when the support is nonempty.
Each supported word ends at the basepoint and belongs to the label subgroup of the loops of this subgraph.
That subgroup is finitely generated by its non-tree edges and lies in \(J\).
This also holds for empty support with the trivial subgroup.
It follows again by the subgroup expectation that \(u\) lies in the group von Neumann algebra of a finitely generated subgroup of \(J\).

For \(x\in D(F)\cap U(J)\), put \(y=(1+x^*x)^{-1}\) and \(z=xy\).
Adjoint closure puts both in \(D(F)\), and boundedness in \(\mathcal N(J)\) follows from the scalar functions \(1/(1+r^2)\) and \(r/(1+r^2)\) in polar decomposition.
Take \(J_0\le J\) generated by the two finite generating sets obtained for \(y,z\).
Since \(y\) is an affiliated unit, \(x=zy^{-1}\) lies in \(U(J_0)\).
The finitely generated subgroup case gives \(x\in D(J_0)\).

Finally if \(F\) has an infinite basis, any one expression producing \(x\in D(F)\) uses only finitely many basis letters from group-ring inputs.
It defines the same element in the algebra of the finite-rank free factor \(F_0\) on those letters, because subgroup embeddings reflect affiliated invertibility.
For arbitrary subgroups \(B,C\), their bounded group algebras inside the ambient von Neumann algebra satisfy \(\mathcal N(B)\cap\mathcal N(C)=\mathcal N(B\cap C)\) by Fourier support and expectation.
Their affiliated algebras satisfy the analogous equality by applying the bounded transform and its spectral recovery, as in the [subgroup intersection for the norm equation](Yin_C_A0168_v1.md#complementary-eigenmodules-and-a-relative-norm).
Thus \(x\in D(F_0)\cap U(F_0\cap J)\), and the finite-rank case applies.
All uses of the finite-alphabet and tree tests above concern free groups of finite rank.

## Excluding the order-two endpoint

If the half increment occurred, the [relative norm calculation](Yin_C_A0168_v1.md#complementary-eigenmodules-and-a-relative-norm) would give \(g\in Ks\), \(g^2\in K\) and a unit \(b\in D(K)\cap U(J)\) for \(J=K\cap g^{-1}Kg\), normalized by \(g\), such that \((g b g^{-1})b=g^2\).
Taking \(F=K\) in the intersection result gives \(b\in D(J)\).
The character separates \(g\) from \(K\), and \(g^2\in J\), so \(J\triangleleft L=\langle J,g\rangle\) with \(L/J\cong C_2\).
The subgroup \(J\) of the free group \(K\) is free and \(L\) is torsion-free by the ambient hypothesis.
[Linnell, Theorem 1.3](../audits/literature/Lin93/Yin_U001.md#lin93-u001) supplies a division ring between \(\mathbb CL\) and \(U(L)\) for a torsion-free group with normal free subgroup and elementary amenable quotient.
Inside it the ring \(D(L)\) is a division ring, and it contains both \(D(J)\) and \(g\).
The norm identity reads \((g^{-1}b)^2=1\) there.
Factoring \(X^2-1\) in the element \(X=g^{-1}b\) gives \(b=\pm g\).
This contradicts \(b\in U(J)\), since a bounded operator of \(U(J)\) lies in \(\mathcal N(J)\), whereas \(g\delta_1=\delta_g\) is supported outside \(J\).
The [general complex Atiyah question](../tasks/Yin_T_A0001_v1.md#contract) still allows nonfree shortened subgroups and other rank increments.

## Assessment history

### Decision free-subgroup-intersection

| Field | Value |
| --- | --- |
| date | 2026-11-26T03:47 |
| status | proved |
| reason | Independent review verified the complete argument and its stated hypotheses. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Descent for every subgroup of every free group and the order-two endpoint application. |
| argument | [Finite index and free factors](#finite-index-and-free-factors) | Matrix restriction, two tree tests and finite completion of a basis cover. |
| argument | [Finite subgraph](#bounded-fourier-coefficients-and-a-finite-subgraph) | Recognizable reduced-word Fourier series, distinct cosets and unbounded fractions. |
| argument | [Local norm exclusion](#excluding-the-order-two-endpoint) | Linnell's theorem on the torsion-free index-two extension. |
| review | [Free subgroup intersection](../audits/reviews/Yin_R_A0175_v1.md#free-subgroup-intersection) | Independent whole-argument finding on the stated result. |

## Current assessment

[Selected decision](#decision-free-subgroup-intersection)

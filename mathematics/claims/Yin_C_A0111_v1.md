---
author: Yin
---
# Matrix rank for rows supported in distinct free factors

## Statement

Let \(H_1,\ldots,H_m\) be subgroups of a discrete group \(G\) for which the natural map \(\ast_{i=1}^m H_i\to G\) is injective.
Consider a matrix \(M=(a_{ij})\) with \(n\) columns whose \(i\)-th row has entries in \(\mathbb C H_i\).
For \(g\in H_i\) write \(w_{i,g}=([g]a_{i1},\ldots,[g]a_{in})\in(\mathbb C^n)^*\), acting on columns by the bilinear row-column pairing.
For \(J\subseteq\{1,\ldots,m\}\) put
\[
 d_J=\dim_{\mathbb C}\operatorname{span}\{w_{i,g}:i\in J,\ g\in H_i\}.
\]
Write \(\operatorname{rk}_G M\) for the von Neumann dimension of the closed range of left convolution by \(M\), with the unnormalized matrix trace and the canonical group trace.
Suppose that for every \(i\), every nonzero element of \(\operatorname{span}_{\mathbb C}\{a_{i1},\ldots,a_{in}\}\) has dense convolution range on \(\ell^2(H_i)\).
Then
\[
 \operatorname{rk}_G M=
 \min_{J\subseteq\{1,\ldots,m\}}\bigl(m-|J|+d_J\bigr).                 \tag{1}
\]
The scalar injectivity hypothesis \(P_0\), that every nonzero complex group-ring scalar is injective in the regular representation, suffices separately on each \(H_i\).
Indeed, the adjoint of a nonzero group-ring scalar is again a nonzero group-ring scalar.

There is also a converse witness when the density hypothesis is omitted.
The right-hand side of (1) always bounds \(\operatorname{rk}_G M\) from above.
If the inequality is strict, some nonzero complex linear combination \(s\) of entries of a single original row has nondense convolution range in its own factor, so the group-ring scalar \(s^*\) has nontrivial kernel there.

In particular, suppose \(a,b\in\mathbb C H_1\), \(c,d\in\mathbb C H_2\), \(a\ne0\), and the two factors satisfy \(P_0\).
In the affiliated algebra \(\mathcal U(G)\), the first Schur complement \(d-ca^{-1}b\) is either zero or invertible.
More precisely, writing \(M=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\), this complement is zero precisely when \((c,d)=(0,0)\) or there exists \(\lambda\in\mathbb C\) such that \(b=\lambda a\) and \(d=\lambda c\).
For the full matrix in (1), the same zero-or-invertible alternative holds at every scalar pivot reached by row and column permutations and successive Schur complements at invertible scalar pivots.

<a id="argument"></a>
## A commutator that extracts a scalar from one row

We may replace \(G\) by \(L=\langle H_1,\ldots,H_m\rangle=\ast_i H_i\).
The orthogonal summands \(\ell^2(Lt)\) for right cosets are copies of the regular representation of \(L\) for every operator in the original matrix.
The diagonal coefficients at the identity that compute rank are therefore those of the matrix over \(L\).
The same decomposition with \(H_i\) in place of \(L\) shows that a scalar in \(\mathbb C H_i\) has dense range on \(\ell^2(H_i)\) exactly when it has dense range on \(\ell^2(L)\).

Put \(\mathcal H=\ell^2(L)\), let \(E\) be the rank-one orthogonal projection onto \(\mathbb C\delta_e\), and let \(D_i\) be the projection onto the closed span of the nonempty reduced words ending in \(H_i\).
Write \(x\) also for left convolution by \(x\).
For \(x\in\mathbb C H_k\),
\[
 [D_i,x]=
 \begin{cases}
 xE-Ex,& k=i,\\
 0,& k\ne i .
 \end{cases}                                                           \tag{2}
\]
To check this, first take \(x=h\in H_k\).
Outside \(H_k\), left multiplication by \(h\) preserves the last factor of a reduced word, since cancellation of its first letter can change its last factor only if the word belonged to \(H_k\).
On \(\ell^2(H_k)\) the projection is \(1-E\) for \(k=i\) and zero for \(k\ne i\).
These subspaces and their complements are invariant under \(h\), giving (2) and then its linear extension.

For an arbitrary subset of rows let \(N\) be the restricted matrix, and let \(q_N\) be the projection onto \(\ker N^*\).
Write \(e_i:\mathcal H\to\mathcal H^{\#\mathrm{rows}(N)}\) for coordinate inclusion at a retained row \(i\).
Given \(\xi=(\xi_1,\ldots,\xi_n)\in\ker N\), apply \(q_N\) to
\((D_i^{\oplus\#\mathrm{rows}(N)}N-ND_i^{\oplus n})\xi\).
The result is zero because \(N\xi=0\) and \(q_N N=0\).
The commutator vanishes outside row \(i\) by (2).
In that row the terms \(\sum_j E a_{ij}\xi_j\) vanish because row \(i\) of \(N\xi\) is zero.
Consequently
\[
 q_N e_i\,s\,\delta_e=0,\qquad s=\sum_{j=1}^n \xi_j(e)a_{ij}.          \tag{3}
\]
Right translations commute with \(q_N\), its coordinate inclusions and left convolution.
Their translates of \(\delta_e\) span a dense space, so (3) gives the bounded-operator identity \(q_N e_i s=0\).
If \(q_N e_i\ne0\), every nonzero \(s\) obtained this way has nondense range on \(\mathcal H\) and hence on \(\ell^2(H_i)\).
Replacing \(\xi\) by its right translates in the same kernel gives this implication with \(\xi_j(t)\) in place of \(\xi_j(e)\) at each \(t\in L\).

## The rank formula and the witness

For a row set \(J\), let \(W_J=\bigcap_{i\in J,\, g\in H_i}\ker w_{i,g}\subseteq\mathbb C^n\).
Its codimension is \(d_J\).
The restricted matrix \(M_J\) annihilates \(\ell^2(L;W_J)\) because each summand \(w_{i,g}\xi(g^{-1}t)\) of its value at \(t\) then vanishes.
Thus \(\operatorname{rk}_L M_J\le d_J\).
The other \(m-|J|\) output coordinates can add at most \(m-|J|\) to the rank, by dimension additivity applied to the projection of the closed range of \(M\) onto the \(J\) coordinates.
This proves the upper bound in (1).

Let \(q\) be the projection onto \(\ker M^*\), and set \(I=\{i:q e_i\ne0\}\).
Every vector in \(\ker M^*\) vanishes on coordinates outside \(I\) because \(q=q^*\).
Extension of an \(I\)-tuple by zero therefore identifies \(\ker M_I^*\) with \(\ker M^*\), in both directions by the formula for \(M^*\).
Writing \(q_I\) for the projection onto \(\ker M_I^*\) in its own coordinate space, we obtain \(q_I e_i\ne0\) for every \(i\in I\) and
\[
 \operatorname{rk}_L M=m-|I|+\operatorname{rk}_L M_I.                 \tag{4}
\]
Here we used the closed range and adjoint kernel as orthogonal complements in the appropriate output space.
The same identity includes \(I=\varnothing\), when \(M\) has dense range.

Under the row density hypothesis, apply (3) to \(N=M_I\).
For every \(\xi\in\ker M_I\), \(i\in I\) and \(t\in L\), the scalar \(\sum_j \xi_j(t)a_{ij}\) must vanish.
Taking all of its group coefficients shows \(\xi(t)\in W_I\).
The reverse inclusion was proved for every row set, so \(\ker M_I=\ell^2(L;W_I)\) and \(\operatorname{rk}_L M_I=d_I\).
Equation (4) now attains the upper bound for \(J=I\), proving (1).

Without the density hypothesis, strict inequality against the minimum in (1) implies \(\operatorname{rk}_L M_I<d_I\) by (4).
The inclusion \(\ell^2(L;W_I)\subseteq\ker M_I\) is then strict.
Choose a vector \(\xi\) in the difference and a coordinate \(t\in L\) with \(\xi(t)\notin W_I\).
There is some \(i\in I\) for which \(s=\sum_j\xi_j(t)a_{ij}\ne0\), by the definition of \(W_I\).
Formula (3) after a right translation gives \(q_Ie_i s=0\) with \(q_Ie_i\ne0\), proving the asserted witness.

## Scalar Schur complements

In the two-row setting \(a\) has an affiliated inverse since \(P_0\) gives injectivity and dense range.
Elimination by invertible affiliated triangular matrices gives \(\operatorname{rk}_G M=1+\operatorname{rk}_G(d-ca^{-1}b)\).
Here affiliated rank is closed-range support trace and is invariant under affiliated units, as in the [affiliated rank identity](../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement).
For a nonzero second row each singleton term on the right side of (1) is at least two.
The whole-row term \(d_{\{1,2\}}\) is one exactly when every coefficient vector in both rows belongs to a single complex line.
Since \(a\ne0\), the line then has the form \(\mathbb C(1,\lambda)\), giving \(b=\lambda a\) and \(d=\lambda c\).
In this case, and for a zero second row, the Schur complement vanishes.
In every other case (1) gives rank two and the scalar complement has rank one, which gives injectivity and dense range by finiteness and faithfulness of the trace.

For successive elimination, all submatrices obtained by deleting or permuting rows and columns retain the factor and density hypotheses.
Suppose \(k\) invertible pivots have been used, and order their original rows and columns in pivot order.
For a proposed next pivot, adjoin its original row and column to these \(k\) rows and columns to form a bordered \((k+1)\)-square submatrix \(B\).
Elimination on \(B\) gives the same first \(k\) pivots and the chosen residual scalar \(u\), since each update uses only the pivot row, the pivot column and the entry being updated.
Thus \(\operatorname{rk}_G B=k+\operatorname{rk}_G u\).
Formula (1) for \(B\) makes this rank an integer, so \(u\) has rank zero or one.
This proves the alternative for any such choice of pivots and also permits computing each residual rank from the original coefficients.

The support condition may be checked after multiplying individual rows on the left and columns on the right by group elements.
These operations preserve every corresponding submatrix rank by unitary equivalence.
Free placement is essential for (1).
For instance, over one infinite cyclic group with generator \(h\), taking two identical rows \((1,h)\) gives rank one, while inserting their two-dimensional coefficient spaces into the right side of (1) gives two.
The scalar regular representation of this group satisfies \(P_0\) by Fourier transformation.
The rank and Schur identities therefore give a positive case of [A0001](../tasks/Yin_T_A0001_v1.md#contract), with the implication from scalar injectivity to unrestricted first Schur complements still open.

## Assessment history

### Decision rank-by-free-rows

| Field | Value |
| --- | --- |
| date | 2026-11-22T04:17 |
| status | proved |
| reason | Independent review verified the full argument at the stated hypotheses and bounds. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Rank for arbitrary rectangular arrays with freely separated row algebras, extraction of a row witness and all scalar pivots. |
| argument | [Proof](#argument) | The terminal-factor commutator, density at the group identity, the coefficient span formula and the bordered pivot calculation. |
| review | [Whole finding](../audits/reviews/Yin_R_A0148_v1.md#whole-finding) | Independent whole-argument finding for the stated scope. |

## Current assessment

[Selected decision](#decision-rank-by-free-rows)

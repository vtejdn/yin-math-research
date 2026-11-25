---
author: Yin
---

# Testing rational kernel projections by two ranks in finite permutation models

## Statement

Let \(G\) be a finitely generated sofic group with a chosen sofic approximation by finite sets \(\Omega_n\), and put \(N_n=|\Omega_n|\).
Write \(A=\mathbb CG\), \(U=L^0(\mathcal N(G))\) and \(D_G=\operatorname{Div}_U(A)\).
For a group-ring matrix \(H\), let \(H_n\) be its finite matrix on \(\Omega_n\) and let \(r_n(H_n)=N_n^{-1}\operatorname{rank}_{\mathbb C}(H_n)\).
Thus an identity block of size \(h\) has normalized rank \(h\).
For a matrix with coefficients in \(A[t]\) we keep the complex parameter \(t\) central and choose word lifts of all coefficients to the marked free group, consistently across \(n\).
Let \((\lambda_n)\) be any prescribed sequence of complex numbers eventually outside each finite set, for example \(\lambda_n=n\).

For \(X\in M_{m,k}(A)\), its Hilbert kernel projection has entries in \(D_G\) if and only if there exist an integer \(h\ge1\) and three fixed polynomial matrices
\[
 L(t)\in M_h(A[t]),\qquad \alpha(t)\in M_{k,h}(A[t]),\qquad \beta(t)\in M_{h,m}(A[t])
\]
such that, for
\[
 J(t)=\begin{pmatrix}L(t)&\beta(t)X\\X\alpha(t)&X\end{pmatrix},
\]
the two normalized ordinary matrix ranks satisfy
\[
                   r_n(L_n(\lambda_n))\longrightarrow h,
             \qquad r_n(J_n(\lambda_n))\longrightarrow h.
\]
No inverses are taken in the finite models.
The same approximation, the same parameter sequence and the same polynomials apply to both rank limits.
For a fixed witness, one may also use random parameters \(\Lambda_n\) with laws satisfying \(\Pr(\Lambda_n\in E)\to0\) for each fixed finite set \(E\subset\mathbb C\), and take both limits in probability.
No independence across models is required.

Even for \(G=\mathbb Z\), there is an \(X\) with zero Hilbert kernel for which every such witness has a singular pivot in every cyclic quotient model.
For the regular action of \(\mathbb Z/n\mathbb Z\) this necessary loss can be exactly \(1/n\) in both normalized ranks.

For the [torsion-free deletion problem](../tasks/Yin_T_A0003_v3.md#contract) in the sofic class, the criterion applies to every finite input width. [Matrix kernel reduction](Yin_C_A0137_v1.md#the-number-of-auxiliary-vectors)
It replaces the affiliated inner inverse of a specified \(X\) by two finite-model rank limits with an existential choice of polynomial matrices of finite size and support.

## Argument

### One moving parameter in finite models

For a fixed rectangular \(P(t)\) over \(A[t]\), write \(r(P(t))\) for its unnormalized von Neumann rank after evaluation at a complex number.
We first prove that \(r_n(P_n(\lambda_n))\) converges to the maximum of \(r(P(t))\).

Lift individual coefficients to \(\mathbb CF\), where \(F\) is free on the chosen marking, and denote the resulting matrix polynomial by \(\widetilde P(t)=\sum_{j=0}^{d}P_jt^j\), with \(s\) input columns.
At a finite model, evaluating all products from their word lifts gives the finite permutation evaluation of the product in \(\mathbb CF\).
Any other consistent word lift of a fixed polynomial matrix changes its normalized rank by \(o(1)\) uniformly in \(t\).
Indeed, for the finitely many words and products defining both lifts, their images realize their relations and multiplication correctly at all points except \(o(N_n)\) points, by the defining local agreement of the sofic approximation.
There are also only \(o(N_n)\) points at which one of the finitely many paths uses such an exceptional point.
On the remaining input basis vectors all the coefficients of the two matrices agree.
The rank of their evaluated difference is bounded by the number of exceptional input basis vectors at every parameter value.

Over \(\mathbb CF[t]\), adjoin unknowns \(y_j=t^j y_0\), \(1\le j\le d\).
Use as the top block row \([P_0,\ldots,P_d]\) and as lower rows the equations \(y_j-t y_{j-1}=0\).
This gives an affine pencil \(B(t)\) with the same rank as \(\operatorname{diag}(\widetilde P(t),I_{ds})\) after any evaluation.
Indeed, replacing the auxiliary variables by the differences \(y_j-t y_{j-1}\) is an invertible triangular change of variables and these differences then eliminate the corresponding top-row blocks.
For a constant polynomial the auxiliary block is empty.
The same identities hold over \(A\) and in the finite matrices.

For a single finite model the affine pencil has its maximal rank outside a finite set, by the minor test.
For the group rank, the sum of the defects at every finite collection of distinct parameters is at most the degree times the supremum rank, by the [one-parameter rank bound](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration).
Consequently the set on which the rank is at least a fixed positive distance below its supremum is finite.
The union of the strict sublevels at distance \(1/j\), \(j\ge1\), is countable.
Choose \(\zeta\) outside that union and all the finite-model exceptional sets.
Write \(B(t)=B(\zeta)+(t-\zeta)B_1\).
For each \(\epsilon>0\) the strict eigenvalue theorem for the two fixed matrices \(B(\zeta),B_1\) over \(\mathbb CF\) gives a single finite set of scalars outside of which every finite permutation evaluation loses less than \(\epsilon N_n\) of the rank at \(\zeta\).
Here the theorem is applied after translating the parameter by \(\zeta\) and changing the sign of the direction matrix.
The finite set is uniform over all finite \(F\)-sets and so applies simultaneously to the chosen models. [Jaikin-Zapirain, Theorems 2.2 and 8.1](../audits/literature/JZ19/Yin_U001.md#strict-eigenvalue-proof)
Since every \(B_n(\zeta)\) has maximal rank and \((\lambda_n)\) escapes every finite set, the difference of the two normalized ranks tends to zero.
Sofic rank approximation at the fixed \(\zeta\) gives \(r_n(B_n(\zeta))\to r(B(\zeta))\). [Jaikin-Zapirain, Theorem 1.3](../audits/literature/JZ19/Yin_U001.md#rank-and-approximation-definitions)
Removing the auxiliary identity block proves the asserted generic rank limit for \(P\).
For random parameters the same proof bounds the probability of a normalized rank drop of size \(\epsilon\) by the mass of the finite exceptional set for that pencil.
For any fixed finite collection of polynomials the union of their exceptional sets still has mass tending to zero.

### Inner inverses and the two rank limits

Suppose first that \(p=p_{\ker X}\) has entries in \(D_G\).
The positive matrix \(X^*X+p\) is an affiliated unit, and its inverse has entries in \(D_G\) by [scalar Gram elimination](Yin_C_A0132_v1.md#argument).
Thus \(Y=(X^*X+p)^{-1}X^*\in M_{k,m}(D_G)\) and \(XYX=X\), by its action on the kernel and its orthogonal complement.
Realize this matrix as \(Y=\alpha L^{-1}\beta\) with group-ring coefficients and an affiliated-unit square matrix \(L\), combining scalar rational realizations of its finitely many entries by block diagonals. [Domain-preserving realizations](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations)
Schur elimination gives \(\operatorname{rk}_G L=h\) and \(\operatorname{rk}_G J=h+\operatorname{rk}_G(X-XYX)=h\).
Use these three constant matrix polynomials for the two rank limits.

Conversely, fix polynomial witnesses satisfying the two limits.
Take a single parameter \(\zeta\) of maximum group rank simultaneously for \(L\) and \(J\), which exists by the one-parameter result.
The finite rank limits identify these two group ranks with \(h\).
Consequently \(L(\zeta)\) is an affiliated unit, and \(Y=\alpha(\zeta)L(\zeta)^{-1}\beta(\zeta)\) has entries in \(D_G\).
The Schur complement has rank zero, hence vanishes by faithfulness and gives \(XYX=X\).

On affiliated columns take \(Q=I_k-YX\).
It is idempotent, and \(QU^k\) equals the affiliated kernel of \(X\), since \(XQ=0\) and \(Qv=v\) whenever \(Xv=0\).
The positive matrix \(H=QQ^*+(I_k-Q)^*(I_k-Q)\) is an affiliated unit.
Indeed, vanishing of both \(Q^*v\) and \((I_k-Q)v\) implies \(v^*v=v^*Qv=0\).
The two summands of \(H\) annihilate each other by idempotence of \(Q\), so \(QQ^*H^{-1}\) is the orthogonal projection onto the range support of \(Q\), which is \(p_{\ker X}\).
All of its entries lie in \(D_G\) by scalar Gram elimination.
This proves the converse, including if the finite \(L_n(\lambda_n)\) are singular on subspaces of normalized dimension tending to zero.
For random parameters both ranks in any fixed witness converge in probability to their respective maximum group ranks by the first part of the proof, so the same reasoning applies.

### A singular pivot in every finite model

Let \(G=\langle g\rangle=\mathbb Z\) with its cyclic quotient models and take \(X=1-g\).
The bilateral shift has no nonzero invariant square-summable vector, so \(p_{\ker X}=0\).
Identify the group algebra with \(\mathbb C[z,z^{-1}]\) by \(g\mapsto z\), retaining \(t\) as the independent parameter in the test.
Suppose that a polynomial witness satisfies the two rank limits and that \(\det L(t,1)\) is not the zero polynomial.
Choose a single \(\zeta\) of maximum group rank for both matrices with \(\det L(\zeta,1)\ne0\).
The Schur calculation gives \(XYX=X\) for \(Y=\alpha(\zeta)L(\zeta)^{-1}\beta(\zeta)\).
Over \(\mathbb C(z)\) this forces \(Y=(1-z)^{-1}\).
Yet the adjugate formula and \(\det L(\zeta,1)\ne0\) give a representative of \(Y\) with a denominator nonzero at \(z=1\).
This contradiction proves \(\det L(t,1)\equiv0\).
On the constant vectors of every cyclic quotient the group generator acts by \(1\), so \(L_n(\lambda_n)\) has an ordinary kernel of dimension at least one for every \(n\).
Taking \(h=1\), \(L=1-g\), \(\alpha=\beta=1\), gives four copies of \(1-g\) in \(J\).
Both ordinary ranks equal \(n-1\), attaining the loss \(1/n\).

## Assessment history

### Decision sofic-kernel-ranks

| Field | Value |
| --- | --- |
| date | 2026-11-25T10:45 |
| status | proved |
| reason | Uniform finite-model rank control at a moving parameter transfers the two Schur ranks to an actual affiliated inner inverse. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Two normalized rank limits for a specified matrix, random parameters and necessity of singular finite pivots. |
| argument | [Argument](#argument) | A pencil over the free group at a common maximal-rank point, uniform strict eigenvalues and affiliated inner inverses. |
| dependency | [Sofic rank approximation](../audits/literature/JZ19/Yin_U001.md#jz19-u001) | Theorems 1.3, 2.2 and 8.1 at their fixed-parameter and uniform strict-eigenvalue interfaces. |
| dependency | [Moving ranks](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) | Countable union of strict sublevels on the parameter line. |
| dependency | [Rational realizations](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) | Realizations of the entries of an affiliated inner inverse. |
| dependency | [Matrix inverse closure](Yin_C_A0132_v1.md#argument) | Scalar Gram inversion over the division closure. |
| dependency | [Matrix-size criterion](Yin_C_A0137_v1.md#the-number-of-auxiliary-vectors) | Application to complete deletion at every finite width. |
| review | [Finite model ranks](../audits/reviews/Yin_R_A0169_v1.md#finite-model-ranks) | Independent proof review at the specified scope. |

## Current assessment

[Selected decision](#decision-sofic-kernel-ranks)

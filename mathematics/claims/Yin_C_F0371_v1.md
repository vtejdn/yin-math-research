---
author: Yin
---

# Variable support, additive separation and ranks of rationality certificates

These deductions address the question of which coordinates of a finite-rank rationality certificate carry information about the corresponding rational function.
They were worked out on 26 November 2026 by Yin's main agent with contributions from three delegates to the algebraic, liberation and dual-system arguments.
The arguments are recorded for comparison and have not received a separate formal review.

<a id="support"></a>
## Variable support under maximal Delta

Let \(U=L^0(M)\) for a finite tracial von Neumann algebra with faithful normal probability trace.
For a tuple \(X\in M^d\) with \(\Delta(X)=d\) and \(I\subseteq\{1,\ldots,d\}\), write \(K_I=\operatorname{Div}_U\mathbb C\langle X_i:i\in I\rangle\), with \(K_\varnothing=\mathbb C\).
Let \(K\) denote the field for the full tuple.
The [algebraic criterion](Yin_C_F0068_v1.md#argument) identifies the unique tensor coordinates \(k_j\) of \(u\in K\) with its rational free difference quotients.
Then
\[
 u\in K_I \quad\Longleftrightarrow\quad k_j=0\quad(j\notin I).
\]
For a nonempty subtuple in the same ambient Hilbert space the finite-rank cycle test for maximal \(\Delta\) follows by filling the omitted coordinates with zero.
If \(u\in K_I\), extend the subtuple's solution by zero and use uniqueness for \(X\).
Conversely, a solution supported in \(I\) already solves the subtuple's equation, so the subtuple criterion gives \(u\in K_I\).
For \(I=\varnothing\), the equation \(u\otimes1=1\otimes u^{\mathrm{op}}\) implies \(u\in\mathbb C\), by applying a linear functional taking \(1\) to \(1\) to the second tensor leg.
In particular, the nonzero coordinates give the unique smallest set of rational generators among the given coordinates for this element, and \(K_I\cap K_J=K_{I\cap J}\).

<a id="separation"></a>
## Additive separation of bounded functions of disjoint blocks

Suppose \(X\) is selfadjoint, every marginal is diffuse and there exists a sum-normalized liberation dual system in the sense of the [liberation criterion](Yin_C_F0079_v5.md#sum-normalization).
For a partition into nonempty blocks \(I_\alpha\), put \(N_\alpha=W^*(X_i:i\in I_\alpha)\).
If \(u_\alpha\in N_\alpha\), then \(\sum_\alpha u_\alpha\) is rational in \(X\) if and only if each \(u_\alpha\) is affiliated rational in the generators of its own block.

To see this, suppose \(u=\sum_\alpha u_\alpha\) is rational.
Fix a block \(I\) and write \(u_I\) for its summand.
On \(M\Omega\), \(L_i\) commutes with every generator of a block omitting \(i\).
This extends to every bounded element of that block algebra: take uniformly bounded polynomials converging strongly to the element by Kaplansky density and pair the polynomial identity against \(\eta\in M\Omega\subseteq\operatorname{Dom}L_i^*\).
For \(\xi\in M\Omega\), the limit uses strong convergence on \(\xi\) and \(L_i\xi\), and the limit multiplier sends \(\xi\) back into \(M\Omega\).
Selfadjointness makes these generator polynomials a star algebra.
Apply the coordinate liberation criterion to the fraction \((1,u,u,1)\) and sum its equations over \(i\in I\).
All summands outside this block commute with these \(L_i\), and \(u_I\) commutes with each \(L_j\) for \(j\notin I\).
Normalization now gives bounded finite-rank \(T_i\) satisfying
\[
 \sum_{i\in I}[\rho(X_i),T_i]=[P_\Omega,u_I].
\]
The identity first holds on \(M\Omega\), which is dense, and both displayed sides are bounded.
Compress it to \(L^2(N_I)\), where \(N_I=W^*(X_i:i\in I)\).
This subspace reduces each right multiplier in the sum and the vacuum projection, and it is invariant under \(u_I\) and its adjoint.
The compressed \(T_i\) still have finite rank.
The liberation hypotheses give maximal \(\Delta\) for \(X\) by the same criterion's maximality proposition.
Any finite-rank cycle on the block Hilbert space extends by zero on the orthogonal complement and by zero in the omitted coordinates to a cycle for \(X\).
Thus the algebraic criterion on the block Hilbert space gives \(u_I\in\operatorname{Div}_{L^0(N_I)}\mathbb C\langle X_i:i\in I\rangle\).
Conversely the inclusion \(L^0(N_I)\subseteq U\) preserves rational evaluations, and \(K\) is closed under addition.

For singleton blocks this says \(\sum_i f_i(X_i)\) is rational precisely when every bounded Borel \(f_i\) agrees almost everywhere for the law of \(X_i\) with a one-variable rational function.
For two free arcsine variables on \((-1,1)\), the liberation gradients vanish by [Voiculescu's freeness criterion, 5.17](../audits/literature/Voi99/Yin_U003.md#liberation-derivation-and-gradient), giving the required system by the [gradient construction](Yin_C_F0082_v1.md#sum-normalized-liberation-dual-system).
The sum \(|X_1|+|X_2|\) is therefore nonrational: a rational function agreeing with \(t\) almost everywhere on \((0,1)\) is identically \(t\) and cannot agree with \(-t\) on \((-1,0)\).
The [arcsine vacuum moment obstruction](Yin_C_F0080_v1.md#argument) uses only one coordinate and the vacuum adjoint pairings, so it also excludes an ordinary dual system for this pair.

<a id="ranks"></a>
## Coordinate ranks of a minimal affine representation

Assume the \(X_i\) are normal generators with a dual system \(D_i\) on \(L^2(W^*(X))\) satisfying the [common domain conditions](Yin_C_F0068_v1.md#dual-specializations).
Write \(u=r(X)\) for a nonzero free rational function \(r\) with a least-dimension affine linear representation
\[
 r=\alpha A^{-1}\beta,\qquad A=A_0-\sum_j A_j x_j
\]
with constant scalar matrices and a full square pencil.
For every fraction pair \(Q\) for \(u\),
\[
 \operatorname{rank}\overline{\Gamma[Q,D_i]}
 =\operatorname{rank}_{\otimes}(\partial_i r)
 =\operatorname{rank}_{\mathbb C} A_i .
\]
Here the tensor rank of an order-two algebraic tensor is its least number of simple summands.
Put \(g=\alpha A^{-1}\) and \(h=A^{-1}\beta\).
The inverse rule gives \(\partial_i r=\sum_{a,b}(A_i)_{ab}\,g_a\otimes h_b^{\mathrm{op}}\).
Each state family is linearly independent over \(\mathbb C\) by [Cohn and Reutenauer, Lemma 4.5](../audits/literature/CR94/Yin_U001.md#cr94-u001), so the tensor rank is the scalar matrix rank.
The evaluation embeds the free field, and multiplying the two tensor legs by the regular denominators \(s\) on the left and \(t\) on the right preserves their linear independence.
For a fraction pair cleared into bounded tensor legs, the certificate coordinate agrees up to sign with the finite-rank operator associated to this cleared derivative.
This identification takes tensor rank to operator rank.
The [dual-system identification and fraction-rank invariance](Yin_C_F0068_v1.md#dual-specializations) give the formula for all pairs.
The [minimal affine inverse calculation](Yin_C_F0107_v1.md#statement) records the state families and their derivatives in its rational \(L^2\) application.

For instance, for \(d\ge2\) take \(p=x_1x_2-x_2x_1\) and \(r=p^{-1}\).
The first two derivatives of \(p\) are \(1\otimes x_2^{\mathrm{op}}-x_2\otimes1\) and \(x_1\otimes1-1\otimes x_1^{\mathrm{op}}\), both of tensor rank two.
Inversion multiplies their two legs by invertible factors and changes the sign.
Thus every fraction pair gives ranks \(2,2,0,\ldots,0\).
This computation applies in particular to the canonical \(q\)-Gaussian family for all \(-1<q<1\) by the [dual construction and extension](Yin_C_F0023_v1.md#statement).

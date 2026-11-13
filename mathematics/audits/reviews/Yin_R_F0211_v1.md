---
author: Yin
---
# Independent review of full-domain duals under a common bounded similarity

<a id="bounded-similarity"></a>
## Bounded similarity

At 2026-11-13T13:12 UTC an agent outside the development of C_F0203 independently inspected the whole fixed v1 statement and argument for Yin.
The reviewer worked from the candidate, the Task definitions and its mathematical inputs, with no development dialogue, draft or previous review supplied or consulted to reach the finding.

For every formal word, conjugating by \(h\) preserves the two traces in each cut separately.
Applying the \(L^2\) bounds of \(W\) and \(W^{-1}\) to the evaluated polynomial therefore gives both inequalities between the least constants, even before any injectivity of evaluation is known.
A finite bound annihilates the kernel of evaluation at \(Y\) and defines a continuous functional on the dense polynomial subspace of \(L^2(N)\).
Reversing the words gives \(\Lambda_i^Y(p^*)=\overline{\Lambda_i^Y(p)}\), so its Riesz vector is selfadjoint and gives the trace pairing in MSW17, Definition 2.1.
The joint formal conjugate relations give the represented difference quotients by MSW17, Theorem 2.5, and their adjoint values at \(1\otimes1\) are precisely these vectors.
Conversely their norms bound the functional, with equality for its operator norm by density.
The finite sum of their squared norms is the joint Fisher information by Definition 2.6.
On the starred core at \(X\), Leibniz and the actual vacuum adjoint give the required estimate on each holomorphic test polynomial.

For \(a\in M\), the estimate \(\|(P_Na)b\|_2=\|P_N(ab)\|_2\leq\|a\|\|b\|_2\) on \(N\) identifies \(P_Na\) with an element of \(N\) of norm at most \(\|a\|\) by the standard tracial commutant theorem.
Orthogonality and \(1\in H_N\) also give \(\tau(P_Na)=\tau(a)\).
The negative of the closed contraction in C_F0022 has the required generator-first sign.
Extending it by zero on \(H_N^\perp\) extends its adjoint by zero there, and \(L_{Y_j}\) preserves both summands.
Thus the generator commutator holds on every \(a\in M\), including when \(N\) is proper.
Testing the adjoint pairing on vectors \(Wv\) gives \(\operatorname{Dom}(D_i^X)^*=(W^*)^{-1}\operatorname{Dom}\widetilde D_i^*\).
Both input maps \(W^{-1}\) and \(W^*\) preserve \(M\) with operator-norm bound \(\kappa\), and the respective output maps \(W\) and \((W^{-1})^*\) have Hilbert-space norm at most \(\kappa\).
Every bounded vector thus belongs to both actual domains, with the respective operator-norm-to-\(L^2\) bounds \(4\kappa^2\|\eta_i\|_2\) and \(5\kappa^2\|\eta_i\|_2\).
The trace and the unit are invariant under \(W\), which preserves the vacuum projection under similarity and gives the stated commutators for \(X\).

For arbitrary bare duals, \(Wb\) and \(X_j Wb=W(Y_jb)\) both lie in \(M\) for each \(b\in N\).
Commuting \(P_N\) with \(L_{Y_j}\) therefore gives the bare commutator with right side \(\delta_{ij}\tau(b)1\) after compression.
Selfadjointness, generation of \(N\), the restricted trace and the full domain \(N\) supply all the hypotheses of C_F0071 v2, Part B.
This gives joint conjugates from bare duals and closes the cycle of implications.

In C_F0133 the positive scalar coordinate and the constant matrix units lie in \(W^*(X)\), while the similar variable \(Y\) has the semicircular law and generates an abelian subalgebra.
The shift commutator on \(L^2(W^*(Y))\) extends and transports as asserted.
Differentiating \([X^2,X^*]=0\) forces the \(e_{21}\otimes e_{11}\) coefficient of \(\delta(X^*)\) to equal \(s/(s-t)\) off the diagonal.
Its squared norm diverges on \([1/2,1]^2\), where both scalar densities are bounded below.
This excludes every normalized starred Hilbert-valued derivation while giving a bounded witness for the duals.

The argument establishes the equivalence of the four conditions, the strict implication from the starred hypothesis and both estimates for the constructed duals.
The reviewer checked the cited MSW17 formal conjugate and Fisher statements in the retained preprint, pp. 5–8, and the AP18 commutant and conditional expectation statements in the retained draft, printed pp. 99 and 140.
The latter attribution agrees with Theorem 9.1.2 and Remark 9.1.3 for the trace-preserving expectation.
The review used C_F0022 and C_F0071 at the stated selfadjoint interfaces and inspected their relevant derivations, accepting their underlying source results at the recorded scope.
It did not re-audit the original literature proofs or examine the general F0011 objectives outside this similarity class.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Bounded similarity](#bounded-similarity) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Bounded similarity](#bounded-similarity) | [Statement](../../claims/Yin_C_F0203_v1.md#statement) | Common bounded invertible similarity, the four conditions, starred implication, strictness and the stated quantitative estimates. |
| [Bounded similarity](#bounded-similarity) | [Argument](../../claims/Yin_C_F0203_v1.md#argument) | Entire proof including formal tests, both domain bounds, reverse compression and the strict example. |
| [Bounded similarity](#bounded-similarity) | [Task hypotheses](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Generator-first commutators, actual Hilbert adjoints and bare, strong and starred existential hypotheses. |
| [Bounded similarity](#bounded-similarity) | [MSW17 selfadjoint conjugates](../literature/MSW17/Yin_U001.md#msw17-u001) | Formal conjugates on a selfadjoint generating tuple, algebraic descent and finite joint free Fisher information. |
| [Bounded similarity](#bounded-similarity) | [AP18 commutant](../literature/AP18/Yin_U002.md#ap18-u002) | Standard tracial commutant on the subalgebra and the resulting contractivity of the projection on bounded elements. |
| [Bounded similarity](#bounded-similarity) | [Selfadjoint full domains](../../claims/Yin_C_F0022_v1.md#3-the-entire-bounded-algebra-lies-in-both-domains) | Closed contraction, its adjoint, their bounds (9) and their use in the generator identity on every bounded vector. |
| [Bounded similarity](#bounded-similarity) | [Selfadjoint bare converse](../../claims/Yin_C_F0071_v2.md#statement) | Part B applied to the bare system on the entire generated subalgebra \(N\). |
| [Bounded similarity](#bounded-similarity) | [Strictness example](../../claims/Yin_C_F0133_v1.md#statement) | Nonnormal single generator, common similarity, bounded dual and failure of every normalized starred derivation. |

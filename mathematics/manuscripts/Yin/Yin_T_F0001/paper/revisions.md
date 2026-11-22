# Manuscript revision opinions

The opinions below concern Section 6 of [examples.tex](sections/examples.tex).

## Required revisions

- **Example 6.1, `ex:maximal-delta-without-liberation`, passage from the commutator relations to the limit.**
  Relate \(p_n\) to the continuous function \(f\) already chosen for the two spectral intervals.
  Explain that \(Z\) preserves \(\mathcal M\Omega\), so the relation on this subspace extends to every polynomial in \(Z\) by induction and linearity.
  State \(\mathcal M\Omega\subseteq\operatorname{Dom}B^*\) for both choices of \(B\), using the definition of a liberation dual system and boundedness of \(P_\Omega\).
  This inclusion justifies the adjoint pairing used to pass to the limit.

- **Example 6.2, `ex:liberation-without-duals`, vacuum estimate at the end.**
  State \(\Omega\in\operatorname{Dom}D\cap\operatorname{Dom}D^*\) from the dual-system definition when writing the identity with \(D\Omega\) and \(D^*\Omega\).
  These two vectors give the fixed constant in the estimate for the possibly unbounded dual operator.

- **Example 6.3, `ex:normality`, Fock space setup.**
  Identify the Fock space for the two creation operators with the vacuum representation \(H=L^2(W^*(S_1,S_2),\tau)\).
  This specifies the space on which \(D\in\mathcal B(H)\) and the finite-rank operators act.

- **Subsection 6.2, opening comparison with Lin00.**
  Explain the passage from the free group algebra in Linnell's statement to the polynomial algebra \(\mathcal A_X\) used here.
  Taking inverses of the unitary generators already gives the group algebra inside each relevant division closure.
  Monotonicity places the division closure in the group von Neumann algebra between the division closure in the reduced group \(C^*\)-algebra and the bounded part of the affiliated division closure, which Linnell identifies.

- **Proposition 6.4, `prop:scalar-bounded-dual`, reduction to the spectral representation.**
  The statement concerns \(H=L^2(\mathcal M,\tau)\), while the proof works on \(K=L^2(W^*(X),\tau)\).
  State that \(K\) reduces \(X\) and contains \(\Omega\).
  Compress a solution on \(H\) to \(K\) and extend a solution on \(K\) by zero to \(H\), using \(P_\Omega=P_1\oplus0\) and the same commutator equation.
  This transfers the existence criterion, skew-adjointness and the norm bound to the space in the statement.

- **Example 6.5, `ex:bounded-division-closure`, membership and norm separation.**
  Identify the original algebra containing \(S\) and justify the passage from \(Y=XSX\) there to \(S\in\mathcal M=W^*(X,Y)\) and \(S=X^{-1}YX^{-1}\) in the affiliated algebra of \(\mathcal M\).
  One direct route is to use bounded spectral cutoffs of \(X^{-1}\) on both sides of \(Y\), giving compressions of \(S\) that converge strongly to \(S\).
  At the trace factorization in the norm estimate, say that \(B=(S-c)^*(S-c)\) and \(\pi_\varepsilon\) belong to the two free algebras \(W^*(S)\) and \(W^*(X)\), respectively.

- **Example 6.5, `ex:bounded-division-closure`, identification of the tensor spaces.**
  Justify the unitary identification of \(L^2(\mathcal M,\tau)\) with the orthogonal sum of the tensor spaces \(H_n\) before using the actions of \(X\) and \(S=l+l^*\).
  Give a short construction or an applicable free-product citation together with the reindexing by semicircular degree and the resulting actions.
  The [tracial Fock model in the supporting argument](../../../../claims/Yin_C_F0012_v1.md#1-an-explicit-tracial-fock-model) gives a direct route.
  The [citation map](../citation.md) lists a reference to Voi98 §§5.5 and 5.13 for this step. Reconcile that entry with the citation or argument actually used in the revised TeX.

- **Example 6.5, `ex:bounded-division-closure`, formulas for \(Y\) and \(V^*+V\).**
  Replace \(XL^*X\) in the expansion of \(Y\) by \(Xl^*X=L^*\), since \(L=XlX\).
  State that \(L^*\) vanishes on \(H_0\) and give its displayed tensor formula for \(n\geq1\).
  In the integral formula for \(V^*+V\), write \(\int f\,d\mu=\langle 1,f\rangle\) because the inner product is linear in its second variable.
  The estimate for \(K\) uses the Cauchy–Schwarz inequality. Replace the reference to equality.

- **Subsection 6.2, sentence syntax.**
  Correct “At moment,” “on \(H_0\) and and show,” and “a operator.”
  Split or recast the comma splices beginning “So we see that \(S\in L^0(\mathcal M)\)” and “Put \(B\).”

## Optional improvements

- **Example 6.3, the obstruction to rationality.**
  Explain that the centralizer of \(c\) in the affiliated algebra is closed under inversion.
  The two length-two tensors in \([S_2,S_1]\Omega\) then give a short verification that \(c^*\) lies outside that centralizer.

- **Opening of Section 6 and Example 6.2.**
  Describe the first two examples as establishing strictness of the implications between the hypotheses of the three criteria.
  In the arcsine argument, announce the contradiction between the constant vacuum pairing and the vanishing \(L^2\) norm of the odd powers.
  A one-line derivation of \(m_r\) using \(t=\cos\theta\) would make the source of the moment formula readily visible.

- **Transition to Proposition 6.4 and the proof plan for Example 6.5.**
  Replace “may be known to experts” and the procedural lead-in with the precise use of the proposition. It supplies the bounded dual for the scalar coordinate \(X\) from the density \(4t^3\).
  When introducing \(\xi_\varepsilon\), explain that polynomial evaluations act asymptotically like their constant terms on these vectors while \(S\) gives the norm separation.
  At the assertion that \(\tilde R\) commutes with \(X\), identify the identity for \(K\) on \(H_1\) and the distinct tensor factors for \(n\geq2\).
  Before defining \(D_1\), explain that the terms built from \(D_2\) cancel \([Y,\tilde D_X]\) while preserving the commutator with \(X\).

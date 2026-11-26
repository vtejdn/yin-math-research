# Manuscript revision opinions

The opinions concern Proposition 5.8, `prop:fraction-commutator-rank`, and the one-variable comparison at the end of [Section 5](sections/dual-system-criterion.tex).

## Required writing corrections

- **Domains and use of the linear functionals.**
  The wording “on \(g_j\)” and “on \(h_k^{\mathrm{op}}\)” leaves the domains unclear at the evaluations on \(y_\nu\) and \(z_\nu^{\mathrm{op}}\).
  Choose \(\varphi_j\) and \(\widetilde{\varphi}_k\) on the first and second tensor factors, respectively, and retain their prescribed values on the two independent families.
  Name the expansion from the linear representation and the chosen shortest tensor decomposition when applying \(\varphi_j\otimes\widetilde{\varphi}_k\).

- **Scope and rank preservation in the one-variable comparison.**
  Replace “In one variable case” with an opening that fixes \(d=1\), \(X=X_1\) and its dual operator \(D_1\) under the hypotheses of Proposition 5.8.
  Identify \(A(x)=A_0+xA_1\) as the pencil in the chosen minimal linear representation.
  When introducing the divided difference, identify \(z\) and \(w\) as the local coordinates at \(\lambda\) for the two tensor factors.
  After the divided-difference expansion, use injectivity of Taylor expansion on rational functions regular at \(\lambda\) to explain why expansion in the two tensor factors preserves the tensor rank.
  This connects the tensor rank of \(\partial_1 r\) to the algebraic rank of the displayed coefficient matrix.

- **Conclusion of the Kronecker comparison.**
  State explicitly that Proposition 5.8 identifies this Hankel rank with \(\operatorname{rank}\overline{\Gamma[Q,D_1]}\) for every fraction pair \(Q\) for \(r(X)\).
  Replace “rationality complexity” with the actual rank identity and “finite rankness of its Hankel matrix” with “finiteness of its Hankel rank.”
  If the concluding comparison addresses the rationality criterion, attribute that criterion to Theorem 1.9 and the rank computation for rational functions to Proposition 5.8.

## Optional improvements

- **Transition from tensors to finite-rank operators.**
  Introduce \(T_j=-\Theta(\ell_j)\) when invoking Lemma 3.3 and say which commutator equation the tuple solves.
  Invoke Lemma 5.3 in the next sentence to identify each \(T_j\) with the corresponding fraction commutator closure.

- **Injectivity of \(B\) and surjectivity of \(C\).**
  Name the two families of vectors in \(H\) after evaluation and denominator multiplication.
  Write \(C^*e_k=J(h_k(X)t\Omega)\) to make clear which vectors establish injectivity of \(C^*\) and hence surjectivity of \(C\).

- **Tensor-rank definition and choice of decomposition.**
  In the final sentence of the proposition, specify \(p\geq 0\) so that the definition also reads directly for the zero tensor.
  Omit the repeated \(y_\nu\otimes z_\nu^{\mathrm{op}}\) after “simple tensors” in the proof, since the sum already specifies these terms.

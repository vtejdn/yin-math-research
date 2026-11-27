# Manuscript revision opinions

These opinions cover the abstract and Sections 1–6 of the current F0001 manuscript.

## Corrections to scope, references and wording

- **State the scalar-shift hypothesis in the abstract and before Proposition 4.7.**
  The abstract describes the second criterion using liberation dual systems and leaves its hypothesis on scalar shifts implicit.
  Summarize the first criterion by its conclusion. “Under maximal \(\Delta\), rationality is equivalent to solvability of a finite-rank commutator equation for some fraction pair.”
  For the second criterion, write “If \(X\) admits a liberation dual system and every scalar shift \(X_i-\lambda\) is invertible in the affiliated algebra, solvability of the finite-rank commutator equation is independent of the fraction pair.”
  The sentence immediately before Proposition 4.7 should likewise name both inputs when introducing maximal \(\Delta\). [Abstract](main.tex#L55) · [Proposition 4.7 lead-in](sections/liberation-dual-system-criterion.tex#L233)

- **Introduce \(\mathcal F(H)\) and \(\rho\) before the first commutator display.**
  In Section 1.1, a sentence such as “Write \(\mathcal F(H)\) for the bounded finite-rank operators on \(H\), and let \(\rho(x)\) denote right multiplication by \(x\in\mathcal M\)” gives the reader the meaning of both symbols before the characterization of \(\Delta(X)=d\).
  Recall the notation in Section 2 when introducing the tensor representation of finite-rank operators. [First use](sections/introduction.tex#L34)

- **Specify the reverse passage between the two equations in Theorem 1.7.**
  The sentence beginning “Conversely, we will see” lacks a grammatical connection to the claim about the liberation relations.
  Write “Conversely, Lemma 3.3 turns the summed commutator equation into a tensor identity. After clearing denominators, the map \(c\otimes e^{\mathrm{op}}\mapsto cL_i e\) on \(\mathcal M\Omega\) annihilates the terms corresponding to \([\rho(X_j),T_j]\) for \(j\ne i\) by the liberation relations. Lemma 4.8 gives \([\rho(X_i),T_i]=\overline{\Gamma[Q,L_i]}\) for the original tuple.” [Introduction after Theorem 1.7](sections/introduction.tex#L205)

- **Specify the scalar coefficients in Lemma 2.5.**
  The preceding balancing identity uses \(v_1,v_2\in U\), while the line proving right \(F\)-linear independence needs its coefficients in \(F\).
  Write “If \(a+ub=0\) with \(a,b\in F\) and \(b\ne0\), then \(u=-ab^{-1}\in F\).” [Proof of Lemma 2.5](sections/preliminaries.tex#L75)

- **Name the conclusion obtained by interchanging the tensor factors in Lemma 4.5.**
  “Injectivity of the other natural map” leaves its referent unclear, and the displayed kernel formula for \(I_W\otimes\pi\) allows a nonzero kernel.
  Write “Interchanging the tensor factors gives \(\ker(I_W\otimes\pi)=W\otimes_{\mathbb C}E\).” [Proof of Lemma 4.5](sections/liberation-dual-system-criterion.tex#L157)

- **Use the actual mathematical operation in the lead-ins to Lemma 4.8 and the calculation in Lemma 5.3.**
  Replace “We records two technical lemmas” with “The next two lemmas recover the \(L^2\) tensor factors and establish closability of the fraction commutators.”
  Replace “Let us fix \(i\) … and we evaluate the equation under … for both sides” with “Fix \(i\) and \(\xi\in\mathcal M\Omega\), and apply \(\ell\mapsto m_{D_i}(\ell)\xi\) to both sides of equation (25).” [Before Lemma 4.8](sections/liberation-dual-system-criterion.tex#L263) · [Proof of Lemma 5.3](sections/dual-system-criterion.tex#L96)

- **Frame Example 6.3 in terms of solvability and name the hypotheses supplying maximal \(\Delta\).**
  The opening can state the observed distinction directly. “For a bounded rational element, the finite-rank commutator equation can be solvable for one fraction pair and unsolvable for another.”
  Replace “The distributions of both \(h\) and \(S\) has no atoms, and hence” with “Since \(h\) and \(S\) are free and have nonatomic distributions,” before invoking MSY23 for \(\Delta(h,S)=2\).
  After applying the identity to \(\Omega\), state the contradiction by pairing “\(T_Y(h\Omega)=-h^{-1}\)” with “\(T_Y(h\Omega)\in H\) and \(h^{-1}\notin H\).” [Example 6.3](sections/examples.tex#L132)

## Optional improvements

- **Apply common denominators to all tensor factors in one step in Lemma 3.1.**
  After writing the \(k_i\) as finite sums of simple tensors, choose \(s\) for all first factors and \(t\) for all second factors using the common-denominator lemma.
  Display the resulting transformation of an individual summand \(u\otimes v^{\mathrm{op}}\) into \(su\otimes(vt)^{\mathrm{op}}\). [Proof of Lemma 3.1](sections/maximal-delta.tex#L19)

- **Connect Proposition 5.8 directly to Corollary 5.9.**
  Replace the longer lead-in about independence from a choice of realization with “The ranks in Proposition 5.8 also bound the dimension of a minimal linear representation of \(r\).”
  Refer to the operators in the bound as fraction commutator closures, matching the proposition. [Before Corollary 5.9](sections/dual-system-criterion.tex#L424)

- **Include the fraction-pair example in the introduction's roadmap.**
  In the description of Section 6, name the dependence of solvability on the fraction pair as one of the distinctions established by the examples. [Organization](sections/introduction.tex#L267)

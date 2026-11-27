# Manuscript revision opinions

These opinions cover the abstract and Sections 1–6 of the current F0001 manuscript.

## Corrections to references and wording

- **Specify the scalar coefficients in Lemma 2.5.**
  The preceding balancing identity uses \(v_1,v_2\in U\), while the line proving right \(F\)-linear independence needs its coefficients in \(F\).
  Write “If \(a+ub=0\) with \(a,b\in F\) and \(b\ne0\), then \(u=-ab^{-1}\in F\).” [Proof of Lemma 2.5](sections/preliminaries.tex#L75)

- **Name the conclusion obtained by interchanging the tensor factors in Lemma 4.5.**
  “Injectivity of the other natural map” leaves its referent unclear, and the displayed kernel formula for \(I_W\otimes\pi\) allows a nonzero kernel.
  Write “Interchanging the tensor factors gives \(\ker(I_W\otimes\pi)=W\otimes_{\mathbb C}E\).” [Proof of Lemma 4.5](sections/liberation-dual-system-criterion.tex#L157)

- **Use the actual mathematical operation in the lead-ins to Lemma 4.8 and the calculation in Lemma 5.3.**
  Replace “We records two technical lemmas” with “The next two lemmas recover the \(L^2\) tensor factors and establish closability of the fraction commutators.”
  Replace “Let us fix \(i\) … and we evaluate the equation under … for both sides” with “Fix \(i\) and \(\xi\in\mathcal M\Omega\), and apply \(\ell\mapsto m_{D_i}(\ell)\xi\) to both sides of equation (25).” [Before Lemma 4.8](sections/liberation-dual-system-criterion.tex#L263) · [Proof of Lemma 5.3](sections/dual-system-criterion.tex#L96)

- **Name the hypotheses supplying maximal \(\Delta\) and clarify the contradiction in Example 6.3.**
  Replace “The distributions of both \(h\) and \(S\) has no atoms, and hence” with “Since \(h\) and \(S\) are free and have nonatomic distributions,” before invoking MSY23 for \(\Delta(h,S)=2\).
  After applying the identity to \(\Omega\), state the contradiction by pairing “\(T_Y(h\Omega)=-h^{-1}\)” with “\(T_Y(h\Omega)\in H\) and \(h^{-1}\notin H\).” [Example 6.3](sections/examples.tex#L134)

## Optional improvements

- **Apply common denominators to all tensor factors in one step in Lemma 3.1.**
  After writing the \(k_i\) as finite sums of simple tensors, choose \(s\) for all first factors and \(t\) for all second factors using the common-denominator lemma.
  Display the resulting transformation of an individual summand \(u\otimes v^{\mathrm{op}}\) into \(su\otimes(vt)^{\mathrm{op}}\). [Proof of Lemma 3.1](sections/maximal-delta.tex#L19)

- **Connect Proposition 5.8 directly to Corollary 5.9.**
  Replace the longer lead-in about independence from a choice of realization with “The ranks in Proposition 5.8 also bound the dimension of a minimal linear representation of \(r\).”
  Refer to the operators in the bound as fraction commutator closures, matching the proposition. [Before Corollary 5.9](sections/dual-system-criterion.tex#L424)

- **Include the fraction-pair example in the introduction's roadmap.**
  In the description of Section 6, name the dependence of solvability on the fraction pair as one of the distinctions established by the examples. [Organization](sections/introduction.tex#L268)

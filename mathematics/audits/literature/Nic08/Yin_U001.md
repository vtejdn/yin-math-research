---
author: Yin
---

# Nic08: unconditional completions and the amenable spectral obstruction

<a id="nic08-u001"></a>
## Source and inspection scope

The adopted source is the [final arXiv v2](readme.md#arxiv-v2).
The definitions in Section 8.1 on p. 18 and Section 8.3 on pp. 19–20, and the whole short statement and proof of Proposition 8.7 on p. 20, were read directly on 12 November 2026.
The norm comparison and the passage from equality of selfadjoint spectral radii to relative spectral equality were checked at that scope.
The argument uses the standard Banach-algebra spectral-radius formula and amenability's norm equality for convolution by nonnegative coefficients.
These standard inputs were accepted; the paper's earlier general spectral-morphism theory, K-theory results and cited originals were not audited end to end.
The earlier v1 passages were compared only at the [specified edition correspondence](readme.md#arxiv-v1).
This is a development-role source inspection, not an independent review of a project proof.

<a id="spectral-equivalence"></a>
## Definition: spectral equivalence over a common algebra

Let \(A\) and \(B\) be unital Banach-algebra completions of a common unital algebra \(X\).
Section 8.1 calls them spectrally equivalent over \(X\) if
\[
\sigma_A(x)=\sigma_B(x)\qquad(x\in X).
\]
They are completely spectrally equivalent over \(X\) if the corresponding equality holds in \(M_n(A)\) and \(M_n(B)\) for every \(n\ge1\) and every \(x\in M_n(X)\).
The definition itself does not require a continuous homomorphism connecting the two completions.
For an actual unital homomorphism \(\phi:A\to B\), being spectral relative to a subalgebra \(X\subset A\) means \(\sigma_A(x)=\sigma_B(\phi(x))\) for every \(x\in X\).
The finite-support group-algebra application below retains the common algebra \(X=\mathbb CG\), rather than replacing it by a completed algebra.

<a id="unconditional-completion"></a>
## Definition: unconditional completion and the Sigma-one convention

For a discrete group \(G\), write
\[
f=\sum_g f(g)g\in\mathbb CG,
\qquad |f|_{\mathrm{coef}}=\sum_g |f(g)|g.
\]
The second expression is coefficientwise absolute value, not the operator absolute value \((f^*f)^{1/2}\).
The paragraph preceding Proposition 8.7 calls a Banach-algebra completion \(A(G)\) unconditional when its norm satisfies
\[
\bigl\||f|_{\mathrm{coef}}\bigr\|_{A(G)}=\|f\|_{A(G)}
\qquad(f\in\mathbb CG).
\]
The source attributes this terminology to Lafforgue; that attribution is recorded without a historical-priority claim.

Section 8.3 calls \(G\) a \(\Sigma_1\)-group when the inclusion \(\ell^1(G)\to C_r^*(G)\) is spectral relative to \(\mathbb CG\):
\[
\sigma_{\ell^1(G)}(f)=\sigma_{C_r^*(G)}(f)
\qquad(f\in\mathbb CG).
\]
This quantifier concerns finite-support elements and does not assert spectral equality for every \(f\in\ell^1(G)\).

<a id="proposition-8-7"></a>
## Proposition 8.7 and the checked mechanism

Suppose that \(G\) is amenable and that an unconditional Banach-algebra completion \(A(G)\) is spectrally equivalent to \(C_r^*(G)\) over \(\mathbb CG\).
Proposition 8.7 states that \(G\) is then a \(\Sigma_1\)-group.
In particular an unconditional completion with that spectral-equivalence property cannot bypass the finite-support spectral obstruction already present in \(\ell^1(G)\).
The proposition does not assume that the completion's involution is continuous, and the source notes the simpler argument available when it is a Banach star algebra.

For \(f=f^*\in\mathbb CG\), the regular element is selfadjoint and spectral equivalence gives
\[
\|f\|_{C_r^*}=r_{A(G)}(f)\le\|f\|_{A(G)}.
\]
The same inequality applied to the selfadjoint element \(|f|_{\mathrm{coef}}\), followed by amenability and unconditionality, gives the source's key comparison
\[
\|f\|_1
=\bigl\||f|_{\mathrm{coef}}\bigr\|_{C_r^*}
\le\bigl\||f|_{\mathrm{coef}}\bigr\|_{A(G)}
=\|f\|_{A(G)}.
\]
Applying these comparisons to the selfadjoint powers \(f^n\) and taking roots gives equality of the \(\ell^1\) and regular spectral radii for every selfadjoint finite-support \(f\).

The final paragraph checks the needed relative version of the usual spectral-radius argument.
For a dense star homomorphism \(\phi:A\to B\) between Banach star algebras, let \(X\) be a dense star subalgebra on which selfadjoint spectral radii agree.
If \(\phi(x)\) is invertible, approximate its inverse by \(\phi(x_n)\) with \(x_n\in X\).
Both \(\phi((xx_n)(xx_n)^*)\) and \(\phi((x_nx)^*(x_nx))\) tend to the identity.
The spectral-radius hypothesis makes the corresponding elements invertible in \(A\) for sufficiently large \(n\), giving respectively a right and a left inverse for \(x\).
Applied to the actual inclusion \(\ell^1(G)\to C_r^*(G)\), this proves the proposition's full finite-support spectral equality.

<a id="local-use-boundary"></a>
## Boundary for the coefficient-correlation application

The source supplies an existing unconditional-completion obstruction, not a bound on the finite-kernel correlations \(\mathcal C_F\).
Its displayed norm comparison is derived under spectral equivalence of \(A(G)\) and \(C_r^*(G)\), which must not be silently dropped when citing Proposition 8.7.
The project's separate norm argument using continuous evaluation of the identity coefficient, bounded convolution multiplication and coefficientwise absolute values has its own [hypotheses](../../../claims/Yin_C_A0014_v4.md#no-weaker-solid-convolution-norm) and [proof](../../../claims/Yin_C_A0014_v4.md#the-solid-norm-lower-bound).
That argument is not presented as the statement of Proposition 8.7 or as an established novelty result.
Neither this source proposition nor its inspected proof excludes atoms of arbitrary torsion-free amenable group-ring inputs.

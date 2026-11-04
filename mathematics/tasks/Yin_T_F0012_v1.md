---
author: Yin
---

# Brown measure convergence for general polynomials in independent GUE matrices

## Contract

### Question

Fix \(d\geq 1\) and a scalar polynomial \(P\in\mathbb C\langle x_1,\ldots,x_d\rangle\) in self-adjoint indeterminates.
The coefficients and degree of \(P\) are fixed as \(N\to\infty\), and \(P\) may be non-self-adjoint.
For each \(N\), let \(H_1^{(N)},\ldots,H_d^{(N)}\) be independent \(N\times N\) GUE matrices, each with density proportional to \(\exp(-N\operatorname{Tr}(H^2)/2)\) on the Hermitian matrices, where \(\operatorname{Tr}\) is the unnormalized trace.
Let \(s_1,\ldots,s_d\) be freely independent centered semicircular elements of variance one in a finite von Neumann algebra with faithful normal tracial state \(\tau\).
Set \(A_N=P(H_1^{(N)},\ldots,H_d^{(N)})\) and \(a=P(s_1,\ldots,s_d)\).

Let \(\mu_N=N^{-1}\sum_{j=1}^N\delta_{\lambda_j(A_N)}\), counting eigenvalues with algebraic multiplicity, and let \(\mu_a^{\mathrm{Br}}\) be the Brown measure of \(a\) with respect to \(\tau\).
Does \(\mu_N\) converge weakly in probability on \(\mathbb C\) to \(\mu_a^{\mathrm{Br}}\) for every such \(d\) and \(P\)?
The proposed convergence means that for every bounded continuous \(\varphi:\mathbb C\to\mathbb R\),
\[
\frac{1}{N}\sum_{j=1}^N\varphi(\lambda_j(A_N))
  \xrightarrow[N\to\infty]{\mathbb P} \int_{\mathbb C}\varphi\,d\mu_a^{\mathrm{Br}}.
\]

### Scope and starting references

The target is the unperturbed GUE ensemble, including polynomials with nonnormal evaluations.
Almost-sure weak convergence would strengthen the stated target.
[BSS18, arXiv v3, Section 7](https://arxiv.org/html/1506.02017v3#S7) formulates the eigenvalue convergence conjecture for arbitrary polynomials of independent self-adjoint Gaussian matrices.
For \(P=P^*\), convergence of normalized trace moments gives the known self-adjoint case.

Pairing independent GUE matrices as \(G_j=(H_{2j-1}^{(N)}+iH_{2j}^{(N)})/\sqrt{2}\) gives independent complex Ginibre matrices.
[Han26, arXiv v1, Theorem 1.2](https://arxiv.org/html/2606.01664v1#S1) proves weak convergence in probability for polynomials in the \(G_j\) alone, with free circular variables in the limit.
Expressing an arbitrary \(P\) in these coordinates generally introduces \(G_j^*\), the extension identified in [Han26, Question 1.8](../audits/literature/Han26/Yin_U001.md#gue-boundary).

For almost every \(z\in\mathbb C\), the logarithmic potential of \(\mu_N\) is \(N^{-1}\sum_{j=1}^N\log\sigma_j(A_N-zI_N)\), where \(\sigma_j\) are the singular values.
An argument by hermitization must control the logarithmic contribution of small singular values when removing the regularizer after \(N\to\infty\).
The related [affine spectral-potential Task](Yin_T_F0008_v1.md#contract) concerns the limiting operator and supplies context for this distinction.

### Completion criteria

Resolve the assertion either by a proof for every fixed \(d,P\) in the stated ensemble or by a rigorous counterexample within that ensemble.
A counterexample must specify fixed \(d,P,\varphi\), a tolerance \(\eta>0\) and a subsequence along which the probability of an error greater than \(\eta\) stays bounded away from zero.
Completion requires review of the proof or counterexample against this exact contract.

## Current decision
[Selected decision](#decision-full-polynomial-proof)

## Lifecycle and completion

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-11-04T05:32 |
| status | active |
| authority | Yin requested a new F-series Task for the general GUE question with no self-adjointness assumption on the polynomial. |
| reason | The assigned question concerns empirical eigenvalue convergence for the full polynomial class, including the unresolved nonnormal case. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Contract](#contract) | The unperturbed GUE model, weak convergence in probability on the plane and the stated proof or counterexample criteria. |

### Decision full-polynomial-proof

| Field | Value |
| --- | --- |
| date | 2026-11-04T17:35 |
| status | completed |
| authority | Yin authorized continued research along F0028 and parallel investigation of the matrix-coefficient determinant formulas; the existing exact contract permits completion by a full proof with review. |
| reason | C_F0186 proves the assertion for every fixed scalar polynomial in the stated unperturbed GUE ensemble. R_F0190 independently reviews the entire argument and its exact applicability to this contract, finding no unresolved substantive gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Original contract](#contract) | Every fixed scalar polynomial, including nonnormal evaluations, with weak convergence in probability against every bounded continuous real test function. |
| support | [General result](../claims/Yin_C_F0186_v1.md#statement) | The complete general monic-pencil bound and scalar-polynomial Brown-measure conclusion. |
| support | [Complete proof](../claims/Yin_C_F0186_v1.md#argument) | The local geometric estimate, exact linearization and logarithmic-potential passage establishing this contract. |
| review | [Independent whole-chain finding](../audits/reviews/Yin_R_F0190_v1.md#whole-chain-finding) | Explicitly binds this contract and both selected supports, including external-source applicability and the stated inspection limits. |

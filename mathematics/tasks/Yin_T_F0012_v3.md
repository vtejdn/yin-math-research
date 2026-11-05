---
author: Yin
---

# Almost-sure Brown measure convergence for finite-variance Wigner polynomials

This is the finite-variance Wigner extension of the [completed GUE almost-sure contract](Yin_T_F0012_v2.md#contract).
The GUE versions and their exact completion evidence remain preserved.

## Contract

### Input model and question

Fix \(d\ge1\).
For each \(j\), fix a complex off-diagonal law \(\xi_j\) with \(\mathbb E\xi_j=0\) and \(\mathbb E|\xi_j|^2=1\), and a real diagonal law \(\zeta_j\) with \(\mathbb E\zeta_j=0\) and \(\mathbb E|\zeta_j|^2<\infty\).
The laws are independent of \(N\), and no moment of order \(2+\varepsilon\), bounded density, or non-atomicity is assumed.
Real off-diagonal laws are allowed, and the real and imaginary parts of a complex entry need not be independent.

On a common probability space, for every \(N\), form \(d\) independent Hermitian matrices \(W_j^{(N)}\).
Within each matrix, the upper off-diagonal entries are independent copies of \(\xi_j/\sqrt N\), the diagonal entries are independent copies of \(\zeta_j/\sqrt N\), and these families are independent.
The lower entries are the conjugates of the upper entries.
No independence between different sizes is imposed; the standard nested infinite-array coupling is included.

Fix a scalar polynomial \(P\in\mathbb C\langle x_1,\ldots,x_d\rangle\) in self-adjoint indeterminates, with fixed coefficients and degree.
The polynomial need not be self-adjoint.
Let \(s_1,\ldots,s_d\) be free centered variance-one semicircular elements in a finite von Neumann algebra with faithful normal tracial state.
Does
\[
 \mu_N=\frac1N\sum_{k=1}^N\delta_{\lambda_k(P(W^{(N)}))}
 \longrightarrow\mu_{P(s)}^{\mathrm{Br}}
 \quad\text{weakly almost surely on }\mathbb C
\]
hold for every such choice of laws, polynomial and cross-size coupling?
Eigenvalues are counted with algebraic multiplicity.
For each fixed model and polynomial, the conclusion requires one event of probability one on which convergence holds for every bounded continuous real test function on the plane.
The event may depend on the model and polynomial.

### Scope and prior evidence

The completed [GUE theorem](../claims/Yin_C_F0186_v3.md#statement) is a special case with its recorded hypotheses and review.
Its Gaussian concentration and Gaussian tube probabilities do not automatically apply to arbitrary Wigner entries.
Finite-variance self-adjoint spectral convergence and Hermitized spectral convergence are controls for this question; they alone do not settle the nonnormal eigenvalue problem.
The exact linearization remains algebraic, but any new small-singular-value, truncation or logarithmic-potential interface must be justified for this model.

The fixed-law assumption excludes an arbitrary variance-one triangular array whose entry law changes with size without a Lindeberg condition.
No expectation-convergence assertion for unregularized logarithmic determinants is part of this contract.
A failure of such an auxiliary assertion for discrete laws is not a counterexample to the stated weak almost-sure conclusion.

### Completion criteria

Resolve the full assertion by a proof or a rigorous counterexample under these exact finite-variance laws and coupling quantifiers.
A counterexample must identify fixed entry laws, a fixed polynomial, an allowed coupling, a bounded continuous real test function and a positive-probability event of failure.
A self-adjoint special case, Gaussian-smoothed model, convergence only in probability, or a result with extra moment/density assumptions is partial progress rather than completion.
Completion requires review of the complete proof or counterexample against this contract.

## Separate determinant objectives

The separately authorized [matrix-valued affine-pencil Task F0013](Yin_T_F0013_v1.md#contract) and [scalar-valued polynomial Task F0014](Yin_T_F0014_v1.md#contract) study normalized determinant upper-limit equalities under the same fixed-law finite-variance model.
The matrix question is sufficient for the scalar question through exact linearization.
Neither upper-limit conclusion alone completes this Task's full-sequence almost-sure weak convergence, as the [retained separation example](../ledger/Yin_L_F0061_v2.md#brown-nonimplication) explains.
This organization leaves the present contract and selected lifecycle decision unchanged.

## Current decision

[Selected decision](#decision-finite-variance-reopened)

## Lifecycle and completion

### Decision finite-variance-reopened

| Field | Value |
| --- | --- |
| date | 2026-11-05T00:07 |
| status | active |
| authority | Yin explicitly requested reactivating F0012 to investigate almost-sure weak convergence under existence of second moments. |
| reason | The ensemble is broadened from GUE to fixed-law finite-variance Wigner matrices, while retaining the general nonselfadjoint polynomial and almost-sure weak-convergence objective. The existing Gaussian proof does not discharge the new distributional interfaces. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Finite-variance Wigner contract](#contract) | Fixed centered independent Wigner input laws with finite second moments, general scalar polynomials, and one-event almost-sure weak convergence under the stated cross-size couplings. |

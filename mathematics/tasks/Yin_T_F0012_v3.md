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

The [reviewed symmetric-carrier extension](../claims/Yin_C_F0186_v7.md#decision-symmetric-carrier-reviewed) now gives full almost-sure Brown and fixed-parameter determinant limits for its stated real-input class, including nonlinear single-carrier polynomials and noncommuting palindromes.
It does not cover a general nonsymmetric carrier or arbitrary auxiliary matrix coefficients, and therefore supplies partial progress for this unchanged contract.
The [reviewed isolated-minor theorem](../claims/Yin_C_F0194_v1.md#decision-isolated-minor-reviewed) now controls its precisely specified bottom event for real Wigner matrices with arbitrary polynomially bounded nonsymmetric shifts.
That restricted version alone leaves complementary principal-minor branches; the probability-level treatment below still does not supply this Task's full-sequence conclusion.
The [reviewed corank-tail reduction](../claims/Yin_C_F0194_v2.md#decision-corank-tail-reviewed) now excludes full corank at least two for arbitrary polynomially bounded independent nonsymmetric complex shifts and for the original three-real-Wigner product at each fixed nonzero parameter.
This closes that lower-rank branch, while corank one and positive small-singular-value estimates remain outside the rank theorem itself.
The [reviewed many-index and finite-radius reduction](../claims/Yin_C_F0194_v3.md#decision-many-index-reviewed) then replaces the union over possible principal indices by an average for real Wigner matrices with independent nonsymmetric complex shifts.
Its polynomial-shift bound retains the mean probability of low-matching actual minors, which has not been controlled for the original product-inverse shift.
The [reviewed unary refinement](../claims/Yin_C_F0194_v4.md#decision-unary-reviewed) controls an additional low-matching branch with many effective unary coefficients, including the precise distinction between two-point and larger-support laws.
The remaining joint event is explicit, and this restricted estimate supplies no completion of the present full-sequence Brown contract.
The [reviewed nonsymmetric-shift probability floor](../claims/Yin_C_F0194_v5.md#decision-nonsymmetric-floor-reviewed) now controls that tiny-ratio low-matching intersection for real Wigner inputs, using an arbitrary-power second-smallest floor and internal-row exposure.
Its least-value failure probability tends to zero but is not summable as stated; complex input laws, general polynomial propagation and the present full-sequence almost-sure conclusion remain outside this result.
The [reviewed nonsymmetric-carrier assembly](../claims/Yin_C_F0186_v10.md#decision-nonsymmetric-carrier-reviewed) propagates this probability estimate to its real-input carriers and every fixed spectral parameter, with logarithmic convergence in probability and arbitrary-coupling upper-limit equality.
These determinant conclusions do not complete the full-sequence almost-sure Brown contract.
The [reviewed phase-line floor](../claims/Yin_C_F0194_v6.md#decision-phase-line-floor-reviewed) extends the probability estimate to complex off-diagonal laws \(\xi=c\eta\) with fixed unit phase \(\operatorname{Re}c\ne0\) and real centered variance-one \(\eta\).
Its broader auxiliary second-value and rank estimates include every phase, but the pure-imaginary odd-size example excludes an all-size least-value theorem at that boundary; no full Brown conclusion is inferred.

The [reviewed complex-law floor package](../claims/Yin_C_F0194_v7.md#decision-complex-floor-reviewed) extends the probability estimate to all non-line complex laws and gives a symmetric-quantile guarded estimate for purely imaginary inputs, together with an arbitrary-power even-dimensional skew floor.
The [reviewed random-diagonal quantile theorem](../claims/Yin_C_F0194_v8.md#decision-random-diagonal-reviewed) discharges that guard uniformly for every independent nonconstant real diagonal law of finite second moment and hence supplies the all-dimension arbitrary-complex-shift probability floor in that case.
Its remaining matching error is still not summable; the centered constant-diagonal boundary is exactly the zero law.
The [reviewed determinant assembly](../claims/Yin_C_F0186_v11.md#decision-complex-affine-carrier-reviewed) establishes arbitrary-coupling determinant upper limits for every scalar affine tuple, one-variable matrix polynomials and its eligible-exposure complex carrier class.
Its probability limits and dimension upper limits still do not provide this Task's full-sequence almost-sure planar control.

The [reviewed positive-covariance additive theorem](../claims/Yin_C_F0186_v15.md#decision-positive-covariance-additive-reviewed) gives full-sequence Brown limits for an exposed combination satisfying its weighted second-moment criterion, with an arbitrary independent polynomial background and fixed outer polynomials.
Its [independent whole-chain review](../audits/reviews/Yin_R_F0190_v14.md#positive-covariance-additive-whole-proof) checks the [positive mirror-pair floor](../claims/Yin_C_F0194_v11.md#decision-positive-pair-reviewed) and the complete deduction.
One exposed off-diagonal law with \(|E\xi^2|<1\) suffices, while a common phase-line exposed family lies outside this sufficient condition.
The earlier elliptic and conditional versions retain their exact scopes; this larger subclass still does not complete the present arbitrary-polynomial contract.

The [reviewed recursive-carrier theorem](../claims/Yin_C_F0186_v16.md#decision-recursive-carrier-reviewed) extends this full-sequence Brown conclusion to finite certified two-sided carriers with independent polynomial backgrounds and eligible real symmetric seeds.
Its induction supplies arbitrary-power least-value floors and a quantitative intermediate exponent for every node, including the stated outer-polynomial closure.
The certificate requires each newly exposed input to be absent from the whole background; arbitrary repeated-variable polynomials still lie outside this sufficient class.

The [reviewed three-real-product theorem](../claims/Yin_C_F0186_v23.md#decision-three-real-product-reviewed) now proves full-sequence almost-sure Brown convergence for three independent real finite-second-moment Wigner factors under every allowed cross-size coupling.
Its [independent whole-chain review](../audits/reviews/Yin_R_F0190_v22.md#three-real-product-whole-proof) covers the actual structured-companion count application, complete conditional numerator, exhaustive minor branches, arbitrary-power floor and planar passage.
The same theorem gives almost-sure logarithmic limits at each fixed nonreal parameter and at zero, without asserting such a limit at nonzero real parameters.
This resolves that product subclass beyond the earlier probability estimate, while arbitrary polynomials and general complex input laws retain the full present contract.

The [adopted two-class theorem C186v24](../claims/Yin_C_F0186_v24.md#decision-two-real-classes-reviewed) now treats every fresh real additive input plus an arbitrary independent scalar polynomial and every fixed ordered product of independent real Wigner inputs.
It gives arbitrary-power least-value floors, finite-target full-sequence almost-sure logarithms at every fixed complex parameter and one-event Brown convergence under arbitrary cross-size coupling.
Its [independent whole-proof and correction finding](../audits/reviews/Yin_R_F0190_v23.md#two-real-classes-repaired-whole-proof) covers the complete chain, including the explicit additional low-matching exceptional event.
These real-input subclasses do not resolve the general contract; the earlier all-parameter ordered-product limsup conclusion is strengthened rather than newly obtained.

The [reviewed GOE theorem](../claims/Yin_C_F0186_v9.md#decision-goe-parity-reviewed) proves this full Brown-measure conclusion for every scalar polynomial when the entries have the exact normalized real Gaussian laws.
It allows arbitrary cross-size coupling and gives one event for every bounded continuous test function.
This completes the GOE submodel, while the present arbitrary finite-variance contract remains active.

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

---
author: Yin
---

# Dimension-limsup determinants of matrix-valued affine Wigner pencils

## Contract

### Input model

Fix \(d\ge1\).
For each \(j\), the off-diagonal law \(\xi_j\) is a fixed complex law with \(\mathbb E\xi_j=0\) and \(\mathbb E|\xi_j|^2=1\); the diagonal law \(\zeta_j\) is fixed, real, centered and has finite second moment.
For every \(N\), the upper off-diagonal entries of \(W_j^{(N)}\) are independent copies of \(\xi_j/\sqrt N\), its diagonal entries are independent copies of \(\zeta_j/\sqrt N\), and the lower entries are conjugates of the upper ones.
All these families and the \(d\) matrices are independent within each size.
All sizes live on one probability space with arbitrary cross-size coupling.
Real and atomic laws are allowed, and the real and imaginary components of an entry need not be independent.
The entry laws do not vary with \(N\), and no moment above two or density is imposed.
Let \(s_1,\ldots,s_d\) be free centered variance-one semicircular elements in a finite von Neumann algebra with faithful normal tracial state \(\tau\).

### Main question

Fix \(m\ge1\) and arbitrary \(A_0,A_1,\ldots,A_d\in M_m(\mathbb C)\), independently of \(N\), and put
\[
 L_N=A_0\otimes I_N+\sum_jA_j\otimes W_j^{(N)},\qquad
 L=A_0\otimes1+\sum_jA_j\otimes s_j,\qquad
 \tau_m=\operatorname{tr}_m\otimes\tau.
\]
Does
\[
 \limsup_{N\to\infty}\frac1{mN}\log|\det L_N|
 =\log\Delta_{\tau_m}(L)
 \quad\text{almost surely}
 \tag{Matrix-limsup}
\]
hold for every fixed model, coefficient tuple and allowed coupling?
Equivalently, is \(\limsup_N|\det L_N|^{1/(mN)}=\Delta_{\tau_m}(L)\) almost surely?
The event may depend on the fixed tuple, laws and coupling; a common event for all uncountably many tuples is not required.
Use the ordinary FK determinant including zero mass, with \(\log0=-\infty\) and \(\exp(-\infty)=0\).
The coefficients need not be selfadjoint, and the constant matrix may be singular or zero.
Both matrix size \(m\) and the coefficient tuple are fixed as \(N\) grows.

### Scope and completion criteria

Resolve (Matrix-limsup) by a complete proof or a rigorous counterexample under these exact hypotheses and obtain applicable review of that resolution.
A counterexample must specify fixed coefficients and entry laws, an allowed coupling and a positive-probability failure of the displayed equality.
The already available upper bound \(\limsup\le\log\Delta(L)\) alone is not completion.
A GUE-only, scalar-coefficient, monic-only or nondegenerate-covariance result is partial progress for this full affine contract.
The [zero-limit and upper-semicontinuity discussion](../ledger/Yin_L_F0061_v2.md#upper-limit) separates the automatic direction from the unresolved equality.
The [GUE theorem](../claims/Yin_C_F0186_v3.md#statement) and [finite-variance controls](../claims/Yin_C_F0186_v4.md#statement) remain available at their exact existing scopes.
The [real symmetric conditional-shift theorem](../claims/Yin_C_F0188_v2.md#statement) is not a theorem for arbitrary auxiliary matrix coefficients.

Full-sequence fixed-parameter convergence and expectation convergence of unregularized logarithms are not required for completion.
They may be studied as strengthenings only with explicit admissible hypotheses: the [parity and atomic examples](../ledger/Yin_L_F0061_v1.md#real-affine-obstruction) prevent asserting them uniformly in this model.
This Task concerns determinant approximation, separately from the [F0012 full-sequence Brown-measure contract](Yin_T_F0012_v3.md#contract).
The [exact linearization transfer](../ledger/Yin_L_F0061_v2.md#linearization-transfer) explains its sufficient relationship to the [separate scalar determinant question](Yin_T_F0014_v1.md#contract).

For a finite free logarithm, the [reviewed marginal criterion](../claims/Yin_C_F0190_v1.md#decision-coupling-criteria-reviewed) shows that the lower bound under every allowed coupling is equivalent to a vanishing lower limit of each fixed lower-deviation probability.
It is enough to approach the target in probability along a suitable deterministic dimensional subsequence.
This exact reduction supplies no such estimate for the general coefficient tuple; the original equality remains unresolved.

The [reviewed GOE affine theorem](../claims/Yin_C_F0186_v9.md#decision-goe-parity-reviewed) establishes the upper-limit equality for every fixed coefficient tuple in the exact real Gaussian submodel, including singular constant matrices.
It proves the full logarithmic limit along all even dimensions and classifies full-sequence convergence at a finite target by existence of one odd-dimensional real-symmetric invertible witness.
Arbitrary fixed-law finite-variance entries remain outside that Gaussian result.

The [reviewed complex affine and matrix-fiber theorem](../claims/Yin_C_F0186_v11.md#decision-complex-affine-carrier-reviewed) resolves this contract for every scalar coefficient tuple, that is, for all m=1, under the full stated complex finite-variance model.
It also resolves every fixed matrix polynomial in one Hermitian input and the specified real-linear-combination reductions, including arbitrary singular constant matrices.
The finite-target logarithms converge in probability along all even dimensions, with the theorem's exact pure-imaginary zero-diagonal obstruction to a full-sequence probability limit.
Several unrelated matrix coefficient directions remain outside that result, so the original arbitrary-m contract stays active.

The [reviewed positive-frame block theorem](../claims/Yin_C_F0187_v3.md#decision-block-intermediate-reviewed) proves a summable intermediate singular-value bound for fixed matrix coefficients satisfying its additional condition \(\chi_A>0\), with arbitrary constant coefficient \(A_0\).
It also derives a finite free logarithm and controls the intermediate negative-logarithmic range, while leaving the bottom contribution unresolved.
Its actual projected-block and elimination examples show why neither free invertibility nor the ordinary polynomial linearization supplies that frame condition in general.

The [reviewed bounded two-channel theorem](../claims/Yin_C_F0187_v4.md#decision-bounded-two-channel-reviewed) supplies weak physical delocalization and residual inverse row-energy spread for its real bounded model despite a zero one-step frame constant.
It is uniform over single physical deletions and removed eigenmodes, with the residual assertion restricted to the invertible branch without conditioning by its probability.
Fourth-layer noncancellation, singular minors and the bottom logarithm remain outside that theorem, so it does not establish the present determinant equality.

The [reviewed auxiliary Gram and actual cross-energy theorem](../claims/Yin_C_F0187_v5.md#decision-auxiliary-cross-energy-reviewed) now excludes common approximate input eigenvectors, separates the auxiliary components of all eigenmodes, and gives a residual fourth cross-layer energy lower bound for closest-to-zero modes in the same bounded real model.
The last estimate is uniform on the invertible branch and assumes no pole dominance; its actual fresh-row Walsh interpretation requires a single physical deletion and a Rademacher first input.
It does not by itself control cancellation in the complete fourth-layer sum; the whole-layer and graph-normalized results below address two specified coefficient regimes.

The [reviewed two-original-sign-row floor](../claims/Yin_C_F0194_v12.md#decision-two-original-row-reviewed) controls its two-channel pencil and associated quadratic polynomial conditionally on an actual minor with a fixed inverse bound, with a small real exposed-diagonal guard and an exact finite-second-moment diagonal corollary.
Its original off-diagonal rows are Rademacher, its failure rate is not summable, and its minor guard has no asserted high-probability bound; these restrictions prevent completing the present arbitrary-coefficient and arbitrary-law contract.

The [reviewed whole fourth-layer theorem](../claims/Yin_C_F0187_v6.md#decision-whole-layer-rank-reviewed), [operator-gap extension](../claims/Yin_C_F0187_v9.md#decision-operator-gap-reviewed) and [comparable-mode extension](../claims/Yin_C_F0187_v9.md#decision-comparable-modes-reviewed) now cover all invertible inverse-mode regimes in the bounded real two-channel model.
The [reviewed balanced middle theorem](../claims/Yin_C_F0187_v9.md#decision-balanced-middle-reviewed) supplies intermediate logarithmic control despite the degenerate coefficient frame.
The [reviewed unconditional assembly](../claims/Yin_C_F0186_v17.md#decision-bounded-two-channel-reviewed) then eliminates singular minors and the Rademacher restriction by a deterministic whole-parent translation and weighted two-copy conditioning.
The [reviewed diagonal extension](../claims/Yin_C_F0186_v18.md#decision-finite-diagonal-two-channel-reviewed) permits arbitrary fixed centered real diagonal laws with finite second moment while retaining bounded real off-diagonal laws.
For that exact fixed pencil, it proves a \(cN^{-5}\) least-value floor, full-sequence logarithmic convergence in probability and the required arbitrary-coupling almost-sure limsup.
The original arbitrary coefficients and finite-second-moment laws remain outside this submodel, so the contract and selected lifecycle decision stay unchanged.

The [reviewed finite-variance conditional bridge](../claims/Yin_C_F0194_v14.md#decision-finite-variance-graph-reviewed) removes the boundedness and fair-sign restrictions from the row conversion, while allowing an arbitrary independent real symmetric second input.
It retains the actual-minor energy, coordinate-load and graph-area hypotheses and their averaged failure, so it does not establish a general finite-variance floor or the present determinant equality.

The [reviewed original-law physical theorem](../claims/Yin_C_F0187_v10.md#decision-finite-variance-physical-reviewed) establishes almost-sure weighted weak limits, physical resolvent/projector bounds and full inverse-residual spread for that fixed two-channel pencil under arbitrary fixed real finite-second-moment laws.
It is uniform over the stated small physical deletions and permits a deterministic vanishing parent shift.
Visible-residual comparison, complete fourth-layer coercivity and the finite-variance determinant conclusion remain outside its scope.
The [reviewed finite-variance middle theorem](../claims/Yin_C_F0187_v11.md#decision-finite-variance-middle-reviewed) additionally gives a \((j/N)^{3/2}\) intermediate profile beyond \(O(\sqrt{N\log N})\) bottom indices and proves the logarithmic probability conclusion conditional on a separate polynomial least-value floor.
That separate floor is now supplied for this fixed real pencil by the complete finite-variance assembly below; broader coefficients and complex inputs remain outside that result.

The [reviewed finite-variance joint gap](../claims/Yin_C_F0187_v12.md#decision-finite-variance-joint-gap-reviewed) also rules out a common approximate eigenvector of the two original inputs at fixed bounded scalar centers, uniformly through one physical deletion.
It supplies no auxiliary Gram or coefficient-energy conclusion by itself; the later fixed assembly supplies those additional inputs without resolving the original contract.
The [reviewed low-mode Gram theorem](../claims/Yin_C_F0187_v13.md#decision-finite-variance-low-mode-gram-reviewed) separately proves auxiliary Gram separation in every fixed energy range for the same original finite-second-moment real pencil.
Its compressed joint gap and component estimates are uniform over every single deletion and all unit vectors in repeated eigenspaces.
Complete fourth-layer coercivity and the least-value floor remain unresolved by that theorem.

The [reviewed real-parameter extension](../claims/Yin_C_F0186_v19.md#decision-real-parameter-two-channel-reviewed) permits every fixed real \(\alpha\ne1\) and every fixed real quadratic parameter \(t\) in its explicit strict interval.
For nonzero \(t\), its signed selfadjoint linearization has the exponent-five floor and the corresponding logarithmic probability limit and arbitrary-coupling limsup.
The off-diagonal laws remain bounded and real, while the diagonal laws need only finite second moments; general coefficient tuples remain outside this extension.

The [reviewed finite-variance two-channel theorem](../claims/Yin_C_F0186_v20.md#decision-finite-variance-two-channel-reviewed) removes off-diagonal boundedness for the fixed real pencil with identity coupling and \(\alpha=\sqrt2\).
Its [independent whole-chain review](../audits/reviews/Yin_R_F0190_v19.md#finite-variance-two-channel-whole-chain) covers the shifted high-rank and [adopted low-rank](../claims/Yin_C_F0187_v15.md#decision-shifted-finite-variance-low-rank-reviewed) interfaces, actual conditioning, original-matrix transfer and logarithmic deduction.
It proves a \(cN^{-6}\) least-value floor in probability, all-dimension logarithmic convergence in probability and the required almost-sure limsup under every cross-size coupling.
This settles that fixed coefficient tuple with arbitrary real finite-second-moment laws; general matrix coefficients and complex input laws remain unresolved.
No full-sequence almost-sure logarithmic conclusion or completion of this contract is asserted.

The [reviewed three-channel probability floor](../claims/Yin_C_F0194_v16.md#decision-three-channel-sixth-bridge-reviewed) proves an \(aN^{-17/2}\) least-singular-value bound in probability for the fixed real path pencil \(I_3\otimes C+\operatorname{diag}(0,1,\sqrt2)\otimes D+K\otimes I\), where \(K\) is the three-vertex path adjacency matrix.
It allows arbitrary fixed real finite-second-moment input laws and has [independent whole-proof review](../audits/reviews/Yin_R_F0200_v16.md#sixth-original-row-whole-proof).
The [adopted three-channel middle theorem](../claims/Yin_C_F0187_v25.md#decision-three-channel-middle-reviewed) now supplies the separate intermediate negative-logarithmic control.
The [reviewed complete determinant assembly](../claims/Yin_C_F0186_v21.md#decision-finite-variance-three-channel-reviewed), with [independent whole-proof review](../audits/reviews/Yin_R_F0190_v20.md#finite-variance-three-channel-whole-proof), gives a finite free logarithm, all-dimension logarithmic convergence in probability and the required almost-sure limsup under every cross-size coupling for this fixed real coefficient tuple.
Arbitrary matrix coefficients and complex inputs retain the full original obligation; no full-sequence almost-sure logarithmic limit or Task completion is asserted.

The [adopted positive-frame rectangle result](../claims/Yin_C_F0194_v18.md#decision-positive-frame-rectangles-reviewed), with its exact statement in C194v17, supplies all-small-support physical rectangles and norm-guarded distance averaging for arbitrary fixed complex auxiliary coefficients and original complex laws satisfying the positive frame condition.
The separate [adopted low inverse-energy result](../claims/Yin_C_F0194_v18.md#decision-low-inverse-energy-reviewed) controls the complete Schur numerator and graph-distance probabilities on the slowly growing inverse-energy branch for arbitrary fixed real symmetric coefficients, with no positive frame assumption.
Both have independent whole-proof review at their exact scopes.
The [adopted inverse trace-norm extension](../claims/Yin_C_F0194_v20.md#decision-inverse-trace-norm-approximation-reviewed) permits a minor-measurable real symmetric approximation with fixed normalized Frobenius energy and nuclear error o(N), in its real size-three positive-frame free-gap model.
Its [independent whole-proof finding](../audits/reviews/Yin_R_F0200_v22.md#inverse-trace-norm-approximation-whole-proof) covers complete Schur and graph control and, under an additional vanishing mean approximation-failure hypothesis, an original N^(-2) floor, probability logarithms on the stated deterministic dimensions and the every-coupling limsup.
The actual free-gap model has not been shown to satisfy that mean hypothesis; this conditional extension does not settle the free-gap branch or the original contract.
The [adopted spectral-point geometry](../claims/Yin_C_F0187_v26.md#decision-positive-frame-spectral-spread-reviewed) additionally supplies full and fixed-mode-residual inverse-energy divergence, separate physical row and diagonal spread, and head delocalization for real symmetric positive-frame pencils when zero lies in the free spectrum.
The [adopted complete sixth-coefficient theorem](../claims/Yin_C_F0187_v27.md#decision-positive-frame-complete-sixth-reviewed) supplies the corresponding energy, physical-group loads and graph-area comparison for real symmetric auxiliary size three on that spectral-point branch.
The [adopted fixed-input probability interface](../claims/Yin_C_F0194_v19.md#decision-fixed-input-sixth-bridge-reviewed) converts those explicit minor hypotheses into a norm-guarded averaged least-value estimate; both results have independent whole-proof review.
The [adopted spectral-point assembly](../claims/Yin_C_F0186_v22.md#decision-positive-frame-spectral-point-assembly-reviewed) now removes the singular-minor restriction by a common atom-avoiding shift and returns to the original matrix quantitatively.
It proves an N^(-17/2) least-value floor in probability, a finite free logarithm, all-dimension logarithmic convergence in probability and the required every-coupling almost-sure limsup for fixed real symmetric size-three positive-frame coefficients with zero in the free spectral support.
Its [independent whole-proof review](../audits/reviews/Yin_R_F0190_v21.md#positive-frame-spectral-point-assembly-whole-proof) checks the full original-law and logarithmic chain.
The [current coefficient route](../strategies/Yin_S_F0032.md#current-allocation-and-discriminating-tests) retains arbitrary auxiliary dimensions, zero-frame coefficients, nonselfadjoint coefficients and general complex input laws; the later complete free-gap assembly below removes the spectral-position restriction within the stated real size-three positive-frame class.
This coefficient-class theorem is partial progress and does not complete the original arbitrary-coefficient contract.

The [adopted qualitative single-pole theorem](../claims/Yin_C_F0194_v23.md#decision-diffuse-single-pole-reviewed) gives complete Schur and graph control for real symmetric size-three positive-frame coefficients under its single-pole, bounded residual-energy, stable-background and diffuse-mass hypotheses, without a polynomial rate for the residual comparison or a pole upper bound.
The separately [adopted original-model diffusion theorem](../claims/Yin_C_F0194_v24.md#decision-original-diffuse-mass-reviewed) supplies that diffuse mass at vanishing additional average cost, without a full-parent or minor norm bound, using original simultaneous cuts and a regularized principal core.
Both have independent whole-proof review; their original scopes alone do not establish actual single-pole and stable-residual coverage or complete this arbitrary-coefficient contract.
The [adopted low-rank residual and one-mode theorem](../claims/Yin_C_F0194_v25.md#decision-low-rank-residual-reviewed) now removes the separate stable-background condition for bounded-energy residuals with rank-o(N) inverse error, and gives natural-scale physical spread in the real positive-frame model.
In auxiliary dimension three it controls every single-pole magnitude and yields an N^(-9/2) original-parent probability floor and the determinant conclusion under the exact average residual-tightness and shift hypotheses.
Its [independent whole-proof review](../audits/reviews/Yin_R_F0200_v28.md#low-rank-residual-whole-proof) covers that conditional chain, whose one-mode residual-tightness premise is not established by that theorem.

The [adopted high-residual theorem C194v26](../claims/Yin_C_F0194_v26.md#decision-free-gap-high-residual-reviewed) and [adopted bounded-two-mode assembly C194v27](../claims/Yin_C_F0194_v27.md#decision-two-mode-free-gap-reviewed) now bypass that premise and cover the complementary free-gap case.
The complete original-law argument gives a free-gap N^(-15/2) probability floor and, after joining the spectral-point branch, a common N^(-17/2) floor, finite free logarithm, all-dimension logarithmic convergence in probability and every-coupling almost-sure limsup for all fixed real symmetric size-three positive-frame coefficient tuples.
Their independent whole-proof findings [R200v29](../audits/reviews/Yin_R_F0200_v29.md#free-gap-reservoir-whole-proof) and [R200v30](../audits/reviews/Yin_R_F0200_v30.md#two-mode-free-gap-whole-proof) retain the complete conditioning, graph denominator, limit order, original-parent transfer and logarithmic interfaces.
This removes the spectral-position restriction only within that coefficient class; arbitrary auxiliary dimension, degenerate or nonselfadjoint coefficients and general complex input laws remain outside it.
No full-sequence almost-sure logarithmic conclusion or completion of this unchanged contract is asserted.

## Public literature boundary

The [2026-11-05 primary-source comparison](../ledger/Yin_L_F0062_v1.md#wigner-status) found no theorem or counterexample covering this exact contract and identified explicit related conjectures still discussed in 2026.
It does not certify that this precise finite-variance, fixed-parameter, arbitrary-coupling limsup formulation has already been explicitly named as a public open problem.
The distinction between public source status and the repository's internal results is preserved there.
The contract and selected lifecycle decision are unchanged by this literature assessment.

## Current decision

[Selected decision](#decision-separated-determinant-objective)

## Lifecycle and completion

### Decision separated-determinant-objective

| Field | Value |
| --- | --- |
| date | 2026-11-05T03:58 |
| status | active |
| authority | Yin requested separate Tasks for matrix-valued linear-polynomial and scalar-valued polynomial determinants, following the discussion of dimension limsup. |
| reason | The matrix coefficient problem has an independently identifiable analytic obstruction and supplies the scalar determinant problem through exact linearization; the original Brown-measure objective remains separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Matrix-pencil determinant question](#contract) | Ordinary normalized determinant limsup equality for arbitrary fixed affine coefficients under fixed-law finite-variance Wigner inputs and arbitrary cross-size couplings. |

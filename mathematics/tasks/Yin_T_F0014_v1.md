---
author: Yin
---

# Dimension-limsup determinants of scalar-valued Wigner polynomials

## Contract

### Input model and main question

Use exactly the fixed-law finite-second-moment Wigner and free semicircular model in [the matrix-pencil Task](Yin_T_F0013_v1.md#input-model), including real or complex off-diagonal laws, independent diagonal laws, independence within each size and arbitrary cross-size coupling.
Fix an arbitrary scalar-coefficient polynomial \(P\in\mathbb C\langle x_1,\ldots,x_d\rangle\) in selfadjoint indeterminates and an arbitrary deterministic \(z\in\mathbb C\).
The polynomial need not be selfadjoint, and its degree and coefficients do not vary with \(N\).
Does
\[
 \limsup_{N\to\infty}\frac1N\log|\det(P(W^{(N)})-zI_N)|
 =\log\Delta_\tau(P(s)-z)
 \quad\text{almost surely}
 \tag{Scalar-limsup}
\]
hold for every fixed model, polynomial, parameter and allowed coupling?
Equivalently, is \(\limsup_N|\det(P(W^{(N)})-zI_N)|^{1/N}=\Delta_\tau(P(s)-z)\) almost surely?
The ordinary determinant includes every zero singular value, with \(\log0=-\infty\).
The event may depend on the fixed polynomial and parameter; simultaneous validity for all complex parameters on one event is not required.
The formulation at \(z=0\) for all scalar polynomials is equivalent by replacing \(P\) by \(P-z\).
Constants and the exceptional value \(z=P(0)\) are included.

### Relationship to the matrix and Brown objectives

The [matrix-pencil question](Yin_T_F0013_v1.md#contract) is sufficient for this Task by the [exact finite and free determinant identities](../ledger/Yin_L_F0061_v2.md#linearization-transfer).
The auxiliary dimension is fixed, and the normalization changes from \(1/(mN)\) to \(1/N\) by multiplication by \(m\).
The linearization parameter is a corner coefficient, not the ordinary spectral parameter of the full auxiliary matrix.
A proof only for monic pencils gives the direct normalized reduction away from \(z=P(0)\), leaving that fixed exceptional parameter outside this Task's complete scope.
No converse reduction to every matrix-coefficient pencil is assumed.

The [F0012 contract](Yin_T_F0012_v3.md#contract) remains the distinct full-sequence almost-sure weak Brown-measure problem.
Correct pointwise determinant upper limits do not by themselves establish that spectral conclusion, as the [alternating-shift example](../ledger/Yin_L_F0061_v2.md#brown-nonimplication) demonstrates.
An appropriate full-sequence logarithmic or planar-defect estimate is an additional step when using determinant work toward F0012.

### Completion criteria and existing evidence

Resolve (Scalar-limsup) by a complete proof or a rigorous counterexample and obtain applicable review against the exact contract.
A counterexample must identify fixed entry laws, a fixed polynomial and parameter, an allowed coupling, and a positive-probability failure of the equality.
An upper bound alone, an almost-every-parameter assertion omitting exceptional fixed values, or a restricted polynomial or entry-law class is partial progress rather than completion.
Full-sequence convergence and expectation convergence of unregularized logarithms are not part of this primary contract.
The [real commutator and discrete-logarithm obstructions](../ledger/Yin_L_F0061_v1.md#real-affine-obstruction) explain that distinction without refuting the present upper-limit question.

The [GUE pencil result](../claims/Yin_C_F0186_v3.md#statement) supplies the GUE case through linearization.
The [finite-variance controls and cyclic spectral subclasses](../claims/Yin_C_F0186_v4.md#statement) retain their exact distinction between weak spectral convergence and determinant convergence.
The [conditional complex symmetric polynomial classes](../claims/Yin_C_F0186_v6.md#statement) give stronger fixed-parameter logarithmic convergence for their underlying displayed polynomials; their arbitrary outer polynomial images are asserted there only at the Brown-measure level.
No broader determinant conclusion is imported from those spectral results.

The [reviewed symmetric-carrier and polynomial-closure theorem](../claims/Yin_C_F0186_v7.md#decision-symmetric-carrier-reviewed) now proves fixed-parameter full logarithmic limits for its wider real-input carrier class and every fixed outer polynomial.
It also treats finite ordered products of those outputs at zero, allowing dependence and noncommutation between factors.
The [reviewed marginal criterion](../claims/Yin_C_F0190_v1.md#decision-coupling-criteria-reviewed) identifies the exact remaining probability obligation for this Task's arbitrary-coupling upper limit; it does not establish that obligation for general polynomials.

The [reviewed nonsymmetric-carrier theorem](../claims/Yin_C_F0186_v10.md#decision-nonsymmetric-carrier-reviewed) removes every reversal-symmetry restriction from its real-input conditional-factor certificate.
It proves fixed-parameter logarithmic convergence in probability and the required almost-sure upper-limit equality for that class, its two-sided forms, outer polynomials and zero-shift ordered products.
In particular, arbitrary finite ordered products of distinct independent real Wigner inputs are covered at every fixed parameter, including zero.
Arbitrary scalar polynomials and the full complex-input model remain outside that theorem.

For three distinct independent real inputs, the [reviewed product theorem C186v23](../claims/Yin_C_F0186_v23.md#decision-three-real-product-reviewed) strengthens that product conclusion to a full-sequence almost-sure logarithmic limit at each fixed nonreal parameter and at zero, with independent whole-chain review.
The earlier all-parameter limsup result retains its scope; this strengthening supplies no new assertion for arbitrary scalar polynomials or complex input laws.

The [adopted two-class theorem C186v24](../claims/Yin_C_F0186_v24.md#decision-two-real-classes-reviewed) now treats every fresh real additive input plus an arbitrary independent scalar polynomial and every fixed ordered product of independent real Wigner inputs.
It gives arbitrary-power least-value floors, finite-target full-sequence almost-sure logarithms at every fixed complex parameter and one-event Brown convergence under arbitrary cross-size coupling.
Its [independent whole-proof and correction finding](../audits/reviews/Yin_R_F0190_v23.md#two-real-classes-repaired-whole-proof) covers the complete chain, including the explicit additional low-matching exceptional event.
These real-input subclasses do not resolve the general contract; the earlier all-parameter ordered-product limsup conclusion is strengthened rather than newly obtained.

The [reviewed complex affine and carrier theorem](../claims/Yin_C_F0186_v11.md#decision-complex-affine-carrier-reviewed) now proves the required upper-limit equality for every scalar affine polynomial under the full complex finite-variance model, including its exact purely imaginary parity branch.
It also proves the equality for every polynomial in one Hermitian variable or the specified real linear combination, and extends the carrier certificate to arbitrary complex backgrounds when every actually exposed input is not purely imaginary.
The two-sided, outer-polynomial and zero-shift ordered-product conclusions retain their exact scopes there.
The [reviewed carrier extension](../claims/Yin_C_F0186_v12.md#decision-carrier-extension-reviewed) also covers tuples whose inputs each have a fixed real-symmetric or purely imaginary zero-diagonal transpose sign, with even-dimensional probability convergence and the required full-sequence upper limit.
With arbitrary complex backgrounds, it enlarges the eligible exposures to include positive diagonal variance and gives all-dimension probability convergence.
Its exact two-sided, outer-polynomial and ordered zero-shift product closures are retained there.
Arbitrary noncommutative polynomials and purely imaginary zero-diagonal exposures with general complex backgrounds remain outside these two sufficient conditions.

The [reviewed GOE theorem](../claims/Yin_C_F0186_v9.md#decision-goe-parity-reviewed) now proves this upper-limit equality for every fixed scalar polynomial and parameter in the real Gaussian submodel, including \(z=P(0)\).
The logarithms converge along all even dimensions, and the theorem's odd-witness criterion identifies exactly when the finite-target limit holds through every dimension.
This Gaussian submodel does not resolve the arbitrary finite-variance contract.

The [reviewed positive-covariance additive theorem](../claims/Yin_C_F0186_v15.md#decision-positive-covariance-additive-reviewed) gives full-sequence fixed-parameter logarithmic limits for its exposed additive combinations with arbitrary independent polynomial backgrounds and every outer polynomial.
Its strict weighted second-moment criterion, common-phase-line boundary and constant-polynomial cases are explicit; general polynomials without that exposure remain unresolved here.

The [reviewed recursive-carrier theorem](../claims/Yin_C_F0186_v16.md#decision-recursive-carrier-reviewed) further gives full-sequence logarithmic limits at every fixed parameter for its finite certified nodes and their outer polynomials, including the exact constant and zero branches.
It also gives the zero-shift logarithmic limit for finite ordered products of the declared nonzero polynomial factors, allowing dependence and noncommutation between factors.
The certificate retains its exact fresh-exposure and symmetric-seed restrictions; general shifted products without a node certificate and arbitrary scalar polynomials remain unresolved.

The [reviewed two-channel diagonal extension](../claims/Yin_C_F0186_v18.md#decision-finite-diagonal-two-channel-reviewed) also proves this Task's equality for the fixed quadratic polynomial \(P(x,y):=(x+\sqrt2y)(x+y)-1\) at zero, with two arbitrary fixed bounded real off-diagonal laws and fixed centered real diagonal laws having finite second moment.
Its normalized logarithm converges in probability along all dimensions, and its almost-sure limsup equals the finite free logarithm under every cross-size coupling.
The exact finite and free block identities account for the auxiliary normalization factor of two.
This fixed polynomial and parameter do not resolve the original arbitrary-polynomial, arbitrary-parameter and finite-second-moment contract.

The [reviewed real-parameter theorem](../claims/Yin_C_F0186_v19.md#decision-real-parameter-two-channel-reviewed) extends the quadratic conclusion to every fixed real \(\alpha\ne1\) and
\[
 -\frac{(c_\alpha-1-\alpha)^2}{c_\alpha}<t<
 \frac{(c_\alpha+1+\alpha)^2}{c_\alpha},
 \qquad c_\alpha:=\sqrt{2(1+\alpha^2)},
\]
for \((x+\alpha y)(x+y)-t\), under bounded real off-diagonal laws and finite-second-moment diagonals.
It proves the full-sequence probability logarithmic limit and arbitrary-coupling almost-sure limsup throughout that interval, with the exponent-five floor restricted to \(t\ne0\).
The zero parameter uses the existing affine-product result; endpoints and nonreal parameters remain outside this new theorem.

The [reviewed finite-variance two-channel theorem](../claims/Yin_C_F0186_v20.md#decision-finite-variance-two-channel-reviewed) now permits arbitrary fixed real finite-second-moment off-diagonal and diagonal laws for the fixed polynomial \(P(x,y)=(x+\sqrt2y)(x+y)-1\) at zero.
It proves a \(cN^{-6}\) least-value floor, the all-dimension probability logarithmic limit and the every-coupling almost-sure limsup, with [independent whole-chain review](../audits/reviews/Yin_R_F0190_v19.md#finite-variance-two-channel-whole-chain).
Its tail extension and the preceding bounded-law real-parameter extension have different scopes and do not jointly establish an unrestricted finite-variance parameter theorem.
Arbitrary polynomials, parameters and complex input laws remain subject to the original contract.

The [reviewed three-channel probability floor](../claims/Yin_C_F0194_v16.md#decision-three-channel-sixth-bridge-reviewed) proves an \(aN^{-17/2}\) least-singular-value bound in probability for \(P(C,D)=(C+\sqrt2D)(C+D)C-2C-\sqrt2D\) at zero, under arbitrary fixed real finite-second-moment input laws.
Its exact pencil-to-cubic inverse transfer and original-law probability argument have [independent whole-proof review](../audits/reviews/Yin_R_F0200_v16.md#sixth-original-row-whole-proof).
The [reviewed complete three-channel assembly](../claims/Yin_C_F0186_v21.md#decision-finite-variance-three-channel-reviewed) now combines the floor with the [adopted middle estimate](../claims/Yin_C_F0187_v25.md#decision-three-channel-middle-reviewed) to prove a finite free logarithm, all-dimension logarithmic convergence in probability and the required every-coupling almost-sure limsup for this ordered cubic at zero.
Its [independent whole-proof review](../audits/reviews/Yin_R_F0190_v20.md#finite-variance-three-channel-whole-proof) checks the finite/free identities and normalization factor three.
This includes the exceptional parameter \(P(0)=0\); arbitrary polynomials, other parameters and complex inputs remain outside the result, so the full Task is unchanged.

The [adopted positive-frame spectral-point pencil theorem](../claims/Yin_C_F0186_v22.md#decision-positive-frame-spectral-point-assembly-reviewed) supplies a further conditional linearization interface only when the actual chosen pencil has real symmetric size-three coefficients, positive complex-direction frame, original real inputs and zero in its free spectral support.
Its [exact scalar-application boundary](../claims/Yin_C_F0186_v22.md#scope-and-provenance) supplies neither such a certificate for an arbitrary scalar polynomial nor a least-value transfer from a determinant identity alone.
The [adopted two-mode and free-gap assembly C194v27](../claims/Yin_C_F0194_v27.md#decision-two-mode-free-gap-reviewed), with [independent whole-proof review](../audits/reviews/Yin_R_F0200_v30.md#two-mode-free-gap-whole-proof), removes the spectral-position restriction for that real symmetric size-three positive-frame coefficient class.
Its application to a scalar polynomial still requires an actual linearization satisfying every remaining hypothesis and the exact finite/free determinant normalization.
It supplies no such certificate for arbitrary polynomials, no general complex-input extension, and no automatic floor transfer or Brown conclusion.

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
| authority | Yin requested a separate scalar-valued polynomial determinant Task alongside the matrix-valued linear-polynomial determinant Task. |
| reason | The scalar determinant question has its own fixed-parameter and dimension-limsup completion criteria; linearization is a sufficient route and does not replace the distinct F0012 spectral target. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Scalar-polynomial determinant question](#contract) | Ordinary normalized determinant limsup equality for every fixed scalar polynomial and fixed complex shift in the stated finite-variance model. |

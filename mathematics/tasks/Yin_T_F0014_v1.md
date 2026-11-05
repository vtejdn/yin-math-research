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

The [reviewed GOE theorem](../claims/Yin_C_F0186_v9.md#decision-goe-parity-reviewed) now proves this upper-limit equality for every fixed scalar polynomial and parameter in the real Gaussian submodel, including \(z=P(0)\).
The logarithms converge along all even dimensions, and the theorem's odd-witness criterion identifies exactly when the finite-target limit holds through every dimension.
This Gaussian submodel does not resolve the arbitrary finite-variance contract.

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

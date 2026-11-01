---
author: Yin
---

# Selfadjoint Affine Dyson Reduction

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_F0008_v1](../tasks/Yin_T_F0008_v1.md#yin_t_f0008) | Yin_C_F0121-Yin_C_F0122/Yin_C_F0125 retain smaller scoped formulas; Yin_C_F0126 resolves the structured indefinite extension to all complex coefficients |

## Route

| Field | Value |
| --- | --- |
| disposition | completed |
| priority | Selfadjoint and indefinite interface established |

The Route section owns the current allocation.
Dated outcomes, earlier authorizations and superseded allocations below retain their recorded scope.

<a id="s_f0018"></a>
Goal: [Yin_T_F0008](../tasks/Yin_T_F0008_v1.md#yin_t_f0008), second milestone and a restricted route toward the first.
Priority and disposition belong to the [route selection](#route).

Updated: 2026-09-13.
The selfadjoint deliverable and its connection to the general affine problem are completed; the successive restricted regimes remain part of the evidence.

## Mechanism and Exact Target

Assume all coefficient matrices, including the drift, are selfadjoint.
Work directly with the m by m equation instead of hermitizing to size 2m.
Here the drift and covariance determine the operator-valued semicircular distribution; Yin_C_F0119's phase-loss obstruction for general complex coefficients does not apply.

Use the [smaller exact primitive](../claims/Yin_C_F0119_v1.md#basic-checks-and-simpler-cases) as a baseline.
Seek global extrema, restricted spectral-gap principles or a precisely justified saddle formula.
Distinguish a valid restricted positive-resolvent domain from an arbitrary real algebraic branch at zero.

## Completed Deliverable and Reopening Conditions

[Yin_C_F0121](../claims/Yin_C_F0121_v1.md#yin_c_f0121) supplies the smaller matrix-supersolution minimum for positive pencils, with negative pencils handled by sign reversal.
[Yin_C_F0122](../claims/Yin_C_F0122_v1.md#isotropic-covariance-minimax) covers every real spectral parameter for isotropic covariance.
[Yin_C_F0125](../claims/Yin_C_F0125_v1.md#yin_c_f0125), with its [review](../audits/reviews/Yin_R_F0125_v1.md), gives a separate ordered matrix minimax under its explicit strict Hilbert-Schmidt covariance positivity; the obstruction to removing that hypothesis remains retained.

[Yin_C_F0126](../claims/Yin_C_F0126_v1.md#yin_c_f0126) resolves the structured indefinite Schur action needed to connect this route with arbitrary complex coefficients.
Its final trial matrices have the original size, while its proof uses hermitization to select the physical branch.
Its independent review (original material now separated into [Yin_R_F0128_v1](../audits/reviews/Yin_R_F0128_v1.md), [R_F0174 determinant-presentation finding](../audits/reviews/Yin_R_F0174_v1.md#determinant-presentation-finding)) covers both the global extremum and full MS24 recovery.
This supplies the required generalization without extending the positive-pencil supersolution argument by assumption.

[Yin_C_F0127](../claims/Yin_C_F0127_v1.md#yin_c_f0127) and its [review](../audits/reviews/Yin_R_F0180_v1.md#current-affine-attainment) identify attainment exactly with bounded invertibility.
For positive selfadjoint pencils, the new optimizer is \(E(S^{-2})\), whereas Yin_C_F0121 uses \(E(S^{-1})\); these are distinct variables, and an expectation does not preserve their square.
The [formula comparison](../ledger/Yin_L_F0033_v1.md#comparison-of-formulas-and-proof-inputs) and [contract review](../audits/reviews/Yin_R_F0126_v1.md) document how the selfadjoint and general targets meet.

No further step remains for the selected selfadjoint deliverable.
Reopen Yin_S_F0018 for a concrete defect in a stated regime, branch selection or the signed reduction.
An unrestricted version of the particular Yin_C_F0125 minimax, new nonsemicircular/rational scope, rates or priority claims are separate possible projects.
This completion does not erase the narrower formulas or assign them a mathematical Role.

## Evidence and Changes

- 2026-09-13, another AI agent, coordinated with the coordinating agent: completed, active to completed.
  The reviewed Yin_C_F0121/Yin_C_F0122/Yin_C_F0125 regimes and independent Yin_C_F0126 signed-Schur proof fulfill the smaller-matrix study and its required indefinite-to-general connection; Yin_C_F0127 resolves the attainment/gap interface.
  Related Yin_S_F0017, Yin_S_F0019, Yin_S_F0021 and Yin_S_F0022 are linked by the synthesis, with no remaining obligation transferred from this route.
  Reopen only under the conditions above.

The earlier entries record the state and allocation at their dates; their active/open wording is historical.

- The coordinating agent: Yin_C_F0124 now covers all selfadjoint affine pencils and agrees with Yin_C_F0121 on its positive regime.
  Under the user's added parallel-exploration direction, this route remains active for other general formulations, including an ordinary matrix-inequality/signature extension through Yin_S_F0022.
  Yin_C_F0121's positivity certificate remains a distinct useful conclusion.

- The coordinating agent: added and activated as the user-selected simplification.
  No selfadjoint result is automatically extended to arbitrary complex coefficients.
- The coordinating agent: [Yin_C_F0121](../claims/Yin_C_F0121_v1.md#decision-candidate-0004) proves the matrix-inequality minimum for every strictly positive pencil, with sign reversal covering strictly negative ones.
  [Yin_C_F0122](../claims/Yin_C_F0122_v1.md#decision-candidate-0004) covers isotropic covariance with arbitrary selfadjoint drift and every real spectral parameter.
  General indefinite pencils and positive spectral-edge boundaries remain separate; next connect the [ordered-minimax](Yin_S_F0021.md#s_f0021) and [signed-Schur](Yin_S_F0022.md#s_f0022) tests.

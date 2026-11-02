---
author: Yin
---

# A Variational Formula for a Signed Schur Pencil

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_F0008_v1](../tasks/Yin_T_F0008_v1.md#yin_t_f0008) | Yin_C_F0126 resolves the structured indefinite Schur extremum for every complex pencil; Yin_C_F0127 gives exact unique attainment and spectrum |

## Route

| Field | Value |
| --- | --- |
| disposition | completed |
| priority | Independent general formula established |

## Feedback and lineage

| Relation | Source | Scope |
| --- | --- | --- |
| predecessor | [Yin_S_F0021](Yin_S_F0021.md#s_f0021) | General-formula work is absorbed through different signed Schur variables; the predecessor restricted theorem and failed raw candidate are not promoted. |

The Route section owns the current allocation.
Dated outcomes, earlier authorizations and superseded allocations below retain their recorded scope.

<a id="s_f0022"></a>
Goal: [Yin_T_F0008](../tasks/Yin_T_F0008_v1.md#yin_t_f0008).
Origin: the coordinating agent added this strategy on 2026-09-12 after the positive-pencil formulas and ordered minimax suggested separating positive and negative Schur blocks.
Priority and disposition belong to the [route selection](#route).

## Exact Reduction and Target

The [signed Schur factorization](../ledger/Yin_L_F0033_v1.md#signed-schur-linearization) identifies every regularized determinant Delta_epsilon(S) with the determinant of the selfadjoint affine pencil [[epsilon squared I,S],[S*,-I]].
The factorization and normalized determinant identity are elementary checked inputs; no extremum is inferred from them.

Find a genuine ordered variational principle for this indefinite pencil class, using freely chosen finite matrices.
Its fixed negative Schur block may allow a separate maximization or elimination step.
Keep the domains, inertia or positivity constraints, and physical-branch selection explicit.

## Achieved Result and Route Lineage

[Yin_C_F0126](../claims/Yin_C_F0126_v1.md#yin_c_f0126), which has a [complete signed-Schur self-review](../audits/reviews/Yin_R_F0128_v1.md#general-signed-schur-finding) and a separately scoped [determinant-presentation self-review](../audits/reviews/Yin_R_F0174_v1.md#determinant-presentation-finding), achieves this target for arbitrary complex affine semicircular coefficients.
At positive regularization it gives an ordered minimum over two positive Schur variables after a maximum over a free complex off-diagonal variable.
A positive Stein equation proves that every critical point has the required signs and hence is the physical Dyson solution.
Rescaling the positive variable removes the regularization parameter and gives a direct infimum over all positive definite matrices.
The zero-mean specialization recovers the full MS24 capacity formula, including zero capacity.

This is an independent derivation, not a reformulation of Yin_C_F0124.
The earlier [circular comparison proof](../ledger/Yin_L_F0032_v1.md) remains a separate successful precursor.
The resulting direct formula also achieves [Yin_S_F0024](Yin_S_F0024.md#s_f0024)'s target.
General-formula work from [Yin_S_F0021](Yin_S_F0021.md#s_f0021) is absorbed here through these Schur variables; its restricted Yin_C_F0125 and the failure of its unrestricted raw minimum-maximum are preserved there, not promoted to unrestricted statements.

The subsequent [Yin_C_F0127 attainment result](../claims/Yin_C_F0127_v1.md#yin_c_f0127), with [its independent review](../audits/reviews/Yin_R_F0180_v1.md#current-affine-attainment), identifies a finite critical point, attainment of the infimum, and bounded invertibility as equivalent conditions.
The minimizer is unique when it exists.
Applied to shifts, this detects the full spectrum by nonattainment; it does not identify the spectrum with Brown-measure support.

The stated variational deliverable has no remaining proof obligation.
A concrete challenge to Yin_C_F0126 or its audited reductions would justify reopening this route; broader refinements require an explicit follow-up allocation.
Route completion makes no goal-completion or manuscript-selection decision.

## Historical Discriminating Steps and Boundary

First solve the scalar Schur-block problem and compare its reduced objective with [Yin_S_F0021](Yin_S_F0021.md#s_f0021).
Then test whether the positive-variable block can use the [Yin_S_F0020 action](Yin_S_F0020.md#s_f0020).
A successful finite-epsilon formula would cover arbitrary affine complex coefficients through the recorded factorization; passing to epsilon zero remains an explicit final step.

At the initial checkpoint the structured indefinite extremum was unproved.
The positive-pencil minimum could not be used unchanged because the Schur pencil has both signs.
No general matrix saddle theorem or convexity assertion was imported from outside the local repository.

## Evidence and Changes

- 2026-09-13, the Task-contract agent, coordinated with the coordinating agent: completed (`active` to `completed`) after Yin_C_F0126 passed independent review.
  The signed Schur extremum, removal of regularization, arbitrary complex coefficient scope and full MS24 specialization discharge the stated deliverable.
  This route absorbs Yin_S_F0021's general-formula allocation and supplies Yin_S_F0024's direct positive-matrix formula; Yin_C_F0127 supplies the reviewed attainment boundary.
  Earlier raw-signature failures remain recorded, and no broader U/V minimum-maximum is asserted.
  The coordinating agent coordinates the corresponding route-index updates; no additional work is selected within this completed deliverable.

- The coordinating agent: activated under the user's added direction to continue independent parallel exploration after Yin_C_F0124.
  The [signed-inequality exploration](../ledger/Yin_L_F0032_v1.md) seeks a formula closer to Yin_C_F0121's ordinary matrix inequalities.
  Yin_C_F0124 already gives a general value by ordinary hermitization, but does not supply the signed-block extremum sought here.
  Thus this route is an alternative-formulation task, not an unresolved prerequisite of Yin_C_F0124.

- The coordinating agent: added as a proposed strategy with a proved algebraic reduction.
  The first selected continuation remains Yin_S_F0021's reduced-Hessian test; this complementary route is ready for activation when its scalar block test is undertaken.

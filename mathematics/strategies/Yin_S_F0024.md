---
author: Yin
---

# Direct Positive-Matrix Affine Capacity

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_F0008_v1](../tasks/Yin_T_F0008_v1.md#yin_t_f0008) | Yin_C_F0126 gives the unrestricted positive-matrix infimum and full MS24 scaling; benchmark-derived reformulations retain their separate provenance |

## Route

| Field | Value |
| --- | --- |
| disposition | completed |
| priority | Direct capacity formula established |

The Route section owns the current allocation.
Dated outcomes, earlier authorizations and superseded allocations below retain their recorded scope.

<a id="s_f0024"></a>
Goal: [Yin_T_F0008](../tasks/Yin_T_F0008_v1.md#yin_t_f0008).
Added by the coordinating agent on 2026-09-13 after the user explicitly requested parallel independent exploration beyond the searched formula.
Priority and disposition belong to the [route selection](#route).

## Target and Mechanisms

Seek an affine analogue of capacity expressed directly through ordinary positive trial matrices, determinant ratios and mean-dependent terms.
Prefer a formula whose zero-mean specialization visibly becomes ordinary capacity.
Test whether two-sided scaling, a positive matrix certificate, circular information-plus-noise structure, or a controlled mixed-covariance term can accomplish this at the full complex coefficient scope.

The [Yin_C_F0124 formula](../claims/Yin_C_F0124_v1.md#yin_c_f0124) is an exact benchmark, not the prescribed final answer.
A reformulation of Yin_C_F0124 must be labeled as such.
An independent derivation requires its own global variational proof.
Covariance-only formulas that discard the mixed products are already obstructed by Yin_C_F0119 and should not be proposed unchanged.

## Achieved Direct Formula

[Yin_C_F0126](../claims/Yin_C_F0126_v1.md#yin_c_f0126) achieves the full target through the independent [Yin_S_F0022 signed Schur route](Yin_S_F0022.md#s_f0022).
It expresses the determinant as an infimum over all positive definite matrices, using a determinant ratio and a mean-dependent term obtained from a finite real-linear solve.
The mixed covariance is retained for arbitrary complex coefficients.
There is no residual regularization parameter or Hilbert--Schmidt feasibility constraint.
At zero mean the correction vanishes, and positive scaling reduces the remaining determinant ratio directly to ordinary capacity at the full MS24 scope, including zero capacity.
The complete proof passed independent review (original material now separated into [Yin_R_F0128_v1](../audits/reviews/Yin_R_F0128_v1.md), [R_F0174 determinant-presentation finding](../audits/reviews/Yin_R_F0174_v1.md#determinant-presentation-finding)).

[Yin_C_F0127](../claims/Yin_C_F0127_v1.md#yin_c_f0127), with [independent attainment review](../audits/reviews/Yin_R_F0180_v1.md#current-affine-attainment), further proves that this infimum has a finite critical point or a minimizer exactly when the pencil is boundedly invertible; that point is unique.
This provides the exact boundary of attainment rather than assuming an optimizer exists for every pencil.

The direct formula is proved independently of Yin_C_F0124.
The [positive-certificate reformulation](../claims/Yin_C_F0164_v1.md#statement) remains a benchmark-derived alternative and is not counted as another independent general proof.
The [original-size positive-pair formula](../claims/Yin_C_F0165_v1.md#statement), [independent scalar elliptic formula and obstructions](../claims/Yin_C_F0166_v1.md#statement), [circular precursor](../claims/Yin_C_F0167_v1.md#statement) and [circular-potential/signature boundary](../claims/Yin_C_F0168_v1.md#statement) retain their exact separate dependencies and current self-review findings.
The circular precursor and earlier two-sided-scaling tests remain in their original records.
No claim of novelty or final manuscript-form selection follows from completing this route.

No obligation remains for the stated direct-capacity target.
Reopen for a concrete defect in the general formula or its centered reduction; additional computational or expository preferences are separate follow-up work.

## Historical Parallel Work and Decision Tests

The [direct-capacity exploration](../ledger/Yin_L_F0028_v1.md) investigates independent information-plus-noise and two-sided scaling mechanisms.
The [positive-certificate reformulation](../ledger/Yin_L_F0031_v1.md) tests whether the benchmark's large Hilbert--Schmidt inequality and inverse can be replaced by ordinary matrix certificates and an explicit inner extremum.

Compare trial dimensions, feasible-domain transparency, extremum order, singular cases and the exact zero-mean reduction.
Check deterministic, scalar bulk/exterior, circular and phase-sensitive covariance examples.
Retain a restricted result at its actual scope while continuing toward a general formula.

## Evidence and Changes

- 2026-09-13, the Task-contract agent, coordinated with the coordinating agent: completed (`active` to `completed`).
  Yin_C_F0126, obtained through Yin_S_F0022 and independently reviewed, supplies the requested direct positive-matrix formula at arbitrary complex coefficient scope with the full zero-mean MS24 reduction.
  Yin_C_F0127 settles its attainment boundary.
  Yin_C_F0124-derived certificates retain their provenance, and unsuccessful or restricted probes remain preserved.
  The coordinating agent coordinates the route-index update; no further obligation remains for this deliverable.

- 2026-09-13: activated as a parallel route under the user's added direction.
  Yin_C_F0124 and its source provenance remain unchanged; no final formula or manuscript designation is selected by this route's creation.

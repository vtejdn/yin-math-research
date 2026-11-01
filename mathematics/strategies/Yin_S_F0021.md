---
author: Yin
---

# Ordered Minimax, Scalarization and Stability

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_F0008_v1](../tasks/Yin_T_F0008_v1.md#yin_t_f0008) | Restricted Yin_C_F0125 is proved; the raw unrestricted U/V candidate is refuted; Yin_C_F0126 supplies the general extremum through different variables |

## Route

| Field | Value |
| --- | --- |
| disposition | superseded |
| priority | General target absorbed by Yin_S_F0022 |

## Feedback and lineage

| Relation | Source | Scope |
| --- | --- | --- |
| predecessor | [Yin_S_F0017](Yin_S_F0017.md#s_f0017) | Ordered-real/imaginary successor added 2026-09-12; retain its restricted result and unrestricted negative-direction obstruction. |

The Route section owns the current allocation.
Dated outcomes, earlier authorizations and superseded allocations below retain their recorded scope.

<a id="s_f0021"></a>
Goal: [Yin_T_F0008](../tasks/Yin_T_F0008_v1.md#yin_t_f0008).
Origin: the coordinating agent added this strategy on 2026-09-12 under the authorized variational exploration.
Priority and disposition belong to the [route selection](#route).

## Mechanism and Current Evidence

The [scalar and isotropic-covariance derivation](../claims/Yin_C_F0122_v1.md) maximizes an imaginary-part variable first.
The resulting real-part objective is strictly convex and selects the physical branch on both sides of spectral edges.
The ordered optimizer need not be a global saddle of the unprocessed objective.
Isotropic covariance already permits arbitrary selfadjoint drift and noncommuting noise coefficients.

The [positive real-gap formula](../claims/Yin_C_F0121_v1.md) instead uses a stable positive supersolution to select a valid matrix domain.
These two mechanisms suggest testing positivity and stability of the reduced Hessian after an inner optimization, rather than imposing a global convex-concave assertion on the raw Dyson action.

## Established Scope, Failure and Successor

[Yin_C_F0125](../claims/Yin_C_F0125_v1.md#yin_c_f0125) passed [independent complete-proof review](../audits/reviews/Yin_R_F0125_v1.md).
For selfadjoint coefficients, including an arbitrary selfadjoint mean, and a completely positive covariance that is strictly positive as a Hilbert--Schmidt operator, it gives an attained minimum over a Hermitian variable after a maximum over a positive semidefinite variable.
The proof permits noncommuting drift and noise coefficients.
This completes the restricted matrix minimum-maximum subproblem; it does not cover arbitrary covariance or every zero-capacity case of MS24.

The same review verifies an [exact counterexample](../claims/Yin_C_F0125_v1.md#negative-hs-minimax-obstruction) to removing Hilbert--Schmidt positivity from that formula: covariance conjugation by the diagonal Pauli matrix and a nonzero off-diagonal Pauli mean give a proposed value strictly below the actual determinant.
Thus the unchanged unrestricted minimum-over-U/maximum-over-V formula is refuted.
The [negative-direction continuation](../ledger/Yin_L_F0030_v1.md) also records failure of a raw covariance-signature saddle test.
That local failure does not by itself refute every reordered signed value formula; the proposed balanced-signature continuation has no general proof.

The general-formula allocation is superseded by [Yin_S_F0022](Yin_S_F0022.md#s_f0022).
Its independently reviewed [Yin_C_F0126](../claims/Yin_C_F0126_v1.md#yin_c_f0126) uses different Schur variables and a positive Stein equation to obtain the full complex coefficient formula and the full MS24 specialization.
It does not prove the failed U/V extension or the unproved balanced-signature candidate.
The latter remains a recorded optional alternative, with global extremum ordering and degenerate-covariance cases unresolved, and is not selected for further work in this route.
Yin_C_F0125 remains a useful independent restricted formula.

Reinstating this route requires a deliberate allocation to its original ordered-real/imaginary mechanism, with a concrete change that addresses the recorded negative-direction obstruction and with ownership reconciled against Yin_S_F0022.
General-formula obligations are already discharged by the successor; no goal-state decision is made here.

## Historical Next Discriminating Steps

1. Extend the scalarized proof to a covariance preserving a finite commutative matrix subalgebra, with a precise symmetric covariance matrix.
   Check whether eliminating the positive imaginary variables makes the remaining Hessian nonnegative.
   Separate positivity of map entries from positivity of that covariance matrix as a quadratic form.
2. For an invertible covariance that is positive as a Hilbert-Schmidt operator, test a quadratic dual action involving its inverse and the determinant of a complex matrix.
   This is only a candidate mechanism; prove attainment, the order of extrema and the physical-branch comparison, or record an explicit counterexample.
3. Compare the positive-supersolution spectral-radius certificate with this reduced Hessian.
   Seek a condition that remains meaningful in the spectral bulk and can replace the positive-resolvent interval.

The scalar elliptic family in the [spectral module](../claims/Yin_C_F0123_v1.md#scalar-tests-that-preserve-the-missing-covariance) is the next nonselfadjoint consistency test.
A valid general formula must preserve its covariance phase information and its line-supported degeneration.

## Evidence and Changes

- 2026-09-13, the Task-contract agent, coordinated with the coordinating agent: superseded (`active` to `superseded`) by Yin_S_F0022 for the general-formula allocation.
  Yin_C_F0125 completes the reviewed strictly Hilbert--Schmidt-positive subproblem, while its raw unrestricted extension is refuted by the reviewed counterexample.
  Yin_C_F0126 achieves the unrestricted target through different variables; it leaves the separate balanced-signature candidate unproved and unselected.
  Earlier evidence is preserved.
  The coordinating agent coordinates the route-index and lineage updates; no duplicate general exploration remains assigned to Yin_S_F0021.

- The coordinating agent, earlier checkpoint: [coupled-diagonal exploration](../claims/Yin_C_F0125_v1.md) recorded a restricted matrix-covariance argument, then not yet registered or independently reviewed.
  After Yin_C_F0124 passed review, the user required continued parallel independent exploration.
  At that checkpoint the route remained active for a general ordered matrix minimax; inverse-M-matrix and Hilbert--Schmidt-positive restrictions were steps to examine, not replacements of the full target.

- The coordinating agent: added and activated after the ordered scalar formula succeeded and the isotropic extension was derived.
  Parent [Yin_S_F0017](Yin_S_F0017.md#s_f0017) remains the general target; [Yin_S_F0018](Yin_S_F0018.md#s_f0018) and [Yin_S_F0019](Yin_S_F0019.md#s_f0019) supply the positive-gap and spectral tests.

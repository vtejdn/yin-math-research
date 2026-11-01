---
author: Yin
---

# Structural Conditions for Analytic Rationality

## Task associations

| Task | Scope |
| --- | --- |
| [R-diagonal and transport contract](../tasks/Yin_T_F0009_v1.md#contract) | Structural residual/realization conditions, homogeneous norm estimates and quantitative regularity for the inherited R-diagonal and analytic-transport models; rational L2 boundedness and bounded scalar reconstruction remain separate. |
| [Expanded model contract](../tasks/Yin_T_F0001_v1.md#expanded-affiliated-and-boundedness-contract) | Historical selected model scope: Structural residual/realization conditions, Haagerup/RD estimates and quantitative differential regularity for the inherited models; distinct L2 and bounded scalar targets |
| [General bounded-closure contract](../tasks/Yin_T_F0003_v1.md#contract) | Bounded scalar reconstruction component: structural conditions and the existing model routes; the completed sufficient-condition round does not settle every model or the distinct rational L2 target |

## Route

| Field | Value |
| --- | --- |
| disposition | active |
| priority | Model coordination |

## Feedback and lineage

| Relation | Source | Scope |
| --- | --- | --- |
| predecessor | [Yin_S_F0004](Yin_S_F0004.md#s_f0004) | Broader structural successor to the model-specific residual mechanism, authorized 2026-09-09; the old model route remains paused. |

The Route section owns the current allocation.
Dated outcomes, earlier authorizations and superseded allocations below retain their recorded scope.

<a id="s_f0007"></a>
The [historical 2026-09-27 allocation](../tasks/Yin_T_F0001_v2.md#reorganization-authorization-2026-09-27) names a separate R-diagonal and analytic-transport Task as the destination of this programme.
The corresponding contract is [T_F0009](../tasks/Yin_T_F0009_v1.md#contract), which owns both inherited model properties and their remaining completion obligations.
This coordinating route retains its recorded active disposition and structural mechanisms for the residual R-diagonal and analytic-transport programme.
Current disposition and priority are owned by the [route selection](#route).

Original authorization: user-requested follow-up to [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001), 2026-09-09.
The user explicitly requested this strategy and investigation of regularity conditions, including conjugate variables and finite free Fisher information.
The exact associations above retain the earlier model selection and the bounded-reconstruction component of the completed general bounded-closure Task; the corresponding T_F0009 contract above identifies the destination, without authorizing current execution.

Lineage: a broader structural successor to the model mechanism in [Yin_S_F0004](Yin_S_F0004.md#s_f0004), informed by the resolved affiliated criterion Yin_C_F0013 and the Yin_C_F0012/Yin_C_F0014 counterexamples.
The original Yin_T_F0001 conjecture remains refuted.
This route records an authorized exploratory program, not a replacement universal conjecture.

## Two Exact Targets

For finite normal generating tuples where the relevant embedded free field is justified, set

\[
A_X=\mathbb C\langle X\rangle,\quad F_X=\operatorname{Div}_{U(M)}A_X,
\quad\mathcal R_X=\operatorname{Div}_M A_X.
\]

Seek structural, independently checkable conditions giving one or both of:

1. **Square-integrable rational boundedness:** $F_X\cap L^2(M)\subseteq M$.
2. **Bounded scalar reconstruction:** $F_X\cap M=\mathcal R_X$.

These are separate properties.
[Yin_C_F0013](../claims/Yin_C_F0013_v1.md#yin_c_f0013) already settles the general affiliated finite-defect characterization under the original normal/bounded-dual setting.
The meaning of bounded scalar reconstruction is fixed in [the precise conventions](../ledger/Yin_L_F0013_v1.md#rationality-conventions).
A result for one property is not automatically a result for the other.

## Checked Mechanisms and Obstructions

- [Yin_C_F0015](../claims/Yin_C_F0015_v1.md#yin_c_f0015), at its current material decision, isolates the scalar analytic step: finite residual/Hankel structure and a subexponential homogeneous norm estimate imply boundedness.
  Its hypotheses must be derived from the candidate model, not asserted as a definition of regularity.
- [Miy26-U002](../audits/literature/Miy26/Yin_U002.md#miy26-u002) and the exact free Haar variant in Miy26-U003 are established positive models.
  Their coefficient, regularization and bounded-intersection inputs remain separate.
- [Yin_C_F0016](../claims/Yin_C_F0016_v1.md#yin_c_f0016), at its current material decision, tests finite free Fisher information against the existing examples.
  In the selfadjoint bounded-dual setting, L2 conjugate variables already exist.
  Thus their bare existence is not additional regularity capable of excluding Yin_C_F0012/Yin_C_F0014.
  Its beta-law example also excludes bounded Lipschitz conjugates alone as a sufficient condition for rational L2 boundedness; it does not exclude bounded scalar reconstruction under that stronger hypothesis.
- Yin_C_F0007's finite-dimensional rational derivative factors in $L^2(M)$ are not automatically finite-dimensional coefficient residuals in an orthogonal basis.
  Finite-dimensional state realizations in the free field also do not imply square integrability of every inverse entry.
- [Miy22-U005, Lemma 3.8](../audits/literature/Miy22/Yin_U005.md#miy22-u005) supplies scalar elimination for a norm-decaying geometric matrix inverse without adjoint closure.
  [Yin_C_F0008](../claims/Yin_C_F0008_v1.md#yin_c_f0008) is a different elimination input for arbitrary bounded matrix inverses under its adjoint-closure hypothesis.

## Structural Questions and Discriminating Tests

| Branch | Structural input to investigate | Exact missing implication and next test |
| --- | --- | --- |
| Residuals and realizations | Finite Hankel rank, recognizable series, backward shifts, finite-dimensional linear systems and observability/Stein identities | Derive the actual coefficient residual operations from multiplication or free difference quotients in a specified orthogonal basis. Identify a finite realization of the basis transformation. Algebraic rationality in the generators alone does not establish this. |
| Orthogonal polynomial and Fock structure | Wick recursions, finite recurrence data, free Meixner or other tractable polynomial models, and deformed Fock representations | Work out low-degree residual/commutator identities first, then prove a rule for arbitrary word length. A finite list of low-degree identities is only diagnostic evidence. |
| Haagerup and rapid decay | Homogeneous operator-norm bounds with polynomial or subexponential degree growth | Verify the precise alphabet, grading, coefficient norm and holomorphic/full-star scope. Combine only with residual structure in that same expansion. For scalar boundedness a scalar estimate suffices; inverse-matrix reconstruction has additional requirements. |
| Differential regularity | Quantitative conditions involving conjugate variables, free difference quotients, spectral nondegeneracy or coercivity | L2 conjugates alone fail for both targets; even bounded Lipschitz conjugates fail for the L2 target. Identify an additional estimate excluding the beta-law endpoint pole, or investigate bounded scalar reconstruction separately. Then test whether the estimate controls coefficient shifts or full rational inverse states. |
| Transport and free Gibbs models | Quantitative analytic changes of variables, invertible Jacobians and small perturbations of known positive models | Check which graded/residual estimates transfer and whether the map preserves the algebraic rational field. Analytic transport alone need not be a rational coordinate transformation. |

The [search and regularity evidence](../claims/Yin_C_F0016_v1.md#regularity-strategy-evidence) owns inspected primary sources, exact positive results and unresolved applications.
Literature progress on one column does not automatically provide the missing implication in the last column.

## Execution Order and Decision Rules

The user's earlier [explicit Yin_T_F0001 expansion](../tasks/Yin_T_F0001_v1.md#expanded-affiliated-and-boundedness-contract) selected three model routes: [Yin_S_F0008, q-Gaussian](Yin_S_F0008.md#s_f0008), [Yin_S_F0009, holomorphic R-diagonal](Yin_S_F0009.md#s_f0009), and [Yin_S_F0010, analytic free transport](Yin_S_F0010.md#s_f0010).
That selection superseded the earlier suggestion to check a Meixner recurrence first.
The [later historical allocation](../tasks/Yin_T_F0001_v2.md#manuscript-and-other-tasks) assigns Yin_S_F0009/Yin_S_F0010 to a separate R-diagonal and analytic-transport Task and the q-Gaussian targets to a separate q-Gaussian boundedness Task.
The corresponding contracts are [T_F0009](../tasks/Yin_T_F0009_v1.md#contract) for the R-diagonal and transport programme and [T_F0006](../tasks/Yin_T_F0006_v1.md#contract) for the q-Gaussian targets; the associations retain those distinct scopes.
Meixner remains an optional source lead for a named structural interface, not an additional assigned model Task.

The [application map](../ledger/Yin_L_F0007_v1.md#finite-residual-applications) supplies the established semicircular, polynomial-coordinate and supported Haar/Hardy baselines.
Each new route first distinguishes applicability of the affiliated theorem, an L2-to-bounded conclusion, and bounded scalar reconstruction.
The shared question is whether analytic regularity supplies finite-dimensional coefficient dynamics or another quantitatively controlled rational reconstruction.

1. Keep the two targets distinct, and verify a candidate regularity condition against simple spectral singularities before launching a general proof.
   Finite Fisher information alone is excluded for both targets; bounded Lipschitz conjugates alone are excluded for the L2 target.
   Do not repeat these universal routes without a changed hypothesis.
2. Use finite-Hankel/linear-system equivalences to replace the residual hypothesis by a structural statement that can be checked in a concrete model.
   Compare with the existing [JMS21 Gramian interface](../audits/literature/JMS21/Yin_U001.md#jms21-u001) and the audited recognizable-series inputs.
3. Select a candidate model only after both its residual operation and a matching norm estimate have credible exact source or derivation support.
   A known Haagerup estimate by itself is insufficient.
4. For the second target, additionally construct a fully bounded inverse representation or another valid scalar reconstruction.
   Do not infer division-closure membership from a norm limit.
5. Promote a new model theorem only after stating its exact assumptions, recording the complete argument and an independent review.
   A failed stronger condition refutes that proposed implication, not every narrower positive model.

Continue when a source identity or model calculation addresses a named missing implication.
Redirect when a counterexample retains the proposed regularity.
Pause a source branch when repeated searches do not refine the condition; record the unresolved interface and reopen upon a new structural lead.

## Evidence and Changes

2026-09-27, Codex recorded for Yin: transfer coordination of Yin_S_F0009/Yin_S_F0010 to the R-diagonal and analytic-transport Task named in the [historical allocation](../tasks/Yin_T_F0001_v2.md#reorganization-authorization-2026-09-27); disposition active -> active, with mechanisms, mathematical assessments and the separate L2/bounded-reconstruction targets retained.
At that checkpoint, T_F0001 was assigned the polynomial-domain affiliated criterion, and separate q-Gaussian boundedness and free-product reconstruction Tasks were named for their respective model work.
This is ownership maintenance, not new research authorization or a manuscript selection.

The latest [model synthesis](../ledger/Yin_L_F0003_v1.md#boundedness-model-synthesis) integrates Yin_C_F0017-Yin_C_F0020 at their current material decisions.
The positive holomorphic theorem supplies scalar reconstruction as well as boundedness; the R-diagonal inverse excludes an unrestricted affiliated-L2 extension; projective Jacobian control supplies bounded duals but fails to preserve finite rank in general; q-Hermite poles supply a complete scalar baseline.
These results refine the next tests rather than resolving the multivariable q/transport targets.

Subsequent update, 2026-09-09: independently reviewed [Yin_C_F0022](../claims/Yin_C_F0022_v1.md#yin_c_f0022) establishes affiliated finite-defect rationality for selfadjoint finite-Fisher tuples using canonical closed duals.
[Yin_C_F0023](../claims/Yin_C_F0023_v1.md#yin_c_f0023) and the independent Dab10-U002 Lipschitz route give bounded normalized duals for all finite-dimensional q-Gaussian tuples with -1<q<1.
This resolves main-theorem applicability for that entire model interval, not the distinct rational L2 boundedness or bounded scalar reconstruction targets.
Yin_C_F0016's counterexamples to those analytic upgrades remain valid.

- The coordinating agent created Yin_S_F0007 as an active coordinating route under the user's explicit follow-up authorization.
  Preserved Yin_S_F0004's previous model-specific record and all original Yin_T_F0001 completion evidence.
  Yin_C_F0015 and Yin_C_F0016 have separate proof/review assessments in the Claim materials.
  No assertion of a new positive tuple family or literature priority is made.
- Integration verification, 2026-09-09: Yin_C_F0015 and Yin_C_F0016 both passed independent internal mathematical review.

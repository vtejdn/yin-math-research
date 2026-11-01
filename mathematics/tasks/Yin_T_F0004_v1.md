---
author: Yin
---

# Miy26 spectral generalization

## Current decision

[Selected recorded decision](#decision-candidate-0001)

## Yin_T_F0004: Extending Miy26 Spectral Formulas

<a id="contract"></a>
<a id="yin_t_f0004"></a>

Origin and authorization: user-assigned, 2026-09-11; explicitly start autonomous exploration.
Current state: completed at the recorded spectral-generalization scope.
The user seeks a broad family containing the free (semi)circular examples for which Miy26-type spectral formulas hold; the exact resolved formulas and broader questions are separated below.

## Execution boundary

Current local family boundary: `execution/Yin_E_F0004.md`.

## Target and Source Boundaries

Use the [complete Miy26 audit](../audits/literature/Miy26/readme.md) to state exactly which source formula is being generalized before deriving a new result.
In particular distinguish:

1. Theorem 1.1: rational affiliated L2 elements of a finite free semicircular family are bounded.
2. Corollary 1.2 and its scalar resolvent/spectrum criterion, including actual affiliated inverse existence and square integrability.
3. The holomorphic circular polynomial/creation-operator spectrum comparison of Lemma 4.1 and Corollary 4.2, and the more specific coefficient/transfer-matrix formulas derived from it.

The main research target is a rigorous spectral formula on a broad class containing the source's (semi)circular cases.
An extension of L2 rational boundedness may supply the mechanism but is not silently substituted for the spectral conclusion.
State scalar versus matrix coefficients, selfadjoint versus holomorphic polynomials, normalization, affiliation, inverse existence and the spectrum's ambient algebra.
Brown-measure support, spectrum and a finite transfer-matrix radius are different objects until their equivalence is proved.
Retain the source audit's cyclic-subspace qualification for the quadratic transfer matrix.

## Completion and Progress Criteria

Find a precise general theorem and a substantial class for which the exact formula is proved, verify inclusion of the relevant semicircular/circular source cases, and obtain independent review of the proof and source interfaces.
A bare analogy, an existing source special case, or a numerical spectrum plot alone is not completion.
Failed candidate classes should produce explicit counterexamples or clearly located missing steps.

## Related Records

- [Yin_S_F0014: Miy26 spectral generalization](../strategies/Yin_S_F0014.md#s_f0014).
- [Miy26 spectral interfaces](../audits/literature/Miy26/Yin_U003.md#miy26-u003) and [circular resolvents](../audits/literature/Miy26/Yin_U005.md#miy26-u005).
- [Yin_T_F0003](Yin_T_F0003_v1.md#yin_t_f0003), a related but distinct bounded-closure question; [Claim index](../claims/index.md) for existing residual and model results.

## Contract History

- 2026-09-11: registered and started from the user's instruction.
  Source-formula disambiguation is part of this research, without restricting the user's broad-family objective to an easier special case.
- 2026-09-11: completed after independent review of Yin_C_F0093-Yin_C_F0095 and the additional all-positive-rate result Yin_C_F0096.
  The completed deliverables include an actual inverse-L2 spectral criterion with the semicircular/circular baseline and a separate explicit product spectrum formula.
  No unchanged universal creation-model or transfer-matrix formula is claimed.

<a id="reviewed-outcomes-2026-09-11"></a>
## Reviewed Outcomes and Continuation Boundary

[Yin_C_F0096](../claims/Yin_C_F0096_v1.md#yin_c_f0096), with its [independent full review](../audits/reviews/Yin_R_F0110_v1.md#original-f0044-account), extends Miy26's rational-L2 result to every finite free family of free-Poisson variables with arbitrary positive real rates and positive jumps, mixed with semicircular variables.
It proves that every affiliated rational L2 element belongs to the generated C*-algebra.
Consequently, for every rational affiliated f, a complex number lambda is outside its ordinary closed-operator spectrum exactly when f-lambda has an existing affiliated inverse in L2.
Bounded rational images inherit this spectral criterion, including circular families and finite real-jump compound-Poisson constructions.
The proof uses Yan25's exact Wick formula, a polynomial homogeneous norm bound, Yin_C_F0034's finite-defect algebra and Yin_C_F0015's residual decay; it needs neither a normalized bounded dual nor maximal Delta.

[Yin_C_F0095](../claims/Yin_C_F0095_v1.md#yin_c_f0095) independently supplies finite matrix/corner transfer and a rational-rate Poisson realization through rectangular circular matrices.
That transfer result remains useful separately from Yin_C_F0096's larger parameter range.
Its exact corner and division-ring hypotheses must be checked before reuse.

The distinct holomorphic comparison branch gives [Yin_C_F0093](../claims/Yin_C_F0093_v1.md#yin_c_f0093), spectrum inclusion and equality of polynomial hulls for normalized iid R-diagonal coordinates, and [Yin_C_F0094-P2](../claims/Yin_C_F0094_v1.md#yin_c_f0094), an explicit product spectrum and Brown-support set when the steps have no L2 inverse.
Yin_C_F0094's source-support gap and complete positive-density repair remain visible in its proof history and independent audit.
The [KPZ26 application](../audits/literature/KPZ26/Yin_U001.md#kpz26-selected-audit) supplies a separate established homogeneous freely infinitely divisible R-diagonal disk formula; it is not presented as a new project result.

The [contract comparison](../audits/reviews/Yin_R_F0096_v1.md#yin_t_f0004-a-spectral-formula-with-the-relevant-source-cases-included) checks the actual spectral conclusion and inclusion of the semicircular/circular baselines.
These results do not establish arbitrary mixed-degree R-diagonal creation-spectrum equality, general q-Gaussian rational-L2 boundedness, or the bounded scalar division-closure equality of Yin_T_F0003.
[Yin_S_F0014](../strategies/Yin_S_F0014.md#s_f0014) retains these distinctions and the next discriminating questions.


## Lifecycle and completion


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | completed |
| authority | Initial recorded disposition in Yin_T_F0004_v1; original assignment and criteria remain in mathematics/tasks/Yin_T_F0004_v1.md#yin_t_f0004 |
| reason | Preserve the completed disposition already recorded at registration; this timestamp is registration, not an inferred historical completion date. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Exact material](#contract) | Exact original contract and success conditions retained in this material. |
| review | [Exact material](../audits/reviews/Yin_R_F0096_v1.md#final-additional-pass) | The original completion criteria and limitations in the cited completion comparison for Yin_T_F0004. Preserve recorded lifecycle and completion evidence; historical review classification is not inferred. |

Retained historical evidence boundaries:

- Original completion/review artifact retained as context: [Exact material](#reviewed-outcomes-2026-09-11).
  Recorded scope: The original completion criteria and limitations in the cited completion comparison for Yin_T_F0004.
  Preserve recorded lifecycle and completion evidence; historical review classification is not inferred.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

The original completion criteria and limitations in the cited completion comparison for Yin_T_F0004.
Preserve recorded lifecycle and completion evidence; historical review classification is not inferred.

Completion contract: [Exact material](#contract).

Review: [Exact material](#reviewed-outcomes-2026-09-11); [Exact material](../audits/reviews/Yin_R_F0096_v1.md#final-additional-pass).

Material covered by that review: [Exact material](Yin_T_F0004_v1.md).

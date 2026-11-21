---
author: Yin
---

# General Bounded-Closure Conditions

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_F0003_v2](../tasks/Yin_T_F0003_v2.md#contract) | General sufficient conditions for bounded rational closure equality, with the retained scalar question and selfadjoint bounded-dual counterexample tests. |

## Route

| Field | Value |
| --- | --- |
| disposition | active |
| priority | Test proposed sufficient hypotheses against simpler selfadjoint bounded-dual examples. |

The Route section owns the current allocation.
Dated outcomes, earlier authorizations and superseded allocations below retain their recorded scope.

<a id="s_f0013"></a>
Goal: [Yin_T_F0003](../tasks/Yin_T_F0003_v2.md#contract).
The completed first sufficient-condition round is retained below.
The current user-directed continuation incorporates the search for a simpler counterexample with selfadjoint generators and whole-space bounded duals.
The current results and remaining tests below keep rational membership, boundedness and exclusion from every bounded matrix expression as separate obligations.

First examine invariance under rational coordinate changes and reductions to verified families, then residual/realization criteria that are independently checkable.
Compare each proposed analytic condition against Yin_C_F0012/Yin_C_F0016 and distinguish complete bounded rational closure from the scalar division closure.
A condition furnishing bounded inverse realizations is sufficient only after its hypothesis is established for all relevant elements; bounded output is not that hypothesis.

The main sufficient-condition discriminator remains a precise stability theorem with a nontrivial application, or a common residual estimate verified on a family.
Existing model routes retain their own obligations.

## Selfadjoint counterexample tests

[C_F0012 v3](../claims/Yin_C_F0012_v3.md#statement), with its [independent whole-proof and comparison review](../audits/reviews/Yin_R_F0056_v3.md#quadratic-selfadjoint-finding), gives the tuple \((h,\operatorname{Re}(hz),\operatorname{Im}(hz))\), where \(z\) is circular and free from \(h\).
It has bounded duals and a positive witness \(u^*(h^2)^{-1}u\) outside the generated C*-algebra, hence outside every bounded matrix rational closure.
The maximum degree drops from three to two and the dual needs only a weighted right annihilation operator, but the generator count increases from two to three.
Thus selfadjointness, bounded duals and quadratic dependence on elementary free inputs still do not suffice for the equality.
The two-generator simplification remains open, and this example does not complete the general sufficient-condition Task.

[C_F0369](../claims/Yin_C_F0369_v1.md#statement), with its disclosed [developer self-review](../audits/reviews/Yin_R_F0378_v1.md#quadratic-finding), resolves several direct two-generator tests at their exact scopes.
The anticommutator pair \((h,hb+bh)\) has bounded duals and generates the full original C*-algebra, but \(b\) is not affiliated rational in that pair; no original polynomial witness of b-degree at most one can give a counterexample.
The commutator pair \((h,\mathrm i[h,b])\) has no bounded dual system, and the original small-spectral-vector mechanism fails for every genuinely b-dependent selfadjoint quadratic in the stated class.
These facts do not rule out all two-generator quadratic examples.

Next concrete test: verify or refute the [higher-degree polynomial intersection candidate](../drafts/Yin_D_F0046.md) for the anticommutator pair, including the exact graded commutator block and finite-rank remainder compression.
Even a positive result there would concern polynomial witnesses and would not by itself settle the full bounded rational-closure equality.
Do not reuse b as a candidate witness for that pair without changing the already excluded premise.

## 2026-09-11 Outcome and Handoff

The initial discriminator above is resolved by [Yin_C_F0089](../claims/Yin_C_F0089_v1.md#yin_c_f0089), with independently reviewed finite-index transfer and virtually free applications.
[Yin_C_F0087](../claims/Yin_C_F0087_v1.md#yin_c_f0087) and [Yin_C_F0090](../claims/Yin_C_F0090_v1.md#yin_c_f0090) supply separate commutative mechanisms.
The [goal outcome](../tasks/Yin_T_F0003_v1.md#reviewed-outcomes-2026-09-11) links all proofs and the cusp/dimension-two obstructions.

Further work should test closure under free products with diffuse marginals, or find a bounded scalar reconstruction mechanism for nonuniform finite atomic laws.
The finite-index theorem alone cannot answer either question.
The q-Gaussian and analytic-transport obligations now have their separate [T_F0006](../tasks/Yin_T_F0006_v1.md#contract) and [T_F0009](../tasks/Yin_T_F0009_v1.md#contract) homes; the separate rational-L2 boundedness result must not be substituted for the scalar closure equality.

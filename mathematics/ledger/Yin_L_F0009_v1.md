---
author: Yin
---

# Intermediate Domains for the Affiliated Rationality Criterion

Date: 2026-09-10.
This synthesis answers the user's request to reduce the dual-domain requirements without making polynomial-only domains the objective.
It compares the exact linked theorems; their claim and review records own mathematical status.
The earlier Yin_C_F0024, Yin_C_F0025-Yin_C_F0028, and the original bounded-intersection counterexample are preserved.

## The General Left-Module Form

[Yin_C_F0029](../claims/Yin_C_F0029_v1.md#yin_c_f0029) uses any Hilbert-dense left M-submodule E of H as the common dual domain.
For each adjoint it suffices to have another Hilbert-dense left M-submodule V_i in its domain.
Impose the usual generator identities on E and take closures of these restrictions.
No right-generator invariance, Banach-space completeness, polynomial-core inclusion, vacuum membership, or uniform estimate on all M is assumed.
The spaces E and V_i may contain unbounded L2 vectors.

A particularly concrete certificate is E=Mh for a bounded regular h in M, and V_i=E when this space lies in each adjoint domain.
No bounded inverse for h or boundedness of h X_j h^{-1} is required.
Left multiplication by every bounded numerator and denominator preserves the domain automatically.
The common core is specified rather than inferred for an arbitrary larger closed extension.

For every affiliated u and every pair of bounded fractions u=s^{-1}a=bt^{-1}, all compositions in sD_i b-aD_i t are defined on E.
The full finite-rank equivalence, bounded Hilbert extensions, independence of the fractions and full closed-domain bounded-f criterion are retained.
The proof works for jointly dependent multivariable elements; it does not assume bounded intermediate inverse matrices or reduce to one coordinate.

## What Makes the Proof Work

The mechanism needed for arbitrary bounded fractions is left-module invariance of the test domain, not membership of every bounded vector in it.
Dense left-module adjoint tests make every cleared defect closable.
If such a defect is finite rank after multiplying by regular denominators, its restriction to the dense denominator range is closable and finite rank, hence extends to a bounded finite-rank operator on all H.
That graph is contained in the closure of the full defect, so the closure must be the same everywhere-defined operator.
This proves cancellation without a uniform estimate on all bounded vectors.

Finite trace and left-module density supply projections e_n in E with traces tending to 1.
After removing the left supports of X_i(1-e_n), one obtains projections p_n of trace tending to 1 with Mp_n and every (Mp_n)X_i contained in Me_n.
Closed graph gives an operator-norm-to-L2 bound on each Me_n separately.
Consequently the normality/Liouville argument and its Kaplansky extension work on each local space Mp_n, where every required composition is defined.
The finite-rank defects are already bounded Hilbert operators, so the resulting tensor identity extends from these dense local test spaces to H.
Thus no global right-generator invariance or global infinity-to-L2 estimate is necessary.

## Domain and Vacuum Comparison

| Result | Dual input domain | Adjoint tests required | Vacuum convention | Actual scope |
| --- | --- | --- | --- | --- |
| [Yin_C_F0024](../claims/Yin_C_F0024_v1.md#yin_c_f0024) | M | all M | vacuum belongs to both domains | Full affiliated criterion |
| [Yin_C_F0030](../claims/Yin_C_F0030_v1.md#yin_c_f0030) | M | any dense left M-submodule | vacuum belongs to the dual domain; no adjoint-vacuum hypothesis | Same full criterion; removal of an explicit premise, without a proved strict-separation example |
| [Yin_C_F0029](../claims/Yin_C_F0029_v1.md#yin_c_f0029) | any Hilbert-dense left M-submodule E of H; Mh is a concrete option | dense left M-submodules, possibly different for each adjoint | vacuum membership is not required | Same full criterion on the specified core and its closure; a strict multivariable example is supplied |
| [Yin_C_F0028](../claims/Yin_C_F0028_v1.md#yin_c_f0028) | starred polynomial core | vacuum adjoint plus bounded starred commutators | vacuum belongs to both core/adjoint domains | Complete one-coordinate criterion only |

A left M-submodule that fails to contain all bounded vectors cannot contain the vacuum: if it contained 1, left invariance would make it contain M.
Thus Yin_C_F0029 is a change in the geometry of the allowed core, not an intermediate unital algebra containing the polynomial algebra.
One may use Yin_C_F0030 when retaining the original all-M dual input and its vacuum is preferable.
An additional demand for a normalized vacuum-containing core strictly between the polynomial algebra and M remains a separate question.

The free-Haar example in Yin_C_F0029 verifies a strict reduction for a generally noncommuting tuple: a bounded dual is perturbed by right multiplication by an affiliated positive eta at least 1 and outside L2.
Taking h=(1+eta^2)^{-1/2} gives Mh as a graph core for the resulting duals and a subset of their adjoint domains.
The vacuum lies outside both actual domains.
The right-multiplier perturbation cancels in every cleared defect, so the strict example verifies the domain distinction; it does not assert a previously unknown rationality classification of free Haar variables.

## Why a C*-Algebra Substitution Is Insufficient

Suppose a closed dual and its adjoint both have domains containing C*(X).
Closed graph on this Banach algebra gives operator-norm-to-L2 estimates for both maps there.
Kaplansky approximation to any bounded element of M supplies uniformly bounded approximants in C*(X).
Weakly convergent subnets of their images and weak closedness of the two Hilbert graphs place every bounded element in both domains.
Thus this substitution recovers the all-M domain condition after closure and is not a genuine reduction.
This is the same analytic mechanism proved in [Yin_C_F0027](../claims/Yin_C_F0027_v1.md#yin_c_f0027), with its complete C*-algebra domain replacing the two separately assumed core estimates.

The selected Yin_S_F0011 task is therefore the intermediate-domain result above.
The bare polynomial-core converse and the stronger bounded realization assertion keep their previous assessments; neither is a prerequisite for using Yin_C_F0029 or Yin_C_F0030.

## Formal comparison finding

The original complete comparison review is retained at [R_F0018](../audits/reviews/Yin_R_F0018_v1.md#separate-comparison-note-review), with its disclosed unknown initial-context relationship and original 2026-09-10 scope.
This current locator neither changes the dated mathematical synthesis nor certifies a new independent review.

---
author: Yin
---

# An Independent Signed Schur Minimum for Affine Circular Pencils

The current complete independent circular signed-Schur proof is owned by [C_F0167](../claims/Yin_C_F0167_v1.md#argument).
The [original R_F0123 finding](../audits/reviews/Yin_R_F0123_v1.md#3-circular-physical-inverse-and-determinant-normalization) inspected that complete argument; the original preliminary-collaboration and source boundaries remain below.

Record kind: project deduction and strategy exploration.
Date: 2026-09-13.
Author: yin_t_f0008-contract agent.
Goal: [Yin_T_F0008](../tasks/Yin_T_F0008_v1.md#yin_t_f0008); route: [Yin_S_F0022](../strategies/Yin_S_F0022.md#s_f0022).
No Claim ID or mathematical Role is assigned here.
The coordinating agent owns registration and the current assessment.

The user requested continued independent exploration of a general variational formula, with Yin_C_F0121's matrix-inequality mechanism as a priority.
The [formula](../claims/Yin_C_F0167_v1.md#statement) was developed from the signed Schur action.
It does not use Spe26 or Yin_C_F0124 in its derivation or proof.
It currently covers arbitrary affine matrix-valued circular noise; the general nonzero pseudo-covariance extension is an explicitly separate obligation.

## Local and external inputs

The local inputs are the [signed Schur factorization](Yin_L_F0033_v1.md#signed-schur-linearization), the [Yin_C_F0119 Dyson primitive](../claims/Yin_C_F0119_v1.md#yin_c_f0119), and the [Yin_C_F0121 positive-supersolution action](../claims/Yin_C_F0121_v1.md#minimum-over-all-matrix-supersolutions).
The primitive is used at an actual inverse expectation, not assumed to be a global extremum.

The global comparison uses Hansen and Pedersen, *Jensen's Operator Inequality*, Theorem 2.1(ii), checked in the [primary author preprint](https://arxiv.org/pdf/math/0204049), printed/PDF p. 3.
It applies an operator-convex function to a unital matrix column.
We use the function \(h(t)=t-\log t-1\) on \((0,\infty)\).
Its operator convexity follows from that of the inverse and the integral representation of \(-\log\).
The interval and unital-column version matter: the contractive variant with an additional value at zero is not the statement being invoked.
The source statement and its applicability were checked; a full audit of that paper is not claimed.

A scoped search also found Hachem, Loubaton and Najim, *Deterministic equivalents for certain functionals of large random matrices*, [primary preprint](https://arxiv.org/pdf/math/0507172), Theorem 4.1 and equation (4.3), printed/PDF p. 18.
It gives a related logarithmic determinant expression evaluated at deterministic-equivalent equations for variance-profile random matrices; Appendix C derives that expression by differentiation.
This is a useful related mechanism, not a cited global minimum theorem for the [matrix formula](../claims/Yin_C_F0167_v1.md#statement).
No novelty claim is made.

## Remaining general extension and numerical exploration

For an arbitrary complex semicircular pencil, the additional map \(\rho(X)=\sum_ja_jXa_j\) need not vanish.
Its covariance contributes an additional term in the off-diagonal Schur variable.
The present proof does not discard that term or identify the resulting law with a circular one.
Extending the Jensen and positive left-right comparison to that coupled quadratic form is a concrete continuation of Yin_S_F0022.
General indefinite selfadjoint pencils likewise remain outside the independent formula proved here.

Before the comparison proof was found, a floating-point search used NumPy seed 84903, 36 size-two circular coefficient families, one to three Kraus matrices, regularizations in \(\{0.1,0.3,1\}\), and six positive-matrix gradient starts per family.
No objective value below the physical value was found; the largest downward discrepancy was about \(1.8\times10^{-15}\).
The search is motivation only.
The proof rests on the [physical identities and global comparison](../claims/Yin_C_F0167_v1.md#argument), not on numerical minimization or Yin_C_F0124 benchmark values.

An independent agent checked the algebra in the exact [difference and global comparison](../claims/Yin_C_F0167_v1.md#global-comparison-by-operator-jensen-and-a-positive-left-right-operator), including the weighted Jensen step and the commuting positive left/right multiplication operators.
That preliminary collaboration does not certify the full module or replace a complete proof audit of the physical identities and determinant normalization.

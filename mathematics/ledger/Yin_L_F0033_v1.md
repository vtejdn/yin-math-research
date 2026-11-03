---
author: Yin
---

# Affine Variational Formulas: Independent General Formula and Spectrum

Record kind: synthesis and justified route development for [Yin_T_F0008](../tasks/Yin_T_F0008_v1.md#yin_t_f0008).
Updated: 2026-09-13.
Author: root.
The initial offline exploration is retained below as dated history.
The current continuation permits local and external literature search and has no usage-based stop.
This record does not create a separate source of Claim assessments or declare the goal complete.

## General Formula Obtained by the Independent Exploration

The user requested parallel exploration after Yin_C_F0124 and declined to adopt the externally found formula as the final version.
[Yin_C_F0126](../claims/Yin_C_F0126_v1.md#yin_c_f0126) supplies a different general formula with a proof independent of Spe26 and Yin_C_F0124.
Its complete review (original material now separated into [Yin_R_F0128_v1](../audits/reviews/Yin_R_F0128_v1.md), [R_F0174 determinant-presentation finding](../audits/reviews/Yin_R_F0174_v1.md#determinant-presentation-finding)) checks all complex coefficient matrices, the global extremum and physical branch, removal of regularization, singular cases and the full MS24 reduction.
No manuscript formula or mathematical Role is selected by this record.

For free standard semicircular variables and arbitrary complex matrices of size m, write
\[
 S=a_0+\sum_j a_j\otimes s_j,\qquad
 \eta(X)=\sum_j a_jXa_j^*,\qquad \rho(X)=\sum_j a_jXa_j.
\]
For every freely chosen \(R>0\), define \(H_R=I+\eta(R)\) and let \(Z_R\) be the unique solution of the real-linear equation
\[
 H_RZ_RR^{-1}+\rho(Z_R^*)=a_0.
\]
With the normalized trace \(\varphi=\operatorname{tr}_m\otimes\tau\), Yin_C_F0126 gives
\[
 \Delta_\varphi(S)=e^{-1/2}\inf_{R>0}
 \left[\frac{\det(I+\eta(R))}{\det R}\right]^{1/(2m)}
 \exp\!\left[\frac1{2m}\operatorname{Re}\operatorname{Tr}(a_0^*Z_R)\right].
\]
The only outer constraint is ordinary positive definiteness.
The inner equation is positive definite on the real Hilbert space of complex matrices for every trial; its inverse is not an assumed feasibility condition.
Its equivalent quadratic maximum is taken first.
The formula has no remaining regularization parameter and permits a determinant value of zero.
The logarithmic form is retained in the proof.

At \(a_0=0\), the inner solution vanishes for every trial, and
\[
 \inf_{R>0}\frac{\det(I+\eta(R))}{\det R}
 =\operatorname{cap}(\eta),\qquad
 \Delta_\varphi(S)=e^{-1/2}\operatorname{cap}(\eta)^{1/(2m)}.
\]
The first equality follows from determinant monotonicity and the scaling \(R=tB\), \(t\to\infty\), for each fixed \(B>0\).
It includes singular covariance outputs and zero capacity.
Thus MS24 is recovered at the level of the full variational formula, without choosing a Dyson stationary point or using the MS24 determinant equality in the proof.

[Yin_C_F0127](../claims/Yin_C_F0127_v1.md#yin_c_f0127), with its [original attainment finding](../audits/reviews/Yin_R_F0180_v1.md#historical-affine-attainment), proves that the infimum is attained exactly when S is boundedly invertible.
The unique minimizer and its inner solution are
\[
 R_*=E((S^*S)^{-1}),\qquad Z_{R_*}=E((S^*)^{-1}).
\]
For \(T=\sum_j a_j\otimes s_j\), set \(a_0=-zI\): nonattainment detects precisely \(z\in\sigma(T)\).
The canonical regularized minimizing matrices diverge there, by the separately reused rational-L2 input Yin_C_F0095.
This concerns the entire operator spectrum.
Brown potentials and their justified measure limits remain the separate Yin_C_F0123 interface; equality of Brown support and operator spectrum is not asserted.

## Comparison of Formulas and Proof Inputs

| Record | Scope and trial variables | Actual derivation and relation to other formulas |
| --- | --- | --- |
| [Yin_C_F0121](../claims/Yin_C_F0121_v1.md#yin_c_f0121) | Strictly positive selfadjoint pencil; matrix supersolutions | Existing positive-pencil least-supersolution proof. Its optimizer is \(q=E(S^{-1})\), whereas Yin_C_F0126 uses \(R_*=E(S^{-2})\); their relation is \(R_*=q^2+q\eta(R_*)q\), not an identification of the variables. |
| [Yin_C_F0124](../claims/Yin_C_F0124_v1.md#yin_c_f0124) | All selfadjoint pencils and all complex pencils by hermitization; strict Hilbert--Schmidt domain | Candidate explicitly attributed to [Spe26](../audits/literature/Spe26/Yin_U001.md); the source supplied no proof and its nonstrict inverse domain required repair. The project supplied and reviewed the global comparison and full MS24 reduction. Retained benchmark. |
| [Positive-certificate reformulation](../claims/Yin_C_F0164_v1.md#statement) | All-positive trial parametrization of Yin_C_F0124 | Proved bijection with the benchmark domain; simplifies feasibility and the centered scaling. It depends on Yin_C_F0124 and is not a second independent proof. |
| [Yin_C_F0125](../claims/Yin_C_F0125_v1.md#yin_c_f0125) | Arbitrary selfadjoint drift; covariance strictly positive as a Hilbert--Schmidt operator; ordered Hermitian/positive minimax | Independent auxiliary Dyson equation and reduced-Hessian proof. An exact counterexample prevents dropping the covariance hypothesis for that formula. |
| [Circular Schur formula](../claims/Yin_C_F0167_v1.md#statement) | Circular pencils; free positive trial and inner complex maximum | Independent Jensen comparison using the scoped [HP03 input](../audits/literature/HP03/Yin_U001.md). Retained restricted alternative; not the proof of general Yin_C_F0126. |
| [Yin_C_F0126](../claims/Yin_C_F0126_v1.md#yin_c_f0126) | Every complex affine pencil; original-size positive trial and unique complex inner maximum | Coercivity plus a positive Stein equation shows every critical point is physical; Yin_C_F0119 supplies Dyson uniqueness and the determinant primitive. Homogeneous rescaling removes regularization. Does not use Yin_C_F0124, HP03 or the MS24 centered determinant conclusion. |
| [Yin_C_F0127](../claims/Yin_C_F0127_v1.md#yin_c_f0127) | Exact attainment, unique optimizer and full-spectrum criterion for Yin_C_F0126 | A stationary point supplies a strict positive certificate on the full hermitized space; analytic branch selection and the Yin_C_F0123 gap interface give actual bounded invertibility. Yin_C_F0095 is an existing input only for the L2/canonical-divergence restatement. |

The signed Schur action in Yin_C_F0126 resolves the structured indefinite extremum left open below.
It connects the selfadjoint target to all complex coefficients in one proof, while Yin_C_F0125 retains a smaller selfadjoint minimax under an additional hypothesis.
The [direct-capacity exploration](Yin_L_F0028_v1.md) preserves its source/search and candidate boundaries; the complete [paired formulation](../claims/Yin_C_F0165_v1.md#argument) and [scalar elliptic argument with exact obstructions](../claims/Yin_C_F0166_v1.md#argument) now have their own C homes.
The retained unsuccessful variants supply no additional general theorem.
The [negative-direction exploration](Yin_L_F0030_v1.md) retains the unresolved signed candidate; its complete [circular-potential identification and local-saddle obstruction](../claims/Yin_C_F0168_v1.md#argument) keep the exact distinction between failure of that mechanism and failure of the goal.

## Mathematical Operation and Completion Evidence, 2026-09-13

The parallel exploration produced Yin_C_F0125, the independent general proof Yin_C_F0126 and the attainment interface Yin_C_F0127.
Each registered conclusion has its own scoped review at the finding's actual relationship.
The original [C_F0125 review](../audits/reviews/Yin_R_F0125_v1.md#positive-covariance-minimax-finding) and [C_F0126 review](../audits/reviews/Yin_R_F0128_v1.md#general-signed-schur-finding) are self-reviewed; their real 2026-09-13 acts and mathematical scopes remain unchanged.
Those findings and the [completion/interface comparison](../audits/reviews/Yin_R_F0126_v1.md#contract-and-review-relationship) do not supply the subsequent independent complete-Task logical-chain inspection, whose [follow-up scope](../tasks/Yin_T_F0008_v1.md#pending-independent-complete-chain-inspection) is retained at the Task.
This synthesis records their relationship, preserves the earlier full proofs and attempts, and distinguishes proposal provenance from logical dependence.
No existing proof is replaced, lemma extracted, or theorem Role assigned.
The [independent contract comparison](../audits/reviews/Yin_R_F0126_v1.md) checks the original three milestones, Yin_C_F0121 generalization and the user's added independent-exploration direction.
Goal completion belongs to [Yin_T_F0008](../tasks/Yin_T_F0008_v1.md#completion-and-evidence).
Route dispositions belong to the responsible S materials; the [strategy index](../strategies/index.md#yin_t_f0008) supplies navigation.

An unrestricted version of the unsuccessful U/V minimax, convergence rates, efficient certified optimization, Brown-support equality and literature priority remain separate possible questions.
They are not claimed consequences of the present results.
Local source inspection and selected external searches are recorded in the [source-search record](Yin_L_F0029_v1.md); no novelty claim is made.

## Historical Frontier, 2026-09-12

The following sections describe the initial offline checkpoint before Yin_C_F0124.
Their open-problem descriptions and route priorities are historical; current dispositions belong to the [positive-cone](../strategies/Yin_S_F0020.md#route), [ordered-minimax](../strategies/Yin_S_F0021.md#route) and [signed-Schur](../strategies/Yin_S_F0022.md#route) strategies.

## Established Mechanisms to Combine

| Regime | Exact responsible record | What the mechanism provides |
| --- | --- | --- |
| Centered selfadjoint noise plus a positive definite imaginary matrix drift | [Positive-cone formula](../claims/Yin_C_F0120_v1.md) | An attained minimum over every positive definite trial matrix; convexity on explicit exponential paths; exact recovery of ordinary capacity at zero drift |
| Strictly positive or strictly negative selfadjoint affine pencil | [Real-gap formula and refinements](../claims/Yin_C_F0121_v1.md) | A physical inverse expectation selected by positive supersolutions; finite matrix certificates and a true matrix minimum |
| Scalar and commuting coefficients; isotropic covariance with arbitrary selfadjoint drift | [Ordered minimax](../claims/Yin_C_F0122_v1.md) | The imaginary variable is maximized first, leaving a strictly convex scalar objective; the isotropic case includes noncommuting noise coefficients and complete spectral density |
| Arbitrary complex matrix coefficients with scalar spectral shift | [Spectral potential](../claims/Yin_C_F0123_v1.md) | A finite Dyson equation plus one invertible finite linear system for the positive regularized Brown density; a source-justified weak limit |

These results move beyond Yin_C_F0119's infimum along a prescribed one-parameter family.
They do not yet supply one global capacity-type objective for every affine complex coefficient family.
The exact assumptions and review evidence remain in the responsible proofs and registry.

<a id="signed-schur-linearization"></a>
## A Signed Schur Linearization of Every Regularized Determinant

There is a direct algebraic reduction that motivates a further route.
For any bounded S in M_m(M) and epsilon>0, set
\[
 L_\varepsilon=
 \begin{pmatrix}\varepsilon^2I_m&S\\S^*&-I_m\end{pmatrix},
 \qquad Q_\varepsilon=SS^*+\varepsilon^2I_m>0.
\]
The Schur factorization is
\[
 L_\varepsilon=
 \begin{pmatrix}I_m&-S\\0&I_m\end{pmatrix}
 \begin{pmatrix}Q_\varepsilon&0\\0&-I_m\end{pmatrix}
 \begin{pmatrix}I_m&0\\-S^*&I_m\end{pmatrix}.
                                                               \tag{1}
\]
The triangular outer factors have Fuglede-Kadison determinant one: along their affine paths from the identity, the logarithmic derivative is the trace of an off-diagonal square-zero matrix and vanishes.
Applying the same bounded invertible determinant multiplicativity as in the [local foundations](Yin_L_F0036_v1.md), and keeping the trace normalized on size 2m, gives
\[
 \Delta_{\operatorname{tr}_{2m}\otimes\tau}(L_\varepsilon)
 =\exp\!\left(\frac12\varphi_m\log Q_\varepsilon\right)
 =\Delta_\varepsilon(S).
                                                               \tag{2}
\]
All factors are invertible at positive epsilon.
Equality of the singular-value distributions of SS* and S*S identifies the last expression with Yin_C_F0119's regularization convention.

If S=a_0+sum a_j s_j, then L_epsilon is itself a selfadjoint affine semicircular pencil, with constant block matrix [[epsilon squared I,a_0],[a_0*,-I]] and noise blocks [[0,a_j],[a_j*,0]].
Equation (1) presents it with one positive and one negative Schur block.
This is a direct use of the usual Schur-complement factorization, not a newly designated project theorem.

The reduction preserves the unresolved issue: the pencil L_epsilon is indefinite, so the positive-pencil minimum cannot be applied to it.
A valid variational principle for this structured indefinite class would give every positive-epsilon regularized determinant in the general problem; taking epsilon down to zero would then recover the requested determinant.
It remains necessary to prove the appropriate ordered minimum/maximum, feasible domains and physical-branch comparison for that class.

## Priority of the Next Tests

The [positive-cone action route](../strategies/Yin_S_F0020.md#s_f0020) supplies a proven inner minimization mechanism.
The [ordered-minimax route](../strategies/Yin_S_F0021.md#s_f0021) supplies a way for an imaginary variable to select a convex real-part objective.
The [signed-Schur route](../strategies/Yin_S_F0022.md#s_f0022) makes explicit how a successful indefinite extension would cover arbitrary complex coefficients.

Before any generalization is accepted, it must reproduce the centered capacity value, the scalar real spectral-edge transition and the scalar elliptic potential, including the degeneration to a measure on a line.
A stationary Dyson action, a positive-map assumption substituted for Hilbert-Schmidt positivity, or a Brown-support calculation substituted for a full spectral-gap argument does not settle these tests.

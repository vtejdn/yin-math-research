---
author: Yin
---

# Variational and capacity formulas for a single-Haar determinant and its coefficient dependence

## Contract

### Original question and authority

On 2026-10-11 Yin explicitly requested a new F-series Task to find variational and capacity formulas for the determinant of an operator in one Haar unitary variable, and to study the determinant's dependence on its coefficients.
The preceding discussion identified the classical scalar object as p(U), with all powers belonging to the same commutative algebra W*(U).
This is a separately assigned analytical Task, not a reopening of the completed [F0008 semicircular Task](Yin_T_F0008_v1.md#contract) or a resumption of the separate Lehmer-gap investigation discussed at assignment.

### Objects and determinant conventions

Let (M,tau) be a finite von Neumann algebra with faithful normal tracial state and U a Haar unitary:
\[
\tau(U^n)=0\quad(n\in\mathbb Z\setminus\{0\}),\qquad U^*U=UU^*=1.
\]
No free-independence hypothesis is imposed on the powers of U.
Fix a finite integer exponent interval I={l,...,u}.
The scalar coefficient space is C^I, with
\[
p_a(z)=\sum_{j\in I}a_jz^j,\qquad
D(a)=\Delta_\tau(p_a(U)),\qquad L(a)=\log D(a).
\]
Coefficients may be arbitrary complex numbers, including zero coefficients and changing effective degree.
The zero polynomial has D=0 and L=-infinity.
For nonzero p, use Haar probability mu on T and natural logarithms:
\[
L(a)=\int_{\mathbb T}\log|p_a(z)|\,d\mu(z).
\]
Nonzero polynomials with unit-circle zeros remain in scope.

The finite-matrix extension, within the same single-variable framework, is
\[
P_A(z)=\sum_{j\in I}A_jz^j,\qquad A_j\in M_r(\mathbb C),\quad r\ge1,
\]
with ordinary FK determinant under phi_r=tr_r tensor tau.
Thus
\[
L_r(A)=\log\Delta_{\phi_r}(P_A(U))
=\frac1r\int_{\mathbb T}\log|\det P_A(z)|\,d\mu(z)
\]
when det P_A is not identically zero, and L_r=-infinity otherwise.
This is the ordinary determinant including zero spectral mass; the kernel-removed determinant is a distinct quantity.
For comparison with integer group-ring conventions, the unnormalized logarithmic determinant is r L_r(A).
No dimension-normalized quantity may silently replace that total value.

### Assigned research objectives

1. **Variational formulas.**
   Derive and compare exact infimum, minimum or correctly ordered saddle representations for D and L, with explicit freely variable weights, positive matrices or structured operators and admissible domains.
   State whether a formula is finite-dimensional, genuinely infinite-dimensional, or a controlled limit of finite problems.
   Prioritize descriptions built directly from coefficient data; identify what additional simplification is achieved beyond the original circle integral and scalar pointwise log identity.
   Prove both inequality directions, attainment or nonattainment, and the correct limiting convention at circle zeros and the zero polynomial.
   Investigate the matrix extension with the same explicit scope.
2. **Capacity formulas.**
   Find a coefficient-defined positive-map, Toeplitz/convolution or other explicit capacity functional whose relation to D is rigorously established.
   Specify variables, normalization, coefficient construction, homogeneity and exact determinant exponent, and test degeneration and zero capacity.
   A definition that merely renames the unknown determinant or Mahler integral as capacity is not a formula resolving this objective.
   Do not assume that F0008's semicircular covariance map controls a Haar polynomial.
   If a natural proposed capacity class fails, retain a precise obstruction for that class and continue toward an appropriate alternative; a restricted failure does not exclude every possible capacity description.
3. **Dependence on coefficients.**
   For each fixed finite exponent interval, determine the valid continuity and regularity statements for D and extended-real L.
   Derive directional/parameter derivatives and, where justified, second variations or convexity/concavity and potential-theoretic properties.
   Treat zero crossings on T, repeated roots, effective-degree changes and the zero-polynomial boundary explicitly.
   Establish the corresponding matrix-coefficient statements on their actual valid domains, including the identically singular determinant locus.
   Distinguish holomorphic coefficient dependence from real differentiability of a real-valued determinant.
   Clearly separate fixed-support results from estimates uniform in degree or matrix size.
4. **Interaction of the formulas.**
   Explain how optimizers, regularized inverse-square expectations and capacity degenerations reflect coefficient perturbations.
   Give exact checks on representative scalar and matrix examples and identify any losses in finite approximations or linearizations.
   Numerical evidence may guide a conjecture but does not replace an exact formula or a proof of coefficient regularity.

The scalar objectives are the core deliverables.
Finite-matrix coefficients are an explicit extension target, not a replacement for the scalar problem.
Any completed scalar result and still-open matrix generalization must be reported separately; full Task completion requires accounting for both at their recorded scope.

### Starting inputs and reuse boundaries

- [Single-Haar scalar identification and trace convention](../audits/literature/Luc22/Yin_U001.md#luc22-kernel-removed-determinant), and [abelian matrix reduction](../audits/literature/Luc22/Yin_U002.md#luc22-abelian-matrix-approximation).
- [F0008 general affine semicircular formula](../claims/Yin_C_F0126_v1.md#statement), [attainment criterion](../claims/Yin_C_F0127_v1.md#yin_c_f0127), and [regularized proof](../claims/Yin_C_F0126_v1.md#regularized-minimum-used-in-the-proof).
  These supply methods and comparisons at their actual distributional hypotheses; they do not assert a Haar formula.
- [Earlier single-Haar formulation](../ledger/Yin_L_G0002_v1.md#single-haar-formulation), including [regularization and estimate direction](../ledger/Yin_L_G0002_v1.md#regularization-and-direction).
  This rolling G draft records self-checked elementary baselines and no independent review; it is not adopted as a new fixed theorem by this Task.
- [L4 finite-section and Gram analysis](../ledger/Yin_L_G0001_v1.md#degree-window-tests), with the [Den09 finite-section source interface](../audits/literature/Den09/Yin_U002.md#finite-section-determinant).
  Reuse their exact approximation direction and input-dependent costs.

Perform a bounded local and primary-source reuse check before claiming a new formula or coefficient theorem.
Existing Jensen/root expressions, circle integrals, scalar log variation and fixed-input Toeplitz limits are baselines to be used and attributed, not presumed novel results.
No source intake, proof re-audit or novelty claim is created by this registration.

### Completion criteria and partial progress

Retain complete arguments for the stated variational and capacity descriptions, their domains, normalization, degeneration and attainment boundaries, together with a coherent coefficient-dependence account.
State exactly which scalar and matrix coefficient classes are covered.
A fixed-degree sample, a numerical minimum, the scalar log identity alone, a stationary equation without an extremum proof, or a formula excluding circle zeros cannot silently complete the unrestricted core.

For an explicitly proposed formula class that cannot cover the assigned domain, retain the exact failed implication and proof or counterexample, and identify the corresponding unresolved alternative.
Partial formulas and coefficient theorems receive their actual scope; do not mark the Task complete solely because one proposed class fails.
Any proposed adjustment of the original research objective must be explicit and authorized at its actual scope.

The main agent arranges separately organized review of key new formulas and of the final logical chain against this contract, with self-review, independent AI review and unreviewed source interfaces distinguished.
Completion requires a corresponding Task decision selecting the actual fixed support and a review covering the completed contract.

### Relationship to Lehmer and execution

Complex coefficient dependence is the primary analytical setting.
Integer/Laurent coefficient specializations may supply later inputs to the separate question whether Mahler measures greater than one of integer polynomials have a uniform gap from one.
That Lehmer-gap question is outside this analytical Task's completion criteria and supplies no execution authority here.
A connection back to an integer gap must retain the full polynomial, actual trace normalization and every approximation or small-singular-value cost.

The initial decision assigns an active research objective.
This registration starts no autonomous run.
Any further execution follows the [execution rules](../../framework/rules/execution.md) and Yin's current execution policy, looked up locally in `profiles/Yin/execution.md`.
Do not copy another Task's baseline, usage allowance or stopped period.

## Current decision
[Selected decision](#decision-completed-single-haar-analysis-2026-10-13)

## Continuation

The selected completed decision below owns the final analytical scope.
[S_F0025](../strategies/Yin_S_F0025.md#single-haar-analysis) records the completed route and optional stronger follow-ups.
[Mathematical scope and formula interfaces](../ledger/Yin_L_F0046_v1.md#mathematical-scope) maps the coefficient domains, fixed results and reuse limitations.
The [final contract review](../audits/reviews/Yin_R_F0133_v1.md#f0010-fixed-chain-completion-finding) binds the exact three fixed supporting accounts and their source/review limits.
The [derived strategy entrance](../strategies/index.md#task-yin_t_f0010) is navigation only.

## Lifecycle and completion

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-11T10:21 |
| status | active |
| authority | Yin's explicit request in this conversation to establish an F-series Task for variational and capacity formulas of a determinant in one Haar unitary, and its dependence on coefficients. |
| reason | Register this independently assigned analytical objective with scalar and finite-matrix scope, source/model boundaries, exact completion criteria and an initial continuation strategy. The formulas and coefficient-dependence questions remain unresolved beyond the identified baselines. No autonomous research period is started by registration. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Contract](#contract) | The single-Haar determinant, variational and capacity objectives, coefficient dependence, exact domains and completion criteria stated above. |

### Decision completed-single-haar-analysis-2026-10-13

| Field | Value |
| --- | --- |
| date | 2026-10-13T07:10 |
| status | completed |
| authority | Yin's explicit original assignment of the scalar and finite-matrix analytical Task, followed by the 2026-10-13 instruction to take F0010 as the objective and begin advancing it. This decision records satisfaction of the unchanged assigned contract. |
| reason | The selected fixed accounts establish exact coefficient-defined scalar and finite-matrix capacities, global variational and convolution representations with all stated degeneration and attainment boundaries, and fixed-support coefficient continuity, valid variations and singular controls. The separate final review compares the actual fixed support with all four original objectives and passes the complete contract. No required mathematical argument remains missing. Completion retains the accepted external-statement interfaces and the nonessential known-Gram original-theorem attribution limitation; it asserts neither original discovery, a complete external-proof audit, numerical implementation, degree/size-uniform estimates nor a Lehmer gap. This completion authorizes no execution of the separate Lehmer-gap investigation. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Original contract](#contract) | The unchanged scalar and arbitrary finite-matrix analytical objectives, including circle zeros, zero input, effective degree changes and identically singular matrix determinants. |
| support | [Scalar capacities](../ledger/Yin_L_F0043_v1.md#fixed-f0002-first-round-account) | Complete coefficient-Gram maximum, Toeplitz dual, prediction capacities, exact optimizers and all boundary controls. |
| support | [Coefficient dependence](../ledger/Yin_L_F0044_v1.md#fixed-f0002-first-round-account) | Complete fixed-support continuity and potential theory, exact scalar differentiability boundary, variations and finite-matrix transfer at the stated domains. |
| support | [Matrix capacities](../ledger/Yin_L_F0045_v1.md#fixed-f0002-first-round-account) | Complete block-Gram maximum, positive-field infimum, convolution-capacity limit, normalization and singular/coupled controls. |
| dependency | [DR10 matrix factorization](../audits/literature/DR10/Yin_U002.md#dr10-u002) | Exact accepted same-degree outer matrix-factor existence statement and applicability, without a whole original-proof audit. |
| review | [Final contract review](../audits/reviews/Yin_R_F0133_v1.md#f0010-fixed-chain-completion-finding) | Actual complete fixed chain, all four original objectives, source interfaces, prior whole reviews and exact completion limitations; PASS at the recorded mathematical scope. R_F0133 and its R_F0131/R_F0132 prior findings retain their currently declared unknown initial-context relationships. |

## Pending independent full-chain inspection

The selected 2026-10-13 completion decision records satisfaction of the analytical contract at the stated mathematical scope.
Its selected R_F0133 finding and the prior R_F0131/R_F0132 findings retain unknown initial-context relationships, as disclosed in their responsible review accounts.
They do not establish the separately required independent inspection of the complete Task chain, and no separately sufficient full-chain independent finding is selected here.
That inspection remains pending for the original contract, the complete L_F0043/L_F0044/L_F0045 support, their actual mathematical dependencies and the accepted DR10 statement/applicability interface.
The pending review obligation preserves the historical completed decision, recorded mathematical findings and source limits; it does not activate execution.

## Execution boundary

Local execution requires separate preparation of `execution/Yin_E_F0010.md` under the execution rules.
The lifecycle recorded here does not activate a local run.

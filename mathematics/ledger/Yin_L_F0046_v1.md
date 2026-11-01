---
author: Yin
---

# Single-Haar determinant: mathematical scope and formula interfaces

<a id="mathematical-scope"></a>
## Objects and coefficient domain

The [F0010 contract](../tasks/Yin_T_F0010_v1.md#contract) concerns one Haar unitary U with its probability trace.
For a fixed finite integer interval I, define
\[
 p_a(U):=\sum_{j\in I}a_jU^j,\qquad
 D(a):=\Delta_\tau(p_a(U)),\qquad L(a):=\log D(a).
\]
The coefficients range over the full complex space C^I, including zero coefficients, effective-degree changes, repeated roots, circle roots and the zero polynomial.
Set D(0)=0 and L(0)=-infinity.
Real derivatives of these real-valued functions must be distinguished from holomorphic coefficient dependence.

For finite matrix coefficients A_j in M_r(C), use the ordinary determinant under normalized trace tr_r tensor tau.
Its logarithm is
\[
 L_r(A)=\frac1r\int_{\mathbb T}\log|\det P_A(z)|\,d\mu(z),
 \qquad P_A(z):=\sum_{j\in I}A_jz^j,
\]
with L_r=-infinity when det P_A is identically zero.
The unnormalized total logarithm is rL_r.
A kernel-removed determinant is a different quantity.

<a id="formula-interfaces"></a>
## Mathematical questions and fixed results

| Question | Responsible result and essential scope |
| --- | --- |
| Which coefficient-defined positive variables give exact extrema? | [Scalar Gram and Toeplitz formulas](../claims/Yin_C_F0174_v1.md#argument) give a finite maximum, its equal dual infimum and prediction limits, with explicit optimizer and attainment boundaries. [Matrix formulas](../claims/Yin_C_F0176_v1.md#argument) give block-Gram, positive-field and convolution descriptions with the required trace normalization. |
| Which coefficient information must a capacity retain? | The same scalar and matrix accounts preserve cross-coefficient phase information in Gram constraints. Their covariance-only counterexamples identify an insufficient proposed class without excluding the valid alternative. |
| How do coefficient perturbations interact with zeros and regularization? | [Coefficient dependence](../claims/Yin_C_F0175_v1.md#argument) establishes fixed-support continuity, valid first and second variations, scalar circle-root nonsmoothness, repeated-root controls, and matrix determinant-polynomial transfer. |
| What changes at singular inputs and in finite approximations? | The capacity accounts distinguish finite Gram attainment from bounded-field or analytic nonattainment, retain the ordinary zero branch and pay the actual input-dependent approximation costs. Coefficient regularization and its limits have their separately stated domains. |

The complete proofs and precise source assumptions belong to those three responsible C arguments.
The original L accounts retain the fixed inputs of the historical R/Task decisions and cross-line consumers.
Their exact controls include monomials, circle-nonvanishing polynomials, simple and repeated circle-root crossings, degree drops, zero input, matrix direct sums, coupled coefficients and identically singular matrix determinants.

<a id="reuse-boundaries"></a>
## Reuse boundaries and unresolved stronger questions

- [Luc22 scalar](../audits/literature/Luc22/Yin_U001.md#luc22-kernel-removed-determinant) and [matrix](../audits/literature/Luc22/Yin_U002.md#luc22-abelian-matrix-approximation) interfaces supply the Haar/Mahler identification and trace bookkeeping.
  The ordinary zero branch above remains explicit.
- The [single-Haar weight baseline](Yin_L_G0002_v1.md#single-haar-formulation), [its regularization](Yin_L_G0002_v1.md#regularization-and-direction), and [the finite-section account](Yin_L_G0001_v1.md#degree-window-tests) supply existing methods.
  A trial value in an infimum is an upper bound; fixed-input limits do not supply estimates uniform in degree.
- [F0008's formula](../claims/Yin_C_F0126_v1.md#statement), [attainment result](../claims/Yin_C_F0127_v1.md#yin_c_f0127) and [regularized argument](../claims/Yin_C_F0126_v1.md#regularized-minimum-used-in-the-proof) are methodological comparisons at their free-semicircular hypotheses.
  Those hypotheses are not transferred to powers of one Haar unitary.
- The precise original theorem body for the recognized scalar maximum-Gram method remains an attribution limitation in [the scalar account](../claims/Yin_C_F0174_v1.md#scalar-capacity-finite-sdp) and [its review](../audits/reviews/Yin_R_F0132_v1.md#scalar-capacity-whole-independent-finding).
  Its complete local proof does not depend on that inaccessible body.
  Other external inputs retain their actual statement/applicability or proof-inspection scope.
- A classification of every matrix singular stratum, bounds uniform in degree or matrix size, a numerical solver, and an integer Lehmer gap are outside the established conclusions.

The [coefficient review](../audits/reviews/Yin_R_F0131_v1.md#coefficient-whole-independent-finding), [scalar and matrix review](../audits/reviews/Yin_R_F0132_v1.md), and [whole-contract review](../audits/reviews/Yin_R_F0133_v1.md#f0010-fixed-chain-completion-finding) record the actual mathematical checks.
The [selected Task decision](../tasks/Yin_T_F0010_v1.md#decision-completed-single-haar-analysis-2026-10-13) owns completion.
This note organizes their mathematical scope and does not supply an additional proof or enlarge those review findings.

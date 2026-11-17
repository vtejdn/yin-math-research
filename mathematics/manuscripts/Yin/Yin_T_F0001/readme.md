---
author: Yin
---

# Yin_T_F0001: Affiliated Rationality Manuscript

Primary Task: [Yin_T_F0001](../../../tasks/Yin_T_F0001_v7.md#yin_t_f0001).

## Paper

The current paper is [paper/main.tex](paper/main.tex).
It contains the maximal-\(\Delta\) rationality criterion, the criterion for tuples admitting a liberation dual system with every scalar shift regular, the dual-system criterion, the application to normal generators with nonatomic spectral distributions and L2 liberation gradients, its ordinary conjugate-variable corollary, the arcsine example and a circular counterexample.
The current theorem order, hypotheses, proof routes and numbering are recorded in [organization.md](organization.md).

## Mathematical Provenance

| Paper environment | Authoritative mathematics and fixed review evidence |
| --- | --- |
| `thm:delta` (Theorem 1.4) | [C_F0068 Part A and P1](../../../claims/Yin_C_F0068_v1.md#argument); [R_F0040](../../../audits/reviews/Yin_R_F0040_v1.md) and [R_F0041](../../../audits/reviews/Yin_R_F0041_v1.md) retain their fixed scopes. |
| `thm:intrinsic-analytic` (Theorem 1.7) and `lem:liberation-normalization` (Lemma 4.1) | [C_F0079 v5](../../../claims/Yin_C_F0079_v5.md#statement) and its [whole-v5 mathematical review](../../../audits/reviews/Yin_R_F0093_v1.md#whole-v5-finding) retain general sum normalization and all four equivalent conditions with X_i-lambda regular for every i and every complex lambda in the criterion, without normality or generation. The exact [v4 inputs](../../../claims/Yin_C_F0079_v4.md#argument) and [C_F0068 Part A](../../../claims/Yin_C_F0068_v1.md#argument) retain their stated scopes. The recorded self-review of the narrower [C_F0063](../../../claims/Yin_C_F0063_v1.md#statement) retains its original conjugate-variable scope. |
| `thm:analytic` (Theorem 1.9) | The certificate proof follows [C_F0024-P3](../../../claims/Yin_C_F0024_v2.md#yin_c_f0024-p3), with the retained full-domain interfaces in [C_F0068 Part C](../../../claims/Yin_C_F0068_v1.md#dual-specializations). Lemma 6.6 supplies conjugate variables, Corollary 5.7 gives the certificate criterion, Lemma 6.3 identifies the finite-rank coordinates and Lemma 6.7 supplies the summed identity for the converse. [The original R_F0067 finding](../../../audits/reviews/Yin_R_F0067_v1.md#conclusion) retains its P2 scope and is not a review of P3 or this reorganization. |
| `def:liberation-gradients` (Definition 5.1) | [Voi99-U003](../../../audits/literature/Voi99/Yin_U003.md#voi99-u003) supplies the prescriptions, gradient moments and signed actual-adjoint interface; [Voi99-U004](../../../audits/literature/Voi99/Yin_U004.md#voi99-u004) supplies the finite-information convention. [C_F0083 v2](../../../claims/Yin_C_F0083_v2.md#statement) retains the full individual-algebra domain formulation. The manuscript definition explicitly requires represented well-definedness and the actual adjoint domain. |
| `lem:gradient-liberation` (Lemma 5.2) | [C_F0082](../../../claims/Yin_C_F0082_v1.md#statement) and its [R_F0080 self-review](../../../audits/reviews/Yin_R_F0080_v1.md#whole-deduction) retain the general liberation-gradient construction, using the energy calculation and actual closure in [C_F0063 Appendix A](../../../claims/Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions). The proof on each full coordinate algebra extends both the operator and adjoint domains. |
| `prop:liberation-gradients` (Proposition 5.3) | Direct application of Lemma 5.2, Theorem 1.7 and Proposition 4.5, with normality and nonatomicity imposed explicitly. The criterion holds for every fraction pair, with uniqueness for a fixed pair, and applies to any normalized system. |
| `prop:normal-conjugates` (Corollary 5.7) | Lemma 5.6 verifies the hypotheses of Proposition 5.3, which gives the criterion and maximal Delta. |
| `lem:conjugate-liberation` (Lemma 5.6) | [C_F0025](../../../claims/Yin_C_F0025_v1.md) supplies the normal-phase identities. The manuscript first proves nonatomicity using the closure domain. The conversion to L2 liberation gradients uses the actual polynomial adjoint formula, Voi99 Remark 5.5(c) and relation descent on each full coordinate algebra. |
| `lem:tensor-difference-injectivity` (Lemma 4.3) and `lem:tensor-l2-recovery` (Lemma 4.4) | [C_F0079 v4](../../../claims/Yin_C_F0079_v4.md#argument) retains the complete minimal-tensor-decomposition and quotient-recovery argument, with its [fixed self-review](../../../audits/reviews/Yin_R_F0058_v4.md#finding). The current manuscript separates the algebraic observation into Lemma 4.3 and invokes it for both quotient maps in Lemma 4.4. |
| `prop:liberation-delta` (Proposition 4.5) and `lem:tensor-images-l2` (Lemma 4.6) | [C_F0079 v4](../../../claims/Yin_C_F0079_v4.md#argument) separates maximal Delta from algebraic L2 recovery. The [fixed self-review](../../../audits/reviews/Yin_R_F0058_v4.md#finding) checks individual tensor injectivity under regularity of every scalar shift, coordinate separation, adjoint domains, finite-rank closure and regular cancellation. |
| `lem:fraction-ranks` (Lemma 6.2), `lem:finite-rank-identification` (Lemma 6.3) and `lem:fundamental` (Lemma 6.7) | The current Section 6 extracts the common-denominator and finite-rank identification arguments, and extends the residual-operator construction to a normalized liberation system. |
| `lem:dual-conjugates` (Lemma 6.6) | [C_F0037](../../../claims/Yin_C_F0037_v1.md#yin_c_f0037-p1) supplies the closable-domain spectral-pinching argument, and [C_F0070 Parts A and C](../../../claims/Yin_C_F0070_v1.md#statement) retain the represented derivation and vacuum-adjoint interface. |
| `rem:liberation-without-conjugates` (Remark 5.8) | [C_F0080](../../../claims/Yin_C_F0080_v1.md#statement) fixes the complete arcsine counterexample, both the monomial and Chebyshev proofs, and the compared definitions. Its selected decision adopts the recorded [R_F0053 self-review](../../../audits/reviews/Yin_R_F0053_v1.md#whole-proof-finding). The manuscript retains the monomial proof and records its zero liberation gradient. |
| `rem:normality` (Remark 7.1) | [C_F0074](../../../claims/Yin_C_F0074_v1.md#statement) and [R_F0047](../../../audits/reviews/Yin_R_F0047_v1.md#conclusion). |

Fixed Claim, R and U assessments remain at their responsible mathematical homes.
See the [open manuscript problems](review.md) and the [paper's build record](paper/readme.md).

Section 5 first treats liberation gradients and then ordinary conjugate variables.
Section 6 uses the conjugate-variable case to prove the dual-system criterion, followed by Examples in Section 7.

## Project Choices and Sources

The paper's audience, style models, terminology-source roles, introductory citation order and bibliography display are in [writing.md](writing.md).
Current mathematical symbols and terminology are in [conventions.md](conventions.md).
Current external citation uses and their source-evidence links are in [citation.md](citation.md).

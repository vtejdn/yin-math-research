---
author: Yin
---

# Yin_T_F0001: Affiliated Rationality Manuscript

Primary Task: [Yin_T_F0001](../../../tasks/Yin_T_F0001_v7.md#yin_t_f0001).

## Paper

The current paper is [paper/main.tex](paper/main.tex).
It contains the maximal-\(\Delta\) rationality criterion, the criterion for tuples admitting a liberation dual system with every scalar shift regular, and the dual-system criterion.
The final section separates maximal \(\Delta\) from the existence of a liberation dual system, illustrates the analytic hypotheses, and gives an example in which the two division closures differ on bounded elements.
Remark 4.1 follows the recalled definition at the start of Section 4 and states that L2 liberation gradients give a normalized liberation dual system.
The current theorem order, hypotheses, proof routes and numbering are recorded in [organization.md](organization.md).

## Mathematical Provenance

| Paper environment | Authoritative mathematics and fixed review evidence |
| --- | --- |
| `thm:delta` (Theorem 1.4) | [C_F0068 Part A and P1](../../../claims/Yin_C_F0068_v1.md#argument); [R_F0040](../../../audits/reviews/Yin_R_F0040_v1.md) and [R_F0041](../../../audits/reviews/Yin_R_F0041_v1.md) retain their fixed scopes. |
| `thm:intrinsic-analytic` (Theorem 1.7) and `prop:liberation-normalization` (Proposition 4.2) | [C_F0079 v5](../../../claims/Yin_C_F0079_v5.md#statement) and its [whole-v5 mathematical review](../../../audits/reviews/Yin_R_F0093_v1.md#whole-v5-finding) retain general sum normalization and all four equivalent conditions with X_i-lambda regular for every i and every complex lambda in the criterion, without normality or generation. The exact [v4 inputs](../../../claims/Yin_C_F0079_v4.md#argument) and [C_F0068 Part A](../../../claims/Yin_C_F0068_v1.md#argument) retain their stated scopes. |
| `thm:analytic` (Theorem 1.9) | The certificate proof follows [C_F0024-P3](../../../claims/Yin_C_F0024_v2.md#yin_c_f0024-p3), with the retained full-domain interfaces in [C_F0068 Part C](../../../claims/Yin_C_F0068_v1.md#dual-specializations). Remark 5.1 gives maximal Delta. The MSY23 embedding gives scalar-shift regularity, and Proposition 5.6 supplies a normalized liberation dual system for applying Theorem 1.7. Lemma 5.3 identifies the finite-rank coordinates, and Lemma 5.7 supplies the summed identity for the converse. [The original R_F0067 finding](../../../audits/reviews/Yin_R_F0067_v1.md#conclusion) retains its P2 scope. |
| `rem:liberation-gradients` (Remark 4.1) | [C_F0082](../../../claims/Yin_C_F0082_v1.md#statement) and its [R_F0080 self-review](../../../audits/reviews/Yin_R_F0080_v1.md#whole-deduction) retain the gradient-to-dual construction, both actual domains and normalization. [Voi99-U003](../../../audits/literature/Voi99/Yin_U003.md#liberation-derivation-and-gradient) supplies the cited gradient formulation. The remark states the implication without its construction or estimates. |
| `lem:tensor-difference-injectivity` (Lemma 4.4) and `lem:tensor-l2-recovery` (Lemma 4.6) | [C_F0079 v4](../../../claims/Yin_C_F0079_v4.md#argument) retains the complete minimal-tensor-decomposition and quotient-recovery argument, with its [fixed self-review](../../../audits/reviews/Yin_R_F0058_v4.md#finding). The current manuscript separates the algebraic observation into Lemma 4.4 and applies it to Psi_x and both quotient maps in Lemma 4.6. |
| `lem:tensor-quotient-kernels` (Lemma 4.5) | The elementary vector-space statement is proved directly using a complement to the subspace. Its two kernel equalities are used in Lemma 4.6. |
| `prop:liberation-delta` (Proposition 4.7) and `lem:tensor-images-l2` (Lemma 4.8) | [C_F0079 v4](../../../claims/Yin_C_F0079_v4.md#argument) separates maximal Delta from algebraic L2 recovery. The [fixed self-review](../../../audits/reviews/Yin_R_F0058_v4.md#finding) checks individual tensor injectivity under regularity of every scalar shift, coordinate separation, adjoint domains, finite-rank closure and regular cancellation. |
| `rem:dual-maximality` (Remark 5.1) | [C_F0024 v1, Section 3](../../../claims/Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors) clears finite-rank ranges into the dual domain before using the trace argument from MSY23 Proposition 6.2. The remark uses the generator-first commutator convention. |
| `lem:fraction-ranks` (Lemma 5.2) and `lem:finite-rank-identification` (Lemma 5.3) | Section 5 extracts the common-denominator and finite-rank identification arguments. |
| `prop:dual-liberation-construction` (Proposition 5.6) and `lem:fundamental` (Lemma 5.7) | Proposition 5.6 constructs a normalized liberation dual system for any tuple with a dual system. Lemma 5.7 uses the residual-operator argument for normal generators to compare the fraction commutators and derive the summed identity. |
| `ex:maximal-delta-without-liberation` (Example 6.1) | [C_F0370 v1](../../../claims/Yin_C_F0370_v1.md#statement) proves maximal Delta for the selfadjoint direct-sum pair and rules out liberation duals using its common spectral projection. The [self-review](../../../audits/reviews/Yin_R_F0379_v1.md#shared-projection-finding) checks the matrix criterion and the two adjoint-domain limits. |
| `ex:liberation-without-duals` (Example 6.2) | [C_F0080](../../../claims/Yin_C_F0080_v1.md#argument) supplies the arcsine law, moments and odd-monomial sequence; its [R_F0053 self-review](../../../audits/reviews/Yin_R_F0053_v1.md#whole-proof-finding) retains its fixed original scope. The manuscript applies the moment calculation directly to the ordinary dual commutator and bounds its vacuum pairing using the two domain inclusions. |
| `ex:normality` (Example 6.3) | [C_F0074](../../../claims/Yin_C_F0074_v1.md#statement) and [R_F0047](../../../audits/reviews/Yin_R_F0047_v1.md#conclusion). |
| `prop:scalar-bounded-dual` (Proposition 6.4) | The [rank-one specialization in Kat68-U001](../../../audits/literature/Kat68/Yin_U001.md#scalar-bounded-dual) gives the bounded density criterion and the norm estimate. |
| `ex:bounded-division-closure` (Example 6.5) | [C_F0012 v1](../../../claims/Yin_C_F0012_v1.md#statement) supplies the selfadjoint pair \((h,hbh)\) and the witness \(b\), written in the manuscript as \((X,XSX)\) and \(S\). The [proof in v5](../../../claims/Yin_C_F0012_v5.md#decision-kato-scalar-dual) uses the right free-product lift and the v4 coordinate change to construct the bounded duals for the pair. The manuscript obtains the scalar dual by applying Proposition 6.4. The [self-review](../../../audits/reviews/Yin_R_F0056_v5.md#kato-sandwich-finding) checks the scalar construction and the transfer in v5. The [independent review of v1](../../../audits/reviews/Yin_R_F0056_v1.md#main-counterexample-finding) covers the original construction and norm separation. The manuscript combines the norm separation with spectral permanence to exclude \(S\) from the division closure in \(\mathcal M\). |

Fixed Claim, R and U assessments remain at their responsible mathematical homes.
See the [open manuscript problems](review.md) and the [paper's build record](paper/readme.md).

Section 5 proves the dual-system criterion directly from Theorem 1.7.

## Project Choices and Sources

The paper's audience, style models, terminology-source roles, introductory citation order and bibliography display are in [writing.md](writing.md).
Current mathematical symbols and terminology are in [conventions.md](conventions.md).
Current external citation uses and their source-evidence links are in [citation.md](citation.md).

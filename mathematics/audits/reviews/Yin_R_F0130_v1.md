---
author: Yin
---

# Retained project review: Matrix coefficients of free circular elements and vanishing rho

These are the original review accounts relocated from [the inspected material](../../claims/Yin_C_F0173_v1.md#argument).
References to the argument, sections or formulas above/below retain their original context in that linked material.
The recorded authorship, checking relationship, inputs, verdicts and limitations are unchanged; this administrative relocation performs no new mathematical review.

<a id="circular-example-independent-review"></a>
## Independent review

Reviewed: 2026-10-10T05:20.
Human record author: Yin.
Method: a separately assigned noncontributor agent independently reconstructed the local calculation and checked the cited source interfaces.
The inspected candidate was `mathematics/drafts/Yin_D_F0004.md`, prepared at 2026-10-10T05:17, before this finding was appended.
This finding covers all of the statement, proof and application-boundary sections above; their mathematical content was not edited during review.

Arrangement and inputs: the reviewer first inspected the circular example and standing definitions, reconstructed the cumulants and directly read DG24 before giving preliminary findings.
The complete candidate and the coordinating agent's precise MS17 source locators were then supplied for this exact-text check.
The reviewer did not contribute to the candidate or example, and did not consult the earlier circular-example self-review, proof-generation dialogue or DG24 source-reading record.
Navigation mentioning earlier reviews was seen but not used as evidence.
For the application interface, C_F0170's setting was read; earlier Brown-review conclusions were not used to certify this argument.

Mathematical findings: **pass within the stated scope; no unresolved gap or missing hypothesis found.**
The decisive checks were as follows.

- Formula (1) holds for arbitrary ordered matrices, including q=1.
  Since every u_j commutes with B, each moment factors as the ordered matrix product times the scalar moment.
  In a nested noncrossing contraction, an interval block's output is inserted at its original position, preserving that same order; recursion and uniqueness therefore give the displayed amplified cumulant.
  No commutation among the A_i or x_i is used.
- The scalar semicircular cumulants in (2) follow from the Catalan moments and the scalar moment--cumulant recursion; freeness makes mixed source cumulants zero.
  The c_k have the stated unit mixed covariances, zero unmixed covariances and zero higher cumulants.
  Grouping disjoint source families preserves freeness: in the product-cumulant formula, a partition contributing to a mixed cumulant of words must connect all word blocks, whereas nonzero source-cumulant blocks cannot connect different source groups.
  This also checks the grouping step used for the c_k.
- Direct multiplication proves both paired-coefficient identities.
  Cyclicity of Tr proves the Hilbert--Schmidt adjoint identity.
  Formula (3) has the correct order and adjoints, in particular E(T* x T*)=rho(x*)*.
  Hence rho=0 eliminates both unmixed second cumulants for every x, and the general unpaired centered-pencil assertion follows from (1)--(2).
- The remaining cumulants are exactly of the types allowed by DG24's circular definition.
  Each acquires the phase factor exp(i theta) exp(-i theta)=1, and all other cumulants remain zero.
  The recursion therefore proves invariance of moments with arbitrary B insertions, not merely scalar moments.
  Zero or singular d_k cause no exception, and m=1 gives the stated scalar covariance.
- The example supplies a_0=0 and rho=0 in C_F0170's setting.
  Positive capacity is needed only where that result explicitly assumes it for global absolute continuity.
  This is a checked hypothesis interface, not a fresh validation of the existing Brown or spectral conclusions.

Source completeness: **pass for the sources actually used here.**
The reviewer directly read the retained [DG24 arXiv v2](../../literature/pdf/DG24.pdf), Definition 2.5 on printed/PDF pp. 4--5 and Theorem 2.9(b)/Definition 2.10 on p. 6, using both extracted text and rendered pages.
Their recursion and circular characterization apply with B=M_m(C) and E=id_B tensor tau, without a nondegeneracy assumption.
The reviewer also directly read [MS17](../../literature/pdf/MS17.pdf), Chapter 2, Section 2, Exercise 9 on printed p. 34 / PDF p. 46, and Theorems 13--14 on printed p. 37 / PDF p. 49, again checking rendered pages.
Exercise 9 and Theorem 14 supply the exact foundational assertion in (2); Theorem 13 additionally identifies the product-cumulant formula used to check grouping.
These established scalar freeness and R-diagonal characterizations are accepted at their checked statement and applicability scopes.
Their original full equivalence proofs and cited upstream proofs were not independently re-audited.

Limits and disposition: the complete local proof above is independently reviewed and cleared for fixed registration with this finding preserved.
This review does not re-audit C_F0170, any complete source article/book, or the Brown potential, density and spectral-disk proof.
It makes no novelty determination, formal-verification claim, new Claim adoption or Task-completion decision.
The source-reading navigation is not substituted for the direct inspections reported here.

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Independent review](#circular-example-independent-review) | [Statement and conventions](../../claims/Yin_C_F0173_v1.md#circular-example-statement) | Exact hypotheses, all three assertions and the general centered rho=0 extension checked, including arbitrary complex and degenerate coefficients. |
| [Independent review](#circular-example-independent-review) | [Proof](../../claims/Yin_C_F0173_v1.md#circular-example-proof) | Complete local proof, formulas (1)--(3), circular normalization and freeness, Hilbert--Schmidt adjoint, operator-valued characterization and phase invariance checked with the stated accepted foundational inputs. |
| [Independent review](#circular-example-independent-review) | [Application and review boundary](../../claims/Yin_C_F0173_v1.md#radial-application-interface) | Hypothesis match to C_F0170, capacity qualification and explicit limits checked; the existing Brown and spectral proofs are outside this finding. |
| [Independent review](#circular-example-independent-review) | [C_F0173 statement](../../claims/Yin_C_F0173_v1.md#statement) | Complete unchanged paired and unpaired zero-rho coefficient example: all assertions, amplified cumulant recursion, circular normalization and grouping freeness, covariance and Hilbert–Schmidt adjoint identities, rotation invariance with arbitrary base insertions and the exact radial hypothesis interface. Original DG24/MS17 source and visual/proof limits retained; no Brown or spectral proof is re-audited. |
| [Independent review](#circular-example-independent-review) | [C_F0173 complete argument](../../claims/Yin_C_F0173_v1.md#argument) | Complete unchanged paired and unpaired zero-rho coefficient example: all assertions, amplified cumulant recursion, circular normalization and grouping freeness, covariance and Hilbert–Schmidt adjoint identities, rotation invariance with arbitrary base insertions and the exact radial hypothesis interface. Original DG24/MS17 source and visual/proof limits retained; no Brown or spectral proof is re-audited. |

## Review relationships

| Review | Relationship |
| --- | --- |
| [Independent review](#circular-example-independent-review) | independently reviewed |

## Current retained proof location

The additional C_F0173 bindings locate the unchanged already inspected statement, full local argument and application boundary.
The original C_F0173 inputs, actual 2026-10-10 review arrangement, source readings and all limits remain intact.
This locating maintenance is not a new mathematical review.

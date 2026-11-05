# Review of the F0012 Manuscript

On 2026-11-05T14:18 UTC, the current agent acting for Yin reviewed the complete working-tree `main.tex`, all five included sections, the document bibliography and generated bibliography text, and the project and document prose.
The review followed a complete reading of the [general writing rules](../../../../framework/rules/writing.md), Yin's [author-wide policy](../../../../profiles/Yin/writing/readme.md), the [free-probability policy](../../../../profiles/Yin/writing/free_probability.md), the [manuscript conventions](../conventions.md) and the [bibliography guidance](../../bibliography-guidelines.md).
The agent had the earlier revision discussion, acceptance conclusions and manuscript review in context; the review relationship is `self-reviewed`.
The reading checked the written deductions and their source interfaces, using the [project provenance map](../readme.md#mathematical-provenance), [citation map](../citation.md) and the retained source inspections at their recorded depth.

| Current TeX scope | Finding |
| --- | --- |
| [Introduction](sections/introduction.tex), `def:brown-measure`, `def:pencil`, `def:fk-determinant`, `thm:brown` and `thm:affine` | Checked the Gaussian and tracial normalizations, eigenvalue multiplicity, arbitrary coupling across sizes and the one-event quantifier for each fixed polynomial. The abstract and affine theorem correctly qualify logarithmic mean convergence by finiteness of the limit and distinguish it from determinant convergence. The Brown-measure and determinant definitions have matching source citations and normalizations. The first-use pencil citation and the organization of the core input definitions remain writing issues R10 and R11. |
| [Distance estimate](sections/geometry.tex), `prop:distance` | Checked the compression dimensions, preservation of the compressed subspace by the constant term, the real quadratic map, treatment of empty zero sets at fixed norm cutoff and the Hermitian lift of the complete residual. The polynomial distance inequality is applied with the stated real domain dimension and a nonempty zero set. |
| [Gaussian tubes and monic pencil proof](sections/probability.tex), `lem:gaussian-tube`, `eq:norm-tail` and the proof of `thm:pencil` | Checked the regular-level approximation and segment argument, Gaussian ball mixture, inverse-radius moments through the ambient dimension, Gaussian coordinate scaling and summability. The norm-tail constants are independent of matrix size, and integration gives the displayed uniform first-moment bound. |
| [Affine determinant proof](sections/affine.tex), `subsec:generic-invertibility` and `subsec:global-floor` | Checked maximum-rank divisibility, transfer to Hermitian Gaussian coordinates, the zero-atom exclusion for finite free logarithm, the moving norm cutoff and the deterministic singular-input set. The added-coordinate estimate uses one of the quadratic compressed maps; R9 asks that this hypothesis be explicit in its local statement. R12 corrects the description of the fixed coefficient matrices. |
| [Affine limits](sections/affine.tex), `subsec:affine-counting`, `subsec:affine-as` and `subsec:affine-mean` | Checked the fixed-amplification transform comparison, the normalized Frobenius Lipschitz factor, the summable fluctuation estimates and the logarithmic tail integration down to zero. The minus-infinite branch uses fixed regularizers and the one-sided bound on the unregularized logarithm. |
| [Brown-measure proof](sections/brown.tex), `subsec:linearization` through `subsec:brown-as` | Checked the determinant and inverse identities, the finite fixed-shift probability limit and the factor of the pencil size. Uniqueness of probability limits identifies the almost-sure limit after the affine result is proved. Joint measurability, Fubini on a countable exhaustion and local \(L^1\) convergence give weak convergence on one event. |

No additional error invalidating a main statement was found in the written deductions checked here.
The [independent fixed-proof review](../../../audits/reviews/Yin_R_F0190_v3.md#independent-strong-proof) retains its own inputs and scope.
This manuscript reading does not repeat the proofs of the external source theorems or establish a new independent full-chain review.

## Definition and citation coverage

The definition and citation check covered every section, including informal introductions of the input laws, compressed polynomial maps, Gaussian mixture, tensor blow-up, Cauchy transforms and linearization.
It checked defining equality, introduction before use, ambient structures, notation consistency, source roles, necessary modifiers and the distinction between previous results and the paper's contribution.
The free-probability exemption for the term von Neumann algebra applies, with the required finiteness and faithful normal tracial-state hypotheses stated explicitly.
The core input definitions and the first-use attribution of the pencil formulation remain unresolved as R10 and R11.

All 22 explicit citation occurrences are represented in the current citation map, and the twelve bibliography entries are exactly the cited works.
The retained source inspections support the stated citation roles, including the separate scalar and matrix-valued SS15 uses, the maximum-rank interpretation of DM17, and the normalization and edition conventions.
The document subset preserves the canonical bibliographic facts with the permitted journal abbreviations and cited-edition notes.
The generated bibliography has the selected labels, initials and alphabetical author order; both BSS18 occurrences of `Hermitian` retain their capitalization.
No unresolved or duplicate semantic cross-reference label was found.

## Outstanding writing requests

The current recommendation is minor revision for [R9–R14](revisions.md).
The manuscript sources were not changed by this review.
The organization record and citation map still describe the current TeX.
Compilation and PDF layout were not repeated in this source review; current build facts remain in the [document README](readme.md#latest-build).

## Targeted follow-up findings

On 2026-11-05T14:33 UTC, following the author's question, the current agent rechecked `def:brown-measure` and all uses of `\Delta` in the current TeX.
The initial definition check overlooked that the text only says that `\Delta` acts in the sense of distributions, without naming the Laplacian or specifying its sign and normalization.
The later identity in `brown.tex`, line 166, determines the intended convention, but the first definition still needs its local explanation.
This omission qualifies the earlier definition-coverage account and is retained as [R13](revisions.md#r13-identify-and-normalize-the-laplacian-at-first-use).

On 2026-11-05T14:43 UTC, the current agent rechecked the Han26 comparison in `introduction.tex`, lines 31–34, against the retained source account and the author's question about the sentence's purpose.
The earlier exposition check overlooked that the adjoint observation does not state its intended consequence for the applicability of Han26 Theorem 1.2.
The source attribution remains supported, while [R14](revisions.md#r14-state-the-consequence-of-introducing-the-ginibre-adjoints) requires that consequence and the role of Question 1.8 to be explicit.

---
author: Yin
---

# F0001 Manuscript Writing Choices

## Audience and Manuscript Choices

The paper addresses readers in free probability and operator algebras.
The explicit manuscript choices below apply together with the current repository's mathematical writing rules.

## Style and Terminology Sources

Use MSY23 as the primary style model for the introduction, definitions, theorem statements, proof exposition and transitions.
Yin20 and ACSY24 are additional models for suitable components, with MSY23 remaining primary.
This manuscript has no additional text-reuse restriction.
Apply the current repository's text-reuse rules.
The style role does not adopt MSY23's novelty claims, author information, acknowledgements, funding statements or journal layout.

The selected terminology sources are MSY23, Yin20, Miy22 and MS23.
Hun74 is additionally selected for applicable algebraic terminology and definitions.
The terminology sources have no further priority order; choose the formulation that matches the current mathematics.
Hun74 is not a style model.
The [citation map](citation.md) records actual external citation applications and links to the responsible source evidence.

## Introduction and Explanatory Commentary

After the opening problem paragraph, introduce Connes's rationality conjecture for free group algebras and its connection to Kronecker's criterion.
Continue with DR97's proof, Lin00's extension to affiliated operators and Miy22's semicircular criterion, in that order.
Cite Kro81 as the historical source for Kronecker's criterion.
Retain Con94 IV.3 Proposition 1 for the Hardy-projection commutator formulation; do not attribute that operator formulation directly to Kro81.

Introductory comments may anticipate later results to explain a definition or construction, identify a main idea or proof step, and emphasize a consequential hypothesis, quantifier or conclusion.
They need not state a new mathematical fact.
Judge their usefulness by reader orientation and support in the later argument.
Information also appearing in a theorem does not by itself make a comment redundant.
Keep comments proportionate and accurate, and retain the separate standards for novelty, attribution, comparisons and necessary modifiers.

State the identification \(H=L^2(\M,\tau)\subset L^0(\M)\), and the induced inclusion \(H\otimes_{\C}H\subseteq L^0(\M)\otimes_{\C}L^0(\M)^{\mathrm{op}}\), in the setting of Subsection 1.1.
Introduce \(\M\Omega=\{x\Omega:x\in\M\}\) as a dense subspace of \(H\) immediately before the definition of a liberation dual system, where it is first used to specify operator domains.

## Preliminary Organization

Organize Section 2 in five subsections: division closures and the abstract free field; coordinate maps over division subrings; fractions of affiliated operators; algebraic tensors and finite-rank operators; the invariant \(\Delta\) and free-field realization.
Present the coordinate-map and balanced-tensor argument with the abstract algebraic tools.
Explain the use of “rational in \(X\)” by the equality of division and rational closures when \(\Delta(X)=d\), with a forward reference to the maximal-Delta discussion.
Keep regularity, canonical fractions, fraction terminology and the common-denominator lemmas together, in dependency order.
Define the Hilbert–Schmidt space before the unitary extension of \(\Theta\).
State the consequences of maximal \(\Delta\), including free-field evaluation and equality of rational and division closures, after its definition and finite-rank characterization.
Place the Linnell–Miyagawa comparison at the end of Subsection 2.3: first give the general finite-rank rationality criterion using left and right fractions, then its semicircular analogue with the explicit expression \(\Gamma[Q,r_i^*]\).
Preserve the existing mathematical environments and their semantic labels when reorganizing these materials.

## Liberation Normalization

State the sum-to-\(P_\Omega\) normalization of liberation dual systems as a lemma at the beginning of Section 4.
Define the correction and all corrected operators on \(\M\Omega\), and verify the liberation relations, the sum identity and the common adjoint-domain condition explicitly.
The normalization lemma uses only the liberation dual-system conditions and imposes no normality, scalar-shift regularity or generation hypothesis.

## Mathematical Citations and Attribution

Cite adopted specialized formulations and substantive external results for their actual role.
Explain consequential mathematical adaptations and use precise locators where useful.
Distinguish exposition from historical priority.
Normally cite a definition at its introduction and then use its local reference.
When citing a numbered formula, refer directly to "equation (n)" or "identity (n)", rather than adding an informal label such as "the generator identity in equation (n)".
Routine steps can be omitted when the intended reader can supply them.
A joint background or “see” citation does not by itself assert that every cited formulation is identical.

Use the selected terminology source roles above together with the current repository's terminology rules.
An exemption for explaining a term does not exempt a theorem, proof, construction or historical assertion from its own source requirements.
Source observations remain evidence, not an additional policy layer.

## Bibliography Display

Use alphabetic author–year labels with the `amsalpha` BibTeX style.
The style orders the bibliography by its alphabetic author–year labels, with works of the same author list appearing chronologically.
Display given-name initials followed by complete family names, generated by the style from complete author names stored in the bibliography.
Use the EMS entry structure, Mathematical Reviews journal abbreviations and the cited-items-only rule, with the journal/volume/year/page-or-article-number sequence produced by the selected style.

The manuscript `references.bib` is a synchronized typesetting subset of the canonical [bibliography](../../literature/references.bib).
Store complete author, title and publication fields from the canonical bibliography in the subset, with MR journal abbreviations; retain full journal names and complete publication/edition facts in the canonical bibliography.
Keep category-appropriate structured fields for articles, books, chapters, preprints and article identifiers.
Do not duplicate a complete journal citation in a `note` field.
A note may identify a cited edition or add information not already printed from structured fields.

The selected display is informed by the [MSY23 bibliography observations](../../audits/literature/MSY23/Yin_U005_v1.md#bibliographic-display-observed-in-the-published-edition) and the recorded [AMS/EMS/LMS comparisons](../bibliography-guidelines.md).
These sources support a family of mathematical bibliography practices, not a single universal BibTeX style.
Venue-specific punctuation and fonts do not change source identity or bibliographic accuracy.

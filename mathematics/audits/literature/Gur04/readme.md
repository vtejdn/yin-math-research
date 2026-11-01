# Gur04 Source Audit

<a id="source-version"></a>
## Source and version

The [canonical bibliography](../../../literature/references.bib) identifies the work.
This audit reads the user-supplied published article by Leonid Gurvits, *Classical complexity and quantum entanglement*, Journal of Computer and System Sciences 69 (2004), 448-484, DOI [10.1016/j.jcss.2004.06.003](https://doi.org/10.1016/j.jcss.2004.06.003).

- Local source: [Gur04.pdf](../../../literature/pdf/Gur04.pdf), the current supplied formal article.
- Edition: published JCSS article, 37 PDF pages; printed page equals PDF page plus 447.

On 2026-10-14 the named U001–U005 interfaces and corrections were compared individually with the current formal passages.
U002 corrects its former p.453 square-root attribution; its correct estimate and all other recorded findings remain.
This comparison does not substitute current bytes for an earlier reviewer's input or broaden the original review depths.
- Reviewer: source-audit agent, self-review, 2026-09-12.
The subsequent [original capacity finding](../../reviews/Yin_R_F0176_v2.md#capacity-gur04-finding) checks U002-U003 and two Appendix C counterexamples; its original inherited mathematical context remains unknown, and the other units retain their stated inspection depth.

## Reusable units

| Unit | Scope and exact home | Coverage |
| --- | --- | --- |
| Gur04-U001 | [Positive maps, rank, and ERP](Yin_U001.md#gur04-u001); Definitions 2.1/2.3/2.5, Theorem 2.7, Example 2.9, pp. 450-456 | Definitions and elementary rank/counterexample checked; matroid-intersection theorem accepted only at the stated source-interface depth. |
| Gur04-U002 | [Capacity and approximate scaling](Yin_U002.md#gur04-u002); Definitions 4.2/4.4, Lemma 4.5, Theorem 4.6, pp. 461-464 | Qualitative equivalence reconstructed with explicit elementary dependency supplements; self-reviewed. |
| Gur04-U003 | [Exact scaling and unique minimizers](Yin_U003.md#gur04-u003); Theorem 4.7, pp. 464-465 | Attainment, coercivity, strictness and converse reconstructed; corrected normalizer and \(N=1\) boundary retained. |

## Findings that affect reuse

The qualitative central chain is valid for **positive** maps on complex matrix algebras: rank non-decrease, positive capacity and arbitrarily close doubly stochastic scaling are equivalent.
Exact scaling additionally requires positive attained capacity.
Theorem 4.7's normalization and the \(N=1\) zero-map boundary must be handled as recorded in U003.

The ordinary determinant polynomial is controlled by quantum permanent, and agrees with the rank-nondecrease test only under ERP.
The source itself gives an explicit 3-by-3 skew-symmetric counterexample to omitting that promise.
Thus Gur04's general positive-map theorem and its promised ordinary-Edmonds algorithm have different scopes.

<a id="search-and-coverage"></a>
## Search evidence and coverage boundaries

The source was read by section and theorem using local text extraction.
All seven main sections and the appendix structure were mapped; the detailed reconstructed passages and unchecked subpassages are stated in the units.
PDF pages 10, 12, 15-18, 25 and 31-32 were rendered and visually inspected for normalization, scaling, hardness parameters and Appendix C hypotheses.
Text extraction contains broken mathematical glyphs, so the identified errors were checked against rendered primary pages.
Poppler emitted font-substitution warnings, but the relevant symbols and full statement contexts were legible.

Two bounded web queries were run on 2026-09-12: `"Gurvits" "classical complexity and quantum entanglement" erratum` and `"A deterministic algorithm approximating the mixed discriminant" pdf Samorodnitsky`.
The first did not identify a formal erratum in the returned results; the second did not produce a retrieved primary copy of the earlier Gurvits-Samorodnitsky paper.
Search-result metadata and third-party transcriptions were not used as proof evidence.
The local Gur04 PDF supplies the exact statements; the qualitative capacity/exact-scaling proofs were completed using the elementary reconstructions in U002-U003, not an unverified external inequality.
No claim that all errata or later developments have been searched is made.

The mixed-discriminant upper constant \(N^N/N!\), original earlier source proofs, all quantum-permanent generalizations, the full bit-complexity analysis and the complete hardness reduction are outside the audited proof scope.
A source study covering these identified interfaces is complete at this recorded depth; it is not a certificate that every printed statement in the 37-page article is correct.
No numeric computation, formal verification, source-PDF modification, or publication action was performed.

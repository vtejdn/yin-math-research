---
author: Yin
---

<a id="xia23-u001"></a>
# Xia23-U001: Disk-Cauchy Commutators and the Adjoint Obstruction

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Source: [Xia23, author PDF](https://www.acsu.buffalo.edu/~jxia/Preprints/integv3.pdf), Example 1.6 and formulas (1.5)-(1.7), printed/PDF p. 3. |
| source-locator | Related primary source: [ST06, arXiv v2](https://arxiv.org/pdf/math/0401091v2), Example 8.5, pp. 29-30, and Corollary 8.6, p. 30. |
| inspection | Coverage: **Read; selected statements checked** in parsed primary PDF text. The star-interface source reader checked the original example and metadata; the coordinating agent inspected the Xia passage. |

- Source: [Xia23, author PDF](https://www.acsu.buffalo.edu/~jxia/Preprints/integv3.pdf), Example 1.6 and formulas (1.5)-(1.7), printed/PDF p. 3.

- Related primary source: [ST06, arXiv v2](https://arxiv.org/pdf/math/0401091v2), Example 8.5, pp. 29-30, and Corollary 8.6, p. 30.
  Xia attributes the example to that work.
- Trigger/date: 2026-09-08, assessing the user's proposed adjoint-generated variant [Yin_C_F0003](../../../claims/Yin_C_F0003_v1.md#yin_c_f0003) of Yin_T_F0001.
- Coverage: **Read; selected statements checked** in parsed primary PDF text.
  The star-interface source reader checked the original example and metadata; the coordinating agent inspected the Xia passage.
  No full article audit, rendered page comparison, or original trace-ideal proof certification was performed.

## Relevant Example and Normalization

Xia uses planar area dA, the normal operator N=M_z on L2 of the unit disk, and

\[
(Tf)(z)=\int_B\frac{f(w)}{z-w}\,dA(w).
\]

Example 1.6 states that T is compact, that [N,T] is rank one, and that [N*,T] is not trace class.
Its formula (1.7) displays the kernel (bar(z)-bar(w))/(z-w) for the adjoint commutator.

For the normalized probability measure mu=dA/pi, the project's convention is D=-T/pi, giving [D,N]=P_Omega with [S,T]=ST-TS.
The scalar change of Hilbert-space measure does not affect boundedness or rank.
Yin_C_F0003 proves boundedness directly and proves infinite rank using antiholomorphic monomials, so neither compactness nor the stronger non-trace-class theorem is required as an external dependency.

The parsed text of ST06 Example 8.5 suggests a sign mismatch between its printed kernel and displayed commutator.
This was not checked in a rendered image and is not recorded as a visually confirmed erratum.
The project's signs are fixed by its direct cancellation calculation, which also agrees with Xia's convention after the stated conversion.
Corollary 8.6 confirms the original intended failure of the adjoint trace-class implication, independently of a global sign.

## Search and Verification Boundary

Public searches used generic terms including "Cauchy transform unit disk commutator multiplication normal operator rank one" and "Fuglede theorem finite rank commutator normal operator Cauchy transform."
An encyclopedia result was used only as a lead, not as proof evidence.
The Xia author PDF supplied the exact example; its bibliography led to the original arXiv paper.
The author's publication list and journal issue index established Xia23's publication year; the original work's journal identity supports ST06, while the inspected artifact remains its 2004 arXiv v2.

Search stopped after identifying the matching example and primary locators.
No Unt20 text or private manuscript content was searched or uploaded.
No source PDF was retained locally.
The independently reviewed counterexample and the decision not to replace Yin_C_F0001 belong in the project ledger and proof audit, not in this source statement check.

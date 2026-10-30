---
author: Yin
---

<a id="pv23-u001"></a>
# PV23-U001: Matrix Domains and Scalar Inversion

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | [PV23 arXiv v2](https://arxiv.org/html/2009.08527v2), under the registered source identity (private lookup: `../../../literature/registry.md#kronecker-strategy-intake`). |
| source-locator | §4.3: Definition 4.11, Proposition 4.12, Example 4.13 and Theorem 4.14. |
| inspection | 2026-09-09: Read, with the definition and domain distinction checked; no full proof audit. |

Date: 2026-09-09.
Source/version: [PV23, arXiv v2](https://arxiv.org/html/2009.08527v2), registered in the source index (private lookup: `../../../literature/registry.md#kronecker-strategy-intake`).
Scope: Section 4.3, Definition 4.11, Proposition 4.12, Example 4.13 and Theorem 4.14.
Coverage: **read**, with the definition and domain distinction checked; no full proof audit.

The source separates the scalar rational-expression domain from the matrix domain, which permits block inversions during expression construction.
Property I requires entries of every invertible matrix over an algebra to be expressible using admissible scalar rational expressions in that matrix's entries.
Proposition 4.12 characterizes it by equality of these domains.
Example 4.13 shows stable finiteness alone does not imply Property I; its cited free-ideal-ring foundations were not independently audited here.
Theorem 4.14 concerns the matrix domain over a stably finite algebra.

Consequence for [Yin_S_F0002](../../../strategies/Yin_S_F0002.md#s_f0002): a bounded inverse pencil and scalar elimination remain separate obligations.
Neither Property I for the project algebra nor boundedness of an affiliated inverse follows from these statements.
This is an applicability check, not a counterexample to Yin_C_F0001 or a claim that finite von Neumann algebras fail Property I.

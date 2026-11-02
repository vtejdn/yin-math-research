---
author: Yin
---

<a id="pv23-u001"></a>
# PV23-U001: Matrix Domains and Scalar Inversion

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | [PV23 arXiv v2](https://arxiv.org/html/2009.08527v2). |
| source-locator | §4.3: Definition 4.11, Proposition 4.12, Example 4.13 and Theorem 4.14. |
| inspection | 2026-09-09: Read, with the definition and domain distinction checked; no full proof audit. |

Date: 2026-09-09.
Source/version: [PV23, arXiv v2](https://arxiv.org/html/2009.08527v2).
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

## Additional retained definition source recheck

<a id="pv23-definition-recheck"></a>


Date and reviewer: 2026-09-10, the coordinating agent.
Source: [PV23, arXiv v2 PDF](https://arxiv.org/pdf/2009.08527v2), 2022-10-18, 60 pages; bibliographic identity is in [references.bib](../../../literature/references.bib).
The exact-version temporary PDF was obtained after the web reader failed.
The title, Definition 1.2 on printed/PDF p. 10 and the full p. 46 were read; p. 46 was rendered and visually checked.
This supplements [PV23-U001](Yin_U001.md#pv23-u001), with no whole-paper proof audit.

<a id="matrix-domain-property-i"></a>
## Matrix Domain and Property I

Section 4.3, equation (4.17), p. 46: the matrix $A$-domain of a scalar noncommutative rational function is the union of its expression domains when synthesis may use matrix-valued expressions and matrix inversions before producing a scalar output.
The ordinary $A$-domain uses scalar expressions.
Definition 4.11, p. 46: a unital $K$-algebra has Property I if, for every invertible matrix over it, every inverse entry is the value of a scalar noncommutative rational expression over $K$ in the original matrix entries, defined at that tuple.
This is a general property of the algebra; separate ambient instances are not definitions.
Proposition 4.12 characterizes Property I by equality of scalar and matrix domains for matrix-valued rational functions.
It is a known external result, not a project Claim to reprove.
The existing audit retains its stated verification depth.
No assertion that a particular project algebra satisfies Property I follows just from the definition.

## Stable Finiteness

Definition 1.2, p. 10: for every matrix size, $AB=I$ implies $BA=I$ over the unital algebra.
This is the same general property used in the Yin20/MSY23 rank arguments.
It is not Property I, and the source's counterexample to that implication remains separate from the definitions.

## Citation and Use

The passages are `current formulation` candidates, with no priority claim.
Property I is a comparison input for Yin_S_F0002; Yin_C_F0008's own positive-pivot theorem is not retroactively claimed to depend on PV23.
The [definition-use record](../../../ledger/Yin_L_F0004_v1.md) preserves that distinction.

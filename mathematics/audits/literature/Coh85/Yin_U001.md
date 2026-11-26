---
author: Yin
---

# Cohn's Definition of Division Closure

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Coh85-U001

Source: [Coh85, retained second-edition scan](../../../literature/pdf/Coh85.pdf), Exercises 7.1, item 4, printed p.387 / PDF p.407; ring conventions on printed p.xviii / PDF p.16.

Date and scope: 2026-10-11, direct visual reading for Yin and independent AI verification by a separate agent.
Reading coverage: Read.
This checks the definition, conventions and complex-algebra applicability, not the proofs requested by the exercise or the whole book.

### Definition and applicability

For a ring homomorphism \(f:R\to S\), Exercise 7.1.4 defines the division closure as the least subring of \(S\) containing \(\operatorname{im}f\) and closed under inverses of its elements when these inverses exist in \(S\).
The printed name is division closure.

The p.xviii conventions require rings to have an identity, subrings to inherit it and homomorphisms to preserve it.
For the inclusion \(A\hookrightarrow B\) of unital complex algebras, the resulting subring contains every scalar multiple of the identity and is therefore a complex subalgebra.

### Comparison and citation

[Coh06 Exercise 7.1.3](../Coh06/Yin_U001.md#coh06-u001), printed p.417, defines the same construction as unit-closure.
[Lin00 Section 1](../Lin00/readme.md), retained preprint p.2, also uses division closure.

This is a verified earlier source, not a claim of historical first occurrence.
Exercise 7.1.4 also asks for proofs about rational closure and examples distinguishing the two closures; those tasks were not reviewed here and are not used by this definition.

### Verification and limits

The title and copyright pages identify P. M. Cohn, second edition, Academic Press, 1985, and ISBN 0-12-179152-1.
The PDF is a scan without a useful text layer; extraction supplied only page breaks.
The conclusions above were checked on rendered original pages, including the complete definition and the applicable convention paragraph.
A separate AI reviewer independently inspected both passages and confirmed the specialization without editing this unit.
No computation or formal verification was performed.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Coh85, second edition, Academic Press, 1985; pre-existing local scan, 608 PDF pages. |
| source-locator | Exercises 7.1, item 4, printed p.387 / PDF p.407; ring conventions, printed p.xviii / PDF p.16. |
| inspection | Definition, name, conventions and complex-algebra specialization directly checked visually and independently reviewed by a separate AI agent on 2026-10-11. Exercise proofs and the rest of the book were not audited. |

## Retained selected rational-closure source reading

## Rational-closure comparison

On 2026-10-11, Section 7.1, printed p.382 / PDF p.402, was directly read for the rational-closure definition by matrix inverses, together with Exercise 7.1.4 on p.387 comparing it with division closure.
A separate AI reviewer independently checked these passages and MSY23 Definition 4.7 and pp.25--26.
The definitions distinguish the two closures, including their containment and the stated possibility of strict containment.
Coverage: Read; the exercise's proof tasks and examples were not newly audited.
The earlier division-closure unit retains its original review scope.

<a id="matrix-inverses-and-linearization"></a>
## Matrix inverses and linearization

On 2026-11-26, Yin's writing agent read Section 5.8, printed p. 272 / PDF p. 292, and Theorem 7.1.2 with its proof, printed pp. 383–384 / PDF pp. 403–404, in the retained second-edition scan.
Part (b) of Theorem 7.1.2 gives an entry of the inverse of a full polynomial matrix for each element of the free field, using the inclusion of the free algebra and the family of full matrices.
Section 5.8 gives Higman's linearization by enlargement and uses the convention \(A=A_0+\sum_j A_jx_j\).

For the application to a selected entry of \(B^{-1}\), write \(B=B_0+ab\), where \(a\) is a column and \(b\) is a row supported at the chosen polynomial entry.
The enlargement
\[
\begin{pmatrix} B_0&a\\-b&1\end{pmatrix}
\]
has Schur complement \(B\) at the bottom-right entry.
Its upper-left inverse block is \(B^{-1}\), so each enlargement preserves the desired entry.
Iterating gives a full linear matrix whose inverse yields the same entry between a scalar coordinate row and column.
Cohn and Reutenauer state the resulting existence assertion in Section 3.1, Proposition 1, and refer to Theorem 7.1.2. [CR94, p. 524](../../../literature/pdf/CR94.pdf#page=8).
This reading checks the source passages and this application to an inverse entry.

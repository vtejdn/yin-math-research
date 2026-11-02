---
author: Yin
---

# BJL19: Matrix Geometric Mean and Positive Riccati Equation

Source/version: the artifact is [arXiv:1712.01504v1](../../../literature/pdf/BJL19.pdf), dated 5 December 2017.
Its title, authors and version were checked.
The canonical key follows the 2019 journal publication, verified on the publisher's [article page](https://www.sciencedirect.com/science/article/pii/S0723086918300021); full metadata belongs to [references.bib](../../../literature/references.bib).
Journal page locators have not been inferred from the preprint.

Scope and state: on 2026-10-10 the assigned comparison agent read Section 2, equations (8)–(14) on p. 5 and Theorem 2 and its proof on pp. 6–7 of this preprint.
The selected geometric-mean formula and positive-solution characterization were checked; this is not a whole-paper or optimal-transport proof audit.

The adopted definition and its positive Riccati characterization are retained in the [fixed matrix-geometric-mean entry](../../../ledger/Yin_L_F0054_v1.md#matrix-geometric-mean).
Theorem 2 also characterizes `A^{-1}#B` as the minimizer of `Tr(A X+B X^{-1})`; this is a broader optional comparison.

Boundary: the geometric mean explains the explicit square-root formula and positive Riccati solution.
It does not alone prove a bijection with a domain defined by strict Hilbert–Schmidt positivity; that requires a separate completely positive map estimate.
When `H_b=I+eta(b)` depends on `b`, this is not an identification of a determinant optimization with a fixed-endpoint transport problem.

Search evidence: public searches for the positive solution of `X A X=B` and matrix geometric means located the authors' preprint; the publisher page separately verified the journal identity.
The search stopped once the exact local coordinate formula was identified.

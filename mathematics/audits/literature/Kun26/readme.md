---
author: Yin
---

# Kun26: Semicircular Spectral-Edge Feasibility

Source/version: the artifact is [arXiv:2606.14687v1](../../../literature/pdf/Kun26.pdf).
The title, author and 12 June 2026 version were checked in the retained PDF.
Canonical bibliographic details belong to [references.bib](../../../literature/references.bib).

Scope and state: on 2026-10-10 the assigned comparison agent read Theorem 1.1 and Remark 1.3 (pp. 1–2), Theorem 1.9 (p. 5), Proposition 4.2 and the Schur-complement derivation in Section 4.1 (pp. 14–16).
This is a selected statement and applicability check with the local block calculation checked; it is not a review of the whole source proof or its random-matrix applications.
The original Lehner source was not inspected directly.

In Theorem 1.9 take Hermitian coefficients `A_0=-a_0`, `A_j=-a_j`, and set `eta(x)=sum_j a_j x a_j` and `S=a_0 tensor 1+sum_j a_j tensor s_j`, with free standard semicircular s_j.
Write `Z=b`.
Denote the primal block at scalar value `c=0` by `L(b)` and its Schur complement by `F(b)`; the corresponding block at general c has Schur complement `c I+F(b)`.
Proposition 4.2 forces any feasible Z to be positive definite.
Thus a feasible negative c gives `F(b)>0`, and a strictly positive F(b) permits a sufficiently small negative c.
Since the infimum is the upper spectral edge of -S, strict positivity of S is equivalent to nonemptiness of the strict feasible set.
No attainment of the spectral-edge infimum is needed.

Boundary: this source connection concerns positivity and the linear matrix inequality.
It does not identify an affine determinant minimum, a least feasible matrix or a unique minimizer of a determinant variational functional.
Original Lehner attribution is mediated by Kunisky's Theorem 1.1, not a claim of direct inspection of Lehner's Corollary 1.5.

Search evidence: public searches for Lehner matrix-coefficient norm formulas and semicircular semidefinite programming led to this author preprint; the exact arXiv HTML and PDF were read.
The search stopped once Theorem 1.9 and Section 4.1 supplied the precise LMI comparison.
No private manuscripts were disclosed or searched.

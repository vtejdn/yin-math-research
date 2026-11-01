---
author: Yin
---

# BV04: contextual optimization references

Source: Stephen Boyd and Lieven Vandenberghe, *Convex Optimization* (Cambridge University Press, 2004), retained author-hosted seventh printing with corrections (2009).
Bibliographic identity and artifact facts are in the [canonical bibliography](../../../literature/references.bib); the local artifact is [BV04.pdf](../../../literature/pdf/BV04.pdf).

## Scope and actual inspection

Selected passages were read on 2026-10-10.
This is a contextual source reading, not a whole-book audit or acceptance of a general optimization algorithm for affine determinant functionals.
The title and copyright pages identify the authors, edition, publication year and seventh printing.

- Section 3.3, Example 3.22, printed p.92 (PDF p.106), computes the conjugate of a strictly positive quadratic form.
  On the real Hilbert space of Hermitian matrices, a quadratic form with strictly positive operator `C_c+eta`, where `C_c(x)=cxc` and `c>0`, has its square completion expressed by the inverse of that operator.
  Strict positivity is a necessary separate hypothesis.
  Neither attainment of a remaining infimum nor interchange of extrema follows from this conjugacy.
- Appendix A.5.5, printed pp.650--651 (PDF pp.664--665), derives Schur elimination of a variable from a quadratic form.
  Eliminating a maximizing variable gives the reduced Hessian by this block operation, with its sign determined by the negative Hessian in that variable.
  Positive-definiteness and global conclusions require separate arguments.

The displayed elementary calculations and their quadratic-form specializations were checked.
No surrounding algorithmic or complexity results were reviewed or transferred.
Other chapters remain outside the present scope.
No source prose was reused.

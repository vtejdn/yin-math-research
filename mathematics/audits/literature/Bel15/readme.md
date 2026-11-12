---
author: Yin
---

# Bel15: imaginary-part parametrization

Source: Serban Teodor Belinschi, *Some Geometric Properties of the Subordination Function Associated to an Operator-Valued Free Convolution Semigroup*, arXiv:1503.06390v2, 3 March 2016; original submission 2015.
Bibliographic and artifact facts are in the [canonical bibliography](../../../literature/references.bib).
Retained primary text: [Bel15.pdf](../../../literature/pdf/Bel15.pdf).
The distinct Julia–Wolff–Carathéodory paper, arXiv:1510.05377v2, is registered as [Bel15b](../Bel15b/readme.md).

## Selected reading and application

Read on 2026-10-10.
The title page and introduction, Proposition 3.1 and its setup (printed/PDF pp.6--7), and Remark 3.2 (pp.11--12) were inspected.
The abstract-level lead from the earlier search is thereby replaced by this selected-statement reading.
The complete analytic proof of Proposition 3.1 and the boundary-derivative results of Section 4 were not audited.

Proposition 3.1 fixes a positive regularizer q and expresses the imaginary part v_q(u) through the positive equation

\[
v_q(u)=q+\eta\bigl(((X-u)v_q(u)^{-1}(X-u)+v_q(u))^{-1}\bigr).
\]

Here u is selfadjoint, the base is a C*-algebra, and eta is completely positive on the relevant C*-completion.
The proposition provides an analytic parametrization; Remark 3.2 discusses uniqueness of the fixed point and its relation to the subordination function.

Set the source's formal selfadjoint variable X to zero, take the base M_m(C), and use a completely positive covariance eta composed with evaluation at X=0.
Suppose D=eta(1)>0 and epsilon>0, and set the source regularizer q=epsilon D.
For v>0,

\[
-\operatorname{Im}(u+iv)^{-1}=(v+uv^{-1}u)^{-1}.
\]

Thus v=epsilon D+eta(-Im(u+iv)^(-1)) is exactly this specialization.
Source q denotes the prescribed regularizer, rather than minus the imaginary part of an inverse matrix.

This identification of the positive inner equation supplies no affine determinant variational formula, reduced Hessian formula or ordered-extrema identity.
Such conclusions require separate uniqueness and convexity arguments.
The source is used for contextual attribution; no existing Claim dependency or proof-review scope changes.

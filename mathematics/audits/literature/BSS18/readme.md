---
author: Yin
---

# BSS18: regularized Brown measures and hermitization

Source/version: Belinschi, Sniady and Speicher, *Eigenvalues of non-Hermitian random matrices and Brown measure of non-normal operators: Hermitian reduction and linearization method*.
The [canonical bibliography](../../../literature/references.bib) identifies the 2018 journal article; [BSS18.pdf](../../../literature/pdf/BSS18.pdf) is arXiv:1506.02017v3, 8 September 2017, 37 pages.

On 2026-10-10, the selected statements were read.
Coverage state: **Read**, contextual comparison, self-review.
No full proof audit or new Claim acceptance is asserted.

Sections 2.1.5--2.1.6, equations (7)--(11), printed/PDF pp.6--8, identify the Brown potential, regularized Cauchy transform, positivity of the regularized measure and its weak convergence.
Section 2.2 begins on printed/PDF p.8 with the selfadjoint two-by-two hermitization and conditional expectation.
These passages and the title page were inspected directly; PDF p.7 was also rendered and checked visually.
Traciality and a faithful finite trace are part of the setting.
The one-half trace-log normalization must be retained under matrix amplification with normalized trace.

The selected passages supply the established regularization and hermitization context.
They do not supply a positive-matrix variational minimum, optimizer Hessian or a general uniform estimate as the regularizer tends to zero.
Weak convergence of these measures is not a statement about convergence of arbitrary random-matrix eigenvalue distributions from star moments.
The full linearization and subordination arguments were not audited.
The bounded reading stopped after these interfaces were clear; no source prose was reused.

<a id="polynomial-eigenvalue-question"></a>
## Polynomial eigenvalue-convergence question

On 2026-11-05, an agent representing Yin directly inspected Section 7, “Final remarks: Discontinuity of Brown spectral measure,” printed/PDF pp. 33--34 of the same arXiv:1506.02017v3 edition.
The unnumbered Conjecture is on printed/PDF p. 34; its complete page was also rendered and checked visually.
It takes a polynomial \(p\) in \(m\) noncommuting variables, explicitly allowing \(p\) to be non-self-adjoint, and \(m\) independent self-adjoint Gaussian or, more generally, Wigner random matrices \(X_N^{(1)},\ldots,X_N^{(m)}\) with a free semicircular star-moment limit \(s_1,\ldots,s_m\).
It sets \(A_N:=p(X_N^{(1)},\ldots,X_N^{(m)})\) and \(x:=p(s_1,\ldots,s_m)\), and conjectures that the eigenvalue distributions \(\mu_{A_N}\) converge to the Brown measure \(\mu_x\).
This is the ordinary scalar-polynomial setting; the passage states no matrix-coefficient extension.

For the meaning of the source notation, Section 2.1.4, equation (6), printed/PDF p. 6, was inspected directly as well.
There \(\mu_A\) for a random matrix denotes its mean empirical eigenvalue distribution, while the empirical distribution itself is measure-valued and random.
The Section 7 conjecture does not explicitly specify almost-sure or in-probability convergence, numerical variance conventions, a rate, or detailed Wigner hypotheses.
Thus the passage verifies the attribution of the polynomial eigenvalue-convergence question, including the normalized GUE specialization, without attributing an almost-sure formulation or a general Wigner theorem to this source.
It is a conjecture and supplies no proof of eigenvalue convergence from star moments.
This inspection checks the question, ensemble and polynomial scope and the measure notation; it is not a full proof audit or an independent review of a project argument.

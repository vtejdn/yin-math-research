---
author: Yin
---

# Yin_C_F0026 - Complete Review of the Small-Core Fraction Obstruction

<a id="small-core-fraction-obstruction-finding"></a>

## Actual review relationship

The reviewer proposed the weighted-disk Cauchy--Riemann perturbation mechanism during preliminary mathematical discussion. That substantive contribution to the reviewed construction makes the complete retained finding self-reviewed.
The original independent descriptions, dates and full checked scope are preserved as historical facts; no isolated arrangement or new review is asserted.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Retained complete finding](#small-core-fraction-obstruction-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Retained complete finding](#small-core-fraction-obstruction-finding) | [Exact statement](../../claims/Yin_C_F0026_v1.md#statement) | Whole four-assertion weighted-disk construction, constants, actual closed and adjoint domains, compatible and canonical bounded fractions, distributional failure and exact distinction from compact/Hilbert--Schmidt hypotheses. |
| [Retained complete finding](#small-core-fraction-obstruction-finding) | [Exact argument](../../claims/Yin_C_F0026_v1.md#2-the-probability-space-and-a-bounded-cauchy-dual) | Whole four-assertion weighted-disk construction, constants, actual closed and adjoint domains, compatible and canonical bounded fractions, distributional failure and exact distinction from compact/Hilbert--Schmidt hypotheses. |

- Date and reviewer: 2026-09-10; the reviewing agent.
- Target: [Yin_C_F0026](../../claims/Yin_C_F0026_v1.md#yin_c_f0026), Sections 1-7, authored by another AI agent and allocated by the coordinating agent.
- Disclosure: during preliminary discussion, the reviewer independently suggested the general mechanism of adding a weighted-disk Cauchy-Riemann operator to a bounded Cauchy dual.
  The reviewer did not author the target artifact or its explicit canonical-fraction witness.
  This is a separate review of the complete written construction with that overlap disclosed, not a claim of independent rediscovery or external human review.
- Scope: all four assertions, every constant and operator domain, the density and adjoint calculation, both bounded fraction choices, the distributional obstruction, and the distinction from the stronger ACSY24 hypotheses.
- Outcome: the complete artifact is correct at its stated scope.
  No mathematical correction or unresolved qualification is required.
  The responsible Claim materials and their selected decisions own the current assessment.

## Obligations and Findings

| Obligation | Evidence checked | Finding |
| --- | --- | --- |
| A diffuse finite probability space and dense starred core exist | Polar normalization, coordinate generation, and polynomial approximation on the closed disk | Correct |
| The Cauchy operator is bounded with the required sign | Two absolute-kernel bounds and the Schur calculation; direct cancellation of y-x | Correct; norm at most 16 and commutator P |
| Normalization preserves the relevant data | The vacuum image is bounded and its multiplication operator commutes with both coordinates | Correct |
| The added differential operator is closable with dense polynomial adjoint domain | Weighted integration by parts, vanishing boundary contribution, and an explicit square-integrable adjoint coefficient | Correct |
| The final closed domain is the differential domain | Bounded perturbation of convergent graph pairs | Correct |
| Both generator commutators extend boundedly | The Cauchy commutator plus the elementary Wirtinger identities | Correct |
| One fraction choice works | Polynomial coefficients preserve the core, giving minus P | Correct |
| The canonical fraction choice fails literally | Its bounded numerator has a non-square-integrable distributional derivative near zero | Correct |
| The obstruction has exactly the claimed scope | The added adjoint commutator is noncompact, and the compatible fraction choice remains available | Correct |

## Measure, Density, and the Bounded Cauchy Dual

For the weight $w=(4/\pi)(1-r^2)^3$, polar integration gives $8\int_0^1r(1-r^2)^3\,dr=1$.
The weight is positive on the open disk, and planar Lebesgue measure has no atoms.
Thus the integral trace on the corresponding equivalence classes in $L^\infty$ is faithful and normal, and the algebra is diffuse.
The coordinate and its conjugate generate the Borel sigma algebra modulo null sets, so the normal coordinate generates the indicated von Neumann algebra.
Polynomials in the coordinate and its conjugate are uniformly dense in the continuous functions on the closed disk by Stone-Weierstrass.
The latter functions are dense in the weighted L2 space, proving the required Hilbert-space density.

The translated disk is contained in a disk of radius two, and $\int_{|v|<2}|v|^{-1}dA(v)=4\pi$.
Multiplication by the weight bound $4/\pi$ gives exactly the constant 16 in both Schur estimates.
The displayed Cauchy-Schwarz argument therefore gives $\|K\|\le16$.
It first applies to bounded inputs and then extends by their Hilbert-space density.
The same absolute-kernel estimate gives $\|K\Omega\|_\infty\le16$.
Consequently the bounded normalization $G=K-M_{K\Omega}$ is legitimate, with the available bound $\|G\|\le32$.

Direct substitution gives $(KX-XK)f=\int f\,d\mu$, so the sign in $[K,X]=P$ is correct.
The commutator with the conjugate coordinate has kernel $(\bar y-\bar x)/(y-x)$.
Its absolute value is one off the product-null diagonal, so its Hilbert-Schmidt norm is exactly one.
The abelian multiplication correction commutes with both coordinates and therefore changes neither commutator.
It makes $G\Omega=0$ without changing any later differential-domain issue.

## Weighted Adjoint and the Actual Closed Domain

The Wirtinger conventions in the target give $\partial_{\bar z}z=0$ and $\partial_{\bar z}\bar z=1$.
With the inner product linear in its second variable, integration by parts yields
\[
E^*p=-\partial_zp+\frac{3\bar z}{1-|z|^2}p
\quad(p\in\mathcal A).
\]
The sign and conjugation are correct because $\partial_z w=-3\bar z\,w/(1-|z|^2)$.
On a disk of radius R, the boundary contribution is bounded by a fixed polynomial-dependent constant times $(1-R^2)^3$.
It tends to zero as R tends to one, justifying the boundary-free identity without imposing a hidden boundary condition on the polynomials.

The adjoint coefficient has squared norm
\[
72\int_0^1r^3(1-r^2)\,dr
=72\left(\frac14-\frac16\right)=6.
\]
The remaining polynomial factors and derivatives are bounded, so every polynomial belongs to the adjoint domain.
That domain is dense, and E is therefore closable.

Adding the bounded G gives $\overline{D_0}=G+\overline E$ with exactly the domain of $\overline E$.
This equality also follows directly from the equivalence between convergence of E-images and D0-images along a Hilbert-convergent polynomial sequence.
The polynomial adjoint domain is retained, with $D_0^*=G^*+E^*$ on it.
Normalization and both commutator identities in equation (15) follow with the stated signs.
Graph approximation proves invariance under the coordinate and its adjoint on the full closed domain.
No conclusion about invariance under all bounded measurable multipliers is used at this point.

The Hilbert space is infinite dimensional, so its identity operator is noncompact.
Adding the compact Hilbert-Schmidt Cauchy commutator cannot make it compact.
Thus the final adjoint-generator commutator is bounded but noncompact and is not Hilbert-Schmidt.
This verifies the exact distinction from the ACSY24 derivation interface.

## The Fractions and the Distributional Obstruction

The coordinate is nonzero almost everywhere and has affiliated inverse $u=1/z$.
It is bounded and regular as a denominator, even though its inverse is unbounded.
The polynomial fraction choice $s_0=t_0=X$ and $a_0=b_0=1$ has all required inputs in the core and gives $XD_0-D_0X=-P$.

For the other choice, $|u|=1/r$ implies
\[
(1+|u|^2)^{-1/2}=\frac r{\sqrt{1+r^2}}.
\]
Multiplying by u gives the stated numerator $b=e^{-i\theta}/\sqrt{1+r^2}$.
All four coefficients are bounded and the positive denominators are nonzero almost everywhere, hence regular.
Both fraction identities and their identification with the positive canonical bounded-transform fractions are correct.

If b were in the domain of $\overline E$, polynomial graph approximants would converge together with their Wirtinger derivatives in the weighted Hilbert space.
On every disk of radius less than one, the weight is bounded above and below by positive constants.
The convergences therefore hold in ordinary local L2, and testing against compactly supported smooth functions identifies the distributional derivative of b with the asserted Hilbert-space limit h.

On the punctured disk, direct polar differentiation gives
\[
\partial_{\bar z}b
=\frac12\left(-\frac r{(1+r^2)^{3/2}}
+\frac1{r\sqrt{1+r^2}}\right)
=\frac1{2r(1+r^2)^{3/2}}.
\]
The angular sign in this calculation is correct.
Its squared weighted L2 integral on the punctured disk of radius one-half is
\[
2\int_0^{1/2}\frac{(1-r^2)^3}{(1+r^2)^3}\,\frac{dr}{r},
\]
which diverges because the continuous ratio has a positive lower bound there.
Agreement on the punctured annuli already contradicts h belonging to H.
No assumption about a possible additional distribution supported at zero is needed.
Thus b is outside the actual closed E-domain and, by bounded perturbation, outside the actual closed D0-domain.

At the polynomial test vector Omega, the first term of the canonical-fraction defect would require the nonexistent Hilbert-space value $\overline{D_0}(b\Omega)$.
The literal two-term expression is therefore undefined there.
The argument does not claim that a distributional combined expression could not be regularized after multiplication and cancellation.
Such a regularization is a different definition, exactly as the artifact states.

## Scope and Verification Limits

The example proves that merely bounded adjoint-generator commutators on the starred core do not supply the arbitrary-fraction domain formulation of Yin_C_F0024.
It also proves failure of the inclusion of every bounded vector in the closed dual domain.
It does not refute the Hilbert-Schmidt hypotheses of ACSY24, because those hypotheses fail explicitly in this example.
It does not refute an existential compatible-fraction condition, since the polynomial fractions already work.
It does not decide a rationality theorem based on another rigorously specified common domain or a closure of a combined defect.

The reviewer checked the complete artifact and recomputed the displayed constants, signs, fractions, and local divergence directly.
No whole-paper source result is required for this construction, and no uninspected source theorem is introduced by this review.
This is not numerical validation, proof-assistant verification, external human review, or a historical-priority assessment.
The target was not edited during the review.

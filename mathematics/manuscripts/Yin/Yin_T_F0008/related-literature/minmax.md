---
author: Yin
---

# Related literature for the ordered min--max section

The original analysis below follows Section 6 of the 33-page revision identified in the [original inventory](readme.md#original-29-item-inventory-in-the-33-page-revisions-order); its theorem and equation numbers are retained as historical locators.
It recorded contextual citation candidates, not new proof dependencies or novelty findings.
The local Bia97 and BCG25 reading records were consulted first, followed by the selected reading specified below on 2026-10-10.
The later authorized integration in the [current Section 6](../paper/sections/ordered-minmax.tex) is recorded at the end of this note.

## Proposition 6.1: the shifted scalar semicircle

The manuscript identifies the logarithmic determinant with an ordered minimum in the real variable after a maximum in the nonnegative imaginary variable.
It also gives the optimizer inside and outside the semicircular support.

**Direct comparison: BCG25.**
David Belius, Francesco Concetti and Giuseppe Genovese, *Variational formula for the logarithmic potential of free additive convolutions*, arXiv:2506.19064v1 (2025), [primary PDF](https://arxiv.org/pdf/2506.19064), equation (1.6), Theorem 1.1 and Section 1.3.
This work was already registered and [locally read](../../../../audits/literature/BCG25/Yin_U001.md), but was absent from the manuscript's then nine-entry bibliography.
Its semicircle specialization supplies a branch-restricted scalar infimum for real points below the lower spectral edge.
Theorem 1.1 treats more general compactly supported scalar free convolutions; Section 1.3 explains why the branch restriction matters.

For the manuscript's variance convention set their beta squared equal to sigma.
Their Stieltjes transform uses the denominator lambda minus z, so its sign must be converted before comparing it with the manuscript's matrix Cauchy transform.
Proposition 6.1 allows every real shift and optimizes in two successive variables.
Equality of determinant values in the common exterior regime does not identify the trial domains or justify exchanging extrema.
The strongest editorial use is a short comparison after the scalar formula, with the broader free-convolution discussion placed after Proposition 6.2.
No claim of a new formula or of an extension of their entire theorem is supported by this bounded search.

**Methodological contrast: Sion.**
Maurice Sion, *On general minimax theorems*, Pacific Journal of Mathematics 8 (1958), 171--176, [publisher PDF](https://msp.org/pjm/1958/8-1/pjm-v8-n1-p14-s.pdf), Section 3, Theorem 3.4 and its following compactness corollary.
The relevant requirements include quasi-concavity/quasi-convexity, appropriate semicontinuity and compactness.
These are conditions for interchanging extrema.
The manuscript instead proves convexity of the function obtained after maximizing and gives a scalar example where the displayed optimizing pair is not a global saddle.
Consequently this source is an optional contrast, not a proof reference for Proposition 6.1.
The existing concrete example may already explain the distinction adequately; a citation is useful only if the paper discusses minimax duality explicitly.

## The commuting-coefficient consequence, equation (6.5)

Simultaneous diagonalization and separability reduce the expression to copies of Proposition 6.1, with deterministic diagonal entries handled separately.
The BCG25 comparison carries over componentwise on appropriate exterior regimes, but supplies no additional matrix-coupling result.
No separate research citation is recommended merely for this finite direct-sum step.
Its role in the article is to identify a transparent matrix class and to prepare the contrast with isotropic and noncommuting covariances.

## Proposition 6.2: isotropic covariance and the spectral coordinate

**Direct identification, already cited: Bia97.**
Philippe Biane, *On the free convolution with a semi-circular distribution*, Indiana University Mathematics Journal 46 (1997), 705--718, [journal page](https://www.iumj.indiana.edu/IUMJ/FULLTEXT/1997/46/1467).
Section 3, Lemma 4, Proposition 2 and Corollary 3 identify the boundary coordinate and density.
The retained published PDF, printed pp.708--711, was reread alongside the [existing source note](../../../../audits/literature/Bia97/readme.md).
The correspondence is t=sigma, the input measure equal to the empirical eigenvalue measure nu, the boundary height v_t(p)=q(p), and psi_t(p)=X(p).
This is an exact identification of those parts of the proposition.
The source does not state the manuscript's ordered determinant optimization.

BCG25 provides a complementary comparison: its scalar convolution setting is broader, while its displayed variational theorem is confined to the left exterior and a selected branch.
The manuscript uses a finite-atomic nu induced by a matrix and obtains its ordered expression for every real x.
These two different directions of scope should be stated separately.
This is a worthwhile contextual citation in Section 6.2, and possibly one sentence in the introduction's discussion of related variational formulas.

**Original research lead: operator-valued boundary geometry.**
Serban Teodor Belinschi, *Some Geometric Properties of the Subordination Function Associated to an Operator-Valued Free Convolution Semigroup*, [arXiv:1503.06390v2](https://arxiv.org/abs/1503.06390v2), revised 2016.
Its author-supplied abstract explicitly places operator-valued semicircular convolution and boundary subordination in the continuation of Biane's work.
In the original search the primary abstract and version history were read, but repeated PDF/HTML requests failed, so that analysis adopted no theorem-level assertion.
It was identified as further reading for the transition from scalar boundary coordinates to Theorem 6.4.
The [subsequent Bel15 inspection](#bel15-integration-followup) records the now-retained source and the exact equation comparison separately.

## Remark 6.3 and the covariance counterexample after Theorem 6.4

**A useful distinction from MDE literature.**
Oskari Ajanki, Laszlo Erdos and Torben Kruger, *Stability of the Matrix Dyson Equation and Random Matrices with Correlations*, [arXiv:1604.08188v5](https://arxiv.org/abs/1604.08188v5), [published article](https://doi.org/10.1007/s00440-018-0835-z), 2019.
Assumption A1, equation (2.7), compares the positive-map output on R>=0 with the normalized trace of R times the identity.
Exact statement reading is recorded in [the core analysis](core.md).

The manuscript's isotropic map sigma tr(.) I satisfies that order-comparison condition but annihilates traceless matrices when m>1.
Thus order flatness does not imply strict positivity as a Hilbert--Schmidt operator.
Conversely, the manuscript's map eta(b)=ZbZ is completely positive and invertible but has a negative Hilbert--Schmidt eigenvalue.
Together these examples distinguish three different hypotheses: complete positivity, order flatness, and positive definiteness on Hilbert--Schmidt space.
A concise comparison beside Remark 6.3 would prevent readers from importing an inapplicable regularity or variational theorem.
The quantitative MDE results have further hypotheses and are not invoked to prove Theorem 6.4.

## Theorem 6.4: a matrix ordered minimum and maximum

The important connection is between the optimizing equations and an operator-valued Dyson equation, together with convexity obtained after the inner maximization.
The HRS07 and AEK sources described in [core.md](core.md) are relevant to the branch-selection and stability parts of this mechanism.
Biane and Belinschi provide scalar and operator-valued subordination context.
None of the checked statements has been identified here with the complete ordered formula of Theorem 6.4, including its Hilbert--Schmidt positivity hypothesis, boundary maximizers and attainment assertions.

**Optimization interpretation of the proof.**
Stephen Boyd and Lieven Vandenberghe, *Convex Optimization* (2004), [author-hosted book](https://www.seas.ucla.edu/~vandenbe/cvxbook/bv_cvxbook.pdf), Appendix A.5.5, printed pp.650--651, explains the Schur complement produced by eliminating variables from a quadratic form.
In the manuscript the Hessian blocks are B, -B and C, so differentiation of the maximizing equation yields the reduced Hessian B+C B^{-1} C.
This is the same elimination operation, with the sign dictated by maximization.
The source is a useful optional explanation of the method; it does not establish the positive definiteness of B for this Dyson problem or global convexity of the unreduced function.
Its classical background status makes a citation less urgent than the closer free-probability comparisons.

The centered equality (6.21) should be connected back to the capacity discussion in Section 1 and Lemma 4.1, as the manuscript already does.
An operator-scaling citation can provide context for the equation eta(b)=b^{-1}, but must retain the stronger hypothesis here: positive capacity alone does not supply all the attainment and uniqueness properties used in this subsection.

## Remark 6.5: completion of the quadratic correction

**Exact standard construction, optional reference.**
Boyd and Vandenberghe, Section 3.3, Example 3.22, printed p.92, gives the conjugate of a strictly positive quadratic form.
Apply it to the real Hilbert space of Hermitian matrices with Q=C_(c_b)+eta.
The inverse quadratic correction is exactly the maximum of the associated linear-minus-quadratic expression.
Its use explains why this second ordered representation needs the inverse of Q but not the inverse of eta.

The completion is already proved in a few lines in the manuscript, so a citation is optional and can be omitted for the intended mathematical audience.
If terminology is useful, call it quadratic conjugacy or completion of the square.
Neither that identification nor Sion's theorem supplies attainment of the infimum in b or an interchange of extrema.

<a id="search-scope-and-remaining-work"></a>
## Original search scope and limits

The search found BCG25 already in the repository, rather than a newly acquired source.
Bia97 was verified using the retained primary article after the publisher PDF endpoint failed.
BCG25's arXiv PDF was read at equations (1.6), (1.12)--(1.15) and Section 1.3; the author's PDF order was used rather than the differing arXiv metadata order.
Sion's Section 3 was read from the publisher.
The UCLA copy of Boyd--Vandenberghe succeeded after the Stanford endpoint timed out; Examples 3.22--3.23 and the Schur-complement passages were read, not the whole book.
Belinschi remained an abstract-level lead at the end of that original search.

It does not establish that no exact matrix min--max precedent exists.
The highest-value editorial addition in this section is the BCG25 comparison; the AEK hypothesis distinction is next.
The remaining references should be selected only if their explanations improve the actual text.

## Authorized integration in the current manuscript

Yin subsequently authorized the whole substantive comparison map, retaining the existing section structure and concise prose.
The [current ordered min--max section](../paper/sections/ordered-minmax.tex) implements the following placements with actual canonical keys:

- Before `prop:minmax-isotropic`, `Bia97` retains the exact boundary-coordinate/density identification, and `BCG25` supplies the broader-input but branch-restricted left-exterior comparison.
  This one paragraph also covers the scalar and commuting specializations without repeating it after each formula.
- In `rem:minmax-domains`, `AEK19` explains why isotropic order flatness does not imply strict positivity on Hilbert–Schmidt space.
- After `eq:minmax-matrix-inner` and the auxiliary uniqueness argument, `Bel15` identifies the positive inner equation as the specialization recorded below.
  `HRFS07` supplies the related half-plane uniqueness context in Section 2; it is not cited as a proof of the entire ordered formula.
- After `eq:minmax-matrix-hessian`, `BV04`, Appendix A.5.5, explains the Schur-complement elimination.
  In `prop:minmax-square-completion`, Example 3.22 explains the exact quadratic conjugacy.
  Neither citation asserts an interchange of extrema or attainment of the remaining infimum.

Sion remains a methodological comparison in this analysis, rather than a manuscript proof reference: the paper retains its concrete non-saddle example and does not invoke minimax interchange.
The commuting reduction and centered specialization keep their existing direct arguments.
This implements the substantive connections without assigning an external theorem to every elementary step.
The [integration review](../paper/review.md#citation-and-mathematical-comparison-checks) owns manuscript verification, and the [document README](../paper/readme.md#receiving-build) owns build evidence.

<a id="bel15-integration-followup"></a>
### Bel15: retained source and exact inner-equation specialization

The subsequent source acquisition retained [Bel15.pdf](../../../../literature/pdf/Bel15.pdf), arXiv:1503.06390v2.
The [scoped source record](../../../../audits/literature/Bel15/readme.md) records direct reading of Proposition 3.1 and its setup (printed/PDF pp. 6–7), and Remark 3.2 (pp. 11–12).
These passages were also checked against the TeX by the bounded integration reviewer.
This later reading resolves the original access limitation for the stated comparison; the complete analytic proof and unrelated boundary results are not claimed as audited.

Take the source's base algebra to be \(M_m(\mathbb C)\), its selfadjoint variable \(X=0\), and its prescribed regularizer \(q=\varepsilon D\), where \(D=\eta(1_m)>0\) has already been proved in the manuscript.
Composing the manuscript covariance with evaluation at \(X=0\) gives the required completely positive map.
Proposition 3.1 then reads

\[
v=\varepsilon D+\eta\bigl((v+uv^{-1}u)^{-1}\bigr),
\qquad u=u^*,\quad v>0.
\]

Since \(-\operatorname{Im}(u+iv)^{-1}=(v+uv^{-1}u)^{-1}\), this is exactly `eq:minmax-matrix-inner`.
The source's \(q\) is the prescribed regularizer; it is not the manuscript's temporary notation for minus the imaginary part of the inverse matrix.
The current prose explicitly distinguishes those source variables.
The identification supplies the subordination interpretation of the inner equation, not the manuscript's variational functional, its reduced Hessian, the order of the extrema or their determinant value.

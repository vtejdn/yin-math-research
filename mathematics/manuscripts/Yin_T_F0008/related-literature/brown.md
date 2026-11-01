# Related literature for the Brown-measure applications

Author: Yin.

Search and reading date: 2026-10-10.
Scope: Corollary 1.7, Proposition 1.8 and every named result and substantial unnumbered discussion in Section 7 of the current [manuscript](../paper/sections/spectral.tex).
This is a selective related-literature assessment, not a novelty assessment, a source intake, or an independent proof audit.
Existing TeX, bibliography entries, registry records and fixed mathematical materials are unchanged.

The purpose is to explain direct and indirect mathematical connections beyond indispensable proof inputs.
A source's usefulness for comparison does not make it a premise of the manuscript's proof.
Source identifiers below are local navigation labels, not newly allocated bibliography keys.
For each source, the stated reading depth applies to every proposed use below.

## Coverage in manuscript order

### Corollary 1.7: capacity bound and absence of atoms

**Content.**
For arbitrary complex coefficient matrices and every shift, the manuscript bounds the determinant below by the centered capacity value.
Positive capacity therefore excludes every atom of the Brown measure.
This is stronger than mere triviality of the kernel at one shift, but does not assert a planar density.

**Worth connecting.**
Keep the existing MS24 determinant-capacity reference.
Add a comparison, in Section 7.2 rather than the introductory corollary, with [ACSY24](#acsy24) and [SS15](#ss15): their atom/rank framework identifies a different observable unless the evaluated operator is normal.
For an analytic regularization comparison, [BYZ](#byz) provides a useful contrasting class with planar absolute continuity under scalar free circular addition.

**Writing value and boundary.**
Explain that the present sufficient condition concerns a uniform lower bound for the logarithmic potential.
Do not present rank-based non-atomicity or the circular-addition density theorem as proofs of this general result.
The two alternative connections are useful only if the paragraph states this difference; a bare list of atomlessness papers would be misleading.

### Proposition 1.8: radial distribution and full operator spectral disk

**Content.**
Under zero constant term and vanishing pseudo-covariance, the potential is a concave function of squared radius, its derivative gives the radial distribution, and the full spectrum is the disk of radius `sqrt(r(eta))`.
The Brown measure has an area density away from zero; positive capacity removes its possible origin atom.

**Worth connecting.**
[AK20](#ak20) is the closest existing comparison for matrix-coefficient circular combinations.
[HL00](#hl00) supplies the classical scalar R-diagonal perspective.
Place a short orientation sentence in Introduction 1.4, with the substantive comparison after Proposition 7.4.

**Boundary.**
Operator-valued circularity and scalar R-diagonality are different hypotheses.
A comparison must not apply the scalar S-transform formula merely from `rho=0`.
Nor may the operator spectral disk be silently identified with Brown support.
These distinctions are already important in the manuscript and make the comparison informative.

### Section 7.1 and Definition 7.1: potential, support and regularization

**Content.**
The shifted determinant is the normalized logarithmic potential; its distributional Laplacian is the Brown measure.
Attainment detects bounded invertibility.
The regularized minimizer equals the conditional expectation of the squared-singular-value resolvent.

**Worth connecting.**
Existing [MS17](#ms17) already supplies the basic convention.
[Belinschi--Sniady--Speicher](#bss18) is a more focused research reference for the regularized Cauchy transform and hermitization.
Use it near (7.5)--(7.7), or reserve it for the final comparison in Section 7.5, to avoid duplicate exposition.

**Boundary.**
The source provides a computational framework, not this positive-matrix variational representation.
Weak convergence of regularized measures and convergence of finite-matrix eigenvalue distributions are separate issues.
No additional citation is needed merely to repeat the definition if MS17 remains the chosen reference.

### Proposition 7.2: possible locations of atoms

**Content.**
Invertibility of the deterministic constant shift implies positivity of the determinant of the full pencil.
Consequently possible Brown atoms lie among eigenvalues of the constant matrix.
The proof uses the main formula to obtain monotonicity along rays, then factors out an invertible constant matrix.

**Worth connecting.**
[ACSY24](#acsy24) offers an algebraic comparison: point-spectrum atoms, rational evaluation and rank.
[HS09](#hs09) explains the broader Brown-measure spectral-subspace setting.

**Writing value and boundary.**
This is a good place to explain what kind of atom information is being obtained: a location restriction, without atom weights or a claim that every allowed location is occupied.
No exact external theorem proving this whole proposition under precisely its arbitrary-coefficient hypotheses was verified in this bounded search.
That statement is a search limit, not evidence of novelty.
Do not add a theorem citation that only treats selfadjoint polynomials as if it proves this nonnormal statement.

### Unnumbered discussion after Proposition 7.2: atomlessness, area density and kernels

**Content.**
A selfadjoint semicircular example separates absence of atoms from planar absolute continuity.
Equation (7.11) obtains the trace of a kernel projection from the regularized minimizer.
The nilpotent `2 x 2` example separates that trace from the Brown atom weight.

**Worth connecting.**
[ACSY24](#acsy24), Section 2.1, directly discusses the second distinction.
[HS09](#hs09), Theorem 1.1, gives the spectral-subspace projection whose trace equals Brown mass.

**Recommendation.**
This is among the best additional citations in Section 7: it turns a local caution into a connection with the established distinction between geometric point-spectrum weights and Brown-measure mass.
The manuscript's elementary examples should remain; they make the difference immediately visible.

### Example 7.3 and the cumulant explanation: matrix-valued circularity

**Content.**
Pairing coefficients `d_k/sqrt(2)` and `i d_k/sqrt(2)` yields `rho=0` and `eta(x)=sum d_k x d_k*`.
Only the alternating second operator-valued cumulants survive.
Rotation invariance follows before using the main determinant theorem.

**Worth connecting.**
Keep [DG24](#dg24), with its separate characterization and definition locators.
The example also gives the exact model used in [AK20](#ak20).
A brief forward connection to the matrix-covariance literature has real value; an additional general reference on scalar circular elements adds little.

**Boundary.**
DG24 identifies the distributional class; it does not supply the radial determinant formula or spectral calculation in the manuscript.
The arbitrary matrix coefficients should remain explicit when comparing with a scalar circular element free from a deterministic deformation.

### Proposition 7.4: radial density and regularized minimizers

**Content.**
The squared-radius envelope determines the distribution, yields local Lipschitz regularity away from zero and the estimate `beta(z) <= 1/(pi |z|^2)`, and recovers the radial distribution from regularized optimizers.

**Worth connecting.**
The existing [AK20](#ak20) paragraph is well placed.
[HL00](#hl00) provides a distinct radial calculation using an S-transform when scalar R-diagonality is available.

**Recommendation.**
Explain this as a comparison of available data and hypotheses: the manuscript uses the covariance map and positive-matrix trials, whereas the scalar theory uses the singular-value distribution.
Do not claim a variable substitution or a direct derivation between the two formulas without proving it.
The density estimate in the manuscript controls average mass per squared radius; it does not give monotonicity of pointwise density.

### Unnumbered discussion after Proposition 7.4: spectral disk versus Brown support

**Content.**
The manuscript deliberately distinguishes the full spectrum from Brown support and permits degenerate covariance maps.

**Worth connecting.**
[AK20](#ak20) gives the relevant stronger flatness regime.
The deformed commutative-base setting of [Alt--Kruger, deformed circular elements](#ak-deformed) supplies a useful route toward support geometry; its companion [Alt--Kruger, pseudospectrum](#ak-pseudo) links support to random-matrix pseudospectra.

**Boundary.**
Do not import disk-filling or support-equals-spectrum conclusions from these more structured settings.
The companion random-matrix result concerns specified consecutive limits and assumptions, not arbitrary matrix-coefficient pencils.

### Proposition 7.5: resolvent equation with a strict spectral-radius condition

**Content.**
Bounded invertibility is equivalent to a finite matrix equation together with `r(Psi_g)<1`.
The condition selects the expected inverse and is equivalent to a positive solution of a strict Stein inequality.
The positive inverse-square moment is a convergent positive series.

**Worth connecting.**
[Alt--Kruger, deformed circular elements](#ak-deformed) has a closely related spectral-radius boundary in a commutative covariance setting.
The [Kronecker-matrix lead](#kronecker) connects the hermitized Dyson equation to spectral exclusion for structured random matrices.

**Recommendation.**
A comparison paragraph should identify the common stability mechanism: a positive-map spectral radius crosses one.
The manuscript treats the finite noncommutative coefficient algebra and retains `rho`; the closest deformed-circular comparison has zero pseudo-covariance and a commutative base.
The algebraic Dyson equation alone is not the statement being compared.
The Kronecker source remains a lower-priority discovery until its exact applicable result is inspected.

**Explicit overlap, calculated from the manuscript's maps.**
Assume `rho=0`.
If `a_0=diag(a_i)` and `eta(x)=diag(sum_j s_ij x_jj)`, then for `z` outside `spec(a_0)` the map in Corollary 7.6 has diagonal range, and its restriction to diagonal matrices is `D_(|a_i-z|^-2) S`, where `(S v)_i=sum_j s_ij v_j`.
It vanishes on matrices with zero diagonal, so its nonzero eigenvalues and spectral radius are exactly those of this restriction.
Thus the manuscript's spectral-radius test reduces to the familiar variance-profile test in this overlap.
The diagonal assumptions alone do not imply `rho=0`.
This elementary identification does not transfer the other paper's support or density theorem beyond its assumptions.

### Corollary 7.6: contour mass, exterior determinant and deterministic eigenvalue count

**Content.**
A contour in the resolvent set gives Brown mass by integrating the trace of the expected resolvent.
When `rho=0`, the exterior potential is the deterministic log determinant, the spectrum is described by a positive-map spectral radius, and enclosed mass is the normalized algebraic eigenvalue count of the constant matrix.

**Worth connecting.**
[HS09](#hs09), Introduction (1.3) and Theorem 1.1, links such contour calculations to Riesz idempotents and invariant spectral subspaces.
[Alt--Kruger, deformed circular elements](#ak-deformed) is useful specifically for the spectral-radius part.

**Recommendation.**
Emphasize that the contour integral computes a spectral-cluster mass.
The multiple-of-`1/m` conclusion here follows from the deterministic argument principle under `rho=0`; it is not an unconditional Brown-atom quantization theorem.
This distinction is especially important if [SS15](#ss15) is cited nearby.

### Lemma 7.7: positive matrix regularizer and inverse Hessian

**Content.**
An arbitrary positive coefficient-algebra regularizer preserves the variational representation.
The optimizer Hessian is positive definite, and its inverse is the conditional expectation of the two-sided resolvent map `k -> Q_D^{-1} k Q_D^{-1}`.

**Worth connecting.**
[Boyd--Vandenberghe](#bv) provides a general optimization perspective on partial minimization and Schur complements, which is useful for the next proposition.
The trace-log and resolvent differentiation in this lemma also belong to the standard sensitivity mechanism already visible in the manuscript's proof.

**Recommendation.**
No close external counterpart to the lemma's exact matrix-regularizer/inverse-Hessian identity was verified by the search.
Retain its self-contained proof.
If an optimization reference is included, use it for the general mechanism, without attributing this lemma to a convex-optimization theorem.
Positive Hessian at the optimizer does not establish global convexity of the manuscript's functional.

### Proposition 7.8: density through optimizer derivatives and Hessians

**Content.**
The envelope derivative recovers the regularized Cauchy transform.
The Laplacian is expressed through the Schur complement of the optimizer Hessian; the regularized density is strictly positive and converges weakly as a measure.

**Worth connecting.**
[Belinschi--Sniady--Speicher](#bss18) is the strongest immediate addition.
[Zhong](#zhong) and [BYZ](#byz) connect the positive resolvent expression and implicit differentiation to density formulas under free circular addition.
[Boyd--Vandenberghe](#bv) is optional methodological background.

**Recommendation.**
Present the Hessian formula as an expression for an already defined regularized density, and explain its relation to hermitization.
The other sources' nonzero circular covariance supplies regularization assumptions not present for arbitrary coefficients here.
Do not infer existence of a limiting planar density from positivity at every positive regularizer.

### Unnumbered linearized Dyson comparison after Proposition 7.8

**Content.**
A linearized Dyson equation recovers the same first and second potential derivatives as the optimizer method.
Neither finite-positive-regularizer calculation supplies a uniform inverse bound at zero regularizer.

**Worth connecting.**
Use [Belinschi--Sniady--Speicher](#bss18) for the hermitization/linearization computational framework.
[Alt--Kruger, deformed circular elements](#ak-deformed), Sections 5.3--5.4 and 6, connects the loss of stability to boundary and density analysis.

**Boundary.**
An equality between the two derivative calculations in the manuscript is stronger than a general statement that both are numerical approaches, but it does not compare their complexity or conditioning.
Those claims would require separate analysis.

### Section 7.6: selfadjoint and isotropic recoveries

**Content.**
Selfadjoint coefficients recover a one-dimensional spectral measure; isotropic covariance reduces the calculation to the earlier two-variable formula.

**Worth connecting.**
Existing [MS17](#ms17) and the manuscript's Bia97 reference are sufficient for the specific recoveries.
[SS15](#ss15) can supply broader algebraicity and atom context only if the discussion is expanded to polynomial spectral distributions.

**Recommendation.**
Do not add another citation merely for every recovery.
Preserve the distinction between a density on the real line and a density with respect to planar area.

### Section 7.6: scalar circular law and a circular-plus-zero block

**Content.**
The scalar minimization gives the uniform disk law, while a diagonal circular/zero block has half that law and half a point mass.

**Worth connecting.**
[HL00](#hl00) is a useful classical recovery reference.
[HS09](#hs09), Proposition 6.5, supplies the general invariant-block decomposition context.

**Recommendation.**
The short scalar calculation should remain, since it checks normalization and attainment.
The block example demonstrates the permitted degeneracy; it should not be used to justify scalar R-diagonality for all operator-valued circular elements.

### Section 7.6: deterministic point mass

**Content.**
The scalar Hessian expression becomes an explicit positive approximate point mass and checks signs, normalization and both real directions.

**Worth connecting.**
[Belinschi--Sniady--Speicher](#bss18), Section 2.1.6, supplies sufficient regularization context.
A separate external citation for the elementary polar integral is unnecessary.
Its main role is internal verification of Proposition 7.8.

## Source notes and verification boundaries

### MS17

James A. Mingo and Roland Speicher, *Free Probability and Random Matrices* (2017), [publisher DOI](https://doi.org/10.1007/978-1-4939-6942-5).
Already in the manuscript bibliography and repository.
Existing source interfaces and manuscript locators were checked: Chapter 11, Theorem 5, Definition 6, (11.6)--(11.8), and Section 9, (11.14)--(11.15).
These cover potential normalization, support inclusion and weak regularization.
No new whole-book reading was performed.
Keep as the basic exposition reference; the research sources below add connections rather than replace its conventions.

### AK20

Johannes Alt and Torben Kruger, *Inhomogeneous Circular Law for Correlated Matrices* (public preprint 2020; inspected v2, 2021), [arXiv v2](https://arxiv.org/abs/2005.13533v2).
Already in the manuscript and registry.
The existing [source note](../../../audits/literature/AK20/readme.md) was read, and the primary arXiv description was checked.
Theorem 2.5 and Proposition 2.9 relate matrix-coefficient free circular combinations to a radial Brown density.
Their two-sided flatness condition yields much stronger regularity and support information.
This search did not repeat the earlier statement/render inspection or audit their proofs.
High-value existing citation, appropriately retained after Proposition 7.4.

### DG24

Ken Dykema and John Griffin, *On operator valued Haar unitaries and bipolar decompositions of R-diagonal elements* (2024), [DOI](https://doi.org/10.1007/s00020-024-02760-z), [inspected preprint](https://arxiv.org/abs/2306.17133v2).
Already in the manuscript and registry.
The existing [source note](../../../audits/literature/DG24/readme.md) was read.
Theorem 2.9(b) is the alternating-cumulant characterization; Definition 2.10 specializes to circular elements.
Current use is already exact.
No full bipolar-decomposition proof or new source statement was reviewed in this search.

### HL00

Uffe Haagerup and Flemming Larsen, *Brown's Spectral Distribution Measure for R-Diagonal Elements in Finite von Neumann Algebras* (2000), [publisher](https://doi.org/10.1006/jfan.2000.3610), [author preprint](https://www.maphysto.dk/publications/MPS-RR/1999/27.pdf).
In the repository as HL00 and cited in the current manuscript.
The primary publisher abstract and institutional publication record were inspected.
The existing repository statement inspection locates Theorem 4.4 at printed p.13/PDF p.14 and Proposition 4.6 at printed pp.19--21.
These give the scalar R-diagonal radial law and support exceptions.
The current online theorem text/screenshot retrieval failed, so exact theorem details here retain that earlier inspection status.
High-value historical/mathematical comparison, conditional on scalar R-diagonality; no claim of direct applicability to arbitrary matrix-valued circular elements.

### ACSY24

Octavio Arizmendi, Guillaume Cebron, Roland Speicher and Sheng Yin, *Universality of free random variables: Atoms for non-commutative rational functions* (2024), [DOI](https://doi.org/10.1016/j.aim.2024.109595), [public preprint](https://arxiv.org/pdf/2107.11507).
Already in the repository under ACSY24 and cited in the current manuscript.
The public 60-page preprint's Section 2.1, printed p.10, was read directly: point-spectrum weights are bounded above by Brown atom weights, with possible strict inequality.
The introduction's non-star rational-function restriction was also checked.
The repository holds a differently paginated 73-page published version; no numbering equivalence was assumed.
This is a high-priority citation for the kernel/atom discussion, not an attribution of Proposition 7.2's full claim.

### SS15

Dimitri Shlyakhtenko and Paul Skoufranis, *Freely independent random variables with non-atomic distributions* (2015), [DOI](https://doi.org/10.1090/S0002-9947-2015-06434-4), [authors' institutional record](https://escholarship.org/uc/item/0cz0p5jw).
Registered as SS15, absent from the manuscript bibliography.
The primary institutional abstract and existing registry scope were inspected.
The work connects an Atiyah property to atom quantization and algebraicity for matricial polynomial spectral distributions.
No exact theorem establishing general nonnormal Brown-atom quantization was verified; the abstract must not be used for that extension.
Lower priority than ACSY24 for the present text.
Further exact-statement reading is needed before any stronger comparison is written.

### HS09

Uffe Haagerup and Hanne Schultz, *Invariant subspaces for operators in a general II1-factor* (2009), [published article](https://www.numdam.org/item/PMIHES_2009__109__19_0/), [published PDF](https://www.numdam.org/article/PMIHES_2009__109__19_0.pdf).
Registered as HS09 and cited in the current manuscript.
Directly read Theorem 1.1/7.1, Introduction (1.3), and Proposition 6.5, printed pp.20, 22, 69 and 76--77.
A spectral-subspace projection has trace equal to Brown mass; invariant block decompositions give weighted Brown measures.
These statements place the contour and block examples in a broader setting.
The source is stated for a II1 factor; extensions to arbitrary finite algebras were not investigated.
Original proofs were not audited.

### AK-deformed

Johannes Alt and Torben Kruger, *Brown measures of deformed L-infinity-valued circular elements* (2024 preprint; publisher listing 2026), [arXiv HTML v2](https://arxiv.org/html/2409.15405v2), [publisher page](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/brown-measures-of-deformed-linfty-valued-circular-elements/FD396FE006A07262F48D2D572B03E1EF).
Registered as AK26 and cited in the current manuscript.
Directly read Section 2, Assumptions A1--A2, Theorem 2.2, Proposition 5.16 and the Sections 5--6 outline.
A commutative base, block-primitivity and data regularity permit analytic density/support conclusions and a positive-operator spectral-radius boundary.
A2 is automatic for a finite base.
This is a high-priority comparison for deformed circular spectra and regularity, not a theorem for arbitrary noncommutative covariance maps.
The HTML has inconsistent displayed version/compilation dates; use its explicitly recorded locators here and resolve the exact artifact before manuscript intake.
Publisher metadata appeared in primary search results; its full-page retrieval failed.
No proof audit.

### AK-pseudo

Johannes Alt and Torben Kruger, *Spectrum occupies pseudospectrum for random matrices with diagonal deformation and variance profile* (2024 preprint), [arXiv v2](https://arxiv.org/html/2404.17573v2).
Absent from the manuscript and not found in the scoped registry search.
Directly read Theorems 2.1 and 2.4, Remark 2.5 and Definition 3.2.
The model has independent centered entries, deterministic diagonal deformation and specified profile regularity/nondegeneracy; its limiting density is identified with a deformed operator-valued circular Brown measure.
Theorem 2.4 compares asymptotic pseudospectra with the support through consecutive limits.
Useful as indirect random-matrix motivation after the spectral criterion.
No local law, finite-size rate, or theorem applicability to arbitrary coefficient maps is adopted.

### BSS18

Serban T. Belinschi, Piotr Sniady and Roland Speicher, *Eigenvalues of non-Hermitian random matrices and Brown measure of non-normal operators: Hermitian reduction and linearization method* (2018), [publisher](https://doi.org/10.1016/j.laa.2017.09.024), [public preprint](https://arxiv.org/pdf/1506.02017).
Cited in the current manuscript as BSS18; the repository key BSS17 denotes an unrelated two-projection paper and must not be reused.
Directly read Sections 2.1.5--2.1.6, (7)--(11), preprint pp.6--8, and the primary publisher abstract.
The regularized Cauchy transform, positivity of regularized Brown measures and weak convergence are direct background for Proposition 7.8.
Hermitization, subordination and linearization provide the computational comparison.
The manuscript's additional representation uses its own variational optimizer and Hessian.
No general random-matrix eigenvalue-convergence theorem is inferred from convergence of star moments.
High-priority addition.

### Zhong

Ping Zhong, *Brown measure of the sum of an elliptic operator and a free random variable in a finite von Neumann algebra* (2021 preprint; inspected arXiv v5, 2025), [version record](https://arxiv.org/abs/2108.09844), [PDF](https://arxiv.org/pdf/2108.09844v5).
Registered as Zho26 and cited in the current manuscript.
Directly read Theorem 4.2 and its proof, printed pp.28--30.
For scalar free circular addition it gives a density in the positive subordination region, with a positive two-resolvent term and an implicit-derivative term.
This is a useful methodological comparison to Proposition 7.8, under different structural assumptions.
The source's Theorem 4.3 cites the stronger global bound from BYZ; cite that original source for the bound.
Publication identity beyond the inspected preprint was not fully reconciled.

### BYZ

Serban Belinschi, Zhi Yin and Ping Zhong, *The Brown measure of a sum of two free random variables, one of which is triangular elliptic* (2022 preprint; inspected final arXiv revision, 2024), [arXiv](https://arxiv.org/abs/2209.11823), [PDF](https://arxiv.org/pdf/2209.11823).
Registered as BYZ24 and cited in the current manuscript.
Directly read Theorem 7.10, Lemma 7.11 and the associated limiting argument, preprint pp.42--45.
Under free circular addition, regularized densities have a uniform bound `1/(pi t)`, which yields global absolute continuity of the limiting measure.
This is the clearest comparison for the missing uniform control in a general positive-regularizer formula.
The broader paper treats triangular elliptic operators and unbounded deformations; only the circular subsection was inspected.
The current manuscript must separately verify scalar freeness before invoking that specialization.

### BV

Stephen Boyd and Lieven Vandenberghe, *Convex Optimization* (2004), [authors' book page](https://web.stanford.edu/~boyd/cvxbook/), [authors' slides](https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf).
Registered as BV04 and cited in the current manuscript.
The slide on partial minimization, PDF p.67, was directly inspected: eliminating a quadratic variable produces a Schur complement.
The initial book-PDF retrieval failed; the coordinating reader subsequently obtained the [author-hosted UCLA copy](https://www.seas.ucla.edu/~vandenbe/cvxbook/bv_cvxbook.pdf) and read Appendix A.5.5, printed pp.650--651, as recorded in [the min--max analysis](minmax.md).
This is indirect conceptual background for (7.27), not verification of the exact nonlinear optimizer Hessian formula, and not evidence that the manuscript functional is jointly convex.
Low-priority optional citation; the current proof is already short and self-contained.

### Kronecker

Johannes Alt, Laszlo Erdos, Torben Kruger and Yuriy Nemish, *Location of the spectrum of Kronecker random matrices* (2019), [arXiv](https://arxiv.org/abs/1706.08343), [institutional publication record](https://research-explorer.ista.ac.at/record/6240), [DOI](https://doi.org/10.1214/18-AIHP894).
Absent from the manuscript and not found in the scoped registry search.
Only the primary abstract/record was obtained; PDF retrieval did not provide readable theorem text.
It is a plausible connection between structured block matrices, the matrix Dyson equation and spectral exclusion.
Record as a lead requiring exact-theorem inspection, not a ready citation for Proposition 7.5's equivalence.
No specific result number is adopted from search snippets.

## Original editorial priorities

1. Add the precise kernel-versus-Brown-atom comparison from ACSY24 near (7.11).
2. Add Belinschi--Sniady--Speicher near the regularized density and linearized-Dyson discussion.
3. Add a short scalar R-diagonal comparison with HL00 beside the radial result, after checking the exact retained version on intake.
4. Compare the affine circular spectral-radius criterion with Alt--Kruger's deformed circular work, explicitly restricting the comparison to the commutative-base overlap.
5. Use HS09 if the contour formula is given an interpretation in terms of spectral subspaces; this provides more insight than an isolated argument-principle citation.
6. Compare the limiting-density issue with BYZ, with Zhong as an optional complementary formula/method reference.

AK20, DG24 and MS17 already serve useful roles.
BV and the Kronecker lead should not be added just to enlarge the bibliography.
SS15 becomes worthwhile only if the manuscript deliberately develops the rank/algebraicity comparison.

## Search limit

No exhaustive citation-network search or priority claim is made.
The assessment stopped once the principal conceptual connections had exact source locators or an explicit lower verification level; unavailable theorem text remains a reading task rather than a silently accepted result.

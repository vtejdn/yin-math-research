---
author: Yin
---

# F0012 Citation Applications

The map follows the current paper sources, with the bibliographic fields in the [canonical bibliography](../../literature/references.bib).
The [whole-chain review for F0012 v2](../../audits/reviews/Yin_R_F0190_v3.md#source-inspection-and-acceptance-boundary) checks the selected primary statements and the strengthened applications.
Its coverage of external proof inputs is at statement level, while its checks of the project argument include the local adaptations.

## `BSS18`

In `paper/sections/introduction.tex`, the paragraph beginning “Belinschi, Śniady and Speicher” cites the unnumbered Conjecture in Section 7, arXiv:1506.02017v3, printed/PDF p. 34.
The scalar polynomial in Theorem `thm:brown`, including a non-self-adjoint one, and its independent normalized GUE inputs belong to the source's self-adjoint Gaussian-to-free-semicircular setting.
The citation attributes the question; it supplies no convergence proof and does not attribute an almost-sure formulation to the source.
The source's \(\mu_A\) denotes a mean empirical measure, and Section 7 does not specify almost-sure or in-probability convergence; Theorem `thm:brown` proves almost-sure weak convergence of the random empirical measures in the GUE case.
See the [source-level passage, ensemble scope and measure-notation inspection](../../audits/literature/BSS18/readme.md#polynomial-eigenvalue-question).

## `CGP22`

In `paper/sections/introduction.tex`, the paragraph following the model conventions cites pp. 1–2 of arXiv:1912.04588v1 for normalized trace-moment convergence to free variance-one semicircular elements and convergence of the maximum input norm to two.
In `paper/sections/brown.tex`, subsection `subsec:potentials` uses the same pages for those moments and the operator norm bound on the GUE inputs.
The source's unnormalized trace in the density and normalized trace in the moments agree with the paper's \(\operatorname{Tr}\) and \(\operatorname{tr}_N\).
The input norm limit gives a fixed cutoff in the scalar probability argument, and polynomial approximation on the resulting common compact interval yields the squared singular-value law convergence.

In `paper/sections/brown.tex`, `eq:resolvent` uses Corollary 1.3 of arXiv:1912.04588v1, printed p. 5, at amplification size one with no additional deterministic inputs.
At fixed \(z\), the polynomial \(Q_z=(P-z)^*(P-z)\) has scalar coefficients and is self-adjoint in the self-adjoint input indeterminates.
The source's Stieltjes transform uses the same \((w-x)^{-1}\) convention, and the manuscript uses its bound in the upper half-plane.
In `paper/sections/affine.tex`, subsection `subsec:affine-counting` uses the same corollary with fixed amplification size \(m\) and deterministic coefficient matrices and their adjoints.
Interchanging the tensor factors gives the comparison under \(\operatorname{tr}_m\otimes\tau\).
The source's factor \(m^2\) and coefficient norms enter the constant, while the \(N^{-2}\) scale is retained.
See the [scalar application](../../claims/Yin_C_F0186_v1.md#polynomial-application) and the [matrix-valued application](../../claims/Yin_C_F0186_v2.md#logarithmic-tail).

In `paper/sections/probability.tex`, `eq:gaussian-concentration` uses Proposition 4.4, p. 30, with the independent real standard Gaussian coordinates described on p. 31.
The manuscript applies the one-sided bound to both signs to get the two-sided form for normalized singular-value averages.
Proposition 2.11, p. 10, supplies a one-matrix tail with constants independent of \(N\ge1\).
Integration gives the displayed uniform first-moment bound \(M_0=C_{\mathrm{op}}+c_{\mathrm{op}}^{-1}\).
The stronger quadratic norm tail in `eq:norm-tail` follows from the concentration inequality and the \(N^{-1/2}\) coordinate scaling.
See the [norm and concentration inputs](../../claims/Yin_C_F0186_v3.md#inputs) and the [independent source check](../../audits/reviews/Yin_R_F0190_v3.md#source-inspection-and-acceptance-boundary).

## `DM17`

In `paper/sections/affine.tex`, subsection `subsec:generic-invertibility` uses Definitions 2.1–2.2 and Proposition 2.3 of the published edition, journal p. 49 / PDF p. 6.
Over the infinite field \(\mathbb C\), the **maximum** rank of the square tensor blow-up is divisible by its size \(N\).
The paper proves the reduction to the affine maximum and the transfer to the Hermitian coordinates.
See the [edition and inspection note](../../audits/literature/DM17/readme.md) and the [retained rank argument](../../claims/Yin_C_F0186_v2.md#generic-rank).

## `Han26`

In `paper/sections/introduction.tex`, the Ginibre comparison cites Theorem 1.2, arXiv:2606.01664v1, pp. 2–3, for weak convergence in probability for fixed scalar polynomials in independent complex Ginibre matrices, with free circular limits.
Question 1.8 on p. 6 addresses the use of adjoints that occurs when a general GUE polynomial is expressed in paired Ginibre coordinates.
Both citations delimit the earlier result's input class and give context for the GUE theorem.
See the [source theorem and normalization](../../audits/literature/Han26/Yin_U001.md#statements) and the [GUE interface](../../audits/literature/Han26/Yin_U001.md#gue-boundary).

In the proof outline in `paper/sections/introduction.tex`, Section 5, pp. 32–34, supplies the hermitization and logarithmic truncation scheme, including the squared-singular-value normalization in (5.1).
The source writes the products in the opposite adjoint order, which gives the same squared-singular-value laws in finite dimension and the same limiting laws under the trace.
The manuscript establishes the required GUE pencil bound and logarithmic tail before passing to the planar Laplacian.
See the [logarithmic cutoff inspection](../../audits/literature/Han26/Yin_U001.md#hermitization).

In `paper/sections/brown.tex`, subsection `subsec:linearization` compares the affine Schur complement with Section 2.2, p. 10 and following.
Both constructions use a root block and upper triangular chains, with an invertible constant matrix for the full pencil when \(z\ne P(0)\).
The manuscript derives its own chain for each word in place of the source's coefficient-tensor factorization by homogeneous degree.
See the [source linearization inspection](../../audits/literature/Han26/Yin_U001.md#linearization).

## `KSS16`

In `paper/sections/geometry.tex`, Proposition `prop:distance` invokes (KS2), arXiv:1412.5088v1, printed p. 2.
The input is the polynomial-map inequality on all of \(\mathbb R^p\), with a nonempty zero set in the use here.
The compressed real-coordinate map has degree two, and its domain dimension depends only on the fixed coefficient size and the two compression dimensions.
The bounded-norm proposition absorbs the source's denominator and excludes empty zero sets by compactness.
In `paper/sections/affine.tex`, subsection `subsec:global-floor` retains the denominator's growth as the norm cutoff varies and applies the same polynomial-map inequality to the degree-at-most-three map with nonempty zero set obtained by adjoining one coordinate.
See the [moving-cutoff argument](../../claims/Yin_C_F0186_v3.md#global-repair-growth).
The 2019 correction affects other semialgebraic-map statements, leaving this polynomial-map input intact.
See the [error-bound argument](../../claims/Yin_C_F0186_v1.md#error-bound) and [source and correction review](../../audits/reviews/Yin_R_F0190_v1.md#primary-sources-and-acceptance-boundary).

## `Lot15`

In `paper/sections/probability.tex`, Lemma `lem:gaussian-tube` invokes Theorem 1.1, arXiv:1210.3742v4, printed p. 1.
A nonempty regular level of a real polynomial of degree at most \(D\) is a smooth complete intersection of codimension one, so the source's bound for a uniformly sampled point in an arbitrary Euclidean ball applies with \(s=1\) and source tube radius \(\varepsilon=\rho\).
The approximation by regular levels, Gaussian mixture and inverse-radius moment estimate are derived in the manuscript.
See the [Gaussian averaging argument](../../claims/Yin_C_F0186_v3.md#tube-without-floor).
See the [tube argument](../../claims/Yin_C_F0186_v1.md#tubes) and [review of the extension](../../audits/reviews/Yin_R_F0190_v1.md#tubes-and-the-gaussian-estimate).

## `Mec19`

In `paper/sections/affine.tex`, subsection `subsec:affine-counting` uses Corollary 4.39, printed/PDF p. 47 of the author-hosted notes dated 27 April 2019.
The matrices are square and complex, and the Euclidean norm on ordered singular values corresponds to the Frobenius norm on the matrices.
Cauchy–Schwarz with the normalized singular-value average gives the dimension factor used in Gaussian concentration.
See the [edition and inspection note](../../audits/literature/Mec19/readme.md) and the [Frobenius specialization](../../claims/Yin_C_F0186_v3.md#singular-value-perturbation).

## `MS17`

In `paper/sections/introduction.tex`, Definition `def:brown-measure` and its surrounding discussion use the first edition, Chapter 11, Theorem 5 and Definition 6, printed p. 268 / PDF p. 276, and the normal specialization on printed p. 270 / PDF p. 278.
For a bounded element in a finite von Neumann algebra with faithful normal tracial state, the source identifies \(\log\Delta(a-z)\) with \(\tau(\log|a-z|)\).
Theorem 5 yields a locally integrable potential by subharmonicity, identifies its \(1/(2\pi)\)-scaled distributional Laplacian as the Brown probability measure, and states the support inclusion and logarithmic-potential representation in (11.6)–(11.7).
The normal specialization is used in the introductory comparison with spectral measures.
See the [monograph passage inspection](../../audits/literature/MS17/Yin_U001.md#ms17-u001) and the [registered Brown-measure convention](../../definitions/index.md#brown-measure).

## `MS24`

In `paper/sections/introduction.tex`, Definition `def:fk-determinant` preceding Theorem `thm:affine` uses arXiv:2406.15922v1, Definition 2.1(ii), Remark 2.2(i) and Proposition 2.3(vi), printed/PDF pp. 5–6.
The logarithmic spectral integral includes the zero atom, and the free pencil uses the normalized matrix trace tensored with the tracial state.
The finite-dimensional formula gives the \(1/(mN)\) power of the absolute determinant in the chosen notation.
See the [checked determinant convention](../../audits/literature/MS24/Yin_U001.md#determinant-convention).

## `NS06`

In `paper/sections/introduction.tex`, the opening model setup recalls the free semicircular convention from Definition 2.16 and Remark 2.17(2), printed p. 29 / PDF p. 46, and Definition 5.3, printed pp. 64–65 / PDF pp. 81–82, of the 434-page publisher edition.
The source's semicircle radius is two for the manuscript's variance one, and its linear functional is the manuscript's trace on the unital algebras generated by the individual semicircular elements.
Freeness uses centered elements and distinct consecutive algebras.
See the [semicircular definition](../../audits/literature/NS06/Yin_U002.md#semicircular), the [freeness definition](../../audits/literature/NS06/Yin_U002.md#free-independence) and the [registered model conventions](../../definitions/index.md#probability-and-models).

## `Sar42`

In `paper/sections/probability.tex`, the proof of Lemma `lem:gaussian-tube` invokes Theorems 4.1 and 7.2 of the 1942 journal edition, printed pp. 885 and 889 / PDF pp. 3 and 7, to choose a positive regular value below all the finitely chosen positive endpoint values.
The real polynomial \(q:\mathbb R^n\to\mathbb R\) is \(C^\infty\); Theorem 4.1 covers \(n=1\), and Theorem 7.2 applies for \(n>1\) with source domain dimension \(n\), target dimension one and differentiability order \(n\).
The critical values are Lebesgue-null, so they cannot fill the positive interval bounded by the minimum endpoint value.
The manuscript's separate segment argument ensures that the chosen level is nonempty and approximates the relevant zeros.
The citation supports the regular-value choice; the tube inequality and Gaussian averaging remain the local argument.
See the [source statements, scalar convention, direct specialization and inspection limits](../../audits/literature/Sar42/Yin_U001.md#sar42-u001).
The source proofs were not audited.

## `SS15`

In `paper/sections/brown.tex`, subsection `subsec:log-tail` invokes Theorem 1.1(5)–(6), arXiv:1305.1920v1, printed p. 2, for local convergent fractional-power expansions of the Cauchy transform, and Corollary 1.2, printed p. 3, for atomlessness.
The coefficient amplification size is one, the arguments are freely independent semicircular elements, and the paper checks that the positive self-adjoint polynomial \(Q_z\) is nonconstant.
The source expansion agrees with the Cauchy transform on the upper half-plane near zero.
The manuscript excludes powers below \(-1\) and uses the zero-atom limit of \(\mathrm{i}tG(\mathrm{i}t)\) to eliminate order \(-1\).
In `paper/sections/affine.tex`, subsection `subsec:affine-counting` uses Theorem 1.1(5)–(6) in its matrix-valued form.
There the finiteness of the free logarithm supplies the zero-atom exclusion needed for the same power estimate.
The matrix-valued application does not use scalar atomlessness.
See the [affine source interface](../../claims/Yin_C_F0186_v2.md#logarithmic-tail).
The resulting quantitative bound on the mass near zero is a local deduction.
See the [review of the primary statements](../../audits/reviews/Yin_R_F0190_v1.md#primary-sources-and-acceptance-boundary) and [review of their application](../../audits/reviews/Yin_R_F0190_v1.md#linearization-and-logarithmic-tails).

---
author: Yin
---

# F0012 Citation Applications

The map follows the current paper sources, with the bibliographic fields in the [canonical bibliography](../../literature/references.bib).
The [whole-chain source review](../../audits/reviews/Yin_R_F0190_v1.md#primary-sources-and-acceptance-boundary) checks selected primary statements and their applicability to F0012.
Its coverage of external proof inputs is at statement level, while its checks of the project argument include the local adaptations.

## `BSS18`

In `paper/sections/introduction.tex`, the paragraph beginning “Belinschi, Śniady and Speicher” cites Section 7, arXiv:1506.02017v3, printed p. 34.
The conjecture there concerns the eigenvalue laws of scalar polynomials, including non-self-adjoint ones, in independent self-adjoint Gaussian or Wigner matrices with free semicircular limits.
The citation attributes the question, and Theorem `thm:brown` treats its normalized GUE specialization.
See the [primary passage](https://arxiv.org/html/1506.02017v3#S7) and the [Task's starting references](../../tasks/Yin_T_F0012_v1.md#contract).

## `CGP22`

In `paper/sections/introduction.tex`, the paragraph following the model conventions cites pp. 1–2 of arXiv:1912.04588v1 for normalized trace-moment convergence to free variance-one semicircular elements and convergence of the maximum input norm to two.
In `paper/sections/brown.tex`, subsection `subsec:potentials` uses the same pages for those moments and the operator norm bound on the GUE inputs.
The source's unnormalized trace in the density and normalized trace in the moments agree with the paper's \(\operatorname{Tr}\) and \(\operatorname{tr}_N\).
The input norm limit of two gives the fixed norm cutoff, and polynomial approximation on the resulting common compact interval yields the squared singular-value law convergence used here.

In `paper/sections/brown.tex`, `eq:resolvent` uses Corollary 1.3 of arXiv:1912.04588v1, printed p. 5, at amplification size one with no additional deterministic inputs.
At fixed \(z\), the polynomial \(Q_z=(P-z)^*(P-z)\) has scalar coefficients and is self-adjoint in the self-adjoint input indeterminates.
The source's Stieltjes transform uses the same \((w-x)^{-1}\) convention, and the manuscript uses its bound in the upper half-plane.
See the [source review](../../audits/reviews/Yin_R_F0190_v1.md#primary-sources-and-acceptance-boundary) and the [polynomial application](../../claims/Yin_C_F0186_v1.md#polynomial-application).

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
The bound on the coordinate norm absorbs the source's denominator, and compactness handles a map with empty zero set.
The 2019 correction affects other semialgebraic-map statements, leaving this polynomial-map input intact.
See the [error-bound argument](../../claims/Yin_C_F0186_v1.md#error-bound) and [source and correction review](../../audits/reviews/Yin_R_F0190_v1.md#primary-sources-and-acceptance-boundary).

## `Lot15`

In `paper/sections/probability.tex`, Lemma `lem:gaussian-tube` invokes Theorem 1.1, arXiv:1210.3742v4, printed p. 1.
A nonempty regular level of a real polynomial of degree at most \(D\) is a smooth complete intersection of codimension one, so the source's bound for a uniformly sampled point in an arbitrary Euclidean ball applies with \(s=1\) and source tube radius \(\varepsilon=\rho\).
The approximation of the original zero set by regular levels and the Gaussian mixture of uniform balls are derived in the manuscript.
See the [tube argument](../../claims/Yin_C_F0186_v1.md#tubes) and [review of the extension](../../audits/reviews/Yin_R_F0190_v1.md#tubes-and-the-gaussian-estimate).

## `MS17`

In `paper/sections/introduction.tex`, Definition `def:brown-measure` and its surrounding discussion use the first edition, Chapter 11, Theorem 5 and Definition 6, printed p. 268 / PDF p. 276, and the normal specialization on printed p. 270 / PDF p. 278.
For a bounded element in a finite von Neumann algebra with faithful normal tracial state, the source identifies \(\log\Delta(a-z)\) with \(\tau(\log|a-z|)\).
Theorem 5 yields a locally integrable potential by subharmonicity, identifies its \(1/(2\pi)\)-scaled distributional Laplacian as the Brown probability measure, and states the support inclusion and logarithmic-potential representation in (11.6)–(11.7).
The normal specialization is used in the introductory comparison with spectral measures.
See the [monograph passage inspection](../../audits/literature/MS17/Yin_U001.md#ms17-u001) and the [registered Brown-measure convention](../../definitions/index.md#brown-measure).

## `NS06`

In `paper/sections/introduction.tex`, the opening model setup recalls the free semicircular convention from Definition 2.16 and Remark 2.17(2), printed p. 29 / PDF p. 46, and Definition 5.3, printed pp. 64–65 / PDF pp. 81–82, of the 434-page publisher edition.
The source's semicircle radius is two for the manuscript's variance one, and its linear functional is the manuscript's trace on the unital algebras generated by the individual semicircular elements.
Freeness uses centered elements and distinct consecutive algebras.
See the [semicircular definition](../../audits/literature/NS06/Yin_U002.md#semicircular), the [freeness definition](../../audits/literature/NS06/Yin_U002.md#free-independence) and the [registered model conventions](../../definitions/index.md#probability-and-models).

## `SS15`

In `paper/sections/brown.tex`, subsection `subsec:log-tail` invokes Theorem 1.1(5)–(6), arXiv:1305.1920v1, printed p. 2, for local convergent fractional-power expansions of the Cauchy transform, and Corollary 1.2, printed p. 3, for atomlessness.
The coefficient amplification size is one, the arguments are freely independent semicircular elements, and the paper checks that the positive self-adjoint polynomial \(Q_z\) is nonconstant.
The source expansion agrees with the Cauchy transform on the upper half-plane near zero.
The manuscript excludes powers below \(-1\) and uses atomlessness to control the imaginary part at order \(-1\) on the positive imaginary axis.
The resulting quantitative bound on the mass near zero is a local deduction.
See the [review of the primary statements](../../audits/reviews/Yin_R_F0190_v1.md#primary-sources-and-acceptance-boundary) and [review of their application](../../audits/reviews/Yin_R_F0190_v1.md#linearization-and-logarithmic-tails).

---
author: Yin
---

# Related literature for the general formula and its proof

This is a manuscript-specific analysis of optional contextual citations, read on 2026-10-10.
It covers Definitions 1.1 and 1.2, Theorem 1.3, Definition 2.1, and the unnumbered arguments in Sections 2 and 3 of the current [introduction](../paper/sections/introduction.tex), [preliminaries](../paper/sections/dyson.tex), and [main proof](../paper/sections/main-proof.tex).
The comparison formulas and Brown-measure applications have separate analyses.

The purpose is to identify connections that help explain the work, including connections that are not proof dependencies.
The candidates are contextual comparisons, not new external theorem premises.
Existing source audits are reused at their recorded scope.
New readings are identified below; they are not whole-paper audits or novelty searches.

## Analysis in manuscript order

| Manuscript content | Connection worth explaining | Candidate and suggested placement | Mathematical boundary |
| --- | --- | --- | --- |
| Definition 1.1: determinant and capacity | Capacity puts a determinant problem into the setting of operator scaling, rank non-decrease, and noncommutative rank. This explains why the completely positive coefficient map is useful beyond calculating a scalar quantity. | The existing Gur04 citation can be made more informative with one short paragraph near the centered identity. GGOW20 is a strong optional additional reference for the noncommutative-rank connection; see the source descriptions below. | Rank non-decrease and positive capacity do not mean a bounded inverse exists after evaluating the pencil in semicircular operators. Arithmetic input restrictions matter for computational complexity statements. |
| Definition 1.2: affine pencil, and the phase obstruction immediately after it | The distinction between the covariance map and the additional map recording coefficients without adjoints explains why arbitrary affine pencils require more information than centered determinants. | Existing MS24, Theorem 1.2 and Lemma 3.5(ii), already provide the most direct reference. The full block covariance in Section 2.3 makes the connection explicit. | The displayed scalar counterexample is self-contained. No extra reference is needed merely to cite its elementary inequalities. The centered theorem should not be described as determining the noncentered determinant from the covariance alone. |
| Theorem 1.3: the determinant formula | The zero-constant-term specialization gives exactly the MS24 determinant-capacity identity. The added constant term also connects the problem to deterministic equivalents of logarithmic determinants of noncentered random matrices. | Retain MS24 as the direct mathematical predecessor. Consider restoring HLN07 as one paragraph of related work after the principal theorem or at the end of Section 2.2. | HLN07 evaluates an expression at a solution of deterministic resolvent equations. It does not assert the present infimum over arbitrary positive matrix trials, and its asymptotic random-matrix assumptions are different. |
| Theorem 1.3: attainment and the unique minimizer | There are two useful comparisons: capacity minimizers describe exact operator scaling; the manuscript's minimizer describes a bounded inverse. This distinction makes the spectral meaning of the new variational parameter clear. | Gur04, Theorem 4.7, is appropriate for a concise comparison immediately after the centered reduction, if this distinction is developed there. | These are different minimization problems. For the scalar centered example with covariance equal to the identity, homogeneous capacity is attained on the determinant-one slice, whereas the manuscript's quotient is \((1+b)/b\) and reaches its infimum only as \(b\to\infty\). |
| The reduction to capacity, equation (1.11) | The homogeneous logarithmic capacity function has a geodesically convex optimization theory on positive definite matrices. | Allen-Zhu, Garg, Li, Oliveira and Wigderson (2018), Section 1.1, is a useful optional reference after the centered reduction. | A theory for \(\log\det\eta(b)-\log\det b\) does not automatically establish convexity or an algorithmic complexity bound for the full affine function \(\mathcal V\). |
| Definition 2.1 and Section 2.1: the matrix Cauchy transform, Dyson equation and uniqueness | The half-plane condition is the established mechanism for selecting the resolvent solution among algebraic solutions. There is also a convergent fixed-point iteration in the operator-valued literature. | Helton, Rashidi Far and Speicher (2007), Theorem 2.1 and Sections 1–3, is the strongest addition. Place it next to the uniqueness discussion; retain the manuscript's short proof. Ajanki, Erdős and Krüger (2019), Section 2.1, connects the same equation to correlated random matrices. | With the manuscript convention, the positive-imaginary-part MDE solution is \(M=-G\). The published iteration uses a different contraction argument from the manuscript's row/column estimate. No convergence of an arbitrary proposed iteration follows. |
| Section 2.2: integrating the Cauchy transform | Recovering a logarithmic determinant by integrating a resolvent, and simplifying it to finite log-determinants plus a covariance correction, also appears in information theory and deterministic-equivalent calculations. | HLN07, Section 4 and Theorem 4.1, equation (4.3), is a particularly useful method comparison after equation (2.4). | This identifies a related calculation, not equality of the two variational formulas. The source's communication-theoretic quantity must not be confused with the operator-scaling capacity of Definition 1.1. |
| Section 2.3: hermitization and regularization | The same two-by-two block construction brings a nonselfadjoint problem into operator-valued semicircular theory. Regularization makes logarithmic determinants accessible through resolvents. | MS24, Section 3, and MS17, Chapter 11, Section 9, already cover the exact construction. HLN07 supplies additional context for the regularized logarithmic functional if desired. | No new source is recommended just to duplicate the existing hermitization references. The singular zero-regularizer limit requires the manuscript's own monotone spectral argument. |
| Section 2.4: the positive-map estimate and Neumann series | A strict positive defect \(W-\Psi(W)>0\) is a certificate of similarity to a strict contraction and of spectral radius below one. This is an operator-theoretic version of a discrete Lyapunov/Stein criterion. | Popescu (2003), Lemma 5.5 and Theorem 5.9, supplies an exact external connection. A brief reference at the start or end of this paragraph is sufficient. | Complete positivity is sufficient; the source's result is formulated even for positive maps. Finite-dimensional maps satisfy its normality requirement automatically. The strict defect is essential to the stated spectral-radius conclusion. |
| Section 2.4: Stieltjes inversion and the spectral-gap test | This gives the passage from an analytic matrix equation to the actual spectral support. | Existing MS17 is adequate for inversion. Ajanki–Erdős–Krüger, Proposition 2.1, provides a related matrix-valued Stieltjes representation. | Keep the distinction between analytic continuation of the selected Cauchy transform and an arbitrary selfadjoint algebraic solution. No new citation is needed for the elementary kernel proof retained here. |
| Section 3.1: coercive regularization and elimination of \(Y\) | This is a real quadratic maximization followed by a coercive positive-matrix minimization. | No separate new contextual citation is recommended for completing the square or the elementary coercivity estimate. | Adding a reference here would contribute less than explaining why regularization produces an attained minimum. No general geodesic convexity assertion has been checked for this function. |
| Section 3.2: every critical point is the resolvent solution | The proof joins two established mechanisms: positive-map stability forces the sign of a block, and half-plane uniqueness identifies that block with a resolvent. | Refer back to the Popescu and Helton–Rashidi Far–Speicher connections in Sections 2.4 and 2.1. | The critical-point equations, their signed Schur-complement construction and the identification of the particular optimizer are the manuscript's argument; neither reference by itself supplies those deductions. |
| Section 3.3: the minimum value and removal of regularization | The resolvent primitive is related to HLN07, while the passage from attained regularized minima to an unregularized infimum explains the global variational assertion. | One HLN07 citation in Section 2.2 is enough; avoid repeating it through the calculation. | An equation-evaluated formula is not already a global minimum formula. The fixed-trial upper bound and monotone limit are the relevant additional steps. |
| Section 3.4: critical point implies a spectral gap | The full block identity \(D-\mathcal S(D)=G_0^2>0\) is a strict positive-map stability certificate. Invertibility of the linearized Dyson equation then allows analytic continuation. | Popescu, Theorem 5.9, is the direct operator-theoretic connection. Ajanki–Erdős–Krüger, Section 4 and Theorem 2.6, provide broader MDE stability context. | The latter's quantitative theorem assumes flatness and decay conditions not imposed here. It is related methodology, not a direct theorem application proving this manuscript's arbitrary-covariance spectral-gap conclusion. |
| Section 3.5: invertibility implies attainment and uniqueness | The optimizer is a conditional expectation of an inverse square, obtained as a norm limit in a spectral gap. The uniqueness conclusion comes from identifying the analytic resolvent and its derivative. | The two earlier connections already supply sufficient context. No extra citation is recommended just for continuity of inversion. | Keep the manuscript's proof visible. Neither capacity attainment nor a general abstract optimization statement supplies this optimizer formula. |

## Sources and actual reading depth

### Existing determinant and capacity sources

**Tobias Mai and Roland Speicher, _Fuglede–Kadison determinants of matrix-valued semicircular elements and capacity estimates_ (2024), [arXiv:2406.15922v1](https://arxiv.org/abs/2406.15922v1).**
Already in the manuscript as MS24.
Theorem 1.2 is the exact centered determinant identity; Lemma 3.5(ii) provides the block covariance.
This analysis reused the [existing MS24 audit](../../../../audits/literature/MS24/readme.md), checked the current manuscript's specialization and opened the public abstract.
It did not rerun the source proof audit.
Retain the existing citation; use it to explain the precise recovery rather than adding a second broad historical paragraph.

**Leonid Gurvits, _Classical complexity and quantum entanglement_ (2004), [publisher DOI](https://doi.org/10.1016/j.jcss.2004.06.003).**
Already in the manuscript as Gur04.
Definitions 4.2/4.4 and Theorems 4.6/4.7 relate capacity to approximate and exact scaling.
Reused the [source audit](../../../../audits/literature/Gur04/readme.md), and read its [exact-scaling unit](../../../../audits/literature/Gur04/Yin_U003.md), including the recorded normalizer and scalar-zero qualifications.
No new whole-source review occurred.
Its main optional value is explaining what homogeneous capacity attainment means, before contrasting it with bounded invertibility in Theorem 1.3.

**Ankit Garg, Leonid Gurvits, Rafael Oliveira and Avi Wigderson, _Operator Scaling: Theory and Applications_ (2020), [published author PDF](https://www.math.ias.edu/~avi/PUBLICATIONS/GargGOW20.pdf).**
Canonical repository key GGOW20 and cited in the current manuscript.
Theorem 1.4 and Sections 1.1–1.3 give the noncommutative-rank context.
Reused the [full-version source audit](../../../../audits/literature/GGOW20/readme.md), including its distinction between exact scaling, approximate scaling and analytic invertibility.
No new source-proof review occurred.
This is a strong optional introduction reference; detailed algorithmic claims would need the precise encoding and precision assumptions.

### Capacity and geodesic optimization

**Zeyuan Allen-Zhu, Ankit Garg, Yuanzhi Li, Rafael Oliveira and Avi Wigderson, _Operator Scaling via Geodesically Convex Optimization, Invariant Theory and Polynomial Identity Testing_ (2018), [arXiv:1804.01076v1](https://arxiv.org/abs/1804.01076v1).**
Registered as AZGL+18 and cited in the current manuscript.
The arXiv record and PDF introduction, Sections 1.1–1.2.1, were read.
Section 1.1, equation (1.1), explicitly considers \(\log\det T(X)-\log\det X\) on the positive cone; its Theorem M1 is labeled informal.
The algorithmic proofs were not checked.
This is a direct contextual connection for the homogeneous capacity function, and an indirect optimization comparison for the affine problem.
Do not cite its high-accuracy algorithm as an algorithm for the manuscript's full function without a separate reduction.

### Half-plane uniqueness and matrix Dyson stability

**J. William Helton, Reza Rashidi Far and Roland Speicher, _Operator-valued Semicircular Elements: Solving a Quadratic Matrix Equation with Positivity Constraints_ (2007), IMRN, Article rnm086, [published author-hosted PDF](https://mathweb.ucsd.edu/~helton/BILLSPAPERSscanned/HRS07.pdf), [arXiv record](https://arxiv.org/abs/math/0703510).**
Registered and cited in the current manuscript as HRFS07.
Read Sections 1–2, Theorem 2.1, and the contraction mechanism in Section 3.
The substitution \(W=iG\), \(V=-i(w1_d-A)\) gives \(VW+\Theta(W)W=1_d\) and \(\operatorname{Re}W>0\).
The source explains uniqueness and fixed-point iteration through holomorphic contraction; the manuscript proves uniqueness by a weighted row/column estimate.
This is a high-value direct connection.
No full independent proof audit was performed.

**Oskari H. Ajanki, László Erdős and Torben Krüger, _Stability of the Matrix Dyson Equation and Random Matrices with Correlations_ (2019), PTRF 173, 293–373, [publisher](https://doi.org/10.1007/s00440-018-0835-z), [arXiv:1604.08188v5](https://arxiv.org/abs/1604.08188v5).**
Registered and cited in the current manuscript as AEK19.
The public publisher record and arXiv v5, pages 1–9, were read, including Proposition 2.1, assumptions A1/A2, Theorem 2.6 and the distinction from random-matrix assumptions.
Their equation becomes ours under \(M=-G\), with covariance \(\Theta\).
The selected statements establish a precise contextual link to Stieltjes representation and stability.
Quantitative stability uses flatness and decay; the manuscript does not assume these.
The stability proof in Section 4 and the random-matrix proofs were not audited.

### Logarithmic determinants and deterministic equivalents

**Walid Hachem, Philippe Loubaton and Jamal Najim, _Deterministic equivalents for certain functionals of large random matrices_ (2007), Annals of Applied Probability 17, 875–930, [published author-hosted PDF](https://ligm.univ-eiffel.fr/~whachem/AAP0223.pdf), [DOI](https://doi.org/10.1214/105051606000000925).**
Canonical key HLN07 and an [existing selected audit](../../../../audits/literature/HLN07/Yin_U001.md); cited in the current manuscript.
This is an existing candidate worth restoring.
The present reading additionally checked the published-layout title page, assumptions A1–A3 on pp. 879–880, and Section 4, Theorem 4.1/(4.3), pp. 891–892.
These assume real iid centered entries with unit variance and a finite \(4+\epsilon\) moment, bounded variance profile, uniformly bounded row/column Euclidean norms of the deterministic shift, and an aspect-ratio limit.
The formula approximates a normalized expected log-determinant using deterministic resolvent equations.
Its proof in Appendix C was not audited.
The strongest connection is the resolvent-integration method and finite log-determinant/covariance correction; it is not the present unrestricted variational identity.

For the manuscript's regularized functional, the elementary identity

\[
\varphi_m\!\left(\log(1_m+\varepsilon^{-2}S^*S)\right)
=2\log\Delta_\varepsilon(S)-2\log\varepsilon
\]

explains the relation of the quantities being studied.
This is a local normalization comparison, not an assertion that HLN07 applies to every coefficient map in the manuscript.

### Positive-map stability and the Stein equation

**Gelu Popescu, _Similarity and ergodic theory of positive linear maps_ (2003), [arXiv:math/0310113v1](https://arxiv.org/abs/math/0310113v1).**
Registered and cited in the current manuscript as Pop03.
Read the introduction and Lemma 5.5, Lemma 5.8 and Theorem 5.9 with their proofs, preprint pp. 24–26.
Theorem 5.9 relates strict contractive similarity, spectral radius below one, and positive invertible solutions to \(X-\phi(X)=R\), with the Neumann-series solution.
This directly contextualizes the manuscript's finite-dimensional strict-defect argument.
The source allows normal positive maps on \(\mathcal B(H)\); normality is automatic here.
It does not construct the manuscript's matrices \(D,G_0\), identify the physical Dyson branch or prove the ensuing spectral gap.
This was a selected proof reading, not an independent whole-paper audit.
In Lemma 5.5's forward proof, the displayed equality for \(R-\phi(R)\) should be read as the lower bound supplied by the preceding inequality; the stated criterion and its use here require only that bound.

## Additional lead with lower verification depth

**Johannes Hoffmann, Tobias Mai and Roland Speicher, _Computing the Noncommutative Inner Rank by Means of Operator-Valued Free Probability Theory_, [publisher DOI](https://doi.org/10.1007/s10208-024-09684-5).**
The primary publisher's indexed Section 4.4 and Lemma 4.6 were inspected in the public search result.
The lemma controls small spectral mass through a Fuglede–Kadison determinant under its stated selfadjoint and zero-kernel hypotheses.
This provides an indirect computational interpretation of determinant estimates.
Full publication-year/version metadata and the complete proof were not checked in this pass; an attempted additional arXiv open failed.
Keep this as a follow-up lead rather than a citation-ready theorem comparison.
Do not infer a spectral gap from the logarithmic small-mass estimate.

## Editorial priorities and limits

No comprehensive citation-chain or priority search was attempted.

The highest-value additions are Helton–Rashidi Far–Speicher for the Dyson solution, HLN07 for the log-determinant calculation, and Popescu for strict positive-map stability.
GGOW20 and Allen-Zhu–Garg–Li–Oliveira–Wigderson are useful if the introduction explains the wider role of capacity.
Ajanki–Erdős–Krüger is useful for connecting the proof to MDE stability while stating its stronger quantitative assumptions.
The elementary coercivity, square completion and continuity steps do not need separate references merely to increase citation coverage.

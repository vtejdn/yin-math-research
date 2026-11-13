---
author: Yin
---

# F0008 Citation Applications

The current TeX in `paper/` is authoritative for the citation uses recorded here.
Each row is one source-specific use of a citation that appears in the current manuscript; grouped TeX citations have separate entries under each cited work.
The canonical bibliography owns bibliographic fields, and the linked U or other fixed source record owns source statements, inspected editions and source-review limits.
This map records only current citation applications, not consulted or uncited works.

## `ACSY24`

Source evidence: [ACSY24-U004](../../../audits/literature/ACSY24/Yin_U004.md#acsy24-u004) checks the Section 2.1 point-spectrum/Brown-atom interface and distinguishes it from other source findings.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/spectral.tex`, `subsec:brown-atoms`, `eq:brown-kernel-limit` | `\cite[Section~2.1, p.~12]{ACSY24}` | Supports that the kernel-projection weight is at most the Brown-measure atom; the nilpotent matrix calculation is local, and no later source formula is imported. |

## `AEK19`

Source evidence: [AEK19 source record](../../../audits/literature/AEK19/readme.md) records arXiv v5, the published-version comparison, Assumptions A1–A2, Theorem 2.6 and Proposition 4.4, with their extra hypotheses and proof limits.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/ordered-minmax.tex`, `rem:minmax-domains` | `\cite[Assumption A1]{AEK19}` | Identifies order flatness for the isotropic map; the example shows that this does not imply strict Hilbert–Schmidt positivity. |
| `paper/sections/spectral.tex`, `rem:dyson-stability` | `\cite[Section 4.2, Proposition 4.4 and Theorem 2.6]{AEK19}` | Compares the linearized Dyson stability operator under \(M=-G\); the source's quantitative conclusions require its stated flatness and spatial-decay assumptions, which are not claimed for the block covariance. |

## `AK20`

Source evidence: [AK20 source record](../../../audits/literature/AK20/readme.md) records arXiv v2 and the exact flatness hypotheses and inspected statements.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/spectral.tex`, passage beginning “Under the stronger two-sided flatness assumption” | `\cite[Proposition~2.9 and Theorem~2.5]{AK20}` | Compares the radial density under two-sided flatness with the local result for possibly degenerate maps; no Brown-support equality is imported. |

## `AK26`

Source evidence: [AK26 source record](../../../audits/literature/AK26/readme.md) records the checked arXiv v3 edition, assumptions A1–A2 and the exact theorem/proposition scopes.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/spectral.tex`, `rem:brown-variance-profile` | `\cite[arXiv version, Proposition~5.16]{AK26}` | Compares the diagonal variance-profile threshold \(r(\mathsf S D_z)=1\) with the locally obtained similar product \(D_z\mathsf S\). |
| `paper/sections/spectral.tex`, `rem:brown-variance-profile` | `\cite[arXiv version, Theorem~2.2]{AK26}` | Records the source's support and density conclusion under A1–A2; the manuscript's elementary spectral reduction does not assume those conditions. |

## `AZGL+18`

Source evidence: [AZGL+18 source record](../../../audits/literature/AZGL+18/readme.md) records the full arXiv v1 text, the published-article identity and the limits of its capacity/scaling comparison.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/introduction.tex`, paragraph after `def:determinant-capacity` | `\cite[Section 1.1]{AZGL+18}` | Supports the geodesic-convexity context for the homogeneous log-determinant capacity objective, not the affine determinant formula. |
| `paper/sections/imaginary-hs.tex`, operator-scaling comparison | `\cite{AZGL+18}` | Relates capacity/norm minimizations to operator scaling with independent left and right basis changes; the manuscript's same-factor identity is proved locally. |

## `BCG25`

Source evidence: [BCG25-U001](../../../audits/literature/BCG25/Yin_U001.md#bcg25-u001) records the exact semicircle specialization and branch restriction in the cited preprint.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/ordered-minmax.tex`, `prop:minmax-isotropic` comparison paragraph | `\cite[Theorem 1.1 and (1.6)]{BCG25}` | Contrasts a branch-restricted scalar free-convolution formula below the spectrum with the manuscript's finite-atomic ordered formula for every real \(x\). |

## `Bel15`

Source evidence: [Bel15 source record](../../../audits/literature/Bel15/readme.md) records the retained arXiv v2, Proposition 3.1, Remark 3.2 and the local \(X=0,\ q=\varepsilon D\) specialization.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/ordered-minmax.tex`, matrix minimax argument following `prop:minmax-matrix` | `\cite[Proposition 3.1 and Remark 3.2]{Bel15}` | Identifies the positive inner equation as a subordination specialization with source \(X=0\) and \(q=\varepsilon D\); the source's \(q\) is not the manuscript's variable \(q\), and no determinant minimization is imported. |

## `Bia97`

Source evidence: [Bia97 source record](../../../audits/literature/Bia97/readme.md) records the published article, the finite-atomic specialization, exact Section 3 locators and inspection limits.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/ordered-minmax.tex`, `prop:minmax-isotropic` | `\cite[Section 3, Lemma 4, Proposition 2 and Corollary 3]{Bia97}` | Attributes the classical semicircular spectral coordinate and density after specializing to the finite eigenvalue measure; the ordered determinant optimization is proved locally. |

## `BJL19`

Source evidence: [BJL19 source record](../../../audits/literature/BJL19/readme.md) records arXiv v1, Section 2 and Theorem 2, including the positive-solution characterization.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/imaginary-hs.tex`, geometric-mean identification after `eq:hs-balanced-scale` | `\cite[Section 2]{BJL19}` | Identifies \(c_b=b^{-1}\#H_b\) as the positive solution of \(c_bbc_b=H_b\); the strict-domain bijection is established separately. |

## `BSS18`

Source evidence: [BSS18 source record](../../../audits/literature/BSS18/readme.md) records arXiv v3, the exact regularization/hermitization passages and the absence of a full proof audit.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/spectral.tex`, regularized Cauchy-transform discussion | `\cite[arXiv version, Sections~2.1.6 and~2.2]{BSS18}` | Supplies the regularized Brown-potential and hermitization context; it does not supply the manuscript's positive-matrix minimum or a general zero-regularizer bound. |

## `BV04`

Source evidence: [BV04 source record](../../../audits/literature/BV04/readme.md) records the retained seventh printing with corrections and the exact Example 3.22 and Appendix A.5.5 passages.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/ordered-minmax.tex`, `prop:minmax-matrix` reduced-Hessian argument | `\cite[Appendix A.5.5]{BV04}` | Attributes the Schur elimination step for the Hessian after maximizing the auxiliary variable; positivity and global strict convexity are proved locally. |
| `paper/sections/ordered-minmax.tex`, `prop:minmax-square-completion` | `\cite[Example 3.22]{BV04}` | Attributes finite-dimensional quadratic conjugacy for the positive coefficient operator; the operator's positivity is checked in the manuscript. |

## `BYZ24`

Source evidence: [BYZ24 source record](../../../audits/literature/BYZ24/readme.md) records arXiv v3, the scalar-free circular hypotheses and the inspected density-bound passages.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/spectral.tex`, `rem:brown-circular-addition` | `\cite[arXiv version, Theorem~7.10 and Lemma~7.11]{BYZ24}` | Compares a uniform regularized-density bound and limiting absolute continuity under scalar free circular addition; those assumptions are not asserted for general matrix-coefficient pencils. |

## `DG24`

Source evidence: [DG24 source record](../../../audits/literature/DG24/readme.md) records the retained arXiv v2 definitions, theorem and their matrix-valued cumulant scope.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/spectral.tex`, `ex:brown-circular-coefficients` | `\cite[Theorem 2.9(b)]{DG24}` | Supports the \(M_m(\mathbb C)\)-valued \(R\)-diagonal characterization from the vanishing of nonalternating cumulants; the source theorem is not used for Brown-measure conclusions. |
| `paper/sections/spectral.tex`, `ex:brown-circular-coefficients` | `\cite[Definition 2.10]{DG24}` | Supplies the \(M_m(\mathbb C)\)-valued circular terminology once only the alternating second cumulants remain. |

## `FK52`

Source evidence: [MS24-U001](../../../audits/literature/MS24/Yin_U001.md#ms24-u001) records the Fuglede–Kadison determinant convention, and [Yin_L_F0036](../../../ledger/Yin_L_F0036_v1.md) checks the original FK52 bounded multiplicativity input and its analytic extension.
FK52 is the published 1952 determinant paper; this citation does not attribute the matrix capacity definition to it.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/introduction.tex`, `def:determinant-capacity` follow-up | `\cite{FK52,Gur04}` | Serves as a “see also” reference for determinant theory; MS24 supplies the manuscript's capacity definition and centered identity. |

## `GGOW20`

Source evidence: [GGOW20-U001](../../../audits/literature/GGOW20/Yin_U001.md#ggow20-u001) records the published full article's rank and operator-scaling statements in Sections 1.1–1.3.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/introduction.tex`, capacity/operator-scaling paragraph | `\cite[Sections 1.1--1.3]{GGOW20}` | Provides background linking capacity with operator scaling and noncommutative rank; no algorithmic conclusion is imported. |

## `Gur04`

Source evidence: [Gur04-U002](../../../audits/literature/Gur04/Yin_U002.md#gur04-u002) checks capacity and approximate scaling, and [Gur04-U003](../../../audits/literature/Gur04/Yin_U003.md#gur04-u003) reconstructs exact scaling and attainment in its stated scope.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/introduction.tex`, `def:determinant-capacity` follow-up | Grouped “see also” citation: `Gur04` alongside FK52 | Records Gurvits's capacity/scaling context; the affine determinant formula is not attributed to Gurvits. |
| `paper/sections/main-proof.tex`, `rem:capacity-attainment` | `\cite[Theorem 4.7]{Gur04}` | Relates homogeneous-capacity attainment to exact operator scaling, explicitly distinguished from attainment of the affine determinant minimum. |

## `Han08`

Source evidence: [Han08 source record](../../../audits/literature/Han08/readme.md) records the retained arXiv v6 definition, homogeneity and local trace identity.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/imaginary-hs.tex`, Wigner–Yanase correction discussion | `\cite{Han08}` | Supplies the Wigner–Yanase skew-information definition used to name the local commutator expression; the original Wigner–Yanase paper was not inspected. |

## `HL00`

Source evidence: [HL00 source record](../../../audits/literature/HL00/readme.md) records the retained author preprint, Theorem 4.4 and its scalar \(R\)-diagonal scope.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/spectral.tex`, `rem:brown-scalar-r-diagonal` | `\cite[author preprint, Theorem~4.4]{HL00}` | Compares the scalar \(R\)-diagonal radial-law formula; matrix-valued \(\rho=0\) alone does not supply scalar \(R\)-diagonality. |

## `HLN07`

Source evidence: [HLN07-U001](../../../audits/literature/HLN07/Yin_U001.md#hln07-u001) records the cited deterministic-equivalent theorem at statement/applicability depth.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/dyson.tex`, finite log-determinant discussion | `\cite[Theorem 4.1]{HLN07}` | Provides a related finite log-determinant expression evaluated at deterministic resolvent solutions; the arbitrary positive-trial minimization is proved separately. |

## `HRFS07`

Source evidence: [HRFS07 source record](../../../audits/literature/HRFS07/readme.md) records the published article, the half-plane uniqueness theorem and the Section 3 contraction argument.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/dyson.tex`, positive-real-part form of the Dyson equation | `\cite[Theorem 2.1 and Section 3]{HRFS07}` | Supports uniqueness of the physical half-plane solution; the manuscript also gives a direct proof for the derivative estimate it needs. |
| `paper/sections/imaginary-hs.tex`, `rem:positive-cone-context` | `\cite[Theorem 2.1]{HRFS07}` | Supplies existence, uniqueness and iteration for the positive matrix equation; the local minimizer conclusion uses additional selfadjointness and a separate proof. |

## `HS09`

Source evidence: [HS09 source record](../../../audits/literature/HS09/readme.md) records the published statement passages, II\(_1\)-factor hypothesis and exact contour/block limits.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/spectral.tex`, `rem:brown-spectral-subspaces` | `\cite[Theorem~1.1]{HS09}` | Supplies the invariant-subspace projection whose trace is the Brown measure of the Borel set, under the source's II\(_1\)-factor hypothesis. |
| `paper/sections/spectral.tex`, `rem:brown-spectral-subspaces` | `\cite[Introduction, (1.3)]{HS09}` | Identifies the Riesz-idempotent comparison for a contour in the resolvent set; the local eigenvalue-count specialization additionally assumes \(\rho=0\). |
| `paper/sections/spectral.tex`, invariant-block recovery paragraph | `\cite[Proposition~6.5]{HS09}` | Supplies the weighted Brown-measure decomposition for an invariant projection; the scalar circular block example is computed locally. |

## `Kun26`

Source evidence: [Kun26 source record](../../../audits/literature/Kun26/readme.md) records the retained arXiv v1, Theorem 1.9, Section 4.1 and the local Schur-complement specialization.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/positive-pencils.tex`, `rem:positive-sdp` | `\cite[Theorem 1.9 and Section 4.1]{Kun26}` | Supplies the semicircular spectral-edge feasibility formula; the affine determinant minimum and least feasible matrix are established locally. |

## `Miy22`

Source evidence: [Miy22-U001](../../../audits/literature/Miy22/Yin_U001.md#miy22-u001) records the published Section 2.1 Fock model and its normalization.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/positive-pencils.tex`, Fock-space positivity proof | `\cite[Section 2.1, pp.~3--5]{Miy22}` | Supplies the joint semicircular distribution of the left-creation operators; the square-completion and positivity consequence are local. |

## `MS17`

Source evidence: [MS17-U001](../../../audits/literature/MS17/Yin_U001.md#ms17-u001) records the selected affine, Brown-measure and weak-regularization interfaces and their proof boundaries.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/introduction.tex`, semicircular setting | `\cite[Section 1.11 and Chapter 2, Section 2]{MS17}` | Supplies the adopted freeness terminology for the standard semicircular family. |
| `paper/sections/introduction.tex`, Brown-measure introduction | `\cite[Chapter 11, Section 9]{MS17}` | Supplies the logarithmic-potential convention; the variational formula is proved locally. |
| `paper/sections/dyson.tex`, matrix Cauchy transform | `\cite[Chapter 9, (9.5)]{MS17}` | Supplies the resolvent sign convention. |
| `paper/sections/dyson.tex`, Dyson equation | `\cite[Chapter 9, Definition 10, Theorem 11 and Proposition 13]{MS17}` | Supplies the operator-valued semicircular moment/Dyson input; the convergent-series argument and continuation are given in the manuscript. |
| `paper/sections/dyson.tex`, `subsec:hermitization` | `\cite[Chapter 11, Section 9]{MS17}` | Supplies the established selfadjoint block-hermitization construction alongside the MS24 citation. |
| `paper/sections/spectral.tex`, Brown measure definition | `\cite[Chapter 11, Theorem 5, Definition 6 and (11.6)--(11.8)]{MS17}` | Supplies the Brown-measure potential and normalization facts; no equality of support and spectrum is asserted. |
| `paper/sections/spectral.tex`, regularized potential proof | `\cite[Chapter 11, Section 9, (11.14)--(11.15)]{MS17}` | Supplies weak convergence of the regularized Brown measures, not pointwise convergence of arbitrary densities. |
| `paper/sections/spectral.tex`, selfadjoint recovery | `\cite[Chapter 11, p.~270]{MS17}` | Supplies equality of Brown and scalar spectral measures for a normal operator; the manuscript applies it only to the selfadjoint pencil. |

## `MS24`

Source evidence: [MS24-U001](../../../audits/literature/MS24/Yin_U001.md#ms24-u001), [MS24-U002](../../../audits/literature/MS24/Yin_U002.md#ms24-u002), and [MS24-U003](../../../audits/literature/MS24/Yin_U003.md#ms24-u003) record the retained arXiv v1 determinant, capacity, covariance and centered-identity interfaces.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/introduction.tex`, centered determinant paragraph | `\cite[Theorem 1.2]{MS24}` | States the centered determinant/capacity result motivating the affine extension; the affine formula is proved in the manuscript. |
| `paper/sections/introduction.tex`, matrix notation paragraph | `\cite[Section 2.2]{MS24}` | Supports the size-explicit identity-matrix notation. |
| `paper/sections/introduction.tex`, `def:determinant-capacity` | `\cite[Definitions 1.1 and 2.1]{MS24}` | Supplies the determinant and capacity definitions with the source's trace and trial-domain conventions. |
| `paper/sections/introduction.tex`, complete-positivity explanation | `\cite[Section 2.2]{MS24}` | Supports complete positivity of coefficient maps of the displayed Kraus form. |
| `paper/sections/introduction.tex`, `def:affine-pencil` terminology sentence | `\cite[p.~3]{MS24}` | Supports the source's extended semicircular-pencil terminology for nonselfadjoint coefficient matrices. |
| `paper/sections/introduction.tex`, coefficient-map notation | `\cite[Theorem 1.2 and Lemma 3.5(ii)]{MS24}` | Supplies the \(\eta,\rho\) notation and covariance-map formulas. |
| `paper/sections/dyson.tex`, determinant convention paragraph | `\cite[Proposition 2.3]{MS24}` | Supplies multiplicativity and the block-diagonal determinant rule under the stated normalized trace. |
| `paper/sections/dyson.tex`, `subsec:hermitization` | `\cite[Section 3]{MS24}` | Supplies the source's block construction used in hermitization. |
| `paper/sections/dyson.tex`, adjoint covariance maps | `\cite[Lemma 3.5(ii)]{MS24}` | Supports the notation for \(\eta^*,\rho^*\) and the block covariance action. |
| `paper/sections/imaginary-hs.tex`, zero-mean recovery | `\cite[Theorem 1.2]{MS24}` | Identifies the centered special case recovered by the local limiting argument; no attainment conclusion is imported. |

## `Pop03`

Source evidence: [Pop03 source record](../../../audits/literature/Pop03/readme.md) records arXiv v1, the strict-defect criterion and the finite-dimensional applicability used here.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/dyson.tex`, strict Stein criterion | `\cite[Lemma 5.5 and Theorem 5.9]{Pop03}` | Supplies the positive-map strict-defect/spectral-radius criterion; the manuscript's finite-dimensional conjugation and Neumann-series application is stated locally. |

## `SH15`

Source evidence: [SH15 source record](../../../audits/literature/SH15/readme.md) records the published SIAM edition, Section 2, Definitions 2.1–2.2 and equation (2.2).

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/imaginary-hs.tex`, `rem:positive-cone-context` | `\cite[Section 2, equation (2.2)]{SH15}` | Supplies the affine-invariant positive-definite geodesic; strict convexity is proved locally. |

## `Spe26`

Source evidence: [Spe26-U001](../../../audits/literature/Spe26/Yin_U001.md#spe26-u001) records the public discussion and its exact candidate-expression limits; no proof is attributed to that post.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/introduction.tex`, opening motivation | `\cite{Spe26}` | Attributes the motivating question about extending the centered determinant formula to arbitrary mean to the public blog post. |
| `paper/sections/introduction.tex`, opening of “Other variational descriptions” | `\cite{Spe26}` | Attributes the candidate strict-domain Hilbert–Schmidt formula to the public discussion, not a proof. |
| `paper/sections/imaginary-hs.tex`, positive-matrix formula discussion | `\cite{Spe26}` | Identifies the public candidate expression discussed before the local proof. |
| `paper/sections/imaginary-hs.tex`, `rem:hs-strict-domain` | `\cite{Spe26}` | Attributes only the proposed expression; the manuscript records the undefined inverse on the nonstrict domain and proves its strict version. |

## `Zho26`

Source evidence: [Zho26 source record](../../../audits/literature/Zho26/readme.md) records the retained arXiv version, Theorem 4.2 and its circular-addition hypotheses.

| TeX use | Citation locator | Application and boundary |
| --- | --- | --- |
| `paper/sections/spectral.tex`, `rem:brown-circular-addition` | `\cite[arXiv version, Theorem~4.2]{Zho26}` | Compares the optimizer derivative with the source's density formula for scalar-free circular addition; its scalar-freeness and region hypotheses remain explicit. |

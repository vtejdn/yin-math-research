---
author: Yin
---

# Related Literature: Hilbert--Schmidt Comparison and Positive Pencils

This is a manuscript-facing literature assessment, read in manuscript order, for Proposition 1.4, Definition 1.5, Theorem 1.6, Section 4, Section 5 and Appendix A.
The search and statement inspection occurred on 2026-10-10.
This note proposes contextual citations and precise comparisons.
It does not add proof dependencies, register sources, audit whole papers, establish priority, or change manuscript mathematics.

The current public proposal is **Spe26**; restricted manuscripts are excluded from the public search and from this note's external comparisons.
The manuscript already cites Spe26, Gur04, MS24 and Miy22.

## Sources and inspection depth

The labels below are local navigation labels, not proposed canonical bibliography keys.

- **K26:** Dmitriy Kunisky, *Lehner's operator norm formulas, semidefinite programming, and spiked matrix models*, arXiv:2606.14687v1, 12 June 2026.
  [Primary full text](https://arxiv.org/html/2606.14687v1).
  Inspected Theorem 1.1, Remark 1.3, Theorem 1.9, Proposition 4.2 and the derivation in Section 4.1.
  Theorem 1.9 expresses the upper spectral edge of a selfadjoint semicircular pencil through the block constraint
  \[
  \inf\left\{c:\begin{pmatrix}cI-A_0-\Phi(Z)&I\\I&Z\end{pmatrix}\ge0\right\},
  \qquad \Phi(Z)=\sum_i A_iZA_i.
  \]
  Proposition 4.2 shows that block feasibility forces \(Z>0\).
  The paper also studies duality and applications; those applications were not reviewed here.
- **L99:** Franz Lehner, *Computing norms of free operators with matrix coefficients*, American Journal of Mathematics 121 (1999), 453--486.
  [Author's publication record](https://www.math.tugraz.at/~lehner/publ.html).
  The original publisher full text was inaccessible in this pass.
  K26 explicitly identifies Corollary 1.5 as the semicircular norm formula and explains its spectral-edge formulation in Remark 1.3.
  Thus the original attribution is supported by the author's bibliographic record and K26, but the exact original Corollary 1.5 was **not directly inspected**.
  Before inserting an exact original-result locator, inspect an accessible original copy.
- **HRS07:** J. William Helton, Reza Rashidi Far and Roland Speicher, *Operator-valued semicircular elements: Solving a quadratic matrix equation with positivity constraints*, IMRN 2007, rnm086, DOI 10.1093/imrn/rnm086.
  [Author-hosted published PDF](https://mathweb.ucsd.edu/~helton/BILLSPAPERSscanned/HRS07.pdf).
  Inspected Theorem 2.1, Sections 2.1--2.2, Proposition 3.2 and the numerical discussion in Section 4.
  The theorem selects the solution of \(VW+\eta(W)W=I\) having strictly positive real part when \(\operatorname{Re}V>0\), with an analytic positivity-preserving map under the stated boundedness hypotheses.
  Its fixed-point route differs from the manuscript's positive-cone minimization.
  Only the cited passages, not the complete numerical analysis, were reviewed.
- **SH15:** Suvrit Sra and Reshad Hosseini, *Conic geometric optimization on the manifold of positive definite matrices*, SIAM Journal on Optimization 25 (2015), 713--739, DOI 10.1137/140978168.
  [Author PDF](https://optml.mit.edu/papers/sra_hosseini_gopt.pdf); [inspected preprint v3](https://arxiv.org/abs/1312.1039v3), 12 December 2014.
  Publication identity was checked, but theorem locators below are from v3: Section 2, Definitions 1--2, equation (2), Theorems 3, 15 and 27.
  These describe the affine-invariant positive-matrix geodesic and ways to construct geodesically convex functions.
  Published/preprint numbering was not equated.
- **AZGLOW18:** Zeyuan Allen-Zhu, Ankit Garg, Yuanzhi Li, Rafael Oliveira and Avi Wigderson, *Operator Scaling via Geodesically Convex Optimization, Invariant Theory and Polynomial Identity Testing*, STOC 2018; [arXiv:1804.01076v1](https://arxiv.org/abs/1804.01076v1).
  The inspected full preprint has a 3 November 2017 title-page date and an April 2018 arXiv submission.
  Inspected Section 1.1, equation (1.1), and Section 3.1, Definitions 3.3--3.5 and Proposition 3.6.
  These relate determinant capacity to scaling and orbit-norm formulations and discuss geodesic convexity of logarithmic capacity.
  Complexity theorems and their proofs were not checked for transfer to the manuscript.
- **BJL17:** Rajendra Bhatia, Tanvi Jain and Yongdo Lim, *On the Bures-Wasserstein distance between positive definite matrices*, [arXiv:1712.01504v1](https://arxiv.org/abs/1712.01504v1), 5 December 2017.
  Inspected Section 2, equations (8)--(14), and Theorem 2 with its proof.
  The geometric mean \(A\#B\) is the positive solution of \(XA^{-1}X=B\), and the same matrix solves a trace minimization.
  This is a precise matrix-analysis identification relevant to the manuscript's coordinate map.
  No manuscript algorithm or transport theorem is inferred from it.
- **H08 / WY63:** Frank Hansen, *Metric adjusted skew information*, [arXiv:math-ph/0607049v6](https://arxiv.org/abs/math-ph/0607049v6), 21 February 2008, introduction, printed p. 3, explicitly defines \(I(\rho,A)=-\tfrac12\operatorname{Tr}[\rho^{1/2},A]^2\) and discusses its homogeneity.
  That definition was inspected.
  The original reference is E. P. Wigner and M. M. Yanase, *Information Contents of Distributions*, PNAS 49 (1963), 910--918, [publisher record](https://www.pnas.org/doi/10.1073/pnas.49.6.910).
  Its bibliographic identity was checked, but the original article scans were blocked by cookie/reCAPTCHA responses.
  H08 supplies the directly checked definition; WY63 is not represented as directly read.
- **G19:** Jean Gallier, *The Schur Complement and Symmetric Positive Semidefinite (and Definite) Matrices*, [author note](https://www.cis.upenn.edu/~jean/schur-comp.pdf), title-page revision 24 August 2019.
  Inspected Section 1 block factorization/inversion, Proposition 2.1, Proposition 4.2 and Theorem 4.3.
  This is an author-written expository proof source for Schur complements and the range condition in singular quadratic minimization.
  It is an optional explanatory reference, not an original-priority attribution.
  The results are written for real symmetric matrices; Hermitian versions require adjoints, or realification for the real Hilbert spaces in Proposition 4.5.

## 1. Proposition 1.4: strict Hilbert--Schmidt determinant formula

**Existing direct connection.**
[Speicher's public post](https://rolandspeicher.com/2026/09/09/a-story-of-the-determinant-of-operator-valued-semicircular-elements/) was reopened.
The displayed affine expression and the nonstrict Hilbert--Schmidt constraint remain the correct public provenance of the candidate formula.
The manuscript already explains that its strict-domain theorem is proved within the manuscript.
This citation should remain attached to the candidate expression, with the exact domain distinction retained.

**Additional connection worth making.**
The resulting formula belongs to a family of positive-matrix variational descriptions, alongside spectral-edge optimization (L99/K26) and capacity/scaling (MS24/AZGLOW18).
This is a comparison of the quantities computed and the feasible sets, not a claim of a common objective or common optimizer.
A short introductory transition can situate these three problems; the detailed coordinate and quadratic-term comparison belongs in Section 4.

**Recommendation.**
Keep the existing Spe26 citation.
Link forward to the concrete LMI/spectral-edge comparison after Theorem 1.6 rather than adding an undifferentiated reference list to Proposition 1.4.
No additional public source for the full strict-domain affine determinant theorem was verified by this bounded search.

## 2. Definition 1.5: the feasible matrices

**Direct external connection.**
K26's small SDP uses exactly the same block pattern.
Substitute
\[
A_0=-a_0,\quad A_i=-a_i,\quad \Phi=\eta,\quad Z=b.
\]
At \(c=0\), its constraint becomes the manuscript's \(L(b)\ge0\).
Thus the feasible set is a zero-level slice of the spectral-edge SDP for \(-S\).
This identification needs no commutation or nondegeneracy assumption on the selfadjoint coefficients.

**Citation placement.**
Immediately after the definition, or in the paragraph opening Section 5, identify this exact relation and cite K26, Theorem 1.9.
G19, Proposition 2.1, is a lower-value optional reference for the familiar Schur calculation; the manuscript already gives that calculation, so a separate textbook citation is unnecessary unless an optimization-oriented explanation is added.

## 3. Theorem 1.6: positivity and the determinant minimum

**Direct connection and its boundary.**
The spectral-edge formula yields
\[
S>0
\iff \lambda_{\max}(-S)<0
\iff \exists b>0:\ a_0-b^{-1}-\eta(b)>0.
\]
For the last equivalence, a negative feasible spectral threshold gives a strictly positive residual.
Conversely, a strictly positive residual permits a small negative threshold.
This explains the strict-feasibility part of Theorem 1.6 through K26/L99.

The determinant identity, the least feasible matrix \(q=E_m(S^{-1})\), and uniqueness for \(J\) are separate statements.
The inspected spectral-edge theorem does not establish these assertions.
In particular, \(J\) is not the linear objective of the SDP; convexity of the feasible set does not turn the determinant minimization into a standard convex SDP.

**Recommendation.**
Add a short comparison paragraph after Theorem 1.6, with fuller detail at the start of Section 5.
This is the strongest additional literature connection in the assigned sections.
Verify the original L99 passage before citing its exact numbering; K26's relevant theorem was directly checked.

## 4. Lemma 4.1: the positive-cone minimum

**Same equation, different characterization.**
With \(V=D\) and \(W=b\), the Euler equation is the HRS07 equation.
For \(D>0\), it describes the unique positive solution.
The manuscript supplies its variational characterization through \(J_D\), using Hilbert--Schmidt selfadjointness of the completely positive map.
The HRS07 setting permits more general analytic maps and does not supply this same scalar functional.

**Geometric connection.**
The paths \(b_0^{1/2}e^{tx}b_0^{1/2}\) are the geodesics described in SH15.
Strict convexity along these paths explains uniqueness even where ordinary linear convexity fails.
The manuscript's explicit sums of exponentials verify this property directly, so SH15 should orient the reader to the geometry, without replacing that proof or asserting convexity for unrelated manuscript functionals.

**Placement.**
One sentence after the proof can name this geometric interpretation; another can identify the positive equation with HRS07, Theorem 2.1.
Both are new optional citations in the manuscript.

## 5. Proposition 4.2: imaginary constant term

**Connection.**
HRS07 provides the surrounding matrix-valued resolvent problem and the distinguished positive-real-part solution.
Here the manuscript evaluates the Fuglede--Kadison determinant from the same solution and identifies it as a positive-cone minimum.
The congruence reducing arbitrary \(D>0\) to \(D=I\) is part of the manuscript's determinant argument.

**Recommendation.**
Reuse the preceding HRS07 comparison rather than cite it at every Dyson equation.
Explicitly separate the known resolvent characterization from the determinant evaluation.
The search did not identify and verify an external paper with the exact arbitrary-matrix-\(D\) variational determinant formula; this is a search limitation, not a novelty claim.

## 6. Equations (4.4)--(4.5): zero regularizer and homogeneous capacity

The zero-mean determinant identity is already correctly connected to MS24, Theorem 1.2.
The homogeneous trace expression also has a concrete scaling interpretation: if \(\det c=1\), then
\[
\operatorname{Tr}(c\eta(c))
=\sum_j\|c^{1/2}a_jc^{1/2}\|_{\mathrm{HS}}^2,
\qquad
\inf_{\det c=1}\operatorname{Tr}(c\eta(c))
=m\operatorname{Cap}(\eta)^{1/m}.
\]
Thus the manuscript expresses the capacity through a *common positive congruence* of a selfadjoint coefficient tuple.
AZGLOW18, Section 3.1, supplies the broader left-right scaling/orbit-norm context; its two scaling factors should not be silently identified with the single congruence factor above.
Gur04 remains the existing foundational citation for capacity and exact versus approximate scaling.

**Placement.**
A compact remark after (4.5) could make this connection useful.
Do not transfer an operator-scaling complexity guarantee to the manuscript's functional without a separate algorithmic analysis.

## 7. Remark 4.3: the strict domain

The public proposal is the immediate reference and is already cited.
G19, Proposition 4.2 and Theorem 4.3, offers a general explanation of why singular quadratic optimization needs a range condition as well as a generalized inverse.
This is relevant only if the manuscript later discusses a nonstrict-domain extension.
It does not repair the public formula by itself.

**Recommendation.**
Keep the present explicit counterexample and strict-domain statement.
Do not add a pseudoinverse discussion or a generic citation merely to lengthen the remark.
The range-condition literature is a useful contextual lead, not a verified alternative theorem for the current domain.

## 8. Lemma 4.4: positive coordinates for the strict domain

**Exact identification.**
In the standard matrix-geometric-mean notation of BJL17, Section 2,
\[
c_b=b^{-1}\#H_b.
\]
Its defining equation \(c_bbc_b=H_b\) is precisely the positive Riccati equation characterizing that mean.
BJL17, Theorem 2, also connects this matrix to a trace variational problem.
This gives a familiar matrix-analysis meaning to the explicit square root in (4.6).

The strict-Hilbert--Schmidt domain bijection also needs the completely positive Stein/Neumann argument.
That part is not supplied by merely recognizing a geometric mean.
Since \(H_b\) itself depends on \(b\), the full coordinate map is not a transport problem with two fixed endpoint matrices.

**Placement.**
One optional sentence after (4.6), or after the proof, is sufficient.
The optimal-transport background of BJL17 is indirect context and does not need an application paragraph here.

## 9. Proposition 4.5: order between the quadratic corrections

The proof's block elimination is the Schur-complement mechanism in G19, Section 1 and Proposition 2.1, applied to a real Hilbert space of matrices.
The particular block identity following from \(KJK=J\), and the resulting comparison with \(I+\Psi_+\), are additional structures in this proof.
The search did not locate a directly matching external comparison theorem.

**Recommendation.**
Retain the self-contained proof.
A reference to general block elimination is optional and lower value than the concrete noncommutativity interpretation in Remark 4.7 below.
Do not describe the inequality as a mere variable change or as ordinary inverse monotonicity applied to the full unsplit equations.

## 10. Lemma 4.6: global comparison

This is a global quadratic upper bound for the logarithmic determinant as a function of its selfadjoint constant term, under \(\|\Psi\|_{2\to2}<1\).
It uses the positive-cone equation and a support/kernel decomposition.
Neither the inspected HRS07 uniqueness theorem nor the geometric optimization results imply this upper bound by themselves.

**Search outcome.**
Public searches on semicircular determinants, quadratic majorants, positive fixed-point equations and variational matrix inequalities did not yield a verified external theorem with this statement.
The best contextual references concern its mechanisms in Appendix A.
No claim about nonexistence or priority follows.

**Recommendation.**
No additional standalone citation presently merits insertion at the lemma.
The existing internal dependencies should remain explicit.

## 11. Remark 4.7: equality of infima versus pointwise comparison

**A precise connection to quantum information.**
In its \(\eta=0\) case, the difference of the manuscript's corrections has the exact form
\[
\begin{aligned}
q_{\mathrm{gen}}(b)-q_{\mathrm{HS}}(b)
&=\operatorname{Tr}(ba_0^2)
 -\operatorname{Tr}(b^{1/2}a_0b^{1/2}a_0)\\
&=\tfrac12\|[b^{1/2},a_0]\|_{\mathrm{HS}}^2\\
&=\operatorname{Tr}(b)\,
 I\!\left(\frac{b}{\operatorname{Tr}(b)},a_0\right).
\end{aligned}
\]
The first line follows by substituting \(Z_b=a_0b\) and \(c_b=b^{-1/2}\); expanding the squared commutator proves the second.
The last line uses the directly inspected Wigner--Yanase definition in H08.
This is an elementary local calculation, self-checked here, not a newly accepted project Claim.

It explains exactly why the \(\eta=0\) comparison is strict when \([b,a_0]\ne0\), and why scalar data cannot display this discrepancy.
It does **not** identify the correction gap for arbitrary nonzero \(\eta\) with the same skew information.

**Placement.**
An optional short addition to Remark 4.7 could replace or accompany the isolated numerical example.
Cite the directly checked definition source and the original work with its acquisition/inspection status made accurate before manuscript integration.
The manuscript currently has neither citation.

## 12. The closing hermitization paragraph of Section 4

The comparison between an \(m\)-dimensional formula and its \(2m\)-dimensional selfadjoint realization is already supported by the manuscript's hermitization/Dyson discussion and MS24, Lemma 3.5(ii).
The precise connection is equality of normalized determinants under hermitization, with a different matrix trial size.
No additional citation found in this pass materially improves that explanation.

## 13. Section 5: individual proof mechanisms and consequences

| Mathematical content | External connection and limits | Suggested use |
| --- | --- | --- |
| \(L(b)\ge0\iff F(b)\ge0\), convex feasible sets | The exact connection to K26 was given at Definition 1.5; ordinary block positivity is also covered by G19. | Put the spectral-edge comparison in the opening paragraph; avoid duplicate citation at the same Schur calculation. |
| Fock-space square completion | Miy22, Section 2.1, is already cited for the realization. L99 is a relevant broader setting for matrix-coefficient creation/annihilation norms, but its exact original proof was not read in this pass. | Keep Miy22. Add L99 only when discussing the spectral-edge history, after checking the original. |
| Monotone iteration and least feasible \(q\) | The recursion uses \((a_0-\eta(q_k))^{-1}\), unlike HRS07's plus-sign map. The manuscript proves its branch selection from finite Fock compressions. | State the sign/branch distinction if comparing algorithms. Do not cite HRS07 as proving this monotone least-supersolution assertion. |
| Minimum and uniqueness of \(J\) | The least-element order argument and local positive Hessian have a different role from either SDP convexity or geodesic convexity of \(J_D\). | No generic convex-optimization citation should imply convexity of \(J\). |
| \(b_*=q^2+q\eta(b_*)q\) | This is a discrete Lyapunov/Stein-type equation for the derivative of the Dyson solution. It connects susceptibility to the same positive-map stability condition used elsewhere. No additional exact source theorem was checked for this derivative in the present pass. | Keep the displayed differentiation and existing internal reference; a named control-theory analogy alone adds little. |
| Nonstrict boundary example \(2+s\) | It distinguishes zero spectral edge from a positive gap, consistent with the threshold interpretation above. | The example is already self-contained; do not add an unrelated general warning about boundary attainment. |

## 14. Appendix A: individual mechanisms

| Appendix content | Related literature and actual relationship | Citation judgment |
| --- | --- | --- |
| A.1: \((J-A)^{-1}\le(I-A)^{-1}\) for a selfadjoint involution and \(\|A\|<1\) | Block inverse and Schur elimination in G19, Section 1, explain the reduction. The indefinite involution and the sign of its correction are specific to the displayed argument. | A generic tool citation is optional; no external theorem with precisely this order statement was verified. |
| A.1: complete positivity of the inverse series | The convergent series is built from compositions of completely positive maps; this is distinct from Hilbert--Schmidt positivity. | The direct proof is short and clarifies the distinction. No additional citation is recommended. |
| A.2: maximizing the regularized determinant minus a quadratic form | Coercivity and differentiation produce a stationary Dyson equation. HRS07 is related through the equation, but does not justify the global maximum bound. | Reuse the Section 4 context if desired; preserve the manuscript proof. |
| A.3: support/kernel decomposition and effective covariance | Schur reduction is a general matrix mechanism (G19). Complete positivity of the effective map and strict Hilbert--Schmidt contraction use the special inverse comparison. | Do not attribute the full reduction to a generic Schur-complement source. |
| A.4: positive-cone estimate and removal of the regularizer | The effective equation is another application of Lemma 4.1, hence related to HRS07 at the fixed-point level. The uniform error bound and limiting determinant comparison remain additional assertions. | Prefer the explicit internal link to Lemma 4.1. No new outside citation is needed at the limit passage. |

## Decisions, access limitations and review relation

The unexpectedly direct K26 block constraint was read in full mathematical form; the geometric-mean and skew-information identifications were then checked against primary research texts.

The most useful additions are (i) the exact spectral-edge/LMI correspondence near Theorem 1.6, (ii) the fixed-point/geodesic interpretation of Lemma 4.1, (iii) the geometric-mean identification in Lemma 4.4, and (iv) the \(\eta=0\) skew-information identity in Remark 4.7.
The homogeneous capacity/scaling connection is also useful if space permits.
Standard Schur-complement references and broad control-theory analogies should remain optional because the corresponding computations are already explicit.

Access limitations: original L99 full text could not be inspected; the official Boyd--Vandenberghe book PDF returned a tool error, so G19's author-hosted note was used instead; the original WY63 full text was blocked, so H08 supplied the checked definition.
SH15's published PDF was discoverable but later extraction requests failed; exact theorem locators use its accessible v3 preprint.
The coordinating reader subsequently obtained the UCLA author copy of Boyd--Vandenberghe; the specific passages read are recorded in [the min--max analysis](minmax.md).
No new artifacts were retained in that pass and no canonical source-registration or proof-review status is claimed.

The original independent checks of the two local identifications, including their normalization and scope limits, are retained in [the manuscript-local bounded findings](../paper/review.md#original-related-literature-bounded-review).

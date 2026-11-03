---
author: Yin
---

# Affine Determinants: External Candidates and Their Applicability

Record kind: targeted source search and local candidate audit for [Yin_T_F0008](../tasks/Yin_T_F0008_v1.md#yin_t_f0008).
Dates: 2026-09-12 to 2026-09-13.
Author: research agent another AI agent.
The user authorized external literature exploration in this continuation.
Source discoveries below are not new proved Claims, and do not modify the status of Yin_C_F0119-Yin_C_F0123.
Bibliographic identities are registered in literature/readme.md; source statements and verification boundaries are owned by the precise audit units linked below.
The later [project proof](../claims/Yin_C_F0124_v1.md) develops the proposed general formula; its proof review controls the result status.
The exploratory obligations below preserve the search checkpoint.

## Local Search and the Question Left Open

The search first inspected the existing MS24 and MS17 audit interfaces, and the [variational frontier](Yin_L_F0033_v1.md).
These provide the exact Dyson primitive, positive real and imaginary drift formulas, ordered scalar/isotropic minimax, and capacity scaling.
They do not already supply a global optimization formula for arbitrary selfadjoint drift.
The missing input is a finite-dimensional variational domain that selects the physical branch throughout the spectrum without assuming that the trial matrix solves the Dyson equation.

External queries used public mathematical terminology, including matrix Dyson equation, variational principle, operator-valued semicircular determinant, and logarithmic potential of free additive convolution.
No private manuscript content was supplied externally.

## A Direct Public Candidate from Speicher

The exact proposal and source-status assessment are owned by [Spe26-U001](../audits/literature/Spe26/Yin_U001.md#spe26-u001), with bibliographic and online-only access metadata in the Spe26 intake.
The public author post attributes the candidate to ChatGPT and supplies no inspectable proof.
The exploration below starts from that candidate; no source theorem asserting its correctness was accepted.

For selfadjoint \(a,a_j\in M_m(\mathbb C)\), let
\[
 S=a+\sum_j a_j\otimes s_j,\qquad
 \eta(x)=\sum_j a_jxa_j,\qquad
 \mathcal C_b(x)=bxb,
\]
and use the normalized Hilbert-Schmidt inner product.
The proposed right side is
\[
 e^{-1/2}\inf_{\substack{b>0\\\mathcal C_b-\eta\succeq0}}
 \Delta_m(b)
 \exp\!\left[\frac12
   \langle a,(\mathcal C_b+\eta)^{-1}(a)\rangle_2\right].       \tag{1}
\]
Here \(\succeq0\) is positivity on the entire Hilbert-Schmidt space.
The printed inverse is ordinary; no convention addresses its possible kernel.
Formula (1) is a directly relevant research candidate, not an accepted external proof input.
The source's earlier centered formula is the already audited MS24 result.

### The Printed Domain Does Not Guarantee the Printed Inverse

The following finite-dimensional calculation is a local audit of (1).
Set
\[
 m=2,\qquad a_1=Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
 \qquad b=I_2.
\]
The map \(\eta=\operatorname{Ad}Z\) is the identity on diagonal matrices and minus the identity on off-diagonal matrices.
Consequently, \(\mathcal C_b-\eta=I-\eta\succeq0\), but \(\mathcal C_b+\eta=I+\eta\) vanishes on all off-diagonal matrices.
Taking
\[
 a=\begin{pmatrix}0&1\\1&0\end{pmatrix}
\]
places the drift in this kernel.
Thus the displayed objective is undefined at an allowed trial point.
This identifies a formulation defect; it does not disprove an appropriately defined infimum formula.

A natural candidate repair is to use the open domain
\[
 \mathcal B_\eta^{\mathrm{str}}
   =\{b>0:\mathcal C_b-\eta\succ0\}.                         \tag{2}
\]
This set is nonempty, since \(b=tI\) is feasible for sufficiently large \(t\).
On (2), the inverse in (1) is positive definite.
Here is an elementary verification that does not assume Hilbert-Schmidt positivity of \(\eta\).

Write \(\mathcal T_b(x)=b^{-1/2}xb^{-1/2}\) and
\[
 \Phi_b=\mathcal T_b\eta\mathcal T_b,
 \qquad
 \Phi_b(x)=\sum_j c_jxc_j,
 \qquad c_j=b^{-1/2}a_jb^{-1/2}=c_j^*.
\]
Congruence by the positive invertible Hilbert-Schmidt operator \(\mathcal T_b\) converts \(\mathcal C_b\pm\eta\) to \(I\pm\Phi_b\).
For a selfadjoint \(x\), diagonalize \(x\) with eigenvalues \(\lambda_k\).
Then
\[
 \left|\langle x,\Phi_b(x)\rangle_2\right|
 \leq \frac1m\sum_{j,k,l}|\lambda_k\lambda_l|\,|(c_j)_{kl}|^2
 =\langle |x|,\Phi_b(|x|)\rangle_2.                         \tag{3}
\]
Because \(\Phi_b\) is selfadjoint and preserves adjoints, each of its real eigenvalues has a nonzero selfadjoint eigenvector: take a nonzero real or imaginary part of any eigenvector.
Equation (3) and the Rayleigh bound show that the absolute value of every eigenvalue is at most its largest eigenvalue.
If \(I-\Phi_b\succ0\), this largest eigenvalue is less than one, so \(I+\Phi_b\succ0\).
The same argument gives semidefinite positivity on the closed domain, but cannot give invertibility there, as the example shows.

An alternative closed-domain formulation uses the extended quadratic function
\[
 \mathcal Q_K(a)
 =\sup_{x=x^*}\left\{\langle a,x\rangle_2
                     -\frac12\langle x,Kx\rangle_2\right\}
 =\begin{cases}
   \frac12\langle a,K^\dagger a\rangle_2,&a\in\operatorname{ran}K,\\
   +\infty,&a\notin\operatorname{ran}K,
  \end{cases}                                                  \tag{4}
\]
where \(K=\mathcal C_b+\eta\succeq0\).
This equality follows by diagonalizing \(K\) on the real space of selfadjoint matrices.
The equivalence between a repaired closed-domain infimum and the strict-domain infimum, and either infimum's equality to the determinant, remain proof obligations.
Formula (4) must not be silently substituted for the source's printed ordinary inverse.

### An Independent Scalar Check

For \(m=1\), let \(\eta(x)=\sigma x\), \(\sigma>0\), and \(a\in\mathbb R\).
Taking logarithms of (1) gives the trial objective
\[
 f_a(b)=\log b-\frac12+\frac{a^2}{2(b^2+\sigma)},
 \qquad b\geq\sqrt\sigma.
\]
Its derivative has the sign of
\[
 (b^2+\sigma)^2-a^2b^2.
\]
If \(|a|\leq2\sqrt\sigma\), this is nonnegative throughout the domain, so the infimum is
\[
 \frac12\log\sigma-\frac12+\frac{a^2}{4\sigma}.
\]
If \(|a|>2\sqrt\sigma\), the unique minimizer is
\[
 b_* =\frac{|a|+\sqrt{a^2-4\sigma}}2,
\]
and the minimum is \(\log b_*+\sigma/(2b_*^2)\).
These are exactly the bulk and exterior values in the existing [scalar proof](../claims/Yin_C_F0122_v1.md).
Passing to \(b>\sqrt\sigma\) leaves both infimum values unchanged.
This is a consistency check for the proposed repair, not evidence of the general matrix equality.

### Numerical Adversarial Check with a Noncommuting Drift

Executed on 2026-09-13 with Python 3.13.15, standard library only.
The original screen was run directly from a PowerShell here-string; its exact program now has the native J home linked below.
No new screen was run during this retention maintenance.
It checks a necessary universal upper bound in a one-Kraus \(2\times2\) model.
Any such selfadjoint Kraus matrix can be diagonalized; a diagonal unitary then makes the drift's off-diagonal entry real without changing the Kraus matrix.
Thus the parametrization tests noncommuting coefficients, including negative Hilbert-Schmidt covariance eigenvalues \(pq<0\).

For \(B=\operatorname{diag}(p,q)\) and \(A=\left(\begin{smallmatrix}a&z\\z&d\end{smallmatrix}\right)\), the determinant of (A+tB) is quadratic in \(t\).
Its roots reduce the potential calculation to the explicit scalar semicircle potential; the calculation uses no Dyson solver.
No violation appeared in 200,000 seeded trials.
The largest residual was \(-3.2285730582892747\cdot10^{-6}\).
This floating-point screen is evidence of consistency, not a proof or a validated numerical certificate.

The exact retained [native program](../computations/programs/Yin_J_F0010/main.py) and [reproduction account](../computations/programs/Yin_J_F0010/readme.md) supply this original screen.


The printed worst trial was \(k=59790\), \(p=-0.6276111874414962\), \(q=0.7787443888517115\), \(a=0.5943016407731344\), \(d=-0.6839372533367548\), \(z=0.4610325177001209\), with potential \(-0.15598734721283608\) and bound \(-0.1559841186397778\).
Values arbitrarily close to zero determinants can make this numerical comparison delicate; the subsequent proof must be independent of the screen.

## A Scalar Free-Convolution Variational Theorem

The exact statement, conventions and inspection depth are owned by [BCG25-U001](../audits/literature/BCG25/Yin_U001.md#bcg25-u001); its [edition note](../audits/literature/BCG25/readme.md#yin) identifies the inspected v1 and the title-page/arXiv author-order difference.
The source minimizes a scalar free-convolution action only below the left support edge, on a domain restricted by both positivity of the logarithm's argument and (0<g<g_*).
Its warning that unrestricted minimization can fail is directly relevant to the present branch-selection problem.

The local applicability judgment is as follows.
For isotropic matrix covariance, the scalar spectral law is a free additive convolution with the empirical eigenvalue law of the drift.
Thus this theorem can be compared with the exterior portion of [Yin_C_F0122](../claims/Yin_C_F0122_v1.md).
It is not needed to validate that existing independent proof, and does not replace its full real-axis minimax argument.
For general matrix covariance, a scalar \(R\)-transform and the one-dimensional order used in the source do not give the missing matrix domain or global extremum.

## A Secondary Direction Retained as a Lead

Johannes Alt and Torben Krueger, [*Brown measures of deformed \(L^\infty\)-valued circular elements*](https://arxiv.org/html/2409.15405v2), arXiv:2409.15405v2.
Abstract, contents and the introduction were inspected.
The base algebra is commutative and the main regularity statements impose assumptions on deformation and covariance.
Its Sections 4-6 and Appendix B concern the Dyson representation and stability of Brown measures.
This search did not import a theorem from that paper or locate a global determinant extremum.
Its source and scope warrant a later focused spectral audit if a proposed variational formula needs a deformed circular benchmark.
No full-paper absence claim is made from text search.

The Ajanki--Erdos--Krueger lead is now located in the [identified arXiv v6](../audits/literature/AEK19qve/readme.md#yin).
The [C_F0125 source comparison](../claims/Yin_C_F0125_v1.md#source-reuse-and-scope) distinguishes the scaling equation (11.8) from the purely imaginary, zero-drift minimization in Lemma 6.8 and (6.28), with its actual hypotheses.
That narrower comparison supplies no accepted proof input for the ordered covariance formula and no general-real-drift or noncommuting-matrix extension.

## Consequences for the Research Plan

1. Audit the repaired strict-domain version of (1) before inventing a competing general formula.
   It already has the desired freely variable positive matrix and retains negative Hilbert-Schmidt directions of the covariance.
2. Establish any global inequality and branch-selection equality separately.
   Correct stationary equations or the scalar check alone do not establish the infimum.
3. Prove centered capacity recovery as an optimization identity, including zero capacity and nonattainment, rather than evaluating only at a hypothetical balanced optimizer.
4. If a selfadjoint formula survives, apply the previously checked hermitization or signed-Schur reduction to address arbitrary complex coefficients, keeping normalized trace factors and regularization limits explicit.
5. Preserve the public source's proposed status and the local origin of any subsequent proof or counterexample.
   An author-hosted discussion of AI output is neither a peer-reviewed theorem nor an independent proof certificate.

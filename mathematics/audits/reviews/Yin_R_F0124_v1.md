---
author: Yin
---

# Yin_T_F0008: Independent Review of the Affine Hilbert--Schmidt Infimum

- Date and reviewer: 2026-09-13, indefinite-variation agent, independent mathematical review.
  The reviewer did not author either proof module.
  During review, the reviewer supplied the clarification before companion equation (9), reconstructed the physical approximation independently, and discussed the finite-dimensional covariance interface with the authors.
  This collaboration is disclosed.
- Targets: [Yin_T_F0008](../../tasks/Yin_T_F0008_v1.md#yin_t_f0008) and [Yin_C_F0124](../../claims/Yin_C_F0124_v1.md#decision-candidate-0004); the complete [affine infimum proof](../../claims/Yin_C_F0124_v1.md), Sections 1--7, and the complete [global comparison proof](../../claims/Yin_C_F0124_v1.md#affine-hs-variation-tests).
  Registration and current mathematical/review assessments belong to the coordinating agent and the responsible Claim material and its selected decision.
  No mathematical Role is assigned here.
- Inspected revision: the 2026-09-13 text containing the explicit commutator separation before companion equation (9), the kernel-corner proof (10)--(18), the physical approximation (5)--(9) in the main module, the finite capacity reductions (10)--(17), and the exact checks in Section 7.
  Navigation and registration labels may change without altering these findings.
  Later substantive changes require scoped review.
- Mathematical finding: the two inequalities and their assembly pass this review, including arbitrary finite size, all selfadjoint coefficients and drift, arbitrary complex coefficients after hermitization, empty noise, zero determinants and nonattainment.
  The valid formula is an infimum on its stated strict domain.
  This does not validate the source's ordinary inverse on its larger nonstrict domain.

Final inspected artifacts after the authors' registration and source-navigation edits:

- Main affine infimum proof
- Global comparison proof

## Obligations and Evidence

| Obligation | Decisive evidence checked |
| --- | --- |
| Free finite-dimensional trials and a defined objective | Any positive matrix satisfying strict Hilbert--Schmidt positivity is allowed; large scalar matrices are feasible. The scaled covariance has absolute spectral radius below one, so the plus-sign linear map is invertible. No physical equation restricts a trial matrix. |
| A global inequality | The regularized determinant minus the quadratic mean penalty has an actual global maximum over all Hermitian means. Stationarity is used only after maximizing; a uniform bound at that maximum controls every mean. |
| Negative Hilbert--Schmidt covariance directions | Complete positivity is never substituted for positivity of a Hilbert--Schmidt quadratic form. The involution inverse in the corner argument may itself be indefinite in the latter sense; its separately proved inverse comparison is the property used. |
| Singular real resolvent | The support and kernel of the real part are both retained. The support contributes determinant one; the kernel is controlled by an effective positive-cone minimum. |
| Uniform control before the limit | The corner trace identity cancels the potentially unbounded resolvent trace. The remaining error is bounded by \((\varepsilon+\varepsilon^2/2)/(1-\rho)\), independent of the maximizing mean and its corner dimensions. |
| Matching admissible approximants | The explicit matrices constructed from the physical resolvent satisfy congruence-unitarity and strict admissibility. Their objective differs from the regularized determinant by the stated bounded trace correction. |
| Complete centered recovery | Two-variable capacity duality, a symmetric geodesic midpoint and scalar scaling give the capacity identity directly. Positive regularization supplies a feasible sequence without a zero-drift balancing point. Zero capacity is included. |
| General complex coefficients | Hermitization preserves the normalized determinant. The full covariance is retained with drift. At zero drift, conjugation symmetry and a geodesic midpoint give the square relation between hermitized and original capacities. |

## Global Comparison and the Kernel Corner

The regularized mean functional is differentiable on the finite real vector space of Hermitian matrices.
Tracing its logarithmic derivative in a direction \(h\) and using cyclicity yields \(\operatorname{tr}_m(Hh)\), where
\[
 R=E((a+T-i\varepsilon)^{-1})=H+iQ,\qquad Q>0.
\]
Consequently a global maximum satisfies \(a=(I+\Psi)H\), and Dyson gives \(R^{-1}=H-iB\), \(B=\Psi(Q)+\varepsilon I>0\).
The Yin_C_F0119 primitive has the correct sign after adjunction and yields the comparison module's equation (8).

The revised argument correctly avoids splitting a product into real and imaginary parts before its coefficients are Hermitian.
Subtracting the two inverse products gives
\[
 [Q,B]+i[Q+B,H]=0.
\]
The first term is skewadjoint and the second selfadjoint; both vanish.
The coefficient \(QH-HB\) is now selfadjoint, so the subsequent split is legitimate.
Thus \(QB=BQ=I-H^2\), \(QH=HB\), and \(HQ=BH\).
These imply that the support and kernel of \(H\) reduce \(Q,B,R\).
On the support, \(U=\operatorname{sign}(H)\) gives \(R^{-1}=UR^*U\), and the absolute determinant is one.
Both positive and negative spectral values of \(H\) are allowed.

The inverse comparison was checked independently.
For a selfadjoint operator \(A\) with norm at most \(\rho<1\) and a selfadjoint involution \(J\), the inverse \((J-A)^{-1}\) has norm at most \((1-\rho)^{-1}\).
Writing \(J=I-2P\), the finite perturbation formula gives a negative semidefinite correction to \((I-A)^{-1}\), since its compression is strictly larger than \(I/2\).
This proves the needed order inequality even though \((J-A)^{-1}\) need not be positive as a Hilbert--Schmidt operator.
In the actual matrix-algebra setting the Neumann series consists of completely positive maps, proving positivity in the different, order-preserving sense.

All corner traces and adjoints use unnormalized Hilbert--Schmidt inner products; there is no missing ratio of corner dimensions.
The Schur complement of the compression of \(I-\Psi\), followed by the inverse comparison, proves strict positivity of \(I-\Phi\).
The effective drift \(D\) is positive because the inverse map is completely positive.
The trace identity in companion (15) follows by moving both off-corner maps and the selfadjoint inverse under that same unnormalized pairing.

Only Yin_C_F0120's finite-dimensional minimization proof is needed.
A completely positive Hilbert--Schmidt selfadjoint map has Hermitian Kraus matrices: average a Kraus representation with its adjoint and take the Hermitian real and imaginary parts.
Thus the finite action proof applies to the effective covariance.
Comparing its minimum with the identity gives companion (16), with the stated signs and factors.
The exact trace cancellation gives the uniform error estimate, also when either corner is absent.
No inverse of \(H\) on its kernel is used.

## Physical Approximation and Degenerate Limits

For positive regularization, \(Q\) is strictly positive.
With \(K=Q^{-1/2}HQ^{-1/2}\), write
\[
 R=Q^{1/2}(K+iI)Q^{1/2},\qquad
 b=Q^{-1/2}(I+K^2)^{-1/2}Q^{-1/2}.
\]
The factors depending on \(K\) commute, and direct multiplication proves \(RbR^*=b^{-1}\) and \(R^{-1}=bR^*b\).
The real and imaginary equations in main (8) follow with their multiplication order intact.

For the scaled covariance the positive matrix \(W=b^{1/2}Qb^{1/2}\) has strict defect \(W-\Psi(W)=\varepsilon b^{-1}>0\).
Similarity by its square root gives a strict contraction in the positive order-unit norm, so the finite spectrum lies in the unit disk.
Hilbert--Schmidt selfadjointness of the original scaled map then gives strict Hilbert--Schmidt admissibility.

The objective calculation was reconstructed independently:
\[
 \Phi_a(b_\varepsilon)=\log\Delta_\varepsilon(S)
                  -\frac{\varepsilon}{2}\operatorname{tr}_dQ.
\]
The correction lies in \([0,1/2]\).
At finite limiting logarithmic determinant, the spectral measure has no zero atom and dominated convergence makes the correction vanish.
At logarithmic determinant \(-\infty\), subtracting a bounded correction preserves that limit.
Thus the matching sequence requires neither attainment nor a limiting inverse, and includes the deterministic zero pencil.

## Capacity Reduction and Exact Checks

The finite capacity reduction was checked independently of MS24's determinant conclusion.
For a singular positive output, the determinant-one trace infimum is zero by shrinking on its support and compensating on its kernel.
Joint geodesic convexity follows from explicit nonnegative exponential coefficients, not Euclidean convexity.
The equality of the two midpoint coordinates follows from uniqueness of the positive solution of \(rp^{-1}r=q\), which also implies \(rq^{-1}r=p\).
This justifies the symmetric reduction of the two-variable capacity infimum.

Scalar scaling gives exactly the constant \(d/2\) and coefficient \(1/2\) of \(\log\operatorname{cap}(\eta)\).
The regularized finite minima converge by testing fixed trial matrices.
At finite limiting value the estimate \(t\operatorname{Tr}q_t\le f_t-f_0\) controls the correction; at \(-\infty\), its nonnegativity gives the needed bound.
The converse estimate for every admissible \(b\) uses arithmetic--geometric mean and capacity scaling.
No zero-drift minimizer is assumed.

Hermitization doubles the matrix size but introduces no additional square root in the normalized determinant.
At zero drift, the midpoint of \(q\) and \(JqJ\), \(J=\operatorname{diag}(I,-I)\), is fixed by that conjugation, preserves determinant and does not increase the centered quadratic expression.
Its two diagonal blocks give the two-variable capacity expression for the original covariance.
This verifies \(\operatorname{cap}(\Theta)=\operatorname{cap}(\eta_0)^2\), including zero, and the full exponent \(1/(2m)\) in MS24's original formula.

Section 7 also passes direct checks.
The deterministic scalar infimum has value \(\log|a|\) and is \(-\infty\) at zero.
The scalar semicircle derivative has the displayed numerator and selects the proper boundary or larger exterior root.
For the standard circular element, the covariance exchanges the two diagonal entries and kills off-diagonal entries; the scalar trial family produces the disk potential and its exterior logarithm.
The independently known Yin_C_F0123 benchmark and the global comparison together show that other trials cannot improve those exact values.
These checks supplement the general proof and do not replace it.

## Dependencies, Attribution and Review Limits

The precise dependency scopes inspected were:

- Yin_C_F0119's moment recursion, resolvent uniqueness and Cauchy-transform primitive, including its additive constant at large imaginary parameter.
  Its later identification of a centered expression through MS24 is not used.
- Yin_C_F0120's finite coercivity, exponential-path convexity, derivative and minimum characterization.
  Its determinant identity and later MS24 comparison are not needed.
- The existing MS24/FK52 audit of bounded multiplicativity, including singular factors; and the scaling audit's determinant variational identity and change of variables.
  These are resolved source interfaces at the scope used here.
- Yin_C_F0121 only for the final positive-pencil comparison, and Yin_C_F0123 for the established Brown-measure interpretation and derivative interface.
  Neither is an additional premise of the universal infimum.

The source search identifies Speicher's post as the origin of the candidate and records the printed inverse defect.
An AI-generated claim in that post is not used as proof.
The comparison, domain repair and finite capacity reduction are explicitly project deductions.
Publication priority and exhaustive literature novelty have not been reviewed.

The inspected statement covers the core scope of the current Yin_T_F0008 contract: one finite-matrix infimum applies to all selfadjoint drifts and all complex coefficients by hermitization, and its zero-constant specialization gives the full MS24 equality, including degeneracies.
Yin_C_F0121 retains its additional positivity certificate and its own feasible domain.
The new argument makes no unsupported assertion about the complete spectrum of a nonnormal pencil, differentiation of an unattained infimum, or attainment in the strict domain.

This is internal independent mathematical review.
Formal verification, external expert review, publication review and a new manuscript/PDF build were not performed.
The companion's exploratory numerical calculation was not rerun by this reviewer and is not a proof premise.
Goal completion and theorem designation require separate contract and authorization decisions by the coordinating agent; this audit assigns neither.

## Relationship arrangement

The original reviewer supplied the necessary clarification preceding companion equation (9): the commutator terms must first be separated before the inverse products are split.
The inspected corrected complete argument includes that mathematical repair and the disclosed covariance-interface discussion with its authors.
Its combined finding is self-reviewed, despite the separate reviewer identity and independent reconstruction of other steps.
The full original 2026-09-13 reasoning, accepted dependencies and bounds remain unchanged; this original finding supplies no isolated coverage of the corrected complete proof.
The later [R_F0178 complete isolated finding](Yin_R_F0178_v1.md#affine-infimum-whole-proof) checks that proof, including the commutator-first repair, at its own exact input and scope, as selected by [C_F0124](../../claims/Yin_C_F0124_v1.md#decision-isolated-whole-review-adoption).
That later review does not change this original finding's self-reviewed relationship or date.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original finding](#obligations-and-evidence) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original finding](#obligations-and-evidence) | [C_F0124 statement](../../claims/Yin_C_F0124_v1.md#statement) | Complete main Sections 1–7 and global comparison: every finite size and selfadjoint drift, strict Hilbert–Schmidt trial domain, kernel/support corner comparison, admissible physical approximation, finite capacity reduction and arbitrary complex coefficients after hermitization. Includes empty noise, zero determinants and nonattainment; excludes the source’s undefined nonstrict inverse, a general nonnormal spectrum equality and differentiating an unattained infimum. |
| [Original finding](#obligations-and-evidence) | [Global comparison argument](../../claims/Yin_C_F0124_v1.md#affine-hs-variation-tests) | Complete main Sections 1–7 and global comparison: every finite size and selfadjoint drift, strict Hilbert–Schmidt trial domain, kernel/support corner comparison, admissible physical approximation, finite capacity reduction and arbitrary complex coefficients after hermitization. Includes empty noise, zero determinants and nonattainment; excludes the source’s undefined nonstrict inverse, a general nonnormal spectrum equality and differentiating an unattained infimum. |
| [Original finding](#obligations-and-evidence) | [Physical approximation argument](../../claims/Yin_C_F0124_v1.md#3-a-physical-approximating-sequence) | Complete main Sections 1–7 and global comparison: every finite size and selfadjoint drift, strict Hilbert–Schmidt trial domain, kernel/support corner comparison, admissible physical approximation, finite capacity reduction and arbitrary complex coefficients after hermitization. Includes empty noise, zero determinants and nonattainment; excludes the source’s undefined nonstrict inverse, a general nonnormal spectrum equality and differentiating an unattained infimum. |

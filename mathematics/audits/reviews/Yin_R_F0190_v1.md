---
author: Yin
---

# Fixed GUE pencils and polynomial Brown measures: independent whole-chain review

Date: 2026-11-04T17:24 (UTC).
The human record author is Yin.
This initial independent review covers the complete [C_F0186 argument](../../claims/Yin_C_F0186_v1.md#argument) and its consequence for the exact [F0012 contract](../../tasks/Yin_T_F0012_v1.md#contract).
The reviewed artifact is the current fixed candidate with assessment decision-candidate, dated 2026-11-04T17:07, including the clarified upper-half-plane domain in (R).
The candidate was held fixed during the substantive review; the only intervening change was that domain clarification, which was inspected before recording this finding.

The reviewing agent was outside substantive proof development and received the fixed candidate, exact Task, applicable rules and primary-source locators.
No exploration notes, proof-generation dialogue, author explanation of a proof step, strategy, earlier review finding or other agent's mathematical conclusion was supplied or consulted.
The assignment supplied administrative execution facts and identified the existence of the KSS correction without supplying its mathematical conclusion.
The reviewer first inspected the contract and complete candidate and formed its own findings, then checked the directly used primary-source statements and their applicability.
No prior review was relied upon, and the source-audit record linked by the candidate was not used as a substitute for reading the primary sources.
The reviewer supplied no substantive repair.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-chain finding](#whole-chain-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-chain finding](#whole-chain-finding) | [Exact C statement](../../claims/Yin_C_F0186_v1.md#statement) | Every fixed monic matrix-coefficient GUE pencil, its norm-restricted estimate (P), and the scalar-polynomial Brown-measure consequence. |
| [Whole-chain finding](#whole-chain-finding) | [Complete C argument](../../claims/Yin_C_F0186_v1.md#argument) | Complete deterministic compression/error-bound/lifting argument, singular-variety tube passage, Gaussian scaling, linearization, logarithmic cutoff removal and planar convergence. |
| [Whole-chain finding](#whole-chain-finding) | [External C inputs](../../claims/Yin_C_F0186_v1.md#inputs) | Identification, stated hypotheses and actual use of the listed external inputs, including the scope of the KSS correction; original theorem proofs are accepted inputs rather than newly audited proofs. |
| [Whole-chain finding](#whole-chain-finding) | [Exact T contract](../../tasks/Yin_T_F0012_v1.md#contract) | Unperturbed independent normalized GUE, every fixed scalar polynomial in self-adjoint variables including nonnormal evaluations, and convergence in probability against every bounded continuous real test function. |

## Primary sources and acceptance boundary

The following statements were read directly and are accepted as established external inputs at the stated scope.
Their full original proofs were not independently re-audited in this review.
All local adaptations and interfaces in the candidate were checked independently.

| Source and exact inspected locator | Applicability and inspection |
| --- | --- |
| [KSS, arXiv:1412.5088v1, p. 2 (KS2) and p. 5 Corollary 2.1](https://arxiv.org/pdf/1412.5088v1#page=2), local original mathematics/literature/pdf/KSS16--arxiv-v1.pdf | (KS2) is stated for a real polynomial map on the entire real input space, with exponent determined by its input dimension and degree. The candidate's real quadratic maps satisfy these hypotheses. The algebraic-restriction corollary is consistent with that use. The underlying Kurdyka--Spodzieja proof cited by this source was not separately audited. |
| [KSS correction, Discrete & Computational Geometry 62 (2019), pp. 990-991](https://link.springer.com/content/pdf/10.1007/s00454-019-00128-4.pdf) | Both pages were read. The target-dimension amendments concern the general semialgebraic mapping statements in publication Corollary 2.2, Remark 2.4 and Corollary 3.3. They do not amend the polynomial-map (KS2) invoked here. No uncorrected general semialgebraic-map exponent is substituted for this polynomial-map input. |
| [Lotz, arXiv:1210.3742v4, Theorem 1.1, p. 1](https://arxiv.org/pdf/1210.3742v4#page=1), local original mathematics/literature/pdf/Lot15.pdf | Setting the source codimension to one gives exactly (T1). The source permits arbitrary ball centers and radii and bounds the probability using degree and ambient dimension. The candidate first applies it to regular hypersurfaces. |
| [CGP, arXiv:1912.04588v1, pp. 1-2 and Corollary 1.3, p. 5](https://arxiv.org/pdf/1912.04588v1#page=5), local original mathematics/literature/pdf/CGP22--arxiv-v1.pdf | The GUE density normalization agrees with the Task. The introductory moment and norm limits supply the standard GUE inputs. Corollary 1.3 with amplification size one gives the claimed resolvent comparison for the fixed self-adjoint scalar polynomial \(Q_z\), with no normality condition on \(P\). |
| [SS, arXiv:1305.1920v1, Theorem 1.1(5)(6), p. 2, and Corollary 1.2, p. 3](https://arxiv.org/pdf/1305.1920v1#page=2), local original mathematics/literature/pdf/SS15--arxiv-v1.pdf | These provide the algebraic Cauchy transform, local convergent Puiseux behavior and atomlessness for a nonconstant scalar self-adjoint polynomial in free semicircular variables. The positivity and nonconstancy of \(Q_z\) are checked below. |
| [Han26, arXiv:2606.01664v1, Section 1.3, pp. 6-7; Section 2.2, p. 10; Section 5, pp. 32-34](https://arxiv.org/pdf/2606.01664v1#page=7), local original mathematics/literature/pdf/Han26.pdf | Brown-measure/hermitization normalization and the logarithmic-potential passage were inspected. The linearization principle supplies attribution, while the candidate proves its own word-chain formula. Han's Ginibre convergence theorem is not used as a GUE theorem. |

The usual finite-dimensional determinant, Schur-complement and spectral-measure identities, Sard's theorem, and the Brown logarithmic-potential identity are accepted standard inputs in their stated domains.
The review checks their uses here rather than claiming a fresh proof of these foundational results.

## Deterministic estimate

The approximate kernel vector has exactly \(m\) physical components, so its component span \(W\) has dimension \(1\le k\le m\).
The outgoing span is orthogonal to \(W\), has dimension at most \(dk\), and contains every component of \(H_jU-UA_j\).
Consequently (C1) is an equality, and (C2) accounts for the entire residual, including its part outside \(W\).
There is no discarded compression error.

The Hermitian coordinates have real dimension \(k^2\) per matrix, the complex outgoing blocks have dimension \(2\ell k\), and the vector contributes \(2mk\).
These counts give (C3), while the operator-norm cutoff gives (C4).
The coordinate maps depend only on the fixed coefficients and the finite pair \((k,\ell)\), not on physical subspace orientations or \(N\).
The quadratic normalization coordinate makes every zero's vector a unit vector.
No full-rank hypothesis on its component matrix is needed.

(KS2) supplies (C5) with an exponent independent of \(N\).
For an empty zero set, the continuous residual has a positive minimum on the compact coordinate region containing the actual inputs.
Taking a common threshold, exponent and constant over the finite set of types is legitimate.
Types not realizable in a particular physical dimension cause no problem.

The lifted perturbations (C6) are Hermitian and have the asserted action on \(U\mathbb C^k\).
The repaired vector remains supported there, so the unchanged other columns do not affect its exact kernel equation.
The diagonal and two off-diagonal blocks are Hilbert--Schmidt orthogonal, giving the factor two in (C7).
This proves (BE), including a common small-residual threshold.
Neither measurable selection nor a distributional assertion about the adaptive subspaces is used.

## Tubes and the Gaussian estimate

For codimension one, the sum in (T1) is four times the difference of \((1+(2D+1)u)^n\) and \((1+u)^n\), where \(u=\rho/\sigma\).
The derivative bound gives (T2), including its exponential factor.

For the singular-zero-set extension, nonzero nonnegative \(q_N\) is positive somewhere in every neighborhood of each zero.
The finite cover of the relevant compact zero set gives one positive upper bound on the level \(\delta\) valid for all those zero points.
The line segments and intermediate-value theorem supply nearby level points, and a positive regular value can be selected below that bound.
Its level set is a smooth real hypersurface of the same degree bound, so Lotz's theorem applies.
Letting the approximation tolerance tend to zero proves the bound for the original zero set, even in higher real codimension.
This reasoning does not apply the complete-intersection theorem directly to a singular set.

The density calculation (T3) is exact: the ball mixture with \(S\sim\chi_{n+2}\) yields the standard Gaussian density.
The lower-tail event \(S<\sqrt n/2\) is exponentially small, and the complementary radius bound in (T2) gives (T4).

In real Hilbert--Schmidt orthonormal coordinates the Task's GUE density has variance \(1/N\) in every coordinate.
Thus \(n=dN^2\), the singular-input polynomial has degree at most \(2mN\), and its value at the origin is one.
The deterministic perturbation distance becomes \(C\sqrt N\varepsilon^\alpha\) in standard Gaussian coordinates.
These facts give \(N^{5/2}\) in (P) and (T6).
An empty determinant zero set is covered by (BE), not by a distance-to-empty-set convention.
For \(A\alpha>5/2\), the exponential factor stays bounded and the tube probability tends to zero.
A fixed norm cutoff above two removes the GUE exceptional event in probability.
This proves the pencil conclusion without irreducibility or covariance assumptions.

## Linearization and logarithmic tails

For each word, \(Q_w^{-1}\) has exactly the product needed for \(-B_wQ_w^{-1}C_w\).
Block concatenation has Schur complement \(P-z\), and its constant input is \(D_z\).
For \(z\ne P(0)\), left normalization produces a monic pencil of fixed coefficient size.
The inverse root block and the direction of inequality (L) are correct.
Schur-complement equivalence also covers the singular case.
Absorbing the fixed scalar multiplier in the exponent gives (LSV) for each such \(z\).
The finite-\(N\) determinant polynomial is nonzero because its value at the zero tuple is nonzero; exact singularity has probability zero.

For nonconstant \(P\), the highest homogeneous part of \(Q_z=(P-z)^*(P-z)\) is nonzero, so SS's nonconstant scalar hypothesis holds.
The final (R) explicitly restricts to \(\Im w>0\), which agrees with every use of CGP's absolute-imaginary-part bound.
The original domain ambiguity was clarified and the final line rechecked; no estimate or argument changed.

At zero, the Cauchy-transform bound excludes Puiseux powers below \(-1\), and atomlessness excludes the \(-1\) coefficient.
The remaining positive exponent gap yields \(\beta_z>0\).
The scalar kernel bound and (R) give the error \(N^{-2}t^{-4}\).
The condition \(\gamma_z(4+\beta_z)<2\) absorbs that error throughout \(N^{-\gamma_z}\le t\le1\), proving (W).
No later step requires uniformity in \(z\).

On the good event, squared singular values are at least \(N^{-2B_z}\).
The mass below \(N^{-\gamma_z}\), multiplied by \(2B_z\log N\), has expectation tending to zero by (W).
Integration by parts bounds the remaining interval by a quantity tending to zero with the upper cutoff.
If the floor lies above the intermediate scale, the lower interval is empty and the same bound remains valid.
Markov's inequality is used on the good-event contribution; the complementary probability tends to zero by (LSV).
No expectation bound on the exceptional event's untruncated logarithm is needed.
This proves (UI), and the same positive power behavior gives logarithmic integrability for the limit law.

## Planar convergence and the original contract

GUE star-moment convergence and a bounded norm event give weak convergence in probability of each fixed-\(z\) squared-singular-value law.
Bounded continuous logarithmic truncations converge, the norm event removes the upper cutoff, and (UI) removes the lower cutoff.
This gives pointwise-in-\(z\) convergence in probability of potentials outside \(P(0)\).

On the norm event all eigenvalues lie in one fixed disk.
Translated logarithmic kernels have uniformly bounded \(L^2\) norms on each compact planar set for translations in that disk.
The radial integral of \(r|\log r|^2\) is finite at zero.
Jensen gives the uniform \(L^2\) bound for \(u_N\), and the Brown-potential identity gives the corresponding bound for \(u\).
Fubini and dominated convergence apply to the bounded probabilities of pointwise deviations, giving convergence in probability of the area of the deviation set.
Cauchy--Schwarz on that set then gives local \(L^1\) convergence in probability.
This justifies the distributional Laplacian passage; pointwise convergence alone was not substituted for it.

The factor \(1/2\) for squared singular values and \(1/(2\pi)\) for the planar logarithmic kernel agree with the inspected hermitization convention.
The determinant counts eigenvalues with algebraic multiplicity, as the contract requires.
The norm event gives tightness, and smooth approximation on the fixed disk extends convergence to every bounded continuous test function.
Excluding one point from the potential argument does not omit an atom from the resulting distributional measure identity.
Constant \(P\) gives the same point mass on both sides.
All temporary restrictions are discharged: every fixed \(d,P\) is covered, nonnormal evaluations are permitted, the ensemble remains unperturbed GUE, and the conclusion is exactly weak convergence in probability.

## Whole-chain finding

The independently inspected final candidate contains a complete argument for its pencil bound and the exact F0012 assertion, relying on the accepted established external theorems identified above.
No unresolved substantive mathematical gap or failed implication was found in the complete chain.
The source statements, relevant correction scope and application hypotheses checked here support those uses; the original source proofs remain outside this review.
The final domain clarification in (R) has been checked and leaves no outstanding qualification on an actual use.
This finding can support the corresponding Claim assessment and Task completion through its declared bindings; their responsible decisions still own adoption.

This is an agent mathematical review of the fixed argument, not proof-assistant verification, external peer review, a priority determination or a proof of the cited source theorems.
No almost-sure convergence, uniformity in \(z\), extension to other ensembles or broader statement is certified.

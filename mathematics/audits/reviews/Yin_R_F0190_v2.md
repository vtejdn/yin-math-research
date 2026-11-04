---
author: Yin
---

# Affine GUE pencil determinants: independent whole-proof review

Review time: 2026-11-04T18:00, in UTC minutes.
The human record author is Yin.
This is a separately organized independent agent review of the fixed affine statement and argument in [C_F0186 v2](../../claims/Yin_C_F0186_v2.md#statement), including its declared inputs.
The reviewer took no part in the substantive development or repair of this proof.
Only the fixed proof artifacts, necessary dependencies, assignment scope, applicable rules and administrative repository facts were supplied.
No exploration notes, proof-generation dialogue, author explanations or previous review conclusions were supplied or consulted before the finding below was formed.
No previous review finding is relied on here.

## Inputs

[Affine statement](../../claims/Yin_C_F0186_v2.md#statement) supplies the complete hypotheses, both limits, the conditional singular-value conclusions and the normalization conventions.
[Affine argument](../../claims/Yin_C_F0186_v2.md#argument) supplies the proof through its zero-limit, rank, repair, Gaussian-tube, logarithmic-tail and cutoff-removal sections.
[Declared source scope](../../claims/Yin_C_F0186_v2.md#inputs) identifies its external and local dependencies.
[Polynomial distance argument](../../claims/Yin_C_F0186_v1.md#error-bound) and [Gaussian tube argument](../../claims/Yin_C_F0186_v1.md#tubes) supply the particular v1 geometric inputs used in v2.
[Ordinary determinant convention](../literature/MS24/Yin_U001.md#determinant-convention) fixes the normalized trace and inclusion of zero spectral mass.
The review reads those mathematical inputs directly, without adopting the earlier review of v1 or reviewing its separate scalar-polynomial application.
The v2 candidate was held fixed during this inspection.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole affine proof finding](#independent-affine-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole affine proof finding](#independent-affine-proof) | [Affine statement](../../claims/Yin_C_F0186_v2.md#statement) | All fixed-coefficient hypotheses, extended-real logarithmic and determinant-root limits, positive-determinant floor and cutoff tube estimate, degenerate cases and trace normalization. |
| [Whole affine proof finding](#independent-affine-proof) | [Affine argument](../../claims/Yin_C_F0186_v2.md#argument) | Complete logical chain from weak convergence through the zero-limit, generic-rank, affine-repair, affine-tube, logarithmic-tail and determinant-limit sections. |
| [Whole affine proof finding](#independent-affine-proof) | [Declared inputs](../../claims/Yin_C_F0186_v2.md#inputs) | Exact external statements and applicability, local geometric dependencies and accepted source-proof boundaries. |
| [Whole affine proof finding](#independent-affine-proof) | [v1 polynomial error bound](../../claims/Yin_C_F0186_v1.md#error-bound) | The stated KSS inequality, bounded-coordinate consequence, empty-zero-set alternative and Hermitian lifting mechanism used by v2. |
| [Whole affine proof finding](#independent-affine-proof) | [v1 Gaussian tube bound](../../claims/Yin_C_F0186_v1.md#tubes) | Lotz specialization, regular-level extension to a nonzero nonnegative polynomial, Gaussian mixture and estimate (T4), without requiring a nonzero value at the origin. |
| [Whole affine proof finding](#independent-affine-proof) | [Determinant convention](../literature/MS24/Yin_U001.md#determinant-convention) | Only the ordinary logarithmic spectral-integral definition, normalized amplification and treatment of zero spectral mass; no other MS24 result is adopted by this binding. |

<a id="independent-affine-proof"></a>
## Whole affine proof finding

The reviewed argument establishes the complete v2 statement within its accepted external-theorem boundary.
No unresolved mathematical gap was found in the stated hypotheses, quantifiers, local adaptations or dependency interfaces.
The statement includes singular constant coefficients and zero limiting determinants, and does not require a scalar evaluation at which the pencil is invertible.
The positive-determinant assumption is used only for the polynomial floor and the finite-logarithm branch of the proof.
This finding does not select a Claim assessment or alter any Task contract.

### Primary statements and applicability

The following passages were read in the actual retained originals.
Their stated mathematical inputs are accepted here, without claiming an independent audit of their complete original proofs.

| Source and inspected passage | Matched input and use |
| --- | --- |
| [DM17 published original](../../literature/pdf/DM17.pdf), journal pp. 45 and 49, Definitions 2.1--2.2 and Proposition 2.3 | The field is infinite, as required for the application over the complex numbers; the maximum rank of a square tensor blow-up is a multiple of its blow-up size. This is not a divisibility statement for every member of that matrix space. |
| [KSS16 arXiv v1](../../literature/pdf/KSS16--arxiv-v1.pdf), p. 2, (KS2), with p. 5, Corollary 2.1, as contextual confirmation | The global real polynomial-map distance inequality has exponent D(6D-3)^(p-1); the affine compression maps have real degree two and bounded input coordinates. The zero set is assumed nonempty at this use. |
| [Lot15 arXiv v4](../../literature/pdf/Lot15.pdf), p. 1, Theorem 1.1 | The codimension-one complete-intersection specialization gives (T1). The regular positive levels used locally are smooth hypersurfaces of the same degree bound. |
| [SS15 arXiv v1](../../literature/pdf/SS15--arxiv-v1.pdf), pp. 1--2, Theorem 1.1(5)(6) | The theorem applies to a self-adjoint matrix of noncommutative polynomials in free semicircular variables, including \(Q=L^*L\) with fixed matrix coefficients; it supplies the algebraic Cauchy transform and convergent local Puiseux expansion. No scalar atomlessness statement is substituted. |
| [CGP22 arXiv v1](../../literature/pdf/CGP22--arxiv-v1.pdf), pp. 1 and 3--5, especially Corollary 1.3 | The GUE density agrees with the candidate normalization. The corollary allows fixed deterministic matrices and their adjoints and supplies the N^(-2) resolvent error with imaginary-part powers -5 and -2. The fixed amplification factor m^2 is absorbed into the coefficient-dependent constant. |

The standard joint GUE moment and norm limits are accepted inputs, also consistent with CGP22's introductory normalization and Theorem 1.2 with no additional deterministic tuple.
Basic spectral functional calculus, the polynomial identity principle, nullity of a nonzero real polynomial's zero set, and Sard's theorem in the regular-level argument are the usual foundational inputs at their stated scopes.
The original IQS proof behind DM17 Proposition 2.3 was not re-proved.
No unresolved source-identification or applicability issue was found for the substantive theorem inputs actually used.
This source check is not a novelty search or a claim about priority.

### Weak convergence, the zero branch and eventual full rank

The normalization of the empirical measure of \(L_N^*L_N\) is \(1/(mN)\), so one half of its logarithmic integral is exactly \(U_N\).
Fixed coefficients, joint GUE moment convergence and a norm event whose probability tends to one give weak convergence in probability of these measures.
Bounded continuous test functions then give weak convergence of their deterministic expectations.
For fixed positive regularization, the logarithm is bounded on the common spectral compact set on that norm event.
Consequently the regularized logarithms converge in probability, and monotone removal of the regularization proves the claimed extended-real convergence when u is minus infinity.
That branch needs no lower singular-value estimate.

For finite u, zero spectral mass is absent.
The maximum-rank locus of the homogeneous coefficient pencil intersects the locus where its zeroth variable is invertible, because these are nonempty Zariski open subsets of one complex affine space.
Right multiplication by that variable's inverse proves equality of the homogeneous blow-up rank and the affine maximum rank r_N.
DM17 therefore makes r_N a multiple of N.
A real Hermitian basis is a complex basis of the whole matrix algebra, so restriction to Hermitian tuples does not annihilate a nonzero maximum-rank minor.
The absolutely continuous GUE tuple attains r_N almost surely.
If infinitely many sizes were deficient, the expected squared-singular-value measures would have a zero atom of mass at least 1/m along that subsequence.
Portmanteau for the closed set consisting of zero would force the limiting measure to have such an atom, contradicting finite u.
Thus the affine determinant is a nonzero polynomial and the random pencil is almost surely invertible at every sufficiently large size.
No noncommutative-rank conclusion or finite-size invertibility is assumed in this deduction.

### Uniform geometric repair and Gaussian tubes

The physical component span of an approximate kernel has dimension at most m, and the outgoing component span has dimension at most dm.
The constant matrix acts on coefficient indices and leaves the physical component span invariant, which verifies the absence of an outgoing A_0 term.
The two orthogonal residuals and the unit-vector equation are exactly a degree-two real polynomial system.
Its coordinate dimension is at most m^2(2d^2+d+2), and its squared coordinate norm is at most 2dkM^2+1.
These bounds depend on the fixed coefficients and cutoff, but not on N or the orientations of the two subspaces.

For each nonempty zero set, the checked KSS input yields a nearby exact solution.
For an empty zero set, continuity on the bounded closed coordinate region excludes sufficiently small residuals.
There are only finitely many dimension types, so one positive exponent and one residual threshold work for every N.
Lifting the corrected coordinates through the original isometries preserves Hermitian symmetry and gives the displayed Hilbert--Schmidt estimate and an exact unit kernel vector.
The construction is deterministic, so no measurable choice of the adaptive subspaces is needed.

The regular-level argument in v1 was checked directly for any nonzero nonnegative polynomial.
Near every zero there is a positive value; a finite cover of the relevant compact zero set and the intermediate value theorem give uniform approximation by one sufficiently small regular positive level.
Sard's theorem supplies such levels, and Lotz's bound is uniform in their choice.
Passing the approximation radius to zero therefore covers singular zero sets and zero sets of larger real codimension.
The argument uses nonidentity of the polynomial, not its value at the origin.

The Gaussian density is exactly the mixture of uniform-ball densities with radius distributed as chi with n+2 degrees of freedom.
Conditioning that radius to be at least sqrt(n)/2 turns the ball estimate into (T4), with an exponentially small lower-tail error.
For n=dN^2, determinant degree at most 2mN, and repair radius C sqrt(N) epsilon^alpha, the factor D sqrt(n) times the radius is bounded by a constant times N^(5/2) epsilon^alpha.
This proves (A), and choosing B alpha greater than 5/2 proves (F) on a GUE norm event with probability tending to one.
If the singular set is empty, the deterministic repair excludes the small-residual event itself.
A nonzero constant determinant polynomial is covered by that case.

### Resolvent scale, logarithmic tails and final normalization

After tensor-factor interchange, Q_N is a scalar self-adjoint noncommutative polynomial in the GUE variables and the fixed coefficient matrices and their adjoints, so CGP22 Corollary 1.3 applies exactly as stated.
The free comparison is Q under the normalized trace tau_m.
SS15 supplies the local Puiseux expansion for its Cauchy transform.
The general bound \(|G_Q(it)|\le1/t\) on the positive imaginary axis excludes powers below -1, and \(itG_Q(it)\to\nu(\{0\})=0\) excludes a term of order -1 here.
The remaining expansion therefore gives the stated positive exponent beta, with beta at most one.

For the nonnegative spectral variable, the indicator bound on [0,t] converts the transform estimate into
\[
 \mathbb E\nu_N([0,t])\le C\bigl(t^\beta+N^{-2}t^{-4}\bigr).
\]
The omitted N^(-2)t^(-1) term is smaller on 0<t<=1.
For t at least N^(-gamma), the choice gamma(4+beta)<2 absorbs the error term into t^beta uniformly.
On the polynomial-floor event, the logarithmic contribution below N^(-gamma) is at most 2B log(N) times the mass below that threshold, whose expected upper bound tends to zero.
Layer integration on the interval between N^(-gamma) and epsilon gives the stated C epsilon^beta(1+|log epsilon|) bound.
Markov's inequality and the vanishing probability of failure of the floor event establish (UI).
No expectation of the untruncated logarithm on the complementary event is needed, and eventual almost-sure nonsingularity removes any uncounted atom at zero.

The bounded continuous logarithmic truncation converges by weak convergence.
A fixed upper cutoff is valid on the norm event, and (UI) removes the lower cutoff in probability.
The same Puiseux estimate controls the limiting logarithmic tail.
This proves the finite-u logarithmic limit, and continuity of exponentiation gives the root-determinant limit; the zero branch already gives the same conclusion when u is minus infinity.
Replacing 1/(mN) by 1/N raises the limiting ordinary determinant to the mth power.
The stated factor for invertible A_0 agrees with the normalized finite-matrix determinant, and no factorization is used for singular A_0.
The fully deterministic case, including singular A_0, satisfies the statement directly.

### Scope and remaining limits

No mathematical or source-applicability repair is required by this review for the exact v2 statement and the geometric inputs listed above.
The finding concerns the complete affine determinant theorem, not the separate v1 scalar-polynomial application, a variational formula for the limiting determinant, or a new Task completion.
It establishes no convergence of logarithmic expectations, complex determinant phases, almost-sure convergence, growing-coefficient result or other ensemble extension.
There was no proof-assistant formal verification, and no original external-theorem proof was audited in full.
The record supplies actual project-level independent review evidence within those limits, not publication acceptance or a priority claim.

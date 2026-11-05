---
author: Yin
---

# Almost-sure and mean determinant convergence: independent whole-proof review

Date: 2026-11-04T18:45, UTC.
Human record author: Yin.
This is a separately organized independent review of the fixed C_F0186_v3 candidate and its exact F0012 v2 completion scope.
The reviewer was outside substantive proof development and received the fixed statements, arguments, necessary dependencies, applicable rules and administrative assignment.
No development discussion, working draft, earlier R finding or other agent verdict was supplied or consulted before forming this finding.
The directly needed source units were consulted as mathematical input records, and the primary passages listed below were opened in the retained PDFs.
The prior C versions were read for their actual arguments and interfaces; their existing assessment labels were not used as a substitute for checking them.

The inspected candidate is [C_F0186_v3](../../claims/Yin_C_F0186_v3.md#statement), at its `strong-candidate` revision, including the complete argument and declared source scope.
The reviewed goal is the [F0012 v2 contract](../../tasks/Yin_T_F0012_v2.md#contract).
This review covers all strengthened affine conclusions, the displayed global small-ball estimate, the optional direct free determinant identity, and the full scalar Brown-measure conclusion.
It records a mathematical review, not a C assessment or T lifecycle decision.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof and contract finding](#independent-strong-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof and contract finding](#independent-strong-proof) | [Strengthened statement](../../claims/Yin_C_F0186_v3.md#statement) | Every stated affine convergence mode, finite and minus-infinite limits, the global small-ball estimate, determinant-root moments, and almost-sure scalar Brown-measure convergence under arbitrary cross-size couplings. |
| [Whole-proof and contract finding](#independent-strong-proof) | [Complete strengthened argument](../../claims/Yin_C_F0186_v3.md#argument) | All local estimates, limit passages, boundary cases, source interfaces and the complete Brown-measure transfer, including the alternative bounded determinant identity. |
| [Whole-proof and contract finding](#independent-strong-proof) | [Declared inputs](../../claims/Yin_C_F0186_v3.md#inputs) | Exact uses of the prior versions and the retained external statements, with the source-proof acceptance boundary below. |
| [Whole-proof and contract finding](#independent-strong-proof) | [Exact reactivated contract](../../tasks/Yin_T_F0012_v2.md#contract) | Full-sequence weak convergence on one probability-one event for each fixed scalar polynomial and each allowed coupling; the associated affine strengthening is separately checked at C_v3. |
| [Whole-proof and contract finding](#independent-strong-proof) | [Affine probability statement](../../claims/Yin_C_F0186_v2.md#statement) | The complete affine probability theorem, its finite-limit singular-value estimate, and its extended-real normalization as inputs to v3. |
| [Whole-proof and contract finding](#independent-strong-proof) | [Affine argument](../../claims/Yin_C_F0186_v2.md#argument) | Weak singular-value convergence, generic rank, affine compression and Hermitian lifting, Gaussian tubes, logarithmic tails and probability-limit normalization. |
| [Whole-proof and contract finding](#independent-strong-proof) | [Affine input scope](../../claims/Yin_C_F0186_v2.md#inputs) | Applicability of rank regularity, the v1 geometric inputs and the matrix-valued CGP22/SS15 statements. |
| [Whole-proof and contract finding](#independent-strong-proof) | [Mesoscopic counting input](../../claims/Yin_C_F0186_v2.md#logarithmic-tail) | The absence of a zero atom for finite free logarithm, Puiseux decay, the normalized resolvent error and the bound on the full interval from the moving cutoff to one. |
| [Whole-proof and contract finding](#independent-strong-proof) | [Original pencil and polynomial statement](../../claims/Yin_C_F0186_v1.md#statement) | The monic pencil floor and scalar polynomial probability convergence retained as direct starting support in the Task. |
| [Whole-proof and contract finding](#independent-strong-proof) | [Original argument](../../claims/Yin_C_F0186_v1.md#argument) | The complete compression, tube and scalar-polynomial probability argument at the declared external-input boundary. |
| [Whole-proof and contract finding](#independent-strong-proof) | [Polynomial error bound](../../claims/Yin_C_F0186_v1.md#error-bound) | The exact real KSS inequality and the dimension-independent bounded-coordinate Hermitian repair. |
| [Whole-proof and contract finding](#independent-strong-proof) | [Uniform-ball and Gaussian tubes](../../claims/Yin_C_F0186_v1.md#tubes) | Lotz's codimension-one specialization, extension to singular nonnegative polynomial zero sets, exact radial Gaussian mixture and the original polynomial floor. |
| [Whole-proof and contract finding](#independent-strong-proof) | [Scalar polynomial application](../../claims/Yin_C_F0186_v1.md#polynomial-application) | Exact word-chain linearization, finite determinant identity, fixed-shift finite logarithmic probability limit and Brown-potential normalization. |
| [Whole-proof and contract finding](#independent-strong-proof) | [Ordinary determinant convention](../literature/MS24/Yin_U001.md#determinant-convention) | Normalized matrix trace, inclusion of a zero atom, and the nonnegative root determinant convention used throughout. |
| [Whole-proof and contract finding](#independent-strong-proof) | [Bounded multiplicativity input](../literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation) | The retained bounded product theorem and finite-tracial adaptation used only by the optional direct linearization identity. |

<a id="independent-strong-proof"></a>
## Whole-proof and contract finding

The complete argument supports every conclusion of C_F0186_v3 under its stated accepted external inputs.
The Brown-measure conclusion satisfies the exact mathematical completion criterion of T_F0012_v2.
No unresolved mathematical dependency or failed implication was found in the inspected chain.
This conclusion makes no novelty or priority determination and is not formal verification.

### Prior arguments and their interfaces

The affine rank step is valid over the infinite field of complex numbers.
The maximum-rank locus intersects the open condition that the homogeneous constant variable is invertible; right multiplication then identifies homogeneous blow-up rank with affine maximum rank.
Hermitian matrices form a real form whose complexification is the entire matrix space, so polynomial density transfers that generic rank to the GUE input.
Rank divisibility by \(N\) converts any non-full generic rank into zero mass at least \(1/m\).
Weak convergence of the expected squared-singular-value laws and the closed-set Portmanteau inequality rule out infinitely many such sizes when the free logarithm is finite.
The conclusion is eventual nonidentity of the determinant, not an unsupported assertion that every blow-up matrix has divisible rank.

The compression retains the whole residual in the orthogonal spaces \(W\) and \(W_{\rm out}\).
The coordinate dimensions depend only on the fixed coefficient sizes, the normalization coordinate prevents a zero repaired vector, and the explicit lift changes Hermitian matrix blocks with the asserted Frobenius cost.
The dependence of the physical subspaces on a witness introduces no probability conditioning or measurable-selection assumption.
The finite family of coordinate maps remains the same when the norm cutoff varies.

The Lotz specialization has the correct codimension-one binomial factors.
For a nonzero nonnegative polynomial, the finite-cover and regular-value construction places every relevant zero near a smooth positive level set with the same degree bound.
The resulting tube inclusion is sufficient before the tolerance tends to zero, including singular zero sets and sets of higher real codimension.
Empty zero sets and nonzero constant polynomials are separately harmless.

The CGP22 comparison uses fixed matrix amplification with its normalized trace.
The squared affine pencil is a self-adjoint matrix-valued polynomial, so the SS15 matrix-valued algebraicity and local Puiseux statements apply.
Finite free logarithm supplies the missing zero-atom exclusion; scalar atomlessness is not imposed on the matrix-valued law.
The resolvent bound excludes powers below \(-1\), the zero-atom limit removes the \(-1\) term, and the remaining Puiseux powers give \(0<\beta\le1\).
The CGP error is of order \(N^{-2}t^{-4}\) after the counting-kernel factor, so \(\gamma<2/(4+\beta)\) gives the stated uniform mesoscopic interval bound.
The original v1 scalar application additionally has a nonconstant self-adjoint squared polynomial and uses the inspected scalar atomlessness statement.
These facts justify its finite fixed-shift logarithmic probability limit.

### Global tail and expectation strengthening

The Gaussian radial mixture has chi distribution with \(n+2\) degrees of freedom.
Its negative moments through order \(n\) are finite, and the displayed gamma-function lower bound and monotonicity of probability-space \(L^p\) norms give the asserted uniform bound of order \(n^{-k/2}\) for the \(k\)-th negative moment.
Expanding the finite nonnegative binomial polynomial before averaging is essential and is carried out correctly.
The resulting Gaussian tube estimate has no additive exceptional probability independent of the radius.

For a nonempty compressed zero set, global KSS yields the repair factor \(1+M^2\) times a fixed positive power of the residual.
For an empty type, the auxiliary map \(G(x,y)\) has exactly the zero set \(\mathbb R^p\times\{0\}\), and its KSS application at \((x,1)\) gives the stated polynomial lower bound on the residual.
The degree-three exponent and the extra input coordinate give \(E=3\cdot15^p\).
With \(\theta\le\min(a/2,1/(2E_*))\), the moving cutoff excludes every empty type for sufficiently small \(\varepsilon\) and leaves a strictly positive repair exponent \(b=a-\theta\).
All thresholds are common across the finite list of types and independent of \(N\).

The elementary net argument has the correct ambient real dimension \(2N\) and variance \(1/N\) for each quadratic form.
Its displayed estimate holds for \(M\ge9\), gives summable fixed-cutoff failures and supplies uniform moments of every fixed positive order.
Combining it with the repaired distance in Gaussian coordinates, \(n=dN^2\) and determinant degree at most \(2mN\) gives the factor \(N^{5/2}\).
The remaining norm error decays faster than any fixed power of \(\varepsilon\), which proves the claimed global small-ball range including its condition \(N^{5/2}\varepsilon^b\le1\).

The expected lower logarithmic tail is controlled on all three intervals.
Below \(N^{-2B}\), integrating the global tail gives order \(N^{5/2-Bb}\); between that scale and \(N^{-\gamma}\), monotonicity gives order \((\log N)N^{-\gamma\beta}\); above it, the mesoscopic bound integrates to the stated \(\varepsilon\) tail.
The choices \(Bb>5/2\) and \(2B>\gamma\) make these deductions valid simultaneously.
Tonelli is applied to nonnegative functions, and eventual exact nonsingularity was already proved, so integrability is a consequence of the bounds rather than an assumption about exceptional events.
The uniform norm moments control the upper logarithmic tail.
Bounded truncations then prove \(L^1\) convergence and convergence of expectations for finite \(u\).

For \(u=-\infty\), the positive part has uniformly bounded expectation and each regularization is bounded below and uniformly integrable above.
Its probability limit therefore also gives convergence of its expectation.
The inequality \(U_N\le U_{N,\delta}\), followed by \(\delta\downarrow0\), proves extended expectation convergence to \(-\infty\) without invoking an undefined \(L^1\) distance.
The root determinant is bounded by the pencil norm, so its probability convergence and uniform moments of an order greater than each prescribed \(p\) give the claimed \(L^p\) convergence, also when the limit is zero.

### Almost-sure affine convergence

The elementary singular-value proof correctly bounds the doubly substochastic weights arising from two singular-value decompositions.
Its Frobenius inequality supplies the factor \(1/\sqrt{mN}\) for the normalized singular-value average.
Together with the affine Gaussian-coordinate factor \(N^{-1/2}\), this gives Lipschitz constant \(\kappa_A\operatorname{Lip}(f)/(\sqrt m N)\), hence Gaussian concentration with \(N^2\) in the exponent.
The estimate is global and requires no norm-event extension.

For a fixed regularizer, the concentration errors are summable, while the expected regularized logarithm has the free limit by uniform integrability.
A countable sequence of regularizers therefore proves the almost-sure minus-infinite branch.
For finite \(u\), the old tube bound with \(B\alpha>7/2\) and the fixed norm estimate give a summable singular-value floor.
The smoothed small-mass statistic has Lipschitz constant of order \(t^{-1/2}\), and at \(t=N^{-\gamma}\) its concentration exponent is \(N^{2-\gamma(1+2\beta)}\).
It is a positive power because \(\beta\le1\) and \(\gamma(4+\beta)<2\).
Thus the mass at the moving cutoff is eventually of order \(N^{-\gamma\beta}\) almost surely.

The clipped logarithm has the same \(t^{-1/2}\) Lipschitz scale, so its centered fluctuations tend to zero almost surely along the whole sequence.
Its means converge by the mesoscopic layer integral and then by sending a fixed cutoff to zero.
On the eventual singular-value floor, its difference from \(U_N\) is bounded by \(B\log N\) times the mass below the moving cutoff, which tends to zero almost surely.
All uses of Borel--Cantelli are its first lemma; no independence across sizes enters.
The completely deterministic pencil is handled directly, including singular constant matrices.

### Linearization, one event and the exact contract

The word-chain auxiliary block is unit upper triangular, its inverse is polynomial, and Schur elimination gives the finite determinant equality with no missing size or determinant factor.
The normalized affine logarithm must be multiplied by the fixed block size \(q\) to equal the scalar normalized logarithm.
The v1 fixed-shift probability limit and the v2 affine probability theorem consequently identify the free affine logarithm with \(u_P(z)/q\).
This comparison precedes and does not assume almost-sure convergence, so the implication is acyclic.
The alternative bounded-operator factorization is also valid: each bounded unit triangular factor is similar to factors tending to the identity, multiplicativity preserves its determinant under similarity, and the normalized direct-sum trace supplies weight \(1/q\).
No inverse of \(P(s)-z\) or division by a zero determinant is used.

For each fixed \(z\ne P(0)\), the affine almost-sure result gives the scalar potential limit.
Joint measurability and Fubini on countably many disks give one event on which this holds for planar almost every \(z\).
The single excluded point has no effect.
A separate summable norm event gives eventual common deterministic compact support for the finite spectra; the Brown support is also bounded by the operator norm.
Translated logarithmic kernels are uniformly square integrable on each compact planar set, so Jensen and the Brown-potential identity give the required \(L^2\) bounds.
Almost-everywhere potential convergence then gives convergence in planar measure, and the displayed Cauchy--Schwarz estimate upgrades it to local \(L^1\) convergence on that same event.
The distributional Laplacian identity and pathwise smooth approximation on the common compact support yield weak convergence against every bounded continuous real test function on the event.
There is no uncountable intersection of probability-one events.
Constant polynomials give the same point mass at all sizes.
The event may depend on the fixed polynomial and coupling, exactly as permitted by the Task.

### Source inspection and acceptance boundary

The following primary statements were checked in the retained originals, including their stated domains and the current applications.

| Source | Directly inspected passage | Role and boundary |
| --- | --- | --- |
| [KSS16 original](../../literature/pdf/KSS16--arxiv-v1.pdf) | PDF p. 2, (KS2) | Real polynomial-map global distance inequality, including its input-dimension exponent; accepted theorem, original proof not re-audited. |
| [Lot15 original](../../literature/pdf/Lot15.pdf) | PDF p. 1, Theorem 1.1 | Complete-intersection uniform-ball tube estimate; accepted source theorem, with the singular-zero-set extension checked locally. |
| [DM17 original](../../literature/pdf/DM17.pdf) | PDF pp. 1 and 6, Definitions 2.1-2.2 and Proposition 2.3 | Infinite-field setting and maximum blow-up rank divisibility; the underlying IQS proof is accepted. |
| [CGP22 original](../../literature/pdf/CGP22--arxiv-v1.pdf) | PDF pp. 5, 10 and 30-31, Corollary 1.3, Proposition 2.11, Proposition 4.4 and Gaussian coordinates | Fixed-amplification resolvent comparison, norm tail and Gaussian concentration; source proofs and the cited general concentration proof are not newly audited. |
| [SS15 original](../../literature/pdf/SS15--arxiv-v1.pdf) | PDF pp. 1-3, Theorem 1.1 and Corollary 1.2 | Matrix-valued algebraicity/Puiseux input and the separate scalar atomlessness application; underlying source proofs are accepted. |
| [Mec19 original](../../literature/pdf/Mec19.pdf) | PDF p. 47, Corollary 4.39 and its displayed proof | Exact singular-value perturbation attribution checked; the candidate's elementary Frobenius proof was independently checked, without auditing all earlier majorization theorems. |

The retained [ordinary determinant convention](../literature/MS24/Yin_U001.md#determinant-convention), [bounded multiplicativity input](../literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation) and [Brown-measure convention](../literature/BZ22/Yin_U001.md#brown-measure-convention) were checked at their actual stated scope.
The optional determinant argument uses the retained bounded product theorem; this review does not claim a new inspection of the original FK52 scan.
Standard GUE star-moment convergence, Brown-potential existence and support facts, spectral functional calculus, elementary polynomial zero-set facts, Tonelli/Fubini and first Borel--Cantelli remain accepted foundational inputs in their stated domains.
The relevant erratum was consulted and contains no objection affecting the selected geometric, affine or scalar GUE proof chain; the Ginibre-specific corrections are not used to establish a GUE theorem here.
No source-proof audit beyond the disclosed scope, machine formalization, experimental certificate or priority search is claimed.
The main agent retains responsibility for actual C/T adoption and navigation updates.

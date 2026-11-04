---
author: Yin
---

# Separate whole-chain review of the fixed GUE-pencil candidate

Date of review: 2026-11-04T17:21 UTC.
Human record author: Yin.
This review concerns the complete fixed candidate [Yin_C_F0186_v1](../../claims/Yin_C_F0186_v1.md#argument), whose selected candidate assessment is dated 2026-11-04T17:07, and the original [F0012 contract](../../tasks/Yin_T_F0012_v1.md#contract).
The candidate was uncommitted during the initial inspection.
A bounded recheck at 2026-11-04T17:23 UTC includes the subsequent explicit domain clarification \(\Im w>0\) in its displayed resolvent estimate (R).
The source estimate uses absolute imaginary parts, and every application in the candidate takes \(w=it\) with \(t>0\), so this clarification preserves the reviewed reasoning and conclusion.
The mathematical finding below covers those exact physical versions with this domain clarification, not a later substantive revision or an enlarged contract.

## Arrangement and inputs

The reviewing agent was initially supplied the fixed candidate, original Task and applicable rules, without proof-development dialogue or draft material.
It read the candidate and Task before checking the original sources and forming its findings.
During the review, an agent-inventory call unexpectedly displayed a completed development agent's short summary mentioning compression, the Lojasiewicz repair, Hermitian lifting, the Lotz/Gaussian mixture, the scaling factor and a separate positive-trace direction.
No draft, development dialogue or previous review record was opened.
This exposure prevents an independent classification under the current review rules.
The relationship is therefore recorded as self-reviewed, meaning a separate but non-independent agent inspection; this finding does not discharge an independent-review obligation.

The project inputs are the [exact statement](../../claims/Yin_C_F0186_v1.md#statement), [complete argument](../../claims/Yin_C_F0186_v1.md#argument) and [original contract](../../tasks/Yin_T_F0012_v1.md#contract).
No prior project review was relied on.
External statements were checked directly in the source documents identified below.
The source theorem proofs were accepted within their stated scope and were not fully re-audited.
The review includes the project's own adaptations, dimension and degree dependence, probability estimates, linearization, logarithmic cutoff removal and final convergence against the Task.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-chain finding](#whole-chain) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-chain finding](#whole-chain) | [C_F0186 exact statement](../../claims/Yin_C_F0186_v1.md#statement) | Arbitrary fixed complex coefficient matrices in monic GUE pencils, the stated norm-restricted quantitative bound, and every fixed scalar polynomial in the Task ensemble. |
| [Whole-chain finding](#whole-chain) | [C_F0186 complete argument](../../claims/Yin_C_F0186_v1.md#argument) | Entire retained argument, including every local adaptation and the accepted external inputs at the inspection depth recorded here. |
| [Whole-chain finding](#whole-chain) | [F0012 original contract](../../tasks/Yin_T_F0012_v1.md#contract) | All fixed d and scalar P, possibly non-self-adjoint, unperturbed normalized independent GUE, algebraic eigenvalue multiplicities and weak convergence in probability against each bounded continuous real test function. |

## External statements and applicability

The [Kurdyka--Spodzieja--Szlachcinska preprint, arXiv:1412.5088v1, p. 2, (KS2)](https://arxiv.org/pdf/1412.5088v1#page=2) gives the real polynomial-map distance inequality with exponent \(D(6D-3)^{p-1}\).
The map is defined on all of real input space; no isolated-zero or target-dimension restriction is imposed.
The same input was traced to [Kurdyka--Spodzieja, Proceedings of the AMS 142 (2014), Corollary 10, printed p. 3100](https://scispace.com/pdf/separation-of-real-algebraic-sets-and-the-lojasiewicz-5gutm7h1kr.pdf#page=12), in a copy of the published original.
The candidate's maps have degree exactly two because their normalization coordinate is quadratic.
Their source dimension is \(p_{k,\ell}\), independent of the matrix size.
The [2019 correction, pp. 990--991](https://link.springer.com/content/pdf/10.1007/s00454-019-00128-4.pdf) was read in the publisher PDF.
It adds target dimension to the graph-based semialgebraic-map estimates in published Corollaries 2.2 and 3.3 and the associated remark.
It does not amend the separately cited polynomial-map (KS2) or the 2014 Corollary 10.
The polynomial-map statement is accepted here; its original proof is not a reviewed project lemma.

The [Lotz preprint, arXiv:1210.3742v4, Theorem 1.1, p. 1](https://arxiv.org/pdf/1210.3742v4#page=1) has exactly the binomial-degree bound used after setting codimension to one.
Section 4.2, p. 11, defines its complete intersections through linear independence of the defining gradients.
Thus a nonempty regular level of the real polynomial \(q_N\) satisfies the source hypothesis.
The candidate does not apply that smooth hypothesis directly to the possibly singular zero set.
The source theorem and definition are accepted; its curvature and integral-geometric proof was not fully reviewed.

The [Collins--Guionnet--Parraud preprint, arXiv:1912.04588v1, Corollary 1.3, p. 5](https://arxiv.org/pdf/1912.04588v1#page=5) supplies the expected Stieltjes-transform comparison with \(M^2N^{-2}\) and powers \(|\Im w|^{-5}+|\Im w|^{-2}\).
Set the amplification dimension to one and the fixed self-adjoint polynomial to \(Q_z\).
Its GUE normalization on p. 1 matches the Task.
Theorem 1.2, p. 4, with a scalar deterministic companion, together with Definition 2.1, p. 7, also supplies the needed star-moment and norm convergence.
The free variables there are variance-one semicirculars.
These source statements are accepted; their original proofs were not re-audited.

The [Shlyakhtenko--Skoufranis preprint, arXiv:1305.1920v1, Theorem 1.1(5)(6) and Corollary 1.2, p. 2](https://arxiv.org/pdf/1305.1920v1#page=2) supplies an algebraic Cauchy transform, a local meromorphic expansion in a root coordinate, and atomlessness for a nonconstant self-adjoint scalar polynomial of free semicirculars.
These assumptions apply to \(Q_z=(P-z)^*(P-z)\).
Its highest homogeneous part is nonzero in the free polynomial algebra, so nonconstant \(P\) cannot produce a constant formal \(Q_z\).
The statements are accepted; the source proofs were not fully reviewed.

For the final potential identities, [Han26, Section 1.3, equations (1.6)--(1.7)](https://arxiv.org/html/2606.01664v1#S1.SS3) was checked as the cited convention.
The potential representation and support property were also checked in [Haagerup--Schultz, arXiv:math/0605251v1, Theorem 2.7, p. 8, and Proposition 2.17, p. 18](https://arxiv.org/pdf/math/0605251v1#page=8).
A bounded \(a=P(s)\) lies in the theorem's class, and its Brown measure is a probability measure supported in its spectrum.
Its potential is \(\tau(\log|a-z|)\), with distributional Laplacian \(2\pi\mu_a^{\mathrm{Br}}\).
These statements are accepted without a full review of their proofs.
No Ginibre eigenvalue-convergence theorem is used to infer the GUE conclusion.

## Whole-chain finding

<a id="whole-chain"></a>

No fatal mathematical gap was found in the exact candidate argument.
Subject to the accepted external theorem boundary above, the proof establishes both the stated pencil bound and the original F0012 assertion.
The checks supporting this conclusion follow.

### Fixed-dimensional backward error

The witness space \(W\) has dimension between one and \(m\).
The outgoing space contains every \(P_{W^\perp}H_jW\) and has dimension at most \(dk\).
Consequently \(H_jU=UA_j+VB_j\) is an equality, so (C2) accounts for the entire residual rather than only a projected portion.
Hermitian coordinates for \(A_j\), complex coordinates for \(B_j,\widetilde v\), and the normalization equation give precisely \(dk^2+2d\ell k+2mk\) real variables.
Their Euclidean norm is bounded independently of \(N\) by (C4).
The real coefficients of each resulting polynomial map depend only on the fixed coefficient matrices and its finite type.

For a nonempty real zero set, (KS2) and the bounded input region yield (C5).
Closedness gives an attained nearest zero.
If a type has no zero, its residual has a positive minimum on the relevant closed bounded input ball, so that type contributes no sufficiently small residual.
There are finitely many types, permitting a common positive exponent, cutoff and constant.
If all types are excluded, the small-residual implication is vacuous.
No lower bound on the rank of the repaired witness columns is required.

In (C6), the adjoint term has zero product with \(U\), since \(V^*U=0\).
Thus the repaired Hermitian matrices act on all of \(W\) by the repaired \(A'_j,B'_j\), even when \(\widetilde v'\) loses rank.
The normalization coordinate guarantees a nonzero unit kernel vector.
The three matrix blocks are orthogonal in Hilbert--Schmidt norm, giving the factor two in (C7).
These checks establish a perturbation of Hilbert--Schmidt size \(O(\varepsilon^\alpha)\), with no ambient-\(N\) loss.
The witness-dependent isometries only prove a deterministic inclusion, so a measurable selection is unnecessary.

### Real geometry and Gaussian probability

The determinant at zero input equals one.
Therefore \(q_N=|\det T_N|^2\) is a nonzero real polynomial, nonnegative on the real Hermitian-coordinate space and of degree at most \(2mN\).
An empty zero set is compatible with the backward-error argument only by exclusion of small residuals on the norm event.
There is no substitution of a complex zero for a real Hermitian perturbation.

For a fixed ball and tube radius, the relevant zeros form a compact set.
Near each zero, a positive value of \(q_N\) exists because a nonzero polynomial cannot vanish on an open ball.
A finite cover and segments from nearby zeros to those positive points give simultaneous approximation by every sufficiently small positive level.
Sard's theorem allows such a level with nonvanishing gradient.
It is nonempty when the relevant zero set is nonempty.
This yields the asserted inclusion into a tube of radius \(\rho+\eta\) about a smooth complete intersection.
Lotz's bound is uniform over the level, so taking \(\eta\) to zero is valid.
No uniform choice of a level over all Gaussian radii is needed: the deterministic ball bound holds for each radius.

Writing \(t=\rho/\sigma\), the sum in (T1) is
\(4[(1+(2D+1)t)^n-(1+t)^n]\).
The mean-value estimate gives (T2), retaining its exponential factor.
The proposed mixing density is the density of \(\chi_{n+2}\); division by the ball volume and integration from \(|x|\) gives the standard Gaussian density exactly.
A Chernoff bound for its squared radius gives the exponentially small lower-radius event.
On its complement, \(n/\sigma\le2\sqrt n\), proving (T4).

The Task density makes real Hilbert--Schmidt coordinates independent \(N(0,1/N)\) variables.
Thus the backward-error radius is multiplied by \(\sqrt N\), while \(\sqrt n=\sqrt d\,N\) and \(D\le2mN\).
Their product gives \(N^{5/2}\varepsilon^\alpha\), not an exponential dimension constant.
This proves the norm-restricted estimate (P).
Taking \(A\alpha>5/2\) and a fixed norm cutoff above two gives the asserted floor with probability tending to one.
A larger \(A\) makes the tube contribution smaller than any prescribed inverse power; the displayed observation about that contribution does not itself change the norm-tail term.

### Polynomial linearization and fixed-shift applicability

For each word, the only path from the first to the last chain coordinate has the required ordered product.
The minus signs in \(C_w\) and the Schur complement produce the positive word coefficient.
The block \(Q\) has a polynomial inverse for every evaluation, while the full constant block is invertible precisely when \(z\ne P(0)\).
After left multiplication by \(D_z^{-1}\), the matrix is a monic pencil with fixed complex coefficient matrices.

The inverse root block is \((P(0)-z)(P(H)-zI)^{-1}\).
Its norm is bounded by the norm of the full inverse, which gives exactly the direction and factor in (L).
The Schur complement also gives equivalence of singularity, so this step does not discard singular matrices.
For fixed \(z\ne P(0)\), the determinant polynomial is nonzero at zero input, hence the singular event has Gaussian probability zero.
A fixed scalar factor can be absorbed into the exponent of \(N\).
The exceptional shift is one point, negligible for the later planar integration.
Constant \(P\) is handled separately by the identical point masses.

### Averaged lower tail and logarithmic cutoff

The transform of the positive operator \(Q_z(s)\) has the expansion supplied by SS15.
Along \(it\), the probability-measure bound rules out powers below \(-1\).
The coefficient of a \(w^{-1}\) term equals the zero atom by the usual limit \(itG(it)\); atomlessness removes it.
The remaining finitely spaced Puiseux exponents therefore yield some positive \(\beta_z\), reduced to at most one if necessary.
If zero is outside the exceptional set, ordinary local analyticity is sufficient.

For the positive spectral variable \(x\), the kernel inequality in the candidate gives a bound on \(\nu_N^z([0,t])\) from \(t|\Im G(it)|\).
Multiplication of the CGP estimate by \(t\) produces \(N^{-2}t^{-4}\), with the smaller term absorbed for \(t\le1\).
The condition \(\gamma_z<2/(4+\beta_z)\) implies \(N^{-2}t^{-4}\le t^{\beta_z}\) throughout the stated mesoscopic interval.
Thus (W) has the required uniformity in \(t\) for each fixed \(z\).

On the least-singular-value good event, the squared singular values are bounded below by \(N^{-2B_z}\).
Below \(N^{-\gamma_z}\), their entire negative logarithmic contribution is bounded by the mass there times \(2B_z\log N\), whose expected upper bound tends to zero.
On the remaining interval, integration by parts against the mass function gives the stated \(\varepsilon^{\beta_z}(1+|\log\varepsilon|)\) bound and a vanishing endpoint term.
The good event need not be independent of that mass: the unconditional expectation upper bound applies to its indicator-restricted contribution.
The bad event is discarded in probability, not in expectation.
Markov's inequality then gives (UI).
The same power estimate gives logarithmic integrability for the limiting measure.
This is sufficient for the probability conclusion, without an expected logarithmic tail bound on the rare bad event.

### Potentials and the exact Task conclusion

Star-moment convergence and norm control give weak convergence in probability of the squared-singular-value laws.
Bounded logarithmic truncations converge; the norm event controls the upper tail and (UI) controls the lower tail.
The factor one half for squared singular values agrees with \(N^{-1}\log|\det(A_N-zI)|\).

On a fixed compact planar set, translated logarithmic kernels have uniformly bounded \(L^2\) norms when their centers lie in a fixed disk.
Jensen's inequality applies to the empirical eigenvalue measure, including algebraic multiplicities.
The Brown potential representation and its spectral support give the same bound for the limit.
Pointwise convergence in probability outside one shift implies convergence to zero of the expected area where the potential difference exceeds a fixed tolerance, by bounded convergence and Tonelli.
Cauchy--Schwarz on that area, with the common \(L^2\) bound, upgrades this to local \(L^1\) convergence in probability.
Logarithmic singularities at individual eigenvalues affect only planar null sets and do not obstruct these estimates.

The distributional Laplacian identities then prove convergence against compactly supported smooth functions.
The fixed norm event and the Brown spectral support put both measures in one deterministic disk with probability tending to one.
Uniform smooth approximation on that disk extends the conclusion to every bounded continuous real test function.
The proof retains arbitrary fixed \(d,P\), nonnormal evaluations, the unperturbed GUE law and the exact probabilistic quantifiers in F0012.
There is no dependence on a varying polynomial, perturbation of the ensemble or uniformity in the shift that the Task did not require.

## Limits and disposition

The whole local proof was checked mathematically; this is not a structural-only pass or a numerical test.
No counterexample or failed implication was identified.
The accepted source theorems remain external inputs whose complete original proofs were not independently re-audited.
There was no proof-assistant verification, and the review makes no novelty or priority assertion.
This finding is self-reviewed because of the actual context exposure described above.
It provides no independent-review credit and changes neither the Claim assessment nor the Task lifecycle by itself.

---
author: Yin
---

# Gaussian tubes and integrable determinant tails

Review act: 2026-11-04T18:46 UTC.
Human record author: Yin.
This is a separately organized independent key-step review of the fixed C_F0186_v3 expectation and global-small-singular-value branch.
The reviewer received the fixed candidate, its necessary mathematical inputs, the assigned scope and administrative facts, without substantive proof-development dialogue, drafts, earlier R findings or other reviewers' conclusions.
The reviewer did not develop or repair the argument.
No earlier review verdict is used as evidence for this finding.

## Inputs

- [Strengthened statement and argument](../../claims/Yin_C_F0186_v3.md#statement).
  The inspected conclusions are (Global), finite-limit logarithmic \(L^1\) and mean convergence, the minus-infinite extended mean, and every fixed finite root-determinant \(L^p\) limit.
  The exact argument sections are bound below.
- [Fixed affine probability theorem](../../claims/Yin_C_F0186_v2.md#statement).
  Its probability conclusions and weak spectral convergence are accepted prior inputs; the rank, compression, regularization and mesoscopic-counting interfaces used here were rechecked directly.
- [Real polynomial distance inequality](../../claims/Yin_C_F0186_v1.md#error-bound).
  The stated KSS inequality and its Hermitian lifting interface were checked against the retained original.
- [Uniform-ball tube estimate and regular-level extension](../../claims/Yin_C_F0186_v1.md#tubes).
  The exact codimension-one Lotz specialization and the local extension to nonzero nonnegative polynomials were rechecked.
- [Ordinary determinant convention](../literature/MS24/Yin_U001.md#determinant-convention).
  The logarithm includes a zero atom, and the matrix trace is normalized by \(1/m\).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | [Strengthened statement](../../claims/Yin_C_F0186_v3.md#statement) | (Global), (Mean), the extended mean for \(u=-\infty\), and root-determinant convergence in every fixed finite \(L^p\), with the exact fixed-coefficient GUE hypotheses; excludes (AS) and the Brown-measure conclusion. |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | [Argument entrance](../../claims/Yin_C_F0186_v3.md#argument) | Weak spectral convergence, normalization, within-size laws and deterministic cases needed by this branch; excludes the subsequent almost-sure chain. |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | [Gaussian tubes](../../claims/Yin_C_F0186_v3.md#tube-without-floor) | Exact chi-ball mixture, finite negative moments and the Gaussian tube bound without an additive error. |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | [Repair growth](../../claims/Yin_C_F0186_v3.md#global-repair-growth) | Uniform polynomial growth of the repair, treatment of empty compressed zero sets and moving norm cutoff. |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | [Elementary norm tail](../../claims/Yin_C_F0186_v3.md#norm-tail) | Gaussian quadratic-form variance, sphere net, constants and uniform moments. |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | [Global small-ball bound](../../claims/Yin_C_F0186_v3.md#global-small-ball) | Event inclusion, \(N^{5/2}\) scaling, absorption of the norm tail, and integrable negative-logarithm tail. |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | [Expected logarithmic tail](../../claims/Yin_C_F0186_v3.md#mean-log-tail) | Integration on all three intervals, Tonelli, eventual zero-atom exclusion and expected uniform integrability. |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | [Finite logarithmic limit](../../claims/Yin_C_F0186_v3.md#l1-log-limit) | Positive spectral-tail control and removal of both logarithmic cutoffs in \(L^1\). |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | [Minus-infinite mean](../../claims/Yin_C_F0186_v3.md#minus-infinite-mean) | Well-defined extended expectation, fixed-regularizer \(L^1\) convergence and upper comparison as the regularizer decreases to zero. |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | [Root determinant moments](../../claims/Yin_C_F0186_v3.md#root-determinant-moments) | Probability convergence plus norm domination implies every fixed finite \(L^p\) conclusion, including limit zero. |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | [Affine weak convergence](../../claims/Yin_C_F0186_v2.md#argument) | The weak singular-spectral and expected-measure convergence used before logarithmic truncation. |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | [Regularized zero limit](../../claims/Yin_C_F0186_v2.md#zero-limit) | Fixed-regularizer convergence in probability and \(u_\delta\downarrow u\), including \(u=-\infty\). |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | [Matrix-space rank](../../claims/Yin_C_F0186_v2.md#matrix-space-rank) | DM17 definitions and the accepted square-blow-up rank divisibility statement over \(\mathbb C\). |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | [Eventual generic invertibility](../../claims/Yin_C_F0186_v2.md#generic-rank) | Affine/homogeneous maximum-rank equality, Hermitian Zariski density and the zero-atom contradiction. |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | [Affine compression and lift](../../claims/Yin_C_F0186_v2.md#affine-repair) | Finite quadratic types, coordinate bounds, residual preservation and the Hermitian Hilbert--Schmidt lift. |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | [Mesoscopic counting](../../claims/Yin_C_F0186_v2.md#logarithmic-tail) | Matrix-valued CGP comparison and SS Puiseux input yielding (W); no use of an untruncated exceptional-event expectation. |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | [KSS input](../../claims/Yin_C_F0186_v1.md#error-bound) | Exact global polynomial-map inequality and the distance-to-zero interpretation for nonempty zero sets. |
| [Integrable-tail and mean finding](#integrable-tail-and-mean) | [Lotz input and extension](../../claims/Yin_C_F0186_v1.md#tubes) | Uniform-ball estimate, regular-level extension and Gaussian mixture identity needed by v3. |

## Primary-source checks and accepted boundary

The following retained originals were read directly at the stated passages.
Their theorem statements, normalizations and hypotheses match the applications described here.
The original proofs of these established external theorems, including the underlying IQS regularity proof, were not re-audited in full.
They are accepted external inputs at this explicit boundary.

| Source and exact passage | Checked use |
| --- | --- |
| [KSS16, arXiv:1412.5088v1, PDF p. 2, (KS2)](../../literature/pdf/KSS16--arxiv-v1.pdf#page=2) | For a real polynomial map on \(\mathbb R^p\) of degree \(D\), the exponent is \(D(6D-3)^{p-1}\) and the global denominator is \(1+\lvert x\rvert^2\). |
| [Lot15, arXiv:1210.3742v4, Theorem 1.1, PDF p. 1](../../literature/pdf/Lot15.pdf#page=1) | The codimension-one specialization is the finite binomial sum used in v1; the theorem allows arbitrary positive ball and tube radii. |
| [DM17, published paper, Definitions 2.1--2.2 and Proposition 2.3, journal p. 49 / PDF p. 6](../../literature/pdf/DM17.pdf#page=6) | The maximum rank of the square tensor blow-up is divisible by the blow-up size; this does not say that each member has divisible rank. |
| [CGP22, arXiv:1912.04588v1, Corollary 1.3, PDF p. 5](../../literature/pdf/CGP22--arxiv-v1.pdf#page=5) | Fixed, possibly noncommuting deterministic coefficient matrices and their adjoints are allowed; the fixed amplification contributes \(m^2N^{-2}\), and the resolvent powers are \(5\) and \(2\). |
| [SS15, arXiv:1305.1920v1, Theorem 1.1(5)(6), PDF pp. 1--2](../../literature/pdf/SS15--arxiv-v1.pdf#page=2) | The algebraicity and convergent local Puiseux statement applies to self-adjoint matrix-valued polynomials in free semicircular variables. |
| [CGP22, Proposition 2.11, PDF p. 10](../../literature/pdf/CGP22--arxiv-v1.pdf#page=10) | The source norm bound is valid for every size and yields all fixed moments by integrating its tail; the elementary proof (N) independently supplies the bound used in this branch. |
| [CGP22, Proposition 4.4, PDF p. 30, and coordinates on p. 31](../../literature/pdf/CGP22--arxiv-v1.pdf#page=30) | Standard real Gaussian concentration and the \(N^{-1/2}\) Hilbert--Schmidt scaling match the candidate's source statements; this expectation branch does not require the later almost-sure concentration chain. |

The standard GUE moment limit, finite-dimensional spectral identities, polynomial zero-set facts, Sard's theorem and nonnegative integration theorems are accepted at their usual stated domains.
No source issue affecting the inspected branch was found.
This source check makes no novelty claim or whole-source proof-verification claim.

## Decisive checks

### Rank and compression interfaces

For finite \(u\), the limiting law \(\nu\) of \(L^*L\) has no atom at zero.
The maximum affine rank equals the rank of the homogeneous matrix-space blow-up because the maximum-rank locus intersects the nonempty open set where the auxiliary coefficient of \(A_0\) is invertible.
Multiplication by its inverse gives the affine slice.
A real Hermitian basis is also a complex basis of all matrices, so a nonzero maximum minor remains nonzero on Hermitian coordinates and the Gaussian tuple has that maximum rank almost surely.
Rank divisibility then makes every nonzero rank deficit at least \(N\).
An infinite subsequence of such deficits would give \(\bar\nu_N(\{0\})\ge1/m\), contradicting the closed-set Portmanteau inequality and \(\nu(\{0\})=0\).
This validates eventual nonidentity of \(q_N\), including singular \(A_0\).

The compression uses \(1\le k\le m\) and \(0\le\ell\le dk\).
Its real input dimension is \(dk^2+2d\ell k+2mk\), independent of \(N\).
The residual coordinates and the normalization equation are quadratic, and the actual coordinate norm satisfies \(\lvert x\rvert^2\le2dkM^2+1\).
The constant term has no outgoing component because each physical vector component lies in \(W\).
Keeping the physical isometries while changing compressed coordinates gives a Hermitian perturbation with squared Hilbert--Schmidt norm at most \(2\lvert x'-x\rvert^2\).
The repaired normalized vector is an exact kernel vector.
This is a deterministic existence argument and needs no measurable selection.

### Polynomial growth, including empty types

For a nonempty compressed zero set, solving (KS2) for the distance gives precisely
\[
 \operatorname{dist}(x,F_i^{-1}(0))
 \le C_i(1+\lvert x\rvert^2)\lvert F_i(x)\rvert^{1/(2\,9^{p_i-1})}.
\]
The lift therefore has growth \(C(1+M^2)\varepsilon^a\) with a common positive exponent and constants independent of \(M,N\).

For an empty type, \(G_i(x,y)=(yF_i(x),y(y-1))\) has zero set \(\mathbb R^{p_i}\times\{0\}\).
At \((x,1)\) its distance to the zero set is exactly one.
The ambient dimension is \(p_i+1\), so the degree-three KSS exponent is \(E_i=3\,15^{p_i}\).
Thus \(\lvert F_i(x)\rvert\ge c_i(2+\lvert x\rvert^2)^{-E_i}\), with the stated weaker exponent also valid if the actual degree is two.
No convention for distance to an empty set is used.

At \(M=\varepsilon^{-\theta/2}\), the lower bound for an empty type is at least \(c_i'\varepsilon^{\theta E_i}\).
The choice \(\theta E_i\le1/2\) excludes such a type for all sufficiently small \(\varepsilon\), uniformly over the finite list.
For nonempty types the repair is \(O(\varepsilon^{a-\theta})\), and \(\theta\le a/2\) gives \(b=a-\theta>0\).
If there are no nonempty types, the low-residual event is empty on the moving norm cutoff.
This also covers an empty singular-input set.

### Gaussian tube bound without an error floor

The regular-level construction in v1 is valid on each fixed compact set of relevant zeros.
A nonzero nonnegative polynomial has positive values arbitrarily close to each zero.
A finite cover and a common sufficiently small regular level approximate all those zeros within any prescribed tolerance.
Lotz's codimension-one theorem applies to that smooth level set, with the same degree bound, and letting the tolerance decrease proves the displayed uniform-ball estimate for the original zero set.
No smoothness or real codimension-one hypothesis on the original singular set is inserted.

The radial density
\[
 w_n(s)=\frac{s^{n+1}e^{-s^2/2}}{2^{n/2}\Gamma(n/2+1)}
\]
divided by the radius-\(s\) ball volume and integrated over \(s\ge\lvert x\rvert\) gives exactly the standard Gaussian density.
Thus the chi distribution has \(n+2\), rather than \(n\), degrees of freedom.
All negative moments needed after the binomial expansion have orders \(k\le n<n+2\) and are finite.
The gamma integral estimate gives
\[
 (\mathbb ES^{-n})^{1/n}
 \le e^{1/n+1/2}n^{-1/2}
 \le e^{3/2}n^{-1/2}.
\]
Monotonicity of probability-space \(L^p\) norms then gives (T2) for every needed \(k\).
Taking expectations of the finite polynomial before the exponential upper bound is legitimate and yields (T3) with no residual probability term.
The mean-value bound for the difference of the two \(n\)-th powers gives the factor \(8C_0D\sqrt n\,\rho\).

### Global small singular values and norm tails

For the specified GUE normalization, \(v^*Hv\) has variance \(1/N\) for every complex unit vector.
The \(1/4\)-net has at most \(9^{2N}\) points and yields the factor two in the quadratic-form approximation to \(\|H\|\).
The final inequality in (N) is valid because \(M\ge9\) implies \(M^2\ge32\log9\).
It gives uniformly bounded moments of every fixed positive order.

With \(D\le2mN\), \(n=dN^2\) and \(\rho=C\sqrt N\,\varepsilon^b\), the tube factor is \(O(N^{5/2}\varepsilon^b)\).
The moving norm failure is \(2d\exp(-N\varepsilon^{-\theta}/16)\).
On the stated domain \(N^{5/2}\varepsilon^b\le1\), the tube exponential is bounded.
The norm failure is bounded uniformly by \(C\varepsilon^b\), hence by the same right side of (Global).
All thresholds and exponents depend only on the fixed coefficients.
For each sufficiently large \(N\), the exponential bound for \(\log^-s_{\min}(L_N)\) past \(K\log N\) proves its integrability and all fixed positive moments by tail integration.
The completely deterministic case is covered directly by the candidate's separate argument.

### Expected negative logarithmic tails

The CGP comparison is applicable to the matrix-valued self-adjoint polynomial \(L_N^*L_N\) after tensor-factor interchange.
The fixed matrix amplification and coefficient norms enter only its constant.
The SS input supplies a convergent Puiseux expansion of its free Cauchy transform.
The bound \(\lvert G(it)\rvert\le t^{-1}\) excludes powers below \(-1\), and \(itG(it)\to\nu(\{0\})=0\) excludes a nonzero order-\(-1\) term.
If zero is an ordinary analytic point, the same conclusion holds directly.
Consequently \(t\lvert\Im G(it)\rvert\le Ct^\beta\) for some \(0<\beta\le1\).
The kernel bound and resolvent comparison give
\[
 \mathbb E\nu_N([0,t])\le C(t^\beta+N^{-2}t^{-4}),
\]
and \(\gamma(4+\beta)<2\) proves (W) throughout \(N^{-\gamma}\le t\le1\).

On \(0<t\le a_N=N^{-2B}\), the global small-ball bound applies for all large \(N\), since \(Bb>5/2\).
Using \(\nu_N([0,t])\le1_{\{s_{\min}\le\sqrt t\}}\) gives an integrable bound \(CN^{5/2}t^{b/2}\), whose integral against \(dt/t\) is \(O(N^{5/2-Bb})\).
On \([a_N,t_N]\), monotonicity bounds the mass by \(Ct_N^\beta\), giving \(O((\log N)N^{-\gamma\beta})\).
On \([t_N,\varepsilon]\), (W) integrates to \(O(\varepsilon^\beta)\); the layer boundary contributes \(O(\varepsilon^\beta\lvert\log\varepsilon\rvert)\).
Tonelli is applied only to nonnegative functions.
Exact zero mass vanishes almost surely at every sufficiently large size, so no singular value at zero is omitted from the logarithmic expectation.
These estimates prove (EUI) and eventual integrability without assuming an exceptional-event logarithm is already integrable.

### Mean limits and root determinant moments

The bound \(\|L_N\|\le C_A(1+\max_j\|H_j^{(N)}\|)\) and (N) control the positive spectral logarithmic tail uniformly in \(N\).
At fixed lower and upper cutoffs, weak convergence in probability gives convergence in \(L^1\) because the truncated integrals are bounded.
The triangle inequality, (EUI), the positive-tail bound and the free logarithmic integrability remove both cutoffs and give \(\mathbb E\lvert U_N-u\rvert\to0\) for finite \(u\).
The normalization factor is \(1/2\) when integrating \(\log x\) against the squared-singular-value law.

For arbitrary coefficients, \(U_N^+\le\log^+\|L_N\|\), so its expectation is finite even if the negative part has infinite mean.
For fixed \(\delta>0\), \(U_{N,\delta}\ge\log\delta\) and its positive part is uniformly integrable.
Its established probability convergence therefore improves to \(L^1\).
The comparison \(U_N\le U_{N,\delta}\) yields
\[
 \limsup_N\mathbb EU_N\le u_\delta.
\]
As \(u_\delta\downarrow-\infty\), this proves the claimed extended mean limit.
It makes no assertion of an \(L^1\) distance to an infinite value and does not require eventual finite expectations in that case.

Finally, \(0\le D_N\le\|L_N\|\).
For any prescribed \(0<p<\infty\), choose a fixed \(q>p\).
The uniform \(q\)-moment bound makes \(\lvert D_N-e^u\rvert^p\) uniformly integrable, and the fixed prior probability convergence proves its expectation tends to zero.
This argument also applies when \(e^u=0\) and when \(p<1\).
No estimate uses independence between different sizes.

<a id="integrable-tail-and-mean"></a>
## Finding and remaining scope

The inspected global-small-singular-value and expectation branch is mathematically sufficient under the accepted external-input boundary stated above.
No unresolved gap in this branch or its checked source applicability was found.
It establishes (Global), eventual integrability and finite-limit logarithmic \(L^1\)/mean convergence, the minus-infinite extended mean, and all fixed finite root-determinant \(L^p\) limits for the exact coefficients and normalization in C_F0186_v3.

This finding does not review the almost-sure affine concentration argument, the scalar word-chain transfer, the planar Brown-potential argument, or the full reactivated F0012 contract.
It supplies no Task-completion verdict or mathematical assessment selection.
Those conclusions require their own applicable coverage.
No numerical experiment, build result or formal proof-assistant verification is used as mathematical evidence.

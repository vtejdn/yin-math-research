---
author: Yin
---

# Planar smoothing identities and sharp exact-input truncation thresholds

This Preparation concerns the original [finite-variance F0012 contract](../tasks/Yin_T_F0012_v3.md#contract), with arbitrary fixed real or complex entry laws and arbitrary cross-size couplings.
The [accepted spectral and planar controls](../claims/Yin_C_F0186_v4.md#argument) leave the first unsupported step at the [singular regularization defect](../claims/Yin_C_F0186_v4.md#remaining-defect).
The [determinant upper-limit separation](../ledger/Yin_L_F0061_v2.md#brown-nonimplication) and [negative logarithm example](Yin_D_F0010.md#negative-logarithmic-gap) remain actual constraints on this investigation.
The present material is ordinary proof development by an assigned agent for Yin, without independent-review or adoption status.
Only this new Draft is maintained by this assignment.

## Starting scope

The main probe asks whether planar averaging removes a bottom-logarithmic obligation by itself.
A second probe determines the precise raw-entry cutoff needed for an exact-input comparison under the original coupling quantifier.
Neither probe changes the Task, assumes density or a moment above two, or transfers eigenvalue convergence through a low-rank or small-norm perturbation.
The existing [nilpotent-shift failures](../ledger/Yin_L_F0058_v1.md#failed-shortcuts) already rule out those general stability shortcuts and are reused rather than asserted as a new finding.

<a id="original-argument"></a>
## Reconstruction of the original argument and its first missing step

Fix the laws, polynomial and common probability space exactly as in the Task.
The accepted [finite-variance controls](../claims/Yin_C_F0186_v4.md#finite-variance-weak) first use centered fixed raw-entry truncations, bounded colored moments and rank estimates only for Hermitian polynomial outputs to establish expected Hermitized weak limits.
The [independent-row-block argument](../claims/Yin_C_F0186_v4.md#row-concentration) makes those weak limits almost sure with summable marginal errors, and therefore respects every cross-size coupling.
The [positive logarithmic tails](../claims/Yin_C_F0186_v4.md#log-statistics) and [fixed-regularizer convergence](../claims/Yin_C_F0186_v4.md#regularized-potentials) then give locally uniform convergence of the regularized potentials on a common countable-parameter event.
The [eigenvalue logarithmic moment and local planar bounds](../claims/Yin_C_F0186_v4.md#noncompact-planar) supply tightness and local planar uniform integrability for the unregularized eigenvalue potentials.

None of these conclusions relates the two potentials in the remaining lower direction.
The exact first missing implication is that the nonnegative area integral of their difference tends to zero after taking the dimension upper limit and then removing the regularizer.
The slow diagonal regularizer controls the regularized sequence only; the [D10 counterexample](Yin_D_F0010.md#negative-logarithmic-gap) prevents combining a polynomial floor with qualitative weak convergence as a substitute.
The [L61 separation](../ledger/Yin_L_F0061_v2.md#brown-nonimplication) likewise prevents substituting a correct pointwise determinant upper limit for full-sequence planar convergence.
The two calculations below test genuine averaging and exact-input comparison interfaces without asserting either missing implication.

<a id="scalar-planar-smoothing"></a>
## A universal planar bound for scalar spectral smoothing

Let \(A\in M_N(\mathbb C)\) be arbitrary, with eigenvalues \(\lambda_1,\ldots,\lambda_N\) counted algebraically, and write
\[
 u_A(z)=\frac1N\sum_{i=1}^N\log|z-\lambda_i|,
 \qquad
 v_{A,\delta}(z)=\frac1{2\pi}\int_0^{2\pi}u_A(z+\delta e^{it})\,dt.
\]
The scalar Jensen formula retained at [Den09-U001, Mahler conventions](../audits/literature/Den09/Yin_U001.md#mahler-measure), specialized to a degree-one polynomial and rescaled by \(\delta\), gives
\[
 v_{A,\delta}(z)=\frac1N\sum_i\log\max\{|z-\lambda_i|,\delta\}.
 \tag{S1}
\]
Unit-circle zeros are allowed by that exact retained source interface.
Consequently \(v_{A,\delta}-u_A\ge0\) almost everywhere and, by Tonelli and translation invariance,
\[
 \int_{\mathbb C}(v_{A,\delta}-u_A)\,d^2z
 =2\pi\int_0^\delta r\log(\delta/r)\,dr
 =\frac\pi2\delta^2.
 \tag{S2}
\]
The equality is independent of \(A\) and \(N\), and requires no norm, moment, singular-value or eigenvector estimate.
In particular an arbitrary moving scalar circular smoothing can be removed in local planar \(L^1\) whenever its radius tends to zero.
An isotropic scalar noise with random radius \(R\) gives the same calculation with right side \(\pi\mathbb E R^2/2\), when that second moment is finite.

This does not estimate the singular regularization used by the Task.
Put
\[
 w_{A,\delta}(z)=\frac1{2N}\sum_i\log(|z-\lambda_i|^2+\delta^2),
 \qquad
 u_{A,\delta}(z)=\frac1{2N}\log\det((A-z)^*(A-z)+\delta^2I).
\]
The [Cauchy--Binet inequality already proved for the actual matrices](../claims/Yin_C_F0186_v4.md#noncompact-planar), applied to \(A-z\), gives
\[
 u_{A,\delta}\ge w_{A,\delta}\ge v_{A,\delta}\ge u_A.
 \tag{S3}
\]
Thus the comparison needed to bound the singular defect by scalar smoothing has the wrong direction.
The scalar output perturbation in (S1) translates every eigenvalue exactly and supplies no independent matrix-entry regularity.
Its harmless removal cannot be substituted for removing entrywise Gaussian noise or singular regularization.

There is also a dimension-free local bound on the soft eigenvalue smoothing.
For every disk \(K\) of radius \(R>0\),
\[
 0\le\int_K(w_{A,\delta}-u_A)\,d^2z
 \le\frac\pi2\left[
  (R^2+\delta^2)\log(R^2+\delta^2)
  -R^2\log R^2-\delta^2\log\delta^2\right].
 \tag{S4}
\]
Indeed, the radial function \(f(r)=\tfrac12\log(1+\delta^2/r^2)\) is nonnegative and decreasing.
For any measurable set of area \(\pi R^2\), layer-cake integration bounds its translated integral by the centered radius-\(R\) disk integral: at each height the intersection area is at most the smaller of the two areas.
That centered integral is
\[
 \pi\int_0^R r\log(1+\delta^2/r^2)\,dr
 =\frac\pi2\int_0^{R^2}\log(1+\delta^2/t)\,dt,
\]
which evaluates to the right side of (S4).
Apply this separately at each \(\lambda_i\) and average.
For fixed \(R\), the bound tends to zero at order \(\delta^2(1+|\log\delta|)\).

The only part not bounded to vanish by this computation is \(u_{A,\delta}-w_{A,\delta}\), the multiplicative eigenvalue--singular-value gap in Cauchy--Binet.
Saying that this gap vanishes is another formulation of the unresolved planar condition, not a new estimate or a solution.
The useful conclusion of this probe is the exact safe scalar-smoothing bound and the demonstrated direction of the comparison; it gives no new bound for the original nonnormal defect.

<a id="sharp-exact-truncation"></a>
## Sharp universal raw-entry thresholds for exact-input transfer

The following comparison does apply to the original Wigner input, without invoking spectral stability.
For each size \(N\), replace every raw off-diagonal variable \(\xi_j\) by \(\xi_j1_{\{|\xi_j|\le N^{3/2}\}}\), and every raw diagonal variable \(\zeta_j\) by \(\zeta_j1_{\{|\zeta_j|\le N\}}\).
Use the original variables to couple the truncated and original matrices, retain the factor \(N^{-1/2}\), and do not recenter or rescale the truncated laws.
Then the original tuple and this raw-truncated tuple agree for every sufficiently large size, almost surely, under every cross-size coupling allowed by the Task.
Every fixed nonnormal polynomial and its eigenvalue measure therefore also agree eventually, as an identity of actual matrices.

Here is the complete tail-sum argument.
For any random variable \(X\) with finite second moment and integers \(b\ge0\),
\[
 \sum_{N\ge1}N^b\mathbb P\{|X|>N^{(b+1)/2}\}
 =\mathbb E\sum_{N<|X|^{2/(b+1)}}N^b
 \le C_b\mathbb E|X|^2.
 \tag{T1}
\]
The last bound follows by comparing the finite power sum with its elementary integral; the sum is zero when \(|X|\le1\).
There are at most \(N^2/2\) off-diagonal variables for each input and \(N\) diagonal variables.
A union bound and (T1), with \(b=2\) and \(b=1\), show that the disagreement probabilities are summable.
First Borel--Cantelli uses no independence across sizes and proves eventual exact equality.
This strengthens the raw \(N^2\) cutoff used for the [previous polynomial-norm bound](../claims/Yin_C_F0186_v4.md#log-statistics), but supplies no estimate for the smaller entries or their bottom logarithms.
The raw off-diagonal cutoff here corresponds to a normalized matrix-entry cutoff \(N\), so it is much larger than a fixed or polylogarithmic normalized cutoff.

For comparison, raw off-diagonal cutoff \(N\) and diagonal cutoff \(\sqrt N\) suffice for exact matching in probability.
Finite second moments imply \(t^2\mathbb P\{|X|>t\}\to0\), because that expression is bounded by \(\mathbb E[|X|^21_{\{|X|>t\}}]\).
Multiplying the respective tail probabilities by the respective coordinate counts proves the in-probability claim.
It does not give a summable marginal error and therefore cannot justify arbitrary-coupling almost-sure transfer.

Centering or variance-normalizing the cutoff variables can destroy this eventual identity even on an outcome with no discarded entries.
Their comparison with the original nonnormal output needs a separate argument.
The present lemma deliberately makes no such inference from the small deterministic mean, small norm or low rank of a resulting perturbation.

<a id="atomic-cutoff-obstruction"></a>
## An atomic original-model obstruction to smaller exact-match cutoffs

A single fixed real atomic variance-one law shows that the preceding exponents are sharp among power cutoffs for universal exact-input transfer.
Set
\[
 c=\left(\sum_{k\ge1}k^{-2}\right)^{-1},
 \qquad
 \mathbb P\{X=2^k\}=\mathbb P\{X=-2^k\}
 =\frac{c}{2\,4^kk^2}\quad(k\ge1),
\]
and put the remaining probability at zero.
The displayed masses sum to less than one, symmetry gives mean zero, and
\[
 \mathbb E X^2=c\sum_{k\ge1}k^{-2}=1,
 \qquad
 \mathbb E|X|^{2+\varepsilon}
 =c\sum_{k\ge1}\frac{2^{\varepsilon k}}{k^2}=\infty
 \quad(\varepsilon>0).
\]
For \(t\ge2\), comparison of the geometric tail after \(\lfloor\log_2t\rfloor\) gives positive constants \(a_1,a_2\) such that
\[
 \frac{a_1}{t^2(1+\log t)^2}
 \le p(t):=\mathbb P\{|X|>t\}
 \le\frac{a_2}{t^2(1+\log t)^2}.
 \tag{T2}
\]
The lower bound keeps only the first allowed dyadic atom, and the upper bound sums the remaining geometric series with denominators bounded below by the first index squared.
Use this law for the off-diagonal entries of one real Wigner input and, when needed, for its diagonals.
It satisfies the exact fixed-law Task assumptions.

For \(m_N\) independent coordinates, raw cutoff \(R_N\) changes at least one coordinate with probability
\[
 q_N=1-(1-p(R_N))^{m_N}.
 \tag{T3}
\]
This is also exactly the total-variation distance between the original product law and its raw-truncated product law, using the convention that total variation is the supremum of event-probability differences.
The event that some coordinate exceeds the cutoff gives the lower bound \(q_N\), since its truncated probability is zero.
The actual coordinatewise truncation coupling gives the matching upper bound, since the two vectors differ with probability \(q_N\).
Consequently another coupling of those two product laws cannot improve the exact-match probability beyond \(1-q_N\).

For \(0\le p\le1\),
\[
 1-e^{-m_Np}\le q_N\le\min\{1,m_Np\}.
\]
Hence \(q_N\) is bounded below by a positive constant times \(\min\{1,m_Np(R_N)\}\).
For off-diagonal \(m_N=N(N-1)/2\) and cutoff \(R_N=N^\alpha\), (T2) yields a nonsummable sequence \(q_N\) for every \(0<\alpha<3/2\).
For diagonal \(m_N=N\), it is nonsummable for every \(0<\alpha<1\).
Nonpositive exponents have disagreement probability tending to one and are excluded even more directly.
Choose the matrices independently across dimensions, an allowed coupling.
The disagreement events are then independent, and second Borel--Cantelli gives infinitely many disagreements almost surely.
Thus no smaller exponent has a universal eventual exact-input matching theorem under the Task's quantifiers.
This does not show failure of the Brown-measure conclusion: disagreement of input matrices is a different event.
The same example has \(q_N\to1\) for every off-diagonal exponent \(\alpha<1\), or diagonal exponent \(\alpha<1/2\), so the earlier universal in-probability thresholds are sharp as well.

A stronger obstruction concerns the commonly desired raw cutoff
\[
 R_N=\sqrt N\,(\log N)^B,\qquad B\ge0\text{ fixed}.
 \tag{T4}
\]
For off-diagonal entries, the number \(M_N\) of discarded independent coordinates is binomial with mean
\[
 \lambda_N=m_Np(R_N)
 \asymp\frac{N}{(\log N)^{2B+2}}.
\]
The probability of no discarded coordinate is at most \(e^{-\lambda_N}\), and these probabilities are summable.
Therefore every allowed cross-size coupling has at least one discarded coordinate at every sufficiently large size, almost surely.
In particular this cutoff fails exact-input matching even in probability.
Its original and truncated product laws have total-variation distance tending to one, so this obstruction applies to every exact-match or total-variation transfer of those laws.

Nevertheless the same coupling has only a vanishing rank fraction of discarded entries almost surely.
To see this without an unrecorded concentration input, use independence within each size to write
\[
 \mathbb E e^{\theta M_N}
 =(1-p+p e^\theta)^{m_N}
 \le\exp(\lambda_N(e^\theta-1)).
\]
Markov's inequality at \(\theta=\log2\) gives
\[
 \mathbb P\{M_N>2\lambda_N\}
 \le\exp(-(2\log2-1)\lambda_N).
\]
This sequence is summable, so \(M_N=O(N/(\log N)^{2B+2})=o(N)\) almost surely under every coupling.
Replacing one off-diagonal coordinate changes a Hermitian input by rank at most two, so the discarded off-diagonal matrix has rank \(o(N)\).
An arbitrary finite-variance diagonal law can be left untruncated in this example; taking it identically zero isolates the off-diagonal assertion exactly.

Thus the original model itself can force the following simultaneous facts: a polylogarithmic normalized entry cutoff changes the input at every sufficiently large dimension, while the normalized rank of the change tends to zero.
Exact matching cannot remove that cutoff, and the established Hermitian rank comparison alone supplies no nonnormal eigenvalue transfer.
This is a new precise threshold obstruction to an exact-matching proof route, not a Wigner-polynomial spectral counterexample or a new general impossibility theorem for truncation.

## Remaining scope and source limits

The planar probe uses the exact Jensen formula already retained at the cited Den09 source unit and the proved finite-dimensional Cauchy--Binet inequality already retained in C186v4.
Its remaining integrations, product-coordinate probabilities, tail sums and exponential-moment calculation are given in full here.
The atomic cutoff law and its obstruction require no external random-matrix theorem or source acquisition.
No new literature follow-up is needed for these exact limited conclusions.
The missing nonnormal planar gap still needs a genuinely random estimate for the original polynomial or its actual linearization; neither scalar smoothing nor the exact extreme-entry cutoff establishes it.

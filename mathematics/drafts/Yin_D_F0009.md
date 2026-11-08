---
author: Yin
---

# Disk averages and a truncated second eigenvalue moment for F0012

This working argument concerns the [fixed-law finite-variance Wigner problem](../tasks/Yin_T_F0012_v3.md#contract).
It gives a one-statistic criterion for an arbitrary fixed polynomial, and proves the full convergence when the filled Brown support has zero planar area.
The general lower bound for the statistic is open.
These deductions have not received independent review.

<a id="positive-part"></a>
## The upper bound for the potential

Let \(A_N=P(W^{(N)})\), \(a=P(s)\), \(\mu_N\) be the empirical eigenvalue probability measure, and \(\mu\) be the Brown measure of \(a\).
Use the sign convention \(U_\eta(z)=\int\log|z-w|\,d\eta(w)\) and write \(u_N=U_{\mu_N}\), \(u=U_\mu\).
All integrals in \(z\) below use Lebesgue area \(dA\).
Fix a sample in the probability-one event of the [regularized potential limits](../claims/Yin_C_F0186_v4.md#regularized-potentials) for \(\delta=1/k\) and the [eigenvalue bounds](../claims/Yin_C_F0186_v4.md#noncompact-planar).
For each such \(\delta\), the singular-value regularization \(u_{N,\delta}\) majorizes \(u_N\) and converges locally uniformly to \(u_\delta\).
Also \(u_\delta\downarrow u\) in local \(L^1\).
For any bounded disk \(D\), these facts give
\[
 \limsup_N\int_D(u_N-u)_+\,dA\le \int_D(u_\delta-u)\,dA .
\]
Sending \(\delta\) to zero gives \(\int_D(u_N-u)_+\,dA\to0\) on this same event for every bounded disk.
This uses regularized Hermitization and no estimate for a least singular value.

<a id="disk-moment"></a>
## A disk average and the remaining lower bound

Fix \(R>\max_{w\in\operatorname{supp}\mu}|w|\), for instance \(R>\|a\|\), and let \(D_R=\{|z|<R\}\).
Define \(m=\int|w|^2\,d\mu(w)\) and \(m_{N,R}=\int\min(|w|^2,R^2)\,d\mu_N(w)\).
We claim the pathwise identity
\[
 \int_{D_R}|u_N-u|\,dA=\frac{\pi}{2}(m-m_{N,R})+o(1).
 \tag{1}
\]
In addition, \(\int_{R<|z|<S}|u_N-u|\,dA\to0\) for every \(S>R\).

The [circle mean used for scalar spectral smoothing](../ledger/Yin_L_F0065_v1.md#scalar-planar-smoothing) gives
\[
 \frac1{2\pi}\int_0^{2\pi}\log|re^{i\theta}-w|\,d\theta=\log\max(r,|w|).
\]
Write \(t_N(r)=\int\log^+(|w|/r)\,d\mu_N(w)\).
For \(r>\max_{\operatorname{supp}\mu}|w|\), the circular mean of \(u_N-u\) is \(t_N(r)\ge0\).
The logarithmic singularity of an eigenvalue on the circle is integrable.
Radial integration shows that the signed integral of \(u_N-u\) over each such exterior annulus is nonnegative.
Its \(L^1\) norm there is therefore bounded by twice the integral of \((u_N-u)_+\), which tends to zero.
In particular, choose \(\max_{\operatorname{supp}\mu}|w|<r_0<R\).
Monotonicity in \(r\) gives
\[
 \pi(R^2-r_0^2)t_N(R)
 \le\int_{r_0<|z|<R}(u_N-u)\,dA
 \le\int_{D_R}(u_N-u)_+\,dA\longrightarrow0 .
\]

Integrating the same circle mean with \(2\pi r\,dr\) from zero to \(R\) gives the exact kernel identity
\[
 \int_{D_R}\log|z-w|\,dA(z)
 =\pi R^2(\log R-\tfrac12)
  +\frac{\pi}{2}\min(|w|^2,R^2)+\pi R^2\log^+(|w|/R).
 \tag{2}
\]
Indeed, one splits the radial integral at \(|w|\) when \(|w|<R\).
Integrating (2) against \(\mu_N-\mu\) gives
\(\int_{D_R}(u_N-u)\,dA=\tfrac\pi2(m_{N,R}-m)+\pi R^2t_N(R)\).
The identity \(|x|=2x_+-x\), the upper bound for the potential and \(t_N(R)\to0\) now give (1).

In particular \(\limsup_N m_{N,R}\le m\).
Convergence \(u_N\to u\) in \(L^1_{\mathrm{loc}}(\mathbb C)\) is equivalent to the single lower bound \(\liminf_N m_{N,R}\ge m\), by (1) and exterior annulus convergence.
The [pathwise Brown criterion](../claims/Yin_C_F0186_v4.md#remaining-defect) then gives exactly the weak convergence required by F0012.
The cutoff in \(m_{N,R}\) keeps this test bounded under finite second moments of the original inputs.
The statistic uses eigenvalues of \(A_N\), while \(N^{-1}\operatorname{Tr}(A_N^*A_N)\) measures squared singular values.
For the [nilpotent shifts with Haar unitary limit](../ledger/Yin_L_F0058_v1.md#failed-shortcuts), \(m_{N,R}=0\) and \(m=1\) at every \(R>1\).
In this example (1) gives the exact integral \(\pi/2\).

<a id="thin-support"></a>
## Convergence on the unbounded component and a sufficient support condition

Let \(G\) be the unbounded component of \(\mathbb C\setminus\operatorname{supp}\mu\), and let \(H=\mathbb C\setminus G\).
Then \(u_N\to u\) in \(L^1_{\mathrm{loc}}(G)\).
If \(H\) has planar area zero, the convergence holds in \(L^1_{\mathrm{loc}}(\mathbb C)\) and the empirical measures converge weakly to \(\mu\).
This covers a Brown support contained in a line segment.
The unit circle illustrates why bounded complementary components enter \(H\).

To prove these assertions, take any subsequence.
Pathwise tightness gives a further subsequence with weak limit \(\nu\).
The [positive logarithmic second-moment bound and kernel truncation](../claims/Yin_C_F0186_v4.md#remaining-defect) give \(u_N\to U_\nu\) in \(L^1_{\mathrm{loc}}(\mathbb C)\) on this subsequence.
Indeed \(\int(\log^+|w|)^2\,d\nu(w)\) obeys the same bound by lower semicontinuity, so the far tail estimate in that truncation argument applies to both measures even before identifying \(\nu\).
The upper bound for the positive part gives \(U_\nu\le u\) almost everywhere.
Exterior annulus convergence gives \(U_\nu=u\) almost everywhere on \(\{|z|>R\}\).

On \(G\), \(u\) is harmonic and \(U_\nu\) is subharmonic, as follows locally from the logarithmic kernel and its circle mean.
The far part of the kernel is continuous locally by the finite positive logarithmic moment, and truncation of the negative singularity from below gives upper semicontinuity of \(U_\nu\).
The submean inequality gives \(U_\nu-u\le0\) everywhere on \(G\) from its almost-everywhere upper bound.
This function attains zero in an exterior annulus.
At a zero, its area submean inequality forces it to vanish almost everywhere on each sufficiently small disk about that point.
Upper semicontinuity and nonpositivity then force it to vanish throughout the disk.
Thus its zero set is both open and closed in \(G\), so \(U_\nu=u\) on \(G\).
Every original subsequence consequently has a further subsequence converging locally in \(L^1(G)\) to \(u\).
When \(H\) has zero area, \(U_\nu=u\) almost everywhere in the whole plane and the same subsequence argument applies on each disk.

<a id="wigner-lower-bound"></a>
## The missing estimate for arbitrary support

For a general \(P\), the remaining random-matrix input is a lower bound on \(m_{N,R}\) under the original fixed laws.
For the quantifier over all cross-size couplings, an exact marginal target is
\[
 \sum_N\mathbb P\{m_{N,R}<m-\eta\}<\infty
 \qquad\text{for every rational }\eta>0 .
\]
It suffices by the first Borel--Cantelli lemma.
It is necessary for an every-coupling conclusion because independent matrices across sizes form an allowed coupling, to which the second Borel--Cantelli lemma applies.
No such marginal bound for arbitrary \(P\) follows from (1) or the Hermitized weak limits.
For independent row-block replacements, the [fourth-moment bound and mean condition](../ledger/Yin_L_F0067_v1.md#mean-and-influences) give one sufficient route to this summability.
The [single-entry construction for bounded Wigner inputs](../ledger/Yin_L_F0067_v1.md#single-entry-oscillation) rules out a uniform \(o(1)\) influence bound, leaving the size of typical changes open.

---
author: Yin
---

# The cubic Brown limit and the ordinary determinant at every prescribed shift

<a id="statement"></a>
## Real finite-variance Wigner inputs

Let \(X_N,Y_N\) be two independent real symmetric Wigner matrices with the fixed centered laws, unit strict upper variances, finite diagonal second moments and \(N^{-1/2}\) normalization of the [finite-variance contract](../tasks/Yin_T_F0012_v3.md#contract).
Write \(P=1+x^2y+yx,\ P_N=P(X_N,Y_N),\ p=P(s_1,s_2)\) at free standard semicirculars with faithful normal tracial state \(\tau\), and \(u(w)=\tau\log|p-w|\).
Under every coupling across dimensions the ordinary normalized log determinant \(U_N(w)=N^{-1}\log|\det(P_N-wI)|\) converges to \(u\) almost surely in local planar \(L^1\), the empirical eigenvalue measures converge weakly almost surely to the Brown measure of \(p\), and the [bottom-\(h_N\) integrated deviation series](Yin_C_F0362_v2.md#statement) is finite, where \(h_m=\lceil\log(m+3)\log\log(m+3)\rceil\).
For every prescribed \(w\in\mathbb C\), \(U_N(w)\to u(w)\) in probability and almost surely along \(N=2^j\), and \(\limsup_N U_N(w)=u(w)\) almost surely under every coupling.
The pointwise events here may depend on the prescribed parameter.

More precisely, on prescribed principal sites of size \(n=N-o(N)\) let \(M=P(X_0,Y_0)\) use the restricted inputs with their original normalization, and write \(t_1\le\cdots\le t_n\) for the singular values of \(M-w_N I\).
For any prescribed real \(w_N\to w\in\mathbb R\), almost surely
\[
 \frac1N\sum_{i>j}\log t_i\longrightarrow u(w)\quad(j=h_n,2h_n),
 \qquad \frac{h_n}{N}\log^-t_{2h_n+1}\longrightarrow0 .
\]
The established [cubic planar result and its nonreal fixed-point comparison](Yin_C_F0362_v2.md#terminal) supply the off-axis and planar conclusions; the proof below treats the real axis.

<a id="argument"></a>
<a id="slice-test"></a>
## A quadratic test on a short spectral interval of \(Y\)

Use the prescribed nested principal minors of size \(l=N-o(N)\) needed in the [cubic trim induction](Yin_C_F0362_v1.md#trim).
Write \(X,Y\) for the two inputs restricted to one such minor, \(K=N^2\), and \(\delta=N^{-\gamma}\) for a sufficiently small fixed \(0<\gamma<1/4\).
On the full Frobenius guard both input norms are at most \(K\), with failure probability \(O(N^{-3})\).
The [two-slice comparison](Yin_C_F0362_v1.md#escape) holds both in its indicated order and with \(X,Y\) exchanged.
In particular the spaces \(E\) spanned by one or two grid intervals of radius \(2\delta\) in either input have dimension \(O(l/\log^2N)\) except with summable probability.
If \(\Pi\) projects onto such a space for \(Y\), a complex unit vector cannot have both \(\|(1-\Pi)v\|=o(K^{-1})\) and \(\|(1-\Pi)Xv\|=o(1)\) on those guards.
The analogous assertion holds for \(X\)-slices and \(Yu\).

Fix a bounded real interval of shifts \(|w|\le R\).
For a single \(Y\)-slice \(E\), condition on \(Y\), retaining the stated dimension bound, and define
\[
 D_{\mu,w}=\mu X^2+YX-(w-1)I,\qquad N^{-10}\le|\mu|\le K,\quad \mu\in\mathbb R .
\]
Except with summable probabilities, on the norm and dimension guards there is a \(c>0\) such that simultaneously in these parameters and slices,
\[
 \|D_{\mu,w}v\|\ge c|\mu|\quad(v\in E_{\mathbb C},\ \|v\|=1).
 \tag{1}
\]
To prove this, fix first real \(v,\mu,w\).
Partition the sites into three blocks of nearly equal size and call one with \(\|v_H\|\ge1/\sqrt3\) the block \(H\); call the others \(B,C\).
Keep only the two independent strict upper rectangles joining \(H\) to \(B\) and \(B\) to \(C\) fresh in \(X\).
The twofold alternating difference of \((D_{\mu,w}v)_C\) on independent resamplings of the rectangles equals
\[
   \mu\,\Delta X_{CB}\Delta X_{BH}v_H .
\]
The reverse product of the two symmetric changes ends in \(H\), hence contributes nothing on \(C\); all linear and constant terms cancel.
The [finite-variance rectangular row bound](Yin_C_F0196_v6.md#truncated-core), applied successively to the two independent difference rectangles at the original scale, gives a norm at least \(c_0|\mu|\) outside \(Ce^{-c'l}\).
If the conditional probability of norm \(\|(D_{\mu,w}v)_C\|<c_0|\mu|/8\) were \(q\), the four resamplings would all satisfy this inequality with probability at least \(q^4\) by two Cartesian Cauchy--Schwarz steps.
Thus \(q\le C e^{-c''l}\), without conditioning the rectangles on an operator norm bound.

Take nets of mesh \(N^{-50}\) for the real unit sphere of \(E\), the indicated \(\mu\) ranges and \([-R,R]\), with parameter net points in their ranges.
Their combined log size is \(O(l/\log N+\log N)=o(l)\).
On the original norm guard \(\|D_{\mu,w}\|\le C_R N^6\), and a change in \(\mu,w\) costs at most \(K^2|\Delta\mu|+|\Delta w|\).
The total errors are \(o(N^{-10})\) and can be absorbed into a smaller \(c|\mu|\).
All grid intervals and prescribed minors together cost a polynomial factor.
The uniform real bound extends to complex \(v\) by applying it separately to real and imaginary parts, since \(D_{\mu,w}\) and \(E\) are real.
This proves (1).

<a id="real-direction"></a>
## The small leading direction in the cubic companion

Use the four-channel pencil \(L(w)\), its graph equations, \(\tau=N^{-170}\), \(\rho=N^{-130}\) and \(e=N^{-120}\) of the [directional calculation](Yin_C_F0362_v1.md#direction).
Suppose a unit left or right near-mode of \(L(w)\) at residual \(\tau\) violates the unscaled directional border floor \(\rho\).
After normalization of its physical component the scalar residual for \(M^{\mathsf T}-wI\) or \(M-wI\) is less than \(N^{-150}\), and the two corresponding inequalities (2) of that calculation hold for an auxiliary unit vector \(a\).
For \(|a_0|\ge N^{-40}\) the two-slice contradiction there uses no imaginary-part hypothesis: on the left use the roots of \(x^2+a_3/a_0\), and on the right the two centers \(-a_2/a_0,-a_1/a_0\) of the \(X\)-slices.
It remains to treat \(|a_0|<N^{-40}\).

On the left the same unit-coefficient bounds give \(|a_2|\ge(4K)^{-1}\) and
\[
  \|(X-\lambda)u\|\le4K(e+N^{-40}K)\le N^{-35},
  \qquad \lambda=\langle u,Xu\rangle\in[-K,K].
\]
The scalar residual and \(\|(X^2-\lambda^2)u\|\le2K N^{-35}\) now imply
\[
 \|(X+\lambda^2 I)Yu-(w-1)u\|\le N^{-150}+2K^2N^{-35}.
\]
Use the union of \(X\)-slices about \(\lambda,-\lambda^2\), omitting a slice if no spectrum is within \(\delta\) of its center.
Off that union \(\|(1-\Pi)u\|\le N^{-35}/\delta\), and
\(\|(1-\Pi)Yu\|\le\delta^{-1}[(R+1)N^{-35}/\delta+N^{-150}+2K^2N^{-35}]\).
These two bounds contradict two-slice escape.

On the right one has \(|a_1|\ge(4K)^{-1}\) and
\[
 \|(Y-\mu)v\|\le4K(e+N^{-40}K^2)\le N^{-33},
 \qquad \mu=\langle v,Yv\rangle\in[-K,K].
\]
Replacing \(X^2Yv\) by \(\mu X^2v\) in the scalar residual gives \(\|D_{\mu,w}v\|\le N^{-150}+K^2N^{-33}\).
For \(|\mu|\le N^{-10}\) take the \(Y\)-slice about zero.
On its complement,
\[
 \|(1-\Pi)v\|\le2N^{-10}/\delta,\qquad
 \|(1-\Pi)Xv\|\le\delta^{-1}
 \big[2(R+1)N^{-10}/\delta+N^{-150}+K^2N^{-33}+K^2N^{-10}\big].
\]
The second inequality follows by moving the \(\mu X^2v\) term to the other side and inverting \(Y\) on this complement.
The bounds are respectively \(o(K^{-1})\) and \(o(1)\); they contradict escape with the colors exchanged, including at \(w=1\).

For \(|\mu|>N^{-10}\) take the single \(Y\)-slice about \(\mu\), so \(\|(1-\Pi)v\|\le N^{-33}/\delta\).
Hence \(\|\Pi v\|=1-o(1)\) and
\[
 \|D_{\mu,w}\Pi v\|\le N^{-150}+K^2N^{-33}+C_RN^6 N^{-33}/\delta=o(N^{-10}).
\]
This contradicts (1).
We have proved the directional floor \(\rho\) on both whole near-null spaces of each prescribed old minor for these real shifts.

<a id="real-trim"></a>
## Real trims and the determinant comparison

Apply the [four-channel border induction](Yin_C_F0362_v1.md#trim) with the floor just proved.
At deficit \(q\ge h_n\), projecting each raw border direction onto the old tail gives the polynomial volume gain except with \(CN^C e^{-cq}+CN^{-3}\), besides the whole-chain guard exceptions.
The guards used conditionally depend on the current old minor; the bounds for all these guards and the full norm are charged separately, without conditioning on future rows.
The chain starts \(\lfloor n/\log^3(n+3)\rfloor\) sites below the target and the accumulated undivided logarithmic cost is \(o(N)\).
The initialization there applies to the real shifts because the scalar Schur polynomial \(1+s^3x^2y+s^2yx-w\) is nonzero for every \(w\) and \(1/2\le s\le2\).
Thus the compact family of full shifted companions has the same free small-mass and regularized finite comparisons, including at \(w=1\).
The fixed-clip upper bound, Schur singular-factor comparison and subtraction of the two trims in that argument give the stated real trimmed limits and the adjacent loss for every prescribed real sequence \(w_N\to w\).

At a regular real parameter in a fixed compact interval start the [scalar determinant flag](Yin_C_F0362_v2.md#flag) of size \(k=2\lfloor\log^3(N+3)/2\rfloor\) with \(n=N-k\).
The left and right singular frames can be taken real.
For \(r>0\) each selected bottom vector has residual at most \((N^7+R)N^{-Ah_n}\).
Apply the [sparse near-vector bound](Yin_C_F0186_v42.md#word-spread) directly to \(P-w\) or its reversal, with top cubic word \(x^2y\) or \(yx^2\) of coefficient one, outside probability \(O(N^{-J})\) for any fixed \(J\).
The [single real overlap argument](Yin_C_F0357_v1.md#real-restoration) then gives the two overlap floors \(N^{-(B+2)r}\) with failure \(O(h_n\sqrt{\log K_*/n}+h_nN^{-3}+N^{-J})\), \(K_*=C_J\log^3(N+2)\).
Indeed after deleting \(cn/\log K_*\) coordinates the restriction of every tested real bottom direction to the remaining coordinates has norm at least \(K_*^{-C}\); the resulting individual coordinate bases and the one-dimensional Fourier estimate apply at each Gram--Schmidt stage.
The exterior-power lower bound holds unchanged, also for \(r=0\).

At a single real node the [nine-kernel independence proof](Yin_C_F0363_v1.md#argument) gives nine **real** directions modulo scalars, including at \(w=1\).
The scalar cofactor uses only the first kernel.
For a compact real interval, continuity in measure of the free inverses and compactness give uniform positive mass above a positive threshold on the relevant distinct-site corners, for all unit real coefficient vectors.
The [physical corner approximation](Yin_C_F0363_v1.md#corners) works with these real directions alone: the compact full companion family and bounded free Schur factors give uniform small singular mass for inverse clipping, and the finite polynomial and rank comparisons use no lower bound on \(|\operatorname{Im}w|\) once that mass and corner spread are available.
This is the same real-parameter use of cutoff and row concentration as in the [single-node kernel comparison](Yin_C_F0357_v1.md#real-restoration).
Thus the [two-panel deletion](Yin_C_F0362_v2.md#flag) and the [three paired contractions in six panels](Yin_C_F0363_v1.md#polarization) cost \(O(n^{-1/8})\) and \(O(n^{-1/128})\) per regular transition, respectively, up to exponentially small old-minor and conditional exceptions.
For the latter the conditional coefficients and bilinear forms are real, the selected \(11,22,33\) coefficients are tested in that order, and the same finite-dimensional spans remove the other pairings.
The last six Cartesian differences cost the same sixty-fourth root.
The [exact normal factors and rank corrections](Yin_C_F0362_v2.md#restoration) are unchanged.

For each \(N\), almost every real \(w\) makes the original scalar minor regular almost surely, by Fubini for its monic characteristic polynomial.
Counting bad transitions only at regular incoming matrices charges a first zero after a good initial step.
The comparisons give the [undivided determinant bound (1)](Yin_C_F0362_v2.md#terminal) with error probability
\[
 O\big(h_n\sqrt{\log K_*/n}+k n^{-1/128}+kN^{-3}+N^{-J}\big)
\]
plus summable norm, rectangular and old-minor exceptions, uniformly at these regular-almost-sure real parameters on compact intervals.
Both sides of that undivided inequality are continuous even at poles of the resolvent.
Approximating an arbitrary prescribed real point by such parameters and applying Fatou to the strict violation gives the same bound at every real \(w\).
The error vanishes along the full sequence and is summable along dyadic sizes.
The real trims at sizes \(n=N-k,N\) and the adjacent log loss in the displayed lower comparison now give the pointwise lower convergence in probability and the dyadic almost-sure lower bound under every coupling.
The full-size upper trim bounds \(U_N\) above up to \(O(h_N\log N/N)\) on the norm guard.
This gives the almost-sure full-sequence upper bound and, together with the dyadic conclusion, the stated limsup.

## Current assessment
[Selected decision](#decision-cubic-real-reviewed)

## Assessment history

### Decision cubic-real-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:44 |
| status | open |
| reason | A two-rectangle test on a short spectral interval excludes the remaining real-axis direction, and the real kernel comparison gives a candidate proof at every prescribed real point. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Cubic result](#statement) | Full planar limit, terminal series, real trimmed limits and the ordinary determinant at each prescribed complex shift. |
| argument | [Real spectral-slice tests](#argument) | Directional bounds, the real trim induction and recovery of the untrimmed determinant. |
| support | [Real directional bounds](#real-direction) | Both near-kernel orientations, with separate estimates at small and large Rayleigh quotient. |
| support | [Real trims and determinant](#real-trim) | Both trim sizes, adjacent loss, the real one-node restoration and its probability bounds. |
| dependency | [Planar cubic theorem](Yin_C_F0362_v2.md#statement) | The planar and nonreal conclusions and the exact scalar determinant comparison. |
| dependency | [Nine resolvent kernels](Yin_C_F0363_v1.md#statement) | Rational independence at each real parameter and the sixth-difference argument used with real directions. |

### Decision cubic-real-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:48 |
| status | proved |
| reason | Two independent rectangular exposures and the two spectral-window estimates supply the real-axis trim and restoration for all prescribed real parameters. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact theorem](#statement) | Two independent rectangular exposures and the two spectral-window estimates supply the real-axis trim and restoration for all prescribed real parameters. |
| argument | [Complete argument](#argument) | The hypotheses, parameter scope and conclusions of the fixed proof. |
| review | [Independent whole-proof assessment](../audits/reviews/Yin_R_F0370_v3.md#cubic-real-whole-proof) | The stated mathematical scope and remaining restrictions. |

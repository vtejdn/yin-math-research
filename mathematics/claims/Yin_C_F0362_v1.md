---
author: Yin
---

# Polylogarithmic singular-value trims for the cubic \(1+x^2y+yx\)

<a id="statement"></a>
## The scalar limits and the remaining loss

Take two independent **real symmetric** Wigner inputs \(X,Y\) with the centered fixed laws, unit strict upper variances, finite diagonal second moments and \(N^{-1/2}\) scaling of the [finite-variance contract](../tasks/Yin_T_F0012_v3.md#contract).
There is no assumption on their coupling across dimensions.
Put \(P=1+x^2y+yx\), \(u(w)=\tau\log|P(s_1,s_2)-w|\) at free standard semicirculars, and \(h_n=\lceil\log(n+3)\log\log(n+3)\rceil\).
On a prescribed deterministic set of \(n=N-o(N)\) sites, \(n\le N\), form \(M=P(X|_{[n]},Y|_{[n]})\) after restricting the inputs, with the original scaling.
Let \(t_1(w)\le\cdots\le t_n(w)\) be the singular values of \(M-wI\), and put \(b_j(w)=N^{-1}\sum_{i>j}\log t_i(w)\).
For \(j=h_n,2h_n\), almost surely under every allowed coupling,
\[
 b_j\longrightarrow u \quad\text{in }L^1_{\rm loc}(\mathbb C).
\]
For each prescribed sequence \(w_N\to w\notin\mathbb R\), \(b_j(w_N)\to u(w)\) almost surely as well.
The four-channel pencil below has the same two limits when the largest \(4n-j\) singular values are retained with normalization \(1/N\).
The loss \((h_n/N)\log^-t_{2h_n+1}\) tends to zero in disk integral and at these prescribed moving parameters.
In particular, for the full matrix \(n=N\), weak convergence of the eigenvalue measures to the Brown measure of \(P(s_1,s_2)\) almost surely under every coupling is equivalent to
\[
 \sum_{N>h_N}\Pr\!\left\{\frac1N\int_{|w|\le R}
 \sum_{i=1}^{h_N}\log^-t_i(w)\,dA(w)>\epsilon\right\}<\infty
 \qquad (R,\epsilon>0).
\]
Here \(dA\) is planar Lebesgue measure and \(\log^-0=+\infty\).
The summability in this last display is not proved.

<a id="argument"></a>
<a id="escape"></a>
## Independent rows force escape from two thin spectral slices

Use at most \(N\) prescribed nested principal minors on \(l=N-o(N)\) sites, with the original scaling, and write \(X,Y\) also for each minor.
The full-input guard \(\max(\|X_N\|,\|Y_N\|)\le K=N^2\) has failure probability \(O(N^{-3})\) by the Frobenius second moment; it bounds every minor.
Take a sufficiently small fixed \(0<\gamma<1/4\), and \(\delta=N^{-\gamma}\).
Use a \(\delta\)-grid in \([-K-2,K+2]\) with intervals of radius \(2\delta\).
The [uniform real-center count and row concentration](Yin_C_F0351_v12.md#real-trim) imply that, outside summable exceptions, every such grid interval for every prescribed minor contains at most \(Cl/\log^2 N\) eigenvalues of \(X\), with multiplicities.
Let \(E\) be the real span of the \(X\)-eigenspaces in one or two grid intervals and denote its orthogonal projection by \(\Pi\).
With summable total exception, on all these minors and for every such \(E\),
\[
 \|(1-\Pi)Yv\|\ge c\|v\|\quad (v\in E_{\mathbb C}). \tag{1}
\]

Condition only on the old \(X\) first.
For a fixed real unit \(v\in E\) and real \(b\in E\), choose the half of the sites carrying at least half the squared mass of \(v\).
On the opposite half expose the principal block of \(Y\) there.
The remaining rectangular rows have independent strict upper variables, and the part of \(Yv-b\) being tested has arbitrary fixed shifts and coefficient squared norm at least \(1/2\) before normalization.
The [finite-variance rectangular row bound](Yin_C_F0196_v6.md#truncated-core) hence gives \(\Pr\{\|Yv-b\|\le c_0\mid X\}\le Ce^{-c'l}\), uniformly in \(b,v\); replacing \(l^{-1/2}\) by \(N^{-1/2}\) changes only a bounded factor.
Use \(N^{-4}\)-nets of the real unit sphere of \(E\) and the radius-\(2K\) real ball of \(E\).
Their combined log size is \(O(\dim(E)\log N)=O(l/\log N)\).
The approximation costs at most \(N^{-4}(K+1)\) on the norm guard, which was not conditioned on in the rectangular estimate.
The closest possible \(b=\Pi Yv\) has norm at most \(K\) there.
There are polynomially many grid pairs and nested minors; union bounds give (1) for real vectors, then real and imaginary parts give its complexification with the same \(c>0\).
It follows on this event that a complex unit \(v\) cannot satisfy both \(\|(1-\Pi)v\|=o(K^{-1})\) and \(\|(1-\Pi)Yv\|=o(1)\): apply (1) to \(\Pi v\) and use the norm guard.
The test also covers a single interval or an empty spectral slice.
For each complex number \(z\), the real spectral points with \(|x-z|\le\delta\) lie in a grid interval centered nearest \(\operatorname{Re}z\) if this set meets \([-K,K]\); otherwise no interval is needed.
On the complement of the chosen interval the factor \(X-z\) has singular values at least \(\delta\).

<a id="direction"></a>
## Directional lower bounds for the cubic companion

Fix a bounded set of \(w\) with \(|\Im w|\ge\eta>0\).
On each old minor take the pencil
\[
 L(w)=\begin{pmatrix}
 1-w&X&0&Y\\ 0&-I&X&0\\ Y&0&-I&0\\ X&0&0&-I
 \end{pmatrix}
\]
with scalar entries tensored with identities.
The invertible auxiliary pivot has determinant of modulus one and polynomial inverse; its Schur complement is \(M-w\).
Finite determinants therefore agree in absolute value, and the normalized free logarithm of the pencil is \(u(w)/4\) by the same unit triangular elimination and [bounded determinant multiplicativity](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation).
In fact \(L(w)\) is full at every complex \(w\) because \(P-w\) is a nonzero free polynomial.

Take residual cutoff \(\tau=N^{-170}\) and desired unscaled adjoint border floor \(\rho=N^{-130}\).
For a left unit vector of residual \(\|L(w)^*\ell\|\le\tau\) the auxiliary equations give the approximation \((u,Xu,X^2u,Yu)\), with the first component exact and total error \(C(1+K)\tau\).
For a right unit vector with \(\|L(w)r\|\le\tau\), the corresponding approximation is \((v,XYv,Yv,Xv)\) with the same error.
Thus the physical component on either side has norm at least \(c(1+K)^{-2}\ge N^{-5}\) for large \(N\).
After dividing by its norm, its scalar residual for \(M^*-\bar w\) or \(M-w\) is at most \(CN^5(1+K)^2\tau<N^{-150}\).
Below \(u,v\) denote the resulting physical **unit** vectors.

Let \(a=(a_0,a_1,a_2,a_3)\) range over the complex auxiliary unit sphere.
Collect the two fresh real color columns from the actual physical row and column addition, omitting their common \(N^{-1/2}\) normalization.
Applying the adjoint of the upper border in direction \(a\) to a left vector gives the two color components from the nonzero entries of its \(X,Y\) coefficient matrices; use their transposes for the lower border on the right.
Conjugation of all four directional coefficients leaves the tested unit sphere unchanged.
If either actual directional adjoint has norm less than \(\rho\) on such a near-null unit vector, the normalized graph substitution yields, on the relevant side,
\[
 \begin{array}{ll}
 \|(a_1+a_2X)u+a_0Yu\|\le e,&\|(a_3+a_0X^2)u\|\le e,\\
 \|(a_3+a_1Y)v+a_0XYv\|\le e,&\|(a_2+a_0X)v\|\le e ,
 \end{array} \tag{2}
\]
where \(e=N^{-120}\), since \(CN^5(\rho+(1+K)\tau)\le e\).

First suppose \(|a_0|\ge N^{-40}\) and write \(a'_j=a_j/a_0\), \(e'=N^{-80}\).
All primed coefficients are bounded by \(N^{40}\).
On the left take the at most two grid slices for the two complex roots of \(x^2+a'_3\).
Outside their union each factor has modulus at least \(\delta\), even when the roots coincide.
Hence \(\|(1-\Pi)u\|\le e'\delta^{-2}\).
The first equation and commutation of \(X,\Pi\) give \(\|(1-\Pi)Yu\|\le e'+N^{40}(1+K)e'\delta^{-2}\).
On the right take the slices for \(-a'_2,-a'_1\).
The second equation gives \(\|(1-\Pi)v\|\le e'\delta^{-1}\), while the first gives
\(\|(1-\Pi)Yv\|\le \delta^{-1}(e'+N^{40}e'\delta^{-1})\) by inversion of \(X+a'_1\) off that union.
In both cases the two distances contradict (1).

If \(|a_0|<N^{-40}\), on the left \(|a_3|\le e+N^{-40}K^2\) and \(\|(a_1+a_2 X)u\|\le e+N^{-40}K\).
Since \(a\) is unit these bounds force \(|a_2|\ge (4K)^{-1}\) for large \(N\): otherwise \(|a_1|\le 1/4+o(1)\).
The real Rayleigh quotient \(\lambda=\langle u,Xu\rangle\) then minimizes \(\|Xu-zu\|\) over complex \(z\), giving \(\|(X-\lambda)u\|\le 4K(e+N^{-40}K)\).
In \(\langle u,(I+YX^2+XY)u\rangle\) the replacements \(X^2u\mapsto\lambda^2u\) and \(Xu\mapsto\lambda u\) leave a real number and cost at most \((2K^2+K)\|(X-\lambda)u\|\).
Thus the imaginary part is \(o(1)\), contradicting the scalar residual and \(|\Im w|\ge\eta\).
On the right \(|a_2|\le e+N^{-40}K\), \(\|(a_3+a_1Y)v\|\le e+N^{-40}K^2\), so \(|a_1|\ge(4K)^{-1}\) by the same unit-norm argument.
With \(\mu=\langle v,Yv\rangle\) one has \(\|(Y-\mu)v\|\le4K(e+N^{-40}K^2)\).
Replacing \(Yv\) by \(\mu v\) in the two expectations for \(X^2Y\) and \(YX\) costs at most \((K^2+K)\|(Y-\mu)v\|=o(1)\) and leaves a real expectation.
This contradicts the right scalar residual.
These estimates give the floor \(\rho\) on either whole near-null subspace, simultaneously in every direction.

<a id="trim"></a>
## Paired physical borders and both trims

Use the [paired singular-volume inequality](Yin_C_F0347_v1.md#statement) with four channels.
For old retained index \(r\) let \(q=4l-r\ge32\).
If fewer than \(q/2\) old values are at most \(\tau\), compression monotonicity gives \(p_{r+8}(L')\ge p_r(L)\tau^8\) for the extended pencil, where \(p_r\) multiplies the \(r\) largest singular values.
Otherwise the tail projections off the first \(r+4\) left and \(r\) right singular vectors each retain at least \(\lfloor q/4\rfloor\) low singular directions.
On the old-measurable events of (1) and the norm guard the preceding directional adjoint floor and min--max give that many singular values at least \(\rho\) in each projected raw border map from the two stacked color columns.
The [fresh input projection argument](Yin_C_F0186_v41.md#flattening) applies to the two independent real strict-upper laws at their original scale: before normalization the input projection has rank at least \(\lfloor q/4\rfloor\), and both fixed positive variances have a common truncated second-moment bound.
This gives a lower bound \(c\rho\sqrt{q/N}\) on the projected normalized border in any fixed auxiliary unit direction except with conditional probability \(Ce^{-cq}\).
The fresh raw columns have combined norm at most \(N^2\) outside conditional probability \(O(N^{-3})\); on this guard a net of radius \(N^{-140}\) in the fixed four-dimensional complex sphere suffices for a polynomial lower bound in every direction.
Intersect the two border successes by union bound, as their fresh coordinates are shared.
The two volumes and the paired inequality now give \(p_{r+8}(L')\ge N^{-C}p_r(L)\), except with conditional probability \(CN^{C}e^{-cq}+CN^{-3}\) on the old events, independently of the corner block.
Here conditioning is only on the old principal inputs; the simultaneous whole-chain guard failures are added by a union bound, without conditioning the fresh border on future success.

At the target \(n\), use \(k=\lfloor n/\log^3(n+3)\rfloor\) additions starting at \(l=n-k\) with deficit \(4k+j\) for \(j=h_n,2h_n\).
Each addition reduces the deficit by four.
All failures over the chain have summable probabilities because the minimum deficit is at least \(h_n\), \(h_n/\log N\to\infty\), and the accumulated logarithmic cost is \(O(k\log N)=o(N)\).
For initialization apply the [affine polynomial-window initialization](Yin_C_F0186_v42.md#old-trim) to the pencils \(L(w_N;s x,s y)\), \(s=\sqrt{l/N}\to1\).
For \(1/2\le s\le2\) and \(w\) in a fixed disk the Schur polynomial \(1+s^3 x^2y+s^2 yx-w\) never vanishes identically.
The compact family is full, so the [free count](Yin_C_F0352_v1.md#statement) and [finite comparison](Yin_C_F0195_v4.md#free-background) supply the required uniform polynomial window.
Specifically, at the initial lower clip \(l^{-\gamma_0}\) for sufficiently small \(\gamma_0>0\) the count is \(o(l/\log^3N)\) with summable exceptions by [row-rank concentration](Yin_C_F0186_v4.md#row-concentration).
Integrating the window count to a fixed small cutoff controls the expected clipped negative logarithm; the fixed-cutoff weak limit, the affine second-moment positive tail and the same concentration with logarithmic variation give the initial clipped potential limit.
All retained values exceed this lower clip, and the omitted positive terms cost \(o(N)\) since their number is \(o(l)\) and the bottom median is eventually bounded by fixed-cutoff convergence.
Thus the initial retained product has normalized lower limit at least \(u(w)\), using the trace factor \(4l/N\to4\).
The border steps give the same lower limit at the final size.
A fixed lower clip at the final size bounds the trimmed log above with error at most \(j|\log d|/N\) for \(0<d<1\); then let \(d\downarrow0\).
This proves the two prescribed-parameter limits for the companion.

The finite Schur elimination above is a product of unit triangular transformations with polynomial norms and inverse norms under the guard, reducing the companion to \(\operatorname{diag}(M-w,-I,-I,-I)\).
The absolute determinants agree, so comparison of the \(j\) omitted singular values costs \(O(j\log N)\) in the retained log, and the corresponding product inequalities extend to singular shifts by continuity.
Removing the added unit values costs at most the same order by the polynomial norm guard, as in the [omitted-factor comparison](Yin_C_F0186_v41.md#assembly).
This yields the scalar moving limits.

For local \(L^1\) convergence apply Fubini to fixed nonreal parameters first.
On each disk the companion's positive log sum divided by \(N\) is eventually bounded on each good path, by the [finite-variance positive-log estimate](Yin_C_F0186_v4.md#log-statistics) at zero and the bounded parameter perturbation.
For varying minor sizes and scale one may use the same capped row concentration directly at zero: the affine second moments bound the expected normalized positive log, its variation up to the norm guard is \(O(\log N)\), and the resulting deviations are summable in \(N\).
The trimmed companion log is thus bounded above by a pathwise constant and below by the normalized scalar characteristic log minus a pathwise constant.
The negative part of the latter has uniformly bounded disk \(L^2\) norm by Jensen applied to the translated kernels \(\log^-|w-\lambda|\), since \(n/N\le1\).
This gives uniform integrability and both planar limits, with the same uniform omitted-factor comparison for the scalar.
The adjacent loss follows from
\[
 h_n\log^-t_{2h_n+1}\le N(b_{2h_n}-b_{h_n})+
 \sum_{i=h_n+1}^{2h_n}\log^+t_i,
\]
whose final sum is \(O(h_n\log N)\) on each disk under the norm guard.
Finally \(b_{h_N}\) minus the ordinary full scalar potential is the normalized bottom negative-log sum up to a uniform \(O(h_N\log N/N)\) positive-log error.
The [pathwise scalar potential criterion](Yin_C_F0186_v4.md#remaining-defect) and the two Borel--Cantelli implications give the stated terminal equivalence as in the [disk loss argument](Yin_C_F0186_v41.md#terminal): use first Borel--Cantelli on countably many disks and tolerances for sufficiency, and independent tuples across dimensions for necessity.

## Current assessment
[Selected decision](#decision-cubic-trim-reviewed)

## Assessment history

### Decision cubic-trim-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:09 |
| status | open |
| reason | Spectral slice escape and the four-channel graph give a candidate proof of both trims; the bottom polylogarithmic loss remains unestimated. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Cubic trim limits](#statement) | Real finite-variance inputs, prescribed minors, moving nonreal parameters, disk limits and terminal equivalence. |
| argument | [Escape on the old minor](#argument) | The span of up to two spectral slices of one color and the independent rows of the second. |
| support | [Four-channel directions](#direction) | Both singular orientations and all complex auxiliary directions. |
| support | [Trim assembly](#trim) | Fresh pairs, affine initialization, scalar comparison and the remaining bottom loss. |

### Decision cubic-trim-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:14 |
| status | proved |
| reason | The two-slice escape bound and both directional border estimates give the two cubic principal trims and the bottom-logarithm equivalence. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Unequal-length cubic](#statement) | Local planar and moving nonreal trims under real finite-variance input laws. |
| argument | [Complete proof](#argument) | Thin spectral windows, conditional rows and paired-border initialization. |
| support | [Terminal equivalence](#trim) | The stated marginal series is necessary and sufficient. |
| review | [Independent whole-proof review](../audits/reviews/Yin_R_F0370_v1.md#cubic-trim-whole-proof) | Full fixed theorem and its unresolved bottom estimate. |

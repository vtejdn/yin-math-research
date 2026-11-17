---
author: Yin
---

# Polylogarithmic trims for \(1+x^q y+yx\) using unequal border volumes

<a id="statement"></a>
## The scalar trims under the original law

Fix an integer \(q\ge2\), and let \(X_N,Y_N\) be independent real symmetric Wigner matrices under the fixed-law, finite-second-moment [contract](../tasks/Yin_T_F0012_v3.md#contract), with \(N^{-1/2}\) normalization and arbitrary coupling across dimensions.
Put \(P:=1+x^q y+yx\), \(u(w):=\tau\log|P(s_1,s_2)-w|\) at free standard semicirculars, and \(h_n:=\lceil\log(n+3)\log\log(n+3)\rceil\).
On a prescribed deterministic set of \(n=N-o(N)\) sites, form \(M:=P(X|_{[n]},Y|_{[n]})\) after restricting the inputs, keeping their original scaling.
Write \(t_1(w)\le\cdots\le t_n(w)\) for the singular values of \(M-wI\), and \(b_j(w):=N^{-1}\sum_{i>j}\log t_i(w)\).
Then almost surely under every allowed coupling,
\[
 b_{h_n}\longrightarrow u,\qquad b_{2h_n}\longrightarrow u
 \quad\hbox{in }L^1_{\mathrm{loc}}(\mathbb C).
 \tag{T1}
\]
For each prescribed deterministic sequence \(w_N\to w\notin\mathbb R\), both convergences also hold almost surely at \(w_N\).
The \((q+2)\)-channel pencil defined below has the same limits, retaining its largest \((q+2)n-j\) singular values and normalizing by \(1/N\).
Moreover \((h_n/N)\log^-t_{2h_n+1}\to0\) in disk integral and at these prescribed moving parameters.

For the full matrix, almost-sure weak convergence of the eigenvalue measures to the Brown measure of \(P(s_1,s_2)\) under every coupling is therefore equivalent to
\[
 \sum_N\Pr\left\{
 \frac1N\int_{|w|\le R}\sum_{i=1}^{h_N}\log^-t_i(w)\,dA(w)>\epsilon
 \right\}<\infty
 \qquad(R,\epsilon>0).
 \tag{T2}
\]
Here \(\log^-0:=+\infty\), and omission of finitely many small dimensions is understood.
The series (T2) is not estimated here.

<a id="left-statement"></a>
## A left directional estimate at every fixed degree

Fix an integer \(q\ge2\) and \(R<\infty\).
Let \(X_N,Y_N\) be independent real symmetric Wigner matrices under the fixed-law, finite-second-moment [contract](../tasks/Yin_T_F0012_v3.md#contract), with the original \(N^{-1/2}\) normalization.
For each \(N\), prescribe at most \(N\) nested principal site sets, all of whose sizes \(l\) satisfy \(l/N\to1\) uniformly.
Write \(X,Y\) for the restrictions to any one of these sets.
There is no restriction on coupling between dimensions.

Index \(q+2\) channels by \(0,\ldots,q+1\).
Define the affine pencil \(L_q(w)\) by its nonzero blocks
\[
 (L_q)_{00}:=(1-w)I,\quad (L_q)_{01}:=X,\quad
 (L_q)_{0,q+1}:=Y,
\]
\[
 (L_q)_{jj}:=-I\ (1\le j\le q+1),\qquad
 (L_q)_{j,j+1}:=X\ (1\le j<q),\qquad
 (L_q)_{q,0}:=Y,\quad (L_q)_{q+1,0}:=X.
\]
Its scalar Schur complement is \(I+X^qY+YX-wI\).
For \(a\in\mathbb C^{q+2}\) and \(\ell=(\ell_0,\ldots,\ell_{q+1})\), define
\[
 D_X(a,\ell):=\sum_{j=0}^{q-1}a_{j+1}\ell_j+a_0\ell_{q+1},
 \qquad
 D_Y(a,\ell):=a_{q+1}\ell_0+a_0\ell_q.
 \tag{1}
\]
These are the two unnormalized adjoint color coefficients of the actual upper physical border; conjugating all components of \(a\) gives the equivalent adjoint convention.

Put \(B:=100(q+1)^2\).
There are measurable exceptional events \(\mathcal B_N\), with \(\sum_N\Pr(\mathcal B_N)<\infty\), such that for all sufficiently large \(N\) outside \(\mathcal B_N\), simultaneously for the prescribed minors, \(|w|\le R\), and complex unit vectors \(a,\ell\),
\[
 \|L_q(w)^*\ell\|\le N^{-6B}
 \quad\Longrightarrow\quad
 \big(\|D_X(a,\ell)\|^2+\|D_Y(a,\ell)\|^2\big)^{1/2}
 \ge N^{-4B}.
 \tag{2}
\]
Each minor's usable event depends only on that minor's two inputs.
The simultaneous exception bound is unconditional, so these old-minor events may be used before exposing its fresh border, without conditioning that border on success at future sizes.
The conclusion holds eventually almost surely under every allowed cross-dimensional coupling.

At general fixed \(q\), assertion (2) is a left estimate only.
The proof of (T1) combines it with a right estimate restricted to four selected fresh channels and an unequal-border volume comparison.

<a id="argument"></a>
<a id="linear-test"></a>
## A linear test in the independent symmetric input

We first prove a conditional estimate needed on small spectral subspaces of \(X\).
Suppose a deterministic real symmetric \(l\)-by-\(l\) matrix \(X\) has at least \(\kappa l\) eigenvalues in each of
\(I_+:=[1/2,3/2]\) and \(I_-:=[-3/2,-1/2]\), where \(\kappa>0\) is fixed and \(l/N\to1\).
Let \(Q\) be its spectral projection onto \(I_+\cup I_-\).
For every deterministic real unit vector \(u\), real vector \(b\), and real target \(z\),
\[
 \Pr\{\|Q(XYu+Yb)-z\|<c\sqrt{1+\|b\|^2}\mid X\}
 \le Ce^{-cl}.
 \tag{3}
\]
The constants depend only on \(\kappa\) and the fixed strict upper law of \(Y\), and the target can also absorb its exposed diagonal coordinates.

Here is the deterministic singular-value calculation behind (3).
For \(i<j\), let \(H_{ij}:=e_ie_j^{\mathsf T}+e_je_i^{\mathsf T}\), and form the coefficient matrix with columns \(Q(XH_{ij}u+H_{ij}b)\).
Temporarily add the diagonal basis matrices \(H_{ii}:=\sqrt2e_ie_i^{\mathsf T}\).
The covariance sum of all these deterministic columns is
\[
 Q\big[X^2+2\alpha X+\|b\|^2I+T\big]Q,
 \qquad \alpha:=\langle u,b\rangle,
\]
\[
 T:=(Xu)(Xu)^{\mathsf T}+bb^{\mathsf T}
       +(Xb)u^{\mathsf T}+u(Xb)^{\mathsf T},\qquad
 \operatorname{rank}T\le4.
 \tag{4}
\]
This identity is just summation over the displayed symmetric matrix basis; no Gaussian input is introduced into the probability model.
Set \(s^2:=1+\|b\|^2\) and \(\beta^2:=\|b\|^2-\alpha^2\ge0\).
The scalar part of (4) is \((X+\alpha I)^2+\beta^2I\).
If \(\alpha\ge0\), on \(I_+\) it is at least \(s^2/8\), and if \(\alpha<0\), the same lower bound holds on \(I_-\).
The rank-four correction therefore leaves at least \(\kappa l-4\) eigenvalues above \(s^2/8\).

The sum of the squared norms of the added diagonal columns is at most
\[
 4\big(\|QX\|^2\|u\|^2+\|b\|^2\big)\le 13s^2.
\]
Its positive covariance has at most \(208\) eigenvalues greater than \(s^2/16\).
Removing these diagonal columns thus leaves at least \(\kappa l-212\) eigenvalues at least \(s^2/16\), by intersecting the corresponding spectral subspaces.
For large \(l\), the strict upper coefficient matrix has at least \(\kappa l/2\) singular values at least \(s/4\).
After the original normalization these values are at least \(s/(4\sqrt N)\).

Condition on all diagonal entries of \(Y\).
The remaining raw strict upper coordinates are independent with their fixed centered variance-one law.
Project the input onto the right singular directions just obtained, and use the [finite-variance projection estimate](Yin_C_F0186_v41.md#flattening), with its arbitrary fixed translation.
That estimate depends on the projection's rank and coordinate weights, not on the number of raw coordinates, so it applies to the \(l(l-1)/2\) coordinates here.
Explicitly, a fixed cutoff leaves independent bounded coordinates of positive conditional variance, retains a fixed fraction of the projection trace outside \(Ce^{-cl}\), and the convex bounded-product estimate gives an order-\(\sqrt l\) norm floor, uniformly in the conditioned shifts.
Multiplication by \(s/(4\sqrt N)\) proves (3), and integration over the diagonal removes that conditioning.

For a complex unit vector \(u\), at least one of its real and imaginary parts has norm at least \(1/\sqrt2\).
Apply (3) to that real part after normalization, with \(b=X^qu\) interpreted in the same real part and with the corresponding part of any complex target.
Consequently, for every fixed complex unit \(u\) and complex \(t\),
\[
 \Pr\{\|(YX^q+XY-tI)u\|<c\mid X\}\le Ce^{-cl}.
 \tag{5}
\]
In this passage (3) is applied to the target after compression by \(Q\); contraction then gives the displayed uncompressed bound.

<a id="thin-spaces"></a>
## Uniform tests on finitely many spectral slices

Use the full Frobenius guard \(\max(\|X_N\|,\|Y_N\|)\le K:=N^2\), whose failure probability is \(O(N^{-3})\).
It bounds every prescribed principal restriction.
Fix a sufficiently small \(0<\gamma<1/4\), let \(\delta:=N^{-\gamma}\), and use a \(\delta\)-grid in \([-K-2,K+2]\) with intervals of radius \(2\delta\).
The [uniform real-center count](Yin_C_F0351_v12.md#real-trim) implies, except with summable probability over the prescribed minors, that each interval contains at most \(Cl/\log^2N\) eigenvalues of \(X\), with multiplicity.
The [finite-variance weak law](Yin_C_F0186_v4.md#finite-variance-weak) and its [row-rank concentration](Yin_C_F0186_v4.md#row-concentration) give the two fixed positive bulk counts required above, uniformly over these minors, except with summable probability.
Indeed their expected normalized interval counts tend to the positive semicircle masses, and a fixed smaller count fails with \(Ce^{-cl}\) for each minor.

Let \(E\) be the complexification of the real spectral span of any union of at most \(q\) grid intervals.
Its complex dimension is \(O_q(l/\log^2N)\).
Condition on \(X\) with these two count properties.
A net of mesh \(N^{-(2q+10)}\) of the complex unit sphere of \(E\), together with a net of that mesh in \(\{|t|\le R+1\}\), has logarithmic size \(o(l)\).
On the norm guard the operator \(YX^q+XY-tI\) has norm at most \(C_RK^{q+1}\), so the net approximation error is \(o(1)\).
Apply (5) to these fixed net points before adding any norm-guard exception.
There are only polynomially many choices of the grid intervals and prescribed minors.
We obtain, outside summable exceptions, simultaneously for these spaces and \(|t|\le R+1\),
\[
 \|(YX^q+XY-tI)u\|\ge c_*\|u\|\qquad(u\in E).
 \tag{6}
\]

On the same collection of spaces the [independent-row escape proof](Yin_C_F0362_v1.md#escape) gives
\[
 \|(I-\Pi_E)Yu\|\ge c_*\|u\|\qquad(u\in E).
 \tag{7}
\]
Its proof applies unchanged to this fixed number of intervals: the real unit-vector and target nets still have logarithmic size \(O_q(l/\log N)=o(l)\), and the rectangular row bound is uniform in the fixed target.
Real and imaginary parts give (7) on the complexification.
The constants in (6) and (7) may be decreased to a common positive value.
In particular, (7) excludes a complex unit vector whose distances of \(u\) and \(Yu\) from \(E\) are respectively \(o(K^{-1})\) and \(o(1)\).
All probability estimates were conditional only on the actual old first input and, where indicated, the old second-input diagonal; the norm guards were added afterwards.

<a id="direction"></a>
## The left graph and both sizes of the leading coefficient

Suppose a unit left near-mode and a unit direction violate (2).
The auxiliary equations of \(L_q(w)^*\ell\) give the graph
\[
 (u,Xu,X^2u,\ldots,X^qu,Yu)
\]
with \(u=\ell_0\) exact and total error at most \(C_qK^{q-1}N^{-6B}\).
Thus \(\|u\|\ge N^{-(2q+1)}\) for large \(N\).
Divide the graph by \(\|u\|\) and henceforth take \(u\) to be a physical unit vector.
The scalar residual and the two border inequalities then imply
\[
 \|(YX^q+XY-(\bar w-1)I)u\|\le N^{-5B},
 \tag{8}
\]
\[
 \|p(X)u+a_0Yu\|\le e:=N^{-3B},\qquad
 \|(a_{q+1}+a_0X^q)u\|\le e,
 \qquad p(x):=\sum_{j=1}^qa_jx^{j-1}.
 \tag{9}
\]
For these estimates the graph substitution costs at most \(C_qN^{4q+1}N^{-6B}\) in (8), and at most \(C_qN^{2q+1}(N^{-4B}+K^{q-1}N^{-6B})\) in (9); the chosen \(B\) absorbs the constants for large \(N\).

If \(|a_0|\ge N^{-B}\), divide (9) by \(a_0\).
Choose \(E\) from the at most \(q\) complex roots of \(x^q+a_{q+1}/a_0\), keeping a grid interval about a root's real part only if some real spectral point is within \(\delta\) of that root.
Outside this union every root factor has modulus at least \(\delta\).
Therefore
\[
 \|(I-\Pi_E)u\|\le N^{-2B}\delta^{-q},
\]
\[
 \|(I-\Pi_E)Yu\|\le N^{-2B}
       +qN^BK^{q-1}N^{-2B}\delta^{-q}.
\]
These are \(o(K^{-1})\) and \(o(1)\), contradicting (7).

If \(|a_0|<N^{-B}\), the second inequality of (9) gives
\( |a_{q+1}|\le e+N^{-B}K^q=o(1)\).
Since \(a\) is unit, the coefficient vector of \(p\) has Euclidean norm at least \(1/2\) for large \(N\), while
\[
 \|p(X)u\|\le e+N^{-B}K\le2N^{-B+2}.
 \tag{10}
\]
This estimate does not require a lower bound on the leading coefficient of \(p\).
To see this, write its actual degree as \(d\le q-1\) and factor \(p(x)=c_d\prod_{j=1}^d(x-z_j)\).
The coefficient norm bound gives
\( |c_d|\prod_j(1+|z_j|)\ge1/2\).
For \(|x|\le K\) outside the grid slices attached to its roots,
\[
 \frac{|x-z_j|}{1+|z_j|}\ge\frac{\delta}{2K+2},\qquad
 |p(x)|\ge\frac12\left(\frac{\delta}{2K+2}\right)^{q-1}.
 \tag{11}
\]
For \(|z_j|\le2K+1\) this follows from the distance \(\delta\); for larger roots the ratio is at least \(1/2\).
The same lower bound holds for a nonzero constant \(p\), with an empty union.
Let \(E\) be this union of at most \(q-1\) slices.
Equations (10) and (11) give
\[
 \|(I-\Pi_E)u\|\le C_qN^{-B+2+(2+\gamma)(q-1)}.
 \tag{12}
\]
In particular \(\|\Pi_Eu\|=1-o(1)\).
Equations (8), (12), and the norm bound \(C_RK^{q+1}\) yield
\(\|(YX^q+XY-(\bar w-1)I)\Pi_Eu\|=o(1)\), contradicting (6).
Both cases are impossible, proving (2).

<a id="restricted-right"></a>
## Four right directions suffice

Take a fixed \(q\ge2\), retain \(B=100(q+1)^2\), and restrict the fresh direction to
\(a_1=\cdots=a_{q-2}=0\), with no erased component when \(q=2\).
Its four possible channels are \(S:=\{0,q-1,q,q+1\}\).
Fix a compact set \(|w|\le R\), \(|\operatorname{Im}w|\ge\eta>0\).
The corresponding right graph is
\((v,X^{q-1}Yv,X^{q-2}Yv,\ldots,Yv,Xv)\).
A failed right directional floor \(N^{-4B}\) on a unit right near-mode of residual at most \(N^{-6B}\) would give, by the same graph normalization,
\[
 \|a_{q+1}v+(a_0X^{q-1}+a_{q-1})Yv\|\le e,\qquad
 \|(a_q+a_0X)v\|\le e,
 \qquad e=N^{-3B},
 \tag{13}
\]
together with \(\|(X^qY+YX-(w-1)I)v\|\le N^{-5B}\), where \(v\) is now a physical unit vector.
For \(|a_0|\ge N^{-B}\), take the union of the slice about \(-a_q/a_0\) and the at most \(q-1\) root slices of \(x^{q-1}+a_{q-1}/a_0\).
Writing its projection as \(\Pi\), (13) gives
\[
 \|(I-\Pi)v\|\le N^{-2B}\delta^{-1},\qquad
 \|(I-\Pi)Yv\|\le\delta^{-(q-1)}
       \big(N^{-2B}+N^BN^{-2B}\delta^{-1}\big).
\]
These contradict (7).

For \(|a_0|<N^{-B}\), (13) instead gives
\[
 |a_q|\le e+N^{-B}K,\qquad
 \|a_{q-1}Yv+a_{q+1}v\|\le e+N^{-B}K^q.
\]
Since \(a\) is unit and supported on \(S\), \(|a_{q-1}|\ge(4K)^{-1}\) for large \(N\); otherwise \(|a_{q+1}|\le1/4+o(1)\).
The real Rayleigh quotient \(\mu:=\langle v,Yv\rangle\) minimizes \(\|(Y-z)v\|\) over complex \(z\), so
\[
 \|(Y-\mu)v\|\le4K(e+N^{-B}K^q).
 \tag{14}
\]
Replacing \(Yv\) by \(\mu v\) in
\(\langle v,(X^qY+YX)v\rangle=\langle X^qv,Yv\rangle+\langle Yv,Xv\rangle\)
changes it by at most \((K^q+K)\|(Y-\mu)v\|=o(1)\) and leaves a real number.
The scalar residual then contradicts \(|\operatorname{Im}w|\ge\eta\).
Thus the right directional floor holds uniformly on the whole right near-null subspace for every unit direction supported on \(S\).

The unrestricted right floor is not asserted for \(q>2\).
At \(q=3\), allowing \(a_1\ne0\) leaves the relation \((a_1X+a_2)Yv+a_4v\approx0\) in the small-\(a_0\) branch; it need not force one-vector Rayleigh localization.
The following compression avoids needing that assertion.

<a id="rectangular-step"></a>
## Adding a physical site through a rectangular compression

Put \(p:=q+2\), add one physical site to an old \(l\)-site principal pair, and permute coordinates so its full pencil is
\[
 L'=\begin{pmatrix}L&U\\ V^*&D\end{pmatrix},
 \qquad U,V\in\mathbb C^{pl\times p}.
\]
Keep every old coordinate, all \(p\) new columns, and only the four new rows in \(S\), obtaining the rectangular compression
\[
 B_S:=\begin{pmatrix}L&U\\ V_S^*&D_{S,:}\end{pmatrix}
 \quad\hbox{of size }(pl+4)\hbox{ by }(pl+p).
\]
For every \(j\), singular-value monotonicity under compression gives \(p_j(L')\ge p_j(B_S)\), where \(p_j\) multiplies the largest \(j\) singular values.
The two borders in this compressed matrix use the actual shared fresh \(X,Y\) entries at their original scale.

For an old retained index \(r\), let \(d:=pl-r\ge4p\).
Use the [rectangular paired-volume inequality](Yin_C_F0366_v1.md#statement) with \(a=p\) columns and \(b=4\) rows: its left projection removes the first \(r+p\) old singular directions and its right projection removes the first \(r\).
If fewer than \(d/2\) old singular values are at most \(\tau:=N^{-6B}\), then at least \(r+p+4\) old singular values exceed \(\tau\), and compression monotonicity already gives
\(p_{r+p+4}(L')\ge p_r(L)\tau^{p+4}\).
Otherwise each relevant projected tail contains at least \(\lfloor d/4\rfloor\) low singular directions.
The left floor (2) and the restricted right floor above give at least that many singular values at least \(\rho:=N^{-4B}\) for each direction's raw input map, by min--max on those low singular spaces.

Apply the [fresh-input projection estimate](Yin_C_F0186_v41.md#flattening) to the stacked independent strict upper color columns.
For each fixed unit direction in \(\mathbb C^p\) on the left or \(\mathbb C^4\) on the right, their normalized projected image has norm at least \(c\rho\sqrt{d/N}\), except with conditional probability \(Ce^{-cd}\).
Their raw combined norm exceeds \(N^2\) with conditional probability \(O(N^{-3})\).
On its complement nets of mesh \(N^{-(4B+5)}\) in these fixed-dimensional complex unit spheres extend the bounds to all directions, decreasing the polynomial floors if necessary.
Indeed the normalized border map is \(O(N^{3/2})\)-Lipschitz in the direction, while the fixed-direction floor is at least a constant times \(N^{-4B-1/2}\).
The left \(p\)-column volume and right four-column volume are consequently bounded below by fixed powers of \(N^{-1}\).
Intersect their successes by a union bound; the upper and lower borders are allowed to share every fresh random variable.
The paired estimate and the compression into \(L'\) give
\[
 p_{r+p+4}(L')\ge N^{-C}p_r(L),
 \tag{15}
\]
except with conditional probability \(CN^Ce^{-cd}+CN^{-3}\) on the old-measurable guards, independently of the corner block.
Whole-chain old-guard and norm failures are added separately, without conditioning the fresh border on future success.
The full pencil gains \(p=q+2\) coordinates while the retained index gains \(p+4\), so the deficit decreases by four for every fixed \(q\).

<a id="trim"></a>
## Initialization, iteration, and scalar transfer

At the target size \(n\), put \(m:=\lfloor n/\log^3(n+3)\rfloor\) and begin at \(l:=n-m\) sites with deficit \(d_0:=4m+j\), for \(j=h_n\) or \(2h_n\).
After \(m\) steps (15) the full \(p\)-channel pencil has deficit \(j\).
The accumulated logarithmic cost is \(O(m\log N)=o(N)\).
The conditional exceptions over the chain are summable in \(N\), since \(d\ge h_n\), \(h_n/\log N\to\infty\), and \(mN^{-3}\le N^{-2}\).
The old events established above also have summable simultaneous exceptions.

For each prescribed \(w_N\to w\notin\mathbb R\), initialize using the [affine polynomial-window argument](Yin_C_F0186_v42.md#old-trim) on the canonical \(l\)-dimensional pencils \(L_q(w_N;s x,s y)\), where \(s:=\sqrt{l/N}\to1\).
Their scalar Schur complement is
\(1+s^{q+1}x^qy+s^2yx-w_N\), a nonzero free polynomial for every complex shift and \(1/2\le s\le2\).
Thus this compact family is full.
The [uniform free count](Yin_C_F0352_v1.md#statement) and [finite bounded-background comparison](Yin_C_F0195_v4.md#free-background) give the same polynomial window as in that initialization argument.
At a sufficiently small inverse-power clip the expected small-value count is \(o(l/\log^3N)\), and original row-rank concentration makes its exceedance of \(d_0\) summably unlikely.
Layer integration, fixed-clip convergence, and the affine second-moment positive-log bound give convergence of the clipped normalized log.
The omitted positive terms are \(o(N)\): their number is \(o(l)\) and their values are bounded by the eventually bounded bottom median.
Consequently the initial retained logarithm has lower limit at least \(u(w)\), with physical normalization \(1/N\).
The \(p\)-channel free logarithm equals \(u(w)/p\), by its unit triangular Schur elimination and [bounded determinant multiplicativity](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation).
Its trace factor in this initialization is \(pl/N\to p\).
Equation (15) propagates the same lower bound to the target.
At the target a fixed lower clip bounds the retained log above with error \(j|\log d|/N\), for \(0<d<1\); then let \(d\downarrow0\).
This proves both prescribed moving-parameter limits for the companion.

On the norm guard the finite triangular Schur factors and their inverses have polynomial norms in \(N\), uniformly for \(w\) on a disk.
They reduce the companion to \(\operatorname{diag}(M-wI,-I,\ldots,-I)\), with \(q+1\) auxiliary identity blocks, and preserve absolute determinants.
The [omitted-factor comparison](Yin_C_F0186_v41.md#assembly) therefore changes the retained logarithm by \(O(j\log N)\), including at singular shifts by continuity.
Removing the auxiliary unit singular values costs at most the same order.
This proves the scalar moving limits.

For local planar convergence apply Fubini first at fixed nonreal parameters.
The companion's normalized positive-log sum is eventually bounded on each disk almost surely, by the affine second-moment bound and capped row concentration, as in the [local planar initialization argument](Yin_C_F0186_v42.md#old-trim).
Its trimmed log is bounded above by that sum and below by the normalized scalar characteristic log minus that sum.
The negative part of the normalized characteristic log has uniformly bounded disk \(L^2\) norm by Jensen applied to \(\log^-|w-\lambda|\), since \(n/N\le1\).
These bounds give uniform integrability, hence the companion and scalar limits (T1).
Finally
\[
 h_n\log^-t_{2h_n+1}\le N(b_{2h_n}-b_{h_n})
          +\sum_{i=h_n+1}^{2h_n}\log^+t_i
\]
gives the adjacent loss, because its final sum is \(O(h_n\log N)\) on each disk under the norm guard.
Subtracting the ordinary scalar potential from \(b_{h_N}\) gives the bottom negative-log sum up to \(O(h_N\log N/N)\).
The [pathwise scalar potential criterion](Yin_C_F0186_v4.md#remaining-defect), first Borel--Cantelli for sufficiency under every coupling, and second Borel--Cantelli under independent dimensions for necessity give (T2).

## Current assessment
[Selected decision](#decision-word-trims-reviewed)

## Assessment history

### Decision word-trims-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T20:53 |
| status | open |
| reason | The conditional symmetric-input test proves the left floor, four selected right directions avoid the unresolved branches, and the unequal-border comparison decreases the singular deficit at every fixed degree. This is a complete candidate trim proof; separate mathematical review and the terminal-loss estimates remain pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Fixed-degree word trims](#statement) | Every fixed degree parameter at least two, original real finite-variance laws, prescribed minors, moving nonreal parameters, planar limits, adjacent loss and terminal equivalence. |
| argument | [Conditional test and complete trim proof](#argument) | Strict-upper covariance, finite-variance input projection, left and restricted-right floors, rectangular compression and initialization. |
| support | [Fixed-degree left estimate](#left-statement) | The left directional floor holds for every fixed degree and all bounded complex shifts. |
| support | [Unequal fresh borders](#rectangular-step) | All left channels and four right channels reduce the deficit by four at every physical addition. |

### Decision word-trims-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T20:57 |
| status | proved |
| reason | The independent symmetric-input test supplies the full left floor and four right directions, and the unequal-volume step proves both principal trims at every fixed power. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Principal logarithmic trims](#statement) | Every fixed integer q at least two and original real finite-variance inputs. |
| argument | [Complete proof](#argument) | Conditional covariance, spectral windows and the physical row addition. |
| support | [Initialization and limits](#trim) | Two trim levels, adjacent logarithm and the exact terminal equivalence. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0375_v1.md#word-trims-whole-proof) | The fixed statement and all dependent estimates. |

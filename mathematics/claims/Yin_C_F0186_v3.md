---
author: Yin
---

# Almost-sure and mean determinant convergence for GUE pencils

This version strengthens the affine [v2 theorem](Yin_C_F0186_v2.md#statement) and the scalar-polynomial [v1 theorem](Yin_C_F0186_v1.md#statement).
The exact strengthened Brown-measure objective is [F0012 v2](../tasks/Yin_T_F0012_v2.md#contract).
The preceding mathematical versions and their actual adoption/review scopes remain preserved.
No novelty or priority claim is made.

<a id="statement"></a>
## Exact strengthened conclusions

Fix \(d,m\ge1\) and \(A_0,\ldots,A_d\in M_m(\mathbb C)\), independent of \(N\).
On a common probability space, for each \(N\), let \(H_1^{(N)},\ldots,H_d^{(N)}\) be independent Hermitian GUE matrices with density proportional to \(\exp(-N\operatorname{Tr}(H^2)/2)\).
There is no restriction on the coupling between different sizes.
Let \(s_1,\ldots,s_d\) be free centered semicircular elements of variance one in a finite von Neumann algebra with faithful normal tracial state \(\tau\), and set
\[
 L_N=A_0\otimes I_N+\sum_{j=1}^d A_j\otimes H_j^{(N)},\qquad
 L=A_0\otimes1+\sum_{j=1}^d A_j\otimes s_j,\qquad
 \tau_m=\operatorname{tr}_m\otimes\tau.
\]
Use the [ordinary determinant convention](../audits/literature/MS24/Yin_U001.md#determinant-convention), where \(\operatorname{tr}_m=\operatorname{Tr}_m/m\), \(\log0=-\infty\), and \(\exp(-\infty)=0\).
Put
\[
 U_N=\frac1{mN}\log|\det L_N|,\quad
 u=\tau_m(\log|L|)\in[-\infty,\infty),\quad
 D_N=|\det L_N|^{1/(mN)}.
\]
Then, for every such coupling,
\[
 U_N\longrightarrow u\quad\text{almost surely},\qquad
 D_N\longrightarrow e^u=\Delta_{\tau_m}(L)\quad\text{almost surely}.
 \tag{AS}
\]
If \(u>-\infty\), \(U_N\) is integrable for all sufficiently large \(N\), and
\[
 \mathbb E|U_N-u|\longrightarrow0,\qquad \mathbb E U_N\longrightarrow u.
 \tag{Mean}
\]
If \(u=-\infty\), its positive part is integrable, so \(\mathbb E U_N\in[-\infty,\infty)\) is well defined, and \(\mathbb E U_N\to-\infty\).
There is no \(L^1\) distance to minus infinity.
The almost-sure assertion in that case means eventual decrease below each finite negative threshold, without requiring monotonicity of the sequence.
For every fixed \(0<p<\infty\), also \(\mathbb E|D_N-e^u|^p\to0\), including \(u=-\infty\).

A quantitative input for finite \(u\) is the following global estimate.
There are \(b,C,\varepsilon_0>0\) and \(N_0\), depending on the fixed coefficients, such that
\[
 \mathbb P\{s_{\min}(L_N)\le\varepsilon\}
 \le C N^{5/2}\varepsilon^b
 \quad\text{if }N\ge N_0,\quad 0<\varepsilon\le\varepsilon_0,\quad
 N^{5/2}\varepsilon^b\le1.
 \tag{Global}
\]
In particular, this estimate has no error term independent of \(\varepsilon\).

Finally, for every fixed scalar polynomial \(P\in\mathbb C\langle x_1,\ldots,x_d\rangle\) in self-adjoint indeterminates, the empirical eigenvalue probability measures of \(P(H^{(N)})\), with algebraic multiplicities, converge weakly almost surely to the Brown measure of \(P(s)\).
For each fixed \(P\) and each allowed coupling, there is a single event of probability one on which convergence holds against every bounded continuous real test function on \(\mathbb C\).
That event may depend on \(P\); no simultaneous assertion over all polynomial coefficients is made.

The coefficients may be nonnormal, and \(A_0\) may be singular.
No irreducibility or one-step covariance lower bound is imposed.
All coefficient sizes, degrees and coefficient values remain fixed.
The results do not concern a complex determinant phase or an ensemble other than the stated GUE law.

<a id="inputs"></a>
## Inputs and actual source scope

The accepted prior results are [v2's affine probability theorem](Yin_C_F0186_v2.md#statement) and its [complete argument](Yin_C_F0186_v2.md#argument), particularly eventual nonidentity of the affine determinant, the finite list of compressed quadratic maps, and the mesoscopic expected counting bound.
The geometric inputs are the real polynomial inequality (KSS) in [v1's error-bound section](Yin_C_F0186_v1.md#error-bound) and the exact uniform-ball bound with regular-level extension in [v1's tube section](Yin_C_F0186_v1.md#tubes).
The exact scalar word-chain linearization and known pointwise convergence in probability of scalar logarithmic potentials are used from [v1's polynomial application](Yin_C_F0186_v1.md#polynomial-application).
These uses do not assume the stronger conclusions being proved here.

For Gaussian concentration and a source comparison for norm control, the retained [CGP22 original](../literature/pdf/CGP22--arxiv-v1.pdf), arXiv:1912.04588v1, was inspected at Proposition 4.4 on PDF p. 30, its real GUE coordinates on p. 31, and Proposition 2.11 on p. 10.
Its Corollary 1.3 on p. 5 and the matrix-valued algebraicity/Puiseux input of SS15 have the exact scope already recorded in v2.
The new Gaussian-mixture calculation and the treatment of empty compressed zero types are proved below, rather than attributed to those sources.

The singular-value perturbation statement and proof were inspected in [Mec19, Corollary 4.39, p. 47](../literature/pdf/Mec19.pdf#page=47), with [edition and inspection scope](../audits/literature/Mec19/readme.md).
A complete elementary proof of the exact Frobenius case used here is included below.
The optional direct free determinant identity later uses the [retained bounded multiplicativity theorem](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation); the main Brown-measure implication instead uses uniqueness of already-established probability limits.
The primary proofs behind the accepted KSS, Lotz, Gaussian concentration, CGP resolvent and SS algebraicity statements are not newly audited in full.
First Borel--Cantelli, Tonelli/Fubini, elementary Gaussian integration and finite-dimensional spectral identities are used in their standard stated domains.

<a id="argument"></a>
## Complete strengthened argument

Let \(\nu_N\) be the empirical law of \(L_N^*L_N\), normalized by \(1/(mN)\), and let \(\nu\) be the law of \(L^*L\) under \(\tau_m\).
Their weak convergence in probability and fixed-regularizer convergence are available from v2 before any logarithmic-tail argument.
All probability estimates below use only the within-size law.
If every random coefficient is zero, the affine logarithms and root determinants equal their free values identically.
For finite \(u\) in that deterministic case, choose \(\varepsilon_0<s_{\min}(A_0)\) for (Global).
Thus the affine conclusions in that case are immediate; the concentration argument below may assume at least one random coefficient is nonzero.

## Gaussian concentration already present in CGP22

Source: [CGP22, arXiv:1912.04588v1](../literature/pdf/CGP22--arxiv-v1.pdf), PDF p. 30, Proposition 4.4.
The original statement was read directly.
For a real \(K\)-Lipschitz function \(F\) on Euclidean space and a vector \(g\) of independent standard real Gaussians, it states
\[
 \mathbb P\{F(g)-\mathbb EF(g)\ge t\}\le
 \exp\!\left(-\frac{t^2}{2K^2}\right),\qquad t>0.
\]
Applying it separately to \(F\) and \(-F\) gives the two-sided bound with prefactor two.
The proposition attributes the standard concentration result to its reference [2], Lemma 2.3.3; that underlying proof was not re-audited.

CGP22 PDF p. 31 explicitly uses the Gaussian coordinates
\(\sqrt N H_{rr}\), \(\sqrt{2N}\Re H_{rs}\), and \(\sqrt{2N}\Im H_{rs}\), for \(r<s\).
These are precisely the Hilbert--Schmidt orthonormal real coordinates for the normalization in F0012.
Consequently
\[
 \|H(g)-H(g')\|_{\mathrm{HS}}=N^{-1/2}|g-g'|.
\]
For independent inputs, squared Hilbert--Schmidt distances add across the tuple.

## GUE norm tails and moments from the same original

CGP22 PDF p. 10, Proposition 2.11, was read directly.
It gives constants \(D,\alpha>0\) such that for every \(N\ge1\) and \(u\ge0\),
\[
 \mathbb P\{\|H^{(N)}\|\ge D+u\}\le e^{-\alpha uN}.
 \tag{N1}
\]
It also states a moment bound \(\mathbb E\|H^{(N)}\|^k\le C^k\) for \(k\le\alpha N/2\).
The source's original proof is an accepted external input at that statement.

For the present applications, (N1) itself implies
\[
 \sup_N\mathbb E\|H^{(N)}\|^p<\infty
 \quad\text{for every fixed }p>0,
 \qquad
 \sup_N\mathbb E\|H^{(N)}\|\le C_0:=D+\alpha^{-1}.
\]
This follows by integrating the tail, using \(e^{-\alpha uN}\le e^{-\alpha u}\).
In standard Gaussian coordinates, \(g\mapsto\|H(g)\|\) is globally \(N^{-1/2}\)-Lipschitz, since the operator norm is bounded by the Hilbert--Schmidt norm.
Proposition 4.4 therefore gives the additional local deduction
\[
 \mathbb P\{\|H^{(N)}\|\ge C_0+t\}
 \le e^{-Nt^2/2},\qquad t>0.
\]
In particular, for \(M\ge2C_0\),
\[
 \mathbb P\{\|H^{(N)}\|>M\}\le e^{-NM^2/8}.
 \tag{N2}
\]
A union bound supplies the factor \(d\) for a fixed tuple of \(d\) inputs.
The fixed-cutoff exceptional probabilities are summable in \(N\), and the estimate applies to a cutoff depending on a small-singular-value parameter.
Neither summability nor the first Borel--Cantelli lemma requires independence across matrix sizes.


<a id="singular-value-perturbation"></a>
## Singular-value Frobenius perturbation inequality

For \(A,B\in M_k(\mathbb C)\), let \(a_1\ge\cdots\ge a_k\ge0\) and \(b_1\ge\cdots\ge b_k\ge0\) be their singular values.
Then
\[
 \sum_{i=1}^k(a_i-b_i)^2\le\|A-B\|_{\mathrm{HS}}^2.
 \tag{SV}
\]
An inspected author-hosted formulation with proof is Mark W. Meckes, *Lecture notes on matrix analysis*, 27 April 2019, [Corollary 4.39, printed/PDF p. 47](https://case.edu/artsci/math/mwmeckes/matrix-analysis.pdf#page=47).
That corollary permits rectangular complex matrices and every corresponding symmetric-gauge/unitarily-invariant norm; (SV) is its Euclidean/Frobenius specialization.
The source statement and its Hermitian-dilation proof were read, without a whole-notes audit.
The retained [Mec19 original and source note](../audits/literature/Mec19/readme.md) provide the actual selected edition and inspection boundary.

For a self-contained proof of precisely (SV), write \(A=U\operatorname{diag}(a)V^*\) and \(B=W\operatorname{diag}(b)Z^*\), with unitary factors.
Set \(C=U^*W\), \(D=V^*Z\), and \(w_{ij}=|C_{ij}||D_{ij}|\).
Every row and every column sum of \(w\) is at most one, by Cauchy--Schwarz.
Thus
\[
 \Re\operatorname{Tr}(A^*B)\le\sum_{i,j}a_i b_jw_{ij}.
\]
Put \(a_{k+1}=b_{k+1}=0\), \(\Delta a_p=a_p-a_{p+1}\ge0\), and \(\Delta b_q=b_q-b_{q+1}\ge0\).
The bound on row and column sums yields
\[
 \sum_{i,j}a_i b_jw_{ij}
 =\sum_{p,q}\Delta a_p\Delta b_q\sum_{i\le p,j\le q}w_{ij}
 \le\sum_{p,q}\Delta a_p\Delta b_q\min(p,q)
 =\sum_i a_i b_i.
\]
Expanding \(\|A-B\|_{\mathrm{HS}}^2=\sum_i a_i^2+\sum_i b_i^2-2\Re\operatorname{Tr}(A^*B)\) proves (SV).
This uses only singular-value decomposition, Cauchy--Schwarz and finite summation.

If \(h:[0,\infty)\to\mathbb R\) is \(L_h\)-Lipschitz, (SV) immediately gives
\[
 \left|\frac1k\sum_i h(s_i(A))-\frac1k\sum_i h(s_i(B))\right|
 \le\frac{L_h}{\sqrt k}\|A-B\|_{\mathrm{HS}}.
 \tag{SA}
\]
This is the normalization needed for a scalar average over all \(k=mN\) singular values.


<a id="tube-without-floor"></a>
## Gaussian tubes without an additive error

Let \(q\) be a nonzero nonnegative real polynomial on \(\mathbb R^n\) of degree at most \(D\ge1\), and let \(Z=q^{-1}(0)\).
If \(Z\) is empty, all the following bounds hold trivially.
For a point uniform in the radius-\(s\) ball, the codimension-one Lotz bound with the already proved regular-level extension is
\[
 \mathbb P\{\operatorname{dist}(x,Z)\le\rho\}
 \le4\left[\left(1+\frac{(2D+1)\rho}{s}\right)^n
             -\left(1+\frac{\rho}{s}\right)^n\right].
 \tag{T1}
\]
This is the binomial form of the sum in v1 (T1), valid for every positive \(s,\rho\).

A standard Gaussian \(g\in\mathbb R^n\) is exactly the mixture of uniform points in radius-\(S\) balls, where \(S\) has the chi distribution with \(n+2\) degrees of freedom.
For integers \(0\le k\le n\),
\[
 \mathbb E S^{-k}=2^{-k/2}
 \frac{\Gamma((n+2-k)/2)}{\Gamma((n+2)/2)},\qquad
 \mathbb E S^{-n}=\frac{2^{-n/2}}{\Gamma(n/2+1)}.
\]
The elementary bound
\[
 \Gamma(x+1)=\int_0^\infty t^x e^{-t}\,dt
 \ge \int_x^{x+1} t^x e^{-t}\,dt
 \ge x^x e^{-(x+1)}\qquad(x>0)
\]
implies \(\mathbb E S^{-n}\le e(e/n)^{n/2}\).
The monotonicity of probability-space \(L^p\) norms, applied to \(S^{-1}\), therefore gives
\[
 \mathbb E S^{-k}\le\left(\frac{C_0}{\sqrt n}\right)^k,
 \qquad 1\le k\le n,\qquad C_0=e^{3/2}.
 \tag{T2}
\]

Expand the polynomial in (T1) before taking expectations.
All its coefficients are nonnegative, so (T2) yields
\[
 \begin{aligned}
 \mathbb P\{\operatorname{dist}(g,Z)\le\rho\}
 &\le4\sum_{k=1}^n\binom nk\bigl((2D+1)^k-1\bigr)
                   \left(\frac{C_0\rho}{\sqrt n}\right)^k\\
 &=4\left[\left(1+\frac{C_0(2D+1)\rho}{\sqrt n}\right)^n
             -\left(1+\frac{C_0\rho}{\sqrt n}\right)^n\right]\\
 &\le8C_0D\sqrt n\,\rho
       \exp\bigl(C_0(2D+1)\sqrt n\,\rho\bigr).
 \end{aligned}
 \tag{T3}
\]
There is no additive term independent of \(\rho\).
Bounding the binomial expression by an exponential before averaging over \(S\) would lose the finite negative-moment argument and is not used.

<a id="global-repair-growth"></a>
## Repair growth and empty compressed types

Let \(F_i:\mathbb R^{p_i}\to\mathbb R^{q_i}\) be one of the finitely many quadratic maps indexed by the compression dimensions in C_F0186_v2.
Its coefficients and dimensions are independent of \(N\).
The actual compressed coordinates obey
\[
 |F_i(x)|\le\varepsilon,\qquad |x|^2\le C_1(1+M^2)
 \tag{C1}
\]
when \(\max_j\|H_j\|\le M\), with fixed \(C_1\).

For each type with nonempty zero set, KSS gives
\[
 \operatorname{dist}(x,F_i^{-1}(0))
 \le C_i(1+|x|^2)|F_i(x)|^{a_i},
 \qquad a_i=\bigl(2\,9^{p_i-1}\bigr)^{-1}.
 \tag{C2}
\]
Using degree two is legitimate because the normalization coordinate is quadratic.
Let \(a>0\) be the minimum of these exponents; if there are no nonempty types, take any \(a>0\), for example one.
For \(0<\varepsilon\le1\), the existing Hermitian lift then gives
\[
 \left(\sum_j\|\Delta H_j\|_{\mathrm{HS}}^2\right)^{1/2}
 \le C(1+M^2)\varepsilon^a
 \tag{C3}
\]
for every realized nonempty type.
Here the constant \(C\) is independent of \(M,N,\varepsilon\).

For a type with \(F_i^{-1}(0)=\varnothing\), define the degree-at-most-three real polynomial map
\[
 G_i(x,y)=\bigl(yF_i(x),\ y(y-1)\bigr).
\]
Its zero set is exactly \(\mathbb R^{p_i}\times\{0\}\).
At \((x,1)\), the distance to this zero set is one and \(G_i(x,1)=(F_i(x),0)\).
Applying KSS to \(G_i\), whose zero set is nonempty, gives
\[
 |F_i(x)|\ge c_i(2+|x|^2)^{-E_i},\qquad E_i=3\,15^{p_i}.
 \tag{C4}
\]
If the actual degree is smaller than three, its degree is at least two because of \(y(y-1)\); the smaller KSS exponent still implies this displayed weaker bound since \(2+|x|^2\ge1\).
This avoids any convention for distance to an empty set.

Let \(E_*=\max_i E_i\) over the empty types, with \(E_*=1\) if there are none.
Choose
\[
 0<\theta\le\min\left(\frac a2,\frac1{2E_*}\right),\qquad
 b=a-\theta>0,
 \qquad M=M(\varepsilon)=\varepsilon^{-\theta/2}.
 \tag{C5}
\]
By (C1) and (C4), an empty type would satisfy
\[
 |F_i(x)|\ge c'_i\varepsilon^{\theta E_i}
            \ge c'_i\varepsilon^{1/2}>\varepsilon
\]
for every sufficiently small \(\varepsilon>0\), with one common threshold for all types.
Thus empty types are excluded on this moving norm event.
For nonempty types, (C3) becomes \(C\varepsilon^b\), since \(1+M^2\le2\varepsilon^{-\theta}\).
Consequently, for all sufficiently small \(\varepsilon\),
\[
 \{s_{\min}(L_N)\le\varepsilon,\ \max_j\|H_j\|\le M(\varepsilon)\}
 \subseteq
 \{\operatorname{dist}(g,Z_N)\le C\sqrt N\,\varepsilon^b\},
 \tag{C6}
\]
where \(g\) denotes standard real Gaussian GUE coordinates and \(Z_N\) is the singular-input set.
If \(Z_N\) is empty, the event on the left is empty by the construction itself.

<a id="norm-tail"></a>
## An elementary GUE norm bound

For a fixed complex unit vector \(v\), \(v^*H_j^{(N)}v\) is a real Gaussian of variance \(1/N\): it is the Hilbert--Schmidt coordinate in the direction \(vv^*\), whose Hilbert--Schmidt norm is one.
The Gaussian moment generating function and the exponential Markov inequality give
\[
 \mathbb P\{|v^*H_j^{(N)}v|>t\}\le2e^{-Nt^2/2}.
\]
A \(1/4\)-net of the unit sphere in \(\mathbb C^N\simeq\mathbb R^{2N}\) has cardinality at most \(9^{2N}\), by the disjoint-ball volume estimate for a maximal separated set.
For a Hermitian matrix \(H\), approximation of a maximizing unit vector by this net gives
\[
 \|H\|\le2\max_{v\text{ in the net}}|v^*Hv|.
\]
The union bound therefore gives
\[
 \mathbb P\{\max_{1\le j\le d}\|H_j^{(N)}\|>M\}
 \le2d\exp\left(N\left(2\log9-\frac{M^2}{8}\right)\right)
 \le2d e^{-NM^2/16}\qquad(M\ge9).
 \tag{N}
\]
In particular, the maximum norm has uniformly bounded moments of every fixed positive order, for all \(N\ge1\).

<a id="global-small-ball"></a>
## A global small-ball estimate

Assume \(u> -\infty\), so that for every sufficiently large \(N\),
\[
 q_N(g)=|\det L_N(N^{-1/2}g)|^2
\]
is a nonzero nonnegative polynomial of degree at most \(2mN\), by C_F0186_v2.
Choose the fixed small-\(\varepsilon\) threshold so that also \(M(\varepsilon)\ge9\).
Use (T3), (C6), \(n=dN^2\), and (N) to obtain
\[
 \mathbb P\{s_{\min}(L_N)\le\varepsilon\}
 \le C N^{5/2}\varepsilon^b
          \exp(CN^{5/2}\varepsilon^b)
       +2d\exp\left(-\frac N{16}\varepsilon^{-\theta}\right).
 \tag{S1}
\]
All constants, \(b,\theta>0\), and the threshold are independent of \(N\).
No irreducibility, covariance condition or invertibility of \(A_0\) is introduced.
The estimate also includes an empty singular-input set.

For \(N^{5/2}\varepsilon^b\le1\), the first exponential is bounded by a fixed constant.
The elementary bound \(e^{-\varepsilon^{-\theta}/16}\le C\varepsilon^b\), valid on the fixed small-\(\varepsilon\) interval, bounds the second term uniformly for \(N\ge1\).
Hence
\[
 \mathbb P\{s_{\min}(L_N)\le\varepsilon\}
 \le C N^{5/2}\varepsilon^b
 \quad\text{if }0<\varepsilon\le\varepsilon_0,\quad
 N^{5/2}\varepsilon^b\le1,\quad N\ge N_0.
 \tag{S2}
\]
Unlike the earlier norm-restricted bound, this tail can be integrated all the way to zero.

For example, if \(X_N=\log^-s_{\min}(L_N)\), then for any fixed \(K>5/(2b)\), all sufficiently large \(N\) and \(t\ge K\log N\),
\[
 \mathbb P\{X_N\ge t\}\le C N^{5/2}e^{-bt}.
 \tag{S3}
\]
Tail integration gives \(\mathbb E X_N^p=O((1+\log N)^p)\) for every fixed \(p>0\), after increasing \(N_0\) if necessary.
In particular, eventual exact nonsingularity is accompanied by integrability of the negative logarithm.
For any prescribed \(r>0\), choosing \(Bb>r+5/2\) also gives \(\mathbb P\{s_{\min}(L_N)\le N^{-B}\}=O(N^{-r})\).

<a id="mean-log-tail"></a>
## Expected negative logarithmic tails

Retain \(\beta>0\) and \(0<\gamma<2/(4+\beta)\) from the C_F0186_v2 mesoscopic estimate
\[
 \mathbb E\nu_N([0,t])\le Ct^\beta,
 \qquad N^{-\gamma}\le t\le1.
 \tag{W}
\]
Choose \(B\) with \(Bb>5/2\) and \(2B>\gamma\), and put \(a_N=N^{-2B}\), \(t_N=N^{-\gamma}\).
For \(0<t\le a_N\), (S2) and the fact that one singular value below \(\sqrt t\) is necessary for positive mass below \(t\) give
\[
 \mathbb E\nu_N([0,t])
 \le\mathbb P\{s_{\min}(L_N)\le\sqrt t\}
 \le C N^{5/2}t^{b/2}.
\]
Therefore
\[
 \int_0^{a_N}\mathbb E\nu_N([0,t])\,\frac{dt}{t}
 \le C N^{5/2-Bb}\longrightarrow0.
 \tag{E1}
\]
On the next interval, monotonicity and (W) give
\[
 \int_{a_N}^{t_N}\mathbb E\nu_N([0,t])\,\frac{dt}{t}
 \le C(2B\log N)N^{-\gamma\beta}\longrightarrow0.
 \tag{E2}
\]
For fixed \(0<\varepsilon<1\) and large \(N\), layer integration, (W), (E1) and (E2) yield
\[
 \begin{aligned}
 \mathbb E\int_{(0,\varepsilon)}|\log x|\,d\nu_N(x)
 &\le |\log\varepsilon|\mathbb E\nu_N([0,\varepsilon])
       +\int_0^\varepsilon\mathbb E\nu_N([0,t])\,\frac{dt}{t}\\
 &\le C\varepsilon^\beta(1+|\log\varepsilon|)
        +C(\log N)N^{-\gamma\beta}
        +C N^{5/2-Bb}.
 \end{aligned}
 \tag{E3}
\]
Tonelli applies to the nonnegative integrands, and the displayed finite bounds prove the required integrability rather than assuming it.
The absence of an exact zero atom holds almost surely for all \(N\ge N_0\) by the established rank argument.
Thus
\[
 \lim_{\varepsilon\downarrow0}\limsup_N
 \mathbb E\int_{(0,\varepsilon)}|\log x|\,d\nu_N(x)=0.
 \tag{EUI}
\]

<a id="l1-log-limit"></a>
## Finite logarithmic limits: \(L^1\) and expectation convergence

The deterministic coefficient norm bound gives
\[
 \|L_N\|\le C_A\left(1+\max_j\|H_j^{(N)}\|\right).
\]
The norm tail (N) implies uniformly integrable positive logarithmic spectral tails:
\[
 \lim_{R\to\infty}\sup_N
 \mathbb E\int_{(R,\infty)}\log x\,d\nu_N(x)=0.
 \tag{E4}
\]
Indeed the integral is bounded by \(2\log^+\|L_N\|\,1_{\{\|L_N\|>\sqrt R\}}\), and (N) integrates its expectation uniformly.
For fixed lower and upper cutoffs, weak convergence in probability of \(\nu_N\) gives convergence of the bounded continuous logarithmic truncation in \(L^1\), since those integrals are uniformly bounded.
Remove the two cutoffs using (EUI), (E4), and the corresponding limiting logarithmic integrability.
The triangle inequality proves
\[
 \mathbb E|U_N-u|\longrightarrow0,
 \qquad \mathbb E U_N\longrightarrow u,
 \qquad u> -\infty.
 \tag{L1}
\]
These expectations are finite for every sufficiently large \(N\); a finite collection of smaller sizes at which the determinant is identically zero does not affect the asserted limit.

<a id="minus-infinite-mean"></a>
## Minus-infinite limit: extended expectation convergence

For arbitrary coefficients, \(U_N^+\le\log^+\|L_N\|\), whose expectation is uniformly bounded by (N).
Thus \(\mathbb E U_N\) is a well-defined extended real number in \([-\infty,\infty)\), even when \(L_N\) is identically singular.
For a fixed \(\delta>0\), the regularized logarithm
\[
 U_{N,\delta}=\frac1{2mN}\log\det(L_N^*L_N+\delta^2I)
\]
has a fixed lower bound \(\log\delta\); its positive part is uniformly integrable by the same norm tail.
Its already established convergence in probability to \(u_\delta\) therefore holds in \(L^1\), so \(\mathbb E U_{N,\delta}\to u_\delta\).
Because \(U_N\le U_{N,\delta}\),
\[
 \limsup_N\mathbb E U_N\le u_\delta.
\]
If \(u=-\infty\), let \(\delta\downarrow0\) and use \(u_\delta\downarrow-\infty\).
This gives \(\mathbb E U_N\to-\infty\) in the extended-real sense.
No \(L^1\) distance to minus infinity is asserted.

## Root determinant moments

The normalized nonnegative determinant \(D_N=|\det L_N|^{1/(mN)}\) satisfies \(D_N\le\|L_N\|\).
The norm tail gives uniformly bounded moments of every order, so the probability convergence already established in v2 also implies \(D_N\to e^u\) in every fixed finite \(L^p\), including the zero-limit case.
This consequence concerns the nonnegative root determinant and supplies no complex phase statement.


<a id="global-lipschitz"></a>
## Global affine Lipschitz estimates

Write the tuple as \(H=N^{-1/2}g\) in real Hilbert--Schmidt orthonormal coordinates, with \(g\) standard Gaussian.
Set \(\kappa_A=(\sum_j\|A_j\|_{\rm HS}^2)^{1/2}\).
The tensor Hilbert--Schmidt identity and Cauchy--Schwarz give
\[
 \|L_N(g)-L_N(g')\|_{\rm HS}
 \le\kappa_A N^{-1/2}\|g-g'\|_2.
\]
For a globally Lipschitz function \(f:[0,\infty)\to\mathbb R\), put
\[
 \Phi_{N,f}(g)=\frac1{mN}\sum_i f(s_i(L_N(g))).
\]
By (SV) and Cauchy--Schwarz for the normalized sum,
\[
 \operatorname{Lip}(\Phi_{N,f})
 \le \frac{\kappa_A}{\sqrt m}\frac{\operatorname{Lip}(f)}N.
 \tag{Lip}
\]
The case \(\kappa_A=0\) is deterministic.
Otherwise Gaussian concentration gives
\[
 \mathbb P\{|\Phi_{N,f}-\mathbb E\Phi_{N,f}|>a\}
 \le2\exp\left[-\frac{c_A N^2a^2}{\operatorname{Lip}(f)^2}\right].
 \tag{GC}
\]
No operator-norm event enters (Lip) or (GC).

<a id="zero-affine-limit"></a>
## Minus-infinite affine limit

For fixed \(\delta>0\), take \(f_\delta(s)=\tfrac12\log(s^2+\delta^2)\), whose Lipschitz constant is \(1/(2\delta)\).
For every fixed \(a>0\), (GC) is summable over \(N\).
Taking \(a=1/k\), \(k\ge1\), proves
\[
 U_{N,\delta}-\mathbb EU_{N,\delta}\longrightarrow0
 \quad\hbox{almost surely},\qquad
 U_{N,\delta}=\frac1{2mN}\log\det(L_N^*L_N+\delta^2I).
\]
Fixed-regularizer weak spectral convergence from v2 and (N) imply convergence in \(L^1\) to
\[
 u_\delta=\tfrac12\tau_m\log(L^*L+\delta^2I).
\]
Indeed, the negative part is bounded by a constant depending on \(\delta\), and the positive part is bounded by
\(C_\delta+\log(1+\max_j\|H_j^{(N)}\|)\), whose squares have uniformly bounded means.
Thus \(U_{N,\delta}\to u_\delta\) almost surely.

Intersect these events over a sequence \(\delta_k\downarrow0\).
Since \(U_N\le U_{N,\delta_k}\) and \(u_{\delta_k}\downarrow u\),
\[
 \limsup_N U_N\le u\quad\hbox{almost surely}.
\]
When \(u=-\infty\), this is precisely (AS).
This branch needs no minimum-singular-value estimate.

<a id="summable-floor"></a>
## Summable floor for a finite limit

Assume \(u>-\infty\) and fix \(M\ge9\), using the elementary norm bound (N).
At \(\varepsilon=N^{-B}\), v2 estimate (A) gives a tube contribution
\(O(N^{5/2-B\alpha})+e^{-cN^2}\) once \(B\alpha>5/2\).
Choose \(B\alpha>7/2\).
Adding the summable norm-cutoff failure gives
\[
 \sum_N\mathbb P\{s_{\min}(L_N)<N^{-B}\}<\infty.
 \tag{SF}
\]
The finitely many sizes before v2's generic-rank threshold do not matter.
Hence almost surely all sufficiently large \(N\) have every squared singular value at least \(N^{-2B}\).

<a id="summable-small-mass"></a>
## Concentrated mass at a moving cutoff

Let \(\nu_N\) be the normalized spectral law of \(L_N^*L_N\), and \(\nu\) its free limit.
Use the exponent \(0<\beta\le1\) and resolvent comparison of [v2](../claims/Yin_C_F0186_v2.md#logarithmic-tail).
Fix
\[
 0<\gamma<\frac2{4+\beta},\qquad t_N=N^{-\gamma}.
\]
Define
\[
 c_t(s)=\frac{t^2}{s^4+t^2},\qquad
 C_N(t)=\frac1{mN}\sum_i c_t(s_i(L_N)).
\]
Substitution \(s=\sqrt t\,y\) in the derivative gives \(\|c_t'\|_\infty\le4t^{-1/2}\).
Moreover,
\[
 \nu_N([0,t])\le2C_N(t),\qquad
 \mathbb EC_N(t)=t\,|\Im\mathbb EG_{L_N^*L_N}(it)|.
\]
The same resolvent argument as v2 gives \(\mathbb EC_N(t_N)\le C N^{-\gamma\beta}\).
Using (GC) with \(a=N^{-\gamma\beta}\),
\[
 \mathbb P\{|C_N(t_N)-\mathbb EC_N(t_N)|>N^{-\gamma\beta}\}
 \le2\exp[-cN^{2-\gamma(1+2\beta)}].
 \tag{CM}
\]
Its exponent is positive, since \(\gamma(4+\beta)<2\) and \(1+2\beta<4+\beta\).
Borel--Cantelli therefore implies
\[
 \nu_N([0,t_N])\le C'N^{-\gamma\beta}
 \quad\hbox{eventually almost surely}.
 \tag{Mass-AS}
\]

<a id="clipped-log"></a>
## Moving clipped logarithms

Set
\[
 h_t(s)=\log\max(s,\sqrt t),\qquad
 V_N(t)=\frac1{mN}\sum_i h_t(s_i(L_N))
       =\frac12\int\log\max(x,t)\,d\nu_N(x).
\]
The function \(h_t\) is globally \(t^{-1/2}\)-Lipschitz.
For each fixed \(a>0\), (GC) at \(t_N\) is summable with bound \(2\exp[-cN^{2-\gamma}a^2]\).
Taking \(a=1/k\) gives
\[
 V_N(t_N)-\mathbb EV_N(t_N)\longrightarrow0
 \quad\hbox{almost surely}.
 \tag{Clip-conc}
\]

For fixed \(0<\varepsilon<1\), weak spectral convergence and uniform norm moments give
\[
 \mathbb EV_N(\varepsilon)\longrightarrow
 v(\varepsilon)=\frac12\int\log\max(x,\varepsilon)\,d\nu(x).
\]
For \(t_N<\varepsilon\), layer integration gives
\[
 V_N(\varepsilon)-V_N(t_N)
 =\frac12\int_{t_N}^{\varepsilon}\nu_N([0,t))\,\frac{dt}{t}.
\]
The v2 bound \(\mathbb E\nu_N([0,t])\le Ct^\beta\) on \(t_N\le t\le1\) implies
\[
 0\le\mathbb EV_N(\varepsilon)-\mathbb EV_N(t_N)
 \le C'\varepsilon^\beta.
\]
Since \(v(\varepsilon)\downarrow u\), first let \(N\to\infty\), then \(\varepsilon\downarrow0\), to obtain
\[
 \mathbb EV_N(t_N)\longrightarrow u.
 \tag{Clip-mean}
\]
This step never integrates the unregularized logarithm on an exceptional event.

Increase \(B\) in (SF) if needed so \(B>\gamma/2\).
On the eventual floor,
\[
 0\le V_N(t_N)-U_N\le B(\log N)\nu_N([0,t_N]).
\]
By (Mass-AS), the right side tends to zero almost surely.
Together with (Clip-conc) and (Clip-mean), this proves (AS) for finite \(u\).

<a id="linearization-transfer"></a>
## Transfer to scalar polynomial potentials

Fix a nonconstant scalar polynomial \(P\), and use the exact word-chain linearization \(L_P(z;x)\) of fixed size \(q\) in [v1](../claims/Yin_C_F0186_v1.md#polynomial-application).
Its auxiliary block \(Q\) is unit upper triangular with polynomial inverse, and its Schur complement is \(P(x)-z\).
For every finite tuple,
\[
 \det L_P(z;H^{(N)})=\det(P(H^{(N)})-zI_N).
 \tag{Lin-det}
\]
For each fixed \(z\ne P(0)\), the v1 pointwise potential proof already gives convergence in probability to the finite value
\(u_P(z)=\tau\log|P(s)-z|\).
The affine probability theorem in v2 and (Lin-det) identify the free affine logarithm by uniqueness of probability limits:
\[
 q\,\tau_q\log|L_P(z;s)|=u_P(z).
 \tag{Free-id}
\]
In particular the affine free logarithm is finite.
This uses an established probability theorem, not the desired almost-sure strengthening.
Applying (AS) to this fixed affine pencil now proves
\[
 u_N(z):=\frac1N\log|\det(P(H^{(N)})-zI_N)|
 \longrightarrow u_P(z)
 \quad\hbox{almost surely for each fixed }z\ne P(0).
 \tag{Point-AS}
\]
No uniformity or measurable selection of exponents in \(z\) is needed.

The free identity also has a direct bounded-operator proof.
Use bounded multiplicativity and normalization from [FK52-U001](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation) and [MS24-U001](../audits/literature/MS24/Yin_U001.md#determinant-convention).
The exact factorization is
\[
 \begin{pmatrix}a&B\\C&Q\end{pmatrix}
 =\begin{pmatrix}I&BQ^{-1}\\0&I\end{pmatrix}
  \begin{pmatrix}P-z&0\\0&Q\end{pmatrix}
  \begin{pmatrix}I&0\\Q^{-1}C&I\end{pmatrix}.
\]
Each unit triangular factor has determinant one: conjugate by scalar diagonal matrices so its strict triangular entries tend to zero in norm, use multiplicativity to preserve its determinant under similarity, then continuity near the identity.
The same argument handles \(Q\).
Direct-sum trace weights give
\(\Delta_{\tau_q}(L_P(z;s))=\Delta_\tau(P(s)-z)^{1/q}\), including a zero determinant.
For \(q=1\) there is no auxiliary block.
This is an alternative justification, not an extra premise needed by the probability-limit route.

<a id="brown-as"></a>
## One event and planar convergence

The maps \((\omega,z)\mapsto u_N(\omega,z)\) are jointly measurable logarithms of determinant polynomials, with \(\log0=-\infty\), and \(u_P\) is measurable.
Thus the set of pairs where (Point-AS) fails is measurable.
For Lebesgue-almost every \(z\), its probability section has measure zero.
Fubini on each compact disk, then a countable union of disks, supplies an event \(\Omega_1\) of probability one on which \(u_N(\omega,z)\to u_P(z)\) for Lebesgue-almost every \(z\) in the plane.
There is no intersection of uncountably many probability-one events.

By (N) and Borel--Cantelli, another event \(\Omega_2\) of probability one has all input norms eventually bounded by one fixed deterministic constant.
Consequently the spectra of \(P(H^{(N)})\) are eventually in a fixed deterministic disk of radius \(M_P\).
Choose \(M_P>\|P(s)\|\) as well.
Translated logarithmic kernels have uniformly bounded \(L^2(K)\) norms for translations in that disk and any fixed compact planar \(K\).
The finite eigenvalue formula and Jensen give
\[
 \|u_N\|_{L^2(K)}\le C_{K,M_P}
 \quad\hbox{eventually on }\Omega_2.
\]
The Brown-potential identity gives the same bound for \(u_P\).

Fix \(\omega\in\Omega_1\cap\Omega_2\).
For every \(\delta>0\), dominated convergence of indicators gives
\[
 |\{z\in K:|u_N(z)-u_P(z)|>\delta\}|\longrightarrow0.
\]
Cauchy--Schwarz then gives
\[
 \|u_N-u_P\|_{L^1(K)}
 \le\delta|K|+2C_{K,M_P}
       |\{z\in K:|u_N(z)-u_P(z)|>\delta\}|^{1/2}.
\]
Let \(N\to\infty\), then \(\delta\downarrow0\).
Using integer-radius disks yields local \(L^1\) convergence on this same event.
The distributional logarithmic-potential identity therefore gives convergence against every compactly supported smooth test function on the event.
The eventual common compact spectral support and positivity extend this pathwise to every bounded continuous test function.
No further uncountable intersection over test functions is needed because the local \(L^1\) conclusion already holds on the event.
Constant \(P\) gives the same point mass at every size.
This proves the exact reactivated F0012 assertion under the stated accepted inputs.



## Current assessment
[Selected decision](#decision-strong-reviewed)

## Assessment history

### Decision strong-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-04T18:40 |
| status | open |
| reason | Complete strengthened arguments are retained for independent review, including global integrable small-singular-value tails, almost-sure affine logarithms, mean convergence and the exact reactivated Brown-measure contract. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Strengthened conclusions](#statement) | Almost-sure and mean affine logarithmic convergence, root determinant moments, the global small-ball bound and almost-sure scalar Brown-measure convergence for arbitrary cross-size couplings. |

### Decision strong-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-04T18:49 |
| status | proved |
| reason | The independent whole-proof finding checks every strengthened affine conclusion and the exact almost-sure Brown-measure contract; a separate independent key-step finding checks the global integrable tail and mean branch. All local interfaces are closed within the stated accepted external-theorem boundary. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact strengthened conclusions](#statement) | Almost-sure affine logarithms, finite-limit L1 and mean convergence, minus-infinite extended means, root determinant moments, the global small-ball bound and almost-sure scalar Brown-measure convergence under arbitrary cross-size couplings. |
| argument | [Complete strengthened argument](#argument) | All geometric, concentration, expectation and planar limit arguments, including their boundary cases and normalizations. |
| dependency | [Affine probability theorem](Yin_C_F0186_v2.md#statement) | Fixed-coefficient probability limits and the norm-restricted polynomial floor used before the stronger conclusions. |
| dependency | [Affine proof interfaces](Yin_C_F0186_v2.md#argument) | Eventual generic invertibility, fixed compressed maps, weak singular-spectral convergence, regularization and mesoscopic counting. |
| dependency | [Real polynomial error bound](Yin_C_F0186_v1.md#error-bound) | The accepted global KSS inequality and its Hermitian repair interface, with growth and empty-type adaptations proved here. |
| dependency | [Uniform-ball geometric input](Yin_C_F0186_v1.md#tubes) | Exact Lotz specialization, regular-level extension and Gaussian mixture identity; the no-additive-error integration is proved here. |
| dependency | [Scalar polynomial probability application](Yin_C_F0186_v1.md#polynomial-application) | Exact word-chain linearization, finite fixed-shift logarithmic probability limit and Brown-potential convention used in the acyclic almost-sure transfer. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0190_v3.md#independent-strong-proof) | The entire exact statement and argument, selected prior interfaces, and original strengthened Task contract. |
| review | [Independent integrable-tail finding](../audits/reviews/Yin_R_F0188_v2.md#integrable-tail-and-mean) | Additional key-step review of the global small-ball bound, finite and minus-infinite means, and root determinant moments; does not supply the almost-sure Brown verdict. |

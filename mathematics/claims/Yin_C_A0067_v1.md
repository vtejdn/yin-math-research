---
author: Yin
---

# Recovering the spatial kernel tail from signed first-return means

## Statement

Let \(A\) be a finite rectangular matrix over \(\mathbb CG\), where \(G\) is finitely generated, and write \(m\) for its number of columns.
Put \(H=I-A^*A/M\) for \(M>0\) with \(M\ge\|A\|^2\), so \(0\le H\le I\).
Write \(p=1_{\{1\}}(H)\) and fix an integer \(w\ge1\) bounding the word lengths of the coefficients of \(H\).
For a group element \(g\ne e\) and coordinates \(i,j\), let \(x=\delta_g e_i\), \(y=\delta_e e_j\), so \(x^*p y=\widehat p(g)_{ij}\).
For \(\zeta=1,i_{\mathbb C}\), where \(i_{\mathbb C}^2=-1\), and each sign take the unit vector \(\xi_\pm=(x\pm\zeta y)/\sqrt2\).
Form two real sequences from the original product moments by
\[
 h_n^\pm=\frac{1+\xi_\pm^*H^n\xi_\pm}{2},\qquad
 f_n^\pm=h_n^\pm-\sum_{l=1}^{n-1}f_l^\pm h_{n-l}^\pm\quad(n\ge1),
 \qquad h_0^\pm=1.                                                \tag{1}
\]
The constant term in the numerator adds a known stationary state of weight one half.
Each \(f_n^\pm\) is obtained from finitely many true product fibers of \(A^*A\), including the matrix indices and phases at both endpoints.
For each sign \(f_n^\pm\ge0\), \(\sum_{n\ge1}f_n^\pm=1\), and the first mean \(m_\pm=\sum_{n\ge1}n f_n^\pm\) lies between one and two.
In particular the signed difference
\[
     d_\zeta(i,j,g)=\sum_{n\ge\lceil |g|/w\rceil} n(f_n^- - f_n^+)          \tag{2}
\]
converges absolutely at each endpoint.
The omitted early differences are zero.
One has the exact identity
\[
       \operatorname{Re}(\zeta\widehat p(g)_{ij})=
                         \frac{d_\zeta(i,j,g)}{m_+m_-}.                  \tag{3}
\]
It follows for any nonnegative weight \(W\) on \(G\) and any radius \(R\ge1\) that
\[
 \sum_{|g|\ge R}W(g)\|\widehat p(g)\|_{\rm HS}^2
 \ \le\ \sum_{|g|\ge R}W(g)\sum_{i,j,\zeta}|d_\zeta(i,j,g)|^2
 \ \le\ 16\sum_{|g|\ge R}W(g)\|\widehat p(g)\|_{\rm HS}^2 .            \tag{4}
\]
In particular an upper bound for the signed excursion means bounds the whole exterior of a ball on one fixed group.
No hypothesis on the trace of \(p\), a spectral gap, or a second matrix with the same kernel enters (1)–(4).
Taking \(W(g)=(1+|g|)^\beta\) with \(\beta>3\), convergence of the middle sum at \(R=1\) gives integral kernel dimension on an individual good four-line group. [Spatial trace criterion](../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace)
This uses first-return means for individual pairs of probes and keeps the signs inside the sum over time.
The [schedule criterion](Yin_C_A0062_v1.md#statement) instead bounds errors in approximating the full projection by ordinary powers.

On a fixed good four-line group, for \(\beta>3\), either of the following stronger requirements is equivalent to closed range of \(A\):

1. Along some real sequence \(z\uparrow1\) the weighted spatial square sum at \(R=1\) of the Abel contrasts \((f^+(z)-f^-(z))/(1-z)\) stays bounded, where \(f^\pm(z)=\sum_{n\ge1}f_n^\pm z^n\).
2. The spatial square sum with the same weight is finite after replacing each \(|d_\zeta|\) by \(\sum_n n|f_n^--f_n^+|\).

## Argument

For a given \(\xi\) among the four probes, apply \(K=H\oplus1\) to the Hilbert space extended by one scalar coordinate, and take \(\eta=(\xi,1)/\sqrt2\).
Then \(h_n=\eta^*K^n\eta\).
The scalar spectral measure at \(\eta\) has mass
\[
             a=\frac{1+\xi^*p\xi}{2}\in[1/2,1]
\]
at one, including when \(A\) is injective.
Let \(Q=I-\eta\eta^*\), \(b=QK\eta\), and \(C=QKQ\) on \(Q\mathcal H\).
Splitting a product at its first return to the probe, or taking the Schur complement in \(I-zK\), gives for \(0\le z<1\)
\[
 h(z)=\sum_{n\ge0}h_nz^n=\frac{1}{1-f(z)},\qquad
 f(z)=z\eta^*K\eta+z^2 b^*(I-zC)^{-1}b.                              \tag{5}
\]
This is the rank-one instance of the operator renewal identity, with the first-return generating series starting at power one. [Grünbaum–Velázquez, Theorem 2.5, equation (26)](../literature/pdf/GV17--arxiv-v2.pdf#page=18)
Multiplication of the scalar power series gives the recursion (1).
Since \(C\) is a positive contraction, its coefficients \(b^* C^{n-2}b\) are nonnegative for \(n\ge2\), and \(f_1=\eta^*K\eta\ge0\).
This positivity concerns the completed sums even if individual group words have complex coefficients.
The probe has two spatial endpoints and an auxiliary coordinate.
Its returns refer to the rank-one projection onto \(\eta\).

By the spectral theorem \((1-z)h(z)\to a\) as \(z\uparrow1\).
Since \(a>0\), (5) and monotone convergence give \(\sum f_n=1\).
Also
\[
 \sum_{n\ge1} f_n(1+z+\cdots+z^{n-1})
       =\frac{1-f(z)}{1-z}=\frac1{(1-z)h(z)} .
\]
Monotone convergence gives \(\sum n f_n=1/a\).
The two signs have \(a_+-a_-=\operatorname{Re}(\zeta x^*p y)\).
If \(nw<|g|\), then \(x^*H^n y=0\), so \(h_n^+=h_n^-\) and recursively \(f_n^+=f_n^-\) through this degree.
Thus (2) equals \(m_- -m_+\), and taking reciprocals gives (3).
For each phase the product \(m_+m_-\) is in \([1,4]\).
Squaring (3) for both phases recovers the squared modulus between the two stated bounds, independently of the endpoint, coordinates and group.
Summing nonnegative quantities proves (4), including infinite values.
All finite prefixes in (1) use the original signed powers, since \(\xi^*H^n\xi\) is the explicit combination of the two diagonal and two off-diagonal entries at the selected sites.
Estimating the full signed time sums in (2) still requires a tail bound or an exact cancellation argument for the chosen matrix.

The recursions also give finite one-sided estimates.
For any of the probes put
\[
 L_N=\sum_{k=0}^{N}\left(1-\sum_{n=1}^k f_n\right).
\]
Counting the contributions of each \(f_n\) gives \(1\le L_N\uparrow m_\pm\le2\).
In particular the original complex coefficient at a specified endpoint satisfies
\[
        \tfrac12-(L_N^-)^{-1}\ \le\
        \operatorname{Re}(\zeta\widehat p(g)_{ij})\ \le\
        (L_N^+)^{-1}-\tfrac12 .
\]
These finite intervals bound a single component of the coefficient.
At an endpoint with a nonzero original atom for a probe, replacing its reciprocal mean by the universal lower bound \(1/2\) can leave slack even in the limit.

## Two stronger tests characterize closed range

For real \(0<z<1\) set \(R_z=(1-z)(I-zH)^{-1}\) and \(a_\pm(z)=(1-z)h^\pm(z)\).
The stationary half of each probe gives \(1/2\le a_\pm(z)\le1\).
Equation (5) yields the exact relation
\[
 \frac{f^+(z)-f^-(z)}{1-z}
 =\frac{a_+(z)-a_-(z)}{a_+(z)a_-(z)}
 =\frac{\operatorname{Re}(\zeta x^*R_z y)}{a_+(z)a_-(z)} .
\]
Thus the squared spatial norm of the Abel contrasts, summing both phases and all matrix entries outside the identity, is comparable within factors one and sixteen to the corresponding squared norm of \(R_z\).
Its identity coefficient is uniformly bounded since \(R_z\) is a positive contraction.
Moreover \(R_z\to p\) in trace \(L^2\) by spectral convergence.
If the weighted square norms stay bounded along a sequence, the rapid-decay shell estimate in [C57](Yin_C_A0057_v1.md#interchanging-the-scales-forces-a-spectral-gap) uniformly bounds the norm of its Fourier tails outside radius \(2^J\) by a constant times \(2^{-(\beta-3)J/2}\).
This estimate applies to infinite Fourier series with finite weighted norm by truncation and trace \(L^2\) identification.
Inside a fixed ball all coefficients converge, so this sequence converges to \(p\) in operator norm.
If \(A\) has nonclosed range, positive spectral values of \(A^*A\) approach zero, and \(\|R_z-p\|=1\) for every \(0<z<1\).
This proves the necessity of closed range for requirement 1.
Because the two first-return sequences each sum to one, \(|1-z^n|\le n(1-z)\) shows that requirement 2 implies requirement 1.

Conversely suppose the spectrum of \(H\) away from one lies in \([0,\theta]\) for some \(\theta<1\), as holds in the closed-range case.
Then \(\|H^k-p\|\le\theta^k\), and propagation bounds \(\sum_{|g|>kw}\|\widehat p(g)\|_{\rm HS}^2\le m\theta^{2k}\).
On the radius-\(kw\) ball use the trace \(L^2\) error bound \(\sqrt m\,\theta^k\) times the maximum square-root weight.
Outside the ball sum the displayed tail inequality on consecutive shells of width \(w\).
Together these bounds give \(\|H^k-p\|_{\ell^2_\beta}\le C\theta_1^k\) for any fixed \(\theta<\theta_1<1\), where the squared coefficient norm uses weight \((1+|g|)^\beta\).
They also give \(p\in\ell^2_\beta\).
Consequently \(R_z=p+(1-z)\sum_{k\ge0}z^k(H^k-p)\) extends analytically as a weighted coefficient array to \(|z|<1/\theta_1\).

For complex \(z\) in this disk the numerator \(a_+(z)-a_-(z)\) uses the polarized expression \((\zeta x^*R_z y+\bar\zeta y^*R_z x)/2\).
Its weighted coefficient norm is bounded on every smaller closed disk since swapping the endpoints inverts \(g\) and exchanges the matrix indices.
The denominators stay uniformly separated from zero on some disk of radius \(r>1\), independent of the probes.
Indeed their spectral representation is \(a_\pm(z)=a_\pm+\int_{[0,\theta]}(1-z)/(1-zt)\,d\nu_\pm(t)\), where \(a_\pm\ge1/2\) and the positive remainder has mass at most one.
For \(|z|\le1\) the real part of \((1-z)/(1-zt)\) is nonnegative, since \(1-(1+t)\operatorname{Re}z+t|z|^2\ge(1-|z|)(1-t|z|)\).
On a slightly larger disk its derivative is uniformly bounded for \(0\le t\le\theta\), so shrinking the enlargement ensures \(|a_\pm(z)|\ge1/4\).
Choose \(r<1/\theta_1\) inside that enlargement.
The identity \(f^+(z)-f^-(z)=(1-z)(a_+(z)-a_-(z))/(a_+(z)a_-(z))\) now gives a continuation uniformly bounded in the spatial weighted square norm on \(|z|=r\).
Cauchy's coefficient formula and the triangle inequality in that norm give \(\|f_n^+-f_n^-\|_{\ell^2_\beta}\le C' r^{-n}\), jointly over endpoints, indices and phases.
Summing with the weight \(n\) proves requirement 2.
This direction needs only finite propagation and the gap.

## Time cancellation on a gapless cyclic direction of a four-line group

In a fixed realization of the [four-line free-subalphabet event](Yin_C_A0059_v1.md#statement), take one covered rose generator \(u\).
It has infinite order and \(|u^r|\ge c r\) in the ambient group for all integers \(r\ge1\), with some \(c>0\).
Take \(A=1-u\) and \(M=4\), for which \(H=(2+u+u^{-1})/4\).
The cyclic shift on each right coset has no invariant vector and has approximate invariant unit vectors, so \(A\) is injective with nonclosed range.
We calculate the signed return contrast directly for the real probes at endpoints \(e,u^r\).

For \(0<z<1\) put \(s=\sqrt{1-z}\), \(b_z=(1-s)/(1+s)\).
The kernel at \(u^r\) of \((I-zH)^{-1}\) is \(s^{-1}b_z^{|r|}\) on the cyclic subgroup.
Indeed the sequence decays at both ends, solves \((1-z/2)G_r=(z/4)(G_{r-1}+G_{r+1})\) off zero and satisfies \((1-z/2)G_0-(z/2)G_1=1\).
Thus the two *unpadded* real probe Green functions are \((1\pm b_z^r)/s\).
Adding the stationary coordinate as in (1) gives
\[
     h^\pm(z)=\frac{1+s(1\pm b_z^r)}{2s^2},\qquad
     f^+(z)-f^-(z)=
       \frac{4s^3 b_z^r}{(1+s)^2-s^2b_z^{2r}} .                       \tag{6}
\]
For each \(r\), the reciprocal means are both \(1/2\) by these formulas, so the signed difference (2) is exactly zero.
For the imaginary phase the real walk has equal probe moments for both signs.

Taking absolute values of the differences *before* summing over time gives a different result.
Since the two first-return sequences each sum to one,
\[
 \sum_{n\ge1}n|f_n^+-f_n^-|\ \ge\
  \frac{|f^+(z)-f^-(z)|}{1-z},
\]
by \(|1-z^n|\le n(1-z)\).
Choosing \(s=1/r\) for large \(r\) in (6), the factor \(b_z^r\) tends to \(e^{-2}\).
The right side is at least a fixed positive multiple of \(1/r\).
Consequently the quadratic spatial test with these timewise absolute values diverges for every polynomial weight exponent \(\beta\ge1\), already on the endpoints \(u^r\) of this fixed group.

There is a parallel failure at a common finite Abel parameter.
For all \(r\) between \(1/s\) and \(2/s\), \(b_z^r\) is bounded below uniformly as \(s\downarrow0\).
The contrast in (6) divided by \(1-z\) is thus at least a constant times \(s\) on order \(s^{-1}\) endpoints of ambient length at least \(c/s\).
Its squared spatial norm of exponent \(\beta>1\) diverges at least as a positive multiple of \(s^{1-\beta}\), although its limit at every endpoint is zero.
This distinguishes the signed first means in (4) from both stronger replacements on an actual four-line group.

The same failure occurs when the true kernel has positive dimension and both probes detect it.
Choose another covered generator \(v\) and take the row \(A=(1-u)T\), \(T=(1,-v)\), with \(M=8\).
The coisometry \(S=T/\sqrt2\) gives \(p=I-S^*S\) and \(H^n=p+S^* H_0^n S\), where \(H_0=(2+u+u^{-1})/4\); the row has nonclosed range and kernel dimension one.
On its first coordinate \((H^n)_{11}=(I+H_0^n)/2\).
At the same distinct endpoints \(e,u^r\) both original real probes therefore put mass \(1/2\) on the kernel, or mass \(3/4\) at one after the auxiliary coordinate is included.
Their first means are \(4/3\).
The corresponding generating functions are \(h^\pm(z)=[3+s(1\pm b_z^r)]/(4s^2)\), giving \(f^+(z)-f^-(z)=8s^3 b_z^r/[(3+s)^2-s^2b_z^{2r}]\).
The preceding lower bounds still apply, although the exact signed diagonal contrast vanishes away from the identity.
The off-diagonal projection entry is \(p_{12}=v/2\), so the projection itself also has a nonzero coefficient at a nonidentity endpoint.

## Assessment history

### Decision signed-first-return-means

| Field | Value |
| --- | --- |
| date | 2026-11-17T11:33 |
| status | proved |
| reason | Independent review verified the exact recovery of complex coefficients, the exterior estimates, both closed-range equivalences and both fixed-group examples. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Signed endpoint means for arbitrary inputs and the two stronger conditions on a good four-line group. |
| argument | [Proof](#argument) | Padded probes, first means, uniform Abel bounds, coefficient signs and the explicit nonclosed-range inputs. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0103_v1.md#whole-argument-finding) | Independent review of the statement and argument under the specified order of summation. |

## Current assessment

[Selected decision](#decision-signed-first-return-means)

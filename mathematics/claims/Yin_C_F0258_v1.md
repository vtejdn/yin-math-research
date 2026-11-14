---
author: Yin
---

# Overlapping projection tests and the uniform singular concentration of omitted shifts

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(Z=X_i\) be a coordinate of a bounded normal generating tuple with [actual starred conjugate variables](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) in a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace.
Write \(N=W^*(X_j:j\ne i)\) and \(c=c_i(X)\) for the optimal [original right column constant](Yin_C_F0208_v1.md#statement).
For \(r>0\) define the nondecreasing concentration function
\[
             F(r)=\sup_{b\in N}\tau(1_{[0,r]}(|Z-b|)).
\]
The shifts may be nonnormal and may vary with \(r\).
If \(c<\infty\), then
\[
              \int_0^\infty F(r)^3\,\frac{dr}{r^3}\le24c^2,
              \qquad \lim_{r\downarrow0}\frac{F(r)^3}{r^2}=0.       \tag{1}
\]
There is also a simultaneous estimate for arbitrary finite families of nonzero projections \(e_j\in M\), shifts \(b_j\in N\), and radii \(r_j>0\) with \(\|(Z-b_j)e_j\|_2\le r_j\sqrt{t_j}\), where \(t_j=\tau(e_j)\).
For all real coefficients \(\alpha_j\ge0\),
\[
       \sum_j\alpha_j\frac{t_j^2}{r_j}
                 \le \frac{64}{9} c\left\|\sum_j\alpha_j e_j\right\|_2 .  \tag{2}
\]
The constant \(64/9\) improves to \(2\) for exact right spectral cutoffs \(e_j=1_{[0,r_j]}(|Z-b_j|)\).
In particular, for a sequence with \(t_{j+1}\le\theta t_j\), \(0<\theta<1\), one has
\[
      \sum_j\frac{t_j^3}{r_j^2}
           \le (64c/9)^2\frac{1+\sqrt\theta}{1-\sqrt\theta}.           \tag{3}
\]
These bounds permit overlapping and noncommuting projections.
Divergence in (1), or failure of a finite uniform constant in (2) for one fixed actual normal tuple, excludes a bare full-domain dual system on its [two-free-Haar enlargement](Yin_C_F0208_v1.md#statement).
For scalar shifts alone all three estimates hold unconditionally under the actual vacuum hypothesis, with \(c\) on the right replaced by \(12\|\xi_\mu\|_2\), where \(\xi_\mu\) is the distinguished marginal vacuum.
This last assertion still permits arbitrary ambient projections in (2) and (3).

## Argument

### A simultaneous estimate with the square root of the optimal density

Assume \(c<\infty\).
The [weighted commutator theorem](Yin_C_F0211_v1.md#statement) gives a positive faithful density \(d\) with \(\tau(d)=1,\ d^{-1}\in L^1(M)\), and a bounded operator \(T\) of norm \(c\) on \(L^2(M)\).
For every \(V=Z-b,\ b\in N\), it satisfies \([T,L_V]=|1\rangle\langle d^{-1/2}|\), where \(L_V\) denotes left multiplication.
Put \(h=\sqrt d\), so \(\|h\|_2=1\).
For a nonzero projection \(p\) of trace \(s\) write \(\langle u\rangle_p=\tau(pu)/s\) for positive integrable \(u\).
The trace weighted by \(p/s\), restricted to the spectral algebra of \(h\), is a probability measure.
Jensen's inequality gives \(\langle h\rangle_p\ge \langle d^{-1}\rangle_p^{-1/2}\).

For \(p=1_{[0,r]}(|V|)\) and \(q=1_{[0,r]}(|V^*|)\), polar decomposition gives \(\tau(p)=\tau(q)=s\).
Compressing the commutator by \(L_q,L_p\) gives
\[
       s\sqrt{\langle d^{-1}\rangle_p}
          =\sqrt{s}\,\|p d^{-1/2}\|_2\le 2cr.
\]
Indeed \(\|qV\|,\|Vp\|\le r\).
Thus \(s^2/r\le2c\,\tau(hp)\), also when \(s=0\).

Now take one arbitrary approximate test \(e,b,r\) of trace \(t\) as in (2).
In \(eMe\) the spectral projection \(p=1_{[0,4r^2]}(eV^*Ve)\) has trace \(s\ge3t/4\) by Markov's inequality and satisfies \(\|Vp\|\le2r\).
For each \(\varepsilon>0\) the right cutoff \(q'=1_{[0,2r+\varepsilon]}(|V|)\) has trace at least \(s\).
Indeed, if \(\tau(q')<s\), the map \(q'p\) has source support of trace at most \(\tau(q')\) by polar decomposition, leaving a nonzero vector in \(pL^2(M)\cap(1-q')L^2(M)\), contrary to the bound on \(Vp\).
Its left counterpart \(q=1_{[0,2r+\varepsilon]}(|V^*|)\) has the same trace and \(\|qV\|\le2r+\varepsilon\).
Compressing by \(L_q,L_p\) yields \(s\sqrt{\langle d^{-1}\rangle_p}\le c(4r+\varepsilon)\).
Jensen and \(0\le p\le e\) give \(s^2\le c(4r+\varepsilon)\tau(hp)\le c(4r+\varepsilon)\tau(he)\).
Letting \(\varepsilon\downarrow0\) gives \(t^2/r\le(64/9)c\,\tau(he)\).
Summing against the stated coefficients and using tracial Cauchy–Schwarz against the same unit vector \(h\) proves (2).

For \(g_j=e_j/\sqrt{t_j}\), positivity and traciality give \(0\le\tau(g_jg_k)\le\sqrt{\min(t_j,t_k)/\max(t_j,t_k)}\le\theta^{|j-k|/2}\).
The row sums of this Gram matrix on any finite segment are bounded by \(B=(1+\sqrt\theta)/(1-\sqrt\theta)\).
Hence \(\|\sum_j a_jg_j\|_2^2\le B\sum_j a_j^2\), by \(2|a_ja_k|\le a_j^2+a_k^2\).
Set \(u_j=t_j^{3/2}/r_j\) and apply (2) with \(\alpha_j=u_j/\sqrt{t_j}\) on each finite segment.
Division by \((\sum_j u_j^2)^{1/2}\) gives (3), including its infinite-series assertion by monotonicity.

### Integration over shifts chosen separately at each scale

Let \(h^*\) be the decreasing rearrangement of \(h\) on \((0,1)\), defined by its trace distribution, and \(A(t)=t^{-1}\int_0^t h^*(v)\,dv\).
For any projection \(p\) of trace \(s\), layer integration of \(h\) and \(\tau(p1_{(a,\infty)}(h))\le\min(s,\tau(1_{(a,\infty)}(h)))\) give \(\tau(hp)\le s A(s)\).
Whenever \(0<t<F(r)\), one can choose a shift whose exact cutoff mass \(s\) exceeds \(t\).
The exact compression and the monotonicity of \(A\) then give \(t/r\le s/r\le2cA(s)\le2cA(t)\).

The averaging operator satisfies \(\|A\|_{L^2(0,1)}\le2\|h^*\|_2=2\).
Indeed \(A(t)=\int_0^1h^*(vt)\,dv\), and Minkowski's integral inequality bounds the norm by \(\int_0^1v^{-1/2}\,dv\,\|h^*\|_2\).
Tonelli's theorem now gives
\[
  \int_0^\infty F(r)^3\frac{dr}{r^3}
   =3\int_0^1 t^2\int_{\{r:F(r)>t\}}\frac{dr}{r^3}\,dt
   \le 6c^2\int_0^1 A(t)^2\,dt\le24c^2.
\]
Since \(F\) is increasing, its integral over \([r,2r]\) with that cubic integrand is at least \(3F(r)^3/(8r^2)\).
Absolute continuity of the integral proves the limit in (1).
The two-Haar assertion now follows from the fixed column criterion.
For instance, a lower bound \(F(r)\ge a r^{2/3}(\log(1/r))^{-1/3}\) for every sufficiently small positive \(r\), with \(a>0\), would already force divergence in (1).
This specifies a sufficient rate for a search and does not supply a law realizing it.

### Scalar shifts with projections in the ambient algebra

The [scalar column theorem and positive compression](Yin_C_F0233_v1.md#a-scalar-commutator-and-positive-weights-in-the-ambient-algebra) give an implementer of norm \(c_0\le12\|\xi_\mu\|_2\) and a normalized density \(d_0\) in \(W^*(Z)\).
For an ambient test \(e,\lambda,r\), let \(w=\mathbb E_{W^*(Z)}e,\ k=w1_{[0,2r]}(|Z-\lambda|)\), and \(s=\tau(k)\).
Then \(0\le k\le w\le1\), \(\tau(w|Z-\lambda|^2)\le r^2 t\), and \(s\ge3t/4\).
Compress the scalar commutator on both sides by \(L_{\sqrt k}\).
The result is \(\sqrt{s}\|\sqrt k d_0^{-1/2}\|_2\le4c_0 r\).
Applying Jensen to the spectral law of \(\sqrt{d_0}\) weighted by \(k/s\) gives \(s^2\le4c_0r\tau(k\sqrt{d_0})\le4c_0r\tau(e\sqrt{d_0})\), using trace-preserving expectation and truncation for the last comparison.
This proves the same simultaneous estimate with the unit vector \(\sqrt{d_0}\).
Exact cutoffs already lie in the scalar algebra, so the exact compression and the rearrangement proof apply there directly.
The Gram estimate uses only the ambient projection traces.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T12:19 |
| status | open |
| reason | Fix the joint tests for arbitrary overlapping projections and the integral of concentration maximized over shifts at every radius. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Uniform cubic concentration integral, overlapping projections, geometric trace sequences and the scalar-shift and free-enlargement consequences. |
| argument | [Argument](#argument) | Rank-one compression, approximate right kernels, trace-weighted Jensen, decreasing rearrangement and the positive Gram estimate. |
| dependency | [Optimal weighted commutator](Yin_C_F0211_v1.md#statement) | A single normalized density and implementer for all omitted shifts at a coordinate of finite right column cost. |
| dependency | [Two-Haar column criterion](Yin_C_F0208_v1.md#statement) | Infinite original cost excludes every bare full-domain system after the free enlargement, which retains actual conjugate variables. |
| dependency | [Scalar column bound and weighted cutoffs](Yin_C_F0233_v1.md#a-scalar-commutator-and-positive-weights-in-the-ambient-algebra) | The marginal implementer bound and compression of a positive spectral weight from an ambient projection. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T12:22 |
| status | proved |
| reason | Adopt the simultaneous projection bound and the cubic integral for the supremum of singular masses over all omitted shifts. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Uniform cubic concentration integral, overlapping projections, geometric trace sequences and the scalar-shift and free-enlargement consequences. |
| argument | [Argument](#argument) | Rank-one compression, approximate right kernels, trace-weighted Jensen, decreasing rearrangement and the positive Gram estimate. |
| dependency | [Optimal weighted commutator](Yin_C_F0211_v1.md#statement) | A single normalized density and implementer for all omitted shifts at a coordinate of finite right column cost. |
| dependency | [Two-Haar column criterion](Yin_C_F0208_v1.md#statement) | Infinite original cost excludes every bare full-domain system after the free enlargement, which retains actual conjugate variables. |
| dependency | [Scalar column bound and weighted cutoffs](Yin_C_F0233_v1.md#a-scalar-commutator-and-positive-weights-in-the-ambient-algebra) | The marginal implementer bound and compression of a positive spectral weight from an ambient projection. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0267_v1.md#finding) | Both compression constants, geometric separation of traces, rearrangement, the scalar specialization and the two-Haar consequence. |

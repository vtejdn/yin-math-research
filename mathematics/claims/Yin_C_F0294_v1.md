---
author: Yin
---

# Cubic concentration from a single bounded slice and least squares on polynomial cuts

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(X\) be a finite tuple of at least two bounded normal generators of a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace and actual starred conjugate variables.
Fix \(Z=X_i\), its derivation \(\delta_i\), the represented starred polynomial algebra \(P\), and the omitted von Neumann algebra \(N=W^*(X_j:j\ne i)\).
Put
\[
 a=\sup_{\|x\|\le1,\ x\in P}\|(\mathrm{id}\otimes\tau)\delta_i x\|_2,\qquad
 F(r)=\sup_{b\in N}\tau(1_{[0,r]}(|Z-b|)),\qquad
 I=\int_0^\infty F(r)^3\,\frac{dr}{r^3}.
\]
Then \(I\le384a^2\) in the extended reals.
In particular a divergent cubic envelope at either coordinate of a normal pair excludes a bare dual system on the original pair.
This also applies to longer tuples and excludes strong duals.

For \(n\ge1\) set \(t_n=2^{-n}\).
For each \(n\) choose the countable dense set \(Q_n\) of trace-\(t_n\) projections in the [polynomial congruence construction](Yin_C_F0288_v1.md#statement) at the designated coordinate.
Writing \(\mathbb E_N\) for the trace-preserving conditional expectation, set
\[
 W_e=\mathbb E_N(e),\qquad C_e=\mathbb E_N(Ze),\qquad
 d(e)=\tau(eZ^*Z)-\lim_{j\to\infty}\tau(C_e(W_e+2^{-j}1)^{-1}C_e^*),
 \qquad d_n=\inf_{e\in Q_n}d(e).
\]
Each \(d_n>0\), and \(I=\infty\) is equivalent to \(\sum_{n\ge1}t_n^4/d_n=\infty\).
Each \(d(e)\) is the limit of least-squares residuals on finite lists of omitted starred words.
These conditions do not presuppose attainment of any shift optimum.

## Argument

### Trimming the right singular projection against two normal densities

Assume \(a<\infty\).
By the [single-input theorem](Yin_C_F0276_v1.md#statement) the slice extends to a normal bounded map \(E:M\to L^2(M)\) and admits two positive densities \(h,k\in L^1(M)\), each of trace at most one, such that
\[
       \|Ex\|_2^2\le a^2\{\tau(hx^*x)+\tau(kxx^*)\}.
\]
It obeys \(E((Z-b)x)-(Z-b)E(x)=\tau(x)1\) for every \(x\in M\) and \(b\in N\).
Indeed the generator commutator and left linearity over the omitted core follow from the product rule there.
For fixed core left factor the extension in \(x\) follows from normality, and separate normal continuity in the bounded omitted factor gives the asserted identity for all \(b\).

Put \(u=h+k\) and denote by \(u^*(v)=\inf\{K\ge0:\tau(1_{(K,\infty)}(u))\le v\}\) its decreasing rearrangement, where the star here denotes rearrangement.
It is finite for \(v>0\), the trace of the indicated open tail at \(K=u^*(v)\) is at most \(v\) by right continuity, and layer integration gives \(\int_0^1u^*(v)\,dv=\tau(u)\le2\).
Fix \(T=Z-b\), \(r>0\), and let \(e,f\) be the right and left spectral cutoffs up to \(r\) of \(|T|\) and \(|T^*|\), respectively.
They have equal trace \(s\) by the unitary polar decomposition in the [shifted singular-law theorem](Yin_C_F0229_v1.md#statement).
Suppose \(s>0\), set \(K=u^*(s/4)\), \(l=1_{(K,\infty)}(u)\), and take the projection
\[
                    p=e\wedge(1-l)\wedge 1_{\{0\}}(|lT|).
\]
The right support of \(lT\) has the same trace as its left support, which is at most \(l\) in projection order.
The trace dimension inequality for intersections thus gives \(\tau(p)\ge s-2\tau(l)\ge s/2\).
Both \(p\) and the left support of \(Tp\) are orthogonal to \(l\), and the right support of \(Tp\) lies under \(p\).
On \(1-l\) the compressed positive forms of both \(h\) and \(k\) are at most \(K(1-l)\) since \(h,k\le u\).
Applying the two-density inequality to \(p,Tp\) and using \(\|Tp\|_2\le r\sqrt{s}\) gives
\[
                 \|E(p)\|_2\le a\sqrt{2Ks},\qquad
                 \|E(Tp)\|_2\le ar\sqrt{2Ks}.
\]
Pair the commutator at \(p\) with \(f\) in the trace Hilbert space.
Since \(\|T^*f\|_2\le r\sqrt{s}\), the result is
\[
       \tfrac12s^2\le s\tau(p)
           \le\sqrt{s}\|E(Tp)\|_2+r\sqrt{s}\|E(p)\|_2
           \le2ar s\sqrt{2K}.
\]
For \(0<t<F(r)\) choose a shift whose cutoff has trace \(s>t\).
Monotonicity of the rearrangement then gives \(t^2/r^2\le32a^2u^*(t/4)\).
With \(q(t)=\inf\{r>0:F(r)>t\}\) for \(0<t<1\), the uniform singular-law bound \(F(r)^2\le\pi r\|\delta_i^*(1\otimes1)\|_2\) and the zero shift give \(0<q(t)\le\|Z\|\).
Every \(r>q(t)\) satisfies \(F(r)>t\), so the last squared estimate holds with \(q(t)\) in place of \(r\).
Integrating in \(t\) gives
\[
 I=3\int_0^1t^2\int_{\{r:F(r)>t\}}\frac{dr}{r^3}\,dt
      =\frac32\int_0^1\frac{t^2}{q(t)^2}\,dt
      \le192a^2\int_0^{1/4}u^*(v)\,dv\le384a^2.
\]
The value at an endpoint \(r=q(t)\) does not affect the inner integral.
The [normal bare-dual theorem](Yin_C_F0070_v1.md#statement) makes \(a\) finite at every coordinate when a bare system exists.
This proves the original-tuple obstruction, including in dimension two.

### Optimal residual on a prescribed projection

For any projection \(e\in M\) the squared error of \(b\in N\) is
\[
 J_e(b)=\|(Z-b)e\|_2^2
       =\tau(eZ^*Z)-2\operatorname{Re}\tau(b^*C_e)+\tau(bW_e b^*).
\]
Completing the square in \(J_e(b)+\eta\|b\|_2^2\) for \(\eta>0\) gives the bounded minimizer \(C_e(W_e+\eta1)^{-1}\) and minimum \(\tau(eZ^*Z)-\tau(C_e(W_e+\eta1)^{-1}C_e^*)\).
These minima decrease to \(\inf_{b\in N}J_e(b)\), since the penalty at any fixed \(b\) tends to zero.
For fixed bounded \(b\) the quantity \(J_e(b)=\tau(e|Z-b|^2)\) is continuous in \(e\) in the trace Hilbert metric.
Taking the infimum first in \(e\) for fixed \(b\) shows that \(d_n\) is the same infimum over the entire trace layer as over \(Q_n\), including when all minimizing sequences of shifts are unbounded in operator norm.

Enumerate the omitted starred words, including the unit, as \(w_1,w_2,\ldots\).
For the first \(m\) form \(G_{ab}=\tau(e w_a^*w_b)\), \(g_a=\tau(e w_a^*Z)\).
The minimum of \(J_e\) over their complex span is \(\tau(eZ^*Z)-g^*G^\dagger g\), with \(G^\dagger\) the Moore–Penrose inverse.
This is the squared distance from \(Ze\) to the span of \(w_ae\), so \(g\) is orthogonal to the nullspace of \(G\).
By bounded strong-star approximation by omitted starred polynomials, \(be\) lies in the trace Hilbert closure of these spans for every \(b\in N\).
Hence the finite minima decrease to \(d(e)\).

### Comparing the errors with the singular-mass quantiles

Fix \(t=t_n\).
For \(r<q(t/2)\) the right cutoff at radius \(r\) has trace at most \(t/2\) for every shift.
Testing \(|Z-b|^2\ge r^2 1_{(r,\infty)}(|Z-b|)\) against any trace-\(t\) projection and letting \(r\uparrow q(t/2)\) proves the first inequality below.
For \(r>q(t)\) some bounded \(b\) has cutoff of trace greater than \(t\).
It contains a trace-\(t\) subprojection by diffuseness of corners, on which the squared error is at most \(tr^2\).
Letting \(r\downarrow q(t)\) gives the upper bound
\[
                    0<\tfrac12 t\,q(t/2)^2\le d_n\le t\,q(t)^2 .
\]
With \(B_n=t_n^3/q(t_n)^2\), these inequalities yield \(B_n\le t_n^4/d_n\le16 B_{n+1}\).
The integral of \(t^2/q(t)^2\) over \([1/2,1)\) is finite.
On \([t_{n+1},t_n]\), replacing \(q\) by its endpoint values bounds the integral below by \(7B_n/24\) and above by \(7 B_{n+1}/3\).
The layer integral formula therefore proves the asserted equivalence, independently of finiteness of \(a\).
This reduces a counterexample search to a series of residuals computed on the joint law.
Whether one actual normal tuple has a divergent series, and whether the canonical slices are bounded for every tuple with finite series, remain open.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T15:02 |
| status | open |
| reason | Fix the two-density trimming estimate and the countable regression test for independent inspection. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Cubic bound from the original one-input norm in every dimension at least two and the dyadic divergence test. |
| argument | [Argument](#argument) | Quantile trimming of both supports, integration, regularized least squares, polynomial cuts and Gram approximation. |
| dependency | [Single-input theorem](Yin_C_F0276_v1.md#statement) | Normal bounded extension, two normal densities of trace at most one and omitted left module property. |
| dependency | [Singular-law theorem](Yin_C_F0229_v1.md#statement) | Uniform mass bound and unitary polar decomposition for every omitted shift. |
| dependency | [Bare normal duals](Yin_C_F0070_v1.md#statement) | A bare dual system yields finite original single-input slice norm. |
| dependency | [Polynomial congruence cuts](Yin_C_F0288_v1.md#statement) | Countable dense family of projections of each prescribed interior trace in the original algebra. |
| dependency | [Projection layers](Yin_C_F0282_v1.md#a-bounded-patch-in-a-fixed-trace-layer) | Diffuseness of corners and trace dimension inequality for projections. |
| dependency | [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Bounded strong-star approximation in the omitted generated algebra. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T15:10 |
| status | proved |
| reason | Independent review verified the two-density estimate on the original pair and the equivalence between divergence of the cubic integral and the dyadic residual series. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Cubic bound from the original one-input norm in every dimension at least two and the dyadic divergence test. |
| argument | [Argument](#argument) | Quantile trimming of both supports, integration, regularized least squares, polynomial cuts and Gram approximation. |
| dependency | [Single-input theorem](Yin_C_F0276_v1.md#statement) | Normal bounded extension, two normal densities of trace at most one and omitted left module property. |
| dependency | [Singular-law theorem](Yin_C_F0229_v1.md#statement) | Uniform mass bound and unitary polar decomposition for every omitted shift. |
| dependency | [Bare normal duals](Yin_C_F0070_v1.md#statement) | A bare dual system yields finite original single-input slice norm. |
| dependency | [Polynomial congruence cuts](Yin_C_F0288_v1.md#statement) | Countable dense family of projections of each prescribed interior trace in the original algebra. |
| dependency | [Projection layers](Yin_C_F0282_v1.md#a-bounded-patch-in-a-fixed-trace-layer) | Diffuseness of corners and trace dimension inequality for projections. |
| dependency | [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Bounded strong-star approximation in the omitted generated algebra. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0303_v1.md#finding) | Complete fixed candidate and its declared dependency interfaces. |

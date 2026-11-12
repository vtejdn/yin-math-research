---
author: Yin
---
# Central support and three translates in two common-power cases

Date: 2026-11-12 (Asia/Hong_Kong).
This argument tests two of the common-power alternatives in [C_A0009_v4](../claims/Yin_C_A0009_v4.md#all-positive-eight-cycle-classes).

## Statement

For actual elements \(a,b\) of a torsion-free group, put \(T=1+a-b\) and \(\delta=\dim_G\ker T\).
The conclusions are
\[
 b^2=a^3\quad\Longrightarrow\quad\delta\le\frac16,
 \qquad
 (ba^2)^2=a^3\quad\Longrightarrow\quad\delta\le\frac16.
\tag{1}
\]
There is also a precise central-support bound, proved using bounded spectral cuts rather than an assumed fiber representation.
No freeness, orderability or inheritance of an Atiyah property by an arbitrary quotient is used.

The finite-cycle classification in C_A0009_v4 is not a proof input for (1).
Together with that [accepted classification](../claims/Yin_C_A0009_v4.md#decision-reviewed-short-cycle-bound), (1) leaves only \((ba)^2=a^3\) among its three alternatives for a hypothetical \(\delta\ge1/4\), with the same exact moments and negative-class restrictions.
The previous universal strict bound \(\delta<8/29\) remains in force; no zero-kernel conclusion is asserted here.

<a id="argument"></a>

## Actual subgroup, spectral cuts and reused foundations

Work first in \(H=\langle a,b\rangle\) and \(M=\mathcal N(H)\), with the canonical probability trace \(\tau\).
Right-coset decomposition transfers the kernel dimension to an arbitrary ambient group \(G\).
An element called central below is central in \(H\) and \(M\); it need not be central in the ambient group.
The [cyclic regular spectral law](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions), the [bounded compression method](../claims/Yin_C_A0009_v2.md#the-exact-compression-imposed-by-a-three-term-kernel), and the [polar-decomposition dimension argument](../claims/Yin_C_A0009_v3.md#the-first-translate-configuration-closes-at-two-copies) are reused at their stated scopes.
The finite spectral projections and trigonometric formulas below are derived directly.
No additional external theorem, historical priority or general direct-integral assertion is adopted.

Suppose first that \(b^2=a^3=z\).
The element \(z\) commutes with \(a\) and \(b\), hence is central in \(H\).
If \(a=e\), torsion-freeness forces \(b=e\), and \(T=1\).
Thus the only case requiring a proof has \(a\ne e\), so \(z\) has infinite order and has Haar spectral law under \(\tau\).
In particular each singleton spectral projection of \(z\) is zero.

Let \(\theta=\operatorname{Arg}(z)\), with the Borel branch \(-\pi<\theta\le\pi\), and let
\[
 e_E=1_E(\theta)
\]
denote its central spectral projection for a Borel set \(E\subset(-\pi,\pi]\).
Then
\[
 \tau(e_E)=\frac{|E|}{2\pi},
\tag{2}
\]
where \(|E|\) is Lebesgue measure.
All singleton exceptions below therefore disappear as actual operator projections, by faithfulness of the trace.

## The relation \(b^2=a^3\) pins the compression

Put \(p=P_{\ker T}\) and \(A=pap\).
The bounded equation \(bp=(1+a)p\), followed by taking its norm square, gives
\[
 A+A^*=-p,\qquad pbp=p+A.
\tag{3}
\]
Since \(b^*=z^{-1}b\), taking adjoints of the second relation in (3) also gives
\[
 p+A^*=z^{-1}(p+A).
\]
Using \(A+A^*=-p\), this becomes the bounded identity
\[
 (1+z)A=-p.
\tag{4}
\]
This pins the compression, whereas the original trinomial equation alone only pins its real part.

For complete domain control, let
\[
 f_N=1_{\{|1+z|\ge1/N\}}.
\]
These are central projections increasing to one, because the spectral projection at \(z=-1\) is zero.
The inverse of \(1+z\) on \(f_N\) is bounded, so (4) gives the ordinary bounded equality
\[
 Af_N=c(z)pf_N,\qquad c(z)=-\frac1{1+z}.
\tag{5}
\]
Every subsequent formula involving this rational function is first read on these cuts.
Equivalently, (5) is the actual central affiliated identity \(A=c(z)p\), but no unbounded inverse is applied to an arbitrary Hilbert-space vector.

## Three root projections and the exact allowed half-circle

For \(k=0,1,2\), define central unitary functions and spectral projections
\[
 \lambda_k(z)=\exp\left(\frac{i(\theta+2\pi k)}3\right),
 \qquad
 E_k=\frac13\left(1+\lambda_k^{-1}a+\lambda_k^{-2}a^2\right).
\tag{6}
\]
Since \(a^3=z=\lambda_k^3\), the elementary finite Fourier identities show that the \(E_k\) are mutually orthogonal selfadjoint projections, that their sum is one, and that \(aE_k=\lambda_kE_k\).
This constructs the three-root decomposition inside the actual von Neumann algebra.

One also has \(a^2=za^*\), so (5) implies
\[
 pa^2pf_N=z\overline{c(z)}pf_N.
\]
Compressing (6), and using \(z\lambda_k^{-2}=\lambda_k\), gives
\[
 pE_kpf_N=t_k(z)pf_N,
 \qquad
 t_k(z)=\frac{1+2\operatorname{Re}(c(z)\lambda_k^{-1})}{3}.
\tag{7}
\]
In particular these scalar central coefficients must be nonnegative wherever \(p\) has central support.

For \(-\pi<\theta<\pi\), the explicit expression is
\[
 t_k(\theta)=\frac13\left(
 1-\frac{\cos(5\theta/6+2\pi k/3)}{\cos(\theta/2)}
 \right).
\tag{8}
\]
The denominator is positive on this interval.
For \(0<\theta<\pi\), elementary difference-of-cosines identities give
\[
\begin{aligned}
 t_0(\theta)
 &=\frac{2\sin(2\theta/3)\sin(\theta/6)}{3\cos(\theta/2)},\\
 t_1(\theta)
 &=\frac{2\sin((2\theta+\pi)/3)\sin((\theta+2\pi)/6)}
 {3\cos(\theta/2)},\\
 t_2(\theta)
 &=\frac{2\sin((\pi-2\theta)/3)\sin((2\pi-\theta)/6)}
 {3\cos(\theta/2)}.
\end{aligned}
\tag{9}
\]
Thus \(t_0,t_1>0\) there, while \(t_2\) has the sign of \(\pi/2-\theta\).
For negative angles, \(t_0(-\theta)=t_0(\theta)\) and \(t_1(-\theta)=t_2(\theta)\).
Consequently all three weights are strictly positive exactly when
\[
 0<|\theta|<\frac\pi2,
\tag{10}
\]
apart from the zero values at the boundary angles.
At \(\theta=0\), their values are \((0,1/2,1/2)\); at \(\theta=\pi/2\) or \(-\pi/2\), one other weight is zero.
Those three singleton sets, and the branch endpoint \(z=-1\), have zero spectral projection.

To convert the signs into support without an informal fiber argument, intersect an arbitrary region \(\{t_k\le-\varepsilon\}\), \(\varepsilon>0\), with \(f_N\).
On that central cut the left side of (7) is positive and the right side is at most \(-\varepsilon p f_N\).
Therefore \(p\) vanishes on that cut.
Taking unions over positive rational \(\varepsilon\) and over \(N\) excludes every region with a negative weight.
The preceding signs prove
\[
 \boxed{p=e_Ip,\qquad I=(-\pi/2,\pi/2),\qquad\tau(e_I)=\frac12.}
\tag{11}
\]
Using the closed half-circle would give the same operator projection.
On this support, \(|1+z|\ge\sqrt2\), so the compressed rational function in (5) is now bounded.

## Three columns give the conditional dimension bound

Consider the bounded synthesis row on three copies of \(p\ell^2(H)\),
\[
 F(\xi_0,\xi_1,\xi_2)=\xi_0+a\xi_1+a^2\xi_2.
\tag{12}
\]
Its Gram matrix is \(G=(pa^{j-i}p)_{0\le i,j\le2}\).
Let \(V\) be the central matrix
\[
 V_{kj}=\frac{\lambda_k^j}{\sqrt3},\qquad 0\le k,j\le2.
\]
The ratios of the \(\lambda_k\) are the distinct third roots of unity, so \(V\) is unitary.
Equations (6)--(7) imply the exact identity
\[
 G=3V^*\operatorname{diag}(t_0p,t_1p,t_2p)V
\tag{13}
\]
on the support (11).
For example, its \((i,j)\) entry is \(\sum_k\lambda_k^{j-i}t_kp=pa^{j-i}p\), which checks the ordering and complex conjugates.

Let \(g_N\) be the central projection inside \(e_I\) where \(\min_k t_k\ge1/N\).
These projections increase to \(e_I\), since the exceptional zero weights have singleton support of trace zero.
On three copies of \(pg_N\ell^2(H)\), (13) is bounded below by \((3/N)\) times the identity projection.
Therefore the row (12), restricted to that domain, is injective.
Its range lies in \(g_N\ell^2(H)\), because \(g_N\) is central.
Polar decomposition with the usual unnormalized trace on the three-column domain gives
\[
 3\tau(pg_N)\le\tau(g_N).
\tag{14}
\]
Normality of the trace and (11) yield
\[
 \boxed{\delta\le\frac13\tau(e_I)=\frac16.}
\tag{15}
\]
No uniform positive lower bound on the weights over the whole half-circle is required.
The bounded-cut argument supplies the dimension conclusion even though their values approach zero.

The same proof after intersecting every cut with an arbitrary \(e_E\) proves the stronger measure inequality
\[
 \boxed{3\tau(pe_E)\le\tau(e_{E\cap I})
 =\frac{|E\cap I|}{2\pi}
 \quad\text{for every Borel }E\subset(-\pi,\pi].}
\tag{16}
\]
This is a precise conditional trace bound: the kernel has zero mass off the half-circle and at most one third of the ambient central spectral mass on every subset of it.
It states the intended fiber-trace restriction without assuming any particular direct-integral realization or a countability property of the full ambient group.

## The \(j=2\) relation transfers by an exact adjoint identity

Now assume \((ba^2)^2=a^3=z\), and put \(w=ba^2\).
Then \(H=\langle a,w\rangle\), \(w^2=a^3=z\), and \(z\) is central.
If \(a=e\), torsion-freeness again gives \(b=e\), so the degenerate case is immediate.
Otherwise \(z\) has the same infinite-order Haar spectral law used above.
Let
\[
 Q=1+a-w.
\]
The already proved case with \(w^2=a^3\) applies to \(Q\) in this actual group, without any replacement of the group by its one-relator presentation.
The original operator satisfies
\[
 T a^2=a^2+a^3-w=zQ^*,
\tag{17}
\]
because \(a^2=za^*\) and \(w=zw^*\).
Multiplication by \(a^2\) and \(z\) preserves kernel dimensions, and polar decomposition in a finite von Neumann algebra makes the kernel traces of \(Q\) and \(Q^*\) equal.
These assertions hold separately on every central spectral cut \(e_E\).
Consequently, if \(p_T\) and \(p_Q\) are the two kernel projections,
\[
 \tau(p_Te_E)=\tau(p_Qe_E)
 \quad\text{for every Borel }E.
\tag{18}
\]
Thus (11), (15) and (16) all transfer to \(T\).
In particular \(\dim_G\ker T\le1/6\), proving the second assertion in (1).

## The remaining middle relation and the exact boundary

For comparison only, suppose \((ba)^2=a^3=z\) and write \(w=ba\).
The kernel-preserving right multiplication gives
\[
 S=Ta=a+a^2-w.
\tag{19}
\]
Here \(w^2=a^3=z\) implies
\[
 S^*=z^{-1}S.
\tag{20}
\]
Since \(z\) is central, \(S\) is normal.
More explicitly, with the bounded central square root \(\zeta=e^{i\theta/2}\), the operator \(\zeta^{-1}S\) is selfadjoint.
This does not imply that its kernel is zero.

The scalar-compression step (4) does not transfer to (19).
If \(r=P_{\ker S}\) and \(C=rar\), then \(wr=(a+a^2)r\) gives
\[
 C+C^*=-r,\qquad rwr=C+zC^*.
\tag{21}
\]
The relation \(w^*=z^{-1}w\), after compression, becomes
\[
 (C+zC^*)^*=z^{-1}(C+zC^*),
\]
which is an identity for every \(C\) commuting with the central \(z\).
It supplies no equation pinning \(C\) to a scalar function of \(z\).
Thus the half-circle support conclusion proved for \(j=0,2\) has not been established for \(j=1\).
No injectivity, improved numerical bound, or exclusion of a known group class is inferred from the normality in (20).

The [generic Laurent-rank theorem](../claims/Yin_C_A0012_v2.md#exact-generic-rank-for-rectangular-laurent-matrices) does not apply merely because \(z\) is central.
That theorem uses a specified finite Laurent expression with bounded coefficients in an actual coefficient-algebra tensor product with the central circle algebra.
The present central extension has not been shown to split in that way, and no such finite Laurent realization with a fixed bounded coefficient algebra has been supplied.
The central spectral cuts and Gram argument above do not require that additional realization and do not assume a generic-specialization conclusion for these group operators.

By the accepted finite-cycle statement of [C_A0009_v4](../claims/Yin_C_A0009_v4.md#statement), any hypothetical \(\delta\ge1/4\) must satisfy exactly one of the three relations \((ba^j)^2=a^3\).
The bounds (1) exclude \(j=0\) and \(j=2\) from that hypothetical range.
The only remaining alternative is therefore
\[
 \boxed{(ba)^2=a^3,\qquad\delta\ge1/4,}
\tag{22}
\]
together with that finite-cycle statement's exact moment and negative-class restrictions.
This narrows the residual configuration under the hypothesis \(\delta\ge1/4\), without proving that it exists.
The original all-matrix Task and the vanishing of the scalar kernel remain unresolved.

## Assessment history

### Decision reviewed-central-three-translates

| Field | Value |
| --- | --- |
| date | 2026-11-11T19:34 |
| status | proved |
| reason | Independent whole-artifact review verifies the central compression, finite root projections, bounded-cut three-column Gram, conditional trace bound, exact adjoint transfer and narrowing to the middle common-power relation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both common-power bounds of 1/6, exact central-support and measure restrictions, and the residual middle relation for a hypothetical kernel of trace at least 1/4. |
| argument | [Argument](#argument) | The full bounded-cut proof, all exceptional spectral points, Gram and trace calculations, transfer, accepted finite-cycle interface and remaining-case limits. |
| review | [Independent whole-artifact finding](../audits/reviews/Yin_R_A0028_v4.md#whole-artifact-finding) | Entire fixed statement and argument, actual domains and subgroup trace, with the older finite classification reused at its accepted scope. |

## Current assessment

[Selected decision](#decision-reviewed-central-three-translates)


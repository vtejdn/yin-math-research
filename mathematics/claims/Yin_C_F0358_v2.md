---
author: Yin
---

# Exactly real eigenvalues and the fixed-shift contribution from the nonreal spectrum

<a id="statement"></a>
## The two symmetrizer classes

Use either of the two classes of the [polynomial symmetrizer theorem](Yin_C_F0358_v1.md#statement), with its complex Hermitian Wigner laws, its fixed \(P,G\), limiting selfadjoint \(h\), and arbitrary cross-size coupling.
Count eigenvalues with algebraic multiplicities.
For every finite realization, write \(k_N=\dim\ker G_N\), \(d_N=n_-(G_N)\), and let \(m_N\) be the number of nonreal eigenvalues of \(P_N\).
Then
\[
             m_N\le 2d_N+k_N .
\]
Almost surely \(m_N/N\to0\), and the subprobability measure counting only the exactly real eigenvalues of \(P_N\), with weight \(1/N\) each, converges weakly to the full law of \(h\).
In particular this conclusion applies to the [shared-input example at the free spectral edge](Yin_C_F0358_v1.md#example).

For each compact \(K\subset\mathbb C\setminus\mathbb R\) put
\[
 D_N(z)=\frac1N\sum_{\operatorname{Im}\lambda\ne0}\log^-|\lambda-z|,
 \qquad u(z)=\tau\log|p-z|.
\]
On one probability-one event there are finite continuous functions \(e_N\) on \(K\) with \(\sup_K|e_N|\to0\) and
\[
 \frac1N\log|\det(P_N-zI)|=u(z)+e_N(z)-D_N(z),\qquad z\in K .
\]
Use \(+\infty\) for \(D_N(z)\) when a root equals \(z\).
Consequently the almost-sure ordinary limsup equality at a prescribed nonreal \(z\) is equivalent to \(\liminf_N D_N(z)=0\) almost surely.
The equivalent question for an exact word-chain pencil has the same loss divided by its fixed auxiliary size.

<a id="argument"></a>
## A finite-dimensional bound from the two ends of the real axis

In the [finite range compression](Yin_C_F0358_v1.md#argument), write \(D=G_N|_{\operatorname{ran}G_N}\), \(C=P_N|_{\operatorname{ran}G_N}\).
For \(R\) sufficiently large for this realization, the inertia of \((C+R)D\) equals that of \(D\), and that of \((C-R)D\) equals that of \(-D\).
Indeed divide by \(R\) and use norm convergence to the two invertible Hermitian matrices \(D,-D\).
The net increase in negative inertia is therefore \(\dim\operatorname{ran}G_N-2n_-(G_N)\).
The finite jump inequality gives at least this many real eigenvalues in \((-R,R)\), proving the upper bound for \(m_N\), also if the right side exceeds \(N\).
The empty range gives the same bound directly.

In both model classes the limiting \(g\) is positive and has zero kernel.
By [selfadjoint polynomial weak convergence](Yin_C_F0186_v4.md#finite-variance-weak), the normalized number of eigenvalues of \(G_N\) in the closed set \((-\infty,0]\) tends to zero almost surely.
Therefore \(m_N=o(N)\) on that event.
Removing these eigenvalues changes the integral of a bounded test function by at most its supremum times \(m_N/N\).
The [earlier weak limit](Yin_C_F0358_v1.md#free-inertia) now proves convergence of the measure on the exactly real roots.
The [thin-support theorem](Yin_C_F0186_v25.md#statement) already gives the full weak measure once its free support is identified as real.
Weak convergence to a real-supported law by itself allows every finite root to have nonzero imaginary part.

<a id="loss"></a>
## Isolating the remaining logarithmic error

Sum \(\log|\lambda-z|\) first over the real eigenvalues.
For \(z\in K\) this logarithm is bounded below by \(\log\operatorname{dist}(K,\mathbb R)\).
Its positive tail is uniformly integrable in \(\lambda\) along the realization by the [almost-sure bound on the positive logarithmic second moment](Yin_C_F0186_v4.md#log-statistics).
Weak convergence of the real-root measure therefore gives pointwise convergence of this partial potential to \(\int\log|t-z|\,d\mu_h(t)=u(z)\).
Convergence is uniform on \(K\): differences in the log distances to a real root at two points of \(K\) are bounded by their separation divided by \(\operatorname{dist}(K,\mathbb R)\).
The free potential has the same estimate.

The normalized sum of \(\log^+|\lambda-z|\) on nonreal roots tends uniformly to zero on \(K\).
Indeed \(\log^+|\lambda-z|\le C_K+\log^+|\lambda|\), so Cauchy--Schwarz bounds the sum by \(C_Km_N/N+O_\omega(\sqrt{m_N/N})\).
Let \(e_N\) be the partial real-root potential minus \(u\), plus this nonreal positive sum.
This gives the stated identity without adding or subtracting infinite terms and proves the equivalence at the fixed point.
For a linearization use [ordinary and free block elimination](../ledger/Yin_L_F0061_v2.md#linearization-transfer).
An estimate on distances from the at most \(2d_N+k_N\) roots to the specified parameter remains necessary in the absence of finite positivity or other information about these roots.

## Current assessment
[Selected decision](#decision-real-roots-reviewed)

## Assessment history

### Decision real-roots-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T16:31 |
| status | open |
| reason | Comparing the two extreme inertias bounds the number of nonreal roots and confines the remaining fixed-parameter loss to those roots. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exactly real roots and ordinary determinants](#statement) | Almost-sure real-root abundance and the residual loss away from the real axis. |
| argument | [Finite count](#argument) | Includes finite singular and indefinite symmetrizers. |
| support | [Uniform error decomposition](#loss) | Handles coincidences with a prescribed shift and both trace normalizations. |

### Decision real-roots-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T16:33 |
| status | proved |
| reason | The extreme inertias bound the nonreal algebraic count, and the real-root weak limit isolates the remaining prescribed-shift logarithmic loss. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Precise result](#statement) | Both metric classes, exact real roots and the compact-uniform finite error off the real line. |
| argument | [Complete proof](#argument) | The extreme inertias bound the nonreal algebraic count, and the real-root weak limit isolates the remaining prescribed-shift logarithmic loss. |
| review | [Whole-proof assessment](../audits/reviews/Yin_R_F0366_v2.md#real-roots-whole-proof) | Both metric classes, exact real roots and the compact-uniform finite error off the real line. |

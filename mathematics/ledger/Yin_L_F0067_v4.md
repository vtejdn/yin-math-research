---
author: Yin
---

# A uniform spectral gap can be lost after one real sign-column compression

The [Gaussian flag proof](../claims/Yin_C_F0351_v1.md#later-hyperplanes) and its [mixed-law extension](../claims/Yin_C_F0351_v2.md#quadratic-matchings) estimate the change of a determinant after compression onto the orthogonal complement of a fresh real column.
The following calculation tests whether a lower bound on the singular values of the symmetric matrix in that quadratic form suffices for a sign column at every possible exterior.
The [earlier open-chain construction](Yin_L_F0067_v3.md#one-coordinate) tests variation in an interior entry with the exterior fixed.

<a id="sign-compression"></a>
## Exact compression for every sign column

Take even \(n\) and the \(n/2\) arguments \(\theta_j=(2j-1)\pi/n\) in the open upper half-plane.
Let \(M\) be the direct sum of the real rotations
\[
 M_j=\begin{pmatrix}\cos\theta_j&-\sin\theta_j\\ \sin\theta_j&\cos\theta_j\end{pmatrix}.
\]
Its eigenvalues are exactly the roots of \(z^n+1\).
The matrix is normal and \(s_{\min}(zI-M)\ge 1-|z|\) for \(|z|<1\).
This example has the required polynomial form with bounded deterministic real symmetric factors: on block \(j\) use \(A_j=\operatorname{diag}(1,-1)\) and \(B_j=\left(\begin{smallmatrix}t/3&s\\s&-t/3\end{smallmatrix}\right)\) with \(t=\cos\theta_j,\ s=\sin\theta_j\), as in the [two-dimensional evaluation](../claims/Yin_C_F0349_v1.md#argument).

Let \(v=g/\sqrt n\) for any \(g\in\{-1,1\}^n\), and let \(C\) be the compression of \(M\) to \(v^\perp\).
The symmetric part under transpose of each two-dimensional block of \((zI-M)^{-1}\) is a scalar times the identity.
Every entry of \(v\) has squared modulus \(1/n\), so
\[
 v^{\mathsf T}(zI-M)^{-1}v
   =\frac1n\operatorname{Tr}(zI-M)^{-1}
   =\frac{z^{n-1}}{z^n+1}.
\]
The cofactor identity gives \(\det(zI-C)=z^{n-1}\).
For \(|z|\le r<1\), \(z\ne0\), the normalized logarithmic loss of this one compression relative to \(M\) is
\[
 \frac1n\log|z^n+1|-\frac{n-1}{n}\log|z|.
\]
It stays uniformly positive on any fixed disk compactly contained in \(0<|z|<1\) for all large \(n\).
On a disk also disjoint from the real axis, the symmetric part of the inverse still has all singular values bounded below by \(|\operatorname{Im}z|/(1+r)^2\), by the inverse identity of C351v1.
In particular a large matching of coefficients can consist entirely of square terms, which become constants under the two-point sign law.

For independent Rademacher entries in the column, failure here has conditional probability one for this deterministic exterior and a whole nonreal disk.
The construction makes no assertion about the probability that these exterior matrices occur as a Wigner minor or about the determinant after additional hyperplane deletions.
The [actual-minor and discrete interior tests](../drafts/Yin_D_F0044.md) take account of constraints on the physical Wigner pair before the first deletion.

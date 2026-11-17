---
author: Yin
---

# A one-dimensional terminal deficit in the real quadratic companion problem

The [paired-border argument](../claims/Yin_C_F0347_v1.md#statement) and the [actual Wigner border calculation](../claims/Yin_C_F0186_v36.md#one-step) leave the last few singular values in the potential of \(AB+2BA\).
This calculation tests whether a floor in probability and convergence of a trimmed product suffice to control their planar contribution almost surely.
It combines the [real reversal and shift construction](Yin_L_F0066_v23.md#exterior-chain) with the [finite and cyclic shift comparison](Yin_L_F0061_v2.md#brown-nonimplication).
The [preceding paired-border discussion](Yin_L_F0067_v2.md#paired-border-terminal) retains its separate conditional example for genuine Wigner entries.

<a id="rare-chain"></a>
## Two bounded real symmetric inputs

Let \(S\) be the upper shift of size \(N\), \(U=S+e_Ne_1^t\) the cyclic shift and \(R\) the coordinate reversal.
Put \(B=R\).
Choose \(A=SR\) with probability \(1/N\) and \(A=UR\) otherwise, independently across sizes.
Both choices are real symmetric contractions.
Since \(RSR=S^t\) and \(RUR=U^t\), the matrix \(AB+2BA\) is respectively \(S+2S^t\) or \(U+2U^t\).
The normal cyclic matrices have empirical eigenvalue measures tending to the image of Haar circle measure under \(w\mapsto w+2w^{-1}\).
The open-chain matrices are diagonally similar to the real symmetric tridiagonal matrices with off-diagonal entries \(\sqrt2\), by conjugating with a diagonal geometric progression.
They have real eigenvalues \(2\sqrt2\cos(j\pi/(N+1))\), \(1\le j\le N\).
The two eigenvalue laws have different weak limits.
The independent events of probability \(1/N\) occur infinitely often, so weak convergence to the cyclic law holds in probability and fails almost surely in this example.

<a id="terminal-loss"></a>
## Only the smallest value carries the exceptional loss

Write \(\Omega=\{z:|z-i/2|\le1/20\}\).
All shifted cyclic matrices have a common positive singular-value lower bound on \(\Omega\), by the positive distance from this disk to the ellipse \(\{3\cos t-i\sin t:t\in\mathbb R\}\).
For the open chain \(T=S+2S^t-zI\), on the codimension-one subspace perpendicular to \(\ker S^t\) the triangle inequality gives \(\|Tv\|\ge(1-|z|)\|v\|\).
Thus at most one singular value can fall below \(1-\sup_{\Omega}|z|>0\).
Every singular value is bounded above by \(3+\sup_{\Omega}|z|\).

The normalized cyclic logarithmic potential tends uniformly on \(\Omega\) to \(\log2\).
Indeed the Riemann sums converge uniformly because of the gap, and Jensen's circle formula evaluates the mean of \(\log|w^2-zw+2|\).
Both roots lie outside the unit circle for \(z\in\Omega\), by continuity from zero throughout the ellipse interior.
For the open chain the log determinant converges uniformly on the same disk to \(\log|r(z)|\), where \(r(z)\) is the larger-modulus root of \(r^2-zr+2=0\).
The exact tridiagonal recurrence gives the determinant in modulus as \(|(r^{N+1}-r'^{\,N+1})/(r-r')|\), with \(r'\) the other root.
The two roots have distinct moduli off the real segment \([-2\sqrt2,2\sqrt2]\).
Compactness gives \(\sup_{\Omega}|r'/r|<1\), and \(\sup_{\Omega}|r|<2\) since \(|r|=2\) forces \(z=r+2/r\) onto the ellipse.
In particular the two normalized log determinants differ by a fixed positive amount throughout the disk for large \(N\).

For a deterministic cutoff \(L_N\to\infty\) with \(L_N=o(N)\), the difference of the two shifted matrices has rank at most two.
The singular-value interlacing inequality therefore bounds the absolute difference of their normalized clipped log sums by \(2(L_N+\log(3+\sup_\Omega|z|))/N\) for all sufficiently large \(N\).
Equivalently, apply the rank comparison to the bounded monotone test \(s\mapsto\max(\log s,-L_N)\) on the common spectral interval.
The clipped log potentials of both cases consequently converge uniformly to the cyclic target on this disk.
Since only the smallest singular value can drop below the fixed lower bound above, deleting that one value also gives uniform convergence to the cyclic target in both cases.
To see this directly, clip at a fixed positive level below both the cyclic gap and the lower bound on the second-smallest open-chain singular value.
The clipped sums change by \(O(1/N)\) across the rank-two perturbation, and omitting their last bounded clipped summand costs \(O(1/N)\).
Restoring the true last value in the open chain produces a deficit bounded below on the disk after normalization, and thus gives a positive lower bound after area integration.
In particular the smallest open-chain singular value is exponentially small there, uniformly in \(z\).

This model realizes the same polynomial in two bounded real symmetric inputs and exhibits nonsummable failures on a fixed nonreal disk, with just one exceptional terminal value.
Its within-size entry law has dependent coordinates.
For the [Wigner Task](../tasks/Yin_T_F0012_v3.md#contract), one must exploit the original independent-entry distribution to bound the frequency or integrated cost of the terminal loss.
The construction determines no lower bound on that frequency for a Wigner ensemble.

<a id="one-coordinate"></a>
## Conditional oscillation on changing one Wigner diagonal coordinate

The open chain admits a perturbation of one diagonal entry of \(A\) at the scale of the Wigner normalization.
Write \(S_t=S+t e_Ne_1^t\), \(A_t=S_tR=SR+t e_Ne_N^t\), \(B=R\), and \(M_t=A_tB+2BA_t=S_t+2S_t^t\).
For the open chain of size \(j\), let \(d_j(z)=\det(S+2S^t-zI_j)\), with the shifts on the right taken at size \(j\).
The recurrence \(d_0=1,\ d_1=-z,\ d_j=-zd_{j-1}-2d_{j-2}\) gives \(\sup_\Omega |d_j|/2^j\le Cq^j\) for constants \(C<\infty,\ 0<q<1\) by the root bounds above.
For \(N\ge3\), expanding the two corner entries gives
\[
 \det(M_t-zI_N)=d_N(z)-2t^2d_{N-2}(z)+(-1)^{N-1}t(1+2^N).
\]
Indeed a term using both corners contains the transposition of the two endpoints and the open interior minor.
A term using only one corner must traverse the other \(N-1\) edges of the chain in the corresponding direction, giving one of the two oriented \(N\)-cycles.
Hence for \(t=N^{-1/2}\) and for \(t=1\) the determinant has modulus \(2^N t(1+o(1))\) uniformly on \(\Omega\).
The normalized log potential increases by at least a constant \(c>0\) on this disk when \(t\) changes from zero to \(N^{-1/2}\), for all sufficiently large \(N\).

At these prescribed matrices the perturbed chain also has a uniform polynomial least-value bound on the disk.
The matrix \(K=(M_1-zI_N)^{-1}(M_t-zI_N)\) differs from \(I_N\) by rank at most two and has bounded norm by the cyclic gap.
At most two of its singular values exceed one, by restricting to the kernel of \(K-I_N\).
The determinant ratio therefore gives
\[
 s_{\min}(K)\ge\frac{|\det K|}{\max(1,\|K\|)^2}\ge c' N^{-1/2}
\]
for \(t=N^{-1/2}\) and a uniform \(c'>0\) after decreasing the constant.
Multiplying by \(M_1-zI_N\) preserves this lower bound up to its uniform gap constant.

To test conditioning under actual Wigner laws, take independent standard real Gaussian raw off-diagonal entries in both colors, independent standard Gaussian raw diagonals in \(B\), and independent raw diagonals of \(A\) with law
\[
 \tfrac12\mathcal N(0,1)+\tfrac14\delta_0+\tfrac18(\delta_1+\delta_{-1}).
\]
Every raw law is centered and has finite fourth moment.
The off-diagonal variances equal one and the diagonal variance of \(A\) is \(3/4\).
Normalize all matrices by \(N^{-1/2}\) and condition on every upper-triangular coordinate of both matrices except the last diagonal entry of \(A\).
The prescribed exterior consists of the normalized coordinates of \(SR,R\) in these positions.
Every neighborhood of this exterior has positive probability at the given \(N\), since each of its independent coordinate laws has a Gaussian component.
The remaining raw diagonal entry still has atoms of mass \(1/4\) at zero and \(1/8\) at one.

For each sufficiently large \(N\), uniform continuity of the determinant over the compact disk and a bounded neighborhood of this exterior gives a positive-probability exterior neighborhood on which the two atom choices retain a uniform positive gap in their normalized log potentials.
Explicitly, fix \(q<q_1<1\).
For the zero choice take the neighborhood small enough to preserve the upper bound \(2^N q_1^N\), and for the one choice preserve the lower bound \(2^N/(2\sqrt N)\).
Thus the two resulting normalized log potentials integrated over \(\Omega\) differ by at least \(c_\Omega>0\), independently of \(N\).
Finite eigenvalues have area zero and their logarithmic singularities are locally integrable.
This gives a fixed conditional oscillation of the disk integral on those exteriors using a single independent raw coordinate.

The exterior probabilities in this last argument may be summably small.
Indeed the neighborhoods can be chosen inside \(|B_{1N}|>1/2\), since \(R_{1N}=1\), and the fourth moment of that single labeled raw entry gives an upper bound \(16\mathbb E|\sqrt{N} B_{1N}|^4/N^2\).
The conditional oscillation tests estimates required to hold uniformly over the exterior, while the frequency of terminal losses after averaging over actual Wigner exteriors remains unresolved.

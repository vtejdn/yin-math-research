---
author: Yin
---

# Repairing a Wigner pencil while preserving every diagonal entry

On 18 November 2026 Yin's research agents examined how to use a [product-law tube estimate](../claims/Yin_C_F0186_v43.md#tube) for [F0012](../tasks/Yin_T_F0012_v3.md#contract), [F0013](../tasks/Yin_T_F0013_v1.md#contract) and [F0014](../tasks/Yin_T_F0014_v1.md#contract) when the independent diagonal laws may even be point masses.
The [unrestricted kernel repair](../claims/Yin_C_F0186_v38.md#argument) perturbs the realized diagonals in a real symmetric or complex Hermitian color.
The calculation here retains a fixed diagonal on a geometrically specified part of the small-singular-value event.

<a id="repair"></a>
## A correction annihilating all physical components

Fix a square affine pencil \(L\) of coefficient size \(m\).
On \(\max_j\|W_j\|\le\varepsilon^{-\theta}\), suppose a complex unit vector \(v=(v_1,\ldots,v_m)\) satisfies \(\|L(W)v\|\le\varepsilon\).
Write \(U\) for a real isometry onto the span of the real and imaginary parts of its physical components \(v_i\), and put \(P=UU^{\mathsf T}\), \(Q=I-P\).
The [structured repair](../claims/Yin_C_F0186_v38.md#argument) gives perturbations \(\Delta_j\) of total Hilbert–Schmidt norm at most \(C\varepsilon^d\) and a nonzero exact kernel vector whose physical components are in the complexification of \(\operatorname{ran}U\).
Here \(d,\theta>0\) are fixed by the pencil and the allowed real symmetric and Hermitian colors.

Suppose
\[
 \max_i P_{ii}\le \tfrac12-\delta,\qquad 0<\delta\le\tfrac12 .
 \tag{1}
\]
Let \(H_{ij}=Q_{ij}^2\).
For \(p_i=P_{ii}\), its diagonal is \((1-p_i)^2\) and its off-diagonal row sum is \(p_i(1-p_i)\) since \(Q^2=Q\).
The diagonal exceeds that sum by \((1-p_i)(1-2p_i)\ge\delta\).
Thus \(H\) is real symmetric with eigenvalues at least \(\delta\), by the Gershgorin bound.
For each color put \(a_j=-H^{-1}\operatorname{diag}\Delta_j\), using the diagonal vector, which is real even for a Hermitian color.
The matrix \(K_j=Q\operatorname{diag}(a_j)Q\), now using the diagonal matrix, is real symmetric, annihilates \(\operatorname{ran}U\), and has diagonal vector \(Ha_j\).
Therefore \(\Delta_j+K_j\) preserves the original diagonal and the same corrected kernel vector.
Moreover
\[
 \|K_j\|_{\rm HS}\le\|a_j\|_2\le\delta^{-1}\|\Delta_j\|_{\rm HS}.
\]
The distance to a singular tuple with the actual prescribed diagonals is at most \(C(1+\delta^{-1})\varepsilon^d\) in Hilbert–Schmidt norm, with no physical dimension factor in this correction.

<a id="slice"></a>
## Conditional test in the independent upper entries

Keep arbitrary centered diagonal laws of finite second moment, and use upper-entry laws covered by the [one-block sublevel estimate](../claims/Yin_C_F0186_v43.md#one-block).
Condition on the diagonal variables and form the pencil determinant \(F\) in the raw upper-entry blocks only.
Fix a dimension and include the probability of an identically zero slice as an exception whenever it can occur.
On every other slice the constants in the product tube estimate are independent of the frozen diagonal values.
If the small-singular-value event has even one eligible vector \(v\) satisfying (1), the raw upper tuple lies within coordinate sup distance \(C\sqrt N(1+\delta^{-1})\varepsilon^d\) of the zero set of that same slice on the norm guard.
Applying the tube estimate first on the whole conditional product law, then integrating, gives an upper bound
\[
 C N^2\big[\sqrt N(1+\delta^{-1})\varepsilon^d\big]^p
   + C N\varepsilon^{2\theta}
\]
for the probability of a small least singular value with such a vector on nonzero slices, when the first term is sufficiently small.
Here \(p>0\) comes from the one-block estimates.
The norm exception is estimated on the original law by the expected squared Hilbert–Schmidt norms.
In particular \(\delta=N^{-a}\) with fixed \(a>0\) is sufficient for polynomial floors of arbitrarily high confidence on this portion of the event.

For the [ordinary cyclic determinant](../claims/Yin_C_F0359_v2.md#statement), each frozen diagonal and \(N\) gives a monic polynomial in the spectral parameter when all upper entries are set to zero.
An identically zero slice in the upper variables forces that one polynomial to vanish at the prescribed parameter.
Fubini and countability of the dimensions therefore give almost surely nonzero slices in every dimension for Lebesgue-almost every prescribed spectral parameter.
For the scalar word-chain the same conclusion follows from \(\det(zI-P(W))\) at zero upper entries and its [Schur identity](../ledger/Yin_L_F0061_v2.md#linearization-transfer).
These arguments may leave specific exceptional parameters in the determinant Tasks.
For the Brown limit, a remaining sufficient estimate is summability at almost every fixed parameter of the probability that a very small least singular value occurs and every approximate kernel vector at the chosen tolerance violates (1).
The almost-every-parameter [clipping and planar argument](Yin_L_F0070_v1.md#localization) then removes the cutoff.

<a id="obstruction"></a>
## A delocalized vector whose component span contains a coordinate axis

Take \(N\ge3\) and \(b=N^{-1/2}(1,\ldots,1)^{\mathsf T}\).
Define real symmetric zero-diagonal matrices \(X,Y\) by
\[
 X_{ij}=\frac{1}{N-1}\quad (i\ne j),\qquad
 Y_{1j}=Y_{j1}=\frac1{N-1}\quad(j>1),\qquad
 Y_{ij}=-\frac1{(N-1)(N-2)}\quad(i,j>1,\ i\ne j).
\]
Then \(Xb=b\), \(X=-I/(N-1)\) on \(b^\perp\), \(Yb=N^{-1/2}e_1\), and both matrices have operator norm at most one by their absolute row sums.
The fixed two-channel pencil
\[
 L(X,Y)=\begin{pmatrix}I-X&0\\-Y&I\end{pmatrix}
\]
has a simple kernel spanned by \(v=(b,N^{-1/2}e_1)\) and has an invertible evaluation at the zero tuple with these same diagonals.
After normalizing \(v\), every physical site has total coordinate mass at most \(2/N\), whereas its component span contains \(e_1\) exactly.

In fact for every complex unit vector \((x,y)\) with \(\|L(X,Y)(x,y)\|\le\varepsilon\), one has \(x=cb+O_{\ell^2}(\varepsilon)\) and \(y=cN^{-1/2}e_1+O_{\ell^2}(2\varepsilon)\).
These follow from the spectral gap of \(I-X\) on \(b^\perp\) and \(\|Y\|\le1\).
For \(\varepsilon=o(N^{-1/2})\), normalization gives \(|c|\ge1/2\) for all large \(N\).
Rotating the common phase makes \(c>0\) and preserves the real span of all real and imaginary components.
Approximating \(e_1\) by \(\sqrt N\,\operatorname{Re}(y)/c\) in that span bounds its distance by \(4\sqrt N\varepsilon\).
Hence its first diagonal leverage satisfies \(P_{11}\ge1-16N\varepsilon^2\), even when the approximate vector may be selected after seeing the tuple.
This deterministic example prevents deducing (1) from small physical-site masses and bounded input norms alone.
It gives no probability estimate under a Wigner law.

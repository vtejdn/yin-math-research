---
author: Yin
---

# A quantile-grid bound for algebraic tubes under product laws

On 18 November 2026 a research delegate for Yin investigated the terminal logarithm in [F0014](../tasks/Yin_T_F0014_v1.md#contract), including the prescribed shift \(P(0)\).
The calculation gives a coefficient-independent tube estimate in terms of the concentration functions of independent real coordinates.
It provides a geometric alternative to the [Gaussian translation argument](../claims/Yin_C_F0186_v38.md#argument).

<a id="tube"></a>
## The tube probability

Let \(X=(X_1,\ldots,X_k)\) have independent atomless real coordinates, with possibly different laws, and put \(q(r)=\max_j\sup_a\Pr\{a\le X_j\le a+r\}\).
Let \(F\) be a nonzero nonnegative real polynomial of degree at most \(D\ge1\) in these coordinates and \(Z=\{F=0\}\).
For every \(r>0\) the estimate is
\[
 \Pr\{\operatorname{dist}_\infty(X,Z)\le r\}
 \ \le\ \min\{1,32D k^2 q(r)\}. \tag{1}
\]
The empty zero set has an empty tube.
For a complex polynomial one can apply (1) to the squared modulus, with twice its degree.

For an integer \(K\ge1\), choose independent auxiliary offsets \(U_j\) uniform on \((0,1)\).
In coordinate \(j\) insert the \(K\) thresholds at quantiles \((h+U_j)/K\), \(0\le h<K\), using the left quantile inverse of its continuous distribution function \(G_j\).
For fixed offsets each open interval has marginal mass at most \(1/K\), including the two unbounded intervals, and their thresholds have zero marginal mass.
Independence gives probability at most \(K^{-k}\) to each open box.
For two fixed numbers \(x_j,y_j\), a random threshold falls between them with probability at most \(K|G_j(x_j)-G_j(y_j)|\).
Indeed the expected number in the interval is its mass times \(K\), since the rank grid has mean counting measure \(K\,du\) on \((0,1)\).
The thresholds coincide with a fixed endpoint with probability zero, including when the distribution function has flat intervals.
For each fixed \(x\) with \(\operatorname{dist}_\infty(x,Z)\le r\), choose a point \(y\in Z\) at distance at most \(r\), which exists by closedness in finite dimensions.
Conditionally on this fixed \(x,y\), the probability that they belong to the same open box is at least \(1-Kkq(r)\).
Only the event that the open box of \(x\) meets the fixed closed set \(Z\) is integrated over \(x\), so no random choice of its witness is needed.
That event is measurable since membership of countably many points of a fixed countable dense subset of \(Z\) detects intersection with an open box.

<a id="box-count"></a>
## Counting boxes intersected by a hypersurface

For every such grid the number of open boxes meeting \(Z\) is at most \((K+2D)^k-K^k\).
If any box meets \(Z\), it also contains a point where \(F>0\), since \(F\) vanishes on no open box.
There are finitely many boxes and each is convex, so all boxes meeting \(Z\) meet the level \(M=\{F=\delta\}\) for all sufficiently small \(\delta>0\).
Choose such a \(\delta\) to be a regular value of \(F\) restricted to every positive-dimensional coordinate slice formed by the grid planes, including the ambient space.
There are finitely many slices, and Sard's theorem allows this choice while excluding all constant slice values and all values at grid vertices.
Thus the nonempty sliced levels are smooth, and each further coordinate plane cuts them transversely or misses them.

On a smooth manifold with finitely many components, removing a transverse closed level hypersurface increases the component count by at most the number of its components.
Within each original component the adjacency graph of complementary regions is connected, as paths between regions can be taken transverse to the cut.
Each connected component of the cut contributes at most one edge because its two local sides extend continuously along it, distinguished by the sign of the cutting coordinate.
This also applies on the open manifold remaining after earlier planes have been removed.
Adding grid planes successively therefore bounds the number of components of \(M\) off the planes by the sum of component counts for all slices of \(M\), including \(M\) itself.
In the induction, the cut term for the last plane uses only earlier planes restricted to it, so each subset of planes occurs once.
Two different planes fixing the same coordinate have empty intersection.
There are at most \(\binom{k}{j}K^j\) slices of codimension \(j\), and every vertex misses \(M\).
On a slice of dimension \(l=k-j\ge1\), Milnor's bound gives at most \(D(2D-1)^{l-1}\le(2D)^l\) components, including for noncompact affine levels. [Milnor, Theorem 2, p. 275](https://doi.org/10.1090/S0002-9939-1964-0161339-9)
Each component of the complement of the planes in \(M\) belongs to one open box.
Summing the slice bounds for \(0\le j\le k-1\) gives the claimed count.

Take \(K=\lfloor(2kq(r))^{-1}\rfloor\) when \(8Dk^2q(r)\le1\).
Then \(K\ge(4kq(r))^{-1}\), and a point of the tube has probability at least \(1/2\) over the grids to lie in a box meeting \(Z\).
Integrating gives an upper bound \(2[(1+2D/K)^k-1]\) for the tube probability.
Using \(2Dk/K\le8Dk^2q(r)\le1\) and \(e^s-1\le2s\) on this interval gives (1).
For larger \(q(r)\) the probability bound by one suffices.

<a id="wigner"></a>
## Wigner pencil application

Take the finite-variance model of [F0013](../tasks/Yin_T_F0013_v1.md#contract) with real upper entries or with independent real and imaginary parts in a planar upper entry.
Assume every scalar raw coordinate including each diagonal satisfies \(q(r)\le M r^\alpha\) for \(0<r\le1\) with fixed \(M,\alpha>0\).
A centered and rescaled middle-thirds Cantor law is an example with \(\alpha=\log 2/\log 3\), since an interval with \(3^{-(n+1)}<r\le3^{-n}\) meets at most two level-\(n\) Cantor intervals, each of mass \(2^{-n}\).
This law is singular and atomless.

On each dimension admitting a deterministic invertible evaluation, \(F=|\det L(W)|^2\) is a nonzero polynomial of degree at most \(2mN\) on \(k=O(N^2)\) independent scalar raw coordinates.
Constant nonzero determinants give an empty zero set.
The [deterministic structured repair](../claims/Yin_C_F0186_v38.md#argument) places the event \(s_{\min}(L(W))\le\varepsilon,\ \max_j\|W_j\|\le\varepsilon^{-\theta}\) within Hilbert–Schmidt distance \(C\varepsilon^\eta\) of a singular mixed tuple for fixed \(\theta,\eta>0\), or shows that the guarded event is empty.
Its raw-coordinate distance in the sup norm is at most \(C\sqrt N\,\varepsilon^\eta\).
By the second moments and Markov's inequality the norm exception has probability at most \(CN\varepsilon^{2\theta}\).
For \(C\sqrt N\,\varepsilon^\eta\le1\), (1) gives the total bound
\[
 CN\varepsilon^{2\theta}
   + C N^{5+\alpha/2}\varepsilon^{\alpha\eta}.
\]
Taking a sufficiently large fixed power \(\varepsilon=N^{-B}\) therefore gives a summable least-value failure bound.
The [finite-variance clipped logarithm](../claims/Yin_C_F0186_v40.md#determinant) then supplies the ordinary logarithm on good dimensions, and the fixed witness parity and scalar linearization apply even at \(z=P(0)\). [Good dimensions and the scalar reduction](../claims/Yin_C_F0186_v40.md#scalar)
For each fixed \(z\ne P(0)\) every dimension is good, giving the almost-sure Brown limit by the [pathwise planar argument](../claims/Yin_C_F0186_v38.md#polynomial-consequences).
The grid argument requires independent scalar coordinates, and the stated pencil application also requires the concentration bound for all coordinates in the full space of the deterministic repair.
Correlated planar coordinates, deterministic diagonals and Bernoulli laws remain outside this calculation.

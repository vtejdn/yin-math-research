---
author: Yin
---

# An actual Gaussian pair with a positive spectral partition cost on every small endpoint

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

There is a bounded normal pair \((Z,T)\), with \(T\) selfadjoint, satisfying both the full actual starred conjugate-variable condition and the strong bounded-vector domain condition of [F0011](../tasks/Yin_T_F0011_v1.md#contract).
Let \(\mu\) be the marginal of \(Z\), \(\zeta=-i[Z^*,\xi_Z]\) its real liberation vacuum and \(\nu\) the left-right marginal spectral measure of \(\zeta\).
There is a compact set \(K_0\) of \(\mu\)-mass \(1/2\) and an absolute \(c>0\) such that for every Borel \(F\subset K_0\) of positive mass \(t\) and every countable Borel partition \(F=\bigsqcup_i F_i\) modulo \(\mu\), omitting zero masses \(t_i=\mu(F_i)\),
\[
             \sum_i\frac{\nu(F_i^2)}{t_i^2}
                \ \ge\ c\sum_i t_i^{3/4}
                \ \ge\ c\,t^{3/4}.                                      \tag{1}
\]
In fact the left side is at least \(c\,t/(\sup_i t_i)^{1/4}\).
Although \(\nu\) has bounded product density and finite inverse-gap energy, the infimum in (1) over partitions cannot be bounded by \(C\lambda(F)\) for every \(F\subset K_0\) with any one finite positive measure \(\lambda\) and finite \(C\).
It follows that the local ball-mass hypothesis of [the subdivision criterion](Yin_C_F0332_v1.md#subdivision-by-cubes) fails for every such control measure.
There is also no dominating Hilbert-valued map with \(\mathcal H^2\)-null essential range as in [the feature criterion](Yin_C_F0337_v1.md#the-remaining-disks-under-feature-domination), even without its secant-energy requirement.

Write \(T(B)=\int\min(1,r^2/|a-v|^2)d\mu(v)\) for \(B=B(a,r)\).
All sufficiently small disks meeting \(K_0\) satisfy \(T(B)\le C_0\mu(3B)\) with one absolute constant \(C_0\).
Thus their thresholds lie on the side \(T(B)\le K\mu(3B)\) of the [disk reduction](Yin_C_F0337_v1.md#disks-of-small-local-mass) once its permitted absolute \(K\) is taken at least \(C_0\).
The normalized marginal on \(K_0\) alone has finite [averaged squared density \(W\)](Yin_C_F0297_v1.md#statement), whereas the full example has \(W=\infty\).
Its full marginal curvature kernel also has unbounded negative Rayleigh quotients on bounded Hilbert unit vectors.
The actual original slices have finite cost and the canonical closures and their adjoints act on every bounded vector.
Inequality (1) concerns the separate endpoint cost before angular integration.

## Argument

### Marginal geometry

Let \(C\subset[0,1]\) be the Cantor set obtained by taking the leftmost and rightmost quarters at every step.
Give each level \(n\) interval mass \(2^{-n}\), and call the resulting probability \(\tau_C\).
Let \(K_0=[0,1]+iC\) with probability \(\mu_0=dx\otimes\tau_C\).
A ball of radius \(4^{-n}\) centered on \(C\) contains a whole level \(n\) interval up to endpoints and meets a bounded number of such intervals, by their separation.
Interpolation between successive radii gives one-dimensional ball mass comparable to \(r^{1/2}\) on \(C\) for \(0<r\le1\).
Intersecting a disk with the product, using inscribed and circumscribed coordinate squares, now gives
\[
           c_1 r^{3/2}\le\mu_0(B(z,r))\le C_1r^{3/2}
              \qquad(z\in K_0,\ 0<r\le1).
\]
The upper bound also holds at arbitrary centers after enlarging about a point of intersection.
In particular \(W(\mu_0)<\infty\) by summing \(O(r_j)\) at small dyadic radii.
The scalar normal vacuum exists by the [geometric criterion](Yin_C_F0255_v1.md#statement).
Indeed the maximal linear density is uniformly bounded, and for fixed endpoint \(z\) the integral of squared curvature over triples with maximal pair distance comparable to \(r\) is \(O(r^{-2}r^3)\), summable over dyadic scales.

For the other half of \(\mu\) take \(\sigma'\), the compact probability on separated pairs of horizontal segments constructed in [the negative curvature example](Yin_C_F0331_v1.md#a-disjoint-component-that-excludes-positive-diagonal-decompositions).
Its support is at a fixed positive distance from \(K_0\).
Set \(\mu=(\mu_0+\sigma')/2\).
Both component scalar energies are finite, and the maximal linear density at a point contributed by the other component is uniformly bounded.
On any mixed triangle the curvature is at most twice the reciprocal of the fixed separation.
Hence \(\mu\) has an actual scalar vacuum.
The density on each nondegenerate straight segment of \(\sigma'\) has a positive constant value on its interior, so every point there makes infinitely many summands of the defining \(W(\mu)\) bounded below by a positive constant.
This proves \(W(\mu)=\infty\).
The cited opposite-sign tests on the two segments in a cluster have negative curvature Rayleigh quotients tending to \(-\infty\).
In the mixed marginal their original quotients acquire a fixed positive factor after trace normalization, while off-component third points add a uniformly bounded kernel on their supports by the fixed gap.
The negative divergence persists.

If \(B=B(a,r)\) meets \(K_0\) and \(r\) is sufficiently small, \(3B\) contains a disk of radius \(r\) centered on \(K_0\), hence \(\mu(3B)\ge c_2 r^{3/2}\).
Annuli of radius \(2^jr\) about \(a\) bound the \(\mu_0\) part of \(T(B)\) by \(C r^{3/2}\sum_{j\ge0}2^{-j/2}\), using its ball upper bound also for large radii by increasing the constant.
The separated component contributes \(O(r^2)\).
This proves the asserted disk estimate with a finite absolute \(C_0\).

### A Gaussian pair and its actual spectral measure

Write \(x_z=\operatorname{Re}z\) on \(K_0\), and put \(\alpha=3/8\).
On \(\mathbb T=\mathbb R/\mathbb Z\) take the continuous even function
\[
             g(x)=\sum_{n\ge0}2^{-\alpha n}\cos(2\pi 2^n x).
\]
For \(z,w\in K_0\) set \(G(z,w)=\exp(g(x_z-x_w))\), and set \(G=1\) if either endpoint is outside \(K_0\).
This scalar symmetric measurable amplitude and its inverse are bounded.
Take \(Z\) to be the coordinate in \(L^\infty(\mu)\) and \(T\) the one-color selfadjoint Gaussian field with this amplitude over \(Z\), formed using one independent free standard semicircular as in the [Gaussian matrix theorem](Yin_C_F0209_v1.md#statement).
Its row bound holds by boundedness of \(G\).
Define
\[
 H(z,v)=\int\left|G(z,w)^{-1}G(w,v)-G(z,w)G(w,v)^{-1}\right|^2d\mu(w).
\]
For \(z,v\in K_0\), the other half of the middle-variable law contributes zero, and symmetry and the uniform horizontal coordinate under \(\mu_0\) give
\[
 H(z,v)=2\int_0^1\sinh^2\!\big(g(x_z-y)-g(x_v-y)\big)\,dy
       \asymp \operatorname{dist}_{\mathbb T}(x_z,x_v)^{3/4}.            \tag{2}
\]
To check both inequalities, \(|\sinh b|\asymp|b|\) on the bounded range of differences.
Parseval gives \(2\sum_{n\ge0}2^{-2\alpha n}\sin^2(\pi2^n d)\) for the integral of the squared differences, where \(d=\operatorname{dist}_{\mathbb T}(x_z,x_v)\).
For \(0<d\le1/2\) choose \(n\ge0\) with \(2^n d\in[1/4,1/2]\) for the lower bound.
For the upper bound split at this scale and sum the geometric estimates with \(\sin^2(\pi 2^j d)\le\min(1,\pi^2 2^{2j}d^2)\).
At \(d=0\) both sides vanish.

On \(K_0^2\), \(H(z,v)/|z-v|^2\le C|z-v|^{-5/4}\).
Its integral is finite by the \(r^{3/2}\) ball upper bound, since the dyadic contributions are \(O(r^{1/4})\).
The ratio is bounded across components by their separation, and \(H=0\) when both endpoints are in the other component.
The two tests of the Gaussian theorem are therefore finite, including the inverse-amplitude test for \(T\).
This proves full actual conjugacy and both strong domains in the generated algebra.
At \(Z\) the vacuum is its scalar vacuum plus the second Gaussian chaos with the two-edge coefficient of formula (2) of that theorem.
Multiplying that coefficient by \(-i(\bar z-\bar v)\) gives the liberation vacuum path coefficient, since its scalar part commutes with \(Z^*\). [Liberation commutator](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core)
The joint spectral actions multiply the two path endpoints, so \(\nu=H\mu^2\) on the whole square, as claimed.
All spectral statements use the generated algebra and its actual trace.

### The obstruction to subdivision

Fix \(E\subset K_0\) of mass \(s>0\).
For each \(z\in E\), the part of \(E\) within circular horizontal distance \(s/4\) from \(x_z\) has mass at most \(s/2\), since even the probability \(\mu_0\) gives the corresponding horizontal interval mass \(s/2\).
Consequently at least half the \(E^2\) product mass has horizontal separation at least \(s/4\).
Equation (2) gives \(\nu(E^2)/s^2\ge c s^{3/4}\).
Summing this inequality over partition cells and using \(\sum_i t_i=t\) proves (1), including the fine-partition estimate.

Partition \(K_0\) into \(n\) horizontal-parameter sets of equal mass \(1/(2n)\).
The sum of their individual lower bounds for the optimal subdivision costs is at least \(c' n^{1/4}\).
A fixed finite control measure would bound every such sum by \(C\lambda(K_0)\).
In particular this excludes the ball-mass hypothesis, by the partition consequence of the subdivision criterion for every Borel set.
If a Hilbert-valued map with \(\mathcal H^2\)-null essential range dominated \(H\) as in the feature criterion, cover its range on a conull set by countably many Borel sets with sum of squared diameters arbitrarily small.
Partition \(K_0\) by their successive disjoint preimages.
On each cell the square-mass quotient of \(\nu\) is bounded by the square of the corresponding diameter.
This contradicts (1) for \(F=K_0\).
The same argument applies to any positive-mass subset of \(K_0\), including inside arbitrarily small disks meeting it in positive mass.
The established Gaussian slice theorem controls the actual signed behavior on this example.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:10 |
| status | open |
| reason | Fix the quantitative actual spectral obstruction to subdivision and null-range domination on disks with controlled mass, including the separated marginal with infinite averaged squared density. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Positive subdivision costs, failure of finite control measures and null-range features, typical disk comparison and both actual strong domains. |
| argument | [Argument](#argument) | Cantor product scaling, separated segment pairs, lacunary Gaussian amplitude, exact spectral density and partition lower bound. |
| dependency | [Gaussian matrix theorem](Yin_C_F0209_v1.md#statement) | Scalar positive one-noise field, actual and strong equivalence, and the intrinsic two-edge vacuum coefficient. |
| dependency | [Normal liberation commutator](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Conversion of the second-chaos vacuum to the joint spectral measure of the liberation gradient. |
| dependency | [Marginal vacuum criterion](Yin_C_F0255_v1.md#statement) | Scalar actuality under the maximal linear density and squared Menger curvature integrals. |
| dependency | [Separated segments](Yin_C_F0331_v1.md#a-disjoint-component-that-excludes-positive-diagonal-decompositions) | Actual scalar law and divergent negative curvature Rayleigh quotients on its signed pair tests. |
| dependency | [Endpoint partition](Yin_C_F0332_v1.md#subdivision-by-cubes) | Local mass domination would control all optimal small-endpoint costs by a single finite measure. |
| dependency | [Feature partition](Yin_C_F0337_v1.md#the-remaining-disks-under-feature-domination) | Null essential range would yield zero endpoint cost. |
| dependency | [Disk classification](Yin_C_F0337_v1.md#disks-of-small-local-mass) | Mass threshold whose residual disks are realized by the product component. |
| dependency | [Averaged squared density](Yin_C_F0297_v1.md#statement) | Exact \(W\) tested on the product component and the full law. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:20 |
| status | proved |
| reason | R_F0343 checked the actual Gaussian construction, both coordinates, squared spectral density and failure of both forms of endpoint payment, including all eight declared dependencies. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Positive subdivision costs, failure of finite control measures and null-range features, typical disk comparison and both actual strong domains. |
| argument | [Argument](#argument) | Cantor product scaling, separated segment pairs, lacunary Gaussian amplitude, exact spectral density and partition lower bound. |
| dependency | [Gaussian matrix theorem](Yin_C_F0209_v1.md#statement) | Scalar positive one-noise field, actual and strong equivalence, and the intrinsic two-edge vacuum coefficient. |
| dependency | [Normal liberation commutator](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Conversion of the second-chaos vacuum to the joint spectral measure of the liberation gradient. |
| dependency | [Marginal vacuum criterion](Yin_C_F0255_v1.md#statement) | Scalar actuality under the maximal linear density and squared Menger curvature integrals. |
| dependency | [Separated segments](Yin_C_F0331_v1.md#a-disjoint-component-that-excludes-positive-diagonal-decompositions) | Actual scalar law and divergent negative curvature Rayleigh quotients on its signed pair tests. |
| dependency | [Endpoint partition](Yin_C_F0332_v1.md#subdivision-by-cubes) | Local mass domination would control all optimal small-endpoint costs by a single finite measure. |
| dependency | [Feature partition](Yin_C_F0337_v1.md#the-remaining-disks-under-feature-domination) | Null essential range would yield zero endpoint cost. |
| dependency | [Disk classification](Yin_C_F0337_v1.md#disks-of-small-local-mass) | Mass threshold whose residual disks are realized by the product component. |
| dependency | [Averaged squared density](Yin_C_F0297_v1.md#statement) | Exact \(W\) tested on the product component and the full law. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0343_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

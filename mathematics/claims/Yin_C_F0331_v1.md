---
author: Yin
---

# Failure of optimized rectangular estimates at linear spectral decay

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Use the positive disk and angular representation of the squared curvature kernel and the analytic unitary tests in [the rectangle criterion](Yin_C_F0329_v1.md#statement).
For each \(\varepsilon>0\) there is an exchange-symmetric actual normal pair with exact product two-marginal traces and strong duals in the [semicircular neighborhood](Yin_C_F0324_v1.md#statement) of tolerance \(\varepsilon\).
Its liberation gradients have operator norm below \(\varepsilon\), and at both coordinates their spectral measures satisfy the stronger critical estimate
\[
     d\nu(z,w)\le\varepsilon^2\min(1,|z-w|)\,d\mu(z)d\mu(w).             \tag{1}
\]
At either coordinate the integrated rectangular cost is infinite even when each pair of disjoint endpoint sets uses the smallest of three estimates:
the optimized signed bound (2) below, the absolute Hilbert-kernel bound of C_F0326, and the localized bounded-kernel estimate of C_F0297 with any admissible supporting square.
The curvature quadratic form on bounded marginal Hilbert unit vectors is unbounded below.
Hence the same marginal curvature kernel admits no positive diagonal-block decomposition modulo an \(L^2(\mu^2)\) remainder.
Both actual normalized slice costs stay bounded by an absolute constant.

Here is the optimization in the statement.
For disjoint positive-mass projections \(e,f\) of a marginal, write \(t=\tau(e), s=\tau(f)\), \(A=\nu(e^2), B=\nu(f^2)\), and \(C=\nu(e\times f)+\nu(f\times e)\), where a squared set denotes its Cartesian square.
For any \(R>0\) the lower bound for the signed form on \(e\otimes f+f\otimes e\) is the negative of
\[
 D_R=\frac{R A}{t}+\frac{B}{R s}
       +(\sqrt R\,t-s/\sqrt R)^2
       +\frac{R^2 A+R^{-2}B+C}{Rt+s/R}.                                 \tag{2}
\]
The optimized cost is \(\inf_{R>0}D_R\); the choice \(R=s/t\) recovers the centered estimate.
Thus the power condition \(O(r^{1+\alpha})\), \(\alpha>0\), in the Dini criterion cannot be replaced by \(O(r)\) to conclude that these integrated costs are finite.
The operator-domain implication at critical decay remains open for arbitrary pairs.

## Argument

### The uncentered square

For a bounded real marginal function \(k\) let \(b=k\otimes k\), \(E_b=(\mathrm{id}\otimes\tau)iI_b\gamma\), and \(\eta_b=k\zeta k\), with \(\zeta=(i\gamma)^*(1\otimes1)\).
Here \(F_b(u)=\operatorname{Re}\langle u,-iE_bu\rangle\).
In the [finite-kernel energy identities](Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) the row is \((\tau k)k\) and \(b\circ b=\|k\|_2^2b\).
Thus for any stated analytic test \(u\),
\[
 \|k\|_2^2 F_b(u)
 = \|\eta_b\|_2^2-\|E_bu-u\eta_b\|_2^2
                  +2(\tau k)\operatorname{Im}\tau(k u^* E_bu).
\]
The same formulas apply on adjoining bounded Borel marginal functions, since their liberation derivative is the inner difference on that marginal.
As \(\tau(k\eta_b)\) is real, completing the square against \(i(\tau k)u k\) bounds the right side by \(\|\eta_b\|_2^2+(\tau k)^2\|k\|_2^2\).
Apply this upper bound with \(k=\sqrt R\,e-f/\sqrt R\) and subtract it from the two [diagonal projection lower bounds](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block), with coefficients \(R,R^{-1}\).
Expansion of the four disjoint spectral rectangles of \(\|k\zeta k\|_2^2\) gives (2).
In particular
\[
       \inf_{R>0}D_R\ \ge\
        2t\{\sqrt{s^2+B/s}-s\},                                         \tag{3}
\]
by retaining \(B/(Rs)+(\sqrt R\,t-s/\sqrt R)^2\) alone.

### A critical phase on a dense collection of horizontal segments

We first construct a planar probability and a measure-preserving parametrization by \(x\in[0,1)\).
Write \(r_j=2^{-2m_j}\), \(d_j=\sqrt{r_j}\), \(m_1=20,\ m_{j+1}=4m_j\), and \(p_j=10^{-5}/(j+1)^2\), \(j\ge1\).
In \([1/4,3/4]\) use grid cells of length \(r_j\).
Pair the centers from the first half of each consecutive interval of length \(2d_j\) with their translates by \(d_j\) in its second half.
The grids are aligned since \(d_j/r_j\) and \(1/(8d_j)\) are integers.
Discard any pair for which either center is within \(2r_j\) of a previously removed interval.
At each retained pair \(x,x+d_j\), remove the two open intervals of length \(p_jr_j/2\) about these centers.
Send them, linearly, to two horizontal segments of length \(r_j/100\) centered at \(x\pm r_j/20+i r_j\), respectively.
The remaining parameter set \(K\subset[0,1)\) stays on the real line by the identity map.
All assignments are disjoint up to their null endpoints.

There are at least \(c/r_j\) retained pairs at each level, with an absolute \(c>0\).
Indeed the old intervals have total length at most \(\sum_k p_k\), and their number is at most \(\sum_{k<j}r_k^{-1}\).
The number of grid centers discarded, multiplied by \(r_j\), is at most a fixed constant times \(\sum_k p_k+r_j\sum_{k<j}r_k^{-1}\), also when both members of a pair are discarded.
With these parameters this is smaller than \(1/16\), whereas the original number of pairs is \(1/(4r_j)\).
For every retained first center \(x\), the interval \([x-r_j/100,x+r_j/100]\) retains length at least \(r_j/100\) of \(K\).
No older interval meets it, the one current hole costs at most \(p_jr_j\), and later holes within it cost at most \(\sum_{k>j}(2+r_j/r_k)p_kr_k\).
Denote the resulting probability by \(\sigma\) and the inverse interval parameter by \(h_0(z)\).
Thus the circle phase on this model could be written \(e^{2\pi i h_0(z)}\).
In particular, inverse parameters on the two segments of a pair differ by \(d_j+O(p_jr_j)\).

On level \(j\) the marginal has a density on the horizontal line of height \(r_j\) bounded by \(50p_j\), with all segments disjoint on that line.
On height zero its density is at most one.
Thus \(\sigma(B(z,R))\le C R\).
Its actual scalar vacuum also exists.
For detail, write these horizontal densities as \(w_i\) including the one on the real line, with \(\sum_i\|w_i\|_\infty<\infty\) and all horizontal supports in \([0,1]\).
The scalar Cauchy transform regularized by \(\bar z/(|z|^2+\delta^2)\), evaluated from layer \(j\) to layer \(i\), is convolution on the line with \((x-i y)/(x^2+c^2)\), where \(y\) is the difference of the heights and \(c^2=y^2+\delta^2\).
Its Lebesgue \(L^2\) operator norm is at most \(2\pi\) uniformly: the transforms of \(c/(x^2+c^2)\) and \(x/(x^2+c^2)\) have moduli at most \(\pi\), from the Fourier pair of \(e^{-c|s|}\) and the Poisson kernel and its conjugate, and \(|y|\le c\).
Consequently the sum on each output line has Lebesgue Hilbert norm at most \(2\pi\sum_j\|w_j\|_{L^2(dx)}<\infty\).
Integrating its square against the output densities gives a uniform bound on \(L^2(\sigma)\).
On a marginal starred polynomial the divided difference \((f(z)-f(w))/(z-w)\) is bounded off the diagonal and its regularizations converge in the double trace.
Antisymmetry expresses that trace pairing as twice the pairing with the conjugated regularized Cauchy transform.
A weak Hilbert limit thus supplies the actual vacuum of the represented divided-difference derivation.
The law is diffuse and null representatives have zero divided difference in the product law.

On a single segment the inverse parameter is Lipschitz with constant at most \(50p_j\); on \(K\) it is the identity.
Between different components the distance from a point at height \(r_j\) to a point on the other component is at least \(c r_j\), including the other segment of the same pair.
Moreover \(|h_0(z)-\operatorname{Re}z|\le 2\sqrt{r_j}\) there.
These facts give \(|h_0(z)-h_0(w)|^2\le C|z-w|\) on the full marginal.
They give more than this pointwise bound for its secant energy.
For \(z\) on layer \(j\), the integral over other components of \(|z-w|^{-2}\) is at most \(C/r_j\) by annular summation of the ball bound.
Decomposing \(h_0\) into the horizontal coordinate and its error, each rare layer contributes at most its mass times a constant from its own error on different components, and the errors at the second endpoints are bounded by symmetry.
The same-component Lipschitz bound controls the remaining pairs.
Hence \(\iint |h_0(z)-h_0(w)|^2 |z-w|^{-2}d\sigma^2<\infty\).

### A disjoint component that excludes positive diagonal decompositions

Independently put paired horizontal segments at horizontal centers \(3+2^{-n}\), at heights zero and \(R_n=2^{-9n-8}\), of common length \(R_n/100\), \(n\ge1\).
Give the \(n\)th pair total mass \(q_n=255\cdot2^{-8n}\), equally divided with uniform arclength.
This defines a probability \(\sigma'\).
Use consecutive intervals of lengths \(q_n\) in \([0,1)\), in index order, and their successive halves to parametrize these segments linearly.
The inverse parameter on each segment has Lipschitz norm at most \(Cq_n/R_n\), with oscillation at most \(q_n\) within its pair.
It is globally \(1/2\)-Hölder: within a segment use \(\min(q_n,Cq_n |z-w|/R_n)^2\le C q_n^2 |z-w|/R_n\); across its two segments use their gap; between pairs \(n<k\) the parameter difference is at most \(\sum_{l\ge n}q_l\), while the spatial distance is at least \(c2^{-n}\).
Its inverse secant energy is finite, since the within-pair contribution is at most \(C\sum q_n^4/R_n^2\) and the distinct pairs have uniformly bounded inverse-square potentials by their gaps and masses.

The scalar vacuum criterion also holds for \(\sigma'\).
The external inverse-square potentials of each pair are uniformly bounded, its own contribution to maximal linear density is at most \(Cq_n/R_n\), and \(\sum q_n^3/R_n^2<\infty\).
For triples all in one pair the curvature either vanishes on one line or is at most \(2/R_n\).
For triples involving different pairs it is bounded by twice the inverse separation for any differing pair of labels, giving a finite integral by the same uniform external potentials.
Apply the [geometric scalar criterion](Yin_C_F0255_v1.md#statement).

The reason for choosing two straight segments is the sign of the internal curvature quadratic form.
On the template of separation one, length \(1/100\), endpoints on the same line have normalized kernel at most two, since only the half mass on the other line contributes and squared curvature is at most four.
For endpoints on different lines almost every third point makes a triangle with two vertices on one line and one on the other.
Its squared curvature is \(4/[(1+d_1^2)(1+d_2^2)]\) where \(|d_1|,|d_2|\le1/100\) are the two horizontal displacements from the opposite vertex.
The normalized kernel on the cross rectangle is therefore at least \(4/(1+10^{-4})^2\).
The test equal to \(+1,-1\) on the two lines has strictly negative curvature quadratic form.
Internal rescaling gives a Rayleigh quotient at most \(-c q_n^2/R_n^2\) on the corresponding normalized signed tests.
The kernel contribution on that pair from external third points is uniformly bounded by the external inverse-square potentials.
Thus the quadratic form is unbounded below on bounded Hilbert unit vectors.
This uses the separated-cluster mechanism of [the earlier indefinite template](Yin_C_F0297_v1.md#statement) with a one-dimensional parametrized support.

Take the equally weighted mixture of \(\sigma,\sigma'\), with parametrization by the first and second halves of the unit interval.
The fixed separation preserves scalar actuality by the divided-difference formula on the two squares and a bounded cross kernel.
It preserves finite secant energy and the \(1/2\)-Hölder bound for the combined interval parameter.
The negative Rayleigh quotients persist, since the extra third points are at a fixed distance.

### Inserting the construction into a semicircular neighborhood

Let \(G_{\rm sc}\) and \(Q_{\rm sc}\) denote the continuous cumulative distribution function and quantile of standard semicircular probability.
Choose small \(d>0\), then small \(p,q>0\) with \(p+q<1/2\).
On the angular parameter \(\theta\in[0,1]\) define the continuous periodic reference
\[
  G(\theta)=
   \begin{cases}
      Q_{\rm sc}(\theta/(1-p)),&0\le\theta\le1-p,\\
      Q_{\rm sc}((1-\theta)/p),&1-p\le\theta\le1 .
   \end{cases}
\]
Its Haar pushforward is exactly standard semicircular.
Define the generating map \(F\) on the circle as follows.
On \(0\le\theta<1-p-q\) put \(F=Q_{\rm sc}(\theta/(1-p-q))\).
On \(1-p-q\le\theta<1-p\) map the interval linearly in its parameter to the preceding combined geometry, translated and scaled by \(z\mapsto 2+3d+dz\).
On \(1-p\le\theta<1\) put \(F=G(\theta)+i d\).
Up to null endpoints these images are disjoint and the map has a Borel inverse \(h\), valued on the unit circle.
Write \(\mu=F_*m\) for its trace law.
The two nonexceptional inverse parameters are Lipschitz functions of the horizontal variable by boundedness of the semicircular density.
On the exceptional part the preceding Hölder bound and finite secant energy carry over under scaling and the parametrization of a short angular interval.
The three images have positive separations for fixed \(d\), so \(h\) satisfies a global \(1/2\)-Hölder bound and has finite squared secant energy.
All constants here may depend on the chosen geometry.
The negative Rayleigh quotients on the scaled straight pairs still tend to minus infinity since fixed positive masses and scale factors preserve divergence and external third points contribute a bounded kernel there.
If \(g=\sum_k\lambda_k1_{B_k}\otimes1_{B_k}+b\) with \(\lambda_k\ge0,\ b\in L^2(\mu^2)\), each finite positive sum has nonnegative quadratic form.
The partial sums are bounded by \(g+|b|\) in \(L^1\), so their pairings against any fixed bounded test pass to the limit.
This would bound every such unit-vector quotient below by \(-\|b\|_2\), a contradiction.

The scalar vacuum \(\xi_\mu\) can be made arbitrarily close to the coordinate in \(L^2(\mu)\).
The diagonal contribution on each of the three components is its mass times its own normalized vacuum, by the divided-difference pairing.
The main one is the coordinate times \(1-p-q\); the return component has scalar vacuum equal to its real coordinate.
The scaled exceptional component has fixed finite scalar vacuum norm divided by \(d\).
Their discrepancy from the coordinate has norm at most \(p+q+C\sqrt p+C\sqrt q+Cq^{3/2}/d\) for \(d<1/10\).
The cross vacuum adds at most \(C\sqrt{p+q}/d\) since the off-component inverse-gap tensor has that Hilbert bound and its inner derivation has vacuum of norm at most twice the kernel norm. [Mixed-gap calculation](Yin_C_F0305_v1.md#the-distinguished-derivative-before-smoothing)
Also \(\|F-G\|_\infty\) can be made arbitrarily small by making \(d,q\) small: on the exceptional interval both images are close to 2 by continuity of the quantile, on the main part the two quantile arguments differ by at most \(q/(1-p)\), and on the return part the distance is \(d\).

Take \(X,U\) free Haar and choose \(V\in W^*(U)\) with smooth circle density \(1+2a\cos(2\phi)\), \(0<a<1/4\), by the monotone angle quantile.
As \(a\downarrow0\) this quantile converges uniformly to the identity, since its distribution functions do, with density bounded below by \(1/2\).
Thus \(\|V-U\|\to0\).
The pair \(X,X^*U\) is free Haar by Haar absorption, so \(G(X),G(X^*U)\) are free standard semicirculars.
For fixed \(p\), continuity of \(G\) on the circle gives \(\|G(X^*V)-G(X^*U)\|\to0\), for instance by uniform Laurent approximation.
The normal pair \(W_0=F(X), W_1=F(X^*V)\) is therefore arbitrarily close to this free pair in operator norm.

The [phase-coupling construction and graph transfer](Yin_C_F0329_v1.md#a-phase-coupling-that-distinguishes-the-two-arcs) apply here since \(\mu\) has its actual scalar vacuum and \(h\) has finite secant energy.
They give full actuality, exchange, exact two-marginal product trace and strong domains, with an absolute normalized cost bound by [the full phase estimate](Yin_C_F0320_v1.md#statement).
In particular \(H=\xi_V V^*-1\) is nonzero, \(\|H\|_\infty\le2a\), the liberation gradients have norm at most \(4a\), and
\[
       d\nu=\|H\|_2^2|h(z)-h(w)|^2\,d\mu^2 .
\]
This proves (1) by fixing the geometry first and then making \(a\) sufficiently small.
The squared difference between the joint and marginal vacua is \(\|H\|_2^2\) times the secant energy of \(h\), by [the exact phase-vacuum formula](Yin_C_F0265_v1.md#statement).
Hence the two actual vacua are also arbitrarily close in trace Hilbert norm to the same free semicirculars.

### Divergence of all three rectangle bounds

Work in the \(\sigma\) portion in its original spatial units.
The fixed translation and similarity scale multiply the parameter measure \(dA(\mathrm{center})\,dr/r^5\) by a fixed positive factor, and the marginal masses of this portion have one fixed positive multiplier.
They do not affect divergence.
For each retained first center \(x\), allow \(v\) in the part of \(K\) within \(r_j/100\) of \(x\), disk centers within \(r_j/50\) of \(x+i r_j/2\), and radii in \([1.4r_j,1.6r_j]\).
Use \(p_v(z)=\operatorname{Re}((z-v)/(\bar z-\bar v))\) and thresholds \(l\in[-1/2,-1/4]\), \(u\in[1/4,1/2]\) as in [the positive rectangle formula](Yin_C_F0329_v1.md#integrating-the-two-block-estimate).
For all sufficiently large \(j\), no external component or older layer enters these disks.
On the real bulk \(p_v=1\) almost everywhere, and on both elevated segments over \(x\) it is less than \(-0.9\), by their horizontal proximity compared with their height.
For the upper and lower level sets \(E,F_1\), respectively, the masses satisfy \(t\asymp r_j,\ s\asymp p_jr_j\), uniformly in all selected parameters, with constants allowed to depend on the fixed graft.
The lower bound for \(t\) follows from the surviving real bulk in the disk.
For the upper bound for \(s\), \(p_v<-1/4\) restricts the horizontal displacement from \(v\) to at most a constant times the height.
On each layer \(k\ge j\) only a bounded number of segments can meet this condition, hence their total mass is at most \(C\sum_{k\ge j}p_k r_k\le C' p_j r_j\).
The ball bound for \(\sigma\) supplies the upper estimate for \(t\).
In the final short angular parametrization the phases on the two selected segments still differ by at least a fixed positive constant times \(d_j\): their interval parameters differ by \(d_j+O(p_j r_j)\) and the rescaling of the angular interval is fixed and nonzero.
It follows that \(B=\nu(F_1^2)\ge c_a r_j(p_jr_j)^2\).

Since \(p_j\to0\), (3) is at least \(c'_a r_j^2\sqrt{p_j}\) for all sufficiently large \(j\).
The [absolute Hilbert-kernel bound](Yin_C_F0326_v1.md#statement) costs at least a constant times \(\sqrt{ts}\asymp r_j\sqrt{p_j}\).
The [localized bounded-kernel estimate](Yin_C_F0297_v1.md#statement) costs at least \(3(t+s)^2\) on a supporting square, since that square contains the two positive-mass levels modulo null sets and the kernel has supremum one.
Its own square-mass term is therefore at least \(c r_j^2\).
The minimum of all three numerical costs is at least \(c''_a r_j^2\sqrt{p_j}\).
The mass of \(v\), the available center area and the radial interval with its weight give a parameter measure at least \(c/r_j\) per first center, including the two fixed threshold intervals.
The center neighborhoods for different first centers are disjoint, and the radial windows for different \(j\) are disjoint.
Summing over at least \(c/r_j\) centers gives a lower bound \(c_a\sum_j\sqrt{p_j}=\infty\).
This argument produces no unbounded actual signed form or slice in the example.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T18:25 |
| status | open |
| reason | Fix the critical exchange-symmetric example, the optimized signed estimate, and simultaneous failure of three rectangle budgets and the positive diagonal decomposition. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual critical-decay pair near free semicirculars, strong domains and divergent estimates even after optimization. |
| argument | [Argument](#argument) | Rank-one square, shifted grid holes, scalar regularity, indefinite doublets, near-semicircular graft and nonsummable balanced family of disks and levels. |
| dependency | [Rectangle criterion and representation](Yin_C_F0329_v1.md#integrating-the-two-block-estimate) | Positive kernel integral, choice of disk/angular parameters and convergence of the matched forms. |
| dependency | [Phase realization](Yin_C_F0329_v1.md#a-phase-coupling-that-distinguishes-the-two-arcs) | Actual graph transfers, exact product trace and spectral density for the zero-mean free unitary product law. |
| dependency | [Finite kernel energy](Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) | Row, kernel-square and signed terms on analytic unitaries. |
| dependency | [Projection energy](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Lower bound on the two diagonal rectangles. |
| dependency | [Localized cost](Yin_C_F0297_v1.md#statement) | Local absolute estimate and the earlier use of indefinite curvature templates. |
| dependency | [Hilbert-kernel estimate](Yin_C_F0326_v1.md#statement) | The absolute cost and the positive-diagonal plus square-integrable remainder criterion. |
| dependency | [Marginal vacuum criterion](Yin_C_F0255_v1.md#statement) | Actuality of the separated double-segment scalar law. |
| dependency | [Mixed-gap calculation](Yin_C_F0305_v1.md#the-distinguished-derivative-before-smoothing) | Vacuum estimate across the separated pieces in the final graft. |
| dependency | [Phase norm identity](Yin_C_F0265_v1.md#statement) | Exact distinction between the joint and scalar vacua in the Borel phase model. |
| dependency | [Uniform phase estimate](Yin_C_F0320_v1.md#statement) | Absolute true slice-to-vacuum bound in both orientations. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T18:39 |
| status | proved |
| reason | Adopt the critical linear-decay construction and failure of the optimized and localized costs after independent review of the full proof. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual critical-decay pair near free semicirculars, strong domains and divergent estimates even after optimization. |
| argument | [Argument](#argument) | Rank-one square, shifted grid holes, scalar regularity, indefinite doublets, near-semicircular graft and nonsummable balanced family of disks and levels. |
| dependency | [Rectangle criterion and representation](Yin_C_F0329_v1.md#integrating-the-two-block-estimate) | Positive kernel integral, choice of disk/angular parameters and convergence of the matched forms. |
| dependency | [Phase realization](Yin_C_F0329_v1.md#a-phase-coupling-that-distinguishes-the-two-arcs) | Actual graph transfers, exact product trace and spectral density for the zero-mean free unitary product law. |
| dependency | [Finite kernel energy](Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) | Row, kernel-square and signed terms on analytic unitaries. |
| dependency | [Projection energy](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Lower bound on the two diagonal rectangles. |
| dependency | [Localized cost](Yin_C_F0297_v1.md#statement) | Local absolute estimate and the earlier use of indefinite curvature templates. |
| dependency | [Hilbert-kernel estimate](Yin_C_F0326_v1.md#statement) | The absolute cost and the positive-diagonal plus square-integrable remainder criterion. |
| dependency | [Marginal vacuum criterion](Yin_C_F0255_v1.md#statement) | Actuality of the separated double-segment scalar law. |
| dependency | [Mixed-gap calculation](Yin_C_F0305_v1.md#the-distinguished-derivative-before-smoothing) | Vacuum estimate across the separated pieces in the final graft. |
| dependency | [Phase norm identity](Yin_C_F0265_v1.md#statement) | Exact distinction between the joint and scalar vacua in the Borel phase model. |
| dependency | [Uniform phase estimate](Yin_C_F0320_v1.md#statement) | Absolute true slice-to-vacuum bound in both orientations. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0337_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

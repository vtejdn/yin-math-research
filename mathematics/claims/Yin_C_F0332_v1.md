---
author: Yin
---

# Subdividing the smaller endpoint of a curvature rectangle

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(Z\) be a distinguished normal coordinate of a bounded normal tuple with actual starred conjugate variables in a finite von Neumann algebra with faithful normal probability trace.
Write \(\mu\) for its compact diffuse law, \(\xi\) for its joint conjugate variable, \(\zeta=(i\gamma)^*(1\otimes1)\) for its real partial liberation vacuum, and \(\nu\) for the joint spectral measure of \(\zeta\) under left and right multiplication by \(Z\).
Let \(\lambda\) be a finite positive planar Borel measure and \(A\ge1,\ 0\le M<\infty\).
Assume
\[
 \begin{split}
   d\nu(z,w)&\le M\{\lambda(B(z,A|z-w|))+\lambda(B(w,A|z-w|))\}\,d\mu(z)d\mu(w),\\
   I_\lambda&=\iiint\kappa(z,v,w)^2\,d\mu(z)d\mu(v)d\lambda(w)<\infty ,             \tag{1}
 \end{split}
\]
where \(\kappa\) is reciprocal circumradius, zero on collinear or repeated triples.
The conventions of open or closed balls give the same sufficient condition after an arbitrary enlargement of \(A\).
For the matched curvature form of this coordinate on each original analytic test unitary,
\[
                 F_g(u)\ge -C_A M I_\lambda,\qquad
                 g(z,w)=\int\kappa(z,v,w)^2d\mu(v).                       \tag{2}
\]
Both oriented right slices are bounded on the entire original polynomial unit ball by \(C_A(\|\xi\|_2+\sqrt{M I_\lambda})\).
The canonical generator-first operator and its adjoint have domains containing all bounded vectors.
These conclusions require only the stated assumptions at the distinguished coordinate in the actual tuple.

In particular one may take \(\lambda=\mu\) whenever the density of \(\nu\) is bounded by a constant times the marginal masses of the two balls at the endpoint distance.
The critical estimate \(d\nu\le L|z-w|\,d\mu^2\) suffices on any compact Lipschitz graph over a real interval, for arbitrary correlations and without a positive lower bound on the real parameter density.
The mixed-measure criterion also applies to the critical example with divergent unrefined costs in [C_F0331](Yin_C_F0331_v1.md#statement).
There are actual trace-independent exchange pairs with bounded normalized slice costs for which no finite \(\lambda\) satisfies the first line of (1) for any finite \(A,M\).
The general implication remains open.

## Argument

### Subdivision by cubes

For a measurable marginal set \(F\) and any \(\epsilon>0\), one can partition \(F\), up to a null set, into countably many Borel sets \(F_i\) of positive masses \(s_i\) with
\[
                  \sum_i \frac{\nu(F_i\times F_i)}{s_i^2}
                            \le C_A M\{\lambda(F)+\epsilon\}.             \tag{3}
\]
Take first \(F\) compact and intersect it with a half-open square grid of mesh \(\delta\).
For points in any one cell \(Q\), both balls in (1) are contained in a fixed concentric enlargement \(c_A Q\) of its closed square.
The cell quotient in (3) is at most \(2M\lambda(c_A Q)\).
The enlarged squares overlap at most \(C_A\) times and the union for original cells meeting \(F\) lies in the \(C_A\delta\)-neighborhood of \(F\).
Finiteness and continuity of \(\lambda\) from above give (3) by taking \(\delta\) small.
For Borel \(F\), successively take disjoint compact subsets in the residual set whose union carries the entire restricted \(\mu\)-mass, by inner regularity.
Use separate meshes with a summable sequence of errors; the \(\lambda\)-masses of the compact subsets sum to at most \(\lambda(F)\).
Null cells can be omitted throughout.
The assertion concerns a choice for each fixed \(F\).

Let \(E,F\subset B=B(a,r)\) be disjoint Borel sets with masses \(t\ge s>0\) respectively and let \(q_{EF}=1_E\otimes1_F+1_F\otimes1_E\).
Apply the [signed lower bound](Yin_C_F0326_v1.md#statement) with the larger set unchanged to each \(E,F_i\) from (3).
Writing \(D=\nu(E^2)\), \(D_i=\nu(F_i^2)\) and \(C_i=\nu(E\times F_i)+\nu(F_i\times E)\), its cost is at most
\[
             2s_iD/t^2+2tD_i/s_i^2+C_i/t .
\]
Indeed the centered-square term in that bound expands into two diagonal terms bounded by \(s_iD/t^2,tD_i/s_i^2\), and the cross term \(C_i/(t+s_i)\).
The sum of the rectangular kernels converges boundedly to \(q_{EF}\) in the marginal spectral representation, so its fixed-unitary pairing passes to the sum.
Put \(b=1+2A\), enlarging it slightly if necessary.
On \(B^2\) the density bound in (1) is at most \(2M\lambda(bB)\), where \(bB=B(a,br)\).
Use this bound on \(D\) and \(\sum C_i\), apply (3) to the other term, and send \(\epsilon\) to zero.
Interchanging the endpoint sets in the other mass order gives
\[
       F_{q_{EF}}(u)\ge -C_A M\{\lambda(bB)\min(t,s)+t\lambda(F)+s\lambda(E)\}.      \tag{4}
\]
The inequality also holds if either marginal mass vanishes, since the signed form then vanishes.
The right side of (4) is explicit, so integrating it requires no measurable choice of the auxiliary partitions.

### Integrating the smaller level mass

In the [positive disk representation](Yin_C_F0329_v1.md#integrating-the-two-block-estimate), for fixed \(v,B\) take \(p\) equal to the real or imaginary part of \(h_v(z)=(z-v)/(\bar z-\bar v)\), assigning any bounded value at \(v\).
Put \(E=B\cap\{p>u_0\}\), \(F=B\cap\{p<l\}\) for \(-1<l<u_0<1\).
For \(\mu(B)>0\), take a pair \(P_+,P_-\) of real random variables with the common law \(p_*(\mu|_B/\mu(B))\) by evaluating its quantile at \(U,1-U\) for one uniform \(U\).
Then
\[
  \mathbb P(P_+>u_0,\ P_-<l)=\min(t,s)/\mu(B).
\]
Both events are upper intervals in \(U\), up to null endpoints, including for laws with atoms and the strict thresholds shown.
Integrating the triangle in the two levels gives
\[
       \int_{l<u_0}\min(t,s)\,dl\,du_0
          =\tfrac12\mu(B)\mathbb E(P_+-P_-)_+^2
          \le 2\inf_{c\in\mathbb R}\int_B |p-c|^2\,d\mu .
\]
The inequality follows by inserting any constant in the difference and using its two identical marginal laws.
When \(\lambda(bB)>0\), average over constants \(c=p(w)\) with normalized \(\lambda\) on \(bB\).
The integral of the first term of (4) in its braces is at most \(2\int_B\int_{bB}|p(z)-p(w)|^2\,d\lambda(w)d\mu(z)\).
It is zero if \(\lambda(bB)=0\).
The integral of \(t\lambda(F)+s\lambda(E)\) is exactly \(\tfrac12\int_B\int_B|p(z)-p(w)|^2\,d\lambda(w)d\mu(z)\), by the same elementary triangle integration for the two orders of the values.

For distinct \(z,w\),
\[
   \int_0^\infty\int_{\mathbb C}1_B(z)1_{bB}(w)\,\frac{dA(a)\,dr}{r^5}
                \le \frac{C_b}{|z-w|^2}.
\]
Indeed no center works if \((1+b)r<|z-w|\), and the available center area is at most \(\pi r^2\) thereafter.
Summing over the two components of \(h_v\) gives \(|h_v(z)-h_v(w)|^2\), which divided by \(|z-w|^2\) equals \(\kappa(z,v,w)^2\).
Coincidences have zero measure in \(\mu^2\otimes\lambda\) since \(\mu\) is diffuse, even for atomic \(\lambda\).
Tonelli thus bounds the integral of the right-hand costs in (4) by \(C_A M I_\lambda\).
On truncated radii the bounded marginal kernels can be paired before or after integration by normality; the enlarged balls only enter the estimate.
As the truncations exhaust the radii the curvature kernels increase to \(g\).
The matched limit on each analytic unitary follows from convergence in \(L^2(\mu^2)\) of their products with the marginal gap, as in the [signed energy argument](Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries).
This proves (2).
Substitution in the same real-component energy calculation and decomposition of a core contraction into real and imaginary parts gives the stated bounds for both orientations and then both original bounded-vector domains.

### Marginal and geometric control measures

For \(\lambda=\mu\), actual scalar conjugacy supplies \(I_\mu<\infty\) by the [geometric criterion](Yin_C_F0255_v1.md#statement).
If the marginal has a uniform positive lower linear mass on its support, this case in particular covers linear decay in the endpoint distance.
A compact marginal on the graph \(z=x+i\phi(x)\) of a Lipschitz function on a bounded nondegenerate interval requires no such lower bound on its own mass.
Take \(\lambda\) to be the image of Lebesgue length on that interval.
For a ball centered on the graph of radius \(A|z-w|\), its \(\lambda\)-mass dominates a fixed multiple of \(|z-w|\) for \(z,w\) on the graph; this follows by taking parameter displacements up to the radius divided by the Lipschitz constant of the graph map and using the finite diameter at large radii.
The [graph scalar argument](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) gives an \(L^3(dx)\) density of the parameter law from scalar actuality, and gives a scalar vacuum for any such density on the graph.
Adding the parameter length measure keeps the density in \(L^3\), so the normalized law of \(\mu+\lambda\) has finite total squared curvature, which contains \(I_\lambda\) as a nonnegative mixed term.

The same reasoning covers a finite sum of control measures with finite mixed integrals when their sum dominates the spectral density in (1).
For example, planar Lebesgue measure on a bounded disk containing a neighborhood of the compact spectrum has finite mixed integral.
For fixed \(z,v\) the integral in the area variable \(w\) is at most \(C(1+\log_+(D'/|z-v|))\) for a fixed containing diameter \(D'\).
Use \(\kappa^2\le4/|z-v|^2\) within distance \(2|z-v|\) of \(z\) and \(\kappa^2\le4/|z-w|^2\) outside.
Integrating the logarithm in \(v,z\) is permitted since \(\mu(B(z,t))\le t M_1\mu(z)\) and \(M_1\mu\in L^2(\mu)\) by the scalar criterion.

### The two rectangular counterexamples

For the [critical example](Yin_C_F0331_v1.md#statement) take \(\lambda\) to be the sum of \(\mu\), planar area on a disk containing a neighborhood of the entire support, and length on the real base interval of [its horizontal layers](Yin_C_F0331_v1.md#a-critical-phase-on-a-dense-collection-of-horizontal-segments), transported under the fixed affine graft.
All three mixed integrals are finite.
For the length term, adding this interval length to the layered measure preserves summability of the horizontal density suprema in its Cauchy-transform proof.
The other pieces of the graft and the doublets are at a fixed positive distance from this interval component, so the normalized sum of the full law and the extra length has a scalar vacuum by the same disjoint-component calculation used there.
Its finite curvature bounds the mixed length term.

For completeness, the phase \(h\) in that example obeys the first inequality of (1) for this sum of measures, up to fixed constants.
On a single straight segment of either small-component construction the change of its angular parameter up to an endpoint distance is bounded by a fixed multiple of the mass of a ball of twice that distance, by linear parametrization with its assigned mass.
This also bounds the squared phase change as the phase is bounded.
On the real base and the two semicircular-law intervals the inverse angle is Lipschitz, so the area term suffices there.
For two different components of the grid construction use the horizontal coordinate and its error of order \(\sqrt{r_j}\) on a segment of height \(r_j\), in the original units.
The squared angle difference is bounded by \(C(|z-w|^2+r_j+r_k)\), assigning height zero on the base.
Each nonzero height is bounded by a fixed multiple of \(|z-w|\) on such a pair.
A ball enlarged by a fixed sufficiently large factor then reaches the real base interval and captures length at least a fixed multiple of that height, since the segment centers project into the middle half of the interval.
For [the separate doublets](Yin_C_F0331_v1.md#a-disjoint-component-that-excludes-positive-diagonal-decompositions), different segments of the same pair have phase difference \(O(q_n)\) and their enlarged ball contains a whole segment of mass comparable to \(q_n\).
Between different pairs of indices \(n<k\), the parameter difference is \(O(q_n)\), smaller than a constant times the gap \(2^{-n}\); area suffices.
Across the separated main constituents of the final graft the area lower bound at their fixed gap suffices as well.
These estimates remain true with changed constants under the fixed affine changes in that example.
Its actual spectral density equals a constant times \(|h(z)-h(w)|^2\).
Thus one-sided subdivision proves finiteness of the signed loss even though the unsubdivided optimized estimates have divergent integral and \(g\) is unbounded below as a quadratic form.

In contrast, the earlier [two-arc phase construction](Yin_C_F0329_v1.md#a-phase-coupling-that-distinguishes-the-two-arcs) gives actual strong exchange pairs with positive fixed lower spectral density on \(C_n^+\times C_n^-\) for all \(n\), while each twin group lies at height and separation of order \(r_n=2^{-3n-12}\) above \(x_n=2^{-n}\).
For any fixed finite \(A\), both balls in (1) on each such product are contained in \(B(x_n,C_A r_n)\).
These containing disks are pairwise disjoint for all sufficiently large \(n\).
The positive density lower bound would force a fixed positive \(\lambda\)-mass in each disk, which is impossible for a finite measure.
This excludes automatic necessity of (1) even with the exact two-marginal product traces and small bounded liberation gradients.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T18:36 |
| status | open |
| reason | Fix the endpoint subdivision, mixed curvature estimate and critical applications for independent whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both domain bounds from an auxiliary control measure, critical Lipschitz graphs, and scopes of the two examples. |
| argument | [Argument](#argument) | Grid partitions, smaller-side signed sum, countermonotone quantiles, enlarged disk integral and comparison of actual model densities. |
| dependency | [Signed block estimate](Yin_C_F0326_v1.md#statement) | Unequal-trace lower bound before partitioning the smaller endpoint. |
| dependency | [Disk representation](Yin_C_F0329_v1.md#integrating-the-two-block-estimate) | Exact positive representation, truncated pairing and passage to the analytic core. |
| dependency | [Matched energy](Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Gap-weighted limit and both oriented original bounds from a uniform negative-form bound. |
| dependency | [Geometric criterion](Yin_C_F0255_v1.md#statement) | Actual scalar maximal-density and squared curvature estimates, also for normalized sums. |
| dependency | [Graph parameter](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Necessity and sufficiency of cubic integrability on a Lipschitz graph. |
| dependency | [Critical example](Yin_C_F0331_v1.md#statement) | Actuality, curvature obstruction and spectral density formula for the critical near-semicircular pair. |
| dependency | [Horizontal layers](Yin_C_F0331_v1.md#a-critical-phase-on-a-dense-collection-of-horizontal-segments) | Phase oscillations, scale-to-height gaps, arc allocation, and scalar Cauchy-transform control after adding length. |
| dependency | [Straight doublets](Yin_C_F0331_v1.md#a-disjoint-component-that-excludes-positive-diagonal-decompositions) | Inverse parameter oscillations and distances between and within the separated groups. |
| dependency | [Separated phase values](Yin_C_F0329_v1.md#a-phase-coupling-that-distinguishes-the-two-arcs) | Actual strong model with fixed density on opposite tiny arcs in disjoint neighborhoods. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T18:45 |
| status | proved |
| reason | R_F0338 checked the corrected fixed statement, the smaller-endpoint partition, angular variance integration and all nine declared dependency interfaces. The mixed curvature criterion gives both original bounded-vector domains at the distinguished coordinate, including critical linear decay on a Lipschitz graph. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both domain bounds from an auxiliary control measure, critical Lipschitz graphs, and scopes of the two examples. |
| argument | [Argument](#argument) | Grid partitions, smaller-side signed sum, countermonotone quantiles, enlarged disk integral and comparison of actual model densities. |
| dependency | [Signed block estimate](Yin_C_F0326_v1.md#statement) | Unequal-trace lower bound before partitioning the smaller endpoint. |
| dependency | [Disk representation](Yin_C_F0329_v1.md#integrating-the-two-block-estimate) | Exact positive representation, truncated pairing and passage to the analytic core. |
| dependency | [Matched energy](Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Gap-weighted limit and both oriented original bounds from a uniform negative-form bound. |
| dependency | [Geometric criterion](Yin_C_F0255_v1.md#statement) | Actual scalar maximal-density and squared curvature estimates, also for normalized sums. |
| dependency | [Graph parameter](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Necessity and sufficiency of cubic integrability on a Lipschitz graph. |
| dependency | [Critical example](Yin_C_F0331_v1.md#statement) | Actuality, curvature obstruction and spectral density formula for the critical near-semicircular pair. |
| dependency | [Horizontal layers](Yin_C_F0331_v1.md#a-critical-phase-on-a-dense-collection-of-horizontal-segments) | Phase oscillations, scale-to-height gaps, arc allocation, and scalar Cauchy-transform control after adding length. |
| dependency | [Straight doublets](Yin_C_F0331_v1.md#a-disjoint-component-that-excludes-positive-diagonal-decompositions) | Inverse parameter oscillations and distances between and within the separated groups. |
| dependency | [Separated phase values](Yin_C_F0329_v1.md#a-phase-coupling-that-distinguishes-the-two-arcs) | Actual strong model with fixed density on opposite tiny arcs in disjoint neighborhoods. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0338_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

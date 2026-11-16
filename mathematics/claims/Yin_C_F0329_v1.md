---
author: Yin
---

# A decay criterion for rectangular curvature costs and an exchange-symmetric obstruction

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

At an actual coordinate of a bounded normal tuple with faithful normal probability trace, let \(\mu\) be the compact marginal law, \(D>0\) its support diameter, and \(\zeta=(i\gamma)^*(1\otimes1)\) the real partial liberation vacuum.
Write \(\nu\) for the joint spectral measure of \(\zeta\) under the two marginal actions and \(g(z,w)=\int\kappa(z,v,w)^2\,d\mu(v)\) for the squared Menger curvature kernel.
Consider the [positive disk and angular rectangle representation](../drafts/Yin_D_F0006.md#positive-rectangular-representation-of-the-menger-kernel) and its nonnegative integrated cost \(\mathcal C\), defined precisely below.
If a bounded nondecreasing function \(\omega\) on \([0,D]\) satisfies
\[
 d\nu(z,w)\le\omega(|z-w|)\,d\mu(z)d\mu(w),\qquad
                         \int_0^D\frac{\omega(r)}{r^2}\,dr<\infty ,
\]
then
\[
 \mathcal C\le C\left[
  \|M_1\mu\|_{L^1(\mu)}\int_0^D\frac{\omega(r)}{r^2}\,dr+
                         \frac{\omega(D)}{D^2}\right]                   \tag{1}
\]
for an absolute constant \(C\).
Here \(M_1\mu(z)=\sup_{r>0}\mu(B(z,r))/r\).
Consequently the matched signed curvature form is bounded below uniformly on the strict polynomial analytic unitary tests, and both oriented original coordinate slices are bounded on polynomial contractions.
The hypothesis includes \(\omega(r)=O(r^{1+\alpha})\) as \(r\downarrow0\) for any \(\alpha>0\).

For every \(\varepsilon>0\) there is an actual exchange-symmetric normal pair with exact product two-marginal trace, both full strong duals and
\(\|\zeta\|_\infty<\varepsilon,\ \nu\le\varepsilon^2\mu^2\) at each coordinate, for which \(\mathcal C=\infty\).
The same example has infinite integrated cost even if one uses the smaller of the signed rectangle cost and the absolute Hilbert-kernel bound from [C_F0326](Yin_C_F0326_v1.md#statement) on each rectangle.
The marginal \(g\) lies outside \(L^2(\mu^2)\), but its positive diagonal blocks have finite signed cost and its remainder lies in \(L^2(\mu^2)\) as in (4) of that result.
The pairs also obey the absolute joint slice-to-vacuum ratio bound for free unitary phase couplings.
The divergence concerns the stated integral budgets.

## Argument

### Integrating the two-block estimate

For \(z\ne v\) let \(p_v(z)\) denote in turn the real and the imaginary part of \((z-v)/(\bar z-\bar v)\).
Assign any value at \(v\), a marginal null point.
For a disk \(B(a,r)\) and levels \(-1<l<u<1\) put \(E=B(a,r)\cap\{p_v>u\}\), \(F=B(a,r)\cap\{p_v<l\}\).
Write \(t=\mu(E),s=\mu(F)\), and \(e,f\) for the marginal spectral projections.
For \(ts>0\) set \(k=e/t-f/s\) and put
\[
  C(E,F)=ts\left[\frac{\nu(E^2)}{t^3}+\frac{\nu(F^2)}{s^3}
                     +\frac{\|k\zeta k\|_2^2}{1/t+1/s}\right].
\]
Take zero cost for \(ts=0\).
Set \(\mathcal C\) equal to \(2/c_0\) times the sum for the two choices of \(p_v\) of the integrals of this cost against \(d\mu(v)dA(a)dr\,dl\,du/r^5\).
Here the positive absolute constant \(c_0\) is the integral of \(1_{B(a,r)}(0)1_{B(a,r)}(1)dA(a)dr/r^5\).
For clarity, the disk integral at two distinct sites is \(c_0/|z-w|^2\) by a similarity.
The threshold-area integral of the symmetric rectangle kernel at these sites in the disk is \((p_v(z)-p_v(w))^2/2\).
Adding the two components gives the squared curvature times \(|z-w|^2/2\) by the inscribed-angle identity.
This proves the stated representation of \(g\).

Set \(w_r=\omega(\min(2r,D))\).
On the disk product the assumed density bound is \(w_r\).
Thus \(\nu(E^2)\le w_rt^2,\ \nu(F^2)\le w_rs^2\), and the spectral calculus gives \(\|k\zeta k\|_2^2\le w_r(1/t+1/s)^2\).
It follows that \(C(E,F)\le2w_r(t+s)\) whenever both sets have positive mass.
The two thresholds must then belong to the essential range interval of \(p_v\) on the disk.
Its length is at most \(C_1\min(1,r/|z-v|)\) for any \(z\) in the disk distinct from \(v\): if \(|z-v|>4r\), angular variation is bounded by \(C_1r/|z-v|\) by differentiation on that disk, and otherwise the trivial diameter two suffices after increasing \(C_1\).
Since \(t+s\le\mu(B(a,r))\), integration in the two levels costs at most a constant times \(w_r\int_{B(a,r)}\min(1,r^2/|z-v|^2)d\mu(z)\).
Integrating over the possible centers for each \(z\) gives area \(\pi r^2\).

Now \(\iint\min(1,r^2/|z-v|^2)d\mu(v)d\mu(z)\) is at most both one and \(C_2r\int M_1\mu\,d\mu\).
For the latter bound, at each \(z\) use its ball mass estimate on the inner disk and on annuli with radii \(2^jr\), summing \(C2^{-j}rM_1\mu(z)\).
This maximal function is in \(L^2(\mu)\) by the [actual scalar vacuum criterion](Yin_C_F0255_v1.md#statement).
Integrating \(w_r\) against these bounds with measure \(dr/r^3\), splitting at \(D/2\), proves (1).
At radii truncated away from zero and infinity, the kernel representation and Fubini apply to the fixed-unitary insertion pairing since it is normal on bounded marginal kernels and the relevant parameter region has finite measure.
The signed rectangular estimate gives the lower bound \(-\mathcal C\).
As the truncations exhaust all radii, the kernels increase to \(g\).
The gap times \(g\) is square integrable, so the two generator gap tensors and then the fixed analytic forms converge by the [matched curvature graph argument](Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries).
The signed energy inequality there gives both original slice bounds.

### A planar law with small components above a straight interval

Let \(x_n=2^{-n},\ r_n=2^{-3n-12},\ t_n=r_n/n^2,\ \rho_n=t_n^{5/4}/1000\), \(n\ge1\).
At each of the two centers \(x_n\pm r_n/20+i r_n\), take a semicircular arc \(C_n^\pm\) of radius \(\rho_n\) carrying normalized arclength of mass \(t_n/2\).
Endpoints have zero mass.
Put the remaining probability equally with constant density on the two intervals \([0,1]\) and \([3,4]\).
This defines the diffuse compactly supported \(\mu\).

The distance from \(C_n^\pm\) to any other component is at least \(cr_n\) with an absolute \(c>0\).
At a point on either real interval the mass of any disk of radius \(R\) is \(O(R)\).
Indeed every arc group meeting the disk has \(r_n\lesssim R\) by its height, and the disjoint intervals \([x_n-r_n,x_n+r_n]\) for the groups that meet it all lie in a real interval of length \(O(R)\).
Their total masses are bounded by the sum of those interval lengths.
For a point on \(C_n^\pm\) the same \(O(R)\) holds for \(R\ge cr_n\), with constants allowed to depend on this absolute \(c\).
The group \(n\) contributes at most \(t_n\lesssim R\), and all other groups meeting the disk have \(r_j\lesssim R\) by the dyadic separation of the real centers.
At smaller \(R\) only the one arc can occur upon decreasing \(c\), and its disk mass is at most \(C(t_n/\rho_n)R\) by arclength on a semicircle.
Thus \(\int (M_1\mu)^2d\mu<\infty\) since \(\sum t_n^3/\rho_n^2<\infty\).

Remove from \(g\) the blocks \((t_n/2)\rho_n^{-2}1_C\otimes1_C\) for every \(C=C_n^\pm\), and call the remaining nonnegative kernel \(b\).
The removed term is precisely the contribution from triples on the same arc, almost everywhere.
For two endpoints on the real intervals, the contribution from each rare group is at most \(C t_n\phi_n(z)\phi_n(w)\) with \(\phi_n(x)=r_n/((x-x_n)^2+r_n^2)\).
Indeed for a point \(v\) off the real line and two real endpoints the exact squared curvature is \(4(\operatorname{Im}v)^2/(|v-z|^2|v-w|^2)\), and all points of the group have height comparable to \(r_n\).
Since \(\|\phi_n\|_{L^2(dx)}^2\le C/r_n\), these kernels sum in product \(L^2\) by \(\sum t_n/r_n<\infty\).
For an endpoint \(z\in C_n^\pm\) and \(w\) on another component, put \(d=|z-w|\ge cr_n\).
The diameter bound \(\kappa\le2/\max(d,|z-v|)\) and the disk mass bound above on scales at least \(d\) give \(g(z,w)\le C/d\) by dyadic annuli about \(z\).
A second use of the mass bound gives \(\int_{|z-w|\ge cr_n}|z-w|^{-2}d\mu(w)\le C/r_n\).
For two endpoints on the same arc the unremoved third sites are also at distance at least \(cr_n\), giving \(b(z,w)\le C/r_n\).
These estimates yield \(\|b\|_{L^2(\mu^2)}<\infty\) by \(\sum(t_n/r_n+t_n^2/r_n^2)<\infty\).
The block integrals sum finitely by \(\sum t_n^3/\rho_n^2<\infty\), so the scalar curvature is finite and the geometric criterion supplies an actual marginal vacuum.
However the block squared norms sum to at least \(\sum_n(t_n/2)^4/\rho_n^4=\infty\), so \(g\notin L^2(\mu^2)\).

### A phase coupling that distinguishes the two arcs

Parametrize the planar law by a Haar circle variable, choosing a Borel isomorphism \(F\) up to null sets as follows.
Allocate two disjoint short angular intervals about \(1\) and \(-1\), each of Haar mass \(\sum_n t_n/2\).
Subdivide each into successive intervals of masses \(t_n/2\) and map these by linear arclength parametrizations onto \(C_n^+\) and \(C_n^-\), respectively.
Map each of the two complementary long intervals linearly onto one of the two real intervals.
Discard the countable endpoints on both sides and extend measurably there.
The inverse circle-valued function \(h\) is Lipschitz with an absolute constant on each real interval, and with constant \(O(t_n/\rho_n)\) on \(C_n^\pm\), since arclength and chord distance are comparable on a semicircle.
The values of \(h\) on the two arcs of any group are separated by an absolute positive distance.
Its secant energy \(J=\iint |h(z)-h(w)|^2/|z-w|^2\,d\mu^2\) is finite.
For the own-arc pairs use \(\sum t_n^4/\rho_n^2<\infty\).
For the pairs with one rare endpoint and the other on another component, use the preceding \(C/r_n\) bound for the off-component inverse-square integral and \(\sum t_n/r_n<\infty\).
Pairs on different real intervals have a fixed gap.

Let \(X\) be Haar, and \(V\) free from \(X\) with circle density \(1+2a\cos(2\phi)\) relative to Haar probability, where \(0<a<1/4\).
This non-Haar unitary has zero mean, and its bounded density gives an actual scalar vacuum by the geometric criterion.
Write \(Y=X^*V,\ Z_0=F(X),\ Z_1=F(Y)\).
The [Haar absorption and exchange calculation](Yin_C_F0315_v1.md#actuality-of-the-product-law) gives an involution exchanging \(X,Y\), and \(Y\) is Haar.
For positive powers the conditional expectation of \(Y^j=(X^*V)^j\) onto \(W^*(X)\) vanishes by the reduced-word formula since \(V\) is centered.
The negative powers follow by adjunction.
Thus the two generated marginals have exact product trace, also for their relabelings by \(F\).

For the pair \(Z_0,Y=h(Z_0)^*V\) the [phase coupling criterion](Yin_C_F0265_v1.md#statement) gives full actuality since \(J<\infty\).
At \(Z_0\) its distinguished derivative kills \(W^*(Y)\) on bounded strong-star approximants from the omitted algebra.
Consequently it restricts to the \(Z_0,Z_1\) core with its same vacuum and intrinsic coarse values, since \(F\) generates the same von Neumann algebras and the approximants pass the product rule to every word. [Omitted-algebra graph calculation](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra)
Exchange supplies the other actual derivative.
The [uniform coupling bound](Yin_C_F0320_v1.md#statement) gives strong domains and its absolute slice-to-vacuum bound throughout this family.

For \(H=\xi_V V^*-1\), the [liberation vacuum calculation](Yin_C_F0265_v1.md#the-base-coordinate-vacuum-and-its-inverse-gap-energy) gives \(\gamma^*(1\otimes1)=h^*Hh-H\) and
\[
             d\nu=\|H\|_2^2 |h(z)-h(w)|^2d\mu(z)d\mu(w).
\]
The same liberation holds after relabeling \(Y\), by the same omitted-algebra approximation; the factor \(-i\) for the real liberation leaves its spectral measure unchanged.
The angular formula \(H^*=P_-\rho-P_+\rho\) for circle density \(\rho\) gives \(\|H\|_\infty\le2a\), and \(H\ne0\) since \(V\) is non-Haar. [Angular derivative](Yin_C_F0320_v1.md#the-angular-derivative-and-the-cubic-density-defect)
Thus \(\|\zeta\|_\infty\le4a,\ \nu\le16a^2\mu^2\), and exchange gives both estimates at the other coordinate.
Choose \(4a<\varepsilon\).
For each own-arc block, \(\nu(C^2)\le C\|H\|_2^2 t_n^4\) because the corresponding angular interval has length \(O(t_n)\).
Its signed lower-bound cost in (4) of C_F0326 is \(\rho_n^{-2}\nu(C^2)\).
The sum is finite and the remainder \(b\) was proved square integrable.

### Divergence of the integrated costs

Use \(p_v=\operatorname{Re}((z-v)/(\bar z-\bar v))\).
Restrict \(v\) to \([x_n-r_n/100,x_n+r_n/100]\) in the bulk.
Take the center in the disk of radius \(r_n/20\) about \(x_n+i r_n/2\) and \(3r_n/2<r<2r_n\).
Each such disk contains both rare arcs and a real bulk interval of length comparable to \(r_n\), and meets no other rare group.
On the real bulk \(p_v=1\) almost everywhere, while on both arcs \(|\operatorname{Re}(z-v)|\le r_n/10,\ |\operatorname{Im}(z-v)|\ge 0.99r_n\) give \(p_v<-0.9\).
For \(-1/2<l<-1/4,\ 1/4<u<1/2\), the lower set is exactly the rare group up to null sets.
It has mass \(s=t_n\); the upper set has bulk mass \(t\) comparable to \(r_n\).
Since \(h\) separates the two arc families, the cross terms between the two arcs inside \(F^2\) give \(\nu(F^2)\ge c_1\|H\|_2^2t_n^2\).
The nonnegative cost therefore has \(C(E,F)\ge t\nu(F^2)/s^2\ge c_2\|H\|_2^2r_n\).

On the same rectangles the alternative absolute cost from (2) of C_F0326 is \((2m+3)\sqrt{2ts}\ge c_3r_n/n\) for any admissible domination constant \(m\).
The smaller of the two costs is thus at least \(c_a r_n/n\), for \(c_a>0\) independent of \(n\).
The parameter volume at scale \(n\) against the prescribed measure is bounded below by a constant times \(r_n\cdot r_n^2\cdot r_n/r_n^5=1/r_n\), using the fixed positive interval lengths for the two thresholds.
The radius ranges for different \(n\) are disjoint.
Summing gives at least \(c'_a\sum_n1/n=\infty\) for the minimum and hence also for the original cost.
This proves the stated limitation even with exact two-marginal trace and arbitrarily small positive liberation bounds.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T18:09 |
| status | open |
| reason | Fix the radial decay criterion and the actual two-marginal example obstructing the integrated rectangle bounds. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Integrated decay estimate, original slice conclusion and trace-independent exchange example with divergent rectangle costs. |
| argument | [Argument](#argument) | Disk and angular oscillation integration, rare arc geometry, generator relabeling, liberation density, and a divergent disjoint-scale lower sum. |
| dependency | [Signed rectangle and kernel estimates](Yin_C_F0326_v1.md#statement) | Unequal-mass signed bound, absolute Hilbert-kernel alternative and finite cost of positive square blocks modulo a Hilbert remainder. |
| dependency | [Actual marginal geometry](Yin_C_F0255_v1.md#statement) | Squared maximal linear density and Menger curvature characterize scalar actuality. |
| dependency | [Signed curvature limit](Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Weighted gap convergence on analytic tests and both oriented original costs from the uniform lower bound. |
| dependency | [Phase coupling criterion](Yin_C_F0265_v1.md#statement) | Finite inverse-map secant energy gives actual vacua in the once-relabelled pair. |
| dependency | [Liberation law](Yin_C_F0265_v1.md#the-base-coordinate-vacuum-and-its-inverse-gap-energy) | Explicit bounded commutator expression and product spectral density of the first liberation vector. |
| dependency | [Omitted graph](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Extension by zero to bounded functions of the relabeled second variable and passage to joint words. |
| dependency | [Haar exchange](Yin_C_F0315_v1.md#actuality-of-the-product-law) | Haar absorption, exchanging involution and preservation of the two generated marginal algebras. |
| dependency | [Uniform phase estimate](Yin_C_F0320_v1.md#statement) | Both strong domains and a uniform normalized bound for all actual twice-relabelled product models. |
| dependency | [Angular vacuum](Yin_C_F0320_v1.md#the-angular-derivative-and-the-cubic-density-defect) | Fourier expression bounding the liberation gradient for the smooth non-Haar density. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T18:39 |
| status | proved |
| reason | Adopt the Dini estimate and the actual exchange-symmetric example with divergent integrated costs after independent review of all nine dependency interfaces. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Integrated decay estimate, original slice conclusion and trace-independent exchange example with divergent rectangle costs. |
| argument | [Argument](#argument) | Disk and angular oscillation integration, rare arc geometry, generator relabeling, liberation density, and a divergent disjoint-scale lower sum. |
| dependency | [Signed rectangle and kernel estimates](Yin_C_F0326_v1.md#statement) | Unequal-mass signed bound, absolute Hilbert-kernel alternative and finite cost of positive square blocks modulo a Hilbert remainder. |
| dependency | [Actual marginal geometry](Yin_C_F0255_v1.md#statement) | Squared maximal linear density and Menger curvature characterize scalar actuality. |
| dependency | [Signed curvature limit](Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Weighted gap convergence on analytic tests and both oriented original costs from the uniform lower bound. |
| dependency | [Phase coupling criterion](Yin_C_F0265_v1.md#statement) | Finite inverse-map secant energy gives actual vacua in the once-relabelled pair. |
| dependency | [Liberation law](Yin_C_F0265_v1.md#the-base-coordinate-vacuum-and-its-inverse-gap-energy) | Explicit bounded commutator expression and product spectral density of the first liberation vector. |
| dependency | [Omitted graph](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Extension by zero to bounded functions of the relabeled second variable and passage to joint words. |
| dependency | [Haar exchange](Yin_C_F0315_v1.md#actuality-of-the-product-law) | Haar absorption, exchanging involution and preservation of the two generated marginal algebras. |
| dependency | [Uniform phase estimate](Yin_C_F0320_v1.md#statement) | Both strong domains and a uniform normalized bound for all actual twice-relabelled product models. |
| dependency | [Angular vacuum](Yin_C_F0320_v1.md#the-angular-derivative-and-the-cubic-density-defect) | Fourier expression bounding the liberation gradient for the smooth non-Haar density. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0335_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

---
author: Yin
---

# Review of the decay criterion and divergent rectangular curvature costs

## Finding

At 2026-11-16T18:10 UTC a separately assigned agent for Yin independently reviewed the entire C_F0329 v1 candidate fixed at 18:09 UTC.
The reviewer did not develop this proof or receive author explanations, development dialogue or prior findings on the candidate.
The mathematical inputs were the candidate and its cited results, including the disk representation identified in its statement.
The decay criterion gives the asserted original slice bounds, and the example has divergent integrated costs at both coordinates despite its strong domains and uniform normalized slice bound.

For two unit-separated sites the possible disk centers have area at most \(\pi r^2\), have zero area for \(r<1/2\), and have positive area for \(r>1\).
This gives \(0<c_0<\infty\), and joint translation, rotation and dilation at separation \(d\) multiply the integral by \(d^{-2}\).
When the ordered values of a component of the angular phase differ by \(\Delta\), the threshold pairs giving the symmetric rectangle occupy a triangle of area \(\Delta^2/2\).
The squared distance of the two complex phases is four times the squared sine of the angle at \(v\), hence equals \(d^2\kappa^2\).
Combining the two real components proves the normalization \(2/c_0\) of the positive representation.

Within a disk, domination by \(w_r=\omega(\min(2r,D))\) gives \(\|k\zeta k\|_2^2\le w_r(1/t+1/s)^2\) by integration of \(|k(z)k(w)|^2\).
Together with the two individual block terms this gives \(2w_r(t+s)\).
If both sets carry mass then both thresholds belong to the angular range interval on the disk.
Its squared oscillation is bounded by a constant times \(\min(1,r^2/|z-v|^2)\) for every site \(z\) in that disk, since at \(|z-v|>4r\) all intervening points stay at least \(|z-v|/2\) from \(v\).
Integration in the disk center contributes \(\pi r^2\).
The inner ball and successive dyadic annuli contribute at most \(CrM_1\mu(z)\), and the total may also be bounded by one.
The small-radius integral is thus bounded by a constant times \(\|M_1\mu\|_1\int_0^D\omega(s)s^{-2}\,ds\), by \(s=2r\).
Integrating \(r^{-3}\) on \(r\ge D/2\) gives \(2/D^2\).
On a bounded radius window away from zero, centers relevant to the marginal form a bounded region, giving the required finite parameter measure for the signed pairing.
As the windows exhaust \((0,\infty)\), the truncated kernels increase to \(g\) and their gap multiples converge in Hilbert norm by \(\int|z-w|^2g^2\,d\mu^2\le4c^2(\mu)\).
The first-derivative series on each strict analytic test and the cited signed energy inequality then give both oriented bounds on the represented core.

The two arcs in a group have center separation \(r_n/10\), total mass \(t_n=r_n/n^2\), and radius \(\rho_n\ll r_n\).
Distinct groups have mutually separated real centers on the larger scale \(2^{-\min(n,j)}\).
At real sites the disjoint real intervals attached to the groups meeting a radius-\(R\) disk all fit in a real interval of length \(O(R)\), by the heights of their arcs.
For a site on arc \(n\) the corresponding \(O(R)\) estimate begins at \(cr_n\), and below that scale the only mass is bounded by \(C t_n R/\rho_n\).
The exceptional maximal-density integral and the same-arc triple curvature are summable by \(t_n^3/\rho_n^2=10^6 t_n^{1/2}\).
After removing each same-arc square kernel with coefficient \((t_n/2)/\rho_n^2\), the bulk-to-bulk remainder has \(L^2\) norm bounded by \(C\sum t_n/r_n\) using the exact formula for curvature at two real sites.
For another component at distance \(d\ge cr_n\) from the first rare endpoint, integration of the diameter bound gives \(g\le C/d\) and \(\int_{d\ge cr_n} d^{-2}\,d\mu\le C/r_n\).
For a pair on the same arc the residual third-site contribution is at most \(C/r_n\).
These bounds sum in squared norm using \(\sum_n(n^{-2}+n^{-4})<\infty\).
In contrast, the disjoint removed blocks alone have squared norms proportional to \(t_n^4/\rho_n^4=10^{12}/t_n\).
This proves \(g\notin L^2\) together with finite scalar curvature and an actual marginal vacuum.

Centered short Haar intervals at \(1,-1\) can be chosen with equal mass and opposite centers, so the two complementary intervals have equal mass as required by the real bulk.
Discarding their endpoints and the countably many subdivision endpoints leaves the prescribed measurable inverse.
Arclength and chord length are comparable on each semicircle, giving same-arc phase energy \(O(t_n^4/\rho_n^2)\).
The other pairs with a rare endpoint contribute \(O(\sum_n t_n/r_n)\).
The near-constant smooth circle density for \(V\) has zero first moment and only the second Fourier modes besides its constant.
Centered reduced-word products therefore give \(\mathbb E_{W^*(X)}(Y^j)=0\) for every nonzero integer \(j\), proving exact two-marginal product traces after relabeling.
Finite inverse-map energy and scalar actuality give the first actual derivative before relabeling.
Bounded approximation from the omitted algebra identifies that derivative on the original relabeled core with its intrinsic values and the same vacuum, and exchange supplies the other coordinate.
The normalized full-core estimate applies to this pair.
For the two-mode density the angular formula gives \(H^*=a(e^{-2i\phi}-e^{2i\phi})\), so \(H\ne0\) and \(\|H\|_\infty=2a\).
The explicit liberation vacuum then gives \(\|\zeta\|_\infty\le4a\) and the claimed product density.
On the same-arc square the angular interval length is \(O(t_n)\), so its signed block cost is \(O(\|H\|_2^2 t_n^4/\rho_n^2)\), summable.

In the indicated disjoint radius windows, the disks contain both rare arcs and a bulk subinterval of length comparable to \(r_n\), with no other rare group.
The real angular component equals one on the real line away from \(v\), while the horizontal displacement and the height bounds on both arcs give a value less than \(-0.9\).
The threshold sets therefore have masses \(t\asymp r_n\) and \(s=t_n\).
The two opposite short Haar intervals give a uniform lower bound on the squared phase separation for cross-arc pairs in \(F^2\).
It follows that the signed cost is at least \(c\|H\|_2^2 r_n\) and the absolute cost at least \(c' r_n/n\).
For any fixed \(a>0\), the smaller is bounded below by a positive multiple of \(r_n/n\).
The bulk \(v\)-interval, disk of centers and radius window have measures comparable to \(r_n,r_n^2,r_n\), respectively, and the level intervals have fixed lengths.
After the factor \(r^{-5}\) these yield volume comparable to \(1/r_n\), so summing the costs over disjoint windows gives the divergent harmonic series.
Choosing \(a\) small enough for the requested liberation bounds retains this positive lower coefficient.
The nine declared dependency interfaces were checked at their stated uses.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0329_v1.md#decision-candidate) | Exact fixed 18:09 UTC candidate, both parts and their inputs. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0329_v1.md#statement) | Weighted radial decay, signed and absolute costs, actual exchange pair, strong duals, two-marginal product trace, Hilbert remainder and divergent integrated minimum. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0329_v1.md#argument) | Entire disk and angular representation, truncation limit, geometry and phase of the example, and its quantitative lower bound over disjoint windows. |
| [Finding](#finding) | [Rectangular estimates](../../claims/Yin_C_F0326_v1.md#statement) | Unequal-mass two-block cost, absolute symmetric Hilbert-kernel cost, and the summable own-arc square criterion with a Hilbert remainder. |
| [Finding](#finding) | [Marginal geometry](../../claims/Yin_C_F0255_v1.md#statement) | Actuality from finite squared maximal density and total squared curvature, and the converse for the radial estimate. |
| [Finding](#finding) | [Signed curvature limit](../../claims/Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Convergence of the gap tensors and analytic insertion form, followed by the two oriented core bounds. |
| [Finding](#finding) | [Phase coupling](../../claims/Yin_C_F0265_v1.md#statement) | Actuality of the partially relabeled pair using finite secant energy and actual scalar vacua. |
| [Finding](#finding) | [Liberation measure](../../claims/Yin_C_F0265_v1.md#the-base-coordinate-vacuum-and-its-inverse-gap-energy) | The conjugated centered angular vacuum, its joint spectral density, and the non-Haar criterion. |
| [Finding](#finding) | [Omitted graph](../../claims/Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Omitted Borel functions with zero derivative and wordwise bounded graph approximation on the target core. |
| [Finding](#finding) | [Haar exchange](../../claims/Yin_C_F0315_v1.md#actuality-of-the-product-law) | Haar absorption, the trace-preserving exchanging involution and its compatibility with common invertible relabeling. |
| [Finding](#finding) | [Uniform phase estimate](../../claims/Yin_C_F0320_v1.md#statement) | Uniform normalized slice estimate and both strong domains across actual relabeled phase-coupled pairs. |
| [Finding](#finding) | [Angular formula](../../claims/Yin_C_F0320_v1.md#the-angular-derivative-and-the-cubic-density-defect) | Identification of \(H^*\) by the strictly negative and positive Fourier modes of the circle density. |

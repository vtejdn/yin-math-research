---
author: Yin
---

# Review of the critical spectral-decay example for rectangular estimates

## Finding

At 2026-11-16T18:26 UTC a separately assigned agent for Yin independently reviewed the entire C_F0331 v1 candidate fixed at 18:25 UTC.
The reviewer did not develop the proof and received the fixed mathematical inputs without development dialogue, author explanations, exploration notes or prior findings on this candidate.
The example realizes the critical spectral decay and semicircular approximation at both coordinates, has the stated strong domains, and makes the integrated minimum of the three specified bounds infinite.

In the finite-kernel identity, the composition of \(k\otimes k\) with itself is \(\|k\|_2^2(k\otimes k)\), and its row is \((\tau k)k\).
Put \(v=E_bu-u\eta_b\).
The row term contains \(2(\tau k)\operatorname{Im}\tau(ku^*v)\) because \(\tau(k\eta_b)\) is real.
Completing the square against \(i(\tau k)uk\) bounds this term minus \(\|v\|_2^2\) by \((\tau k)^2\|k\|_2^2\).
For \(k=\sqrt R\,e-f/\sqrt R\), subtracting that upper bound from the weighted diagonal lower bounds yields exactly (2), since the four rectangles in the vacuum norm are orthogonal and their squared multipliers are \(R^2,R^{-2},1,1\).
The choice \(R=s/t\) centers \(k\).
Keeping the mean square and \(B/(Rs)\), then minimizing \(Rt^2+(s^2+B/s)/R-2ts\), gives (3) for every choice of the two sets.

There are \(1/(4r_j)\) candidate pairs in the aligned grid.
For an old hole of length \(\ell\), at most \(\ell/r_j+6\) centers lie within \(2r_j\).
Counting rejected pairs by these centers gives a discarded fraction bounded by \(\sum_k p_k+6r_j\sum_{k<j}r_k^{-1}<1/16\), using \(r_{j+1}=r_j^4\) and \(r_1=2^{-40}\).
The real interval of length \(r_j/50\) about a retained first center has no old hole and loses at most \(p_jr_j\) at the current stage.
For a later level its intersecting holes have total length at most \((2+r_j/r_k)p_kr_k\), even when a boundary hole extends into the interval.
Summation leaves at least \(r_j/100\) of real mass.
The two assigned segments have inverse parameters differing by \(d_j+O(p_j r_j)\); their centers and lengths leave spatial gaps comparable to \(r_j\).

The density on each high layer is at most \(50p_j\), so summing its \(L^\infty\) norm over the layers, including the bulk, gives linear ball growth.
The same sum controls the sum of Lebesgue \(L^2\) norms since horizontal support has length at most one.
For vertical difference \(y\) and \(c=(y^2+\delta^2)^{1/2}\), the two Fourier multipliers of \(x/(x^2+c^2)\) and \(y/(x^2+c^2)\) have sup norms at most \(\pi\) and \(\pi|y|/c\).
The total convolution on each output line consequently has uniformly bounded Lebesgue \(L^2\) norm.
Weighting and summing the output lines gives a uniform regularized \(L^2(\sigma)\) bound.
The conjugate of a weakly convergent subsequence, with the factor two from antisymmetrization, represents the double-trace limit on every polynomial.
This proves actuality on the represented marginal core.
On different components, the horizontal error in the inverse parameter is \(O(\sqrt{r_j})\) at a level \(j\) point, while all off-component distances from it are at least \(c' r_j\).
The linear ball bound gives an off-component inverse-square potential at most \(C/r_j\).
Squaring the error and integrating thus costs at most a constant times that layer's mass, with the other endpoint accounted for by symmetry.
The horizontal coordinate contributes a bounded secant and same-component inverse parameters are uniformly Lipschitz.
These estimates give the finite secant energy and global one-half Holder bound.

For the second geometry \(\sum q_n=1\).
Off-pair inverse-square potentials are uniformly bounded by the mass and the \(2^{-\min(n,k)}\) gaps.
The same-pair costs for squared maximal density and curvature are bounded by \(C\sum q_n^3/R_n^2<\infty\).
The parameter oscillation \(q_n\), together with the \(Cq_n/R_n\) same-segment Lipschitz bound and the opposite-segment gap \(R_n\), gives a uniform one-half Holder constant and secant energy bounded there by \(C\sum q_n^4/R_n^2<\infty\).
On the unit template the same-line interactions in the normalized kernel are at most two and the opposite-line interactions at least \(4/(1+10^{-4})^2>2\).
Equal masses thus give a strictly negative Rayleigh quotient for opposite constant signs.
Scaling and normalizing the signed test on pair \(n\) gives an internal quotient at most \(-c q_n^2/R_n^2\), tending to minus infinity, while the third points outside the pair give a uniformly bounded correction.
Mixture, similarity and the separated semicircular components preserve this divergence.
If a positive square sum plus a Hilbert kernel represented \(g\), dominated convergence for each fixed bounded test would retain positivity of the square sum and give a uniform lower Rayleigh bound from the Hilbert norm, contradicting these quotients.

The main and return semicircular parametrizations have different imaginary parts and the exceptional geometry is separated horizontally from both.
Their inverses are Lipschitz on each semicircular component by boundedness of the density.
The combined circle inverse has finite secant energy and is globally one-half Holder.
The scalar vacuum on each diagonal block receives a factor equal to its mass, while scaling the exceptional block divides its normalized vacuum by \(d\).
The cross terms have coarse norm \(O(\sqrt{p+q}/d)\), explaining the order of parameter choices in the joint Hilbert estimate.
The continuous periodic reference has semicircular law on both traversals.
Its difference from the actual map in sup norm is small by the modulus of the semicircular quantile, the width of the exceptional interval and the spatial displacements of order \(d\).
After fixing these parameters, uniform convergence of the circle quantile for the smooth two-mode product law and Laurent approximation of the continuous reference give the second coordinate's operator-norm comparison in the same tracial extension.
The graph transfer and exchange give the actual pair, exact two-marginal traces and strong domains.
The joint vacuum differs from its marginal projection in squared norm by \(\|H\|_2^2\) times the fixed finite secant energy.
The uniform phase theorem gives the absolute normalized slice bound independently of the chosen geometry.
Since \(\|H\|_\infty\le2a\), \(\|H\|_2>0\) and the joint spectral density is \(\|H\|_2^2|h(z)-h(w)|^2\), decreasing \(a>0\) after fixing the geometry gives (1), the required vacuum proximity and small operator-norm gradients simultaneously.

In the selected disk windows no older horizontal line can participate at sufficiently large \(j\).
For each later or current layer \(k\), the angular lower threshold restricts the real displacement from \(v\) to a fixed multiple of \(r_k\), which meets only a bounded number of the segments on that grid.
The captured lower mass is thus \(s\asymp p_jr_j\) and the surviving real bulk gives \(t\asymp r_j\).
Across the two specified segments the phase separation is at least a fixed multiple of \(\sqrt{r_j}\) after grafting, hence \(B\gtrsim_a p_j^2r_j^3\).
In (3) the term \(B/s\) is at least a positive multiple of \(p_jr_j^2\), whereas \(s^2=O(p_j^2r_j^2)\).
This gives the lower bound \(c_a r_j^2\sqrt{p_j}\) on the optimized cost at large \(j\).
The Hilbert-kernel cost is at least \(c r_j\sqrt{p_j}\).
Any supporting square for the nonzero symmetric rectangle includes both positive-mass levels modulo null sets, giving a localized cost at least \(3(t+s)^2\).
The stated minimum therefore retains the optimized-order lower bound.
The \(v\)-mass, center area and weighted radial window give measure at least \(c/r_j\) per retained center.
Center neighborhoods are disjoint within a level and the radial windows are disjoint across levels.
There are at least \(c/r_j\) centers, so the lower sum dominates \(\sum_j\sqrt{p_j}\), which diverges.
The ten dependency interfaces were checked at their uses.
The general operator-domain implication at critical decay remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0331_v1.md#decision-candidate) | Entire fixed 18:25 UTC candidate and its mathematical inputs. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0331_v1.md#statement) | Uncentered optimized rectangle estimate, failure of three integrated costs and any positive block decomposition, critical liberation decay and the actual bounded-slice pair. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0331_v1.md#argument) | Complete energy, grid, convolution, parametrization, signed Rayleigh, semicircular graft and disjoint-window arguments. |
| [Finding](#finding) | [Rectangular representation](../../claims/Yin_C_F0329_v1.md#integrating-the-two-block-estimate) | Angular levels, disk-center and radius measure, represented curvature and its Dini comparison. |
| [Finding](#finding) | [Phase realization](../../claims/Yin_C_F0329_v1.md#a-phase-coupling-that-distinguishes-the-two-arcs) | Actual derivatives after relabeling, exchange, exact marginal trace, spectral density and bounded nonzero angular vacuum. |
| [Finding](#finding) | [Finite kernel energy](../../claims/Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) | Exact signed row and composition terms for a rank-one real kernel on either analytic test. |
| [Finding](#finding) | [Diagonal energy](../../claims/Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Signed lower bounds for bounded Borel diagonal projection kernels. |
| [Finding](#finding) | [Localized cost](../../claims/Yin_C_F0297_v1.md#statement) | Localized supporting-square estimate, including its \(3t^2\) term, and scope of the earlier indefinite template. |
| [Finding](#finding) | [Absolute kernel cost](../../claims/Yin_C_F0326_v1.md#statement) | Hilbert cost for a symmetric disjoint rectangle and the positive-square plus Hilbert remainder criterion. |
| [Finding](#finding) | [Marginal actuality](../../claims/Yin_C_F0255_v1.md#statement) | Actual scalar vacuum for the second geometry from squared maximal density and finite total curvature. |
| [Finding](#finding) | [Mixed-gap vacuum](../../claims/Yin_C_F0305_v1.md#the-distinguished-derivative-before-smoothing) | Weighted diagonal vacuum and the twice-kernel norm estimate on the separated graft components. |
| [Finding](#finding) | [Exact joint energy](../../claims/Yin_C_F0265_v1.md#statement) | Orthogonal joint-minus-marginal vacuum norm from the finite secant integral and angular vacuum. |
| [Finding](#finding) | [Absolute phase bound](../../claims/Yin_C_F0320_v1.md#statement) | Uniform normalized right-slice cost for both coordinates of the actual relabeled phase model in both orientations. |

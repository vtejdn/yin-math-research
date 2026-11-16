---
author: Yin
---

# Independent review of the mixed curvature measure criterion

## Finding

On 2026-11-16T18:39 UTC a reviewer outside proof development independently examined the [candidate decision](../../claims/Yin_C_F0332_v1.md#decision-candidate) dated 2026-11-16T18:36, with \(0\le M<\infty\) in the reviewed statement.
The reviewer received the fixed mathematics and its scope without proof-development discussion or a prior finding on this candidate.
The proof establishes (2), the bounds for both oriented slices, the asserted domain inclusions and the applications, including the nonnecessity example.

On a grid of mesh \(\delta\), both endpoint balls for a pair in a single cell are contained in an enlarged square of diameter \(O_A(\delta)\).
The spectral density inequality bounds the self-rectangle divided by the squared cell mass by \(2M\) times the measure of that enlarged square.
Bounded overlap and continuity from above give (3) for compact sets.
Countably many disjoint compact subsets carrying the full restricted marginal mass give the Borel case, using separate meshes and summable errors.

Fix the larger endpoint \(E\) and subdivide the smaller one.
For masses \(t,s_i\) and the notation \(D,D_i,C_i\) of the proof, the centered-square contribution is exactly
\[
 \frac{s_i^2D/t^2+t^2D_i/s_i^2+C_i}{t+s_i}.
\]
This is at most \(s_iD/t^2+tD_i/s_i^2+C_i/t\).
After including the two diagonal terms, the \(D\)- and cross-rectangle contributions sum to \(O(Ms\,\lambda(bB))\), since the parent disk bounds the density on \(B^2\).
The \(D_i\) terms sum to \(O_A(Mt(\lambda(F)+\epsilon))\) by (3).
Normality of the pairing on bounded kernels handles the countable disjoint sum, and \(\epsilon\downarrow0\) followed by interchange of the endpoints gives (4).
Its right side is measurable in the disk and thresholds, independently of the partitions.

For the normalized law of either angular component on \(B\), the quantiles at \(U,1-U\) realize the upper and lower threshold events as nested upper intervals in \(U\).
This gives joint probability \(\min(t,s)/\mu(B)\) even at atoms.
Threshold integration gives the triangular area \((P_+-P_-)_+^2/2\).
Inserting an arbitrary constant bounds the resulting integral by twice the unnormalized marginal variance about that constant.
Averaging over constants from \(bB\) with \(\lambda\) cancels the prefactor \(\lambda(bB)\).
The other two terms of (4) give the two complementary orders in \(\frac12\int_{B^2}|p(z)-p(w)|^2\,d\mu(z)d\lambda(w)\).
Null marginal disks and zero control mass in the enlarged disk contribute zero to their respective terms.

For \(z\ne w\), the center area bound \(\pi r^2\) and the necessary radius \(r\ge |z-w|/(1+b)\) bound the enlarged disk integral by \(C_b/|z-w|^2\).
Combining the real and imaginary angular components gives exactly \(|z-w|^2\kappa(z,v,w)^2\) in the numerator.
Coincidences have product measure zero by diffuseness of both marginal integration variables, including when \(\lambda\) has atoms.
Thus Tonelli bounds the integrated loss by \(C_A M I_\lambda\).
The positive disk representation identifies the numerator on truncated radii, and the integrable gap-weighted square of \(g\) yields convergence on the analytic unitary tests.
The signed energy inequality controls each oriented right slice on the entire core by \(C_A(\|\xi\|_2+\sqrt{M I_\lambda})\), which supplies both domain inclusions at the distinguished coordinate.
The ball convention is immaterial off the null diagonal after strictly increasing \(A\).

Actual scalar conjugacy gives the mixed integral directly for \(\lambda=\mu\).
On a compact Lipschitz graph over a finite interval, parameter length gives the required lower mass at every endpoint scale, including near the ends of that interval.
The parameter law has an \(L^3\) density, and adding length preserves that condition.
The scalar criterion applied to their normalized sum therefore bounds its nonnegative mixed term.
For planar area on a containing disk, the near and far parts of the area integration give a logarithmic bound in the inverse endpoint separation.
Integrating the logarithm against the two marginal variables costs at most a constant times \(1+\int M_1\mu\,d\mu\) by the ball bound and layer integration.

For the critical example I checked both parts of the exceptional graft and the separated semicircular components.
On a single short segment the phase increment is bounded by a constant times the marginal mass out to that parameter displacement, by linearity of its parametrization.
Between distinct components of the grid the squared phase increment is \(O(|z-w|^2+r_j+r_k)\).
Area controls its quadratic term, and the separated heights and interior projection onto the real base guarantee that an enlarged ball collects base length comparable to either nonzero height.
In the straight doublets the control ball covers a segment of mass comparable to \(q_n\) within a pair, while different pairs have parameter changes \(O(q_n)\) and spatial separation at least a constant times \(2^{-n}\) for the earlier index \(n\).
The separated constituents and real Lipschitz inverse branches are covered by the area term.
Adding the real base length to the horizontal-layer component adds one bounded line density to the summable family.
The uniform regularized Cauchy estimates persist, and the fixed positive gaps to the remaining components preserve the normalized-sum scalar vacuum.
Hence the resulting control measure has finite mixed integral.
The cited example's divergent unsubdivided numerical costs and negative curvature Rayleigh quotients concern those quantities, while (2) bounds the actual signed loss.

In the two-arc example the phase is separated on the two opposite arcs of each group and the noise vacuum is nonzero.
This gives a fixed positive density lower bound on each opposite-arc rectangle of positive marginal product measure.
For fixed \(A\), both control balls on that rectangle lie in \(B(2^{-n},C_A2^{-3n-12})\).
Those disks are eventually disjoint.
For \(M>0\) condition (1) would force a fixed positive mass on each disk, contradicting finiteness of \(\lambda\), and \(M=0\) contradicts the density lower bound directly.
The example has exact product two-marginal traces, strong duals and bounded normalized costs.
The review checked all nine declared dependency interfaces and the uses of both examples.
The unrestricted normal implication remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0332_v1.md#decision-candidate) | Complete fixed candidate with nonnegative finite \(M\) and its nine declared inputs. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0332_v1.md#statement) | Mixed-measure criterion, both orientation and domain conclusions, graph corollary, critical example and nonnecessity. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0332_v1.md#argument) | Smaller-endpoint partition, exact rectangular expansion, strict quantile events, enlarged disk integration, gap limit and all geometric applications. |
| [Finding](#finding) | [Signed rectangles](../../claims/Yin_C_F0326_v1.md#statement) | Unequal-trace block estimate with the centered-square cross term before summation. |
| [Finding](#finding) | [Disk representation](../../claims/Yin_C_F0329_v1.md#integrating-the-two-block-estimate) | Positive threshold and disk formula, normalization, truncated pairing and analytic test limit. |
| [Finding](#finding) | [Matched energy](../../claims/Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Coarse gap convergence and passage from the uniform signed lower bound to both original slices and domains. |
| [Finding](#finding) | [Scalar criterion](../../claims/Yin_C_F0255_v1.md#statement) | Maximal density, squared curvature and mixed terms in normalized sums of finite measures. |
| [Finding](#finding) | [Graph parameter law](../../claims/Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Necessity and sufficiency of the cubic parameter-density condition on a Lipschitz graph. |
| [Finding](#finding) | [Critical example](../../claims/Yin_C_F0331_v1.md#statement) | Actual spectral density and the previously constructed divergence of unsubdivided bounds and negative curvature Rayleigh quotients. |
| [Finding](#finding) | [Horizontal layers](../../claims/Yin_C_F0331_v1.md#a-critical-phase-on-a-dense-collection-of-horizontal-segments) | Phase slopes, heights, separations, and preservation of the scalar vacuum after adding parameter length. |
| [Finding](#finding) | [Straight doublets](../../claims/Yin_C_F0331_v1.md#a-disjoint-component-that-excludes-positive-diagonal-decompositions) | Mass, within-pair and across-pair phase oscillations and separations used by the three control measures. |
| [Finding](#finding) | [Opposite arc groups](../../claims/Yin_C_F0329_v1.md#a-phase-coupling-that-distinguishes-the-two-arcs) | Positive spectral density on opposite tiny arcs, product two-marginal traces and bounded normalized costs. |

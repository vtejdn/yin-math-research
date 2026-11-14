---
author: Yin
---

# Independent review of finite planar networks with unrestricted tangencies

At 2026-11-14T11:36 UTC, an agent outside development of this proof reviewed the [candidate fixed at 2026-11-14T11:35](../../claims/Yin_C_F0248_v2.md#decision-candidate) for Yin.
The reviewer had previously inspected the [distinct-tangent version](Yin_R_F0257_v1.md#finding) independently.
This review examined the full v2 argument using its fixed text and mathematical inputs, without exploration notes, proof-development discussion, author explanations or an earlier v2 review.
The earlier review covered the unchanged localized v1 estimates.
Their applicability to the present geometry and the new same-tangent estimates were checked here.

## Finding

The argument establishes finite original column cost at the distinguished coordinate in both orientations for every network in the statement.
Its positive-height estimates require neither a power-law comparison at a vertex nor monotonicity of the height.
The two original canonical domains and the all-coordinate equivalence follow at the stated scope.

**Geometry and encoding.**
Separate short pieces at the ends of each old edge leave only one possible common vertex for any pair after the finite subdivision.
For each equal-tangent pair, projection onto its common outgoing direction has derivative bounded below on both initial pieces.
The two graph heights have equal value and slope at the vertex and strict order at every other common abscissa, by disjointness.
Their half-difference \(d\) is positive on \((0,R]\), with \(d(0)=d'(0)=0\).
After equalizing projected lengths or shrinking the common interval to \(u>0\), any part of the cross rectangle with at least one variable in the excess pieces has positive planar separation by compactness.
The construction applies to each pair separately in the presence of additional incident branches.

The recursion \(\ell_n=c\,d(x_n)\) gives \(0<\ell_n<x_n/2\) by the Lipschitz bound and forces \(x_n\downarrow0\) by continuity and positivity of \(d\).
Throughout each tile, \(d(x)\) lies within \(d(x_n)/2\) of \(d(x_n)\).
Writing \(t=x-x_{n+1}\) gives \(F_\pm(x)-10x=b_\pm\ell_n-9t\), hence the stated bound by a fixed multiple of \(d(x)\).
The images of the two labelled intervals occupy offsets \((1,2)\ell_n\) and \((4,5)\ell_n\).
Their intervening gap has length \(2\ell_n\), and the gap between successive tiles has length \(5\ell_{n+1}+\ell_n\).
In both cases the displacement of the endpoints in the plane is bounded by a constant times that length.
The uniform Lipschitz bound extends across the accumulation point at zero by continuity and across the finitely many remaining pieces by positive parameter separation.

Removing the countably many endpoints preserves both spectral legs by diffuseness.
On the remaining support the assigned real labels have a Borel inverse and the decoder is Lipschitz, even if its interpolating segments intersect its image elsewhere.
Mesh-cell images thus have separate disk centers, disjoint spectral projections and radii bounded by the mesh times the decoder constant.
The packing estimate and the weak limit of the \(L^3\) histograms give the actual scalar vacuum for the real parameter.
For the invariant liberation vacuum the decoder inequality bounds the new inverse-square-gap energy by its original finite value times the squared Lipschitz constant.
The unchanged omitted algebras and their energies restore full actual ACSY on the new mixed core, to which the real-coordinate column bound applies.
These uses of C_F0250 depend only on the verified encoding properties.

**Comparable heights.**
The periodic extension of the cut-off \(g'(ut)\) has square-integrable weak first derivative across \(t=0\) because \(g'(0)=0\).
Both its size and its derivative on the fixed support are \(O(u\|g''\|_\infty)\).
The absolute sum of its Fourier coefficients therefore has the same bound by Cauchy–Schwarz.
After evaluation at \((\theta x+(1-\theta)y)/u\), the two factors of each character have modulus one.
The resulting bound on \(G\) makes \(K_0=(1+iG)^{-1}\) a single bounded Schur symbol on the whole small square.

For \(D_0=v+i(d_x+d_y)\), the integral of \(e^{-\lambda(d_x+d_y)+i\lambda v}\) is \(i/D_0\).
The stated two factors with the square-root weights each have \(L^2(d\lambda)\) norm \(1/\sqrt2\), giving multiplier norm at most \(1/2\) for \(i\sqrt{d_xd_y}/D_0\) on arbitrary branch measures.
In bands separated by at most one index the ratios of the extreme heights are bounded by four, so the separated square-root factors recover \((d_x+d_y)/D_0\) with a uniform bound.
They recover \((\epsilon_+(x)-\epsilon_-(y))/D_0\) by the same estimate on each one-variable error.
Since \(v/D_0=1-i(d_x+d_y)/D_0\), shrinking \(u\) makes \(iGv/D_0\) small in multiplier norm on every such rectangle.
The inverse of \(D/D_0=1+iGv/D_0\) and hence \(K\) have uniform bounds there, including points with \(v=0\).
For each of the three offsets, orthogonal input projections and orthogonal output projections give a direct sum of compressed operators, bounded by the supremum of the block bounds.
Flat levels and disconnected height bands preserve these projection properties.

**Separated heights and summation.**
The test point \(x-d'(x)/M_0\) stays in \([0,2u]\), since \(d'(0)=0\) and \(|d'(x)|\le M_0x\).
Taylor's upper bound at that point is \(d(x)-|d'(x)|^2/(2M_0)\), which must be nonnegative.
Hence \(\sqrt d\) has derivative bounded by \(L_0\) on the positive interval and is \(L_0\)-Lipschitz through the endpoint.
This verifies the localization of the cited square-root estimate under the actual one-sided hypotheses. [Glaeser, Lemme I and the attribution to Malgrange](../literature/Gla63/readme.md#lemme-i)
If one height belongs to \((\delta/2,\delta]\) and the other is at most \(\delta/4\), then the square roots differ by at least \((1/\sqrt2-1/2)\sqrt\delta\).
It follows that \(|v|\ge b\sqrt\delta\), independently of which variable has larger abscissa.
The cutoff quotient \(\phi\) belongs to \(H^1(\mathbb R)\) and \(\widehat\phi\) to \(L^1\), so rescaling its Fourier representation gives a multiplier equal to \(1/v\) throughout this whole higher/lower rectangle at cost \(O(\delta^{-1/2})\).

With \(A=d_x+d_y\), \(\|A\|_{\rm Schur}\le2\delta\) on that rectangle.
The norm of \(G\) and the bound \(O(\sqrt{D_*})\) on \(A J_\delta\) tend to zero with \(u\).
One choice of \(u\) therefore suffices for all the inverses, since \(M_0,b\) can be fixed on the initial chart.
Writing \(Q=1+iG+iA J_\delta\) gives \(K=(10+(\epsilon_+-\epsilon_-)J_\delta)Q^{-1}\).
Subtracting \(10K_0\) leaves the numerator \((\epsilon_+-\epsilon_- -10iK_0 A)J_\delta\) times \(Q^{-1}\).
The first factor before \(J_\delta\) costs \(O(\delta)\), proving the required \(O(\sqrt{\delta})\) bound simultaneously for all the lower bands with this higher band fixed.
Each such symbol has a bounded extension by zero via the two compressions.
For both possible placements of the higher band the series of these norms is bounded by a constant times \(\sum_{j\ge0}2^{-j/2}\sqrt{D_*}\).
Adding the comparable-offset corrections to the same global baseline covers the entire positive-height cross rectangle.

**Original coordinates and domains.**
Pullback along the two label assignments identifies the two measured branch spaces, and the transpose controls the reverse orientation.
The old-core Schur insertion bound acts on full finite mixed columns at the real parameter.
The forward Lipschitz decoder permits norm-controlled approximation in its derivation graph before application of the bounded cross symbol.
On the original distinguished generator this localized symbol cancels its forward divided difference, including the rotation factor.
On the starred generator it leaves the forced original phase, and both derivations kill the omitted starred letters.
The outer Leibniz rule gives equality on the original mixed core and passage to the graph limit gives the original rectangle estimate.
For the same-piece and distinct-tangent rectangles only a chosen projection chart must be regular, since other pieces can occupy separate parameter intervals.
The remaining positive-distance pieces use the original separated Fourier estimate.
Thus the countably many tiles occur only within an already bounded multiplier, and a finite sum of rectangle bounds suffices on the original core.
Reflection gives the original one-input left bound by flip-adjoint.
The two-slice theorem puts \(M\Omega\) in the domains of the canonical closure and its adjoint.
Boundedness of \(X_j\) and of the core commutator permits extension of the generator-first identity to the negative closure by graph convergence.
For the reverse implication the strong duals restrict to full-domain maps and \(\Omega\) belongs to each adjoint domain, meeting parts A and C of C_F0070.
No cost uniform in the geometry or the law follows, and carriers with infinitely many intersections lacking a finite subdivision lie outside this result.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Network statement](../../claims/Yin_C_F0248_v2.md#statement) | Finite regular networks with arbitrary tangencies, distinguished columns in both orientations, original domains and the all-coordinate equivalence. |
| [Finding](#finding) | [Network argument](../../claims/Yin_C_F0248_v2.md#argument) | Whole v2 proof, including adaptive labels, one-sided square-root estimate, both height-band bounds, common baseline, original mixed-core transfer and finite assembly. |
| [Finding](#finding) | [Prior subdivision](../../claims/Yin_C_F0248_v1.md#a-finite-subdivision-admitting-pairwise-graph-charts) | Finite separation of original ends and monotone charts where applicable at single pieces or pairs of distinct tangents. |
| [Finding](#finding) | [Prior local rectangles](../../claims/Yin_C_F0248_v1.md#returning-the-localized-derivation-to-the-original-tuple) | Local single-piece and distinct-tangent estimates and original positive-distance recovery regardless of tangencies elsewhere. |
| [Finding](#finding) | [Real encoding](../../claims/Yin_C_F0250_v1.md#a-real-parameter-interleaving-the-two-branches) | Conull Borel inverse and Lipschitz decoder suffice for real density and actual vacua, after direct verification for these new tiles. |
| [Finding](#finding) | [Real-coordinate columns](../../claims/Yin_C_F0246_v1.md#the-real-parameter-and-its-original-column) | Original finite-column bound on the actual parameter tuple with arbitrary normal omitted coordinates. |
| [Finding](#finding) | [Measurable Schur factors](../literature/AP25/Yin_U001.md#ap25-u001) | Two bounded factors in \(L^2(d\lambda)\) give the product-measure Schur bound for the branch spaces. |
| [Finding](#finding) | [Original localized transfer](../../claims/Yin_C_F0250_v1.md#recovery-of-the-original-columns) | Schur insertion, norm-controlled approximation, forced generator values, reversed and same-piece rectangles. |
| [Finding](#finding) | [Canonical domains](../../claims/Yin_C_F0072_v1.md#statement) | Part B for the original right slice and its actual adjoint using estimates in the two orientations. |
| [Finding](#finding) | [Converse for normal tuples](../../claims/Yin_C_F0070_v1.md#statement) | Parts A and C applied to the restriction of strong full-domain duals with vacuum in each adjoint domain. |

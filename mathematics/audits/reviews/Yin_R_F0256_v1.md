---
author: Yin
---

# Independent review of the column estimate for graphs with bounded slope variation on each dyadic shell

An independent agent for Yin reviewed the complete [candidate dated 2026-11-14T11:05](../../claims/Yin_C_F0247_v1.md#decision-candidate) and its direct inputs.
The reviewer did not participate in developing this proof and received no development dialogue, author explanations or previous conclusions about this candidate.
The existing review of the bounded-variation input concerned the preceding claim.
I checked the input itself and the new localization and summations against the fixed candidate.

## Finding

At 2026-11-14T11:07 UTC I found that the candidate proves (1) with \(C(L)(1+V)\) uniformly over the stated vertices, scales, tuples and finite columns.
It also establishes the actual vacuum, both orientations, the domains of the original closure and its Hilbert adjoint, the commutator with the stated sign, the simultaneous application and the non-Schur example.

The old real-coordinate estimates apply to the original represented starred core and give \(c(C\delta)\le4\|\xi\|_2\) and \(\|\rho\|_3^3\le C_0\|\mathbb E_N\xi\|_2^2\).
For fixed \(b,J,D\), the compressed liberation norm squared is the joint measure of the compression square.
For a pair of distinct spectral points in that square of gap \(u\), the sum of \(d_n^{-2}\) over \(d_n\ge u/2\) is at most \(16/(3u^2)\).
The joint liberation measure has zero diagonal mass, so integrating this bound over \(J^2\) gives its part of (2).
The \(\rho^3\) integral is localized to \(J\) as well, since the length estimate for each shell and the \(\ell^3\) convolution apply to its intersection with \(J\).
Diffuseness gives \(\mu(\{b\})=0\), so the shell masses account for the full compressed trace.
Thus the same numerical constant applies to all the interval hulls, and the global squared energy is bounded by an absolute multiple of \(\|\xi\|_2^2\).

On a hull of finite slope variation, the Stieltjes formula uses only the slope derivative in its open interior.
For \(s,t\) straddling \(b\), the two signs of \(s-t\) in the average-slope calculation give the displayed kernel \(J_b/(s-t)\) on the liberation derivative.
The two Laplace parameters each give decay at rate at least \((d_n+d_k)/2\) for second shells \(k<n\), and at least \(d_n/2\) for the whole inner second range.
The numerator is at most \(d_n\) in modulus.
Multiplication by the block bound costs at most a constant times \(2^{k-n}A_k\) or \(A_n\), respectively, since the two projections in each block are orthogonal and their join lies in the corresponding ball inside \(J\).
For each separated symbol the product-rule correction \(pG(w)\) obeys the same column estimate as \(G(pw)\), using \(\sum_m\|p_m G(w)\|_2^2\le\|\sum_m p_m^*p_m\|\|G(w)\|_2^2\).
Bounded graph approximation of the marginal factor for liberation permits the Borel restrictions in this calculation.
The first inner projection remains on the right of the slice, giving Hilbert orthogonality across disjoint first shells.
Convolution by the summable \(2^{-d}\) on \(\ell^2\) therefore gives the bound \(C U(J)\) at each \(b\).
The truncations act on each \(\delta(p_m)\) by bounded symbols, and the inner spectral measure of this vector is absolutely continuous with respect to \(\mu^2\).
Joint measurability in the cyclic spectral space of each vector and integration against the finite variation measure give (3), including singular variation and boundary jumps interior to a hull.

Subtracting the apex reciprocal \(Q(y)^{-1}\) from the secant and dividing by \(x-y\) gives exactly (4).
For \(k\ge j+N\), the independent supremum bounds on the two ratios are \(2^{1-N}\) and \(B2^{1-N}\) throughout the single block containing all those second shells.
Expanding the two geometric series costs at most four times the separated norm products of the remaining factors, which are bounded by \(C(B)/r_j\).
For \(k\le j-N\) the reversed expansion has the extra factor \(r_j/r_k^2\) and hence yields \(2^{k-j}A_k\) after the liberation estimate.
This asymmetric grouping avoids counting a fixed first-shell cost once for each smaller second shell.
For opposite signs in the remaining offsets, the real parts of both Laplace exponents supply decay at rate at least \((r_j+r_k)/2\).
With \(m=\min(j,k)\), the resulting \(r_j/(r_j+r_k)^2\) times \(r_m A_m\) is at most \(A_m\).

For a fixed offset \(d=k-j\) and common sign, the closed hull contains \(|d|+1\) shell interiors and \(|d|\) intervening slope jumps, each of size at most \(2L\) by the bounded one-sided slope traces.
Away from the endpoints each first point belongs to at most \(|d|+1\) such hulls.
This also bounds the overlap for the first marginal of the joint liberation measure by normality of spectral multiplication.
Consequently the squared \(U(J)\) are summable with this multiplicity even when the total slope variation diverges at the apex.
For the remaining term the mask acts on an integral operator \(T\) by \(\sum_j 1_{E_j} T 1_{F_j}\).
The orthogonality of each projection family bounds its operator norm by \(\|T\|\), and the second-variable multiplier has norm at most two.
The first-shell projections for distinct \(j\) are orthogonal at each fixed offset.
All sums converge on the original coarse vectors by bounded truncations, and the number of offsets depends only on \(L\).
These checks give precisely the claimed linear dependence on \(1+V\), including at an apex in the spectral support.

The graph scalar-vacuum criterion applies to the compact real \(L^3\) density, and \(|h(s)-h(t)|\ge|s-t|\) controls the transported inverse-gap integral.
Injective Borel relabellings on conull sets preserve all marginal algebras and the partial liberation vacuum.
On the new mixed core the bounded secant carries the old closed derivation to the prescribed target one.
The simultaneous column cutoff in the cited graph approximation controls the input norm by \(1+\varepsilon\) in the limit and requires only boundedness of the secant at this transfer step.
Applying the argument with \(-g\) on the adjoint tuple gives the same right-column constant and, by flip-adjoint, a left single-input bound for the original derivation.
Part B of the two-slice theorem now applies on the weakly dense represented core.
The product rule gives \(E(Y_jp)=Y_j E(p)+\delta_{ij}\tau(p)\Omega\), and passage to the closed graph gives \([Y_j,-\bar E]=\delta_{ij}P_\Omega\) there.
Applying the distinguished result separately to each original selfadjoint coordinate permits arbitrary correlations.

In the example the tent slopes are \(1/2\) and \(-1/2\), its interior jump has magnitude one in every positive shell, and continuity across shells and at zero gives a globally \(1/2\)-Lipschitz odd extension.
At the two sampled phases \(Q\) takes the values \(1\) and \(\beta=1+i/6\).
For \(j<k\), \(t_k/s_j=(3/4)2^{j-k}\), and subtracting one from the sampled inverse secant gives an error \(O(2^{j-k})\).
For \(j>k\), division by \(t_k\) instead gives an error \(O(2^{k-j})\) from \(\beta^{-1}\) away from the finitely many central diagonals.
Each individual diagonal has multiplier norm bounded by the supremum of its entries, so these errors have bounded Schur norm uniformly in the sample size and starting index.
The test \(D_{jk}=1/(j-k)\) off the diagonal, zero on it, has norm at most \(\pi\).
The pairing of the two-constant triangular multiplier applied to \(D\) with the normalized constant vector on both sides equals \((\beta^{-1}-1)\sum_{d=1}^{n-1}(1-d/n)/d\), which is unbounded.
Every finite configuration starting sufficiently late has distinct nodes in the stipulated support interval.
Its normalized indicator compressions exist for arbitrarily small disjoint neighborhoods because each node is in the support.
Continuity on each of the finitely many off-diagonal rectangles yields convergence to the sampled matrix in operator norm, proving the asserted measurable obstruction for every such marginal.
The cited established results were used at the interfaces listed below, without a new audit of their external proofs.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate decision](../../claims/Yin_C_F0247_v1.md#decision-candidate) | Fixed candidate, including all stated uniformity, orientations and the polygon. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0247_v1.md#statement) | Shellwise variation hypothesis, quantitative column estimate, vacuum, domains, commutator, correlated tuples and non-Schur example. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0247_v1.md#argument) | Complete localization, summation, transfer and obstruction proof. |
| [Finding](#finding) | [ACSY and domain conventions](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Represented starred core and generator-first convention for the strong condition. |
| [Finding](#finding) | [Real-coordinate estimates](../../claims/Yin_C_F0246_v1.md#the-real-parameter-and-its-original-column) | Quantitative original column, diffuse real density and its cubed integral. |
| [Finding](#finding) | [Inverse-gap identity](../../claims/Yin_C_F0238_v1.md#statement) | Old energy of the marginal-orthogonal vacuum component and the target existence criterion. |
| [Finding](#finding) | [Inner spectral measure class](../../claims/Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Product-law domination for truncating coarse symbols. |
| [Finding](#finding) | [Liberation blocks](../../claims/Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Equation (6), compression to the joint spectral ball and right support in the first projection. |
| [Finding](#finding) | [One-vertex estimate](../../claims/Yin_C_F0246_v1.md#a-uniform-estimate-at-one-vertex) | Multiplying a liberation block by bounded separated Borel factors and summing orthogonal outputs. |
| [Finding](#finding) | [Variation identity](../../claims/Yin_C_F0246_v1.md#decomposition-by-the-variation-of-the-slope) | Stieltjes difference kernel on the open interior of each hull, with both crossing orientations. |
| [Finding](#finding) | [Schur slicing](../../claims/Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice) | Separated baseline and disjoint paired masks applied to the old core. |
| [Finding](#finding) | [Graph vacuum](../../claims/Yin_C_F0244_v1.md#argument) | Invariant liberation under omitted Borel changes and sufficiency of the scalar real-parameter density criterion. |
| [Finding](#finding) | [Target graph approximation](../../claims/Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Identification of the target derivation and a single norm cutoff for the graph approximation of a finite column. |
| [Finding](#finding) | [Two-slice theorem](../../claims/Yin_C_F0072_v1.md#statement) | Part B applied to the actual canonical right slice and its Hilbert adjoint. |
| [Finding](#finding) | [Discrete Hilbert-transform test](../../claims/Yin_C_F0241_v1.md#a-logarithmic-lower-bound-for-the-inverse-divided-difference) | Uniform input bound, logarithmic triangular pairing and finite-rank compression. |

---
author: Yin
---

# Uniformity of the disk estimates and transfer through finite spectral labels

## Finding

On 2026-11-16T19:52 UTC a separate agent for Yin checked the passage from the signed angular estimate to the uniform relative projection estimate in C_F0346 v1.
The reviewer had no role in developing the proof and received the fixed Claim and its dependencies, without exploration notes, proof-generation dialogue or an author's explanation.
The inputs include the selected assessment lines printed in the fixed dependencies.
The reviewer did not consult their R findings or use their verdicts to infer the estimates.

The argument gives an absolute constant for a distinguished normal coordinate and a killed trace-half projection on their represented starred polynomial core.
The finite partition with zero liberation mass on its diagonal blocks is needed only in the circle construction.
The checks below include the scalar square function, the conditional projection on all finite-label words and the return from the lattice to the original relative core.

### Matrix and measure estimates

A subcell \(R\) in pivot cell \(l\) has \(\nu(R^2)=0\), so the projection square identity gives \(F_{1_R\otimes1_R}\ge0\).
For the two tests \(k\pm N^{3/4}1_R\), the squared norms divided by \(t_l\sqrt N\) tend uniformly in \(R\) to one at fixed \(l,k\).
Their trace perturbations are bounded by \(t_lN^{-1/4}\).
All terms in the averaged squared vacuum numerator involving two endpoints in \(R\) vanish.
Averaging the surviving single-endpoint integrals over the \(N\) subcells gives the row error \(2\sum_i k_i^2\nu_{il}/t_l\), since \(\nu\) is symmetric.
Replacing the two denominators by their uniform asymptotic equivalent is valid on the nonnegative numerators, whose normalized average is bounded at this fixed partition.

After centering \(p\) for the normalized restriction to \(Q=3B\), the two families of outer products have off-diagonal sum \(-p_i^2-p_j^2+2p_ip_j\) before compression.
Each generating vector is orthogonal to \(t\), which fixes the diagonal since \(t_i>0\).
Compression to \(B\) contributes exactly the single boundary sum over \(i\in B,j\in Q\setminus B\) when tested on \(t\).
The diagonal bound for \(i\ne l\) is \(4(t_l/\mu(Q))1_B(i)\operatorname{osc}_Q(p)^2\).
The possibly large pivot entry is multiplied by \(\nu_{ll}=0\) in the trace.
Pairing the positive factors with \(X_0+D_l\succeq0\) therefore costs at most \(8\operatorname{osc}_Q(p)^2\nu(B\times Q)/\mu(Q)\) in addition to the boundary sum.
Quantization in the range of \(p\) converges uniformly and the fixed analytic test acts continuously on bounded kernels.

For \(z\in B(a,r), w\in 3B(a,r)\), integration in the center and radius costs at most \(\pi\int_{|z-w|/4}^\infty r^{-3}\,dr\).
The squared angular difference includes the compensating \(|z-w|^2\) at every triple of distinct sites.
Thus the boundary sum costs total squared curvature, while the second error on \(T(B)\le K\mu(3B)\) costs the inverse-gap integral against \(\nu\).
On the remaining disks C_F0337 collects the angular factors first.
Its annular telescoping uses \(r\theta(x,r)\le\mu(3B)\) for \(x\in B\).
With \(K>4C_0\) the constant part is absorbed and the squared differences have summable weights \(2^{-j}\).
Area integration and a change of scale give \(L=\int_{\rm bad}\mu(B)T(B)^2\,dA\,dr/r^5\le C G(\mu)\).
The absolute cost is then bounded by \(C(\sqrt{LI}+L)\), with \(I=\int |z-w|^{-2}d\nu\).
The monotone truncations of the nonnegative curvature kernel converge on each analytic test through the two gap tensors, by \(\int |z-w|^2g^2\,d\mu^2\le4\int\kappa^2\,d\mu^3\).

### Uniform square-function constants

Writing \(b(x)^2=\int\kappa(x,y,z)^2\,d\mu(y)d\mu(z)\) and \(f=M_1\mu+b\), the change \(d\sigma=f^{-1}d\mu\) gives \(\sigma(B(a,r))\le2r\).
Assigning each triple to a vertex minimizing \(f\) gives \(\int_{Q^3}\kappa^2d\sigma^3\le3\sigma(Q)\) at every restriction.
The reviewer checked Theorem 19.1 on p. 102 of Tolsa's archived preprint and its curvature packing statement on p. 103.
After fixing the growth bound, the theorem tests the sharp density difference for \(\sigma|_Q\) globally with cost \(C\sigma(Q)\).
The smooth density is an integral of the sharp ones with the fixed weights \(s(-\psi'(s))\,ds\), and scale invariance of \(dr/r\) transfers this testing bound.

Lacey and Martikainen's Theorem 1.3 on pp. 1–2 of their arXiv edition requires a test of mean one on each cube of positive measure, the size condition and Hölder regularity in the integration variable.
The tests \(1_Q\) have exact mean one and squared norm \(\sigma(Q)\), and their testing region is contained in the all-radii test for \(\sigma|_Q\).
The fixed smooth kernel satisfies the hypotheses with \(m=\alpha=1\).
In the scale Hilbert space its size is at most \(C/|x-y|\) and its two first differences are bounded by \(C|\Delta|/|x-y|^2\) when \(|\Delta|\le |x-y|/2\).
Summation on annuli gives both integral Hörmander bounds uniformly.
García-Cuerva and Martell, printed pp. 614, 617 and 626, allow this kernel, its off-support integral formula and the established \(L^2\) bound.
Rescaling \(\sigma\) by \(1/2\) meets their unit upper-growth convention at a fixed cost.
Their Theorem 2.7 at \(p=3\) follows by the \(3/2\) estimate for the Hilbert adjoint and duality, with uniform constants in this family.
Finally \(\int f^3d\sigma=\int f^2d\mu\le2G(\mu)\) yields the original weighted square estimate by Hölder.
This inspection uses the three published theorem interfaces and does not audit their full proofs.

### Both directions of the lattice comparison

Rounding an actual \(Z\) to \(U=\sum_i c_i e_i\) at mesh \(h\) gives \(\|U-Z\|\le h\).
Distinct cells have \(|z-w|\le3|c_i-c_j|\) and conditional expectation onto the rounded algebra contracts the corresponding liberation blocks.
Comparison with the soft Cauchy transform incurs \(O(M_1\mu(x))\) on the nearby cells and a summable \(O(2^{-j}M_1\mu(x))\) in the distant annuli.
These estimates bound \(B_c\) by \(C\|\xi\|_2\).
Off the product-null diagonal the bounded finite-label phases converge to the actual normal phase.
The finite Leibniz expansion therefore converges in the common coarse space and the input norms converge for every fixed word.

Conversely the centered free extension of \(\operatorname{ad}-\gamma\) kills the corner noises and preserves its vacuum.
Subtracting this derivation from \(\operatorname{ad}\) gives partial liberation for the spread coordinate.
In the old vacuum pairing tested at \(e_i p e_i\) the two end corrections cancel, and insertion of \(e_i\otimes e_i\) in \(\gamma p\) vanishes on the generators and hence on words.
Thus \(e_i\eta e_i=0\) independently of the size of \(t_i\).
The new distinct circles are separated by at least \(3|c_i-c_j|/4\).
Their scalar within-circle vacuum contributions are bounded by \(Ct_i/h\le CM_i\), and the errors in the cross-circle Cauchy integrals sum over annuli to \(CM_i\).
The relative vacuum reconstruction therefore costs at most \(CB_c\), including its off-diagonal spectral part.

At distinct centers the circle displacements in \(z-w\) have combined size at most \(h/4\).
The geometric expansion for \(1/(z-w)\) converges uniformly there, and every nonconstant term has a positive power of a centered displacement whose circle mean is zero.
The conditional projection on the two coarse factors thus sends each spread indicator derivative exactly to its discrete derivative.
Bimodularity extends the equality to every represented word in \(P,e_i\).
The required indicator is smooth near the separated spectral components, so first-derivative polynomial approximation gives operator norm convergence on inputs and coarse norm convergence on their derivatives.
The disk bound on the circle models gives \(\|E_c p\|_2\le CB_c\|p\|\) on these graph limits.
Applying rounding to an arbitrary relative projection model then gives its uniform estimate.
Neither direction uses a prior uniform estimate for the entire collection of circle models.

The inspection ends at the relative projection estimate and its stated interface with C_F0308.
It leaves the independent verification of the original canonical operator domains, the converse implication, the affiliated fraction tests and the complete Task to their respective reviews.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Spectral rows on the enlarged disk](../../claims/Yin_C_F0346_v1.md#the-enlarged-disk-in-the-signed-angular-estimate) | Uniform sign averaging at each pivot. |
| [Finding](#finding) | [Compressed positive matrices](../../claims/Yin_C_F0346_v1.md#a-positive-matrix-on-the-larger-disk) | Off-diagonal expansion, pivot cancellation and boundary term. |
| [Finding](#finding) | [Angular integration](../../claims/Yin_C_F0346_v1.md#summation-of-the-angular-kernels) | Good and bad disks, truncation and absolute constants. |
| [Finding](#finding) | [Partition removal](../../claims/Yin_C_F0346_v1.md#removing-the-partition-and-identifying-the-original-operators) | Only the removal of the partition up to the uniform projection bound. |
| [Finding](#finding) | [Uncentered square](../../claims/Yin_C_F0331_v1.md#the-uncentered-square) | Upper bound with the inserted rank-one kernel. |
| [Finding](#finding) | [Projection square](../../claims/Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Lower bound when the projected liberation vacuum vanishes. |
| [Finding](#finding) | [Square function after a change of measure](../../claims/Yin_C_F0337_v1.md#a-change-of-measure-for-the-density-square-function) | Uniform growth, curvature testing, extrapolation and return to the original measure. |
| [Finding](#finding) | [Small local mass](../../claims/Yin_C_F0337_v1.md#disks-of-small-local-mass) | Telescoping at an absolute threshold and aggregate cost. |
| [Finding](#finding) | [Tolsa's square function](../literature/Tol17/Yin_U001.md#the-global-square-function-under-uniform-linear-growth) | Theorem 19.1 under normalized growth. |
| [Finding](#finding) | [Vertical square-function testing](../literature/LM17/Yin_U001.md#indicator-testing) | Theorem 1.3 with the cube indicators. |
| [Finding](#finding) | [Vector-valued kernel](../literature/GM00/Yin_U001.md#operator-kernel) | Definition 2.1 in the scale Hilbert space. |
| [Finding](#finding) | [Vector-valued strong type](../literature/GM00/Yin_U001.md#strong-type) | Theorem 2.7 at exponent three. |
| [Finding](#finding) | [Rounding](../../claims/Yin_C_F0339_v1.md#rounding-an-actual-coordinate) | Uniform discrete budget and convergence on the represented core. |
| [Finding](#finding) | [Free corner noises](../../claims/Yin_C_F0339_v1.md#free-noise-in-each-spectral-corner) | Actual partial liberation vacuum and vanishing equal-label blocks. |
| [Finding](#finding) | [Circle vacuum](../../claims/Yin_C_F0339_v1.md#the-scalar-vacuum-of-the-spread-measure) | Uniform scalar and inverse-gap contributions. |
| [Finding](#finding) | [Circle recovery](../../claims/Yin_C_F0339_v1.md#recovering-the-discrete-derivative-on-circles) | Conditional expectations and graph approximation on arbitrary old words. |
| [Finding](#finding) | [Mixed energy](../../claims/Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Gap-weighted convergence and signed estimate on each analytic test. |
| [Finding](#finding) | [Relative coefficients](../../claims/Yin_C_F0308_v1.md#statement) | Incoming projection constant at the factor-two comparison. |

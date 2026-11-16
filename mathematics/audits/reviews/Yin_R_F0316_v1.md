---
author: Yin
---

# Review of the relative Gaussian vacuum and its uniform slice constant

## Finding

At 2026-11-16T16:19 UTC a separately assigned agent reviewed the complete [C_F0307 v1 candidate](../../claims/Yin_C_F0307_v1.md#decision-candidate) for Yin.
The reviewer did not participate in its development and received the fixed proof and scope without development dialogue, author explanations, exploration notes or prior findings on this candidate.
The equivalence, exact vacuum norm, both \(\sqrt{17}\) estimates, characterization of the null directions and disk example follow under the stated assumptions.

**Free smoothing in both directions.**
The original \(Z\) law is diffuse, so the outer difference at \(Z\) has trivial kernel on the coarse space and the normal relation forces the starred symbol even for the single given derivation.
On the free product of its represented core with the new noise polynomials the derivation extends by the product rule.
For a reduced centered word containing a noise letter, cutting at any original letter puts a centered noise segment on at least one trace leg.
A bounded original tensor multiplying that segment leaves its trace zero by freeness, and approximation gives the same identity for the actual Hilbert tensors.
The vacuum on the original algebra is consequently still the vacuum of the enlarged derivation.
Restricting to \(Z,T^\epsilon\) takes the vacuum to its orthogonal projection because the two marginal symbols and the resulting word derivatives all lie in the smaller coarse space.
The independent semicircular derivatives divided by \(\epsilon\) supply each of the other normalized derivatives there.
The full Gaussian theorem thus computes the projected vacuum norm, including the contribution of \(\xi_N\).
Each polynomial approximating an original Hilbert vector is the norm limit of its evaluations at \(T^\epsilon\), which proves convergence in norm of the projections on original vectors without any nesting.
Conversely, the inverse matrix cost is at most \(q/\epsilon^2\).
Together with bounded regularized two-edge integrals and the scalar vacuum this gives smoothed vacua bounded in the common Hilbert space.
Testing a weak subsequential limit against fixed words is valid because both the word evaluations and the two-symbol derivative evaluations converge strongly.
For a zero relation \(p\), testing \(apb\) pairs its formal derivative with every product tensor from the represented core, which proves descent.
The resulting actual vacuum permits the preceding necessity argument to recover equality of norms.

**Monotonicity and rank.**
Taking the \(ij\) entry between a \(P\)-eigenvector and a \(Q\)-eigenvector yields the overlap times \(t_{j,\epsilon}/s_{i,\epsilon}-s_{i,\epsilon}/t_{j,\epsilon}\), with \(s_{i,\epsilon}^2=s_i^2+\epsilon^2\) and likewise for \(t_{j,\epsilon}\).
Its squared modulus increases as \(\epsilon\) decreases.
The matrix formula is measurable and monotone convergence applies without selecting measurable eigenbases.
A nonzero overlap of a positive eigenspace with the opposite nullspace produces infinite limit off the product-null diagonal.
Finite energy therefore forces the two kernel projections to coincide for almost every triple.
For fixed middle \(w\) this makes the projections at two independent endpoints equal almost surely, so integrating in one endpoint gives a matrix depending only on \(w\).
Edge reversal and integration once more make that matrix constant and invariant under entrywise conjugation.
On this projection both regularized matrices equal \(\epsilon I\), and on its complement the monotone limit gives the positive-matrix integral.
This proves both directions, including the all-zero and full-rank cases.

**The numerical bound.**
For positive invertible \(P,Q\), write \(U=P^{-1}Q-I\), \(V=I-PQ^{-1}\).
The cross term satisfies \(\operatorname{Re}\operatorname{tr}(U^*V)=\operatorname{tr}(QP^{-1}+PQ^{-1}-2I)\ge0\) by the reciprocal eigenvalues of \(QP^{-1}\) and \(PQ^{-1}\), which are positive.
After the indicated variable reversals this gives \(B^2\le\|H\|_2^2\) for the combined degree-one coefficient array.
At each of the two possible suffix degrees the cut colors have orthogonal initial subspaces, giving the single bound \(2\sqrt2 B\) with all colors included.
The fixed free reference map costs \(3\|\xi_N\|_2\).
Cauchy--Schwarz and orthogonality of relative degrees zero and two give
\[
  3\|\xi_N\|_2+2\sqrt2\|H\|_2
       \le\sqrt{17}\,(\|\xi_N\|_2^2+\|H\|_2^2)^{1/2}.
\]
The intrinsic path isometry identifies the two represented operator norms and both coarse generator symbols when passing from a rectangular amplitude to the positive square model.

Clipping eigenvalues from above decreases every absolute log-ratio, so every clipped two-edge density squared is bounded by its unclipped value.
The cross-term inequality also dominates the individual clipped arrays in their respective reversed variables, giving coefficient-norm convergence.
Linearity and the colored cut estimate make the reference correction maps Cauchy in operator norm on their common reference core.
Their dense Hilbert adjoint domains give normal extensions of the same norms, including for differences by linearity and uniqueness of extension.
For fixed output test vectors the pairings converge in predual norm, so the limiting map is normal.
The clipped fields are uniformly bounded and converge strongly-star by the row bound and vacuum \(L^2\) convergence.
A clipped polynomial thus converges ultraweakly to the original polynomial, while its two-symbol derivative tensors converge in Hilbert norm by strong convergence of the bounded outer factors.
These two limits identify the reference map with the unclipped canonical slice on every target polynomial and preserve the constant.
The final smoothing limit uses norm convergence of the input generators and (3).
Applying the same argument to the flip-adjoint derivation at \(Z^*\) yields the left bound with \(\|\xi^*\|_2=\|\xi\|_2\).
The two actual core bounds imply the two domain inclusions for the original closure and its adjoint.

**Disk example.**
The masses sum to one, with constant area density on the disks and separation larger than \(2^{-\min(j,k)}/3\).
The bounded area density gives the scalar vacuum by the referenced disk calculation.
On the diagonal block \(E_n^2\) the inverse-square contribution is one for every \(n\).
For three distinct indices the two separated sums for the two-edge energy are proportional to \(\sum_j2^{-3j/2}\) and \(\sum_k2^{-k/2}\).
Equal endpoint indices give zero.
When exactly one endpoint matches the middle, the mass product is \(t_n^2t_m\).
For the ratio \(h_nh_m/t_n\) the two series in the stated estimate both decay as \(2^{-j/2}\).
For the reciprocal ratio the two series decay as \(2^{-11n/2}\) and \(2^{-3m/2}\), respectively.
These estimates prove finite \(J\) despite divergent inverse-square amplitude.
The independence of the single-input bound from the finite color counts excludes unbounded slice-to-vacuum ratios in this Gaussian family.
The review uses the existing Gaussian, free reference and domain results at the interfaces specified below.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate decision](../../claims/Yin_C_F0307_v1.md#decision-candidate) | Fixed candidate reviewed in full. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0307_v1.md#statement) | Relative actuality, exact norm, both dimension-free inequalities and domains, fixed real nullspace and example without an integrable inverse square. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0307_v1.md#argument) | Entire proof including both smoothing directions, monotonicity and degeneracy, quantitative reference construction, upper cutoff transfer, flip and disk summations. |
| [Finding](#finding) | [Matrix Gaussian theorem](../../claims/Yin_C_F0209_v1.md#argument) | Bounded fields, full criterion, intrinsic square representation, exact vacuum, cut sums, coefficient arrays and spectral clipping. |
| [Finding](#finding) | [Gaussian statement](../../claims/Yin_C_F0209_v1.md#statement) | Full actuality with both integrability conditions and the exact two-edge norm. |
| [Finding](#finding) | [Normal phase](../../claims/Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Forced starred symbol from diffuseness and the single distinguished normal relation. |
| [Finding](#finding) | [Free normal estimate](../../claims/Yin_C_F0162_v1.md#statement) | Equation (S5) with constant three on the scalar base and its free reference semicirculars. |
| [Finding](#finding) | [Normal extension](../../claims/Yin_C_F0276_v1.md#a-normal-extension-and-two-normal-densities) | Normal extension preserving the norm of each bounded core map with dense Hilbert adjoint domain. |
| [Finding](#finding) | [Flip-adjoint derivative](../../claims/Yin_C_F0073_v1.md#statement) | Flip on adjointed inputs, adjoint base and equality of vacuum norms. |
| [Finding](#finding) | [Two-slice criterion](../../claims/Yin_C_F0072_v1.md#statement) | Domain conclusion for the actual right-slice closure and Hilbert adjoint. |
| [Finding](#finding) | [Disk marginal](../../claims/Yin_C_F0303_v1.md#a-non-gaussian-example-at-the-summability-threshold) | Bounded area density of the given disk mixture and existence of its scalar vacuum. |
| [Finding](#finding) | [Relative ratios](../../claims/Yin_C_F0305_v1.md#statement) | Meaning of the single-input cost and its normalization in the excluded Gaussian family. |

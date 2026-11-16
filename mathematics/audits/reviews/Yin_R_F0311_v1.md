---
author: Yin
---

# Review of marginal commutator bounds and the scale of block noise

## Finding

At 2026-11-16T16:00 UTC a separately assigned agent for Yin independently reviewed the complete [C_F0303 v1 candidate](../../claims/Yin_C_F0303_v1.md#decision-candidate) fixed at 15:57 UTC.
The reviewer took no part in its development and received the fixed claim and its direct inputs without development dialogue, exploration notes, author explanations or earlier findings on the candidate.
The summation bound, the necessary inverse-scale condition, the noisy-coordinate construction with a scalar conjugate variable, and the exact disk threshold follow.

Multiplying the distinguished derivative by the inner difference gives the represented liberation derivation.
The outer normality relation determines the adjoint letter by injectivity off the diffuse diagonal, and the two corrections at \(Z^*\otimes1-1\otimes Z^*\) cancel.
The real derivation \(i\gamma\) has a densely defined adjoint by the vacuum identity on outer polynomial tensors.
For \(e\in W^*(Z)\), bounded marginal polynomial approximants converge to \(e\) in the closed liberation graph by the explicit difference formula.
The simultaneous graph actions of omitted coefficients and their adjoints commute with the graph projection, and both representations are normal.
They therefore intertwine the closed derivation for every bounded \(H\) of the omitted von Neumann algebra.
Taking Hilbert adjoints of this relation for selfadjoint \(H\) proves adjoint-domain invariance under \(A=H\otimes1-1\otimes H^{\mathrm{op}}\).
The bounded Borel symbol \(P(z,w)=e(z)-e(w)\) belongs to both finite-measure Hilbert spaces in the marginal adjoint theorem.
Its row minus its column is \(2(e-t1)\), so \(\gamma^*P=[e,\eta]+2(e-t1)\).
These domain facts justify testing \(AP=\bar\gamma[H,e]\) against itself in (3).

Cyclicity gives \(\|AP\|_2^2=(\tau\otimes\tau)(A^2P^2)\) even for noncommuting \(A,P\).
The two terms of \(P^2\) give equal contributions \(t(1-t)\bigl(s_e^2+s_q^2+(m_e-m_q)^2\bigr)\), which each dominate \(t(1-t)v\) by the variance decomposition.
The commutator with \(H\) has Hilbert operator norm at most \(2K\).
For a disjoint family the direct-sum norm of \(([e_j,\eta])_j\) is at most \(2\|\eta\|_2\), and that of \((e_j-t_j1)_j\) is at most one.
This gives the constant in (1) and excludes zero denominators at positive variance.
Approximating \(\eta\) in \(L^2\) by bounded vectors gives uniform decay of both \(\|e\eta\|_2\) and \(\|\eta e\|_2\) as \(\tau(e)\to0\), including for overlapping projections.

In the block construction the distinguished vacuum forces diffuseness even if none was initially imposed on \(Z\).
Indeed marginal conditional expectation on both coarse legs projects the restricted derivation to a scalar one and preserves the vacuum pairing, so the scalar geometric criterion excludes atoms.
Taking \(H=Y\) in (1) is legitimate because the centered noise is orthogonal to the base and has squared norm \(\tau(V^2)\tau(D^2)^2>0\).
Using \(\mathbb E_{M_0}(VaV)=\tau(V^2)\tau(a)1\) in the two off-diagonal blocks gives the exact commutator formula, and the diagonal block formula requires division by \(\sqrt{t_j}\) for its normalized Hilbert norm.
Since \(d_j>0\), the possible single term with \(t_j>1/2\) causes no loss in deducing (2).

For the converse construction, centering the syllables verifies the free extension of the scalar vacuum on every reduced word.
Insertion of \(b_m\otimes b_m\) has vacuum \(b_m g b_m\) because both base factors have zero derivative.
Freeness identifies \(\|a g c\|_2^2\) with \(\|a\|_2^2\|g\|_2^2\|c\|_2^2\) for bounded base factors and the centered noise vector, by bounded approximation in the noise algebra.
It gives joint convergence of the two truncations in Hilbert norm for \(b=D^{-1}\in L^2\).
On each fixed word the derivative converges by bounded outer multiplication on the finitely many insertions.
The resulting derivation sends \(Y\) to \(1\otimes1\) and kills the base, so its values on the pair lie in the pair's coarse correspondence and projection gives the claimed actual vacuum and norm estimate.
At 2026-11-16T16:02 UTC the reviewer rechecked the clarified final paragraph of the statement against this construction.
Both formulations of sufficiency now explicitly assume that \(V\) has an actual scalar conjugate variable.
The hypothesis matters even for \(H_0=0\) and \(D=1\), which satisfy (2).
For free centered noise on \(\{-1,1\}\), differentiating \(Y^2=1\) would force the vector \(Y\otimes1+1\otimes Y\) of squared norm two to vanish.

The disk weights sum to one and the ratios of weights to areas are constant.
Uniform quadratic ball growth bounds both the maximal linear density and the squared curvature energy, since a shell of maximum distance \(r\) contributes \(O(r^2)\) to the two-point integral for fixed \(z\).
The uniform law on the interval meets the real scalar \(L^3\) criterion.
The inverse-square sum equals \(3\sum_j j^{-2\alpha}\), including harmonic divergence at equality.
For \(m<n\) the distance between disks is at least \((13/32)2^{-m}\).
The ratios \(d_n/d_m\) are uniformly bounded in this order, and the two ratio contributions are bounded by constant multiples of \(\sum_m\sum_{n>m}t_n\) and \(\sum_m d_m^2\sum_{n>m}t_n/d_n^2\).
Both are finite for \(\alpha>1/2\).
The zero-drift free location and scale criterion then gives actual conjugate variables and strong duals, and its equivalence excludes strong duals when (2) diverges.
The direct inputs were checked at the indicated interfaces.
Their upstream proofs and the unrestricted implication in F0011 lie outside this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0303_v1.md#decision-candidate) | Decision identifying the fixed whole argument and inputs reviewed. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0303_v1.md#statement) | Commutator bounds, inverse-scale necessity, noisy-coordinate sufficiency under the scalar vacuum hypothesis, and the exact disk threshold. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0303_v1.md#argument) | Closed graph and adjoint pairing, orthogonal sum, free-product insertion, planar curvature and ratio estimates. |
| [Finding](#finding) | [Liberation recovery](../../claims/Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Forced marginal star value and commutator vacuum under the distinguished-coordinate hypotheses. |
| [Finding](#finding) | [Measurable spectral blocks](../../claims/Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Graph approximation of a bounded marginal spectral projection. |
| [Finding](#finding) | [Omitted graph actions](../../claims/Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Normal extension of both omitted graph multipliers. |
| [Finding](#finding) | [Marginal adjoint formula](../../claims/Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Bounded Borel domain and the sign of the antisymmetric correction. |
| [Finding](#finding) | [Scalar geometric criterion](../../claims/Yin_C_F0255_v1.md#statement) | Diffuseness from a scalar vacuum and sufficiency of the disk measure's two energy bounds. |
| [Finding](#finding) | [Real scalar density](../../claims/Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Scalar actuality of the uniform real noise. |
| [Finding](#finding) | [Free location and scale](../../claims/Yin_C_F0277_v1.md#statement) | Equivalence of actual vacua and strong duals for the scalar zero-drift model with the indicated ratio energy. |

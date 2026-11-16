---
author: Yin
---

# Review of the averaged square-density criterion for canonical domains

## Finding

At 2026-11-16T15:31 UTC a separately assigned agent reviewed the entire [C_F0297 v1 candidate](../../claims/Yin_C_F0297_v1.md#decision-candidate) for Yin.
The reviewer had no role in its development and received the fixed proof, dependencies and scope without exploration notes, development dialogue, author explanations or previous reviews of this candidate.
Both the quantitative domain conclusion and the example follow under the stated hypotheses.

For a symmetric kernel \(b=q^{\circ k}\) with \(|q|\le1_{B^2}\), its supremum, its vacuum norm and its row \(L^2\) norm are bounded respectively by \(t^{k-1}\), \(t^{k-1}h\) and \(t^{k+1/2}\).
In each sliced summand the first tensor leg ends with an inner marginal factor supported on \(B\), even after multiplying on the outside before slicing.
Thus \(E_bu=(E_bu)e\) and \(|\langle u,E_{b\circ b}u\rangle|\le\sqrt t\|E_{b\circ b}u\|_2\).
Equations (B0c) and (B0e) give the displayed recurrence for either sign of the analytic unitary.
Dividing by \(t^{2k-2}\) gives coefficient \(t^{3/2}\) on \(w_{2k}\).
The finite-word insertion estimate and the first-derivative series give \(w_k\le C_u t\) at this fixed \(u\), so the dyadic supremum \(S\) satisfies \(S^2\le(2h+3t^{3/2})S\).
The last right-support pairing gives precisely \(2\sqrt t\,h+3t^2\).
Product conditional expectations and fixed-\(u\) continuity justify (2) for measurable bounded \(q\).

For \(w\in A\), every eligible endpoint lies in \(5A\) and every point of \(5A\) lies within \(3\sqrt2\,r_j\) of \(w\).
The diameter shell gives \(\kappa^2\le16/r_j^2\), hence \(\sum s_{jA}t_B^2\le16W\).
In the vacuum sum the commutator contributes \(|z-v|^2\), killing the spectral diagonal even if the joint measure of \(\xi\) charges it.
At most 25 dilated squares contain \(z\) at a fixed scale.
For \(z\ne v\), the admissible inverse squared scales sum to at most \(200/(3|z-v|^2)\).
Consequently (4) holds with \(C_0=80000/3\), and Cauchy--Schwarz applied to \(\sqrt{s_{jA}/t_B}\,h_B\) and \(\sqrt{s_{jA}}\,t_B\) bounds the sum of the absolute energies by \(8\sqrt{C_0W}\|\xi\|_2+48W\).

The nonnegative kernel sums increase to \(g\), and Jensen gives \(\int |z-v|^2 g^2\,d\mu^2\le4\int\kappa^2\,d\mu^3<\infty\).
Both generator gaps therefore converge strongly as coarse vectors, which suffices on words and on the differentiated binomial series.
With the inner product linear in the second variable, \(\operatorname{Im}\langle u,i(\mathrm{id}\otimes\tau)I_g\gamma(u)\rangle\) has exactly the real-part convention used in the signed mixed energy.
Its absolute bound yields \(V(u)\le C(\|\xi\|_2+\sqrt W)\) by the quadratic inequality.
Averaging the two signs, taking real and imaginary parts, and applying the actual core adjoint formula gives both oriented bounds.
Weak graph limits of bounded Kaplansky approximants also pass the polynomial commutator through multiplication by \(X_j\), with the claimed generator-first sign.

For the negative direction, the limiting same-segment endpoint pairs contribute zero against a third point at the origin, whereas both mixed pairs have positive curvature and negative coefficient.
The diameter stays at least \(1-2d\) for these third points.
At fixed \(d>0\) bounded area densities give an \(O_d(r^4)\) diameter lower tail for the remaining terms, so choosing \(\varepsilon\) after \(d\) preserves strict negativity.
The constant test is strictly positive.
The cluster masses sum to one and \(\sum_m4^m t_m<\infty\) bounds the intercluster sum uniformly using the stated separation.
The dyadic estimate for each cluster follows by summing \(r_j^2/R_n^4\) below its size and \(r_j^{-2}\) above it.
In particular \(t_n^3/R_n^2=343\,2^{8-n}\) is summable, while \(t_n^2/R_n^2=49\,2^{8+2n}\) diverges.
The term \(j=0\) handles radii larger than the support diameter in the maximal-density comparison, and (3) bounds the total curvature by integration.
The scalar geometric criterion therefore applies to the full mixture.
The remainder outside triples from a common cluster has bounded kernel by the two intercluster estimates.
The normalized tests on a single cluster consequently have the claimed divergence with each sign.
For a putative nonnegative block expansion its partial sums are bounded by \(g+|b|\in L^1(\mu^2)\), giving nonnegative limiting forms on each bounded test, while the row bound makes \(b\) Hilbert--Schmidt.
This precludes the negative divergence.
The uniform interval has bounded maximal density, zero curvature and divergent \(W\) on its interior as asserted.

The inspection covers the stated sufficient condition and the scalar obstruction to the specified positive-block decomposition.
The existing results below were checked at their used mathematical interfaces, including the mixed-defect normalization and both actual graphs.
The unrestricted implication for normal tuples remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0297_v1.md#statement) | Both quantitative oriented estimates, both canonical domains, the generator commutators and the signed scalar counterexample to block decomposition. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0297_v1.md#argument) | Entire candidate, including finite and measurable kernels, scale summation, graph passage, two template signs, cluster estimates, scalar actuality and the interval limit. |
| [Finding](#finding) | [Task contract](../../tasks/Yin_T_F0011_v1.md#contract) | Actual starred derivations of a normal tuple, the full bounded-vector domains and the commutator convention. |
| [Finding](#finding) | [Liberation vacuum](../../claims/Yin_C_F0238_v1.md#statement) | Actual partial liberation and the commutator formula giving the squared spectral gap. |
| [Finding](#finding) | [Marginal adjoint](../../claims/Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Symmetric finite tensors, spectral absolute continuity and the localized vacuum formula. |
| [Finding](#finding) | [Finite-kernel energy](../../claims/Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) | Equations (B0c) and (B0e) on both analytic unitaries and the fixed-input insertion continuity. |
| [Finding](#finding) | [Scalar criterion](../../claims/Yin_C_F0255_v1.md#statement) | Diffuseness and total curvature for an actual marginal, and sufficient geometric energy for actual scalar conjugate variables. |
| [Finding](#finding) | [Signed mixed-energy passage](../../claims/Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Signed energy, strong convergence of the gap tensors and the passage to both oriented core bounds. |
| [Finding](#finding) | [Positive-block statement](../../claims/Yin_C_F0292_v1.md#statement) | Nonnegative blocks with a uniformly square-integrable-row remainder in the excluded decomposition. |
| [Finding](#finding) | [Actual normal phase graphs](../../claims/Yin_C_F0076_v1.md#statement) | Applicable mixed tensor-leg domains under the actual starred hypothesis. |
| [Finding](#finding) | [Mixed-energy identities](../../claims/Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) | Equations (19) and (20), the curvature coefficient and the oriented contractions. |
| [Finding](#finding) | [Two-slice theorem](../../claims/Yin_C_F0072_v1.md#statement) | Actual core-adjoint formula and weak closedness of both graphs. |
| [Finding](#finding) | [Original canonical operators](../../claims/Yin_C_F0078_v2.md#the-original-canonical-operators) | Passage of the commutators on bounded vectors after obtaining the two core bounds. |

---
author: Yin
---

# Review of canonical domains after subtracting circular curvature components

## Finding

At 2026-11-16T15:09 UTC an agent outside proof development independently checked the [candidate of 2026-11-16T15:00](../../claims/Yin_C_F0292_v1.md#decision-candidate), its whole argument, and its dependencies at their stated uses.
The reviewer received the fixed candidate and review scope without development dialogue, proof notes, author explanations or previous findings about this candidate.
The signed lower bound suffices for both domains, including when the curvature kernel has no bounded integral operator.
The sufficient condition on circles and the example with an infinite fourth composition both hold.

For a block \(e\otimes e\), completing the square in the projection identity costs \(\|e\zeta e\|_2^2/t\), since left multiplication by either analytic unitary is an isometry.
Summing the lower bounds only uses \(\lambda_n\ge0\), with no orthogonality assumption in (1).
The row bound for \(b\) implies its product-measure \(L^2\) bound since \(\mu\) is a probability; its separate \(\nu_\zeta\) bound is exactly the other weighted-liberation hypothesis.
The slice estimate for \(i I_b\gamma\) consequently bounds the absolute value of the scalar pairing for \(I_b\gamma\) on either analytic unitary, by first taking its polynomial series.
Conditional Jensen and \(|z-v|^2\kappa^4\le4\kappa^2\) give an integrable majorant for the squared gap-weighted partial sums, using the finite total curvature of the actual marginal and the bounded support for the contribution of \(b\).
More precisely the majorant can be taken to be \(|z-v|^2(g+2|b|)^2\); no majorant for \(g^2\) is needed.
The two generator tensors therefore converge, and the finite Leibniz sums followed by the absolutely summable first-derivative series give the asserted limit at \(u\).
In particular the limit descends through represented polynomial relations since all approximants do.

The actual mixed tensor-leg graphs used to derive (19) and (20) exist under the actual starred hypotheses alone, as specified in [the phase theorem](../../claims/Yin_C_F0076_v1.md#statement).
Tracing the middle variable in the mixed defect gives one half of the gap tensor at either distinguished letter and zero at the other letters.
Thus the defect term subtracted in (19) is \(Q_g(u)/2\), and the other term has absolute value at most \(2V(u)\|\xi\|_2\).
Averaging the two analytic signs recovers the selfadjoint input, so both real slices are uniformly bounded on selfadjoint core contractions and hence on the entire core unit ball by scaling and taking real and imaginary parts.
Their two complex combinations bound the right slices of \(\delta\) and its flip-adjoint companion; taking the tracial adjoint at \(p^*\) turns the latter into the left slice of \(\delta\) at \(p\).
These are precisely the two estimates required for the original closure and adjoint.
The core relation \(E(X_jp)-X_jE(p)=\delta_{ij}\tau(p)1\) passes through the graph closure because multiplication by \(X_j\) and \(P_\Omega\) are bounded; negating the closure gives the generator-first sign on \(\mathcal M\Omega\).

Write \(S\) for the supremum in (2).
For endpoints on different circles the third point outside the first circle costs at most \(4S\) after integration, and one on the first circle costs at most another \(4S\) by the sum for the second endpoint.
For endpoints on the same circle its own contribution is exactly \(t_n/r_n^2\) almost everywhere by diffuseness, with the remaining contribution at most \(4S\).
The bounded remainder is in both required spaces (the vacuum spectral measure is finite and absolutely continuous with respect to \(\mu^2\)).
Since \(d\nu_\zeta=|z-v|^2d\nu_\xi\), the diagonal block of cost \(r_n^{-2}\|e_n\zeta e_n\|_2^2\) is at most \(4\nu_\xi(K_n^2)\); disjointness bounds their sum.

In the example the masses sum to one, the pairwise distances have the stated lower bound, and \(\sum_m4^m t_m<\infty\) bounds the separation sum uniformly.
Both the diagonal curvature energy and the integrated square of the own-circle maximal linear density are bounded by a constant times \(\sum_n t_n^3/r_n^2\), a convergent geometric series proportional to \(\sum_n 2^{-n}\).
For a disk centered on \(K_n\), a contribution from \(K_m\) requires a radius at least \(d_{nm}\), so Cauchy--Schwarz against the separation sum bounds the other-circle maximal density.
The scalar criterion gives an actual vacuum, while the indicator Rayleigh quotients grow as \(t_n^2/r_n^2\), precluding both boundedness and the symmetric weighted Schur inequality.
Continuity on the two fixed noncollinear arcs and at zero gives a uniform lower bound for the first and last factors of the fourfold kernel integral when its three intermediate points lie on one sufficiently late circle.
The two internal factors cost at least \((t_n/r_n^2)^2\) almost everywhere on that triple.
These disjoint triples contribute a divergent series proportional to \(\sum_n2^n\), for every endpoint pair in the positive-measure rectangle.
This review checks the fixed dependencies at these interfaces, without re-auditing their full proofs or settling the converse in the [unrestricted normal problem](../../tasks/Yin_T_F0011_v1.md#contract).

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0292_v1.md#decision-candidate) | The fixed candidate and all its asserted conclusions. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0292_v1.md#statement) | Both domains, the circle condition and the divergent example. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0292_v1.md#argument) | The full signed estimate, mixed energy, geometry and example. |
| [Finding](#finding) | [Projection block](../../claims/Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Equation (4) for Borel projections and both analytic signs. |
| [Finding](#finding) | [Weighted liberation](../../claims/Yin_C_F0077_v1.md#statement) | Uniform Hilbert slice bound for the symmetric remainder and absolute continuity of the vacuum measure. |
| [Finding](#finding) | [Scalar criterion](../../claims/Yin_C_F0255_v1.md#statement) | Finite total curvature and diffuseness under actuality; sufficiency for the scalar example. |
| [Finding](#finding) | [Mixed energy](../../claims/Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) | The actual-graph identities (19) and (20), including their sign, half factor and analytic limit. |
| [Finding](#finding) | [Phase theorem](../../claims/Yin_C_F0076_v1.md#statement) | No marginal growth hypothesis for the actual mixed graphs used in (19) and (20). |
| [Finding](#finding) | [Two slices](../../claims/Yin_C_F0072_v1.md#statement) | Part B for the right and left slice on the original represented core. |
| [Finding](#finding) | [Original operators](../../claims/Yin_C_F0078_v2.md#the-original-canonical-operators) | Closure and adjoint domains and the generator-first commutators after negation. |
| [Finding](#finding) | [Liberation vacuum](../../claims/Yin_C_F0238_v1.md#statement) | Squared-gap spectral measure identity for the circle-block cost. |
| [Finding](#finding) | [Weighted curvature condition](../../claims/Yin_C_F0291_v1.md#statement) | Boundedness required by its symmetric weighted Schur inequality. |
| [Finding](#finding) | [Task contract](../../tasks/Yin_T_F0011_v1.md#contract) | Meaning of the coordinatewise strong dual system and limits of the sufficient condition. |

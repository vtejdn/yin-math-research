---
author: Yin
---

# Review of the Gaussian column density and its critical integrability exponent

On 2026-11-14T12:41 UTC, a separate agent reviewed for Yin the complete [candidate dated 2026-11-14T12:38](../../claims/Yin_C_F0263_v1.md#decision-candidate).
The reviewer had no role in developing the proof and received the fixed claim and its dependencies without development discussion or earlier findings on this candidate.

## Finding

Under the actual starred condition the reciprocal kernel \(\beta=1/a\) is the vacuum vector in the full generated algebra.
Truncations are bounded selfadjoint fields, so convergence of their vectors in \(L^2\) gives convergence of their squares in \(L^1\).
Conditional expectation of each square integrates \(\beta_n^2\) over the second variable, giving \(h\) in the limit and \(\tau(h)=\|\xi\|_2^2>0\).
For a bounded input \(p\), integration over the added final edge gives \(\|R_n p\|_2^2=\tau(h_n p^*p)\).
The same calculation on differences and \(p^*p\le\|p\|^2 1\) justify Hilbert convergence without any uniform operator bound on the creations.
Subtracting the limit from right multiplication \(p\xi_n\to p\xi\) identifies the limit of \(R_n^*p\) and bounds its norm.

I checked the commutator on each path degree.
Left creation and final annihilation commute on positive degrees, including degree one, where both orders retain the same new initial edge.
The two annihilations integrate independent endpoint variables on degrees at least two and have zero composition on smaller degrees.
The sole surviving commutator on degree zero integrates against \(a\beta_n\), which tends to one in \(L^2(\mu^2)\).
Its limit on the whole path space is the vacuum projection.
Left multiplication by either marginal letter commutes with final annihilation, and the original right slice has \([E,L_{T_a}]=P_\Omega\) by its outer product rule.
The matching commutators and values on the vacuum identify the two maps on all original mixed words.
Squaring the bound gives \(2\tau((\xi^2+h)p^*p)\), the claimed constant for the normalized density, with the same density for every summand in a finite column.

For the two-disk pair the core approximants \(u_nT_a v_n\) have outputs \(u_n\tau(v_n)\to q e_r\).
Uniformly bounded strong convergence gives convergence on the vector \(\sqrt w\) for each proposed probability density.
The two marginal conditional expectations of \(B_r=(e_rT_a f)^*(e_rT_a f)\) have operator norm bounded by an absolute multiple of \(t_r\sqrt r\), since \(Qe_r\) equals \(\int_{e_r}m\,d\mu\) on \(f\) and the semicircular conditional expectation is bounded by \(4\tau(B_r)1\).
This uniform estimate survives convex combinations and \(L^1\) closure for each \(r\), whereas the squared slice norm equals \(q^2t_r\).

For the operator norm test I checked both orientations of compression.
The squared creation norm is at most \(\int_{e_r}m\,d\mu\) when the new initial vertex belongs to \(e_r\), and at most \(q\sqrt r/2\) in the reversed compression whose adjoint gives annihilation.
This yields \(\|B_r\|_\infty=O(r^{1/2})\), and the trace calculation gives \(\|B_r\|_1=O(r^{5/2})\).
Interpolation gives \(\|B_r\|_{4/3}=O(r^{1/8+15/8})=O(t_r)\).
The normalized tests tend to zero in \(L^1\) and are bounded in \(L^{4/3}\), so truncation of any fixed \(L^4\) density and Hölder's inequality give \(\tau(wB_r)/t_r\to0\).
This contradicts domination at each fixed finite constant, also excluding higher exponents by the probability trace.

For the positive density, the separated cross kernels represent \(gSf+fSg\) by bounded truncation in \(L^2\), with \(g(z)=\sqrt2|z|^{-1/4}\) on \(D_0\).
The radial integral for \(g\in L^{2s}\) is finite exactly when \(s<4\), and multiplication on either side by \(S,f\) is bounded on this space.
The same-disk field is bounded.
The potentially singular term in \(h\) on \(D_0\) is \(q/m\), whose \(s\)-th power has the same radial integrability threshold.
These checks establish the claimed \(L^s\) range for the explicit density and, together with the normalized tests, the exact range for existence on this fixed pair.
The general domination estimate and all stated obstructions are supported at the indicated original-core scope.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0263_v1.md#statement) | General explicit density and column domination, marginal convex hull obstruction, and sharp strong integrability range on the fixed pair. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0263_v1.md#argument) | Right creation and limiting annihilation on bounded inputs, identification on the starred core, positive and negative two-disk estimates. |
| [Finding](#finding) | [Single-channel vacuum](../../claims/Yin_C_F0157_v2.md#statement) | Actual starred hypothesis gives the full generated algebra and its reciprocal one-edge vacuum. |
| [Finding](#finding) | [Bounded coordinates, phase, and generation](../../claims/Yin_C_F0157_v2.md#bounded-coordinates-phase-and-generation) | Creation action, its endpoint integral norm, symmetry, and representation of truncated and separated fields. |
| [Finding](#finding) | [Normal starred values](../../claims/Yin_C_F0076_v1.md#statement) | The actual distinguished derivation kills the omitted starred marginal generator. |
| [Finding](#finding) | [Two-disk construction](../../claims/Yin_C_F0259_v1.md#argument) | Actual Markov pair, its cross amplitude, masses and bounded polynomial approximation with convergent original slices. |
| [Finding](#finding) | [Semicircular marginal and conditional square](../../claims/Yin_C_F0259_v1.md#the-semicircular-marginal-and-the-conditional-square) | The degree-zero conditional square in the base and the trace bound for its expectation in the semicircular marginal. |

---
author: Yin
---

# Independent review of overlapping projection tests and uniform singular concentration

## Finding

At 2026-11-14T12:20 UTC a reviewing agent for Yin checked the whole statement and argument of the [F0258 candidate](../../claims/Yin_C_F0258_v1.md#decision-candidate) of 2026-11-14T12:19 UTC.
The agent took no part in developing the proof and received only the assignment, fixed inputs and repository instructions.
The initial inspection used the candidate and its mathematical dependencies, without exploration notes, development dialogue, author explanations or earlier review opinions.
The estimates (1)–(3), the improved constant for exact cutoffs, the scalar specialization and the obstruction after free enlargement all follow under the stated hypotheses.

### Compression and overlapping tests

The finite-column hypothesis supplies one normalized density \(d\) and one implementer \(T\) for the distinguished coordinate, by (2) of F0211.
Commutation with the other normal generators gives commutation with their adjoints by Fuglede and then with all left multipliers from \(N\).
Thus subtracting any omitted shift preserves the same rank-one commutator.
With \(h=\sqrt d\), the law of \(h\) weighted by \(p/\tau(p)\) is a probability law for every projection \(p\) of positive trace \(s\), even when \(p\) does not commute with \(d\).
The expectations of \(h\) and \(h^{-2}\) are finite, and convexity of \(x\mapsto x^{-2}\) gives \(\langle h\rangle_p\sqrt{\langle h^{-2}\rangle_p}\ge1\).

For \(V=Z-b\) the polar isometry identifies the complements of the right and left radius-\(r\) cutoffs, so their traces agree, including when the kernels are nonzero.
The norm of the rank-one compression is \(\sqrt{\tau(q)}\sqrt{\tau(p d^{-1})}\).
The other expression for the commutator bounds this norm by \(c(\|Vp\|+\|qV\|)\).
For the exact cutoffs both operator norms are at most \(r\), which gives \(s^2\le2cr\,\tau(hp)\) by the preceding Jensen bound.
For an approximate test, the corner trace of \(eV^*Ve\) is at most \(r^2t\), so the part \(p\le e\) below or at \(4r^2\) has mass \(s\ge3t/4\) and \(\|Vp\|\le2r\).
If the right cutoff at \(2r+\varepsilon\) had mass less than \(s\), its restriction to \(pL^2(M)\) would have a nonzero kernel by finite tracial support comparison.
Every vector there would lie above that cutoff, contradicting \(\|Vp\|\le2r\) for a nonzero vector.
The matching left cutoff therefore has mass at least \(s\), and compression gives \(s^2\le c(4r+\varepsilon)\tau(hp)\).
Positivity transfers this estimate to \(\tau(he)\), and \(4(4/3)^2=64/9\) after passage to the limit.
The same \(h\) tests every summand, and \(\|h\|_2=1\) gives the asserted \(L^2\) norm of their weighted sum.

For two normalized projections \(g_j=e_j/\sqrt{t_j}\) and \(g_k=e_k/\sqrt{t_k}\), positivity of \(\tau(e_je_ke_j)\) and its upper bound by each trace give the stated decay \(\theta^{|j-k|/2}\).
The sum over both directions is at most \((1+\sqrt\theta)/(1-\sqrt\theta)\).
Writing \(u_j=t_j^{3/2}/r_j\), the weighted inequality bounds \(\sum u_j^2\) by \((64/9)c\|\sum u_jg_j\|_2\) on each finite segment, which gives (3) with one power of the row-sum bound after squaring.
The partial sums increase, so this also covers the infinite sequence.

### Rearrangement, free enlargement and scalar specialization

Layer integration gives \(\tau(hp)\le\int_0^s h^*(v)\,dv\) for arbitrary \(p\), since \(\tau(pf)\le\min(s,\tau(f))\) for every spectral projection \(f\) of \(h\).
Thus \(F(r)>t\) implies \(r\ge t/(2cA(t))\) by choosing just one cutoff with mass exceeding \(t\) and using the decrease of \(A\).
The positive constant \(c\) is nonzero since the right slice of \(Z\) is \(1\).
This inclusion of radius sets needs neither attainment of the supremum nor a measurable selection of shifts.
The function \(F\) is measurable by monotonicity, and integrating \(r^{-3}\) on the resulting half-line gives \(2c^2 A(t)^2/t^2\).
The layer factor \(3t^2\) and the dilation estimate \(\|A\|_2\le2\|h^*\|_2=2\) then give \(24c^2\).
Integration on \([r,2r]\) bounds \(3F(r)^3/(8r^2)\) by an integral vanishing at the origin.
The displayed logarithmic lower rate makes the integrand at least \(a^3/(r\log(1/r))\), whose integral diverges.
Divergence of the cubic integral or unbounded simultaneous test ratios for a single tuple force infinite original column cost, and F0208 excludes every bare witness for that coordinate after the two-Haar enlargement.

For a scalar shift the F0233 marginal implementer and its faithful normalized density have exactly the vacuum and Hilbert space required for commutator compression.
The conditional expectation \(w\) of an ambient test projection preserves both its mass \(t\) and its \(|Z-\lambda|^2\) moment.
Cutting this weight at \(2r\) loses at most \(t/4\).
For the surviving commuting weight \(k\), the two compressed commutator terms have norms at most \(2c_0r\) each, since \(\|\sqrt k\|\le1\) and \(\|(Z-\lambda)\sqrt k\|\le 2r\).
Weighted Jensen yields \(s^2\le4c_0r\,\tau(k\sqrt{d_0})\), bounded in turn by \(4c_0r\,\tau(e\sqrt{d_0})\) through conditional expectation and bounded truncations.
This transfers the common test vector to the ambient space, while the exact cutoffs are already marginal projections.
Consequently the ambient Gram estimate and the marginal rearrangement give all the scalar conclusions with \(c_0\le12\|\xi_\mu\|_2\).
The cited established results were checked at these interfaces.
The conditional obstruction supplies no tuple with divergent concentration.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0258_v1.md#statement) | All three estimates, exact cutoff constant, arbitrary ambient projections, scalar case and free enlargement. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0258_v1.md#argument) | Weighted compression, approximate corner, overlap Gram bound, uniform rearrangement, small-radius limit and scalar conditional expectation. |
| [Finding](#finding) | [Weighted commutator](../../claims/Yin_C_F0211_v1.md#statement) | Common optimal implementer, normalization, inverse integrability and commutation with the omitted algebra. |
| [Finding](#finding) | [Enlarged column criterion](../../claims/Yin_C_F0208_v1.md#statement) | Infinite original column cost excludes a bare witness for the old coordinate and the enlarged tuple retains actual vacua. |
| [Finding](#finding) | [Marginal commutator and ambient weights](../../claims/Yin_C_F0233_v1.md#a-scalar-commutator-and-positive-weights-in-the-ambient-algebra) | Actual marginal vacuum, the bound \(12\|\xi_\mu\|_2\) and compression by a positive weight obtained by conditional expectation. |

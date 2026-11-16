---
author: Yin
---
# Four cyclic cosets with a common intersection

A separate reviewing agent checked the entire [fixed Claim](../../claims/Yin_C_A0023_v1.md) for Yin on 2026-11-16T16:01 UTC.
The reviewer did not develop its proof or receive development discussions, author explanations, exploration notes or previous verdicts on it.
The previously cited double-coset calculation was read at its bounded-coefficient approximation interface.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0023_v1.md#statement) | Rank at least four sevenths under distinctness of all twelve ordered double cosets and equality of the six pairwise subgroup intersections. |
| [Whole-argument finding](#whole-argument-finding) | [Double-coset orthogonality](../../claims/Yin_C_A0023_v1.md#double-coset-orthogonality) | Fourth moment, intersection expectations, initial rank-preserving normalization, and the trivial common intersection. |
| [Whole-argument finding](#whole-argument-finding) | [Alternating normalization](../../claims/Yin_C_A0023_v1.md#alternating-normalization-on-the-two-circles) | Fiber averages, multipliers on both sides, entropy decreases, integrability and the final numerical rank estimate. |

## Whole-argument finding

Writing \(d_{ij}=g_i(h)x_ix_j^{-1}g_j(h)^*\), the fourth moment is the squared norm of \(1+\sum_{i\ne j}d_{ij}\).
Uniformly bounded Fejér approximants to the two circle coefficients converge in \(L^2\), so the product converges in \(L^2\) by the operator norm bound on the other factor in each of the two differences.
Its Fourier support stays in \(Hx_ix_j^{-1}H\).
These twelve supports are pairwise disjoint by hypothesis, and all miss \(H\) since the right cosets \(Hx_i\) are distinct.
Tracial cyclicity gives \(\|d_{ij}\|_2^2=\tau(T_iT_j)\).
Pairwise equality \(H_i\cap H_j=J\) allows Parseval to express every mixed term as an inner product of the corresponding \(E_JT_i,E_JT_j\) on the same subgroup.
Summing the terms gives the displayed fourth moment, and the Hilbert space sum-of-squares inequality gives the factor \(3/4\).
The unit first moment and trace Cauchy–Schwarz against the range projection then give the required link to rank.

The initial Laurent polynomials have only finitely many zeros on the circle, each of finite order.
Their normalized squared moduli are bounded by one and have integrable negative logarithms by comparison with \(-2\log|f_i|\) plus a constant.
The first left multiplier is an affiliated unit, and the resulting coefficients are bounded.
For trivial \(J\), the sum of the expectations is the constant one, already giving rank at least \(4/7\).

For infinite \(J\), conjugating its generator back through \(x_i\) gives a nonzero integer power \(h^{m_i}\).
On the circle for \(h\), a right test function for \(J\) thus becomes its composition with \(z\mapsto z^{m_i}\).
The adjoint averaging map has exactly \(|m_i|\) terms with equal weights, including for negative \(m_i\).
It follows that the right multiplication by \(c(k)^{-1/2}\) divides each intensity by \(c(z^{m_i})\).
Positivity almost everywhere gives an affiliated inverse, and \(c(z^{m_i})\ge u_i(z)/|m_i|\) bounds each intermediate intensity.
The subsequent left multiplier uses their sum \(b\), bounded below by \(1/4\) because \(c\le4\).
It is also bounded above by \(\sum_i|m_i|\).
Both updates preserve affiliated rank, and every row-normalized operator has bounded coefficients to which the moment estimate applies.

Each power map sends Haar probability to Haar probability.
Consequently \(\int c=1\), the column-normalized densities satisfy \(\sum_iP_iv_i=1\), and \(\int b=1\).
The fiber lower bound for \(c\), its uniform upper bound, and integrability of \(\log u_i\) give \(\log c\in L^1\).
The two bounds for \(b\) then give the same integrability for the new edge densities, so induction justifies taking all logarithmic integrals.
The uniform edge densities \(1/4\) give both uniform marginals even when the four covering indices differ.
The entropy drops for right and left normalization are thus exactly \(-\int\log c\) and \(-\int\log b\).
Jensen gives their nonnegativity and the zero lower bound for the entropy, making the successive right drops summable.

On \(0<x\le4\) the function \(x-1-\log x\) has second derivative at least \(1/16\) and vanishes to first order at one.
The right drop therefore bounds \(\|c_n-1\|_2^2/32\).
The squared norms of \(c_n\) tend to one, and \(1\le r(a)(1+3\|c_n\|_2^2/4)\) at every stage gives \(r(a)\ge4/7\).
Only the scalar moment bound is passed to the limit, so convergence of the multipliers or existence of a limiting normalized operator is unnecessary.

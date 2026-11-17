---
author: Yin
---

# Endpoint weights for the powers of a normalized Gram operator

At 2026-11-17T02:08 UTC an agent outside the development of Yin_C_A0057_v1 independently reviewed its fixed statement and three proof sections for Sheng Yin.
No proof-development dialogue, author explanation or earlier finding on this claim was supplied.
The reviewer reused the ball inequality and trace-integrality input previously checked for the four-line groups and examined the new moment, limit-order and kernel-projection arguments directly.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0057_v1.md#statement) | Exponents, limit orders, unnormalized matrix trace, closed-range equivalence and the noncommuting row example. |
| [Whole-argument finding](#whole-argument-finding) | [Argument](../../claims/Yin_C_A0057_v1.md#argument) | Endpoint grouping, fourth differences, fixed-scale convergence and comparison of dyadic sums with spatial moments. |
| [Whole-argument finding](#whole-argument-finding) | [Closed range](../../claims/Yin_C_A0057_v1.md#interchanging-the-scales-forces-a-spectral-gap) | Uniform operator-norm tails along a subsequence, failure of norm convergence at a spectral accumulation point, and sufficiency of closed range. |
| [Whole-argument finding](#whole-argument-finding) | [Nonclosed-range family](../../claims/Yin_C_A0057_v1.md#nonclosed-range-with-exponential-decay-after-canceling-an-injective-factor) | Kernels and ranges of the row, Neumann-series propagation, exponential coefficient tails and actual trace. |
| [Whole-argument finding](#whole-argument-finding) | [Rapid decay and trace](../../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace) | Operator-norm shell estimate and integrality from a spatial moment of exponent strictly above three. |

## Whole-argument finding

Writing \(Q_k(g)\) for the group coefficient matrix, the binomial identity gives the multiplier \((1-e^{-s|g|})^4\) on its squared Hilbert–Schmidt norm.
Terms contributing to a coefficient must first be summed with their complex phases and matrix indices.
The spectral theorem gives \(Q_k\to p\) in trace \(L^2\), so the corresponding coefficient vectors converge in \(\ell^2\).
At each fixed \(s\), multiplication of these vectors by \((1-e^{-s|g|})^2\) is a contraction, proving convergence of the squared norms in the fourth difference.

For positive integer radius \(r\), the dyadic term with \(2^j\le r<2^{j+1}\) bounds the full sum below by a constant multiple of \(r^\beta\).
The terms on either side are bounded above by geometric series using respectively \(1\) and \((2^{-j}r)^4\), requiring \(0<\beta<4\).
All terms are nonnegative, permitting summation even when the moment is infinite.
The omitted identity coefficient has finite norm.
This proves the first equivalence and, for \(\beta>3\), allows the spatial integrality result.
If any exponent above three is available, a smaller exponent strictly between three and four is available as well.

A finite liminf after summing all scales yields a subsequence bounded in weighted \(\ell^2_\beta\), including its degree-zero part since \(\|Q_k\|_2\le\sqrt m\).
The ball bound and Cauchy–Schwarz over shells from \(J\) onward then give an operator-norm tail bounded by a constant times \(2^{-(\beta-3)J/2}\) uniformly on the subsequence.
Finite balls and convergence of their coefficients give norm convergence along that subsequence to \(p\).
If positive spectrum accumulates at zero, the spectrum of \(B\) on the orthogonal complement of its kernel approaches zero, giving \(\|Q_k-p\|=1\) for every \(k\).
Conversely a gap gives geometric convergence in norm and hence in trace \(L^2\).
Outside radius \(kw\) the coefficients of \(Q_k\) vanish, so this same bound gives an exponential \(\ell^2\) tail for \(p\).
Inside that ball the squared weighted error costs at most \((1+kw)^\beta\) times the squared \(L^2\) error.
These bounds give uniformly bounded weighted masses for all powers under closed range, and divergence to infinity in the nonclosed-range case.
The zero matrix gives constant powers and vanishing fourth differences.

For \(T=(1,V)\) surjectivity follows from the first coordinate, whereas \(1-g\) is injective and has nonclosed range on the regular Hilbert space.
Thus the kernel of \((1-g)T\) is the kernel of \(T\), with range exactly that of \(1-g\).
The formula using \((TT^*)^{-1}=(1+VV^*)^{-1}\) gives the kernel projection of unnormalized trace one.
The proposed geometric sums converge in operator norm at a geometric rate with propagation \(O(k)\), and multiplication by the two finite row factors only adds a constant radius.
This gives exponential decay of the squared-summable Fourier tail of that projection without commuting \(g\) with \(V\).

The argument supports both limit-order conclusions and the example.
The earlier product-fiber results, including their [four-line specialization](../../claims/Yin_C_A0051_v1.md#product-fibers-and-complex-coefficients-in-the-four-line-law), concern specified vertex factors.
They provide no estimate for the full sequence of distance-weighted moments of an arbitrary matrix on a fixed realization.

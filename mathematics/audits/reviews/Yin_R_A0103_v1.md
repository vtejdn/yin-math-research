---
author: Yin
---

# Polarized renewal means and uniform tests for closed range

At 2026-11-17T03:31 UTC a separate agent reviewed all of the fixed [C67](../../claims/Yin_C_A0067_v1.md) for Sheng Yin, including the closed-range equivalence and both cyclic examples.
The reviewer prepared the GV17 bibliography and checked its normalization and previously worked on the four-line constructions.
The reviewer did not develop C67 or receive its proof-development dialogue, author explanations or an earlier assessment of it.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [C67 statement](../../claims/Yin_C_A0067_v1.md#statement) | All group and matrix hypotheses, arbitrary nonnegative weights, cutoff, signed means, and the two stronger tests at exponent strictly above three. |
| [Whole-argument finding](#whole-argument-finding) | [C67 argument](../../claims/Yin_C_A0067_v1.md#argument) | Rank-one padding, sign and phase of polarization, renewal coefficients and reciprocals, original finite product fibers and finite intervals. |
| [Whole-argument finding](#whole-argument-finding) | [C67 closed-range equivalence](../../claims/Yin_C_A0067_v1.md#two-stronger-tests-characterize-closed-range) | Uniform Abel estimates versus endpointwise convergence, the rapid-decay norm obstruction, and the converse analytic extension and summation of absolute coefficients. |
| [Whole-argument finding](#whole-argument-finding) | [C67 cyclic examples](../../claims/Yin_C_A0067_v1.md#time-cancellation-on-a-gapless-cyclic-direction-of-a-four-line-group) | Infinite cyclic nonclosed range, both exact contrasts, timewise and Abel lower bounds, the positive kernel and its nonidentity off-diagonal coefficient. |
| [Whole-argument finding](#whole-argument-finding) | [L55 integrality](../../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace) | Operative exponent and unnormalized trace under the weighted-square tail bound. |
| [Whole-argument finding](#whole-argument-finding) | [C57 rapid-decay shell bound](../../claims/Yin_C_A0057_v1.md#interchanging-the-scales-forces-a-spectral-gap) | Weighted-square tails and extension by norm truncation. |
| [Whole-argument finding](#whole-argument-finding) | [C59 cyclic metric bound](../../claims/Yin_C_A0059_v1.md#statement) | Infinite order, lower bound on ambient lengths of powers, and availability of the second generator on the selected event. |

## Whole-argument finding

The source comparison covers the time-weighted rank-one convention for the authors' operator first-return function. [GV17, Theorem 2.5, equation (26)](../../literature/pdf/GV17--arxiv-v2.pdf#page=18)

For \(g\ne e\) the endpoints are orthogonal even when their coordinate indices coincide.
On the padded space, the upper-left Schur complement of \(I-zK\) in the probe direction gives \(1-z\eta^*K\eta-z^2b^*(I-zC)^{-1}b\).
Its reciprocal is the probe Green function.
Thus the return series is \(z\) times the GV17 first-return function and has no constant term.
The expansion gives \(f_1=\eta^*K\eta\ge0\) and \(f_n=b^*C^{n-2}b\ge0\) for \(n\ge2\), including when \(C\) has norm one.
The atom \(a=(1+\xi^*p\xi)/2\) lies in \([1/2,1]\), so dominated convergence for \((1-z)/(1-zt)\) on the spectral interval gives \((1-z)h(z)\to a\).
Consequently \(f(z)\uparrow1\).
Summing \(f_n(1+\cdots+z^{n-1})\) and using monotone convergence gives first mean \(1/a\).
This proves finiteness of both unsigned first means at each endpoint, hence absolute convergence of the signed time series there.

The two unpadded quadratic forms differ by \(2\operatorname{Re}(\zeta x^*py)\).
The padding divides their difference by two, giving \(a_+-a_-=\operatorname{Re}(\zeta x^*py)\).
Taking reciprocals gives precisely \(m_- -m_+=(a_+-a_-)m_+m_-\).
The phase \(i\) contributes the negative imaginary part, whose square is the required second summand of the modulus.
The product of the means is between one and four, giving factors one and sixteen for the squared sums.
The strict inequality \(nw<|g|\) makes both off-diagonal \(H^n\) entries zero.
The triangular recursion then agrees through all those times, so the first retained integer is \(\lceil |g|/w\rceil\), including exact multiples of \(w\).
Binomially expanding \(H^n\) and multiplying the finite arrays for \(A^*A\) supplies every required entry from matrix-indexed paths whose products coincide in the actual group.
The constant in \(h_n\) is an additional stationary contribution, not a trace approximation.
The conclusion presupposes actual finite product-fiber information and supplies no uniform algorithm for recognizing words in arbitrary presentations.
Also \(L_N=\sum_n\min(n,N+1)f_n\), which increases from one to the true mean and verifies both reciprocal interval endpoints.
Adding the finite identity coefficient to the exterior sum permits the stated L55 application.

For real Abel parameter, \(a_\pm(z)\in[1/2,1]\) by positivity.
The signs reverse between the difference of means and \(f^+(z)-f^-(z)\) in precisely the way given by the two reciprocals.
Polarization yields the two components of \(R_z\) with the same bounded denominators, and its identity coefficient is uniformly bounded.
For any bounded sequence of the weighted spatial sums, the C57 shell bound on the fixed good group makes the operator-norm Fourier tails uniformly small since \(\beta>3\).
Finite truncations justify the same bound for coefficients with finite weighted square sum, identifying their operator limit by trace \(L^2\) convergence.
Spectral convergence \(R_z\to p\) in trace \(L^2\) controls each coefficient in a fixed finite ball, hence would force operator-norm convergence along the chosen sequence.
On the complement of the kernel the scalar Abel multiplier approaches one along the spectrum whenever the positive spectrum of \(A^*A\) accumulates at zero.
Its norm there is then exactly one at every \(0<z<1\), contradicting the proposed convergence.
The implication from absolute timewise sums uses zero total difference of the two return distributions and \(1-z^n\le n(1-z)\) before the spatial sum.

In the closed-range direction the spectral gap bounds \(\|H^k-p\|\le\theta^k\) with a chosen \(0<\theta<1\).
Finite propagation gives the exterior unweighted square mass of \(p\) beyond \(kw\) at most \(m\theta^{2k}\).
Summing on shells of width \(w\) adds only a polynomial factor in \(k\), as does the weighted mass inside the ball of \(H^k-p\).
Thus the asserted exponential estimate in weighted coefficient norm holds with any \(\theta<\theta_1<1\).
It continues \(R_z\) analytically to \(|z|<1/\theta_1\) after the atom has been separated.
For complex \(z\) the proof correctly uses the two entries of the polarized form without applying a nonholomorphic real part to the continuation.
The second entry amounts to interchanging matrix indices and inverting \(g\), both weight-preserving operations.
On the closed unit disk the real part of \((1-z)/(1-zt)\) is nonnegative for \(0\le t\le\theta\), so the stationary mass gives a uniform positive real part for each denominator.
For \(1<r'<1/\theta_1\), its derivative in \(z\) is bounded by \((1-r'\theta)^{-2}\) throughout \(|z|\le r'\).
Moving radially a sufficiently small fixed distance from the unit disk therefore retains modulus at least \(1/4\) uniformly in the probe.
The continued difference of the return functions on a common circle \(1<r<r'\) has bounded weighted square norm.
Cauchy's coefficient formula, followed by the triangle inequality in weighted \(\ell^2\), bounds the array at time \(n\) by \(Cr^{-n}\).
Summing \(nCr^{-n}\) justifies the spatial norm of the sum of timewise absolute values, establishing both closed-range equivalences.

For \(A=1-u\), the quoted C59 event makes all positive powers distinct and gives \(|u^r|\ge cr\).
The cyclic Fourier shift yields injectivity with nonclosed range and \(H=(2+u+u^{-1})/4\).
The decaying solution of the three-term resolvent equation has ratio \((1-\sqrt{1-z})/(1+\sqrt{1-z})\), and the unit source at zero fixes its prefactor as \(1/\sqrt{1-z}\).
Padding the two real endpoint probes gives (6), with positive numerator \(4s^3 b_z^r\) and a denominator tending to one as \(s\downarrow0\).
Both first means are two and their exact difference vanishes.
At \(s=1/r\), the timewise absolute first moment exceeds a fixed multiple of \(1/r\), giving divergence of \(\sum_r r^{\beta-2}\) for \(\beta\ge1\).
At a common \(s\), the \(r\)'s in \([1/s,2/s]\) have \(b_z^r\) bounded below, yielding the claimed lower bound of order \(s^{1-\beta}\) on the squared Abel norm and divergence for \(\beta>1\).

For the row example \(SS^*=I\) and \(A^*A/8=S^*((1-u)^*(1-u)/4)S\).
This gives the stated decomposition of \(H^n\), nullity one and \((H^n)_{11}=(I+H_0^n)/2\), also at \(n=0\).
The unpadded real probes in this coordinate have mass \(1/2\) at the kernel, giving padded mass \(3/4\) and mean \(4/3\).
Taking reciprocals of the two displayed Green functions gives the factor \(8s^3 b_z^r\) and denominator \((3+s)^2-s^2b_z^{2r}\), which again gives both lower bounds.
Finally \(p_{12}=v/2\), so the nonidentity coefficient claimed for the full projection coexists with the zero diagonal contrast at the designated distant endpoints.
The fixed argument supports C67 in full, including the distinction between the exact coefficient identity and the stronger uniform tests that force a gap.

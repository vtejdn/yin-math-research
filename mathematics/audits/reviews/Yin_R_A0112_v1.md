---
author: Yin
---

# Review of finite signed first-return sums on spatial shells

At 2026-11-17T03:52 UTC an agent outside the development of Yin_C_A0076_v1 independently checked the fixed statement, the two proof sections and the application for Sheng Yin.
The reviewer had independently reviewed C74, which supplies the final example, and had received no development account, previous verdict or draft proof of C76.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0076_v1.md#statement) | Unconditional sum of squared time-prefix norms, infinite dyadic hypothesis, radius-dependent finite cutoff, exponent of the exterior error, and both comparisons with the projection. |
| [Whole-argument finding](#whole-argument-finding) | [Joint square bound](../../claims/Yin_C_A0076_v1.md#the-joint-square-bound-across-time-and-endpoints) | Real part of the scalar denominator on the open disk, analytic polarization, both phases, unnormalized matrix trace and radial Parseval bound. |
| [Whole-argument finding](#whole-argument-finding) | [Spatial shell proof](../../claims/Yin_C_A0076_v1.md#passing-from-finite-returns-to-a-spatial-shell) | Spectral sublevels from dyadic increments, real Abel limit in the joint coefficient norm, time tail, spatial weight and application. |
| [Whole-argument finding](#whole-argument-finding) | [Renewal identity and first means](../../claims/Yin_C_A0067_v1.md#argument) | Padded probability measure, scalar generating series and the sign, normalization and two-phase comparison at the endpoint. |
| [Whole-argument finding](#whole-argument-finding) | [Resolvent contrast](../../claims/Yin_C_A0067_v1.md#two-stronger-tests-characterize-closed-range) | Real-parameter quotient and the polarized numerator that continues analytically for nonreal parameters. |
| [Whole-argument finding](#whole-argument-finding) | [Original-group application](../../claims/Yin_C_A0074_v1.md#resolvent-of-the-original-product-fibers) | Positive spectral mass of the normalized matrix away from its kernel, nonclosed range and failure of all the finite-power tests. |
| [Whole-argument finding](#whole-argument-finding) | [Signed spatial decay in the example](../../claims/Yin_C_A0074_v1.md#taking-the-signed-time-sum-at-its-endpoint) | Actual exponential localization of the limiting signed means for that family. |

## Whole-argument finding

Each finite prefix \(b_n\) vanishes outside the propagation radius of \(Q^n\), by equality of the two probe recursions before the spatial endpoints can interact.
The generating series of the prefixes is \((f^+-f^-)/(1-z)\).
The stationary mass contributes at least \(1/2\) to the real part of each denominator throughout the unit disk, since the rest of the spectral integrand has nonnegative real part there.
In particular the scalar renewal identity has no zero-denominator singularity on the disk.
For nonreal \(z\), polarization gives the sum of the two cross coefficients with conjugate **phase** factors and with \(R_z\) in both terms.
Replacing it by the real part of one coefficient would destroy analyticity.
The reversed endpoint coefficient is the \((j',i)\) entry at \(g^{-1}\), so the full two-phase polarized array has norm at most \(\sqrt2\|R_z\|_2\).
The geometric resolvent multiplier has modulus at most two for \(0\le s\le1\), whence \(\|R_z\|_2\le2\sqrt m\).
Division by the two factors of modulus at least \(1/2\) gives squared norm at most \(128m\).
Integrating scalar Parseval at radius \(r<1\), summing nonnegative terms and letting \(r\uparrow1\) establishes (1) for all inputs, including those without a spectral gap.
Cauchy–Schwarz in time gives the asserted full-spatial-norm truncation estimate directly from (1).

For (2) the positive dyadic increments telescope in trace to \(\tau_m(Q^{2^j}-p)\), since spectral convergence removes the stationary mass.
For \(2^j\le 1/t<2^{j+1}\) and \(0<t\le1/2\), the multiplier on the positive sublevel \((0,t]\) is at least \(1/4\) and \(2^{-j}<2t\).
This gives the \(O(t^\alpha)\) sublevel bound, extended to \(t>1/2\) by the finite total trace.
For real \(1/2\le z<1\) put \(v=1-z\).
The squared remainder multiplier on \((2^q v,2^{q+1}v]\) is \(O(2^{-2q})\) uniformly for \(z\ge1/2\), so the sublevel estimate yields \(O(v^\alpha)\) for its squared trace norm precisely in the claimed range \(0<\alpha<2\).
The remainder matrix is positive.
For either two-site unit probe its expectation is at most twice the matrix trace by the translated diagonal estimates and Cauchy–Schwarz.
After padding, the variation in each denominator from its limit is therefore at most \(\sqrt m\|R_z-p\|_2\), uniformly over all sites and phases.
The reciprocal products vary by this same order and multiply the fixed square-summable array of polarized \(p\)-coefficients.
Together with polarization of \(R_z-p\) this bounds the joint Hilbert-space error.
The endpoint sign is consistent with \(d\) being the minus first mean minus the plus first mean.

At radius \(2^j\) the squared time tail is bounded by a constant times \(2^{\kappa j}e^{-2L(j+1)}\), from \(1-z_j^2\ge 2^{-\kappa j}\) and the chosen \(N_j\).
The lower bound on \(L\) makes this \(O(2^{-\kappa\alpha j})\), the squared order of the separate real-Abel error.
Restricting those two joint bounds to one shell costs only its maximum weight \(O(2^{\beta j})\).
Summation is geometric under \(\kappa\alpha>\beta\), with the factor \(1/2\) in (3)'s exponent coming from the square root.
The two-phase comparison in C67 and the triangle inequality give the exterior comparisons also as extended norms.
The polynomial in the radius bounds the maximum time index on a particular shell, including its logarithmic factor.
The argument supplies neither a polynomial operation count for enumerating a whole shell nor a finite verification of the infinite family (2).
For the C74 rows, scaling the positive spectral variable by \(M\) preserves its sublevel exponent \(1/(2d)\).
Integration against that bound gives \(O(n^{-1/(2d)})\) for \(\tau_m(Q^n-p)\), which bounds the required dyadic increments.
Consequently this application passes while its signed limiting array has the independently established exponential spatial decay.
The fixed statement and both proof sections pass at their stated scopes.

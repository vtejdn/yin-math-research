---
author: Yin
---

# Finite kernel witnesses and certified errors for signed first-return shells

At 2026-11-17T04:42 UTC an agent outside the development of Yin_C_A0084_v1 independently reviewed the fixed statement and all three proof sections for Sheng Yin.
The reviewer previously inspected the cyclic-minor and lattice examples in their own materials.
The review used the fixed claim and its direct mathematical inputs.
No proof-development dialogue, author explanation or prior finding on this claim was supplied.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0084_v1.md#statement) | Finite certification, the either-kernel density guarantee, whole-array error and both weighted exterior comparisons. |
| [Whole-argument finding](#whole-argument-finding) | [Finite trace bounds](../../claims/Yin_C_A0084_v1.md#finite-lower-bounds-on-the-unknown-trace) | Finite group equations, support projections, unnormalized rectangular index and exact smaller deficiency. |
| [Whole-argument finding](#whole-argument-finding) | [Finite error](../../claims/Yin_C_A0084_v1.md#a-fully-finite-error-bound-at-all-endpoints) | Polynomial majorant, exact infimum, signed Abel comparison and constants, time truncation and weighted shell sum. |
| [Whole-argument finding](#whole-argument-finding) | [Scope on examples](../../claims/Yin_C_A0084_v1.md#scope-on-matrices-with-nonclosed-range) | Dense-range termination, the distinction between prior estimates and certificate error, and the blocked full-matrix example. |
| [Whole-argument finding](#whole-argument-finding) | [Signed first-return means](../../claims/Yin_C_A0067_v1.md#statement) | Oppositely signed cumulative sums, exact two-phase comparison with the original projection. |
| [Whole-argument finding](#whole-argument-finding) | [Joint square bound](../../claims/Yin_C_A0076_v1.md#the-joint-square-bound-across-time-and-endpoints) | Polarization and denominators of the original probes, the generating function and the joint \(128m\) estimate. |
| [Whole-argument finding](#whole-argument-finding) | [Cyclic minor](../../claims/Yin_C_A0081_v1.md#statement) | Dense range of the input matrix. |
| [Whole-argument finding](#whole-argument-finding) | [Free-subgroup row products](../../claims/Yin_C_A0082_v1.md#statement) | Exponential square localization of the actual projection. |
| [Whole-argument finding](#whole-argument-finding) | [Dimension-four comparison](../../claims/Yin_C_A0068_v1.md#statement) | Polynomial exterior squared tail and absence of a reduced-algebra closed-range representative. |
| [Whole-argument finding](#whole-argument-finding) | [Two-row map](../../claims/Yin_C_A0064_v1.md#the-row-map-and-its-kernel) | Dense nonclosed range, nullity one and absence of nonzero finite null vectors. |
| [Whole-argument finding](#whole-argument-finding) | [Two-row localization](../../claims/Yin_C_A0064_v1.md#a-tail-estimate-from-one-finite-moment) | Exponential spatial estimate for its kernel projection. |

## Whole-argument finding

The complete argument establishes the stated finite certificate and characterizes when this procedure can reach arbitrary positive accuracy.
A vector supported in the radius-\(s\) ball can produce nonzero entries of \(Bx\) only within radius \(s+w\).
The nullspace of those finite equations therefore gives exact polynomial columns \(W_s\) with \(BW_s=0\), on either side of the rectangular problem.
The support projection of \(W_sW_s^*\) is the projection on the closed span of the right translates of its columns.
On the spectrum in \([0,b_s)\), the increasing functions \(1-(1-t/b_s)^k\) converge to the indicator of \(t>0\).
They give finite polynomial lower bounds on the kernel projection even if its column span has smaller dimension.
The supports increase with the ball through all finite null vectors, and normality yields the claimed supremum of the finite traces.

The initial and final projections of the rectangular polar partial isometry have equal unnormalized traces, so \(m-d_A=r-d_{A^*}\).
Taking the larger of the two computable lower traces gives exactly the smaller of the two density defects after optimizing.
Faithfulness makes a zero defect equivalent to equality of the corresponding closed submodule with the full Hilbert kernel.
This includes the zero kernel of either \(A\) or \(A^*\).
All trace expressions at finite indices come from identity coefficients of finite products.

For \(0\le Q\le I\) the discarded Abel tail is a positive operator bounded by \(z^{K+1}I\).
Thus \(U_{z,K}\ge R_z\ge p\), and commutation allows their squares to be compared.
Moreover \(R_zp=p\), so \(\|R_z-p\|_2^2=\tau_m(R_z^2)-d_A\).
For fixed \(z\) the polynomial upper bound converges in norm to \(R_z\).
Along rational \(z\uparrow1\), spectral convergence gives \(\tau_m(R_z^2)\to d_A\).
These upper approximations are independent of the two lower witnesses, so the infimum of \(v\) equals (2), including when both defects are positive.

The sign in \(b_n\) produces the generating function \(C(z)=(f^+(z)-f^-(z))/(1-z)\).
Its limit has the signed mean \(m_- -m_+\) by the two unit masses of the return laws and their finite first means.
For positive \(R_z-p\), the two-site quadratic form in a padded denominator is bounded uniformly by \(\tau_m(R_z-p)\), accounting for the padding factor \(1/2\).
The latter trace is at most \(\sqrt m\,\|R_z-p\|_2\).
The reciprocal product on \([1/2,1]^2\) has partial derivatives of magnitude at most eight.
Polarization has norm at most \(\sqrt2\) jointly over all entries, endpoints and both phases, and \(\|p\|_2\le\sqrt m\).
These bounds give \(4\sqrt2+16\sqrt2\,m\le32(m+1)\) as a valid coefficient multiplying \(\|R_z-p\|_2\) in the Abel error.
Cauchy–Schwarz in time with the \(128m\) joint square bound gives exactly the other term of (3).
For a chosen \(z<1\) this term tends to zero with \(N\), so enumeration with certified finite arithmetic reaches any strict positive tolerance when (2) vanishes.
A positive defect gives a strictly positive lower limit for the displayed error bound.

Restriction of this single global error to a shell is contractive.
Its weighted norm there is bounded by \(2^{\beta(j+1)/2}2^{-(\beta/2+\eta)j}\), using the integral group word length.
Summing the squares over disjoint shells gives the \(O_{\beta,\eta}(2^{-\eta J})\) exterior norm error.
The norm of the exact signed array lies between one and four times the projection norm by C67, with the same weight and exterior.
The triangle inequalities in both directions therefore control the measured norms and the true norm as stated.
This argument requires a bound or a measurement on every relevant shell to deduce summability.

Dense range in the cyclic-minor and product-lattice cases makes the adjoint kernel zero and thus suffices for termination.
For the free-subgroup row-product case the exponential tail controls the exact array, and then the certified shell errors control the measured array at \(R=2^J\).
For the four-dimensional product group the cited rate is for a squared norm, giving a measured norm \(O(R^{(\beta-4)/2}+R^{-\eta})\) at \(0\le\beta<4\).
Finally \(A_0\) is a two-row, three-column operator with dense nonclosed range, no finite null vectors and nullity one.
In \(A_0\oplus A_0^*\) the two full kernels, for the matrix and its adjoint, each have dimension one and both finite-vector modules vanish, since any finite vector would give a finite vector in each block.
Hence (2) equals one on this full matrix, although the kernel projection is the exponentially localized projection of \(A_0\) in one block and zero in the other.
The example concerns the displayed full-matrix certificate, for which better spatial behavior alone does not lower the trace infimum.

---
author: Yin
---

# Identical row Gram matrices and different kernel projections on a product group

At 2026-11-17T03:21 UTC an agent outside the development of Yin_C_A0068_v1 independently reviewed the fixed statement and all three proof sections for Sheng Yin.
The reviewer received no development dialogue, author explanation or prior finding about this claim.
The reviewer had previously checked the endpoint-series definition and the earlier torus example in C56.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0068_v1.md#statement) | Both lattice dimensions, the two rational matrices, equality of scalar return data, critical weighted moments, schedule threshold and arbitrary finitely generated product factor. |
| [Whole-argument finding](#whole-argument-finding) | [Gram matrices](../../claims/Yin_C_A0068_v1.md#matrices-with-identical-row-products) | Walsh coefficients, exterior-algebra factorization, dimensions, spectra, range and constant comparison projection. |
| [Whole-argument finding](#whole-argument-finding) | [Endpoint coefficients](../../claims/Yin_C_A0068_v1.md#grouped-endpoints-and-adjacent-times) | Exact block polynomial, uniform annular multiplier estimates, shell and tail summation, and upper and lower increment estimates. |
| [Whole-argument finding](#whole-argument-finding) | [Critical moment and support](../../claims/Yin_C_A0068_v1.md#the-discontinuity-the-critical-exponent-and-support) | Directional discontinuity, exclusion of every closed-range representative, fourth-moment divergence, three-dimensional threshold and independently translated support. |
| [Whole-argument finding](#whole-argument-finding) | [Endpoint series](../../claims/Yin_C_A0062_v1.md#statement) | Endpoint weight and squared time increments of the same normalized column Gram operator. |

## Whole-argument finding

The coefficients of the finite unitary \(U\) are rational because each Walsh entry enters in a product of two entries, contributing \(\pm1/N\).
Exterior multiplication and contraction give \(\{e_i,e_j^*\}=\delta_{ij}I\), so the central coefficients \(1-z_i\) give \(L^2=\ell I\) with the positive lattice Laplacian.
This is the lattice Hodge–Dirac square, also treated by [Miranda and Parra, §3, Lemma 3.1](https://arxiv.org/pdf/2304.00153#page=12).
The two constructed row Gram matrices therefore agree exactly.
Their positive column spectral measures agree by polar decomposition, and the equal numbers of columns give equal zero masses.
Since \(\ell\) vanishes only at a torus point of measure zero and takes arbitrarily small positive values, the final projections are \(I_N\), the ranges are dense and nonclosed, and the unnormalized nullities are \((d-1)N\).
The zero block columns of \(A_0\) account for its entire kernel.

Expanding a power of \(I-A^*A/M\) through \(AA^*=\ell I\) gives (1), so signed lattice amplitudes at the same endpoint are added before squaring.
On an annulus of radius \(t\), each order-\(s\) derivative of the quotient \(\overline a_i a_j/\ell\) costs \(O(t^{-s})\).
Differentiation of \(q^k\) costs the same powers of \(t\) times bounded functions of \(kt^2\), uniformly in \(k\), because \(M>4d\) and \(1-q\) is quadratic at zero.
Cutting into annuli, \(L>d\) integrations by parts give bounds \(Ct^d(1+t|x|)^{-L}\) whose geometric sum is \(O((1+|x|)^{-d})\).
The limiting quotient satisfies the same estimates away from the one puncture, which has zero measure.
The finite support in \(H\) is fixed as \(k\) varies, and the product word length shifts the lattice radii by only finitely many fixed offsets.
This gives the squared shell estimate \(O((1+r)^{-d-1})\).
In dimension four the shells up to \(R\) give the logarithm in the endpoint bound, while shells beyond \(R\) give \(O(R^{-4})\) and the stated \(O_\beta(R^{\beta-4})\) projection tail.

The exact squared increment is the torus integral of \(Nq^{2k}(1-q^{l-k})^2\).
When \(l/k\) remains bounded above and bounded away from one, a ball of radius \(O(k^{-1/2})\) gives the Gaussian upper scale \(k^{-d/2}\), with the complement controlled by Gaussian decay.
A fixed annulus at radius comparable to \(k^{-1/2}\) supplies the matching lower bound.
On the prescribed geometric schedule rounding leaves \(l/k\to2^\kappa>1\), so convergence holds exactly for \(2\kappa>\beta\), including divergence at equality.

On the punctured torus each diagonal projection block is continuous, but two coordinate directions give different limits at the missing point.
Full support of Haar measure rules out a continuous representative even after allowing operator-valued entries over \(H\).
A closed-range Gram operator has a kernel projection given by continuous functional calculus, excluding any such representative with the same kernel.
In dimension three, a spatial moment with \(\beta>3\) would give an absolutely convergent Fourier series for the diagonal and hence continuity.
In dimension four, the \(C^2\) rescaling of the diagonal symbol on a fixed unit annulus gives a second derivative of size at least \(c|\xi|^{-2}\) throughout a cone about a different coordinate axis.
Its squared integral diverges on that cone, excluding the fourth moment by Parseval.

The input entry containing \(U_{11}\) recovers all generators of \(H\) from differences at one lattice coordinate, and the scalar difference entries recover the central generators \(z_i\), including \(z_1\) in the first entry.
For the projection, one nonzero lattice coefficient of the \(21\) block similarly carries all generators of \(H\).
Each scalar diagonal has a positive identity coefficient, and conditioning on the other coordinates gives a strictly positive first cosine coefficient by strict positive covariance of \(\cos\xi_i\) with \(s/(s+2-2\cos\xi_i)\).
Thus support differences recover \(z_i\) on each diagonal.
Independent left and right translations only conjugate these differences, and the recovered subgroups \(H\times\{0\}\) and \(\langle z_i\rangle\) are normal in the product.

The statements about endpoint coefficients, kernel discontinuity and support hold for the constructed matrices on \(H\times\mathbb Z^d\).
For four-line \(H\) the proof requires the indicated external lattice factor.

---
author: Yin
---

# Internal review of the retained affine determinant reformulations

Review performed: 2026-10-21T00:26.
Human record author: Yin.
The maintenance agent read the full L_F0028 and L_F0031 arguments, the exact C_F0124 strict-domain, approximation and complex-coefficient interfaces, and the entire original R_F0123.
It assembled the three current C statements and proof homes and then checked their complete arguments and interfaces below.
That assembly and mathematical involvement make these findings self-reviewed.
No isolated independent arrangement, new source proof, numerical experiment or formal verification is claimed.
The source proposal attribution, accepted Dyson/global-comparison/capacity interfaces, original dates and older fixed L review inputs are retained.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Full positive cone](#positive-cone-finding) | self-reviewed |
| [Two positive matrices](#two-positive-matrices-finding) | self-reviewed |
| [Scalar infimum and obstructions](#scalar-obstructions-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Full positive cone](#positive-cone-finding) | [C_F0164 statement](../../claims/Yin_C_F0164_v1.md#statement) | Exact strict-domain certificate equivalence, whole-cone bijection, inverse and ordered formulas, full centered reduction and disclosed complex extension. |
| [Full positive cone](#positive-cone-finding) | [C_F0164 argument](../../claims/Yin_C_F0164_v1.md#argument) | Complete retained L_F0031 Sections 1-4 proof with C_F0124 accepted at its exact strict-domain theorem scope. |
| [Two positive matrices](#two-positive-matrices-finding) | [C_F0165 statement](../../claims/Yin_C_F0165_v1.md#statement) | Arbitrary affine complex semicircular coefficients, all positive X,Y, real quadratic inner maximum, circular elimination and zero-drift capacity formula. |
| [Two positive matrices](#two-positive-matrices-finding) | [C_F0165 argument](../../claims/Yin_C_F0165_v1.md#argument) | Entire domain-surjectivity, physical diagonal approximation, real Legendre computation and capacity argument retained from L_F0028 Sections 2-4. |
| [Scalar infimum and obstructions](#scalar-obstructions-finding) | [C_F0166 statement](../../claims/Yin_C_F0166_v1.md#statement) | Entire scalar elliptic infimum including line/no-noise/zero cases, fixed-noise phase obstruction and explicit divergent joint M2 maximum. |
| [Scalar infimum and obstructions](#scalar-obstructions-finding) | [C_F0166 argument](../../claims/Yin_C_F0166_v1.md#argument) | Complete independent Dyson-root/primitive limit and the two exact counterexample computations retained from L_F0028 Sections 5-7. |

## Positive cone finding

The proof fixes selfadjoint finite coefficients and normalized trace, so the covariance is completely positive and Hilbert--Schmidt selfadjoint.
The strict certificate becomes W-Psi(W)>0 after congruence; similarity by W's square root gives a strictly subunital positive map, hence spectral radius below one.
The converse additionally needs C_F0124's absolute control of negative eigenvalues; strict positivity of I-Psi alone would not suffice for a general selfadjoint linear map.
With that accepted positive-map fact, the completely positive Neumann inverse gives q>0 from its zeroth term, with the equation normalized to I.
Uniqueness of the positive square root gives the unique positive b solving bqb=I+eta(q), and both compositions establish a bijection.
The determinant exponent is 1/(2d), and the plus map has a strictly positive real Hermitian quadratic form.
Completing its square proves a finite unique inner maximum with the written order of extrema; no minimax interchange is used.
The zero-mean ratio is bounded below by capacity and approaches each fixed shape's capacity ratio by scalar scaling to infinity.
Singular outputs, zero capacity and nonattainment are included by this two-stage infimum argument.
The arbitrary complex extension uses the accepted hermitization/capacity-square interface, retaining all covariance blocks.
The full original R_F0123 Section 2 agrees with this unchanged argument and its dependency boundary.
The exact current statement is proved at that accepted input depth; this is a dependent reformulation of C_F0124, with no second global comparison or independent discovery asserted.

## Two positive matrices finding

The two positive square roots solve PXP-eta(Y)=I and QYQ-eta*(X)=I in the exact written order.
For every positive X,Y this is a strict certificate on the full 2m-dimensional hermitized Hilbert--Schmidt space, not only on diagonal blocks.
Conversely the positive Neumann solution for an admissible diagonal b remains diagonal by invariance, and uniqueness of its two positive square roots recovers precisely X,Y.
Restricting b to diagonal blocks does not discard the determinant infimum: the actual hermitized resolvent has off-diagonal real and diagonal positive imaginary blocks, so the exact C_F0124 approximating b is diagonal.
The global lower bound is inherited from that theorem, including minus infinity values, rather than inferred from stationarity.
The plus-map completion is on the real Hermitian space.
Its off-diagonal restriction gives Re tr(a0*Z), the two half-quadratic terms and the equation PZQ+rho(Z*)=a0 with the normalized 2m-to-m factors correct.
The variable rho(Z*) is real linear; no complex-linear differentiation is used.
Strict definiteness proves existence, finiteness and uniqueness of the inner maximum at every positive pair.
Determinants of the certificate equations give exactly the 1/(4m) logarithmic coefficient.
For rho=0 ordinary multiplication solves Z and yields the circular term.
At zero drift independent positive trial variables factor the two nonnegative infima; scalar scaling permits singular outputs and zero capacity, and the disclosed capacity duality equates eta and eta*.
This proves the complete statement at its stated C_F0124/capacity input scope, with no outer attainment, independent global proof or phase-insensitive generalization added.

## Scalar obstructions finding

The scalar proof uses the physical C_F0119 Dyson equation and primitive directly, without C_F0124 or C_F0165.
Equality of the two tracial singular-value laws gives equal positive diagonal imaginary parts.
Inversion gives (r-v)q=epsilon, rh+t conjugate(h)=a and r(q^2+abs(h)^2)=1, so r>v.
On that open domain every nonzero term of the scalar root equation decreases, the epsilon term forces divergence at v, and the sum tends to zero at infinity; the regularized root is unique.
The derivative of f has the stated sign, so the limiting root or boundary gives its global infimum.
Substitution in the primitive gives f(r)+epsilon*q/2; q^2<=1/v for v>0 makes the correction vanish.
The tracial regularized logarithmic determinant decreases to the ordinary extended-real value.
The line case is handled on the open domain with zero numerator absent; the noiseless scalar infimum separately gives log(abs(a)), including minus infinity at zero.
For the fixed elliptic family v=1 and 0<t<1, shifts r and ir with 0<r<1-t have different explicit potentials despite identical modulus and noise, disproving the asserted radial-only mechanism.
For the joint matrix maximum, W=Q^(1/2)PQ^(1/2) and D=Q^(-1/2)aQ^(1/2) reduce the fixed-Q optimization to two scalar phi values by concavity and sign averaging.
With Q=exp(2uX) and aX=-Xa the singular values are exp(2u),exp(-2u); the supremum 4u+exp(-4u)-1 diverges.
The actual diagonal circular pencil has two boundary scalar logarithmic determinants zero by the proved scalar formula, so its normalized logarithmic determinant is zero.
Both failure scopes are exactly those stated; neither rules out ordered optimization or the general mathematical Task.
No unresolved mathematical issue affecting these exact retained assertions was found in this internal review.

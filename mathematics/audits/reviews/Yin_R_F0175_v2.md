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
| [Circular Schur minimum](#circular-schur-finding) | self-reviewed |
| [Circular convolution and signature failure](#circular-signature-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Full positive cone](#positive-cone-finding) | [C_F0164 statement](../../claims/Yin_C_F0164_v1.md#statement) | Exact strict-domain certificate equivalence, whole-cone bijection, inverse and ordered formulas, full centered reduction and disclosed complex extension. |
| [Full positive cone](#positive-cone-finding) | [C_F0164 argument](../../claims/Yin_C_F0164_v1.md#argument) | Complete retained L_F0031 Sections 1-4 proof with C_F0124 accepted at its exact strict-domain theorem scope. |
| [Two positive matrices](#two-positive-matrices-finding) | [C_F0165 statement](../../claims/Yin_C_F0165_v1.md#statement) | Arbitrary affine complex semicircular coefficients, all positive X,Y, real quadratic inner maximum, circular elimination and zero-drift capacity formula. |
| [Two positive matrices](#two-positive-matrices-finding) | [C_F0165 argument](../../claims/Yin_C_F0165_v1.md#argument) | Entire domain-surjectivity, physical diagonal approximation, real Legendre computation and capacity argument retained from L_F0028 Sections 2-4. |
| [Scalar infimum and obstructions](#scalar-obstructions-finding) | [C_F0166 statement](../../claims/Yin_C_F0166_v1.md#statement) | Entire scalar elliptic infimum including line/no-noise/zero cases, fixed-noise phase obstruction and explicit divergent joint M2 maximum. |
| [Scalar infimum and obstructions](#scalar-obstructions-finding) | [C_F0166 argument](../../claims/Yin_C_F0166_v1.md#argument) | Complete independent Dyson-root/primitive limit and the two exact counterexample computations retained from L_F0028 Sections 5-7. |
| [Circular Schur minimum](#circular-schur-finding) | [C_F0167 statement](../../claims/Yin_C_F0167_v1.md#statement) | Every positive trial for arbitrary affine matrix circular noise, unique regularized minimum, ordered Schur form, full centered capacity and exact order-of-limits boundary. |
| [Circular Schur minimum](#circular-schur-finding) | [C_F0167 argument](../../claims/Yin_C_F0167_v1.md#argument) | Complete L_F0032 physical identities, Jensen comparison, left-right spectral calculus, ordered completion and limiting argument; exact HP03/C_F0119 interfaces. |
| [Circular convolution and signature failure](#circular-signature-finding) | [C_F0168 statement](../../claims/Yin_C_F0168_v1.md#statement) | Strict-Hilbert--Schmidt-positive circular infimal convolution, explicit indefinite raw-signature saddle failure and the limited local balancing observation. |
| [Circular convolution and signature failure](#circular-signature-finding) | [C_F0168 argument](../../claims/Yin_C_F0168_v1.md#argument) | Entire L_F0030 circular primitive/limit identification, exact covariance spectrum, local implicit-function/Hessian computation and candidate-failure distinctions. |

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

## Additional review performed

The two following complete findings were performed at 2026-10-21T00:28 after full reading of L_F0030/L_F0032, the complete original R_F0123/R_F0125 and C_F0125's exact matrix continuation and limiting interfaces.
They are new current mathematical findings, not a redating or expansion of the first three findings or the original September reviews.
The same maintenance agent assembled the current C homes, so these two findings are also self-reviewed.

## Circular Schur finding

The signed inverse has positive top diagonal expectation and negative bottom diagonal expectation, making its Schur complement invertible.
Boundedness of the pencil gives strict positive lower bounds on P0 and Q0, and the real-gap Dyson primitive is justified by the actual bounded inverse, rather than a formal real root.
Circular decomposition cancels both mixed covariance blocks, while the diagonal maps are eta and eta* in the written order.
Block inversion gives all three physical equations; signed Schur multiplicativity yields the regularized determinant with the exact 2m normalization.
The primitive's trace term and the last physical identity then identify V(Q0).
For arbitrary positive Q, the exact difference has the displayed signs and the normalization Q0+M*M+Phi*(W)=I with W>0.
Unital-column Jensen applies to h(t)=t-log(t)-1 on the positive open interval after adding the defect square root with input I; no value at zero is required.
The last correction is the Hilbert--Schmidt quadratic form of h(D), with D(X)=R^(-1)XU a product of commuting positive left/right multiplication operators.
Its positivity does not assert that the matrices R and U commute.
The remaining trace Q0*h(U) is zero only at U=I, proving the global minimum and uniqueness.
The negative quadratic completion in Z and positive logarithmic completion in P establish precisely the stated order of optimization.
At zero drift the objective decreases pointwise with regularization, and testing each fixed positive trial interchanges that decreasing limit with the infimum, including minus infinity.
Scaling the trial to zero removes its trace term and yields capacity even for singular outputs or nonattainment.
For nonzero drift the explicit scalar circular exterior example shows why setting regularization to zero before minimizing is invalid.
The full original R_F0123 Sections 3-5 agrees with this entire retained chain; its author disclosed development collaboration, which supplies no isolated independence.
The exact C_F0167 statement passes at its disclosed C_F0119/HP03 input depths, and nonzero pseudo-covariance remains outside this circular proof.

## Circular signature finding

Under strictly positive Hilbert--Schmidt covariance, C_F0125 supplies the finite ordered theorem and the required local uniform convergence/equicoercivity.
The auxiliary circular hermitization has Hadamard blocks R* and -R even for noncommuting U,V, so its determinant is abs(det(R)) squared.
Its covariance trace is -2 Tr(Q eta(Q)); the normalized C_F0119 primitive gives exactly the inner optimized circular potential.
The positive imaginary drift epsilon*eta(I) reduces by fixed congruence to ordinary regularization, and the already accepted limit interfaces permit the outer infimum.
Thus the factor 1/(2m) in the infimal convolution is correct; no C_F0124 equality is used.
For the indefinite example the three selfadjoint Kraus matrices give the stated diagonal covariance V0 and off-diagonal eigenvalues 100,-100.
The displayed positive Q0 solves eta(Q0)=Q0^(-1); its conjugated covariance has eigenvalues 1,-9/11,10/11,-10/11, so minus one is absent.
This makes the implicit circular imaginary equation invertible at zero mean and regularization.
Its positive branch is physically selected by the accepted uniqueness, and differentiating the real equation gives the Hessian C_Q0 with the stated unnormalized trace.
Adding eta^(-1) produces the exact diagonal matrix with entries 800,100,8 divided by 9900.
The given negative eigenvector ratio lies between -0.625 and -0.62; the displayed quadratic form is positive there.
This disproves a local maximum in the raw negative direction and hence the proposed raw-signature saddle mechanism.
The original text correctly refrains from disproving every possible ordered value using that local fact alone.
After balancing, the inverse-covariance-plus-identity Hessian is nonpositive on negative eigenspaces in this example; no global conclusion or zero-capacity passage is supplied by this observation.
The entire exact statement passes at its disclosed C_F0125/C_F0119 input scopes.

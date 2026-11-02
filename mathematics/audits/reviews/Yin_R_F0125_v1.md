---
author: Yin
---

# Review of Yin_C_F0125: Ordered Matrix Minimax under Positive Hilbert--Schmidt Covariance

<a id="positive-covariance-minimax-finding"></a>

## Review arrangement

The coordinating reviewer assigned the mathematical route and received mathematical progress descriptions before reconstruction.
That shared development context makes the finding self-reviewed under the current relationship rule; the old independent wording remains an historical description, not isolated-context certification.
No new mathematical review, changed conclusion or redated finding is created by this explicit relationship and locator declaration.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Retained complete finding](#positive-covariance-minimax-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Retained complete finding](#positive-covariance-minimax-finding) | [Exact statement](../../claims/Yin_C_F0125_v1.md#statement) | Entire C_F0125 continuation equations (22)-(29) for strictly Hilbert--Schmidt-positive covariance and arbitrary selfadjoint drift, plus the exact negative-covariance obstruction. The preceding coupled-diagonal draft is expressly excluded. |
| [Retained complete finding](#positive-covariance-minimax-finding) | [Exact argument](../../claims/Yin_C_F0125_v1.md#uniqueness-of-the-inner-maximum-through-a-different-semicircular-model) | Entire C_F0125 continuation equations (22)-(29) for strictly Hilbert--Schmidt-positive covariance and arbitrary selfadjoint drift, plus the exact negative-covariance obstruction. The preceding coupled-diagonal draft is expressly excluded. |

Date: 2026-09-13.
Reviewer: the coordinating agent.
Author: indefinite-variation agent.
Goal: [Yin_T_F0008](../../tasks/Yin_T_F0008_v1.md#yin_t_f0008).
Root assigned the general minimax route and received progress descriptions, then independently reconstructed the proof; the review is not a claim of independent discovery.
The candidate is independent of Spe26 and Yin_C_F0124.

## Exact Scope and Artifact

Reviewed artifact: [the Yin_C_F0125 section](../../claims/Yin_C_F0125_v1.md#yin_c_f0125), equations (22)--(29), and the [negative-direction obstruction](../../claims/Yin_C_F0125_v1.md#negative-hs-minimax-obstruction).

The preceding coupled-diagonal derivation is historical context and is not promoted by this review.
The reviewed statement assumes that all coefficients, including the arbitrary mean, are selfadjoint, and that the completely positive covariance is strictly positive as a Hilbert--Schmidt operator.
It gives a true minimum over Hermitian U followed by a maximum over positive semidefinite V.
The additional strict covariance hypothesis is indispensable for the displayed formula; the included counterexample rules out deleting it.

## Proof Obligations Checked

1. **A defined finite inner maximum.**
   At fixed U, the negative definite covariance-inverse quadratic dominates logarithmic growth.
   The logarithmic determinant is upper semicontinuous when assigned minus infinity at singular matrices.
   Testing V=I gives a finite value.
   The bound is uniform for U in compact sets and regularization in a bounded interval.
2. **No boundary optimizer at positive regularization.**
   The gradient is minus K(V) plus epsilon I plus Q, where R=(U+iV) inverse=P-iQ.
   Positive-cone first-order conditions give C=K(V)-epsilon I-Q positive semidefinite and Tr(CV)=0.
   Applying the positive map eta gives V=eta(Q)+epsilon eta(I)+eta(C)>0.
   Strict positivity of eta(I) follows from injectivity of eta and its selfadjoint Kraus representation.
   Concavity is not assumed to obtain these first-order conditions.
3. **Uniqueness before using a reduced Hessian.**
   The displayed size-2m inverse and auxiliary circular covariance satisfy a physical Dyson equation with positive imaginary part.
   The block inverse was checked by the Hadamard unitary even when U,V do not commute.
   Positive deterministic congruence reduces the imaginary drift to the scalar case of Yin_C_F0119.
   Consequently all global inner maxima coincide.
4. **Correct finite operator order.**
   The completely positive map eta S_R has a strictly positive subinvariant V, with defect epsilon eta(I).
   Hence its spectral radius is below one.
   Hilbert--Schmidt positivity of eta, separately from complete positivity, permits similarity to the selfadjoint operator eta^(1/2) S_R eta^(1/2).
   This proves K-S_R>0.
   The identity S_R-T_R=2 C_Q is positive as a Hilbert--Schmidt operator because Q>0.
   There is no substitution of positivity preservation for positivity of a quadratic form.
5. **A global outer minimum.**
   The Hessian blocks are B, minus B, and the real trace-selfadjoint mixed operator C_R.
   The reduced Hessian B+C_R B^{-1} C_R is strictly positive.
   Inner uniqueness and the implicit-function theorem justify differentiating the reduced function globally.
   Testing V=I gives a coercive quadratic lower bound in U.
   Therefore the ordered minimum exists uniquely at positive regularization.
6. **Physical value and normalization.**
   The two stationary equations combine to R^{-1}=a+i epsilon D-eta(R).
   Its negative imaginary part selects the actual expected inverse of S+i epsilon D.
   The congruence version of the Yin_C_F0119 primitive gives the displayed objective exactly, with the unnormalized trace divided by m.
   This identification is made only after proving the ordered global extremum.
7. **The zero-regularization limit.**
   The inner bounds give local uniform convergence of the reduced objectives; the same quadratic lower bound gives equicoercivity.
   Minima therefore converge and the limiting convex coercive function has a minimum.
   On the operator side, a fixed D^{-1/2} congruence reduces to the ordinary scalar spectral regularization.
   This establishes the determinant limit without claiming that S commutes with D.
8. **Centered specialization at its actual scope.**
   Evenness and convexity put the outer minimizer at zero.
   The positive-definite inverse-covariance quadratic makes the remaining logarithmic maximum strictly concave.
   Yin_C_F0120's centered finite action is strictly convex and coercive under the additional Hilbert--Schmidt positivity, and its balance yields the equality in (29).
   The capacity is positive and the balancing point is attained in this restricted class.
   No claim of full MS24 zero-capacity coverage is made.

## Exact Failure Outside the Stated Covariance Class

For eta=Ad(Z), with Z=diag(1,-1), and mean a=tX, X the first Pauli matrix, eta is completely positive but has a negative Hilbert--Schmidt eigenvalue.
At U=0 the unnormalized imaginary supremum is exactly minus t squared minus one: write Tr(VZVZ)=(V11-V22)^2+2 det V and use log x-x at most minus one.
V=I attains equality.
The normalized proposed infimum is therefore at most minus (1+t squared)/2.

The actual pencil satisfies S squared=(t squared+s squared)I, so its logarithmic determinant is one half of the semicircular integral of log(t squared+s squared), strictly greater than minus one half.
The discrepancy is strict for every t>0.
This is a counterexample to the broader displayed formula, not merely an absence of its proof.

The separate unbounded-inner example also checks out: at U=uX, diagonalize V in the X basis with eigenvalues r,c/r.
The covariance penalty stays c while the logarithmic determinant diverges as r tends to infinity.
This prevents interpreting arbitrary covariance as automatically giving a finite inner maximum.

## Dependencies and Disposition

The decisive source inputs are the already reviewed Yin_C_F0119 physical Dyson equation and primitive, bounded determinant multiplicativity, and the finite action part of Yin_C_F0120.
The ordinary implicit-function theorem, compactness, finite spectral calculus and the positive-map order-unit norm argument are used at their standard finite-dimensional scope.
The QVE literature lead in the historical preamble is not a proof dependency or a novelty determination.

**Review outcome: passed for Yin_C_F0125's exact covariance restriction and negative-direction boundary.**
No mathematical Role is assigned.
The broader Yin_T_F0008 search remains active by user instruction.
The result does not establish an arbitrary-covariance minimax, a minimax interchange, or a joint saddle property.
Further negative-direction work is recorded in a separate continuation so the inspected artifact remains stable.


<a id="registration-2026-09-13"></a>
## Inspected input boundary

The opening diagonal derivation remains a historical draft, while the Yin_C_F0125 continuation has the scoped review above.
Current assessments belong to the responsible Claim material and its selected decision.

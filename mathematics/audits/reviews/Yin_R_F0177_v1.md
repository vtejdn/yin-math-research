---
author: Yin
---

# Complete self-review of the retained Brown envelope, radial, resolvent and capacity arguments

Date: 2026-10-21T02:24.
Human record author: Yin.
Reviewer/method: the material-construction agent, with the existing proof development and surrounding F-line mathematical context available.
This is an actual complete internal self-review of the fixed retained arguments, not an isolated independent inspection.
The four original L drafts were read in full; their substantive reasoning and the actually used C_F0126/C_F0127/C_F0123 interfaces were reconstructed before the retained C arguments were selected.
The separate historical author and collaborator checks remain with the retained mathematical accounts in their responsible C/L/R homes and are not relabelled as independent whole-proof findings.
This review performs no research computation, source download, new source-page or visual inspection, formal verification, manuscript build or Task decision.

## Inputs and review boundary

The exact retained mathematical inputs are [C_F0169](../../claims/Yin_C_F0169_v1.md#argument), [C_F0170](../../claims/Yin_C_F0170_v1.md#argument), [C_F0171](../../claims/Yin_C_F0171_v1.md#argument) and [C_F0172](../../claims/Yin_C_F0172_v1.md#argument), at the four distinct review scopes bound below.
C_F0126 supplies the proved real-linear positive inner problem, the unrestricted determinant formula and its unique regularized physical optimizer.
C_F0127 supplies its critical-point, Stein and bounded-inverse equivalences.
C_F0123 supplies the accepted compactly supported Brown logarithmic potential, normalized Laplacian, weak regularization and fixed-positive-regularizer derivative interface.
Those responsible materials retain their own reviews and accepted external source limits; this is not a new full audit of their proofs or source foundations.
C_F0167 supplies only the existing circular physical Schur positivity used for the finite-regularization normalization check.
AK20-U001 is a related-work comparison under stronger flatness, not a proof input.
The unchanged mathematical bodies and explicit scope/failed-inference boundaries were inspected together; the locating wrappers do not create broader conclusions.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Envelope and positive Hessian](#envelope-hessian-finding) | self-reviewed |
| [Radial mass and spectral disk](#radial-mass-finding) | self-reviewed |
| [Stable resolvent and Brown masses](#resolvent-mass-finding) | self-reviewed |
| [Capacity lower bound and atomlessness](#capacity-atomlessness-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete finding](#envelope-hessian-finding) | [C_F0169 statement](../../claims/Yin_C_F0169_v1.md#statement) | Whole envelope and Hessian argument: scalar and arbitrary positive matrix regularization, actual unique physical optimizer, first derivatives, strict Hessian and completely positive inverse response, quadratic-form bounds, bounded-inverse zero-regularizer extension, Schur-complement density, sensitivity and scalar normalization. No global convexity or uniform boundary stability. |
| [Complete finding](#envelope-hessian-finding) | [C_F0169 complete argument](../../claims/Yin_C_F0169_v1.md#argument) | Whole envelope and Hessian argument: scalar and arbitrary positive matrix regularization, actual unique physical optimizer, first derivatives, strict Hessian and completely positive inverse response, quadratic-form bounds, bounded-inverse zero-regularizer extension, Schur-complement density, sensitivity and scalar normalization. No global convexity or uniform boundary stability. |
| [Complete finding](#radial-mass-finding) | [C_F0170 statement](../../claims/Yin_C_F0170_v1.md#statement) | Whole centered rho=0 argument: radial concave envelope, logarithmic-potential representation, all one-sided slopes, absence of positive-radius atoms, local absolute continuity and density bounds, positive-capacity whole-measure absolute continuity, regularized-minimizer reconstruction and exact operator spectral disk including degenerate maps. No Brown-support/full-disk equality or convergence rate. |
| [Complete finding](#radial-mass-finding) | [C_F0170 complete argument](../../claims/Yin_C_F0170_v1.md#argument) | Whole centered rho=0 argument: radial concave envelope, logarithmic-potential representation, all one-sided slopes, absence of positive-radius atoms, local absolute continuity and density bounds, positive-capacity whole-measure absolute continuity, regularized-minimizer reconstruction and exact operator spectral disk including degenerate maps. No Brown-support/full-disk equality or convergence rate. |
| [Complete finding](#resolvent-mass-finding) | [C_F0171 statement](../../claims/Yin_C_F0171_v1.md#statement) | Whole affine branch and mass argument: equivalent strict CP-stable finite resolvent certificate and unique physical branch; rho=0 spectral region/exterior determinant and contour eigenvalue mass; circle means and atoms; singular-value kernel limits and nilpotent distinction; all possible Brown atoms confined to deterministic mean eigenvalues. Each extra hypothesis and negative boundary retained. |
| [Complete finding](#resolvent-mass-finding) | [C_F0171 complete argument](../../claims/Yin_C_F0171_v1.md#argument) | Whole affine branch and mass argument: equivalent strict CP-stable finite resolvent certificate and unique physical branch; rho=0 spectral region/exterior determinant and contour eigenvalue mass; circle means and atoms; singular-value kernel limits and nilpotent distinction; all possible Brown atoms confined to deterministic mean eigenvalues. Each extra hypothesis and negative boundary retained. |
| [Complete finding](#capacity-atomlessness-finding) | [C_F0172 statement](../../claims/Yin_C_F0172_v1.md#statement) | Whole deterministic-mean lower-bound argument: nonnegative real-linear mean energy, exact capacity constant, real-scaling monotonicity/concavity, arbitrary-mean positive-capacity atomlessness, coefficient-controlled logarithmic disk-mass bound and scalar semicircle limitation. No area-density or spectral-support equality. |
| [Complete finding](#capacity-atomlessness-finding) | [C_F0172 complete argument](../../claims/Yin_C_F0172_v1.md#argument) | Whole deterministic-mean lower-bound argument: nonnegative real-linear mean energy, exact capacity constant, real-scaling monotonicity/concavity, arbitrary-mean positive-capacity atomlessness, coefficient-controlled logarithmic disk-mass bound and scalar semicircle limitation. No area-density or spectral-support equality. |

<a id="envelope-hessian-finding"></a>
## Envelope and positive Hessian finding

The complete C_F0169 argument passes at its stated fixed-positive-regularizer and bounded-inverse scopes.

For an arbitrary positive matrix regularizer D, the transformed pencil S D^(-1/2), trial R'=D^(1/2) R D^(1/2) and inner solution Z'=Z D^(1/2) preserve the mean energy.
Both transformed inner terms equal the original term multiplied on the right by D^(-1/2), and both determinant normalizations acquire the same minus log det D.
This establishes the whole matrix-regularizer formula, rather than inferring it from scalar regularizers.

The differentiable actual optimizer R_D=E((S*S+D)^(-1)) obeys gradient V(R_D)+D=0.
Its directional derivative is minus A_D(B), where A_D(B)=E(Q_D^(-1) B Q_D^(-1)).
Differentiating stationarity gives H_D A_D=I on the finite real Hermitian space.
The traced quadratic form of A_D is the faithful trace of the square of Q_D^(-1/2) B Q_D^(-1/2), strictly positive for nonzero Hermitian B.
Thus A_D is invertible and H_D=A_D^(-1)>0, with the stated complete positivity of the inverse response and both squared spectral bounds.
At boundedly invertible S, norm convergence of Q_D^(-1) gives the claimed unregularized inverse-Hessian identity; no uniform statement on the spectrum is inserted.

The real mean derivatives have negative real and imaginary trace signs.
Combining them with partial_z=(partial_x-i partial_y)/2 gives minus conjugate Tr Z divided by 2m.
Implicit differentiation uses the proved nonsingular Hessian; the Schur complement and the factor 1/(4 pi m) therefore have the correct Brown normalization.
The direct operator trace of Q^(-1)P^(-1) is positive by square-root cyclicity even though its factors need not commute.
The upper bound by Tr R/(pi m), the positive-regularizer t derivative, and the deterministic point-mass density have the stated signs and factors.
Unique attainment alone is not used as a proof of Hessian invertibility.
Global objective convexity, a uniform vanishing-regularizer condition number and pointwise limiting densities remain unproved and excluded.

<a id="radial-mass-finding"></a>
## Radial mass and spectral disk finding

The complete C_F0170 argument passes for centered rho=0 pencils, including degenerate covariance.

With rho zero the inner solution is -z H_R^(-1)R, so the objective is affine with positive slope in s=absolute value of z squared.
Its infimum is concave and nondecreasing.
The accepted Brown potential and angular logarithmic identity give the finite positive-radius representation by log max(s,t).
The left and right derivatives of this representation bracket any circle atom in the opposite order from concavity; hence every such atom vanishes.
Consequently F=2s f' is continuous and F(s)/s is nonincreasing.
The displayed difference estimate makes F locally Lipschitz away from zero, excluding radial singular continuous mass as well as circle atoms and giving 0 at most F' at most F/s.
The polar area factor is 1/pi, not an additional factor two.
Positive capacity makes the potential at zero finite, which excludes the only remaining possible atom and proves the stated whole-measure absolute continuity.
The general nonradial atomlessness statement is not substituted for this separate radial argument.

At fixed regularizer, compact positive-cone sublevels and uniqueness justify the envelope derivative.
For positive s, secant bounds for concave functions prove convergence of derivatives to the differentiable limiting f.
The rescaling Q=epsilon squared times R preserves exactly the trace combination in the mass formula, without requiring the matrices themselves to converge.
The inherited physical Schur inequality gives the strict finite-regularization mass bound.

For the spectrum, the C_F0127 stationary equation forces Y=-I/conjugate(z) and (s Id-eta)R=I.
The positive Neumann series supplies R when s>r(eta).
Conversely a positive R solution makes the similar CP map strictly subunital, with spectral radius r(eta)/s<1.
The critical equation also excludes z=0 from the resolvent and handles r(eta)=0.
This proves the full operator disk while making no claim that the Brown support fills it.
The scalar circular law, empty noise, diagonal circular-plus-zero example and the abstract nonmonotone density control are consistent with these exact boundaries.

<a id="resolvent-mass-finding"></a>
## Stable resolvent and Brown masses finding

The complete C_F0171 argument passes at each explicitly separated hypothesis.

A resolvent point supplies the positive Stein defect and therefore a strict CP stability certificate.
Conversely the positive series for b_z solves b_z=g(I+eta(b_z))g*.
With Y=g*, both the inner equation and the two zero-gradient identities of C_F0127 follow in the displayed order.
The existing critical-point theorem then identifies the bounded inverse and unique physical branch.
An arbitrary algebraic solution without the strict stability condition is not accepted.

When rho=0, g=a_z^(-1); a singular a_z cannot admit that certificate.
This gives exactly the stated spectral-radius region.
At the attained value H=a_z b_z a_z* and the mean energy is m, so the exterior potential is log absolute det a_z divided by m in every resolvent component.
The contour derivative is minus one half the normalized trace of g; Cauchy integration gives the stated negative contour sign.
Only a contour with positive distance from the operator spectrum supplies the no-boundary-mass step.
The finite eigenvalue count additionally uses rho=0 and does not quantize arbitrary atom weights.

For circle means, the bounded positive logarithmic part and a uniformly integrable negative angular part justify integration order even at individual infinite-potential points.
The left/right derivatives of max(t,s) give open/closed disk masses with the displayed directions.
Bounded convergence gives both center-atom limits.
The infimum remains angle-dependent and is never interchanged with a common-matrix infimum.

The regularized trace and logarithmic ratios use the compact singular-value distribution and give only the kernel projection mass.
The deterministic size-two nilpotent has kernel mass one half and Brown atom one, so the two notions remain separated.

For atom localization, the positive real-linear energy makes every centered ray potential nondecreasing in its nonnegative radius.
The bound by the one-dimensional integral of minus log absolute t is at most two on every nontrivial segment, uniformly in the source point.
Tonelli and compact support therefore preclude a centered ray interval of potential minus infinity.
For an invertible deterministic shift A, the inequality (AB)*(AB) at least c squared B*B and operator monotonicity of log transfer finiteness from the centered pencil at the nonzero shift -1.
A positive Brown atom forces potential minus infinity, proving that only eigenvalues of the deterministic mean can carry atoms.
The converse and unconditional atom-weight quantization remain unproved.

<a id="capacity-atomlessness-finding"></a>
## Capacity lower bound and atomlessness finding

The complete C_F0172 argument passes for arbitrary complex deterministic means.

The real-linear inner operator is positive definite, so its inverse quadratic mean energy is nonnegative.
Taking infima gives the determinant lower bound with normalized exponent 1/(2m) and constant e^(-1/2), including the extended-real zero-capacity case.
Real scaling of a fixed mean makes that energy t squared times its original value; its infimum is therefore nondecreasing and concave in that squared real scale.
No complex-linearity or general rotational invariance is used.

At positive capacity the same lower bound applies to every shifted mean and is finite.
Compact Brown support bounds the positive logarithmic part, so a positive atom would force the potential to minus infinity at its location, a contradiction.
The scalar semicircle verifies both the capacity constant and the failure of any conclusion of planar absolute continuity.

For a disk of radius r below L_z=M+absolute value of z, the log potential is at most p log r+(1-p)log L_z.
Combining with the uniform lower bound gives the stated inequality with the correct denominator and direction.
The numerator is nonnegative by the same upper and lower potential bounds.
The coefficient norm bound uses semicircular norm two and remains positive at positive capacity.
No power-law estimate, strict mean monotonicity, unique minimizing mean or support/spectrum equality is obtained.

## Disposition and remaining review boundary

These four complete arguments have an actual self-reviewed internal finding, sufficient for the stated mathematical adoption without claiming independent coverage.
They were not repairs of an independently identified proof gap.
The original collaborator checks are narrower evidence, and no finding here manufactures a historical independent review.
A separately isolated inspection of the complete arguments can still provide independent coverage.
All new C decisions own their exact adoptions; this R changes no Task, role, manuscript or objective.

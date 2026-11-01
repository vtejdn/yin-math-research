---
author: Yin
---
# Independent scalar review of soft-energy polarization and the factor-two quadratic estimate

Review performed and recorded: 2026-10-16T03:37.
Human record author: Yin.
This is a separately assigned AI mathematical review, not a personal human inspection.

## Arrangement and exact scope

This review covers Part A of the fixed [C_F0162 v1 statement](../../claims/Yin_C_F0162_v1.md#statement) and Sections 1-5 of its [argument](../../claims/Yin_C_F0162_v1.md#argument).
The reviewer did not develop or edit this Claim.
The assignment provided the fixed Claim, identified the scalar calculations to check, and stated that author-development dialogue had not been supplied.
No exploration notes, finite-point diagnostics, author-development dialogue or previous review conclusion for this Claim were consulted.
The reviewer had previously reviewed the distinct three-circle Claim C_F0161; its conclusions and review are not proof inputs here.
The provenance paragraph inside C_F0162 was read only as part of the fixed artifact.

The reviewer first recalculated the three anchor contributions to the soft kernel, both cubic-energy coefficients and the real gap, then checked the actual adjoint and weak/strong passage against the declared C_F0055 interfaces.
C_F0076 Part 1 and its first argument section were also read solely to check Part A's identification with every one-generator normal actual-A system.
Its accepted diffuseness input was reused at the existing scope, without reopening its external source proofs or importing its iterated-derivative conclusions.
The selected decisions of these existing inputs were inspected after the local scalar calculations.

The inspected artifact is the uncommitted working-copy physical v1 with initial decision dated 2026-10-16T03:30.
Repository HEAD was 1b0009e237e11d309456540e58d828f2e2156e25, which does not identify that new Claim's bytes.
Its starting assessment was proof draft with unreviewed review status.
Part B and argument Section 6, including free-product lifting, power iteration, mixed-word estimates and canonical full-domain restoration, are outside this review's mathematical conclusion.
Reading those passages to delimit the scope supplies no review of their proof.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Scalar conclusion](#scalar-conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Scalar conclusion](#scalar-conclusion) | [C_F0162 statement](../../claims/Yin_C_F0162_v1.md#statement) | Part A only: actual scalar one-sided adjoints, real fixed-vector inequality S2, complex factor-two inequality S3 and the identification with every one-generator normal actual-A system. No Part B coverage. |
| [Scalar conclusion](#scalar-conclusion) | [C_F0162 argument](../../claims/Yin_C_F0162_v1.md#argument) | Sections 1-5 only: actual operators, all soft-kernel collision terms, cubic-energy polarization, exact real gap, weak vacua, strong original-core difference quotients, cancellation and complex decomposition. No Section 6 coverage. |
| [Scalar conclusion](#scalar-conclusion) | [C_F0055 statement](../../claims/Yin_C_F0055_v1.md#statement) | Compact nonatomic scalar law and actual vacuum hypotheses match Part A; only the Sections 3-7 interfaces specified below are used. |
| [Scalar conclusion](#scalar-conclusion) | [C_F0055 Section 3](../../claims/Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) | Actual vacuum identity on smooth scalar tests, with its accepted C1 polynomial approximation input, as used by the soft-vacuum bound. |
| [Scalar conclusion](#scalar-conclusion) | [C_F0055 Section 4](../../claims/Yin_C_F0055_v1.md#4-soft-kernels-and-exact-positive-three-point-formulas) | Positive soft three-point identity, independently recalculated here with the conjugate kernel orientation and with collisions retained. |
| [Scalar conclusion](#scalar-conclusion) | [C_F0055 Section 5](../../claims/Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | Accepted uniform soft Cauchy bound under the actual vacuum; used only as uniform L2 control for the weak-vacuum limit. |
| [Scalar conclusion](#scalar-conclusion) | [C_F0055 Section 6](../../claims/Yin_C_F0055_v1.md#6-positive-weights-give-the-scalar-core-bound) | Original polynomial soft difference quotients converge strongly by bounded divided differences and dominated convergence; its contraction estimate is not used to infer S2 or S3. |
| [Scalar conclusion](#scalar-conclusion) | [C_F0055 Section 7](../../claims/Yin_C_F0055_v1.md#7-actual-adjoints-and-original-graph-restoration) | Actual original-core adjoint formula only; no Hilbert-space boundedness, enlarged domain or stronger quadratic estimate is imported. |
| [Scalar conclusion](#scalar-conclusion) | [C_F0076 statement](../../claims/Yin_C_F0076_v1.md#statement) | Part 1 only: accepted diffuseness and phase determination for normal actual-A derivations, specialized to one scalar generator. |
| [Scalar conclusion](#scalar-conclusion) | [C_F0076 first argument section](../../claims/Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Hypothesis match for accepted diffuseness and the injective coarse difference operator; direct verification that the scalar phase and Leibniz rule uniquely give the displayed divided difference. |

## Actual scalar hypotheses and adjoints

The quotient on the represented star algebra is independent of the polynomial representative and has bounded values on the compact product support off its null diagonal.
Its outer Leibniz rule and delta X=1 tensor 1 hold directly.
The actual vacuum hypothesis supplies the identity <xi,p>=integral E0p.
Expanding the divided difference of conjugate(a)p and swapping variables gives the vector a xi-JE0Ja representing the adjoint pairing at a.
This vector belongs to H because a is bounded, xi belongs to H and E0 maps polynomials into H.
Thus both a tensor 1 and 1 tensor a are in the actual delta* domain, with common value T(a)=a xi-L(a)=E0*a.
The equality of the two one-sided maps uses symmetry of the divided difference, without assuming that delta is real.

For the final scope assertion in Part A, C_F0076 Part 1 is an accepted input whose full normal-A hypothesis holds for the supplied one-generator system.
Its diffuseness conclusion makes the spectral collision diagonal null.
Applying the derivation to XX*=X*X gives (z-w)delta(X*)=bar z-bar w.
Multiplication by z-w is injective on this product L2 space, so the phase is unique.
The Leibniz rule then fixes the derivation on every starred polynomial.
No unspecified extension or formal vacuum substitutes for the actual operators.

## Direct calculation of positivity and collisions

Write x=|z-v| squared, y=|w-v| squared and r=|z-w| squared.
The three real anchor contributions to S_t are
\[
 \frac{r+x-y}{2(r+t)(x+t)},\qquad
 \frac{r+y-x}{2(r+t)(y+t)},\qquad
 \frac{x+y-r}{2(x+t)(y+t)}.
\]
These formulas follow from the real inner-product polarization of each pair of displacement vectors and remain valid when displacements vanish.
Their common numerator is
\[
 (r+x-y)(y+t)+(r+y-x)(x+t)+(x+y-r)(r+t)
 =H_\triangle+t(x+y+r).
\]
This verifies equation (6) directly, including its factor 1/2.
The nonnegative area expression H_triangle and t>0 prove S_t>=0.
If z=w differs from v, then r=0 and x=y, and the formula reduces to \(x/(x+t)^2\), which is exactly |k_t(z,v)| squared.
If all points coincide, it gives zero.
No repeated-point energy term disappears.

The kernel is bounded by 1/(2 sqrt(t)) in magnitude and is antisymmetric.
For any finite positive measure, all cubic integrals are absolutely integrable.
The three anchor integrals are equal by permutation of variables, and their common integral is the squared Cauchy-field norm.
Consequently the energy is one third of the integral of S_t, as in equation (7).
Conjugation relative to C_F0055 does not change this real kernel.

## The two polarization coefficients and exact real gap

For bounded real f, the perturbed measure (1+s f)mu is positive on an interval about s=0.
Both sides of the cubic identity are polynomials in s, so equality on that interval determines their coefficients.
On the field side the exact integrand is
\[
 (1+s f)\bigl(|B_t|^2+2s\operatorname{Re}(C_tf\,\overline{B_t})
                    +s^2|C_tf|^2\bigr).
\]
Its quadratic coefficient is ||C_tf||2 squared plus twice the real integral of f C_tf conjugate(B_t).
On the symmetric-kernel side, the three pair terms cancel the factor 1/3 and give integral S_t f(z)f(w).
This proves equation (8) with the stated coefficient two.

For the separate perturbation by f squared, the linear coefficient is the integral of f squared |B_t| squared plus twice the real integral of C_t(f squared) conjugate(B_t).
The three single-variable terms on the kernel side again cancel 1/3, giving integral S_t f(z) squared.
This is exactly equation (9); it does not use a coefficient from a different perturbation without making that substitution.

Using u_t=2B_t, direct expansion gives
\[
 \operatorname{Re}\langle T_t(f^2),u_t\rangle-\|T_tf\|_2^2
 =\int f^2|B_t|^2+2\operatorname{Re}\int C_t(f^2)\overline{B_t}
       -\|C_tf\|_2^2-2\operatorname{Re}\int fC_tf\overline{B_t}.
\]
Subtracting the two checked coefficients identifies this expression with integral S_t times (f(z) squared-f(z)f(w)).
Symmetry in z,w makes it one half the integral of S_t times (f(z)-f(w)) squared.
This establishes the exact nonnegative gap (10).
Using B_t in place of u_t would not give this identity; the factor two is correctly retained throughout.

## Weak vacuum, strong core convergence and cancellation

The soft original-core E_t is the bounded polynomial divided difference multiplied by a scalar between zero and one.
That scalar tends to one off the null diagonal.
Dominated convergence in L2(mu tensor mu), followed by the norm-one tensor contraction, proves E_tp->E0p strongly for each polynomial p.
The chosen kernel orientation gives L_t=JE_tJ, so L_tp->Lp strongly on the same core.

Let the C_F0055 soft Cauchy field use its original conjugate kernel.
The present B_t is its complex conjugate and therefore has the same L2 norm, at most ||xi||2.
The accepted source hypothesis is precisely the actual vacuum identity supplied here, with compact support and a diffuse probability law.
This is the sole uniform soft-field estimate needed for the new limit argument.

Since the kernel is antisymmetric,
\[
 \int E_tp\,d\mu
 =2\int p(z)\overline{B_t(z)}\,d\mu(z)
 =\langle u_t,p\rangle.
\]
The strong E_t convergence and the actual vacuum identify the limit as <xi,p>.
The uniform bound ||u_t||2<=2||xi||2 and density of P extend this convergence to every Hilbert test vector.
Thus u_t converges weakly to the actual xi.
Neither u_t nor T_t is asserted to equal an original adjoint value before that limit, and no strong convergence of u_t is invoked.

For real f, expansion of the real-gap inequality cancels exactly ||f u_t||2 squared on the two sides and leaves
\[
 \|L_tf\|_2^2
 \le\operatorname{Re}\langle2fL_tf-L_t(f^2),u_t\rangle.
\]
The first vector on the right converges strongly because f is bounded and f,f squared belong to P.
For q_t=2fL_tf-L_t(f squared) and its strong limit q, the error pairing <q_t-q,u_t> tends to zero by the uniform bound on u_t, while <q,u_t> converges by weak convergence.
This proves the legitimate limit (18).
Reintroducing ||f xi||2 squared and using T(f)=f xi-Lf gives exactly S2.
No pairing of two merely weakly convergent sequences is passed to the limit.

## Complex functions and dependence boundary

For a=f+i h with real core f,h, complex linearity gives Ta=Tf+i Th.
The Hilbert estimate ||Tf+i Th||2 squared <=2(||Tf||2 squared+||Th||2 squared) is valid without any reality of these images.
Commutativity supplies |a| squared=f squared+h squared, so summing the two S2 inequalities yields the first inequality in S3 with factor two.
The second is Cauchy-Schwarz.
The summed real pairing is nonnegative; the proof does not assert that the full complex pairing is real.
This commutative decomposition is used only in the scalar argument and supplies no mixed noncommutative square identity.

The new argument uses C_F0055's uniform vacuum-field bound, actual core-adjoint identity, and elementary core convergence.
Its previously proved infinity-to-L2 contraction constant, full-domain result and free-normal lifting are not used to establish S2 or S3.
Thus a stronger quadratic estimate has not been smuggled in through the older contraction estimate.
The polynomial approximation source underlying the accepted C_F0055 smooth-test interface remains accepted at its recorded statement-and-applicability depth; no new external proof audit is claimed.
All newly checked identities and limit arguments are displayed above.
No numerical diagnostics, formal verification, sharpness result, principal-value theorem or novelty search is claimed.

## Scalar conclusion

Part A of C_F0162 v1 and the complete scalar argument in Sections 1-5 pass this independent review.
No coefficient, sign, collision, actual-domain, limit or direct-input applicability defect was found within this scope.
This finding supports the exact real inequality S2 and complex factor-two inequality S3 under the stated scalar actual-vacuum hypothesis, including the stated one-generator normal-A identification.
It does not support Part B by itself and cannot serve as a whole-Claim or Task-completion review.
The free-product application and the resulting canonical-domain claims require their separately assigned review.

---
author: Yin
---
# Factorization continuity and the projective criterion: review with a disclosed application repair

Date: 2026-10-14T20:28.
Human record author: Yin.
This review covers the complete [C_F0151 v2](../../claims/Yin_C_F0151_v2.md#statement), after first checking v1 and identifying the product-order error below.
The conditional theorem, smooth calculi, continuity inputs and projective criterion were independently checked.
The reviewer supplied the bounded-intertwining repair of the concrete hS application; that repaired application is explicitly self-reviewed here and requires complementary independent coverage.

The assignment supplied the hS factorization summary and verification targets.
Earlier T_F0011 work and the reviewer's independent review of C_F0150 are related background, not development of this conditional theorem or projective criterion.
No D_F0005 development text or proof-generation dialogue was consulted.
The fixed versions and exact dependencies were read.
No earlier C_F0151 review findings were supplied or relied on.
The repair was communicated after checking v1; the unchanged portions were compared against v2.

## Review relationships

| Review | Relationship |
| --- | --- |
| [V1 product-order finding](#v1-product-order-finding) | independently reviewed |
| [Independent conclusion](#independent-conclusion) | independently reviewed |
| [Repaired application](#repaired-application) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [V1 product-order finding](#v1-product-order-finding) | [C_F0151 v1 argument](../../claims/Yin_C_F0151_v1.md#argument) | Concrete diffuseness paragraph: after v=sqrt(h)w the written inference changes Sh into hS incorrectly. |
| [Independent conclusion](#independent-conclusion) | [C_F0151 v2 statement](../../claims/Yin_C_F0151_v2.md#statement) | Entire conditional factorization theorem and general bounded-dual projective criterion, with exact limits. The repaired verification of the concrete hS hypotheses is covered separately. |
| [Independent conclusion](#independent-conclusion) | [C_F0151 v2 argument](../../claims/Yin_C_F0151_v2.md#argument) | AC1--AC4, C1/C3 norm continuity, multiplicativity and support, super-decomposability, divisible-subspace/eigenvalue checks, Laursen application and both AC5--AC6 criterion directions; excludes only the repaired concrete diffuseness verification. |
| [Independent conclusion](#independent-conclusion) | [Lau88-U001](../literature/Lau88/Yin_U001.md#lau88-u001) | Exact Proposition 3.7 and Theorem 4.1 hypotheses and conclusions, at the unit's published-input inspection limits. |
| [Independent conclusion](#independent-conclusion) | [C_F0069 argument](../../claims/Yin_C_F0069_v1.md#argument) | Triangular-intertwiner method and complete elementary absence of normal divisible subspaces; the extra nonnormal calculus is checked here. |
| [Repaired application](#repaired-application) | [C_F0151 v2 statement](../../claims/Yin_C_F0151_v2.md#statement) | Concrete hS application and its exact bare-existence/projective-functional equivalence, using the independently checked general theorem. |
| [Repaired application](#repaired-application) | [C_F0151 v2 argument](../../claims/Yin_C_F0151_v2.md#argument) | Corrected X sqrt(h)=sqrt(h)Y, factor injectivities, diffuse Y and reference-to-two-variable restriction. |
| [Repaired application](#repaired-application) | [C_F0147 reference input](../../claims/Yin_C_F0147_v1.md#3-polynomial-retraction-proves-maximal-delta) | Actual semicircular reference conjugates, maximal reference Delta and full-polynomial injectivity applied to hS-lambda; no target-A or bare-dual conclusion imported. |

## V1 product-order finding

Writing v=sqrt(h)w in Yv=lambda v, with Y=sqrt(h)S sqrt(h), and cancelling the injective sqrt(h) gives (Sh-lambda)w=0.
It does not give the asserted (hS-lambda)w=0.
Thus the original concrete diffuseness inference was invalid as written.
This is an argument error, not evidence against the theorem.
V1 remains preserved.
The reviewer supplied X sqrt(h)=sqrt(h)Y as a direct repair, now present in v2; all other mathematics is unchanged.

## Independent checks of the conditional theorem

### The calculi are continuous, multiplicative and local

For polynomials, AY^kB=X^(k+1), so AC1 equals f(X).
Approximating f' uniformly and integrating gives simultaneous C1 approximation.
The first divided-difference bound then gives norm convergence of AC1 and membership in norm-closed N.
Multiplicativity follows by approximating both factors.
Vanishing near K makes all values and repeated-node derivatives in the divided differences vanish, proving locality.

The identity

\[
 (z-X)^{-1}=z^{-1}I+z^{-1}A(z-Y)^{-1}B
\]

holds on both sides outside K.
Expanding its product around P yields the four AC2 terms: f'(0)P, the two second divided differences, and the third divided difference at (s,0,0,t).
For f(x)=x^2 this is XP+PX; for f(x)=x^3 it is X^2P+XPX+PX^2.
The same Laurent coefficient calculation gives every monomial.
BPA is Hilbert--Schmidt because P has rank one.
The two-sided selfadjoint spectral calculus is contractive on the Hilbert--Schmidt space for bounded scalar kernels.
The second and third divided differences are bounded by the respective derivative suprema divided by 2 and 6.
Thus AC2 is C3-continuous; no operator-norm Schur-multiplier assertion is needed.

Approximating the third derivative and integrating three times gives polynomial C3 approximation, which passes the polynomial Leibniz identity to AC3.
Polynomial Gamma preserves H_N; its Hilbert--Schmidt, hence operator-norm, limit also does.
Restriction N to H_N is bounded because ||a||2<=||a||.
These facts justify every block of AC4 and its multiplicativity and locality.

### The spectral and algebraic premises of Laursen are present

A complex open cover of compact real K admits real-interval smooth cutoffs with compact supports in the respective open sets and sum one near K.
Their calculus operators commute with the triangular operator.
For lambda outside one cutoff support, choose a smooth function equal to (x-lambda)^(-1) near that support.
Multiplicativity gives a two-sided inverse on the cutoff range; boundedness passes the identity to its closure.
Each restricted spectrum therefore lies in the required open set.
The two closed ranges sum to the whole space, and the cutoffs commute with the operator.
This is super-decomposability in Lau88's exact definition.
The identical diagonal argument proves decomposability of L_X on the operator-norm Banach space N.

The elementary normal argument in C_F0069 was reread: a divisible vector lies in every squared resolvent range, giving a finite fourth-order spectral potential at every point; a planar disk covering contradicts a nonzero spectral measure.
The bounded injective map B sends an X-divisible subspace to a Y-divisible one because BX=YB.
This applies to H_N and to N embedded in H_N.
Projection to the second and then first component excludes every triangular-divisible subspace.
Diffuseness of selfadjoint Y and injectivity of B likewise exclude X eigenvectors, and hence triangular eigenvectors.

Lau88 Proposition 3.7 now makes the triangular algebraic spectral subspaces closed.
The source L_X is decomposable, and the target triangular operator has no eigenvalues, hence no critical eigenvalues.
Theorem 4.1 applies with n=1.
The identity T J=J L_X for J(a)=(E(a),a) is exactly E(Xa)-XE(a)=tau(a)1, so the commutator sign is correct.
The conclusion is operator-norm-to-L2 boundedness, not closability or a vacuum adjoint.

## Independent checks of the projective criterion

The conjugate Hilbert factor has the correct complex structure.
A bounded E gives the bilinear form (a,bar(eta)) mapped to <eta,Ea>, with projective functional norm ||E||.
On q(a,eta) it equals

\[
 \langle\eta,E(Xa)-XE(a)\rangle
 =\tau(a)\langle\eta,1\rangle,
\]

because <X*eta,Ea>=<eta,XEa> under the linear-in-second convention.
This proves well-definedness despite possible algebraic relations among the q generators, as well as boundedness for the inherited projective norm.

Conversely, complex Hahn--Banach extends bounded L from that span.
For each a the resulting functional is conjugate-linear and bounded in eta, so Hilbert Riesz gives Ea.
Bilinearity makes E linear, and the projective estimate gives ||Ea||2<=||L||||a||.
Testing q proves the full commutator on all bounded a.
For tuples, each desired dual uses the combined span of all q_j and the delta_ij prescription.
No automatic continuity for arbitrary tuples follows from this criterion.
It characterizes bare witnesses only when the separate continuity implication applies.

## Repaired application

This finding is self-reviewed because the reviewer supplied the correction.
The factors A=sqrt(h) and B=sqrt(h)S are bounded, AB=hS and BA=sqrt(h)S sqrt(h)=Y=Y*.
Both sqrt(h) and S are injective by their diffuse semicircular laws, so B is injective.

C_F0147 Section 3 verifies actual reference conjugates, obtains maximal reference Delta and uses the checked full-polynomial interface.
The scalar hS-lambda is nonzero and full over the three-variable free polynomial algebra, so its evaluation is injective for every lambda.
Its left action preserves the closed two-variable L2 subspace, where it remains injective.
No target/reference equality is assumed.

For every Y eigenvector in that subspace,

\[
 (X-\lambda)\sqrt h\,v=\sqrt h\,(Y-\lambda)v=0.
\]

Injectivity of X-lambda implies sqrt(h)v=0, and injectivity of sqrt(h) gives v=0.
This includes lambda=0 and uses no inverse factor.
The selfadjoint Y has diffuse law.
All hypotheses of the independently checked conditional theorem therefore hold.
The application is mathematically complete, but independent adoption requires the complementary review of this repaired step.

## Inspection limits

The three exact direct inputs and the named MSY interface at the concrete-use boundary were read.
Lau88 is accepted at U001's published-statement scope; predecessor proofs were not newly audited.
No computation or formal verification is claimed.
C_F0150's actual A witness and the open target Hilbert-graph comparison are context, not proof premises.
The result neither constructs nor excludes a bare dual for hS, and gives no canonical adjoint/full-domain conclusion.

## Independent conclusion

The conditional factorization automatic-continuity theorem, its entire smooth-calculus/Laursen proof, and both directions of the general bounded-dual projective criterion in C_F0151 v2 pass the independent review.
No gap remains in those scopes.
This finding alone does not independently certify the repaired concrete application.

Together with the self-reviewed application above, the complete v2 mathematics is supported.
Independent whole-result adoption additionally needs the requested independent finding for that application.
The actual review relationship is mixed and must not be summarized as an uninvolved whole-proof review by this reviewer.

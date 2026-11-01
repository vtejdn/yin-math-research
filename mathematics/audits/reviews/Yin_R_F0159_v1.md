---
author: Yin
---
# Independent application-only review of the repaired hidden-factor continuity example

Review performed and recorded: 2026-10-14T20:29.
Human record author: Yin.
This is a separately organized AI review of the explicitly limited application below.

## Exact scope and arrangement

The assigned input is [C_F0151 v2](../../claims/Yin_C_F0151_v2.md), initial decision dated 2026-10-14T20:24.
This review covers only the paragraph beginning 'For the hidden-factor model', the statement's resulting hS automatic-continuity consequence, and its exact C_F0147 reference interface.
The conditional automatic-continuity theorem, smooth triangular calculus, Lau88 hypotheses and projective functional criterion are outside this review.
Their independent coverage must come from the separately assigned review; this record cannot by itself support whole-Claim acceptance.

The earlier normal-branch reviewer identified the v1 product-order error and supplied the repaired bounded intertwining identity.
Root assigned this complementary check because that contribution is development of the repaired step.
This reviewer was told the repair context and the proposed identity before reading v2, so this is not a blind review.
The reviewer did not propose, develop or edit the application and independently checks its algebra, regularity input and domains below.

This agent previously developed the separate target resolvent obstruction C_F0148 and the Riesz criterion retained in D_F0005.
Those do not supply this repaired application.
Although C_F0151 mentions the Riesz criterion as a comparison, that comparison and the new projective criterion are outside the present independent scope.
Root's continuing D14 development was not consulted as proof evidence here.
The complete fixed C_F0151 text was visible for context, without a claim of checking its other proof sections.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Application conclusion](#application-conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Application conclusion](#application-conclusion) | [C_F0151 v2 statement](../../claims/Yin_C_F0151_v2.md#statement) | Only the concrete h=2+s0, X=hS consequence: the stated bounded selfadjoint factorization hypotheses hold, so the separately reviewed conditional theorem makes every hypothetical bare dual norm bounded. No existence or nonexistence conclusion is covered. |
| [Application conclusion](#application-conclusion) | [C_F0151 v2 argument](../../claims/Yin_C_F0151_v2.md#argument) | Only the paragraph beginning 'For the hidden-factor model' and its immediate consequence: correct factor order, bounded injective B, all-lambda injectivity, bounded intertwining and diffuse Y; no audit of the smooth calculus or functional criterion. |
| [Application conclusion](#application-conclusion) | [C_F0147 Section 3](../../claims/Yin_C_F0147_v1.md#3-polynomial-retraction-proves-maximal-delta) | Accepted full-polynomial injectivity in the three-semicircular reference, applied to the nonzero scalar polynomial hS1-lambda and restricted to the two-variable reference Hilbert subspace. No target-A or all-bare-F conclusion of C_F0147 is imported. |

## Factor order and injectivity

For the standard semicircular s0, h=2+s0 is bounded positive with spectrum [0,4] and no atom at zero.
Hence sqrt(h) is bounded and injective.
S is also bounded and injective because its standard semicircular law has no atom at zero.
With

\[
 A=\sqrt h,\qquad B=\sqrt h\,S,
\]

one has AB=hS=X and BA=sqrt(h) S sqrt(h)=Y.
The latter is bounded selfadjoint.
The operator B is injective on the ambient standard Hilbert space: Bv=0 first gives Sv=0 by injectivity of sqrt(h), and then v=0 by injectivity of S.
No inverse of h, S, A or B is applied to a Hilbert vector.

These statements concern bounded left multiplication on the ambient L2 space, exactly as permitted by the conditional theorem.
B need not preserve the smaller target standard Hilbert space, and neither B nor Y is claimed to belong to N=W*(X).

## The exact reference input supplies every spectral parameter

C_F0147 Section 3 establishes maximal Delta for the bounded finite-Fisher reference tuple (h,S1,S2), and accepts the full-linear/full-polynomial equivalence that makes every full square polynomial matrix injective in its ambient standard representation.
For each complex lambda, the scalar polynomial hS1-lambda is nonzero in the reference free polynomial algebra: its length-two word hS1 has coefficient one and cannot cancel with a scalar.
A nonzero one-by-one polynomial matrix is full, since factorization through size zero would give the zero matrix.
Thus X-lambda is injective on that three-variable ambient Hilbert space for every lambda, including zero.

The two-variable reference algebra W*(h,S1) embeds trace-preservingly into the three-variable reference.
Its L2 subspace is invariant under hS1-lambda; a kernel vector there would already be an ambient kernel vector.
Therefore the same injectivity holds on the two-variable reference space used in C_F0151.
This restriction does not assert equality with the target algebra W*(hS1).
The unchanged accepted C_F0147/R_F0154 source scope is reused; the entire MSY source proof is not newly audited here.

## Bounded intertwining proves diffuseness

The repaired identity has the correct order:

\[
 X\sqrt h=hS\sqrt h=\sqrt h(\sqrt h S\sqrt h)=\sqrt hY.
\]

If (Y-lambda)v=0 for a Hilbert vector v, bounded multiplication gives

\[
 (X-\lambda)\sqrt h\,v=\sqrt h(Y-\lambda)v=0.
\]

Injectivity of X-lambda implies sqrt(h)v=0, and injectivity of sqrt(h) gives v=0.
The proof is valid for every complex lambda and does not separate zero through an inverse-product argument.

For selfadjoint Y, an atom in its tracial spectral law at a real lambda would give a nonzero spectral projection e and hence a nonzero L2 eigenvector e Omega, because the trace is faithful.
The absence of all eigenvectors therefore makes its law diffuse.
This verifies the remaining concrete hypothesis of the conditional theorem.

Consequently that theorem, once adopted at its separate independent scope, applies to the actual pair N=W*(hS) inside the two-variable reference algebra.
If a generator-first bare dual D satisfies [X,D]=P, then E=-D satisfies [E,X]=P.
The conditional result therefore gives exactly the stated operator-norm-to-L2 bound for every such witness.
It does not construct one, constrain a canonical adjoint domain, or prove the projective criterion without its separate argument.

## Application conclusion

**The repaired concrete application of C_F0151 v2 passes this independent check.**
The factorization, all-lambda reference injectivity, bounded intertwining, diffuseness and sign conversion are valid at the stated target/ambient domains.
This finding complements, and does not replace, the other review's coverage of the unchanged general theorem and criterion.
V1's reversed-order reasoning is not covered by this passing finding.
No modification to v2 is required within this narrow scope.

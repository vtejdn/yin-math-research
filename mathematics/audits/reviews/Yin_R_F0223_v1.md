---
author: Yin
---
# Independent review of normality for ACSY generators with fibers of order at most two

## Whole-proof finding

At 2026-11-13T14:22 UTC a separate agent outside proof development reviewed Yin's complete [C_F0215 v1 argument](../../claims/Yin_C_F0215_v1.md#argument) for the candidate decision dated 2026-11-13T14:19.
The reviewer received the fixed Claim and review scope and consulted no proof-development dialogue, exploratory notes, author explanation or previous finding on this Claim.
The weaker derivation and injectivity hypotheses imply normality, with the stated first- and third-order local lower bounds on the two possible nonnormal parts.
The actual ACSY hypothesis supplies injectivity and gives the asserted strong and bare full-domain duals.

The ACSY derivation has the starred core, outer actions and actual adjoint vacuum required by Proposition 3.5, so maximality holds for this bounded generator.
For every fixed complex \(a\), the size-one polynomial \(u-a\) is full, and its affiliated inverse from MSY23 Theorem 1.1 forces its kernel projection to vanish.
Functional calculus computes this projection fiberwise, with positive normalized trace on any fiber where \(a\) is an eigenvalue.
This excludes a positive mass of such fibers for each fixed \(a\).
For a fixed second endpoint the excluded eigenvalues form a finite set, so Fubini gives disjoint spectra almost everywhere on the product.
The common-root condition is measurable, for instance by the resultant of the two characteristic polynomials on each pair of fiber sizes.

For \(C=[X,X^*]\) the quadratic identity gives \(C^2=\tfrac12{\rm Tr}(C^2)I\) on two-dimensional fibers, and the coefficient is strictly positive on each nonnormal fiber.
Polarization gives the displayed anticommutator formula, and tracing \(X^j C\) gives zero by cyclic permutation.
Thus the three central polynomials have the asserted values on all fibers, including the one-dimensional ones where each vanishes.
On the nonnormal part their common level sets determine the trace and determinant of \(X\), since \(2\det X=({\rm Tr}X)^2-{\rm Tr}(X^2)\).
A positive mass on a level set would therefore put positive mass on a fixed eigenvalue.
The law of the triple is diffuse on this part, which removes its equality locus from the product measure.

The inclusion of the generated algebra preserves its tracial Hilbert norm and intertwines its two multiplication actions with the ambient field actions.
Taking the Hilbert tensor of this inclusion embeds the coarse bimodule into the product field, with a simple tensor evaluated at its two respective endpoints.
Differentiating \(Za=aZ\) there gives the scalar endpoint difference times \(\delta a\) equal to the outer difference \(D_a\delta Z\).
A common full-measure set suffices for this finite family of relations.
Division at each pair yields (2), regardless of the integrability of the quotient.

For simple roots, right multiplication by \(P_1(t)\) on the first factor kills \(P_2(t)\) and commutes with left multiplication by \(X_t^*\).
Left multiplication by \(P_1(s)\) on the second factor kills \(P_2(s)\) and commutes with right multiplication by \(X_s^*\).
Applying these operations to the entire Sylvester inverse therefore isolates exactly the denominator \(\lambda_1(t)-\lambda_1(s)\), even if the other same-branch denominator tends to zero at a comparable rate.
If the residue at equal matrices vanished, contracting its second tensor factor against a linear functional taking value one at \(p\) would give \(x^*p\in\mathbb Cp\).
The eigenline would then reduce \(x\), which diagonalizes \(x\) in an orthonormal basis in dimension two.
Hence the residue norm stays positive on a neighborhood of the nonnormal matrix, and both filter norms are bounded there by continuity of the local idempotents.
Second countability supplies a positive-measure choice of neighborhood with one consistent root label.

For repeated roots, write \(A=L_{N_t}\otimes I\) and \(B=I\otimes R_{N_s}\).
They commute and have square zero, so \((A-B)^2=-2AB\), and the reciprocal of \(dI+A-B\) has the displayed negative cubic numerator when applied to the unit tensor.
Multiplication by \(d^3\) before applying the adjoint-generator difference gives (4), including its scalar \(\bar d\) and the right product \(N_sN_s^*\).
At coincidence, tracing the first factor leaves \(-2\,{\rm Tr}(N^*N)N\ne0\).
Continuity on the repeated-root locus and the same countable-cover argument give a local uniform bound times \(|d|^{-3}\), without any division at an equal eigenvalue.

Each chosen eigenvalue law is bounded, finite, nonzero and diffuse, including after restriction to the selected neighborhood.
Summing the squared masses in disjoint planar grid cells gives a mass of at least a positive constant times \(r^2\) at distances at most \(r\), and diffuseness removes the diagonal.
Layer integration against \(2r^{-3}\,dr\) gives logarithmic divergence for the inverse-square kernel already at distances below one, where the inverse-sixth power dominates it.
Thus the squared Hilbert norm of the starred value would have infinite integral in either nonnormal case.

With normality established, spectral calculus identifies \(M\) with the scalar algebra of the compact diffuse spectral law of \(X\).
Differentiating commutativity fixes \(\delta X^*=(\bar z-\bar w)/(z-w)\) almost everywhere, and the derivation rule then gives the scalar divided difference for every represented star polynomial.
Pairing it with the unit tensor gives precisely the vacuum functional in the scalar part of C_F0055 v1.
For the original closure \(E\) of the right slice, the [reviewed scalar conclusion](Yin_R_F0037_v1.md#scalar-findings) puts every bounded function in \(\operatorname{Dom}E\cap\operatorname{Dom}E^*\).
On the polynomial core \(E_0(zp)=zE_0p+P_\Omega p\).
Approximating any vector of \(\operatorname{Dom}E\) in the graph norm and using boundedness of multiplication by \(z\) and of \(P_\Omega\) preserves this identity on the closed domain.
Consequently \([X,-E]=P_\Omega\) on every bounded vector, with the adjoint-domain inclusion required for the strong dual and the restriction required for the bare dual.
The source theorems were used at the statement and applicability depth of the cited units.
This review covers the size-two result and its scalar conclusion only.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0215_v1.md#statement) | Field and trace hypotheses, weaker normalized derivation, simple and repeated root lower bounds, normality and both full-domain duals under actual ACSY. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0215_v1.md#argument) | Central separators, product exceptions, Sylvester equations, bounded idempotent filters and Jordan coefficients, planar energy and scalar operator domains. |
| [Whole-proof finding](#whole-proof-finding) | [ACSY maximality](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 applied to the represented starred algebra, normalized coarse derivation and actual vacuum. |
| [Whole-proof finding](#whole-proof-finding) | [Affiliated invertibility](../literature/MSY23/Yin_U001.md#msy23-u001) | Theorem 1.1 for full scalar linear polynomials of the one bounded generator and its kernel projections. |
| [Whole-proof finding](#whole-proof-finding) | [Planar diagonal energy](../../claims/Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Rechecked the grid and layer integral for each bounded diffuse branch law of positive mass. |
| [Whole-proof finding](#whole-proof-finding) | [Scalar canonical domains](../../claims/Yin_C_F0055_v1.md#statement) | Scalar vacuum and both original domains for the right contraction with the generator-first sign after negation. |

---
author: Yin
---
# Independent review of localized column bounds on separated normal spectral components

## Whole-proof finding

At 2026-11-14T10:07 UTC the reviewer independently checked all three parts of the [statement](../../claims/Yin_C_F0237_v1.md#statement) and the complete [argument](../../claims/Yin_C_F0237_v1.md#argument) fixed in the [candidate decision](../../claims/Yin_C_F0237_v1.md#decision-candidate) of 2026-11-14T10:06.
The reviewer had independently reviewed the finite-arc parameter theorem C_F0234, had used the two-Haar column criterion, and had worked on a separate question about omitted algebra unitaries.
The reviewer had no part in developing the separated-component or partial-unitary argument of this candidate and consulted no exploration draft, proof-development discussion or earlier finding for it.
All three claims hold, including the full original starred-core column bound and both canonical bounded-vector domains at the distinguished coordinate.

**Different components and column encoding.**
For an elementary tensor \(x\otimes y\) from \(Dz\), the first term of the Leibniz rule on \(zw\) contributes \(x\tau(yw)\) to \(L(zw)\).
After the right multiplication by \(v\) this is \(xv\tau(wy)\), exactly \(C I_{v\otimes w}(x\otimes y)\).
Continuity on the Hilbert tensor space proves (1), and uniform approximation of \(w\) in the norm closure uses only the bounded extension of \(L\).
The resulting operator-norm-to-Hilbert bound is \(2B\|v\|\|w\|\), so absolute projective sums can be applied before the final slice.
For \(D=I_{X\otimes1-1\otimes X}\delta\), the off-diagonal marginal phase gives \(D(X^*)=X^*\otimes1-1\otimes X^*\).
The other generator values, the actual adjoint of the two core tensors and reality after multiplication by \(i\) put this derivation within the liberation contraction calculation, also in the free enlargement.
Two separated compact spectral components admit smooth disjoint cutoffs with positive distance between their supports.
Dividing their product by \(z-w\) gives a smooth four-real-variable kernel, and the Fourier majorant \((1+|m|^2)^{-3}\) is summable in dimension four.
Each separated Fourier factor is a continuous marginal function, so (1) applies, and multiplication by the liberation symbol gives exactly the \(a,b\) indicator tensor.

On the enlarged algebra the Haar generator cuts are zero and \(\widetilde E_{ab}(u_j z_j)=u_j E_{ab}(z_j)\) for old coefficients.
The old enlarged vacuum and spectral projections agree on the old algebra.
The old Hilbert values multiplied by the free conjugates \(u_j\) are orthogonal across \(j\) by conditional expectation, extending from bounded old vectors by density.
The two-Haar norm bound for their polynomial input is twice the old column norm, which gives \(4B_{ab}^2\) after squaring.
This argument converts an enlarged singleton estimate into the claimed column bound even though the localized map has its own generator value.

**Same-component cores and actual vacua.**
Compact injectivity and regularity give projection charts through the endpoints of an arc and around every point of a closed curve.
The inverse on the circle is taken as a circle-valued function on the curve, so patching its plane extensions does not require a single continuous angle on the circle.
A cutoff separating \(K_a\) from the remaining spectrum extends the corner-supported functions while retaining their prescribed values on all other components.
The scalar marginal formula and uniform \(C^1\) plane-polynomial approximation thus give both norm and coarse-graph approximation, for the functions and their adjoints.
In particular this applies to \(p\), the corner parameter and \(X(1-p)\), and finite product approximants justify the actual closed product rule throughout the mixed core \(\mathcal Q\).
This is a weakly dense unital star core since corner functional calculus recovers \(Xp\) from \(t\) and \(p\).

On the real interval the secant \(J\) has derivative on the diagonal.
Across the diagonal of the torus it is the quotient of two \(C^2\) angular divided differences, with denominator \(i e^{i\theta}\) at equality.
Injectivity off the diagonal and regularity on it give a positive lower bound for \(|J|\) on the parameter square, and the reciprocal \(K\) has summable separated coefficients by the two-dimensional \(H^2\) Fourier estimate.
For the tensor adjoint of \(J\), a source coefficient \(c_n\) of \(r\) on the circle produces \(|n|\) Laurent tensor terms, with total absolute frequency in each term at most \(|n|+1\), for both positive and negative powers.
The zero power in a corner factor is \(p\).
Between distinct components the old scalar derivative of each factor is bounded by a fixed reciprocal separation, and on \(K_a^2\) it is bounded by its frequency times \(\|K\|_\infty\).
These bounds apply also to the adjoints, and the original vacuum pairing on products gives an actual adjoint-domain bound of order \(1+|\alpha|+|\gamma|+\|\xi_i\|_2\) per factor pair.
Thus the Laurent series converges in the actual adjoint graph by \(\sum_n(1+n^2)|c_n|<\infty\).
On an interval the integral representation for the secant has a coefficient of order \(|n c_n|\) and its two frequencies have total absolute value \(|n|\omega\), yielding the same summability and graph-continuous integrals.
Consequently \(I_J^*(1\otimes1)\) belongs to the original adjoint domain, and testing the restriction of the original closed graph to \(\mathcal Q\) gives the asserted actual vacuum of \(\theta\).
The symbols of both \(p\) and the complementary coordinate are constant on \(K_a\), so their derivatives after this inner localization vanish.
For \(t\) the localized derivative is \(p\otimes p\).
In the arc case this generator rule and the zero starred omitted values imply reality, algebraic tensor range and equality of the two iterates, because the iterated difference is an outer derivation and \(\theta p=0\).
Mai's slice bound therefore applies on the full mixed core.

**Noncentral partial unitary.**
The outer support of \(\theta u^*\) follows from \(u^*=pu^*p\) and \(\theta p=0\).
Then \(0=\theta(uu^*)=p\otimes u^*+u\,\theta u^*\) implies \(\theta u^*=-u^*\otimes u^*\).
For \(\beta=iI_{u\otimes p}\theta\) the two generator values are \(iu\otimes p\) and \(-ip\otimes u^*\), which are flip-adjoints of each other.
The actual vacuum follows from testing the \(\theta\)-adjoint on \(-iu^*\otimes p\), a tensor of mixed core factors.
The same product rule applied to the actual vacuum of \(\beta\) puts the dense algebraic core tensors in its adjoint domain and supplies closability.
On \(u\) the iterated difference is \(-u\otimes p\otimes p\), while on \(u^*\) it is \(p\otimes p\otimes u^*\).
Its two mixed Leibniz terms cancel, and insertion of \(p\) in the middle leg commutes with both outer actions.
These generator checks prove (3) on all words without moving \(p\) past an omitted generator.
Contraction sends \(\kappa_p\beta\) to \(\tau(p)T\), where \(T=C\beta\).
The algebraic range ensures \(Tz\in\mathcal Q\), so \(T^2z\) is defined, and reality gives both \(\zeta=\zeta^*\) and \(T^*z=z\zeta-Tz\).
Using these identities in the cited unitary energy computation gives precisely the additional term \(-\operatorname{Re}\langle i\tau(p)Tz,z\rangle\).
For the analytic unitary made from a strict selfadjoint contraction, the binomial approximants for it and its adjoint converge in norm and in the first derivative graph.
Their product derivatives converge to zero by closability and the constant product \(1\).
The energy identity then gives \(2\|\zeta\|_2+\tau(p)\) on these unitaries, since the whole-algebra trace gives them Hilbert norm one.
Averaging the two signs, scaling strict selfadjoint inputs and splitting a general input into real and imaginary parts give the stated factor of two on \(\mathcal Q\).
The inner support gives \(C\theta(z)\in Hp\) and \(Tz=i(C\theta(z))u\), so right multiplication by \(u^*\) recovers \(C\theta(z)\) using \(uu^*=p\).

**Returning to the original core and the Task domains.**
In (4), \(L(zw_\ell)\) is legitimate on the norm closure of \(\mathcal Q\) while the coarse product identity is evaluated on \(z\in\mathcal Q\).
The projective expansion for \(K\) recovers \(I_{p\otimes p}\bar\delta\) there by cancellation on the corner tensor square.
For each original word the indicated substitutions lie in \(\mathcal Q\) and converge in norm.
Their marginal derivative errors on \(K_a^2\) are bounded by the inverse secant norm times the parameter difference-quotient error.
For Laurent sums the shortest angular distance divided by the chord length is at most \(\pi/2\), which controls those difference quotients, including for the adjoints.
The complementary square has zero error and the cross terms converge by separation.
The product rule gives convergence in the original derivative graph of every substituted word and hence of every old polynomial.
Taking this limit transfers the right-slice bound to the original core, including the corresponding original core of the enlargement, where the column encoding applies.
The finite sum over all ordered pairs \(a,b\) recovers \(C\delta_i\) because the inner multipliers sum to the identity.
The column triangle inequality proves finiteness of its original column cost.
Reflection of every carrier and the adjoint companion tuple give boundedness of the other original slice by the flip-adjoint formula.
C_F0072 Part B now places all bounded vectors in the actual canonical closure and adjoint domains.
For a sequence from the original graph core converging to a closed-domain input, the generator commutator identity forces the left-multiplied sequence also to converge in the graph, since the extra rank-one term is bounded.
The negative canonical closure thus has the generator-first commutators of the Task on all bounded vectors.
Applying this at every covered coordinate yields the stated sufficient condition for a strong system.
The result is conditional on the finite separated spectral cover and leaves the general correlated-normal Task open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0237_v1.md#statement) | All three items, including cross components without regularity, whole closed carriers, original column and strong domains. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0237_v1.md#argument) | Localization, actual graph transport, corner energy identity, original-core recovery, finite column encoding and two-sided canonical domains. |
| [Whole-proof finding](#whole-proof-finding) | [Original Task definitions](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Actual represented starred derivation, strong adjoint and operator domains, and generator-first commutator sign. |
| [Whole-proof finding](#whole-proof-finding) | [Normal phase](../../claims/Yin_C_F0076_v1.md#statement) | Part 1, diffuseness, original graph, starred marginal derivatives, zero omitted values and conjugate companions. |
| [Whole-proof finding](#whole-proof-finding) | [Liberation contraction](../../claims/Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions) | Actual core vacuum and bounded right slice of the liberation derivation. |
| [Whole-proof finding](#whole-proof-finding) | [Free enlarged vacuum](../../claims/Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Actual old-coordinate derivation and vacuum retained with zero new Haar cuts. |
| [Whole-proof finding](#whole-proof-finding) | [Free column encoding](../../claims/Yin_C_F0208_v1.md#encoding-finite-columns-by-two-haar-unitaries) | Norm factor two and orthogonality of the old Hilbert-space coefficients. |
| [Whole-proof finding](#whole-proof-finding) | [Parameter charts](../../claims/Yin_C_F0234_v1.md#parameters-on-disjoint-arcs) | Endpoint extensions, compact embedding and separated plane cutoffs. |
| [Whole-proof finding](#whole-proof-finding) | [Marginal approximation](../../claims/Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) | Uniform real \(C^1\) approximation by starred polynomials and uniform convergence of off-diagonal quotients. |
| [Whole-proof finding](#whole-proof-finding) | [Fourier estimates](../../claims/Yin_C_F0137_v1.md#fourier-summability-needed-for-the-two-changes-of-coordinates) | Weighted one-dimensional coefficients and two-dimensional absolute summability. |
| [Whole-proof finding](#whole-proof-finding) | [Tensor adjoint](../../claims/Yin_C_F0137_v1.md#ax-implies-as-actual-adjoint-of-the-j-multiplier) | Actual adjoint norm estimate and graph-continuous integration for bounded differentiated factors. |
| [Whole-proof finding](#whole-proof-finding) | [Real coassociative estimate](../literature/Mai15/Yin_U002.md#mai15-u002) | Theorem 4.9 on the actual algebraic-valued arc derivation on the mixed core. |
| [Whole-proof finding](#whole-proof-finding) | [Unitary energy calculation](../../claims/Yin_C_F0043_v1.md#31-the-exact-defect-of-coassociativity) | Equations (12)–(13), with the middle-leg projection and resulting scalar \(\tau(p)\) checked separately. |
| [Whole-proof finding](#whole-proof-finding) | [Two canonical domains](../../claims/Yin_C_F0072_v1.md#statement) | Part B for the original two bounded trace slices, the closure and its actual Hilbert adjoint. |

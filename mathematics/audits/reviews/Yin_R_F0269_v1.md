---
author: Yin
---

# Independent review of the weighted drift and Gaussian covariance criterion

A reviewer for Yin examined the entire [candidate dated 2026-11-14T12:14](../../claims/Yin_C_F0260_v1.md#decision-candidate), including its original canonical domains and column bounds.
The reviewer had no role in developing the proof and received the claim locator and review scope without development dialogue, exploration notes, author explanations or earlier findings on this candidate.

## Finding

At 2026-11-14T12:23 UTC the reviewer found the equivalence and both vacuum formulas proved under the stated row bound and measurable real drift.
The argument also proves the bounded-vector domains of the original right slices and their Hilbert adjoints, and the right column inequalities for the tuple and its adjoint tuple.
The following checks cover the complete argument and the uses of its declared project dependencies at their selected proved scopes.

For the necessity direction, the scalar vacuum pairing restricts to the represented marginal core, where the derivative in \(Z\) is the scalar divided difference and that in \(B\) vanishes.
Testing the latter on \(\alpha B\gamma\) identifies \(b\overline{P_{H_1}\xi_B}=1\), since marginal polynomial rectangles distinguish finite complex measures on the compact product.
This excludes a positive-measure zero set and gives the reciprocal test.
Multiplication by \(b\) then takes \(L^2(b^2\,d\mu^2)\) onto \(H_1\), so the intrinsic algebra contains the vector of \(S\) in its tracial Hilbert space.
Since \(S\) is bounded, conditional expectation fixes it as an operator.

For smooth positively separated endpoint tests, \(C^1\) polynomial approximation controls the divided differences uniformly and the bounded letter \(B\) preserves convergence in the Leibniz expansion.
In the linear test, inserting the omitted drift slot in the scalar telescoping identity for \(\alpha f\gamma=0\) produces the term \(\alpha(z)d_f(z,v)\gamma(v)\).
In the quadratic test the two omitted drift slots produce that same term multiplied by \(q(v)f(v)+f(z)q(z)\).
These identities use pointwise telescoping off the diagonal, even for a measurable representative of \(f\).
The remaining endpoint and middle derivatives have the opposite total contribution, giving first \(P_{H_1}\xi_Z=-\overline J\) and then precisely its pairing with the quadratic test's one-edge component.
The two-field terms give \((b(w,v)^2-b(z,w)^2)/(z-v)\), with the scalar component of the tested word zero by disjoint support.
The squared \(L^2\) norm of the unweighted two-edge product \(b(z,w)b(w,v)\) is at most \(\rho^4\) by symmetry and integration at \(w\).
Consequently the vacuum pairing density is locally integrable at separated endpoints, and testing there with middle polynomials identifies \(P_{H_2}\xi_Z=K\) on the complement of the null endpoint diagonal.
The geometric reformulation uses only the scalar part of the compact planar marginal theorem.

For sufficiency the adjoint on each tensor leg reverses the last two vertices of \(A_0\) and the first two of \(A_1\), respectively.
For \(r=b(w,v)/b(z,w)>0\) the resulting numerators \(r-1\) and \(1-r^{-1}\) have product \((r-1)^2/r\ge0\), bounding the sum of squared coefficient norms by \(\|K\|_2^2\).
Reinsertion gives their sum with denominator \(\bar z-\bar v\), while a degree-zero insertion conjugates each scalar coefficient with its endpoint order preserved.
This yields \(\zeta-\overline J+K\) in three orthogonal degrees and \(b^{-1}\) in degree one for \(B\).
The degree-zero and degree-one cut estimates and the free lift of the scalar derivative give both sliced bounds on the reference core by addition, so the two-slice theorem gives the required actual reference graphs.

For the weak test, the soft difference for \(g\) is its divided difference multiplied by \(|z-v|^2/(|z-v|^2+\varepsilon^2)\).
Joint \(L^1\) convergence therefore gives convergence against any bounded polynomial tensor.
Equation (M5) supplies weak \(L^2\) convergence of the adjoints on that tensor, so pairing against fixed \(g\in L^2\) identifies the same limit.
With an extra variable the tensor product of a weakly convergent adjoint test and a fixed polynomial converges weakly in the product Hilbert space.
This justifies using the integrated formula for the measurable edge coefficients.
In particular \(d_f=bJ\) lies in \(L^1\), and multiplying each correction array by the outer \(b(z,v)\) gives an \(L^1\) function on triples by Cauchy–Schwarz and the row bound.
Taking the positive clipping \(b_m\) preserves integrable domination of both formal differences by the Lipschitz property and preserves the uniform field norm bound.
At each fixed clipping, moving the scalar derivative onto the polynomial test handles the approximants' derivative pairings by \(L^2\) convergence of their kernels.
The insertion pairings pass by bounded convergence there, and then by domination by \(b\) times the absolute coefficient as \(m\) increases.
These two limits cancel both external-edge differences and \(d_f\) at \(Z\), and leave \(1\otimes1\) at \(B\) for its own derivative.

Moving the closed reference slice to its adjoint on the left test vector justifies strong-star passage on the operator side.
Uniformly bounded graph approximants for the input and its product with \(B\) have bounded slice images, and weak closedness identifies every weak cluster point with the corresponding actual graph value.
This gives the commutators on every bounded vector.
Negating the reference slices gives the prescribed generator-first sign and retains the required adjoint domains.
Conversely, an arbitrary full strong system on the intrinsic normal tuple satisfies the normal reconstruction theorem, including the adjoint-at-\(1\) hypothesis that supplies actual ACSY.
For the constructed system its slices vanish at \(1\), so induction using the starred generator commutators identifies them with the target slices on the represented mixed core.
The adjoints at \(1\) consequently determine all target vacuum components, including the absence of any higher ones.
Conjugating the base variable sends the marginal vacuum to its adjoint and preserves each integrability test.
The right bound for that tuple applies to the flip-adjoint of the original derivative on the starred core, giving the original left bound.
The two bounds are therefore available on the target core itself for Part B of the two-slice theorem, which establishes both original canonical domains.

On adjoining two independent semicirculars the free reference estimate still applies, and each inserted tensor uses just the old color.
The added colors do not contribute to the tested coefficients of \(B\).
The resulting bounded-input slice agrees with the original on old polynomials and commutes with each added left multiplier on bounded vectors by its zero commutator.
Norm approximation gives the same commutation for the two continuous Haar functions.
For \(u_k=U^kVU^{-k}\), freeness gives \(\mathbb E_{\rm old}(u_k^*u_l)=\delta_{kl}1\), hence orthogonality also for old Hilbert-valued outputs by bounded approximation.
Applying the enlarged slice to \(\sum_k u_kp_k\) and using the free Haar norm bound \(2\|\sum_k p_k^*p_k\|^{1/2}\) gives a uniform column constant at each old coordinate.
Conjugation of the base repeats this argument for the adjoint tuple.
The review concerns the stated single-channel drifted model and the indicated interfaces of previously proved inputs.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate decision](../../claims/Yin_C_F0260_v1.md#decision-candidate) | Whole dated candidate with the row bound and real measurable drift. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0260_v1.md#statement) | All three equivalent conditions, generation, both complete vacua, norm, original graphs and both oriented column bounds. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0260_v1.md#argument) | All necessity tests, reference constructions, weak coefficient limits, intrinsic identifications, adjoint orientation and enlarged column argument. |
| [Finding](#finding) | [Gaussian fields and generation](../../claims/Yin_C_F0157_v2.md#bounded-coordinates-phase-and-generation) | Positive-amplitude generation, bounded field and strong-star convergence of the clipped fields. |
| [Finding](#finding) | [Normal phases](../../claims/Yin_C_F0076_v1.md#statement) | Marginal divided difference, zero omitted starred derivatives and the actual flip-adjoint companion. |
| [Finding](#finding) | [Target moment tests](../../claims/Yin_C_F0156_v1.md#actual-target-moment-tests) | Smooth separated endpoint tests in the original vacuum pairing and the product rule. |
| [Finding](#finding) | [Centered quadratic test](../../claims/Yin_C_F0157_v2.md#necessary-integrals-on-the-target-core) | Surviving centered two-field density with a row bound and the squared path product estimate. |
| [Finding](#finding) | [Reference corrections](../../claims/Yin_C_F0209_v1.md#reference-corrections-for-bounded-positive-matrices) | Scalar free lift, one-channel signs and orientation, external multiplication by the field coefficient. |
| [Finding](#finding) | [Finite-degree cut estimates](../../claims/Yin_C_F0209_v1.md#contractions-with-a-single-inserted-color) | Hilbert insertions of degrees zero and one, both sliced orientations and adjoint reinsertion with additional inactive colors. |
| [Finding](#finding) | [Weak integration by parts](../../claims/Yin_C_F0156_v1.md#weak-algebraic-tensor-integration-by-parts) | Weak convergence in (M5) on fixed polynomial tensor tests, also with an extra fixed tensor factor. |
| [Finding](#finding) | [Kernel commutator tests](../../claims/Yin_C_F0156_v1.md#bounded-gaussian-kernels-and-the-original-reference-commutator) | Bounded symmetric approximants, polynomial tensor testing and adjoint passage in reference commutators. |
| [Finding](#finding) | [Strong-to-ACSY theorem](../../claims/Yin_C_F0070_v1.md#statement) | Full generator-first domains on the normal intrinsic tuple, vacuum at the unit, and canonical normalization on the core. |
| [Finding](#finding) | [Original two-slice theorem](../../claims/Yin_C_F0072_v1.md#statement) | Separate bounds for both orientations yield both full original domains on the reference and the target. |
| [Finding](#finding) | [Column encoding](../../claims/Yin_C_F0241_v1.md#two-gaussian-channels-supply-the-column-test-inside-the-model) | Free Haar functions, commutation on bounded elements, input norm and orthogonality for old coefficients. |
| [Finding](#finding) | [Scalar geometric criterion](../../claims/Yin_C_F0255_v1.md#statement) | Equivalence of the scalar vacuum with square-integrable maximal linear density and finite total squared curvature. |

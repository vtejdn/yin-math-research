---
author: Yin
---

# Review of the Hilbert–Schmidt drift criterion for arbitrary free selfadjoint noise

At 2026-11-14T13:24 UTC, a separate agent reviewed for Yin the whole [candidate dated 2026-11-14T13:19](../../claims/Yin_C_F0268_v1.md#decision-candidate).
The reviewer had no role in its development and received the fixed claim and the requested scope without exploration notes, proof-generation dialogue or earlier findings on this claim.
A review of a different claim was consulted for its record format.

## Finding

The equivalence, the two original bounded-vector domains, both finite-column conclusions and the vacuum norm identity hold under the stated hypotheses.
The proof uses the scalar noise vacuum and the two base column hypotheses even when the drift is an arbitrary bounded selfadjoint element of the generated base algebra.

On the base, the reversed right-slice bound is a left-slice bound by the flip-adjoint rule, so the two-contraction theorem applies.
For the free extension of the old derivative, the slice takes \(w b\) to \(w E_i b\) for every orthonormal prefix \(w\) ending in the noise factor and every base core coefficient \(b\).
Summing the coefficient squares gives the conditional expectation onto the base of the input column square.
This proves the free old column estimate in each orientation.
Matrix Kaplansky density supplies core columns with a common bound approaching the column norm.
Their images are weakly relatively compact, and the weakly closed linear graph identifies every cluster point with the value of the original closure.
The same argument applies to bounded strong-star approximation of products involving the drift.

For necessity, the forced marginal phases identify the restriction of the target old derivative on the base core, hence the projection of its vacuum \(\zeta\) is \(\xi_i\).
Writing \(v_0=v-\tau(v)\), the map \(a\otimes b\mapsto a v_0 b\) multiplies Hilbert norm by \(\|v_0\|_2\).
In the test on \(aTb\), a trace leg containing \(v_0\) between base factors has zero trace.
For a core-polynomial drift the remaining difference is \(-\tau(a[E_i,B]b)\) by the product rule.
Replacing the drift by \(B+\tau(v)1\) preserves the commutator, and bounded selfadjoint core approximants give the same identity for this drift by testing \(E_i((B+\tau(v)1)b)\) against \(a^*\in\operatorname{Dom}E_i^*\).
If \(d\) represents the resulting functional on the coarse tensor product, then \(\langle d,a\otimes b\rangle=\langle a^*,\Theta(d^\star)b\rangle\).
Indeed \(d=x\otimes y\) gives \(\tau(x^*a)\tau(y^*b)\).
Thus \(-\Theta(d^\star)\) agrees with \(K_i\) on the core and then on all bounded base inputs by the graph limits just described.
This necessity test uses the variance of \(v\) only to ensure continuity and introduces no variance factor into the identified commutator.

For the insertion estimate, the represented free-product core admits the derivation with \(d_\beta v=\beta\) since the diffuse selfadjoint coordinate has no polynomial relation.
For \(\beta=x\otimes y\), every cut before the final noise block of a reduced word has zero right trace.
After cyclically moving the last base coefficient next to \(y\), the remaining suffix, including its later centered noise block, has zero expectation onto the base, even after its first noise coefficient is split into scalar and centered parts.
The last cut on \(qba\) leaves \(q(e b)x\,\tau(a y)\).
In the right noise-module expansion of \(p_j y\), deleting scalar coefficients for the nonempty prefixes changes the coefficient column norm by at most \(\|y\|_2\), since their squared moduli sum to at most the trace of the full coefficient column square.
Conditional expectation bounds that full square by \(\|y\|_2^2 1\) for a unit input column.
The centered scalar slice \(e_c\) kills constants, and on the projected coefficients it produces \(q(e_c b)\tau(a y)\).
The commutative finite-family inequality bounds the resulting map \(S_p:H\to K_0^m\) by \(2\sqrt{4/\pi}\,a_v\).
Multiplication is an isometry on \(K_0\otimes_2 H\) because the scalar and centered parts of the appended base coefficient land in orthogonal reduced summands.
Applying \(S_p\otimes I\) to the flipped tensor \(\sum y_\ell\otimes x_\ell\) therefore controls the entire centered column by the coarse norm.

For the scalar output let \(P\) retain the vacuum and the words ending in a centered base letter.
For any \(y\in R\), decompose \(ay=\tau(ay)1+(ay)^\circ\).
The suffix \((ay)^\circ g^*\) ends in a centered noise letter, whereas the component \(\tau(ay)b g^*\) contributes \(q\,\tau(ay)\tau(b g^*)\) after projection.
Bounded centered approximation of \(g^*\) justifies the computation in \(L^2\).
Right multiplication by each \(x_\ell\) is performed *after* this projection.
Writing \(P=I-Q\), the identity term is the column of \(p_j\sum_\ell y_\ell g^*x_\ell\), whose norm is bounded by \(\|g\|_2\|\beta\|_2\) by freeness and the input column bound.
For the complementary term, \(y\mapsto(Q(p_j y g^*))_j\) maps \(H\) into \(K_0^m\) with norm at most \(\|g\|_2\) because \(\|y g^*\|_2=\|y\|_2\|g\|_2\).
The same tensor multiplication isometry supplies a second bound \(\|g\|_2\|\beta\|_2\).
These two estimates justify scalar deletion with the indicated order of all base factors.
At each fixed polynomial the coarse derivation value depends continuously on \(\beta\), so the bounds pass to every Hilbert tensor.

The ordinary free noise derivative has vacuum \(g\) by the centered-word trace test.
For \(x\otimes y\), the double trace of the insertion equals that of the ordinary derivative of \(xpy\).
This pairs \(p\) with \(x^*g y^*\), giving the componentwise adjoint in (6).
The flip-adjoint instead takes the reversed derivation to \(d_{\beta^\dagger}\), giving the left-contraction bound required for the actual adjoint domain.
The product rule gives \([F_\beta,v]p=x\tau(yp)\) for \(\beta=x\otimes y\), hence \([F_\beta,v]=\Theta(\beta)e_R\) on bounded vectors by Hilbert tensor density and bounded core approximation.
On nonempty old-slice prefixes ending in a noise letter, base left multiplication preserves the prefix space and leaves the terminal coefficient unchanged.
The commutator with \(B\) consequently vanishes there, and is \(K_i\) on the base summand.

Taking \(\beta_i=-\Theta^{-1}K_i\) cancels the old commutator with \(T\).
At the last coordinate \(\Theta(1\otimes1)e_R=P_1\) on the full free-product Hilbert space.
Negating the normalized operators gives the generator-first sign, and pairing on bounded inputs places every bounded vector in the actual adjoint domains of the sums.
Since \(W^*(Y)\) contains \(R\) and \(v=T-B\), the normal strong-to-actual theorem applies on the original represented target core, recovering its conjugate vectors from the adjoints at \(1\).
The correction \(J_g(\beta_i^\star)\) is orthogonal to the base and has squared norm \(\|g\|_2^2\|K_i\|_{\rm HS}^2\) by freeness.
The canonical comparison then identifies the negative original slice closures on all bounded vectors, so the target core inherits the established column bounds.
For \(Y^*\), flip-adjoint actuality gives the necessary commutators using \(X^*\) as base, with the same \(T=v+B\) and the two available base orientations.
The construction and column estimate consequently apply to that tuple as well.
The earlier scalar estimate, commutative finite-family inequality and normal canonical-domain results were used at their stated interfaces.
This review concerns the drift class specified in the candidate.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0268_v1.md#decision-candidate) | Candidate dated 2026-11-14T13:19 and its selected premises. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0268_v1.md#statement) | Three equivalent conditions, original canonical duals and adjoints, both finite-column orientations and exact vacuum formulas. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0268_v1.md#argument) | Whole proof, including the single-noise test, scalar and centered deletion for noncommutative coefficients, arbitrary coarse tensors and recovery on the represented core. |
| [Finding](#finding) | [Free reference lifting](../../claims/Yin_C_F0212_v1.md#the-canonical-slices-on-the-base-and-its-free-extensions) | Extension of the old derivative to a free factor, its vacuum, oriented column bounds and full original domains. |
| [Finding](#finding) | [Bounded drift compression](../../claims/Yin_C_F0212_v1.md#compression-of-the-commutator-with-a-bounded-drift) | Prefix invariance and bounded strong approximation for the compression \(K_i e_R\). |
| [Finding](#finding) | [One-noise test](../../claims/Yin_C_F0212_v1.md#the-forced-one-noise-vacuum-component) | Endpoint traces, approximation of the drift, Riesz vector and the sign and adjoints in \(\Theta\). |
| [Finding](#finding) | [Terminal column estimate](../../claims/Yin_C_F0265_v1.md#a-global-square-integrable-kernel-estimate-for-mixed-columns) | Last-block formula and simultaneous centered estimate as used in the adaptation to noncommuting base coefficients. |
| [Finding](#finding) | [Free right-module identity](../../claims/Yin_C_F0045_v1.md#3-an-orthogonal-right-module-decomposition-of-the-full-core) | Right prefix orthogonality, appended-base isometry and the conditional expectation of the coefficient column square. |
| [Finding](#finding) | [Finite-family inequality](../../claims/Yin_C_F0045_v1.md#2-reuse-and-the-remaining-imported-functional-analytic-input) | Squared constant \(4/\pi\) for the centered slice from the abelian noise algebra into a Hilbert space. |
| [Finding](#finding) | [Scalar slice estimate](../../claims/Yin_C_F0055_v1.md#statement) | Actual scalar divided-difference vacuum gives the required operator-norm-to-Hilbert bound on the noise core. |
| [Finding](#finding) | [Forced phase and adjoint orientation](../../claims/Yin_C_F0076_v1.md#statement) | Identity of old derivatives on the base and actual normalized derivatives of the adjoint tuple. |
| [Finding](#finding) | [Two-contraction theorem](../../claims/Yin_C_F0072_v1.md#statement) | Original closed slice and actual adjoint have all bounded-vector domains after bounding both contractions. |
| [Finding](#finding) | [Normal strong-to-actual implication](../../claims/Yin_C_F0070_v1.md#statement) | Actual normalized derivations and their vacuum vectors on the represented target core. |
| [Finding](#finding) | [Canonical comparison](../../claims/Yin_C_F0075_v1.md#statement) | Part 4 identifies the original closures and their actual adjoints with the normalized strong witnesses on bounded vectors. |
| [Finding](#finding) | [Column cost](../../claims/Yin_C_F0208_v1.md#statement) | Normalization by the operator norm of the finite input column on each represented starred core. |

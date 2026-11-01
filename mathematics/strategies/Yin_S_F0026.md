---
author: Yin
---
# From ACSY vacua to full bounded-vector duals

## Task associations

| Task | Scope |
| --- | --- |
| [T_F0011 contract](../tasks/Yin_T_F0011_v1.md#contract) | Compare the normal analytic hypotheses S and A, and the general maximal-Delta hypotheses F and A, including actual canonical domains and existential quantifiers. |

## Route

| Field | Value |
| --- | --- |
| disposition | active |
| priority | Follow the authorized paired-quadratic route for A plus normality, with a*a on the left and aa* on the right. The remaining normal scope is arbitrary correlated coordinates. The general A-to-F comparison remains unresolved. |

Updated: 2026-10-18.
This route starts with the present Task and does not take over T_F0005's distinct obligations.

## Current question and exact reduction

Let X be a finite bounded generating tuple in a finite tracial von Neumann algebra.
The three hypotheses are exactly those of the linked Task: S requires dual and adjoint domains containing all M Omega, F requires only bare linear full-domain duals, and A requires represented starred Hilbert-valued derivations with actual vacuum adjoints.
They concern existence, not the behavior of one arbitrarily selected witness.

For normal tuples [C_F0075](../claims/Yin_C_F0075_v1.md#statement) proves S(X) iff F(X) and F(X*).
Since A is adjoint stable, the two universal normal implications A implies S and A implies F are equivalent.
A normal separating example for A versus S yields an A-but-not-F example at X or X*.
This does not assert the pointwise implication A(X) and F(X) implies S(X).

For arbitrary tuples [C_F0133](../claims/Yin_C_F0133_v1.md#statement) now excludes both S implies A and F implies A, even with bounded full-H duals.
The opposite implication A implies F is still unresolved.
Therefore the general comparison is not yet classified as a strict implication or incomparability.

The accepted [arcsine consequences](../claims/Yin_C_F0163_v1.md#statement), self-reviewed in [R_F0172](../audits/reviews/Yin_R_F0172_v1.md#whole-proof-finding), exclude ordinary duals and the proposed finite-rank liberation test in that example.
Both A and S fail there, so it does not separate the two normal hypotheses.
The [rank obstruction](../drafts/Yin_D_F0002.md#a-rank-obstruction-to-recovering-independent-selfadjoint-coordinates) rules out obtaining independent selfadjoint coordinates by inverting the normal phase matrix.
The [Die26 source boundary](../audits/literature/Die26/readme.md#normal-dual-domain-boundary) retains the additional assumptions in the almost-coassociative route; it supplies no unrestricted endpoint estimate.

## Inputs and remaining estimates

- [C_F0070](../claims/Yin_C_F0070_v1.md#statement) identifies normal A-to-F with the actual full-domain problem for the canonical right contraction and already proves normal S implies A.
- [C_F0072](../claims/Yin_C_F0072_v1.md#statement) turns two operator-norm-to-L2 contraction bounds into both actual canonical domains.
  No reality premise is needed once these bounds have been obtained.
- [C_F0075](../claims/Yin_C_F0075_v1.md#statement) compares every supplied strong normal system with the canonical system on M Omega and transfers finite-rank closures for each complete natural-domain fraction operator.
  Thus the operator-compatibility obligation is resolved under S; it is not inferred from A alone.
- [C_F0074](../claims/Yin_C_F0074_v1.md#statement) remains the distinct circular obstruction to removing normality from the specified fraction-commutator rationality criterion.
  It satisfies all three hypotheses and does not separate them.
- The accepted special classes and the independent normal F-to-A left-contraction reductions remain in [L_F0050 v5](../ledger/Yin_L_F0050_v5.md).
  They are inputs, not a general solution.

## Paired quadratic estimates and the remaining correlated scope

Write T_ell(a)=delta_i*(a tensor 1) and T_r(a)=delta_i*(1 tensor a) on the full represented starred polynomial core.
The current route seeks a finite constant for ||T_ell(a)||2 squared <= C_ell ||T_ell(a*a)||2 and separately ||T_r(a)||2 squared <= C_r ||T_r(aa*)||2.
The direct actual-adjoint power bound makes Hilbert-valued power iteration available once these inequalities are proved.
Both resulting slice bounds then give the original canonical domains through C_F0072 Part B.

The adopted [C_F0162](../claims/Yin_C_F0162_v1.md#decision-reviewed-quadratic) proves both inequalities with constant 2||xi_i||2 for every scalar normal actual-A law and for every freely independent normal tuple on its full mixed core.
Its scalar proof uses positive soft Cauchy energy, real polarization and cancellation before a strong-weak limit; the complex decomposition is confined to the scalar commutative algebra.
The adopted [C_F0160](../claims/Yin_C_F0160_v1.md#decision-reviewed-quadratic) lifts fixed-vector domination through free-product modules, preserving the left a*a and right aa* orders.
The resulting slice constants are 3||xi_i||2, with both original canonical domains and the generator-first dual relation.
The full review [R_F0171](../audits/reviews/Yin_R_F0171_v1.md#conclusion) covers the entire result, while [R_F0170](../audits/reviews/Yin_R_F0170_v1.md#scalar-conclusion) independently covers its scalar part.
The S conclusion for these classes was already available; the new contribution is the quadratic estimate and the stated constants.

For arbitrary correlated normal tuples, the adopted [C_F0158 v2](../claims/Yin_C_F0158_v2.md#decision-reviewed-quadratic) proves the coordinate estimate when the distinguished coordinate is selfadjoint or unitary.
In the unitary case it retains the defect as a positive residual square and gives constant ||2xi_i-X_i||2.
The adopted [C_F0159](../claims/Yin_C_F0159_v1.md#decision-reviewed-quadratic) gives the sharp constant ||xi||2 for rotational scalar laws, including radius atoms and accumulation at zero.
However, the adopted [C_F0161](../claims/Yin_C_F0161_v1.md#decision-reviewed-quadratic) gives a normal actual-A example supported on three displaced circles where this vacuum-norm constant fails.
Together with C_F0162, that example has an optimal constant strictly larger than ||xi||2 and at most 2||xi||2; it does not refute the existence of a finite constant or A implies S.

The unresolved target is the paired quadratic estimate for arbitrary correlated normal tuples with general normal coordinates.
Neither scalar real-imaginary decomposition nor the free-product direct-sum identity applies at that scope.
[D_F0002](../drafts/Yin_D_F0002.md#paired-quadratic-route-current-boundary) retains the mathematical continuation, and the Task's execution document owns its operational pause.
No Task completion follows from this round.

## Work branches and decision conditions

The normal branch has a directly ACSY-based proof of the actual joint tensor-leg phase domains and starred-core coassociativity in [C_F0076](../claims/Yin_C_F0076_v1.md#statement), independently reviewed in [R_F0049](../audits/reviews/Yin_R_F0049_v1.md#conclusion).
The subsequent reuse check located the main actual-domain mechanism already in [C_F0056](../claims/Yin_C_F0056_v1.md#statement) and [L_F0011](../ledger/Yin_L_F0011_v1.md); C_F0076 supplies an alternative proof and improves the regularized intermediate bound from 132 to 24, rather than first establishing the entire domain result.
[D_F0002](../drafts/Yin_D_F0002.md) retains this comparison and the unresolved energy interface.
The target is a uniform right-contraction bound on all mixed starred words for arbitrary correlated normal tuples.
[C_F0057](../claims/Yin_C_F0057_v1.md#statement) already excludes positivity or a lower bound determined only by marginal curvature.
The unweighted liberation estimate in [C_F0063 Appendix A](../claims/Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions) supplies an auxiliary bound but does not invert the singular phase multiplier.

The accepted [C_F0137](../claims/Yin_C_F0137_v1.md#statement), reviewed in [R_F0144](../audits/reviews/Yin_R_F0144_v1.md#conclusion), proves A(X) iff A(S) iff F(S) iff F(X) iff S(X) for arbitrarily correlated selfadjoint S and normal spectral graphs X_i=S_i+i g_i(S_i), with real C3 functions g_i.
Both canonical bounded-vector domains are included.
The Fourier and actual adjoint-graph transport allow nonanalytic graphs, but do not cover arbitrary two-dimensional normal spectra.
The accepted [C_F0140](../claims/Yin_C_F0140_v1.md#statement), reviewed in [R_F0147](../audits/reviews/Yin_R_F0147_v1.md#conclusion), covers a genuinely planar class: scalar actual-vacuum normal Z, a free standard semicircular S, positive regular h=f(Z) with real C1 planar f, and X=(Z,hSh).
Here A, F and S are equivalent to h inverse in L2, with actual canonical domains.
The free reference law is essential to the correction estimate; arbitrary correlated normal tuples remain open.

The accepted [C_F0077](../claims/Yin_C_F0077_v1.md#statement), reviewed in [R_F0050](../audits/reviews/Yin_R_F0050_v1.md#conclusion), proves the weighted partial-liberation contraction estimate when the real symmetric kernel has a uniform row-L2 bound and its actual weighted vacuum.
It also identifies the marginal polynomial-adjoint graph and the absolute continuity of the liberation-vacuum spectral measure.
This is not an absolute-continuity claim for every joint vector measure.

The accepted [C_F0078](../claims/Yin_C_F0078_v1.md#statement), reviewed in [R_F0051](../audits/reviews/Yin_R_F0051_v1.md#conclusion), now proves A iff S, and hence A implies F, for arbitrary correlated normal tuples whose marginals obey a uniform upper-growth bound of some exponent strictly greater than one.
Bounded planar densities are included.
A finite number of curvature-kernel compositions reaches the row-L2 theorem, and descending finite energy inequalities restores both original canonical domains even when the original curvature kernel is not coarse L2.
Its exact whole-domain and one-common/every-fraction comparison is included.
The growth hypothesis remains substantive; no bare-F converse is claimed.

D_F0002 retains the failed complex cross-energy identity: the Haar test excludes coercivity from it alone.
The accepted actual scalar-law obstruction [C_F0143](../claims/Yin_C_F0143_v1.md#statement), independently reviewed in [R_F0150](../audits/reviews/Yin_R_F0150_v1.md#conclusion), has finite curvature with divergent fourth kernel composition and a positive auxiliary contraction unbounded from the operator norm to L2, while the original normal canonical domains hold.
This excludes the absolute auxiliary-norm approach at full scope; the remaining correlated target is a lower bound for its negative quadratic part.
It is not a normal hypothesis-separation example.

The accepted [C_F0146](../claims/Yin_C_F0146_v1.md#statement), independently reviewed in [R_F0153](../audits/reviews/Yin_R_F0153_v1.md#conclusion), now refutes the proposed universal negative-form bound using only the actual square-root-weighted vacuum.
Its three-block free semicircular law has weighted vacuum norm squared 9t cubed/8, while a fixed normalized-corner analytic-unitary test has a negative form proportional to t squared.
This is a realized liberation example, not an abstract vector measure.
Its marginal is atomic and its edge weight is not a normal-coordinate curvature kernel.
The remaining normal route must therefore retain the full three-point phase/curvature coupling.
D_F0002 records the actual almost-everywhere phase-family graph reduction.
The accepted [C_F0149 v2](../claims/Yin_C_F0149_v2.md#statement), independently reviewed in [R_F0157](../audits/reviews/Yin_R_F0157_v1.md#conclusion), proves a uniform finite-model bound for every first-Wick vector and an exact operator formula on every relative Wick degree.
Its proof retains the full three-point coupling; the operator includes a degree-lowering correction.
The v1 vacuum-normalization comparison was removed in v2 and its finding remains in R_F0157.
This does not control arbitrary analytic unitaries or arbitrary correlated normal laws.
The continued three-block unitary cross-Gram identity and exact remaining estimates stay in D_F0002.

The arbitrary-tuple branch has excluded the free semicircular left-coordinate transformation as a separating class: [C_F0134](../claims/Yin_C_F0134_v1.md#statement), independently reviewed in [R_F0141](../audits/reviews/Yin_R_F0141_v1.md#conclusion), proves A(h,hS) iff F(h,hS) iff S(h,hS) iff h inverse belongs to L2, when h is positive regular with a scalar L2 conjugate and S is standard semicircular free from h.
It also restores both canonical bounded-vector domains.
The inverse need not be bounded.
No reverse-order bare-F equivalence is adopted.

The earlier correlated weighted obstruction is now resolved in its stated reference class.
[C_F0135](../claims/Yin_C_F0135_v1.md#statement), reviewed in [R_F0142](../audits/reviews/Yin_R_F0142_v1.md#conclusion), fixes the reduction under a Hilbert-space bounded canonical S-contraction.
[C_F0136](../claims/Yin_C_F0136_v1.md#statement), reviewed in [R_F0143](../audits/reviews/Yin_R_F0143_v1.md#conclusion), proves the affiliated kernel-weight estimate directly from the real coassociative energy identity.
Finally [C_F0138](../claims/Yin_C_F0138_v1.md#statement), reviewed in [R_F0145](../audits/reviews/Yin_R_F0145_v1.md#conclusion), removes the bounded-H premise: for any finite-Fisher selfadjoint reference pair with positive regular h, A(h,hS) iff S(h,hS) iff both h inverse and h inverse times xi_S belong to L2.
Its input and output estimates establish the actual product domains and both full-M target domains.
Each condition implies F; the reverse implication from F is not established at this broader scope.
No reverse-order bare-F equivalence is adopted.

The accepted [C_F0139](../claims/Yin_C_F0139_v1.md#statement), reviewed in [R_F0146](../audits/reviews/Yin_R_F0146_v1.md#conclusion), gives the finite kernel-tensor energy estimate, its abelian simultaneous-measure extension and both actual domains.
Its Sylvester example has A, F and S all true for (h,hS+i r Sh), 0<r<1, while all fail for (h,hS) with the same shifted semicircular h and free S.
This proves noninvariance under the indicated invertible real-linear coordinate change, not a separation of A and F.

The accepted [C_F0141](../claims/Yin_C_F0141_v1.md#statement), independently reviewed in [R_F0148](../audits/reviews/Yin_R_F0148_v1.md#conclusion), proves A-to-S for a selfadjoint finite-Fisher reference pair and a generating target (h,Y), Y=sum a_j(h)S b_j(h), with its polynomial coefficient nonzero in the coarse product measure.
A three-measure approximation on the target star core restores both given canonical contractions and their actual adjoints on M.
It does not require the inverse coefficient itself in coarse L2 or injectivity of the different multiplier on H.
This closes the polynomial-linear coordinate class under its explicit reference hypotheses; it is not a result for an arbitrary A-only reference tuple.

The accepted [C_F0142](../claims/Yin_C_F0142_v1.md#statement), reviewed in [R_F0149](../audits/reviews/Yin_R_F0149_v1.md#conclusion), resolves represented derivations for the genuinely nonlinear target Y=ShS+i hSh.
A target polynomial relation forces uniqueness among all coarse-affiliated derivations; a Cayley transform gives their actual bounded starred-generator values.
Thus existential A is equivalent to two precise actual-adjoint tests for one specified derivative, at 1 and at C*, where C is the reference h-derivative of Y.
For a general correlated reference pair those memberships remain unresolved.
A separate positive-S construction solves the weighted Hilbert-Schmidt equation, but neither unweights it nor constructs an arbitrary bare dual.

The accepted [C_F0144](../claims/Yin_C_F0144_v1.md#statement), reviewed in [R_F0151](../audits/reviews/Yin_R_F0151_v1.md#conclusion), verifies both actual-adjoint tests in the concrete free example h=2+s_0, S=c+s_1, c>6.
Here h inverse is not L2.
Relative Fock grading makes the inverse-coefficient series converge in both required adjoint graph norms, proving A.
The accepted [C_F0145](../claims/Yin_C_F0145_v1.md#statement), reviewed in [R_F0152](../audits/reviews/Yin_R_F0152_v1.md#conclusion), proves an H-to-L1 estimate for finite relative-degree kernels and its weighted-summable version.
Actual Riesz adjoint tests and the reverse-core identity then give both original canonical full-M domains.
Applied to that inverse series and the finite h correction, it proves A, S and F for this genuinely nonlinear singular example.
It does not require a projective inverse coefficient or settle arbitrary reference tuples.

The continuing [D_F0003](../drafts/Yin_D_F0003.md) owns the general actual-adjoint and all-bare-witness questions.
It also retains a bounded invertible coefficient with actual vacuum tests but an unbounded contraction, together with the proof that this bad coefficient cannot be an actual inverse Jacobian in the reference free algebra.
Thus a free choice of a bad coefficient does not supply an ACSY separating tuple.
[J_F0008](../computations/programs/Yin_J_F0008/readme.md) retains reproducible finite inverse diagnostics; its atomic matrix inputs are not actual ACSY examples.
The global projective-inverse shortcut is excluded by the corrected source scope in [LSW24b-U001](../audits/literature/LSW24b/Yin_U001.md#lsw24b-u001), without deciding the particular coefficient's projective invertibility.
Useful weaker graph methods and exact remaining integrability/range obligations stay in D.

The adversarial [D_F0004](../drafts/Yin_D_F0004.md) studies the negative weighted liberation form in an actual Haar/Poisson joint law.
Two explicit families of mixed unitary words have all-degree lower bounds controlled by the actual square-root vacuum; these remain development findings, not independently adopted Claims.
[J_F0009](../computations/programs/Yin_J_F0009/readme.md) retains exact finite Laurent-kernel controls and a narrow floating diagnostic, without replacing the actual tracial law by finite matrices or asserting a universal bound.

The accepted [C_F0147](../claims/Yin_C_F0147_v1.md#statement), independently reviewed in [R_F0154](../audits/reviews/Yin_R_F0154_v1.md#conclusion), gives a concrete alternative test: three free semicircular reference variables, h=2+s_0 and X=(hS_1,hS_2), in the target algebra N=W*(X).
It proves Delta_N(X)=2 while excluding each possible bare coordinate dual, using target row-kernel projection columns and the actual range obstruction 1 not in hL2 of the ambient algebra.
The target star algebra is algebraically free, yet no Hilbert-valued coordinate derivation can extend to the full reference polynomial algebra.
The accepted [C_F0148](../claims/Yin_C_F0148_v1.md#statement), independently reviewed in [R_F0155](../audits/reviews/Yin_R_F0155_v1.md#conclusion), now excludes each actual target ACSY coordinate witness.
It uses original-core approximations to normalized target resolvents and weak convergence of the arbitrary starred-value tensor tests, without extending a derivation to the reference variables.
Thus this tuple has maximal Delta while A and F both fail; it does not separate A from F.
More generally, for at least two coordinates, full A forces the inverse of sum_j X_j X_j* to have finite trace and every bounded vector to lie in the actual Hilbert row range.
The remaining general problem must therefore go beyond this finite-row nonrange obstruction.

D_F0003 also retains the exact algebraic Ext-one splitting formulation and the simpler arcsine falsification of Delta implying F.
A free-algebra resolution of length one does not force Ext-one to vanish, and algebraic-dual-valued extensions do not provide Hilbert-valued maps.
The natural right-annihilation construction is valid on the holomorphic core but fails already at a starred generator.
A separate necessary system from actual ACSY bounded regularizations is retained without assuming Hilbert control of their commutators with the hidden reference h.

The accepted [C_F0150](../claims/Yin_C_F0150_v1.md#statement), independently reviewed in [R_F0156](../audits/reviews/Yin_R_F0156_v1.md#conclusion), gives a new one-coordinate test X=hS, h=2+s_0, in N=W*(X).
The oriented separated-leg coefficient space is contained isometrically in both actual reference adjoint domains.
The two coefficients alpha(u,v)=v/(u squared+v squared) and beta(u,v)=u/(u squared+v squared) solve the normalized product equation and have total squared Hilbert norm at most one.
Their whole-core vacuum, followed by intrinsic tensor and vacuum compression, proves A(N;X), despite h inverse not being L2.
The accepted [C_F0152](../claims/Yin_C_F0152_v1.md#statement), independently reviewed in [R_F0160](../audits/reviews/Yin_R_F0160_v1.md#conclusion), now constructs an intrinsic bare full-domain dual for this target and places all bounded target vectors in the original canonical forward closure.
Complete-terminal-block cancellation and a partial-block column/concatenation estimate give the explicit bound sqrt(2)+1+2||beta||2.
No full adjoint domain is asserted; this tuple satisfies A and F and does not separate them.
[C_F0151 v2](../claims/Yin_C_F0151_v2.md#statement) fixes an automatic-continuity argument for every hypothetical bare dual at this nonnormal factorization, followed by an exact projective-tensor functional criterion.
The general theorem and criterion are independently checked in [R_F0158](../audits/reviews/Yin_R_F0158_v1.md#independent-conclusion), and the repaired application is independently checked in [R_F0159](../audits/reviews/Yin_R_F0159_v1.md#application-conclusion).
Its selected decision adopts their complementary scopes.
The full A-to-F comparison itself remains unresolved.
The exact projective functional for this example is consequently bounded.
D_F0003 now returns to arbitrary affine/polynomial matrix relations and their actual weighted range obligations; these are distinct from the settled example.
D_F0005 retains its separate scalar Cauchy mechanism as a developer-checked diagnostic, with the positive full-domain resolution linked.

The accepted [C_F0153](../claims/Yin_C_F0153_v1.md#statement), independently reviewed in [R_F0161](../audits/reviews/Yin_R_F0161_v1.md#conclusion), proves both original canonical domains for a normal Gaussian pair (Z,T) obtained from a free semicircular by positive symmetric coefficients on finitely many separated spectral blocks of Z.
Its arbitrary-abelian-base relative-degree lemma controls the correction by its actual vacuum uniformly in block sizes, masses and coefficient ratios, and yields the full analytic-unitary lower form.
The finite atomic formal vacuum remains distinct from an actual normal conjugate vector.
The accepted [C_F0156](../claims/Yin_C_F0156_v1.md#statement), independently reviewed in [R_F0164](../audits/reviews/Yin_R_F0164_v1.md#conclusion), extends the result to every bounded positive symmetric measurable Gaussian kernel under actual target A.
Quadratic and linear target tests force the degree-two correction and reciprocal coefficient in L2.
Soft-Cauchy adjoints on algebraic tests, followed by actual full-adjoint matrix elements, identify both original target canonical domains without assuming maximal/minimal derivative-domain equality.
The accepted [C_F0157](../claims/Yin_C_F0157_v1.md#statement), independently reviewed in [R_F0165](../audits/reviews/Yin_R_F0165_v1.md#conclusion), gives the exact bounded measurable Hermitian Gaussian criterion: A iff S iff the scalar actual vacuum exists and both the reciprocal modulus and its three-variable ratio difference are L2.
Actual target linear tests exclude zero sets; an explicit trace-preserving phase automorphism handles complex Hermitian kernels.
This implies F but gives no bare-F converse.
Under these equivalent conditions the already accepted C_F0075 comparison applies to the specified canonical operators and each fraction pair.
D_F0002 retains the unique phase and lower-form diagnostics for the unrestricted correlated-normal question, which remains open.
Its later developer-checked [colored-adjoint calculation](../drafts/Yin_D_F0002.md#the-actual-colored-adjoint-reverses-the-second-matrix-index) corrects a proposed matrix cancellation route: the actual real positive-matrix vacuum uses R minus its inverse transpose, so the constant-one coefficient estimate survives.
The untransposed counterexample is retained only as an inapplicable surrogate.
Actual multicoordinate moment extraction, generation and original domain passage remain separate obligations.

The accepted [C_F0154](../claims/Yin_C_F0154_v1.md#statement), independently reviewed in [R_F0162](../audits/reviews/Yin_R_F0162_v1.md#conclusion), proves inverse-trace integrability and an actual Hilbert right inverse on bounded columns for an affine matrix pencil with regular LL* and strictly positive scalar kernel compression.
The accepted [C_F0155](../claims/Yin_C_F0155_v1.md#statement), independently reviewed in [R_F0163](../audits/reviews/Yin_R_F0163_v1.md#conclusion), removes the scalar-null blocks relevant to a relation, proves regularity of the surviving block through rectangular finite-rank cycles, and transfers through a bounded polynomial linearization.
Consequently every bounded relation Pa=0 for a holomorphic polynomial matrix has a Hilbert solution Pz=-(id tensor tau)((delta_i P) dot a), with a bounded linear choice for each fixed P,i.
This removes all such finite range obstructions.
Choices and bounds still depend on P; constructing one coherent dual on all M remains open.
D_F0003 owns the remaining finite-to-global interface.
It constructs a finite-rank Hilbert operator satisfying every prescribed finite collection of commutator tests exactly.
Its developer-checked [pointwise-radius criterion](../drafts/Yin_D_F0003.md#an-exact-pointwise-radius-criterion-for-bare-full-domain-duals) now identifies the exact additional requirement for bare F: choose finite radii for each input before the finite sets are selected, with one feasible family satisfying all their radius constraints simultaneously.
A product of weak compact Hilbert balls then supplies a coherent global map; conversely any bare dual supplies those radii.
A uniform operator-norm-to-H bound is only a stronger sufficient specialization.
The equivalent [affine support estimate](../drafts/Yin_D_F0003.md#an-equivalent-estimate-on-every-affine-relation) expresses the exact requirement as abs(<eta,A_i tau(a)>) <= sum_l r_i(a_l) norm((L*eta)_l) for every bounded affine relation La=0, with radii chosen before all relations and r_i(1)=0.
The product-ball image and nearest-point argument prove equivalence with bare F at developer-checked scope.
Actual ACSY data have not yet supplied these common coordinate radii or the equivalent estimate.
Its subsequent estimates show why neither a fixed elementary approximation of the starred derivative tensors nor a uniform weighted inverse-trace bound closes this gap: the latter sufficient bound diverges in an explicit scalar finite-Fisher example although the true forced solutions remain controlled.
The next estimate must retain the actual bounded-kernel-column forcing set rather than replace it by that coarse trace bound.

These branches share the A-to-F question but have different structural inputs.
A proof for arbitrary tuples would settle the normal applicability comparison as well.
A nonnormal counterexample would settle only the general classification; the normal branch would remain necessary.

## Evidence and decisions

On 2026-10-15 the bounded-similarity construction was fixed in C_F0133 and independently reviewed in [R_F0140](../audits/reviews/Yin_R_F0140_v1.md#conclusion).
This resolves the general F-to-A direction negatively and focuses further comparison on the reverse direction.
The complete normal adjoint-tuple reduction and canonical compatibility were fixed in C_F0075 and independently reviewed in [R_F0048](../audits/reviews/Yin_R_F0048_v1.md#conclusion).
Both were adopted by their responsible Claim decisions.

The later results C_F0076 and C_F0134 give the direct phase-domain proof and the free singular-coordinate test class, with the prior-domain provenance correction stated above.
C_F0135-C_F0141 fix and independently review the weighted reduction and energy mechanisms, the C3 graph class, the stronger correlated singular-coordinate theorem, the nonnormal Sylvester example, the normal free congruence class and the polynomial-linear target-core theorem.
C_F0077-C_F0143 add the row-kernel theorem, the correlated normal upper-growth class, the exact nonlinear actual-adjoint reduction and the realized scalar obstruction to absolute curvature estimates.
C_F0144-C_F0145 add the actual nonlinear free vacua and the relative-degree theorem restoring both specified target canonical domains.
C_F0146 excludes a further arbitrary-weight lower-form method by a realized tracial counterexample.
C_F0147 separates maximal Delta from every bare full-domain dual.
C_F0148 resolves its target-A question negatively and supplies the general actual inverse-row-square necessary condition.
C_F0149 v2 adds a finite-model curvature bound and exact Wick action.
C_F0150 gives an actual A-positive single hidden-factor candidate, while C_F0151 v2 makes its all-bare-dual question an exact bounded-functional test.
C_F0152 constructs the required bare dual and original canonical forward domain for that candidate.
C_F0153 proves the finite normal Gaussian correction theorem; C_F0154-C_F0155 give actual matrix inverse estimates and every finite polynomial relation compatibility.
C_F0156-C_F0157 restore the original domains for measurable Gaussian kernels and give the exact Hermitian class criterion.
The unrestricted implication remains open.
Their selected Claim decisions own acceptance.
The continuing D materials retain the further constructions and useful failures at their stated development scope; none of these results supplies a completion decision for this Task.

The Task remains active.
Completion requires a full-scope theorem or an existential separating example in each outstanding direction, plus the exact comparison of applicability and operator realizations; progress on a method does not satisfy that contract.

The explicit normal-endpoint continuation is retained in [D_F0006](../drafts/Yin_D_F0006.md#selfadjoint-tests-and-the-correlated-unitary-obstruction).
It reduces a sufficient universal quadratic theorem to positive core inputs and excludes the sharp scalar fixed-vacuum domination even on a strictly positive mixed test in an actual correlated-unitary model.
The same model's all-degree adjoint norms remain bounded for each fixed law.
The finite normal-coordinate-change tests in J_F0009 are diagnostic only and provide neither the unrestricted endpoint estimate nor an actual domain counterexample.

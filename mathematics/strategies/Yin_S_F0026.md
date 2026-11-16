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
| priority | Bound both oriented cutoff norms on a neighborhood of each single marginal point for tuples of length at least three, or construct an actual normal pair with divergent cubic concentration. |

Updated: 2026-11-16.
This route starts with the present Task and does not take over T_F0005's distinct obligations.

## Current question and exact reduction

Let X be a finite bounded generating tuple in a finite tracial von Neumann algebra.
The three hypotheses are exactly those of the linked Task: S requires dual and adjoint domains containing all M Omega, F requires only bare linear full-domain duals, and A requires represented starred Hilbert-valued derivations with actual vacuum adjoints.
They concern existence, not the behavior of one arbitrarily selected witness.

For normal tuples [C_F0075](../claims/Yin_C_F0075_v1.md#statement) proves S(X) iff F(X) and F(X*).
Since A is adjoint stable, the two universal normal implications A implies S and A implies F are equivalent.
A normal separating example for A versus S yields an A-but-not-F example at X or X*.
This does not assert the pointwise implication A(X) and F(X) implies S(X).

For arbitrary tuples the applicability classes of the two maximal-Delta criteria are incomparable.
The [two-point modulus](../claims/Yin_C_F0225_v1.md#decision-reviewed) has a uniformly bounded actual vacuum as its small singular value tends to zero, while the corresponding left and right singular projections force the bounded-dual cost to diverge.
Countable assembly and free semicircular enlargement give a single two-coordinate example with actual ACSY and no algebraic full-domain dual system.
In the opposite direction the [similarity example](../claims/Yin_C_F0133_v1.md#statement) and the [weighted ergodic factor](../claims/Yin_C_F0219_v1.md#decision-reviewed) have whole-Hilbert-space duals and fail actual ACSY.
Thus A and S are also incomparable at this generality.
On the A-only example the [ACSY criterion](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) gives maximal Delta, and on the F-only example the [bare-dual criterion](../claims/Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors) gives it.
The [common-factor example](../claims/Yin_C_F0148_v1.md#statement) also permits maximal Delta when both hypotheses fail.

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
[D_F0002](../drafts/Yin_D_F0002.md#paired-quadratic-route-current-boundary) retains the paired quadratic route.
The [spectral cut criterion](../drafts/Yin_D_F0006.md#spectral-cuts-for-the-two-contraction-bounds) identifies the optimal positive-core bound on each leg with a supremum of spectral cut pairings.
The remaining estimate must control all unit test vectors on both legs for a fixed correlated tuple.
On the signed-curvature route, the [angular calculation](../drafts/Yin_D_F0002.md#angular-modes-of-the-three-point-curvature-form) gives negative directions at a set of third points of positive measure even for an actual scalar conjugate variable.
The test on arbitrary endpoint vectors omits constraints satisfied by the three vertices of an actual mixed unitary.
Equations (P14) and (P15) retain those constraints and give a finite positive-semidefinite sufficient condition whose uniform validity remains open.
The [positive-mixture estimate and three-circle example](../drafts/Yin_D_F0002.md#positive-mixtures-of-spectral-projection-blocks) extend the projection-block bound to an integral of such blocks and exhibit a scalar ACSY curvature kernel that has no exact representation of that kind.

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
Version 1 bounds both original canonical domains by a finite descent from the row-L2 estimate and specifies the whole-domain and one-common/every-fraction comparison.

A weaker marginal criterion now follows from [C_F0078 v2](../claims/Yin_C_F0078_v2.md#decision-reviewed), independently checked in [R_F0207](../audits/reviews/Yin_R_F0207_v1.md#curvature-row-criterion).
Bounding the row integral of the curvature kernel and the product of that kernel with the endpoint distance suffices, even when no finite composition has a known uniform square-integrable row.
The dyadic square sum of the maximal marginal ball densities implies both bounds and includes logarithmic decay with exponent greater than one half.
A [correlated shrinking-circle example](../drafts/Yin_D_F0006.md#a-sharp-threshold-on-a-fixed-singular-marginal) tests the spectral cut bounds beyond the uniform curvature-row class by computing the exact second-chaos correction in the measurable Gaussian criterion.

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
The accepted [C_F0149 v2](../claims/Yin_C_F0149_v2.md#statement), checked in [R_F0157's whole-proof finding](../audits/reviews/Yin_R_F0157_v1.md#conclusion) with an unknown initial-context relationship, proves a uniform finite-model bound for every first-Wick vector and an exact operator formula on every relative Wick degree.
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

The [general-branch draft](../drafts/Yin_D_F0003.md) retains other model-specific actual-adjoint and all-witness tests.
It also retains a bounded invertible coefficient with actual vacuum tests but an unbounded contraction, together with the proof that this bad coefficient cannot be an actual inverse Jacobian in the reference free algebra.
Thus a free choice of a bad coefficient does not supply an ACSY separating tuple.
[J_F0008](../computations/programs/Yin_J_F0008/readme.md) retains reproducible finite inverse diagnostics; its atomic matrix inputs are not actual ACSY examples.
The global projective-inverse shortcut is excluded by the corrected source scope in [LSW24b-U001](../audits/literature/LSW24b/Yin_U001.md#lsw24b-u001), without deciding the particular coefficient's projective invertibility.
Useful weaker graph methods and exact remaining integrability/range obligations stay in D.

The adversarial [D_F0004](../drafts/Yin_D_F0004.md) studies the negative weighted liberation form in an actual Haar/Poisson joint law.
[L_F0056](../ledger/Yin_L_F0056_v1.md#uniform-bounds-for-two-mixed-word-families) retains the completed all-degree lower bounds for two explicit mixed-word families, controlled by the actual square-root vacuum; these remain development findings, not independently adopted Claims.
[J_F0009](../computations/programs/Yin_J_F0009/readme.md) retains exact finite Laurent-kernel controls and a narrow floating diagnostic, without replacing the actual tracial law by finite matrices or asserting a universal bound.

The accepted [C_F0147](../claims/Yin_C_F0147_v1.md#statement), independently reviewed in [R_F0154](../audits/reviews/Yin_R_F0154_v1.md#conclusion), gives a concrete alternative test: three free semicircular reference variables, h=2+s_0 and X=(hS_1,hS_2), in the target algebra N=W*(X).
It proves Delta_N(X)=2 while excluding each possible bare coordinate dual, using target row-kernel projection columns and the actual range obstruction 1 not in hL2 of the ambient algebra.
The target star algebra is algebraically free, yet no Hilbert-valued coordinate derivation can extend to the full reference polynomial algebra.
The accepted [C_F0148](../claims/Yin_C_F0148_v1.md#statement), with its complete self-review in [R_F0155](../audits/reviews/Yin_R_F0155_v1.md#conclusion), now excludes each actual target ACSY coordinate witness.
It uses original-core approximations to normalized target resolvents and weak convergence of the arbitrary starred-value tensor tests, without extending a derivation to the reference variables.
Thus this tuple has maximal Delta while A and F both fail; it does not separate A from F.
More generally, for at least two coordinates, full A forces the inverse of sum_j X_j X_j* to have finite trace and every bounded vector to lie in the actual Hilbert row range.
The two-point-modulus construction uses a singular-value lower bound along a sequence of laws.

D_F0003 also retains the exact algebraic Ext-one splitting formulation and the simpler arcsine falsification of Delta implying F.
A free-algebra resolution of length one does not force Ext-one to vanish, and algebraic-dual-valued extensions do not provide Hilbert-valued maps.
The natural right-annihilation construction is valid on the holomorphic core but fails already at a starred generator.
A separate necessary system from actual ACSY bounded regularizations is retained without assuming Hilbert control of their commutators with the hidden reference h.

The accepted [C_F0150](../claims/Yin_C_F0150_v1.md#statement), independently reviewed in [R_F0156](../audits/reviews/Yin_R_F0156_v1.md#conclusion), gives a new one-coordinate test X=hS, h=2+s_0, in N=W*(X).
The oriented separated-leg coefficient space is contained isometrically in both actual reference adjoint domains.
The two coefficients alpha(u,v)=v/(u squared+v squared) and beta(u,v)=u/(u squared+v squared) solve the normalized product equation and have total squared Hilbert norm at most one.
Their whole-core vacuum, followed by intrinsic tensor and vacuum compression, proves A(N;X), despite h inverse not being L2.
The accepted [C_F0152](../claims/Yin_C_F0152_v1.md#statement), checked in the self-reviewed [R_F0160 finding](../audits/reviews/Yin_R_F0160_v1.md#conclusion), now constructs an intrinsic bare full-domain dual for this target and places all bounded target vectors in the original canonical forward closure.
Complete-terminal-block cancellation and a partial-block column/concatenation estimate give the explicit bound sqrt(2)+1+2||beta||2.
No full adjoint domain is asserted; this tuple satisfies A and F and does not separate them.
[C_F0151 v2](../claims/Yin_C_F0151_v2.md#statement) fixes an automatic-continuity argument for every hypothetical bare dual at this nonnormal factorization, followed by an exact projective-tensor functional criterion.
The general theorem and criterion are independently checked in [R_F0158](../audits/reviews/Yin_R_F0158_v1.md#independent-conclusion), and the repaired application is independently checked in [R_F0159](../audits/reviews/Yin_R_F0159_v1.md#application-conclusion).
Its selected decision adopts their complementary scopes.
The general counterexample above uses a different family.
The exact projective functional for this example is consequently bounded.
D_F0003 now returns to arbitrary affine/polynomial matrix relations and their actual weighted range obligations; these are distinct from the settled example.
D_F0005 retains its separate scalar Cauchy mechanism as a developer-checked diagnostic, with the positive full-domain resolution linked.

The accepted [C_F0153](../claims/Yin_C_F0153_v1.md#statement), checked in [R_F0161's whole-proof finding](../audits/reviews/Yin_R_F0161_v1.md#conclusion) with an unknown initial-context relationship, proves both original canonical domains for a normal Gaussian pair (Z,T) obtained from a free semicircular by positive symmetric coefficients on finitely many separated spectral blocks of Z.
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
The accepted [C_F0155](../claims/Yin_C_F0155_v1.md#statement), checked in [R_F0163's whole-proof finding](../audits/reviews/Yin_R_F0163_v1.md#conclusion) with an unknown initial-context relationship, removes the scalar-null blocks relevant to a relation, proves regularity of the surviving block through rectangular finite-rank cycles, and transfers through a bounded polynomial linearization.
Consequently every bounded relation Pa=0 for a holomorphic polynomial matrix has a Hilbert solution Pz=-(id tensor tau)((delta_i P) dot a), with a bounded linear choice for each fixed P,i.
This removes all such finite range obstructions.
Choices and bounds still depend on P; constructing one coherent dual on all M remains open.
D_F0003 owns the remaining finite-to-global interface.
[C_F0200](../claims/Yin_C_F0200_v1.md#decision-reviewed), independently checked in [R_F0208](../audits/reviews/Yin_R_F0208_v1.md#whole-proof-finding), gives one normalized dual on the holomorphic module generated by any prescribed countable set of bounded inputs and the unit.
Stabilization of closed restriction images permits a summably convergent choice on each countable chain.
The same algebraic local solvability holds for the diffuse arcsine law, where every normalized solution maps the norm-one Chebyshev polynomial of degree n to a vector of Hilbert norm equal to the square root of n.
The arcsine law has neither a global bare dual nor an actual conjugate variable.
D_F0003 also constructs a finite-rank Hilbert operator satisfying every prescribed finite collection of commutator tests exactly.
Its developer-checked [pointwise-radius criterion](../drafts/Yin_D_F0003.md#an-exact-pointwise-radius-criterion-for-bare-full-domain-duals) now identifies the exact additional requirement for bare F: choose finite radii for each input before the finite sets are selected, with one feasible family satisfying all their radius constraints simultaneously.
A product of weak compact Hilbert balls then supplies a coherent global map; conversely any bare dual supplies those radii.
A uniform operator-norm-to-H bound is only a stronger sufficient specialization.
The equivalent [affine support estimate](../drafts/Yin_D_F0003.md#an-equivalent-estimate-on-every-affine-relation) expresses the exact requirement as abs(<eta,A_i tau(a)>) <= sum_l r_i(a_l) norm((L*eta)_l) for every bounded affine relation La=0, with radii chosen before all relations and r_i(1)=0.
The product-ball image and nearest-point argument prove equivalence with bare F at developer-checked scope.
Actual ACSY data have not yet supplied these common coordinate radii or the equivalent estimate.
Its subsequent estimates show why neither a fixed elementary approximation of the starred derivative tensors nor a uniform weighted inverse-trace bound closes this gap: the latter sufficient bound diverges in an explicit scalar finite-Fisher example although the true forced solutions remain controlled.
The next estimate must retain the actual bounded-kernel-column forcing set rather than replace it by that coarse trace bound.

[C_F0201](../claims/Yin_C_F0201_v1.md#decision-reviewed), independently checked in [R_F0209](../audits/reviews/Yin_R_F0209_v1.md#whole-proof-finding), gives two optimal finite-word tests on the same joint star law.
The first gives the least joint Hilbert norm of an actual vacuum and of the starred-generator derivatives, with descent through every represented relation.
The second converges to the least operator-norm-to-H norm of a full-domain witness, allowing its value on the unit to vary.
For arbitrary correlated normal tuples, the remaining comparison is whether finite limits in the first test bound the second test in degree for the tuple and its adjoint.
For tuples with a nonconstant normal affine combination, boundedness of the second test already characterizes bare F.
Outside classes with automatic continuity, unboundedness of the second test alone cannot exclude every algebraic full-domain witness.

For the unrestricted implication across all tuple lengths, the [semicircular extension theorem](../claims/Yin_C_F0205_v1.md#decision-reviewed) removes this obstacle.
Adjoining one freely independent standard semicircular coordinate preserves every old ACSY cost and can only increase the old optimal bounded-dual costs.
If a tuple with actual conjugate variables has an infinite bounded-dual cost, its free extension is an existential counterexample to bare full-domain duality.
The universal positive direction is therefore equivalent to bounding the second test in degree on every law where the first test is finite in all coordinates.
The [countable assembly theorem](../claims/Yin_C_F0210_v1.md#decision-reviewed) reduces a sufficient counterexample search to a sequence of single generators: an unbounded ratio of optimal dual cost to actual conjugate-vector norm gives a single ACSY generator with infinite cost, and then an actual two-coordinate separator.
This criterion works at arbitrary finite cutoffs without a uniform bound on the derivative of the adjoint generator.
The [mixed circular blocks](../claims/Yin_C_F0207_v1.md#decision-reviewed) show why the squared Hilbert–Schmidt norms of individual forced blocks cannot replace dual costs in this search.
The [resolvent and word tests](../drafts/Yin_D_F0003.md#resolvent-tests-for-the-one-generator-norm-ratio) give lower bounds to compare with the norm of a particular actual vacuum.

The [common similarity theorem](../claims/Yin_C_F0203_v1.md#decision-reviewed) proves the positive direction for tuples jointly similar through a bounded invertible element to a selfadjoint tuple.
For a single generator whose nonconstant holomorphic polynomial is central, [C_F0204](../claims/Yin_C_F0204_v1.md#decision-reviewed) already forces normality under ACSY, and hence full-domain duality by the scalar result.
The [type I summand theorem](../claims/Yin_C_F0216_v1.md#decision-reviewed) gives the single-generator implication from ACSY to strong duality in every finite type I algebra.
Its proof forces the type I central part to be diffuse abelian even when a type II part is present.
Together with the [two-by-two similarity counterexample](../claims/Yin_C_F0133_v1.md#decision-reviewed), this gives strict implication from ACSY to bare duality within the class of single generators in finite type I algebras.
The [size-two pole calculation](../claims/Yin_C_F0215_v1.md#decision-reviewed) also forces normality from just a represented normalized derivation and injectivity of every scalar shift, and gives a third-order lower bound on the Jordan fibers.
For two or more coordinates C_F0216 excludes every type I central summand under ACSY.
Bare full-domain duals also exclude such a summand at these lengths: their [maximal Delta](../claims/Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors) makes every nonzero holomorphic polynomial [affiliated-invertible](../audits/literature/MSY23/Yin_U001.md#msy23-u001), whereas the nonzero polynomial constructed in [the multi-coordinate argument](../claims/Yin_C_F0216_v1.md#two-or-more-coordinates) vanishes on a positive homogeneous matrix summand.
For two central summands, [C_F0206](../claims/Yin_C_F0206_v1.md#decision-reviewed) assembles both dual conditions from the corners whenever their separating projection belongs to the coordinate derivation domains.
Two spectrally disjoint translated circular variables furnish a nonfactor single-generator law with all three conditions.
The [Gaussian kernel theorem](../claims/Yin_C_F0157_v2.md#decision-reviewed) covers every bounded Hermitian first-chaos coordinate paired with its diffuse normal base, including unbounded kernels whose amplitude truncations stay a positive distance away in operator norm.
The [matrix criterion](../claims/Yin_C_F0209_v1.md#decision-reviewed) gives the corresponding intrinsic equivalence for finitely many bounded selfadjoint Gaussian fields with measurable rectangular coefficients over that base.
For one field with a [bounded measurable drift and variable covariance](../claims/Yin_C_F0260_v1.md#decision-reviewed), the additional condition is square integrability of the drift divided difference divided by the Gaussian amplitude.
Its squared norm gives the exact additional contribution to the base vacuum, and the criterion yields the original full domains in both orientations.
For the unrestricted normal question the [two-Haar extension](../claims/Yin_C_F0208_v1.md#decision-reviewed) makes the universal implication equivalent to a single-state estimate on polynomial columns at each coordinate.
An unbounded column cost on one fixed normal ACSY tuple would yield a normal separating tuple after adjoining the two unitaries.
The [weighted commutator characterization](../claims/Yin_C_F0211_v1.md#decision-reviewed) shows that every optimal column state has a normal density with integrable inverse.
It gives a necessary packing bound for orthogonal small-singular-value projections of differences between the distinguished coordinate and elements generated by the other coordinates.
For [one fixed correlated pair with a standard semicircular coordinate](../claims/Yin_C_F0259_v1.md#decision-reviewed), every density in that marginal algebra fails to dominate even single mixed polynomials, although a density in the generated algebra does give domination.
For a [symmetric Markov covariance density](../claims/Yin_C_F0262_v1.md#decision-reviewed), such marginal domination is equivalent to uniform boundedness of the integrals of its reciprocal on the rows.
The [explicit full-algebra density](../claims/Yin_C_F0263_v1.md#decision-reviewed) combines the square of the field vacuum with its conditional expectation on the base.
On the fixed two-disk pair it works in every \(L^s,\ 1\le s<4\), while no \(L^4\) density or convex mixture of the two marginals' densities suffices.
The [weak fourth-moment calculation](../drafts/Yin_D_F0006.md#weak-fourth-moment-gaussian-density) estimates the spectral tail of this density and extends the obstruction to products of weights from the two marginals.
The [separated-interval law](../claims/Yin_C_F0264_v1.md#decision-reviewed) forces arbitrarily large dominating densities where the real vacuum stays bounded.
After freely adjoining a semicircular coordinate, positive quadratic forms in the two vacua and their iterated marginal expectations still fail on the original scalar tests.
At a [selfadjoint distinguished coordinate](../claims/Yin_C_F0266_v1.md#decision-reviewed), the canonical adjoint on the core acts isometrically on inputs weighted by a unique normal density.
Its compression to the distinguished marginal equals the conditional variance of the joint vacuum plus the squared modulus of the boundary Cauchy transform.
For a single real generator, domination of that last scalar weight characterizes all densities that work on the entire core.
For a [general normal coordinate](../claims/Yin_C_F0271_v1.md#decision-reviewed), two marginal tests detect whether such an exact isometric density exists on the mixed core: their defects vanish together exactly for affine-line support.
The marginal projection of every mixed output has a column estimate, and two-sided comparability of the two-block law extends the estimate to the closed span of products of an omitted coefficient followed by a marginal one.
The [fixed-tuple single-input estimate](../claims/Yin_C_F0276_v1.md#decision-reviewed) gives \(a_i\le c_i\le\sqrt2\,a_i\) for three or more coordinates, where \(a_i\) measures the slice on individual contractions and \(c_i\) measures all finite columns.
In this dimension a divergent column or cubic concentration integral rules out bare full-domain duals on the original tuple.
At every dimension the [fixed-trace cutoff test](../claims/Yin_C_F0282_v1.md#decision-reviewed) reduces forward domain inclusion to pointwise boundedness on a nonmeagre family of projections of one prescribed trace, for example \(1/2\), using any sequence of cutoff radii tending to zero.
Failure omits a dense \(G_\delta\) of the same projections from the original domain and makes their regularized outputs unbounded along that sequence.
On an original tuple of at least two coordinates, [negative spectral projections of polynomial congruences](../claims/Yin_C_F0288_v1.md#decision-reviewed) give a countable dense family of any prescribed trace on which both limiting slice values exist.
Uniform boundedness on this family suffices, although the unsliced derivatives are unbounded in every open patch.
The [localization theorem](../claims/Yin_C_F0295_v1.md#statement) permits a different test on the original algebra.
For each fixed tuple and orientation it suffices to bound the forward norms along each sequence of good spectral cuts on disjoint annuli shrinking to at most two marginal points, allowing the bound to depend on the sequence.
Indeed, failure produces one such sequence with forward norms tending to infinity, while a finite slice norm bounds every sequence.
If the forward domain contains \(M\Omega\), averaging the squared norm of the slice of an independently signed sum of orthogonal projections bounds the sum of their squared slice norms by the squared single-input norm, since each signed sum is a contraction.
The missing implication is to control these disjoint tests using the actual joint vacuum.
For the universal implication the [one-point corner criterion](../claims/Yin_C_F0299_v1.md#statement) permits testing just one marginal point at a time, since a pair can be enlarged by a free Haar unitary.
Local control at every point on the original pair itself gives an unconditional weighted estimate, with weight determined by its liberation vacuum.
The [spectral corner formula](../claims/Yin_C_F0301_v1.md#statement) identifies the cutoff test on any Borel spectral set of positive mass with a relative single-input slice in the corner.
At a putative bad point, every neighborhood has infinite relative cost even though \(t^3\|\xi^e\|_{2,\tau_e}^2\) tends to zero with its marginal mass \(t\).
The next local estimate must use how the relative slice acts on mixed inputs in that same corner; small weighted vacuum energy alone supplies no bound in the calculation.
After freely adjoining a Haar unitary, the [unitary orbit of one fixed projection](../claims/Yin_C_F0289_v1.md#decision-reviewed) gives the exact original single-input norm up to the factor \(\sqrt{t(1-t)}\), where \(t\) is the projection trace.
For a fixed selfadjoint mixed polynomial, its [spectral projections](../claims/Yin_C_F0285_v1.md#decision-reviewed) belong to both canonical domains and their cutoffs converge in norm outside a set of thresholds of Hausdorff dimension at most \(2/3\).
The exceptional dimension is sharp for the sufficient integral estimate, and the good thresholds need not cut a prescribed trace.
Finite sums of [alternating matrix products](../claims/Yin_C_F0284_v1.md#decision-reviewed) admit column estimates in terms of their factor norms and the number of distinguished marginal factors.
Even for a free Haar pair the half-circle projection of the product of its generators admits no bounded strong-star approximation of uniformly bounded cost of this form.
For two coordinates a bounded slice is an operator-norm limit of finite-column maps supported away from progressively smaller left projections.
The [alternating conditional-expectation estimate](../claims/Yin_C_F0280_v1.md#decision-reviewed) gives the entire column bound from \(a_i<\infty\) if a finite iterate makes the row density bounded.
When both marginals are maximal abelian, this condition can be tested on their conditional spectral densities, uniformly over input word length.
For all dimensions [one freely adjoined scalar normal coordinate](../claims/Yin_C_F0278_v1.md#decision-reviewed) with a scalar conjugate variable suffices to detect an infinite original column cost.
The [ordered product density](../claims/Yin_C_F0279_v1.md#decision-reviewed) also yields an exact weighted norm test for two-block outputs without a uniform lower Gram bound.
Its [conditional divergences](../claims/Yin_C_F0281_v1.md#decision-reviewed) quantify how much mass must leave increasingly rare spectral pairs and constrain nearly perfectly correlated tests.
Symmetric ordered couplings with finite reverse product divergence can still have maximal centered correlation one, leaving the other mixed-word tests essential.
For [a measurable location and scale of a free selfadjoint noise](../claims/Yin_C_F0277_v1.md#decision-reviewed), two explicit weighted differences together with an inverse-scale and marginal vacuum condition characterize both regularity hypotheses.
On the area disk, simultaneous location \(|Z|^\beta\) and scale \(|Z|^\alpha\) have both properties precisely for \(\alpha<1\) and \(\beta>2\alpha-1\), for positive exponents.
For a [commuting drift](../claims/Yin_C_F0283_v1.md#decision-reviewed) added to freely independent noise, the joint conditions are equivalent and force the drift to be a measurable function of the observed normal coordinate with square-integrable divided difference.
In a correlated semicircular pair, folding the first coordinate by absolute value preserves the generated algebra and both marginal conjugate variables but destroys the first joint conjugate variable.
For a [disk-valued Möbius transform of a free Haar unitary](../claims/Yin_C_F0290_v1.md#decision-reviewed), the marginal vacuum, an inverse-defect integral and a weighted divided-difference integral characterize both joint conditions, including when the disk parameter approaches the unit circle.
For normalized disk area and parameter \(1-|z|^\alpha\), both conditions hold exactly for \(0<\alpha<2\).
For old tuples with finite column costs in both orientations, the [bounded semicircular drift theorem](../claims/Yin_C_F0212_v1.md#decision-reviewed) decides both conditions for the tuple obtained by adjoining a free semicircular plus an arbitrary bounded selfadjoint old-algebra element.
With [arbitrary free selfadjoint noise having a scalar vacuum](../claims/Yin_C_F0268_v1.md#decision-reviewed), the two conditions hold exactly when the commutator of each old canonical slice with the drift is Hilbert–Schmidt.
The squared norm of each old vacuum increases by the squared Hilbert–Schmidt norm of its commutator times the squared norm of the noise vacuum.
For the original coordinate slice, the [omitted-algebra estimate](../claims/Yin_C_F0217_v1.md#decision-reviewed) controls every column after projecting its outputs to the algebra generated by the other coordinates.
It controls the entire output on linear combinations of words with one unstarred occurrence of the distinguished coordinate and arbitrary bounded omitted factors.
The [first output layer](../claims/Yin_C_F0223_v1.md#decision-reviewed) also satisfies a column estimate for every original starred polynomial, with constant at most twice the vacuum norm.
It controls the full slice on words with up to two unstarred occurrences of the distinguished centered coordinate and arbitrary omitted-coordinate coefficients.
For unrestricted inputs the remaining estimate concerns the output perpendicular to both the omitted algebra and the cyclic bimodule generated by the centered coordinate.
When the omitted algebra is abelian, the [weighted joint-span estimate](../claims/Yin_C_F0228_v1.md#decision-reviewed) also controls the span generated by the centered coordinate and its adjoint under an inverse-square-root condition on the projected vacua.
A correlated parabolic normal pair satisfies this condition and has both full domains even though the uniform phase gap vanishes.
The [measurable corner theorem](../claims/Yin_C_F0226_v1.md#decision-reviewed) excludes an asymptotically commuting bounded sequence of omitted coefficients of positive variance against any fixed nonconstant bounded spectral function of the distinguished coordinate.
The [common column tests](../claims/Yin_C_F0227_v1.md#decision-reviewed) describe exactly what must persist along a sequence of uniformly bounded normal laws with uniformly bounded actual vacua for some limiting law to have infinite column cost.
They also rule out divergent singular-projection tests localized in the omitted algebra by a conditional inverse covariance estimate.
For shifts by arbitrary omitted coefficients, the [unconditioned mass estimate](../claims/Yin_C_F0229_v1.md#decision-reviewed) gives \(\tau(1_{[0,r]}(|X_i-b|))^2\le\pi r\|\xi_i\|_2\) in the original algebra.
Its integrated identity controls the failure of the polar unitary of the shift to align with the actual marginal phase.
The [four-point estimate](../claims/Yin_C_F0230_v1.md#decision-reviewed) relates this loss to the angles of cross ratios drawn from two weighted marginal laws of the distinguished coordinate.
Along bounded shifts with phase loss tending to zero on weights of uniformly positive trace, a subsequence of the weighted laws is carried in the limit by a common line.
For singular spectral projections whose radii tend to zero, the mass estimate forces the traces to tend to zero, so that the positive lower trace in this conclusion cannot be retained.
The [weighted polar derivative calculation](../drafts/Yin_D_F0006.md#shifted-modulus-graph-and-phase-mismatch) places the modulus in the closed derivation domain and controls the difference of its two derivative terms with the weight \((v+w)^{-1/2}\).
For tests where the resolvent phase pairing is nonpositive, the [signed resolvent estimate](../drafts/Yin_D_F0006.md#nonpositive-compressed-phase) gives the exponent \(2/3\).
For a family of such tests a Hilbert-space overlap bound on the normalized resolvent vectors suffices for the required packing sum.
The [scalar radial examples](../drafts/Yin_D_F0003.md#sharp-scalar-limits-of-radial-vacuum-tests-at-an-omitted-shift) show that the radial vacuum identity with a strictly positive compressed phase allows exponents between \(1/2\) and \(2/3\) in abstract scalar data.
Realizing those data for an actual coordinate and omitted shift requires the phase to come from the marginal normal operator.
The [overlapping projection estimates](../claims/Yin_C_F0258_v1.md#decision-reviewed) also test noncommuting projections outside the omitted algebra.
Writing \(F(r)\) for the supremum, over all omitted shifts, of the singular mass up to \(r\), a finite original column cost \(c\) forces \(\int_0^\infty F(r)^3\,dr/r^3\le24c^2\).
The shift may vary at every radius, so divergence for this single envelope would give a separating normal tuple after adjoining two free Haar unitaries.
Conversely, finiteness of the cubic integral gives [both canonical domains and uniform cutoff convergence](../claims/Yin_C_F0287_v1.md#decision-reviewed) on the polar factors of the shifts, their adjoints and their products with omitted contractions on either side.
The same estimate applies to shifts of a fixed mixed polynomial and, for a selfadjoint polynomial, to every threshold in a family with finite common cubic integral.
The [supporting-half-plane estimate](../claims/Yin_C_F0231_v1.md#decision-reviewed) shows that \(t^3/r^2\to0\) uniformly when an omitted unitary can put the real part of \(X_i-b\) above \(-\kappa r\) for fixed \(\kappa\), where \(t\) is its singular mass up to \(r\).
At these shifts a divergent sum still requires an unbounded Gram norm for the normalized inverse tests.
The [endpoint integral for restricted shifts](../claims/Yin_C_F0261_v1.md#decision-reviewed) follows from the actual vacuum alone for all shifts admitting such a supporting half-plane at the tested radius, and for any fixed family with nonpositive radial phase pairing at every scale.
The [positive-phase estimate](../claims/Yin_C_F0261_v2.md#decision-reviewed) gives the cubic integral for every uniform normalized phase bound strictly below \(1/3\), even when the maximizing shift varies with the radius.
At equality the radial identities admit a square-integrable vacuum functional and logarithmic divergence, leaving realization by an actual omitted shift open.
The [two original resolvent tests](../claims/Yin_C_F0269_v1.md#decision-reviewed) force the normalized right and left singular spectral projections of any divergent envelope to concentrate at the same marginal spectral point along a sequence of radii and shifts.
The [mixed tests at the limiting point](../drafts/Yin_D_F0006.md#mixed-spectral-localization-at-divergent-shifts) also concentrate the polar variation, and a fixed shift must share that spectral point with the coordinate.
The [normal-residual classification](../claims/Yin_C_F0270_v1.md#decision-reviewed) excludes divergence for all shifts leaving a normal residual, with scalar shifts the only such choices for noncollinear marginal spectra.
For [marginal secants in a single narrow cone](../claims/Yin_C_F0272_v1.md#decision-reviewed), the two resolvent traces give a quantitative cubic bound over the entire omitted algebra, including shifts leaving nonnormal residuals.
The [local secant obstruction](../claims/Yin_C_F0273_v1.md#decision-reviewed) excludes divergence if every marginal spectral point has a unique limiting chord direction, even when those directions vary across the spectrum.
At a putative fixed critical shift the limiting marginal point must have phase spread at least \(4/\sqrt3-2\).
For a compact family of affine shifts by a second coordinate with slope bounded away from zero, the [simultaneous marginal test](../claims/Yin_C_F0296_v1.md#statement) constrains both spectra at the same character of the generated two-coordinate \(C^*\)-algebra.
The [remaining arbitrary-shift problem](../drafts/Yin_D_F0006.md#matching-singular-points-for-affine-shifts) concerns shifts for which that second derivative has variable tensor values or is undefined.
For a [fixed bounded Borel shift](../claims/Yin_C_F0298_v1.md#decision-reviewed), local adjoint tests on regular inverse branches constrain the two singular states even if the shift lies outside the global coarse derivative domain.
For a [regularly varying singular law](../claims/Yin_C_F0274_v1.md#decision-reviewed) of index \(\alpha\) with divergent cubic integral, the corresponding bound is \(2(\csc(\pi\alpha/2)-1)\), including critical laws with a vanishing slowly varying factor.
The [localization of the divergent integral](../drafts/Yin_D_F0006.md#local-critical-shell-integrals) retains radii of infinite cubic integral in every neighborhood of one exceptional point.
The [disk pair with a common character](../claims/Yin_C_F0275_v1.md#decision-reviewed) realizes all marginal secant directions at that character while its nonnormal residual has singular mass asymptotic to \(s^2\).
The [marginal density and spectral partition estimate](../claims/Yin_C_F0233_v1.md#decision-reviewed) bounds the original sum itself when each shift has a local finite-spectrum approximation with uniformly bounded effective number of spectral values and approximation and commutator errors of order \(r_j\sqrt{t_j}\).
It applies to singular projections outside the omitted algebra and permits different spectral partitions for different shifts.
The [four-value shift](../claims/Yin_C_F0235_v1.md#decision-reviewed) in a free Haar pair violates both the half-plane and finite-spectrum approximation hypotheses along every sufficiently small exact singular cutoff, even though the pair has strong duals.
For this model the commutator error divided by \(r\sqrt{t_r}\) diverges even when the four-value shift itself is used as the approximant.
Thus a proof from these projection tests must allow large off-diagonal components on small corners even for independent coordinates.
There is a separate positive result for correlated coordinates whose marginal spectra admit smooth parametrizations.
The [finite disjoint arc theorem](../claims/Yin_C_F0234_v1.md#decision-reviewed) gives the original column cost and both canonical domains at a specified coordinate with such a carrier, without any spectral assumption on the other coordinates.
The [closed curve theorem](../claims/Yin_C_F0236_v1.md#decision-reviewed) allows a full regular loop with weighted summable Fourier coefficients, including every regular \(C^3\) embedded loop.
The full comparison holds when each coordinate admits one of these two carrier types.
The [separated component theorem](../claims/Yin_C_F0237_v1.md#decision-reviewed) also controls mixed words within each regularly parametrized component, even when a single coordinate carries both arcs and complete loops.
For arbitrary diffuse marginals, the [inverse spectral gap criterion](../claims/Yin_C_F0238_v1.md#decision-reviewed) separates the marginal and off-diagonal contributions to the actual vacuum and recovers the original column cost by testing uniform boundedness of its regularizations.
The [scalar vacuum norm squared](../claims/Yin_C_F0255_v1.md#decision-reviewed) is comparable to the sum of the total squared Menger curvature and the integral of the squared maximal linear density.
For an [arbitrary scalar normal law](../claims/Yin_C_F0267_v1.md#decision-reviewed), a weight dominates the original slice exactly when it controls the local vacuum and line-density term pointwise and the positive two-point curvature integral on nonnegative tests.
The same two constraints hold on the marginal compression of any mixed weight.
On the uniform disk the [radial weight criterion](../drafts/Yin_D_F0006.md#radial-disk-weights) gives the sharp logarithmic power two at the center, also on the mixed core after a free extension.
For [square-Dini changes of planar coordinates](../claims/Yin_C_F0254_v1.md#decision-reviewed), a direct comparison of the three-point soft Cauchy kernels gives an explicit upper bound for the new vacuum norm.
For [all global bilipschitz homeomorphisms of the plane](../claims/Yin_C_F0256_v1.md#decision-reviewed), the geometric energy and the mixed vacuum norm squared are comparable in both directions with constants depending only on distortion.
The [exact change in right column cost](../claims/Yin_C_F0257_v1.md#decision-reviewed) is measured on the original mixed columns by inserting the inverse secant of the coordinate change.
If all near-identity maps have finite cost, the costs of their Lipschitz first variations must be uniformly bounded at a dense open set of centers.
The [Poisson–Haar calculation](../drafts/Yin_D_F0002.md#poisson-haar-bilipschitz-orbit) controls the entire mixed word space on the bilipschitz orbit of that particular correlated pair through the last block in each reduced word.
For a [free unitary rotated by a Borel phase](../claims/Yin_C_F0265_v1.md#decision-reviewed), an arbitrary planar base with actual scalar vacuum yields both conditions exactly when the divided difference of the phase is square integrable or the unitary has Haar law.
Thus even a discontinuous phase with finite energy can be treated on the full mixed core.
The [density factorization argument](../drafts/Yin_D_F0002.md#cauchy-measure-with-cubic-density) also considers representations of a scalar law as an \(L^3\) density over a measure with uniformly bounded hard Cauchy truncations on \(L^2\).
Any separating example must have finite inverse-gap energy of the liberation vector and fail a uniform regularized column bound, possibly after taking the adjoint tuple and adjoining two free Haar unitaries.
The [dyadic column estimate](../claims/Yin_C_F0242_v1.md#decision-reviewed) gives at most logarithmic growth as the cutoff is removed, with square-root logarithmic growth for the off-diagonal vacuum contribution.
The [localized curvature estimate](../claims/Yin_C_F0297_v1.md#decision-reviewed) sums the squared dyadic marginal ball densities without any separate summability assumption on the liberation vacuum.
Even on a [single nondecreasing Lipschitz graph](../claims/Yin_C_F0300_v1.md#decision-reviewed) with finite total squared curvature, bounding each shell kernel by its supremum on a supporting square costs a positive amount on every sufficiently small scale, for every partition of the integrated third variable.
Further use of this estimate at that endpoint requires cancellation or finer control in the two remaining spectral variables.
Its shell bounds are summable under the stated logarithmic improvements in the marginal ball masses and the inverse-gap energy.
For general marginals the remaining issue is cancellation across shells.
On a [fixed correlated pair with rectangular spectral support](../claims/Yin_C_F0253_v1.md#decision-reviewed), the full soft cutoff has a uniform column bound, while a single half-plane cutoff costs at least a constant times \((\log(1/r))^{1/4}\).
At each radius one mixed polynomial also gives this lower bound for the angular root mean square, so the estimate requires cancellation between opposite directions before taking norms.
In the [Poisson Haar pair](../drafts/Yin_D_F0002.md#spectral-phases-in-r1-and-collinear-annular-outputs-in-a-correlated-haar-pair), the fine radial shells on powers of the generator product give positive multiples of the same vector, while the full shell series on its Laurent polynomials sums to zero.
Even for correlated Haar generators with bounded duals, the [fixed-cutoff counterexample](../claims/Yin_C_F0245_v1.md#decision-reviewed) shows that evaluating the free model's sliced words at the correlated generators gives an unbounded map on the correlated operator-norm unit ball.
The [two-block criterion](../claims/Yin_C_F0239_v1.md#decision-reviewed) excludes the pair consisting of a diffuse normal coordinate and its conjugate by an independent free unitary of nonzero trace.
The [singular disk coupling](../claims/Yin_C_F0240_v1.md#decision-reviewed) nevertheless supports bounded tests in both two-block directions even with positive diagonal mass.
In its commuting realization a degree-three zero relation detects the failure of the full vacuum.
In its noncommuting realization neither coordinate has a full mixed-word vacuum, by the [free conjugation theorem](../claims/Yin_C_F0243_v1.md#decision-reviewed) for diffuse commuting normal generators and a free unitary of nonzero trace.
In the [two-segment Gaussian example](../claims/Yin_C_F0241_v1.md#decision-reviewed), an inverse divided difference with logarithmically divergent Schur multiplier norms still permits finite original columns in both orientations.
More generally, the [spectral relabelling theorem](../claims/Yin_C_F0244_v1.md#decision-reviewed) tests the transformed vacuum by its scalar marginal and the pushforward inverse-gap integral of the same liberation vector.
Both tests are invariant under a real Lipschitz graph over a selfadjoint coordinate, in arbitrary correlated tuples.
A measurable Schur bound on the inverse secant suffices to control the original columns after the coordinate change.
For [graph slopes of bounded variation](../claims/Yin_C_F0246_v1.md#decision-reviewed), integrating the slope variation against the estimates for single vertices controls both original columns, even when the inverse secant has infinite Schur norm.
The column bound depends on the total slope variation and the original real conjugate-variable norm, allowing infinitely many jumps of summable magnitude.
Around one accumulation point, [the localized shell bound](../claims/Yin_C_F0247_v1.md#decision-reviewed) uses only the largest slope variation on a single one-sided shell.
It proves both domains for the dyadically repeated triangular graph even though its slope has infinite total variation and its sampled inverse secants have unbounded Schur norms on interval-supported marginals.
The [local slope oscillation estimate](../claims/Yin_C_F0286_v1.md#decision-reviewed) gives both domains when the squared slope oscillations weighted by local linear density sum uniformly over scales.
The [four-point curvature bound](../claims/Yin_C_F0291_v1.md#decision-reviewed) makes the uniform row estimate alone sufficient and permits certain unbounded rows when a Schur weight also controls the off-diagonal spectral measure of the joint vacuum.
On the graph of distance to the middle-thirds Cantor set, the weighted example in that result has uniformly bounded curvature rows exactly for logarithmic decay exponent \(\beta>1/2\).
On [finite arc networks](../claims/Yin_C_F0248_v2.md#decision-reviewed), each pair of incident branches with distinct outgoing tangents has its own real projection chart.
At a common tangent, encoding intervals of length comparable to the actual branch separation and grouping by height gives the mixed-column bound even at infinite-order contact.
The finite sum of the pair estimates controls the original mixed words on networks with crossings, branches and cycles.
For [two graphs with equal slopes on their closed contact set](../claims/Yin_C_F0252_v1.md#decision-reviewed), assigning each common point a single real label retains its full spectral mass.
The square-root height estimate sums the interaction of this set with all positive height bands, including when infinitely many complementary intervals meet the set.
For [power-order contact](../claims/Yin_C_F0250_v1.md#decision-reviewed), interleaving the two branches in real intervals of the size of their separation gives a forward Lipschitz decoder and a cross-branch Schur estimate, including for \(x\pm i x^2\).
For arbitrary planar marginals, the [rectangular liberation calculation](../drafts/Yin_D_F0002.md#a-rectangular-liberation-block-and-the-remaining-diagonal-terms) retains the two diagonal quadratic forms omitted by a cross-only estimate.
The fixed-center mass series in (R3) there is bounded uniformly by scalar packing.
In the [Poisson unitary pair](../claims/Yin_C_F0251_v1.md#decision-reviewed), both diagonal forms can be arbitrarily negative on the same norm-one mixed word as the law varies; the actual cross compression of the liberation vacuum controls their weighted sum on all the tested powers.
For a Lipschitz graph the [weak trace-class estimate](../audits/literature/CSZ18/Yin_U001.md#csz18-u001) applies to the exact inverse-secant symbol, and the [heat-semigroup BMO estimate](../audits/literature/CJSZ20/Yin_U001.md#cjsz20-u001) acts on its finite spectral blocks.
The [semicircular Chebyshev tests](../claims/Yin_C_F0249_v1.md#decision-reviewed) have degree-dependent unbounded pairings on the entire graph heat BMO and weak trace-class unit balls, even for length-one mixed columns.
For each fixed actual inverse secant their pairings are square summable, so a proof using these operator estimates must retain the special symbol in the mixed-word test.
The [two-point modulus rank obstruction](../claims/Yin_C_F0232_v1.md#decision-reviewed) excludes every normal encoding retaining the full matrix-amplified star algebra of the nonnormal example, and rules out bounded-vacuum approximation of its real–imaginary and polar pairs in moments.
For the alternative representation as the midpoint of two unitaries, [localization of the relative unitary](../drafts/Yin_D_F0006.md#two-point-modulus-matrix-encoding) forces vacuum blowup even for perturbations retaining just one approximate atom of positive mass.

On the general branch, the [noisy Jordan family](../claims/Yin_C_F0213_v1.md#decision-reviewed) forces a bounded-dual cost of order inverse noise at fixed matrix size.
At size two a separating sequence exists along this route exactly when the noise level times the norm of the projection of the canonical vacuum onto the kernel of the closed starred cut tends to zero on a subsequence.
The [vacuum-only tests](../claims/Yin_C_F0214_v1.md#decision-reviewed) compute the required infimum for any represented tuple by imposing every word degree before removing the penalty on the starred values.
Reversing those limits can give an arbitrarily smaller denominator already on scalar normal laws with both full domains.
For [univalent circular changes](../claims/Yin_C_F0218_v1.md#decision-reviewed) the least vacuum norm is attained and equals the reciprocal absolute derivative at the origin.
Thus unbounded bounded-dual costs for changes normalized to derivative one would suffice for the single-generator assembly.
The [bounded circular shear](../claims/Yin_C_F0221_v1.md#decision-reviewed) realizes unbounded costs with both actual vacuum norms one across two-coordinate laws, while each individual law has strong duals.
The second generator in that quadratic family has growing operator norm, and the one-generator assembly does not furnish a separating law from these pairs.
More sharply, the [joint graph-domain obstruction](../claims/Yin_C_F0222_v1.md#decision-reviewed) rules out the separated-spectra assembly itself at tuple length two or greater, even with nonnormal coordinates.
A central projection in the generated \(C^*\)-algebra would give two incompatible equations in the affiliated algebra of a pair of corners.
The [two-circular palindrome drift](../drafts/Yin_D_F0005.md#two-circular-palindrome-drift) has bounded operator norm and formally infinite derivative energy, but its first commutator remains bounded and the equal-cut vacuum correction has an unbounded starred value.
For this drift the [analytic-word calculation](../drafts/Yin_D_F0005.md#circular-shear-analytic-columns) gives a uniform column bound even with arbitrarily many analytic noise letters, leaving the mixed starred tests essential to this route.
On the factor branch, the [weighted ergodic shift theorem](../claims/Yin_C_F0219_v1.md#decision-reviewed) excludes every nonconstant positive log-integrable weight from ACSY, even with atomic weight distributions.
An irrational rotation gives a single generator of a type II factor with a bounded whole-Hilbert dual and no normalized coarse derivation.
For candidate matrix encodings, the [Brown-measure energy obstruction](../claims/Yin_C_F0220_v1.md#decision-reviewed) requires mutually singular Brown measures across every commuting graph-domain projection.
It excludes the two-by-two cyclic generator with upper-right unit and lower-left strict contraction from actual ACSY.

The [continuous tests in C_F0201 v2](../claims/Yin_C_F0201_v2.md#decision-reviewed) characterize a separating moment limit of bounded normal tuples with uniformly bounded conjugate vectors.
For each proposed dual norm cap, a fixed finite-word test must retain a strictly positive discrepancy along a common subsequence, in a single coordinate and direction.
The [pair-relative commutant theorem](../claims/Yin_C_F0202_v1.md#decision-reviewed) excludes nontrivial mixtures of distinct laws from both classes when there are at least two normal coordinates.
Thus a limit retaining ACSY must generate a factor even when its proposed approximants have identical one-coordinate marginal laws.
The [two translated semicircular systems](../drafts/Yin_D_F0003.md#exponential-word-obstructions-in-a-mixture-of-two-factor-laws) give explicit exponential growth of both represented word tests on a mixture.

The arbitrary-tuple counterexample uses nonnormal coordinates.
In its single-generator building blocks the projections onto the small singular spaces of \(X\) and \(X^*\) differ.
Normality identifies these projections and determines the starred derivative by the marginal phase, removing the freedom used in the group-ring vacuum construction.

## Evidence and decisions

On 2026-10-15 the bounded-similarity construction was fixed in C_F0133 and independently reviewed in [R_F0140](../audits/reviews/Yin_R_F0140_v1.md#conclusion).
It resolves the general F-to-A direction negatively.
The independent [review of the two-point-modulus example](../audits/reviews/Yin_R_F0233_v1.md#whole-proof-finding) verifies the reverse nonimplication.
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
The unrestricted normal implication remains open.
Their selected Claim decisions own acceptance.
The continuing D materials retain the further constructions and useful failures at their stated development scope; none of these results supplies a completion decision for this Task.

The Task remains active.
Completion still requires the normal A-to-S direction and its consequences for the two fraction criteria at that scope, followed by review of the full contract.

The explicit normal-endpoint continuation is retained in [D_F0006](../drafts/Yin_D_F0006.md#selfadjoint-tests-and-the-correlated-unitary-obstruction).
It reduces a sufficient universal quadratic theorem to positive core inputs and excludes the sharp scalar fixed-vacuum domination even on a strictly positive mixed test in an actual correlated-unitary model.
The same model's all-degree adjoint norms remain bounded for each fixed law.
The finite normal-coordinate-change tests in J_F0009 are diagnostic only and provide neither the unrestricted endpoint estimate nor an actual domain counterexample.

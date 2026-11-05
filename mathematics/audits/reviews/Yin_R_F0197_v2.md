---
author: Yin
---

# Independent review of the full Haar affine determinant limit

<a id="independent-full-haar-proof"></a>
## Finding: the full statement and original four-part contract are supported

Review act: 2026-11-05T09:31, human record author Yin.
A separately organized AI reviewer outside substantive proof development examined the fixed [full statement](../../claims/Yin_C_F0192_v2.md#statement), [complete argument](../../claims/Yin_C_F0192_v2.md#argument) and every direct dependency declared by [the candidate decision](../../claims/Yin_C_F0192_v2.md#decision-full-haar-candidate).
The review also compared the result with the complete [original F0015 contract](../../tasks/Yin_T_F0015_v1.md#contract).
The supplied context contained the assignment, fixed locators, human authority, applicable rules and operational limits, with no proof-generation dialogue, exploration notes, mathematical development summary, author explanation or prior conclusion about this full proof.
The reviewer read the fixed mathematics directly, formed the initial full-proof findings, and subsequently consulted [the earlier restricted review](Yin_R_F0197_v1.md#independent-haar-structural-proof) only to compare the retained generic-rank and asymptotic-input scope.
That earlier finding supplies no review of the new proof.
No substantive correction or additional proof mechanism was contributed by this reviewer.

The exact full statement is supported without a remaining mathematical gap at the accepted external-input boundary stated below.
It gives almost-sure extended-real convergence of the ordinary normalized logarithmic determinant for every fixed arbitrary complex coefficient tuple and every allowed cross-dimensional coupling.
The finite-target least-singular-value probability floor is also supported for every prescribed power.
The original contract is resolved affirmatively in all four entries: full limit and upper-limit equality under arbitrary coupling, and each assertion under independent dimensions.
This finding supplies mathematical completion coverage; it does not itself select a Claim assessment or Task lifecycle decision.

## Geometric repair and the Haar tube

The approximate kernel's component span has dimension at most m, and its full output span has dimension at most (r+1)m.
Their frame coordinates recover the entire residual, including the arbitrary constant coefficient, rather than only a compressed part of it.
The residual, frame-isometry constraints and vector normalization form a fixed-dimensional degree-two real polynomial map.
There are finitely many dimension types, so the accepted bounded-coordinate error bound yields one positive exponent independent of N.
For an empty-zero-set type, the original compact coordinate bound gives a positive minimum residual and excludes that type below a fixed threshold.

I checked the polar extension calculation, including B*B, its identity action on the input frame and the Hilbert--Schmidt estimates independent of ambient dimension.
The corrected frames therefore lift to nearby full unitaries acting on the corrected normalized vector, which is an exact kernel vector.
The same correction controls intrinsic distance through the principal logarithm near the identity.
Zero-dimensional orthogonal complements cause no exception.
No compatibility between different input unitaries beyond their individual isometric actions is needed.

The tube proof uses an independent Haar center W and a uniformly sampled Euclidean ball coordinate H.
For each fixed H, right multiplication by C(H) preserves the full product Haar law, so averaging gives exactly Haar measure without a chart-density comparison.
The unit coordinate ball supplies a dimension-independent lower bound for the inverse Cayley denominators.
A nearby singular unitary tuple therefore has Hermitian inverse coordinates within twice the original intrinsic or chordal distance, even when those repaired coordinates lie outside the sampling ball.

I checked the block Schur complement (H11)--(H12) with the order of all noncommuting factors retained.
The first mN rows are constant, so the squared complex determinant is a nonnegative real polynomial of degree at most 2rmN.
Nonidentity holds in every translated Cayley chart because that chart is dense and the original determinant has an open nonzero locus.
The accepted regular-level extension of the uniform-ball tube theorem applies to this nonzero polynomial, including singular zero sets and real codimension greater than one.
Substitution of \(n=rN^2\) and \(D=2rmN\) gives the stated \(O(N^3\varepsilon)\) bound in its stated small-radius regime.
Its constants are independent of the numerical coefficient values subject to nonidentity.
The empty singular set has probability zero throughout this argument.

## Quantitative spectral and probability interfaces

The Par22 specialization uses auxiliary size 2m and deterministic coefficient matrices that may fail to commute with one another.
The tensor flip preserves normalized trace and gives precisely the displayed Hermitization, including the singular or zero constant term.
Multiplication of the resolvent comparison by \(t\) produces the error \(N^{-2}\log^2N\,t^{-4}\); the additional \(t^{-1}\) term is smaller for \(0<t\le1\).
The symmetric Hermitization law has the same singular-value integrals for even tests, with no missing factor of two.

I checked the correction from the source's conditional SU(N) center to the full Haar mean.
Factoring each unitary by a determinant phase in \([0,2\pi)\) moves its special-unitary conditional average by at most \(2\pi L\sqrt{r/N}\).
Averaging this diameter estimate identifies the full mean, and the triangle inequality retains exactly the deterministic shift in (H17).
The singular-value Frobenius inequality, tensor Hilbert--Schmidt bound and Cauchy--Schwarz give the normalization in (H18), hence (H19).
When every random coefficient is zero, the statistic is deterministic and requires no concentration estimate.

A finite ordinary free logarithm excludes the zero atom of the singular law and of its Hermitization.
SS15's Haar matrix-polynomial Puiseux expansion applies to this selfadjoint Hermitization.
The resolvent bound excludes exponents below minus one, and the limit of \(itG(it)\) excludes the minus-one coefficient when the zero atom is absent.
The next possible rational exponent yields the positive power used in (H20); atomlessness of arbitrary matrix polynomials is neither assumed nor inferred.

Both strict inequalities for \(\gamma\) in (H21) have their stated separate roles.
The first absorbs the logarithmic resolvent error uniformly for \(t_N\le t\le1\).
The second makes the conditional-center shift negligible relative to \(t_N^\beta\) and makes the moving-count concentration probabilities summable.
First Borel--Cantelli proves (H22) for every coupling.
The clipped logarithm has Lipschitz constant at most \(N^\gamma\), so its mean-centered deviation also tends to zero almost surely with summable tails.
Every probability argument here uses only the product Haar marginal at a single dimension.

## Logarithmic cutoff removal and contract comparison

For finite u, the accepted zero-free-kernel generic-rank result gives determinant nonidentity for every sufficiently large dimension.
Combining the unitary backward error with the intrinsic tube gives probability at most \(C N^3\varepsilon^\alpha\) in the required radius range.
Choosing \(B\alpha>4\) gives a summable polynomial floor, and choosing \(B\alpha>q+3\) gives the stated probability floor for each \(q>0\).
One can also impose \(B>\gamma\) without weakening either conclusion.

The deterministic coefficient norm bound makes every fixed clipped logarithm a bounded continuous spectral test, so almost-sure weak convergence also gives convergence of its expectation by bounded convergence.
Layer integration of the uniform expected-count bound gives the displayed \(C\varepsilon^\beta\) error between the fixed and moving clipped means.
Taking \(N\to\infty\) and then \(\varepsilon\downarrow0\) identifies those means with finite \(u\).
On the common eventual floor event, the remaining difference between the moving clipped log and the ordinary log is at most \(B\log N\,\nu_N([0,t_N])\), which tends to zero by (H22).
This is a complete lower-tail argument rather than an inference from weak convergence alone.

For \(u=-\infty\), a countable decreasing family of fixed cutoffs, weak convergence and the norm bound give the full limit through every dimension.
No generic nonidentity, finite invertibility or floor is required in that branch, so identically singular finite pencils and all-zero coefficients remain covered.
The traces are normalized by mN for the pencil and 2mN for Hermitization throughout.
The claim's event may depend on the fixed coefficients and coupling, exactly as the contract permits.
There is no uncountable simultaneous-event requirement.
Full convergence implies upper-limit equality in both the finite and minus-infinite cases, and the arbitrary-coupling conclusion includes independent dimensions.
Thus no original assertion, coupling regime, coefficient degeneracy or dimensional endpoint remains as an unresolved mathematical obligation.

## Accepted source inputs and inspection limits

The bounded-coordinate real polynomial-map inequality and the uniform-ball tube theorem, including its regular-level extension, were read in [C_F0186_v1](../../claims/Yin_C_F0186_v1.md#error-bound) at their exact adopted scopes.
Their foundational external proofs remain accepted rather than newly re-audited.
The unitary constraints, frame lift, random-center chart, determinant-degree calculation and probability applications were checked directly here.
I read the full retained [generic-rank deduction](../../claims/Yin_C_F0192_v1.md#haar-generic-rank) and matched its zero-free-kernel hypothesis; no GUE probability conclusion is reused.
I also read the self-contained [singular-value Frobenius proof](../../claims/Yin_C_F0186_v3.md#singular-value-perturbation).

For [the Haar moment input](../../ledger/Yin_L_F0062_v1.md#haar-pencils), I checked CM14's published primary [Theorem 1.4 and Corollary 2.3](https://smf.emath.fr/download/pdf/44403), printed pp. 150 and 154 / PDF pp. 5 and 9.
They impose independence within each Haar tuple, with no cross-dimensional independence requirement; their strong-convergence setting includes trace convergence and fixed matrix coefficients.
Only moments and their bounded continuous singular-test consequence are needed here.
Their original proofs were not re-audited.
The accepted [Par22 unit](../literature/Par22/Yin_U001.md#par22-u001) was read in full at arXiv:2005.13834v2 Corollary 1.1, the precise tensor Hermitization specialization and Proposition 5.1 with its actual conditional center.
The accepted [SS15 unit](../literature/SS15/Yin_U001.md#ss15-u001) was read in full at the retained arXiv:1305.1920v1 Theorem 1.1(5)(6), including its Haar alternative, matrix coefficients, zero-atom boundary and actual edition qualification.
These established external statements are resolved inputs at those scopes, without a new full audit of their foundational proofs.

The [ordinary Fuglede--Kadison convention](../literature/MS24/Yin_U001.md#determinant-convention) was checked against the statement and original contract, including all zero spectral mass.
No claim is made about expectation convergence of unregularized logarithms, Brown measures, uniform coefficient-set limits, adjoint or higher-degree extensions, priority, formal verification or associated code.
None of those is required by the reviewed original contract.


<a id="post-completion-full-haar-chain"></a>
## Post-completion finding: the actually adopted full chain meets the original contract

Review act: 2026-11-05T09:37, human record author Yin.
This is a separately arranged independent inspection after [the Task completion decision](../../tasks/Yin_T_F0015_v1.md#decision-completed-full-haar-limit) and [the Claim proof decision](../../claims/Yin_C_F0192_v2.md#decision-full-haar-reviewed) were selected.
The reviewer remains outside substantive proof development and received only the fixed decision locators, actual adoption facts and operational limits for this follow-up, without mathematical development summaries or repair participation.
I read both actual selected decisions, the complete original contract, the current full statement and argument, their exact support and review selections, and the declared dependency scopes.
I reuse the directly inspected dependencies and the independently checked mathematics in [the initial whole-proof finding](#independent-full-haar-proof) only at their unchanged exact scopes.
I also checked the applicable existing proved decisions for the retained polynomial and tube inputs, the Haar generic-rank deduction and the singular-value perturbation input.
The new selections neither substitute a proof artifact nor change any necessary mathematical hypothesis or dependency scope.

The Task selects the full statement of C_F0192_v2 as its sole mathematical support and the initial whole-proof finding as its review evidence.
The selected Claim decision adopts that same statement and complete argument, all seven exact dependencies inspected above, and that same independent finding.
Every adopted statement, argument and dependency has its exact matching binding in the selected review, and the explicit relationship is independently reviewed.
The earlier review preceded both decisions and is applicable to their unchanged mathematics.
The present post-completion finding adds the actual adopted-chain check without backdating that review or treating its former contract coverage as an inspection of decisions not then made.

Working backward from the original contract, arbitrary coefficients require no monic, rank-one, bulk, invertibility or strict-stability reduction.
The adopted unitary-frame repair and Haar tube give the summable finite-target floor, while the accepted resolvent and Puiseux interfaces and the actual full-mean concentration shift give the moving small-mass bound and clipped-log limit.
The final logarithmic removal therefore controls the missing lower tail for the full coefficient class.
For a minus-infinite free logarithm, the separate fixed-cutoff argument covers every dimension without invoking generic invertibility.
The norm bound, the inclusion of all zero spectral mass in the ordinary determinant, and the normalized traces match the original contract in both branches.
No conclusion from the broader GUE theorems, conditional Schur theorem, sparse structural special cases, coupling-criteria theorem or positive determinant moments is needed beyond the exact retained inputs actually selected.

The original four obligations are all met: the full limit holds for every allowed coupling, its upper limit is therefore the same extended-real value, and independent dimensions are an included coupling regime for each assertion.
The event may depend on the fixed coefficient tuple and coupling, and the proof proceeds through all positive integer dimensions.
The adopted chain contains no unselected open premise, no cycle through an alternative proof, and no remaining coefficient, coupling or zero-target restriction.
The accepted external-theorem boundaries in the initial finding remain the boundaries of this conclusion; foundational source proofs, priority and formal verification have not acquired additional inspection through completion.
The actually selected Task completion is mathematically supported, and no post-completion mathematical obligation remains within its original contract.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Full Haar proof and completion finding](#independent-full-haar-proof) | independently reviewed |
| [Post-completion full Haar chain](#post-completion-full-haar-chain) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Full Haar proof and completion finding](#independent-full-haar-proof) | [Full statement](../../claims/Yin_C_F0192_v2.md#statement) | Entire extended-real ordinary logarithmic limit for every fixed arbitrary complex tuple and every coupling, including the finite-target floor at every prescribed probability power. |
| [Full Haar proof and completion finding](#independent-full-haar-proof) | [Complete argument](../../claims/Yin_C_F0192_v2.md#argument) | All new unitary repair, Cayley tube, quantitative spectral, central-phase, count, floor and logarithmic steps, including zero-target and deterministic cases. |
| [Full Haar proof and completion finding](#independent-full-haar-proof) | [Original Haar contract](../../tasks/Yin_T_F0015_v1.md#contract) | All four original obligations: full limit and upper-limit equality under arbitrary coupling and under independent dimensions, through all positive integer dimensions and with arbitrary constant coefficient. |
| [Full Haar proof and completion finding](#independent-full-haar-proof) | [Polynomial-map error bound](../../claims/Yin_C_F0186_v1.md#error-bound) | Accepted bounded-coordinate real polynomial-map distance inequality and its applicability to the finite list of unitary-frame coordinate types; no Gaussian law is invoked. |
| [Full Haar proof and completion finding](#independent-full-haar-proof) | [Uniform-ball algebraic tubes](../../claims/Yin_C_F0186_v1.md#tubes) | Only (T1)--(T2) and the proved regular-level extension for nonzero nonnegative polynomials, applied to each exact translated Cayley determinant polynomial. |
| [Full Haar proof and completion finding](#independent-full-haar-proof) | [Eventual Haar nonidentity](../../claims/Yin_C_F0192_v1.md#haar-generic-rank) | Complete retained zero-free-kernel implication for eventual nonidentity on full-unitary tuples; its algebraic and Haar applicability, with no quantitative floor borrowed from it. |
| [Full Haar proof and completion finding](#independent-full-haar-proof) | [Haar weak convergence](../../ledger/Yin_L_F0062_v1.md#haar-pencils) | Accepted almost-sure fixed-coefficient Haar moments and bounded continuous singular tests under every coupling; other determinant formulas and survey conclusions are not premises. |
| [Full Haar proof and completion finding](#independent-full-haar-proof) | [Singular-value Frobenius inequality](../../claims/Yin_C_F0186_v3.md#singular-value-perturbation) | Squared singular-value perturbation bound and the normalized spectral-statistic Lipschitz consequence with dimension mN. |
| [Full Haar proof and completion finding](#independent-full-haar-proof) | [Quantitative Haar source](../literature/Par22/Yin_U001.md#par22-u001) | Exact accepted arXiv v2 Corollary 1.1 at fixed matrix amplification and Proposition 5.1 at the conditional special-unitary center, with the new full-mean correction checked in C. |
| [Full Haar proof and completion finding](#independent-full-haar-proof) | [Free Haar algebraicity](../literature/SS15/Yin_U001.md#ss15-u001) | Exact accepted retained arXiv v1 Theorem 1.1(5)(6) for selfadjoint matrix polynomials in free Haar unitaries, with the zero atom separately excluded by finite ordinary free logarithm. |
| [Full Haar proof and completion finding](#independent-full-haar-proof) | [Ordinary determinant convention](../literature/MS24/Yin_U001.md#determinant-convention) | Normalized finite-tracial logarithmic determinant including zero spectral mass, matched to the full statement and original contract. |
| [Post-completion full Haar chain](#post-completion-full-haar-chain) | [Selected Task completion](../../tasks/Yin_T_F0015_v1.md#decision-completed-full-haar-limit) | Actual completed decision, unchanged contract, sole full-theorem support and exact independent-review selection; all four asserted outcomes are supported. |
| [Post-completion full Haar chain](#post-completion-full-haar-chain) | [Original Haar contract](../../tasks/Yin_T_F0015_v1.md#contract) | Full limit and upper-limit equality under both arbitrary coupling and independent dimensions, with arbitrary fixed complex coefficients and the ordinary extended-real determinant through all dimensions. |
| [Post-completion full Haar chain](#post-completion-full-haar-chain) | [Selected Claim proof decision](../../claims/Yin_C_F0192_v2.md#decision-full-haar-reviewed) | Actual proved decision, exact selected statement, complete argument, all seven declared mathematical dependencies and applicable independent evidence. |
| [Post-completion full Haar chain](#post-completion-full-haar-chain) | [Full theorem support](../../claims/Yin_C_F0192_v2.md#statement) | Entire adopted full Haar logarithmic limit and its stated finite-target floor, with all coefficient, coupling and zero-target cases retained. |
| [Post-completion full Haar chain](#post-completion-full-haar-chain) | [Complete adopted argument](../../claims/Yin_C_F0192_v2.md#argument) | End-to-end unitary repair, translated Cayley tube, generic nonidentity, quantitative spectral interfaces, actual concentration center, summable events and logarithmic removal. |
| [Post-completion full Haar chain](#post-completion-full-haar-chain) | [Selected initial independent evidence](#independent-full-haar-proof) | Actual independently reviewed relationship and exact statement, argument, original-contract and dependency bindings at their unchanged mathematical and source-inspection scopes. |
| [Post-completion full Haar chain](#post-completion-full-haar-chain) | [Polynomial-map distance input](../../claims/Yin_C_F0186_v1.md#error-bound) | Accepted bounded-coordinate real algebraic distance inequality for the finite list of unitary-frame types, with no Gaussian input-law transfer. |
| [Post-completion full Haar chain](#post-completion-full-haar-chain) | [Uniform-ball tube input](../../claims/Yin_C_F0186_v1.md#tubes) | Only (T1)--(T2) and the nonzero nonnegative-polynomial regular-level extension as used for each exact translated Cayley polynomial. |
| [Post-completion full Haar chain](#post-completion-full-haar-chain) | [Haar generic nonidentity](../../claims/Yin_C_F0192_v1.md#haar-generic-rank) | Accepted zero-free-kernel implication for every sufficiently large dimension and its full-unitary applicability; no small-positive-singular-value conclusion is borrowed. |
| [Post-completion full Haar chain](#post-completion-full-haar-chain) | [Haar asymptotic input](../../ledger/Yin_L_F0062_v1.md#haar-pencils) | Fixed-coefficient almost-sure Haar moment convergence and the bounded continuous singular-test consequence under every allowed coupling. |
| [Post-completion full Haar chain](#post-completion-full-haar-chain) | [Singular-value perturbation input](../../claims/Yin_C_F0186_v3.md#singular-value-perturbation) | Exact deterministic Frobenius inequality and normalized spectral-statistic Lipschitz consequence; none of the broader GUE conclusions is a Haar premise. |
| [Post-completion full Haar chain](#post-completion-full-haar-chain) | [Par22 quantitative input](../literature/Par22/Yin_U001.md#par22-u001) | Accepted exact arXiv v2 Corollary 1.1 at fixed noncommuting coefficient amplification and Proposition 5.1 at its actual conditional SU center. |
| [Post-completion full Haar chain](#post-completion-full-haar-chain) | [SS15 algebraicity input](../literature/SS15/Yin_U001.md#ss15-u001) | Accepted exact retained arXiv v1 Theorem 1.1(5)(6) for selfadjoint free Haar matrix polynomials; finite ordinary free logarithm separately excludes the zero atom. |
| [Post-completion full Haar chain](#post-completion-full-haar-chain) | [Ordinary determinant convention](../literature/MS24/Yin_U001.md#determinant-convention) | Normalized finite-tracial ordinary logarithm including zero spectral mass, with the exact original Task and adopted theorem conventions. |

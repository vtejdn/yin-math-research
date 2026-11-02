---
author: Yin
---

# Intrinsic affiliated rationality from the original polynomial dual data

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## Intrinsic regular commutators from original polynomial dual domains

<a id="statement"></a>
<a id="liberation-intrinsic-affiliated-criterion"></a>

Permanent proof artifact, 2026-09-29.
Authorship: another AI agent; root contributed the dense test-functional realization and criterion formulation.
The [selected decision](#current-assessment) owns the current assessment; the cited findings own their actual review relationships and scopes.
This material itself does not close a Goal.

Exact accepted direct dependencies: C_F0025 (recorded assessment 3) (original normal-core derivation, normalization, maximal Delta and free-field embedding); C_F0027 (recorded assessment 3) (actual original-closure recovery from core bounds); C_F0043 (recorded assessment 3) (the real controlled-defect norm calculation, with the complete liberation specialization below); C_F0034 (recorded assessment 3) (general finite-commutator fraction algebra); C_F0035 (recorded assessment 3) (the algebraic balanced-tensor equalizer).
Appendix A is part of this proof, not a dependency on an unregistered positive exploration claim.
The original exploration and its completed independent review are retained as provenance: [exploration](../ledger/Yin_L_F0011_v1.md#normal-mixed-energy-liberation-reduction), [review](../audits/reviews/Yin_R_F0035_v1.md).
No new external theorem or new full source audit is asserted.

The main body is promoted from the complete scratch candidate, preserving its mathematics.
Appendix A reproduces the full positive liberation-bound argument from the previously reviewed exploration, omitting only historical administrative status and the superseded reconstruction discussion.
Its complete proof is submitted again as part of the present independent review.
The Task's allowance for an explicitly modified criterion is assessed separately from the theorem.
Literal arbitrary raw-composition-domain agreement is not asserted.
## Liberation tensors and intrinsic regular deconvolution

Date: 2026-09-29.
Human author: Yin.
Proof development: another AI agent, with root's contribution of the dense test-functional realization and criterion formulation.
At authorship, this was a complete algebraic candidate submitted for independent review.

This note proves a finite-rank intrinsic regular-commutator criterion under the exact original C_F0025 hypotheses.
Its construction uses the actual original liberation closures.
It separately identifies the remaining issue in equating this construction with every possible raw composition domain of the original unbounded normal duals.
These two assertions must not be conflated.

## 1. Objects and already reviewed analytic input

Let M, H=L2(M,tau), U=U(M), P=C<X,X*> and the original normal-coordinate data D_i0 be as in C_F0025 (recorded assessment 3).
Put eta_i0=D_i0(1) and normalize on P by E_i0(p)=D_i0(p)-p eta_i0.
Write E_i=closure(E_i0).
The canonical original derivations partial_i satisfy E_i0=(id tensor tau)partial_i on P.
Write F=Div_U C<X_1,...,X_d>.
The accepted maximal-Delta conclusion embeds the free skew field and makes X_i-lambda invertible in U for every scalar lambda.
All unlabelled tensor products below are algebraic over C.

This normalization is derived from the specified original data, not an extra assumption.
C_F0025 proves that the bounded weak forms are unchanged.
Right multiplication by eta_i0 has both M in its domain and M in its adjoint domain.
Its contribution to any regular defect on M is s(bq eta_i0)-a(tq eta_i0)=(sb-at)q eta_i0=0.
Thus normalization also leaves every legitimate all-M regular defect unchanged.
Raw domain intersections for unbounded duals are not identified by this observation alone.

Use Theta(g tensor h)q=g tau(hq), with the usual conjugation convention equivalently Theta(g tensor h)=|g><Jh|.
It identifies H tensor_alg H with the finite-rank operators on H, and extends isometrically from the Hilbert tensor product to the Hilbert-Schmidt class.
Bounded outside multiplication corresponds to the outer bimodule action.

Define the inner operator

    B_i(g tensor h)=g X_i tensor h-g tensor X_i h.

It commutes with both outer U-actions whenever those actions make algebraic sense.
On Hilbert tensors it is bounded and corresponds to

    Theta(B_i t)=[rho(X_i),Theta(t)].                         (1)

Appendix A below fully proves the following liberation construction; its earlier independently reviewed exploration is retained as provenance:

    delta_i=i B_i partial_i,  A_i0=(id tensor tau)delta_i,
    M subset Dom closure(A_i0) intersect Dom A_i0*.

These are the actual closures from P.
Denote the closure by A_i and its restriction to M by A_i^M.
Its adjoint contains M.
Thus C_F0034 applies with the specified domain E=M and adjoint test module V=M.
The generator commutators are

    [A_i^M,X_j]=i delta_ij Theta(X_i tensor 1-1 tensor X_i).  (2)

To extend the initial P identity to M here, approximate any vector of Dom A_i by its original graph-core polynomials.
Since the commutator on P is bounded, X_j preserves Dom A_i and the identity extends; then restrict to M.
No boundedness of A_i on H is asserted.

On P, the sum of liberation derivations is p tensor 1-1 tensor p, times i.
Consequently sum_i A_i p=i(p-tau(p)).
To extend to M, choose uniformly bounded polynomial approximants converging strongly, hence in L2, to a fixed bounded element.
The infinity-to-L2 bounds make each A_i output bounded in L2.
Every joint weak cluster belongs to the actual original graphs because closed linear graphs are weakly closed.
Thus the sum has the asserted limit.
No bounded-strong continuity follows from the infinity-to-L2 estimate alone.
Hence

    sum_i A_i^M=i(I-P_Omega) on M.                          (3)

## 2. The finite-tensor removal lemma

Lemma.
Suppose x is bounded, x-lambda is invertible in U for every complex lambda, and T belongs to U tensor U.
If

    B_x T in H tensor_alg H,

then T belongs to H tensor_alg H.
Also B_x is injective on U tensor U.

Proof.
First observe that multiplication by x on either side of U has no nonzero finite-dimensional invariant complex subspace.
Such a subspace would contain an eigenvector v, contradicting invertibility of x-lambda.
The same observation holds for its restrictions to H.

More generally, let V,W be complex vector spaces, a an endomorphism of V and b an endomorphism of W having no nonzero finite-dimensional invariant subspace.
The map a tensor I-I tensor b on V tensor W is injective.
Indeed, if a nonzero tensor lies in its kernel, choose a minimal expression sum_{k=1}^m v_k tensor w_k with both families linearly independent.
Applying the quotient W/span{w_k} in the second leg shows b w_k belongs to this span for each k.
This is the forbidden finite-dimensional invariant subspace.
The symmetric version applies when a has that property instead.

Now apply the quotient U->U/H in the first leg to B_x T.
Since H is stable under right multiplication by x, B_x descends to (U/H) tensor U.
Its kernel is zero by the preceding observation on left multiplication on the second leg.
Exactness of algebraic tensoring over a field therefore gives T in H tensor U.
Apply U->U/H in the second leg next.
The descended map on H tensor (U/H) has zero kernel by right multiplication on its first leg.
Thus T in H tensor H.
The same invariant-support argument directly proves injectivity on U tensor U.
This is an algebraic result, with no inverse norm estimate and no completed-tensor quotient.
QED.

For later uniqueness, B_i is also injective on the Hilbert tensor product.
Under the Hilbert-Schmidt identification, a kernel vector is a compact operator commuting with the bounded normal operator rho(X_i).
Fuglede gives commutation with its adjoint and hence a reducing finite-dimensional nonzero eigenspace of the compact positive operator T*T, unless T=0.
The restriction of rho(X_i) to that subspace has an eigenvector, impossible because X_i-lambda is regular.
Thus the Hilbert-Schmidt commutator map in (1) is bounded and injective.
Its inverse on its range is a closed operator between Hilbert-Schmidt spaces.
Its range need not be closed.

## 3. An affiliated derivation obtained from actual finite defects

For u in U and a bounded fraction pair

    u=s^-1 a=b t^-1,   s,a,b,t in M, s,t regular,

form the actual liberation defect on M:

    F_i(u;s,a,b,t)z=s A_i^M(bz)-a A_i^M(tz).                (4)

Every input is in the specified original closure domain.
C_F0034 says (4) is closable; when finite-rank, its closure is a unique bounded finite-rank operator.
It also supplies fraction independence and inverse closure.
By (2), every u in F has such finite defects for every pair.

Whenever the defects for a fixed i are finite, put

    eta_i(u)=s^-1 Theta^-1(F_i(u;s,a,b,t)) t^-1 in U tensor U. (5)

This is independent of the pair.
Indeed the common-multiple identity from C_F0034 is y F_i(new) y'=x F_i(old) x', with xs=ys_new and t x'=t_new y'.
Applying Theta^-1 and cancelling the regular outside coefficients in U proves equality in (5).

On the finite-defect algebra, eta_i is a derivation.
Addition follows from common denominators.
For completeness, use the C_F0034 product notation: a1 s2^-1=x^-1 y, t1^-1 b2=p q^-1, so x a1=y s2 and t1 p=b2 q.
The product pair is ((x s1),y a2,b1 p,(t2 q)), and its defect is

    F_product=x F_1 p+y F_2 q.

Multiplying its tensor by (x s1)^-1 and (t2 q)^-1 gives precisely eta_i(u1) u2+u1 eta_i(u2).
The inverse pair (a,s,t,b) gives defect -F, hence eta_i(u^-1)=-u^-1 eta_i(u)u^-1.
Constants have zero defect.

For each rational expression, recursively form its formal derivative by the polynomial Leibniz and inverse rules.
The proved derivation and inverse rules for eta_i show that eta_i(u) is i B_i applied to this formal tensor.
Since B_i is injective on U tensor U by Section 2, the formal tensor is independent of the rational expression chosen for u.
This defines the rational derivation internally, without an additional localization theorem.
Equation (2) therefore gives

    eta_i(u)=i B_i partial_i^rat u,  u in F.                (6)

The inner operator B_i commutes with the outer actions, so it indeed composes with the rational derivation as a derivation.

For any fraction pair of any u in F, (5)-(6) imply

    B_i [s (partial_i^rat u) t]=(1/i)Theta^-1(F_i).         (7)

The left bracket is an algebraic affiliated tensor.
The right side lies in H tensor_alg H.
Section 2 therefore proves the strong conclusion

    s (partial_i^rat u) t in H tensor_alg H                 (8)

for every bounded fraction pair, even when u is unbounded.
This argument uses the actual liberation defects and does not assume any all-M bound or domain inclusion for the original D_i.

## 4. The intrinsic criterion and its exact convention

There is first a densely defined test-functional realization for EVERY affiliated u and chosen bounded fraction pair.
On M tensor_alg M define the conjugate-linear functional

    Gamma_i(p tensor q*)=<p,F_i(u;s,a,b,t)q>, p,q in M.

Here F_i is still its actual operator on M from (4); no boundedness or finite rank is presupposed.
Complex linearity of F_i and the Hilbert inner product make this a well-defined conjugate-linear algebraic tensor functional.
The normal operator B_i on the Hilbert tensor product is injective with dense range; so is its adjoint B_i*.
Thus

    Test_i=B_i*(M tensor_alg M)

is Hilbert dense.
Define on exactly this dense space

    R_i(B_i* z)=(1/i) Gamma_i(z).                           (9a)

Injectivity of B_i* makes the definition unambiguous.
This is an explicit densely defined distributional regular commutator, constructed solely from the actual original liberation closures and the specified fractions.

Saying that R_i has a finite-rank representer means that there exists k_i in H tensor_alg H with R_i(w)=<w,k_i> for every w in Test_i.
Such a representer is unique by density.
Indeed, using the linear-second inner-product convention,

    <B_i* z,k_i>=<z,B_i k_i>=(1/i)Gamma_i(z).

Testing all p,q in M says exactly that the densely defined F_i has bounded finite-rank extension i Theta(B_i k_i), with the equality initially on M.

Equivalently, define K_i(u;s,a,b,t) only when (4) has a bounded Hilbert-Schmidt extension and that extension belongs to the range of the bounded injective Hilbert-Schmidt commutator map T -> i[rho(X_i),T].
In that event K_i is its unique Hilbert-Schmidt inverse:

    i[rho(X_i),K_i]=F_i.                                   (9)

This is a closed Hilbert-Schmidt inverse convention, not an arbitrary distributional inverse.
A bounded extension of the densely defined (4), if it exists, is unique.
Thus every object in the definition is canonical for the chosen fractions and actual original liberation closures.
The finite-rank version of this definition is exactly the finite-rank representer condition for the always-defined test functional (9a).

Theorem.
Under the exact C_F0025 assumptions, u belongs to F if and only if for one bounded fraction pair every K_i in (9) exists and has finite rank.
Equivalently, every densely defined test functional (9a) has a finite-rank representer.
In that event this holds for every pair and

    K_i=Theta(s (partial_i^rat u) t).                        (10)

Proof.
The forward direction is (7)-(8) and uniqueness in Section 2.
For the reverse, put k_i=Theta^-1(K_i), z_i=s^-1 k_i t^-1.
Summing (4) and using (3) and sb=at yields the actual operator identity

    sum_i F_i=i(a P_Omega t-s P_Omega b).

Consequently (9), transported algebraically and cleared, gives

    sum_i B_i z_i=u tensor 1-1 tensor u.                    (11)

Project to U tensor_F U.
Each B_i z_i vanishes by balancing over F, hence u tensor_F 1=1 tensor_F u.
The C_F0035 algebraic equalizer gives u in F.
This also proves finite-rank fraction independence via the forward result.
The stronger numerical rank invariance can be proved from the C_F0034 common-multiple identity: inner B_i commutes with outside bounded multipliers, so injectivity makes the corresponding K identities hold; bounded regular left and right cancellation preserves a finite rank.
QED.

No all-M domain for D_i, no original normal contraction estimate, and no entrywise-L2 premise on a matrix inverse occurs in this intrinsic theorem.

## 5. Original-operator compatibility and the remaining boundary

For a polynomial p, the actual identity on P uses the normalized original dual contraction E_i0, not the possibly unnormalized D_i0:

    A_i0 p=i(rho(X_i)E_i0 p-E_i0(rho(X_i)p)+p).             (12)

Thus liberation is constructed from the original normal dual by its explicit C_F0025 normalization on the original domain; it is not auxiliary tuple data.
For bounded f, its normalization-invariant weak original form beta_i(f), tested against polynomials, satisfies the Jacobi identity whose commutator by rho(X_i) is (1/i)[A_i,f].
The finite tensor in (10) has the same commutator whenever f is rational.

This observation ALONE does not identify beta_i(f) with (10): a general unbounded sesquilinear form commuting with rho(X_i) is not covered by the finite-tensor injectivity lemma.
The separate compressed minimal-state graph argument currently being authored by counterexample is designed to prove actual original coarse-domain membership and close this bounded compatibility step.
It is not assumed as an already proved premise here.

There is a second, stronger boundary for an unbounded u with arbitrary bounded s,a,b,t.
The raw expression s D_i(bz)-a D_i(tz) is defined on those z for which bz,tz lie in Dom D_i.
Neither density of this intersection nor its being a suitable common graph core has been proved here.
In particular (9) is an explicit intrinsic deconvolved realization, and this note does NOT claim that its K_i agrees on every raw composition-domain vector with that expression.
No enlargement of the original D_i is silently made.

The intrinsic iff criterion is complete as stated.
Equivalence to the literal raw-composition interpretation requires a separate compatibility theorem.
The current T_F0001 contract expressly permits a modified criterion when it is stated and compared explicitly; whether this intrinsic construction fulfils that contract belongs to its separate full contract assessment.
The raw-composition distinction remains visible even if the bounded weak companion is subsequently completed.

In the stronger cases where original D_i and D_i* have their proven all-M infinity-to-L2 bounds, the bounded strong approximation argument extends (12) and its adjoint identity to M after normalization; adding or subtracting right multiplication by eta_i0 does not change the cleared operators.
For arbitrary fractions all raw terms s D_i(bq)-a D_i(tq) are then defined on M.
Their weak Jacobi calculation gives (9a).
Whenever the raw cleared operator has a Hilbert-Schmidt extension, its tensor is a representer of (9a) and hence equals the intrinsic K_i.
In particular the established finite-rank criterion under those stronger hypotheses is recovered with exactly the same cleared operators.
We do not use this stronger hypothesis in Sections 1--4 or infer it for a general correlated normal tuple.

## Appendix A. Automatic actual liberation contractions

This appendix supplies the analytic construction used in Section 1 under exact C_F0025 assumptions.
The following mathematical body is reproduced from the already independently reviewed general-liberation proof.
All its duals are contractions of the normalized original derivation; the normalization and cancellation for the specified original D_i0 are handled in Section 1.
Fix i, write X=X_i, partial=partial_i, xi=partial*(1 tensor 1), and let I_(a tensor b)(v tensor w)=va tensor bw denote the inner bimodule action.
The bounded inner multiplier B=I_(X tensor 1-1 tensor X) commutes with the outer M-actions.
Set

`L=B partial`, `delta=i L`, `T0=(id tensor tau)delta`.

The normal phase identity gives, for both a=X and a=X*,

`L(a)=a tensor 1-1 tensor a`.

On all other starred generators L vanishes.
Consequently delta has algebraic polynomial-tensor values.
It is real for ordinary flip-adjoint: delta(p*)=(delta p)^dagger.
This follows on the generators and then by the outer Leibniz rule.
No iterated phase approximation is needed for delta.

The original polynomial-tensor adjoint formula for partial gives

`partial*(X* tensor 1)=X* xi-1`,
`partial*(1 tensor X*)=xi X*-1`.

Both correction terms use partial^dagger(X*)=1 tensor 1.
Therefore the actual vacuum is

`zeta=delta*(1 tensor 1)=-i[X*,xi]`.

In particular it is in L2; reality implies zeta=zeta*.
The same standard Leibniz calculation puts P tensor_alg P in Dom delta*, proves closability, and gives the actual core formula

`T0* p=p zeta-T0 p`, `p in P`.

Let kappa(a tensor b)=a tensor 1 tensor b.
Exactly as in C_F0043, the difference of the two iterates is an outer derivation, because its two mixed product terms cancel.
On each of X,X* it equals -kappa L, while on other generators it is zero.
Thus the exact algebraic identity is

`(delta tensor I)delta-(I tensor delta)delta=i kappa delta`.

Since T0(P) is contained in P, all the following are original algebraic domain calculations:

`T0^2 p=(id tensor tau)((delta p) dot zeta)+i T0 p`,

`||T0 p||2^2=2 Re<T0 p,p zeta>`
`             -<delta(p* p),1 tensor zeta>-<i T0 p,p>`.

Taking real parts makes the second equality a real equality if desired.
Its extension to analytic-core unitaries uses the same differentiated binomial series as C_F0043 Section 3.2; it depends only on the last displayed expression and first derivative graph convergence.
Hence

`||T u||2<=2||zeta||2+1`

for u=a+i sqrt(1-a^2), a=a* in P, ||a||<1, and also for u*.
Averaging, rescaling selfadjoint elements, and splitting real and imaginary parts give

`||T0 p||2<=(4||zeta||2+2)||p||`,
`||T0* p||2<=(5||zeta||2+2)||p||`, `p in P`.

C_F0027's bounded Kaplansky/weak-closed-graph argument therefore gives

`M subset Dom closure(T0) intersect Dom T0*`

with those same two bounds.
This is a conclusion about the actual original liberation contraction and its adjoint, not a chosen extension.
It holds for arbitrary joint laws under C_F0025; freeness and special spectral geometry are not used.
More abstractly the same proof works for any algebraic liberation derivation with an actual L2 vacuum.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-29T00:17 |
| status | open |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#liberation-intrinsic-affiliated-criterion) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: Under the exact original normal polynomial-core hypotheses, actual liberation closures define dense tensor-test regular commutators for every affiliated element and arbitrary bounded fractions.
Finite-rank representability is equivalent to membership in the original unstarred division closure, with fraction and numerical-rank independence.
The intrinsic realization is explicitly distinguished from unproved literal raw composition domains.

### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-29T00:20 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#liberation-intrinsic-affiliated-criterion) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original normal-core derivations, actual vacua, normalization, maximal Delta and the embedded unstarred free field. |
| dependency | [Exact material](Yin_C_F0027_v1.md#decision-candidate-0002) | Recover the original liberation closure and adjoint on all bounded vectors from their two polynomial-core estimates. |
| dependency | [Exact material](Yin_C_F0043_v1.md#decision-candidate-0002) | Real controlled-defect energy calculation and analytic-unitary argument, fully specialized to liberation in Appendix A. |
| dependency | [Exact material](Yin_C_F0034_v1.md#decision-candidate-0002) | Closability, finite-rank extensions, common fractions and inverse-closed finite-defect algebra for the actual all-M liberation contractions. |
| dependency | [Exact material](Yin_C_F0035_v1.md#decision-candidate-0002) | Algebraic balanced-tensor equalizer over the embedded division ring in the reverse implication. |
| review | [Exact material](../audits/reviews/Yin_R_F0034_v1.md) | Whole permanent main proof and Appendix A: actual original liberation all-M domains, algebraic finite-support deconvolution, fraction-independent affiliated derivation, rational expression independence, all affiliated elements and arbitrary bounded fractions, actual dense tensor tests, both criterion implications, numerical rank independence and stronger-domain compatibility. The literal arbitrary raw composition-domain assertion remains unproved; Task completion is separately audited. |

Recorded mathematical summary: Under the exact original normal polynomial-core hypotheses, actual liberation closures define dense tensor-test regular commutators for every affiliated element and arbitrary bounded fractions.
Finite-rank representability is equivalent to membership in the original unstarred division closure, with fraction and numerical-rank independence.
The intrinsic realization is explicitly distinguished from unproved literal raw composition domains.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision theorem-role

| Field | Value |
| --- | --- |
| date | 2026-10-15T01:47 |
| status | proved |
| authority | Explicit user instruction to designate C_F0063 as a theorem. |
| reason | Designate the existing intrinsic affiliated-rationality result as a theorem. Retain exactly the statement, argument, dependencies, independent review and domain limitations selected by decision-candidate-0002. This role designation adds no new mathematical claim or review. |

Recorded review label: independently reviewed.
Role designation: theorem.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#liberation-intrinsic-affiliated-criterion) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original normal-core derivations, actual vacua, normalization, maximal Delta and the embedded unstarred free field. |
| dependency | [Exact material](Yin_C_F0027_v1.md#decision-candidate-0002) | Recover the original liberation closure and adjoint on all bounded vectors from their two polynomial-core estimates. |
| dependency | [Exact material](Yin_C_F0043_v1.md#decision-candidate-0002) | Real controlled-defect energy calculation and analytic-unitary argument, fully specialized to liberation in Appendix A. |
| dependency | [Exact material](Yin_C_F0034_v1.md#decision-candidate-0002) | Closability, finite-rank extensions, common fractions and inverse-closed finite-defect algebra for the actual all-M liberation contractions. |
| dependency | [Exact material](Yin_C_F0035_v1.md#decision-candidate-0002) | Algebraic balanced-tensor equalizer over the embedded division ring in the reverse implication. |
| review | [Exact material](../audits/reviews/Yin_R_F0034_v1.md) | Whole permanent main proof and Appendix A: actual original liberation all-M domains, algebraic finite-support deconvolution, fraction-independent affiliated derivation, rational expression independence, all affiliated elements and arbitrary bounded fractions, actual dense tensor tests, both criterion implications, numerical rank independence and stronger-domain compatibility. The literal arbitrary raw composition-domain assertion remains unproved; Task completion is separately audited. |


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:18 |
| status | proved |
| authority | Explicit user instruction to designate C_F0063 as a theorem. |
| reason | Select the actual whole-proof finding with its disclosed mathematical contribution and independent-coverage limit. Preserve the proved intrinsic theorem, explicit theorem role, human authority, original dependencies and all historical decisions; no new mathematical review or Task disposition is asserted. |

Role designation: theorem.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#liberation-intrinsic-affiliated-criterion) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original normal-core derivations, actual vacua, normalization, maximal Delta and the embedded unstarred free field. |
| dependency | [Exact material](Yin_C_F0027_v1.md#decision-candidate-0002) | Recover the original liberation closure and adjoint on all bounded vectors from their two polynomial-core estimates. |
| dependency | [Exact material](Yin_C_F0043_v1.md#decision-candidate-0002) | Real controlled-defect energy calculation and analytic-unitary argument, fully specialized to liberation in Appendix A. |
| dependency | [Exact material](Yin_C_F0034_v1.md#decision-candidate-0002) | Closability, finite-rank extensions, common fractions and inverse-closed finite-defect algebra for the actual all-M liberation contractions. |
| dependency | [Exact material](Yin_C_F0035_v1.md#decision-candidate-0002) | Algebraic balanced-tensor equalizer over the embedded division ring in the reverse implication. |
| review | [Original finding](../audits/reviews/Yin_R_F0034_v1.md#permanent-whole-independent-review-intrinsic-affiliated-criterion) | Self relationship for the corrected permanent theorem and Appendix A, with the reviewer-supplied weak-cluster replacement for the all-M sum step; original arbitrary raw-domain boundary retained. |


### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:17 |
| status | proved |
| authority | Explicit user instruction to designate C_F0063 as a theorem. |
| reason | Adopt the actual newly isolated whole-proof inspection of the unchanged intrinsic theorem and Appendix A, including the weak-cluster all-M sum and complete affected reverse criterion. Preserve the theorem role, human authority, dependencies and exact original-domain/conditional compatibility limits; no Task completion or raw-domain extension is asserted. |

Role designation: theorem.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#liberation-intrinsic-affiliated-criterion) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original normal-core derivations, actual vacua, normalization, maximal Delta and the embedded unstarred free field. |
| dependency | [Exact material](Yin_C_F0027_v1.md#decision-candidate-0002) | Recover the original liberation closure and adjoint on all bounded vectors from their two polynomial-core estimates. |
| dependency | [Exact material](Yin_C_F0043_v1.md#decision-candidate-0002) | Real controlled-defect energy calculation and analytic-unitary argument, fully specialized to liberation in Appendix A. |
| dependency | [Exact material](Yin_C_F0034_v1.md#decision-candidate-0002) | Closability, finite-rank extensions, common fractions and inverse-closed finite-defect algebra for the actual all-M liberation contractions. |
| dependency | [Exact material](Yin_C_F0035_v1.md#decision-candidate-0002) | Algebraic balanced-tensor equalizer over the embedded division ring in the reverse implication. |
| review | [New complete isolated finding](../audits/reviews/Yin_R_F0059_v1.md#whole-intrinsic-proof) | Actual complete statement, Sections1–5 and Appendix A, all necessary accepted interfaces, weak-cluster repair, finite-tensor and Hilbert uniqueness, every bounded pair, equalizer reverse implication and exact conditional original-operator boundary; no new full-source or Task-completion review. |

## Recorded review scopes

Whole permanent main proof and Appendix A: actual original liberation all-M domains, algebraic finite-support deconvolution, fraction-independent affiliated derivation, rational expression independence, all affiliated elements and arbitrary bounded fractions, actual dense tensor tests, both criterion implications, numerical rank independence and stronger-domain compatibility.
The literal arbitrary raw composition-domain assertion remains unproved; Task completion is separately audited.

Review: [Exact material](../audits/reviews/Yin_R_F0034_v1.md).

Material covered by that review: [Exact material](Yin_C_F0063_v1.md).

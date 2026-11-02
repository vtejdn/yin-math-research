---
author: Yin
---

# Polynomial-core and normal dual domains

## Current decision

[Selected recorded decision](#decision-candidate-0001)

## Yin_T_F0005: Polynomial-Core and General Normal Dual Domains

<a id="contract"></a>
<a id="yin_t_f0005"></a>

Origin and authorization: user-assigned, 2026-09-11.
The user selected all questions in groups I and II and question 7 in group III of the earlier numbered research discussion, with polynomial domains the priority in group I.
Current state: active.
This goal owns questions 1-4; it does not reopen the completed, narrower Yin_T_F0002 contract.

## Execution boundary

Current local family boundary: `execution/Yin_E_F0005.md`.

## Exact Questions and Priority

Work in a finite tracial von Neumann algebra (M,tau) with faithful normal probability trace, H=L2(M,tau), vacuum Omega, and a bounded normal tuple X generating M.
Keep A_X=C<X> separate from the starred polynomial test algebra P_X=C<X,X*>.
Rational closures in this goal use A_X, without adjoining extra adjoints.

1. **Q1: analytic spectral arcs on small modules.**
   Extend Yin_C_F0039's automatic adjoint-module conclusion from E=M to arbitrary dense left M-modules E for closable normalized duals.
   A concrete test is X_j=S_j+i epsilon_j S_j^2, with S_j selfadjoint and epsilon_j nonzero real.
   No bounded reference dual is assumed.
   State and justify the domains and convergence of the infinite paired-operator correction.
2. **Q2: general spectral phases.**
   Determine whether the projectively summable conjugate-phase assumption can be removed, initially even on E=M.
   The normal divided-difference kernel is (conj(z)-conj(w))/(z-w), off the null diagonal.
   Identify a replacement mechanism or a counterexample satisfying the actual remaining dual assumptions, including normal spectra beyond lines and circles.
3. **Q3: starred polynomial domains, primary priority.**
   Starting with the exact [Yin_C_F0025](../claims/Yin_C_F0025_v1.md#yin_c_f0025) hypotheses on D_i with domain P_X Omega, vacuum in the Hilbert-adjoint domain, [D_i,X_j]=delta_ij P_Omega, and compact starred-generator commutators (automatically Hilbert-Schmidt there), prove or refute the missing converse: every bounded element of Div_{L0(M)} A_X has bounded finite-rank representatives of the core weak commutator forms.
   Also seek a compatible full affiliated-fraction criterion using these small domains, proving fraction independence and all necessary domain statements.
   The exact ACSY24 derivation formulation is an important sufficient input to compare, not an excuse to assume an M-module domain.
   Separate bounded weak-form representability, literal commutators, closed-domain invariance and adjoint-core assertions.
   Keep any revised criterion explicit rather than declaring these different assertions equivalent without proof.
4. **Q4: replacements for density.**
   Find useful separation/compatibility hypotheses for nondense test spaces, including factor-specific tests or jointly total compatible families with uniform finite-rank control.
   Yin_C_F0084 rules out merely omitting an arbitrarily small positive-trace component.
   Do not silently assign a single-valued Hilbert adjoint to a nondensely defined operator.

Q3 has first priority.
Q1, Q2 and Q4 remain authorized; partial cases and failed stronger routes are retained as such.
The starred polynomial domain is dense in H but generally is not a left M-module.
The selfadjoint case is a useful baseline, not a replacement for the normal target.

## Completion Criteria

Track Q1-Q4 separately.
Completion requires a proof, an exact counterexample, or a justified classification resolving each recorded question at its stated scope, with independent review of new mathematical deductions.
Useful sufficient conditions and obstructions count as progress; they do not silently discharge the broader quantifiers.
Partial mathematical outcomes do not complete this exploratory program.


## Related Records

Latest reviewed Q3 continuation, 2026-09-11: [Yin_C_F0049](../claims/Yin_C_F0049_v1.md#yin_c_f0049), with [complete review](../audits/reviews/Yin_R_F0024_v1.md), removes the C1 density assumption from Yin_C_F0048.
Every merely measurable density bounded above and bounded away from zero, with angular mean one relative to the radial reference law, has the same vacuum equivalence and quantitative estimate.
Annular localization supplies the rough inverse-density tests in the original global graph.
Arbitrary positive-radius atoms are allowed; Yin_C_F0045 gives the free-product consequence.
Arbitrary angular measures and correlated tuples remain open.

Latest nonradial Q3 scope, 2026-09-11: [Yin_C_F0048](../claims/Yin_C_F0048_v1.md#yin_c_f0048), with [complete review](../audits/reviews/Yin_R_F0022_v1.md), treats densities bounded above and bounded away from zero relative to a rotational law, with angular mean one.
A real C1 representative off zero makes the original vacuum-adjoint condition imply the radial midpoint criterion and the marginal infinity-to-2 estimate.
The sufficient transfer permits merely measurable densities and constructs the actual new vacuum vector.
Arbitrary positive-radius atoms are included.
Yin_C_F0045 then restores both original all-M domains for freely independent such normal coordinates.
General angular measures and correlated tuples remain unresolved.

Latest radial Q3 scope, 2026-09-11: [Yin_C_F0047](../claims/Yin_C_F0047_v1.md#yin_c_f0047), with [complete review](../audits/reviews/Yin_R_F0025_v1.md), removes the radius-nonatomicity restriction of Yin_C_F0046.
Every rotational normal law satisfying the exact core vacuum condition has the required marginal estimate, including arbitrary circle/diffuse mixtures.
A quantile identity supplies the same-circle correction; a countable Haar-circle example has an unbounded Hilbert dual.
Yin_C_F0045 gives both original all-M domains for freely independent such coordinates.
The original nonradial and correlated-tuple targets remain open.


Reviewed radial Q3 class, 2026-09-11: [Yin_C_F0046](../claims/Yin_C_F0046_v1.md#yin_c_f0046), with [complete independent review](../audits/reviews/Yin_R_F0077_v1.md#original-f0053-account), derives the marginal infinity-to-2 estimate from the exact vacuum-adjoint condition for rotationally invariant laws with nonatomic radius distribution.
Yin_C_F0045 then restores both original all-M domains for freely independent such normal coordinates.
Power-density examples violate linear growth and have unbounded Hilbert duals, so this genuinely extends the geometric sufficient class.
Arbitrary nonradial measures and correlated tuples remain unresolved.

Reviewed Q4 family interface, 2026-09-11: [Yin_C_F0110](../claims/Yin_C_F0110_v1.md#yin_c_f0110), with [complete independent review](../audits/reviews/Yin_R_F0120_v1.md#original-f0047-account), replaces individual domain density by collectively total left-module families and explicit cross-adjoint pairings.
Uniform rank of mixed local test matrices is equivalent to the full affiliated criterion; no local operator-norm bound is added.
Every individual window and the algebraic aggregate can be proper.
This supplies the requested compatible-family alternative in Q4, while retaining aggregate density and leaving non-total factor tests and Q1-Q3 open.


Latest reviewed free-product Q3 step, 2026-09-11: [Yin_C_F0045](../claims/Yin_C_F0045_v1.md#yin_c_f0045), with [complete independent review](../audits/reviews/Yin_R_F0023_v1.md), lifts marginal infinity-to-2 estimates to both original all-M domains for freely independent normal coordinates.
The full original starred core decomposes as orthogonal right marginal modules; the actual adjoint decomposes as well, and the complex little Grothendieck inequality controls mixed words.
Yin_C_F0044's geometric marginal class consequently gives full free-normal examples without analytic parametrization.
The original unstarred affiliated criterion is restored.
Automatic estimates for arbitrary marginals and correlated tuples remain open.

Latest reviewed geometric Q3 step, 2026-09-11: [Yin_C_F0044](../claims/Yin_C_F0044_v1.md#yin_c_f0044), with [complete independent review](../audits/reviews/Yin_R_F0076_v1.md#original-f0052-account), gives both original dual and adjoint domains on a specified coordinate algebra whose marginal has linear growth and finite total Menger curvature.
Positive reweighting of the exact Tol17 identity gives a global infinity-to-2 estimate.
For d=1 this is an all-M domain result, with canonical scalar examples.
For a tuple it controls only the individual marginal algebras.
The exact vacuum hypothesis supplies a distributional density; automatic truncation control and mixed-word bounds remain separate.
Linear growth is explicitly shown not automatic.

Earlier reviewed Q3 advance, 2026-09-11: [Yin_C_F0043](../claims/Yin_C_F0043_v1.md#yin_c_f0043) and [its complete independent review](../audits/reviews/Yin_R_F0075_v1.md#original-f0041-account) settle unitary tuples and coordinatewise univalent analytic closed curves under the exact Yin_C_F0025 bare starred-polynomial-core hypotheses.
The real unitary derivative has a controlled nonzero coassociativity defect; graph inverse calculus and two-boundary Cauchy integration recover both original all-M domains.
The original unstarred A_X remains the rational algebra.
Together with Yin_C_F0042 this covers arcs and closed curves in their stated separate coordinate parametrizations; arbitrary normal spectra and Q1/Q2/Q4 remain open.

Latest reviewed Q1 advance, 2026-09-11: [Yin_C_F0104](../claims/Yin_C_F0104_v1.md#yin_c_f0104), with [complete independent review](../audits/reviews/Yin_R_F0114_v1.md#original-f0040-account), makes Yin_C_F0102's weighted orbit estimates automatic under either a bounded commutator of the original closed dual with right S_i, or a dense left submodule invariant under all right smooth functions of S_i.
It uses the canonical analytic Chebyshev expansion and retains the original adjoints.
The quadratic graph has an explicit bounded correction with norm at most 2 abs(epsilon_i) times the right-commutator norm.
No commuting projection window or coefficient smallness is assumed, but the new right-domain premises are not yet automatic from arbitrary E.
Q1 remains open at its full scope, and Q3 remains the primary bare-core target.

Progress checkpoint, 2026-09-11: [Yin_C_F0040](../claims/Yin_C_F0040_v1.md#yin_c_f0040) and its [independent review](../audits/reviews/Yin_R_F0070_v1.md#original-f0055-account) resolve the bare-core reduction for X_i=S_i+i g_i(S_i), real polynomial g_i, without coefficient smallness or assumed freeness.
This is a Q3 subcase.
The subsequent [Yin_C_F0041 analytic-graph extension](../claims/Yin_C_F0041_v1.md#yin_c_f0041), independently reviewed in [its audit](../audits/reviews/Yin_R_F0074_v1.md#original-f0036-account), replaces real polynomial g_i by functions real on a compact interval and holomorphic nearby.
It proves equality of the original closure with the auxiliary selfadjoint-core closure, without assuming the two polynomial algebras coincide.
The further [Yin_C_F0042](../claims/Yin_C_F0042_v1.md#yin_c_f0042), with [complete independent review](../audits/reviews/Yin_R_F0072_v1.md#original-f0035-account), covers every coordinate with one holomorphic injective parametrization on a neighborhood of its compact real parameter interval.
Runge/Cauchy graph approximation now removes even the inclusion of the auxiliary polynomial algebra in the original core; the original operator closures and adjoints are still recovered.
Closed curves and arbitrary normal spectra remain separate.
The accompanying [Yin_C_F0102 local-orbit criterion](../claims/Yin_C_F0102_v1.md#yin_c_f0102) gives automatic actual adjoint modules under a weighted local estimate, automatically satisfied by coordinate-commuting large projection windows.
Its reviewed cancelling-block example obstructs arbitrary tensor-representation continuity, not Q1 itself.
General dense-module arcs, Q2/Q4 and arbitrary normal spectra remain unresolved.

- [Yin_S_F0011](../strategies/Yin_S_F0011.md#s_f0011): primary polynomial-core route.
- [Yin_S_F0015](../strategies/Yin_S_F0015.md#s_f0015): companion normal-phase and density questions.
- [Completed Yin_T_F0002 outcomes](Yin_T_F0002_v1.md#reviewed-outcomes-2026-09-11); [Claim index](../claims/index.md).

## Retained mathematical frontier

The original targets retain these boundaries:

- Q1-Q2: the additional right-domain conditions in Yin_C_F0104 and the restricted spectral classes do not resolve arbitrary dense modules or general normal phases.
- Q3: the measurable-density continuation removes the C1 density assumption from Yin_C_F0048, retaining uniform positive angular comparison.
  Yin_C_F0045 supplies the free-product lift.
  Singular angular laws, arbitrary normal measures and correlated tuples remain open.
- Q4: Yin_C_F0110 provides compatible individually nondense windows with aggregate density; it does not remove aggregate separation.
- Q5-Q6: Yin_C_F0107's actual affine L2 inverse reduction and Yin_C_F0111's restricted small-q charge results leave general multivariable rational L2 boundedness and bounded division closure open.
- Q7: Yin_C_F0106 settles finite-dimensional free factors; the diffuse free-product question remains open.
- Separate strong-Atiyah question: no result here proves strong Atiyah for every finitely generated torsion-free group.
- Historical graph-results discussion: the earlier account reported real/complex graph results, general-K Theorems 1.6-1.7 and an additional-sofic Qbar case as established at their reviewed scopes, while retaining a coefficient-interface gap in the original general-K graph conclusions.
  This Task identifies no exact source or local proof home for those theorem numbers; the report supplies neither a local Task identity nor a selected mathematical input.

A proposed candidate, neither proved nor independently reviewed, is to replace global density bounds by bounds on each fixed annulus.
The local cutoff argument might supply marginal estimates on bounded functions supported away from zero.
A localized version of Yin_C_F0045 could then aim for actual domains on left modules M e_(i,n), with common projection intersections providing a dense left module.
It still requires a complete proof of the free-prefix estimate, original dual/adjoint graph recovery, generator commutators and compatibility with the existing affiliated criterion.
No all-M conclusion or Claim is assigned to this candidate.

The target questions themselves have not been narrowed or marked complete.

## Contract History

- 2026-09-11: registered after the user clarified the selection as original questions 1-7; restored the original numbered list through this thread's read-only history.
  The new instruction expressly prioritizes polynomial-only domains, superseding the earlier choice not to prioritize that target for the completed intermediate-domain round.
  It does not erase the earlier results or authorize manuscript theorem designation, lemma extraction, commit or publication.


## Lifecycle and completion


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | active |
| authority | Origin and authorization: user-assigned, 2026-09-11. The user selected all questions in groups I and II and question 7 in group III of the earlier numbered research discussion, with polynomial domains the priority in group I. Current state: active. This goal owns questions 1-4; it does not reopen the completed, narrower Yin_T_F0002 contract. |
| reason | Preserve the original recorded active disposition and its unchanged contract scope; the recording timestamp is not an inferred historical activation or completion date. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Exact material](#contract) | Exact original contract and success conditions retained in this material. |

---
author: Yin
---

# Independent internal review: Yin_C_F0051 upper-density transfer

Review completed: 2026-09-16T13:13.
Human record author: Yin.
Reviewer: separately organized Codex research subagent the reviewing agent; the proof was developed by another research subagent following the coordinator's proposal.

Reviewed Claim: [Yin_C_F0051_v1](../../claims/Yin_C_F0051_v1.md#decision-candidate-0001).
Selected statement and complete supporting argument: [Yin_C_F0051_v1.md](../../claims/Yin_C_F0051_v1.md#upper-density-normal-core-transfer), Sections 1--6.
No earlier auxiliary proof is additionally selected as support for this Claim.

Consumer scope: the original normal polynomial-core domain question.
This is authorization/scope provenance, not a logical proof dependency.

**Verdict: pass for the complete stated sufficient-direction result, the actual marginal identities and domains, the original free-tuple polynomial weak-form equivalence and affiliated-fraction criterion, and the explicit unbounded-dual example.**
The independent radial assumption `A in L2(sigma)` is essential to the stated scope.
No necessity theorem or unrestricted normal-tuple conclusion is accepted or inferred.

## 1. Review arrangement and input disclosure

The reviewer did not develop, write, edit, or advise the proof under review.
Before this assignment, the reviewer had investigated the separate original-closure bridge for C_F0050 and reviewed that Claim's local-domain result.
That work provided familiarity with the polynomial/core distinctions and the shared earlier inputs; it did not supply or verify this upper-density transfer in advance.
The coordinator supplied this complete proof, its intended scope, and requested review targets.
The reviewer read the full target and formed initial findings before consulting the earlier C_F0048 review for comparison.
The earlier C_F0045 review and the shared direct proof interfaces had already been read during the C_F0050 work and were reused at their recorded scopes.
This is a separately organized internal AI review with disclosed context, not blind review, external human review, or independence inferred merely from using a different agent.

The review rechecked the direction of every norm comparison, actual adjoint membership, bounded polynomial approximation and both original graphs, the full C_F0045/C_F0024 consumer interface, and the explicit example.
It then compared the unchanged sufficient-direction mechanism with the earlier C_F0048 review.
No discrepancy or correction was found.
Neither the author's draft nor canonical metadata, Task files, or indexes were edited by this review.

## 2. Fixed direct dependencies and accepted-input boundary

All direct Claim inputs have repository UID `a8c6a9c0-1862-4303-917f-cd13f3e71b59`.
The exact inputs and inspected proof interfaces are:

| Fixed direct dependency | Exact use |
| --- | --- |
| [Yin_C_F0025_v1](../../claims/Yin_C_F0025_v1.md#decision-candidate-0002) | Original compact starred-core hypotheses, canonical normalization and marginal divided difference; the implication from bounded finite-rank original polynomial weak forms to affiliated rationality. |
| [Yin_C_F0024_v1](../../claims/Yin_C_F0024_v1.md#decision-candidate-0002) | All-M finite-defect criterion, fraction independence and bounded finite-rank extensions; bounded-element full-closed-domain invariance for the closure of the stated all-M restriction. Current selected criterion proof is P2; the original file supplies its authoritative statement. The ancillary P1 applications are not used here. |
| [Yin_C_F0045_v1](../../claims/Yin_C_F0045_v1.md#decision-candidate-0002) | Marginal infinity-to-2 estimate implies both original all-M domains for free coordinates; original normalization, all-M generator relations, equality of original and all-M restriction closures, and the actual free-product construction in Section 8. |
| [Yin_C_F0047_v1](../../claims/Yin_C_F0047_v1.md#decision-candidate-0002) | Radial midpoint sufficient criterion with arbitrary positive-radius atoms, the radial actual vacuum vector, infinity-to-2 bound, original bounded-function domains and adjoint identity. |
| [Yin_C_F0048_v1](../../claims/Yin_C_F0048_v1.md#decision-candidate-0002) | Section 3 sufficient-direction transfer proof and actual vacuum pairing, reconstructed in the new target after removing the unused quantitative lower-bound assumption. Its larger-hypothesis statement is not applied as a black box to the smaller hypotheses. |

C_F0049 is a comparison explaining the remaining necessity question, not a logical input.
C_F0050 and the reviewer's conditional graph-core bridge are not used by this proof.
The earlier [C_F0048 review](Yin_R_F0022_v1.md) and [C_F0045 review](Yin_R_F0023_v1.md) are accepted prior review evidence for those direct inputs, not substitutes for rechecking the new assembly.

No new external mathematical theorem is introduced.
The free-product estimate uses the existing C_F0045 source interface, including its already checked complex little Grothendieck theorem.
The target's changed-measure argument itself uses elementary Hilbert adjoints, bounded integral kernels, compact-measure continuous approximation, Stone-Weierstrass and weak closedness of closed linear graphs.
Source identification and applicability are sufficient at the accepted depths already recorded in these direct inputs; no new whole-source audit or web acquisition is claimed.

## 3. Positivity and the one-direction Hilbert comparison

The conditions `0<b<=B` almost everywhere imply that mu and nu have exactly the same null sets and therefore the same essential sup norms for measurable functions.
They do not imply an inverse L2 norm estimate, and none is used.
The only Hilbert inclusion is the bounded linear map

`I:L2(nu)->L2(mu)`, with `||I||<=sqrt(B)`.

This inclusion also preserves weak convergence.
Explicitly, for `g in L2(mu)`, the function `b g` belongs to L2(nu), because `int |b g|^2 dnu <= B int |g|^2 dmu`.
Thus every mu pairing with `I h_n` is a legitimate nu pairing against `b g`.
This verifies the potentially delicate weak-limit step without using `1/b` or an inverse inclusion.

The radius condition is probability mass on `(0,R]`, which permits zero in the topological support.
Positive-radius atoms cause no planar atoms because angular Haar measure is nonatomic.
Multiplying by b preserves this property.
Polynomial kernels are bounded off the null diagonal, so represented-polynomial definitions and all initial pairings are legitimate.

## 4. Transfer identity and the actual new vacuum vector

C_F0047 supplies both actual radial domains for every bounded function and the stated constant `a_nu`.
For polynomial p, its divided-difference kernel defines a bounded Hilbert operator `K_(nu,p)`.
Graph approximation from the specified polynomial core consequently proves that p preserves the original radial domain and

`E_nu(p h)-p E_nu h=K_(nu,p)h`.

Taking `h=b` uses its already established original radial-domain membership.
The kernel identity then gives (9), and the upper comparison yields exactly `a_mu=2 B^(3/2) a_nu`.
Both occurrences of B have the required direction; no lower bound enters.

Vacuum membership is established separately from this Banach-to-Hilbert estimate.
Since b is real and in the actual radial adjoint domain, (11) is a valid adjoint pairing on every original polynomial p.
With the inner product linear in its second variable, its representing vector is

`xi_mu=E_nu^*b-JE_nu b=b xi_nu-2J E_nu b`.

The displayed signs and conjugations are correct.
The upper inclusion and boundedness of b put this vector in L2(mu), with the bound in (12).
Thus it is the actual value `e_(mu,0)^*1`; no new extension has been selected and no vacuum vector has been inferred solely from an infinity-to-2 estimate.

Expanding the polynomial product in this actual vacuum pairing proves `e_(mu,0)^*p=p xi_mu-J e_(mu,0)Jp`.
Polynomial kernel boundedness permits the exchange of variables.
Its dense polynomial domain proves closability, and the same identity gives the stated adjoint estimate.

## 5. Actual global graph recovery and identities

For a bounded measurable f, equivalence of null sets makes it a bounded nu-measurable function with the same essential norm.
Bounded continuous approximation for the compact measure followed by uniform starred-polynomial approximation provides `p_n->f` in L2(nu), with norm bound arbitrarily close to `||f||_infinity`.
A subsequence converges nu-almost everywhere.
Upper comparison gives L2(mu) convergence, and equivalence supplies the same almost-everywhere interpretation for mu.

The two polynomial estimates bound both output sequences in L2(mu).
Taking weak subsequences in the product of their Hilbert graph spaces and using weak closedness puts f in the original closure and the actual original adjoint.
The output bounds follow by lower semicontinuity.
This argument proves the domains before making use of them in later identities.

The functions `b p_n` are uniformly bounded and converge to `b f` in L2(nu).
Pairing their actual radial images against the dense `Dom E_nu^*`, then using the uniform output bound, proves the full weak convergence (14).
The bounded inclusion I legitimately transports that weak convergence to L2(mu).
Dominated convergence gives `p_n E_nu b -> f E_nu b` strongly in both spaces.
Applying these statements to the original polynomial identity identifies the unique original value

`E_mu f=E_nu(bf)-f E_nu b`.

Likewise `p_n xi_mu -> f xi_mu` strongly in L2(mu).
The already proved all-bounded-function estimate for E_mu gives weak convergence of `E_mu Jp_n` to `E_mu Jf` by adjoint testing.
Complex conjugation preserves weak convergence as an antilinear isometry.
Weak closedness of the actual adjoint therefore gives its full bounded-function formula.
Neither the mu and nu adjoints nor the closures of arbitrary unbounded sums are identified.

## 6. Complete original free-tuple and rationality interface

The free-product application retains every original C_F0025 hypothesis, including compact starred-generator commutators and the original vacuum-adjoint condition.
C_F0025 identifies each normalized marginal core with the canonical operator treated above.
Its norm estimate is precisely C_F0045's only additional analytic hypothesis.

C_F0045 then restores both actual original all-M domains, including arbitrary mixed right-multiplier normalizations, and extends the generator relations to M.
Its closure argument is essential: the restriction to M contains the original polynomial core and lies in the original closed operator, so its closure equals that original operator.
The actual adjoints agree as well.
Thus every domain required by C_F0024 is supplied for the correct operators, not substitute extensions.

For `f in F intersect M`, C_F0024 gives the original full-domain bounded finite-rank commutator; restriction of its legitimate adjoint pairing to the original `P x P` gives the reverse direction of (16).
Conversely, the original weak-form condition implies `f in F` by C_F0025.
This second direction is retained explicitly; it is not inferred from the Hilbert density of a smaller test module.
The unstarred algebra A_X remains unchanged.

The same C_F0024 statement gives the complete affiliated-fraction criterion with all bounded fraction inputs on M, fraction independence and the unique bounded finite-rank representatives.
Its current P2 selection and closure convention were checked.
No bounded scalar rational reconstruction is added.

Finally, the construction has actual examples: the scalar vacuum just proved and the polynomial adjoint identity give valid closable marginal cores.
Their unstarred commutators equal P, while the starred phase kernel has absolute value one off the null diagonal and Hilbert-Schmidt norm one.
C_F0045's Section 8 construction thus supplies the required full starred free-product cores, rather than merely assuming their existence.

## 7. Explicit example and genuinely unbounded dual

For every parameter `2/3<beta<1`, the radial probability `beta r^(beta-1)dr` on `(0,1]` is nonatomic and has `A(r)=r^(beta-1)`.
Direct integration gives `||A||_2^2=beta/(3 beta-2)`, finite exactly at the stated lower-threshold side.
The density `b=1+(1-r)cos(theta)` is real, has angular mean one, and satisfies `r<=b<=2-r<2`.
Thus it is strictly positive everywhere on the represented positive radii and has an upper bound B=2.

Its essential infimum is zero, not merely its pointwise infimum: for any epsilon>0 choose a positive-measure radial interval with `r<epsilon/2` and a positive angular interval around pi with `1+cos(theta)<epsilon/2`.
Since `b=r+(1-r)(1+cos(theta))`, their product has b<epsilon.
Each fixed annulus still has a positive lower bound, so this particular example demonstrates failure of the former global lower bound; the theorem itself does not require even annulus-local lower bounds.

The actual vacuum and both domains follow from the proved transfer, with all hypotheses checked.
They are not inferred from the formal expression for xi alone.
Finite free products satisfy the original core hypotheses by the construction in Section 6 above.

For a hypothetically bounded Hilbert extension T of the scalar canonical normalized core, density and polynomial invariance imply `[T,X]=P` on the whole Hilbert space.
For the spectral projection `e_r=1_(|X|<r)`, angular mean one gives `||e_r P e_r||=mu(|X|<r)=r^beta`.
Because e_r commutes with X and `||X e_r||<=r`,

`r^beta=||e_r[T,X]e_r||<=2r||T||`.

The ratio `r^(beta-1)` diverges as r decreases to zero, contradicting beta<1.
This proves that the specified canonical dual has no bounded Hilbert extension, while its original closed and adjoint domains still contain all bounded functions.
It does not depend on a bounded reference dual.

## 8. Acceptance and verification boundary

The entire stated proof passes internal mathematical review, and the fixed dependency and source interfaces are complete for its scope.
This is a sufficient class obtained by supplying `A in L2` independently; it does not derive that condition from the new mu vacuum hypothesis, prove a vacuum equivalence without lower bounds, settle arbitrary singular angular laws or correlated tuples, or complete the unrestricted normal-vacuum domain project.

No mathematical correction was requested.
Numerical experiments, manuscript compilation, proof-assistant verification, external human review, and novelty/priority assessment were not performed.
The proof and its dependency interfaces were checked analytically.
Canonical assessment publication, generated navigation and any later reuse remain separate actions.

---
author: Yin
---

# Independent review of the original iterated-domain bridge

Date: 2026-09-28T17:56.
Human record author: Yin.
Reviewer: the separately assigned `counterexample` research subagent.
Scope: whole mathematical review of **Yin_C_F0056_v1**, all six sections of [the permanent proof](../../claims/Yin_C_F0056_v1.md#normal-phase-original-coassociativity).
The final permanent proof was reopened.

The initial whole-proof review inspected the historical draft `tmp/t_f0001-2026-09-29/normal-coassociativity-domain-bridge.md`.

Arrangement: the reviewer did not develop this bridge and was supplied its finished text plus root's request to challenge the original tensor domains, closure argument, and estimates.
The reviewer had previously independently reviewed the scalar soft-Cauchy candidate now registered as C_F0055_v1.
That previous review and the actual C_F0025/ACSY24 interfaces are the accepted inputs here; the authoring dialogue for this bridge was not supplied.
After reading the argument the reviewer sent the author initial checks and one optional request to spell out the antiunitary justification for the conjugate iterate.

The permanent proof was compared with that scratch artifact using the complete textual diff.
Changes are its header and explicit tensor-domain conventions, the current accepted C_F0055 (recorded assessment 2) and C_F0025 (recorded assessment 3) dependency links/status, source-scope notes, and the explicit antiunitary-domain explanation for F_i^2 already checked in the initial review below.
The inequalities, graph-recovery proof, product-rule argument and conclusions are unchanged.
The added conventions and explanation were read and verified; no enlarged domain or target scope has been inserted.
Root allocated C_F0056; the reviewer changed no records or indexes.

## Verdict and exact scope

The bridge is mathematically valid given its stated scalar inputs, which are now supplied by the independently reviewed C_F0055 (recorded assessment 2) scalar result.
No freeness is needed.
The conclusion is genuine coassociativity on every original mixed starred polynomial, with both iterated expressions in their actual closed tensor domains.
It does not assert coassociativity on every vector of Dom closure(partial_i), and this review accepts no such extension.
It also does not supply a mixed-word L-infinity-to-L2 estimate or the general correlated affiliated criterion.

## Original tensor domains and bounded approximation

C_F0025 supplies the represented starred polynomial algebra, atomless marginal law, canonical phase k, and coarse derivation with an actual vacuum adjoint.
Expanding partial(a* p b*) and pairing with 1 tensor 1 puts P tensor P in the actual adjoint domain.
Thus the coarse derivation is closable.
The closed operator used in the first leg is closure(partial_i) tensor I; the algebraic domain P tensor P is a graph core for it, because the second copy of P is Hilbert dense and the first copy is the prescribed graph core.
The analogous statement holds in the second leg.

For fixed t>0, the geometric-series approximants to

    k_t(z,w)=(bar z-bar w)^2/(|z-w|^2+t)

are algebraic tensors of coordinate starred polynomials.
Their first real derivatives converge uniformly on a fixed product square.
This controls the first-variable and second-variable divided differences uniformly, so both original closed tensor graphs really contain k_t and the displayed quotient values.
The multiplicative geometric-series remainder is a real number in [0,1] on the relevant spectral support.
Hence each approximant has spatial operator norm at most one.
The coordinate spectral tensor embeds isometrically in the full tuple's coarse tensor; its graph approximation uses the same original full-tuple polynomial derivation and needs no reducing-subspace assertion for a newly chosen extension.

## The uniform triple estimate

With a=z-w, b=v-w, x=|a|^2, y=|b|^2, r=|a-b|^2, the numerator calculation is

    bar a^2(y+t)-bar b^2(x+t)
      =bar a bar b(bar a b-bar b a)+t(bar a-bar b)(bar a+bar b).

The squared first factor is x y H, where H=16 area^2, and |bar a-bar b|^2=r.
Applying |u+v|^2<=2|u|^2+2|v|^2 and |a+b|^2<=2(x+y) gives precisely the two terms in equation (4).
In the first, x/(x+t)^2<=1/x and y/(y+t)^2<=1/y give the curvature majorant.
In the second,

    t(r+t)/[(x+t)(y+t)]<=5

follows from r<=2(x+y): the contributions 2tx, 2ty, t^2 are at most 2,2,1 after division.
Thus equation (5) and the total bound

    ||L_t||2^2 <= 2(6)||eta_i||2^2+40(3)||eta_i||2^2
                =132||eta_i||2^2

are correct.
The bound is uniform as t tends to zero, including collinear triples.
The limiting phase difference has the exact squared modulus H/(x y r), so its final L2 bound is sqrt(6)||eta_i||2.
The two estimates have different purposes; the final integrability alone would not have justified the original graph limit.

## Weak and strong graph recovery

Away from all three collision diagonals, the quotients converge uniformly on each subset with distances bounded below.
Bounded tests supported on the union of such subsets are dense in the triple Hilbert space because the marginal is atomless.
Uniform L2 bounds therefore identify every weak limit with the actual second divided difference.
The first graph component tends strongly to k.
Weak closedness of the original tensor graphs consequently puts k in both actual domains and gives the stated values.

Scalar divided differences of the function z -> bar z obey the algebraic second-difference symmetry.
With the usual ordered triple legs this identifies the two outputs, including the possible collinear case.
No pointwise diagonal interpretation is needed, because those sets have product measure zero.

The simultaneous strong graph approximation is also valid.
Choose algebraic approximants for each fixed t with errors tending to zero in both graph norms; their spatial norm bound is retained.
The resulting sequence converges weakly in the product of the input and two output Hilbert spaces.
Finite convex combinations of its tails converge strongly to the same product-space limit by the Hilbert-space separation argument given in the artifact.
Convexity preserves the spatial norm bound of one.
It is important here that one common sequence approximates both iterated domains; the text supplies it.

## Mixed polynomial product rules and contracted iterates

Every partial_i p is a finite sum of spatial bounded tensors obtained by bounded polynomial outer multipliers of 1 tensor 1 or k_i.
This does not mean that k_i itself is an algebraic tensor.
Substitute the simultaneous uniformly bounded graph approximants just obtained.
For a polynomial coefficient a, partial_i a is a bounded spatial tensor, so all extra product-rule terms converge in L2 under bounded spatial multiplication.
Multipliers of the limiting triple derivative are likewise bounded.
This verifies the domains before taking limits in the formal product rules.

For a product p q, the two iterated Leibniz expansions have the same cross term, (partial_i p)_{12}(partial_i q)_{23}.
Its order is correct under the outer left/right bimodule convention; its spatial boundedness makes the term a legitimate L2 vector.
After cancellation, the associator is an outer derivation.
It vanishes on each unstarred coordinate, on the i-th starred coordinate by the recovered second-difference identity, and on the remaining starred coordinates because their i-th derivative vanishes.
Induction proves coassociativity on every mixed starred polynomial.

The further domain assertion E_(i,0)p in Dom E_i also holds.
Contract the second leg of an original graph approximation to partial_i p for closure(partial_i) tensor I.
Contracting the corresponding output's third leg commutes with differentiating the first leg.
This gives a sequence of original polynomials converging in the original coarse-derivative graph to (id tensor tau)partial_i p.
On the domain of that closed coarse derivative, contraction of its value agrees with the original contraction closure, since the same graph approximants prove that inclusion.
Applying the contraction again therefore defines E_i(E_(i,0)p) and identifies it with the stated double contraction.
This argument never assumes that the contraction's domain equals the coarse derivative's entire domain.

## Conjugate derivation, adjoints, and remaining boundary

The conjugate derivation obtained by adjoint plus tensor flip has actual vacuum xi_i*.
The phase unitary U_i is the bounded measurable ratio of an injective normal inner spectral operator's adjoint to that operator; its modulus is one off the null diagonal.
It commutes with the outer actions.
Checking both Xi and Xi* gives partial_i^dagger=U_i* partial_i on the complete starred polynomial domain, and hence

    <U_i(1 tensor 1),partial_i p>=<xi_i*,p>.

This is exactly the actual adjoint-domain test claimed for U_i(1 tensor 1).
It does not infer domain invariance from boundedness of U_i alone.

The adjoint formulas E0*p=p xi_i-F0p and F0*p=p xi_i*-E0p have the correct sign and multiplier order.
They follow by the same actual Hilbert pairing used in C_F0025, because Theta(partial(p*))^*1 is precisely the contracted conjugate derivation.
Applying Hilbert adjoint/conjugation with reversal of the triple tensor legs transfers the established coassociativity and its original-domain statements to the conjugate derivation; this also justifies the announced F_i^2 assertion.

Neither ordinary coassociativity nor these adjoint identities provides the mixed iterate E_i F_(i,0)p with the needed estimate.
The artifact explicitly retains that obligation, correctly avoiding the reality assumption used in the selfadjoint contraction theorem.
No general all-M inclusion or T_F0001 completion follows yet.

## Dependency and verification limits

The direct substantive inputs are C_F0025 (recorded assessment 3)'s canonical coarse-derivative interface and C_F0055 (recorded assessment 2)'s scalar soft-energy/curvature conclusion.
The original ACSY24 source interface is already audited; no stronger source claim is imported.
The geometric-series estimates, finite convex approximation, closed tensor graphs and all new product/domain arguments were checked in this review.
No additional external theorem with an unverified applicability premise is required.
No numerical experiment, proof-assistant verification, external human review or novelty certification was performed.

## Preserved original review timing

The initial complete review was recorded at 2026-09-28T17:47; the permanent binding above was recorded separately at 2026-09-28T17:56.
These are the original historical observations, with the original inspection scope retained.
This clarification adds no new review.

## Relationship arrangement

The retained arrangement identifies a distinct reviewer outside this bridge's development, supplied finished text and exact review scope, and expressly states that the authoring dialogue was not supplied.
The prior scalar review is a necessary fixed dependency interface, not a contribution to this new bridge.
The optional antiunitary explanation spelled out a domain justification already checked in the initial finding; no substantive gap repair or changed mathematical proof is recorded.
The existing independent relationship is retained for the exact six-section original-domain scope.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original finding](#verdict-and-exact-scope) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original finding](#verdict-and-exact-scope) | [Statement](../../claims/Yin_C_F0056_v1.md#statement) | Complete six-section original iterated-Hilbert-domain bridge, bounded geometric approximants, soft triple bound, both original weak/strong graphs, mixed starred product rules, actual squared contractions and phase adjoints; no full-domain coassociativity or correlated contraction. |
| [Original finding](#verdict-and-exact-scope) | [Complete argument](../../claims/Yin_C_F0056_v1.md#normal-phase-original-coassociativity) | Complete six-section original iterated-Hilbert-domain bridge, bounded geometric approximants, soft triple bound, both original weak/strong graphs, mixed starred product rules, actual squared contractions and phase adjoints; no full-domain coassociativity or correlated contraction. |

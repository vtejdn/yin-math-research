---
author: Yin
---

<a id="normal-mixed-energy-liberation-reduction"></a>
# Normal mixed energy and general liberation: the remaining correlated estimate

The complete liberation proof is owned by [C_F0063 Appendix A](../claims/Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions).
The full actual mixed-domain proof is also retained in [C_F0076](../claims/Yin_C_F0076_v1.md#argument), while the [C_F0078 Section 6 energy interface](../claims/Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) retains the complete actual-adjoint and analytic-unitary energy chain.
R_F0035/R_F0039 retain their original mixed-domain, conditional-energy and actual-liberation scopes; the general sufficient mixed-defect inequality remains unproved here.

Date: 2026-09-29.
Human author: Yin.
Exploration developed by another AI agent, with scoped independent mathematical review by `counterexample`.
Consumer: [T_F0001's current contract](../tasks/Yin_T_F0001_v2.md).
This is a combined exploration module, not a new Claim or a manuscript result designation.
The positive auxiliary conclusion is the general liberation contraction; the original correlated normal contraction remains conditional on the explicitly stated mixed-defect estimate.

Direct inputs are [C_F0025_v1](../claims/Yin_C_F0025_v1.md#decision-candidate-0002), [C_F0027_v1](../claims/Yin_C_F0027_v1.md#decision-candidate-0002), [C_F0043_v1](../claims/Yin_C_F0043_v1.md#decision-candidate-0002), [C_F0055_v1](../claims/Yin_C_F0055_v1.md#decision-candidate-0002), and [C_F0056_v1](../claims/Yin_C_F0056_v1.md#decision-candidate-0002).
The source/template boundaries and original-domain qualifications are retained in the two component notes below.
Their local draft status labels identify the authoring stage; the separate permanent review owns its stated scope.

## Mixed normal phase domains and the exact remaining energy estimate

Date: 2026-09-29.
Agent: another AI agent.
Status: proof/reduction draft; no new Claim allocation requested.
Uses the accepted C_F0055 scalar estimate and C_F0056 original phase-domain bridge.
This extends the latter's domain calculation, not its contraction conclusion.

## 1. All four mixed iterates have original domains

Fix i and write partial=partial_i, xi=partial* (1 tensor 1), partial^dagger(p)=(partial(p*))^dagger, with ordinary flip-adjoint dagger.
The actual vacuum of partial^dagger is xi*.
Write E0=(id tensor tau)partial and F0=(id tensor tau)partial^dagger, with their original closures E,F.

The C_F0056 approximation

`k_t(z,w)=conj(z-w)^2/(|z-w|^2+t)`

also handles conj(k_t).
Conjugating the numerator of its first-variable divided difference leaves the absolute value unchanged; replacing the denominator z-v by conj(z-v), as partial^dagger does on the coordinate algebra, also leaves it unchanged.
Thus exactly the same 132-bound applies to each of k_t and conj(k_t), for both derivations and both tensor legs.

Use the same finite geometric polynomial sums, then convexify in the product of the input Hilbert space and all relevant derivative-output Hilbert spaces.
This yields common algebraic tensor approximants, uniformly bounded in spatial norm, converging strongly in all these original graph norms.
The mixed-product argument from C_F0056 consequently proves that for every p in P all four tensors

`(partial tensor I)partial p`, `(I tensor partial)partial p`,
`(partial tensor I)partial^dagger p`,
`(I tensor partial^dagger)partial p`

and the analogous ones with partial and partial^dagger swapped are in the stated original closed tensor domains.
In particular E F0p and F E0p are actual vectors.
This says nothing about all vectors in Dom E or Dom F.

## 2. Ordinary-real components and legitimate adjoints

Set

`delta_x=(partial+partial^dagger)/2`,
`delta_y=(partial-partial^dagger)/(2i)`.

They are real for the ordinary coarse involution.
Their actual vacua are

`zeta_x=(xi+xi*)/2`, `zeta_y=i(xi-xi*)/2`,

both selfadjoint, with `||zeta_x||2^2+||zeta_y||2^2=||xi||2^2`.
The core adjoint formula and bounded polynomial derivative images prove closability separately; closability is not inferred merely from taking linear combinations of closable operators.
Put T_a0=(id tensor tau)delta_a and let T_a be its original closure, for a=x,y.
Then

`T_a0* p=p zeta_a-T_a0 p`,  `p in P`.

The graph approximation in Section 1 shows more: T_a0 p has polynomial approximants uniformly bounded in operator norm and converging in the original delta_a graph.
They are obtained by partially tracing the common bounded tensor approximants of delta_a p.
Thus they also converge in the T_a graph.
Uniform boundedness and L2 convergence imply strong multiplication on each fixed L2 vector, so their products with zeta_a converge in L2.
Closedness of T_a0* therefore gives

`T_a0 p in Dom T_a0*`,
`T_a0*(T_a0 p)=(T_a0 p)zeta_a-T_a(T_a0 p)`.                      (1)

This is the exact domain statement needed in the norm identity.

## 3. Exact sum-of-components identity

Define the actual coassociativity defects on P by

`A_a=(delta_a tensor I)delta_a-(I tensor delta_a)delta_a`,
`C3=id tensor tau tensor tau`.

Contracting their definitions and using the vacuum on the second leg gives

`T_a(T_a0 p)=C3 A_a p+(id tensor tau)((delta_a p) dot zeta_a)`.

The product on the right is an L2 tensor: delta_a p is a bounded spatial tensor.
This identity follows first on the uniformly bounded algebraic approximants from Section 1 and then in the original graphs.

Equation (1) now permits the same calculation as C_F0043 Section 3.1, retaining the exact defect term.
Taking real parts gives

`sum_a ||T_a0 p||2^2`
` = 2 Re sum_a <T_a0 p,p zeta_a>`
`   - Re sum_a <delta_a(p* p),1 tensor zeta_a>`
`   - Re <C3(A_x+A_y)p,p>`.                                    (2)

For a selfadjoint a in P with ||a||<1, the binomial series defining `u=a+i(1-a^2)^(1/2)` has polynomial approximants converging in norm and in the delta_x, delta_y, A_x, A_y graph seminorms.
Each of these is an outer derivation, so the usual power estimate is enough; no second-derivative convergence of the approximants is needed in the last line of (2).
The last line is continuous in precisely those norms, and u*u=1 has zero derivative.
Hence for these analytic-core unitaries u,

Here and in (3)--(4), A_a u means the norm-convergent value of the displayed derivation power series, equivalently the limit of A_a on these fixed polynomial approximants.
We use (2)'s last-line limit only: no closability of A_a or original iterated-domain assertion at every such u is inferred.

`V(u)^2=2 Re sum_a <T_a u,u zeta_a>-Re <C3(A_x+A_y)u,u>`,
`V(u)^2=sum_a ||T_a u||2^2`.                                   (3)

Since E=T_x+i T_y on this core, a uniform bound on V gives the desired original E contraction bound; the adjoint follows by the real core formulas.

Source boundary: the selfadjoint source calculation was freshly rechecked in Dabrowski, arXiv:0804.2906v2, printed p.9, Lemmas 10--12 (https://arxiv.org/pdf/0804.2906).
It is used as the known norm-identity mechanism, not as a theorem covering this normal tuple.
The project C_F0043 already supplies its correct unitary controlled-defect modification.

## 4. The one remaining sufficient inequality

It would suffice to prove finite constants c0,c1, depending on the full original tuple and its actual joint vacuum data, such that

`-Re <C3(A_x+A_y)u,u> <=c0+c1 V(u)`                              (4)

for every analytic-core unitary u above.
Indeed (3) then gives

`V(u)^2 <=(2||xi||2+c1)V(u)+c0`,

a uniform quadratic bound.
Applying it to u and u*, taking their average, rescaling selfadjoint core elements, then splitting real/imaginary parts recovers an infinity-to-L2 bound on the whole original polynomial core.
The existing C_F0027 original-graph argument would then recover all M domains and the full affiliated criterion for correlated normal tuples.

No proof of (4) is supplied here.
The separately drafted correlated-Haar family shows that c0,c1 cannot simply be replaced by a constant lower bound depending only on marginal laws/curvature and the operator norm.
Its actual joint vacua grow, so it does not exclude (4) with joint information.

The actual phase-adjoint identity `partial*(U(1 tensor 1))=xi*` is available.
Formally integrating a derivative of U by parts reintroduces mixed E F and F E terms; eliminating them using (2) is circular unless a further positive or lower-order term is isolated.
No automatic lower bound has yet resulted from that identity alone.


## General normal-coordinate liberation

[C_F0063 Appendix A](../claims/Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions) retains the complete actual liberation proof.
It proves the two core bounds and both original all-M domains for arbitrary joint laws, with the actual vacuum, coassociativity defect and controlled energy calculation.
The original [R_F0035](../audits/reviews/Yin_R_F0035_v1.md) and [R_F0039](../audits/reviews/Yin_R_F0039_v1.md) findings retain their original mixed-energy and liberation scopes; this reference repair performs no new review.

## Reconstruction boundary

The desired normal derivative is formally partial=B^(-1)L.
The inverse inner multiplier is singular at equal spectral coordinates and need not be bounded.
An infinity-to-L2 bound for the contraction of L supplies no bound for a contraction after arbitrary singular inner multiplication.
Replacing B^(-1) by a soft inverse gives finite constants at each regularization, but the preceding proof provides no uniform bound as the regularization tends to zero.
The mixed-curvature weighting has the same issue: finite scalar L1 mass of its weight is not a bound for a general correlated mixed word.
Thus this auxiliary result is not a proof of the remaining T_F0001 contract.

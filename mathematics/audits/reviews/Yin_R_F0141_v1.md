---
author: Yin
---
# Independent review of the singular free semicircular coordinate equivalence

Review performed and recorded: 2026-10-14T17:00.
Human record author: Yin.
This is a separately assigned AI mathematical review, not a personal human inspection.

## Arrangement and scope

The reviewer did not develop, propose or edit [C_F0134 v1](../../claims/Yin_C_F0134_v1.md).
Root supplied only the fixed candidate and the complete review assignment.
No author draft, proof-development discussion or informal explanation was read.
The candidate's development attribution and initial decision dated 2026-10-14T16:54 were visible.
The reviewer read the complete candidate and its two direct source units, then independently checked every displayed construction, actual-domain argument and necessity implication recorded below.
Earlier reviews of other candidates do not verify this proof.

This finding covers the entire statement and all seven proof sections: the precise reference-pair assumptions, generation, free weighted creation estimate, actual spectral-truncation domains and adjoints, both full-domain dual coordinates, represented starred derivations and their actual vacua, canonical bounded-vector domains, and necessity for arbitrary F and A witnesses.
It does not claim a theorem about arbitrary nonnormal coordinate changes or infer nonexistence merely from failure of a selected operator candidate.

The accepted inputs are [Dab10-U002 Sections 2-3](../literature/Dab10/Yin_U002.md#dab10-u002) and the exact free-product/semicircular interfaces in [Voi98-U005](../literature/Voi98/Yin_U005.md#voi98-u005).
Their retained source inspection and foundational limitations remain unchanged.
No new original-PDF inspection or recursive proof audit of their cited foundations was needed or performed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0134 statement](../../claims/Yin_C_F0134_v1.md#statement) | Exact hypotheses on positive regular h, its scalar L2 conjugate, standard semicircular S free from W*(h), and generation; equivalence of A, F, S and inverse L2 membership, explicit actual vacua and both canonical bounded-vector domains. |
| [Conclusion](#conclusion) | [C_F0134 argument](../../claims/Yin_C_F0134_v1.md#argument) | Complete Sections 1-7: reference and free-adjoining interfaces, weighted right creation and spectral domain, transported adjoints and signs, represented derivations, canonical graphs, and both existential necessity proofs. |
| [Conclusion](#conclusion) | [Dab10-U002](../literature/Dab10/Yin_U002.md#dab10-u002) | Sections 2-3 and their stated selfadjoint premise: scalar-conjugate free-adjoining gives the pair (xi_h,S), represented free difference quotients, the closed h-contraction, actual operator/adjoint domains containing M, constants 4 and 5, and bounded-set weak continuity. No bounded-H or Lipschitz-conjugate conclusion is imported. |
| [Conclusion](#conclusion) | [Voi98-U005](../literature/Voi98/Yin_U005.md#voi98-u005) | Pointed free-product Hilbert model and left/right end-action identities, with the standard variance-one semicircular normalization and right-creation formulas checked explicitly in the candidate. Its original selfadjoint-dual normalization is not substituted for the present transported operators. |

## Exact reference pair and generation

The pair (h,S) consists of bounded selfadjoint generators.
The scalar conjugate of h lies in L2(W*(h)); adjoining a free standard semicircular variable gives the joint conjugate system (xi_h,S), precisely the free-adjoining identity retained in Dab10-U002 Section 2.
Thus that unit supplies actual represented difference quotients on A_0=C<h,S>, rather than formal derivatives that might fail to respect represented relations.
Its Sections 2-3 supply B=closure((id tensor tau) partial_h), B1=0, B*1=xi_h, both bounded-vector domains, and the respective operator-norm-to-L2 estimates 4 norm(xi_h)_2 and 5 norm(xi_h)_2.
They do not assert B is bounded on H.

The reference generator identities extend to M exactly as stated.
For uniformly norm-bounded polynomials p_n tending to a in L2, both h p_n and S p_n are uniformly bounded and converge to h a and S a in L2.
The source's bounded-set weak continuity identifies the B-images in the core commutators with their actual B-values on M.
This uses the actual closed operator and its established domains.

For e_n=1_[1/n,infinity)(h), regularity implies e_n tends strongly to 1.
The bounded functional-calculus element h inverse e_n belongs to W*(h), and its product with Y is e_n S.
The latter converges strongly to S.
Hence W*(h,Y)=W*(h,S)=M even when the inverse is not L2.
The represented algebra A_X=C<h,hS,Sh> is therefore a dense unital star algebra.
In particular, the tuple in every implication really generates the prescribed M; generation is not postponed until the sufficient inverse-integrability case.

## Right creation and the exact weighted estimate

The reduced-word model and the Chebyshev recurrence for the variance-one semicircular law identify r as right creation, increasing the terminal semicircular degree or appending the degree-one semicircular vector.
Its images of the orthonormal reduced-word sectors are orthonormal, so r is an isometry.
On every finite reduced word, right multiplication by S equals r+r*, and r* annihilates the vacuum.
Comparing the left and right end actions gives [r*,S]=P, with the nonzero term arising on the vacuum, and [r*,a]=[r,a]=0 for every a in N.
These identities extend to H because the relevant operators are bounded.
The normalization uses S=ell+ell*, not the differently scaled semicircular convention in part of Voi98.

For bounded c in N, the range of r consists of vectors whose final reduced block is a nonvacuum semicircular block.
Right multiplication by the scalar part tau(c) preserves this terminal sector.
Appending c minus tau(c) yields terminal N sectors orthogonal to it.
On each reduced-word sector, the latter is tensor concatenation with the centered vector, giving exactly its L2 norm as the multiplier norm.
Orthogonality among the original sectors persists.
Therefore

\[
\|\rho(c)r\zeta\|_2^2
=(|\tau(c)|^2+\|c-\tau(c)\|_2^2)\|r\zeta\|_2^2
=\|c\|_2^2\|\zeta\|_2^2.
\]

Density proves this equality for every input in H.
In particular the operator norm distance between rho(c_n)r and rho(c_m)r is exactly norm(c_n-c_m)_2.
Thus L2 approximation defines the bounded C_c unambiguously.
Freeness is essential to this exact estimate; the proof does not assert it for correlated reference pairs.

When b=h inverse is in L2, take the increasing spectral truncations \(b_n=b\,1_{\{b\le n\}}\).
The bounded operators rho(b_n)r converge in norm to C_b.
For every zeta in H, spectral calculus for the positive selfadjoint right multiplier rho(b) says that convergence of its truncation values on r zeta is exactly the domain criterion.
Hence rH is contained in Dom rho(b), and rho(b)r=C_b on all H.
This proves the actual domain assertion in (7), not just convergence of a formal product.

## The transported closed operator and its actual adjoint

Define K=rho(b)r* on the candidate's full natural domain.
It is closed: convergence of zeta_n and K zeta_n gives convergence of r*zeta_n, so closedness of rho(b) applies.
Every bounded a belongs to this domain.
Indeed r*a=aS-ra, the first term belongs to M and therefore to Dom rho(b), while the second belongs there by the preceding all-H conclusion.
Consequently Ka=aSb-C_ba.

Freeness and the variance-one normalization give norm(Sb)_2=norm(b)_2: first compute the equality for spectral cuts, then use L2 convergence.
Together with the exact norm of C_b and norm(a)_2 at most norm(a), this proves the candidate's bound norm(Ka)_2 at most 2 norm(b)_2 norm(a).

For q in M, q b belongs to H and q lies in Dom rho(b).
On the entire natural domain of K, the actual pairing is

\[
\langle q,K\zeta\rangle
=\langle qb,r^*\zeta\rangle
=\langle r(qb),\zeta\rangle.
\]

Thus q belongs to Dom K* and K*q=r(qb), with the displayed bound.
Only this inclusion is used; the proof never assumes equality of the complete adjoint-product domains.
Since r commutes with left N, r b_n=b_n S.
Passing to L2 gives K*1=rb=bS, with the stated order of the factors.

Left multiplication by any bounded element commutes with the affiliated right multiplier on its domain and preserves that domain.
This justifies moving such left coefficients through rho(b) in the tested commutators on M.
The right-deletion identities then give [K,h]=0 and [K,S]=bP, where bP is a bounded rank-one map.
Multiplying by h gives [K,hS]=P because hb=1.
Every tested input is bounded and all these expressions have the established actual domains.

## Both dual coordinates and their adjoints

The domain-M operators E_Y=K|_M and E_h=B|_M-K rho(S)|_M are defined on all bounded vectors because aS is bounded.
For E_Y the identities are [E_Y,h]=0 and [E_Y,hS]=P.
For E_h, the h-commutator is P.
The other commutator cancels because

\[
[B,hS]=PS,\qquad [K\rho(S),hS]=P\rho(S)=PS.
\]

The last equality is the trace identity tau(aS)=tau(Sa), evaluated on arbitrary a in H by continuity.
It does not commute S with P.

For every q in M, testing all bounded a gives the actual adjoint values E_Y*q=K*q and E_h*q=B*q-rho(S)K*q.
All vectors on the right are in H by the previously proved domains and boundedness of rho(S).
Thus both adjoint domains contain dense M, so both supplied operators are closable.
Negating E_h and E_Y produces the generator-first S(X) witnesses.
Their nonzero possible vacuum values cause no difficulty; the definition of S does not require normalization.

## Actual represented derivations and vacuum vectors

On finite sums of bounded polynomial tensors, u tensor v mapped to u b tensor v is a well-defined linear map into H tensor H.
It commutes with the outer left and right actions because b is inserted on the right of the first factor.
The map u tensor v mapped to u tensor S v inserts S on the left of the second factor and has the same outer compatibility.
No bounded extension of the first map to the whole Hilbert tensor product is needed.

Composing these operations with the represented reference difference quotients therefore gives genuine outer derivations delta_Y and delta_h on A_0.
Using hb=1 verifies all four coordinate values in (17), including the cancellation delta_h(hS)=1 tensor S-1 tensor S=0.
Restricting to the actual star algebra A_X respects all its relations automatically.
This is a separate construction of A(X); no general S-to-A principle for nonnormal tuples is invoked.

Since r* equals the reference S right contraction on A_0, its commutator normalization proves Q_Y=K there.
The Leibniz rule gives

\[
K(pS)=(\mathrm{id}\otimes\tau)(\delta_Y(p)\cdot S)+pb.
\]

Traciality identifies the last-leg contraction after multiplication by S on the right or on the left.
Thus Q_h=B-K rho(S)+rho(b) with exactly the positive final term.
Pairing these core expressions against the vacuum, using K*1=bS and B*1=xi_h, gives the actual representing vectors

\[
Q_Y^*1=bS,\qquad Q_h^*1=\xi_h-bS^2+b.
\]

Both belong to H because b is L2 and S is bounded.
The scalar vacuum pairing of delta equals that of its right contraction; hence these are also precisely the two actual delta-adjoint vacuum vectors in the statement.
Restriction from A_0 to the dense A_X preserves these values and their uniqueness.

The domain-M extensions of both contractions are operator-norm-to-L2 bounded using the proved estimates.
Their actual adjoints contain M: this was shown for B and K rho(S), while positivity of b gives the exact right-multiplication pairing with q b for the remaining term.
The core restrictions are therefore closable and their core adjoints already contain M.
Uniformly norm-bounded Kaplansky polynomial approximants in A_X have bounded contraction images.
Weak compactness and the weakly closed graph of each specified core closure put every bounded vector in that closure's domain.
Its actual adjoint is the core adjoint and retains M in its domain.
This proves the stated canonical conclusion, without identifying its entire domain with the larger natural product domain of K.

## Necessity for every F witness

Let E=-D_Y be any bare Y-coordinate witness.
The other coordinate forces [E,h]=0 on all M; the Y coordinate gives [E,hS]=P there.
Since h and S are bounded, every intermediate input in the product expansion belongs to M, even though E's outputs need only lie in H.
Thus h[E,S]=P and

\[
h(E(S)-S E(1))=1.
\]

The bracket is an actual H vector.
Positive regular h has injective left multiplication, and the spectral equation hv=1 forces v=h inverse as an affiliated vector.
Its belonging to H therefore forces b in L2.
This proof neither normalizes E nor assumes continuity, closability or an adjoint for it.
It applies to every possible F witness, not merely to the candidate K or B-K rho(S).
Since S implies F, the same necessary condition applies to every strong system as well.

## Necessity for every A witness using polynomial tests only

For any A(X) witness, take its Y derivation and actual vacuum xi.
It vanishes on h and hence on every scalar polynomial f(h).
The legal algebraic input f(h)Y therefore has derivative f(h) tensor 1.
Its actual adjoint pairing implies

\[
|\tau(f(h))|\le\|\xi\|_2\,\|f(h)hS\|_2
=\|\xi\|_2\,\|h f(h)\|_2.
\]

The equality follows from freeness of N and S and tau(S squared)=1, using the bounded N element h f(h).
No extension of the arbitrary derivation to functional calculus is involved.

Let mu be the compactly supported spectral measure of h.
Regularity and faithfulness give no atom at zero.
Multiplication by t has dense range in L2(mu); since polynomials are dense and t is bounded, t C[t] is dense as well.
The displayed estimate makes the functional t f mapped to integral f bounded on this dense subspace.
Its Riesz vector w lies in L2(mu), with norm at most norm(xi)_2, and satisfies

\[
\int(t\overline w-1)f\,d\mu=0
\]

for every polynomial f.
The coefficient is integrable and defines a finite complex measure.
Uniform polynomial density on the compact real interval therefore makes that measure zero.
Hence t conjugate(w)=1 almost everywhere, so b=1/t belongs to L2 and has the claimed norm bound.
The argument excludes every actual-vacuum witness when b is not L2, using only polynomial elements of its given domain.

## Dependency and conclusion boundaries

Dab10-U002's accepted free-adjoining, algebraic-freeness and selfadjoint contraction interfaces apply exactly to the reference pair.
Its closed-real-derivation and conjugate-variable foundations retain their prior inspection limits.
Voi98-U005 supplies the pointed free-product representation and end-action mechanism; the specific variance-one right creation, weighted equality, spectral passage and transported coordinates are verified above.
There is no dependency cycle or additional unverified analytic estimate.
No numerical, proof-assistant, source-priority or general nonnormal classification claim is made.

## Conclusion

The complete statement and all seven proof sections of C_F0134 v1 pass this independently organized review with no required mathematical correction.
The exact two dependency interfaces are adequate at their recorded scopes.
This finding supports proved / independently reviewed for this fixed candidate if its responsible decision adopts it.

For precisely the stated positive regular scalar-conjugate h and free standard semicircular S, the tuple (h,hS) generates M and all three existential conditions A, F and S are equivalent to h inverse in L2.
The sufficient witnesses have the stated actual vacua and both canonical bounded-vector domains.
The two necessity arguments apply to arbitrary witnesses, whereas the weighted sufficient construction uses freeness.
No implication among A, F and S for general bounded nonnormal tuples follows from this special-class equivalence.

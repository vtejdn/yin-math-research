---
author: Yin
---
# Independent review of the correlated weighted full-domain reduction

Review performed and recorded: 2026-10-14T17:28.
Human record author: Yin.
This is a separately assigned AI mathematical review, not a personal human inspection.

## Arrangement and scope

The reviewer did not develop or edit [C_F0135 v1](../../claims/Yin_C_F0135_v1.md).
Root assigned the complete fixed candidate and the required scope of review.
The candidate's attribution, initial decision dated 2026-10-14T17:24 and description of the author's preparation were visible.
No author D material, proof-development discussion or informal explanation was read.
The reviewer read the full C and the precise direct interfaces of Dab10-U002 and C_F0129 Section 3 before reaching this conclusion.

This finding covers the complete statement and all four proof sections: reference assumptions and generation, represented ACSY derivations and their actual vacua, necessity from arbitrary ACSY witnesses, automatic continuity and normalization of arbitrary bare witnesses, uniqueness on the larger reference core, and restoration of the actual closed/adjoint domains from the weighted estimate.
It is an initial whole-proof review of this fixed reduction, not a review of a proposed counterexample or a completion review of T_F0011.

The accepted inputs are used at their recorded scopes.
In particular, the entire homogeneous K=0 case of C_F0129 Section 3 is covered by that Claim's selected independent review; its surrounding bounded-division-closure theorem is not imported as a hypothesis or conclusion.
No original source PDF, author draft or recursive predecessor-proof audit was consulted in this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0135 statement](../../claims/Yin_C_F0135_v1.md#statement) | Exact correlated selfadjoint reference assumptions; generation; A iff inverse L2; under inverse L2, F iff S iff the weighted core bound; explicit actual vacua, K-adjoint formula and full-domain dual choices. |
| [Conclusion](#conclusion) | [C_F0135 argument](../../claims/Yin_C_F0135_v1.md#argument) | All four sections, especially core-adjoint pairings before the weighted hypothesis, arbitrary-witness automatic continuity and larger-core uniqueness, and actual closed-graph/adjoint-domain restoration. |
| [Conclusion](#conclusion) | [Dab10-U002](../literature/Dab10/Yin_U002.md#dab10-u002) | Sections 2-3 at the selfadjoint joint-conjugate premise: represented reference difference quotients, canonical h-contraction and actual adjoint on M, constants 4 and 5, and bounded-set weak continuity. Hilbert boundedness is assumed separately only for B_S. |
| [Conclusion](#conclusion) | [C_F0129 Section 3](../../claims/Yin_C_F0129_v1.md#3-automatic-continuity-with-a-general-hilbert--schmidt-commutator) | Exact accepted auxiliary lemma: a linear map on all M commuting with a bounded diffuse selfadjoint h is operator-norm-to-H bounded, using its K=0 Hilbert-Schmidt case. No bounded-division-closure, rank-one, closability or adjoint premise is added. |

## Reference premises and generation

The stipulated reference pair (h,S) is bounded selfadjoint, generates M and has an actual joint L2 conjugate system.
This matches Dab10-U002's represented difference-quotient and canonical-contraction setting.
The h-coordinate canonical closure B_h and its actual adjoint therefore contain all bounded vectors, satisfy the operator-norm-to-L2 estimates with constants 4 norm(xi_h)_2 and 5 norm(xi_h)_2, and have bounded-set weak continuity.
This supplies the two h-coordinate generator identities on M by applying the core identities to uniformly bounded polynomial approximants and their bounded left h- and S-products.

The S-coordinate's extension to B(H) is an explicit stronger premise.
It is the extension of the normalized canonical contraction, so it vanishes at 1 and has [B_S,h]=0 and [B_S,S]=P on H by density.
The proof does not obtain B_h in B(H) or require it.
Freeness, semicircularity and an independent-coordinate hypothesis are absent throughout.

Regularity of h makes its spectral cuts e_n increase strongly to 1.
The bounded functional-calculus elements c_n=h inverse e_n satisfy c_nY=e_nS, which converges strongly to S.
Thus W*(h,Y)=M before any inverse-L2 assumption is imposed.
Both A_X=C<h,hS,Sh> and A_0=C<h,S> are dense star algebras; their possible inequality is retained.
The reference conjugate-system hypothesis ensures the difference quotients are defined on the represented A_0 rather than merely on formal words.

## Derivations and actual vacua when the inverse is L2

Assume b=h inverse belongs to H.
For a bounded polynomial u, u b belongs to H.
Therefore the insertion u tensor v mapped to u b tensor v is a legitimate algebraic tensor map on the reference derivative values.
It commutes with the outer left/right actions.
The second insertion, left multiplication by S on the second tensor factor, is bounded on the Hilbert tensor product and also commutes with the outer actions.
Their composition with the represented reference difference quotients gives the actual derivations in (4).

Checking h and hS uses only hb=1: delta_Y h=0 and delta_Y(hS)=1 tensor 1, while delta_h h=1 tensor 1 and its value on hS is the cancellation 1 tensor S-1 tensor S.
Restricting these actual maps to A_X respects every represented starred relation.
No general nonnormal S-to-A theorem is invoked.

On A_0, B_S p is a polynomial because partial_S p is a finite sum of polynomial tensors.
Hence K_0p=(B_Sp)b is defined.
Its actual core-adjoint pairing for every bounded q is

\[
\langle q,(B_Sp)b\rangle
=\tau(q^*(B_Sp)b)
=\tau(bq^*B_Sp)
=\langle qb,B_Sp\rangle
=\langle B_S^*(qb),p\rangle.
\]

Positivity makes b selfadjoint, and the trace pairing is legitimate for the bounded-L2 products.
Boundedness of B_S is essential here: its actual adjoint acts on every qb in H.
This proves M contained in Dom K_0* and the exact formula K_0*q=B_S*(qb), without assuming the weighted estimate or a full-M extension for K_0.
Density of M already proves K_0 closable.

The right contraction of delta_h is B_h p-K_0(pS)+pb.
Indeed the delta_Y product rule applied to pS gives the last term pb, and traciality identifies the trace of the second tensor factor with S multiplied on either side.
The sign of the final right-multiplication term is positive.

Pairing the two core contractions against 1 gives respectively B_S*b and

\[
\xi_h-\rho(S)B_S^*b+b
=\xi_h-(B_S^*b)S+b.
\]

Each is in H since B_S* and right multiplication by S are bounded.
These are the actual adjoint representing vectors on A_0 and hence on the dense restricted domain A_X.
The vacuum pairing of a derivative equals that of its right contraction, so the same vectors prove the exact ACSY premise and formulas (V).
This construction uses no weighted core estimate.

## Necessity for an arbitrary ACSY witness

For any A(X) witness, the Y-coordinate derivation vanishes on h and every scalar polynomial f(h).
Therefore the permitted domain element f(h)Y has derivative f(h) tensor 1.
The actual vacuum xi gives

\[
|\tau(f(h))|\le\|\xi\|_2\|h f(h)S\|_2
\le\|\xi\|_2\|S\|\,\|h f(h)\|_2.
\]

Only boundedness of right multiplication by S is used in the second inequality; no free factorization of the norm is assumed.

The spectral measure mu of h is supported in a compact positive interval with zero allowed only as a non-atomic endpoint.
Regularity and trace faithfulness give mu({0})=0.
Multiplication by t has dense range in L2(mu).
Applying this bounded multiplication to polynomial approximants shows t C[t] is dense as well.
The displayed bound therefore extends t f mapped to integral f to a bounded L2 functional.
Its Riesz vector w satisfies

\[
\int(t\overline w-1)f\,d\mu=0
\]

for every polynomial.
The coefficient is integrable, so this is a finite complex measure annihilating the polynomials.
Uniform polynomial density on the compact real interval forces that measure to vanish.
Hence w=1/t almost everywhere and b belongs to L2, with the stated bound norm(b)_2 at most norm(xi)_2 norm(S).
The argument tests only polynomial elements of the supplied domain.
It applies to every A witness, without extending its derivative to measurable functional calculus.
Together with the preceding construction it proves (2).

## Every bare full-domain witness forces the same weighted core estimate

Let E=-D_Y be an arbitrary F(X) witness.
It is defined on all M and satisfies [E,h]=0.
The h in the statement is bounded, diffuse and selfadjoint, and the zero commutator is Hilbert-Schmidt.
These are all the hypotheses of the auxiliary lemma in C_F0129 Section 3.
Its accepted conclusion makes E bounded from the Banach space M with operator norm to H.
This is not a Hilbert-space boundedness or closability assertion.
No bounded-division-closure hypothesis from the encompassing C_F0129 theorem is used.

Writing eta=E1 and E-circle(a)=E(a)-a eta preserves every left commutator, makes the vacuum zero, and remains operator-norm-to-H bounded because norm(a eta)_2 is at most norm(a) norm(eta)_2.
All inputs in the identity

\[
h[E^{\circ},S]=[E^{\circ},hS]=P
\]

lie in M.
Evaluation at 1 gives h E-circle(S)=1.
Since h is positive regular, the only affiliated solution is b, so b is an actual H vector.
For any bounded a the same identity and injectivity of h on H give [E-circle,S]a=tau(a)b.
Thus the two reference-core commutators are exactly [E-circle,h]=0 and [E-circle,S]=bP.

The polynomial map K_0 has those same identities: compute [B_S,h]=0 and [B_S,S]=P on polynomials, then multiply the outputs on the right by b.
Its vacuum is zero.
Induction on the length of a word in h,S therefore gives E-circle(p)=K_0p for every p in A_0.
This is a determination of actual maps on words, so represented polynomial relations cause no ambiguity.
S need not lie in the smaller target algebra A_X; E is given on all M, which includes every intermediate reference-core input.
The operator-norm bound for E-circle proves the weighted estimate on A_0.

Consequently this direction covers every F witness.
It neither presumes a preferred witness nor identifies an arbitrary supplied map with a particular closed extension on all M.
It also proves inverse-L2 necessity for F before using (3).

## The weighted bound restores the actual domains and constructs S

Conversely assume b in H and the weighted estimate.
The core-adjoint formula already proved gives M contained in Dom K_0*, with

\[
\|K_0^*q\|_2\le\|B_S\|\,\|b\|_2\|q\|.
\]

For K=closure(K_0), its actual adjoint is exactly K_0*.
The second domain is thus established before restoring the first one; no missing second contraction estimate is inferred.

For a in M choose uniformly norm-bounded Kaplansky approximants p_n from A_0 tending to a in L2, with the bound arbitrarily close to norm(a).
The weighted estimate makes K_0p_n weakly relatively compact.
The closed linear graph of K is weakly closed, so a weak graph limit has input a and puts a in Dom K.
Weak lower semicontinuity gives norm(Ka)_2 at most C norm(a).
This restores the specified original core closure, not an arbitrary Banach-space extension.

The commutators pass to M by the simultaneous bounded-approximant graph argument in the candidate.
Equivalently, since A_0 is a graph core invariant under h,S and bP is a bounded rank-one operator on H, graph approximation extends [K,h]=0 and [K,S]=bP to Dom K.
Their restriction to the now-established M domain gives [K,hS]=P.

The proposed operators E_Y=K|_M and E_h=B_h|_M-K rho(S)|_M are therefore defined on all M.
Right multiplication by bounded S preserves M.
Their four operator-first coordinate commutators follow from the reference identities; the Y-commutator for E_h cancels because [B_h,hS]=PS and [K rho(S),hS]=P rho(S)=PS.
The equality is tracial, not a claim that S commutes with P.

For each q in M, pairing against every input a in M gives the actual adjoint values E_Y*q=K*q and E_h*q=B_h*q-rho(S)K*q.
All vectors on the right exist by the verified domains, and rho(S) is bounded selfadjoint.
Thus both actual adjoint domains contain M.
Negating these operators yields generator-first S witnesses.
The immediate S-to-F implication and the preceding all-witness direction complete every equivalence in (3), together with the exact formula (D).

## Dependency and scope check

The selected Dab10 interface concerns the canonical selfadjoint h-contraction, its actual adjoint and the two operator-norm-to-L2 bounds.
The independent bounded-H assumption is made only for B_S.
The selected C_F0129 auxiliary lemma explicitly permits arbitrary Hilbert-Schmidt K, including zero, and its proof and current selected independent review were inspected at this exact scope.
Its spectral/automatic-continuity foundations retain their recorded accepted-input limits.
No other theorem about bounded rational adjoints, free products, or adjoint invariance of F is used.

The proof is acyclic: the core-adjoint formula precedes the weighted estimate, the arbitrary-witness direction produces that estimate using a separately accepted continuity lemma, and the converse constructs the required actual domains directly.
The proof does not recycle the desired existence conclusion to bound the candidate operator.
No numerical, proof-assistant or novelty claim is made.

## Conclusion

The full statement and all four proof sections of C_F0135 v1 pass this independently organized review with no required mathematical correction.
The two direct dependency interfaces are adequate at their recorded scopes.
This finding supports proved / independently reviewed for this exact fixed candidate if adopted by its responsible Claim decision.

Under precisely the stipulated correlated selfadjoint reference assumptions, the target tuple generates M; A(X) is equivalent to inverse-L2 membership, and, in that inverse-L2 regime, F(X), S(X) and the stated weighted core bound are equivalent.
The actual vacua and K-adjoint/domain formulas are proved.
The result neither proves the weighted bound for every such pair nor constructs a pair violating it.
It is an exact reduction of the remaining issue, not a general A-to-F theorem or a counterexample to that implication.

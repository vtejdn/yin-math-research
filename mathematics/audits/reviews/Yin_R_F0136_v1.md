---
author: Yin
---
# Independent review of closed normalized duals under bounded division closure of adjoints

Review performed and recorded: 2026-10-14T13:20.
Human record author: Yin.
This is a separately assigned AI mathematical review, not a personal human inspection.

## Arrangement and exact scope

The reviewer did not develop or edit the candidate in [C_F0129 v1](../../claims/Yin_C_F0129_v1.md).
The coordinating agent assigned a complete proof review, especially its general Hilbert--Schmidt commutator lemma, conjugate-derivation implementation, realification, and restoration of both actual domains.
Shared conversation supplied the comparison question and a summary of earlier results.
The candidate's own proof and assessment, its direct inputs, and the earlier comparison context were available.
Initial mathematical findings were formed by reading the complete candidate and checking its calculations; afterward R_F0042 was consulted for the retained source boundary and review format.
No earlier complete review of this candidate was supplied or used.

The inspected artifact is the fixed statement and complete argument in C_F0129 v1, as present at commit 60ba1c3c and read on the review date.
Its Sections 2--7 and all listed direct dependency interfaces are covered.
The result is evaluated for arbitrary bounded generating tuples, with the exact additional assumption that each adjoint belongs to the scalar division closure formed using bounded inverses in M.
No normality is added.

Published MSY23 and Lau88 results are accepted at the exact statement and applicability scopes recorded in their source units.
This review checks their local use, not their entire original proofs or cited predecessor literature.
The project proofs of the finite-rank trace step, the symmetric-form bound, and the present domain constructions were checked directly.
No new external literature inspection, numerical test, formal proof, manuscript review, or Task-completion review is claimed.

## Current relationship clarification

The original dated independent wording remains the historical description.
The reviewer did not develop or edit this candidate and formed its initial calculations before consulting R_F0042.
However shared conversation supplied a summary of earlier mathematical results and comparison context, whose exact content is not retained sufficiently to establish whether it was only the fixed dependency material or additional substantive author explanation.
A fixed proof, exact review scope and necessary dependencies are legitimate inputs.
The stated summary alone does not prove either isolation or an actual contribution, so the current exact relationship is unknown.
No reviewer-supplied mathematical repair is recorded for this complete candidate.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | unknown |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0129 statement](../../claims/Yin_C_F0129_v1.md#statement) | Bare full-M dual identities and bounded scalar division closure of all adjoints imply the stated normalized canonical closed duals with M Omega in both actual domains; arbitrary bounded generating tuples. |
| [Conclusion](#conclusion) | [C_F0129 argument](../../claims/Yin_C_F0129_v1.md#argument) | Complete Sections 2--7, including general-K automatic continuity, implementation, signs, actual adjoints, both graph restorations and precise nonconclusions. |
| [Conclusion](#conclusion) | [C_F0008 Section 4](../../claims/Yin_C_F0008_v1.md#4-application-to-the-original-bounded-target) | Exact bounded scalar division-closure convention and adjoint-closure condition; no scalar matrix-elimination theorem is needed by this candidate. |
| [Conclusion](#conclusion) | [C_F0024 Section 3](../../claims/Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors) | Bare full-domain finite-rank proof of maximal Delta, including denominator clearing, bounded finite-rank trace products and absence of a normality or adjoint-domain premise. |
| [Conclusion](#conclusion) | [MSY23-U002](../literature/MSY23/Yin_U002.md#msy23-u002) | Accepted maximal-Delta/full-linear-matrix equivalence for arbitrary bounded tuples and its interface with affiliated invertibility. |
| [Conclusion](#conclusion) | [MSY23-U004](../literature/MSY23/Yin_U004.md#msy23-u004) | Accepted embedded free-field realization; only invertibility of nonzero scalar rational elements in the affiliated algebra is used to obtain diffuse Y. |
| [Conclusion](#conclusion) | [C_F0069 Part A](../../claims/Yin_C_F0069_v1.md#a-automatic-boundedness) | Provenance and mechanism of triangular continuity and divisible-subspace exclusion; the present general-K extension is separately checked, not imported from the rank-one statement. |
| [Conclusion](#conclusion) | [Lau88-U001](../literature/Lau88/Yin_U001.md#lau88-u001) | Exact accepted well/super-decomposability, algebraic spectral-space and critical-eigenvalue definitions, Proposition 3.7 and Theorem 4.1; every local premise checked, original-proof inspection limits retained. |
| [Conclusion](#conclusion) | [C_F0071 v2 Part A](../../claims/Yin_C_F0071_v2.md#application-to-a-real-derivation) | Symmetric-form argument and real-derivation consequence, with the constant 2 sqrt(2), actual vacuum meaning and norm-density interface directly checked. No later mixed-tuple result is required. |
| [Conclusion](#conclusion) | [C_F0070 Part B](../../claims/Yin_C_F0070_v1.md#exact-equivalence-under-the-acsy24-hypotheses) | Kaplansky/weak-graph restoration mechanism only; the present candidate proves both required estimates and neither imports normal starred uniqueness nor assumes the canonical-domain conclusion. |

## Algebraic preparation and the diffuse element

Put \(B=\operatorname{Div}_M\mathbb C\langle X\rangle\), with inverses admitted only when boundedly invertible in M.
The hypothesis X_j* in B makes B a star algebra by induction on rational expressions.
Inverse closure of a unital C*-subalgebra gives A subset B subset C*(X), with norm closure C*(X).
Thus B Omega and A Omega are dense in H.

Normalization E_i(a)=-D_i(a)+aD_i(1) is legitimate on every bounded input.
The correction a -> a D_i(1) commutes with left multiplication and is bounded M-to-H, without being assumed bounded on H.
It preserves the commutator sign [E_i,X_j]=delta_ij P and makes E_i(1)=0.
Product and inverse commutator rules are valid because every bounded factor and its admitted inverse preserve M Omega.

The identification Theta(u tensor v)=u P v is complex linear and injective on algebraic tensors; its extension identifies the Hilbert tensor space with Hilbert--Schmidt operators.
The dagger convention gives Theta(eta dagger)=Theta(eta)*.
Every rational-expression commutator is therefore a finite-rank bounded operator with bounded coefficients in B.
Equality of represented elements implies equality of these extensions on the dense domain M Omega, so the induced derivation delta_i:B -> B tensor_alg B is well-defined.
Applying its commutator to Omega gives E_i|B=(id tensor tau)delta_i.

The direct finite-rank trace proof in C_F0024 Section 3 needs only the supplied maps and generator relations.
Clearing the finitely many output vectors by one regular right denominator places every relevant range inside M Omega.
Thus D_j S_i and all subsequent traced products are bounded finite rank, even though D_j is initially only algebraic.
The two independently variable right multipliers test dense vector families, and injectivity of the clearing multiplier removes it.
This yields maximal Delta without normality, continuity, or adjoint domains.

The accepted MSY23 interfaces then put B inside an embedded free division ring in the affiliated algebra.
A nonscalar selfadjoint real or imaginary part of X_1 lies in B, since X_1 cannot be scalar under its dual identity.
For every real lambda, Y-lambda is nonzero in that division ring, hence affiliated-invertible.
Its kernel projection is zero.
Faithfulness gives nonatomicity of the spectral distribution and therefore of every vector spectral measure of left multiplication by Y.
No bounded inverse or rational-matrix atomlessness is inferred.

## General Hilbert--Schmidt commutator lemma

For [E,Y]=K on all M Omega, with Y diffuse selfadjoint and K Hilbert--Schmidt, the algebraic graph map J(a)=(E(a),a) intertwines T=L_Y on the Banach space M with the bounded triangular operator S on H direct_sum M.
The upper-right block is K composed with the bounded inclusion M -> H.
The sign SJ=JT is correct.

Left and right multiplication by the selfadjoint N=lambda(Y) commute on the Hilbert space of Hilbert--Schmidt operators.
For rank-one tensors, their joint scalar spectral measures are products of nonatomic vector spectral measures.
The diagonal therefore has measure zero; density extends this to the joint spectral projection on the entire Hilbert--Schmidt space.
Consequently the double-operator-integral divided difference in (15) is well-defined for arbitrary K, and Gamma_z=K.
The derivative bound along the compact real spectral interval gives the stated Hilbert--Schmidt estimate.

The divided-difference product identity proves the triangular smooth calculus multiplicative, including its upper-right block, because psi(N) iota=iota L_psi(Y).
Cutoffs adding to one near the spectrum sum to the identity under this calculus.
Their closed ranges give invariant subspaces with spectra inside their supports: a smooth inverse near each compact support is an actual two-sided inverse on its closed range.
This verifies super-decomposability in Lau88's sense.
T is decomposable using a finite spectral partition of Y with supports compactly contained in the given open cover; the subspaces are p_j M, closed in the operator norm.

The divisible-subspace argument is also valid.
Membership in Ran(N-lambda)^2 for every lambda makes the fourth inverse-distance integral finite everywhere.
A positive-measure level set of that integral would have mass at most C n r^2 under the planar grid cover, for every r, a contradiction.
Projecting an S-divisible subspace to M and then injecting into H proves it vanishes; the remaining first-coordinate part vanishes by the same argument.
S has no eigenvalues because neither diagonal operator does.

Thus Lau88 Proposition 3.7 supplies closed algebraic spectral subspaces, and Theorem 4.1 applies without critical eigenvalues.
It makes J, and hence E:M -> H, bounded.
The candidate uses this only after constructing Y and verifying [E_i,Y] is Hilbert--Schmidt.
There is no circular continuity assumption.

## Conjugate derivation, realification and actual vacua

Both the star on B and the dagger on tensors are conjugate linear, so delta_i# is complex linear and an outer derivation.
If delta_i#(X_j)=sum a_ijk tensor b_ijk, the order in (24) is correct:

rho(a) P rho(b) xi = tau(xi b) a = a P b xi.

Thus sum rho(a_ijk) E_j rho(b_ijk) has precisely the required generator commutators.
Right multipliers commute with the left generators.
Subtracting a times its value at Omega normalizes without changing those commutators.
Agreement on generators extends to every bounded rational expression by the product and inverse rules.
Therefore F_i implements delta_i# on B, and F_i|B=(id tensor tau)delta_i#.
Every term is bounded M-to-H by the already established bounds for E_j and the bounded coefficients; no new automatic-continuity assertion is needed.

The realifications alpha=(delta+delta#)/2 and beta=(delta-delta#)/(2i) are real.
Their contractions are G=(E+F)/2 and H=(E-F)/(2i).
The dense star-algebra hypothesis for C_F0071 Part A is B inside C*(X), and these contractions are bounded for its operator norm.

The underlying symmetric-form lemma was checked directly.
Extending a bounded contraction and its vacuum functional to C*(X), a continuous square partition of a selfadjoint element with overlap at most two yields sum ||G h_j||_2^2 <= 2 ||G||^2 by independent signs.
The symmetric identity at h_j,h_j and Cauchy--Schwarz bound the vacuum by 2 sqrt(2)||G||||a||_2.
Hermiticity and a phase rotation give the same bound for general a.
This is an actual L2-representing vector, not a formal pairing.
The argument needs no coassociativity or pre-existing closability.

With the inner product linear in its second variable, delta=alpha+i beta gives xi=zeta_G-i zeta_H, exactly (34).
Reality makes the two zeta vectors selfadjoint.
Restricting delta_i from B to A already proves the full ACSY vacuum condition for that starred algebra; this consequence requires no normality.

## Both canonical domains and the generator identity

For a real contraction G, the symmetric identity reads

<Ga,b>+<a,Gb>=<zeta,a* b>=<a,b zeta>.

Traciality and zeta=zeta* justify the last equality with this inner-product convention.
Restricting the tested first variable to A proves the actual adjoint formula G_0* b=b zeta-Gb for every b in B.
Combining G and H by explicit pairings, rather than asserting a global adjoint-of-sum identity, gives

E_i0* b=b xi_i-F_i b,  b in B.

Since B Omega is dense, E_i0 is closable.
The same polynomial core A has the two distinct bounds ||E_i0 a||_2 <= C_i||a|| and ||E_i0* a||_2 <= (||xi_i||_2+C_i')||a||.
The second is not inferred merely from the first.

Kaplansky density, followed by norm approximation in C*(X), supplies uniformly bounded a_gamma in A with a_gamma Omega converging strongly to an arbitrary a Omega.
The first estimate supplies a weak graph-cluster pair for closure(E_i0); its closed linear graph is weakly closed.
The second estimate independently supplies a graph-cluster pair for the closed operator E_i0*.
These are separate legal subnet arguments, proving membership in both actual domains.
No identification with the supplied full-domain map is needed.

Finally, A is invariant under X_j and the core commutator is bounded.
Graph-norm approximation passes this identity to the full domain of closure(E_i0), including invariance under X_j.
Negation gives the exact generator-first convention for the asserted normalized closed duals.
Vanishing at Omega survives closure.

## Conclusion

The exact statement and complete argument of C_F0129 v1 pass this independently organized review, under the declared accepted source interfaces, with no required mathematical correction.
This supports a proved / independently reviewed assessment for that fixed claim if adopted by its responsible decision.

In particular, bare full-M duals together with \(X_j^*\in\operatorname{Div}_M\mathbb C\langle X\rangle\) imply the ACSY24 derivation and actual-vacuum hypothesis for arbitrary bounded generating tuples.
The proof gives more: the closures of the normalized supplied maps restricted to the starred polynomial core have M Omega in both their domains and actual adjoint domains.

The reverse implication from ACSY24 plus the same bounded-division-closure assumption has not been proved here.
The present automatic-continuity lemma assumes an already existing map on all M; it cannot be applied just to an ACSY polynomial-core operator.
A reverse argument still needs suitable core norm-to-L2 bounds or another construction of full-M duals.
Failure to supply that argument is not a counterexample to the reverse implication.

The conclusion does not identify arbitrary supplied full-domain maps with their canonical closures on all M, does not establish closability of those supplied maps on that larger domain, and does not remove the bounded adjoint-closure hypothesis.
Source completeness is limited to the listed accepted theorem interfaces and explicitly checked project arguments; no priority or exhaustive-literature claim is made.

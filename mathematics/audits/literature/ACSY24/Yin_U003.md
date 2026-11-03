---
author: Yin
---
# ACSY24: matrix realizations, derivations, compression and Atiyah interfaces

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | [ACSY24](../../../literature/pdf/ACSY24.pdf), published Advances in Mathematics 443 (2024), 109595; retained 73-page edition. |
| source-locator | Section 3, pp.30--38; Section 4.1--4.2, pp.38--44; printed page numbers equal PDF page numbers. |
| inspection | 2026-10-14, AI source-proof self-review under Yin's explicit full-audit request. All stated passages and proofs were read; exact prior audits and accepted external inputs are identified below. No new independent or formal verification is claimed. |

The 2026-11-02 repair reading revisited Theorem 4.7 and its proof, pp.43--44, at the BBL21 interface described below; it supplies no new whole-source or independent review.

## ACSY24-U003

### Lemma 3.1 and Proposition 3.2: matrix realizations

Lemma 3.1 replaces a normal variable with rational atomic weights by a diagonal n by n model with repeated scalar atomic entries and atomless residual entries.
Splitting its normal spectral measure into the stated atomic and residual summands verifies the joint moments of that single variable.
If the residual weight is zero, choose the auxiliary probability algebra C; do not divide by tau(q_0)=0.

Proposition 3.2 treats an arbitrary normal Y, extracting floor(n tau(q_lambda)) scalar slots at each atom and leaving arbitrary normal entries in the other slots.
The model lives after a trace-preserving enlargement and satisfies
\[
 I_n\otimes Y=UDU^*,\qquad U=U^*=U^{-1}.
\]
The source's support calculation for its partial isometries was checked: u_ij=p_j u_ij p_i makes unwanted products vanish, and adjoint pairing gives U^2=I.
No additional coherence of all u_ij as matrix units is necessary.

The proof nevertheless needs two repairs.
Having a nonatomic variable does not imply that the original M is type II1.
Also, its chosen projections p_i must **commute with Y**.
Arbitrary cuts of q_0 or of residual spectral projections need not do so.
Enlarge to a II1 factor and choose the cuts in a diffuse maximal abelian algebra containing W*(Y).
Within an atom block Y is scalar, and within the other blocks the abelian cuts also commute with Y.
Then the displayed sum sum_j p_jYp_j=Y is justified and the transported diagonal entries are normal.

The standard factor-enlargement input can be seen directly: take A=M tensor L-infinity(T), with a central Haar unitary v in its second factor, and form N=A*L-infinity(T), with Haar u in the new factor.
On L2(N) minus L2(A), conjugation by v^k tends weakly to zero.
This follows first for reduced words with finite Fourier endpoints, then by L2 approximation.
A central element of N therefore belongs to A; commuting also with u forces it to be scalar by the reduced-word decomposition.
Thus N is a finite diffuse factor and contains M trace-preservingly.
A maximal abelian subalgebra of a II1 factor is diffuse: an atom e would make eAe scalar, while every element of eNe commutes with A and would have to belong to A, contradicting the II1 corner.
Its measure-theoretic cuts supply every required trace.
This resolves the concrete construction rather than assuming that arbitrary projections commute.

<a id="derivation-adjoint-and-compression"></a>
### Lemma 3.3 and the exact nonnormal derivation interface

The source domain is a weakly dense star algebra A, and the codomain is L2(M) tensor_2 L2(M) with outer bimodule actions.
In particular it need not be A tensor_alg A.
Lemma 3.3's full equivalence, beyond the previous supporting-interface reading, follows from the product rule on a* x b*.
With inner product linear in the second argument and zeta=delta*(1 tensor 1),
\[
 \delta^*(a\otimes b)=a\zeta b-
 \bigl[(\tau\otimes{\rm id})\delta(a^*)\bigr]^*b
 -a\bigl[({\rm id}\otimes\tau)\delta(b^*)\bigr]^* .
\tag{1}
\]
Each contraction is in L2 and each multiplication here is by a bounded element.
Thus an actual vacuum adjoint implies that every algebraic tensor is in the actual adjoint domain.
The converse uses a=b=1.
The map T -> T sharp eta, for eta in A tensor_alg A, is bounded on the Hilbert tensor product and commutes with outer actions; pairing with the vacuum gives delta*(eta*) and proves the third equivalent condition.
No reality condition on delta was used.

Theorem 3.4 and Proposition 3.5 are reused from [U001](Yin_U001.md#acsy24-u001), including its complete Hilbert-Schmidt regularization reconstruction, and the separate [R_F0044 no-normality finding](../../reviews/Yin_R_F0044_v1.md#acsy-no-normality).
They conclude maximal Delta for arbitrary bounded generators under the starred-core derivation and actual vacuum-adjoint assumptions.
**Normality is not required.**
The phrase on p.36 placing the constructed dual in the affiliated algebra is not a valid affiliation conclusion: its commutator with a generator is the vacuum projection.
The actual proof uses a closable operator on H, its starred-core commutators, its adjoint and bounded regularization.
The existing reconstruction supplies that argument without assuming affiliation to M or full domain M Omega.

### Lemma 3.6, Theorem 3.7 and Corollary 3.8

Lemma 3.6 obtains a unitary derivation with partial(U)=1 tensor 1 by twisting the unitary difference quotient d(U)=1 tensor U.
Equation (1) justifies the twist and its vacuum adjoint.
The initial inspection left the general L3-density and free-Brownian-density source interfaces unverified.
The receiving applicability check now reuses the direct primary readings in [Voi99-U004](../Voi99/Yin_U004.md#unitary-derivation-and-fisher-information) and [Voi99-U002](../Voi99/Yin_U002.md#unitary-free-brownian-motion), without expanding that original dated inspection or any old R finding.
For a unitary U with law p d lambda, p in L3 of normalized Haar measure, put h=d*(1 tensor 1)=-i(Hp)(U), using U004's corrected sign and Hilbert-transform convention.
The represented core is the Laurent-polynomial algebra in U; the absolutely continuous law has infinite spectrum, so no nonzero Laurent-polynomial relation obstructs the derivation.
For an additional unital star algebra B, the extension uses the stated freeness of B and the U algebra and the corresponding free-product core, as in Voi99 Proposition 8.4.
On the outer Hilbert tensor bimodule define the unitary bimodule map W(a tensor b)=a tensor U*b.
Then partial=W d has partial(U)=1 tensor 1 and partial(U*)=-U* tensor U*, so it is not the original d.
Since W*(1 tensor 1)=1 tensor U belongs to the algebraic adjoint test core, equation (1) gives the actual vacuum
\[
 \partial^*(1\otimes1)=d^*(1\otimes U)=hU+U
 =U\bigl(1-\mathrm i(Hp)(U)\bigr)\in L^2(M).
\]
The L2 assertion follows from the source's Hp in L2(p d lambda) and bounded multiplication by U; no reality hypothesis for partial is added.
Voi99 Proposition 1.6 supplies bounded density, hence L3 density, for free unitary Brownian motion at strictly positive time; its point-mass law at time zero is excluded.

The Haar case actually needed for Theorem 4.1 has a direct check.
On Laurent polynomials,
\[
 \partial U^m=\sum_{j=0}^{m-1}U^j\otimes U^{m-1-j}\quad(m>0),\qquad
 \partial U^{-m}=-\sum_{j=1}^{m}U^{-j}\otimes U^{-(m+1-j)}.
\]
The vacuum functional is the coefficient of U in the polynomial, so partial*(1 tensor 1)=U.
This proves the needed Haar premise directly, separately from the general L3 source interface above.

For Theorem 3.7 extend each derivation by zero on the freely adjoined M_n(C).
For a reduced alternating centered word involving the new factor, the vacuum trace of its derivative vanishes: every differentiated summand has a centered new-factor word on at least one side.
For a word entirely in A the trace is the original vacuum trace.
By linearity and L2 approximation for the tensor values,
\[
 (\widetilde\tau\otimes\widetilde\tau)\widetilde\partial
 =(\tau\otimes\tau)\partial E_A.
\]
The extension therefore has the original vacuum-adjoint vector.
Twist by E_i1 tensor E_1j and restrict to the E_11 corner.
Direct multiplication gives partial_ij(X_kl)=delta_ik delta_jl (E_11 tensor E_11).
With normalized corner trace n times the ambient trace, the tensor norm scales by n while the vector norm scales by sqrt(n); the adjoint formula has the source's factor n.
When necessary interpret the vector as its E_11 corner compression.
This proves the finite-d joint version simultaneously, not merely independent d=1 statements.
Proposition 3.5 gives Delta=d n^2.

Corollary 3.8 consequently has the required unitary-vacuum input for Haar U and for the stated general L3-density law, with the Laurent/free-product core and freeness hypotheses above retained.
The finite-family compression conventions were checked against [NS06](../../../literature/pdf/NS06.pdf), Theorems 14.18 and 14.20, printed pp.234--235/PDF pp.251--252.
The scalar cyclic-cumulant criterion identifies the amplified compressed Haar matrix as free from M_n(C).
Vanishing mixed cumulants also applies to the joint compressed families; it does not assert that individual entries of a unitary matrix are mutually free.

### Proposition 3.9: the amplification freeness step

Let D=M_n(C).
Entrywise freeness gives
\[
 M_n(A*B)=M_n(A)*_D M_n(B)
\]
at the level of the generated reduced tracial algebras.
If C inside M_n(A) is scalar-free from D, then W*(C,D) is its scalar reduced free product C*D.
Associativity of reduced-word expansions gives
\[
 (C*D)*_D M_n(B)=C*M_n(B).
\]
To check this identity, expand each factor into its D-expectation and its centered part; alternating centered amalgamated words have zero D-expectation, and scalar-centered C words and D words are orthogonal by the original scalar freeness.
These same reduced words have exactly the scalar free-product trace on the right.
The faithful traces identify the generated algebras.
This proves the proposition and fills the joint-freeness justification implicit in the source's short Haar-conjugation proof.
Merely knowing that one Haar unitary is free from C would not, by itself, justify conjugating an arbitrary third algebra.

### Theorem 4.1, Remark 4.2, Proposition 4.3, Corollary 4.4

Reuse [U002](Yin_U002.md#acsy24-u002) at its exact full selected proofs.
The newly checked dependencies above close the compression/freeness interfaces it retained externally.
Theorem 4.1 uses mutually independent compressed Haar families and diffuse diagonal variables; Proposition 2.33 and the maximal-Delta theorem identify their rational algebra with the relevant free field.
With common denominator n,
\[
 \operatorname{rank}_{M}A(X)=\frac1n\operatorname{rank}_{\mathbb F}A(\overline X).
\]
Rational domains and ranks follow from Schur complements and regularity, not an unbounded substitution with undefined intermediate inverses.

Remark 4.2 and Proposition 4.3 retain all relations in each input algebra A_i inside a matrix algebra over one maximal-Delta algebra.
They permit certain nonnormal algebra models; they do not say that marginal kernel masses classify arbitrary nonnormal tuples.
In Corollary 4.4 the finite group regular representations have compatible probability traces after amplification to n=lcm(|G_i|).
Group inverse generators are evaluated as genuine unitary inverses before linearization.
Matrix rank uses the same 1/n factor.
This retains the finite-group application without importing any broader group theorem from secondary background references.

<a id="atiyah-property-convention"></a>
### Definition 4.5, Corollary 4.6 and Theorem 4.7

Definition 4.5 quantifies over every polynomial matrix and an additive subgroup Gamma containing Z.
Its star-subalgebra wording does not literally fit the holomorphic algebra C<X> for a general normal tuple in Corollary 4.6.
The proved rank property applies to that unital algebra; it need not be star closed.
Common-denominator Theorem 4.1 proves the least-common-multiple denominator in Corollary 4.6.

Theorem 4.7 asserts the Atiyah property for two free bounded selfadjoint variables whenever every marginal atomic mass belongs to the chosen additive subgroup Gamma containing Z, including irrational atomic masses.
Its proof invokes published BBL21 Corollary 3.3 for a generally nonselfadjoint linearized matrix.
The inspected [BBL21 preprint v2](../../../literature/pdf/BBL21--arxiv-v2.pdf) has Remark 3.3 instead; its relevant Corollary 4.3 requires a selfadjoint pencil and an invertible matrix-valued expectation of the kernel projection.
The final journal mathematical text remains unavailable, so this difference does not establish a misnumbered published citation or a refutation of the theorem.
The source's stated compression/doubling conclusion by itself only controls twice the nullity, which does not permit division by two in arbitrary Gamma.
[BBL21-U001](../BBL21/Yin_U001.md#bbl21-u001) retains the precise source identities, hypotheses and actual inspection limits.

The full local repair is [C_F0181](../../../claims/Yin_C_F0181_v1.md#graded-subordination-proof), using the identified v2 Theorem 3.5 and conditional-resolvent identity (3.7).
It keeps square padding through both support cuts, verifies invertibility of both expected kernel projections and preserves off-diagonal symmetry through the subordination limits.
This makes the factor of two common to the exact one-variable trace identity, before drawing a subgroup conclusion.
The proof preserves every hypothesis and conclusion of Theorem 4.7.
Its [current proved decision](../../../claims/Yin_C_F0181_v1.md#decision-reviewed-adoption) adopts the [independent whole correction finding](../../reviews/Yin_R_F0185_v1.md#whole-candidate-finding), which checks the complete unchanged proof and exact source interfaces.
The remaining published-corollary identification is a separate source-attribution limit.
This interface is outside the proofs of Theorems 1.1 and 1.2 and does not affect the Lemma 3.3 tensor-adjoint formula separately used by C_F0146 and C_F0149.

### Scope of the conclusion

The algebraic model and the normal-target matrix realization are audited with the explicit repairs above and accepted free-field/compression inputs.
The general L3-density receiving interface uses the explicit twist, actual adjoint vector and source/core hypotheses above; it does not identify the two derivations or assert an arbitrary-core extension.
The full two-variable Atiyah conclusion has the independently checked local proof above, separately from the unavailable journal-corollary attribution and accepted analytic-foundation limits.
The user's earlier no-normality question for Proposition 3.5 stays resolved; these source and inspection limits do not reinstate a normality premise in that proposition.

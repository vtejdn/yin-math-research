---
author: Yin
---

# Independent review of the maximal-Delta criterion and dual specializations

Date: 2026-10-09T16:47.
Human record author: Yin.
Method: separately organized agent review of the complete fixed Claim, with particular attention to Part B and the analytic interfaces in Part C.
This is an agent review recorded under the bound human author's identity; no personal human inspection is asserted.

## Arrangement, inputs and inspected artifact

The reviewer did not participate in development of the argument.
The assignment supplied the target and questions to investigate, but no proof-generation dialogue, exploratory derivations or prior verdict.
The reviewer first read the exact [statement](../../claims/Yin_C_F0068_v1.md#statement) and [Argument P1](../../claims/Yin_C_F0068_v1.md#argument), identified the obligations below, and only then inspected the fixed dependency statements and proofs.
The exploratory D material was not consulted.
No prior R finding or informal review was used to decide this verdict.
Some dependency files contain historical assessment and source-review paragraphs; those became visible during the subsequent dependency reading and were not substituted for the calculations recorded here.

The inspected artifact is Yin_C_F0068_v1.md, dated 2026-10-09T16:42, with its initial proof-draft/under-review decision and complete Sections 1--5.
All three statement parts and the complete argument were examined.
The mathematical statement was reread before recording this finding.
There was no requested mathematical repair during this review.
The arrangement is an initial independent review of this assembled Claim, not a retrospective claim to have independently developed the underlying external theorems.

## Initial obligations

The following obligations were formulated from the statement before consulting dependency review histories.

1. Establish the tensor criterion in both directions, including the same-unit division-subring requirement, affiliated outer-denominator clearing, and uniqueness.
2. Check the right-action/tensor signs and the existential fraction certificate in both directions.
3. Verify maximal Delta for the sandwich pair, von Neumann generation, impossibility for the trivial fraction, the displayed good fraction, and the stronger all-bounded-vector dual obstruction.
4. Derive maximal Delta from condition (D) without assuming bounded Hilbert-space duals or rationality.
5. Verify that the standalone fraction calculus supplies every legal bounded fraction, bounded finite-rank representatives, and coordinatewise numerical ranks without circular use of a final rationality theorem.
6. Match the normal-generator fundamental identity, including its sign and the coefficient equation sb=at.
7. Establish equality with the bounded representatives on the entire natural domains, and unconditional density of those domains.
8. Recover the bounded-element criterion and full closed-domain invariance.
9. Identify the actual canonical conjugate-variable closure, both required domains, and the one-variable case.

## Algebraic criterion and sharpness findings

The [C_F0035 equalizer proof](../../claims/Yin_C_F0035_v1.md#yin_c_f0035-p1) applies to the same-unit division subring supplied by the maximal-Delta free-field interface.
In particular, the right-F-linear coordinate functional on a basis containing 1 and u gives the correct balanced map; neither commutativity of F nor absence of zero divisors in U is used.
Projecting the tensor identity kills each generator balancing term.
Thus Part A provides the reverse implication needed later, independently of any dual.

For the forward implication, the outer bimodule product and inverse formulas agree with the corresponding formulas for u tensor 1 minus 1 tensor u.
A finite rational expression supplies finite algebraic tensors; subsequent uniqueness removes expression dependence.
The affiliated row and column functional-calculus denominators clear all finitely many tensor factors simultaneously.
Multiplication by these denominators commutes with each Psi through the outer action and is invertible in U.

For g,h in H the pairing tau(hq) is defined for q in H by the L2-L2 trace pairing.
With the Claim's second-slot-linear convention, Theta(g tensor h)q=g tau(hq) is complex bilinear in g,h and identifies the algebraic tensor product with bounded finite-rank operators.
Direct calculation gives
\[
[\rho(X_i),\Theta(g\otimes h)]
=\Theta(gX_i\otimes h-g\otimes X_i h).
\]
This verifies both the sign and the tensor legs.
After clearing, maximal Delta proves injectivity; after outer division the finite-rank certificate yields the original affiliated tensor equation.
The argument establishes some fraction, and does not silently establish every fraction.

For Part B, h is injective, its inverse is affiliated, and the displayed spectral cutoffs recover S strongly inside W*(h,hSh).
Thus the new pair generates the stated M and S belongs to its affiliated division closure.
The base variables h,S are freely independent and atomless, exactly the hypotheses of the accepted entropy interface.

Expansion of the sandwich commutator gives
\[
[RBR,T]=[R,BRT+TRB]+[B,RTR].
\]
All transformed cycle terms remain finite rank.
Injectivity and dense range of R cancel RTR=0, proving maximal Delta for the sandwich pair.
For the trivial fraction, SP-PS=[B,P]; the base-pair cycle identity therefore forces RT_YR=P.
Applying it to Omega forces T_Yh=h^{-1}, contradicting the divergent integral of t^{-2}.
This does not depend on an unproved assertion about tensors outside H.

For Q=(h,hS,Sh,h), the displayed T_Y=P and T_h=-PSh-hSP give, under Psi, precisely hS tensor h minus h tensor Sh.
Thus the example has an actual good fraction.
Finally, the proposed all-M dual would imply h(D_Y(Sh)-S D_Y(h))=1 on bounded-vector inputs.
The parenthesized vector would be h^{-1} in H, the same contradiction.
The obstruction already precedes any adjoint-domain requirement.

## Dual, fraction and domain findings

Condition (D) gives closability of each restriction D_{i,0}.
In the maximal-Delta proof, a common right denominator clears the finite-dimensional cycle ranges into M.
The further left and right commutant multipliers preserve the zero-cycle identity and bounded ranges.
Hence every D_{j,0}S_i is bounded finite rank, ordinary trace cyclicity applies, and independent dense commutant test vectors force each cycle operator to vanish.
This checks maximality without presupposing any finite-defect rationality criterion.

The reviewer rechecked [C_F0034-P1](../../claims/Yin_C_F0034_v1.md#yin_c_f0034-p1), including its [C_F0031 finite-range cancellation](../../claims/Yin_C_F0031_v1.md#yin_c_f0031-p1).
With E=V_i=M Omega, all module and adjoint-domain hypotheses hold.
Adjoint testing makes every cleared defect closable.
A closable finite-range map has a bounded closure.
Restriction to a Hilbert-dense subspace with finite range forces the same bounded closure, which validates cancellation through a bounded injective left multiplier and a bounded dense-range right multiplier preserving E.
No graph-density assumption is silently imposed.

The common-multiple identity
\[
yT_i(Q_1)y'=xT_i(Q)x'
\]
therefore proves both finite-rank independence and equality of the coordinatewise finite ranks.
The addition, product and inverse fraction formulas were checked directly; the product proof does not require its auxiliary numerators to be regular.
These operations prove the forward inclusion of the affiliated division closure into the finite-defect class.
They do not use maximal Delta or a final rationality conclusion.

For [C_F0033-P1](../../claims/Yin_C_F0033_v1.md#yin_c_f0033-p1), the needed hypotheses are exactly normality, generation, closable dual restrictions on a dense left M-module, and bounded extensions of the defects.
Equality of the legal fractions supplies sb=at.
Its conclusion is
\[
\sum_i[\rho(X_i),T_i]=aPt-sPb,
\]
with the same sign as Part A.
The local computation and the normal-operator exponential argument were checked.
In this application E=M, so the module windows can be M itself: closedness of the Hilbert closure makes the restriction M with its operator norm to H have a closed graph, hence it is bounded.
Adjoint testing gives bounded-set weak continuity.
The entire-function argument transfers generator commutation to adjoints; Kaplansky approximation then transfers it to all M coefficients.
Thus the consumed E=M case does not need an unproved domain localization.
Applying Part A now proves the reverse inclusion, and tensor uniqueness proves (D3).

For the natural-domain passage, s*eta and a*eta remain bounded vectors and therefore belong to the adjoint domain.
Pairing the raw expression against eta in M Omega first identifies its adjoint test vector with K*eta on the dense bounded-vector domain, and then proves equality with K on every q in the full natural domain.
This uses actual adjoints and avoids any claim that simultaneous graph approximation of bq and tq is available.
Each natural domain contains M Omega regardless of rationality, which also proves density of their intersection.

For bounded f, Q=(1,f,f,1) is legal.
The graph core M Omega is a core by the definition of the chosen closure.
If q_n tends to q in that graph norm, the bounded commutator formula makes D_{i,0}(fq_n) tend to f\widehat D_i q+T_iq.
Closedness gives domain invariance and the full-domain formula.
Restriction proves the converse.
An arbitrary larger closed extension is not substituted anywhere.

## The two applications and source limits

A bounded dual B_i satisfies (D) on all H, and its restriction to the dense subspace M Omega closes back to B_i.
This supplies the asserted bounded-dual application for bounded normal generators.

For conjugate variables the reviewer inspected only the analytic construction and domain conclusions in [C_F0022 Sections 2--3](../../claims/Yin_C_F0022_v1.md#2-sources-and-the-additional-analytic-input), not its final rationality theorem as an input.
The polynomial adjoint has the correct tensor-leg orientation,
\[
(D_i^0)^*p=p\xi_i-D_i^0p.
\]
The accepted selfadjoint contraction estimate gives the sufficient constants 4 and 5 for arbitrary complex polynomials.
Bounded Kaplansky approximants and weak closedness of the actual Hilbert graphs put every bounded vector into the canonical closure and its adjoint domains.
The resulting bounded-set weak continuity extends the generator identities.
Since the polynomial core lies in M Omega, closing the restriction to M Omega gives exactly the original canonical polynomial closure.
The full natural domains in the Claim consequently belong to that precise closed operator.

The exact accepted source interfaces checked for applicability were:

| Interface | Inspected fixed source and retained boundary |
| --- | --- |
| Maximal Delta, finite-rank cycles, and the free field | [MSY23-U002](../literature/MSY23/Yin_U002_v1.md#msy23-u002), published Section 3, pp. 12--20; [MSY23-U004](../literature/MSY23/Yin_U004_v1.md#msy23-u004), published Section 5.1, pp. 28--34. Arbitrary bounded tuples and the same-unit affiliated division subring match Part A. Their foundational free-field and affiliated-algebra inputs remain accepted inputs. |
| Free atomless base pair | [MSY23-U005](../literature/MSY23/Yin_U005_v1.md#msy23-u005), Section 6.1 entropy interface. Selfadjointness, freeness and absence of atoms hold for h,S. The original CS05 entropy/homological comparison and free-additivity proofs were not re-audited. |
| Polynomial dual and adjoint | [MS23-U001](../literature/MS23/Yin_U001_v1.md#ms23-u001), Definitions 2.3--2.4 and Theorem 2.5 interface. Finite-Fisher algebraic freeness and the accepted difference-quotient foundations remain at their recorded source limits. |
| Operator-norm-to-L2 estimates | [Dab10-U002](../literature/Dab10/Yin_U002_v1.md#dab10-u002), arXiv:0804.2906v2, Lemma 12, PDF p. 9. The source's closed-real-derivation functional calculus is an accepted input; the source is not asserted to give a Hilbert-space bounded canonical dual under finite Fisher alone. |
| The case d=1 | [Voi98-U003](../literature/Voi98/Yin_U003_v1.md#voi98-u003), Proposition 3.6 and the standard semicircular conjugate. Freely adjoining a semicircular variable preserves the original conjugate and polynomial contraction values, allowing the printed d>=2 estimate to be applied and restricted. |

These were local source-unit and project-proof readings.
This review did not newly retrieve or fully audit the original external papers, their entire proofs, or their broader applications.
The standard affiliated functional calculus, algebraic basis theorem, Kaplansky density and elementary Hilbert-space facts are accepted at the precise uses described above.
The current Claim's reproduced denominator, maximality and adjoint-bridge arguments were checked directly; the final conclusions of C_F0007, C_F0024, C_F0067, C_F0022 and C_F0013 were not used as shortcuts.

## Conclusion

No unresolved mathematical defect was found in the exact statement or complete Argument P1 of Yin_C_F0068_v1.md under the identified accepted external inputs.
This finding supports a proved / independently reviewed assessment of Parts A, B and C together.

The result recovers the affiliated and bounded-element finite-rank criteria for bounded duals and for canonical finite-Fisher duals, including every legal bounded fraction, the full natural domains, and coordinatewise rank independence.
Part B correctly prevents interpreting these analytic conclusions as consequences of maximal Delta alone.
No equality with scalar division closure inside M, novelty certification, formal verification, external human peer review, publication or Task completion is concluded.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [Exact statement](../../claims/Yin_C_F0068_v1.md#statement) | Entire Parts A, B and C, including hypotheses, all fraction quantifiers, tensor uniqueness, counterexample, actual closed domains, bounded-element invariance, both applications and rank independence. |
| [Conclusion](#conclusion) | [Complete Argument P1](../../claims/Yin_C_F0068_v1.md#argument) | Complete Sections 1--5, with independently reconstructed algebra and analytic interface checks; external source proofs retain the explicit accepted-input limits recorded in this review. |

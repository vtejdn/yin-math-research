---
author: Yin
---

# Independent whole-proof review of maximal-Delta rationality and dual recovery

Date: 2026-10-09T16:47.
Human record author: Yin.
Review method: a separately assigned AI agent performing mathematical proof and dependency-interface checking.

## Arrangement, inputs and inspection sequence

This is an initial independent review of the complete fixed [Yin_C_F0068_v1 statement](../../claims/Yin_C_F0068_v1.md#statement) and [argument P1](../../claims/Yin_C_F0068_v1.md#argument), dated 2026-10-09T16:42.
The target was read with its initial proof-draft, under-review assessment.
The reviewer did not develop the proof and was separately tasked to check all of Parts A, B and C and argument Sections 1--5.

The supplied context consisted of the repository instructions and the review assignment identifying the fixed target and the required scope.
No proof-generation dialogue, author explanation, exploratory draft or earlier discussion check was supplied to this reviewer.
The linked exploratory D material was not opened.
Obligations were first enumerated from the statement, then the target proof and exact mathematical interfaces were checked.
Existing source-unit inspection and review metadata were encountered when reading accepted inputs; those historical conclusions were not substituted for checking the present proof.
No prior review of this new target or another concurrent reviewer's conclusions was consulted before reaching the findings below.

The review rederived the algebra, denominator manipulations, commutator signs, counterexample and analytic implications described below.
This is an independent mathematical review, not a claim that the human record author personally performed the checks.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete conclusion](#conclusion) | [Exact statement](../../claims/Yin_C_F0068_v1.md#statement) | Complete Parts A, B and C: all hypotheses and quantifiers, both uniqueness assertions, sharpness, SOME/EVERY, coordinatewise ranks, natural domains, bounded-element graph invariance and both specializations. |
| [Complete conclusion](#conclusion) | [Exact argument P1](../../claims/Yin_C_F0068_v1.md#argument) | Complete Sections 1--5 with the precise accepted inputs and inspection limits below; includes the noncircular assembly and finite-Fisher analytic interface, without selecting any older Claim's final rationality conclusion. |

## Obligations derived from the statement

| Obligation | Decisive verification | Finding |
| --- | --- | --- |
| Maximal Delta under the stated bounded-tuple hypotheses | MSY23-U002 finite-rank cycles and MSY23-U004 free-field evaluation were checked without normality or generation assumptions. | Applicable in Part A. |
| Affiliated tensor existence, converse and uniqueness | Rational-expression induction, the right/left balanced tensor equalizer, and simultaneous outer denominators were rederived. | All three steps valid. |
| Finite-rank certificate and fixed-fraction uniqueness | The complex-bilinear trace pairing identifies finite-rank operators with algebraic L2 tensors; the commutator sign and both outer divisions agree. | Equivalent to rationality with an existential fraction. |
| The complete sharpness example | Generation, maximal Delta, failure of the trivial fraction, the explicit good fraction and absence of an all-M dual were checked separately. | Each asserted obstruction and positive example holds. |
| Actual dual defects and all fractions | Condition (D), finite-defect closability/cancellation, and the normal-generator fundamental identity were matched at their actual domains. | SOME/EVERY and coordinatewise finite numerical ranks follow. |
| Full natural domains and bounded-element graph statement | Adjoint testing on all bounded vectors and closure of the bounded-vector restriction were checked. | No missing simultaneous-core approximation. |
| Canonical finite-Fisher recovery | Polynomial adjoint formula, norm-to-L2 estimates, weakly closed graphs, extended generator identities and the d=1 reduction were checked. | Exactly the stated canonical closure satisfies (D). |

## Part A: algebra, denominators and operator identification

The free-field input is the combination of the finite-rank-cycle/full-linear-matrix theorem in [MSY23-U002](../literature/MSY23/Yin_U002.md#msy23-u002) with the affiliated invertibility and evaluation theorem in [MSY23-U004](../literature/MSY23/Yin_U004.md#msy23-u004).
The latter's same-unit image equals the affiliated division closure.
The tuple is only bounded here; neither a formal selfadjoint involution on its evaluated free field nor generation of the ambient algebra is used.

For the outer action on the algebraic tensor product, each Psi_i is a bimodule map.
The identity
\[
\delta(vw)=(\delta v)w+v(\delta w)
\]
and its inverse analogue verify rational-expression induction without presupposing that the derivative tensors are independent of the chosen expression.
In the converse, balancing over X_i kills every Psi_i term.
The right-F-linear coefficient functional in [C_F0035-P1](../../claims/Yin_C_F0035_v1.md#yin_c_f0035-p1) applies because F is a same-unit division subring; it does not require F central or U a domain.

For finitely many first factors, an affiliated row G gives the bounded regular left denominator (1+GG*)^(-1/2).
An affiliated column C of second factors gives the bounded regular right denominator (1+C*C)^(-1/2).
Matrix affiliated functional calculus makes the respective cleared products bounded.
The denominators are injective with dense range and are units in U; bounded inverses are unnecessary.
Clearing on the outer legs commutes with every Psi_i.
Thus a kernel tuple becomes a bounded-vector tensor tuple to which finite-rank-cycle injectivity applies.
Inverting the outer actions proves uniqueness and then rational-expression independence.

With the inner product linear in the second variable, h corresponds to the bounded functional q -> tau(hq), whose Riesz vector is h*.
This makes Theta a complex-linear bijection from H tensor_alg H to bounded finite-rank operators.
Trace cyclicity gives
\[
[\rho(X_i),\Theta(g\otimes h)]q
 =gX_i\tau(hq)-g\tau(X_i hq)
 =\Theta(\Psi_i(g\otimes h))q.
\]
All pairings are defined by L2 times L2 in L1 and bounded multiplication.
The inclusion of H tensor_alg H in U tensor_C U is injective.

For rational u, adding u to the two finite lists to be cleared gives a=su and b=ut in M and the certificate tensors s k_i t.
Conversely the tensor of any finite-rank certificate can be divided by s on the first leg and t on the second, giving exactly delta(u).
The proof therefore establishes the existential quantifier in (A3), and subtracting two solutions proves fixed-fraction uniqueness.
It does not assert that a prescribed fraction clears all tensor factors into L2.

## Part B: sharpness and the all-M obstruction

For the stated free pair, both h and S are atomless bounded selfadjoint variables, so the accepted entropy interface gives maximal Delta.
The inverse q=h^(-1) lies in U but not H because its squared L2 norm is the divergent integral of t^(-2).
The equality S=q(hSh)q places S in F.
The spectral cutoffs e_n make (e_n q)(hSh)(q e_n)=e_n S e_n elements of W*(h,hSh); their strong limit is S, proving generation.

The noncommutative operator expansion
\[
[R,BRT+TRB]+[B,RTR]=[RBR,T]
\]
was checked term by term.
It transfers a finite-rank cycle for (h,hSh) to the base pair.
Injectivity and dense range of R then give T_Y=0.
Thus the sandwich tuple has maximal Delta.

For the trivial fraction of S, the transformed base-pair cycle forces R T_Y R=P, with the stated sign.
Evaluating at Omega would give an H vector v=T_Y h satisfying v h=1.
In U this forces v=q, contradicting q not in H.
This establishes failure of the actual operator certificate independently of the derivative interpretation.
The derivative interpretation also agrees: k_Y=q tensor q, while k_h=-q tensor S-S tensor q.

For the good fraction s=t=h, the tensors
\[
l_Y=1\otimes1,\qquad l_h=-1\otimes Sh-hS\otimes1
\]
give, after cancellation, hS tensor h-h tensor Sh.
Hence T_Y=P and T_h=-PSh-hSP have exactly the required right side.

Finally, an all-M operator D_Y with the two specified generator commutators would satisfy
\[
h\bigl(D_Y(Sh\Omega)-S D_Y(h\Omega)\bigr)=\Omega.
\]
Every input is bounded, so all terms exist under the proposed hypothesis.
The vector in parentheses would again be q, which is not in H.
This contradiction needs no closability or adjoint-domain assumption.

## Part C: exact analytic interfaces and all domains

The restriction D_{i,0} is closable because its adjoint contains M Omega.
In the maximality argument, a common right denominator makes the ranges of all finite-rank T_i bounded.
Right multiplication commutes with the left X_i, so each transformed tuple remains a cycle.
The operators D_{j,0} S_i are bounded finite rank because their finite-dimensional ranges lie in the actual domain.
The trace of each bounded finite-rank commutator vanishes.
Testing the resulting trace identity with independent c,e in M kills every T_j.
This step uses actual finite-rank operators throughout.

For [C_F0034-P1](../../claims/Yin_C_F0034_v1.md#yin_c_f0034-p1), E=V_i=M Omega are dense left M-modules and the adjoint and generator hypotheses all hold.
The proof's closability, common-multiple equations, product identity, inversion and coordinatewise rank statements were inspected.
Its underlying [C_F0031-P1](../../claims/Yin_C_F0031_v1.md#yin_c_f0031-p1) cancels regular factors by taking the bounded finite-rank closure of a dense restriction of a closable operator.
This is valid without assuming that Hilbert density alone is graph density.
The inverse-closed finite-defect algebra contains the generators, giving every-fraction finite rank for rational u.

For [C_F0033-P1](../../claims/Yin_C_F0033_v1.md#yin_c_f0033-p1), the normality, generation, dense-module closability and dual identities all match; equality of the two fractions supplies sb=at.
Its proof and the local norm/weak-continuity mechanism of [C_F0032-P1](../../claims/Yin_C_F0032_v1.md#yin_c_f0032-p1) were inspected.
In this application E=M, so the windows may be taken equal to M.
Normality supports the bounded entire-function commutation argument, and generation supports the extension to all bounded left coefficients.
Neither premise is silently used in Part A.

The fundamental identity makes actual finite-rank defects into the Part A certificate.
This proves the reverse implication without invoking an older rationality conclusion.
Tensor uniqueness then identifies their tensors with s k_i(u) t.
Their membership in H tensor_alg H for every fraction is a consequence of this analytic argument.

Each natural domain contains M Omega because b,t are bounded and that space lies in the closure's domain.
For a bounded representative K, the adjoint test vector
\[
b^*\widehat D_i^*(s^*\eta)-t^*\widehat D_i^*(a^*\eta)
\]
is defined for every bounded eta.
Its equality to K*eta on the dense bounded-vector tests gives equality of the raw expression to K on the entire natural domain.
This proves the claimed extension without approximating bq and tq simultaneously in graph norms.

For bounded f, M Omega is a core for the specified closure by definition.
Applying the bounded commutator identity along a graph-convergent sequence proves invariance of the full closed domain.
The converse follows by restriction.
No arbitrary larger closed extension is used.

## Finite-Fisher inputs and dependency limits

The analytic portions of [C_F0022, Sections 2--3](../../claims/Yin_C_F0022_v1.md#2-sources-and-the-additional-analytic-input) were checked for their actual content, rather than inferred from that Claim's assessment.
The accepted underlying interfaces were inspected in [MS23-U001](../literature/MS23/Yin_U001.md#ms23-u001), [Dab10-U002](../literature/Dab10/Yin_U002.md#dab10-u002), and [Voi98-U003](../literature/Voi98/Yin_U003.md#voi98-u003), at the conjugate/normalized-dual, contraction-estimate and free-extension scopes respectively.

In particular, the tensor-leg convention yields (D_i^0)*p=p xi_i-D_i^0p.
The constants 4 and 5 follow from the selfadjoint contraction estimate and splitting into real and imaginary parts; these are operator-norm-to-L2 estimates.
Kaplansky approximation produces bounded images, and weak closedness of the actual Hilbert graphs gives both all-M domains.
Dense adjoint tests give bounded-set weak continuity and the generator identities on M.
Freely adjoining one semicircular variable handles d=1 at the printed two-variable estimate's scope.
The polynomial core lies in M, so taking the closure after restriction to M recovers exactly the canonical Hilbert closure.

The source free-field theorem, finite-tracial affiliated and matrix foundations, the atomless-free entropy comparison/additivity, algebraic-freeness/conjugate interface and the Dab10 closed-real-derivation functional-calculus foundation remain accepted external inputs.
Their relevant statements, hypotheses and applications were inspected through the named fixed source units; this review does not re-audit their complete original literature proofs or perform a new primary-PDF audit.

The dependency graph is acyclic: MSY23 and the tensor equalizer supply Part A; standalone fraction calculus and the normal-generator fundamental identity connect actual dual defects to Part A; the finite-Fisher analytic construction verifies (D).
C_F0022's final rationality assertion, C_F0024's final rationality assertion and C_F0013's final rationality assertion are not premises.
Historical extraction and comparison references do not add reverse edges.

## Conclusion

The complete statement and argument of Yin_C_F0068_v1 pass this independent mathematical review at the exact scopes bound above.
No unresolved mathematical defect was found, and no repair is required by this review.
The checked argument supports project assessment proved with review status independently reviewed for Parts A, B and C together.

This finding supports an explicit adopting Claim decision; the review itself does not select that decision, change an older Claim's proof, complete a Task or assert novelty.
The sharp distinction between SOME in the Delta-only certificate and SOME/EVERY under (D) is essential.
The bounded canonical dual operators are not asserted to act boundedly on all H, and no equality with scalar division closure inside M is established.

The work was mathematical reading and reconstruction, without formal verification, numerical evidence or external human peer review.
No target Claim, other mathematical material, navigation or Git state was changed by this reviewer.

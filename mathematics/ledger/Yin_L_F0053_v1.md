---
author: Yin
---
# Full-source audit comparison for condition A and normal bounded-vector domains

Date: 2026-10-16.
Yin requested full audits of Mai15 and MSW17, with particular attention to selfadjointness, the normal implication A to S and possible proof reuse.
Two source readers separately reviewed the retained 44-page Mai15 and 26-page MSW17 artifacts, and root rechecked the central adjoint/energy interfaces and the reported tensor-leg issue.
The source records disclose the actual reading and proof scope, corrections and retained external inputs.
This comparison is a synthesis of that work, not a new proof of A implies S or an independent project-theorem acceptance.
The [Mai15 whole-paper source assessment](../audits/literature/Mai15/Yin_U003.md#whole-paper-inspection-scope) and [MSW17 source assessment](../audits/literature/MSW17/readme.md) own the detailed source findings.
The previous [literature collection](Yin_L_F0051_v1.md) retains its earlier, shallower reading scope.

## Exact mathematical question

Let X be a finite bounded generating tuple in a finite tracial von Neumann algebra M, let H=L2(M,tau), and put P=C<X,X*>.
A means that complex-linear outer derivations delta_i:P -> H tensor_2 H satisfy delta_i(X_j)=delta_ij 1 tensor 1 and have actual vacuum adjoints delta_i*(1 tensor 1) in H.
S means that densely defined D_i satisfy M Omega subset Dom D_i intersect Dom D_i* and [X_j,D_i]=delta_ij P_Omega on all bounded vectors.
The question concerns the canonical operators D_i=-closure((id tensor tau)delta_i), or another system with the stated actual domains.
Neither merely dense domains nor an arbitrary extension with different values answers it.

## Which selfadjointness assumptions do actual work

| Step | Actual structural requirement | Consequence for normal A |
| --- | --- | --- |
| Mai15 Lemmas 4.3 and the first part of 4.7: actual adjoint-domain multiplication and algebraic tensors in Dom delta* | Weakly dense unital star domain, outer Leibniz rule and actual vacuum; no reality or selfadjoint generating tuple | Directly applicable. The derivation is closable, but this does not give a uniform contraction estimate. |
| MSW17 Proposition 2.3: descend formal difference quotients through evaluation | Conjugate tests and a star-closed test algebra; selfadjoint generators make the source's unstarred polynomial algebra star closed | A already includes descent on the represented star algebra. No new descent obligation is needed there. |
| MSW17 Proposition 2.4: highest-degree reduction of a polynomial relation | Well-defined coordinate derivations on the holomorphic algebra and their Leibniz word formulas | The argument itself needs neither selfadjoint nor normal generators. It concerns C<X>, not algebraic freeness of the generally related list (X,X*). |
| Mai15 Theorem 4.9: two contraction estimates | A real derivation, algebraic core-tensor range, actual vacuum and zero coassociativity defect | The tested x is arbitrary, not required selfadjoint. General normal A does not automatically supply these structural hypotheses. |
| MSW17 Lemma 3.4 | Ordinary selfadjoint free difference quotients, hence the preceding real/coassociative structure | Exact constants for arbitrary complex polynomials are supported by the fully checked Mai15 proof; a literal citation of Dab10's selfadjoint/unitary formulation alone is insufficient for that full range. |
| [Mai15 Proposition 4.14](../audits/literature/Mai15/Yin_U003.md#zero-divisor-survival) and MSW17's two-sided kernel reduction | Both xu=0 and x*v=0, actual adjoint estimates and bounded approximation | The tested x or polynomial P need not be selfadjoint. Left and right kernel projections must be kept distinct. |
| MSW17 Proposition 3.9 and the entropy-dimension passage | Selfadjoint tuple, semicircular regularization and the selfadjoint free-Fisher/non-microstates entropy interfaces | The printed argument does not transfer by replacing the tuple by an arbitrary normal one. |
| [Mai15 directional-gradient proof](../audits/literature/Mai15/Yin_U003.md#directional-gradients) | Real directions supply real coassociative derivations; finite-chaos degree and kernel contractions supply descent | Selfadjointness of the final Wigner element is used to express the final atom conclusion through a real spectral measure. The zero-divisor mechanism has a wider tested-element scope. |

Thus the abstract analytic bottleneck is not the requirement that every element tested in an estimate be selfadjoint.
It is the combination of reality, actual iterated-domain control and the coassociative energy identity.
The source proofs explicitly distinguish these roles.

## Exact analytic interface and the remaining normal obstruction

For a real, algebraic-core-valued coassociative derivation with xi=delta*(1 tensor 1), [Mai15-U002](../audits/literature/Mai15/Yin_U002.md#mai15-u002) checks
\[
 \|\delta^*(a\otimes1)\|_2,\ \|\delta^*(1\otimes a)\|_2
 \le\|\xi\|_2\|a\|,
 \qquad
 \|(\mathrm{id}\otimes\tau)\delta(a)\|_2,
 \|(\tau\otimes\mathrm{id})\delta(a)\|_2
 \le2\|\xi\|_2\|a\|.
\]
The proof uses T(a)=delta*(a tensor 1) and the identity
\[
 \|T(a)\|_2^2=\langle T(a^*a),\xi\rangle,
\]
with the source's inner product linear in the first variable.
Power iteration on a*a then supplies the exact constants for arbitrary a.
The separate [C_F0072 graph-restoration theorem](../claims/Yin_C_F0072_v1.md#statement) turns two operator-norm-to-L2 contraction bounds into both actual canonical bounded-vector domains.
This gives a complete route in the selfadjoint source setting and in other settings where all those structural hypotheses have actually been established.

For a normal coordinate, the starred derivative is the phase
\[
 \delta_i(X_j^*)=\delta_{ij}k_j,
 \qquad k_j(z,w)=\frac{\bar z-\bar w}{z-w}.
\]
The original delta_i need not be real, and k_j need not be a finite algebraic core tensor.
[C_F0076](../claims/Yin_C_F0076_v1.md#statement) supplies actual closed tensor-leg domains and pure coassociativity, but that is not all of Mai15 Definition 4.8 and does not supply reality.
Realifying delta_i mixes it with its conjugate derivation; the mixed defect need not vanish.
The earlier mixed-energy and marginal-only obstruction results therefore remain relevant.

There is a different real algebraic derivation available, namely the liberation reweighting delta_i^lib=i Psi_i delta_i.
Its actual vacuum and bounded-vector estimates are already established in [C_F0063 Appendix A](../claims/Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions).
Its defect is
\[
 (\delta_i^{\rm lib}\otimes\mathrm{id})\delta_i^{\rm lib}
 -(\mathrm{id}\otimes\delta_i^{\rm lib})\delta_i^{\rm lib}
 =\mathrm i\kappa\delta_i^{\rm lib},
 \qquad \kappa(a\otimes b)=a\otimes1\otimes b.
\]
Mai15 Theorem 4.9 is consequently not a ready-made replacement for that separate controlled-defect proof.
Recovering an original contraction by inverting the inner multiplier would require control of its generally singular inverse.
The audit has not removed that obstacle or resolved general normal A implies S.

## A more specific continuing sufficient-condition route

The [last section of D_F0002](../drafts/Yin_D_F0002.md#the-power-iteration-mechanism-from-mai15-and-the-missing-quadratic-estimate) retains the complete working calculation rather than treating it as an accepted new Claim.
For a general A derivation define the actually existing maps T_ell(a)=delta*(a tensor 1) and T_r(a)=delta*(1 tensor a).
The general starred adjoint formula and the Leibniz rule already give
\[
 \limsup_{m\to\infty}\|T_\ell(a^m)\|_2^{1/m}\le\|a\|,
 \qquad
 \limsup_{m\to\infty}\|T_r(a^m)\|_2^{1/m}\le\|a\|.
\]
This part of Mai's power-iteration strategy needs neither reality nor normality.
A sufficient remaining target would be uniform quadratic inequalities
\[
 \|T_\ell(a)\|_2^2\le C_\ell\|T_\ell(a^*a)\|_2,
 \qquad
 \|T_r(a)\|_2^2\le C_r\|T_r(a^*a)\|_2.
\]
The working calculation derives both contraction bounds and then S from these two inequalities.
It does not prove them under normal A, assert their necessity for S, or remove a mixed defect by an inequality without justification.
Its value is to isolate the automatic growth condition from the still-missing quadratic control.

## Source corrections that affect use

The detailed corrections, tests and corrected proof chains belong to the respective U records.
The following are the consequential reuse boundaries.

- Mai15 Lemma 4.11 and its application write T with codomain M, although T(1)=xi is only assumed in L2.
  The proof uses only Hilbert norms, so replacing the codomain by L2 repairs the application without changing the constants.
- Mai15 Corollary 4.12 omits the actual vacuum-adjoint assumption while using delta*(1 tensor 1) and Theorem 4.9.
  Its usable statement includes that assumption.
- Mai15's complex-direction notation has conjugation and field/Wick-vector issues; the [directional-gradient record](../audits/literature/Mai15/Yin_U003.md#directional-gradients) gives the corrected conventions.
  The real-direction proof needed for the main finite-chaos result survives these corrections.
  The [continuity estimate in Lemma 5.9](../audits/literature/Mai15/Yin_U003.md#degree-reduction) also needs its direction norm factor.
- MSW17 Proposition 3.9's p.17 displayed limit uses the wrong tensor leg after taking P(X^t)*v.
  The correct first-order norm involves (partial P)(X)*(v tensor 1), equivalently (v* tensor 1)(partial P)(X), rather than componentwise star followed by right multiplication on the second leg.
  The reported counterexample checks the displayed identity; it does not by itself refute the entire constant-16 inequality.
  The corrected quantitative estimate yields the same alpha=0 conclusion used by the main theorem.
- The projective-norm limsup in MSW17 Proposition 3.9 requires lifting a near-optimal evaluated tensor decomposition and controlling the evaluation-kernel remainder.
  The source record supplies this omitted justification without assuming algebraic independence in advance.
- MSW17 Example 3.13 misses a factor 2 in its displayed squared-norm calculation, and Appendix A.1 reverses two implication labels and names the wrong assumption.
  The corrected zero conclusions and algebraic equivalence remain valid.

The uncorrected quantitative display in MSW17 is therefore not adopted merely because the paper has now been read in full.
The qualitative no-zero-divisor chain is assessed with the corrected tensor orientation and the retained external semicircular regularization input.
The full-source records also retain their other standard external inputs rather than claiming recursive audits of all cited literature.

## Scope and disposition

The source-version search checked the exact arXiv records and bounded title/erratum searches on 2026-10-16.
No identified author-issued erratum was obtained by this search; the corrections above are local inspection findings, not author-confirmed changes.
The audit target is the retained preprint artifact of each work, not an unperformed collation of MSW17's publisher typesetting.
No source PDF bytes or fixed earlier U versions were changed.

The directly reusable results are the general adjoint-domain interfaces, the selfadjoint quotient/relations argument and the correctly scoped real-coassociative estimates.
The full normal bounded-vector problem remains unresolved at this point.
Any future adoption of a new quadratic estimate or a changed canonical-domain proof requires its own complete mathematical argument and review at that scope.

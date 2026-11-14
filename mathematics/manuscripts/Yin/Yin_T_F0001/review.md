---
author: Yin
---

# F0001 Manuscript Review

This record retains actual mathematical scrutiny of the current manuscript.
It is not a fixed R review, a source audit or a proof source.
Fixed Claim, literature and project-review evidence remains at its responsible mathematical home.

## Current Review Boundary

The current manuscript is the working-tree TeX in [paper/main.tex](paper/main.tex) and its included section files, as inspected for the scoped reviews below.
The scoped entries identify the inspected objects, locations, actual relationships and limits.
Dates are retained where recorded; the arbitrary-bounded-tuple and circular-counterexample entries have no separately recorded date.
No entry asserts independent review of the current full paper.
The current labels `thm:intrinsic-analytic`, `thm:analytic` and `rem:boundary-interpretation` are numbered Theorem 1.7, Theorem 1.9 and Remark 3.4, respectively.
The Hochschild remark follows the proof of Theorem 1.4 in `paper/sections/maximal-delta.tex`.
Section 2 has five subsections ordered from division closures and the free field through coordinate maps, affiliated fractions and finite-rank tensor realizations to maximal Delta and free-field realization.
The tensor and trace interfaces are in Subsection 2.4, the balanced-tensor equalizer `lem:equalizer` is Lemma 2.2, and the free-field realization `lem:free-field` is Lemma 2.9.
The current Section 5 order and domain conditions have a [scoped reorganization check](#liberation-gradients-reorganization-20261028).
External citation applications and source-level evidence are mapped in [citation.md](citation.md).
The latest build facts are in [paper/readme.md](paper/readme.md), separate from mathematical review.

## Theorem 1.4: Maximal-Delta Criterion

<a id="delta-every-fraction-tensors-20261015"></a>
### Every-fraction tensor condition

On 2026-10-15, the authoring agent self-reviewed the five-condition statement of Theorem 1.4, the Section 3 proof and its direct use in Section 4.
The checked scope included the universal fraction-pair quantifier, tensor spaces, opposite-factor multiplication, regular denominator clearing and the implication from every-fraction affiliated witnesses to a bounded-tensor witness for one pair.
This was a scoped manuscript check, not an independent proof review or whole-paper audit.

<a id="delta-bounded-fraction-tensors-20261015"></a>
### Bounded tensor witnesses

On 2026-10-15, the authoring agent self-reviewed the existential bounded-tensor condition in Theorem 1.4 and its five-step proof cycle.
The check covered the tensor-to-finite-rank correspondence, the sign \(T_i=-\Theta(\ell_i)\), inverse outside multiplication and the finite-rank converse.
It did not change the theorem's statement or establish independent review.

<a id="tensor-trace-interfaces-20261018"></a>
## Tensor and Trace Interfaces

On 2026-10-18, the authoring agent checked Subsection 2.4 and its direct uses in the current operator proofs.
The checked interfaces are the Theta bijection, its Hilbert-Schmidt extension, its bimodule and commutator actions, and the extension of tau to H.
Lemma 4.5 uses the adjoint-domain condition for closability and the bounded finite-rank closure of Lemma 4.2, after which Theta supplies the algebraic L2 tensor.
Lemma 6.5 uses the closed graph theorem, adjoint-generator intertwining, Kaplansky density and weak closedness of the graph in the module extension.
Lemma 6.2 proves coordinate rank independence using injective left factors and dense-range right factors.
The tau extension is used in the liberation contraction, now Lemma 5.2, for \(\tau(v_r\eta)\) with \(\eta\in H\), while the product trace in Definition 2.7 applies tau only to elements of M.
Lemma 2.2 retains the balanced-tensor equalizer statement, proof and label `lem:equalizer` used by Theorem 1.4.
This was a scoped authoring-agent check of the retained interfaces and their sufficiency for the current proofs, not an independent whole-manuscript review.

<a id="normalized-liberation-criterion-20261018"></a>
## Theorem 1.7: Normalized Liberation Criterion

The corresponding fixed research statement and complete added argument are retained in [C_F0079 v5](../../../claims/Yin_C_F0079_v5.md#statement), with its [separately arranged mathematical finding](../../../audits/reviews/Yin_R_F0093_v1.md#whole-v5-finding).
That finding concerns the fixed research mathematics; the manuscript-local checks below retain their stated authoring-agent relationships and dates.

On 2026-10-18, the authoring agent checked the sum normalization in Definition 1.6, the accompanying construction in Section 4, the closure identity of `lem:tensor-images-l2` and the four-condition proof of Theorem 1.7 in the current TeX.
The check also covered the affected normal-conjugate, ordinary-dual and example applications.
The existing mathematical environments were preserved.

The normalization is \(\sum_i L_i=P_\Omega\) on \(\M\Omega\).
The construction is stated as Lemma 4.1, `lem:liberation-normalization`, with the correction and every corrected operator defined on \(\M\Omega\).
On 2026-10-25, a local authoring-agent check of the expanded proof verified generator commutation, the normalized sum and the common adjoint domain through the displayed inner-product identity.
This check concerns the extracted lemma and its definition interface, not a new review of the other Section 4 proofs.
For \(C:=\sum_iL_i-P_\Omega\) on that domain, the defining relations give \([X_j,C]=0\).
Replacing \(L_i\) by \(L_i-C/d\) on \(\M\Omega\) preserves every generator relation and the common adjoint domain, since the adjoints of the finite linear combinations contain \(\M\Omega\).
The resulting sum is \(P_\Omega\), so existence of a normalized system imposes no additional assumption on \(X\).
Normalization need not determine the system: for \(d\) at least two, adding \(cI\) to one coordinate and subtracting it from another preserves the defining conditions.

<a id="liberation-arbitrary-tuple-20261018"></a>
### Arbitrary bounded tuples

Definition 1.6 applies to every bounded tuple \(X\in\M^d\).
The boundedness of the \(X_j\) preserves \(\M\Omega\) and makes the displayed compositions meaningful; the definition uses neither normality nor generation of \(\M\).
The current criteria add normality or regularity of every scalar shift only where their proofs use it.
The density used in Proposition 4.4 and Lemma 4.5 is that of \(\M\Omega\) and \(t\M\Omega\) in \(H\), independent of generation by \(X\).

For a rational \(u\) and any \(Q=(s,a,b,t)\), Theorem 1.4(3) gives \(h:=a\otimes t^{\mathrm{op}}-s\otimes b^{\mathrm{op}}=\sum_i\Psi_i(\ell_i)\).
Lemma 4.5's proof gives \(\ell_i\) in the algebraic L2 tensor product and \(\overline{\Phi_i(h)}=\Theta(\Psi_i(\ell_i))\).
Since \(\Phi_i(h)=-\Gamma[Q,L_i]\) restricted to \(\M\Omega\), the common-domain argument of Lemma 6.1 makes the full natural-domain fraction commutator closable.
Its closure extends the bounded operator \(-\overline{\Phi_i(h)}\), whose domain is all \(H\), and therefore equals it.
Thus \(T_i:=-\Theta(\ell_i)\) satisfies \([\rho(X_i),T_i]=\overline{\Gamma[Q,L_i]}\), proving (1) implies (4) of Theorem 1.7.
For (4) implies (3), summing on \(\M\Omega\), using the normalization on \(b\M\Omega\) and \(t\M\Omega\), and extending the resulting bounded identity by density proves the criterion.
The unchanged implications (3) implies (2) and (2) implies (1) close the cycle.
Lemma 6.1 is independent of this theorem, so its forward reference introduces no circular dependency.
The individual finite-rank preimages in (4) are the same tuple as in (2), by the existing certificate uniqueness.

The name normalized is an explicitly defined manuscript convention.
The inspected Voi99 Definition 13.1 and Remarks 13.2, printed pp.160-161, impose neither a sum condition nor zero vacuum; [Voi99-U001](../../../audits/literature/Voi99/Yin_U001.md#bounded-liberation-dual-system) retains that source interface.
MS23 Definition 2.4 uses normalized for ordinary duals with \(D_i\Omega=0\), as retained in [MS23-U001](../../../audits/literature/MS23/Yin_U001.md#ms23-u001) and checked against [the available preprint, p.7](https://arxiv.org/pdf/2203.00547).
The targeted literature search found no relevant use establishing canonical or normalized as a standard name for the present sum condition; no priority claim follows from that limited search.
The local convention is written explicitly and is not attributed to either source.

This is a scoped authoring-agent self-review, not an independent review or a revision of the fixed C_F0079 assessment.

<a id="liberation-sum-explanation-20261019"></a>
## Theorem 1.7: Summing the Fraction-Commutator Closures

On 2026-10-19, the authoring agent checked the introductory explanation of how assertion (4) of Theorem 1.7 yields a finite-rank solution in assertion (3) against the unnumbered sum identity in its proof in Section 4.
Assertion (4) supplies finite-rank \(T_i\) with \([\rho(X_i),T_i]=\overline{\Gamma[Q,L_i]}\).
Normalization first gives their sum identity on \(\M\Omega\); the commutators and \(\Gamma[Q,P_\Omega]\) are bounded, so density extends the identity to \(H\) and yields the solution in (3).
The introductory display uses this bounded identity under assertion (4), without asserting an everywhere-defined sum for arbitrary unbounded fraction-commutator closures.
This is a scoped authoring-agent check of the explanation, domain passage and direct references, not an independent or whole-manuscript proof review.

<a id="liberation-regular-shifts-20261018"></a>
## Liberation Dual Systems: Regular Scalar Shifts

On 2026-10-18, the authoring agent checked `prop:liberation-delta`, `lem:tensor-images-l2` and Theorem 1.7 with \(X_i-\lambda\) regular for every index \(i\) and every complex lambda.
The exact mathematical statement and argument are [C_F0079 v4](../../../claims/Yin_C_F0079_v4.md#statement), with the fixed [R_F0058 v4 self-review](../../../audits/reviews/Yin_R_F0058_v4.md#finding).
The manuscript check covered the three statements, their proofs and applications, and the matching abstract, introduction, conventions and organization record.
The checked theorem retains the universal fraction-pair quantifier and uniqueness for each fixed pair; the normalization and fourth equivalent condition are covered by the preceding review entry.

Regularity is invertibility in L0(M), without a bounded-inverse requirement in M.
Lemma 4.3 already has this scalar-shift hypothesis.
It excludes nonzero finite-dimensional invariant subspaces for left and right multiplication, giving individual tensor injectivity.
Bounded multiplication preserves H for a nonnormal \(X_i\) as well, so the quotient-factor recovery argument applies.
Proposition 4.4 uses this hypothesis directly after coordinate separation, without a spectral argument.
Lemma 4.5 still uses the common adjoint domain, finite-rank closure on the dense subspace \(t\M\Omega\), Theta and regular cancellation.
Neither proof needs normality, generation of M or commutator relations for adjoint generators.
Theorem 1.4 applies to arbitrary bounded tuples, so the proof of Theorem 1.7 retains its implication cycle and uniqueness.

The current Section 5 separates the gradient-to-dual construction in Lemma 5.2 from the ordinary-conjugate conversion in Lemma 5.6.
Proposition 5.3 explicitly assumes normality and nonatomicity, which supply regularity of every scalar shift.
Lemma 5.6 proves nonatomicity from ordinary conjugate variables, so Corollary 5.7 inherits that regularity; the [2026-10-28 check](#liberation-gradients-reorganization-20261028) records this reorganization.
The ordinary dual-system criterion and its proof retain their existing hypotheses.
Lemma 6.3 identifies the finite-rank solutions with the fraction-commutator closures, so the liberation and ordinary-dual criteria remain consistent.
The normalization argument is now Lemma 4.1 in the manuscript.
The nonnormal liberation-gradient counterexample remains in [C_F0083 v2](../../../claims/Yin_C_F0083_v2.md#statement), outside the manuscript.

No unresolved correction was found in this scope.
This is authoring-agent self-review with access to the developing proof and fixed inputs, not an independent full-paper or source audit.

<a id="analytic-proof-via-liberation-20261018"></a>
## Theorem 1.9: Dual-System Proof

On 2026-11-14, the authoring agent self-checked the proof of Theorem 1.9 through the conjugate-variable criterion, the added Lemma 6.6, the retained fraction and fundamental-identity lemmas and the corresponding introduction and organization references.
This is a scoped authoring-agent self-review of the current working-tree manuscript, not an independent review or a change to any fixed Claim, R or U assessment.
The current Section 6 contains the fraction-domain, fraction-rank, identification and fundamental-identity lemmas used by the proof.

Lemma 6.2 uses common regular multipliers \(xs=ys'\) and \(tp=t'q\), giving \(xa=ya'\) and \(bp=b'q\) in \(M\).
The identity \(x\Gamma[Q,D]p=y\Gamma[Q',D]q\) is first asserted only on \(\M\Omega\).
If the closure for \(Q\) has finite rank, injectivity of \(y\) makes the restriction for \(Q'\) to \(q\M\Omega\) finite rank.
This restriction is densely defined and closable by Lemma 6.1, so Lemma 4.2 gives a bounded finite-rank closure on all \(H\).
The full natural-domain closure extends this operator and hence equals it.
Only after both closures are bounded is the common-denominator identity extended to \(H\).
Injective left multiplication and dense-range right multiplication preserve finite rank, proving equality of ranks.
The current proof uses this lemma for rank independence; the certificate converse applies to the prescribed fraction pair directly.

Lemma 6.3 assumes only the ordinary dual relations and the common domain and adjoint-domain condition, without normality or generation.
For a finite-rank solution, \(\ell_j=-\Theta^{-1}(T_j)\) has the sign required by Lemma 3.3.
After Lemma 3.1 clears all tensor factors, applying \(c\otimes e^{\mathrm{op}}\mapsto cD_i(e\xi)\) uses only inputs in \(\M\Omega\).
The dual relations give \(-s'\Gamma[Q,D_i]t'\xi=\Theta(\ell'_i)\xi=-s'T_i t'\xi\).
Regular cancellation and density of \(t'\M\Omega\) identify the bounded \(T_i\) with the closure on the entire natural domain, using Lemma 6.1.
No rationality criterion is used in this identification lemma.

Lemma 6.6 specializes the spectral-pinching argument in [C_F0037](../../../claims/Yin_C_F0037_v1.md#yin_c_f0037-p1) and the vacuum calculation in [C_F0070 Part C](../../../claims/Yin_C_F0070_v1.md#statement).
The common adjoint-domain hypothesis gives closability of the restrictions to M Omega; Lemma 6.5 supplies operator-norm-to-L2 boundedness, not boundedness on H.
Testing against the dense adjoint domain gives weak continuity on uniformly bounded strongly convergent nets.
For $A=[D_i^\circ,x^*]+\delta_{ij}K_x$, Jacobi's identity gives $[A,x]=0$; Lemma 6.4 and bounded Kaplansky approximation extend commutation to the coordinate von Neumann algebra.
Spectral pinching bounds the diagonal blocks of the starred commutator by $2\varepsilon c_\xi$, uniformly in the number of cells, and the pinched phase kernel tends to zero in Hilbert--Schmidt norm.
This proves the starred commutator formula on the specified domain without assuming its boundedness in advance.
The commutator product rule then defines well-defined derivations on the represented starred polynomial algebra, and the vacuum pairing gives $\partial_i^*(1\otimes1)=-D_i^*\Omega+(D_i\Omega)^*$ with the generator-first sign.
The argument uses the phase-kernel construction in Section 5 but neither its conjugate-variable hypothesis nor Theorem 1.9.

Lemma 6.7 defines \(K_i=[\rho(X_i),D_i|_{\M\Omega}]\), \(C=\sum_iK_i-P_\Omega\) and \(L_i=K_i-C/d\).
The adjoints of these operators contain \(\M\Omega\), as checked by the displayed \(K_i\) adjoint formula.
The generator-first sign follows from \([\rho(X_i),P_\Omega]=[X_i,P_\Omega]\) and Jacobi's identity.
The sum of the \(L_i\) is \(P_\Omega\) on \(\M\Omega\).
Normality and generation are used in Lemma 6.5 to make \(C\) left M-linear, which kills its fraction commutators on \(\M\Omega\).
The equality between the \(L_i\) fraction commutator and the commutator with \(\rho(X_i)\) is first proved on \(\M\Omega\).
The full closure identity follows only when the ordinary fraction commutator has bounded closure, using Lemma 6.1.
The normal spectral-atom argument proves regularity of every \(X_i-\lambda\) directly from the ordinary dual relation.
The prior fundamental summed identity is retained as a consequence.

For Theorem 1.9, Lemma 6.6 verifies the hypothesis of Corollary 5.7.
The implication (1) implies (3) uses the every-fraction certificate conclusion inherited from Proposition 5.3 and then applies Lemma 6.3.
For (3) implies (1), the summed identity in Lemma 6.7 makes the finite-rank ordinary fraction-commutator closures a certificate for the specified pair, so Corollary 5.7 and Proposition 5.3 give rationality.
Lemmas 6.1 and 4.2 give the equivalence of (2) and (3), and Lemma 6.2 supplies the rank statement.
Theorem 1.7 only uses Lemma 6.1 from this section, and the proofs of the Section 5 applications use no dual-system criterion, so the reorganized dependency has no cycle.
No unresolved mathematical correction was found in this checked scope.

<a id="liberation-gradients-reorganization-20261028"></a>
## Section 5: Liberation Gradients Before Ordinary Conjugate Variables

On 2026-10-28, the authoring agent self-reviewed the rewritten Section 5, its introductory references, citation uses and corresponding manuscript records.
The retained inputs are [C_F0082](../../../claims/Yin_C_F0082_v1.md#decision-self-reviewed), [C_F0063 Appendix A](../../../claims/Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions), the individual-algebra formulation in [C_F0083 v2](../../../claims/Yin_C_F0083_v2.md#statement), and the exact source interfaces mapped in [citation.md](citation.md).
Their fixed assessments and earlier review relationships are unchanged.
This is a scoped authoring-agent self-review, not an independent review, a new source-proof audit or a whole-paper certification.

Definition 5.1 explicitly requires the represented derivation on each \(\mathcal P_i=\operatorname{Alg}(A_i,B_i)\), not merely the common polynomial algebra, and its actual Hilbert adjoint with \(1\otimes1\) in the domain.
The signs \(j_i=-\gamma_i^*(1\otimes1)\), \(j_i^*=-j_i\) and \(\delta_i^*(1\otimes1)=\mathrm i j_i\) were checked using the manuscript's second-variable-linear inner product.
Lemma 5.2 retains the nonzero coassociativity defect, the energy identity and analytic polynomial approximation.
Convergence of the derivative of the approximate unitary product and closedness of \(\overline{\delta_i}\) justify its limit being zero.
The contraction bound and the actual core-adjoint formula give both operator-norm-to-L2 estimates.
Kaplansky approximation and weakly closed graphs then put \(\mathcal M\Omega\) in the domains of the actual closure and its adjoint.
The graph-core argument extends the generator commutators, and Lemma 4.1 supplies normalization.
The lemma does not assert that this last normalization preserves closedness of the chosen operators.
Proposition 5.3 separately assumes normality and nonatomicity; together these make every scalar shift regular.
Theorem 1.7 gives the criterion for every fraction pair, uniqueness for a fixed pair and its conclusions for any normalized system; Proposition 4.4 gives maximal Delta.

Definition 5.4 retains the ordinary starred-polynomial derivations and actual adjoint condition.
Lemma 5.5 retains the phase-kernel uniqueness proof.
The first part of Lemma 5.6 retains the Neumann-series domain check and direct nonatomicity proof, independently of maximal Delta.
Its second part forms \(\gamma_i^\circ=\Psi_i\partial_i\), uses the phase kernel to obtain algebraic tensor values, and uses Mai15 Lemma 4.3 for the actual polynomial adjoint vector \([X_i^*,\xi_i]\).
Thus \(j_i=[\xi_i,X_i^*]\) satisfies the polynomial moment identity.
Voi99 Remark 5.5(c), checked directly in the published pp.115-116 this round, extends the word-moment formula by bounded Kaplansky approximation.
The local test on \(urv\), for a represented relation \(r=0\), forces its evaluated tensor derivative to vanish.
This proves well-definedness on the full \(\mathcal P_i\), and the L2 moment bound gives its actual adjoint condition.
Lemma 5.6 therefore supplies both hypotheses needed by Proposition 5.3, giving Corollary 5.7.
The user-authorized change of the ordinary proposition to a corollary retains `prop:normal-conjugates`; all previous semantic labels and mathematical environments remain represented.
The three-main-theorem structure is unchanged.

Remark 5.8 retains the arcsine model and complete monomial obstruction and adds its zero liberation gradient, which places it under Proposition 5.3.
The earlier fixed and manuscript-review scopes for that example are preserved in the [remark entry](#arcsine-liberation-counterexample-20261018).
The corresponding introduction, numbering, terminology, source mapping and provenance links were checked against the current TeX.
Build diagnostics and their limits are recorded separately in [paper/readme.md](paper/readme.md).

<a id="dual-conjugate-section-order-20261018"></a>
## Section Order and the Dual-System Definition

On 2026-11-14, the authoring agent checked the order Section 4 for the liberation criterion, Section 5 for applications to liberation gradients and conjugate variables, and Section 6 for the ordinary dual-system criterion.
Section 5 retains its internal order: liberation gradients first, ordinary conjugate variables as a corollary.
Theorem 1.9 now uses Corollary 5.7 through the conjugate-variable conclusion of Lemma 6.6.
All existing mathematical environments and semantic labels are retained.

Definition 1.8 retains the common domain and adjoint-domain inclusion and the generator-first commutator relations preceding Theorem 1.9.
Containment of \(\mathcal M\Omega\) gives dense definition of each operator.
Theorem 1.9 states normality and generation separately.
The original hypothesis equation and its label remain in the definition.
Lemma 6.1 still uses only the common-domain hypotheses, so its forward use in Theorem 1.7 introduces no dependency cycle.
These are scoped authoring-agent checks, not independent proof or source audits.

<a id="conjugate-hypotheses-dual-comparison-20261018"></a>
## Conjugate-Variable Hypotheses and the Analytic Criteria

The 2026-10-18 check of the conjugate-variable hypotheses now refers to Lemma 5.6 and Corollary 5.7, in the sense of Definition 5.4.
On 2026-10-28, the authoring agent checked their explicit normality and generation hypotheses and the proof's choice of the actual derivations from that definition.
The corollary follows through L2 liberation gradients and Proposition 5.3; it no longer repeats the construction or applies Theorem 1.7 directly.
All previous semantic labels are retained.

The introductory comparison of Theorems 1.7 and 1.9 retains its previously checked content.
For the normalized system constructed in Lemma 6.7, the identity between \(\overline{\Gamma[Q,L_i]}\) and \([\rho(X_i),\overline{\Gamma[Q,D_i]}]\) is stated only when the ordinary fraction commutator has bounded closure.
Normalization gives the summed certificate, and Lemma 6.3 identifies the finite-rank witnesses with the ordinary fraction-commutator closures.
This does not infer finite rank merely from finite rank of a commutator.
The open question about ordinary dual systems under ordinary conjugate variables is retained.
This is a scoped authoring-agent presentation and deduction check, not an independent review of these earlier proofs.

<a id="introductory-dual-conjugate-definitions-20261018"></a>
## Introductory and Section 5 Definitions

The 2026-10-18 check of the introductory definitions remains applicable to Definitions 1.6 and 1.8 immediately before Theorems 1.7 and 1.9.
Their mathematical contents and semantic labels are retained, and the normalization construction remains in Section 4.
On 2026-10-28, the authoring agent checked the reorganized Section 5 definition interfaces and their introductory references.

Definition 5.1 now introduces L2 liberation gradients on each full coordinate algebra \(\mathcal P_i\), with represented well-definedness and the actual adjoint condition explicit.
The former ordinary conjugate-variable definition is retained verbatim as Definition 5.4.
It prescribes the starred-polynomial derivations and their generator values, requires the actual adjoint-domain inclusion and names \(\xi_i=\partial_i^*(1\otimes1)\).
Generation makes the domain dense in H.
This ordinary definition imposes no normality or reality hypothesis and makes no uniqueness claim for arbitrary nonnormal tuples.
The Section 5 results state their additional hypotheses separately.
The introductory references, conventions, organization and citation map now distinguish these two definitions and their compiled numbers.
This is a scoped authoring-agent check, not an independent proof or source review.

<a id="conjugate-dual-lemma-reorganization-20261016"></a>
## Section 6: Closable Module Commutation and the Fundamental Identity

On 2026-10-16, the authoring agent self-reviewed the closable module-commutation proof stated as Lemma 6.5.
The check covered the closed graph bound, adjoint-generator intertwining, Kaplansky approximation and Hilbert-space closedness in the module extension.
The same section check covered Lemma 6.7's adjoint domain for the residual operator, its closability and the Jacobi calculation yielding commutation with each generator.
It also checked the displayed signs and final fraction identity.
These are scoped authoring-agent checks, not independent or whole-manuscript proof reviews.

<a id="direct-classical-fuglede-20261016"></a>
## Lemma 5.5: Classical Fuglede Application

The 2026-10-16 authoring-agent check of the direct classical Fuglede step applies to the retained normal-adjoint uniqueness proof, now Lemma 5.5.
On 2026-10-28, the authoring agent checked this relocation and the unchanged proof.
Normality and the Hilbert-Schmidt hypothesis imply the bounded-operator hypotheses of Fuglede's theorem.
The intervening map \(z\mapsto S(z\Omega)\) is not used for this step.
This is a scoped applicability and exposition check, not a new source inspection or independent proof review.

<a id="fuglede-intertwining-consolidation-20261016"></a>
## Lemma 6.4: Bounded-Map Adjoint Intertwining

On 2026-10-16, the user authorized the one-sentence classical reminder and the adjacent bounded-map analogue now stated as Lemma 6.4, retaining label `lem:normal-intertwining`.
The authoring agent checked its bounded-map hypotheses and its uses in the module and normal-adjoint arguments, including the distinct normed domains.
The [citation map](citation.md) links the CS77 source interface.
No new source audit or independent proof review is claimed.

<a id="conjugate-nonatomicity-20261018"></a>
## Lemma 5.6: Direct Nonatomicity

The direct nonatomicity proof checked on 2026-10-18 is retained as the first part of Lemma 5.6.
On 2026-10-28, the authoring agent checked its preservation under the reorganization and its use of the ordinary Definition 5.4.
The actual adjoint condition, through [ACSY24-U003](../../../audits/literature/ACSY24/Yin_U003.md#derivation-adjoint-and-compression), gives a dense tensor-adjoint domain and hence closability of each \(\partial_i\).
For \(y=X_i-\lambda\), the Neumann series for \(r_\varepsilon=(y^*y+\varepsilon^2)^{-1}\) converges in operator norm and its derivatives converge in the Hilbert tensor product.
Multiplying its partial sums by \(\varepsilon^2y\) also puts \(f_\varepsilon=\varepsilon^2yr_\varepsilon\) in the actual closure domain.
The inverse derivative formula and normality give the displayed derivative limit \(e\otimes e\), where \(e\) is the spectral projection at \(\lambda\).
Since \(f_\varepsilon\to0\) in operator norm, closedness and faithfulness force \(e=0\).
This argument assumes no formula for \(\partial_i(X_i^*)\).

The second part of the lemma now establishes L2 liberation gradients on the full coordinate algebras, as checked in the [reorganization entry](#liberation-gradients-reorganization-20261028).
Proposition 5.3 supplies the liberation dual system, rationality criterion and maximal Delta after these two hypotheses have been obtained.
The nonatomicity argument itself uses neither maximal Delta nor the free-field embedding.
This is scoped authoring-agent self-review, not an independent review of the full construction or a new source audit.

<a id="normal-conjugate-proposition-20261018"></a>
## Corollary 5.7: Normal Conjugate Variables

Corollary 5.7 retains `prop:normal-conjugates` and the authorized corollary environment.
On 2026-10-28, the authoring agent checked its deduction from Lemma 5.6 and Proposition 5.3.
Normality, generation and admission of conjugate variables in the sense of Definition 5.4 remain explicit.
Lemma 5.6 supplies nonatomic spectral distributions and L2 liberation gradients, so Proposition 5.3 gives the every-fraction criterion, uniqueness for a fixed pair and maximal Delta.
All conclusions of Theorem 1.7 apply to any normalized liberation system for the tuple.
This makes no uniqueness claim for such a system and no existence claim for ordinary dual operators.
The use of this corollary in Theorem 1.9 is checked in the [current dual-system proof entry](#analytic-proof-via-liberation-20261018).
This is a scoped authoring-agent check of the presentation and direct deduction, not a new independent review of the inputs.

<a id="arcsine-liberation-counterexample-20261018"></a>
## Remark 5.8: Arcsine Example

The arcsine example added on 2026-10-18 is retained as Remark 5.8, with the same semantic label and complete monomial proof.
The fixed result and both its monomial and original Chebyshev arguments remain in [C_F0080](../../../claims/Yin_C_F0080_v1.md#argument).
Its selected assessment adopts [R_F0053](../../../audits/reviews/Yin_R_F0053_v1.md#whole-proof-finding), whose actual self-review relationship is retained.
The earlier separately assigned agent also inspected the manuscript remark without developing either proof; this does not enlarge the fixed review's recorded relationship or scope.

On 2026-10-28, the authoring agent checked the retained remark and the added connection to Proposition 5.3.
The multiplication model has a faithful normal trace and a nonatomic selfadjoint generator, so all scalar shifts are regular.
The bounded operator \(L=P_\Omega\) satisfies the full operator and adjoint-domain conditions and the manuscript's sum normalization.
For one coordinate relative to scalars, \(a\mapsto a\otimes1-1\otimes a\) is a well-defined derivation with zero product trace; hence its actual adjoint vector and liberation gradient are zero.
This verifies the general proposition's gradient hypothesis directly.
The monomial calculation still has product-trace derivative equal to one, with the displayed \(4^{-n}\) binomial convolution, while the L2 norms tend to zero.
The actual adjoint condition in Definition 5.4 would contradict that limit, so ordinary conjugate variables do not exist.
No new external theorem is used in the added observation.
This local presentation check is not a new independent proof review or a review of the whole manuscript.

<a id="circular-normality-remark"></a>
## Remark 7.1: Circular Counterexample

The authoring agent self-reviewed the abbreviated current presentation of Remark 7.1 against [C_F0074](../../../claims/Yin_C_F0074_v1.md#statement) and its fixed review [R_F0047](../../../audits/reviews/Yin_R_F0047_v1.md#conclusion), whose initial-context relationship is unknown.
The check retained the standard free semicircular pair, explicit bounded dual, zero fraction commutators for every pair and the inverse-closed-centralizer argument excluding the adjoint.
This was a local presentation check, not a new independent proof review.


<a id="psi-generalization-20261029"></a>
## Definition 1.3 and Lemma 4.3: Right Multiplication

The authoring agent self-checked the extension of Definition 1.3 from the tuple entries to an arbitrary element x of L0(M), with Psi_i defined as Psi_(X_i).
The opposite-factor multiplication gives v^op x^op=(xv)^op, so the two right multiplication maps in Lemma 4.3 produce exactly Psi_x.
The lemma still assumes x in M and regularity of every scalar shift.
These hypotheses ensure that both factor maps preserve H and have no nonzero finite-dimensional invariant subspace.
The two quotient maps are linear maps on vector-space quotients; no quotient-algebra structure or invariant-subspace assertion about the quotient maps is used.
In the first quotient step the unquotiented second factor gives injectivity, and in the second step the unquotiented first factor H gives injectivity.
The check retained all existing mathematical environments and semantic labels.
This is a manuscript self-review of notation and the unchanged proof mechanism, not a new fixed Claim or independent review.


<a id="scalar-injectivity-via-lemma32-20261029"></a>
## Lemma 4.3: Injectivity from Lemma 3.2

The authoring agent self-checked the revised injectivity argument under the unchanged regularity hypothesis of Lemma 4.3.
A finite-rank operator commuting with x has finite-dimensional x-invariant range; regularity of every scalar shift excludes every nonzero eigenvector and forces that range to vanish.
Remark 2.8 then gives maximal Delta for the one-element tuple, so Lemma 3.2 applies directly and proves injectivity of Psi_x.
The argument uses neither Proposition 4.4 nor any liberation dual system, so the later use of Lemma 4.3 in Proposition 4.4 creates no circular dependency.
The abstract difference-map observation and the two quotient steps are retained for the L2 assertion.
All existing environments, semantic labels, hypotheses and conclusions are preserved.
This is a scoped manuscript self-review, not a new independent review or fixed Claim assessment.


<a id="tensor-recovery-range"></a>
## Lemma 4.3: Range of the Restriction

A scoped agent check of the current Definition 1.3 and Lemma 4.3 excludes replacing the conclusion by bijectivity of Psi_x from the algebraic tensor product H tensor H onto itself.
Put $U:=L^0(\mathcal M)$, $V:=U\otimes_{\mathbb C}U^{\mathrm{op}}$ and $W:=H\otimes_{\mathbb C}H$.
The linear multiplication map $m:V\to U$, defined by $m(u\otimes v^{\mathrm{op}}):=uv$, satisfies $m\Psi_x(u\otimes v^{\mathrm{op}})=uxv-u(xv)=0$.
Since $m(1\otimes1)=1$, the tensor $1\otimes1\in W$ is outside $\Psi_x(V)$, so the restriction to W is not surjective onto W.
Under the lemma's hypotheses, its actual conclusions are injectivity on V and $\Psi_x^{-1}(W)=W$; the reverse inclusion in this equality uses $x\in\mathcal M$.
The statement now uses this compact form, and the proof explicitly records preservation of W and introduces the tensor k for the other inclusion.
Consequently, the restriction is a bijection $\Psi_x|_W:W\to\Psi_x(V)\cap W$, rather than a bijection onto W.
This check verifies only the range obstruction, the reformulation of the stated conclusions and the affected proof transitions; it is not an independent review of the lemma's proof.

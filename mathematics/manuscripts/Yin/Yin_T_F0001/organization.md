---
author: Yin
---

# F0001 Manuscript Organization

The current [paper](paper/main.tex) is authoritative for statements, notation, numbering and proofs.
This record summarizes the selected mathematical environments and their proof routes.
It does not select a new research objective or change Claim status.

## Document Order

The paper is compiled from `main.tex` and seven section files.

| Section | Current title | Mathematical content |
| --- | --- | --- |
| 1 | Introduction | Definitions 1.1-1.3, 1.6 and 1.8, Theorems 1.4, 1.7 and 1.9, the intervening remark and the statement of the paper's organization. |
| 2 | Preliminaries | Division closures, the abstract free field and coordinate separation; fractions of affiliated operators; tensor realizations of finite-rank operators; Delta and free-field realization. |
| 3 | Rationality under maximal Delta | Lemmas 3.1–3.3, the proof of Theorem 1.4 and the Hochschild interpretation in Remark 3.4. |
| 4 | Liberation dual system criterion | The normalization Lemma 4.1, finite-rank closure and individual tensor lemmas, Proposition 4.4, the L2 recovery Lemma 4.5 and the proof of Theorem 1.7. |
| 5 | Dual system criterion | Lemmas 5.1-5.5 on fraction domains, rank independence, identification of finite-rank solutions and module commutation; the direct normalized liberation construction in Lemma 5.6 and the proof of Theorem 1.9. |
| 6 | Applications to liberation gradients and conjugate variables | Subsection 6.1 introduces Definition 6.1, the liberation construction in Lemma 6.2 and the rationality criterion in Proposition 6.3. Subsection 6.2 contains Definition 6.4, Lemmas 6.5-6.6, the ordinary conjugate-variable Corollary 6.7 and the arcsine example in Remark 6.8. |
| 7 | Examples | The circular counterexample in Remark 7.1, comparing the maximal-Delta and dual-system criteria. |

## Preliminary Order

Section 2 proceeds from abstract algebra to affiliated fractions and Hilbert-space realizations, ending with maximal Delta.
All existing mathematical environments and their semantic labels are retained.

| Subsection | Current title | Contents and dependencies |
| --- | --- | --- |
| 2.1 | Division closures and the free field | Definition 2.1 gives division closure and rationality; the abstract free field and its difference quotients follow. The terminology is justified by the closure equality when Delta(X)=d, with a forward reference to Subsection 2.5. |
| 2.2 | Coordinate maps over division subrings | Lemma 2.2 gives the balanced-tensor equalizer for every u in U, using a right-linear coordinate map. This algebraic construction requires no maximal-Delta hypothesis. |
| 2.3 | Fractions of affiliated operators | Definition 2.3 introduces regularity before the canonical fraction construction. Definition 2.4 gives fraction and common-denominator terminology before Lemmas 2.5–2.6. The Linnell–Miyagawa comparison concludes the subsection. |
| 2.4 | Algebraic tensors and finite-rank operators | The finite-rank, right-multiplication and Hilbert–Schmidt notation precedes Theta, its unitary extension and its bimodule and commutator identities. The trace extension to H is retained. |
| 2.5 | The invariant Delta and free-field realization | Definition 2.7 defines the cycles and Delta, followed by the maximality characterization in Remark 2.8, the free-field realization in Lemma 2.9 and equality of rational and division closures under maximal Delta. |

The abstract free field is introduced before its evaluation in affiliated operators.
The Hilbert–Schmidt space is defined before the unitary extension of Theta, and maximal Delta is stated before its free-field and closure consequences.

## Main Theorems

| Environment | Hypotheses and conclusion | Proof route |
| --- | --- | --- |
| Theorem 1.4, `thm:delta` | For a bounded tuple with Delta(X)=d, rationality is equivalent to an affiliated tensor identity, the tensor identity for every fraction pair, bounded tensor witnesses for some fraction pair, and a finite-rank certificate for some fraction pair. The witnesses are unique for the specified data. | Section 3 proves the five-condition cycle using the free-field realization, difference quotients, denominator clearing, tensor injectivity, the Theta correspondence and the balanced-tensor equalizer. |
| Theorem 1.7, `thm:intrinsic-analytic` | For X in M^d with every scalar shift regular, fix a normalized liberation dual system. Rationality is equivalent to a finite-rank certificate for some fraction pair, to such certificates for every pair, and to closure Gamma[Q,L_i] lying in [rho(X_i),F(H)] for every pair and every i. The certificate tuple is unique for each fixed pair. | The cycle is (1) implies (4) implies (3) implies (2) implies (1). Proposition 4.4 gives maximal Delta. Theorem 1.4(3) and Lemma 4.5 give algebraic L2 tensors and closure Phi_i(h)=Theta(Psi_i(ell_i)); Lemma 5.1 identifies the full fraction-commutator closure, with T_i=-Theta(ell_i). Summing uses the normalization. Theorem 1.4 gives the converse and uniqueness. |
| Theorem 1.9, `thm:analytic` | For bounded normal generators and a dual system in the sense of Definition 1.8, rationality is equivalent to finite rank of every fraction commutator, equivalently bounded finite-rank closure on its full natural domain. Each coordinate rank is independent of the fraction pair. | Lemma 5.6 constructs a normalized liberation dual system directly from the ordinary duals and verifies regularity of scalar shifts. The implication (1) implies (3) uses Theorem 1.7(4), summation and Lemma 5.3 to identify the finite-rank solutions. The converse first uses Lemma 5.2 to pass to every fraction pair, then Lemma 5.6 and Theorem 1.7(4). Lemmas 5.1 and 4.2 give (2) equivalent to (3); Lemma 5.2 gives rank independence. |

Theorem 1.4 does not require normality or generation of M.
Its finite-rank condition asks for some fraction pair.
Theorem 1.7 applies to every prescribed fraction pair, and its witnesses may depend on that pair.
For the normalized liberation system constructed from a dual system in Lemma 5.6, the identity closure Gamma[Q,L_i]=[rho(X_i),closure Gamma[Q,D_i]] holds when the ordinary fraction commutator has bounded closure.
Normalization and Lemma 5.3 identify the finite-rank operators in Theorem 1.7(4) with these closures, explaining the relation to Theorem 1.9.
The introduction retains the open question about ordinary duals under the conjugate-variable condition for normal generators; it makes no reverse implication from liberation duals to ordinary conjugate variables or ordinary dual systems.

## Tensor and Liberation Results

Subsection 2.4, “Algebraic tensors and finite-rank operators”, uses CS05 equations (1.1)–(1.2) for Theta and its four tensor-factor actions.
It gives the linear bijection from algebraic L2 tensors to bounded finite-rank operators, its Hilbert–Schmidt extension, the bounded-factor specialization and the commutator identity.
It also fixes the extension \(\tau(\xi)=\langle\Omega,\xi\rangle\) for \(\xi\in H\), used in the liberation-gradient construction.
Lemma 2.2 is the balanced-tensor equalizer used by Theorem 1.4.

Lemmas 3.1–3.3 respectively clear a finite family of affiliated tensors, prove tensor injectivity under maximal Delta, and convert algebraic L2 tensor certificates into finite-rank operator certificates with the sign T_i=-Theta(ell_i).

| Environment | Statement or construction | Proof route |
| --- | --- | --- |
| Definition 1.6, `def:liberation-dual-system` | For an arbitrary tuple X in M^d, operators L_i with M Omega contained in Dom L_i and Dom L_i*, and [X_j,L_i]=delta_ij[X_i,P_Omega] on M Omega. | This is the manuscript's domain variant of Voi99 Definition 13.1. The definition additionally calls a system normalized when its sum equals P_Omega on M Omega; Lemma 4.1 constructs such a system without extra hypotheses on X. This sum convention is local. |
| Lemma 4.1, `lem:liberation-normalization` | Every X in M^d admitting a liberation dual system admits a normalized one. | The proof sets C=sum_k L_k-P_Omega and subtracts C/d from each L_i on M Omega. Since C commutes with each X_j, the corrected operators retain the liberation relations and sum to P_Omega; an explicit inner-product identity verifies their common adjoint domain. No normality, regularity or generation hypothesis is used. |
| Lemma 4.2, `lem:finite-closure` | A densely defined closable finite-rank operator has a bounded finite-rank closure with the same range and rank. | The statement is cited to Kat95 Problem III.5.18. |
| Lemma 4.3, `lem:tensor-l2-recovery` | If every x-lambda is regular, the map Psi_x from Definition 1.3 is injective; an algebraic L2 image has an algebraic L2 preimage. | The finite-rank commutant of x vanishes, so maximal Delta for the one-element tuple and Lemma 3.2 give injectivity. Passing to the quotient by H in each tensor factor gives recovery. |
| Proposition 4.4, `prop:liberation-delta` | Tuples X in M^d with X_i-lambda regular for every i and every complex lambda and with a liberation dual system satisfy Delta(X)=d. | Clear a finite-rank cycle's tensor factors, apply Phi_i(c tensor d^op)=cL_i d on M Omega, use individual injectivity and cancel the denominators. |
| Lemma 4.5, `lem:tensor-images-l2` | Under the same hypotheses, a bounded algebraic total image h=sum_i Psi_i(k_i) forces each k_i into H tensor_alg H and gives closure Phi_i(h)=Theta(Psi_i(k_i)). | Phi_i(h) is closable by the adjoint-domain condition. The cleared identity makes its restriction to t M Omega finite rank, so Lemma 4.2 gives a bounded finite-rank closure. Theta, regular cancellation and Lemma 4.3 recover the tensors. |

Proposition 4.4 is proved separately from Lemma 4.5.
Its proof uses the liberation commutator relations and regularity of every scalar shift; the recovery lemma uses the adjoint-domain condition to obtain closability.
The density needed in these proofs is that of M Omega and t M Omega in H.
Proposition 4.4, Lemma 4.5 and Theorem 1.7 require neither normality nor generation of M by X.
The proof of Theorem 1.7 follows Lemma 4.5 in Section 4.
Its new assertion (4) uses a normalized system; normalization is always available and hence does not restrict the admissible tuples X.
The reference to Lemma 5.1 uses only its common-domain hypotheses and has no dependence on Theorem 1.7.

## Ordinary Duals, Liberation Gradients and Conjugate Variables

Definition 1.8, `def:dual-system`, precedes Theorem 1.9 and states the common domain and adjoint-domain inclusion and the generator-first relations on M Omega.
Theorem 1.9 and Lemmas 5.3 and 5.6 use this definition; normality and generation remain separate hypotheses wherever needed.
Lemma 5.1 supplies closability on the natural fraction-commutator domain.
Lemma 5.2, `lem:fraction-ranks`, uses common denominators and the finite-rank closure lemma to propagate finite rank from one fraction pair to every pair and prove equality of the ranks.
Lemma 5.3, `lem:finite-rank-identification`, clears the tensor factors of a finite-rank solution and applies the ordinary dual relation on M Omega to identify its coordinates with the actual fraction-commutator closures.
These fraction lemmas require no normality or generation of M.
The generic domain assumptions in Lemmas 5.1 and 5.2 remain sufficient, so Lemma 5.1 can also be used with liberation dual operators in Section 4.
Lemma 5.4, `lem:normal-intertwining`, gives the bounded-map adjoint intertwining from CS77; the classical Fuglede statement precedes it.
Lemma 5.5 uses that lemma, the closed graph theorem and Kaplansky density for closable module commutation.
Lemma 5.6, `lem:fundamental`, sets K_i=[rho(X_i),D_i restricted to M Omega], C=sum_i K_i-P_Omega and L_i=K_i-C/d.
It checks the common adjoint domain, normalized liberation relations and regularity of scalar shifts.
Lemma 5.5 makes C left M-linear, so Gamma[Q,C] vanishes on M Omega.
This gives closure Gamma[Q,L_i]=[rho(X_i),closure Gamma[Q,D_i]] whenever the latter ordinary fraction commutator has bounded closure, and retains the fundamental summed identity.
The proof of Theorem 1.9 uses Theorem 1.7(4) in both directions and needs no result from Section 6.

Section 6 first treats liberation gradients and then derives the ordinary conjugate-variable case.
Definition 6.1, `def:liberation-gradients`, uses the represented derivations on each full algebra \(\mathcal P_i=\operatorname{Alg}(W^*(X_i),W^*(X_j:j\ne i))\).
It explicitly requires well-definedness and the actual Hilbert-adjoint condition, with \(j_i=-\gamma_i^*(1\otimes1)\).
Lemma 6.2, `lem:gradient-liberation`, uses \(\delta_i=\mathrm i\gamma_i\) and proves the energy estimate with its nonzero coassociativity defect.
Analytic polynomial approximation of unitaries and closedness of \(\overline{\delta_i}\) give an operator-norm-to-L2 bound for the contraction.
The core adjoint formula supplies the corresponding adjoint bound.
Kaplansky approximation and weakly closed graphs put \(\mathcal M\Omega\) in both domains of the actual closure \(C_i=\overline{C_i^\circ}\).
Graph-core approximation extends the generator relation, and \(L_i=\mathrm i C_i\) is a liberation dual system.
Lemma 4.1 supplies normalization.
Proposition 6.3, `prop:liberation-gradients`, assumes normal generators with nonatomic spectral distributions in addition to \(L^2\) liberation gradients.
Nonatomicity makes every scalar shift regular, so Theorem 1.7 gives the rationality criterion for every fraction pair, uniqueness for each fixed pair and all its conclusions for any normalized system.
Proposition 4.4 gives maximal Delta.

Definition 6.4, `def:conjugate-variables`, retains the starred polynomial derivations, prescribed generator values and actual adjoint-domain inclusion.
The normal-adjoint kernel and Lemma 6.5, `lem:normal-adjoint-uniqueness`, retain their proof and identify the adjoint-generator derivatives.
Lemma 6.6, `lem:conjugate-liberation`, assumes normal generators admitting conjugate variables in the sense of Definition 6.4.
It proves nonatomicity directly from closability of the conjugate derivations, using the retained Neumann-series domain check and a spectral limit in the graph of each closed derivation.
It does not use maximal Delta or the free-field embedding.
The polynomial derivation \(\gamma_i^\circ=\Psi_i\partial_i\) has the actual adjoint vector \([X_i^*,\xi_i]\), giving \(j_i=[\xi_i,X_i^*]\).
Voiculescu's word-moment formula and bounded Kaplansky approximation extend this identity to the coordinate von Neumann algebras.
Testing formal relations against products \(urv\) proves that the derivation descends to \(\mathcal P_i\), where the L2 moment identity establishes the actual adjoint condition.
Thus Proposition 6.3 applies.
Corollary 6.7 retains the label `prop:normal-conjugates` and obtains all conclusions of Proposition 6.3, including the every-fraction criterion and maximal Delta, from Lemma 6.6.
This authorized environment change does not change the three-main-theorem structure.

Remark 6.8, `rem:liberation-without-conjugates`, retains the arcsine example and its monomial obstruction.
The arcsine coordinate has nonatomic law, regular scalar shifts and the normalized liberation dual \(L=P_\Omega\).
Its liberation gradient relative to scalars is zero, so it satisfies Proposition 6.3.
The monomials \(X^{2n+1}\) tend to zero in L2 and have divided-difference product trace equal to one, contradicting the actual adjoint condition in Definition 6.4.

Section 7, Examples, retains the circular counterexample in Remark 7.1.
The example applies MSY23 Proposition 6.2 directly to its bounded dual for maximal Delta and compares Theorems 1.4 and 1.9.
The bounded-dual specialization is described directly in the introduction through Theorem 1.9.

The project README maps these environments to responsible mathematical records.
The project review distinguishes manuscript-local checks from fixed proof and source reviews.

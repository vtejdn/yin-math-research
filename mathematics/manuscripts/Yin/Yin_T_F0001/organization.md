---
author: Yin
---

# F0001 Manuscript Organization

The current [paper](paper/main.tex) is authoritative for statements, notation, numbering and proofs.
This record summarizes the selected mathematical environments and their proof routes.
It does not select a new research objective or change Claim status.

## Document Order

The paper is compiled from `main.tex` and six section files.

| Section | Current title | Mathematical content |
| --- | --- | --- |
| 1 | Introduction | Definitions 1.1-1.3, 1.6 and 1.8, Theorems 1.4, 1.7 and 1.9, the intervening remark and the statement of the paper's organization. |
| 2 | Preliminaries | Division closures, the abstract free field and coordinate separation; fractions of affiliated operators; tensor realizations of finite-rank operators; Delta and free-field realization. |
| 3 | Rationality under maximal Delta | Lemmas 3.1–3.3, the proof of Theorem 1.4 and the Hochschild interpretation in Remark 3.4. |
| 4 | Liberation dual system criterion | An unnumbered recall of Definition 1.6 and the two tensor-evaluation identities precede the normalization Lemma 4.1, finite-rank closure and individual tensor lemmas, Lemma 4.4 on quotient maps and tensor products, Proposition 4.6, the L2 recovery Lemma 4.7, the proof of Theorem 1.7 and the short liberation-gradient remark, Remark 4.8. |
| 5 | Dual system criterion | Lemmas 5.1-5.5 on fraction domains, rank independence, identification of finite-rank solutions and module commutation; Lemma 5.6 gives the normalized liberation construction and summed identity. Theorem 1.9 follows directly from Theorem 1.7. |
| 6 | Examples | The arcsine example in Remark 6.1 distinguishes the two analytic hypotheses; the circular counterexample in Remark 6.2 shows why normality is needed for the ordinary dual-system criterion. |

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
| Theorem 1.7, `thm:intrinsic-analytic` | For X in M^d with every scalar shift regular, fix a normalized liberation dual system. Rationality is equivalent to a finite-rank certificate for some fraction pair, to such certificates for every pair, and to closure Gamma[Q,L_i] lying in [rho(X_i),F(H)] for every pair and every i. The certificate tuple is unique for each fixed pair. | The cycle is (1) implies (4) implies (3) implies (2) implies (1). Proposition 4.6 gives maximal Delta. Theorem 1.4(3) and Lemma 4.7 give algebraic L2 tensors and closure m_{L_i}(ell_0)=Theta(Psi_i(ell_i)); Lemma 5.1 identifies the full fraction-commutator closure, with T_i=-Theta(ell_i). Summing uses the normalization. Theorem 1.4 gives the converse and uniqueness. |
| Theorem 1.9, `thm:analytic` | For bounded normal generators and a dual system in the sense of Definition 1.8, rationality is equivalent to finite rank of every fraction commutator, equivalently bounded finite-rank closure on its full natural domain. Each coordinate rank is independent of the fraction pair. | Lemma 5.6 supplies a normalized liberation dual system and scalar-shift regularity. Theorem 1.7 gives finite-rank certificates for each prescribed fraction pair; Lemma 5.3 identifies them with the ordinary fraction-commutator closures. Conversely, the summed identity of Lemma 5.6 supplies a certificate, so Theorem 1.7 gives rationality. Lemmas 5.1 and 4.2 give (2) equivalent to (3); Lemma 5.2 gives rank independence. |

Theorem 1.4 does not require normality or generation of M.
Its finite-rank condition asks for some fraction pair.
Theorem 1.7 applies to every prescribed fraction pair, and its witnesses may depend on that pair.
For the normalized liberation system constructed from a dual system in Lemma 5.6, the identity closure Gamma[Q,L_i]=[rho(X_i),closure Gamma[Q,D_i]] holds when the ordinary fraction commutator has bounded closure.
The resulting summed identity verifies the certificate required by Theorem 1.7, while Lemma 5.3 identifies the certificate coordinates with the ordinary fraction-commutator closures.
The arcsine example shows that the liberation criterion has strictly weaker hypotheses than the ordinary dual-system criterion.

## Tensor and Liberation Results

Subsection 2.4, “Algebraic tensors and finite-rank operators”, uses CS05 equations (1.1)–(1.2) for Theta and its four tensor-factor actions.
It gives the linear bijection from algebraic L2 tensors to bounded finite-rank operators, its Hilbert–Schmidt extension, the bounded-factor specialization and the commutator identity.
It also fixes the extension \(\tau(\xi)=\langle\Omega,\xi\rangle\) for \(\xi\in H\).
Lemma 2.2 is the balanced-tensor equalizer used by Theorem 1.4.

Lemmas 3.1–3.3 respectively clear a finite family of affiliated tensors, prove tensor injectivity under maximal Delta, and convert algebraic L2 tensor certificates into finite-rank operator certificates with the sign T_i=-Theta(ell_i).

| Environment | Statement or construction | Proof route |
| --- | --- | --- |
| Definition 1.6, `def:liberation-dual-system` | For an arbitrary tuple X in M^d, operators L_i with M Omega contained in Dom L_i and Dom L_i*, and [X_j,L_i]=delta_ij[X_i,P_Omega] on M Omega. | This is the manuscript's domain variant of Voi99 Definition 13.1. The definition additionally calls a system normalized when its sum equals P_Omega on M Omega; Lemma 4.1 constructs such a system without extra hypotheses on X. This sum convention is local. |
| Lemma 4.1, `lem:liberation-normalization` | Every X in M^d admitting a liberation dual system admits a normalized one. | The proof sets C=sum_k L_k-P_Omega and subtracts C/d from each L_i on M Omega. Since C commutes with each X_j, the corrected operators retain the liberation relations and sum to P_Omega; an explicit inner-product identity verifies \(\mathcal M\Omega\subseteq\operatorname{Dom}\widetilde L_i^*\) for every \(i\). No normality, regularity or generation hypothesis is used. |
| Lemma 4.2, `lem:finite-closure` | A densely defined closable finite-rank operator has a bounded finite-rank closure with the same range and rank. | The statement is cited to Kat95 Problem III.5.18. |
| Lemma 4.3, `lem:tensor-difference-injectivity` | For linear maps A on V and B on W, A tensor I minus I tensor B is injective on the algebraic tensor product if either map has no nonzero finite-dimensional invariant subspace. | A minimal tensor decomposition of a nonzero kernel vector would give a finite-dimensional invariant subspace; interchange the factors for the symmetric case. |
| Lemma 4.4, `lem:tensor-quotient-kernels` | For a subspace E of a complex vector space V and the quotient map pi, the natural maps in both tensor orders are injective, and ker(pi tensor I)=E tensor W and ker(I tensor pi)=W tensor E. | Choose a complement V_1 with \(V=E\oplus V_1\), distribute the tensor product over this direct sum and use that pi restricts to an isomorphism on V_1. Interchange the tensor factors for the second equality. |
| Lemma 4.5, `lem:tensor-l2-recovery` | If every x-lambda is regular, the map Psi_x from Definition 1.3 is injective; an algebraic L2 image has an algebraic L2 preimage. | Regularity of every x-lambda excludes nonzero finite-dimensional invariant subspaces for both factor multiplication maps, so Lemma 4.3 gives injectivity of Psi_x. For each tensor factor, passing to the quotient by H, applying Lemma 4.3 and identifying the kernel by Lemma 4.4 gives recovery. |
| Proposition 4.6, `prop:liberation-delta` | Tuples X in M^d with X_i-lambda regular for every i and every complex lambda and with a liberation dual system satisfy Delta(X)=d. | Clear a finite-rank cycle's tensor factors and use m_{L_i}(Psi_j(ell))=delta_ij Theta(Psi_i(ell)) to separate the i-th term on M Omega. Boundedness and density, individual injectivity and cancellation of the denominators give the conclusion. |
| Lemma 4.7, `lem:tensor-images-l2` | Under the same hypotheses, a bounded algebraic total image ell_0=sum_i Psi_i(k_i) forces each k_i into H tensor_alg H and gives closure m_{L_i}(ell_0)=Theta(Psi_i(k_i)). | The inclusion \(\mathcal M\Omega\subseteq\operatorname{Dom}L_i^*\) gives \(\mathcal M\Omega\subseteq\operatorname{Dom}T_i^*\) for \(T_i=m_{L_i}(\ell_0)\), so \(T_i\) is closable. The two separately numbered formulas for m_{L_i} move the outside factors inside m_{L_i} and separate the i-th term, giving sT_i t=Theta(Psi_i(ell_i)). This makes the restriction to t M Omega finite rank, so Lemma 4.2 gives a bounded finite-rank closure. Theta, regular cancellation and Lemma 4.5 recover the tensors. |

Proposition 4.6 is proved separately from Lemma 4.7.
Its proof uses the liberation commutator relations and regularity of every scalar shift; the recovery lemma uses \(\mathcal M\Omega\subseteq\operatorname{Dom}L_i^*\) to obtain closability.
The density needed in these proofs is that of M Omega and t M Omega in H.
Proposition 4.6, Lemma 4.7 and Theorem 1.7 require neither normality nor generation of M by X.
The proof of Theorem 1.7 follows Lemma 4.7 in Section 4.
Its new assertion (4) uses a normalized system; normalization is always available and hence does not restrict the admissible tuples X.
The application of Lemma 5.1 uses \(\mathcal M\Omega\subseteq\operatorname{Dom}L_i\cap\operatorname{Dom}L_i^*\), and the proof of Lemma 5.1 does not use Theorem 1.7.

## Ordinary Duals and Liberation Gradients

Definition 1.8, `def:dual-system`, precedes Theorem 1.9 and states \(\mathcal M\Omega\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*\) and the generator-first relations on M Omega.
Theorem 1.9 and Lemmas 5.3 and 5.6 use this definition; normality and generation remain separate hypotheses wherever needed.
Lemma 5.1 supplies closability on the natural fraction-commutator domain.
Lemma 5.2, `lem:fraction-ranks`, uses common denominators and the finite-rank closure lemma to propagate finite rank from one fraction pair to every pair and prove equality of the ranks.
Lemma 5.3, `lem:finite-rank-identification`, clears the tensor factors of a finite-rank solution and applies the ordinary dual relation on M Omega to identify its coordinates with the actual fraction-commutator closures.
These fraction lemmas require no normality or generation of M.
For each operator \(D\), Lemmas 5.1 and 5.2 require \(\mathcal M\Omega\subseteq\operatorname{Dom}D\cap\operatorname{Dom}D^*\).
They require no ordinary dual commutator relations, so Lemma 5.1 also applies to the liberation dual operators in Section 4.
Lemma 5.4, `lem:normal-intertwining`, gives the bounded-map adjoint intertwining from CS77; the classical Fuglede statement precedes it.
Lemma 5.5 uses that lemma, the closed graph theorem and Kaplansky density for closable module commutation.
Lemma 5.6, `lem:fundamental`, sets K_i=[rho(X_i),D_i restricted to M Omega], C=sum_i K_i-P_Omega and L_i=K_i-C/d.
It proves \(\mathcal M\Omega\subseteq\operatorname{Dom}K_i^*\cap\operatorname{Dom}C^*\cap\operatorname{Dom}L_i^*\) for every \(i\), verifies the normalized liberation relations and proves regularity of every scalar shift.
Lemma 5.5 makes C left M-linear, so Gamma[Q,C] vanishes on M Omega.
This gives closure Gamma[Q,L_i]=[rho(X_i),closure Gamma[Q,D_i]] whenever the latter ordinary fraction commutator has bounded closure, and retains the fundamental summed identity.
The proof of Theorem 1.9 uses Theorem 1.7 in both directions.
Its converse needs only the specified fraction pair; propagation between pairs is retained for rank independence.

Remark 4.8, `rem:liberation-gradients`, closes Section 4.
For the coordinate algebras A_i and the algebras B_i generated by the other coordinates, it states that L2 liberation gradients give a normalized liberation dual system in the sense of Definition 1.6.
The definition is cited to Voi99 Sections 5.3--5.4; the construction and estimates remain in C_F0082 and are not developed in the manuscript.
Normality and nonatomic spectral distributions supply the regularity hypothesis when applying Theorem 1.7.

Section 6, Examples, begins with the arcsine example in Remark 6.1, `rem:liberation-without-duals`.
The arcsine coordinate has nonatomic law, regular scalar shifts and the normalized liberation dual \(L=P_\Omega\).
Its liberation gradient relative to scalars is zero.
The odd monomials tend to zero in L2, whereas the vacuum pairing of their ordinary dual commutators would equal one.
The two vacuum domain inclusions bound that pairing by a fixed constant times the L2 norm, excluding every ordinary dual system.

Remark 6.2 retains the circular counterexample.
The example applies MSY23 Proposition 6.2 directly to its bounded dual for maximal Delta and compares Theorems 1.4 and 1.9.
The bounded-dual specialization is described directly in the introduction through Theorem 1.9.

The project README maps these environments to responsible mathematical records.
The project review distinguishes manuscript-local checks from fixed proof and source reviews.

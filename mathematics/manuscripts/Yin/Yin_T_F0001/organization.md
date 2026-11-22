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
| 4 | Liberation dual system criterion | An unnumbered recall of Definition 1.6 is followed by Remark 4.1 on liberation gradients and the two tensor-evaluation identities. Proposition 4.2 normalizes the system, and Lemmas 4.3 through 4.6 give closure and tensor tools. The proof of Theorem 1.7 follows Proposition 4.7 and Lemmas 4.8 and 4.9 on algebraic L2 recovery and closability of fraction commutators. |
| 5 | Dual system criterion | An unnumbered recall of Definition 1.8 is followed by Remark 5.1 on maximal Delta. Lemmas 5.2 through 5.5 establish rank independence, identify finite-rank solutions and give the required module commutation. Proposition 5.6 constructs the normalized liberation dual system. Lemma 5.7 compares fraction commutators and gives the summed identity. Theorem 1.9 uses maximal Delta to obtain scalar-shift regularity before applying Theorem 1.7. |
| 6 | Examples | Example 6.1 separates maximal Delta from liberation duals, Example 6.2 distinguishes the two analytic hypotheses, Example 6.3 shows why normality is needed, and Example 6.4 separates the division closures on bounded elements. |

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
| Theorem 1.7, `thm:intrinsic-analytic` | For X in M^d with every scalar shift regular, fix a normalized liberation dual system. Rationality is equivalent to a finite-rank certificate for some fraction pair, to such certificates for every pair, and to closure Gamma[Q,L_i] lying in [rho(X_i),F(H)] for every pair and every i. The certificate tuple is unique for each fixed pair. | The cycle is (1) implies (4) implies (3) implies (2) implies (1). Proposition 4.7 gives maximal Delta. Theorem 1.4(3) and Lemma 4.8 give algebraic L2 tensors and closure m_{L_i}(ell_0)=Theta(Psi_i(ell_i)). Lemma 4.9 gives closability of Gamma[Q,L_i], whose closure equals the bounded closure of its restriction to M Omega. Take T_i=-Theta(ell_i). Summing uses the normalization. Theorem 1.4 gives the converse and uniqueness. |
| Theorem 1.9, `thm:analytic` | For a tuple of normal operators with a dual system on \(L^2(W^*(X),\tau)\), membership in \(\operatorname{Div}_{L^0(W^*(X))}\mathcal A_X\) is equivalent to finite rank of every fraction commutator, equivalently bounded finite-rank closure on its full natural domain. Each coordinate rank is independent of the fraction pair. | The proof sets \(\mathcal M=W^*(X)\). Remark 5.1 gives maximal Delta, and the free-field embedding gives scalar-shift regularity. Proposition 5.6 supplies a normalized liberation dual system. Theorem 1.7 gives finite-rank certificates for each prescribed fraction pair, and Lemma 5.3 identifies them with the ordinary fraction-commutator closures. Conversely, the summed identity of Lemma 5.7 supplies a certificate, so Theorem 1.7 gives rationality. Lemmas 4.9 and 4.3 give the equivalence of (2) and (3). Lemma 5.2 gives rank independence. |

Theorem 1.4 does not require normality or generation of M.
Its finite-rank condition asks for some fraction pair.
Theorem 1.7 applies to every prescribed fraction pair, and its witnesses may depend on that pair.
Lemma 5.7 compares the fraction commutators for a dual system and any normalized liberation dual system for the same tuple.
For normal generators, it identifies \(\overline{\Gamma[Q,L_i]}\) with \([\rho(X_i),\overline{\Gamma[Q,D_i]}]\) on \(\mathcal M\Omega\).
For finite-rank ordinary closures, the summed identity extends by density to the certificate identity on \(H\) required by Theorem 1.7.
Lemma 5.3 identifies the certificate coordinates with the ordinary fraction-commutator closures.
The arcsine example shows that the liberation criterion has strictly weaker hypotheses than the ordinary dual-system criterion.

## Tensor and Liberation Results

Subsection 2.4, “Algebraic tensors and finite-rank operators”, uses CS05 equations (1.1)–(1.2) for Theta and its four tensor-factor actions.
It gives the linear bijection from algebraic L2 tensors to bounded finite-rank operators, its Hilbert–Schmidt extension, the bounded-factor specialization and the commutator identity.
It also fixes the extension \(\tau(\xi)=\langle\Omega,\xi\rangle\) for \(\xi\in H\).
Lemma 2.2 is the balanced-tensor equalizer used by Theorem 1.4.

Lemmas 3.1–3.3 respectively clear a finite family of affiliated tensors, prove tensor injectivity under maximal Delta, and convert algebraic L2 tensor certificates into finite-rank operator certificates with the sign T_i=-Theta(ell_i).

| Environment | Statement or construction | Proof route |
| --- | --- | --- |
| Definition 1.6, `def:liberation-dual-system` | For an arbitrary tuple X in M^d, operators L_i with M Omega contained in Dom L_i and Dom L_i*, and [X_j,L_i]=delta_ij[X_i,P_Omega] on M Omega. | This is the manuscript's domain variant of Voi99 Definition 13.1. The definition additionally calls a system normalized when its sum equals P_Omega on M Omega; Proposition 4.2 constructs such a system without extra hypotheses on X. This sum convention is local. |
| Proposition 4.2, `prop:liberation-normalization` | Every X in M^d admitting a liberation dual system admits a normalized one. | The proof sets C=sum_k L_k-P_Omega and subtracts C/d from each L_i on M Omega. Since C commutes with each X_j, the corrected operators retain the liberation relations and sum to P_Omega; an explicit inner-product identity verifies \(\mathcal M\Omega\subseteq\operatorname{Dom}\widetilde L_i^*\) for every \(i\). No normality, regularity or generation hypothesis is used. |
| Lemma 4.3, `lem:finite-closure` | A densely defined closable finite-rank operator has a bounded finite-rank closure with the same range and rank. | The statement is cited to Kat95 Problem III.5.18. |
| Lemma 4.4, `lem:tensor-difference-injectivity` | For linear maps A on V and B on W, A tensor I minus I tensor B is injective on the algebraic tensor product if either map has no nonzero finite-dimensional invariant subspace. | A minimal tensor decomposition of a nonzero kernel vector would give a finite-dimensional invariant subspace; interchange the factors for the symmetric case. |
| Lemma 4.5, `lem:tensor-quotient-kernels` | For a subspace E of a complex vector space V and the quotient map pi, the natural maps in both tensor orders are injective, and ker(pi tensor I)=E tensor W and ker(I tensor pi)=W tensor E. | Choose a complement V_1 with \(V=E\oplus V_1\), distribute the tensor product over this direct sum and use that pi restricts to an isomorphism on V_1. Interchange the tensor factors for the second equality. |
| Lemma 4.6, `lem:tensor-l2-recovery` | If every x-lambda is regular, the map Psi_x from Definition 1.3 is injective; an algebraic L2 image has an algebraic L2 preimage. | Regularity of every x-lambda excludes nonzero finite-dimensional invariant subspaces for both factor multiplication maps, so Lemma 4.4 gives injectivity of Psi_x. For each tensor factor, passing to the quotient by H, applying Lemma 4.4 and identifying the kernel by Lemma 4.5 gives recovery. |
| Proposition 4.7, `prop:liberation-delta` | Tuples X in M^d with X_i-lambda regular for every i and every complex lambda and with a liberation dual system satisfy Delta(X)=d. | Clear a finite-rank cycle's tensor factors and use m_{L_i}(Psi_j(ell))=delta_ij Theta(Psi_i(ell)) to separate the i-th term on M Omega. Boundedness and density, individual injectivity and cancellation of the denominators give the conclusion. |
| Lemma 4.8, `lem:tensor-images-l2` | Under the same hypotheses, a bounded algebraic total image ell_0=sum_i Psi_i(k_i) forces each k_i into H tensor_alg H and gives closure m_{L_i}(ell_0)=Theta(Psi_i(k_i)). | The inclusion \(\mathcal M\Omega\subseteq\operatorname{Dom}L_i^*\) gives \(\mathcal M\Omega\subseteq\operatorname{Dom}T_i^*\) for \(T_i=m_{L_i}(\ell_0)\), so \(T_i\) is closable. The two separately numbered formulas for m_{L_i} move the outside factors inside m_{L_i} and separate the i-th term, giving sT_i t=Theta(Psi_i(ell_i)). This makes the restriction to t M Omega finite rank, so Lemma 4.3 gives a bounded finite-rank closure. Theta, regular cancellation and Lemma 4.6 recover the tensors. |
| Lemma 4.9, `lem:fraction-domains` | If \(\mathcal M\Omega\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*\), then \(\Gamma[Q,D_i]\) is densely defined and closable for every fraction pair \(Q\). | The factors \(b,t\) preserve \(\mathcal M\Omega\), so the domain contains \(\mathcal M\Omega\). Since \(s^*,a^*\) also preserve \(\mathcal M\Omega\), equation (22) gives \(\mathcal M\Omega\subseteq\operatorname{Dom}\bigl((\Gamma[Q,D_i])^*\bigr)\). |

Proposition 4.7 is proved separately from Lemma 4.8.
Its proof uses the liberation commutator relations and regularity of every scalar shift; the recovery lemma uses \(\mathcal M\Omega\subseteq\operatorname{Dom}L_i^*\) to obtain closability.
The density needed in these proofs is that of M Omega and t M Omega in H.
Proposition 4.7, Lemma 4.8 and Theorem 1.7 require neither normality nor generation of M by X.
The proof of Theorem 1.7 follows Lemma 4.9 in Section 4.
Its new assertion (4) uses a normalized system; normalization is always available and hence does not restrict the admissible tuples X.
The proof applies Lemma 4.9 with \(D_i=L_i\) using \(\mathcal M\Omega\subseteq\operatorname{Dom}L_i\cap\operatorname{Dom}L_i^*\).

## Ordinary Duals and Liberation Gradients

Definition 1.8, `def:dual-system`, precedes Theorem 1.9 and states \(\mathcal M\Omega\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*\) and the generator-first relations on M Omega.
Section 5 recalls Definition 1.8 in unnumbered form after its opening paragraph.
Remark 5.1, `rem:dual-maximality`, derives maximal Delta from this dual system by clearing the ranges of finite-rank cycles into \(\mathcal M\Omega\) before applying the MSY23 trace argument.
Theorem 1.9, Lemma 5.3, Proposition 5.6 and Lemma 5.7 use this definition.
Their statements specify normality and generation where needed.
Lemma 5.2, `lem:fraction-ranks`, uses common denominators and the finite-rank closure lemma to propagate finite rank from one fraction pair to every pair and prove equality of the ranks.
Lemma 5.3, `lem:finite-rank-identification`, clears the tensor factors of a finite-rank solution and applies \(m_{D_i}\) to the resulting tensor equality.
The ordinary dual relation on \(\mathcal M\Omega\) selects the \(i\)-th term.
Agreement on a dense subspace and closability give \(\overline{\Gamma[Q,D_i]}=T_i\).
These fraction lemmas require no normality or generation of M.
Lemmas 4.9 and 5.2 apply whenever \(\mathcal M\Omega\subseteq\operatorname{Dom}D\cap\operatorname{Dom}D^*\).
Lemma 5.4, `lem:normal-intertwining`, gives the bounded-map adjoint intertwining from CS77.
The classical Fuglede statement precedes it.
Lemma 5.5 uses that lemma, the closed graph theorem and Kaplansky density for closable module commutation.
Proposition 5.6, `prop:dual-liberation-construction`, sets K_i=[rho(X_i),D_i restricted to M Omega], C=sum_i K_i-P_Omega and L_i=K_i-C/d for any tuple admitting a dual system.
It proves \(\mathcal M\Omega\subseteq\operatorname{Dom}K_i^*\cap\operatorname{Dom}C^*\cap\operatorname{Dom}L_i^*\) for every \(i\), verifies the normalized liberation relations, and shows that \(C\) commutes with each \(X_j\) on \(\mathcal M\Omega\).
Lemma 5.7, `lem:fundamental`, assumes that the \(X_j\) are normal and generate \(\mathcal M\).
For each \(i\), the difference \(C_i=K_i-L_i\) is closable and commutes with every \(X_j\) on \(\mathcal M\Omega\).
Lemma 5.5 makes each \(C_i\) left \(\mathcal M\)-linear, so \(\Gamma[Q,C_i]\) vanishes on \(\mathcal M\Omega\).
This gives the coordinate identity on \(\mathcal M\Omega\), and normalization gives the summed identity there.
The proof of Theorem 1.9 starts with maximal Delta from Remark 5.1.
Maximal Delta then supplies the free-field embedding, so the nonzero free-field element \(x_i-\lambda\) evaluates to a regular element of \(\mathcal M\).
The proof uses Theorem 1.7 in both directions.
Its converse needs only the specified fraction pair; propagation between pairs is retained for rank independence.

Remark 4.1, `rem:liberation-gradients`, follows the recalled definition at the start of Section 4.
For the coordinate algebras A_i and the algebras B_i generated by the other coordinates, it states that L2 liberation gradients give a normalized liberation dual system in the sense of Definition 1.6.
The definition is cited to Voi99 Sections 5.3--5.4; the construction and estimates remain in C_F0082 and are not developed in the manuscript.
Normality and nonatomic spectral distributions supply the regularity hypothesis when applying Theorem 1.7.

Example 6.1 starts with a direct sum of a free semicircular pair and its translate.
The full linear matrix criterion gives maximal Delta, and a common spectral projection contradicts the two liberation commutator requirements.

Example 6.2 gives the arcsine construction, `ex:liberation-without-duals`.
The arcsine coordinate has nonatomic law, regular scalar shifts and the normalized liberation dual \(L=P_\Omega\).
Its liberation gradient relative to scalars is zero.
The odd monomials tend to zero in L2, whereas the vacuum pairing of their ordinary dual commutators would equal one.
The two vacuum domain inclusions bound that pairing by a fixed constant times the L2 norm, excluding every ordinary dual system.

Example 6.3 gives the circular counterexample.
The bounded dual gives maximal Delta by MSY23 Proposition 6.2, and the free-field embedding gives regular scalar shifts.
With \(L=P_\Omega\), the example applies Theorem 1.7 and compares its commutator condition with the finite-rank condition in Theorem 1.9.
The bounded-dual specialization is described directly in the introduction through Theorem 1.9.

Example 6.4, `ex:bounded-division-closure`, uses the selfadjoint pair \((X,XSX)\), where \(X\) has law \(4t^3\,dt\) on \((0,1)\) and \(S\) is a standard semicircular element free from \(X\).
It takes \(\mathcal M=W^*(X,Y)\) and computes the product \(X^{-1}YX^{-1}=S\) in the algebra of affiliated operators, giving \(S\in\operatorname{Div}_{L^0(\mathcal M)}\mathcal A\cap\mathcal M\).
Thus \(X,S\) generate \(\mathcal M\) and give its reduced free product representation.
Kato's commutator theorem gives a bounded scalar dual for \(X\), and Voiculescu's right free-product representations lift it and semicircular right creation to the bounded dual system \((T,r)\) for \((X,S)\).
The change of generators identifies the rank-one commutator with \(S\) required of the new second dual.
In the semicircular Fock realization of the free product, a bounded operator on the last two tensor factors realizes this commutator, and a correction by right multiplications gives the first dual.
Small spectral projections of \(X\) give \(\operatorname{dist}(S,C^*(X,Y))\geq1\).
Spectral permanence gives inverse closure of \(C^*(X,Y)\) in \(\mathcal M\).
The norm separation then excludes \(S\) from the division closure in \(\mathcal M\).

The project README maps these environments to responsible mathematical records.
The project review distinguishes manuscript-local checks from fixed proof and source reviews.

---
author: Yin
---

<a id="dab14-u001"></a>
# Dab14-U001: q-Gaussian Defect Kernels and Projective Inverses

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Inspected artifact: the [published 52-page PDF](https://www.numdam.org/article/AIHPB_2014__50_4_1404_0.pdf), 2014, DOI 10.1214/13-AIHP548. |
| source-locator | Locators: Section 4.2.1, Lemma 27 and Theorem 28's scalar inequality, printed p. 1440 / PDF p. 37; projective tensor conventions, p. 1441 / PDF p. 38; Corollary 29 and its first projective-norm argument, p. 1442 / PDF p. 39. |
| inspection | Coverage: `Read`. |

- Record: 2026-09-09, the q-Gaussian mechanism agent; direct primary statement, convention and selected-proof reading for [Yin_S_F0008](../../../strategies/Yin_S_F0008.md#s_f0008).
- Source identity: [Dab14 in the bibliography](../../../literature/readme.md).
  Inspected artifact: the [published 52-page PDF](https://www.numdam.org/article/AIHPB_2014__50_4_1404_0.pdf), 2014, DOI 10.1214/13-AIHP548.
  No local PDF retained; no preprint-to-journal comparison performed.
- Locators: Section 4.2.1, Lemma 27 and Theorem 28's scalar inequality, printed p. 1440 / PDF p. 37; projective tensor conventions, p. 1441 / PDF p. 38; Corollary 29 and its first projective-norm argument, p. 1442 / PDF p. 39.
- Coverage: `Read`.
  The specified established statements are accepted for use under the [external-input rule](../../../../framework/rules/literature-audits.md#accepted-external-inputs).
  This is not a complete audit of their original proofs or of the article.

## Accepted Statements and Conventions

Let $-1<q<1$, $d<\infty$, $M=\Gamma_q(\mathbb R^d)$ with its faithful vacuum trace, and $X_i$ its canonical variance-one selfadjoint generators.
Write $P_m$ for the orthogonal q-particle projections and
\[
\Xi_q=\sum_{m\ge0}q^mP_m.
\]
The source's $r(e_i)$ is right **creation**, so its bounded adjoint satisfies
\[
[r(e_i)^*,X_j]=\delta_{ij}\Xi_q.
\]
Lemma 27 is stated in the Hilbert-Schmidt regime $q^2d<1$ and identifies $a\otimes b^{\mathrm{op}}$ with the kernel $aP_\Omega b:\widehat x\mapsto\widehat a\,\tau(bx)$.

For $\xi$ in degree $m$, Theorem 28 gives
\[
\|W(\xi)\|\le C_{|q|}^{3/2}(m+1)\|\xi\|_q,\qquad
C_r=\prod_{k\ge1}(1-r^k)^{-1}.
\tag{1}
\]
In $\mathcal B=M\widehat\otimes_\pi M^{\mathrm{op}}$, the product is
$(a\otimes b)(c\otimes e)=ac\otimes eb$.
Let $K_q$ denote the tensor representing $\Xi_q$, to distinguish the two products and inverses.
Corollary 29 gives, for $s=|q|d<1$,
\[
\|K_q-1\otimes1\|_\pi
\le C_{|q|}^3\left[
\frac{4s}{1-s}+\frac{5s^2}{(1-s)^2}+
\frac{2s^3}{(1-s)^3}\right]=:\nu(q,d).
\tag{2}
\]
Thus $\nu(q,d)<1$ gives a projective inverse.
For $d\ge2$, the source's sufficient range is $|q|d\le0.13$.

## Inspected Mechanism and Local Adaptation

The first estimate in Corollary 29 uses an orthonormal basis of each degree in the **q-inner product**, writes its projection as a sum of Wick rank-one kernels, and applies (1).
The number of basis vectors is $d^m$.
This portion of the displayed argument was read; it uses a finite faithful trace rather than factoriality.
Although the source introduces the projective notation in a factor setting, the same finite-basis estimate applies in the one-dimensional algebra.
Yin_C_F0020 also supplies an independent one-variable bounded-dual construction.

The substantive correction of the bounded q-annihilation operators by $K_q^{-1}$ is the project deduction [Yin_C_F0020 A](../../../claims/Yin_C_F0020_v1.md#yin_c_f0020), using the right-multiplication action of [Yin_C_F0018](../../../claims/Yin_C_F0018_v1.md#yin_c_f0018).
Those claims own the operator-action proof and its independent-review assessments.

This unit accepts the scalar Haagerup theorem and the specified commutator interface at their checked source scope.
It does not independently audit the original Haagerup proof or all closed-derivation assertions in Lemma 27.
The tensor-valued extension of Theorem 28 and the spatial-tensor inverse bound in Corollary 29 are not needed here.

## Limits and Verification Facts

$K_q^{-1}$ is an inverse in $\mathcal B$, not a bounded inverse of the compact operator $\Xi_q$ on Fock space.
Neither Hilbert-Schmidt membership nor an inverse solely in a spatial tensor product establishes the projective action used in Yin_C_F0020.
This source interface supplies no finite coefficient residual space, no all-q simultaneous bounded dual, and no several-variable rational L2 boundedness or bounded scalar reconstruction conclusion.

The search followed MS23's dual-domain distinction to this published source.
Parsed pages and surrounding definitions were read; Numdam page-image requests timed out.
The kernel convention was cross-checked against the displayed rank-one identification, and the relevant norm formula against the corollary's first proof.
No unresolved objection affects this accepted interface.
No systematic errata search, whole-paper review, numerical experiment or formal verification was performed.

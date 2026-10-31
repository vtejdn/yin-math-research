---
author: Yin
---

# Dab14-U002: Lipschitz conjugate systems and exact q/tensor conventions

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Published 52-page Numdam PDF, 2014, DOI 10.1214/13-AIHP548. |
| source-locator | Definition 1 p. 1405 / PDF 2; Section 4.2.1 pp. 1439-1440 / PDF 36-37; tensor convention p. 1441 / PDF 38; Corollary 29 p. 1442 / PDF 39. |
| inspection | 2026-09-10 exact selected statements/definitions read; PDF pp. 2,37,38 visually inspected; no whole-paper proof audit. |

<a id="dab14-u002"></a>
## Selected source scope

The reading dates, artifact distinctions, substantive source content and actual limits below remain those of that original inspection.
The original-proof inspection limits remain those stated below.

## Retained selected source content

Date: 2026-09-10.
Reviewer: the selfadjoint-interface agent.
This sidecar supplements [Dab14-U001](Yin_U001.md#dab14-u001) retaining that source audit and its original scope.
Source: [Dab14, published Numdam PDF](https://www.numdam.org/article/AIHPB_2014__50_4_1404_0.pdf), 52 pages, 2014, DOI 10.1214/13-AIHP548.
The shared bibliographic identity is [Dab14 in references.bib](../../../literature/references.bib).
Printed page = one-based PDF page + 1403.
Fresh scope: Definition 1 and its preceding paragraph, p. 1405 / PDF p. 2; Section 4.2.1, pp. 1439-1440 / PDF pp. 36-37; Lemma 27, p. 1440; tensor conventions, p. 1441 / PDF p. 38; and Corollary 29's relevant inverse-algebra distinction, p. 1442 / PDF p. 39.
PDF pp. 2, 37 and 38 were visually inspected.
No full-paper proof audit or systematic preprint-to-published comparison is asserted.

<a id="lipschitz-conjugate-condition"></a>
## Lipschitz Conjugate Variable Condition

Exact source: Definition 1, printed p. 1405 / PDF p. 2.
This supplies a precise source-definition home beyond the older U001's q-kernel scope.
For \(M=W^*(X_1,\ldots,X_N)\), the source first defines the polynomial-domain partial free difference quotients for algebraically free coordinates by the Leibniz rule and \(\partial_jX_i=\delta_{ij}1\otimes1\).
The conjugates are \(\xi_i=\partial_i^*(1\otimes1)\in L^2(M)\), when these adjoint vectors exist.
The Lipschitz conjugate variable condition requires the quotients to be defined, every \(\xi_i\) to exist, and

\[
\xi_i\in\operatorname{Dom}\overline{\boldsymbol\partial},\qquad
(\overline{\boldsymbol\partial}\xi_i)_j\in M\bar\otimes M^{\mathrm{op}}
\quad\text{for every }i,j,
\]

where \(\overline{\boldsymbol\partial}\) is the closure of the simultaneous polynomial-domain map \(\boldsymbol\partial=(\partial_1,\ldots,\partial_N)\).
The source uses a spatial von Neumann tensor product, viewed in its product-trace \(L^2\) space.
This is not a projective-tensor bound and is not a definition of operator-Lipschitz functions.
It does not insert boundedness of the conjugates or the dual operators as additional defining clauses.
Its following entropy theorem has a separate embeddability hypothesis; that is not part of Definition 1.

[MS23, p. 8](../MS23/Yin_U001.md#conjugate-and-lipschitz-systems) states its formulation using the individual closed quotients.
Keep these exact closure formulations attached to their sources; replacing a simultaneous graph core by separate approximations is not justified merely by matching notation.
No new claim or reproof of an equivalence is allocated here.

<a id="q-model-and-defect-kernel"></a>
## q-Fock Model, Wick Map and Defect Kernel

Exact source: Section 4.2.1 and Lemma 27, printed pp. 1439-1440 / PDF pp. 36-37.
Existing home: [U001, accepted statements and conventions](Yin_U001.md#accepted-statements-and-conventions).
The real finite-dimensional \(H\), its complexification, \(-1<q<1\), and the symmetrizer inner product give the same general q-Fock construction indexed through [MS23](../MS23/Yin_U001.md#q-fock-and-wick-model).
Here \(\ell(h)\) denotes **left creation**, \(\ell(h)^*\) its q-adjoint, \(\omega(h)=\ell(h)+\ell(h)^*\), and \(\Gamma_q(H)=W^*(\omega(h):h\in H)\), with faithful vacuum trace.
The source's Wick notation is \(\psi(\eta)\Omega=\eta\).
Thus its creation/star notation is reversed relative to MS23's \(l_i^*\) creation convention.

The operator \(r(h)\) is **right creation** by adjoining \(h\) to the right, and \(r(h)^*\) is right q-annihilation.
For the degree projections \(P_n\), the source defines

\[
\Xi_q=\sum_{n\geq0}q^nP_n,\qquad
\Xi_q^{\,Q}=\sum_{n=0}^{Q}q^nP_n.
\]

For finite dimension \(N\), the Hilbert-Schmidt condition in Lemma 27 is \(q^2N<1\).
The source's q-derivations on the polynomial algebra have

\[
\partial_j^{(q)}X_i=\delta_{ij}\Xi_q
=[X_i,r(h_j)]=[r(h_j)^*,X_i].
\]

These are distinct from free difference quotients, whose coordinate derivative is \(1\otimes1\), identified with \(P_\Omega\).
The kernel identification is \(a\otimes b^{\mathrm{op}}\mapsto aP_\Omega b\), not the left-right multiplication operator \(x\mapsto axb\).
The sufficient Hilbert-Schmidt regime is a property of this application, not another definition of \(\Xi_q\).
MS23's free right deletion is not \(r(h_i)^*\) at nonzero \(q\).

<a id="projective-tensor-action"></a>
## Projective Tensor Product and Side Multiplication

Exact source: printed p. 1441 / PDF p. 38, paragraphs before Assumption \(I_q\).
Existing home: [U001](Yin_U001.md#accepted-statements-and-conventions).
The source uses the Banach projective tensor algebra \(M\widehat\otimes_\pi M^{\mathrm{op}}\), with product

\[
(a\otimes b^{\mathrm{op}})(c\otimes d^{\mathrm{op}})
=ac\otimes(db)^{\mathrm{op}},
\qquad
(a\otimes b^{\mathrm{op}})\#x=axb.
\]

The ordinary projective norm is the infimum of \(\sum_k\|a_k\|\|b_k\|\) over tensor representations, followed by completion.
The source calls the image of the contractive left-right action \(LR(M)\), and uses the same symbol \(\#\) for explicitly indicated compatible side actions.
It introduces these conventions for a finite \(II_1\) factor; the existing U001 separately records the finite-tracial adaptation needed by the project.
Corollary 29's projective inverse is the inverse of the tensor representing \(\Xi_q\) in this tensor algebra.
It is not a bounded inverse of the compact Fock-space operator \(\Xi_q\).
The Hilbert-Schmidt identification and the side-multiplication representation have different products; inverse statements require the algebra to be named.

## Outcome and Citation Use

The recheck confirms the old U001's kernel and projective-algebra conventions and supplies Definition 1's exact published locator.
No new mathematical correction to a project claim was found in this scope.
Use “current formulation” for Definition 1, “notation” for Section 4.2.1 and the side products, and “standard” for the projective tensor convention; no historical-origin claim is made.

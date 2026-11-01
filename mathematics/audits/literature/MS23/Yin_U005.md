---
author: Yin
---

<a id="ms23-u005"></a>
# MS23-U005: Main Theorem, Consequences, and Research Interfaces

Inspected edition: [Yin's source notes](readme.md#yin-edition).

- Source: [MS23](../../../literature/pdf/MS23.pdf), supplied published 36-page article; exact artifact identity and version comparison in the [source index](readme.md).
- Scope: introduction and Theorem 1.1, pp. 1-3; every item of Corollary 1.2, pp. 3-4; contextual assertions, pp. 1-5; references, pp. 35-36; the external analytic interface needed by Proposition 6.2.
- Record: 2026-09-09, the coordinating agent, primary reading, local implication checks and self-review; independent review is recorded in the source completion review.
- Coverage: audited within this interface scope, with established external theorems accepted at their explicitly stated inspection depths.
This does not claim complete original-proof audits of those other works.

## Theorem 1.1 and the Complete Internal Chain

For every fixed finite d>=1 and -1<q<1, the canonical variance-one selfadjoint q-Gaussian tuple A has a conjugate system xi with

\[
 \xi_i\in M,\qquad \xi_i\in\operatorname{dom}\overline\partial_j,
 \qquad \overline\partial_j\xi_i\in M\overline\otimes M
 \quad(1\le i,j\le d).
\]

The tuple is represented on the q-Fock space with faithful vacuum trace.
These are exactly the source's Lipschitz conditions, not boundedness of a densely defined dual operator.
The main theorem is assembled from the following separately reconstructed arguments:

1. Strict positive q-Gram matrices and triangular Wick polynomials give a well-defined algebraically free polynomial domain (U001).
2. The recursive normalized dual is the special crossing-partition sum and has commutator delta_ij P_Omega on that domain (U002).
3. Completely paired diagrams force the quadratic crossing exponent; uniform bounded free deletion makes the vacuum functional bounded, so xi_i=D_i^*Omega exists (U003).
4. Theorem 2.5 identifies it as a conjugate variable; the homogeneous Haagerup bound gives operator-norm convergence of its Wick series (U001/U003).
5. The Wick derivative partition induction and coefficient bounds give convergence in the spatial tensor norm, and graph closedness establishes the derivative domain (U004).

The source also contains a one-variable closed formula, a real symmetric mixed extension in Remark 5.4, Wick inversion, entire analytic conjugate series, and a Gibbs potential.
The main theorem does not depend on the later Gibbs potential, the mixed extension, microstates entropy, or any bounded rationality conjecture.

## Corollary 1.2, Items 1 and 2

**Affiliated free field and absence of atoms.**
By U003, Phi*(A)<infinity.
The previously audited free Stam/projection bound gives Phi*(A+sqrt(t)S)<=Phi*(A) for a free semicircular S, so t Phi*(A+sqrt(t)S)->0.
Thus the non-microstates dimension delta-star defined by this Fisher limit equals d.
The accepted CS05 comparison delta-star<=Delta<=d, precisely recorded in [MSY23-U005](../MSY23/Yin_U005.md#msy23-u005), gives Delta(A)=d.
[MSY23-U002, Theorem 3.1](../MSY23/Yin_U002.md#msy23-u002), converts maximal Delta into injectivity of every full affine linear evaluation.
The [MSY23-U004 free-field realization](../MSY23/Yin_U004.md#msy23-u004) then applies, using finite-affiliated invertibility and Theorem 5.6: evaluation embeds the free field in U(M), and its image is Div_U(M) C<A>.
This route retains CS05's original-proof inspection limit, but uses no unproved bounded-dual assumption.

A nonzero field element evaluates to an affiliated inverse and therefore has zero kernel.
If r=r* is a nonconstant field element, r-lambda is nonzero for every real lambda, so each spectral atom projection is zero.
The correct evaluation assertion concerns rational functions as field elements, or nondegenerate expressions representing them; it does not license an expression containing an inverse of the zero field element.
None of these implications places every evaluated rational function in M.

**Analytic evaluation injectivity.**
The required primary source is [Dab14, arXiv:1008.4742v3](https://arxiv.org/pdf/1008.4742), Lemma 37, PDF p. 53, in the 57-page version dated 2013-03-08.
For bounded selfadjoints with finite non-microstates Fisher information, a noncommutative power series of radius R>max_i||A_i|| cannot vanish upon evaluation unless it is the zero formal series.
The statement, surrounding hypotheses and short proof were directly read, and a second reviewer independently checked the primary statement and its lack of a small-q hypothesis.
The theorem is accepted for use; its whole original analytic argument is not independently re-audited here.
This is stronger than polynomial algebraic freeness and supplies a formal/evaluated bridge.

MS23's bibliography [9] prints 2010 with the published volume/pages; the registered journal year of Dab14 is 2014.
Keep its arXiv-version pagination separate from the 52-page journal artifact previously used by the project.

## Corollary 1.2, Item 3: the Nonconstant Qualification

The exact conclusion is that a **nonconstant** selfadjoint polynomial p(A) of degree k>=1 has a distribution function that is Holder continuous with exponent

\[
 \alpha=\frac{1}{2^k-1}.
\]

This follows from the Lipschitz-conjugate part of [BM20, Banna and Mai, arXiv:1809.11153v3](https://arxiv.org/pdf/1809.11153v3), Theorem 1.1, PDF p. 3 of the inspected 33-page preprint, revised 2019-11-20.
Its statement and hypotheses were directly read and accepted, including an independent primary recheck; its original proof was not audited.
Its other finite-Fisher exponent is 2/[3(2^k-1)], which is not the exponent claimed here.
The formal MS23 PDF p. 4 was visually inspected to resolve the superscript in the denominator.

MS23 omits the word nonconstant in this item.
A constant polynomial has a point mass with a discontinuous cumulative distribution function, and k=0 would make the displayed denominator zero.
The correction is necessary but does not affect the main theorem or its nonconstant applications.

## Corollary 1.2, Items 4-6

The finite Fisher statement is immediate from the finite conjugate tuple.
The microstates conclusion delta_0(A)=d uses two additional accepted primary interfaces, checked by the scope reviewer on 2026-09-09:

1. **Embedding for the full interval.**
[Nou06, arXiv:math/0605790v1](https://arxiv.org/pdf/math/0605790), 33 pages, uploaded 2006-05-31, Section 3, pp. 10-13, fixes arbitrary -1<q<1 and finite d.
Lemma 3.1, p. 11, retains joint moments after a uniform truncation.
The construction on p. 13 immediately before Theorem 3.3 explicitly embeds Gamma_q(R^d), normally and trace preservingly, in a tracial ultraproduct of finite-dimensional tracial algebras.
Embed each finite-dimensional tracial algebra trace preservingly in the hyperfinite II1 factor R; passing to ultraproducts gives the required R^omega embedding.
The parameter declaration, truncation statement and embedding passage were directly read.
The complete original central-limit/truncation/extension proof is accepted rather than independently re-audited.
Nou06 is a different article from the 21-page Nou04 used for mixed norm estimates.
This argument uses the explicit embedding, not a general inference from QWEP terminology.
2. **Lipschitz entropy theorem.**
[Dab14 arXiv v3](https://arxiv.org/pdf/1008.4742), Corollary 25, PDF p. 38, final sentence, and the unnumbered introductory theorem on p. 2, give delta_0(A)=d for an R^omega-embeddable selfadjoint tuple with Lipschitz conjugates.
The exact statement and context were read.
This general assertion has no small-q assumption; the article's separate small-q verification of its hypotheses must not restrict the theorem's use with MS23's all-q verification.
Its original stochastic/entropy proof was not audited here.

The initial check of [Sni01](https://arxiv.org/pdf/math/0007158), the source's reference [24], revealed that its Gaussian random matrix construction states a nonnegative-q restriction.
That specific construction is not used as evidence for negative q.
The targeted search stopped after Nou06 supplied the exact all-q embedding; no failure of embeddability is inferred from Sni01's narrower model.

**Tensor convention for these applications.**
Dab14 and DI16 formulate the Lipschitz derivative in M spatial-tensor M^op, whereas MS23 and U004 use ordinary M spatial-tensor M.
An identification of their L2 spaces alone would not identify these operator-norm completions.
U004 equations (8)-(10), however, bound the absolute sum of the norms ||a||||b|| of the individual simple-tensor terms before taking the spatial norm.
The identical summable majorant therefore applies after replacing each second factor b by b^op.
Polynomial approximations converge in that spatial tensor norm as well.
The canonical trace-L2 identification then identifies the limit with the same closed difference quotient.
Thus the stronger tensor convention required by the two external theorems is actually supplied by the reconstructed estimates, without assuming that partial passage to an opposite algebra is spatially isometric.
The original integration reviewer supplied and checked this conversion, so that corrected finding is self-review.
The fresh2026-10-21 isolated integration finding checks the existing conversion independently at the scope below.

For **d>=2**, the non-Gamma assertion follows from the exact finite-Fisher non-Gamma theorem, [Dab10-U001, Theorem 13](../Dab10/Yin_U001.md#dab10-u001), already checked in arXiv:0804.2906v2, PDF p. 10.
It asserts that bounded central sequences are asymptotically scalar.
Its statement and applicability are accepted; its original proof was not re-audited here.

Items 5 and 6 need d>=2.
For d=1, M is a diffuse abelian algebra, so it has nontrivial central sequences and is its own Cartan subalgebra.
These are concrete scope corrections to the abbreviated introductory corollary.
The source's main Lipschitz, free-field and potential conclusions still apply at d=1.

For **no Cartan**, [DI16, Dabrowski and Ioana, arXiv:1212.6425v1](https://arxiv.org/pdf/1212.6425), 31-page preprint dated 2012-12-27, Theorem 1.3, PDF p. 3, applies to an algebraically free bounded selfadjoint tuple with d>=2 and Lipschitz conjugates, and concludes that the generated algebra is a II1 factor with no Cartan subalgebra.
The source page was visually checked because parsed text can lose the equality in >=2.
All these hypotheses follow here from U001/U004.
The theorem requires no R^omega embedding, so this item can be obtained independently of the preceding entropy route.
Its original derivation/deformation proof was not audited.
The stronger tensor-product assertion in that theorem is not required for the present corollary.

## What This Supplies to the Project

The complete audit replaces the earlier selected-reading interface for the supplied published version.
It gives precise all-q polynomial-domain duals, their vacuum adjoints, q-Wick derivatives, Lipschitz conjugates and entire analytic conjugate series.
The essential decay is q raised to a quadratic crossing count for the specially structured series.

For [Yin_S_F0008](../../../strategies/Yin_S_F0008.md#s_f0008), the following distinctions remain in force:

- MS23's normalized polynomial-domain D_i, free right deletion r_i, and right q-annihilation are three different operators when q is nonzero.
- [Yin_C_F0020 A](../../../claims/Yin_C_F0020_v1.md#yin_c_f0020) constructs simultaneous bounded duals in a quantitative small-q range by correcting the right q-annihilator through a projective kernel inverse.
The full MS23 proof supplies no enlargement of that range.
- The estimates of D_i^*Omega do not control the non-vacuum outputs of D_i.
A bounded dual on all L2 is a separate norm question.
- Entire conjugate series do not supply finite coefficient residual dimension for an arbitrary rational element, nor a bounded inverse linear representation.
- The two multivariable targets F_A intersect L2(M) subset M and F_A intersect M = Div_M C<A> remain open within this project.
The all-q scalar marginal result and the refutation of the unchanged universal Yin_C_F0001 retain their existing assessments.

## Search and Verification Boundaries

All introductory and reference pages were read against the supplied source.
Historical claims about isomorphism, strong solidity, previous factoriality results, orthogonal-polynomial books and general statistics are contextual citations, not newly proved results or exhaustive current-status claims.
The original proofs of all 27 references were not audited.
The title-and-authors search combined MS23 with erratum/correction; it identified no correction notice in that bounded search, which does not prove that none exists.
An attempted Bozejko institutional access encountered an anti-bot page, and the historical Krolak PostScript endpoint returned 404.
[MS23-U001, the homogeneous norm estimate](Yin_U001.md#setting-norms-and-corrected-wick-recursion) and [MS23-U001, the free-deletion bound](Yin_U001.md#lemma-22-free-right-deletion-is-bounded) record the scalar-q primary substitutes and their exact remaining proof-inspection limits.
The inaccessible Krolak theorem concerns the mixed-parameter Haagerup inequality; no inspection of that theorem is claimed here.

The [source index](readme.md) preserves the earlier 30-page arXiv reading separately from this full 36-page published audit.
No source artifact was modified.
Mathematical reconstruction, independent AI review, exact finite computation, formal verification and human review are distinct; only the first three are performed here.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | MS23, the supplied 36-page published article, Advances in Mathematics 413 (2023), 108834; printed and one-based PDF pages agree. The earlier 30-page arXiv reading and external source editions retain their separate recorded scopes. |
| source-locator | Introduction and Theorem 1.1, printed/PDF pp. 1-3; all Corollary 1.2 items, pp. 3-4; context, pp. 1-5; references, pp. 35-36; the external analytic interface for Proposition 6.2. |
| inspection | 2026-09-09: primary reading, qualified consequence-chain and local implication checks with self-review; separate integration review is recorded in the source home. Accepted external theorems keep their exact statement, selected-proof and access limits; the 27 original references were not recursively audited. Earlier 30-page arXiv reading is separate from this 36-page published audit, with no exhaustive version/errata or current-status claim. |

## Current project proof review

The fresh2026-10-21 [independent finding](../../reviews/Yin_R_F0060_v1.md#ms23-u005-isolated-finding) covers the complete qualified local integration chain, opposite-tensor majorant and common simultaneous-gradient approximation.
It checks fixed local mathematics at the retained accepted-source depth; it performs no new primary-page inspection or finite execution and certifies no old reviewer isolation or date.
The [later old-findings comparison](../../reviews/Yin_R_F0060_v1.md#ms23-old-findings-comparison) preserves the original negative interface findings and distinguishes their historical evidence from this current proof review.

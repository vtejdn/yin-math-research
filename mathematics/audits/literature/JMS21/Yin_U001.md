---
author: Yin
---

# JMS21: Rational Fock Series and Finite-State Stability

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Inspected [arXiv:2010.06585v1](https://arxiv.org/pdf/2010.06585v1), 2020-10-13, 23 pages, for the formally published 2021 work. |
| source-locator | Theorem A, p.3; Lemma 3.4, pp.9–10; Theorem 3.5, pp.10–11. |
| inspection | The statements and relevant proof passages were read as text. |

No successful rendered-page check or complete journal/preprint comparison is claimed.

<a id="jms21-u001"></a>
## JMS21-U001: Square-Summable Coefficients and the State Gramian

Date: 2026-09-09, the transfer-route agent.
Scope: a selected mechanism for [Yin_T_F0001](../../../tasks/Yin_T_F0001_v1.md#yin_t_f0001); no whole-paper audit.

Source: Jury, Martin, and Shamovich, *Non-commutative rational functions in the full Fock space*, Trans. Amer. Math. Soc. 374(9) (2021), 6727-6749, [DOI](https://doi.org/10.1090/tran/8418).
The inspected primary artifact is [arXiv:2010.06585v1](https://arxiv.org/pdf/2010.06585v1), 2020-10-13, 23 pages: Theorem A, p. 3; Lemma 3.4, pp. 9-10; Theorem 3.5, pp. 10-11.
Text of these statements and their relevant proof passages was read; no successful rendered-page check or complete journal/preprint comparison is claimed.

### Source Interface

Let r be a noncommutative rational function regular at the scalar origin, with a minimal realization

\[
r(z)=b^*(I-\sum_i A_i z_i)^{-1}c,
\qquad \alpha_w=b^*A^w c.
\]

Lemma 3.4 and Theorem 3.5 show that `sum_w |alpha_w|^2<infinity` forces every state-entry series to have square-summable coefficients and makes A jointly similar to a strict row contraction.
Theorem A supplies the associated rational Fock-space and bounded free-multiplier characterizations.
These concern formal Taylor coefficients and the free row-ball geometry, not evaluation at an arbitrary tracial tuple.
The consistent convention above is used below without asserting a source typographical error from parsed text.

### Independent Reconstruction

Treat the zero series separately.
Minimality gives words u_a,v_b such that the rows `b* A^{u_a}` form an invertible matrix R and the columns `A^{v_b}c` form an invertible matrix S.
Thus

\[
(RA^wS)_{ab}=\alpha_{u_aw v_b}.
\]

For fixed u,v, concatenation `w -> uwv` is injective.
Square summability of alpha therefore gives

\[
\sum_w\|A^w\|_{\rm HS}^2<\infty.
\]

Define the norm-convergent finite-dimensional Gramian

\[
G=\sum_w A^w(A^w)^*\ge I,
\qquad
G-\sum_i A_iGA_i^*=I.
\]

The identity follows by partitioning nonempty words by their first letter.
With `B_i=G^{-1/2}A_iG^{1/2}`,

\[
\sum_i B_iB_i^*=I-G^{-1}
\le (1-\|G\|^{-1})I<I.
\]

This directly proves strict row contractivity after similarity.
It replaces the source's external similarity-theorem step by an explicit positive Gramian; no irreducibility assumption is needed.
The author's check covered multiplication order, both minimality bases, coefficient injection, convergence, and the empty word.
The coordinating agent independently read the cited source passages and checked this reconstruction on 2026-09-09, including the strict inequality and the contraction estimate below.
This is a selected proof-mechanism review, not a full-paper audit or formal verification.

### Exact Transfer Boundary

One useful conditional deduction is immediate.
If a tuple Y satisfies `sum_i Y_i*Y_i<=I` and the above coefficient hypothesis holds, then

\[
V=\sum_i B_i\otimes Y_i,
\qquad \|V\|\le\|B_{\rm row}\|\|Y_{\rm col}\|<1.
\]

Hence the pencil has a bounded inverse.
The scalar-pivot argument in [Miy22-U005](../Miy22/Yin_U005.md#miy22-u005) then places the realized scalar output in `Div_M C<Y>`; the similarity only uses scalar coefficients.
This conditional deduction has not received a separate project-claim audit.

For [Yin_C_F0001](../../../claims/Yin_C_F0001_v1.md#yin_c_f0001), boundedness of f or of its evaluated state vectors in L2(M) does not identify the formal Taylor coefficients with an orthonormal expansion.
A separate coefficient estimate is required.
Scalar-origin regularity also needs justification; arbitrary free-field elements need not have it.
Rescaling X to a contraction changes the rational series and does not automatically establish its square summability.

Finally, polynomial matrix V with decaying powers produces norm limits of holomorphic polynomials.
Such a target cannot cover every Yin_C_F0001 element: for Haar U, the bounded rational element U^{-1} is outside the norm closure of C[U], as its vacuum vector has negative Fourier degree.
A general strategy must therefore allow suitable bounded rational coordinates or separate Laurent expansions, or retain an explicit restricted subclass.
This source supplies a stability mechanism, not the missing general bounded scalar descent.

## Additional original definition reading

The original unit's theorem proof/review depth remains unchanged, and this maintenance performed no new source opening.

<a id="jms21-definition-recheck"></a>
Date and reviewer: 2026-09-10, the coordinating agent.
Source: [JMS21, arXiv v1](https://arxiv.org/pdf/2010.06585v1), 2020-10-13, 23 pages.
The exact-version temporary PDF title and complete printed/PDF p. 4 were read for the definitions below, together with the existing [JMS21-U001](Yin_U001.md#jms21-u001) applicability account.
No new proof audit of the stability theorem or journal/preprint comparison is claimed.

<a id="free-row-ball"></a>
## Free Row Ball and Fock Hardy Space

Section 2, p. 4: the noncommutative universe is the disjoint union of all finite matrix levels; the free row ball consists of tuples with row-operator norm less than one.
Explicitly this norm is $\|\sum_jZ_jZ_j^*\|^{1/2}$.
The source also allows a level on a fixed separable infinite-dimensional Hilbert space.
The Fock Hardy space consists of square-summable formal word coefficients.
This is the full Fock coefficient space already used in the formal-series group; it is not another definition for each matrix level.
Identifying these coefficients with a chosen expansion in $L^2(M,\tau)$ requires the actual basis/coefficient interface.
The source's realization and stability results do not supply that interface for an arbitrary tracial tuple.

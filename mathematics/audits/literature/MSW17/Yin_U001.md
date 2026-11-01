---
author: Yin
---

<a id="msw17-u001"></a>
# MSW17-U001: Selfadjoint Conjugate Variables and Contraction Estimates

The inspected edition and source context are described in the [source notes](readme.md#yin-source-edition).

## Source and inspection

Source edition: [MSW17, retained arXiv:1502.06357v2 PDF](../../../literature/pdf/MSW17--arxiv-v2.pdf), 26 pages; its arXiv watermark says 2 September 2015, while the internal title-page date is 12 May 2018; this is the retained preprint artifact, not the publisher typesetting.

Source passages: Definition 2.1, Remark 2.2 and Propositions 2.3--2.4, pp.5--7; Theorem 2.5, p.7; Definition 2.6, p.8; Section 3.2, pp.11--16, especially Lemmas 3.3--3.4 and equations (3.2)--(3.6), pp.12--13; printed and one-based PDF pages coincide.

Inspection: 2026-10-16, delegated AI source-audit agent for Yin; prior selected reading deepened to a full check of the source's algebraic and analytic interfaces, within the full-paper reading whose distinct scope is retained in the [source comparison](../../../ledger/Yin_L_F0053_v2.md); audited within the stated scope, with the Dab10/Mai15 attribution boundary and retained external inputs stated below.

The initial 2026-10-16 reading inspected selected statements, hypotheses, adjacent proof explanations and source attributions, without an independent proof audit or whole-paper review.
The later source inspection described here deepened those algebraic and analytic interfaces; it does not retrospectively enlarge the earlier reading or a review that used it.
The present source inspection is user directed and does not resume an autonomous mathematical Task.

<a id="the-sources-selfadjoint-setting"></a>
<a id="relation-to-condition-a"></a>
## Exact selfadjoint specialization of condition A

Let $(M,\tau)$ be a finite von Neumann algebra with faithful normal tracial state, let $X=(X_1,\ldots,X_n)$ be bounded generators, and put $H=L^2(M,\tau)$ and $\mathcal P=\mathbb C\langle X,X^*\rangle$.
The condition called A in this literature question consists of complex-linear outer derivations
\[
 \delta_i:\mathcal P\subset H\longrightarrow H\bar\otimes H,
 \qquad \delta_iX_j=\delta_{ij}1\otimes1,
 \qquad 1\otimes1\in\operatorname{Dom}\delta_i^*.
\]
The last membership concerns the actual Hilbert-space adjoint of the operator with that dense starred core.
Condition A alone imposes neither normality of $X$ nor reality, coassociativity, or algebraic tensor values for $\delta_i$ on the whole starred algebra.

If $X_j=X_j^*$ for every $j$, then $\mathcal P=\mathbb C\langle X\rangle$ and the specified generator values determine the usual word-cut difference quotients.
Reality, algebraic tensor values and coassociativity follow from those word formulas.
The vacuum-adjoint condition is the conjugate-variable condition, with the source convention $\xi_i=\partial_i^*(1\otimes1)$ and
\[
 \tau(\xi_i p)=(\tau\otimes\tau)(\partial_i p),
 \qquad p\in\mathcal P.
\]
Conversely, MSW17 defines conjugate relations on formal polynomials before evaluation, proves absence of algebraic relations in Theorem 2.5, and then obtains the well-defined densely defined difference quotients and the actual vacuum adjoints.
The inspected source proofs of this equivalence and algebraic descent are Propositions 2.3--2.4 and Theorem 2.5, pp.5--7 of the retained edition.
For the finite tuple under condition A, $\Phi^*(X)=\sum_i\|\xi_i\|_2^2<\infty$.
Definition 2.6 sets $\Phi^*(X)=\infty$ when no conjugate system exists.

The source's original ambient-algebra formulation allows $N=W^*(X_1,\ldots,X_n)\subseteq M$ for a selfadjoint tuple and uses $P=\mathbb C\langle X_1,\ldots,X_n\rangle$.
Before evaluation at $X$, Definition 2.1 defines formal difference quotients in the selfadjoint indeterminates $Z_1,\ldots,Z_n$ and asks for vectors $\xi_j\in L^2(M,\tau)$ such that
\[
 (\tau\otimes\tau)((\partial_j Q)(X))=\tau(\xi_j Q(X))
 \qquad(Q\in\mathbb C\langle Z_1,\ldots,Z_n\rangle).
\]
Remark 2.2 projects these vectors onto $L^2(N,\tau)$ to obtain the conjugate system in the generated algebra; when $M=N$, that projection changes no ambient generated space.
Proposition 2.3 makes a polynomial relation descend to its evaluated derivatives, and Proposition 2.4 repeatedly contracts derivatives of a highest-degree monomial before Theorem 2.5 establishes injective evaluation.
For the analytic source estimates, the densely defined operator has domain exactly $P$ in $L^2(N)$.
The original adjoint interface is attributed to Voi98, Corollary 4.2 and Proposition 4.3, whose separate inspected passages are retained in [Voi98-U004](../Voi98/Yin_U004.md#voi98-u004).
The [ACSY24-U001](../ACSY24/Yin_U001.md#acsy24-u001) unit supplies the distinct general starred-core source interface and its own limits.

<a id="adjoint-domains-and-the-sources-estimates"></a>
## What the analytic source supplies

For $a,b,p\in\mathcal P$, Lemma 3.3 gives
\[
 \partial_i^*(a\otimes b)
 =a\xi_i b-(\mathrm{id}\otimes\tau)(\partial_i a)b
       -a(\tau\otimes\mathrm{id})(\partial_i b),
\]
and $\mathcal P\otimes\mathcal P\subset\operatorname{Dom}\partial_i^*$, hence closability.
Lemma 3.4 supplies
\[
 \|\partial_i^*(p\otimes1)\|_2,
 \quad\|\partial_i^*(1\otimes p)\|_2
 \leq\|\xi_i\|_2\|p\|,
\]
and
\[
 \|(\mathrm{id}\otimes\tau)\partial_i p\|_2,
 \quad\|(\tau\otimes\mathrm{id})\partial_i p\|_2
 \leq2\|\xi_i\|_2\|p\|.
\]
All these statements allow arbitrary complex polynomials $p$.
They are operator-norm-to-$L^2$ estimates and do not assert that the difference quotient or its canonical dual is bounded on $H$.

The proof, tensor-leg ordering, full complex-polynomial range and constants retain the source-inspection scope stated above and in the [full-source comparison](../../../ledger/Yin_L_F0053_v2.md).
The printed attribution of Lemma 3.4 is not a literal statement match: Dab10 Lemma 12 states its sharp estimate for selfadjoint or unitary elements.
Mai15 Theorem 4.9 supplies a separately checked, noncircular proof for arbitrary complex elements under the real, algebraic-range and coassociative hypotheses that hold here.
Its exact scope is recorded in [Mai15-U002](../Mai15/Yin_U002.md#mai15-u002).
No original-paper author confirmation of this attribution detail is claimed.

## The selfadjoint bounded-vector dual interface

The canonical polynomial contraction is $C_i p=(\mathrm{id}\otimes\tau)\partial_i p$.
It satisfies $[C_i,X_j]p=\delta_{ij}\tau(p)1$.
The preceding adjoint identity identifies $\partial_i^*(p\otimes1)$ with the restriction of $C_i^*$ to the polynomial core.
The estimates on both restrictions are exactly the input for the closed-graph and bounded-approximation argument already retained in [Dab10-U002](../Dab10/Yin_U002.md#dab10-u002).
That argument places every $x\Omega$, $x\in M$, in both the domain of the closure of $C_i$ and the domain of its adjoint.
It also passes the commutator identity to bounded vectors.

With the generator-first sign convention, take $D_i=-\overline{C_i}$.
The resulting selfadjoint-generator conclusion is
\[
 M\Omega\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*,
 \qquad [X_j,D_i]x\Omega=\delta_{ij}P_\Omega x\Omega
 \quad(x\in M).
\]
Here $P_\Omega$ is the orthogonal projection onto $\mathbb C\Omega$.
This is the bounded-vector domain condition called S in the literature question.
The sign is essential: the positive contraction $C_i$ has the opposite commutator order.
The domain conclusion is an existing source-based consequence using the cited graph argument, not a theorem explicitly stated as S in MSW17.

## General and normal tuples: what is not supplied

For a nonselfadjoint tuple, the values of $\delta_i$ on $X_j^*$ are not specified by their values on $X_j$.
One therefore cannot infer the real free-difference-quotient formula, its coassociativity on the starred core, or the estimates above from condition A alone.
The word-cut argument still handles the holomorphic subalgebra, but that subalgebra need not be a dense star core for $H$.
Normality of each $X_j$ does not itself fill this analytic gap.
The source's two-sided zero-divisor and semicircular-perturbation arguments do not establish normal A-to-S; their separate inspection limits remain in the [full-source comparison](../../../ledger/Yin_L_F0053_v2.md).

<a id="earlier-preprint-and-verification-limits"></a>
## Edition, searches and revision scope

The [arXiv version record](https://arxiv.org/abs/1502.06357v2), rechecked on 2026-10-16, identifies this work as an extended version of arXiv:1407.5715.
The earlier preprint has a different title and result numbering, so its passages are not substituted for this artifact's 26-page locators.
The authors' [arXiv:1407.5715v2 record](https://arxiv.org/abs/1407.5715v2) identifies the earlier title *Absence of algebraic relations and of zero divisors under the assumption of finite non-microstates free Fisher information* and says that it was not intended for publication in that form.
That earlier preprint was consulted online at its conjugate-variable definitions and Lemmas 3.3--3.4 during the 2026-10-16 directed search.
The search followed the exact title, both arXiv identifiers and the authors' publication metadata; the [publisher record](https://www.sciencedirect.com/science/article/pii/S0001870815301183) establishes the 2017 publication identity.
Those readings do not substitute the earlier preprint or publisher typesetting for the mathematical passages of the retained arXiv:1502.06357v2 artifact.
At the initial selected-reading stage, Theorem 3.1's no-zero-divisor conclusion was located as context but its full proof and entropy-dimension regularization arguments were uninspected; the later full-paper work retains its separate scope in the [source comparison](../../../ledger/Yin_L_F0053_v2.md).
This audit used the retained PDF throughout; the experimental arXiv HTML was consulted for comparison of notation and its dynamically generated date was not treated as a different mathematical edition.
Canonical publication identity is in [references.bib](../../../literature/references.bib).
No complete comparison with publisher typesetting, exhaustive search for errata, or formal verification was performed.

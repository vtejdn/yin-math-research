---
author: Yin
---

<a id="lin00-u001"></a>
# Lin00-U001: Rationality Criteria, Amplifications and Source Conventions

Source: [Lin00, retained arXiv v1](../../../literature/pdf/Lin00--arxiv-v1.pdf), dated 1999-07-12, seven pages.
All page numbers in this unit refer to this preprint.
The published work is J. Funct. Anal. 171(1) (2000), 115--123.
The registry (private lookup: `../../../literature/registry.md#lin00-full-audit-intake`) owns artifact and version facts.
This is part of the user-requested [complete source audit](readme.md).

## Setting and the two representations

Let $G=F(X)$ be a free group and set

$$
H_+=\ell^2(G),\quad M=W(G),\quad A=C_r^*(G),\quad U=U(G).
$$

Here $U$ is the $*$-algebra of closed densely defined operators affiliated with the finite group von Neumann algebra $M$, with sums and products interpreted as closures.
The source's inner product is linear in the first variable.

The rooted Cayley tree has edge set $E$, a disjoint union of copies of the regular left $G$-set.
The vertex-to-edge map sends a non-root vertex to the last edge on the path from the identity and sends the identity to an extra scalar vector.
Its linear extension is a unitary

$$
P:H_+\longrightarrow H_-:=\ell^2(E)\oplus\mathbb C,
\qquad Q=P^{-1}=P^*.
$$

This is the construction already checked in [DR97-U002](../DR97/Yin_U002_v1.md#dr97-u002).
For $a\in M$, let $a_E$ denote the bounded amplification on the edge space.
For $u\in U$, the closed amplification has domain

$$
\operatorname{Dom}(u_E)
=\left\{(\xi_j)_j\in\bigoplus_j H_+:
 \xi_j\in\operatorname{Dom}u\text{ for every }j,
 \sum_j\|u\xi_j\|^2<\infty\right\}.
$$

The last condition is necessary for infinite multiplicity; the Cartesian-product formula on p. 2 omits it.
For finite multiplicity it follows from the componentwise domain conditions.

The preprint extends operators to $H_-$ by

$$
\widehat u=u_E\oplus I_{\mathbb C}.
$$

This convention preserves products, adjoints and invertibility, but is not an additive or complex-linear representation.
If $e$ is the projection onto the scalar summand, then

$$
\widehat{a+b}=\widehat a+\widehat b-e,
\qquad \widehat{ca}=c\widehat a+(1-c)e.
$$

Thus algebraic identities using additivity on $H_-$ hold only after accounting for a finite-rank correction.
[U002](Yin_U002_v1.md#lin00-u002) does so.
The zero-scalar convention used in DR97 differs by the rank-one projection $e$ for every bounded coefficient.
It gives the same **finite-rank property** for the tests below, not necessarily the same operator or numerical rank.
For Proposition 1.2 we retain the source's identity-scalar convention and its exact operator domains; see [U003](Yin_U003_v1.md#lin00-u003).

## Bounded fractions and common denominators

The accepted finite-tracial affiliated $*$-algebra and spectral-calculus foundation is identified in U004.
It supplies the following concrete fraction construction, including the common-denominator assertion used in U002.
For $u_1,\ldots,u_n\in U$, regard the row $T=(u_1,\ldots,u_n)$ and column $V=(u_1,\ldots,u_n)^{\mathsf T}$ as affiliated matrix operators.
Put

$$
s=(1+TT^*)^{-1/2},\qquad t=(1+V^*V)^{-1/2}.
$$

Spectral calculus and polar decomposition give bounded operators $sT$ and $Vt$, of norm at most one: the scalar bound is $r/(1+r^2)^{1/2}\leq1$.
The positive elements $s,t\in M$ have zero kernel and dense range, so are invertible in $U$.
In particular $a_i=su_i$ and $b_i=u_it$ are bounded, and

$$
u_i=s^{-1}a_i=b_it^{-1}\quad(1\leq i\leq n).
$$

The expressions here denote closed affiliated products, including the row and column constructions in a finite matrix amplification of $M$.
This proves simultaneous left and right denominators without an additional unverified Ore-localization premise.
If a represented affiliated element is invertible, its bounded numerator is also invertible in $U$, since it is a product of invertible affiliated elements.
U002 uses precisely this observation for its numerator and denominator changes.
On 2026-10-10 the algebra reviewer independently checked this later supplement, including the matrix-corner interpretation, norm bounds, regularity and closed-product fraction identities, and found no additional obligation beyond the stated foundational input.

<a id="lin00-fraction-tests"></a>
## Fraction tests and Theorem 1.1

Write

$$
D(G)=\operatorname{Div}_{U}\mathbb CG,
\qquad S(G)=\operatorname{Div}_{A}\mathbb CG.
$$

The source initially calls $S(G)$ the matrix rational closure, then uses DR97 to identify it with the scalar division closure.
The equality of the closures is an input with a proof, not a convention.
Its precise source scope is recorded in [U004](Yin_U004_v1.md#lin00-u004).

Every $u\in U$ admits bounded left and right fractions

$$
u=s^{-1}a=bt^{-1},\qquad a,b,s,t\in M,
\qquad s,t\text{ invertible in }U.
$$

For this fraction pair define bounded operators of specified types:

$$
A_P(s,a,b,t)=\widehat s P b-\widehat a P t:H_+\to H_-,
$$

$$
B_P(s,a,b,t)=sQ\widehat b-aQ\widehat t:H_-\to H_+.
$$

Let $R(G)$ require both operators to have finite rank for **every** bounded fraction pair; let $R'(G)$ require it for **at least one** such pair.
Theorem 1.1, p. 3, states

$$
D(G)=R(G)=R'(G),\qquad D(G)\cap M=S(G),
$$

and asserts that every $u\in D(G)$ has left and right fraction representations with all four coefficients in $S(G)$.
The proof is reconstructed in U002, with the bounded DR97 input and source-scope boundary in U004.

For bounded $u$, choose $(s,a,b,t)=(1,u,u,1)$.
Then

$$
A_P=Pu-\widehat uP,\qquad B_P=Q\widehat u-uQ=-QA_PQ.
$$

Consequently only one commutator needs checking in the bounded case.
This computation does **not** remove one of the two tests in the general unbounded statement.
The preprint explicitly says after Theorem 1.1 that the author could not prove the proposed one-test weakening.
This audit does not assert its failure, or present the 1999 comment as a current open-problem assessment.

On $H_+\oplus H_-$, put

$$
F=\begin{pmatrix}0&Q\\P&0\end{pmatrix},\qquad
\widetilde a=\operatorname{diag}(a,\widehat a).
$$

The two tests are exactly the off-diagonal blocks of $\widetilde sF\widetilde b-\widetilde aF\widetilde t$; finite rank of this block operator is equivalent to finite rank of both blocks.
This checks the alternate formulation on pp. 3--4, including its operator types.

<a id="lin00-finite-codimension"></a>
## Proposition 1.2 and its domain quantifier

Proposition 1.2, p. 4, states that $u\in D(G)$ exactly when there is a subspace $V\subset H_+$ of finite **algebraic** codimension such that

$$
V\cap\operatorname{Dom}u
=V\cap P^{-1}\operatorname{Dom}\widehat u,
\qquad Pu\xi=\widehat uP\xi
\quad(\xi\text{ in this common domain}).
$$

This does not assert that $V\subset\operatorname{Dom}u$, that $V$ is closed, or that the commutator is a bounded operator on all of $H_+$.
The sentence immediately following the proposition explicitly requires equality of domains.
U003 reconstructs the two implications, including the algebraic complement choices in the source proof.

## French synopsis and introductory assertions

The French synopsis on pp. 1--2 repeats the main results, but its displayed inverse defect is $sP^{-1}b-tP^{-1}a$, whereas the English definition on p. 3 and the proofs use $sP^{-1}b-aP^{-1}t$.
The English definition is the one audited.
The French wording also calls $R(G),R'(G)$ subsets of $G$ instead of $U(G)$; the intended ambient algebra is explicit in the English text.
These are local source discrepancies, not author-confirmed corrections.

The p. 3 phrase assigning $g*=0$ on a one-element **set** is not a group action as literally written.
The tree construction is interpreted via the distinguished scalar vector and the specified operator lift.
The finite-rank defect calculation is insensitive to a change confined to that scalar summand, as shown above.

The introductory identification of $D(G)$ with a free field is separate from the proof of Theorem 1.1: U002 proves equality of the fraction-test class with division closure without using the assertion that this closure is a division ring.
U004 records the actual evidence for the contextual free-field assertion and other external references.
The bibliography and historical remarks were read; no historical priority or exhaustive errata search is inferred.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Lin00, arXiv:math/9907075v1, dated 1999-07-12, retained seven-page PDF; journal metadata J. Funct. Anal. 171(1) (2000), 115--123. Full journal/preprint equality is not assumed. |
| source-locator | French synopsis pp. 1--2; Introduction pp. 2--4, definitions of the affiliated, division and rational closures, Theorem 1.1, block-operator reformulation and Proposition 1.2; bibliography p. 7. |
| inspection | 2026-10-10: coordinating agent read the complete extracted text and visually checked all seven pages, reconstructed the typed fraction tests, bounded/common fraction construction and block equivalence, checked bounded reduction, compared the French and English formulas, and checked the exact domain quantifier. The algebra and domain reviewers independently checked the statement extraction, scalar conventions, typed tests, bounded/block equivalences and domain quantifier without requiring a mathematical correction. The later common-denominator supplement is separately checked as recorded below. Main proofs and their independent-review records are in U002--U004; no claim of formal or external human verification. |

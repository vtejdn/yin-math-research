---
author: Yin
---

# NS06-U002: Probability definitions and scalar-law identities

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Registered supplied 434-page publisher-layout NS06.pdf; printed pages equal PDF pages minus 17. No source bytes or artifact facts changed. |
| source-locator | Definitions 1.1/1.3/1.12,2.16,5.3,11.3,15.3 and Proposition 12.3, Theorems 12.5/12.7 with Notation 12.6 at the exact printed/PDF locators retained below. |
| inspection | 2026-09-10 selected definitions with the disclosed page-boundary extraction and one visual page; the scalar-law interface reuses the 2026-09-16 publisher-edition reading retained in R_F0099. No whole-book or new source-proof audit. |

<a id="ns06-u002"></a>
<a id="ns06-definition-recheck"></a>
## Original selected probability definitions

Date and reviewer: 2026-09-10, the coordinating agent.
Source: [NS06](../../../literature/pdf/NS06.pdf), the supplied 434-page publisher-layout edition.
This selected definition review supplements the earlier [NS06-U001](Yin_U001.md#ns06-u001) polar/product interface; it does not enlarge that earlier proof inspection or constitute a whole-book audit.
Printed page numbers below equal PDF page numbers minus 17.
The listed definition passages were read directly from the PDF; PDF pp. 20-22, 28, 46, 81-82, 192, 257-258 were extracted with page boundaries.
The rendered page at PDF p. 258 was also inspected for the cumulant convention.

<a id="probability-space"></a>
## Probability Spaces and Basic Operator Terminology

Definition 1.1, printed pp. 3-4 / PDF pp. 20-21: a noncommutative probability space is a unital complex algebra with a unital linear functional.
A trace satisfies $\varphi(ab)=\varphi(ba)$; a star-probability space additionally has a star-algebra and positive functional.
Definition 1.3, printed p. 5 / PDF p. 22, defines faithfulness by $\varphi(a^*a)=0\Rightarrow a=0$.
Definition 1.1(3) gives the usual selfadjoint, unitary and normal conditions.
In the project, the von Neumann algebra, faithful normal tracial state and chosen tuple are stated in each consumer; these hypotheses are not new indexed definitions for each model.

## Free Independence

Definition 5.3, printed pp. 64-65 / PDF pp. 81-82: unital subalgebras $(A_i)$ are free when $\varphi(a_1\cdots a_k)=0$ for centered $a_j\in A_{i(j)}$ with neighboring indices distinct.
Sets are free when their generated unital algebras are free.
Star-freeness uses the generated star-algebras.
This distinction matters when a holomorphic subalgebra is used later; it does not change the initial algebra in a rationality statement automatically.

## Haar Unitary

Definition 1.12(1), printed p. 11 / PDF p. 28: $u$ is unitary and $\varphi(u^k)=0$ for every nonzero integer $k$.
The source's finite-order $p$-Haar variant is not required for the current Claims and is not separately registered.

<a id="semicircular"></a>
## Semicircular Element

Definition 2.16 and Remark 2.17(2), printed p. 29 / PDF p. 46: a selfadjoint element is semicircular of radius $r>0$ when its law has density $2(\pi r^2)^{-1}\sqrt{r^2-t^2}$ on $[-r,r]$.
Standard semicircular means radius 2 and variance 1.
Different radii are parameter choices.
Circular/Fock realizations retain their explicit scaling in the consuming model.

## Free Cumulants

Definition 11.3, printed p. 175 / PDF p. 192, defines $\kappa_\pi=\sum_{\sigma\leq\pi}\varphi_\sigma\mu(\sigma,\pi)$ on the lattice of noncrossing partitions and $\kappa_n=\kappa_{1_n}$, with arguments distributed in block order.
The usual moment-cumulant inversion is an established source identity, not a new project Claim.

<a id="cumulant-additivity-and-formal-inverse-cauchy-interface"></a>
## Cumulant Additivity and the Formal Inverse-Cauchy Interface

The direct primary-reading evidence for this interface is retained in [R_F0099, Independence and source-inspection depth](../../reviews/Yin_R_F0099_v1.md#independence-and-source-inspection-depth).
On 2026-09-16 that reviewer read Proposition 12.3 and its short proof, printed pp. 196-197 / PDF pp. 213-214; Theorem 12.5 and the Cauchy-series discussion, printed p. 198 / PDF p. 215; and Notation 12.6 and Theorem 12.7 with its displayed derivation, printed p. 199 / PDF p. 216, in the same supplied 434-page publisher edition.
The formulas below retain that inspected interface; no new primary-source reading or review is claimed.

For a variable \(a\) in a noncommutative probability space, write \(m_n(a)=\varphi(a^n)\) and \(\kappa_n(a)=\kappa_n(a,\ldots,a)\).
Proposition 12.3 gives, for freely independent \(a,b\),

\[
\kappa_n(a+b)=\kappa_n(a)+\kappa_n(b)\qquad(n\geq1).
\]

With the formal power-series conventions

\[
M_a(t)=1+\sum_{n\geq1}m_n(a)t^n,\qquad
C_a(t)=1+\sum_{n\geq1}\kappa_n(a)t^n,
\]

Theorem 12.5 states \(M_a(t)=C_a(tM_a(t))\).
Set

\[
R_a(w)=\sum_{n\geq1}\kappa_n(a)w^{n-1},\qquad
G_a(z)=z^{-1}M_a(z^{-1}).
\]

Notation 12.6 and Theorem 12.7 give the formal compositional inverse identities

\[
K_a(w)=w^{-1}+R_a(w),\qquad
G_a(K_a(w))=w,\qquad K_a(G_a(z))=z.
\]

Consequently \(R_{a+b}=R_a+R_b\) for freely independent \(a,b\), and the same additivity holds for a finite free sum.
For a selfadjoint variable with law \(\mu\), the Cauchy-transform sign convention is \(G_\mu(z)=\int(z-t)^{-1}\,d\mu(t)\).

These established source identities are accepted at their formal scope for [C_F0115](../../../claims/Yin_C_F0115_v1.md#free-square-zero-sum-hermitization), whose Section 2 verifies the required scalar freeness of its bounded selfadjoint hermitized summands.
Their use as convergent analytic germs for compactly supported laws and the continuation to the actual upper-half-plane Cauchy transform are local reasoning in [C_F0115, Section 3](../../../claims/Yin_C_F0115_v1.md#3-from-a-local-inverse-series-to-the-actual-upper-half-plane-branch), checked separately in [R_F0099, Complete argument checks, items 4-5](../../reviews/Yin_R_F0099_v1.md#complete-argument-checks).
They are not additional global analytic conclusions asserted by these formal source identities.
As recorded in R_F0099, the general combinatorial foundations, including vanishing mixed free cumulants and the earlier moment-cumulant theory, remain accepted established inputs rather than newly audited proofs.
The corroborating reading of Proposition 16.8, printed p. 263 / PDF p. 280, is not an additional necessary input to this interface.

<a id="r-diagonal"></a>
## R-Diagonal Element

Notation 15.2 and Definition 15.3, printed pp. 240-241 / PDF pp. 257-258: all star-cumulants vanish except those of even length alternating between $a$ and $a^*$.
Odd-length sequences are explicitly declared nonalternating.
The two determining sequences are $\kappa_{2n}(a,a^*,\ldots,a,a^*)$ and $\kappa_{2n}(a^*,a,\ldots,a^*,a)$; in the tracial case they coincide.
This definition does not make $a$ normal.
The Haar-product and injective polar results remain the accepted results in NS06-U001; their proofs are not reconstructed here.

## Citation and Use Boundary

The definition passages above are `standard` / `current formulation` citation candidates.
No historical-priority claim is made.
Consumers and exact proof scopes are linked through the [definition-use record](../../../ledger/Yin_L_F0004_v1.md); those are new documentation links for preserved arguments, not assertions that the old proofs cited these pages originally.

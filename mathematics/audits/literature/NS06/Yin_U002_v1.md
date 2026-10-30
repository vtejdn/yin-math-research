---
author: Yin
---

# NS06-U002: Probability definitions

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Registered supplied 434-page publisher-layout NS06.pdf; printed pages equal PDF pages minus 17. No source bytes or artifact facts changed. |
| source-locator | Definitions 1.1/1.3/1.12,2.16,5.3,11.3,15.3 at the exact printed/PDF locators retained below. |
| inspection | 2026-09-10 selected definitions with the disclosed page-boundary extraction and one visual page. No whole-book or new source-proof audit. |

<a id="ns06-u002"></a>
<a id="ns06-definition-recheck"></a>
## Original selected probability definitions

Date and reviewer: 2026-09-10, the coordinating agent.
Source: [NS06](../../../literature/pdf/NS06.pdf), the supplied 434-page publisher-layout edition in the sole registry (private lookup: `../../../literature/registry.md#ns06-intake`).
This selected definition review supplements the earlier [NS06-U001](Yin_U001_v1.md#ns06-u001) polar/product interface; it does not enlarge that earlier proof inspection or constitute a whole-book audit.
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

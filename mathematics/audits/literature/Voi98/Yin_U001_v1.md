---
author: Yin
---

<a id="voi98-u001"></a>
# Voi98-U001: Setting, Normalization and Historical Scope

- Source: [Voi98](../../../literature/pdf/Voi98.pdf), registered 39-page published version, Sections 0-2 and opening of Section 3, printed pp. 189-193; notation comparisons on pp. 196, 213-214, 222-223, and note added in proof on p. 227.
  Printed page = PDF page + 188.
- Record: 2026-09-08, the coordinating agent, for [Voi98 finite-Fisher source audit](readme.md#voi98-finite-fisher-source-audit).
- Kind and depth: foundational conventions, normalization check and historical claims.
  Definitions and elementary comparisons reconstructed; original microstates and general classical analytic constructions were not audited in this unit.

## Ambient objects and independence

Use a finite von Neumann algebra $M$ with faithful normal tracial state $\tau$, $\tau(1)=1$, and a unital star-subalgebra $B\subseteq M$.
Variables $X_j=X_j^*\in M$ are bounded and their number $n$ is finite and positive.
Write $B[X_1,\ldots,X_n]$ for the evaluated algebra and $N=W^*(B,X_1,\ldots,X_n)$.
The relevant polynomial vectors are dense in $L^2(N,\tau)$; they need not be dense in the larger $L^2(M,\tau)$.

The Hilbert-space convention is linear in the first argument, $\langle a,b\rangle=\tau(b^*a)$.
For $1\leq p<\infty$, $\|a\|_p=\tau(|a|^p)^{1/p}$; the printed p. 193 shorthand lacks the $p$th root if interpreted as a norm.
Square-integrable vectors are canonically affiliated operators in the finite tracial model, with their multiplication and domains stated where used.
This does not make every such vector bounded.

Free independence means that alternating products of centered elements from consecutive distinct algebras have zero trace.
It is not classical independence or commutativity.
A standard $(0,1)$-semicircular variable has mean zero, variance one, norm two, and density

$$p_S(x)=\frac{1}{2\pi}\sqrt{4-x^2}\,1_{[-2,2]}(x).$$

When an auxiliary semicircular family is adjoined, use a tracial free-product extension; it is free from the entire specified original algebra.
Distributional statements are unchanged by that extension.
The source's later Fock model $s(h)=(l(h)+l(h)^*)/2$ instead has variance $\|h\|^2/4$: a unit vector there does not give the variance-one normalization without rescaling.
U005 checks the corresponding dual-system signs.

## Formal derivatives versus evaluated operators

The formal algebra $B\langle t\rangle$ has the derivation $\partial t=1\otimes1$, $\partial b=0$ and outer bimodule actions

$$a\cdot(u\otimes v)\cdot b=au\otimes vb.$$

To regard it as a derivation on the evaluated $B[X]$, the source assumes $X$ and $B$ are algebraically free.
For several variables the analogous assumption concerns all formal relations with coefficients in $B$.
It is stronger than merely asking each $X_j$ to have an infinite scalar spectrum.
The difference quotient may always be computed on a formal expression; its descent to an evaluated algebra must be justified before operator adjoints or closures are used.
U002 and U007 state how this matters for conjugate relations and limits.

The opposite-algebra version $\widetilde\partial$ has the same underlying vector values but multiplies its second factor oppositely.
The action $(u\otimes v)\#a=uav$ accounts for this convention.
One must not change the product while retaining unconverted chain rules.
The unscaled iterates are $\partial^{(1)}=\partial$ and $\partial^{(k+1)}=(\partial\otimes\mathrm{id}^{\otimes k})\partial^{(k)}$; there is no factorial.
Higher derivative formulas in U002 and U004 use this exact convention.

## The two entropy constructions and the scalar constants

The paper keeps $\chi,\Phi$ for its earlier microstates-based/scalar quantities and introduces $\chi^*,\Phi^*$ for the new conjugate-variable construction.
Its relative colon $\chi^*(X:B)$ is defined using relative difference quotients; it must not be identified with microstates entropy 'in the presence of' $B$.
These are distinct definitions even though Proposition 7.6 states equality of the scalar, unconditioned entropies using earlier analytic inputs; U008 records the exact proof-inspection boundary.

Section 2 defines its historical scalar quantity by

$$\Phi_{\mathrm{old}}(X)=\lim_{t\downarrow0}\frac{\chi(X+\sqrt tS)-\chi(X)}{t}.$$

The new quantity is $\Phi^*(X)=\|J(X)\|_2^2$.
With variance-one semicircles and the heat derivative convention of Section 7, the first quantity is **one half** of the second wherever this derivative exists as stated.
Already for $X=S$, the new information is one, while $\chi(\sqrt{1+t}S)-\chi(S)=\tfrac12\log(1+t)$ gives the old derivative $1/2$.
The source's informal language that the one-variable definitions coincide cannot erase this normalization difference.

For precision let $H$ denote the normalized Hilbert transform

$$Hp(x)=\pi^{-1}\operatorname{p.v.}\int\frac{p(y)}{x-y}\,dy.$$

Proposition 3.5 says $J(X)=2\pi Hp(X)$, with the regularized $L^3(dx)$ limit and $L^2(p\,dx)$ membership justified in U002.
Thus the new information is $4\pi^2\int(Hp)^2p\,dx$, and its half is $2\pi^2\int(Hp)^2p\,dx$.
If the unnormalized transform is used instead, that half is $2\int(H_{\rm unnorm}p)^2p\,dx$.
This resolves the ambiguity in Section 2's notation for $H$ without silently changing the time parameter.

The p. 192 cubic-density display $\Phi(X)=\tfrac23\int p^3$ is inconsistent with its stated heat-derivative normalization.
For the standard semicircular density,

$$\int p_S^3\,dx=\frac{3}{4\pi^2},\qquad J(S)=S.$$

Its printed right side is $1/(2\pi^2)$, not the required $1/2$.
With the usual normalized Hilbert-transform cubic identity, the consistent old/new coefficients are $2\pi^2/3$ and $4\pi^2/3$, respectively.
The elementary semicircular countercheck alone establishes the discrepancy; this unit does not pretend to have audited the original general singular-integral identity in Part I.
The definitions and later proofs of $\Phi^*$ use $J$ directly and do not depend on the defective introductory display.

## Verification and historical limits

The coordinating agent read the introduction, notation, scalar motivation and reference list and visually inspected the decisive normalization formulas.
The author's [publication list](https://math.berkeley.edu/~dvv/Publications.pdf), item 43, and the [publisher record](https://link.springer.com/article/10.1007/s002220050222) confirm the article identity.
The note added in proof concerns a then-new microstates additivity result with a modified definition; it is not a theorem identifying $\chi$ and $\chi^*$ for arbitrary tuples.

The introduction's open questions, applications to factors and historical priority reports were inspected as context.
This audit does not assert that their 1998 status remains current.
The local algebraic, operator and entropy units are the reusable proof records; no new theorem-discovery claim is assigned here.
On 2026-09-08, the separate external-input reviewer read this full unit, visually checked source PDF pp. 2-4 and the relevant Section 7 displays, and independently recomputed the semicircle cubic integral, old/new factor and Fock variance.
No gap was found within the stated normalization and historical scope.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Voi98, the retained 39-page published journal article, printed pp. 189-227; printed page = PDF page + 188. Other works retain their separate exact versions and inspection limits in the body. |
| source-locator | Sections 0-2 and opening of Section 3, printed pp. 189-193; notation comparisons on pp. 196, 213-214, 222-223, and note added in proof on p. 227. |
| inspection | 2026-09-08: definitions, normalization and elementary comparisons reconstructed, with separate review of the semicircle constants and historical scope. Original microstates and general classical analytic constructions were not audited in this unit; the 1998 contextual questions are not asserted to remain current. |

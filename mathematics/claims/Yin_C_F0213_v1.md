---
author: Yin
---
# Vacuum norms and bounded duals for a Jordan block with free circular noise

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(k\ge2\), let \(J=\sum_{a=1}^{k-1}e_{a,a+1}\) in \(B=M_k(\mathbb C)\) with normalized trace, and take a free standard circular element \(c\) in the tracial free product \(B*W^*(c)\).
For \(\varepsilon>0\) set \(Z=J+\varepsilon c\), \(N=W^*(Z)\), \(H=L^2(N,\tau)\), \(\Omega=1\), and \(G=H\otimes_2H\) with outer actions.
Write \(x,y\) for the formal letters evaluated at \(Z,Z^*\), and \(d_x,d_y\) for their evaluated outer word cuts.
Use inner products linear in the second argument and \(\beta(Z)=\inf\|E:N\to H\|\) subject to \([E,L_Z]=P_\Omega\) on \(N\) with \(E1\) unrestricted.

1. The represented star algebra is free on \(x,y\).
   Both cuts are closable operators from its Hilbert-dense polynomial core to \(G\) and have actual adjoint vacua.
   In particular \(d_x\) witnesses actual ACSY with zero starred value and vacuum \(\xi_0=d_x^*(1\otimes1)\) of norm at most \(\varepsilon^{-1}\).
2. Put \(\zeta=Z/\|Z\|_2^2\) and \(H_{\mathrm{hol}}=\overline{\mathbb C[Z]}^{\,H}\).
   Every actual ACSY vacuum has holomorphic projection \(\zeta\), of norm \(((k-1)/k+\varepsilon^2)^{-1/2}\).
   For every fixed word degree \(n\ge1\) one can choose a starred value \(K_n\in G\) so the resulting derivation with value \(1\otimes1\) at \(Z\) has vacuum pairing represented by \(\zeta\) on **every** word of degree at most \(n\).
   For \(n\ge2k-1\) any such \(K_n\) has norm at least \(c_k/\varepsilon\) for all sufficiently small \(\varepsilon\), with \(c_k>0\) independent of \(n,\varepsilon\).
3. The bounded-dual cost satisfies
   \[
      \beta(Z)\le\varepsilon^{-1},\qquad
      \liminf_{\varepsilon\downarrow0}\varepsilon\beta(Z)
             \ge\frac{1}{4k^{3/2}} .
   \]
4. Write \(T=\overline{d_y}\) on the represented polynomial core and \(d_k(\varepsilon)\) for the infimum of the vacuum norm over actual ACSY witnesses, with no uniform bound imposed on their starred values.
   Then
   \[
          d_k(\varepsilon)=\|P_{\ker T}\xi_0\|_2,\qquad
          H_{\mathrm{hol}}\subseteq\ker T .
   \]
   For \(k=2\), a sequence drawn from this model with \(\varepsilon\downarrow0\) can have \(\beta(Z)/\|\xi\|_2\to\infty\) for actual vacua \(\xi\) precisely when
   \[
            \liminf_{\varepsilon\downarrow0}
                  \varepsilon\|P_{\ker\overline{d_y}}\xi_0\|_2=0 .       \tag{1}
   \]
   Condition (1) would produce a two-generator counterexample to the universal implication from actual ACSY to bare full-domain duals by the [one-generator ratio criterion](Yin_C_F0210_v1.md#statement).
   Its validity for these \(k=2\) laws remains open here.

## Argument

### Compression of the circular right deletion

On the circular factor use the [circular Fock model and its right deletion](Yin_C_F0074_v1.md#argument).
In orthonormal complex creation letters \(u,v\) one has \(c=\ell(u)+\ell(v)^*\), \(c^*=\ell(v)+\ell(u)^*\), \(\|c\|\le2\), and the norm-one right deletion \(R=r(u)^*\) satisfies \(R\Omega=0\), \([R,L_c]=P_\Omega\), \([R,L_{c^*}]=0\).
In the [pointed free-product representation](../audits/literature/Voi98/Yin_U005.md#voi98-u005) take its right-factor lift \(\widetilde R\), acting on the last circular Hilbert factor with the prefix ending in the matrix factor or empty.
It commutes with the left matrix action.
The same-factor commutators vanish on all reduced-word summands containing a matrix syllable, where the left and right ends act separately.
On the circular factor Hilbert space the commutators are the two intrinsic commutators above, so their global values are \(P_\Omega,0\).
Let \(Q:L^2(B*W^*(c))\to H\) be the tracial subalgebra projection.
It fixes the vacuum and commutes with \(L_Z,L_{Z^*}\).
Hence \(E_0=\varepsilon^{-1}Q\widetilde R|_H\) has norm at most \(\varepsilon^{-1}\), kills the vacuum and satisfies
\[
         [E_0,L_Z]=P_\Omega,\qquad [E_0,L_{Z^*}]=0 .
\]
Restriction to \(N\subset H\) gives the upper bound for \(\beta\).

For each represented polynomial \(p\), \([E_0,L_p]\) is a finite sum of terms \(L_a P_\Omega L_b\).
Identify \(a\otimes b\) with \(h\mapsto a\tau(bh)\), an isometry from the coarse tensor to the Hilbert--Schmidt space.
The commutator corresponds to \(d_xp\) by the product rule, and its scalar vacuum pairing is \(\langle E_0^*\Omega,p\rangle\).
This proves the asserted actual vacuum \(\xi_0\) on the whole core.
Taking adjoints gives the bounded operator \(U=-E_0^*\) with \([U,L_{Z^*}]=P_\Omega\), \([U,L_Z]=0\).
The same construction represents \(d_y\), with vacuum \(U^*\Omega-(U\Omega)^*\), since \(\tau(p\,U\Omega)=\langle (U\Omega)^*,p\rangle\).
For either cut \(\delta\), the vacuum in the adjoint domain implies that every core tensor \(a^*\otimes b^*\) belongs to that domain.
Indeed the scalar pairing of \(a(\delta p)b\) is the adjoint vacuum pairing on \(apb\) minus those of \((\delta a)pb\) and \(ap(\delta b)\).
The latter two are bounded in absolute value by \(\|\delta a\|_2\|b\|_\infty\|p\|_2\) and \(\|\delta b\|_2\|a\|_\infty\|p\|_2\) by moving the outer multipliers onto the vacuum tensor.
These tensors span a dense subspace of \(G\), giving closability.

### Algebraic kernel and finite word tests

Grade the pointed free-product Hilbert space by total circular Fock degree, adding the tensor lengths inside all circular syllables and giving each matrix syllable degree zero.
Left matrix multiplication preserves the span of degrees at most \(j\) and left multiplication by \(c\) or \(c^*\) raises that bound by at most one, by the reduced-word action and the circular creation-deletion formulas.
For a word of length \(m\) in \(Z,Z^*\), its degree-\(m\) projection comes entirely from taking all \(m\) noise terms and all \(m\) creations.
It is \(\varepsilon^m\) times the tensor word in \(u,v\) of the same pattern in the circular factor.
Distinct words of length \(m\) give orthogonal tensors, and every shorter word has zero projection there.
Applying this to the highest nonzero homogeneous part proves algebraic injectivity on the whole polynomial space.
It also implies injectivity of evaluation on the algebraic tensor product of two polynomial spaces.
In \(d_yp\) the coefficient at a given word pair \(a\otimes b\) is precisely the coefficient of \(ayb\) in \(p\).
Consequently the polynomial kernel consists exactly of \(\mathbb C[x]\).

Conjugation by a diagonal phase unitary sends \(J\) to \(e^{it}J\), and the circular rotations send \(c\) to \(e^{it}c\).
They induce a joint trace-preserving rotation of \(Z\) by freeness.
Hence \(\tau(Z^m)=0\) for \(m\ge1\) and different analytic powers are orthogonal.
Freeness and centering give \(\|Z\|_2^2=(k-1)/k+\varepsilon^2\).
The functional \(\ell(p)=(\tau\otimes\tau)d_xp\) takes value one at \(x\) and zero at every other analytic monomial, including \(1\).
Every actual witness agrees with this functional on analytic words by the generator equation, which gives the stated holomorphic projection by density.

For arbitrary \(K\in G\), use the derivation \(\delta_K\) on the free represented algebra with \(\delta_K Z=1\otimes1\), \(\delta_K Z^*=K\).
The [word-cut insertion identity](Yin_C_F0201_v1.md#argument), with \(K^\sharp\) the componentwise adjoint antiunitary, gives
\[
        \langle1\otimes1,\delta_Kp\rangle
              =\ell(p)+\langle K^\sharp,d_yp\rangle .                  \tag{2}
\]
On words through degree \(n\) the difference \(\langle\zeta,p\rangle-\ell(p)\) vanishes on the kernel of \(d_y\).
It therefore induces a functional on a finite-dimensional image in \(G\).
Riesz representation and surjectivity of \(\sharp\) yield \(K_n\) giving (2) with left side \(\langle\zeta,p\rangle\) at that degree.
There is no uniform-in-degree estimate from this argument.

To measure the starred value forced by these tests, take \(r=y^{k-1}x^k\).
At \((J,J^*)\) it vanishes, and each \(y\)-cut has a right factor ending in \(J^k=0\).
Thus \(\|r(Z)\|_2+\|d_yr(Z)\|_2=O_k(\varepsilon)\) by polynomial expansion for \(0<\varepsilon\le1\).
At \(\varepsilon=0\) only the final \(x\)-cut contributes to \(\ell(r)\), with value \(\tau((J^*)^{k-1}J^{k-1})=1/k\).
By continuity \(\ell(r)=1/k+O_k(\varepsilon)\).
Equation (2) then forces \(\|K_n\|_2\ge c_k/\varepsilon\) when the vacuum pairing is \(\zeta\) through degree \(2k-1\), since \(\|\zeta\|_2\le\sqrt2\).
For a general actual pair this test bounds \(\|\xi\|_2+\|K\|_2\) from below on the same scale.

### The near-nilpotent bounded-dual test

For any bounded admissible \(E:N\to H\), applying its commutator recursively to analytic powers and using their zero traces gives
\[
                   E(Z^k)=Z^k E1+ Z^{k-1}.
\]
Hence \(2\|E\|\|Z^k\|_\infty\ge\|Z^{k-1}\|_2\), allowing an arbitrary \(E1\).
In operator norm,
\[
       Z^k=\varepsilon\sum_{j=0}^{k-1}J^jcJ^{k-1-j}
                     +O_k(\varepsilon^2)
\]
because \(J^k=0\), and the coefficient has norm at most \(2k\).
Also \(Z^{k-1}\to J^{k-1}=e_{1k}\), of Hilbert norm \(1/\sqrt{k}\).
Taking the infimum over \(E\) and the lower limit proves the stated estimate.

### Closed kernel and the unrestricted vacuum infimum

All actual witnesses arise from (2), since a derivation on this core is determined by its two letter values.
As \(\ell(p)=\langle\xi_0,p\rangle\), the full-core pairing in (2) has a Hilbert representative exactly when \(K^\sharp\in\operatorname{Dom}T^*\).
In that case the representative is \(\xi_0+T^*K^\sharp\).
The attainable vacua thus form the affine space \(\xi_0+\operatorname{Ran}T^*\).
Taking distance to zero and using \((\operatorname{Ran}T^*)^\perp=\ker T\) proves the projection formula, including when the infimum is not attained.
Closedness of the graph and the algebraic kernel show \(H_{\mathrm{hol}}\subseteq\ker T\).
Finite-degree solvability with increasing \(K_n\) does not identify this closed kernel.

If (1) holds, choose a sequence realizing it and actual vacua within one of the respective infima.
The lower bound on \(\varepsilon\beta(Z)\) yields \(\beta(Z)/\|\xi\|_2\to\infty\).
Conversely a divergent ratio on such a sequence gives \(\varepsilon d_2(\varepsilon)\le\varepsilon\|\xi\|_2\to0\) by the upper bound on \(\varepsilon\beta(Z)\).
The [cutoff-free ratio criterion](Yin_C_F0210_v1.md#statement) now proves the conditional consequence.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T13:59 |
| status | open |
| reason | The actual noise witnesses, finite-degree flexibility, bounded-dual divergence rate and exact remaining projection condition are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Noisy Jordan laws, actual and finite-degree vacuum pairings, bounded-dual cost and conditional separation. |
| argument | [Argument](#argument) | Right deletion, compression, free polynomial core, finite tests, near-nilpotent recursion and the closed-kernel distance. |
| dependency | [Circular Fock construction](Yin_C_F0074_v1.md#argument) | Standard circular creation and right-deletion model, normalization and the two intrinsic commutators. |
| dependency | [Free-product end actions](../audits/literature/Voi98/Yin_U005.md#voi98-u005) | Reduced-word realization and opposite-end lifts in the tracial free product. |
| dependency | [Starred-value word cuts](Yin_C_F0201_v1.md#argument) | Outer tensor pairing for a freely chosen starred value on the represented core. |
| dependency | [One-generator ratio criterion](Yin_C_F0210_v1.md#statement) | An unbounded bounded-dual to actual-vacuum norm ratio yields a two-coordinate counterexample. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T14:05 |
| status | proved |
| reason | Adopt the noisy Jordan estimates, including the necessary and sufficient remaining projection condition for the proposed separation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Noisy Jordan laws, actual and finite-degree vacuum pairings, bounded-dual cost and conditional separation. |
| argument | [Argument](#argument) | Right deletion, compression, free polynomial core, finite tests, near-nilpotent recursion and the closed-kernel distance. |
| dependency | [Circular Fock construction](Yin_C_F0074_v1.md#argument) | Standard circular creation and right-deletion model, normalization and the two intrinsic commutators. |
| dependency | [Free-product end actions](../audits/literature/Voi98/Yin_U005.md#voi98-u005) | Reduced-word realization and opposite-end lifts in the tracial free product. |
| dependency | [Starred-value word cuts](Yin_C_F0201_v1.md#argument) | Outer tensor pairing for a freely chosen starred value on the represented core. |
| dependency | [One-generator ratio criterion](Yin_C_F0210_v1.md#statement) | An unbounded bounded-dual to actual-vacuum norm ratio yields a two-coordinate counterexample. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0221_v1.md#whole-proof-finding) | Right lift and commutators, actual closed cuts, finite-degree flexibility, bounded-dual cost and the kernel criterion. |

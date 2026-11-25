---
author: Yin
---

# The polynomial degree needed to recover a rational element from its jets

## Statement

Let \(G\) be a finitely generated discrete group, \(A=\mathbb CG\), and \(U=L^0(\mathcal N(G))\), with the group trace normalized by \(\tau(1)=1\).
Write \(D_G\) and \(R_G\) for the division closure and the \(*\)-regular closure of \(A\) in \(U\).
For a central variable \(z\), let \(P=U[[z]]\) and \(S=\operatorname{Div}_{U((z))}(A[z])\).
Fix a finite set \(F\subset G\) containing the identity and an integer \(n\ge1\).
Consider realizations
\[
 f(z)=\alpha L(z)^{-1}\beta,\qquad
 L(z)=\sum_{j=0}^d L_jz^j,\qquad
 L_j\in M_n(\operatorname{span}_{\mathbb C}F),
 \tag{1}
\]
where \(L(z)\) is invertible over \(U((z))\) and the row \(\alpha\) and column \(\beta\) are complex.
Such realizations belong to \(S\) by [formal scalar inversion](Yin_C_A0143_v1.md#formal-inversion-by-scalar-pivots).

There is a constant \(C(G,F,n)>0\), independent of \(d\), all scalar coefficients and the pole order of \(L^{-1}\), with the following property.
For positive integers \(N>C(G,F,n)d\), every realization (1) satisfies
\[
\begin{aligned}
 f\in z^NP &\ \Longrightarrow\ f=0,\\
 f-u\in z^NP,\quad u\in U &\ \Longrightarrow\ f=u\text{ as a constant series and }u\in D_G,\\
 f\in P,\quad f^2-f\in z^NP &\ \Longrightarrow\ f^2=f .
\end{aligned}                                                    \tag{2}
\]

In particular, every \(u\in R_G\) has some fixed \(F,n\) for which, at each order \(N\ge1\), a realization \(f_N\) satisfies \(f_N-u\in z^NP\) with degree \(d_N\le N\).
For \(u\in U\), membership in \(D_G\) is equivalent to the existence of fixed \(F,n\) and such realizations along some sequence \(N\to\infty\) with \(d_N/N\to0\).
If \(u\in R_G\setminus D_G\), every realization of an \(N\)-jet at any fixed \(F,n\) must therefore have \(d_N\ge N/C(G,F,n)\).
The upper and lower bounds apply together at a choice of \(F,n\) supporting the construction of degree at most \(N\).

For \(x\in D_G\) and \(p=p_{\ker x}\), the sublinear degree criterion for \(p\in D_G\) also holds with the weaker jet requirements
\[
                   f_N\in P,\qquad f_N(0)=p,\qquad f_N^2-f_N\in z^NP .
\]
Consequently complete deletion of the local condition in the [finite-rank equation](../tasks/Yin_T_A0003_v3.md#contract) for a fixed finitely generated torsion-free group is equivalent to this sublinear bound for every \(x\in D_G\).
Whether all these kernel projections admit sublinear degree remains open.

## Argument

### A rank gap before adjoining the variable

Write \(\operatorname{rk}_G\) for affiliated rank with the unnormalized matrix trace.
For an ordinary square matrix \(H\in M_n(\operatorname{span}_{\mathbb C}F)\), a complex row \(a\) and a complex column \(b\), form
\[
                            T=\begin{pmatrix} H&-b\\ a&0\end{pmatrix}.
\]
The coefficients of \(H,a,b\) are coordinates on one complex affine space.
For each \(m\ge1\), the set of coordinates where \(\operatorname{rk}_G T\le n+1/m\) is [Zariski closed](Yin_C_A0128_v1.md#statement).
This descending chain of closed sets stabilizes at some \(m_0\), where its intersection is the locus \(\operatorname{rk}_G T\le n\).
When \(H\) is an affiliated unit, block elimination gives \(\operatorname{rk}_G T=n+\operatorname{rk}_G(aH^{-1}b)\).
Hence there is a number \(\delta_n=\delta(G,F,n)>0\), for instance \(1/m_0\), such that
\[
                   aH^{-1}b\ne0\quad\Longrightarrow\quad
                   \operatorname{rk}_G(aH^{-1}b)\ge\delta_n.           \tag{3}
\]
In particular, distinct scalar values of two such rational expressions are separated by at least \(\delta_{2n}\) in rank distance, by using the direct sum of their pivots to represent the difference.

### The degree estimate

For \(f\) in (1), set \(J=G\times\mathbb Z\), write \(Z\) for the generator of the central factor, and put
\[
                    B(z)=\begin{pmatrix}L(z)&-\beta\\\alpha&0\end{pmatrix}.
\]
The [truncated matrix estimate](Yin_C_A0149_v1.md#vanishing-order-and-the-rank-of-a-bordered-matrix) gives, for each \(N\ge1\) with \(f\in z^NP\),
\[
                      n\le \operatorname{rk}_J B(Z)\le n+\frac{2nd}{N}. \tag{4}
\]
The estimate compares multiplication modulo \(z^N\) with cyclic evaluation and permits arbitrary polynomial degree and any finite pole order for \(L^{-1}\).

By the [Laurent evaluation theorem](Yin_C_A0143_v1.md#statement), \(L(Z)\) is an affiliated unit and \(S\to D_J\), \(z\mapsto Z\), is injective.
Thus \(f\ne0\) implies \(\operatorname{rk}_J B(Z)>n\) by the Schur complement.
Choose a complex number \(s\) where both \(L(s)\) and \(B(s)\) have maximal rank.
Each polynomial matrix has this rank off a countable set, and its rank at \(Z\) is the same maximum by integration on the unit circle. [Generic polynomial ranks](Yin_C_A0149_v1.md#rank-over-a-finite-interval-of-powers)
In particular \(L(s)\) is an affiliated unit and
\[
        \operatorname{rk}_J B(Z)-n
        =\operatorname{rk}_G\big(\alpha L(s)^{-1}\beta\big)\ge\delta_n
        \qquad(f\ne0).
\]
Here every entry of \(L(s)\) still belongs to \(\operatorname{span}_{\mathbb C}F\), however many powers of \(z\) occur in \(L(z)\).
Together with (4), this proves \(N\le 2nd/\delta_n\) for a nonzero realization of order at least \(N\).

If \(f-u\in z^NP\), the difference \(f(z)-f(2z)\) lies in \(z^NP\).
It has a realization of size \(2n\), support \(F\) and degree at most \(d\), using the diagonal blocks \(L(z),L(2z)\).
The same bounds apply to \(f^2-f\), whose pivot is \(\left(\begin{smallmatrix}L&-\beta\alpha\\0&L\end{smallmatrix}\right)\), with row \((\alpha,-\alpha)\) and column \(\binom{0}{\beta}\).
Thus one can take
\[
                       C(G,F,n)=\max\{2n/\delta_n,\,4n/\delta_{2n}\}.
\]
In the second implication of (2), \(f(z)=f(2z)\) forces its coefficients in every positive degree to vanish, and \(S\cap U=D_G\) gives \(u\in D_G\). [Descent of constant series](Yin_C_A0141_v1.md#descent-of-a-constant-series)
The zero test for \(f^2-f\) gives the third implication.

### Linear upper bounds and rational recovery

For each \(u\in R_G\) there are a rectangular group-ring matrix \(K\), a complex row \(\epsilon\) and a complex column \(\gamma\) such that
\[
                       g(z)=\epsilon K^*(KK^*+zI)^{-1}\gamma
                       \in S\cap P,\qquad g(0)=u .
\]
The [constant-term construction](Yin_C_A0141_v1.md#realizing-every-element-of-the-regular-closure) proves these assertions and the formal invertibility of the displayed pivot.
Adjoin a first row and column to obtain
\[
                    \begin{pmatrix}1&-\epsilon K^*\\0&KK^*+zI\end{pmatrix}.
\]
Multiplying its inverse by the first coordinate row and the column \(\binom0\gamma\) recovers \(g\).
This is a realization (1) of degree at most one with a fixed finite support and size.
Substitution \(z\mapsto z^N\) is a homomorphism on formal Laurent series and preserves inverses.
Consequently \(g(z^N)-u\in z^NP\), and the substituted realization has degree at most \(N\).

If \(u\in D_G\), its scalar rational expression over \(A\) has a constant realization (1) by [block linearization](Yin_C_A0141_v1.md#recovering-a-laurent-coefficient-from-finitely-many-equations).
It supplies every order with \(d_N=0\).
Conversely, if \(d_N/N\to0\) for fixed \(F,n\), then \(N>C(G,F,n)d_N\) eventually, and (2) gives \(u\in D_G\).

The kernel projection \(p=p_{\ker x}\) belongs to \(R_G\) by [regularity and relative inverses](../audits/literature/JZ19/Yin_U001.md#regular-closure-definitions).
Every full \(N\)-jet at \(p\) has idempotent defect in \(z^NP\) because \(p^2=p\).
Conversely, (2) turns an idempotent jet of sublinear degree with residue \(p\) into an exact idempotent of \(S\cap P\) with that residue.
Applying [idempotent recovery](Yin_C_A0147_v1.md#recovering-the-orthogonal-projection) to \(x^*x\) gives \(p\in D_G\).
The [scalar kernel-projection criterion](Yin_C_A0131_v1.md#which-rationality-is-detected) now gives the equivalence with complete deletion.

## Assessment history

### Decision sublinear-degree

| Field | Value |
| --- | --- |
| date | 2026-11-25T11:38 |
| status | proved |
| reason | A rank gap at one ordinary parameter and a truncation bound control vanishing order linearly in the polynomial degree. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The three degree bounds and the characterization by sublinear degree at fixed support and size. |
| argument | [Argument](#argument) | The rank gap before adjoining the parameter, generic specialization, and the linear upper bound for every regular-closure residue. |
| dependency | [Rank sublevels](Yin_C_A0128_v1.md#statement) | Closedness in the finite space of ordinary pencil coefficients. |
| dependency | [Truncated rank estimate](Yin_C_A0149_v1.md#vanishing-order-and-the-rank-of-a-bordered-matrix) | Vanishing order versus polynomial degree and generic rank. |
| dependency | [Analytic evaluation](Yin_C_A0143_v1.md#statement) | Simultaneous generic ranks and injectivity. |
| dependency | [Residue realization](Yin_C_A0141_v1.md#statement) | Affine Gram realizations of regular-closure residues and descent of constant series. |
| dependency | [Exact idempotent lifting](Yin_C_A0147_v1.md#statement) | Recovery of a scalar kernel projection from an exact lift. |
| dependency | [Original equation](Yin_C_A0131_v1.md#which-rationality-is-detected) | The scalar kernel criterion for complete deletion. |
| review | [Sublinear degree](../audits/reviews/Yin_R_A0171_v1.md#sublinear-degree) | Independent review of the complete statement and proof. |

## Current assessment

[Selected decision](#decision-sublinear-degree)

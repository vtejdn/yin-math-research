---
author: Yin
---

# Deciding closed range and estimating signed shells from a cyclic minor

## Statement

Fix a non-elementary torsion-free word-hyperbolic group \(G\), in particular an individual four-line group satisfying the [geometric criterion](../ledger/Yin_L_A0054_v1.md#the-geometric-input-and-its-application-to-the-planted-laws).
Let \(H=\langle t\rangle\) be a maximal infinite cyclic subgroup.
Take an \(r\)-by-\(m\) matrix \(A\) over \(\mathbb CG\) with \(r\) selected columns giving a square matrix over \(\mathbb CH=\mathbb C[t,t^{-1}]\) with nonzero Laurent determinant.
The remaining columns can have arbitrary support in \(G\).
For a finite row or column translation which produces this form one can apply the conclusions in those coordinates and translate back.

Collect the coefficient columns of \(A\) in the finitely many right cosets \(Hx\) which occur.
Thus \(A_{\bullet j}=\sum_x F_{j,x}(t)x\) with Laurent polynomial columns \(F_{j,x}\); concatenate these columns into a single matrix \(F\).
Then the range of \(A\) is dense, and it is closed **exactly when** \(F(z)\) has row rank \(r\) for every \(|z|=1\).
In every case a Laurent polynomial basis of the column module of \(F\) yields a factorization \(A=D(t)T\) with \(D(t)\) injective of dense range and \(T\) a finite group-ring matrix of full closed row range.
In particular a same-kernel row system can be found from the input even when none is supplied.
All group data in forming \(F\) consist of the coset comparisons and the exponents of \(t\) in the actual coefficient support.

In the nonclosed case let \(d\ge1\) be the maximum multiplicity of a unit-circle zero of an invariant factor of \(D\).
For \(Q=I-A^*A/M\), \(M>\|A\|^2\), the positive spectral mass of \(I-Q\) below \(s\) is comparable to \(s^\alpha\) at zero with \(\alpha=1/(2d)\).
The actual projection has exponentially weighted square-summable coefficients.
For the [finite signed first-return sums on shells](Yin_C_A0076_v1.md#statement), for any \(\beta\ge0,\ \kappa\alpha>\beta\), and \(R=2^J\) sufficiently large, one obtains
\[
 \sum_{|g|\ge R}(1+|g|)^\beta\!
 \sum_{i,j,\zeta}|B_\bullet(g,i,j,\zeta)|^2
       \ \le\ C_{\beta,\kappa}\big(e^{-cR}+R^{-(\kappa\alpha-\beta)}\big).       \tag{1}
\]
Here \(B_\bullet\) is computed on each shell from the original powers of \(Q\) to the polynomial time horizon of C76.
The constants are for one fixed group and matrix.
The criterion also gives \(\dim_G\ker A=m-r\), since the range is dense.

## Spectral packets along a maximal cyclic subgroup

For \(g\notin H\) the pairs of boundary fixed points of \(t\) and \(gtg^{-1}\) are disjoint, and both elements act with north–south dynamics.
Indeed an infinite maximal amenable subgroup containing \(H\) exists by taking unions of chains.
It is virtually cyclic, hence infinite cyclic in this torsion-free group, so equals \(H\).
Its boundary pair and the disjointness for translates outside it are given by [Boutonnet and Carderi, Lemma 2.2 and proof, p. 6](../literature/pdf/BC15--arxiv-v2.pdf#page=6).
Choose disjoint neighborhoods for the four endpoints.
All sufficiently large positive and negative powers of each element send the complement of its repelling neighborhood into its attracting neighborhood for that sign.
The ping-pong argument, applied to reduced alternating syllables, gives \(b\ge1\) such that \(s=t^b,\ v=gt^bg^{-1}\) freely generate a group of rank two.

Let \(E_\delta\) be the spectral projection of \(t\) for the union of the chordal \(\delta\)-neighborhoods of a fixed finite set \(\Lambda\) on the unit circle.
We claim \(\|E_\delta g E_\delta\|\to0\) as \(\delta\downarrow0\) for every \(g\notin H\).
For phases \(\lambda,\mu\) average the first \(N\) powers of \(\bar\lambda^b s\) and of \(\bar\mu^b v\), calling the contractions \(U_N,V_N\).
One has \(\|U_N^*V_N\|\le2/\sqrt N\), uniformly in both phases.
To verify it, decompose into right cosets of \(\langle s,v\rangle\).
On one copy of the free group let \(P_s\) project onto words starting with an \(s\)-syllable and define \(P_v\) similarly.
The \(N\) translates by \(s^{-j}\) of the complement of \(P_s\) have disjoint word supports, so \(\|U_N^*(I-P_s)\|=N^{-1/2}\).
Likewise \(\|(I-P_v)V_N\|\le N^{-1/2}\) by taking the adjoint.
Since \(P_s\le I-P_v\), insertion of \(I-P_s\) and \(P_s\) between the averages proves the bound.

A unit vector supported spectrally within \(\delta\) of \(\lambda\) for \(t\) differs from its \(U_N\) average by at most \(b(N+1)\delta/2\), using \(|z^{bj}-\lambda^{bj}|\le bj|z-\lambda|\).
The \(g\)-translate of a packet about \(\mu\) differs by the same bound from its \(V_N\) average.
Consequently the absolute scalar product between the original first packet and the translate of the second is at most \(2/\sqrt N+b(N+1)\delta\).
Split the union of arcs into at most \(|\Lambda|\) disjoint pieces and sum the at most \(|\Lambda|^2\) pair estimates.
Taking first \(N\) large and then \(\delta\) small proves the claim, simultaneously on any specified finite set of \(g\)'s.

## A lower bound from the collected coefficients

First consider a matrix \(T\) still containing a square cyclic minor \(P(t)\) with nonzero determinant, and suppose its collected matrix \(F_T(z)\) has full row rank on the circle.
Coefficient multiplication projected onto \(H\) gives exactly
\[
 E_H(TT^*)=\sum_{j,x} F_{T,j,x}(t)F_{T,j,x}(t)^* \ge b_0 I_r
\]
for some \(b_0>0\) by compactness.
Indeed \(x y^{-1}\in H\) exactly when the cosets \(Hx,Hy\) agree.
Let \(\Lambda\) be the unit-circle zero set of \(\det P\).
If empty, the selected minor already gives a lower bound.
Otherwise use the preceding spectral projections in every row coordinate.
The finitely many terms outside \(H\) in \(TT^*\) have compressions whose norms tend to zero, since their constant coefficient matrices commute with \(E_\delta\).
Thus for sufficiently small \(\delta\), \(E_\delta TT^*E_\delta\ge b_0 E_\delta/2\).
Off those arcs the least singular value of \(P\) is at least \(\sigma_\delta>0\).
For every \(\xi\), commutation of \(P(t)^*\) with \(E_\delta\) gives
\[
 \|(I-E_\delta)\xi\|\le\sigma_\delta^{-1}\|P(t)^*\xi\|
                 \le\sigma_\delta^{-1}\|T^*\xi\|.
\]
The triangle inequality applied to \(T^*E_\delta\xi\) gives
\[
 \|\xi\|\le\big[\sigma_\delta^{-1}
    +(2/b_0)^{1/2}(1+\|T\|\sigma_\delta^{-1})\big]\|T^*\xi\|.
\]
This proves surjectivity and a positive row-Gram bound.

For the original \(F\), choose a Laurent polynomial basis of its column module, free of rank \(r\) over this principal ideal domain because it contains the cyclic minor's columns (use representative \(1\) on \(H\)).
Put the basis columns in \(D\), and write \(F=D F_T\).
The columns of \(F_T\) span the full Laurent module, so \(F_T\) has a Laurent right inverse.
Reassembling each original column gives \(A=D T\).
The selected columns of \(T\) still have cyclic support and nonzero determinant because the original minor does and \(\det D\ne0\).
The preceding lower bound applies to \(T\).
On the cyclic cosets, \(D\) acts by its torus multiplier; since its determinant has only finitely many zeros, \(D\) is injective with dense range.
Thus \(\operatorname{ran} A=\operatorname{ran}D\).
This range is closed exactly when \(D\) is invertible on the circle, equivalent to full circle rank of \(F\).

## Estimating the original shell sums

In the nonclosed case the two Gram bounds for \(TT^*\) compare \(AA^*\) from above and below with positive multiples of \(DD^*\).
Laurent Smith reduction of \(D\) uses boundedly invertible left and right multipliers on the whole circle.
The finite-dimensional singular values at each \(z\) are therefore bounded above and below by the corresponding ordered singular values of its diagonal invariant-factor matrix times positive constants.
Near each unit-circle zero the small absolute values of the diagonal factors are comparable to the respective integer powers of angular distance from that point.
Circle integration, and then trace comparison for sublevels and rectangular polar decomposition, give the stated exponent \(1/(2d)\) for the positive part of \(A^*A/M\). [Spectral comparison for finite traces](Yin_C_A0062_v1.md#a-rational-example-using-the-whole-group)
Integrating the heat multiplier on this measure yields \(\tau_m(Q^n-p)=O(n^{-\alpha})\), hence the dyadic difference assumption in C76.

The finite signed products also give an approximation with linear propagation to \(I-p=T^*(TT^*)^{-1}T\).
Choose \(b_1>\|TT^*\|\); the first \(n\) terms of the geometric series for \((TT^*)^{-1}\) have norm error \(O(\|I-TT^*/b_1\|^n)\) with ratio strictly below one.
Multiplication at the ends by \(T^*,T\) preserves linear propagation and geometric error.
Summing the resulting squared coefficient errors on successive word shells gives \(\sum e^{c'|g|}\|\widehat p(g)\|_{\rm HS}^2<\infty\) for some \(c'>0\).
The signed limiting first means are within a factor four in coefficient norm of the projection off the identity, by [C67](Yin_C_A0067_v1.md#statement).
Apply the C76 shell truncation bound to the original matrix and absorb its geometric tail and the squared truncation error to obtain (1).
This analysis covers inputs with the indicated cyclic minor; no such minor is established for an arbitrary group-ring matrix.

## A two-row example with full row-product support

Choose \(X\) consisting of \(e\) and one representative of each nontrivial double coset \(HxH\) needed for the elements of a fixed finite generating set of \(G\); put \(V=\sum_{x\in X}x\).
Thus \(H\) and \(X\) generate \(G\), and \(X\setminus\{e\}\ne\varnothing\).
Consider the integer input
\[
 A=\begin{pmatrix}
       (1-t)^2&0&1-t\\
       0&(1+t)^2(1-t)&(1+t)^2 V
    \end{pmatrix}.
\]
Its cyclic minor is the first two columns.
Collecting the third column on \(H\) and at any \(Hx\ne H\) gives respectively \((1-t,(1+t)^2)^t\) and \((0,(1+t)^2)^t\).
The generated Laurent module therefore has basis \(D=\operatorname{diag}(1-t,(1+t)^2)\).
After division the two third-column coset vectors are the constant vectors \((1,1)^t,(0,1)^t\); even at \(t=1\), where both cyclic columns of \(T\) vanish, these vectors enforce the lower bound by the packet estimate.
The row range of \(A\) is nonclosed, \(\alpha=1/4\), and (1) holds for \(\kappa>4\beta\).

The \(21\) row product is \((1+t)^2 V(1-t^{-1})\).
On \(H\) its terms are \(t^2+t-1-t^{-1}\).
For each \(x\notin H\) all elements \(t^i x t^j\) occurring in this product are distinct: an equality between different pairs would put a nonidentity power of \(t\) in \(xHx^{-1}\), impossible by the disjoint boundary pairs above.
The different double cosets cannot cancel each other.
Thus the support of this single row-product entry includes \(e,t\) and all \(x\in X\), as does the input entry \((1+t)^2V\).
Left differences inside either entry still generate \(G\) after independent row and column translations.
In particular the separate [free-subgroup row-product test](Yin_C_A0082_v1.md#statement) cannot account for (1) here on a four-line group, since that group is not free.

## Assessment history

### Decision cyclic-minor-shell-estimate

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:46 |
| status | proved |
| reason | Independent review verified the packet norm bound, the Laurent factorization, the closed-range criterion, the signed-shell estimate and the full-support two-row example. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Matrices with a full-row-rank cyclic Laurent minor, including gapless cases whose row products require the full group. |
| argument | [Proof](#spectral-packets-along-a-maximal-cyclic-subgroup) | Free-power compression, coset collection, row lower bound, invariant factors and the quantitative shell conclusion. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0117_v1.md#whole-argument-finding) | Independent review of the argument and its stated scope. |

## Current assessment

[Selected decision](#decision-cyclic-minor-shell-estimate)

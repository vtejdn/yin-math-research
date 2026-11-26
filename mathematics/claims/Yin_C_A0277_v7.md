---
author: Yin
---

# One balanced face and a summable intersection of two free faces

## Statement

Use the three rows
\[
 (1,1,1),\qquad (1,\lambda u,\mu v),\qquad (a,bw,cz)
\]
over a discrete group \(G\), where \(|\lambda|=|\mu|=1\) and \(a,b,c\) are arbitrary nonzero complex numbers.
Let \(A=\langle u,v\rangle\) and \(B=\langle w,z\rangle\) be free on the displayed pairs.
For the [three-edge covering tree](Yin_C_A0277_v2.md#the-row-projection-on-the-three-regular-tree) of \(A\), let \(d_A(x)\) be the distance from \(L_1\) to \(L_x\), twice the six-letter length in \(u,v,u^{-1}v\) and their inverses.
Put
\[
      C=A\cap B,\qquad
      \Xi=\sum_{x\in C\setminus\{1\}}2^{-d_A(x)},\qquad
      \eta=\frac{1}{3\cdot2^{19}}.
\]
If \(\Xi\le\eta\), the regular nullity with unnormalized coordinate trace satisfies
\[
                            \delta\le \tfrac12-2^{-28}.
\]
The hypothesis uses only the distances measured in the balanced face.
It allows intersections with several free generators and puts no bound on the ratios of the three moduli in the other face.

For \(C=\langle x\rangle\) infinite cyclic, \(d_A(x)\ge22\) suffices.
Indeed the [axis calculation](Yin_C_A0277_v6.md#the-trace-on-the-common-cyclic-subgroup) gives \(\Xi=2^{1-d_A(x)}/(1-2^{-\ell_A})\le(8/3)2^{-d_A(x)}\), since \(\ell_A\ge2\).
This conclusion allows arbitrary nonzero moduli in the second face, even if \(x\) is short in that face.

## Bounds using one balanced face

On the constant two-coordinate space \(W=\mathbf1^\perp\), write \(P,Q\) for the two row-kernel projections and \(\overline Q\) for the identity coefficient of \(Q\).
Both projections have trace one and their meet has trace \(\delta\), by the [two-row calculation](Yin_C_A0277_v1.md#the-scalar-coefficient-of-each-row-projection).
Here \(P_1=I_W/2\), whereas every other \(P_x\) on \(A\) is rank one of Hilbert-Schmidt norm \(2^{-d_A(x)}\), by the tree formula.
Every \(Q_y\) has operator norm at most one as a coordinate compression of the projection.
Each nonidentity term in the trace of \(PQ\) comes from \(x\in C\setminus\{1\}\).
The rank-one trace norm of \(P_x\) is its Hilbert-Schmidt norm, hence
\[
                          |\operatorname{Tr}(PQ)-1/2|\le\Xi .
\]

For \(a_0\in A\) of tree distance two, the Fourier coefficient of \([P,Q]\) there is
\[
 [P_{a_0},\overline Q]+\sum_{x\in C\setminus\{1\}}
      (P_{a_0x}Q_{x^{-1}}-Q_x P_{x^{-1}a_0}).
\]
Indeed if \(a_0\) is a product in either order, its \(B\)-factor must lie in \(C\).
The formula follows by the square-summable Fourier convolution, as in the [ordered product calculation](Yin_C_A0277_v6.md#grouping-the-coefficients-of-each-ordered-product).
There is no common element of distance at most twenty in \(A\), other than the identity, because one such term would already contribute at least \(2^{-20}>\eta\).
In particular \(a_0 x\) and \(x^{-1}a_0\) are nonidentity for each indicated \(x\).
Their respective distances are at least \(d_A(x)-2\).
The Hilbert-Schmidt norm of the sum of error terms at \(a_0\) is therefore at most \(8\Xi\).

Put \(s=\|\overline Q-I_W/2\|_{\rm op}\).
Over the six distance-two elements the [rank-one commutator calculation](Yin_C_A0277_v3.md#the-commutator-on-the-six-short-elements) gives
\(\sum_{a_0}\|[P_{a_0},\overline Q]\|_{\rm HS}^2\ge3s^2/4\).
The triangle inequality on the six coefficients and Parseval give
\[
               \|[P,Q]\|_{2,\operatorname{Tr}}
                   \ge \tfrac{\sqrt3}{2}s-8\sqrt6\,\Xi .
\]

## When the second face is near its balanced projection

First suppose \(s\ge1/753\).
The last estimate yields \(\|[P,Q]\|_{2,\operatorname{Tr}}\ge\sqrt3/1506-8\sqrt6\,\eta>1/882\).

For \(s<1/753<1/512\), let \(Q_0\) be the third-row projection obtained by replacing each scalar with its phase.
The [free tree energy bounds](Yin_C_A0277_v3.md#a-uniform-estimate-for-all-third-row-moduli) give \(\|Q-Q_0\|\le26s\).
They compute in the free subgroup \(B\) alone, and regular subgroup inclusion preserves these norms.
Since no nonidentity common element has six-letter length at most ten on the \(A\) side, the two ten-letter balls have trivial intersection.
The [finite short-product comparison](Yin_C_A0281_v1.md#local-uniqueness-in-the-two-products) gives
\(\|[2P-I_W,2Q_0-I_W]\|_{2,\operatorname{Tr}}>1/5\).
For any selfadjoint \(X\), the commutator with \(P\) uses only the two off-diagonal compressions, so \(\|[P,X]\|_{2,\operatorname{Tr}}\le\|X\|_{2,\operatorname{Tr}}\le\sqrt2\|X\|\).
Consequently
\[
              \|[P,Q]\|_{2,\operatorname{Tr}}
                    \ge 1/20-26\sqrt2/753>1/882 .
\]
The last numerical comparisons follow for example from \(\sqrt3>1.732,\ \sqrt6<2.45,\ \sqrt2<1.41422\).
The [projection trace identity](Yin_C_A0277_v2.md#a-discrepancy-on-products-of-two-short-elements) gives
\[
  \delta\le\operatorname{Tr}((PQP)^2)
          =\operatorname{Tr}(PQ)-\tfrac12\|[P,Q]\|_{2,\operatorname{Tr}}^2
          \le\tfrac12+\eta-\frac1{2\cdot882^2}
          <\tfrac12-2^{-28}.
\]

## An intersection with two free generators

A sufficient condition for the bound on \(\Xi\) is \(C\subseteq\langle u^n,v^n\rangle\) with \(n\ge23\).
A freely reduced length-\(k\) word in \(u^n,v^n\) has ordinary free word length \(nk\) in \(u,v\).
It has \(d_A\ge nk\) since each of the six letters has ordinary length at most two and advances at most two tree edges in a shortest expression.
There are \(4\cdot3^{k-1}\) such words, giving
\[
                   \Xi\le\frac{4\cdot2^{-n}}{1-3\cdot2^{-n}}
                      <\eta .
\]

For a concrete marking in the free group on \(p,q\), take \(u=p,\ v=q,\ w=p^n q^n,\ z=p^{2n}q^n\).
Then \(B=\langle p^n,q^n\rangle\subset A\) since \(zw^{-1}=p^n\), giving the full rank-two intersection in this test.
All six face pairs are free.
Indeed their pairs of exponent vectors in \(\mathbb Z^2\) are independent: the first two row pairs are the bases of \(A,B\) on the displayed generators, and the remaining row pair has vectors \((n-1,n),(2n,n-1)\).
The first two column pairs are \(p,w\) and \(q,z\) up to inverses, and the last has vectors \((-1,1),(n,0)\) up to sign.
Independence makes each two-element pair noncommuting in the ambient free group, and a noncommuting pair in a free group freely generates its subgroup.
The ambient free-group integrality also holds in this example.
The estimate above applies in every group satisfying the stated face and intersection hypotheses.

## Assessment history

### Decision one-balanced-free-face

| Field | Value |
| --- | --- |
| date | 2026-11-26T15:54 |
| status | proved |
| reason | The weighted sum in the balanced face controls the nullity for arbitrary moduli in the other face. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The weighted sum in the balanced face controls the nullity for arbitrary moduli in the other face. |
| argument | [Bounds using one balanced face](#bounds-using-one-balanced-face) | Bounds using one balanced face. |
| argument | [When the second face is near its balanced projection](#when-the-second-face-is-near-its-balanced-projection) | When the second face is near its balanced projection. |
| argument | [An intersection with two free generators](#an-intersection-with-two-free-generators) | An intersection with two free generators. |
| review | [One balanced free face](../audits/reviews/Yin_R_A0217_v1.md#one-balanced-free-face) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-one-balanced-free-face)

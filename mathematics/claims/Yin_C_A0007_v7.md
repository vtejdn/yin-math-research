---
author: Yin
---
# Nonpolynomial subordination boundaries for finite cyclic-amalgam pencils

## Statement

Keep the noncentral amalgam \(F(z,a,b)=F(z,a)*_{\langle z\rangle}F(z,b)\) of [the complete-frame calculation](Yin_C_A0007_v6.md#statement).
Write \(A=a-1,\ B=b-1,\ \mathcal B=\mathcal N(\langle z\rangle)\), and let \(e_{22}\) be the middle coordinate projection in three dimensions.
Choose a selfadjoint Laurent polynomial \(h=h(z)\) whose values on the unit circle are strictly positive.
The two finite selfadjoint vertex matrices
\[
 X_a=\begin{pmatrix}A^*hA&A^*&0\\A&0&0\\0&0&0\end{pmatrix},
 \qquad X_b=-\begin{pmatrix}0&0&0\\0&0&B\\0&B^*&B^*hB\end{pmatrix}
\]
have true norm subordination boundaries at zero
\[
 b_a=-h^{-1}e_{22},\qquad b_b=h^{-1}e_{22}.
\]
Both act nontrivially on the complete kernel of \(X_a+X_b\).
The total and shifted marginal nullities are respectively one and two, two, in the unnormalized trace.
For every nonconstant such \(h\), no Laurent polynomial edge matrix equals the boundary action on that kernel.
The boundary belongs to the rational closure of the edge ring with a denominator certified by the circle gap.

## Argument

Let \(R_1\) have rows \((A,1,0)\) and \((0,1,B)\), and \(p_1=P_{\ker R_1}\).
The [degree-three tree calculation](Yin_C_A0007_v6.md#exact-expected-projection-from-the-degree-three-tree) gives \(E_H(p_1)\ge m I\), \(m=(9-\sqrt{33})/24\).
Set \(D=\operatorname{diag}(1,h,1)\) and \(R_h=\operatorname{diag}(h,h)R_1D^{-1}\).
Its rows are \(r_a=(hA,1,0)\) and \(r_b=(0,1,hB)\), in the indicated order even when \(h\) does not commute with \(a,b\).
Direct multiplication gives
\[
 X_a-b_a=r_a^*h^{-1}r_a,\qquad
 X_b-b_b=-r_b^*h^{-1}r_b.
\]
Here these equations initially define two candidates and verify their actions on \(\ker R_h\).
The adjoint \(R_1^*\) is injective by the injectivity of \(A^*,B^*\), and the bounded invertible factors preserve injectivity of \(R_h^*\).
Consequently the kernel of \(R_h^*\operatorname{diag}(h^{-1},-h^{-1})R_h=X_a+X_b\) equals \(\ker R_h=D\ker R_1\).
Let \(p_h\) project onto that closed range.
Polar decomposition of \(Dp_1\) preserves its trace, hence \(\operatorname{Tr}(p_h)=1\), where \(\operatorname{Tr}\) incorporates the group trace.
The inequality \(Dp_1D^*\le\|D\|^2p_h\) and bimodularity give
\[
 E_H(p_h)\ge \|D\|^{-2}D E_H(p_1)D^*
       \ge \gamma I,\qquad \gamma=m/(\|D\|\|D^{-1}\|)^2.
\]
The amplified vertex algebras are free over \(M_3(\mathcal B)\).
The bounded inverse just proved allows application of [BBL21, Theorems 3.2 and 3.5 in arXiv v2](../audits/literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface).
For the genuine boundary \(d_j\), its intersection identity gives \((X_j-d_j)p_h=0\).
The displayed factorizations give \((X_j-b_j)p_h=0\), so \((b_j-d_j)E_H(p_h)=0\) proves equality.
Each row has a constant unit entry and is onto, and positivity of \(h^{-1}\) identifies the kernel of its signed quadratic form with the row kernel.
Each shifted marginal therefore has nullity two.
For any bounded edge matrix \(c\),
\[
 \gamma\|b_j-c\|_2^2\le \|(X_j-c)p_h\|_2^2
 =\operatorname{Tr}((b_j-c)E_H(p_h)(b_j-c)^*)\le\|b_j-c\|_2^2 .
\]
Thus \(X_jp_h\ne0\) and a polynomial representative of that action would coincide with \(b_j\).
The units in \(\mathbb C[z,z^{-1}]\) are scalar monomials, and a strictly positive scalar monomial on the whole circle is constant.
This proves the asserted polynomial obstruction.

For \(h=3+z+z^{-1}\), set \(r=(3-\sqrt5)/2\).
The Laurent coefficients of \(1/h\) are \((-r)^{|k|}/\sqrt5\), as follows by multiplying this absolutely convergent series by \(h\), using \(r+r^{-1}=3\) and \(3-2r=\sqrt5\).
The squared \(L^2\)-distance from \(b_j\) to degree-\(N\) edge matrices (frequencies \(-N,\ldots,N\)) is
\[
 \frac{2r^{2N+2}}{5(1-r^2)}
\]
by Fourier orthogonality for the canonical trace.
The preceding two-sided estimate bounds the optimal squared kernel-action error between \(\gamma\) times this number and the number itself.
Here \(\gamma=m/25\), since \(1\le h\le5\).
This family gives nonzero rational boundaries of finite vertex pencils with known marginal ranks.
Whether finite vertex pencils with full expected kernel can force a boundary outside the edge rational closure remains open in this route.

## Assessment history

### Decision rational-edge-boundaries

| Field | Value |
| --- | --- |
| date | 2026-11-21T03:25 |
| status | proved |
| reason | Independent whole-proof review supports the stated result under its declared hypotheses. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both finite vertex matrices, genuine nonzero rational boundaries, nullities and nonpolynomiality. |
| argument | [Argument](#argument) | Complete bounded kernel transport, subordination, rigidity and quantitative Fourier error. |
| review | [Whole finding](../audits/reviews/Yin_R_A0020_v7.md#whole-finding) | Complete independent review of the fixed statement, proof and direct interfaces. |
| dependency | [Tree expectation](Yin_C_A0007_v6.md#exact-expected-projection-from-the-degree-three-tree) | Initial complete kernel, trace and bounded conditional Gram. |
| dependency | [BBL21](../audits/literature/BBL21/Yin_U001.md#bbl21-u001) | Amplified general-base norm limits and kernel-intersection formula under the verified bounded-inverse hypothesis. |

## Current assessment

[Selected decision](#decision-rational-edge-boundaries)

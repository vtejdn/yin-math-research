---
author: Yin
---
# Three-point curvature bounds linear Wick forms and determines the full Wick operator

Human author: Yin.
The normal-branch agent developed the three-variable positive-semidefinite inequality, its curvature summation and the exact all-degree operator formula.
Root proposed the finite block-weighted semicircular diagnostic to preserve the three-point geometry after the arbitrary-weight obstruction.
These are development contributions, not independent review of this fixed candidate.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let N have mutually orthogonal projections p_1,...,p_n summing to 1, with positive tracial masses m_i, and let S be standard semicircular free from N in a finite tracial free product M.
Assume N is their finite-dimensional abelian span.
Let a=(a_ij) be real symmetric with every entry strictly positive; no positive-semidefinite matrix hypothesis is imposed.
Set

\[
 T=\sum a_{ij}p_iSp_j,\quad R=\sum a_{ij}^{-1}p_iSp_j,
 \qquad\mathcal A=\operatorname{alg}(N,T)=\operatorname{alg}(N,S),
\]

where reciprocals are entrywise.
The represented partial liberation gamma on A is prescribed by gamma(n)=n tensor 1-1 tensor n for n in N and gamma(T)=0.
It has actual bounded vacuum zeta=(i gamma)*1=-i[R,T].
Inner products are linear in the second variable, outer actions are the usual ones, and I_q denotes inner insertion.

Choose distinct complex numbers z_i, let c_uvw be their Menger curvature, with value zero for repeated indices, and put g_uv=sum_w m_w c_uvw squared.
Define the bounded vector xi by

\[
 p_u\xi p_v=\frac{i\,p_u\zeta p_v}{\bar z_u-\bar z_v}\ (u\ne v),
 \qquad p_u\xi p_u=0.
\]

Then zeta=-i[Z*,xi], Z=sum_i z_i p_i.
For every first-relative-Wick vector V=sum_(i,j) b_ij p_i S p_j, with arbitrary complex b, the actual core contraction C_g=(id tensor tau)I_g gamma obeys

\[
 \operatorname{Re}\langle V,C_gV\rangle
 \ge-\|V\|_\infty^2\|\xi\|_2^2.
 \tag{1}
\]

The constant is independent of n, all masses, locations and coefficients.
Its proof includes the reusable three-variable inequality (D3) below for all positive A and complex B.

For any real symmetric finite marginal kernel g, not necessarily the curvature kernel, the same core contraction has the exact action C_g=R_g+K_g on every relative Wick degree, with R_g preserving degree and K_g lowering it by two, as specified in (D7)-(D10).
These are algebraic-core identities; no H-boundedness of the two operators is asserted.

The vector xi is only the explicitly defined commutator solution.
It is not an actual conjugate vector for the atomic Z.
Inequality (1) is not asserted for arbitrary analytic unitaries, all relative Wick polynomials, or an arbitrary correlated normal ACSY law.
Thus this result is a finite-model diagnostic and reusable algebraic estimate, not a resolution of the full normal implication.

## Reuse and source scope

The finite substitution and actual-vacuum mechanism extend the realized model of C_F0146, with the full formulas for arbitrary n written below.
The general semicircular mixed-moment input is [NS06-U004](../audits/literature/NS06/Yin_U004.md#ns06-u004); its exact retained source is used only for the free Wick and conditional moment formulas, not a new theorem about liberation.
The actual tensor-adjoint interface is [ACSY24-U003](../audits/literature/ACSY24/Yin_U003.md#acsy24-u003).
No numerical scan, uninspected stochastic estimate, new source acquisition or novelty claim is used.
The three-variable matrix inequality is proved directly.

## Argument

Let N be the finite abelian algebra with projections p_1,...,p_n of positive masses m_1,...,m_n summing to one, and let S be standard semicircular free from N.
Take an entrywise positive real symmetric matrix a=(a_ij) and put
\[
 T=\sum_{i,j}a_{ij}p_iSp_j,\qquad
 R=\sum_{i,j}a_{ij}^{-1}p_iSp_j.
\]
The inverse coefficients are entrywise reciprocals.
The same finite algebraic substitution and actual tensor-adjoint calculation as in [C_F0146](Yin_C_F0146_v1.md#argument) show that liberation gamma of N against T is represented on the full N,S core and has actual real vacuum zeta=-i[R,T].
The reciprocal substitution recovers S from N,T; the scalar correction terms in the adjoint calculation cancel as sum_(i,j)(m_i p_j-m_j p_i)=0.
Thus this is an actual family of liberation laws at every n.
More explicitly, with gamma_0 the free-reference liberation of N against S and partial_S the semicircular derivative,
\[
 Q:=\gamma S=S\otimes1-1\otimes S
 -\sum_{i,j}a_{ij}^{-1}p_iT\otimes p_j
 +\sum_{i,j}a_{ij}^{-1}p_i\otimes Tp_j,
 \qquad \gamma=\gamma_0+I_Q\partial_S.
\]
The reference actual vacua gamma_0*1=0 and partial_S*1=S follow by testing reduced centered free words, with the scalar semicircular word-cut formula on the single-factor words.
All coefficients of Q are bounded reference-core elements.
The actual algebraic-tensor adjoint formula in [ACSY24-U003, equation (1)](../audits/literature/ACSY24/Yin_U003.md#acsy24-u003) then gives gamma*1=[R,T], hence zeta=-i[R,T].
This proves an actual vacuum on the entire represented core, not only formal moment equations.
The symmetric finite marginal adjoint formula also puts every finite marginal tensor used here in the actual beta* domain, where beta=i gamma.

Choose distinct complex locations z_1,...,z_n, set Z=sum_i z_i p_i, and define the curvature weights
\[
 g_{uv}=\sum_w m_w c_{uvw}^2,
\]
where c is the Menger curvature for three distinct locations and is zero for repeated indices.
Define the bounded vector xi by its blocks
\[
 p_u\xi p_v=\frac{i\,p_u\zeta p_v}{\bar z_u-\bar z_v}\quad(u\ne v),
 \qquad p_u\xi p_u=0.
 \tag{D1}
\]
This vector solves zeta=-i[Z*,xi], but it is not asserted to be an actual conjugate vector for Z.
The atomic coordinate cannot meet that ACSY premise.
For \(V=\sum_{i,u}b_{iu}p_iSp_u\), with arbitrary complex coefficients b, the diagnostic bound is
\[
 \operatorname{Re}\langle V,C_gV\rangle
 \ge-\|V\|_\infty^2\|\xi\|_2^2.
 \tag{D2}
\]
The constant is independent of the number of atoms, their masses, their locations, a and b.

### The ratio inequality on one triangle

For positive numbers A_1,A_2,A_3 and complex numbers B_1,B_2,B_3, set s_uv=A_u/A_v+A_v/A_u.
Then
\[
 \begin{split}
 F(A,B)&=\sum_{u<v}
 \bigl(|B_u|^2+|B_v|^2-s_{uv}\operatorname{Re}(\bar B_uB_v)\bigr)\\
 &\ge-\frac12\sum_u |B_u|^2
 \left(\frac{A_v}{A_w}-\frac{A_w}{A_v}\right)^2,
 \qquad\{u,v,w\}=\{1,2,3\}.
 \end{split}
 \tag{D3}
\]
Here the pair (v,w) is opposite vertex u.
To prove it, put x=s_12, y=s_13, z=s_23.
Twice the Hermitian matrix of the left side plus the displayed half-weighted sum is
\[
 H=\begin{pmatrix}z^2&-x&-y\\-x&y^2&-z\\-y&-z&x^2\end{pmatrix}.
\]
All x,y,z are at least 2.
Direct expansion of their ratios gives
\[
 x^2+y^2+z^2-xyz=4.
\]
Every two-by-two principal minor is nonnegative: for instance yz>=x, as the product yz contains the terms A_1/A_2+A_2/A_1 plus two positive terms.
The determinant is
\[
 \det H=2(x^2y^2+x^2z^2+y^2z^2)-10(x^2+y^2+z^2)+24
 =6(d_x+d_y+d_z)+2(d_xd_y+d_xd_z+d_yd_z)\ge0,
\]
where d_x=x^2-4, d_y=y^2-4 and d_z=z^2-4.
The positive diagonal and these principal minors make H positive semidefinite, proving (D3) for complex B as well.
No sign assumption on the B coefficients is used.

### Exact trace formulas and the triple summation

Write kappa_i(u,v)=a_iu/a_iv-a_iv/a_iu.
The fourth free moment calculation used in [C_F0146](Yin_C_F0146_v1.md#argument) gives
\[
 \|\xi\|_2^2
 =\sum_{u\ne v}\frac{m_um_v}{|z_u-z_v|^2}
       \sum_i m_i\kappa_i(u,v)^2.
 \tag{D4}
\]
Indeed p_u zeta p_v is a sum of the orthogonal second-Wick paths p_u S p_i S p_v with the indicated ratio coefficients; diagonal vacuum blocks vanish by symmetry of a.

For completeness, let row_g(j)=sum_v g_jv m_v.
Direct differentiation of p_i S p_j gives
\[
 C_g(p_iSp_j)=\operatorname{row}_g(j)p_iSp_j
 -\frac{m_j}{a_{ij}}\sum_u g_{uj}a_{iu}p_iSp_u.
 \tag{D4a}
\]
Indeed the first differentiated projection has zero partial trace by centering of S.
In the middle term, the ordered-pair insertion into gamma S is
\[
 I_{p_u\otimes p_v}\gamma S
 =\sum_k(1-a_{ku}/a_{kv})p_kSp_u\otimes p_v
 +\sum_l(a_{vl}/a_{ul}-1)p_u\otimes p_vSp_l.
\]
The last differentiated projection cancels the constant part of the first sum and leaves (D4a).
Orthogonality of the first-Wick blocks p_i S p_u then gives
\[
 \begin{split}
 Q_g(V)&:=\operatorname{Re}\langle V,C_gV\rangle\\
 &=\frac12\sum_{i,u,v}m_im_um_vg_{uv}
 \left(|b_{iu}|^2+|b_{iv}|^2
 -\left(\frac{a_{iu}}{a_{iv}}+\frac{a_{iv}}{a_{iu}}\right)
       \operatorname{Re}(\bar b_{iu}b_{iv})\right).
 \end{split}
 \tag{D5}
\]
Insert the actual curvature sum for g and group the three edges of each unordered triple {u,v,w}.
For fixed i its contribution is m_i m_u m_v m_w c_uvw squared times F((a_iu,a_iv,a_iw),(b_iu,b_iv,b_iw)).
Applying (D3) before dropping positive terms yields
\[
 Q_g(V)\ge-\frac12\sum_i m_i\sum_{v<w}m_vm_w\kappa_i(v,w)^2
       \sum_{u\notin\{v,w\}}m_u|b_{iu}|^2c_{uvw}^2.
\]
For every distinct triple, c_uvw squared <=4/|z_v-z_w| squared.
Therefore, with r_i=sum_u m_u|b_iu| squared,
\[
 Q_g(V)\ge-2\sum_i m_i r_i
         \sum_{v<w}\frac{m_vm_w\kappa_i(v,w)^2}{|z_v-z_w|^2}
 \ge-\left(\max_i r_i\right)\|\xi\|_2^2.
 \tag{D6}
\]
Finally E_N(VV*)=sum_i r_i p_i by the free second moment formula, so max_i r_i<=||V|| infinity squared.
This proves (D2).
The ordered-pair factor 2 in (D4) is exactly the factor appearing in (D6).

For selfadjoint V, the coefficient in the small-parameter analytic-unitary second variation is governed by this quadratic form whenever the linear vacuum term vanishes, as it does for these first-Wick vectors.
Thus the small-corner first-Wick family cannot refute a curvature-specific bound by mass concentration: (D2) is a genuine uniform analytical estimate, not a finite numerical scan.

The remaining gap is explicit.
General mixed words have higher-Wick and scalar contractions, whose quadratic kernels need not decompose into (D5) with a fixed positive ratio row.
Nothing here supplies an actual normal conjugate vector in the atomic law, passes from the second variation to every analytic unitary, or establishes (D2) for arbitrary correlated normal laws.
A general proof would need an analogue of the opposite-edge triangle inequality which preserves the actual joint-vacuum cost beyond this linear-Wick representation.

### Exact action on every relative Wick degree

The same finite Gaussian model admits an explicit operator calculation beyond its first degree.
Let W^S_(i0,...,in) be its relative S-Wick path, with leading term p_i0 S p_i1 ... S p_in and all noncrossing contractions subtracted, and let W^S_(i)=p_i.
The inspected [NS06-U004 mixed-moment formula](../audits/literature/NS06/Yin_U004.md#ns06-u004), equation (14.5), shows that different paths of positive degree n are orthogonal, with squared norm product_(r=0)^n m_ir, and different degrees are orthogonal.
These paths span the algebraic core.
This also follows inductively from the recurrence
\[
 W^S_{a,i_0,\ldots,i_n}
 =p_a S W^S_{i_0,\ldots,i_n}
 -\mathbf1_{a=i_1}m_{i_0}W^S_{i_1,\ldots,i_n}
 \quad(n\ge1),
\]
with the final term absent at n=0.
The Kronecker indicator enforces multiplication of the endpoint projections.

Use the rescaled T-Wick paths
\[
 W^T_{i_0,\ldots,i_n}
 =\left(\prod_{r=0}^{n-1}a_{i_ri_{r+1}}\right)
       W^S_{i_0,\ldots,i_n}.
\]
This is the actual T-Wick recursion, since its N-valued covariance on a projection p_j has diagonal coefficients m_j a_ij squared.
Left multiplication has the convenient formula
\[
 T W^T_{i_0,\ldots,i_n}
 =\sum_a W^T_{a,i_0,\ldots,i_n}
 +m_{i_0}a_{i_0i_1}^2W^T_{i_1,\ldots,i_n}
 \quad(n\ge1),
 \tag{D7}
\]
and only the creation sum at degree zero.

Define an algebraic degree-preserving operator R_g by changing the final index j:
\[
 R_gW^T_{i_0,\ldots,i_{n-1},j}
 =\operatorname{row}_g(j)W^T_{i_0,\ldots,i_{n-1},j}
 -m_j\sum_u g_{uj}W^T_{i_0,\ldots,i_{n-1},u}.
 \tag{D8}
\]
At degree zero the same formula means R_gp_j=row_g(j)p_j-m_j sum_u g_uj p_u.
Define K_g=0 in degrees zero and one; in higher degrees remove the final two edges:
\[
 K_gW^T_{i_0,\ldots,i_{n-2},i,j}
 =m_im_j g_{i_{n-2},j}
       (a_{ij}^2-a_{i_{n-2},i}^2)
       W^T_{i_0,\ldots,i_{n-2}}.
 \tag{D9}
\]
Then the actual canonical contraction on the algebraic core is exactly
\[
 C_g=R_g+K_g.
 \tag{D10}
\]

To check this identity without an unproved chaos-invariance assertion, both operators in (D8)-(D9) preserve the initial projection in positive degree, and K_g also does so when it reaches degree zero.
Thus their commutators with each left p_l are zero outside degree zero.
On degree zero, R_g has exactly the finite-rank commutator Theta(I_g gamma(p_l)); that Hilbert--Schmidt operator is supported on the marginal H_N, so these are the required full-core commutators.
Moreover (R_g+K_g)1=0.

Equation (D7) shows that [R_g,T] vanishes on every degree except one.
At degree one it is
\[
 [R_g,T]W^T_{ij}
 =m_im_j\sum_u g_{uj}(a_{iu}^2-a_{ij}^2)p_u.
\]
Equation (D9) cancels precisely this value through K_g T W^T_ij, whereas T K_g W^T_ij=0.
On degree zero both commutators vanish.
On degree two, K_g applied after the creation part of T produces the creation part of T applied to K_g, and its other terms vanish.
On degrees at least three, deletion of the last two edges commutes with creation/deletion of the first edge, with the same coefficients in (D7).
Hence [R_g+K_g,T]=0 on the whole core.
The required commutators with the generating N,T and the value at 1 determine the canonical contraction by induction on words, proving (D10).

In the orthogonal S-path coordinates, (D8) acts at the final vertex by the same ratio matrix as in (D5), now for every preceding path.
The lowering coefficient in (D9) becomes
\[
 m_im_j g_{aj}\left(\frac{a_{ij}}{a_{ai}}-\frac{a_{ai}}{a_{ij}}\right)
 \quad\text{for the tail }(a,i,j).
\]
This is a concrete decomposition of the all-degree core operator.
It does not yet bound its form on arbitrary analytic unitaries: the diagonal triangle estimate must be summed with actual operator-norm control of the tail coefficients, and the cross-degree pairing with K_g must also be controlled.
Hilbert orthogonality alone bounds only the total L2 mass and does not supply either missing operator-norm estimate.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:26 |
| status | open |
| reason | Complete finite-model triangle bound and exact all-degree Wick action; removes the final normalization-ambiguous comparison to the weighted vacuum, preserving the explicit action coefficients. Independent review of this revision is pending; actual normal and full-unitary estimates remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Finite-model theorem](#statement) | Uniform linear-Wick curvature form, three-variable inequality and exact full-core Wick action, with no actual normal-A claim. |
| argument | [Complete argument](#argument) | Actual finite substitution/vacuum, 3-by-3 positive semidefiniteness, triple summation with constant one, and all-degree commutator identification. |
| dependency | [Realized finite substitution](Yin_C_F0146_v1.md#argument) | Prototype finite-coefficient construction and actual vacuum mechanism; its arbitrary-n formulas and adaptations are explicitly supplied here. |
| dependency | [Actual tensor adjoint](../audits/literature/ACSY24/Yin_U003.md#acsy24-u003) | Equation (1) on finite bounded reference-core coefficients, after the reference actual vacua are verified. |
| dependency | [Free semicircular mixed moments](../audits/literature/NS06/Yin_U004.md#ns06-u004) | Equation (14.5), its conditional second/fourth moments and the stated relative Wick recursion; source proof limits retained. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T20:28 |
| status | proved |
| reason | Adopt the complete finite-model curvature estimate and all-degree core action after R_F0157 checked v2 and all three inputs, preserving the distinct v1 normalization finding. No general normal or all-unitary estimate is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Finite-model theorem](#statement) | Uniform linear-Wick curvature form, three-variable inequality and exact full-core Wick action, with no actual normal-A claim. |
| argument | [Complete argument](#argument) | Actual finite substitution/vacuum, 3-by-3 positive semidefiniteness, triple summation with constant one, and all-degree commutator identification. |
| dependency | [Realized finite substitution](Yin_C_F0146_v1.md#argument) | Prototype finite-coefficient construction and actual vacuum mechanism; its arbitrary-n formulas and adaptations are explicitly supplied here. |
| dependency | [Actual tensor adjoint](../audits/literature/ACSY24/Yin_U003.md#acsy24-u003) | Equation (1) on finite bounded reference-core coefficients, after the reference actual vacua are verified. |
| dependency | [Free semicircular mixed moments](../audits/literature/NS06/Yin_U004.md#ns06-u004) | Equation (14.5), its conditional second/fourth moments and the stated relative Wick recursion; source proof limits retained. |
| review | [Complete independent review](../audits/reviews/Yin_R_F0157_v1.md#conclusion) | Entire v2 theorem and argument, actual finite model and vacua, triangle constants, all-degree commutators, exact dependencies and the preserved v1 normalization boundary. |


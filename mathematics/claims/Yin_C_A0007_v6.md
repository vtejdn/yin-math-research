---
author: Yin
---
# Complete affiliated frames and actual subordination boundary coefficients

This development serves [S_A0005](../strategies/Yin_S_A0005.md) under [A0001](../tasks/Yin_T_A0001_v1.md#contract).
It computes the conditional boundary products for the complete affiliated frame selected in [L_A0058](../ledger/Yin_L_A0058_v1.md#first-priority-in-s_a0005).
It also gives a three-square additive realization with the same nullity, full expected-kernel support, zero polynomial kernel and actual subordination boundary values equal to zero.
These are exact calibration results over a free amalgam.
They extend the available witness examples without claiming a new group class or a general construction for arbitrary Task inputs.

## Inputs

- [C_A0007_v5](Yin_C_A0007_v5.md#argument) supplies the exact support-compression correction and its arbitrary-input limitation.
- [L_A0023_v1](../ledger/Yin_L_A0023_v1.md#an-additive-noncentral-boundary-matrix) supplies the original additive free-boundary matrix and its zero polynomial kernel.
- [C_A0004_v2](Yin_C_A0004_v2.md#free-projection-and-gap) supplies the degree-four tree Green coefficients and the original edge projection.
- [BBL21](../audits/literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface) supplies the actual subordination boundary theorem for a boundedly invertible expected kernel.
  Its equation (3.7), retained in the same source unit, supplies the conditional resolvent identity used below.
- [The affiliated graph calculation](../ledger/Yin_L_A0058_v1.md#a-complete-kernel-frame-in-the-free-boundary-calibration) supplies the initial complete-frame construction.

The analytic subordination theorem and finite tracial affiliated-operator calculus are accepted at these previously retained interfaces.
The conditional coefficients, regression obstruction, kernel transport and second model below are checked directly.

<a id="statement"></a>
## Setting and statement

Use
\[
 G=F(z,a,b)=G_1*_{H}G_2,\qquad
 G_1=F(z,a),\quad G_2=F(z,b),\quad H=\langle z\rangle.
\]
Let \(M=\mathcal N(G)\), \(\mathcal B=\mathcal N(H)\), and let \(E_H\) be the canonical trace-preserving expectation, amplified entrywise.
Write \(\tau\) for the canonical group trace and \(\nu\) for nullity measured with the unnormalized matrix trace.
Set
\[
 A=a-1,\qquad B=b-1,\qquad \partial=(A\ B),
\]
\[
 T=T_a+T_b=
 \begin{pmatrix}0&A&B\\A^*&0&0\\B^*&0&0\end{pmatrix},
\]
where \(T_a\) contains the \(A,A^*\) entries and \(T_b\) contains the \(B,B^*\) entries.
Both summands are finite selfadjoint matrices over their indicated vertex group rings.

For \(p_T=P_{\ker T}\), the exact conditional data are
\[
 E_H(p_T)=
 \begin{pmatrix}0&0&0\\0&1/2&-1/6\\0&-1/6&1/2\end{pmatrix},
 \qquad
 E_H(T_ap_T)=
 \begin{pmatrix}0&-1/3&1/3\\0&0&0\\0&0&0\end{pmatrix},
 \qquad E_H(T_bp_T)=-E_H(T_ap_T).
 \tag{1}
\]
If \(q=\operatorname{diag}(0,I_2)\), then \(s(E_H(p_T))=q\), \(qTq=0\), \(\nu(T)=1\), and the support-compression correction is \(\delta_q(T)=1\).
Nevertheless every \(b\in M_3(\mathcal B)\) satisfies
\[
 \|(T_a-b)p_T\|_{2,\operatorname{Tr}\otimes\tau}^2\ge\frac13.
 \tag{2}
\]
Equality is attained by a selfadjoint constant matrix.
The actual subordination function for \(T_a+T_b\) therefore has no finite norm boundary limit at zero for either summand.

Define a second additive selfadjoint matrix by
\[
 R=\begin{pmatrix}A&1&0\\0&1&B\end{pmatrix},
 \qquad J=\operatorname{diag}(1,-1),\qquad
 Y=R^*JR=Y_a+Y_b,
 \tag{3}
\]
\[
 Y_a=\begin{pmatrix}A^*A&A^*&0\\A&1&0\\0&0&0\end{pmatrix},
 \qquad
 Y_b=\begin{pmatrix}0&0&0\\0&-1&-B\\0&-B^*&-B^*B\end{pmatrix}.
 \tag{4}
\]
Then
\[
 \ker Y=\ker R,\qquad \nu(Y)=1,\qquad
 \ker(Y:(\mathbb CG)^3\longrightarrow(\mathbb CG)^3)=0,
 \tag{5}
\]
and
\[
 E_H(P_{\ker Y})=
 C_1:=
 \begin{pmatrix}
 1/3&1/6&1/12\\
 1/6&1/3&1/6\\
 1/12&1/6&1/3
 \end{pmatrix}
 \ge \frac{9-\sqrt{33}}{24}I_3.
 \tag{6}
\]
The actual BBL21 boundary values for (4) at zero exist and are \(b_a=b_b=0\).
The resulting unnormalized nullities obey
\[
 \nu(Y_a-b_a)+\nu(Y_b-b_b)=2+2=3+\nu(Y).
 \tag{7}
\]
The finite invertible matrix
\[
 Q=\begin{pmatrix}0&1&0\\1&-A&0\\0&0&-1\end{pmatrix},
 \qquad
 Q^{-1}=\begin{pmatrix}A&1&0\\1&0&0\\0&0&-1\end{pmatrix}
 \tag{8}
\]
maps the complete kernel of \(T\) onto that of \(Y\).
Thus this realization has zero nullity correction while replacing the deficient expected support by full support.

<a id="argument"></a>
## Complete graph frame for the first model

Left convolution by \(A\) and by \(A^*\) is injective with dense range, by the infinite cyclic subgroup calculation.
In the finite affiliated algebra define
\[
 C=A^{-1}B,\qquad
 \operatorname{dom}C=\{y:By\in\operatorname{ran}A\}.
\]
The composition is closed because \(A^{-1}\) is closed and \(B\) is bounded.
Its domain is dense by finite tracial affiliated-product calculus.
For \(Wy=(-Cy,y)\), injectivity of \(A\) gives
\[
 Ax+By=0\iff y\in\operatorname{dom}C,\quad x=-Cy.
\]
Consequently \(\operatorname{ran}W=\ker\partial\), a closed subspace.
The positive operator \(W^*W=I+C^*C\) is bounded below by the identity.
The polar normalization
\[
 V=W(I+C^*C)^{-1/2}
\]
is a bounded isometry with \(V^*V=I\) and \(VV^*=P_{\ker\partial}\).
These are closed affiliated products whose bounded extensions lie in the corresponding matrix spaces over \(M\).
This identifies the complete analytic kernel even though the polynomial kernel vanishes.

## Exact conditional products for the first model

Put
\[
 L=AA^*+BB^*=4-a-a^{-1}-b-b^{-1}.
\]
The degree-four tree bound gives \(L\ge(4-2\sqrt3)I>0\).
Hence
\[
 P:=P_{\ker\partial}=I_2-\partial^*L^{-1}\partial,
 \qquad p_T=\operatorname{diag}(0,P).
 \tag{9}
\]
The retained tree Green coefficients are
\[
 \tau(L^{-1}g)=\frac38\,3^{-|g|},\qquad g\in F(a,b),
 \tag{10}
\]
where \(|g|\) is reduced word length.
The subgroup \(F(a,b)\) meets \(H\) trivially.
Thus \(E_H\) restricts to \(\tau(\,\cdot\,)1\) on \(\mathcal N(F(a,b))\), and all the present conditional calculations are scalar matrix calculations.
The coefficients in (10) at lengths zero, one and two are respectively \(3/8,1/8,1/24\).
Equation (9) then gives
\[
 E_H(P)=C_0:=
 \begin{pmatrix}1/2&-1/6\\-1/6&1/2\end{pmatrix}.
 \tag{11}
\]
Its eigenvalues are \(1/3,2/3\), and
\[
 C_0^{-1}=\begin{pmatrix}9/4&3/4\\3/4&9/4\end{pmatrix}.
\]

Only the first row of \(T_ap_T\) can be nonzero, with tail entries \(AP_{11},AP_{12}\).
Cyclicity of \(\tau\), normality of \(A\), and (10) give
\[
 \tau(AP_{11})=\tau(A)-\tau(L^{-1}AAA^*)=-1+\frac23=-\frac13.
\]
Indeed \(AAA^*=3a-a^2+a^{-1}-3\), whose pairing with (10) is \(-2/3\).
Similarly
\[
 \tau(AP_{12})=-\tau(L^{-1}BAA^*)=\frac13,
\]
because \(BAA^*=2b-ba-ba^{-1}-2+a+a^{-1}\) pairs to \(-1/3\).
This proves (1).
The relation \(Tp_T=0\) gives the last equality of (1).

The trace of (11) is one, so \(\nu(T)=1\).
Its support in three coordinates is \(q\), and \(qTq=0_q\) has corner nullity two.
The exact correction formula of C_A0007_v5 gives
\[
 \delta_q(T)=2-1=1.
 \tag{12}
\]
The off-corner map is the original row \(\partial\), with regular rank one.

## Regression obstruction to an actual boundary value

Let \(r=(A,0)\), \(t=\tau(rP)=(-1/3,1/3)\), and \(d_0=tC_0^{-1}=(-1/2,1/2)\).
A calculation from (10) gives
\[
 \tau(rPr^*)=\tau(AP_{11}A^*)=\frac23.
 \tag{13}
\]
For details, writing \(x=AA^*=2-a-a^{-1}\), one has
\[
 x^2=6-4(a+a^{-1})+a^2+a^{-2},
 \qquad
 \tau(x^2L^{-1})=\frac43.
\]
Thus (13) equals \(\tau(x)-\tau(x^2L^{-1})=2-4/3\).

For any bounded row \(d\in M_{1,2}(\mathcal B)\), bimodularity and trace preservation yield
\[
 \begin{aligned}
 \tau((r-d)P(r-d)^*)
 &=\frac23-tC_0^{-1}t^*
   +\tau((d-d_0)C_0(d-d_0)^*)\\
 &=\frac13+\tau((d-d_0)C_0(d-d_0)^*)\ge\frac13.
 \end{aligned}
 \tag{14}
\]
Here \(tC_0^{-1}t^*=1/3\).
The first row of \((T_a-b)p_T\) has the left side of (14) as its squared \(L^2\)-norm, and the other rows contribute nonnegative terms.
This proves (2).
Equality holds for
\[
 b_0=\begin{pmatrix}0&-1/2&1/2\\-1/2&0&0\\1/2&0&0\end{pmatrix}.
\]
In particular the formal recovery equation \(bE_H(p_T)=E_H(T_ap_T)\) has bounded selfadjoint solutions, but every such candidate fails the required kernel relation by the positive error (14).

To obtain the assertion about actual subordination, let \(E_a\) be the trace-preserving expectation onto \(M_3(\mathcal N(G_1))\).
This is the von Neumann algebra generated by \(M_3(\mathcal B)\) and \(T_a\), since constant matrix units isolate \(A=a-1\).
The conditional resolvent identity in BBL21 gives
\[
 (\omega_a(i\eta I)-T_a)
 E_a\!\left[i\eta(i\eta I-T)^{-1}\right]=i\eta I.
 \tag{15}
\]
The scaled resolvent tends to \(p_T\) in \(L^2\) as \(\eta\downarrow0\).
If \(\omega_a(i\eta I)\) had a finite norm limit \(b\in M_3(\mathcal B)\), (15) would imply
\[
 (b-T_a)E_a(p_T)=0.
\]
Since \(b-T_a\) belongs to the range algebra of \(E_a\), trace preservation and bimodularity imply
\[
 \|(b-T_a)p_T\|_2^2
 =(\operatorname{Tr}\otimes\tau)
   \bigl((b-T_a)E_a(p_T)(b-T_a)^*\bigr)=0.
\]
This contradicts (2).
The same argument applies to \(T_b\), using \(T_bp_T=-T_ap_T\).
It invokes the conditional resolvent identity in the upper half-plane, while establishing failure of the finite norm endpoint directly.

## A full-support additive realization

For (3), the adjoint acts by
\[
 R^*(u,v)=(A^*u,u+v,B^*v).
\]
Injectivity of \(A^*,B^*\) makes \(R^*\) injective.
Consequently \(R^*JR\xi=0\) implies \(JR\xi=0\), and hence \(R\xi=0\).
This proves \(\ker Y=\ker R\).
Using the finite tracial rank identity for \(R,R^*\), its nullity is \(3-2=1\).

There is also a complete affiliated frame with explicit domains.
On the dense common domain
\[
 \mathcal D=\operatorname{ran}A\cap\operatorname{ran}B
 =\operatorname{dom}A^{-1}\cap\operatorname{dom}B^{-1},
 \qquad
 W_1y=(-A^{-1}y,y,-B^{-1}y),
 \tag{16}
\]
the operator \(W_1\) is closed and has range exactly \(\ker R\).
Density follows from intersection of the domains of finitely many affiliated operators in a finite von Neumann algebra.
Closedness follows by applying closedness of each inverse to the common middle coordinate.
The two equations \(Ax+y=0\), \(y+Bz'=0\) give both directions of the range assertion.
The positive selfadjoint operator \(K=W_1^*W_1\) is the operator associated to the closed quadratic form
\[
 \|A^{-1}y\|^2+\|y\|^2+\|B^{-1}y\|^2,\qquad y\in\mathcal D,
\]
so \(K\ge I\).
The bounded polar normalization \(V_1=W_1K^{-1/2}\) satisfies \(V_1^*V_1=I\) and \(V_1V_1^*=P_{\ker Y}\).

The polynomial kernel is zero.
For a finite vector in \(\ker R\), the two equations imply \(Ax=Bz'\).
After separating finite supports into right cosets of \(F(a,b)\), this is a finite edge chain with zero boundary on the free Cayley tree.
Leaf removal gives \(x=z'=0\), and then \(y=0\).
Since \(\ker Y=\ker R\) analytically, the same conclusion holds for finite vectors in \(\ker Y\).

An elementary argument already proves full expected support.
Write \(p_Y=P_{\ker Y}\).
Its entries lie in \(\mathcal N(F(a,b))\), so \(E_H(p_Y)\) is a constant positive matrix.
If a constant row \(c=(c_1,c_2,c_3)\) annihilates its range, faithfulness of \(\tau\) gives \(cp_Y=0\), and hence
\[
 -c_1A^{-1}+c_2-c_3B^{-1}=0
\]
as an affiliated identity, by (16).
Multiplication on the left by \(A\) and on the right by \(B\) gives the finite identity
\[
 -c_1B+c_2AB-c_3A=0.
 \tag{17}
\]
The coefficients of \(ab,b,a\), respectively, force \(c_2,c_1,c_3\) to vanish.
Thus \(E_H(p_Y)\) is positive definite and has a bounded inverse.

### Exact expected projection from the degree-three tree

For completeness, all entries of this expectation can be computed.
Put \(U=\operatorname{diag}(1,-1)\), \(S=\operatorname{diag}(1,1,-1)\), and \(D=URS\).
Then
\[
 D=\begin{pmatrix}A&1&0\\0&-1&B\end{pmatrix},\qquad
 DD^*=\begin{pmatrix}3-a-a^{-1}&-1\\-1&3-b-b^{-1}\end{pmatrix}.
 \tag{18}
\]
This is the incidence Laplacian of the universal cover of the graph with two vertices, a loop at each vertex and one joining edge.
The deck group is \(F(a,b)\), and the universal cover is the degree-three tree.
Its adjacency norm is at most \(2\sqrt2\).
One direct verification orients the tree towards an end and writes adjacency as \(L+L^*\), where the operator summing the two forward children has norm \(\sqrt2\).
Consequently \(DD^*\ge(3-2\sqrt2)I\).

Its inverse kernel between vertices at distance \(d\) is
\[
 k(d)=\frac23\,2^{-d}.
 \tag{19}
\]
The recursion \(3k(d)-k(d-1)-2k(d+1)=0\) for \(d\ge1\) and the root equation \(3k(0)-3k(1)=1\) verify the inverse column.
The column is square summable, and bounded invertibility of the Laplacian gives uniqueness.
Using \(P_{\ker D}=I-D^*(DD^*)^{-1}D\), the endpoint distances of the three edges in one fundamental domain give
\[
 E_H(P_{\ker D})=
 \begin{pmatrix}1/3&1/6&-1/12\\1/6&1/3&-1/6\\-1/12&-1/6&1/3\end{pmatrix}.
\]
The diagonal entry uses \(1-2(k(0)-k(1))=1/3\).
The adjacent-edge entries use \(k(0)-2k(1)+k(2)=1/6\), with their incidence signs.
The two loop edges use \(k(1)-2k(2)+k(3)=1/12\), again with their incidence signs.
Since \(P_{\ker R}=S P_{\ker D}S\), this gives (6).
The eigenvalues of \(C_1\) are \(1/4\) and \((9\pm\sqrt{33})/24\).

### Actual boundaries and kernel transport

The two vertex algebras are free over \(M_3(\mathcal B)\), and (6) verifies the bounded-inverse premise of BBL21.
The theorem therefore supplies actual selfadjoint norm limits \(b_a,b_b\in M_3(\mathcal B)\), with \(b_a+b_b=0\) and
\[
 (Y_a-b_a)p_Y=(Y_b-b_b)p_Y=0.
\]
Each row of \(R\) annihilates \(p_Y\), so \(Y_ap_Y=Y_bp_Y=0\).
Taking expectation gives \(b_jC_1=0\), hence \(b_a=b_b=0\).
Each row \((A,1,0)\) and \((0,1,B)\) has regular rank one, witnessed by its constant unit entry.
The two marginal nullities are therefore two, proving the exact theorem identity (7).

Finally, \(\ker T=\{(0,x,z'):Ax+Bz'=0\}\).
The matrix \(Q\) in (8) sends such a vector to \((x,-Ax,-z')\), which lies in \(\ker R\).
Conversely every vector in \(\ker R\) has the form \((x,-Ax,z'')\) with \(Ax=Bz''\), whose \(Q^{-1}\)-image is \((0,x,-z'')\in\ker T\).
Both maps are bounded finite group-ring matrices.
This proves the exact complete-kernel transport and its zero nullity correction.
The displayed formulas (4) verify vertex additivity directly.

## Consequence for the strategy

The first model proves that a complete bounded frame obtained from affiliated rational columns can coexist with a positive lower bound for every candidate boundary-recovery error.
Its formal expectation equation therefore cannot replace the actual subordination boundary theorem.
The second model has full expected support and genuine boundary recovery, while admitting no nonzero polynomial kernel column.
This separates polynomial kernel generation from the bounded-inverse condition actually used by the theorem.
The positive inverse-square-root normalization supplies complete bounded frames with the stated domains, and the actual expected projection determines whether the theorem applies.
The known free-group geometry and independently certified cyclic denominators resolve both examples.
Extension to inputs with an unknown off-corner rank or uncontrolled boundary coefficient class remains the substantive A0001 obligation.

## Assessment history

### Decision reviewed-affiliated-boundaries

| Field | Value |
| --- | --- |
| date | 2026-11-21T02:59 |
| status | proved |
| reason | Independent whole-artifact inspection supports the two exact calibrations, including the positive regression obstruction, admissible full-support realization and complete kernel transport. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both models, actual boundary behavior, complete frames, all conditional constants and zero-correction kernel transport. |
| argument | [Argument](#argument) | Entire domain-aware proof, exact Green calculations, subordination interfaces and declared limits. |
| review | [Whole-artifact finding](../audits/reviews/Yin_R_A0020_v6.md#whole-artifact-finding) | Independent complete statement and proof inspection, including the final bounded-inverse wording. |
| dependency | [Degree-four Green coefficients](Yin_C_A0004_v2.md#free-projection-and-gap) | Actual free-tree inverse coefficients and projection used in the first calculation. |
| dependency | [Support correction](Yin_C_A0007_v5.md#argument) | Exact corner-nullity convention and off-corner correction for the deficient expected support. |
| dependency | [BBL21 interface](../audits/literature/BBL21/Yin_U001.md#bbl21-u001) | Equation (3.7) and Theorems 3.2 and 3.5 in arXiv v2, with general base, bounded inverse and norm boundary topology. |

## Current assessment

[Selected decision](#decision-reviewed-affiliated-boundaries)

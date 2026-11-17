---
author: Yin
---

# Singular-value products with unequal numbers of added columns and rows

<a id="statement"></a>
## The rectangular border inequality

For a complex matrix \(Z\), let \(p_j(Z)\) be the product of its \(j\) largest singular values, with \(p_0(Z)=1\) and missing singular values equal to zero.
For a matrix \(W\) with \(j\) columns write \(\operatorname{vol}_j(W)=\det(W^*W)^{1/2}\).
Fix integers \(a\ge b\ge1\), let \(M\in\mathbb C^{n\times n}\), and form
\[
 B=\begin{pmatrix}M&U\\V^*&D\end{pmatrix},
 \qquad
 U\in\mathbb C^{n\times a},\quad
 V\in\mathbb C^{n\times b},\quad
 D\in\mathbb C^{b\times a}.
\]
Suppose \(0\le r\le n-a-b\), fix a singular vector decomposition of \(M\), and let \(Q_L\) and \(Q_R\) remove, respectively, its first \(r+a\) left and first \(r\) right singular vectors.
Then, with \(c_a=2^{3a}\binom{2a}{a}\),
\[
 p_{r+a+b}(B)
 \ \ge\ c_a^{-1}p_r(M)
       \operatorname{vol}_a(Q_LU)
       \operatorname{vol}_b(Q_RV).
 \tag{1}
\]
The same fixed decomposition determines both projections at singular-value ties.
There is no restriction on \(D\) or on dependence between the two borders.
When \(r>n-2a\), the left projected volume is zero, so the nonzero conclusion of (1) is confined to \(r\le n-2a\).

This is a project deduction from the [paired block inequality](Yin_C_F0347_v1.md#statement).
It allows fewer good new row directions than new column directions while retaining a gain of \(a+b\) singular values.

<a id="padding-limit"></a>
## Removing the singular values supplied by auxiliary rows

Let \(A:\mathbb C^N\to\mathbb C^H\), let \(F:\mathbb C^d\to\mathbb C^N\) be an isometry, and put
\[
 A_t=\begin{pmatrix}A\\tF^*\end{pmatrix},\qquad t>0.
\]
For every integer \(j\ge0\),
\[
 \limsup_{t\to\infty}t^{-d}p_{j+d}(A_t)
 \le p_j(A).
 \tag{2}
\]
For \(d=0\) this is immediate.
Otherwise choose an isometry \(F_\perp\) onto \(\operatorname{ran}(F)^\perp\), and use the unitary domain basis \([F,F_\perp]\).
In that basis,
\[
 A_t=
 \begin{pmatrix}AF&AF_\perp\\tI_d&0\end{pmatrix}
 =
 \begin{pmatrix}I_H&t^{-1}AF\\0&I_d\end{pmatrix}
 \begin{pmatrix}0&AF_\perp\\tI_d&0\end{pmatrix}
 =S_t C_t.
\]
The norm of \(S_t\) is at most \(1+t^{-1}\|A\|\).
For \(t>\|A\|\), the largest \(d\) singular values of \(C_t\) are \(t\), and its remaining singular values are those of \(AF_\perp\), with the usual zero convention.
Contractivity and submultiplicativity on exterior powers give
\[
 t^{-d}p_{j+d}(A_t)
 \le (1+t^{-1}\|A\|)^{j+d}p_j(AF_\perp)
 \le (1+t^{-1}\|A\|)^{j+d}p_j(A).
\]
Letting \(t\to\infty\) proves (2), including cases in which either product vanishes.

<a id="argument"></a>
## Padding the shorter border

If \(r>n-2a\), then \(\operatorname{rank}Q_L=n-r-a<a\), and (1) follows from nonnegativity.
Assume \(r\le n-2a\) and put \(d=a-b\).
The case \(d=0\) is the cited paired block inequality with \(k=a\).
For \(d>0\), choose an \(n\)-by-\(d\) isometry \(E\) with range in
\[
 \operatorname{ran}Q_R\cap
       \operatorname{ran}(Q_RV)^\perp.
\]
This is possible because that space has dimension at least \(n-r-b\ge a-b=d\).
Consequently \(Q_RE=E\), \(E^*Q_RV=0\), and
\[
 \operatorname{vol}_a\bigl(Q_R[V,tE]\bigr)
 =t^d\operatorname{vol}_b(Q_RV).
 \tag{3}
\]
The identity remains valid if \(Q_RV\) is rank deficient.

Append \(d\) auxiliary rows to \(B\):
\[
 B_t=
 \begin{pmatrix}
 M&U\\V^*&D\\tE^*&0
 \end{pmatrix}.
\]
This is a square matrix of size \(n+a\), with paired border size \(a\), right border columns \([V,tE]\), and corner block obtained by stacking \(D\) above \(d\) zero rows.
The paired block inequality applies to this corner without any invertibility assumption and gives, using (3),
\[
 p_{r+2a}(B_t)
 \ge c_a^{-1}t^d p_r(M)
       \operatorname{vol}_a(Q_LU)
       \operatorname{vol}_b(Q_RV).
 \tag{4}
\]
Apply (2) to \(A=B\), \(F=(E^{\mathsf T},0^{\mathsf T})^{\mathsf T}\), and \(j=r+a+b\).
Here \(F^*=[E^*,0]\), so the augmented matrix in (2) is exactly \(B_t\), and \(j+d=r+2a\).
Divide (4) by \(t^d\), take the upper limit, and obtain (1).

<a id="square-compression"></a>
## Keeping selected new rows of a square addition

Suppose a square matrix \(\widehat B\) of size \(n+a\) extends \(M\) by \(a\) columns and \(a\) rows.
Keep all columns, all \(n\) old rows and any \(b\) of its new rows, obtaining the rectangular matrix \(B\) above.
Since row restriction is an orthogonal compression,
\[
 p_{r+a+b}(\widehat B)\ge p_{r+a+b}(B),
\]
and hence the right side of (1) also bounds the singular product of \(\widehat B\).
If the old retained index is \(r=n-\delta\), the new retained index is \(r+a+b\), and its deficit from the new square dimension \(n+a\) is \(\delta-b\).
In particular, \(a=q+2\) and \(b=4\) decrease that deficit by four whenever \(q\ge2\) and the two projected volumes admit the needed lower bounds.
This deterministic statement does not supply probability bounds for those volumes.

## Assessment history

### Decision rectangular-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T20:51 |
| status | open |
| reason | Auxiliary rows reduce the rectangular border inequality to the paired inequality; the fixed deduction awaits a separate review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Rectangular inequality](#statement) | Complex matrices, arbitrary corner, unequal border sizes and the stated singular-vector projections. |
| argument | [Auxiliary-row proof](#argument) | Padding, the exact projected volume and removal of the added singular values. |
| support | [Padding limit](#padding-limit) | The normalized singular-product upper bound with constant one. |
| support | [Square compression](#square-compression) | Selected new rows and the deficit decrease. |
| dependency | [Paired block inequality](Yin_C_F0347_v1.md#statement) | The proved square-border bound with \(k=a\) and constant \(c_a\). |


### Decision rectangular-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T20:56 |
| status | proved |
| reason | Padding the smaller border and removing its large singular values proves the unequal-volume product bound, with the stated full-square compression consequence. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Rectangular singular-product bound](#statement) | Arbitrary fixed border sizes, dimension restrictions and all lower corners. |
| argument | [Complete deterministic proof](#argument) | The padding volume and shear limit. |
| support | [Deficit decrease](#square-compression) | Use of selected incoming and outgoing channel spaces. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0374_v1.md#rectangular-whole-proof) | The complete statement and singular cases. |

## Current assessment
[Selected decision](#decision-rectangular-reviewed)

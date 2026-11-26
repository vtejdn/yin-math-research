---
author: Yin
---

# Full rank for two-sided cycles in the congruence double

## Statement

Use the [congruence double](Yin_C_A0121_v1.md#statement)
\[
 V=\ker(\operatorname{SL}_3(\mathbb Z)\to\operatorname{SL}_3(\mathbb F_3)),\quad
 b=I+3E_{12},\quad a=I+9E_{13},\quad G=V_1*_{\langle b\rangle}V_2,
 \qquad p=1-b+a_1+a_2.
\]
Here \(a_j\) is the copy of \(a\) in \(V_j\).
For \(n\ge2\) let \(C\) have \(p\) on its diagonal, \(-u_i\) in position \((i,i+1)\) for \(1\le i<n\), and \(-u_n\) in position \((n,1)\), with other entries zero.
Take \(u_i=\gamma_{i1}g_{i1}+\gamma_{i2}g_{i2}\), where \(g_{ij}\in V_j\) and \(\gamma_{ij}\in\mathbb C\).
For each vertex form the ordered product
\[
 w_j=(a_j^{-1}g_{nj})(a_j^{-1}g_{1j})\cdots(a_j^{-1}g_{n-1,j}).
\]
If both \(w_1,w_2\) are nonidentity, then \(C\) has regular rank \(n\), and
\[
 p-u_n p^{-1}u_1 p^{-1}u_2\cdots p^{-1}u_{n-1}
\]
is an affiliated unit.
The expression belongs to the first scalar inverse layer of \(\mathbb CG\).
A finite-dimensional test below also covers some cases with \(w_j=1\) and gives an upper bound on nullity in all cases.

In particular put \(s=I+3E_{21}\), \(t=I+3E_{32}\) and denote their vertex copies by subscripts.
The two-state choice \(u_1=s_1+s_2,\ u_2=t_1+t_2\) gives a unit \(p-u_2p^{-1}u_1\).
For the three-state choice \(u_1=s_1+s_2,\ u_2=t_1+t_2,\ u_3=s_1t_1+t_2s_2\), the exact scalar \(p-u_3p^{-1}u_1p^{-1}u_2\) is an affiliated unit.
In both examples the auxiliary weight spaces can be chosen so that each arrow has an invertible corner in each vertex.

## Both cycles in the finite representation

Let \(D\) be the image of \(V\) modulo \(5\), and \(K=\langle\bar b,\bar a\rangle\cong(\mathbb Z/5)^2\) as in the [finite quotient calculation](Yin_C_A0121_v1.md#the-finite-quotient-detecting-the-commutator).
Fix the character \(\chi\) of \(K\) taking \(\bar b\) to \(1\) and \(\bar a\) to a primitive fifth root of unity.
On each right coset \(Kx\) choose \(\eta(x)\) on the unit circle for a fixed representative, and extend by \(\eta(kx)=\chi(k)\eta(x)\).
Let \(W\delta_x=\eta(x)\delta_x\) on \(\ell^2(D)\).
Use \(\lambda_D\oplus\lambda_D\) with the weight spaces consisting of \((\xi,W\xi)/\sqrt2\) and \((\xi,-W\xi)/\sqrt2\), identifying each with \(\ell^2(D)\).
In these coordinates both off-diagonal blocks of a group element \(g\in V\) equal
\[
 B(g)=\tfrac12\big(\lambda_D(\bar g)-W^*\lambda_D(\bar g)W\big).
\]
This is a weighted permutation with weight \((1-\eta(x)\overline{\eta(\bar g x)})/2\) at \(x\).
Thus \(B(b)=0\) and \(B(a)\) is invertible.
For any fixed finite list of \(g\) with \(\bar g\notin K\), this construction can make every \(B(g)\) invertible.
Since \(K\bar g x\ne Kx\) for every \(x\), equality of the indicated phases would impose a relation on two independent coset phases.
The finitely many such relations have measure zero for independent uniform phases.
Use the same representation on each vertex and bend the second vertex by the two weights as in the [regular trace identity](Yin_C_A0118_v1.md#regular-trace-identity-and-the-specialization).
The identity \(B(b)=0\) guarantees agreement along the entire edge at every unit phase.

## Eliminating each vertex cycle

Split \(p\) as \(1-b+a_1\) in the left vertex and \(a_2\) in the right vertex.
For the left \(12\) corner and right \(21\) corner of the unbent twists use the preceding identifications, and set \(d=|D|\).
In vertex \(j\) divide each row on the left by its boundedly invertible diagonal corner \(\lambda_G(a_j)\otimes B(a)\).
For the arrow \(i\) the corresponding normalized entry is \(-T_{ij}\), where
\[
 T_{ij}=\lambda_G(a_j^{-1}g_{ij})\otimes C_{ij},\qquad
 C_{ij}=\gamma_{ij} B(a)^{-1}B(g_{ij}).
\]
Here \(B(g_{ij})\) uses the identification of \(V_j\) with \(V\).
Successive elimination at the first \(n-1\) identity pivots leaves
\[
 I_d-T_{nj}T_{1j}\cdots T_{n-1,j}
 =I_d-\lambda_G(w_j)\otimes K_j,\qquad K_j=C_{nj}C_{1j}\cdots C_{n-1,j}.
\]
The product order follows from \(x_i=T_{ij}x_{i+1}\) and the closing equation at \(x_n\).
This uses the [ordered three-state elimination](../ledger/Yin_L_A0009_v1.md#an-ordered-three-state-example) with finite-dimensional coefficient matrices on the individual translations.

For \(w_j\ne1\), torsion-freeness gives infinite order.
On each right coset of \(\langle w_j\rangle\), Fourier transformation reduces the last operator to \(I_d-zK_j\) on the circle, up to orientation.
Its determinant has constant term one and vanishes at most at finitely many points, so its regular rank is \(d\).
For \(w_j=1\) the loss of rank is precisely \(\dim_{\mathbb C}\ker(I_d-K_j)\).
Write \(k_j\) for this loss, with \(k_j=0\) when \(w_j\ne1\).
The two vertex corners have ranks \(nd-k_1\) and \(nd-k_2\), respectively.
The [two-corner inequality](Yin_C_A0123_v1.md#a-polynomial-with-affiliated-coefficients) gives
\[
 0\le n-\operatorname{rk}_G C\le(k_1+k_2)/(2d).
\]
In particular both zero losses give full rank.
For the original matrix the first \(n-1\) pivots are \(p\), an affiliated unit by the [mixed scalar calculation](Yin_C_A0121_v1.md#the-regular-rank-computation).
The last Schur complement is the scalar in the statement, and its nullity equals that of \(C\).
The rank estimate alone need not give equality when a vertex loses rank.

## Two and three states with two vertex contributions on every arrow

Modulo \(9\), \(a\) becomes the identity and multiplication of matrices \(I+3X\) adds their \(X\) coordinates modulo \(3\).
For the two-state example both products \(w_j\) reduce modulo \(9\) to \(I+3(E_{21}+E_{32})\).
For the three-state example both products reduce to \(I+6(E_{21}+E_{32})\).
The unequal closing words \(s_1t_1\) and \(t_2s_2\) contribute the same first-order coordinates in this check, while their actual order remains in the two vertex convolutions.
Both residues are nonidentity.
Also \(\bar s,\bar t,\overline{st},\overline{ts}\) lie outside \(K\), since their off-diagonal entries below the diagonal survive modulo \(5\), whereas \(K\) consists of upper triangular matrices.
The coset-phase choice therefore makes every indicated arrow corner invertible simultaneously.
This verifies a fully occupied cycle on each side for the specified [mixed-word test](../strategies/Yin_S_A0012.md#route).
The estimate uses a single translation per visible arrow at each vertex.
Classifying rank-deficient branches for more general additive entries requires additional information about the vertex corner ranks.

## Assessment history

### Decision two-sided-cycles

| Field | Value |
| --- | --- |
| date | 2026-11-26T03:35 |
| status | proved |
| reason | Independent review verified the complete statement and argument at the specified scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Regular rank, cycle-word hypothesis and the two explicit examples. |
| argument | [Finite representation](#both-cycles-in-the-finite-representation) | Graph weight spaces and simultaneous nonzero corners. |
| argument | [Cycle elimination](#eliminating-each-vertex-cycle) | Product order, torus rank, deficient corners and the regular trace bound. |
| argument | [Applications](#two-and-three-states-with-two-vertex-contributions-on-every-arrow) | Both mixed cyclic inputs and their residues. |
| review | [Two-sided cycles](../audits/reviews/Yin_R_A0174_v1.md#two-sided-cycles) | Independent whole-argument finding on this fixed version. |

## Current assessment

[Selected decision](#decision-two-sided-cycles)

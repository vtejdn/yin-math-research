---
author: Yin
---

# Unitary deformations for triangular chains with a repeated mixed denominator

## Statement

Let \(V_1,V_2\le G\) and take finite-dimensional vertex representations on two auxiliary spaces of the same positive dimension \(d\), as in the [two-weight deformation](Yin_C_A0118_v1.md#regular-trace-identity-and-the-specialization).
More precisely, assume there are infinitely many unit phases \(t\) at which a unitary representation of \(G\) restricts to a fixed \(\pi_1\) on \(V_1\) and to \(D_t\pi_2D_t^{-1}\) on \(V_2\), with \(D_t=\operatorname{diag}(tI_d,I_d)\).
Let \(A=L+R\) be an \(m\)-by-\(n\) matrix, where \(L,R\) are affiliated over the first and second vertex respectively.
Twist each by its fixed unbent vertex representation together with the regular representation of \(G\), and denote the auxiliary corner matrices by \(L_{ij},R_{ij}\).
All ranks below use unnormalized coordinate traces.
Then
\[
             2d\,\operatorname{rk}_G A
                        \ \ge\ \operatorname{rk}_G R_{21}
                                  +\operatorname{rk}_G L_{12}.           \tag{1}
\]
The corner matrices on the right have \(md\) rows and \(nd\) columns.
In the square case two full corners suffice for invertibility.

In particular suppose \(p=p_L+p_R\) has its two indicated vertex corners of full rank \(d\).
For every \(q\ge1\), every strictly upper triangular \(N\in M_q(L^0(\mathcal N(V_1)))\), every vertex-one column \(b\) and vertex-two row \(c\) of compatible size, the scalar
\[
                      p-c(pI_q-N)^{-1}b                                \tag{2}
\]
is an affiliated unit over \(G\).
In particular when \(p_L,p_R,N,b,c\) belong entrywise to inverse layer \(k\) of their respective vertices, (2) at its prescribed finite inverse domain belongs to layer \(k+1\) of \(G\) and has zero kernel.
The conclusion also holds for \(q=0\) with scalar \(p\).
This includes the mixed denominator of the [congruence double](Yin_C_A0121_v1.md#statement) and the [quotient with the conjugated commutation relation](Yin_C_A0122_v1.md#statement).

## A polynomial with affiliated coefficients

At each admissible phase the normal regular twist preserves trace up to the factor \(2d\).
For bounded elements the unitary on each group fiber multiplies by its representation matrix and fixes the identity fiber, as in [the trace proof](Yin_C_A0118_v1.md#regular-trace-identity-and-the-specialization).
It intertwines the amplified spectral projections.
The normal homomorphism extends to affiliated operators, by spectral truncations and polar decomposition, respecting sums and the closure of images.
Restriction to a vertex agrees with its own regular twist by agreement on group elements and normality, including the constant conjugation \(D_t\) for vertex two.

Write the twisted matrix in the two auxiliary coordinates, multiply the second block of output rows by \(t\), and move those rows to the top.
The resulting polynomial is
\[
 F(t)=
 \begin{pmatrix}
 t L_{21}+R_{21} & t(L_{22}+R_{22})\\
 L_{11}+R_{11} & L_{12}+tR_{12}
 \end{pmatrix}.
\]
Its rank agrees with \(2d\,\operatorname{rk}_G A\) at every admissible phase.
At zero the block upper right vanishes.
Its rank is at least the sum of the diagonal ranks, also for rectangular blocks: projection of its closed range onto the first output coordinates has range closure of rank \(\operatorname{rk} R_{21}\), and the kernel of this restricted projection contains the closed range of \(L_{12}\) in the second output coordinates.
This dimension calculation takes place on affiliated modules, or after clearing left denominators.

For that clearing, choose one bounded operator \(s\in\mathcal N(G)\) invertible in the affiliated algebra such that every one of the finitely many scalar coefficient entries \(a\) has \(sa\) bounded.
For example take the inverse square root of \(1+\sum aa^*\) as in the [common denominator construction](Yin_C_F0068_v1.md#argument).
Left multiply all output coordinates by \(s\), preserving all the displayed ranks at every complex parameter.
The resulting polynomial has bounded coefficients and degree at most one.
For any \(k>1\) distinct admissible phases, the [finite-evaluation inequality](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) bounds \( (k-1)\operatorname{rk}_G F(0)\) by the sum of the ranks at those phases.
Division by \(k\) and passage to infinity prove (1).
No division or approximation by a nonunitary group representation at \(t=0\) is involved.

## The finite inverse layer

Apply (1) first to \(p\), proving that \(p\) is a unit.
Apply it next to the square border \(\left(\begin{smallmatrix}p I_q-N&b\\c&p\end{smallmatrix}\right)\).
Allocate the terms \(-N,b\) to the left vertex and \(c\) to the right.
Its \(L_{12}\) corner is block upper triangular with \(q+1\) copies of the full scalar-input corner of \(p_L\) on the diagonal.
Its \(R_{21}\) corner is block lower triangular with the analogous copies for \(p_R\).
Both are affiliated units, so the border has full rank.
The inside block \(pI_q-N\) has a finite upper triangular inverse with entries in the algebra generated by \(p^{-1}\) and the entries of \(N\).
Elimination gives (2).
Subgroup inclusions preserve each finite inverse layer and therefore the repeated-inverse expression has the claimed depth bound. [Chain realization](Yin_C_A0117_v1.md#chain-realization-and-rank)
In the unrestricted layer test \(c,b,N\) can involve overlapping groups and the last diagonal entry can be arbitrary.
Those inputs need not have full corner matrices in (1).

## Assessment history

### Decision mixed-denominator-chain-ranks

| Field | Value |
| --- | --- |
| date | 2026-11-22T04:54 |
| status | proved |
| reason | Independent review verifies the full statement and argument under the specified assumptions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A lower bound from two auxiliary corner ranks for rectangular affiliated input, and full rank for repeated-denominator chains of every finite length with the specified vertex coefficients. |
| argument | [Proof](#a-polynomial-with-affiliated-coefficients) | Trace preservation of the affiliated twists, denominator clearing for specialization and the triangular corner ranks of every border. |
| review | [Whole finding](../audits/reviews/Yin_R_A0160_v1.md#whole-finding) | Independent whole-argument finding at the stated scope. |

## Current assessment

[Selected decision](#decision-mixed-denominator-chain-ranks)

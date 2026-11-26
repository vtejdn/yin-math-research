---
author: Yin
---

# Two actual Schur pivots can witness every visible index-four character together

## Statement

Use the [order-twenty half-kernel hypotheses and the common sign kernel \(N\)](Yin_C_A0344_v1.md#statement).
Let \(R\) be the four-square commutator on \(N\), of regular rank two, and put \(A=\mathbb C N\).
Call a marking character \(\psi\) visible if its ordinary rank \(r_\psi=\operatorname{rank}\psi(R)\) is at least three.
The [character detection theorem](Yin_C_A0343_v1.md#statement) gives at least one such character.
There are at most five, and \(N_{\mathrm{ab}}=C_5\).

There are constant invertible changes of row and column coordinates on \(R\) and a leading two-square submatrix \(D\) which is invertible in \(M_2(U(N))\) as well as at every visible character.
A first group-ring pivot \(a\) and its next scalar Schur pivot \(b\in A[a^{-1}]\) are affiliated units and have nonzero formal numerical values at all those characters.
Over \(A[a^{-1}][b^{-1}]\) the whole \(R\) has inner rank two.
Its two-square Schur complement after the elimination vanishes entrywise in this actual ring, while the same four rational expressions evaluated at \(\psi\) have rank \(r_\psi-2\).
In particular, a visible three-square minor always realizes the last branch of the [two-pivot alternative](Yin_C_A0344_v1.md#two-scalar-pivot-decisions) after constant changes of coordinates.
The third row and column extending \(D\) may depend on the character.

For a single visible character every initial group-ring entry in the resulting four-square matrix can be taken to have at most four group labels.
For simultaneous pivots the same bound holds outside one row, whose entries have at most six.
The entire matrix still uses the [same eight labels](Yin_C_A0331_v1.md#two-involutions-with-a-polynomial-commutator).
These bounds refer to the matrix before rational elimination.
The proof selects constant combinations inside the four coordinates; it gives no invertibility assertion for an arbitrarily prescribed pair of original rows and columns.

## Two-dimensional input and output spaces

Write \(m=(st)^{-1}\), \(J_j=\left(\begin{smallmatrix}0&jI_2\\j^{-1}I_2&0\end{smallmatrix}\right)\) for \(j=s,t\), and \(L=TJ_tT^{-1}\) for the original constant assembly \(T\).
Thus \(R=m[J_s,L]\), with the scalar translation acting on all four coordinates.
For any nonzero constant column \(v\in\mathbb C^2\) and row \(w\in(\mathbb C^2)^*\) define
\[
 V_v=T\begin{pmatrix}v&0\\0&v\end{pmatrix},
 \qquad U_w=\begin{pmatrix}w&0\\0&w\end{pmatrix}T^{-1}.
\]
We prove that \(D_{w,v}=U_wR V_v\) is an affiliated unit matrix for every such pair.

The [normalized basis for the kernel of \(R\)](Yin_C_A0331_v2.md#constructing-the-basis-and-checking-both-actions) has a constant left inverse formed by selecting the second coordinate of each of the two pairs after \(T^{-1}\), in reversed pair order.
Hence the kernel meets the plane \(V_{e_1}U(H)^2\) trivially: on this plane both selected coordinates vanish, while on the kernel they determine the vector.
For arbitrary \(v\ne0\) choose a numerical invertible matrix \(C\) with first column \(v\).
The assembly \(T\operatorname{diag}(C,C)\) leaves \(L\), hence \(R\), unchanged and replaces each signed rectangle by its product on the right with \(C\).
The half kernels are preserved, so the same normalized-basis result applied in these coordinates proves that \(R V_v\) has rank two for every \(v\ne0\).

Use the dual assembly \(T_\dagger=(T^{-1})^*\), for which \(T_\dagger J_tT_\dagger^{-1}=L^*\).
It again satisfies the four-sign half-kernel hypotheses.
Indeed at each pair of signs the two eigenspaces of \(J_s^*,L^*\) are the orthogonal complements of the two original eigenspaces at the opposite signs.
Those planes each have dimension two and their intersection has dimension \(1/2\).
The dimension of the joint orthogonal complement is thus \(4-(2+2-1/2)=1/2\), and the dual graph formula identifies the resulting half kernels. [Dual planes in the four-sign construction](Yin_C_A0331_v1.md#two-involutions-with-a-polynomial-commutator)

The dual commutator satisfies \(R_\dagger=m[J_s,L^*]=-m R^* m\), since \(J_s\) is selfadjoint.
The input plane \(T_\dagger\operatorname{diag}(w^*,w^*)U(H)^2=U_w^* U(H)^2\) is preserved by the scalar translation \(m\) and its inverse.
Injectivity of \(R_\dagger\) on this plane therefore yields injectivity of \(R^*U_w^*\).
Consequently \(U_w R\) has rank two.
Since \(R V_v\) has the full rank of \(R\), its image has the same closure as that of \(R\); applying the bounded map \(U_w\) preserves equality of these image closures after taking closure.
It follows that \(D_{w,v}\) has rank two.
Its group-ring entries belong to \(A\), so the regular subgroup rank formula gives rank two on \(N\) as well.
A full-rank square matrix in the finite affiliated algebra is invertible there.

## Simultaneous numerical rank for the same input and output spaces

Extend each visible \(\psi\) to a marking character on \(H\), and denote its values on \(s,t\) by \(x,y\).
Such extensions come from \(H_{\rm ab}=C_5\times C_2^2\) by the [subgroup identification](Yin_C_A0344_v1.md#the-subgroup-and-a-full-numerical-minor).
Over this character the matrix \(T^{-1}\psi(R)T\) is \((xy)^{-1}\) times the additive commutator of \(T^{-1}J_xT\) with \(J_y\).
It anticommutes with \(J_y\) since \(J_y^2=I\).
In coordinates consisting of the positive and negative eigenspaces of the two-position numerical involution \(\left(\begin{smallmatrix}0&y\\y^{-1}&0\end{smallmatrix}\right)\), this gives a block matrix
\[
                      \begin{pmatrix}0&A_\psi\\ B_\psi&0\end{pmatrix}.
\]
Each off-diagonal block acts on the two fiber coordinates.
Both blocks are nonzero since their ranks add to \(r_\psi\ge3\).
The maps duplicating \(v,w\) on the two positions commute with the position coordinate change, with the corresponding change also on the two coordinates of \(D_{w,v}\).
It follows that \(\psi(D_{w,v})\) is invertible exactly when \((w A_\psi v)(w B_\psi v)\ne0\).

Let \(k\) be the number of visible characters.
A nonzero two-square matrix annihilates at most one vector of the form \((1,j)^{\mathsf T}\) as \(j\) varies.
Choose \(j\in\{0,\ldots,2k\}\) so that all \(2k\) block images of \(v=(1,j)^{\mathsf T}\) are nonzero.
Choose \(i\) from the same integer set so that \(w=(1,i)\) annihilates none of these vectors.
Complete \(v,w\) to constant column and row bases using \(e_2,e_2^{\mathsf T}\).
After processing the two positions in each fiber first, these bases furnish four rows and four columns of an invertible coordinate change whose leading two-square block is \(D_{w,v}\).

In the unsheared coordinates every row has a fixed output position and every column has a fixed input position.
Indeed the four blocks of \(T^{-1}R T=m[T^{-1}J_sT,J_t]\) have this property before choosing the fiber vectors.
All entries of \(T^{-1}J_sT\) are supported on \(s^{\pm1}\), and \(J_t\) has one nonzero position per row and per column.
Each fixed block of the commutator therefore uses at most the four words \(ms^{\pm1}t^{e},mt^{f}s^{\pm1}\), where \(e,f\in\{1,-1\}\) are fixed by that column and row respectively.
The changes of fiber coordinates within these blocks preserve their supports.

For a single character use row and column permutations within \(D_{w,v}\) so its first pivot \(a\) has nonzero character value.
For several visible characters one can take the first row plus \(\lambda\) times the second as the new first row, retaining the second.
The evaluated first column of \(D_{w,v}\) is nonzero at every visible character, so \(\lambda\in\{0,\ldots,k\}\) avoids the at most \(k\) zeros of the new first entries.
For each fixed column only the left-position exponent \(f\) can now take both signs, giving at most six labels within that first row.
The leading block remains an affiliated unit after each of these constant changes.

## Two actual inverses and the formal remainder

The first pivot \(a\) is a group-ring scalar and has nonzero values at the selected visible characters.
It is an affiliated unit by scalar injectivity.
Eliminating it in \(D=D_{w,v}\) after the prescribed permutations or shear gives the scalar \(b=D_{22}-D_{21}a^{-1}D_{12}\).
The invertibility of the two-square block implies \(b\) is an affiliated unit, and the ordinary nonzero block determinant implies \(b(\psi)=\det D(\psi)/\psi(a)\ne0\).
Write the full four-square matrix in these coordinates as \(\left(\begin{smallmatrix}D&E\\F&G\end{smallmatrix}\right)\).
Then \(D^{-1}\) belongs to the ring with the two successive inverses, and block elimination gives
\[
                             G-FD^{-1}E=0
\]
in that ring, since the whole regular rank is two and the leading block accounts for both dimensions.
The same operations give a two-column factorization of \(R\) there, and its regular rank supplies the matching lower bound for inner rank.

Instead take the formal unital algebra obtained by universally adjoining \(a^{-1}\), followed by the inverse of the resulting Schur word \(b\).
Every visible character under consideration extends to these two universal steps by its nonzero scalar pivot values.
Its evaluation on the displayed two-square expression then has rank \(r_\psi-2\), by ordinary numerical elimination.
In particular some entry is nonzero and extends the leading block to a numerically invertible three-square minor using the corresponding remaining row and column, whereas the actual regular rank of that minor is two.
When \(r_\psi=4\) the whole formal remainder is numerically invertible.

## Assessment history

### Decision simultaneous-actual-pivots-on-the-common-sign-subgroup

| Field | Value |
| --- | --- |
| date | 2026-11-26T18:53 |
| status | proved |
| reason | Constant input and output planes give an actual invertible two-square block at every visible character and a rank-two factorization after two scalar inversions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Constant input and output planes give an actual invertible two-square block at every visible character and a rank-two factorization after two scalar inversions. |
| argument | [Two-dimensional input and output spaces](#two-dimensional-input-and-output-spaces) | Two-dimensional input and output spaces. |
| argument | [Simultaneous numerical rank for the same input and output spaces](#simultaneous-numerical-rank-for-the-same-input-and-output-spaces) | Simultaneous numerical rank for the same input and output spaces. |
| argument | [Two actual inverses and the formal remainder](#two-actual-inverses-and-the-formal-remainder) | Two actual inverses and the formal remainder. |
| dependency | [First pivot alternative](Yin_C_A0344_v1.md#statement) | The actual subgroup and the original nested-minor test. |
| review | [Two actual pivots over the index-four subgroup](../audits/reviews/Yin_R_A0236_v1.md#two-actual-pivots-over-the-index-four-subgroup) | The preceding version was independently inspected. |
| review | [Simultaneous actual pivots on the common sign subgroup](../audits/reviews/Yin_R_A0237_v1.md#simultaneous-actual-pivots-on-the-common-sign-subgroup) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-simultaneous-actual-pivots-on-the-common-sign-subgroup)

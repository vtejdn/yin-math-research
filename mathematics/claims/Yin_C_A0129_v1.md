---
author: Yin
---

# Odd stabilization and the unit class in two inverse layers

## Statement

Let \(R\) be any unital complex algebra and \(K_0(R)\) the Grothendieck group of its finitely generated projective right modules.
The following are equivalent.

1. The class \([R]\) belongs to \(2K_0(R)\).
2. For some positive odd integer \(n\) there are matrices \(J,X\in M_n(R)\) with \(J^2=I_n\), \(X\) invertible, and \(XJX^{-1}=-J\).
3. The matrices in item 2 can be chosen with \(X^2=I_n\).

For a discrete group \(H\), write \(D_0(H)=\mathbb CH\) and form \(D_{j+1}(H)\) by adjoining inverses of the elements of \(D_j(H)\) invertible in the actual affiliated algebra \(U(H)\).
If \([1]\in2K_0(D_2(H))\), a single square positive matrix over \(\mathbb CH\) has von Neumann nullity \(n/2\) for some positive odd \(n\).
Here and below matrix ranks and nullities use the unnormalized matrix trace.
If \(L\le H\) has finite odd index \(n\), then
\[
 [1]\notin2K_0(D_{2n}(L))\quad\Longrightarrow\quad [1]\notin2K_0(D_2(H)).
\]
All three statements hold without an Atiyah integrality hypothesis.
They apply in particular to the half-dimensional Schur-kernel question for [A0001](../tasks/Yin_T_A0001_v1.md#contract).

## Odd stabilization

Suppose \([R]=2([E]-[F])\), where \(E,F\) are finitely generated projective right modules.
By the definition of the group completion, \(R\oplus F^{\oplus2}\oplus V\simeq E^{\oplus2}\oplus V\) for a finitely generated projective \(V\).
Add a complement for \(V\) to both sides, then add one free coordinate to both if necessary, so \(V\) is replaced by a free module \(R^k\) of even rank.
Choose \(F'\) with \(F\oplus F'\simeq R^s\).
Adding two copies of \(F'\) gives
\[
 R^{1+2s+k}\simeq (E\oplus F'\oplus R^{k/2})^{\oplus2}.
\]
On this pair of isomorphic summands take \(J\) to act as \(1,-1\) and \(X\) to interchange the summands.
Transport them to the odd-rank free module to obtain item 3, which immediately gives item 2.

Conversely \(e=(I_n+J)/2\) and \(f=I_n-e\) are complementary idempotents.
The conjugation by \(X\) identifies their projective modules, so \(n[R]=2[eR^n]\).
Writing \(n=2h+1\) gives \([R]=2([eR^n]-h[R])\).
A unital representation of the ring containing the witness into \(M_d(K)\) for a division ring \(K\) and odd \(d\) would give the two complementary idempotents equal ranks in odd total dimension \(nd\), which is impossible.

## A positive matrix over the original group ring

Take an odd certificate \(J,X\) for \(R=D_2(H)\).
The same two complementary idempotents become isomorphic projective summands over \(U(H)\).
The von Neumann dimension of the range of \(e\) is therefore \(n/2\), by additivity and invariance under an affiliated isomorphism.

We record explicitly how to use the finite inverse expressions in these idempotents.
Each evaluated entry is of the form \(cM^{-1}b\), where \(c,M,b\) are a row, square matrix and column over \(\mathbb CH\), and \(M\) is invertible over \(U(H)\).
A group-ring entry has this form with \(M=(1)\).
Addition uses a block diagonal \(M\) and the concatenated rows and columns.
For a product of entries with data \((c_i,M_i,b_i)\), use
\[
 M=\begin{pmatrix}M_1&-b_1c_2\\0&M_2\end{pmatrix},
 \qquad c=(c_1,0),\qquad b=(0,b_2)^{\mathsf T},
\]
where the last notation stacks block columns.
The new matrix is invertible by its triangular form and gives the factors in the specified order.
If \(r=cM^{-1}b\) is an allowed scalar denominator, the block matrix with rows \((M,b),(-c,0)\) is invertible since its second Schur pivot is \(r\).
The bottom-right entry of its inverse is \(r^{-1}\).
These operations cover the finite expressions actually used and require no specialization to another representation.

Take the direct sum \(M\) of these entrywise denominators, and place each row block and column block at its corresponding output and input coordinate.
This gives \(e=CM^{-1}B\) over \(U(H)\) and \(m\) is the size of \(M\).
Then the square group-ring matrix
\[
 Z=\begin{pmatrix}M&B\\-C&0\end{pmatrix}
\]
has rank \(m+n/2\) by elimination at \(M\).
Thus \(Z^*Z\) is a positive group-ring matrix with nullity \(n/2\).
The size \(m+n\) depends on a particular finite certificate and its inverse expressions.

For a conditional relative \(K_0\) obstruction let \(i\colon K_0(\mathbb CH)\to K_0(R)\) be extension of scalars.
The von Neumann dimension defines an additive real-valued map on \(K_0(R)\) by extension to \(U(H)\), since every short exact sequence of finitely generated projectives with projective quotient splits.
If \(1/2\) does not belong to the trace image of \(i\), then any \(x\in K_0(R)\) with \(2x=[R]\) maps to an element of exact order two in the cokernel of \(i\).
Indeed the dimension of \(x\) is \(1/2\), while \(2x\) comes from the group-ring unit.
This deduction requires the stated restriction on the trace image.

## Finite-index transfer with a depth bound

Let \(L\le H\) have finite index \(n\) and choose representatives of the left cosets of \(L\).
The right \(L\)-coordinate description gives a normal embedding \(\mathcal N(H)\to M_n(\mathcal N(L))\) sending \(\mathbb CH\) into \(M_n(\mathbb CL)\).
Its extension to affiliated operators preserves products, adjoints and actually available inverses.

For any \(j\) and any \(n\)-by-\(n\) matrix \(A\) over \(D_j(L)\) invertible over \(U(L)\) in matrix size \(n\), one has
\[
 A^{-1}\in M_n(D_{j+n}(L)).
\]
Indeed each \(D_j\) is closed under adjoints by induction.
For the kernel projection \(p\) of the first diagonal entry, positivity gives \((A^*A)^{1/2}e_1p=0\), where \(e_1\) is the first-coordinate column.
Injectivity of \(A^*A\) forces \(p=0\).
This diagonal entry is an affiliated unit, and its inverse lies in \(D_{j+1}\).
One Schur congruence leaves a positive full matrix with entries in \(D_{j+1}\).
Induction on size gives the inverse of this matrix by at most \(n-1\) more layers.
Undoing the elimination gives \((A^*A)^{-1}\), and \((A^*A)^{-1}A^*=A^{-1}\).
The same reasoning works for unbounded entries with the algebraic operations in \(U(L)\).

Apply the matrix inverse bound to the image of each denominator over \(D_0(H)\), and then to each denominator over \(D_1(H)\).
This maps \(D_2(H)\) into \(M_n(D_{2n}(L))\).
Composing the induced map on \(K_0\) with the matrix Morita identification sends the source unit class to \(n[D_{2n}(L)]\).
For odd \(n\) this equals the target unit class modulo \(2\), which proves the claimed implication.
The estimate allows a change of depth even when only scalar inverses are used in the source.

## A torsion-free calibration for multiplicative commutators

Let \(K=\langle u,v\mid vuv^{-1}=u^{-1}\rangle=\mathbb Z\rtimes\mathbb Z\) and \(H=K*\mathbb Z\).
The group \(K\) is torsion-free by the semidirect product description, and \(H\) is torsion-free by free product normal form.
The homomorphism \(H\to K\) killing the added generator has free kernel, the free product of the cyclic groups generated by its conjugates under \(K\).
Since \(K\) is elementary amenable, \(H\) is in [Linnell's class](../ledger/Yin_L_A0001_v1.md), so \(D_\infty(H)\) is a skew field.
The induced rank map \(K_0(D_2(H))\to K_0(D_\infty(H))=\mathbb Z\) sends the unit to one and excludes divisibility by two.

Nevertheless \(z=u-u^{-1}=u^{-1}(u^2-1)\) is a unit in \(D_1(H)\).
Indeed \(u^2\) has infinite order, so the regular translation by \(u^2\) has no nonzero invariant square-summable vector.
Conjugation gives \(v z v^{-1}=-z\), so \(v z v^{-1}z^{-1}=-1\).
Thus the class of the scalar unit \(-1\) already vanishes in \(K_1(D_1(H))\), while the unit class in \(K_0(D_2(H))\) has odd image in \(\mathbb Z\).
The involution equation \(J^2=I_n\) in the odd certificate supplies information that the ordinary anticommutation of units does not detect.

## Assessment history

### Decision parity-certificates

| Field | Value |
| --- | --- |
| date | 2026-11-23T07:16 |
| status | proved |
| reason | Independent inspection verified the complete statement, its arguments and the stated limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Odd stabilization, a half-integer positive matrix and depth transfer. |
| argument | [Odd stabilization](#odd-stabilization) | Stable complements and conjugate eigensummands. |
| argument | [Group-ring realization](#a-positive-matrix-over-the-original-group-ring) | Finite rational linearization and the relative cokernel condition. |
| argument | [Transfer](#finite-index-transfer-with-a-depth-bound) | Positive pivots and the effect of an odd index on the unit class. |
| argument | [Klein bottle calibration](#a-torsion-free-calibration-for-multiplicative-commutators) | A commutator at depth one and indivisibility of the unit. |
| review | [Independent finding](../audits/reviews/Yin_R_A0164_v1.md#parity-certificates) | Whole argument at the stated scope. |

## Current assessment

[Selected decision](#decision-parity-certificates)

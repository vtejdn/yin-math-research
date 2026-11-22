---
author: Yin
---
# Finite-support syzygies at the first noninteger matrix size

## Statement

Let \(B=\mathbb CG\) for a discrete group \(G\), acting by left convolution, and let \(U\) be the algebra of operators affiliated to its group von Neumann algebra.
Write \(\operatorname{rk}D\) for the von Neumann dimension of the closed image, using the canonical trace and the unnormalized matrix trace.
For a group-ring matrix \(D\) with \(q\) columns, let \(K_{\rm fin}(D)\) be the closed linear span in \(\ell^2(G)^q\) of all columns \(w\in B^q\) with \(Dw=0\).
This subspace is invariant under right translations.

Every finite group-ring matrix of noninteger rank contains an entry submatrix of size \(n\times n\) with rank in \((n-1,n)\).
Consequently, if there is any failure of integrality, there is a smallest failing square size \(n\), and every group-ring matrix with fewer than \(n\) rows or fewer than \(n\) columns has integer rank.
Every \(A\in M_n(B)\) of noninteger rank at this size has \(\operatorname{rk}A\in(n-1,n)\).

Suppose \(n\ge2\), fix such an \(A\), and let \(1\le k<n\).
For **every** group-ring \(k\times n\) matrix \(X\) of analytic rank \(k\),
\[
 \dim_G\ker(XA)=n-k,\qquad
 \dim_G K_{\rm fin}(XA)\in\{0,\ldots,n-k-1\}.
 \tag{1}
\]
The same assertions apply to \(A^*\) and hence to left relations on column combinations of \(A\).
In particular each full-rank \((n-1)\)-row combination has analytic nullity one and zero finitely supported kernel.
More generally, if \(Y\in M_{n,n-k}(B)\) has rank \(n-k\), then \(XAY\ne0\).

At size two suppose only that every nonzero element of \(B\) is injective on \(\ell^2(G)\).
Write \(A=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\) with \(a\ne0\) and put \(s=d-ca^{-1}b\in U\).
If there are a nonzero group-ring row \(u\) and a nonzero group-ring column \(v\) with \(uAv=0\), then \(s=0\) or \(s\) is a unit of \(U\).
If \(0<\operatorname{rk}s<1\), every nonzero row \(u\) gives a pair \((r_1,r_2)=uA\) which freely generates a unital associative algebra on two generators in \(B\).
It also gives an injection \((x,y)\mapsto r_1x+r_2y\) from the free right module \(B^2\) to \(B\).

There is a finite-dimensional test for the same Schur alternative.
For any two nonzero finite-dimensional complex spaces \(E\subseteq B^{1\times2}\), \(F\subseteq B^{2\times1}\), let \(W=\operatorname{span}_{\mathbb C}\{uAv:u\in E,\ v\in F\}\).
If
\[
 \dim_{\mathbb C} W<\dim_{\mathbb C} E+\dim_{\mathbb C} F-1 ,
 \tag{2}
\]
then \(s=0\) or \(s\) is a unit.
In particular an obstruction \(0<\operatorname{rk}s<1\) requires
\[
 |H S J|\ \ge\ 2|H|+2|J|-1
 \tag{3}
\]
for all finite nonempty \(H,J\subset G\), where \(S\) is the union of the four entry supports of \(A\).
The test (2) uses the actual output coefficient span, which may have smaller dimension than \(\mathbb C[HSJ]\).
These are conditional restrictions for [A0001](../tasks/Yin_T_A0001_v1.md#contract).

## Argument

### Finding a smallest fractional submatrix

Choose a submatrix \(C\) minimal under row and column deletions among the submatrices of noninteger rank of the given input.
Write \(\operatorname{rk}C=h+\delta\), where \(h\) is an integer and \(0<\delta<1\).
Adding one row or column increases analytic rank by a number in \([0,1]\), by dimension additivity for closed spans and the equality of the ranks of a matrix and its adjoint.
If a column gives zero increase, its closed image is already contained in the previous closed image, by faithfulness of the trace.
These facts use the [finite-trace rank calculus](../audits/literature/MSY23/Yin_U004.md#msy23-u004).

Delete one column of \(C\).
The resulting rank is integral by minimality, so it equals \(h\).
Add the columns of this deletion successively, keeping a column precisely when it increases rank.
All ranks encountered are integers by minimality, and zero increases leave the previous closed span unchanged.
Thus exactly \(h\) columns suffice for the whole closed image of the deletion.
Putting back the omitted column gives rank \(h+\delta\) using \(h+1\) columns, so minimality forces \(C\) to have \(h+1\) columns.
Applying the same argument to \(C^*\) gives \(h+1\) rows.
This also works when \(h=0\), using the rank-zero empty matrix.
A rectangular counterexample with one side smaller than the smallest failing square size would now contain a smaller failing square.
At the smallest failing square size, a matrix of noninteger rank must itself be the square found by the deletion argument.

### Full row and column combinations cannot annihilate each other

For \(X\) as in (1), restriction of \(X\) to the closed image of \(A\) loses at most \(\dim_G\ker X=n-k\) dimensions.
Hence \(\operatorname{rk}(XA)\ge\operatorname{rk}A-(n-k)>k-1\).
Since \(XA\) has just \(k<n\) rows, its rank is integral and therefore equals \(k\).
Its nullity is \(n-k\).

Rectangular integrality also allows us to extend \(X\) to an \(n\times n\) matrix \(P\) over \(B\), invertible in \(M_n(U)\), with first \(k\) rows \(X\).
Indeed, the same greedy column selection gives \(k\) columns of \(X\) forming a square of rank \(k\).
After a column permutation, write \(X=(X_0,X_1)\) with \(X_0\) this square.
Appending the coordinate rows \((0,I_{n-k})\) gives a block triangular matrix invertible over \(U\), since \(X_0\) is an affiliated unit.
Undo the column permutation.
Similarly extend any full-column-rank \(Y\in M_{n,n-k}(B)\) to a polynomial matrix \(Q\) invertible over \(U\), with \(Y\) its last \(n-k\) columns.

If \(XAY=0\), write
\[
 PAQ=\begin{pmatrix}D&0\\ T&H\end{pmatrix},
 \qquad D\in M_k(B),\quad H\in M_{n-k}(B).
 \tag{4}
\]
The top row block has rank \(\operatorname{rk}D\), and adding the last \(n-k\) rows can increase it by at most \(n-k\).
Since \(\operatorname{rk}(PAQ)=\operatorname{rk}A>n-1\), this gives \(\operatorname{rk}D>k-1\).
The same argument using the last \(n-k\) columns gives \(\operatorname{rk}H>n-k-1\).
Each diagonal block has smaller square size, so each is full and invertible over \(U\).
The triangular matrix in (4) would then be invertible over \(U\), contradicting \(\operatorname{rk}A<n\).

Start with no columns and adjoin a polynomial syzygy of \(XA\) whenever its closed image increases the span of the columns already selected.
For any list of at most \(n-k\) such columns the matrix rank is integral, as it has fewer than \(n\) columns.
Every positive increase therefore adds one.
If \(n-k\) columns were selected, they would form a matrix \(Y\) forbidden by (4).
Hence selection terminates with an integer \(j\le n-k-1\), and the closed image of the selected columns contains the image of each polynomial syzygy.
The closed image of one such column is the closed span of its right translates, since finitely supported inputs are dense and the column acts boundedly.
It follows that the selected closed image equals \(K_{\rm fin}(XA)\), proving (1).
In the amenable case [complete kernel localization](Yin_C_A0001_v2.md#proof-of-complete-rational-kernel-localization) gives equality with the whole kernel, excluding (1).

### The two-by-two Schur complement

The scalar hypothesis makes every nonzero entry and ratio denominator used as a pivot a unit of \(U\).
The two elementary triangular operations about \(a\) give \(\operatorname{rk}A=1+\operatorname{rk}s\).
If \(0<\operatorname{rk}s<1\), then \(A\) has first failing square size two, and (4) with \(k=1\) applies to every nonzero \(u,v\), each of analytic rank one.
Consequently \(uAv\ne0\).
The contraposition gives the first Schur alternative because a scalar of rank zero vanishes and a scalar of rank one is an affiliated unit.
One direct witness arises from a common right multiple \(ap=bq\) with \((p,q)\ne(0,0)\), by taking \(u=(1,0)\) and \(v=(p,-q)^t\).
Left common multiples and witnesses obtained by combining both rows and columns are covered by the same argument.

For a nonzero \(u\), the absence of a zero pair makes \((r_1,r_2)=uA\) an injective map \(B^2\to B\) on finite columns.
Its image \(r_1B+r_2B\) is a proper right ideal.
Indeed if it were all of \(B\), this map would be a right module isomorphism \(B^2\simeq B\).
Tensoring this isomorphism with the left augmentation module \(\mathbb C\) would give \(\mathbb C^2\simeq\mathbb C\).
Any polynomial relation on \(r_1,r_2\) can be written \(c+r_1p(r_1,r_2)+r_2q(r_1,r_2)=0\) by separating the empty word and the first letter.
A nonzero scalar \(c\) would put \(1\) in the proper ideal.
Thus \(c=0\), and injectivity gives \(p(r_1,r_2)=q(r_1,r_2)=0\).
Induction on the maximum word length shows that all coefficients vanish.
In particular for each finite nonempty \(J\subset G\), injectivity of this row on \(\mathbb C[J]^2\) gives \(|(\operatorname{supp}r_1\cup\operatorname{supp}r_2)J|\ge2|J|\).

For (2), form the complex linear map \(L:E\otimes F\to W\) induced by \(u\otimes v\mapsto uAv\).
If \(\dim W\le\dim E+\dim F-2\), its kernel contains a nonzero decomposable tensor.
This is the two-factor case of [Parthasarathy, Proposition 1.4, arXiv v1, pp. 5–6](../literature/pdf/Par04--arxiv-v1.pdf#page=5).
Indeed the Segre variety has dimension \(\dim E+\dim F-2\) and \(\mathbb P(\ker L)\) has codimension \(\dim W\) in \(\mathbb P(E\otimes F)\).
The [projective dimension theorem used in L40](../ledger/Yin_L_A0040_v1.md) gives an intersection.
Hence \(uAv=0\) for some nonzero \(u,v\).
Taking both coordinates of \(E\) supported on \(H\) and both coordinates of \(F\) supported on \(J\) gives \(W\subseteq\mathbb C[HSJ]\), proving (3).

## Two integral ranks with no finite zero pair

Let \(G=F(x,y)\times\langle t\rangle\) with \(t\) of infinite order.
This torsion-free free-by-cyclic group satisfies the scalar hypothesis by [Linnell's theorem](../audits/literature/Lin00/Yin_U004.md).
In \(B_0=\mathbb C F(x,y)\) set \(r=(x-1,y-1)\), \(c=r^*\), and over \(B=B_0[t,t^{-1}]\) set
\[
 A_0=cr,\qquad A_1=cr+10t I_2.
\]
The [free-tree boundary calculation](../ledger/Yin_L_A0002_v1.md#denominator-clearing-and-finite-propagation) shows that \(rv\ne0\) for every nonzero \(v\in B_0^2\).
Indeed a finite edge chain of boundary zero on a tree vanishes by removal of leaf edges.
Taking adjoints gives \(uc\ne0\) for each nonzero \(u\in B_0^{1\times2}\).
The group algebra \(B_0\) is a domain by the scalar hypothesis, so \((uc)(rv)\ne0\) for every such pair.
For any nonzero Laurent row \(u\) and column \(v\) over \(B_0\), take their coefficients \(u_i,v_j\) of least \(t\)-degree.
In both \(uA_0v\) and \(uA_1v\) the coefficient of \(t^{i+j}\) is \((u_ic)(rv_j)\ne0\).

The factorization of \(A_0\) bounds its rank by one, and its upper left entry \((x-1)^*(x-1)\ne0\) has rank one, giving equality.
Since \(\|cr\|=\|r\|^2\le8\), the perturbation of \(10tI_2\) by \(cr\) has a bounded inverse by the Neumann series.
Thus \(A_1\) has rank two.
Both matrices have a nonzero upper left entry and pass every necessary nonvanishing and expansion test above, while their Schur complements have ranks zero and one respectively.
The remaining step for a general group is to exclude a proper nonzero analytic kernel in the case where all the polynomial pairings survive.

## Assessment history

### Decision finite-syzygy-defect

| Field | Value |
| --- | --- |
| date | 2026-11-22T04:17 |
| status | proved |
| reason | Independent review verified the full argument at the stated hypotheses and bounds. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Size-minimal fractional rank, missing finite kernel dimension, and finite two-sided criteria for the first Schur complement. |
| argument | [Proof](#argument) | Submatrix descent, polynomial row and column completions, tensor dimension and the two regular examples. |
| review | [Whole finding](../audits/reviews/Yin_R_A0150_v1.md#whole-finding) | Independent whole-argument finding for the stated scope. |

## Current assessment

[Selected decision](#decision-finite-syzygy-defect)

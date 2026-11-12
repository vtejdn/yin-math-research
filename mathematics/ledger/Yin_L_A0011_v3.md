---
author: Yin
---
# Equal common powers and the next central-column separation

This continuing investigation develops the exact central-column separation in [L_A0011 v2](../ledger/Yin_L_A0011_v2.md#central-columns-expose-the-next-row-separation-condition) toward the full [A0001 contract](../tasks/Yin_T_A0001_v1.md#contract).
It asks what equal cube and fourth powers of actual torsion-free group labels force on the rationally conjugated row difference, including cyclic permutation extensions over arbitrary torsion-free coefficient groups.
The investigation distinguishes independently certified inverses, exact mergers, unresolved rational separations and an actual kernel-preserving encoding of arbitrary finite matrices.
The first two certified pivots, their affiliated-ring domain interpretation and their exact rank bookkeeping are reused from the fixed input and its [independent review](../audits/reviews/Yin_R_A0013_v2.md#whole-artifact-finding).
No full-Task reduction or general later-pivot theorem is assumed.

## The full-contract trial and the actual inputs

The proposed complete chain starts with an arbitrary torsion-free group \(H\) and an arbitrary \(A\in M_{m,n}(\mathbb CH)\), with unnormalized matrix traces.
It would have to encode the kernel dimension of \(A\) in a common-power reciprocal array by actual independently invertible matrix operations, with every added identity or zero coordinate accounted for.
One could first embed \(H\) in a specified torsion-free group, since the [Task's subgroup argument](../tasks/Yin_T_A0001_v1.md#reduction-to-finitely-generated-groups) preserves its original kernel dimension.
The first unsupported step remains that encoding.
The tensor-coordinate construction below supplies an exact rank interface for a restricted class of matrices, but does not supply the needed arbitrary-input map.
Even on that restricted class, its three-square scalar residual remains unresolved for general \(H\).
Thus neither a general later-pivot induction nor a completion of A0001 follows from the positive calculations here.

The reused actual-ring tools are the [cyclic unit certificate](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions), [finite affiliated Schur interface](../ledger/Yin_L_A0009_v1.md#the-exact-size-reducing-step), and [central-column shape and rank formula](../ledger/Yin_L_A0011_v1.md#a-shape-invariant-with-central-column-parameters).
The [fixed v2 discussion](../ledger/Yin_L_A0011_v2.md#central-columns-expose-the-next-row-separation-condition) already contains the common-degree geometric expansion, but only records the resulting rank upper bound.
These interfaces and their [independent v2 review](../audits/reviews/Yin_R_A0013_v2.md#whole-artifact-finding) provide an adequate method for the direct algebraic extensions below.
The tensor test additionally checks the exact scope of [C_A0002](../claims/Yin_C_A0002_v1.md#statement), rather than assuming a general tensor injectivity principle.
No whole-group Atiyah theorem, free-field evaluation, Ore localization, or noncyclic diffuseness assertion is used.

All affiliated operations below take place in \(L^0(\mathcal N(G))\), or the explicitly named subgroup algebra, with their closed sum and product interpretation.
Every asserted inverse is either displayed through certified factors or obtained from the cited finite-affiliated interface.
Rank means the unnormalized trace of the range support, so a matrix with \(n\) columns has kernel dimension \(n-\operatorname{rk}\).
An unbounded matrix unit preserves these ranks by that interface; no everywhere-defined unbounded change of Hilbert-space variables is asserted.

## Equal powers give a common right-coefficient equation

Let \(a,b\in G\) be distinct and satisfy \(a^d=b^d=w\ne e\), where \(d\ge2\).
Put \(u:=a-b\) and \(y:=u^{-1}bu\).
The original binomial \(u\) is an independently certified unit.
The elementary telescoping identity
\[
\sum_{k=0}^{d-1}b^k(a-b)a^{d-1-k}=a^d-b^d=0
\]
and \(b^ku=uy^k\) give
\[
\sum_{k=0}^{d-1}y^k a^{d-1-k}=0.
\tag{1}
\]
This common right-coefficient equation is stronger information than merely retaining \(y^d=w\).
Its coefficients are powers of the same original pivot label \(a\), and they are placed on the right exactly as displayed.
It does not make \(a\) commute with \(y\).

For equal cubes, (1) becomes
\[
y^2+ya+a^2=0.
\tag{2}
\]
For two transformed rows \(y,z\), put \(\Delta:=y-z\).
Subtracting their equations yields
\[
y\Delta=-\Delta(z+a).
\tag{3}
\]
Both coefficients in this intertwining relation are actual units.
Indeed \(y\) is similar to a group element and \(z(z+a)=-a^2\), so
\[
z+a=-z^{-1}a^2.
\]
Also \((z+a)^2=az\) and \((z+a)^3=-w\), by direct use of (2).
Consequently \(-z-a\) has the same cube \(w\) as \(y\), and (3) intertwines two actual rational cube roots of \(w\).

Equation (3) is not a zero-or-unit certificate for \(\Delta\).
If \(p\) is its kernel projection, then \(\Delta(-z-a)p=0\) in the affiliated ring, but this identity supplies no upper bound forcing \(p=0\).
In particular, a difference of rational cube roots is not an original group binomial merely because its two coefficients satisfy a common polynomial.
The general three-square central-column formula remains
\[
\operatorname{rk}_G K=2+\operatorname{rk}_G\Delta,
\qquad
\dim_G\ker K=\dim_G\ker\Delta.
\tag{4}
\]

## Fourth powers: an exact square-class screen

For any distinct original labels \(a,b\), the same similarity gives the useful identity
\[
u(y+a)=bu+ua=a^2-b^2.
\tag{5}
\]
If \(a^2=b^2\), then \(y=-a\) exactly.
If \(a^2\ne b^2\), the right side is an original group binomial, so \(y+a=u^{-1}(a^2-b^2)\) is independently a unit.
This conclusion uses actual equality or inequality of the original squared group labels.
It does not require a division property of an unknown coefficient algebra.

Now let three pairwise distinct rows \(a_1,a_2,a_3\) satisfy \(a_i^4=w\ne e\), and retain the distinct central-column gates of L_A0011 v2.
If their squares are all equal, pivoting at \(a_1\) gives \(a_2'=a_3'=-a_1\), and (4) gives rank two and kernel dimension one for a three-square array.
If their squares occupy exactly two distinct classes, permute rows so that \(a_1^2=a_2^2\ne a_3^2\).
Then \(a_2'=-a_1\), while (5) proves that \(a_3'+a_1\) is a unit.
Thus \(a_2'-a_3'=-(a_3'+a_1)\) is independently a unit, and the array has rank three and zero kernel.
This is a next-separation certificate for every actual torsion-free group satisfying these hypotheses, without virtually abelian coverage as a premise.
It is a restricted matrix theorem, not a whole-group Atiyah theorem.

The case of three distinct squared labels is not settled by (5).
There each \(a_i'+a_1\) is known to be a unit, but their difference remains the unresolved separation.
For completeness, (1) for fourth powers reads
\[
y^3+y^2a+ya^2+a^3=0,
\]
or, with \(x:=y+a\),
\[
y^2x=-xa^2.
\tag{6}
\]
When \(a^2\ne b^2\), \(x\) is already a unit by (5), and (6) is an actual similarity relation between \(y^2\) and \(-a^2\).
This extra identity still does not certify differences between two such \(y\)'s.

## An exact power-matrix interface, beyond the rank cap

Let \(a_1,\ldots,a_p\) be actual group elements with \(a_i^d=w\ne e\), and let \(b_1,\ldots,b_q\) be pairwise distinct central group labels, with \(a_i\ne b_j\).
Centrality is required only in the subgroup supporting these labels.
All \(a_i-b_j\), \(b_j-b_k\), and \(w-b_j^d\) are independently units.
For the last assertion, equality \(w=b_j^d\) would make the commuting quotient \(a_i b_j^{-1}\) a finite-order group element, contradicting distinctness and torsion-freeness.

Define the power matrix and central coefficient matrix by
\[
V_{ik}:=a_i^k\quad(0\le k<d),
\qquad
B_{kj}:=b_j^{d-1-k},
\qquad
Z:=\operatorname{diag}\bigl((w-b_j^d)^{-1}\bigr)_{j=1}^q.
\]
The finite geometric identity gives
\[
D:=\bigl((a_i-b_j)^{-1}\bigr)_{i,j}=VBZ.
\tag{7}
\]
If \(q=d\), then \(B\) is an actual matrix unit over the central affiliated subalgebra.
Here is an explicit certificate using only the known differences.
After reversing the power rows, change the monomial basis \(1,X,\ldots,X^{d-1}\) to
\[
1,\quad (X-b_1),\quad (X-b_1)(X-b_2),\quad\ldots,\quad
\prod_{r=1}^{d-1}(X-b_r).
\]
The coefficient change is triangular with diagonal one, so is a matrix unit with a finite algebraic inverse.
Its evaluation at \(b_j\) is triangular, with diagonal entries
\[
1,\quad b_2-b_1,\quad\ldots,\quad\prod_{r=1}^{d-1}(b_d-b_r).
\]
Each is a product of independently known commuting units, giving the required triangular inverse.
No genericity assertion or division of an unknown noncommutative coefficient is used.
For \(q>d\), write \(B=[B_0\ B_1]\), where \(B_0\) consists of the first \(d\) columns and has the certified inverse just constructed.
The explicit matrix unit
\[
Q:=\begin{pmatrix}B_0^{-1}&-B_0^{-1}B_1\\0&I_{q-d}\end{pmatrix},
\qquad
Q^{-1}=\begin{pmatrix}B_0&B_1\\0&I_{q-d}\end{pmatrix}
\]
satisfies \(BQ=[I_d\ 0]\), and hence \(DZ^{-1}Q=[V\ 0]\).
Therefore
\[
\operatorname{rk}_G D=\operatorname{rk}_G V,
\qquad
\dim_G\ker D=(q-d)+\dim_G\ker V
\quad(q\ge d).
\tag{8}
\]
The displayed kernel dimension of \(V\) uses its \(d\) columns, even when \(p\ne d\).

If the labels additionally have a common nonidentity power as in L_A0011 v2, that material's independently certified diagonal factors identify its reciprocal geometric-sum array \(K\) with \(D\) up to matrix units.
Thus (8) also holds with \(K\) in place of \(D\).
For \(q<d\), (7) still holds, but this column operation cannot retain all \(d\) columns of \(V\), and the equality of ranks in (8) is not asserted.

There is a further fourth-power consequence when \(q\ge4\).
Suppose four distinct row labels occur as two pairs whose respective squares are \(s\) and \(r\), with \(s\ne r\).
After ordering the power columns as \(0,2,1,3\), a row with square \(s\) is
\[
(1,s,a_i,a_i s).
\]
Within each pair, the two-square matrix with rows \((1,a_i)\) is a unit, because its scalar Schur difference is an original binomial.
Removing those two block row factors leaves, up to row order, two copies of the two-square matrix
\[
\begin{pmatrix}1&s\\1&r\end{pmatrix}.
\]
This matrix is a unit by the original binomial \(r-s\); no commutation between \(r\) and \(s\) is needed for this two-square elimination.
Consequently that four-row power submatrix has rank four, so every larger array containing it has rank exactly four by the common-degree cap.
Its kernel dimension is \(q-4\).
This supplies another finite certificate from actual square classes, without resolving configurations lacking two such pairs.

These square-class configurations occur over arbitrary torsion-free coefficient groups in the cyclic extension below with \(d=4\).
Choose nonidentity \(h,k\in H\), put \(v:=h^{(0)}h^{(2)}\) and \(u:=k^{(0)}\), and use the four rows
\[
t,\quad vtv^{-1},\quad utu^{-1},\quad uvtv^{-1}u^{-1}.
\tag{8a}
\]
Since \(v\) commutes with \(t^2\), the first pair has square \(t^2\), and the second has square \(ut^2u^{-1}\).
These two squares are distinct because
\(ut^2u^{-1}t^{-2}=k^{(0)}(k^{-1})^{(2)}\ne e\).
The first two rows are distinct because \(vtv^{-1}t^{-1}=h^{(0)}(h^{-1})^{(1)}h^{(2)}(h^{-1})^{(3)}\ne e\), and conjugation distinguishes the second pair as well.
Different squares distinguish rows across pairs.
All four rows have fourth power \(t^4\).
Thus any three rows consisting of the first pair and one from the second realize the rank-three case, and all four realize the rank-four certificate with at least four central columns.
No commutation relation between \(h\) and \(k\) is assumed.

## Cyclic permutation extensions retain a tensor-coordinate matrix

Let \(H\) be any torsion-free group and \(d\ge2\).
Put
\[
G:=H^d\rtimes_\alpha\langle t\rangle,
\qquad
\alpha(h^{(j)})=h^{(j+1\bmod d)},
\qquad
w:=t^d.
\]
Here \(h^{(j)}\) denotes \(h\) in the \(j\)-th direct factor.
The group is torsion-free: a finite-order element first projects to zero in \(\mathbb Z\), and then lies in the torsion-free direct product \(H^d\).
The element \(w\ne e\) is central.
For each selected \(h\in H\), define
\[
v_h:=h^{(0)},\qquad a_h:=v_h t v_h^{-1}.
\]
Then \(a_h^d=w\), and distinct \(h\)'s give distinct actual group labels, since
\[
a_h t^{-1}=h^{(0)}(h^{-1})^{(1)}.
\]
Take \(q\ge d\) central columns \(b_j:=w^j\), \(1\le j\le q\), and let \(L\) be a common positive multiple of \(1,\ldots,q\).
These labels obey the exact common-power identities
\[
a_h^{dL}=b_j^{L/j}=w^L\ne e.
\tag{9}
\]
Their \(t\)-degrees distinguish every row from every column; the column labels are pairwise distinct.
Thus all initial gates used by the reciprocal array have their original cyclic unit certificates.

For the power matrix, direct conjugation gives
\[
v_h^{-1}a_h^k t^{-k}=t^k v_h^{-1}t^{-k}=(h^{-1})^{(k)}.
\]
Therefore diagonal group-unit row and column operations identify \(V\) with the \(p\)-by-\(d\) matrix
\[
M_{ik}:=(h_i^{-1})^{(k)},
\qquad 0\le k<d.
\tag{10}
\]
Together with (8), this proves the exact interface
\[
\operatorname{rk}_G K=\operatorname{rk}_{H^d}M,
\qquad
\dim_G\ker K=(q-d)+\dim_{H^d}\ker M.
\tag{11}
\]
The change from \(G\) to \(H^d\) uses the canonical subgroup trace, not normalized finite-index restriction.
In particular, no factor \(d\) is introduced.
All column and row multipliers have already been certified independently of the unknown rank of \(M\).

For equal cubes, select \(h_1=e,h_2=h^{-1},h_3=k^{-1}\), where \(e,h,k\) are distinct, and take \(q=d=3\).
The resulting tensor-coordinate matrix is
\[
M=\begin{pmatrix}
1&1&1\\
h^{(0)}&h^{(1)}&h^{(2)}\\
k^{(0)}&k^{(1)}&k^{(2)}
\end{pmatrix}.
\tag{12}
\]
The first scalar pivot is one, and the next is the original binomial \(h^{(1)}-h^{(0)}\), which is a unit because \(h\ne e\).
Write \(h_j:=h^{(j)}\) and \(k_j:=k^{(j)}\).
The final scalar is
\[
T:=(k_2-k_0)-(k_1-k_0)(h_1-h_0)^{-1}(h_2-h_0).
\tag{13}
\]
The exact rank and nullity formulas are
\[
\operatorname{rk}_G K=\operatorname{rk}_{H^3}M
=2+\operatorname{rk}_{H^3}T,
\qquad
\dim_G\ker K=\dim_{H^3}\ker T.
\tag{14}
\]
Thus the original common-cube next separation has exactly the rank of this concrete scalar rational tensor expression.
This reduction retains arbitrary relations between \(h\) and \(k\) inside \(H\); the three copies commute only across different coordinates.
It supplies neither an inverse for \(T\) nor an example of a fractional kernel.

## Why the available tensor theorem does not close this test

Put
\[
A:=(k_1-k_0)(h_1-h_0)^{-1},
\qquad B:=Ah_0-k_0.
\]
Then (13) is the exact expression
\[
T=k_2-Ah_2+B.
\tag{15}
\]
The coefficients \(A,B\) lie in \(L^0(\mathcal N(H\times H))\) for coordinates zero and one, and commute with the individual bounded operators \(h_2,k_2\) in the third coordinate.
No commutation, normality or joint scalar spectral resolution of \(A\) and \(B\) is established.
Even the original group labels \(h_2,k_2\) need not commute with one another.

Nevertheless \(T\ne0\) follows independently from the actual group trace.
Use the [bounded-denominator construction](../claims/Yin_C_A0002_v1.md#foundations-and-conventions) first on \(A\) to choose a bounded injective \(d_0\) with \(d_0A\) bounded, then on \(d_0B\) to choose a bounded injective \(d_1\) with \(d_1d_0B\) bounded.
The product \(d:=d_1d_0\) is bounded and injective, and both \(dA,dB\) are bounded.
All of these operators lie in the first two tensor factors.
If \(T=0\), its left multiple by \(d\) is the bounded tensor identity
\[
d\otimes k-(dA)\otimes h+(dB)\otimes1=0.
\tag{16}
\]
Apply the bounded normal slice map given in the third factor by \(x\mapsto\tau_H(xk^{-1})\).
Since \(e,h,k\) are distinct actual group labels, their canonical trace coefficients give \(d=0\), contradicting injectivity on the nonzero module.
This proves \(T\ne0\), and hence \(\operatorname{rk}_{H^3}T>0\) by faithfulness of the trace.
It excludes an exact third-pivot merger in the particular tensor family (12), while leaving a possible nonzero kernel completely unresolved.
In particular, a zero-or-unit theorem for this family would have to prove that \(T\) is a unit in every case, rather than allow a zero alternative.

The [C_A0002 theorem](../claims/Yin_C_A0002_v1.md#statement) starts with spectral kernel chains of one specified affiliated operator and constructs an injective map from tensor products of those chains.
Its consequence is a lower bound on a denominator-cleared Hilbert--Schmidt centralizer in terms of squared spectral-layer dimensions.
It provides neither an upper bound forcing these dimensions to vanish nor injectivity of an arbitrary expression with two unrelated operator coefficients such as (15).
The kernel equation in (15) has not been converted to the chains of one common operator with distinct scalar parameters required by that theorem.
Treating \(A,B\) as simultaneously diagonal scalar parameters would add an unjustified hypothesis.
Likewise, diffuseness of the cyclic labels \(h_j,k_j\) does not imply diffuseness of arbitrary rational expressions formed from their same-coordinate pairs.

The weaker fact that tensor products of already injective bounded maps remain injective also does not apply directly: (15) is a sum, not an exhibited tensor product of such maps.
The available tensor theorem therefore leaves (13) open at the present scope.
This is a failure of this proposed application, not a proof that (13) is equivalent to the division-closure problem for \(H\).
No such equivalence has been established here.

## Exact contribution and remaining obligations

The equal-power right polynomial, square-class certificates, exact power-matrix factorization and cyclic-permutation tensor interface are direct calculations from the cited fixed inputs.
The [independent whole-artifact finding](../audits/reviews/Yin_R_A0013_v3.md#whole-artifact-finding) checks these conclusions and their exact limits.
Its scope includes the actual matrix-unit construction, all rectangular kernel-dimension terms, the fourth-power square-class cases, the semidirect-product labels, the nonvanishing trace slice and the tensor theorem's applicability boundary.

The most concrete remaining three-square question is whether the necessarily nonzero scalar \(T\) in (13), for actual distinct \(e,h,k\) in arbitrary torsion-free \(H\), is always an actual unit.
The construction does not assume that a torsion-free quotient inherits an Atiyah theorem from a relation-free parent.
It also does not replace actual group labels by freely chosen rational unitaries.
Its matrix \(M\) has one group label repeated in independent tensor coordinates along each row; its entries cannot presently be chosen independently to reproduce arbitrary complex group-ring matrices.
Thus an extension from (11) or (14) to the full Task still requires an explicit arbitrary-input reduction with its own independently certified multipliers and exact dimension bookkeeping.

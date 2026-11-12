---
author: Yin
---
# A noncentral finite-kernel support obstruction and its stable shear boundary

This investigation addresses the rank-deficient branch of [C_A0007_v3](../claims/Yin_C_A0007_v3.md#the-rank-deficient-normalization-boundary) for [S_A0005](../strategies/Yin_S_A0005.md).
The question is whether zero stabilization and a finite congruence preserving the two vertex coefficient rings can spread a deficient polynomial kernel witness to full expected support, with a known nullity correction.
The calculation below gives an actual noncentral cyclic example for which every polynomial kernel witness remains deficient, and proves a no-go statement for an explicit family of additive-preserving stable shears.
It does not exclude arbitrary affine enlargements or every polynomial congruence preserving additivity.
The obstruction applies to the specified stable-shear family and retains the successful support-cut calculation below.

## Fixed inputs and reuse

The [free-tree finite-support obstruction](../ledger/Yin_L_A0002_v1.md#denominator-clearing-and-finite-propagation) supplies the boundary operator with nonzero analytic kernel but zero polynomial kernel.
The [two-coordinate degeneration](../ledger/Yin_L_A0013_v1.md#full-support-does-not-supply-a-bounded-inverse-even-for-a-group-ring-matrix) distinguishes full support from a strict lower bound.
The [affine realization in L_A0014](../ledger/Yin_L_A0014_v1.md#affine-realization-changes-the-support-behavior) shows why changing the realization demands new kernel bookkeeping.
[C_A0007_v3](../claims/Yin_C_A0007_v3.md#polynomial-normalization-over-the-cyclic-edge) removes the strict-lower-bound obstacle only after full expected support is available.
The present calculation addresses missing expected support, with an explicit integer nullity correction throughout.
It uses the established affiliated-rank and subgroup interfaces already retained in those inputs and no newly acquired source.

## An additive noncentral boundary matrix

Let
\[
G_1:=F(z,a),\qquad G_2:=F(z,b),\qquad
H:=\langle z\rangle,\qquad
G:=G_1*_H G_2=F(z,a,b).
\]
The subgroup embeddings are the displayed free-group embeddings, and \(H\) is infinite cyclic and noncentral in both vertices.
Write \(E_H\) for coefficient expectation, amplified entrywise for matrices, and use unnormalized group traces for every nullity.
Put
\[
A:=a-1,\qquad B:=b-1,\qquad
\partial:=(A\ \ B),\qquad
T:=\begin{pmatrix}
0&A&B\\ A^*&0&0\\ B^*&0&0
\end{pmatrix}
=T_a+T_b,
\]
where \(T_a\) contains only the \(A,A^*\) entries and \(T_b\) contains only the \(B,B^*\) entries.
Thus \(T_a\in M_3(\mathbb CG_1)\) and \(T_b\in M_3(\mathbb CG_2)\) are selfadjoint.

The adjoint kernel of \(\partial\) is zero: a vector in it is invariant under \(a\), hence is constant on each infinite \(\langle a\rangle\)-orbit and cannot be a nonzero square-summable vector.
Consequently \(\partial\) has analytic rank one, and its right kernel has von Neumann dimension one.
The two off-diagonal blocks of \(T\) act between the first coordinate and the remaining two coordinates, so
\[
\ker T=\{0\}\oplus\ker\partial,
\qquad \nu_3(T)=1.
\tag{1}
\]
Only polar decomposition and the unnormalized finite trace enter this calculation.

On the other hand,
\[
\ker\bigl(T:(\mathbb CG)^3\longrightarrow(\mathbb CG)^3\bigr)=0.
\tag{2}
\]
Indeed \(A^*x_0=0\) first gives \(x_0=0\), and the remaining equation is \(Ax_1+Bx_2=0\).
Partition finite supports into right cosets of \(F(a,b)\).
Within each coset this is a finitely supported edge chain with zero boundary on the free Cayley tree, hence every coefficient vanishes by leaf removal.
This reuses the exact finite-support obstruction of L_A0002 rather than assuming an algebraic basis for the analytic kernel.

## A four-square witness with maximal but deficient expected support

Define
\[
v:=\begin{pmatrix}z\\a\\b\end{pmatrix},\qquad
P:=\begin{pmatrix}1&0\\-v&I_3\end{pmatrix},\qquad
P^{-1}=\begin{pmatrix}1&0\\v&I_3\end{pmatrix},
\]
and set
\[
Y:=P^*(0\oplus T)P
=\begin{pmatrix}v^*Tv&-v^*T\\-Tv&T\end{pmatrix}.
\tag{3}
\]
Both \(P\) and \(P^{-1}\) are bounded finite group-ring matrices, so this congruence has no unbounded-domain issue.
It gives
\[
\nu_4(Y)=1+\nu_3(T)=2.
\tag{4}
\]
The extra kernel dimension is exactly the displayed zero coordinate.

Although \(v\) has coefficients in both vertices, the transformed summands
\[
Y_j:=\begin{pmatrix}v^*T_jv&-v^*T_j\\-T_jv&T_j\end{pmatrix}
\tag{5}
\]
still belong to their respective vertex group rings.
For example,
\[
T_av=\begin{pmatrix}Aa\\A^*z\\0\end{pmatrix},\qquad
v^*T_av=z^{-1}Aa+a^{-1}A^*z\in\mathbb CG_1,
\]
and the corresponding formulas with \(B,b\) lie in \(\mathbb CG_2\).
This verifies vertex membership directly without commuting \(z\) with \(a\) or \(b\).

Equation (2) and the polynomial inverse of \(P\) identify the entire polynomial kernel:
\[
\ker_{\mathbb CG}Y=W\mathbb CG,
\qquad
W:=P^{-1}\begin{pmatrix}1\\0\\0\\0\end{pmatrix}
=\begin{pmatrix}1\\z\\a\\b\end{pmatrix}.
\tag{6}
\]
The words \(1,z\) lie in the same right coset of \(H\), while \(a,b\) lie in distinct further right cosets.
Consequently
\[
C:=E_H^{(4)}(WW^*)
=\begin{pmatrix}
1&z^{-1}&0&0\\ z&1&0&0\\0&0&1&0\\0&0&0&1
\end{pmatrix}.
\tag{7}
\]
Its first two-square block has eigenvalues \(0,2\), so \(C\) has affiliated rank three and is bounded below by its support projection.
There is a support deficiency of exactly one, not a small-eigenvalue degeneration on that support.

More strongly, no other finite polynomial kernel columns for this same matrix can have full expected Gram.
Every such matrix is \(WF\) for a finite row matrix \(F\) over \(\mathbb CG\), and the nonzero base row
\[
\ell:=(-z\ \ 1\ \ 0\ \ 0)\in M_{1,4}(\mathbb CH)
\]
satisfies \(\ell WF=0\).
Bimodularity gives
\[
\ell E_H^{(4)}(WFF^*W^*)\ell^*=0.
\tag{8}
\]
The adjoint of \(\ell\) is a nonzero bounded kernel column of this positive expected Gram, which therefore cannot have full support.
Its rank is at most three, and the original \(W\) attains that bound.

The closed range of the entire polynomial kernel has von Neumann dimension one because \(W^*W=4I\).
The analytic kernel has dimension two by (4).
Hence this example's complete kernel cannot arise from a finite group-ring invertible congruence of a constant matrix: the constant kernel columns and the finite inverse would then generate the entire analytic kernel by polynomial columns.
The missing part is the free-boundary analytic kernel, not another overlooked finite witness.
The calculation gives no new group class, since the ambient group is free and already has known Atiyah ranks.

## Smith support and the exact compression correction

This same example does admit the previously known support-cut repair, which must be kept separate from the failure of full-support polynomial witnesses for its fixed realization.
Let \(Q\in M_4(\mathbb CH)\) be the identity except for \(Q_{21}:=-z\), so that
\[
QW=\begin{pmatrix}1\\0\\a\\b\end{pmatrix}=:W_0,
\qquad
E_H^{(4)}(W_0W_0^*)=q:=\operatorname{diag}(1,0,1,1).
\tag{13}
\]
This is the constant cyclic support corner produced by the module normalization, up to a coordinate permutation.
The appropriate congruence is
\[
\widehat Y:=(Q^{-1})^*YQ^{-1}
=\begin{pmatrix}
0&-s^*&0&0\\
-s&0&A&B\\
0&A^*&0&0\\
0&B^*&0&0
\end{pmatrix},
\qquad s:=Aa+Bb.
\tag{14}
\]
Indeed the triangular shears combine to remove the first component \(z\) of \(v\), leaving \((0,a,b)^t\).
Both transformed summands remain in their original vertex rings because \(Q,Q^{-1}\) lie in the cyclic group ring.

The second coordinate of every analytic kernel vector of \(\widehat Y\) vanishes, since its third row imposes \(A^*x_2=0\).
The remaining coordinates satisfy the single row equation
\[
R\eta=0,\qquad R:=(-s\ \ A\ \ B).
\tag{15}
\]
The row has dense range, because \(R^*\xi=0\) in particular gives \(A^*\xi=0\).
Its analytic rank is therefore exactly one and its nullity is two.
Thus \(p_{\widehat Y}\le q\) and \(\nu_4(\widehat Y)=2\), while \(W_0^*W_0=3I\) gives
\[
\tfrac13q\le E_H^{(4)}(p_{\widehat Y})\le q.
\tag{16}
\]
In particular, \(q\) is the actual expected-kernel support, not merely the support of an incomplete finite witness.

Nevertheless,
\[
q\widehat Yq=0.
\tag{17}
\]
As an operator on the three-coordinate corner, its nullity is three, so this compression adds exactly one kernel dimension.
That correction is independently the rank of the discarded row \(R\); it is not inferred by assuming integral ranks for arbitrary compressed matrices.
The compressed vertex summands are both zero, so their subordination calculation is trivial.
Alternatively, retaining all four coordinates, the right support cut \(\widehat Yq\) has nullity three and adjoint kernel exactly \(q\); the subsequent left cut \(q\widehat Yq=0_4\) has nullity four.
The two corrections are each one, exactly as in the established two-support-cut mechanism of L_A0014 and C_F0181.
This calculation therefore supplies a noncentral obstruction to one certificate class, but no new support-cut mechanism beyond those inputs.

## A support lemma for additive-preserving stable shears

Let \(\mathcal S:=\mathbb CG_1+\mathbb CG_2\) denote the linear space of additive vertex coefficients.
For a finite \(c\in\mathbb CG\),
\[
(a^{-1}-1)c\in\mathcal S\quad\Longrightarrow\quad c\in\mathbb CG_1.
\tag{9}
\]
To prove this, examine coefficients on each orbit \(\langle a\rangle g\) outside \(G_1\).
The orbit is disjoint from \(G_1\), and it intersects \(G_2\) in at most one point, because two such intersections would give a nonzero power of \(a\) in \(G_2\).
The coefficients of a finite difference \((a^{-1}-1)c\) sum to zero on each such orbit.
If the difference lies in \(\mathcal S\), its restriction to this orbit has at most one nonzero coefficient, so that coefficient is zero.
The original finite coefficient sequence is then translation invariant on an infinite orbit and must vanish.
Thus no coefficient of \(c\) lies outside \(G_1\), proving (9).
Interchanging \(a,G_1\) with \(b,G_2\) gives the corresponding implication.
In particular,
\[
(a^{-1}-1)c,(b^{-1}-1)c\in\mathcal S
\quad\Longrightarrow\quad c\in\mathbb CG_1\cap\mathbb CG_2=\mathbb CH.
\tag{10}
\]

Now allow an arbitrary number \(m\ge1\) of added zero coordinates and any finite matrix \(V\in M_{3,m}(\mathbb CG)\).
Write \(c\in M_{1,m}(\mathbb CG)\) for its first row, and define
\[
P_V:=\begin{pmatrix}I_m&0\\-V&I_3\end{pmatrix},\qquad
Y(V):=P_V^*(0_m\oplus T)P_V
=\begin{pmatrix}V^*TV&-V^*T\\-TV&T\end{pmatrix}.
\tag{11}
\]
Suppose only that \(Y(V)\) is additive in the two vertex group rings, meaning that every entry lies in \(\mathcal S\).
The last two rows of the lower-left block force every entry of \(A^*c\) and \(B^*c\) into \(\mathcal S\).
Equation (10) therefore gives \(c\in M_{1,m}(\mathbb CH)\).

The complete polynomial kernel and analytic nullity remain explicit:
\[
\ker_{\mathbb CG}Y(V)=W_V(\mathbb CG)^m,
\qquad
W_V:=\begin{pmatrix}I_m\\V\end{pmatrix},
\qquad
\nu_{m+3}(Y(V))=m+1.
\tag{12}
\]
The nonzero base row
\[
\ell_V:=(-c\ \ 1\ \ 0\ \ 0)
\]
annihilates \(W_V\), and hence every polynomial kernel matrix for \(Y(V)\).
The same bimodularity argument as (8) proves that every polynomial expected Gram is deficient.
Thus arbitrary zero stabilization followed by this general finite shear cannot repair full expected support while preserving additivity.
The obstruction is forced by vertex membership, not by a special choice of \(V\), a failure to find enough columns, or an uncomputed extra kernel.
The exact nullity correction is always the integer \(m\).

## What this does and does not exclude

Further invertible congruences over the cyclic affiliated field preserve the deficiency of any displayed expected Gram whenever the transformed witnesses remain finite; the coefficient matrix rank is unchanged by the invertible cyclic factor.
Padding an already deficient witness by independent zero-coordinate witnesses increases both the ambient size and the expected-Gram rank by the same amount and leaves its deficit unchanged.
These observations complement the stable-shear obstruction but do not classify arbitrary alternating sequences of general congruences and enlargements.

The example rules out a universal assertion that an additive noncentral group-ring matrix with nonzero analytic kernel has finite kernel columns of full expected support, even when it already has nonzero polynomial kernel columns.
The stable calculation additionally rules out the explicit family (11) as a general remedy for the free-boundary deficiency.
It does not rule out a different additive realization with invertible auxiliary blocks, a more general polynomial congruence, or a constrained analytic boundary method not requiring a finite full-support witness.
Any such extension must explain how it eliminates the base annihilator exhibited above while tracking its new kernels.
For the displayed example, compression is fully computed in (13)--(17) and succeeds only with its explicitly certified correction.
The remaining question is whether a matrix outside this independently controlled boundary-row mechanism admits a comparably explicit repair; the present draft does not settle it.

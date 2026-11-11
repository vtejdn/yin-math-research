---
author: Yin
---
# Three-term rows, preserved coefficient fields and the full-rank obstruction

Date: 2026-11-11 (Asia/Hong_Kong).
This investigation for [Yin_T_A0001](../tasks/Yin_T_A0001_v1.md#contract) asks which part of the two-monomial whole-row criterion can survive the addition of a third term.
The selected Promislow pencil passes the specified original cyclic, positive-real-part and integer-grading screens, but its scalar endpoint is resolved by an explicit actual finite-index model with known virtually abelian coverage.
A second three-term pencil admits a strict dimension descent preserving a cyclic coefficient field between noncommuting group-monomial row and column factors.
Every pivot in both calculations is independently justified before its inverse is used, and all kernel dimensions use the canonical trace and unnormalized matrix trace.
The final row-splitting construction shows that an unrestricted three-term-row theorem would be equivalent to the full Atiyah matrix problem.
These are direct specializations, comparisons and exact interfaces for known cyclic, finite-index and Higman mechanisms, not a claim of new positive group-class coverage or historical novelty.
All affiliated products below are closed products in the actual algebra.
The [independent whole-artifact finding](../audits/reviews/Yin_R_A0012_v1.md#whole-artifact-finding) covers all the mathematics below, with the exact source and foundational limits retained in that review.

## Group and selected pencil

Use the previously retained [Promislow group](../ledger/Yin_L_A0003_v1.md#retained-candidate-beyond-the-ambient-cyclic-quotient-test)
\[
P=\langle a,b\mid b^{-1}a^2b=a^{-2},\ a^{-1}b^2a=b^{-2}\rangle.
\]
The source facts are [Gar21, arXiv v4, Section 3.1, pp. 4--5](../literature/pdf/Gar21--arxiv-v4.pdf#page=4): this group is torsion-free, and
\[
N=\langle X=a^2,Y=b^2,Z=(ab)^2\rangle\cong\mathbb Z^3,
\qquad P/N\cong C_2^2.
\]
The action and cocycle in those exact passages are enough for every group identity used below.
No unit-conjecture construction in the source is used.
The abelianization is \(C_4\oplus C_4\), as follows directly by abelianizing the displayed presentation.

Select
\[
p=1+a+b,
\qquad
A=\begin{pmatrix}1+a&b\\-1&1\end{pmatrix}.
\tag{P1}
\]
The whole rows of \(A\) have respectively three and two group monomial terms.
Swap its rows and use the scalar pivot \(-1\); the residual Schur complement is exactly \(p\).
Thus the independently invertible elementary factors from [the scalar Schur step](../ledger/Yin_L_A0009_v1.md#the-exact-size-reducing-step) give
\[
\operatorname{rk}_P A=1+\operatorname{rk}_P p,
\qquad
\dim_P\ker A=\dim_P\ker p.
\tag{P2}
\]
This reduction demonstrates the new scalar endpoint created by one three-term row.
It does not assume that endpoint is invertible.

## Direct-test screen

The support \(\{1,a,b\}\) generates all of \(P\), which has no nonzero homomorphism to \(\mathbb Z\).
Consequently the supporting-subgroup grading used in [the singleton-extreme test](../ledger/Yin_L_A0008_v1.md#a-singleton-extreme-support-term-and-the-earlier-examples) is unavailable.
The three coefficients have equal modulus, so none dominates the sum of the other two.
The support is not contained in a coset of a cyclic subgroup: since it contains the identity, this would imply that \(a,b\) commute, whereas their defining conjugation relation and the infinite order of \(a\) prohibit that.
This excludes the direct cyclic-support test, without asserting that all possible certified multiplications have been ruled out.

For the energy screen, one can test all characters of \(P\) using explicitly approximate regular-representation eigenvectors.
Let \(R=\{1,a,b,ab\}\), let
\[
B_L=\{X^iY^jZ^k:-L\le i,j,k\le L\},
\qquad F_L=\coprod_{r\in R}rB_L.
\]
For each fixed \(s\in P\), left multiplication permutes the four cosets and translates each integer cube by one fixed vector, since \(sr=r'n\) for a fixed \(n\in N\).
Therefore \(|sF_L\mathbin\triangle F_L|/|F_L|\to0\).
For a unitary character \(\chi:P\to\mathbb T\), set
\[
\xi_{L,\chi}=|F_L|^{-1/2}\sum_{g\in F_L}\overline{\chi(g)}\delta_g.
\]
Then
\[
\|\lambda(s)\xi_{L,\chi}-\chi(s)\xi_{L,\chi}\|^2
=\frac{|sF_L\mathbin\triangle F_L|}{|F_L|}\longrightarrow0.
\tag{P3}
\]
Thus positivity of a bounded matrix over \(\mathbb CP\) implies positivity of every corresponding finite character evaluation, by testing \(v\otimes\xi_{L,\chi}\) and taking the limit.
Every assignment \(\chi(a),\chi(b)\in\mu_4\) defines a character.

For \(p\), the four choices \((1,1),(-1,-1),(i,i),(-i,-i)\) give values \(3,-1,1+2i,1-2i\).
If \(\operatorname{Re}(\gamma p)\ge0\), the first two evaluations force \(\operatorname{Re}\gamma=0\), and the last two force \(\operatorname{Im}\gamma=0\).
Consequently no nonzero scalar phase makes the real part of \(p\) positive.

The displayed matrix \(A\) also has no constant weighted phase-energy certificate:
\[
\operatorname{Re}(\gamma W A)\not\ge0
\qquad
(\gamma\in\mathbb C^\times, W\in M_2(\mathbb C),\ W>0).
\tag{P4}
\]
Indeed, evaluation at \((-1,-1)\) gives the real symmetric indefinite matrix
\[
A_0=\begin{pmatrix}0&-1\\-1&1\end{pmatrix}.
\]
Testing its eigenvectors with positive and negative real eigenvalues forces \(\operatorname{Re}\gamma=0\), since \(v^*Wv>0\).
Write \(\gamma=it\), with \(t\in\mathbb R\setminus\{0\}\).
For any Hermitian evaluated matrix \(A_j\), the positive matrix \(\operatorname{Re}(itWA_j)=it(WA_j-A_jW)/2\) has trace zero and hence vanishes.
Apply this to \(A_0\) and to
\[
A_1=A(1,-1)=\begin{pmatrix}2&-1\\-1&1\end{pmatrix}.
\]
Their difference is \(\operatorname{diag}(2,0)\), so commuting with both first makes \(W\) diagonal and then makes \(W=wI\), with \(w>0\).
At \((i,1)\), however,
\[
\operatorname{Re}(itwA(i,1))
=\begin{pmatrix}-tw&itw\\-itw&0\end{pmatrix}
\]
has determinant \(-t^2w^2<0\), a contradiction.
The screen concerns this original matrix and these specified tests, not all possible equivalent realizations.

## Actual finite-index matrix model

The unitary identification
\[
V:\ell^2(N)^4\longrightarrow\ell^2(P),
\qquad V(\eta_r)_{r\in R}=\sum_{r\in R}\lambda(r)\eta_r
\]
defines the actual normal faithful representation \(\rho(T)=V^*TV\).
For left multiplication by a group element, its \((r,s)\) entry is the group element \(r^{-1}gs\in N\) when \(gs\in rN\), and is zero otherwise.
Thus \(\rho(\mathcal N(P))\subseteq M_4(\mathcal N(N))\), with its spectral and affiliated extension as in [the earlier actual finite-index model](../ledger/Yin_L_A0003_v1.md#actual-affiliated-embedding).
The trace identity is
\[
(\operatorname{Tr}_4\otimes\tau_N)(\rho(T))=4\tau_P(T).
\tag{P5}
\]
It holds on group elements and extends normally; the same relation holds for kernel projections and affiliated ranks.
In particular,
\[
\dim_P\ker p=\frac14\dim_N\ker\rho(p).
\tag{P6}
\]

In the order \((1,a,b,ab)\), the explicit matrix is
\[
M=\rho(p)=
\begin{pmatrix}
1&X&Y&0\\
1&1&0&X^{-1}Z\\
1&0&1&X^{-1}\\
0&XY^{-1}Z^{-1}&1&1
\end{pmatrix}.
\tag{P7}
\]
For example, the only nonobvious products needed for its columns are
\(ba=ab\,XY^{-1}Z^{-1}\), \(aab=bX^{-1}\), and \(bab=aX^{-1}Z\).
These follow from the exact action and cocycle in Gar21, Section 3.1.
Every whole row of \(M\) still has exactly three group monomial terms.
The preserved structure used next is commutative rational dependence on the three translation generators, rather than a three-term row bound.

## Independently certified scalar pivot chain

The Fourier transform identifies \(\mathcal N(N)\) with \(L^\infty(\mathbb T^3)\), and nonzero Laurent polynomials have zero sets of Haar measure zero.
For completeness, the latter follows by induction on the number of variables: view a nonzero Laurent polynomial as a one-variable polynomial, choose one nonzero coefficient polynomial, discard its measure-zero vanishing set by the induction hypothesis, and use finiteness of the remaining one-variable root set with Fubini's theorem.
Hence every nonzero element of \(\mathbb C(X,Y,Z)\) is an independently justified actual affiliated unit.
This is the elementary abelian mechanism, and it uses no Atiyah premise for \(P\).
Evaluation at \((1,1,1)\) below is merely a certificate that a displayed Laurent polynomial is not identically zero, not a normal character of \(L^\infty(\mathbb T^3)\).

The first scalar pivot of \(M\) is \(1\).
After removing it, swap the first two remaining rows to obtain
\[
C=\begin{pmatrix}
-X&1-Y&X^{-1}\\
1-X&-Y&X^{-1}Z\\
XY^{-1}Z^{-1}&1&1
\end{pmatrix}.
\]
The second pivot \(-X\) is an independently invertible group monomial.
Its Schur complement is
\[
S=\begin{pmatrix}d&e\\f&k\end{pmatrix},
\quad
\begin{aligned}
d&=X^{-1}(1-X-Y),\\
e&=X^{-2}(1-X+XZ),\\
f&=Y^{-1}Z^{-1}(1-Y+YZ),\\
k&=1+X^{-1}Y^{-1}Z^{-1}.
\end{aligned}
\tag{P8}
\]
The third pivot \(d\) is nonzero because \(d(1,1,1)=-1\), so its affiliated inverse is justified before the last Schur complement is formed.
Write
\[
w=k-fd^{-1}e.
\]
Direct Laurent expansion gives
\[
\Delta:=\det M=Xdk-Xef
=3-X-X^{-1}-Y-Y^{-1}-Z-Z^{-1},
\qquad w=\frac{\Delta}{Xd}.
\tag{P9}
\]
The polynomial \(\Delta\) is nonzero since \(\Delta(1,1,1)=-3\).
Thus the last pivot \(w\) is an independently justified affiliated unit; equivalently its rational expression is regular at this point and evaluates to \(3\).
Every step uses exact elementary triangular units in the actual affiliated matrix ring.
The successive ranks are therefore \(4,3,2,1\), and every corresponding closed kernel dimension is zero.
By (P6), \(\dim_P\ker p=0\), and (P2) gives \(\operatorname{rk}_P A=2\) and \(\dim_P\ker A=0\).
No inverse is applied to every Hilbert-space vector as a pointwise domain assertion; the Schur identities use closed affiliated products and rank invariance.

## Scope of the structure and known coverage

The calculation preserves the actual field \(\mathbb C(X,Y,Z)\) through all four scalar pivots and proves their nonvanishing independently.
It does not preserve the literal three-monomial row bound: the final numerator has seven monomials, and intermediate entries become rational.
The denominator \(d\) and numerator \(\Delta\) can also be certified by the earlier abelian grading tests after the actual finite-index expansion.
The absence of an integer character on \(P\) therefore does not preclude a grading on the translation subgroup after changing the matrix realization.

The source classification already covers all of \(P\), since \(N\cong\mathbb Z^3\) is normal with finite quotient and \(P\) is torsion-free.
This is a special case of [Lin93's class \(\mathcal C\) coverage](../audits/literature/Lin93/Yin_U001.md#group-class-and-exact-theorems), as previously recorded for this exact group.
The calculation adds an explicit screened example and independent scalar-pivot certificate to the current investigation, with no claim of historical novelty or new positive Atiyah coverage.
Torsion-freeness alone does not supply a finite-index abelian subgroup, a commutative rational coefficient field, or the nonvanishing of all future pivots.
These are the exact additional features on which this calibration depends.

## An explicitly preserved coefficient class

Let \(G\) be torsion-free, let \(t\in G\setminus\{e\}\), and put \(U=\mathcal U(\mathcal N(G))\).
The [cyclic regular-representation proof](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions) identifies an actual copy \(K_t\cong\mathbb C(z)\) inside \(U\), obtained by evaluating rational functions at \(t\).
Every nonzero Laurent polynomial in \(t\) is injective on the regular representation because \(t\) has infinite order, and therefore is an affiliated unit.
Consequently every nonzero element of \(K_t\) is an actual unit, independently of any Atiyah hypothesis for \(G\).
Only the infinite order of this selected \(t\) is needed here; torsion-freeness supplies that condition for every nonidentity choice.
We use group elements below as their left regular operators.

Suppose an \(m\)-by-\(n\) matrix has an explicit factorization
\[
A=\operatorname{diag}(u_1,\ldots,u_m)\,F\,
  \operatorname{diag}(v_1,\ldots,v_n),
\qquad u_i,v_j\in G,\quad F\in M_{m,n}(K_t).
\tag{G1}
\]
The \(u_i,v_j\) need not commute with \(t\) or with one another.
Their diagonal matrices and inverses are known bounded group-ring units.
For an initial group-ring example one may require \(F\) to have Laurent-polynomial entries; the enlarged rational coefficient class is what elimination preserves.

Choose any nonzero entry of \(F\), permute its row and column to position \((1,1)\), and write \(f=f_{11}\).
The corresponding scalar pivot of \(A\) is
\[
a=u_1 f v_1,
\qquad a^{-1}=v_1^{-1}f^{-1}u_1^{-1}.
\tag{G2}
\]
This inverse is justified before forming a Schur complement, since \(f\ne0\) in the explicitly known field \(K_t\).
For \(i,j>1\), the resulting Schur entry is
\[
\begin{aligned}
S_{ij}
&=u_i f_{ij}v_j
 -(u_i f_{i1}v_1)(v_1^{-1}f^{-1}u_1^{-1})(u_1f_{1j}v_j)\\
&=u_i\bigl(f_{ij}-f_{i1}f^{-1}f_{1j}\bigr)v_j.
\end{aligned}
\tag{G3}
\]
Thus the row and column gauges survive deletion of the pivot, and the inner coefficient remains in the same actual cyclic field.
This is a precise invariant under scalar dimension reduction; it does not claim that the bound of three monomial terms survives.
All products in (G2)--(G3) are products in the affiliated algebra, with closure understood.

The [actual Schur equivalence](../ledger/Yin_L_A0009_v1.md#the-exact-size-reducing-step) gives
\[
\operatorname{rk}_G A=1+\operatorname{rk}_G S,
\qquad
\dim_G\ker A=\dim_G\ker S.
\tag{G4}
\]
These are statements about closed kernel dimensions; no pointwise Hilbert-space substitution by an unbounded inverse is asserted.
Continue until the remaining matrix is exactly zero.
Every nonzero field entry is a justified pivot, so if \(r\) pivots occur then
\[
\operatorname{rk}_G A=r=\operatorname{rank}_{K_t}F,
\qquad
\dim_G\ker A=n-r.
\tag{G5}
\]
The zero or nonzero decisions are identities in the displayed rational function field, rather than unproved invertibility decisions in a general rational closure.
The existence of the explicit gauges (G1) is an additional sufficient condition and is not inferred from torsion-freeness or from row sparsity.
All the rational coefficients and their certified inverses lie in the actual rational closure of \(\mathbb CG\), since they are obtained from the cyclic group ring by actual inversions.

For an original bordered pencil \(Q=\left(\begin{smallmatrix}0&u\\v&L\end{smallmatrix}\right)\) with nonzero constant borders \(u,v\) and an independently invertible affine denominator \(L\) of size \(N\ge2\), suppose its \((N-1)\)-square complementary block has form (G1), with field rank \(r\).
The [complementary-block identity](../ledger/Yin_L_A0005_v1.md#complementary-block-reduction-and-the-scalar-obstruction) and original bordered Schur identity give
\[
\operatorname{rk}_GQ=2+r,
\qquad
\operatorname{rk}_G(uL^{-1}v)=2+r-N.
\]
The latter is a scalar rank in \([0,1]\), so the integer \(r\) must be \(N-2\) or \(N-1\).
The scalar rational value is accordingly zero or an actual affiliated unit, with its inverse in the actual rational closure by the retained inverse-closure interface.
This supplies a sufficient condition on the actual complementary block; it does not certify the original denominator or assert that arbitrary complementary blocks have this form.

For matrices with one group monomial in each nonzero entry, a useful way to find (G1) is to normalize edge labels along a spanning forest in the bipartite graph of rows and columns.
If the remaining actual labels all lie in one cyclic subgroup, the normalized matrix has Laurent-polynomial entries in that generator.
This is an exact sufficient certificate when the labels and gauges have been exhibited; it makes no uniform algorithmic claim about arbitrary group-word equality.

## A concrete three-term pencil over the Promislow group

Use the same Promislow group and translation generators as above.
Gar21, Section 3.1, pp. 4--5, also gives the unique normal forms and conjugation data used in the screen below.
Set
\[
F(X)=
\begin{pmatrix}
1&1&1\\
1&2&1\\
1&1&X
\end{pmatrix},
\qquad
A=\operatorname{diag}(a,b,ab)\,F(X)\,\operatorname{diag}(1,a,b).
\tag{G6}
\]
Then
\[
A=
\begin{pmatrix}
a&a^2&ab\\
b&2ba&b^2\\
ab&aba&abXb
\end{pmatrix}.
\tag{G7}
\]
Each whole row has exactly three nonzero group-monomial terms.
Its coefficient support contains \(a,b\) and therefore generates all of \(P\).
It is outside the previous whole-row two-monomial condition.

The first displayed pivot is the known bounded unit \(a\).
Its Schur complement is exactly
\[
\begin{aligned}
S
&=
\begin{pmatrix}2ba&b^2\\aba&abXb\end{pmatrix}
-\binom{b}{ab}a^{-1}\begin{pmatrix}a^2&ab\end{pmatrix}\\
&=
\begin{pmatrix}ba&0\\0&ab(X-1)b\end{pmatrix}.
\end{aligned}
\tag{G8}
\]
For example, the off-diagonal cancellations are \(b^2-ba^{-1}ab=0\) and \(aba-aba^{-1}a^2=0\), with precisely the indicated noncommutative order.
The next pivot \(ba\) is another independently known group unit.
The final scalar \(ab(X-1)b\) is an actual unit because \(X\ne e\) has infinite order, so \(X-1\) has the independent cyclic injectivity certificate.
Consequently
\[
\operatorname{rk}_P A
=1+\operatorname{rk}_P S
=2+\operatorname{rk}_P\bigl(ab(X-1)b\bigr)
=3,
\qquad
\dim_P\ker A=0.
\tag{G9}
\]
The first two eliminations use bounded group-monomial pivots; only the final inverse of \(X-1\) can be unbounded.
The rank argument handles that inverse in the actual affiliated algebra and does not assign it an unrestricted Hilbert-space domain.

## The precise original-pencil screen

The original coefficient support is
\[
\mathcal S=\{a,X,ab,b,ba,Y,aba,abXb\}.
\tag{G10}
\]
It generates \(P\), so there is no nonzero actual integer character on the support subgroup to which the previous scalar grading test could be applied directly.
The support is not contained in one cyclic subgroup: \(a\) and \(b\) do not commute, since otherwise \(b^{-1}a^2b=a^{-2}\) would force \(a^4=e\), contradicting torsion-freeness and \(X\ne e\).
This excludes direct membership of the original coefficients in one cyclic group ring.
It does not exclude transformations by already known units, which are exactly what (G6) provides.

The conjugation and cocycle formulas on the cited Gar21 pages give the following normal forms, and their uniqueness shows that no element of \(\mathcal S\) is the identity or the inverse of another element of \(\mathcal S\).

| Element | Normal form | Inverse normal form |
| --- | --- | --- |
| \(a\) | \(a\) | \(X^{-1}a\) |
| \(X\) | \(X\) | \(X^{-1}\) |
| \(ab\) | \(ab\) | \(Z^{-1}ab\) |
| \(b\) | \(b\) | \(Y^{-1}b\) |
| \(ba\) | \(X^{-1}YZ^{-1}ab\) | \(X^{-1}Yab\) |
| \(Y\) | \(Y\) | \(Y^{-1}\) |
| \(aba\) | \(Y^{-1}Zb\) | \(Zb\) |
| \(abXb\) | \(X^{-1}Y^{-1}a\) | \(Y^{-1}a\) |

Write \(A=\sum_{g\in\mathcal S}A_g g\), where \(A_g\in M_3(\mathbb C)\).
Suppose there were \(z\in\mathbb C\setminus\{0\}\) and a constant positive definite \(W\in M_3(\mathbb C)\) such that
\[
H=\operatorname{Re}(zWA)\ge0.
\tag{G11}
\]
Since \(e\notin\mathcal S\), the unnormalized canonical matrix trace of \(H\) is zero.
Faithfulness of that finite trace gives \(H=0\).
But \(\mathcal S\cap\mathcal S^{-1}=\varnothing\), so the Fourier coefficient of \(H\) at any \(g\in\mathcal S\) is exactly \(zWA_g/2\).
It cannot vanish when \(A_g\ne0\), because \(zW\) is invertible.
This contradiction excludes every direct test of the form (G11), with any scalar phase and any constant positive definite left weight.
It says nothing about real-part certificates after a different group-valued change of rows or columns.

The diagonal row and column gauges in (G6) nevertheless convert \(A\) to the cyclic matrix \(F(X)\).
Thus this example survives the specified original-pencil screen but is completely covered once the existing cyclic mechanism is transported through these explicit bounded units.
The retained candidate already records the full Atiyah coverage of this virtually abelian group.
Neither (G9) nor the invariant (G3) gives new Atiyah group-class coverage or an independent constraint on an arbitrary three-term Schur complement.
Its useful contribution is the explicit preserved structure: different rows and columns may carry noncommuting group gauges while the remaining coefficients stay inside one independently known cyclic field.
When two branches produce unrelated holonomy elements and no such common field is exhibited, the next Schur pivot remains an unresolved scalar rational sum rather than a certified unit.

## A concrete limit of the cyclic gauge condition

The first pencil (P1) cannot be reduced to a single cyclic Laurent group ring by group-monomial diagonal row and column factors of the displayed form.
Indeed, suppose \(u_i^{-1}A_{ij}v_j^{-1}\in\mathbb C[H]\), where \(H=\langle t\rangle\) is cyclic.
Linear independence of distinct group elements in the group ring implies that each monomial in the transformed \((1,1)\) entry lies in \(H\), as do the three other nonzero monomial entries.
Put
\[
c=u_1^{-1}v_1^{-1}\in H,
\quad d=u_2^{-1}v_1^{-1}\in H,
\quad e=u_2^{-1}v_2^{-1}\in H.
\]
Then \(u_1^{-1}v_2^{-1}=cd^{-1}e\in H\).
The other top-left monomial and the top-right entry therefore imply
\[
u_1^{-1}a u_1=(u_1^{-1}a v_1^{-1})c^{-1}\in H,
\qquad
u_1^{-1}b u_1=(u_1^{-1}b v_2^{-1})(cd^{-1}e)^{-1}\in H.
\]
They would commute, contradicting the already checked noncommutation of \(a,b\).
Thus the finite-index step used for (P1) cannot simply be replaced by this explicit cyclic Laurent gauge certificate.
This exclusion concerns those diagonal group-monomial gauges, not arbitrary invertible rational changes of basis or a claimed classification of all cyclic realizations.

## An elementary row-splitting step

Let \(A\in M_{m,n}(\mathbb CG)\), and count the displayed group monomials in each complete row, including their input-coordinate labels.
Suppose row \(i\) has \(r>3\) terms, and write its first two terms as a row vector \(C\in M_{1,n}(\mathbb CG)\).
Thus \(Cx=c_1g_1x_{j_1}+c_2g_2x_{j_2}\), with the possibility \(j_1=j_2\).
Let \(A_0=A-e_iC\), and form
\[
\widetilde A=
\begin{pmatrix}A_0&e_i\\-C&1\end{pmatrix}.
\]
The new bottom equation defines one auxiliary variable as the sum of the two selected terms.
The original row now has \(r-1\) terms, and the new row has exactly three displayed terms.
Every other row is unchanged.
Direct multiplication gives
\[
\begin{pmatrix}I_m&-e_i\\0&1\end{pmatrix}
\widetilde A
\begin{pmatrix}I_n&0\\C&1\end{pmatrix}
=\operatorname{diag}(A,1).
\tag{U1}
\]
Both triangular multipliers are bounded group-ring units with explicitly bounded triangular inverses.
The only eliminated pivot is the scalar identity; no nonzero group-ring scalar is assumed invertible.
Consequently
\[
\operatorname{rk}_G\widetilde A=1+\operatorname{rk}_GA,
\qquad
\dim_G\ker\widetilde A=\dim_G\ker A.
\tag{U2}
\]
There is also a bounded module isomorphism \(x\mapsto(x,Cx)\) from \(\ker A\) onto \(\ker\widetilde A\), whose bounded inverse is coordinate projection.
Thus this particular step has no unbounded-domain issue.

Iterate with the written term lists, without optional cancellation.
The nonnegative integer
\[
K=\sum_{i=1}^m\max(r_i-3,0)
\]
decreases by exactly one at each step.
After \(K\) steps there is an \((m+K)\)-by-\((n+K)\) matrix \(B\) with at most three group monomial terms per whole row and
\[
\operatorname{rk}_GB=K+\operatorname{rk}_GA,
\qquad
\dim_G\ker B=\dim_G\ker A.
\tag{U3}
\]
The entries retain the original group monomials and added scalar identities, so a matrix initially affine in a fixed group tuple stays affine in that tuple.
Coincident labels or cancellations only reduce the actual support; they do not invalidate the displayed complexity decrease.

It follows that, for any fixed group \(G\), integer kernel dimension for every matrix with at most three monomial terms per whole row is equivalent to integer kernel dimension for every finite matrix over \(\mathbb CG\).
If one formulates the restricted assertion only for square matrices, pad a rectangular matrix with zero rows or columns before applying the construction; zero-column padding adds a known integer to its kernel dimension.
Torsion-freeness is not used in this equivalence.
In particular, deriving the unrestricted three-term assertion from torsion-freeness would prove the original Task, rather than merely extend a weak sparse case.
This does not rule out an induction; it identifies the exact strength required of its additional preserved structure.

## Source comparison and bounded search

The actual noncommutative identity (U1) is a direct application of the already inspected Coh06, Section 5.8, Higman stabilization, with its [source scope](../audits/literature/Coh06/Yin_U002.md#coh06-u002).
A bounded primary-source search on 2026-11-11 for matrix sparsification with three entries per row also found Alon and Yuster, *Matrix sparsification and nested dissection over arbitrary fields*, JACM 60(4), article 25 (2013), DOI [10.1145/2505989](https://doi.org/10.1145/2505989).
The inspected [author manuscript](../literature/pdf/AY13--author.pdf#page=4), Section 2.1, Theorem 2.1, pp. 3--4, states a field-valued sparsification with at most three nonzero entries in every row and column and an explicit rank shift.
This is related prior work, not an input to (U1)--(U3): its stated field hypothesis and entry count do not themselves prove the whole-row group-monomial claim over an arbitrary group ring.
The author manuscript's title page and Theorem 2.1 statement were inspected; its subsequent algorithmic proof and complexity claims were not audited.
The publication identity was checked against the authors' [institutional bibliographic record](https://cris.tau.ac.il/en/publications/matrix-sparsification-and-nested-dissection-over-arbitrary-fields/).
The search stops at these sufficient attribution and comparison facts; it makes no claim that this is the earliest additive row-splitting construction.

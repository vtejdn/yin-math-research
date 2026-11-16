---
author: Yin
---
# An index-two character and an exact coefficient test for half rank

## Statement

Let \(K\) be a discrete group with a subgroup \(H\) of index two.
Choose \(t\in K\setminus H\), put \(\sigma(h)=t^{-1}ht\), and suppose \(\chi:H\to\mathbb Z\) is nonzero with \(\chi\circ\sigma=-\chi\).
Then \(\chi(t^2)=0\).
Let \(c=u+tv\in\mathbb C[K]\), with \(u,v\in\mathbb C[H]\) both nonzero.
For either of these two coefficient sums write \(f_+,f_-\) for its highest and lowest \(\chi\)-degree parts and \(W(f)\) for the difference of those degrees.
Use canonical scalar regular ranks and the unnormalized extension of the trace to matrices.

* If \(W(u)>W(v)\) then \(2r_K(c)\ge r_H(u_+)+r_H(u_-)\).
  If \(W(v)>W(u)\) then \(2r_K(c)\ge r_H(v_+)+r_H(v_-)\).
* If the widths agree and \(u_+\) is a single term, the construction below gives a power series \(S(s)=\sum_{j\ge0}S_j s^j\) with coefficients in \(\mathbb C[H]\).
  Then \(r_K(c)\ge1/2\), and
  \[
          r_K(c)=\tfrac12\quad\Longleftrightarrow\quad S_j=0\text{ for every }j.
  \]
  If \(S_j\) is the first nonzero coefficient, then \(2r_K(c)\ge1+r_H(S_j)\).
  In particular, an injective first coefficient proves \(r_K(c)=1\).
* With the supports, subgroup and character fixed in this tied case, finitely many of the coefficient equations \(S_j=0\) cut out the exact half-rank locus on the coefficient torus.
  The conclusion is existential in the truncation order.
  On an effectively specified algebraic family, with effective exact group equality and algebraic coefficient equations, a search through successive truncations certifies absence of a half rank whenever none exists.

This test uses the character of the subgroup even when the group \(K\) itself has finite abelianization.
In that case every nonzero integral character of an index-two subgroup satisfies the required sign rule.
Indeed the invariant character \(\psi=\chi+\chi\circ\sigma\) extends to \(K\) over \(\mathbb Q\) by assigning \(\psi(t^2)/2\) to \(t\).
Invariance and the relation for \(t^2\) verify the extension on coset products, so finite abelianization forces \(\psi=0\).
Since \(t^2\) itself is fixed by \(\sigma\), the sign rule implies \(\chi(t^2)=0\).
This gives a possible further test on the [intrinsic finite-abelianization subgroup of a half-rank pair](Yin_C_A0024_v1.md#characters-and-the-two-orientations-of-cyclic-cosets).
Its hypotheses do not require amenability of \(K\), an Atiyah theorem for \(H\), or a division ring for its coefficients.

## Argument

Using the two right-\(H\)-module summands represented by \(1,t\), left convolution by \(u+tv\) is the matrix
\[
        M=\begin{pmatrix}u&t^2\sigma(v)\\v&\sigma(u)\end{pmatrix}
        \quad\text{over }\mathbb C[H].
\]
Its \(H\)-rank is \(2r_K(c)\), since the diagonal coefficients of the range projection at \(1,t\) are both the canonical \(K\)-trace.
Twist each group term \(h\) of all four entries by \(s^{-\chi(h)}\).
At \(|s|=1\) this twist is a trace-preserving automorphism of \(\mathcal N(H)\), implemented on the regular Hilbert space by multiplication by the unitary character.
Also multiply rows and columns by scalar powers of \(s\) as needed.
Whenever the resulting matrix is polynomial in \(s\), its rank supremum on \(\mathbb C\) equals the common rank on the circle.
Indeed the [one-variable Vandermonde estimate](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) gives at most countably many exceptions to the supremum for such bounded-coefficient matrices.
The same argument applies after polynomial elementary operations that are invertible at nonzero \(s\).

Let the largest heights in the four entries of \(M\), in row order, be \(\alpha,\beta,\gamma,\delta\).
The two sums \(\alpha+\delta,\beta+\gamma\) are \(W(u),W(v)\) by the sign rule.
If \(\alpha+\delta>\beta+\gamma\), use the doubled character \(2\chi\) and choose an integer \(k\) strictly between \(2(\beta-\alpha)\) and \(2(\delta-\gamma)\).
Give the first and second rows powers \(2\alpha,\ 2\delta-k\), and the two columns powers \(0,k\).
In the resulting polynomial matrix the highest diagonal parts are its constant diagonal, and the off-diagonal entries vanish at zero.
Its rank there is \(r_H(u_+)+r_H(u_-)\) since \(\sigma\) preserves trace.
If the other width is larger, interchange the columns first and argue in the same way, using invariance under multiplication by \(t^2\in H\).

For a tie, use the original character.
Multiply the rows by powers \(\alpha,\gamma\) and the columns by powers \(0,\beta-\alpha\).
The tie gives \(\gamma+\beta-\alpha=\delta\), so the resulting matrix has entries \(A(s),B(s),C(s),D(s)\) that are polynomials in \(s\), each with its top group terms in its constant coefficient.
Since \(A_0=u_+\) is a nonzero scalar times a group element, it is a unit already in \(\mathbb C[H]\).
Form the **ordered** series
\[
 E=C A^{-1},\qquad S=D-E B,\qquad
 E_j=\left(C_j-\sum_{i<j}E_i A_{j-i}\right)A_0^{-1},\qquad
 S_j=D_j-\sum_{i=0}^j E_i B_{j-i}.                                    \tag{1}
\]
All coefficients in (1) are finite group-ring sums.
The upper-left entry at zero already gives matrix rank at least one.
Suppose \(S_j\ne0\) and all earlier coefficients vanish.
Subtract \((\sum_{i=0}^j E_i s^i)\) times the upper row from the lower row and divide that lower row by \(s^j\).
These operations produce a polynomial matrix because the lower-left entry was divisible by \(s^{j+1}\) and the lower-right by \(s^j\).
At zero the diagonal of the upper triangular matrix is \(A_0,S_j\), giving rank \(1+r_H(S_j)\) by elimination of the upper-right entry using the invertible pivot.
Applying the circle argument to this polynomial matrix proves the lower bound.

Conversely, if all \(S_j\) vanish, \(A(s)^{-1}\) exists in operator norm for sufficiently small \(|s|\), by the Neumann series about \(A_0\).
Its norm-convergent Taylor series agrees term by term with the formal inverse in (1).
Thus the Schur complement vanishes on this disk, and ordinary bounded invertible row and column operations give matrix rank exactly one there.
The same polynomial generic-rank argument, now applied to the polynomial matrix **before** elimination, shows that its common circle rank equals one.
This proves the equivalence without evaluating a possibly divergent series at a unit-circle parameter.

With fixed support, every scalar coordinate of every \(S_j\) is a Laurent polynomial in the original nonzero coefficients by (1).
The Laurent polynomial ring on finitely many variables is Noetherian, so the ideal generated by all such coordinates is generated by finitely many of them.
Taking the largest order used by these generators gives a sufficient finite truncation.
Adding the equations of a specified algebraic family in the coefficient torus therefore gives an empty complex zero set exactly when some finite truncation already does.
Polynomial feasibility with inverse variables tests each truncation; an open constraint can likewise be imposed by adjoining the inverse of its defining nonvanishing polynomial.
Equality of the ideals at two consecutive orders by itself does not prove that every later order adds nothing.

## What a tied leading face detects

If both extremes of \(u,v\) consist of single group terms, write their group elements as \(h_+,h_-\in H\) and \(t v_+,t v_-\in tH\), with \(v_\pm\) here denoting just group elements.
The four entries at zero have group labels \(h_+,t^2\sigma(v_-),v_+,\sigma(h_-)\).
The two terms of \(S_0\) have different group labels unless
\[
                    (tv_+)h_+^{-1}(tv_-)=h_- .
\]
This follows by multiplying the required equality \(\sigma(h_-)=v_+h_+^{-1}t^2\sigma(v_-)\) on the left by \(t\) and on the right by \(t^{-1}\).
For a torsion-free \(H\) a binomial with distinct labels acts injectively, since after a unit translation it is a nonzero Laurent polynomial in an infinite-order element.
For coincident labels a nonzero scalar residual also has full rank.
Hence half rank requires both this group identity and equality of the products of the two within-coset endpoint coefficients.

In the strict-width case a singleton winning face and any other nonempty winning face already force rank greater than one half.
The same holds if both winning faces have at most four labels in a torsion-free group by the [four-point rank gap](Yin_C_A0027_v1.md#four-point-rank).
In the tied case, failure to find a nonzero leading determinant only selects the higher coefficients in (1).

## The second coefficient on the actual twelve-row support

Use [C_A0035, formula (4)](Yin_C_A0035_v1.md#the-true-fibers-and-all-binary-solutions) for the normalized row weights \(U_i\) on its six-parameter binary solution variety.
Denote the free scalar parameters there by \(a,b,c,x,y,z\) and the original group generators by \(X,Y\).
Use the [faithful Heisenberg sign representation](../ledger/Yin_L_A0043_v1.md#supports-multiplicities-and-a-faithful-calculation) with group elements \((p,q,k;i,j)\).
Take \(K=G_3,\ H=\{i=1\}\) inside the group image, \(t=Y\), and \(\chi=p\) on \(H\).
The affine multiplication formula makes \(\chi\) additive on \(H\), and conjugating by \(Y\) reverses its sign.
The same model gives the central Heisenberg translation \(h=(0,0,1;1,1)=(XY)^{-2}\), of infinite order.

For the row support, the endpoint indices \(h_+,h_-,tv_+,tv_-\) are \(2,10,11,5\); for the column support they are \(1,10,5,11\).
Both widths tie on each side.
The group equality above holds in each case and the two coefficient tests are \(U_2U_{10}=U_{11}U_5\) and \(V_1V_{10}=V_5V_{11}\).
Both hold identically in (4) of the cited Claim.
The first faces alone therefore give no exclusion on this entire binary family.

Here are the inputs to (1) through degree two for the **row** operator, specified by their vertex indices.
A row index \(i\) contributes \(U_i\) times its group label \(g_i\) in block \(A\), or \(\sigma(g_i)\) in block \(D\).
A label outside \(H\) contributes \(U_i\) times \(t^{-1}g_i\) in block \(C\), or \(t^2\sigma(t^{-1}g_i)\) in block \(B\).

| Degree | \(A\) | \(B\) | \(C\) | \(D\) |
| --- | --- | --- | --- | --- |
| 0 | 2 | 5 | 11 | 10 |
| 1 | 1,4 | 7,8 | 6,12 | 3,9 |
| 2 | 3,9 | 6,12 | 7,8 | 1,4 |

For direct multiplication set \(L=(1,0,1;1,-1)\) and \(J=(0,-2,-1;1,1)\).
The recurrence gives \(E_0=bL\), \(E_1=aJ-abxz/y^2\).
Since \(B_0=-(y/x)A_0\), add \(y/x\) times column one to column two and denote the two new entries in that column by \(B',D'\).
This leaves the Schur complement unchanged and gives \(B'_0=D'_0=0\).
Multiplying the entries in the table gives \(D'_1=E_0B'_1\), so \(S_0=S_1=0\).
At order two the product \(D'_2-E_0B'_2-E_1B'_1\) is
\[
\begin{aligned}
 S_2={}&-\left(ax/y+y^4/(x^2z^2)\right)h^{-1}\\
 &+\left(1+ay^3/(xz^2)+b^2y^4/(x^2z^2)+abz/y\right)\\
 &-\left(b^2+aby^3/(x^2z)\right)h .
\end{aligned}
\]
At \(a=b=c=x=y=z=1\) the result is \(4-2h^{-1}-2h\).
Every nonzero value of this Laurent polynomial in \(h\) gives \(r_{G_3}(\sum_iU_i g_i)=1\).
This includes a Zariski-open set of the binary parameter torus and every choice of positive real free parameters, since the coefficient of \(h^{-1}\) is strictly negative there.
At \(a=-1,\ b=c=x=y=z=1\) this entire second coefficient vanishes and the second-order test is insufficient.

The [known torsion-free elementary amenable case](../ledger/Yin_L_A0001_v1.md#known-positive-results) already supplies integrality for this particular group, which embeds in a finite extension of the Heisenberg group.
The example verifies how the finite rank calculation behaves on an actual family whose binary equations extinguish the leading terms.
In another group the test uses the finite group products and the index-two character directly.
It gives no conclusion for an input lacking the subgroup, character or specified leading pivot, and leaves the general [Atiyah question](../tasks/Yin_T_A0001_v1.md#contract) open.

## Assessment history

### Decision index-two-character

| Field | Value |
| --- | --- |
| date | 2026-11-17T01:56 |
| status | proved |
| reason | Independent mathematical review covers the statement, argument and their stated limitations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The anti-invariant character test, its finite coefficient equations at a tied monomial pivot, and the verified second-order calculation. |
| argument | [Proof](#argument) | Complete argument with its actual hypotheses and scope. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0068_v1.md#whole-argument-finding) | Independent review of the proof and its direct inputs. |

## Current assessment

[Selected decision](#decision-index-two-character)

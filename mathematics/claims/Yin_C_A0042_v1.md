---
author: Yin
---
# Complete lifting test at characteristic two for a cyclic quotient of order seven

## Statement

Let \(Q=C_7=\langle X\rangle\), and project two finite lists of group labels to \(Q\).
Within each list every occurrence has prescribed residue coefficient one in characteristic two.
On either side distinguish the **occupied classes**, which have at least one occurrence, from the **odd classes**, which have odd occurrence count.
The two parity indicators \(\bar a,\bar b\in\mathbb F_2[Q]\) are assumed to satisfy \(\bar a\bar b=0\).
The task here is to solve the projected equations, summing coefficients at each occupied class while preserving the nonzero residue on every individual occurrence.
A class of even positive multiplicity can have aggregate coefficient zero.

For lifting at the marked point, allowing a finite extension \(L/\mathbb Q_2\) means that each individual coefficient reduces to one modulo the maximal ideal of \(\mathcal O_L\).
Precision \(2^n\) means reduction modulo \(2^n\mathcal O_L\), independently of the ramification index.
The following table classifies all possibilities.
In the two middle rows with different sizes, \(m_j\) denotes the number of occupied classes on the side with \(j\) odd classes.

| Parity masks | Additional condition | Lift modulo \(4\) | Lift modulo \(8\) | Exact characteristic-zero lift at the point |
| --- | --- | --- | --- | --- |
| One parity indicator zero, or one side has all seven classes odd | None | Yes | Yes | Yes |
| One parity size three, the other four | \(m_3\ge4,\ m_4\ge5\) | Yes | Yes | Yes |
| One parity size three, the other four | Either size requirement fails | No | No | No |
| Both parity sizes four | At least one side has at least five occupied classes | Yes | Yes | Yes |
| Both parity sizes four | Each side occupies exactly its four odd classes | Yes | No | No |

The parity masks in the last four rows must satisfy the assumed zero product, which fixes opposite nontrivial Fourier orbits as described below.
Every positive answer in the table is realized over \(\mathbb Z_2\), and every negative answer persists over **all** finite ramified or unramified extensions.
An exact lift can be chosen in a number field at a place of local degree one above two.
Thus a lift modulo eight is sufficient for an exact lift of the projected equations in this case.
The [general local saturation criterion](Yin_C_A0039_v1.md#horizontal-specialization) does not assert this precision cutoff for other group tables.

## Separating the cubic factors

All seventh roots of unity lie in the unramified cubic extension of \(\mathbb Q_2\), since \(\mathbb F_8^\times\) has seven elements and the roots of \(X^7-1\) are simple modulo two.
Choose a primitive root \(\zeta\) whose reduction \(\omega\) satisfies \(\omega^3+\omega+1=0\).
Besides the trivial frequency, the two Frobenius orbits are indexed by \(\{1,2,4\}\) and \(\{3,5,6\}\) among the powers of \(\zeta\).
For the first orbit put
\[
 \eta=\zeta+\zeta^2+\zeta^4,\quad \eta'=\zeta^3+\zeta^5+\zeta^6=-1-\eta,\qquad
 f(X)=X^3-\eta X^2+\eta'X-1 .
\]
Multiplying the two orbit sums gives \(\eta\eta'=2\).
The reduction of \(\eta\) is zero by the trace coefficient of the chosen cubic, while that of \(\eta'\) is one.
Both therefore belong to \(\mathbb Z_2\): the two roots of \(Y^2+Y+2\) lift the distinct roots zero and one by Hensel's lemma.
In particular \(v_2(\eta)=1\), and \(\mathbb Q(\eta)\) is a number field embedded in \(\mathbb Q_2\).
The roots of \(f\) are exactly this orbit, by the elementary symmetric functions of those three roots.
The other orbit is obtained by inverting the group generator.

The Fourier matrix on \(Q\) is invertible over the integer splitting ring and modulo every \(2^n\), because every difference of two distinct seventh roots is a unit.
The same is true upon adjoining the roots to any proposed ramified extension.
If a factor is a unit at a frequency after reduction, the value of the other factor there must vanish modulo the tested precision.
Vanishing at a full cubic orbit is equivalent to the vanishing of the three coefficients of the remainder modulo its monic cubic, by the invertible three-point Vandermonde matrix.
At the trivial frequency the required value is the augmentation.

The nonzero residual Fourier values of either indicator form a union of Frobenius orbits, and the two unions are disjoint.
A vector with only the trivial frequency active is precisely the full-group indicator.
That case and a zero parity vector lift by elementary signs: cancel paired occurrences class by class, and, for a full-group indicator, use equal numbers of positive and negative signs on its partner's even parity support.
For a zero parity vector all its projected sums can be made zero.
These are integer lifts of the projected occurrence equations.

In all remaining cases each factor is active on one nontrivial orbit and vanishes on the other, with distinct active orbits for the two factors.
For a prescribed vanishing orbit, invert the labels if necessary so its cubic is \(f\).
The nonzero vectors \(1,\omega,\ldots,\omega^6\) exhaust \(\mathbb F_2^3\).
The seven translates of \(\{0,1,3\}\) modulo seven index the three-element sets with vector sum zero: one is given by \(\omega^3=1+\omega\), translation multiplies by a nonzero scalar, and there are exactly seven two-dimensional subspaces in \(\mathbb F_2^3\).
Their seven complements also have sum zero, as do the empty and full sets.
This accounts for all \(2^{7-3}\) vectors in the kernel of evaluation at \(\omega\).
Thus the remaining odd masks are precisely those triples or quadruples, after the possible inversion of labels.
A triple is a unit at the trivial frequency; a quadruple is zero there.
Two triples cannot be partners.

## The two small determinants

For the classes on one side take the three rows of the remainder map modulo \(f\) in the basis \(1,X,X^2\).
When augmentation must also vanish, place the row of ones above these three rows.
Modulo two the corresponding columns are \(\omega^i\) and \((1,\omega^i)\), respectively, in binary coordinates.
An invertible maximal minor modulo two allows exact lifting of a compatible binary solution: choose lifts of the other coordinates and solve for the pivot coordinates by the inverse minor.
This preserves their prescribed residues.
The entries of the matrix and inverse minor lie in \(\mathbb Q(\eta)\) and are integral at the chosen place.

With just the three remainder equations, four or more occupied classes give full row rank modulo two, since a proper subspace contains at most three of the seven distinct nonzero vectors.
The exceptional triple mask occupying just three classes is a translate of \(\{0,1,3\}\) in the chosen orientation.
For these columns the determinant is \(\eta\), as \(X^3=1+(1+\eta)X+\eta X^2\) modulo \(f\).
Translation of the class labels acts invertibly by \(X^j\) modulo \(f\) since \(f\) divides \(X^7-1\).
It affects the determinant only by a unit and a possible reordering sign.
Consequently the marked triple cannot solve the remainder equations even modulo four, including after arbitrary ramification: the adjugate would make a determinant of valuation \(v_L(2)\) times each unit coordinate zero modulo \(4\).

For a quadruple mask, its four reduced columns \(\omega^i\) form the affine plane complementary to the two-dimensional linear subspace of the omitted line.
Any three of the four are linearly independent, because no three points of this affine plane have sum zero.
The augmented columns \((1,\omega^i)\) of the four have rank three, and adding any of the remaining three classes gives rank four.
Thus five or more occupied classes permit exact lifting with both augmentation and cubic remainder zero.

For the four columns of the representative quadruple \(\{2,4,5,6\}\), the matrix including augmentation is
\[
 \begin{pmatrix}
   1&1&1&1\\
   0&\eta&-1&-1-\eta\\
   0&-1&-1&-\eta\\
   1&-1&-1-\eta&1
 \end{pmatrix}.
\]
The last three rows follow by successive multiplication by \(X\) modulo \(f\).
Its determinant is \(4+\eta\), of valuation one over \(\mathbb Q_2\).
Translation preserves this valuation, acting trivially on the augmentation and invertibly on the remainder coordinates.
Write \(v_L\) for a valuation in any extension containing the splitting field.
If all four coordinates are units with the marked residues and the cubic remainder vanishes modulo \(2^n\) for \(n\ge2\), then their augmentation \(s\) has
\[
                              v_L(s)=v_L(2).
\]
Indeed, multiplying the vector of outputs \((s,0,0,0)\bmod 2^n\) by the adjugate gives the determinant times the four input units modulo \(2^n\).
The cofactors of the augmentation row are units by the independence of every three remainder columns modulo two.
The congruence therefore forces the indicated valuation, which is strictly less than that of \(2^n\).
The statement concerns any representatives of the augmentation modulo \(2^n\).

## Completing the lift and distinguishing the two precisions

In a triple-quadruple pair, the triple side needs just the cubic remainder condition, and the quadruple side must also have zero augmentation because the triple augmentation is a unit.
The two determinant tests give necessity at precision four and exact sufficiency under the stated occupied counts.
On the lifted pair the two active cubic orbits are separated and the product at the trivial frequency is zero, so the full product is zero.

In a quadruple-quadruple pair there is a common residual zero only at the trivial frequency.
Each side can be lifted with its required cubic remainder exactly zero, even with just four occupied classes.
Each augmentation is even over \(\mathbb Z_2\), so their product vanishes modulo four.
If either side occupies five or more classes, impose zero augmentation on that side to obtain an exact lift.
If both sides occupy exactly four, a solution modulo eight would require each opposite cubic remainder to vanish modulo eight.
The second determinant then forces both augmentations to have valuation \(v_L(2)\); their product cannot vanish modulo eight.
This proves the full table, including after arbitrary finite extensions.

To pass from aggregate coordinates to the prescribed occurrences at any positive precision or exactly, assign one to all but the last occurrence of an occupied class.
If its count is \(m\) and its prescribed lifted sum is \(s\), assign \(s-(m-1)\) to the last.
Its residue is one and the sum is correct.
Unoccupied classes must be zero in all the linear calculations.
In the nontrivial cubic cases where the table gives an exact lift, one can even require every occupied **aggregate** to be nonzero in characteristic zero.
Every three distinct remainder columns are independent in characteristic zero, since they are independent modulo two or form one of the determinant-\(\eta\) triples.
Likewise any four augmented columns are independent: an affine dependence of four distinct binary points occurs only for one of the seven complementary planes, whose determinant was checked above.
This characteristic-zero independence is also a special case of Chebotarëv's prime-order Fourier minor theorem, proved in [Tao, Lemma 1.3](https://arxiv.org/pdf/math/0308286v6#page=3).
The two displayed determinant valuations supply the extra information used at finite precision here.
In the successful cases there is at least one more occupied column than the number of imposed rows.
Deleting any one column still leaves a full-rank matrix, so the characteristic-zero kernel is not contained in any coordinate hyperplane.
Starting at a lift, add a sufficiently divisible multiple of a kernel vector over \(\mathbb Q(\eta)\) avoiding all coordinate hyperplanes; this preserves all residues and can keep every occupied aggregate nonzero.
The occurrence convention also covers a side with zero parity vector where an identically zero aggregate factor was used.

## Exact masks and an example failing first at eight

With one occurrence for every listed point, the ordered nonempty support pairs giving zero product modulo two number \(420\).
The full-indicator cases contribute \(2(\binom72+\binom74+\binom76)=126\) pairs lifting by signs over the integers.
There are two orders of the distinct cubic orbits, seven choices of each orbit's triple or complementary quadruple, and two placements of the odd augmentation in a triple-quadruple pair.
Thus \(196\) pairs already fail modulo four, including the [sparse seven-cycle obstruction](../ledger/Yin_L_A0045_v1.md#three-obstructing-product-fibers-in-a-cyclic-quotient-of-order-seven).
The other \(98=2\cdot7^2\) pairs first fail modulo eight.
All these counts refer to ordered supports with their actual group labels and no quotient by rotations.

For example, use the row support \((2,4,5,6)\) with coefficients \((-1,-1,-1,1)\) and the column support \((1,2,3,5)\) with coefficients \((-1,1,1,1)\), writing labels additively modulo seven.
Their product over \(\mathbb Z[Q]\) is \(-4\) times the identity element, by collecting the sixteen terms.
The two odd masks are complements of opposite oriented lines, so the valuation argument excludes **every** lift of this marked point modulo eight even though the displayed signs solve it modulo four.
For [A0001](../tasks/Yin_T_A0001_v1.md#contract), a verified quotient with the specified occupied and odd masks can therefore obstruct lifting a particular characteristic-two construction before one knows all the original product fibers.
A successful quotient lift imposes only the summed quotient equations, and the group \(C_7\) in this calculation has torsion.

## Assessment history

### Decision precision-eight

| Field | Value |
| --- | --- |
| date | 2026-11-17T02:27 |
| status | proved |
| reason | Independent mathematical review covers the full argument and its limitations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All marked occurrence masks, including arbitrary finite ramification and the first obstructed precision. |
| argument | [Proof](#separating-the-cubic-factors) | Complete argument under the stated hypotheses. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0073_v1.md#whole-argument-finding) | Independent review of these conclusions and their inputs. |

## Current assessment

[Selected decision](#decision-precision-eight)

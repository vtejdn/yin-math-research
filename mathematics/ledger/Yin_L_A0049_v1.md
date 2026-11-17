---
author: Yin
---

# A finite integral feasibility test for prescribed type and color parities

Fix either side of the Ope26f matching prescription, any permitted inverse pairing, and any prescribed increments \(\eta(\bar t)=-\eta(t)\) in \(C_7\).
All three are fixed throughout the test.
Let \(T_\tau\) be the prescribed integral total of full type \(\tau\) at an admissible size \(n\). [Ope26f, §2.1](../literature/pdf/Ope26f.pdf#page=4)
The matching condition equates the integer stub counts of inverse letters after shifting colors.
With a specified parity for **each** type-color entry, the following are equivalent.

1. There is a signed integral solution with precisely the type totals \(T_\tau\) and the specified parities.
2. There is a solution with those parities to the stub equations and the type totals modulo \(256\).
3. After adding a sufficiently large balanced block with even entries, there is a nonnegative integral realization with the same parities and the correspondingly enlarged prescribed totals.

The source proportions are preserved under the balanced enlargement.
Without that enlargement the bound and equivalence with item 2 concern signed solutions.
For prescribed aggregate parities alone one may leave the individual entries as variables subject to their aggregate equations modulo two.
The modulus \(256\) is a uniform sufficient precision.
Whether a smaller modulus suffices for all fixed inverse pairings and increments remains open here.

## A right inverse up to a power of two

Let \(R=\mathbb Z[C_7]\), write \(X\) for the group generator and \(\mathcal N=1+X+\cdots+X^6\).
One type histogram is an element \(Y_\tau\in R\) with augmentation \(T_\tau\).
Define the \(R\)-linear map \(A\) by taking the stub histogram at \(\bar t\) minus \(X^{\eta(t)}\) times the stub histogram at \(t\), one equation per oriented inverse pair.
Each histogram is summed over the types carrying its letter.
The source prescribes equal total counts for inverse letters.
Hence \(AY\) always has augmentation zero in every coordinate when \(Y\) has the required type totals.

Let \(N\) be the \(16513\)-by-\(16513\) point-by-line incidence matrix and \(J\) the all-ones matrix of that size.
Each line and point has \(129\) incidences and two distinct points determine one line.
Consequently \(NN^{\mathsf T}=128I+J\) and
\[
                         N(129N^{\mathsf T}-J)=128\cdot129\,I .
\]
On just the empty-extra type of each line the map \(A\) is \(E N\).
The rows of \(E\) compare disjoint pairs of ordinary points, except for the three mixed ordinary-extra pairs, whose rows each have only their one ordinary point.
Every such row has nonempty support, distinct rows have disjoint supports, and each nonzero entry is \(\pm X^c\).
Thus \(E\) has an \(R\)-linear right inverse obtained by using one ordinary endpoint per row.
It preserves the augmentation-zero constraint on each entry.
In particular, for any augmentation-zero output \(r\), select \(w\) with \(Ew=r\) using this inverse.
Put \(K=(129N^{\mathsf T}-J)w\) on the empty-extra types and zero on all others.
Then \(AK=128\cdot129\,r\) and every entry of \(K\) has augmentation zero.

## Correcting a lift modulo 256

Choose integral representatives \(Y_\tau\) of a solution in item 2.
Changing one coordinate per type by a multiple of \(256\) gives its original exact total \(T_\tau\), preserving all congruences.
Now \(AY=256r\) with each \(r_t\) of augmentation zero.
Using \(K\) from the previous section, set
\[
               Y'_\tau=645Y_\tau-10K_\tau-92T_\tau\mathcal N .
\]
The last vector \((T_\tau\mathcal N)_\tau\) satisfies the stub equations exactly, since each shift fixes \(\mathcal N\) and the total counts of \(t,\bar t\) are equal.
Since \(645=5\cdot129\), we have \(645\cdot256=10\cdot128\cdot129\), hence \(AY'=0\).
The equality \(645-7\cdot92=1\) gives the exact original totals, and reduction modulo two leaves \(Y'\equiv Y\).
This proves item 1 for arbitrary admissible \(n\), including when the original totals are not divisible by seven.
Item 1 implies item 2 by reduction.

For every type there are positive integral counts in a uniform seven-color block at an admissible multiple of \(14(16513)^2\).
Twice this full block is positive, even in every entry, balanced in every color, and satisfies every prescribed stub shift.
Adding sufficiently many copies removes all negative entries without changing the parities.
Each resulting integer equality of block sizes admits a matching of named stubs by a bijection, independently on the two sides.
Conversely subtracting any such added blocks from a realization gives a signed solution at the original totals.
For a two-sided test the same number of blocks may be added to both sides.
These algebraic implications do not prove connectedness or any geometric safeguard for arbitrary choices of the bijections.

## Many binary solutions cannot lift

The rank obstruction can already be seen on the augmentation-zero deviations, independently of any choice of source type totals.
The two nontrivial factors of \(\mathbb Z_2[C_7]\) are copies of the ring of integers \(\mathcal O\) of the unramified cubic extension, each with residue field \(\mathbb F_8\).
Indeed the two distinct cubics of the cyclotomic polynomial modulo two lift to coprime monic cubics, with roots the two Frobenius orbits of primitive seventh roots. [Cubic factors and unramified splitting](../claims/Yin_C_A0042_v1.md#separating-the-cubic-factors)
The augmentation-zero module identifies with these two factors.
In either factor all \(8258\) rows of \(A\) are independent over the fraction field of \(\mathcal O\), by the right inverse up to \(128\cdot129\) already proved.

Over characteristic two the rank of the ordinary point-line matrix is at most \(1+3^7=2188\).
To see this, extend the residue field to one containing \(\mathbb F_{128}\) and choose representatives for projective points and lines.
The incidence indicator of a point \((x,y,z)\) with the line \((a,b,c)\) is \(1+(ax+by+cz)^{127}\).
As \(127=\sum_{j=0}^6 2^j\), the power is the product of the seven Frobenius powers of the linear form.
Its expansion has at most \(3^7\) terms, each the product of a monomial in the point coordinates and a monomial in the line coordinates.
Including the constant gives the stated rank bound, which descends because ranks of matrices are unchanged by field extension.
The ordinary stubs of full types just repeat the incidence columns of their lines.
The three extra stub rows on the first side have sum zero in characteristic two, since each full type has either zero or two extras.
On the second side the three extra rows are equal.
Thus the entire stub matrix, and therefore its composition with the shifted comparison map, has residue rank at most \(2190\) on the first side and \(2189\) on the second.

In each nontrivial Fourier factor, Smith normal form over the discrete valuation ring \(\mathcal O\) now shows that the reduction of the exact kernel has codimension at least \(8258-2190=6068\), respectively \(8258-2189=6069\), in the binary kernel, measured over \(\mathbb F_8\).
Indeed the exact kernel of a map of full row rank is a direct summand of the free source of complementary rank, while the binary kernel has dimension determined by the smaller residue rank.
The integral reduction is contained in that \(2\)-adic reduction, so the same directions are impossible for integer solutions.
In fact there is no further loss for exact integral augmentation-zero deviations: the kernel of the corresponding map of free abelian groups is a direct summand, with complementary summand mapping injectively to its image, and tensoring its integer Smith form with \(\mathbb Z_2\) preserves that kernel.
The bound \(128\) annihilates the \(2\)-primary cokernel in each factor, by the displayed right inverse and the fact that \(129\) is a unit there.
This explains the single extra factor of two in the correction precision for lifting a fixed parity.

At a balanced admissible baseline these missing directions give actual binary perturbations satisfying all type-total and shifted stub congruences modulo two, but admitting no exact signed lift and hence no realization after even balanced enlargement.
The rank gap does not specify which **aggregate masks** fail.
On augmentation-zero deviations the aggregate of the realizable reductions is an ideal of \(\mathbb F_2[C_7]\) in its augmentation ideal, by addition and cyclic translation of integral solutions.
The four possibilities consist of zero, either one of the two \(\mathbb F_8\) components, or both.
The finite congruence test distinguishes membership without identifying the full binary kernel with its liftable part.
In particular the [binary construction for every permitted inverse pairing](Yin_L_A0048_v1.md#a-line-code-vector-for-the-given-inverse-pairing) cannot be declared liftable or unliftable merely by this dimension count.

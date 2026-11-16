---
author: Yin
---
# Small quotient groups in the first lifting test

Given a zero product on specified supports over \(\mathbb F_2[G]\), a homomorphism to a finite group \(Q\) gives necessary equations for lifting it on those supports.
Treat each original row and column as a separate occurrence with unknown odd coefficient, and sum its coefficients over equal images in \(Q\).
A failure of the [modulo-four test](../claims/Yin_C_A0038_v1.md#the-incidence-matrix-and-lifting) on the coarser product fibers rules out an odd lift modulo four on the original ones.
The argument also applies to group-labelled vertex occurrences when every occurrence coefficient is to be odd.

## Quotients of order at most four

Every such projected zero product over a group \(Q\) of order at most four admits an integral solution of the projected equations with every occurrence coefficient in \(\{1,-1\}\).
This holds with arbitrary repetitions and missing quotient labels.
Record \(A,B\subset Q\) as the classes occurring an odd number of times on the respective sides.
Their indicator sums in \(\mathbb F_2[Q]\) have zero product.
At each class pair off the repeated occurrences with coefficients \(1,-1\), leaving one occurrence for each odd class.
If one parity set is empty, this already makes its projected factor zero, and the other factor can use arbitrary signs.
It remains to find signs for the two nonempty parity sets.
Whenever one set is the whole group and the other has even size, use coefficients one on the whole group and equally many signs of each kind on the other set.
Their product vanishes integrally because multiplication by any group element permutes the whole-group sum.

For the trivial group there is no nonempty pair left to consider.
For \(C_2\), two nonempty parity sets with zero product must both be the whole group, since singleton sums are units.
For \(C_3=\langle x\rangle\), the factorization \(X^3-1=(X-1)(X^2+X+1)\) over \(\mathbb F_2\) gives a product of two fields.
A nonzero zero pair has one factor divisible by \(X^2+X+1\), the whole-group sum in the degree-less-than-three representatives, and the other has even augmentation.

For \(C_4=\langle x\rangle\) use \(\mathbb F_2[X]/((1+X)^4)\).
The orders of two nonzero annihilating factors in \(1+X\) sum to at least four.
A factor of order three is the whole-group sum \((1+X)^3\), with an even-size partner.
Otherwise both have order two, hence both are multiples of \(1+X^2\).
Their supports are unions of pairs exchanged by \(x^2\), since \((1+X^2)(c+dX)\) already describes every such multiple.
Give the first factor coefficient one throughout and give opposite signs on each pair of the second.
Their product vanishes because \((1+x^2)(1-x^2)=0\).

For \(C_2\times C_2\), an odd-size indicator is a unit over \(\mathbb F_2\), since its square is the identity.
A nonzero zero pair therefore has even-size supports.
Unless one is the whole group, each is a two-point translate of \(\{1,d\}\) for some involution \(d\).
Distinct nonidentity differences \(d,e\) give four distinct terms in \((1+d)(1+e)\).
Thus the differences agree, and the signs lifting \((1+d)(1-d)=0\) work.
These cases establish the stated integral compatibility on the quotient equations.

## Three obstructing product fibers in a cyclic quotient of order seven

In \(C_7=\mathbb Z/7\), take \(A=\{0,1,3\}\), \(B=\{0,1,2,4\}\), each with one occurrence of each listed element.
Adding the twelve pairs gives two representations for each label \(0,1,\ldots,5\) and none for 6, hence a zero product over \(\mathbb F_2\).
The fibers at \(2,4,5\) are respectively
\[
     \{(0,2),(1,1)\},\qquad
     \{(0,4),(3,1)\},\qquad
     \{(1,4),(3,2)\}.
\]
Their six cells have even degrees at every row and column.
Thus they obstruct a lift modulo four.
In fact they exclude any coefficients with these exact two supports over every field of characteristic different from two.
The first two equations force \(V_2=-U_1V_1/U_0\) and \(V_4=-U_3V_1/U_0\).
Then \(U_1V_4=U_3V_2\ne0\), whereas the third equation forces opposite values.
This also excludes any characteristic-zero lift of a residue point on these exact supports over a ramified extension field.

For application to a quotient of another group, it suffices that these sets are precisely the occupied quotient classes and that their occurrence counts are all odd.
In that case their summed coefficients must remain odd units modulo four and nonzero in a characteristic-zero valuation ring lifting the same residue point.
Seeing only these *parity* sets permits additional even-multiplicity occupied classes with nonzero even lifted sums.
Their additional terms can invalidate the displayed equations.
In full generality apply the criterion to the coarser fibers on the original occurrence rectangle, retaining every incident vertex.
No realization of this table as a quotient of the source group Ope26f is assumed.

## Full occupancy in odd order

When \(|Q|\) is odd and every class of \(Q\) occurs on both sides, the projected equations always admit a lift modulo four for any all-ones zero product modulo two.
Indeed let \(\bar a,\bar b\) be the projected elements of \(S=\mathbb F_2[Q]\) with \(\bar a\bar b=0\).
Maschke's averaging argument applies since \(|Q|\) is odd.
In particular, averaging a linear projection onto the right ideal \(\ker L_{\bar a}\) under the right \(Q\)-action gives a right \(S\)-linear projection.
This projection is left multiplication by an idempotent \(\bar e\), its value at the identity.
Then \(\bar a\bar e=0\) and \(\bar e\bar b=\bar b\).

Lift \(\bar e\) arbitrarily to \(e\in(\mathbb Z/4)[Q]\) and put \(E=3e^2-2e^3\).
The difference \(E-e=-(2e-1)(e^2-e)\) vanishes modulo two.
The identity \(E^2-E=(e^2-e)^2(4e^2-4e-3)\) gives \(E^2=E\), since \(e^2-e\) is a multiple of two.
If \(a_0,b_0\) are any lifts of \(\bar a,\bar b\), the pair \(a_0(1-E),Eb_0\) lifts them and has zero product.
At a class with \(m\ge1\) occurrences every prescribed modulo-four sum of parity \(m\) can be realized by signs, since changing one sign changes the sum by two modulo four.
Full occupancy therefore realizes every coefficient of this lifted pair on the original occurrence sets.
In particular a quotient of odd order can provide a modulo-four obstruction only if at least one side omits a quotient class.

---
author: Yin
---

# Algebraic parameters of maximal rank and the amenable strong Atiyah conjecture

## Statement

For a discrete group \(G\) and a rectangular affine pencil \(P(z)=A+zB\) over \(\mathbb ZG\), use the canonical group trace and the unnormalized matrix trace to define its rank.
Consider the following universal assertions over finitely generated torsion-free amenable groups.

1. Every group in the class satisfies the complex strong Atiyah conjecture.
2. For every such group and pencil, only finitely many complex parameters have rank below the maximum.
3. Every such pencil attains its complex maximum at some algebraic number.

These assertions are equivalent.
One may also ask for an integer point in assertion 3.
More precisely, if a group \(K\) in the class fails the conjecture, put \(W=(K^3)\wr\mathbb Z\).
There is a rectangular pencil over \(\mathbb ZW\) whose maximal-rank locus is exactly \(\mathbb C\setminus\overline{\mathbb Q}\).
The construction guarantees a drop from the generic rank and allows a fixed kernel at all parameters.

The [rational coefficient criterion](Yin_C_A0162_v1.md#statement) uses attainment of maximal rank to specialize rational expressions.
Even a one-variable, integer-input consequence of that hypothesis, imposed throughout the torsion-free amenable class, is equivalent to the complex strong Atiyah conjecture throughout that class.
This leaves open whether the [unrestricted finite-rank equation](../tasks/Yin_T_A0003_v3.md#contract) is sufficient there by a different argument.

## Argument

### A zero divisor with algebraic coefficients

If the complex strong Atiyah conjecture holds for \(G\), all ranks of \(P(z)\) are integers.
If the maximum is positive, the rank-drop locus is the sublevel at one less than that maximum.
It is a proper [Zariski closed set](Yin_C_A0128_v1.md#statement) in the complex line and hence finite.
If the maximum is zero the locus is empty.
This proves the forward implications, including integer attainment.

Suppose now that \(K\) fails the conjecture.
By [finite scalar descent for amenable groups](Yin_C_A0001_v2.md#finite-scalar-descent-and-a-complete-conditional-kernel-witness), there are nonzero \(a,b\in\mathbb CK\) with \(ab=0\).
Keep their finite supports, use separate variables for both coefficient lists, and normalize one nonzero coefficient in each list to one.
The coefficient equations for the zero product and these two normalizations are polynomials over \(\mathbb Q\) with a common complex solution.
They generate a proper ideal of a polynomial ring over \(\mathbb Q\).
The residue field of any maximal ideal containing it is a finite extension of \(\mathbb Q\) by the [weak Nullstellensatz, Theorem 10.34.1(1)](../audits/literature/The26b/Yin_U002.md#residue-fields-of-finite-type-algebras).
Embedding that field in \(\mathbb C\) gives a new pair \(a,b\) with the same two designated coefficients equal to one and \(ab=0\).
Choose a finite normal extension \(E/\mathbb Q\) in \(\mathbb C\) containing the coefficients and their complex conjugates.

Write \(D=a^*a\in EK\), and let \(p\) be the kernel projection of \(D\).
The nonzero range of \(b\) lies in its kernel, and \(a\ne0\), so \(0<\tau(p)<1\).
This step uses only the projection as a bounded group von Neumann operator.
Its membership in the division closure would be an additional property.

### Independent projections at the lamps

The base \(H=\bigoplus_{\mathbb Z}K^3\) of \(W\) has three independent copies of \(p\) at each height.
Their shifts at all heights commute, and the trace of a finite product using distinct copies is the product of the individual traces.
This follows from the tensor product of the canonical traces on the factors of any finite subproduct.
In one copy we observe either the projection \(p\) or its complement, obtaining a binary coordinate.
The three coordinates at a height therefore give eight letters, and every finite word, including its prescribed bordering letters, has positive probability.
The joint law is the product of these eight-letter distributions, and the shift of \(W\) translates the height coordinate.

In the finite von Neumann algebra of \(W\), the shift and these commuting projections realize the regular probability-space action of this shift.
Indeed for a function \(f\) of finitely many coordinates the group trace of \(f t^n\) vanishes when \(n\ne0\), by the disjoint height cosets of the base, and equals its product-measure integral when \(n=0\).
Norms in the trace Hilbert space of finite sums of such products are thus exactly those in the regular crossed-product representation.
The map extends to a unitary of those trace Hilbert spaces intertwining left multiplication, hence gives a trace-preserving isomorphism of the generated von Neumann algebras.

Use one of the eight letters as a delimiter and use the [two-coordinate interval pencil](Yin_C_A0162_v1.md#the-integral-pencil-on-lamplighter-intervals) with these projections and the shift.
Denote the resulting bounded operator by \(T(z)=C_0+zC_1\).
Almost surely the delimiters yield finite intervals in both directions, since every letter has positive probability and heights are independent.
The finite block for a word \(w\) has a one-dimensional kernel precisely at the roots of its polynomial \(p_w\).
These polynomials include all nonconstant integer polynomials with positive leading coefficient, and every \(p_w\) is nonzero.
At a root, the associated cylinder has positive probability and the kernel has nonzero trace there.
At any transcendental parameter every block is injective.
Thus the nullity of \(T(z)\) is positive exactly on \(\overline{\mathbb Q}\).
This use of the interval pencil requires positivity of each letter probability and does not require them to be equal.

### Eliminating the lamp projections without inverting them

The entries of \(C_0,C_1\) are finite sums of products of shifts, group-ring coefficients and the three lamp projections or their complements.
We now replace each occurrence of a lamp projection by finitely many homogeneous group-ring equations, using the [graph construction for regular-closure operators](Yin_C_A0158_v1.md#group-ring-equations-for-a-regular-closure-matrix).
For the appropriate translated copy of \(D\) and an input \(v\), use an auxiliary variable \(w\) satisfying \(D^2w=Dv\).
The output \(v-Dw\) is uniquely \(pv\), and the output \(Dw\) is uniquely \((1-p)v\).
Indeed the affiliated relative inverse \(D^{[-1]}\) gives the particular solution \(w=D^{[-1]}v\), and the difference between any two solutions lies in \(\ker D^2=\ker D\).
These are equations of right modules over \(U_W\), the affiliated ring of \(W\).

Introduce separate output variables for every intermediate operation in finite expressions computing \(C_0v\) and \(C_1v\) on an input column \(v\) of length two.
Group multiplications, addition and copying require only equations over \(EW\).
Denote the two final output columns by \(y_0,y_1\), and impose \(y_0+zy_1=0\).
All equations together form a rectangular affine pencil \(L(z)\) over \(EW\).
The projection of its affiliated kernel to \(v\) is surjective onto \(\ker T(z)\), since the intermediate outputs are uniquely determined and lifts exist at every operation.
When \(v=0\), all intermediate outputs vanish, and each occurrence of the auxiliary \(w\) is free in its fixed kernel of \(D\).
Only its output, already zero, enters later operations.
The kernel of the coordinate projection is consequently independent of \(z\).
Additivity of affiliated module dimension gives a constant \(\gamma\) with
\[
                   \operatorname{rk}_W L(z)=\gamma-\dim_W\ker T(z).
\]
Equivalently the kernel sequence splits over \(U_W\), since an affiliated matrix kernel is generated by its orthogonal projection.
The maximum is attained exactly at the transcendental parameters.

### Restriction to integer coefficients

Represent the coefficients of \(E\) by their \(\mathbb Q\)-linear multiplication matrices in a fixed basis of \(E\), leaving the scalar parameter \(z\) free.
Over \(\mathbb C\), a constant change of bases gives a direct sum of the conjugate pencils \(L^\sigma(z)\), one per embedding of \(E\).
This is [restriction of scalars in characteristic zero](Yin_C_A0159_v1.md#transporting-inner-inverses-between-coefficient-fields).
The group \(W\) is finitely generated, torsion-free and amenable, since its base is a restricted direct sum of finite products of \(K\) and its quotient is infinite cyclic.
In particular \(W\) is sofic, and [invariance of group-matrix rank](Yin_C_A0007_v10.md#scalars-in-the-division-closure-on-a-sofic-group) applies to every extension \(\widetilde\sigma\) of \(\sigma\) to an automorphism of \(\mathbb C\).
For every \(\lambda\), the rank of \(L^\sigma(\lambda)\) equals the rank of \(L(\widetilde\sigma^{-1}(\lambda))\).
All summands thus attain the same maximum at every transcendental parameter and fall below it at every algebraic parameter.
Multiplication by a common nonzero integer clears the denominators in the two rational coefficient matrices.
This gives the asserted integer pencil, refutes assertion 3 under the assumed failure at \(K\), and completes the equivalence.

## Assessment history

### Decision algebraic-rank-attainment

| Field | Value |
| --- | --- |
| date | 2026-11-25T13:44 |
| status | proved |
| reason | A single intermediate-rank lamp produces the word distributions and fixed auxiliary equations needed to realize all algebraic parameters as rank drops of an integer pencil. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Equivalence of algebraic maximal-rank attainment and the complex strong Atiyah conjecture throughout the torsion-free amenable class. |
| argument | [Argument](#argument) | Algebraic coefficients for a zero product, independent lamp projections, elimination with fixed auxiliary nullity and restriction of scalars. |
| dependency | [Amenable scalar descent](Yin_C_A0001_v2.md#finite-scalar-descent-and-a-complete-conditional-kernel-witness) | A nontrivial finite zero product after a failure of integrality. |
| dependency | [Rank sublevels](Yin_C_A0128_v1.md#statement) | The finite exceptional set under integral ranks. |
| dependency | [Finite residue fields](../audits/literature/The26b/Yin_U002.md#the26b-u002) | Theorem 10.34.1(1) for descent of the zero product to a number field. |
| dependency | [Interval pencil](Yin_C_A0162_v1.md#the-integral-pencil-on-lamplighter-intervals) | Word encoding and its dependence on positive letter probabilities. |
| dependency | [Graph equations](Yin_C_A0158_v1.md#group-ring-equations-for-a-regular-closure-matrix) | Encoding a projection by affiliated equations over the group ring. |
| dependency | [Coefficient descent](Yin_C_A0159_v1.md#transporting-inner-inverses-between-coefficient-fields) | Restriction of scalars by simultaneous diagonalization. |
| dependency | [Rank invariance](Yin_C_A0007_v10.md#scalars-in-the-division-closure-on-a-sofic-group) | Ranks in the conjugate pencil blocks. |
| review | [Algebraic rank attainment](../audits/reviews/Yin_R_A0173_v1.md#algebraic-rank-attainment) | Independent review of the complete statement and proof. |

## Current assessment

[Selected decision](#decision-algebraic-rank-attainment)

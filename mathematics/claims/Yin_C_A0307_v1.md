---
author: Yin
---

# A coefficient-independent gap near a fixed order-twenty-four marking

## Statement

Let \(H=\langle s,t\rangle\) be a torsion-free marked group with regular scalar group-ring injectivity and a character to \(C_{24}\) taking \(s,t\) to \(3,4\).
There is an \(\epsilon>0\), depending on the marked group, such that for every four-site matrix \(K=B+At-s(D+Ct)\) with noninteger regular nullity,
\[
                          \dim_H\ker K\le 1/2-\epsilon .
\]
The coefficients are arbitrary complex two-square matrices, with no restrictions on their norms or condition numbers.

In fact there is a finite marked word radius \(R\) such that the same gap works in every torsion-free, scalar-injective two-generator group with the same normalized character degrees and the same relations through length \(R\) as \(H\).
This assertion gives no computed values of \(R,\epsilon\) and does not assume that scalar injectivity passes to arbitrary limits of marked groups.
The [order-24 exclusion](Yin_C_A0303_v1.md#statement) is used at the given group.

## Balancing the cyclic plane

For a noninteger input the [four-column linearization and reductions](Yin_C_A0184_v1.md#the-four-group-elements-and-the-trace-bound) give regular pencils \(P(z)=Az+B,\ Q(z)=Cz+D\).
In coordinates ordered as input and output let \(V(z)\subset\mathbb C^2\oplus\mathbb C^2\) be the plane spanned generically by the columns of \((Q(z),P(z))^{\mathsf T}\), meaning the vertical stack of the two blocks.
Its cyclic range \(V(t)\) is the graph of \(M(t)=P(t)Q(t)^{-1}\) as an affiliated module.
Regular nullity is the trace dimension of its intersection with the graph of \(sI_2\).
It is at most \(1/2\) by the four-position window, since all conjugates of \(t\) have degree zero modulo four and \(s\) has degree three.
The matrix \(M(z)\) has no constant point correspondence, as that would give integer nullity by the [constant-line test](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer).

For a numerical positive matrix \(T\) on \(\mathbb C^2\) of trace one, let \(P_T\) be the orthogonal image projection of \((T\oplus T)V(t)\).
If \(T\) is invertible its image has trace two.
If \(T=e\) is a rank-one projection, the null intersection with \(\ker e\oplus\ker e\) follows from the absence of constant point correspondence: over \(\mathbb C(z)\) such an intersection would give a fixed input line mapped into itself.
Cyclic spectral evaluation preserves this rank calculation.
Thus at \(e\) the image projection is exactly \(e\oplus e\).
The sum of the two diagonal block matrices of group traces of \(P_T\), divided by two, is a positive matrix of trace one and equals \(e\) on the boundary of the ball of choices of \(T\).
It varies continuously: the operators \((T\oplus T)P_I\), where \(P_I\) is the original plane projection, vary in norm with constant image trace; spectral cutoff on the limiting range gives convergence of image projections in trace \(L^2\) by the [constant-metric projection argument](Yin_C_A0277_v4.md#a-constant-change-of-metric-balances-the-first-projection).
The no-retraction theorem on the three-ball therefore gives an invertible \(T\) making the sum of the two block trace matrices exactly \(I_2\).
The constant \(T\oplus T\) preserves the graph of \(sI_2\), so it preserves the intersection dimension.
The balanced plane still has a pair of generating columns of degree at most one.

## Compactness of degree-one plane presentations

Suppose the local uniform assertion fails.
For each \(n\) take a group agreeing with \(H\) on relations through length \(n\) and an input of noninteger nullity exceeding \(1/2-1/n\), and balance its plane as above.
For its two polynomial columns take an orthonormal basis \(p_n,q_n\) of their two-dimensional complex span in the eight-dimensional coefficient space of four-component linear polynomials.
After a subsequence these columns converge to two orthonormal polynomial vectors \(p,q\).
In addition divide the six polynomial coefficients of the exterior vector \(p_n\wedge q_n\) (each entry has degree at most two) by the joint Euclidean norm of all their coefficients.
Pass to a subsequence with a nonzero limiting exterior polynomial.
Its values are decomposable by the polynomial Plücker equations and determine a rational two-plane \(V(z)\) off finitely many points: where a chosen nonzero exterior coordinate does not vanish one can express a basis by ratios of exterior coordinates.
The orthogonal plane projections converge pointwise almost everywhere on the circle and hence in Haar \(L^2\), so the limit is balanced.

There are two possibilities for this limit.
If \(p,q\) are independent over \(\mathbb C(z)\), they present \(V(z)\) by two linear columns.
If they are dependent over that field, they are polynomial scalar multiples of one primitive polynomial column, by dividing out the gcd of a column's entries.
That primitive column must be constant, since otherwise both scalar multiples would be constant and \(p,q\) would be dependent over \(\mathbb C\).
The limit plane contains this nonzero constant vector: at a generic point it contains the limit \(p(z)\), as follows by convergence of both the projections and the polynomial vectors.

The limiting plane at \(H\) has graph intersection of dimension at least \(1/2\).
For detail let \(S\) be the graph projection of \(sI_2\), with the corresponding projection at each marked group.
Its entries are constant multiples of \(1,s,s^{-1}\).
The unnormalized trace of the intersection is the decreasing limit of \(\operatorname{Tr}((SP_V S)^k)\), by positive contraction spectral calculus.
At fixed \(k\) these moments converge to those of the limiting plane.
Indeed cyclic Haar measure is the same in all the groups because \(t\) has infinite order.
Replace the varying cyclic projection by the limiting cyclic matrix function with \(L^2\) error tending to zero; then approximate that fixed function by uniformly bounded matrix Laurent polynomials using Fejér convolution.
Telescoping products bounds both moment errors by constants times the \(L^2\) errors.
For fixed Laurent polynomials the regular traces eventually agree by equality of relations on increasing marked balls.
Taking the infimum over \(k\) proves the claim.

## Ruling out the limiting intersection

If the projection of \(V(z)\) onto one coordinate pair is injective as a map of two-dimensional rational spaces, \(V\) is a graph over that pair.
Exchange input and output if necessary, using \(s^{-1}\) as the graph shift.
The four-window bound on this graph gives dimension at most \(1/2\), and equality forces the rational transfer to be invertible by its fourth-power identity. [Transfer equality](Yin_C_A0183_v1.md#transfer-matrices-and-equality)
If \(V\) has a constant vector, its two components are nonzero by invertibility, and give a constant point correspondence.
This would yield integer dimension in \(H\).
Otherwise its linear presentation from the preceding section realizes this \(1/2\) as the nullity of a four-site matrix: the graph parametrization by the two stacked columns identifies the polynomial kernel with the intersection, since projection onto the input is a cyclic rational unit.
This contradicts the [four-site exclusion](Yin_C_A0303_v1.md#statement), also with the marking \((s^{-1},t)\) when input and output were exchanged.

If neither of the two coordinate projections is injective, both have rank one and the plane is \(X(z)\oplus Y(z)\) for two rational lines on the respective coordinates.
If one line is constant, say with orthogonal projection \(e\), balance makes the average projection of the other line \(I-e\).
A field of rank-one projections averaging to this projection is equal to it almost everywhere, by positivity on its orthogonal complement.
The two constant complementary lines have zero graph intersection.
This also handles every split plane containing a nonzero constant vector.

In the remaining split case there is a linear presentation and both lines are nonconstant.
In a common constant coordinate basis each is the graph of a nonconstant fractional linear function: project a nonzero one of the two linear columns onto the relevant coordinate pair and take the ratio of its components.
The intersection dimension is then the nullity of \(f(t)-h(s^{-1}ts)\) for these two functions \(f,h\), by conjugating the output line by \(s^{-1}\).
Clear a Laurent denominator on the left from the first cyclic and on the right from the second.
Scalar injectivity on \(H\) makes the nullity zero or one.
If it is one, the two rational functions of the actual translations are equal.
Each is a nonconstant fractional linear function invertible as a change of variable, so the common affiliated function generates the cyclic von Neumann algebra of each translation.
Equality of the cyclic algebras implies equality of their cyclic subgroups, by Fourier support.
Hence \(s^{-1}ts=t^{\pm1}\).
This is a single marked relation, and it holds also in every sufficiently late approximating group.
Such a group is cyclic-by-cyclic and amenable; scalar injectivity then gives integer matrix ranks by [Ore localization](Yin_C_A0211_v1.md#right-fractions-for-commensurable-amenable-subgroups), contradicting the noninteger inputs used in the sequence.
All possible limiting planes are excluded, proving the uniform assertion.

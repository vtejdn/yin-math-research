---
author: Yin
---

# A positive integral lamplighter operator with a nonrational kernel projection

## Statement

Let \(\Gamma=C_2\wr\mathbb Z\) be the ordinary lamplighter group, let \(U=L^0(\mathcal N(\Gamma))\) be its affiliated ring for the group trace, and let \(D\) be the division closure of \(\mathbb C\Gamma\) in \(U\).
There is a positive scalar \(a\in\mathbb Z\Gamma\) whose kernel projection \(p\) lies outside \(D\).
Consequently neither the division closure nor the rational closure of \(\mathbb C\Gamma\) in \(U\) is von Neumann regular.
This answers [Linnell's Problem 4.5](https://arxiv.org/abs/math/0311071v2) for its specified group with torsion.

For the construction, Fourier transform the lamps and write \(s_i=1\) or \(-1\) according as the bit at height \(i\) is \(1\) or \(0\).
Let \(s\) be multiplication by \(s_i\), let \(e\) be the indicator of the transition from \(0\) at \(i-1\) to \(1\) at \(i\), put \(q=1-e\), and set \((\nabla f)_i=f_{i+1}-f_i\).
Then one can take
\[
                    h=e+q\nabla^*s\nabla q,\qquad a=(16h)^2.
\]
The same kernel projection is outside the intrinsic division closure of the coordinate indicators and the shift for every shift-invariant probability measure of full support on the binary full shift.
In particular, if \(K\) is a nontrivial torsion-free group with a projection \(b\in D_K\) of trace strictly between zero and one, the shifted copies of \(b\) in \(K\wr\mathbb Z\) give this example in the algebra they generate with the shift.
Membership of the projection in the larger division closure of \(\mathbb C[K\wr\mathbb Z]\) remains open in this construction.

## Argument

### Periodic specialization of a proposed rational projection

The [Fourier representation of the lamps](Yin_C_A0138_v1.md#finite-height-relations-at-a-periodic-configuration) identifies \(\mathbb C\Gamma\) with the algebra of finite sums of shifts with locally constant coefficients on the binary full shift.
In this representation the group trace uses the Bernoulli measure with equal weights.
The operator \(s\) is the zeroth lamp, and \(e\) is a product of two commuting factors of the form \((1\pm s_j)/2\) at adjacent heights.
Thus \(16h\in\mathbb Z\Gamma\), \(h=h^*\), and \(a\) is positive with kernel projection \(p_{\ker h}\).

For a periodic bit sequence of period \(d\), group \(d\) consecutive heights and represent translation through one period by the variable \(z\).
Each finite sum of shifts with cylinder coefficients becomes a \(d\)-by-\(d\) matrix over \(\mathbb C[z,z^{-1}]\).
Use the involution given by complex conjugation and \(z^*=z^{-1}\) on the field \(F=\mathbb C(z)\).
Periodic evaluation extends to a unital \(*\)-homomorphism from the division closure into \(M_d(F)\). [Periodic evaluation](Yin_C_A0138_v1.md#evaluation-of-rational-expressions)
Ara and Claramunt obtain the periodic quotient of the \(*\)-regular closure in [Theorem 4.11](https://arxiv.org/abs/2005.12374).

The same evaluation of rational expressions works for any shift-invariant probability measure giving positive mass to each nonempty cylinder.
Indeed, a violation of \(\ker K'\subseteq\ker B'\) over \(F\) for evaluated cylinder matrices has a Laurent-polynomial vector witness after clearing denominators.
Here the prime denotes evaluation at the periodic sequence.
Unfolding this vector gives a finitely supported vector on the integer heights, and its two outputs depend on only finitely many bits.
The same vector, taken on the corresponding cylinder and extended by zero elsewhere, violates \(\ker K\subseteq\ker B\) in the regular crossed-product representation.
This implication preserves injectivity of each square polynomial pivot.
It also preserves vanishing of a realization \(\alpha L^{-1}\beta\), by applying it to \(K=[L,-\beta]\) and \(B=[\alpha,0]\), as in the cited periodic evaluation argument.
All periodic evaluations below use \(F\), so translation through the period has infinite order.

Suppose that \(p=p_{\ker h}\) belongs to the division closure in question.
Write \(p=\alpha L^{-1}\beta\) for a square matrix \(L\) over the cylinder algebra with finite shifts, invertible in the affiliated matrix algebra, a row \(\alpha\) and a column \(\beta\) over the same algebra. [Rational realizations](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations)
Since \(p=p^*=p^2\), \(hp=0\) and \(h^2+p\) is an affiliated unit, these relations and the inverse of \(h^2+p\) survive periodic evaluation.
Consequently \(p'\) is the orthogonal projection onto \(\ker h'\) over \(F\).
In fact, for \(h'v=0\), the vector \((1-p')v\) is killed by \((h')^2+p'\), so it vanishes.
Orthogonality uses the usual Hermitian form over \(F\), which is positive definite in the algebraic sense since a sum of squared absolute values vanishing identically on the unit circle has all its summands zero.

### Kernel on two consecutive runs

For \(n,m\ge1\), repeat the word \(1^n0^m\) and take the period to start at height zero.
The unique marked vertex in this period is zero.
For a kernel vector \(v\) of \(h'\), the marked equation is \(v_0=0\), and the next marked endpoint likewise has \(v_{n+m}=z^{\pm1}v_0=0\).
At every unmarked vertex the equation equates the currents in the two adjacent edges.
Hence for one \(c\in F\) the equations are
\[
             s_i(v_{i+1}-v_i)=c\quad (0\le i<n+m),\qquad
             0=v_{n+m}-v_0=(n-m)c.
\]
Thus the kernel vanishes for \(n\ne m\).
For \(n=m\), taking \(c=1\) gives a generating vector with real entries independent of \(z\) and entry \(1\) at height one.
Write \(\delta_1\) for the height-one coordinate vector in the period.
The entry \(\delta_1^*p'\delta_1\) is zero for \(n\ne m\), and for \(n=m\) it is the reciprocal of the squared norm of that generator.

### A finite sum of products for every rational numerator

Write \(L_{nm},\alpha_{nm},\beta_{nm}\) for the evaluated matrices on this word.
The scalar \(-\det L_{nm}\,\delta_1^*p'\delta_1\) is the determinant of the bordered matrix
\[
          H_{nm}=
          \begin{pmatrix}L_{nm}&\beta_{nm}\delta_1\\
                          \delta_1^*\alpha_{nm}&0\end{pmatrix}.
\]
Each \(L_{nm}\) is invertible over \(F\).
The infinite array \((\det H_{nm})_{n,m\ge N}\) therefore has nonzero entries exactly on its diagonal for every \(N\ge1\).
In particular its finite submatrices have unbounded rank over \(F\).

We show instead that the determinants of every such bordered family have bounded array rank.
All shifts occurring in the finitely many coefficients have bounded length, and all cylinder functions used to form these coefficients read bits in a fixed finite neighborhood.
Order the rows and columns of \(L_{nm}\) by height, keeping the matrix coordinates together at each height.
Place the extra row and column with the \(1\)-run, and place the cut carrying \(z\) between the last \(0\) and the first \(1\).
For all sufficiently large \(n,m\) the diagonal block on the \(1\)-run, including the extra row and column, depends only on \(n\), and the block on the \(0\)-run depends only on \(m\).
Indeed each coefficient reads only the neighboring bits, which in both runs are fixed up to the distance from their two ends.
The border has nonzero coefficients only within bounded distance of height one, and each shift crossing the period cut contributes its fixed \(z\) or \(z^{-1}\).
The two off-diagonal blocks have entries only among the bounded sets of coordinates near the two ends of each run and the extra coordinate.
Label these coordinates by the end, the distance from it and the matrix coordinate.
Once both runs exceed twice the shift and cylinder radii combined, all the off-diagonal coefficients in these labels are independent of \(n,m\).

Thus write \(H_{nm}=\operatorname{diag}(A_n,B_m)+E_{nm}\), where \(E_{nm}\) is supported on the labelled coordinates just described.
Order these coordinates first in each block, using the same row and column permutation so the determinant is unchanged.
Expand the determinant of the sum by minors of \(E_{nm}\).
There are only finitely many potentially nonzero choices of its row and column sets \(I,J\), independent of \(n,m\), and each chosen minor is constant over \(F\).
The complementary minor of the block diagonal matrix vanishes unless equal numbers of rows and columns were removed from each block.
When those numbers agree it equals a minor of \(A_n\) times a minor of \(B_m\).
The cofactor sign is constant for each such choice, since the offset \(\dim A_n\) of the second block appears in the sum of the selected indices an even number of times.
It follows that \(\det H_{nm}=\sum_{j=1}^k f_j(n)g_j(m)\) over \(F\) for one finite \(k\) and all sufficiently large \(n,m\).
Each finite submatrix of this array has rank at most \(k\).
The contradiction proves \(p\notin D\), including the assertion for arbitrary full-support invariant measures.

### Regularity and the torsion-free lamp construction

If \(h\) had an inner inverse \(y\in D\), the idempotent \(j=1-yh\) would have image \(\ker h\) on the affiliated right module.
The two positive operators \(jj^*\) and \((1-j)^*(1-j)\) have complementary support projections \(p\) and \(1-p\).
Their sum is an affiliated unit and therefore has inverse in \(D\).
Multiplying \(jj^*\) by that inverse gives \(p\in D\), a contradiction.
Moreover \(D\) is closed under inverses of square matrices over \(D\) which are invertible over \(U\), by [successive elimination of the leading Gram blocks](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations).
Hence it is the rational closure in Linnell's question, also by his Proposition 4.3 since \(\Gamma\) is amenable. [Linnell, Proposition 4.3 and Problems 4.4–4.5](../audits/literature/Lin06/Yin_U001.md#regularity-of-the-rational-closure)
Ara and Goodearl proved unit-regularity for the division closure of the proper subalgebra generated by a partial shift. [Theorem 6.13](https://arxiv.org/abs/1410.8838)

For \(W=K\wr\mathbb Z\) as in the statement, the projections obtained from \(b\) at the distinct heights commute, and every prescribed cylinder has positive trace by independence of the tensor factors.
Together with the shift they give the regular Bernoulli crossed-product representation with weights \(\tau(b),1-\tau(b)\). [Independent lamp projections](Yin_C_A0164_v1.md#independent-projections-at-the-lamps)
This representation and its affiliated inclusion preserve kernel projections and invertibility.
The formula for \(h\) now uses rational coefficients in \(D_W\), and its kernel projection is outside the division closure generated by these binary observations and the shift.
Other coefficients of \(\mathbb CW\) can enter a rational realization in \(D_W\).
Indeed, there is no unital ring retraction from \(D_W\) to the intrinsic binary division closure.
Evaluating the latter at the constant bit sequence gives a unital homomorphism to \(F\).
For a nonidentity lamp element \(g\), the commutator of \(g\) and the shift is a nonidentity element \(u\) of infinite order.
The element \(1-u\) is an affiliated unit in \(D_W\), since the action of \(u\) on each coset of its cyclic subgroup is a bilateral shift.
Any unital map from \(D_W\) into a commutative field would kill \(1-u\).
The nonregularity proved here therefore determines the intrinsic lamp-ring obstruction and leaves the [torsion-free question](../tasks/Yin_T_A0003_v3.md#contract) open.

## Assessment history

### Decision two-run-kernel

| Field | Value |
| --- | --- |
| date | 2026-11-26T04:30 |
| status | proved |
| reason | The dimensions on two consecutive runs make a diagonal array of projection numerators, while every rational realization would give an array of bounded rank. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Positive integral scalar on the binary lamplighter, nonregularity of its complex rational closure, full-support laws and the intrinsic torsion-free comparison. |
| argument | [Argument](#argument) | Periodic specialization, conservation of the signed current, determinant expansion over two interfaces, inner inverse and subgroup obstructions. |
| dependency | [Periodic specialization](Yin_C_A0138_v1.md#evaluation-of-rational-expressions) | Evaluating a legal expression while retaining translation through a whole period. |
| dependency | [Rational realizations](Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations) | A single full group-ring pivot for a putative projection. |
| dependency | [Independent observations](Yin_C_A0164_v1.md#independent-projections-at-the-lamps) | The Bernoulli crossed product inside the group generated by torsion-free lamps and the shift. |
| dependency | [Linnell's question](../audits/literature/Lin06/Yin_U001.md#lin06-u001) | The rational closure and group in Problem 4.5. |
| review | [Two-run kernel](../audits/reviews/Yin_R_A0176_v1.md#two-run-kernel) | Independent review of the complete statement and argument. |

## Current assessment

[Selected decision](#decision-two-run-kernel)

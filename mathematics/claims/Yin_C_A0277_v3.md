---
author: Yin
---

# One balanced row excludes half nullity for every choice of the other moduli

## Statement

Let the first row of a three-square group-ring matrix be \((1,1,1)\), the second \((1,\lambda u,\mu v)\) with \(|\lambda|=|\mu|=1\), and the third a row of arbitrary nonzero scalar multiples of \(1,w,z\).
Suppose \(A=\langle u,v\rangle\) and \(B=\langle w,z\rangle\) are free on their indicated pairs and \(A\cap B=\{1\}\).
With the unnormalized coordinate trace its regular nullity satisfies
\[
                             \delta\le\tfrac12-\frac{3}{2^{21}} .
\]
Only one of the two rows after the first is required to have unit moduli.
The estimate is uniform over the other three positive moduli and all phases.

Use \(P,Q\) for the two row-kernel projections on the two-dimensional constant space \(W=\mathbf1^\perp\) tensored with the regular group space, as in the [two-row calculation](Yin_C_A0277_v1.md#the-scalar-coefficient-of-each-row-projection).
Write \(\overline Q\) for the identity Fourier coefficient of \(Q\), a positive matrix of trace one on \(W\), and \(s=\|\overline Q-I_W/2\|_{\mathrm{op}}\).
There is a second estimate
\[
                             \tfrac12-\delta\ge 3s^2/8 .
\]
The scalar coefficient \(\overline Q\) is \(I_W/2\) precisely when the third row has three equal moduli.

## The commutator on the six short elements

The full trace \(\operatorname{Tr}(PQ)\) is \(1/2\) by the [one-balanced-row trace identity](Yin_C_A0277_v1.md#the-scalar-coefficient-of-each-row-projection).
The commutator square calculation gives \(\|[P,Q]\|_{2,\operatorname{Tr}}^2\le2(1/2-\delta)\).
For \(a\in A\setminus\{1\}\), the coefficient of this commutator at \(a\) is \([P_a,\overline Q]\), since the \(AB\) and \(BA\) factorizations there each use the identity of \(B\).
At the six distance-two elements the [tree formula](Yin_C_A0277_v2.md#the-row-projection-on-the-three-regular-tree) gives \(P_a\) as a scalar of modulus \(1/4\) times \(f_i f_j^*\) for every ordered \(i\ne j\), where \(f_i=(e_i-\mathbf1/3)/\|e_i-\mathbf1/3\|\).

Put \(D=\overline Q-I_W/2\) and \(v_i=f_i^*D f_i\).
Since \(\sum f_i f_i^*=3I_W/2\) and \(\operatorname{tr}D=0\), one has \(\sum v_i=0\).
Expanding the Hilbert-Schmidt squares gives
\[
 \sum_{i\ne j}\|[f_i f_j^*,D]\|_{\rm HS}^2
      =6\operatorname{tr}(D^2)-2\sum_{i\ne j}v_i v_j
      =6\operatorname{tr}(D^2)+2\sum_i v_i^2 .
\]
Thus Parseval on the six coefficients yields
\(\|[P,Q]\|_{2,\operatorname{Tr}}^2\ge (3/8)\operatorname{tr}(D^2)=3s^2/4\).
Here \(D\) is a traceless selfadjoint matrix of size two.
This proves the second estimate.

## The least energy for prescribed values on the three root edges

Denote the third-row moduli by \(r_i>0\), scaled without changing its kernel so that \(\sum_i r_i^2=3\).
A free-group character of \(B\) and a common scalar phase remove its three coefficient phases for computing its trace matrix.
Use the [three-edge covering tree](Yin_C_A0277_v2.md#the-row-projection-on-the-three-regular-tree), now for \(B\).
The flow equations are zero sum at every left vertex and zero \(r_i\)-weighted sum over the incident edge colors at every right vertex.

Suppose \(\overline Q\) is invertible on \(W\).
Evaluation of a square-summable flow in the two-row kernel at the three edges of the identity left vertex gives an operator \(E\) into \(W\) with \(EE^*=\overline Q\), by the compression of the orthogonal kernel projection to these edge vectors.
Thus \(E\) is onto, and the least squared norm of a flow with specified root values \(x\in W\) is \(x^*\overline Q^{-1}x\), achieved by \(E^*\overline Q^{-1}x\).
Deleting the root splits the extension problem into three independent branches.
Let \(c_i\) be the least squared norm on the branch through an edge of color \(i\) pointing next to a right vertex, including the edge itself, for edge value one.
All are finite since \(E\) is onto; rescaling a feasible root value supplies an extension of any single root edge.
The minimum exists by orthogonal projection onto a closed affine subspace.
Similarly write \(d_i\) for the branch cost with next vertex on the left.
The colored tree has the same branching by colors at every vertex on the same side.
In particular the branches with next vertex on the left can be filled using the already feasible forward branches at their two child edges, so \(d_i\) is finite too.
Independence gives
\[
             x^*\overline Q^{-1}x=\sum_i c_i |x_i|^2\qquad (x\in W).
\]

Across the first vertex of each branch, optimize the two independent child values subject to their one linear equation.
For instance at a right vertex the two values \(y_j\) have \(\sum_{j\ne i}r_jy_j=-r_i\) and cost \(\sum_{j\ne i}d_j|y_j|^2\).
Weighted Cauchy-Schwarz with equality, and then the corresponding unweighted computation at a left vertex, yield
\[
            c_i=1+\frac{r_i^2}{\sum_{j\ne i}r_j^2/d_j},
              \qquad d_i=1+\frac{1}{\sum_{j\ne i}1/c_j}.
\]
In particular if \(\overline Q=I_W/2\), testing \(x=e_i-e_j\) gives \(c_i+c_j=4\) for every pair, hence all \(c_i=d_i=2\).
The first branch equation now gives \(2r_i^2=\sum_{j\ne i}r_j^2\), so all the moduli are equal.
Conversely equal moduli give the scalar matrix by permutation symmetry of the balanced free row.

## A uniform estimate for all third-row moduli

For \(s\ge1/512\) the established bound \(3s^2/8\) is at least \(3/2^{21}\).
Suppose \(s<1/512\), so \(\overline Q\) is invertible.
For \(x=e_i-e_j\), the eigenvalue bounds on \(\overline Q^{-1}\) give
\[
       (1/2+s)^{-1}\le (c_i+c_j)/2\le(1/2-s)^{-1}.
\]
The pair averages differ from two by at most \(4s/(1-2s)\); adding two such averages and subtracting the third gives \(|c_i-2|\le13s\).
The formula for \(d_i\) puts it between \(2-7s\) and \(2+7s\).
Writing \(t_i=r_i^2\) and using \(\sum t_i=3\), the formula for \(c_i\) gives
\[
             \frac{1-13s}{2+7s}\le\frac{t_i}{3-t_i}
                          \le\frac{1+13s}{2-7s}.
\]
It follows that \(|t_i-1|\le 33s/(3-6s)\le12s\), and thus \(|r_i-1|\le7s\).

Let \(Q_0\) be the projection for the row with the same phases and all moduli one.
On \(W\) the difference of the weighted and unweighted row operators has norm at most \(7\sqrt3\,s<13s\) for \(s>0\), and is zero for \(s=0\).
The adjoint of the unweighted row is bounded below by \(1/\sqrt3\), by the [free-row spectral gap](Yin_C_A0281_v1.md#stability-under-changes-in-the-four-moduli).
The adjoint of the weighted row is therefore bounded below by \(1/\sqrt3-13s>1/2\).
Comparing the two kernels as in that calculation gives \(\|Q-Q_0\|\le26s\): the two cross-projection norms are bounded by the row difference times the inverse of the respective lower modulus, and their maximum is the norm of the projection difference.

For any selfadjoint \(X\) on the two-coordinate space, \([P,X]\) consists of its two off-diagonal blocks relative to \(P\), with signs.
Thus \(\|[P,X]\|_{2,\operatorname{Tr}}\le\|X\|_{2,\operatorname{Tr}}\le\sqrt2\,\|X\|\).
The [short-product discrepancy](Yin_C_A0277_v2.md#a-discrepancy-on-products-of-two-short-elements) for the balanced pair gives \(\|[P,Q_0]\|_{2,\operatorname{Tr}}\ge\sqrt3/16\).
Consequently
\[
          \|[P,Q]\|_{2,\operatorname{Tr}}
                  \ge \sqrt3/16-26\sqrt2/512>1/32.
\]
In this case \(1/2-\delta>1/2048\), also giving the claimed uniform bound.

## Assessment history

### Decision one-balanced-row-and-all-remaining-moduli

| Field | Value |
| --- | --- |
| date | 2026-11-26T14:38 |
| status | proved |
| reason | Independent full review confirmed the tree energy comparison and the uniform gap for all moduli of the remaining row. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The two gap bounds and the equality characterization for the scalar trace matrix. |
| argument | [The commutator on the six short elements](#the-commutator-on-the-six-short-elements) | The six rank-one numerical matrices and the trace discrepancy. |
| argument | [The least energy for prescribed values on the three root edges](#the-least-energy-for-prescribed-values-on-the-three-root-edges) | Root evaluations and the two minimum-energy recursions. |
| argument | [A uniform estimate for all third-row moduli](#a-uniform-estimate-for-all-third-row-moduli) | Control of the three moduli, the two kernel projections and the quantitative gap. |
| review | [One balanced row and all remaining moduli](../audits/reviews/Yin_R_A0210_v1.md#one-balanced-row-and-all-remaining-moduli) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-one-balanced-row-and-all-remaining-moduli)

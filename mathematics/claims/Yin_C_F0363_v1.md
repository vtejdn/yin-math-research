---
author: Yin
---

# Nine cubic resolvent kernels and the sixth difference of a three-dimensional determinant

<a id="statement"></a>
## Rational independence and a simultaneous small-ball estimate

For the [finite-variance Wigner Task](../tasks/Yin_T_F0012_v3.md#contract) take independent **real symmetric** original inputs.
Use a prescribed principal minor of size \(n=N-o(N)\) at original scaling and write its two inputs as \(X,Y\).
Let \(P=1+X^2Y+YX,\ R_w=(P-w)^{-1}\) at each regular parameter, and define
\[
 A=(1,XY,Y),\qquad B=(1,X,Y),\qquad
 K_{ij}(w)=\operatorname{sym}(A_iR_wB_j)-\mathbf1_{\{i=j=2\}}I,\qquad 1\le i,j\le3 .
\]
Here transpose reverses words and fixes complex scalars, and \(\operatorname{sym}H=(H+H^{\mathsf T})/2\).
In the semicircular free field, the nine functions at each of any finite number of distinct complex parameters are jointly linearly independent modulo scalars over \(\mathbb C\).

Fix \(D\) and take at most \(D\) prescribed nodes separated by a fixed positive distance in a compact subset of the open upper half-plane.
Split the old physical sites into six deterministic panels whose sizes differ by at most one.
Consider \(s\) of these nodes and, at each, any past-measurable symmetric kernels \(\widetilde K_{ij}\) differing from \(K_{ij}\) by rank \(O(k)\) per kernel, where \(k=o(n)\) and the implicit rank bound is deterministic.
Let \(g\) be an independent raw column of iid copies of one fixed nonconstant real strict upper entry law.
At every regular node under test form
\[
 f_w(g)=c_w\det[(g^{\mathsf T}\widetilde K_{ij}(w)g)_{i,j=1}^3]+b_w(g),
\]
where \(0<|c_w|\), the polynomial \(b_w\) of degree at most five and the choice of ranks and kernels are fixed before \(g\).
There are old-minor exceptional events of probability \(O(e^{-cn})\) for the prescribed tuple such that, conditionally on the past outside them, for each fixed \(C_0<\infty\),
\[
 \Pr_g\{ |f_w(g)|\le C_0|c_w|\text{ at all }s\text{ nodes}\}
 \ \le C_D n^{-s/128}+C_D e^{-c_D n}.
 \tag{1}
\]
The conditional estimate concerns histories regular at the tested nodes and uniform admissible rank changes.
It applies to a transition defined to be bad only at regular incoming nodes, with the original minor regular as well.
At the \(3\)-direction restoration for the pencil
\[
 \begin{pmatrix}(1-w)I+YX&X\\XY&-I\end{pmatrix}
\]
these functions correspond to the ordering \((v,0),(0,v),(Yv,0)\) on each side, up to the permutations arising in the fresh row and column maps.
An \(N^{-18}\) ratio threshold satisfies the hypothesis in (1) whenever the product of the two normal volumes is at least \(cN^{-12}\), since the three raw quadratic forms supply the further factor \(N^{-3}\).

<a id="argument"></a>
## Separating the three relations left by scalar inputs

In commuting variables the nine numerators before subtracting the identity are the entries of
\[
 \begin{pmatrix}1&x&y\\xy&x^2y&xy^2\\ y&xy&y^2\end{pmatrix},
 \qquad F=1+(x^2+x)y .
\]
Clear the distinct denominators \(F-w\) of a putative relation modulo scalars and reduce modulo each \(F-w\).
All other factors become nonzero constants, so the corresponding numerator is divisible by \(F-w\).
By degree it is a constant multiple of \(F-w\).
The seven distinct numerator monomials, the two repetitions and this one multiple show that the contribution at this node, modulo scalars, is a linear combination of
\[
 D_1=\operatorname{sym}(R_wY-YR_w),\quad
 D_2=\operatorname{sym}(XYR_w-YR_wX),\quad
 D_3=\operatorname{sym}(XYR_wX+XYR_w+(1-w)R_w-I).
\]
The relation \((P-w)R_w=I\) gives \(D_3=\operatorname{sym}([XYR_w,X]+[X,Y]R_w)\).

Take \(X=\operatorname{diag}(a,b)\) and \(Y=\operatorname{diag}(c,d)+t(E_{12}+E_{21})\).
At \(t=0\) the inverse has diagonal entries \(r_1=(1-w+(a^2+a)c)^{-1}\) and \(r_2=(1-w+(b^2+b)d)^{-1}\).
Differentiation gives \(R'_{12}=-(a^2+b)r_1r_2,\ R'_{21}=-(b^2+a)r_1r_2\).
The \(12\) entries of \(D'_1,D'_2,D'_3\), after division by \((a-b)r_1r_2/2\), are respectively
\[
 (c-d)(a+b-1),\qquad (a-b)(c+d),\qquad
 a(b+1)c-b(a+1)d-(a-b)(1-w).
 \tag{2}
\]
For instance the two unsymmetrized terms for the last derivative sum to
\((a-b)\{ac(a^2+b)r_1r_2-bd(b^2+a)r_1r_2+(1-a)r_2+(b-1)r_1\}\) before division by two.
These identities hold as rational functions since regular real specializations are dense.
For generic \(a,b,d\), take the residue in \(c\) at \((w-1)/(a^2+a)\).
Every other node is regular there.
After removing the common nonzero factors, the coefficient of \(d\) in the residue identity for the three coefficients \(\alpha,\beta,\gamma\) of this node is
\[
 -\alpha(a+b-1)+\beta(a-b)-\gamma b(a+1)=0.
\]
The \(ab\) and constant terms and then the \(a\) coefficient give \(\gamma=\alpha=\beta=0\).
Repeating this at every node proves the free-field assertion because any such relation would hold at all jointly regular symmetric matrix specializations.
Inclusion of the conjugate nodes gives real-linear independence of all entrywise real and imaginary directions modulo scalars on the stated upper-half-plane tuples.

<a id="corners"></a>
## Physical corners of the original minor

For each ordered pair of distinct panels apply the [free distinct-site corner and finite approximation argument](Yin_C_F0351_v9.md#kernels) to the joint family of real and imaginary parts just separated.
In the free model the equal-trace coordinate projections are free from \(X,Y\).
A zero corner for a symmetric real combination forces all its distinct corners to vanish by permutation of the free projections, hence commutation with a nontrivial free projection and scalarity.
Compactness of the separated node and unit-coefficient sets and continuity of the affiliated inverses in measure supply a uniform positive fraction of singular values above a positive threshold.
The rational expressions use only \(P-w\), its transpose and fixed words of degree at most two as outside factors.
The [finite physical-corner comparison](Yin_C_F0351_v6.md#physical-corners) clips the two inputs, regularizes each inverse, and uses the free absence of a zero singular atom and row-rank concentration to return to the true inverses up to small rank.
Replacing each outside word by the clipped word costs at most the sum of its input rank discrepancies by telescoping the product.
It gives bounded corner approximants with total error rank arbitrarily small compared with the good fraction outside an exponentially small exception on the old minor, for **each prescribed tuple**, uniformly in that tuple.
The \(O(k)\) further rank errors per true kernel fit within the same slack for large \(n\).
These statements concern the off-diagonal physical corners, so the scalar in \(K_{22}\) drops out.

We use the following consequence of the [projected output spread and disjoint bases](Yin_C_F0351_v6.md#border-tests).
For two as yet unexposed panels \(a,b\) let \(u_a,u_b\) be independent vectors of iid differences of two raw coordinates, and let \(H_{ab}(w)\) have entries \(u_a^{\mathsf T}(\widetilde K_{ij})_{ab}u_b\).
Consider one real part of a complex linear form in the nine entries for each of \(m\) nodes.
Suppose the coefficient array at each node has Euclidean norm at least one, allowing unbounded arrays fixed before \(u_a\).
In the coefficient vector on panel \(b\) one may add an element of a fixed real subspace of bounded dimension known before \(u_a\), with coefficients depending on \(u_a\).
Project off that subspace in the spread estimate on panel \(a\), together with every allowed deletion on \(b\).
For any real unit combination of the \(m\) tests the stacked real coefficient array has norm at least one, because the nine real and imaginary pairs are indexed separately at each node.
Indeed a coefficient \(z\) in a real-part test contributes the pair \((\Re z,-\Im z)\).
The uniform unit-array estimate of the cited argument applies after dividing by the array norm and scaling back.
Except with exponentially small probability in \(u_a\), the matrix of real coefficient vectors on the last panel retains least singular value at least \(c\sqrt n\) after every sufficiently small fixed fraction of coordinates is deleted.
Projection removes the arbitrary added vectors even when their coefficients are large.
Disjoint bases and the independent \(u_b\) now bound the probability of a fixed-radius box in these \(m\) tests by \(C n^{-m/2}+Ce^{-cn}\), uniformly in the past and in any centers fixed before \(u_b\).
Testing complex moduli implies smallness of these real parts.

<a id="polarization"></a>
## Three successive pairs of independent panel differences

Write \(\mathcal D(H,J,L)=[tuv]\det(tH+uJ+vL)\) and let \(E_{jj}\) be the diagonal matrix unit.
Suppress the node in four forms below, and use the same \(H_{ab}=H_{ba}\) for a pair written in either order, by symmetry of each physical kernel.
Define
\[
 U_2=\mathcal D(H_{12},E_{22},E_{33})=(H_{12})_{11},
 \qquad U_4=\sum_{\{ab,cd\}}\mathcal D(H_{ab},H_{cd},E_{33}),
 \qquad U_6=\sum_{\{ab,cd,ef\}}\mathcal D(H_{ab},H_{cd},H_{ef}).
\]
The sums range over the three unordered pair partitions of the first four labels and the fifteen unordered pair partitions of all six.

For every prescribed subset of \(m\) nodes the two-panel bound above gives joint probability \(O(n^{-m/2})+O(e^{-cn})\) of \(|U_2|\le1\).
Consider next such a subset on which all \(|U_4|\le1\), and sum over the possible subsets of nodes with \(|U_2|\le1\).
For a specified such subset of size \(d\), the preceding estimate pays \(O(n^{-d/2})+O(e^{-cn})\) before drawing panels 3 and 4.
Condition on panels 1 and 2.
At each other node the coefficient of \((H_{34})_{22}\) in \(\mathcal D(H_{12},H_{34},E_{33})\) equals \(U_2\), of modulus greater than one.
Whenever panel 4 is paired to 1 or 2, its coefficient vector lies in the span of the real and imaginary images of those two already drawn vectors under all relevant transposed physical corners into panel 4.
This subspace is fixed before panel 3 and has bounded dimension since the number of kernels and nodes is fixed.
The two-panel bound for panels 3 and 4 therefore pays \(O(n^{-(m-d)/2})+O(e^{-cn})\) for the remaining nodes, conditionally and uniformly on the specified history.
Summing over the finitely many exact subsets gives \(O(n^{-m/2})+O(e^{-cn})\) for the joint four-panel smallness.

For the six-panel test, classify the nodes by \(|U_4|\le1\) after the first four panels.
When panels 5 and 6 pair together, the coefficient of \((H_{56})_{33}\) in the sum of these terms is \(U_4\) by trilinearity.
In every other term panel 6 pairs with a label \(j\le4\).
Its coefficient vector belongs to the span of the real and imaginary images of \(u_j\) in panel 6 under the corresponding corners, again fixed before panel 5.
Conditioning on the first four panels now gives the same multiplication of the four-panel cost on the small subset and the two-panel cost on its complement.
Thus for any fixed radius the probability of simultaneous smallness of \(U_6\) is \(O(n^{-s/2})+O(e^{-cn})\).

Finally apply Cartesian Cauchy--Schwarz once on each of the six independent panels to the original joint small-value event.
The \(64\) resamplings in a successful cube imply a sixfold finite difference of modulus at most \(64 C_0 |c_w|\) at each node.
All lower-degree terms vanish.
In total degree six the surviving monomials use each panel exactly once.
The two choices of order in each quadratic pair and the determinant polarization give precisely \(2^3 c_w U_6\), up to the common sign of the difference convention.
Taking the sixty-fourth root of the joint bound proves (1).
For \(D=256\) shifts assigned to at most \(k=O(\log^3 N)\) chronological steps with fresh columns and the stated incoming conditions, multiplication over steps and summation over assignments give \(O(k^{256}n^{-2})\) plus the old-minor and exponentially small errors.
The [separated-tuple integration](Yin_C_F0351_v9.md#terminal) converts this to summability of every fixed positive bad-area deviation on a bounded upper-half-plane compact, when the transitions have these hypotheses.

## Current assessment
[Selected decision](#decision-six-panel-reviewed)

## Assessment history

### Decision six-panel-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:27 |
| status | open |
| reason | The two-site residues and the three successive panel pairs give the claimed estimates, pending independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Cubic resolvent kernels](#statement) | Joint independence and the degree-six conditional estimate for original real Wigner laws. |
| argument | [Scalar specialization and residues](#argument) | Arbitrary finite sets of distinct complex nodes. |
| support | [Physical corner estimates](#corners) | Separated prescribed nonreal tuples, fixed-rank-fraction slack and arbitrary past-measurable rank \(O(k)\) changes. |
| support | [Six-panel contraction](#polarization) | Conditional probability exponent and summable separated-tuple bound. |

### Decision six-panel-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:32 |
| status | proved |
| reason | Two-site differentiation separates the nine kernel directions, and successive pair tests control the sixth Cartesian difference at all assigned nodes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Cubic kernel and joint probability bound](#statement) | The specified separated parameters and original fresh-row laws. |
| argument | [Complete argument](#argument) | Scalar, two-site and conditional physical-corner tests. |
| support | [Six-panel test](#polarization) | Small cofactor conditions and the product of conditional costs. |
| review | [Independent whole-proof review](../audits/reviews/Yin_R_F0371_v1.md#six-panel-whole-proof) | Complete fixed statement and its hypotheses. |

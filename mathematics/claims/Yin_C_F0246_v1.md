---
author: Yin
---

# Column bounds on Lipschitz graphs with derivative of bounded variation

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Suppose \(X=(X_1,\ldots,X_d)\) is a finite tuple of bounded normal generators of a finite von Neumann algebra \(M\) with faithful normal probability trace \(\tau\), satisfying the [actual starred ACSY condition](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Fix a selfadjoint coordinate \(S=X_i\) with actual distinguished vacuum \(\xi\) on the old represented starred core \(P_X\).
Let \(I=[l,r]\) be a compact interval containing \(\sigma(S)\).
Suppose \(g:I\to\mathbb R\) is absolutely continuous and its derivative has a real representative \(m\) of bounded variation.
Use its right-continuous representative in the interior and its one-sided values at the endpoints, and put \(V=|dm|((l,r))\), the total variation of the distributional derivative of \(m\).
Replace \(S\) by \(Z=h(S)\), where \(h(s)=s+i g(s)\).
Each other coordinate may be left unchanged or replaced by a bounded Borel function of itself which is one-to-one on a conull Borel set and has Borel inverse there.
Denote the resulting tuple by \(Y\).

The distinguished derivation at \(Z=Y_i\) has an actual vacuum on the full represented starred core \(P_Y\).
Write \(C=\mathrm{id}\otimes\tau\), \(E_{Y,i}=C\delta_{Y,i}\), \(H=L^2(M,\tau)\) and \(\Omega=1\).
There is an absolute constant \(A\) such that
\[
 \left(\sum_k\|E_{Y,i}p_k\|_2^2\right)^{1/2}
 \le A(1+V)\|\xi\|_2\left\|\sum_kp_k^*p_k\right\|^{1/2}
 \qquad(p_k\in P_Y,\ \text{finite columns}).                              \tag{1}
\]
The adjoint tuple has the same bound at its distinguished coordinate.
For the canonical operator with initial graph \(p\Omega\mapsto E_{Y,i}p\), both its closure and its Hilbert adjoint have domains containing \(M\Omega\).
Its negative closure satisfies the strong generator-first commutator at \(i\).

In particular any correlated selfadjoint tuple with actual conjugate variables has \(\mathsf A\) and \(\mathsf S\) after applying such a graph change to each coordinate.
The bound applies to continuous finite piecewise affine graphs and to \(S+i a|S|\), with \(V\le2|a|\) in the latter example.
Both countably many slope jumps of summable total magnitude and singular continuous slope variation are allowed.

## Argument

### The real parameter and its original column

Write \(N=W^*(S)\), \(\mu\) for the law of \(S\), and \(\xi_N=\mathbb E_N\xi\).
Its density \(\rho=d\mu/ds\), extended by zero to the line, satisfies
\[
                  \int_{\mathbb R}\rho^3\,ds\le A_0\|\xi_N\|_2^2 .          \tag{2}
\]
Indeed the [marginal packing estimate](Yin_C_F0233_v1.md#statement), part 1, applied to a real interval partition of mesh length \(\ell\), gives \(\sum_J\mu(J)^3/\ell^2\le A_0\|\xi_N\|_2^2\) for the disjoint interval projections and their individual centers.
The histograms on dyadic refinements of \(I\) therefore have bounded \(L^3\) norms and converge against continuous tests to \(\mu\).
Weak compactness and lower semicontinuity in \(L^3(I)\) give (2).
The spectral law is diffuse.

Let \(\delta\) be the original derivative at \(S\), and use the inner calculus \(I_{v\otimes w}(a\otimes d)=av\otimes wd\) on the coarse Hilbert tensor product.
Its partial liberation \(\gamma=I_{s-t}\delta\) differentiates the distinguished marginal by the inner difference and kills all the other marginal factors.
For its actual vacuum \(\eta=\gamma^*(1\otimes1)\) and joint left-right spectral measure \(\nu\), the [inverse-gap identity](Yin_C_F0238_v1.md#statement) gives
\[
                 \int_{s\ne t}\frac{d\nu(s,t)}{|s-t|^2}
                   =\|\xi-\xi_N\|_2^2,\qquad \nu\{s=t\}=0.                \tag{3}
\]
The target partial liberation acts by the same rules on the algebra generated algebraically by all the marginal von Neumann algebras, by the [invariance under a Borel relabelling](Yin_C_F0244_v1.md#the-invariant-liberation-derivation).
Its transformed inverse-gap integral stays finite since \(|h(s)-h(t)|\ge|s-t|\).
The [scalar Lipschitz graph criterion](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) gives an actual scalar vacuum for \(h_*\mu\) by (2), so the distinguished target derivation is actual by the inverse-gap criterion.
These arguments also apply with \(g\) replaced by \(-g\) to the adjoint tuple.

For a map on \(P_X\), let \(c(T)\) denote the least right column bound as in (1) with these inputs.
We have \(c(C\delta)\le4\|\xi\|_2\).
Indeed the distinguished real derivation takes value \(1\otimes1\) at \(S=S^*\) and zero at all other starred letters by the [normal generator formulas](Yin_C_F0076_v1.md#statement).
Consequently it is algebraic-valued, real under flip-adjoint, and coassociative, since the difference of its two iterates is an outer derivation vanishing on all generators.
These properties persist on adjoining two free Haar unitaries whose derivatives vanish and on which the [old vacuum is preserved](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words).
The [real coassociative estimate](../audits/literature/Mai15/Yin_U002.md#mai15-u002), Theorem 4.9, bounds the enlarged right slice on one input by \(2\|\xi\|_2\) times its operator norm.
The [two-Haar encoding](Yin_C_F0208_v1.md#encoding-finite-columns-by-two-haar-unitaries) transfers this bound to old columns with one more factor two.

### Decomposition by the variation of the slope

Put \(q(t)=1+i m(t)\), \(K(s,t)=(s-t)/(h(s)-h(t))\) for \(s\ne t\).
With \(B=(l,r)\), define for each \(b\in B\) and \(s,t\) on strictly opposite sides of \(b\)
\[
 \sigma=\operatorname{sign}(s-t),\qquad x=|s-b|,\quad y=|t-b|,\qquad
 H_b(s,t)=\frac{-i x}{q(t)\,\sigma(h(s)-h(t))\,(x+y)},\qquad
 J_b(s,t)=(s-t)H_b(s,t).                                                  \tag{4}
\]
Set both symbols to zero on the rest of the square.
Since \(|q|\ge1\) and \(|h(s)-h(t)|\ge x+y\) on the crossing set, \(|J_b|\le1\).
We claim that
\[
                      K(s,t)=q(t)^{-1}+\int_B J_b(s,t)\,dm(b)             \tag{5}
\]
for \(\mu^2\)-almost every pair.
Exclude the diagonal, the interval endpoints and all atoms of \(|dm|\) from both scalar variables, which removes a \(\mu^2\)-null set by diffuseness.
Let \(\overline m_{st}=(g(s)-g(t))/(s-t)\) be the average slope on the intervening interval.
For \(s>t\), integrating \(m(v)-m(t)=\int_{(t,v]}dm(b)\) in \(v\) gives
\[
 m(t)-\overline m_{st}
    =-\frac{1}{s-t}\int_{(t,s)}(s-b)\,dm(b).
\]
For \(s<t\), integrating \(m(t)-m(v)=\int_{(v,t]}dm(b)\) gives \(\int_{(s,t)}(b-s)\,dm(b)/(t-s)\) instead.
Thus the common signed expression is \(-\sigma\int x/(x+y)\,dm(b)\) over the open intervening interval.
Now \(K-q(t)^{-1}=i(m(t)-\overline m_{st})/[q(t)(1+i\overline m_{st})]\), and \(1+i\overline m_{st}=(h(s)-h(t))/(s-t)\).
This proves (5), including the sign in (4).

The separated symbol \(q(t)^{-1}\) costs at most \(2c(C\delta)\) for the slice on old columns, by the [product identity with bounded measurable coefficients](Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice).
It remains to bound \(C I_{J_b}\delta\) uniformly in \(b\).
On any subrectangle separated from the vertex on the first leg, \(H_b\) is bounded and \(I_{J_b}\delta=I_{H_b}\gamma\) there.
This permits the projection estimates for liberation to be applied to the residual in (5).

### A uniform estimate at one vertex

Take \(R=r-l>0\), \(r_j=2^{-j}R\) for \(j\ge0\), and \(Q_j=1_{\{|S-b|\le r_j\}}\).
Set \(t_j=\tau(Q_j)\) and \(d_j=(\|Q_j\eta Q_j\|_2+t_j^{3/2})/r_j\).
Uniformly in \(b\),
\[
                   \sum_{j\ge0}d_j^2\le A_1\|\xi\|_2^2.                  \tag{6}
\]
For the first term, \(\|Q_j\eta Q_j\|_2^2\le\nu\{0<|s-t|\le2r_j\}\) by (3).
At fixed \(u=|s-t|>0\), \(\sum_{u\le2r_j}r_j^{-2}\le A_2/u^2\) by geometric summation.
Tonelli and (3) give the required squared sum.
For the mass term let \(w_k=\mu\{r_{k+1}<|s-b|\le r_k\}\).
Hölder on this pair of real intervals gives \(\sum_k(w_k/r_k^{2/3})^3\le A_3\int\rho^3\), since its total length is at most \(2r_k\) and different shells are disjoint.
Diffuseness gives \(t_j=\sum_{k\ge j}w_k\), so
\[
 \frac{t_j}{r_j^{2/3}}
       =\sum_{k\ge j}2^{-2(k-j)/3}\frac{w_k}{r_k^{2/3}}.
\]
The triangle inequality for shifted \(\ell^3\) sequences and the geometric sum bound the \(\ell^3\) norm of this output by an absolute multiple of the input norm.
Cubing and using (2) proves \(\sum_jt_j^3/r_j^2\le A_4\|\xi_N\|_2^2\), and hence (6).

On one orientation of the crossing set fix \(r_{j+1}<x\le r_j\) on the first side, with spectral projection \(e_j\).
On the other side first use the whole range \(0<y\le r_j\) as a single projection \(f\).
For larger \(y\) use one projection \(f\) for each shell \(r_{k+1}<y\le r_k\), \(k<j\).
In the first case \(e_j\vee f\le Q_j\), in the second \(e_j\vee f\le Q_k\).
The projections \(e_j,f\) are orthogonal.
By the [measurable block estimate](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block), (6) there, \(G=C I_{e_j\otimes f}\gamma\) has column cost bounded respectively by \(A_5r_jd_j\) and \(A_5r_kd_k\).
Here \(\|(e_j\vee f)\eta(e_j\vee f)\|_2\le\|Q_k\eta Q_k\|_2\) whenever the union is under \(Q_k\), since it compresses that Hilbert vector on both sides.

There is a separated Laplace representation of \(H_b\) on each rectangle.
Use
\[
 \frac{1}{\sigma(h(s)-h(t))(x+y)}
   =\int_0^\infty\!\int_0^\infty
       e^{-\lambda\sigma(h(s)-h(b))-\alpha x}
       e^{\lambda\sigma(h(t)-h(b))-\alpha y}\,d\alpha\,d\lambda .        \tag{7}
\]
The real parts of the two exponents are \(-(\lambda+\alpha)x\) and \(-(\lambda+\alpha)y\).
Include \(x\) in the first factor and \(-i/q(t)\) in the second.
Let \(x_{\min}=r_j/2\) and put \(y_{\min}=0\) for the first rectangle, \(y_{\min}=r_k/2\) for a larger shell.
After restricting the factors to their respective spectral projections, the integral of the product of their supremum norms is at most
\[
  \int_0^\infty\!\int_0^\infty r_j e^{-(\lambda+\alpha)(x_{\min}+y_{\min})}
                   \,d\alpha\,d\lambda
    =\frac{r_j}{(x_{\min}+y_{\min})^2}.                                  \tag{8}
\]
All separated factors are bounded measurable marginal functions.
For each product \(v(s)w(t)\) the localized slice costs at most \(2c(G)\|v\|_\infty\|w\|_\infty\).
To see this directly, let \(\theta=I_{e_j\otimes f}\gamma\).
The identity \(C I_{v\otimes w}\theta(p)=(G(pw)-pG(w))v\) holds first for marginal polynomial \(w\).
For measurable \(w\), choose uniformly bounded marginal polynomial approximants \(w_n\) converging strongly-star and in \(L^2\).
Their liberation derivatives converge by the explicit inner-difference formula on the marginal, so \(\theta(w_n)\to\theta(w)\) and \(\theta(pw_n)\to\theta(pw)\) in coarse norm on this enlarged core. [Bounded marginal liberation graph](Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy)
For a fixed polynomial column the products with these approximants have column norms at most \(\|w\|_\infty\|\sum p_k^*p_k\|^{1/2}\) in the limit superior, by taking approximants of norm at most \(\|w\|_\infty+o(1)\).
For the second term use \(\sum_k\|p_kG(w)\|_2^2\le\|\sum_k p_k^*p_k\|\|G(w)\|_2^2\).
These facts prove the desired column estimate for bounded \(v,w\).
The double integral in (7) converges on each fixed coarse input by (8), for instance by first integrating over bounded parameter squares and then taking their increasing limit.

Thus the cost on \(0<y\le r_j\) is at most \(A_6d_j\), while a larger \(y\)-shell costs at most \(A_6\,2^{k-j}d_k\).
The entire slice with its first variable in shell \(j\) has cost at most \(A_6(d_j+\sum_{k<j}2^{k-j}d_k)\).
All its outputs have right support in \(e_j\) because the first inner spectral projection remains at the right end of the first tensor leg after slicing.
These supports are orthogonal for distinct first shells and also for the two first-side orientations.
For a fixed test column, square-sum over first shells and orientations, using (6) and the triangle inequality for shifted \(\ell^2\) sequences with weights \(2^{-n}\).
The sum over finitely many first shells has column cost at most \(A_7\|\xi\|_2\), uniformly in the truncation and the vertex \(b\).
As the truncation increases, the first-shell-restricted symbols multiplying \(\delta(p)\) are bounded by one by (4) and converge to \(J_b\) off the two endpoint lines.
Each such line is null for \(\mu^2\) for fixed \(b\), and the coarse vector spectral measures are dominated by \(\mu^2\). [Inner spectral measure class](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core)
Dominated convergence proves \(c(C I_{J_b}\delta)\le A_7\|\xi\|_2\).

### Integration over vertices and the target mixed core

The symbols \(J_b(s,t)\) are jointly Borel in \(b,s,t\) and uniformly bounded.
For each coarse vector \(v\), \(b\mapsto I_{J_b}v\) is strongly measurable.
Indeed the cyclic spectral subspace of \(v\) is \(L^2\) of its finite scalar measure on \(I^2\), which is separable, and joint measurability gives measurable scalar tests by Fubini.
The same observation holds on each finite direct sum of such spaces.
Since \(|dm|(B)=V<\infty\), Bochner integration against \(dm\) is allowed.
Scalar testing and Fubini in these cyclic spaces identify the integral with \(I_{\int J_b\,dm(b)}v\).
In particular the lines at the endpoints of any single vertex can be discarded also after integration by Fubini, even when \(dm\) has atoms.
Taking \(v=\delta(p_k)\), \(C\) commutes with this integral by boundedness.
The triangle inequality in the finite column Hilbert space, (5) and the uniform vertex bound yield
\[
                 c(C I_K\delta)\le2c(C\delta)+A_7 V\|\xi\|_2
                                    \le A(1+V)\|\xi\|_2                    \tag{9}
\]
on the old mixed core.

On target mixed starred words use [the bounded graph approximation for the relabelled core](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple).
Its graph argument needs Lipschitz regularity at the distinguished coordinate and only bounded Borel relabelling at the omitted coordinates.
It identifies \(\delta_{Y,i}=I_K\bar\delta\) there by the generator values and supplies old-core approximating columns with convergent coarse derivatives and limit superior of their column norms at most \(1+\varepsilon\) for each target column of norm at most one.
The ratio symbol is bounded by one, so (9) passes through this graph limit, and then \(\varepsilon\downarrow0\) proves (1).
For the adjoint tuple the old real-coordinate derivative remains real with the same vacuum on the same core, since the omitted starred letters are still killed.
The new graph changes \(g\) to \(-g\) and preserves \(V\), so the same right column estimate bounds the original left slice on a single input by tracial involution.
The [two-slice domain theorem](Yin_C_F0072_v1.md#statement), part B, gives the two bounded-vector domains.
The identity \(E_{Y,i}(Y_jp)-Y_jE_{Y,i}(p)=\delta_{ij}\tau(p)1\) extends to the closure by graph approximation and gives the strong commutator for its negative.
Applying this at every graph of a selfadjoint tuple proves the final assertion.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T11:00 |
| status | open |
| reason | The uniform column bound for graphs with slope of bounded variation, its mixed-core transfer and its two domain conclusions are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The BV-slope bound on all mixed columns in both orientations, the canonical bounded-vector domains and the simultaneous application to correlated selfadjoint tuples. |
| argument | [Argument](#argument) | Secant expansion by the slope variation, uniform two-sided Laplace rectangles, orthogonal first-shell outputs, inverse-gap and density sums, signed integration and norm-controlled transfer of target columns. |
| dependency | [Marginal packing](Yin_C_F0233_v1.md#statement) | Part 1 on disjoint scalar interval projections gives the \(L^3\) bound on the old real parameter density. |
| dependency | [Inverse-gap vacuum criterion](Yin_C_F0238_v1.md#statement) | Liberation vacuum and its spectral inverse-gap identity for the old distinguished coordinate, and the criterion for actual target vacuum existence. |
| dependency | [Coarse measure class](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Absolute continuity of each marginal inner spectral measure with respect to product law, for shell and measure-integration limits. |
| dependency | [Invariant liberation](Yin_C_F0244_v1.md#the-invariant-liberation-derivation) | Preservation of the actual liberation rules and its vacuum under bounded conull Borel coordinate changes. |
| dependency | [Scalar Lipschitz graph](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | A compact real \(L^3\) probability density on the parameter has an actual scalar vacuum after a Lipschitz graph change. |
| dependency | [Normal derivative at a real generator](Yin_C_F0076_v1.md#statement) | Part 1, all omitted starred values vanish and the selfadjoint distinguished derivative is real. |
| dependency | [Two-Haar extension](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | The algebraic free extension preserving the actual old vacuum and killing both Haar factors. |
| dependency | [Two-Haar column encoding](Yin_C_F0208_v1.md#encoding-finite-columns-by-two-haar-unitaries) | Operator-norm cost at most two and exact Hilbert orthogonality for each fixed old column. |
| dependency | [Real coassociative estimate](../audits/literature/Mai15/Yin_U002.md#mai15-u002) | Theorem 4.9 on the actual algebraic real derivation in the free enlargement, with right contraction bound \(2\|\xi\|_2\). |
| dependency | [Measurable separated multipliers](Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice) | Equations (2)–(3) for the constant first-leg symbol and bounded measurable reciprocal tangent on the second leg. |
| dependency | [Localized liberation column](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Equation (6) for two disjoint measurable projections, the compression vacuum and trace to the power \(3/2\). |
| dependency | [Bounded marginal liberation graph](Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) | Enlarged graph with bounded Borel factors and graph approximation for the finite projection-inserted liberation calculations. |
| dependency | [Relabelled mixed core](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Identification on the target generators, graph approximation at the distinguished and omitted factors, and preservation of the input norm for finite columns. |
| dependency | [Actual canonical domains](Yin_C_F0072_v1.md#statement) | Part B on the original algebraic canonical right slice and its actual Hilbert-space adjoint after bounding both slices. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T11:05 |
| status | proved |
| reason | Adopt the uniform original two-domain estimate for graphs with slope of bounded variation after independent whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The BV-slope bound on all mixed columns in both orientations, the canonical bounded-vector domains and the simultaneous application to correlated selfadjoint tuples. |
| argument | [Argument](#argument) | Secant expansion by the slope variation, uniform two-sided Laplace rectangles, orthogonal first-shell outputs, inverse-gap and density sums, signed integration and norm-controlled transfer of target columns. |
| dependency | [Marginal packing](Yin_C_F0233_v1.md#statement) | Part 1 on disjoint scalar interval projections gives the \(L^3\) bound on the old real parameter density. |
| dependency | [Inverse-gap vacuum criterion](Yin_C_F0238_v1.md#statement) | Liberation vacuum and its spectral inverse-gap identity for the old distinguished coordinate, and the criterion for actual target vacuum existence. |
| dependency | [Coarse measure class](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Absolute continuity of each marginal inner spectral measure with respect to product law, for shell and measure-integration limits. |
| dependency | [Invariant liberation](Yin_C_F0244_v1.md#the-invariant-liberation-derivation) | Preservation of the actual liberation rules and its vacuum under bounded conull Borel coordinate changes. |
| dependency | [Scalar Lipschitz graph](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | A compact real \(L^3\) probability density on the parameter has an actual scalar vacuum after a Lipschitz graph change. |
| dependency | [Normal derivative at a real generator](Yin_C_F0076_v1.md#statement) | Part 1, all omitted starred values vanish and the selfadjoint distinguished derivative is real. |
| dependency | [Two-Haar extension](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | The algebraic free extension preserving the actual old vacuum and killing both Haar factors. |
| dependency | [Two-Haar column encoding](Yin_C_F0208_v1.md#encoding-finite-columns-by-two-haar-unitaries) | Operator-norm cost at most two and exact Hilbert orthogonality for each fixed old column. |
| dependency | [Real coassociative estimate](../audits/literature/Mai15/Yin_U002.md#mai15-u002) | Theorem 4.9 on the actual algebraic real derivation in the free enlargement, with right contraction bound \(2\|\xi\|_2\). |
| dependency | [Measurable separated multipliers](Yin_C_F0244_v1.md#bounded-measurable-coefficients-before-the-slice) | Equations (2)–(3) for the constant first-leg symbol and bounded measurable reciprocal tangent on the second leg. |
| dependency | [Localized liberation column](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Equation (6) for two disjoint measurable projections, the compression vacuum and trace to the power \(3/2\). |
| dependency | [Bounded marginal liberation graph](Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) | Enlarged graph with bounded Borel factors and graph approximation for the finite projection-inserted liberation calculations. |
| dependency | [Relabelled mixed core](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Identification on the target generators, graph approximation at the distinguished and omitted factors, and preservation of the input norm for finite columns. |
| dependency | [Actual canonical domains](Yin_C_F0072_v1.md#statement) | Part B on the original algebraic canonical right slice and its actual Hilbert-space adjoint after bounding both slices. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0255_v1.md#finding) | Both orientations, baseline-independent column bound, Stieltjes decomposition, uniform localized inverse-gap and mass estimates, strong commutator, and all stated simultaneous graphs. |

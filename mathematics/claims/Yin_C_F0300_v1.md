---
author: Yin
---

# Divergent localized curvature bounds on a single Lipschitz graph

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

There is a nondecreasing \(1\)-Lipschitz function \(g:[0,1]\to\mathbb R\) such that the law \(\mu\) of \(Z=s+ig(s)\) for uniform \(s\in[0,1]\) has an actual scalar conjugate variable and finite total squared Menger curvature, but the following localization cost is bounded below by an absolute constant at every sufficiently small radius.

Write \(K=\operatorname{supp}\mu\), let \(\kappa(z,w,v)\) be reciprocal circumradius with value zero for collinear or repeated triples, and let \(\mathcal A_r\) be any countable measurable partition of \(K\).
For \(A\in\mathcal A_r\) put
\[
 q_{r,A}(z,v)=\int_A
     1_{\{r/2<\operatorname{diam}\{z,w,v\}\le r\}}
     \kappa(z,w,v)^2\,d\mu(w).
\]
Choose any measurable \(B_A\subseteq K\) such that \(q_{r,A}\) vanishes \(\mu^2\)-almost everywhere off \(B_A^2\), and set
\[
             H(r)=\sum_{A\in\mathcal A_r}\|q_{r,A}\|_{L^\infty(\mu^2)}
                                                \mu(B_A)^2 .
\]
Then \(H(r)\ge c>0\) for every sufficiently small \(r>0\), uniformly over both choices.
There are choices with \(H(r)\le C\) for every \(r>0\).
In particular even the infimum over choices costs order \(N\) over \(N\) successive sufficiently small dyadic scales.
The sums of the actual curvature integrals over disjoint diameter shells are finite.
For this scalar law the signed curvature form on analytic-core unitaries is nonnegative.
Consequently the localized estimate in [the square-density argument](Yin_C_F0297_v1.md#summing-by-triangle-diameter) cannot cover all actual planar laws just by inserting the actual kernel suprema or refining the partition of the third point.
Decompositions depending on the two endpoint variables separately are outside the lower bound.

## Argument

### The graph and the supply of almost horizontal secants

Choose a closed nowhere dense set \(F\subset[0,1]\) of Lebesgue measure at least \(3/4\).
For example start with the unit interval and at step \(k\ge1\) remove from the middle of each remaining interval an open fraction \(2^{-k-2}\) of its length.
The removed measures sum to at most \(1/4\), and the largest remaining interval length tends to zero.
Put \(g(s)=\int_0^s1_{[0,1]\setminus F}(y)\,dy\) and write \(h(s)=s+ig(s)\).
The [Lipschitz graph theorem](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) supplies an actual scalar vacuum since the uniform parameter density belongs to \(L^3(ds)\).
The [scalar geometric criterion](Yin_C_F0255_v1.md#statement) gives finite total curvature and both canonical domains.
The probability is diffuse and \(\mu(B(z,r))\le2r\) by horizontal projection.

For every sufficiently small \(r>0\) a set \(F_r\subseteq F\cap[1/8,7/8]\) of measure at least \(1/4\) satisfies
\[
                       |(x-r,x+r)\setminus F|\le r/40
                  \qquad (x\in F_r).                                     \tag{1}
\]
Indeed \(F\cap[1/8,7/8]\) has measure at least \(1/2\).
For a fixed finite-stage set \(F_k\supset F\), discard from this set of centers the \(r\)-neighborhood of the finitely many endpoints of \(F_k\), of measure \(O_k(r)\).
At each other center the interval is inside \(F_k\), and the integral of \(r^{-1}|(x-r,x+r)\cap(F_k\setminus F)|\) in \(x\) is at most \(2|F_k\setminus F|\) by Fubini.
Since the latter tends to zero with \(k\), Markov's inequality and then small \(r\) give (1).
Using the explicit finite-stage construction above suffices for this proof.

Choose a maximal family of centers \(x_l\in F_r\) with pairwise distances at least \(3r\).
Intervals of radius \(3r\) about them cover \(F_r\), so their number is at least \(1/(24r)\).
Use the following windows in the parameter line, interpreted as graph subsets under \(h\):
\[
       W_l=[x_l-r/32,x_l+r/32],\qquad
       V_l=[x_l+11r/16,x_l+23r/32].
\]
Write \(\widetilde W_l=h(W_l)\) and \(\widetilde V_l=h(V_l)\).
All windows stay in \((0,1)\) when \(r\) is sufficiently small, and the \(V_l\) are disjoint.
For \(w\in\widetilde W_l\) and \(v\in\widetilde V_l\) the horizontal displacement lies between \(21r/32\) and \(3r/4\), while the absolute vertical displacement is at most \(r/40\) by (1).
For \(z,v\in\widetilde V_l\) their distance is at most \(\sqrt2\,r/32\).
Thus every triangle with third point in \(\widetilde W_l\) and endpoints in \(\widetilde V_l\) belongs to the indicated diameter shell.

Each \(V_l\) contains a nonempty open subinterval \(I_l\) in the complement of \(F\).
There \(g\) is affine of slope one.
For two distinct endpoints on \(h(I_l)\) and \(w\in\widetilde W_l\), the distance from \(w\) to the slope-one line through the endpoints is at least \((21/32-1/40)r/\sqrt2\).
The formula for reciprocal circumradius as twice that distance divided by the distances from \(w\) to the endpoints gives \(\kappa(z,w,v)\ge c_1/r\).
Both endpoints range independently over a set of positive mass, however short \(I_l\) is.

### Any supporting square must also carry the remote window

Fix a cell \(A\) with \(a_l=\mu(A\cap\widetilde W_l)>0\).
The preceding estimate gives \(\|q_{r,A}\|_\infty\ge c_1^2 a_l/r^2\).
Furthermore \(\mu(\widetilde V_l\setminus B_A)=0\).
Indeed for a fixed \(v\in\widetilde V_l\) and \(w\in A\cap\widetilde W_l\), the secant \(wv\) has slope strictly less than one in absolute value.
It therefore contains at most one point of the segment \(h(I_l)\).
For almost every \(z\in h(I_l)\) the triangle has positive curvature and belongs to the shell.
Fubini and \(a_l>0\) give \(q_{r,A}(z,v)>0\) for almost every pair in \(h(I_l)\times\widetilde V_l\).
Since \(q_{r,A}\) is supported on \(B_A^2\) almost everywhere and \(\mu(h(I_l))>0\), the assertion follows.

Let \(m_A\) be the number of indices with \(a_l>0\).
The disjoint windows each have mass \(r/32\), so \(\mu(B_A)\ge m_A r/32\).
For \(m_A>0\),
\[
 \|q_{r,A}\|_\infty\mu(B_A)^2
 \ge (c_1^2/32^2)m_A^2\max_l a_l
 \ge (c_1^2/32^2)\sum_l a_l .
\]
Summing over the partition gives a constant times \(\sum_l\mu(\widetilde W_l)\ge(1/(24r))(r/16)>0\).
This lower bound includes partitions whose cells have arbitrarily small mass and all permissible supports for their kernels.

For the upper estimate take planar grid cells of side \(r\) and their concentric fivefold dilates as supporting squares, intersected with \(K\).
Then \(\|q_{r,A}\|_\infty\le16\mu(A)/r^2\) by the diameter bound and \(\mu(B_A)\le5r\) by horizontal projection.
This yields \(H(r)\le400\).

Finally, for the scalar original algebra partial liberation acts by \(u(z)-u(v)\).
For any bounded measurable \(u\) the signed curvature integral is absolutely convergent since \(\iint g_\mu\,d\mu^2=\iiint\kappa^2\,d\mu^3<\infty\), where \(g_\mu(z,v)=\int\kappa(z,w,v)^2d\mu(w)\).
Symmetry gives
\[
 \operatorname{Re}\iint\overline{u(z)}(u(z)-u(v))g_\mu(z,v)\,d\mu(z)d\mu(v)
       =\tfrac12\iint|u(z)-u(v)|^2g_\mu(z,v)\,d\mu(z)d\mu(v)\ge0.
\]
On analytic-core unitaries this is precisely the form used in the [localized energy proof](Yin_C_F0297_v1.md#summing-by-triangle-diameter), by first using finite sums of bounded shell kernels, then passing to the limit by integrability and the gap-tensor convergence there.
This graph disproves universal summability of the proposed majorant and leaves the implication for general correlated normal tuples open.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T15:38 |
| status | open |
| reason | Fix the graph obstruction for arbitrary third-variable partitions and supporting spectral squares at every small scale. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual scalar law, uniform shell lower bound, bounded optimal cost per scale, finite curvature and nonnegative scalar form. |
| argument | [Argument](#argument) | Fat Cantor graph, near-horizontal secants and slope-one subintervals, Fubini support test, uniform packing and scalar sign. |
| dependency | [Lipschitz graph actuality](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | An actual scalar conjugate variable for the graph of a Lipschitz function over a compact real parameter law with \(L^3\) density. |
| dependency | [Scalar geometric criterion](Yin_C_F0255_v1.md#statement) | The signed curvature integral is finite and the scalar canonical operator and adjoint have the required domains. |
| dependency | [Localized shell argument](Yin_C_F0297_v1.md#summing-by-triangle-diameter) | The cost tested here, its original grid choices and the passage from shell kernels to the actual signed form. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T15:41 |
| status | proved |
| reason | Independent review verified the lower bound over all third-variable partitions and supporting squares, finite total curvature and the nonnegative signed form on the scalar graph. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual scalar law, uniform shell lower bound, bounded optimal cost per scale, finite curvature and nonnegative scalar form. |
| argument | [Argument](#argument) | Fat Cantor graph, near-horizontal secants and slope-one subintervals, Fubini support test, uniform packing and scalar sign. |
| dependency | [Lipschitz graph actuality](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | An actual scalar conjugate variable for the graph of a Lipschitz function over a compact real parameter law with \(L^3\) density. |
| dependency | [Scalar geometric criterion](Yin_C_F0255_v1.md#statement) | The signed curvature integral is finite and the scalar canonical operator and adjoint have the required domains. |
| dependency | [Localized shell argument](Yin_C_F0297_v1.md#summing-by-triangle-diameter) | The cost tested here, its original grid choices and the passage from shell kernels to the actual signed form. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0308_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

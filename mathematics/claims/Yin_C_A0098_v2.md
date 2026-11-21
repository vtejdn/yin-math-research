---
author: Yin
---
# Three-label progressions, explicit Følner bounds, and kernel deficiency

## Statement and counts

Let \(g_1,g_2,g_3\) be distinct elements of a torsion-free group \(G\), and let \(B\subset G\) be finite and nonempty.
Assume that every element of \(\{g_1,g_2,g_3\}B\) has at least two representations \(g_i b\).
Write \(N=|B|\) and
\[
 t_1=g_2^{-1}g_1,\qquad
 t_2=g_3^{-1}g_2,\qquad
 t_3=g_1^{-1}g_3,\qquad t_3t_2t_1=1.                       \tag{1}
\]
For each \(i\), take the directed translation graph on \(B\) with edges \(b\to t_i b\) whenever both vertices belong to \(B\).
The graphs have no directed cycles, since every \(t_i\) has infinite order.
Let \(P_i\) be its number of degree-two vertices, \(I_i\) its number of isolated vertices, and \(E_i\) its number of edges.
Thus \(P_i\) is also the number of starting points \(b\) of progressions \(b,t_i b,t_i^2b\) inside \(B\).
Set
\[
                         P=\sum_iP_i,\qquad I=\sum_iI_i.
\]
These counts retain the label-pair multiplicity: if two ratios happen to be equal or inverse, their graphs are still counted separately.
Let \(Q\) be the number of product fibers with three representations.

Let \(K\subset B\) be the union of all the degree-two vertex sets and put \(s=|K|\).
A vertex outside \(K\) has degree one in each of the three graphs.
Call these vertices good.
Let \(J\) count the two-representation product fibers whose two column labels both belong to \(K\).
Then
\[
 2E_i=N+P_i-I_i,\qquad P-I=3Q,\qquad
 s\le P,\qquad Q\le P/3,                                   \tag{2}
\]
and in fact
\[
                              P\ge2.                       \tag{3}
\]
In particular the original three-term progression conclusion holds, with all three vertices distinct.

There are two classes \(B_+,B_-\) of good vertices, defined by their directed cycles on the label triangle below.
Put
\[
                         d_i=|t_iB_+\mathbin\triangle B_-|.
\]
Their exact total boundary is
\[
                    d_1+d_2+d_3=3s-3Q-2J.                  \tag{4}
\]

If \(s<N\), choose the larger of the two cycle classes as \(U\), and let \(V\) be the other class.
If \(U=B_+\), put \(\varepsilon=1\); if \(U=B_-\), put \(\varepsilon=-1\).
Choose \(b\in\{1,2,3\}\) with \(d_b=\min_i d_i\), and set
\[
                   q_i=(t_b^\varepsilon)^{-1}t_i^\varepsilon
                   \quad(i\ne b).
\]
Then
\[
 |U|\ge(N-s)/2,\qquad
 \frac{\sum_{i\ne b}|q_iU\mathbin\triangle U|}{|U|}
 \le\frac{8(s-Q-\frac23J)}{N-s}.                            \tag{5}
\]
In particular, when \(P<N\), the right-hand side is at most
\[
                              \frac{8P}{N-P}.              \tag{6}
\]
When \(s=N\), there are no good vertices and no nonempty Følner set is supplied by this construction.
When \(s<N\) but \(P\ge N\), formula (5) remains valid and (6) is not used.

To state expansion in a fixed subgroup, let
\[
 H=\langle t_b^{-1}t_i:i\ne b\rangle.
\]
This subgroup is independent of the base index \(b\).
For each base index define
\[
 h_b=\inf_{\varnothing\ne F\subset H,\ F\ {\rm finite}}
       \frac{\sum_{i\ne b}|(t_b^{-1}t_i)F\mathbin\triangle F|}{|F|},
 \qquad h_*=\min_{b=1,2,3}h_b.                              \tag{7}
\]
Here the sum has two terms, each a symmetric difference; this fixes the normalization of the expansion constant.
One has
\[
 h_*(N-s)\le8(s-Q-\tfrac23J),
 \qquad
 P\ge s\ge\frac{h_*N+8Q+\frac{16}{3}J}{h_*+8}
       \ge\frac{h_*}{h_*+8}N.                              \tag{8}
\]
The inequalities in (8) remain valid when \(s=N\).
For \(s<N\), a nonempty finite set in \(H\), or in the conjugate subgroup arising from \(\varepsilon=-1\), can be extracted with the ratio in (5).

Finally fix nonzero left coefficients \(\alpha_1,\alpha_2,\alpha_3\) in a field \(k\), and suppose the coefficient map
\[
 \mathcal M_\alpha:k^B\longrightarrow k^{\{g_1,g_2,g_3\}B},
 \qquad
 (\mathcal M_\alpha z)_h=\sum_{g_i b=h}\alpha_i z_b
\]
has a kernel vector with every coordinate nonzero.
Let \(c\) be the number of components of the full column collision graph, where every pair of representations in one fiber joins their column labels.
Let \(c_2\) be its component count after retaining only the edges from two-representation fibers, including isolated vertices.
Then
\[
 2c\le P,\qquad c_2\le c+2Q,
\]
\[
 \dim_k\ker\mathcal M_\alpha
 \le\left\lfloor\frac{c_2+c}{2}\right\rfloor
 \le c+Q
 \le\lfloor P/2\rfloor+Q
 \le\frac56P.                                             \tag{9}
\]
For \(P=2\), necessarily \(Q=0\), the collision graph is connected, and this kernel is one-dimensional.
This last assertion includes the stated existence of a full-support kernel vector.

## The local degree identity

At a vertex \(b\in B\), let \(p_b\) count the colors in which it has degree two and let \(i_b\) count the colors in which it is isolated.
On the triangle with vertices \(1,2,3\), include an arrow \(i\to j\) whenever \(g_i b=g_j b'\) for some \(b'\in B\).
Each represented output \(g_i b\) has two or three representations, so label \(i\) has one or two outgoing arrows.
Let \(r_b\) count those labels \(i\) for which \(g_i b\) is a three-representation output.
The total number of arrows is \(3+r_b\).

For a fixed unordered label pair, the number of these arrows is the degree of \(b\) in its translation graph: zero, one, or two.
Summing the degrees also gives \(3+p_b-i_b\).
Therefore
\[
                             p_b-i_b=r_b\ge0.               \tag{10}
\]
In particular any isolated vertex in one color is a degree-two vertex in another color.
This proves that every vertex outside \(K\) has degree one in all three colors.
Every column appearing in a triple fiber belongs to \(K\).

In a finite union of paths, the degree sum gives \(2E_i=N+P_i-I_i\).
Also each triple fiber supplies exactly three row-column incidences, so \(\sum_b r_b=3Q\).
Summing (10) proves \(P-I=3Q\).
This establishes (2).

## Good cycles and the exact boundary

At a good vertex the three arrows give an orientation of the label triangle.
Each label has at least one outgoing arrow, and there are exactly three arrows.
Thus every label has exactly one outgoing arrow.
The orientation is one of the two cycles
\[
 1\to2\to3\to1,\qquad 1\to3\to2\to1.
\]
These define \(B_+\) and \(B_-\), respectively.
Along an edge with two good endpoints, the orientation of its label pair reverses.
The endpoints consequently have opposite cycle types.
For every color,
\[
 t_iB_+\subseteq B_-\cup K,\qquad
 t_i^{-1}B_-\subseteq B_+\cup K.                            \tag{11}
\]

An edge between \(B_+\) and \(K\) contributes to \(t_iB_+\setminus B_-\).
An edge between \(B_-\) and \(K\) contributes to \(B_-\setminus t_iB_+\).
Every good-bad edge is of exactly one of these types.
Hence \(d_i\) is precisely the number of color-\(i\) edges between \(K\) and its complement.

The total degree of \(K\) over all colors, using (10), is
\[
                         3s+\sum_{b\in K}r_b=3s+3Q.
\]
Each triple fiber has three distinct column labels: equality of two columns would force equality of two left labels.
Its three pairwise edges therefore form a triangle entirely inside \(K\).
Different fibers contribute different colored edges.
Thus there are exactly \(3Q+J\) internal edges of \(K\), counting all colors.
Subtracting twice this number from its degree sum proves (4).

This count must retain the triple triangles.
Counting all incidences at triple fibers as possible boundary edges would instead give a weaker and unnecessary error term.

## Excluding zero or one labelled progression

If \(P=0\), then \(K\) is empty, \(Q=0\), and (4) gives \(d_i=0\) for all \(i\).
At least one cycle class is nonempty, and its color neighbors show that both are nonempty.
Consequently
\[
                         t_1B_+=t_2B_+=t_3B_+=B_-.
\]
Every \(t_j^{-1}t_i\) stabilizes the nonempty finite set \(B_+\).
Left translation by such an element has a finite orbit, so some positive power fixes a point.
Cancellation and torsion-freeness give \(t_j^{-1}t_i=1\).
All three \(t_i\) are equal to an element \(t\), and (1) gives \(t^3=1\).
Then \(t=1\), contradicting the distinct left labels.

If \(P=1\), equation (2) forces \(Q=0\) and \(I=1\).
Equation (10) now says \(p_b=i_b\) at every vertex.
The unique degree-two occurrence and unique isolated occurrence must therefore be at the same vertex, in different colors.
The three values \(P_i-I_i\) are a permutation of \(1,-1,0\).
But the integers \(E_i\) in (2) require each \(P_i-I_i\) to have the same parity as \(N\).
This contradiction proves (3).

## Both signs, cosets, and the Følner estimate

If the positive class is chosen, (11) uses \(t_i\).
If the negative class is chosen, it uses \(t_i^{-1}\).
The symmetric-difference sizes are the same in both cases, because
\[
 |t_i^{-1}B_-\mathbin\triangle B_+|
             =|B_-\mathbin\triangle t_iB_+|=d_i.
\]
Writing \(\tau_i=t_i^\varepsilon\), the triangle inequality gives
\[
 |q_iU\mathbin\triangle U|
   =|\tau_iU\mathbin\triangle\tau_bU|
   \le d_i+d_b.
\]
Since \(d_b\) is minimal,
\[
 \sum_{i\ne b}|q_iU\mathbin\triangle U|
 \le(d_1+d_2+d_3)+d_b
 \le\tfrac43(d_1+d_2+d_3)
 =4(s-Q)-\tfrac83J.
\]
Together with \(|U|\ge(N-s)/2>0\), this proves (5).
Using \(s\le P<N\), \(Q,J\ge0\), gives (6).

For the positive choice the subgroup generated by the \(q_i\) is \(H\).
Its independence of \(b\) follows by writing
\[
 t_b^{-1}t_i=(t_1^{-1}t_b)^{-1}(t_1^{-1}t_i)
\]
and reversing the role of the bases.
For the negative choice, \(q_i=t_bt_i^{-1}\), and
\[
 t_b^{-1}q_it_b=t_i^{-1}t_b=(t_b^{-1}t_i)^{-1}.              \tag{12}
\]
Thus its subgroup is \(t_bHt_b^{-1}\), and its expansion constant for these two generators equals \(h_b\).
Conjugation preserves cardinalities, and replacing a generator by its inverse preserves \(|qF\mathbin\triangle F|\).

For a subgroup acting by left translation on \(G\), the orbits are the right cosets \(Hg\).
Partition \(U\) into these orbits, using the conjugate subgroup instead when \(\varepsilon=-1\).
Each generator preserves every orbit, so the numerator and denominator of the boundary ratio are sums over the nonempty pieces.
At least one piece has ratio no larger than the whole \(U\).
Right multiplication by its representative's inverse places that finite set inside the subgroup without changing the ratio.
This proves the asserted Følner-set extraction.
Applying (7) to every orbit also gives
\[
 h_b|U|\le\sum_{i\ne b}|q_iU\mathbin\triangle U|.
\]
Combine this with (5), and use \(h_*\le h_b\), to obtain the first inequality of (8) when \(s<N\).
When \(s=N\), both good classes are empty and (4) gives \(s-Q-\frac23J=0\), so that inequality is still true.
Rearranging it proves all of (8).

## Coefficient-kernel deficiency

Every component of the full collision graph inherits the no-singleton condition: all representations of an output are joined within one component.
Every progression is likewise contained in one component.
Apply (3) to each of them.
This gives \(2c\le P\).
Adding a triple fiber to the double-edge graph can join at most three components, reducing their number by at most two.
Adding all \(Q\) triple fibers gives \(c_2-c\le2Q\).

Let \(v\in\ker\mathcal M_\alpha\) have all coordinates nonzero, and write an arbitrary candidate vector as \(z_b=v_bu_b\).
In a double fiber its two nonzero coefficients sum to zero at \(v\).
The equation for \(z\) therefore becomes a nonzero multiple of \(u_b-u_{b'}=0\).
All \(u_b\) are constant on each component of the double-edge graph, leaving \(c_2\) scalar variables.

A triple fiber supplies three nonzero weights summing to zero.
If its vertices are in three different double-edge components, it gives a three-variable equation with all coefficients nonzero.
If they occupy two components, the two combined weights are nonzero opposites, since one component contains a single original vertex.
It gives a nonzero two-variable equation.
If all three vertices lie in one component, its equation vanishes.
Thus the supports of the remaining equations have two or three vertices and connect these \(c_2\) variables into exactly \(c\) components.

Consider one such connected component with \(v'\) variables.
Start with one vertex and repeatedly choose an equation meeting the reached set and at least one unreached vertex.
Such an equation exists until every vertex is reached, and adds at most two vertices.
The chosen equations are linearly independent: choose one newly reached variable for each equation; no earlier chosen equation contains that variable, giving a triangular minor with nonzero diagonal.
There are at least \(\lceil(v'-1)/2\rceil\) chosen equations.
The kernel on this component has dimension at most \(\lfloor(v'+1)/2\rfloor\).
Summing gives
\[
 \dim_k\ker\mathcal M_\alpha
 \le\left\lfloor(c_2+c)/2\right\rfloor
 \le c+Q,
\]
and (2)–(3) give the remaining bounds in (9).
If \(P=2\), then \(Q=0\), \(c=c_2=1\), and the connected double-edge equations leave exactly one scalar because \(v\) exists.

## Scope of the quantitative conclusion

The expansion statement concerns the subgroup \(H\) generated by the differences \(t_b^{-1}t_i\), with the generators and normalization in (7).
No expansion assumption on a larger ambient group is substituted for this one.
A positive \(h_*\) forces a positive progression density by (8).
For fixed left ratios, a sequence of such support configurations with \(P/N\to0\) gives Følner sets in \(H\), using (12) when the negative class occurs.
There are only three possible base choices; passing to one subsequence fixes the generating pair.
Thus the usual Følner criterion forces \(H\) to be amenable in this situation.
When \(H\) is amenable, \(h_*=0\) and this expansion argument supplies no positive density bound.
It still supplies (2)–(4), (9), and \(P\ge2\); it neither constructs an actual witness nor proves that sparse-progression configurations exist.

For a single ratio, if its path components have vertex lengths \(\ell\), then
\[
 P_i=\sum_{\text{paths}}\max(\ell-2,0),
 \qquad
 \#\{\text{length-}r\text{ progressions}\}
       =\sum_{\text{paths}}\max(\ell-r+1,0).
\]
Thus the three-term count records excess length beyond two.
The present bounds do not force a four-term progression or a specified longer chain: their numerical input does not distinguish many three-vertex paths from fewer longer paths.
This is a limitation of the count, not an assertion that an arbitrary collection of such paths is realizable by the actual group-product table.

For a zero product over a field with exact supports, singleton fibers are impossible because both coefficients in their sole representation are nonzero.
Hence all the combinatorial conclusions apply to the [A0002 contract](../tasks/Yin_T_A0002_v1.md#contract).
The rank conclusion additionally uses the given full-support coefficient witness and does not replace the original scalar zero-divisor question.

## Assessment history

### Decision progression-expansion

| Field | Value |
| --- | --- |
| date | 2026-11-21T05:07 |
| status | proved |
| reason | The independent inspection verifies the stated deductions and the applicability of the identified inputs at the recorded scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement-and-counts) | Exact progression counts, the expansion bound and the finite kernel dimension under the stated support hypothesis. |
| argument | [Proof](#the-local-degree-identity) | Local degrees, oriented cycles, the two signs and coset estimates, and the rank bound from connected components. |
| review | [Whole finding](../audits/reviews/Yin_R_A0134_v2.md#whole-finding) | Full inspection with its stated dependency and example limits. |
| dependency | [Qualitative progression](Yin_C_A0098_v1.md#decision-three-label-progression) | The previously verified exclusion of zero progressions, used within the stronger count. |

## Current assessment

[Selected decision](#decision-progression-expansion)

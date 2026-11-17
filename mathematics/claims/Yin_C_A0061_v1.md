---
author: Yin
---
# A lower bound for finite subgroup indices, perfect kernels and a nonsolvable color certificate

## Statement

Let \(P\) be a fixed finite group, with fixed surjective increments from the Ope26f rose group \(F\) to \(P\).
Use the [balanced matching law for \(P\)](Yin_C_A0044_v1.md#matching-within-the-prescribed-color-classes), or change the count of each full type in each planted color by \(O(1)\), uniformly in \(n\), preserving its original uncolored total and the exact equalities of matching-block sizes.
Take the independently uniform bijections within the resulting blocks and the corresponding sufficiently small fixed logarithmic girth constant.
Write \(G_n\) for the actual cone group and \(\pi:G_n\to P\) for the planted quotient.
For constants \(\kappa,c>0\) depending on the fixed planting data, conditional on girth the probability that \(H=\ker\pi\) has a proper subgroup of index at most \(\kappa n/\log n\) is at most \(e^{-cn}\) for large \(n\).
Normality of the subgroup is unnecessary.
Thus on this event of no small indices every map from \(G_n\) to a finite group of order at most \(\kappa n/\log n\) factors through \(\pi\).
Moreover, with probability tending to one conditional on girth, \(H\) is perfect.
In particular every homomorphism from \(G_n\) to any solvable group, including an infinite solvable group, factors through \(\pi\).
The result also applies to the original uncolored law \(P=1\), giving trivial integral abelianization with probability tending to one.

For the full [four-line coarse populations](Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings) there are connected, torsion-free realizations with the prescribed root separations and original binary zero product having these simultaneous properties:

1. The actual group surjects onto \(P=C_7\times A_5\) over the four-line character to \(C_7\).
2. The kernel of the character to \(C_7\) is itself perfect. Every further quotient over \(C_7\) with solvable kernel is therefore just \(C_7\). In particular no quotient over the character of order 21 exists.
3. The \(P\)-bin parities certify surviving original group labels in all three even colors of **each** factor, including left color 3. No collection of opposite-side basepoints or other group relations can pair all vertices in any of these six colors.

The general perfect-kernel statement applies to the indicated probability laws; it is not a claim about every matching with their type counts.
The second construction is exceptional in the original four-line law: applying the subgroup bound to its planted group \(C_7\) excludes the required quotient of its kernel onto \(A_5\) with exponentially high probability.
The survival certificate uses the prescribed nonsolvable quotient on these realizations. This does not settle erasure on every tuple without a \(C_{21}\) certificate.

## An entropy inequality independent of the marking alphabet

Put \(q=128,\ k=q+1,\ v=q^2+q+1,\ p=k/v,\ d=|P|\).
First use balanced weights within one fixed planted color on one side.
Give each vertex an additional marking in any finite alphabet, with overall proportions \(m_i\).
Equivalently one may use arbitrary marking probability vectors on each full type with the balanced type weights, without requiring integral counts.
Let \(z_{Li}\) be the marking proportion for the ordinary line \(L\), and \(u_{ti}\) the proportion conditional on carrying the ordinary point \(t\).
Lines are equally frequent and the point marginal equals \(p\), so \(\mathbb E_tu_{ti}=m_i\) and \(u_{ti}\le m_i/p\).
The incidence matrix of the plane has \(NN^{\mathsf T}=qI+\mathbf1\mathbf1^{\mathsf T}\), and \(u_{\cdot i}=N^{\mathsf T}z_{\cdot i}/k\).
Consequently
\[
  \mathbb E_t (u_{ti}-m_i)^2
     \le (q/k^2)m_i(1-m_i),\qquad
  \mathbb E_t [u_{ti}(1-u_{ti})]\ge(1-q/k^2)m_i(1-m_i).
\]
This is the [ordinary incidence calculation](Yin_C_A0040_v1.md#the-probability-of-a-cut) component by component.

If \(0<m_i\le p^2\), the bound \(u_{ti}\le m_i/p\) gives
\(\mathbb E_t[-u_{ti}\log u_{ti}]\ge\tfrac12 m_i\log(1/m_i)\).
If \(p^2\le m_i\le1\), use \(-u\log u\ge u(1-u)\).
The ratio \((1-x)/\log(1/x)=\int_0^1 x^s\,ds\) is increasing on \((0,1)\), and its limit at one is one.
As \((1-q/k^2)(1-p^2)/\log(1/p^2)>1/10\), summing the two bounds and omitting the zero coordinates gives
\[
                     \mathbb E_{t\ {\rm ordinary}} H(u_t)
                                   \ge \tfrac1{10} H(m).                 \tag{1}
\]
All entropies use natural logarithms.
The constant is independent of the number and sizes of the marking classes.

## Vertex markings from small-index subgroups

The connected \(P\)-cover of the rose has directed edges \(z\to z\eta(t)\) for each generator \(t\), with inverse readings allowed.
If \(H\) has a subgroup of index \(m\ge2\), its action by right multiplication on the set of right cosets of that subgroup is transitive on \(m\) points.
Pull this action back along the surjection \(\ker(F\to P)\to H\).
It is represented on the planted rose cover by bijections \(\sigma_{t,z}\) of these \(m\) points on the directed edges, with inverse bijections on reverse readings.
Indeed, choose a spanning tree, put identity permutations on it, and use on every non-tree edge the right action of its based fundamental cycle.
Following a path then composes the successive edge bijections in traversal order.
There is no choice of an additional mark \(j(z)\) for each planted color satisfying \(j(z\eta(t))=\sigma_{t,z}(j(z))\) on every edge.
Such a section would give a point over the base vertex fixed by every closed path in the cover, contradicting transitivity on more than one point.

On the first matching graph there does exist an additional vertex marking \(f\) satisfying
\[
                           f(x^t)=\sigma_{t,z}(f(x))                    \tag{2}
\]
whenever \(x\) has planted color \(z\) and carries \(t\).
Indeed any closed graph walk lifts to a loop in the rose cover at its starting color.
After connecting its start to the base vertex by a tree path, this relator is killed in \(H\), since it is a conjugate of a defining cone relation.
Thus its permutation is the identity.
Choose an initial mark in each matching component and transport it along paths, giving \(f\) independently of path choice.
The first graph alone supplies this necessary condition.

Fix an assignment of edge bijections and the marking distributions \(w_{\tau,z}\) on each nonempty full type \(\tau\) and planted color \(z\) on this first side.
These determine the overall distribution \(m_z\) in that color and the two matching-end distributions, denoted by \(u_{t,z}\) at the source.
Their compatibility requires that the distribution on the reverse block is the image of the forward one under \(\sigma_{t,z}\).
Given compatible histograms, multiply the multinomial counts of vertex markings by the probability that every bijection matches the specified markings.
For one block of size \(N_{t,z}\) the latter factor is \(\prod_i(N_{t,z}u_{t,z}(i))!/N_{t,z}!\).
Let \(n_{\tau,z}\) be the type-and-color counts. As in the [fixed-target argument](Yin_C_A0044_v1.md#connectedness-and-factorization-through-the-finite-quotient), the expected number of compatible markings with those histograms is bounded by
\[
    \exp\{n(A-B)+O(m\log(n+1))\},\quad
    A=\sum_{\tau,z}\frac{n_{\tau,z}}n H(w_{\tau,z}),\quad
    B=\frac12\sum_{t\ {\rm signed},z}\frac{N_{t,z}}nH(u_{t,z}).         \tag{3}
\]
The half sum uses exact equality of the entropies at the two ends of each matching.
There are a fixed number of original types, letters and planted colors and at most \(m\) numerator factorials per block or denominator factorials per fine type.
The bound \(\log j!=j\log j-j+O(\log(n+1))\) for \(0\le j\le n\) therefore gives the displayed uniform error.

For balanced weights, concavity bounds \(A\) by \(d^{-1}\sum_zH(m_z)\).
Discarding the extra labels in \(B\) and applying (1) gives \(B\ge (k/(20d))\sum_z H(m_z)\).
These bounds hold up to an additive \(o(1)\) for the actual bounded perturbations, uniformly for \(2\le m\le n\).
To check this, keep the marking distributions on each full type and replace the type weights at each planted color by their balanced limits.
The resulting overall and letter-conditional distributions of the marks differ from the actual ones by \(O(1/n)\) in total variation, uniformly even if many marks occur.
Indeed they are mixtures of the same finitely many distributions with normalized weights differing by that amount, and every letter-and-color block has linear size.
Entropies of two distributions on \(m\) symbols at total variation \(s\) differ by at most \(h(s)+s\log m\), where \(h\) is binary entropy, by coupling them to disagree with probability \(s\) and conditioning on the disagreement indicator.
Frequency-weight errors multiply entropies at most \(\log m\).
Thus, also for the true weights,
\[
      A-B\le -(k/20-1)d^{-1}\sum_z H(m_z)+o(1) .                       \tag{4}
\]

For permutations admitting no section, choose a modal mark \(j(z)\) in each planted color.
At least one block violates \(j(z\eta(t))=\sigma_{t,z}(j(z))\), so every edge of that block has a nonmodal endpoint.
Its size is \(np/d+O(1)\) and every vertex is used at most twice there, including when the two planted colors agree.
There are therefore at least \(np/(2d)-O(1)\) nonmodal vertices over all planted colors.
Because \(H(m_z)\ge1-\max_i m_z(i)\) and the true planted-color weights are \(1/d+O(1/n)\), the mean entropy in (4) is at least \(p/(3d)\) for sufficiently large \(n\).
This yields \(A-B\le-\gamma\) for some \(\gamma>0\) independently of \(m\le n\) and the assignment for all large \(n\).

There are at most \((n+1)^{dT_0m}\) histograms on a side with \(T_0\) full types, and at most \((m!)^{8258d}\) assignments of permutations, even allowing arbitrary permutations on the spanning-tree edges.
For \(m\le n\), their logarithms and the error in (3) are together at most \(C_0m\log(n+1)\) for a fixed \(C_0\).
Take \(\kappa>0\) small enough that \(C_0m\log(n+1)\le\gamma n/2\) whenever \(m\le\kappa n/\log n\) for all large \(n\).
Summing over the fewer than \(n\) possible degrees leaves an unconditioned failure probability \(\exp(-\Omega(n))\).
This union bound covers all permutation representations arising from index-\(m\) subgroups, all their possible vertex markings and all the specified indices simultaneously.
The same exponential bound holds after girth conditioning because its probability is at least \(\exp(-o(n))\); for bounded perturbations use the [within-block switching argument](Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts) with block sizes \(np/d+O(1)\).

## From bounded-length relators to perfection

Put \(r=1+d(8258-1)\), the first Betti number of the connected planted rose cover.
With conditional probability \(1-o(1)\), all source graph components have diameter at most \(D\log n\) for a fixed \(D\).
The [finite-planting diameter proof](Yin_C_A0044_v1.md#girth-conditioning-and-bounded-patterns) uses the uniform \(np/d+O(1)\) block sizes and unchanged degrees, so the same small-set expansion estimate applies after the bounded perturbation.
Choose in each component a breadth-first tree.
The closed words of the non-tree edges based by this tree, of lengths at most \(2D\log n+1\), normally generate the cone relations.
For the cover presenting \(H\), attach each of these words at every starting color of \(P\).
Every lift closes because the word has trivial planted increment; including every starting color accounts for all conjugates on passing from \(F\) to the kernel of \(F\to P\).
This presents the abelianization \(H_{\rm ab}\) as \(\mathbb Z^r\) modulo the subgroup generated by the signed edge counts of these lifted walks on the non-tree edges of a fixed tree in the planted rose cover.
Paths in that tree used to base the lifted loops contribute zero. [Cover calculation in binary coefficients](Yin_C_A0047_v1.md#a-finite-test-for-complete-erasure-of-a-color)

Now use the small-index conclusion on the diameter event.
It excludes a mod-two character and hence the relation vectors span \(\mathbb F_2^r\).
Choose \(r\) of them with odd determinant.
Every chosen vector has \(\ell^1\)-norm at most \(2D\log n+1\), and hence its Euclidean norm satisfies the same bound.
Hadamard's inequality implies that the positive index of their lattice is at most \((C\log n)^r\), with \(C>2D+2\) fixed.
The index of the full relation lattice divides that index.
If \(H_{\rm ab}\) were nontrivial, it would therefore have a quotient of some prime order at most \((C\log n)^r\).
Since \(r\) is fixed, this is smaller than \(\kappa n/\log n\) for sufficiently large \(n\), contrary to the subgroup bound.
This proves \(H_{\rm ab}=0\) with conditional probability tending to one.
A homomorphic image of a perfect group is perfect, and a solvable group has no nontrivial perfect subgroup, giving the asserted factorization.

## A refinement that distinguishes all six colors using a perfect kernel

For the four-line data take \(P=C_7\times A_5\), with \(d=420\), and \(n\) a sufficiently large multiple of \(2dv^2\).
Use three even permutations \(s_1=(1\,2\,3),s_2=(1\,2\,4),s_3=(1\,2\,5)\).
They generate \(A_5\): successively adjoining \((1\,2\,j)\) to the alternating group on \(j-1\) letters gives a transitive subgroup on \(j\) letters with a point stabilizer containing the old group, hence the full alternating group, starting from \(j=3\).
Keep the coarse increments on the four-line ordinary intersection arrows and make every ordinary–ordinary increment trivial in the second coordinate.
On the three mixed extra–ordinary pairs give the chosen orientations increments \((0,s_1),(0,s_2),(0,s_3)\), with inverses in reverse.
These increments generate \(P\).

Start by splitting each original full type equally among the \(d\) fine colors, which is integral at these sizes.
For each of the four selected empty-extra line types \(i\in D_0=\{0,1,2,4\}\), add the following bounded changes to the counts of \((c,h)\) on both sides, where \(f_i(c)=7\mathbf1_{\{c=i\}}-1\):
\[
 \begin{array}{c|c}
 h & \text{change}\\ \hline
 1 & f_i(c)-\mathbf1_{\{c=i+1\}}-\mathbf1_{\{c=i+2\}}\\
 s_1 & \mathbf1_{\{c=i+1\}}\\
 s_2 & \mathbf1_{\{c=i+2\}}\\
 \text{all other }h & 0 .
 \end{array}
\]
The coarse sums are the prescribed \(f_i(c)\), and the total for each full type is unchanged.
Intersection-arrow changes match in each sheet by their dependence only on \(c-i\).
Private ordinary points of a selected line are paired within that line.
Both ends of each mixed pair are unmodified: the ordinary partners are outside all selected lines and no changed type contains extras.
Thus right multiplication by the indicated increment matches equally sized blocks, also for the noncommuting \(A_5\) generators, and the cone group surjects onto \(P\).

Choose roots of fine color \((0,1)\).
The balanced fine count \(n/d\) is even.
On the \(s_1\)-sheet the odd forward colors are \(D_0+1=\{1,2,3,5\}\), and on the \(s_2\)-sheet they are \(D_0+2=\{2,3,4,6\}\).
Thus every even coarse color \(3,5,6\) has an odd refined bin on either forward side.
In particular the two \(s_1,s_2\) bins over forward color 3 each have exactly \(n/420+1\) occurrences, whereas its identity bin has \(n/420-6\).
Inverting the second factor sends \((c,h)\) to \((-c,h^{-1})\) bijectively.
Parity in each fine bin is unchanged on collecting equal original group elements.
Connectedness and the source safeguards hold with conditional probability \(1-o(1)\): the fixed finite-\(P\) [bounded-pattern comparison](Yin_C_A0044_v1.md#girth-conditioning-and-bounded-patterns) uses block sizes of order \(n\) and a bounded whole-chain color factor, and each positive refined turn estimate changes multiplicatively by at most \(1+O(1/n)\) as in the [bounded-perturbation proof](Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts).
Forbidden turns remain absent, the diameter estimate above applies, and the balanced limiting cut exponent retains its strict gap on macroscopic cuts since all increments generate \(P\).
These arguments use fixed \(P\) and a girth constant satisfying \(c\log(2d|T|/p)<1\) and \(2c\log132<1\).
Consequently connected, root-separated torsion-free realizations with the two original nonzero binary zero divisors and these exact refined counts exist.

On the simultaneous perfect-kernel event, let \(K=\ker(G_n\to C_7)\).
There is an exact sequence \(1\to H\to K\to A_5\to1\).
Since \(H\) and \(A_5\) are perfect, \(H=[H,H]\subseteq[K,K]\) and \([K,K]\) maps onto \(A_5\), giving \(K=[K,K]\).
Any solvable image of \(K\) is therefore trivial.
In particular any larger quotient over the specified \(C_7\) with a solvable kernel would restrict to a nontrivial solvable image of \(K\), which is impossible.
This proves the simultaneous obstruction on this exceptional family without relying on a \(C_{21}\) quotient, an exhaustive list of candidate loop words, or a limitation on the number of basepoints.

## Assessment history

### Decision small-indices-and-perfect-kernels

| Field | Value |
| --- | --- |
| date | 2026-11-17T10:53 |
| status | proved |
| reason | Independent review verified the growing-index estimate, the integral perfection argument and the nonsolvable quotient that certifies six surviving colors. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Absence of small-index subgroups with the stated probability, perfection of the planted kernel, and the four-line realization over \(C_7\times A_5\). |
| argument | [Proof](#an-entropy-inequality-independent-of-the-marking-alphabet) | Uniform entropy, coset actions, bounded-length relations and the actual labels in the nonsolvable quotient. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0097_v1.md#whole-argument-finding) | Independent review of the probability bounds, the two perfect kernels and the six odd refined bins. |

## Current assessment

[Selected decision](#decision-small-indices-and-perfect-kernels)

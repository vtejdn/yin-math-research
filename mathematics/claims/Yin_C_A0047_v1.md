---
author: Yin
---
# Common-label return probabilities and homology tests for a surviving quotient class

## Statement

Use the two finite immersed graphs in Ope26f, their cone group \(G\), and the root factors with vertex labels \(g_x\) and \(h_y^{-1}\) as in [the source, §1](../literature/pdf/Ope26f.pdf#page=2).
The graphs and all their matchings are fixed in the first two assertions.

1. There is a symmetric lazy walk on the pairs of vertices in the two root components whose limiting transition probabilities give the exact partition into simultaneous-step components.
   For a connected tuple with the prescribed type counts and girth at least three, more than \(99.1\%\) of all \(n^2\) pair occurrences lie in components consisting of one edge and its two endpoints.
   Each such edge gives a specific equality of group products, although other components may have the same group product.
2. Suppose an actual quotient \(\eta:G\to C_7\) is given and put \(K=\ker\eta\), \(V=K/([K,K]K^2)\), regarded as an \(\mathbb F_2\)-vector space.
   From the finite matching tuple one can compute the exact partition of the occurrences over each quotient class by their labels in \(E=G/([K,K]K^2)\), using binary linear algebra.
   The number of odd bins gives a certified lower bound on the number of original group labels surviving binary collection in that class.
   A real character-sum estimate and one-sided random tests below can certify that an even occurrence class is not completely erased.
3. In the balanced planted \(C_7\) matching law, with probability \(1-\exp(-c n)\) for some \(c>0\) and all large admissible \(n\) after girth conditioning, \(V=0\).
   Consequently \(K\) has **no nontrivial finite \(2\)-group quotient of any order** on this event.
   In particular there is no new quotient of \(G\) over the prescribed \(C_7\) whose kernel over \(C_7\) is a nontrivial finite \(2\)-group.
   These conclusions continue to hold with probability tending to one on the [torsion-free planted realizations](Yin_C_A0044_v1.md#statement).

The second test concerns actual original labels, with a one-sided conclusion on survival.
The third assertion explains a limitation of *all* relative \(2\)-group refinements for one class of source-type graphs even though their true support histograms are large.

## The fixed-graph walk

At a pair \((x,y)\), stay put with probability \(1/2\).
Otherwise choose one signed letter uniformly from the source alphabet \(T\).
Follow it on both graphs if it is available at both vertices, and stay put if it is unavailable on either side.
Every edge step has a reverse step with the same probability by the inverse-letter matching.
Thus the transition matrix \(P\) is symmetric with uniform stationary measure, and every common step has positive probability.
Laziness places the spectrum in \([0,1]\).
The Dirichlet form of \(I-P\) is a positive weighted sum of squared differences across the common edges.
Its kernel consists exactly of functions constant on each connected component of the simultaneous-step graph.
Writing \(D(u)\) for the component of a pair occurrence \(u\), finite-dimensional spectral calculus gives
\[
              \lim_{k\to\infty}P^k(u,v)
                 =\frac{\mathbf 1_{\{v\in D(u)\}}}{|D(u)|},
       \qquad
              \lim_{k\to\infty}\operatorname{Tr}(P^k)
                 =\#\{\text{simultaneous-step components}\}.
\]
The trace here is the ordinary unnormalized trace on the finite pair space.
Every move preserves \(g_xh_y^{-1}\) by the ordered group identity \((g_xt)(h_yt)^{-1}=g_xh_y^{-1}\).
Conditional on the fixed matchings, the trajectory stays within one *known* product fiber, but its limiting uniform law is on the component it can reach.
The source's parity argument counts each whole component with its even cardinality and permits further mergers of components in the actual group.
Averaging the transition probabilities over new matching tuples also changes the cone group and does not test equality for the original tuple.

For the quantitative assertion choose \(x,y\) independently and uniformly on their connected sides.
This random choice of a start uses only the deterministic vertex-type counts in [Ope26f, §2.1](../literature/pdf/Ope26f.pdf#page=4).
Put \(v_0=16513\), \(\rho=129/v_0\), and let \(d\) be the number of common outgoing labels.
The two ordinary lines meet in one point except when they coincide, when they meet in 129 points.
The extras contribute two precisely when the first side has a pair of extras and the second side has all three.
Hence
\[
 d=1+128\,\mathbf1_{\{\text{same line}\}}
      +2\,\mathbf1_{\{\text{both extra sets nonempty}\}},\quad
 \mathbb E(d-1)=128/v_0+3\rho^2,\quad
 \Pr(d>1)\le 1/v_0+3\rho^2/2.
\]
Indeed the line coincidence probability is \(1/v_0\) and the two relevant extra-set frequencies are \(3\rho/2\) and \(\rho\).
In a loop-free graph of minimum degree one, any degree-one vertex outside an isolated two-vertex edge has a neighbor of degree greater than one.
The number of such degree-one vertices is bounded by the sum of degrees of all the higher-degree vertices.
The source girth assumption ensures the common graph has no loops or parallel edges.
Thus the fraction outside isolated edges is at most
\[
  \Pr(d>1)+\mathbb E[d\,\mathbf1_{\{d>1\}}]
       \le 130/v_0+6\rho^2 <0.00824 .
\]
In particular the fixed-graph limiting mean return probability is greater than \(0.9917/2\).
In the [high-probability connected source law](Yin_C_A0040_v1.md#distinct-labels-away-from-the-roots), an additional \(o(n^2)\) pair occurrences in probability suffice to remove the pairs meeting an ambiguous factor vertex and their mates on isolated edges.
The remaining certified edges pair distinct pairs of surviving group labels.

## A finite test for complete erasure of a color

For \(c\in C_7\) choose a fixed word for a representative \(s(c)\in G\) with \(\eta(s(c))=c\).
For each vertex occurrence on one side let \(g\) denote its *factor* label, using the inverse path label on the second side.
In class \(c\), record the vector \(v(g)=[s(c)^{-1}g]\in V\).
Two such labels have the same image in \(E\) exactly when their vectors agree.
A different common representative merely translates all these vectors.

The vector space and the recorded vectors are computable without solving the word problem in \(G\).
Use a spanning forest of both graphs to obtain all the fundamental closed-walk relator words for the cone group, including components outside the two root components.
Start with the rose cover having vertices \(C_7\) and edges \(c\to c+\eta(t)\) for each positive generator \(t\), with inverse traversal allowed.
Attach each relator at each possible starting color and record the edge vector of its closed lift modulo two.
If \(\partial_1\) is the vertex-edge boundary, then
\[
                V=\ker\partial_1\big/\langle
                  \text{edge vectors of all lifted relators}\rangle .
\]
To see the formula, collapse a spanning tree of the rose cover. Its non-tree edges freely generate the subgroup of the rose group with zero total color.
The lifts of all relators normally generate the extra relations for \(K\), because conjugations in the original free group are represented by first reaching one of the seven starting colors and then using kernel conjugation.
After abelianizing and reducing modulo two, these become exactly the displayed edge vectors in the cycle space.
The loop labeled \(s(c)^{-1}g\) based at the identity color gives the requested vector in this computation.
This construction in particular gives \(V\) finite dimension.
It also gives a two-sided test for an *entire* occurrence fiber.
For a pair \(u=(x,y)\) compute its simultaneous-step component \(D(u)\) and the set \(F_E(u)\) of all pairs with the same product image in \(E\).
The latter comparison only involves zero-color difference words when the coarse \(C_7\) products agree, so the same loop-vector calculation suffices.
Then \(D(u)\subseteq F_G(u)\subseteq F_E(u)\) for the actual occurrence fiber \(F_G(u)\).
If the two computable sets agree, they certify the whole fiber in the original group.
In particular, if both have size two and the two row labels have distinct images in \(E\), the two pairs also give distinct actual pairs of group labels.
Neither row label nor either column label of these two pairs can have an additional occurrence: keeping its partner fixed would produce a third occurrence in that same fiber.
The certified pair is therefore a complete double fiber on the collected supports as well.

Fix one class with \(N\) vertex occurrences on one side and let \(m_v\) count the occurrences with recorded vector \(v\).
The odd bins of the finite quotient give at least \(s=\#\{v:m_v\text{ odd}\}\) surviving group labels in this class: an odd bin contains an original group label of odd multiplicity, and different bins cannot use the same original label.
The sum \(\sum_v(m_v\bmod2)\,v\) is a quick sufficient certificate when nonzero, but it can vanish with \(s>0\).
There is also a sharp lower bound using a real second moment.
For uniform \(\lambda\in V^*=\operatorname{Hom}(V,\mathbb F_2)\), put
\[
             Z(\lambda)=\sum_{\text{occurrences }g:\eta(g)=c}
                                (-1)^{\lambda(v(g))}.
\]
Orthogonality of the binary characters and the elementary integer inequality \(j^2\ge 2j-\mathbf1_{\{j\ {\rm odd}\}}\) yield
\[
             \mathbb E_\lambda |Z(\lambda)|^2=\sum_v m_v^2,\qquad
             s\ge 2N-\mathbb E_\lambda |Z(\lambda)|^2 .
\]
This expectation is over test characters of the fixed quotient kernel, not over matching tuples or common-step trajectories.
For an exact one-sided random certificate, select \(r\) independent uniform forms and bin by their \(r\)-bit outputs.
An odd output bin proves original survival on every realization of the forms.
If \(s>0\), a chosen odd vector collides with any of the other \(s-1\) odd vectors with probability at most \((s-1)2^{-r}\), since a form vanishes on their nonzero difference with probability \(1/2\).
Even-multiplicity bins cannot affect this parity.
Thus \(r\ge\lceil\log_2(2N)\rceil\) gives detection probability at least \(1/2\) when \(N>0\) and the full vector test detects survival.
Failure of the test need not establish erasure in \(G\).

For example, take \(\mathbb Z^2\to C_7\) by reducing the first coordinate modulo seven.
The four labels \(0,(7,0),(0,1),(7,1)\) in the identity class have distinct vectors filling \(V=\mathbb F_2^2\).
Their vector sum is zero and every single binary linear functional has only even bins.
The exact character-sum moment is four, certifying all four survivors.
This illustrates the test on actual group labels independently of any assertion that these are the unknown matching labels.
In the [four-class exception for the collected source supports](Yin_C_A0043_v1.md#passing-from-vertices-to-the-two-actual-supports), a single certified survivor outside the four odd colors on either side rules out that exception.

## Why every relative two-group refinement can disappear

Conjugation makes \(V\) an \(\mathbb F_2[C_7]\)-module: the action of \(K\) on its own mod-two abelianization is trivial.
Assume \(V\ne0\) and choose an irreducible quotient module \(W\).
The factorization of \(X^7-1\) over \(\mathbb F_2\) into one linear and two irreducible cubic factors shows that \(W\) is one-dimensional trivial, or is the additive \(\mathbb F_8\) with the generator acting by a primitive seventh root.
This follows directly by considering \(W\) as a simple module over the cyclic polynomial quotient in the [seven-class calculation](Yin_C_A0042_v1.md#separating-the-cubic-factors).
The kernel of \(V\to W\) is normal in \(E\), and dividing by it gives a surjection from \(G\) to an extension of \(C_7\) with kernel \(W\).
This extension splits: if \(t\) lifts a generator, \(t^7\in W\) and \(t^{14}=1\), so \(t^8\) is a lift of the same generator of order seven.
The quotient is therefore \(C_{14}\) in the trivial case, or the group of affine permutations \(z\mapsto uz+b\) of \(\mathbb F_8\) in the cubic case.
Both primitive-root actions generate the full multiplicative group of order seven and give the same abstract affine target.
The resulting map is nontrivial on \(K\), so it does not factor through the given map to \(C_7\).

Apply [the planted finite-target estimate](Yin_C_A0044_v1.md#connectedness-and-factorization-through-the-finite-quotient) to the fixed list consisting of \(C_{14}\) and \(\operatorname{AGL}(1,8)\).
It excludes such a nonfactoring map with exponentially high probability in the planted girth-conditioned law.
This proves the asserted simultaneous conclusion \(V=0\).
Any nontrivial finite \(2\)-group has a quotient of order two, so the existence of a nontrivial finite \(2\)-group quotient of \(K\) would force \(V\ne0\).
Any surjective refinement of \(G\to C_7\) by a nontrivial finite \(2\)-group kernel would in turn restrict to such a quotient of \(K\).
No increasing list of target orders or uniform probability estimate over that list is needed.

The [balanced construction](Yin_C_A0044_v1.md#the-histogram-after-collecting-actual-group-labels) has even positive class counts before and after collection with high probability.
On its simultaneous event \(V=0\), every bin test above sees just the already even class parity, although \(n/7-o(n)\) actual group labels in each class survive.
The separation provided by the walk, by a finite quotient, and by a rooted diagram estimate thus has different observable consequences on the same law.

## Assessment history

### Decision walk-and-kernel-homology

| Field | Value |
| --- | --- |
| date | 2026-11-17T08:44 |
| status | proved |
| reason | The review checked the walk, the finite linear test and the passage from elementary abelian to arbitrary finite two-groups. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Common-step limits, detection of a surviving color and the lack of relative two-group quotients in the balanced model. |
| argument | [Proof](#the-fixed-graph-walk) | Complete argument under the stated hypotheses. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0078_v1.md#whole-argument-finding) | Review of the entire argument with its stated dependencies. |

## Current assessment

[Selected decision](#decision-walk-and-kernel-homology)

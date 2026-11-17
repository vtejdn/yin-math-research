---
author: Yin
---
# Exact counts in the cross-side simultaneous-step forest

Take the two sides of an Ope26f tuple whose graphs are connected, have the prescribed types, and admit no reduced spherical arrangement with only ordinary boundaries.
Let \(\mathcal D\) be the simultaneous-step graph on all \(n^2\) pairs, and let \(P\) be the [fixed-graph lazy walk](../claims/Yin_C_A0047_v1.md#the-fixed-graph-walk).
The true product fibers on occurrences can still merge components of \(\mathcal D\).
Their merger count has an exact expression in terms of the excess of the true fiber sizes above two.

## Forest and return probability

The ordinary two-disk argument of [C_A0045](../claims/Yin_C_A0045_v1.md#synchronous-components-and-protected-vertices) applies to this cross-side graph as well.
Indeed any nonempty cyclically reduced closed walk in \(\mathcal D\) projects in both coordinates to cyclically immersed closed paths reading the same word.
Immediate inverse readings would backtrack in the pair graph by immersion.
Read one projected path forwards on its disk, the other backwards on another disk, and join corresponding occurrences by disjoint arcs across the annulus.
Each paired occurrence belongs to a different graph side and therefore uses a different underlying edge.
This would be an ordinary reduced arrangement under [Ope26f, Definition 4.1](../literature/pdf/Ope26f.pdf#page=14).
Thus \(\mathcal D\) is a forest.

For each signed letter the number of pairs admitting that step is \((n\rho)^2\), where \(\rho=129/v,\ v=16513\).
Every undirected edge is counted twice, so with \(|T|=v+3\) the component count is
\[
     b=n^2-\tfrac12 |T|(n\rho)^2
       =\tfrac{n^2}{2}(1-\delta),\qquad
     \delta=128/v+3\rho^2 .
\]
Here \(v\rho^2=129^2/v=1+128/v\).
Consequently the mean return probability of the walk, averaged over a uniform start after the tuple is fixed, has the exact limit
\[
                    \lim_{k\to\infty}n^{-2}\operatorname{Tr}(P^k)
                          =\tfrac12(1-\delta).
\]
The estimate in C_A0047 gives more than \(99.17\%\) of pair occurrences on isolated edges, but their individual walk return limits do not identify equality of group products across different components.

## Mergers and true support cells

Write \(f_{\rm occ}\) for the number of distinct group products among all vertex-pair occurrences, and \(N_g\) for the multiplicity at an occurring product \(g\).
Since the product is constant on every component, \(b-f_{\rm occ}\) counts the decrease in the number of classes on passing from component to product equality.
Exactly
\[
             \sum_{g:N_g>0}(N_g-2)=\delta n^2+2(b-f_{\rm occ}).
\]
This identifies how much of the excess above two is already forced by the graph and how much comes from identifying different components.
In particular the limiting common-walk trace alone supplies only the first term and the value of \(b\).

Now first collect each original factor over \(\mathbb F_2\) and count ordered pairs of its surviving support elements.
Let \(M\) be the size of this rectangle, \(f\) its number of distinct group products, and \(m_g\) the multiplicities of those products.
Every \(m_g\) is even by the source zero product, and \(f\le f_{\rm occ}\le b\) since all surviving pairs have occurrence representatives.
It follows that
\[
     \sum_{g:m_g\ge4}m_g
       \ \ge\ \sum_{g:m_g>0}(m_g-2)
       \ =\ M-2f\ \ge\ \delta n^2-(n^2-M).
\]
The [support estimate](../claims/Yin_C_A0040_v1.md#distinct-labels-away-from-the-roots) gives \(M=n^2-o(n^2)\) in probability on the connected source realizations.
Thus at least \((\delta-o(1))n^2\) cells of the *collected* rectangle belong to true group-product fibers of size at least four, with \(\delta>0.0079\).
This lower bound controls a number of cells, allowing them to be concentrated in fewer large fibers.
It uses no estimate on the number of mergers and no separation theorem for paths rooted at both coordinates of a pair.

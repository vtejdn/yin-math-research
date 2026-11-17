---
author: Yin
---
# Linear fillings and complex operator ranks in the matching groups

Let \(F\) denote the free group on the rose generators in [Ope26f](../literature/pdf/Ope26f.pdf#page=4), let \(G_n\) be the quotient obtained by coning all components of the two labelled graphs, and let \(L=\lfloor c\log n\rfloor\) be the girth threshold for the law in question.
Under the original law, the [balanced seven-color law](Yin_L_A0047_v1.md#the-bounded-pattern-estimate-with-the-seven-colors), and the [four-line law](../claims/Yin_C_A0051_v1.md#geometric-safeguards-under-the-change-of-counts), all probabilities below are conditional on the stated girth event and \(n\) runs through the admissible sizes for that law.
There is a constant \(c_*>0\), independent of \(n\), such that with probability tending to one, simultaneously:

1. Every nonempty cyclically reduced rose word \(W\) trivial in \(G_n\) admits a cone-disk filling of total inner boundary length at most \(|W|/c_*\).
   In particular \(|W|\ge c_* L\), and \(G_n\) is torsion-free and word-hyperbolic.
2. For every finite matrix over \(\mathbb C G_n\) whose regular operator has closed range, its von Neumann kernel dimension (ordinary, unnormalized matrix trace) is an integer.
   Every nonzero scalar over \(\mathbb C G_n\) with closed regular range is injective.

On any sequence of these good realizations, for every fixed finite rectangular matrix \(A\) over \(\mathbb CF\), the regular ranks of its images converge from at most the free-group rank to that rank.
In particular, at every fixed rose radius, the supremum of the kernel dimensions of nonzero scalar polynomials supported in the ball tends to zero, uniformly over all their complex coefficients.
Over every field, a nonzero zero product with one factor in the rose ball of radius \(R\) and the other supported on \(s\) elements anywhere must satisfy \(2Rs\ge c_*L\).
These are statements about the actual quotient groups, including the four-line groups with their two nonzero characteristic-two factors.

## The geometric input and its application to the planted laws

[Mghirbi–Douglas, arXiv:2611.04599v1, Definition 3.3 and Theorem B](https://arxiv.org/html/2611.04599v1#S3.SS2) give a deterministic criterion for a finite immersed graph to have a torsion-free word-hyperbolic cone group.
The inspected [November 2026 preprint](../literature/pdf/MD26.pdf#page=13) distinguishes capped pictures for words from pictures protecting designated roots in Section 4.
The free outer disk and the quantitative filling bound are their results.
Their [Corollary 5.3](https://arxiv.org/html/2611.04599v1#S5) already gives the original characteristic-two zero-divisor application.
Here is why the same result applies to the two planted laws, including the prescribed four-line parity patterns.

Their (P1) requires degree at least five and girth at least \(L\ge 3\).
The matching graphs have degree at least 129 and the girth is conditioned.
For (P2) the diameter bound \(dL\) holds with conditional probability \(1-o(1)\) in both linked planted arguments, and \(\log_2(2n)\le\lambda L\) for all large \(n\) with \(\lambda=1+2/(c\log 2)\).
For (P3), the rooted bounded-pattern estimates in those same arguments choose \(\epsilon\in(0,1]\) before the three finite pattern bounds.
Apply them once, at the triple in equation (2) of Definition 3.3 calculated from \(\epsilon,d,\lambda\), using the designated roots of the graphs.
Their path systems, distinct-edge comparisons, interval conventions and allowed rooted break are those of [Ope26f, Proposition 3.1](../literature/pdf/Ope26f.pdf#page=7).
For the original law this verification is already Mghirbi–Douglas, Lemma 3.5.
Thus pattern-freeness and the respective original or planted conclusions hold simultaneously with conditional probability \(1-o(1)\).

For a nonempty cyclically reduced null word \(W\), a reduced cone picture with free outer word exists by their Lemmas 4.2 and 4.3.
It has at least one nonempty cyclically immersed inner graph boundary, so its total inner length \(H_0\) is at least \(L\).
Their [Proposition 4.4 and proof of Theorem B](https://arxiv.org/html/2611.04599v1#S4.SS3) give
\[
                   L\le H_0\le\frac{16}{13\epsilon}|W|,
       \qquad \operatorname{Area}(W)\le H_0 .
\]
The area is for the finite rose presentation with the fundamental loops of spanning trees of the graph components.
Consequently \(c_*=13\epsilon/16\) works for the marked systole, and the map \(F\to G_n\) is injective on every word ball of radius strictly less than \(c_*L/2\).
No uniform hyperbolicity constant in the individual Cayley graphs is used.
Given an actual good tuple with a supplied effective upper bound for \(16/(13\epsilon)\), word equality is decidable by finite search: for the difference word enumerate planar van Kampen diagrams up to the resulting area bound.
If the outer length is \(h\), at most \(A\) faces are needed and each relator has length at most the computable maximum \(m\).
Even boundary bridges are counted twice, so there are at most \((h+mA)/2\) edges in such a diagram.
This is a finite certificate search, without a practical size estimate.
An existence or high-probability assertion by itself does not supply a tuple.

## From hyperbolicity to integral traces

[Lafforgue's Baum–Connes theorem for hyperbolic groups](https://ems.press/journals/jncg/articles/3925) gives surjectivity of reduced assembly with trivial coefficients.
The specialization to the word metric of a hyperbolic group follows [Theorem 0.4 on printed pages 3–4](../literature/pdf/Laf12.pdf#page=3).
By [BCM04, Theorem 6.3](../audits/literature/BCM04/Yin_U001.md#assembly-trace), the canonical trace on its image is integer-valued for a countable torsion-free group.
Therefore every matrix projection over \(C_r^*(G_n)\) has integral unnormalized trace.
For a closed-range matrix \(A\), the spectrum of \(A^*A\) off zero is bounded away from zero, so continuous functional calculus places its kernel projection in the corresponding matrix algebra over \(C_r^*(G_n)\).
For a nonzero scalar its kernel projection cannot be the identity.
Positivity, integrality and faithfulness of the trace make that projection zero.
Thus a fractional kernel dimension on these groups requires nonzero spectrum accumulating at zero and a kernel projection lying outside the reduced group \(C^*\)-algebra.

## The rank seen by a fixed matrix

Let \(A\in M_{p,q}(\mathbb CF)\), with entries supported in the word ball of radius \(R\), and let \(A_n\) be its image.
Choose \(M>0\) bounding \(\|A\|\) and every \(\|A_n\|\), for instance one plus the sum of the absolute values of all matrix coefficients.
Put \(h_k(t)=1-(1-t/M^2)^k\) on \([0,M^2]\).
These polynomials increase there to \(\mathbf1_{(0,\infty)}\).
If \(2kR<c_*L\), the unnormalized traces of \(h_k(A_n^*A_n)\) and \(h_k(A^*A)\) agree: all word monomials have length at most \(2kR\), and no nontrivial reduced word of that length is killed (cyclically reduce a conjugate if necessary).
The quotient rank is at least this common trace.
For each fixed \(k\) equality of these two polynomial traces holds eventually, and monotone convergence as \(k\to\infty\) gives the free rank as a lower bound for the limit inferior of the quotient ranks.

For the opposite inequality let \(r\) be the inner rank of \(A\) over \(\mathbb CF\), the least middle size of a factorization into two matrices over that ring.
It equals the rank over the universal field of fractions because the free group algebra is a semifir ([Lew74, §II, p. 340](../literature/pdf/Lew74.pdf#page=2) and [Coh06, Theorem 7.5.13(f) and Corollary 7.5.14](../literature/pdf/Coh06.pdf#page=474)).
[Lin93, p. 573](../audits/literature/Lin93/Yin_U001.md#hughes-lewin-and-universality) identifies that very field with the free group's affiliated division closure.
Over it, invertible row and column operations reduce \(A\) to a rectangular identity of size \(r\) padded by zeros.
These operations are invertible over the affiliated algebra as well, so they preserve its module rank, equivalently the trace of the regular range projection (the support of a matrix is its image projection over the affiliated algebra).
Thus the free regular rank equals \(r\).
The original factorization descends to every quotient and gives \(\operatorname{rank}_{G_n} A_n\le r\), without any analytic specialization of the field.
Combined with the lower bound this proves convergence.
In particular, among those indices where \(A_n\) has closed range, its rank eventually equals the free integer rank, even if the gaps have no common positive lower bound.

For the uniform scalar assertion normalize the coefficient vector on the finite ball to Euclidean norm one, a compact sphere, and take one common \(M\) as above.
Every such free-group scalar has rank one by the affiliated division-ring result.
Its free trace of \(h_k(A^*A)\) is continuous in the coefficients, increases with \(k\), and tends pointwise to one.
By compactness the convergence is uniform.
Given any tolerance choose that single \(k\) and then use \(2kR<c_*L\) for all sufficiently large good tuples.
This bounds the scalar kernel dimension uniformly by the tolerance.

There is a consequence for algebraic annihilators whose terms need not be short words.
Fix positive integers \(R,s\).
For every sufficiently large good tuple there are no nonzero \(a,b\in\mathbb C G_n\) with \(ab=0\), with \(a\) supported in the rose ball of radius \(R\) and \(b\) supported on at most \(s\) group elements anywhere.
Indeed lift the coefficients of \(a\) along that ball, which embeds for large \(n\), and take the uniform kernel bound strictly less than \(1/s\).
For \(b\), irrespective of its word lengths,
\[
  \|b\|_2^2=\tau(b^*b)\le \|\lambda(b)\|^2\operatorname{rank}_{G_n}(b)
      \le s\|b\|_2^2\operatorname{rank}_{G_n}(b).
\]
Here \(\|\lambda(b)\|\le\|b\|_1\le\sqrt{s}\|b\|_2\), and the support projections of \(b^*b\) and \(bb^*\) have equal trace.
The range of \(b\) therefore has dimension at least \(1/s\) and cannot lie in the kernel of \(a\).
Taking adjoints gives the other order.
Thus any complex algebraic annihilators of bounded-radius scalars must have support sizes tending to infinity along good tuples, even if their word lengths are unrestricted.
The rank method still permits fractional dimensions at individual indices without closed range.
It supplies neither a rank convergence rate uniform in growing word radii nor the unrestricted strong Atiyah conjecture.

## Lifting a small algebraic annihilator

For algebraic zero products a separate argument gives a numerical bound in every characteristic, even when the support radius varies.
Let \(\pi:F\twoheadrightarrow G\) be a marked quotient killing no nontrivial freely reduced word of length strictly below \(\sigma>0\).
Fix a field \(k\) and nonzero \(a,b\in kG\) with \(ab=0\).
Suppose \(S=\operatorname{supp}a\) lies in the radius-\(R\) rose ball and write \(T=\operatorname{supp}b\).
There is no word-length assumption on \(T\).
Make a multigraph on \(T\) by inserting an edge for every equality \(x h=y h'\) of distinct product occurrences, with \(x,y\in S\) and \(h,h'\in T\).
In the direction \(h\to h'\), this says \(h'=y^{-1}x h\).
The reverse uses the inverse multiplier.
The endpoints are distinct by cancellation in \(G\), and parallel edges are retained.
For every component \(Q\), the restriction \(b_Q\) of \(b\) to \(Q\) satisfies \(a b_Q=0\), since each individual product fiber is contained on the column side in one component.
In fact
\[
                     2R\,|Q|\ \ge\ \sigma .
\]

To see this, fix lifts \(X_x\in F\) of the elements of \(S\) of lengths at most \(R\), and label the directed edge above by \(X_y^{-1}X_x\).
Root a spanning tree of \(Q\) at \(h_0\).
Put \(V_{h_0}=1\), and propagate along tree edges by *left* multiplication by their labels.
Then \(\pi(V_h)=h h_0^{-1}\).
For each nontree edge the walk along it and back along the tree is a simple cycle (allowing length two) of length at most \(|Q|\).
Multiplying its labels in reverse traversal order gives a word of length at most \(2R|Q|\) trivial in \(G\), because it fixes its starting vertex by left multiplication.
If \(2R|Q|<\sigma\) it is trivial in \(F\).
Hence every edge, including the nontree ones, satisfies \(V_{h'}=X_y^{-1}X_x V_h\).
Cancelling the shared tree path from the root gives precisely the cycle identity.
The products \(X_xV_h\) consequently agree for each collision, and cannot agree across different original products because their images are \(x h h_0^{-1}\).
The factor labels themselves stay distinct under the lifts within each side.
Thus the lifted polynomials with the same coefficients are nonzero and multiply to zero in \(kF\).
This is impossible: the free group has a bi-invariant order, in which the two least terms give a unique least product, with nonzero coefficient.

Taking \(\sigma=c_*L\) gives the asserted restriction for every good tuple.
The same conclusion holds for the other factor order by applying inversion, which is an anti-automorphism of \(kG\) and preserves the rose ball.
Left-translating the first support or right-translating the second merely multiplies the product by a unit, so the corresponding translates are allowed as well.
Unlike a comparison of the word lengths of both factors, the obstruction controls the number of terms of an arbitrarily distant annihilator, component by component.

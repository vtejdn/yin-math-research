---
author: Yin
---
# Connected matching graphs and the sizes of the two characteristic-two supports

## Statement

Use the two random graphs on \(n\) vertices each in [Ope26f, §2.1](../literature/pdf/Ope26f.pdf#page=3), with the logarithmic girth conditioning of its §2.3 and \(n\) tending to infinity through the specified multiples of \(2(16513)^2\).
Fix one prescribed root on each side.
With probability tending to one, each entire side is connected.
Moreover the two actual support sizes of the group-ring factors of §6 are each \(n-o(n)\) in probability.
In particular these conclusions hold simultaneously for a sequence of the source's torsion-free realizations.
They also hold under further conditioning on the source's prescribed diameter and absence-of-arrangements event, which has probability tending to one.

For the trivial homomorphism to \(C_7\), on the connected event each side has exactly \(n\) vertex occurrences in the identity class and the occurrence product has exactly \(n^2\) pairs there.
After collecting the actual group labels over \(\mathbb F_2\) but before projecting, each side has even support size, at least two when its root is separated.
The projected occurrence counts and the cardinalities of the actual supports are different quantities.
The [fixed finite target estimate](Yin_C_A0041_v1.md#statement) excludes every nontrivial homomorphism to \(C_7\) with probability tending to one.
The calculation below also gives the explicit bound \(\exp(-25pn+o(n))\) for the probability of such a homomorphism, with \(p=129/16513\).

## The probability of a cut

Write \(q=128,\ v=q^2+q+1,\ k=q+1\), and \(p=k/v\).
For either side of the graph, take a coloring of its vertices and denote its overall color probabilities by \(m_i\).
For an ordinary point \(t\) of the projective plane let \(p_{ti}\) be the proportion of color \(i\) among the \(np\) vertices carrying \(t\).
For an arbitrary signed label \(t\), including the extra labels, define \(p_{ti}\) by the same rule.
Let \(P_t=(p_{ti})_i\) and use natural-log entropy \(H(P)=-\sum_i P_i\log P_i\).

Consider the event that every matching preserves colors, or more generally sends them by a prescribed permutation for each signed label and its inverse.
If the two color histograms at opposite labels fail to agree after that permutation, the event has probability zero.
Otherwise the probability for one inverse pair is \(\prod_i (np\,p_{ti})!/(np)!\).
The two label entropies are equal, so independence of inverse-pair matchings and the factorial estimate bound the probability for this fixed coloring by
\[
 \exp\left(-\frac{np}{2}\sum_{t\text{ signed}}H(P_t)+O(\log(n+1))\right)
 \le
 \exp\left(-\frac{nk}{2}\,\mathbb E_t H(P_t)+O(\log(n+1))\right),        \tag{1}
\]
where the expectation on the right is uniform over the \(v\) ordinary points and the alphabet and number of colors are fixed.
At most \(\exp(nH(m))\) colorings have any one given overall histogram \(m\), by the multinomial bound, and there are polynomially many such histograms.

The incidence matrix \(N\) between equally frequent line types and ordinary points satisfies \(NN^{\mathsf T}=qI+\mathbf1\mathbf1^{\mathsf T}\).
If \(z_{Li}\) is the color-\(i\) proportion on line \(L\), the vector \((p_{ti})_t\) is \(N^{\mathsf T}(z_{Li})_L/k\).
Both means are \(m_i\).
On subtracting the mean and taking squared norms,
\[
 \mathbb E_t(p_{ti}-m_i)^2
   =\frac{q}{k^2}\mathbb E_L(z_{Li}-m_i)^2
   \le \frac{q}{k^2}m_i(1-m_i).
\]
Since \(H(P)\ge1-\sum_iP_i^2\), this gives
\[
 \mathbb E_t H(P_t)\ge
 (1-q/k^2)(1-\sum_i m_i^2)\ge (1-q/k^2)\theta,
 \qquad \theta=1-\max_i m_i.                                           \tag{2}
\]

For a binary coloring take \(0<\theta\le1/2\) as the proportion in the smaller color class.
If \(\theta\ge p^2\), its entropy satisfies \(H(m)\le\theta(1+\log(1/\theta))\le\theta(1+2\log(1/p))\).
Using (2) and the displayed \(q,k,p\) gives \((k/2)\mathbb E_tH(P_t)-H(m)\ge4\theta\).
For \(0<\theta<p^2\), write \(z_t\) for the smaller *global* class's proportion at ordinary point \(t\).
Then \(z_t\le\theta/p\) and \(\mathbb E_t z_t=\theta\).
As \(H(P_t)\ge z_t\log(1/z_t)\), we have
\[
 \mathbb E_t H(P_t)\ge\theta\log(p/\theta)
                  \ge \tfrac12\theta\log(1/\theta).
\]
With \(k=129\) and \(\theta<p^2\), the same gap \(4\theta\) follows.

For any fixed \(0<\rho<1/2\), (1) now bounds the unconditioned probability of a partition having no crossing edge and smaller part between \(\rho n\) and \(n/2\) by \(\exp(-4\rho n+O(\log(n+1)))\).
Here the identity color permutations express precisely that no matching crosses the partition.
The [girth-conditioning estimate](Yin_C_A0041_v1.md#girth-conditioning-and-the-torsion-free-realizations) gives the conditioning event probability at least \(\exp(-o(n))\), so such a cut has probability \(o(1)\) in the conditioned law.
Meanwhile the proof of [Ope26f, Lemma 2.3, pp. 6–7](../literature/pdf/Ope26f.pdf#page=6) gives a fixed sufficiently small \(\rho>0\) for which every nonempty set of at most \(\rho n\) vertices grows by a factor of at least two on adjoining its neighbors, with conditional probability \(1-o(1)\) on both sides.
A component in this size range would fail that property.
If a side is disconnected, its smallest component has size at most \(n/2\), so the two estimates exclude disconnection with probability \(1-o(1)\).

For the numerical \(C_7\) bound take the seven colors to be vertex potentials for a proposed nonzero label character, as in the [finite target criterion](Yin_C_A0041_v1.md#a-finite-target-as-a-vertex-coloring).
Choose \(t\) with nonzero increment.
Every one of the \(np\) matching edges for this inverse pair must have an endpoint outside the largest color class.
A vertex occurs at most twice among their endpoints, giving \(\theta\ge p/2\).
Since \(H(m)\le\theta(1+\log(6/\theta))\), (2) implies
\[
   \tfrac{k}{2}\mathbb E_tH(P_t)-H(m)
       \ge \theta\bigl(\tfrac{k}{2}(1-q/k^2)-1-\log(12/p)\bigr)
       \ge 50\theta\ge25p .
\]
One side suffices for the necessary color constraints on a character of the whole group, because loops from every component are coned.
There are at most \(7^{8258}\) assignments on the rose generators, independently of \(n\).
Equation (1), the histogram count and the girth-conditioning estimate give the claimed exponential bound.

## Distinct labels away from the roots

For any matching tuple the group is defined by coning all components, independently of the choice of roots.
Call a vertex ambiguous if some path from it to a different vertex of its component has trivial group label.
For a fixed component root the group labels of two vertices in that component coincide exactly when the path between them has trivial label, by composition and path independence.
Thus an unambiguous vertex contributes a singleton group label regardless of the component root.

For either side, [Ope26f, Proposition 4.5 and Proposition 5.1, pp. 18–20](../literature/pdf/Ope26f.pdf#page=18) imply that the probability that any one vertex specified as that side's root is ambiguous tends to zero in the girth-conditioned ensemble.
Here the other side's root can be fixed arbitrarily throughout.
Vertices of the same full prescribed type on the chosen side can be interchanged by permutations of their names preserving the matching law and the girth condition.
There are only finitely many types independent of \(n\), and the source's predetermined-root assertion applies to a representative in each.
The supremum over individual vertices of the probability of ambiguity therefore tends to zero.
Linearity of expectation gives \(o(n)\) expected ambiguous vertices on each side.
For every fixed \(\varepsilon>0\), Markov's inequality makes the probability of more than \(\varepsilon n\) ambiguous vertices tend to zero.
This argument controls their fraction without requiring all \(n\) root-separation events simultaneously.

On a connected side all its unambiguous vertices contribute distinct singleton coefficients to its factor, also after taking inverses on the second side.
The support cardinality is at most \(n\) and at least \(n\) minus the number of ambiguous vertices.
Moreover each surviving label has odd multiplicity, so the support size is congruent to the total number \(n\) of occurrences modulo two.
Here \(n\) is even, and root separation ensures the identity survives.
These facts give the stated asymptotics and the deterministic lower bound two for connected, root-separated realizations.
For the trivial \(C_7\) map the actual supports instead give \(|\operatorname{supp}\alpha|\,|\operatorname{supp}\beta|\) pairs in the identity class, which is \(n^2-o(n^2)\) in probability.
The histogram with \(n^2\) pairs counts all occurrences before collecting any repeated label.

The original paper specifies its matching tuple existentially in [§6, p. 24](../literature/pdf/Ope26f.pdf#page=24).
These estimates do not prescribe the exact support sizes of an individual unspecified tuple, nor do they assert connectivity or the absence of a nontrivial \(C_7\) character for every tuple meeting its topological safeguards.

## Assessment history

### Decision matching-connectivity

| Field | Value |
| --- | --- |
| date | 2026-11-17T02:27 |
| status | proved |
| reason | Independent mathematical review covers the full argument and its limitations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Connectedness, support collision asymptotics and the exponential bound on a nonzero character to the seven-cycle. |
| argument | [Proof](#the-probability-of-a-cut) | Complete argument under the stated hypotheses. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0071_v1.md#whole-argument-finding) | Independent review of these conclusions and their inputs. |

## Current assessment

[Selected decision](#decision-matching-connectivity)

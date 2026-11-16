---
author: Yin
---

# Fixed finite targets for the random matching presentation in Ope26f

## Statement

Let \(G_n\) be the group obtained by coning every component of the two graphs in the Ope26f matching model.
The two sides have \(n\) vertices each, with the fixed type proportions of §2.1, and the original independently uniform bijections are used for distinct inverse pairs and sides. [Ope26f, pp. 2–4](../literature/pdf/Ope26f.pdf#page=2)
Fix a finite group \(Q\).
There is a constant \(c_Q>0\) such that for all sufficiently large admissible \(n\)
\[
 \Pr\bigl(\operatorname{Hom}(G_n,Q)\text{ contains a nontrivial map}\bigr)
                     \le e^{-c_Q n}.
\]
The same bound, with a possibly smaller positive constant, holds under the source's logarithmic girth conditioning and under the further condition that its diameter and reduced-arrangement conclusions hold.
In particular there exist torsion-free realizations with the source's nonzero characteristic-two zero product and no nontrivial homomorphism to \(C_7\).
For each fixed \(M\) the statement holds simultaneously for all finite groups of order at most \(M\).
The constants depend on the targets, and this probability bound allows exceptional matching tuples.

## A finite target as a vertex coloring

Represent the rose fundamental group by the free group \(F\) on its inverse pairs and take \(T\) as the signed alphabet.
The group of the cone complex is the quotient of \(F\) by the normal closure of the labels of the closed walks in **all** graph components, by van Kampen.
A homomorphism \(\theta:F\to Q\) descends precisely when there are vertex colors \(f(v)\in Q\) satisfying
\[
                          f(v')=f(v)\theta(t)                           \tag{1}
\]
along every signed edge \(v\xrightarrow{t}v'\).
Necessity follows by transporting an arbitrary initial color along paths in each component, since all closed walks have trivial image.
Conversely the ordered product of the increments around a closed walk fixes its starting color under right multiplication and is therefore the identity.
It suffices for the probability upper bound to impose (1) on the first side alone.

Write \(\lambda_\tau>0\) for the fixed fraction of vertices there of each type \(\tau\), and \(S_\tau\subseteq T\) for its labels.
The fraction \(\rho=\sum_{\tau:t\in S_\tau}\lambda_\tau=129/16513\) is independent of \(t\).
For a proposed coloring, let \(v_\tau\) be its color probability vector on type \(\tau\) and let
\[
                  v_t=\rho^{-1}\sum_{\tau:t\in S_\tau}\lambda_\tau v_\tau.
\]
Necessary for any compatible matching is \(v_{\bar t}=(R_{\theta(t)})_*v_t\), where \(R_g\) is right multiplication in \(Q\).
These equalities define a compact set in the product of the type simplices.
They do not require that the graph be connected or that its chosen roots have specified colors.

## Strict entropy loss

Write \(H(v)=-\sum v_i\log v_i\), with \(0\log0=0\).
For a feasible fixed coloring and one oriented label \(t\) per inverse pair, the matching is accepted precisely when it sends each color class onto the specified translated class.
There are \(\prod_{q\in Q}(n\rho\,v_t(q))!\) such bijections out of \((n\rho)!\).
Matchings of distinct inverse pairs are independent in the unconditioned law.
For fixed type histograms the number of vertex colorings is a product of multinomial coefficients, one for each type.
Using \(\log(m!)=m\log m-m+O(\log(n+1))\) uniformly for \(0\le m\le n\), the expected number of compatible colorings with those histograms is at most
\[
             \exp\bigl(n(F_0-F_1)+O_{Q,T}(\log(n+1))\bigr),
 \qquad
 F_0=\sum_\tau\lambda_\tau H(v_\tau),\quad
 F_1=\tfrac12\sum_{t\in T}\rho H(v_t).
\]
The half sum uses the equality of the entropies at the two ends of each feasible matching.
There are at most \((n+1)^{|Q|\,\#\{\tau\}}\) choices of type histograms.

Concavity of entropy gives
\[
        F_1\ge\tfrac12\sum_\tau |S_\tau|\lambda_\tau H(v_\tau)
              \ge (129/2)F_0 .
\]
If \(F_0-F_1=0\), both quantities vanish.
Then every type and every label class is monochromatic.
Any two types on the first side contain a common ordinary letter since their ordinary lines in the projective plane intersect.
Because all type weights are positive, the color of that letter class is the color of both types.
Consequently one color occurs on the whole side and every signed label occurs there.
Compatibility forces right multiplication by every \(\theta(t)\) to fix that color, so \(\theta\) is trivial.

For each nontrivial \(\theta\), continuity and compactness thus give \(\max(F_0-F_1)<0\) on its nonempty feasible set, and an empty feasible set contributes nothing.
The polynomial factors in the first-moment estimate are absorbed by this strict exponential loss.
There are only finitely many homomorphisms from the finitely generated \(F\) to a fixed \(Q\).
The union bound proves the unconditional assertion, and another finite union covers all targets of bounded order.

## Girth conditioning and the torsion-free realizations

Let \(L=\lfloor c\log n\rfloor\) with \(c\) as in the source's (2.5), and \(d_*=132\).
In the original model let \(Z\) be the number of edges of either graph belonging to a cycle shorter than \(L\), with loops and pairs of parallel edges included.
Counting cycle descriptions and their distinct matching prescriptions as in the proof of Lemma 2.2 gives
\[
  \mathbb E Z\ \le\ 2\sum_{1\le k<L} k(2|T|/\rho)^k
                      \ \le\ n^{\gamma+o(1)},\qquad
                \gamma=c\log(2|T|/\rho)<1 .
\]
Pick \(\gamma<\gamma'<1\).
Markov's inequality gives probability at least \(1/2\) of \(Z\le n^{\gamma'}\) for sufficiently large \(n\).
Each such tuple has a sequence of at most \(n^{\gamma'}\) transpositions leading to a tuple of girth at least \(L\).
Indeed Lemma 2.2 chooses a nonbad edge of the same side and inverse pair, at distance greater than \(2L\) from a bad edge.
The bad edges exclude at most \(n^{\gamma'}\) choices and the degree bound excludes \(O(d_*^{2L+2})=o(n)\) others out of \(n\rho\).
Its switch creates no short cycle and strictly decreases \(Z\). [Ope26f, Lemma 2.2 and its proof, pp. 5–6](../literature/pdf/Ope26f.pdf#page=5)

Each tuple has at most \(C n^2\) possible individual transpositions, with a fixed \(C\) accounting for both sides and all inverse pairs.
All transpositions are reversible, so a girth-\(\ge L\) tuple has at most \(\sum_{j\le n^{\gamma'}}(C n^2)^j=\exp(o(n))\) tuples within that distance.
The unconditioned measure is uniform on the tuples.
Their cardinalities therefore imply \(\Pr(\mathrm{girth}\ge L)\ge\exp(-o(n))\).
Dividing the unconditional bound by this quantity preserves its exponential decay.

In that girth-conditioned law the diameter conclusion of Lemma 2.3 and absence of reduced spherical arrangements in Proposition 4.5 hold with probability \(1-o(1)\). [Ope26f, pp. 6–7 and Proposition 4.5, p. 18](../literature/pdf/Ope26f.pdf#page=18)
Further conditioning on their intersection changes the probability bound by at most a factor \(1+o(1)\).
The source then applies Proposition 5.1 and Corollary 5.3 to obtain root separation and torsion-freeness, and §6 gives the two nonzero factors and their zero product over \(\mathbb F_2\). [Ope26f, pp. 20–24](../literature/pdf/Ope26f.pdf#page=20)
For \(Q=C_7\), \(G_n\) is finitely generated and its abelianization on this high-probability event is finite of order prime to seven.
Indeed an infinite finitely generated abelian group, or a finite abelian group of order divisible by seven, has a quotient of order seven.
In particular testing a \(C_7\) quotient cannot provide a uniform obstruction for all of the source's torsion-free matching choices.
This argument leaves the characteristic-zero zero-product question open.

## A cyclic voltage cover that forces torsion

Fix *any* actual tuple, its cone group \(G\), and a surjection \(\theta:F\to C_7\).
Form a new labeled graph tuple by replacing every vertex \(v\) by \((v,c)\), \(c\in C_7\), and each edge \(v\xrightarrow{t}v'\) by the edges \((v,c)\xrightarrow{t}(v',c+\theta(t))\).
Cone its components to the **same rose** and denote the resulting group by \(G'\).
Every new graph loop has zero voltage, so \(\theta\) descends to a surjection \(G'\to C_7\).

If a closed walk in the original graphs has label \(W\) of nonzero voltage, its sevenfold repetition lifts to a closed walk and gives the relation \(W^7=1\) in \(G'\).
Its image under the new surjection has order seven, so \(W\) has order exactly seven in \(G'\).
If every original closed walk has zero voltage, the cover over each old component is a disjoint union of seven isomorphic labeled copies, by transporting colors from a basepoint.
In that case the two sets of closed-walk labels generate the same normal subgroup in \(F\), and \(G'=G\) with \(\theta\) already descending.
Thus this particular cover preserves torsion-freeness of a torsion-free cone group precisely when the quotient already existed.
It does not decide what can be achieved by choosing fresh matchings subject to color constraints.

## Assessment history

### Decision finite-quotient-scarcity

| Field | Value |
| --- | --- |
| date | 2026-11-17T02:27 |
| status | proved |
| reason | Independent mathematical review covers the full argument and its limitations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exponential loss for any prescribed finite target, conditioning and the torsion issue with deterministic voltage covers. |
| argument | [Proof](#a-finite-target-as-a-vertex-coloring) | Complete argument under the stated hypotheses. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0072_v1.md#whole-argument-finding) | Independent review of these conclusions and their inputs. |

## Current assessment

[Selected decision](#decision-finite-quotient-scarcity)

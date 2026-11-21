---
author: Yin
---
# A fixed-tuple probability bound for short sparse relations after color erasure

## Statement

Fix either side and a forward color \(c\in\{3,5,6\}\) of a connected tuple with the [four-line types, inverse pairing and prescribed populations](Yin_C_A0051_v1.md#four-lines-and-the-exact-color-matchings).
Suppose that every true group label in this color has even vertex multiplicity.
Draw \(s=62\) of its \(D=8252\) neutral ordinary inverse-pair types uniformly without replacement, retaining their formal markings.
For this set \(S\), let \(K_S\) be the subgroup they generate and put \(H=2\lceil\log n/\log(65/64)\rceil+4\).
In the marked Cayley graph of \(K_S\), let \(P_H\) project onto the closed span of the translates of oriented chains of cyclically reduced null words of length at most \(H\).
Let \(P_\infty\) project onto the closed span of all finite complex cycles.
Write \(E\) for the event that the same \(S\) satisfies
\[
 \operatorname{Tr}_{K_S}P_H\ge 1/128,\qquad
 \operatorname{Tr}_{K_S}P_\infty\ge 1/64
\]
with the unnormalized matrix trace.
The [finite-matrix and Betti-number identifications](Yin_C_A0091_v1.md#compression-to-the-finite-edge-set) give \(\operatorname{rk}_{K_S}R_{S,H}\ge1/128\) on \(E\), and \(\beta^{(2)}_1(K_S)\le61-1/64\) there when \(K_S\) is infinite.

For \(j=0,1,2,3\), put \(p_j=\binom{249}{j}\binom{D-249}{s-j}/\binom{D}{s}\), and define
\[
 \mu=2-2p_0-3p_1-2p_2-p_3,\qquad
 \rho=\frac{\mu-1/32}{2-1/32}.
\]
Then \(\Pr_S(E)>\rho>0.0428\), with \(\rho\approx0.04283973615\).
Further, for every prescribed set \(F\) of at most fourteen neutral inverse-pair types, some \(S\) disjoint from \(F\) satisfies both trace bounds.
These assertions concern the alphabet draw on the specified tuple.

## Argument

Let \(V\) be the set of true labels of the color having a nonempty set of ordinary signed stubs of odd multiplicity, and put \(v=|V|\).
The [four-line neutral degree bound](Yin_C_A0085_v1.md#the-neutral-degrees-on-the-four-lines) makes the graph on \(V\) nonempty and gives at least 249 neutral signed stubs at each vertex under full erasure.
At the minimum ordinary weight of 256, the symmetric difference of two projective lines contains at most four active points and three ordinary partners of extra letters, leaving at least 249 neutral signed stubs before the draw.
At a vertex \(g\), one inverse-pair type contributes zero, one or two to its degree, including the two ends of a loop.
For the sampled degree \(d'_g\) define
\[
 f(j)=j-2\mathbf1_{\{j>0\}},\qquad
 X=\frac1v\sum_{g\in V}f(d'_g).
\]
If the sampled graph has \(e\) edges and \(v_0\) nonisolated vertices, then \(vX=2e-2v_0\).
The [cycle deletion argument](Yin_C_A0091_v1.md#argument) gives at least \(\lceil v/128\rceil\) independent oriented cycles of length at most \(H\) whenever \(X\ge1/32\).
On the same graph its entire cycle space has dimension at least \(v/64\).
Applying [finite edge compression](Yin_C_A0091_v1.md#compression-to-the-finite-edge-set) to these two spaces proves \(\{X\ge1/32\}\subseteq E\) for each \(S\).

### The smallest expected truncated contribution

Take \(h(j)=\min(2,f(j))\).
Its values at \(0,1,2,3\) are \(0,-1,0,1\), and it equals \(2\) thereafter.
At a fixed vertex let \(m\) denote the number of occupied inverse pairs and \(a\) the number that contribute two.
Thus \(m+a\ge249\).
For fixed \(m\), changing a single contribution to a double one can only increase \(h(d'_g)\) pointwise.
If the changed pair is sampled, the old degree is at least one, and \(h\) is nondecreasing from one onwards.

For \(125\le m\le249\) it thus suffices to take \(a=249-m\).
Starting from 249 distinct single contributions, produce each such pattern by repeatedly replacing two single contributions by one double and one zero.
Only samples containing exactly one of the two affected pairs change the conditional expectation.
For such a sample, let \(Y\) be the degree from the other 61 pairs drawn uniformly from the remaining \(D-2\).
By symmetry the new conditional expectation minus the old one equals
\[
 \tfrac12\mathbb E[h(Y)+h(Y+2)-2h(Y+1)]
 =\tfrac12\bigl(2\Pr(Y=0)-\Pr(Y=3)\bigr).
\]
The remaining population has \(a_0\) double, \(b_0\) single and \(N_0\) zero contributions, with \(2a_0+b_0=247\) and \(N_0\ge8003\).
The two ways to obtain degree three give
\[
 \frac{\Pr(Y=3)}{\Pr(Y=0)}
 =\frac{a_0b_0\binom{N_0}{59}+\binom{b_0}{3}\binom{N_0}{58}}
        {\binom{N_0}{61}}
 \le \frac{247^2}{8\cdot130^2}+\frac{\binom{247}{3}}{130^3}<2 .
\]
Indeed \(a_0b_0\le247^2/8\), and each successive downward binomial ratio is at most \(61/(N_0-60)<1/130\).
Thus each replacement increases the expected truncated contribution.

For \(m\ge249\), it suffices by the fixed-\(m\) comparison to use only single contributions.
When one more formerly empty pair becomes single, condition on sampling that pair.
The other 61 pairs then give a hypergeometric count \(Y\) in a population of \(D-1\) with \(m\) occupied pairs.
The conditional increment is \(\Pr(1\le Y\le3)-\Pr(Y=0)\).
When \(\Pr(Y=0)>0\), the ratio \(\Pr(Y=1)/\Pr(Y=0)=61m/(8191-m)\) exceeds one for \(m\ge249\).
When \(\Pr(Y=0)=0\), the increment is nonnegative as well.
This proves that 249 singles minimize \(\mathbb E h(d'_g)\) over all the multiplicity patterns with degree at least 249, including vertices at which both signs of a type occur.

For 249 singles the expected value is exactly \(\mu\approx0.1155907305477\).
Consequently \(U=v^{-1}\sum_g h(d'_g)\) satisfies \(\mathbb E U\ge\mu\), \(U\le X\) and \(U\le2\), with no independence assumption across vertices.
If \(\Pr(X\ge1/32)<1\), the complement has \(U<1/32\), so
\[
 \mu\le\mathbb E U <(1/32)\Pr(X<1/32)+2\Pr(X\ge1/32).
\]
This gives \(\Pr(X\ge1/32)>\rho\), also true when the event has probability one.

### Avoiding fourteen prescribed types

Enlarge \(F\) to fourteen types if necessary and sample uniformly from the remaining \(N=8238\) types.
Every vertex retains at least \(249-28=221\) signed stubs before sampling.
Write \(u\ge221\) for its actual remaining degree.
At most \(u\) pair types meet the vertex, so
\[
 \mathbb E f(d'_g)\ge \phi(u)
 =\frac{62u}{N}-2+2\frac{\binom{N-u}{62}}{\binom{N}{62}},
\]
where a binomial coefficient with upper index below its lower index is zero.
For \(u\ge221\), the successive difference is
\[
 \phi(u+1)-\phi(u)=\frac{62}{N}
 \left(1-2\frac{\binom{N-u-1}{61}}{\binom{N-1}{61}}\right)>0.
\]
When the displayed ratio is positive it is at most \((1-u/(N-1))^{61}\le (1+61u/(N-1))^{-1}<1/2\).
Direct integer comparison gives
\[
 \phi(221)=\frac{13702}{8238}-2+
       2\frac{\binom{8017}{62}}{\binom{8238}{62}}
       \approx0.0314424390670>1/32 .
\]
It follows that \(\mathbb E X>1/32\) in this conditional sample, hence some alphabet disjoint from \(F\) has \(X\ge1/32\).

### Consequences for a complete family of cone fillings

On a tuple with the [bounded cone covering](Yin_C_A0092_v1.md#the-number-of-cones-required-at-the-c_a0091-scale), let \(\mathcal A\) consist of the inclusion-minimal neutral label supports of size at most 62 of nonzero outputs across the entire cover.
The [covering implication](Yin_C_A0092_v1.md#exact-alphabet-probabilities-and-a-usable-conditional-threshold) puts \(E\) inside the event that some \(A\in\mathcal A\) is contained in \(S\).
An upper bound \(\rho\) on this latter probability therefore excludes erasure.
In particular, writing \(q_j=\binom{62}{j}/\binom{8252}{j}\), the sufficient union bound is now \(\sum_{A\in\mathcal A}q_{|A|}\le\rho\).
Exact comparison gives \(\lfloor\rho/q_2\rfloor=771\) and \(\lfloor\rho/q_3\rfloor=106045\), for families consisting wholly of pairs or wholly of triples, respectively.
Under erasure, every set meeting every member of \(\mathcal A\) must have at least fifteen labels, since the alphabet constructed outside any fourteen prescribed types still contains a member.
These criteria include arbitrary numbers of cones within the filling bound.
Their application to a particular exceptional tuple requires control of its complete family of output supports.

## Assessment history

### Decision fixed-alphabet-probability

| Field | Value |
| --- | --- |
| date | 2026-11-21T06:38 |
| status | proved |
| reason | The independent reviewer verifies the four-line input, extremal truncated expectation, strict hypergeometric inequalities and the transfer to the same sampled alphabet. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The same two trace bounds on a fixed erased tuple with probability exceeding rho, fourteen-type avoidance and complete-cover consequences. |
| argument | [Proof](#argument) | Minimum neutral degree, a clipped sampling estimate, conditional avoidance and finite cone-cover thresholds. |
| review | [Whole finding](../audits/reviews/Yin_R_A0127_v2.md#whole-finding) | Independent whole-claim inspection at the scope specified in the finding. |
| dependency | [Neutral degrees](Yin_C_A0085_v1.md#decision-odd-stub-degrees) | The 249 neutral signed stubs at an even nonempty true label of the specified four-line color. |
| dependency | [Trace comparison](Yin_C_A0091_v1.md#decision-short-relation-rank) | Cycle deletion and compression for the marked rank and full cycle-space dimension. |
| dependency | [Complete covering family](Yin_C_A0092_v1.md#decision-reviewed-contact-criterion) | A nonzero short-relation matrix is detected by a minimal neutral support in the covering configurations. |

## Current assessment

[Selected decision](#decision-fixed-alphabet-probability)

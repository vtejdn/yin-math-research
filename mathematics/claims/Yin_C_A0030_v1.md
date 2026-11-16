---
author: Yin
---
# Sampling the coefficient variety of a zero product and detecting complementary ranks

## Statement

Fix finite nonempty subsets \(A,B\) of any discrete group \(G\).
In the complex coefficient torus impose, for **every** \(w\in AB\),
\[
                   \sum_{xy=w} a_x b_y=0.                               \tag{1}
\]
Fix one row coefficient and one column coefficient to one by separate nonzero scalar rescalings.
Call the resulting affine algebraic set \(Z\); all coefficients remain nonzero and the support sets are fixed.
Use the canonical regular ranks \(r(a),r(b)\).

On each nonempty irreducible component of \(Z\), both ranks attain their respective suprema simultaneously almost surely for any probability law absolutely continuous with respect to volume on its smooth locus. A point component carries its point mass.
Their suprema sum to at most one.
If a single half-rank pair occurs on a component, almost every such sample on that component has both ranks exactly \(1/2\).
Independent continuously distributed coefficients on the entire coefficient torus, in contrast, give each factor rank one almost surely when the joint distributions on their coefficient spaces have densities.

Assume \(Z\ne\varnothing\).
The following are equivalent:

1. There is a complex pair on these supports with (1) and both ranks exactly \(1/2\).
2. For every \(\varepsilon>0\) there is a pair on the same supports with coefficients in \(\overline{\mathbb Q}\), satisfying (1), whose two complex regular ranks are at least \(1/2-\varepsilon\).
3. For the finite-moment quantities \(s_k\) below one has \(\lim_{k\to\infty}s_k=1/2\).

On fixed supports where item 1 fails, there is a positive gap between \(1/2\) and the smaller rank, uniform over all solutions to (1).
The quantities \(s_k\) use finitely many actual group products at each order. The convergence statement supplies no stopping bound in \(k\).

## Argument

### Rank from random evaluations on a connected parameter space

For holomorphic finite-coefficient families \(T\) on a connected complex manifold, use the function spaces \(V_n\), dimensions \(d_n\) and multiplication maps \(T_n:V_n\otimes\ell^2(G)\to V_{n+1}\otimes\ell^2(G)\) from [the analytic family bound](Yin_C_A0028_v1.md#argument).
Its proof gives \(r(T_n)\ge d_n R\), where \(R=\sup_p r(T(p))\), and a subsequence with \(d_n/d_{n+1}\to1\).
Take \(d_{n+1}\) independent samples \(p_j\) from a law with a density in local complex coordinates.
The evaluation matrix of a basis of \(V_{n+1}\) at these points is invertible with probability one.
Indeed, until the accumulated evaluation rows span the dual, some nonzero function of the space annihilates all these rows.
Its vanishing at the next independent point has probability zero, since a nonzero holomorphic function on a connected complex manifold has a volume-zero set of zeros.
Equivalently, the evaluation determinant is a nonzero holomorphic function on the product manifold: independent evaluation rows exist because the functions form a basis.
The zero-measure assertion follows locally by expanding in one variable at a polydisc center, using a nonzero coefficient function, induction in the remaining variables, the one-variable isolated-zero theorem and Fubini.
The corresponding real-analytic result is also stated in [Mityagin's note](https://arxiv.org/abs/1512.07276).

On any such invertible evaluation tuple the closed image of \(T_n\), under this invertible scalar coordinate change, lies in the direct sum of the closed ranges of the \(T(p_j)\).
Its module dimension is preserved by the coordinate change. Taking expectations yields
\[
          d_n R\ \le\ r(T_n)\ \le\ d_{n+1}\,\mathbb E\,r(T(p)).
\]
The rank is measurable and lower semicontinuous: a spectral cut of the input support at a positive singular-value threshold remains a subspace of injectivity under a sufficiently small norm perturbation.
Taking the subsequence yields \(\mathbb E r=R\), hence \(r=R\) almost surely. The intersection of the probability-one events for the two factors still has probability one.

### Components and exact support

Use the elementary complex-variety facts that an affine algebraic set of finite type has finitely many irreducible components, and the smooth locus of an irreducible complex variety is a connected complex manifold dense in the usual topology.
For the two topology comparisons see [Milne, Chapter 15, Propositions 15.1 and 15.2](https://www.jmilne.org/math/CourseNotes/AG15.pdf).
This applies inside the coefficient torus, which can equally be presented by adjoining inverse coordinates.
By lower semicontinuity the supremum of rank on each component is the same as on its smooth locus, including when the specified half pair is singular or belongs to more than one component.
For a point component the conclusions are immediate.
Apply the evaluation result on each positive-dimensional smooth locus: the two almost-sure ranks sum to at most one by (1). If a point has two half ranks, the two suprema are at least one half and therefore equal one half.
On the unrestricted coefficient torus, the supremum for one factor is one, since a single coefficient can dominate the sum of the moduli of all the others, giving a bounded inverse by a Neumann series after translation.
This proves the sampling assertions.

The supremum on \(Z\) of \(\min\{r(a),r(b)\}\) is attained: on each component it is the minimum of the two simultaneous generic ranks, and there are finitely many components.
It is at most \(1/2\), and attainment at \(1/2\) means both ranks equal \(1/2\).
Consequently absence of a half pair gives the stated uniform gap, even if (1) admits many full-support solutions.

The equations and the nonvanishing conditions are defined over \(\mathbb Q\).
Points of \(Z\) with algebraic coefficients are dense in its usual topology: a rational open box in the real and imaginary coordinates that meets \(Z\) gives an existential polynomial system of equalities and strict inequalities over \(\mathbb Q\).
Real-closed-field quantifier elimination gives a point of that box over the real algebraic numbers.
This argument uses the equations of the whole variety and does not require a component to be defined over \(\mathbb Q\).
Lower semicontinuity of the two ranks at a half pair now proves item 2. Conversely item 2 forces the attained supremum of the smaller rank to be \(1/2\).
This concerns actual complex regular rank; the [finite-characteristic comparison](Yin_C_A0029_v1.md#statement) uses amenability to compare a different rank in positive characteristic.

### Finite moments using the original product equations

Normalize \(\widetilde a=a/\|a\|_2,\ \widetilde b=b/\|b\|_2\).
For each such input \(c\) with support size \(m\) and \(\|c\|_2=1\) put
\[
       h_k(c)=1-\tau\big((1-c^*c/m)^k\big),\qquad
       s_k=\sup_{(a,b)\in Z}\min\{h_k(\widetilde a),h_k(\widetilde b)\}.
\]
The norm estimate \(\|c\|\le\|c\|_1\le\sqrt m\) puts \(1-c^*c/m\) between zero and one.
The spectral theorem shows \(h_k(c)\uparrow r(c)\).
Hence \(\sup_k s_k=\sup_Z\min\{r(a),r(b)\}\), by monotonicity for each fixed pair and interchange of suprema.
This proves item 3 and the equivalence.
With unit \(2\)-norms the \(h_k\) are real polynomials in the real and imaginary parts of the coefficients; the trace just extracts the identity coefficient of each finite product.
One may work on the unit spheres with exact nonzero supports instead of the coordinate normalization in (1), by rescaling.
Thus each \(s_k\) is the supremum of a bounded semialgebraic optimization problem given the required finite word-equality data in \(G\).
Lower moment estimates or sampling at finite precision alone do not certify that the limit equals \(1/2\).

## Assessment history

### Decision component-sampling

| Field | Value |
| --- | --- |
| date | 2026-11-17T00:51 |
| status | proved |
| reason | The independent review covers the full fixed statement, proof and stated scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Simultaneous generic ranks, fixed-support attainment and the finite-moment limit. |
| argument | [Proof](#argument) | Complete argument under the stated hypotheses. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0061_v1.md#whole-argument-finding) | Independent mathematical review of the result and its limitations. |

## Current assessment

[Selected decision](#decision-component-sampling)

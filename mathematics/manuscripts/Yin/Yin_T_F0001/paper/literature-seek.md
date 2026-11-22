# Literature Search

## Example 6.1

Example 6.1 in [examples.tex](sections/examples.tex), label `ex:liberation-without-duals`, exhibits a selfadjoint generator with arcsine law and regular scalar shifts.
It takes \(L=P_\Omega\) and excludes an ordinary dual system in the domain sense of Definition 1.8.
The search looked for a source that explicitly exhibits both properties for the same example, including other laws and the original bounded formulations.

- Voiculescu's Part VI, Definition 13.1 and Remark 13.2(c), give the algebra-based definition and a construction of a liberation dual system from an ordinary dual system.
  The one-coordinate choice \(T=P_\Omega\) with scalar coefficient algebra satisfies Definition 13.1 directly.
  The inspected §13, pp. 160–161 of the published edition, gives no explicit example that also excludes an ordinary dual system. [Voiculescu 1999](https://doi.org/10.1006/aima.1998.1819) · [Section 13 source inspection](../../../../audits/literature/Voi99/Yin_U001.md)
- Voiculescu's Part V, §5, and Mai, Speicher and Yin's §6.2 concern ordinary dual systems.
  The examples in Part V, §5.13, and MSY23, Proposition 6.3, exhibit ordinary dual systems.
  Shlyakhtenko's Theorem 1 concerns the unbounded ordinary setting.
  These passages give no example separating the two dual-system conditions. [Voiculescu 1998](https://doi.org/10.1007/s002220050222) · [Mai, Speicher and Yin 2023](https://doi.org/10.1016/j.jfa.2023.110016) · [Shlyakhtenko, arXiv v1](https://arxiv.org/abs/math/0504062)

The searches on 2026-11-20 UTC used `liberation dual system` and its hyphenated variant, Voiculescu's `dual system to` terminology, and combinations of `dual operator`, `liberation gradient`, `arcsine`, `example`, `converse` and `13.2(c)`.
They covered general web search, arXiv-oriented searches and the relevant passages of the primary sources above.
An Oberwolfach search hit brings up adjacent abstracts on ordinary dual systems and liberation. [Oberwolfach Reports 2015, No. 28, pp. 1587–1588](https://publications.mfo.de/bitstream/handle/mfo/3475/OWR_2015_28.pdf?sequence=1)

Within this search scope, no source was found that explicitly gives a liberation dual system and excludes an ordinary dual system for the same example.
Example 6.1 uses its direct argument for that conclusion.

### Arcsine Cauchy transform

The search on 2026-11-21 UTC for the arcsine Cauchy transform checked §§2.1–2.2 and Example 2.8. [Sch17, arXiv v4](https://arxiv.org/html/1605.06689v4).
For variance $1/2$ the density in that example is the one in the manuscript, and its reciprocal Cauchy transform is $F_\mu(z)=\sqrt{z^2-1}$ in the upper half-plane.
Taking the reciprocal and passing to the real axis on $(1,\infty)$ gives $G_\mu(r)=(r^2-1)^{-1/2}$, with the positive square root since $G_\mu(r)>0$.

## Example 6.3

The search on 2026-11-21 UTC matched the steps of `ex:bounded-division-closure` in [examples.tex](sections/examples.tex) with results on bicommutants, inverse closure of unital $C^*$-subalgebras, free-product duals and bounded commutators for operator-valued semicircular variables.

- The bicommutant theorem states that a unital strongly closed selfadjoint subalgebra $N\subseteq\mathcal B(H)$ satisfies $N=N''$.
  Here $N=W^*(X,Y)$, and commutation with $X$ and $Y$ implies commutation with $S$ by cancellation of $X$ on the left and its dense range on the right. [AP18, Theorem 2.1.3, p. 30](https://www.math.ucla.edu/~popa/Books/IIun.pdf#page=36).
- Spectral permanence applies to arbitrary elements of a unital $C^*$-subalgebra containing the ambient unit.
  The inclusion $C^*(X,Y)\subseteq M$ shares the unit, so an element of $C^*(X,Y)$ invertible in $M$ has its inverse in $C^*(X,Y)$. [Put19, Theorem 1.5.3, p. 24](https://web.uvic.ca/~ifputnam/ln/C%2A-algebras.pdf#page=24).
- Voi98, §5.5, gives the pointed free-product left and right representations and their commutator identities.
  For the right lift of $T_0$ the same-factor commutator is the extension of $[X,T_0]$ by zero off the vacuum-plus-one-factor space, and the cross-factor commutator with $S$ is zero.
  Proposition 5.6 also gives this lift using the bounded dual to the semicircular factor in §5.13, with $iT_0$ as the bounded selfadjoint input to the first factor and $-i$ times its lift as the output in the manuscript's normalization.
  Skew-adjointness of $T_0$ follows from the compressed skew-adjoint Hilbert transform and the same real multiplication operator on each side.
  The elementary tensor model used for the construction of $D_2$ still requires its own identification with the free-product space. [Voi98, §§5.5–5.6 and §5.13](https://doi.org/10.1007/s002220050222) · [Source inspection](../../../../audits/literature/Voi98/Yin_U005.md#free-products-55-58).
- Tao06, Proposition 1.2, already supplies the unweighted Hilbert-transform bound used for the scalar $T_0$.
  The local application conjugates by the square root of the density, bounds the resulting multiplication operators and calculates the rank-one commutator. [Tao06, Proposition 1.2](https://www.math.ucla.edu/~tao/247a.1.06f/notes4.pdf) · [Review of the source application in C_F0012 v1](../../../../audits/reviews/Yin_R_F0056_v1.md#main-counterexample-finding).

The searches for `bounded dual system`, `rank-one commutator`, and `operator-valued semicircular`, combined with `sandwich`, `free product`, and `right creation`, found no inspected result supplying a bounded $D_2$ commuting with $X$ and satisfying $[Y,D_2]=P_\Omega$ for $Y=XSX$ with $0\in\sigma(X)$.
The scalar free-product lift applies to the free factors $W^*(X)$ and $W^*(S)$.
For the change from $S$ to $Y$, the free difference quotient in the $S$ coordinate is $X\otimes X^{\mathrm{op}}$, which has no bounded inverse in $M\bar\otimes M^{\mathrm{op}}$ because $0\in\sigma(X)$.
Thus a change-of-variables argument requiring bounded invertibility is inapplicable here.
The triangular-kernel construction and the correction producing $D_1$ continue to supply the bounded dual system, and the small-spectral-vector argument supplies the quantitative norm separation. [C_F0012 v1 and its review](../../../../audits/reviews/Yin_R_F0056_v1.md#main-counterexample-finding).

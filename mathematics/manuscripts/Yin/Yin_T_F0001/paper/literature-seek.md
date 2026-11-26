# Literature Search

## Introduction

The search on 2026-11-26 examined sources for the problem introduced after the free-field realization theorem, the transition from the semicircular result to the dual-system criterion, and the role of finite rank in [the introduction](sections/introduction.tex).
The search used combinations of `affiliated division closure`, `rationality criterion`, `finite rank commutators`, `dual system` and `noncommutative Hankel matrix` and followed the references from the free-group and semicircular criteria.

- Collins, Mai, Miyagawa, Parraud and Yin explicitly ask for a criterion of the Duchamp–Reutenauer and Linnell type for membership in the affiliated division closure when \(\Delta(X)=d\).
  The final substantive paragraph of the introduction, arXiv v4 p. 4, states the question for operators affiliated with \(W^*(X)\).
  This is the direct motivation for `thm:delta` after the opening sentence citing MSY23.
  The locator was checked in arXiv v4 and the bibliographic identity was checked against the publisher record. [CMM+24, Introduction](https://arxiv.org/pdf/2103.05962#page=4) · [Journal record](https://link.springer.com/article/10.1007/s00208-022-02530-5).
- Miyagawa leaves the extension of Theorem 3.1 to general tuples admitting a dual system for future work in Remark 3.11, p. 18 of the published edition.
  Theorem 3.1 concerns bounded division closure and the remark uses bounded dual operators.
  The remark can motivate the affiliated criterion for normal tuples in `thm:analytic`, alongside Theorem 4.5 in the existing Miy22 paragraph.
  The distinction between the two ambient algebras matters because `ex:bounded-division-closure` gives strict inclusion for a selfadjoint tuple with a bounded dual system. [Miy22, Theorem 3.1 and Remark 3.11](https://doi.org/10.1016/j.jfa.2022.109609) · [Local example](sections/examples.tex).
- Berstel and Reutenauer, Chapter 2, §1, Theorem 1.6, give the finite-Hankel-rank characterization of rational formal series, credited there to Carlyle–Paz and Fliess.
  The retained manuscript statement on p. 31 supplies optional background for the sentence on Duchamp and Reutenauer's use of rational series.
  The rank is algebraic and the rows and columns are indexed by words. [BR10 source reading](../../../../audits/literature/BR10/Yin_U002.md#formal-hankel-rank).
- Shlyakhtenko's discussion of unbounded dual systems in §1.1, Theorem 1 and its corollary, is an optional precedent at `def:dual-system`.
  He treats selfadjoint generators on the polynomial domain.
  The manuscript uses \(\mathcal M\Omega\) as a common subspace of the domains of the operators and their adjoints.
  The candidate citation concerns the unbounded formulation. [Shl06 source reading](../../../../audits/literature/Shl06/Yin_U001.md#shl06-normalized-dual-construction).

## Example 6.1

The lookup for `ex:maximal-delta-without-liberation` checked the published MSY23 Theorem 3.1 and Proposition 6.2 and the semicircular Fock commutators in Voi98, §5.13.
The full linear matrix criterion shows that the direct sum of the semicircular pair and its translate has maximal Delta.
The obstruction using the common spectral projection is supplied by the fixed local argument, including the two adjoint-domain pairings. [MSY23](https://doi.org/10.1016/j.jfa.2023.110016) · [Voi98](https://doi.org/10.1007/s002220050222) · [C_F0370 v1](../../../../claims/Yin_C_F0370_v1.md#argument).

## Example 6.2

Example 6.2 in [examples.tex](sections/examples.tex), label `ex:liberation-without-duals`, exhibits a selfadjoint generator with arcsine law and regular scalar shifts.
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
Example 6.2 uses its direct argument for that conclusion.

### Arcsine Cauchy transform

The search on 2026-11-21 UTC for the arcsine Cauchy transform checked §§2.1–2.2 and Example 2.8. [Sch17, arXiv v4](https://arxiv.org/html/1605.06689v4).
For variance $1/2$ the density in that example is the one in the manuscript, and its reciprocal Cauchy transform is $F_\mu(z)=\sqrt{z^2-1}$ in the upper half-plane.
Taking the reciprocal and passing to the real axis on $(1,\infty)$ gives $G_\mu(r)=(r^2-1)^{-1/2}$, with the positive square root since $G_\mu(r)>0$.

## Proposition 6.4

The follow-up search on 2026-11-22 UTC targeted the equivalence between a bounded solution of \([X,D]=P_1\) and an essentially bounded Lebesgue density for the law of one bounded selfadjoint \(X\) in [examples.tex](sections/examples.tex), label `prop:scalar-bounded-dual`.
The search used `bounded dual system`, `rank-one commutator`, `rank-one self-commutator`, `bounded density` and `Hilbert transform`, and followed references in the papers on singular integral models.
Compression to the cyclic subspace \(L^2(W^*(X),\tau)\) and extension by zero identify solvability there with solvability on the ambient Hilbert space, since the cyclic subspace reduces \(X\) and contains \(1\).

- Formula (2.2), Theorem (6.2) and the estimate on p. 545 of Kat68 give the full equivalence and a skew-adjoint solution of norm at most \(\pi\|w\|_\infty\) by taking the positive commutator to be \(P_1\). [Kat68](https://doi.org/10.4064/sm-31-5-535-546) · [Inspected rank-one specialization](../../../../audits/literature/Kat68/Yin_U001.md#scalar-bounded-dual).
- Pin68, Theorem 2.1 and the proof on pp. 224–226, give a singular integral representation for bounded selfadjoint \(U,V\) with \(VU-UV=(\pi i)^{-1}C\) for positive trace-class \(C\).
  On the cyclic space, take \(U=X\), \(V=iD_0\), and \(C=\pi P_1\), where \(D_0=(D-D^*)/2\) still satisfies \([X,D_0]=P_1\).
  In the scalar representation the coefficient \(k(t)^*\) in the proof is \(\sqrt{\pi}\) times the image of \(1\) under the representing unitary.
  The essential boundedness of \(k\) therefore gives a spectral density \(w(t)=|k(t)|^2/\pi\). [Pin68, published edition, Theorem 2.1](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6064-11511_2006_Article_BF02391914.pdf#page=6).
- CP71, p. 452, states the model in both directions for hyponormal operators whose rank-one self-commutator vector is cyclic for the real part.
  Applied to \(T=X+D_0\), whose self-commutator is \(2P_1\), their formulas (1.6)–(1.10) identify the law of \(X\) as \(w(t)\,dt\), where \(w(t)=|b(t)|^2/\pi\) on the Lebesgue model space \(L^2(E,dt)\).
  Conversely, given \(w\), set \(E=\{w>0\}\), \(a=0\) and \(b=\sqrt{\pi w}\) in (1.7).
  The unitary \(f\mapsto\sqrt{w}\,f\) from \(L^2(\mu)\) onto \(L^2(E,dt)\) identifies the model solution with the desired dual.
  The normalized Hilbert transform on \(L^2(\mathbb R,dt)\) has norm one, so the constructed dual has norm at most \(\pi\|w\|_\infty\).
  The authors attribute the cyclic rank-one representation to Xa Dao-xeng and point to Rosenblum's proof on p. 326.
  These earlier works were identified through CP71 and their relevant passages remain uninspected. [CP71, published edition, p. 452](https://www.e-periodica.ch/cntmng?pid=com-001%3A1971%3A46%3A%3A38#page=3).
- Kap15, Theorem 1.1 and (1.3), characterize solvability of the commutator equation on \(L^2(\mu)\) by uniform boundedness of the regularized Cauchy operators.
  For a compactly supported atomless real measure and the constant kernel \(1\) of \(P_1\), these are the regularizations of the Hilbert kernel \(1/(s-t)\), up to the commutator sign.
  Taking the limit against functions with separated compact supports gives the restricted bound used in LT13, Theorem 5.1, with both measures equal to \(\mu\).
  In dimension one its growth bound \(\mu(I)\leq C|I|\) gives the bounded-density necessity.
  The atomless assumption follows from the commutator equation by compression to any point spectral projection. [Kap15, published edition, p. 128](https://emis.de/ft/8583#page=4) · [LT13, published edition, Theorem 5.1](https://ems.press/content/serial-article-files/38411#page=19).
- Within the free-probability sources checked, the closest formulation is Shl24, p. 1273, which identifies the scalar dual with the Hilbert kernel and then discusses bounded dual systems for tuples.
  The inspected free-probability passages yielded no explicit scalar bounded-density equivalence.
  The operator-theory sources above already cover the equivalence, with Kat68 supplying the most direct reference for the current proof. [Shl24, published report, p. 1273](https://content.ems.press/assets/public/full-texts/serials/owr/21/2/14298372/online/10.4171-owr-2024-22.pdf#page=47).

## Example 6.5

The search on 2026-11-21 UTC matched the steps of `ex:bounded-division-closure` in [examples.tex](sections/examples.tex) with results on bicommutants, inverse closure of unital $C^*$-subalgebras, free-product duals and bounded commutators for operator-valued semicircular variables.

- A bicommutant proof of $S\in W^*(X,Y)$ uses cancellation of $X$ on the left and its dense range on the right to conclude that every operator commuting with $X,Y$ commutes with $S$. [AP18, Theorem 2.1.3, p. 30](https://www.math.ucla.edu/~popa/Books/IIun.pdf#page=36).
- For the calculation of $S=X^{-1}YX^{-1}$ in the example, the product of affiliated operators is the closure of their composition.
  The spectral characterization of affiliation puts a bounded affiliated operator in the represented von Neumann algebra. [AP18, Proposition 7.2.3 and Theorem 7.2.8, pp. 103–105](https://www.math.ucla.edu/~popa/Books/IIun.pdf#page=109).
- Spectral permanence applies to arbitrary elements of a unital $C^*$-subalgebra containing the ambient unit.
  The inclusion $C^*(X,Y)\subseteq M$ shares the unit, so an element of $C^*(X,Y)$ invertible in $M$ has its inverse in $C^*(X,Y)$. [Put19, Theorem 1.5.3, p. 24](https://web.uvic.ca/~ifputnam/ln/C%2A-algebras.pdf#page=24).
- Voi98, §5.5, gives the pointed free-product left and right representations and their commutator identities.
  For the right lift of $T_0$ the same-factor commutator is the extension of $[X,T_0]$ by zero off the vacuum-plus-one-factor space, and the cross-factor commutator with $S$ is zero.
  Proposition 5.6 also gives this lift using the bounded dual to the semicircular factor in §5.13, with $iT_0$ as the bounded selfadjoint input to the first factor and $-i$ times its lift as the output in the manuscript's normalization.
  In the earlier Hilbert-transform proof, skew-adjointness of $T_0$ follows from the compressed skew-adjoint Hilbert transform and the same real multiplication operator on each side.
  The elementary tensor model used for the construction of $D_2$ still requires its own identification with the free-product space. [Voi98, §§5.5–5.6 and §5.13](https://doi.org/10.1007/s002220050222) · [Source inspection](../../../../audits/literature/Voi98/Yin_U005.md#free-products-55-58).
- Tao06, Proposition 1.2, supplies the unweighted bound in the earlier Hilbert-transform construction of the scalar $T_0$.
  The local application conjugates by the square root of the density, bounds the resulting multiplication operators and calculates the rank-one commutator. [Tao06, Proposition 1.2](https://www.math.ucla.edu/~tao/247a.1.06f/notes4.pdf) · [Review of the source application in C_F0012 v1](../../../../audits/reviews/Yin_R_F0056_v1.md#main-counterexample-finding).

The searches for `bounded dual system`, `rank-one commutator`, and `operator-valued semicircular`, combined with `sandwich`, `free product`, and `right creation`, found no inspected result supplying a bounded $D_2$ commuting with $X$ and satisfying $[Y,D_2]=P_\Omega$ for $Y=XSX$ with $0\in\sigma(X)$.
The scalar free-product lift applies to the free factors $W^*(X)$ and $W^*(S)$.
For the change from $S$ to $Y$, the free difference quotient in the $S$ coordinate is $X\otimes X^{\mathrm{op}}$, which has no bounded inverse in $M\bar\otimes M^{\mathrm{op}}$ because $0\in\sigma(X)$.
Thus a change-of-variables argument requiring bounded invertibility is inapplicable here.
The triangular-kernel construction and the correction producing $D_1$ continue to supply the bounded dual system, and the small-spectral-vector argument supplies the quantitative norm separation. [C_F0012 v1 and its review](../../../../audits/reviews/Yin_R_F0056_v1.md#main-counterexample-finding).

### Bounded dual for the scalar factor

The search on 2026-11-22 UTC checked one-variable bounded dual systems and bounded positive rank-one commutators for the step \([X,D_X]=P_\Omega|_{H_0}\) on \(H_0=L^2(\mu)\) in [examples.tex](sections/examples.tex), label `ex:bounded-division-closure`.

- Kato's (2.2), p. 536, and Theorem (6.2), p. 543, give a bounded solution of \([X,D_X]=P_\Omega|_{H_0}\) exactly when the spectral measure of \(\Omega\) has an essentially bounded Lebesgue density.
  In this case \(w(t)=4t^3\mathbf 1_{(0,1)}(t)\), so the result applies directly.
  The sufficiency argument on p. 545 also gives a skew-adjoint solution of norm at most \(4\pi\) after centering the selfadjoint solution and multiplying by \(i\).
  Proposition 6.4 states the scalar criterion and the general norm bound. Example 6.5 applies both to the given density. [Kat68, published edition](https://doi.org/10.4064/sm-31-5-535-546) · [Inspected passage and specialization](../../../../audits/literature/Kat68/Yin_U001.md#scalar-bounded-dual).
- Voiculescu's §5.1 fixes the bounded selfadjoint convention, §5.6 gives the free-product lift, and §5.13 supplies the semicircular dual.
  Mai, Speicher and Yin use the manuscript's normalization in Definition 6.1 and deduce \(\Delta=n\) in Proposition 6.2 for an \(n\)-tuple with a bounded dual system. [Voi98](https://doi.org/10.1007/s002220050222) · [MSY23](https://doi.org/10.1016/j.jfa.2023.110016).
- Shlyakhtenko's Corollary 2 relates finite free Fisher information to closable skew-symmetric duals on the polynomial domain.
  The boundedness needed for the scalar free-product input is supplied by the Kato criterion. [Shl06, author preprint, §1.2](https://abelsymposium.no/symp2004/preprints/shlyakhtenko.pdf#page=4) · [Inspection of Corollary 2](../../../../audits/literature/Shl06/Yin_U001.md#corollary-2-and-the-essential-skew-adjointness-limit).

### Free-product lift and the tensor realization used for the second dual

The search on 2026-11-22 UTC checked the application of Voi98 to both lifted duals and looked for a direct source for the second dual after the change of generators.

- On p. 212, the basic Fock commutators in §5.13 give \([\ell(h)^*,r(h)]=P\) and \([\ell(h),r(h)]=0\) for a unit vector \(h\), hence \([S,r(h)]=P\) for the variance-one element \(S=\ell(h)+\ell(h)^*\).
  The right representations in §5.5, p. 209, lift this operator and \(T_0\) to a generator-first dual system for the free pair \((X,S)\).
  Proposition 5.6, pp. 209–210, gives the free-product existence statement in the selfadjoint convention. [Voi98](https://doi.org/10.1007/s002220050222) · [Source inspection](../../../../audits/literature/Voi98/Yin_U005.md#free-products-55-58).
- The reduced free-product and semicircular Fock realizations from those sections give \(H_n=H_0^{\bar\otimes(n+1)}\) by grouping according to the total semicircular degree.
  The current proof writes \(Y=L+L^*\) with \(L=XlX\), then computes the commutators with \(Y\) using the last-two-factor operator \(\tilde{R}\) and the lift \(\tilde{D}_X\) of the scalar dual \(D_X\) to the last factor. [Fixed model and construction](../../../../claims/Yin_C_F0012_v1.md#1-an-explicit-tracial-fock-model).

Searches on bounded dual systems, rank-one commutators and operator-valued semicircular Fock constructions found sources for the Fock model and the lift.
The inspected passages did not provide a bounded \(D_2\) with \([X,D_2]=0\) and \([Y,D_2]=P_\Omega\) for the sandwich with \(0\in\sigma(X)\).

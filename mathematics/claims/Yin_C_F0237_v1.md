---
author: Yin
---
# Column bounds on separated components of a normal spectrum, including complete closed curves

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X_1,\dots,X_d\) be bounded normal generators of a finite von Neumann algebra \(M\) with faithful normal probability trace \(\tau\), satisfying the [actual starred ACSY condition](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Fix \(X=X_i\), its prescribed derivation \(\delta=\delta_i\) on the represented starred core \(\mathcal P\), and put \(H=L^2(M)\), \(C=\mathrm{id}\otimes\tau\).
Suppose \(\sigma(X)=\bigcup_{a=1}^n K_a\) is a finite disjoint union of nonempty compact sets and put \(p_a=1_{K_a}(X)\).
Define the inner multiplier \(I_{v\otimes w}(s\otimes t)=sv\otimes wt\) and the localized right slices
\[
       E_{ab}=C I_{p_a\otimes p_b}\delta:\mathcal P\longrightarrow H.
\]
A map \(T:\mathcal P\to H\) has finite column cost if for some \(c<\infty\), for every finite column \(z_j\in\mathcal P\),
\[
              \sum_j\|Tz_j\|_2^2\le c^2\left\|\sum_jz_j^*z_j\right\|.
\]

1. Every \(E_{ab}\) with \(a\ne b\) has finite column cost.
2. The same conclusion holds for \(E_{aa}\) if \(K_a\) lies on a compact regular \(C^3\) embedded arc or on a regular simple closed \(C^3\) curve.
   An arc has an injective parametrization on a nondegenerate compact real interval, extending \(C^3\) past its endpoints with nonvanishing derivative on the interval.
   A closed curve has an injective \(C^3\) parametrization on the whole unit circle, with nonvanishing angular derivative.
   No smoothness is required on the other \(K_b\).
3. If every \(K_a\) satisfies item 2, the original \(c_i(X_1,\ldots,X_d)\) is finite and the canonical slice \(E_{i,0}=C\delta_i\) has \(M\Omega\subseteq\operatorname{Dom}\overline E_{i,0}\cap\operatorname{Dom}E_{i,0}^*\).
   Its negative closure supplies the strong commutator at coordinate \(i\).
   The other coordinates can have arbitrary spectra and joint correlations.
   If each coordinate has such a cover, \(\mathsf A\Rightarrow\mathsf S\) for the full tuple.

The constants concern a fixed finite separated partition.
The hypotheses allow a single component to contain an entire simple closed curve.

## Argument

### Two slice identities and the different-component terms

All tensor products of Hilbert spaces below are the completed coarse space with outer actions on the left of the first leg and right of the second.
When \(D\) is an outer derivation on a unital starred core \(\mathcal Q\) and \(L=CD\) obeys \(\|Lz\|_2\le B\|z\|\), it extends to the operator-norm closure of the core.
For \(z,w\in\mathcal Q\) and bounded \(v\), traciality and the product rule give
\[
              C I_{v\otimes w}Dz=L(zw)v-zL(w)v .                 \tag{1}
\]
For fixed \(z\) this remains true for every \(w\) in the norm closure, since the left side only multiplies \(Dz\) by \(w\).
Consequently its norm is bounded by \(2B\|v\|\|w\|\|z\|\).
Absolutely projectively summable series and Bochner integrals of such multipliers are allowed by this bound and continuity of the inner action on the coarse space.
Only the slice must extend in operator norm in this argument.

We use the same norm estimates both in \(M\) and after adjoining two jointly free Haar unitaries free from \(M\).
The enlarged tuple satisfies actual ACSY with the original derivation on old words by [the two-Haar enlargement](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words).
For each localized derivation \(I_{p_a\otimes p_b}\delta\), the enlarged derivation kills the two Haar generators and their adjoints.
Once a bound \(B_{ab}\) from operator norm to Hilbert norm for its slice on the enlarged core is established, [the free column encoding](Yin_C_F0208_v1.md#encoding-finite-columns-by-two-haar-unitaries) yields, for old words or polynomials \(z_j\),
\[
 \sum_j\|E_{ab}z_j\|_2^2
   =\left\|\widetilde E_{ab}\left(\sum_j u_jz_j\right)\right\|_2^2
   \le 4B_{ab}^2\left\|\sum_jz_j^*z_j\right\| .                 \tag{2}
\]
Here \(u_j=U^j VU^{-j}\) in the two new unitaries, and orthogonality follows by freeness because the old sliced vectors belong to \(H\).
The same \(\delta_i\) and all spectral projections on old inputs are retained.

Let \(D=I_{X\otimes1-1\otimes X}\delta\).
Its slice is bounded by [the liberation contraction calculation](Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions).
Indeed \(D\) has the values \(y\otimes1-1\otimes y\) at \(y=X,X^*\), and zero at the omitted starred generators by [the forced normal phase](Yin_C_F0076_v1.md#statement).
The twist \(iD\) is real, algebraic-valued and has the actual vacuum obtained by applying \(\delta^*\) to \(-i(X^*\otimes1-1\otimes X^*)\), as in that calculation.
These are exactly the hypotheses of its algebraic controlled-defect proof, also in the enlargement.
For \(a\ne b\) take smooth compact plane cutoffs \(\chi_a,\chi_b\) equal to the two projection indicators on the spectrum, with disjoint supports a positive distance apart.
The kernel \(\chi_a(z)\chi_b(w)/(z-w)\), continued by zero at the diagonal, is smooth with compact support on the product of the planes.
On periodizing it, three integrations with \(1-\Delta\) give Fourier coefficients \(O((1+|m|^2)^{-3})\) summable over \(\mathbb Z^4\).
Each Fourier character separates into two continuous functions of \(X\), in the norm closure of \(\mathcal P\).
Multiplying \(D\) by this projective kernel cancels \(z-w\) in the commuting marginal inner actions and gives \(I_{p_a\otimes p_b}\delta\).
Formula (1) on the enlarged core followed by (2) proves item 1.

### Actual localized derivations on a parameter core

Fix a good component \(K_a\), put \(p=p_a\), and write \(r\) for its parametrization on \(I\) or \(\mathbb T\), with \(h\) its inverse on the curve.
Let \(t\in pMp\) be the parameter \(h(X)p\), understood as zero off \(K_a\).
It is selfadjoint on an arc and a unitary in \(pMp\) on a closed curve.
In the latter case \(tt^*=t^*t=p\), which need not be central in \(M\).
Functions of the parameter on this component use the corner unit \(p\), so the constant function one denotes \(p\).
Use as mixed starred core \(\mathcal Q\) the algebra generated by \(p,t,X(1-p)\) and the original omitted coordinates, including the new Haar generators when working in the enlargement.
It generates the same von Neumann algebra because \(Xp=r(t)\) in the corner.

The projection \(p\), the complementary part \(X(1-p)\), and smooth functions of \(t\) with corner support have old-core approximants converging in operator norm together with their derivatives in coarse norm.
To see this, extend the parameter to the plane in local projection charts on the curve.
Projection in a nonorthogonal direction to the tangent is locally invertible on the parameter, with the endpoint extensions on an arc.
The local inverse on a circle takes its values in \(\mathbb T\subset\mathbb C\) on the curve.
Disjointness of the spectral components, compactness and injectivity permit finitely many charts and a partition of unity, followed by a cutoff equal to one on \(K_a\) and zero on the other components.
This extends each of the specified smooth scalar functions as a plane \(C^1\) function agreeing on the spectrum, as in [the compact arc chart argument](Yin_C_F0234_v1.md#parameters-on-disjoint-arcs).
Uniform approximation with first real derivatives on a containing rectangle by starred polynomials bounds the error of the marginal quotients \((f(z)-f(w))/(z-w)\) uniformly off the diagonal. [Smooth marginal graph approximation](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests)
The diagonal is null, and the forced phase gives exactly this derivative on marginal polynomials.
The closed graph of \(\delta\) gives the required limits, including for adjoints.
Products of these approximants preserve graph convergence by the product rule and uniform operator convergence of the factors.
Thus the entire mixed core is in the original closed domain with this product rule.

On the parameter space put \(J(s,v)=(r(s)-r(v))/(s-v)\), using \(r'\) on the real diagonal and \( (d/d\theta)r(e^{i\theta})/(i e^{i\theta})\) on the circle diagonal.
It is \(C^2\) and never zero on the compact parameter square.
In circle coordinates near the diagonal this follows by dividing the real angular divided differences of the numerator and of the exponential, whose diagonal derivative is nonzero.
Away from the diagonal, injectivity supplies nonvanishing.
Both \(J\) and \(K=1/J\) are used only in the corner tensor.
On the arc use the cutoff and periodic extensions in [the Fourier multiplier argument](Yin_C_F0137_v1.md#fourier-summability-needed-for-the-two-changes-of-coordinates).
On the circle the kernel \(K\) is already \(C^2\) on a two-torus.
Thus \(K\) has an absolutely summable separated Fourier expansion, using Parseval with second derivatives and \(\sum_{m,n}(1+m^2+n^2)^{-2}<\infty\).

For \(J\) one needs its actual tensor adjoint in the original graph.
For the real interval use the integrals of separated exponentials for the divided differences of the periodic extension of \(r\), whose one-dimensional coefficients satisfy \(\sum_n(1+n^2)|c_n|<\infty\).
For the circle expand \(r(s)=\sum_{n\in\mathbb Z}c_n s^n\) with the same weighted summability by Parseval for the third derivative and Cauchy–Schwarz.
For \(n>0\) the divided difference is a sum of \(n\) monomial tensors \(s^j v^{n-1-j}\), \(0\le j<n\).
For \(n=-m<0\) it is \(-\sum_{j=1}^m s^{-j}v^{-(m+1-j)}\).
The summands use the corner unit at exponent zero.
All exponential factors on the interval or powers on the circle, extended by zero to other components, have norm at most one.
Their original coarse derivative norms, and those of their adjoints, are bounded by \(C_0(1+|\alpha|)\) for frequency \(\alpha\).
On \(K_a^2\) the scalar difference quotient is bounded by \(|\alpha|\|K\|_\infty\), using exponential differences on the interval and \(|s^m-v^m|\le |m||s-v|\) on the circle.
Between components the denominator is bounded away from zero, and on the remaining square the numerator is zero.
The actual tensor-adjoint estimate for two such factors costs at most a constant times \(1+|\alpha|+|\gamma|+\|\xi_i\|_2\).
It follows by applying the vacuum pairing to products of their bounded graph approximants, as in [the tensor-adjoint estimate](Yin_C_F0137_v1.md#ax-implies-as-actual-adjoint-of-the-j-multiplier).
Each \(n\) therefore costs \(O((1+n^2)|c_n|)\) in the adjoint graph in either expansion, including the Bochner integrals on the interval.
Continuity of those integral factors in the adjoint graph follows by the same product estimate for their differences on bounded frequency intervals.
It follows by closedness that \(I_J^*(1\otimes1)\in\operatorname{Dom}\delta^*\).

On \(\mathcal Q\) put \(\theta=I_J\bar\delta\), using the kernel supported on \(p\otimes p\).
It has actual vacuum \(\delta^*(I_J^*(1\otimes1))\), kills \(p,X(1-p)\) and their adjoints, and kills all omitted starred coordinates.
Its value at \(t\) is \(p\otimes p\), since the localized derivative of \(t\) is \(K\) and \(JK=1\) on the parameter square.
On an arc this makes \(\theta\) real and algebraic-valued.
Its coassociativity follows because the iterated difference is an outer derivation that vanishes on every starred generator, using \(\theta p=0\).
The [real coassociative slice estimate](../audits/literature/Mai15/Yin_U002.md#mai15-u002) makes \(C\theta\) bounded from \(\mathcal Q\) in operator norm to \(H\).

### The partial-unitary calculation on the whole algebra

On the circle put \(u=t\).
Since \(\theta p=0\), differentiating \(u^*=pu^*p\) gives the outer support \(\theta u^*=p\cdot(\theta u^*)\cdot p\).
Differentiating \(uu^*=p\) and multiplying on the outer left by \(u^*\) now gives \(\theta u^*=-u^*\otimes u^*\).
Define \(\beta=i I_{u\otimes p}\theta\).
On \(u,u^*\) its values are \(iu\otimes p,-ip\otimes u^*\), respectively, and it kills the remaining starred generators of \(\mathcal Q\).
Hence it is real under flip-adjoint and has algebraic tensor values.
Its actual vacuum is \(\zeta=\theta^*(-i u^*\otimes p)\).
Indeed \(p,u\) and their adjoints belong to \(\mathcal Q\), so the two differentiated-factor terms in the tensor-adjoint product identity and the vacuum of \(\theta\) bound this functional on the Hilbert space.
Reality gives \(\zeta=\zeta^*\), and the same adjoint product argument makes \(\beta\) closable.

For \(\kappa_p(a\otimes b)=a\otimes p\otimes b\), the two sides of
\[
    (\beta\otimes\mathrm{id})\beta-(\mathrm{id}\otimes\beta)\beta
                       =i\kappa_p\beta                                  \tag{3}
\]
are outer derivations, since the mixed terms cancel.
On \(u,u^*\) they have values \(-u\otimes p\otimes p,\ p\otimes p\otimes u^*\), respectively, and both sides vanish on every other generator and adjoint.
Thus (3) holds on mixed words without a commutativity assumption on \(p\).
For \(T=C\beta\), contraction by \(\mathrm{id}\otimes\tau\otimes\tau\) gives
\[
       T^2z=C((\beta z)\cdot\zeta)+i\tau(p)Tz,\qquad
       T^*z=z\zeta-Tz\quad(z\in\mathcal Q).
\]
The second formula is the real tensor-adjoint product rule at \(z\otimes1\).
The [unitary energy calculation](Yin_C_F0043_v1.md#31-the-exact-defect-of-coassociativity), applied to these identities, gives
\[
 \|Tz\|_2^2=2\operatorname{Re}\langle Tz,z\zeta\rangle
      -\operatorname{Re}\langle\beta(z^*z),1\otimes\zeta\rangle
      -\operatorname{Re}\langle i\tau(p)Tz,z\rangle .
\]
Take a selfadjoint \(a\in\mathcal Q\) with \(\|a\|<1\).
The binomial expansions of \(z=a+i(1-a^2)^{1/2}\) and \(z^*\) converge in operator norm with convergent coarse derivatives, by the summable power-derivative bounds at this strict radius.
For either unitary the displayed identity passes to the limit with vanishing product derivative because \(z^*z=1\) and \(\beta\) is closable.
It follows that \(\|Tz\|_2\le2\|\zeta\|_2+\tau(p)\).
Averaging the two unitary tests, scaling, and decomposing into real and imaginary parts gives
\[
           \|Ta\|_2\le 2(2\|\zeta\|_2+\tau(p))\|a\|
                     \qquad(a\in\mathcal Q).
\]
The construction uses the unit of the full mixed algebra for the binomial test and the original probability trace throughout.
Since every \(\theta a\) has inner support \(Hp\otimes pH\), \(C\beta(a)=i(C\theta(a))u\), so \(C\theta(a)=-i(C\beta(a))u^*\).
This bounds \(C\theta\) in the closed-curve case as well.

### Recovering the localized derivative on the original starred core

Write \(L=C\theta\), which is operator-norm-to-Hilbert bounded on \(\mathcal Q\) in both cases.
Expand \(K=\sum_\ell c_\ell v_\ell\otimes w_\ell\) in the corner Fourier factors of norm at most one, with \(\sum_\ell|c_\ell|<\infty\).
Every \(w_\ell\) belongs to the norm closure of \(\mathcal Q\) by corner functional calculus.
Formula (1) gives on the mixed core
\[
 C I_K\theta(z)=\sum_\ell c_\ell\big(L(zw_\ell)v_\ell-zL(w_\ell)v_\ell\big),
 \qquad \|C I_K\theta(z)\|_2\le 2\|L\|\left(\sum_\ell|c_\ell|\right)\|z\|.
                                                               \tag{4}
\]
On \(\mathcal Q\), the actual tensor \(I_K\theta\) equals \(I_{p\otimes p}\bar\delta\) by the product of the marginal symbols.

To recover the same slice from (4) on each old word, replace its letters \(X,X^*\) by \(X(1-p)+r_n(t)\) and the adjoint expression, where \(r_n(t)\) uses the corner unit.
On an interval use complex polynomial approximation in \(C^1\) and on a circle use Laurent sums converging in \(C^1\).
These substitutions converge in operator norm.
On the marginal square of \(K_a\) their \(\delta\)-derivative errors are bounded by the parameter divided-difference error times \(\|K\|_\infty\).
For the circle the shortest angular distance is at most \(\pi/2\) times the chord distance, which gives uniform divided-difference control from \(C^1\) convergence, also for adjoints.
Across \(K_a\) and its complement the numerator error tends uniformly to zero and the denominator stays away from zero.
The error vanishes on the complementary square.
The omitted letters need no approximation.
Hence the product rule gives convergence in the old graph for the mixed approximants to each old word and each old polynomial.
Passing (4) through these limits gives the asserted operator-norm bound for \(C I_{p\otimes p}\delta\) on precisely the original core.
All steps apply in the free enlargement, and (2) now proves item 2.

If all components of the distinguished spectrum satisfy item 2, the finite sum of the \(E_{ab}\) is \(C\delta_i\), so its column cost is finite by the triangle inequality for a Hilbert direct sum.
The adjoint tuple also satisfies actual ACSY, with the flip-adjoint conjugate derivations and the conjugated carriers. [Normal phase and companion](Yin_C_F0076_v1.md#statement)
The right slice for its coordinate bounds the original left slice by tracial involution.
The [two-slice domain theorem](Yin_C_F0072_v1.md#statement), Part B, therefore supplies both actual bounded-vector domains for the canonical original operator.
On its algebraic graph the commutator at each generator is bounded, equal to \(\delta_{ij}P_\Omega\) in operator-first order.
Taking graph approximants shows that left generator multiplication preserves the closed domain and the identity holds there.
Thus \(-\overline E_{i,0}\) provides the strong witness at \(i\), proving item 3.

## Scope and provenance

The coordinating agent developed the [different-component localization](../drafts/Yin_D_F0002.md#localization-between-separated-spectral-components), including the multiplier calculation before the right trace.
The check_defect agent for Yin developed the same-component parameter argument with the coordinating agent's proposed partial-unitary defect and checked its transfer to the original mixed starred words.
This extends the [finite arc calculation](Yin_C_F0234_v1.md#statement) to complete closed components.
The older [single analytic closed-curve result](Yin_C_F0043_v1.md#statement) supplies the unitary energy argument at its original scope.
Intersecting carriers without a separated spectral partition and accumulations of infinitely many components are outside this argument.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T10:06 |
| status | open |
| reason | The localization, partial-unitary energy calculation and original column estimates are fixed for whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Different-component and good same-component column bounds, distinguished canonical full domains, and the sufficient strong-system consequence. |
| argument | [Argument](#argument) | Liberation localization, actual arc and closed-curve parameter vacua, partial-unitary defect, projective recorrection, original-core approximation and two-Haar recovery. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#statement) | Part 1, actual closability and diffuse marginal, starred values including omitted coordinates, and conjugate companions. |
| dependency | [Liberation slice](Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions) | Algebraic liberation, its actual vacuum and bounded right slice in an actual normal ACSY algebra. |
| dependency | [Free enlarged vacuum](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Extension of all actual old-coordinate values to the free product and zero derivative on new Haar factors. |
| dependency | [Finite column encoding](Yin_C_F0208_v1.md#encoding-finite-columns-by-two-haar-unitaries) | Free-conjugate unitary words, their norm bound and orthogonality of old Hilbert-valued outputs. |
| dependency | [Arc parameter charts](Yin_C_F0234_v1.md#parameters-on-disjoint-arcs) | Local inverse, endpoint extension and separated cutoffs for parameter values on the spectrum. |
| dependency | [Marginal smooth approximation](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) | Uniform bivariate polynomial approximation including first derivatives. |
| dependency | [Fourier expansions](Yin_C_F0137_v1.md#fourier-summability-needed-for-the-two-changes-of-coordinates) | Weighted Fourier expansion for one-dimensional divided differences and absolute summability for two-dimensional \(C^2\) multipliers. |
| dependency | [Actual tensor adjoint](Yin_C_F0137_v1.md#ax-implies-as-actual-adjoint-of-the-j-multiplier) | Tensor-adjoint bound on bounded graph-approximable factors and passage through convergent graph expansions. |
| dependency | [Real coassociative estimate](../audits/literature/Mai15/Yin_U002.md#mai15-u002) | Theorem 4.9 on the weakly dense real, algebraic-valued arc parameter core. |
| dependency | [Unitary energy identity](Yin_C_F0043_v1.md#31-the-exact-defect-of-coassociativity) | Adjoint-product calculation of equations (12)–(13), with the changed defect scalar computed in (3). |
| dependency | [Two-slice domains](Yin_C_F0072_v1.md#statement) | Part B, actual original closure and adjoint containing the bounded vectors under the two core bounds. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T10:25 |
| status | proved |
| reason | Adopt the separated-component estimates and original full domains after the independent full-core and partial-unitary calculation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Different-component and good same-component column bounds, distinguished canonical full domains, and the sufficient strong-system consequence. |
| argument | [Argument](#argument) | Liberation localization, actual arc and closed-curve parameter vacua, partial-unitary defect, projective recorrection, original-core approximation and two-Haar recovery. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#statement) | Part 1, actual closability and diffuse marginal, starred values including omitted coordinates, and conjugate companions. |
| dependency | [Liberation slice](Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions) | Algebraic liberation, its actual vacuum and bounded right slice in an actual normal ACSY algebra. |
| dependency | [Free enlarged vacuum](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Extension of all actual old-coordinate values to the free product and zero derivative on new Haar factors. |
| dependency | [Finite column encoding](Yin_C_F0208_v1.md#encoding-finite-columns-by-two-haar-unitaries) | Free-conjugate unitary words, their norm bound and orthogonality of old Hilbert-valued outputs. |
| dependency | [Arc parameter charts](Yin_C_F0234_v1.md#parameters-on-disjoint-arcs) | Local inverse, endpoint extension and separated cutoffs for parameter values on the spectrum. |
| dependency | [Marginal smooth approximation](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) | Uniform bivariate polynomial approximation including first derivatives. |
| dependency | [Fourier expansions](Yin_C_F0137_v1.md#fourier-summability-needed-for-the-two-changes-of-coordinates) | Weighted Fourier expansion for one-dimensional divided differences and absolute summability for two-dimensional \(C^2\) multipliers. |
| dependency | [Actual tensor adjoint](Yin_C_F0137_v1.md#ax-implies-as-actual-adjoint-of-the-j-multiplier) | Tensor-adjoint bound on bounded graph-approximable factors and passage through convergent graph expansions. |
| dependency | [Real coassociative estimate](../audits/literature/Mai15/Yin_U002.md#mai15-u002) | Theorem 4.9 on the weakly dense real, algebraic-valued arc parameter core. |
| dependency | [Unitary energy identity](Yin_C_F0043_v1.md#31-the-exact-defect-of-coassociativity) | Adjoint-product calculation of equations (12)–(13), with the changed defect scalar computed in (3). |
| dependency | [Two-slice domains](Yin_C_F0072_v1.md#statement) | Part B, actual original closure and adjoint containing the bounded vectors under the two core bounds. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0246_v1.md#whole-proof-finding) | Both types of same-component bounds, all cross-component bounds, the projection defect, original column and both canonical domains. |

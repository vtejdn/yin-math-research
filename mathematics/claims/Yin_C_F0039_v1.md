---
author: Yin
---

# Projective normal spectral phases give automatic adjoint modules; analytic arcs

## Current assessment
[Selected decision](#decision-isolated-current-review-20261022)

## Automatic Adjoint Modules from Normal Spectral Phases

<a id="statement"></a>

Date: 2026-09-11.
Human author: Yin.
Proof development: another AI agent.
Authorization: the normal-domain investigation autonomous domain reduction; root allocated Yin_C_F0039 and requested the general projective-phase statement with selfadjoint/unitary instances.
Record kind: new Claim/proof module and a continuation checkpoint.

The original [Yin_C_F0038](Yin_C_F0038_v1.md#yin_c_f0038) selfadjoint proof remains unchanged.
A preliminary mixed-coordinate draft was broadened to the present general sufficient condition before independent review or Claim-index selection.
The present file is the complete candidate; no reviewed prior Yin_C_F0039 proof is being replaced.

<a id="yin_c_f0039"></a>
## Yin_C_F0039: A Summable Conjugate Spectral Phase Gives an Adjoint Module

Provenance: project deduction from Yin_C_F0038's L1 method, Yin_C_F0037's automatic normal-generator commutators, and Yin_C_F0018's right-multiplier tensor action.
Mathematical assessment at authorship: proof draft; complete candidate below.
Review assessment at authorship: self-reviewed; independent review pending.
Current candidate proof: [yin_c_f0039-p1](#yin_c_f0039-p1).

Let \((\mathcal M,\tau)\) be finite tracial with faithful normal probability trace, \(H=L^2(\mathcal M,\tau)\), \(\Omega=1\), and \(P=P_\Omega\).
The inner product is linear in its second variable.
Let \(X=(X_1,\ldots,X_d)\) be bounded normal generators of \(\mathcal M\), and suppose closable maps \(D_{i,0}:\mathcal M\to H\), with domain exactly the bounded vectors, satisfy
\[
[D_{i,0},X_j]a=\delta_{ij}Pa\qquad(a\in\mathcal M).
\tag{47.1}
\]
A bounded reference dual and invariant test spaces in the adjoint domains are not assumed.

Let \(\mu_i\) be the spectral distribution of \(X_i\), and put \(B_i=W^*(X_i)\).
By Yin_C_F0037 these distributions are nonatomic.
On their product spaces define
\[
k_i(z,w)=\frac{\bar z-\bar w}{z-w}\quad(z\ne w),
\qquad k_i(z,z)=0.
\]
Assume, for each \(i\), that there are \(a_{in},b_{in}\in B_i\), \(n\geq1\), such that
\[
\sum_n\|a_{in}\|\|b_{in}\|<\infty,
\qquad
\sum_n a_{in}(z)b_{in}(w)=\overline{k_i(z,w)}
\quad\text{for }\mu_i\otimes\mu_i\text{-almost every }(z,w).
\tag{47.2}
\]
This is an explicit lift of the conjugate phase to the Banach projective tensor product \(B_i\widehat\otimes_\pi B_i\).
It is not asserted to follow from boundedness of the measurable phase, and no injectivity of the map from that completion to measurable kernels is assumed.
Fix one expansion in (47.2).

Write \(\rho(b)\xi=\xi b\) and define on \(\mathcal M\)
\[
Q_{i,0}(a)=\sum_n\rho(a_{in})D_{i,0}(a b_{in}).
\tag{47.3}
\]
This series converges in \(H\).
Set
\[
\eta_i=D_{i,0}\Omega,\quad \nu_i=Q_{i,0}\Omega,
\qquad
D_{i,0}^0(a)=D_{i,0}(a)-a\eta_i,
\quad Q_{i,0}^0(a)=Q_{i,0}(a)-a\nu_i.
\]
There is \(\xi_i\in L^1(\mathcal M,\tau)\), not required to be selfadjoint, such that
\[
\tau(D_{i,0}^0a)=\tau(\xi_i a)\qquad(a\in\mathcal M).
\tag{47.4}
\]
Every \(p\in\mathcal M\) satisfying \(p\xi_i^*\in H\) belongs to \(\operatorname{Dom}D_{i,0}^*\), with
\[
D_{i,0}^*p=p\xi_i^*-Q_{i,0}^0p+p\eta_i^*.
\tag{47.5}
\]
Consequently
\[
h_i=(1+\xi_i^*\xi_i)^{-1/2}\in\mathcal M
\tag{47.6}
\]
is regular and \(\mathcal M h_i\) is a dense left module in the adjoint domain.
All conclusions of Yin_C_F0029/Yin_C_F0030 therefore hold with no separate adjoint-module premise.
In particular, for fractions \(u=s^{-1}a=bt^{-1}\in L^0(\mathcal M)\) with \(s,a,b,t\in\mathcal M\) and regular \(s,t\),
\[
u\in\operatorname{Div}_{L^0(\mathcal M)}\mathbb C\langle X\rangle
\quad\Longleftrightarrow\quad
\operatorname{rank}\bigl(sD_{i,0}b-aD_{i,0}t\bigr)|_{\mathcal M}<\infty
\quad\text{for every }i.
\tag{47.7}
\]
The algebra in this conclusion does not silently include generator adjoints.
No L2 assertion about \(\xi_i\), finite Fisher information, or vacuum membership in the adjoint domains is made.

### Explicit Normal Instances

Condition (47.2) holds whenever each coordinate is selfadjoint or unitary, with arbitrary mixtures.
For a selfadjoint coordinate \(\overline{k_i}=1\) almost everywhere, so one can choose \(Q_{i,0}=D_{i,0}\).
For a unitary coordinate,
\[
\overline{k_i(z,w)}=-zw,
\qquad Q_{i,0}=-\rho(X_i)D_{i,0}\rho(X_i).
\tag{47.8}
\]
Thus Haar coordinates are included without assuming a bounded reference dual.

More generally, (47.2) holds if each normal coordinate has spectrum contained in an affine real line or a circle of positive radius.
Indeed, for \(X_i=\alpha_iY_i+\beta_i1\), \(\alpha_i\ne0\), with \(Y_i\) selfadjoint or unitary, the conjugate phase is \((\alpha_i/\bar\alpha_i)\overline{k_{Y_i}}\), still an elementary tensor.
These are direct source-free substitutions into (47.2), not a separate main-theorem designation.

It also holds for each coordinate of the form \(X_i=r_i(S_i)\), where \(S_i\) is selfadjoint with spectrum in a compact real interval \(I_i\), and \(r_i\) is holomorphic on a neighborhood of \(I_i\), injective on \(I_i\), and has nonzero derivative everywhere on \(I_i\).
The [analytic-arc verification](#analytic-arc-application) below proves the exact phase hypothesis.
The coordinates need not be free.
For example, \(r_i(t)=t+\mathrm i\varepsilon_i t^2\), with any real \(\varepsilon_i\), supplies noncircular normal spectral arcs.
The dual and all-bounded-vector domain assumptions remain required; this geometric condition does not itself construct such duals.

### Reuse Check and Dependencies

[Yin_C_F0038-P1](Yin_C_F0038_v1.md#yin_c_f0038-p1) constructs L1 densities from closability and an all-\(\mathcal M\) domain before using selfadjointness.
The [AP18 L1 interface](../audits/literature/AP18/Yin_U003_v1.md#l1-predual-interface) supplies completeness, the norm identity and normal pairing.
[Yin_C_F0037-P1](Yin_C_F0037_v1.md#yin_c_f0037-p1) supplies atomlessness and the actual Hilbert-Schmidt starred commutators, without (47.2) or an adjoint module.
[Yin_C_F0018 Section 1](Yin_C_F0018_v1.md#1-algebra-norms-and-the-correction-lemma) gives the projective norm and the exact right-multiplier action; its bounded-operator mechanism is adapted below to a bounded map from operator norm to Hilbert norm.
The Hilbert-Schmidt/tensor correspondence is the accepted [Yin_C_F0025 convention](Yin_C_F0025_v1.md#yin_c_f0025).
The final criterion uses [Yin_C_F0029-P2](Yin_C_F0029_v1.md#yin_c_f0029-p2).

These checked local interfaces supply the needed mechanisms, so no additional primary-source search is required before this proof.
No general operator-norm bound for a normal double-operator-integral phase is imported.
The new point is the explicit use of (47.2) to construct the flipped-adjoint derivative with a controlled action on all bounded vectors.

<a id="yin_c_f0039-p1"></a>
### Proof yin_c_f0039-p1

Closed graph gives \(c_i=\|D_{i,0}\|_{\infty\to2}<\infty\).
For (47.3),
\[
\|\rho(a_{in})D_{i,0}(a b_{in})\|_2
\leq c_i\|a\|\|a_{in}\|\|b_{in}\|.
\]
Thus the series defines a bounded map \((\mathcal M,\|\cdot\|)\to H\), with norm at most \(c_i\sum_n\|a_{in}\|\|b_{in}\|\).
This assertion does not require the resulting map \(Q_{i,0}\) to be closable as a Hilbert-space operator.

On uniformly operator-norm-bounded strongly convergent nets \(a_\alpha\to a\), the outputs \(D_{i,0}a_\alpha\) converge weakly: test against its dense adjoint domain and extend from those tests by the uniform bound.
For each fixed \(n\), right multiplication of the input by \(b_{in}\) preserves bounded strong convergence, and the bounded right output multiplier preserves weak convergence.
Summability gives a uniform tail bound on (47.3), so \(Q_{i,0}a_\alpha\rightharpoonup Q_{i,0}a\) as well.
Subtracting the vacuum right multipliers preserves this property for both normalized maps.

The construction of (47.4) is precisely the part of Yin_C_F0038 that used no selfadjointness.
Choose \(v_n\in\operatorname{Dom}D_{i,0}^*\) with \(v_n\to\Omega\).
The functionals with L2 densities \((D_{i,0}^*v_n)^*\) satisfy
\[
\|\tau_{(D_{i,0}^*v_n)^*}-\tau_{(D_{i,0}^*v_m)^*}\|
\leq c_i\|v_n-v_m\|_2.
\]
L1 norm equality and completeness produce a density representing \(a\mapsto\tau(D_{i,0}a)\); subtract \(\eta_i\) to obtain \(\xi_i\).
There is no reality assertion about this density.

Use the Hilbert-Schmidt identification
\[
\Theta(g\otimes h)\zeta=g\langle Jh,\zeta\rangle,
\]
extended isometrically from \(H\widehat\otimes H\).
Yin_C_F0037 gives
\[
[D_{i,0},X_j^*]=\delta_{ij}K_j,
\qquad K_j=\Theta(k_j).
\tag{47.9}
\]
Right multipliers commute with all bounded left coordinates.
Moreover
\[
\rho(a)\Theta(g\otimes h)\rho(b)=\Theta(ga\otimes bh).
\tag{47.10}
\]
This identity follows by traciality in the input scalar and fixes both multiplication orders.

For the unstarred coordinates, (47.1), (47.2) and the norm-convergent series give
\[
[Q_{i,0},X_j]
=\delta_{ij}\Theta(\overline{k_i})
=\delta_{ij}K_i^*.
\tag{47.11}
\]
The second equality uses symmetry \(k_i(z,w)=k_i(w,z)\); under \(\Theta\), operator adjoint is tensor-leg flip followed by star.
For starred coordinates, (47.9)-(47.10) and the fact that all coefficients lie in the same abelian \(B_i\) give
\[
[Q_{i,0},X_j^*]
=\delta_{ij}\Theta\left(k_i(z,w)\sum_n a_{in}(z)b_{in}(w)\right)
=\delta_{ij}P.
\tag{47.12}
\]
Here the series converges in Hilbert-Schmidt norm, bounded by \(\|K_i\|_{\mathrm{HS}}\sum_n\|a_{in}\|\|b_{in}\|\).
Atomlessness from Yin_C_F0037 makes the diagonal null, so \(k_i\overline{k_i}=1\) almost everywhere.
These calculations never multiply an arbitrary left coordinate through the right-tensor coefficients.

Let \(\mathcal P=\mathbb C\langle X,X^*\rangle\).
By the word product rule and (47.9), every \([D_{i,0},a]\), \(a\in\mathcal P\), has a bounded Hilbert-Schmidt representative.
Define the actual evaluated derivation
\[
\partial_i a=\Theta^{-1}([D_{i,0},a]),
\qquad
\partial_i^\dagger a=\operatorname{flip}\bigl((\partial_i(a^*))^*\bigr).
\tag{47.13}
\]
It is representation independent by injectivity of \(\Theta\); no algebraic-freeness assumption is needed to define it this way.
The first map is a derivation for the outer bimodule actions, and star together with flip makes the second a complex-linear derivation for those same actions.
Their target here is the completed Hilbert tensor product, not necessarily its algebraic finite-rank subspace.

On the generators, \(\partial_i^\dagger X_j=\delta_{ij}\overline{k_i}\) and \(\partial_i^\dagger X_j^*=\delta_{ij}1\otimes1\).
Equations (47.11)-(47.12) and the product rule show that \(Q_{i,0}\) implements exactly this derivation.
Applying the two commutators to the vacuum, with the correct normalization, yields
\[
D_{i,0}^0a=(\mathrm{id}\otimes\tau)(\partial_i a),
\qquad
Q_{i,0}^0a=(\mathrm{id}\otimes\tau)(\partial_i^\dagger a)
\qquad(a\in\mathcal P).
\tag{47.14}
\]
Both contractions are bounded on the Hilbert tensor product.

For \(p,q\in\mathcal P\), (47.4) and the product rule give
\[
\tau(\xi_i p^*q)
=\tau(D_{i,0}^0(p^*q))
=\tau((Q_{i,0}^0p)^*q)+\tau(p^*D_{i,0}^0q).
\tag{47.15}
\]
Indeed the first-leg contraction of \(\partial_i(p^*)\) is \((Q_{i,0}^0p)^*\) by (47.13)-(47.14).
The tensor calculation can first be checked on finite tensors and then passed to the Hilbert completion through these bounded contractions and bounded outer multipliers.
Replacing \(Q_{i,0}^0\) by \(D_{i,0}^0\) here would generally be wrong for a normal coordinate.

Kaplansky density applies to \(\mathcal P\).
First approximate \(q\) and then \(p\) by uniformly bounded polynomials converging strongly together with their adjoints.
The weak continuity of the normalized maps, the normal L1 pairings and the other strongly convergent Hilbert factors extend (47.15) to all \(p,q\in\mathcal M\).
Successive limits avoid a weak-weak pairing.
If \(p\xi_i^*\in H\), then
\[
\langle p,D_{i,0}^0q\rangle
=\langle p\xi_i^*-Q_{i,0}^0p,q\rangle.
\]
Adding the vacuum right multiplier proves (47.5) on the entire actual domain \(\mathcal M\).

Write \(\xi_i=v_i|\xi_i|\).
The polar decomposition gives
\[
h_i\xi_i^*
=(1+|\xi_i|^2)^{-1/2}|\xi_i|v_i^*\in\mathcal M.
\]
The element \(h_i\) is positive and regular, so \(\mathcal M h_i\) is a dense left module, and every one of its elements satisfies (47.5).
This supplies exactly the missing Yin_C_F0029 adjoint hypothesis and proves (47.7), together with the other stated Yin_C_F0029 consequences.

Finally, the explicit selfadjoint, unitary and affine-line/circle instances follow from the phase calculations already displayed.
In the unitary case (47.12) can also be checked directly from \([D_{i,0},X_i^*]=-X_i^*PX_i^*\), using traciality \(\tau(X_i^*aX_i)=\tau(a)\).
This verifies the sign in (47.8).

<a id="analytic-arc-application"></a>
### Verification for Analytic Embedded Arcs

This is a verification of the existing condition (47.2), using ordinary Taylor expansions and Cauchy coefficient estimates; no further unbounded-operator input or new project Claim is needed.

Fix a compact interval \(I\), a selfadjoint \(S\) with spectrum in \(I\), and \(X=r(S)\) under the conditions stated above.
Since \(r|_I\) is a continuous injection of a compact space, it is a homeomorphism onto its image.
Consequently \(S=(r|_I)^{-1}(X)\) by continuous functional calculus, and
\[
W^*(S)=W^*(X).
\tag{47.16}
\]
In particular bounded Borel functions of \(S\) are allowable coefficients in (47.2).

Put \(r^\#(z)=\overline{r(\bar z)}\), holomorphic on a possibly smaller common neighborhood of \(I\).
Define the holomorphic divided differences
\[
G_r(z,w)=\begin{cases}
\dfrac{r(z)-r(w)}{z-w},&z\ne w,\\
r'(z),&z=w,
\end{cases}
\qquad G_{r^\#}\text{ analogously}.
\]
The diagonal extension is jointly holomorphic, as follows from the ordinary local Taylor series.
Injectivity on \(I\) and \(r'(t)\ne0\) show that \(G_{r^\#}\) has no zero on \(I^2\).
Compactness therefore gives an open complex neighborhood of \(I^2\) on which
\[
F(z,w)=\frac{G_r(z,w)}{G_{r^\#}(z,w)}
\tag{47.17}
\]
is holomorphic.
For distinct real \(t,s\in I\),
\[
F(t,s)=\frac{r(t)-r(s)}{\overline{r(t)}-\overline{r(s)}}
=\overline{k_X(r(t),r(s))}.
\tag{47.18}
\]
The formula's continuous diagonal value need not equal the convention \(k_X(z,z)=0\).
This is immaterial because Yin_C_F0037 supplies a nonatomic spectral law, so the diagonal has product measure zero.

Choose \(R>0\) so small that every closed polydisk with center in \(I^2\) and radius \(2R\) in each coordinate lies in that holomorphic neighborhood.
Such one common radius exists by compactness; thus a single fine partition works for every pair of cells.
The union of these closed polydisks is compact, so \(|F|\) has a finite uniform bound \(M_F\) there.

Partition \(I\) into finitely many disjoint Borel intervals \(I_1,\ldots,I_N\) of diameter at most \(R/2\), and choose \(c_j\in I_j\).
Around every \((c_j,c_k)\), Taylor expansion and Cauchy's estimate on the radius-\(R\) polydisk give
\[
F(t,s)=\sum_{m,n\geq0}\gamma_{mn}^{jk}(t-c_j)^m(s-c_k)^n,
\qquad
|\gamma_{mn}^{jk}|\leq M_F R^{-m-n}.
\]
Multiply the two leg functions by the corresponding interval indicators.
For
\[
a_{jkmn}(t)=\gamma_{mn}^{jk}1_{I_j}(t)(t-c_j)^m,
\qquad b_{jkmn}(s)=1_{I_k}(s)(s-c_k)^n,
\]
their norm products are bounded by \(M_F2^{-m-n}\).
Thus
\[
\sum_{j,k=1}^N\sum_{m,n\geq0}
\|a_{jkmn}\|_\infty\|b_{jkmn}\|_\infty
\leq4M_FN^2<\infty.
\tag{47.19}
\]
The sums reconstruct \(F\) on each rectangle and hence on all of \(I^2\).
Evaluate these functions at \(S\), use (47.16) to regard them as elements of \(W^*(X)\), and use (47.18) off the null diagonal.
This is precisely the expansion required in (47.2).

For the indicated parabola, \(r(t)=t+\mathrm i\varepsilon t^2\) is entire, its real part on the real axis is \(t\), and \(r'(t)=1+2\mathrm i\varepsilon t\) never vanishes there.
It meets all the hypotheses for every real \(\varepsilon\), with no smallness restriction.

## Self-Review and Continuation

The author checked the all-bounded-vector norm and weak-continuity bounds for the infinite series, the side and order of both right multipliers, the non-selfadjoint L1 density, the Hilbert-Schmidt product with the spectral phase, the flipped-adjoint derivation rule on the completed tensor product, both vacuum normalizations, the sequential approximation limits, and the polar-decomposition damping orientation.
The analytic-arc check additionally covers the nonvanishing denominator on the full real square, a common complex radius for every partition rectangle, the summable Cauchy bounds and the null-diagonal convention.
No independent review, computation, formal verification, external human review or novelty assessment is claimed at authorship.

The principal remaining questions are whether (47.2) can be replaced by a weaker multiplier condition, whether nonsmooth or two-dimensional normal spectral sets satisfy a suitable substitute, and whether the all-\(\mathcal M\) dual domain can simultaneously be reduced to an arbitrary dense left module.
Analytic embedded arcs are now a proved application at the exact assumptions above.
A bounded measurable phase and a Hilbert-Schmidt kernel alone do not establish the required projective lift.
The theorem does not assert that lift for arbitrary normal spectra.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:05 |
| status | proved |
| reason | Adopt the exact actual original finding and disclosed unknown initial-context relationship, preserving the mathematical assessment, fixed statement and argument, dependencies and historical decisions. No new review or mathematical proof version is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0039-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0073_v1.md#general-proof-checks) | Entire C_F0039 projective-phase theorem, exact original coefficients, full proof and separately checked analytic embedded-arc application. Actual original finding with unknown initial-context arrangement; historical date and accepted-input depth unchanged. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the separate isolated current finding on the unchanged fixed statement and proof, with exact conditions and scope. Preserve historical findings, relationships, source depths and dates; no new mathematical proof version is introduced. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0039-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0073_v1.md#current-isolated-finding) | Entire C_F0039 projective-phase theorem, exact original coefficients, full proof and separately checked analytic embedded-arc application. |

## Historical assessments


These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0039-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0073_v1.md#general-proof-checks) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0073_v1.md#general-proof-checks).

Material covered by that review: [Exact material](Yin_C_F0039_v1.md).

---
author: Yin
---

# Nonnegative bounded densities preserve original normal-core domains and the free-tuple criterion

## Current assessment
[Selected decision](#decision-finding-owned-applicability)

## Nonnegative bounded densities and the original normal polynomial core

<a id="statement"></a>

Kind: Claim / proof module.
Date: 2026-09-16.
Human record author: Yin.
A Codex research agent developed the argument following the coordinator's proposed zero-set continuation and removal of the unused angular normalization.
Consumer: the separate normal-domain investigation, Q3.

<a id="nonnegative-density-normal-core-transfer"></a>

This is a scope extension beyond the strictly positive, independently reviewed result in [C_F0051 v1 at recorded assessment 2](Yin_C_F0051_v1.md#decision-candidate-0002).
That artifact is unchanged and is cited for comparison, not as a proof premise.
No necessity result or unrestricted completion of the normal-domain investigation is asserted.
## 1. Statement, source reuse and the changed hypothesis

Let sigma be a probability on (0,R], R finite, and let
\[
 d\nu(re^{i\theta})=d\sigma(r)\,\frac{d\theta}{2\pi},\qquad
 A(r)=\frac{\sigma((0,r))+\sigma(\{r\})/2}{r}\in L^2(\sigma).
                                                               \tag{1}
\]
Let b be merely measurable with
\[
 0\le b\le B<\infty\quad\nu\text{-a.e.},\qquad
 \int b\,d\nu=1,
 \qquad d\mu=b\,d\nu.                            \tag{2}
\]
In contrast to C_F0051 v1 at recorded assessment 2, b may vanish on a set of positive nu-measure, and its angular mean need not be one at each radius.
The measure sigma is the radius law of the reference nu; it need not be the radius law of mu.
More explicitly the latter is bar b(r) d sigma(r), where bar b(r) is the angular mean of b.
The global normalization in (2) makes mu a probability, and no comparison with mu's own radial midpoint is asserted.
We use only mu<<nu and ||h||_(L2(mu))<=sqrt(B)||h||_(L2(nu)); null sets and essential sup norms are **not** identified.

For lambda=nu,mu, define the canonical core on the represented starred polynomials P_lambda=C[z,bar z] in H_lambda=L2(lambda) by
\[
 e_{\lambda,0}p(z)=\int\frac{p(z)-p(w)}{z-w}\,d\lambda(w).
                                                               \tag{3}
\]
Inner products are linear in the second variable and J denotes complex conjugation.
Then the conclusion is that e_(mu,0) is closable and its original closure E_mu and actual adjoint E_mu* satisfy
\[
 L^\infty(\mu)\subseteq\operatorname{Dom}E_\mu
                     \cap\operatorname{Dom}E_\mu^*.             \tag{4}
\]
Put
\[
 c_{\rm rad}=(1+\sqrt5)/\sqrt3,\quad
 a_\nu=2c_{\rm rad}\|A\|_{L^2(\sigma)},\quad
 a_\mu=2B^{3/2}a_\nu,\quad
 \xi_\nu(re^{i\theta})=2e^{i\theta}A(r).
\]
The actual mu vacuum vector is
\[
 \xi_\mu=E_\nu^*b-JE_\nu b=b\xi_\nu-2JE_\nu b
                    \quad\text{as an }L^2(\mu)\text{ class}.   \tag{5}
\]
For every f in L-infinity(mu), choose a nu-measurable representative on S={b>0} and extend it by zero to S-complement; call it tilde f.
Then
\[
 \begin{split}
 E_\mu f&=\bigl(E_\nu(b\widetilde f)
                    -\widetilde f E_\nu b\bigr)|_\mu,\\
 E_\mu^*f&=f\xi_\mu-JE_\mu Jf,\\
 \|E_\mu f\|_{L^2(\mu)}&\le a_\mu\|f\|_{L^\infty(\mu)},\\
 \|E_\mu^*f\|_{L^2(\mu)}
 &\le(a_\mu+\|\xi_\mu\|_{L^2(\mu)})\|f\|_{L^\infty(\mu)}.
 \end{split}                                                     \tag{6}
\]
The notation |_mu means the continuous restriction map L2(nu)->L2(mu).
This statement never identifies the two Hilbert adjoints.

Knowledge reuse: [C_F0047](Yin_C_F0047_v1.md) gives the actual radial domains, estimate, and bounded-function adjoint identity.
The transfer calculation of [C_F0048](Yin_C_F0048_v1.md), checked in its [independent review](../audits/reviews/Yin_R_F0022_v1.md), already supplies the density pairing mechanism without division by b.
C_F0048/C_F0049's written assumptions are uniformly positive; the independently reviewed C_F0051 v1 at recorded assessment 2 is strictly positive without a lower bound.
Those statements also retain angular mean one.
None states the present zero-set extension with only total-mass normalization.
The new step is to recover the intrinsic mu sup-norm estimate through zero extension and uniqueness of the original closed graph.
The angular-mean identity plays no role in the forward pairing, estimates, or graph recovery below; only the probability normalization is needed.
We reuse [C_F0045](Yin_C_F0045_v1.md), [C_F0025](Yin_C_F0025_v1.md) and [C_F0024](Yin_C_F0024_v1.md) only after that step.
Their existing source interfaces suffice; no new external theorem or source search is needed.
C_F0051 v1 at recorded assessment 2 is an independently reviewed comparison of scope, not an additional proof premise here.

## 2. The represented core and the actual vacuum vector

Both measures are compactly supported nonatomic probabilities.
Nonatomicity follows from the angular Haar measure for nu and absolute continuity for mu; radial atoms cause no problem.
The polynomial divided difference is bounded off the null diagonal.
If p=0 mu-almost everywhere, then p(z)-p(w)=0 for mu tensor mu-almost every pair.
Fubini therefore gives e_(mu,0)p=0 mu-almost everywhere.
Thus (3) is well-defined on **represented** P_mu even if it has more relations than P_nu.
These polynomials are dense in H_mu by compact support, continuous-function density, and Stone-Weierstrass.

C_F0047 gives all bounded nu-functions in the original E_nu and E_nu* domains, with
\[
 \|E_\nu h\|_{L^2(\nu)}\le a_\nu\|h\|_{L^\infty(\nu)},
 \qquad E_\nu^*h=h\xi_\nu-JE_\nu Jh.             \tag{7}
\]
In particular b and bp belong to those domains.
The polynomial commutator K_(nu,p) has bounded kernel (p(z)-p(w))/(z-w).
Taking graph approximants in the original radial core proves
\[
 E_\nu(ph)-pE_\nu h=K_{\nu,p}h
       \quad(h\in\operatorname{Dom}E_\nu).
\]
For h=b this gives the exact identity, interpreted in H_mu,
\[
 e_{\mu,0}p=E_\nu(pb)-pE_\nu b.                  \tag{8}
\]
Hence the **initial** bound is only
\[
 \|e_{\mu,0}p\|_{L^2(\mu)}
       \le a_\mu\|p\|_{L^\infty(\nu)}.          \tag{9}
\]
It is not yet the marginal input needed by C_F0045.

Using b in the actual radial adjoint domain, pair (8) to obtain
\[
 \begin{split}
 \int e_{\mu,0}p\,d\mu
 &=\langle b,E_\nu(pb)\rangle_\nu
                          -\int bpE_\nu b\,d\nu\\
 &=\int\bigl(\overline{E_\nu^*b}-E_\nu b\bigr)p\,d\mu.
 \end{split}                                                     \tag{10}
\]
No inverse density enters this calculation.
The vector in (5) is in L2(mu), with
\[
 \|\xi_\mu\|_{L^2(\mu)}
 \le B^{3/2}\bigl(\|\xi_\nu\|_{L^2(\nu)}+2a_\nu\bigr).
                                                               \tag{11}
\]
Thus (10) proves the actual statement 1 in Dom(e_(mu,0)*) and its value (5).
Reality of b and (7) give the second formula there.

Symmetry of the canonical divided-difference kernel, by the already checked polynomial adjoint calculation in C_F0048, gives
\[
 e_{\mu,0}^*p=p\xi_\mu-Je_{\mu,0}Jp
                         \quad(p\in P_\mu).      \tag{12}
\]
This is obtained by testing all represented polynomial vectors; well-definedness was just verified.
The actual adjoint domain therefore contains the dense P_mu, so e_(mu,0) is closable.
Combining (9),(12) and ||p||_(infinity,mu)<=||p||_(infinity,nu) gives the initial adjoint estimate
\[
 \|e_{\mu,0}^*p\|_{L^2(\mu)}
 \le(a_\mu+\|\xi_\mu\|_{L^2(\mu)})
                                \|p\|_{L^\infty(\nu)}.         \tag{13}
\]

## 3. Zero extension supplies the intrinsic norm and the original graphs

For f in L-infinity(mu), the measures mu and nu restricted to S={b>0} have the same null sets.
Consequently f has a representative tilde f on S, extended as zero on S-complement, with
\[
 \|\widetilde f\|_{L^\infty(\nu)}
                 =\|f\|_{L^\infty(\mu)}.         \tag{14}
\]
The assertion about null sets is confined to S, where b is strictly positive; no positive lower bound is necessary there.
A mu-null subset of S is nu-null since its integral of the positive function b is zero.

Choose starred polynomials p_n with p_n->tilde f in L2(nu), uniformly bounded nu sup norms, and an almost-everywhere convergent subsequence.
Bounded continuous approximation followed by uniform polynomial approximation permits the common bound to be arbitrarily close to the right side of (14).
Their mu classes then converge to f in L2(mu), since mu<=B nu.

By (9),(13), the original core images e_(mu,0)p_n and e_(mu,0)*p_n are bounded in H_mu.
Select weakly convergent output subsequences.
The graphs of the original closure E_mu and of the actual closed adjoint E_mu*=e_(mu,0)* are closed linear subspaces, hence weakly closed.
Their first coordinates converge strongly to f.
This proves (4), and weak lower semicontinuity with (14) proves the intrinsic estimates in (6).

In particular, apply this argument to f equal to the mu class of **any original polynomial** p.
Its zero extension need not equal p as a nu function.
Nevertheless both it and the constant original-core graph value have first coordinate f in the same original closed graph; uniqueness forces the recovered value to equal e_(mu,0)p.
Therefore
\[
 \boxed{\quad
 \|e_{\mu,0}p\|_{L^2(\mu)}
       \le a_\mu\|p\|_{L^\infty(\mu)}
       \qquad(p\in P_\mu).\quad}                \tag{15}
\]
This is the required improvement of (9), not an identification of the two sup norms.

To check the actual formula in (6), the radial estimate and adjoint pairing give E_nu(bp_n) weakly convergent to E_nu(b tilde f) in L2(nu): test first against Dom(E_nu*), use strong convergence of bp_n, then use density and the uniform output bound.
The restriction map to L2(mu) is bounded, so it preserves this weak convergence.
Dominated convergence on the chosen subsequence gives p_n E_nu b->tilde f E_nu b strongly.
Equation (8) and weak closedness of the original E_mu graph now give its asserted actual value.
It is independent of the extension: changing an extension only on S-complement leaves b tilde f unchanged nu-a.e., and leaves tilde f E_nu b unchanged mu-a.e.

The actual adjoint formula in (6) follows from (12): p_n xi_mu->f xi_mu strongly, while E_mu Jp_n converges weakly to E_mu Jf by adjoint pairing and the now established intrinsic estimate.
The original adjoint graph is weakly closed.
This completes the original-graph proof; no independently selected extension of either operator has been substituted.

## 4. Free tuples and an example with a positive-measure zero-density region

For a finite freely independent normal generating tuple with laws satisfying (1)-(2), retain **all exact original C_F0025 hypotheses**: original domain is the full starred polynomial algebra, vacuum lies in each actual adjoint domain, unstarred generator commutators are rank one, and starred generator commutators have compact bounded extensions.
C_F0025 identifies the normalized marginal restrictions with (3).
The intrinsic estimate (15), not the weaker (9), now supplies C_F0045 with a_j=2B_j^{3/2}a_(nu_j).

C_F0045 therefore restores both all-M domains of the **original** closures and actual adjoints.
Its original-generator identities and unchanged-closure statement permit C_F0024 to be applied exactly.
Thus, for f in M, membership in Div_(L0(M)) C<X_1,...,X_d> is equivalent to bounded finite-rank representability of the original C_F0025 weak forms.
C_F0024's complete affiliated-fraction criterion and its some/every fraction independence also hold at their stated scope.
The rational algebra remains unstarred; no bounded division-closure equality is asserted.

Actual examples exist: (10),(12) establish the marginal vacuum and closability, the canonical unstarred commutator is P, and the starred commutator has kernel (bar(z)-bar(w))/(z-w), with Hilbert-Schmidt norm one because mu is nonatomic.
C_F0045's existing free-product construction therefore gives the exact original cores, rather than assuming unspecified duals exist.

For a concrete measure, take 2/3<beta<1,
\[
 d\sigma(r)=\beta r^{\beta-1}\,dr\quad(0<r\le1),\qquad
 b(re^{i\theta})=2\mathbf1_{\{\cos\theta>0\}}.     \tag{16}
\]
It has angular mean one, B=2, and b=0 on the left half-plane, a set of nu-measure 1/2.
The radial midpoint satisfies
\[
 A(r)=r^{\beta-1},\qquad
 \|A\|_{L^2(\sigma)}^2=\frac{\beta}{3\beta-2}<\infty.
\]
Hence the constructed vector (5) is the actual vacuum adjoint by (10), and all of (4)-(6),(15) hold.
This example is outside C_F0051 v1 at recorded assessment 2 because the measures do not have the same null sets.
Its additional angular-mean-one property is specific to this example and is not needed in the statement or proof.

The conclusion remains a sufficient one under the independent reference-radial L2 premise.
It does not establish necessity for nonnegative densities, cover singular angular laws or unbounded densities, or resolve correlated normal tuples.
Author checks specifically covered represented-core well-definedness, the distinction between (9) and (15), the zero-extension norm identity restricted to S, actual graph uniqueness, independence of extensions, the absence of any use of radiuswise angular normalization, and the exact C_F0045 input.
No numerical or formal verification is claimed.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-16T13:22 |
| status | open |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#nonnegative-density-normal-core-transfer) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: A probability with any bounded nonnegative density relative to a radial reference satisfying the L2 midpoint condition has both original bounded-function domains; zero-set extension recovers intrinsic estimates and the full original free-tuple criterion.

### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-16T13:26 |
| status | proved |

Recorded review label: independently reviewed.
This historical label is qualified by R_F0028's [review-relationship correction](../audits/reviews/Yin_R_F0028_v1.md#review-relationship-correction): the disclosed prior development inputs make the original complete mathematical check self-reviewed for present use.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#nonnegative-density-normal-core-transfer) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original compact starred-polynomial-core hypotheses, normalization and weak-form-to-rationality implication. |
| dependency | [Exact material](Yin_C_F0024_v1.md#decision-candidate-0002) | Full affiliated-fraction and bounded-element criterion after recovery of both original all-M domains. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Intrinsic marginal infinity-to-L2 lifting, original dual and adjoint graph restoration and free-product examples. |
| dependency | [Exact material](Yin_C_F0047_v1.md#decision-candidate-0002) | Reference radial midpoint sufficient condition, actual radial domains, vacuum formula and quantitative bound. |
| dependency | [Exact material](Yin_C_F0048_v1.md#decision-candidate-0002) | Density-transfer and vacuum-pairing mechanism, reconstructed here without strict positivity or angular normalization. |
| review | [Exact material](../audits/reviews/Yin_R_F0028_v1.md) | Complete selected proof including represented-core well-definedness, actual vacuum, both original graphs, intrinsic norm recovery, full free-tuple affiliated criterion and zero-density example; radial reference L2 premise retained. |

Recorded mathematical summary: A probability with any bounded nonnegative density relative to a radial reference satisfying the L2 midpoint condition has both original bounded-function domains; zero-set extension recovers intrinsic estimates and the full original free-tuple criterion.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision candidate-0003

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-19T13:54 |
| status | proved |

Recorded review label: independently reviewed.
This historical label is qualified by R_F0028's [review-relationship correction](../audits/reviews/Yin_R_F0028_v1.md#review-relationship-correction): the disclosed prior development inputs make the original complete mathematical check self-reviewed for present use.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#nonnegative-density-normal-core-transfer) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original compact starred-polynomial-core hypotheses, normalization and weak-form-to-rationality implication. |
| dependency | [Exact material](Yin_C_F0024_v1.md#decision-candidate-0002) | Full affiliated-fraction and bounded-element criterion after recovery of both original all-M domains. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Intrinsic marginal infinity-to-L2 lifting, original dual and adjoint graph restoration and free-product examples. |
| dependency | [Exact material](Yin_C_F0047_v1.md#decision-candidate-0002) | Reference radial midpoint sufficient condition, actual radial domains, vacuum formula and quantitative bound. |
| dependency | [Exact material](Yin_C_F0048_v1.md#decision-candidate-0002) | Density-transfer and vacuum-pairing mechanism, reconstructed here without strict positivity or angular normalization. |
| review | [Exact material](../audits/reviews/Yin_R_F0055_v1.md#c-f0089-applicability) | Yin_C_F0052 (recorded assessment 2): current-rule execution-path and exact review-evidence correspondence; retain the original complete mathematical check and exact scope. Its original independent description is historical and is corrected to self-reviewed on the disclosed prior development inputs in R_F0028's [relationship correction](../audits/reviews/Yin_R_F0028_v1.md#review-relationship-correction). No new whole-proof independent review, proof change, dependency change or Task completion. |

Recorded mathematical summary: A probability with any bounded nonnegative density relative to a radial reference satisfying the L2 midpoint condition has both original bounded-function domains; zero-set extension recovers intrinsic estimates and the full original free-tuple criterion.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-applicability

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:13 |
| status | proved |
| reason | Select the same actual applicability finding at its responsible R home, with its original date, exact per-Claim scope and known shared mathematical context, preserving statement, argument, dependencies and mathematical assessment. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#nonnegative-density-normal-core-transfer) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original compact starred-polynomial-core hypotheses, normalization and weak-form-to-rationality implication. |
| dependency | [Exact material](Yin_C_F0024_v1.md#decision-candidate-0002) | Full affiliated-fraction and bounded-element criterion after recovery of both original all-M domains. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Intrinsic marginal infinity-to-L2 lifting, original dual and adjoint graph restoration and free-product examples. |
| dependency | [Exact material](Yin_C_F0047_v1.md#decision-candidate-0002) | Reference radial midpoint sufficient condition, actual radial domains, vacuum formula and quantitative bound. |
| dependency | [Exact material](Yin_C_F0048_v1.md#decision-candidate-0002) | Density-transfer and vacuum-pairing mechanism, reconstructed here without strict positivity or angular normalization. |
| review | [Retained applicability finding](../audits/reviews/Yin_R_F0055_v1.md#c-f0089-applicability) | The original 2026-09-19T13:52 per-Claim review applicability, exact fixed inputs and unchanged mathematical scope; self-reviewed and no new whole-proof or independent review. |

## Recorded review scopes

Complete selected proof including represented-core well-definedness, actual vacuum, both original graphs, intrinsic norm recovery, full free-tuple affiliated criterion and zero-density example; radial reference L2 premise retained.

Review: [Exact material](../audits/reviews/Yin_R_F0028_v1.md).

Material covered by that review: [Exact material](Yin_C_F0052_v1.md).

Yin_C_F0052 (recorded assessment 2): current-rule execution-path and exact review-evidence correspondence; retain the original complete mathematical check and exact scope.
Its original independent description is historical and is corrected to self-reviewed on the disclosed prior development inputs in R_F0028's [relationship correction](../audits/reviews/Yin_R_F0028_v1.md#review-relationship-correction).
No new whole-proof independent review, proof change, dependency change or Task completion.

Review: [Exact material](../audits/reviews/Yin_R_F0055_v1.md#c-f0089-applicability).

Material covered by that review: [Exact material](Yin_C_F0052_v1.md).

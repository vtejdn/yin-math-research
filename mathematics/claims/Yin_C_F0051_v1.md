---
author: Yin
---

# Upper density bounds suffice for original normal-core domains and the free-tuple rationality criterion

## Current assessment
[Selected decision](#decision-finding-owned-applicability)

## Upper density bounds suffice for the radial-to-normal core transfer

<a id="statement"></a>

Kind: Claim/proof module.
Date: 2026-09-16.
Human record author: Yin.
A research subagent developed the argument following the coordinator's upper-density proposal.
Consumer: the separate normal-domain investigation, Q3.
The [selected assessment](#decision-finding-owned-applicability) records the mathematical and review assessments.
The original Task quantifiers remain unchanged.

<a id="upper-density-normal-core-transfer"></a>
## 1. Exact scope and reuse

Let sigma be a probability on (0,R], with R finite, and let nu be its rotational planar lift:
\[
 d\nu(re^{i\theta})=d\sigma(r)\,\frac{d\theta}{2\pi}.
\]
Positive-radius atoms in sigma are allowed.
Define
\[
 A(r)=\frac{\sigma((0,r))+\sigma(\{r\})/2}{r},
 \qquad A\in L^2(\sigma).                         \tag{1}
\]
Let b be real and measurable with
\[
 0<b\le B<\infty\quad\nu\text{-a.e.},\qquad
 \int_0^{2\pi}b(re^{i\theta})\,\frac{d\theta}{2\pi}=1
 \quad\text{for sigma-a.e. }r,
 \qquad d\mu=b\,d\nu.                            \tag{2}
\]
There is **no** global or local positive lower-bound assumption on b.
The assumption (1) is retained; no necessity conclusion deriving it from a mu-vacuum condition is asserted.

The existing [C_F0048](Yin_C_F0048_v1.md) already proves the sufficient transfer by a method that uses only the upper bound and equivalence of null sets.
Its written statement retains 0<m<=b, but strict positivity almost everywhere is enough for that equivalence.
Its quantitative lower bound is used in the necessity direction, when estimating inverse-density tests.
[C_F0049](Yin_C_F0049_v1.md) removes smoothness from that necessity argument while retaining the lower bound; it does not already state the present upper-only conclusion.

The proof below reuses the actual radial closure, adjoint and estimate of [C_F0047](Yin_C_F0047_v1.md), the transfer proof and [review of C_F0048](../audits/reviews/Yin_R_F0022_v1.md), and the original-operator consequence of [C_F0045](Yin_C_F0045_v1.md), with its [review](../audits/reviews/Yin_R_F0023_v1.md).
It also checks the exact [C_F0025](Yin_C_F0025_v1.md) and [C_F0024](Yin_C_F0024_v1.md) consumer hypotheses.
These established interfaces suffice; no new external theorem or source acquisition is needed.
The extension is a removal of an unused sufficient-direction hypothesis, plus an explicit actual-graph verification for the bounded-function transfer.
No novelty or full general-normal conclusion is asserted.

For lambda=nu or mu, let H_lambda=L^2(lambda), with inner product linear in the second variable, let J be complex conjugation, and define the canonical operator on the represented starred polynomial core P=C[z,bar z] by
\[
 e_{\lambda,0}p(z)=\int\frac{p(z)-p(w)}{z-w}\,d\lambda(w).
                                                               \tag{3}
\]
The measures are nonatomic, even if sigma has positive-radius atoms.
Every polynomial divided difference is bounded off the null diagonal.
Thus (3) is well-defined on represented polynomials.
The polynomials are dense in their respective L2 spaces by compact support and Stone-Weierstrass.

Write E_lambda for the original Hilbert closure, when closability has been established; E_lambda* is the actual Hilbert adjoint in its own specified measure space.
Set
\[
 c_{\rm rad}=\frac{1+\sqrt5}{\sqrt3},\quad
 \xi_\nu(re^{i\theta})=2e^{i\theta}A(r),\quad
 a_\nu=2c_{\rm rad}\|A\|_{L^2(\sigma)},\quad
 a_\mu=2B^{3/2}a_\nu.                            \tag{4}
\]

The candidate conclusion is that e_(mu,0) is closable, its actual vacuum adjoint exists with
\[
 \boxed{\quad
 \xi_\mu=e_{\mu,0}^*1
       =E_\nu^*b-JE_\nu b
       =b\xi_\nu-2JE_\nu b,\quad}                \tag{5}
\]
and
\[
 L^\infty(\mu)\subseteq\operatorname{Dom}E_\mu
                      \cap\operatorname{Dom}E_\mu^*.
                                                               \tag{6}
\]
For every bounded measurable f, the actual values satisfy
\[
 \begin{split}
 E_\mu f&=E_\nu(bf)-fE_\nu b,\\
 E_\mu^*f&=f\xi_\mu-JE_\mu Jf,\\
 \|E_\mu f\|_{L^2(\mu)}&\le a_\mu\|f\|_\infty,\\
 \|E_\mu^*f\|_{L^2(\mu)}
   &\le(a_\mu+\|\xi_\mu\|_{L^2(\mu)})\|f\|_\infty.
 \end{split}                                                     \tag{7}
\]
Identification between nu and mu on the right of (5) and (7) means equality of measurable functions, not identification of their Hilbert adjoints.

## 2. Transfer on the original polynomial core and the vacuum pairing

Strict positivity b>0 nu-a.e. gives equivalence of the measures and equal essential sup norms.
The upper bound gives the continuous inclusion L2(nu)->L2(mu) with norm at most sqrt(B).
No inverse inclusion is used.

C_F0047 gives the actual radial domains and, for every bounded f,
\[
 \|E_\nu f\|_{L^2(\nu)}\le a_\nu\|f\|_\infty,
 \qquad E_\nu^*f=f\xi_\nu-JE_\nu Jf.             \tag{8}
\]
For each polynomial p, the radial commutator has bounded kernel
\[
 K_{\nu,p}h(z)=\int
       \frac{p(z)-p(w)}{z-w}h(w)\,d\nu(w).
\]
Polynomial graph approximation to any h in Dom(E_nu) therefore proves that ph is in that same original domain and
\[
 E_\nu(ph)-pE_\nu h=K_{\nu,p}h.
\]
Indeed, for core approximants h_n, both p h_n and E_nu(p h_n)=pE_nu h_n+K_(nu,p)h_n converge in their Hilbert norms; closedness gives the assertion.
Taking h=b is legitimate by (8), and yields
\[
 e_{\mu,0}p=E_\nu(pb)-pE_\nu b.                  \tag{9}
\]
Consequently,
\[
 \|e_{\mu,0}p\|_{L^2(\mu)}
 \le\sqrt B\bigl(\|E_\nu(pb)\|_{L^2(\nu)}
                  +\|pE_\nu b\|_{L^2(\nu)}\bigr)
 \le2B^{3/2}a_\nu\|p\|_\infty.                  \tag{10}
\]

This infinity-to-2 estimate by itself is not used to assert vacuum-adjoint membership.
Instead use b in the **actual radial adjoint domain**, which follows from (8), and pair (9):
\[
 \begin{split}
 \int e_{\mu,0}p\,d\mu
 &=\langle b,E_\nu(pb)\rangle_\nu
                      -\int bp E_\nu b\,d\nu\\
 &=\int\bigl(\overline{E_\nu^*b}-E_\nu b\bigr)p\,d\mu.
 \end{split}                                                     \tag{11}
\]
Since b is real, (8) gives E_nu*b=b xi_nu-JE_nu b.
Norm comparison shows that the vector in (5) belongs to L2(mu), with
\[
 \|\xi_\mu\|_{L^2(\mu)}
 \le B^{3/2}\bigl(\|\xi_\nu\|_{L^2(\nu)}+2a_\nu\bigr).
                                                               \tag{12}
\]
Equation (11) therefore proves precisely 1 in Dom(e_(mu,0)*) and its value (5).

The canonical symmetric-kernel identity, proved by testing every polynomial q in the adjoint pairing, is
\[
 e_{\mu,0}^*p=p\xi_\mu-Je_{\mu,0}Jp\qquad(p\in P).
                                                               \tag{13}
\]
It follows by expanding the divided difference of bar(p)q and interchanging the two variables in the second summand; all involved polynomial kernels are bounded.
Thus the adjoint domain contains the dense P, proving closability, and (10),(13) give the polynomial adjoint bound in (7).

## 3. Actual graph recovery and the bounded-function identity

For any bounded measurable f, choose polynomials p_n converging to f in L2(nu), with uniformly bounded sup norms, and, after passage to a subsequence, pointwise nu-almost everywhere.
Such a sequence is obtained by bounded continuous approximation for the compact Borel measure, followed by uniform starred-polynomial approximation.
The common bound can be taken arbitrarily close to ||f||_infinity.
Since the measures are equivalent and mu<=B nu, the same p_n converge to f in L2(mu) and almost everywhere for mu.

First use only the polynomial estimates.
The outputs e_(mu,0)p_n and e_(mu,0)*p_n are bounded in L2(mu).
Weakly convergent subsequences of the corresponding graph vectors lie in the weakly closed graphs of the original closure E_mu and of the actual closed adjoint e_(mu,0)*=E_mu*.
Their first coordinates converge strongly to f.
This proves both actual domain inclusions (6), with the bounds in (7) by weak lower semicontinuity and the arbitrarily close input norm bound.
It does not replace either graph by a newly defined extension.

We next identify the actual value of E_mu f.
The functions bp_n converge to bf in L2(nu), with uniform sup bounds.
The radial estimates and adjoint pairing imply
\[
 E_\nu(bp_n)\rightharpoonup E_\nu(bf)
                    \quad\text{in }L^2(\nu).      \tag{14}
\]
To check this assertion directly, pair first with any h in Dom(E_nu*): \(\langle h,E_\nu(bp_n)\rangle =\langle E_\nu^*h,bp_n\rangle\).
Strong input convergence gives the limit; density of that test domain and the uniform output bound give weak convergence against all L2(nu) vectors.
All bounded inputs already lie in the original radial domain by C_F0047.

The continuous inclusion L2(nu)->L2(mu) preserves weak convergence.
Also p_n E_nu b converges strongly to f E_nu b in both L2 spaces, by dominated convergence along the chosen almost-everywhere subsequence and its uniform sup bound.
Applying these facts to (9) gives
\[
 e_{\mu,0}p_n\rightharpoonup E_\nu(bf)-fE_\nu b
                    \quad\text{in }L^2(\mu).
\]
The original graph of E_mu is weakly closed and p_n->f strongly, so its unique value at f is exactly the first formula in (7).

Finally, for the actual adjoint formula, p_n xi_mu->f xi_mu strongly in L2(mu).
The already established all-bounded-function domain and estimate for E_mu show, by the same adjoint-pairing argument as (14), that E_mu Jp_n converges weakly to E_mu Jf.
Apply (13) and the weak closedness of the actual adjoint graph to obtain the second formula in (7).
This completes the actual-domain and identity proof without any lower bound on b.

## 4. Original free-product duals and the complete Q3 converse in this class

Take the exact original C_F0025 setting: a finite bounded normal generating tuple X=(X_1,...,X_d), original operators D_(j,0) on exactly the full starred polynomial algebra
\[
 \mathcal P=\mathbb C\langle X_1,\ldots,X_d,X_1^*,\ldots,X_d^*\rangle,
\]
the actual vacuum-adjoint condition, rank-one unstarred generator commutators, and compact bounded starred-generator commutators.
Let D_j denote their original Hilbert closures.
Assume the coordinate algebras W*(X_j) are freely independent and their marginal laws each satisfy (1)-(2), with their own sigma_j,b_j,B_j.

Normalize on the original core by eta_j=D_(j,0)1 and E_(j,0)p=D_(j,0)p-p eta_j.
C_F0025 identifies the marginal restriction e_j with the canonical core (3).
Equation (10) therefore supplies the exact hypothesis of C_F0045 with
\[
 a_j=2B_j^{3/2}\,2c_{\rm rad}\|A_j\|_{L^2(\sigma_j)}.
\]
All other assumptions of C_F0045 are retained unchanged.
Its already reviewed argument thus gives
\[
 M\subseteq\bigcap_j\bigl(\operatorname{Dom}D_j
                     \cap\operatorname{Dom}D_{j,0}^*\bigr).
                                                               \tag{15}
\]
It also extends the original generator commutators to M and proves that restricting D_j to M and reclosing returns the original D_j, with its actual original adjoint.
In particular no replacement dual or enlarged starred rational algebra has been introduced.

Let A_X=C<X_1,...,X_d> remain the unstarred algebra and F=Div_(L0(M)) A_X.
Combining the exact C_F0045 consumer interface with C_F0024 gives, for every f in M,
\[
 f\in F
 \quad\Longleftrightarrow\quad
 \beta_j^f(p,q)=\langle D_{j,0}^*p,fq\rangle
               -\langle f^*p,D_{j,0}q\rangle
 \text{ has a bounded finite-rank representative for every }j.
                                                               \tag{16}
\]
Here p,q range over the **original** P.
This supplies the missing Q3 converse within the present marginal class, including the already established forward direction.

For completeness the same accepted C_F0024 interface restores the full affiliated-fraction criterion: if u in L0(M) is written
\[
 u=s^{-1}a=cv^{-1},\qquad s,a,c,v\in M,\quad s,v\text{ regular},
\]
then u belongs to F iff every original all-M cleared defect
\[
 z\longmapsto sD_j(cz)-aD_j(vz)\qquad(z\in M)
\]
has finite-dimensional range, for some, equivalently every, such fraction pair.
The defects then have unique bounded finite-rank extensions.
Literal full-closed-domain commutator invariance for bounded f follows from that same theorem at its stated scope.
Fraction independence is reused from C_F0024; it is not inferred directly from the changed-measure identity.

The scalar canonical constructions also produce actual examples: (5),(13) provide the marginal vacuum condition and closability, [e_(mu,0),X]=P, and the starred commutator has kernel (bar(z)-bar(w))/(z-w), of Hilbert-Schmidt norm one.
C_F0045's Section 8 free-product construction therefore produces original starred polynomial cores with precisely these hypotheses.
This avoids assuming the existence of unspecified duals in the example below.

## 5. A genuine upper-only example with the actual vacuum condition

Choose 2/3<beta<1, R=1, and
\[
 d\sigma(r)=\beta r^{\beta-1}\,dr\quad(0<r\le1),
 \qquad b(re^{i\theta})=1+(1-r)\cos\theta.
                                                               \tag{17}
\]
The angular mean is one, and
\[
 r\le b(re^{i\theta})\le2-r<2.
\]
Thus every annulus bounded away from zero has a positive lower bound, whereas ess inf_nu b=0.
To see the latter in the essential sense, for any epsilon>0 take a small positive-radius interval with r<epsilon/2 and an angular neighborhood of pi where 1+cos(theta)<epsilon/2; their product has positive nu-measure and b<epsilon there.

There are no radial atoms, so
\[
 A(r)=r^{\beta-1},\qquad
 \|A\|_{L^2(\sigma)}^2
   =\int_0^1\beta r^{3\beta-3}\,dr
   =\frac{\beta}{3\beta-2}<\infty.               \tag{18}
\]
The proof above therefore constructs the **actual** mu vacuum vector
\[
 \xi_\mu=b\,(2e^{i\theta}r^{\beta-1})-2JE_\nu b
                  \in L^2(\mu),
\]
and verifies its adjoint pairing on every original starred polynomial through (11).
Its existence is not inferred from a formal density identity or a newly chosen extension.
Equations (6)-(7) apply, and free products of finitely many such examples satisfy (15)-(16).

This example is not covered by C_F0048/C_F0049's written global lower-bound hypotheses.
It also does not rely on a bounded Hilbert-space dual.
Indeed angular mean one gives mu(B(0,r))=r^beta.
If its canonical normalized core admitted a bounded Hilbert-space extension T, the actual commutator [T,X]=P would imply, after compression by e_r=1_(|X|<r),
\[
 r^\beta=\|e_rPe_r\|
          =\|e_r[T,X]e_r\|
          \le2r\|T\|.
\]
As r decreases to zero this contradicts beta<1.
Thus the example has an unbounded dual with both actual bounded-function domains.

## 6. Boundaries and review targets

The proof removes the density lower bound only from a sufficient direction with A in L2 supplied independently.
It proves no vacuum equivalence or necessity under upper bounds alone.
Singular angular conditional laws, unbounded densities, arbitrary normal marginals, and correlated tuples remain outside the conclusion.
It does not assert F intersect M=Div_M A_X, which is a different bounded-reconstruction question.

Author checks covered positivity versus uniform positivity, the direction of each Hilbert-norm comparison, the actual radial graph invariance in (9), the conjugations and signs in (11), the independent construction of the actual vacuum vector, the weak original-graph passage in Section 3, the exact C_F0045/C_F0024 consumer interfaces, and the essential infimum and vacuum legitimacy of (17).
Separate review should particularly verify that no inverse norm comparison or inverse-density test enters the proof.
No numerical computation, proof assistant, independent review, or whole-source audit is claimed at authoring.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-16T13:11 |
| status | open |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#upper-density-normal-core-transfer) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: A radial L2 midpoint condition and an almost-everywhere positive bounded angular density suffice without any lower bound; the original dual and adjoint domains and full polynomial-core criterion follow in the stated free class.

### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-16T13:16 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#upper-density-normal-core-transfer) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Exact original normal polynomial-core hypotheses, normalization and the weak-form-to-rationality implication. |
| dependency | [Exact material](Yin_C_F0024_v1.md#decision-candidate-0002) | Full affiliated-fraction and bounded-element criterion once both original all-M domains are recovered. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Marginal infinity-to-L2 lifting, original dual and adjoint graph restoration, and canonical free-product examples. |
| dependency | [Exact material](Yin_C_F0047_v1.md#decision-candidate-0002) | Radial midpoint sufficient condition, actual radial closure and adjoint, vacuum formula and quantitative bound. |
| dependency | [Exact material](Yin_C_F0048_v1.md#decision-candidate-0002) | Sufficient-direction density-transfer proof mechanism and actual vacuum pairing, refined here without its quantitative lower bound. |
| review | [Exact material](../audits/reviews/Yin_R_F0030_v1.md) | Complete selected proof and explicit example; independently assumed radial L2 midpoint condition, actual vacuum and original graphs, original polynomial-core and affiliated interfaces; no necessity assertion. |

Recorded mathematical summary: A radial L2 midpoint condition and an almost-everywhere positive bounded angular density suffice without any lower bound; the original dual and adjoint domains and full polynomial-core criterion follow in the stated free class.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision candidate-0003

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-19T13:53 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#upper-density-normal-core-transfer) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Exact original normal polynomial-core hypotheses, normalization and the weak-form-to-rationality implication. |
| dependency | [Exact material](Yin_C_F0024_v1.md#decision-candidate-0002) | Full affiliated-fraction and bounded-element criterion once both original all-M domains are recovered. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Marginal infinity-to-L2 lifting, original dual and adjoint graph restoration, and canonical free-product examples. |
| dependency | [Exact material](Yin_C_F0047_v1.md#decision-candidate-0002) | Radial midpoint sufficient condition, actual radial closure and adjoint, vacuum formula and quantitative bound. |
| dependency | [Exact material](Yin_C_F0048_v1.md#decision-candidate-0002) | Sufficient-direction density-transfer proof mechanism and actual vacuum pairing, refined here without its quantitative lower bound. |
| review | [Exact material](../audits/reviews/Yin_R_F0055_v1.md#c-f0088-applicability) | Yin_C_F0051 (recorded assessment 2): current-rule execution-path and exact review-evidence correspondence; retain the original complete independent mathematical review at its unchanged scope. No new whole-proof independent review, proof change, dependency change or Task completion. |

Recorded mathematical summary: A radial L2 midpoint condition and an almost-everywhere positive bounded angular density suffice without any lower bound; the original dual and adjoint domains and full polynomial-core criterion follow in the stated free class.

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
| argument | [Exact material](#upper-density-normal-core-transfer) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Exact original normal polynomial-core hypotheses, normalization and the weak-form-to-rationality implication. |
| dependency | [Exact material](Yin_C_F0024_v1.md#decision-candidate-0002) | Full affiliated-fraction and bounded-element criterion once both original all-M domains are recovered. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Marginal infinity-to-L2 lifting, original dual and adjoint graph restoration, and canonical free-product examples. |
| dependency | [Exact material](Yin_C_F0047_v1.md#decision-candidate-0002) | Radial midpoint sufficient condition, actual radial closure and adjoint, vacuum formula and quantitative bound. |
| dependency | [Exact material](Yin_C_F0048_v1.md#decision-candidate-0002) | Sufficient-direction density-transfer proof mechanism and actual vacuum pairing, refined here without its quantitative lower bound. |
| review | [Retained applicability finding](../audits/reviews/Yin_R_F0055_v1.md#c-f0088-applicability) | The original 2026-09-19T13:52 per-Claim review applicability, exact fixed inputs and unchanged mathematical scope; self-reviewed and no new whole-proof or independent review. |

## Recorded review scopes

Complete selected proof and explicit example; independently assumed radial L2 midpoint condition, actual vacuum and original graphs, original polynomial-core and affiliated interfaces; no necessity assertion.

Review: [Exact material](../audits/reviews/Yin_R_F0030_v1.md).

Material covered by that review: [Exact material](Yin_C_F0051_v1.md).

Yin_C_F0051 (recorded assessment 2): current-rule execution-path and exact review-evidence correspondence; retain the original complete independent mathematical review at its unchanged scope.
No new whole-proof independent review, proof change, dependency change or Task completion.

Review: [Exact material](../audits/reviews/Yin_R_F0055_v1.md#c-f0088-applicability).

Material covered by that review: [Exact material](Yin_C_F0051_v1.md).

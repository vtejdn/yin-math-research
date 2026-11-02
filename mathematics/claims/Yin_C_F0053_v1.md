---
author: Yin
---

# Finite curvature and square-integrable maximal density restore original normal-core domains

## Current assessment
[Selected decision](#decision-finding-owned-applicability)

## Maximal-density energy gives original normal-core domains

<a id="statement"></a>

Kind: Claim/proof module.
Date: 2026-09-16.
Human record author: Yin.
Argument developed by a research subagent following the coordinator's bounded curvature-interface investigation.
Consumer: the separate normal-domain investigation, Q3.
The [selected assessment](#decision-finding-owned-applicability) records the mathematical and review assessments.
No unrestricted normal-vacuum implication or Task completion is asserted.

<a id="maximal-density-cauchy-core-transfer"></a>
## 1. Exact statements

Let mu be a compactly supported Borel probability on the complex plane.
Set

\[
 M_1\mu(z)=\sup_{r>0}\frac{\mu(B(z,r))}{r},
 \qquad
 G(\mu)=c^2(\mu)+\int(M_1\mu)^2\,d\mu,
 \tag{1}
\]

where `c^2(mu)` is total Menger curvature: the integral over triples of the squared reciprocal circumradius, with value zero on collinear triples.
Assume

\[
                         G(\mu)<\infty.            \tag{2}
\]

This condition excludes atoms and does not require a uniform linear-growth constant.
On `H=L2(mu)` use the inner product linear in its second variable and define the canonical operator on the represented starred polynomial core `P=C[z,bar z]` by

\[
 E_0p(z)=\int\frac{p(z)-p(w)}{z-w}\,d\mu(w).
 \tag{3}
\]

Every such divided difference is bounded on the compact spectral support off its null diagonal; thus (3) is well-defined on represented polynomials.

**A. Original scalar domains and quantitative bound.**
The actual vacuum adjoint `xi=E_0^*1` exists, the operator is closable, and its original Hilbert closure E and actual Hilbert adjoint E* satisfy

\[
 L^\infty(\mu)\subseteq\operatorname{Dom}E\cap\operatorname{Dom}E^*.
 \tag{4}
\]

Let K_0 be the absolute constant in the primary-source bound (S) of Section 2, and put

\[
 Q=\sqrt{K_0G(\mu)},\qquad a=(5+2\sqrt{27})Q.
\]

For every bounded measurable f,

\[
 \|\xi\|_2\le2Q,\qquad
 \|Ef\|_2\le a\|f\|_\infty,\qquad
 E^*f=f\xi-JEJf,
 \qquad
 \|E^*f\|_2\le(a+\|\xi\|_2)\|f\|_\infty,
 \tag{5}
\]

where `Jf=overline(f)`.
No bounded Hilbert-space dual is asserted.

**B. Original free-normal-tuple criterion.**
Take the exact [C_F0025](Yin_C_F0025_v1.md#yin_c_f0025) setting: bounded normal generators `X_1,...,X_d` of a finite tracial von Neumann algebra M, original operators `D_(j,0)` with domain exactly the full starred polynomial algebra, vacuum in each actual adjoint domain, `[D_(j,0),X_k]=delta_(jk)P`, and compact bounded starred-generator commutators.
Let `D_j=closure(D_(j,0))`.
Suppose the coordinate algebras are freely independent and each marginal law mu_j satisfies (2).
Then

\[
 M\subseteq\bigcap_j(\operatorname{Dom}D_j\cap\operatorname{Dom}D_{j,0}^*).
 \tag{6}
\]

For the original unstarred algebra `A_X=C<X_1,...,X_d>` and `F=Div_(L0(M)) A_X`, every bounded f satisfies

\[
 f\in F\quad\Longleftrightarrow\quad
 \beta_j^f(p,q)=\langle D_{j,0}^*p,fq\rangle
               -\langle f^*p,D_{j,0}q\rangle
 \text{ has a bounded finite-rank representative for every }j,
 \tag{7}
\]

where p,q range over the original full starred polynomial core.
The complete [C_F0024](Yin_C_F0024_v1.md#yin_c_f0024) affiliated-fraction criterion also holds for the original restrictions to M, including fraction independence and bounded finite-rank extension.
Bounded f in F preserves each original full closed domain with that commutator representative.

**C. Curvature alone is insufficient.**
For every `1/3<alpha<1`, the probability

\[
 d\mu(x)=(1-\alpha)x^{-\alpha}\,dx\quad(0<x<1)
 \tag{8}
\]

has zero Menger curvature but its canonical operator (3) has no infinity-to-L2 bound.
Its actual vacuum adjoint does not exist.
Thus it is an obstruction to using curvature alone, not a counterexample satisfying the original vacuum hypothesis.

## 2. Reuse and the selected source interface

The weighted-measure mechanism reuses the proof in [C_F0044](Yin_C_F0044_v1.md), which assumes uniform linear growth and finite curvature.
Its linear-growth hypothesis is replaced here by (2) using a different established source interface.
[C_F0045](Yin_C_F0045_v1.md) supplies the complete free-product and original-domain consequence once the marginal bound has been proved.
C_F0025 supplies the normalization, canonical marginal and weak-form forward direction; C_F0024 supplies the all-M affiliated criterion.
Their existing reviewed arguments are used at these stated scopes.

The new selected source is Xavier Tolsa and Joan Verdera, *May the Cauchy transform of a non-trivial finite measure vanish on the support of the measure?*, Annales Academiae Scientiarum Fennicae Mathematica 31 (2006), 479--494.
Its [publisher PDF](https://www.acadsci.fi/mathematica/Vol31/tolsa.pdf), definitions on printed p.480 and Theorem 2 on p.481, was read successfully.
[TV06-U001](../audits/literature/TV06/Yin_U001.md#tv06-u001) records the separate source-interface inspection at statement/application depth, with no full proof audit or retained PDF.

For a finite positive Radon measure lambda with `G(lambda)<infinity`, the exact consequence needed from that theorem is

\[
 \limsup_{\epsilon\downarrow0}
 \|C_\epsilon\lambda\|_{L^2(\lambda)}^2
 \le K_0G(\lambda),
 \qquad
 C_\epsilon\lambda(z)=\int_{|z-w|>\epsilon}\frac{d\lambda(w)}{z-w},
 \tag{S}
\]

for an absolute constant K_0.
The source identifies the norm limit using limiting linear density and curvature; bounding that density by M_1 yields (S).
No numerical value or density-normalization coefficient is needed.

The earlier Cauchy branch in [Yin_S_F0011](../strategies/Yin_S_F0011.md) correctly excluded this theorem as a way to derive its geometric hypotheses from an arbitrary vacuum functional.
This proof retains those hypotheses explicitly.
No implication from the vacuum to (2), principal values or bounded truncations is used.

## 3. Positive weights and the scalar core estimate

If mu had an atom at z, then `M_1 mu(z)=infinity` on a set of positive mu measure, contrary to (2).
Thus mu is nonatomic.
For real measurable f with `||f||_infinity<=1`, define

\[
 d\lambda_f=(1+f/2)\,d\mu.
\]

The pointwise comparisons `mu/2<=lambda_f<=3mu/2` imply

\[
 c^2(\lambda_f)\le(3/2)^3c^2(\mu),\qquad
 M_1\lambda_f\le(3/2)M_1\mu,\qquad
 G(\lambda_f)\le\frac{27}{8}G(\mu).
 \tag{9}
\]

For curvature, multiply the three nonnegative densities in the triple integral.
For the maximal-density integral, use the displayed pointwise maximal bound twice and the measure comparison once.
Every source hypothesis is therefore satisfied by lambda_f.

Apply (S) to mu and lambda_f and change the latter output measure using `mu<=2lambda_f`.
With Q from Section 1 this gives

\[
 \limsup_{\epsilon\downarrow0}\|C_\epsilon\mu\|_{L^2(\mu)}\le Q,
 \qquad
 \limsup_{\epsilon\downarrow0}\|C_\epsilon\lambda_f\|_{L^2(\mu)}
 \le\frac{\sqrt{27}}2Q.
 \tag{10}
\]

By linearity of the truncated integral,

\[
 C_\epsilon(f\mu)=2(C_\epsilon\lambda_f-C_\epsilon\mu).
\]

The triangle inequality gives the bound `(sqrt(27)+2)Q` for real f of sup norm at most one.
Scaling, then splitting a complex f into its real and imaginary parts, yields

\[
 \limsup_{\epsilon\downarrow0}\|C_\epsilon(f\mu)\|_{L^2(\mu)}
 \le2(\sqrt{27}+2)Q\|f\|_\infty.
 \tag{11}
\]

This is a limit bound for each fixed f.
A common cutoff threshold for every f is neither asserted nor required.

For a fixed starred polynomial p, its truncated divided difference is

\[
 E_\epsilon p=p C_\epsilon\mu-C_\epsilon(p\mu).
\]

The divided difference is bounded, and mu has no atoms.
Dominated convergence first in the inner integral and then in L2(mu) gives `E_epsilon p->E_0p`.
Equations (10)--(11) therefore prove

\[
 \|E_0p\|_2\le[1+2(\sqrt{27}+2)]Q\|p\|_\infty
                  =a\|p\|_\infty.
 \tag{12}
\]

## 4. Actual vacuum and both original scalar graphs

Swapping the variables in the truncated double integral gives the exact identity

\[
 \int E_\epsilon p\,d\mu=2\int p C_\epsilon\mu\,d\mu.
 \tag{13}
\]

By (10), choose a sequence of truncations tending to zero whose Cauchy transforms converge weakly in L2(mu) to h, with `||h||_2<=Q`.
Passing to the limit in (13) using `E_epsilon p->E_0p` gives

\[
 \int E_0p\,d\mu=2\int p h\,d\mu
                 =\langle2Jh,p\rangle.
\]

Hence the actual vacuum adjoint exists and equals `xi=2Jh`, with norm at most 2Q.
The dense polynomial pairings determine h uniquely; no chosen extension or assumed principal-value interpretation is required for this construction.

The symmetric divided-difference kernel and the actual vacuum pairing give, for every starred polynomial p,

\[
 E_0^*p=p\xi-JE_0Jp.
 \tag{14}
\]

To verify that this is an actual adjoint identity, expand the divided difference of `overline(p)q` in the vacuum pairing and exchange its two variables in the second term.
All polynomial kernels are bounded.
The resulting equality holds against every q in the original core, so it represents the actual adjoint functional.
Thus P is contained in `Dom E_0^*`, proving closability, and (12)--(14) give the two polynomial infinity-to-L2 estimates in (5).

For bounded measurable f, bounded continuous approximation for the compact Borel measure followed by uniform starred-polynomial approximation gives `p_n->f` in L2(mu), with uniform sup norm arbitrarily close to `||f||_infinity`.
The two output sequences are bounded.
Weak subsequences in the product Hilbert space lie in the weakly closed graphs of the original closure E and actual adjoint E*.
Their first coordinates converge strongly to f, proving (4) and the two estimates in (5).

After taking an almost-everywhere convergent subsequence, boundedness gives `p_n xi->f xi` strongly in L2.
Also `E Jp_n` converges weakly to `E Jf`: pair first against the dense actual adjoint domain and use the already established bounded output estimate.
Applying (14) and weak closedness of the actual adjoint graph proves the bounded-function identity in (5).
No assertion that P is an adjoint graph core is made or needed.

The canonical example has `[E_0,z]=P_1`, while `[E_0,bar z]` has kernel `(bar z-bar w)/(z-w)`.
The latter has absolute value one off the null diagonal and Hilbert--Schmidt norm one.
The construction therefore meets the actual compact starred-core hypotheses, rather than merely producing a formal vacuum candidate.

## 5. Original free-product operators and affiliated criteria

In statement B, normalize the original polynomial operators by

\[
 \eta_j=D_{j,0}1,\qquad E_{j,0}p=D_{j,0}p-p\eta_j.
\]

C_F0025 identifies their marginal restriction with (3).
The newly proved estimate (12) is precisely the additional marginal hypothesis in C_F0045.
All other C_F0045 assumptions, including freeness and the original compact core conditions, are present.
That theorem gives (6) for the original nonnormalized closures and actual adjoints, extends their generator relations to M, and proves that reclosing their restrictions to M returns the original D_j.
The last conclusion follows because those restrictions contain the original polynomial core and are contained in the original closed operators.

C_F0024 now applies to these exact all-M restrictions.
In particular, if `f in F intersect M`, its bounded finite-rank commutator on M extends to the full original `Dom D_j`.
Pairing against original polynomial adjoint vectors proves the reverse direction of (7).
The forward direction is C_F0025's original weak-form implication.
This avoids any passage from mere Hilbert density of a smaller domain to an original graph identity.

Explicitly, for every `u in L0(M)` and bounded fractions

\[
 u=s^{-1}a=b t^{-1},\qquad s,a,b,t\in M,
 \qquad s,t\text{ regular},
\]

C_F0024 gives `u in F` if and only if all maps

\[
 z\longmapsto sD_j(bz)-aD_j(tz),\qquad z\in M,
\]

have finite-dimensional range, for some, equivalently every, fraction pair.
Each such defect has its unique bounded finite-rank extension.
Every input lies in M, so no unbounded expression is inserted into an undefined original operator domain.
The algebra A_X is the original unstarred algebra throughout.

The scalar construction in Section 4 can also be combined by C_F0045's actual free-product construction to produce examples of the exact original tuple hypotheses.
No bounded Hilbert dual or bounded scalar rational reconstruction is inferred from these facts.

## 6. Zero curvature does not control the canonical operator

Let mu be (8) with `1/3<alpha<1`.
It is a nonatomic compactly supported probability whose support lies on a line; its total Menger curvature is therefore zero.
Define `p_n(x)=(1-x)^n`, so `||p_n||_infinity=1`.

For `0<x<1/(4n)` and `1/n<y<2/n`, the difference `p_n(x)-p_n(y)` is bounded below by a positive absolute constant for all sufficiently large n.
Also `0<y-x<2/n`.
Since p_n is decreasing, its divided difference is nonpositive for every distinct x,y in the interval; contributions from the rest of the integral cannot cancel the displayed rectangle.
Consequently

\[
 |E_0p_n(x)|\ge c n\,\mu((1/n,2/n))\ge c_\alpha n^\alpha
 \quad(0<x<1/(4n)),
\]

and

\[
 \|E_0p_n\|_2^2\ge c_\alpha n^{2\alpha}\mu((0,1/(4n)))
                 \ge c'_\alpha n^{3\alpha-1}\longrightarrow\infty.
 \tag{15}
\]

This proves the failure of an infinity-to-L2 estimate.
It also cannot be an example with the original vacuum condition.
The same sign and rectangle estimate give

\[
 \left|\int E_0p_n\,d\mu\right|\ge c_\alpha n^{2\alpha-1}.
\]

Meanwhile `(1-x)^(2n)<=exp(-2nx)` and a change of variable give

\[
 \|p_n\|_2\le C_\alpha n^{(\alpha-1)/2}.
\]

The quotient of the last two bounds grows at least as `n^((3alpha-1)/2)`.
Hence the vacuum functional is not bounded in L2, proving statement C in full.
Curvature alone misses the diagonal-density contribution; (2) supplies additional information rather than following from this example.

## 7. Precise remaining general-vacuum boundary

For a general compact nonatomic normal law with actual vacuum xi, elementary symmetrization still gives only

\[
 2\lim_{\epsilon\downarrow0}\int p C_\epsilon\mu\,d\mu
 =\int\overline\xi p\,d\mu
 \quad(p\in\mathbb C[z,\bar z]).
\]

Convergence of these pairings on a dense noncomplete polynomial space is not a uniform Hilbert-norm estimate.
Neither (2) nor bounded Cauchy truncations have been derived from that identity.
C_F0044 already supplies an actual vacuum example without a uniform linear-growth constant, so that stronger growth premise cannot be inserted automatically either.

The present result is the sufficient geometric class (2), with original domains, original weak-form converse and full affiliated criterion at the free-tuple scope.
It does not settle arbitrary marginal measures, correlated tuples, or the separate equality `F intersect M=Div_M A_X`.
The zero-curvature example fails the vacuum hypothesis and is not a counterexample to the original vacuum-based criterion.
No numerical test, proof-assistant verification, full-source audit, external human review or priority claim is asserted here.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-16T13:34 |
| status | open |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#maximal-density-cauchy-core-transfer) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: Finite Menger curvature plus square-integrable maximal linear density imply an intrinsic core estimate, actual vacuum and both original bounded-function domains, with the full free-tuple criterion; finite curvature alone is insufficient.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-16T13:38 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#maximal-density-cauchy-core-transfer) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Exact original normal polynomial-core hypotheses, canonical marginal normalization and weak-form-to-rationality implication. |
| dependency | [Exact material](Yin_C_F0024_v1.md#decision-candidate-0002) | Full affiliated-fraction criterion, fraction independence and original full-domain invariance after both all-M domains are restored. |
| dependency | [Exact material](Yin_C_F0044_v1.md#decision-candidate-0002) | Positive-weight proof mechanism and original graph-recovery interface, reconstructed under maximal-density energy rather than uniform linear growth. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Marginal intrinsic infinity-to-L2 lifting, both original free-product domains, unchanged closures and actual canonical examples. |
| review | [Exact material](../audits/reviews/Yin_R_F0027_v1.md) | Complete statements A/B/C and all selected proof/source support; fixed dependencies, positive weighting, original vacuum and graphs, full free-tuple affiliated interface and nonvacuum counterexample; no unrestricted vacuum-to-energy implication. |

Recorded mathematical summary: Finite Menger curvature plus square-integrable maximal linear density imply an intrinsic core estimate, actual vacuum and both original bounded-function domains, with the full free-tuple criterion; finite curvature alone is insufficient.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision candidate-0003

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-19T13:54 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#maximal-density-cauchy-core-transfer) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Exact original normal polynomial-core hypotheses, canonical marginal normalization and weak-form-to-rationality implication. |
| dependency | [Exact material](Yin_C_F0024_v1.md#decision-candidate-0002) | Full affiliated-fraction criterion, fraction independence and original full-domain invariance after both all-M domains are restored. |
| dependency | [Exact material](Yin_C_F0044_v1.md#decision-candidate-0002) | Positive-weight proof mechanism and original graph-recovery interface, reconstructed under maximal-density energy rather than uniform linear growth. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Marginal intrinsic infinity-to-L2 lifting, both original free-product domains, unchanged closures and actual canonical examples. |
| review | [Exact material](../audits/reviews/Yin_R_F0055_v1.md#c-f0091-applicability) | Yin_C_F0053 (recorded assessment 2): current-rule execution-path and exact review-evidence correspondence; retain the original complete independent mathematical review at its unchanged scope. No new whole-proof independent review, proof change, dependency change or Task completion. |

Recorded mathematical summary: Finite Menger curvature plus square-integrable maximal linear density imply an intrinsic core estimate, actual vacuum and both original bounded-function domains, with the full free-tuple criterion; finite curvature alone is insufficient.

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
| argument | [Exact material](#maximal-density-cauchy-core-transfer) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Exact original normal polynomial-core hypotheses, canonical marginal normalization and weak-form-to-rationality implication. |
| dependency | [Exact material](Yin_C_F0024_v1.md#decision-candidate-0002) | Full affiliated-fraction criterion, fraction independence and original full-domain invariance after both all-M domains are restored. |
| dependency | [Exact material](Yin_C_F0044_v1.md#decision-candidate-0002) | Positive-weight proof mechanism and original graph-recovery interface, reconstructed under maximal-density energy rather than uniform linear growth. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Marginal intrinsic infinity-to-L2 lifting, both original free-product domains, unchanged closures and actual canonical examples. |
| review | [Retained applicability finding](../audits/reviews/Yin_R_F0055_v1.md#c-f0091-applicability) | The original 2026-09-19T13:52 per-Claim review applicability, exact fixed inputs and unchanged mathematical scope; self-reviewed and no new whole-proof or independent review. |

## Recorded review scopes

Accompanying material (original association; no added proof premise): [Exact material](../audits/literature/TV06/Yin_U001.md).

Complete statements A/B/C and all selected proof/source support; fixed dependencies, positive weighting, original vacuum and graphs, full free-tuple affiliated interface and nonvacuum counterexample; no unrestricted vacuum-to-energy implication.

Review: [Exact material](../audits/reviews/Yin_R_F0027_v1.md).

Material covered by that review: [Exact material](../audits/literature/TV06/Yin_U001.md); [Exact material](Yin_C_F0053_v1.md).

Yin_C_F0053 (recorded assessment 2): current-rule execution-path and exact review-evidence correspondence; retain the original complete independent mathematical review at its unchanged scope.
No new whole-proof independent review, proof change, dependency change or Task completion.

Review: [Exact material](../audits/reviews/Yin_R_F0055_v1.md#c-f0091-applicability).

Material covered by that review: [Exact material](../audits/literature/TV06/Yin_U001.md); [Exact material](Yin_C_F0053_v1.md).

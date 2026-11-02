---
author: Yin
---

# Measurable angular densities: vacuum equivalence and original domains without density regularity

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Measurable angular densities and the original normal core

<a id="statement"></a>
<a id="yin_c_f0049"></a>

Date: 2026-09-11.
Human author: Yin.
Proof development: another AI agent.
Consumer: the separate normal-domain investigation.
At authorship, this was a complete continuation candidate awaiting independent review.

The coordinating agent proposed removing the C1 assumption from the necessity direction of [Yin_C_F0048](Yin_C_F0048_v1.md#yin_c_f0048), including an investigation of positive radial tests.
The author supplied the annular localization and rotation argument below.
Root subsequently checked the annular split, finite-measure normalization and graph-limit mechanism before the independent review; this preliminary collaboration is disclosed.
The frozen Yin_C_F0048 proof remains unchanged.

The C1 assumption on the density can be removed.
Localization to any fixed annulus uses the already proved measurable sufficiency of Yin_C_F0048 there; smooth cutoffs then recover actual global domain vectors.
Rotation is applied to an operator pairing on the annulus, so the inverse density need not be differentiated.

Current assessment, 2026-09-11: registered as ordinary **Yin_C_F0049** after [complete review by a separate agent](../audits/reviews/Yin_R_F0024_v1.md), with preliminary collaboration disclosed.
The proof and pass verdict were complete when registered.
The measurable-density vacuum equivalence, unchanged quantitative estimate and original-domain consequence are proved.
This supersedes the initial pending assessment and removes Yin_C_F0048's C1 density restriction in the stated uniformly comparable class.
General angular measures and correlated tuples remain open.
No Role or lemma extraction is assigned.

## 1. Exact statement and reuse boundary

Keep the notation of Yin_C_F0048.
Thus sigma is any probability on (0,R], nu is its rotationally invariant planar lift, and
\[
 d\mu=b\,d\nu,\qquad 0<m\le b\le B<\infty,\qquad
 \int_0^{2\pi}b(re^{i\theta})\,\frac{d\theta}{2\pi}=1
 \quad\text{for sigma-almost every }r.
 \tag{1}
\]
The density is only measurable.
Positive radius atoms are allowed.
Let
\[
 A(r)=\frac{\sigma((0,r))+\sigma(\{r\})/2}{r},\qquad
 e_{\mu,0}p(z)=\int\frac{p(z)-p(w)}{z-w}\,d\mu(w)
 \tag{2}
\]
on the represented starred polynomial core.

Then
\[
 \boxed{\quad
 1\in\operatorname{Dom}e_{\mu,0}^*
 \quad\Longleftrightarrow\quad A\in L^2(\sigma).
 \quad}
 \tag{3}
\]
If xi_mu=e_(mu,0)*1, the necessity estimate is unchanged:
\[
 \|A\|_2\le\frac{\|\xi_\mu\|_{L^2(\mu)}}{2\sqrt m}.
 \tag{4}
\]
Consequently the infinity-to-2 estimate, actual two-domain conclusion, vacuum formula and free-product application of Yin_C_F0048 hold under (1), without its additional C1 assumption.
In particular
\[
 \|e_{\mu,0}p\|_{L^2(\mu)}
 \le\frac{2(1+\sqrt5)B^{3/2}}{\sqrt{3m}}
           \|\xi_\mu\|_{L^2(\mu)}\|p\|_\infty.
 \tag{5}
\]

The local reuse check read Yin_C_F0048, its [independent audit](../audits/reviews/Yin_R_F0022_v1.md), [Yin_C_F0047](Yin_C_F0047_v1.md#yin_c_f0047), and the distributional boundary in [Yin_C_F0044](Yin_C_F0044_v1.md#yin_c_f0044).
The C1 approximation used for smooth cutoffs is precisely [VV16-U001](../audits/literature/VV16/Yin_U001.md#vv16-u001), already imported at statement and applicability inspection depth.
The source searches for Cauchy truncations and positivity in these existing records were checked; no additional external theorem or broad search is needed.
This proof invokes only the measurable sufficient direction of Yin_C_F0048 on a fixed annulus, where its radial hypothesis is independently automatic.
It does not invoke the converse being proved.

Sufficiency in (3) is already Yin_C_F0048.
For necessity assume the left side and write E_mu for the actual closure.
Its existence follows from the same polynomial adjoint identity as in Yin_C_F0048:
\[
 e_{\mu,0}^*p=p\xi_\mu-Je_{\mu,0}Jp.
 \tag{6}
\]

## 2. Canonical operators on a fixed annulus

Let
\[
 V=\{z:a<|z|<c\},\qquad 0<a<c<\infty,
\]
and suppose t=nu(V)>0.
Angular mean one gives mu(V)=t.
Put
\[
 \nu_V=\nu|_V,\qquad \mu_V=\mu|_V.
\]
The probability measures nu_V/t and mu_V/t still differ by the same density b and satisfy (1).
The midpoint radial quantity for nu_V/t is bounded by 1/a.
Hence Yin_C_F0047 and the measurable sufficient direction of Yin_C_F0048 apply to these probabilities.

Use F_(nu,V) and F_(mu,V) for the actual canonical closed operators with the unnormalized finite integration measures nu_V and mu_V.
They equal t times the respective probability operators.
Multiplying the Hilbert-space measure by the constant t does not change domains or adjoints; thus both operators and both adjoints contain all bounded functions in their actual domains.
There are finite constants C_(lambda,V) such that
\[
 \|F_{\lambda,V}f\|_{L^2(\lambda_V)}
       \le C_{\lambda,V}\|f\|_\infty,
 \qquad \lambda\in\{\nu,\mu\}.
 \tag{7}
\]
No bound uniform as a decreases to zero is asserted.

The transfer identity extends from polynomials to every bounded measurable f:
\[
 F_{\mu,V}f=F_{\nu,V}(fb)-fF_{\nu,V}b.
 \tag{8}
\]
To check this for the actual operators, take uniformly bounded polynomials p_n converging to f almost everywhere and in L2 of the equivalent finite measures.
The polynomial identity is Yin_C_F0048.
The bounds (7) make both operator-output sequences bounded.
Closedness of the respective graphs identifies their weak limits with the outputs in (8), whereas p_n F_(nu,V)b converges strongly by dominated convergence.
This proves (8), including the actual-domain meaning of each term.

For later use, any globally C1 function restricted to V has its canonical integral as its actual operator value.
Indeed, real C1 polynomial approximation on a square containing the spectral support gives uniform convergence of divided differences, exactly as in Yin_C_F0048 Section 4.
This statement needs no smoothness of b.

## 3. Smooth cutoffs recover bounded vectors in the original global domain

Let h be a smooth function whose compact support K is contained in V.
Set
\[
 d=\operatorname{dist}(K,V^c)>0.
\]
For a polynomial p, hp is globally C1 on a neighborhood of the compact spectrum, and the same C1 approximation puts hp in Dom(E_mu) with its canonical integral as its actual value.

The exact decomposition is
\[
 E_\mu(hp)(z)=
 \begin{cases}
 F_{\mu,V}(hp)(z)+hp(z)c_{\mu,V^c}(z),&z\in V,\\[3pt]
 -\displaystyle\int_V\frac{h(w)p(w)}{z-w}\,d\mu(w),&z\notin V,
 \end{cases}
 \tag{9}
\]
where
\[
 c_{\mu,V^c}(z)=\int_{V^c}\frac{d\mu(w)}{z-w}
\]
is used only on K.
All cross integrals have distance at least d.
Formula (7) and this separation give a finite constant C_h such that
\[
 \|E_\mu(hp)\|_{L^2(\mu)}\le C_h\|p\|_\infty.
 \tag{10}
\]
For example the internal operator contributes C_(mu,V)||h||_infinity, and the two cross terms contribute at most 2||h||_infinity/d.

Now let f be any bounded measurable function on the full spectrum.
Approximate f by uniformly bounded polynomials p_n in L2(mu), passing to an almost-everywhere convergent subsequence.
Then hp_n converges strongly to hf and (10) bounds the outputs.
Weak closedness of the original graph shows
\[
 hL^\infty(\mu)\subseteq\operatorname{Dom}E_\mu.
 \tag{11}
\]
Moreover (9) holds with p replaced by f.
Its internal term converges weakly to F_(mu,V)(hf) by (7) and closedness.
Its cross multiplication term converges strongly, and its exterior integral term converges strongly because the separated kernel is bounded on V^c times K.
These identify the actual global output, rather than selecting a new extension.

Only h is differentiated in this argument.
In particular, choose any complex chi in C_c^1((0,infinity)), set
\[
 \phi(re^{i\theta})=\chi(r)e^{i\theta},\qquad
 \psi=\phi/b,
 \tag{12}
\]
and take an annulus V and a smooth cutoff h equal to one on the support of phi and compactly supported in V.
Then psi is bounded, h psi=psi, and (11) puts psi in the original Dom(E_mu).
If the annulus has zero measure, the test is zero and can be discarded.

## 4. The annular vacuum pairing for a rough inverse density

Write R_s f(z)=f(e^{is}z) on L2(nu_V).
Radial invariance makes R_s unitary, and direct calculation on polynomials gives
\[
 F_{\nu,V}R_s=e^{is}R_sF_{\nu,V}.
 \tag{13}
\]
The polynomial core is invariant under rotations, so this identity and domain invariance extend to the actual closure.

The function phi in (12) satisfies R_s phi=e^{is}phi.
Thus (13) shows F_(nu,V)phi is radial.
By the angular mean condition,
\[
 \int bF_{\nu,V}\phi\,d\nu_V
      =\int F_{\nu,V}\phi\,d\nu_V.
 \tag{14}
\]
One also has
\[
 \int\phi F_{\nu,V}b\,d\nu_V=0.
 \tag{15}
\]
Here is the needed justification for averaging the unbounded operator.
Since b belongs to its actual domain, (13) implies
\[
 F_{\nu,V}R_sb=e^{is}R_sF_{\nu,V}b.
\]
Both components of this graph vector vary continuously in L2 with s.
Integrating the graph over the circle is therefore legitimate by closedness.
The average of R_s b is the constant 1, by (1), and F_(nu,V)1=0.
On the other hand a change of variable shows that
\[
 \int\phi F_{\nu,V}R_sb\,d\nu_V
       =\int\phi F_{\nu,V}b\,d\nu_V
\]
for every s.
Its average is zero, proving (15).
This is a graph integral, not an assumed weak-star continuity of an arbitrary map on L-infinity.

Apply (8) to psi=phi/b.
Equations (14)-(15) give
\[
 \begin{aligned}
 \int F_{\mu,V}\psi\,d\mu_V
 &=\int bF_{\nu,V}\phi\,d\nu_V
                   -\int\phi F_{\nu,V}b\,d\nu_V\\
 &=\int F_{\nu,V}\phi\,d\nu_V.
 \end{aligned}
 \tag{16}
\]
No pointwise or absolutely integrable divided difference of the rough function psi is asserted.

## 5. Cross terms and the global midpoint identity

Integrate the exact global output (9) for psi.
Swapping variables in its separated exterior term gives
\[
 \int E_\mu\psi\,d\mu
 =\int F_{\mu,V}\psi\,d\mu_V
       +2\int_V\phi(z)c_{\mu,V^c}(z)\,d\nu(z).
 \tag{17}
\]
The cancellation psi b=phi accounts for the measure nu in the last integral.

The cross integral is absolutely convergent because phi is supported in K.
Simultaneously rotate z and w in
\[
 \iint_{V\times V^c}
       \frac{\phi(z)b(w)}{z-w}\,d\nu(z)d\nu(w).
\]
The annulus and its complement are rotation invariant; the phase of phi cancels that of the denominator.
Averaging b(w) therefore replaces it by one.
Combining this fact with (16) proves
\[
 \int E_\mu\psi\,d\mu
 =\iint\frac{\phi(z)-\phi(w)}{z-w}\,d\nu(z)d\nu(w)
 =2\int A(r)\chi(r)\,d\sigma(r).
 \tag{18}
\]
The last equality is Yin_C_F0047's frequency-one calculation including the same-radius atom.
Its use is valid before knowing A in L2, since chi/r is bounded and supported away from zero.
The full radial integral in (18) has a C1 divided difference and is absolutely integrable; it does not presuppose an actual global radial vacuum adjoint.

Finally the original vacuum functional and (1) give
\[
 2\left|\int A\chi\,d\sigma\right|
 =|\langle\xi_\mu,\psi\rangle_\mu|
 \le \frac{\|\xi_\mu\|_{L^2(\mu)}}{\sqrt m}
                 \|\chi\|_{L^2(\sigma)}.
 \tag{19}
\]
As in Yin_C_F0048, density of these smooth radial tests, local boundedness of A and exhaustion away from zero imply A in L2 with (4).
This proves necessity, hence (3).
Yin_C_F0048's sufficient direction then gives (5), its actual vacuum formula and both original domains; [Yin_C_F0045](Yin_C_F0045_v1.md#yin_c_f0045) supplies the free-product consequence.

## 6. A positive-test calculation and the remaining boundary

The initially tested positive cone by itself would not prove necessity.
For nonnegative nondecreasing chi, r=|z|, s=|w| and alpha=arg(z)-arg(w), direct algebra gives
\[
 \operatorname{Re}\frac{\chi(r)e^{i\arg z}-\chi(s)e^{i\arg w}}{z-w}
 =
 \frac{(\chi(r)-\chi(s))(r-s)
       +(\chi(r)s+\chi(s)r)(1-\cos\alpha)}
      {|z-w|^2}\ge0.
 \tag{20}
\]
For such tests whose angular lift phi extends C1 across zero, the original graph approximation and density comparison yield
\[
 2m^2\int A\chi\,d\sigma
       \le \|\xi_\mu\|_2\|\chi\|_2.
\]
This cone cannot detect the full L2 condition: for sigma=beta r^(beta-1)dr on (0,1) with 1/2<beta<=2/3, A=r^(beta-1) decreases, belongs to L1, and fails to belong to L2.
Opposite monotonicity gives
\[
 \int A\chi\,d\sigma
       \le\left(\int A\,d\sigma\right)
          \left(\int\chi\,d\sigma\right)
       \le\|A\|_1\|\chi\|_2
\]
for every nonnegative nondecreasing chi.
This is only a limitation of that testing cone, not a counterexample satisfying the vacuum hypothesis.
Annular localization provides the missing unrestricted radial tests.

The conclusion still requires uniform positive comparison with angular Haar measure.
Singular angular conditional laws and arbitrary normal measures are not covered.
No bounded Hilbert dual, uniform Cauchy truncation bound, general correlated-tuple conclusion or bounded scalar rational reconstruction is claimed.

Independent review should check finite-measure normalization, the actual bounded-function transfer (8), the cutoff decomposition and graph limit (9)-(11), the graph rotation average proving (15), and the separated cross-term sign and factor two in (17).
All earlier records remain unchanged.


## Assessment history


### Decision candidate-0002

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
| argument | [Exact material](#2-canonical-operators-on-a-fixed-annulus) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0024_v1.md) | Original selected finding; its actual scope and limits remain in the cited review. |

Original review classification and limitations: independently reviewed; preliminary collaboration disclosed

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision candidate-0004

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T02:52 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-canonical-operators-on-a-fixed-annulus) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0024_v1.md) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:02 |
| status | proved |
| reason | Adopt the exact original finding at its actual self-reviewed relationship. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-canonical-operators-on-a-fixed-annulus) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0024_v1.md#6-positive-tests-and-the-retained-boundary) | Whole six-section measurable angular-density vacuum equivalence and quantitative original-domain theorem: finite-measure annular normalization, rough inverse-density graph cutoffs, rotation of actual closed graph, midpoint identity with radius atoms and failure of the positive test cone. Exact uniform density comparison and freeness limits retained. |

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

Original review classification and limitations: independently reviewed; preliminary collaboration disclosed

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0024_v1.md).

Material covered by that review: [Exact material](Yin_C_F0049_v1.md).

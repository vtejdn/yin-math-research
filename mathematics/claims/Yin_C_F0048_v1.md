---
author: Yin
---

# Bounded positive angular densities: radial transfer, C1 vacuum converse and original core domains

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Angular density perturbations of the radial normal-core criterion

<a id="statement"></a>
<a id="yin_c_f0048"></a>

Date: 2026-09-11.
Human author: Yin.
Proof development: another AI agent.
Consumer: the separate normal-domain investigation and the marginal input of [Yin_C_F0045](Yin_C_F0045_v1.md#yin_c_f0045).
Record kind: complete restricted continuation candidate, author self-reviewed and awaiting independent review.
No Claim ID or Role is assigned.

Contribution: root proposed the density comparison, the test function divided by the density, the simultaneous-rotation identity and the transfer through a radial commutator.
This record supplies the domain arguments, the actual vacuum vector for the changed measure, and the quantitative conclusions.
The reviewing agent another AI agent independently checked the rotation mechanism and located the same polynomial approximation source before the final audit.
These preliminary contributions are disclosed.

For a bounded positive angular density with a C1 representative away from zero, the exact marginal vacuum-adjoint condition implies the infinity-to-2 estimate.
The radial law may have arbitrary atoms at positive radii.
In the opposite direction, the radial criterion constructs valid cores even for merely measurable angular densities.
The unrestricted normal-measure problem remains open.

Current assessment, 2026-09-11: registered as ordinary **Yin_C_F0048** after [complete review by a separate agent](../audits/reviews/Yin_R_F0022_v1.md), with preliminary contributions disclosed.
The measurable-density sufficient transfer, C1 converse, actual vacuum formula, original-domain consequence and nonradial example are proved as stated.
This supersedes the initial pending assessment.
The selected approximation input is indexed as [VV16-U001](../audits/literature/VV16/Yin_U001.md#vv16-u001), accepted at statement and applicability inspection depth.
General normal measures and correlated tuples remain open.
No Role or lemma extraction is assigned.

## 1. Reuse and the approximation input

The reuse check read [Yin_C_F0025](Yin_C_F0025_v1.md#yin_c_f0025), [Yin_C_F0045](Yin_C_F0045_v1.md#yin_c_f0045), [Yin_C_F0046](Yin_C_F0046_v1.md#yin_c_f0046), [Yin_C_F0047](Yin_C_F0047_v1.md#yin_c_f0047), and their relevant independent reviews.
Yin_C_F0047 supplies the midpoint criterion, the quantitative radial bound and the domains of the original radial closure and adjoint.
Neither uniform Cauchy truncation estimates nor a bounded Hilbert-space dual are available or needed.

A local search found no previously imported C1 Bernstein approximation statement.
The targeted primary search supplies A. Yu. Veretennikov and E. V. Veretennikova, *On partial derivatives of multivariate Bernstein polynomials*, [arXiv:1507.05235 PDF](https://arxiv.org/pdf/1507.05235).
Theorems 3 and 4(1), printed pp.6-7, state uniform approximation on the cube by tensor-product Bernstein polynomials, together with uniform approximation of all derivatives of a fixed order for a C^m function on R^d.
Only d=2, m=1 is imported, applied separately to real and imaginary parts.
The exact statements were read; a complete audit of the higher-order proof is not claimed.
The supplied 19-page PDF has an arXiv v2 margin dated 2016-10-16 and a title-page date 2018-10-15.
The [abstract page](https://arxiv.org/abs/1507.05235) gives a different title beginning *On convergence of partial derivatives*.
These are recorded version observations.
No source PDF was retained.

The application below uses a globally C1 function and an affine change of square.
The passage from C1 approximation to the graph of the actual core operator is proved explicitly.

## 2. Setting and conclusions

Let sigma be any probability on (0,R], where R is finite, and define the radial planar probability nu by
\[
 d\nu(re^{i\theta})=d\sigma(r)\,\frac{d\theta}{2\pi}.
\]
Atoms, a singular continuous part and an absolutely continuous part of sigma are all allowed.
There is no atom at radius zero.
Set
\[
 F_-(r)=\sigma((0,r)),\qquad
 a(r)=\sigma(\{r\}),\qquad
 A(r)=\frac{F_-(r)+a(r)/2}{r},\qquad
 c_{\rm rad}=\frac{1+\sqrt5}{\sqrt3}.
 \tag{1}
\]

Let b be a real measurable function such that
\[
 0<m\le b\le B<\infty\quad \nu\text{-almost everywhere},
 \qquad
 \int_0^{2\pi}b(re^{i\theta})\,\frac{d\theta}{2\pi}=1
 \quad\text{for sigma-almost every }r.
 \tag{2}
\]
Put mu=b nu.
It is a probability with the same radius distribution sigma, is nonatomic, and has the same null sets and compact support as nu.
In particular the two essential sup norms coincide.

For lambda equal to nu or mu, consider the represented starred polynomial algebra P=C[z,bar z] in H_lambda=L2(lambda), and the canonical core
\[
 e_{\lambda,0}p(z)=\int
       \frac{p(z)-p(w)}{z-w}\,d\lambda(w).
 \tag{3}
\]
Every divided difference in (3) is bounded off the null diagonal.
A polynomial which vanishes lambda-almost everywhere gives zero in (3), so the represented operator is well defined.
Inner products are linear in the second variable; J is complex conjugation.

The following assertions hold.

1. If A belongs to L2(sigma), then 1 belongs to the actual domain of e_(mu,0)*, the core is closable, and its actual closure E_mu and actual adjoint E_mu* have all bounded measurable functions in their domains.
   More precisely, with
\[
 \xi_\nu=2e^{i\theta}A,\qquad
 a_\nu=2c_{\rm rad}\|A\|_2,
\]
one has
\[
 \|e_{\mu,0}p\|_{L^2(\mu)}
 \le a_\mu\|p\|_\infty,\qquad
 a_\mu=2B^{3/2}a_\nu.
 \tag{4}
\]
This assertion requires only the measurability in (2).

2. For the converse, assume in addition that b agrees nu-almost everywhere with a real C1 function on the punctured plane.
   If
\[
 1\in\operatorname{Dom}e_{\mu,0}^*,\qquad
 \xi_\mu=e_{\mu,0}^*1,
\]
then
\[
 \|A\|_{L^2(\sigma)}
       \le\frac{\|\xi_\mu\|_{L^2(\mu)}}{2\sqrt m}.
 \tag{5}
\]
Consequently, within this additional C1 class the vacuum condition is equivalent to A in L2, and it implies
\[
 \boxed{\quad
 \|e_{\mu,0}p\|_{L^2(\mu)}
 \le \frac{2c_{\rm rad}B^{3/2}}{\sqrt m}
          \|\xi_\mu\|_{L^2(\mu)}\|p\|_\infty .
 \quad}
 \tag{6}
\]
No bound on the derivatives of b near zero is assumed.

3. In assertion 1 the actual vacuum vector is
\[
 \boxed{\quad
 \xi_\mu=E_\nu^*b-JE_\nu b
        =b\xi_\nu-2JE_\nu b.
 \quad}
 \tag{7}
\]
The operators on the right are the original radial closure and adjoint from Yin_C_F0047.
The identification in (7) is between measurable functions for equivalent measures; their Hilbert adjoints are always taken in their own specified L2 spaces.

## 3. Transfer from a radial core without differentiating the density

Assume A in L2(sigma).
Yin_C_F0047 gives
\[
 L^\infty(\nu)\subseteq
       \operatorname{Dom}E_\nu\cap\operatorname{Dom}E_\nu^*,
 \qquad
 \|E_\nu f\|_2\le a_\nu\|f\|_\infty,
 \qquad
 E_\nu^*f=f\xi_\nu-JE_\nu Jf
 \tag{8}
\]
for bounded f.
The last identity follows from the core identity by bounded polynomial approximation and weak closedness of the two actual graphs, as in that proof.

For every polynomial p, the commutator on the radial polynomial core is the bounded integral operator
\[
 K_{\nu,p}h(z)=
   \int\frac{p(z)-p(w)}{z-w}h(w)\,d\nu(w).
 \tag{9}
\]
Its bounded kernel makes it Hilbert-Schmidt.
Taking graph approximations to any h in Dom(E_nu) proves that multiplication by p preserves this domain and that
\[
 E_\nu(ph)-pE_\nu h=K_{\nu,p}h.
 \tag{10}
\]
In particular b and pb belong to the original domain, even when b is merely measurable.
Substituting h=b gives the exact identity
\[
 e_{\mu,0}p=E_\nu(pb)-pE_\nu b.
 \tag{11}
\]
This uses the changed integration measure b nu in (3); it does not identify the two operators or their adjoints.

Norm comparison and (8) now give
\[
 \|e_{\mu,0}p\|_{L^2(\mu)}
 \le\sqrt B\bigl(\|E_\nu(pb)\|_{L^2(\nu)}
                   +\|pE_\nu b\|_{L^2(\nu)}\bigr)
 \le2B^{3/2}a_\nu\|p\|_\infty.
\]
This proves (4).
The lower bound in (2) ensures that the displayed essential sup norm can equally be taken for mu.

It remains essential to construct the new vacuum adjoint, rather than infer it from the infinity-to-2 bound.
Using b in the actual radial adjoint domain, one obtains
\[
 \begin{aligned}
 \int e_{\mu,0}p\,d\mu
 &=\langle b,E_\nu(pb)\rangle_\nu
                         -\int bpE_\nu b\,d\nu\\
 &=\int\bigl(\overline{E_\nu^*b}-E_\nu b\bigr)p\,d\mu.
 \end{aligned}
 \tag{12}
\]
Both terms in (7) belong to L2(mu).
Thus (12) proves the actual vacuum assertion and the first equality in (7).
Since b is real, (8) gives its second equality.
In particular
\[
 \|\xi_\mu\|_{L^2(\mu)}
 \le B^{3/2}\bigl(\|\xi_\nu\|_{L^2(\nu)}+2a_\nu\bigr)<\infty.
 \tag{13}
\]

For completeness, the canonical core identity for either measure is
\[
 e_{\lambda,0}^*p
       =p\xi_\lambda-Je_{\lambda,0}Jp
       \quad (p\in P),
 \tag{14}
\]
whenever its vacuum vector exists.
Indeed, expand the divided difference of bar(p)q in the vacuum pairing, then interchange the two variables in the second summand.
All polynomial kernels are bounded.
This proves (14) on the actual adjoint by testing every q in P.

Thus e_(mu,0) is closable, and
\[
 \|e_{\mu,0}^*p\|_2
       \le(\|\xi_\mu\|_2+a_\mu)\|p\|_\infty.
 \tag{15}
\]
To restore the original domains, approximate any bounded measurable f in L2(mu) by polynomials p_n with uniformly bounded sup norms.
Such a sequence follows from bounded continuous approximation for a compact Borel measure, followed by uniform starred-polynomial approximation.
The two bounds give weakly convergent subsequences of the graph outputs.
A closed linear graph is weakly closed, so f belongs to both Dom(E_mu) and Dom(E_mu*).
This proves the domain assertion for the original closure and adjoint, not for a newly chosen extension.

## 4. C1 tests belong to the original graph

For the converse assume only the vacuum condition and the extra C1 representative in assertion 2.
Formula (14) already gives closability; the infinity-to-2 bound is not yet used.

Let beta be the real C1 representative of b on the punctured plane.
Choose a smooth positive function kappa on R which equals the identity on [m,B], and put beta_+=kappa(beta).
Then beta_+ is positive and C1 on the punctured plane and agrees with b nu-almost everywhere.
This modification removes any need for positivity of the original representative away from the spectral support.

For any complex chi in C_c^1((0,infinity)), set
\[
 \phi(z)=\chi(|z|)\frac{z}{|z|},\qquad
 \psi(z)=\frac{\phi(z)}{\beta_+(z)}
 \quad(z\ne0),
 \qquad \phi(0)=\psi(0)=0.
 \tag{16}
\]
Both functions are globally C1 and compactly supported; they vanish on a neighborhood of zero.
The density may have unbounded derivatives towards zero because this construction uses a fixed annulus for each test.

Choose a closed square Q containing the spectral support.
The imported Bernstein approximation gives polynomials p_n in the real coordinates x,y, equivalently starred polynomials in z, such that
\[
 \|p_n-\psi\|_{C(Q)}
       +\|d(p_n-\psi)\|_{C(Q)}\longrightarrow0.
 \tag{17}
\]
Here d is the real differential with its operator norm; convergence of the two partial derivatives gives this norm convergence.
Since Q is convex, the fundamental theorem of calculus along a segment implies
\[
 \sup_{\substack{z,w\in Q\\z\ne w}}
 \left|\frac{(p_n-\psi)(z)-(p_n-\psi)(w)}{z-w}\right|
 \le\|d(p_n-\psi)\|_{C(Q)}.
 \tag{18}
\]
It follows that p_n converges to psi in L2(mu) and the canonical integral outputs converge uniformly to the same integral with psi in place of p_n.
Hence psi lies in the graph closure of the original core and
\[
 E_\mu\psi(z)=\int\frac{\psi(z)-\psi(w)}{z-w}\,d\mu(w).
 \tag{19}
\]
This argument never assumes the conclusion (4) for mu.

## 5. Simultaneous rotation recovers the midpoint radial functional

Let I_mu(psi)=int E_mu psi dmu.
From (19) and beta_+=b almost everywhere,
\[
 I_\mu(\psi)=\iint
 \frac{\phi(z)b(w)-\phi(w)b(z)}{z-w}\,d\nu(z)d\nu(w).
 \tag{20}
\]
The combined kernel is absolutely integrable: it equals b(z)b(w) times the bounded divided difference of psi.
Do not split it into separate potentially singular Cauchy integrals.

For each rotation z->e^{it}z, w->e^{it}w, radial invariance preserves the double measure and phi(e^{it}z)=e^{it}phi(z).
Averaging (20) over t and using (2) therefore gives
\[
 I_\mu(\psi)=
 \iint\frac{\phi(z)-\phi(w)}{z-w}\,d\nu(z)d\nu(w)
 =I_\nu(\phi).
 \tag{21}
\]
Fubini is justified before the average: the rotated combined kernel equals
\[
 b(e^{it}z)b(e^{it}w)
 \frac{\psi(e^{it}z)-\psi(e^{it}w)}{e^{it}z-e^{it}w},
\]
which is bounded by B squared times the global Lipschitz constant of psi for almost every (t,z,w).
The measures have no point atoms, so the diagonal is null even when the two radii agree with positive probability.

The same-circle and unequal-radius calculations of Yin_C_F0047, applied to the single angular mode phi, give
\[
 I_\nu(\phi)
 =\int\frac{2F_-(r)+a(r)}r\chi(r)\,d\sigma(r)
 =2\int A(r)\chi(r)\,d\sigma(r).
 \tag{22}
\]
This use does not assume A in L2: chi(r)/r is bounded and compactly supported away from zero.
In the frequency-one calculation, the local term is F_+(r)chi(r)/r and the outer integral contributes F_-(r)chi(r)/r after Fubini.
The equal-radius mass supplies precisely a(r)chi(r)/r.

The original vacuum pairing, (21)-(22), and (2) imply
\[
 \begin{aligned}
 2\left|\int A\chi\,d\sigma\right|
 &=|\langle\xi_\mu,\psi\rangle_\mu|\\
 &\le\|\xi_\mu\|_{L^2(\mu)}
       \left(\int\frac{|\phi|^2}{b}\,d\nu\right)^{1/2}\\
 &\le\frac{\|\xi_\mu\|_{L^2(\mu)}}{\sqrt m}
                      \|\chi\|_{L^2(\sigma)}.
 \end{aligned}
 \tag{23}
\]
Smooth compactly supported functions away from zero are dense in L2(sigma), including when sigma has atoms.
The locally bounded function A defines the functional on this dense subspace.
The bound (23), first on each compact annulus and then by exhaustion, implies A in L2(sigma) with (5).
Combining (5) and (4) proves (6).

## 6. Exact compact-core hypotheses and nonradial examples

For mu, the canonical core satisfies
\[
 [e_{\mu,0},X]=P_\mu,\qquad
 [e_{\mu,0},X^*]\text{ has kernel }
       \frac{\bar z-\bar w}{z-w}.
 \tag{24}
\]
The second commutator has Hilbert-Schmidt norm one.
Thus the constructed vacuum vector and the resulting closability meet the exact single-coordinate Yin_C_F0025 hypotheses.
Conversely, a Yin_C_F0025 marginal has the canonical normalized form (3); its marginal vacuum vector is the conditional projection of the full normalized vector.
Formula (6) therefore provides the precise missing input of Yin_C_F0045 for this class.

For freely independent normal coordinates whose laws satisfy the C1 case and whose original duals satisfy Yin_C_F0025, Yin_C_F0045 restores both original all-M domains.
If constructing a free product from such laws, the sufficient measurable case provides the needed marginal cores and bounds before that same lift.
The unnormalized original duals are recovered as in Yin_C_F0045 by adding their original right-multiplication terms; the full vacuum vectors are retained when testing their actual adjoints.

For a concrete nonradial example, take the countable-circle radius law of Yin_C_F0047 with 2/3<beta<1 and put
\[
 b(re^{i\theta})=1+\varepsilon\cos\theta,\qquad
 \varepsilon\in\mathbb R,\quad 0<|\varepsilon|<1.
 \tag{25}
\]
It has angular mean one, lower bound 1-|epsilon| and upper bound 1+|epsilon|, with a C1 representative off zero.
Its radius law still satisfies A in L2.
The resulting measure is nonradial, meets all the canonical compact-core conditions and has both original bounded-function domains.

The disk masses are unchanged by (2), so this example still violates linear growth.
It also has no bounded Hilbert-space extension of its normalized dual: the same compression of [E,X]=P_mu by 1_(|X|<r_n) used in Yin_C_F0047 would bound the unchanged disk mass by 2r_n||E||.
Thus this extension does not rely on a bounded reference dual.

## 7. Boundary and review obligations

Necessity was proved with a C1 representative away from the origin.
It has not been proved here for arbitrary measurable b satisfying (2).
Sufficiency needs no density derivatives.
This does not settle measures whose angular conditional laws are singular or fail uniform comparison with angular Haar measure, or correlated normal tuples.
There is no asserted uniform Cauchy truncation estimate or bounded scalar rational reconstruction.

Independent review should verify the changed-measure vacuum formula (12), actual radial domain use in (10)-(11), the off-support positive modification, real C1 graph approximation, the combined-kernel rotation average, the atomic midpoint in (22), and the restoration of the original two domains.
The previous radial and nonatomic records remain unchanged.
No source-priority claim or formal verification is made.


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
| argument | [Exact material](#3-transfer-from-a-radial-core-without-differentiating-the-density) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0022_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original review classification and limitations: independently reviewed; preliminary contributions disclosed

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
| argument | [Exact material](#3-transfer-from-a-radial-core-without-differentiating-the-density) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0022_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

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
| argument | [Exact material](#3-transfer-from-a-radial-core-without-differentiating-the-density) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0022_v1.md#5-original-domains-and-the-nonradial-example) | Whole seven-section angular-density theorem: measurable bounded positive sufficiency, actual changed-measure vacuum and adjoints, C1-only necessity via inverse-density graph tests and rotation, exact constants, original domains and nonradial unbounded-dual example. No unrestricted angular law or correlated tuple conclusion. |

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

Original review classification and limitations: independently reviewed; preliminary contributions disclosed

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0022_v1.md).

Material covered by that review: [Exact material](Yin_C_F0048_v1.md).

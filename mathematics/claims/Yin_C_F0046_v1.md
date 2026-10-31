---
author: Yin
---

# Radial vacuum data imply marginal bounds; exact unbounded normal-dual examples

## Current assessment
[Selected decision](#decision-isolated-current-review-20261022)

## A radial class where the marginal polynomial-core bound is automatic

<a id="statement"></a>
<a id="yin_c_f0046"></a>

Date: 2026-09-11.
Human author: Yin.
Proof development: another AI agent.
Consumer: the separate normal-domain investigation, especially the marginal input of [Yin_C_F0045](Yin_C_F0045_v1.md#yin_c_f0045).
Record kind: bounded continuation, complete restricted deduction and remaining-interface analysis.
Assessment: author self-reviewed, awaiting independent review.
No Claim ID or Role is assigned.

For a rotationally invariant normal spectral law with nonatomic radius distribution, the exact vacuum-adjoint condition implies the required marginal infinity-to-2 bound.
The proof uses angular Fourier modes and two radial Hardy quantities; it assumes neither linear growth nor finite curvature, and does not replace distributional vacuum information by unproved bounds on Cauchy truncations.
The arbitrary-measure implication remains unresolved.

Current assessment, 2026-09-11: registered as ordinary **Yin_C_F0046** after [complete independent review](../audits/reviews/Yin_R_F0077_v1.md#5-power-density-example-and-limits).
The exact radial vacuum condition, automatic marginal estimate, original domains and unbounded-dual example are proved.
Radius nonatomicity is retained; arbitrary nonradial measures remain open.
This supersedes the initial pending labels.
No Role or lemma extraction is assigned.

## 1. Exact input and reuse

Retain [Yin_C_F0025](Yin_C_F0025_v1.md#yin_c_f0025), including its original starred polynomial core, the vacuum in the actual adjoint domain, the rank-one unstarred generator commutators and compact bounded starred-generator commutators.
Normalize as in that claim.
On a coordinate algebra B=W*(X), its canonical marginal restriction e_0 is
\[
e_0p(z)=\int\frac{p(z)-p(w)}{z-w}\,d\mu(w),
\qquad p\in\mathcal P=\mathbb C[z,\bar z].
\tag{1}
\]
The spectral measure mu is compactly supported and nonatomic.
The kernel in (1) is bounded for each starred polynomial, so (1) is an ordinary absolutely convergent integral, not a principal value.
The actual marginal vacuum adjoint is the conditional projection of the full normalized vacuum-adjoint vector onto L2(B).

The exact outstanding hypothesis of Yin_C_F0045 is
\[
\|e_0p\|_2\le a\|p\|_\infty\qquad(p\in\mathcal P)
\tag{2}
\]
for a finite constant a.
Yin_C_F0045 lifts (2) through freely independent coordinate algebras and restores both original all-M domains.

The reuse check read Yin_C_F0025, [Yin_C_F0026](Yin_C_F0026_v1.md#yin_c_f0026), [Yin_C_F0028](Yin_C_F0028_v1.md#yin_c_f0028), [Yin_C_F0043](Yin_C_F0043_v1.md#yin_c_f0043), [Yin_C_F0044](Yin_C_F0044_v1.md#yin_c_f0044), Yin_C_F0045, and [Dab10-U002](../audits/literature/Dab10/Yin_U002.md#dab10-u002).
Yin_C_F0026 loses compactness of the extra starred commutator and is not a counterexample to the present assumptions.
Yin_C_F0028 does not put all bounded measurable coordinate functions into the original domains.
The Dab10 contraction uses reality and coassociativity; Yin_C_F0043 computes a particular unitary defect rather than supplying an arbitrary-normal theorem.

The local literature registry and existing Cauchy source locators were searched next.
A targeted primary web search for distributional Cauchy information, vacuum conjugates, curvature and infinity-to-2 estimates did not produce an applicable automatic theorem.
The existing [Tol17-U001](../audits/literature/Tol17/Yin_U001.md#tol17-u001) retains its explicit growth hypothesis.
A primary search result for [Tolsa-Verdera, May the Cauchy transform of a non-trivial finite measure vanish on the support of the measure?](https://mat.uab.cat/~xtolsa/xv2.pdf) displayed a different criterion involving finite curvature and an integrable maximal-density bound.
The full endpoint failed to open, so no theorem from that article is imported or newly audited.
This is a bounded search boundary, not an assertion that no general theorem exists.

## 2. Restricted statement

Suppose mu is rotationally invariant and its radius distribution nu is a nonatomic probability on (0,R], where R is finite.
It may accumulate at zero, have gaps, or be singular with respect to Lebesgue measure.
In polar coordinates,
\[
d\mu(re^{i\theta})=d\nu(r)\,\frac{d\theta}{2\pi}.
\]
Put
\[
F(r)=\nu((0,r)),\qquad
A(r)=\frac{F(r)}r,\qquad
B(r)=\int_{(r,R]}\frac1s\,d\nu(s).
\tag{3}
\]
There is no atom at zero, and the nonatomic radius assumption also makes every individual circle mu-null.

For the canonical core operator (1), the following conclusions hold.

1. The vacuum belongs to Dom(e_0*) if and only if A belongs to L2(nu).
   In that case
\[
\xi(re^{i\theta})=e_0^*1(re^{i\theta})
=2e^{i\theta}A(r),\qquad
\|\xi\|_2=2\|A\|_{L^2(\nu)}.
\tag{4}
\]
2. Under this condition,
\[
\boxed{\ \|e_0p\|_2
\le(1+\sqrt5)\|A\|_{L^2(\nu)}\|p\|_\infty
=\frac{1+\sqrt5}{2}\|\xi\|_2\|p\|_\infty.\ }
\tag{5}
\]
The adjoint has the corresponding bound
\[
\|e_0^*p\|_2
\le\left(1+\frac{1+\sqrt5}{2}\right)\|\xi\|_2\|p\|_\infty.
\tag{6}
\]
3. These hypotheses produce actual examples of Yin_C_F0025, and its original marginal closures and adjoints have all bounded coordinate vectors in their domains.
   In a freely independent normal tuple, if every radius distribution has this form, Yin_C_F0045 applies with the constant in (5), giving both original all-M domains.

The radius restriction is part of this statement.
No conclusion for arbitrary radial atoms, or arbitrary nonradial measures, is inferred here.

## 3. Angular coefficients without an unjustified singular integral

For p in the starred polynomial algebra write its finite angular expansion as
\[
p(re^{i\theta})=\sum_{n\in\mathbb Z}p_n(r)e^{in\theta}.
\]
Each coefficient has the form r^{|n|} times a polynomial in r squared.
For nu-almost every r, Parseval and the essential sup norm give
\[
\sum_n|p_n(r)|^2
=\int|p(re^{i\theta})|^2\,\frac{d\theta}{2\pi}
\le\|p\|_\infty^2.
\tag{7}
\]

If s<r, expand
\[
\frac1{re^{i\theta}-se^{i\phi}}
=\sum_{k\ge0}\frac{s^k}{r^{k+1}}
 e^{-i(k+1)\theta}e^{ik\phi};
\]
if s>r, expand
\[
\frac1{re^{i\theta}-se^{i\phi}}
=-\sum_{k\ge0}\frac{r^k}{s^{k+1}}
 e^{ik\theta}e^{-i(k+1)\phi}.
\]
For fixed unequal r,s both series converge uniformly in the two angles.
Let T p be the function with angular coefficient n-1 given by
\[
(Tp)_{n-1}(r)=
\begin{cases}
\displaystyle r^{n-1}\int_{(0,r)}s^{-n}p_n(s)\,d\nu(s),
   &n\le0,\\[6pt]
\displaystyle-r^{n-1}\int_{(r,R]}s^{-n}p_n(s)\,d\nu(s),
   &n\ge1.
\end{cases}
\tag{8}
\]
All these radial integrals exist for r>0: their kernels in absolute value are at most 1/r on the inner interval and 1/s on the outer interval.
Set
\[
h(re^{i\theta})=e^{-i\theta}A(r).
\]
Angular integration of the bounded divided difference in (1) now gives the pointwise identity
\[
e_0p=p h-Tp.
\tag{9}
\]

Only the divided difference in (1) is initially integrated against the full product measure.
Its boundedness permits Fubini.
For unequal radii, angular integration gives the two terms in (9); their subsequent radial integrals are individually finite by (8).
The set s=r is nu-null.
Thus (9) uses an iterated angular calculation.
It does not assert that the separately singular full Cauchy integrals are absolutely convergent, or that any family of isotropically truncated Cauchy transforms is uniformly bounded.

## 4. The vacuum condition identifies exactly one radial quantity

Only the angular coefficient n=1 of p can contribute to the integral of e_0p.
By (8)-(9),
\[
\begin{aligned}
\int e_0p\,d\mu
&=\int \frac{F(r)}r\,p_1(r)\,d\nu(r)
+\int\int_{(r,R]}\frac{p_1(s)}s\,d\nu(s)d\nu(r)\\
&=2\int A(r)p_1(r)\,d\nu(r).
\end{aligned}
\tag{10}
\]
The interchange is legitimate even before assuming A in L2: p_1(r)/r is a bounded polynomial in r squared, and F<=1.

If A is in L2, (10) is exactly the bounded L2 vacuum functional represented by (4), using an inner product linear in its second variable.
This proves sufficiency in (4).

Conversely, suppose xi=e_0*1 is in L2(mu).
Take its angular Fourier coefficients xi_n in L2(nu).
Testing (10) against r^{|n|}e^{in theta}Q(r squared) gives xi_n=0 for n different from 1, and
\[
r\,\overline{\xi_1(r)}=2F(r)
\quad\text{for nu-almost every }r.
\tag{11}
\]
To justify identification, polynomials Q(r squared) are uniformly dense in the continuous functions on [0,R], since r -> r squared is a homeomorphism there.
The finite signed measures tested in (11) are integrable: r xi_1 is L1 and F is bounded.
The same argument applies to r^{|n|}xi_n for the other modes.
Their vanishing moments imply the displayed densities vanish.
Since nu({0})=0, the powers of r can be cancelled almost everywhere.
This identifies every Fourier coefficient and proves (4), including necessity of A in L2.

## 5. The outer Hardy quantity is controlled by the inner one

Assume A is in L2(nu).
The continuous Stieltjes functions F and B satisfy
\[
dF=d\nu,\qquad dB=-r^{-1}\,d\nu.
\]
On [epsilon,R], B is finite and continuous of bounded variation, with B(R)=0.
Stieltjes integration by parts gives
\[
\begin{aligned}
\int_{(\epsilon,R]}B(r)^2\,d\nu(r)
&=-F(\epsilon)B(\epsilon)^2
  +2\int_{(\epsilon,R]}\frac{F(r)}r B(r)\,d\nu(r)\\
&\le2\left(\int_{(\epsilon,R]}A^2\,d\nu\right)^{1/2}
       \left(\int_{(\epsilon,R]}B^2\,d\nu\right)^{1/2}.
\end{aligned}
\tag{12}
\]
If the last factor is zero there is nothing to divide by; otherwise division proves the norm bound on this interval.
Let epsilon decrease to zero and use monotone convergence:
\[
\boxed{\ \|B\|_{L^2(\nu)}\le2\|A\|_{L^2(\nu)}.\ }
\tag{13}
\]
No boundary limit at zero was assumed: the lower-end boundary term in (12) has the favorable sign and was discarded before passage to the limit.

For n<=0, the coefficient kernel in (8) is r^{-1}(s/r)^{-n}, of absolute value at most 1/r.
The triangle inequality for the finite coefficient vector, followed by (7), therefore gives
\[
\left(\sum_{n\le0}|(Tp)_{n-1}(r)|^2\right)^{1/2}
\le A(r)\|p\|_\infty.
\tag{14}
\]
For n>=1 the kernel is s^{-1}(r/s)^{n-1}, of absolute value at most 1/s.
The same vector inequality gives the upper bound B(r)||p||_infinity for those coefficients.
The two output-frequency sets are disjoint.
Parseval, followed by (13), yields
\[
\|Tp\|_2^2
\le(\|A\|_2^2+\|B\|_2^2)\|p\|_\infty^2
\le5\|A\|_2^2\|p\|_\infty^2.
\tag{15}
\]
Since ||p h||_2<=||p||_infinity ||A||_2, (9) proves (5).

## 6. Exact dual hypotheses and the original domains

For any compactly supported nonatomic mu, the operator (1) on the actual starred polynomial algebra has
\[
[e_0,z]=P,\qquad
[e_0,\bar z]f(z)
=\int\frac{\bar z-\bar w}{z-w}f(w)\,d\mu(w).
\tag{16}
\]
The second operator is Hilbert-Schmidt: its kernel has modulus one away from the null diagonal, so its Hilbert-Schmidt norm is one.
If two polynomial representatives agree mu-almost everywhere, their divided differences agree mu-times-mu almost everywhere, so (1) is well-defined on the represented algebra.

Under (4), the vacuum adjoint and bounded core commutators give the actual adjoint formula
\[
e_0^*p=p\xi-J e_0Jp,\qquad Jp=\bar p.
\tag{17}
\]
This is the symmetric scalar-kernel specialization of Yin_C_F0025 and Yin_C_F0044.
It is tested against the entire marginal starred core, not just holomorphic polynomials.
It makes e_0 closable and proves (6).
Thus the construction meets every exact Yin_C_F0025 hypothesis, including compactness, rather than merely a formal conjugacy identity.

Apply bounded polynomial approximation and the weak closed-graph argument of Yin_C_F0044 to (5)-(6).
Every bounded coordinate vector belongs to the original closure and actual adjoint domains.
For the marginal of an initially given tuple, the full adjoint formula retains the full vacuum vector in its multiplication term, as in Yin_C_F0044 Section 5.
The marginal estimate (5) therefore supplies those original coordinate-domain inclusions.
If the coordinate algebras are freely independent, Yin_C_F0045 gives the stronger all-M conclusion for the entire original tuple.
No statement that a new adjoint replaces the original adjoint is used.

## 7. A concrete planar example beyond uniform linear growth

For 2/3<beta<1, take R=1 and
\[
d\nu(r)=\beta r^{\beta-1}\,dr,\qquad
F(r)=r^\beta,\qquad A(r)=r^{\beta-1}.
\]
Then
\[
\|A\|_2^2=\frac{\beta}{3\beta-2}<\infty,
\qquad \|\xi\|_2^2=\frac{4\beta}{3\beta-2}.
\tag{18}
\]
The rotationally invariant planar probability mu and the canonical e_0 consequently satisfy (4)-(6) and every core condition (16).
But
\[
\frac{\mu(B(0,r))}{r}=r^{\beta-1}\longrightarrow\infty.
\tag{19}
\]
It has no uniform linear-growth constant.
This is a nonselfadjoint normal example to which the present automatic marginal result applies directly.
Finite curvature is not assumed or inferred by this proof.

The same example distinguishes the conclusion from boundedness H -> H.
If e_0 had a bounded Hilbert extension E, its commutator with X=z would equal P on H.
Compress by the projection e=1_{|X|<r}.
Since e commutes with X and ||Xe||<=r,
\[
r^\beta=\|ePe\|=\|e[E,X]e\|\le2r\|E\|,
\]
which contradicts beta<1 as r decreases to zero.
Thus this example really has an unbounded Hilbert dual, despite both original all-L-infinity domains and the infinity-to-2 bound.
For beta<=2/3 the vacuum condition itself fails by (18), so that parameter range is not a counterexample under the exact hypotheses.

## 8. Remaining general-measure issue and bounded stopping point

For arbitrary mu, the exact vacuum condition still gives only the L2-representable symmetrized Cauchy functional from Yin_C_F0044:
\[
2\lim_{\epsilon\downarrow0}\int p\,C_\epsilon\mu\,d\mu
=\langle \xi,p\rangle.
\]
It does not by itself permit a uniform-boundedness argument on all of L2; the tested polynomial set is a dense noncomplete subspace.
The geometric truncation method retains its extra assumptions, and the selfadjoint/unitary contraction identities cannot be imported without their reality and coassociativity interfaces.

The radial proof avoids that step through the exact angular decomposition (8) and the order of the radii in (12).
Neither mechanism is available for a general planar measure.
It proves a substantial automatic subclass, not a counterexample or a proof of the unrestricted implication from Yin_C_F0025 to (2).
The arbitrary marginal and correlated-tuple questions remain open.

The bounded investigation stops here.
Independent review should verify all radius and angular assumptions, the orientation of (4)/(8), moment identification in (11), the signed lower boundary term in (12), the disjoint frequency sets in (15), and the actual Yin_C_F0025/domain verification in Sections 6-7.
No scalar rational reconstruction, Claim registration, source-priority result or formal verification is asserted.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:49 |
| status | proved |
| reason | Adopt the exact original finding at its disclosed unknown initial-context relationship. Preserve the mathematical statement, status, selected proof, dependencies and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#3-angular-coefficients-without-an-unjustified-singular-integral) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0077_v1.md#5-power-density-example-and-limits) | Whole radial theorem: nonatomic radius distribution, exact vacuum-adjoint iff A=F/r is in L2, angular/Stieltjes infinity-to-2 estimate, original closure and adjoint coordinate domains, free-tuple application and explicit unbounded-dual power-density example. Radius atoms, nonradial measures and correlated tuples excluded. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the separate isolated current finding on the unchanged fixed statement and proof, with exact conditions and scope. Preserve historical findings, relationships, source depths and dates; no new mathematical proof version is introduced. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#3-angular-coefficients-without-an-unjustified-singular-integral) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0077_v1.md#current-isolated-finding) | Whole radial theorem: nonatomic radius distribution, exact vacuum-adjoint iff A=F/r is in L2, angular/Stieltjes infinity-to-2 estimate, original closure and adjoint coordinate domains, free-tuple application and explicit unbounded-dual power-density example. Radius atoms, nonradial measures and correlated tuples excluded. |

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
| argument | [Exact material](#3-angular-coefficients-without-an-unjustified-singular-integral) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0077_v1.md#5-power-density-example-and-limits) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0077_v1.md#5-power-density-example-and-limits).

Material covered by that review: [Exact material](Yin_C_F0046_v1.md).

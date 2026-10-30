---
author: Yin
---

# All rotational normal radius laws admit the automatic core estimate; Haar mixtures included

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Radial atoms and the canonical normal polynomial core

<a id="statement"></a>
<a id="yin_c_f0047"></a>

Date: 2026-09-11.
Human author: Yin.
Proof development: another AI agent.
Consumer: the separate normal-domain investigation and [Yin_C_F0045](Yin_C_F0045_v1.md#yin_c_f0045).
Record kind: complete extension candidate; author self-reviewed, awaiting independent review.
No Claim ID or Role is assigned.

Contribution and provenance: root proposed the extension to radius atoms, identified the same-circle positive-frequency term, and suggested the midpoint vacuum formula and quantile comparison.
This contribution is retained explicitly.
This record supplies the complete ordered quantile proof and examples.
The reviewed [nonatomic-radius version, Yin_C_F0046](Yin_C_F0046_v1.md#yin_c_f0046) is retained unchanged.

The exact marginal vacuum-adjoint condition gives the required infinity-to-2 estimate for every compactly supported rotationally invariant law without an atom at the origin.
Arbitrary mixtures of circle and diffuse radius distributions are allowed.
Neither linear growth nor finite curvature is assumed.

Current assessment, 2026-09-11: registered as ordinary **Yin_C_F0047** after [complete review by a separate agent](../audits/reviews/Yin_R_F0025_v1.md), with the preliminary contributions disclosed there.
The midpoint vacuum criterion, arbitrary-radius estimate, original-domain consequence and countable-circle example are proved.
This supersedes the initial pending assessment.
Nonradial marginals and correlated tuples remain open.
The Yin_C_F0046 proof is unchanged; no Role or lemma extraction is assigned.

## 1. Reuse and exact statement

The previous [Yin_C_F0046 proof](Yin_C_F0046_v1.md#yin_c_f0046) and [independent audit](../audits/reviews/Yin_R_F0077_v1.md#original-f0053-account) were read, together with the original compact-core and domain interfaces of [Yin_C_F0025](Yin_C_F0025_v1.md#yin_c_f0025) and Yin_C_F0045.
The unchanged parts are the bounded polynomial divided difference, the exact starred-generator phase kernel and the actual adjoint formula.

A local search for the required quantile or atomic Hardy extension found no previously recorded statement beyond Yin_C_F0046.
A targeted primary search identified the ordinary Hardy-operator inequality as the relevant classical estimate.
The publisher endpoint for the search result [An Equality Underlying Hardy's Inequality](https://doi.org/10.1080/00029890.2022.2051407) returned 403, so no result from that article is imported.
The particular p=2 estimate needed here is proved below by integration by parts; it is a classical Hardy estimate, not a claimed new inequality.

Let nu be any Borel probability on (0,R], with R finite, and let
\[
d\mu(re^{i\theta})=d\nu(r)\,\frac{d\theta}{2\pi}.
\]
The law nu may have atoms and a singular or absolutely continuous part.
The measure mu is still nonatomic because normalized angular measure has no point atoms.
Define
\[
F_-(r)=\nu((0,r)),\quad a(r)=\nu(\{r\}),\quad
F_+(r)=F_-(r)+a(r),\quad
M(r)=F_-(r)+\frac{a(r)}2,\quad A(r)=\frac{M(r)}r.
\tag{1}
\]
On the starred polynomial core in L2(mu), define the canonical operator
\[
e_0p(z)=\int\frac{p(z)-p(w)}{z-w}\,d\mu(w).
\tag{2}
\]
Every polynomial divided difference in (2) is bounded off the null diagonal.

Then
\[
1\in\operatorname{Dom}e_0^*
\quad\Longtrightarrow\quad A\in L^2(\nu),
\]
and the exact vacuum vector is
\[
\xi(re^{i\theta})=2e^{i\theta}A(r),\qquad
\|\xi\|_2=2\|A\|_2.
\tag{3}
\]
Under this condition,
\[
\boxed{\quad
\|e_0p\|_2\le
\frac{2(1+\sqrt5)}{\sqrt3}\|A\|_2\|p\|_\infty
=\frac{1+\sqrt5}{\sqrt3}\|\xi\|_2\|p\|_\infty.
\quad}
\tag{4}
\]
The corresponding actual-adjoint bound adds ||xi||_2 to the constant multiplying ||p||_infinity.
These bounds restore the original bounded-coordinate domains; Yin_C_F0045 gives the original all-M domains for freely independent such coordinates.

The excluded atom at radius zero would be an atom of mu itself.
Under the exact Yin_C_F0025 hypotheses, atomlessness is already necessary by [Yin_C_F0028](Yin_C_F0028_v1.md#yin_c_f0028).
Thus the restriction at the origin does not exclude any valid core model.

## 2. The same-radius calculation

Write a starred polynomial in its finite angular expansion
\[
p(re^{i\theta})=\sum_{n\in\mathbb Z}p_n(r)e^{in\theta},
\qquad
\sum_n|p_n(r)|^2\le\|p\|_\infty^2
\quad\text{for nu-almost every }r.
\tag{5}
\]
Each p_n(r) is r^{|n|} times a polynomial in r squared.

When both variables lie on the same circle, elementary Laurent factorization gives
\[
\int\frac{e^{in\theta}-e^{in\phi}}
 {r(e^{i\theta}-e^{i\phi})}\,\frac{d\phi}{2\pi}
=
\begin{cases}
r^{-1}e^{i(n-1)\theta},&n\ge1,\\
0,&n\le0.
\end{cases}
\tag{6}
\]
For n>=1 expand (z^n-w^n)/(z-w); only the term with zero w power survives.
For n=-k<0, the quotient is a sum of terms with strictly negative w powers, so its mean is zero.
The case n=0 is immediate.

For unequal radii use the two geometric series already checked in Yin_C_F0046.
Define
\[
I_n(r)=r^{n-1}\int_{(0,r)}s^{-n}p_n(s)\,d\nu(s)\quad(n\le0),
\]
\[
O_n(r)=r^{n-1}\int_{(r,R]}s^{-n}p_n(s)\,d\nu(s)\quad(n\ge1).
\]
Combining the unequal-radius and same-radius contributions gives
\[
(e_0p)_{n-1}(r)=
\begin{cases}
\displaystyle \frac{F_-(r)}r p_n(r)-I_n(r),&n\le0,\\[4pt]
\displaystyle \frac{F_+(r)}r p_n(r)+O_n(r),&n\ge1.
\end{cases}
\tag{7}
\]
Here the output angular index is n-1.
The second line includes the atomic contribution a(r)p_n(r)/r required by (6).
All off-radius integrals are finite because their kernels have magnitude at most 1/r on the inside and 1/s on the outside.

The calculation begins with the bounded divided difference in (2), so Fubini is available.
It does not split a conditionally convergent planar Cauchy integral without justification or assume a uniform principal-value truncation bound.

## 3. An ordered quantile identity

Let b(t), 0<t<1, be the nondecreasing quantile of nu:
\[
b(t)=\inf\{r\in[0,R]:F_+(r)\ge t\}.
\]
Since nu has no atom at zero, b(t)>0 for t>0.
Its pushforward of Lebesgue measure is nu.
At a radius atom r of mass a(r), it equals r on the interval
\[
J_r=(F_-(r),F_+(r)),
\]
up to endpoints.
For almost every t outside these disjoint atomic intervals, t=F_-(b(t))=F_+(b(t)).
These statements follow directly from monotonicity of F_+ and the definition of b; endpoints form a null set.

Set
\[
\widetilde p_n(t)=p_n(b(t)),\qquad
U(t)=\frac{t}{b(t)},\qquad
V(t)=\int_t^1\frac{ds}{b(s)}.
\tag{8}
\]
For the auxiliary Fourier operator T define
\[
(T\widetilde p)_{n-1}(t)=
\begin{cases}
\displaystyle b(t)^{n-1}\int_0^t b(s)^{-n}\widetilde p_n(s)\,ds,
&n\le0,\\[5pt]
\displaystyle-b(t)^{n-1}\int_t^1 b(s)^{-n}\widetilde p_n(s)\,ds,
&n\ge1.
\end{cases}
\tag{9}
\]
The same kernel bounds as above hold because b is nondecreasing.
The exact identity is
\[
(e_0p)(b(t)e^{i\theta})
=\widetilde p(t,\theta)e^{-i\theta}U(t)
 -(T\widetilde p)(t,\theta).
\tag{10}
\]

To verify (10) on a plateau J_r, first take n<=0.
The first integral in (9) equals
\[
I_n(r)+\frac{t-F_-(r)}r p_n(r).
\]
Subtracting it from t p_n(r)/r gives the first line of (7).
For n>=1, the second line of (9) equals
\[
-O_n(r)-\frac{F_+(r)-t}{r}p_n(r).
\]
Its subtraction gives the second line of (7).
Outside the plateaux there is no equal-radius mass and (10) reduces to the original unequal-radius formula.

Thus the two terms on the right can depend on the position inside a plateau, but this dependence cancels in their difference.
The left side is the pullback of the actual core operator.
Neither auxiliary term is substituted for that operator or its adjoint.

## 4. Vacuum identification

Only input angular frequency 1 contributes to the vacuum coefficient.
Formula (7) and an ordinary Fubini interchange give
\[
\begin{aligned}
\int e_0p\,d\mu
&=\int \frac{F_+(r)}r p_1(r)\,d\nu(r)
+\int\int_{(r,R]}\frac{p_1(s)}s\,d\nu(s)d\nu(r)\\
&=\int\frac{2F_-(r)+a(r)}r p_1(r)\,d\nu(r)
=2\int A(r)p_1(r)\,d\nu(r).
\end{aligned}
\tag{11}
\]
This interchange does not require A in L2: p_1(r)/r is bounded, and both F functions are at most one.

If A is in L2, (11) gives the vacuum vector (3).
Conversely, test a proposed L2 adjoint vector modewise against r^{|n|}e^{in theta}Q(r squared).
The weighted Fourier coefficients are L1, and uniform density of polynomials in r squared identifies the resulting finite complex measures.
All modes except 1 vanish and
\[
r\,\overline{\xi_1(r)}=2F_-(r)+a(r)
\quad\text{almost everywhere}.
\]
As r>0 almost everywhere, this proves necessity and (3).
This moment argument works equally for atoms; no nonatomicity of nu is needed.

For the test p=z, one obtains
\[
2\int F_-\,d\nu+\sum_r a(r)^2=1.
\]
This is also the symmetry identity for two independent radii: the strict-order probabilities sum to one minus the equal-radius probability.
It confirms the normalization in (11).

## 5. Midpoints and the Hardy bound

On an atomic interval J_r of length a=a(r) and midpoint M=M(r),
\[
\int_{J_r}\frac{t^2}{r^2}\,dt
=\frac{aM^2}{r^2}+\frac{a^3}{12r^2}.
\]
Outside those intervals, t=M(b(t)).
Therefore Tonelli gives the exact, possibly infinite identity
\[
\|U\|_{L^2(0,1)}^2
=\|A\|_{L^2(\nu)}^2
+\sum_{r:a(r)>0}\frac{a(r)^3}{12r^2}.
\tag{12}
\]
Since M(r)>=a(r)/2,
\[
\boxed{\quad
\|A\|_2\le\|U\|_2\le\frac2{\sqrt3}\|A\|_2.
\quad}
\tag{13}
\]
The squared factor 4/3 is exact for an isolated first atom whose lower mass is zero.
No sharper constant is required.

For epsilon>0, b(t)>=b(epsilon)>0 on [epsilon,1), so V is absolutely continuous there and V'(t)=-1/b(t).
Integration by parts gives
\[
\int_\epsilon^1 V(t)^2\,dt
=-\epsilon V(\epsilon)^2+2\int_\epsilon^1 U(t)V(t)\,dt.
\]
Cauchy-Schwarz and monotone convergence imply the elementary dual Hardy estimate

\[
\|V\|_2\le2\|U\|_2.
\tag{14}
\]
The lower boundary term is discarded with its favorable sign before taking epsilon to zero.

For n<=0, (9) has kernel b(t)^{-1}(b(s)/b(t))^{-n} on s<t, bounded in magnitude by 1/b(t).
The finite coefficient-vector triangle inequality and (5) give pointwise bound U(t)||p||_infinity.
For n>=1, the corresponding kernel is b(s)^{-1}(b(t)/b(s))^{n-1}, bounded by 1/b(s), giving V(t)||p||_infinity.

These two groups have disjoint output frequencies.
Parseval and (14) give
\[
\|T\widetilde p\|_2^2
\le(\|U\|_2^2+\|V\|_2^2)\|p\|_\infty^2
\le5\|U\|_2^2\|p\|_\infty^2.
\tag{15}
\]
The quantile pullback is an isometry in L2 and preserves the essential sup norm.
Combining (10), (13) and (15) proves (4).

## 6. Actual operators and mixtures of circles

For the represented starred core, (2) is well defined, and
\[
[e_0,X]=P,\qquad
[e_0,X^*]\ \text{has kernel}\quad
\frac{\bar z-\bar w}{z-w}.
\tag{16}
\]
The second operator has Hilbert-Schmidt norm one, because mu is nonatomic.
Equation (3) supplies the actual vacuum adjoint.
The core adjoint identity
\[
e_0^*p=p\xi-J e_0Jp,\qquad Jp=\bar p,
\tag{17}
\]
then proves closability and the adjoint bound following (4).
It is tested on the full starred polynomial algebra.

The two bounds, weak closedness of the original graphs and bounded polynomial approximation put L-infinity(mu) into the domains of the actual closure and actual adjoint.
Restoring normalization or embedding this marginal in a full tuple proceeds exactly as in Yin_C_F0046/Yin_C_F0044: retain the full vacuum vector for the original adjoint multiplication term.
Under freeness Yin_C_F0045 lifts the estimate to every bounded element of the generated algebra.

Any finite mixture of Haar circles of positive radii satisfies (3), since A is bounded by the reciprocal of the smallest radius.
A single circle of radius r has A=1/(2r) and xi=e^{i theta}/r, as expected.
The theorem also covers countably many circles accumulating at zero, subject exactly to the summability in (3), and mixtures with an arbitrary diffuse radius component.

## 7. A countable Haar-circle example with an unbounded Hilbert dual

Let 2/3<beta<1, set s=2^{-beta}, and take
\[
r_n=2^{-n},\qquad a_n=(1-s)s^{n-1},\qquad n\ge1.
\]
These masses sum to one.
At r_n,
\[
F_-(r_n)=s^n,\qquad
M(r_n)=\frac{1+s}{2}s^{n-1},\qquad
A(r_n)=(1+s)(2s)^{n-1}.
\]
Consequently
\[
\|A\|_2^2
=\frac{(1-s)(1+s)^2}{1-4s^3}<\infty.
\tag{18}
\]
The resulting mixture of Haar circles meets every exact compact-core condition and has both original all-bounded-function domains.

Its mass in the open disk of radius r_n is s^n, so
\[
\frac{\mu(B(0,r_n))}{r_n}=(2s)^n\longrightarrow\infty.
\tag{19}
\]
Thus linear growth fails.
If the normalized dual had a bounded Hilbert extension E, compression of [E,X]=P by e_n=1_{|X|<r_n} would imply
\[
s^n=\|e_nPe_n\|\le2r_n\|E\|,
\]
contradicting (19).
This is an actually unbounded dual with the asserted two domains.
No curvature condition is assumed or inferred.

For 0<beta<=2/3, the series in (18) diverges and the canonical vacuum condition fails, so those parameters are not counterexamples under Yin_C_F0025.

## 8. Boundary and review obligations

This completes the radius-atom extension for rotationally invariant measures.
It does not settle arbitrary nonradial marginal measures or correlated normal tuples.
The whole-operator conclusion is infinity-to-2 and an original-domain inclusion, not Hilbert boundedness or bounded scalar rational reconstruction.

Independent review should check the exact same-circle contribution (6), both plateau cancellations in (10), the vacuum coefficient and moment identification, the midpoint variance and sharp ratio 4/3, the lower Hardy boundary term, and the original domain and countable-circle verifications.
No previous frozen proof is altered.
No source-priority claim, formal verification or mathematical Role is asserted.


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
| argument | [Exact material](#3-an-ordered-quantile-identity) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0025_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

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
| argument | [Exact material](#3-an-ordered-quantile-identity) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0025_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

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
| argument | [Exact material](#3-an-ordered-quantile-identity) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0025_v1.md#5-actual-domains-and-the-countable-circle-example) | Whole eight-section arbitrary-radius rotational-law theorem: same-circle term, ordered quantile plateau cancellation, midpoint vacuum criterion and variance, Hardy constants, actual original domains and countable-circle unbounded-dual example. No origin atom, nonradial/correlated theorem or bounded scalar reconstruction. |

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

Review: [Exact material](../audits/reviews/Yin_R_F0025_v1.md).

Material covered by that review: [Exact material](Yin_C_F0047_v1.md).

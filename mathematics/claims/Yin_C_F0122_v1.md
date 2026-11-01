---
author: Yin
---

# Ordered scalar/commuting and isotropic-covariance minimax; complete isotropic spectral density

## Current assessment
[Selected decision](#decision-m04-isolated-review)

## An Exact Ordered Minimax for a Shifted Semicircle

<a id="statement"></a>

<a id="yin_c_f0122"></a>
No mathematical Role is assigned.

Record kind: project deduction for the user-authorized offline [Yin_T_F0008](../tasks/Yin_T_F0008_v1.md#yin_t_f0008).
Date: 2026-09-12.
Author: root.
This records an ordinary new deduction and a commuting specialization, without assigning an extracted-lemma or theorem Role.
No network search or novelty claim is made.
The full noncommuting variational problem remains separate.

<a id="scalar-minimax"></a>
## Exact Scalar Statement

Let s be a standard semicircular element in a finite von Neumann algebra with faithful normal tracial state tau.
Let sigma > 0 and a be real, and put S = a times 1 + sqrt(sigma) s.
Define, for p real and q nonnegative,
\[
 L_{a,\sigma}(p,q)
 =\frac{(a-p)^2-q^2}{2\sigma}
   +\frac12\log(p^2+q^2),\qquad \log0=-\infty.
                                                               \tag{1}
\]
Then
\[
 \boxed{\quad
 \log\Delta_\tau(S)
   =\min_{p\in\mathbb R}\ \max_{q\geq0}
      L_{a,\sigma}(p,q).
 \quad}                                                        \tag{2}
\]
Both successive extrema are attained, and the minimizing p is unique.
The order of optimization is part of the formula.
A claim of a global saddle point or permission to interchange min and max is not made.

Equivalently, without an exponential trace or complex logarithm,
\[
 \Delta_\tau(S)
 =\min_{p\in\mathbb R}\ \max_{q\geq0}
   \left|(p+iq)
      \exp\!\left(\frac{(a-p)^2-q^2}{2\sigma}\right)\right|.
                                                               \tag{3}
\]
The scalar absolute value is its finite-dimensional Fuglede-Kadison determinant.
The variables p and q are freely chosen trial numbers; they are not required to solve a Dyson equation.

## Inputs and Exact Optimization

The [Yin_C_F0119 scalar potential](Yin_C_F0119_v1.md#explicit-obstruction-to-using-only-the-original-covariance) gives, after scaling and semicircular symmetry,
\[
 U_\sigma(a)=\log\Delta_\tau(a+\sqrt\sigma s)
 =\begin{cases}
   \frac12\log\sigma-\frac12+\frac{a^2}{4\sigma},
       & |a|\leq2\sqrt\sigma,\\
   -\log|g|+\frac\sigma2g^2,
       & |a|>2\sqrt\sigma,
  \end{cases}                                                  \tag{4}
\]
where g is the real solution of sigma g squared minus a g plus 1 = 0 with the smaller absolute value.
This is a checked semicircular logarithmic potential, not a new attribution of its underlying source formula.

For fixed p, let r = q squared.
The part depending on r has derivative
\[
 \frac{\partial}{\partial r}
       \left(-\frac r{2\sigma}+\frac12\log(p^2+r)\right)
 =-\frac1{2\sigma}+\frac1{2(p^2+r)}.
\]
It is strictly decreasing where finite.
The unique maximizing r is therefore \(r=(\sigma-p^2)_+\).
The inner value, including the terms independent of r, is
\[
 F_{a,\sigma}(p)
 =\frac{(a-p)^2}{2\sigma}
 +\begin{cases}
    \frac{p^2}{2\sigma}-\frac12+\frac12\log\sigma,
         & |p|\leq\sqrt\sigma,\\
    \log|p|,& |p|\geq\sqrt\sigma.
   \end{cases}                                                 \tag{5}
\]
The two values and first derivatives agree at the endpoints.
In the inner interval the second derivative is 2/sigma.
Outside it the second derivative is 1/sigma minus 1/p squared, which is strictly positive away from the endpoints.
Thus F is continuously differentiable, strictly convex on the real line, and coercive.
Its unique minimizer is
\[
 p_*=
 \begin{cases}
 a/2,& |a|\leq2\sqrt\sigma,\\
 \bigl(a+\operatorname{sgn}(a)\sqrt{a^2-4\sigma}\bigr)/2,
       & |a|>2\sqrt\sigma,
 \end{cases}
 \qquad q_*=\sqrt{(\sigma-p_*^2)_+}.                            \tag{6}
\]
For the first case, substitution gives exactly the first line of (4).
For the second, q_* = 0 and p_* solves p squared minus a p plus sigma = 0.
Put g = 1/p_*.
Then a minus p_* equals sigma g, so the value is minus log absolute g plus sigma g squared over 2, the second line of (4).
This proves (2); strict monotonicity of the exponential proves (3), including the zero value assigned at (p,q)=(0,0).

At a=0, the minimum occurs at p=0, q=sqrt(sigma), yielding log Delta = (log sigma - 1)/2.
Thus exp(2 log Delta + 1) equals sigma, precisely the scalar capacity.
For |a|>2 sqrt(sigma), the maximizing q switches to the boundary q=0 and the minimizing p automatically selects the correct root.

## Ordered Minimax Is Not Automatically a Saddle Point

Outside the semicircular support, q_* = 0 and p_* is nonzero.
Holding q=0 fixed instead makes L(p,0) tend to negative infinity as p tends to zero.
Hence p_* does not minimize L(p,q_*) over all real p.
In particular, the optimizer of the ordered problem (2) is not a global saddle point of the raw two-variable objective in this regime.

The valid convexity belongs to the function after maximizing q, namely (5), rather than to every fixed-q slice.
This example supplies a concrete warning for matrix extensions: proving the ordered variational identity may be possible even when a usual convex-concave saddle assertion is false.
It does not by itself prove a strict gap between the two orders of optimal values.

## Commuting Matrix Coefficients

Suppose all selfadjoint matrices a_0,...,a_n commute.
Simultaneously diagonalize them, writing their real diagonal entries as a_jk, 1 <= k <= m.
Let a_k = a_0k and sigma_k = sum over j>=1 of a_jk squared.
In the diagonal model, the k-th entry of S has semicircular law with mean a_k and variance sigma_k; joint independence between those diagonal entries is unnecessary for the normalized trace of log absolute S.

If every sigma_k is positive, direct sums and separability of the successive extrema give
\[
 \log\Delta_{\operatorname{tr}_m\otimes\tau}(S)
 =\frac1m\min_{p\in\mathbb R^m}\max_{q\in[0,\infty)^m}
       \sum_{k=1}^m L_{a_k,\sigma_k}(p_k,q_k).                 \tag{7}
\]
This is a genuine finite-dimensional variational formula for every real drift in the commuting family.
If some sigma_k is zero, replace its summand by the deterministic value log absolute a_k.
A zero deterministic entry makes the whole logarithmic determinant negative infinity.
The remaining positive-variance coordinates retain (7).

No assertion that a formal replacement of p,q,sigma by noncommuting matrices preserves (2) is made.
The reduced-objective convexity and root selection are the specific mechanisms to test in a matrix generalization, alongside the [selfadjoint route](../strategies/Yin_S_F0018.md#s_f0018).

<a id="isotropic-covariance-minimax"></a>
## Isotropic Covariance: Arbitrary Selfadjoint Drift

The same mechanism extends beyond commuting coefficients.
Let a_0,...,a_n be selfadjoint matrices in M_m(C), and assume
\[
 \eta(b)=\sum_{j\geq1}a_jba_j
       =\sigma\operatorname{tr}_m(b)I_m,\qquad \sigma>0.
\]
No commutation of a_0 with the noise coefficients is assumed.
Write \(S=a_0\otimes1+\sum_{j\geq1}a_j\otimes s_j\), and let \(\nu=m^{-1}\sum_{k=1}^m\delta_{\lambda_k}\) be the eigenvalue probability measure of a_0, with multiplicities.
For real x,
\[
 \boxed{\quad
 \log\Delta_{\varphi_m}(S-xI_m)
 =\min_{p\in\mathbb R}\max_{q\geq0}
 \left\{
    \frac{(x-p)^2-q^2}{2\sigma}
      +\frac12\int\log((p-t)^2+q^2)\,d\nu(t)
 \right\}.
 \quad}                                                        \tag{8}
\]
Equivalently, the integral term is \(m^{-1}\log|\det((p+iq)I_m-a_0)|\).
Thus (8) is a two-real-variable optimization with a freely evaluated ordinary matrix determinant.
It applies both inside and outside the spectrum.
Both ordered extrema are attained; the minimizing p is unique.

### Inner maximization and the reduced convex objective

Put
\[
 I(p,q)=\int\frac{d\nu(t)}{(p-t)^2+q^2}.
\]
At q=0 interpret a pole as infinity.
Differentiating with respect to q squared shows that the unique inner optimizer q(p) is zero when I(p,0) <= 1/sigma, and otherwise is the unique positive solution of I(p,q) = 1/sigma.
It is continuous.
Indeed the positive branch follows the strictly decreasing continuous function of q, and it can approach zero only at a non-pole point satisfying I(p,0) = 1/sigma.
At an atom of mass w it satisfies q squared >= sigma w.

The set on which q(p)>0 is a bounded finite union of intervals.
Its endpoints are roots, away from the finitely many atoms, of the rational equation I(p,0) = 1/sigma; this equation has only finitely many roots.
Define
\[
 X(p)=p+\sigma\int\frac{p-t}{(p-t)^2+q(p)^2}\,d\nu(t).
                                                               \tag{9}
\]
This function is continuous.
Where q>0, set
\[
 B=\int\frac{d\nu(t)}{((p-t)^2+q^2)^2}>0,
 \qquad C=\int\frac{p-t}{((p-t)^2+q^2)^2}\,d\nu(t).
\]
Implicit differentiation of I=1/sigma gives q'=-C/(qB), and hence
\[
 X'(p)=2\sigma\left(q^2B+\frac{C^2}{B}\right)>0.
                                                               \tag{10}
\]
On an open complementary interval q=0 and \(X'(p)=1-\sigma I(p,0)>0\).
Equality can occur only at the finitely many roots of I(p,0)=1/sigma.
These calculations and continuity across endpoints show that X is strictly increasing on the real line.
Also X(p)=p+O(1/p) at infinity, so X maps the real line onto itself.

The derivative in p of the maximized objective in (8) is (X(p)-x)/sigma.
This follows directly on each positive-q or zero-q interval; the derivatives extend continuously across their finitely many endpoints because q(p) is continuous and all denominators there are nonzero.
The reduced objective is therefore continuously differentiable, strictly convex and coercive.
Its unique minimum occurs at the unique p such that X(p)=x.

### Identifying the physical solution and the determinant

For z=x+i epsilon in the upper half-plane, the smaller Dyson equation gives
\[
 G(z)=(w(z)I_m-a_0)^{-1},\qquad
 g(z)=\operatorname{tr}_mG(z)=\int\frac{d\nu(t)}{w(z)-t},
 \qquad w(z)=z-\sigma g(z).
                                                               \tag{11}
\]
Here Im w>0.
Writing w=p+iq, imaginary parts give
\[
 \varepsilon=q(1-\sigma I(p,q)),\qquad I(p,q)<1/\sigma.
                                                               \tag{12}
\]
Cauchy-Schwarz gives |g| squared <= I(p,q), so |w-z|<=sqrt(sigma).
Moreover every eigenvalue satisfies |w-lambda_k|>=sqrt(sigma/m).
Thus as epsilon decreases to zero, w remains bounded and uniformly away from all poles.
Every subsequential limit satisfies (12) at epsilon=0 and I<=1/sigma, so its imaginary part is exactly q(p).
Its real part satisfies X(p)=x by (11).
Uniqueness from (9)-(10) identifies every subsequence and proves convergence to p+i q(p).

The exact Yin_C_F0119 primitive, now in matrix size m, yields
\[
 \log\Delta_{\varphi_m}(S-zI_m)
 =\int\log|w(z)-t|\,d\nu(t)
       +\frac\sigma2\operatorname{Re}(g(z)^2).
                                                               \tag{13}
\]
In the boundary limit, g=(x-p-iq)/sigma.
Substituting in (13) gives exactly the objective in (8) at its unique ordered optimizer.
The pole separation makes this limit finite.
The operator-side boundary limit is the ordinary logarithmic determinant by monotone spectral integration for selfadjoint S.
This proves (8), without choosing an arbitrary real algebraic root.

This proof is a direct scalarization of the already checked Dyson equation.
It does not invoke an unverified global subordination or free-convolution variational theorem, and does not claim that the representation or underlying semicircular convolution model is new in the literature.
Its relation to existing variational formulations remains a future attribution check under the offline constraint.

### Spectral information and a determinant form

The same bounds and subsequence argument give continuous boundary values, with |g(z)|<=1/sqrt(sigma).
Scalar Stieltjes inversion, obtained by integrating the Poisson kernel as in the [spectral module](Yin_C_F0123_v1.md#selfadjoint-coefficients-a-smaller-spectral-equation), then gives the continuous probability density
\[
 \frac{d\mu_S}{dx}(x)
     =\frac{q(X^{-1}(x))}{\pi\sigma}.
                                                               \tag{14}
\]
Dominated convergence in the inversion integral is legitimate by the stated uniform bound; the atom limit vanishes for the same reason.
Thus this identifies the whole spectral measure, not only its absolutely continuous part.
Faithfulness identifies its support with the operator spectrum.

Exponentiating (8) produces a compact determinant formula:
\[
 \boxed{\quad
 \Delta_{\varphi_m}(S-xI_m)
 =\min_{p\in\mathbb R}\max_{q\geq0}
   \Delta_{\operatorname{tr}_m}\!\left(
     ((p+iq)I_m-a_0)
     \exp\!\left[\frac{(x-p)^2-q^2}{2\sigma}\right]
   \right).
 \quad}                                                        \tag{15}
\]
The exponential here is a scalar multiplying the matrix.
Setting a_0=0 and x=0 gives exp(-1/2)sqrt(sigma), in agreement with cap(eta)=sigma^m.
When m=1, (8) reduces by translation to (2).
This supplies a noncommuting-coefficient test class for extending the ordered-minimax mechanism to general covariance maps.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:09 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#inputs-and-exact-optimization) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](#identifying-the-physical-solution-and-the-determinant) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0181_v1.md#scalar-and-commuting-calculations) | Complete scalar and commuting ordered minimax proof, equations (1)–(7): successive extrema, strict convexity after the inner maximum, unique optimizer, physical scalar root, determinant normalization, zero-variance coordinates and failure of a raw global saddle. No optimization-order interchange is certified. |
| review | [Original finding](../audits/reviews/Yin_R_F0122_v1.md#isotropic-covariance-calculations) | Full isotropic-covariance extension, equations (8)–(15), in the scalar/commuting context: arbitrary selfadjoint drift, all real spectral arguments including edges and closing gaps, strict reduced convexity, physical branch and pole separation, exact determinant and whole continuous spectral measure. No arbitrary noncommutative covariance minimax is certified. |


### Decision m04-isolated-review

| Field | Value |
| --- | --- |
| date | 2026-10-23T00:23 |
| status | proved |
| reason | Adopt the separately performed isolated review of the complete scalar, commuting and isotropic mathematics, retaining the adequate original isotropic self-review in place and preserving all optimization-order and attribution limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Scalar argument](#inputs-and-exact-optimization) | Complete scalar and commuting ordered minimax proof and its singular, deterministic and saddle boundaries. |
| argument | [Isotropic argument](#identifying-the-physical-solution-and-the-determinant) | Entire isotropic extension, physical scalarization, boundary control, exact potential and whole continuous spectral measure. |
| review | [Scalar isolated finding](../audits/reviews/Yin_R_F0181_v1.md#f0080-scalar-and-commuting-finding) | Equations (1)-(7), attained successive extrema, unique optimizer, physical root, normalization, zero-variance coordinates and raw saddle failure; no order interchange. |
| review | [Isotropic isolated finding](../audits/reviews/Yin_R_F0181_v1.md#f0080-isotropic-and-whole-spectral-measure-finding) | Equations (8)-(15), arbitrary selfadjoint drift at exact isotropic covariance, all real arguments, repeated eigenvalues, edges and closing gaps, physical branch/pole separation, determinant and whole continuous spectral measure; no general covariance minimax. |
| review | [Retained original isotropic self-review](../audits/reviews/Yin_R_F0122_v1.md#isotropic-covariance-calculations) | Original 2026-09-12 isotropic finding at its actual self-reviewed relationship, exact source and attribution limits, reused in place without retrospective independence. |

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
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

Original review classification and limitations: independently reviewed; spectral-interface collaboration disclosed

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#inputs-and-exact-optimization) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](#identifying-the-physical-solution-and-the-determinant) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0181_v1.md#original-f0071-account) | Complete scalar and commuting minimax argument (equations (1)-(7)) and the full isotropic-covariance extension (equations (1)-(15)): strict convexity and the unique ordered extremum, the physical branch and exact determinant, and the complete isotropic spectral measure, at the stated scopes. |

Original review classification and limitations: independently reviewed; spectral-interface collaboration disclosed

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

<a id="decision-candidate-0004"></a>

### Historical assessment candidate-0004

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T02:52 |
| status | proved |
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#inputs-and-exact-optimization) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](#identifying-the-physical-solution-and-the-determinant) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0181_v1.md#original-f0071-account) | Complete scalar and commuting minimax argument (equations (1)-(7)) and the full isotropic-covariance extension (equations (1)-(15)): strict convexity and the unique ordered extremum, the physical branch and exact determinant, and the complete isotropic spectral measure, at the stated scopes. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Complete scalar and commuting minimax argument (equations (1)-(7)) and the full isotropic-covariance extension (equations (1)-(15)): strict convexity and the unique ordered extremum, the physical branch and exact determinant, and the complete isotropic spectral measure, at the stated scopes.

Review: [Exact material](../audits/reviews/Yin_R_F0181_v1.md#original-f0071-account).

Material covered by that review: [Exact material](Yin_C_F0122_v1.md).

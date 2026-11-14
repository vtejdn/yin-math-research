---
author: Yin
---

# A Borel drift and a variable Gaussian covariance over a planar normal coordinate

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(Z\) be the coordinate function of a compactly supported diffuse planar probability \(\mu\), put \(N=L^\infty(\mu)\), and take a standard semicircular \(S=S^*\) free from \(N\) with the free product trace.
For a nonnegative symmetric Borel kernel \(b(z,v)=b(v,z)\), assume the row bound
\[
                \rho^2=\operatorname*{ess\,sup}_{v}
                                  \int b(z,v)^2\,d\mu(z)<\infty .
\]
Let \(T_b=T_b^*\) be its bounded first-chaos field, with kernel \(b\) in \(H_1=L^2(\mu^2)\), where a separated kernel \(a(z)c(v)\) represents \(a(Z)Sc(Z)\).
Let \(f\in L^\infty(\mu)\) be real.
Set \(B=f(Z)+T_b\), use the intrinsic algebra \(W^*(Z,B)\), and write \(H_k=L^2(\mu^{k+1})\) for the relative Wick spaces of the ambient free product.
The following conditions are equivalent.

1. The pair \((Z,B)\) has [actual starred ACSY](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) on its represented starred polynomial core.
2. The pair satisfies the full strong dual condition on the intrinsic tracial Hilbert space.
3. The scalar marginal \(Z\) has an actual vacuum \(\zeta\), \(b>0\) almost everywhere, and each coefficient in (1) is square integrable on its product space.
   \[
   b(z,v)^{-1},\qquad
   J(z,v)=\frac{f(z)-f(v)}{(z-v)b(z,v)},\qquad
   K(z,w,v)=
       \frac{b(w,v)/b(z,w)-b(z,w)/b(w,v)}{\bar z-\bar v}.
   \tag{1}
   \]

The endpoint diagonal is product-null.
The marginal premise in item 3 can equivalently be stated as finite squared Menger curvature and finite squared maximal linear density integral by the [scalar geometric criterion](Yin_C_F0255_v1.md#statement).
Under these conditions the intrinsic algebra equals \(W^*(N,S)\), and in \(H_0\oplus H_1\oplus H_2\) the actual coordinate vacua are
\[
                     \xi_Z=\zeta\oplus(-\overline J)\oplus K,\qquad
                     \xi_B=0\oplus b^{-1}\oplus0 .                      \tag{2}
\]
In particular the squared norm at \(Z\) is \(\|\zeta\|_2^2+\|J\|_2^2+\|K\|_2^2\).
Both original canonical closures and their adjoints contain every bounded vector in their domains, and the right column bounds hold at both coordinates for the pair and its adjoint pair.
The row bound allows unbounded \(b\), and \(f\) need only satisfy the weighted condition in (1).

## Argument

### Extracting the three tests on the target core

The [one-channel representation](Yin_C_F0157_v2.md#bounded-coordinates-phase-and-generation) gives \(\|T_b\|\le2\rho\), \(T_b\Omega=b\), and identifies the two endpoint actions with multiplication in those variables.
For an actual pair, the [normal generator formulas](Yin_C_F0076_v1.md#statement) give the scalar divided difference at \(Z\) and zero derivative of the omitted starred letters.
Projection of the \(Z\) vacuum onto \(H_0\) therefore gives \(\zeta\), and the \(B\) vacuum is orthogonal to \(H_0\).
Represent intrinsic vectors inside the ambient Wick space.
For marginal polynomials \(\alpha,\gamma\), evaluating the \(B\)-vacuum identity on \(\alpha B\gamma\) and using its zero \(H_0\) component gives
\(\langle P_{H_1}\xi_B,\alpha(z)b(z,v)\gamma(v)\rangle=\tau(\alpha)\tau(\gamma)\).
The product of \(b\) and \(\overline{P_{H_1}\xi_B}\) is integrable.
Polynomial rectangles determine the measure, giving \(b\,\overline{P_{H_1}\xi_B}=1\) almost everywhere.
Thus \(b>0\) almost everywhere and \(1/b\in H_1\).
Since the target algebra contains \(N\), it contains \(B-f(Z)=T_b\).
Positive amplitude gives \(W^*(N,T_b)=W^*(N,S)\) by density of the vectors \(\alpha T_b\gamma\Omega\) in degree one and conditional expectation fixing the bounded element \(S\).

Write \(d_f(z,v)=(f(z)-f(v))/(z-v)\) off the diagonal.
Take smooth marginal functions \(\alpha,\gamma\) with supports at positive distance, and a marginal polynomial \(q\).
The smooth endpoints are admissible by uniform polynomial approximation with their first derivatives on a rectangle and the product rule with the bounded target letter \(B\). [Separated endpoint vacuum tests](Yin_C_F0156_v1.md#actual-target-moment-tests)
The identification from such rectangles uses the complement of the null endpoint diagonal.
For example, it can be exhausted by countably many products of open sets with positively separated closures, where smooth endpoint functions determine finite measures.

For the \(Z\) derivative, \(\alpha B\gamma\) has zero scalar part because \(\alpha\gamma=0\), and one-edge kernel \(\alpha(z)b(z,v)\gamma(v)\).
In the double trace of its derivative the one-field terms are centered.
Ordinary telescoping of the scalar difference of the zero function \(\alpha f\gamma\) shows that the two endpoint derivative terms of the drift sum to
\(-\iint\alpha(z)d_f(z,v)\gamma(v)\,d\mu(z)d\mu(v)\).
The denominator stays away from zero on its support.
This identity uses pointwise values of the drift at the two endpoints.
It follows that \(b\,\overline{P_{H_1}\xi_Z}=-d_f\), so \(J\in H_1\) and \(P_{H_1}\xi_Z=-\overline J\).

Next test \(\alpha BqB\gamma\).
Its scalar part is zero by the disjoint endpoints, its one-edge kernel is
\[
      \alpha(z)b(z,v)\gamma(v)\big(f(z)q(z)+f(v)q(v)\big),
\]
and its two-edge kernel is \(\alpha(z)b(z,w)q(w)b(w,v)\gamma(v)\).
The latter belongs to \(H_2\) since \(\int b(z,w)^2 b(w,v)^2\,d\mu^3\le\rho^4\).
In the derivative double trace, the terms involving exactly one field vanish by centering and the trace factorization on the two legs.
The terms containing two drifts equal
\[
 -\iint \alpha(z)d_f(z,v)\gamma(v)
              \big(q(v)f(v)+f(z)q(z)\big)\,d\mu(z)d\mu(v).
\]
Indeed the five-factor scalar difference quotient of \(\alpha f q f\gamma=0\) telescopes, and the two slots occupied by \(f\) give exactly the negative of the terms where only \(\alpha,q,\gamma\) are differentiated.
Both drift-slot contributions are supported at separated endpoints.
This is precisely the pairing with the already identified one-edge vacuum.
The remaining two-field double trace is the [centered quadratic test](Yin_C_F0157_v2.md#necessary-integrals-on-the-target-core), whose density against \(\alpha(z)q(w)\gamma(v)\) is \((b(w,v)^2-b(z,w)^2)/(z-v)\).
Comparison with the two-edge kernel yields \(P_{H_2}\xi_Z=K\) by localization in the endpoints and polynomial density in \(w\).
This proves every necessary integral in (1).

### Reference derivations and weak testing of the Borel coefficients

Assume item 3, which also gives generation as above.
Use the free reference algebra generated algebraically by \(Z,Z^*,S\).
Its base derivative \(\delta_N\) is the free lift of the scalar divided difference and kills \(S\).
It has vacuum \(\zeta\) and both bounded sliced estimates on bounded inputs. [Free reference estimate](Yin_C_F0209_v1.md#reference-corrections-for-bounded-positive-matrices)
An insertion \(\delta_\beta\) means the free outer derivation with \(\delta_\beta S=\beta\) and zero on the base.
Define the three components of the insertion by
\[
\begin{split}
 \beta_0(z,v)&=-J(z,v),\\
 A_0(z,w,v)&=\frac{b(w,v)/b(z,v)-1}{z-w}
                  &&\text{in } H_0\otimes H_1,\\
 A_1(z,w,v)&=\frac{1-b(z,w)/b(z,v)}{w-v}
                  &&\text{in } H_1\otimes H_0 .
\end{split}                                                              \tag{3}
\]
Here \(\beta_0\) is in \(H_0\otimes H_0\), and put \(\beta_1=A_0\oplus A_1\).
The arrays are the one-channel reference corrections in the cited calculation.
To check their joint square integrability, write \(r=b(w,v)/b(z,w)\).
After reversal of the path variables for the two respective arrays their absolute values become \(|r-1|/|z-v|\) and \(|1-r^{-1}|/|z-v|\).
The product \((r-1)(1-r^{-1})\) is nonnegative, so the sum of their squared norms is at most \(\|K\|_2^2\).
Componentwise adjoint and reinsertion of the noise give the two-edge vacuum \(K\), as is also seen by summing \((r-1)/(\bar z-\bar v)\) and \((1-r^{-1})/(\bar z-\bar v)\).
The degree-zero insertion gives the one-edge vacuum \(\overline{\beta_0}=-\overline J\), because the path endpoints stay in their order under reinsertion of a scalar tensor with componentwise adjoint.

Set \(\Delta_Z=\delta_N+\delta_{\beta_0}+\delta_{\beta_1}\) and \(\Delta_B=\delta_{1/b}\) on the reference core.
Their actual vacua are the vectors in (2).
The [finite-degree cut estimates](Yin_C_F0209_v1.md#contractions-with-a-single-inserted-color) apply to each of the degree-zero and degree-one components, bounding both sliced orientations on the reference operator unit ball.
By [the two-slice theorem](Yin_C_F0072_v1.md#statement) the closed right contractions \(E'_j=\overline{(\mathrm{id}\otimes\tau)\Delta_j}\) and their Hilbert adjoints have every bounded vector in their domains and are bounded from operator norm to Hilbert norm there.
The contractions kill \(1\).

We verify their commutators with \(f(Z)+T_b\) using Hilbert matrix elements on reference polynomials.
This verification only requires integrated coefficient identities against bounded Wick polynomial tests.
The unweighted divided difference \(d_f=bJ\) is in \(L^1(\mu^2)\) by Cauchy–Schwarz, even if its \(L^2\) norm is infinite.
The two formal divided differences of \(b\) are
\[
 \frac{b(z,v)-b(w,v)}{z-w}=-b(z,v)A_0(z,w,v),\qquad
 \frac{b(z,w)-b(z,v)}{w-v}=-b(z,v)A_1(z,w,v).
 \tag{4}
\]
Both right sides are in \(L^1(\mu^3)\), because \(b(z,v)\in L^2(\mu^3)\) and (3) lies in \(L^2\).

Here is the weak scalar test in the integrability range used in (4).
If \(g\in L^2(\mu)\) and its pointwise divided difference \(d_g\) belongs to \(L^1(\mu^2)\), then for a marginal polynomial tensor \(U\),
\[
                      \int\overline U\, d_g\,d\mu^2
                           =\langle\delta_N^*U,g\rangle .                 \tag{5}
\]
Indeed regularized difference quotients are \(d_g(z,v)|z-v|^2/(|z-v|^2+\varepsilon^2)\) and converge in \(L^1\) by domination.
The regularized tensor adjoints of \(U\) converge weakly in \(L^2(\mu)\) to \(\delta_N^*U\) by (M5) in the [scalar weak integration-by-parts argument](Yin_C_F0156_v1.md#weak-algebraic-tensor-integration-by-parts).
Pairing the first convergence against the bounded \(U\) and the second against \(g\) proves (5).
With an additional parameter, each polynomial tensor test is a finite sum of products with a bounded test in that parameter.
Tensoring the weak \(L^2\) adjoint convergence with that fixed polynomial and using the joint \(L^1\) convergence of the differences proves (5) integrated in the extra variable.

To see how (5) gives the commutator, first take polynomial approximants to \(f\) bounded uniformly and converging almost everywhere.
At \(b\) first use \(b_m=\min(b,m)\), then at each fixed \(m\) use uniformly bounded real symmetric polynomial kernels tending almost everywhere to \(b_m\). [Bounded-kernel approximation and tensor commutators](Yin_C_F0156_v1.md#bounded-gaussian-kernels-and-the-original-reference-commutator)
The corresponding bounded operators converge strongly-star to their targets at each fixed \(m\).
Also \(T_{b_m}\to T_b\) strongly-star because their row norms are bounded by \(\rho\) and \(b_m\to b\) in \(L^2\).
For reference polynomials \(u,v\) and a polynomial approximant \(a\) the exact identity is
\[
    \langle u,[E'_j,a]v\rangle=\langle u\otimes v^*,\Delta_j a\rangle.
 \tag{6}
\]
On the left one can transfer \(E'_j\) to its Hilbert adjoint on \(u\), so strong-star convergence of the bounded operators gives convergence of the commutator matrix elements.
On the right, the \(\delta_N\) term from a polynomial base input has degree \((0,0)\), and that from a polynomial field kernel has degrees \((0,1),(1,0)\) and the two formal endpoint differences in (4).
The projections of \(u\otimes v^*\) onto these degrees are finite sums of tensors of bounded marginal polynomials in the path variables by the Wick recurrence.
For fixed \(m\), convergence of the pairings of the formal differences of the polynomial kernels follows by moving the scalar derivative in the varying leg onto the fixed polynomial tensor and using \(L^2\) convergence of the kernels.
Equation (5) identifies this pairing with the ordinary integral of the formal difference of \(b_m\).
The clipping function is \(1\)-Lipschitz, so these differences are dominated by the absolute formal differences of \(b\) in (4).
They converge in \(L^1\) as \(m\) increases.
The same fixed-test argument gives \(d_f\) on the base input \(f\).

The insertion terms vanish on every marginal input.
On a polynomial field their arrays are the field kernel at the two external endpoints times the inserted tensor, by the [reference coefficient calculation](Yin_C_F0209_v1.md#reference-corrections-for-bounded-positive-matrices).
They pass first to \(b_m\) against fixed polynomial tests by bounded convergence at that \(m\).
They then pass to \(b\) by \(L^1\) domination, using the integrability of \(b(z,v)|\beta_0|,\ b(z,v)|A_0|,\ b(z,v)|A_1|\) and \(b(z,v)/b(z,v)=1\) almost everywhere.
Consequently the degree-zero pairing for \([E'_Z,B]\) vanishes by \(d_f+b\beta_0=0\), and its two degree-one pairings vanish by (4).
For \([E'_B,B]\), the only surviving array is \(b/b=1\), giving \(P_\Omega\) in (6).
At \(Z\) the two commutators are \(P_\Omega\) and zero by the reference values on \(Z\).
At \(Z^*\) they are respectively the operator with the forced normal phase kernel and zero.
These equalities extend from reference polynomial tests to all bounded input vectors by bounded strong-star polynomial approximation, operator-norm-to-Hilbert boundedness on bounded elements and weak closedness of the graphs of \(E'_j\).
In particular, for a bounded net converging strongly-star to \(v\), every weak cluster point of the contraction images is the graph value at \(v\).

### Original domains and columns

The negatives of the reference contractions therefore give the generator-first strong system on the intrinsic algebra.
The [normal strong-to-ACSY theorem](Yin_C_F0070_v1.md#statement) gives actual target derivations with the forced starred generator values.
The normalized reference contractions agree with the target right slices on all starred words, by the generator commutators, the product rule and their common value zero at \(1\).
Their Hilbert adjoints at \(1\) consequently give the target vacuum identities (2), and density of the target core fixes the full vacuum vectors.
For the adjoint tuple the reference construction uses the conjugate base variable, conjugating the base difference denominators while \(f,b\) remain real in the relabelled variables.
The conditions (1) and all norms are unchanged.
The right bound in this orientation supplies a left one-input bound for the original target derivation by flip-adjoint.
Part B of the two-slice theorem now gives the bounded-vector domains for the actual original target closure and adjoint at each coordinate.
This proves the sufficiency and, together with the normal strong-to-ACSY implication and the target tests, the equivalence.

For the column assertion adjoin two standard semicirculars free from \(N,S\) and from each other.
Use the same reference derivatives at the two old coordinates, killing the added semicirculars.
The free scalar lift and finite-degree cut bounds still apply with the two extra noise colors, using zero insertions at both new slots.
Testing with the added colors projects the tensor test onto the matching degree and color components and preserves the matrix elements above.
The resulting right slices on the enlarged target core have the same single-input boundedness and kill the new letters in their derivations.
The enlargement has actual vacua by free extension from the original pair.
In the [two-semicircular column encoding](Yin_C_F0241_v1.md#two-gaussian-channels-supply-the-column-test-inside-the-model), the two free Haar unitaries obtained in their continuous functional calculi commute as left multipliers with these closed slices on bounded vectors, by the zero derivatives.
Encoding an old column \((p_k)\) in \(\sum_k U^k V U^{-k}p_k\) bounds its input norm by \(2\|\sum_kp_k^*p_k\|^{1/2}\) and gives the sum of the squared old output norms by orthogonality.
The same reasoning on the adjoint tuple proves the asserted two oriented column bounds.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T12:14 |
| status | open |
| reason | Fix the weighted Borel-drift criterion, its three orthogonal vacuum components and the original two-domain and column conclusions for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Drifted single-channel Gaussian pair with a row-bounded covariance, measurable drift, actual vacuum criterion, both canonical domains and columns. |
| argument | [Argument](#argument) | Separated target moment tests, drift cancellations, degree-zero and degree-one insertions, weak integrable-kernel testing, and original mixed-core and column transfer. |
| dependency | [Gaussian fields and generation](Yin_C_F0157_v2.md#bounded-coordinates-phase-and-generation) | Row-norm bound, clipped field convergence, and generation under positive amplitude. |
| dependency | [Normal phases](Yin_C_F0076_v1.md#statement) | Actual scalar restriction, omitted starred generator values and flip-adjoint orientation. |
| dependency | [Target moment tests](Yin_C_F0156_v1.md#actual-target-moment-tests) | Smooth separated endpoint functions in the target graph and vacuum Leibniz pairings. |
| dependency | [Centered quadratic test](Yin_C_F0157_v2.md#necessary-integrals-on-the-target-core) | Degree-two coefficient and integrable quadratic test for the row-bounded field. |
| dependency | [Reference corrections](Yin_C_F0209_v1.md#reference-corrections-for-bounded-positive-matrices) | Free base derivative, signed endpoint arrays, adjoint reinsertion and action of a field on inserted tensors. |
| dependency | [Finite-degree cut estimates](Yin_C_F0209_v1.md#contractions-with-a-single-inserted-color) | Actual vacua and both bounded slice orientations of the relative degree-zero and degree-one reference insertions. |
| dependency | [Weak integration by parts](Yin_C_F0156_v1.md#weak-algebraic-tensor-integration-by-parts) | Formula (M5) and weak scalar algebraic adjoint convergence used for \(L^1\) differences tested by bounded polynomials. |
| dependency | [Kernel commutator tests](Yin_C_F0156_v1.md#bounded-gaussian-kernels-and-the-original-reference-commutator) | Fixed polynomial tensor tests, bounded strong-star approximation and identification of actual reference matrix elements. |
| dependency | [Normal strong-to-ACSY theorem](Yin_C_F0070_v1.md#statement) | Reconstructing the canonical target derivations on the represented core from the supplied strong duals. |
| dependency | [Original two-slice theorem](Yin_C_F0072_v1.md#statement) | Full bounded-vector domains for the actual closures and Hilbert adjoints in both reference and target applications. |
| dependency | [Column encoding](Yin_C_F0241_v1.md#two-gaussian-channels-supply-the-column-test-inside-the-model) | Free semicircular enlargement and Haar orthogonality on a column of old target polynomials. |
| dependency | [Scalar geometric criterion](Yin_C_F0255_v1.md#statement) | Optional equivalent geometric formulation of the scalar vacuum premise. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T12:25 |
| status | proved |
| reason | Adopt the drifted Gaussian equivalence, its exact vacuum vectors and the original full-domain and finite-column consequences. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Drifted single-channel Gaussian pair with a row-bounded covariance, measurable drift, actual vacuum criterion, both canonical domains and columns. |
| argument | [Argument](#argument) | Separated target moment tests, drift cancellations, degree-zero and degree-one insertions, weak integrable-kernel testing, and original mixed-core and column transfer. |
| dependency | [Gaussian fields and generation](Yin_C_F0157_v2.md#bounded-coordinates-phase-and-generation) | Row-norm bound, clipped field convergence, and generation under positive amplitude. |
| dependency | [Normal phases](Yin_C_F0076_v1.md#statement) | Actual scalar restriction, omitted starred generator values and flip-adjoint orientation. |
| dependency | [Target moment tests](Yin_C_F0156_v1.md#actual-target-moment-tests) | Smooth separated endpoint functions in the target graph and vacuum Leibniz pairings. |
| dependency | [Centered quadratic test](Yin_C_F0157_v2.md#necessary-integrals-on-the-target-core) | Degree-two coefficient and integrable quadratic test for the row-bounded field. |
| dependency | [Reference corrections](Yin_C_F0209_v1.md#reference-corrections-for-bounded-positive-matrices) | Free base derivative, signed endpoint arrays, adjoint reinsertion and action of a field on inserted tensors. |
| dependency | [Finite-degree cut estimates](Yin_C_F0209_v1.md#contractions-with-a-single-inserted-color) | Actual vacua and both bounded slice orientations of the relative degree-zero and degree-one reference insertions. |
| dependency | [Weak integration by parts](Yin_C_F0156_v1.md#weak-algebraic-tensor-integration-by-parts) | Formula (M5) and weak scalar algebraic adjoint convergence used for \(L^1\) differences tested by bounded polynomials. |
| dependency | [Kernel commutator tests](Yin_C_F0156_v1.md#bounded-gaussian-kernels-and-the-original-reference-commutator) | Fixed polynomial tensor tests, bounded strong-star approximation and identification of actual reference matrix elements. |
| dependency | [Normal strong-to-ACSY theorem](Yin_C_F0070_v1.md#statement) | Reconstructing the canonical target derivations on the represented core from the supplied strong duals. |
| dependency | [Original two-slice theorem](Yin_C_F0072_v1.md#statement) | Full bounded-vector domains for the actual closures and Hilbert adjoints in both reference and target applications. |
| dependency | [Column encoding](Yin_C_F0241_v1.md#two-gaussian-channels-supply-the-column-test-inside-the-model) | Free semicircular enlargement and Haar orthogonality on a column of old target polynomials. |
| dependency | [Scalar geometric criterion](Yin_C_F0255_v1.md#statement) | Optional equivalent geometric formulation of the scalar vacuum premise. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0269_v1.md#finding) | Whole candidate including the integrable weak difference quotients, row-bounded unbounded amplitudes, both original domains and oriented column estimates. |

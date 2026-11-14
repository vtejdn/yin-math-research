---
author: Yin
---

# Exact column costs under bilipschitz relabelling and their Lipschitz variations

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X\) be a finite tuple of bounded normal generators of a finite von Neumann algebra \(M\) with faithful normal probability trace \(\tau\), satisfying actual starred ACSY.
Fix \(i\), write \(Z=X_i\) with law \(\mu\), and let \(P_X=\mathbb C\langle X,X^*\rangle\), \(H=L^2(M,\tau)\), \(\delta_X=\delta_{X,i}\), \(C=\mathrm{id}\otimes\tau\).
For a bounded Borel symbol \(b\) on the distinguished spectral square define
\[
 \mathfrak c_X(b)=
 \sup_{\|\sum_j p_j^*p_j\|\le1}
    \left(\sum_j\|C I_b\delta_X p_j\|_2^2\right)^{1/2},
\]
where \(p_j\) range over finite columns in \(P_X\) and \(I_b\) is the inner spectral calculus on the coarse tensor space.
In particular \(I_{a\otimes d}(v\otimes w)=va(Z)\otimes d(Z)w\).
The value \(+\infty\) is allowed and diagonal values are immaterial.

1. Replace \(Z\) by \(\phi(Z)\) for a bilipschitz homeomorphism of the whole plane, keeping the other coordinates, and denote the resulting tuple by \(Y\).
   It is actual, and for every bounded Borel symbol \(b\) in the \(Y\) coordinate,
   \[
    \mathfrak c_Y(b)=\mathfrak c_X\!\left(K_\phi\, b(\phi(z),\phi(w))\right),
    \qquad K_\phi(z,w)=\frac{z-w}{\phi(z)-\phi(w)} .                     \tag{1}
   \]
   Thus \(\mathfrak c_X(K_\phi)\) is precisely the original right column cost at \(Y_i\).
2. Let \(\mathcal B\) be the open unit ball of the complex Banach space of Lipschitz maps \(f:\mathbb C\to\mathbb C\) with \(f(0)=0\), in the Lipschitz norm.
   Write \(Y_f\) for the tuple obtained using \(\phi_f=\mathrm{id}+f\) and \(Dg(z,w)=(g(z)-g(w))/(z-w)\) off the diagonal.
   Suppose \(\mathfrak c_{Y_f}(1)<\infty\) for every \(f\in\mathcal B\).
   There is a dense open subset of \(\mathcal B\) such that at each of its points \(f_0\) there are constants \(B,R>0\) with
   \[
           \sup_{\|g\|_{\rm Lip}\le1,\ g(0)=0}
              \mathfrak c_{Y_{f_0}}\big((Dg)^m\big)\le B R^{-m}
                              \qquad(m\ge1).                              \tag{2}
   \]
   The functions \(g\) and their divided differences here are in the new coordinate \(\phi_{f_0}(Z)\).
   In particular, if in some nonempty open subset of \(\mathcal B\) every center has unbounded first-order supremum in (2), then some \(Y_f\) in that subset has infinite right column cost.
   Its two-free-Haar enlargement is actual and has no bare full-domain dual system.
3. At any actual center \(Y\), the first-order supremum in (2) equals a supremum of Lipschitz dual norms of limits of zero-mass measures obtained from its actual mixed columns and Hilbert tests.
   Precisely, let \(\Pi_Y\) be the joint projection-valued measure of its two inner marginal actions.
   For a normalized finite column \(p\) from \(P_Y\) and a Hilbert test column \(q\) with \(\sum_j\|q_j\|_2^2\le1\), set
   \[
     \beta_{p,q}(A)=\sum_j\langle q_j\otimes1,\Pi_Y(A)\delta_Y p_j\rangle,
     \qquad
     \lambda_\epsilon=(\pi_1)_*
       \left(\frac{1_{|z-w|>\epsilon}}{z-w}\,\beta_{p,q}\right)
       -(\pi_2)_*\left(\frac{1_{|z-w|>\epsilon}}{z-w}\,\beta_{p,q}\right). \tag{3}
   \]
   The inner product is linear in the second variable, and \(\pi_1,\pi_2\) are the two coordinate projections.
   Equip compactly supported zero-mass complex measures with the norm
   \[
      \|\lambda\|_{\rm Lip^*}
        =\sup_{\|g\|_{\rm Lip}\le1,\ g(0)=0}\left|\int g\,d\lambda\right|
   \]
   using complex-valued functions on the plane.
   Then each \(\lambda_\epsilon\) has a limit \(\Lambda_{p,q}\) in the completion for this norm, and
   \[
             \sup_{\|g\|_{\rm Lip}\le1,\ g(0)=0}\mathfrak c_Y(Dg)
                       =\sup_{p,q}\|\Lambda_{p,q}\|_{\rm Lip^*}.          \tag{4}
   \]
   This transportation norm is used for complex zero-mass measures in its stated dual sense.

## Argument

### Comparing the two represented cores in both directions

By [planar bilipschitz invariance](Yin_C_F0256_v1.md#statement) the new tuple has actual ACSY.
Both cores generate \(M\) and the inner marginal calculus identifies a symbol of the new spectral variables with its pullback by \((\phi,\phi)\) in the old calculus.
The [coarse measure-class calculation](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) and diffuseness imply that the diagonal has zero coarse spectral projection.
The two secant ratios for \(\phi,\phi^{-1}\) are bounded and are reciprocals after the change of variables.

We use the graph approximation in the [mixed-core transfer proof](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) before applying a bounded multiplier.
Bounded Lipschitz functions on the compact distinguished spectrum admit uniform polynomial approximants with uniformly bounded Lipschitz constants on that spectrum.
Their marginal divided differences converge in the coarse \(L^2\) norm by domination off the diffuse diagonal, including for the conjugate functions.
Bounded strong-star graph approximation then extends to products and their adjoints by the outer Leibniz rule.
For a finite unit column \(p\) in \(P_Y\) it yields \(P_X\)-columns approximating \(p\) in the entrywise graph of \(\overline\delta_X\), with limsup column norm at most \(1+\varepsilon\) for any \(\varepsilon>0\).
The norm bound uses polynomial approximants to a smooth cutoff applied to the squared column modulus, equal to one near \([0,1]\), as in that proof.
It concerns the input before any symbol is inserted and requires no Schur multiplier bound on the secant.

On \(P_Y\), \(I_{K_\phi}\overline\delta_X=\delta_Y\).
At \(\phi(Z)\) the multiplier cancels the forward divided difference, at \(\phi(Z)^*\) it leaves the forced starred phase in the new coordinate, and both sides kill the omitted starred letters. [Forced normal derivatives](Yin_C_F0076_v1.md#statement)
The product rule on the bounded graph approximants establishes the identity on mixed words.
Inserting \(b\) now amounts to inserting \(b(\phi(z),\phi(w))K_\phi\) in the old coarse space.
Applying the bound on the approximating columns and then taking \(\varepsilon\) to zero proves the inequality from left to right in (1) whenever its right side is finite.
It holds as an extended inequality in all cases.
For the reverse inequality interchange \(X,Y\) and use \(\phi^{-1}\) in the same approximation and generator calculation.
Applying the resulting inequality to \(K_\phi\,b(\phi(z),\phi(w))\) in the old variables cancels the inverse secant and leaves \(b\) in the new variables.
This gives equality, including the possible infinite values.

### Category and differentiation at a regular center

For \(f\in\mathcal B\) the map \(\phi_f\) separates distances by at least \(1-\|f\|_{\rm Lip}\) times the original distance.
It maps onto the plane, since for every \(a\in\mathbb C\) the contraction \(z\mapsto a-f(z)\) has a fixed point.
In (1) its secant multiplier is \((1+Df)^{-1}\).
This symbol depends continuously on \(f\) in supremum norm locally in \(\mathcal B\), because the denominator is bounded below there.
For a fixed finite original column \(p\), the output depends continuously on the symbol by the Hilbert-space bound on inner multiplication.
Thus \(F(f)=\mathfrak c_{Y_f}(1)\), the supremum of these continuous norms on fixed original columns, has relatively closed sublevel sets.

Under the finiteness hypothesis the closed sets \(\{F\le n\}\), \(n\in\mathbb N\), cover \(\mathcal B\).
Their relative interiors have dense union by the Baire category theorem applied inside each nonempty open subset of the Banach-space ball.
At any point \(f_0\) in this union choose \(s>0\) and \(B<\infty\) so the ball of radius \(s\) around \(f_0\) lies in \(\mathcal B\) and \(F\le B\) on it.
The same argument is local if the initial finiteness assumption is only made on a nonempty open subset.

Put \(a=1+Df_0\), \(\phi_0=\mathrm{id}+f_0\), and \(h=g\circ\phi_0\) for a normalized direction \(g\) in the statement.
Then \(h(0)=0\) and \(\|h\|_{\rm Lip}\le1+\|f_0\|_{\rm Lip}\).
Choose \(R>0\) with \(R(1+\|f_0\|_{\rm Lip})<\min(s,1-\|f_0\|_{\rm Lip})\).
For \(|t|\le R\) the reciprocal \((a+tDh)^{-1}\) is analytic in the parameter on a neighborhood of the closed disk as a bounded spectral symbol, by the uniformly convergent geometric series there.
On each normalized \(P_X\)-column the norm of the vector obtained by inserting this symbol and taking the right slice is at most \(B\), by (1) and the bound on \(F(f_0+th)\).
Cauchy's coefficient formula on \(|t|=R\) bounds its \(m\)-th power-series coefficient by \(BR^{-m}\), uniformly in the input column.
This coefficient is the sliced insertion of \((-1)^m(Dh)^m a^{-m-1}\).
On the original spectral square \(Dh(z,w)=Dg(\phi_0(z),\phi_0(w))a(z,w)\), so (1) converts the coefficient's column cost exactly to \(\mathfrak c_{Y_{f_0}}((Dg)^m)\).
This proves (2).
Its local contrapositive gives a single infinite-cost relabelling in the open set specified in part 2.
The [two-Haar enlargement theorem](Yin_C_F0208_v1.md#statement) then gives the actual normal tuple with no bare full-domain system under that hypothesis.
Failure of the first-order condition at a single center does not establish the open-set hypothesis.

### The transportation norm of a tested column

For a fixed \(p,q\), (3) defines a finite complex spectral measure, since Cauchy–Schwarz on disjoint spectral projections bounds its variation by
\((\sum_j\|q_j\|_2^2)^{1/2}(\sum_j\|\delta_Yp_j\|_2^2)^{1/2}\).
It is absolutely continuous with respect to the product law by the coarse measure-class calculation.
The adjoint of \(C\) sends \(q_j\) to \(q_j\otimes1\).
Consequently its integral against a bounded symbol \(b\) equals \(\sum_j\langle q_j,C I_b\delta_Yp_j\rangle\), with the symbol integrated linearly.

At every \(\epsilon>0\) the truncated measure before either push-forward has finite variation, and the two push-forwards have the same mass.
For a Lipschitz unit test \(g\), integration of \(g\) against their difference gives exactly \(\int_{|z-w|>\epsilon}Dg(z,w)\,d\beta_{p,q}\).
These values differ from \(\int Dg\,d\beta_{p,q}\) by at most \(|\beta_{p,q}|\{0<|z-w|\le\epsilon\}\), uniformly in \(g\), using the vanishing diagonal mass.
This tends to zero for each fixed pair \(p,q\).
It proves convergence in the stated norm completion without assuming absolute integrability of \(\beta_{p,q}/(z-w)\) at the diagonal.
The limit has norm \(\sup_g|\int Dg\,d\beta_{p,q}|\).
Taking the supremum over columns and tests and using Hilbert norm duality yields (4), since the three suprema can be taken in either order.
An obstruction obtained from (4) must therefore concern the spectral measures of the actual column tests.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T12:16 |
| status | open |
| reason | Fix the exact two-core comparison, category-based necessary estimates and column-induced Lipschitz dual norms for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Extended-real column costs for bounded symbols, local category obstruction, all first and higher Lipschitz variations and the first-order transportation norm. |
| argument | [Argument](#argument) | Both norm-controlled graph approximations, analytic estimates on actual columns, local Baire contrapositive and convergence for complex column measures. |
| dependency | [Bilipschitz ACSY invariance](Yin_C_F0256_v1.md#statement) | The new represented tuple is actual under each whole-plane bilipschitz coordinate change. |
| dependency | [Mixed-core graph approximation](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Entrywise derivative convergence, generator identification and column-norm restoration, in turn for the forward and inverse relabellings. |
| dependency | [Normal starred values](Yin_C_F0076_v1.md#statement) | Diffuseness and forced original and transformed generator values, including the omitted starred letters. |
| dependency | [Coarse measure class](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Product-law absolute continuity of inner coarse spectral measures and vanishing mass on the diffuse diagonal. |
| dependency | [Two-Haar enlargement](Yin_C_F0208_v1.md#statement) | Infinite right column cost for one actual normal coordinate excludes all bare full-domain systems on the enlarged tuple. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T12:22 |
| status | proved |
| reason | Adopt the bidirectional cost identity and its local variation and dual-norm consequences after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Extended-real column costs for bounded symbols, local category obstruction, all first and higher Lipschitz variations and the first-order transportation norm. |
| argument | [Argument](#argument) | Both norm-controlled graph approximations, analytic estimates on actual columns, local Baire contrapositive and convergence for complex column measures. |
| dependency | [Bilipschitz ACSY invariance](Yin_C_F0256_v1.md#statement) | The new represented tuple is actual under each whole-plane bilipschitz coordinate change. |
| dependency | [Mixed-core graph approximation](Yin_C_F0244_v1.md#passing-to-the-original-core-of-the-relabelled-tuple) | Entrywise derivative convergence, generator identification and column-norm restoration, in turn for the forward and inverse relabellings. |
| dependency | [Normal starred values](Yin_C_F0076_v1.md#statement) | Diffuseness and forced original and transformed generator values, including the omitted starred letters. |
| dependency | [Coarse measure class](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Product-law absolute continuity of inner coarse spectral measures and vanishing mass on the diffuse diagonal. |
| dependency | [Two-Haar enlargement](Yin_C_F0208_v1.md#statement) | Infinite right column cost for one actual normal coordinate excludes all bare full-domain systems on the enlarged tuple. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0266_v1.md#whole-proof-finding) | All three assertions, the two represented core transfers and the conditional obstruction on an open set. |

---
author: Yin
---

# Spectral relabelling of normal coordinates and column bounds for Schur multipliers

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_i)_{i=1}^d\) be a finite bounded normal generating tuple in a finite von Neumann algebra with faithful normal probability trace.
Assume the full [ACSY condition](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Write \(P_X=\mathbb C\langle X,X^*\rangle\), \(N_i=W^*(X_i)\), and let \(\mu_i\) be the diffuse law of \(X_i\).
For each coordinate let \(Y_i=h_i(X_i)\), where \(h_i\) is bounded Borel and one-to-one on a conull Borel set with Borel inverse there.
The generated von Neumann algebras are unchanged.
Let \(\eta_i\) be the vacuum of the partial liberation derivation \(\gamma_i\), with sign convention \(\gamma_i f=f\otimes1-1\otimes f\) on \(N_i\).
Let \(\nu_i\) be the joint spectral measure of \(\eta_i\) for left and right multiplication by \(X_i\).

1. The coordinate \(Y_i\) has an actual distinguished vacuum on \(P_Y\) if and only if its marginal has an actual scalar vacuum and
   \[
               \iint_{z\ne w}\frac{d\nu_i(z,w)}{|h_i(z)-h_i(w)|^2}<\infty.       \tag{1}
   \]
   Its squared norm is the sum of (1) and the squared scalar vacuum norm.
   If \(h_i^{-1}\) is Lipschitz on the conull image, (1) is automatic.
   This assertion also applies to a coordinate left unchanged when other coordinates are relabelled.
2. In addition suppose \(h_i\) is Lipschitz on its conull domain, and the measurable kernel
   \[
            K_i(z,w)=\frac{z-w}{h_i(z)-h_i(w)}
   \]
   is a Schur multiplier with respect to \(\mu_i,\mu_i\), with norm \(m_i\).
   Suppose \(Y_i\) has the actual vacuum in item 1 and \(c_i(X)<\infty\) for the [original right column](Yin_C_F0208_v1.md#statement).
   Then \(c_i(Y)\le 2m_i c_i(X)\), on the full represented starred polynomial core of \(Y\).
   No regularity on the omitted relabellings beyond the initial Borel assumptions is required.
   The corresponding result for the adjoint tuples uses the conjugate kernel with the same multiplier norm.
3. Let \(S=(S_i)\) be any bounded selfadjoint generating tuple with actual conjugate variables.
   For any real Lipschitz functions \(g_i\) on the spectra, put \(Y_i=S_i+i g_i(S_i)\).
   Then \(Y\) has actual ACSY on its full mixed core.
   Conversely, actual ACSY for such a graph tuple implies actual ACSY for \(S\).
   Whenever \((s-t)/(h_i(s)-h_i(t))\), \(h_i(s)=s+i g_i(s)\), is a measurable Schur multiplier for the law of \(S_i\), the original canonical operator at \(Y_i\) and its Hilbert adjoint both have domains containing every bounded vector.
   If all these kernels are Schur multipliers, the canonical operators witness \(\mathsf S(Y)\).

Here a measurable Schur multiplier acts by pointwise multiplication on square-integrable integral kernels on \(L^2(\mu_i)\) with a uniform bound in their integral-operator norm.
A Lipschitz graph with a corner may violate this multiplier hypothesis. [Correlated two-segment example](Yin_C_F0241_v1.md#statement)

## Argument

### The invariant liberation derivation

Fix a coordinate and suppress its subscript.
Liberation for \(X\) has actual vacuum \(\eta=[X_i^*,\xi_i]\). [Normal recovery criterion](Yin_C_F0238_v1.md#statement)
The derivation \(\gamma\) is closable because \(i\gamma\) is real with an actual vacuum.
For a bounded element in any one marginal algebra, uniformly bounded marginal polynomials converge strongly-star to it by [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001).
Their liberation derivatives converge in Hilbert norm, to \(a\otimes1-1\otimes a\) at the distinguished marginal and zero at an omitted marginal.
For any finite word of such factors, the outer Leibniz sums converge strongly in the coarse space since bounded strongly-star convergent coefficients act strongly on both legs.
Thus the algebra generated algebraically by all the \(N_j\) lies in the closed graph, with the same generator rules.
The adjoint pairing against \(\eta\) persists on that algebra.
It therefore restricts to \(P_Y\), where \(\eta\) is still the vacuum by density.
Its left and right spectral measure in the new coordinate is \((h_i,h_i)_*\nu_i\).
The exceptional sets discarded in defining a Borel inverse have zero weight for either leg by normality of the actions, and the spectral diagonal of \(\eta\) has zero weight by [the marginal liberation adjoint](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint).
Applying the normal recovery criterion to \(Y\) proves item 1.
If \(|z-w|\le L|h_i(z)-h_i(w)|\), the new integral is at most \(L^2\int |z-w|^{-2}\,d\nu_i\), which is finite by the original vacuum.

### Bounded measurable coefficients before the slice

We prove the column estimate for a general bounded Schur symbol \(K\) in the distinguished marginal, on an initial finite column from \(P_X\).
Let \(C=\mathrm{id}\otimes\tau\), \(E=C\delta\) and \(c=c_i(X)\).
In the inner spectral calculus use \(I_{v\otimes w}(a\otimes b)=av\otimes wb\).
A finite bounded column \((b_j)\) anywhere in \(M\) has
\[
                   \sum_j\|\bar E b_j\|_2^2\le c^2\Big\|\sum_j b_j^*b_j\Big\|.     \tag{2}
\]
Indeed approximate the corresponding column in a matrix algebra by bounded core columns strongly-star with the same column norm bound, by matrix Kaplansky density (embed a single column into a square matrix and take the same column after approximation).
The actual vacuum gives closability of \(E\) by [the canonical contraction theorem](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001).
The uniform column bound on the approximants gives weak cluster points in a finite Hilbert direct sum, and the weakly closed graph places each \(b_j\) in the original closure with the claimed bound.
This argument also gives weak convergence of \(\bar E b_\alpha\) to \(\bar E b\) whenever \(b_\alpha\to b\) strongly-star on a bounded ball: every weak cluster point is the unique graph value.

For \(p\in P_X\) and bounded measurable marginal factors \(v,w\),
\[
       C I_{v\otimes w}\delta(p)=(\bar E(pw)-p\bar E(w))v .                     \tag{3}
\]
For polynomial \(w\), this follows by the Leibniz rule and the trace, and requires only boundedness of \(v\).
Bounded marginal polynomial approximants to \(w\) converge strongly-star, giving strong convergence on the left of (3) and weak convergence on the right by (2).

Use the measurable Schur factorization
\[
       K(z,w)=\sum_{\ell}v_\ell(z)w_\ell(w),\qquad
       \Big\|\sum_\ell |v_\ell|^2\Big\|_\infty^{1/2}
       \Big\|\sum_\ell |w_\ell|^2\Big\|_\infty^{1/2}\le m ,
                                                                            \tag{4}
\]
with \(m=\|K\|_{\rm Schur}\).
The product space is a compact marginal probability space, and the measurable factorization theorem applies to its product measure with exactly the integral-operator norm in the statement. [Aleksandrov–Peller, Theorem 4.2](../audits/literature/AP25/Yin_U001.md#measurable-schur-factorization)
Equivalently one can use bounds \(m+\varepsilon\) and let \(\varepsilon\downarrow0\).
Denote the two square-sum bounds in (4) by \(V,W\), respectively.
For any finite set of factors,
\[
 \sum_{j,\ell}\|\bar E(p_jw_\ell)\|_2^2
 \le c^2\Big\|\sum_\ell w_\ell^*\big(\sum_jp_j^*p_j\big)w_\ell\Big\|
 \le c^2 W^2\Big\|\sum_jp_j^*p_j\Big\|.
\]
The operator \((x_\ell)\mapsto\sum_\ell x_\ell v_\ell\) from a Hilbert direct sum to \(H\) has norm at most \(V\), by taking its adjoint and using traciality.
For the second term in (3), the same row bound gives \(\|\sum_\ell\bar E(w_\ell)v_\ell\|_2\le VcW\).
Multiplication on the left by the column \((p_j)\) costs at most \(\|\sum_jp_j^*p_j\|^{1/2}\).
Thus the slice with the partial symbol costs at most \(2cVW\).
The symbols converge pointwise product-almost everywhere and are uniformly bounded by \(VW\).
The inner spectral measures of coarse vectors are absolutely continuous with respect to the product law, so the bounded multipliers converge strongly on every \(\delta(p_j)\).
This proves the bound \(2mc\) without assuming absolute summability of separated sup norms.

### Passing to the original core of the relabelled tuple

A bounded Lipschitz function \(h_i\) on a conull spectral set extends to the support by continuity and to a surrounding rectangle with finite Lipschitz constant, by extending its real and imaginary parts separately.
Mollification followed by polynomial approximation in \(C^1\) gives polynomials converging uniformly to \(h_i\) on the spectrum with uniformly bounded Lipschitz constants.
This uses the [smooth marginal approximation](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests).
The original marginal divided differences then converge in \(L^2(\mu_i^2)\) by domination and diffuseness, and the same holds for the conjugate.
Consequently \(Y_i,Y_i^*\) have bounded strong-star graph approximants for \(\delta_i\).
For an omitted Borel marginal one can use uniformly bounded strong-star approximants with zero derivative.
On products the approximants converge strongly-star on bounded balls and in the original derivation graph by the Leibniz rule.
On \(P_Y\), \(I_K\bar\delta_i\) is the target derivation: its value on \(Y_i\) is one, on \(Y_i^*\) it is the target marginal phase, and on omitted letters it is zero.
The unique actual target derivation has these values. [Forced starred derivatives](Yin_C_F0076_v1.md#statement)

A separate approximation for each entry would not preserve the input column norm.
For a target column \(b\) with \(m\) entries and norm at most one, start with the bounded graph approximants just constructed, say \(b_\alpha\).
They converge strongly-star entrywise to \(b\), with convergent entrywise derivatives and adjoint derivatives.
Put \(H_\alpha=b_\alpha^*b_\alpha\), \(H=b^*b\); these scalar-algebra elements and their derivatives converge in the same senses.
Choose a real \(C^\infty\) function \(f\) equal to \(1\) on a neighborhood of \([0,1]\), such that \(\sqrt{t}|f(t)|\le1+\varepsilon\) for \(t\ge0\).
On a bounded interval containing the spectra of all \(H_\alpha,H\), approximate \(f\) and its derivative uniformly by real polynomials.
For any bounded selfadjoint graph input \(a\) above, the derivative formula for \(f(a)\) inserts the scalar divided difference \(f^{[1]}\) at **outer** left and right multiplication by \(a\) into \(\bar\delta_i a\).
For polynomials this is the finite product rule.
Uniform first-derivative approximation gives uniform convergence of the divided differences, hence the formula and graph convergence for \(f(a)\).
For \(a=H_\alpha\), the outer spectral actions of the approximating polynomial divided differences converge strongly as \(\alpha\) varies, by bounded strong-star convergence.
Uniform derivative approximation therefore gives \(\delta f(H_\alpha)\to0\) in the closed graph's derivative component, since \(f^{[1]}\) vanishes on \([0,1]^2\).
Using the polynomial approximants to \(f\) in the products \(b_\alpha f(H_\alpha)\) gives original-core columns converging to \(b\) in the entrywise graph with limsup column norm at most \(1+\varepsilon\).
Indeed \(\|b_\alpha f(H_\alpha)\|=\|\sqrt{H_\alpha}f(H_\alpha)\|\le1+\varepsilon\), and the supplementary polynomial errors can be taken arbitrarily small uniformly in \(\alpha\) by boundedness of \(b_\alpha,\delta H_\alpha\).
Apply the preceding Schur estimate, pass to this graph limit and let \(\varepsilon\downarrow0\).
For \(X^*,Y^*\), conjugation of the marginal variables and the kernel gives the same Schur norm.
This proves item 2.

### Arbitrary Lipschitz graphs over a real coordinate

First observe that actual scalar vacuum on a Lipschitz graph forces an \(L^3(ds)\) density \(\rho\) for its real parameter.
Indeed, in any interval partition of the parameter line with mesh \(\ell\), each corresponding spectral projection \(e_I\) has its graph carrier inside a disk of radius at most \(L\ell\), where \(L=\operatorname{Lip}(h)\).
Apply the [positive-weight scalar packing estimate](Yin_C_F0233_v1.md#statement), item 1, to these mutually orthogonal projections to obtain
\[
                      \sum_I \mu(I)^3/\ell^2\le C L^2\|\xi_{\rm marg}\|_2^2 ,
\]
where here \(\mu\) denotes the real parameter law.
The piecewise constant densities \(\mu(I)/\ell\) have precisely the sum on the left as their cubed Lebesgue \(L^3\) norms.
On dyadic refinements of a fixed interval containing the compact support, these histograms converge as measures against every continuous test by uniform continuity.
Their bounded \(L^3\) norms give a weak cluster point, identifying \(\rho\in L^3\).
The packing input only needs scalar ACSY for this application and applies also to the identity graph.

Conversely, for any compactly supported nonnegative probability density \(\rho\in L^3(ds)\) and real Lipschitz \(g\), the graph law has an actual scalar vacuum.
Extend \(g\) to the line and write \(h(s)=s+ig(s)\).
Let \(T_g\) be the Cauchy singular integral with kernel \(1/(h(s)-h(t))\) against \(dt\).
It acts boundedly on Lebesgue \(L^3\) and \(L^{3/2}\) with this parameter-line convention. [Cauchy integral on Lipschitz graphs](../audits/literature/Mus14/Yin_U001.md#cauchy-integral-on-a-lipschitz-graph)
For clarity one may use the skew transpose \((T_g-T_g^{\rm tr})/2\), where the transpose uses the bilinear Lebesgue pairing and the consistent extensions at the dual exponents.
This bounded operator, denoted \(T\), has the same off-diagonal kernel by antisymmetry, and satisfies \(\int vT u=-\int uT v\) for bounded compactly supported functions, extended by density to the dual exponents.

For a star polynomial \(p\), extend \(f(s)=p(h(s),\overline{h(s)})\) from an interval containing the support to a bounded compactly supported Lipschitz function on the line agreeing there.
In the pairing with \(\rho\) one has
\[
 \iint \frac{f(s)-f(t)}{h(s)-h(t)}\rho(s)\rho(t)\,ds\,dt
              =\int\rho [M_f,T]\rho\,ds=2\int f\rho\,T\rho\,ds .           \tag{5}
\]
Here is a verification using only the off-diagonal kernel and the \(L^p\) bounds.
Partition the compact parameter interval into finitely many intervals of length at most \(\ell\).
Between disjoint intervals the integral formula for the commutator follows first for test densities supported a positive distance apart and then by cutting off thin endpoint neighborhoods.
Operator pairings converge by the \(L^3,L^{3/2}\) bounds and absolute integrability of the difference kernel follows from \(|h(s)-h(t)|\ge|s-t|\).
On each same-interval pairing subtract a constant from \(f\) in the commutator.
The resulting absolute values sum to at most \(2\operatorname{Lip}(f)\ell\|T\|_{3\to3}\sum_I\|\rho1_I\|_3\|\rho1_I\|_{3/2}\), which tends to zero by discrete Hölder.
The same-interval contributions of the bounded difference kernel tend to zero by diffuseness.
This proves the first equality; skew transposition gives the second.
Hölder gives \(\int |T\rho|^2\rho\le\|T\rho\|_3^2\|\rho\|_3\).
Thus \(2\overline{T\rho}\) represents the vacuum with the tracial inner product linear in the second argument.
This proof requires neither a pointwise choice of tangent at every point nor a principal-value formula for the vacuum on general mixed words.

Because both the graph and the identity have this same \(L^3\) criterion, their scalar vacuum conditions are equivalent.
Their spectral gaps satisfy \(|s-t|\le |h_i(s)-h_i(t)|\le L_i|s-t|\).
In either direction the generator change preserves the liberation vacuum and the finiteness of its inverse-gap integral by item 1.
This establishes the first two assertions of item 3 for arbitrary correlations, with no multiplier condition.
For a distinguished selfadjoint coordinate of the actual tuple \(S\), the real-coordinate contraction estimate applies also after adjoining two free Haar generators, since the omitted starred letters are killed.
The [selfadjoint coordinate bound and column recovery](Yin_C_F0234_v1.md#statement) apply directly with the identity straight arc, yielding \(c_i(S)<\infty\) (equally in the adjoint orientation).
Item 2 then bounds the target columns in both orientations when the inverse secant is Schur.
The two bounds control the right and left original slices by the tracial flip and give the required closure and adjoint domains by [the two-slice theorem](Yin_C_F0072_v1.md#statement).
The algebraic commutator at a generator is bounded on the original core, so the identity extends to the graph closure and its restriction to all bounded vectors, with negative closure for generator-first order.

### Scope of the converse problem

Every finite correlated selfadjoint tuple with actual vacua and every real Lipschitz graph on its coordinates now yields an actual normal tuple, including graphs with arbitrarily many turns.
If the universal normal implication fails on this class, at least one inverse secant must fail the stated Schur bound.
For such kernels the failure itself gives no lower bound on the original column cost, as the correlated Gaussian example shows.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T10:52 |
| status | open |
| reason | Fix the Borel vacuum criterion, the mixed-core Schur estimate and the scalar and correlated Lipschitz graph result for whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Borel relabelling criterion, right-column transfer and actual vacuum invariance on arbitrary Lipschitz graphs. |
| argument | [Argument](#argument) | Common liberation graph, square-factor column bound, input column norm restoration and the scalar Cauchy integral. |
| dependency | [Inverse-gap criterion](Yin_C_F0238_v1.md#statement) | Actual liberation, scalar vacuum and off-diagonal recovery, including the norm and coarse measure class. |
| dependency | [Liberation adjoint](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Absolute continuity of the liberation vacuum spectral measure. |
| dependency | [Dense bounded approximants](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Kaplansky density on bounded balls, also in matrix algebras. |
| dependency | [Canonical contraction](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Theorem 3.4, closability of the original sliced operator. |
| dependency | [Measurable Schur factorization](../audits/literature/AP25/Yin_U001.md#ap25-u001) | Pointwise square-summable envelopes with product bounded by the measurable Schur norm. |
| dependency | [Scalar approximation](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) | Simultaneous first-derivative and uniform polynomial approximation of smooth planar functions. |
| dependency | [Forced normal phase](Yin_C_F0076_v1.md#statement) | Distinguished divided differences, omitted starred values and conjugate companions. |
| dependency | [Packing](Yin_C_F0233_v1.md#statement) | Item 1 for disjoint scalar projections in intervals on a Lipschitz graph. |
| dependency | [Lipschitz Cauchy operator](../audits/literature/Mus14/Yin_U001.md#mus14-u001) | The parameter-line Cauchy integral with its off-support kernel and Lebesgue bounds at the dual exponents. |
| dependency | [Straight-arc column](Yin_C_F0234_v1.md#statement) | Full mixed-starred-core column for a selfadjoint distinguished coordinate under actual ACSY. |
| dependency | [Canonical domains](Yin_C_F0072_v1.md#statement) | Part B, both actual bounded-vector domains from the two original sliced estimates. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T10:57 |
| status | proved |
| reason | Adopt the coordinate criterion, the Schur column transfer and the two-way Lipschitz graph ACSY result after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Borel relabelling criterion, right-column transfer and actual vacuum invariance on arbitrary Lipschitz graphs. |
| argument | [Argument](#argument) | Common liberation graph, square-factor column bound, input column norm restoration and the scalar Cauchy integral. |
| dependency | [Inverse-gap criterion](Yin_C_F0238_v1.md#statement) | Actual liberation, scalar vacuum and off-diagonal recovery, including the norm and coarse measure class. |
| dependency | [Liberation adjoint](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Absolute continuity of the liberation vacuum spectral measure. |
| dependency | [Dense bounded approximants](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Kaplansky density on bounded balls, also in matrix algebras. |
| dependency | [Canonical contraction](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Theorem 3.4, closability of the original sliced operator. |
| dependency | [Measurable Schur factorization](../audits/literature/AP25/Yin_U001.md#ap25-u001) | Pointwise square-summable envelopes with product bounded by the measurable Schur norm. |
| dependency | [Scalar approximation](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) | Simultaneous first-derivative and uniform polynomial approximation of smooth planar functions. |
| dependency | [Forced normal phase](Yin_C_F0076_v1.md#statement) | Distinguished divided differences, omitted starred values and conjugate companions. |
| dependency | [Packing](Yin_C_F0233_v1.md#statement) | Item 1 for disjoint scalar projections in intervals on a Lipschitz graph. |
| dependency | [Lipschitz Cauchy operator](../audits/literature/Mus14/Yin_U001.md#mus14-u001) | The parameter-line Cauchy integral with its off-support kernel and Lebesgue bounds at the dual exponents. |
| dependency | [Straight-arc column](Yin_C_F0234_v1.md#statement) | Full mixed-starred-core column for a selfadjoint distinguished coordinate under actual ACSY. |
| dependency | [Canonical domains](Yin_C_F0072_v1.md#statement) | Part B, both actual bounded-vector domains from the two original sliced estimates. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0253_v1.md#whole-proof-finding) | The full mixed cores, marginal and liberation tests, measurable Schur factorization, column norm restoration, scalar graph equivalence and both canonical domains under the multiplier hypothesis. |

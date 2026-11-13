---
author: Yin
---
# Canonical column costs of normal moment limits and conditional covariance constraints

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Fix \(d\ge1,\ R>0\), and finite \(L_i\ge0\) for \(1\le i\le d\).
Let \(\mathcal K\) be the joint star-moment laws of bounded normal generating tuples \(X=(X_1,\ldots,X_d)\) in finite von Neumann algebras \(M=W^*(X)\) with faithful normal probability trace \(\tau\), \(\|X_j\|\le R\), satisfying [actual ACSY](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) with \(\|\xi_i\|_2\le L_i\) for every coordinate.
Use the topology of pointwise convergence of star moments in the countable word basis.
Let \(E_i=(\mathrm{id}\otimes\tau)\delta_i\) be the canonical slice on the represented star-polynomial core, where \(\delta_i\) and its vacuum \(\xi_i\) are unique.
For each fixed formal star-polynomial column \(P=(p_a)_{a=1}^m\), let
\[
 H_{i,P}(\tau)=\left(\sum_a\|E_i p_a(X)\|_2^2\right)^{1/2},\qquad
 \|P\|_{\mathrm u,R}=\sup_{\max_j\|Y_j\|\le R}
                   \left\|\sum_a p_a(Y)^*p_a(Y)\right\|^{1/2},
\]
where the supremum is over all bounded operator tuples on arbitrary Hilbert spaces.
Write \(c_i(\tau)\) for the supremum of \(H_{i,P}(\tau)\) under the represented normalization \(\|\sum_a p_a(X)^*p_a(X)\|\le1\).

1. The class \(\mathcal K\) is compact metrizable and every \(H_{i,P}\) is continuous on it.
   The canonical column cost satisfies
   \[
             c_i(\tau)=\sup_{\|P\|_{\mathrm u,R}\le1}H_{i,P}(\tau).       \tag{1}
   \]
   The supremum can be taken over the countable collection with complex rational coefficients.
   In particular \(c_i\) is lower semicontinuous.
2. Let \(\tau_n\in\mathcal K\), fix \(i\), and let \(\omega\) be a free ultrafilter on the sequence with moment limit \(\tau_\omega\).
   Then \(c_i(\tau_\omega)=\infty\) exactly when for every positive integer \(l\) there is a fixed rational column \(P_l\) with \(\|P_l\|_{\mathrm u,R}\le1\) and \(\{n:H_{i,P_l}(\tau_n)>l+1\}\in\omega\).
   Some subsequential cluster law has infinite \(c_i\) exactly when there are such fixed columns \(P_l\) for which, for every \(m\), arbitrarily late terms satisfy all \(H_{i,P_l}(\tau_n)>l+1,\ 1\le l\le m\).
   In either case, adjoining two jointly free Haar unitaries free from the indicated limiting tuple gives a normal actual ACSY tuple with no bare full-domain dual system.
3. For any one normal actual ACSY law, fix \(i\) and put \(N=W^*(X_j:j\ne i)\), \(A=N\bar\otimes N^{\mathrm{op}}\) with product trace \(\tau_A\).
   For \(D=\sum_\ell b_\ell\otimes a_\ell^{\mathrm{op}}\in N\odot N^{\mathrm{op}}\) write \(D\cdot X_i=\sum_\ell b_\ell X_i a_\ell\).
   Then
   \[
             \tau_A(|D|)\le \|\xi_i\|_2\,\|D\cdot X_i\|_2.               \tag{2}
   \]
   In particular \(\|bX_i-X_i a\|_2\|\xi_i\|_2\ge4/\pi\) for unitaries \(a,b\in N\) whenever at least one is Haar.
   If \(N\) is diffuse, the distance of \(X_i\) from the closed linear span of vectors intertwining any pair of diffuse unitaries in \(N\) is at least \(1/\|\xi_i\|_2\).
   For pairwise orthogonal nonzero projections \(e_k\in N,\ b_k\in N,\ r_k>0\) satisfying \(\|(X_i-b_k)e_k\|_2\le r_k\sqrt{\tau(e_k)}\), one has
   \[
                      \sum_k\tau(e_k)/r_k^2\le\|\xi_i\|_2^2 .          \tag{3}
   \]
4. More generally, select any nonempty subfamily \(J\) and let \(N=W^*(X_j:j\notin J)\), taking \(\mathbb C1\) when the complement is empty.
   Write \(x_j=X_j-\mathbb E_N X_j,\ V=(\mathbb E_N(x_i^*x_j))_{i,j\in J}\) and \(W=(\mathbb E_N(\xi_i^*\xi_j))_{i,j\in J}\).
   The bounded conditional covariance \(V\) has full support and
   \[
       (V+\eta I)^{-1}\le W\quad(\eta>0),\qquad V^{-1}\le W,\qquad
       (\operatorname{Tr}_{|J|}\otimes\tau)(V^{-1})\le\sum_{i\in J}\|\xi_i\|_2^2 .       \tag{4}
   \]
   The inequality for the affiliated inverse is in form order and \(\operatorname{Tr}_{|J|}\) is unnormalized.
   The same assertions hold with Gram entries \(\mathbb E_N(x_i x_j^*)\) and \(\mathbb E_N(\xi_i\xi_j^*)\).

The limit criteria require simultaneous persistent tests on the specified compact class.
They supply no example of a law with infinite column cost.

## Argument

### Continuity of actual slice tests

The [compact moment-law theorem](Yin_C_F0201_v2.md#statement) gives compact metrizability at the cutoff, closure of the normal locus and lower semicontinuity of the joint witness costs \(\alpha_i\).
On the normal locus finiteness of every \(\alpha_i\) means actual ACSY, and the [forced normal phase](Yin_C_F0076_v1.md#statement) has coarse norm one at its own starred coordinate and zero at all the others.
Thus \(\mathcal K\) is exactly the intersection of the normal locus with the closed sublevels \(\alpha_i^2\le L_i^2+1\) for all \(i\).

To verify continuity, let \(\tau_n\to\tau\) in \(\mathcal K\), and write \(\mu_n,\mu\) for the distinguished normal marginal laws.
Their common support disk is compact, so star-moment convergence gives weak convergence of \(\mu_n^2\) to \(\mu^2\) on its square by polynomial density.
By [the forced normal phase theorem](Yin_C_F0076_v1.md#statement), \(\mu\) and every \(\mu_n\) are diffuse, \(\delta_i X_i^*=k_i\) with \(k_i(z,w)=(\bar z-\bar w)/(z-w)\), and all the other starred coordinate values vanish.
Set the scalar \(k_i\) equal to zero on the diagonal.
It is bounded and continuous off that \(\mu^2\)-null closed set.
For every \(\eta>0\) there exists a fixed star polynomial \(q(z,w,\bar z,\bar w)\) with \(\|k_i-q\|_{L^2(\mu^2)}<\eta\), by density.
The bounded function \(|k_i-q|^2\) is continuous \(\mu^2\)-almost everywhere, so \(\|k_i-q\|_{L^2(\mu_n^2)}\to\|k_i-q\|_{L^2(\mu^2)}\).
Replacing each starred phase by this fixed tensor polynomial in the outer word formula for \(\delta_i p_j\) produces a right slice which is a finite sum of word evaluations times ordinary star moments.
Its squared Hilbert norm is therefore a continuous function of finitely many moments.
The error in each actual slice has Hilbert norm at most \(C_{p_j,R}\|k_i-q\|_{L^2(\mu_n^2)}\), by the finite outer product rule, the common cutoff and contractivity of the right slice on the coarse Hilbert space.
The same bound holds at \(\tau\), and letting \(\eta\downarrow0\) proves the claimed continuity.

### Normalizing columns in every representation

For (1), the universal unit ball gives at most the represented cost.
For the reverse inequality, take a finite column \(P\) of represented norm at most one at the single target law and choose formal expressions for all its entries.
Write \(A=P^*P=\sum_jp_j^*p_j\) and \(L=\max(1,\|P\|_{\mathrm u,R}^2)\).
Fix \(\epsilon>0\) and choose a smooth positive scalar \(h\) on \([0,L]\) equal to one on a neighborhood of \([0,1]\) and satisfying \(\sqrt{s}\, h(s)\le 1+\epsilon\) throughout the interval \([0,L]\).
For example, interpolate by a smooth convex cutoff between \(1\) and \(s^{-1/2}\) before \(s=(1+\epsilon)^2\), keeping \(h=1\) below the transition.
Take polynomials \(q_l\to h\) uniformly together with their first derivatives by approximating \(h'\) and integrating.
Uniform functional calculus gives \(\|P q_l(A)\|_{\mathrm u,R}\le1+\epsilon+\sqrt L\,\|q_l-h\|_\infty\).
At the target law \(q_l(A)\to1\) in operator norm and \(\delta_i q_l(A)\to0\) in the coarse norm.
Indeed the latter equals the scalar divided difference of \(q_l\) at the commuting selfadjoint outer multipliers \(L_A,R_A\) applied to \(\delta_i A\).
Both spectra lie in \([0,1]\), so its norm is at most \(\|\delta_i A\|_2\sup_{[0,1]}|q_l'|\to0\).
The product rule now gives convergence of the slices of \(p_j q_l(A)\) to \(E_i p_j\).
Divide the new formal columns by \(1+\epsilon+\sqrt L\,\|q_l-h\|_\infty\), send \(l\to\infty\) and then \(\epsilon\downarrow0\) to prove (1).

The supremum in (1) can be taken over a countable collection, using complex rational coefficients and rational downward rescaling.
Indeed coefficient approximation on each fixed finite support is uniform in the universal column norm, and all corresponding slice errors are controlled by the word rule, the cutoff and \(\|k_i\|_2=1\).
In particular \(c_i\) is lower semicontinuous on \(\mathcal K\).

### Fixed tests along limits

For the specified ultrafilter limit, continuity gives \(H_{i,P}(\tau_\omega)=\lim_\omega H_{i,P}(\tau_n)\) for each fixed \(P\).
If the cost is infinite, for each \(l\) take a rational universal-unit column with value greater than \(l+2\) at that limit, so the set in item 2 belongs to \(\omega\).
Conversely each such set forces the limiting value to be at least \(l+1\), giving infinite cost by (1).

A sequence in \(\mathcal K\) has a cluster law with \(c_i=\infty\) exactly when there are fixed universal-unit columns \(P_l\) such that, for every \(m\), arbitrarily late terms satisfy \(H_{i,P_l}>l+1\) for all \(1\le l\le m\).
In the forward direction choose tests with \(H_{i,P_l}>l+2\) at the cluster law and use continuity.
Conversely, extract increasing indices meeting the first \(m\) tests and take a convergent subsequence.
At its limit the inequalities \(H_{i,P_l}\ge l+1\) hold for every fixed \(l\).
By [two-Haar enlargement](Yin_C_F0208_v1.md#statement) this would give a normal ACSY tuple without bare full-domain duals.

### Intertwining and small omitted-algebra corners

With the notation of item 3 set \(x=X_i-\mathbb E_NX_i\).
The [coarse summand of the cyclic bimodule](Yin_C_F0217_v1.md#statement) has projection \(P_{\rm c}\) reducing the outer \(N\)-actions, and its isometry to \(L^2(A)\) sends \(P_{\rm c}x\) to \(h^{1/2}\), where \(\|h^{-1/2}\|_{2,A}\le\|\xi_i\|_2\).
This projection kills \(L^2(N)\), hence sends \(D\cdot X_i\) to the same vector as \(D\cdot x\).
After the isometry that vector is \(D h^{1/2}\).
The identity \(D=(D h^{1/2})h^{-1/2}\) in \(L^1(A)\) follows by spectral truncation of the faithful affiliated \(h\).
Tracial Hölder and Hilbert projection now give (2).

In particular, for arbitrary unitaries \(a,b\in N\), applying (2) to \(D=b\otimes1-1\otimes a^{\rm op}\) and taking the product spectral law yields
\[
 \|bX_i-X_i a\|_2\,\|\xi_i\|_2
         \ge\iint_{\mathbb T^2}|z-w|\,d\mu_b(z)\,d\mu_a(w).
\]
The two laws enter independently on the right even when \(a,b\) are correlated inside \(N\).
If either unitary is Haar then the integral is \((2\pi)^{-1}\int_0^{2\pi}2|\sin(\theta/2)|\,d\theta=4/\pi\).
This excludes a sequence \(b_n X_{i,n}-X_{i,n}a_n\to0\) in \(L^2\) for any such choices under a uniform bound on the actual vacua.
If \(N\) is diffuse, every vector \(v\in L^2(M)\) intertwining two diffuse unitaries from \(N\) is killed by \(P_{\rm c}\), as in [the intertwining argument](Yin_C_F0217_v1.md#intertwining-vectors-and-normalizers).
Hence the distance of \(X_i\) to their entire closed linear span is at least \(\|h^{1/2}\|_{2,A}\ge\|\xi_i\|_2^{-1}\), by \(1\le\|h^{1/2}\|_{2,A}\|h^{-1/2}\|_{2,A}\).
This applies to the span of all unitary normalizers.

Similarly, for projections \(e,f\in N\), insert \(D=1\otimes e^{\rm op}-f\otimes1\).
Its absolute value is the sum of the two orthogonal projections \((1-f)\otimes e^{\rm op}\) and \(f\otimes(1-e)^{\rm op}\).
This gives
\[
 \|X_i e-f X_i\|_2\,\|\xi_i\|_2
    \ge (1-\tau(f))\tau(e)+\tau(f)(1-\tau(e)).
\]
For \(f=e\), approximately reducing projections in the omitted algebra whose traces stay away from zero and one therefore require growing vacuum norms.

For simultaneous small corners there is a stronger summable estimate.
For \(e_k,b_k,r_k\) satisfying the hypotheses of (3), \(D_k=1\otimes e_k^{\rm op}\) are orthogonal projections in \(A\), and in \(L^1(A)\)
\[
 \tau_A(D_k)
  =\tau_A\big((D_k h^{1/2})(h^{-1/2}D_k)\big)
  \le\|D_k h^{1/2}\|_{2,A}\,\|h^{-1/2}D_k\|_{2,A}.
\]
The first norm is the norm of the coarse projection of \(X_ie_k\), unchanged on replacing this vector by \((X_i-b_k)e_k\) because \(b_ke_k\in L^2(N)\).
Consequently \(\|h^{-1/2}D_k\|_{2,A}^2\ge\tau(e_k)/r_k^2\).
Their squared norms sum to at most \(\tau_A(h^{-1})\) by orthogonality of the right projections.
This proves (3), including countable families by finite partial sums.
In particular the [singular projection obstruction](Yin_C_F0211_v1.md#statement) cannot diverge using mutually orthogonal test projections that already belong to \(N\), even with merely an averaged \(L^2\) upper bound on each corner.
The spectral projections of \(|X_i-b_k|\) in the general obstruction can lie outside \(N\); (3) does not cover them.

### Conditional matrix covariance

Write \(m=|J|\).
The omitted-coordinate graph identity gives \(\bar\delta_i(x_j a)=\delta_{ij}1\otimes a\) and \(\bar\delta_i(a x_j)=\delta_{ij}a\otimes1\) for all \(a\in N\).
The omitted algebra is contained in the kernel and its left and right actions preserve the graph by [the closed-graph argument](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra), since \(N\) is contained in the algebra omitting \(i\).
Testing the actual adjoint against those products gives \(\mathbb E_N(\xi_i^*x_j)=\mathbb E_N(x_j\xi_i^*)=\delta_{ij}1\) using the \(L^1\) extension of conditional expectation and trace duality.
The matrix formed by pairing the concatenated row \((x_j)_{j\in J},(\xi_i)_{i\in J}\) with itself and applying the matrix-amplified conditional expectation is therefore
\[
                          \begin{pmatrix} V&I\\ I&W\end{pmatrix}\ge0 .
\]
Positivity in \(L^1(M_{2m}(N))\) follows by bounded Hilbert approximations to the \(\xi_i\), continuity of \(L^2\) products into \(L^1\), and positivity of the expectation.
Add \(\eta I\) to the upper-left block and compress by the bounded block column \(\big(-(V+\eta I)^{-1},I\big)^{\mathsf T}\).
This gives \(W-(V+\eta I)^{-1}\ge0\) in \(L^1\).
The traces then exclude any positive trace for the kernel of \(V\).
The monotone limit of these inverses is \(V^{-1}\) as positive forms, and the trace bound and form inequality follow.
For the left assertion use the concatenated row of \(x_j^*,\xi_i^*\) and the adjoints of the second conditional product identity.
For one coordinate this gives the bounds on both conditional variances with respect to its full omitted algebra.
Centering at any other \(b\in N\) adds a positive square to each variance, preserving its inverse bound by regularization.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T16:32 |
| status | open |
| reason | The continuous normalized tests, limit criteria and conditional restrictions on normal ACSY laws are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Moment-continuous canonical columns, common normalization and infinite-cost limits, trace-norm intertwining and conditional covariance. |
| argument | [Argument](#argument) | Phase approximation, smooth column truncation, compactness, coarse-module projection, corner summation and positive block compression. |
| dependency | [Compact law space and vacuum bounds](Yin_C_F0201_v2.md#statement) | Finite cutoff and number of coordinates, closed normal locus, lower semicontinuous joint witness costs and inheritance of actual ACSY. |
| dependency | [Actual normal starred values](Yin_C_F0076_v1.md#statement) | Item 1, diffuse marginals, unique phase tensor on the own starred generator, zero values on the other starred coordinates and closability. |
| dependency | [Canonical column cost and free enlargement](Yin_C_F0208_v1.md#statement) | Represented normalization and failure of bare full-domain duality for the two-free-Haar enlargement when an old column cost is infinite. |
| dependency | [Coarse cyclic summand](Yin_C_F0217_v1.md#statement) | Projection and bimodule isometry of (3), faithful density and vacuum-controlled inverse in (4), with the intertwining obstruction. |
| dependency | [Omitted-coordinate graph](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Closed derivation kills the other-coordinate von Neumann algebra and commutes with its outer bimodule actions. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T16:45 |
| status | proved |
| reason | Adopt the normal limit criteria and conditional covariance and intertwining bounds after independent whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Moment-continuous canonical columns, common normalization and infinite-cost limits, trace-norm intertwining and conditional covariance. |
| argument | [Argument](#argument) | Phase approximation, smooth column truncation, compactness, coarse-module projection, corner summation and positive block compression. |
| dependency | [Compact law space and vacuum bounds](Yin_C_F0201_v2.md#statement) | Finite cutoff and number of coordinates, closed normal locus, lower semicontinuous joint witness costs and inheritance of actual ACSY. |
| dependency | [Actual normal starred values](Yin_C_F0076_v1.md#statement) | Item 1, diffuse marginals, unique phase tensor on the own starred generator, zero values on the other starred coordinates and closability. |
| dependency | [Canonical column cost and free enlargement](Yin_C_F0208_v1.md#statement) | Represented normalization and failure of bare full-domain duality for the two-free-Haar enlargement when an old column cost is infinite. |
| dependency | [Coarse cyclic summand](Yin_C_F0217_v1.md#statement) | Projection and bimodule isometry of (3), faithful density and vacuum-controlled inverse in (4), with the intertwining obstruction. |
| dependency | [Omitted-coordinate graph](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Closed derivation kills the other-coordinate von Neumann algebra and commutes with its outer bimodule actions. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0236_v1.md#whole-proof-finding) | Continuity, common normalization, cluster and ultrafilter quantifiers, trace-norm gaps, localized columns and both matrix Gram bounds. |

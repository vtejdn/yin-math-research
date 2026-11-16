---
author: Yin
---

# Matching exceptional marginal points for affine shifts of a second normal coordinate

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(Z,Y\) be distinct coordinates of a bounded normal generating tuple in a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace and [actual starred conjugate variables](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Fix a nonempty compact set \(\mathcal L\subset\mathbb C^\times\times\mathbb C\) and set
\[
 F(s)=\sup_{(\lambda,c)\in\mathcal L}
               \tau(1_{[0,s]}(|Z-\lambda Y-c|)).
\]
For either compact marginal spectrum \(K\) and \(z\in K\), write \(e_K(z)\) for the smallest radius of a disk with center on the unit circle containing all limiting chord phases \((\bar v-\bar w)/(v-w)\) for distinct \(v,w\in K\) tending to \(z\).
This is the [local secant spread](Yin_C_F0273_v1.md#statement).
If \(\int_0^\infty F(s)^3ds/s^3=\infty\), there must exist \((\lambda_0,c_0)\in\mathcal L\) and a character of \(C^*(Z,Y)\) with values \(z_0,y_0\) such that
\[
 z_0=\lambda_0 y_0+c_0,\qquad
 \min\{e_{\sigma(Z)}(z_0),e_{\sigma(Y)}(y_0)\}
           \ge 2\big(\sqrt{1+24^{-2}}-1\big).                         \tag{A1}
\]
In particular if no two points of the respective large-spread sets satisfy this affine relation for any allowed parameter, the cubic integral of the entire family is finite.
This applies to arbitrary correlations even when both individual large-spread sets are nonempty.
When the matching condition excludes divergence, the original canonical dual at \(Z\) and its Hilbert adjoint are defined on the polar factors of these residuals, their adjoints and their products on either side by omitted contractions, with uniform strong cutoff convergence in both orientations.

## Argument

To check that both marginal restrictions hold on the same sequence, use the [scale selection](Yin_C_F0269_v1.md#simultaneous-choice-of-scales) with the [simultaneous dyadic tail conditions](Yin_C_F0273_v1.md#concentration-of-the-complex-measures-in-total-variation-away-from-the-point).
Its countable list of fixed Hilbert vectors may include the tensor adjoints of every pair of marginal monomials at \(Z\) for \(\delta_Z\) and also those at \(Y\) for \(\delta_Y\).
These vectors exist by the [actual Hilbert tensor adjoint formula](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability).
Choose parameters at the selected radii \(s_n\downarrow0\) attaining at least \(F(s_n)/2\) in singular mass, and pass to a subsequence on which they converge in \(\mathcal L\).
For \(T_n=Z-\lambda_nY-c_n=U_nP_n\), put \(h_n=s_n^2/(P_n^2+s_n^2)\), \(h_n'=U_nh_nU_n^*\), \(A_n=s_nP_n/(P_n^2+s_n^2)\), \(V_n=U_nA_n\), and \(H_n=\tau(h_n)\).
The selection gives \(\tau(A_n)/H_n\le24\) and \(s_n H_n^{-2}|\langle\eta,L_n\rangle|\to0\) for each listed vector and \(L_n=h_n,V_n\).
It bounds \(J(2^j s_n)\le C 2^{\beta j}F(s_n)\) for all \(j\ge0\), where \(2/3<\beta<1\) and \(J(s)=\int_1^\infty F(su)\,du/u^2\).

For \(Y\), the residual \(Y-(Z-c_n)/\lambda_n=-T_n/\lambda_n\) uses an omitted shift and radius \(s'_n=s_n/|\lambda_n|\).
Its two soft positive weights, radial weight and traced mass are exactly \(h_n,h_n',A_n,H_n\), and its complex test is \(-|\lambda_n|V_n/\lambda_n\).
The corresponding adjoint-test errors thus vanish on the same sequence since \(|\lambda_n|^{-1}\) is bounded.
The dyadic cuts \(1_{\{|T_n/\lambda_n|>2^js'_n\}}\) are exactly \(1_{\{P_n>2^js_n\}}\).
On the bands \(2^js_n<P_n\le2^{j+1}s_n\), \(A_n\le 2^{-j}\) and their traces are at most \(F(2^{j+1}s_n)\le J(2^{j+1}s_n)\).
As \(H_n\ge F(s_n)/4\), the normalized trace mass above \(2^ms_n\) is bounded by \(4C2^\beta\sum_{j\ge m}2^{-(1-\beta)j}\).
Consequently the upper tails of \(A_n/H_n\) in trace on these cuts, before and after polar conjugation, satisfy the same summable dyadic estimate for both marginals.

Apply the [two tensor identities and off-diagonal point-mass argument](Yin_C_F0269_v1.md#two-tensor-identities-off-the-collision-diagonal) to the two coordinate derivations with these tests.
Pass to one subsequence for weak convergence of both triples of measures obtained by tracing marginal functions against \(h_n/H_n,h'_n/H_n\) and the respective complex test divided by \(H_n\) on the two compact spectra.
In each marginal the left and right limits are equal point masses, and the normalized complex measures have uniformly bounded variation.
By the dyadic tail estimates their variations tend to zero outside any neighborhood of the corresponding point as in the [local cone proof](Yin_C_F0273_v1.md#the-two-scalar-trace-inequalities-in-a-local-cone).
The unit-tensor tests of that proof now apply at each marginal, with the same limiting upper bound \(24\) on the radial ratio, yielding (A1)'s two spread inequalities.

The hard right cut \(p_n=1_{[0,s_n]}(P_n)\) is also the hard right cut for the second residual at \(s'_n\).
Its trace-normalized state converges on each marginal to evaluation at the associated point, since \(p_n\le2 h_n\) and \(H_n/\tau(p_n)\le12\).
For the unit vectors \(v_n=p_n/\sqrt{\tau(p_n)}\) this gives \((Z-z_0)v_n\to0\) and \((Y-y_0)v_n\to0\) in trace Hilbert norm, with the same conclusions for both adjoints by normality.
As \(\|T_n v_n\|_2\le s_n\), the limit of the affine relation is \(z_0-\lambda_0y_0-c_0=0\).
Telescoping each fixed starred word from its rightmost letter gives convergence on \(v_n\) to the value of that word at the scalar pair times \(v_n\).
Polynomial evaluation at the pair is therefore contractive in the represented operator norm and extends to a character of \(C^*(Z,Y)\).
When the matching condition rules out divergence, the [polar-factor theorem](Yin_C_F0287_v1.md#statement) gives the two canonical domains and uniform strong cutoff convergence on the indicated polar factors with omitted contractions.
Affine shifts cover only the displayed subfamily of the cubic obstruction; arbitrary omitted shifts and the full mixed-domain question remain open.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T15:14 |
| status | open |
| reason | Fix the two simultaneous marginal tests, their affine compatibility and the resulting finite-integral criterion for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A joint character with two exceptional marginal secant sets at matching values for a compact family of nondegenerate affine shifts. |
| argument | [Argument](#argument) | Simultaneous adjoint tests, coincident radial weights, both point masses, the common hard spectral projection, and scalar evaluation of mixed words. |
| dependency | [Normal starred graph](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Marginal diffuseness, closability and adjoint domains at the marginal polynomial tensor tests for both coordinates. |
| dependency | [Two-resolvent concentration](Yin_C_F0269_v1.md#argument) | Normalization and scale selection for any countable list of fixed Hilbert vectors, both tensor identities, off-diagonal argument and hard cutoffs. |
| dependency | [Local secant estimates](Yin_C_F0273_v1.md#argument) | Simultaneous dyadic tails, localization of both legs in variation and the quantitative local cone lower bound. |
| dependency | [Polar-factor theorem](Yin_C_F0287_v1.md#statement) | Domain inclusion and uniform strong cutoff convergence for omitted multiples of the polar factors when the envelope has finite cubic integral. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T15:16 |
| status | proved |
| reason | Independent review verified the common scale selection, both marginal phase bounds at one character and the polar-factor consequences for the compact affine family. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A joint character with two exceptional marginal secant sets at matching values for a compact family of nondegenerate affine shifts. |
| argument | [Argument](#argument) | Simultaneous adjoint tests, coincident radial weights, both point masses, the common hard spectral projection, and scalar evaluation of mixed words. |
| dependency | [Normal starred graph](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Marginal diffuseness, closability and adjoint domains at the marginal polynomial tensor tests for both coordinates. |
| dependency | [Two-resolvent concentration](Yin_C_F0269_v1.md#argument) | Normalization and scale selection for any countable list of fixed Hilbert vectors, both tensor identities, off-diagonal argument and hard cutoffs. |
| dependency | [Local secant estimates](Yin_C_F0273_v1.md#argument) | Simultaneous dyadic tails, localization of both legs in variation and the quantitative local cone lower bound. |
| dependency | [Polar-factor theorem](Yin_C_F0287_v1.md#statement) | Domain inclusion and uniform strong cutoff convergence for omitted multiples of the polar factors when the envelope has finite cubic integral. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0304_v1.md#finding) | Complete fixed candidate and all four direct inputs. |

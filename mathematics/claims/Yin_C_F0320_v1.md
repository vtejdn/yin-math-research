---
author: Yin
---

# Uniform slice bounds for a normal coordinate coupled to any free unitary by a measurable phase

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(Z\) generate an abelian algebra with compact trace law \(\mu\) and actual scalar conjugate variable \(\xi_\mu\).
Let \(V\) be a unitary free from \(Z\) with diffuse law \(\nu\) and actual scalar divided-difference vacuum \(\xi_V\).
For a unit-modulus Borel function \(h=h(Z)\), set \(Y=h^*V\) and assume that \((Z,Y)\) has actual starred conjugate variables, as characterized by the [measurable phase criterion](Yin_C_F0265_v1.md#statement).
All algebras carry faithful normal probability traces.
There is an absolute constant \(C\) such that, at either coordinate and in either the original or adjoint orientation, the right slice on the represented starred polynomial core satisfies
\[
     \left(\sum_j\|(\mathrm{id}\otimes\tau)\delta_i p_j\|_2^2\right)^{1/2}
          \le C\|\xi_i\|_2
                  \left\|\sum_j p_j^*p_j\right\|^{1/2}                 \tag{1}
\]
for every finite column, where \(\xi_i\) denotes the actual vacuum of that oriented derivation.
The constant is independent of the essential supremum of the density of \(\nu\) and of its distance from Haar measure.

In particular, let \(X\) be Haar and free from a unitary \(V\), and let \(F\) be any bounded Borel map on the circle with measurable inverse on a Haar-conull set.
If the pair \(F(X),F(X^*V)\) has full actual starred conjugate variables, its [normalized full-core cost](Yin_C_F0315_v1.md#statement) satisfies \(k\le C\).
This covers all product laws compatible with actuality, including those with unbounded densities and arbitrarily small nonzero angular vacuum.
Finiteness for all exchange-symmetric normal pairs is still open.

## Argument

### The angular derivative and the cubic density defect

Write \(m\) for Haar probability on the circle and \(H=\xi_V V^*-1\).
The [rotated coordinate calculation](Yin_C_F0265_v1.md#the-rotated-unitary-coordinate) and its [vacuum computation](Yin_C_F0265_v1.md#the-base-coordinate-vacuum-and-its-inverse-gap-energy) use the Laurent derivation \(\mathcal L V=1\otimes V\).
Its scalar right slice is
\[
    Df(z)=\int\frac{f(z)-f(w)}{z-w}\,w\,d\nu(w),\qquad
    \int Df\,d\nu=\langle H,f\rangle_\nu.                              \tag{2}
\]
Indeed applying the divided difference to \(v f(v)\) and subtracting \(f\) gives (2), including the vacuum by adjunction.

The scalar vacuum gives \(\int(M_1\nu)^2\,d\nu<\infty\) by the [maximal density criterion](Yin_C_F0255_v1.md#statement).
On each set where \(M_1\nu\le N\), the restricted measure of every arc \(I\) meeting the set is at most \(C N m(I)\), by taking a ball of radius \(C m(I)\) about a point in the intersection.
The union of these sets carries the measure, so \(\nu=\rho\,dm\), and differentiation on arcs gives \(\rho\le C M_1\nu\) almost everywhere for \(\nu\).
Thus \(\rho\in L^3(m)\).
The [unitary Fisher information identity](../audits/literature/Voi99/Yin_U004.md#unitary-derivation-and-fisher-information) gives
\[
       \Delta:=\int(\rho-1)^2(\rho+2)\,dm=\int\rho^3\,dm-1=3\|H\|_2^2 .
                                                                        \tag{3}
\]

Let \(P_-,P_+\) project onto the strictly negative and strictly positive Fourier modes.
We use the \(L^2(m)\) contraction and the classical \(L^3(m)\) boundedness of \(P_-\) from the circle Hilbert transform in the same source.
For bounded \(f\) the following expression defines a vector in \(L^2(\nu)\), and on Laurent polynomials it equals \(Df\):
\[
        fP_-\rho-P_-(f\rho)
             =\tfrac12 f(\rho-1+H^*)-P_-(f\rho).                       \tag{4}
\]
For the first equality with (2), damp the negative modes by \(r^{|j|}\), \(r<1\).
The corresponding integral kernel is \(rw/(z-rw)\).
The projections converge in \(L^3(m)\) by Poisson approximation, hence in \(L^2(\nu)\) by Hölder.
The factor \(f(z)-f(w)\) for a Laurent polynomial cancels the diagonal singularity uniformly for \(r\ge1/2\), giving (2) in the limit.
Integrating this formula against \(\rho\,dm\), transposition for the bilinear Fourier pairing moves \(P_-\) to \(P_+\).
The pairing is valid by \(L^2(m)\) approximation since \(\rho\) and \(f\rho\) are square integrable.
Equation (2) then yields \(H^*=P_-\rho-P_+\rho\) in \(L^2(\nu)\), by polynomial density and Hölder.
Together with \(P_-\rho+P_+\rho=\rho-1\) this gives (4).

### A Hilbert-space bounded part and an error controlled by the vacuum

Take the disjoint maximal dyadic arcs \(I\) for which the \(m\)-average of \(\rho\) exceeds 2.
The whole circle has average one, so the parent of each selected arc has average at most 2 and \(2<\operatorname{avg}_I\rho\le4\).
Write \(D_0=\bigcup I\) and \(G=\mathbb T\setminus D_0\), so \(\rho\le2\) almost everywhere on \(G\) by dyadic differentiation.
Jensen on each arc gives \(m(D_0)\le\Delta/2\).
Integrating \(\rho^3=(\rho-1)^2(\rho+2)+3\rho-2\) on \(D_0\) gives \(\int_{D_0}\rho^3\,dm\le\Delta+10m(D_0)\le6\Delta\).
Also \(\int_{D_0}\rho^2\,dm\le m(D_0)^{1/3}(\int_{D_0}\rho^3\,dm)^{2/3}\le C\Delta\).

For \(f\in L^2(\nu)\) put \(A_f=P_-(1_G\rho f)\).
Define a linear map \(T\) by retaining \(A_f\) on \(G\) and replacing it on each selected \(I\) by \(\operatorname{avg}_I A_f\), with averages taken against \(m\).
The input multiplied by \(\rho\) is independent of the representative on zero-density sets.
Jensen, \(\operatorname{avg}_I\rho\le4\) and \(\rho\le2\) on \(G\) give
\[
      \|Tf\|_{2,\nu}^2\le4\|A_f\|_{2,m}^2\le8\|f\|_{2,\nu}^2.          \tag{5}
\]
We claim that the remaining scalar operator satisfies
\[
             \|Df+Tf\|_{2,\nu}\le C\sqrt{\Delta}\,\|f\|_\infty
                                                                        \tag{6}
\]
for all bounded \(f\), using the representative-independent extension (4).

It suffices to test \(\|f\|_\infty\le1\).
The multiplication terms in (4) cost at most \((\sqrt\Delta+\|H\|_2)/2\) by (3).
For \(a=1_{D_0}\rho f\), split the output on \(G,D_0\) and apply Hölder to obtain
\[
 \int |P_-a|^2\rho\,dm
 \le 2\|a\|_{2,m}^2+
        \|P_-a\|_{3,m}^2\left(\int_{D_0}\rho^3\,dm\right)^{1/3}
 \le C\Delta .
\]
The remaining difference \(A_f-Tf\) is supported on \(D_0\).
For any bounded \(\alpha\) and arc \(I\), the circle projection satisfies
\[
   \int_I|P_-\alpha-\operatorname{avg}_I P_-\alpha|^3\,dm
                       \le C m(I)\|\alpha\|_\infty^3.                   \tag{7}
\]
For the part of \(\alpha\) in the concentric triple arc this follows by \(L^3\) boundedness and Jensen.
If the triple arc contains the circle, this handles the entire function.
For the complementary part, the oscillation of the integral across \(I\) is at most \(C\|\alpha\|_\infty\): the derivative of the circle projection kernel away from its pole is bounded by \(C/\operatorname{dist}(\cdot,0)^2\), and integrating from distance \(m(I)\) outwards compensates the length of \(I\).
The kernel bound follows directly from \(w/(z-w)\) at disjoint arguments, using angular distance.
This proves (7).
Apply it with \(\alpha=1_G\rho f\), whose essential supremum is at most 2.
Hölder on \(D_0\) now gives
\[
 \int_{D_0}|A_f-Tf|^2\rho\,dm
 \le \left(\sum_I\int_I|A_f-\operatorname{avg}_I A_f|^3\,dm\right)^{2/3}
           \left(\int_{D_0}\rho^3\,dm\right)^{1/3}
 \le C\Delta .
\]
This proves (6).
A large constant part of \(P_-\alpha\) on a small arc is included in the Hilbert-space bounded map (5).

### The full mixed core

Set \(J=\iint |h(z)-h(w)|^2/|z-w|^2\,d\mu^2\) off the null diagonal.
For non-Haar \(\nu\) the [phase criterion](Yin_C_F0265_v1.md#statement) gives \(J<\infty\) and
\[
                \|\xi_1\|_2^2=\|\xi_\mu\|_2^2+\|H\|_2^2J
\]
at the base coordinate.
Use the original free-product core of bounded base letters and Laurent polynomials in \(V\).
Let \(P^\circ f=f-\int f\,d\nu\).
On centered terminal noise polynomials, split the centered output of (2) as \(R_1+R_2\), where
\[
           R_1=-P^\circ T P^\circ,\qquad
           R_2=P^\circ(D+T)P^\circ .
\]
Both maps kill constants.
By (5), \(R_1\) has Hilbert norm at most \(\sqrt8\).
By (3) and (6), \(R_2\) has operator-norm-to-Hilbert norm at most \(C\|H\|_2\), including the centering on its input.
The scalar output in (2) has vacuum \(H\).
These are maps on the scalar terminal coefficient in the original derivative expansion.
No change of spectral variables is involved.

For clarity, the two estimates control different factors in that expansion.
Put \(d=z-w\), \(m_\epsilon=|d|^2/(|d|^2+\epsilon^2)\) and \(k_\epsilon=m_\epsilon(h(z)\overline{h(w)}-1)/d\), set to zero on the diagonal.
Then \(\|k_\epsilon\|_2\le\sqrt J\).
On a reduced word ending in a centered noise letter \(b\) and a bounded base letter \(a\), the weighted terminal derivative contributes the unchanged prefix times \(Db\) times \(O_{k_\epsilon}a\), with \(O_k a(z)=\int k(z,w)a(w)d\mu(w)\).
The [terminal factor estimates](Yin_C_F0316_v1.md#estimating-all-mixed-words) bound the scalar and \(R_2\) contributions on unit columns by \(2\|H\|_2\|k_\epsilon\|_2\) and \(2\sqrt{4/\pi}\|R_2\|_{\infty\to2}\|k_\epsilon\|_2\), respectively.
Their derivation uses the free right-module decomposition, the commutative finite-family inequality and (2) for the scalar part.
The \(R_1\) contribution uses its Hilbert norm on the terminal noise leg and the column bound \(6(2+\sqrt2)\|\xi_\mu\|_2\) for \(O_{k_\epsilon}\) on the last base leg.
Indeed the [scalar bridge formula](Yin_C_F0316_v1.md#the-marginal-kernel-on-a-terminal-base-factor) gives \(O_{k_\epsilon}a=E_{\mu,\epsilon}a-hE_{\mu,\epsilon}(\bar h a)\).
The conditional expectation of the input squared column onto the base controls all last-base coefficients in an orthonormal reduced-prefix and terminal-noise expansion.
These terminal estimates use only the two displayed map norms and the scalar vacuum, so they apply with (5)–(6) for arbitrary \(\rho\in L^3(m)\).

By the [original cutoff identity](Yin_C_F0265_v1.md#removing-the-cutoff-on-the-target-polynomial-core) the remaining free-reference term costs at most \(36\|\xi_\mu\|_2\) uniformly in \(\epsilon\).
On each fixed finite target column \(m_\epsilon\) tends to one strongly as an inner multiplier, since the base trace law is diffuse and the diagonal has zero coarse projection.
Thus the original base column cost is bounded by \(C(\|\xi_\mu\|_2+\|H\|_2\sqrt J)\le C'\|\xi_1\|_2\).
At Haar law \(h^*V\) is Haar and free from the base, and the same cutoff reference result gives the scalar-vacuum column bound directly, including when \(J\) is infinite.
At the other coordinate the [rotated unitary slice](Yin_C_F0265_v1.md#the-rotated-unitary-coordinate) has column cost at most \(\sqrt{4/\pi}\,a_V\) and vacuum \(h^*\xi_V\), where \(a_V\le(2+\sqrt2)\|\xi_V\|_2\) by the [scalar weight estimate](Yin_C_F0267_v1.md#statement).
Conjugating the adjoint pair by \(h\) uses \(V^*\), with reflected density and unchanged norms, as in the [orientation calculation](Yin_C_F0265_v1.md#adjoints-and-the-strong-duals).
This proves (1).

For the common reparametrization \(F\), the [product-law reduction](Yin_C_F0315_v1.md#strong-duals-on-the-full-represented-core) provides the scalar vacuum of \(V\), the base model with \(h(F(X))=X\), and the transfer to the original core by bounded strong-star approximation of the omitted marginal.
Exchange supplies the same normalized bound at \(F(X^*V)\).
Thus (1) gives the asserted uniform bound on \(k\).

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:22 |
| status | open |
| reason | Fix a universal bound for actual measurable-phase free-unitary models by decomposing the original scalar angular slice on dyadic arcs. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Universal full mixed column and orientation bounds for the measurable phase model, and all compatible product laws in common generating reparametrizations. |
| argument | [Argument](#argument) | Cubic density defect, Fourier representation, averaging the good-input projection on bad arcs, and the free-product terminal decomposition. |
| dependency | [Scalar geometric condition](Yin_C_F0255_v1.md#statement) | Actual scalar vacuum gives square integrability of the maximal linear density and hence an \(L^3\) density on the circle. |
| dependency | [Unitary Fisher information](../audits/literature/Voi99/Yin_U004.md#voi99-u004) | The normalized circle cubic identity and the \(L^3\) estimate for the circle Hilbert transform. |
| dependency | [Phase criterion](Yin_C_F0265_v1.md#statement) | Exact base vacuum norm and phase energy for non-Haar product laws. |
| dependency | [Rotated coordinate](Yin_C_F0265_v1.md#the-rotated-unitary-coordinate) | Scalar slice cost lifted to the rotated unitary coordinate and its true vacuum. |
| dependency | [Terminal angular vacuum](Yin_C_F0265_v1.md#the-base-coordinate-vacuum-and-its-inverse-gap-energy) | Angular derivation, its free extension and the centered scalar vacuum. |
| dependency | [Original cutoff](Yin_C_F0265_v1.md#removing-the-cutoff-on-the-target-polynomial-core) | Free term, actual cutoff removal and Haar absorption. |
| dependency | [Adjoint orientation](Yin_C_F0265_v1.md#adjoints-and-the-strong-duals) | Adjoint model conjugation and preservation of both phase energy and vacuum norms. |
| dependency | [Terminal estimates](Yin_C_F0316_v1.md#estimating-all-mixed-words) | Separate estimates for the centered Hilbert-bounded term, the centered operator-norm-bounded term and the scalar output on full mixed columns. |
| dependency | [Marginal bridge](Yin_C_F0316_v1.md#the-marginal-kernel-on-a-terminal-base-factor) | Column control of the terminal-base integral operator by the scalar vacuum, uniformly in the cutoff. |
| dependency | [Scalar weight](Yin_C_F0267_v1.md#statement) | Uniform operator-norm-to-Hilbert bound for the ordinary scalar unitary slice. |
| dependency | [Product-law transfer](Yin_C_F0315_v1.md#strong-duals-on-the-full-represented-core) | Actual scalar product vacuum, measurable inverse, full-core transfer and exchange for the reparametrized pair. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:31 |
| status | proved |
| reason | Adopt the absolute column estimate for all compatible measurable phase models after independent review of the full scalar decomposition and transfer. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Universal full mixed column and orientation bounds for the measurable phase model, and all compatible product laws in common generating reparametrizations. |
| argument | [Argument](#argument) | Cubic density defect, Fourier representation, averaging the good-input projection on bad arcs, and the free-product terminal decomposition. |
| dependency | [Scalar geometric condition](Yin_C_F0255_v1.md#statement) | Actual scalar vacuum gives square integrability of the maximal linear density and hence an \(L^3\) density on the circle. |
| dependency | [Unitary Fisher information](../audits/literature/Voi99/Yin_U004.md#voi99-u004) | The normalized circle cubic identity and the \(L^3\) estimate for the circle Hilbert transform. |
| dependency | [Phase criterion](Yin_C_F0265_v1.md#statement) | Exact base vacuum norm and phase energy for non-Haar product laws. |
| dependency | [Rotated coordinate](Yin_C_F0265_v1.md#the-rotated-unitary-coordinate) | Scalar slice cost lifted to the rotated unitary coordinate and its true vacuum. |
| dependency | [Terminal angular vacuum](Yin_C_F0265_v1.md#the-base-coordinate-vacuum-and-its-inverse-gap-energy) | Angular derivation, its free extension and the centered scalar vacuum. |
| dependency | [Original cutoff](Yin_C_F0265_v1.md#removing-the-cutoff-on-the-target-polynomial-core) | Free term, actual cutoff removal and Haar absorption. |
| dependency | [Adjoint orientation](Yin_C_F0265_v1.md#adjoints-and-the-strong-duals) | Adjoint model conjugation and preservation of both phase energy and vacuum norms. |
| dependency | [Terminal estimates](Yin_C_F0316_v1.md#estimating-all-mixed-words) | Separate estimates for the centered Hilbert-bounded term, the centered operator-norm-bounded term and the scalar output on full mixed columns. |
| dependency | [Marginal bridge](Yin_C_F0316_v1.md#the-marginal-kernel-on-a-terminal-base-factor) | Column control of the terminal-base integral operator by the scalar vacuum, uniformly in the cutoff. |
| dependency | [Scalar weight](Yin_C_F0267_v1.md#statement) | Uniform operator-norm-to-Hilbert bound for the ordinary scalar unitary slice. |
| dependency | [Product-law transfer](Yin_C_F0315_v1.md#strong-duals-on-the-full-represented-core) | Actual scalar product vacuum, measurable inverse, full-core transfer and exchange for the reparametrized pair. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0328_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

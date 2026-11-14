---
author: Yin
---

# Omitted shifts that preserve normality of a coordinate

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(Z=X_i\) be a coordinate of a bounded normal generating tuple \(X\) with actual starred conjugate variables in a finite von Neumann algebra with faithful normal probability trace \(\tau\).
Write \(N=W^*(X_j:j\ne i)\), \(B=W^*(Z)\), and \(\xi=\delta_i^*(1\otimes1)\).
For \(b\in N\) put \(G(b)=[Z-b,(Z-b)^*]\).
The following alternatives characterize the bounded sequences \(b_n\in N\), with \(\sup_n\|b_n\|<\infty\), for which \(\|G(b_n)\|_2\to0\).

1. If the spectral law of \(Z\) is not carried by a straight line, then \(\|G(b_n)\|_2\to0\) if and only if \(\|b_n-\tau(b_n)1\|_2\to0\).
2. If the spectral law lies on \(z_0+\omega\mathbb R\), with \(|\omega|=1\), then \(\|G(b_n)\|_2\to0\) if and only if \(\|\operatorname{Im}(\bar\omega(b_n-\tau(b_n)1))\|_2\to0\), where \(\operatorname{Im}d=(d-d^*)/(2i)\).

In particular, a shift \(Z-b\) is normal precisely for scalar \(b\) in case 1, and precisely for \(b=\lambda1+\omega d\), \(\lambda\in\mathbb C\), \(d=d^*\in N\), in case 2.
Define
\[
       F_{\rm nor}(r)=
       \sup_{\substack{b\in N\\G(b)=0}}\tau(1_{[0,r]}(|Z-b|)).
\]
Then
\[
       \int_0^\infty F_{\rm nor}(r)^3\,\frac{dr}{r^3}
                  \le 24(2+\sqrt2)^2\|\xi\|_2^2 .
                                                                    \tag{1}
\]
In case 2 the same estimate holds with \(96\|\xi\|_2^2\) on the right and with the supremum over all \(b\in N\).
Consequently no exactly normal residual, even from a different shift at each radius, realizes a divergent cubic concentration integral in an actual tuple.

## Argument

### The derivative of the normality defect

Write \(\mathcal B=M\bar\otimes M^{\rm op}\) with product trace, and identify the coarse Hilbert space with \(L^2(\mathcal B)\) by sending \(u\otimes v\) to \(u\otimes v^{\rm op}\).
For \(c\in M\) put \(A_c=c\otimes1-1\otimes c^{\rm op}\).
The [actual starred normal derivative](Yin_C_F0076_v1.md#statement) has \(\delta Z=1\otimes1\) and \(\delta Z^*=k\), where \(k(z,w)=(\bar z-\bar w)/(z-w)\) in the two marginal spectral variables.
The law \(\nu\) of \(Z\) is diffuse, so \(k\) is a symmetric unitary symbol in \(B\bar\otimes B^{\rm op}\).
In this identification \(A_Z k=A_Z^*\).
By the [omitted-algebra graph identity](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra), the closed derivative respects left and right multiplication by arbitrary elements of \(N\).
Expansion of the commutator using \([Z,Z^*]=0\) therefore gives
\[
        G(b)\in\operatorname{Dom}\bar\delta,\qquad
        \bar\delta G(b)=A_b^*-A_b k .
                                                                  \tag{2}
\]
Indeed the product rule for \(T=Z-b\) would give \(A_Tk-A_T^*\), and every mixed product needed to expand this expression has one omitted factor.
Here and below \(\bar\delta\) denotes its value in the identified coarse space.

Suppose \(\|G(b_n)\|_2\to0\) and \(\|b_n\|\le K_0\).
Then
\[
                  \|A_{b_n}^*-A_{b_n}k\|_{2,\mathcal B}\longrightarrow0.
                                                                  \tag{3}
\]
To justify the varying tests in this conclusion, choose any fixed finite sum \(k'\) of tensors of marginal starred polynomials.
Every such tensor belongs to \(\operatorname{Dom}\delta^*\) by the [actual vacuum adjoint formula](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001), as does \(1\otimes1\).
For \(b\in N\), the outer left and right multipliers preserve \(\operatorname{Dom}\delta^*\), and \(\delta^*\) of a multiplied test is the correspondingly multiplied vector \(\delta^*\) of the test.
This follows by moving the multiplier across the Hilbert pairing and using graph invariance under both it and its adjoint.
Left multiplication by \(A_b\) in \(\mathcal B\) is the difference of exactly these two outer multipliers.
Consequently \(u_n'=A_{b_n}^*-A_{b_n}k'\) satisfies \(\|\delta^*u_n'\|_2\le 2K_0(\|\xi\|_2+\|\delta^*k'\|_2)\).
For \(u_n=A_{b_n}^*-A_{b_n}k\), (2) implies \(\langle u_n',u_n\rangle\to0\).
Moreover \(\|u_n\|_2\le4K_0\) and \(\|u_n-u_n'\|_2\le2K_0\|k-k'\|_2\).
Approximating \(k\) in \(L^2(\nu^2)\) by such polynomial tensors proves (3).

The operators in (3) are bounded uniformly in operator norm, and \(k\) is unitary.
Multiplying by adjoints now gives \(\|A_{b_n}A_{b_n}^*-A_{b_n}^*A_{b_n}\|_{2,\mathcal B}\to0\).
The difference on the left is \(A_{[b_n,b_n^*]}\) by opposite multiplication.
For any \(c\in M\), \(\|A_c\|_{2,\mathcal B}^2=2\|c-\tau(c)1\|_2^2\).
A commutator has trace zero, so
\[
                           \|[b_n,b_n^*]\|_2\to0 .                      \tag{4}
\]

### Slicing the phase in the noncollinear case

Identify \(B\) with \(L^\infty(\nu)\).
If \(k\) is constant, its secant equation places almost every \(z\) on the straight line through a fixed typical \(w\) with that secant direction, by Fubini.
Thus case 1 implies \(k\) is nonconstant.
There exists a bounded centered \(h\in B\) such that
\[
                    a(z)=\int h(w)k(z,w)\,d\nu(w)
\]
is nonzero in \(B\).
Otherwise product-function tests with arbitrary first factor and centered second factor show \(k\) depends only on its first variable.
Symmetry then makes it constant.

Let \(\phi_h(c^{\rm op})=\tau(hc)\).
The slice \(\mathrm{id}\otimes\phi_h\) is continuous from \(L^2(\mathcal B)\) to \(L^2(M)\).
It sends \(A_{b_n}^*\) to a scalar since \(\tau(h)=0\), and sends \((b_n\otimes1)k\) to \(b_n a\).
The slice of \((1\otimes b_n^{\rm op})k\) is in \(B\) because the first leg of \(k\) lies in \(B\).
Its operator norm is at most \(K_0\|h\|_1\).
Hence (3) gives a uniformly bounded sequence \(v_n\in B\) with \(\|b_n a-v_n\|_2\to0\).
Choose \(\varepsilon>0\) so that \(p=1_{[\varepsilon,\infty)}(|a|)\) has positive trace.
Multiplication on the right by the bounded inverse of \(a\) on \(p\), extended by zero off \(p\), shows that \(b_n p\) is within \(o(1)\) in \(L^2\) of uniformly bounded elements of \(Bp\).

If \(p=1\), this implies \(\|[b_n,Z]\|_2\to0\).
If \(p\ne1\), it implies \(\|(1-p)b_n p\|_2\to0\).
Since
\[
     \tau(p[b_n,b_n^*])=\|p b_n(1-p)\|_2^2-\|(1-p)b_n p\|_2^2,
\]
(4) also gives \(\|p b_n(1-p)\|_2\to0\), and hence \(\|[b_n,p]\|_2\to0\).
In each case \(b_n\) asymptotically commutes with a fixed nonscalar element of \(B\).
The [omitted-algebra commutation theorem](Yin_C_F0226_v1.md#statement) gives \(\|b_n-\tau(b_n)1\|_2\to0\).
Conversely this convergence gives \(\|G(b_n)\|_2\to0\), since subtracting \(\tau(b_n)1\) does not affect the commutator and multiplication by bounded factors is continuous in \(L^2\) on bounded balls.

### The affine-line case and the concentration bound

In case 2 one has \(k=\bar\omega^2\) almost everywhere, so (3) is exactly \(\|A_{b_n^*-\bar\omega^2b_n}\|_2\to0\).
The formula after (3) identifies this with convergence of the centered imaginary part in the statement.
Conversely, \(\tau(b_n)1+\omega\operatorname{Re}(\bar\omega(b_n-\tau(b_n)1))\) is uniformly bounded and differs from \(b_n\) by \(o(1)\) in \(L^2\).
Subtracting this approximant from \(Z\) gives a scalar plus \(\omega\) times a selfadjoint element.
Bounded multiplication then gives \(\|G(b_n)\|_2\to0\).
Constant sequences give both exact characterizations.

In case 1 the supremum in \(F_{\rm nor}\) runs over scalar centers.
Apply the [cubic concentration theorem](Yin_C_F0258_v1.md#statement) in \(B\) to \(Z\) alone, whose actual scalar vacuum is \(\mathbb E_B\xi\) by restriction to marginal polynomials.
The [planar scalar weight theorem](Yin_C_F0267_v1.md#statement) gives a common dominating density of mass \(\|\mathbb E_B\xi\|_2^2\) and constant \(2+\sqrt2\) before normalizing that density.
Summing its bound on a finite column and using the trace against the positive density bounds the scalar column cost by \((2+\sqrt2)\|\xi\|_2\).
This gives (1).

In case 2 relabel the distinguished coordinate as \(x=\bar\omega(Z-z_0)\) and leave all omitted coordinates fixed.
The original starred algebra is unchanged, and \(\omega\delta_i\) is the relabelled actual derivative there with vacuum \(\bar\omega\xi\); the other actual derivatives already kill \(Z,Z^*\).
The [selfadjoint-coordinate weight](Yin_C_F0266_v1.md#statement) has an unnormalized dominating density \(2(w+(\bar\omega\xi)^2)\) of mass \(4\|\xi\|_2^2\).
Thus the column cost at \(x\) is at most \(2\|\xi\|_2\).
Every shifted modulus \(|Z-b|\) equals \(|x-\bar\omega(b-z_0)|\), and the transformed shift ranges over \(N\).
The cubic theorem for the relabelled tuple gives the asserted estimate over all omitted shifts.
The stability theorem supplies no rate comparing a general nonnormal residual with the radius in its small-singular-value test.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T13:35 |
| status | open |
| reason | Fix the exact and asymptotic normality alternatives for omitted additive shifts, their phase-slice proof and their uniform concentration consequence. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Bounded sequences with vanishing residual normality defect, exact classification and uniform cubic concentration for all exactly normal residuals. |
| argument | [Argument](#argument) | Graph pairing with omitted multipliers, phase-slice detection, asymptotic corner commutation, affine reduction and the scalar and selfadjoint cost bounds. |
| dependency | [Normal starred phase](Yin_C_F0076_v1.md#statement) | Unit secant symbol and its restriction to the scalar coordinate. |
| dependency | [Omitted-algebra graph invariance](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Left and right omitted multipliers preserve the graph, including for arbitrary bounded omitted elements. |
| dependency | [Vacuum tensor adjoint domain](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Finite sums of core polynomial tensors in the actual adjoint domain. |
| dependency | [Omitted-algebra commutation rigidity](Yin_C_F0226_v1.md#statement) | Variance collapse for a bounded omitted sequence asymptotically commuting with one fixed nonscalar marginal test. |
| dependency | [Cubic concentration](Yin_C_F0258_v1.md#statement) | Uniform integral for all omitted shifts from the original distinguished finite column cost. |
| dependency | [Planar scalar weight](Yin_C_F0267_v1.md#statement) | Single marginal density, total mass and universal constant controlling its right slice. |
| dependency | [Real-coordinate weight](Yin_C_F0266_v1.md#statement) | Joint finite-column bound and mass of the unnormalized dominating density at a selfadjoint coordinate. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T13:47 |
| status | proved |
| reason | The independent review verifies both approximate rigidity alternatives and the concentration bound for all exactly normal residuals. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Bounded sequences with vanishing residual normality defect, exact classification and uniform cubic concentration for all exactly normal residuals. |
| argument | [Argument](#argument) | Graph pairing with omitted multipliers, phase-slice detection, asymptotic corner commutation, affine reduction and the scalar and selfadjoint cost bounds. |
| dependency | [Normal starred phase](Yin_C_F0076_v1.md#statement) | Unit secant symbol and its restriction to the scalar coordinate. |
| dependency | [Omitted-algebra graph invariance](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Left and right omitted multipliers preserve the graph, including for arbitrary bounded omitted elements. |
| dependency | [Vacuum tensor adjoint domain](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Finite sums of core polynomial tensors in the actual adjoint domain. |
| dependency | [Omitted-algebra commutation rigidity](Yin_C_F0226_v1.md#statement) | Variance collapse for a bounded omitted sequence asymptotically commuting with one fixed nonscalar marginal test. |
| dependency | [Cubic concentration](Yin_C_F0258_v1.md#statement) | Uniform integral for all omitted shifts from the original distinguished finite column cost. |
| dependency | [Planar scalar weight](Yin_C_F0267_v1.md#statement) | Single marginal density, total mass and universal constant controlling its right slice. |
| dependency | [Real-coordinate weight](Yin_C_F0266_v1.md#statement) | Joint finite-column bound and mass of the unnormalized dominating density at a selfadjoint coordinate. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0279_v1.md#finding) | Full fixed proof, including varying graph tests, phase slices and the affine-line case. |

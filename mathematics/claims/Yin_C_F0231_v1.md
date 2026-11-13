---
author: Yin
---
# Singular mass at a supporting half-plane of an omitted shift

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X_i\) be a coordinate of a finite bounded normal generating tuple with [actual ACSY](../tasks/Yin_T_F0011_v1.md#contract) in a finite von Neumann algebra with faithful normal probability trace \(\tau\).
Write \(N=W^*(X_j:j\ne i)\), \(X=X_i\), and \(\xi=\delta_i^*(1\otimes1)\) for the actual coordinate vacuum.
Fix \(\kappa\ge0\).
For each \(r>0\), let \(b\in N\) and unitaries \(V,W\in N\) satisfy
\[
        D=V^*(X-b)W,\qquad \operatorname{Re}D\ge-\kappa r\,1 .
\]
Set \(e=1_{[0,r]}(|X-b|)\), \(t=\tau(e)\), \(s=(2+3\kappa)r\), \(R=(D+s1)^{-1}\), \(q=\|R\|_2\), and \(u=VRW^*/q\).
Every such \(R\) exists.
The following estimates are uniform over these \(b,V,W\), including nonnormal \(b\) with arbitrary operator norm.

1. The finite-scale and small-radius estimates are
   \[
       \frac{t^3}{r^2}\le\frac{729}{16}(1+\kappa)^2|\langle\xi,u\rangle|^2,\qquad
       \lim_{r\downarrow0}\ \sup_{b,V,W}\frac{t^3}{r^2}=0 .                  \tag{1}
   \]
   For any finite family of admissible \(r_j,b_j,V_j,W_j\), put \(G=(\langle u_j,u_k\rangle)_{jk}\).
   Then
   \[
       \sum_j\frac{t_j^3}{r_j^2}\le\frac{729}{16}(1+\kappa)^2\|G\|\,\|\xi\|_2^2. \tag{2}
   \]
2. If \(\xi\in L^p(M)\) for \(2<p<\infty\), then \(t=O_{\kappa,p,\|\xi\|_p}(r^{p/(p+1)})\).
   If \(\xi\in M\), then \(t=O_{\kappa,\|\xi\|}(r\log(e/r))\) for \(0<r\le1\), with \(e\) in the logarithm denoting Euler's constant.

The hypothesis includes shifts \(b=v|b|\) with unitary \(v\in N\) and \(|b|\ge(\|X\|-\kappa r)1\), by taking \(V=-v\), \(W=1\) and using \(\operatorname{Re}(v^*X)\le\|X\|1\).
The Gram matrix in (2) tests the normalized resolvents with both omitted unitary factors.
The general [orthogonal singular-projection packing test](Yin_C_F0211_v1.md#statement) concerns arbitrary omitted shifts and orthogonal input projections.

## Argument

### The inverse in the closed graph

Put \(A=D+s1\) and \(g=2(1+\kappa)r\), so that \(\operatorname{Re}A\ge g1\).
Both \(A\) and \(A^*\) are bounded below by \(g\) in the trace representation, by Cauchy–Schwarz on their quadratic forms.
Consequently \(A\) is invertible in \(M\).
The [omitted-algebra graph property](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) gives \(\bar\delta_i A=V^*\otimes W\).
Every polynomial in \(A\) belongs to the closed graph with its product rule.
Indeed apply the bounded strongly-star omitted-polynomial approximation from the opening [shifted polynomial graph argument](Yin_C_F0229_v1.md#argument) separately to \(V,W,b\).
On the product net every resulting polynomial in \(A\) converges strongly-star on a bounded ball to its target.
In each differentiated term all outer coefficients converge strongly on the coarse Hilbert space by this bounded convergence, while each approximating omitted coefficient has zero derivative.
This proves the asserted graph convergence and Leibniz expansion.
For \(C>\max(2g,\|A\|^2/(2g))\) one has
\[
      \|1-A/C\|^2\le 1-2g/C+\|A\|^2/C^2<1 .
\]
The Neumann series \(R=C^{-1}\sum_{n\ge0}(1-A/C)^n\) converges in the graph because the derivative of its \(n\)-th power has coarse norm at most \(n\|1-A/C\|^{n-1}/C\).
Summing the absolutely convergent differentiated double series gives \(\bar\delta_i R=-RV^*\otimes WR\).
Using the left and right omitted graph actions gives \(\bar\delta_i(VRW^*)=-VRV^*\otimes WRW^*\).
The vacuum identity, trace invariance under conjugation and inner products linear in the second entry therefore give
\[
          \langle\xi,VRW^*\rangle=-(\tau R)^2,\qquad
          g^2q^3\le|\langle\xi,u\rangle| .                              \tag{3}
\]
The inequality follows from \(\operatorname{Re}R=R^*(\operatorname{Re}A)R\ge gR^*R\).
The singular spectral projection for \(D\) is \(e_D=W^*eW\), since \(|D|=W^*|X-b|W\).
Thus \(t=\tau(RAe_D)\le q\|Ae_D\|_2\le q(s+r)\sqrt{t}\), since \(\|De_D\|_2\le r\sqrt t\).
Thus \(t\le(s+r)^2q^2\).
Combining with (3) gives the first inequality of (1), since \((s+r)^6/g^4=(729/16)(1+\kappa)^2r^2\).
Taking the norm of the synthesis operator of the \(u_j\), whose square is \(\|G\|\), proves (2).

### Inverse tails of strictly accretive shifts

Let \(F(x)\) be the supremum of \(\tau(1_{[0,x]}(|X-b'|))\) over \(b'\in N\) and unitaries \(V',W'\in N\) with \(\operatorname{Re}((V')^*(X-b')W')\ge0\).
The first inequality of (1) with \(\kappa=0\) already gives
\[
            F(x)\le C_0x^{2/3},\qquad C_0=(729/16)^{1/3}\|\xi\|_2^{2/3}.
\]
For admissible \(b,V,W,r\), the operator \(A=V^*(X-(b-sVW^*))W\) has strictly positive real part, with \(b-sVW^*\in N\).
The trace law of \(|R|\) equals that of \(|A|^{-1}\), by the unitary polar decomposition of the invertible \(A\).
Also \(|A|\) is unitarily conjugate to \(|X-(b-sVW^*)|\), and the two unitary factors in \(u\) preserve the singular law of \(R/q\).
Consequently, if \(F(x)\le K x^\gamma\) for all \(x>0\) with \(0<\gamma<1\), then for every \(v>0\)
\[
     \tau(1_{(v,\infty)}(|R|))\le\min(Kv^{-\gamma},q^2/v^2).
\]
Integrating the smaller bound below and above \((q^2/K)^{1/(2-\gamma)}\) gives
\[
      \|u\|_1\le H_\gamma K^{1/(2-\gamma)}q^{-\gamma/(2-\gamma)},
      \qquad H_\gamma=\frac{2-\gamma}{1-\gamma}.                         \tag{4}
\]
With \(\gamma=2/3\) it follows that \(\|u\|_1\to0\) whenever \(q\to\infty\).
For every \(y\in M\), \(|\langle\xi,u\rangle|\le\|\xi-y\|_2+\|y\|\|u\|_1\), so the vacuum pairing tends to zero along any such sequence.
If \(t^3/r^2\) were bounded below by a positive constant along radii tending to zero, \(q\ge\sqrt t/(s+r)\) would tend to infinity.
The first inequality of (1) now proves its uniform limit.

### Iteration for a more integrable vacuum

Fix \(2<p<\infty\) and put \(h=1-2/p\) and \(\gamma_*=p/(p+1)\).
Suppose \(F(x)\le K x^\gamma\) with \(2/3\le\gamma\le\gamma_*\).
By ordinary Hölder interpolation of the spectral \(L^1,L^2\) norms, \(\|u\|_{p/(p-1)}\le\|u\|_1^h\|u\|_2^{1-h}\).
Writing \(\alpha=h\gamma/(2-\gamma)\), (3) and (4) give
\[
     g^2 q^{3+\alpha}\le\|\xi\|_p H_\gamma^h K^{h/(2-\gamma)} .
\]
Together with \(t\le(s+r)^2q^2\), this gives
\[
    t\le 9(1+\kappa)^2\max(1,\|\xi\|_p) H_\gamma^a K^\lambda r^{f(\gamma)},
    \quad
    f(\gamma)=\frac{2(1+\alpha)}{3+\alpha},\quad
    a=\frac{2h}{3+\alpha},\quad
    \lambda=\frac{a}{2-\gamma}.                                          \tag{5}
\]
Here \(g\ge2r\), \(s+r=3(1+\kappa)r\), and the power \(2/(3+\alpha)\) of the vacuum norm is at most one.

To iterate for \(F\), take \(\kappa=0\).
The map \(f\) is increasing on \([2/3,\gamma_*]\), fixes \(\gamma_*\), and \(f(\gamma)>\gamma\) below that endpoint.
Indeed, after multiplication by the positive denominator \((3+\alpha)(2-\gamma)\), the numerator of \(f(\gamma)-\gamma\) is \((2-\gamma)(2-(3-h)\gamma)\), and \(2/(3-h)=\gamma_*\).
Thus repeated application of \(f\) starting at \(2/3\) tends to \(\gamma_*\).

The constants can be chosen uniformly along the iteration and in \(p\) after factoring out \(p+1\).
Let \(A_0=9\max(1,\|\xi\|_p)\) and choose \(B_0=\max(1,C_0,(2A_0)^3)\).
For \(2/3\le\gamma\le\gamma_*\) we have \(H_\gamma\le2(p+1)\) and \(\lambda\le 2/3\).
Also \(a+\lambda=2h(3-\gamma)/(6-(3-h)\gamma)\le1\), since this last inequality is equivalent to \(3(1-h)(2-\gamma)\ge0\).
Starting with \(K=B_0(p+1)\), the next constant from (5) for \(F\) is bounded by
\[
       A_0\,2^a B_0^\lambda(p+1)^{a+\lambda}\le B_0(p+1).
\]
The initial bound at \(2/3\) holds with this \(K\), so passage to the limit gives \(F(x)\le B_0(p+1)x^{\gamma_*}\) at every \(x>0\).
Apply (5) once more with this constant and \(\gamma=\gamma_*\) for the original tolerance to obtain \(t\le(1+\kappa)^2 B_0(p+1)r^{p/(p+1)}\).
If \(\xi\) is bounded, the probability trace gives \(\|\xi\|_p\le\|\xi\|\), so \(B_0\) may be chosen independently of \(p\).
Taking \(p=\max(3,\log(1/r))\) for \(0<r\le1\) gives \(r^{p/(p+1)}\le \exp(1)\,r\) and \(p+1\le4+\log(1/r)\), proving the logarithmic estimate.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T17:14 |
| status | open |
| reason | The omitted-unitary supporting-half-plane mass estimates, normalized resolvent packing and integrability upgrade are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Pointwise, little-order and Gram packing estimates for arbitrary admissible omitted shifts, the finite-\(p\) mass exponent and the bounded-vacuum logarithmic estimate. |
| argument | [Argument](#argument) | Closed-graph inverse, signed vacuum identity, accretive real-part bounds, inverse tails, iteration and uniform control of its constants. |
| dependency | [Omitted-algebra graph actions](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | The closed graph admits left and right multiplication by every omitted element with zero derivative, used on \(V,W,b\) and the inverse test \(VRW^*\). |
| dependency | [Unconditioned shifted polynomial graph](Yin_C_F0229_v1.md#argument) | Opening graph paragraph, specifically the uniformly bounded strongly-star approximants from omitted starred polynomials and the resulting coarse convergence for each product. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T17:28 |
| status | proved |
| reason | Independent review confirms the two omitted unitaries, the exact inverse pairing, the uniform little-order bound and the endpoint iteration for integrable vacua. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Pointwise, little-order and Gram packing estimates for arbitrary admissible omitted shifts, the finite-\(p\) mass exponent and the bounded-vacuum logarithmic estimate. |
| argument | [Argument](#argument) | Closed-graph inverse, signed vacuum identity, accretive real-part bounds, inverse tails, iteration and uniform control of its constants. |
| dependency | [Omitted-algebra graph actions](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | The closed graph admits left and right multiplication by every omitted element with zero derivative, used on \(V,W,b\) and the inverse test \(VRW^*\). |
| dependency | [Unconditioned shifted polynomial graph](Yin_C_F0229_v1.md#argument) | Opening graph paragraph, specifically the uniformly bounded strongly-star approximants from omitted starred polynomials and the resulting coarse convergence for each product. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0240_v1.md#whole-proof-finding) | Both parts, the supporting-half-plane hypothesis at each scale, Gram packing and the finite and infinite integrability endpoints. |

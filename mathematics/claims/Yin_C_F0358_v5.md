---
author: Yin
---

# Dyadic determinants at a fixed imaginary shift for quasi-every real coefficient of a Wigner product

<a id="statement"></a>
## Ordinary logarithms as the coefficient of the first factor varies

Fix the [finite-second-moment Hermitian Wigner model](../tasks/Yin_T_F0013_v1.md#input-model), distinguish one input \(X\), and take any fixed selfadjoint scalar polynomial \(B\) in the same tuple.
Its coefficients are independent of the real parameter \(c\), and \(B\) may involve \(X\).
Fix a real \(t\ne0\), set \(P_c=(c+X)B\), and denote the finite and free ordinary logarithms by
\[
 U_N(c)=N^{-1}\log|\det(P_{c,N}-itI)|,\qquad
 u(c)=\tau\log|(c+s_x)B(s)-it|.
\]
Use \(\log0=-\infty\).
There is a deterministic [polar set](Yin_C_F0348_v1.md#polar-convention) \(E_t\) such that for every fixed real \(c>2\) outside \(E_t\) and every \(\epsilon>0\),
\[
        \sum_{j\ge1}\Pr\{|U_{2^j}(c)-u(c)|>\epsilon\}<\infty .
        \tag{1}
\]
In particular \(U_{2^j}(c)\to u(c)\) almost surely and \(\limsup_N U_N(c)=u(c)\) almost surely under every cross-size coupling.
The normalized logarithm of the [finite negative-subspace determinant](Yin_C_F0358_v3.md#statement) at \(it\) tends to zero along the same dyadic sizes, also with summable probabilities of deviations exceeding each \(\epsilon>0\).
The exceptional set uses only \(t,B\) and the marginal input laws, which may all be purely atomic.
The event of convergence may depend on the fixed coefficient.
For the [exact word-chain linearization](../ledger/Yin_L_F0061_v2.md#linearization-transfer), the finite and free logarithms are divided by its fixed auxiliary dimension.
For \(t=1\) this treats the prescribed spectral point \(i\), leaving the coefficient \(c=2\) outside the result.

<a id="half-plane"></a>
## A determinant quotient on a right half-plane

Fix finite Hermitian matrices \(X,B\), \(a>2\), and put \(X^\#=\max(X,-aI)\) by spectral calculus.
Let \(\mathcal R=\operatorname{ran}B\), write subscripts \(\mathcal R\) for compressions to this range, and set \(T=X^\#_{\mathcal R}-X_{\mathcal R}\ge0\).
In the decomposition \(\mathcal R\oplus\ker B\) the matrix \((w+X)B-itI\) is block lower triangular with lower diagonal block \(-itI\).
The determinant of its first diagonal block is
\(\det B_{\mathcal R}\det(wI+X_{\mathcal R}-itB_{\mathcal R}^{-1})\).
The same formula holds with \(X^\#\).
Use determinant one for a zero-dimensional range.

On \(\operatorname{Re}w>a\), put \(M=wI+X^\#_{\mathcal R}-itB_{\mathcal R}^{-1}\) and \(L=T^{1/2}M^{-1}T^{1/2}\).
The Hermitian part of \(M\) dominates \((\operatorname{Re}w-a)I\), so \(\|M^{-1}\|\le(\operatorname{Re}w-a)^{-1}\).
The identity \(\operatorname{Re}M^{-1}=M^{-*}(\operatorname{Re}M)M^{-1}\) gives \(\operatorname{Re}L\ge0\).
Cancel the two fixed range and kernel factors and cycle the determinant to obtain
\[
 \frac{\det((w+X)B-itI)}{\det((w+X^\#)B-itI)}
     =\det(I-L)=D(w)\det(I+L),
 \qquad D(w)=\frac{\det(I-L)}{\det(I+L)} .
 \tag{2}
\]
Since \((I+L)^*(I+L)-(I-L)^*(I-L)=4\operatorname{Re}L\ge0\), the Cayley transform \((I-L)(I+L)^{-1}\) is a contraction and \(|D|\le1\).
All singular values of \(I+sL\) are at least one for \(0\le s\le1\).
Integration of \(\operatorname{Re}\operatorname{Tr}((I+sL)^{-1}L)\) and the Schatten product inequality \(\|L\|_1\le\|M^{-1}\|\operatorname{Tr}T\) give
\[
  0\le\log|\det(I+L)|\le\operatorname{Tr}T/(\operatorname{Re}w-a).
  \tag{3}
\]

<a id="zeros"></a>
## The contribution of half-plane zeros

The bounded rational function \(D\) satisfies \(D(R)=1-2\operatorname{Tr}T/R+O(R^{-2})\) as real \(R\to+\infty\), by expanding \(M^{-1}\) there.
For each zero \(\alpha\) in the half-plane, counted with multiplicity, divide out \(b_\alpha(w)=(w-\alpha)/(w+\overline{\alpha}-2a)\), and call the resulting rational function \(H\).
There are finitely many factors, each has modulus one on the boundary line, and \(H(\infty)=1\).
Boundedness of \(D\) removes any rational pole on the boundary, so the maximum principle on expanding half-disks gives \(|H|\le1\).
Thus \(h=-\log|H|\) is a nonnegative harmonic function on the half-plane and
\[
 \lim_{R\to\infty}Rh(R)
    =2\left(\operatorname{Tr}T-\sum_{\alpha}(\operatorname{Re}\alpha-a)\right)\ge0.
 \tag{4}
\]
For fixed \(w\) and real \(R>a\), the disk form of Harnack's inequality gives \(h(w)\le(1+\rho)h(R)/(1-\rho)\) with \(\rho=|w-R|/|w+R-2a|\).
Indeed, after sending \(R\) to zero by the disk coordinate \((w-R)/(w+R-2a)\), the Poisson kernel on a circle of radius \(r>\rho\) is at most \((r+\rho)/(r-\rho)\) times its value at zero, and \(r\uparrow1\) gives the bound.
Since \(R^{-1}(1+\rho)/(1-\rho)\to1/(\operatorname{Re}w-a)\), equation (4) gives \(h(w)\le2\operatorname{Tr}T/(\operatorname{Re}w-a)\).

Fix a compact real interval \(K\subset(a,\infty)\), put \(d=\tfrac12\operatorname{dist}(K,a)>0\), and let \(V=\{\alpha:\operatorname{dist}(\alpha,K)<d\}\).
The identity
\[
 -\log|b_\alpha(w)|
 =\tfrac12\log\!\left(1+
      \frac{4(\operatorname{Re}w-a)(\operatorname{Re}\alpha-a)}{|w-\alpha|^2}\right)
\]
shows that for \(w\in K\), each \(\alpha\notin V\) costs at most \(C_K(\operatorname{Re}\alpha-a)\).
For \(\alpha\in V\) one instead has \(-\log|b_\alpha(w)|\le C_K+\log^-|w-\alpha|\), since the denominator of \(b_\alpha\) is bounded there.
Here \(\log^-r=\max(0,-\log r)\).
By (4), at most \(\operatorname{Tr}T/d\) zeros belong to \(V\).
Combining (2)--(4), for every \(w\in K\) we obtain
\[
 \left|\log\left|\frac{\det((w+X)B-itI)}{\det((w+X^\#)B-itI)}\right|\right|
 \le C_K\operatorname{Tr}T+
             \sum_{\alpha\in V}\log^-|w-\alpha| ,
 \tag{5}
\]
with the extended value at a zero.

<a id="dyadic"></a>
## Summing the coefficient zeros and identifying the free limit

Apply (5) in each Wigner size, always evaluating \(B\) on the original inputs, including the original \(X\).
The [dyadic tail estimate at \(p=1\)](Yin_C_F0365_v1.md#tails) gives
\[
 \sum_{N=2^j,\,j\ge1}\mathbb E\,N^{-1}\operatorname{Tr}T
 \le\sum_{N=2^j,\,j\ge1}\mathbb E\,\operatorname{tr}_N((-aI-X)_+)<\infty .
\]
For \(m\ge2\) choose \(a=2+1/(2m)\), \(K_m=[2+1/m,2+m]\), and \(V_m\) as in (5).
The measure \(\eta_m=\sum_{j\ge1}2^{-j}\mathbb E\sum_{\alpha\in V_m}\delta_\alpha\), using the zeros at size \(2^j\), is finite by (4).
These counts are measurable as the half-plane zeros coincide, with multiplicity, with those of the numerator determinant in (2), a nonzero polynomial with measurable coefficients at each size.
The measure \(\eta=\sum_{m\ge2}2^{-m}\eta_m/(1+\eta_m(\mathbb C))\) is finite.
The [finite-energy criterion for mean zero measures](Yin_C_F0358_v4.md#polar) makes \(E_t=\{c:\int\log^-|c-\alpha|\,d\eta(\alpha)=\infty\}\) polar.
For fixed \(c\in K_m\setminus E_t\), (5) and Tonelli give a finite dyadic sum of the expected absolute normalized log ratios.
Those ratios therefore tend to zero in normalized logarithm almost surely for every coupling.

For such a real \(c\), put \(S^\#=(cI+X^\#)^{1/2}\) and \(S=|cI+X|^{1/2}\).
The determinant in the denominator of (2) equals that of the Hermitian product \(S^\#BS^\#\) shifted by \(itI\).
The rank distance between \(S^\#BS^\#\) and \(SBS\) is at most \(2\#\{\lambda(X)<-a\}\), by expanding their difference.
Its fraction tends to zero almost surely along the dyadics by the same tail estimate with \(|X|\mathbf1_{|X|>a}\).
The [Hermitian comparison theorem](Yin_C_F0358_v3.md#comparison), applicable since \(c+s_x\ge(c-2)1>0\), and rank interlacing give weak convergence of the clipped Hermitian laws to the spectral law of \((c+s_x)^{1/2}B(s)(c+s_x)^{1/2}\).
Moreover \((S^\#)^2\le |cI+X|+(c-a)I\) by scalar calculus, so its normalized squared positive-log singular moments are eventually bounded by the [polynomial log estimates](Yin_C_F0186_v4.md#log-statistics).
The three-factor singular-value bound in the same [Hermitian comparison proof](Yin_C_F0358_v3.md#comparison) transfers these bounds and those for \(B\) to \(S^\#BS^\#\).
Since \(\log|x-it|\) is bounded below on the real line, truncation gives convergence of the normalized denominator logarithm to \(u(c)\), using [free cycling](Yin_C_F0358_v1.md#free-inertia).

Equation (2) now yields dyadic almost-sure convergence of \(U_N(c)\).
The [full-sequence regularized upper bound](Yin_C_F0348_v1.md#argument) gives the stated upper-limit equality.
Subtracting the [convergent Hermitian logarithm](Yin_C_F0358_v3.md#comparison) of \(SBS-itI\) gives the asserted negative-subspace limit by its [exact determinant identity](Yin_C_F0358_v3.md#argument).
Apply both dyadic limits to the coupling with independent samples across sizes.
For each deviation threshold the events are independent in this coupling, so the converse part of Borel--Cantelli proves (1) and the same summability for the compression, both in terms of single-size probabilities.

## Current assessment
[Selected decision](#decision-coefficient-half-plane-reviewed)

## Assessment history

### Decision coefficient-half-plane-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:49 |
| status | open |
| reason | The coefficient determinant factors into a bounded half-plane quotient and a controlled nonvanishing factor, allowing the dyadic tail estimate to bound its logarithmic loss outside a polar set. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Fixed imaginary shift and real coefficient](#statement) | Ordinary dyadic logarithms and the full upper limit under arbitrary coupling. |
| argument | [Finite quotient](#half-plane) | Singular second factors, clipping and accretivity at a fixed imaginary shift. |
| support | [Local zero estimate](#zeros) | The finite Blaschke factors, harmonic term and clipped trace bound. |
| support | [Dyadic limit](#dyadic) | The deterministic polar exception, free limit and summable marginal deviations. |

### Decision coefficient-half-plane-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T17:54 |
| status | proved |
| reason | The accretive coefficient quotient and dyadic negative-tail estimate give summable marginal deviations at each nonexceptional fixed real coefficient strictly above two. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Fixed imaginary shift and varying real coefficient](#statement) | The polar set may depend on the fixed imaginary shift and the model. |
| argument | [Complete half-plane proof](#half-plane) | Range compression and the finite determinant ratio. |
| support | [Dyadic probabilities](#dyadic) | Ordinary and compressed logarithms and the auxiliary trace factor. |
| review | [Independent whole-proof assessment](../audits/reviews/Yin_R_F0366_v5.md#coefficient-half-plane-whole-proof) | The fixed theorem with real coefficient greater than two. |

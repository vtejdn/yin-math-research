---
author: Yin
---

# Pure-imaginary Wigner zero-shift logarithms and constant-diagonal floors

<a id="scope"></a>
## Scope and review boundary

The first deduction below gives an almost-sure logarithmic limit through even dimensions for a single purely imaginary Wigner input with zero diagonal and zero spectral shift.
This is stronger in probability mode than the corresponding conclusions in the adopted [scalar-affine assembly](../claims/Yin_C_F0186_v11.md#scalar-affine-statement) and [signed carrier theorem](../claims/Yin_C_F0186_v12.md#signed-carrier-statement).
The second deduction treats a nonzero constant diagonal law at every fixed scalar parameter; that law lies outside the [adopted nonconstant-diagonal floor](../claims/Yin_C_F0194_v8.md#pure-imaginary-application).
These two deductions remain proof development without their own formal review or adoption.
The accepted input reviews do not constitute review of these assembled conclusions.

Fix a real law \(\eta\) with \(\mathbb E\eta=0\) and \(\mathbb E\eta^2=1\).
For each dimension \(N\), let \(W_N\) have independent strict upper entries \(i\eta_{jk}/\sqrt N\), conjugate lower entries, and identically zero diagonal.
Every realization is Hermitian and transpose-skew.
The entry law is fixed independently of dimension, and the dimensions may have any coupling preserving these within-dimension laws.
No moment above two, density or cross-size independence is assumed.
Let \(s\) be a standard semicircular element in a finite von Neumann algebra with faithful normal tracial state \(\tau\), and use ordinary determinants with \(\log0=-\infty\).

<a id="even-zero-log"></a>
## Almost-sure zero-shift logarithms through even dimensions

Apply the adopted [C_F0194_v7 even skew floor](../claims/Yin_C_F0194_v7.md#even-floor) to this model with \(F=0\) and \(b>2\).
Its failures are summable over even dimensions, so first Borel--Cantelli supplies an eventual polynomial least-value floor there.
The accepted [C_F0187_v2 intermediate theorem](../claims/Yin_C_F0187_v2.md#statement), applied to the original complex law \(i\eta\), gives increasing singular values
\[
 a_r(W_N)\ge c(r-1)/N,\qquad
 \lceil N^{3/4}\rceil+1\le r\le N
\]
outside a summable exceptional event.
This intermediate theorem allows the zero diagonal and imposes no real/imaginary independence condition.

The accepted [C_F0186_v4 complex-input controls](../claims/Yin_C_F0186_v4.md#statement) give weak convergence to the semicircular spectral law, equivalently convergence of singular laws to that of \(|s|\), and positive logarithmic tail control.
The semicircular law has bounded density near zero, so \(\tau\log|s|\) is finite.
On the even-dimensional good event, the bottom \(O(N^{3/4})\) normalized negative logarithms contribute \(O(N^{-1/4}\log N)\).
The middle bound controls the remaining values below \(t\) by \(Ct(1+|\log t|)+o(1)\).
Clipping the logarithm at fixed lower and upper cutoffs, passing by the weak law, then removing the tails proves
\[
 \frac1N\log|\det W_N|\longrightarrow \tau\log|s|\in\mathbb R
 \quad\hbox{almost surely as }N\to\infty\hbox{ through even dimensions}.
 \tag{Even-log}
\]
Every odd-dimensional log determinant equals \(-\infty\) identically.
Consequently the same deduction includes
\[
 \limsup_{N\to\infty}N^{-1}\log|\det W_N|
  =\tau\log|s|,\qquad
 \liminf_{N\to\infty}N^{-1}\log|\det W_N|=-\infty
 \quad\hbox{almost surely under every allowed coupling}.
\]
This is the one-input zero-shift instance, rather than a theorem for arbitrary polynomials or arbitrary spectral parameters.

<a id="scalar-shift-guards"></a>
## Fixed scalar floors for a nonzero constant diagonal

Separately fix \(a\in\mathbb R\setminus\{0\}\) and put
\[
 W_N^{(a)}=W_N+\frac{a}{\sqrt N}I_N.
\]
This has the same centered variance-one purely imaginary upper law and the fixed real diagonal law \(\zeta=a\), which is not centered.
For each fixed \(\lambda\in\mathbb C\) and \(b>0\), the following floor holds for some fixed \(A,C_b,C,N_0>0\):
\[
 \mathbb P\{s_{\min}(W_N^{(a)}-\lambda I_N)\le N^{-A}\}
 \le C_bN^{-b}+C\sqrt{\log(2+N)}N^{-1/18},
 \qquad N\ge N_0.
 \tag{Constant-diagonal-scalar-floor}
\]
There is no parity restriction, and the constants may depend on the fixed law, \(a\), \(\lambda\) and \(b\).

Use the adopted [C_F0194_v7 quantile-guarded floor](../claims/Yin_C_F0194_v7.md#quantile-guard-floor), whose real diagonal law need not be centered, with \(F=-\lambda I_N\) and \(L_0=1\).
For \(k_N=4\lfloor\sqrt N\rfloor+1\), every actual principal minor has symmetric part
\[
 S_i=\left(\frac{a}{\sqrt N}-\lambda\right)I_{N-1}.
\]
If \(\lambda=0\), then \(s_{k_N}(S_i)=|a|/\sqrt N\ge N^{-1}\) for all sufficiently large \(N\).
If \(\lambda\ne0\), then \(|a/\sqrt N-\lambda|\ge|\lambda|/2\ge N^{-1}\) for all sufficiently large \(N\).
Thus the exact symmetric-principal-quantile guard holds deterministically in both cases, and the fixed shift satisfies a polynomial entry bound.
The accepted guarded theorem proves (Constant-diagonal-scalar-floor) without any additional guard failure.
Its matching error is not claimed summable.

This fixed-parameter result does not contradict the [constant-diagonal obstruction](../claims/Yin_C_F0194_v8.md#constant-diagonal-boundary): the cancelling shift \(-aI_N/\sqrt N\) in that obstruction varies with dimension.
No logarithmic conclusion for a noncentered diagonal model is asserted here; the logarithmic argument above uses only the centered zero-diagonal model.
For a nonconstant finite-second-moment diagonal law, including a noncentered one, the adopted C_F0194_v8 application already gives the stronger arbitrary-complex-shift probability floor.

---
author: Yin
---

# Spectral mass around every small positive spectral value of a Schur complement

## Statement

Let \(H\) be finitely generated, with word length \(|g|\), and assume the ball form of rapid decay
\[
        \|f\|_{\rm op}\le C(1+N)^r\|f\|_2
           \quad(\operatorname{supp}f\subseteq\{|g|\le N\}),\qquad r>0 .
\]
Let \(K=[L,R]\in M_2(\mathbb C H)\), where the regular column \(L\) is bounded below.
Put
\[
 a=L^*L,\quad X=a^{-1}L^*R,\quad D=R^*R-(L^*R)^*a^{-1}(L^*R).
\]
Fix \(\Lambda\ge\|K\|^2\), and write \(B=K^*K/\Lambda,\ S=D/\Lambda\).
Both are positive contractions.
For \(T=B,S\), use its regular spectral measure \(\mu_T\), with unnormalized coordinate trace, and put \(F_T(u)=\mu_T((0,u])\).
All estimates concern positive spectral mass and allow an atom at zero.

There are constants \(0<c<1<C_1,\ b>0,\ \lambda_0>0\), depending on the input, such that for **every** \(\lambda\in\sigma(S)\cap(0,\lambda_0)\),
\[
          \mu_S((c\lambda,C_1\lambda])
                \ \ge\ b\,\frac{\lambda^r}{(1+\log(1/\lambda))^{2r}} .
\]
For nonclosed range there is also the critical estimate
\[
                       \limsup_{u\downarrow0}\frac{F_S(u)}{u^r}>0 .
\]
In particular \(\int_{(0,1]}u^{-r}\,d\mu_S(u)\) diverges.
Either \(F_S(u)=o(u^r)\) or finiteness of this positive-spectrum negative moment forces closed range of \(S\) and \(K\).
For fractional four-site inputs the [bounded column theorem](Yin_C_A0323_v1.md#statement) supplies \(L\).
In that setting, if the scalar projection traces of \(C_r^*(H)\) omit the regular nullity, the two estimates necessarily apply at a nonclosed range.
The estimates themselves require no trace-range assumption.

The proof also gives a test for excluding a specified point of \(\sigma(S)\) using a finite moment of the original matrix \(B\).
The group-ring matrix \(K\) can have arbitrary finite support, and the Schur scalar \(D\) can have infinite Fourier support.

## Comparing spectral intervals under bounded elimination

Let
\[
       U=\begin{pmatrix}1&-X\\0&1\end{pmatrix},\qquad
       k=\max(\|U\|^2,\|U^{-1}\|^2),\qquad \beta=\min\sigma(a/\Lambda)>0 .
\]
An upper bound for \(k\), such as \((1+\|X\|)^2\), can be used throughout.
The [Gram congruence](Yin_C_A0323_v1.md#reduction-to-one-scalar-in-the-reduced-group-algebra) gives \(U^*BU=\operatorname{diag}(a/\Lambda,S)\).
For positive \(T\) write \(N_T(u)=\mu_T([0,u])\) when \(u\ge0\).
For \(T_0=U^*BU\) one has \(N_B(u/k)\le N_{T_0}(u)\le N_B(ku)\).
Indeed on the image by \(U\) of the spectral subspace \(T_0\le u\), the Rayleigh quotient of \(B\) is at most \(ku\).
This image has the original trace dimension and has trivial intersection with the spectral subspace \(B>ku\), so its dimension is at most \(N_B(ku)\).
Applying the same argument to \(U^{-1}\) gives the other direction.
The two kernel dimensions coincide.
Subtracting them and using the gap in \(a/\Lambda\) gives
\[
                         F_B(u/k)\le F_S(u)\le F_B(ku)
                                  \qquad (0<u<\beta).
\]
This also proves equivalence of the two positive gaps at zero.

For each \(0<\lambda<\beta\) belonging to \(\sigma(S)\), there is a \(\lambda'\in\sigma(B)\cap[\lambda/k,k\lambda]\).
In fact every sufficiently small open neighborhood of \(\lambda\) has positive spectral mass by faithfulness.
Comparison across its two endpoints yields positive spectral mass of \(B\) between the lower endpoint divided by \(k\) and the upper endpoint multiplied by \(k\).
Shrinking the neighborhood and using closedness of the spectrum proves the assertion.
Conversely any positive mass of \(B\) on \((l,h]\) is retained in the wider Schur band:
\[
                 \mu_S((l/k,kh])\ge\mu_B((l,h])\qquad(0<l<h,\ kh<\beta).
\]

## A polynomial localized at a spectral point

We prove the annular estimate first for \(B\).
Choose an integer \(w\ge1\) bounding its propagation, so each matrix entry is supported in the ball of radius \(w\).
The assumed ball inequality applies also to matrices with the same constant, by bounding their operator norm by the square root of the sum of squared entry norms.
For \(0\le u\le1\), take \(\theta=\arcsin\sqrt u\) and use the [polynomial Fejer kernel](Yin_C_A0056_v1.md#argument)
\[
    f_n(u)=\left(\frac{\sin(n\theta)}{n\sin\theta}\right)^2,\qquad
    f_n(0)=1,\qquad h_n(u)=4 f_n(u)(1-f_n(u)).
\]
The polynomial degrees are at most \(n-1,2(n-1)\), respectively, and \(0\le h_n\le1\), \(h_n(0)=0\).
One has
\[
         f_n(u)\le\min(1,(n^2u)^{-1}),\qquad 1-f_n(u)\le C_2 n^2u .
\]
The second estimate follows by writing the squared average of the \(n\) phases \(e^{2ij\theta}\) as a double sum, then applying \(1-\cos(2(i-j)\theta)\le2(i-j)^2\theta^2\) and \(\theta\le\pi\sqrt u/2\).

Fix \(y\in(0,\pi)\) with \((\sin y/y)^2=1/2\).
For any sufficiently small \(\lambda\in\sigma(B)\setminus\{0\}\), take \(n\) to be the nearest integer to \(y/\arcsin\sqrt\lambda\).
Then \(n\asymp\lambda^{-1/2}\), \(f_n(\lambda)=1/2+O(\sqrt\lambda)\), and \(h_n(\lambda)\ge1-C_3\lambda\).
Indeed \(n\theta=y+O(\theta)\), \(\sin\theta/\theta=1+O(\theta^2)\), and \(4f(1-f)=1-4(f-1/2)^2\).
There are fixed \(0<c_2<1<C_4\) such that \(h_n(u)\le1/2\) for \(u\notin(c_2\lambda,C_4\lambda]\), by the two bounds just proved.
Set \(j=\lceil(r+1)\log_2(1/\lambda)\rceil\).
For small enough \(\lambda\), spectral calculus gives \(\|h_n(B)^j\|\ge(1-C_3\lambda)^j\ge1/2\).
The polynomial has propagation at most \(2j(n-1)w\).
Consequently
\[
 \frac1{4C^2(1+2j(n-1)w)^{2r}}
      \ \le\ \int h_n(u)^{2j}\,d\mu_B(u)
      \ \le\ \mu_B((c_2\lambda,C_4\lambda])+2\cdot 2^{-2j}.
\]
The last error is \(O(\lambda^{2r+2})\), since the unnormalized matrix measure has total mass two.
The lower bound on the left is at least a constant times \(\lambda^r/(1+\log(1/\lambda))^{2r}\).
This proves the annular estimate at every sufficiently small actual spectral point of \(B\), irrespective of gaps elsewhere in its spectrum.
Given such a point \(\lambda\) of \(S\), apply this estimate at a point of \(\sigma(B)\) between \(\lambda/k\) and \(k\lambda\).
The previous band comparison then proves the bound for \(S\), using the widened annulus \((c_2\lambda/k^2,k^2C_4\lambda]\).

## The critical exponent and finite moments in the original group

Suppose positive spectrum of \(B\) tends to zero.
Choose a sequence of such spectral points and the corresponding integers \(n\to\infty\) above.
Now fix an integer \(j\ge1\) with \(d=2j>r\).
The norms \(\|h_n(B)^j\|\) are bounded below, so the ball inequality gives \(\int h_n^{2j}\,d\mu_B\ge c_3 n^{-2r}\) along this sequence with \(c_3>0\).
If \(F_B(u)=o(u^r)\), the integral is instead \(o(n^{-2r})\).
Indeed \(h_n^{2j}\le 4^{2j}\min(1,(n^2u)^{-d})\) for \(u>0\) and vanishes at zero.
Integration of that decreasing majorant on the positive spectrum, before the factor \(4^{2j}\), gives
\[
       n^{-2d}F_B(1)+d n^{-2d}\int_{n^{-2}}^1 F_B(u)u^{-d-1}\,du .
\]
On a sufficiently small fixed interval insert \(F_B(u)\le\epsilon u^r\) for arbitrary \(\epsilon>0\), and on its complement use boundedness of \(F_B\).
Since \(d>r\) this gives the claimed little-oh estimate.
Thus the critical limsup for \(B\) is positive.
Nonclosed range of \(K\) is equivalent to positive spectrum tending to zero for \(B\) and also for \(S\).
As \(F_B(u)\le F_S(ku)\) at small \(u\), the critical limsup for \(S\) follows.
A finite negative \(r\)-th moment would imply \(u^{-r}F_S(u)\le\int_{(0,u]}v^{-r}\,d\mu_S(v)\to0\), giving the stated divergence and closed-range tests.
If the kernel trace is absent from the scalar projection traces, closed range is impossible by the [scalar projection construction](Yin_C_A0323_v1.md#reduction-to-one-scalar-in-the-reduced-group-algebra).

For a finite moment test, take any polynomial \(q\) of degree \(m\) and \(0<\lambda<\beta\).
If
\[
   \min_{u\in[\lambda/k,k\lambda]\cap[0,1]} |q(u)|^2
               > C^2(1+mw)^{2r}({\rm Tr}_2\otimes\tau)(q(B)^*q(B)),
\]
then \(\lambda\notin\sigma(S)\).
Indeed the right side bounds \(\|q(B)\|^2\).
Any spectral preimage in the indicated interval would contradict the inequality.
This test uses only group coefficients at the identity of a polynomial in \(B\) of degree at most \(2m\).
They are determined by grouping the products of the original finite-support coefficients according to their equalities in \(H\) through word length \(2mw\).
Thus the numerical test with a supplied ball constant and a valid bound on \(k\) never requires the Fourier coefficients of \(a^{-1}\).

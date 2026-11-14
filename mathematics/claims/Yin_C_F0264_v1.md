---
author: Yin
---

# A real law forces a local density term in addition to the vacuum square

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

There is a compactly supported probability law \(d\mu=\rho\,dx\) on the real line such that \(X(x)=x\) has an actual conjugate variable \(\xi\) in \(L^2(\mu)\), and both the original canonical right-slice closure and its Hilbert adjoint contain \(L^\infty(\mu)\) in their domains.
Write \(E=(\mathrm{id}\otimes\tau)\delta_X\) on the represented polynomial algebra, with \(\delta_X X=1\otimes1\).
If \(d\in L^1(\mu)_+\) and \(C<\infty\) satisfy
\[
                   \|Ep\|_2^2\le C^2\int |p|^2d\,d\mu
                      \qquad (p\in\mathbb C[X]),                         \tag{1}
\]
then almost everywhere for \(\mu\)
\[
                   C^2 d(x)\ \ge\ \tfrac14|\xi(x)|^2+\pi^2\rho(x)^2 .
                                                                         \tag{2}
\]
Here \(\rho\) is constant on each of a countable family of disjoint intervals.
Its values on those intervals tend to infinity, although \(|\xi|\) is uniformly bounded on a positive-length subinterval of every one of them.
Consequently every \(d\) with \(d\le K(1+|\xi|^2)\) almost everywhere for some \(K<\infty\) fails (1).

Adjoin a standard semicircular \(S\) freely to \(X\) and work in \(M=W^*(X,S)\) with its free product trace.
The pair satisfies actual starred ACSY and the strong condition on the original mixed core, with vacuum coordinates \(\xi,S\) and both bounded-vector domains for its actual canonical closures.
For a positive \(d\in L^1(M)\), domination of the original mixed right slice at \(X\) by \(C^2\tau(dp^*p)\) forces (2) with the marginal compression \(\mathbb E_{W^*(X)}d\) in place of \(d\).
In particular the following explicit family contains no dominating probability density.
Start from the squares
\[
          (\alpha1+\beta\xi+\gamma S)^*(\alpha1+\beta\xi+\gamma S),
                       \qquad \alpha,\beta,\gamma\in\mathbb C ,
\]
and allow finite positive linear combinations and finitely many applications of the trace-preserving expectations onto \(W^*(X)\), \(W^*(S)\), or the scalars.
This covers arbitrary signs in the scalar coefficients and positive scalar quadratic forms in these two joint vacua.
The obstruction concerns these proposed densities on a pair having the full domains.

## Argument

### Separated intervals and the actual scalar vacuum

For \(n\ge1\) set \(c_n=2^{-n}\), \(\ell_n=2^{-6n-4}\), \(A_n=2^n\) and \(I_n=(c_n-\ell_n,c_n+\ell_n)\).
The closures of the intervals are disjoint because \(\ell_n\le c_n/32\) and \(c_{n+1}=c_n/2\).
Define
\[
       \rho(x)=\kappa\sum_{n\ge1} A_n1_{I_n}(x),\qquad
                  \kappa=\left(2\sum_{n\ge1}A_n\ell_n\right)^{-1}.
\]
This is an atomless probability supported in \([0,1]\), with \(\rho\in L^3(dx)\) by \(\sum_n A_n^3\ell_n<\infty\).
Put \(H_\varepsilon(x)=\int_{|x-y|>\varepsilon}(x-y)^{-1}\,d\mu(y)\).
If \(x\in I_n\), the contribution of \(I_m\) for \(m<n\) is bounded absolutely by \(6\kappa A_m\ell_m/c_m\).
For \(m>n\) the same bound holds with denominator \(c_n\).
Indeed the distance between these intervals exceeds one third of the larger center.
The sums of both bounds are uniformly bounded, using \(A_m\ell_m=2^{-5m-4}\) and the geometric tail for \(m>n\).
For fixed \(x\) all the other intervals have positive distance from \(x\), so their contribution converges as \(\varepsilon\downarrow0\).

Inside the interval \(I_n=(a_n,b_n)\) the self contribution converges to \(\kappa A_n\log((x-a_n)/(b_n-x))\).
Its truncations are uniformly bounded in absolute value by the absolute value of that limit.
Indeed the truncated integral is \(\kappa A_n\) times the difference of the positive parts of \(\log((x-a_n)/\varepsilon)\) and \(\log((b_n-x)/\varepsilon)\).
The square integral of the logarithm over \(I_n\) against Lebesgue measure is a fixed finite multiple of \(\ell_n\) by rescaling.
Thus a common \(L^2(\mu)\) majorant follows from \(\sum_n A_n^3\ell_n<\infty\).
Dominated convergence gives a real \(H\in L^2(\mu)\) with \(H_\varepsilon\to H\) in \(L^2(\mu)\).

On the represented polynomials the scalar outer derivation is \(\delta_Xp(x,y)=(p(x)-p(y))/(x-y)\) off the null diagonal.
The quotient is bounded for each polynomial on \([0,1]\).
Antisymmetrizing its integral on \(|x-y|>\varepsilon\) gives \(2\int pH_\varepsilon\,d\mu\).
Passing to the limit gives the actual Hilbert adjoint value \(\xi=2H\) at \(1\otimes1\) by density of the polynomial core.
The [scalar actual-domain theorem](Yin_C_F0055_v1.md#statement) now gives the asserted canonical and adjoint domains and boundedness from operator norm to Hilbert norm on the core.

On \(J_n=(c_n-r_n,c_n+r_n)\), where \(r_n=\ell_n/(10A_n)\), the logarithm has absolute value at most \(3r_n/\ell_n\), using \(|(x-c_n)/\ell_n|\le1/10\).
The self contribution is uniformly bounded there, as is the sum of the other intervals.
Hence \(\sup_n\operatorname*{ess\,sup}_{J_n}|\xi|<\infty\), while \(\rho=\kappa A_n\) on \(J_n\).

### Modulated real-line tests on the original core

For \(f\in C^1([0,1])\) the integral \(E f(x)=\int (f(x)-f(y))/(x-y)\,d\mu(y)\) is bounded by \(\|f'\|_\infty\).
Approximate \(f'\) uniformly by complex polynomials and integrate the approximants with the correct initial value.
Both \(f\) and its derivative are then approximated uniformly by polynomials and their derivatives.
It follows that (1), when valid on its original core, holds for each such \(f\) with this integral as its output, since \(d\) is integrable.

Fix an interval \(I_n\), write \(r=\kappa A_n\), and choose \(\phi\in C^\infty_c(I_n)\).
For \(k>0\) let \(f_k(x)=\phi(x)e^{ikx}\), extending \(\phi\) by zero outside \(I_n\).
For \(x\in I_n\) the symmetric truncated integral and its limit give
\[
       E f_k(x)= e^{ikx}\phi(x)H(x)-
                        r\,\operatorname{pv}\int_{\mathbb R}
                              \frac{\phi(y)e^{iky}}{x-y}\,dy .             \tag{3}
\]
The second term only sees \(\rho\) on the support of \(\phi\).
For each fixed \(x\), after multiplication by \(e^{-ikx}\), its principal value without the prefactor \(r\) tends to \(-i\pi\phi(x)\).
To see this, substitute \(t=x-y\) and subtract \(\phi(x)\) in the numerator on \(|t|<1\).
The residual function \((\phi(x-t)-\phi(x)1_{\{|t|<1\}})/t\) belongs to \(L^1(dt)\) and its Fourier integral tends to zero by the Riemann–Lebesgue lemma.
The remaining integral is \(-2i\phi(x)\int_0^k (\sin u)/u\,du\).
The latter real integral tends to \(\pi/2\) by the Dirichlet integral, obtained for example by first inserting \(e^{-\eta u}\), integrating to \(\arctan(1/\eta)\), and removing the damping using the uniform \(O(1/R)\) tails from integration by parts on \([R,\infty)\).

It follows that \(e^{-ikx}E f_k(x)\to\phi(x)(H(x)+i\pi r)\) on \(I_n\).
Since \(H\) is real and \(|f_k|^2=|\phi|^2\), Fatou's lemma restricted to \(I_n\) in (1) gives
\[
     \int_{I_n}|\phi|^2 (H^2+\pi^2r^2)\,d\mu
                       \le C^2\int_{I_n}|\phi|^2d\,d\mu .                 \tag{4}
\]
These squared tests imply the order inequality of the corresponding finite measures on \(I_n\), by uniformly approximating the square roots of nonnegative compactly supported continuous tests by smooth functions there.
The union of the intervals carries the entire probability.
Substitution of \(H=\xi/2\) in (4) now proves (2).
On the sets \(J_n\) its right side grows at least as \(\pi^2\kappa^2 A_n^2\), whereas \(K(1+|\xi|^2)\) is bounded there uniformly in \(n\).
Their positive \(\mu\)-mass proves the claimed failure.

### Joint vacuum squares after free semicircular extension

Let \(B_X=W^*(X)\) and \(B_S=W^*(S)\).
The semicircular difference quotient has its actual vacuum \(S\) by the semicircular integration-by-parts identity, equivalently by cutting the scalar Chebyshev recurrence.
Extend each marginal derivation by zero on the other free factor.
On centered reduced words of length at least two every double-trace derivative vanishes by freeness of a nonempty segment on one side of each cut, and such words are orthogonal to either marginal vacuum.
This gives the actual joint adjoints on the mixed core by the [free extension vacuum argument](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words).
The [free marginal domain theorem](Yin_C_F0045_v1.md#statement), with the scalar actual-domain theorem applied in both factors, gives all bounded vectors in the domains of each original canonical contraction and its actual adjoint.
The negatives of the normalized closures give the generator-first strong systems.
On polynomials in \(X\) the mixed right slice has precisely the same values as the scalar \(E\).
Since \(\tau(dp^*p)=\tau((\mathbb E_{B_X}d)p^*p)\) there, (2) constrains this compression of every mixed dominating \(d\).

Write \(v=\alpha1+\beta\xi+\gamma S\), a tracial \(L^2\) vector.
Using \(\tau(\xi)=0\) from the vacuum identity on \(1\), \(\tau(S)=0\), \(\tau(S^2)=1\), and freeness, the two compressions are
\[
 \mathbb E_{B_X}(v^*v)=|\alpha+\beta\xi|^2+|\gamma|^2 1,\qquad
 \mathbb E_{B_S}(v^*v)=|\alpha+\gamma S|^2+|\beta|^2\|\xi\|_2^2 1 .
\]
These formulas follow first for bounded centered truncations of \(\xi\), then by \(L^2\) convergence and continuity of multiplication \(L^2\times L^2\to L^1\).
The first expectation is bounded above by \(K_v(1+|\xi|^2)\).
The second is bounded because \(S\) is bounded.
For either marginal \(L^1\) element its conditional expectation onto the other free marginal equals its trace times \(1\), first for bounded elements and then by truncation.
Idempotence of the expectations and linearity now give the same upper bound with some finite constant for the \(B_X\)-compression of every element of the stated family.
Equation (2) therefore excludes them all from domination at \(X\), even on single marginal polynomials in the original mixed core.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T12:53 |
| status | open |
| reason | Fix the local lower bound for dominating densities, the separated real-law example and its finite joint quadratic-form obstruction for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Necessary local density and vacuum terms, exclusion of all densities bounded by a constant plus the vacuum square on this law, and specified mixed quadratic forms after a free extension. |
| argument | [Argument](#argument) | Actual truncated scalar adjoint, bounded-vacuum peak centers, modulated original-core tests, local principal-value limit and finite compressions of joint quadratic expressions. |
| dependency | [Actual scalar-domain theorem](Yin_C_F0055_v1.md#statement) | The actual marginal vacuum implies both original bounded-vector domains and the marginal operator-norm-to-Hilbert estimate. |
| dependency | [Free extension of the vacuum](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Centered free-word tests for the actual vacuum of each extended marginal derivation. |
| dependency | [Free marginal domain lift](Yin_C_F0045_v1.md#statement) | Lifting the original canonical domains and actual adjoints from the two scalar marginals to all bounded vectors of the free product. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T13:06 |
| status | proved |
| reason | The independent review verifies the local weight obstruction on the actual scalar core and its persistence for the stated quadratic expressions after free extension. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Necessary local density and vacuum terms, exclusion of all densities bounded by a constant plus the vacuum square on this law, and specified mixed quadratic forms after a free extension. |
| argument | [Argument](#argument) | Actual truncated scalar adjoint, bounded-vacuum peak centers, modulated original-core tests, local principal-value limit and finite compressions of joint quadratic expressions. |
| dependency | [Actual scalar-domain theorem](Yin_C_F0055_v1.md#statement) | The actual marginal vacuum implies both original bounded-vector domains and the marginal operator-norm-to-Hilbert estimate. |
| dependency | [Free extension of the vacuum](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Centered free-word tests for the actual vacuum of each extended marginal derivation. |
| dependency | [Free marginal domain lift](Yin_C_F0045_v1.md#statement) | Lifting the original canonical domains and actual adjoints from the two scalar marginals to all bounded vectors of the free product. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0273_v1.md#finding) | Entire separated-interval construction, actual domains, localized modulation and marginal compressions. |

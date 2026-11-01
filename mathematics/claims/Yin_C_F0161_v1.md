---
author: Yin
---
# Three displaced circles exclude the universal vacuum-norm quadratic constant

Task: [T_F0011](../tasks/Yin_T_F0011_v1.md#contract).
Developed by the coordinating agent for Yin on 2026-10-16.
This is a complete candidate for independent review, not a refutation of the quadratic route with an unspecified finite constant.

## Current assessment
[Selected decision](#decision-reviewed-quadratic)

## Statement

Put r=1/10, c_0=0, c_1=1, c_2=i, and let mu_j be uniform probability on the circle z=c_j+r exp(i theta).
Let mu=(mu_0+mu_1+mu_2)/3, M=L-infinity(mu), tau(f)=integral f dmu, H=L2(mu), X(z)=z, and P=C[X,X*].
All inner products are linear in the second variable.
The three circles are disjoint and mu is diffuse.
The bounded normal X generates the finite tracial algebra M.
On the represented star algebra P, define the outer derivation
\[
 \delta f(z,w)=\frac{f(z)-f(w)}{z-w}.
\]
The product-null diagonal is immaterial.
Then this is an actual condition-A system: delta X=1 tensor 1 and 1 tensor 1 belongs to Dom delta*.
Writing xi=delta*(1 tensor 1), both one-sided actual adjoints equal
\[
 T(a)=\delta^*(a\otimes1)=\delta^*(1\otimes a),\qquad a\in P.
\]
The map T extends boundedly to H, and a bounded dual D on H establishes S for X.
Nevertheless there are elements a in P with
\[
 \boxed{\ \|Ta\|_2^2>\|\xi\|_2\|T(a^*a)\|_2
                  =\|\xi\|_2\|T(aa^*)\|_2.\ }
 \tag{S1}
\]
Consequently the individually optimal quadratic constants are strictly greater than norm(xi)_2 in this example.
Some finite constants do exist, so this does not refute either quadratic estimate with an unspecified constant, A implies S, or the scalar full-domain result.
It excludes the universal sharp vacuum-norm constant and the stronger domination using the fixed vector xi.

## Argument

### 1. Actual derivation, bounded contraction and vacuum

Each starred polynomial is Lipschitz on a compact rectangle surrounding the support, so its divided difference is bounded.
The formula is independent of the representative and satisfies the outer Leibniz rule and delta X=1 tensor 1.
Let E_0=(id tensor tau)delta on P.
Put p=1/3.
On each circle the same-circle part of E_0 is p times the translated radius-r circle operator.
By the exact Fourier calculation in [C_F0047 Section 2](Yin_C_F0047_v1.md#2-the-same-radius-calculation), the latter sends exp(i n theta) to r^{-1} exp(i(n-1)theta) for n>=1 and to zero for n<=0, so its H norm is 1/r.
The cross-circle part is multiplication by its row integral minus an integral operator with kernel (z-w)^{-1} between distinct circles.
Since |z-w|>=1-2r=4/5, each of these two terms has H norm at most 5/4.
For the integral term this follows directly from Cauchy-Schwarz on the probability product space, and for the multiplication term from its uniform row bound.
Thus E_0 has a bounded H extension E satisfying
\[
 \|E\|_{2\to2}\le\frac{10}{3}+\frac52=\frac{35}{6}<6.
 \tag{1}
\]
The first coefficient is p/r; the Hilbert direct sum of the three circle spaces takes the maximum of these equal norms.

The functional (tau tensor tau)delta f=tau(Ef) is L2 bounded.
Its actual Riesz vector is xi=E*1=delta*(1 tensor 1).
The same-circle formula and symmetrization of the cross-circle double integrals give, on the j-th circle,
\[
 \xi(c_j+r e^{i\theta})
 =\frac p r e^{i\theta}
    +2p\sum_{k\ne j}\frac1{\bar z-\bar c_k}.
 \tag{2}
\]
For the cross terms, averaging (z-w)^{-1} over a different circle yields (z-c_k)^{-1}, by its absolutely convergent geometric series.
The two appearances of f in the divided difference contribute equally after swapping z,w, which gives the factor 2.
The vector (2) is bounded and its norm is at most 6 by (1).

The divided difference is symmetric under swapping z,w.
Actual adjoint pairing therefore places both a tensor 1 and 1 tensor a in Dom delta* for all a in P and gives T=E* on P.
In particular T itself is Hilbert bounded with norm less than 6.
Expanding delta(bar a f), using the vacuum pairing and swapping the tensor factors gives
\[
 T(a)=a\xi-JEJa,\qquad Ja=\bar a,
 \tag{3}
\]
first on P and then on bounded functions by the bounded operators in (1), bounded multiplication by xi, and density.
The identity [E,X]=P_Omega follows from the Leibniz rule on P and extends to H by boundedness.
Hence D=-E has [X,D]=P_Omega on H and its adjoint also has domain H, proving S.

### 2. An explicit non-Hermitian vacuum pairing

Let h be the indicator of the circle centered at c_1=1.
For a function b constant with value b_j on each circle, (2)--(3) give
\[
 T(b)(z)=b_j\frac p r e^{i\theta}
       +p\sum_{k\ne j}\frac{b_j+b_k}{\bar z-\bar c_k},
 \qquad z=c_j+r e^{i\theta}.
 \tag{4}
\]
The within-circle derivative of b is zero, so (4) also follows by evaluating its cross-circle differences directly.
For k,l distinct from j, geometric-series integration gives
\[
 G_{jkl}:=\int\frac1{z-c_k}\frac1{\bar z-\bar c_l}\,d\mu_j(z)
 =\frac1{(c_j-c_k)(\bar c_j-\bar c_l)-r^2}.
 \tag{5}
\]
The series are absolutely convergent because each center separation exceeds r.
The positive angular self term in (2) is orthogonal to all nonpositive angular cross terms, as are the analogous mixed pairings with (4).
Put psi=<xi,T(h)>.
The same-circle terms are real.
The cross contribution from the circle centered at c_1 is real because it is a positive multiple of the squared norm of its full cross sum.
The only remaining imaginary terms come from the two other circles and equal
\[
 \begin{aligned}
 \operatorname{Im}\psi
 &=2p^3\operatorname{Im}(G_{0,2,1}+G_{2,0,1})\\
 &=\frac2{27}\left(-\frac{10000}{10001}
                         +\frac{10000}{19801}\right)\\
 &=-\frac{196000000}{5346804627}=:-s,
 \qquad s>\frac1{30}.
 \end{aligned}
 \tag{6}
\]
In particular b maps to <xi,T(b)> is not Hermitian even on this abelian algebra.

### 3. A strict violation and its original-core realization

Set t=1/1000 and a=1+i t h.
Since h is a projection, a*a=aa*=1+t^2 h.
The linear-second convention and (6) give
\[
 \|Ta\|_2^2
 =\|\xi\|_2^2+2st+t^2\|Th\|_2^2
 \ge\|\xi\|_2^2+2st.
 \tag{7}
\]
On the other hand, ||xi||2<=6 and ||Th||2<=6 by (1), so
\[
 \|\xi\|_2\|T(a^*a)\|_2
 \le\|\xi\|_2^2+t^2\|\xi\|_2\|Th\|_2
 \le\|\xi\|_2^2+36t^2.
 \tag{8}
\]
Because 2s>1/15>36/1000, (7) is strictly larger than (8).

The supports are disjoint compact sets, so h is the restriction of a smooth real cutoff on a rectangle containing them.
The already checked bivariate polynomial approximation interface in [C_F0055 Section 3](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) gives real starred polynomials h_n converging uniformly to h on the support.
Set a_n=1+i t h_n in P.
Then a_n converges uniformly to a and a_n*a_n=a_n a_n* converges uniformly to 1+t^2 h.
The bounded actual T sends these convergences to L2 convergence.
Thus the strict inequality persists for every sufficiently large n, proving S1 on the required original polynomial core.
The test in the larger continuous-function algebra is not substituted for that conclusion.

### 4. The exact scope of the obstruction

For any positive b in P, actual adjoint pairing gives
\[
 \tau(b)=\langle T(b),X-\tau(X)1\rangle.
\]
If sigma=||X-tau(X)1||2, it follows that
\[
 \|Ta\|_2^2\le\|T\|_{2\to2}^2\|a\|_2^2
 \le\sigma\|T\|_{2\to2}^2\|T(a^*a)\|_2.
 \tag{9}
\]
The same argument uses aa* for the right side.
This finite upper bound and the strict fixed-core violation show that the optimal constants are finite and strictly exceed ||xi||2.
In particular the stronger estimate ||Ta||2 squared <= Re<T(a*a),xi> is false as well, since its right side is at most the right side of S1.
A different fixed vector or a larger finite constant remains possible.
No inference concerning nonexistence of S is drawn; this example has bounded full-H duals.

## Source and checking scope

The mathematical inputs are the translated single-circle Fourier operator from C_F0047 and the polynomial approximation interface already checked in C_F0055.
The mixture vacuum, cross-circle kernels, exact rational imaginary part and strict polynomial-core violation are new calculations displayed here.
No assertion of novelty or priority is made.
The coordinating author checked the signs, series, three-circle weights, adjoint domains, strict gap and approximation passage; a separate fixed-material review is still required before acceptance.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-16T03:21 |
| status | open |
| reason | Complete explicit actual-A normal example excludes the vacuum-norm constant while retaining a finite quadratic constant and bounded full-H duals; fresh independent review pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact three-circle law, actual A and S, strict failure of the constant norm(xi), and existence of a larger finite constant. |
| argument | [Argument](#argument) | Bounded circle/cross decomposition, explicit vacuum and adjoint, rational imaginary pairing, strict gap and polynomial approximation. |
| dependency | [C_F0047 Section 2](Yin_C_F0047_v1.md#2-the-same-radius-calculation) | Exact same-circle Fourier contraction, translated and scaled. |
| dependency | [C_F0055 Section 3](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) | Uniform real bivariate polynomial approximation to the smooth cutoff on a compact rectangle. |

### Decision reviewed-quadratic

| Field | Value |
| --- | --- |
| date | 2026-10-16T03:32 |
| status | proved |
| reason | Adopt the entire fixed statement and argument after its separate whole-proof review, with all declared direct inputs resolved at the retained scopes. This result does not settle the unrestricted normal A-to-S question. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire fixed statement and its explicit positive or negative scope. |
| argument | [Argument](#argument) | Complete fixed argument, original-domain assertions and direct-input applications. |
| dependency | [C_F0047 Section 2](Yin_C_F0047_v1.md#2-the-same-radius-calculation) | Exact same-circle Fourier contraction, translated and scaled. |
| dependency | [C_F0055 Section 3](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests) | Uniform real bivariate polynomial approximation to the smooth cutoff on a compact rectangle. |
| review | [Independent whole-proof review](../audits/reviews/Yin_R_F0168_v1.md#conclusion) | Entire statement and argument with the exact direct dependencies and limits in the review bindings. |


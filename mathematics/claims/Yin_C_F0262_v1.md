---
author: Yin
---

# Marginal domination and the exact Hilbert norm of a Gaussian Markov coordinate slice

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(Z(z)=z\) have compact diffuse planar law \(\mu\), and put \(N=L^\infty(\mu)\).
Let \(P(z,y)>0\) almost everywhere be a symmetric measurable Markov density relative to \(\mu\), so \(\int P(z,y)\,d\mu(y)=1\) almost everywhere.
In the [one-channel Gaussian model](Yin_C_F0157_v2.md#bounded-coordinates-phase-and-generation), take the real coefficient \(a=\sqrt P\) and the selfadjoint field \(T=T_a\) over \(N\).
Write \(M=W^*(Z,T)\), \(\mathcal P=\mathbb C\langle Z,Z^*,T\rangle\) in its tracial representation, and \(\mathcal N_0=\mathbb C[Z,Z^*]\).
Assume the represented core has the distinguished coordinate derivation \(\delta_T\) with values \(1\otimes1\) on \(T\) and zero on \(Z,Z^*\).
In particular this holds under the [actual starred Gaussian criterion](Yin_C_F0209_v1.md#statement).
No hypothesis on a vacuum or a dual for the base coordinate enters the distinguished-slice calculation.
Put \(E_T=(\mathrm{id}\otimes\tau)\delta_T\), and allow the value \(+\infty\) in
\[
        H(z)=\int \frac{d\mu(y)}{P(z,y)},\qquad H_*=\operatorname*{ess\,sup}_z H(z).
\]

The following conditions are equivalent.

1. There are \(C<\infty\) and a probability density \(w\in L^1(W^*(T))_+\) such that
   \[
                 \|E_Tp\|_2^2\le C^2\tau(wp^*p) \qquad(p\in\mathcal P).
                 \tag{1}
   \]
2. Some such \(w,C\) satisfy (1) on just the single products \(p=uTv\) for all \(u,v\in\mathcal N_0\).
3. \(H_*<\infty\).
4. Inequality (1) holds on \(\mathcal P\) with \(w=1\).

The exact squared Hilbert-norm cost on the original mixed polynomial core is \(H_*\), including when the supremum is infinite.
For finite \(H_*\), the closure of \(E_T\) is a bounded operator on the entire \(L^2(M)\) with norm \(\sqrt{H_*}\).
More precisely, given any fixed marginal probability density \(w\), put \(s=\tau(wT^2)\).
Then \(0<s<4\), and the best squared constant for (1) on the single products of item 2 is
\[
                                 H_*-1+\frac1s .                           \tag{2}
\]
This formula concerns the single products for general \(w\) and the full core for \(w=1\).
In particular \(P\ge c>0\) suffices with full unweighted cost at most \(c^{-1/2}\).
There is a correlated actual starred ACSY pair satisfying the strong condition for which \(P\) has essential infimum zero and the exact full unweighted cost is \(\sqrt2\).

## Argument

### The terminal integral on the Gaussian paths

The row norm of \(a\) is one, hence \(T\) is bounded.
Positivity of \(a\) gives generation of the one-channel reference algebra \(M=W^*(N,S)\), where \(S\) is the free standard semicircular used to construct the field. [Field construction and generation](Yin_C_F0157_v2.md#bounded-coordinates-phase-and-generation)
In its [Gaussian path representation](Yin_C_F0209_v1.md#colored-paths-and-the-rank-obstruction), \(L^2(M)=\bigoplus_{n\ge0}H_n\), \(H_n=L^2(\mu^{n+1})\), and the vacuum \(\Omega=1\) belongs to \(H_0=L^2(\mu)\).
Left multiplication by \(u\in N\) multiplies the first variable by \(u(x_0)\).
Left multiplication by \(T\) is \(L+L^*\), where \(L\) creates a leading edge with coefficient \(a(x_0,x_1)\).
In positive degrees \(L^*\) integrates away the first variable with that coefficient, and \(L^*\) is zero in degree zero.

Assume \(H_*<\infty\).
Set \(D|_{H_0}=0\), and on every \(H_n\), \(n\ge1\), define
\[
       (DF)(x_0,\ldots,x_{n-1})
          =\int\frac{F(x_0,\ldots,x_{n-1},y)}{a(x_{n-1},y)}\,d\mu(y).
          \tag{3}
\]
Rowwise Cauchy–Schwarz bounds the norm on each degree by \(\sqrt{H_*}\).
Different degrees have orthogonal images, giving the same bound on their Hilbert direct sum.
On each \(H_{n-1}\) the adjoint of this degree map sends \(g\) to \(g(x_0,\ldots,x_{n-1})/a(x_{n-1},y)\).
Its squared norm at \(g\) is the integral of \(|g|^2 H(x_{n-1})\).
In particular testing row level sets in \(H_0\) gives the norm \(\sqrt{H_*}\) already on \(H_1\to H_0\).

The terminal integral commutes with every left base multiplier.
On \(H_n\) for \(n\ge1\), it commutes with \(L\) since the added leading edge stays in the output.
It commutes with \(L^*\) on every degree.
For \(n=0,1\) the two compositions with \(L^*\) vanish.
For \(n\ge2\) they integrate the leading and final variables in either order, even when the two edges have a common endpoint.
Indeed at fixed remaining variables the two coefficients are functions of separate integration variables with squared integrals \(1\) and \(H(x_{n-1})\).
This bounds the absolute double integral against the corresponding \(L^2\) section of \(F\) and justifies Fubini.
On \(H_0\) one has \(DLg=\int g\,d\mu\) by \(a/a=1\), while \(LDg=0\).
Consequently \([D,T]=P_\Omega\), where \(P_\Omega v=\Omega\langle\Omega,v\rangle\).
The outer Leibniz rule gives the same commutators for \(E_T\) on the original core, and both maps send \(1\) to zero.
Induction on words yields \(E_Tp=D(p\Omega)\) on \(\mathcal P\).
Since the original core is Hilbert dense, its closure is \(D\) and its operator norm is exactly the norm of (3).

### The conditional square of a single mixed product

Set \(A_n(x_0,\ldots,x_n)=\prod_{j=1}^na(x_{j-1},x_j)\) and \(A_0=1\).
Successive Markov integrations give \(\|A_n\|_2=1\), \(LA_n=A_{n+1}\), and \(L^*A_n=A_{n-1}\) for \(n\ge1\).
Thus \(U_n(T)\Omega=A_n\), where \(U_0=1,\ U_1(t)=t,\ U_{n+1}=tU_n-U_{n-1}\).
These orthonormal polynomial vectors span \(L^2(W^*(T))\) and \(T\) has the standard semicircular law by the [Markov path recurrence](Yin_C_F0259_v1.md#the-semicircular-marginal-and-the-conditional-square).
In particular \(0<s<4\) for every normal marginal probability density, since \(T^2\) has zero spectral mass at \(0\) and \(4\).

For \(u,v\in\mathcal N_0\) put \(p=uTv\) and \(Qv(z)=\int P(z,y)v(y)\,d\mu(y)\).
The square \(p^*p=\bar vT|u|^2T v\) has only degrees zero and two at the vacuum.
Its scalar expectation is \(A=\int |u|^2 Q(|v|^2)\,d\mu\).
Its two-edge path is \(\bar v(x)a(x,z)|u(z)|^2a(z,y)v(y)\).
Pairing this path against \(A_2\) gives \(B=\int |u|^2|Qv|^2\,d\mu\), by symmetry of \(P\).
Conditional expectation is the Hilbert projection onto the marginal polynomial vectors, whence
\[
           \mathbb E_{W^*(T)}(p^*p)=A1+B(T^2-1),\qquad 0\le B\le A .
           \tag{4}
\]
The last inequality uses Jensen's inequality for the probability row.
Equation (4) extends the projection-coefficient computation for indicator endpoints to complex polynomials.
Duality with the marginal \(L^1\) space, or pairing bounded truncations and passing to the limit, gives \(\tau(wp^*p)=A+(s-1)B\).
The original right slice on the single product is \(u\,\tau(v)\) by the generator values.

### Exact row testing on the original single products

For any \(D_0\ge0\), the squared domination bound with constant \(D_0\) on these products is equivalent to
\[
 \left|\int v\,d\mu\right|^2
    \le D_0\left(\int |v(y)|^2P(z,y)\,d\mu(y)
           +(s-1)\left|\int v(y)P(z,y)\,d\mu(y)\right|^2\right)
           \tag{5}
\]
for almost every row \(z\) and all \(v\in C(\operatorname{supp}\mu)\).
In fact (4) gives the integrated version against every \(|u(z)|^2\).
Uniform approximation of the square root of a nonnegative continuous test by base polynomials allows all such continuous tests, and hence gives (5) almost everywhere for each polynomial \(v\).
Take a common conull row set for the countable algebra with rational complex coefficients.
Its uniform density on the support and finiteness of the probability rows extend the inequality to every continuous \(v\) there.
The converse follows by integration.

Fix a good row, put \(\nu_z=P(z,\cdot)\mu\) and write \(m_v=\int v\,d\nu_z\).
The expression in parentheses in (5) is
\[
                  \|v-m_v\|_{L^2(\nu_z)}^2+s|m_v|^2 .
\]
It defines a norm equivalent, after taking the square root, to the usual probability-row Hilbert norm since \(s>0\).
The functional \(v\mapsto\int v\,d\mu\) is bounded in this norm exactly when \(h_z(y)=1/P(z,y)\) is in \(L^2(\nu_z)\).
Indeed continuous functions are dense, and any Hilbert representer in the usual row norm must have conjugate density \(d\mu/d\nu_z=h_z\) by equality of the finite measures on continuous tests.
Its usual squared norm is \(H(z)\) and its constant component is \(1\).
The squared dual norm for (5) is therefore \(\|h_z-1\|_{L^2(\nu_z)}^2+s^{-1}=H(z)-1+s^{-1}\), with value \(+\infty\) if the functional is unbounded.
Taking the row essential supremum proves (2).

Testing just these products forces \(H_*<\infty\) under any marginal probability density domination, whereas (3) gives \(w=1\) on the entire core whenever \(H_*<\infty\).
The full core contains the single products, so (2) at \(s=\tau(T^2)=1\) also gives an infinite unweighted core norm if \(H_*=\infty\).
This completes the equivalence and the norm computation.

### A correlated positive example without a uniform transition lower bound

Take normalized area measure on the unit disk, \(x(z)=\operatorname{Re}z\), and \(P(z,v)=1+x(z)x(v)\).
The kernel is symmetric and Markov because \(\int x\,d\mu=0\), with \(P>0\) almost everywhere.
Caps of positive area near the opposite real endpoints make its essential infimum zero.
The distribution of \(x\) has density \((2/\pi)\sqrt{1-t^2}\) on \([-1,1]\).
By its symmetry
\[
 H(z)=\frac{2}{\pi}\int_{-1}^1
                \frac{\sqrt{1-t^2}}{1-x(z)^2t^2}\,dt .
\]
This increases to \((2/\pi)\int_{-1}^1(1-t^2)^{-1/2}\,dt=2\) as \(|x(z)|\) increases to \(1\), so \(H_*=2\).
For the scalar coordinate the area density gives a uniform bound on \(\int |z-v|^{-1}\,d\mu(v)\) by integration over a disk of radius two.
The square-integrable conjugate variable follows by antisymmetrizing the scalar divided difference, as in the [area-law vacuum calculation](Yin_C_F0259_v1.md#a-markov-covariance-with-a-small-transition-probability).
The first integral in the Gaussian ACSY criterion is \(\int H\,d\mu\le2\).
Its second integrand is
\[
 \frac{|P(w,v)-P(z,w)|^2}{|z-v|^2 P(w,v)P(z,w)}
             \le\frac{1}{P(w,v)P(z,w)}
\]
because \(|x(w)|\le1\) and \(|x(v)-x(z)|\le |v-z|\).
Its integral is at most \(\int H(w)^2\,d\mu(w)\le4\).
The [one-channel case of the Gaussian criterion](Yin_C_F0209_v1.md#statement) gives actual starred ACSY and the strong domain condition for the pair.
Since \(\int x^2\,d\mu=1/4\), the field covariance gives \(\tau(xTxT)=\int x(z)x(v)P(z,v)\,d\mu^2=1/16\).
Freeness of the centered coordinates \(x,T\) would give zero.
The commutator \([Z,T]\) has one-edge coefficient \((z-v)a(z,v)\) of strictly positive norm.
The correlated pair thus realizes the full mixed-core norm \(\sqrt2\).

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T12:34 |
| status | open |
| reason | Fix the exact full Hilbert norm, the marginal-density criterion, the sharp single-product constants and the disk example for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Distinguished slice at the Markov Gaussian field, reciprocal row criterion, all mixed polynomials and single products, and a correlated example. |
| argument | [Argument](#argument) | Terminal integration commutator, marginal projection of the conditional square, exact row dual norms, and verification of both Gaussian vacuum integrals. |
| dependency | [Field construction and generation](Yin_C_F0157_v2.md#bounded-coordinates-phase-and-generation) | Markov row bound, leading creation and annihilation, and generation of the whole one-channel path space by the intrinsic pair. |
| dependency | [Gaussian paths](Yin_C_F0209_v1.md#colored-paths-and-the-rank-obstruction) | Wick-space inner product and actions of the field and endpoint base multipliers. |
| dependency | [Markov path recurrence](Yin_C_F0259_v1.md#the-semicircular-marginal-and-the-conditional-square) | Semicircular polynomial basis for the Markov field and the indicator-endpoint conditional-square calculation extended here. |
| dependency | [Area-law vacuum](Yin_C_F0259_v1.md#a-markov-covariance-with-a-small-transition-probability) | Scalar conjugate variable from the absolute Cauchy integral for the correlated example. |
| dependency | [Gaussian criterion](Yin_C_F0209_v1.md#statement) | Sufficient original derivation premise under actual ACSY and the two vacuum-integral checks yielding actual ACSY and the strong condition in the disk example. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T12:43 |
| status | proved |
| reason | Adopt the exact marginal domination criterion for Gaussian Markov fields and its original full Hilbert norm and single-product constants. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Distinguished slice at the Markov Gaussian field, reciprocal row criterion, all mixed polynomials and single products, and a correlated example. |
| argument | [Argument](#argument) | Terminal integration commutator, marginal projection of the conditional square, exact row dual norms, and verification of both Gaussian vacuum integrals. |
| dependency | [Field construction and generation](Yin_C_F0157_v2.md#bounded-coordinates-phase-and-generation) | Markov row bound, leading creation and annihilation, and generation of the whole one-channel path space by the intrinsic pair. |
| dependency | [Gaussian paths](Yin_C_F0209_v1.md#colored-paths-and-the-rank-obstruction) | Wick-space inner product and actions of the field and endpoint base multipliers. |
| dependency | [Markov path recurrence](Yin_C_F0259_v1.md#the-semicircular-marginal-and-the-conditional-square) | Semicircular polynomial basis for the Markov field and the indicator-endpoint conditional-square calculation extended here. |
| dependency | [Area-law vacuum](Yin_C_F0259_v1.md#a-markov-covariance-with-a-small-transition-probability) | Scalar conjugate variable from the absolute Cauchy integral for the correlated example. |
| dependency | [Gaussian criterion](Yin_C_F0209_v1.md#statement) | Sufficient original derivation premise under actual ACSY and the two vacuum-integral checks yielding actual ACSY and the strong condition in the disk example. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0271_v1.md#finding) | All four equivalent conditions, row duality, terminal commutator, the critical reciprocal bound and the correlated disk example. |

---
author: Yin
---

# A narrow cone of marginal secants controls the cubic integral over all omitted shifts

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(Z=X_i\) belong to a bounded normal generating tuple with actual starred conjugate variables in a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace.
Write \(N=W^*(X_j:j\ne i)\), \(\xi=\delta_i^*(1\otimes1)\), and \(\mu\) for the spectral law of \(Z\).
Its marginal phase is \(k(z,w)=(\bar z-\bar w)/(z-w)\) off the null diagonal.
Let \(F(s)=\sup_{b\in N}\tau(1_{[0,s]}(|Z-b|))\).
Suppose for some \(\lambda\) on the unit circle and \(0\le\varepsilon<4/\sqrt3-2\) one has
\[
                      |k(z,w)-\lambda|\le\varepsilon
                          \qquad(\mu^2\text{-almost everywhere}).
                                                                    \tag{1}
\]
Then
\[
                      \int_0^\infty F(s)^3\,\frac{ds}{s^3}
                                  \le C_\varepsilon\|\xi\|_2^2.       \tag{2}
\]
The constant is finite and depends only on the indicated upper bound \(\varepsilon\).
In particular all omitted shifts are allowed, including nonnormal shifts varying with radius.

A sufficient geometric condition is that the marginal, after a rotation and translation, is carried by the graph of a real Lipschitz function of one real variable with Lipschitz constant \(L\) satisfying
\[
                  \frac{2L}{\sqrt{1+L^2}}<\frac4{\sqrt3}-2.
\]
The function may be specified on a compact subset of the real line.
The estimate requires only (1) for the original marginal, independently of the geometry of the other coordinates.
It bounds the cubic obstruction; a bound on the full mixed column cost is a separate requirement for the universal normal implication.

## Argument

### Combining both resolvent tests at one radius

For an omitted shift \(b\) put \(Z-b=UP\), \(P=|Z-b|\).
Use the scalar functions \(h_s(v)=s^2/(v^2+s^2)\) and \(a_s(v)=sv/(v^2+s^2)\).
Write \(h=h_s(P)\), \(h'=UhU^*\), \(V=Ua_s(P)\), \(H=\tau(h)>0\), \(A=\tau(a_s(P))\), and \(m=\tau(V)\).
The [shifted resolvent graph](Yin_C_F0229_v1.md#argument) gives the unitary polar decomposition and the two derivative identities on the actual graph, with the original derivative represented in \(\mathcal B=M\bar\otimes M^{\rm op}\):
\[
 s\delta V=h'\otimes h^{\rm op}-(V\otimes V^{\rm op})k,\qquad
 s\delta h=-(h\otimes V^{\rm op})k - V^*\otimes h^{\rm op}.
\]
The second follows by differentiating the inverse of \(P^2+s^2\), as in the [two resolvent identities](Yin_C_F0269_v1.md#two-tensor-identities-off-the-collision-diagonal).
Use the decreasing rearrangement \(v_\xi\) of \(|\xi|\), \(H_\xi(t)=\int_0^t v_\xi(u)\,du\), and set
\[
       D(s)=\int_s^\infty H_\xi(F(t))\,dt/t^2,\qquad d_s=s\sqrt{D(s)} .
\]
Both \(|\langle\xi,V\rangle|\) and \(|\langle\xi,h\rangle|\) are at most \(sD(s)\) by the [rearrangement estimate](Yin_C_F0269_v1.md#simultaneous-choice-of-scales).
Trace the identities and replace \(k\) by \(\lambda 1\).
The product trace norm of \(V\otimes V^{\rm op}\) is \(A^2\), and that of \(h\otimes V^{\rm op}\) is \(HA\).
Thus (1), tracial duality and the vacuum identity give
\[
 \begin{aligned}
 H^2&\le \operatorname{Re}(\lambda m^2)+\varepsilon A^2+d_s^2,\\
 H|\lambda m+\bar m|&\le\varepsilon HA+d_s^2.
 \end{aligned}                                                        \tag{3}
\]
The first trace has positive leading term \(H^2\).
The plus sign in the second trace restricts the real part needed in the first.

Choose a unit square root of \(\lambda\).
For \(y=\sqrt\lambda\,m\), \(|\lambda m+\bar m|=2|\operatorname{Re}y|\), while \(\operatorname{Re}(\lambda m^2)\le(\operatorname{Re}y)^2\).
If \(H>d_s\), (3) therefore gives
\[
          H^2\le \tfrac14(\varepsilon A+d_s)^2+\varepsilon A^2+d_s^2 .
\]
Taking the Euclidean norm of the sum of \((\varepsilon A/2,\sqrt{\varepsilon}A,0)\) and \((d_s/2,0,d_s)\) shows that
\[
                  H-cA\le (\sqrt5/2)d_s,\qquad
                  c=\sqrt{\varepsilon+\varepsilon^2/4}.                 \tag{4}
\]
This also holds if \(H\le d_s\).
The restriction on \(\varepsilon\) needed in the remainder is just \(c<1/\sqrt3\).
Solving \(\varepsilon+\varepsilon^2/4<1/3\) gives the stated interval.

### Scale averaging and passage to the full envelope

For \(c<1/\sqrt3\) choose \(2/3<\beta<1\) with \(c\le\cot(\pi\beta/2)\).
For example one may take the midpoint of \(2/3\) and \((2/\pi)\operatorname{arccot}c\), with \(\operatorname{arccot}0=\pi/2\).
Apply the [positive scale average](Yin_C_F0261_v2.md#a-positive-scale-average-of-the-signed-resolvent-test) to (4), for each fixed \(b\) before taking the supremum.
More explicitly, integrating \(H(ru)-cA(ru)\) against \(u^{-\beta}du/u\) on \([1,\infty)\) integrates the one-variable kernel
\[
          K(t)=\int_1^\infty u^{-\beta}\frac{u^2-cut}{u^2+t^2}\frac{du}{u},
                   \qquad t=v/r .
\]
The cited calculation gives \(K(t)\ge(1-c)1_{[0,1]}(t)/(2\beta)\): its full Mellin integral has nonnegative sign when \(c\le\cot(\pi\beta/2)\), and its scale tail can omit only the negative part before the unique change of sign, or start wholly in the positive part.
Consequently
\[
 F(r)\le \frac{\sqrt5\,\beta}{1-c}
         \int_1^\infty u^{-\beta}ru\sqrt{D(ru)}\,\frac{du}{u}.
\]
For \(\eta>0\) put \(I_\eta=\int_\eta^\infty F(r)^3dr/r^3\) and \(J_\eta=\int_\eta^\infty H_\xi(F(r))^{3/2}dr/r^{3/2}\).
Both are finite for each \(\eta\).
Exactly the [truncated integral bounds](Yin_C_F0261_v2.md#closing-the-cubic-integral) applied to this inequality give
\[
 I_\eta^{1/3}\le
 \sqrt{3/2}\frac{\sqrt5\,\beta}{(1-c)(\beta-2/3)}J_\eta^{1/3},
 \qquad J_\eta\le3(2I_\eta/3)^{1/4}\sqrt2\,\|\xi\|_2^{3/2}.
\]
For \(I_\eta>0\), substitute, divide by \(I_\eta^{1/12}\) and take the fourth power.
The resulting bound is independent of \(\eta\), proving (2) by monotone convergence.
The zero case needs no division.

For \(z=x+if(x)\), each secant has slope \(u\) with \(|u|\le L\).
Its phase is \((1-iu)/(1+iu)\), whose distance to \(1\) is \(2|u|/\sqrt{1+u^2}\).
Rotating the graph multiplies all its phases by a single unit scalar, and translation preserves the phase.
This proves the graph assertion, including for nonsmooth functions.
The constants furnished here are sufficient; their optimality for the class of actual tuples is open.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T13:46 |
| status | open |
| reason | Fix a uniform cubic bound for all omitted shifts by testing both original resolvent blocks and absorbing the marginal secant variation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Uniform cubic concentration over the entire omitted algebra for near-collinear marginal secants and the small-Lipschitz-graph application. |
| argument | [Argument](#argument) | Pointwise elimination of the mean polar phase, positive scale averaging and the truncated nonlinear integral bound. |
| dependency | [Shifted resolvent graph](Yin_C_F0229_v1.md#argument) | Unitary polar decomposition and the original closed derivation on resolvent tests of arbitrary omitted shifts. |
| dependency | [Two resolvent identities](Yin_C_F0269_v1.md#two-tensor-identities-off-the-collision-diagonal) | Two exact operator derivatives including opposite multiplication and the sign on the diagonal block. |
| dependency | [Rearrangement bound](Yin_C_F0269_v1.md#simultaneous-choice-of-scales) | Uniform pairing estimate for both fixed-radius resolvent blocks against the actual vacuum. |
| dependency | [Positive scale average](Yin_C_F0261_v2.md#a-positive-scale-average-of-the-signed-resolvent-test) | Mellin kernel positivity and uniform cutoff lower bound for \(c<1/\sqrt3\). |
| dependency | [Truncated integral bounds](Yin_C_F0261_v2.md#closing-the-cubic-integral) | Two weighted Hardy bounds on every truncated interval for the same monotone envelope. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T14:01 |
| status | proved |
| reason | The independent review verifies the all-shifts estimate under the marginal secant cone and the stated graph application. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Uniform cubic concentration over the entire omitted algebra for near-collinear marginal secants and the small-Lipschitz-graph application. |
| argument | [Argument](#argument) | Pointwise elimination of the mean polar phase, positive scale averaging and the truncated nonlinear integral bound. |
| dependency | [Shifted resolvent graph](Yin_C_F0229_v1.md#argument) | Unitary polar decomposition and the original closed derivation on resolvent tests of arbitrary omitted shifts. |
| dependency | [Two resolvent identities](Yin_C_F0269_v1.md#two-tensor-identities-off-the-collision-diagonal) | Two exact operator derivatives including opposite multiplication and the sign on the diagonal block. |
| dependency | [Rearrangement bound](Yin_C_F0269_v1.md#simultaneous-choice-of-scales) | Uniform pairing estimate for both fixed-radius resolvent blocks against the actual vacuum. |
| dependency | [Positive scale average](Yin_C_F0261_v2.md#a-positive-scale-average-of-the-signed-resolvent-test) | Mellin kernel positivity and uniform cutoff lower bound for \(c<1/\sqrt3\). |
| dependency | [Truncated integral bounds](Yin_C_F0261_v2.md#closing-the-cubic-integral) | Two weighted Hardy bounds on every truncated interval for the same monotone envelope. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0281_v1.md#finding) | Both signed trace constraints, operator-norm perturbation, subcritical range and the Mellin and Hardy estimates. |

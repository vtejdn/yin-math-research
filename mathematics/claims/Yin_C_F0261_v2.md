---
author: Yin
---

# Cubic concentration at omitted shifts with positive radial phase below one third

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(Z=X_i\) be a coordinate of a bounded normal generating tuple with actual starred conjugate variables in a finite von Neumann algebra with faithful normal probability trace \(\tau\).
Write \(N=W^*(X_j:j\ne i)\) and \(\xi=\delta_i^*(1\otimes1)\).
For \(b\in N\), let \(Z-b=U_bP_b\) be its polar decomposition, let \(\mu_b\) be the law of \(P_b=|Z-b|\), and write \(m_b(v,w)\) for its [compressed marginal phase](Yin_C_F0229_v1.md#the-integrated-phase-defect).
Fix a family \(\mathcal G\subset N\) and set \(F(r)=\sup_{b\in\mathcal G}\mu_b([0,r])\), with empty supremum zero.
For \(a_s(v)=sv/(s^2+v^2)\), assume that a constant \(0\le\rho<1/3\) satisfies
\[
 \operatorname{Re}\iint a_s(v)a_s(w)m_b(v,w)\,d\mu_b(v)d\mu_b(w)
             \le \rho\left(\int a_s\,d\mu_b\right)^2
                         \qquad(s>0,\ b\in\mathcal G).                    \tag{1}
\]
Put \(c=\sqrt\rho\) and choose \(2/3<\beta<1\) with \(c\le\cot(\pi\beta/2)\).
Such a choice exists for every \(\rho<1/3\).
There is an absolute constant \(C\) such that
\[
 \int_0^\infty F(r)^3\,\frac{dr}{r^3}
     \le C\left(\frac{2\beta}{(1-c)(\beta-2/3)}\right)^4\|\xi\|_2^2 .    \tag{2}
\]
In particular shifts approaching the supremum may vary with the radius.
Under the actual tuple hypothesis alone, the [accretive-family conclusion of v1](Yin_C_F0261_v1.md#statement) also holds.
For \(\kappa\ge0\) and
\[
 F_\kappa(r)=\sup\{\mu_b([0,r]):b\in N,\ V,W\in\mathcal U(N),\
                              \operatorname{Re}(V^*(Z-b)W)\ge-\kappa r1\},
\]
one has \(\int_0^\infty F_\kappa(r)^3\,dr/r^3\le C(1+\kappa)^4\|\xi\|_2^2\).

The threshold in (1) is sharp for the abstract scalar radial vacuum identities.
At \(\rho=1/3\) there is a radial probability law \(\mu\), a constant phase \(m=1/3\), and a vector in \(L^2(\mu)\) representing the radial derivative functional (7) below on every \(C^1[0,1]\) profile, for which \(\int_0^1\mu([0,r])^3\,dr/r^3=\infty\).
Realization of these endpoint data as an actual omitted shift remains open.

## Argument

### A positive scale average of the signed resolvent test

For a fixed \(b\), write \(H_b(s)=\int h_s\,d\mu_b\), \(h_s(v)=s^2/(s^2+v^2)\), and \(A_b(s)=\int a_s\,d\mu_b\).
Let \(v_\xi\) be the decreasing rearrangement of \(|\xi|\) on \((0,1)\), \(H(t)=\int_0^t v_\xi(u)\,du\), and \(D(s)=\int_s^\infty H(F(x))\,dx/x^2\).
The [fixed-radius vacuum identity](Yin_C_F0261_v1.md#nonpositive-radial-phase-on-a-fixed-shift-family) expresses \(H_b(s)^2\) as the phase integral in (1) plus \(s^2\operatorname{Re}\langle\xi,U_bP_b(P_b^2+s^2)^{-1}\rangle\).
The norm of this last operator test is at most \(1/s\), and its singular mass above \(y>0\) is at most \(F(1/y)\), since \(v/(v^2+s^2)\le 1/v\) for \(v>0\) and is zero at \(v=0\).
Thus the [vacuum rearrangement bound](Yin_C_F0261_v1.md#testing-the-actual-vacuum-against-a-truncated-inverse) and (1) give
\[
            H_b(s)-c A_b(s)\le s\sqrt{D(s)} .                             \tag{3}
\]
The term on the left can have either sign before averaging.

Average (3) at \(s=ru\) against \(u^{-\beta}du/u\) on \([1,\infty)\).
The integral of its left side is absolutely convergent since \(h_s,a_s\) are bounded by one.
For \(v=rt,\ t>0\), the resulting one-particle kernel is
\[
 K(t)=\int_1^\infty u^{-\beta}\frac{u^2-cut}{u^2+t^2}\,\frac{du}{u}
     =t^{-\beta}\int_{1/t}^\infty
                        \frac{y^2-cy}{1+y^2}y^{-\beta}\,\frac{dy}{y}.    \tag{4}
\]
The integral on the whole positive half-line in the right expression equals
\[
            \frac{\pi}{2}\left(\csc(\pi\beta/2)-c\sec(\pi\beta/2)\right)
               \ge0 .
\]
Indeed \(x=y^2\) reduces its two terms to \(\tfrac12\int_0^\infty x^{p-1}(1+x)^{-1}dx\) with \(p=1-\beta/2,(1-\beta)/2\), respectively.
For \(0<p<1\), integrating \(z^{p-1}/(1+z)\) on a slit annulus with \(0<\arg z<2\pi\) gives \((1-e^{2\pi ip})\int_0^\infty x^{p-1}(1+x)^{-1}dx=2\pi i e^{i\pi(p-1)}\) from the pole at \(-1\), the outer and inner arc integrals tending to zero.
The full integral thus has the displayed value, with convergence at both endpoints.
The numerator \(y^2-cy\) is negative only for \(0<y<c\), so every upper tail in (4) has nonnegative integral.
If \(0<t\le1\), the first integrand before the weight has \((u^2-cut)/(u^2+t^2)\ge(1-c)/2\) for \(u\ge1\).
At \(t=0\) the original average equals \(1/\beta\).
Hence \(K(t)\ge (1-c)1_{[0,1]}(t)/(2\beta)\) throughout.
Fubini on the bounded left-side kernels now gives
\[
 F(r)\le\frac{2\beta}{1-c}\int_1^\infty
                  u^{-\beta}ru\sqrt{D(ru)}\,\frac{du}{u}.                \tag{5}
\]
Here the scale integration was performed for each shift before taking the supremum.
The right side is finite since \(D(s)\le\|\xi\|_2/s\) and \(\beta>1/2\).

### Closing the cubic integral

For \(\varepsilon>0\) set \(I_\varepsilon=\int_\varepsilon^\infty F(r)^3dr/r^3\), \(J_\varepsilon=\int_\varepsilon^\infty H(F(r))^{3/2}dr/r^{3/2}\).
Both are finite since the trace is a probability.
Writing
\[
     s^{2/3}D(s)=\int_1^\infty y^{-2/3}\,
                     \frac{H(F(sy))}{(sy)^{1/3}}\,\frac{dy}{y}
\]
and applying Minkowski on \([\varepsilon,\infty)\) with \(ds/s\) bounds the \(L^{3/2}\) norm by \((3/2)J_\varepsilon^{2/3}\).
It follows that \(s^{1/3}\sqrt{D(s)}\) has \(L^3\) norm at most \(\sqrt{3/2}J_\varepsilon^{1/3}\) there.
Multiply (5) by \(r^{-2/3}\) and apply Minkowski in this \(L^3\) space.
For each \(u\ge1\), changing variables to \(s=ru\) bounds the norm of \(r^{-2/3}ru\sqrt{D(ru)}\) by \(u^{2/3}\sqrt{3/2}J_\varepsilon^{1/3}\), since \(s\ge u\varepsilon\ge\varepsilon\).
Integration yields
\[
 I_\varepsilon^{1/3}\le
       \sqrt{3/2}\,\frac{2\beta}{(1-c)(\beta-2/3)}\,J_\varepsilon^{1/3}. \tag{6}
\]
The [layer and Hardy estimate of v1](Yin_C_F0261_v1.md#a-nonlinear-integral-estimate) applies to this nondecreasing \(F\) and \(v_\xi\), giving \(J_\varepsilon\le 3(2I_\varepsilon/3)^{1/4}\sqrt2\,\|\xi\|_2^{3/2}\).
For \(I_\varepsilon>0\), substitute this bound into (6), divide by \(I_\varepsilon^{1/12}\) and take the fourth power.
Monotone convergence gives (2), including the zero case.
The separate accretive-family estimate is exactly the [rotated resolvent argument of v1](Yin_C_F0261_v1.md#omitted-unitary-rotations-into-a-half-plane).

### Endpoint radial law

At \(\rho=1/3\), take \(d\mu(v)=\tfrac23 v^{-1/3}1_{(0,1)}(v)\,dv\) and constant compressed phase \(m=\rho\).
The real constant-phase radial trace functional used in the [radial power-law construction](../drafts/Yin_D_F0003.md#examples-with-a-strictly-positive-uniform-phase-defect) is
\[
 \mathcal L(\phi)=\tfrac12\iint
 \left[(1+\rho)\frac{\phi(v)-\phi(w)}{v-w}
       +(1-\rho)\frac{\phi(v)+\phi(w)}{v+w}\right]d\mu(v)d\mu(w).        \tag{7}
\]
The first quotient has its continuous diagonal value for \(\phi\in C^1[0,1]\).
The sum kernel is integrable since integration over \(0<w<v<1\) bounds its integral by a constant times \(\int_0^1v^{-2/3}dv\).
Define
\[
 \zeta(v)=-\frac23\int_1^\infty w^{-1/3}
              \left(\frac{1+\rho}{v-w}+\frac{1-\rho}{v+w}\right)dw .
\]
This vector belongs to \(L^2(\mu)\), since it is bounded on \(0<v\le1/2\) and is \(O(1+|\log(1-v)|)\) as \(v\uparrow1\).
To verify its pairing, cut the difference term to \(w/v\notin[(1+\eta)^{-1},1+\eta]\), a region invariant under exchanging \(v,w\).
At fixed \(\eta>0\), \(|v-w|^{-1}\le(2+\eta)/(\eta(v+w))\) there, so symmetrizing the two terms gives an integral of \(\phi(v)\) against the sum of the corresponding one-variable kernels.
In this sum extend the \(w\) integral to infinity and subtract its tail over \(w>1\).
With \(w=vu\) the full integral is \((2/3)v^{-1/3}\) times a scalar tending to zero.
Indeed, at \(\rho=1/3\), the scalar is \((4/3)\int u^{-1/3}/(1-u)\,du\) with the multiplicative cutoff plus \((2/3)\int u^{-1/3}/(1+u)\,du\) without a cutoff.
The latter integral before its coefficient equals \(2\pi/\sqrt3\) by the preceding slit integral at \(p=2/3\).
Inverting \(u\mapsto 1/u\) above one in the cutoff integral gives
\[
 \int_0^{1/(1+\eta)}\frac{u^{-1/3}-u^{-2/3}}{1-u}\,du
       \ \longrightarrow\ -3\int_0^1\frac{dt}{1+t+t^2}
       =-\frac{\pi}{\sqrt3},
\]
where \(u=t^3\).
These two scalar contributions cancel exactly, and their bounded cutoffs times \(v^{-1/3}\) are dominated in \(L^1(\mu)\).
The subtracted tail converges pointwise to \(-\zeta(v)\) and is bounded by a constant times \(1+|\log(1-v)|\), independently of the cutoff, by splitting \(w>1\) at \(2\).
The original cutoff difference quotient is bounded by \(\|\phi'\|_\infty\), so dominated convergence proves \(\mathcal L(\phi)=\int\phi(v)\zeta(v)\,d\mu(v)\), including for profiles with nonzero endpoint value.
Condition (1) holds with equality in this scalar model.
In particular for \(\phi(v)=v/(v^2+s^2)\) substitution in (7) gives \(s^2\mathcal L(\phi)=H_\mu(s)^2-\rho A_\mu(s)^2\), where \(H_\mu=\int h_s\,d\mu\) and \(A_\mu=\int a_s\,d\mu\) at that scale.
Its mass on \([0,r]\) equals \(r^{2/3}\) for \(0<r\le1\), giving the logarithmically divergent cubic integral.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T12:59 |
| status | open |
| reason | Extend the phase allowance to every value below one third, retain the accretive conclusion and identify the critical scalar obstruction. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Cubic concentration for the original accretive families and for a fixed family satisfying the integrated positive-phase allowance, with a scalar endpoint obstruction. |
| argument | [Argument](#argument) | Positive Mellin average before taking the supremum, truncated cubic integral, and exact radial vacuum at the critical power. |
| dependency | [Compressed phase](Yin_C_F0229_v1.md#the-integrated-phase-defect) | The actual marginal phase of a shifted polar decomposition. |
| dependency | [Fixed-radius vacuum identity](Yin_C_F0261_v1.md#nonpositive-radial-phase-on-a-fixed-shift-family) | Equality before applying a sign to the radial phase. |
| dependency | [Vacuum rearrangement](Yin_C_F0261_v1.md#testing-the-actual-vacuum-against-a-truncated-inverse) | Bound on the vacuum paired with the singular resolvent at each scale and shift. |
| dependency | [Nonlinear integral estimate](Yin_C_F0261_v1.md#a-nonlinear-integral-estimate) | Layer and Hardy estimate relating the two truncated norms. |
| dependency | [Accretive family](Yin_C_F0261_v1.md#omitted-unitary-rotations-into-a-half-plane) | Original two-sided unitary rotations, varying with the radius, and their cubic integral. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T13:06 |
| status | proved |
| reason | The independent review establishes the uniform subcritical estimate and proves sharpness for the abstract radial identities. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Cubic concentration for the original accretive families and for a fixed family satisfying the integrated positive-phase allowance, with a scalar endpoint obstruction. |
| argument | [Argument](#argument) | Positive Mellin average before taking the supremum, truncated cubic integral, and exact radial vacuum at the critical power. |
| dependency | [Compressed phase](Yin_C_F0229_v1.md#the-integrated-phase-defect) | The actual marginal phase of a shifted polar decomposition. |
| dependency | [Fixed-radius vacuum identity](Yin_C_F0261_v1.md#nonpositive-radial-phase-on-a-fixed-shift-family) | Equality before applying a sign to the radial phase. |
| dependency | [Vacuum rearrangement](Yin_C_F0261_v1.md#testing-the-actual-vacuum-against-a-truncated-inverse) | Bound on the vacuum paired with the singular resolvent at each scale and shift. |
| dependency | [Nonlinear integral estimate](Yin_C_F0261_v1.md#a-nonlinear-integral-estimate) | Layer and Hardy estimate relating the two truncated norms. |
| dependency | [Accretive family](Yin_C_F0261_v1.md#omitted-unitary-rotations-into-a-half-plane) | Original two-sided unitary rotations, varying with the radius, and their cubic integral. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0270_v2.md#finding) | All five direct interfaces, the truncated scale estimates, the accretive family and the endpoint distinction. |

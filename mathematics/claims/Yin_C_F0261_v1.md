---
author: Yin
---

# Cubic concentration integrals from vacuum tests at accretive and nonpositive-phase shifts

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(Z=X_i\) be a coordinate of a bounded normal generating tuple with actual starred conjugate variables in a finite von Neumann algebra with faithful normal probability trace.
Write \(N=W^*(X_j:j\ne i)\) and \(\xi=\delta_i^*(1\otimes1)\) for the coordinate vacuum.
For \(b\in N\) put \(P_b=|Z-b|\) and \(m_b(r)=\tau(1_{[0,r]}(P_b))\).
For any \(\kappa\ge0\), set
\[
 F_\kappa(r)=\sup\{m_b(r):b\in N,\ V,W\in\mathcal U(N),\
                      \operatorname{Re}(V^*(Z-b)W)\ge-\kappa r\,1\}.
\]
An empty supremum of masses is zero.
There is an absolute constant \(C\) for which
\[
              \int_0^\infty F_\kappa(r)^3\,\frac{dr}{r^3}
                         \le C(1+\kappa)^4\|\xi\|_2^2 .                  \tag{1}
\]
The admissible shifts and the two omitted unitaries may vary with the radius.

There is a second conclusion for any fixed family \(\mathcal G\subset N\).
For \(b\in\mathcal G\) write \(Z-b=U_b P_b\) and use the compressed marginal phase \(m(v,w)\) and singular law \(\mu_b\) from the [actual shifted resolvent identity](Yin_C_F0229_v1.md#the-integrated-phase-defect).
Assume, for every \(b\in\mathcal G\) and \(r>0\), that
\[
 \operatorname{Re}\iint a_r(v)a_r(w)m(v,w)\,d\mu_b(v)d\mu_b(w)\le0,
                       \qquad a_r(v)=\frac{rv}{v^2+r^2}.
\]
In particular pointwise nonpositive real compressed phase suffices.
For \(F_{\mathcal G}(r)=\sup_{b\in\mathcal G}m_b(r)\),
\[
              \int_0^\infty F_{\mathcal G}(r)^3\,\frac{dr}{r^3}
                       \le C\|\xi\|_2^2 .                                 \tag{2}
\]
Both results use only the actual vacuum of the given tuple.
They bound the [singular concentration test for finite column cost](Yin_C_F0258_v1.md#statement) on these families without a column bound or an \(L^p,\ p>2\), hypothesis.
Realizing divergence over all omitted shifts still requires other shifts.

## Argument

### A nonlinear integral estimate

Let \(F:(0,\infty)\to[0,1]\) be nondecreasing, let \(v\ge0\) be in \(L^2(0,1)\), and put \(H(t)=\int_0^t v(s)\,ds\).
Suppose
\[
       F(r)^2/r^2\le L\int_r^\infty H(F(x))\,\frac{dx}{x^2}
                                          \qquad(r>0).                    \tag{3}
\]
We show that \(I=\int_0^\infty F(r)^3\,dr/r^3\le C_0L^2\|v\|_2^2\) for an absolute constant.
For \(\varepsilon>0\) let \(I_\varepsilon\) be this integral restricted to \([\varepsilon,\infty)\) and set \(J_\varepsilon=\int_\varepsilon^\infty H(F(r))^{3/2}\,dr/r^{3/2}\).
Both are finite.
Multiply (3) by \(r^{2/3}\) and substitute \(x=ry\).
The resulting right side is \(L\int_1^\infty y^{-2/3}H(F(ry))/(ry)^{1/3}\,dy/y\).
Taking the \(L^{3/2}([\varepsilon,\infty),dr/r)\) norm, Minkowski's inequality and \(\int_1^\infty y^{-2/3}\,dy/y=3/2\) give
\[
                         I_\varepsilon^{2/3}\le (3L/2)J_\varepsilon^{2/3}.
\]
For \(0<t<1\) let \(Q_\varepsilon(t)=\inf\{r\ge\varepsilon:F(r)>t\}\) with empty infimum \(+\infty\).
Since each superlevel set is a terminal interval up to an endpoint, layer integration gives
\[
 I_\varepsilon=\frac32\int_0^1\frac{t^2}{Q_\varepsilon(t)^2}\,dt,\qquad
 J_\varepsilon=3\int_0^1\frac{\sqrt{H(t)}v(t)}{\sqrt{Q_\varepsilon(t)}}\,dt .
\]
Factor the integrand in the second formula as \((t^2/Q_\varepsilon(t)^2)^{1/4}\sqrt{H(t)/t}\,v(t)\).
The Hardy average \(A(t)=H(t)/t\) satisfies \(\|A\|_2\le2\|v\|_2\) by Minkowski applied to \(A(t)=\int_0^1v(ut)\,du\).
Hölder with exponents \(4,4,2\) therefore yields \(J_\varepsilon\le 3(2I_\varepsilon/3)^{1/4}\sqrt2\,\|v\|_2^{3/2}\).
If \(I_\varepsilon>0\), substitute this bound and divide by \(I_\varepsilon^{1/4}\) after raising the previous norm inequality to power \(3/2\).
It follows that \(I_\varepsilon\le C_0 L^2\|v\|_2^2\), also when \(I_\varepsilon=0\).
Monotone convergence gives the asserted estimate.

### Testing the actual vacuum against a truncated inverse

Take \(v\) to be the decreasing rearrangement of \(|\xi|\) and use the same \(H\).
For a contraction \(x\) with right support of trace at most \(m\), one has
\[
                             |\langle\xi,x\rangle|\le H(m).
\]
Indeed, writing \(\xi=U|\xi|\), for the projection \(e_y=1_{(y,\infty)}(|\xi|)\) one has
\(|\tau(e_yU^*x)|\le\min(\tau(e_y),\|x\|_1)\le\min(\tau(e_y),m)\) by the trace-norm bounds for either factor.
Integration over \(y\ge0\) gives \(H(m)\) by the scalar layer formula.
This remains valid for \(L^2\) vacuum vectors by truncation, since the trace is finite.
For a bounded operator \(K\) with \(\|K\|\le1/r\) and \(\tau(1_{(y,\infty)}(|K|))\le F(1/y)\) for \(0<y<1/r\), apply this contraction estimate to the polar partial isometry of \(K\) times each level projection of \(|K|\).
Layer integration and \(x=1/y\) give
\[
                    |\langle\xi,K\rangle|
                           \le \int_r^\infty H(F(x))\,\frac{dx}{x^2}.     \tag{4}
\]
This estimate allows the partial isometry to change at every test.

### Omitted unitary rotations into a half-plane

For an admissible test at \(r\) set \(D=V^*(Z-b)W,\ s=(2+3\kappa)r,\ g=2(1+\kappa)r,\ R=(D+s)^{-1}\), and \(q=\|R\|_2\).
The [accretive inverse and vacuum calculation](Yin_C_F0231_v1.md#the-inverse-in-the-closed-graph) gives
\[
       |\langle\xi,VRW^*\rangle|=|\tau R|^2\ge g^2q^4,\qquad
                          m_b(r)\le(s+r)^2q^2 .
\]
In particular \(m_b(r)^2/r^2\le (81/4)(1+\kappa)^2|\langle\xi,VRW^*\rangle|\).
The bound on the real part of \(D+s\) gives \(\|VRW^*\|\le1/g\le1/r\).
For \(y>0\) the trace mass of \(|VRW^*|\) above \(y\) is at most the singular mass of \(D+s\) up to \(1/y\), by trace invariance of the singular law under adjoint and multiplication by unitaries.
Since \(D+s=V^*(Z-b')W\) with \(b'=b-sVW^*\in N\) and \(\operatorname{Re}(D+s)\ge g1\), this mass is at most \(F_\kappa(1/y)\).
Thus (4) applies with \(F_\kappa\).
It is nondecreasing since both the cutoff interval and the class admitted by the half-plane condition increase with \(r\).
Taking the supremum over tests proves (3) with \(L=(81/4)(1+\kappa)^2\), giving (1).

### Nonpositive radial phase on a fixed shift family

For \(b\in\mathcal G\) write \(P=P_b,\ U=U_b\), and put \(h_r(v)=r^2/(v^2+r^2)\).
The [shifted resolvent differentiation](Yin_C_F0229_v1.md#argument) at squared radius \(r^2\), followed by the [polar phase pairing](Yin_C_F0229_v1.md#the-integrated-phase-defect), gives
\[
   \tau(h_r(P))^2=r\operatorname{Re}\langle\xi,U a_r(P)\rangle
       +\iint a_r(v)a_r(w)\operatorname{Re}m(v,w)\,d\mu_b(v)d\mu_b(w).
\]
This is the fixed-radius identity used in the [nonpositive-phase test](../drafts/Yin_D_F0006.md#nonpositive-compressed-phase).
Since \(h_r(v)\ge1/2\) for \(v\le r\), the assumed sign gives \(m_b(r)^2/r^2\le4|\langle\xi,K\rangle|\) for \(K=U P(P^2+r^2)^{-1}\).
Its singular values are given by \(v/(v^2+r^2)\le\min(1/r,1/v)\) on the law of \(P\), with the continuous value zero at \(v=0\).
Thus its mass above \(y>0\) is at most \(m_b(1/y)\le F_{\mathcal G}(1/y)\).
Holding \(\mathcal G\) fixed lets (4) use this same envelope at every threshold.
Taking the supremum over \(b\in\mathcal G\) in the vacuum estimate gives (3) with \(L=4\).
This proves (2).

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T12:29 |
| status | open |
| reason | Fix the endpoint concentration integral under the two actual vacuum tests and the nonlinear estimate that allows the shift to vary with scale. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Cubic integrability of the radius-wise accretive envelope and of the nonpositive-phase envelope on a fixed family, with only an actual square-integrable vacuum. |
| argument | [Argument](#argument) | Nonlinear Hardy estimate, singular rearrangement of a vacuum test, closure of the rotated family under the positive scalar shift and the signed phase calculation. |
| dependency | [Accretive resolvent](Yin_C_F0231_v1.md#the-inverse-in-the-closed-graph) | Actual identity and lower bounds at omitted-unitary rotations, including the mass and inverse norm at the indicated scale. |
| dependency | [Shifted graph calculus](Yin_C_F0229_v1.md#argument) | Differentiation of the shifted resolvent on the original closed graph and absence of singular kernel. |
| dependency | [Compressed phase](Yin_C_F0229_v1.md#the-integrated-phase-defect) | Conditional phase and exact trace pairing with both radial factors in the original algebra. |
| dependency | [Uniform concentration test](Yin_C_F0258_v1.md#statement) | Meaning of the cubic integral as a necessary condition for finite original column cost, used only to interpret the conclusion. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T12:33 |
| status | proved |
| reason | Adopt the cubic concentration estimates on both classes of omitted shifts from the actual square-integrable vacuum. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Cubic integrability of the radius-wise accretive envelope and of the nonpositive-phase envelope on a fixed family, with only an actual square-integrable vacuum. |
| argument | [Argument](#argument) | Nonlinear Hardy estimate, singular rearrangement of a vacuum test, closure of the rotated family under the positive scalar shift and the signed phase calculation. |
| dependency | [Accretive resolvent](Yin_C_F0231_v1.md#the-inverse-in-the-closed-graph) | Actual identity and lower bounds at omitted-unitary rotations, including the mass and inverse norm at the indicated scale. |
| dependency | [Shifted graph calculus](Yin_C_F0229_v1.md#argument) | Differentiation of the shifted resolvent on the original closed graph and absence of singular kernel. |
| dependency | [Compressed phase](Yin_C_F0229_v1.md#the-integrated-phase-defect) | Conditional phase and exact trace pairing with both radial factors in the original algebra. |
| dependency | [Uniform concentration test](Yin_C_F0258_v1.md#statement) | Meaning of the cubic integral as a necessary condition for finite original column cost, used only to interpret the conclusion. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0270_v1.md#finding) | Truncated Hardy estimate, singular-value trace pairing, all radius-dependent admissible rotations and the fixed nonpositive-phase family. |

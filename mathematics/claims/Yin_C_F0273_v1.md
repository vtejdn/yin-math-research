---
author: Yin
---

# Exceptional secant directions at a divergent singular concentration point

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(Z=X_i\) be a coordinate of a bounded normal tuple with actual starred conjugate variables in a finite von Neumann algebra with faithful normal probability trace.
Write \(N=W^*(X_j:j\ne i)\), \(K=\sigma(Z)\) and \(F(s)=\sup_{b\in\mathcal G}\tau(1_{[0,s]}(|Z-b|))\) for any fixed nonempty family \(\mathcal G\subset N\).
For \(z_0\in K\), let \(S(z_0)\) be the set of limiting phases of chords
\[
            k(z,w)=\frac{\bar z-\bar w}{z-w},
       \qquad z,w\in K,\quad z\ne w,\quad z,w\longrightarrow z_0 .
\]
Define \(e(z_0)=\min_{|\lambda|=1}\max_{\gamma\in S(z_0)}|\gamma-\lambda|\).
The set \(S(z_0)\) is nonempty and compact since the actual spectral law is diffuse and has support \(K\).
If \(\int_0^\infty F(s)^3\,ds/s^3=\infty\), the common point \(z_0\) of the two marginal spectral limits in the [concentration theorem](Yin_C_F0269_v1.md#statement) can be chosen to satisfy
\[
                   e(z_0)\ \ge\ \varepsilon_0,\qquad
            \varepsilon_0=2\left(\sqrt{1+24^{-2}}-1\right)>0 .         \tag{1}
\]
In particular, if each point of \(K\) has \(e(z)<\varepsilon_0\), the cubic integral is finite over **all** omitted shifts.
The secant directions and the neighborhood on which they are controlled may vary with the point.
This is a finiteness statement; it gives no numerical integral bound from that local condition alone.

For any fixed \(b\in N\) with \(\tau(1_{[0,s]}(|Z-b|))=s^{2/3}\) on \(0<s<1\), every common spectral limit point obtained along the concentrating sequence in the theorem must satisfy the stronger bound
\[
                            e(z_0)\ge 4/\sqrt3-2.                      \tag{2}
\]
This applies to a hypothetical actual realization of the critical radial model.
It uses only the singular law at the specified shift.

## Argument

### Concentration of the complex measures in total variation away from the point

Write \(Z-b=UP\), \(h=h_s(P)=s^2/(P^2+s^2)\), \(V=Ua\), \(a=a_s(P)=sP/(P^2+s^2)\), \(H=\tau(h)\), \(A=\tau(a)\), and \(h'=UhU^*\).
Take the original [simultaneous scale selection](Yin_C_F0269_v1.md#simultaneous-choice-of-scales) with the estimates \(H\ge F(s)/4\), \(J(s)\le6 F(s)\), \(J(s)=\int_1^\infty F(su)du/u^2\).
We can simultaneously obtain for any fixed \(2/3<\alpha<1\) a constant \(C_\alpha\) such that along this sequence
\[
                J(2^j s)\le C_\alpha 2^{\alpha j}F(s)
                              \qquad(j\ge0).                           \tag{3}
\]
Indeed, in the original probability proportional to \(F(s)^3ds/s^3\) on \([\eta,\infty)\), the third moment of \(J(2^j s)/F(s)\) is at most \(27\,2^{2j}\).
This follows by dilation of the \(L^3\) bound on \(s^{-2/3}J(s)\) there.
Ratios at \(F=0\) may be set equal to zero.
The probability of any failure of (3) is at most \(27 C_\alpha^{-3}\sum_{j\ge0}2^{(2-3\alpha)j}\), less than \(1/8\) for a suitable constant.
The original \(j=0\) condition \(J(s)\le6F(s)\) costs at most \(1/8\) and the size and finitely many adjoint-test conditions cost less than \(1/2\) for sufficiently small \(\eta\).
Therefore all can be imposed at once.
Pass to a decreasing subsequence with the asserted common point.
The original bound \(A/H\le24\) is retained.

For a neighborhood \(O\) of \(z_0\) let \(p=1_{K\setminus O}(Z)\).
Both \(\tau(ph)/H\) and \(\tau(ph')/H\) tend to zero by concentration.
For \(v\le2^m s\) one has \(a_s(v)\le2^mh_s(v)\), and for \(v>2^m s\) one has \(a_s(v)\le s/v\).
Splitting the tail into dyadic intervals gives
\[
    \frac{\tau(a1_{\{P>2^m s\}})}{H}
       \le \frac1H\sum_{j\ge m}2^{-j} F(2^{j+1}s)
       \le 4 C_\alpha 2^\alpha\sum_{j\ge m}2^{-(1-\alpha)j}.
\]
Here \(F\le J\) by monotonicity.
The conjugated tail has the same trace.
Take the limit along the sequence for fixed \(m\), followed by \(m\to\infty\), to obtain
\[
             \tau(pa)/H,\quad\tau(pUaU^*)/H\ \longrightarrow0.
\]
Let \(G(c)=\tau(c(Z)V)/H\), \(R(c)=\tau(c(Z)h)/H\) and \(L(c)=\tau(c(Z)h')/H\).
In particular \(|G|(K\setminus O)\to0\).
Indeed, for each marginal contraction \(c=pc\) the pairing with \(V\) is the trace against the two Hilbert vectors \(\sqrt a,U\sqrt a\), and its absolute value divided by \(H\) is at most \((\tau(pa)\tau(pUaU^*))^{1/2}/H\).
Taking the supremum gives the asserted variation bound.
This step is also valid in the singleton power-law case on any concentrating sequence from the original theorem, without the additional selection (3): \(F(t)=\min(t^{2/3},1)\) gives \(J(2^j s)\le3\,2^{2j/3}F(s)\) for \(s\le1\).

### The two scalar trace inequalities in a local cone

Choose any \(\epsilon>e(z_0)\), and choose \(|\lambda|=1\) attaining the minimum in the definition of \(e(z_0)\).
There is a neighborhood \(O\) of \(z_0\) with \(|k(z,w)-\lambda|\le\epsilon\) throughout its off-diagonal spectral square.
Otherwise there would be pairs tending to \(z_0\) and, by compactness of the unit circle, an accumulation phase contradicting \(\epsilon>e(z_0)\).
At each scale the leg measures are absolutely continuous with respect to the diffuse marginal law, so the collision diagonal is null before passage to the limit.
The two products \(G\otimes G\) and \(R\otimes G\) have total variation tending to zero outside \(O^2\), since the individual variations are bounded uniformly and concentrate in \(O\).
Thus integrating \(k-\lambda\) against the first product costs at most \(\epsilon(A/H)^2+o(1)\) and against the second at most \(\epsilon A/H+o(1)\).
This compares the two kernels on the original measures at each scale, without assigning a limiting diagonal phase.

The [two resolvent identities](Yin_C_F0269_v1.md#two-tensor-identities-off-the-collision-diagonal), tested against the unit, show
\[
       1-\int k\,d(G\otimes G)\to0,\qquad
       \int k\,d(R\otimes G)+\overline{G(1)}\to0 .
\]
Here the terms involving the actual vacuum vanish by the simultaneous scale selection with the unit tensor adjoint included.
Take a subsequence with \(A/H\to B\le24\) and \(G(1)\to q\).
Since \(R(1)=1\), the local cone bounds give
\[
       1\le \operatorname{Re}(\lambda q^2)+\epsilon B^2,\qquad
       |\lambda q+\bar q|\le\epsilon B .
\]
The [two-trace phase calculation](Yin_C_F0272_v1.md#combining-both-resolvent-tests-at-one-radius) or the identity \(|\lambda q+\bar q|=2|\operatorname{Re}(\sqrt\lambda q)|\) gives \(1\le (\epsilon+\epsilon^2/4)B^2\).
Let \(\epsilon\downarrow e(z_0)\).
Using \(B\le24\) proves (1).

For the singleton critical law the density on \((0,1)\) is \(\tfrac23 v^{-1/3}\).
Substitute \(v=su\) in \(H,A\), so their ratio tends by monotone convergence in the two positive integrals to
\[
    \frac{\int_0^\infty u^{2/3}/(1+u^2)\,du}
         {\int_0^\infty u^{-1/3}/(1+u^2)\,du}
              =\frac{\csc(5\pi/6)}{\csc(\pi/3)}=\sqrt3 .
\]
The beta integrals are evaluated by \(x=u^2\) as in the [Mellin calculation](Yin_C_F0261_v2.md#a-positive-scale-average-of-the-signed-resolvent-test).
Using \(B=\sqrt3\) yields (2).
For example a marginal with a single limiting chord direction at each point has \(e=0\) everywhere, so these endpoint obstructions do not occur there.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T13:48 |
| status | open |
| reason | Fix the quantitative local secant obstruction to any divergent cubic envelope and its stronger critical-law constant. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Necessary angular spread at a common spectral concentration point in general and for the critical power law. |
| argument | [Argument](#argument) | Simultaneous dyadic tails, total variation localization, two original trace identities on a local spectral square and the endpoint ratio. |
| dependency | [Fixed-shift or varying-shift concentration](Yin_C_F0269_v1.md#statement) | Extraction of a common limiting spectral point for left and right weights. |
| dependency | [Original scale selection](Yin_C_F0269_v1.md#simultaneous-choice-of-scales) | Truncated \(L^3\) control of \(J\), uniform adjoint limits and the normalized polar mass bound. |
| dependency | [Two original resolvent identities](Yin_C_F0269_v1.md#two-tensor-identities-off-the-collision-diagonal) | Measures paired with the unimodular marginal phase on the original soft weights. |
| dependency | [Trace elimination](Yin_C_F0272_v1.md#combining-both-resolvent-tests-at-one-radius) | The real-part constraint from the sum of the complex mean and its conjugate. |
| dependency | [Mellin integral](Yin_C_F0261_v2.md#a-positive-scale-average-of-the-signed-resolvent-test) | Evaluation of both beta integrals with the indicated positive exponents. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T14:05 |
| status | proved |
| reason | The independent review verifies quantitative local angular spread at the concentrating point and the stronger constant for the critical singular law. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Necessary angular spread at a common spectral concentration point in general and for the critical power law. |
| argument | [Argument](#argument) | Simultaneous dyadic tails, total variation localization, two original trace identities on a local spectral square and the endpoint ratio. |
| dependency | [Fixed-shift or varying-shift concentration](Yin_C_F0269_v1.md#statement) | Extraction of a common limiting spectral point for left and right weights. |
| dependency | [Original scale selection](Yin_C_F0269_v1.md#simultaneous-choice-of-scales) | Truncated \(L^3\) control of \(J\), uniform adjoint limits and the normalized polar mass bound. |
| dependency | [Two original resolvent identities](Yin_C_F0269_v1.md#two-tensor-identities-off-the-collision-diagonal) | Measures paired with the unimodular marginal phase on the original soft weights. |
| dependency | [Trace elimination](Yin_C_F0272_v1.md#combining-both-resolvent-tests-at-one-radius) | The real-part constraint from the sum of the complex mean and its conjugate. |
| dependency | [Mellin integral](Yin_C_F0261_v2.md#a-positive-scale-average-of-the-signed-resolvent-test) | Evaluation of both beta integrals with the indicated positive exponents. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0282_v1.md#finding) | Scale selection and dyadic tails, concentration in total variation, both trace limits and the endpoint Mellin ratio. |

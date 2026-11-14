---
author: Yin
---

# Dominating weights for the right slice of a scalar normal coordinate

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(\mu\) be a compactly supported planar probability such that the normal coordinate \(Z(z)=z\) has an actual conjugate variable \(\xi=\delta^*(1\otimes1)\) on the represented starred polynomial algebra \(P=\mathbb C[Z,Z^*]\).
Put \(E=(\mathrm{id}\otimes\tau)\delta\) on \(P\) and \(T=E^*|_P\) on \(L^2(\mu)\), with inner product linear in the second variable.
Let \(\kappa\) be the reciprocal circumradius, taken to be zero for repeated or collinear triples.
Define
\[
 \theta(z)=\lim_{r\downarrow0}\frac{\mu(B(z,r))}{2r},\qquad
 g(z,w)=\int\kappa(z,w,v)^2\,d\mu(v),\qquad
 d_0=\tfrac14|\xi|^2+\pi^2\theta^2,\qquad
 W(z)=d_0(z)+\tfrac12\int g(z,w)\,d\mu(w).
\]
These functions exist almost everywhere with \(g\in L^1(\mu^2)_+\) and \(W\in L^1(\mu)_+\).
Every real \(f\in P\) satisfies
\[
 \begin{aligned}
  \operatorname{Re}\langle\xi,Tf\rangle&=\int fW\,d\mu,\qquad \int W\,d\mu=\|\xi\|_2^2,\\
  \|Tf\|_2^2&=\int d_0 f^2\,d\mu+
       \tfrac12\iint g(z,w)f(z)f(w)\,d\mu(z)d\mu(w)\\
  &=\int W f^2\,d\mu-
       \tfrac14\iint g(z,w)(f(z)-f(w))^2\,d\mu(z)d\mu(w).
 \end{aligned}                                                        \tag{1}
\]
Every complex \(p\in P\) satisfies
\[
       \|Tp\|_2\le\sqrt2\,\|p\|_{L^2(W\mu)},\qquad
       \|Ep\|_2\le(2+\sqrt2)\|p\|_{L^2(W\mu)} .                        \tag{2}
\]

More generally, a nonnegative \(d\in L^1(\mu)\) admits a finite \(C\) in
\[
                 \|Ep\|_2^2\le C^2\int|p|^2 d\,d\mu \quad(p\in P)       \tag{3}
\]
exactly when both of the following conditions hold for finite \(A,K\).
\[
 \begin{aligned}
    d_0&\le A d\quad\mu\text{-almost everywhere},\\
    \iint g(z,w)f(z)f(w)\,d\mu(z)d\mu(w)
       &\le K\int d f^2\,d\mu\quad(0\le f\in L^\infty(\mu)).
 \end{aligned}                                                         \tag{4}
\]
Condition (3) gives \(A=C^2\) and \(K=18C^2\).
Thus on any straight line precisely the weights \(d\) with \(d_0\le A d\) satisfy (3).
On the unit disk with normalized area measure one has \(d_0(z)=|z|^2\), yet every \(d\) satisfying (3) obeys
\[
        C^2\int_{|z|<r}d\,d\mu \ \ge\ 2r^4\log(1/r)\qquad(0<r<1).       \tag{5}
\]
In particular \(d_0\) alone fails there.

For a coordinate \(X_i\) of an arbitrary actual normal tuple in a finite tracial algebra, the marginal \(\mu\) and its scalar vacuum determine \(d_0,g\) as above.
If \(D\in L^1(M)_+\) dominates the mixed right slice on the original starred polynomials with constant \(C\) as in (3) with \(\tau(Dp^*p)\), its compression \(\mathbb E_{W^*(X_i)}D\) satisfies both bounds in (4) for this marginal.

## Argument

### Hard Cauchy transforms and the original core

The [scalar geometric criterion](Yin_C_F0255_v1.md#statement) gives diffuseness, \(g\in L^1(\mu^2)\), and \(\int(M_1\mu)^2d\mu<\infty\), where \(M_1\mu(z)=\sup_r\mu(B(z,r))/r\).
We use the [exact Tolsa–Verdera formula with arclength density](../audits/literature/TV06/Yin_U002.md#tv06-u002).
For bounded real \(f\), the finite positive measures \(\lambda_s=(1+s f)\mu\) are comparable to \(\mu\) whenever \(|s|\|f\|_\infty<1\).
Each has finite curvature and finite squared maximal-density integral by domination of its three factors by a constant times \(\mu\).
Its arclength density equals \((1+s f)\theta\) almost everywhere, by differentiation of \(f\) with respect to the finite planar measure \(\mu\) on balls.
Here the ball differentiation theorem for finite Borel measures on Euclidean space applies also to bounded Borel functions.

Use the conjugated Cauchy kernel \(k(z,w)=1/(\bar z-\bar w)\).
Let \(C_\epsilon f=\int_{|z-w|>\epsilon}k(z,w)f(w)\,d\mu(w)\).
For \(f=1\), the source yields a strong \(L^2(\mu)\) limit \(B\).
For real bounded \(f\), subtract the strong transforms of \(\lambda_s\) and \(\mu\) at one nonzero admissible \(s\), and divide by \(s\).
Comparability of the measures lets both converge in \(L^2(\mu)\).
This gives \(C_\epsilon f\to C f\) strongly, with the same principal-value formula almost everywhere.
Splitting a bounded complex \(f\) into its real and imaginary parts extends the convergence to that \(f\).

For \(p\in P\) the quotient \((p(z)-p(w))/(z-w)\) is bounded on the compact support off the null diagonal.
The marginal divided difference is the actual derivative on this core and the scalar adjoint is \(Tp=p\xi-JEJp\), where \(Jp=\bar p\). [Original scalar adjoint formula](Yin_C_F0162_v1.md#1-actual-scalar-operators-and-orientation)
Integrating the quotient over \(|z-w|>\epsilon\) in both variables and interchanging them gives \(\langle 2C_\epsilon1,p\rangle\).
Passing to the limit gives \(2B=\xi\).
Likewise \(JEJp=pB-Cp\) by integrating the difference in the conjugate orientation.
Consequently \(Tp=pB+Cp\).
Use these last two formulas to denote the transforms \(L(f)=fB-Cf\) and \(T(f)=fB+Cf\) on bounded Borel inputs, and put \(E(f)=JLJf\).
They agree with the specified original operators on \(P\).

### Polarizing the exact energy

Write \(\int_2\) and \(\int_3\) for integration against \(\mu^2\) and \(\mu^3\), respectively.
For every sufficiently small real \(s\) and real bounded \(f\), the norm identity reads
\[
 \int|B+sCf|^2(1+s f)\,d\mu
 =\frac{\pi^2}{3}\int\theta^2(1+s f)^3d\mu
  +\frac16\int_3\kappa^2\prod_{u\in\{z,w,v\}}(1+s f(u)).
\]
The last product uses all three arguments, and the repeated-point set is null.
All coefficients are integrable.
Equating coefficients of \(s\) gives
\[
 \int f|B|^2\,d\mu+2\operatorname{Re}\langle B,Cf\rangle
 = \pi^2\int f\theta^2\,d\mu+\tfrac12\int_2 g(z,w)f(z).
\]
Since \(\xi=2B\) and \(Tf=fB+Cf\), this gives the first identity of (1), including its mass at \(f=1\).
Equating coefficients of \(s^2\) gives
\[
 \|Cf\|_2^2+2\operatorname{Re}\langle fB,Cf\rangle
 = \pi^2\int\theta^2 f^2\,d\mu+\tfrac12\int_2 g(z,w) f(z) f(w).
\]
Adding \(\|fB\|_2^2\) gives the second line of (1).
Symmetry of \(g\) gives its third line.
This proves (1) for every bounded real input of these transforms.
For complex \(p=f+ih\), the sum of the real estimates and \(\|Tf+iTh\|^2\le2(\|Tf\|^2+\|Th\|^2)\) give the first bound in (2).
The second follows from \(L(p)=p\xi-Tp\), \(|\xi|^2\le4W\), and conjugation.
These bounds apply to every bounded Borel input of the formulas.

### Localizing the multiplier part

Assume (3).
The represented starred polynomials are dense in \(L^2((1+d+W)\mu)\), by uniform density in the continuous functions on the compact support and density of continuous functions for this finite Borel measure.
By (2) the estimates therefore extend (3) to all bounded Borel inputs, with exactly the transform \(E(f)\) just defined.

Partition the compact support by half-open mesh squares \(Q\) of side \(2^{-n}\) and set \(f_Q=f1_Q\) for a bounded real \(f\).
Only finitely many squares at each scale are needed.
The second line of (1) gives
\[
        \lim_{n\to\infty}\sum_Q\|T(f_Q)\|_2^2=\int d_0 f^2\,d\mu .      \tag{6}
\]
Indeed the summed kernel term contains the indicator that \(z,w\) belong to the same square.
It tends to zero off the null diagonal and is bounded in absolute value by \(\|f\|_\infty^2 g\).

For each Lipschitz \(\psi\) on the support, antisymmetry of the hard kernel gives
\[
 \sum_Q\langle f_Q\psi,C_\epsilon f_Q\rangle
  =\tfrac12\int_2 1_{\mathrm{same}\ Q}1_{|z-w|>\epsilon}
       f(z)f(w)(\bar\psi(z)-\bar\psi(w))k(z,w).
\]
The kernel multiplied by the difference of \(\psi\) is bounded by its Lipschitz constant.
At fixed mesh the strong cutoff limits remove \(\epsilon\), and dominated convergence as the mesh shrinks sends the expression to zero.
Real (1) and \(Cf_Q=T(f_Q)-f_Q B\) give
\[
  \left(\sum_Q\|Cf_Q\|_2^2\right)^{1/2}
  \le\left(\int W f^2\,d\mu\right)^{1/2}
      +\left(\int|B|^2 f^2\,d\mu\right)^{1/2}
\]
uniformly in the mesh.
Approximate \(B\) in \(L^2(\mu)\) by Lipschitz \(\psi\), possible by polynomial density.
The error in the summed pairing is at most \(\|f\|_\infty\|B-\psi\|_2(\sum_Q\|Cf_Q\|_2^2)^{1/2}\).
Thus \(\sum_Q\langle f_Q B,C f_Q\rangle\to0\).
For real \(f_Q\), \(\|E(f_Q)\|_2^2-\|T(f_Q)\|_2^2=-4\operatorname{Re}\langle f_Q B,Cf_Q\rangle\).
Summing (3) and taking the limit in (6) now gives \(\int d_0 f^2d\mu\le C^2\int d f^2d\mu\).
Indicators prove the first part of (4).

### The remaining curvature condition

For bounded real \(f\), the just-proved multiplier bound gives \(\|f\xi\|_2\le 2C\|f\|_{L^2(\mu_d)}\), where \(d\mu_d=d\,d\mu\).
Since \(Tf=f\xi-JEJf\), (3) gives \(\|Tf\|_2\le3C\|f\|_{L^2(\mu_d)}\).
Insert this in the second line of (1) and drop \(\int d_0f^2d\mu\) to get the required kernel bound with \(K=18C^2\).

Conversely, because \(g\ge0\) pointwise, the absolute value of its quadratic form at a bounded real \(f\) is bounded by that form at \(|f|\).
The two conditions (4) thus give \(\|Tf\|_2^2\le(A+K/2)\|f\|_{L^2(\mu_d)}^2\).
The real and imaginary parts of a complex \(p\) yield the factor-two squared bound for \(T(p)\).
Using \(p\xi-Tp=L(p)\) and conjugation gives (3) with \(C=2\sqrt A+\sqrt{2A+K}\).
Summation of (3) on finite columns gives domination by the same density and constant.
When the support lies on a straight line \(g=0\), so only the multiplier condition remains.
When \(\mu\) is the marginal of an actual normal tuple, the forced divided difference restricted to pure starred polynomials has both legs in that marginal and the mixed right slice there equals \(E\). [Marginal derivative of an actual normal tuple](Yin_C_F0076_v1.md#statement)
The trace-preserving conditional expectation identifies \(\tau(Dp^*p)\) with the corresponding marginal weight on these inputs, proving the compression assertion.

### A disk with vanishing one-dimensional density

Let \(d\mu=dA/\pi\) on \(|z|<1\), where \(dA\) is ordinary area.
The kernel \(1/|z-w|\) is absolutely integrable in either variable uniformly on the disk, by polar integration over a disk of radius two.
Antisymmetrizing its integral against the polynomial divided difference gives the actual vacuum with \(\xi(z)=2B(z)\).
For \(|z|<1\) the unbarred Cauchy transform is \(\bar z\).
Indeed the angular average of \(1/(z-se^{it})\) is \(1/z\) for \(s<|z|\) and zero for \(s>|z|\) by the geometric series, giving \(|z|^2/z\) after radial integration.
The value at zero vanishes by symmetry.
Thus \(B(z)=z\), \(\theta=0\), and \(d_0=|z|^2\).
For \(q_r=1_{\{|z|<r\}}\) the same angular calculation gives \(E(q_r)(z)=-r^2/z\) on \(r<|z|<1\).
Its squared norm on that annulus is \(2r^4\log(1/r)\).
The extension of (3) to bounded inputs gives (5).
Since \(\int_{|z|<r}|z|^2d\mu=r^4/2\), \(d_0\) cannot dominate the slice on this law.
The marginal itself has both bounded-vector domains by the scalar geometric criterion.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T13:14 |
| status | open |
| reason | Fix the scalar curvature identity, exact two-condition weight characterization and planar disk obstruction for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Explicit weight and exact real adjoint energy, complete criterion on scalar weights, disk lower bound and necessary marginal compression of a mixed weight. |
| argument | [Argument](#argument) | Principal values for real and complex inputs, cubic polarization with normalized density, fine-partition recovery of the multiplier, positive-kernel domination, and disk indicator tests. |
| dependency | [Geometric scalar criterion](Yin_C_F0255_v1.md#statement) | Actual vacua give the two geometric energy inputs, diffuseness and the scalar bounded-vector domains. |
| dependency | [Tolsa–Verdera energy and normalization](../audits/literature/TV06/Yin_U002.md#tv06-u002) | Strong hard cutoff convergence and the curvature and ordinary arclength density terms with their exact coefficients for positive finite reweightings. |
| dependency | [Scalar adjoint formula](Yin_C_F0162_v1.md#1-actual-scalar-operators-and-orientation) | Identification on the original polynomial core of the actual adjoint with the vacuum multiplier minus the conjugated slice. |
| dependency | [Normal marginal derivative](Yin_C_F0076_v1.md#statement) | The derivative of a joint actual normal system is the represented scalar divided difference on the distinguished marginal. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T13:18 |
| status | proved |
| reason | Independent review verifies the exact planar weight criterion, including the arclength normalization and the bounded measurable input extension. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Explicit weight and exact real adjoint energy, complete criterion on scalar weights, disk lower bound and necessary marginal compression of a mixed weight. |
| argument | [Argument](#argument) | Principal values for real and complex inputs, cubic polarization with normalized density, fine-partition recovery of the multiplier, positive-kernel domination, and disk indicator tests. |
| dependency | [Geometric scalar criterion](Yin_C_F0255_v1.md#statement) | Actual vacua give the two geometric energy inputs, diffuseness and the scalar bounded-vector domains. |
| dependency | [Tolsa–Verdera energy and normalization](../audits/literature/TV06/Yin_U002.md#tv06-u002) | Strong hard cutoff convergence and the curvature and ordinary arclength density terms with their exact coefficients for positive finite reweightings. |
| dependency | [Scalar adjoint formula](Yin_C_F0162_v1.md#1-actual-scalar-operators-and-orientation) | Identification on the original polynomial core of the actual adjoint with the vacuum multiplier minus the conjugated slice. |
| dependency | [Normal marginal derivative](Yin_C_F0076_v1.md#statement) | The derivative of a joint actual normal system is the represented scalar divided difference on the distinguished marginal. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0276_v1.md#finding) | All proof sections, the positive-measure source formula and its normalization, necessity and sufficiency, the disk lower bound and the correlated marginal restriction. |

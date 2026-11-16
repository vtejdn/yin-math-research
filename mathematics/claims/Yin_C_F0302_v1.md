---
author: Yin
---

# Negative mixed-unitary forms on shrinking endpoint cuts of circular curvature

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

There exists one correlated pair of bounded normal generators \((Z,Y)\) with actual starred conjugate variables and strong duals, and a sequence of genuine endpoint restrictions of its distinguished Menger curvature kernels, for which the negative form has no bound by a tuple-dependent constant times the kernel integral.
In detail, both generators are unitary, \(Z\) has a bounded density on the unit circle, and \(\mu\) denotes its law.
Use the partial liberation \(\gamma\) at \(Z\), equal to the inner difference on its marginal and zero on \(Y,Y^*\).
For a bounded real symmetric kernel \(q\) put
\[
 Q_q(u)=\operatorname{Re}\langle u,(\mathrm{id}\otimes\tau)I_q\gamma(u)\rangle ,
 \qquad I_{a\otimes b}(v\otimes w)=va\otimes bw .
\]
For each sufficiently large \(n\) there is a nonnegative symmetric kernel \(q_n\) of positive integral obtained by restricting the squared curvature to two endpoint arcs and a third-point arc, all within distance \(2n^{-1/4}\) of the point \(1\), in the diameter shell \((3n^{-1/4}/2,3n^{-1/4}]\).
There is an actual test \(u_n=a_n+i\sqrt{1-a_n^2}\) with \(a_n\) a selfadjoint represented mixed starred polynomial and \(\|a_n\|<1\), satisfying
\[
                   -Q_{q_n}(u_n)\ \ge\ c\sqrt n\iint q_n\,d\mu^2.       \tag{1}
\]
Here \(c>0\) is fixed for the entire tuple and sequence.

For the mixed powers \(W^n=(ZY)^n\) the same lower bound holds.
For these powers and all subkernels \(0\le q\le 1\) the unnormalized negative part is nevertheless bounded by the inverse-gap energy in the actual joint vacuum.
Thus (1) excludes the proposed local bound by unweighted curvature mass and leaves the unrestricted normal comparison open.

## Argument

### The tuple and the conditional suffixes

Take \(\mu(dz)=c_0|1-z|^4\,dm(z)\) on the unit circle with normalized Haar measure \(m\) and normalizing constant \(c_0\).
Set \(\rho(z)=1-|1-z|^4/32\), \(h(z)=\bar z\rho(z)\).
In the finite tracial free product of \(N=W^*(Z)=L^\infty(\mu)\) with a free Haar unitary \(V\), let \(Y\) be the [Möbius coupling](Yin_C_F0290_v1.md#statement) with parameter \(h\).
The scalar conjugate variable exists because the maximal linear density is bounded and the squared Menger curvature equals one on almost every triple. [Scalar criterion](Yin_C_F0255_v1.md#statement)
The integral \(I=\int(1-\rho^2)^{-1}d\mu\) is finite by cancellation with the fourth power in the density.
Since \(h\) is Lipschitz, the other integral in the coupling theorem satisfies
\[
 J=\iint\frac{|h(z)-h(v)|^2\,d\mu(z)d\mu(v)}
               {|z-v|^2(1-\rho(z)^2)(1-\rho(v)^2)}
 \ \le\operatorname{Lip}(h)^2 I^2 .
\]
The theorem gives both \(\mathsf A\) and \(\mathsf S\) and \(\|\xi_Z\|_2^2=\|\xi_\mu\|_2^2+2J\).
The conditional expectation of \(Y\) on \(N\) is the nonconstant \(h\), hence the coordinates are correlated.

For each word in base letters and positive \(Y\)'s, its conditional expectation on \(N\) is the corresponding word with every \(Y\) replaced by \(h\).
To see this first replace \(h\) by \(s h\) with \(s<1\) in the coupling formula.
Its norm-convergent expansion has constant term \(s h\), and each other monomial has strictly positive degree under the trace-preserving free Haar rotation \(V\mapsto e^{i\theta}V\) fixing \(N\).
Every term of positive degree has zero conditional expectation on \(N\) by rotation invariance.
Products retain this constant-term rule, and the [bounded strong-star convergence of the unitary couplings](Yin_C_F0290_v1.md#unitarity-generation-and-conditional-law-at-the-endpoint) passes it to \(s\uparrow1\).
Taking adjoints gives the corresponding negative-word rule.

For any finite word \(p\) in unitary marginal and omitted letters, the contribution to \(Q_q(p)\) from a marginal letter \(v_0\in N\) in \(p=l v_0 b\) has density with respect to \(q\,d\mu^2\)
\[
       \operatorname{Re}\!\left[
          \overline{\mathbb E_N(b)(z)}\,\mathbb E_N(b)(v)
                (1-\overline{v_0(z)}v_0(v))
                    \right].                                             \tag{2}
\]
Indeed this Leibniz term in \(\gamma p\) is \(l v_0\otimes b-l\otimes v_0b\).
Pairing after insertion of a separated tensor against \(p\), unitarity of the prefix gives \(p^*l v_0=b^*\) and \(p^*l=b^*v_0^*\).
The trace pairings give (2), first for separated tensors and then bounded measurable kernels by simple-function approximation against these bounded densities and the finite tensor expansion.
Here the word letters used are \(Z,Z^*,Y,Y^*\).

Put \(W=ZY\), \(t=\rho(z)\rho(v)\), \(d(z,v)=1-\operatorname{Re}(\bar z v)\).
Each suffix after a distinguished \(Z\) in \(W^m\) has conditional expectation \(h\rho^{j-1}=\bar z\rho^j\) for one \(1\le j\le m\).
In \(W^{-m}=(Y^* Z^*)^m\), the corresponding suffixes have expectations \(\rho^j\), \(0\le j<m\).
Thus, for \(m\ge1\), the two signed densities in (2), summed over the word, are
\[
    F_m(z,v)=-d(z,v)t\,\frac{1-t^m}{1-t},\qquad
    F_{-m}(z,v)=d(z,v)\,\frac{1-t^m}{1-t}.                               \tag{3}
\]
Values at \(t=1\) are irrelevant since \(\mu\{1\}=0\).
For positive powers \(t d(z,v)\le |h(z)-h(v)|^2/2\).
Also \(1-t\ge\sqrt{(1-\rho(z)^2)(1-\rho(v)^2)}\ge(1-\rho(z)^2)(1-\rho(v)^2)\).
Since the circle has diameter two, integrating (3) against \(0\le q\le1\) gives \(0\le -Q_q(W^m)\le 2J\) uniformly.

### Small-scale endpoint cuts

Put \(\delta=n^{-1/4}\) and use the arcs \(E_n,F_n,H_n\) corresponding respectively to angles \([\delta,11\delta/10]\), \([-11\delta/10,-\delta]\) and \([-\delta/10,\delta/10]\).
For sufficiently large \(n\), triples with endpoints in \(E_n,F_n\) in either order and third point in \(H_n\) have diameter between \(3\delta/2\) and \(3\delta\).
They have squared curvature one, apart from null coincidences.
The restricted kernel is therefore \(q_n=\mu(H_n)(1_{E_n}\otimes1_{F_n}+1_{F_n}\otimes1_{E_n})\).
On its support \(d(z,v)\) is comparable to \(n^{-1/2}\) and \(1-t\) is comparable to \(1/n\), with fixed positive comparison constants.
In particular \(t^n\) lies in a fixed compact subinterval of \((0,1)\).
The first formula in (3) proves (1) for \(W^n\).

### Passing to the strict selfadjoint polynomial test

For \(x\) on the angular parameter line, take \(A(x)=\cos x-\sin(2x)\), \(a(x)=\varepsilon A(x)\), \(f(x)=a(x)+i\sqrt{1-a(x)^2}\) with fixed sufficiently small \(\varepsilon>0\).
Use \(f(x)=\sum_{k\in\mathbb Z}c_k e^{ikx}\).
For \(0\le s\le1\) the asymmetry of its Fourier energies obeys
\[
    \sum_{k\ge1}(|c_k|^2-|c_{-k}|^2)(1-s^k)
                        =\varepsilon^3(1-s)^2/4+O(\varepsilon^4) .        \tag{4}
\]
In fact \(f=i+\varepsilon A-i\varepsilon^2 A^2/2+O(\varepsilon^4)\) uniformly, also in \(L^2\).
At positive frequencies \(1,2\) the coefficients of \(A\) are \(1/2,i/2\) and those of \(A^2\) are \(i/2,1/4\).
The squared-norm differences at these frequencies are \(\varepsilon^3/2\) and \(-\varepsilon^3/4\) up to \(O(\varepsilon^4)\).
All other nonconstant frequencies contribute in total at most \(O(\varepsilon^4)\) by Parseval since the first-order term vanishes there.
These bounds are independent of \(s\) and give (4).

By circle functional calculus set \(u_\theta=f(e^{i\theta}W^n)\), identifying \(f(e^{ix})=f(x)\).
Then \(a(e^{i\theta}W^n)\) is a strict selfadjoint polynomial in the represented starred generators.
The Fourier series of \(f\) converges with \(\sum(1+|k|)|c_k|<\infty\), by repeated integration by parts since \(a\) is a strict contraction and \(f\) is smooth.
Consequently its evaluation converges after applying the liberation derivation, using \(\|\gamma W^{kn}\|_2\le n|k|\max(\|\gamma W\|_2,\|\gamma W^*\|_2)\) and the product rule.
The Fourier limit agrees with the binomial-series graph evaluation by closability of liberation (the real derivation \(i\gamma\) has its actual vacuum).
For \(q_n\), bounded inner insertion and the slice are continuous on the coarse Hilbert space.
Averaging \(Q_{q_n}(u_\theta)\) over \(\theta\) therefore keeps exactly the terms \(|c_k|^2 Q_{q_n}(W^{kn})\).
By (3) the averaged density equals
\[
 -\frac{d(z,v)}{1-t}\left[
  \sum_{k\ge1}(|c_k|^2-|c_{-k}|^2)(1-(t^n)^k)
       -(1-t)\sum_{k\ge1}|c_k|^2(1-(t^n)^k)\right].
\]
On the arcs, \(t^n\) stays bounded away from one, so (4) makes the first sum at least a fixed positive multiple of \(\varepsilon^3\) for sufficiently small fixed \(\varepsilon\).
The second term in brackets tends uniformly to zero since \(f\) is unimodular and \(1-t=O(n^{-1})\).
The averaged density is therefore at most \(-c\sqrt n\) throughout the rectangle.
At least one angle gives (1).

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T15:57 |
| status | open |
| reason | Fix the realized obstruction to controlling localized negative curvature solely by integrated kernel mass, including the strict analytic-unitary scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | One actual correlated unitary pair, shrinking endpoint-restricted diameter shells, and unbounded negative-form-to-mass ratios for both actual test classes. |
| argument | [Argument](#argument) | Conditional suffix formula, inverse-gap comparison, choice of arcs, phase averaging and the asymmetric Fourier energies of the analytic-unitary test. |
| dependency | [Möbius--Haar coupling](Yin_C_F0290_v1.md#statement) | Actuality, both strong domains, vacuum energy and the strong-star approximation of the coupling with positive Haar Fourier modes. |
| dependency | [Scalar geometry](Yin_C_F0255_v1.md#statement) | Existence of the actual scalar vacuum for the bounded circle density. |
| dependency | [Liberation adjoint and graph](Yin_C_F0077_v1.md#statement) | Closability of actual real liberation for convergence to the analytic-unitary graph value. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:13 |
| status | proved |
| reason | Independent review verified the signed mixed-power and analytic-unitary tests on one actual strong pair, the inverse-gap energy bound and the growing negative ratio for localized shell mass. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | One actual correlated unitary pair, shrinking endpoint-restricted diameter shells, and unbounded negative-form-to-mass ratios for both actual test classes. |
| argument | [Argument](#argument) | Conditional suffix formula, inverse-gap comparison, choice of arcs, phase averaging and the asymmetric Fourier energies of the analytic-unitary test. |
| dependency | [M枚bius--Haar coupling](Yin_C_F0290_v1.md#statement) | Actuality, both strong domains, vacuum energy and the strong-star approximation of the coupling with positive Haar Fourier modes. |
| dependency | [Scalar geometry](Yin_C_F0255_v1.md#statement) | Existence of the actual scalar vacuum for the bounded circle density. |
| dependency | [Liberation adjoint and graph](Yin_C_F0077_v1.md#statement) | Closability of actual real liberation for convergence to the analytic-unitary graph value. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0310_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

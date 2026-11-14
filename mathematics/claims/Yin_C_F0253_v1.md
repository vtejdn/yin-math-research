---
author: Yin
---

# Oriented soft Cauchy cutoffs on a fixed correlated planar law

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

There is a fixed bounded normal generating pair \((Z,B)\) in a finite von Neumann algebra with faithful normal probability trace, satisfying actual starred ACSY and the strong domain condition.
Its coordinates are correlated and do not commute, and the spectral law of \(Z\) is absolutely continuous with positive density in the interior of a rectangle.
All its canonical column costs in both adjoint orientations are finite.

Use the original represented starred polynomial core \(P\), the partial liberation \(\gamma\) of \(W^*(Z)\) at \(Z\), the right trace \(C=\mathrm{id}\otimes\tau\) and the inner calculus \(I_{v\otimes w}(a\otimes b)=av\otimes wb\).
For \(r>0\), put \(u=z-w\) and define
\[
 \begin{split}
 k_r(u)&=\frac{\bar u}{|u|^2+r^2},\qquad
 m_\theta(u)=1_{\{\operatorname{Re}(e^{-i\theta}u)>0\}},\\
 E_r^\theta&= C I_{m_\theta k_r}\gamma,\qquad E_r=C I_{k_r}\gamma .
 \end{split}                                                             \tag{1}
\]
Let \(c(T)\) be the least finite-column bound
\[
        \left(\sum_j\|T p_j\|_2^2\right)^{1/2}
                  \le c(T)\left\|\sum_jp_j^*p_j\right\|^{1/2}
                        \quad (p_j\in P),
\]
allowing \(+\infty\).
There are constants \(a>0\) and \(r_0>0\) such that, for all \(0<r<r_0\),
\[
 \begin{aligned}
  c(E_r^\theta)&\ge a\,(\log(1/r))^{1/4}
                                  &&(-\pi/6\le\theta\le\pi/6),\\
  \sup_{\substack{p\in P\\\|p\|\le1}}
     \left(\int_0^{2\pi}\|E_r^\theta p\|_2^2
                         \frac{d\theta}{2\pi}\right)^{1/2}
                  &\ge a\,(\log(1/r))^{1/4}.
 \end{aligned}                                                           \tag{2}
\]
The tests giving the second inequality are single mixed starred polynomials \(p=B q(\operatorname{Re}Z)\) up to normalization.
For each fixed \(r\) the same polynomial is used throughout the angular integral.
The pair and its actual vacua are identical for all \(r\).
The test polynomial may vary with \(r\).

The two opposite angular masks satisfy on all of \(P\)
\[
              E_r^\theta+E_r^{\theta+\pi}=E_r,\qquad
                      \sup_{r>0}c(E_r)<\infty.                            \tag{3}
\]
Thus (2) is an obstruction to taking the norm, or the angular average of squared norms, before combining the opposite halves of the Cauchy kernel.

## Argument

### The planar law and its scalar vacuum

Let \(N=L^\infty(\mu)\) with \(Z(z)=z\) and \(z=x+iy\).
Set \(\mu=\tfrac12dx|_{[-1,1]}\otimes\sigma\), where \(\sigma\) is the probability on \([0,e^{-1}]\) with
\[
                  \sigma([0,y])=(\log(1/y))^{-1/2}
                           \qquad(0<y\le e^{-1}).
\]
There is no atom at zero and the density is \(1/(2y(\log(1/y))^{3/2})\) on the open vertical interval.
In particular \(\mu\) is a two-dimensional probability with full rectangular support.
It gives zero mass to every affine line.

The scalar derivative on the represented starred polynomials \(f(Z,Z^*)\) is the divided difference \((f(z)-f(w))/(z-w)\), defined off the product-null diagonal.
Each such polynomial is Lipschitz on the compact rectangle, so its derivative is a coarse Hilbert vector, with the outer product rule and prescribed value one at \(Z\).
The formula is independent of the chosen representative since \(\mu^2\)-almost every pair avoids any \(\mu\)-null set.

Put \(R_r(z)=\int k_r(z-w)\,d\mu(w)\).
We claim \(\sup_{0<r\le1}\|R_r\|_{L^2(\mu)}<\infty\).
For fixed \(y,y'\) write \(a=\sqrt{(y-y')^2+r^2}\).
The real part of the row after integrating against \(dx'/2\) is
\[
            \frac14\log\frac{(x+1)^2+a^2}{(x-1)^2+a^2}.
\]
Its absolute value for \(-1<x<1\) is bounded by \(C_1+|\log(1-|x|)|\), uniformly in \(a\) here.
Indeed both quantities in the ratio are bounded above by a fixed constant, and below by \((1-|x|)^2\).
The absolute imaginary part is at most
\[
          \frac{|y-y'|}{2}\int_{\mathbb R}\frac{dh}{h^2+a^2}
                 =\frac{\pi |y-y'|}{2a}\le\frac{\pi}{2}.
\]
Integrating these two bounds against \(\sigma(dy')\) proves the claim by square integrability of the endpoint logarithm.

The antisymmetry \(k_r(-u)=-k_r(u)\) now gives, for every scalar starred polynomial \(f\),
\[
  \begin{split}
   \iint k_r(z-w)(f(z)-f(w))\,d\mu(z)d\mu(w)
        &= 2\int f(z) R_r(z)\,d\mu(z),\\
   \lim_{r\downarrow0}\iint k_r(z-w)(f(z)-f(w))\,d\mu^2
        &=\iint\frac{f(z)-f(w)}{z-w}\,d\mu^2 .
  \end{split}
\]
The first equality uses ordinary Fubini with bounded \(k_r\) at fixed \(r\).
The second follows from the uniform Lipschitz bound on the divided difference, multiplied by \(|u|^2/(|u|^2+r^2)\).
Hence the double trace of the original derivative extends from its dense starred core with norm at most \(2\sup_r\|R_r\|_2\), where the supremum need only run through \(0<r\le1\).
The actual Hilbert adjoint of that derivative therefore contains \(1\otimes1\) in its domain.

### An actual correlated generating pair

Use one standard semicircular noise \(S\) free from \(N\).
With \(X=\operatorname{Re}Z\), define
\[
      a(z,w)=1+\tfrac14(\operatorname{Re}z+\operatorname{Re}w),\qquad
      T=S+\tfrac14(XS+SX),\qquad B=10+T .
\]
Then \(T\) is the one-channel field with real symmetric coefficient \(a\), and \(1/2\le a\le3/2\).
The [Gaussian covariance theorem](Yin_C_F0209_v1.md#statement) gives \(\|T\|\le3\) from the row bound.
Its inverse coefficient is bounded by two.
For the base-coordinate vacuum test in that theorem put \(P_1=a(z,w)\), \(Q_1=a(w,v)\).
The function \((P_1,Q_1)\mapsto Q_1/P_1-P_1/Q_1\) is uniformly Lipschitz on the indicated positive square and zero when \(P_1=Q_1\).
Since \(|P_1-Q_1|=|\operatorname{Re}(z-v)|/4\le |z-v|/4\), the required squared numerator divided by \(|z-v|^2\) is bounded almost everywhere.
The scalar vacuum just proved supplies the remaining hypothesis.
Thus the intrinsic pair \((Z,T)\) has actual conjugate variables and the strong domains, and its canonical columns in both orientations are finite by the [Gaussian column theorem](Yin_C_F0241_v1.md#statement), part 1.
Replacing \(T\) by \(B=10+T\) preserves the represented unital starred core, the normalized derivative values on both coordinates and the vacuum adjoints.
In particular \(7\le B\le13\).

The trace-preserving expectation onto \(N\) satisfies
\[
       \mathbb E_N((B-10)^2)(z)=\int a(z,w)^2\,d\mu(w)
                        =(1+x/4)^2+1/48 .
\]
The conditional expectation formula is the one-edge inner product with the same endpoint in the [first-chaos representation](Yin_C_F0209_v1.md#colored-paths-and-the-rank-obstruction).
The displayed function has nonzero covariance with \(x\) against the symmetric uniform interval law, so the two generated coordinate algebras are not free.
In the same representation the commutator \([Z,B]\) has first-chaos coefficient \((z-w)a(z,w)\), nonzero in \(L^2(\mu^2)\).
This gives a noncommuting correlated law with all coordinate and vacuum data fixed.

### The oriented row has a positive logarithmic contribution

Write \(R_r^\theta(z)=\int m_\theta(z-w)k_r(z-w)d\mu(w)\).
For each fixed \(r>0\) this is a bounded function.
On the entire selected open half-plane,
\[
 \operatorname{Re}\!\left(e^{i\theta} k_r(u)\right)
          =\operatorname{Re}(e^{-i\theta}u)/(|u|^2+r^2)>0 .
\]
Choose \(|\theta|\le\pi/6\), \(|x|\le1/2\), \(0<y\le r\) and \(0<y'\le r\).
Integrate over \(h=x-x'\in[4r,1/4]\), so \(x'\in[-1,1]\).
With \(v=y-y'\), one has \(|v|\le r\) and
\(\operatorname{Re}(e^{-i\theta}(h+iv))=h\cos\theta+v\sin\theta\ge h/2\).
The denominator \(h^2+v^2+r^2\) is at most \(2h^2\).
Consequently the selected points contribute at least \(1/(4h)\) to the rotated real integrand, and the rest of the selected half-plane contributes nonnegatively.
For \(t=\log(1/r)\) large enough this yields
\[
 |R_r^\theta(x+iy)|\ge c_1\,\sigma([0,r])\log(1/(16r))\ge c_2 t^{1/2}.
\]
The set of these \(z\)'s has \(\mu\)-mass \(\tfrac12\sigma([0,r])=\tfrac12 t^{-1/2}\), so
\[
                       \|R_r^\theta\|_{L^2(\mu)}\ge c_3 t^{1/4}             \tag{4}
\]
uniformly on the specified angle interval.

### The same mixed input across rotations

For a bounded marginal function \(f\), define at fixed \(r,\theta\)
\[
 T_r^\theta f(z)=\int m_\theta(z-w) k_r(z-w)(f(z)-f(w))\,d\mu(w) .
\]
For each scalar starred polynomial \(q\) this is exactly \(E_r^\theta q\) by the prescribed partial liberation \(\gamma q=q\otimes1-1\otimes q\). [Normal liberation](Yin_C_F0238_v1.md#statement)
Moreover \(E_r^\theta(Bq)=B T_r^\theta q\) by \(\gamma B=0\) and the outer product rule.
All these maps are evaluated on the same represented core as the original actual derivatives.
The bounded integral on general \(f\) here is only used to approximate polynomial tests.

Take \(f_N(z)=e^{iN x}\) for integers \(N\to\infty\).
At each fixed \(r,\theta\),
\[
 T_r^\theta f_N=f_N R_r^\theta-H_{r,\theta,N},\qquad
 H_{r,\theta,N}(z)=\int m_\theta(z-w) k_r(z-w)e^{iN\operatorname{Re}w}\,d\mu(w).
\]
For fixed \(z,\theta,r\), integrating first in the vertical variable produces an \(L^1(dx')\) function on \([-1,1]\), bounded in absolute value by \(1/(2r)\) before the uniform horizontal weight.
The Riemann–Lebesgue lemma therefore gives \(H_{r,\theta,N}(z)\to0\).
It also follows by \(L^1\) approximation by step functions and integration of each exponential over an interval.
The integrands are jointly Borel in \(z,\theta\), and the same bound \(1/(2r)\) gives \(H_{r,\theta,N}\to0\) in \(L^2(d\mu\,d\theta/(2\pi))\), and in \(L^2(\mu)\) for each angle separately.
It follows that \(\|T_r^\theta f_N\|_2\to\|R_r^\theta\|_2\) at each angle, with the corresponding convergence of the joint norms over the angle interval.
Indeed \(|f_N|=1\) gives the norm of the leading term exactly, and the difference in norms is bounded by the norm of \(H_{r,\theta,N}\).

For each \(N\) take a complex polynomial \(q_N(x)\) approximating \(e^{iNx}\) uniformly on \([-1,1]\) within \(1/N\), for example a sufficiently long Taylor polynomial.
The integral formula gives \(\|T_r^\theta q_N-T_r^\theta f_N\|_2\le1/(rN)\), uniformly in angle for this fixed \(r\).
The inputs \(p_N=Bq_N(\operatorname{Re}Z)/26\) are original mixed starred polynomials and \(\|p_N\|\le1\) by \(\|B\|\le13\), \(\|q_N\|_\infty\le2\).
Since left multiplication by \(B\) has Hilbert lower bound seven,
\[
                 \|E_r^\theta p_N\|_2\ge(7/26)\|T_r^\theta q_N\|_2 .
\]
Take the supremum over these inputs after the fixed-\(r\) limit in \(N\) and apply (4).
For the angular estimate, apply the same lower bound in the joint Hilbert norm over \([-\pi/6,\pi/6]\) first, then use the full angular integral by nonnegativity and periodicity.
This proves both statements in (2), with one common input at a time in the angular test.

### Opposite orientations

For fixed \(\theta\), \(\mu^2\{\operatorname{Re}(e^{-i\theta}(z-w))=0\}=0\) by the planar density and Fubini.
The spectral measure on the inner legs of any coarse vector is dominated by \(\mu^2\), by the [coarse measure class](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core).
Hence \(I_{m_\theta}+I_{m_{\theta+\pi}}=1\) on the full coarse space, proving the first identity in (3) at every fixed angle on the entire original core.
The [soft-cutoff estimate](Yin_C_F0238_v1.md#statement), equation (2), gives \(\sup_{r>0}c(E_r)\le3c(C\delta_i)<\infty\) at this law.
In particular the angular mean of the vectors \(E_r^\theta p\) at each fixed \(p,r\) is \(E_rp/2\), by pairing opposite angles.
The mean exists by strong measurability of bounded Borel multipliers on the cyclic spectral space of \(\gamma(p)\) and their uniform bound at fixed \(r\).
Equation (2) quantifies what is lost for the angular square mean on that same family of actual mixed inputs.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T11:48 |
| status | open |
| reason | The correlated planar law, its original actual vacua, mixed angular tests and exact cancellation are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A single noncommuting correlated actual law with finite full columns, divergent fixed-angle and common-input angular-square tests, and uniform opposite-pair cancellation. |
| argument | [Argument](#argument) | Scalar adjoint by soft antisymmetric pairing, one-channel construction and conditional covariance, logarithmic oriented rows, normalized polynomial tests and full-cutoff recovery. |
| dependency | [Gaussian covariance criterion](Yin_C_F0209_v1.md#statement) | Scalar vacuum plus finite one-channel inverse amplitude and variation integrals give the actual and strong pair, including the operator norm of the field. |
| dependency | [First-chaos representation](Yin_C_F0209_v1.md#colored-paths-and-the-rank-obstruction) | The endpoint actions and one-edge inner product computing the conditional field square and the commutator norm. |
| dependency | [Gaussian canonical columns](Yin_C_F0241_v1.md#statement) | Part 1 for finiteness of original and adjoint-tuple columns at this fixed single-channel correlated law. |
| dependency | [Original soft cutoff](Yin_C_F0238_v1.md#statement) | Partial liberation and equation (2) bounding the full signed cutoff uniformly by the finite original cost. |
| dependency | [Coarse product measure class](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Every fixed angular boundary is null for every inner coarse vector, giving exact opposite-mask cancellation. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T11:51 |
| status | proved |
| reason | Adopt the fixed-law obstruction for oriented Cauchy cutoffs after independent whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A single noncommuting correlated actual law with finite full columns, divergent fixed-angle and common-input angular-square tests, and uniform opposite-pair cancellation. |
| argument | [Argument](#argument) | Scalar adjoint by soft antisymmetric pairing, one-channel construction and conditional covariance, logarithmic oriented rows, normalized polynomial tests and full-cutoff recovery. |
| dependency | [Gaussian covariance criterion](Yin_C_F0209_v1.md#statement) | Scalar vacuum plus finite one-channel inverse amplitude and variation integrals give the actual and strong pair, including the operator norm of the field. |
| dependency | [First-chaos representation](Yin_C_F0209_v1.md#colored-paths-and-the-rank-obstruction) | The endpoint actions and one-edge inner product computing the conditional field square and the commutator norm. |
| dependency | [Gaussian canonical columns](Yin_C_F0241_v1.md#statement) | Part 1 for finiteness of original and adjoint-tuple columns at this fixed single-channel correlated law. |
| dependency | [Original soft cutoff](Yin_C_F0238_v1.md#statement) | Partial liberation and equation (2) bounding the full signed cutoff uniformly by the finite original cost. |
| dependency | [Coarse product measure class](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Every fixed angular boundary is null for every inner coarse vector, giving exact opposite-mask cancellation. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0262_v1.md#finding) | The actual correlated planar pair, common mixed polynomial angular test, logarithmic lower bound and uniform opposite-pair cancellation. |

---
author: Yin
---

# Strong type for a vector-valued Calderón–Zygmund operator on a measure of polynomial growth

## GM00-U001

The inspected [journal edition](readme.md#yin-edition) defines the measure on printed p. 614 and the vector-valued operator on p. 617.
Section 2.3, Theorem 2.7 and its proof are on p. 626.
This unit records the operator hypotheses and the strong \(p=3\) specialization.

<a id="operator-kernel"></a>
### Vector-valued kernel and operator

On a separable metric space \((X,d)\) the source uses a nonnegative Borel measure \(\sigma\) with \(\sigma(\overline B(x,r))\le r^n\) for all centers and positive radii, with \(n>0\).
A finite uniform growth constant can be normalized by rescaling the measure and tracking the associated operator and kernel constants.

For Banach spaces \(A,B\) let \(K(x,y)\in\mathcal L(A,B)\) off the diagonal.
Section 2 requires a uniform size bound \(\|K(x,y)\|\le C_K d(x,y)^{-n}\).
For every \(x\ne x'\), with \(D=\{y:d(x,y)\ge2d(x,x')\}\), both integral bounds
\[
 \int_D\|K(x,y)-K(x',y)\|\,d\sigma(y)\le C_K,\qquad
 \int_D\|K(y,x)-K(y,x')\|\,d\sigma(y)\le C_K
\]
use the operator norm from \(A\) to \(B\).
Definition 2.1 additionally requires a linear bounded map \(T:L^2(\sigma;A)\to L^2(\sigma;B)\) represented for each \(f\in L^2(\sigma;A)\) by \(\int K(x,y)f(y)\,d\sigma(y)\) for almost every \(x\) outside \(\operatorname{supp}f\).
The off-support formula is sufficient at this interface.

<a id="strong-type"></a>
### The strong \(L^3\) estimate

Theorem 2.7 gives \(T:L^p(\sigma;A)\to L^p(\sigma;B)\) bounded for \(1<p<\infty\).
Taking \(A=\mathbb C\), \(B=L^2((0,\infty),dt/t)\) and \(K(x,y)=(s_t(x,y))_{t>0}\), its \(p=3\) conclusion reads
\[
     \left\|\,\left(\int_0^\infty |Tf(x)(t)|^2\,\frac{dt}{t}\right)^{1/2}\right\|_{L^3(\sigma)}
           \le C\|f\|_{L^3(\sigma)}.
\]
Here \(T\) is the linear map with values in the scale Hilbert space.
The kernel size and both oscillation estimates must hold in that Hilbert norm, and the global \(L^2\) operator bound and off-support representation are additional hypotheses.
The proof obtains strong estimates below two from weak type \((1,1)\) and interpolation.
For the scalar input and Hilbert output the adjoint kernel \(K(y,x)^*\) satisfies the same bounds, so duality at \(p'=3/2\) gives the stated exponent.
The weak-type argument is used here as an established source theorem.
Uniform application to a family requires uniform growth, kernel and global \(L^2\) bounds.

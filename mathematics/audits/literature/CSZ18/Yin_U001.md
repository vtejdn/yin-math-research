---
author: Yin
---

# A weak trace-class bound for a planar double operator integral

<a id="csz18-u001"></a>
## Weak endpoint for the planar symbol

In the [published article](readme.md), Theorem 1.2 (p. 1646) treats a commuting selfadjoint \(d\)-tuple \(A\) in a semifinite tracial von Neumann algebra acting on a separable Hilbert space.
For a bounded Borel symbol \(b\), its double operator integral \(T_b^A\) on \(L^2\) is defined by the joint left and right spectral action of \(A\): the spectral projection of \(B\times C\) acts by \(V\mapsto E_A(B)V E_A(C)\) for Borel \(B,C\subset\mathbb R^d\) (Section 2.4, pp. 1649–1650).
For a real Lipschitz function \(f:\mathbb R^d\to\mathbb R\), equation (2.7) sets
\[
  b_k(\lambda,\mu)=
  \frac{(f(\lambda)-f(\mu))(\lambda_k-\mu_k)}{|\lambda-\mu|^2}
\]
off the diagonal and takes the diagonal value zero.
For \(V\in L^1\cap L^2\) the theorem bounds \(\|T_{b_k}^A V\|_{1,\infty}\) by \(c(d)\|\nabla f\|_\infty\|V\|_1\).
Here \(\|W\|_{1,\infty}=\sup_{t>0}t\,\mu(t,W)\) uses the generalized singular value function for the given trace (Section 2.2).

To identify the relevant symbol take \(A=(\operatorname{Re}Z,\operatorname{Im}Z)\) for one normal operator \(Z\), \(f(x,y)=x\), and write \((a,b)=\lambda-\mu\).
Then \(b_1-i b_2=a/(a+ib)\) whenever \((a,b)\ne(0,0)\).
On a graph \(Z=s+i g(s)\) this gives precisely \((s-t)/(s-t+i(g(s)-g(t)))\).
The weak quasinorm triangle inequality permits this linear combination with an absolute change of constant; each finite matrix amplification satisfies the same hypotheses with \(d=2\).

Theorem 1.2, its weak quasinorm and the kernel convention were inspected on 2026-11-14.
The weak endpoint is accepted for these operator-integral tests; the transference and weak type proofs in Sections 3–5 were outside this inspection.
Weak trace-class control permits singular values proportional to \(1/n\) and therefore does not bound pairings uniformly against arbitrary operator-norm contractions.
Using this source for an original mixed-word derivative would require both a bound on its input in a suitable test norm and a justified passage through the slice and finite column sum.

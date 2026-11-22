---
author: Yin
---

# Kat68: A Bounded Positive Commutator Criterion

## Kat68-U001

The inspected [published edition](readme.md#yin-edition) gives the spectral-projection formula (2.2) on p. 536, defines smoothness on p. 537, and states Theorem (6.2) on p. 543.
The source inspection on 2026-11-22 UTC covered these passages and the existence and norm estimates in the proof of Theorem (6.2), pp. 544–545.
Theorem (2.1) supplies the spectral-projection formula used below.

<a id="t-smoothness"></a>
### Smoothness relative to a bounded selfadjoint operator

Let \(T\) be a bounded selfadjoint operator on a Hilbert space \(\mathcal H\), let \(E_T\) be its spectral measure, and let \(A:\mathcal H\to\mathcal H'\) be a bounded operator into a Hilbert space \(\mathcal H'\).
In the normalization of (2.2), \(A\) is \(T\)-smooth if
\[
\|A\|_T^2
  =\sup_{\substack{I\subset\mathbb R\ \mathrm{interval}\\0<|I|<\infty}}
       \frac{\|A E_T(I)\|^2}{|I|}
  <\infty ,
\]
where \(|I|\) denotes Lebesgue length.
This formulation uses the bounded selfadjoint setting of §§2 and 6.

### Positive commutators

For bounded selfadjoint \(H,L\) on the same Hilbert space with \(L\geq 0\), Theorem (6.2) gives a bounded selfadjoint \(K\) satisfying \(i[H,K]=L\) if and only if \(L^{1/2}\) is \(H\)-smooth.
The sufficiency argument on p. 545, using Theorem (3.2), gives a solution \(K_1\) with \(0\leq K_1\leq 2\pi\|L^{1/2}\|_H^2 1\).
Subtracting the scalar \(\pi\|L^{1/2}\|_H^2 1\) from \(K_1\) preserves the commutator and gives \(\|K\|\leq \pi\|L^{1/2}\|_H^2\).

<a id="scalar-bounded-dual"></a>
### Rank-one specialization to a scalar bounded dual

For a bounded selfadjoint \(X\) with a unit vector \(\Omega\), let \(P_\Omega\) be the projection onto \(\mathbb C\Omega\) and \(\mu(I)=\|E_X(I)\Omega\|^2\).
Since \(\|P_\Omega E_X(I)\|=\|E_X(I)\Omega\|\), formula (2.2) gives
\[
\|P_\Omega\|_X^2=\sup_{0<|I|<\infty}\frac{\mu(I)}{|I|}.
\]
A finite supremum \(C\) gives \(\mu\leq C\,dt\) by interval covers, and \(\mu=w\,dt\) with \(w\in L^\infty\) gives the reverse bound by \(\|w\|_\infty\).
Thus \(P_\Omega\) is \(X\)-smooth exactly when \(\mu=w\,dt\) with \(w\in L^\infty(\mathbb R)\), in which case \(\|P_\Omega\|_X^2=\|w\|_\infty\).

Taking \(H=X\) and \(L=P_\Omega\) in Theorem (6.2) gives the manuscript's normalization \([X,T_0]=P_\Omega\) by setting \(T_0=iK\).
Conversely, if a bounded \(T_0\) satisfies the normalized equation, then \(K=(T_0-T_0^*)/(2i)\) is a bounded selfadjoint solution of \(i[X,K]=P_\Omega\), since \([X,T_0^*]=-P_\Omega\).
Consequently the spectral measure of \(\Omega\) has an essentially bounded Lebesgue density if and only if the bounded dual equation has a solution.
One can choose \(T_0\) skew-adjoint with \(\|T_0\|\leq\pi\|w\|_\infty\).

For \(X\) acting by multiplication on \(L^2(\mu)\) in F0001, Example 6.3, \(\Omega=1\) and \(w(t)=4t^3\mathbf 1_{(0,1)}(t)\).
The criterion gives a bounded \(T_0\) with \(\|T_0\|\leq 4\pi\).
The free-product lift to the pair \((X,S)\) uses Voiculescu's separate proposition.
[Voi98, §5.6](../Voi98/Yin_U005.md#free-products-55-58)

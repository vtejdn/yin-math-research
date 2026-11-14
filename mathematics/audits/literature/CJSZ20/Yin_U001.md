---
author: Yin
---

# The BMO endpoint associated with graph distance

<a id="cjsz20-u001"></a>
## Graph heat semigroup and BMO

Let \(A=A^*\) belong to a finite tracial von Neumann algebra \(M\), and let \(g:\mathbb R\to\mathbb R\) be 1-Lipschitz.
Theorem 1.1 of the [published article](readme.md), p. 3, defines a Markov semigroup \(T_t\) by double operator integration against the spectral measure of \(A\) with symbol
\[
  \exp\!\left(-t\big((s-u)^2+(g(s)-g(u))^2\big)\right).
\]
It bounds, from \(M\) to the associated \(\mathrm{bmo}_T(M)\), the double operator integral with symbol \(g^{[1]}(s,u)=(g(s)-g(u))/(s-u)\) off the diagonal and zero on it.
The operator norm of this map has a numerical bound.
For \(x\in M\) such that \(T_t x\to0\) weak-star as \(t\to\infty\), the column BMO norm used here is
\[
  \|x\|_{\mathrm{bmo}^c_T}
   =\sup_{t\ge0}\|T_t(x^*x)-(T_t x)^*(T_t x)\|_\infty^{1/2};
\]
the row norm applies the column norm to \(x^*\) (Section 2.2, p. 5, equations (2.1)–(2.2)).

Proposition 2.7 (p. 8) also bounds the Euclidean Fourier multiplier for a smooth degree-zero symbol \(m\) away from the origin, with \(m(0)=0\), from bounded operator-valued trigonometric functions to heat-semigroup BMO.
Its constant depends on \(m\) and is independent of the semifinite coefficient algebra.
Lemma 6.2 (p. 20) displays a finite-spectrum transfer for \(g^{[1]}\): conjugation by graph characters attaches the frequency \((s-u,g(s)-g(u))\) to the spectral block \(E_A(\{s\})xE_A(\{u\})\).
Thus the planar symbol \(m(a,b)=a/(a+ib)\), extended by zero at the origin, acts on such a finite sum at exactly the graph frequencies that occur in the inverse divided difference.
This block computation uses smoothness of \(m\) on the unit circle.

The theorem statement, the column norm, the smooth-symbol estimate and the finite-spectrum transference calculation were inspected on 2026-11-14.
The stated divided-difference BMO estimate and Proposition 2.7 are accepted at these scopes.
The full proofs of the multiplier bounds, Markov dilations and interpolation results were outside this inspection.
The named theorem bounds \(g^{[1]}\), while the inverse divided difference uses \(1/(1+i g^{[1]})\) off the diagonal.
Extending the finite spectral calculation for this latter symbol to the desired general spectral calculus requires a justified limit.
The F0011 application further needs uniform Hilbert-space estimates for slices on mixed polynomial columns, which these BMO estimates do not supply.

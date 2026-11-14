---
author: Yin
---

# The Cauchy singular integral in graph coordinates

<a id="mus14-u001"></a>
## Cauchy integral on a Lipschitz graph

For a real Lipschitz function \(A:\mathbb R\to\mathbb R\), put \(g(x)=x+iA(x)\).
In the [published edition](readme.md), p. 1089, equation (1.1), the graph Cauchy integral acts on functions of the real parameter by
\[
     C_\Gamma f(x)=\operatorname{p.v.}\int_{\mathbb R}
              \frac{f(y)}{g(x)-g(y)}\,dy .
\]
The measure is Lebesgue measure on the parameter line, and the kernel has coefficient one.
The Coifman–McIntosh–Meyer theorem stated immediately after (1.1) extends this operator boundedly on \(L^p(\mathbb R,dx)\) for \(1<p<\infty\).
In particular both \(p=3\) and \(p=3/2\) are in its range.

For compact input and test supports a positive distance apart in the real parameter, \(|g(x)-g(y)|\ge|x-y|\) bounds the kernel on their product.
The bilinear pairing of the bounded operator therefore equals the ordinary double integral on those supports, first for smooth tests and then by \(L^p\) and dual \(L^{p'}\) approximation with separated support neighborhoods.
This restricted pairing requires no pointwise limit on the support of the input.
An application to a finite graph segment can first extend \(A\) constantly beyond its endpoints and extend the input by zero.

The formula, the range of exponents and the reduction to the commutator bounds on pp. 1089–1090 were inspected on 2026-11-14.
The stated bounded graph operator is accepted at this scope.
The estimates proving the multilinear bounds later in the article were outside this inspection.

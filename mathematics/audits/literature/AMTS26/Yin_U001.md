---
author: Yin
---

<a id="amts26-u001"></a>
# AMTS26-U001: Meromorphic evaluation and trace-class cycles

The [inspected edition](readme.md#yin-edition) is arXiv v2.
The statement-level inspection covers the introduction's convention for \(\Delta_1\), Theorem 6.6, Corollary 6.9, and the example in Theorem 7.4 and Remark 7.5.

<a id="meromorphic-evaluation"></a>
## Evaluation and embedding

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state, and let \(X\in M^d\) act by left multiplication on \(H=L^2(M,\tau)\).
Write \(\mathscr O_d(r)\) for the ring of noncommutative analytic functions on the row ball of radius \(r\) that are bounded on smaller row balls, and \(\mathscr M_d(r)\) for its universal skew field of fractions.
The source's maximality condition \(\Delta_1(X)=d\) means that the only tuple of trace-class operators \(T_i\) on \(H\) with \(\sum_i[T_i,X_i]=0\) is the zero tuple.
Under this condition and \(\|X\|_{\mathrm{row}}<r\), Theorem 6.6 says that every full matrix over \(\mathscr O_d(r)\) evaluates at \(X\) to a matrix with zero kernel and cokernel.
Corollary 6.9 states that evaluation at \(X\) extends from \(\mathscr O_d(r)\) to an embedding \(\mathscr M_d(r)\hookrightarrow L^0(M)\).

<a id="strict-separation"></a>
## Maximal Delta with a trace-class cycle

Remark 7.5 gives the selfadjoint version of the example in Theorem 7.4.
For a standard free semicircular pair \(S_1,S_2\), its third entry is
\[
 g(S_1,S_2),\qquad
 g(x,y)=\sum_{n\ge 0}\frac{x^n y^n x^n}{n!}.
\]
For the resulting triple the source gives \(\Delta_1<3=\Delta\).
The triple has trivial finite-rank solution space and a nonzero trace-class solution for the homogeneous commutator equation.

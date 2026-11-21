---
author: Yin
---
# Number-field rank integrality from one direct power

On 2026-11-21T04:34 UTC a separate reviewer working for Yin inspected the statement and whole argument of C_A0097_v1.
The reviewer had no role in developing the proof and received no development dialogue, author explanation or prior verdict on it.
The fixed Claim and the [original Task contract](../../tasks/Yin_T_A0001_v1.md#contract) supplied the mathematical inputs.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0097_v1.md#statement) | Every finite rectangular matrix, every embedding of the degree-\(d\) number field, the sufficient number of coordinates and the unnormalized trace. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0097_v1.md#argument) | Column increments, mixed moments from tensor products and restriction of scalars, strict inequality and the numerical endpoint example. |

## Whole finding

Fix \(A\in M_{m,n}(K[G])\), an embedding \(\sigma\), and a column index \(1\le j\le n\).
If \(P\) projects onto the closed range of \(\sigma A_{j-1}\) and \(c\) is the next column, the new closed range is the orthogonal sum of \(\operatorname{ran}P\) and \(\overline{\operatorname{ran}((1-P)c)}\).
Indeed subtracting \(Pc\) from \(c\) preserves the closed span together with \(\operatorname{ran}P\).
The final projection of \((1-P)c\) has the trace of its initial projection by polar decomposition, and that initial projection acts in a single copy of \(\ell^2(G)\).
Thus its dimension \(x_\sigma\) is exactly the rank increment and lies in \([0,1]\), including at \(j=1\).

For \(1\le l\le 2k\), choose \(i\) new prefixes \(A_j\) and \(l-i\) preceding prefixes \(A_{j-1}\).
In distinct group coordinates the Hilbert space tensor product of their closed ranges is the closed range of the tensor product matrix \(B\), since simple tensors of vectors from the ranges have dense span there.
The product trace on the range projection gives \((r_j^\sigma)^i(r_{j-1}^\sigma)^{l-i}\).
Missing factors contribute one, and a present factor with zero columns contributes rank zero, so these formulas include both ends \(i=0,l\).

Expanding each coefficient of \(B\) by its rational multiplication matrix gives one finite rational matrix over \(G^l\).
Under \(G^l\subseteq G^{2k}\), each right coset carries the same left convolution, and evaluating its range projection on the identity coset preserves the group trace.
Separability of \(K/\mathbb Q\) simultaneously diagonalizes the multiplication matrices over \(\mathbb C\), with one block for each of the \(d\) embeddings.
This uses the same embedding in every tensor factor of a block because \(\sigma\) acts on the product of its coefficients.
The constant changes on domain and codomain are bounded invertible module maps, so the input change preserves the range and the output change gives isomorphic closed ranges with equal dimension by polar decomposition.
The unnormalized trace adds the block ranks with weight one.
Consequently rational integrality on the single group \(G^{2k}\) makes each of the required sums of mixed moments an integer.

At fixed \(j\), binomial expansion therefore gives \(\sum_\sigma x_\sigma^l\in\mathbb Z\) through degree \(2k\).
The integer polynomial \(t^k(1-t)^k\) has zero constant term and takes values in \([0,4^{-k}]\) on \([0,1]\).
The sum of its \(d\) values is an integer smaller than one when \(4^k>d\), so every term vanishes and every embedding has only zero or unit increments.
Summing in \(j\) gives the claimed rank under each embedding, and polar decomposition gives kernel dimension \(n-\operatorname{rk}_G(\sigma A)\).
Taking \(k=\lfloor\log_4 d\rfloor+1\) is valid for every positive \(d\), and \(d=1\) is already the rational case on \(G\).
At \(d=4^k\), taking all entries equal to \(1/2\) gives the integral moments \(2^{2k-l}\) for \(1\le l\le2k\).
This verifies the stated limitation of the moment test while leaving the optimal number of coordinates for group-ring matrices open.

The conditional number-field conclusion follows with no further hypothesis on the embeddings or on \(m,n\).
Its application still requires rational integrality on the indicated direct power, and the full Task also allows transcendental coefficients.

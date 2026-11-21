---
author: Yin
---
# A logarithmic direct-power bound for number-field coefficients

## Statement

Let \(G\) be a torsion-free discrete group and \(K\subset\mathbb C\) a number field of degree \(d\).
Let \(k\ge1\) be an integer with \(4^k>d\).
If every rational group-ring matrix on \(G^{2k}\) has integral regular rank, every finite rectangular matrix over \(K[G]\) has integral regular rank on \(G\) under every embedding of \(K\) in \(\mathbb C\).
In particular \(2(\lfloor\log_4 d\rfloor+1)\) coordinates suffice independently of the matrix size and number of coefficients.
For \(d=1\) one coordinate suffices directly.
The regular rank uses the unnormalized matrix trace, so the result is equivalent to integer kernel dimension at this scope.

## Argument

For a matrix \(A\) write \(A_j\) for its first \(j\) columns, with \(A_0\) of rank zero.
For each embedding \(\sigma\) put \(r_j^\sigma=\operatorname{rk}_G(\sigma A_j)\) and \(x_\sigma=r_j^\sigma-r_{j-1}^\sigma\) at a fixed step \(j\).
The two closed column spaces are nested.
Their dimension difference is the rank of the new column projected orthogonally off the preceding closed space, which is at most the regular dimension one of its domain.
Consequently \(0\le x_\sigma\le1\).

For \(1\le l\le2k\) and \(0\le i\le l\), take the external tensor product of \(i\) copies of \(A_j\) and \(l-i\) copies of \(A_{j-1}\), across distinct group coordinates of \(G^l\).
It is a finite rectangular matrix \(B\) over \(K[G^l]\), including the zero-rank terms when an empty prefix occurs.
Under one embedding its rank is \((r_j^\sigma)^i(r_{j-1}^\sigma)^{l-i}\), with the factor for no copies omitted.
Indeed the closed range of the exterior Hilbert tensor product is the Hilbert tensor product of the closed ranges, by density of their algebraic tensor product.
The resulting range projection has the product of their unnormalized traces.

Choose a rational basis of \(K\) and apply the regular representation \(K\to M_d(\mathbb Q)\) to each group coefficient of \(B\).
The resulting rational matrix is over \(G^l\) and its regular rank is unchanged on embedding the coordinate subgroup in \(G^{2k}\), by decomposition into right cosets for left convolution and the canonical trace.
Over \(\mathbb C\) the field algebra \(K\otimes_{\mathbb Q}\mathbb C\) is the direct product of the \(d\) embeddings.
An invertible constant change of basis therefore gives the direct sum of the \(\sigma B\), up to row and column coordinate permutations.
Such bounded invertible changes preserve closed-range dimension by the polar decomposition of the range isomorphism.
By the rational integrality hypothesis this proves
\[
                \sum_\sigma (r_j^\sigma)^i(r_{j-1}^\sigma)^{l-i}\in\mathbb Z .
\]
Binomial expansion now gives \(\sum_\sigma x_\sigma^l\in\mathbb Z\) for every \(1\le l\le2k\).
The coefficients in \([x(1-x)]^k\) are integers and its degree is \(2k\), hence
\[
        \sum_\sigma[x_\sigma(1-x_\sigma)]^k\in\mathbb Z,\qquad
        0\le\sum_\sigma[x_\sigma(1-x_\sigma)]^k\le d\,4^{-k}<1 .
\]
Each summand vanishes, giving \(x_\sigma\in\{0,1\}\) for all embeddings at this column step.
Summing the increments over \(j\) gives the asserted regular ranks.

At \(d=4^k\), an abstract list of \(d\) entries equal to \(1/2\) has integral power sums through degree \(2k\).
Thus these moment conditions alone admit fractional entries at equality.
This numerical example makes no assertion about attainable group-ring ranks.
The [single-group restriction-of-scalars obstruction](../ledger/Yin_L_A0030_v1.md#the-precise-limit-of-restriction-of-scalars) concerns the first moment, and [the direct-power argument for arbitrary complex coefficients](Yin_C_A0096_v1.md#statement) gives a different bound depending on size and coefficient count.
Here no equality of ranks for conjugate coefficients or soficity is required.

## Assessment history

### Decision number-field-moments

| Field | Value |
| --- | --- |
| date | 2026-11-21T04:36 |
| status | proved |
| reason | Independent review verified the rank moments, strict threshold and all embedding and matrix-size quantifiers. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Integral ranks at all embeddings from one degree-dependent rational direct power. |
| argument | [Proof](#argument) | Column increments, simultaneous restriction of scalars and nonnegative integer moment test. |
| review | [Whole finding](../audits/reviews/Yin_R_A0133_v1.md#whole-finding) | Complete independent inspection at the mathematical and source scope stated in the finding. |

## Current assessment

[Selected decision](#decision-number-field-moments)

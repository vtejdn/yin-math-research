---
author: Yin
---
# Number-field rank integrality for odd and even coordinate counts

At 2026-11-21T05:12 UTC a separate agent working for Yin reviewed the full statement and argument of C_A0097_v2.
The reviewer had no part in developing the proof and received no development discussion, author explanation or earlier verdict on v2.
The reviewer consulted the [earlier finding on v1](Yin_R_A0133_v1.md#whole-finding) and checked directly how the [v1 argument](../../claims/Yin_C_A0097_v1.md#argument) applies to each moment used in v2.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole finding](#whole-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole finding](#whole-finding) | [Statement](../../claims/Yin_C_A0097_v2.md#statement) | Rational integrality on \(G^j\), every embedding, arbitrary finite rectangular matrices and the sufficient exponent for every positive field degree. |
| [Whole finding](#whole-finding) | [Argument](../../claims/Yin_C_A0097_v2.md#argument) | Mixed moments for all \(l\le j\), the two parity cases including \(j=1\), summation of rank increments and the endpoint example. |

## Whole finding

At one column step let \(a_\sigma,b_\sigma\) be the regular ranks before and after adding the column at embedding \(\sigma\).
The difference \(x_\sigma=b_\sigma-a_\sigma\) is the dimension of the closed range of the new column projected orthogonally off the preceding closed range.
Its domain has dimension one, so polar decomposition gives \(0\le x_\sigma\le1\).

For each \(1\le l\le j\), tensoring \(i\) new prefixes and \(l-i\) preceding prefixes on distinct coordinates gives a matrix over \(K[G^l]\).
The closed range under \(\sigma\) is the Hilbert tensor product of the closed factor ranges, so its rank is \(b_\sigma^i a_\sigma^{l-i}\), with absent factors omitted.
Any tensor with a zero-column factor contributes zero.
Restriction of scalars gives a rational matrix whose rank is the sum of these products over the \(d\) embeddings.
Indeed \(K\otimes_{\mathbb Q}\mathbb C\) splits as one copy of \(\mathbb C\) for each embedding, and in each block that embedding acts on every factor.
The constant invertible changes of basis preserve closed-range dimension, and the unnormalized matrix trace adds the block dimensions.
Over the coordinate subgroup \(G^l\subseteq G^j\), convolution acts on every right coset as on the subgroup itself, so the trace at the identity gives the same rank in both groups.
Rational integrality on \(G^j\) therefore gives integral mixed sums for every \(i\), with no parity condition on \(l\) or \(j\).
Expanding \((b_\sigma-a_\sigma)^l\) now gives integral power sums through degree \(j\), including the constant sum \(d\) at degree zero.

If \(j=2k\), the sum of \([x_\sigma(1-x_\sigma)]^k\) is an integer in \([0,d/4^k]\), and \(d<2^j=4^k\) forces it to vanish.
If \(j=2k+1\), both \(I_0\) and \(I_1\) in the Claim are integers, since they sum integer polynomials of degree \(j\).
Each interior increment contributes positively to both, so such an increment would imply \(I_0+I_1\ge2\).
Factoring their sum gives \(\sum_\sigma[x_\sigma(1-x_\sigma)]^k\le d/4^k<2\).
For \(k=0\) the two polynomials are \(1-x\) and \(x\), and their sum is identically one even at the endpoints.
Thus each increment lies in \(\{0,1\}\), and summing from the empty prefix gives integral rank at each embedding.

The least positive integer satisfying \(2^j>d\) is \(\lfloor\log_2 d\rfloor+1\), which gives three coordinates for degree four and is independent of matrix size.
At equality \(d=2^j\) the constant list \(x_\sigma=1/2\) has power sum \(2^{j-l}\) in degree \(l\), integral up to \(j\) and equal to \(1/2\) at \(j+1\).
This verifies the claimed limit of the moment argument.
Whether such a list can occur as regular-rank increments under the group hypothesis remains open in this argument.

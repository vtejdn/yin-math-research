---
author: Yin
---
# The odd and even direct-power bounds for number fields

## Statement

Let \(K\subset\mathbb C\) be a number field of degree \(d\), and \(G\) a torsion-free discrete group.
For any integer \(j\ge1\) with \(2^j>d\), rational matrix integrality on \(G^j\) implies integral regular ranks on \(G\) for all finite rectangular \(K[G]\)-matrices under every embedding of \(K\) into \(\mathbb C\).
One may take \(j=\lfloor\log_2 d\rfloor+1\), independently of the size of the matrix.
The even case is the [previous mixed-moment theorem](Yin_C_A0097_v1.md#statement).
For example the sufficient power for degree four is three.

## Argument

Fix a column step of the given matrix and let \(x_\sigma\in[0,1]\) be the regular-rank increase after adding that column at embedding \(\sigma\).
For every \(1\le l\le j\) the sum \(\sum_\sigma x_\sigma^l\) is an integer.
The [restriction-of-scalars proof](Yin_C_A0097_v1.md#argument) gives this at each such \(l\) by using products of the two consecutive column prefixes on \(l\) distinct group coordinates and embedding that subgroup in \(G^j\).
The constant sum \(\sum_\sigma1=d\) is also integral.

For \(j=2k\) the nonnegative integer \(\sum_\sigma[x_\sigma(1-x_\sigma)]^k\) is at most \(d/4^k<1\), giving zero as in v1.
For \(j=2k+1\), form the two sums
\[
       I_0=\sum_\sigma x_\sigma^k(1-x_\sigma)^{k+1},
       \qquad
       I_1=\sum_\sigma x_\sigma^{k+1}(1-x_\sigma)^k.
\]
Both are nonnegative integers because the polynomials have integer coefficients and degree \(j\).
If one increment is strictly between zero and one, it contributes positively to both sums, forcing \(I_0+I_1\ge2\).
Yet
\[
          I_0+I_1=\sum_\sigma [x_\sigma(1-x_\sigma)]^k
                      \le d\,4^{-k}<2 .
\]
For \(k=0\) the right-hand summand is the constant polynomial one, including at both endpoints.
This proves in either parity that each increment is zero or one.
Summing over the column steps proves the assertion with the unnormalized trace.

At \(d=2^j\), a list of \(d\) numbers equal to \(1/2\) has integral power sums through \(j\) and a nonintegral sum at \(j+1\).
Thus the two-parity bound reaches the threshold allowed by these moment data alone.
It does not show that a regular group trace can realize those increments under the rational power hypothesis.

## Assessment history

### Decision both-parities

| Field | Value |
| --- | --- |
| date | 2026-11-21T05:13 |
| status | proved |
| reason | Independent review verified the parity argument and the mixed-moment input for every required coordinate count. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The degree-only rational direct-power bound in both parities under all embeddings. |
| argument | [Proof](#argument) | Column increments, the two odd-degree polynomials and the strict moment threshold. |
| review | [Whole finding](../audits/reviews/Yin_R_A0133_v2.md#whole-finding) | Complete proof and applicability of the preceding mixed-moment calculation. |
| dependency | [Mixed moments](Yin_C_A0097_v1.md#decision-number-field-moments) | The integer moments of each column increment by simultaneous restriction of scalars. |

## Current assessment

[Selected decision](#decision-both-parities)

---
author: Yin
---

# Dimension of a minimal linear representation from fraction commutator ranks

This version develops the dimension estimate associated with the [coordinate rank formula in v1](Yin_C_F0371_v1.md#ranks).
The bound for a minimal monic representation is recorded in [C_F0007 v1](Yin_C_F0007_v1.md#exact-coefficient-ranks-and-the-state-dimension-bound).

<a id="statement"></a>
## Statement

Let \(r\ne 0\) be a rational function in the free field on \(x_1,\ldots,x_d\) over \(\mathbb C\).
Let \(r=uA^{-1}v\) be a minimal linear representation of dimension \(n\), with \(A=A_0+\sum_{i=1}^d A_ix_i\).
Then
\[
 \mathbb C^n=\mathbb Cv+\sum_{i=1}^d\operatorname{im} A_i,
 \qquad
 n\le 1+\sum_{i=1}^d\operatorname{rank}_{\mathbb C}A_i.
\]
Under the normal-tuple and dual-system hypotheses of the coordinate rank formula, every fraction pair \(Q\) for \(r(X)\) therefore satisfies
\[
 n\le 1+\sum_{i=1}^d\operatorname{rank}\overline{\Gamma[Q,D_i]}.
\]

<a id="argument"></a>
## Argument

Put \(h=A^{-1}v\).
By [Cohn and Reutenauer, Section 4.2, Proposition 7](../audits/literature/CR94/Yin_U001.md#cr94-u001), minimality gives linear independence of the entries of \(h\) over \(\mathbb C\).
Let \(w\) be a complex row vector annihilating \(\mathbb Cv+\sum_{i=1}^d\operatorname{im} A_i\).
Then \(wv=0\) and \(wA_i=0\) for every \(i\ge 1\), so \(wA_0h=wAh=wv=0\).
Linear independence gives \(wA_0=0\), hence \(wA=0\) and \(w=0\) by invertibility of \(A\).
The subspace thus equals \(\mathbb C^n\), and its dimension is at most \(1+\sum_{i=1}^d\operatorname{rank}_{\mathbb C}A_i\).
Applying the rank formula in v1 gives the estimate for each fraction pair.

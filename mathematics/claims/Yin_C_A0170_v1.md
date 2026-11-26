---
author: Yin
---

# Mixed Schur complements with one nonedge correction in each vertex

## Statement

Let \(V=\ker(\operatorname{SL}_3(\mathbb Z)\to\operatorname{SL}_3(\mathbb F_3))\), \(b=I+3E_{12}\), \(a=I+9E_{13}\), and \(G=V_1*_{\langle b\rangle}V_2\), with one copy of \(V\) at each vertex.
In \(\mathbb CG\) put \(q=a_1+a_2\), \(c=1-b\), and \(p=q+c\).
Choose \(h_j\in V_j\setminus\langle b\rangle\), nonzero \(\alpha,\beta\in\mathbb C\), and any \(L_1,L_2\in\mathbb C[b^{\pm1}]\).
Set \(f_1=\alpha h_1+L_1\), \(g_2=\beta h_2+L_2\), \(u=q+f_1\), and \(v=q+g_2\).
Then
\[
  \operatorname{rk}_G\begin{pmatrix}p&-u\\-v&p\end{pmatrix}=2,\qquad
  p-vp^{-1}u\ \text{is an affiliated unit}.
\]
Here rank uses the unnormalized matrix trace, and the displayed Schur scalar lies in the first inverse layer.
This calculation makes no scalar injectivity assumption on \(\mathbb CG\).
It includes \(h_1=I+15E_{21}\) at the first vertex and \(h_2=I+15E_{32}\) at the second vertex, even though both reduce to the identity modulo five.

## A single prime detecting both corrections

Use the [graph weight spaces of the congruence double](Yin_C_A0165_v1.md#both-cycles-in-the-finite-representation) at a prime \(\ell>3\) chosen below.
Let \(D\) be the image of \(V\) in \(\operatorname{SL}_3(\mathbb F_\ell)\), and let bars denote reduction into this image, identifying each vertex with \(V\).
The subgroup \(K=\langle\bar a,\bar b\rangle\) consists of all \(I+xE_{12}+yE_{13}\) over \(\mathbb F_\ell\), since \(3\) and \(9\) are invertible and the two matrix units have zero pairwise products.
Define \(\chi(I+xE_{12}+yE_{13})=\exp(2\pi i y/\ell)\), using an integer representative for \(y\).
It is trivial on \(\bar b\) and nontrivial on \(\bar a\).

If an integral \(h_j\) is outside the set of matrices \(I+xE_{12}+yE_{13}\), at least one forbidden entry of \(h_j-I\) is a nonzero integer.
For any prime not dividing this integer, \(\bar h_j\notin K\).
If \(h_j=I+xE_{12}+yE_{13}\), both \(x,y\) are divisible by three.
Here \(y\ne0\), since \(I+xE_{12}=b^{x/3}\) is in the edge.
Exclude primes dividing \(y\), so \(\chi(\bar h_j)\ne1\).
There are only finitely many exclusions for the two elements together.
For the stated example one may take \(\ell=7\).

Choose phases \(\eta\) on \(\ell^2(D)\)'s index set by assigning one unit complex number to a representative of each coset \(Kx\), and extending by \(\eta(kx)=\chi(k)\eta(x)\).
Let \(W\delta_x=\eta(x)\delta_x\).
Represent \(V\) by two copies of the finite left regular representation of its reduction, with weight spaces the two graphs \((\xi,\pm W\xi)/\sqrt2\).
Both off-diagonal weight blocks of an element \(h\) are the same weighted permutation
\[
 B(h)=\tfrac12\bigl(\lambda_D(\bar h)-W^*\lambda_D(\bar h)W\bigr).
\]
It is invertible precisely when \(\eta(\bar h x)\ne\eta(x)\) for every \(x\in D\).
Within \(K\) this inequality holds for every element with nontrivial \(\chi\).
For each \(\bar h_j\notin K\), \(K\bar h_jx\ne Kx\) for all \(x\), so every forbidden equality relates two distinct representative phases.
Avoiding a finite union of Haar-null sets of phase choices gives invertible \(B(a),B(h_1),B(h_2)\) simultaneously.
The operator \(W\) commutes with \(\lambda_D(\bar b)\), so every power of \(b\) acts block diagonally.
Conjugating the second vertex representation by \(\operatorname{diag}(zI,I)\) in the graph weight coordinates therefore gives a representation of the whole amalgam for every unit phase \(z\).

## Two triangular vertex corners

In the original two-by-two matrix add column one to column two, then add row one to row two.
These constant operations yield
\[
             M=\begin{pmatrix}p&c-f_1\\c-g_2&2c-f_1-g_2\end{pmatrix}.
\]
Split \(M\) as a left-vertex part and a right-vertex part, assigning all common edge Laurent entries to the left.
In a regular twist the corner contribution of a group element in a vertex is \(\lambda_G(h)\otimes B(h)\).
Every edge Laurent entry has zero off-diagonal corner term by term, including its negative powers.
Writing
\[
 A_j=\lambda_G(a_j)\otimes B(a),\qquad
 H_1=\alpha\lambda_G(h_1)\otimes B(h_1),\qquad
 H_2=\beta\lambda_G(h_2)\otimes B(h_2),
\]
the unbent \(12\) corner for the left vertex and \(21\) corner for the right vertex respectively become
\[
      \begin{pmatrix}A_1&-H_1\\0&-H_1\end{pmatrix},
      \qquad
      \begin{pmatrix}A_2&0\\-H_2&-H_2\end{pmatrix}.
\]
Their diagonal blocks are boundedly invertible, so each corner has regular rank \(2|D|\).
Applying the [two-corner inequality](Yin_C_A0123_v1.md#statement) to the genuine amalgam representation family gives \(2|D|\operatorname{rk}_G M\ge4|D|\).
Thus \(M\) and the original matrix both have rank two.
The [mixed denominator calculation](Yin_C_A0121_v1.md#the-regular-rank-computation) gives that \(p\) is an affiliated unit.
Eliminating the first diagonal entry of the original matrix now proves that \(p-vp^{-1}u\) is a unit in the affiliated algebra.
Only \(p^{-1}\) is needed to form this scalar.

## Assessment history

### Decision prime-separating-corrections

| Field | Value |
| --- | --- |
| date | 2026-11-26T03:47 |
| status | proved |
| reason | Independent review verified the complete argument and its stated hypotheses. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Full regular rank with one nonedge correction in each vertex. |
| argument | [Prime and phases](#a-single-prime-detecting-both-corrections) | Simultaneously visible weighted permutations and the edge Laurent terms. |
| argument | [Vertex ranks](#two-triangular-vertex-corners) | Two constant operations, triangular corners and the ordered Schur complement. |
| review | [Prime separating corrections](../audits/reviews/Yin_R_A0175_v1.md#prime-separating-corrections) | Independent whole-argument finding on the stated result. |

## Current assessment

[Selected decision](#decision-prime-separating-corrections)

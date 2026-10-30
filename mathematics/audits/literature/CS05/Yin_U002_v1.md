---
author: Yin
---
# CS05 Hilbert–Schmidt tensor identification

## CS05-U002

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | [Retained arXiv:math/0309343v1](../../../literature/pdf/CS05--arxiv-v1.pdf), 20 September 2003, 39 pages; artifact identity is recorded in the registry (private lookup: `../../../literature/registry.md#cs05-source-artifact`). The same notation passage was read in the [author-hosted copy](https://alainconnes.org/wp-content/uploads/betti.pdf). |
| source-locator | Section 1.1, printed/PDF p. 3, equations (1.1)–(1.2) and the intervening Hilbert–Schmidt isometry statement. No identity of pagination with the journal version is asserted. |
| inspection | 2026-10-18. The authoring agent for Yin read the specified passage directly and checked the rank-one formula, Hilbert-space extension and four action identities. This is a scoped source inspection, not an independent project review or a full-paper audit. |

## Tensor identification and actions

<a id="tracial-tensor-identification"></a>
Let \(M\) be the von Neumann algebra in the source's tracial GNS representation, with trace \(\tau\), Hilbert space \(H=L^2(M,\tau)\) and Tomita conjugation \(J\).
The source writes \(M^o\) for the opposite algebra, \(\operatorname{FR}(H)\) for bounded finite-rank operators and \(\operatorname{HS}(H)\) for Hilbert–Schmidt operators.
Its tensor sign \(\otimes\) is algebraic, while \(\bar\otimes\) denotes the appropriate completion.
Equation (1.1) defines
\[
 \Psi:M\otimes_{\mathbb C}M^o\longrightarrow\operatorname{FR}(H),
 \qquad
 \Psi(x\otimes y^o)\xi:=x\,\tau(y\xi)
 \quad(x,y\in M,\ \xi\in H).
\]
Here \(\tau\) on \(H\) means its continuous extension from the tracial GNS space, and the output \(x\) is its GNS vector.
With the inner product linear in the second variable, the same formula is \(\Psi(x\otimes y^o)\xi=x\langle Jy,\xi\rangle\).
The following source sentence states that \(\Psi\) extends to an isometric isomorphism
\[
 L^2(M\bar\otimes M^o)\longrightarrow\operatorname{HS}(H).
\]
Under the product-trace identification, its domain is \(L^2(M)\bar\otimes L^2(M^o)\).

Equation (1.2) identifies four operator actions with tensor-factor actions.
For \(a,x,y\in M\), they are
\[
 \begin{aligned}
  a\Psi(x\otimes y^o)&=\Psi(ax\otimes y^o),&
  \Psi(x\otimes y^o)a&=\Psi(x\otimes(ya)^o),\\
  (Ja^*J)\Psi(x\otimes y^o)&=\Psi(xa\otimes y^o),&
  \Psi(x\otimes y^o)(Ja^*J)&=\Psi(x\otimes(ay)^o).
 \end{aligned}
\]
These identities extend to the completed tensor space by continuity of the bounded actions.

## Inspection and mathematical boundary

The rank-one norm is \(\|\Psi(x\otimes y^o)\|_{\mathrm{HS}}=\|x\|_2\|y\|_2\); the corresponding inner-product calculation gives the stated Hilbert-space isometry.
The checked rank-one formula extends to arbitrary vectors in the two \(L^2\) factors, and its algebraic tensor restriction is a linear bijection onto \(\operatorname{FR}(H)\), by the usual finite-rank decomposition into rank-one operators.
This last restriction uses algebraic tensors of \(L^2\) vectors; equation (1.1) does not assert that bounded tensors \(M\otimes M^o\) exhaust all finite-rank operators.
The four action identities were checked directly from the source formula, traciality and \(Ja^*J\xi=\xi a\).
The inspection uses the standard Hilbert-space rank-one and Hilbert–Schmidt facts and does not audit their foundational proofs.
No statement about separately continuous bilinear forms or equality of their ranks with operator ranks is attributed to this source passage.

---
author: Yin
---

# Matrix transfer across a finite window and its exact rank endpoint

## Statement

Let \(K\le G\) be discrete groups and \(s\in G\).
Write \(U(K),U(G)\) for their regular affiliated algebras and write \(\dim_G\) for the dimension of an affiliated right module with the unnormalized matrix trace.
For \(m\ge2\) use the [finite window](Yin_C_A0181_v1.md#statement)
\[
 K_m=\langle s^i K s^{-i}:0\le i\le m-2\rangle,\qquad
 r=\big|\{K_m s^i:0\le i<m\}\big|.
\]
Put \(S_h=sI_h\).
For \(h\ge1\) and \(M\in M_h(U(K))\), one has
\[
                 \dim_G\ker(S_h-M)\le h/r.
\]
If \(r\ge2\) and equality holds, then \(C=S_h^{-1}M\) satisfies \(C^r=I_h\).
For every \(r\)-th root of unity \(\omega\), the kernel of \(C-\omega I_h\) has dimension \(h/r\).
The bound and endpoint apply to an affiliated transfer matrix without requiring bounded entries or even invertibility of \(M\) in advance.

In particular take \(h=2,\ K=\langle t\rangle\) with \(t\) of infinite order, and \(M\in{\rm GL}_2(\mathbb C(t))\), evaluated at the regular group translation \(t\).
If \(r\ge5\), the intersection of the two graphs of \(M\) and \(sI_2\) cannot have dimension \(1/2\).
At \(r=4\) this dimension forces \(C^4=I_2\), with each of the four eigenspaces of dimension one half.
The cyclic field embeds in \(U(K)\), since every nonzero Laurent polynomial vanishes only on a Haar-null subset of the circle.
These assertions concern a particular transfer matrix and its intersection with the group-translation graph.

## Closed relations with coordinate kernels

More generally let \(P\in M_{2h}(\mathcal N(K))\) be an orthogonal projection, and denote its affiliated range by \(W\) over \(U(G)\).
Put \(t_W=\dim_G W\) and define
\[
 d_v=\dim_G\{x:(0,x)\in W\},\qquad
 d_h=\dim_G\{x:(x,0)\in W\}.
\]
If \(r\ge2\), then
\[
 \dim_G\{x:(x,S_hx)\in W\}
       \le \frac{t_W+(r-2)\min(d_v,d_h)}{r}.                 \tag{1}
\]
Thus a plane with vertical or horizontal coordinate kernel zero retains the \(t_W/r\) bound.
Formula (1) accounts for the possible extra directions when both coordinate maps have a kernel.

In the sequence of cosets in the statement, \(K_ms^i=K_ms^j\) is equivalent to \(s^{i-j}\in K_m\).
The differences satisfying that condition form a subgroup of \(\mathbb Z\), so the first \(r\) cosets are pairwise distinct, even if there are later collisions.
On \(r\) consecutive \(h\)-coordinate blocks impose the equations
\[
          (x_i,x_{i+1})\in W_i,\qquad
          W_i=(s^i I_{2h}) W,\qquad 0\le i\le r-2 .
\]
The projection onto \(W_i\) is \(s^iP s^{-i}\) entrywise, hence the projection \(Q\) onto the joint solutions belongs to \(M_{rh}(\mathcal N(K_m))\).
Indeed \(Q\) is the kernel projection of the bounded matrix formed by applying the complementary projections to adjacent pairs.
The first pair has solution dimension \(t_W\).
At each additional coordinate, forgetting that coordinate maps into the preceding solution space and has kernel of dimension \(d_v\), using the new pair with first coordinate zero.
Hence \(\operatorname{Tr}Q\le t_W+(r-2)d_v\).
Reading the same equations from the other end gives the bound with \(d_h\).

Let \(V\) be the range projection of the isometry \(r^{-1/2}(I_h,S_h,\ldots,S_h^{r-1})^{\mathsf T}\), using the displayed notation for stacked blocks.
When \((x,S_hx)\in W\), the sequence \(x_i=S_h^i x\) satisfies all the equations.
Therefore its solution dimension is at most \(\operatorname{Tr}(Q\wedge V)\le\operatorname{Tr}(QV)\), since \(QVQ\) dominates the meet.
The \((i,j)\) block of \(V\) is \(s^{i-j}I_h/r\).
Trace pairings of all off-diagonal terms with entries of \(Q\) vanish by Fourier support and distinctness of the first \(r\) cosets.
The diagonal terms give \(\operatorname{Tr}(QV)=\operatorname{Tr}Q/r\), proving (1).

## Transfer matrices and equality

Use the graph \(W=\{(x,Mx):x\in U(G)^h\}\).
It has affiliated dimension \(h\) and \(d_v=0\).
Its orthogonal graph projection has entries in \(\mathcal N(K)\), as the support of the affiliated column over \(U(K)\) with blocks \(I_h,M\).
The range of the latter column in affiliated modules equals its support module by the relative inverse.
Thus (1) gives \(h/r\) for \(r\ge2\), while \(r=1\) follows directly from the domain dimension.

For the graph case, writing \(M_i=S_h^i M S_h^{-i}\), the successive equations are \(x_{i+1}=M_i x_i\).
Each initial coordinate defines a unique solution in the affiliated module, of the form
\[
                x_i=S_h^i C^i x_0,\qquad C=S_h^{-1}M .
\]
This follows by induction in the displayed order, since \(M_i S_h^i=S_h^i M\).
In particular \(\operatorname{Tr} Q=h\).
At equality, \(\operatorname{Tr}(Q\wedge V)=\operatorname{Tr}(QV)=h/r\), so \(QVQ=Q\wedge V\) by faithfulness.
Since the meet reduces both projections, \(V(Q-Q\wedge V)=0\), giving \(QV=VQ\).

Conjugate by the block unitary with diagonal entries \(S_h^{-i}\).
The image of \(Q\) becomes the module of sequences \((C^i x_0)_{0\le i<r}\), and \(V\) becomes the projection averaging the coordinates onto the constant sequences.
By commutation, averaging any such solution again gives a solution.
Its constant coordinate must be fixed by \(C\), since \(r\ge2\).
Thus \((C-I_h)\sum_{i=0}^{r-1}C^i=0\), and \(C^r=I_h\).
The scalar interpolation idempotents for the \(r\) distinct roots of \(z^r-1\) now decompose \(U(G)^h\) as the algebraic direct sum of the right eigenspaces.
For each such root \(\omega\) the transfer bound applied to \(\omega^{-1}M\) gives \(\dim_G\ker(C-\omega I_h)\le h/r\).
Their dimensions add to \(h\), so each equals \(h/r\).
This argument uses the algebraic direct sum even when the eigenspaces are not mutually orthogonal.

## Assessment history

### Decision matrix-window

| Field | Value |
| --- | --- |
| date | 2026-11-26T04:23 |
| status | proved |
| reason | The independent review verified the full argument under the specified assumptions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Window bound and the equality condition. |
| argument | [Closed relations with coordinate kernels](#closed-relations-with-coordinate-kernels) | Two coordinate defects and actual coset trace. |
| argument | [Transfer matrices and equality](#transfer-matrices-and-equality) | Unbounded graphs and the complete family of eigenspaces. |
| review | [Matrix window](../audits/reviews/Yin_R_A0179_v1.md#matrix-window) | Independent review of the stated result and its argument. |

## Current assessment

[Selected decision](#decision-matrix-window)

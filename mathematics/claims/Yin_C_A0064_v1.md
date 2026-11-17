---
author: Yin
---

# A finite return moment bounds the kernel tail without finitely supported null vectors

## Statement

Fix one finitely generated group \(G\) with word length \(|\cdot|\), and let \(u,v\) freely generate a subgroup of rank two.
This includes individual four-line groups on the [free-subalphabet event](Yin_C_A0059_v1.md#statement), also in its indicated no-\(C_{21}\) family.
Let \(V\) be the uniform probability on the identity and a finite symmetric generating set of distinct nonidentity elements of \(G\).
For each integer \(d\ge1\) put
\[
 T=\begin{pmatrix}1&-V&0\\0&1-u&1-v\end{pmatrix},
 \qquad A=\operatorname{diag}(1,(1-u)^d)\,T.
\]
The rational group-ring matrix \(A\) has nonclosed range and its kernel has von Neumann dimension one.
Its kernel contains no nonzero finitely supported vector.
The supports of \(A\) and its actual kernel projection \(p\) each require the whole group even after independent translations of rows and columns.

Let \(w\ge1\) be any integer bounding the word lengths in \(T\).
Put \(\gamma=4-2\sqrt3\), \(c=(1+2/\sqrt{\gamma})^{-2}\), \(M=16\), \(H=I_2-TT^*/M\) and \(\theta=1-c/M\).
For any real \(\beta\ge0\) and integer \(k\ge0\) one finite return moment \(t_k=\tau_2(H^{2k})\), with the unnormalized matrix trace, gives
\[
 \sum_{|g|>2kw}(1+|g|)^\beta\|\widehat p(g)\|_{\mathrm{HS}}^2
 \ \le\ t_k\sum_{j\ge0}(1+2(k+j+1)w)^\beta\theta^{2j}.                 \tag{1}
\]
This gives a bound outside every prescribed radius \(R\ge0\) by taking \(k=\lfloor R/(2w)\rfloor\).
It also gives exponential square localization, with any exponential spatial weight \(e^{a|g|}\) such that \(e^{2aw}\theta^2<1\).
The [corrected criterion using the powers of \(I-A^*A/M'\)](Yin_C_A0062_v1.md#statement) applies to this same nonclosed-range input with positive spectral exponent \(1/(2d)\) at zero.

## The row map and its kernel

On the right cosets of \(\langle u,v\rangle\), the translates by left multiplication give copies of the four-regular tree.
For \(D=(1-u,1-v)\), the Gram operator \(DD^*=4I-u-u^{-1}-v-v^{-1}\) is at least \(\gamma I\).
For example, orient each such tree toward one end, so that each vertex has one parent and three children.
For each edge from a parent to a child, use \(2|ab|\le |a|^2/\sqrt3+\sqrt3|b|^2\) with \(a\) at the parent.
Summing gives the adjacency form bound \(2\sqrt3\) on finitely supported functions and then on their Hilbert space closure.
The right inverse \(D^*(DD^*)^{-1}\) has norm at most \(1/\sqrt\gamma\).
For a target \((z_1,z_2)\) take \((b,h)=D^*(DD^*)^{-1}z_2\) and \(a=z_1+Vb\).
This gives a right inverse to \(T\) with norm at most \(1+2/\sqrt\gamma\).
Thus \(TT^*\ge cI_2\).
Also \(TT^*\le10I_2\), since the two rows have squared norm at most \(2\) and \(8\), respectively.

The element \(u\) has infinite order, so \(1-u\) is injective with dense nonclosed range by Fourier transform on each right coset of \(\langle u\rangle\).
The same holds for its \(d\)-th power.
Surjectivity of \(T\) gives \(\operatorname{ran} A=\ell^2(G)\oplus\operatorname{ran}(1-u)^d\), and injectivity of its left factor gives \(\ker A=\ker T\).
The kernel therefore has dimension \(3-2=1\).
For a finitely supported kernel vector, \(D(b,h)=0\) gives a finitely supported flow of zero divergence on a disjoint union of trees.
A leaf in the finite subforest of edges with nonzero coefficients rules out a nonzero flow, so \(b=h=0\) and then \(a=Vb=0\).
In particular projections onto the null vectors supported in any given finite ball are all zero.

## Recovering the generating polynomial from the projection

Let \(E\) take the second coordinate on \(\ker T\).
If \(E(a,b,h)=0\), the equations give \(a=0\) and \((1-v)h=0\), so \(E\) is injective.
Its domain and codomain both have von Neumann dimension one.
The polar decomposition and faithfulness of the trace therefore give dense range.
Consequently \(p_{22}=EE^*\) is positive and injective, with strictly positive identity coefficient.
It has no bounded inverse.
Indeed a lower bound on \(EE^*\) would give a bounded right inverse to \(E\), forcing \(1-u=(1-v)L\) for a bounded operator \(L\) by the second row equation.
Then \(\gamma I\le DD^*\le(1+\|L\|^2)(1-v)(1-v)^*\), impossible on the infinite cyclic cosets of \(v\).

Suppose all translated entries \(g_i p_{ij}h_j\) belong to the group von Neumann algebra of a subgroup \(K\).
The identity coefficient just found gives \(g_2h_2\in K\).
Thus \(C=h_2^{-1}p_{22}h_2\) belongs to that algebra and is injective.
The relation \(p_{12}=Vp_{22}\) follows from the first row equation.
Writing \(Z=g_1Vh_2\) gives \(ZC\in\mathcal N(K)\).
The bounded elements \(ZC(C+\varepsilon I)^{-1}\) belong to \(\mathcal N(K)\) and converge strongly to \(Z\).
Its support contains \(g_1h_2\) and all \(g_1 s h_2\) for the chosen generators \(s\).
Taking differences gives the conjugated generating set \(h_2^{-1}s h_2\) in \(K\), hence \(K=G\).
The input gives this conclusion directly from its entry \(-V\).

## A tail estimate from one finite moment

The coisometry in the left polar decomposition \(T=(TT^*)^{1/2}U\) satisfies \(UU^*=I_2\) and \(U^*U=I_3-p\).
For \(k\ge0\) set
\[
 p^{(k)}= I_3-M^{-1}T^*\sum_{\ell=0}^{k-1}H^\ell T .
\]
This polynomial has propagation at most \(2kw\), with empty sum when \(k=0\).
The finite geometric series gives \(p^{(k)}-p=U^*H^kU\).
Hence its squared trace norm in \(L^2\) is exactly \(t_k\).
In coefficients \(t_k=\sum_{g\in G}\|\widehat{H^k}(g)\|_{\rm HS}^2\).
To compute it, multiply the finite coefficient arrays, sum all amplitudes with the same endpoint in the fixed group, then square and sum.
All these endpoints have length at most \(2kw\).

On the shell \(2\ell w<|g|\le2(\ell+1)w\), the squared coefficient mass of \(p\) is at most \(t_\ell\), by the propagation of \(p^{(\ell)}\).
The Gram bounds give \(0\le H\le\theta I_2\), so \(t_{k+j}\le\theta^{2j}t_k\), and \(t_k\le2\theta^{2k}\).
Summing the shells proves (1) and the exponential version.
The computation uses a gapped row operator with the same kernel as \(A\).
Existence of such a row operator for a general nonclosed-range matrix on a four-line group remains open.

Finally \(c\,\operatorname{diag}(1,|1-u|^{2d})\le AA^*\le 10\,\operatorname{diag}(1,|1-u|^{2d})\) by congruence with the diagonal factor.
The positive spectral mass of \(|1-u|^{2d}\) below \(t\) is comparable to \(t^{1/(2d)}\) at zero, by the circle multiplier \(|1-e^{is}|^{2d}\).
The variational bounds on spectral distribution functions and the polar decomposition of \(A\) transfer this exponent to the positive part of \(A^*A/M'\) for any \(M'>\|A\|^2\).
For \(3<\beta<4\), the series of original endpoint moments and return increments in [C62](Yin_C_A0062_v1.md#argument) therefore converges on geometric schedules \(k_j\asymp2^{\kappa j}\) exactly when \(\kappa>2d\beta\).

## Assessment history

### Decision finite-return-tail

| Field | Value |
| --- | --- |
| date | 2026-11-17T10:56 |
| status | proved |
| reason | Independent review verified the whole-group support, the absence of finite null vectors, the exact return error and the weighted estimate on all exterior shells. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Fixed groups with a free pair, nonclosed range, unrestricted coordinate translations and control beyond every radius. |
| argument | [Proof](#the-row-map-and-its-kernel) | Tree Gram bound, support recovery with a dense-range coordinate, shell estimate and original spectral exponent. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0100_v1.md#whole-argument-finding) | Independent review of the construction and bound, with the established schedule criterion used at its stated scope. |

## Current assessment

[Selected decision](#decision-finite-return-tail)

---
author: Yin
---

# Trace-class and graph BMO obstructions for a normalized mixed-word test

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(S,T\) be freely independent variance-one semicircular elements with trace \(\tau\), \(M=W^*(S,T)\), \(\mu\) the law of \(S\), and \(H=L^2(\mu)\).
Use the free difference quotient \(\partial_S S=1\otimes1,\ \partial_S T=0\), the right slice \(C=\mathrm{id}\otimes\tau\), and the inner product linear in its second variable.
Write \(v_n(s)=T_n(s/2)\), where \(T_n\) is the usual Chebyshev polynomial of the first kind.
For \(n\ge3\) take the length-one polynomial column \(p_n=(T/2)v_n(S)\) and the Hilbert test \(q=T\).
Then \(\|p_n\|\le1,\ \|q\|_2=1\).

1. The nuclear norm of the coarse tensor \(\partial_Sp_n\), identified with an operator from the conjugate of its second Hilbert leg to its first, is at least \(n/4\), although
   \[
       \|C\partial_Sp_n\|_2=1/(2\sqrt2).
   \]
   For every bounded measurable marginal symbol \(K\) the actual sliced pairing is
   \[
       \langle q,CI_K\partial_S p_n\rangle
          =\operatorname{Tr}(O_K B_n),\qquad
       B_n=\tfrac12 O_{H_n},\quad
       H_n(s,t)=\frac{v_n(s)-v_n(t)}{s-t}.
       \tag{1}
   \]
   Here \(O_k\) denotes the integral operator with kernel \(k(s,t)\) on \(H\), and the diagonal can be set to zero.
   The inner marginal action \(I_{v\otimes w}\) sends \(a\otimes b\) to \(av(S)\otimes w(S)b\).
   The test operator \(B_n\) is real symmetric of rank at most \(n\), with \(\|B_n\|_1\ge n/4\).
2. For every real Lipschitz \(g\) on \([-2,2]\), set \(h(s)=s+i g(s)\) and use the graph heat semigroup \(\mathcal T_t\) on \(B(H)\) with symbol \(e^{-t|h(s)-h(u)|^2}\).
   Use its column and row variance seminorms as defined in the argument.
   There are selfadjoint rank-\(n\) contractions \(J_n\) tending to zero under this semigroup as \(t\to\infty\) for each fixed \(n\), with both variance seminorms at most one and
   \[
      \operatorname{Tr}(J_n B_n)=n/4 .
      \tag{2}
   \]
   There are also rank-\(n\) tests \(W_n\) with weak trace-class quasinorm one and
   \[
       \operatorname{Tr}(W_n B_n)=\tfrac14\sum_{j=1}^{n}\frac1j .
       \tag{3}
   \]
   Thus the normalized mixed-word functional in (1), tested on these entire variance or weak trace-class unit balls, has no bound independent of degree.
3. For the actual inverse secant \(K_h(s,t)=(s-t)/(h(s)-h(t))\) of each fixed such graph, write \(\xi_h\in L^2(h_*\mu)\) for the scalar conjugate variable of \(h(S)\).
   In contrast to the growing unit-ball tests, the corresponding pairings satisfy
   \[
       \sum_{n\ge3}\left|\langle q,CI_{K_h}\partial_Sp_n\rangle\right|^2
       \le \tfrac14\|\xi_h\|_2^2 .
       \tag{4}
   \]
   The obstruction concerns enlargement of the test class; these particular words do not obstruct column control for the actual graph family.

## Argument

### The two anti-diagonals and the mixed-word pairing

Use the orthonormal monic polynomials \(u_0=1,\ u_1=s,\ u_{k+1}=su_k-u_{k-1}\) of the variance-one semicircle law. [Semicircular Wick basis](../audits/literature/Miy22/Yin_U001.md#miy22-u001)
Writing \(s=2\cos\theta\) gives \(u_k(s)=\sin((k+1)\theta)/\sin\theta\) in the interior of the support and \(v_n=(u_n-u_{n-2})/2\).
This also gives \(\|v_n(S)\|\le1\); the semicircle support gives \(\|T\|=2\).
The divided difference of \(u_n\) is \(\sum_{i+j=n-1}u_i(s)u_j(t)\): expansion of the generating function \((1-sz+z^2)^{-1}\) shows that its divided difference is \(z\) times the product of the two generating functions.
The same divided difference is the represented free difference quotient by the Leibniz rule.
Hence
\[
  H_n=\tfrac12\left(\sum_{i+j=n-1}u_i\otimes u_j-\sum_{i+j=n-3}u_i\otimes u_j\right).
\]
For \(m\ge1\) let \(J_m u_j=u_{m-1-j}\) for \(0\le j<m\) and \(J_m u_j=0\) for \(j\ge m\).
In this real basis the two sums have integral operators \(J_n,J_{n-2}\) on the same space \(H\), supported on disjoint matrix anti-diagonals.
Thus \(O_{H_n}=(J_n-J_{n-2})/2\); its pairing with the operator-norm contraction \(J_n\) equals \(n/2\).
In particular \(n/2\le\|O_{H_n}\|_1\le n-1\) and \(\|O_{H_n}\|\le1\).

Put \(a=T/2\). For \(f_1,f_2\in H\), freeness and \(\tau(T^2)=1\) give
\(\langle a f_1(S),a f_2(S)\rangle=\langle f_1,f_2\rangle/4\), initially for bounded functions and then by density.
The tensor \(\partial_Sp_n=a\cdot H_n\) therefore has exactly half the nuclear norm of \(O_{H_n}\).
In this identification the second legs \(u_j\) are real: \(u_i\otimes u_j\) acts on \(H\) by \(f\mapsto u_i\langle u_j,f\rangle\), after identifying the conjugate input space by pointwise conjugation.
Slicing on the right keeps precisely the terms indexed by \(j=0\).
The output is \(a(u_{n-1}-u_{n-3})(S)/2\) and has the asserted Hilbert norm.

For \(K(s,t)=v(s)w(t)\), the pairing with \(q=T\) has left factor \(\tau(T a u_i(S)v(S))=\tfrac12\int u_i v\,d\mu\) on the term indexed by \(i,j\), and right factor \(\int w u_j\,d\mu\).
These terms sum to \(\tfrac12\iint K(s,t)H_n(s,t)\,d\mu(s)d\mu(t)\).
The identity extends to bounded measurable \(K\) by \(L^2(\mu^2)\) approximation by finite sums of bounded product functions: \(H_n\) is bounded for fixed \(n\), and multiplication on the first leg by \(a\) and the slice are bounded Hilbert-space maps.
In fact the pairing is continuous in that \(L^2\) norm.
The ordinary trace of the product of two integral Hilbert–Schmidt operators uses the bilinear integral of the first kernel at \((s,t)\) and the second at \((t,s)\).
Since \(H_n\) is real symmetric this proves (1) for complex symbols with exactly the displayed ordering.

### Heat variances and weak trace-class tests

On \(B(H)\) define \(\mathcal T_t\) by averaging conjugations by the multiplication unitaries \(e^{i\zeta\cdot(\operatorname{Re}h,\operatorname{Im}h)}\) against the centered Gaussian probability of covariance \(2t I_2\), using the identity at \(t=0\).
This gives a normal unital completely positive semigroup, and its action on Hilbert–Schmidt kernels is exactly the multiplier in the statement by the Gaussian characteristic function.
Define the column variance seminorm of \(V\) as \(\sup_{t\ge0}\|\mathcal T_t(V^*V)-\mathcal T_t(V)^*\mathcal T_t(V)\|^{1/2}\), and define the row seminorm by applying it to \(V^*\).
These are the [graph heat variance expressions](../audits/literature/CJSZ20/Yin_U001.md#graph-heat-semigroup-and-bmo); here their values on the displayed finite-rank operators follow directly on \(B(H)\).
Complete positivity and unitality put the variance between zero and \(\|V\|^2 I\).
Both seminorms of \(J_n\) are consequently at most one.
Diffuseness of \(\mu\) and injectivity of \(h\) imply that the heat factor tends to zero \(\mu^2\)-almost everywhere, so \(\mathcal T_t(J_n)\to0\) in Hilbert–Schmidt norm for fixed \(n\).
Testing on \(J_n\) now gives (2).

Let \(D_n u_j=(j+1)^{-1}u_j\) for \(0\le j<n\), zero otherwise, and take \(W_n=J_nD_n\).
Its nonzero singular values in decreasing order are \(1,1/2,\ldots,1/n\), giving \(\sup_{1\le k\le n} k s_k(W_n)=1\) in the [weak trace-class convention](../audits/literature/CSZ18/Yin_U001.md#weak-endpoint-for-the-planar-symbol).
The traces of \(W_nJ_n\) and \(W_nJ_{n-2}\) are respectively \(\operatorname{Tr}D_n\) and zero, the latter because the two matrix anti-diagonals do not meet.
Taking the trace against \(B_n=(J_n-J_{n-2})/4\) proves (3).
The operators in (2) and (3) have bounded finite polynomial kernels for each \(n\), so (1) indeed tests them.
They need not be inverse secants of graphs.

### The actual graph pairing

The standard semicircle has scalar conjugate variable \(S\), as follows on the above basis by taking both traces in \(\partial_Su_k\).
The [Lipschitz graph vacuum theorem](Yin_C_F0244_v1.md#statement), item 3 at one coordinate, gives \(\xi_h\).
On the graph write \(y=h(s)\) and use the polynomial \(b_n(y,\bar y)=v_n((y+\bar y)/2)\).
Its value is exactly \(v_n(s)\) because \(\operatorname{Re}h(s)=s\).
The scalar divided difference of \(b_n\) is \(K_h(s,t)H_n(s,t)\) almost everywhere.
Formula (1) and the actual marginal vacuum identity now give
\[
    \langle q,CI_{K_h}\partial_Sp_n\rangle
       =\tfrac12\langle \xi_h\circ h,v_n\rangle_{L^2(\mu)} .
\]
Writing \(d_j=\langle\xi_h\circ h,u_j\rangle\), the right side is \((d_n-d_{n-2})/4\).
The triangle inequality for the two shifted coefficient sequences and Bessel's inequality give (4).
This proves decay along the chosen tests for every fixed graph and leaves the uniform estimate over all mixed columns open.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T11:25 |
| status | open |
| reason | Fix the mixed-polynomial obstructions and the exact inverse-secant comparison for independent inspection. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Normalized mixed column, actual Hilbert test, trace and heat variance bounds, weak endpoint obstruction and decay for fixed graph symbols. |
| argument | [Argument](#argument) | Chebyshev anti-diagonals, freeness, the integral trace pairing, Gaussian conjugation action, weighted flip and original scalar vacuum. |
| dependency | [Semicircular Wick basis](../audits/literature/Miy22/Yin_U001.md#miy22-u001) | Variance-one trace, freeness and the normalized polynomial basis used for both tensor legs. |
| dependency | [Graph heat variance](../audits/literature/CJSZ20/Yin_U001.md#cjsz20-u001) | Row and column variance conventions; the required semigroup and finite-rank estimates are verified directly. |
| dependency | [Weak trace-class endpoint](../audits/literature/CSZ18/Yin_U001.md#csz18-u001) | Weak singular-value norm convention and the endpoint whose arbitrary tests are being compared. |
| dependency | [Lipschitz graph vacua](Yin_C_F0244_v1.md#statement) | Item 3 gives existence of the actual scalar conjugate variable on each fixed graph of the semicircle. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T11:36 |
| status | proved |
| reason | Adopt the mixed-word trace, variance and weak trace-class obstructions and the comparison with fixed genuine graph symbols after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Normalized mixed column, actual Hilbert test, trace and heat variance bounds, weak endpoint obstruction and decay for fixed graph symbols. |
| argument | [Argument](#argument) | Chebyshev anti-diagonals, freeness, the integral trace pairing, Gaussian conjugation action, weighted flip and original scalar vacuum. |
| dependency | [Semicircular Wick basis](../audits/literature/Miy22/Yin_U001.md#miy22-u001) | Variance-one trace, freeness and the normalized polynomial basis used for both tensor legs. |
| dependency | [Graph heat variance](../audits/literature/CJSZ20/Yin_U001.md#cjsz20-u001) | Row and column variance conventions; the required semigroup and finite-rank estimates are verified directly. |
| dependency | [Weak trace-class endpoint](../audits/literature/CSZ18/Yin_U001.md#csz18-u001) | Weak singular-value norm convention and the endpoint whose arbitrary tests are being compared. |
| dependency | [Lipschitz graph vacua](Yin_C_F0244_v1.md#statement) | Item 3 gives existence of the actual scalar conjugate variable on each fixed graph of the semicircle. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0258_v1.md#finding) | All three assertions, the quantitative finite-rank tests, both variance seminorms and the square sum for each actual inverse secant. |

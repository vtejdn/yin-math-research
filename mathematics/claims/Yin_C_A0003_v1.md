---
author: Yin
---
# Energy and regular-transport certificates for bordered matrix rank

Date: 2026-11-11 (Asia/Hong_Kong).
This argument serves [Yin_T_A0001](../tasks/Yin_T_A0001_v1.md#contract) through the [bordered linear-matrix criterion](../ledger/Yin_L_A0004_v1.md#setting-and-exact-criteria).
The main research agent and a development delegate derived the bounded energy argument and its cyclic and finite-graph certificates for Yin.
These are explicit sufficient rank conditions for structured matrices over arbitrary torsion-free groups, with no claim of a new positive group class or historical priority.
Provenance: project deduction using the stated finite-affiliated foundations, with the connection-Laplacian source used for attribution and comparison.

## Statement

### Weighted energy criterion

Let \((M,\tau)\) be a finite von Neumann algebra with a faithful normal tracial state, acting on \(\mathcal H=L^2(M,\tau)\), and put \(U=\mathcal U(M)\).
Use the unnormalized trace \(\operatorname{Tr}_n\otimes\tau\) for matrix ranks and kernel dimensions.
Let \(N\geq1\), \(L\in M_N(M)\), \(W\in M_N(\mathbb C)\) be positive definite, \(0\ne v\in M_{N,1}(\mathbb C)\), and \(\gamma\in\mathbb C^\times\).
Set
\[
u=\gamma v^*W,\qquad
H=\operatorname{Re}(WL)=\frac{WL+L^*W}{2},\qquad
Q=\begin{pmatrix}0&u\\v&L\end{pmatrix}.
\]
If
\[
H\geq0,\qquad \ker H\cap\ker u=\{0\}
\quad\text{in }\mathcal H^N,
\tag{E}
\]
then
\[
\ker Q=\{0\},\qquad
\operatorname{rk}_M Q=N+1,\qquad
Q\in GL_{N+1}(U).
\tag{1}
\]
If, in addition, \(L\in GL_N(U)\), then \(r=uL^{-1}v\) is a unit of \(U\).
For a unital complex subalgebra \(B\subset M\) containing the entries of \(L\), both \(r\) and \(r^{-1}\) then belong to \(\operatorname{Rat}_U(B)\).
The stronger assumption \(H\geq0\) and \(\ker H=\{0\}\) implies \(L\in GL_N(U)\) independently, so in that case all conclusions hold without a separate denominator-invertibility premise.
Condition (E) alone does not assert invertibility of \(L\).
No positive lower spectral bound for \(H\), bounded inverse of \(L\), or bounded inverse of \(Q\) is asserted.

### Cyclic certificate

Let \(G\) be torsion-free, \(M=\mathcal N(G)\), and let \(g_j\in G\setminus\{e\}\), \(\zeta_j\in\mathbb T\), and \(C_j\in M_{m_j,N}(\mathbb C)\) for \(1\leq j\leq m\), where \(m,m_1,\ldots,m_m\) are positive integers.
Complex matrices act on the coordinate factor and commute with the indicated scalar group operators.
Define
\[
\Delta_j
=2-\zeta_j\lambda(g_j)-\overline{\zeta_j}\lambda(g_j^{-1}),
\qquad
H_C=\sum_j C_j^*C_j\,\Delta_j,
\qquad
K_C=\bigcap_j\ker_{\mathbb C} C_j.
\]
Then \(H_C\) is a positive affine group pencil and
\[
\ker H_C=K_C\otimes\ell^2(G),\qquad
\operatorname{rk}_G H_C=N-\dim_{\mathbb C}K_C.
\tag{2}
\]
If \(H=\operatorname{Re}(WL)=H_C\), condition (E) is equivalent to the finite complex-matrix condition
\[
\operatorname{rank}_{\mathbb C}
\begin{pmatrix}C_1\\\vdots\\C_m\\u\end{pmatrix}=N.
\tag{3}
\]
If the stack of the \(C_j\) without \(u\) has column rank \(N\), then \(H_C\) is injective and denominator invertibility is automatic.
If only the augmented stack in (3) has column rank \(N\), conclusion (1) still holds, but the rational Schur conclusion requires \(L\in GL_N(U)\) separately.
One explicit family is
\[
L=W^{-1}(H_C+iK),\qquad u=\gamma v^*W,
\]
where \(K=K^*\) is any affine group pencil of size \(N\).
No commutation between \(K\) and the cyclic factors is required.

### Finite graph certificate

Let \(G\) be torsion-free and let \(\Gamma\) be a finite directed multigraph with vertex set \(\{1,\ldots,N\}\), allowing loops, parallel edges and isolated vertices.
Give every edge \(e=(i,j)\) a group label \(g_e\in G\), a phase \(\zeta_e\in\mathbb T\), and a weight \(c_e>0\).
Define the bounded equivariant incidence operator and its positive square by
\[
(D_\Gamma w)_e
=\sqrt{c_e}\bigl(w_i-\zeta_e\lambda(g_e)w_j\bigr),
\qquad
H_\Gamma=D_\Gamma^*D_\Gamma.
\tag{4}
\]
Both \(D_\Gamma\) and \(H_\Gamma\) are affine pencils in the finite tuple of edge labels and their inverses.
This tuple can be included in a generating tuple of the finitely generated subgroup containing all coefficients under consideration.

For each connected component, choose a root and a spanning tree in the underlying unoriented graph.
The tree equations in \(D_\Gamma w=0\) determine unitary operators
\[
W_i=\alpha_i\lambda(h_i),\qquad |\alpha_i|=1,
\]
such that \(w_i=W_i\xi\), with \(W_i=I\) at the root.
For every edge outside the tree, including a loop, form
\[
T_e=W_i^{-1}\zeta_e\lambda(g_e)W_j
=\eta_e\lambda(k_e).
\tag{5}
\]
Call the component flat when every such operator \(T_e\) is the actual identity, equivalently every closed-walk transport is the identity.
In particular, a tree or an isolated vertex is flat.
Flatness depends on the group elements represented by the closed walks and their phases, not on whether the unreduced formal words are empty.
Let \(f\) be the number of flat connected components.
Then
\[
\dim_G\ker D_\Gamma
=\dim_G\ker H_\Gamma=f,
\qquad
\operatorname{rk}_G D_\Gamma
=\operatorname{rk}_G H_\Gamma=N-f.
\tag{6}
\]

If \(f=0\), then \(H_\Gamma\) is injective.
Consequently, for any \(W,v,\gamma\) as in the weighted energy criterion and any selfadjoint affine \(K\),
\[
L=W^{-1}(H_\Gamma+iK),\qquad
Q=\begin{pmatrix}0&\gamma v^*W\\v&L\end{pmatrix}
\]
satisfy \(L\in GL_N(U)\) and \(\operatorname{rk}_G Q=N+1\).
To certify \(f=0\), it suffices to exhibit a nonidentity loop transport in every connected component.
Such a transport may have a nontrivial group label, or it may have group label \(e\) and phase different from \(1\).

If \(f=1\), take \(W=I\), \(v=e_i\), \(u=e_i^*\), where \(i\) lies in the unique flat component.
Then \(\ker H_\Gamma\cap\ker u=\{0\}\), so (1) holds for every \(L\) with \(\operatorname{Re}L=H_\Gamma\).
The rational Schur conclusion in this case retains the separate assumption \(L\in GL_N(U)\).
No assertion for an arbitrary row on a flat component is included.

## Current assessment

[Selected decision](#decision-reviewed-energy-certificates)

## Assessment history

### Decision reviewed-energy-certificates

| Field | Value |
| --- | --- |
| date | 2026-11-10T19:24 |
| status | proved |
| reason | Independent whole-argument inspection supports the weighted bounded energy proof, cyclic coefficient criterion, exact graph kernel dimensions and all affiliated-inverse qualifications under the declared foundations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete weighted energy, cyclic and finite-graph certificates, including the separate denominator premise under the weaker kernel-intersection hypothesis. |
| argument | [Complete argument](#argument) | Bounded proofs, finite-trace conversion, actual rational closure, regular-transport kernel calculation and coupled example without a spectral gap. |
| review | [Independent Claim finding](../audits/reviews/Yin_R_A0007_v1.md#claim-finding) | Independently reviewed complete statement and argument, accepted foundations, exact source role and limitations. |
| dependency | [Finite affiliated foundations](../audits/literature/MSY23/Yin_U004.md#msy23-u004) | Exactly the finite-affiliated foundations and Lemmas 5.1--5.5: bounded-square injectivity, support traces, unnormalized analytic rank and affiliated invertibility; no Atiyah integrality premise. |
| dependency | [Actual rational closure](../audits/literature/MSY23/Yin_U003.md#msy23-u003) | Exactly the complete-division-closure argument: entries of actual matrix inverses and scalar inverse closure in the fixed affiliated ambient algebra. |

## Argument

### Bounded energy calculation

All operators in the kernel calculation are bounded, so no domain assertion about \(L^{-1}\) is needed.
Suppose \(Q(f,w)=0\), with \(f\in\mathcal H\) and \(w\in\mathcal H^N\).
The two block equations are
\[
uw=0,\qquad Lw=-vf.
\]
The first equation and \(\gamma\ne0\) give \(v^*Ww=0\).
Since \(W=W^*\), the second equation implies
\[
\langle Hw,w\rangle
=\operatorname{Re}\langle WLw,w\rangle
=-\operatorname{Re}\langle Wvf,w\rangle
=0.
\]
For a positive bounded operator, vanishing of this quadratic form is equivalent to \(w\in\ker H\).
Condition (E) now gives \(w=0\).
The remaining equation is \(vf=0\), and the nonzero constant column \(v\) is injective, so \(f=0\).
This proves \(\ker Q=0\).

In a finite von Neumann algebra, an injective bounded square matrix has dense range and an affiliated inverse by polar decomposition and equality of the traces of its two support projections.
The same argument gives its full unnormalized analytic rank.
These standard finite-affiliated facts are accepted at the scope of [MSY23-U004](../audits/literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness).
They prove (1).
If \(\ker H=0\), applying the quadratic-form argument to \(Lw=0\) also gives \(w=0\), and hence the affiliated inverse of \(L\).

When \(L\) is affiliated-invertible, elementary block elimination in \(M_{N+1}(U)\) reduces \(Q\) to \(\operatorname{diag}(-uL^{-1}v,I_N)\).
Invertibility of \(Q\) therefore implies that \(uL^{-1}v\) is a unit of \(U\).
If the entries of \(L\) belong to \(B\), the inverse entries belong to \(\operatorname{Rat}_U(B)\), and that subalgebra is inverse closed in \(U\).
The [retained rational-closure argument](../audits/literature/MSY23/Yin_U003.md#complete-division-closure-and-proposition-411) consequently places both the Schur element and its inverse in the same actual rational closure.

The weaker intersection hypothesis cannot supply denominator invertibility: for \(N=1\), \(W=u=v=1\), and \(L=0\), it holds with \(H=0\), while \(Q\) is the invertible flip matrix and \(L\) is not invertible.
This explains the separate premise in the statement.

### Cyclic regular operators and the finite coefficient test

For \(g\ne e\) in a torsion-free group, every right coset \(\langle g\rangle t\) supports a copy of the bilateral shift under left multiplication by \(g\).
Any eigenvalue of a unitary would have modulus one.
The bilateral shift therefore has no eigenvalues: an eigenvector would have constant absolute value along the infinite orbit and could not be square summable unless zero.
Thus \(1-\zeta\lambda(g)\) is injective for every \(\zeta\in\mathbb T\).
This is the [existing cyclic regular-representation input](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions), with its exact use of torsion-freeness.

For every \(w\in\ell^2(G)^N\),
\[
\langle H_Cw,w\rangle
=\sum_j\bigl\|(1-\zeta_j\lambda(g_j))C_jw\bigr\|^2.
\]
The cyclic operator in each summand acts componentwise on the \(m_j\) coordinates and is injective.
The displayed sum vanishes exactly when \(C_jw=0\) for every \(j\).
This proves the kernel equality in (2).
The projection onto that kernel is the constant matrix projection onto \(K_C\), tensored with the identity on \(\ell^2(G)\), so its group trace equals \(\dim_{\mathbb C}K_C\).
This proves the rank formula in (2).
Intersecting the kernel equality with \(\ker u\) proves the equivalence with (3).
The remaining cyclic conclusions are now direct applications of the weighted energy criterion.

### Tree transport and actual loop operators

Positive edge weights do not affect the zero equations in (4).
An edge equation is \(w_i=\zeta_e\lambda(g_e)w_j\), and traversal in the reverse direction uses the inverse unitary.
Following the unique tree paths from the root therefore gives the unitary transports \(W_i\) and the representation \(w_i=W_i\xi\).
For a nontree edge, substitution gives
\[
W_i\xi=\zeta_e\lambda(g_e)W_j\xi,
\qquad\text{equivalently}\qquad \xi=T_e\xi.
\]
This also handles a loop at a vertex.

Write \(T_e=\eta_e\lambda(k_e)\) as in (5).
If \(k_e\ne e\), its infinite order and the cyclic no-eigenvector argument force \(\xi=0\).
If \(k_e=e\) but \(\eta_e\ne1\), the same conclusion follows from the scalar equation \(\xi=\eta_e\xi\).
These are all cases in which \(T_e\ne I\).
Hence a nonflat connected component contributes no kernel vector.
If every \(T_e=I\), all remaining equations hold for every \(\xi\), so its kernel consists exactly of the vectors in (4).
Tree transports and nontree loop transports generate every closed-walk transport, which proves the equivalent formulation of flatness and its independence of the chosen spanning tree.

For a flat component \(C\), the map
\[
J_C:\ell^2(G)\longrightarrow\ell^2(G)^{V_C},
\qquad
J_C\xi=|V_C|^{-1/2}(W_i\xi)_{i\in V_C}
\]
is an isometry onto the component kernel.
It intertwines right regular translations because every \(W_i\) is a scalar multiple of a left regular unitary.
Each diagonal entry of the range projection \(J_CJ_C^*\) is \(|V_C|^{-1}I\), so its unnormalized group trace is \(1\).
The component decomposition is orthogonal, yielding \(\dim_G\ker D_\Gamma=f\).
The identity \(\langle H_\Gamma w,w\rangle=\|D_\Gamma w\|^2\) gives \(\ker H_\Gamma=\ker D_\Gamma\).
Subtracting the common kernel dimension from the input dimension \(N\) proves (6).
This uses no assertion of integer rank for other group-ring matrices.

If \(f=0\), the energy conclusions follow from \(\ker H_\Gamma=0\).
If \(f=1\) and \(i\) belongs to the flat component, a kernel vector has \(w_i=W_i\xi\).
The coordinate condition \(w_i=0\) forces \(\xi=0\), because \(W_i\) is unitary.
All other components already have zero kernel, proving the stated one-flat-component border conclusion.

For a general scalar row \(u\), its restriction to a flat component imposes
\[
\left(\sum_{i\in V_C}u_iW_i\right)\xi=0.
\]
The coefficient is a scalar group-ring element, whose injectivity is not supplied by the graph calculation in general.
Thus arbitrary borders on flat components can reintroduce the scalar analytic zero-divisor question rather than resolve it.

### A coupled example without a spectral-gap premise

Let \(g,h\in G\) be distinct and put
\[
D=\begin{pmatrix}1&-\lambda(g)\\1&-\lambda(h)\end{pmatrix},
\qquad
H=D^*D=
\begin{pmatrix}
2&-\lambda(g)-\lambda(h)\\
-\lambda(g^{-1})-\lambda(h^{-1})&2
\end{pmatrix}.
\]
The two parallel edges have a fundamental loop with group label \(g^{-1}h\ne e\), so \(H\) is injective.
Consequently, for every selfadjoint affine \(K\in M_2(\mathbb CG)\) and nonzero \(v\in\mathbb C^2\),
\[
L=H+iK,\qquad
Q=\begin{pmatrix}0&v^*\\v&L\end{pmatrix}
\]
satisfy \(L\in GL_2(U)\) and \(\operatorname{rk}_G Q=3\).
There need not be a positive lower bound for \(H\).
For \(G=\mathbb Z=\langle t\rangle\), \(g=e\) and \(h=t\), Fourier transformation gives the smaller eigenvalue \(2-|1+z|\), which tends to zero as \(z\to1\) on the circle.
The argument therefore proves an affiliated-invertibility conclusion without requiring a spectral gap.

## Source relationship and scope

The energy argument is a direct bounded quadratic-form calculation, and the cyclic input is already retained at the cited local scope.
The finite graph construction is related to the established connection-Laplacian energy and compatible-section mechanism in [BSS13, arXiv v2, Section 1.3, pp. 4--5](../literature/pdf/BSS13--arxiv-v2.pdf#page=4).
Those primary passages were read by the development delegate and checked for their actual scope.
They define the finite-dimensional orthogonal connection Laplacian, express its energy as a sum of squared edge discrepancies, and discuss compatible assignments and the kernel for a flat connected graph.
This is source attribution and comparison, rather than a premise supplying the regular-representation result (6).
The \(\ell^2(G)\) holonomy dichotomy, exact group-module dimension and bounded bordered application are proved above.
No Cheeger inequality, finite-dimensional spectral-gap estimate, full-paper audit or historical-priority assertion is imported.

The accepted finite-affiliated foundations convert injectivity of bounded square matrices into affiliated inverses; they do not assume Atiyah integrality.
The proofs use torsion-freeness only to rule out eigenvectors of regular unitaries with nonidentity group labels.
They require neither amenability, an ordering of the group, a cyclic quotient, scalar Ore fractions, nor integer rank of an unrelated matrix.
The rank constraints apply to the stated structured matrices over any torsion-free group, not to every affine pencil or every scalar border.
In particular, no procedure has been established that converts an arbitrary rational realization to a matched border satisfying (E) or one of the explicit positive certificates.
The general forbidden interval remains unresolved outside the verified hypotheses.

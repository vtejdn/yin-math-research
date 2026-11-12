---
author: Yin
---
# Analytic and graph obstructions around the amenable atom problem

This exploration was made on 2026-11-12 for [A0001](../tasks/Yin_T_A0001_v1.md#contract), following Yin's request for structural analytic and probabilistic progress without probing examples.
The known equivalence of the amenable Atiyah and group-ring domain problems is an input, not a result of this round.
The [preceding homological assessment](Yin_L_A0030_v1.md) concerns finite resolutions; this material instead tests operator topologies, inverse gates and weighted support graphs.
The positive quantitative interface is retained separately in [C14](../claims/Yin_C_A0014_v1.md#statement).
The arguments below explain which otherwise natural mechanisms fail to supply that interface.

## Cauchy regularization and the wrong topologies

Let \(G\) be finitely generated amenable, \(0\ne a\in\mathbb CG\), \(H=a^*a\), \(p=1_{\{0\}}(H)\), and \(\alpha=\tau(p)<1\).
For \(t>0\), put
\[
q_t=t(H+t)^{-1},\qquad
\operatorname{rk}_G(T)=\tau(1_{\{|T|>0\}}).
\]
These are bounded rational expressions using actual bounded inverse gates.
Spectral calculus gives strong and \(L^2(\tau)\) convergence \(q_t\to p\), but for distinct \(s,t>0\),
\[
\operatorname{rk}_G(q_t)=1,\qquad
\operatorname{rk}_G(q_t-p)
=\operatorname{rk}_G(q_t-q_t^2)
=\operatorname{rk}_G(q_t-q_s)=1-\alpha.
\tag{1}
\]
Indeed every difference vanishes at \(x=0\) and is nonzero for every \(x>0\), whereas \(t/(x+t)\) is strictly positive everywhere.
Thus these approximants are not Cauchy in rank metric even though their tracial idempotency defects tend to zero.
Rank-continuity results for other approximation schemes cannot be transferred to this one.

There is, nevertheless, a uniform finite-window approximation of their traces.
For finite nonempty \(F\subset G\), let \(P_F\) be coordinate compression, \(H_F=P_FH|_{\ell^2(F)}\), and \(C_F=P_FH|_{\ell^2(F^c)}\).
Write \(b_F=\operatorname{rank}C_F\).
If \(\operatorname{supp}H\subset B_w\), then \(b_F\le|\partial_wF|\), where \(\partial_wF=\{x\in F:B_wx\not\subset F\}\).
The block decomposition of \(H+t\) has
\[
K=H_F+t,\qquad D=H_{F^c}+t,\qquad
S=K-C_FD^{-1}C_F^*.
\]
Here \(D\ge t\), and Schur complementation gives \(P_F(H+t)^{-1}P_F=S^{-1}\).
Since the compression of \((H+t)^{-1}\) is at most \(t^{-1}\), \(S\ge t\).
Also \(S\le K\), whence
\[
0\le tS^{-1}-tK^{-1}\le I,\qquad
\operatorname{rank}(S^{-1}-K^{-1})\le b_F.
\]
The rank assertion follows from \(S^{-1}-K^{-1}=S^{-1}(K-S)K^{-1}\).
Translation invariance gives \(\operatorname{Tr}(P_Fq_tP_F)=|F|\tau(q_t)\).
Consequently
\[
0\le \tau(q_t)-\frac{\operatorname{Tr}(t(H_F+t)^{-1})}{|F|}
\le\frac{b_F}{|F|}\qquad(t>0).
\tag{2}
\]
The error is uniform all the way to \(t=0\).
Taking \(t\downarrow0\) gives the corresponding normalized finite-window kernel estimate.
Uniformity therefore resolves an interchange-of-limits issue, but still yields limits of normalized integers rather than integer values.

## A precise norm barrier

For torsion-free countable amenable \(G\), \(C_r^*(G)\) has no scalar projections other than zero and one.
The exact external chain is [HK97, Corollary 1.3](../audits/literature/HK97/Yin_U001.md#amenable-assembly), giving assembly surjectivity, and [BCM04, Definition 3.5 and Theorem 6.3](../audits/literature/BCM04/Yin_U001.md#assembly-trace), putting the trace image of assembly in \(\Lambda_G=\mathbb Z\) when \(G\) is torsion-free.
Faithfulness of the canonical trace then excludes any scalar projection with trace strictly between zero and one.
This is distinct from assuming inverse-closedness of \(\ell^1(G)\).

Every self-adjoint element of this \(C^*\)-algebra has connected spectrum: a disconnection would yield a nontrivial scalar projection by continuous functional calculus.
In particular, if \(0\in\sigma(H)\) and \(M=\|H\|>0\), then \(\sigma(H)=[0,M]\).
Hence for \(0<t\le M\),
\[
\|q_t^2-q_t\|=\frac14,\qquad \|q_t-p\|=1.
\tag{3}
\]
The first equality evaluates \(tx/(x+t)^2\) at \(x=t\).
For the second, the support of the faithful trace spectral measure is the entire spectrum; on positive spectral values approaching zero, \(q_t-p=t/(x+t)\) approaches one.

More generally, every nontrivial projection \(p\in\mathcal N(G)\) satisfies
\[
\operatorname{dist}(p,C_r^*(G))=\frac12.
\tag{4}
\]
The upper bound uses \(I/2\).
If \(\|b-p\|=\delta<1/2\), replace \(b\) by its self-adjoint part, which does not increase the distance.
Its spectrum lies in \([-\delta,\delta]\cup[1-\delta,1+\delta]\).
The spectral cut \(e=1_{(1/2,\infty)}(b)\) belongs to \(C_r^*(G)\), and \(\|e-b\|\le\delta\).
Thus \(\|e-p\|\le2\delta<1\), excluding both \(e=0\) and \(e=1\), a contradiction.
Tracial convergence of Cauchy approximants supplies no operator-norm route across (4).

## Bounded rational output versus bounded inverse gates

Suppose a finite row \(V=(b_1,\ldots,b_k)\) over \(\mathbb CG\) satisfies
\[
aV=0,\qquad \overline{\operatorname{ran}_{\ell^2}V}=\ker_{\ell^2}a.
\tag{5}
\]
Finite generation of the algebraic annihilator is sufficient for the second condition by [complete amenable kernel density](../claims/Yin_C_A0001_v2.md#rational-kernel-localization).
Put \(c=VV^*\) and \(S=H+c\).
Then \(Hc=cH=0\), and \(\ker S=\ker a\cap\ker V^*=0\).
Thus \(S\) is a unit in the actual affiliated algebra and
\[
p=cS^{-1},\qquad 1-p=HS^{-1}.
\tag{6}
\]
These identities follow by restricting to the two complementary support projections of \(H\) and \(c\); the common zero space vanishes by (5).
Both outputs are bounded projections, and \(1-p\) is a bounded actual-rational operator with the same kernel as \(a\) and gap one.
If \(0<\alpha<1\), (4) forces \(S^{-1}\) to be unbounded.
Indeed a bounded inverse of \(S\in C_r^*(G)\) would belong to that \(C^*\)-algebra by continuous functional calculus and would put \(p\) there.

A single relation \(ab=0\), with \(b\ne0\), gives no guarantee that \(V=b\) satisfies (5).
The residual space is exactly \(\ker a\cap\ker b^*\).
Even the positive repair \(H+bb^*\) cannot have a spectral gap at zero under the torsion-free amenable hypotheses.
If it were boundedly invertible, \(bb^*(H+bb^*)^{-1}\) would be a nontrivial scalar \(C^*\)-projection.
If its zero eigenvalue were isolated, its nontrivial kernel projection would itself be a scalar \(C^*\)-projection.
Both cases are excluded, and the zero operator is excluded by \(a\ne0\).
Moreover, since \(Hbb^*=0\),
\[
bb^*(H+bb^*+t)^{-1}=bb^*(bb^*+t)^{-1}.
\tag{7}
\]
This follows on the support of \(bb^*\), where \(H=0\), and both sides vanish on its complement.
Adding the other square does not improve the boundary regularization of this support.

Thus actual rational closure and linearization can record a bounded kernel projection while hiding an unavoidable unbounded inverse.
The [existing rational Schur realization](../claims/Yin_C_A0001_v2.md#rational-kernel-localization) handles that inverse legitimately but does not promote its output into a projection algebra with integer trace.

## What the support graph already knows

Write \(a=\sum_{s\in S}c_ss\), with every \(c_s\ne0\).
For finite \(F\), let \(B_F:\mathbb C^F\to\mathbb C^{SF}\) be the convolution matrix, with edge weight \(c_s\) at \((sx,x)\), and let \(\Gamma_F\) be its bipartite support graph.
For any \(s_0\in S\), the edges \(x\mapsto s_0x\) match every column.
Thus the maximum matching has size \(|F|\), with no torsion or amenability assumption.
All actual kernel dimension is therefore weighted cancellation:
\[
\dim_{\mathbb C}\ker B_F=|F|-\operatorname{rank}B_F.
\tag{8}
\]
For amenable Følner sets, complete kernel localization identifies \(\alpha\) with the limit of (8) divided by \(|F|\).
There is no remaining Hall deficit for an unweighted matching argument to eliminate.

### Definition: uniquely restricted matching

A matching in a finite bipartite graph is uniquely restricted when the subgraph induced by its saturated vertices has that matching as its unique perfect matching.
Write \(\nu_{\mathrm{ur}}(\Gamma)\) for its maximum size.
For every matrix with this graph and nonzero complex edge weights, such a matching of size \(r\) gives an \(r\times r\) minor with a single nonzero determinant monomial.
Therefore \(\nu_{\mathrm{ur}}(\Gamma)\) is a rank lower bound uniform over all nonzero edge weights.
Only this elementary implication is used below.

Suppose finite nonempty \(S,T\subset G\) have no uniquely represented product: every point of \(ST\) has at least two representations \(st\).
Set \(K=(ST)^{-1}(ST)\) and \(F_T=\bigcap_{t\in T}t^{-1}F\).
For left Følner sets, \(|F_T|/|F|\to1\).
Greedily choose \(J\subset F_T\) with \(STg\), \(g\in J\), pairwise disjoint.
An intersection \(STg\cap STh\ne\varnothing\) implies \(h\in Kg\); each choice discards at most \(|K|\) candidates.
Hence \(|J|\ge |F_T|/|K|\).
The column sets \(Tg\subset F\) are disjoint too, since their translates by any fixed \(s_0\in S\) lie in the disjoint sets \(STg\).

For each \(g\in J\) and row \(y\in STg\), at least two neighbors lie in \(Tg\).
Assign their \(d_y\) edge weights \(1,\ldots,1,-(d_y-1)\), and assign every remaining edge weight one.
These assignments are compatible because the sets of affected rows are disjoint.
They are all nonzero, and each vector \(1_{Tg}\) is in the kernel of the resulting matrix \(B_F^w\).
These vectors are linearly independent, so
\[
\nu_{\mathrm{ur}}(\Gamma_F)\le\operatorname{rank}B_F^w
\le |F|-\frac{|F_T|}{|K|}.
\]
Consequently
\[
\limsup_F\frac{\nu_{\mathrm{ur}}(\Gamma_F)}{|F|}
\le 1-\frac1{|(ST)^{-1}(ST)|}<1.
\tag{9}
\]
This is an obstruction to a nearly full uniquely restricted matching certificate whenever such \(S,T\) exist.
The constructed weights depend on position and generally violate the group-ring restriction \(w(sx,x)=c_s\).
It is not a group-ring zero-divisor construction.

In fact, demanding absence of finite-support kernels for every such nonzero position-dependent weighting, for every finite \(S\), is equivalent to the unique-product property.
For a group with that property, a nonzero finitely supported vector with support \(T\) has a uniquely represented output in \(ST\), so its image has a nonzero coordinate.
Conversely, a pair \(S,T\) with no uniquely represented product admits the same row-sum cancellation weighting on the infinite graph, with kernel vector \(1_T\).
Thus a universal proof robust under arbitrary edge weights asks for this stronger combinatorial structure and does not exploit the tied coefficients of a group ring.

## Randomization retains or changes the decisive correlations

For fixed finite \(S,T\) in a countable group, replace \(c_s\) by shared indeterminates \(z_s\).
The convolution matrix \(B_T(z)\) has polynomial entries.
Its square minor on rows \(s_0T\) has a determinant that is not identically zero: at \(z_{s_0}=1\), \(z_s=0\) for \(s\ne s_0\), it is a permutation matrix.
Therefore the rank-deficient parameter set is contained in a proper algebraic set.
There are only countably many finite \(T\).
With any absolutely continuous joint law for the global coefficients, almost surely no finite-support kernel exists.
Amenable kernel density then gives analytic injectivity almost surely.
No torsion-free assumption entered, so this generic conclusion cannot exclude the exceptional deterministic coefficients relevant to the conjecture.

Alternatively let \(A\) be a bounded weighted operator on the countable vertex space, let \(U,V\) be diagonal unitaries, and put \(B=UAV\).
For the self-adjoint linearization,
\[
\mathcal H_A=\begin{pmatrix}0&A^*\\A&0\end{pmatrix},\qquad
\mathcal H_B=W\mathcal H_AW^*,\qquad W=\operatorname{diag}(V^*,U).
\tag{10}
\]
Every vertex spectral measure is preserved, since \(W\) acts by phases on the coordinate basis.
Also \(P_{\ker B}=V^*P_{\ker A}V\), so all diagonal kernel weights are preserved.
But every finite minor changes only by the product of its row and column phases.

For an alternating cycle with edges \((y_i,x_i)\) and \((y_i,x_{i+1})\), \(x_{r+1}=x_1\), the ratio
\[
\prod_{i=1}^r\frac{w(y_i,x_i)}{w(y_i,x_{i+1})}
\tag{11}
\]
is gauge invariant: row phases cancel within each quotient and column phases telescope.
On a finite connected graph, equality of all such cycle ratios for two nonzero weightings is also sufficient for a row/column \(\mathbb C^\times\) gauge.
Choose a spanning tree and propagate row and column multipliers from one root; each non-tree edge is consistent precisely because its fundamental cycle has the same ratio.
This inverse statement concerns nonzero complex multipliers, not necessarily unitary multipliers or uniformly bounded multipliers on an infinite graph.
Independent vertex phases therefore preserve exactly the cycle cancellations that independent edge phases could change.
Neither global coefficient randomization nor this spectrally exact gauge randomization supplies a conclusion for every fixed group-ring element.

There is a further noise-scale obstruction that requires no spectral-averaging theorem.
Let \(H_0,H_\varepsilon\) be bounded self-adjoint operators in a finite tracial von Neumann algebra with \(\|H_\varepsilon-H_0\|\le\varepsilon\).
Then
\[
\tau 1_{\{0\}}(H_0)
\le \tau1_{[-\varepsilon,\varepsilon]}(H_\varepsilon)
\le \tau1_{[-2\varepsilon,2\varepsilon]}(H_0).
\tag{12}
\]
For the first inequality, a strict reverse trace inequality would force a nonzero intersection of \(\ker H_0\) with the spectral subspace of \(H_\varepsilon\) outside \([-\varepsilon,\varepsilon]\).
On that intersection \(\|H_\varepsilon\xi\|>\varepsilon\|\xi\|\), contrary to the norm perturbation bound.
The second follows identically: a vector in the \(H_\varepsilon\) middle subspace and the \(H_0\) outer subspace would satisfy both \(\|H_0\xi\|>2\varepsilon\|\xi\|\) and \(\|H_0\xi\|\le2\varepsilon\|\xi\|\).
The intersection dimension bound used here is \(\tau(P\wedge Q)\ge\tau(P)+\tau(Q)-1\).
By continuity from above, the middle quantity in (12) tends to the original zero-atom mass.
Consequently making each positive-noise measure nonatomic does not remove its mass in a window at the noise scale.

## The analytic target that survives these obstructions

[C14](../claims/Yin_C_A0014_v1.md#statement) replaces a mere tracial limit by spatially summable increments of optimal polynomial approximants.
Its sufficient condition uses only finite-word moments and ball volumes in each summand, without the unknown atom in the hypothesis.
Its independent Banach-algebra rounding argument lower bounds the positive-spectrum response of explicit filters.
These estimates use the finite propagation of the original group-ring operator, which arbitrary affiliated inverse gates and independent edge noises would discard.

What remains is to derive an applicable increment tail estimate, or a sharper coefficient-sensitive spatial estimate, from the actual algebraic structure.
Amenability supplies the boundary estimate (2), but no such summability bound has been deduced from it.
The polynomial-growth rate consequences in C14 are conditional and are stronger than injectivity: they exclude zero from the entire spectrum.
They cannot serve as a universal target for injective operators whose positive spectrum accumulates at zero.
The graph route would have to control cancellations with the equalities \(w(sx,x)=c_s\) retained, beyond support-only matching and generic random coefficients.
No complete amenable solution, new group-class theorem, or claim of historical novelty is made.

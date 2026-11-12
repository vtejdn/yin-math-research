---
author: Yin
---
# Finite-kernel window compatibility and the solid-norm obstruction

This revision develops the finite correlation quantity of [C14 v3](Yin_C_A0014_v3.md#finite-window-kernel-correlation-criterion), whose earlier statements remain fixed at their stated scopes.
It gives quantitative window identities, an operator-norm approximation on each fixed algebraic kernel witness, and an obstruction to replacing coefficient mass by a weaker solid convolution norm.
It also isolates a finite cut-energy sufficient condition and proves the mandatory lower bound under a hypothetical atom.
No independent uniform correlation upper bound, new group class, or solution of the general amenable problem is asserted.
No concrete group or numerical example is tested.

## Statement

### Setup and coefficient averaging

Let G be a finitely generated discrete group, let a be a nonzero element of \(\mathbb CG\), and let p be the kernel projection of left convolution by a on \(\ell^2(G)\).
Write \(\alpha=\tau(p)<1\), and, for each nonempty finite F, let \(P_F\) be the coordinate projection and \(Q_F\) the orthogonal projection onto
\[
K_F=\{\xi\in\mathbb C[F]:a\xi=0\},\qquad k_F=\dim K_F.
\]
All finite matrices below are also operators on \(\ell^2(G)\) by zero extension.
Writing \(S=\operatorname{supp}a\), the actual finite map defining \(Q_F\) has rows \(y\in SF\), columns \(x\in F\), and entries \(a(yx^{-1})\).
Equal group displacements therefore have exactly the same coefficient throughout these constructions; no independent edge coefficients are introduced.
For a matrix M supported on \(F\times F\), define
\[
\Phi_F(M)=\frac1{|F|}\sum_{x,y\in F}M(y,x)\lambda_{yx^{-1}},
\qquad b_F=\Phi_F(Q_F),\qquad \mathcal C_F=\|b_F\|_1.
\tag{1}
\]
The norm \(\|\cdot\|_1\) in coefficient statements is the convolution coefficient norm, whereas \(\|\cdot\|\) is the regular operator norm.
Set
\[
\phi_F(g)=\frac{|F\cap gF|}{|F|},\quad
r_F=\sum_g\phi_F(g)p(g)\lambda_g,\quad
\delta_F=\alpha-k_F/|F|.
\]

For every G in this setup,
\[
0\le b_F\le r_F\le1,\quad
\tau(r_F-b_F)=\delta_F,\quad
|(r_F-b_F)(g)|\le\delta_F,\quad
|(p-b_F)(g)|\le\delta_F,\quad
\|r_F-b_F\|_1\le\sqrt{|F|\delta_F}.
\tag{2}
\]
If G is amenable and the radius-w word ball contains the support of a, the fixed [kernel-localization theorem](Yin_C_A0001_v2.md#rational-kernel-localization) gives
\[
0\le\delta_F\le\frac{|\partial_wF|}{|F|},\qquad
\partial_wF=\{x\in F:B_wx\not\subset F\}.
\tag{3}
\]
Thus the last estimate in (2) gives \(\sqrt{|\partial_wF|}\), not a bound by the square root of the boundary proportion.

### Exact compatibility of windows

Right translation leaves the normalized convolution average unchanged:
\[
b_{Fz}=b_F\qquad(z\in G).
\tag{4}
\]
For nested windows \(F\subset E\),
\[
|F|b_F\le |E|b_E.
\tag{5}
\]
If \(F_1,\ldots,F_N\) are pairwise disjoint subsets of E, put
\(d=k_E-\sum_i k_{F_i}\ge0\).
Then there is a positive group-ring element c with ac=0 such that
\[
b_E=\sum_i\frac{|F_i|}{|E|}b_{F_i}+c,
\qquad \tau(c)=d/|E|,\qquad \|c\|_1\le\sqrt d.
\tag{6}
\]
The unnormalized rank d is essential in this estimate.
For overlapping windows one still has the exact identities and inequality
\[
K_F\cap K_E=K_{F\cap E},\qquad
K_F+K_E\subset K_{F\cup E},\qquad
k_F+k_E\le k_{F\cap E}+k_{F\cup E},
\tag{7}
\]
but the sum of their orthogonal projections need not be a projection.
No orthogonal gluing assertion for overlaps is used.

### Boundary-controlled norm convergence on fixed kernel witnesses

Let \(B=(\xi_1,\ldots,\xi_m)\) be a nonzero finite row over \(\mathbb CG\) with \(a\xi_j=0\) for every j, viewed as an operator from \(\ell^2(G)^m\) to \(\ell^2(G)\).
Let \(T=\bigcup_j\operatorname{supp}\xi_j\), and define the computable boundary-strip count
\[
d_E(T)=\left|\left(\bigcup_{t\in T}t^{-1}E\right)
\setminus\left(\bigcap_{t\in T}t^{-1}E\right)\right|.
\]
Then, for every finite nonempty E,
\[
B^*(1-b_E)B\le\frac{d_E(T)}{|E|}\|B\|^2I_m,
\qquad
\|(1-b_E)B\|\le\sqrt{\frac{d_E(T)}{|E|}}\|B\|.
\tag{8}
\]
For a left Følner sequence, the right side tends to zero for each fixed B.
Consequently the b_E form a positive contractive left approximate identity, along that sequence, on the closed right ideal
\[
J=\overline{\{\xi\in\mathbb CG:a\xi=0\}}^{\|\cdot\|}\subset C_r^*(G).
\tag{9}
\]
Neither equality of J with the whole analytic annihilator in \(C_r^*(G)\), nor a right approximate identity on J, is asserted.
The convergence is not uniform over the unit ball of the von Neumann kernel: when G is torsion-free amenable and \(0<\alpha<1\), the fixed result still gives \(\|p-b_E\|=1\) for every E.

### Finite cut energy and its nonlocal lower bound

Assume now that G is torsion-free amenable.
For a finite nonempty averaging window W, define the Schur multiplier on bounded operators by
\[
\mathsf M_W(T)(y,x)=\phi_W(yx^{-1})T(y,x).
\]
For an orthogonal projection Q, define its positive cut-energy operator
\[
\mathsf A_W(Q)=Q+\mathsf M_W(Q)
-Q\mathsf M_W(Q)-\mathsf M_W(Q)Q.
\tag{10}
\]
This is an explicitly finite matrix when \(Q=Q_E\), and
\[
0\le\mathsf A_W(Q)\le1,\quad
\mathsf A_W(Q)=\frac1{|W|}\sum_{z\in G}[Q,P_{Wz}]^*[Q,P_{Wz}],\quad
(Q-\mathsf M_W(Q))^2\le\mathsf A_W(Q).
\tag{11}
\]
The positive sum is a strong-operator sum.

For every increasing finite exhaustion \(E_j\) of G, a hypothetical nonzero p forces
\[
\liminf_j\|\mathsf A_W(Q_{E_j})\|\ge\frac12
\quad\text{for every fixed nonempty finite }W.
\tag{12}
\]
In particular a bound strictly below \(1/2\) along a subsequence, for one fixed W, would exclude the zero atom.
This test contains no lower bound on the positive spectrum of \(a^*a\).
It is an unresolved sufficient condition, not an independent upper bound proved from the group hypotheses.

If \(E_j\) is also a left Følner sequence, then
\[
\lim_j\frac{\operatorname{Tr}\mathsf A_W(Q_{E_j})}{|E_j|}
=2\sum_{g\in G}(1-\phi_W(g))|p(g)|^2.
\tag{13}
\]
Along any left Følner sequence \(W_l\), the right side tends to zero as \(l\to\infty\).
Therefore a small normalized trace of this energy is automatic, and does not replace the operator-norm hypothesis.
Under a hypothetical atom, a vanishing proportion of finite-dimensional directions can still carry the mandatory norm in (12).

### No weaker solid convolution norm

Let G be amenable and let \(N:\mathbb CG\to[0,\infty)\) satisfy, for fixed constants \(M,C_0,K>0\),
\[
N(fh)\le M N(f)N(h),\qquad |f(e)|\le C_0N(f),
\qquad N(|b|)\le K N(b)\quad(b=b^*).
\tag{14}
\]
Here \(|b|(g)=|b(g)|\) denotes coefficientwise modulus, not the operator modulus.
No completeness assumption is needed.
Then every self-adjoint finite b satisfies
\[
\|b\|_1\le MK N(b).
\tag{15}
\]
In particular every solid convolution Banach norm with continuous identity coefficient dominates coefficient mass on the b_F, up to its multiplication constant.
Uniform boundedness in such a norm cannot be a weaker substitute for bounded \(\mathcal C_F\).

For any positive submultiplicative weight w, one also has directly
\[
\sum_g w(g)|b(g)|\ge\|b\|_1\qquad(b=b^*).
\tag{16}
\]
The results do not exclude phase-sensitive norms or norms defined only on the annihilator, because taking coefficientwise modulus generally leaves that annihilator.
The unconditional-completion obstruction is related to the inspected [Nica source argument](../audits/literature/Nic08/Yin_U001.md#nic08-u001); the proof below uses the continuous identity coefficient instead of assuming spectral equivalence.
No priority claim is made.

## Argument

### The coefficient map and the boundary defect

The map \(\Phi_F\) is unital and completely positive from matrices on \(\mathbb C[F]\) to \(C_r^*(G)\).
Indeed it has the row form \(|F|^{-1}V(M\otimes I)V^*\), where the entries of V are the unitaries \(\lambda_y\), and \(|F|^{-1}VV^*=I\).
For any finite matrix M, grouping terms by displacement and then applying Cauchy--Schwarz to all entries gives
\[
\|\Phi_F(M)\|_1
\le\frac1{|F|}\sum_{x,y\in F}|M(y,x)|
\le\|M\|_{\mathrm{HS}}.
\tag{17}
\]
The range of \(Q_F\) is contained in that of p and in \(\mathbb C[F]\).
Hence \(T_F=P_FpP_F\) satisfies \(T_FQ_F=Q_FT_F=Q_F\), so \(0\le T_F-Q_F\le1\).
Its trace is \(|F|\alpha-k_F=|F|\delta_F\), and \(\Phi_F(T_F)=r_F\).
Positivity of \(\Phi_F\) and (17) prove the order and coefficient-mass bounds in (2), since
\(\operatorname{Tr}(T_F-Q_F)^2\le |F|\delta_F\).
For any positive group von Neumann element c, Cauchy--Schwarz for its positive trace functional gives \(|c(g)|\le\tau(c)\).
Apply this to \(r_F-b_F\) to obtain the coefficient estimate.
The fixed inequality \(0\le b_F\le p\) from C14 v3 gives the same estimate for \(p-b_F\).
The boundary estimate (3) is exactly the scalar finite-window interface already fixed in C1 v2.

### Translation, orthogonal gluing and overlap

The right translation \(\xi(x)\mapsto\xi(xz^{-1})\) takes \(K_F\) unitarily onto \(K_{Fz}\).
For each translated basis element, convolution gives
\((\xi\lambda_z)(\xi\lambda_z)^*=\xi\xi^*\), proving (4).
If \(F\subset E\), then \(Q_F\le Q_E\), and
\(|E|\Phi_E(Q_F)=|F|b_F\); positivity proves (5).

For disjoint \(F_i\), the sum \(Q_0=\sum_i Q_{F_i}\) is a projection dominated by \(Q_E\).
Thus \(R=Q_E-Q_0\) is a projection of rank d, whose range remains in \(K_E\).
Set \(c=\Phi_E(R)\).
Then c is positive, ac=0, and \(\tau(c)=d/|E|\).
Equation (17) yields \(\|c\|_1\le\|R\|_{\mathrm{HS}}=\sqrt d\), proving (6).
The intersection and sum assertions in (7) follow directly from supports and the same equation \(a\xi=0\).
The dimension formula for two subspaces then gives the inequality.

For instance, whenever E is exactly partitioned into right translates of a single F, (6) gives
\[
\mathcal C_E\le\mathcal C_F+\sqrt d,
\qquad d/|E|=k_E/|E|-k_F/|F|\le\delta_F.
\tag{18}
\]
The resulting error is bounded by \(\sqrt{|E|\delta_F}\).
This is a conditional tiling calculation for arbitrary windows, not an example or an assertion that every Følner set has such a tiling.
It explains why a small density of unmatched kernel directions does not by itself bound their total coefficient correlations.

### Strong sums and the norm estimate

Right translations and coefficient averaging give the positive strong sums
\[
\sum_{z\in G}P_{Ez}=|E|I,\qquad
\sum_{z\in G}Q_{Ez}=|E|b_E.
\tag{19}
\]
To verify the second identity, its (y,x) entry is
\(\sum_{t\in E,\,gt\in E}Q_E(gt,t)\), where \(g=yx^{-1}\), exactly \(|E|b_E(g)\).
Finite partial sums are bounded by the corresponding coordinate sums and hence by \(|E|I\), which justifies strong convergence.
The difference \(R_z=P_{Ez}-Q_{Ez}\) is an orthogonal projection, and summing it gives \(|E|(I-b_E)\).

Let
\[
D_z=\left(\bigcup_{t\in T}t^{-1}Ez\right)
\setminus\left(\bigcap_{t\in T}t^{-1}Ez\right)=D_ez.
\]
For a domain coordinate \(\delta_x\otimes e_j\), the vector \(B(\delta_x\otimes e_j)\) is supported in Tx.
If \(Tx\subset Ez\), it is an exact kernel vector supported in Ez, and is killed by \(R_z\).
If \(Tx\cap Ez\) is empty, it is killed by \(P_{Ez}\) and hence by \(R_z\).
Consequently
\[
R_zB=R_zB(P_{D_z}\otimes I_m),\qquad
B^*R_zB\le\|B\|^2(P_{D_z}\otimes I_m).
\]
Now \(\sum_zP_{D_z}=d_E(T)I\).
Sum the preceding inequality and divide by \(|E|\) to obtain the first estimate in (8).
Since \(0\le1-b_E\le1\), its square is at most itself, proving the second estimate.
For fixed \(t_0\in T\), the set \(D_e\) is contained in \(\bigcup_{t\in T}(t^{-1}E\mathbin\triangle t_0^{-1}E)\), whose relative size tends to zero by the left Følner condition.

The algebraic annihilator is a right ideal and contains every b_E.
Its norm closure J is also a right ideal in \(C_r^*(G)\), by approximation of the right multiplier by group-ring elements.
Equation (8), density and \(\|1-b_E\|\le1\) prove the stated left approximate-identity assertion.
The fixed equality \(\|p-b_E\|=1\) uses the scalar reduced-algebra projection obstruction, as proved in C14 v3; (8) does not alter its scope.

### Cut energies and the half-unit threshold

The multiplier has the positive strong-sum representation
\[
\mathsf M_W(T)=\frac1{|W|}\sum_zP_{Wz}TP_{Wz}.
\tag{20}
\]
For positive T the assertion follows from the same bounded-coordinate-sum argument as (19); it extends to all bounded T by linear decomposition.
The matrix entries are the displayed \(\phi_W\) multiplier.
It is unital and completely positive.
Expanding the squared commutators in (11) and using (20) proves that identity.
If \(r=\mathsf M_W(Q)\), then
\[
\mathsf A_W(Q)=Q(1-r)Q+(1-Q)r(1-Q),
\]
so it is a positive contraction.
Also \(r^2\le r\), and subtracting \((Q-r)^2\) from \(\mathsf A_W(Q)\) leaves \(r-r^2\ge0\).

We use the established [scalar projectionlessness interface](../audits/literature/BCM04/Yin_U001.md#assembly-trace) together with [amenable assembly surjectivity](../audits/literature/HK97/Yin_U001.md#amenable-assembly).
It says that \(C_r^*(G)\) has no projections other than 0 and 1 in the present torsion-free amenable scalar setting.
The following elementary implication is stronger than merely squaring the known distance \(1/2\).
For any nontrivial projection p in the containing von Neumann algebra and any positive contraction \(r\in C_r^*(G)\),
\[
\|p(1-r)p+(1-p)r(1-p)\|\ge\frac12.
\tag{21}
\]
Suppose instead this norm is \(c<1/2\), and put \(d=1/2-c>0\).
In the p and \(1-p\) decomposition, the upper diagonal corner of \(r-1/2\) is at least d and the lower diagonal corner is at most \(-d\).
The upper corner is invertible; its Schur complement in the lower corner is still at most \(-d\), hence invertible.
Thus \(r-1/2\) is invertible as an operator.
The spectral permanence of a unital C*-subalgebra implies its inverse lies in \(C_r^*(G)\).
The two nonzero corners also supply unit vectors with quadratic values of r strictly above and below \(1/2\), so its spectrum meets both sides.
Continuous functional calculus across this gap produces a nontrivial projection in \(C_r^*(G)\), a contradiction.
The constant in this general positive-contraction assertion cannot be improved, since \(r=I/2\) gives equality for every p.

Complete amenable kernel density implies \(Q_{E_j}\to p\) strongly for an increasing exhaustion.
For fixed finite W, \(\mathsf M_W\) is strongly continuous on bounded sets: each output on a coordinate vector uses only the finite set \(\operatorname{supp}\phi_W\), and uniform boundedness extends convergence to all vectors.
Products then converge strongly as well, giving \(\mathsf A_W(Q_{E_j})\to\mathsf A_W(p)\) strongly.
Here \(\mathsf M_W(p)=r_W\in\mathbb CG\).
Lower semicontinuity of the operator norm and (21) prove (12).

### Mean energy versus operator norm

For every finite E, direct matrix trace calculation gives
\[
\operatorname{Tr}\mathsf A_W(Q_E)
=2\sum_{x,y\in E}(1-\phi_W(yx^{-1}))|Q_E(y,x)|^2.
\tag{22}
\]
Put \(T_E=P_EpP_E\).
The coefficient-map proof above gave
\(\|T_E-Q_E\|_{\mathrm{HS}}^2\le |E|\delta_E\), while both Hilbert--Schmidt norms are at most \(\sqrt{|E|}\).
Since \(0\le1-\phi_W\le1\), Cauchy--Schwarz bounds the difference of their normalized weighted squared-entry sums by \(2\sqrt{\delta_E}\).
For \(T_E\), that normalized sum equals
\[
\sum_g\phi_E(g)(1-\phi_W(g))|p(g)|^2.
\]
Along a left Følner sequence, \(\delta_E\to0\) and \(\phi_E(g)\to1\).
Dominated convergence, using \(\sum_g|p(g)|^2=\alpha\), proves (13).
A second application as W becomes Følner proves the iterated zero limit.
More quantitatively, for any \(\eta>0\), the proportion of eigenvalues of the finite positive matrix \(\mathsf A_W(Q_E)\) exceeding \(\eta\) is at most \(\operatorname{Tr}\mathsf A_W(Q_E)/(\eta|E|)\).
Hence density bounds alone permit the large-norm directions required by (12).

### The solid-norm lower bound

For \(b=b^*\), set \(c(g)=|b(g)|\).
Then c is symmetric with nonnegative coefficients, so \(\lambda(c)\) is self-adjoint.
For normalized Følner vectors \(\eta_F=|F|^{-1/2}1_F\),
\[
\langle\lambda(c)\eta_F,\eta_F\rangle
=\sum_g c(g)\phi_F(g)\longrightarrow\sum_g c(g).
\]
The triangle inequality for the regular representation gives the opposite bound, and therefore
\(\|\lambda(c)\|=\|c\|_1=\|b\|_1\).
Faithfulness of the finite trace gives the even-moment formula
\[
\|\lambda(c)\|
=\lim_{n\to\infty}\tau(\lambda(c)^{2n})^{1/(2n)}.
\]
Indeed any spectral interval for \(|\lambda(c)|\) sufficiently close to its norm has a nonzero projection of positive trace, which gives the lower limit; the upper bound is immediate.
But (14) gives
\[
\tau(\lambda(c)^{2n})=c^{2n}(e)
\le C_0M^{2n-1}N(c)^{2n}.
\]
Taking roots proves \(\|b\|_1\le MN(c)\le MK N(b)\), as required.
For (16), submultiplicativity implies \(w(e)\ge1\) and \(w(g)w(g^{-1})\ge w(e)\ge1\).
Use \(|b(g)|=|b(g^{-1})|\) and the arithmetic--geometric mean inequality to pair the two weights.

## Scope and remaining structural input

The boundary estimates (2), (6) and (8), the half-unit obstruction (12), and the norm obstruction (15) are unconditional deductions at their explicit scopes.
They quantify what the available window compatibility supplies and where its control is lost.
In particular (8) is convergence on each fixed algebraic kernel witness, while the trace estimates permit a small set of poorly controlled directions.
No justified step upgrades either statement to uniform control of the full kernel.

The criterion in (12) is an alternative finite-matrix target that avoids total coefficient mass and makes no spectral-gap assumption.
Its implication is proved, but an independent upper estimate below the threshold remains missing.
As with bounded \(\mathcal C_F\), its truth for all actual inputs would settle the scalar amenable problem; merely stating it is not counted as progress toward that proof.
Nor is it asserted to be a strictly weaker logical property of these exact kernels, since zero kernel makes all the quantities vanish.

An unconditional coefficient-norm replacement is excluded by (15), even without assuming spectral invariance of the completion.
A useful next argument must therefore exploit signed or complex same-label cancellations, a genuinely kernel-specific estimate outside (14), or a bound on the largest finite cut-energy directions.
Boundary proportions, rank densities, generic coefficient perturbations and finite generation without inverse control supply none of those estimates here.
The general amenable Atiyah/domain question remains unresolved.

## Assessment history

### Decision reviewed-window-compatibility

| Field | Value |
| --- | --- |
| date | 2026-11-12T14:31 |
| status | proved |
| reason | The complete quantitative window identities, fixed-witness norm bound, half-unit cut-energy obstruction and solid-norm lower bound passed independent review; neither a general correlation upper bound nor a general amenable injectivity theorem is supplied. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact v4 statement](#statement) | Equations (1)–(16), their stated hypotheses, fixed-window and fixed-witness quantifiers, and all sufficient-condition limitations. |
| argument | [Complete v4 argument](#argument) | Coefficient averaging, projection comparison, orthogonal gluing, strong sums, boundary norm estimate, Schur threshold, mean-energy limits and the even-moment norm obstruction. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_A0047_v1.md#whole-argument) | Entire v4 statement, argument, scope and necessary direct interfaces, with accepted external source depths explicit. |
| dependency | [Finite-kernel average](Yin_C_A0014_v3.md#finite-window-kernel-correlation-criterion) | Exact kernel membership, positivity, normalization and the torsion-free amenable norm obstruction for b_F. |
| dependency | [Complete scalar localization](Yin_C_A0001_v2.md#rational-kernel-localization) | The one-column finite-support specialization supplies the boundary deficit and complete Hilbert kernel density. |
| dependency | [BCM04 trace interface](../audits/literature/BCM04/Yin_U001.md#bcm04-u001) | Reduced-algebra assembly trace range used only with HK97 for scalar projectionlessness. |
| dependency | [HK97 assembly interface](../audits/literature/HK97/Yin_U001.md#hk97-u001) | Amenable assembly surjectivity at the recorded external theorem scope. |

The [v3 decision](Yin_C_A0014_v3.md#decision-reviewed-global-obstruction) and its preceding fixed conclusions remain valid.
[Nic08](../audits/literature/Nic08/Yin_U001.md#nic08-u001) supplies related source attribution, not a logical premise for the self-contained coefficient-moment argument.
The [remaining structural input](#scope-and-remaining-structural-input) is expressly unresolved, and this decision does not complete A0001.

## Current assessment

[Selected decision](#decision-reviewed-window-compatibility)

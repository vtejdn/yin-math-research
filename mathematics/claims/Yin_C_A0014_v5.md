---
author: Yin
---
# Localized cut directions and phase-sensitive commutator bounds

This revision continues the fixed-witness and half-unit estimates of [C14 v4](../claims/Yin_C_A0014_v4.md#statement).
It improves the local estimate by removing the convolution condition-number factor, gives a two-scale bound for the exceptional kernel directions, and retains phase cancellation in a finite commutator polynomial of the original input.
It also proves that two proposed coercive upgrades force a spectral gap, so they cannot serve as universal conditions allowing continuous spectrum at zero.
No concrete example is tested, and no independent general bound below one half or uniform bound on the coefficient correlations is claimed.

## Statement

### Conventions

Let G be finitely generated, let \(0\ne a\in\mathbb CG\), and put \(H=a^*a\), \(p=P_{\ker a}\), \(q=1-p\), and \(\alpha=\tau(p)<1\).
The coordinate projections \(P_T\), exact finite-kernel projections \(Q_T\), dimensions \(k_T\), convolution averages \(b_T\), overlap functions \(\phi_W\), Schur multipliers \(\mathsf M_W\), and cut energies \(\mathsf A_W\) have the [v4 conventions](../claims/Yin_C_A0014_v4.md#setup-and-coefficient-averaging).
Write \(r_W=\mathsf M_W(p)\), and, for finite nonempty T and W, set
\[
\beta_W(T)=\frac1{|W|}
\left|\left(\bigcup_{t\in T}t^{-1}W\right)
\setminus\left(\bigcap_{t\in T}t^{-1}W\right)\right|.
\]
Coefficient norms, Hilbert-space norms and operator norms remain distinct.
All positive spectral cutoffs below use a fixed \(0<\eta<1\).

### Local directions without a convolution condition number

For any orthogonal projection Q on \(\ell^2(G)\), and any vector \(\xi\) supported in T with either \(Q\xi=\xi\) or \(Q\xi=0\),
\[
\langle\xi,\mathsf A_W(Q)\xi\rangle
\le\beta_W(T)\|\xi\|_2^2.
\tag{1}
\]
Consequently, for \(T\subset E\),
\[
Q_T\mathsf A_W(Q_E)Q_T\le\beta_W(T)Q_T,
\qquad
Q_T(1-b_W)Q_T\le\beta_W(T)Q_T.
\tag{2}
\]
The bound is uniform over E and over the unit sphere of the specified local space \(K_T\).
It contains no factor \(\|\lambda(\xi)\|/\|\xi\|_2\).

Define the finite kernel-side high-energy projection
\[
h^+_{W,\eta,E}=Q_E1_{[\eta,1]}(\mathsf A_W(Q_E)).
\]
The factors commute, and
\[
\|h^+_{W,\eta,E}Q_T\|
\le\sqrt{\beta_W(T)/\eta}.
\tag{3}
\]
The same bound holds with \(h^+_{W,\eta}=p1_{[\eta,1]}(\mathsf A_W(p))\).
For the latter von Neumann projection,
\[
\tau(h^+_{W,\eta})
\le\delta_T+\frac{\beta_W(T)}{\eta}\frac{k_T}{|T|},
\qquad \delta_T=\alpha-k_T/|T|.
\tag{4}
\]
If G is amenable and \(\operatorname{supp}a\subset B_w\), one may replace \(\delta_T\) by \(|\partial_wT|/|T|\).
Thus (4) supplies a bound using finite kernel data and group-window geometry, without an unknown atom size on its right side.
It bounds dimension, not the largest energy.

### The actual boundary space behind the compression defect

Let \(S=\operatorname{supp}a\), and put
\[
I_W=\bigcap_{s\in S}sW,\quad O_W=SW\setminus I_W,
\quad
L_W=\ker(P_{I_W}a|_{\mathbb C[W]}).
\]
The boundary map \(B_W:L_W\to\mathbb C[O_W]\) is the restriction of \(P_{O_W}a\).
Its kernel is \(K_W\).
If \(P_{L_W}\) is the local weak-solution projection, then
\[
0\le P_WpP_W-Q_W\le P_{L_W}-Q_W,
\qquad
\operatorname{rank}(P_WpP_W-Q_W)\le\operatorname{rank}B_W\le|O_W|.
\tag{5}
\]
Extend \(B_W\) to \(\mathbb C[W]\) by composition with \(P_{L_W}\).
The remaining finite projection has the exact formula
\[
P_{L_W}-Q_W=B_W^*(B_WB_W^*)^\dagger B_W,
\tag{6}
\]
where the dagger denotes the finite-dimensional Moore--Penrose inverse.
No bound on that inverse or on the spatial locality of this projection is asserted.
The formula uses the original equal-displacement coefficients, including every relation among products in G.

### A finite phase-sensitive commutator polynomial

For the original a and finite W, define
\[
\Gamma_W(a)=\mathsf M_W(aa^*)-\mathsf M_W(a)a^*
-a\mathsf M_W(a^*)+aa^*.
\tag{7}
\]
This is a positive element of \(\mathbb CG\), and
\[
a r_Wa^*\le\Gamma_W(a)
=\frac1{|W|}\sum_z[a^*,P_{Wz}]^*[a^*,P_{Wz}].
\tag{8}
\]
For \(a=\sum_s a_s\lambda_s\), its coefficients are exactly
\[
\Gamma_W(a)=\sum_{s,t}a_s\overline{a_t}
\bigl[\phi_W(st^{-1})-\phi_W(s)-\phi_W(t^{-1})+1\bigr]
\lambda_{st^{-1}}.
\tag{9}
\]
Thus all terms with the same actual displacement are combined before taking its norm.
In particular, with
\[
\nu_W=\|\Gamma_W(a)\|,\qquad
\epsilon_W(a)=\sum_s|a_s|\sqrt{2(1-\phi_W(s))},
\]
one has \(0\le\Gamma_W(a)\le\epsilon_W(a)^2I\).
Both \(\nu_W\) and \(\epsilon_W(a)\) tend to zero along a left Følner sequence, without a spectral-gap assumption.

There is a corresponding matrix estimate for every finite row B with \(aB=0\):
\[
B^*(1-r_W)B\le
\mathsf M_W(B^*B)-\mathsf M_W(B^*)B
-B^*\mathsf M_W(B)+B^*B.
\tag{10}
\]
The multiplier is applied entrywise at the appropriate matrix sizes.
These are finite phase-sensitive bounds on fixed input forms, not a uniform bound on the full kernel.

### Complementary high energies lie near the small positive spectrum

For \(\lambda>0\), let \(e_\lambda=1_{[\lambda,\infty)}(H)\).
Then
\[
e_\lambda r_W e_\lambda\le(\nu_W/\lambda)e_\lambda.
\tag{11}
\]
Define \(h^-_{W,\eta}=q1_{[\eta,1]}(\mathsf A_W(p))\).
Whenever \(\nu_W<\eta\lambda\),
\[
\tau(h^-_{W,\eta})\le\tau(1_{(0,\lambda)}(H)).
\tag{12}
\]
More explicitly, if \(\zeta\in q\ell^2(G)\) is a unit vector with \(\langle r_W\zeta,\zeta\rangle\ge c>0\), and \(u=\|1_{(0,\lambda)}(H)\zeta\|\), then
\[
\sqrt c\le u+\sqrt{\nu_W/\lambda}\sqrt{1-u^2}.
\tag{13}
\]
The interval in (12) excludes zero, so it retains the continuous small-positive-spectrum contribution instead of counting the original atom again.

### Two coercive upgrades force a gap

For finite nonempty W, let \(\gamma_W(H)\) be the smallest strictly positive eigenvalue of \(P_WH P_W\) on \(\mathbb C[W]\).
This number exists and is positive.
Set \(\varepsilon_W(H)=\|\mathsf M_W(H)-H\|\).
Then
\[
\mathsf M_W(H)\ge\gamma_W(H)(1-b_W),\qquad
H+\gamma_W(H)b_W\ge(\gamma_W(H)-\varepsilon_W(H))I.
\tag{14}
\]
If G is torsion-free amenable and \(\varepsilon_W(H)<\gamma_W(H)\), it follows that
\[
p=0,\qquad H\ge(\gamma_W(H)-\varepsilon_W(H))I.
\tag{15}
\]

Similarly, suppose for some finite W and finite \(C\ge0\) that the relative form estimate
\[
\Gamma_W(a)\le Caa^*
\tag{16}
\]
holds.
Let f=a*, and let \(\gamma_W(f^*f)>0\) be the analogous finite positive eigenvalue.
For every group in the setup and every \(\zeta\perp\ker f\),
\[
\|f\zeta\|_2^2\ge
\frac{\gamma_W(f^*f)}{(1+\sqrt C)^2}\|\zeta\|_2^2.
\tag{17}
\]
Thus (16), even with arbitrarily large finite C, forces closed range.
For torsion-free amenable G it forces a to be boundedly invertible, with the corresponding positive gap for both \(aa^*\) and \(a^*a\).
Neither (15) nor (16) is a universal atom-only condition compatible with continuous spectrum accumulating at zero.

## Argument

### Local energy and exceptional-direction dimension

Use the exact [cut-commutator identity](../claims/Yin_C_A0014_v4.md#cut-energies-and-the-half-unit-threshold).
If \(T\subset Wz\) or \(T\cap Wz\) is empty, the assumptions \(Q\xi=\xi\) or \(Q\xi=0\) make \([Q,P_{Wz}]\xi=0\).
The remaining z form exactly
\((\bigcup_{t\in T}W^{-1}t)\setminus(\bigcap_{t\in T}W^{-1}t)\).
Inversion identifies their number with \(|W|\beta_W(T)\).
In the first sector the commutator on \(\xi\) is \(-(1-Q)P_{Wz}\xi\); in the second it is \(QP_{Wz}\xi\).
Each has norm at most \(\|\xi\|_2\), proving (1).
Apply this to \(Q_E\) and \(\xi\in K_T\) to prove the first part of (2).
For its second part use \(\sum_z(P_{Wz}-Q_{Wz})=|W|(1-b_W)\); the same inside, outside and cutting-support argument applies to exact finite kernel vectors.

The cut energy commutes with Q because it is diagonal in Q and its complement.
Hence \(\eta h^+_{W,\eta,E}\le\mathsf A_W(Q_E)\), and compression by \(Q_T\) gives (3).
The proof with p is identical.
For an orthonormal basis \((\xi_i)\) of \(K_T\),
\[
\tau(h^+b_T)=\frac1{|T|}\sum_i\|h^+\xi_i\|_2^2
\le\frac{\beta_W(T)}{\eta}\frac{k_T}{|T|}.
\]
Here h+ belongs to the group von Neumann algebra, so the trace of each convolution square is the displayed Hilbert-space quadratic form.
Also \(0\le p-b_T\) and \(h^+\le p\), giving \(\tau(h^+(p-b_T))\le\delta_T\).
This proves (4); its boundary-only version uses the fixed [scalar localization estimate](../claims/Yin_C_A0001_v2.md#rational-kernel-localization).

### Boundary factorization with the actual coefficients

For every \(y\in I_W\), all coordinates \(s^{-1}y\), \(s\in S\), lie in W.
Thus \(a(P_Wp\zeta)(y)=ap\zeta(y)=0\), using the same coefficients at each occurrence of a label.
This proves \(\operatorname{ran}(P_WpP_W)\subset L_W\).
The output of a vector supported in W lies in SW.
Vanishing on both \(I_W\) and \(O_W\) is therefore exactly the full equation \(a\xi=0\), proving \(\ker B_W=K_W\).
As in v4, \(P_WpP_W-Q_W\) is a positive contraction supported on the orthogonal complement of \(K_W\).
Its range is also contained in \(L_W\), so it is dominated by \(P_{L_W}-Q_W\).
The latter projection has rank \(\operatorname{rank}B_W\), proving (5).
The singular-value decomposition of the finite map B_W gives (6), including the zero-rank case.
This identity alone does not bound the nonzero singular values away from zero.

### Phase-sensitive commutator forms

The positive-definite overlap function has the isometry realization
\(V\delta_x=\delta_x\otimes\pi(x^{-1})\xi_W\), where \(\xi_W=|W|^{-1/2}1_W\) and \(\pi\) is the left regular representation.
Thus \(\mathsf M_W(T)=V^*(T\otimes I)V\).
Put \(\Pi=p\otimes I\) and \(D=(a^*\otimes I)V-Va^*\).
Since \(pa^*=0\), one has \(\Pi D=-\Pi Va^*\).
Consequently
\[
a r_Wa^*=D^*\Pi D\le D^*D=\Gamma_W(a).
\]
Expansion of D*D proves (7), while expansion of the coordinate-cut commutators proves the strong-sum identity in (8).
The finite polynomial expansion is exactly (9).
In particular group products that coincide have not been separated or randomized.
For each group unitary,
\(\|(\lambda_s\otimes I)V-V\lambda_s\|=\sqrt{2(1-\phi_W(s))}\).
The triangle inequality applied to D gives \(\Gamma_W(a)\le\epsilon_W(a)^2I\).
Since a has fixed finite support, the left Følner condition gives the asserted convergence.

For a kernel row B, use the amplified isometry \(V_m\) and
\(D_B=(B\otimes I)V_m-VB\).
The equality \(pB=B\) gives \((1-\Pi)D_B=-(1-\Pi)VB\).
Hence \(B^*(1-r_W)B=D_B^*(1-\Pi)D_B\le D_B^*D_B\).
Expanding the last expression proves (10), with all matrix sizes retained.

### Small-positive-spectrum concentration

The bounded operator \(T_\lambda=aH^{-1}e_\lambda\) satisfies
\(a^*T_\lambda=e_\lambda\) and \(T_\lambda^*T_\lambda=H^{-1}e_\lambda\le\lambda^{-1}e_\lambda\).
The inverse is used only on the indicated positive spectral subspace.
Equation (8) therefore gives
\[
e_\lambda r_W e_\lambda
=T_\lambda^*a r_W a^*T_\lambda
\le\nu_W T_\lambda^*T_\lambda,
\]
which proves (11).
On the q corner, \(\mathsf A_W(p)=q r_Wq\).
If \(\nu_W<\eta\lambda\), a vector in both \(h^-_{W,\eta}\) and \(e_\lambda\) would have its r_W quadratic form both at least \(\eta\) and at most \(\nu_W/\lambda\) times its squared norm.
Their intersection is therefore zero.
Both projections lie below q, so the finite von Neumann dimension inequality gives
\(\tau(h^-_{W,\eta})\le\tau(q-e_\lambda)\), exactly (12).
For (13), split \(\zeta\) into its \((0,\lambda)\) and \([\lambda,\infty)\) parts and apply the triangle inequality to \(r_W^{1/2}\zeta\), using \(0\le r_W\le1\) on the first part and (11) on the second.

### Why local positive gaps and relative forms are overstrong

For every nonzero finite convolution f, each column \(f\delta_x\) is nonzero.
Hence \(P_Wf^*fP_W\) has nonzero positive spectrum, and its zero space is precisely \(K_W(f)\).
Finite-dimensional spectral calculus gives
\[
P_Wf^*fP_W\ge\gamma_W(f^*f)(P_W-Q_W(f)).
\]
Translate and average this inequality as in v4 to obtain
\(\mathsf M_W(f^*f)\ge\gamma_W(f^*f)(1-b_W(f))\).
Taking f=a and comparing with H proves (14).
If \(\varepsilon_W(H)<\gamma_W(H)\), compression to p shows that b_W is bounded below by a positive multiple of p.
Since \(0\le b_W\le p\), its support projection is then p and belongs to \(C_r^*(G)\).
The [BCM04/HK97 scalar projection interface](../audits/literature/BCM04/Yin_U001.md#assembly-trace) for torsion-free amenable groups gives \(p=0\), because a is nonzero.
Now every finite kernel is zero, so \(b_W=0\), and (14) yields the full gap in (15).

For (16), set f=a* and use the Hilbert direct sum over the translated windows.
The identity \(fP_{Wz}=P_{Wz}f+[f,P_{Wz}]\) and Minkowski's inequality give
\[
\left(\frac1{|W|}\sum_z\|fP_{Wz}\zeta\|_2^2\right)^{1/2}
\le\|f\zeta\|_2+\langle\Gamma_W(a)\zeta,\zeta\rangle^{1/2}
\le(1+\sqrt C)\|f\zeta\|_2.
\]
The already proved local spectral inequality bounds the squared left side below by
\(\gamma_W(f^*f)\langle(1-b_W(f))\zeta,\zeta\rangle\).
When \(\zeta\perp\ker f\), the exact finite kernel element b_W(f) kills \(\zeta\).
This proves (17), including its constant, and proves closed range without any amenability assumption.
In the torsion-free amenable case the resulting gap between zero and the positive spectrum of \(aa^*\) places its kernel projection in \(C_r^*(G)\).
Projectionlessness excludes that kernel because a* is nonzero.
Thus \(aa^*\) is bounded below by the constant in (17).
Finite-trace polar decomposition gives the same zero kernel dimension for a and a*, and transfers the nonzero spectral lower bound to \(a^*a\).
Hence a is boundedly invertible and the claimed gap consequence follows.

## What the estimates do and do not settle

The local energy estimate (1) and the finite boundary factorization (5) are independent bounds that retain the actual group relations and equal-label coefficients.
Equation (4) turns them into a two-scale quantitative bound for the dimension of high kernel-side cut directions.
Equations (7)–(13) preserve phase cancellation in a finite input polynomial and force complementary high-energy directions toward the small positive spectrum.
These are more precise constraints than mere density or a reformulation of zero kernel.

They still allow nonzero high-energy projections of arbitrarily small trace.
The fixed [half-unit obstruction](../claims/Yin_C_A0014_v4.md#finite-cut-energy-and-its-nonlocal-lower-bound) is an operator-norm statement and does not disappear when those traces are small.
No uniform support or stable synthesis estimate at the required relative scales is proved here.
Finite propagation of a alone does not establish such a propagation bound for its finite or infinite kernel projections.

The straightforward positive-gap and relative-commutator upgrades are now excluded as universal atom-only routes by (15)–(17), rather than left as unchecked possible repairs.
In particular, replacing an absolute error bound by \(\Gamma_W(a)\le Caa^*\) does not preserve the desired allowance for continuous zero spectrum.
The remaining question is whether same-label relations yield an additional signed estimate that controls the high-energy directions without any of these gap-forcing assumptions.
No general upper bound below one half, no uniform \(\mathcal C_F\) bound, no new group class and no solution of the amenable Atiyah/domain problem is supplied.

## Assessment history

### Decision reviewed-cut-localization

| Field | Value |
| --- | --- |
| date | 2026-11-12T15:13 |
| status | proved |
| reason | Independent whole-proof review verifies the local cut bounds, boundary factorization, phase-sensitive forms, exceptional-direction dimension bounds and two gap-forcing implications; no general cut-norm or coefficient-mass upper bound is established. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact v5 statement](#statement) | All seventeen equations and their hypotheses, local support quantifiers, spectral endpoints, convergence assertions and gap-forcing consequences. |
| argument | [Complete v5 argument](#argument) | Support-cut counting, finite boundary equations, Stinespring forms, spectral compression, projection dimension and both coercive implications. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_A0048_v1.md#whole-argument) | Complete statement, argument, limits and necessary direct input interfaces, with no claimed general-problem solution. |
| dependency | [Finite-window conventions and averages](Yin_C_A0014_v4.md#setup-and-coefficient-averaging) | Exact finite kernel averages, positivity, coefficient orientation and trace normalization. |
| dependency | [Translated positive sums](Yin_C_A0014_v4.md#strong-sums-and-the-norm-estimate) | Coordinate and finite-kernel projection sums for the local estimates and finite positive-gap comparisons. |
| dependency | [Cut identities and half-unit obstruction](Yin_C_A0014_v4.md#cut-energies-and-the-half-unit-threshold) | Commutator representation, block decomposition and the norm obstruction retained in the scope conclusions. |
| dependency | [Scalar localization](Yin_C_A0001_v2.md#rational-kernel-localization) | One-column bounded group-ring specialization supplies the boundary-only replacement for the trace deficit. |
| dependency | [BCM04 trace interface](../audits/literature/BCM04/Yin_U001.md#bcm04-u001) | Reduced-algebra scalar projectionlessness consequence combined with HK97, only under torsion-free amenability. |
| dependency | [HK97 assembly interface](../audits/literature/HK97/Yin_U001.md#hk97-u001) | Countable amenable assembly surjectivity at the existing accepted source depth. |

The [v4 decision](Yin_C_A0014_v4.md#decision-reviewed-window-compatibility) remains valid at its fixed scope.
The [remaining norm-control problem](#what-the-estimates-do-and-do-not-settle) is unresolved, and this decision does not complete A0001.

## Current assessment

[Selected decision](#decision-reviewed-cut-localization)

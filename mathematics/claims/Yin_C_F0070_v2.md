---
author: Yin
---
# Starred derivations from bare normal duals and the canonical full-domain equivalence

Date: 2026-10-16.
Human author Yin; the coordinating authoring agent developed and checked this approved alternative proof.
The statement and the arguments after the single-normal-operator step are retained from v1.
The new argument replaces the finite-overlap smooth partition by continuous cutoffs for spectral cells with null boundaries, followed by finite unitary averaging.
It also states the scalar-c version for diffuse normal operators.
No normal-part or Banach-bidual construction is used.

## Proof versions

The [original complete proof](Yin_C_F0070_v1.md#argument), dated 2026-10-14, and its [independent review](../audits/reviews/Yin_R_F0043_v1.md#conclusion) remain fixed at their original scope.
The [cutoff proof below](#proof-by-continuous-cutoffs-and-finite-averaging), dated 2026-10-16, is the current alternative proof.
Its changed step and assembly with the retained tuple, canonical-domain and vacuum arguments are covered by the [scoped self-review](../audits/reviews/Yin_R_F0052_v1.md#conclusion); the original independent review does not transfer to the changed proof.
The selected decision identifies the actual assessment and evidence.

## Current assessment
[Selected decision](#decision-cutoff-reviewed)

## Statement

Let (M,tau) be a finite von Neumann algebra with faithful normal tracial state, H=L2(M,tau), Omega=1, and P=P_Omega.
Let X=(X_1,...,X_d) be a bounded normal generating tuple and A=C<X,X*> the represented starred polynomial algebra.

**A. Automatic starred derivations.**
Suppose only that complex-linear maps D_i:M Omega -> H satisfy [X_j,D_i]=delta_ij P on M Omega.
Put
\[
 E_i(a\Omega)=-D_i(a\Omega)+aD_i\Omega.
\]
Then there exists a unique outer-bimodule derivation
\[
 \delta_i:A\longrightarrow H\otimes_2H,\qquad
 \delta_i(X_j)=\delta_{ij}\Omega\otimes\Omega.
\]
Every marginal law mu_j is diffuse.
Its starred values are
\[
 \delta_i(X_j^*)=\delta_{ij}k_j,\qquad
 k_j(z,w)=\frac{\bar z-\bar w}{z-w}\ (z\ne w),\qquad k_j(z,z)=0.
\]
Here k_j belongs to the marginal abelian tensor subspace.
With Theta(a tensor b)=aPb,
\[
 [E_i,a]=\Theta(\delta_i a)|_{M\Omega},\qquad
 E_i(a\Omega)=(\mathrm{id}\otimes\tau)\delta_i(a)\quad(a\in A).
\]
In particular the contraction is bounded from the operator norm on A to H.
No Hilbert-space closability or adjoint premise on the supplied D_i is assumed.
No vacuum-adjoint conclusion follows from Part A alone in this statement.

**B. Exact comparison under ACSY24.**
Suppose that the same normal tuple satisfies the ACSY24 hypothesis: derivations partial_i:A -> H tensor_2 H satisfy partial_i(X_j)=delta_ij Omega tensor Omega and have actual vacuum adjoints.
Set E_i0=(id tensor tau)partial_i on A Omega and E_i^can=closure(E_i0), as in ACSY24 Theorem 3.4.
The following are equivalent:

1. M Omega is contained in Dom E_i^can for every i.
2. Some bare full-domain linear dual system as in Part A exists.
3. The same E_i0 have full-domain linear extensions E_i:M Omega -> H satisfying [E_i,X_j]=delta_ij P.

In condition 2 the normalized supplied duals agree with the canonical operators on A Omega.
Equality on all M Omega and closability of the supplied full-domain maps are not asserted.

**C. Vacuum corollary.**
Under Part A, if additionally Omega belongs to Dom D_i* for every i, then the unique derivations satisfy the ACSY24 actual vacuum-adjoint condition.
Their vacuum vectors are
\[
 \delta_i^*(\Omega\otimes\Omega)
      =-D_i^*\Omega+(D_i\Omega)^*.
\]
The involution on the final L2 vector is the tracial involution.
This corollary does not require a priori density of Dom D_i*.

## Argument

### Statement and interfaces

Let `(M,tau)` be a finite von Neumann algebra with faithful normal tracial state, let `H=L2(M,tau)`, and put `Omega=1` and `P=P_Omega`.
Identify `M` with `M Omega`.
Suppose that x is bounded and normal and that a bounded complex-linear map `E:M -> H`, with the operator norm on M, satisfies `[E,x]=P` on M.
Then x has diffuse spectral distribution mu and

\[
 [E,x^*]=K_x\big|_M,
 \qquad K_x=\Theta(k_x),\qquad
 k_x(z,w)=\begin{cases}
 (\bar z-\bar w)/(z-w),&z\ne w,\\
 0,&z=w.
 \end{cases}                                                   \tag{S1}
\]

Here the scalar spectral realization identifies `L2(W*(x)) tensor_2 L2(W*(x))` with `L2(mu tensor mu)`, and this is a closed subspace of `H tensor_2 H`.
The unitary coarse-tensor identification is

\[
 \Theta:H\otimes_2 H\longrightarrow S_2(H),
 \qquad \Theta(a\otimes b)=aPb\quad(a,b\in M).
\]

In particular `||K_x||HS=1`.
No Hilbert-space closability of E or adjoint-domain premise is assumed.
If a bounded map E instead satisfies `[E,x]=0`, the conclusion is `[E,x*]=0`; this homogeneous assertion does not require diffuseness.

The kernel construction is the one in [C_F0037](Yin_C_F0037_v1.md#statement).
That earlier proof uses closability to pass from continuous functions to spectral projections.
The proof below replaces that passage by continuous cutoffs for spectral cells with null boundaries; the limits act on fixed Hilbert-space vectors and never pass through E or F.
Its additional published input is the bounded-map Fuglede implication from [CS77-U001](../audits/literature/CS77/Yin_U001_v1.md#cs77-u001): a bounded map `F:M -> H` commuting with left multiplication by a normal x also commutes with left multiplication by x*.
The argument below does not assume normality or weak continuity of E as a Banach-space map.

### Proof by continuous cutoffs and finite averaging

First, if `p=1_{lambda}(x)` is a spectral atom and `[E,x]=P`, then `(x-lambda)E(p)=-tau(p)Omega`.
Multiplication on the left by p gives `tau(p)p=0`; faithfulness forces p=0.
Thus mu is diffuse.
For the remainder, allow `[E,x]=cP` with any complex c and assume that mu is diffuse, as just proved when c=1.
This gives the more general scalar-c interface.
The phase kernel has modulus one off the product-null diagonal and satisfies

\[
 [K_x,x]=[P,x^*].                                               \tag{S2}
\]

Put `C=||E||_{B(M,H)}` and `F=[E,x*]-cK_x|M`.
The map F is bounded from the operator norm on M to H; no bound on F as an operator on H is asserted.
Jacobi's identity and normality give

\[
 [F,x]=[[E,x],x^*]-c[K_x,x]=0.                                 \tag{S3}
\]

The bounded-map Fuglede implication gives `[F,x*]=0`.
Products and uniform approximation therefore give `F(f(x)a)=f(x)F(a)` for every continuous f on `K=sigma(x)` and every a in M.

For epsilon>0, choose a finite Borel partition `B_1,...,B_m` of K, discarding zero spectral projections, with

\[
 \operatorname{diam}B_r\le\varepsilon,
 \qquad \mu(\partial_K B_r)=0.                                \tag{S4}
\]

A rectangular grid with sufficiently small cells supplies such a partition: choose its vertical and horizontal lines outside the countably many lines of positive mu measure and assign the boundary points to adjacent cells.
Write `e_r=1_{B_r}(x)`; the retained projections sum to one.
For each such projection e, continuous functions g_n,h_n on K with values in [0,1] can be chosen to vanish outside the interiors of its cell and its complement, respectively, with

\[
 g_n(x)e=g_n(x),\qquad h_n(x)e=0,\qquad
 g_n(x)\longrightarrow e,\quad h_n(x)\longrightarrow1-e
 \quad\hbox{strongly on }H.                                  \tag{S5}
\]

For example, use continuous distance cutoffs increasing to the indicators of those two relative interiors.
The discrepancy from the cell indicators is supported on its null boundary; faithfulness of tau makes that spectral projection zero on all H, so bounded spectral convergence gives (S5).
For every a in M the continuous module relation gives

\[
 g_n(x)F(ea)=F(g_n(x)ea)=g_n(x)F(a),\qquad
 h_n(x)F(ea)=0.
\]

Taking strong limits on the fixed vectors F(ea) and F(a) yields `eF(ea)=eF(a)` and `(1-e)F(ea)=0`.
Consequently

\[
 F(e_ra)=e_rF(a)\quad(a\in M).                                \tag{S6}
\]

No limit is taken through either of the possibly nonnormal maps E and F.
Choose lambda_r in B_r and define `x_epsilon=sum_r lambda_r e_r` and `E_epsilon(a)=sum_r e_r E(e_r a)`.
For signs sigma in `{1,-1}^m`, the elements `u_sigma=sum_r sigma_r e_r` are unitary and

\[
 E_\varepsilon(a)=2^{-m}\sum_\sigma u_\sigma E(u_\sigma a),
 \qquad \|E_\varepsilon\|_{B(M,H)}\le C.                      \tag{S7}
\]

Since E_epsilon commutes with x_epsilon* and `||x-x_epsilon||<=epsilon`,

\[
 \|[E_\varepsilon,x^*]\|_{B(M,H)}
 \le2\varepsilon C.                                          \tag{S8}
\]

Under Theta inverse, the operator `sum_r e_r K_x e_r` has kernel

\[
 k_x(z,w)\sum_r1_{B_r}(z)1_{B_r}(w).                          \tag{S9}
\]

Its absolute value is bounded by `1_{|z-w|<=epsilon}`.
The diagonal has zero product measure by diffuseness, so dominated convergence gives convergence to zero in Hilbert--Schmidt norm.
By (S6), `F=sum_r e_r F e_r=[E_epsilon,x*]-c(sum_r e_r K_x e_r)|M`.
Together with `||a Omega||2<=||a||`, this yields

\[
 \|F\|_{B(M,H)}\le2\varepsilon C+
 |c|\left\|\sum_r e_rK_xe_r\right\|_{\mathrm{HS}}
 \longrightarrow0.                                         \tag{S10}
\]

Thus `[E,x*]=cK_x|M`, proving (S1) when c=1 and the stated general scalar version for diffuse x.
If `[E,x]=0` without a diffuseness assumption, the bounded-map Fuglede implication applies directly to E and gives `[E,x*]=0`.

### Bare normal tuples determine starred-core derivations

Let the bounded normal tuple `X=(X_1,...,X_d)` generate M, and suppose that complex-linear maps `D_i:M Omega -> H` satisfy `[X_j,D_i]=delta_ij P` on all M Omega.
Put

\[
 E_i(a\Omega)=-D_i(a\Omega)+aD_i\Omega.                         \tag{S11}
\]

Then `E_i Omega=0` and `[E_i,X_j]=delta_ij P`.
[C_F0069, Part A](Yin_C_F0069_v1.md#statement) makes each D_i, and hence each E_i, bounded from M to H, and makes the marginal laws mu_j diffuse.
Apply (S1) with x=X_i to the diagonal relation.
For j unequal to i apply the homogeneous assertion to E_i and X_j.
The result is

\[
 [E_i,X_j^*]=\delta_{ij}K_j\big|_M,
 \qquad K_j=\Theta(k_j).                                      \tag{S12}
\]

Let `A=C<X_1,...,X_d,X_1*,...,X_d*>`.
Repeated use of the commutator product rule shows that `[E_i,a]` on M is the restriction of a Hilbert--Schmidt operator T_i(a) for every a in A: the generator commutators are P or K_j, and multiplication on either side by a bounded polynomial preserves the Hilbert--Schmidt class.
The extension is unique since M Omega is dense in H.
It depends on the represented element a rather than its word representation, because a zero represented element has zero commutator on M.
Define

\[
 \delta_i(a)=\Theta^{-1}(T_i(a))\quad(a\in A).                  \tag{S13}
\]

The outer-bimodule compatibility `Theta(a dot eta dot b)=a Theta(eta)b` and the commutator product rule prove that delta_i is a derivation on the actual starred algebra A.
Its generator values are

\[
 \delta_i(X_j)=\delta_{ij}(\Omega\otimes\Omega),\qquad
 \delta_i(X_j^*)=\delta_{ij}k_j.                               \tag{S14}
\]

Also, because `E_i Omega=0` and `Theta(eta)Omega=(id tensor tau)eta`,

\[
 E_i(a\Omega)=(\mathrm{id}\otimes\tau)\delta_i(a)
 \qquad(a\in A).                                             \tag{S15}
\]

This conclusion establishes the derivation part of the ACSY24 hypotheses from the bare full-domain dual premise for normal tuples.
It does not yet establish `Omega tensor Omega in Dom delta_i*`.
In particular, neither delta_i nor E_i is declared Hilbert-space closable here merely from the operator-norm continuity already proved.

There is also uniqueness of these derivations, without an adjoint premise.
Suppose that `partial_i:A -> H tensor_2 H` is any outer-bimodule derivation with `partial_i(X_j)=delta_ij Omega tensor Omega`.
For a fixed j, define

\[
 L_j=\lambda(X_j)\otimes I-I\otimes\rho(X_j)
 \quad\text{on }H\otimes_2H.
\]

Here lambda and rho denote left and right multiplication on the indicated tensor leg.
The spectral projection of L_j onto its kernel is the joint spectral projection of `z=w`.
The joint trace on the two commuting spectral algebras is the faithful product trace with distribution `mu_j tensor mu_j`; diffuseness makes that projection zero.
Thus L_j is injective on the entire coarse Hilbert space, not just on its abelian subspace.
Differentiating `X_j X_j*=X_j* X_j` gives

\[
 L_j\partial_i(X_j^*)
   =\delta_{ij}(X_j^*\otimes\Omega-\Omega\otimes X_j^*).        \tag{S16}
\]

The vector `delta_ij k_j` solves this equation in the abelian tensor subspace.
Injectivity therefore forces `partial_i(X_j*)=delta_ij k_j`.
The derivations partial_i and delta_i agree on every generator and adjoint, hence on A.
This is the phase-uniqueness mechanism already checked in [C_F0025, Section 3](Yin_C_F0025_v1.md#yin_c_f0025), applied here without an adjoint hypothesis.

### Exact equivalence under the ACSY24 hypotheses

Assume now that the normal generating tuple satisfies ACSY24 Proposition 3.5: on A there are derivations partial_i with the displayed generator values and `Omega tensor Omega in Dom partial_i*`.
Let

\[
 E_{i,0}=(\mathrm{id}\otimes\tau)\partial_i\big|_A,
 \qquad E_i^{\mathrm{can}}=\overline{E_{i,0}},                  \tag{S17}
\]

where the closure exists by [ACSY24, Theorem 3.4](../literature/pdf/ACSY24.pdf), with its exact actual-core interface checked in [ACSY24-U001](../audits/literature/ACSY24/Yin_U001_v1.md#acsy24-u001).
Then the following three conditions are equivalent:

1. `M Omega subset Dom E_i^can` for every i.
2. There exists a bare complex-linear full-domain dual system `D_i:M Omega -> H`, `[X_j,D_i]=delta_ij P`.
3. For each i, the same canonical polynomial operator E_i0 admits a complex-linear extension `E_i:M Omega -> H` satisfying `[E_i,X_j]=delta_ij P` on all M Omega.

Condition 3 implies condition 2 by changing signs.
To prove 2 implies 1, normalize the supplied full-domain duals by (S11).
Equations (S12)--(S16) show that their associated starred-core derivations equal the given partial_i.
Equation (S15) then proves that their restrictions to the *entire starred core* equal E_i0.
Their automatic bounds give constants C_i such that

\[
 \|E_{i,0}(p\Omega)\|_2\le C_i\|p\|\qquad(p\in A).           \tag{S18}
\]

For completeness, fix a in M and choose, by Kaplansky density and uniform approximation in C*(X), a uniformly norm-bounded net `p_alpha in A` with `p_alpha Omega -> a Omega` in H.
The vectors E_i0(p_alpha Omega) are bounded by (S18), hence have a weakly convergent subnet.
The graph of the closed linear operator E_i^can is a norm-closed linear subspace of `H direct_sum H`, so it is weakly closed.
The pair consisting of the strong limit of the first components and the weak limit of the second components belongs to that graph.
Therefore a Omega belongs to Dom E_i^can.
This is precisely the graph restoration mechanism of [C_F0027, Section 5](Yin_C_F0027_v1.md); it gives membership in the original canonical closure.

Finally, assume 1.
On A, `[E_i0,X_j]=delta_ij P`.
If `v in Dom E_i^can`, approximate v in the graph norm by elements of A Omega.
Boundedness of X_j and P and closedness of E_i^can show

\[
 X_jv\in\operatorname{Dom}E_i^{\mathrm{can}},\qquad
 E_i^{\mathrm{can}}X_jv
   =X_jE_i^{\mathrm{can}}v+\delta_{ij}Pv.                     \tag{S19}
\]

Its restriction to M Omega thus supplies the extension in 3.

The equivalence means that, under ACSY24 and normality, an arbitrary algebraic full-domain dual cannot bypass the canonical-closure question.
It does not claim that any of the three conditions always follows from ACSY24.
The supplied normalized full-domain map and the canonical operator have been identified on A only.
No equality of their values on all M Omega, or Hilbert-space closability of the supplied map, is inferred from that agreement: A is not in general operator-norm dense in M.
In the converse direction, bare normal full-domain duals now supply the unique starred derivations, and the remaining ACSY24 obligation is exactly their actual L2 vacuum-adjoint estimate.


### Actual vacuum under the additional single-vector adjoint condition

Use the Hilbert-space inner product linear in its second argument for this calculation.
Part A gives delta_i and E_i(a Omega)=(id tensor tau)delta_i(a) on A.
If eta_i=D_i Omega and Omega is in Dom D_i*, then for a in A,
\[
 \langle\Omega\otimes\Omega,\delta_i(a)\rangle
 =\langle\Omega,E_i(a\Omega)\rangle
 =-\langle D_i^*\Omega,a\Omega\rangle
     +\tau(a\eta_i)
 =\langle-D_i^*\Omega+\eta_i^*,a\Omega\rangle .
\]
Traciality extends to the bounded-L2 product, so tau(a eta_i)=tau(eta_i a).
The displayed representing vector belongs to H.
Since A Omega is dense, this is exactly membership of Omega tensor Omega in Dom delta_i*, with the claimed value.
No step applies a Hilbert closed-graph theorem to the supplied full-domain map.

## Source relationship and limits

[C_F0069 Part A](Yin_C_F0069_v1.md#statement) supplies automatic M-to-H boundedness.
The normal bounded-map Fuglede implication is the accepted specialization of [CS77 Proposition 1](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/EF9F6641DD6268FD9AA68964E85E56FE/S001708950000327Xa.pdf/commutators-and-normal-operators.pdf), checked in [CS77-U001](../audits/literature/CS77/Yin_U001_v1.md#cs77-u001).
The proof uses standard spectral calculus, Hilbert-Schmidt tensor identification, continuous cutoffs at null boundaries and finite unitary averaging.

[C_F0037](Yin_C_F0037_v1.md) is the earlier closable dense-left-module result and proof provenance.
Its spectral-projection/weak-continuity passage is replaced here by the fixed-vector limits (S5)--(S6); the finite-average and kernel estimates are retained without a continuity premise on E.
[C_F0025 Section 3](Yin_C_F0025_v1.md#yin_c_f0025) supplies the already checked phase-uniqueness mechanism, reproduced at its exact hypotheses above.
[C_F0027](Yin_C_F0027_v1.md) is the existing graph-restoration mechanism; Part B states the local application fully.
These are explicit prior interfaces and proof provenance, not claims that the present bare-domain statement was already asserted there.

[ACSY24 Theorem 3.4](../literature/pdf/ACSY24.pdf) supplies closability of the specified canonical core in Part B; its precise domain and adjoint formula are checked in [ACSY24-U001](../audits/literature/ACSY24/Yin_U001_v1.md#acsy24-u001).
Neither that construction nor the maximal-Delta implication from full-domain duals by itself gives the full-domain equivalence.
Theorem 3.4 constructs a core operator from a derivation and vacuum; [C_F0024 Section 3](Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors) concludes maximal Delta from an already full-domain dual.
Proposition 3.5 is the source's maximal-Delta assertion.

The two general questions remain distinct: ACSY24 alone is not shown to imply any of the three equivalent conditions in B, and a bare normal full-domain dual alone is not shown to satisfy the additional actual vacuum condition in C.
Part A resolves the starred-derivation existence part of the latter question.
This record makes no novelty or priority claim.

## Assessment history

### Decision cutoff-draft

| Field | Value |
| --- | --- |
| date | 2026-10-16 |
| status | open |
| reason | Retain the approved cutoff alternative and unchanged tuple, canonical-domain and vacuum arguments before their scoped self-review; v1 retains its reviewed support. |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Unchanged Parts A-C. |
| argument | [Argument](#argument) | Revised S1-S10 and retained S11-S19 and vacuum calculation. |
| dependency | [Automatic norm continuity](Yin_C_F0069_v1.md#statement) | Part A: boundedness of bare full-domain normal duals and diffuse coordinate laws. |
| dependency | [CS77-U001](../audits/literature/CS77/Yin_U001_v1.md#cs77-u001) | Bounded-map Fuglede implication on B(M,H). |
| dependency | [ACSY24-U001](../audits/literature/ACSY24/Yin_U001_v1.md#acsy24-u001) | Part B: actual canonical-core closability under the vacuum premise. |

### Decision cutoff-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-16T04:59 |
| status | proved |
| reason | The authoring agent checked the null-boundary cutoff proof, finite averaging, kernel limit and assembly with the unchanged Parts A-C; the original independent review remains attached only to v1. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Unchanged Parts A-C with all domain and actual vacuum qualifications. |
| argument | [Argument](#argument) | Revised S1-S10, including arbitrary scalar c for diffuse x, and retained S11-S19 and vacuum calculation. |
| dependency | [Automatic norm continuity](Yin_C_F0069_v1.md#statement) | Part A: boundedness of bare full-domain normal duals and diffuse coordinate laws. |
| dependency | [CS77-U001](../audits/literature/CS77/Yin_U001_v1.md#cs77-u001) | Bounded-map Fuglede implication on B(M,H). |
| dependency | [ACSY24-U001](../audits/literature/ACSY24/Yin_U001_v1.md#acsy24-u001) | Part B: actual canonical-core closability under the vacuum premise. |
| review | [Cutoff and assembly self-review](../audits/reviews/Yin_R_F0052_v1.md#conclusion) | Complete v2 statement and argument, with actual self-review relationship and exact bindings. |


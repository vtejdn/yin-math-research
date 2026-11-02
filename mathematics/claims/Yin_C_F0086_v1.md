---
author: Yin
---

# Automatic adjoint modules on dense domains for mixed line/circle normal coordinates

## Current assessment
[Selected decision](#decision-isolated-current-review-20261022)

## Local Adjoint Domains for Selfadjoint and Unitary Coordinates

<a id="statement"></a>

Date: 2026-09-11.
Human author: Yin.
Proof development: another AI agent.
Goal: [Yin_T_F0002](../tasks/Yin_T_F0002_v1.md); route: [Yin_S_F0012](../strategies/Yin_S_F0012.md).

Root requested the mixed selfadjoint/unitary extension of [Yin_C_F0085](Yin_C_F0085_v1.md#yin_c_f0085), with explicit recovery of the original domain after restriction.
The complete Yin_C_F0085 artifact is unchanged.

<a id="yin_c_f0086"></a>
## Yin_C_F0086: Automatic Adjoint Modules for Mixed Coordinates on Dense Left Domains

Mathematical assessment at authorship: proof draft.
Review assessment at authorship: self-reviewed; independent review pending.
Current candidate: [yin_c_f0086-p1](#yin_c_f0086-p1).
The [selected assessment](#current-assessment) records the mathematical and review assessments.

Let \((\mathcal M,\tau)\) be finite tracial with faithful normal probability trace.
Put \(H=L^2(\mathcal M,\tau)\), \(\Omega=1\), \(P=P_\Omega\), and use an inner product linear in its second variable.
Let \(X_1,\ldots,X_d\) generate \(\mathcal M\).
Designate each coordinate as selfadjoint or as unitary, requiring the designated property, with arbitrary mixtures.
Let \(E\subseteq H\) be a dense complex-linear left \(\mathcal M\)-module, and let closable maps \(D_{i,0}:E\to H\), with domain exactly \(E\), satisfy
\[
[D_{i,0},X_j]q=\delta_{ij}Pq\qquad(q\in E).
\tag{51.1}
\]

Then every adjoint domain \(\operatorname{Dom}D_{i,0}^*\) contains a dense complex-linear left \(\mathcal M\)-module \(V_i\).
Thus all conclusions of [Yin_C_F0029-P2](Yin_C_F0029_v1.md#yin_c_f0029-p2) hold for the **original** restrictions \(D_{i,0}:E\to H\), without a separate adjoint-module hypothesis.

More explicitly, there is a common dense left module \(F\subseteq E\), invariant under right multiplication by every unitary coordinate and its inverse, such that \(F\) is a graph core for every \(D_{i,0}\).
Write \(D_i'=D_{i,0}|_F\) and \(\rho(a)v=va\).
On \(F\), define
\[
Q_i=
\begin{cases}
D_i',&X_i\text{ designated selfadjoint},\\
-\rho(X_i)D_i'\rho(X_i),&X_i\text{ chosen as a unitary coordinate}.
\end{cases}
\tag{51.2}
\]
When a coordinate satisfies both descriptions, fix either available designation; the proof works with the chosen one.
There is \(\xi_i\in L^0(\mathcal M)\), not necessarily selfadjoint or globally L1, such that
\[
V_i=\{p\in F\cap\mathcal M:p\xi_i^*\in H\}
\tag{51.3}
\]
is a simultaneous graph core for the pair \((D_i',Q_i)\) and
\[
D_{i,0}^*p=p\xi_i^*-Q_ip\qquad(p\in V_i).
\tag{51.4}
\]

In particular, for any \(u=s^{-1}a=bt^{-1}\in L^0(\mathcal M)\), where \(s,a,b,t\in\mathcal M\) and \(s,t\) are regular,
\[
u\in\operatorname{Div}_{L^0(\mathcal M)}\mathbb C\langle X\rangle
\quad\Longleftrightarrow\quad
\operatorname{rank}(sD_{i,0}b-aD_{i,0}t)|_E<\infty
\quad\text{for every }i.
\tag{51.5}
\]
The full bounded-element, numerical-rank-independence and maximal-Delta conclusions are those of Yin_C_F0029.
No right invariance, inclusion of the vacuum, or boundedness on the whole original domain \(E\) is assumed.
Haar unitaries are included when the stated duals exist; this result does not construct such duals or assume a Haar distribution for arbitrary unitary coordinates.

The adjoint-module and rationality conclusions also hold for coordinatewise affine images \(X_i=\alpha_i1+\beta_iY_i\), where \(\beta_i\ne0\) and each \(Y_i\) is selfadjoint or unitary, thereby covering normal coordinates on affine real lines or circles.
Indeed, the closable operators \(\widetilde D_{i,0}=\beta_iD_{i,0}\) satisfy \([\widetilde D_{i,0},Y_j]=(\beta_i/\beta_j)\delta_{ij}P=\delta_{ij}P\), and their adjoint domains agree with those of \(D_{i,0}\).
Finally \(\mathbb C\langle X\rangle=\mathbb C\langle Y\rangle\), and each cleared defect is multiplied by the nonzero scalar \(\beta_i\), so the base result gives the stated conclusions with their original domains and ranks.

### Reuse and Dependency Boundaries

The local search checked Yin_C_F0032's projection windows, Yin_C_F0039's unitary correction, and Yin_C_F0085's orbit, corner and graph arguments.
The subsequent external search for countable intersections of tracially dense domains and balanced adjoint forms did not locate a verified theorem with the exact needed conclusion.
The countable-intersection and restriction arguments below are therefore supplied directly from Yin_C_F0032, using summable projection deficits; no general topological assertion about arbitrary dense linear subspaces is imported.

The direct accepted inputs are [Yin_C_F0032-P1](Yin_C_F0032_v1.md#yin_c_f0032-p1), the [AP18 L1 predual interface](../audits/literature/AP18/Yin_U003.md#l1-predual-interface), the [FK86 affiliated measure topology](../audits/literature/FK86/Yin_U001.md#measure-topology-interface), and the final Yin_C_F0029 criterion.
The Hilbert closed-graph and orbit mechanism is the part of [Yin_C_F0085-P1](Yin_C_F0085_v1.md#yin_c_f0085-p1) that uses only a closable map on a dense left module; its selfadjoint theorem is not applied to a normal tuple outside its hypotheses.
The non-Hermitian corner adaptation is written out below.
The unitary formula in Yin_C_F0039 is rechecked on the new domain, rather than assuming its all-bounded-vector hypothesis.

<a id="yin_c_f0086-p1"></a>
## Proof yin_c_f0086-p1

**1. A common right-invariant module.**
A countable intersection of dense left \(\mathcal M\)-modules is again dense.
Indeed, let \(E_n\) be these modules.
For any \(\varepsilon>0\), Yin_C_F0032 supplies projections \(f_n\in E_n\) with \(\tau(1-f_n)<\varepsilon2^{-n}\).
Their meet \(f=\bigwedge_n f_n\) satisfies \(f=ff_n\in E_n\) for every \(n\), and
\[
\tau(1-f)\le\sum_n\tau(1-f_n)<\varepsilon.
\]
Taking \(\varepsilon\downarrow0\) gives projections in the intersection tending to one in \(L^2\).
Their left spans prove density.

Let \(\mathcal W\) be the countable subgroup of unitaries consisting of words in the unitary coordinates and their inverses, including the identity.
For \(w\in\mathcal W\), the subspace
\[
E_w=\{v\in H:vw\in E\}=Ew^*
\]
is a dense left module, because right multiplication by a unitary is a Hilbert-space unitary commuting with the left action.
Set
\[
F=\bigcap_{w\in\mathcal W}E_w.
\tag{51.6}
\]
The preceding argument makes \(F\) dense; the identity word gives \(F\subseteq E\).
For \(v\in F\), \(u,w\in\mathcal W\), one has \((vu)w=v(uw)\in E\), so \(F\) is invariant under right multiplication by every word and its inverse.

**2. Restriction preserves the original closures.**
More generally, if \(F\subseteq E\) are dense left modules and \(D:E\to H\) is closable, then \(D|_F\) has the same closure as \(D\).
For each \(v\in E\), the Yin_C_F0085 orbit argument gives
\[
\|D(av)\|_2\le c_v\|a\|,
\qquad
D(a_\alpha v)\rightharpoonup D(av)
\tag{51.7}
\]
whenever \(a_\alpha\to a\) strongly with uniformly bounded operator norms.

First, for \(q\in E\), left spectral cutoffs of \(|q^*|\) produce bounded vectors in \(E\) tending to \(q\) in \(H\), with their \(D\)-images tending weakly to \(Dq\).
Closed linear subspaces of \(H\oplus H\) are weakly closed, so \(E\cap\mathcal M\) is a graph core for \(D\).

For a fixed \(q\in E\cap\mathcal M\), apply Yin_C_F0032 to the **smaller module \(F\)** with the single bounded target \(q\).
It gives projections \(e_n,p_n\), with \(e_n\in F\), \(p_n\to1\) strongly, and
\[
p_nq\in\mathcal M e_n\subseteq F.
\]
These vectors converge to \(q\) in \(H\), while \(D(p_nq)\rightharpoonup Dq\) by (51.7).
The same weak-closed-subspace argument puts \((q,Dq)\) in the norm closure of the graph of \(D|_F\).
Combining the two steps proves
\[
\overline{D|_F}=\overline D,\qquad (D|_F)^*=D^*.
\tag{51.8}
\]
This holds for every \(D_{i,0}\).
The argument does not mistake right cutoffs \(qe_n\) for graph approximations.

**3. The paired derivative and its commutators.**
Fix \(i\), write \(D=D_i'\), and define \(Q=Q_i\) by (51.2).
Both are closable on \(F\).
This is clear for \(Q=D\); for a unitary coordinate \(U=X_i\), both right multipliers in \(-\rho(U)D\rho(U)\) are Hilbert-space unitaries and \(F\) is invariant under them and their inverses.
Thus
\[
\overline Q=-\rho(U)\overline D\,\rho(U)
\]
on the transported domain.
This identity is unitary transport on the input and output, not a similarity assertion using an inverse in one of the two positions.
In particular the orbit estimates and weak continuity (51.7) hold for both \(D\) and \(Q\) on \(F\).

Left invariance of \(F\) and \(UU^*=1\) give
\[
[D_{i,0},X_j^*]|_F=
\begin{cases}
\delta_{ij}P,&X_j\text{ designated selfadjoint},\\
-\delta_{ij}X_j^*PX_j^*,&X_j\text{ designated unitary}.
\end{cases}
\tag{51.9}
\]
All these are bounded operators restricted to \(F\).
If \(X_i\) is designated selfadjoint and \(Q=D\), the required relation
\[
[Q,X_j]=[D,X_j^*]^*,\qquad
[Q,X_j^*]=[D,X_j]^*
\tag{51.10}
\]
follows immediately.
In the unitary case \(U=X_i\), right and left multipliers commute, while
\[
\rho(U)P\rho(U)=UPU.
\]
Indeed, both sides send \(v\) to \(\tau(Uv)U\).
Consequently
\[
[Q,U]=-\rho(U)P\rho(U)=-UPU=[D,U^*]^*,
\qquad
[Q,U^*]=U^*\rho(U)P\rho(U)U^*=P.
\]
The other coordinate commutators vanish.
This proves (51.10) in every case.
The derivation product rule propagates it to
\[
[Q,a]=[D,a^*]^*
\tag{51.11}
\]
for every star-polynomial \(a\), with bounded commutator representatives.

**4. A balanced cross form and local densities.**
On \(F\times F\) define
\[
b(p,q)=\langle p,Dq\rangle+\langle Qp,q\rangle.
\tag{51.12}
\]
This form need not be Hermitian.
Equation (51.11) gives
\[
b(ap,q)-b(p,a^*q)
=-\langle p,[D,a^*]q\rangle+\langle[Q,a]p,q\rangle=0.
\]
Orbit norm estimates extend the identity to \(C^*(X)\); bounded strong-star Kaplansky approximation and (51.7) extend it to all \(a\in\mathcal M\):
\[
b(ap,q)=b(p,a^*q).
\tag{51.13}
\]

For a projection \(e\in F\), the functional \(\phi_e(a)=b(e,ae)\) is normal.
To see the only nontrivial term, approximate \(e\) in \(H\) by \(v_n\in\operatorname{Dom}D^*\).
The normal functionals \(\langle D^*v_n,ae\rangle\) are Cauchy in functional norm by the orbit estimate for \(D(ae)\).
The AP18 L1 norm identity and completeness give the limiting normal functional \(\langle e,D(ae)\rangle\).
The other term \(\langle Qe,ae\rangle\) is already normal.

Balance gives \(\phi_e(a)=\phi_e(eae)\), so it has a unique density \(\xi_e\in eL^1(\mathcal M)e\), now without a selfadjointness assertion.
As in the direct corner calculation of Yin_C_F0085,
\[
b(xe,ye)=\tau(\xi_e x^*y),\qquad
\xi_f=f\xi_e f\quad(f\le e,\ f\in F).
\tag{51.14}
\]

**5. Gluing the complex densities.**
Choose increasing \(e_n\in F\) with \(e_n\uparrow1\), by taking tail meets of Yin_C_F0032 projections with summable trace deficits.
Put \(\xi_n=\xi_{e_n}\).
Compatibility gives \(e_n(\xi_m-\xi_n)e_n=0\) for \(m\ge n\).
The same two-tail decomposition as in Yin_C_F0085 yields
\[
\operatorname{rank}_\tau(\xi_m-\xi_n)\le2\tau(1-e_n).
\tag{51.15}
\]
Here rank denotes the common trace of the left and right supports.
The decomposition and support estimate do not require selfadjointness.
They give a Cauchy sequence in measure, so the FK86 interface supplies a unique \(\xi\in L^0(\mathcal M)\).
Multiplication continuity gives \(e_n\xi e_n=\xi_n\).
For any projection \(e\in F\), intersect it with \(e_n\); compatibility in the common subcorner and \(\tau(e-e\wedge e_n)\to0\) give
\[
e\xi e=\xi_e.
\tag{51.16}
\]
Adjoint continuity permits the corresponding identity with \(\xi^*\).
No global L1 bound or global functional \(\tau(\xi a)\) is inferred.

**6. A simultaneous graph core and the full pairing.**
Set
\[
V=\{p\in F\cap\mathcal M:p\xi^*\in H\}.
\]
This is a complex-linear left module.
It is a simultaneous graph core for \(D,Q\): for \(q\in F\), left spectral cutoffs of \(|q^*|\) produce bounded vectors \(q_n\in F\) with
\[
(q_n,Dq_n,Qq_n)\rightharpoonup(q,Dq,Qq)
\quad\text{in }H\oplus H\oplus H.
\]
For bounded \(q\in F\), left spectral cutoffs of \(|(q\xi^*)^*|\) produce vectors in \(V\) with the same weak graph convergence.
The norm closure of each linear graph is weakly closed, so the two approximations prove the assertion.
In particular \(V\) is dense in \(H\).

For \(p,q\in V\), take the column polar decomposition
\[
h=(p^*p+q^*q)^{1/2},\qquad p=ah,\quad q=ch,\quad h=a^*p+c^*q.
\]
It gives \(h\in F\) and \(h\xi^*=a^*p\xi^*+c^*q\xi^*\in H\).
Write \(s=\operatorname{supp}h\), \(g_k=1_{[1/k,\infty)}(h)\in F\).
The corner formula, now with the correct adjoint on its density, is
\[
b(pg_k,qg_k)
=\langle pg_k\xi^*g_k,qg_k\rangle.
\tag{51.17}
\]
All pairings are defined: \(pg_k\xi^*=a g_k(h\xi^*)\in H\).

The fixed orbit at \(h\) shows \(Q(pg_k)\rightharpoonup Qp\) and \(D(qg_k)\rightharpoonup Dq\); the other vectors converge strongly.
Thus the left side tends to \(b(p,q)\).
On the right, \(pg_k\xi^*\to p\xi^*\) in \(H\), and after the additional right cutoff the limit is \((p\xi^*)s\).
Since \(q=qs\), the pairing tends to \(\langle p\xi^*,q\rangle\).
We obtain
\[
\langle p,Dq\rangle+\langle Qp,q\rangle
=\langle p\xi^*,q\rangle\qquad(p,q\in V).
\tag{51.18}
\]

For fixed \(p\in V\), use the simultaneous graph core to approximate any \(q\in F\) by vectors in \(V\), and pass to the limit.
This proves \(p\in\operatorname{Dom}(D_i')^*\) and \((D_i')^*p=p\xi^*-Qp\).
Finally, (51.8) gives \((D_i')^*=D_{i,0}^*\), or equivalently permits one more \(D_{i,0}\)-graph approximation from \(F\) to every \(q\in E\).
Hence the formula tests against the **whole original domain \(E\)** and proves (51.4).

Repeat for all \(i\).
The dense left modules \(V_i\) now meet exactly Yin_C_F0029's hypotheses for the original duals on \(E\); its reviewed proof gives (51.5) and the other conclusions.
QED.

## Checks and Scope

The author's checks cover the order \(E_w=Ew^*\), invariance by right word multiplication, countable rather than only finite intersections, graph-core recovery of the original restriction, both generator/starred-generator commutators, the cross-form density adjoint, and the right-cutoff pairing.
The proof never assumes the original domain is invariant under right multiplication.

For an entirely selfadjoint tuple, the right-word group is trivial and \(F=E\); the construction recovers Yin_C_F0085.
For a Haar tuple it uses only the unitary identity and the hypothesized closable dual relations.
Finite-spectrum or overlapping coordinate descriptions do not create a new exception: the stated dual identities themselves retain all their algebraic restrictions.

This extension covers the mixed selfadjoint/unitary class and its stated nondegenerate coordinatewise affine images.
It does not pass to an arbitrary infinite projective expansion of a spectral phase on a small domain, where convergence of the corrected dual would require additional control.
No claim about arbitrary analytic arcs or all normal tuples is made here.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:05 |
| status | proved |
| reason | Adopt the exact actual original finding and disclosed unknown initial-context relationship, preserving the mathematical assessment, fixed statement and argument, dependencies and historical decisions. No new review or mathematical proof version is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0086-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0086_v1.md#the-new-domain-arguments) | Complete C_F0086 mixed selfadjoint/unitary theorem, countable right-word graph core, actual original adjoint recovery and final affine consequence. Actual original finding with unknown initial-context arrangement; historical date and accepted-input depth unchanged. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the separate isolated current finding on the unchanged fixed statement and proof, with exact conditions and scope. Preserve historical findings, relationships, source depths and dates; no new mathematical proof version is introduced. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0086-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0086_v1.md#current-isolated-finding) | Complete C_F0086 mixed selfadjoint/unitary theorem, countable right-word graph core, actual original adjoint recovery and final affine consequence. |

## Historical assessments


These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0086-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0086_v1.md#the-new-domain-arguments) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0086_v1.md#the-new-domain-arguments).

Material covered by that review: [Exact material](Yin_C_F0086_v1.md).

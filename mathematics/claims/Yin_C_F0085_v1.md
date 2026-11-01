---
author: Yin
---

# Arbitrary dense selfadjoint dual domains yield automatic adjoint modules

## Current assessment
[Selected decision](#decision-isolated-current-review-20261022)

## Local Balanced Forms on Dense Left Modules

<a id="statement"></a>

Date: 2026-09-11.
Human author: Yin.
Proof development: another AI agent.
Goal: [Yin_T_F0002](../tasks/Yin_T_F0002_v1.md).
Route: [Yin_S_F0012](../strategies/Yin_S_F0012.md).
This is a continuation of [Yin_C_F0038](Yin_C_F0038_v1.md#yin_c_f0038) and [Yin_C_F0039](Yin_C_F0039_v1.md#yin_c_f0039), not a modification of their reviewed proof artifacts.
The discussion below records a substantive attempted extension; it does not by itself assign a Claim or a proved assessment.

## Initial Local Attempt and Its Missing Bridge

For selfadjoint generators and a closable dual operator \(D:E\to L^2(\mathcal M)\) on an arbitrary dense left \(\mathcal M\)-module, consider

\[
b(p,q)=\langle p,Dq\rangle+\langle Dp,q\rangle.
\]

The rank-one dual identities give \(b(X_jp,q)=b(p,X_jq)\).
Bounded orbit maps \(a\mapsto D(av)\) and Kaplansky approximation appear to extend this balance to all \(a\in\mathcal M\).
For each projection \(e\in E\), the balanced form on \(\mathcal M e\) then has a selfadjoint density \(\xi_e\in eL^1(\mathcal M)e\).
A local density alone does **not** certify that any proposed vector lies in \(\operatorname{Dom}D^*\): the adjoint estimate must test against every vector in \(E\), not just \(\mathcal M e\).

The initial unresolved bridge was therefore to glue the corner densities and control the full test domain.
The following proposed repair is retained for review.
Choose increasing \(e_n\in E\) tending to one, so compatibility gives \(e_n\xi_m e_n=\xi_n\) for \(n\le m\).
The difference \(\alpha=\xi_m-\xi_n\) has

\[
\alpha=(1-e_n)\alpha+e_n\alpha(1-e_n),\qquad
\operatorname{rank}_\tau(\alpha)\le2\tau(1-e_n).
\]

Thus it should be Cauchy in measure even though no uniform operator or L1 norm bound is available.
Completeness and continuity of multiplication in the affiliated measure topology would give a selfadjoint \(\xi\in L^0(\mathcal M)\) with all the prescribed corner compressions.
These measure-topology interfaces still require a checked external source at this checkpoint.

The candidate global test module is \(V=\{p\in E\cap\mathcal M:p\xi\in L^2(\mathcal M)\}\).
Successive left spectral cutoffs, weak orbit continuity and convex graph approximation should make \(V\) a graph core for \(D\).
For \(p,q\in V\), the common positive factor \(h=(p^*p+q^*q)^{1/2}\in E\) permits simultaneous reduction to \(\mathcal M e_k\), where \(e_k=1_{[1/k,\infty)}(h)\).
Column polar decomposition gives \(h\xi\in L^2\) directly from \(p\xi,q\xi\in L^2\).
Passing through these common corners would prove \(b(p,q)=\langle p\xi,q\rangle\), and the graph-core property would extend this to all second arguments in \(E\).
Only after these steps are fully checked may one conclude \(V\subseteq\operatorname{Dom}D^*\).

At this checkpoint the complete proof and independent review remain outstanding.
In particular neither compatible corner densities alone nor density of \(\operatorname{Dom}D^*\) is being used as a substitute for an explicit dense left module contained in that domain.
No analogous arbitrary-normal statement follows merely by inserting the Hilbert-Schmidt phase from Yin_C_F0037.

<a id="yin_c_f0085"></a>
## Yin_C_F0085: Automatic Adjoint Modules on Arbitrary Dense Left Domains

The preceding checkpoint is retained as the record of the initial missing bridge.
The following complete candidate supplies the bridge and its source interface.
Mathematical assessment at authorship: proof draft.
Review assessment at authorship: self-reviewed; independent review pending.
The [selected assessment](#decision-candidate-0002) records the mathematical and review assessments.

Let \((\mathcal M,\tau)\) be a finite von Neumann algebra with faithful normal probability trace, \(H=L^2(\mathcal M,\tau)\), \(\Omega=1\), and \(P=P_\Omega\).
The inner product is linear in its second variable.
Let \(X_1,\ldots,X_d\) be bounded selfadjoint generators of \(\mathcal M\), and let \(E\subseteq H\) be an arbitrary dense complex-linear left \(\mathcal M\)-module.
Suppose the maps \(D_{i,0}:E\to H\), with domain exactly \(E\), are closable and satisfy
\[
[D_{i,0},X_j]q=\delta_{ij}Pq\qquad(q\in E).
\tag{50.1}
\]

For every \(i\) there is a selfadjoint \(\xi_i\in L^0(\mathcal M)\) such that
\[
V_i=\{p\in E\cap\mathcal M:p\xi_i\in H\}
\tag{50.2}
\]
is a dense complex-linear left \(\mathcal M\)-module, is a graph core for \(\overline{D_{i,0}}\), and satisfies
\[
V_i\subseteq\operatorname{Dom}D_{i,0}^*,
\qquad
D_{i,0}^*p=p\xi_i-D_{i,0}p\quad(p\in V_i).
\tag{50.3}
\]

Consequently all conclusions of [Yin_C_F0029-P2](Yin_C_F0029_v1.md#yin_c_f0029-p2) hold without a separate adjoint-module premise.
In particular, for any \(u=s^{-1}a=bt^{-1}\in L^0(\mathcal M)\), with \(s,a,b,t\in\mathcal M\) and regular \(s,t\),
\[
u\in\operatorname{Div}_{L^0(\mathcal M)}\mathbb C\langle X\rangle
\quad\Longleftrightarrow\quad
\operatorname{rank}\bigl(sD_{i,0}b-aD_{i,0}t\bigr)|_E<\infty
\quad\text{for every }i.
\tag{50.4}
\]
The numerical rank is independent of the fraction pair.
For bounded \(f\), this is the finite-rank commutator criterion on \(E\) and, equivalently, on the full closed dual domains as in Yin_C_F0029.

The hypotheses do not require \(E\subseteq\mathcal M\), \(1\in E\), right invariance of \(E\), a bounded reference dual, or an L2 conjugate variable.
The multiplier \(\xi_i\) need not lie in L1 globally.
Closability alone gives density of the adjoint domain; (50.2)–(50.3) give the additional left-module structure, which is the substantive conclusion.
Selfadjointness of the generators and of their commutator defects makes the Hermitian form below balanced for the full generating star-algebra.

### Dependencies and Reuse

[Yin_C_F0032-P1](Yin_C_F0032_v1.md#yin_c_f0032-p1) supplies large projections in \(E\).
Its closed-graph and weak-continuity argument is applied below to arbitrary orbits \(a\mapsto D_{i,0}(av)\); the details are included to cover possibly unbounded \(v\in E\).
The [AP18 L1 interface](../audits/literature/AP18/Yin_U003.md#l1-predual-interface) gives the normal-functional norm identity, completeness and density representation.
The new [FK86 measure-topology interface](../audits/literature/FK86/Yin_U001.md#measure-topology-interface) supplies the affiliated topological algebra used in the gluing step.

The reuse search checked the local Yin_C_F0032, Yin_C_F0038 and Yin_C_F0039 arguments, existing affiliated-operator source units, and the measure-topology use in Yin_C_F0014.
It then searched primary external sources for the missing completeness interface, locating FK86 §§1.2, 1.4–1.5; Hiai's *Concise lectures on selected topics of von Neumann algebras*, arXiv:2004.02383, was also consulted as corroboration but is not an additional proof dependency.
No existing registered result supplied the local-to-global adjoint argument below.
Kaplansky density and polar decomposition are the accepted standard inputs already used in Yin_C_F0032/Yin_C_F0033.
The weak-to-norm graph-closure passage uses only the double-orthogonal-complement description of a closed Hilbert subspace.

<a id="yin_c_f0085-p1"></a>
### Proof yin_c_f0085-p1

Fix \(i\) and abbreviate \(D=D_{i,0}\).
Every product of affiliated operators below means its closed product.
A graph core for \(D\) means a subspace whose graph has the same norm closure as the graph of \(D\).

**1. Orbit estimates and balance.**
For each \(v\in E\), the map
\[
T_v:(\mathcal M,\|\cdot\|)\longrightarrow H,\qquad T_v(a)=D(av)
\]
has closed graph.
Indeed, \(a_n\to a\) in operator norm and \(D(a_nv)\to w\) imply \((a_n-a)v\to0\) and \(D((a_n-a)v)\to w-D(av)\); closability forces \(w=D(av)\).
Thus
\[
\|D(av)\|_2\le c_v\|a\|.
\tag{50.5}
\]
If \(a_\alpha\to a\) strongly with uniformly bounded norms, then \(a_\alpha v\to av\) in \(H\).
Pairing with the dense domain of \(D^*\), followed by (50.5), shows
\[
D(a_\alpha v)\rightharpoonup D(av).
\tag{50.6}
\]
Only density of \(\operatorname{Dom}D^*\) is used here.

Define the Hermitian sesquilinear form
\[
b(p,q)=\langle p,Dq\rangle+\langle Dp,q\rangle,\qquad p,q\in E.
\]
For every \(j\), (50.1), selfadjointness of \(X_j\), and \(P=P^*\) give
\[
b(X_jp,q)-b(p,X_jq)
=\delta_{ij}\bigl(\langle Pp,q\rangle-\langle p,Pq\rangle\bigr)=0.
\]
Iteration and complex linearity therefore give \(b(ap,q)=b(p,a^*q)\) for the generated star-polynomial algebra, then for its norm closure by (50.5).
For arbitrary \(a\in\mathcal M\), Kaplansky density gives a uniformly bounded net in that C*-algebra converging strongly with its adjoints to \(a\).
Apply (50.6) to the fixed vectors \(p,q\), and strong convergence to the other factors, to obtain
\[
b(ap,q)=b(p,a^*q)\qquad(a\in\mathcal M,\ p,q\in E).
\tag{50.7}
\]

**2. Normal corner densities.**
Let \(e\in E\cap\mathcal M\) be a projection.
The functional \(\phi_e(a)=b(e,ae)\) is bounded on \(\mathcal M\).
It is normal: choose \(v_n\in\operatorname{Dom}D^*\) tending to \(e\) in \(H\).
The normal functionals
\[
a\longmapsto\langle v_n,D(ae)\rangle
=\langle D^*v_n,ae\rangle
\]
are Cauchy in functional norm, since their difference has norm at most \(c_e\|v_n-v_m\|_2\).
Their L1 densities therefore converge by the AP18 norm identity and completeness.
The limit is \(a\mapsto\langle e,D(ae)\rangle\); the other term \(\langle De,ae\rangle\) is already normal.
Hence \(\phi_e\) has a unique L1 density.

Balance implies \(\phi_e(a)=\phi_e(eae)\).
Hermitian symmetry and balance give \(\phi_e(a^*)=\overline{\phi_e(a)}\).
Uniqueness of the L1 density therefore supplies a selfadjoint \(\xi_e\in eL^1(\mathcal M)e\) with
\[
b(xe,ye)=b(e,x^*ye)=\tau(\xi_e x^*y)
\qquad(x,y\in\mathcal M).
\tag{50.8}
\]
If \(f\le e\) is another projection in \(E\), evaluating (50.8) on \(\mathcal M f\) gives the compatibility
\[
\xi_f=f\xi_e f.
\tag{50.9}
\]

**3. Gluing in measure.**
By Yin_C_F0032 choose projections \(f_n\in E\) with \(\tau(1-f_n)\le2^{-n}\), and set
\[
e_n=\bigwedge_{k\ge n}f_k.
\]
Then \(e_n=e_nf_n\in E\), \(e_n\uparrow1\), and \(\tau(1-e_n)\le\sum_{k\ge n}2^{-k}\to0\).
Write \(\xi_n=\xi_{e_n}\).
For \(m\ge n\), (50.9) gives \(e_n(\xi_m-\xi_n)e_n=0\).

For an affiliated \(z\), let \(\operatorname{rank}_\tau z\) denote the trace of its right support, equivalently its left support by polar decomposition.
Support joins imply subadditivity of this rank.
Put \(\alpha=\xi_m-\xi_n\).
In the affiliated algebra,
\[
\alpha=(1-e_n)\alpha+e_n\alpha(1-e_n).
\]
The first term has left support at most \(1-e_n\); the second has right support at most \(1-e_n\).
Therefore
\[
\operatorname{rank}_\tau(\xi_m-\xi_n)\le2\tau(1-e_n).
\tag{50.10}
\]
Taking the complement of the right support in the defining measure neighborhood shows that \((\xi_n)\) is Cauchy in measure, independently of the sizes of its nonzero values.
Completeness gives \(\xi\in L^0(\mathcal M)\).
Adjoint continuity gives \(\xi=\xi^*\), and multiplication continuity gives \(e_n\xi e_n=\xi_n\).

This also recovers **every** original corner.
If \(e\in E\) is any projection, set \(q_n=e\wedge e_n\).
Then \(q_n\in E\), \(\tau(e-q_n)\le\tau(1-e_n)\), and
\[
q_n\xi q_n=q_n\xi_nq_n=\xi_{q_n}=q_n\xi_e q_n.
\]
Since \(q_n\to e\) in measure, continuity and uniqueness of limits give
\[
e\xi e=\xi_e.
\tag{50.11}
\]
This step uses compressions and the two-tail estimate, not an unsupported assertion that compatible compressions are operator restrictions.

**4. A common dense graph core.**
Define \(V=\{p\in E\cap\mathcal M:p\xi\in H\}\).
Closed-product associativity shows that \(V\) is a complex-linear left \(\mathcal M\)-module.

First let \(q\in E\).
The left spectral cutoffs
\[
a_n=1_{[0,n]}(|q^*|)
\]
increase strongly to one and make \(a_nq\) bounded.
Thus \(a_nq\in E\cap\mathcal M\), \(a_nq\to q\) in \(H\), and \(D(a_nq)\rightharpoonup Dq\) by (50.6).
The norm closure of the graph of \(E\cap\mathcal M\) is a closed linear subspace of \(H\oplus H\), hence the intersection of the kernels of pairings with its orthogonal complement.
It is therefore weakly closed, so \((q,Dq)\) lies in that norm closure.

Now let \(q\in E\cap\mathcal M\).
Set \(z=q\xi\in L^0(\mathcal M)\) and use \(a_n=1_{[0,n]}(|z^*|)\).
Again \(a_n\uparrow1\), and \(a_nz\) is bounded.
Hence \(a_nq\in V\), \(a_nq\to q\) in \(H\), and \(D(a_nq)\rightharpoonup Dq\).
The same closed-subspace argument places \((q,Dq)\) in the norm closure of the graph of \(V\).
Combining the two approximations shows that \(V\) is a graph core for \(D\), and in particular is dense in \(H\).

**5. The global pairing from common corners.**
Let \(p,q\in V\).
Put \(h=(p^*p+q^*q)^{1/2}\).
Polar decomposition of the bounded column with entries \(p,q\) gives contractions \(a,b\in\mathcal M\) with
\[
p=ah,\qquad q=bh,\qquad h=a^*p+b^*q.
\]
Consequently \(h\in E\), and
\[
h\xi=a^*(p\xi)+b^*(q\xi)\in H.
\tag{50.12}
\]
Let \(s=\operatorname{supp}h\) and \(g_k=1_{[1/k,\infty)}(h)\uparrow s\).
The bounded function \(t\mapsto t^{-1}1_{[1/k,\infty)}(t)\) shows \(g_k\in E\), since it multiplies \(h\) on the left.
Thus \(pg_k,qg_k\in\mathcal M g_k\), and (50.8), (50.11) give
\[
b(pg_k,qg_k)=\langle pg_k\xi g_k,qg_k\rangle.
\tag{50.13}
\]
The right side is a legitimate Hilbert pairing: \(pg_k\xi=a g_k(h\xi)\in H\), by (50.12) and commutation of \(g_k,h\).

For the left side, \(pg_k=a g_kh\), \(qg_k=b g_kh\).
The single orbit \(T_h\) gives \(D(pg_k)\rightharpoonup Dp\) and \(D(qg_k)\rightharpoonup Dq\); \(pg_k\to p\) and \(qg_k\to q\) strongly in \(H\).
Hence the left side tends to \(b(p,q)\).

On the right, \(h\xi\) has left support at most \(s\), so \(pg_k\xi=a g_k(h\xi)\to p\xi\) in \(H\).
Its additional right compression converges to \((p\xi)s\), which need not equal \(p\xi\).
Nevertheless \(q=qs\), and the limiting pairing is \(\langle(p\xi)s,q\rangle=\langle p\xi,q\rangle\).
We conclude
\[
\langle p,Dq\rangle+\langle Dp,q\rangle
=\langle p\xi,q\rangle
\qquad(p,q\in V).
\tag{50.14}
\]

**6. Testing against all of \(E\).**
Fix \(p\in V\).
For any \(q\in E\), the graph-core property gives \(q_n\in V\) with \(q_n\to q\) and \(Dq_n\to Dq\) in \(H\).
Passing to the limit in (50.14) yields
\[
\langle p,Dq\rangle=\langle p\xi-Dp,q\rangle\qquad(q\in E).
\]
This is the actual adjoint-domain criterion, and proves (50.3).
Performing the construction for every \(i\) supplies the dense left modules required by Yin_C_F0029.
Invoking its already reviewed proof gives (50.4) and the other announced consequences.
QED.

### Checks, Scope and Remaining Direction

The author's checks include complex conjugation in the balancing identity, compression support of the normal functionals, tracial rank of both off-diagonal tails, recovery of corners outside the chosen exhaustion, the distinction between weak graph approximation and norm graph closure, and the final right-compression pairing.
No \(\tau(\xi a)\) is used for an arbitrary bounded \(a\) when the glued \(\xi\) need not be L1.

The conclusion removes the **separate** adjoint-domain certificate in the selfadjoint case while retaining closability of the specified restriction and density of \(E\).
Yin_C_F0084 still prevents deleting density indiscriminately.
For general normal coordinates, Yin_C_F0039 proves a different sufficient condition with all bounded vectors in the domain and a projective conjugate phase.
Extending the local balanced-form construction to that paired-operator setting remains open here; this proof does not quietly extend its selfadjoint conclusion to all normal tuples.


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
| argument | [Exact material](#yin_c_f0085-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0085_v1.md#full-proof-checks) | Complete selfadjoint dense-left-domain C_F0085 proof, measure-topology gluing, whole original adjoint tests and exact criterion application; no mixed-normal extension. Actual original finding with unknown initial-context arrangement; historical date and accepted-input depth unchanged. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the separate isolated current finding on the unchanged fixed statement and proof, with exact conditions and scope. Preserve historical findings, relationships, source depths and dates; no new mathematical proof version is introduced. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0085-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0085_v1.md#current-isolated-finding) | Complete selfadjoint dense-left-domain C_F0085 proof, measure-topology gluing, whole original adjoint tests and exact criterion application; no mixed-normal extension. |

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
| argument | [Exact material](#yin_c_f0085-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0085_v1.md#full-proof-checks) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0085_v1.md#full-proof-checks).

Material covered by that review: [Exact material](Yin_C_F0085_v1.md).

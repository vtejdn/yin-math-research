---
author: Yin
---

# Normal starred commutators are automatically Hilbert-Schmidt

## Current assessment
[Selected decision](#decision-isolated-whole-review-2026-10-22)

## Yin_C_F0037: Starred-Generator Commutators Are Automatic on a Dense Left Module

<a id="statement"></a>
<a id="yin_c_f0037"></a>

Provenance: project deduction; root suggested testing the Hilbert-Schmidt normal-commutator mechanism, and the present proof supplies the unbounded domain passage.
Mathematical assessment at authorship: proof draft; complete candidate below.
Review assessment at authorship: self-reviewed; independent review pending.
Current candidate proof: [yin_c_f0037-p1](#yin_c_f0037-p1).

Let \((\mathcal M,\tau)\) be a finite von Neumann algebra with faithful normal probability trace, and put \(H=L^2(\mathcal M,\tau)\), \(\Omega=1\), and \(P=P_\Omega\).
Use the inner product linear in its second variable.
Let \(X=(X_1,\ldots,X_d)\) be a bounded normal tuple in \(\mathcal M\), let \(\mathcal E\subset H\) be a dense left \(\mathcal M\)-module, and suppose closable maps \(D_{i,0}:\mathcal E\to H\) satisfy the dual identities \([D_{i,0},X_j]z=\delta_{ij}Pz\) for every \(z\in\mathcal E\).
A bounded reference dual and any module structure in the adjoint domains are **not** assumed.
Generation of \(\mathcal M\) by the tuple is not needed for this assertion.

Let \(\mu_j\) be the spectral distribution of \(X_j\).
It is nonatomic.
On \(L^2(W^*(X_j))\widehat\otimes L^2(W^*(X_j))\), define the vector
\[
k_j(z,w)=\begin{cases}
\dfrac{\bar z-\bar w}{z-w},&z\ne w,\\
0,&z=w,
\end{cases}
\]
and let \(K_j=\Theta(k_j)\) be its Hilbert-Schmidt representative, with the previously checked convention \(\Theta(g\otimes h)\xi=g\langle Jh,\xi\rangle\).
Then
\[
[D_{i,0},X_j^*]z=\delta_{ij}K_jz\quad(z\in\mathcal E),
\qquad \|K_j\|_{\mathrm{HS}}=1.
\tag{38.1}
\]
Thus all starred-generator commutators have bounded Hilbert-Schmidt extensions.
Both \(\operatorname{Dom}\overline{D_{i,0}}\) and \(\operatorname{Dom}D_{i,0}^*\) are invariant under the starred polynomial algebra, with the adjoint commutators supplied by pairing.
This is weaker than asserting that the adjoint domain contains a dense left \(\mathcal M\)-module.

### Inputs and the New Domain Step

[Yin_C_F0025 Sections 2-3](Yin_C_F0025_v1.md#yin_c_f0025) already construct this exact kernel and its Hilbert-Schmidt operator, using the standard tracial tensor identification and scalar spectral theorem.
They identify an already compact starred commutator with \(K_j\).
The present argument does **not** assume that commutator is bounded or compact: it proves this from dense left-module inputs by local orbit maps and spectral pinching.
The kernel construction is reused, while that missing domain passage is proved below.
No additional source theorem about unbounded double operator integrals is invoked.

<a id="yin_c_f0037-p1"></a>
### Proof yin_c_f0037-p1

Fix \(j\) and put \(N=X_j\).
For a spectral atom \(e=1_{\{\lambda\}}(N)\), left invariance and the \(i=j\) dual relation give
\[
e[D_{j,0},N]ez=0=ePez\qquad(z\in\mathcal E).
\]
Since \(\mathcal E\) is dense, boundedness makes \(ePe=0\) on \(H\).
But \(ePe\) is the positive rank-one operator associated to \(e\Omega\), and \(\|e\Omega\|_2^2=\tau(e)\).
Faithfulness gives \(e=0\).
Hence \(\mu_j\) is nonatomic.

The function \(k=k_j\) has modulus one off the now-null diagonal, so it is a unit vector in the completed Hilbert tensor product.
The known unitary \(\Theta\) gives \(K=K_j\) with Hilbert-Schmidt norm one.
Multiplication of the kernel by \(z-w\) directly verifies
\[
[K,N]=[P,N^*].
\tag{38.2}
\]

Fix \(i\), write \(D_0=D_{i,0}\) and \(\delta=\delta_{ij}\), and define the generally unbounded map on \(\mathcal E\)
\[
A=[D_0,N^*]-\delta K.
\]
All its terms are defined because \(N^*\mathcal E\subseteq\mathcal E\).
Normality, the dual relation, and (38.2) give the algebraic Jacobi identity
\[
[A,N]=[[D_0,N^*],N]-\delta[K,N]
=[[D_0,N],N^*]-\delta[P,N^*]=0
\quad\text{on }\mathcal E.
\tag{38.3}
\]

For every fixed \(v\in\mathcal E\), the orbit map \(T_v(a)=D_0(av)\), \(a\in\mathcal M\), is bounded from operator norm to Hilbert norm by the same closed-graph argument as in [the orbit-map proof](Yin_C_F0036_v1.md#yin_c_f0036-p1).
Write its norm as \(t_v\).
Consequently the orbit map \(a\mapsto A(av)\) is also bounded between those spaces.
Moreover it is weakly continuous on operator-norm-bounded strongly convergent nets: for \(a_\alpha\to a\) strongly with uniformly bounded norms, the inputs \(a_\alpha v\) and \(N^*a_\alpha v\) converge in \(H\).
Testing their images under \(D_0\) against \(\operatorname{Dom}D_0^*\), which is dense by closability, gives weak convergence on a dense set of tests; the orbit bounds extend it to all tests.
The bounded \(K\) term and bounded left multiplication by \(N^*\) preserve this conclusion.

Apply the Banach-Liouville argument of [the orbit-map proof](Yin_C_F0036_v1.md#yin_c_f0036-p1) to \(a\mapsto A(av)\) and (38.3).
It proves commutation with \(N^*\), then with starred polynomials in \(N\).
Kaplansky approximation inside \(W^*(N)\), and the just-proved bounded-set weak continuity, give
\[
A(bv)=bAv\qquad(b\in W^*(N),\ v\in\mathcal E).
\tag{38.4}
\]
Here the left side converges weakly during approximation and the right side strongly; this is sufficient to identify their limits.
No closability of \(A\) has been assumed.

Partition the compact spectrum of \(N\) into finitely many Borel cells of diameter at most \(h>0\), with spectral projections \(e_1,\ldots,e_m\) summing to one.
Choose a point \(c_r\) in each nonempty cell and put
\[
r_r=(N^*-\bar c_r)e_r,
\qquad\|r_r\|\leq h.
\]
By (38.4), for fixed \(v\in\mathcal E\),
\[
Av=\sum_r e_r[D_0,N^*]e_rv-\delta\sum_r e_rKe_rv.
\tag{38.5}
\]
We estimate the first sum without any Hilbert-space bound for \(D_0\).
Averaging over independent signs \(\sigma_r\in\{1,-1\}\), orthogonality of the signs gives
\[
\sum_r\|D_0(e_rv)\|_2^2
=\mathbb E\left\|T_v\left(\sum_r\sigma_re_r\right)\right\|_2^2
\leq t_v^2,
\]
because each signed projection sum has norm one.
Likewise the disjoint spectral supports of \(r_r\) give
\[
\sum_r\|D_0(r_rv)\|_2^2
=\mathbb E\left\|T_v\left(\sum_r\sigma_rr_r\right)\right\|_2^2
\leq h^2t_v^2.
\]
The projections in the output are orthogonal, so cancellation of the scalar \(\bar c_r\) yields
\[
\begin{aligned}
\left\|\sum_r e_r[D_0,N^*]e_rv\right\|_2
&=\left\|\sum_r\bigl(e_rD_0(r_rv)-r_rD_0(e_rv)\bigr)\right\|_2\\
&\leq 2h\,t_v.
\end{aligned}
\tag{38.6}
\]
The estimate depends on the one vector \(v\) and is independent of the number of cells.

Under \(\Theta^{-1}\), the pinching \(\sum_r e_rKe_r\) is the kernel \(k(z,w)\) multiplied by the indicator that \(z,w\) belong to the same cell.
This indicator is supported on \(|z-w|\leq h\), and \(k\) is zero on the diagonal.
Dominated convergence therefore gives
\[
\left\|\sum_r e_rKe_r\right\|_{\mathrm{HS}}\longrightarrow0
\qquad(h\downarrow0).
\tag{38.7}
\]
No convergence assumption on the diagonal blocks of \(D_0\) is used.
Equations (38.5)-(38.7) imply \(Av=0\) for every \(v\in\mathcal E\), proving (38.1).

The original generator commutators and (38.1) extend from the specified graph core to \(\operatorname{Dom}\overline{D_0}\), because their representatives are bounded.
The product rule gives the same assertion for starred polynomials.
Pairing the identity for the adjoint polynomial yields invariance of \(\operatorname{Dom}D_0^*\) and the formula
\[
[D_0^*,a]=-[\overline{D_0},a^*]^*
\qquad(a\in\mathbb C\langle X,X^*\rangle),
\]
where the right side is the adjoint of the bounded commutator representative.
This proves the last assertion at its precise polynomial scope.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:54 |
| status | proved |
| reason | Adopt the exact actual original finding at its complete reviewed scope while preserving the mathematical assessment, fixed argument, dependencies and historical decisions. The original initial context-isolation fact remains unknown; no new or redated review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0037-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0066_v1.md#yin_c_f0037-spectral-pinching-and-domain-bridges) | Actual original complete C_F0037 finding at its disclosed accepted-input scope and unknown initial-context relationship; historical source precision and limits remain at this retained original finding. |


### Decision isolated-whole-review-2026-10-22

| Field | Value |
| --- | --- |
| date | 2026-10-22T20:21 |
| status | proved |
| reason | Adopt the actual new isolated whole-proof finding for the unchanged fixed statement and selected argument; retain all original assessments, source depths and useful negative boundaries at their historical scopes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#yin_c_f0037-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New whole-proof finding](../audits/reviews/Yin_R_F0066_v1.md#fresh-c38-whole) | Actual isolated whole-proof inspection at this exact fixed input, including all necessary accepted-input applicability and stated limits; historical findings remain separately unknown. |

## Historical assessments


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
| argument | [Exact material](#yin_c_f0037-p1) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0066_v1.md#yin_c_f0037-spectral-pinching-and-domain-bridges) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).



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

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0066_v1.md#yin_c_f0037-spectral-pinching-and-domain-bridges).

The original whole-source review included the bounded-reference comparison, the normal starred-commutator argument and the selfadjoint L1-density construction.
Its accompanying source context and complete original scope remain in the cited finding.

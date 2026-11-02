---
author: Yin
---

# Small-q bounded duals and all-q rational L2 reconstruction in one-dimensional real marginals

## Current assessment
[Selected decision](#decision-finding-owned-review)

## q-Gaussian Bounded Duals and Rational Boundedness

<a id="statement"></a>

<a id="q-gaussian-boundedness-route"></a>
Date: 2026-09-09.
Provenance: targeted primary-source reading and project deductions by another AI agent.
Authorization: the user's explicit continuation of the [Yin_T_F0001 analytic follow-up](../tasks/Yin_T_F0001_v1.md#authorized-regularity-follow-up), including q-Gaussian models.
Coordinating route: [Yin_S_F0007](../strategies/Yin_S_F0007.md#s_f0007); focused route: [Yin_S_F0008](../strategies/Yin_S_F0008.md#s_f0008).
This note does not reopen the refuted original conjecture.

## Source Interfaces and Their Scope

The following established external inputs are accepted at the inspected statement scope.
Their original proofs are not claimed to have undergone complete independent review.

- **MS23**, [arXiv:2203.00547v3](https://arxiv.org/pdf/2203.00547), Definition 2.4 (p. 7), Proposition 4.5 (p. 14), Theorem 4.6 (p. 17), Corollary 5.3 (pp. 24-25): finite q-Gaussian tuples, $-1<q<1$, have normalized polynomial-domain duals and Lipschitz conjugates.
  These statements do not bound the entire dual operators.
  Corollary 1.2(1), p. 3, identifies their affiliated division closure with the free field.
  The previously inspected interfaces are summarized in [the regularity evidence](Yin_C_F0016_v1.md#regularity-strategy-evidence).
- **Dab14**, [published PDF](https://www.numdam.org/article/AIHPB_2014__50_4_1404_0.pdf), Section 4.2.1, Lemma 27 and Theorem 28 (p. 1440; PDF p. 37), tensor conventions (p. 1441; PDF p. 38), Corollary 29 (p. 1442; PDF p. 39): right q-annihilation has commutator $\delta_{ij}\Xi_q$, $\Xi_q=\sum_{m\ge0}q^mP_m$; Wick evaluation obeys the homogeneous Haagerup bound.
  The corollary gives a projective-tensor inverse when $\nu(q,d)<1$, in particular $d\ge2$, $|q|d\le0.13$.
  The inverse concerns the tensor-algebra element representing the Hilbert-Schmidt kernel, not the operator inverse of the compact $\Xi_q$ on Fock space.
- **BKS97**, [arXiv:funct-an/9604010v1](https://arxiv.org/pdf/funct-an/9604010), Theorem 1.10(1) (p. 7) and Theorem 4.6(1) (p. 20): the one-variable spectral law is the q-Hermite measure on $[-2/\sqrt{1-q},2/\sqrt{1-q}]$ with the product density used below.
  These are preprint page numbers, also the one-based PDF page numbers.

The small-q bounded-dual assertion below is a project application of the projective inverse, with the operator action proved explicitly.
It is not an assertion that MS23's normalized duals have been shown bounded.

<a id="yin_c_f0020"></a>
## Yin_C_F0020: Two Verified q-Gaussian Interfaces

Initial assessment: complete proof draft awaiting independent review.
The [selected material decision](#current-assessment) owns the current assessment.
No novelty or optimal-parameter claim is made.

Let $-1<q<1$, $d<\infty$, and $X=(X_1,\ldots,X_d)$ be the canonical variance-one selfadjoint q-Gaussian tuple with its faithful vacuum trace on $M=\Gamma_q(\mathbb R^d)$.
Write
\[
F_X=\operatorname{Div}_{U(M)}\mathbb C\langle X\rangle,\qquad
\mathcal R_X=\operatorname{Div}_M\mathbb C\langle X\rangle.
\]

**A. Bounded-dual range.** Put $r=|q|$, $s=rd$ and
\[
C_r=\prod_{k=1}^{\infty}(1-r^k)^{-1},\qquad
\nu(q,d)=C_r^3\left[
\frac{4s}{1-s}+\frac{5s^2}{(1-s)^2}+\frac{2s^3}{(1-s)^3}
\right].
\tag{1}
\]
If $s<1$ and $\nu(q,d)<1$, the tuple has bounded operators $D_i$ on $L^2(M)$ satisfying
\[
[D_i,X_j]=\delta_{ij}P_\Omega.
\tag{2}
\]
For $d\ge2$, the explicit range $|q|d\le0.13$ suffices.
Consequently the original bounded-dual hypotheses of [Yin_C_F0013](Yin_C_F0013_v1.md#yin_c_f0013) apply to this canonical tuple in that range.
This part proves neither $F_X\cap L^2(M)\subseteq M$ nor $F_X\cap M=\mathcal R_X$.

**B. All-q scalar marginal.** Let $v\in\mathbb R^d\setminus\{0\}$, $h=\sum_i v_iX_i$ and $N=W^*(h)$.
Set
\[
F_h=\operatorname{Div}_{U(N)}\mathbb C[h],\qquad
\mathcal R_h=\operatorname{Div}_{N}\mathbb C[h].
\]
For every $-1<q<1$,
\[
F_h\cap L^2(N)=F_h\cap N=\mathcal R_h.
\tag{3}
\]
The same implication holds for a scalar rational function of $h$ tested in $L^2(M)$, because the trace and functional calculus restrict to $N$.
In addition, $h$ has a bounded dual on $L^2(N)$.
This last statement concerns its one-variable generated algebra; it does not construct a simultaneous bounded dual system for all coordinates at arbitrary q.

### Proof of A: correct the compact defect by a projective kernel

Let $\mathcal B=M\widehat\otimes_\pi M^{\mathrm{op}}$ be the Banach projective tensor algebra, with
\[
(a\otimes b^{\mathrm{op}})(c\otimes e^{\mathrm{op}})
=ac\otimes(eb)^{\mathrm{op}}.
\]
This is the diagonal case of the independently developed [Yin_C_F0018 correction lemma](Yin_C_F0018_v1.md#yin_c_f0018); the direct argument below fixes its q-specific kernel identification.
For $a\in M$, let $\rho(a)\widehat x=\widehat{xa}$ be right multiplication.
Define
\[
\kappa(a\otimes b^{\mathrm{op}})=aP_\Omega b,\qquad
Q_{a\otimes b^{\mathrm{op}}}(T)=\rho(a)T\rho(b).
\tag{4}
\]
Thus $\kappa(a\otimes b^{\mathrm{op}})\widehat x=\widehat a\,\tau(bx)$.
Both maps extend continuously in projective norm; $Q$ takes values in bounded maps on $B(L^2(M))$, and $\|Q_z\|\le\|z\|_\pi$.
The map $\kappa$ also agrees with the continuous Hilbert-Schmidt identification of the underlying $L^2$ tensor.

Right multiplication commutes with every left $X_j$.
Direct calculation on elementary tensors gives
\[
Q_u(\kappa(z))=\kappa(zu).
\tag{5}
\]
For example, the left side for $z=a\otimes b^{\mathrm{op}}$, $u=c\otimes e^{\mathrm{op}}$ sends $\widehat x$ to $\widehat{ac}\tau(ebx)$.
Continuity extends (5) to $\mathcal B$.
This order is essential: the right-multiplication action is an antihomomorphism in its tensor parameter.

For each q-particle subspace of degree $m$, choose an orthonormal basis $(\xi_{m,k})_{k=1}^{d^m}$ in its actual q-inner product.
Its Wick operators $b_{m,k}=W(\xi_{m,k})$ belong to $M$, have $L^2$ norm one, and satisfy
\[
\kappa\left(\sum_k b_{m,k}\otimes(b_{m,k}^*)^{\mathrm{op}}\right)=P_m.
\tag{6}
\]
Define the tensor directly in the specified projective algebra by
\[
K_q=1\otimes1+
\sum_{m\ge1}q^m\sum_{k=1}^{d^m}
b_{m,k}\otimes(b_{m,k}^*)^{\mathrm{op}}.
\]
The scalar Haagerup estimate, with $\|\xi_{m,k}\|_q=1$, gives
\[
\|K_q-1\otimes1\|_\pi
\le\sum_{m\ge1}|q|^m\sum_{k=1}^{d^m}\|b_{m,k}\|^2
\le C_{|q|}^3\sum_{m\ge1}(|q|d)^m(m+1)^2
=\nu(q,d).
\]
Because $|q|d<1$, this proves convergence in $\mathcal B$.
The last equality follows from $\sum_{m\ge1}(m+1)^2s^m=(1+s)/(1-s)^3-1$ and expansion of the bracket in (1).
Continuity of $\kappa$ and (6) identify the sum with the operator-norm limit of $\sum_{m=0}^nq^mP_m$.
Thus, agreeing with Dab14's Corollary 29, we have
\[
\kappa(K_q)=\Xi_q,\qquad
\|K_q-1\otimes1\|_\pi\le\nu(q,d)<1.
\tag{7}
\]
In particular $K_q^{-1}\in\mathcal B$ by the norm-convergent Neumann series, with norm at most $(1-\nu(q,d))^{-1}$.
The scalar Haagerup input and the finite basis in (6) also explain why this is a projective estimate: each kernel is a sum of $d^m$ bounded elementary tensors.
Mere invertibility in the spatial von Neumann tensor product would not justify the $B(L^2)$ action (4) used here.

Let $A_i=r(e_i)^*$ be right q-annihilation; these are bounded and, by the commutator identity in Lemma 27,
\[
[A_i,X_j]=\delta_{ij}\Xi_q.
\]
Define $D_i=Q_{K_q^{-1}}(A_i)$.
Approximation in projective norm and commutation of all $\rho(a)$ with $X_j$ yield
\[
[D_i,X_j]=Q_{K_q^{-1}}([A_i,X_j])
=\delta_{ij}\kappa(K_qK_q^{-1})
=\delta_{ij}P_\Omega.
\tag{8}
\]
All operators in (8) are bounded on the full Hilbert space, and $\|D_i\|\le\|A_i\|/(1-\nu(q,d))$.
No normalization $D_i\Omega=0$ is needed.

For completeness, the stated numerical sufficient range can be checked without optimizing it.
If $d\ge2$, $s\le13/100$, then $r\le13/200$.
The elementary product bound $\prod_k(1-r^k)\ge1-\sum_k r^k=(1-2r)/(1-r)$ gives
\[
C_r^3\le(187/174)^3.
\]
The bracket in (1) is increasing in $s$ and equals $f(s)=(1+s)/(1-s)^3-1$.
Therefore
\[
\nu(q,d)\le(187/174)^3
\left(\frac{1130000}{658503}-1\right)<1.
\tag{9}
\]
The last inequality is a strict comparison of positive rational numbers.
It includes the endpoint $s=0.13$.
This proves A.

### Proof of B: the endpoint exponent excludes an L2 pole

First take $\|v\|=1$, so $h$ has the variance-one q-Hermite law.
Set $a_q=2/\sqrt{1-q}$.
BKS97's product density, in the parametrization $x=a_q\cos\theta$, is
\[
w_q(x)=\frac{\sqrt{1-q}}{\pi}\sin\theta
\prod_{k=1}^{\infty}(1-q^k)|1-q^ke^{2i\theta}|^2,\qquad0\le\theta\le\pi.
\tag{10}
\]
For fixed $q$, all factors are positive and
\[
(1-r^k)^3\le(1-q^k)|1-q^ke^{2i\theta}|^2
\le(1+r^k)^3.
\]
Both bounding infinite products converge, and the lower product is strictly positive, since $\sum_k r^k<\infty$.
Hence constants $0<c_q<C_q'<\infty$ give
\[
c_q\sqrt{a_q^2-x^2}\le w_q(x)
\le C_q'\sqrt{a_q^2-x^2}\quad(-a_q\le x\le a_q).
\tag{11}
\]
In particular the density is bounded, is strictly positive in the interior, has full interval support, and has square-root vanishing at both endpoints.

Every element of $F_h$ is a scalar rational function $p(h)Q(h)^{-1}$.
Indeed, the scalar rational functions form a field in $U(N)$ because nonzero polynomials have only finitely many zeros and this law is nonatomic; the two inclusions in this description follow from the definition of division closure.
Cancel common factors of $p$ and $Q$, treating the zero function separately.

If the reduced denominator has a real zero $x_0$ in the spectral interval, the rational function has a pole of integer order $k\ge1$.
For an interior zero, its squared modulus times the density dominates a positive multiple of $|x-x_0|^{-2k}$ near $x_0$, which is not integrable.
At an endpoint the lower bound in (11) instead gives the nonintegrable power
\[
|x-x_0|^{1/2-2k};
\]
its exponent is at most $-3/2$.
Thus $L^2$ membership forces $Q$ to be zero-free on the whole compact spectral interval.
Then $Q(h)$ has a bounded inverse in $N$ and $p(h)Q(h)^{-1}\in\mathcal R_h$.
Conversely $\mathcal R_h\subseteq F_h\cap N\subseteq F_h\cap L^2(N)$, proving (3).
Scaling by $\|v\|$ preserves this proof and changes only the endpoints and positive constants.

Finally any bounded probability density $w$ on a compact interval $I$, positive almost everywhere there, admits the following bounded dual for its coordinate function.
With $V:L^2(w\,dx)\to L^2(dx)$ given by $Vf=\sqrt w f$, and
\[
(Tf)(s)=\operatorname{p.v.}\int_I\frac{f(t)}{t-s}\,dt,\qquad
D=V^{-1}M_{\sqrt w}T M_{\sqrt w}V,
\tag{12}
\]
the already accepted [Hilbert-transform interface in Yin_C_F0016](Yin_C_F0016_v1.md#yin_c_f0016) gives $\|T\|\le\pi$ and $\|D\|\le\pi\|w\|_\infty$.
On polynomial vectors, $[D,h]$ cancels the kernel denominator and equals the projection onto constants.
Density of polynomial vectors extends the equality to all of $L^2(w\,dx)$.
Apply this to (11) and its scaled version.
QED.

## What Remains for Several q-Gaussians

The q-Haagerup estimate supplies the analytic half of [Yin_C_F0015](Yin_C_F0015_v1.md#yin_c_f0015): choose an orthonormal basis in each q-particle space and label its $d^m$ vectors by words of length $m$.
Wick evaluation then gives $K_m=C_{|q|}^{3/2}(m+1)$.
However, finite residual rank of the coefficients of an arbitrary $f\in F_X\cap L^2(M)$ in that chosen basis has not been established.

This is a concrete coefficient issue already visible at degree two:
\[
\langle e_1\otimes e_2,e_2\otimes e_1\rangle_q=q,\qquad
\|e_i\otimes e_i\|_q^2=1+q.
\]
Thus elementary tensors are not an orthonormal word basis when $q\ne0$.
A Gram inverse square root gives a basis separately in each degree, but no finite-state compatibility across degrees follows from this construction.

There is also a direct commutator diagnostic.
For MS23's normalized polynomial-domain dual, the cubic recursion gives
\[
D_i e_{abc}=\delta_{ic}e_{ab}-q\,\delta_{ib}\delta_{ac}\Omega.
\tag{13}
\]
In particular its action is not simply deletion of the final letter.
The corresponding Wick derivative has the correction
\[
\partial_iW(e_{abc})
=\delta_{ia}1\otimes W(e_{bc})
+\delta_{ib}X_a\otimes X_c
+\delta_{ic}W(e_{ab})\otimes1
-q\,\delta_{ib}\delta_{ac}1\otimes1.
\tag{14}
\]
These identities follow directly by writing $W(e_{abc})=X_aX_bX_c-\delta_{bc}X_a-\delta_{ab}X_c-q\delta_{ac}X_b$.
They identify why the free suffix argument cannot be copied verbatim.
They do not prove that every alternative finite-state mechanism fails.

Even in the scalar marginal, orthonormal q-Hermite polynomials satisfy
\[
x p_m(x)=\sqrt{[m+1]_q}\,p_{m+1}(x)+\sqrt{[m]_q}\,p_{m-1}(x),
\qquad[n]_q=\frac{1-q^n}{1-q}.
\tag{15}
\]
For a resolvent $(z-h)^{-1}$, $z\notin[-a_q,a_q]$, its coefficients $\alpha_m$ therefore satisfy, for $m\ge1$,
\[
z\alpha_m=\sqrt{[m]_q}\,\alpha_{m-1}
+\sqrt{[m+1]_q}\,\alpha_{m+1}.
\tag{16}
\]
This supplies an exact next test: study an asymptotically constant recurrence with exponentially decaying coefficient perturbations before demanding a constant finite recurrence.
No assertion of finite or infinite Hankel rank for this resolvent is made here.
Part B independently establishes its boundedness.

A viable next step for the full tuple is to derive a similarly controlled residual or transfer equation from its q-Wick recursion, track the degree-dependent Gram geometry, and prove decay sufficient for the already available homogeneous estimate.
This may require a replacement for literal finite residual rank.
A norm-convergent homogeneous expansion would give boundedness; bounded scalar reconstruction would still require its separate rational representation/elimination input.

## Search and Verification Record

The search was triggered by the distinction between MS23's polynomial-domain duals and the bounded duals required by Yin_C_F0013.
Queries examined q-Gaussian bounded duals, Shlyakhtenko's q-commutator construction, projective inverses in Dabrowski's stochastic PDE paper, and q-Hermite marginal laws.
The productive source chain was MS23 to Dab14; BKS97 supplied the independent marginal test.
The work stops this source branch after these exact interfaces and coefficient diagnostics, without claiming an exhaustive survey or absence of stronger published results.

Additional primary material inspected but not needed as a new proof dependency: **Shl04**, Shlyakhtenko, *Some estimates for non-microstates free entropy dimension, with applications to q-semicircular families*, [arXiv:math/0308093v1](https://arxiv.org/pdf/math/0308093v1), Section 3/Lemma 3.1 (pp. 9-10), agrees with the compact-defect commutator quoted in Dab14.
**JL26**, Jekel and Landry, *Compact quantum metric spaces from free probability*, [arXiv:2606.19578v1](https://arxiv.org/html/2606.19578v1), introductory discussion, was checked as a current lead; its metric-space conclusions are not used as a bounded-dual or rationality theorem.

Online parsed source pages were inspected without retaining PDFs.
Numdam page-image requests timed out; its parsed formulas were cross-checked against their definitions, the corollary's displayed proof, and the explicit calculations above.
No full-source audit, numerical simulation, formal verification or external human review is claimed.
Yin_C_F0020's local proof and applicability require independent internal review before promotion.


## Assessment history


### Decision candidate-0002

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
| argument | [Exact material](#proof-of-a-correct-the-compact-defect-by-a-projective-kernel) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](#proof-of-b-the-endpoint-exponent-excludes-an-l2-pole) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0009_v1.md) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:36 |
| status | proved |
| reason | Select the actual retained finding and its explicit relationship at the unchanged mathematical input and original source boundaries; no new whole-proof review or changed mathematical status is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#proof-of-a-correct-the-compact-defect-by-a-projective-kernel) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact argument](#proof-of-b-the-endpoint-exponent-excludes-an-l2-pole) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact review](../audits/reviews/Yin_R_F0009_v1.md#q-gaussian-interfaces-finding) | Whole small-q projective bounded-dual construction, exact closed parameter bound, all-q scalar marginal rational closure, and degree-two/cubic/recurrence diagnostics, with original Dab14/MS23/BKS97 statement-depth limits and no multivariable all-q boundedness assertion. |

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

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0009_v1.md).

Material covered by that review: [Exact material](Yin_C_F0020_v1.md).

---
author: Yin
---

# Every recognizable q-Fock L2 series has exponential state energy; holomorphic q-circular scalar reconstruction

## Current assessment
[Selected decision](#decision-isolated-current-review-20261022)

## Recognizable q-Fock Series: Exponential Energy and Bounded Reconstruction

<a id="statement"></a>

Record kind: substantive research continuation and complete proof.
Date: 2026-09-11.
Author: another AI agent.
Objective: [Yin_T_F0006](../tasks/Yin_T_F0006_v1.md), the actual q-energy gap left by [Yin_C_F0098](Yin_C_F0098_v1.md#yin_c_f0098).
Registered as ordinary Claim Yin_C_F0101 after [independent review](../audits/reviews/Yin_R_F0111_v1.md#review-and-maintenance-scope); no mathematical Role is assigned.
Provenance: project deduction from the source inputs and finite-realization mechanism below; no novelty is asserted.
The older reviewed artifact remains unchanged.

<a id="yin_c_f0101"></a>
**Outcome.**
Every recognizable coefficient series that belongs to the actual q-Fock space has exponentially decaying homogeneous q-energy.
For a canonical finite q-circular system, its specified holomorphic series therefore converges in operator norm and belongs to the bounded scalar division closure of the unstarred polynomial algebra.
A finite matrix-energy test certifies this conclusion.
No assumption of permutation-invariant coefficients or weighted ordinary coefficient summability remains.

The mechanism is bounded deletion of a fixed prefix and suffix, followed by a uniformly bounded concatenation estimate for the complete minimal realization.
It does not give a constant-coefficient recurrence for the scalar energy, which remains excluded by [Yin_C_F0097](Yin_C_F0097_v1.md#yin_c_f0097).

## 1. Reuse, Source Inspection and Exact Norms

The local check read Yin_C_F0097-Yin_C_F0098 ([Yin_C_F0097_v1](Yin_C_F0097_v1.md), [Yin_C_F0098_v1](Yin_C_F0098_v1.md), [Yin_L_F0024_v1](../ledger/Yin_L_F0024_v1.md)), their [independent audit](../audits/reviews/Yin_R_F0109_v1.md#original-f0059-account), [Yin_C_F0015](Yin_C_F0015_v1.md#yin_c_f0015), and [Yin_C_F0017](Yin_C_F0017_v1.md#yin_c_f0017).
Crucially, [MS23-U001](../audits/literature/MS23/Yin_U001.md#ms23-u001) already proves boundedness of ordinary one-letter deletion in the actual q-inner product from a uniform one-factor symmetrizer comparison.
The same primary one-factor input is retained in [MS23-U001, Lemma 2.2](../audits/literature/MS23/Yin_U001.md#lemma-22-free-right-deletion-is-bounded).

A scoped primary search for q-Fock symmetrizer/deconcatenation bounds and recognizable q-series was followed by direct reading of [Nou, arXiv:math/0605789](https://arxiv.org/pdf/math/0605789), pp. 5-6, equation (3) and the proof of Lemma 1, and [Kemp-Miyagawa, arXiv:2409.03177v2](https://arxiv.org/html/2409.03177v2), Theorem 1.2 and Lemma 2.3.
The latter is already accepted as [KM26-U001](../audits/literature/KM26/Yin_U001.md#km26-u001).
These exact statement interfaces were checked; their full original foundational proofs were not re-audited.
No directly matching general recognizable q-series theorem was located in that scoped search, and no novelty claim follows.

Fix a finite alphabet of size d and real \(-1<q<1\).
Set \(V=\mathbb C^d\), with its standard orthonormal basis, and write
\[
P_q^{(n)}=\sum_{\pi\in S_n}q^{\operatorname{inv}(\pi)}U_\pi,
\qquad H_n=(V^{\otimes n},\langle\cdot,P_q^{(n)}\cdot\rangle_0).
\]
The displayed inner-product convention can equivalently place the positive symmetrizer in the other entry.
Let \(H_0=\mathbb C\Omega\) and \(\mathcal H_q=\bigoplus_{n\ge0}H_n\).
For coefficients \(\alpha_w\), put
\[
\xi_n=\sum_{|w|=n}\alpha_we_w,
\qquad e_n=\|\xi_n\|_q^2.
\tag{1}
\]
Thus the hypothesis is \(\sum_ne_n<\infty\), not \(\sum_w|\alpha_w|^2<\infty\).
Raw words within one degree are not orthonormal.

We need two different symmetrizer estimates.
There is \(\omega_q>0\), independent of n, such that
\[
P_q^{(n-1)}\otimes I\le\omega_q^{-1}P_q^{(n)},
\qquad I\otimes P_q^{(n-1)}\le\omega_q^{-1}P_q^{(n)}.
\tag{2}
\]
Nou's Lemma 1 proof states precisely this one-factor comparison.
In contrast, the uniform estimate for an arbitrary split is used only in the concatenation direction:
\[
P_q^{(n+m)}\le C_q(P_q^{(n)}\otimes P_q^{(m)}),
\qquad C_q=\prod_{k\ge1}(1-|q|^k)^{-1}<\infty.
\tag{3}
\]
This is Kemp-Miyagawa Lemma 2.3, also Nou's equation (3).
We do not assume a degree-independent reverse inequality for arbitrary splits, or a uniform equivalence with the ordinary coefficient norm.
The constants here are valid for negative q as well as positive q.

## 2. Fixed Padding Preserves Actual q-Summability

Let \(r_i(e_{wj})=\delta_{ij}e_w\), \(r_i\Omega=0\), be literal right deletion.
If \(Q_i\) is the ordinary rank-one projection onto \(\mathbb Ce_i\), then for \(\eta\in H_n\),
\[
\|r_i\eta\|_q^2
=\langle\eta,(P_q^{(n-1)}\otimes Q_i)\eta\rangle_0
\le\omega_q^{-1}\|\eta\|_q^2.
\]
Summing across orthogonal degrees gives a bounded operator on \(\mathcal H_q\).
This is the already audited MS23 deletion argument.
It is not q-annihilation, nor the q-adjoint of right creation.

Word reversal is unitary on every \(H_n\): conjugating a tensor permutation by reversal preserves its inversion number and hence its symmetrizer weight.
It transfers the right-deletion estimate to left deletion.
In particular both types of deletion preserve the positive-letter Fock space used for q-circular holomorphic coefficients.
Write \(B_q=\max\{1,\omega_q^{-1/2}\}\).

For fixed words u,v, delete the suffix v and then the prefix u, killing words too short or with mismatching letters.
The resulting bounded operator \(D_{u,v}\) has norm at most \(B_q^{|u|+|v|}\) and satisfies
\[
D_{u,v}\xi
=\sum_w\alpha_{uwv}e_w,
\quad \xi=\sum_n\xi_n\in\mathcal H_q.
\tag{4}
\]
This identity is first checked on finite words, then degree by degree for the Hilbert-space limit.
Its degree-n output comes solely from degree \(n+|u|+|v|\), so there is no infinite coefficient rearrangement.
Consequently
\[
\sum_n\left\|\sum_{|w|=n}\alpha_{uwv}e_w\right\|_q^2
\le B_q^{2(|u|+|v|)}\sum_ne_n<\infty.
\tag{5}
\]
Only fixed padding lengths are used; their constants need not remain bounded as the padding grows.

## 3. Every Entry of a Minimal Realization Is q-Summable

Assume \(\alpha_w=\lambda A_w\gamma\) is recognizable.
The zero series is immediate, so choose a nonzero series and a minimal realization of size N, with
\[
A_w=A_{i_1}\cdots A_{i_n},\qquad A_\varnothing=I_N.
\]
Reachability and observability allow words \(u_1,\ldots,u_N\) and \(v_1,\ldots,v_N\) such that the matrix U with rows \(\lambda A_{u_a}\) and the matrix V with columns \(A_{v_b}\gamma\) are invertible.
For every middle word w,
\[
(\alpha_{u_aw v_b})_{a,b}=U A_w V,
\qquad
A_w=U^{-1}(\alpha_{u_aw v_b})_{a,b}V^{-1}.
\tag{6}
\]
Each matrix-entry coefficient sequence is therefore a fixed finite complex linear combination of the padded sequences in (5).
Define
\[
\Xi_n^{ij}=\sum_{|w|=n}(A_w)_{ij}e_w\in H_n,
\qquad
a_n^2=\sum_{i,j=1}^N\|\Xi_n^{ij}\|_q^2.
\tag{7}
\]
Equations (5)-(6) imply
\[
\sum_{n\ge0}a_n^2<\infty.
\tag{8}
\]
This concerns the actual q-Gram energy of all state entries.
It does not bound the energy of unobservable or unreachable states in an arbitrary enlarged realization.
Minimality removes precisely that issue.
Also \(a_0^2=N\); the constant term and the identity state matrix are included.

## 4. Uniform Concatenation Gives Exponential Energy

Let \(J_{n,m}:H_n\otimes H_m\to H_{n+m}\) be literal concatenation.
Here the domain is the ordinary Hilbert tensor product of the two already deformed homogeneous spaces.
Inequality (3) says
\[
\|J_{n,m}\|\le\sqrt{C_q}.
\tag{9}
\]
Matrix multiplicativity gives the exact vector identity
\[
\Xi_{n+m}^{ij}
=J_{n,m}\left(\sum_{k=1}^N\Xi_n^{ik}\otimes\Xi_m^{kj}\right).
\tag{10}
\]
For fixed i,j, the triangle inequality and scalar Cauchy-Schwarz give
\[
\left\|\sum_k\Xi_n^{ik}\otimes\Xi_m^{kj}\right\|^2
\le
\left(\sum_k\|\Xi_n^{ik}\|_q^2\right)
\left(\sum_k\|\Xi_m^{kj}\|_q^2\right).
\]
Summing over i,j and using (9) proves
\[
a_{n+m}\le\sqrt{C_q}\,a_na_m.
\tag{11}
\]
There is no missing state-size factor; the two sums separate exactly into the squared matrix Hilbert-Schmidt energies in (7).
No matrix-valued Haagerup estimate is used.

Put \(b_n=\sqrt{C_q}\,a_n\).
Then \(b_{n+m}\le b_nb_m\), and (8) implies \(b_n\to0\).
Choose an integer k at least one with \(b_k<1\).
If \(b_k=0\), (11) shows that all \(a_n\) for \(n\ge k\) vanish.
Otherwise let \(\rho=b_k^{1/k}\in(0,1)\).
Writing \(n=lk+r\), \(0\le r<k\), gives
\[
b_n\le b_k^l b_r
\le\left(\max_{0\le r<k}b_r\rho^{-r}\right)\rho^n.
\tag{12}
\]
This includes r=0 since \(b_0=\sqrt{C_qN}\ge1\).
Hence in every case there are finite M and \(0<\rho<1\) with
\[
a_n\le M\rho^n\quad(n\ge0).
\tag{13}
\]
Applying the fixed row \(\lambda\) and column \(\gamma\) gives \(\|\xi_n\|_q\le\|\lambda\|\|\gamma\|a_n\).
Thus the original actual q-energy decays exponentially as well.

This proof establishes a useful finite certificate: for a minimal realization, the following are equivalent:

1. The scalar coefficient series belongs to \(\mathcal H_q\).
2. Every state-entry series belongs to \(\mathcal H_q\).
3. There is a finite k such that \(C_q a_k^2<1\).
4. The full state energy has an exponential bound (13).

The only additional direction is that (3) gives (12)-(13) directly, without first assuming (8); (4) implies (2), and scalar compression gives (1).
Each \(a_k^2\) is a finite q-Gram computation from the matrices \(A_i\).
Searching k therefore supplies a terminating certificate on every positive instance, not a decision procedure for all negative instances.
A rigorously bounded larger constant may replace \(C_q\) in a sufficient certificate.

## 5. Actual q-Circular Norm Sum and Scalar Division Closure

Let \(c_i=\ell_q(e_i)+\ell_q(f_i)^*\) for orthonormal one-particle vectors \(e_i,f_i\), and let \(\mathcal M=W^*(c_1,\ldots,c_d)\).
For positive words, \(c_w\Omega=e_w\).
Thus (1) is exactly the L2 energy of the holomorphic homogeneous blocks
\[
F_n(c)=\sum_{|w|=n}\alpha_wc_w.
\]
Kemp-Miyagawa Theorem 1.2 and (13) imply
\[
\sum_n\|F_n(c)\|
\le K\sum_n\sqrt{n+1}\rho^n<\infty.
\tag{14}
\]
The norm sum has the prescribed L2 vector \(\xi\), because both limits have the same degree cutoffs.

Set \(T=\sum_i A_i\otimes c_i\in M_N(\mathbb C\langle c\rangle)\).
The \((i,j)\)-entry of \(T^n\) is the holomorphic block with vector \(\Xi_n^{ij}\).
Apply the scalar homogeneous estimate to every entry.
For an operator matrix B, \(\|B\|\le(\sum_{ij}\|B_{ij}\|^2)^{1/2}\), by Cauchy-Schwarz on its action on column vectors.
Therefore
\[
\|T^n\|\le A(|q|)\sqrt{n+1}\,a_n,
\qquad \sum_n\|T^n\|<\infty.
\tag{15}
\]
Increase the constant to cover n=0 if necessary.
The Neumann series is consequently a bounded two-sided inverse of \(I-T\), and the scalar output \(\lambda(I-T)^{-1}\gamma\) equals (14).

For completeness, the [Yin_C_F0017 scalar-elimination argument](Yin_C_F0017_v1.md#5-bounded-matrix-evaluation-and-scalar-elimination) applies as follows.
Choose k with \(\|T^k\|<1\) and set \(S=I-T^k\).
Every leading principal block of S is invertible in its matrix von Neumann algebra because it is within distance one of the identity.
Successive scalar Schur elimination therefore has bounded invertible pivots: the invertibility of the preceding and next leading blocks gives invertibility of the next scalar Schur complement.
Starting with entries in \(\mathbb C\langle c\rangle\), each elimination step uses sums, products and an inverse of one scalar element boundedly invertible in \(\mathcal M\).
Hence
\[
S^{-1}\in M_N\left(\operatorname{Div}_{\mathcal M}\mathbb C\langle c\rangle\right).
\]
Using
\[
(I-T)^{-1}=(I+T+\cdots+T^{k-1})(I-T^k)^{-1}
\]
proves that its scalar output belongs to
\[
\operatorname{Div}_{\mathcal M}\mathbb C\langle c_1,\ldots,c_d\rangle.
\tag{16}
\]
This is finite scalar reconstruction in the unstarred algebra, not just membership in a matrix rational closure or in a norm closure.
Taking adjoints to estimate norms does not enlarge the algebra in the expression.

There is also a radial extension: (14)-(15) converge in operator norm locally uniformly for \(|z|<\rho^{-1}\) after replacing each c_i by \(zc_i\).
Thus the represented holomorphic branch extends to a disk of radius greater than one.
Its scalar energy generating function is analytic beyond the unit disk; it need not be rational.

## 6. A Noncommuting Example Beyond Both Cases of Yin_C_F0098

Take \(q=1/2\), \(t=3/4\),
\[
A_1=tE_{12},\qquad A_2=tE_{21},\qquad
\lambda=(1,0),\qquad \gamma=(1,0)^{\mathsf T}.
\]
This realization is reachable and observable: \(\gamma,A_2\gamma\) span the columns, and \(\lambda,\lambda A_1\) span the rows.
The state matrices do not commute.
The scalar coefficients equal \(t^{2m}\) on \((12)^m\), including the empty word, and vanish on every other word.
They are not invariant under permutation of the letters.

At degree four the only state-matrix words are 1212 and 2121, with coefficient \(t^4\) in the two different diagonal entries.
The permutations preserving the word 1212 have inversion numbers 0,3,3,4, giving
\[
\|e_{1212}\|_q^2=\|e_{2121}\|_q^2=1+2q^3+q^4.
\]
It follows that
\[
a_4^2=2(3/4)^8(21/16)=\frac{137781}{524288}.
\tag{17}
\]
An elementary rigorous bound suffices for the infinite-product constant.
The first four factors of \(C_{1/2}^{-1}\) have product \(315/1024\), and the remaining product is at least \(1-\sum_{j\ge5}2^{-j}=15/16\).
Thus
\[
C_{1/2}\le\frac{16384}{4725}<\frac72,
\qquad
C_{1/2}a_4^2
<\frac{964467}{1048576}<1.
\tag{18}
\]
The finite certificate proves actual q-summability, exponential decay and bounded scalar reconstruction of
\[
\sum_{m\ge0}(9/16)^m(c_1c_2)^m
=(1-(9/16)c_1c_2)^{-1}.
\]
However, Yin_C_F0098's weighted ordinary coefficient sum equals
\[
\sum_{m\ge0}|t|^{4m}(1-|q|)^{-2m}
=\sum_{m\ge0}(81/64)^m=\infty.
\]
Thus this example belongs to neither of Yin_C_F0098's two sufficient coefficient subclasses, but is covered by the present certificate.
No numerical truncation or unverified asymptotic estimate is used.

## 7. Consequence for Wick Series and the Remaining Goal Boundary

The exponential q-energy conclusion in Sections 2-4 is a statement about recognizable vectors in the q-Fock space itself.
For selfadjoint q-Gaussians, the accepted homogeneous Wick estimate \(\|W(\xi_n)\|\le C(n+1)\|\xi_n\|_q\), recorded in [MS23-U001](../audits/literature/MS23/Yin_U001.md#ms23-u001), consequently makes every such recognizable Wick series converge in operator norm.
This is a boundedness conclusion for its specified Wick coefficients.
The scalar rational reconstruction in Section 5 instead uses the multiplicativity of the q-circular holomorphic monomials; it is not asserted for Wick multiplication.

The argument closes the unrestricted recognizable holomorphic coefficient gap isolated in Section 7 of the older q record, subject to independent review.
It does **not** identify the expansion of an arbitrary affiliated rational function with a recognizable series.
In particular it does not prove that every affiliated rational q-Gaussian L2 element has recognizable Wick coefficients, or that an arbitrary evaluated holomorphic rational expression lies on its formal Taylor branch.
The full Yin_T_F0006 Q5 and Q6 statements retain those separate expansion/evaluation obligations.

The old obstruction to constant energy recurrence remains valid.
The present proof uses multiplicativity of the full matrix coefficient family, the uniform forward concatenation bound, and a sufficiently small finite block.
It never declares the scalar energy to be a finite-matrix power sequence.

## 8. Verification and Review Handoff

The author checked both deletion directions, fixed-padding constants and short words, complex minimal-realization coefficients, all matrix indices in (10)-(11), zero and finite-support cases, negative q and q=0, the constant degree, actual operator powers, scalar Schur elimination, and the strict example's four permutation weights and rational inequalities.
The single-factor deletion and arbitrary-split concatenation statements were separately read in their exact primary locators.
These are existing accepted source inputs; the new deduction is their combination through the complete state-matrix energy.

No code computation, formal verification, external human review, or novelty assessment was performed.
The candidate is complete at its stated scope and ready for an independent full review.
The author has not edited earlier proofs or assigned a Claim ID or Role.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:15 |
| status | proved |
| reason | Adopt the exact actual original finding at its disclosed unknown initial-context relationship. Preserve mathematical status, statement, selected proof, dependencies and historical decisions; no new mathematical proof version or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-fixed-padding-preserves-actual-q-summability) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0111_v1.md#review-and-maintenance-scope) | Entire eight-section recognizable q-Fock state-energy and q-circular reconstruction theorem, including radial extension, finite certificate, strict example and unresolved rational-evaluation boundary. Actual original finding with unknown initial-context relationship; original date and accepted inputs preserved. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the separate isolated current finding on the unchanged fixed statement and proof, with exact conditions and scope. Preserve historical findings, relationships, source depths and dates; no new mathematical proof version is introduced. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-fixed-padding-preserves-actual-q-summability) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0111_v1.md#current-isolated-finding) | Entire eight-section recognizable q-Fock state-energy and q-circular reconstruction theorem, including radial extension, finite certificate, strict example and unresolved rational-evaluation boundary. |

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
| review-status | independently reviewed |

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
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-fixed-padding-preserves-actual-q-summability) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0111_v1.md#review-and-maintenance-scope) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0111_v1.md#review-and-maintenance-scope).

Material covered by that review: [Exact material](Yin_C_F0101_v1.md).

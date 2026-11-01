---
author: Yin
---

# Small-q joint dual inverse and an obstruction to automatic adjoint-vacuum totality

## Current assessment
[Selected decision](#decision-isolated-current-review-20261022)

## Small-q Joint Dual Estimates and the Remaining Holomorphic Totality Gap

<a id="statement"></a>
<a id="yin_c_f0109"></a>

Date/author: 2026-09-11, another AI agent.
Record kind: bounded continuation of [Yin_T_F0006](../tasks/Yin_T_F0006_v1.md#yin_t_f0006).
Provenance: deductions from Yin_C_F0023 and the audited q-Fock foundations, followed by an explicit Hilbert-space perturbation test.
Assessment: complete statements and proofs below, author self-reviewed, awaiting independent review.
No Claim ID or Role is assigned.

The full normalized dual tuple is quantitatively close to literal terminal deletion for small absolute q, and its joint map is invertible after removing the vacuum.
This yields an explicit small-q joint-kernel estimate.
It does not establish the signed holomorphic totality required by Yin_C_F0107.
An arbitrarily small finite-degree perturbation of the backward shift shows why the joint-kernel and finite-polynomial properties alone do not supply adjoint-vacuum orbit density.
That orbit is distinct from the negative-adjoint ranges, with arbitrary input vectors, in the actual signed question.

Current assessment, 2026-09-11: registered as ordinary **Yin_C_F0109** after [complete independent mathematical review](../audits/reviews/Yin_R_F0119_v1.md#4-review-limits).
The quantitative joint inverse on the vacuum complement, the sufficient interval abs(q)<=1/(1000m^2), and the abstract failure of adjoint-vacuum orbit totality under arbitrarily small shift perturbations are proved.
This dated assessment supersedes the initial pending labels.
Signed Hilbert-space totality and multivariable Q5/Q6 remain unresolved.
No Role or lemma extraction is assigned.

## 1. Question and reuse boundary

Use [the signed-dual conventions and complete finite iterated-kernel proof](Yin_C_F0118_v1.md#argument), with d circular pairs and m=2d real coordinates.
The target is
\[
K_{\mathrm{iter}}
=\bigcap_{\substack{1\le k\le d,\ s\ge0\\ j_1,\ldots,j_s\in\{1,\ldots,d\}}}
\ker(D_k^-D_{j_s}^+\cdots D_{j_1}^+)
\stackrel{?}=H_+.
\tag{1}
\]
The preceding record proves (1) on finite polynomial vectors, and on all H at q=0.
[Yin_C_F0107](Yin_C_F0107_v1.md#yin_c_f0107) proves that positive rational L2 vectors satisfy all these tests; it does not supply (1).

The local inputs inspected before the new deduction were [Yin_C_F0023, Sections 2-3](Yin_C_F0023_v1.md#yin_c_f0023), [MS23-U001, Lemma 2.2](../audits/literature/MS23/Yin_U001.md#ms23-u001), [MS23-U002, the normalized-dual partition formula](../audits/literature/MS23/Yin_U002.md#ms23-u002), and [MS23-U003, the conjugate estimates](../audits/literature/MS23/Yin_U003.md#ms23-u003).
The existing holomorphic-kernel calculation supplies the exact leading-degree block used below.
These are sufficient for the proved estimates.

A bounded primary-source search for q-Fock joint creation maps, bounded normalized duals and holomorphic totality also inspected the abstracts/version information of [Kennedy-Nica](https://arxiv.org/abs/1009.0508) and [Miyagawa-Speicher](https://arxiv.org/abs/2203.00547).
The former concerns q-creation algebras; no assertion identifying its generators with the normalized duals, or resolving (1), was consumed.
The latter does not replace the previously audited published MS23 by a different preprint version.
No new external theorem or priority claim results from this search.
Section 5 is proved directly.

## 2. Extracting the degree-lowering remainder

First allow any m>=1 real q-Gaussian coordinates.
Let H be their q-Fock space, Omega its vacuum, P_n the n-particle projection, and P=P_0.
Write D_i for the bounded normalized dual of Yin_C_F0023, and r_i for literal rightmost-letter deletion: r_i(e_w tensor e_j)=delta_ij e_w and r_i Omega=0.
The r_i are not the q-adjoints of right creation.

Put t=abs(q), and retain the audited constants
\[
C_t=\prod_{k\ge1}(1-t^k)^{-1},\qquad
w_t^2=(1-t^2)^{-1}\prod_{k\ge1}\frac{1-t^k}{1+t^k},
\qquad c_t=w_t^{-1/2}.
\tag{2}
\]
All products are positive and finite for 0<=t<1.
Yin_C_F0023 gives polynomials a_{i,r} of degree at most 2r+1 such that
\[
\begin{aligned}
D_i&=\sum_{r\ge0}\sum_{k=1}^{2r+1}E_k(\rho(a_{i,r})),\\
E_k(T)&=\sum_{n\ge k}P_{n-k}TP_n,\qquad \|E_k(T)\|\le\|T\|,\\
\|a_{i,r}\|&\le
(2r+2)C_t^{3/2}m^r t^{r(r+1)/2}
c_t^{r+1}\sqrt{[r]_t!}.
\end{aligned}
\tag{3}
\]
Here rho is right multiplication, [0]_t!=1, and [r]_t! is the product of the first r q-integers with parameter t.
Each diagonal sum is strongly convergent and the outer sum is operator-norm convergent.

The exact leading-degree calculation in the preceding kernel record gives
\[
P_{n-1}D_iP_n=r_iP_n,\qquad E_1(D_i)=r_i.
\tag{4}
\]
Indeed, the normalized derivative of a monomial is the sum of prefixes multiplied by traces of the corresponding suffixes.
Only an empty suffix contributes to degree n-1; nonempty suffixes with nonzero trace have even length at least two.
Lower Wick terms also contribute degree at most n-3.
This proves the first identity on raw words.
Boundedness proves the second on H.

Apply the contractive map E_1 to the norm-convergent series (3), and subtract.
The r=0 term has only its first lowering diagonal and disappears:
\[
D_i-r_i
=\sum_{r\ge1}\sum_{k=2}^{2r+1}E_k(\rho(a_{i,r})),
\qquad
\|D_i-r_i\|\le\epsilon_m(t),
\tag{5}
\]
where
\[
\boxed{\displaystyle
\epsilon_m(t)=C_t^{3/2}
\sum_{r\ge1}2r(2r+2)m^r t^{r(r+1)/2}
c_t^{r+1}\sqrt{[r]_t!}.}
\tag{6}
\]
The ratio of consecutive positive summands tends to zero for fixed 0<t<1; at t=0 the sum is zero.
This compares whole operators on the actual q-Fock Hilbert space.
In particular, we do not identify the r=0 summand of (3), which is right q-annihilation, with literal deletion.
Equation (4) extracts the first lowering diagonal from the entire series, including its higher conjugate contributions.

## 3. The joint deletion map and its perturbation

Let mathfrak r:H -> H^{oplus m} send xi to (r_1 xi,...,r_m xi).
The one-step symmetrizer comparison in MS23-U001 gives the joint bound
\[
\sum_{i=1}^m\|r_i\xi\|_q^2\le c_t^2\|\xi\|_q^2.
\tag{7}
\]
On degree n the left side is the undeformed quadratic form of P^{(n-1)} tensor I, since the one-letter coordinate projections sum to I.
The source comparison bounds this by w_t^{-1} times the degree-n q-form.
Sum over the orthogonal input degrees.

Write C_i for literal right creation, C_i e_w=e_w tensor e_i.
It is bounded by the audited q-Fock construction.
Its q-commutation identity C_i^*C_i=I+q C_iC_i^*, checked on finite words by the q-annihilation formula, implies ||C_i||<=(1-t)^{-1/2}.
For q>=0 take norms in this positive identity; for q<0 it gives C_i^*C_i<=I.
Define
\[
\mathfrak c:H^{\oplus m}\longrightarrow\Omega^\perp,\qquad
\mathfrak c(\eta_1,\ldots,\eta_m)=\sum_i C_i\eta_i.
\]
The triangle inequality and Cauchy-Schwarz yield
\[
\|\mathfrak c\|\le\frac{\sqrt m}{\sqrt{1-t}}.
\tag{8}
\]
On finite words r_i C_j=delta_ij I and sum_i C_i r_i=I-P.
Boundedness extends both identities:
\[
\mathfrak r\mathfrak c=I,\qquad \mathfrak c\mathfrak r=I-P.
\tag{9}
\]
Thus the joint deletion map restricted to Omega-perp is a bounded isomorphism onto H^{oplus m}.
Individual creation ranges need not be orthogonal in the q-inner product.

For the full normalized dual tuple put mathfrak D xi=(D_1 xi,...,D_m xi), and Delta=mathfrak D-mathfrak r.
Equation (5) gives ||Delta||<=sqrt(m) epsilon_m(t).
If
\[
\boxed{\displaystyle
\rho_m(t):=\frac{m\epsilon_m(t)}{\sqrt{1-t}}<1,}
\tag{10}
\]
then mathfrak D mathfrak c=I+Delta mathfrak c is invertible by a norm-convergent Neumann series.
Since mathfrak c is the inverse in (9), this proves
\[
\begin{aligned}
(\mathfrak D|_{\Omega^\perp})^{-1}
&=\mathfrak c(I+\Delta\mathfrak c)^{-1},\\
\|(\mathfrak D|_{\Omega^\perp})^{-1}\|
&\le \frac{\sqrt m}{\sqrt{1-t}(1-\rho_m(t))},\\
\bigcap_{i=1}^m\ker D_i&=\mathbb C\Omega.
\end{aligned}
\tag{11}
\]
In particular
\[
\|\mathfrak D\xi\|
\ge\frac{\sqrt{1-t}(1-\rho_m(t))}{\sqrt m}\|\xi\|,
\qquad \xi\perp\Omega.
\tag{12}
\]
For m=2d the signed change from the real duals to D_1^+,D_1^-,...,D_d^+,D_d^- is unitary on output coordinates.
It preserves these joint norms and invertibility conclusions, with the corresponding signed deletion maps.
Equation (11) controls the common kernel of all positive and negative duals, not the common kernel of the iterated tests in (1).

## 4. A conservative explicit parameter interval

If z=m c_t t/sqrt(1-t)<1, then t^{r(r+1)/2}<=t^r and [r]_t!<=(1-t)^{-r} give
\[
\epsilon_m(t)\le4C_t^{3/2}c_t\sum_{r\ge1}r(r+1)z^r
=\frac{8C_t^{3/2}c_t z}{(1-z)^3}.
\tag{13}
\]
The elementary inequality -log(1-u)<=u/(1-u) gives log C_t<=t/(1-t)^2.
The product for w_t also gives
\[
\begin{aligned}
\log c_t
&=\frac14\left(\log(1-t^2)
+\sum_{k\ge1}\bigl(\log(1+t^k)-\log(1-t^k)\bigr)\right)\\
&\le\frac12\sum_{k\ge1}\frac{t^k}{1-t^k}
\le\frac{t}{2(1-t)^2}.
\end{aligned}
\tag{14}
\]
For t<=1/(1000m^2), in particular t<=1/1000, these estimates give C_t<=2, c_t<=2 and (1-t)^{-1/2}<=2.
Thus z<=4mt<=1/250, and
\[
\rho_m(t)\le
\frac{256\sqrt2\,m^2t}{(1-4mt)^3}
\le\frac{256\sqrt2}{1000(249/250)^3}<1.
\tag{15}
\]
The last inequality follows already by replacing sqrt(2) by 3/2 and multiplying positive rational denominators.
Therefore
\[
\boxed{\ |q|\le\frac1{1000m^2}
\quad\Longrightarrow\quad\text{all conclusions of (11)-(12)}.\ }
\tag{16}
\]
This is deliberately conservative.
For d=2 circular pairs it gives |q|<=1/16000, since m=4.
Nothing here establishes (10) or (1) at q=1/2.
No numerical approximation of the infinite products or unrecorded finite computation is used as proof.

## 5. Small norm and finite-polynomial triangularity do not give orbit totality

This is an abstract obstruction to a proposed inference from joint invertibility, not a counterexample involving actual q-Gaussian duals or a refutation of (1).

On H_0=ell2(N_0) let S be the unilateral shift, with standard orthonormal basis v_n and vacuum v_0.
Given any 0<epsilon<1, choose an odd integer N>=3 with N epsilon>2, and set
\[
B=S^*+\epsilon(S^*)^N
=\bigl(I+\epsilon(S^*)^{N-1}\bigr)S^*.
\tag{17}
\]
Then ||B-S^*||=epsilon.
The first factor is invertible by a Neumann series.
Consequently ker B=C v_0 and B restricted to v_0-perp is a bounded isomorphism onto H_0.
Also B lowers finite polynomial degree, its leading lowering term is S^*, and its extra term lowers degree by the odd integer N.
It is locally nilpotent on the finite span of the v_n.

Nevertheless,
\[
\overline{\operatorname{span}}\{(B^*)^r v_0:r\ge0\}\ne H_0.
\tag{18}
\]
Here is an explicit verification.
Put theta=1/N^2 and zeta=exp(i theta).
Since 0<=k theta<1/N for 0<=k<N,
\[
\operatorname{Re}\sum_{k=0}^{N-1}\zeta^k>N/2>1/\epsilon.
\]
Choose any (N-1)-st root
\[
z_1^{N-1}
=-\left(\epsilon\sum_{k=0}^{N-1}\zeta^k\right)^{-1},
\qquad z_2=\zeta z_1.
\tag{19}
\]
Then 0<|z_1|=|z_2|<1 and z_1!=z_2.
For phi(z)=z+epsilon z^N, use 1-zeta^N=(1-zeta)sum_{k=0}^{N-1}zeta^k:
\[
\phi(z_1)-\phi(z_2)
=z_1(1-\zeta)
\left(1+\epsilon z_1^{N-1}\sum_{k=0}^{N-1}\zeta^k\right)=0.
\tag{20}
\]
The vectors k_z=sum_{n>=0}z^n v_n belong to H_0 for |z|<1 and satisfy S^*k_z=z k_z.
Hence eta=k_{z_1}-k_{z_2} is nonzero, eta is orthogonal to v_0, and B eta=phi(z_1) eta.
For every r>=0, with the inner product linear in the second argument,
\[
\langle (B^*)^r v_0,\eta\rangle
=\langle v_0,B^r\eta\rangle=0.
\tag{21}
\]
This proves (18).
No qualitative noninjectivity theorem for holomorphic functions is needed; (19)-(20) give explicit points.

The polynomial phi also has critical points inside the unit disk because N epsilon>1.
This describes the mechanism: an unweighted operator-norm perturbation may have uncontrolled high-degree analytic behavior.
The example lets N grow as epsilon decreases; it does not exclude a stronger perturbation argument controlling the degree-weighted coefficients of the actual q-duals.

## 6. What remains for the signed problem

Equations (10)-(16) give a full-space joint inverse and exclude extra simultaneous zero vectors for all signs.
The target (1) instead requires the exact density
\[
H_+^\perp
=\overline{\operatorname{span}}
\{(D_{j_1}^+)^*\cdots(D_{j_s}^+)^*(D_k^-)^*\eta:
\eta\in H,\ s\ge0,\ 1\le k,j_1,\ldots,j_s\le d\}.
\tag{22}
\]
The joint inverse supplies no uniform estimate for arbitrarily long positive-adjoint strings or their compatibility with the negative ranges.
Applying a fixed finite product to a polynomial approximation does not preserve the simultaneous kernels.
Finite-polynomial triangularity therefore cannot be extended merely by density.

The counterexample in Section 5 concerns the orbit of one vacuum vector, whereas (22) starts with the full ranges of the negative adjoints, using arbitrary eta in H.
It does not disprove a theorem specific to those ranges.
Its precise conclusion is that small norm, a vacuum-only joint kernel, and leading-degree triangularity do not generally imply adjoint-vacuum orbit totality; these properties cannot be treated as a general automatic cyclicity principle to close the signed argument.

The super-quadratic powers of t in (6) leave a plausible stronger route involving degree-weighted perturbation estimates or controlled simultaneous reconstruction of (22).
No such criterion or reconstruction is proved here.
Neither the all-q target nor a nonzero small-q interval for (1) is established by this record.

This bounded branch stops with the complete estimate (10), sufficient interval (16), and obstruction (17)-(21).
A next attempt must use an additional quantitative or structural property of the actual normalized duals.
The stronger multivariable Q5/Q6 objectives remain open.

## 7. Author checks and review scope

The author rechecked extraction of E_1 from the entire norm-convergent Yin_C_F0023 series, the r=0 cancellation in (5), the symmetrizer sum in (7), both identities in (9), and all dimension and square-root factors in the joint perturbation bound.
The signed transformation uses both signs and m=2d.
Product inequalities and the conservative threshold were derived symbolically.
The counterexample has an explicit nonzero eigenvector orthogonal to every adjoint-vacuum orbit vector, while retaining the exact vacuum kernel and finite-polynomial lowering.

Independent review should cover these deductions and their precise boundaries in Sections 5-6.
Earlier source-audit depths are retained.
No formal verification, numerical evidence, external human review or novelty claim is asserted.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:46 |
| status | proved |
| reason | Adopt the exact original finding at its disclosed unknown initial-context relationship. Preserve the mathematical statement, status, selected proof, conditional boundaries, dependencies and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#3-the-joint-deletion-map-and-its-perturbation) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0119_v1.md#4-review-limits) | Whole seven-section quantitative joint dual inverse on the vacuum complement, explicit sufficient absolute-q interval 1/(1000m squared), and arbitrarily small shift-perturbation failure of one adjoint-vacuum orbit totality. Signed iterated-kernel Hilbert totality and multivariable Q5/Q6 remain open. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the separate isolated current finding on the unchanged fixed statement and proof, with exact conditions and scope. Preserve historical findings, relationships, source depths and dates; no new mathematical proof version is introduced. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#3-the-joint-deletion-map-and-its-perturbation) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0119_v1.md#current-isolated-finding) | Complete Sections 1–7: quantitative small-q joint inverse on the vacuum complement and the explicit single adjoint-vacuum-orbit obstruction. The original signed target involving full negative-adjoint ranges and arbitrary vectors remains unresolved. |

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

Original review classification and limitations: independently reviewed; signed totality open

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
| argument | [Exact material](#3-the-joint-deletion-map-and-its-perturbation) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0119_v1.md#4-review-limits) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original review classification and limitations: independently reviewed; signed totality open

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

<a id="decision-candidate-0004"></a>

### Historical assessment candidate-0004

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T02:52 |
| status | proved |
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#3-the-joint-deletion-map-and-its-perturbation) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0119_v1.md#4-review-limits) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0119_v1.md#4-review-limits).

Material covered by that review: [Exact material](Yin_C_F0109_v1.md).

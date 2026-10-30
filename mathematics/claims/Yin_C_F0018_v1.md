---
author: Yin
---

# Projective inverse-Jacobian correction of duals and the finite-rank obstruction

## Current assessment
[Selected decision](#decision-isolated-review-20261022)

## Analytic Free Transport: Bounded Duals and Rationality Boundaries

<a id="statement"></a>

<a id="analytic-free-transport-boundedness"></a>
Date: 2026-09-09.
Authorization: the user's expanded [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001) program and explicit investigation of analytic free transport.
Route: [Yin_S_F0010](../strategies/Yin_S_F0010.md#s_f0010), under [Yin_S_F0007](../strategies/Yin_S_F0007.md#s_f0007).
The original bounded conjecture remains refuted.
Human author: Yin.
Proof development: mathematical AI agent another AI agent.
No novelty claim is made.

<a id="yin_c_f0018"></a>
## Yin_C_F0018: Projective Tensor Correction of Bounded Duals

Initial assessment: complete proof draft awaiting independent review.
The [selected assessment](#decision-isolated-review-20261022) records the mathematical and review assessments.
The result establishes bounded duals under an explicit inverse-Jacobian condition, together with a precise obstruction to transporting finite rank by the same argument.
It does not establish a general rational boundedness theorem for analytic transports.

Review integration, 2026-09-09: the [independent complete review](../audits/reviews/Yin_R_F0064_v1.md#projective-dual-correction-finding) by another AI agent passed Sections 1-6, including the exact GS14 applicability interface, without mathematical corrections.
The initial assessment above is historical; the [selected assessment](#decision-isolated-review-20261022) records the mathematical and review assessments.

### 1. Algebra, norms, and the correction lemma

Let $(M,\tau)$ be finite with faithful normal tracial state, $H=L^2(M,\tau)$, $\Omega=1$, and $P=P_\Omega$.
Write $\rho(a)\xi=\xi a$ for bounded right multiplication.
Use the usual Banach projective tensor product
\[
\mathcal B=M\widehat\otimes_\pi M^{\mathrm{op}},
\qquad
\|z\|_\pi=\inf\sum_\nu\|a_\nu\|\|b_\nu\|
\]
on finite representations $z=\sum_\nu a_\nu\otimes b_\nu$, followed by completion.
The second factor is labeled opposite; its multiplication is
\[
(a\otimes b)(c\otimes d)=ac\otimes db.
\tag{1}
\]
This extends continuously and makes $\mathcal B$ a unital Banach algebra.
Elements admit countable representations with summable products of norms.
We do not assume that any map from this completion into a von Neumann tensor product is injective.

For an elementary tensor and $T\in B(H)$ define
\[
Q_{a\otimes b}(T)=\rho(a)T\rho(b),
\qquad
\kappa(a\otimes b)=aPb.
\tag{2}
\]
Both maps extend to $\mathcal B$:
\[
\|Q_z(T)\|\le\|z\|_\pi\|T\|,
\qquad
\|\kappa(z)\|_1\le\|z\|_\pi.
\tag{3}
\]
The second estimate uses the trace norm of a rank-one operator, $\|aPb\|_1=\|a\Omega\|_2\|b^*\Omega\|_2\le\|a\|\|b\|$.
The universal projective-norm bound makes the extensions independent of the chosen tensor series.
The same estimate as for $B(H)$ holds on the trace class $\mathcal S_1(H)$.

For $z,w\in\mathcal B$, direct computation on elementary tensors gives
\[
Q_w\circ Q_z=Q_{zw},\qquad
Q_w(\kappa(z))=\kappa(zw).
\tag{4}
\]
For example, $Q_{c\otimes d}(aPb)=acPdb$.
Thus $Q$ is an antihomomorphism into maps on $B(H)$, and the product order in (4) is essential.
Also, for $y\in M$,
\[
[Q_z(T),y]=Q_z([T,y]),
\tag{5}
\]
because right multipliers commute with left multiplication by $y$.
Approximation in the projective norm proves (4)-(5) for completed tensors.

Now suppose $Y=(Y_1,\ldots,Y_d)\in M^d$, $A_1,\ldots,A_d\in B(H)$, and a matrix $\mathcal J=(\mathcal J_{jk})\in M_d(\mathcal B)$ satisfy
\[
[A_k,Y_j]=\kappa(\mathcal J_{jk}).
\tag{6}
\]
Assume $\mathcal J$ is invertible in the Banach algebra $M_d(\mathcal B)$, and put $\mathcal H=\mathcal J^{-1}$.
Define
\[
E_i=\sum_{k=1}^d Q_{\mathcal H_{ki}}(A_k).
\tag{7}
\]
Then $E_i$ is bounded and
\[
\begin{aligned}
[E_i,Y_j]
&=\sum_k Q_{\mathcal H_{ki}}\bigl(\kappa(\mathcal J_{jk})\bigr)\\
&=\kappa\left(\sum_k\mathcal J_{jk}\mathcal H_{ki}\right)
=\delta_{ji}P.
\end{aligned}
\tag{8}
\]
This is the bounded-dual correction lemma.
Neither normality nor generation by $Y$ is required to obtain (8).
They must be imposed separately when applying [Yin_C_F0013](Yin_C_F0013_v1.md#yin_c_f0013).

Use the submultiplicative column-sum matrix norm
\[
\|B\|_{\pi,1}=\max_i\sum_k\|B_{ki}\|_\pi.
\]
Equation (3) gives
\[
\max_i\|E_i\|
\le\|\mathcal H\|_{\pi,1}\max_k\|A_k\|.
\tag{9}
\]
If $\|\mathcal J-I\|_{\pi,1}\le\epsilon<1$, its inverse is the projective-norm convergent Neumann series and $\|\mathcal H\|_{\pi,1}\le(1-\epsilon)^{-1}$.

The diagonal case is useful independently of transport: if $[A_i,Y_j]=\delta_{ij}\kappa(K)$ with one invertible $K\in\mathcal B$, then $E_i=Q_{K^{-1}}(A_i)$.
In particular, a bounded Hilbert-Schmidt-valued dual relation is correctable when its kernel tensor has this specified projective inverse.
Hilbert-Schmidt membership alone supplies no such inverse.

### 2. Apply the lemma to an analytic change of variables

Let bounded $X=(X_1,\ldots,X_d)$ have bounded duals $D_k$, so $[D_k,X_\ell]=\delta_{k\ell}P$.
Choose $R>r>0$ with $\max_\ell\|X_\ell\|\le r$.
For a scalar noncommutative series
\[
F_j(z)=\sum_w c_{j,w}z^w,\qquad
|F_j|_R=\sum_w|c_{j,w}|R^{|w|}<\infty,
\]
set $Y_j=F_j(X)$.
It is an operator-norm convergent evaluation.
Termwise free difference quotients have absolutely convergent evaluated tensors:
\[
\mathcal J_{jk}=(\partial_kF_j)(X)\in\mathcal B.
\]
Indeed, a monomial of length $n$ contributes at most $nr^{n-1}$ to the sum over $k$ of projective norms, and
\[
nr^{n-1}\le\frac{R^n}{R-r}.
\]
For instance this follows from $n(r/R)^{n-1}\le\sum_{\ell=0}^{n-1}(r/R)^\ell$.
Consequently
\[
\sum_k\|\mathcal J_{jk}\|_\pi
\le\frac{|F_j|_R}{R-r}.
\tag{10}
\]
Constant coefficients contribute zero.

On polynomials, the product rule gives $[D_k,F_j(X)]=\kappa((\partial_kF_j)(X))$.
Polynomial truncation converges in operator norm on the left, and its derivative tensors converge in projective norm on the right.
Thus (6) holds with $A_k=D_k$ for the analytic $F_j$ as well.

If this evaluated Jacobian is invertible in $M_d(\mathcal B)$, (7) constructs bounded duals for $Y$.
A simple explicit sufficient condition is
\[
F_j(z)=z_j+G_j(z),\qquad
\frac{\sum_j|G_j|_R}{R-r}<1.
\tag{11}
\]
By (10), the left side bounds $\|\mathcal J-I\|_{\pi,1}$, so (9) provides a quantitative dual bound.

When $X$ and the evaluated $Y_j$ are selfadjoint and $X=G(Y)$ for an actually convergent analytic inverse, $W^*(Y)=W^*(X)$ and $C^*(Y)=C^*(X)$.
Normality and generation then permit Yin_C_F0013 for $Y$.
Invertibility of the evaluated Jacobian alone is not used to claim existence of a global inverse map or generation of the same algebra.

An affine check fixes the index convention: for $Y=BX+c$, $\mathcal J=B$ and (7) gives $E=B^{-T}D$, agreeing with [Yin_C_F0006](Yin_C_F0006_v1.md#yin_c_f0006).
For a polynomial shear, (7) similarly gives the finite right-multiplier correction already recorded there.

### 3. Why projective control does not preserve finite rank

If $z$ is a finite sum of elementary tensors, $Q_z$ maps finite-rank operators to finite-rank operators.
For a general projectively summable $z$, (3) only supplies a trace-class bound.
The stronger implication fails even arbitrarily close to the identity in the projective norm.

Take $M=L^\infty(\mathbb T)$ with normalized Haar trace, let $v(z)=z$, and let $P_n$ be the rank-one projection onto $v^n\in L^2(\mathbb T)$.
For $0<\epsilon<1$, put
\[
L=1\otimes1+\epsilon\sum_{n\ge1}2^{-n}v^n\otimes v^{-n}.
\tag{12}
\]
Then $\|L-1\|_\pi\le\epsilon<1$, so $L$ is invertible in $\mathcal B$.
However,
\[
Q_L(P)=P+\epsilon\sum_{n\ge1}2^{-n}P_n
\tag{13}
\]
has infinite rank.
The vectors $1,v,v^2,\ldots$ are orthonormal, and every displayed diagonal eigenvalue is nonzero.
The series converges in trace norm, as guaranteed by (3), but its rank is infinite.

This proves the claimed finite-rank-preservation obstruction.
It is an obstruction to a general tensor-summation inference, not a construction of an analytic transport whose rational boundedness theorem fails: (12) is not asserted to be a free Jacobian of any coordinate map.

For every bounded $f$, the transported commutators satisfy
\[
[E_i,f]=\sum_k Q_{\mathcal H_{ki}}([D_k,f]).
\tag{14}
\]
Thus finite rank on the right of (14) need not survive the infinite tensor expansion.
Conversely the exact identity
\[
D_k=\sum_iQ_{\mathcal J_{ik}}(E_i)
\]
follows from (4) and $\mathcal H\mathcal J=I$, but has the same issue.
Finite algebraic tensor decompositions of both matrices would preserve finite rank in both directions; projective invertibility by itself does not provide them.
QED for the correction lemma and the obstruction.

## 4. What the GS14 Interface Supplies

[GS14](../literature/readme.md) is Alice Guionnet and Dimitri Shlyakhtenko, *Free monotone transport*, Inventiones mathematicae 197 (2014), 613-661, DOI 10.1007/s00222-013-0493-9.
The inspected [arXiv v3](https://arxiv.org/pdf/1204.2182) has 37 pages and is dated 2013-10-08.

Sections 2.1 and 2.5 specify analytic coefficient and tensor norms.
Theorems 3.15-3.16, pp. 27-28, give transports $F_W(S)=S+f_W(S)$ from a semicircular tuple for sufficiently small selfadjoint analytic potential perturbations, with $|f_W|_{A'}\to0$ for fixed $A'>4$.
Theorem 4.2, p. 29, also supplies an analytic inverse after further smallness.
These are accepted statement-level inputs; their original complete proofs are not re-audited here.
[Primary preprint](https://arxiv.org/pdf/1204.2182).

The exact source hypotheses, accepted-input decision and reading boundary are indexed in [GS14-U001](../audits/literature/GS14/Yin_U001_v1.md#gs14-u001).
That unit records the source input; the projective correction and its application remain the local deduction proved here.

Our deduction is explicit: since $\|S_i\|=2$, choose $R=A'$ and $r=2$ in (11).
The source's coefficient-norm convergence makes (11) hold for sufficiently small perturbations.
Therefore these sufficiently small transports admit bounded duals, and their selfadjointness and analytic inverse supply the remaining Yin_C_F0013 hypotheses.
This uses the direct absolute-coefficient estimate (10); it does not infer a usual projective inverse merely from positivity or invertibility in $M\bar\otimes M^{\mathrm{op}}$.

This source use and deduction give a bounded-dual interface for small analytic transports.
They do not identify the rational fields in the old and new coordinates.

## 5. The Two Boundedness Targets Remain Separate

Put
\[
F_Y=\operatorname{Div}_{U(M)}\mathbb C\langle Y\rangle,\qquad
R_Y=\operatorname{Div}_M\mathbb C\langle Y\rangle.
\]
Yin_C_F0013 now gives a finite-defect criterion for $F_Y$, but the route still seeks
\[
F_Y\cap L^2(M)\subseteq M,\qquad
F_Y\cap M=R_Y.
\tag{15}
\]
An analytic inverse makes the C*-algebras and von Neumann algebras agree.
It does not assert $F_Y=F_X$ or $R_Y=R_X$, since their definitions allow finite rational expressions, not arbitrary convergent power series.

A concrete scalar check demonstrates the field issue.
Let $S$ be standard semicircular and $Y=S+\delta\sin S$, with nonzero real $|\delta|$ sufficiently small for (11).
The real function $x+\delta\sin x$ is strictly increasing on $[-2,2]$ when $|\delta|<1$, so $C^*(Y)=C^*(S)$ and $W^*(Y)=W^*(S)$.
Nevertheless $Y\notin\mathbb C(S)$: equality with a rational function on the interval would, by analytic identity, make the entire function $z+\delta\sin z$ rational, hence polynomial, which it is not.
Thus $F_Y\ne F_S$.
The analytic-map obstruction is real even for maps as close to the identity as desired.

This is not a scalar counterexample to (15).
More generally, if $Y=F(S)$ for a real $C^1$ strictly increasing function with $0<c\le F'\le C$ on $[-2,2]$, both properties in (15) hold in one variable.
Here is the direct consistency check.
A scalar rational function in $Y$ with a reduced pole of order $m\ge1$ at $F(x_0)$ has size comparable to $|x-x_0|^{-m}$ after substitution.
Against the semicircle density its squared modulus is nonintegrable at an interior point, and at an endpoint behaves as a constant times $|x-x_0|^{1/2-2m}$, also nonintegrable.
Thus an $L^2$ rational function has no poles on the compact spectrum.
Its reduced denominator is boundedly invertible, proving both assertions.
This elementary scalar argument supplies a baseline, not a multivariable transport theorem.

Two sufficient mechanisms retain useful content for several variables:

- **Rational compatibility.** If the old and new coordinates are each bounded scalar rational expressions in the other, then $R_X=R_Y$ and $F_X=F_Y$, by substituting the finite valid expressions in both directions.
  The established semicircular boundedness results transfer.
  This includes the Yin_C_F0006 families; general analytic transport does not assert this hypothesis.
- **A fixed bounded realization with a spectral margin.** For a fixed affine pencil $A(Z)=A_0+\sum_iA_iZ_i$, if $A(X)$ is boundedly invertible and
  \[
  \|A(X)^{-1}\|\sum_i\|A_i\|\|Y_i-X_i\|<1,
  \]
  the Neumann argument makes $A(Y)^{-1}$ bounded.
  A scalar compression then has a bounded realization.
  For selfadjoint $Y$, [Yin_C_F0008](Yin_C_F0008_v1.md#yin_c_f0008) converts its polynomial matrix entries and bounded inverse into bounded scalar expressions.
  This checks a specified realization; it is not a uniform estimate for every bounded affiliated rational output at $Y$.

The remaining general implication needs additional control of rational fields, finite residuals, or all required inverse states.
Trace-class control from (14) and the inherited semicircular norm estimate do not by themselves supply any of these.

## 6. Search, Checks, and Next Mathematical Test

The 2026-09-09 source check followed the already registered GS14 reference, rather than collecting a new bibliography.
The arXiv title/version record and parsed pp. 8-11 and 27-29 were read for analytic norms, the tensor product order, norm-small transport, and the inverse map.
The publisher endpoint timed out on this revisit; the 2014 journal metadata above uses the previously checked sole literature registration.
No local PDF was downloaded or changed.

The local proof independently checked the opposite multiplication (1), antihomomorphism order (4), matrix orientation in (8), absolute derivative bound, Neumann control, and the explicit infinite-rank diagonal in (13).
The scalar pole argument and fixed-pencil estimate are mathematical checks, not numerical experiments.

The next discriminating multivariable test is to identify whether the transport's tensor coefficients preserve a finite-dimensional space containing the actual rational derivative factors, or whether a rationally closed family of bounded realizations can be propagated with quantified spectral margins.
An arbitrary projective tensor map already fails to preserve finite rank, so that step must use additional structure of the actual transport.

No general counterexample or positive theorem for arbitrary analytic transports is claimed.
No formal verification, complete GS14 proof audit, external human review, or priority assessment was performed.
The complete independent Yin_C_F0018 review is linked near the start of this record.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:36 |
| status | proved |
| reason | Select the actual retained finding and its explicit relationship at the unchanged mathematical input and original source boundaries; no new whole-proof review or changed mathematical status is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#1-algebra-norms-and-the-correction-lemma) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact review](../audits/reviews/Yin_R_F0064_v1.md#projective-dual-correction-finding) | Complete projective tensor correction, opposite-product/matrix orientation, analytic transport applicability, infinite-rank obstruction and quantitative/stability/scalar interfaces; no general transported rational boundedness or rank preservation. |


### Decision isolated-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:58 |
| status | proved |
| reason | Adopt the actual context-isolated whole-argument finding after complete comparison with the original review; fixed mathematics, conditional scope and historical decisions retain their original meaning. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#1-algebra-norms-and-the-correction-lemma) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New isolated finding](../audits/reviews/Yin_R_F0064_v1.md#projective-correction) | Complete projective correction, opposite-product and matrix orientation, analytic/source smallness, infinite-rank obstruction and scalar/fixed-pencil boundaries; no general transported rational boundedness. |

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
| argument | [Exact material](#1-algebra-norms-and-the-correction-lemma) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0064_v1.md#projective-dual-correction-finding) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

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

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0064_v1.md#projective-dual-correction-finding).

Material covered by that review: [Exact material](Yin_C_F0018_v1.md).

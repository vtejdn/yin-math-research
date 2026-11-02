---
author: Yin
---

# Finite-Fisher obstructions; bounded Lipschitz conjugates still permit an L2 pole

## Current assessment
[Selected decision](#decision-isolated-review-20261022)

## Regularity Assumptions and the Rational Boundedness Problem

<a id="statement"></a>

<a id="regularity-strategy-evidence"></a>
Date: 2026-09-09.
Provenance: project deduction and targeted primary-source reading by another AI agent.
Authorization: the user requested analytic conditions beyond the completed [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001), especially Haagerup estimates and conjugate-variable regularity.
This note does not reopen Yin_T_F0001 or allocate a successor goal.

<a id="yin_c_f0016"></a>
## Yin_C_F0016: Limits of Fisher and Lipschitz Conjugate Regularity

Initial assessment: complete proof draft awaiting independent review.
Current assessment: [selected assessment](#decision-isolated-review-20261022).
No novelty claim is made.

For a finite bounded selfadjoint tuple $X$ generating a finite faithful tracial von Neumann algebra $M$, write

\[
F_X=\operatorname{Div}_{U(M)}\mathbb C\langle X\rangle,\qquad
\mathcal R_X=\operatorname{Div}_M\mathbb C\langle X\rangle.
\]

The condition $\Phi^*(X)<\infty$, meaning existence of its $L^2$ conjugate system, implies neither

\[
F_X\cap L^2(M)\subseteq M
\quad\text{nor}\quad
F_X\cap M=\mathcal R_X.
\tag{1}
\]

Both failures occur in the selfadjoint sandwich tuple of [Yin_C_F0012](Yin_C_F0012_v1.md#yin_c_f0012), which even has a bounded dual system.
Its conjugates are not asserted to be bounded or Lipschitz.

In addition, a one-variable beta law has a bounded dual and a bounded Lipschitz conjugate variable, but still satisfies $F_h\cap L^2(M_0)\not\subseteq M_0$.
This stronger obstruction concerns the first inclusion in (1); it is not a counterexample to bounded intersection under Lipschitz conjugates.

### Part A. Finite Fisher information

#### 1. Bounded duals give finite Fisher information for selfadjoint tuples

Let $[D_i,X_j]=\delta_{ij}P_\Omega$ with bounded $D_i$ and selfadjoint $X_j$.
Then $[D_i^*,X_j]=-\delta_{ij}P_\Omega$.
Set

\[
K_i=\frac{D_i-D_i^*}{2},\qquad Y_i=-iK_i.
\]

Each $Y_i$ is bounded selfadjoint, $\|Y_i\|\leq\|D_i\|$, and $[X_j,Y_i]=i\delta_{ij}P_\Omega$.
These are exactly the [Voi98-U005, Section 5.10](../audits/literature/Voi98/Yin_U005.md#voi98-u005) conventions.
With $J\widehat a=\widehat{a^*}$, its conjugate formula gives

\[
\xi_i=i(JY_iJ-Y_i)\Omega\in L^2(M),\qquad
\|\xi_i\|_2\leq2\|D_i\|,
\]

and $\tau(\xi_i p(X))=(\tau\otimes\tau)(\partial_i p(X))$ for every polynomial $p$.
The generated-algebra hypothesis places $\xi_i$ in the required space; no condition on $D_i\Omega$ is imposed.
Therefore

\[
\Phi^*(X)=\sum_i\|\xi_i\|_2^2\leq4\sum_i\|D_i\|^2<\infty.
\tag{2}
\]

This is the already reviewed convention conversion in [Dab10-U001](../audits/literature/Dab10/Yin_U001.md#dab10-u001).
Its factoriality theorem is not needed here.
Selfadjointness is used in taking adjoints; the argument is not asserted for an arbitrary normal tuple.

#### 2. Apply it to the existing sandwich tuple

Use exactly Yin_C_F0012: $h(t)=t$ with law $4t^3dt$ on $(0,1)$, a free standard semicircular $b$, and $X=(h,Y)$ with $Y=hbh$.
The source proof supplies $M=W^*(h,Y)$, a faithful normal probability trace, and bounded duals $(E_h,E_Y)$.
Equation (2) gives finite Fisher information for this same specified tuple.

The affiliated inverse $q=h^{-1}$ belongs to $F_X$, and

\[
\|q\|_2^2=\int_0^1t^{-2}4t^3\,dt=2.
\]

Every interval $(0,\varepsilon)$ has positive spectral measure, so $q$ is unbounded.
Thus the first inclusion in (1) fails for this tuple.
Moreover $b=qYq\in F_X\cap M$, while Yin_C_F0012 proves

\[
\operatorname{dist}(b,C^*(h,Y))\geq1,\qquad
\mathcal R_X\subseteq C^*(h,Y).
\]

Hence the second equality in (1) fails as well.
This excludes all bounded scalar rational expressions; failure of the particular expression $qYq$ to use bounded inverses is not the nonmembership argument.

[Yin_C_F0014](Yin_C_F0014_v1.md#yin_c_f0014) supplies a stronger weak-commutator obstruction in the same finite-Fisher tuple: $u=qbq\in F_X\cap L^2(M)$ has no bounded weak commutator representative with $E_Y$.
In particular $u$ is unbounded, since bounded $u$ and $E_Y$ would make its specified weak form the bounded operator $[E_Y,u]$.
This consequence uses Yin_C_F0014's established weak-form convention and proof; no unbounded commutator is treated as an everywhere-defined product.

#### 3. The L2 failure already occurs in one variable

Take $M_0=L^\infty((0,1),4t^3dt)$ and its coordinate $h$.
The density $w(t)=4t^3\mathbf1_{(0,1)}(t)$ is compactly supported and

\[
\int_{\mathbb R}w(t)^3\,dt=\frac{32}{5}<\infty.
\]

The [Voi98-U002, Proposition 3.5](../audits/literature/Voi98/Yin_U002.md#voi98-u002) Hilbert-transform construction therefore supplies an $L^2$ conjugate variable and $\Phi^*(h)<\infty$.
But $h^{-1}\in F_h\cap L^2(M_0)\setminus M_0$, by the same integral above.
This calculation does not use the source's disputed introductory cubic-density normalization for Fisher information.

This is compatible with [Yin_C_F0004](Yin_C_F0004_v1.md#yin_c_f0004), whose tested element is assumed bounded.
It distinguishes an $L^2$-to-bounded theorem from the single-normal bounded rationality criterion.

### Part B. A bounded Lipschitz conjugate still permits an L2 pole

This beta-law test was proposed by the coordinating agent and verified by another AI agent, including its graph-domain and bounded-dual arguments.
Put

\[
w(t)=140t^3(1-t)^3\mathbf1_{(0,1)}(t),\qquad
M_0=L^\infty((0,1),w(t)\,dt),\qquad h(t)=t.
\]

The beta integral gives $\int_0^1 w(t)\,dt=1$ and

\[
\|h^{-1}\|_2^2
=140\int_0^1t(1-t)^3\,dt=7.
\tag{3}
\]

Every interval next to zero has positive measure.
Thus the affiliated inverse $h^{-1}\in F_h\cap L^2(M_0)$ is unbounded.

Since $w\in L^3(\mathbb R)$, the same audited Voi98 scalar interface identifies the conjugate with $\xi=g(h)$, where on $(0,1)$

\[
g(t)=2\left[
 w(t)\log\frac{t}{1-t}
 -\int_0^1\frac{w(y)-w(t)}{y-t}\,dy
\right].
\tag{4}
\]

Here $w$ denotes its polynomial formula when used in the difference quotient on $[0,1]$.
The integral is a polynomial in $t$, because $w(y)-w(t)$ is divisible by $y-t$.
The logarithmic term extends to a $C^1$ function on $[0,1]$: its endpoint singularities are multiplied by third-order zeros.
Consequently $g$ and $g'$ are bounded, so $\xi\in M_0$.

It remains to check the graph-domain requirement in the Lipschitz-conjugate definition, not only the pointwise difference quotient.
Conjugate existence makes the polynomial free difference quotient $\partial$ closable.
Uniformly approximate $g'$ on $[0,1]$ by polynomials $r_n$ and set $p_n(t)=g(0)+\int_0^t r_n(s)\,ds$.
Then $p_n\to g$ and $p_n'\to g'$ uniformly.
The fundamental theorem of calculus gives

\[
\sup_{s,t\in[0,1]}
\left|
\frac{p_n(s)-p_n(t)}{s-t}
-\frac{g(s)-g(t)}{s-t}
\right|
\leq\|p_n'-g'\|_\infty\longrightarrow0,
\]

with continuous diagonal values.
Hence $p_n(h)\to\xi$ in $L^2(M_0)$ and $\partial p_n(h)$ converges in $L^2(M_0\bar\otimes M_0)$ to the bounded function $\Delta g(s,t)=(g(s)-g(t))/(s-t)$.
Thus

\[
\xi\in\operatorname{dom}\overline\partial,\qquad
\overline\partial\xi=\Delta g\in M_0\bar\otimes M_0.
\tag{5}
\]

This is exactly the Lipschitz-conjugate definition inspected in MS23, Section 2.2, p. 7; no stronger differentiability convention is assumed.

There is also a bounded dual.
Let $V:L^2(w\,dt)\to L^2(dt)$ be the unitary $Vf=\sqrt w f$, let

\[
(Tf)(s)=\operatorname{p.v.}\int_0^1\frac{f(t)}{t-s}\,dt,
\qquad
D=V^{-1}M_{\sqrt w}T M_{\sqrt w}V.
\]

The [Tao06 Hilbert-transform interface already used in Yin_C_F0012](Yin_C_F0012_v1.md#yin_c_f0012) gives $\|T\|\leq\pi$, so $\|D\|\leq\pi\|w\|_\infty<\infty$.
On polynomial vectors the commutator kernel cancels the factor $t-s$, giving

\[
([D,h]f)(s)=\int_0^1 f(t)w(t)\,dt=(P_\Omega f)(s).
\]

Polynomial vectors are dense, and both sides are bounded, so $[D,h]=P_\Omega$ on the entire Hilbert space.
Equations (3)-(5) therefore show that even bounded duals plus bounded Lipschitz conjugates do not force $F_h\cap L^2(M_0)\subseteq M_0$.
They do not refute the bounded one-normal theorem Yin_C_F0004.
QED.

### Mathematical Review

On 2026-09-09, another AI agent independently reviewed the complete Yin_C_F0016 statement and Parts A-B, including the inverse moments, conjugate conventions, beta endpoint regularity, graph-closure argument, and bounded dual construction.
The [Yin_C_F0016 proof audit](../audits/reviews/Yin_R_F0064_v1.md#fisher-lipschitz-obstructions-finding) records the checked artifact, dependency interfaces, and verification boundaries.
No corrective mathematical edit was required.
The following prospective source comparisons are separate from the counterexample theorem; this review does not establish their original proofs or a positive rationality theorem.

## Stronger Conditions: What the Inspected Sources Actually Give

The following source statements are prospective inputs to a strategy, not additional parts of Yin_C_F0016.
Original proofs have not been fully audited in this search.

### q-Gaussian regularity

[MS23, arXiv:2203.00547v3](https://arxiv.org/pdf/2203.00547), Theorem 4.6 (p. 17), Corollary 4.7 (pp. 20-21), and Corollary 5.3 (pp. 24-25), gives finite Fisher information, bounded conjugates, and Lipschitz conjugates for finite $q$-Gaussian tuples, $-1<q<1$.
Here Lipschitz means $\xi_i\in\operatorname{dom}\overline\partial_j$ and $\overline\partial_j\xi_i\in M\bar\otimes M$ (p. 7).

Its normalized duals are defined on polynomial vectors and need not be bounded (Definition 2.4, p. 7).
The term "dual system" therefore does not establish the bounded-dual hypothesis used in Yin_T_F0001.

The stated homogeneous estimate (p. 5, citing Bozejko's Proposition 2.1) is

\[
\|W(\eta)\|\leq(m+1)C_{|q|}^{3/2}\|\eta\|_q,\qquad \eta\in H^{\otimes m}.
\]

This is useful analytic input.
Our inference: a rational residual/energy mechanism remains to be proved in the deformed Hilbert norm; tensor words are not an orthonormal coefficient basis when $q\ne0$.
The inspected results supply no rational bounded-intersection theorem.
The cited original Bozejko proof was not inspected.

### Strong Haagerup estimates for holomorphic words

[KS07, arXiv:math/0512481v2](https://arxiv.org/pdf/math/0512481), Definition 1.2 and Theorem 1.3 (pp. 2-3), treats freely independent, identically distributed bounded R-diagonal elements.
For positive-length homogeneous holomorphic polynomials it supplies

\[
\|P_n\|\leq C_a\sqrt n\,\|P_n\|_2.
\]

The degree-zero scalar case is handled separately.
The estimate concerns words without adjoints.
It does not by itself cover arbitrary mixed-star polynomials, rational inverses, or a matrix lift.
Our inference: this is a useful norm estimate once the relevant rational coefficients, residual states, and evaluation interface are independently established.

### Analytic free transport

[GS14, arXiv:1204.2182v3](https://arxiv.org/pdf/1204.2182), Theorem 4.2 and Corollary 4.3 (p. 29), constructs invertible analytic transport near semicircular laws under quantitative analytic smallness conditions.
It identifies the generated C*- and von Neumann algebras; finite Fisher information alone is not its hypothesis.

Our inference: analytic transport need not carry rational expressions to rational expressions in the new listed generators.
An abstract algebra isomorphism, or an analytic power-series change of coordinates, therefore does not automatically transfer $F_X\cap M=\mathcal R_X$.
This route needs rational compatibility or a separate residual and inverse analysis.
The [specified rational coordinate transfers](Yin_C_F0006_v1.md#yin_c_f0006) illustrate the additional kind of compatibility already proved locally.

## Search Record and Stopping Rule

On 2026-09-09 the search followed local Voi98, Dab10, MSY23 and Miy26 interfaces.
Query families were: free Fisher information and $L^3$ densities; $q$-Gaussian conjugate variables and Lipschitz regularity; strong Haagerup estimates for R-diagonal variables; and free monotone transport.
Only primary author/preprint/publisher material is used above.

Parsed online PDFs inspected: MS23 v3, 30 pages, selected pp. 5-7, 17, 20-25; KS07's 27-page arXiv v2, selected pp. 2-3; GS14's 37-page arXiv v3, selected pp. 3-4 and 29.
Bibliographic identities are owned by the [canonical bibliography](../literature/references.bib).
Journal versions were not compared with these preprints.
Direct versioned MS23 PDF/HTML access and the author-hosted KS07 PDF failed; the unversioned arXiv PDF URLs succeeded, with versions checked from their title pages and records.
No PDF was downloaded or retained.

Search stopped after the finite-Fisher obstructions and the exact candidate interfaces were identified.
No full audit, exhaustive literature or novelty search, numerical experiment, formal verification, or theorem for a new positive model class was performed.
The proposed analytic package must still verify residual structure, the appropriate energy decay, the required evaluated inverse, and scalar elimination at its actual hypotheses.


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
| argument | [Exact argument](#part-a-finite-fisher-information) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact review](../audits/reviews/Yin_R_F0064_v1.md#fisher-lipschitz-obstructions-finding) | Entire finite-Fisher two-property obstruction and scalar/beta bounded-Lipschitz-conjugate L2 inverse counterexample, actual graph approximation and bounded dual; prospective source comparisons and stronger bounded-intersection claims are excluded. |


### Decision isolated-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:58 |
| status | proved |
| reason | Adopt the actual context-isolated whole-argument finding after complete comparison with the original review; fixed mathematics, conditional scope and historical decisions retain their original meaning. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#part-a-finite-fisher-information) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New isolated finding](../audits/reviews/Yin_R_F0064_v1.md#regularity-obstructions) | Complete finite-Fisher two-property failures and scalar/beta bounded-Lipschitz-conjugate L2 inverse obstruction, with actual graph approximation, bounded dual and exact source/nonconclusion limits. |

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
| argument | [Exact material](#part-a-finite-fisher-information) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0064_v1.md#fisher-lipschitz-obstructions-finding) | Original selected finding; its actual scope and limits remain in the cited review. |

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

Review: [Exact material](../audits/reviews/Yin_R_F0064_v1.md#fisher-lipschitz-obstructions-finding).

Material covered by that review: [Exact material](Yin_C_F0016_v1.md).

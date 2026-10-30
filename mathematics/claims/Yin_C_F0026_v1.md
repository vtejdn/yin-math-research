---
author: Yin
---

# Bounded starred commutators do not preserve arbitrary denominator domains

## Current assessment
[Selected decision](#decision-finding-owned-review)

## A Small-Core Dual Whose Arbitrary Bounded Fractions Are Not Defined on the Core

<a id="statement"></a>

<a id="small-core-domain-obstruction"></a>
<a id="yin_c_f0026"></a>
## Yin_C_F0026: Arbitrary Bounded Fractions Can Leave a Small Dual Core

Date: 2026-09-10.
Authorization: the user requested a smaller polynomial-core version of the full normal-tuple rationality theorem, after the ACSY24 Proposition 3.5 audit.
Provenance: project counterexample construction by another AI agent, assigned by the coordinating agent.
the coordinating agent allocated Yin_C_F0026 to this exact obstruction.
Initial assessment: complete proof draft and author self-check, awaiting review; the [selected assessment](#decision-candidate-0002) records the mathematical and review assessments.
The construction is inspired by the Cauchy-kernel mechanism in [Yin_C_F0003](Yin_C_F0003_v1.md#yin_c_f0003), but all estimates and domain facts needed here are proved below.
No historical priority, formal verification or human-review claim is made.

## 1. Exact Obstruction and Its Limits

There are a diffuse abelian finite tracial von Neumann algebra $(M,\tau)$, one bounded normal generator $X$, and a complex-linear operator $D_0$ with domain exactly

\[
\mathcal A=\mathbb C[X,X^*]\Omega\subset H=L^2(M,\tau)
\]

such that:

1. $\mathcal A$ is dense, $D_0$ is closable, $\mathcal A\subseteq\operatorname{Dom}D_0^*$, and $D_0\Omega=0$.
2. On $\mathcal A$, $[D_0,X]=P_\Omega$, while $[D_0,X^*]$ has an everywhere bounded extension.
3. The affiliated rational element $u=X^{-1}$ has polynomial bounded fractions $u=s^{-1}a=bt^{-1}$ whose cleared defect $sD_0b-aD_0t$ is defined on all of $\mathcal A$ and equals $-P_\Omega$ there.
4. The same $u$ has its usual positive canonical bounded fractions, with coefficients $s,a,b,t\in M$ and regular $s,t$, for which the literal defect
   \[
   z\longmapsto s\overline{D_0}(bz)-a\overline{D_0}(tz)
   \tag{1}
   \]
   is not defined at $z=\Omega$.

Consequently these small-core hypotheses with merely bounded adjoint-generator commutators do not justify defining arbitrary bounded-fraction defects on the entire starred polynomial core.
They also do not imply $M\Omega\subseteq\operatorname{Dom}\overline{D_0}$.
Thus the literal domain and arbitrary-fraction formulation of [Yin_C_F0024](Yin_C_F0024_v1.md#yin_c_f0024) cannot be copied with $M$ replaced by $\mathcal A$ on the basis of those hypotheses alone.

The added adjoint-generator commutator in this example is noncompact, so the example does **not** satisfy the Hilbert-Schmidt commutator hypothesis furnished by the derivations in [ACSY24-U001](../audits/literature/ACSY24/Yin_U001_v1.md#acsy24-u001).
It does not refute a rationality criterion restricted to suitable common domains, a condition asserting existence of compatible fractions, or a separately defined closure or distributional regularization of the combined defect.
Its conclusion concerns the stated literal compositions at the displayed test vector.

## 2. The Probability Space and a Bounded Cauchy Dual

Let $\mathbb D=\{z\in\mathbb C:|z|<1\}$, write $dA$ for ordinary planar Lebesgue measure, and set

\[
d\mu(z)=w(z)\,dA(z),\qquad
w(z)=\frac4\pi(1-|z|^2)^3.
\tag{2}
\]

Polar integration gives

\[
\int_{\mathbb D}d\mu
=8\int_0^1r(1-r^2)^3\,dr=1.
\]

Take $M=L^\infty(\mathbb D,\mu)$ with its integral trace, $H=L^2(\mathbb D,\mu)$, $\Omega=1$, and $X(z)=z$.
This is a finite von Neumann algebra with faithful normal probability trace.
The coordinate $X$ is bounded normal and generates $M$ as a von Neumann algebra; $X^*(z)=\bar z$.
The starred polynomial algebra $\mathcal A=\mathbb C[z,\bar z]$ is dense in $H$, for example by Stone-Weierstrass on the closed disk followed by density of continuous functions in $L^2(\mu)$.
No atom occurs at zero or elsewhere.

For initially bounded $f$, define

\[
(Kf)(x)=\int_{\mathbb D}\frac{f(y)}{y-x}\,d\mu(y).
\tag{3}
\]

This requires no principal value for bounded $f$: the absolute kernel is integrable in each variable.
Indeed, since $w\leq4/\pi$ and $\mathbb D-x\subseteq\{v:|v|<2\}$ for $x\in\mathbb D$,

\[
\sup_{x\in\mathbb D}\int_{\mathbb D}\frac{d\mu(y)}{|y-x|}
\leq\frac4\pi\int_{|v|<2}\frac{dA(v)}{|v|}=16.
\tag{4}
\]

The same bound holds with $x$ and $y$ interchanged.
The elementary Schur estimate therefore gives a bounded extension $K\in B(H)$ with $\|K\|\leq16$.
Explicitly, Cauchy-Schwarz against the measure $|y-x|^{-1}d\mu(y)$ gives

\[
|Kf(x)|^2
\leq16\int_{\mathbb D}\frac{|f(y)|^2}{|y-x|}\,d\mu(y).
\]

Integrating in $x$, applying the other bound in (4), and then using density proves $\|Kf\|_2\leq16\|f\|_2$.
The diagonal $x=y$ has product measure zero, so canceling the factor $y-x$ gives

\[
[K,X]=P_\Omega.
\tag{5}
\]

Also

\[
([K,X^*]f)(x)
=\int_{\mathbb D}\frac{\bar y-\bar x}{y-x}f(y)\,d\mu(y).
\tag{6}
\]

The kernel in (6) has absolute value one off the diagonal.
Thus $[K,X^*]$ is Hilbert-Schmidt, with Hilbert-Schmidt norm one.

Let $k=K\Omega$.
Equation (4) implies $k\in M$ and $\|k\|\leq16$.
Write $M_k$ for multiplication by $k$ and put

\[
G=K-M_k.
\tag{7}
\]

Since $M$ is abelian, $M_k$ commutes with $X$ and $X^*$.
Therefore $G$ is bounded, $G\Omega=0$, $[G,X]=P_\Omega$, and $[G,X^*]=[K,X^*]$.
This bounded normalization will leave every subsequent domain obstruction unchanged.

## 3. The Additional Cauchy-Riemann Operator

Write $z=x+iy$ and use the Wirtinger conventions

\[
\partial_{\bar z}=\tfrac12(\partial_x+i\partial_y),\qquad
\partial_z=\tfrac12(\partial_x-i\partial_y).
\]

Define

\[
E p=\partial_{\bar z}p,\qquad\operatorname{Dom}E=\mathcal A.
\tag{8}
\]

Use the inner product linear in its second variable.
For $a,p\in\mathcal A$, ordinary integration by parts gives

\[
\begin{aligned}
\langle Ea,p\rangle
&=\int_{\mathbb D}(\partial_z\bar a)\,p\,w\,dA\\
&=-\int_{\mathbb D}\bar a\,\partial_z(pw)\,dA\\
&=\left\langle a,-\partial_zp+
                  \frac{3\bar z}{1-|z|^2}p\right\rangle.
\end{aligned}
\tag{9}
\]

There is no boundary contribution: $p,a$ and their derivatives are bounded on the closed disk, and $w$ vanishes on the boundary with a third-order zero.
One may also integrate over disks of radius $R<1$ and let $R$ tend to one; their boundary integrals are bounded by a constant times $(1-R^2)^3$ and tend to zero.
The identity $\partial_z w=-3\bar z\,w/(1-|z|^2)$ gives the last line.

The last vector in (9) belongs to $H$.
In fact

\[
\left\|\frac{3\bar z}{1-|z|^2}\right\|_2^2
=72\int_0^1r^3(1-r^2)\,dr=6<\infty,
\tag{10}
\]

and $p,\partial_zp$ are bounded.
Thus

\[
\mathcal A\subseteq\operatorname{Dom}E^*,\qquad
E^*p=-\partial_zp+\frac{3\bar z}{1-|z|^2}p.
\tag{11}
\]

The adjoint domain is dense, so $E$ is closable.
On the same invariant polynomial core,

\[
E\Omega=0,\qquad [E,X]=0,\qquad [E,X^*]=I.
\tag{12}
\]

Now set

\[
D_0=G+E,\qquad\operatorname{Dom}D_0=\mathcal A.
\tag{13}
\]

Bounded perturbation gives

\[
\overline{D_0}=G+\overline E,
\qquad
\operatorname{Dom}\overline{D_0}=\operatorname{Dom}\overline E.
\tag{14}
\]

To verify the domain equality directly, for $p_n\in\mathcal A$ converging in $H$, convergence of $D_0p_n$ is equivalent to convergence of $Ep_n$, because $Gp_n$ converges.
The two graph closures therefore differ exactly by the bounded term $G$.
Also $D_0^*p=G^*p+E^*p$ for $p\in\mathcal A$, so the required polynomial adjoint domain is retained.

Equations (5), (7) and (12) give

\[
D_0\Omega=0,\qquad
[D_0,X]=P_\Omega,
\qquad
[D_0,X^*]=[K,X^*]+I
\quad\text{on }\mathcal A.
\tag{15}
\]

Both commutators have bounded extensions to $H$.
Graph approximation also shows that $X$ and $X^*$ preserve $\operatorname{Dom}\overline{D_0}$ and that the same bounded commutator identities hold on that full closed domain.
For example, if $p_n\to v$ and $D_0p_n\to\overline{D_0}v$, then $D_0(Xp_n)=X D_0p_n+Pp_n$ converges; closedness supplies the claim for $X$.
The $X^*$ calculation uses the other bounded commutator in (15).

Since $H$ is infinite dimensional, $I$ is noncompact.
Equation (6) is compact, so $[K,X^*]+I$ is noncompact, and in particular is not Hilbert-Schmidt.
This exact feature separates the example from the stronger commutator hypotheses supplied by ACSY24's derivations.

## 4. One Rational Element and Two Bounded Fraction Choices

Let $U=U(M)$ denote the affiliated algebra.
The coordinate $X=z$ is regular because its zero set has measure zero; its affiliated inverse is multiplication by $1/z$.
Thus

\[
u=X^{-1}\in\operatorname{Div}_{U}\mathbb C[X].
\tag{16}
\]

First take

\[
s_0=t_0=X,\qquad a_0=b_0=1.
\]

These are bounded valid left and right fractions $u=s_0^{-1}a_0=b_0t_0^{-1}$, with regular denominators.
Their literal defect is defined on all of $\mathcal A$ and, by (15), equals

\[
s_0D_0(b_0p)-a_0D_0(t_0p)
=X D_0p-D_0(Xp)=-Pp.
\tag{17}
\]

For the second choice write $z=re^{i\theta}$ away from zero and set

\[
s=t=\frac r{\sqrt{1+r^2}},\qquad
a=b=\frac{e^{-i\theta}}{\sqrt{1+r^2}}.
\tag{18}
\]

The value assigned at zero is immaterial.
All four coefficients are bounded measurable functions; $s,t$ are positive and regular.
Pointwise off zero,

\[
s^{-1}a=bt^{-1}=\frac{e^{-i\theta}}r=\frac1z.
\tag{19}
\]

They are precisely the positive bounded-transform fractions:

\[
s=(1+uu^*)^{-1/2},\quad a=su,\qquad
t=(1+u^*u)^{-1/2},\quad b=ut.
\tag{20}
\]

The following section proves $b\notin\operatorname{Dom}\overline{D_0}$.
Consequently (1) is not defined at the polynomial test vector $\Omega=1$, since its first term requires $\overline{D_0}(b\Omega)$.
This suffices to contradict the proposed blanket well-definedness on $\mathcal A$ for every bounded fraction choice; no assertion about the second term's domain is needed.

## 5. The Bounded Numerator Fails the Closed Domain

Suppose, toward a contradiction, that $b\in\operatorname{Dom}\overline E$.
Then there are polynomials $p_n\in\mathcal A$ and an $h\in H$ such that

\[
p_n\longrightarrow b\text{ in }L^2(\mu),\qquad
\partial_{\bar z}p_n\longrightarrow h\text{ in }L^2(\mu).
\tag{21}
\]

On every disk $|z|<R<1$, the weight in (2) is bounded above and bounded below by positive constants.
Thus both convergences in (21) hold locally in ordinary Lebesgue $L^2$.
Testing against compactly supported smooth functions and passing to the limit in the distributional derivative identity gives

\[
\partial_{\bar z}b=h\quad\text{as distributions on }\mathbb D.
\tag{22}
\]

On the punctured disk $b$ is smooth.
Put $g(r)=(1+r^2)^{-1/2}$, so $b=e^{-i\theta}g(r)$.
Using $\partial_{\bar z}=\tfrac12e^{i\theta}(\partial_r+(i/r)\partial_\theta)$, one obtains there

\[
\partial_{\bar z}b
=\frac12\left(g'(r)+\frac{g(r)}r\right)
=\frac1{2r(1+r^2)^{3/2}}.
\tag{23}
\]

Equation (22) forces $h$ to agree almost everywhere with (23) on every annulus compactly contained in the punctured disk.
But its squared $L^2(\mu)$ norm near zero is infinite:

\[
\int_{0<|z|<1/2}
\left|\frac1{2r(1+r^2)^{3/2}}\right|^2d\mu(z)
=2\int_0^{1/2}\frac{(1-r^2)^3}{(1+r^2)^3}\,\frac{dr}{r}
=\infty.
\tag{24}
\]

The ratio multiplying $dr/r$ has a positive lower bound on $[0,1/2]$.
This contradicts $h\in H$.
The argument needs no assertion about a possible distribution supported at zero: equality on the punctured annuli already forces the divergent norm.
Thus $b\notin\operatorname{Dom}\overline E$, and (14) gives

\[
b\notin\operatorname{Dom}\overline{D_0}.
\tag{25}
\]

This proves all four assertions in Section 1.

## 6. What Must Be Kept Separate

The example has a genuine densely defined normalized dual and dense adjoint domain, not just a formal algebraic operator without an adjoint.
Its closed domain is invariant under both the normal generator and its adjoint.
The failure appears when arbitrary bounded fraction coefficients are inserted: generator invariance does not imply invariance under every bounded Borel function or membership of all such coefficient vectors in the domain.

For $u=X^{-1}$ the compatible polynomial fractions in (17) already give a finite-rank defect.
The example therefore does not contradict the existential statement restricted to compatible fractions.
It also does not establish that no densely defined or distributionally regularized defect can be assigned to (18).
Multiplying a distributional derivative by its vanishing bounded denominator, or closing a combined expression after cancellation, changes the definition and needs a separate argument.
Neither operation makes the literal $\overline{D_0}(b\Omega)$ in (1) defined.

The [ACSY24 audit](../audits/literature/ACSY24/Yin_U001_v1.md#acsy24-u001) distinguishes the weaker bounded-commutator regularization used for maximal Delta from the Hilbert-Schmidt commutators supplied by its derivation hypotheses.
The present counterexample fits the former operator hypotheses and fails the latter by (15).
No counterexample to the actual ACSY24 derivation hypothesis or to a carefully reformulated full rationality theorem is claimed here.

## 7. Checks and Review Boundary

The proof directly checks normalization of the measure, both Schur bounds, the exact dual sign, the Hilbert-Schmidt Cauchy commutator, the weighted adjoint and boundary term, bounded perturbation of the graph closure, both fraction identities, and the local distributional obstruction.
It uses ordinary integration by parts, distributional derivatives, elementary Hilbert-space adjoints, and the affiliated inverse of a nonzero almost-everywhere multiplication function.
No whole-paper source theorem is required for the construction.
No numerical experiment, proof-assistant verification, external human review, or historical-priority search has been performed.
the coordinating agent was asked to review this written artifact independently before any claim assessment is promoted or shared index is updated.


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
| argument | [Exact material](#2-the-probability-space-and-a-bounded-cauchy-dual) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0015_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:41 |
| status | proved |
| reason | Select the actual retained findings and their individual checking relationships, with unchanged mathematical status, statement and argument. Original findings, dates, accepted-source depths and historical decisions remain intact; this is no new mathematical review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#2-the-probability-space-and-a-bounded-cauchy-dual) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Retained finding](../audits/reviews/Yin_R_F0015_v1.md#small-core-fraction-obstruction-finding) | Whole four-assertion weighted-disk construction, constants, actual closed and adjoint domains, compatible and canonical bounded fractions, distributional failure and exact distinction from compact/Hilbert--Schmidt hypotheses. |

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

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0015_v1.md).

Material covered by that review: [Exact material](Yin_C_F0026_v1.md).

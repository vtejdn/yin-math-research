---
author: Yin
---

# Actual finite dual states; one-q-variable bounded reconstruction and multivariable comparison obstruction

## Current assessment
[Selected decision](#decision-isolated-current-review-20261022)

## Finite actual-dual state spaces and a one-variable model

<a id="statement"></a>
<a id="yin_c_f0108"></a>

Date/author: 2026-09-11, another AI agent.
Record kind: substantive continuation of [Yin_T_F0006](../tasks/Yin_T_F0006_v1.md).
Assessment: complete candidate deductions and a specific obstruction, author checked; independent review pending.
No Claim ID or Role assigned.

The actual normalized duals preserve finite-dimensional state spaces of rational L2 inverse pencils.
In one variable, their finite invariant spaces can be analyzed completely: a bounded change of Hilbert coordinates conjugates the dual to an entire function of the usual backward shift.
Every finite-dimensional invariant space consequently consists of bounded rational functions, with exponentially decaying actual q-particle energy.
The direct extension of this particular change of polynomial coordinates to d>=2 is impossible: even a one-sided uniform L2 comparison with a semicircular tuple would force identical joint tracial laws.

Current assessment, 2026-09-11: registered as ordinary **Yin_C_F0108** after [complete independent mathematical review](../audits/reviews/Yin_R_F0118_v1.md#5-source-and-review-limits).
The actual inverse-pencil state identity, one-variable entire-symbol model and bounded scalar reconstruction, actual particle decay and full-polynomial multivariable substitution obstruction are proved.
This supersedes the initial pending labels.
Rad92 supplies source context only, with the independent retrieval limitation recorded in the review.
Multivariable finite invariant-space boundedness and Q5/Q6 remain unresolved.
No Role or lemma extraction is assigned.

## 1. Inputs and a finite state identity

The principal input is [the independently reviewed actual rational L2 interface](Yin_C_F0107_v1.md), initially reviewed; see [its audit](../audits/reviews/Yin_R_F0117_v1.md#original-f0060-account).
Its hypotheses hold for finite canonical q-Gaussian tuples by [Yin_C_F0023](Yin_C_F0023_v1.md#yin_c_f0023).
Further local sources read before the calculations were [MS23-U006](../audits/literature/MS23/Yin_U006.md#ms23-u006), [the scalar density comparison in Yin_C_F0020](Yin_C_F0020_v1.md), [Miy22-U002's rational-series decay argument](../audits/literature/Miy22/Yin_U002.md#miy22-u002), and [the semicircular Fock foundation](../audits/literature/Miy22/Yin_U001.md).

Primary searches for q-dual spectral models and free Appell coordinates did not supply the particular invariant-space result below.
Classical q-Appell/Jackson derivatives found in those searches are different operators and are not used.
The Chebyshev moments consumed below are exactly the source-checked finite q-Hermite connection in MS23-U006, Equation (6), not its optional general conjugate formula.

Let
\[
B(X)=A_0-\sum_{i=1}^d A_iX_i,\quad
Y=B(X)^{-1}\in M_n(L^2(M,\tau)),\quad
G=(\tau(Y_{ab}))_{a,b=1}^n.
\]
Suppose B is full and the L2 premise is obtained, for instance, from the preceding minimal-representation bootstrap.
Its entries lie in the embedded free field.
The exact rational derivative and normalized vacuum identities give
\[
\partial_iY_{ab}
=\sum_{j,k}Y_{aj}(A_i)_{jk}\otimes Y_{kb},\qquad
\boxed{\ D_iY=YA_iG.\ }
\tag{1}
\]
The contraction by \(\tau\) is valid on every L2 factor.
It is not evaluation of a formal Taylor series.

For each fixed row a, the finite-dimensional actual Hilbert subspace
\[
V_a=\operatorname{span}_{\mathbb C}\{Y_{a1}\Omega,\ldots,Y_{an}\Omega\}
\]
is invariant under every D_i.
Any row compression \(uY\) likewise has an invariant span.
If its entries are independent, their coordinate matrix for \(D_i|_V\) is \(A_iG\).
Dependence merely passes this matrix action to the corresponding quotient.
No whole-inverse boundedness follows from (1).

A sufficient route to Q5 is thus to prove that finite-dimensional common invariant spaces of the normalized q-duals consist of bounded vectors.
One may also seek the weaker assertion restricted to the inverse-pencil spaces in (1).
The first assertion is proved below for d=1, but is left open for d>=2.

## 2. One q-Gaussian: an exact entire function of the backward shift

Fix real -1<q<1 and one variance-one q-Gaussian X.
Put
\[
a=\sqrt{1-q}\,X,\qquad \nu_q=\text{law of }a.
\]
The support is [-2,2].
Let \(\nu_0\) be the variance-one semicircle law on that interval, and let U_n be its orthonormal monic Chebyshev polynomials:
\[
U_0=1,\quad U_1=t,\quad U_{n+1}=tU_n-U_{n-1}.
\]
Yin_C_F0020's q-density product bounds give constants \(0<c_q\le C_q<\infty\) such that
\[
c_q\,d\nu_0\le d\nu_q\le C_q\,d\nu_0.
\tag{2}
\]
Define \(T:\ell^2(\mathbb N_0)\to L^2(\nu_q)\) on the standard orthonormal basis \(\epsilon_n\) by \(T\epsilon_n=U_n(a)\).
These \(\epsilon_n\) are not the raw q-Fock words.
Polynomial density and (2) show that T is bounded and onto with bounded inverse, with \(\|T\|\le\sqrt{C_q}\), \(\|T^{-1}\|\le c_q^{-1/2}\).

Let \(S^*\epsilon_0=0\) and \(S^*\epsilon_n=\epsilon_{n-1}\) for n>=1.
The elementary divided-difference identity, proved from the displayed three-term recurrence, is
\[
\frac{U_n(t)-U_n(s)}{t-s}
=\sum_{k=0}^{n-1}U_k(t)U_{n-1-k}(s).
\tag{3}
\]
The diagonal value is understood polynomially.
By the finite q-Hermite connection in MS23-U006, taking its vacuum coefficient gives
\[
\int U_{2m}\,d\nu_q=(-1)^m q^{m(m+1)/2},\qquad
\int U_{2m+1}\,d\nu_q=0.
\tag{4}
\]
For the normalized dual D of X, \([D,a]=\sqrt{1-q}P\) and D1=0.
Thus (3) and (4) imply on each polynomial
\[
D\,U_n(a)
=\sqrt{1-q}\sum_{\substack{m\ge0\\2m+1\le n}}
(-1)^m q^{m(m+1)/2}U_{n-2m-1}(a).
\tag{5}
\]
In particular, this is not the q-Hermite deletion formula; it is the action in the specified Chebyshev coordinates.

The function
\[
\phi_q(z)=\sqrt{1-q}\sum_{m\ge0}
(-1)^m q^{m(m+1)/2}z^{2m+1}
\tag{6}
\]
is entire and nonconstant, with \(\phi_q'(0)=\sqrt{1-q}>0\).
At q=0 it equals z.
For negative q the same formula and convergence apply, since absolute convergence is controlled by |q|.
Its series at the contraction S* converges absolutely in operator norm.
Equation (5), density, and boundedness therefore prove the exact identity
\[
\boxed{\ T^{-1}DT=\phi_q(S^*).\ }
\tag{7}
\]
This proof also gives the explicit bound
\[
\|D\|\le\sqrt{C_q/c_q}\,\sqrt{1-q}
\sum_{m\ge0}|q|^{m(m+1)/2}.
\]
It is a one-variable model, not a replacement for Yin_C_F0023's multivariable construction.

## 3. Every finite D-invariant space has bounded rational vectors

Let E be a finite-dimensional D-invariant subspace of \(L^2(\nu_q)\).
Choose a nonzero scalar polynomial p annihilating \(D|_E\), for example its characteristic polynomial.
For every \(f\in E\), put \(\eta=T^{-1}f\).
Equation (7) gives
\[
p(\phi_q(S^*))\eta=0.
\tag{8}
\]
The entire function \(b(z)=p(\phi_q(z))\) is not identically zero: the nonconstant entire function \(\phi_q\) cannot take values in the finite root set of p.

There are only finitely many zeros of b in the closed unit disk.
Form the polynomial P from precisely these zeros with their multiplicities.
Then \(h=b/P\) is analytic and nonzero on a neighborhood of the closed disk.
Both \(h(S^*)\) and \(h(S^*)^{-1}=(1/h)(S^*)\) are defined by norm-convergent power series on some disk of radius greater than one.
They commute with \(P(S^*)\), so
\[
\ker b(S^*)=\ker P(S^*).
\tag{9}
\]
If P is constant this kernel is zero.
Otherwise writing \(\eta=\sum_{n\ge0}\alpha_n\epsilon_n\), (9) is a finite constant-coefficient recurrence for \((\alpha_n)\).
Its ordinary generating function is rational.
Since \(\eta\in\ell^2\), the audited rational-series argument in Miy22-U002 excludes poles on or inside the unit circle after cancellation.
Consequently there exist \(C<\infty\) and \(r<1\), depending on \(\eta\), such that
\[
|\alpha_n|\le Cr^n.
\tag{10}
\]
This step includes roots of P on the unit circle: they do not produce nonzero square-summable contributions.
A zero root can give finitely supported sequences and causes no difficulty.

Now \(\sup_{[-2,2]}|U_n|\le n+1\), as follows from the usual sine formula or its continuous endpoint limit.
Therefore
\[
f=\sum_{n\ge0}\alpha_nU_n(a)
\]
converges in operator norm as well as in L2, identifying f with a bounded element.
It is also scalar rational.
Indeed a rational generating function with no poles in the closed unit disk has coefficients equal to a finite sum of finitely supported sequences and polynomial multiples of \(\lambda^n\), with \(|\lambda|<1\).
The identity
\[
\sum_{n\ge0}\lambda^nU_n(a)
=(1-\lambda a+\lambda^2)^{-1}
\tag{11}
\]
holds in operator norm for \(|\lambda|<1\).
Its denominator has no zero on [-2,2], and differentiating in \(\lambda\) gives the polynomial multiples of n.
Hence each finite contribution is an expression in a with bounded scalar inverses.
We obtain
\[
\boxed{\quad
E\subseteq\operatorname{Div}_{M}\mathbb C[X].
\quad}
\tag{12}
\]
This conclusion concerns every finite invariant space, even when rational membership was not assumed.

There is also an actual q-particle estimate.
The polynomial \(\sum_{k=0}^{N}\alpha_kU_k(a)\) has degree at most N and its operator-norm error is bounded by \(C\sum_{k>N}(k+1)r^k\).
For any \(r<r'<1\), this is at most \(C'(r')^N\).
Let \(Q_m^{(q)}\) denote the orthogonal projection to the m-particle q-Fock space.
Orthogonal projection and the best-approximation inequality give
\[
\left\|\sum_{m>N}Q_m^{(q)}f\right\|_2
\le C'(r')^N.
\tag{13}
\]
Thus the homogeneous q-energy decays exponentially.
No degree-independent equivalence between raw q coefficients and ordinary coefficients is used.

## 4. Why the direct polynomial-coordinate transfer fails for d>=2

For d=2,q=1/2, and more generally d>=2 and q!=0, the direct multivariable version of the bounded map T cannot exist.
The precise obstruction is stronger than a failed estimate for a particular family of words.

Let \(S_1,\ldots,S_d\) be variance-one free semicirculars with trace \(\tau_0\), and let \(X_1,\ldots,X_d\) be variance-one q-Gaussians with trace \(\tau_q\).
Fix any scalar \(c>0\).
There is no constant K such that
\[
\|p(cX_1,\ldots,cX_d)\|_{2,q}
\le K\|p(S_1,\ldots,S_d)\|_{2,0}
\quad\text{for every noncommutative polynomial }p.
\tag{14}
\]
In particular the polynomial substitution map sending free Wick polynomials at S to their evaluations at \(cX\) has no bounded extension.
Choosing \(c=\sqrt{1-q}\) includes the natural coordinate scaling from Section 2.

To prove this, suppose (14) holds.
The linear functional
\[
p(S)\longmapsto\tau_q(p(cX))
\]
is bounded for the semicircular L2 norm, since its absolute value is at most the left side of (14).
Riesz representation gives \(\eta\in L^2(M_0,\tau_0)\) with
\[
\tau_q(p(cX))=\langle\eta,p(S)\rangle.
\]
Traciality implies
\[
\langle\eta,S_i p(S)-p(S)S_i\rangle=0
\quad\text{for all }p,i.
\]
Since left and right multiplication by S_i are bounded selfadjoint operators, polynomial density gives \(S_i\eta=\eta S_i\).

For completeness, the standard central-vector fact needed here has a direct free-group proof.
In each diffuse semicircular coordinate algebra choose the Haar unitary obtained by applying the semicircle distribution function and then \(t\mapsto e^{2\pi it}\).
This Borel change generates the same abelian von Neumann algebra up to null sets.
The resulting unitaries are free.
Reduced group words in them form an orthonormal basis of the generated L2 space, identifying it with \(\ell^2(\mathbb F_d)\).
Commutation of \(\eta\) with S_i implies commutation with these unitaries: the equality first extends by functional calculus, since left and right actions commute.
In group coordinates, a central vector has coefficients constant on conjugacy classes.
Every nonidentity conjugacy class of \(\mathbb F_d\), d>=2, is infinite, so square summability forces every nonidentity coefficient to vanish.
Thus \(\eta\in\mathbb C\Omega\).
The unit value makes \(\eta=\Omega\).

It follows that \(\tau_q(p(cX))=\tau_0(p(S))\) for every p.
The second moment gives \(c^2=1\), hence c=1.
The fourth one-coordinate moment is \(2+q\) for X and 2 for S, giving q=0, the desired contradiction.
The moment \(2+q\) follows directly from the three q-pairings of four letters.
This proves (14) is impossible.

This is the familiar free-group central-vector argument at its required scope; primary source context was checked in F. Rădulescu, *The fundamental group of the von Neumann algebra of a free group with infinitely many generators is \(\mathbb R_+\setminus\{0\}\)*, JAMS 5 (1992), [p. 521](https://art.torvergata.it/bitstream/2108/100647/2/fundamentalS0894-0347-1992-1142260-1.pdf).
The proof above supplies the finite d form directly rather than importing an infinite-generator theorem.

The obstruction does not refute boundedness of finite actual-D invariant spaces.
It excludes only a uniform substitution map on the entire polynomial L2 space.
State-dependent control on the finite spaces in (1) could still exist.
Establishing that control for d=2,q=1/2 is the remaining concrete test; one cannot transfer Section 3 by silently treating multivariable free Wick coordinates as a uniformly equivalent q-Hilbert basis.

## 5. Scope of this continuation

Equations (1) and (7)–(13) are complete candidate proofs.
Equation (14) has a complete obstruction proof and explains why the successful one-variable model does not directly extend.
The current file introduces no unbounded rational L2 example, no all-q multivariable boundedness assertion, and no solution of the iterated holomorphic-kernel totality problem.
The earlier frozen rational-interface proof remains unchanged.


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
| argument | [Exact material](#2-one-q-gaussian-an-exact-entire-function-of-the-backward-shift) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0118_v1.md#5-source-and-review-limits) | Whole five-section actual inverse-state identity, exact one-variable entire backward-shift similarity, finite-invariant-space bounded scalar reconstruction and actual particle decay, plus the full-polynomial multivariable law-comparison obstruction. The Rad92 primary-PDF retrieval limit and open multivariable invariant-space problem remain explicit. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the separate isolated current finding on the unchanged fixed statement and proof, with exact conditions and scope. Preserve historical findings, relationships, source depths and dates; no new mathematical proof version is introduced. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-one-q-gaussian-an-exact-entire-function-of-the-backward-shift) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0118_v1.md#current-isolated-finding) | Whole five-section actual inverse-state identity, exact one-variable entire backward-shift similarity, finite-invariant-space bounded scalar reconstruction and actual particle decay, plus the full-polynomial multivariable law-comparison obstruction. The Rad92 primary-PDF retrieval limit and open multivariable invariant-space problem remain explicit. |

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
| argument | [Exact material](#2-one-q-gaussian-an-exact-entire-function-of-the-backward-shift) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0118_v1.md#5-source-and-review-limits) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0118_v1.md#5-source-and-review-limits).

Material covered by that review: [Exact material](Yin_C_F0108_v1.md).

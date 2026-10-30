---
author: Yin
---

<a id="miy26-u001"></a>
# Miy26-U001: Fock and Affiliated-Operator Interfaces

- Source: [Miy26](../../../literature/pdf/Miy26.pdf), the user-supplied arXiv:2603.19528v2 artifact dated 2026-04-21; fingerprint and acquisition facts in the [literature registry](../../../literature/readme.md).
- Locator: Section 2, pp. 4-6, Theorem 2.1; Theorem 1.1, p. 1.
  Printed and PDF page numbers agree.
- Record: 2026-09-08, the coordinating agent, source reading and local interface reconstruction for [Miy26 spectral source audit](readme.md#miy26-spectral-source-audit).
- Kind and coverage: definitions and reused source interfaces, audited at the finite-system scope below.
  Imported general affiliated-operator theory and free-field results have their actual verification depth recorded in U004.

## Setting and hypotheses

Fix a finite integer $d\geq1$, $H=\mathbb C^d$, and full Fock space

$$
\mathcal F(H)=\bigoplus_{n\geq0}H^{\otimes n},\qquad H^{\otimes0}=\mathbb C\Omega.
$$

For the standard orthonormal basis, left creation $\ell_i$ prepends $e_i$ and right creation $r_i$ appends it.
Their adjoints remove a matching first or last letter and annihilate the vacuum.
Put $s_i=\ell_i+\ell_i^*$, and

$$
\mathcal P=\mathbb C\langle s_1,\ldots,s_d\rangle,
\quad A=C^*(s_1,\ldots,s_d),\quad M=W^*(s_1,\ldots,s_d).
$$

The faithful normal trace is $\tau(x)=\langle x\Omega,\Omega\rangle$; the $s_i$ are variance-one free semicircular operators.
We use $\|f\|_2^2=\tau(f^*f)$ and the unitary identification $L^2(M,\tau)\simeq\mathcal F(H)$.
The left/right multiplication conventions and the word basis are those already audited in [Miy22-U001](../Miy22/Yin_U001_v1.md#miy22-u001).

For words $w=w_1\cdots w_n\in[d]^*$, $e_w=e_{w_1}\otimes\cdots\otimes e_{w_n}$ and $U_w\in\mathcal P$ is the Wick/Chebyshev polynomial satisfying $U_w\Omega=e_w$.
The empty word has $U_\varnothing=1$ and $e_\varnothing=\Omega$.
Reversal $w^{\rm rev}=w_n\cdots w_1$ satisfies $U_w^*=U_{w^{\rm rev}}$.
Word-polynomial substitution is linear, not multiplicative: $U_i^2=U_{ii}+1$.

**Source scope correction.**
The p. 5 assertion that $M$ is a $\mathrm{II}_1$ factor cannot hold for $d=1$, when $M=W^*(s_1)$ is abelian.
The proofs use a finite tracial von Neumann algebra with faithful trace, not factoriality; the main theorem includes the one-generator case unchanged.
For $d\geq2$ the familiar factor identification is a separate foundational fact, unnecessary here.

## Three ambient spaces and two closures

Let $L^0(M,\tau)$ denote the algebra of closed densely defined affiliated operators.
In a finite tracial algebra these are measurable operators; sums and products mean their closed affiliated-algebra realizations, not arbitrary compositions of everywhere-defined maps.

- $C_{\rm div}(s)$ is the scalar division closure of $\mathcal P$ in $M$: invert only elements whose inverses exist in $M$.
- $D(s)$ is the scalar division closure of $\mathcal P$ in $L^0(M,\tau)$: invert elements invertible in that larger algebra.

These are definitions of inverse closure; being a skew field is an additional theorem, not part of either definition.
$D(s)$ is star closed: the adjoint of a finite inverse expression is again an inverse expression, using $(x^{-1})^*=(x^*)^{-1}$.
The precise imported assertion that every nonzero element of $D(s)$ has an affiliated inverse is recorded in [Miy26-U004](Yin_U004_v1.md#miy26-u004).
It is needed for the general resolvent statement in U003.
The local regularization step of U002 only uses inverses known to exist by positivity, so it does not independently need the full free-field theorem.

For $f\in L^2(M,\tau)$, its affiliated realization $L_f$ is the closure of left multiplication on the bounded-vector domain $M\subset L^2(M,\tau)$.
On that domain,

$$
L_f(\widehat b)=f b=R_b f,\qquad b\in M,
\qquad \|fb\|_2\leq\|b\|\,\|f\|_2.
$$

Here $\widehat b=b\Omega$ and $R_b$ is bounded right multiplication.
Thus $\mathcal F_{\rm alg}(H)=\mathcal P\Omega$ lies in the domain of every $L^2$ affiliated operator.
This does not make $L_f$ bounded on all of Fock space.
Miy26 cites its AP18, Theorem 7.3.2, for this canonical realization; U004 records the inspected external evidence.
The association from an $L^2$ affiliated operator to its vector $f\Omega$ is injective, since equality of vectors gives zero $L^2$ norm of their difference and the trace is faithful.

## Theorem 2.1 and actual reuse from Miy22

Miy26 states the following two interfaces:

$$
f\in M:\quad f\in C_{\rm div}(s)
\Longleftrightarrow [r_i^*,f]\text{ has finite rank for every }1\leq i\leq d,
$$

and

$$
D(s)\cap M=C_{\rm div}(s).
$$

These are quoted from [Miy22](../../../literature/pdf/Miy22.pdf), Theorems 3.1 and 4.5, with supporting Lemma 4.3.
Their bounded analytic and affiliated proof chains are already recorded in [Miy22-U005](../Miy22/Yin_U005_v1.md#miy22-u005), [Miy22-U006](../Miy22/Yin_U006_v1.md#miy22-u006), and [Miy22-U007](../Miy22/Yin_U007_v1.md#miy22-u007), with the existing repairs and external-proof limits.
This audit checks the match of the finite variance-one system, trace, scalar closures, and bounded operators; it does not erase those earlier verification boundaries or restart a whole Miy22 audit.

The polynomial commutator formula is

$$
[r_i^*,U_w]e_v=
\begin{cases}
e_u,&w=uiv^{\rm rev},\\
0,&\text{otherwise}.
\end{cases}
$$

It follows from the cut formula in [Miy22-U003](../Miy22/Yin_U003_v1.md#miy22-u003), with commutator convention $[T,f]=Tf-fT$.
U002 separately justifies its extension to $L^2$ coefficients; the bounded-only statement is not silently applied to an arbitrary unbounded operator.

The homogeneous semicircular Haagerup estimate used later is

$$
\left\|\sum_{|w|=n}\alpha_wU_w\right\|
\leq(n+1)\left(\sum_{|w|=n}|\alpha_w|^2\right)^{1/2}.
$$

It is the precise $q=0$ bound used in Miy26 p. 9 and Miy22 Lemma 3.5.
The corresponding word-operator decomposition and norm estimate were reconstructed in [Miy22-U004](../Miy22/Yin_U004_v1.md#miy22-u004).
It concerns a fixed homogeneous degree and standard semicircular normalization; an estimate for an arbitrary polynomial follows by summing degrees, not by asserting a universal norm equality.

## Limits, verification, and revisions

The coordinating agent read Section 2 and the cited existing Miy22 units, and visually inspected the defining formulas and Theorem 2.1 on pp. 5-6 on 2026-09-08.
The finite-dimensional Fock actions, closure distinctions, and domain inequality above were checked locally.
General trace/affiliation infrastructure remains explicitly imported; any additional primary inspection is linked through U004.
No new project theorem, unrestricted operator-domain assertion, or formal verification is made.
On 2026-09-08, the separate spectral-interface reviewer checked the regularizer domains, canonical L2 model and reused interfaces; no unresolved local issue was found.
The integrated audit records the complete review scope.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Miy26, arXiv:2603.19528v2, dated 2026-04-21; the registered 23-page artifact. Printed page numbers equal PDF page numbers. Other works retain the separate versions and limitations stated in the body. |
| source-locator | Section 2, pp. 4-6, Theorem 2.1; Theorem 1.1, p. 1. |
| inspection | 2026-09-08: definitions, normalization, core domains and consumed interfaces checked; local interface reconstruction and separate spectral-interface cross-review recorded. Standard trace/affiliation and free-field inputs retain their actual inspection limits in U004; no unrestricted operator-domain assertion or formal verification. |

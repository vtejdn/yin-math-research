---
author: Yin
---

<a id="miy22-u001"></a>
# Miy22-U001: Fock Model, Word Basis, and Ambient Closures

- Source: [Miy22](../../../literature/pdf/Miy22.pdf), local published journal version, 24 pages.
- Locators: Section 2.1, pp. 3-6; Definitions 2.1-2.3; Section 3 opening, p. 8; Section 4 opening, p. 19.
- Record: 2026-09-08, primary audit by the coordinating agent; source text read and rendered formulas inspected.
  This is a source-input unit for [Miy22 source audit](readme.md#miy22-source-audit).
- Kind: definitions, notation normalization, and foundational source inputs.

## Mathematical Setting

Let $d\geq1$ be finite, $H=\mathbb C^d$ with orthonormal basis $e_1,\ldots,e_d$, and

\[
\mathcal F(H)=\bigoplus_{n\geq0}H^{\otimes n},\qquad H^{\otimes0}=\mathbb C\Omega.
\]

The source uses inner products linear in the first variable.
For a word $w=w_1\cdots w_n$, write $e_w=e_{w_1}\otimes\cdots\otimes e_{w_n}$.
The empty word is represented by $\Omega$.
The left and right creation operators prepend and append letters:

\[
\ell_i e_w=e_{iw},\qquad r_i e_w=e_{wi}.
\]

Their adjoints delete the first or last letter if it equals $i$, and otherwise return zero; both annihilate $\Omega$.
Set

\[
s_i=\ell_i+\ell_i^*,\qquad P=\mathbb C\langle s_1,\ldots,s_d\rangle,
\quad A=C^*(s_1,\ldots,s_d),\quad M=W^*(s_1,\ldots,s_d).
\]

The paper writes $M=L^\infty(s)$ and denotes $A$ by a norm-closure bar over $\mathbb C\langle s\rangle$.
That bar is easily lost in text extraction; this audit uses $P,A,M$ to keep the three algebras distinct.

The vacuum state $\tau(x)=\langle x\Omega,\Omega\rangle$ is a faithful trace on $M$, and the $s_i$ form a variance-one free semicircular family.
The vacuum is cyclic and separating.
The map $x\mapsto\widehat x=x\Omega$ extends to a unitary $L^2(M,\tau)\to\mathcal F(H)$.
These statements are stated on p. 5 and imported there from Miy22's references [15] and [18]; those textbooks were not independently inspected in this audit.
In particular, do not call $M$ a factor uniformly in $d$: $d=1$ is included.

## Word Polynomials and Reversal

The source's monic semicircular Chebyshev normalization is

\[
U_{-1}(x)=0,\quad U_0(x)=1,\quad U_{n+1}(x)=xU_n(x)-U_{n-1}(x).
\]

For the maximal-run decomposition $w=i_1^{k_1}\cdots i_m^{k_m}$, with adjacent run letters distinct, define

\[
U_w=U_{k_1}(s_{i_1})\cdots U_{k_m}(s_{i_m}),\qquad U_\Omega=1.
\]

Then $U_w\Omega=e_w$, so the $U_w$ form an orthonormal basis of $L^2(M,\tau)$.
The run letters need not be pairwise distinct: a word such as $121$ is allowed.
Let $w^{\mathrm{rev}}$ denote reversal; then $U_w^*=U_{w^{\mathrm{rev}}}$.
The source writes $w^*$ for this word reversal, which must not be confused with coefficient conjugation.

The map $X^w\mapsto U_w$ is linear, not multiplicative.
For example, $U_i^2=U_{ii}+1$.
Substituting $s_i$ directly into a formal series whose coefficients are the $U_w$-expansion therefore does not preserve its coefficient interpretation; [U004](Yin_U004_v1.md#miy22-u004) supplies the necessary matrix realization.

For cancellation notation, $vw^{-1}$ removes a suffix $w$, while $w^{-1}v$ removes a prefix.
Failed removal is a zero symbol, not the empty word.
The paper denotes that symbol by $0$, sets $U_0=0$, and separately uses the polynomial $U_0(x)=1$.
In reusable formulas, distinguish the zero vector from $e_\Omega=\Omega$.

## Closure Interfaces

For unital $B\subseteq E$, the division closure is the smallest unital subalgebra containing $B$ and closed under inversion of its elements invertible in $E$.
Rational closure requires the analogous property for inverses of matrices of every finite size.

In this paper:

- $C_{\mathrm{div}}(s)$ and $C_{\mathrm{rat}}(s)$ are the two closures of $P$ inside the **bounded** algebra $M$.
- $\widetilde M=\widetilde L^\infty(s)$ is the algebra of closed densely defined operators affiliated with $M$, with the affiliated-algebra sum/product conventions.
- $D(s)$ is the division closure of $P$ inside $\widetilde M$.

Division closure is not by definition a skew field.
A bounded nonzero element need not be boundedly invertible; inverse closure in $M$ differs from inversion in $\widetilde M$.
The equality of division and rational closures in Theorem 3.1 is a theorem in this setting, not a general algebraic identity.
See [U007](Yin_U007_v1.md#miy22-u007) for the external free-field identification quoted in Section 4 and its role outside the core proof.

## Checks, Dependencies, and Limits

The creation/deletion actions, the Chebyshev vacuum recurrence, and the reversal identity were reconstructed from the definitions.
For a single run, the recurrence cancels the backward-annihilation term; appending a different run leaves only the required creation term when acting on the vacuum.
The separating-vector property can also be checked using the right semicircular operators: they commute with the left algebra and generate a dense vacuum orbit.

The trace/free-semicircular identification and the general affiliated-algebra construction are retained as the foundational inputs quoted by Miy22, without a new proof of those external theories.
No claim is made for an arbitrary tuple of noncommuting operators, a nontracial state, an infinite number of generators, or a different covariance normalization without further adaptation.

This unit supplies the objects used by all other Miy22 units.
No new project theorem or formal verification is asserted.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Miy22, the retained 24-page published Journal of Functional Analysis 283 (2022), article 109609, DOI 10.1016/j.jfa.2022.109609. Printed and PDF pages agree, treating the opening article page as p. 1. The related 20-page arXiv preprint was not compared line by line; its locators are not substituted here. |
| source-locator | Section 2.1, pp. 3-6, Definitions 2.1-2.3; Section 3 opening, p. 8; Section 4 opening, p. 19. |
| inspection | 2026-09-08: source text and rendered formulas inspected; creation/deletion, word reversal and elementary closure conventions reconstructed. Trace/free-semicircular identification and general affiliated-algebra construction remain foundational source-reported inputs; no independent reconstruction of all external theories or formal verification is claimed. |

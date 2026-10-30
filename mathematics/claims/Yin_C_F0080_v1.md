---
author: Yin
---
# A nonatomic normal generator with a liberation dual system and no conjugate variable

Context: determine whether existence of a liberation dual system implies existence of conjugate variables for normal generators with nonatomic spectral distributions.
The human requested that the counterexample and its proof be fixed as mathematical material.

## Statement

Let
\[
 d\mu(x):=\frac{1_{(-1,1)}(x)}{\pi\sqrt{1-x^2}}\,dx,
 \qquad M:=L^\infty((-1,1),\mu),\qquad
 \tau(f):=\int f\,d\mu,
\]
and let \(X(x):=x\), \(H:=L^2(M,\tau)\), \(\Omega:=1\).
Represent M on H by multiplication, and let P_Omega be the orthogonal projection onto the constants.
Then X is a selfadjoint generator of M with nonatomic spectral distribution, and X-lambda is regular for every complex lambda.
The bounded operator L:=P_Omega is a normalized liberation dual system for the one-element tuple X: its domain and adjoint domain are H, and
\[
 [X,L]=[X,P_\Omega],\qquad L=P_\Omega.
\]
However, there is no derivation
\[
 \partial:\mathbb C[X]\subset H\longrightarrow H\bar\otimes H,
 \qquad \partial X=1\otimes_{\mathbb C}1,
 \qquad 1\otimes_{\mathbb C}1\in\operatorname{Dom}\partial^*.
\]
Thus existence of a liberation dual system, even a bounded selfadjoint normalized one, does not imply existence of conjugate variables, even for normal generators with nonatomic spectral distributions and regular scalar shifts.

## Definitions and provenance

The liberation commutator and common-domain conditions are the local variant stated in [C_F0079 v4](Yin_C_F0079_v4.md#liberation-dual-system).
Here normalized means that the sum of the operators is P_Omega, so in one variable the sum condition is simply L=P_Omega.
Regular means injective with dense range, equivalently invertible as an affiliated operator.
The conjugate-variable condition is the actual vacuum adjoint condition for the derivations recorded in [ACSY24-U001](../audits/literature/ACSY24/Yin_U001_v1.md#acsy24-u001).
Since X is selfadjoint, its starred polynomial algebra is exactly C[X], and the prescribed generator value determines the entire derivation.
No comparison theorem from either source is needed in the proof below.

The Chebyshev computation was already present in continuing exploration in a different comparison involving ordinary duals.
The complete calculation is fixed below; the preceding exploration supplies extraction provenance, not a proof dependency.
The liberation-dual conclusion was checked in the current discussion.
A separately assigned checking agent supplied the shorter monomial proof below; that contribution is part of proof development, not an independent review of that proof.

## Argument

### The operator and its liberation dual

The trace is faithful and normal, X is a bounded selfadjoint operator, and its spectral law is mu.
The coordinate function generates the measurable sigma-algebra modulo null sets, so W*(X)=M.
The measure mu has no atoms.
For any complex lambda, multiplication by x-lambda and its adjoint have trivial kernel, since their zero set has mu measure zero (or is empty).
Consequently X-lambda has dense range as well as trivial kernel and is regular.
The operator L=P_Omega is bounded and selfadjoint on H and satisfies the displayed liberation commutator and normalization identities directly.

### Failure of the vacuum adjoint condition

Every nonzero polynomial is nonzero on a set of positive mu measure, so evaluation identifies C[X] with the scalar polynomial algebra.
The product rule and the condition partial X=1 tensor 1 uniquely give
\[
 \partial X^k=\sum_{j=0}^{k-1}X^j\otimes_{\mathbb C}X^{k-1-j}
 \qquad(k\geq1).
\]
This formula defines the difference quotient on C[X].
Under x=cos(theta), mu is the pushforward of dtheta/pi on (0,pi); elementary integration gives
\[
 m_{2r}:=\tau(X^{2r})=4^{-r}\binom{2r}{r},\qquad
 m_{2r+1}:=0.
\]
The binomial series yields
\[
 \sum_{r\geq0}m_{2r}z^r=(1-z)^{-1/2},\qquad
 \sum_{r=0}^{n}m_{2r}m_{2(n-r)}=1.
\]
Hence, for every n>=0,
\[
 (\tau\otimes\tau)(\partial X^{2n+1})
 =\sum_{r=0}^{n}m_{2r}m_{2(n-r)}=1.
\]
On the other hand, |x|<1 mu-almost everywhere, so dominated convergence gives
\[
 \|X^{2n+1}\|_2^2=\int |x|^{4n+2}\,d\mu(x)\longrightarrow0.
\]
If xi:=partial*(1 tensor 1) belonged to H, the adjoint identity and Cauchy-Schwarz would give
\[
 1=\left|(\tau\otimes\tau)(\partial X^{2n+1})\right|
 \leq\|\xi\|_2\,\|X^{2n+1}\|_2\longrightarrow0,
\]
a contradiction.
This excludes every derivation satisfying the prescribed generator value, not just a chosen realization.
No formula for free Fisher information, principal-value Hilbert transform, or maximal-Delta theorem is used.

### The original Chebyshev calculation

For completeness, retain the original argument that detected the same failure of the adjoint-domain condition.
Define the first-kind Chebyshev polynomials by T_n(cos(theta)):=cos(n theta), and set
\[
 \ell(p):=\iint\frac{p(x)-p(y)}{x-y}\,d\mu(x)d\mu(y).
\]
The quotient is its polynomial continuation on the diagonal.
For |z|<1, the generating function and its divided difference are
\[
 G_z(x):=\sum_{n\geq0}T_n(x)z^n=\frac{1-zx}{1-2zx+z^2},
\]
\[
 \frac{G_z(x)-G_z(y)}{x-y}
 =\frac{z(1-z^2)}{(1-2zx+z^2)(1-2zy+z^2)}.
\]
Fourier orthogonality, or the geometric Fourier expansion of the denominator, gives
\[
 \int\frac{d\mu(x)}{1-2zx+z^2}=\frac1{1-z^2}.
\]
Thus ell(G_z)=z/(1-z^2).
Termwise application of ell is justified on compact subdisks: |T_n|<=1 and |T_n'|<=n^2 on [-1,1], and sum n^2 |z|^n converges.
The derivative estimate follows from T_n'(cos(theta))=n sin(n theta)/sin(theta) and |sin(n theta)|<=n|sin(theta)|, with continuous endpoint values.
Comparing coefficients gives
\[
 \ell(T_{2n+1})=1,\qquad\ell(T_{2n})=0.
\]
Fourier orthogonality also gives pairwise orthogonality of T_n(X), n>=1, with squared L2 norm 1/2.
Consequently, for p_N:=sum_{n=0}^{N-1}T_{2n+1},
\[
 \ell(p_N)=N,\qquad\|p_N(X)\|_2=\sqrt{N/2}.
\]
Since ell(p)=(tau tensor tau)(partial p(X)), this again proves that no H-vector represents the vacuum functional.

## Dependencies and limits

The argument is self-contained apart from elementary spectral facts for multiplication operators, the binomial series, Fourier orthogonality, dominated convergence and the Hilbert-space adjoint criterion.
The definition links fix the meaning of the compared conditions; neither linked source supplies an unproved substantive premise.
The example has one selfadjoint generator and makes no claim about a prescribed number of generators greater than one or about the converse implication for arbitrary nonnormal tuples.
No historical novelty or literature-wide priority claim is made.

## Current assessment
[Selected decision](#decision-accepted-counterexample)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-18T11:07 |
| status | open |
| reason | The complete counterexample, shorter monomial argument and original Chebyshev calculation are fixed for review before adoption. |

Recorded authoring stage: proof draft.
Recorded review label: under review.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Nonatomic selfadjoint generator, regular scalar shifts, normalized liberation dual and absence of a conjugate variable. |
| argument | [Argument](#argument) | Complete operator, monomial and Chebyshev proofs with the actual adjoint-domain obstruction. |

### Decision accepted-counterexample

| Field | Value |
| --- | --- |
| date | 2026-10-18T11:14 |
| status | proved |
| reason | A separately organized reviewer independently checked the complete operator construction, monomial proof, original Chebyshev calculation and definition interfaces, with no unresolved gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Nonatomic selfadjoint generator, all regular scalar shifts, normalized liberation dual and absence of a conjugate variable. |
| argument | [Argument](#argument) | Complete construction and both vacuum-adjoint obstructions, with elementary inputs and explicit scope limits. |
| review | [R_F0053 whole-proof finding](../audits/reviews/Yin_R_F0053_v1.md#whole-proof-finding) | Independent review of the exact statement, both complete arguments and compared definition interfaces. |

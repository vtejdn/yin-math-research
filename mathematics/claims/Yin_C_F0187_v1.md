---
author: Yin
---

# Intermediate singular values of finite-variance real Wigner matrices with arbitrary complex shifts

<a id="statement"></a>
## Uniform intermediate-singular-value theorem

Let \(W_n\) be a real symmetric matrix whose upper off-diagonal entries are independent copies of \(\xi/\sqrt n\), where the fixed real law \(\xi\) is centered with variance one.
The diagonal is independent of the off-diagonal entries and can have arbitrary independent laws or be deterministic.
For every deterministic complex matrix \(F_n\), write singular values in decreasing order.
There are \(c,C>0\) and \(n_0\), depending only on the fixed off-diagonal law, such that for \(n\ge n_0\),
\[
 \mathbb P\!\left\{\exists j\in\{\lceil n^{3/4}\rceil,\ldots,n-1\}:
 s_{n-j}(W_n+F_n)<c j/n\right\}
 \le C n^2\exp(-c n^{1/4}).
\]
No symmetry or norm bound on \(F_n\) is required.
The same estimate holds conditionally for a random shift independent of \(W_n\), with constants uniform in its realization.
Thus the bound holds eventually almost surely under every cross-size coupling.
This controls intermediate singular values only; it supplies no estimate for the least singular value or for general matrix-coefficient pencils.

## Inputs, provenance and relevance

This is a local finite-variance adaptation of the projection, convex concentration and negative-second-moment method inspected in [GNT14](../audits/literature/GNT14/readme.md).
Only the dimension-free bounded-product convex concentration theorem is used as an external input; its original proof is not re-audited.
The truncation exponents, arbitrary complex shifts and row-independence restoration are justified explicitly below.
The statement is a reusable input for the [active Task](../tasks/Yin_T_F0012_v3.md#contract), with a distinct small-singular-value mechanism from the broader [spectral-control theorem](Yin_C_F0186_v4.md#statement).
It does not complete that Task or claim novelty.

<a id="argument"></a>
## Proof

## A finite-variance distance estimate with summable failure

We use the standard bounded-product convex concentration inequality: if independent real coordinates have support in intervals of diameter at most \(2b\), and \(f\) is convex and 1-Lipschitz for Euclidean distance, then
\[
 \mathbb P\{|f-\operatorname{med}f|\ge t\}
 \le C\exp(-ct^2/b^2).
 \tag{9}
\]
One inspected primary-source pointer is the bounded-product input stated as Theorem 3.7 and Corollary 3.8 on PDF p. 30 of [Götze--Naumov--Tikhomirov](https://arxiv.org/pdf/1404.7013).
Their adjacent projection scheme motivated the following explicit choice of different truncation and codimension exponents.
The proof of the concentration theorem itself is an external input and is not audited here.

Let \(x=(\xi_1,\ldots,\xi_n)\) have independent copies of a fixed real centered variance-one law with finite second moment.
Let \(H\subset\mathbb C^n\) be a deterministic complex linear subspace with complex codimension \(q\ge c_0n^{3/4}\), and let \(f\in\mathbb C^n\) be arbitrary and deterministic.
There are constants \(c,C>0\), independent of \(H\) and \(f\), such that eventually
\[
 \mathbb P\{\operatorname{dist}(x+f,H)\le c\sqrt q\}
 \le C\exp(-cn^{1/4}).
 \tag{10}
\]
To prove this, truncate by conditioning on the good-coordinate set
\[
 J=\{i:|\xi_i|\le n^{1/4}\}.
\]
Since \(\mathbb P\{|\xi|>n^{1/4}\}\le n^{-1/2}\), a binomial Chernoff bound gives
\[
 \mathbb P\{|J^c|>n^{5/8}\}\le \exp(-c n^{5/8}\log n)
 \tag{11}
\]
for all large \(n\).
Conditional on a fixed good set \(J\), its retained coordinates remain independent, with the common law of \(\xi\) conditional on \(|\xi|\le n^{1/4}\).
Let its mean and variance be \(m_n,v_n\); finite variance gives \(m_n\to0\) and \(v_n\to1\).
Project onto the coordinates in \(J\), and enlarge the projected subspace by the single vector \(f_J+m_n\boldsymbol1\).
Denote the enlarged space by \(H_J'\).
Its codimension is at least
\[
 q-|J^c|-1\ge q/2
\]
eventually whenever \(|J^c|\le n^{5/8}\).
Consequently
\[
 \operatorname{dist}(x+f,H)
 \ge \operatorname{dist}(x_J-m_n\boldsymbol1,H_J').
 \tag{12}
\]
For the centered conditional vector \(y=x_J-m_n\boldsymbol1\), the right-hand distance is convex and 1-Lipschitz as a function of its real coordinates.
If \(Q\) is the complex orthogonal projection onto \((H_J')^\perp\), then
\[
 \mathbb E\|Qy\|^2=v_n\operatorname{Tr}Q\ge q/3.
 \tag{13}
\]
Equation (13) holds although the coordinates are real, since their covariance matrix is \(v_nI\).
By integrating (9), the mean differs from the median by at most \(Cn^{1/4}\), and the variance is at most \(Cn^{1/2}\).
The median is therefore at least \(c\sqrt q\), because \(n^{1/4}=o(\sqrt q)\).
Applying (9) once more gives a conditional lower-tail bound \(C\exp(-cq/n^{1/2})\), uniformly in \(J,H,f\).
Combining it with (11) proves (10).
Separating the bad-coordinate exponent \(5/8\) from the codimension exponent \(3/4\) is essential to the displayed dimension inequality.

## Intermediate singular values of Wigner plus an arbitrary complex shift

Let \(W_n\) be a normalized real symmetric Wigner matrix with the off-diagonal law just used.
Its diagonal can have any independent law, and may instead be deterministic.
Let \(F_n\) be any deterministic complex matrix, with no symmetry or norm bound required in this subsection.
Write singular values in decreasing order.
There are constants \(c,C>0\), uniform over \(F_n\), such that
\[
 \mathbb P\left\{\exists j\in[\lceil n^{3/4}\rceil,n-1]:
  s_{n-j}(W_n+F_n)<c\frac jn\right\}
 \le Cn^2\exp(-cn^{1/4}).
 \tag{14}
\]
Fix such a \(j\), put \(k=\lfloor j/2\rfloor\), and retain the first \(n-k\) rows of \(\sqrt n(W_n+F_n)\), giving a rectangular matrix \(B\).
For each retained row index \(i\), let \(H_i\) be the span of the other retained rows.
Delete coordinate \(i\) from that row and from \(H_i\).
The projected row has independent off-diagonal entries, and is independent of the projected row space: its mirrored partners are precisely the entries in column \(i\), which has been deleted.
The remaining deterministic shift is absorbed into \(f\) in (10).
The ambient dimension is \(n-1\), while the projected span has dimension at most \(n-k-1\), so its codimension is at least \(k\).
Equation (10), conditioning on the projected row space, proves that every retained row has distance at least \(c\sqrt k\) from the other rows, except on a set of probability at most \(Cn\exp(-cn^{1/4})\).
On this event \(B\) has full row rank, and the negative-second-moment identity gives
\[
 T:=\sum_{r=1}^{n-k}s_r(B)^{-2}
   =\sum_{i=1}^{n-k}\operatorname{dist}(B_i,H_i)^{-2}
   \le C\frac nk.
 \tag{15}
\]
Indeed, the Schur formula for the \(i\)-th diagonal entry of \((BB^*)^{-1}\) gives the reciprocal squared row distance, and taking its trace gives both sides of the identity.
There are at least \(j-k\) singular values of \(B\) no larger than \(s_{n-j}(B)\), and hence
\[
 (j-k)s_{n-j}(B)^{-2}\le T.
\]
Combining this with (15), row-deletion interlacing, and the factor \(1/\sqrt n\), yields
\[
 s_{n-j}(W_n+F_n)\ge n^{-1/2}s_{n-j}(B)
 \ge c\frac jn.
\]
A union bound over \(j\) proves (14).
The bound is summable and therefore works for every cross-size coupling.
It also holds conditionally for a random \(F_n\) independent of \(W_n\), because all constants are uniform in the shift.

## Current assessment
[Selected decision](#decision-intermediate-reviewed)

## Assessment history

### Decision intermediate-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T00:39 |
| status | open |
| reason | The complete argument is retained for independent review, with its exact intermediate range and uniform deterministic-shift quantifiers. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Uniform intermediate bound](#statement) | Fixed finite-variance real off-diagonal law, arbitrary independent diagonals and deterministic complex shifts, with summable failure. |

### Decision intermediate-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T00:46 |
| status | proved |
| reason | Independent inspection checked the exact bounded-product concentration input and every local implication, with no substantive gap. This proves only the stated intermediate range, not a least-singular-value or general-pencil bound. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | The full intermediate range, arbitrary deterministic complex shifts and independent diagonals, and summable uniform bounds. |
| argument | [Complete argument](#argument) | The finite-variance conditional truncation, distance estimate, restored independence and negative-second-moment proof. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0191_v1.md#intermediate-bound-reviewed) | Exact statement and complete argument, with explicit source and scope limits. |


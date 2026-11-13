---
author: Yin
---
# A Haar unitary times a two-point modulus separates conjugate variables from full-domain duals

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(G=\langle u,s\mid s^2=1\rangle=\mathbb Z*\mathbb Z_2\), use the same letters for the canonical unitaries in the group von Neumann algebra \(M=L(G)\), and equip \(M\) with the trace at the identity.
Set \(p=(1+s)/2,\ q=1-p,\ h=\varepsilon p+q,\ X=uh\), with \(0<\varepsilon\le1/2\).
Then \(\|X\|=1,\ W^*(X)=M\), and the represented star-polynomial algebra in \(X\) admits an actual [ACSY derivation](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) with vacuum
\[
 \xi=\tfrac12u-\left(\tfrac12+\tfrac1{1-\varepsilon}\right)us .
\]
Its Hilbert norm is at most \(\sqrt{13/2}\).
The [bounded-dual cost](Yin_C_F0201_v1.md#statement) for this generator, with unrestricted value at \(1\), satisfies \(\beta(X)\ge 1/(4\sqrt2\,\varepsilon)\).

Consequently there exists a bounded single generator satisfying actual ACSY with no bounded operator-norm-to-\(L^2\) dual.
There exists a bounded two-coordinate tuple with actual ACSY and no algebraic bare dual system on all bounded vectors, so the implication \(\mathsf A\Rightarrow\mathsf F\) fails for arbitrary finite tuples.
The two-coordinate tuple also fails the stronger full-domain condition \(\mathsf S\).
These assertions concern the arbitrary-tuple branch of the Task.

## Argument

### The represented coordinates and their derivation

One has \(X^*X=\varepsilon^2p+q\), so \(p=(1-X^*X)/(1-\varepsilon^2)\), \(s=2p-1\), \(h^{-1}=\varepsilon^{-1}p+q\), and \(u=Xh^{-1}\) belong to the represented star core.
Thus the core equals \(\mathbb C G\), and \(\|X\|=\|h\|=1\) since \(q\) is nonzero.
Write \(t=usu^{-1}\) and use outer actions on \(L^2(M)\otimes_2L^2(M)\).
Prescribe
\[
 \delta u=1\otimes q+\varepsilon^{-1}t\otimes p,\qquad
 \delta p=-\frac{2}{1-\varepsilon}q u^{-1}\otimes p,\qquad
 \delta s=2\delta p,\qquad
 \delta(u^{-1})=-u^{-1}(\delta u)u^{-1}.
\]
The identities \(s\delta p=-\delta p\) and \((\delta p)s=\delta p\) give \(\delta(s^2)=0\).
The inverse prescription kills the derivatives of both \(uu^{-1}\) and \(u^{-1}u\).
Reduction by these relations gives unique reduced group words, so the prescriptions define a complex-linear outer derivation on \(\mathbb C G\), with finite group-tensor values on each word.
The left factor \(uqu^{-1}=(1-t)/2\) gives
\[
 \delta(uh)=(\delta u)h+u(\varepsilon-1)\delta p
 =1\otimes q+t\otimes p+(1-t)\otimes p=1\otimes1 .
\]

### The adjoint vacuum on every reduced word

Use letters \(u,u^{-1},s\) with adjacent inverse pairs and \(ss\) removed.
The trace of a group element is zero unless that element is the identity, and these words are an orthonormal basis of \(L^2(M)\).
Let \(w=P\ell Q\) be a marked occurrence of a single letter in a reduced word.
For a tensor summand \(a\otimes b\) assigned to \(\delta u\), with \(a,b\) group elements, its positive cut contributes its coefficient to the double trace precisely when \(P=a^{-1}\) and \(Q=b^{-1}\).
In a negative cut the corresponding assigned tensor is \(-u^{-1}a\otimes b u^{-1}\).
It can contribute only if \(P=a^{-1}u\) and \(Q=u b^{-1}\) as group elements.
In both summands of the prescribed \(\delta u\), the right group letters \(b\) belong to \(\{1,s\}\), so this required suffix starts with \(u\).
Such a suffix cannot follow the marked \(u^{-1}\) in a reduced word.
For positive cuts the term \(t\otimes p\) requires prefix \(t^{-1}=usu^{-1}\), which cannot precede \(u\) in a reduced word.
Thus the entire \(\varepsilon^{-1}\) term has zero vacuum pairing on every input.
The two surviving positive cuts from \(1\otimes q\) have empty prefix and give \(1/2\) at \(u\) and \(-1/2\) at \(us\).

For an \(s\)-cut, expand its coefficient as
\[
 -\frac1{1-\varepsilon}(u^{-1}-s u^{-1})\otimes(1+s).
\]
The right leg \(s\) would require suffix \(s\), and the left leg \(su^{-1}\) would require prefix \(us\).
Both would put \(ss\) next to the marked letter.
The only surviving term has prefix \(u\), empty suffix, and contributes \(-1/(1-\varepsilon)\) at \(us\).
This enumeration includes every marked occurrence in every reduced word.
Since all surviving coefficients are real, with the Hilbert inner product linear in the second variable the representing vector is exactly the displayed \(\xi\).
In particular \(1\otimes1\) is in the actual Hilbert adjoint domain, with \(\|\xi\|_2^2=1/4+(1/2+1/(1-\varepsilon))^2\le13/2\).

### All bounded duals and the separating tuple

Let \(E:M\to L^2(M)\) be any bounded solution of \([E,L_X]=P_1\) on \(M\), where \(P_1a=\tau(a)1\).
Take \(f=upu^{-1}\), so \(\|Xp\|=\varepsilon,\ \|fX\|=\varepsilon\) and \(\tau(f)=\tau(p)=1/2\).
Evaluating at \(p\) and multiplying the result by \(f\) gives
\[
 \frac1{2\sqrt2}
 =\|\tau(p)f\|_2
 =\|f E(Xp)-fX E(p)\|_2
 \le 2\varepsilon\|E\|_{M\to L^2(M)} .
\]
This proves the asserted lower bound, including the case of infinite cost.
Now take \(\varepsilon_n=2^{-n}\) for \(n\ge1\).
The bounded generators have common cutoff one, actual vacua of uniformly bounded norm, and finite starred-generator derivative norms at each individual \(n\), because \(X^*\in\mathbb C G\).
The ratio \(\beta(X_n)/(1+\|\xi_n\|_2)\) is unbounded.
The [one-generator assembly theorem](Yin_C_F0210_v1.md#statement) applies with exactly these hypotheses and gives the single generator of infinite bounded cost and the two-coordinate failure of bare duality.
The latter conclusion uses the [free semicircular enlargement](Yin_C_F0205_v1.md#statement), which makes every algebraic full-domain witness in a full system bounded and compresses bounded old-coordinate witnesses back to the original algebra.
Finally \(\mathsf S\) implies \(\mathsf F\) by restriction.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T16:04 |
| status | open |
| reason | The group-ring derivation and its finite-support adjoint vacuum supply the ratio needed for separation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Explicit ACSY witnesses, divergent bounded-dual ratio and the arbitrary-tuple nonimplication. |
| argument | [Argument](#argument) | Group presentation, reduced-word cut enumeration, singular projection cost and exact assembly. |
| dependency | [One-generator ratio criterion](Yin_C_F0210_v1.md#statement) | Assemble a sequence with unbounded ratio into one single-generator ACSY law of infinite bounded cost. |
| dependency | [Free semicircular extension](Yin_C_F0205_v1.md#statement) | Turn the infinite bounded cost into failure of algebraic bare duality for a two-coordinate ACSY tuple. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T16:09 |
| status | proved |
| reason | Adopt the counterexample to the arbitrary-tuple ACSY-to-bare-dual implication after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Explicit ACSY witnesses, divergent bounded-dual ratio and the arbitrary-tuple nonimplication. |
| argument | [Argument](#argument) | Group presentation, reduced-word cut enumeration, singular projection cost and exact assembly. |
| dependency | [One-generator ratio criterion](Yin_C_F0210_v1.md#statement) | Assemble a sequence with unbounded ratio into one single-generator ACSY law of infinite bounded cost. |
| dependency | [Free semicircular extension](Yin_C_F0205_v1.md#statement) | Turn the infinite bounded cost into failure of algebraic bare duality for a two-coordinate ACSY tuple. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0233_v1.md#whole-proof-finding) | Group-core descent, finite-support adjoint vacuum, all bounded witnesses, assembly and exclusion of every algebraic dual system on the enlarged tuple. |

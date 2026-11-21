---
author: Yin
---
# A uniform support bound for the precision of trace-zero idempotents

## Statement

Let \(G\) be any discrete group, let \(p\) be a prime, and let \(e\ge1\).
Suppose
\[
 f=\sum_{i=1}^{k}x_i g_i\in(\mathbb Z/p^e\mathbb Z)[G]
\]
is idempotent, where the labels \(g_i\) are distinct and different from \(1\), and some coefficient \(x_j\) is a unit.
Other coefficients may be zero or nonunits, so the \(k\) labels may be an upper bound on the support.
For \(k\ge2\), put
\[
 n=k+1,\qquad m_k=k^2+k+1,
\]
\[
 H(k)=4n(n+1)2^n
 \left(\log2+\log m_k+2(n+7)\log\!\left(2(n+1)\right)\right).
                                                                    \tag{1}
\]
Then
\[
                         e\log p\le H(k).                            \tag{2}
\]
All logarithms are natural.
The bound is uniform over the group, its actual support table, the marked index \(j\), and every choice of integer representatives of the coefficients.
No zero-divisor or torsion-free hypothesis is used.

There are sharper elementary conclusions for the smallest supports.
One label is impossible.
With at most two labels, the only possibility is \(p=2\), \(e=1\), and
\[
                         f=g+g^2,\qquad \operatorname{ord}(g)=3.
                                                                    \tag{3}
\]
In particular odd characteristic requires at least three support labels.

For a family of such idempotents with \(T=e\log p\to\infty\), (2) gives
\[
 k\ge \frac{\log T}{\log2}-O(\log\log T),
 \qquad
 \liminf\frac{k}{\log T}\ge\frac1{\log2}.                              \tag{4}
\]
At a fixed prime, the precision is at most \(\lfloor H(k)/\log p\rfloor\).
At precision one, only primes \(p\le\exp H(k)\) are possible with at most \(k\) labels.

The unit-coefficient hypothesis is automatic for any nonzero idempotent in \((\mathbb Z/p^e\mathbb Z)[G]\).
Indeed, if all coefficients were divisible by \(p\), then \(f=f^r\in p^r(\mathbb Z/p^e\mathbb Z)[G]\) for every \(r\), and \(f=0\).
The marked coefficient is nevertheless retained in the proof to encode nonvanishing by a polynomial equation.

## The characteristic-zero obstruction

For every discrete group \(G\), an idempotent \(F\in\mathbb C[G]\) whose coefficient at \(1\) is zero must vanish.
Use the faithful regular representation in the finite group von Neumann algebra \(\mathcal N(G)\), with its canonical faithful trace \(\tau\).
The range of the bounded idempotent \(F\) is closed.
Its orthogonal range projection \(P\) belongs to \(\mathcal N(G)\) and satisfies
\[
 PF=F,\qquad FP=P.
\]
Traciality gives
\[
 \tau(F)=\tau(PF)=\tau(FP)=\tau(P).
\]
Since \(\tau(F)\) is the coefficient of \(1\), it is zero by assumption.
Faithfulness gives \(P=0\), hence \(F=0\).
This uses the standard bounded-idempotent trace identity also written out in [C12](Yin_C_A0012_v4.md#complete-bounded-proof); it asserts positivity of the trace of a nonzero idempotent, not integrality of that trace.

## The integral coefficient scheme

Fix the actual labels \(S=\{g_1,\ldots,g_k\}\subset G\setminus\{1\}\) and the marked index \(j\).
In the polynomial ring \(\mathbb Z[X_1,\ldots,X_k,Y]\), put
\[
 F=\sum_{i=1}^k X_i g_i.
\]
For each \(h\in S^2\cup S\), take the coefficient polynomial
\[
 Q_h=\sum_{g_i g_\ell=h}X_iX_\ell
       -\sum_{g_i=h}X_i,                                      \tag{5}
\]
and add
\[
                         Q_*=YX_j-1.                         \tag{6}
\]
There are \(n=k+1\) variables and
\[
 m=|S^2\cup S|+1\le k^2+k+1
\]
equations.
Every equation has degree at most two.
Their integer coefficients have absolute value at most two.
To check the last assertion, a diagonal monomial \(X_i^2\) comes from one ordered cell.
For \(i\ne\ell\), the only cells producing the same commutative monomial \(X_iX_\ell\) are \((i,\ell)\) and \((\ell,i)\); they contribute to the same polynomial only if their actual products coincide.
Thus their combined coefficient is at most two.
The distinct group labels ensure that each linear term in (5) has coefficient \(-1\).
No coefficient grows with the number of cells in a product fiber.
The maximum logarithmic coefficient height is therefore at most \(\log2\).

A complex point of (5) would give an idempotent with coefficient at \(1\) equal to zero, because \(1\notin S\).
The preceding trace argument would force every \(X_i=0\).
Equation (6) excludes this.
Consequently this integral system has no common complex zero.
Actual group realizability is essential to this step; an arbitrary abstract collision partition is not enough.

Apply [Krick–Pardo–Sombra, Theorem 1, arXiv:math/9911094v1, p. 2](https://arxiv.org/pdf/math/9911094), with \(n=k+1\), degree bound two, height bound \(\log2\), and at most \(m_k\) equations.
It gives a nonzero integer \(a\) and integral polynomials \(U_h,U_*\) such that
\[
                 a=\sum_{h\in S^2\cup S}U_h Q_h+U_*Q_*,
 \qquad
                         \log|a|\le H(k).                    \tag{7}
\]
Formula (1) deliberately enlarges the logarithmic contribution in that theorem.
It uses the same conservative arithmetic estimate as [the exact-support transfer in L59](../ledger/Yin_L_A0059_v1.md#a-general-effective-transfer-that-preserves-every-coefficient), with height \(\log2\) instead of zero.
No claim of optimality is made.

Evaluate (7) at the given coefficients modulo \(p^e\), choosing \(Y=x_j^{-1}\).
Idempotence makes every \(Q_h\) zero, and (6) is zero by this choice.
Hence \(a=0\) in \(\mathbb Z/p^e\mathbb Z\), that is,
\[
                         p^e\mid a.
\]
Since \(a\ne0\), one has \(e\log p\le\log|a|\), proving (2).
The exponent is exactly \(e\), with no loss of one power of \(p\).
The coefficients of \(f\) may be chosen independently at successive precisions, and the support table may vary as well.
The same uniform bound still applies.

For a known table one may replace \(m_k\) by the actual equation count and \(\log2\) by its actual maximum coefficient height.
The existence of an integer certificate is all that the proof requires; its coefficients are not claimed to be presently computed for a given table.
Since \(H(k)=O(2^k k^3\log(k+2))\), taking logarithms yields (4).

## The exact one- and two-label cases

For one label, write \(f=xg\) with \(g\ne1\) and \(x\) a unit.
The equality \(g^2=g\) would force \(g=1\), so the coefficient of \(g\) in \(f^2-f\) is \(-x\).
It cannot vanish.

Now suppose at most two labels occur, and write \(f=xg+yh\), with \(g,h\ne1\) distinct and \(x\) a unit.
If \(y\) were not a unit, reduction modulo \(p\) would give the impossible one-label idempotent.
Thus both \(x,y\) are units.
In order for the coefficient of \(g\) in \(f^2\) to equal the nonzero coefficient \(x\), some product of the two labels must equal \(g\).
The possibilities \(g^2=g\), \(gh=g\), and \(hg=g\) are excluded by cancellation and \(g,h\ne1\).
Therefore \(h^2=g\).
Similarly \(g^2=h\).
It follows that \(g^3=1\), \(g\ne1\), and \(h=g^2\).
The identity coefficient of \(f^2-f\) is then \(2xy\).
Since \(x,y\) are units, this forces \(2=0\) in \(\mathbb Z/p^e\mathbb Z\), hence \(p=2\), \(e=1\).
Both coefficients must be one, and direct multiplication gives
\[
 (g+g^2)^2=g^2+g^4=g+g^2
\]
in characteristic two.
This proves (3).

The odd-characteristic lower bound of three labels is attained at \(p=3\): use \(G=C_4\) and \(f=-g-g^2-g^3\) modulo three.
More generally, for every prime power \(p^e\), let \(G\) be cyclic of order \(p^e+1\) and put
\[
                         f=-\sum_{g\in G\setminus\{1\}}g.
\]
There are \(p^e\) pairs of nonidentity elements with product \(1\), and \(p^e-1\) such pairs with product any fixed nonidentity element.
Thus \(f^2=f\) modulo \(p^e\), with trace zero and all support coefficients units.
These torsion examples confirm that a support-dependent bound is necessary; they give no torsion-free example and do not establish sharpness of (1).

## Application to defects of approximate one-sided inverses

Suppose integral group-ring elements \(A,B_e\) satisfy \(AB_e\equiv1\pmod{p^e}\), and set \(D_e=1-B_eA\).
Modulo \(p^e\),
\[
 D_e^2-D_e=B_e(AB_e-1)A=0.
\]
The coefficient trace is cyclic over the commutative coefficient ring, so
\[
 [1]D_e=1-[1](B_eA)=1-[1](AB_e)=0\pmod{p^e}.
\]
If \(D_e\) is nonzero modulo \(p\), a nonidentity coefficient is a unit modulo \(p^e\).
Delete its zero identity coefficient and all other zero coefficients after reduction.
The resulting support of size \(k_e\) meets the statement and satisfies \(e\log p\le H(k_e)\).
If the supports of \(A,B_e\) have sizes \(a,b_e\), respectively, then \(k_e\le ab_e\).

This conclusion is independent of the heights and choices of integral lifts.
A separate bound for solving \(AB_e\equiv1\) with one fixed integral \(A\) may exploit the coefficient height of that \(A\) and be stronger in \(b_e\); that is a different assertion and does not improve the present support-only estimate for \(D_e\).
The [local saturation test C39](Yin_C_A0039_v1.md#statement) addresses lifting a marked zero-product point on one fixed table.
Here every complex fiber is already empty by the trace argument, and (7) bounds the obstruction uniformly over tables of bounded size.
The [projective transfer C93](Yin_C_A0093_v1.md#statement) concerns bilinear zero products and can transfer to smaller supports.
It does not by itself impose idempotence or a zero identity coefficient, which are the extra conditions making the present contradiction unconditional for all groups.

## Assessment history

### Decision trace-zero-idempotents

| Field | Value |
| --- | --- |
| date | 2026-11-21T04:11 |
| status | proved |
| reason | Independent whole-proof inspection supports the stated result at its declared scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Support-only precision bound, sharp small-support classification and reverse-defect application. |
| argument | [Proof](#the-characteristic-zero-obstruction) | Complete trace obstruction, arithmetic certificate, examples, bounds and scope. |
| review | [Whole finding](../audits/reviews/Yin_R_A0130_v1.md#whole-finding) | Complete independent review including the external interfaces and limitations stated in the finding. |

## Current assessment

[Selected decision](#decision-trace-zero-idempotents)

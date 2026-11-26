---
author: Yin
---

# A circle-bounded transfer and a spectral gap at the order-sixteen four-coset marking

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with scalar group-ring injectivity and a cyclic quotient of order sixteen in which \(s\) has odd degree and \(t\) has degree four.
Write \(P(z)=Az+B,\ Q(z)=Cz+D\) for two-square complex pencils and \(K=P(t)-sQ(t)\).
If the regular nullity of \(K\) is \(1/2\), both pencils are invertible at every point of the unit circle.
In particular \(K\) has closed range, its orthogonal kernel projection belongs to \(M_2(C_r^*(H))\), and the squared Fourier coefficients of that projection have a finite exponential moment for some positive exponent in the marked word length.

There is a single \(X\in M_2(\ell^1(H))\) with \(KXK=K\).
Every quotient \(J\) through which the marked character modulo four factors has regular nullity \(1/2\) for the image of this same \(K\), and its range is closed there as well.
In particular if the trace on matrix projections of even one such \(C_r^*(J)\) omits \(1/2\), the supposed half kernel is impossible.
The trace condition may be applied to \(H\) itself.
The theorem leaves open the bounded case when these trace tests give no exclusion.

## The possible singularity has one shared simple root

Write \(a\) for the odd degree of \(s\), \(t_j=s^jts^{-j}\), \(g=s^4\), \(M=PQ^{-1}\), \(W=M(t_1)M(t_0)\).
The [abelian quotient order bound](Yin_C_A0201_v1.md#consequence-for-finite-abelian-quotient-orders) implies \(H_{\rm ab}=C_{16}\) at a half kernel, since a larger finite abelianization would have order at least 32 and an infinite one has arbitrarily large cyclic quotients.
The four-coset condition follows by reduction modulo four.
The [quartic identity and periodic-image theorem](Yin_C_A0310_v1.md#statement) give regular pencils, invertible assembly, disjoint adjacent cyclic groups, \((s^{-1}M(t))^4=I\), and \(W^{-1}=s^{-2}Ws^{-2}\).
In \(F=\langle t_0,t_1,t_2,t_3\rangle=\ker(\chi\bmod4)\) the character \(\psi=\chi/4\) takes all \(t_j\) to one and \(g\) to \(a\) modulo four.

Here we detail the hypotheses needed for the pole reduction.
In the [middle subgroup cutoff and fold argument](Yin_C_A0314_v1.md#the-original-group-hypotheses-for-the-pole-estimates), the middle product belongs to a single coset over the intersection of the two adjacent-pair subgroups.
The fold theorem there recovers each adjacent pair as generators of \(F\), using trivial cyclic intersection, the quartic identity and the impossibility of a constant point correspondence for \(M\).
The latter follows from scalar injectivity and \(s\notin\langle t\rangle\).
The proof of the rotation tests in that section uses only the three independent coefficient matrices of \(P\,{\rm adj}\,Q\).
Thus \(F\) is nonamenable: otherwise its finite extension \(H\) would be amenable and the scalar Ore argument would give integer regular ranks.
The [pole-rank estimate](Yin_C_A0304_v1.md#statement) and the two-factor tail lower bound give the same maximal pole order on both sides when either side has a circle pole.
For example, boundedness of one side bounds its product, whereas a pole on the other side gives an unbounded product.
The order is one or two and the leading residues on a side of maximal order are square-zero of total rank at most one.

The [row and column compression and common-root proof](Yin_C_A0314_v1.md#the-boundary-poles-are-simple-unique-and-at-the-same-point) identifies their leading matrices up to scalar and their roots by the independence of the three coefficients of \(P\,{\rm adj}\,Q\).
Its exclusion of a shared double root uses an element reversing a power of \(s\) and the subgroup carrying powers of \(s\) to themselves or their inverses.
The only extra marking input is that a sign homomorphism positive on \(s\) is positive on \(t\).
This holds here since \(s\) generates \(H_{\rm ab}\).
Thus a singular case would have one common simple circle root \(\alpha\) and proportional residues of square zero.
Every circle determinant zero gives a genuine matrix pole: the numerator is injective on the kernel of its denominator by invertibility of the assembly.
A denominator vanishing as a matrix at a point would leave a pencil of at most two projectively independent matrices, giving a constant point correspondence.
These arguments verify the whole pole reduction at this marking without a numerical exclusion of the bounded case.

## The two geometric sequences of coefficients

Use the [common-residue coordinates](Yin_C_A0303_v1.md#a-matrix-entry-with-absolutely-summable-coefficients).
The residue is in direction \(e_{12}\), and \(h=M_{21}, f=M_{11}, j=M_{22}, m=\det M=p/q,\ w=h/m\) are regular on the circle.
Here \(\det Q=(z-\alpha)q,\ \det P=(z-\alpha)p\), and \(p,q\) have degree at most one and no circle zeros.
The functions \(h\) and \(w\) are nonconstant fractional linear functions with their zero at \(\alpha\).
In particular \(f=f_0+f_1 h,\ j=j_0+j_1 h\).
Both \(f_0\) and \(j_0\) are nonzero: if \(f_0=0\) the first column lies on a constant line, and if \(j_0=0\) the bottom row lies on a constant covector line so its constant kernel maps to the first coordinate line.
Either is a forbidden point correspondence.
The same reasoning for \(M^{-1}\) holds in the coordinate \(w\).

For the forward scalar entry \(L=W_{21}\) one obtains
\[
 L=f_0 h(t_1)+j_0 h(t_0)+(f_1+j_1)h(t_1)h(t_0).
\]
For \(L'=(W^{-1})_{21}\) the formula of the same type uses \(w(t_0),w(t_1)\), nonzero coefficients on both linear terms, and the reverse order in the product.
The product coefficient vanishes on the forward side exactly when \({\rm tr}M\) is constant and on the reverse side exactly when \({\rm tr}M^{-1}=({\rm tr}M)/m\) is constant.
All these entries have absolutely summable Fourier expansions.
The identity \(L'=s^{-2}Ls^{-2}\) is an exact coefficient-preserving bijection between their supported group elements.
Their degrees in \(F\) differ by \(-a\bmod4\), since conjugation by \(s^{-2}\) preserves \(\psi\).
Evaluating the same identity at the four characters \(\zeta^\psi\) gives
\[
 h(\zeta)\,{\rm tr}M(\zeta)\big(m(\zeta)^2+\zeta^a\big)=0
                         \qquad(\zeta^4=1).
\]
It follows in particular that \(m(z)=c z^k\) for \(k=0,1,-1\) forces \({\rm tr}M=0\).
Indeed \(2k-a\) is odd, so at most one of the four points satisfies the last factor; \(h\) vanishes at at most one and a nonzero trace at at most one.
The character is applied only to the regular scalar expressions above.

A nonconstant fractional linear function regular on the circle has either a single nonconstant coefficient at exponent \(1\) or \(-1\), or an infinite sequence \(D r^n\) at exponents \(\sigma n,\ n\ge1,\ \sigma=\pm1,\ 0<|r|<1\), with \(D\ne0\).
In the infinite case its only pole \(\gamma\) is finite and nonzero, and \(r=\gamma^{-1}\) for positive exponents or \(r=\gamma\) for negative exponents.
These statements follow by expanding the simple fraction on the circle.
All labels \(t_1^i t_0^j\) on the first side, and \(t_0^j t_1^i\) on the second, have unique exponent pairs by the trivial adjacent intersection.

Suppose one side uses an infinite sequence and has a nonzero product coefficient.
At every level \(n\ge2\) it has \(n-1\) distinct labels with two nonzero indices, the same coefficient \(D_1r^n\ne0\), and degree \(\sigma n\).
Every one-axis sequence on the other side has at most one index with that modulus, since its nonconstant coefficients are zero, a singleton, or a constant times a strictly decreasing geometric progression in modulus.
For all sufficiently large \(n\) a matching two-index label is necessary.
Consequently the other side also has an infinite sequence and a nonzero product coefficient.
Calling its parameters \(D_2,v,\tau\), there must be integers \(k(n)\) such that
\[
       D_1r^n=D_2v^{k(n)},\qquad \sigma n-a\equiv\tau k(n)\pmod4
\]
when the first side is forward.
The two-side conclusion allows starting with the forward side.
Taking moduli gives \(k(n)=bn+d\) with \(b=\log|r|/\log|v|>0\).
Since every sufficiently large consecutive integer \(n\) is used, \(b\) is a positive integer, and by the reverse comparison so is \(1/b\).
Hence \(b=1\).
Consecutive levels in the complex coefficient equality give \(r=v\); in the congruence they give \(\sigma=\tau\), since \(1\) and \(-1\) are distinct modulo four.
Thus the two pole locations coincide, so the linear denominator \(q\) of \(h\) is proportional to the linear denominator \(p\) of \(w\).
Now \(m\) is constant and the four-character test forces zero trace, contradicting the forward product coefficient.

## The remaining coefficients

On any infinite side the product coefficient is therefore zero.
Such a side has infinite support because both linear terms have nonzero coefficients and their nonconstant labels lie in disjoint cyclic groups.
A side with a singleton has finite support, so either both sides are infinite or both are singletons.
In the first case both \({\rm tr}M\) and \(({\rm tr}M)/m\) are constant.
If the trace were a nonzero constant, \(m\) would be constant and the four-character test would again give zero trace.
In the singleton case \(p,q\) are constant or scalar multiples of \(z\), so \(m=c z^k\) with \(k=0,1,-1\) and the same test applies.
Thus \({\rm tr}M=0\) in every remaining case.

With zero trace the entries are nonzero scalar multiples of \(h(t_1)-h(t_0)\) and \(w(t_1)-w(t_0)\), since \(j=-f\) and the analogous inverse trace is zero.
In the infinite case translate the coefficients at \(t_1^{\sigma n}\) by \(s^{-2}\) on both sides.
The resulting support containment puts each \(t_{-1}^{\sigma n}\) in \(\langle t_0\rangle g\) or \(\langle t_1\rangle g\).
At most one belongs to the former since \(\langle t_{-1}\rangle\cap\langle t_0\rangle=1\).
Consecutive exponents in the latter force \(t_{-1}\in\langle t_1\rangle\) and then \(g\in\langle t_1\rangle\).
Conjugation by \(s^{-1}\) puts \(g\) in \(\langle t_0\rangle\) as well, contradicting the infinite order of \(s\).
In the singleton case the degrees would give \(\sigma-a=\tau\bmod4\) for two signs \(\sigma,\tau\), impossible by parity.
This rules out any circle pole on either side.

## One bounded inverse on the range for every quotient

In the bounded case \(M,Q^{-1}\) are holomorphic on an annulus about the circle, so their cyclic Fourier coefficients are absolutely summable.
Put \(U=s^{-1}M(t)\).
The identity \(U^4=I\) holds in the matrix convolution algebra \(\ell^1(H)\) by faithfulness of its regular representation.
With \(E=(I+U+U^2+U^3)/4\) and \(T=(3I+2U+U^2)/4\), the telescoping identity \((I-U)T=T(I-U)=I-E\) gives
\[
 K=s(U-I)Q(t),\qquad X=-Q(t)^{-1}T s^{-1},\qquad KXK=K .
\]
This bounds the inverse from the range to the orthogonal complement of the kernel in any unitary representation: on the range, first use \(X\) and then project off the kernel.
The identity also makes \(KX\) a bounded idempotent onto the range, so that range is closed.
These conclusions persist under every pushforward of absolutely summable coefficients.

If \(J\) is a quotient retaining the character modulo four, its four sign and phase twists fixing the second mark and multiplying the first by every fourth root permute all four eigenspaces of the pushed-forward \(U\).
Each has trace dimension \(2/4\), since the polynomial idempotents decompose the two-dimensional affiliated module.
The invertible \(Q(t)\) identifies the fixed space with the kernel of the pushed-forward \(K\), also for a finite-order image of \(t\).

Finally, in the original group choose \(L>\|K\|^2\).
Closed range gives \(0<\rho<1\) with \(\|(I-K^*K/L)^j-p_K\|\le \rho^j\) for \(j\ge1\), by the spectral theorem.
This proves \(p_K\in M_2(C_r^*(H))\) and applies equally in every quotient above.
Each polynomial on the left before subtracting \(p_K\) has word propagation at most \(4j\), since each group site of \(K\) has length at most two.
The trace Hilbert norm of the difference is at most \(\sqrt 2\,\rho^j\), so the squared Fourier mass outside radius \(4j\) is at most \(2\rho^{2j}\).
Summing shells proves the stated exponential moment for every \(0<\eta<-\tfrac12\log\rho\), with weight \(e^{\eta |g|}\).

## Assessment history

### Decision closed-range-at-the-order-sixteen-marking

| Field | Value |
| --- | --- |
| date | 2026-11-26T16:23 |
| status | proved |
| reason | Equality forces circle-bounded invertible pencils, an absolutely summable range inverse and an exponentially summable squared kernel tail. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Equality forces circle-bounded invertible pencils, an absolutely summable range inverse and an exponentially summable squared kernel tail. |
| argument | [The possible singularity has one shared simple root](#the-possible-singularity-has-one-shared-simple-root) | The possible singularity has one shared simple root. |
| argument | [The two geometric sequences of coefficients](#the-two-geometric-sequences-of-coefficients) | The two geometric sequences of coefficients. |
| argument | [The remaining coefficients](#the-remaining-coefficients) | The remaining coefficients. |
| argument | [One bounded inverse on the range for every quotient](#one-bounded-inverse-on-the-range-for-every-quotient) | One bounded inverse on the range for every quotient. |
| review | [Closed range at the order-sixteen marking](../audits/reviews/Yin_R_A0220_v1.md#closed-range-at-the-order-sixteen-marking) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-closed-range-at-the-order-sixteen-marking)

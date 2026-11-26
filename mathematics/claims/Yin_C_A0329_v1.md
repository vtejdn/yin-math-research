---
author: Yin
---

# Three arbitrary spectral parameters of a fractional two-square transfer

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with scalar group-ring injectivity and let \(t\) have infinite order.
For regular complex two-square linear pencils \(P,Q\) put \(M=PQ^{-1}\) and \(U=s^{-1}M(t)\) in the regular affiliated algebra.
Suppose \(U\) has at least one eigenspace of noninteger trace dimension, using unnormalized coordinate trace.
Then for every nonzero scalar polynomial \(p\in\mathbb C[z]\) of degree at most three,
\[
                             {\rm rk}_H p(U)\ge1 .
\]
In particular the sum of the dimensions at any three distinct complex eigenvalues is at most one.
Repeated roots are allowed in the polynomial estimate, which also controls generalized eigenspaces.
No character and no count of window cosets is assumed.
For any fixed transfer with fractional spectrum, two distinct eigenspaces with dimensions summing to one leave no other eigenvalue of positive dimension.

## Clearing a quadratic and compressing a cubic

Neither marking can lie in the cyclic subgroup of the other, since all ranks there are integral.
A noninteger eigenspace has dimension in \((0,1)\), and its eigenvalue is nonzero since \(U\) is invertible.
Right multiplication by \(Q(t)\) identifies its dimension with the nullity of \(P(t)-\lambda sQ(t)\).
Thus the [four-site linearization](Yin_C_A0184_v1.md#the-four-group-elements-and-the-trace-bound) gives invertible assembly, and the [constant point test](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer) excludes a fixed line taken by \(M\) to a fixed line.
The same exclusion holds for \(M^{-1}\).
Every eigenspace has dimension at most one by the [two-position estimate](Yin_C_A0183_v1.md#statement).

Since \(U\) is a unit, factors \(z\) can be removed from \(p\) without changing rank.
Put \(t_i=s^its^{-i},\ M_i=M(t_i)\).
For a polynomial of degree two with leading coefficient one, \(s^2p(U)\) is a sum of \(M_1M_0,\ c_1sM_0,\ c_0s^2 I\).
Multiplying on the left by \(\det Q(t_1)\) and on the right by \(Q(t_0)\) produces a group-ring matrix.
Any nonzero such matrix has rank at least one because it has a nonzero scalar entry.
If the result is zero, \(p(U)=0\).
For two distinct roots their eigenspaces would sum directly to dimension two and hence each have dimension one, leaving no fractional eigenvalue.
For a repeated root \(\lambda\), the range of \(U-\lambda I\) would be contained in its kernel, forcing that kernel to have dimension at least one and thus exactly one.
The other shifts are units.
These contradictions prove the quadratic bound.
The linear case follows by multiplying by \(z\) to make a quadratic, and a nonzero constant gives rank two.

Suppose now
\[
                  p(z)=z^3+c_2 z^2+c_1 z+c_0,\qquad c_0\ne0 .
\]
Choose a nonzero constant row \(\ell\) and column \(v\) such that \(\ell M(z)v=a\in\mathbb C^\times\).
The [constant compression calculation](Yin_C_A0327_v1.md#an-exactly-polynomial-compression-of-the-cubic-remainder) applies here because modulo the one-dimensional span of \(\det Q\) the quadratic numerator has only two coefficient matrices, and some projective column makes their images dependent.
Zero constant value would contradict the point test.
Put \(r(z)=\ell M(z)^{-1}v\), which is nonzero by the inverse point test.

Left multiply \(s^3p(U)\) by \(M_2^{-1}\) and right multiply by \(M_0^{-1}s^{-3}\).
The identity \(s M_1=M_2s\) gives, after the indicated row and column compression,
\[
       a s^{-3}+c_2(\ell v)s^{-2}+c_1 r(t_2)s^{-1}
                       +c_0 \ell M_2^{-1}M_3^{-1}v .
                                                        \tag{1}
\]
If \(p(U)\) has rank less than one, so does this scalar.
Multiplication on the left by \(d(t_2)\) and on the right by \(d(t_3)\), \(d=\det P\), clears all its denominators into the group ring.
Therefore (1) is zero, by scalar injectivity.

## The trivial double coset

Write \(C_i=\langle t_i\rangle\).
First suppose \(C_2\cap C_3=1\).
In the cleared version of (1) retain only group elements of \(C_2C_3\).
The map \(z^i w^j\mapsto t_2^i t_3^j\) is injective on Laurent polynomials by uniqueness of the two indices.
The last term gives a polynomial tensor of rank two over \(\mathbb C\) because the two components of \(d(z)\ell M(z)^{-1}\) are linearly independent, and so are those of \(d(w)M(w)^{-1}v\).
A dependence on either side would give a constant point correspondence for \(M^{-1}\).
Two independent rows of coefficients paired with two independent columns have tensor rank two.

The term at \(s^{-j}\) can meet this product set only if \(s^{-j}\in C_2 C_3\), since all its group labels are in \(C_2s^{-j}C_3\).
If this happens for \(j=2\) or \(3\), its contribution is a single elementary tensor, obtained by substituting the unique two indices for \(s^{-j}\).
To exclude membership for \(j=1\), conjugate \(s^{-1}=t_2^i t_3^j\) by \(s^{-2}\) and then multiply by \(s\) on the right to get \(1=t^i s t^j\), contrary to \(s\notin\langle t\rangle\).
Consequently both \(s^{-2}\) and \(s^{-3}\) must belong to the product and \(c_2\ell v\ne0\) to account for the rank-two tensor.
All terms of the cleared identity except the one at \(s^{-1}\) are then supported in the product.
The latter term lies outside it, so \(c_1=0\), since \(r(t_2)\) and the clearing denominators are nonzero cyclic units.

Apply this same implication to the reciprocal transfer with marks \(s^{-1},t\), numerical matrix \(M^{-1}\), and polynomial \(z^3p(z^{-1})/c_0\).
Its evaluated transfer \(sM(t)^{-1}\) is similar to \(U^{-1}\).
Both the rank inequality and the fractional eigenspace hypothesis are preserved.
The reversed adjacent cyclics are disjoint as well.
The preceding argument requires the quadratic coefficient of the reversed polynomial to be nonzero, although it is \(c_1/c_0=0\).
This excludes all cubics in the disjoint case.

## Commensurable neighboring cyclics

If the adjacent cyclics intersect nontrivially the group commensurates \(\langle t\rangle\).
Its abelianization must be finite because a finitely generated infinite abelianization has cyclic quotients of unbounded order, and the [short character estimate](Yin_C_A0198_v1.md#the-lattice-of-all-finite-characters) would force the noninteger nullity at the chosen eigenvalue to vanish.
The absolute commensuration ratio on \(H\) is therefore trivial, and \(s\) normalizes \(\langle t^k\rangle\) for some \(k>0\), possibly by inversion.
All \(t_i\) centralize this subgroup.
For \(q=\det Q\) let \(q_*(z)=\prod_{\zeta^k=1}q(\zeta z)\).
For each \(i\), \(q_*(t_i)\) is a nonzero Laurent polynomial in \(t^k\) and clears the entries of \(M_i\).
In \(s^3p(U)\), move each displayed group shift to the right so that the other factors are products of \(M_i,\ 0\le i\le2\).
A product of the three clearing scalars (or their common product to the third power) clears the entire matrix on the left, since they commute with all \(M_i\).
Rank less than one now implies \(p(U)=0\).

Under this identity neither \(\det P\) nor \(\det Q\) is a Laurent monomial.
Indeed a monomial would make \(U\) or \(U^{-1}\) a group-ring matrix satisfying a scalar polynomial.
The fractional eigenvalue of that matrix has a polynomial idempotent onto its nonzero primary space by the Chinese remainder theorem.
For a single primary factor take the identity.
Multiply it by the highest power of the corresponding linear factor that is still nonzero there.
The resulting nonzero group-ring matrix has image in the actual eigenspace of dimension strictly less than one, contrary to a nonzero column having rank one.
This argument includes a nonsemisimple cubic and applies to \(U^{-1}\) using the reciprocal polynomial.

Take the image \(J=H/\langle t^k\rangle\), write \(x,y\) for the marked images, \(Y_i=\langle x^iyx^{-i}\rangle\), and reduce by the finite normal subgroup \(Z=Y_0\cap Y_1\).
Normality follows because all adjacent finite intersections have equal size and each is the unique subgroup of its size in either cyclic.
In \(\bar J=J/Z\), put \(n=|\bar Y_0|\), so neighboring cyclics meet trivially.
If \(n\ge2\), the diagonal regular twist into \(\bar J\times H\) separates first-coordinate labels in the identity
\[
              -c_0 M_2^{-1}M_3^{-1}
                  =M_1s^{-3}+c_2s^{-2} I+c_1 M_2^{-1}s^{-1}.
\]
The [two consecutive Fourier units](Yin_C_A0310_v1.md#two-consecutive-columns-in-an-arbitrary-periodic-image) apply to \(M^{-1}\), since it has invertible assembly, two nonmonomial determinants, and no point correspondence.
Every frequency block is nonzero, and two are rational units, including both blocks for \(n=2\).
The product on the left has at least \(2n\) distinct nonzero labels in \(\bar Y_2\bar Y_3\).
On the right the first two terms have at most \(n+1\) labels together.
The last term has labels in \(\bar Y_2\bar x^{-1}\), disjoint from \(\bar Y_2\bar Y_3\) because membership would put \(\bar x\) in \(\langle\bar y\rangle\), contradicting the trivial adjacent intersection for \(n\ge2\).
This is impossible since \(2n>n+1\).
If \(n=1\), the reduced group is generated by \(\bar x\) alone.
In the same diagonal twist of \(p(U)=0\) the constant and leading terms have nonzero coefficients at the two ends of the four consecutive powers of \(\bar x^{-1}\).
If \(\bar x\) had order greater than three or infinite order the four powers would be distinct.
Hence \(|\bar J|\le3\).
Since \(Z\) is finite, \(J\) is finite.
It follows that \(H\) is virtually cyclic, contradicting the fractional nullity by [Ore localization](Yin_C_A0211_v1.md#right-fractions-for-commensurable-amenable-subgroups).
This completes the rank estimate.
For distinct roots the kernel of the polynomial is the algebraic direct sum of the respective eigenspaces, proving the stated spectral count.

## Assessment history

### Decision three-arbitrary-spectral-parameters

| Field | Value |
| --- | --- |
| date | 2026-11-26T17:25 |
| status | proved |
| reason | A polynomial of degree at most three has rank at least one on a transfer with fractional spectrum. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A polynomial of degree at most three has rank at least one on a transfer with fractional spectrum. |
| argument | [Clearing a quadratic and compressing a cubic](#clearing-a-quadratic-and-compressing-a-cubic) | Clearing a quadratic and compressing a cubic. |
| argument | [The trivial double coset](#the-trivial-double-coset) | The trivial double coset. |
| argument | [Commensurable neighboring cyclics](#commensurable-neighboring-cyclics) | Commensurable neighboring cyclics. |
| review | [Three arbitrary spectral parameters](../audits/reviews/Yin_R_A0226_v1.md#three-arbitrary-spectral-parameters) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-three-arbitrary-spectral-parameters)

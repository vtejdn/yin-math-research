---
author: Yin
---

# Three cubic phases of a two-square transfer have total nullity at most one

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free and suppose every nonzero scalar in \(\mathbb CH\) acts injectively in the regular representation.
Suppose \(t\) has infinite order and \(s\notin\langle t\rangle\).
For regular complex two-square linear pencils \(P(z)=Az+B,\ Q(z)=Cz+D\) put \(M=PQ^{-1},\ U=s^{-1}M(t)\).
For every nonzero \(\lambda\in\mathbb C\) one has
\[
       \operatorname{rk}_H(U^3-\lambda I)\ge1,\qquad
       \sum_{\omega^3=\lambda}\dim_H\ker(U-\omega I)\le1 ,
\]
with the ordinary, unnormalized two-coordinate trace.
The three eigenspaces need not be actual character twists of one another for this inequality.

If \(H\) admits a character of order three taking \(s\) to a primitive cube root and \(t\) to one, every noninteger nullity of a two-square rectangle \(P(t)-sQ(t)\) is at most \(1/3\).
For every \(\epsilon>0\), at any such marking there is a finite marked neighborhood on which all torsion-free scalar-injective marked groups have their noninteger four-site nullities at most \(1/3+\epsilon\).
The neighboring groups need not retain that character.
In particular a half-dimensional rectangle, on any marks, requires that the quotient of \(H\) by the normal closure of either one of the marks have order at most two.

## An exactly polynomial compression of the cubic remainder

Rescale \(P\) by a nonzero scalar to take \(\lambda=1\) and suppose the cubic remainder has rank strictly less than one.
Polynomial interpolation on \(\ker(U^3-I)\) gives its decomposition as the algebraic direct sum of the three cube-root eigenspaces, whose total dimension exceeds one.
The [two-coset estimate](Yin_C_A0183_v1.md#transfer-matrices-and-equality) bounds each dimension by one.
If one has dimension one at \(\omega\), equality for \(\omega^{-1}M\) gives \(U^2=\omega^2 I\).
Of the three cube roots only \(\omega\) can then have a nonzero eigenspace, a contradiction.
Thus at least one eigenspace has positive noninteger dimension strictly below one.
The [four-column reduction](Yin_C_A0184_v1.md#statement) applied to \(P(t)-\omega s Q(t)\) gives an invertible assembly.
The [constant point correspondence test](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer) similarly excludes for \(M\) any fixed input line carried to a fixed output line.

There are a nonzero constant row \(\ell\), a nonzero constant column \(v\) and \(c\in\mathbb C^\times\) such that \(\ell M(z)v=c\).
To see this, write \(p=\det P,\ q=\det Q,\ N=P\,{\rm adj}\,Q\).
Project the polynomial entries of \(N\), each of degree at most two, to the two-dimensional vector space of polynomials of degree at most two modulo the linear span of the nonzero polynomial \(q\).
Choose a basis there and call its two numerical coefficient matrices \(N_1,N_2\).
The homogeneous quadratic \(\det[N_1v,\ N_2v]\) vanishes at some complex projective point \(v\), also when the quadratic is identically zero.
Choose a nonzero row annihilating both columns.
Then \(\ell N(z)v=c q(z)\) for a scalar \(c\).
If \(c=0\), the nonzero rational column \(M(z)v\) would belong to the fixed line \(\ker\ell\), forbidden above.

Put \(t_j=s^jts^{-j},\ g=s^3,\ M_j=M(t_j)\), and \(T=Q\,{\rm adj}\,P\), so \(M^{-1}=T/p\).
The ordered cubic remainder \(M_2M_1M_0-gI\) has the same rank as \(U^3-I\).
Multiplying on the left by \(M_2^{-1}\) and on the right by \(M_0^{-1}\) leaves \(M_1-M_2^{-1}gM_0^{-1}\).
Now multiply by \(p(t_2)\) on the left and \(p(t_0)\) on the right.
Applying \(\ell,v\) yields the single group-ring scalar
\[
                 c\,p(t_2)p(t_0)-\ell T(t_2)gT(t_0)v .
\]
It has rank strictly below one by the rank of the original remainder.
Scalar injectivity forces it to vanish.
Undoing just the exterior scalar denominators and moving \(g\) to the right gives the exact identity
\[
               \ell M(t_2)^{-1}M(t_3)^{-1}v=c\,g^{-1}.
\]
Thus although the original remainder is only assumed to have small rank, this one compression gives equality of affiliated scalars in the original group.

## Distinct cyclic factors and common powers

Write \(C_i=\langle t_i\rangle\).
Clear a Laurent denominator of the row \(\ell M(t_2)^{-1}\) on the left and one of the column \(M(t_3)^{-1}v\) on the right in the last identity.
A nonzero group-ring element then has support both in \(C_2 C_3\) and in \(C_2g^{-1} C_3\).
It is nonzero because the two exterior denominators and \(c\,g^{-1}\) are units in the affiliated algebra.
Consequently \(g^{-1}\in C_2 C_3\).

If \(C_2\cap C_3=1\), write \(g^{-1}=t_2^i t_3^j\).
The [injective two-variable tensor map](Yin_C_A0291_v1.md#local-fourier-blocks-and-separation-of-repeated-endpoints) now identifies the compressed identity with
\[
                 \ell M(z)^{-1}M(w)^{-1}v=c z^i w^j
                    \quad\text{in } \mathbb C(z)\otimes_{\mathbb C}\mathbb C(w).
\]
The independent-variable map here only uses opposite denominator clearing and the distinctness of the group elements \(t_2^a t_3^b\).
The two component functions of the row \(\ell M(z)^{-1}\) are linearly independent over \(\mathbb C\).
Otherwise its constant kernel line would be sent by \(M^{-1}\) into \(\ker\ell\), and a constant point correspondence for the inverse reverses for \(M\).
The two component functions of \(M(w)^{-1}v\) are also independent, by the same exclusion.
The tensor on the left has rank two because contraction with two independent dual coordinate functionals on its row span gives two independent column functions.
The right hand side is a nonzero elementary tensor.
This contradiction rules out trivial intersection.

If the intersection is nontrivial, \(\langle t\rangle\) and \(s\langle t\rangle s^{-1}\) are commensurable, by conjugating the adjacent pair.
Consequently all of \(H\) commensurates \(\langle t\rangle\).
For each \(x\in H\) the ratio \(b/a\) in a relation \(x t^a x^{-1}=t^b\) with \(ab\ne0\) is well defined, and these ratios give a homomorphism to \(\mathbb Q^\times\) by taking common exponent multiples.
It is one on \(t\) and its conjugates, hence on \(g^{-1}\in C_2 C_3\).
The cube of the ratio at \(s\) is therefore one, so the signed rational ratio at \(s\) is one.
Thus \(s\) centralizes a power \(t^d\), \(d>0\), which is central in \(H\).

Define the nonzero polynomial \(q_*(z)=\prod_{\zeta^d=1}q(\zeta z)\).
It is a polynomial in \(z^d\).
Hence \(q_*(t_j)=q_*(t)\) is the same central affiliated unit for all three factors.
Each \(q_*(t)M_j\) is a group-ring matrix by the adjugate formula.
Multiplying \(M_2M_1M_0-gI\) by \(q_*(t)^3\) consequently yields a group-ring matrix of rank less than one.
If nonzero, one of its entries would be a nonzero scalar of rank one, impossible.
Therefore \(U^3=I\).
The [cubic identity theorem](Yin_C_A0326_v1.md#statement) forces \(s\in\langle t\rangle\), contrary to the hypotheses.
This proves the remainder rank and total nullity assertions.

## Actual phases and the normal closure of a mark

At a fractional rectangle the reduction cited above makes both pencils regular over the cyclic field.
If \(t=1\), the generated group is cyclic and there is no noninteger nullity.
Otherwise the actual character of order three excludes \(s\in\langle t\rangle\).
Its trace-preserving twists give equal dimensions to all three cube-root eigenspaces, with the fixed space identified with the rectangle kernel by the invertible \(Q(t)\).
The total bound gives \(3\delta\le1\).
The three right cosets of \(\langle t_0,t_1\rangle\) at \(1,s,s^2\) are distinct by the character.
The [three-position upper semicontinuity theorem](Yin_C_A0307_v2.md#statement) now gives the finite marked neighborhood for any bound \(1/3+\epsilon\).

Finally the [four-position gap](Yin_C_A0325_v1.md#consequences-for-a-two-label-commutator-witness) already puts the index of the normal closure of either mark at most three at a half kernel, using the adjoint rectangle to exchange the marks.
An index of three gives an actual order-three character that kills this mark and takes the other to a primitive cube root.
The bound \(1/3\) excludes that case, leaving only indices one and two.

## Assessment history

### Decision three-phases-on-a-common-circle

| Field | Value |
| --- | --- |
| date | 2026-11-26T17:25 |
| status | proved |
| reason | Three cube-root eigenspaces with common cube have total dimension at most one, giving the one-third bound for an actual character. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Three cube-root eigenspaces with common cube have total dimension at most one, giving the one-third bound for an actual character. |
| argument | [An exactly polynomial compression of the cubic remainder](#an-exactly-polynomial-compression-of-the-cubic-remainder) | An exactly polynomial compression of the cubic remainder. |
| argument | [Distinct cyclic factors and common powers](#distinct-cyclic-factors-and-common-powers) | Distinct cyclic factors and common powers. |
| argument | [Actual phases and the normal closure of a mark](#actual-phases-and-the-normal-closure-of-a-mark) | Actual phases and the normal closure of a mark. |
| review | [Three phases on a common circle](../audits/reviews/Yin_R_A0226_v1.md#three-phases-on-a-common-circle) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-three-phases-on-a-common-circle)

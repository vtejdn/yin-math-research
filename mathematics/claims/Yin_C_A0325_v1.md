---
author: Yin
---

# A quartic two-square transfer has integral eigenspace dimensions

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free, with injective regular action for every nonzero scalar in \(\mathbb CH\).
Suppose \(t\) has infinite order and \(M(z)=P(z)Q(z)^{-1}\), where \(P,Q\) are regular complex two-square linear pencils.
Write \(U=s^{-1}M(t)\) in the affiliated algebra and use the unnormalized two-coordinate trace.
If \(U^4=I\), every eigenspace of \(U\) has integer dimension.
When \(s\notin\langle t\rangle\) there are exactly two nonzero eigenspaces, of dimension one each, at opposite roots, and \(U^2=I\) or \(U^2=-I\).

In particular suppose the four right cosets of \(K_4=\langle t,sts^{-1},s^2ts^{-2}\rangle\) represented by \(1,s,s^2,s^3\) are distinct.
Every four-site matrix \(K=B+At-s(D+Ct)\) with noninteger regular nullity then satisfies
\[
                              \dim_H\ker K<1/2 .
\]
There is a strictly positive gap below \(1/2\), uniform over coefficients and on a finite marked word neighborhood among torsion-free scalar-injective groups.
The same gap holds for the smaller support trace of rank-one two-label commutator outputs with ordinary input ranks at most two.
No residual finiteness, character, or prescribed abelian quotient is required.

## Recovering the finite support from the quartic identity

All assertions about fractional eigenspaces are automatic if \(s\in\langle t\rangle\), by reduction over \(\mathbb C(t)\).
Otherwise the two cosets of \(\langle t\rangle\) represented by \(1,s\) are distinct.
The [two-position bound and equality theorem](Yin_C_A0183_v1.md#transfer-matrices-and-equality) gives dimension at most one at every scalar eigenvalue.
If a fourth root \(\lambda\) has dimension one, equality applied to \(\lambda^{-1}M\) gives \(U^2=\lambda^2 I\), with the two opposite eigenspaces of dimension one.
Suppose this does not happen.
The four fourth-root spaces give an algebraic direct sum of dimension two, by interpolation in \(U^4=I\).
One therefore has dimension \(\delta\in[1/2,1)\).
Rescale \(P\) by the inverse of that root so this is the fixed space.
The matrix \(P(t)-sQ(t)\) has the same nullity \(\delta\).

We specify why the [finite-support reduction](Yin_C_A0322_v1.md#statement) can be used before imposing any four-coset hypothesis.
Its analytic inputs follow here from the quartic identity and this fractional eigenspace.
The [four-column linearization](Yin_C_A0184_v1.md#the-four-group-elements-and-the-trace-bound) gives an invertible four-square assembly at any noninteger rank; the [constant point test](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer) excludes a constant correspondence for \(M\).
Neither determinant is a Laurent monomial: otherwise \(U\) or \(U^{-1}\) is a group-ring matrix, and the polynomial projection onto its fixed space contains a nonzero group-ring column of rank one in dimension \(\delta<1\).
Put \(t_i=s^its^{-i}\), \(g=s^4\), and \(W=M(t_1)M(t_0)\).
The quartic identity gives \(W^{-1}=s^{-2}Ws^{-2}\) and \(g\in F=\langle t_0,t_1,t_2,t_3\rangle\) by Fourier support.
Consequently \(F\) is normal with cyclic quotient of order dividing four.

In these conditions the [two consecutive Fourier columns](Yin_C_A0310_v1.md#two-consecutive-columns-in-an-arbitrary-periodic-image) and the [finite count](Yin_C_A0310_v1.md#counting-and-lifting-the-two-cyclic-subgroups) apply in every image where \(t\) is periodic.
Those arguments use the actual quartic identity, the two nonmonomial determinants, invertible assembly, absence of a constant point correspondence and the infinite order of the original \(t\).
They make the image of \(F\) a finite product of cyclic subgroups, hence the entire image finite.
In particular the adjacent cyclics in \(H\) intersect trivially: otherwise the absolute commensuration ratio of \(\langle t\rangle\) is one on all \(t_i\) and on \(s^4\), so \(s\) normalizes a nontrivial power subgroup of \(t\).
Killing it gives a finite quotient by the periodic-image conclusion and makes \(H\) virtually cyclic.
This contradicts noninteger nullity by the [amenable Ore argument](Yin_C_A0211_v1.md#right-fractions-for-commensurable-amenable-subgroups).

The [middle cut and fold](Yin_C_A0320_v1.md#checking-the-hypotheses-for-the-fourier-level-sets) now give \(F=\langle t_i,t_{i+1}\rangle\) for every \(i\), using the quartic identity, disjoint adjacent cyclics and absence of a constant correspondence.
This group is nonamenable as it has finite index in \(H\).
These are all the group and pencil inputs of the [bounded coefficient level-set argument](Yin_C_A0318_v1.md#statement), the [common double pole exclusion](Yin_C_A0322_v1.md#the-common-double-root-case-without-a-sign-restriction), and the [two-axis reduction at a simple circle pole](Yin_C_A0322_v1.md#a-simple-boundary-pole-leaves-only-finite-fourier-supports-in-the-compression).
In particular the finite support derived in those arguments needs neither a further character nor the individual dimensions of the other three eigenspaces.

More explicitly, for a common finite nonzero simple root \(\alpha\) one has
\(\det P=c_1z^a(z-\alpha),\ \det Q=c_2z^b(z-\alpha)\), with \(a,b\in\{0,1\}\).
In the basis of the common nilpotent residue write \(f=M_{11},\ h=M_{21},\ j=M_{22},\ m=\det M\).
Set \(\sigma=1\) when \(b=0\), and \(\sigma=-1\) when \(b=1\).
All three entries \(f,h,j\) are affine in \(z^\sigma\), and \(h=H_1(z^\sigma-\alpha^\sigma)\) with \(H_1\ne0\).
The values \(f(\alpha),j(\alpha)\) are both nonzero: otherwise the first column or the second row would give a constant point correspondence.
In the bounded case these formulas also follow directly by cancelling the common residue in the three entries and using \(\det M\) regular nonzero at the root, as in the same reduction.
The determinant is \(m(z)=c z^{e\sigma}\) with \(e=0\) or \(1\).

## Matching the two actual supports

Put \(x=t^\sigma,\ y=sxs^{-1},\ q=s^2\).
Define complex coefficients \(a_{ij}\) for \(i,j\in\{0,1\}\) by the two-variable expansion of \(h(z_1)f(z_0)+j(z_1)h(z_0)\) in \(z_1^{i\sigma}z_0^{j\sigma}\).
Let \(S\) be their nonzero index set.
Substituting \(z_0=\alpha\) leaves \(h(z_1)f(\alpha)\ne0\), so \(S\) is nonempty.
By the two-by-two inverse formula,
\[
 W_{21}=\sum_{(i,j)\in S}a_{ij}y^i x^j,\qquad
 (W^{-1})_{21}=-c^{-2}\sum_{(i,j)\in S}a_{ij}x^{j-e}y^{i-e}.
\]
The coefficients in the two polynomials are the same before the common scalar, since each is a sum of products of complex coefficients in opposite orders.
These formulas use only the regular entries of the two factors even if the upper right entries have a circle pole.
The products have no internal label collisions on either side by \(\langle x\rangle\cap\langle y\rangle=1\).
Thus the middle identity gives equality of two ordinary finite sets:
\[
       \{q^{-1}y^ix^j q^{-1}:(i,j)\in S\}
                =\{x^{j-e}y^{i-e}:(i,j)\in S\}.
\]

Suppose \(e=1\).
Write \(b_0=s^{-1}\), \(b_1=s^{-1}x\).
For any matched pair multiply the equality of its labels on the right by \(q\).
The resulting equation is
\[
                 b_i b_j=(b_{1-i'}b_{1-j'})^{-1}.
\]
Indeed \(b_i b_j=q^{-1}y^i x^j\).
This gives a positive relation of length four on \(b_0,b_1\), which generate \(H\).
Any such relation in a torsion-free group on two generators makes the group amenable.
Four equal letters make one generator trivial.
Three equal letters express the other as a power.
Two occurrences of each give, up to cyclic permutation, either \((b_0b_1)^2=1\) or \(b_0^2b_1^2=1\).
In the latter case the common subgroup generated by \(b_0^2=b_1^{-2}\) is central with quotient generated by two involutions, hence virtually cyclic in the quotient.
All these alternatives contradict the nonamenability of \(H\).

It remains that \(e=0\).
The constant coefficient \(a_{00}\) must vanish.
Otherwise \(s^{-4}\) would be one of \(1,x,y,xy\).
The first three possibilities force \(s\) trivial or \(t\) to be a power of \(s\), since \(s^{-4}\) is fixed by conjugation by \(s\).
In the last possibility \((xs)^2=s^{-2}\); the generators \(xs,s\) again have a common central square up to inversion and generate an amenable group.

Write \(f=f_c+f_1 z^\sigma,\ j=j_c+j_1 z^\sigma\).
Since \(h\) has nonzero constant coefficient, \(a_{00}=0\) gives \(j_c=-f_c\).
Direct expansion then gives \(a_{10}=-H_1j(\alpha)\ne0,\ a_{01}=-H_1 f(\alpha)\ne0\).
Thus the left support contains both \(q^{-1}xq^{-1}\) and \(q^{-1}yq^{-1}\).
The right support is \(\{x,y\}\) or \(\{x,y,xy\}\), with the third label present on both sides exactly when \(a_{11}\ne0\).
Consider the image \(l=q^{-1}xq^{-1}\); the image of the adjacent label is \(sls^{-1}\).

* If \(l=x\), then \(t\) conjugates \(s^2\) to \(s^{-2}\). The [reversed-square obstruction](Yin_C_A0324_v1.md#statement) excludes the chosen fractional nullity \(\delta\ge1/2\).
* If \(l=y\), its conjugate is \(z=qxq^{-1}\), equal to \(x\) or \(xy\) since the two images are distinct. If \(z=x\), then \(q\) commutes with \(x\) and \(y=xq^{-2}\), so \(x,y\) commute. This contradicts the nonamenability of their subgroup. If \(z=xy\), the equality \(x=qyq\) gives \(z=q^2 y\), hence \(q^2=x\), contradicting the disjoint adjacent cyclics.
* If \(l=xy\), the three-point supports are present. Its conjugate is \(yz\) and must be \(x\) or \(y\); the latter forces \(z=1\). Thus the image of the second label is \(x\) and the remaining label satisfies \(q^{-1}yxq^{-1}=y\). Multiplying the two known images with \(q^2\) between them gives \(y=x q^2 x y\). Hence \(q^2=x^{-2}\), a nontrivial power of \(x\) fixed by conjugation by \(s\), again contradicting \(\langle x\rangle\cap\langle y\rangle=1\).

This rules out the selected eigenspace and proves the quartic assertion.

## Consequences for a two-label commutator witness

For four distinct cosets the [window bound and equality theorem](Yin_C_A0183_v1.md#transfer-matrices-and-equality) give \(\delta\le1/2\) at noninteger nullity, since both pencils are regular there.
Equality would give \(U^4=I\) with all four eigenspaces of dimension \(1/2\), which has just been excluded.
The [attainment and upper semicontinuity theorem](Yin_C_A0307_v2.md#the-supremum-and-the-four-coset-gap) gives the asserted uniform marked neighborhood, and the [support-trace equivalence](Yin_C_A0308_v1.md#statement) transfers the gap to the rank-one outputs.

In particular a half-dimensional rectangle on any marking requires that three consecutive conjugates \(t_i,t_{i+1},t_{i+2}\) generate the normal closure of \(t\), with cyclic quotient of order at most three.
Indeed some \(s^k\), \(1\le k\le3\), belongs to \(K_4\).
Then \(t_3=s^k t_{3-k}s^{-k}\) and \(t_{-1}=s^{-k}t_{k-1}s^k\) also lie in \(K_4\), proving normality and the index bound.
If there is a sign character negative on \(s\) and positive on \(t\), already each consecutive pair generates its kernel.
The sign twist makes both the \(+1\) and \(-1\) eigenspaces of \(U\) have dimension \(1/2\).
Their direct sum is the fixed space of \(U^2=s^{-2}W\), of dimension one.
If \(s^2\notin\langle t_0,t_1\rangle\), the two-position equality for this transfer and shift \(s^2\) would give \(U^4=I\), an impossibility here.
Hence \(s^2\) belongs to that pair, which is normal by adjoining its forward and backward conjugates as above, and has the asserted index two by the sign.
Taking the adjoint rectangle gives the corresponding statements for the other marked generator.

## Assessment history

### Decision matching-the-four-finite-coefficient-labels

| Field | Value |
| --- | --- |
| date | 2026-11-26T16:50 |
| status | proved |
| reason | The quartic identity forces integral eigenspaces; equality at four cosets and half-sized rank-one commutator supports is excluded. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The quartic identity forces integral eigenspaces; equality at four cosets and half-sized rank-one commutator supports is excluded. |
| argument | [Recovering the finite support from the quartic identity](#recovering-the-finite-support-from-the-quartic-identity) | Recovering the finite support from the quartic identity. |
| argument | [Matching the two actual supports](#matching-the-two-actual-supports) | Matching the two actual supports. |
| argument | [Consequences for a two-label commutator witness](#consequences-for-a-two-label-commutator-witness) | Consequences for a two-label commutator witness. |
| review | [Matching the four finite coefficient labels](../audits/reviews/Yin_R_A0223_v1.md#matching-the-four-finite-coefficient-labels) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-matching-the-four-finite-coefficient-labels)

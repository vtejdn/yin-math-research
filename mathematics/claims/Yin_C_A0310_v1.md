---
author: Yin
---

# Periodic images and residual finiteness at a four-coset half kernel

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free and assume every nonzero element of \(\mathbb CH\) acts injectively in its regular representation.
Set \(t_j=s^jts^{-j}\) and \(K=\langle t_0,t_1,t_2\rangle\).
Suppose the four right cosets \(Ks^i\), \(0\le i<4\), are distinct and a complex two-by-two matrix \(B+At-s(D+Ct)\) has regular nullity \(1/2\), with unnormalized matrix trace.
For every homomorphism of \(H\) write \(J\) for its image, \(x,y\) for the images of \(s,t\), and \(Y_j=\langle x^jyx^{-j}\rangle\).
If \(y\) has finite order \(m\), let \(Z=Y_0\cap Y_1\).
Then \(Y_1Y_0\) is a normal metabelian subgroup of \(J\) of order \(m^2/|Z|\), and its quotient is cyclic of order dividing four.
In particular all such \(J\) are finite, of derived length at most three, and have order at most \(4m^2/|Z|\).

Consequently the third derived subgroup \(H^{(3)}\) is nontrivial and is contained in the kernel of every such homomorphism.
This excludes a half kernel on a residually finite marked group satisfying the four-coset condition.
In the original group the adjacent infinite cyclic groups \(\langle t_i\rangle,\langle t_{i+1}\rangle\) must intersect trivially.
A character to \(\mathbb Z/4\) taking \(s\) to a generator and \(t\) to zero suffices for the coset condition.
For each \(k\ge1\) the actual quotient \(H/\langle\!\langle t^k\rangle\!\rangle\) has order at most \(4k^2\).

## The quartic identity in the original group

The [four-site rank reduction](Yin_C_A0184_v1.md#statement) gives infinite order for both marks, an invertible assembled coefficient block and regular pencils \(P(z)=Az+B,\ Q(z)=Cz+D\).
Define \(M=PQ^{-1}\) and \(U=s^{-1}M(t)\).
The [four-coset endpoint](Yin_C_A0183_v1.md#transfer-matrices-and-equality) gives \(U^4=I\), with each fourth-root eigenspace of dimension \(1/2\).
In particular
\[
  M(t_3)M(t_2)M(t_1)M(t_0)=s^4I.
\]
The left side is affiliated over \(F=\langle t_0,t_1,t_2,t_3\rangle\), so Fourier support gives \(s^4\in F\).
Conjugating the first or last generator by \(s^{-1}\) or \(s\) uses \(t_{-1}=s^{-4}t_3s^4\) and \(t_4=s^4t_0s^{-4}\).
Thus \(F\) is normal with cyclic quotient of order dividing four.

If \(\det Q\) is a Laurent monomial, \(U\) is a group-ring matrix.
The nonzero group-ring idempotent \((I+U+U^2+U^3)/4\) then has a nonzero column in a half-dimensional module.
Some coordinate of that column is an affiliated unit by scalar injectivity, so the column generates a module of dimension one.
Applying the same argument to \(U^{-1}=M(t)^{-1}s\) rules out a Laurent monomial for \(\det P\).
In either pair of coefficient matrices neither member can be zero, and at least one is invertible, by the constant and quadratic terms of the two-by-two determinant.
Also \(s\notin\langle t\rangle\), so the [constant point correspondence test](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer) rules out any constant input line taken to a constant output line by \(M\).

## Two consecutive columns in an arbitrary periodic image

The finite cyclic groups \(Y_j\) have the same order.
Each neighboring intersection has the same cardinality and is the unique subgroup of that cardinality in either cyclic group.
Thus \(Z\) is normal under \(x,y\), lies in every \(Y_j\), and the adjacent cyclic groups in \(\bar J=J/Z\) intersect trivially.
Use bars for all images in this quotient and let \(n=|\bar y|=m/|Z|\).
If \(n=1\), the image of \(F\) is trivial in \(\bar J\), so the image of \(F\) in \(J\) equals \(Y_0=Z\) and the claimed quotient follows.
Suppose \(n\ge2\).

Embed \(H\) diagonally in \(\bar J\times H\) using its given quotient and the identity.
Regular inclusion along a subgroup preserves the affiliated identity by decomposition into cosets.
For a primitive \(n\)-th root \(\omega\), set \(E_j(z)=n^{-1}\sum_{l=0}^{n-1}\omega^{-jl}M(\omega^l z)\).
Then the twisted factor at \(t_a\) is \(\sum_j\bar y_a^j E_j(t_a)\), where \(\bar y_a=\bar x^a\bar y\bar x^{-a}\).
Moving the two leftmost factors of the quartic product to the right-hand side gives the ordered equality
\[
 M(t_1)M(t_0)=M(t_2)^{-1}M(t_3)^{-1}s^4.
\]
In its diagonal image the possible first coordinates on the right lie in \(\mathcal P=\bar Y_2\bar Y_3\bar x^4\).
Those on the left have unique indices by the trivial adjacent intersection.
Equality of the finite expansions can be checked at each first coordinate even for infinite \(\bar J\): take a common right denominator for the finitely many affiliated coefficients in the second coordinate, then take ordinary Fourier coefficients in the first.
It follows that \(E_a(t_1)E_b(t_0)\ne0\) implies \(\bar y_1^a\bar y_0^b\in\mathcal P\).

Here every \(E_j\) is nonzero and two consecutive indices are units over \(\mathbb C(z)\).
To see this with \(D\) invertible, set \(T=D^{-1}C,\ V=A-BT\), so \(V\) is a unit and \(M=BD^{-1}+Vz(I+zT)^{-1}D^{-1}\).
For invertible \(T\), every nonzero frequency has invertible leading coefficient, while
\[
 E_0(z)D(I-(-zT)^n)=B+(-1)^{n-1}z^n A T^{n-1}
\]
is invertible by its constant or highest coefficient.
This includes \(n=2\).
For rank-one \(T\), its trace is nonzero by the nonmonomial determinant.
The [rank-one Taylor calculation](Yin_C_A0280_v1.md#which-finite-frequencies-must-contribute) gives invertible \(E_1\) and nonzero \(E_j\) for all \(2\le j<n\).
It gives \(E_0=L+f(z)R\) with constant \(L\), rank-one \(R\), and nonconstant \(f\).
A singular \(E_0\) forces \(L,R\) to have a common kernel or common image and hence forces the excluded constant point correspondence, as in the same calculation.
If \(D\) is singular, interchange the corners by parameter inversion, replacing indices \(0,1\) by \(0,-1\).
Evaluation at each original infinite-order translation preserves rational ranks.
Hence for two consecutive indices \(i,i+1\), both entire columns \(\bar Y_1\bar y_0^i,\bar Y_1\bar y_0^{i+1}\) belong to \(\mathcal P\).

## Counting and lifting the two cyclic subgroups

Left multiplication by \(\bar Y_2\) preserves \(\mathcal P\).
Both this set and \(\bar Y_2\bar Y_1\) have cardinality \(n^2\) since adjacent intersections are trivial.
For \(D_0=\bar Y_2\bar Y_1\) the two inclusions therefore give \(D_0\bar y_0^i=\mathcal P=D_0\bar y_0^{i+1}\).
Thus \(D_0\) is invariant on the right by \(\bar Y_0\) and by \(\bar Y_1\).
It contains the identity, so it contains \(A_0=\langle\bar Y_0,\bar Y_1\rangle\), which already contains the \(n^2\) elements of \(\bar Y_1\bar Y_0\).
It follows that \(A_0=D_0=\bar Y_1\bar Y_0\), and \(\bar x A_0\bar x^{-1}\subseteq A_0\) is equality by finite cardinality.
All conjugates of \(\bar Y_0\) now belong to \(A_0\), which equals the image of \(F\).

The image of \(F\) in \(J\) contains \(Z\) and is the full inverse image of \(A_0\).
Since \(Z\subseteq Y_0,Y_1\), this inverse image equals \(Y_1Y_0\) as a set.
Its cardinality is \(m^2/|Z|\), and it is metabelian by [Itô's theorem on products of abelian subgroups](https://doi.org/10.1007/BF01180647).
The cyclic quotient of \(H/F\) gives the claimed index and derived length.

## The obstruction in the original group

If \(H\) were amenable, scalar injectivity and [Ore localization](Yin_C_A0211_v1.md#right-fractions-for-commensurable-amenable-subgroups) would give integer matrix ranks.
In particular \(H\) is not solvable, so \(H^{(3)}\ne1\).
The calculation in every periodic image kills this subgroup, and all finite images are among the periodic ones.
This proves the assertion on residual finiteness.

Suppose an adjacent cyclic intersection is nontrivial, and conjugate it to the pair at \(0,1\).
Then \(H\) commensurates \(\langle t\rangle\).
The absolute ratio \(|b/a|\) for \(h t^a h^{-1}=t^b\) with \(ab\ne0\) is a multiplicative homomorphism \(H\to\mathbb Q_{>0}\), by comparing common powers.
It is one on \(t\), on its conjugates and hence on \(s^4\in F\).
Its value on \(s\) is therefore one, so \(st^k s^{-1}=t^{\pm k}\) for some \(k>0\).
The cyclic group \(\langle t^k\rangle\) is normal and the periodic-image result makes its quotient finite.
This would make \(H\) virtually cyclic and amenable, which was excluded.

## Assessment history

### Decision images-with-one-periodic-mark

| Field | Value |
| --- | --- |
| date | 2026-11-26T15:56 |
| status | proved |
| reason | The complete consecutive columns force a normal product of two finite cyclic groups and a cyclic quotient of order dividing four. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The complete consecutive columns force a normal product of two finite cyclic groups and a cyclic quotient of order dividing four. |
| argument | [The quartic identity in the original group](#the-quartic-identity-in-the-original-group) | The quartic identity in the original group. |
| argument | [Two consecutive columns in an arbitrary periodic image](#two-consecutive-columns-in-an-arbitrary-periodic-image) | Two consecutive columns in an arbitrary periodic image. |
| argument | [Counting and lifting the two cyclic subgroups](#counting-and-lifting-the-two-cyclic-subgroups) | Counting and lifting the two cyclic subgroups. |
| argument | [The obstruction in the original group](#the-obstruction-in-the-original-group) | The obstruction in the original group. |
| review | [Images with one periodic mark](../audits/reviews/Yin_R_A0219_v1.md#images-with-one-periodic-mark) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-images-with-one-periodic-mark)

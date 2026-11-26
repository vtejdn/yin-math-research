---
author: Yin
---

# A cubic two-square transfer forces the shift to be the cyclic label or its inverse or the identity

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with injective regular action for every nonzero scalar of \(\mathbb CH\), and let \(t\) have infinite order.
Let \(P(z)=Az+B,\ Q(z)=Cz+D\) be regular complex two-square linear pencils, put \(M=PQ^{-1}\), and evaluate them at the group translation \(t\) in the regular affiliated algebra.
If \(U=s^{-1}M(t)\) satisfies \(U^3=I\), then
\[
                             s=t^k,\qquad k\in\{-1,0,1\}.
\]
These are exactly the shifts admitting such a cubic identity for some pair of regular pencils.
In particular the regular dimensions of the three eigenspaces of any such \(U\) are integers, using the unnormalized two-coordinate trace.
Rescaling \(P\) gives the same restriction when \(U^3\) is an arbitrary nonzero scalar multiple of the identity.

If instead the three right cosets of \(\langle t,sts^{-1}\rangle\) represented by \(1,s,s^2\) are distinct, every four-site matrix \(B+At-s(D+Ct)\) of noninteger regular nullity has nullity strictly below \(2/3\).
At each such marking the gap below \(2/3\) can be chosen uniformly over all coefficients and on a finite marked word neighborhood among torsion-free scalar-injective groups.

## A two-factor product over a cyclic coset

Suppose \(s\notin\langle t\rangle\).
The [two-position estimate](Yin_C_A0183_v1.md#transfer-matrices-and-equality) bounds the dimension of every scalar eigenspace of \(U\) by one.
If a cube root \(\lambda\) has dimension one, equality for \(\lambda^{-1}M(t)\) gives \(U^2=\lambda^2 I\).
The cubic identity then gives \(U=\lambda^{-2}I\), putting \(s\) in \(\langle t\rangle\) by Fourier support.
All three root spaces therefore have dimension less than one.
Their dimensions sum to two by polynomial interpolation, so each dimension is strictly positive and noninteger.
In particular \(P(t)-sQ(t)\) has noninteger nullity \(\delta\in(0,1)\).
The [four-column reduction](Yin_C_A0184_v1.md#the-four-group-elements-and-the-trace-bound) gives an invertible assembled block, and the [constant line test](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer) rules out every fixed input line that \(M\) maps to a fixed output line.
The two determinants \(\det P,\det Q\) cannot be Laurent monomials.
If one were, then \(U^{-1}\) or \(U\), respectively, would be a group-ring matrix.
Cubic interpolation onto its nonzero fixed space would give a nonzero group-ring column there, generating a submodule of dimension one because some coordinate is a nonzero regularly injective scalar.

Write \(t_i=s^its^{-i}\), \(C_i=\langle t_i\rangle\), \(g=s^3\), \(F=\langle t_0,t_1,t_2\rangle\).
The ordered identity \(M(t_2)M(t_1)M(t_0)=gI\) gives \(g\in F\) by Fourier support.
The subgroup \(F\) is normal, since \(t_3=g t_0g^{-1}\) and \(t_{-1}=g^{-1}t_2g\), and \(H/F\) is cyclic of order dividing three. [Ordered product cut](Yin_C_A0186_v1.md#cutting-the-ordered-product)

First assume \(C_0\cap C_1=1\).
Set \(A_0=\langle t_1,t_0\rangle\), \(J=A_0\cap C_2\), and \(W=M(t_1)M(t_0)=M(t_2)^{-1}g\).
The [bounded-transform cut](Yin_C_A0188_v1.md#regular-fourier-support-of-the-cut) gives a factorization \(g=b a\), \(b\in C_2,\ a\in A_0\), and \(W a^{-1}\in {\rm GL}_2(U(J))\).
Indeed the bounded transform has a nonzero Fourier coefficient at an element \(a\in A_0\cap C_2 g\), and the matrix \(W a^{-1}\) and its inverse then belong to both affiliated subgroup algebras.

The [two-factor fold theorem](Yin_C_A0272_v1.md#statement) applies to \(x=t_1,y=t_0,\ L=R=M\).
Its rotation condition follows from the same [coefficient comparison](Yin_C_A0314_v1.md#the-original-group-hypotheses-for-the-pole-estimates) for any regular two-square linear transfer without constant point correspondence.
Explicitly, the three coefficients of \(N=P\,{\rm adj}\,Q\) are independent, since a matrix span of dimension at most two can be normalized at an invertible value and then has a common constant eigenline.
Hence the entries of \(N\) have no common nonconstant factor.
A rotation \(M(\eta z)=M(z)D_0\) of order \(r\ge2\) gives \(D_0^r=I\), and \(N(\eta z)\) and \(N(z)D_0\) must differ by a nonzero constant since their polynomial entries are primitive.
In an eigenbasis for \(D_0\), each column has degrees in a single residue class modulo \(r\).
For \(r\ge3\) a column thus has just one degree and gives a constant point correspondence.
For \(r=2\) distinct eigenvalues leave one column odd, again with just one degree, while equal eigenvalues leave at most two independent coefficients.
This excludes the required right-matrix rotations, including all scalar rotations on the other factor.
The fold gives \(A_0=J\subset C_2\).
Two nontrivial subgroups \(C_0,C_1\) of the same infinite cyclic group cannot have trivial intersection.
This contradiction treats this branch even if the rational functions have poles on the unit circle.

## Intersecting cyclics and the single complete Fourier column

Suppose now \(C_0\cap C_1\ne1\).
Then \(s,t\) commensurate \(\langle t\rangle\).
The [absolute power-ratio homomorphism](Yin_C_A0310_v1.md#the-obstruction-in-the-original-group) is one on every \(t_i\) and hence on \(g=s^3\in F\), so it is one on \(s\).
Consequently \(s t^d s^{-1}=t^{\pm d}\) for some \(d>0\), and \(\langle t^d\rangle\) is normal in \(H\).

We show that any group image \(G\) in which \(t\) has finite order is finite.
Write \(x,y\) for the marked images, \(y_i=x^iyx^{-i}\) and \(Y_i=\langle y_i\rangle\).
The intersections \(Y_i\cap Y_{i+1}\) all have the same cardinality.
Uniqueness of a subgroup of that cardinality inside each finite cyclic \(Y_i\) makes them the same subgroup \(Z\), normal under \(x,y\).
The adjacent cyclics in \(\bar G=G/Z\) have trivial intersection; write bars for their images and \(n=|\bar Y_0|\).
If \(n\ge2\), for a primitive \(n\)-th root \(\omega\) write
\[
                     E_j(z)=\frac1n\sum_{l=0}^{n-1}\omega^{-jl}M(\omega^l z),
                      \qquad 0\le j<n .
\]
Every \(E_j\) is nonzero and at least one is a unit over \(\mathbb C(z)\).
Here is a direct verification, including \(n=2\).
Nonmonomiality of the two determinants implies \(A,B,C,D\) are nonzero, and at least one member of each pair \(A,B\) and \(C,D\) is invertible by the two extreme determinant coefficients.
When \(D\) is invertible set \(T=D^{-1}C,\ V=A-BT\).
The assembly gives \(V\) invertible and
\[
              M(z)=BD^{-1}+Vz(I+zT)^{-1}D^{-1}.
\]
The constant term \(BD^{-1}\) makes \(E_0\ne0\).
For \(1\le j<n\) the coefficient of \(z^j\) in \(E_j\) is \(V(-T)^{j-1}D^{-1}\), nonzero because \(\det(I+zT)\) is nonconstant and \(T\) has a nonzero eigenvalue.
In particular \(E_1\) is invertible by its leading coefficient.
For \(D\) singular, \(C\) is invertible and the same proof for \(M(z^{-1})=(Bz+A)(Dz+C)^{-1}\) gives all frequencies nonzero and a unit at \(-1\bmod n\).
Reflection of the parameter preserves rational ranks.
Thus the two-frequency case also gives one whole column, without requiring the zero frequency to be a unit.

Embed \(H\) diagonally in \(\bar G\times H\).
Regular inclusion preserves its affiliated identity, including at possible poles, since a nonzero Laurent polynomial of an infinite-order original translation is an affiliated unit.
The finite Fourier expansion of \(M(t_i)\) in the diagonal image has coefficients \(E_j(t_i)\) at the first coordinates \(\bar y_i^j\); the corresponding expansion for the inverse uses \(M^{-1}\).
This is finite cyclic spectral decomposition in the first coordinate. [Diagonal regular twist and comparison](Yin_C_A0310_v1.md#two-consecutive-columns-in-an-arbitrary-periodic-image)
Coefficients with distinct first coordinates are independent even when \(\bar G\) is infinite: one common right denominator in the group von Neumann algebra of the second factor turns the finitely many affiliated coefficients into bounded ones, to which the first-factor Fourier coefficient maps apply.

Choose a unit frequency \(b\).
In \(M(t_1)M(t_0)\) all first coordinates \(\bar y_1^j\bar y_0^b\) occur with nonzero coefficient \(E_j(t_1)E_b(t_0)\), because these products have unique index pairs by the trivial adjacent intersection.
On the other side \(M(t_2)^{-1}g\) has possible first coordinates in \(\bar Y_2\bar x^3\).
Consequently \(\bar Y_1\bar y_0^b\subseteq\bar Y_2\bar x^3\).
Both cosets have size \(n\), so they coincide and their left stabilizers give \(\bar Y_1=\bar Y_2\).
Their intersection is trivial, contradicting \(n\ge2\).
Therefore \(Y_0=Y_1=Z\) is a normal finite cyclic subgroup of \(G\); all conjugates of \(Y_0\) are this subgroup and the quotient has order dividing three by \(g\in F\).
In particular \(H/\langle t^d\rangle\) is finite.
This makes \(H\) virtually cyclic, and scalar injectivity and [amenable Ore localization](Yin_C_A0211_v1.md#right-fractions-for-commensurable-amenable-subgroups) would give integer ranks, contradicting the fractional fixed space.

## The cyclic possibilities and the three-position gap

We have shown \(s\in\langle t\rangle\).
Write \(s=t^k\).
Faithfulness of evaluation on the infinite cyclic subgroup gives
\[
             \big(z^{-2k}\det M(z)\big)^3=1
                         \quad\text{in }\mathbb C(z).
\]
The parenthesis is a constant cube root of unity, so \(\det P=c z^{2k}\det Q\).
The orders at zero of the two nonzero determinant polynomials both belong to \(\{0,1,2\}\); their difference is \(2k\), proving \(|k|\le1\).
The eigenspaces have integer dimension by elimination over \(\mathbb C(t)\) and regular subgroup inclusion.
Conversely \(M(z)=I,zI,z^{-1}I\), respectively, are obtained as quotients of regular linear pencils and give \(U=I\) for \(s=1,t,t^{-1}\).

For noninteger rectangle nullity the [four-column reduction](Yin_C_A0184_v1.md#singular-cyclic-blocks) gives regular pencils.
The [three-position bound](Yin_C_A0183_v1.md#statement) gives \(\delta\le2/3\), with equality forcing \(U^3=I\).
The shifts just classified are incompatible with three distinct cosets, excluding equality.
The [attainment and upper semicontinuity theorem](Yin_C_A0307_v2.md#statement) then gives the strict uniform local gap: a positive supremum is attained, and near a limiting group every upper limit of these suprema is at most its supremum.

## Assessment history

### Decision the-cubic-shift-and-the-three-coset-endpoint

| Field | Value |
| --- | --- |
| date | 2026-11-26T16:50 |
| status | proved |
| reason | The cubic identity forces one of three actual cyclic shifts, so three distinct window cosets give a strict local gap below two thirds. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The cubic identity forces one of three actual cyclic shifts, so three distinct window cosets give a strict local gap below two thirds. |
| argument | [A two-factor product over a cyclic coset](#a-two-factor-product-over-a-cyclic-coset) | A two-factor product over a cyclic coset. |
| argument | [Intersecting cyclics and the single complete Fourier column](#intersecting-cyclics-and-the-single-complete-fourier-column) | Intersecting cyclics and the single complete Fourier column. |
| argument | [The cyclic possibilities and the three-position gap](#the-cyclic-possibilities-and-the-three-position-gap) | The cyclic possibilities and the three-position gap. |
| review | [The cubic shift and the three-coset endpoint](../audits/reviews/Yin_R_A0223_v1.md#the-cubic-shift-and-the-three-coset-endpoint) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-cubic-shift-and-the-three-coset-endpoint)

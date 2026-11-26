---
author: Yin
---

# Abelianization of the neighboring two-generator subgroup at cyclic order twenty-four

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular scalar group-ring injectivity, and let \(\chi:H\twoheadrightarrow C_{24}\) have marks \(3,4\).
Write \(t_i=s^its^{-i}\), \(F=\ker(\chi\bmod4)\), and \(A=\langle t_0,t_1\rangle\).
If a two-by-two four-site rectangle \(B_0+A_0t-s(D+Ct)\) has regular rank \(3/2\), then
\[
       \langle t_0\rangle\cap\langle t_1\rangle=\{1\}
                \quad\Longrightarrow\quad A_{\rm ab}\text{ is finite}.
\]
This finite abelianization maps onto \(C_6\) under \(\chi/4\).
In particular a neighboring free pair cannot support the proposed half nullity, and the same exclusion holds for a pair with disjoint cyclic groups and any infinite abelianization of its generated subgroup.
The argument applies to singular transfers with unit-circle poles.

More precisely, if the transfer identities for a half-nullity rectangle hold and \(A\) has an integer character nonzero on both generators, disjointness of their cyclic groups forces
\[
        A=\langle t_0,t_1\rangle\cap\langle t_2,t_3\rangle=F .
\]
If a character vanishes on exactly one of the two generators, this equality requires no disjointness assumption.
In the order-24 problem, \(F\) has finite abelianization by the [index-four reduction](Yin_C_A0252_v1.md#the-promislow-group-and-the-index-four-subgroup), so either equality contradicts the specified character.

## Two factors in a single subgroup coset

Put \(B=\langle t_2,t_3\rangle\), \(J=A\cap B\), \(g=s^4\), and \(M(z)=(A_0z+B_0)(Cz+D)^{-1}\).
The [four-step equality and middle cut](Yin_C_A0240_v1.md#the-four-step-product-and-its-middle-factors) give \(F=\langle A,B\rangle\), \(g=ba\) with \(b\in B,\ a\in A\), and
\[
                         W a^{-1}\in{\rm GL}_2(U(J)),\qquad
                         W=M(t_1)M(t_0).
\]
The rational matrix \(M\) is generically invertible.
It has a primitive projective numerator of degree at most two: divide the entries of \((A_0z+B_0)\operatorname{adj}(Cz+D)\) by their common polynomial gcd.
There are no nonzero constant vectors \(c,d\) with \(M(z)c\) in the constant line \(\mathbb C(z)d\), since that would give integer regular rank by the [constant point correspondence criterion](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer).
The inverse and transpose have the same two properties.
For the inverse, use the adjugate of the primitive two-by-two numerator and reverse the correspondence.
For the transpose, a correspondence would give fixed covectors whose kernels are lines mapped into one another by \(M\).

We use a consequence for any of these rational matrices, denoted by \(T\).
For a primitive \(d\)-th root \(\xi\), \(d\ge2\), it is impossible to have \(T(\xi z)=T(z)D_0\) with \(D_0\) an invertible constant matrix.
Indeed \(D_0^d=I\), so diagonalize \(D_0\) in a constant input basis.
If \(P(z)\) is the primitive projective numerator in this basis, \(P(\xi z)\) and \(P(z)D_0\) are proportional over \(\mathbb C(z)\), and the scalar of proportionality must be constant by primitivity on both sides.
Each column polynomial therefore has degrees confined to a single residue class modulo \(d\).
If \(d\ge3\), each column contains at most one degree and gives a constant point correspondence.
For \(d=2\) with distinct eigenvalues, one of the two columns uses odd degrees only, hence just degree one.
If \(d=2\) with equal eigenvalues, the entire numerator uses just one parity and its coefficient span has dimension at most two.
Normalizing this span by the inverse of an invertible value of \(P\) gives a common eigenvector, again a constant point correspondence.

## Scaling both generators in the double over the intersection

Let \(\beta:A\to\mathbb Z\) have \(b_i=\beta(t_i)\ne0\) for \(i=0,1\).
It is not necessary for \(\beta\) to extend to \(F\).
Form \(A*_J A\), and use superscripts to indicate its two group embeddings.
Its two copies of \(W a^{-1}\) agree over the affiliated algebra since both come from \(U(J)\).
The character \(\beta\) on each copy extends to the double by the amalgam property.
Thus for \(|z|=1\) the two copies of
\[
             W_z a^{-1}=M(z^{b_1}t_1)M(z^{b_0}t_0)a^{-1}
\]
agree by the unitary character twist, after removing the common scalar \(z^{-\beta(a)}\).

Their equality extends to every \(z\ne0\) by the [polynomial rank argument for ordered products](Yin_C_A0187_v1.md#extending-the-unitary-twists).
For detail, write \(M=P_0/h\) with a polynomial matrix and a common nonzero polynomial denominator.
In each copy solve the two equations with initial vector \(a^{-1}v\),
\[
 h(z^{b_0}t_0)u=P_0(z^{b_0}t_0)a^{-1}v,\qquad
 h(z^{b_1}t_1)y=P_0(z^{b_1}t_1)u .
\]
Use the same \(v\) in both copies and impose equality of the two output vectors \(y\).
All displayed scalar denominators are affiliated units for every \(z\ne0\), by infinite order of \(t_i\).
The kernel of the combined polynomial system, after clearing negative scalar powers, therefore has dimension at most two and has dimension two at every unit phase.
The [finite-evaluation rank inequality](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) bounds the rank at any nonzero \(z\) by the common rank at arbitrarily many unit phases, giving kernel dimension two everywhere.
Thus all initial vectors give equal outputs in the affiliated module at every such parameter.

Choose a sufficiently small positive \(z\) for which each factor has an absolutely convergent Laurent expansion on its scaled circle, from the expansion at zero if \(b_i>0\) and at infinity if \(b_i<0\).
Both copies of \(W_z a^{-1}\) are now bounded.
The two copies of \(A\) intersect in \(J\) by amalgam normal form, and an element of both group von Neumann algebras has Fourier support in \(J\).
In particular \(W_z\) has Fourier support in \(J a\).
This argument only specializes bounded group-ring polynomials before the two denominators are justified; it uses no homomorphism from \(U(F)\) to a quotient.

## Which differences of exponents generate the cyclic factors

Assume \(\langle t_0\rangle\cap\langle t_1\rangle=\{1\}\).
Write \(X_i\) for the Laurent coefficients used for the left copy of \(M\) and \(Y_j\) for those used for the right copy, with their original integer exponents.
The words \(t_1^i t_0^j\) are distinct for different pairs by triviality of the intersection.
Their coefficients in \(W_z\) are \(z^{b_1 i+b_0 j} X_iY_j\).
Hence \(X_iY_j\ne0\) implies \(t_1^i t_0^j\in J a\).

The subgroup of \(\mathbb Z\) generated by the differences \(i-i'\) with \(X_iY_j,X_{i'}Y_j\ne0\) for some common \(j\) is all of \(\mathbb Z\).
If it were proper, choose a prime \(d\) dividing all differences, including the case when all differences are zero.
For each \(j\), its active left indices lie in a single class modulo \(d\).
If all nonzero \(X_i\) already lie in one class, then \(M(\xi z)\) equals a constant scalar times \(M(z)\), contrary to the rotation exclusion above for a primitive \(d\)-th root \(\xi\).
Otherwise choose nonzero \(X_i,X_{i'}\) in different classes.
For every \(j\), at least one of them annihilates \(\operatorname{im}Y_j\).
The images of all \(Y_j\) span \(\mathbb C^2\) because the right matrix is generically invertible.
Therefore \(\ker X_i,\ker X_{i'}\) are distinct lines and both lines occur as images of nonzero \(Y_j\).
For each such line \(V\), the indices \(a\) with \(X_a V\ne0\) then all belong to one residue class \(r_V\).
For a basis consisting of one vector from each line, the two columns of \(M(\xi z)\) are the respective columns of \(M(z)\) multiplied by \(\xi^{r_V}\); this is first an identity of Laurent expansions and then a rational identity.
This gives the prohibited constant right multiplier and proves the claim.

Taking quotients of the two words in \(Ja\) with a common \(j\) puts \(t_1^{i-i'}\) in \(J\), hence \(t_1\in J\).
Apply the same difference assertion to the reversed transpose coefficients \(Y_j^{\mathsf t},X_i^{\mathsf t}\) of the two expansions of \(M^{\mathsf t}\).
The differences \(j-j'\) of active right indices with a common \(i\) also generate \(\mathbb Z\).
The corresponding word quotients put \(t_1^i t_0^{j-j'}t_1^{-i}\) in \(J\), and now \(t_1\in J\) gives \(t_0\in J\).

## When only one generator is scaled

Suppose \(\beta(t_1)\ne0\), \(\beta(t_0)=0\).
For every unit scalar \(\lambda\), twisting \(A\) preserves \(U(J)\) and gives \(M(\lambda t_1)M(t_0)a^{-1}\in{\rm GL}_2(U(J))\).
Dividing two such matrices gives \(M(\lambda t_1)M(\mu t_1)^{-1}\) over \(U(J\cap\langle t_1\rangle)\).
If the intersection is proper, choose a nontrivial root of unity \(\xi\) whose rotation fixes that subgroup's Fourier algebra; the trivial intersection permits any such root.
The rational identity for every \(\lambda,\mu\) on the circle is
\[
 M(\lambda \xi z)M(\mu \xi z)^{-1}
                         =M(\lambda z)M(\mu z)^{-1}.
\]
It follows that \(M(z)^{-1}M(\xi z)\) is invariant under all rotations of \(z\), hence is constant.
The rotation exclusion therefore proves \(t_1\in J\).

It now follows that \(M(t_0)a^{-1}\in{\rm GL}_2(U(J))\).
Its bounded transform, after moving \(a^{-1}\) to the right of the bounded transform of \(M(t_0)\), exhibits a nonempty intersection of \(\langle t_0\rangle\) with \(Ja\).
For \(t_0^h\in Ja\), the matrix \(M(t_0)t_0^{-h}\) belongs to \(U(J\cap\langle t_0\rangle)\).
If that intersection is proper, invariance under some nontrivial finite rotation gives \(M(\xi z)=\xi^h M(z)\), again impossible.
Thus \(t_0\in J\).
If only \(t_0\) has nonzero weight, use \(W^{-1}=M(t_0)^{-1}M(t_1)^{-1}\), the subgroup \(a^{-1}Ja\), and the right coset representative \(a^{-1}\): one has \(W^{-1}a\in{\rm GL}_2(U(a^{-1}Ja))\).
The same argument with \(M^{-1}\) gives \(a^{-1}Ja=A\), hence \(J=A\).

In all the stated cases, \(J=A\) implies \(A\subseteq B\), and \(g=ba\) belongs to \(B\).
Conjugation \(\phi=\operatorname{Ad}(s^2)\) gives \(B=\phi(A)\subseteq\phi(B)=gAg^{-1}\subseteq B\).
Therefore \(A=B=F\).
The group \(A\) is finitely generated, so infinite \(A_{\rm ab}\) would furnish a nonzero integer character.
This proves the assertion.

## Assessment history

### Decision neighboring-groups-with-disjoint-cyclic-subgroups

| Field | Value |
| --- | --- |
| date | 2026-11-26T13:10 |
| status | proved |
| reason | Independent review verified the applicable double, safe parameter continuation, Laurent support and both weight cases. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The necessary finite abelianization and its sixth-order quotient. |
| argument | [Two factors in a single subgroup coset](#two-factors-in-a-single-subgroup-coset) | The middle coset and the exclusion of constant rotational correspondences. |
| argument | [Scaling both generators in the double over the intersection](#scaling-both-generators-in-the-double-over-the-intersection) | Character extension to the double, polynomial continuation and Fourier separation. |
| argument | [Which differences of exponents generate the cyclic factors](#which-differences-of-exponents-generate-the-cyclic-factors) | The exceptional kernel-line configuration and the transposed argument. |
| argument | [When only one generator is scaled](#when-only-one-generator-is-scaled) | One-weight variations, the inverse product and closure of the subgroup cut. |
| review | [Neighboring groups with disjoint cyclic subgroups](../audits/reviews/Yin_R_A0205_v1.md#neighboring-groups-with-disjoint-cyclic-subgroups) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-neighboring-groups-with-disjoint-cyclic-subgroups)

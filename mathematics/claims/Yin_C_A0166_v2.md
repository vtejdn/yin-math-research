---
author: Yin
---

# Finite-rank commutator boundaries with two or three rank-one summands

## Statement

Let \(G\) be torsion-free and suppose every nonzero element of \(B=\mathbb CG\) acts injectively in its regular representation.
Such an element is a unit in the finite affiliated algebra \(U=\mathcal U(G)\).
On \(H=\ell^2(G)\) write \(\rho_s v=vs\) and consider \(F=\sum_s[\rho_s,T_s]\), with each \(T_s\) of finite complex rank.
Use the [rank-one boundary criterion](Yin_C_A0157_v1.md#statement) for the complex strong Atiyah problem.
The identity label can be discarded and each inverse pair can be combined into one orientation, since
\[
 [\rho_{s^{-1}},T]=-[\rho_s,\rho_{s^{-1}}T\rho_{s^{-1}}].
\]
This operation can only decrease the total complex witness rank \(k=\sum_s\operatorname{rank}_{\mathbb C} T_s\).
Retain only nonzero entries and use pairwise distinct labels up to inverse.

1. If the active labels generate a cyclic subgroup, \(F\) cannot have complex rank one, for any \(k\).
   If there are two active labels of ranks \(r,1\), with \(r\ge1\), again \(F\) cannot have rank one.
   Consequently all witnesses of total rank at most two are excluded.
2. At total rank three the only case still requiring consideration has three active labels \(s,t,u\) of rank one.
   If \(F\) has rank one, at least one side of the tensor decomposition has its six endpoints spanning a three-dimensional space.
   On that side the three distinct endpoint planes are either concurrent in a line or have three distinct pairwise intersection lines.
   None of the pairwise intersection lines can be an endpoint line of either incident plane.
   Every pair of labels must freely generate a free group of rank two.
   Moreover the subgroup \(K=\langle s,t,u\rangle\) admits no character \(K\to\mathbb Z\) vanishing on two labels and nonzero on the third.
3. On a three-dimensional side, after taking adjoints on a second tensor leg, write \(s,t,u\) for its right translation labels, inverted if necessary.
   In the concurrent case there exist nonconstant scalar fractional linear functions \(f_s,f_t,f_u\) such that
   \(f_s(s)+f_t(t)-f_u(u)\) has a nonzero left annihilator in \(U\).
   In the case of three distinct intersections the same conclusion holds for \(f_s(s)f_t(t)-f_u(u)\).
   For every such pair of functions the two-label sum and the two-label product separately have the property that subtracting any scalar gives an affiliated unit.
   The remaining third-label comparison is a necessary condition, with no general exclusion asserted when the character test fails.

## Endpoint dimensions and a cyclic chain

Use the identification of finite-rank operators with tensors under which
\(\Theta(v\otimes w)\xi=v\tau(w\xi)\) and the commutator acts by \(v s\otimes w-v\otimes s w\).
A minimal rank decomposition of \(T_s\) uses vectors \(v_{si},w_{si}\) independent on each side within that label.
Let \(a\) be the dimension of the span of all \(v_{si},v_{si}s\), and let \(b\) be that of all \(w_{si},s w_{si}\).
Taking adjoints of the second list turns it into right translations by \(s^{-1}\).
Factoring the boundary through the \(2k\) signed tensor terms and applying the ordinary rank inequality gives
\[
                    \operatorname{rank}_{\mathbb C}F\ge a+b-2k.
\]
In detail the first leg maps \(\mathbb C^{2k}\) onto a space of dimension \(a\), and the second leg supplies a map of rank \(b\) into that coordinate space. The signs and the order of endpoint pairing constitute an invertible signed permutation.

For any nonidentity \(s\), right translation by \(s\) has no nonzero finite-dimensional invariant subspace in \(H\).
Indeed its powers on each left coset of \(\langle s\rangle\) give a bilateral shift.
Thus \(\dim(E+Es)\ge\dim E+1\) for any nonzero finite-dimensional \(E\subset H\).
If \(\dim E=r\) and equality holds, then \(E=v\operatorname{span}_{\mathbb C}(1,s,\ldots,s^{r-1})\) for some \(v\ne0\).
For \(r=1\) this follows from the definition.
For \(r>1\), \(V=E\cap Es^{-1}\) has dimension \(r-1\), and \(V+Vs\subseteq E\) has dimension at least \(r\).
It equals \(E\), and induction applied to \(V\) gives the stated chain.

If all active labels lie in a cyclic subgroup, decompose \(H\) over its left cosets.
Every nonzero rank-one boundary would have a nonzero rank-one block between two of these cosets.
Transport both cosets by left translations to the subgroup to obtain a finite-rank commutator witness on that cyclic group.
The rank-one exclusion there follows from the [division-ring characterization](Yin_C_A0157_v1.md#rank-one-commutator-sums-on-one-fixed-marking) and the ordinary rational function field for the infinite cyclic group, or from the trivial commutator for the trivial subgroup.
One may include a cyclic generator with zero witness.

For two labels of ranks \(r,1\), let \(s\) carry the \(r\)-dimensional first-leg space \(E\) and suppose \(t\notin\langle s\rangle\).
If the first-leg endpoint span has dimension at most \(r+1\), the preceding equality case gives
\(E+Es=v\operatorname{span}(1,s,\ldots,s^r)\).
Both legs \(w,wt\) of the other edge on this side then lie in that space, so \(w=vp(s)\ne0\) and \(wt=vq(s)\).
The group-ring element \(p(s)t-q(s)\) is nonzero because its two terms have disjoint coset supports and \(p(s)\ne0\).
It cannot annihilate \(v\) on the right, by scalar injectivity and invertibility in \(U\).
Thus \(a\ge r+2\).
The same reasoning with adjoints gives \(b\ge r+2\), so the boundary has rank at least two.
The case \(t\in\langle s\rangle\) has already been treated.

## Shared endpoints and lifting a leg into the group ring

Here is a sufficient condition at arbitrary \(k\).
Suppose all first endpoints lie in \(vB\) for a fixed nonzero \(v\in U\), including both ends of every translated pair.
The map \(B\to vB,\ c\mapsto vc\) is complex-linearly injective because every nonzero \(c\in B\) is a unit in \(U\).
Lifting the first endpoint vectors along its inverse makes the boundary a tensor in \(B\otimes_{\mathbb C}H\).
If that boundary had rank one, its lift would be \(a\otimes w\) with nonzero \(a\in B,w\in H\).
Multiplication in \(U\) of each lifted balancing difference is zero because the lifts of a pair are \(c,cs\), by injectivity and associativity.
Consequently \(aw=0\), a contradiction.
The adjoint version holds if all right-translated vectors from the second leg belong to one such \(vB\), since after taking adjoints and interchanging tensor legs each difference becomes the negative of a balancing difference for the inverse label.
In particular one can start from the plane of a single rank-one edge and attach edges in a tree whenever an endpoint of each new edge belongs to the existing span.
Its other endpoint is obtained by a group element or its inverse, so the entire resulting span lies in \(vB\).

For three distinct labels, no two first-leg planes can coincide.
If the planes for \(s,t\) coincide, the two endpoints \(w,wt\) for \(t\) lie in \(v\operatorname{span}(1,s)\), and \(v[(\alpha+\beta s)t-\gamma-\delta s]=0\) with \((\alpha,\beta)\ne(0,0)\).
The four words \(1,s,t,st\) are distinct since \(s,t\) are nonidentity and distinct up to inverse.
Scalar injectivity gives a contradiction.
The same holds for the second-leg planes after adjoints.
Both endpoint dimensions are therefore at least three. If both were at least four the rank inequality would exclude rank one.
On a three-dimensional side two distinct planes already span the entire space.
If their intersection line were an endpoint of either plane, start with the other plane and attach this edge by that endpoint.
The resulting whole endpoint space lies in \(vB\), giving the preceding exclusion.

## A group relation gives two binomials a common left multiple

Suppose a pair of nonidentity labels \(s,t\), distinct up to inverse, does not freely generate its subgroup \(J\).
For any two nonzero affine polynomials \(D_s(s),D_t(t)\) there are \(p,q\in\mathbb CJ\) with
\[
                   pD_s(s)=qD_t(t)\ne0 .
\]
Indeed the unoriented, two-colored Cayley graph of \(J\) has a finite simple cycle, since a nonempty reduced word representing the identity yields a closed walk without backtracking.
Each unoriented edge has exactly one chosen orientation \(g\longrightarrow gs\) or \(g\longrightarrow gt\), by torsion-freeness and the restriction on the two labels.
The infinite group \(J\) has a left translate of the finite cycle disjoint from it, by avoidance of a finite difference set.
Join the cycles by a shortest connecting path.
Their union with that path is a finite connected graph with more edges than vertices.

Map the complex vector space on those edges into the space on their vertices by sending an oriented edge of color \(j\in\{s,t\}\) based at \(g\) to \(gD_j(j)\), the indicated linear combination of its two endpoints.
The dimension inequality gives a nonzero kernel vector.
Collecting its coefficients by color and changing one sign yields \(pD_s(s)=qD_t(t)\).
The chosen orientation makes the basepoints distinct within each color.
If this common value were zero, injectivity of right multiplication by either nonzero denominator in \(U\) would give \(p=q=0\), contradicting the choice of edge coefficients.
The dimension argument allows arbitrary nonzero endpoint weights, including unequal weights around a cycle, without a character condition on those weights.
It also covers a monomial denominator.

Now take any two of the three planes on a three-dimensional side with rank-one boundary, and take a nonzero \(z\) on their intersection line.
There are nonzero denominators \(D_s,D_t\) and affine numerators \(N_s,N_t\) so that these planes together span
\[
            z\operatorname{span}_{\mathbb C}
            (1,D_s(s)^{-1}N_s(s),D_t(t)^{-1}N_t(t)).
\]
For example \(z=v_sD_s(s)\) in the first plane, and \(v_sN_s(s)\) may be chosen independently of \(z\) there.
If their pair fails to generate freely, take a nonzero common left multiple \(m\) just constructed.
Multiplying each of the three displayed coefficients on the left by \(m\) gives a group-ring element, by the two factorizations of \(m\).
The whole endpoint space therefore lies in \((zm^{-1})B\).
Here \(zm^{-1}\) is a nonzero affiliated element, which suffices for the preceding group-ring lift.
This contradicts rank one.
The labels for a second-leg calculation are the inverses of the original labels. Independent inversion of the generators of an abstract free group does not affect the free-pair test.
Thus the argument applies to every pair of active labels on either tight side.

## The three planes and a character test

Write the three planes on the selected side as \(v_g\operatorname{span}(1,g)\) with \(g=s,t,u\).
For any two independent points \(z,z'\) in such a plane there is an identity \(z'=z f_g(g)\) in \(U\), where \(f_g=N_g/D_g\) is fractional linear with independent affine numerator and denominator.
Indeed the points are obtained from the independent coefficient polynomials \(D_g,N_g\), and the denominator is a nonzero group-ring scalar.
In the concurrent case choose \(z\ne0\) on the common line and \(z'_g\) in the respective planes independent of \(z\).
The three distinct lines of their images in the two-dimensional quotient modulo \(z\) give a linear dependence with all three coefficients nonzero.
After scaling and adding a scalar constant to one of the fractional linear functions, this reads
\(z(f_s(s)+f_t(t)-f_u(u))=0\).
In the other case take successive pairwise intersection points \(z_0,z_1,z_2\) around the triangle.
They satisfy \(z_1=z_0f_s(s),\ z_2=z_1f_t(t),\ z_2=z_0f_u(u)\), giving the product relation.

Put \(A=f_s(s)+f_t(t)\) or \(A=f_s(s)f_t(t)\).
For each \(\lambda\in\mathbb C\), left multiplication of \(A-\lambda\) by \(D_s(s)\) and right multiplication by \(D_t(t)\) gives an element of \(\mathbb CK\) supported on \(\{1,s,t,st\}\).
To see that this polynomial is nonzero, use the bases \((D_s,N_s)\) and \((D_t,N_t)\) of the two affine polynomial spaces. The corresponding tensors are respectively
\(N_s\otimes D_t+D_s\otimes N_t-\lambda D_s\otimes D_t\) and \(N_s\otimes N_t-\lambda D_s\otimes D_t\).
Multiplication on this tensor product is injective by the distinctness of the four group elements.
Thus every \(A-\lambda\) is an affiliated unit, in \(U(K)\) as well as \(U(G)\), using the regular coset inclusion.

Suppose there is a character on \(K\) as stated and relabel so that it detects \(u\).
The concurrent description and the cyclic ordering or reversal of the triangle allow any chosen label to play this role.
Write \(f_u(X)=(c+dX)/(e+fX)\) with independent affine numerator and denominator.
The expression \(A-f_u(u)\), multiplied on the right by the denominator, becomes
\[
                    (eA-c)+(fA-d)u .
\]
Both coefficients are affiliated units, since each is a nonzero constant or a nonzero multiple of \(A-\lambda\).
Character twists of the canonical trace representation fix \(A\) and vary \(u\) through \(zu\) for every \(|z|=1\), preserving affiliated rank.
For the two units \(C=eA-c\) and \(D=(fA-d)u\), the pencil \(C+zD\) is invertible outside a countable set of complex parameters because the distinct scalar eigenmodules of \(D^{-1}C\) form an algebraic direct sum over each finite set, so only countably many can have positive dimension.
Full rank of this square affiliated scalar is equivalent to being a unit.
Hence the trace-preserving twists make \(C+D\) a unit as well.
The required nonzero annihilator in \(U(G)\) cannot occur, proving the character test.
This argument uses only the smaller group \(K\) for twisting, even if its character does not extend to \(G\).

The [first version](Yin_C_A0166_v1.md#shared-endpoints-and-lifting-a-leg-into-the-group-ring) treated a common endpoint by lifting a leg into one group-ring copy.
The two disjoint cycles supply the common multiple for the general nonfree pair and give the additional pairwise freeness condition.

## Assessment history

### Decision small-commutator-witnesses

| Field | Value |
| --- | --- |
| date | 2026-11-26T03:35 |
| status | proved |
| reason | Independent review verified the complete statement and argument at the specified scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Small total ranks, the two-label mixed-multiplicity case and the remaining three-label conditions. |
| argument | [Endpoint dimensions](#endpoint-dimensions-and-a-cyclic-chain) | Two spans, extremal chain and rank inequality. |
| argument | [Lifting endpoints](#shared-endpoints-and-lifting-a-leg-into-the-group-ring) | Pulling a leg into the group ring and preserving its tensor rank. |
| argument | [Common left multiple](#a-group-relation-gives-two-binomials-a-common-left-multiple) | Weighted edges and two disjoint cycles. |
| argument | [Three configurations and characters](#the-three-planes-and-a-character-test) | Projective incidence, fractional linear functions and the phase test. |
| review | [Small commutator witnesses](../audits/reviews/Yin_R_A0174_v1.md#small-commutator-witnesses) | Independent whole-argument finding on this fixed version. |

## Current assessment

[Selected decision](#decision-small-commutator-witnesses)

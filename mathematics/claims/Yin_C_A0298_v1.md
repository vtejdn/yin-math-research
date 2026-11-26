---
author: Yin
---

# Three conjugates at order twenty-five and small-dimensional invariant subspaces at both orders

## Statement

Under the [cyclic order-25 or order-26 half-rank hypotheses](Yin_C_A0201_v1.md#statement), take the normalized degrees \((1,7)\) or \((1,10)\), respectively.
At order 25 every three consecutive conjugates \(t_j=s^jts^{-j}\) generate \(H\).
The same assertion holds with the two marks interchanged.
At order 26 every consecutive pair generates the [normal subgroup of index two](Yin_C_A0296_v1.md#statement).

Let \(H\to{\rm PGL}(V)\) be a representation on a finite-dimensional vector space over any field, let \(X,Y\) be lifts of the two marks and put \(r=\operatorname{rank}(Y-I)>0\) for any scalar choice of \(Y\).
There is a nonzero invariant subspace of dimension at most \(3r\) at order 25 and at most \(2r\) at order 26, on whose quotient space the projective image is cyclic if the quotient space is nonzero.
Thus these are dimension bounds for every irreducible such representation.
At order 25 either mark can be used for \(r\).

In particular suppose a quotient \(A_d,\ d\ge5\), sends \(t\) to a single three-cycle or a double transposition in its natural action.
At order 26 every such marking is excluded.
At order 25 the only degrees left by these bounds and the [five-point exclusion](Yin_C_A0293_v1.md#statement) are six and seven; their occurrence under half rank remains open.

## A strict window bound and generation at order twenty-five

The following strict numerical tests also apply without scalar group-ring injectivity.
Suppose there is a marked cyclic quotient at the indicated order, \(t\) has infinite order, and all four complex two-square corners and their assembly are invertible.
Write \(\delta=\dim_H\ker(B+At-s(D+Ct))\) and \(U=s^{-1}(At+B)(Ct+D)^{-1}\) in the actual affiliated algebra.

At order 25 set \(A_0=\langle t_0,t_1,t_2\rangle\).
If \(s,s^2,s^3\) all lie outside \(A_0\), then \(\delta<1/2\).
Indeed the four cosets \(A_0s^j,\ 0\le j\le3\), are distinct.
The [four-position transfer window](Yin_C_A0183_v1.md#transfer-matrices-and-equality) gives \(\delta\le2/4\), with equality forcing all four fourth-root eigenspaces of \(U\) to have dimension \(1/2\).
Use the Laurent deformation with exponents \((3,-4)\), congruent modulo 25 to three times the marked degrees.
At every \(z\in\mu_{25}\) it has the original nullity by a character twist.
At \(z=i\) the \(t\) multiplier is one and the \(s\) multiplier is \(-i\), so the nullity under equality is also \(1/2\).
Twisting this evaluation by the same 25 characters gives nullity \(1/2\) at every point of \(i\mu_{25}\).
The two sets are disjoint.
Clearing the minimum exponent gives a polynomial of degree seven, with invertible constant coefficient \(At\).
The [polynomial nullity budget](Yin_C_A0204_v1.md#the-bound-using-individual-column-widths) bounds the sum of all these nullities by fourteen, whereas equality gives 25.
This proves the strict test.

For a half-rank input some \(s^k\) with \(1\le k\le3\) must therefore belong to \(A_0\).
Since \(t_3=s^kt_{3-k}s^{-k}\) and \(t_{-1}=s^{-k}t_{k-1}s^k\), this subgroup is invariant under \(s\) and \(s^{-1}\).
It is normal in \(H\), and \(H/A_0\) is cyclic since \(t\in A_0\).
The abelianization is exactly \(C_{25}\) by the [order-25 reduction](Yin_C_A0229_v1.md#consequences-for-the-original-half-increment), and \(t\) generates it.
Hence \(H=A_0\), and conjugating gives every consecutive triple.
For the interchanged inverse labels use the adjoint rectangle, with first mark \(t^{-1}\) and second mark \(s^{-1}\).
If their four cosets were distinct, the [noninteger extremal window criterion](Yin_C_A0186_v1.md#statement) would give a cyclic quotient of order four by the normal closure of \(t'=s^{-1}\).
The abelianization \(C_{25}\) permits no such quotient.
Thus the same normality argument proves generation by triples of conjugates of \(s\) under \(t\), and passing to inverses or reversing consecutive indices preserves this assertion.

## The two-position window at order twenty-six

At order 26, if \(s^2\notin\langle t_0,t_1\rangle\), then again \(\delta<1/2\) under the numerical hypotheses above.
The sign character fixing \(t\) and negating \(s\) gives equal dimensions \(\delta\) for the \(+1,-1\) eigenspaces of \(U\).
Thus \(\ker(U^2-I)\) has dimension \(2\delta\).
Writing \(U^2=s^{-2}M(t_1)M(t_0)\) with \(M(y)=(Ay+B)(Cy+D)^{-1}\), the two-position window on \(s^2\) gives \(2\delta\le1\).
At equality it gives a \(-1\) eigenspace of \(U^2\) of dimension one, and the original sign character exchanges its two \(U\)-eigenspaces.
Hence \(\dim\ker(U+iI)=1/2\), as in the [adjacent-generation proof](Yin_C_A0296_v1.md#the-two-step-transfer-cannot-have-a-second-extremal-window).
Use \((3,4)\), congruent to three times the marked degrees modulo 26.
At every point of \(\mu_{26}\cup i\mu_{26}\) the nullity under equality is \(1/2\) by the same argument as above, since \(i^{26}=-1\).
The degree-seven polynomial has invertible constant coefficient \(B\).
The required sum 26 again exceeds fourteen.

In particular this strict numerical test applies whenever a nonsolvable image sends \(t\) to an element of order at most two.
If \(s^2\) belonged to \(\langle t_0,t_1\rangle\), that subgroup would be normal with cyclic quotient by conjugating its two generators in both directions, as in the [index-two calculation](Yin_C_A0296_v1.md#the-subgroup-and-the-periodic-filling).
Its image, generated by two conjugate involutions or by identities, would be solvable.
This cannot give a nonsolvable extension by a cyclic group.

## Invariant subspaces of the projective images

Set \(L_i=X^i\operatorname{im}(Y-I)\).
Each \(L_i\) is the image of \(X^iYX^{-i}-I\).
At order 25 the three projective classes at \(i=0,1,2\) generate the whole image.
Every corresponding matrix preserves \(L_0+L_1+L_2\) and induces the identity on its quotient.
Thus this sum is invariant under the projective group and the projective action on the quotient is trivial.

At order 26 let \(V_0=L_0+L_1\) and \(V_1=XV_0=L_1+L_2\).
Both are invariant under the image of the index-two subgroup \(F\), since each adjacent pair generates \(F\).
As \(s^2\in F\), \(X^2V_0=V_0\), so \(X\) exchanges \(V_0,V_1\).
Their intersection contains \(L_1\) and is \(X\)-invariant.
It therefore contains \(L_0=X^{-1}L_1\), which gives \(V_0=V_1\).
This nonzero subspace is invariant under the entire group.
The second mark acts trivially on the quotient and the projective quotient image is cyclic.

For the alternating-group application use the ordinary complex permutation representation on the sum-zero space of dimension \(d-1\), and then take its projective class.
It is irreducible: the permutation action is doubly transitive, so its commuting matrices on the full permutation space have only a common diagonal and a common off-diagonal entry.
The orthogonal projection of any invariant subspace of the sum-zero space is such a matrix and is scalar on that space.
A three-cycle and a double transposition each have rank two after subtraction of the identity on the sum-zero space, since each reduces the number of cycles of the identity permutation by two and the trivial summand is fixed.
The dimension bounds thus give \(d\le7\) at order 25 and \(d\le5\) at order 26.
The five-point theorem excludes \(d=5\) in both cases.

The subgroup generation alone does not imply solvability for an image with a second mark of order three.
For example \(x=(2\,4)(3\,5)\) conjugates \(y=(1\,2\,3)\) to \((1\,4\,5)\), and these two three-cycles generate \(A_5\): their product is a five-cycle, so their subgroup has order divisible by 15, and \(A_5\) has no proper subgroup of index at most four by simplicity.
The same two elements occur in every triple of consecutive conjugates since \(x^2=1\).
This example tests the generation condition alone; its marked image has already been ruled out for a half-rank rectangle by the separate five-point theorem.

## Assessment history

### Decision three-conjugates-and-the-projective-dimension-bounds

| Field | Value |
| --- | --- |
| date | 2026-11-26T15:12 |
| status | proved |
| reason | The extremal-window argument gives generation at order 25 and the stated invariant-subspace and marking restrictions at both orders. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Generation, invariant subspaces and excluded alternating markings. |
| argument | [A strict window bound and generation at order twenty-five](#a-strict-window-bound-and-generation-at-order-twenty-five) | Additional parameter cosets and both choices of second mark. |
| argument | [The two-position window at order twenty-six](#the-two-position-window-at-order-twenty-six) | The strict bound and adjacent pair. |
| argument | [Invariant subspaces of the projective images](#invariant-subspaces-of-the-projective-images) | The group-invariant subspaces and ranks of the marked permutations. |
| review | [Three conjugates and the projective dimension bounds](../audits/reviews/Yin_R_A0215_v1.md#three-conjugates-and-the-projective-dimension-bounds) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-three-conjugates-and-the-projective-dimension-bounds)

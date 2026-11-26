---
author: Yin
---

# A uniform gap for nonabelian solvable images at noncyclic order twenty

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with injective regular action of every nonzero scalar in \(\mathbb CH\).
Suppose \(H\) has a noncyclic abelian quotient of order twenty.
If \(H'\ne H''\), every complex two-square four-site matrix \(K=B+At-s(D+Ct)\) of noninteger regular rank satisfies
\[
                            \dim_H\ker K\le 19/40 .
\]
The trace is unnormalized on the two matrix coordinates.
Equivalently the group condition is that \(H\) admits a nonabelian solvable image: \(H/H''\) is such an image if \(H'\ne H''\), while every solvable image of a perfect commutator subgroup has trivial commutator subgroup.
In particular a half kernel forces \(H'\) to be perfect and every solvable quotient to factor through \(C_5\times C_2^2\).

For the associated rank-one commutator sum on these two marks with ordinary input ranks at most two, the smaller of the two support traces is at most \(19/40\) whenever \(H'\ne H''\).
This follows from the [exact support-trace rectangles](Yin_C_A0308_v1.md#statement).
The perfect-commutator case still requires a separate argument.

## A positive five-term orbit in ten coordinates

First consider a finite cyclic \(\mathbb Z[\zeta_5]\)-module \(V\) of order prime to ten with generator \(u\); write \(W\) for multiplication by \(\zeta_5\).
Suppose that \(H\) has an affine action with marked elements \((0,\epsilon_s W),(u,\epsilon_t W^2)\), where the two signs are not both positive.
Suppose an additive character of \(V\) of order \(d\) has strictly positive representatives \(c_j<d\) on \(W^j u,\ 0\le j<5\), summing to \(d\).
For any \(h\)-square invertible corners and invertible assembly we claim \(\dim_H\ker K\le h/5\).

To apply this test after changing marks, one may select the character after normalizing the affine pair.
We explain why the positive-orbit condition is unchanged in the above formulation.
Use the three [rectangle symmetries and marked exponents](Yin_C_A0319_v1.md#normalizing-the-two-steps): take \((x,y)=(s,t),(t,s^{-1}),(s,t^{-1})\) for the signs \((-,+),(+,-),(-,-)\), respectively.
These preserve the regular nullity and the corner assumptions.
Write \(R\) for the linear action of \(x\); it is minus a primitive power of \(W\), and the linear action of \(y\) is \(R^k\) with \(k=2,2,3\), respectively.
Conjugate by a translation to make \(x\) linear, and denote the translation part of \(y\) by \(u'\).
Here \(I-W^a\) for \(5\nmid a\) is an automorphism: its cokernel is killed by five by \(\Phi_5(W)=0\), and \(V\) has order prime to five.
Also \(I+W^a\) is an automorphism since \(\Phi_5(-1)=1\).
Thus \(I-R\) is invertible and the normalizing translation exists.
In the first row \(u'=u\), and in the third row inversion of \(t\) multiplies \(u\) by a signed power of \(W\).
In the second row the fixed point of the original \(t\) is \((I+W^2)^{-1}u\); moving it to zero makes the translation of \(s^{-1}\) equal to \((W^{-1}-I)(I+W^2)^{-1}u\).
These changes multiply \(u\) by module automorphisms commuting with \(W\).
Precomposing the additive character by their inverses preserves the five values up to permutation, including a cyclic shift or reversal.

On sites \(i\bmod10\) let \(P\) be the unit shift.
For every \(z^d=1\) use the character powers on \(V\) to represent translations diagonally, with entry at \(i\) the phase of \(R^{-i}\) applied to the translating element, and represent \(R\) by \(P\).
The two marked matrices then have the form \(P,\ P^k\operatorname{diag}(z^{e_i})\).
Here \(e_i\) represents the character on \(R^{-i-k}u'\).
By absorbing a fixed sign and a power of \(W\) in the functional, choose \(e_i>0\) at even \(i\) and \(e_i<0\) at odd \(i\).
In each parity class their absolute values are the five prescribed representatives, since \(-R\) is a generator of the order-five action and the parity class traverses all five exponents.
In particular \(\sum |e_i|=2d\).
These are genuine representations of the affine image; in the regular twist the two group translations \(x,y\) are still present.
The ten-channel nullity is \(10\dim_H\ker K\) at each of the \(d\) roots by absorption.

For general nonzero \(z\) the resulting Laurent matrix has, in the block column at \(i\), the terms \(B,-xD\) at sites \(i,i+1\), and \(Ay,-xCy\) multiplied by \(z^{e_i}\) at sites \(i+k,i+k+1\), respectively.
Multiply columns with negative exponent on the right by \(z^{-e_i}y^{-1}\).
Each of the \(h\) columns per site now has degree at most \(|e_i|\).
At zero the even columns transmit \(B,-xD\) from their original sites.
The odd columns transmit \(A,-xC\) from sites shifted by \(k\).

If \(k\) is even, there is one column at every intermediate site.
Reorder the columns by site.
The resulting cyclic matrix has local diagonal blocks \(B\) or \(A\) and next-row blocks \(-xD\) or \(-xC\).
Its determinant over the commutative polynomial ring in \(x\) has nonzero constant coefficient.
Evaluation at the infinite-order group element \(x\) gives an affiliated unit by the regular cyclic Fourier calculus.
If \(k\) is odd, the two columns arrive together at the even sites and none at odd sites.
The output pairs consisting of an even site and its successor are disjoint; each pair has invertible block \({\rm diag}(I,-xI)\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\).
Thus in both cases the polynomial has full regular rank at zero.
The [individual column-degree inequality](Yin_C_A0204_v1.md#the-bound-using-individual-column-widths) yields \(10d\dim_H\ker K\le2dh\), as claimed.

## Reducing a large fractional nullity to the split module

Write \(\delta=\dim_H\ker K\), and assume \(\delta>19/40\) and the rank is noninteger.
By scalar injectivity a nonzero entry is an affiliated unit, so \(0<\delta<1\).
An infinite abelianization gives arbitrarily large finite quotients.
For a finite abelian quotient of order \(N\), the [short-vector bound](Yin_C_A0198_v1.md#the-lattice-of-all-finite-characters) gives \(\delta\le2\sqrt{2/N}\), since the generic integer rank must be two.
Any abelianization properly covering the given order-twenty quotient is infinite or has order at least forty; then the bound is smaller than \(19/40\).
Consequently \(Q=H_{\rm ab}=C_5\times C_2^2\).
The [short-character inequalities](Yin_C_A0311_v1.md#the-noncyclic-quotient-of-order-twenty) exclude the other markings by \(\delta\le3/10\).
Use the normalized degrees \((1,e_1),(2,e_2)\).

Both mixed order-ten lifts \((1,2),(2,-1)\) have width three and each extreme term is a single corner times a translation.
If both extremes were singular, the projective degree budget of six at the ten phases and both endpoints would give \(10\delta\le4\).
If one extreme is invertible, orient it as the leading coefficient.
The monic companion in six coordinates lies over the group ring since that coefficient has an inverse over the group ring.
If the other end were singular, the eigenspace at zero would have dimension at least one.
For the eleven distinct values consisting of zero and the ten roots, the product of the corresponding linear factors evaluated on the companion is a nonzero group-ring matrix.
If it vanished, interpolation would give a nonzero group-ring idempotent onto an eigenspace of dimension \(\delta<1\).
A nonzero column in its image has rank one by scalar injectivity.
Thus the product has rank at least one, and the direct sum of those eleven eigenspaces has dimension at most five.
This again gives \(10\delta+1\le5\).
The [endpoint comparison](Yin_C_A0311_v1.md#the-two-ends-in-the-equality-case) therefore forces all four corners to be invertible already for \(\delta>2/5\).
The assembly is invertible at noninteger rank by the [four-site reduction](Yin_C_A0184_v1.md#the-four-group-elements-and-the-trace-bound).

The [class-two and dihedral estimates](Yin_C_A0313_v1.md#statement) now exclude all nonabelian dihedral quotients and all order-eight quotients with nontrivial commutator and abelianization of order four.
If the second and third lower central groups differed, the class-two commutator would be a nonzero quotient of \(\bigwedge^2 Q=C_2\).
The class-two image would have order forty and its Sylow two-factor would give a forbidden order-eight quotient.
These are exactly the two original-group inputs to the [metabelian splitting proof](Yin_C_A0313_v2.md#the-sign-action-on-a-simple-quotient).
Thus \(M=H'/H''\) is finite of order prime to five, \(\Phi_5(W)=0\), and \(H/H''=M\rtimes Q\) with the first mark in the complement and the translation of the second generating \(M\) as a module.
This use of the splitting depends only on the two exclusions and the specified abelianization.

The trivial binary coinvariants vanish at the present threshold as well.
Indeed for the quotient on which both signs act trivially the [five-coordinate calculation](Yin_C_A0313_v3.md#five-coordinates-with-coupled-translations) gives \(\delta\le2/5\) when its size exceeds \(18^4\) or one of its simple factors has a positive orbit.
For the remaining odd primes the [explicit extrema](Yin_C_A0313_v3.md#the-remaining-seventeen-marked-representations) give the same bound: the widths for \(p=3,11,41,61,101\) are at most \(25,110,315,395,720\), respectively, and \(\delta\le 2D/(50p)\).
Any nonzero binary reduction of the coinvariants gives the [sixteen-point affine estimate](Yin_C_A0317_v1.md#statement) \(\delta\le13/40\).
These estimates invoke the actual quotient and the invertible corners, not equality of \(\delta\) to one half.
The augmentation ideal of \(\mathbb F_2[C_2^2]\) has cube zero, so the [coinvariant argument](Yin_C_A0317_v1.md#excluding-the-binary-part-and-splitting-the-odd-components) shows \(M\) has odd order.
It is the sum of its three nontrivial sign components, each cyclic over \(\mathbb Z[\zeta_5]\).

## Excluding the nontrivial sign components

Choose a nonzero component \(V\) if one exists.
The marked semidirect product gives an actual quotient acting affinely on \(V\) as in the positive-orbit test, with translation \(u\) the component of the module generator.
If \(|V|>18^4\), the [four-coordinate pigeonhole argument and cyclic translates](Yin_C_A0212_v1.md#a-short-character-and-its-cyclic-translates) produce an additive character whose five strictly positive representatives sum to its order.
That argument uses exactly cyclic generation, the fifth cyclotomic relation and this size inequality.
The ten-channel estimate then gives \(\delta\le2/5\).

For smaller \(V\), choose a prime \(p\) dividing its order and take a simple quotient of \(V/pV\) over the cyclotomic ring.
It is \(\mathbb F_{p^f}\), \(f={\rm ord}_5(p)\), with multiplication by a primitive fifth root and nonzero image of the generator.
Here \(p\ne2,5\) and \(p\le18^4\).
For \(f=4,\ p\ge7\), and for \(f=2\), the [positive five-residue construction](Yin_C_A0215_v1.md#reducing-to-simple-marked-modules) gives the same estimate.
For \(f=1\) the [split-prime sieve](Yin_C_A0215_v1.md#split-primes-and-four-exceptional-cases) finds a positive orbit except at \(11,41,61,101\).
The sole remaining degree-four characteristic is three.
At these five primes the [thirty-four signed representations](Yin_C_A0319_v1.md#costs-of-the-thirty-four-marked-representations) cover all marked simple quotients, with bound at most \(h/5=2/5\).
Each possible nonzero component contradicts \(\delta>19/40\).
It follows that \(M=0\), proving the claimed inequality whenever \(H'\ne H''\).

## Assessment history

### Decision a-uniform-gap-for-every-nonabelian-solvable-image

| Field | Value |
| --- | --- |
| date | 2026-11-26T16:50 |
| status | proved |
| reason | The ten-coordinate estimate eliminates every nonzero residual sign component above nineteen fortieths. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The ten-coordinate estimate eliminates every nonzero residual sign component above nineteen fortieths. |
| argument | [A positive five-term orbit in ten coordinates](#a-positive-five-term-orbit-in-ten-coordinates) | A positive five-term orbit in ten coordinates. |
| argument | [Reducing a large fractional nullity to the split module](#reducing-a-large-fractional-nullity-to-the-split-module) | Reducing a large fractional nullity to the split module. |
| argument | [Excluding the nontrivial sign components](#excluding-the-nontrivial-sign-components) | Excluding the nontrivial sign components. |
| review | [A uniform gap for every nonabelian solvable image](../audits/reviews/Yin_R_A0224_v1.md#a-uniform-gap-for-every-nonabelian-solvable-image) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-a-uniform-gap-for-every-nonabelian-solvable-image)

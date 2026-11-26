---
author: Yin
---

# The fourth cyclotomic quotient vanishes at the order-sixteen marking of degrees one and six

## Statement

Under the [order-sixteen half-kernel hypotheses](Yin_C_A0328_v1.md#statement) put \(M=H'/H''\) and \(S=\operatorname{Ad}_s\) on \(M\).
For \(\ell=4,8,16\) write \(M_\ell=M/\Phi_\ell(S)M\).
Then
\[
 M_4=0,\qquad |M_8|\le16^4,\qquad |M_{16}|\le32^8,\qquad
 \Phi_8(S)\Phi_{16}(S)M=0,\qquad |M|\le 2^{56}.
\]
In particular the entire finite metabelian quotient has order at most \(2^{60}\).
The possible eighth and sixteenth cyclotomic quotients remain.

The rank estimates below only require the actual marked split group images specified there, the marked character of order sixteen, invertible \(B,C,{\cal P}=\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\), and at least one of \(A,D\) invertible.
They hold for \(h\)-square numerical corners with regular nullity denoted by \(\delta\).
The half-kernel application uses these conditions with \(h=2\) by [the two marked lifts](Yin_C_A0328_v1.md#degree-lost-at-singular-extreme-corners).

## Approximating a half turn by an actual character

The [cyclic metabelian calculation](Yin_C_A0212_v1.md#finiteness-and-the-cyclic-module) gives a split quotient \(M\rtimes C_{16}\) with marks \((0,s),(u,s^6)\), where \(u\) generates \(M\) as a \(\mathbb Z[S]\)-module.
The group \(M\) is finite of odd order. [Dihedral and cyclic restrictions](Yin_C_A0328_v1.md#two-dimensional-twists-and-the-sign-quotient)
Put \(d=\ell/2\), so \(\Phi_\ell(X)=X^d+1\).
On \(N=M_\ell\) one has \(S^d=-I\).
Since \(S^\ell=I\), the split group maps onto \(N\rtimes C_\ell\) with the same marked form.
Write \(u\) for its projected generator as well.

If \(|N|>(4d)^d\), there is an additive character of \(N\) whose values on all \(S^i u\) have representatives in \((3/8,5/8)\) in \(\mathbb R/\mathbb Z\).
Indeed the first \(d\) values distinguish the characters since the remaining \(d\) are their negatives.
Partition the torus of the first \(d\) coordinates into \((4d)^d\) equal half-open boxes.
Subtracting two distinct characters in a common box gives a nonzero vector \(x\) of rational lifts with \(|x_i|<1/(4d)\) for these coordinates.
Fill the remaining coordinates by \(x_{i+d}=-x_i\).
On the real space of such antiperiodic lists the cyclic shift is annihilated by \(\Phi_\ell\).
The first \(d\) shifts of \(x\) are independent over the rationals by irreducibility, and hence over the reals by their rational entries.
They form a basis, and each corresponds modulo one to an actual character.
In that basis express the vector with first half constantly \(1/2\) and second half constantly \(-1/2\), and round every coefficient to a nearest integer.
The coordinate errors are strictly less than \(d/(8d)=1/8\).
The rounded list represents the required character after adding one to the second half coordinates. [Rounding cyclic translates](Yin_C_A0212_v1.md#a-short-character-and-its-cyclic-translates)

For such a character let \(k\) be its order and use \(\ell\) coordinates indexed modulo \(\ell\).
If \(P e_i=e_{i+1}\), inducing the character powers gives \(s\mapsto P,\ t\mapsto P^6\operatorname{diag}(w^{v_i})\) for all \(w^k=1\), where \(v_i/k\) represents the value at \(S^{-i-6}u\).
The index shift and reversal preserve the interval, and the representatives at \(i,i+d\) sum to one.
Tensor at \(w=z^{16}\) with the cyclic order-sixteen character evaluated at \(z^k\) for all \(z^{16k}=1\).
Thus the \(s\)-edges have exponent \(k\) and the \(t\)-edges have exponents
\[
                      b_i=6k+16v_i-16k\in(-4k,0),\qquad
                      b_i+b_{i+d}=-4k .
\]
Here \(3k/8<v_i<5k/8\).
These are lifts of actual marked representations and still carry the original group translations.

Multiply each source column block by \(z^{-b_i}\).
The highest degree in this block is \(k-b_i\).
At zero only the \(At\) term survives, giving a translated and permuted invertible block matrix if \(A\) is invertible.
Reversing the columns with their prescribed degrees, only the \(-sD\) term survives at zero, giving an invertible endpoint if \(D\) is invertible.
Thus there is full generic rank and the [column interpolation bound](Yin_C_A0204_v1.md#the-bound-using-individual-column-widths) gives
\[
             16k\ell\,\delta\le h\sum_i(k-b_i)=3hk\ell .
\]
Regular absorption gives the factor \(\ell\) on the left.
Hence \(\delta\le3h/16\) for this orbit.
At a two-square half kernel it follows that \(|M_\ell|\le(4d)^d\) for all three \(\ell\), in particular \(|M_4|\le64\).

## All small fourth-root modules

If \(M_4\ne0\), choose an odd prime \(p\) that divides its order and a simple \(\mathbb F_p[S]\)-quotient of \(M_4/pM_4\).
It is the field obtained by adjoining a primitive fourth root \(r\) to \(\mathbb F_p\).
We can take \(r\) to be the inverse action for the character list.
The size bound leaves \(p=3,7\) in degree two and \(p=5,13,17,29,37,41,53,61\) in degree one.
In degree two the first two values \(a,b\) of a linear functional on \(1,r\) can be chosen arbitrarily.
In degree one they have the form \(a,ar\bmod p\).
The remaining values are \(-a,-b\).
Any index offset and the image of the marked module generator are absorbed by changing the functional.

At \(p=7\) choose \(a=b=3\).
For \(p=29,37,41,53,61\) take respectively
\[
             (r,a,ar\bmod p)=(12,11,16),(6,15,16),(9,16,21),
                          (23,22,29),(11,25,31).
\]
The two listed coordinates and their negatives all lie in \((3p/8,5p/8)\), and replacing \(r\) by \(-r\) preserves this property.
The previous estimate applies to all these markings.

For the remaining cases use the same \(16p\) phases, with first-edge cost \(p\) and second-edge costs the centered representatives of \(6p+16a,6p+16b,6p-16a,6p-16b\) modulo \(16p\).
The permutations have steps one and two on four sites.
The following table gives all seven certificates.

| \(p\) | \(r\) | \(a,b\) | minimum | maximum |
| --- | --- | --- | ---: | ---: |
| 3 | degree two | \(1,1\) | \(-24\) | 12 |
| 5 | \(2,3\) | \(1,r\) | \(-44\) | 24 |
| 13 | \(5,8\) | \(4,7\) for \(r=5\), \(4,6\) for \(r=8\) | \(-104\) | 52 |
| 17 | \(4,13\) | \(6,7\) for \(r=4\), \(6,10\) for \(r=13\) | \(-136\) | 68 |

For each input choose whether to take its second edge and then whether to take the first edge at its intermediate site.
Retain choices with four distinct outputs and minimize or maximize the sum of used edge costs.
The [integer verifier](../computations/programs/Yin_J_A0010/verify_four_phase_extrema.py) enumerates all \(4^4\) choices, yielding sixteen pairs of used edge sets.
For every certificate both extremal pairs of edge sets are unique, even when different matchings have the same pair.
At a site traversed by just one path in a minimum, only \(At\) or \(-sCt\) is used.
At such a site in a maximum only \(B\) or \(-sD\) is used.
Sites with two paths give translated invertible copies of \({\cal P}\).
Thus the [local matching endpoint](Yin_C_A0293_v1.md#invertibility-when-the-extremum-has-unique-edge-sets) is full at the minimum if \(A\) is invertible and at the maximum if \(D\) is invertible, using the known invertibility of \(C,B\), respectively.
The matching-spread estimate gives \(\delta\le h(\max-\min)/(64p)\le17h/80\) in all seven certificates.
At size two both \(3h/16\) and \(17h/80\) are below one half, proving \(M_4=0\).

## The order of the remaining module

Since \(M\) is finite, vanishing of \(M_4\) makes \(\Phi_4(S)\) an automorphism.
The [cyclotomic annihilator](Yin_C_A0328_v1.md#two-dimensional-twists-and-the-sign-quotient) therefore gives \(\Phi_8(S)\Phi_{16}(S)M=0\).
The image of \(\Phi_8(S)\) is a quotient of \(M_{16}\) by applying \(\Phi_8(S)\) to representatives, and its cokernel is \(M_8\).
Consequently \(|M|\le|M_{16}||M_8|\le32^8 16^4=2^{56}\).

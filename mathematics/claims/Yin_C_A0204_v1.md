---
author: Yin
---

# Cyclic twists combined with nonabelian quotients at orders 25 and 26

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free and set \(K=B+At-s(D+Ct)\) for complex two-by-two matrices.
Write \(\delta=\dim_H\ker K\) with the unnormalized matrix trace.
For the two bounds below assume all four corner matrices \(A,B,C,D\) are invertible.
Use the normalized markings of the [two critical cyclic quotients](Yin_C_A0201_v1.md#statement).

1. Suppose \(\chi:H\to C_{26}\) has \((\chi(s),\chi(t))=(1,10)\), and \(H\) has a dihedral quotient in which \(s\) is a reflection and \(t\) a generator of the rotations of odd order \(q\ge3\).
   Then \(\delta\le16/39\) for \(q=3\) and \(\delta\le4/13\) for \(q\ge5\).
   At \(q=3\) the same bound holds whenever \(H\) has a two-dimensional unitary representation in which the image of \(s\) is an involution and the image of \(t\) has the two primitive cube roots as eigenvalues.
2. Suppose \(\chi:H\to C_{25}\) has \((\chi(s),\chi(t))=(1,7)\).
   On coordinates indexed by \(\mathbb Z/5\), let \(P e_j=e_{j+1}\) and let \(E=\operatorname{diag}(1,-1,-1,-1,-1)\).
   Suppose \(s\mapsto P,\ t\mapsto P^2 E\) defines a representation of \(H\).
   If \(\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) is also invertible, then \(\delta\le108/250\).

With scalar group-ring injectivity, these marked quotient conditions exclude rank \(3/2\) for arbitrary corners and exclude a half constant-column increment.
Indeed rank \(3/2\) itself forces all the invertibilities used here by the [four-column reduction](Yin_C_A0184_v1.md#the-four-group-elements-and-the-trace-bound) and the [two extreme directions](Yin_C_A0201_v1.md#counting-zero-and-additional-parameters).
The dihedral hypothesis specifies the actual marked images, independently of any [homological construction of a quotient](Yin_C_A0203_v1.md#from-homology-to-an-actual-rotation-and-reflection).

## The bound using individual column widths

At \(k\) distinct unit phases, let assignments of \(s,t\) give actual unitary representations of a common dimension \(l\).
Assume that their twists of \(K\), after invertible scalar row or column monomials, agree there with a polynomial matrix \(Q(z)\) having individual column degrees at most \(d_i\) for \(1\le i\le 2l\).
If its maximum regular rank is \(2l\), then
\[
                   lk\delta\le\sum_i\min(k,d_i).
\]
The [column interpolation proof](Yin_C_A0202_v1.md#column-widths-and-interpolation) applies to any auxiliary dimension: injective evaluation at one complex parameter makes multiplication by \(Q(z)\) injective on input polynomial columns of respective degrees less than \((k-d_i)_+\).
The resulting outputs have degree less than \(k\) and inject into the sum of their \(k\) evaluation spaces by Vandermonde interpolation.
The domain dimension is \(\sum_i(k-d_i)_+\) and the sum of the closed image dimensions is \(k(2l-l\delta)\) by regular absorption, giving the inequality.
A limiting specialization with ranks arbitrarily close to \(2l\) suffices because the [polynomial rank estimate](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) gives maximal rank outside a countable set.

## The reflection and rotation

For each \(z^{26q}=1\), tensor the cyclic character with values \(z^q,z^{10q}\) by the dihedral representation sending \(s\) to the swap \(J\) and \(t\) to the diagonal matrix with entries \(z^{\pm26(q-1)/2}\).
These two entries are inverse \(q\)-th roots, as required by the reflection relation.
The resulting images are \(z^qJ\) and \(\operatorname{diag}(z^{b_1},z^{b_2})\), where after reduction modulo \(26q\),
\[
                  b_1=-3q+13,\qquad b_2=-3q-13.
\]
At \(q=3\) any representation in the more general hypothesis gives the same phase family with \(J\) replaced by a fixed unitary involution \(R\).
Take the eigenbasis of \(t\); diagonal changes of basis make the off-diagonal entry of the Hermitian matrix \(R\) real and hence make \(R\) real.
Complex conjugation then gives the representation with the two cubic eigenvalues inverted and \(R\) unchanged.
For the third possibility \(t\mapsto I\), \(s\mapsto R\) follows from \(\chi\) modulo two.
These three choices supply all \(z^{26}\) in the construction.
No coprimality between \(q\) and 26 is needed.

In input channel \(j\) multiply the two columns of the twisted \(K\) by \(z^{-\min(0,b_j)}\).
Their degrees are at most \(q+|b_j|\).
At zero the term involving \(s\) disappears and the resulting diagonal blocks are \(B\) when \(b_j>0\) and \(At\) when \(b_j<0\).
They are invertible, and neither \(b_j\) vanishes.
The column inequality gives
\[
 \delta\le \frac{2q+|b_1|+|b_2|}{26q}.
\]
At \(q=3\) the column widths in the two channels are 7 and 25; otherwise both exponents are negative and their absolute values sum to \(6q\).

For a presentation on these two marked generators this dihedral quotient admits a direct relation test.
Every relation word has an even number of \(s^{\pm1}\) letters by \(\chi\bmod2\).
When \(s\) acts by \(u\mapsto-u\) and \(t\) by \(u\mapsto u+1\) on \(\mathbb Z/q\), a relator acts by translation by its signed sum of \(t\)-letters, with each exponent weighted by \((-1)\) to the number of preceding \(s^{\pm1}\) letters.
Thus each signed sum must vanish modulo \(q\); these conditions on any defining relator set are sufficient since the two permutations generate the dihedral group.
For \(q=3\) this is the symmetric group on three elements.

## Five signed permutation coordinates

In the order-25 marking the cyclic character modulo five gives the unsigned representation \(s\mapsto P,\ t\mapsto P^2\).
For \(z^{50}=1\) use the unsigned assignment if \(z^{25}=1\) and the assumed signed assignment if \(z^{25}=-1\).
Tensor by the cyclic character \(s\mapsto z^4,\ t\mapsto z^{28}\).
This gives
\[
 s\longmapsto z^4P,\qquad
 t\longmapsto P^2\operatorname{diag}(z^{-22},z^3,z^3,z^3,z^3).
\]
Indeed the first exponent agrees with 28, and the other four with \(28+25\) modulo 50.
The original signed assignment generates the group of even diagonal signs extended by the cyclic permutation \(P\).
Conjugating \(E\) by powers of \(P\) puts the positive sign in each of the five positions; pairs of these sign vectors generate all even sign vectors.
The quotient has order \(16\cdot5\), and a finite presentation can be tested by evaluating each relator on the displayed signed permutation matrices.

Multiply the two columns in channel zero of the twisted rectangle by \(z^{22}\).
Every other input channel \(j\) has one \(B\) term in row \(j\), \(z^3 At\) in row \(j+2\), \(-z^4sD\) in row \(j+1\), and \(-z^7sCt\) in row \(j+3\), with indices modulo five.
In channel zero the four terms instead have powers \(22,0,26,4\) respectively.
The five channel widths are \(26,7,7,7,7\), with two columns in each channel.

Keep the channel-zero row and column, and eliminate the block \(H_+(z)\) on the four positive-index channels.
Its constant term is the diagonal of four copies of \(B\), so its inverse for small complex \(z\) has a convergent operator-norm power series.
In the two-by-two Schur complement at channel zero the first possible power is seven.
Here are all its paths and contributions, with \(L=B^{-1}\).
The intermediate channel list follows the direction from the initial input to the final output.

| Intermediate channels | Contribution at \(z^7\) |
| --- | --- |
| \(2\) | \(st^2\, C L A\) |
| \(2,3\) | \(-tst\, A L D L A\) |
| \(2,4\) | \(-st^2\, D L A L A\) |
| \(3\) | \(tst\, A L C\) |

Indeed the only starts of degree below seven are \(0\to2\) of degree zero and \(0\to3\) of degree four.
The direct exits from channels \(2,3,4\) have degrees \(7,3,4\), respectively; channel 1 has no direct exit.
Each transition between intermediate channels in the Neumann expansion has degree at least three.
These facts give exactly the paths shown, with their signs coming from Schur elimination and the expansion of \(H_+(z)^{-1}\).
The direct channel-zero term has degree 22.

Put \(F=C-D B^{-1}A\).
The sum in the table is \(st^2\,F B^{-1}A+tst\, A B^{-1}F\).
Both finite coefficient matrices are invertible by the assumed invertibility of \(\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) and of the corners.
The two group words are distinct, since equality would imply \(st=ts\) whereas \(P\) and \(P^2E\) do not commute.
After factoring out the first translation the second translation has infinite order by torsion-freeness.
Fourier transformation along its cyclic subgroup therefore reduces the coefficient to matrices \(F B^{-1}A+\xi A B^{-1}F\) with \(|\xi|=1\).
Their determinant has nonzero constant term, so the coefficient has full regular rank two.
Dividing the Schur complement by \(z^7\) now gives a norm limit of full rank at zero.
Lower semicontinuity of rank and the invertible eight-coordinate block give maximal rank ten for interpolation.
Applying the column bound at the 50 phases gives \(5\cdot50\delta\le2(26+4\cdot7)=108\).

## Markings with the stated abelianizations

For order 26 take the full lift of the orientation-preserving \((2,3,32)\) triangle group to the universal cover of \({\rm PSL}_2(\mathbb R)\).
Its [lifted triangle presentation](../audits/literature/Mil75/Yin_U001.md#lifted-triangle-presentation) has \(X^2=Y^3=Z^{32}=XYZ=c\) central, and the group is torsion-free by its action by increasing homeomorphisms of a line.
In the abelianization, writing \(x,y\) for the classes of \(X,Y\), elimination gives \(2x=3y\) and \(30x=32y\).
Thus the abelianization is \(C_{26}\), with \(x=3u,\ y=2u\) for a generator \(u\).
Mark \(s=X,\ t=YX^{-8}\).
They generate, and taking \(s\) as the quotient generator gives \(t=10s\bmod26\).
Sending \(c\) to one, \(X\) to a transposition, \(Y\) to a three-cycle, and \(Z\) to \((XY)^{-1}\) satisfies the presentation since \(XY\) is a transposition.
This gives the required \(S_3\) marking.

For order 25 take
\[
 H=\langle x,y,c\mid c\text{ central},\ x^5=c,\ y^5=c^{-1},\ (xy)^2=c\rangle .
\]
Modulo \(c\) this is the orientation-preserving \((5,5,2)\) triangle group.
The central element \(c\) has infinite order.
To see this, use its standard lifted triangle group with generators \(X,Y\) satisfying \(X^5=Y^5=(XY)^2=C\) for the infinite central element \(C\).
In the direct product of that lift with an infinite cyclic group on \(w\), quotient by the central subgroup generated by \(Cw^{-25}\).
Then \(w\) still has infinite order, since a power of \(w\) in the defining central subgroup forces the corresponding power of \(C\) to be trivial.
The assignments \(x=Xw^{-4},\,y=Yw^{-6},\,c=w^5\) in this quotient satisfy the presentation of \(H\).
Every finite-order element in the triangle quotient is conjugate into a vertex stabilizer: a nonidentity finite-order orientation-preserving hyperbolic isometry fixes a point, and the triangle tiling has nontrivial point stabilizers only at its vertices.
The three vertex stabilizers have full inverse images conjugate to \(\langle x\rangle,\langle y\rangle,\langle xy\rangle\) by the displayed powers and central kernel.
All are torsion-free, as is the kernel itself, proving torsion-freeness of \(H\).

The abelianization of \(H\) has relation rows \((5,5),(3,-2)\), of determinant \(-25\), and \(x\) generates since killing \(x\) also kills \(y\).
With \(s=x,\ t=yx^{-7}\), therefore \(\chi(s)=1,\chi(t)=7\) in \(C_{25}\).
Assign \(x\mapsto P,\ y\mapsto (P^2E)P^7\) and \(c\mapsto1\).
The image of \(y\) has underlying permutation \(P^4\) and an even sign vector, so its fifth power is one.
The image of \(xy\) is a diagonal sign matrix, hence its square is one.
The induced map on the marked generators gives the specified signed representation.
These examples verify the group and representation hypotheses of the numerical bounds for full corners; the conditional application to arbitrary corners invokes scalar injectivity as stated.

## Assessment history

### Decision combined-cyclic-and-nonabelian-twists

| Field | Value |
| --- | --- |
| date | 2026-11-26T07:40 |
| status | proved |
| reason | The independent whole-proof review verified the statement under its given hypotheses. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both marked quotient tests and their distinct coefficient conditions. |
| argument | [The bound using individual column widths](#the-bound-using-individual-column-widths) | General dimension of the auxiliary representation. |
| argument | [The reflection and rotation](#the-reflection-and-rotation) | Odd rotation orders, the two-dimensional alternative and signed words. |
| argument | [Five signed permutation coordinates](#five-signed-permutation-coordinates) | Column degrees and the lowest Schur terms. |
| argument | [Markings with the stated abelianizations](#markings-with-the-stated-abelianizations) | The two torsion-free triangle examples and their exact markings. |
| review | [Combined cyclic and nonabelian twists](../audits/reviews/Yin_R_A0187_v1.md#combined-cyclic-and-nonabelian-twists) | Independent mathematical finding on this fixed proof. |

## Current assessment

[Selected decision](#decision-combined-cyclic-and-nonabelian-twists)

---
author: Yin
---

# Large cyclotomic quotients of the commutator abelianization at prime-power order

## Statement

Let \(H=\langle s,t\rangle\), let \(H_{\rm ab}=C_{p^a}\) for a prime \(p\) and \(a\ge1\), and take \(s\) mapping to a generator and of infinite order.
Write the additive images of the two generators as \(1,b\), set \(N=[H,H]\), \(M=N_{\rm ab}\), and let \(S\) act on \(M\) by conjugation by \(s\).
For \(\ell=p^j\) with \(1\le j\le a\), put
\[
 L=\ell/p,\quad d=(p-1)L,\quad M_\ell=M/\Phi_\ell(S)M,\qquad
 c_\ell=1+\left\lfloor p(2p-3)L/2\right\rfloor .
\]
All these abelian groups \(M,M_\ell\) are finite.
For any complex coefficient matrices of size \(h\), consider the regular nullity \(\delta\) of \(B+At-s(D+Ct)\), with the unnormalized matrix trace.
Suppose \(B-yD\) is invertible over \(\mathbb C(y)\); in particular an invertible \(B\) suffices.
Then
\[
       |M_\ell|>c_\ell^{\,d}\quad\Longrightarrow\quad\delta\le h/p .
\]
More directly, an actual finite character on \(M_\ell\) whose values on the cyclic orbit have positive representatives summing to \(1\) on each group of \(p\) coordinates as in the proof gives this same bound, irrespective of the order of \(M_\ell\).
Thus \(\delta>h/p\) forces
\[
                 |M|\ \le\ \prod_{j=1}^{a}c_{p^j}^{\,\varphi(p^j)} .
\]
The regular rank estimate uses the indicated pencil condition and the actual representations of \(H\); no general scalar-injectivity premise is needed for the estimate.

In the torsion-free, scalar-injective order-25 half-rank problem the [normalization and corner test](Yin_C_A0201_v1.md#statement) supplies this pencil condition at \(h=2,\ p=5,\ a=2\).
If the commutator abelianization is large at either cyclotomic quotient, the nullity is at most \(2/5\).
Consequently a half-dimensional kernel requires a finite abelian group \(M\) satisfying
\[
          |M|\le18^4 88^{20},\qquad \gcd(|M|,30)=1 .
\]
The size cutoff is sufficient and no optimality is claimed.

## Finiteness and the cyclic module

Since \(H/N\) is cyclic, \(N=[H,H]=[N,N][s,N]\).
Indeed killing the latter two subgroups makes \(H\) abelian.
It follows that \(S-I\) is surjective on \(M\), hence bijective on this finitely generated abelian group; finite generation follows from the finite index of \(N\).
The class of \(s^{p^a}\) is fixed and therefore zero in \(M\).
Thus \(H/[N,N]=M\rtimes C_{p^a}\) with the marked lift of the generator.
Writing \(u=t s^{-b}\) shows that its class \(\bar u\) generates \(M\) as a cyclic module over \(\mathbb Z[S]\).
The endomorphism \(S\) has order dividing \(p^a\).

On \(M\otimes\mathbb Q\) each nontrivial rational irreducible summand is cyclotomic of order \(p^j\).
On each such summand the absolute determinant of \(S-I\) is \(\Phi_{p^j}(1)=p\).
There is no invariant summand, and the integral free quotient of \(M\) has determinant of \(S-I\) equal to a unit.
This forces rational dimension zero.
Also on \(M/pM\) the endomorphism \(S-I\) is nilpotent by \(S^{p^a}=I\), and remains invertible; therefore \(p\) does not divide \(|M|\).
The product of the endomorphisms \(\Phi_{p^j}(S)\) for \(1\le j\le a\) kills \(M\), since its product with the invertible \(S-I\) does.
Filter \(M\) by images of successive partial products.
Each quotient of adjacent images is a quotient of the corresponding \(M_{p^j}\), by applying the preceding product to representatives.
Hence \(|M|\le\prod_j |M_{p^j}|\).

## A short character and its cyclic translates

Fix \(\ell=p^j\) and use additive characters into \(\mathbb R/\mathbb Z\).
For each character \(\eta\) of \(M_\ell\), form the vector with coordinates \(\eta(S^i\bar u)\), \(0\le i<\ell\), using the image of \(\bar u\) in that quotient.
The first \(d\) coordinates distinguish the characters, because the monic annihilating polynomial \(\Phi_\ell=1+X^L+\cdots+X^{(p-1)L}\) and the cyclic generator express every subsequent coordinate in them.
The \(p\) coordinates in each residue class modulo \(L\) sum to zero modulo one.

If \(|M_\ell|>c_\ell^d\), partition the torus of the first \(d\) coordinates into \(c_\ell^d\) half-open equal cubes.
The difference of two distinct characters in one cube has a nonzero rational lift \(x\) with all its first \(d\) coordinates smaller in absolute value than \(1/c_\ell\).
Complete \(x\) to a real vector of length \(\ell\) by taking the negative sum of the first \(p-1\) entries in each residue class for its last entry.
The \(L\) new coordinates have absolute values less than \((p-1)/c_\ell\) and this completion still gives an actual character modulo one.

The real space of vectors summing to zero within each residue class has dimension \(d\).
Cyclic shifts preserve it and satisfy \(\Phi_\ell\) there.
Since \(x\) is nonzero and rational and \(\Phi_\ell\) is irreducible over \(\mathbb Q\), its first \(d\) consecutive shifts are a real basis: a rational dependence of lower degree is impossible, and the rank of their rational coordinate matrix is unchanged by extension to the reals.
Each shift still represents an actual character.
In this space take the vector with all coordinates \(1/p\) except that one subtracts one from a single coordinate in each residue class.
Expand it in the basis of shifts and round every real coefficient to the nearest integer.
The resulting vector \(y\) represents an actual character modulo one.
In each coordinate the rounding error is at most half the sum of the absolute values of \(d\) distinct coordinates of the cyclic vector \(x\).
At most \(L\) of these are completed coordinates.
Thus the error is strictly less than
\[
                  \frac{d+(p-2)L}{2c_\ell}<\frac1p .
\]
After restoring the subtracted integers, the entries lie strictly between zero and \(2/p\).
Each residue-class sum is integral and strictly between zero and two, so equals one.
Their total is \(L\), also in the case \(p=2\) where the upper bound on a single entry is one.

## Regular twists with positive powers

Let \(k\) be the order of this character.
Use the cyclic shift \(P\) on \(\ell\) coordinates, \(Pe_i=e_{i+1}\).
The quotient \(M_\ell\rtimes C_\ell\) of the split metabelian quotient exists because \(S^\ell=I\) on \(M_\ell\).
Represent an element \(n\in M_\ell\) diagonally at coordinate \(i\) by the character value on \(S^{-i}n\), and the cyclic generator by \(P\).
For each \(k\)-th root \(w\), the corresponding power of this character gives the marked representation
\[
     s\longmapsto P,\qquad
     t\longmapsto P^b\operatorname{diag}(w^{e_i}).
\]
Here \(e_i/k\) are the preceding positive representatives with indices negated and shifted by \(-b\), since \(t=u s^b\).
This permutation carries residue classes modulo \(L\) to residue classes, so \(e_i>0\) and \(\sum_i e_i=kL\).

The twisted rectangle is now a polynomial matrix with \(h\) columns of degree at most \(e_i\) at each auxiliary index \(i\).
At zero it equals \(B-sD P\) in block notation.
Constant Fourier transformation of \(P\) splits this into matrices \(B-\lambda sD\), with \(\lambda\) on the unit circle.
Since \(s\) has infinite order and \(\det(B-yD)\) is nonzero as a polynomial, each is an affiliated unit by the bilateral shift model.
Thus polynomial multiplication is injective on columns of polynomials.
At the \(k\) allowed points each kernel has unnormalized dimension \(\ell\delta\) by unitary absorption.
The [unequal-degree interpolation argument](Yin_C_A0202_v2.md#column-widths-and-interpolation), with auxiliary dimension \(\ell\) as in the [finite-dimensional version](Yin_C_A0204_v1.md#the-bound-using-individual-column-widths), gives
\[
                  k\ell\delta\le h\sum_i e_i=hkL.
\]
This is the desired estimate \(h/p\).
In the order-25 application, the [binary test](Yin_C_A0208_v1.md#statement) and the [ternary test](Yin_C_A0209_v1.md#statement) eliminate orders divisible by two and three under the half-rank hypothesis; the prime-power argument above eliminates five independently of that rank hypothesis.
The constants in the two cyclotomic factors are \(18\) and \(88\), respectively.

## Assessment history

### Decision character-bounds-at-prime-power-order

| Field | Value |
| --- | --- |
| date | 2026-11-26T10:12 |
| status | proved |
| reason | Independent inspection verified finiteness, the short-character argument and the regular-rank estimate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The general pencil estimate and the critical order-25 consequence. |
| argument | [Finiteness and the cyclic module](#finiteness-and-the-cyclic-module) | The split action and the product bound without coprime splitting. |
| argument | [A short character and its cyclic translates](#a-short-character-and-its-cyclic-translates) | Independent short translates, rounding and positive representatives. |
| argument | [Regular twists with positive powers](#regular-twists-with-positive-powers) | The marked action, full pencil at zero and the unnormalized bound. |
| review | [Character bounds at prime-power order](../audits/reviews/Yin_R_A0189_v1.md#character-bounds-at-prime-power-order) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-character-bounds-at-prime-power-order)

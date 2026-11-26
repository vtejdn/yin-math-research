---
author: Yin
---

# Finite Fourier coefficients exclude the alternating quotient of degree five at cyclic order twenty-four

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular scalar group-ring injectivity and an abelian quotient of order 24.
If the complex two-by-two rectangle \(K=B+At-s(D+Ct)\) has regular rank \(3/2\), then \(H\) has no quotient isomorphic to the alternating group \(A_5\).
This excludes every finite quotient that itself surjects onto \(A_5\), in the [remaining case \(H'=H''\)](Yin_C_A0278_v1.md#statement).

More generally, use the normalized degrees \(3,4\) on \(s,t\).
For a homomorphism to a finite group write \(x,y\) for their images, \(y_j=x^j y x^{-j}\), \(m=|y|\), and define
\[
               \mathcal R=\langle y_2\rangle\langle y_3\rangle x^4 .
\]
Suppose \(m\ge2\) and \(\langle y_1\rangle\cap\langle y_0\rangle=\{1\}\).
Then at least one of the following two purely finite conditions holds.

1. All \(y_1^i y_0^j\) with \(1\le i,j<m\) belong to \(\mathcal R\).
2. The identity belongs to \(\mathcal R\), and for one sign \(\epsilon\in\{1,-1\}\) both \(y_1^\epsilon y_0^j\) and \(y_1^j y_0^\epsilon\) belong to \(\mathcal R\) for every \(1\le j<m\).

For \(A_5\), 1560 of its 2280 ordered generating pairs satisfy the prior [adjacent-pair generation condition](Yin_C_A0274_v1.md#statement).
The two finite support conditions exclude all 1560.

## Two factors in the actual finite regular twist

Put \(t_j=s^jts^{-j}\) and \(M(z)=(Az+B)(Cz+D)^{-1}\).
The [four-step transfer identity](Yin_C_A0240_v1.md#the-four-step-product-and-its-middle-factors) gives
\[
           M(t_1)M(t_0)= M(t_2)^{-1}M(t_3)^{-1}s^4 .
\]
Let the finite image act by its left regular representation and twist by it.
Equivalently, embed \(H\) diagonally in the product of the finite image and \(H\), an injective group map whose regular inclusion preserves the affiliated identity by coset decomposition.
In the two product factors the left side becomes \(M(y_1t_1)M(y_0t_0)\); the right side becomes \(M(y_2t_2)^{-1}M(y_3t_3)^{-1}x^4s^4\).
The translations \(t_j\) in the second factor have infinite order, so all the cyclic rational denominators remain affiliated units.

For a primitive \(m\)-th root \(\omega\) let
\[
                 E_k(z)=\frac1m\sum_{h=0}^{m-1}\omega^{-kh}M(\omega^h z),
                 \qquad k\bmod m.
\]
Since \(|y_j|=m\), diagonalizing its finite cyclic translation gives \(M(y_jt_j)=\sum_{k=0}^{m-1}y_j^k E_k(t_j)\).
The analogous formula for \(M^{-1}\) confines the finite labels on the right side to \(\mathcal R\).
Distinct finite group elements are independent over the second affiliated algebra: after a common denominator the coefficients are bounded, and the finite group Fourier coefficients recover them.
The trivial cyclic intersection makes every \(y_1^i y_0^j\) have unique indices modulo \(m\) on the left.
Thus
\[
            E_i(t_1)E_j(t_0)\ne0\quad\Longrightarrow\quad
                         y_1^i y_0^j\in\mathcal R .
\]

## Which finite frequencies must contribute

The [cyclic transfer calculation](Yin_C_A0245_v1.md#two-fourier-blocks-of-the-rational-transfer) shows that \(C,D\) are nonzero, at least one is invertible, and \(\det(Cz+D)\) is not a Laurent monomial.
First assume \(D\) is invertible and put \(T=D^{-1}C,\ V=A-BD^{-1}C\).
The assembled block is invertible, so \(V\) is invertible.
Then
\[
          M(z)=BD^{-1}+Vz(I+zT)^{-1}D^{-1}.
\]
If \(C\) is also invertible, each \(E_j(z)\), \(1\le j<m\), has leading Taylor coefficient \(V(-T)^{j-1}D^{-1}\) at degree \(j\), an invertible matrix.
Thus these rational matrices are invertible, including at each actual infinite-order translation in the affiliated sense.
Every resulting pair product is nonzero and the first finite condition follows.

Now suppose \(C\) has rank one.
Its conjugate factor \(T=D^{-1}C\) has rank one and \(\lambda=\operatorname{tr}T\ne0\), since \(\det(Cz+D)=\det D(1+\lambda z)\).
Using \(T^2=\lambda T\) gives
\[
               M(z)=L+zP-\frac{z^2}{1+\lambda z}\,R,\qquad
               L=BD^{-1},\quad P=VD^{-1},\quad R=VTD^{-1}.
\]
Here \(P\) is invertible and \(R\) has rank one.
The block \(E_1\) is invertible by its leading coefficient \(P\).
Every \(E_j\) with \(2\le j<m\) is nonzero, since its coefficient of \(z^j\) is \(-(-\lambda)^{j-2}R\).
Consequently each pair with one index \(1\) and the other nonzero has nonzero product.

The zero block also has full rank.
Indeed \(E_0(z)=L+f(z)R\), where \(f\) is nonconstant because its coefficient of \(z^m\) is \(-(-\lambda)^{m-2}\).
If its determinant vanished identically, \(\det(L+cR)\) would vanish for every \(c\in\mathbb C\).
Then \(L,R\) have a common kernel line or a common image line: if \(L\) has rank one, rank-one maps with distinct image lines and distinct kernel lines have invertible sum, and \(L=0\) also satisfies the alternative.
A common kernel line is sent by \(M(z)\) to its constant image line under \(P\).
For a common image line the same argument applies to \(M(z)^{\mathsf T}\), and the kernels of the resulting two constant covectors give a constant point correspondence for \(M(z)\).
Either case contradicts the [constant point correspondence obstruction](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer), since \(s\notin\langle t\rangle\) by the normalized degrees and \(M(t)-sI\) has rank \(3/2\).
Hence \(E_0(t_1)E_0(t_0)\) is invertible, giving the identity label in \(\mathcal R\).

If \(D\) is singular, \(C\) is invertible and the same proof for \(M(z^{-1})=(Bz+A)(Dz+C)^{-1}\) selects index \(-1\bmod m\) in the original parameter.
It preserves the zero frequency and the absence of a constant point correspondence.
This proves the second condition in the remaining case.

## Exhausting the ordered marks in the alternating group

Any surjection \(H\to A_5\) has \(\langle y_0,y_1\rangle=A_5\).
Indeed the [neighboring generation theorem](Yin_C_A0274_v1.md#statement) identifies their preimage generators with the index-four normal subgroup \(F\) having cyclic quotient, so the image of \(F\) in the perfect group \(A_5\) is the whole group.
The two cyclic subgroups intersect trivially: any common element centralizes their generators, and \(A_5\) has trivial center.
Thus the finite tests apply.

The [exact permutation enumeration](../computations/programs/Yin_J_A0010/verify_a5_transfer.py) lists the 60 even permutations of five entries, multiplies with the right factor applied first, and tests generation by closure from the identity under the two right multiplications.
For each ordered generating pair it forms the four conjugates in their indicated order.
After testing adjacent generation it enumerates \(\mathcal R\) directly and compares the first condition and both choices of sign in the second.
In the table, the sign column tests only the nonzero-index products of the second condition; the last column also requires the identity in \(\mathcal R\).

| \((|x|,|y|)\) | Generate | Adjacent generators | All nonzero pairs | Some sign | Sign and identity |
| --- | ---: | ---: | ---: | ---: | ---: |
| \((2,3)\) | 120 | 120 | 0 | 0 | 0 |
| \((2,5)\) | 240 | 240 | 0 | 0 | 0 |
| \((3,2)\) | 120 | 0 | 0 | 0 | 0 |
| \((3,3)\) | 120 | 0 | 0 | 0 | 0 |
| \((3,5)\) | 480 | 480 | 0 | 240 | 0 |
| \((5,2)\) | 240 | 0 | 0 | 0 | 0 |
| \((5,3)\) | 480 | 240 | 0 | 240 | 0 |
| \((5,5)\) | 480 | 480 | 0 | 240 | 0 |
| Total | 2280 | 1560 | 0 | 720 | 0 |

Neither condition survives for any previously admissible ordered pair.
This contradicts existence of the surjection.

## Assessment history

### Decision finite-support-and-the-alternating-group-on-five-letters

| Field | Value |
| --- | --- |
| date | 2026-11-26T14:38 |
| status | proved |
| reason | The finite Fourier blocks and complete independent enumeration exclude every generating marking of the alternating group of degree five. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both finite support alternatives and the alternating quotient. |
| argument | [Two factors in the actual finite regular twist](#two-factors-in-the-actual-finite-regular-twist) | The genuine regular twist, factor ordering and separation of finite labels. |
| argument | [Which finite frequencies must contribute](#which-finite-frequencies-must-contribute) | Unit and singular corners and the zero frequency. |
| argument | [Exhausting the ordered marks in the alternating group](#exhausting-the-ordered-marks-in-the-alternating-group) | All generating pairs and the two support conditions. |
| review | [Finite support and the alternating group on five letters](../audits/reviews/Yin_R_A0212_v1.md#finite-support-and-the-alternating-group-on-five-letters) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-finite-support-and-the-alternating-group-on-five-letters)

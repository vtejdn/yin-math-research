---
author: Yin
---

# The sixth and twelfth cyclotomic quotients at order twenty-four

## Statement

Assume the torsion-free, scalar-injective half-rank hypotheses of the [order-24 marking](Yin_C_A0241_v1.md#statement), normalized by \(H_{\rm ab}=C_{24}\) with marked degrees \(3,4\).
Write \(g=ts^{-1}\), \(M=H'/H''\), \(S=\operatorname{Ad}_g\) on \(M\), and \(M_r=M/\Phi_r(S)M\).
Then \(M_6\) is trivial, cyclic of order three, or additively isomorphic to \(\mathbb F_4\).
The quotient \(M_{12}\) is trivial or additively isomorphic to \(\mathbb F_4\).

In particular \(M\) is finite and its 2-primary subgroup has order at most \(2^{14}\).
These restrictions allow odd-order contributions from the second and fourth cyclotomic quotients without giving an upper bound on them.

## Two Fourier blocks of the rational transfer

Write \(L(y)=(Ay+B)(Cy+D)^{-1}\) for the rational transfer of the rectangle and \(J=(s^{-1}I_2)L(t)\).
The [four finite phases](Yin_C_A0241_v1.md#a-four-step-identity-tested-on-the-whole-character-group) give \(J^4=I_2\) and each fourth-root eigenspace has dimension \(1/2\).
In particular \(\det(Cy+D)\) cannot be a Laurent monomial.
Otherwise \(L(t)\) and \(J\) are group-ring matrices and the interpolation projection \((I+J+J^2+J^3)/4\) has group-ring entries and nonzero image in the fixed space.
A nonzero column in that image has a nonzero group-ring coordinate, an affiliated unit by scalar injectivity, so its generated right module has dimension one.
This contradicts the fixed-space dimension.
The same argument for \(J^{-1}=L(t)^{-1}(s I_2)\) excludes a Laurent monomial for \(\det(Ay+B)\).
Thus \(C,D\) are both nonzero and at least one of them is invertible: if both were singular the nonzero determinant of the regular pencil could only be a multiple of \(y\).
The same alternatives hold for \(A,B\).

Let \(E_k(y)\), \(k=0,1,2\), be the part of \(L(y)\) transforming by \(\omega^k\) under \(y\mapsto\omega y\), with \(\omega\) a primitive cube root of unity; this is the finite Fourier projection, so \(L=E_0+E_1+E_2\).
If \(D\) is invertible, put \(T=D^{-1}C\) and \(V=A-BD^{-1}C\).
The [assembled coefficient block](Yin_C_A0184_v1.md#the-four-group-elements-and-the-trace-bound) makes \(V\) invertible.
Then
\[
    L(y)=BD^{-1}+Vy(I+yT)^{-1}D^{-1},\quad
    E_1(y)=Vy(I+y^3T^3)^{-1}D^{-1},\quad
    E_2(y)=-Vy^2T(I+y^3T^3)^{-1}D^{-1}.
\]
Thus \(E_1\) is invertible over \(\mathbb C(y)\) and \(E_2\ne0\).
If \(C\) is invertible, applying this calculation to \(L(y^{-1})\) proves that \(E_2\) is invertible and \(E_1\ne0\).
Evaluation at the actual infinite-order translation \(t\) preserves these conclusions.

## A group containing the required translations

Fix \(r=6\) or 12, write \(O=\mathbb Z[\zeta_r]\), and denote its root \(\zeta_r\) by \(z\).
By the [split metabelian construction](Yin_C_A0241_v1.md#a-four-step-identity-tested-on-the-whole-character-group), \(H\) maps onto \(M_r\rtimes C_{24}\), where \(g\) is the cyclic generator and the image of \(s g^{-3}\) generates \(M_r\) as a module.
Hence \(M_r=O/I\) for an ideal \(I\), identifying the generator with the residue of \(1\) and the action of \(g\) with multiplication by \(z\).
Write \(\beta=1-z^4\), which is nonzero, and \(B'=O/\beta I\).
Multiplication by \(\beta\) embeds \(O/I\) into \(B'\): cancellation in the integral domain \(O\) gives injectivity.
Use the induced map into \(B'\rtimes C_{24}\).
With the old cyclic generator written \(\delta\), the two labels become \(\beta\,\delta^3\) and \(z\beta\,\delta^4\), using additive notation for their translation coefficients.
Indeed \(t=gs\).

Conjugate \(\delta\) by the translation with coefficient \(z\), and write \(\gamma\) for the resulting generator.
Conjugation changes its \(j\)-th power by adding \((1-z^j)z\) to the translation coefficient.
It follows that
\[
                            t=\gamma^4,\qquad s=u\gamma^3,\qquad u=1-z\in B'.
\]
The element \(1-z\) is a unit of \(O\) since \(\Phi_r(1)=1\).
In particular \(v=z^{-3}u\) generates all of \(B'\) as an \(O\)-module.
The group \(B'\rtimes C_{24}\) need only contain the image of \(H\); every representation of the containing group restricts to a representation of \(H\).

## A coefficient with three ordered factors

For every circle character \(\psi\) of \(B'\), use \(r\) channels with \(\gamma\) acting as the forward shift \(P\) and a translation \(b\) acting at index \(i\) by \(\psi(z^{-i}b)\).
In the regular twist the inverse of the \(s\)-translation is \(\Delta_\psi(P^{-3}\otimes s^{-1})\), where the diagonal phase of \(\Delta_\psi\) at \(i\) is \(\psi(-z^{-i}v)\).
The twisted \(t\)-translation is \(P^4\otimes t\).
Since \(P^4\) consists of three-cycles at both orders, the coefficient from channel \(i\) to channel \(i+4k\) of \(L(P^4\otimes t)\) is \(E_k(t)\).
This follows by diagonalizing each three-cycle; the rational denominators are invertible in the regular affiliated algebra by cyclic spectral calculus.

Put \(A_*=(P^{-3}\otimes s^{-1})L(P^4\otimes t)\), invertible and independent of \(\psi\).
The [absorbed four-step identity](Yin_C_A0241_v1.md#a-four-step-identity-tested-on-the-whole-character-group) gives \((\Delta_\psi A_*)^4=I\).
Right multiplication by \(A_*^{-1}\) gives an identity with only three internal blocks of \(A_*\).
In its block from \(i_1\) to \(i_4\), the path \((i_1,i_2,i_3,i_4)\) has phase
\(\psi(-v\sum_{j=1}^4z^{-i_j})\) and coefficient
\[
                     (A_*)_{i_4,i_3}(A_*)_{i_3,i_2}(A_*)_{i_2,i_1}.
\]
The right side is the single constant block of \(A_*^{-1}\).
A transition from \(i\) to \(j=i+4k-3\bmod r\) contributes the factor \(s^{-1}E_k(t)\).

Choose the following path according to an invertible denominator corner; if both corners are invertible either choice works.

| \(r\) | Corner | Path | Three successive Fourier indices |
| --- | --- | --- | --- |
| 6 | \(D\) | \((0,1,0,1)\) | \(1,2,1\) |
| 6 | \(C\) | \((1,0,1,0)\) | \(2,1,2\) |
| 12 | \(D\) | \((0,1,2,3)\) | \(1,1,1\) |
| 12 | \(C\) | \((0,5,10,3)\) | \(2,2,2\) |

At order six the selected coefficient has a nonzero middle block between two affiliated units.
At order twelve it is a product of three affiliated units.
Thus in every case it is nonzero.
The two middle indices of all possible paths occupy their prescribed classes modulo \(\gcd(4,r)\), each with three possible values.
With the endpoints fixed, this gives eight other paths.

Let \(h=\sum_{j=1}^4z^{-i_j}\in O\) for the selected path.
For one of the nine elements \(F\) consisting of \(h\) itself and its differences from the eight other path sums, one must have \(Fv=0\) in \(B'\).
Indeed otherwise the selected phase is distinct both from the constant phase and from those of every other path.
Characters of the compact dual of \(B'\) with distinct frequencies in \(B'\) are linearly independent; comparing coefficients in the complex span of the finitely many affiliated matrices would force the selected coefficient to vanish.
Since \(v\) is the residue of a unit of \(O\), \(F\in\beta I\).

## The integral orders and the finite commutator abelianization

The [integer computation](../computations/programs/Yin_J_A0010/verify_middle_terms.py) obtains the following sets of absolute norms of the nine elements \(F\) at each selected path:
\[
 \begin{array}{c|c|c}
 r & |\operatorname{Nm}(\beta)| & \{|\operatorname{Nm}(F)|\} \\ \hline
 6 & 3 & \{3,9,12\}\\
 12 & 9 & \{9,36\}.
 \end{array}
\]
It uses the integral power basis and the matrix of multiplication by each element, including the sign on every competing term.
All listed norms are nonzero.
Therefore \(O/(F)\) surjects onto \(B'\), whose order divides the corresponding norm.
Inside \(B'\) the subgroup \(\beta O/\beta I\) is isomorphic to \(M_r\) and has quotient \(O/\beta O\).
It follows that \(|M_6|\) divides one of \(1,3,4\) and \(|M_{12}|\) divides one of \(1,4\).
Modulo two both \(\Phi_6\) and \(\Phi_{12}\) have only the irreducible factor \(X^2+X+1\).
Thus neither quotient can have \(M_r/2M_r\) of dimension one, excluding order two and cyclic order four and giving the abelian groups in the statement.

Finally \(M\) is finitely generated, \(S^{24}=I\), and \(S-I\) is invertible.
On its free rational part a cyclotomic summand of prime-power order contributes a prime to the absolute determinant of \(S-I\), whereas this determinant on the free integral quotient is one.
The invariant summand is also excluded.
The remaining divisors \(6,12,24\) contribute no rational summands because their respective quotients \(M_r\) are finite and the action on \(M\otimes\mathbb Q\) is semisimple.
This proves finiteness.
The product of all the \(\Phi_r(S)\), \(r\mid24,\ r>1\), annihilates \(M\).
Filtering by the images of successive partial products gives \(|M|\mid\prod_{r\mid24,\ r>1}|M_r|\): each successive quotient is an image of the corresponding \(M_r\).
For \(r=2,4,8\), the invertible map \(S-I\) on \(M_r/2M_r\) is nilpotent, so these factors have odd order.
The bounds for \(r=3,24\) from the [four-term norm calculation](Yin_C_A0241_v1.md#the-norm-of-the-resulting-relation) give 2-primary orders at most \(16,64\), respectively.
Together with the orders for \(r=6,12\) this yields the asserted 2-primary bound.

## Assessment history

### Decision the-sixth-and-twelfth-quotients

| Field | Value |
| --- | --- |
| date | 2026-11-26T12:32 |
| status | proved |
| reason | Independent whole-proof inspection verified the stated bounds, hypotheses and argument at the indicated scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Integral abelian group possibilities and finiteness of the whole commutator module. |
| argument | [Two Fourier blocks of the rational transfer](#two-fourier-blocks-of-the-rational-transfer) | The monomial determinant obstruction and ordered rational Fourier blocks. |
| argument | [A group containing the required translations](#a-group-containing-the-required-translations) | The enlarged module, changed complement and cyclic generator. |
| argument | [A coefficient with three ordered factors](#a-coefficient-with-three-ordered-factors) | Selected nonzero coefficient and possible frequency collisions. |
| argument | [The integral orders and the finite commutator abelianization](#the-integral-orders-and-the-finite-commutator-abelianization) | Norm bounds, the residual binary group structures and filtration. |
| review | [The sixth and twelfth quotients](../audits/reviews/Yin_R_A0202_v1.md#the-sixth-and-twelfth-quotients) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-sixth-and-twelfth-quotients)

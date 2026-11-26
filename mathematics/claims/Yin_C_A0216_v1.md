---
author: Yin
---

# Five independent slices in the twenty-fifth cyclotomic quotient

## Statement

Let \(H=\langle s,t\rangle\) have abelianization \(C_{25}\), with marked images \(1,7\) and \(s\) of infinite order.
Put \(N=[H,H]\), \(M=N_{\rm ab}\), \(S=\operatorname{Ad}(s)\), and \(M_{25}=M/\Phi_{25}(S)M\).
Suppose that \(M_{25}\) has a simple \(\mathbb Z[S]\)-module quotient of characteristic \(p\ne5\) with
\[
                         \operatorname{ord}_{25}(p)=5\operatorname{ord}_5(p).
\]
For \(K=B+At-s(D+Ct)\), assume that the four complex two-by-two corners and \(\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) are invertible.
Then \(\dim_H\ker K\le2/5\) in the regular representation with its unnormalized matrix trace.

Consequently, if \(H\) is torsion-free with scalar group-ring injectivity and \(K\) has rank \(3/2\), every prime divisor \(p\) of the finite group \(M\) satisfies
\[
                           p\bmod25\in\{1,7,18,24\}.
\]
This restriction permits those residue classes; it does not assert that any of them occurs.

## Orbit coordinates on the five slices

The [cyclic-module construction](Yin_C_A0212_v1.md#finiteness-and-the-cyclic-module) gives \(M\rtimes C_{25}\) as an actual quotient with marked lift \(s\), and \(u=ts^{-7}\) generates \(M\) as a module.
Let \(V\) be the simple quotient in the statement and \(f=\operatorname{ord}_5(p)\).
Then \(V\) is the additive space of \(E=\mathbb F_{p^{5f}}\), with \(S\) acting by multiplication by an element of order 25, and \(u\) has nonzero image.
A character of \(V\) gives matrices on 25 coordinates
\[
       s\longmapsto P,\qquad t\longmapsto P^7\operatorname{diag}(w^{e_i})
                  \quad(w^p=1), \qquad P e_i^{\rm std}=e_{i+1}^{\rm std}.
\]
The shift and reversal in the [marked orbit formula](Yin_C_A0212_v1.md#a-short-character-and-its-cyclic-translates) put the exponent lists in the form \(e_i=\lambda(\alpha^i)\), for arbitrary \(\mathbb F_p\)-linear functionals \(\lambda:E\to\mathbb F_p\).
Here \(\alpha\) is the inverse of the multiplier of \(S\); the nonzero factor accounting for \(u\) and the index shift is absorbed in \(\lambda\).

Set \(\beta=\alpha^5\), so \(E_0=\mathbb F_p(\beta)\) has degree \(f\) and \([E:E_0]=5\).
Since \(\alpha\) generates \(E\), the lines \(\alpha^k E_0\), \(0\le k<5\), form a direct sum over \(E_0\).
Thus the five lists
\[
                   e_{k+5j}=\lambda_k(\beta^j),\qquad 0\le j<5,
\]
can be chosen independently, with any \(\mathbb F_p\)-linear functionals on \(E_0\), including zero.
This independence uses the factor of five in the degree hypothesis.

## Positive representatives beyond the finite search

Suppose there is a functional on \(E_0\) whose five values at the powers of \(\beta\) have strictly positive representatives of sum \(p\).
Choose its word on every slice.
Then the 25 positive exponents sum to \(5p\).
The [positive-character rank bound](Yin_C_A0212_v1.md#statement) gives \(2/5\): at zero the constant matrix is \(B-sPD\) on the auxiliary coordinates and has full support by the infinite order of \(s\) and \(\det B\ne0\).
There are \(p\) true phases and the two-column widths sum to \(10p\).

For \(f=4,\ p\ge7\), and for \(f=2\), the positive-sum words are given for every simple order-five marking by the [two analytic cases](Yin_C_A0215_v1.md#reducing-to-simple-marked-modules).
At \(p=2,3\) use the [binary](Yin_C_A0208_v1.md#statement) or [ternary](Yin_C_A0209_v1.md#statement) bound for the primitive order-25 component.
All inverses and prime-order assumptions in these quoted estimates apply here.

For \(f=1\) and \(p\le18^4\), the [split-prime check](Yin_C_A0215_v1.md#split-primes-and-four-exceptional-cases) supplies positive-sum words except at \(11,41,61,101\).
For \(p>18^4\) with \(f=1\), apply the [short-character construction](Yin_C_A0212_v1.md#a-short-character-and-its-cyclic-translates) to the additive order-\(p\) module \(E_0\) itself, with order-five multiplier \(\beta\) and cyclic generator \(1\).
The geometric construction only uses this finite cyclic module and its orbit of characters.
Equivalently take the auxiliary split group \(E_0\rtimes C_{25}\) with the generator acting by \(\beta\).
Its commutator subgroup is \(E_0\) since \(\beta-1\) is a unit there, and its fifth cyclotomic quotient has size \(p>18^4\).
The construction provides five strictly positive representatives of sum \(p\), whichever primitive fifth root is used.
Applying it to this auxiliary module supplies an orbit word; the five-slice argument is what realizes it in the original marked group.
The prime 101 is \(1\bmod25\) and does not satisfy the stated degree hypothesis.

## Twelve zero-parameter certificates

For each remaining \(p\in\{11,41,61\}\), \(\beta\in\mathbb F_p\) is one of the four primitive fifth roots.
Choose \(e_{k+5j}\) as the centered residue of \(c\beta^j\bmod p\) for \(k=0,2,4\), and as zero for \(k=1,3\).
The scale \(c\), total block width \(D_*=\sum_i|e_i|\), and resulting bound are
\[
\begin{array}{c|c|c|c}
 p&c&D_*&2D_* /(25p)\\ \hline
 11&1&45&18/55\\
 41&1&147&294/1025\\
 61&5&213&426/1525 .
\end{array}
\]
With the above \(p\)-phase representation, the four block entries from input \(i\) have row offsets \(0,1,7,8\) and are \(B,-sD,At,-sCt\) with exponents \(0,0,e_i,e_i\).
After multiplying the input by \(w^{-\min(0,e_i)}\), the exponents are nonnegative.
At zero the two offsets \(0,1\) survive exactly if \(e_i\ge0\); the two offsets \(7,8\) survive exactly if \(e_i\le0\).

The [25-coordinate verifier](../computations/programs/Yin_J_A0008/verify_slices.py) checks each primitive root for each listed prime using integer arithmetic.
In all twelve resulting support graphs it finds a perfect matching.
On identifying each matched row with its column, the components with mutual directed reachability are thirteen singleton vertices and six pairs.
In each pair the offsets from one column to the two rows are \(0,1\), and those from the other are \(7,8\).
Ordering the components gives a block triangular matrix.
Its diagonal blocks are the invertible single group-weighted corners and, up to ordering, copies of
\[
 \begin{pmatrix}At&B\\-sCt&-sD\end{pmatrix}
 =
 \operatorname{diag}(I_2,-sI_2)
 \begin{pmatrix}A&B\\C&D\end{pmatrix}
 \operatorname{diag}(tI_2,I_2).
\]
The latter are units since the middle matrix is a block-column permutation of the assumed invertible four-by-four coefficient matrix.
Hence at zero the full regular rank is fifty and the [column-width inequality](Yin_C_A0204_v1.md#the-bound-using-individual-column-widths) gives \(25p\delta\le2D_*\).
This proves the stated bounds without any assumptions about higher matrix ranks.

## The remaining prime divisors

At a half-rank input the [corner conditions](Yin_C_A0201_v1.md#statement) and [constant block normalization](Yin_C_A0184_v1.md#the-four-group-elements-and-the-trace-bound) hold.
The [fifth quotient exclusion](Yin_C_A0215_v1.md#statement) gives \(M_5=0\).
Consequently \(\Phi_5(S)\) is onto on finite \(M\) and \(\Phi_{25}(S)\) annihilates \(M\), by the product annihilator of the [cyclotomic size theorem](Yin_C_A0212_v1.md#finiteness-and-the-cyclic-module).
Thus \(M=M_{25}\), and \(5\) does not divide \(|M|\) by the same theorem.
If \(p\mid |M|\), the nonzero module \(M/pM\) has a simple quotient of characteristic \(p\).
The order of \(p\bmod25\) is either its order modulo five or five times that order, since the reduction map on units has kernel of order five.
The latter case was just excluded; in the former case the order divides four.
The fourth roots of one modulo 25 are exactly \(1,7,18,24\), giving the claimed list.

## Assessment history

### Decision the-degree-five-extension-at-order-25

| Field | Value |
| --- | --- |
| date | 2026-11-26T10:12 |
| status | proved |
| reason | Independent proof review and exhaustive matching enumeration verified the slice transfer and the surviving residue classes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The degree hypothesis, two-fifths estimate and remaining primes. |
| argument | [Orbit coordinates on the five slices](#orbit-coordinates-on-the-five-slices) | Independent characters on five summands in the extension field. |
| argument | [Positive representatives beyond the finite search](#positive-representatives-beyond-the-finite-search) | All nonexceptional primes, including the unbounded range. |
| argument | [Twelve zero-parameter certificates](#twelve-zero-parameter-certificates) | The twelve finite certificates and the original regular-rank bound. |
| argument | [The remaining prime divisors](#the-remaining-prime-divisors) | Surjectivity of the fifth polynomial and the residue-class test. |
| review | [The degree-five extension at order 25](../audits/reviews/Yin_R_A0191_v1.md#the-degree-five-extension-at-order-25) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-degree-five-extension-at-order-25)

---
author: Yin
---

# The binary coinvariants of the noncyclic order-twenty metabelian quotient

## Statement

Assume a half-dimensional kernel at the [noncyclic order-twenty marking](Yin_C_A0313_v1.md#statement).
In the [marked splitting](Yin_C_A0313_v2.md#splitting-with-a-prescribed-lift-of-the-first-mark) put \(M=H'/H''\), and let \(E_1,E_2\) act on \(M\) by the two binary basis elements of \(Q=C_5\times C_2^2\).
Then the largest quotient on which both binary elements act trivially is
\[
        B_*=M/\big((E_1-I)M+(E_2-I)M\big)
                    \ \cong\ (\mathbb Z/2^k\mathbb Z)^4
                         \qquad\text{for some }0\le k\le4 .
\]
In particular its order has no odd prime divisor.
The conclusion concerns the coinvariants, which may have smaller order than the full module when either binary action is nontrivial.

## Five coordinates with coupled translations

By the [metabelian module theorem](Yin_C_A0313_v2.md#statement), \(B_*\) is finite of order prime to five and is cyclic over \(\mathcal O=\mathbb Z[\zeta_5]\).
Write \(v\) for its marked module generator and \(W\) for multiplication by \(\zeta_5\).
There is an actual quotient \(B_*\rtimes C_5\), since the binary subgroup acts trivially after passing to \(B_*\).
The marks there are \((0,w)\) and \((v,w^2)\) for a generator \(w\) of \(C_5\).
For every additive character of \(B_*\) of order \(d\), and each \(w_0^d=1\), inducing its powers gives unitary representations on five coordinates in which \(s\) is the cyclic shift \(P\) and \(t=P^2\operatorname{diag}(w_0^{e_i})\), with \(Pe_i=e_{i+1}\) and indices modulo five.
Here the five residues \(e_i/d\) are character values in \(\mathbb R/\mathbb Z\) on \(W^{-i-2}v\), since \((v,w^2)\) first shifts the coordinate then acts diagonally.
This fixed rotation and reversal preserve positive sums.

If the five positive representatives of an orbit sum to \(d\), the [positive-power interpolation](Yin_C_A0212_v1.md#regular-twists-with-positive-powers) gives \(\delta\le2/5\).
Indeed the five two-coordinate input degrees are \(e_i\); at zero the polynomial matrix is \(B-sD P\) and is regularly invertible by diagonalization of \(P\), the infinite order of \(s\), and invertibility of \(B\).
The latter and the other corner and assembly assumptions used below hold at a half kernel by [the order-twenty endpoint](Yin_C_A0311_v1.md#the-two-ends-in-the-equality-case) and [four-column reduction](Yin_C_A0184_v1.md#statement).
If \(|B_*|>18^4\), the [short-character argument](Yin_C_A0212_v1.md#a-short-character-and-its-cyclic-translates) produces just such an orbit with \(p=\ell=5,\ L=1,\ d_{\rm basis}=4,\ c_\ell=18\).
Its hypotheses here are cyclic generation by the \(W\)-orbit of \(v\), \(\Phi_5(W)=0\) and the cardinality bound, and the preceding representation gives the required original-group evaluation.
Consequently \(|B_*|\le18^4\).

For any odd prime \(p\) dividing \(|B_*|\), take a simple \(W\)-module quotient of \(B_*/pB_*\).
It is \(\mathbb F_{p^f}\) with \(f=\operatorname{ord}_5(p)\), and \(W\) acts by a primitive fifth root.
For \(f=4,\ p\ge7\), or \(f=2\), the positive-sum orbits of the [five-coordinate construction](Yin_C_A0215_v1.md#reducing-to-simple-marked-modules) apply directly.
For \(f=1\), the [split-prime sieve](Yin_C_A0215_v1.md#split-primes-and-four-exceptional-cases) finds such an orbit at every \(p\le18^4\) outside \(11,41,61,101\).
Only this scalar positive-sum sieve is used from the split computation.
It leaves those four primes and the degree-four prime three for the present marking.

## The remaining seventeen marked representations

Let \(p\) be one of these five remaining primes and \(L=10p\).
Use a character of the actual abelian quotient with exponents \(a,b\bmod10\), where \(b\equiv2a\bmod5\) and the two binary parities are independent.
For each \(z^L=1\) tensor this character at \(z^p\) with the five-coordinate representation at \(w_0=z^{10}\).
The resulting first edges have exponent \(pa\), and the second edges at \(i\) have exponents \(b_i\), the centered representatives of \(pb+10e_i\bmod L\) in \([-L/2,L/2)\).
Every twist still includes the original left translations \(s,t\).
In the ternary degree-four case the sequences of character values on the five conjugates fill the sum-zero subspace over \(\mathbb F_3\): the evaluation map on the dual is injective by cyclic generation, and this subspace and the dual both have dimension four.
For a split prime the sequence is \(e_i=c r^i\bmod p\), where \(r\) is one of the four primitive fifth roots and the nonzero scalar \(c\) absorbs the fixed rotation and the chosen functional.
The indexing reversal is covered by running all four roots.

Here are the witnesses and their extreme flow costs.
Each of the sixteen split markings occurs once, and the degree-four ternary module has a single irreducible type.

| \(p\) | \(r\) | \((a,b)\) | \(c\) or ternary list | minimum | maximum |
| --- | --- | --- | --- | ---: | ---: |
| 3 | degree four | \((-1,-2)\) | \((0,0,1,1,1)\) | \(-20\) | 5 |
| 11 | 3, 4 | \((-1,-2)\) | 1 | \(-80\) | 25 |
| 11 | 5, 9 | \((-1,3)\) | 2 | \(-55\) | 55 |
| 41 | 10, 37 | \((-1,-2)\) | 1 | \(-260\) | 55 |
| 41 | 16, 18 | \((-1,-2)\) | 5 | \(-260\) | 55 |
| 61 | 9, 34 | \((0,5)\) | 10 | \(-350\) | 45 |
| 61 | 20, 58 | \((-1,-2)\) | 1 | \(-350\) | 45 |
| 101 | 36, 87 | \((0,0)\) | 1 | \(-360\) | 360 |
| 101 | 84, 95 | \((0,0)\) | 5 | \(-360\) | 360 |

For each column \(i\), choose whether it follows the \(t\)-edge to \(i+2\) or stays at \(i\); at the intermediate vertex \(j\) choose whether to take the \(s\)-edge to \(j+1\) or stay.
A choice at all five columns gives a matching if its five ends are distinct.
The [integer verifier](../computations/programs/Yin_J_A0008/verify_noncyclic_twenty.py) checks all \(4^5\) choices and obtains 24 different pairs of used edge sets.
Its cost is \(pa\) times the number of used \(s\)-edges plus the sum of \(b_i\) over the used \(t\)-edges.
In each row both extrema in the table select unique pairs of used edge sets, including possible multiple matchings with the same pair.
Thus the [invertible matching endpoint](Yin_C_A0293_v1.md#invertibility-when-the-extremum-has-unique-edge-sets) applies, using the four invertible corners and the invertible assembly.
If \(D\) is the difference of the tabulated extrema, the matching spread estimate gives \(5L\delta\le2D\).
Each row has \(4D<5L\), excluding the half kernel.
This step uses no cyclic character of order twenty-five.

## The binary possibilities for the coinvariants

It remains that \(B_*\) is a finite cyclic \(\mathcal O\)-module of order a power of two with \(|B_*|\le18^4\).
For the nonzero case let \(2^k\) be its exponent, so \(B_*\) is a cyclic module of the ring \(R=(\mathbb Z/2^k\mathbb Z)[x]/(\Phi_5)\).
The reduction of \(R\) modulo two is \(\mathbb F_{16}\), since the order of two modulo five is four.
Every element with nonzero reduction is a unit: lift its inverse in the residue field and then invert an element of \(1+2R\) by the finite geometric series.
Using the power basis \(1,x,x^2,x^3\), each nonzero element of \(R\) is \(2^j\) times a unit for some \(0\le j<k\), by dividing its coefficients by their common maximal power of two.
The kernel of a cyclic-module surjection \(R\to B_*\) must therefore be zero, since a nonzero element in this ideal would give \(2^j B_*=0\) with \(j<k\).
Thus \(B_*\cong(\mathbb Z/2^k\mathbb Z)^4\), where \(2^k\le18\) gives \(k\le4\).
The zero module is covered by \(k=0\).

## Assessment history

### Decision odd-primes-in-the-binary-coinvariants

| Field | Value |
| --- | --- |
| date | 2026-11-26T16:23 |
| status | proved |
| reason | The five-channel tests exclude every odd prime in the binary coinvariants and bound their remaining exponent. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The five-channel tests exclude every odd prime in the binary coinvariants and bound their remaining exponent. |
| argument | [Five coordinates with coupled translations](#five-coordinates-with-coupled-translations) | Five coordinates with coupled translations. |
| argument | [The remaining seventeen marked representations](#the-remaining-seventeen-marked-representations) | The remaining seventeen marked representations. |
| argument | [The binary possibilities for the coinvariants](#the-binary-possibilities-for-the-coinvariants) | The binary possibilities for the coinvariants. |
| dependency | [Central and dihedral images](Yin_C_A0313_v1.md#statement) | The central and dihedral quotient obstruction. |
| dependency | [The marked splitting](Yin_C_A0313_v2.md#statement) | The finite module over the order-five integers. |
| review | [The central commutator and dihedral quotients](../audits/reviews/Yin_R_A0221_v1.md#the-central-commutator-and-dihedral-quotients) | Independent review of the first obstruction. |
| review | [The marked metabelian quotient](../audits/reviews/Yin_R_A0221_v1.md#the-marked-metabelian-quotient) | Independent review of the marked splitting. |
| review | [Odd primes in the binary coinvariants](../audits/reviews/Yin_R_A0221_v1.md#odd-primes-in-the-binary-coinvariants) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-odd-primes-in-the-binary-coinvariants)

---
author: Yin
---

# Excluding the fifth cyclotomic quotient at the order-25 marking

## Statement

Let the torsion-free group \(H=\langle s,t\rangle\) have abelianization \(C_{25}\) with marked images \(1,7\), respectively.
Set \(N=[H,H]\), \(M=N_{\rm ab}\), and \(M_5=M/\Phi_5(S)M\), where \(S\) is conjugation by \(s\) and \(\Phi_5=1+X+X^2+X^3+X^4\).
If \(M_5\ne0\), the regular nullity \(\delta\) of \(K=B+At-s(D+Ct)\) satisfies
\[
                             \delta\le 614/1375<1/2
\]
for complex two-by-two \(A,B,C,D\) all invertible with \(\left(\begin{smallmatrix}B&A\\ D&C\end{smallmatrix}\right)\) invertible.
Consequently under scalar group-ring injectivity, any rank-\(3/2\) input at this marking forces \(M_5=0\) by the [four-column reduction](Yin_C_A0184_v1.md#the-four-group-elements-and-the-trace-bound) and [corner test](Yin_C_A0201_v1.md#statement).
The component at \(\Phi_{25}\) is outside the conclusion.

## Reducing to simple marked modules

The [cyclotomic size theorem](Yin_C_A0212_v1.md#statement) gives \(\delta\le2/5\) if \(|M_5|>18^4\), since \(B\) is invertible.
Otherwise a nonzero \(M_5\) has a simple quotient \(V\) of size \(p^f\le18^4\).
Indeed \(M_5\) is finite, and a maximal proper \(S\)-invariant subgroup gives a module of prime characteristic \(p\).
The [cyclic module calculation](Yin_C_A0212_v1.md#finiteness-and-the-cyclic-module) excludes \(p=5\), splits the quotient by \([N,N]\) as \(M\rtimes C_{25}\), and shows that \(u=ts^{-7}\) generates \(M\) as a module.
In \(V\), \(S\) acts by a primitive fifth root in the finite field \(\mathbb F_{p^f}\), with \(f=\operatorname{ord}_5(p)\); this follows from the Frobenius orbit of a root of \(\Phi_5\).
Each simple quotient gives representations on five coordinates by cyclically inducing any of its additive characters: with \(P e_i=e_{i+1}\) modulo five, the images are \(P\) and \(P^2\operatorname{diag}(w^{e_i})\) for each \(w^p=1\).
The exponent list is the orbit of the character evaluated on \(u\), with the order negated and cyclically shifted as in the [orbit formula](Yin_C_A0212_v1.md#a-short-character-and-its-cyclic-translates).
The shift can be absorbed in the chosen character; reversal exchanges a primitive root with its inverse.

An orbit with all five least positive residues summing to \(p\) gives \(\delta\le2/5\) by the same theorem at \(\ell=5\).
At \(p=2,3\) the [signed](Yin_C_A0206_v1.md#statement) and [ternary](Yin_C_A0209_v1.md#statement) bounds instead give \(108/250\) and \(8/25\).
For \(f=4\) and \(p\ge7\) the orbit lists fill the sum-zero subspace on five coordinates, since evaluation on the generating orbit is injective on the dual and both dimensions are four.
Use \((1,1,1,1,p-4)\).

For \(f=2\) the two simple representations correspond to roots \(\alpha\) with \(\alpha^p=\alpha^{-1}\).
Their orbit lists are all solutions of \(e_{i+2}=v e_{i+1}-e_i\), with \(v=\alpha+\alpha^{-1}\), because the first two positions are freely specifiable in the two-dimensional dual.
The two \(v\)'s solve \(v^2+v-1=0\bmod p\) and their positive representatives sum to \(p-1\).
Choose the smaller, so \(1<v<p/2\).
Starting with \(1,1\) gives positive residues \((1,1,v-1,p-2v,v-1)\) of sum \(p\).
Permuting the index \(i\) to \(2i\) exchanges the two Frobenius orbits and preserves the sum and positivity; this treats the other simple representation.

## Split primes and four exceptional cases

For \(f=1\) use a primitive fifth root \(r\bmod p\).
The available nonzero exponent lists are \(e_i=c r^i\bmod p\), \(0<c<p\), with any indexing reversal accounted for by replacing \(r\) with its inverse.
The positive-sum test is identical for all four primitive roots, since their power lists are permutations of one another.
The [exact verifier](../computations/programs/Yin_J_A0008/readme.md) finds 2491 primes \(p\equiv1\bmod5\) up to \(18^4=104976\).
Only \(11,41,61,101\) fail to admit a positive-residue sum \(p\).
It sieves that entire interval, chooses a primitive fifth root by raising elements to \((p-1)/5\), and tests multipliers until finding the required sum or exhausting all of them.

For each remaining marked root, use the following integers.
Write \(b_i\) for the centered representative of \(7ap+25cr^i\bmod25p\) and \(D_* =5ap+\sum_i|b_i|\).

| \(p\) | \(r\) | \(a\) | \(c\) | \(D_*\) | Minimum matchings |
| --- | --- | --- | --- | --- | --- |
| 11 | all four | 1 | 2 | 307 | 2 |
| 41 | all four | 2 | 6 | 1061 | 2 |
| 61 | 9, 34 | 1 | 5 | 1161 | 1 |
| 61 | 20, 58 | 2 | 10 | 1639 | 1 |
| 101 | all four | 1 | 38 | 2198 | 1 |

For \(z^{25p}=1\), take \(w=z^{25}\) in the representation from the simple quotient, then multiply the two generators by the cyclic character values \(z^{ap},z^{7ap}\).
This gives the matrices \(z^{ap}P,\ P^2\operatorname{diag}(z^{b_i})\).
In source coordinate \(i\) the four possible two-by-two blocks of the twisted rectangle have row offsets \(k=0,1,2,3\), respectively, with coefficients
\[
                    B,\quad -sD,\quad At,\quad -sCt .
\]
The exponent for offset \(k\) is \((k\bmod2)ap+\lfloor k/2\rfloor b_i\).
Stripping the minimal power in each column yields total degree at most \(2D_*\).
We verify next that this polynomial is full at some nonzero parameter.
The [individual column-width inequality](Yin_C_A0204_v1.md#the-bound-using-individual-column-widths) then gives \(\delta\le2D_* /(125p)\), since each of the \(25p\) unit phases has nullity \(5\delta\).
The largest of these five bounds is \(614/1375\).

## Minimum matchings and the full-rank specialization

A matching selects one block from every input column and each output row.
Its cost is the sum of the exponents just displayed.
The verifier enumerates all 120 row permutations, skipping those with a forbidden offset \(4\).
For each case of two minima it checks that the two choices differ in exactly two columns, one of which switches between offsets \(2,3\) and the other between \(0,1\).
Unlike the positive-residue test, this computation checks all four generator roots separately because the row offsets depend on their order.

For completeness, fix one minimum matching and label rows by their matched columns.
In each column subtract the cost of its matched entry from every exponent, giving all matched edges cost zero.
View every other possible entry as an edge from its column to its row with this adjusted cost.
A negative directed cycle would lower the cost of the matching by replacing its matched entries along the cycle, contradicting minimality.
Introduce a source with zero-cost edges to all vertices and let \(d_i\) be the integer shortest-path distances.
For an edge from \(i\) to \(j\) of adjusted cost \(c_{ji}\), the exponent \(c_{ji}+d_i-d_j\) is nonnegative.
These substitutions are scalar column and row powers and preserve rank at nonzero parameters.

At zero the surviving edges include the matched loops.
Every other simple directed cycle of surviving edges gives another minimum matching by using that cycle alone.
With a unique minimum, the polynomial at zero is thus triangular after ordering the vertices, and the matched diagonal blocks are units.
With two minima differing by a transposition, the only nontrivial strongly connected component is that pair because every edge in a strongly connected component belongs to a simple directed cycle.
Its two columns have possible offsets \(\{2,3\}\) and \(\{0,1\}\) respectively by the check.
Their corresponding adjacent output rows therefore give the diagonal block, up to reordering,
\[
       \begin{pmatrix}At&B\\-sCt&-sD\end{pmatrix}
       =\operatorname{diag}(I_2,-sI_2)
           \begin{pmatrix}A&B\\ C&D\end{pmatrix}
           \operatorname{diag}(tI_2,I_2).
\]
This too is invertible since the middle matrix is a block-column permutation of the assumed invertible coefficient matrix.
All the remaining diagonal blocks are single invertible corners times translations.
Thus in either case the specially gauged value at zero is boundedly invertible, and it remains invertible for sufficiently small nonzero parameters by norm continuity.
At such a parameter the original column-width gauge has the same full rank, which justifies the preceding interpolation bound.

## Assessment history

### Decision the-fifth-cyclotomic-quotient

| Field | Value |
| --- | --- |
| date | 2026-11-26T10:12 |
| status | proved |
| reason | Independent proof review and independent enumeration verified all split exceptional markings and the strict rank bound. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Uniform rank obstruction and vanishing at half nullity. |
| argument | [Reducing to simple marked modules](#reducing-to-simple-marked-modules) | All simple modules and positive representatives in degrees two and four. |
| argument | [Split primes and four exceptional cases](#split-primes-and-four-exceptional-cases) | Every split prime in the finite interval and all four exceptional primes. |
| argument | [Minimum matchings and the full-rank specialization](#minimum-matchings-and-the-full-rank-specialization) | Full rank in both unique and tied minimum matchings. |
| review | [The fifth cyclotomic quotient](../audits/reviews/Yin_R_A0191_v1.md#the-fifth-cyclotomic-quotient) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-fifth-cyclotomic-quotient)

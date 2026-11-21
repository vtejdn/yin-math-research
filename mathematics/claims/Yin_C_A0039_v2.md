---
author: Yin
---
# Finite-precision detection of the minimum support of an integral annihilator

## Statement

Fix a group \(G\), a nonzero \(A\in\mathbb Z[G]\), and a rational prime \(p\).
Put \(L=(\sum_g |A_g|^2)^{1/2}\).
Let \(s_{\mathbb C}\) be the least support size of a nonzero \(v\in\mathbb C[G]\) with \(Av=0\), or infinity if none exists.
For \(e\ge1\) let \(s_e\) be the least support size of \(v\in(\mathbb Z/p^e)[G]\) with \(Av=0\) and \(v\bmod p\ne0\), again allowing infinity.
Support for \(s_e\) counts all coefficients nonzero modulo \(p^e\).
For every positive cutoff \(s\) and \(p^e>L^s\),
\[
                  s_e\le s \quad\Longleftrightarrow\quad s_{\mathbb C}\le s.
\]
Moreover \(s_e\) increases weakly to \(s_{\mathbb C}\).
If the latter is finite then \(s_e=s_{\mathbb C}\) as soon as \(p^e>L^{s_{\mathbb C}-1}\).
If it is infinite and \(L>1\), every finite \(s_e\) satisfies \(s_e\ge e\log p/\log L\).
The left factor stays fixed, including its integral coefficients.

For the odd-prime witnesses \(ab=1,\ ac=0,\ c\ne0\) of Mghirbi–Douglas, every integral lift \(A\) of \(a\) has primitive finite annihilators at all precisions.
The same dichotomy therefore applies in each fixed torsion-free source group and fixed characteristic.
There is a finite search for each prescribed cutoff using verified equalities in a finite ball.
The source construction supplies the modular annihilators, while a bound small enough for complex transfer remains open.

## Argument

For a finite nonempty \(T\subset G\), let \(M_T\) be the ordinary integer matrix of left multiplication by \(A\) from columns \(T\) to rows \((\operatorname{supp} A)T\).
Its \(j\)-th column is a translate of the coefficient vector of \(A\) and has Euclidean norm \(L\).
A complex null vector on \(T\) implies a nonzero rational one by Gaussian elimination.
Clearing denominators and dividing by the integer gcd produces a primitive integral null vector, nonzero modulo every prime.
This proves \(s_e\le s_{\mathbb C}\).

If \(M_T v=0\bmod p^e\) and one coordinate of \(v\) is a unit, the adjugate of any \(|T|\)-square row minor shows that its determinant kills \(v\) modulo \(p^e\).
Thus each such minor is divisible by \(p^e\).
If the rational column rank is full, some minor has a nonzero determinant of absolute value at most \(L^{|T|}\) by Hadamard's inequality.
As \(L\ge1\), \(p^e>L^s\) excludes full rational rank whenever \(|T|\le s\).
This proves the equivalence.
Reduction from \(p^{e+1}\) to \(p^e\) preserves primitivity and can only decrease support, proving monotonicity.
Apply the equivalence below the least complex support to get the stationarity assertion (the size-one case also follows directly from primitivity and \(s_e\le1\)).
If no complex annihilator exists, the minor bound for each finite \(s_e\) gives the stated growth.
For \(L=1\), \(A\) is a signed group unit and all the minima are infinite.

## All precisions from one modular right inverse

Write \(B,C\in\mathbb Z[G]\) for any finite lifts of \(b,c\), respectively, and \(E=1-AB\).
Then \(E,AC\in p\mathbb Z[G]\).
For every \(e\ge1\) set
\[
 C_e=C-B\left(\sum_{j=0}^{e-2}E^j\right)AC,
 \qquad AC_e=E^{e-1}AC\in p^e\mathbb Z[G],
\]
using an empty sum at \(e=1\).
The equality follows by multiplying by \(A\) on the left and using \(AB=1-E\), with no commutation of \(A\) and \(C\).
All the sums have finite support and \(C_e\bmod p=c\ne0\).
This applies to the actual \(a,b,c\) and group supplied by [MD26, Proposition 7.11 and proof of Theorem C, PDF p.30](../literature/pdf/MD26.pdf#page=30).
The group can be held fixed while \(e\) varies.
Either \(A\) has a finite complex annihilator, or these and every other primitive precision-\(e\) annihilators satisfy the linear support lower bound.
The explicit geometric sums provide no upper bound below that threshold.
This fixes \(A\) and allows any nonzero residue annihilator in defining \(s_e\); [v1](Yin_C_A0039_v1.md#statement) varies coefficients subject to a specific residue point and permits ramification.

## A finite ball for a support cutoff

Connect distinct \(t,t'\in T\) if \((\operatorname{supp}A)t\) and \((\operatorname{supp}A)t'\) intersect.
Different components contribute to disjoint output rows.
Starting from a primitive modular witness, keep a component containing a unit coordinate.
For a complex witness keep a component with a nonzero coefficient.
Right translation puts one vertex at the identity and preserves the kernel equation.
Every vertex in a connected set of at most \(s\) lies at distance at most \(s-1\) from that vertex by steps of left multiplication in \(D=(\operatorname{supp}A)^{-1}\operatorname{supp}A\).
Since \(1\in D\), it suffices to check all nonempty subsets of at most \(s\) elements in \(D^{s-1}\).
At a fixed precision primitive solvability on each subset can be tested by finite enumeration or integer Smith normal form.
The construction needs the actual group identifications among these elements and output rows.
It makes no effective word-problem assumption for arbitrary groups.

## A fixed factor can differ from its support pattern

In \(G=\langle r,t\mid r^7=t^2=1,\ trt=r^{-1}\rangle\), write
\[
 U=r+r^2+r^4,\quad X=1-U,\quad A=X+t,\quad B=X^*-t.
\]
The six nonzero differences of \(1,2,4\bmod7\) run through all nonzero residues, and \(\{1,2,4\}\) and its negative partition those residues.
Hence \(UU^*=3+\sum_{i=1}^6r^i\), \(U+U^*=\sum_{i=1}^6r^i\), and \(XX^*=4\).
The identities \(tX^*=Xt\) and \(tX=X^*t\) give \(AB=BA=3\).
Thus \(A\) has a primitive annihilator \(B\) modulo three, is invertible over \(\mathbb C[G]\), and admits no primitive annihilator modulo \(3^e\) for \(e\ge2\) since \(BA=3\).
Yet \((X+2t)(X^*-2t)=0\) is a complex zero product on exactly the same two supports.
The group has torsion and tests the distinction between a fixed factor and freely chosen coefficients.

## Assessment history

### Decision fixed-factor-precision

| Field | Value |
| --- | --- |
| date | 2026-11-21T03:45 |
| status | proved |
| reason | Independent inspection supports the entire statement and argument at their stated scope. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Fixed integral coefficients, minimum support over precisions and over the complex numbers. |
| argument | [Proof](#argument) | Full minor bound, fixed-group lift construction, connected support search and dihedral calibration. |
| review | [Whole finding](../audits/reviews/Yin_R_A0070_v2.md#whole-finding) | Complete independent finding on the final proof and direct inputs. |
| dependency | [MD26 source interface](../audits/literature/MD26/Yin_U001.md#md26-u001) | Proposition 7.11 and the root-protected application yielding nonzero c. |

## Current assessment

[Selected decision](#decision-fixed-factor-precision)

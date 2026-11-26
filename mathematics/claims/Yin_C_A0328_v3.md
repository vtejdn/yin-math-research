---
author: Yin
---

# Only the sixteenth cyclotomic action remains at the order-sixteen marking of degrees one and six

## Statement

Under the [order-sixteen half-kernel hypotheses](Yin_C_A0328_v1.md#statement) write \(M=H'/H''\), with \(S\) conjugation by \(s\).
Then
\[
                 M/\Phi_8(S)M=0,\qquad S^8=-I\text{ on }M,\qquad
                         |M|\le 2^{40},\qquad |M|\equiv1\bmod16 .
\]
The full metabelian quotient is \(M\rtimes C_{16}\) and has order at most \(2^{44}\).
If \(M\ne0\), each nonidentity element of the cyclic complement fixes only zero on \(M\).
The group \(M\) is a finite odd-order cyclic module over \(\mathbb Z[\zeta_{16}]\).
Its vanishing is still open under these conditions.

## The complete interval test in eight coordinates

Put \(M_8=M/\Phi_8(S)M\), where \(\Phi_8(X)=X^4+1\).
The [positive-coordinate approximation](Yin_C_A0328_v2.md#approximating-a-half-turn-by-an-actual-character) gives \(|M_8|\le16^4\), and the [fourth-root calculation](Yin_C_A0328_v2.md#statement) gives \(\Phi_8(S)\Phi_{16}(S)M=0\).
Assume \(M_8\ne0\) and take a simple quotient \(E\) over \(\mathbb F_p[S]\) for some prime divisor \(p\) of its order.
The prime is odd and \(E=\mathbb F_p(r)\) for a primitive eighth root \(r\) representing the inverse action.
Its degree \(f=\operatorname{ord}_8(p)\) is one or two, and \(p^f\le16^4\).
The split marked quotient provides, for each \(z^{16p}=1\) and each \(\mathbb F_p\)-linear functional, the following marked representation on eight sites:
\[
              s\mapsto z^{ap}P,\qquad
              t\mapsto P^6\operatorname{diag}(z^{b_i}),\qquad
              b_i\equiv6ap+16e_i\bmod16p,\quad e_i=\lambda(r^i).
\]
These are tensor products of the cyclic character and the induced additive character at \(z^{16}\), with \(Pe_i^{\rm site}=e_{i+1}^{\rm site}\).
The nonzero module generator and the cyclic index shift from the translation in the second mark are absorbed in the functional, as in the cited construction.
Opposite indices have \(e_{i+4}=-e_i\).

First test whether all eight residues have representatives in \((3p/8,5p/8)\).
In the degree-one case use one primitive eighth root \(r\) and \(e_i=c r^i\bmod p\).
It suffices to test the possible \(c\) in the interval and the first four coordinates, since the interval is invariant under negation modulo \(p\).
The interval test depends on the unordered orbit, hence gives the same outcome for all four primitive roots.
For \(f=2\), use each factor \(X^2-aX+b\) of \(\Phi_8\), with freely chosen first two consecutive coordinates \(x,y\), since \(1,r\) is a basis.
The other coordinates obey \(e_{j+2}=a e_{j+1}-b e_j\).
The factors are found by the two congruences \(a^3-2ab=0,\ b^2-a^2b+1=0\bmod p\), obtained by reducing \(X^4+1\).
For \(p\not\equiv1\bmod8\) no linear factor exists, so the two monic quadratics found are irreducible.
The interval test may restrict \(x,y\) to the indicated interval and check just the next two coordinates.

The [native verifier](../computations/programs/Yin_J_A0010/verify_eighth_phase_extrema.py) sieves all odd primes up to \(16^4\) and checks exactly 1614 split primes and the 86 quadratic factors at the 43 other primes satisfying \(p^2\le16^4\).
Exactly 41 split primes and 14 individual quadratic markings fail the interval test.
For each successful test the [two antiperiodic columns](Yin_C_A0328_v2.md#approximating-a-half-turn-by-an-actual-character) give \(\delta\le3h/16\) for \(h\)-square invertible \(B,C,{\cal P}\) with \(A\) or \(D\) also invertible.

## Both possible missing corners at the remaining 178 markings

At each failed split prime the verifier separately uses every primitive marked root.
At each failed quadratic it uses the actual factor and ranges over the initial values \(x,y\).
For \(0\le a\le8\) and the selected orbit it takes centered representatives of \(6ap+16e_i\bmod16p\) and allows an additional \(0,16p\) or \(-16p\) at site zero.
These choices preserve the actual representation at all \(16p\) phases.
Every resulting first edge has cost \(ap\).

Write \(n_i,m_i\) for the used second and first edges at \(i\).
All their possible pairs are recovered by choosing the \(n_i\in\{0,1\}\), choosing \(m_7\in\{0,1\}\), and solving \(m_i-m_{i-1}=n_{i-6}-n_i\) with binary periodic values.
At each intermediate site the numbers of inputs and output places agree, so choosing local bijections gives a matching for every retained pair as in the [edge-set proof](Yin_C_A0319_v1.md#costs-of-the-thirty-four-marked-representations).
There are 96 pairs.
Each cost is \(ap\sum_i m_i+\sum_i b_i n_i\).
At a site reached by exactly one input, its corner is prescribed by \(n_{i-6}\) for the incoming second edge and by \(m_i\) for the outgoing first edge.
The four pairs \((0,0),(1,0),(0,1),(1,1)\) respectively use \(B,A,-D,-C\), with their indicated translations.
A double input site uses the assembled invertible four-port block.

For every one of the 164 residual split markings and 14 residual quadratic markings the program finds a choice of exponents with cost spread \(D_*\) and a unique extremal pair of used edge sets such that
\[
                         \frac{D_*}{8\cdot16p}\le\frac{11}{48}.
\]
It performs this test for each possible missing corner \(A\) or \(D\), retaining a certificate only if no single-input site at the chosen end uses that corner.
The two certificates may use different parameters and different extrema.
The [local endpoint blocks](Yin_C_A0293_v1.md#invertibility-when-the-extremum-has-unique-edge-sets) are therefore invertible with exactly the known corner assumptions.
The [matching-spread estimate](Yin_C_A0219_v1.md#statement) and regular absorption give \(\delta\le11h/48\) in the actual representation.
At size two this is \(11/24<1/2\).
Together with the successful interval tests, this excludes every simple quotient of \(M_8\), so \(M_8=0\).

The endomorphism \(\Phi_8(S)\) is surjective and hence invertible on the finite group \(M\).
The previous annihilator \(\Phi_8(S)\Phi_{16}(S)\) then gives \(\Phi_{16}(S)=S^8+I=0\) on \(M\).
It follows that \(M=M_{16}\), whose order bound is \(32^8=2^{40}\), and cyclic generation over the cyclotomic ring follows from the [marked module splitting](Yin_C_A0328_v2.md#approximating-a-half-turn-by-an-actual-character).
Any nontrivial subgroup of \(C_{16}\) contains the eighth power, acting by negation on the odd-order \(M\).
Hence the orbits on \(M\setminus\{0\}\) all have length sixteen.

## Assessment history

### Decision the-finite-eighth-root-sieve

| Field | Value |
| --- | --- |
| date | 2026-11-26T17:25 |
| status | proved |
| reason | The complete eighth-root tests leave a module of order at most two to the fortieth power with only the sixteenth cyclotomic action. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The complete eighth-root tests leave a module of order at most two to the fortieth power with only the sixteenth cyclotomic action. |
| argument | [The complete interval test in eight coordinates](#the-complete-interval-test-in-eight-coordinates) | The complete interval test in eight coordinates. |
| argument | [Both possible missing corners at the remaining 178 markings](#both-possible-missing-corners-at-the-remaining-178-markings) | Both possible missing corners at the remaining 178 markings. |
| dependency | [Corner ranks and dihedral images at order sixteen](Yin_C_A0328_v1.md#statement) | The earlier subgroup and rank conclusions used here. |
| review | [Corner ranks and dihedral images at order sixteen](../audits/reviews/Yin_R_A0228_v1.md#corner-ranks-and-dihedral-images-at-order-sixteen) | Independent inspection of the earlier statement and proof. |
| dependency | [The fourth-root component and the size bound](Yin_C_A0328_v2.md#statement) | The earlier subgroup and rank conclusions used here. |
| review | [The fourth-root component and the size bound](../audits/reviews/Yin_R_A0228_v1.md#the-fourth-root-component-and-the-size-bound) | Independent inspection of the earlier statement and proof. |
| review | [The finite eighth-root sieve](../audits/reviews/Yin_R_A0228_v1.md#the-finite-eighth-root-sieve) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-the-finite-eighth-root-sieve)

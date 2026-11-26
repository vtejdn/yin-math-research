---
author: Yin
---

# Circulations and cyclotomic norms of matching ties on twenty-five coordinates

## Statement

Consider the 25-coordinate characters at the order-25 marking of a two-generator group \(H=\langle s,t\rangle\) with abelianization \(C_{25}\), \(s\mapsto1,\ t\mapsto7\).
On a simple \(\Phi_{25}\) quotient of the commutator abelianization in characteristic \(p\ne5\), write its field as \(E=\mathbb F_p(\alpha)\) with \(\alpha\) of order 25.
For an additive functional \(\lambda:E\to\mathbb F_p\), let \(w_i\) be integral lifts of \(\lambda(\alpha^i)\), \(i\bmod25\).
The [marked orbit construction](Yin_C_A0217_v1.md#characters-from-a-single-coupled-orbit) gives \(p\) true unitary twists with these exponents, retaining the original group translations in the four-site matrix.
In its block support the arrows from input \(i\) have row offsets \(0,1,7,8\) and costs \(0,0,w_i,w_i\), respectively.
Use all four sites when computing the matching costs \(L,U\) as in the [two-end interpolation theorem](Yin_C_A0219_v1.md#statement).

Let \(D\) have vertices \(\mathbb Z/25\) and directed unit-capacity edges \(i\to i+1\), \(i\to i+7\), of respective costs zero and \(w_i\).
The matching costs are precisely the costs of integral circulations on \(D\).
For an oriented simple cycle \(C\) in its underlying undirected graph, write
\[
                   F_C(X)=\sum_{i=0}^{24}d_iX^i,\qquad
                   d_i=\text{signed use of the edge }i\to i+7 .
\]
These signs take values in \(\{-1,0,1\}\).
Put \(\zeta=\exp(2\pi i/25)\).
For the cycles with \(F_C(\zeta)\ne0\), the maximum of the absolute norms from \(\mathbb Q(\zeta)\) to \(\mathbb Q\) is \(5314180901\).
Thus all such \(F_C(\alpha)\) are nonzero for every quadratic marking at \(p>100000\), and for every split marking at \(p>5314180901\).
These conclusions hold without enumerating primes in either range.

There is one simple undirected cycle with zero projection and there are 31 others with \(F_C(\zeta)=0\).
In each of these cases the cycle is the fivefold lift of a simple cycle on the quotient graph modulo five.
For a quadratic marking with \(p>57515629\) one can choose a single nonzero \(\lambda\) with centered representatives \(w_i\) for which \(4(U-L)<25p\) and every simple cycle of zero cost satisfies \(F_C(\zeta)=0\).
This supplies both a strict width and a restriction on the possible ties for that same representation.
To use interpolation to exclude half nullity still requires an injective specialization of the actual polynomial at a nonzero parameter.

## Projecting a matching onto two directed edge sets

At each source \(i\) let \(n_i\) indicate the choice of the translation by seven.
The intermediate vertex is \(j=i+7n_i\).
Both options from this intermediate vertex end at \(j\) or \(j+1\).
There are \(m_j=1-n_j+n_{j-7}\) inputs at \(j\).
Let \(x_j\) of them continue to \(j+1\).
For a perfect matching \(x_j\in\{0,1\}\) and \(m_j-x_j+x_{j-1}=1\).
These equalities are exactly the conservation law
\[
                      n_j+x_j=n_{j-7}+x_{j-1}
\]
for the two edge indicators on \(D\).
Conversely any integral circulation gives \(m_j-x_j=1-x_{j-1}\in\{0,1\}\), so exactly the required number of the \(m_j\) inputs can continue and each output receives one input.
At \(m_j=2\) there are two assignments of the incoming inputs to the two outgoing choices.
They use identical edge indicators and have the same cost.
The two-step arrow from \(i\) to \(i+8\) uses one edge of each type in this construction.
Every matching using a given flow has cost \(\sum_i n_iw_i\).

The difference of any two feasible circulations is an integral circulation with signs on the changed edges.
Starting from the first circulation, orient each changed edge in the direction in which it can be increased, reversing it if its old flow was one.
Conservation decomposes these directed changes into simple directed cycles in the residual graph.
Each such cycle can separately be used to alter the original circulation within its capacities.
Hence if the two flows are minimizing, every cycle in this decomposition has zero cost; maximizing follows by negating all costs.
An off-extremum cycle need not arise in a tie.
The projection does not record the assignment choices at a vertex with \(m_j=2\).

Equivalently, a chosen set of seven-step edges with indicators \(n_i\) can occur in a perfect matching exactly when the sliding sums \(W_j=\sum_{h=0}^6n_{j-h}\) have range at most one.
Indeed the conservation law requires \(x_j+W_j\) to be constant.
Conversely a constant can be chosen to make every \(x_j\) binary under this range condition.
The equivalence covers constant indicators as well.

## The norm calculation and the cycles descending modulo five

A zero complex evaluation is equivalent to \(\Phi_{25}\mid F_C\).
Since \(\Phi_{25}=1+X^5+X^{10}+X^{15}+X^{20}\) and \(\deg F_C\le24\), this is equivalent to the coefficients \(d_i\) being constant within each residue class modulo five.
Write \(b_i\) for the signed use of the edge \(i\to i+1\) in the same oriented cycle.
The conservation law gives \(b_i-b_{i-1}=d_{i-7}-d_i\).
If \(d\) has period five, summing this equation over five consecutive indices gives \(b_i=b_{i-5}\).
Both oriented edge sets therefore descend modulo five.
Translation by five acts freely on the simple cycle and preserves its directed orientation.
The quotient is a simple cycle: all five lifts of each occupied vertex belong to the original cycle and become a single vertex under this action.
A traversal of that quotient has displacement a nonzero multiple of five modulo 25, since zero displacement would give five disconnected lifted cycles.
Reading the unit and seven-step edges as \(s,t\) and their reverse edges as inverses thus gives a projected word with nonzero class in \(H_{\rm ab}\).
The full lifted traversal reads the fifth power of that word up to choice of base vertex.
In a torsion-free \(H\) this group word is nontrivial.
This word fact by itself gives no rank verdict for a matrix with several tied assignments.

For an arbitrary projection, let \(N_C=\prod_{1\le k<25,\ 5\nmid k} F_C(\zeta^k)\).
It is a nonnegative integer by conjugate pairing.
Orthogonality of the 25 Fourier modes gives
\[
        \sum_{k=0}^{24}|F_C(\zeta^k)|^2=25\sum_i d_i^2\le625,
        \qquad N_C\le (625/20)^{10}=(125/4)^{10}.
\]
The [exact cycle verifier](../computations/programs/Yin_J_A0008/verify_cycle_norms.mjs) visits simple cycles with least vertex fixed and only the orientation having the lesser of its two neighbors first.
It covers 2303657 undirected cycles.
Rotation of the indices and reversal of orientation preserve the norm and the zero test.
For a quadratic marking with nonzero field evaluation they give at most 25 distinct vanishing lines in the dual over \(\mathbb F_p\) per projection class.
Encoding the positive and negative masks and identifying projections under these two operations gives 92032 classes.
Seven classes have zero norm, comprising one zero projection and 31 other cycles before identification.
For each class the verifier evaluates the product over all twenty primitive roots in each of the fields of orders \(32000251,32000651\).
It checks that both moduli are prime, that the chosen roots have order 25, and that the product of the two moduli exceeds \((125/4)^{10}\).
The product is the reduction of the integer norm, since it is the resultant of the monic \(\Phi_{25}\) and \(F_C\).
Chinese remaindering therefore recovers \(N_C\) exactly and gives the stated maximum over all classes.

If \(F_C(\alpha)=0\), the map \(X\mapsto\alpha\) sends \(\mathbb Z[X]/(\Phi_{25},F_C)\) onto \(E\).
For \(N_C\ne0\) this source is a finite abelian group of order \(N_C\), since it is the cokernel of multiplication by \(F_C\) on the free integral cyclotomic ring of rank twenty.
Hence \(p^{[E:\mathbb F_p]}\mid N_C\).
This proves both characteristic bounds, uniformly for every primitive \(\alpha\) of the indicated degree.

## Quadratic characters with a strict spread

For a quadratic marking at \(p>100000\) choose \(\lambda\) uniformly on the affine line of functionals with \(\lambda(1)=1\).
No \(\alpha^i\) for \(1\le i<25\) belongs to \(\mathbb F_p\), since its order is five or twenty-five and \(p\equiv-1\bmod25\).
Thus \(\lambda(\alpha^i)\) is uniform on \(\mathbb F_p\) for each of these 24 indices.
For the centered lifts \(w_i\) we obtain
\[
       \mathbb E\sum_i |w_i|=1+24\,\frac{p^2-1}{4p}=6p+1-\frac6p .
\]
Every difference of matching costs is at most \(\sum_i|w_i|\).
By Markov's inequality the number of choices with \(\sum_i |w_i|<25p/4\) is at least \((p-4+24/p)/25\).

For any of the 92025 nonzero-norm classes the equation \(\lambda(F_C(\alpha))=0\) cuts out a linear line in the dual of \(E\).
Each rotation gives at most one such line and negation gives the same line.
Each of these lines intersects \(\lambda(1)=1\) in at most one point, since it passes through the origin and the chosen affine line does not.
At most \(25\cdot92025=2300625\) choices are excluded.
For \(p>25\cdot2300625+4=57515629\), fewer choices are excluded than meet the strict spread bound.
At any remaining choice, an integer zero cost reduces to \(\lambda(F_C(\alpha))=0\), so it can only occur on the zero-norm cycles.

For those cycles the finite-field evaluation always vanishes; their lifted integer costs can still differ from zero by multiples of \(p\).
For a split marking the norm bound also excludes a zero field value for each nonzero-norm cycle above its stated cutoff, but each remaining scalar multiple then gives the same nonvanishing test.
The quadratic averaging argument uses both dimensions of the dual and does not extend that spread estimate to a single split line.

## Assessment history

### Decision circulation-cycles-and-their-integral-norms

| Field | Value |
| --- | --- |
| date | 2026-11-26T11:08 |
| status | proved |
| reason | Independent graph enumeration, exact arithmetic and complete proof review verified the norm and direction bounds. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The graph, actual twists, norm range and limits of the character tests. |
| argument | [Projecting a matching onto two directed edge sets](#projecting-a-matching-onto-two-directed-edge-sets) | The choices at doubled intermediate vertices and the residual cycle decomposition. |
| argument | [The norm calculation and the cycles descending modulo five](#the-norm-calculation-and-the-cycles-descending-modulo-five) | All undirected cycles, fivefold lifts, integer norms and divisibility. |
| argument | [Quadratic characters with a strict spread](#quadratic-characters-with-a-strict-spread) | The affine line count and the simultaneous conditions on a character. |
| review | [Circulation cycles and their integral norms](../audits/reviews/Yin_R_A0195_v1.md#circulation-cycles-and-their-integral-norms) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-circulation-cycles-and-their-integral-norms)

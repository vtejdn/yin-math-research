---
author: Yin
---

# Single cycles at the initial matrix of a four-site transfer

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with abelianization \(C_{25}\) and marks \(1,7\).
Set \(N=H'\), \(M=N_{\rm ab}\) and \(S=\operatorname{Ad}_s\) on \(M\).
Suppose \(M/\Phi_{25}(S)M\) has a simple quotient of prime characteristic \(p\) on which \(S^{-1}\) has primitive eigenvalue \(\alpha\) of order 25, in \(E=\mathbb F_p(\alpha)\).
Use the 25-vertex directed graph with edges \(i\to i+1,i\to i+7\) and the cycle polynomials \(F_C\) of the [circulation calculation](Yin_C_A0225_v1.md#statement).
Write \(\zeta=\exp(2\pi i/25)\).
For each oriented simple cycle \(C\), the coefficients of \(F_C\) are the signed uses of the seven-step edges in that cycle.

Suppose \(p>200\) and there is a nonzero linear functional \(\lambda:E\to\mathbb F_p\) such that
\[
       F_C(\zeta)\ne0\quad\Longrightarrow\quad \lambda(F_C(\alpha))\ne0
       \qquad\text{for every simple cycle }C .
\]
Then for the original four-site matrix \(K=B+At-s(D+Ct)\) one has
\[
                          \dim_H\ker K< h/4
\]
for complex \(h\)-by-\(h\) corners \(A,B,C,D\) all invertible, with \({\cal P}=\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) invertible.
In particular at size two the nullity is strictly less than one half.
For each quadratic marking \(p\equiv-1\bmod25\) with \(p>2300625\) the required functional exists.
For a split marking \(p\equiv1\bmod25,\ p>200\), it exists whenever \(p\) divides none of the nonzero integer norms in the cycle calculation.
These quantitative bounds do not assume scalar group-ring injectivity.

## Choosing a multiple on a fixed line of functionals

Write \(a_i=\lambda(\alpha^i)\), and choose any nonzero coordinate \(a_j\), which exists since the powers of \(\alpha\) span \(E\).
For \(c\in\mathbb F_p\) let \(f(c)\) be the distance of an integer representing \(c\) to the nearest multiple of \(p\).
The centered widths have sum \(D(c)=\sum_i f(ca_i)\).
Put \(m=(p-1)/2\), \(I=\{0,\ldots,m-1\}\subset\mathbb F_p\).
Intersection of two translates of this interval gives \(f(x)=m-|I\cap(I+x)|\).
For the normalized Fourier transform \(\widehat f(k)=p^{-1}\sum_x f(x)\exp(-2\pi ikx/p)\) this implies
\[
 \widehat f(0)=(p^2-1)/(4p),\qquad
 \widehat f(k)=-p^{-1}\left|\sum_{x\in I}\exp(-2\pi ikx/p)\right|^2
 \quad(k\ne0).
\]
In particular \(-\widehat f(1)=\cos^2(\pi/(2p))/(p\sin^2(\pi/p))>p/16\), using \(p\ge3\), \(\cos^2(\pi/(2p))\ge3/4\), and \(\pi^2<10\).
Weight uniform \(c\) by \(1+\cos(2\pi a_jc/p)\), a nonnegative weight of mean one.
The mean of each \(f(ca_i)\) is at most \((p^2-1)/(4p)\), and the cosine correction is nonpositive for each nonzero \(a_i\), by the displayed transform after a change of variable.
The \(j\)-th correction is strictly smaller than \(-p/16\); a zero coordinate contributes nothing.
Thus the weighted mean of \(D\) is strictly smaller than \(25p/4-p/16\).
The point \(c=0\) has weighted mass \(2/p\) and contributes zero.
If every other \(D(c)\) were at least \(25p/4\), the weighted mean would be at least \(25p/4-25/2\), a contradiction for \(p>200\).
Fix such a nonzero \(c\) and centered representatives \(w_i\) of \(ca_i\).
Then \(4\sum_i|w_i|<25p\), and multiplication by \(c\) preserves every nonvanishing cycle test.

Give the unit-step and seven-step edges respective costs zero and \(w_i\).
The [marked orbit formula](Yin_C_A0217_v1.md#characters-from-a-single-coupled-orbit) gives genuine twists \(s\mapsto P,\ t\mapsto P^7\operatorname{diag}(z^{w_i})\) at every \(z^p=1\).
The corresponding polynomial for nonzero \(z\) retains the original group translations.
Its block matching costs \(L,U\) satisfy \(U-L\le\sum_i |w_i|\) because each input contributes either zero or \(w_i\).
We show this same pencil has a nonzero parameter with full regular rank.

## Reversing the edges of a minimum circulation

At input site \(i\) use outgoing vectors \(X_i,Y_i\) on the seven-step and the unit-step edges, respectively.
The incoming values at \(i\) are \(T_i=z^{w_{i-7}}tX_{i-7}\) and \(S_i=sY_{i-1}\).
The kernel equations are equivalent to the local relations
\[
                  S_i=B X_i+A T_i,\qquad Y_i=D X_i+C T_i .
\]
Indeed the second equation defines \(Y_i\) from \(X\), and substituting it into the first gives exactly the twisted rectangle.
At a vertex any two of its four port values \(X_i,T_i,S_i,Y_i\) determine the other two by bounded complex matrices.
The pair \(X_i,T_i\) gives the outputs via \({\cal P}\), and the pair \(S_i,Y_i\) via its inverse.
For a mixed pair solve with the one missing input coefficient, which is an invertible corner.
After selecting any two ports as inputs, each individual block of the resulting two-output linear transformation is invertible: prescribing one of those inputs and either output also determines all four ports.
All port spaces have dimension \(h\) before tensoring with \(\ell^2(H)\).

Choose an integral circulation minimizing the cost and reverse exactly the edges on which it has value one.
Such a minimum exists by the [unit-capacity matching equivalence](Yin_C_A0225_v1.md#projecting-a-matching-onto-two-directed-edge-sets).
At each vertex equal numbers of edges enter and leave in the selected circulation, so after reversal there are again two incoming and two outgoing edges.
Use the preceding local solution with this new partition.
A reversed edge carries the inverse translation and the negative of its former exponent.
For \(z\ne0\) all changes are reversible: a reversed output is the former input of that edge, obtained by applying its original invertible transport to its former output.
The new outgoing system and the original kernel therefore have bounded inverse identifications at every fixed nonzero \(z\).

There is no negative directed cycle in the residual orientation, since a simple negative one could be flipped to decrease the minimum.
Introduce a zero-cost source reaching every vertex, and let \(d_i\) be its shortest-path distances.
Scale all ports at vertex \(i\) by \(z^{-d_i}\).
An edge \(u\to v\) of residual cost \(b\) now has exponent \(b+d_u-d_v\ge0\).
The new equations on the \(50\) outgoing ports have the polynomial form \(O=L_0 T(z)O\), where \(T(z)\) transports outgoing values to the incoming ports and \(L_0\) applies the constant local solutions.
At zero, only zero reduced-cost residual edges transmit values.

## Why each recurrent component has a single cycle

Every directed simple cycle in the zero reduced-cost graph has signed original cost zero.
Reduction of its integer cost modulo \(p\) gives \(c\lambda(F_C(\alpha))=0\).
By hypothesis it therefore satisfies \(F_C(\zeta)=0\).
The [period-five cycle argument](Yin_C_A0225_v1.md#the-norm-calculation-and-the-cycles-descending-modulo-five) shows that its oriented edge set is invariant under translation by five, including the pure unit-step cycle.

Consider any strongly connected component containing a directed cycle and keep only its internal directed edges.
Every one of these edges belongs to a directed simple cycle, so the union of these edges is invariant under the order-five translation, even if other edges of the ambient residual graph are not.
Translation takes a cycle to itself and therefore preserves the component and acts freely on its vertices and edges.
Write \(b\) for the first Betti number of the underlying connected quotient graph.
The component is a connected graph covering of degree five, so its real cycle space has dimension \(5(b-1)+1\), by counting edges and vertices.
Its invariant cycle space has dimension \(b\): an invariant flow is constant on each orbit of directed edges and the conservation equation at a lifted vertex is exactly the equation downstairs.
The directed simple cycles span the real cycle space of a strongly connected graph.
Indeed summing a directed cycle through each edge gives a strictly positive circulation, which can be added with sufficiently large coefficient to any signed real circulation to make it nonnegative.
A nonnegative circulation decomposes into directed simple cycles by successive subtraction of the least edge value along a positive cycle.
Every such cycle in this component is translation-invariant, so the two dimension counts agree and \(b=1\).
The component itself thus has cycle dimension one.
Every vertex has at least one outgoing internal edge and the numbers of internal edges and vertices agree, so it is a single directed simple cycle.

Order the components so all other zero-cost edges go forward.
In a homogeneous solution with incoming values from earlier components zero, a singleton without a loop has zero output.
In a cyclic component only one incoming edge and one outgoing edge per vertex belong to the cycle.
The local transformation from the internal input to the internal output has an invertible complex block, as shown above.
After a full circuit the internal port vector \(\xi\) must satisfy \(\xi=Vg\,\xi\) for an invertible complex \(h\)-by-\(h\) matrix \(V\) and the ordered product \(g\) of the actual group translations along the circuit.
The translations multiply in reverse chronological order for left convolution and commute with the complex blocks.
The circuit projects to a simple base cycle modulo five and is its fivefold lift.
The reverse chronological word of one base traversal has nonzero class modulo 25, since the lifted traversal moves its starting index by a nonzero multiple of five.
The ordered word \(g\) is the fifth power of that word; vertex-dependent complex blocks do not affect it.
Torsion-freeness implies \(g\) has infinite order.
By Fourier decomposition on its infinite cyclic subgroup, \(I-Vg\) is injective: \(\det(I-uV)\) is a nonzero scalar polynomial and its zeros have circle measure zero.
Thus the internal output vanishes, as do all outgoing values on this component.
Induction proves that \(I-L_0T(0)\) is injective.

The [generic polynomial rank estimate](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) gives full rank for the outgoing system at some nonzero parameter, since the zero evaluation already has full rank.
The corresponding original pencil is injective there.
Applying [matching-cost interpolation](Yin_C_A0219_v1.md#statement) at the \(p\) unit phases yields \(25p\dim_H\ker K\le h(U-L)<25ph/4\).

## The split and quadratic nonvanishing tests

For a split marking at a prime not dividing any nonzero integral norm, each \(F_C(\alpha)\) with nonzero norm is a nonzero element of \(\mathbb F_p\), by [reduction of the norm](Yin_C_A0225_v1.md#the-norm-calculation-and-the-cycles-descending-modulo-five).
The identity functional suffices.
For a quadratic marking with \(p>100000\), the same reduction shows that every one of these field elements is nonzero because its vanishing would force \(p^2\le5314180901\).
Each therefore excludes only one projective line of functionals in the two-dimensional dual.
The 92025 nonzero-norm projection classes from the cycle calculation allow at most 25 rotated exclusions per class, since sign has no effect on vanishing.
There are \(p+1\) projective directions.
Consequently \(p>2300625\) suffices to choose a permissible one.
The Fourier argument supplies the required small width on that very line.

## Assessment history

### Decision single-cycle-specialization-and-fourier-reweighting

| Field | Value |
| --- | --- |
| date | 2026-11-26T11:08 |
| status | proved |
| reason | Independent review verified the reversal of occupied edges, the cyclic component proof, regular injectivity and the same-character width estimate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The single-cycle test and its sufficient split and quadratic criteria. |
| argument | [Choosing a multiple on a fixed line of functionals](#choosing-a-multiple-on-a-fixed-line-of-functionals) | Finite Fourier coefficients, the zero multiplier and strict width for a genuine twist. |
| argument | [Reversing the edges of a minimum circulation](#reversing-the-edges-of-a-minimum-circulation) | The fifty-port system, invertible local choices and the integer potentials. |
| argument | [Why each recurrent component has a single cycle](#why-each-recurrent-component-has-a-single-cycle) | Cycle-space descent, the infinite-order group word and the nonzero full-rank evaluation. |
| argument | [The split and quadratic nonvanishing tests](#the-split-and-quadratic-nonvanishing-tests) | The norm and projective-dual counting hypotheses. |
| review | [Single-cycle specialization and Fourier reweighting](../audits/reviews/Yin_R_A0195_v1.md#single-cycle-specialization-and-fourier-reweighting) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-single-cycle-specialization-and-fourier-reweighting)

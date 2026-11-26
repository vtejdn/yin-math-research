---
author: Yin
---

# Antiperiodic lifts with nonzero sum on a half orbit at cyclic order twenty-six

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with abelianization \(C_{26}\), and use the marked images \(1,10\).
Write \(M=H'/H''\) and \(S=\operatorname{Ad}_s\) on \(M\).
Suppose \(M/\Phi_{26}(S)M\) has a simple quotient in characteristic \(p>725546\), with \(S^{-1}\) acting by multiplication by a primitive twenty-sixth root \(\alpha\) in \(E=\mathbb F_p(\alpha)\).
For a split prime omit the twenty primes listed by the cycle computation below.
There is no omitted prime in degree greater than one.
For any complex \(h\)-by-\(h\) matrices \(A,B,C,D\) with each corner and \(\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) invertible, the regular nullity of \(K=B+At-s(D+Ct)\) is strictly smaller than \(3h/13\).
The coordinate trace is unnormalized, and the estimate does not require scalar group-ring injectivity.

The proof uses weights with exact opposite values at indices thirteen apart.
For some zero evaluations of cycle polynomials the signed edge set need not be invariant under this half turn.
We choose the integer lifts to make every such cycle have nonzero integer cost before taking the initial matrix.

## Cycle polynomials after the half turn

Use the unit-capacity directed graph on \(\mathbb Z/26\) with steps one and ten.
For an orientation of a simple cycle in the underlying undirected graph let \(b_i,d_i\) be its signed uses of \(i\to i+1,i\to i+10\), respectively.
Use \(F_C(X)=\sum_{i=0}^{25}d_i X^i\), and define
\[
      G_C(Y)=\sum_{j=0}^{12}v_jY^j,\qquad v_j=(-1)^j(d_j-d_{j+13}).
\]
For every primitive twenty-sixth root \(\xi\) in characteristic zero or \(p>725546\) put \(\gamma=-\xi\).
It has order thirteen and \(F_C(\xi)=G_C(\gamma)\).
Thus at a complex primitive root the value is zero exactly when all thirteen \(v_j\) are the same integer \(k\), since the minimal polynomial of \(\gamma\) is \(1+Y+\cdots+Y^{12}\).

For nonconstant \(v\), subtract its least entry and divide all differences by their common positive divisor, which is at most four.
Translation of cycle indices changes \(v\) by a cyclic permutation and possibly an overall sign, and reversal also changes the sign.
Accordingly choose the least base-five encoding among the rotations of the normalized digits and of those with signs reversed and translated back to least entry zero.
This leaves the integer norm of the normalized polynomial unchanged: a rotation contributes a thirteenth root of unity and a constant contributes zero at \(\gamma\).
The resulting polynomial has the same vanishing test in the stated characteristics as the original cycle at the corresponding marking, up to a nonzero scalar and a cyclic power of \(\gamma\).

The [cycle verifier](../computations/programs/Yin_J_A0009/verify_phi26_cycles.mjs) enumerates each undirected simple cycle by starting at its least vertex and taking the smaller of its two neighbors first.
Of 4004289 cycles, 1509 have all \(v_j=0\) and 106 have all \(v_j=k\ne0\).
There are 30967 normalized nonzero classes up to rotation and sign.
Their positive integral norms take 1957 different values, the largest 2800409.
For exact reconstruction the program multiplies evaluations at all twelve primitive thirteenth roots modulo each of the primes 1001027 and 1001807.
Indeed Parseval for the original twenty-six coefficients bounds the sum over primitive modes of \(|F_C|^2\) by \(26\sum_i d_i^2\le676\).
Conjugate pairing and the arithmetic-geometric mean bound the positive norm by \((169/3)^6\), also an upper bound after division by the content.
The product of the two moduli exceeds this bound, so Chinese remaindering is exact.
Factoring the normalized norms gives 1345 distinct prime divisors and exactly twenty split divisors above 725546, with largest 1799617.
All computations up to the modular products have checked integer ranges and the Chinese reconstruction uses arbitrary-precision integers.

If a nonzero normalized polynomial vanishes at \(\beta=-\alpha\) in \(E\), its integral norm is divisible by \(|E|\).
Indeed the additive cokernel of multiplication by the polynomial on \(\mathbb Z[Y]/(\Phi_{13})\) has order the absolute determinant and surjects onto \(E\) by evaluation.
Thus in degree at least two none of these field elements vanishes at the stated primes, since \(p^2>2800409\).
In the split case the same holds off the twenty selected divisors.
For a nonzero field element its annihilator in the dual of \(E\) is a proper hyperplane.
Each normalized class gives at most thirteen such hyperplanes because the cyclic powers have order thirteen and scalars do not change a vanishing condition.
The union has size at most \(13\cdot30967\,|E|/p<|E|\).
There is therefore a nonzero linear functional \(\lambda:E\to\mathbb F_p\) for which \(\lambda(F_C(\alpha))\ne0\) for every cycle of nonzero complex evaluation.

## A short lift on the selected line

Consider the line of character vectors \((c\lambda(\beta^j)/p)_{j=0}^{12}\) modulo one for \(c\in\mathbb F_p\), with field residues lifted to integers in this notation.
The vectors are distinct because the orbit spans \(E\).
They sum to zero modulo one, since \(\Phi_{13}(\beta)=0\).
In \(V=\{x\in\mathbb R^{13}:\sum_j x_j=0\}\) their lifts form a lattice \(\Lambda\) containing \(\Delta=V\cap\mathbb Z^{13}\) with index \(p\).
Each vector can be lifted to have exact sum zero by adding an integer to one coordinate.
The Gram matrix of the basis \(e_j-e_{12}\), \(0\le j<12\), of \(\Delta\) has determinant thirteen, so \({\rm covol}(\Lambda)=\sqrt{13}/p\).

For \(B_1=\{x\in V:\sum|x_j|<1\}\), its induced Euclidean volume is
\[
        {\rm vol}(B_1)=\sqrt{13}\,\frac{\binom{24}{12}}{2^{12}12!}.
\]
To compute it choose \(a\) positive coordinates and \(13-a\) negative ones.
For a common total \(u\) of either sign one has \(0<u<1/2\).
In the chart omitting one negative coordinate the volume measure is \(\sqrt{13}\) times Lebesgue measure.
Slicing the positive coordinates by their sum gives \(u^{a-1}/(a-1)!\,du\), and the \(12-a\) free negative magnitudes have volume \(u^{12-a}/(12-a)!\).
Integrating and summing over sign choices yields the displayed formula by \(\sum_a\binom{13}{a}\binom{11}{a-1}=\binom{24}{12}\).
Since
\[
                725546 < 2^{12}12!/\binom{24}{12}<725547 ,
\]
the volume is greater than \({\rm covol}(\Lambda)\) at all the indicated primes.
Two points of the open ball in the same lattice coset give a nonzero \(x\in\Lambda\) with \(\sum |x_j|<2\), by the fundamental-domain volume argument.
Every nonzero vector of \(\Delta\) has norm at least two, hence \(x\) represents a nonzero multiple \(c\lambda\) on the selected line.

Put \(y=x+e_0\).
Then \(\sum_j y_j=1\), \(\sum_j|y_j|<3\), and \(py_j\) is an integer.
Set \(w_i=(-1)^i p y_{i\bmod13}\) for \(i\bmod26\).
These are valid lifts of \(c\lambda(\alpha^i)\) since \(\beta=-\alpha\), and \(\sum_i|w_i|<6p\).
They satisfy \(w_{i+13}=-w_i\).
The nonzero sum of the thirteen \(y_j\) is essential.

## Regular rank of the initial matrix

For every \(z^p=1\), the [actual marked representation](Yin_C_A0210_v1.md#a-representation-test-for-a-single-finite-character) sends \(s\) to the forward cyclic shift \(P\) on 26 coordinates and \(t\) to \(P^{10}\operatorname{diag}(z^{w_i})\).
The shift in \(ts^{-10}\) and the value of the cyclic generator in the simple quotient amount to a nonzero factor in the field, absorbed in the functional.
The group-theoretic input for the representation follows from \(S-I\) surjective and hence bijective on the finitely generated abelian \(M\), and \(s^{26}\) fixed and therefore zero in \(M\), giving the split metabelian quotient as in the [cyclic coefficient calculation](Yin_C_A0210_v1.md#the-cyclic-coefficient-module).
Here surjectivity holds because \(H/H'\) is cyclic generated by \(s\), so the commutators \([s,H']\) together with \(H''\) generate \(H'\).

For a simple cycle its signed cost is
\[
                 \sum_i d_iw_i=p\sum_{j=0}^{12} v_j y_j .
\]
If the complex evaluation does not vanish, reduction modulo \(p\) and the choice of functional rule out zero cost.
If \(v_j=k\) is constant, the cost is \(pk\).
Thus every cycle of integer cost zero has \(d_{j+13}=d_j\).
Conservation gives \(b_i-b_{i-1}=d_{i-10}-d_i\), so \(b_i-b_{i+13}\) is constant in \(i\).
Its sign changes under the half turn, therefore it is zero.
Every zero-cost simple cycle is invariant as an oriented edge set under translation by thirteen.

For completeness apply the [port reversal argument](Yin_C_A0226_v1.md#reversing-the-edges-of-a-minimum-circulation) with shifts one and ten on these 26 vertices.
A perfect matching chooses an intermediate vertex \(i+10n_i\) followed by a possible unit step.
The counts satisfy \(n_i+a_i=n_{i-10}+a_{i-1}\) for the two binary edge indicators \(n,a\), and conversely any such circulation supplies a matching.
The local port equations are \(S_i=B X_i+A T_i,\ Y_i=D X_i+C T_i\), with \(S_i=sY_{i-1},\ T_i=z^{w_{i-10}}tX_{i-10}\).
Reversing an integral minimum circulation keeps two incoming and two outgoing ports per vertex.
Any two ports determine the other two by corner and assembly invertibility, including after reversal.
Shortest-path weights on the residual orientation make its transported exponents nonnegative and preserve the kernels at nonzero parameters.

At zero every directed simple cycle of transmitting edges has integer cost zero, hence is invariant under translation by thirteen.
In a nontrivial strongly connected component every internal edge belongs to such a cycle, so the component is preserved by that fixed-point-free involution.
If the quotient component has first Betti number \(b\), the cycle space upstairs has dimension \(2(b-1)+1\), and its invariant subspace has dimension \(b\) by taking flows constant on edge orbits.
The directed simple cycles span the entire real cycle space by adding a positive circulation and decomposing into cycles.
All are invariant, so \(b=1\) and this component is a single directed simple cycle.
Its projection is a simple cycle downstairs, and one traversal downstairs shifts the initial vertex by thirteen modulo 26, since the lift is connected.
Consequently the ordered group word around the lifted cycle, read in reverse chronological order for left convolution, is the square of a word of nonzero image in \(C_{26}\).
This group element \(g\) has infinite order by torsion-freeness.
The return equation on the single cyclic port has coefficient \(I-V_0 g\) with \(V_0\) a complex invertible matrix.
It is injective by the bilateral shift decomposition of \(g\).
Triangular ordering of components proves injectivity at the zero endpoint and hence full rank at a nonzero parameter as in the [single-cycle specialization](Yin_C_A0226_v1.md#why-each-recurrent-component-has-a-single-cycle).

Finally the difference of the extremal matching costs is at most \(\sum_i |w_i|<6p\).
The [two-sided matching estimate](Yin_C_A0219_v1.md#statement) and absorption give \(26p\,\dim_H\ker K<6hp\), proving the claimed bound.

## Assessment history

### Decision antiperiodic-short-lifts-and-the-half-turn

| Field | Value |
| --- | --- |
| date | 2026-11-26T11:44 |
| status | proved |
| reason | Independent review verified the complete norm reconstruction, the lattice volume, the nonzero half-orbit sum and the original-group return equation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Large characteristics, both split and nonsplit markings, and the rank bound. |
| argument | [Cycle polynomials after the half turn](#cycle-polynomials-after-the-half-turn) | All simple cycles, normalized coefficients, exact norms and prime divisors. |
| argument | [A short lift on the selected line](#a-short-lift-on-the-selected-line) | The covolume on a chosen line, the open-ball volume and the translated short vector. |
| argument | [Regular rank of the initial matrix](#regular-rank-of-the-initial-matrix) | The fifty-two-port initial graph, nonzero half-turn displacement and interpolation. |
| review | [Antiperiodic short lifts and the half turn](../audits/reviews/Yin_R_A0197_v1.md#antiperiodic-short-lifts-and-the-half-turn) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-antiperiodic-short-lifts-and-the-half-turn)

---
author: Yin
---

# Cycle norms and at most four singular sites at the sixteenth cyclotomic marking

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free, with a cyclic quotient of order sixteen of marked degrees \(1,6\).
Assume there is a marked affine quotient over \(E=\mathbb F_p(\alpha)\), where \(\alpha\) is a primitive sixteenth root, \(p>40320\), \(s\) acts by \(\alpha^{-1}\), and \(t\) acts by the sixth power of that multiplier followed by a nonzero translation.
For \(K=B+At-s(D+Ct)\) with complex \(h\)-square coefficients assume \(B,C\) and the assembly \({\cal P}=\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) are invertible.
Assume either \(A\) or \(D\) is invertible and that each has numerical rank at least \(h-r\), \(r\ge0\).
With the unnormalized coordinate trace one has
\[
                         \dim_H\ker K<\frac{h}{8}+\frac r4 .
\]

Consequently, under the [order-sixteen half-kernel hypotheses](Yin_C_A0328_v1.md#statement), every prime divisor of \(M=H'/H''\) is at most \(40320\).
In particular the possible split simple quotients now have prime order at most \(40320\), and the same prime threshold applies in every higher field degree.
To see the application, [the previous reduction](Yin_C_A0328_v3.md#statement) gives \(M\) finite of odd order, cyclic over \(\mathbb Z[\zeta_{16}]\), and the actual split metabelian marked quotient.
For any \(p\mid |M|\) a simple quotient of \(M/pM\) supplies this affine action, since the actual translation generator survives.
At a half kernel the [corner costs](Yin_C_A0328_v1.md#degree-lost-at-singular-extreme-corners) give \(B,C\) invertible and at least one of \(A,D\) invertible.
Both \(A,D\) are nonzero.
Indeed if \(A=0\), then \(M(z)^{-1}=(Cz+D)B^{-1}\) for the transfer \(M(z)=(Az+B)(Cz+D)^{-1}\), and if \(D=0\) then \(M(z)=(A+Bz^{-1})C^{-1}\).
An invertible rational matrix in a numerical span of dimension at most two has a constant point correspondence, by normalizing at an invertible value and taking an eigenline of the remaining matrix.
For the inverse the correspondence reverses for the original transfer.
This would force integer rank by the [constant point test](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer), since the marked group cannot be cyclic at a fractional kernel.
Thus \(h=2,r=1\) are admissible and the strict estimate excludes \(p>40320\).

## Cycle values and a short line of actual characters

On the cyclic set of sixteen sites take first and second permutation edges \(i\to i+1,\ i\to i+6\).
Choose an orientation of any simple cycle in the underlying undirected graph and denote its signed second-edge usages by \(n_i\in\{-1,0,1\}\).
The value of \(\sum_i n_i X^i\) at a primitive sixteenth root equals that of the degree-at-most-seven polynomial with coefficients \(v_i=n_i-n_{i+8}\), \(0\le i<8\).
The [integer verifier](../computations/programs/Yin_J_A0010/verify_sixteenth_cycle_norms.py) lists every unoriented simple cycle once, starting at the least vertex and taking the smaller neighbor first.
Of the 15691 cycles, 91 have all \(v_i=0\); all other cycles give 4213 distinct signed vectors for the chosen orientations.
For a nonzero vector its value at a complex primitive root is nonzero by the minimal polynomial \(X^8+1\).
Their positive integral norms have 58 different values, the largest \(3298\).

For exact reconstruction the verifier multiplies the eight evaluations modulo the prime \(7340033\), using \(5712452\) and its odd powers as the primitive sixteenth roots.
Parseval on the original sixteen coefficients bounds the sum of the eight squared moduli by \(16\sum n_i^2\le256\).
The arithmetic-geometric mean bound on their product of moduli is \(32^4\), below the modulus.
Complex conjugation pairs the factors, so the positive norm is recovered exactly.
A zero evaluation at the marked root \(\alpha\) in characteristic \(p\) would force \(p\) to divide that norm, by reduction of the resultant modulo \(p\).
Hence all 4213 values are nonzero in \(E\).
Their individual annihilators in the \(\mathbb F_p\)-linear dual of \(E\) are proper hyperplanes.
Since \(4213<p\), choose one functional \(\lambda\) nonzero on all these values.

The \(p\) multiples of \((\lambda(\alpha^i)/p)_{0\le i<8}\) in \((\mathbb R/\mathbb Z)^8\), with field residues lifted to integers, are distinct since the powers span \(E\).
Their lifts form a lattice of covolume \(1/p\) containing \(\mathbb Z^8\).
The open \(\ell^1\)-ball of radius \(1/2\) has volume \(1/8!>1/p\), by summing the simplex volumes over the orthants.
Two distinct points of the ball therefore differ by a nonzero lattice vector \(v\) with \(\sum |v_i|<1\).
It cannot be an integer vector, so it represents a nonzero multiple \(c\lambda\).
Put \(w_i=p v_i,\ w_{i+8}=-w_i\).
These are integer lifts of \(c\lambda(\alpha^i)\) on all sixteen sites and \(\sum_i|w_i|<2p\).
Modulo \(p\), a cycle with nonzero complex evaluation still has nonzero cost with these second-edge weights and first-edge weights zero.

The [marked semidirect representation](Yin_C_A0328_v2.md#approximating-a-half-turn-by-an-actual-character) gives \(s\mapsto P,\ t\mapsto P^6\operatorname{diag}(z^{w_i})\) for each \(z^p=1\), with \(P\) the unit cyclic shift.
The translation generator and its shift by six are absorbed by composing the additive functional with a nonzero field multiplier.
The twisted rectangle retains the left group translations and has nullity \(16\dim_H\ker K\) at all \(p\) phases.

## The two possible reversal counts

For a perfect matching let \(m_i,n_i\in\{0,1\}\) record its used first and second edges.
These are exactly the unit-capacity circulations:
\[
                        m_i-m_{i-1}=n_{i-6}-n_i .
\]
Equality counts incoming matching paths and output places at each intermediate site, where equal counts admit a bijection.
Choose a minimum-cost circulation for \(w\).
Its complement is a maximum because costs of complementary sets sum to the cost of all edges.
For this circulation let \(a_*\) count sites with \(n_{i-6}=n_i=1,\ m_{i-1}=m_i=0\) and \(d_*\) count sites with \(m_{i-1}=m_i=1,\ n_{i-6}=n_i=0\).
Complementing interchanges these counts.
The same verifier tests each of the \(2^{16}\) second-edge sets and both initial values of \(m_{15}\), retaining precisely the binary periodic solutions of the displayed recurrence.
Among 2912 circulations the numbers having \(\min(a_*,d_*)=0,1,2,3,4\) are \(896,1024,736,224,32\), respectively.

At original site \(i\) the local variables obey \(S_i=B X_i+A T_i,\ Y_i=D X_i+C T_i\), where \(T_i,S_i\) are the incoming second and first edge values.
Reverse the used edges of the selected circulation.
If neither or both edge types are reversed at all four ports, the new incoming pair can be solved for the other pair using \(B^{-1}\) or \(C^{-1}\), respectively.
If the reversed edges pass straight through on the second mark alone, the new inputs are \(S_i,X_i\) and solving uses \(A^{-1}\).
For the first mark alone the inputs are \(Y_i,T_i\), using \(D^{-1}\).
The two remaining mixed choices solve directly with \({\cal P}\) or \({\cal P}^{-1}\). [Port equations](Yin_C_A0226_v1.md#reversing-the-edges-of-a-minimum-circulation)

Select the minimum or the complementary maximum so the possibly singular corner is required at at most \(\min(a_*,d_*)\le4\) sites.
When using the maximum negate all weights so that it becomes a minimum, which only interchanges the nonzero parameter with its inverse.
At each such site replace that one corner by an invertible numerical matrix differing by rank at most \(r\).
This is possible by a perturbation on the kernel into an image complement, arbitrarily small so the assembly stays invertible.
All other site coefficients are retained.
The polynomial with these local replacements may cease to be an actual representation twist.
At each nonzero parameter it differs from the original twisted rectangle by a matrix of rank at most \(4r\): each changed corner contributes a single translated block times a nonzero scalar phase.
Consequently at the \(p\) roots its nullity is at least \(16\dim_H\ker K-4r\).

## Full rank of the modified endpoint

After the replacements all selected local incoming pairs determine the corresponding outgoing pairs.
Reversing the used edges changes each transport to its inverse and negates its exponent, preserving the solution space at every fixed nonzero parameter.
Optimality prohibits negative residual cycles.
Changing the integer powers at the vertices by shortest-path potentials therefore makes all residual exponents nonnegative.
The zero-cost residual edge graph can only contain simple directed cycles whose original signed costs are zero.
For each such cycle the choice of \(\lambda\) forces \(n_i=n_{i+8}\) for the signed second-edge uses of the cycle itself.
For its signed first edges the conservation law then says \(m_i-m_{i+8}\) is constant in \(i\); it is zero since it changes sign on shifting by eight.
Thus every zero-cost simple directed cycle is invariant as an oriented edge set under translation by eight.

As in the [antiperiodic component argument](Yin_C_A0233_v1.md#regular-rank-of-the-initial-matrix), each recurrent strongly connected component is a single directed cycle.
Indeed every internal edge lies on a simple cycle and hence belongs to an invariant cycle in that component.
The component is a connected two-fold graph cover of its quotient under the half turn.
All directed simple cycles are invariant and they span the real cycle space (add a strictly positive circulation and decompose nonnegative circulations).
If the quotient has first Betti number \(b\), the cycle space upstairs has dimension \(2(b-1)+1\), and the invariant subspace has dimension \(b\) by descent of invariant flows.
Hence \(b=1\), and strong connectivity and equal edge and vertex counts give one simple directed cycle.
One turn of its projected cycle displaces a site by eight, so its original ordered group word has nonzero class modulo sixteen under the marked character.
One full upstairs traversal reads the square of this word, up to conjugation, and this group element has infinite order by torsion-freeness.
The constant numerical blocks along the two traversals need not agree.
The resulting return map is a constant matrix times this group element, since numerical matrices commute with translations.
Its difference from the identity is an affiliated unit by the nonzero polynomial \(\det(I-zD)\) for any numerical return matrix \(D\), including a singular one.

It follows by component order that the zero evaluation of the modified outgoing-port system has full regular rank.
Thus it is injective at some nonzero parameter by the [generic rank inequality](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration), and undoing the port substitutions gives an injective modified rectangle there.
Use the prescribed path costs before reversal to apply the [matching-spread estimate](Yin_C_A0219_v1.md#statement) to that modified rectangle.
Its spread is at most \(\sum_i|w_i|<2p\), since only second edges have nonzero cost and they are used at most once per matching.
Combining this upper bound with the rank cost of the modifications at the actual phases gives
\[
               p\big(16\dim_H\ker K-4r\big)
                     \le h(\max\mathrm{\ cost}-\min\mathrm{\ cost})<2hp .
\]
This proves the estimate and the stated prime cutoff.

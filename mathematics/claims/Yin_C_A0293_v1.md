---
author: Yin
---

# Five-point permutation images at the two largest residual abelian orders

## Statement

Let \(H=\langle s,t\rangle\) have a cyclic quotient \(C_n\) with degrees \((1,7)\) at \(n=25\), or \((1,10)\) at \(n=26\).
Assume that the complex \(h\)-square corners \(A,B,C,D\) and the assembly \(\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) are invertible.
For \(K=B+At-s(D+Ct)\), with unnormalized coordinate trace, the following upper bounds hold:
\[
\begin{array}{c|c|c}
 n&\text{additional marked image}&\dim_H\ker K\\ \hline
25&A_5&23h/125\\
26&A_5&29h/130\\
26&S_5,\quad s\ \text{odd},\ t\ \text{even}&31h/130 .
\end{array}
\]
These bounds only use the given homomorphisms, without an independence assumption between their images.

In particular let \(H\) be torsion-free with regular scalar group-ring injectivity and an abelian quotient of order 25 or 26.
If a complex two-by-two four-site rectangle has regular rank \(3/2\), every homomorphism \(H\to S_5\) has cyclic image.
At order 26 there is no subgroup of index five, and at order 25 there is precisely one, the inverse image of the unique index-five subgroup of \(C_{25}\).
This excludes nonsolvable five-point permutation images in the perfect-commutator cases at [order twenty-five](Yin_C_A0229_v1.md#consequences-for-the-original-half-increment) and [order twenty-six](Yin_C_A0237_v1.md#consequences-for-an-arbitrary-half-rank-marking).

## Integer lifts on individual permutation edges

Write \(d=7\) or \(10\), according to \(n\), and let \(x,y\) be the two marked permutations on \(\{0,1,2,3,4\}\).
For an integer \(c\) choose five exponents \(a_j\equiv c\bmod n\) and five exponents \(b_j\equiv dc\bmod n\).
Give the permutation edge \(j\to x(j)\) the multiplier \(z^{a_j}s\), and \(j\to y(j)\) the multiplier \(z^{b_j}t\).
Use the resulting weighted permutations \(S(z),T(z)\) in the block matrix
\[
                  Q(z)=B+AT(z)-S(z)(D+CT(z)).
\]
All coefficient corners act on the \(h\) internal coordinates.
At \(z^n=1\) the two auxiliary permutations are \(z^cP_x,z^{dc}P_y\).
These form a genuine representation of \(H\), obtained by tensoring the fixed permutation representation with the scalar character of its stated cyclic quotient.
Hence [regular absorption](Yin_C_A0194_v1.md#normal-form-for-a-pair-of-unitary-matrices) gives \(\dim_H\ker Q(z)=5\dim_H\ker K\) at all \(n\) distinct parameters.
The formula on arbitrary nonzero \(z\) is an ordinary Laurent polynomial with bounded operator coefficients.

A term from input \(j\) first either stays at \(j\) or takes its \(t\)-edge to \(y(j)\), arriving at an intermediate site \(k\).
It then either stays at \(k\) or takes the \(s\)-edge to \(x(k)\).
The four possibilities have coefficients \(B,At,-sD,-sCt\).
A perfect matching chooses one path per input, with the five final sites distinct.
Its cost is the sum of the exponents of its used edges, counted once each: the \(t\)-edge at \(j\) can be used only by input \(j\), and the \(s\)-edge at \(k\) can reach only output \(x(k)\).
In particular all matchings with the same two sets of used edges have the same cost.

## Invertibility when the extremum has unique edge sets

Suppose the minimum or maximum cost is attained by just one pair of used edge sets.
Negate all exponents if needed so the chosen end is the minimum.
The [minimum matching potentials](Yin_C_A0219_v1.md#lower-and-upper-potentials) turn all exponents nonnegative by scalar row and column gauges, with cost-zero entries along an optimal matching after rescaling.
In the resulting matrix at zero it suffices to retain the terms participating in minimum matchings.
Indeed identify the rows with their matched columns and direct the other zero-cost terms from their columns to their rows.
Every edge internal to a strongly connected component belongs to a directed simple cycle or a matched position, and replacing the matching along a cycle gives an optimal matching containing that term.
This argument includes parallel terms in a matched position.
The remaining edges are strictly block triangular in component order.

To describe the retained matrix, the used \(t\)-edges fix the intermediate site for every input.
The used \(s\)-edges fix the intermediate site for every output, since an output \(l\) is reached from \(x^{-1}(l)\) if that edge is used, and from \(l\) otherwise.
An optimal matching exists, so the two counts coincide at each site.
They can be zero, one or two.
All bijections among the incoming and outgoing ports at each site yield matchings using the same edge sets and hence have the chosen cost.
After permuting coordinates the retained matrix therefore splits into independent square blocks at intermediate sites.
A site with one port on each side gives one invertible corner with group translations.
With two ports the incoming columns are \(k,y^{-1}(k)\), and the outgoing rows are \(k,x(k)\); in each pair the sites are distinct, since two different matching inputs and outputs are required.
In this order its block is
\[
               \operatorname{diag}(I,-sI)
                    \begin{pmatrix}B&A\\D&C\end{pmatrix}
                       \operatorname{diag}(I,tI).
\]
Thus the full endpoint is boundedly invertible.
This also gives a boundedly invertible specialization at nearby nonzero \(z\).
Possible term collisions before collecting the entries cause no issue: a term tied within an optimal matched position is itself in an optimum and has been included in the indicated port block.
The [matching spread bound](Yin_C_A0219_v1.md#statement) applied with the prescribed term costs then gives
\[
                5n\,\dim_H\ker K\ \le\ h(\max\text{ cost}-\min\text{ cost}).
\]

## The finite certificates and the subgroup conclusion

The [five-channel verifier](../computations/programs/Yin_J_A0011/verify_five_channels.py) forms all permutations on five points and their multiplication table.
Under simultaneous conjugation by \(S_5\), all ordered generating pairs of \(A_5\) split into 19 orbits of size 120.
All ordered generating pairs of \(S_5\) with odd first and even second permutation likewise split into 19 orbits of size 120.
The program independently checks orbit sizes and generation by finite closure, and requires exactly one listed certificate per orbit.
Each certificate gives \(c\) and a ten-bit mask indicating which of the exponents \(c,dc\bmod n\), chosen initially in \([0,n-1]\), to reduce by a further \(n\).
For each representative it enumerates the \(4^5\) choices of paths, retains every perfect matching, and computes costs on the distinct pairs of used edge sets.
It verifies uniqueness of those sets at one end.
The largest certified spreads are 23, 29 and 31 in the order of the statement; the [reproduction procedure](../computations/programs/Yin_J_A0011/readme.md#scope-and-reproduction) covers all three families.
Together with interpolation this proves the bounds.

For a half-kernel under scalar injectivity the [corner and marking theorem](Yin_C_A0201_v1.md#statement) supplies the invertible corners and cyclic marking, with invertible assembly by the [four-column reduction](Yin_C_A0184_v1.md#statement).
The abelianization is exactly \(C_n\), and all solvable images are cyclic by the order-25 and order-26 results in the statement.
For the noncyclic abelian quotient of order 25 the [character-lattice test](Yin_C_A0237_v1.md#consequences-for-an-arbitrary-half-rank-marking) already excludes half rank.
Any nonsolvable subgroup of \(S_5\) contains \(A_5\).
Indeed its intersection with \(A_5\) has index at most two.
An intransitive subgroup of \(A_5\) lies in a product of symmetric groups of degrees at most four and is solvable.
A proper transitive subgroup of \(A_5\) has order divisible by five and dividing 60; orders 15, 20 and 30 are impossible by simplicity of \(A_5\) and the coset action of degree at most four.
The remaining orders five and ten give solvable groups.
Thus the only nonsolvable images are \(A_5,S_5\).
A surjection onto \(S_5\) requires a nontrivial sign character.
At order 25 this is impossible and at order 26 its values on the two marks must be odd and even, respectively.
All three bounds at \(h=2\) are strictly less than \(1/2\), excluding the nonsolvable cases.
Finally, a subgroup of index five gives a transitive five-point action, whose image must now be cyclic of order five.
Such an action factors through \(C_n\) and the stabilizer is the inverse image of its index-five subgroup, proving the last assertions.

## Assessment history

### Decision five-point-actions-at-orders-twenty-five-and-twenty-six

| Field | Value |
| --- | --- |
| date | 2026-11-26T15:12 |
| status | proved |
| reason | The verified edge lifts and the endpoint matching argument exclude every noncyclic five-point permutation image under the two critical markings. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The general block bounds and the five-point conclusions. |
| argument | [Integer lifts on individual permutation edges](#integer-lifts-on-individual-permutation-edges) | Actual finite phases and original group factors. |
| argument | [Invertibility when the extremum has unique edge sets](#invertibility-when-the-extremum-has-unique-edge-sets) | The full-rank endpoint when the optimal edge sets agree. |
| argument | [The finite certificates and the subgroup conclusion](#the-finite-certificates-and-the-subgroup-conclusion) | The complete marking orbits and index-five subgroups. |
| review | [Five-point actions at orders twenty-five and twenty-six](../audits/reviews/Yin_R_A0215_v1.md#five-point-actions-at-orders-twenty-five-and-twenty-six) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-five-point-actions-at-orders-twenty-five-and-twenty-six)

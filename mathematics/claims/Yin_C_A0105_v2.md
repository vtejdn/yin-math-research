---
author: Yin
---
# Exact products and bounded unique products in the Gardam presentation

## Statement

Let
\[
 \Gamma=\langle a,b\mid R_1,R_2\rangle,\qquad
 R_1=aba^2b^{-1}a^2b^{-2},\qquad
 R_2=ab^3ab^4a^{-1}b.
\]
Let \(B_r\) be the word-metric ball of radius \(r\) for the symmetric generating set \(\{a,b,a^{-1},b^{-1}\}\).
The [retained verifier J_A0005](../computations/programs/Yin_J_A0005/readme.md), together with the arguments below, gives the following results.

1. A terminating confluent system of 98 two-letter rules on seven generators and their inverses decides equality in \(\Gamma\).
   In particular, product comparisons below are equalities in the presented group, not just in a finite quotient.

2. For radii \(0,\ldots,8\), respectively,
   \[
          |B_r|=1,\ 5,\ 17,\ 53,\ 161,\ 467,\ 1311,\ 3637,\ 9929.
                                                               \tag{1}
   \]

3. Every two nonempty subsets \(P\subseteq B_r\), \(Q\subseteq B_s\) have a uniquely represented product whenever
   \[
                              r+s\le9.                       \tag{2}
   \]
   The maximal direct finite tests are \((r,s)=(1,8),(2,7),(3,6),(4,5)\); the subcase \((4,4)\) was also checked.
   Consequently, for every field \(k\), all nonzero
   \(\alpha\in k[B_r]\), \(\beta\in k[B_s]\) in the range (2) satisfy \(\alpha\beta\ne0\).

4. For the 32-by-28 appendix supports of Mian–Siddique used in [v1](Yin_C_A0105_v1.md#statement), the actual product partition in \(\Gamma\) equals all 336 buckets of J_A0004, cell by cell.
   Thus their product set has exactly 336 elements and the bucket-size distribution in v1 is the exact distribution.
   In particular it has no uniquely represented product.
   The coefficient exclusion for every subrectangle and every field established in v1 remains applicable.

The group presentation and appendix words are from [Mian–Siddique, arXiv v1, pp. 2 and 10](../literature/pdf/MS26b--arxiv-v1.pdf).
The seven-triangle presentation is read from [Gardam's Warwick slides, slide 12](../literature/pdf/Gar21c.pdf#page=12).
Both directions of its identification with the two-generator presentation are established below.
Neither the bounded unique-product tests nor the appendix coefficient exclusion assume torsion-freeness, the lattice description, property (T), a solution of the general zero-divisor conjecture, or the correctness of the source's Lean implementation.

<a id="argument"></a>

## Identifying the seven-triangle presentation

Write uppercase letters for inverses and consider
\[
 T=\langle a,b,c,d,e,f,g\mid
                 acb,\ add,\ afg,\ bbf,\ cef,\ cdg,\ eeg\rangle.
                                                               \tag{3}
\]
These are the seven oriented boundary words on slide 12.
Eliminate five generators using \(acb,bbf,afg,cdg,cef\), in that order:
\[
 c=a^{-1}b^{-1},\qquad
 f=b^{-2},\qquad
 g=b^2a^{-1},\qquad
 d=ba^2b^{-2},\qquad
 e=bab^2.                                                     \tag{4}
\]
For example, \(cdg=1\) gives \(d=c^{-1}g^{-1}=ba^2b^{-2}\), and \(cef=1\) gives \(e=c^{-1}f^{-1}=bab^2\).
No change of generator order is used.

Substitution of (4) into the five relators used for elimination freely reduces each to the empty word.
For the two remaining relators it gives
\[
       add\longmapsto R_1,\qquad
       eeg\longmapsto bR_2b^{-1},                             \tag{5}
\]
after free reduction.
For instance \(add=a(ba^2b^{-2})(ba^2b^{-2})\) freely reduces to \(aba^2b^{-1}a^2b^{-2}\).
Similarly \(eeg\) reduces to \(bab^3ab^4a^{-1}=bR_2b^{-1}\).
Thus substitution defines a homomorphism \(T\to\Gamma\).
Conversely the elimination identities hold in \(T\), so (5) proves that \(a,b\in T\) satisfy \(R_1=R_2=1\).
They define a homomorphism \(\Gamma\to T\).
These maps fix \(a,b\), and (4) shows that their composite also fixes every other generator of \(T\).
They are inverse isomorphisms.
The verifier checks all seven free substitution identities in (5), including the five empty ones.

## A finite complete rewriting system

Let \(\bar x\) denote the inverse of a positive letter \(x\in\{a,\ldots,g\}\).
Use the following rules.

- For each positive letter, cancel \(x\bar x\) and \(\bar x x\).
- For every cyclic permutation \(xyz\) of one of the seven words in (3), use
  \[
                  xy\longrightarrow\bar z,\qquad
                  \bar y\bar x\longrightarrow z.             \tag{6}
  \]
- If \(x\ne y\) are positive letters, there is exactly one positive \(z\) for which cyclic triangles \(xuz\) and \(yvz\) occur in the preceding list.
  Use
  \[
                         \bar x y\longrightarrow u\bar v.    \tag{7}
  \]

The verifier enumerates the cyclic triangles, checks existence and uniqueness of \(z\) in every instance of (7), and checks that no left-hand side is assigned conflicting replacements.
There are 14 cancellation rules, 42 rules from (6), and 42 rules from (7), for a total of 98.
All are valid in \(T\).
For (7), the two triangular relations give \(xu=z^{-1}=yv\), hence \(\bar x y=u\bar v\).

Order words by the lexicographically ordered pair
\[
 \left(\text{length},\
       \#\{(i,j):i<j,\text{ letter }i\text{ is negative and letter }j
                    \text{ is positive}\}\right).           \tag{8}
\]
Cancellations and (6) reduce length.
Rule (7) changes adjacent signs from negative–positive to positive–negative, preserving length and reducing the second entry by one.
Thus every reduction strictly decreases a pair of nonnegative integers in the indicated lexicographic order.
There is no infinite reduction sequence.

All left-hand sides have length two.
Reductions at disjoint positions commute, and two reductions at the same position agree because the replacement is unique.
The only remaining local ambiguity is a three-letter word whose first and last two-letter subwords are both rule left-hand sides.
The verifier enumerates all \(14^3=2744\) three-letter words.
There are 560 such ambiguities, and for each it explicitly reduces the two one-step results to the same word.
Using deterministic reduction to check this is not an assumption of confluence: each reduction is a finite displayed-rule path, so equality of the final strings supplies a joining pair of paths.

For completeness, local joining and termination imply global uniqueness of normal form by induction on (8).
Given two paths to irreducible words, compare their first steps.
If those steps agree, apply the induction hypothesis to the common smaller word.
Otherwise local joining supplies a common descendant of the two smaller first-step words.
Reduce this descendant to an irreducible word.
The induction hypothesis applied at each first-step word identifies both original irreducible results with it.
The case of no first step is immediate.
Thus every word has exactly one irreducible descendant.

These normal forms decide the group word problem, not merely a weaker rewriting congruence.
Indeed the monoid presented by the rule equalities is a group because all inverse cancellations are among the rules.
Each triangle \(xyz\) reduces by (6) to \(\bar z z\), then to the identity.
Conversely every rule has already been derived in the group \(T\).
The monoid and \(T\) are therefore isomorphic by maps fixing the generators.
Confluence identifies their elements exactly with the irreducible words.
Together with (4)–(5), this supplies the asserted exact word problem in \(\Gamma\).

## Exact balls and the appendix partition

J_A0005 enumerates the balls by breadth-first multiplication by \(a,b,A,B\), using the proved normal form as the vertex key.
Every vertex retains a shortest word in these four letters.
Induction on radius proves coverage: any word of length at most \(r+1\) is a word of length at most \(r\) followed by one generator, unless it was already in the previous ball.
Normal-form uniqueness proves that distinct keys represent distinct elements.
This proves that the printed counts are the actual sizes in (1).

For the appendix calculation, the verifier reads the two word lists from the explicit retained [J_A0004 input](../computations/programs/Yin_J_A0004/verify.py).
It forms exact product buckets using normal forms and compares the resulting sets of cell sets with J_A0004's finite-quotient chain buckets.
The two partitions agree, rather than merely having the same bucket counts.
The actual distribution is therefore
\[
\begin{array}{c|rrrrrrrrr}
\text{fiber size}&2&3&4&5&6&7&10&11&12\\ \hline
\text{number}&230&53&26&10&8&6&1&1&1.
\end{array}                                                   \tag{9}
\]
The exact normal forms also check the 32 distinct rows and 28 distinct columns.
This establishes the exactness that v1's necessary-equation proof did not require.
The three support rectangles and the three-pair coefficient contradictions of v1 are reused unchanged.

## Exhausting the bounded rectangles

Fix two of the finite balls and put their elements in independent deterministic total orders.
The sorting key in the program is a finite integer tuple followed by the representative word; it is only a search heuristic.
No compatibility between this order and group multiplication is asserted or used.

For every cell \((i,j)\), its partners are all other cells with the same exact product.
A nonempty row set \(I\) and column set \(J\) have no uniquely represented product exactly when every cell of \(I\times J\) has a partner in \(I\times J\).

Any such rectangle has a unique maximal row and a unique maximal column.
The outer enumeration fixes these maxima, requires both labels, and forbids larger indices.
It skips the pair of maxima only if their cell has no partner within those bounds.
This is necessary because that cell belongs to every rectangle with the chosen maxima.

Within one pair of maxima, a state consists of required row and column sets.
The following tests preserve every possible completion.

1. A prospective row must have a globally nonsingleton product cell with every required column.
   A prospective column must have one with every required row.
   The program intersects the corresponding compatibility masks with the bounds from the maxima.
   If this excludes an already required label, no completion is possible.

2. For a required cell already having a required partner, no additional constraint is needed.
   Otherwise inspect its partners whose two labels remain possible.
   With no such partner the state is impossible.
   With exactly one, both of that partner's labels are forced.

3. If some labels have been forced, continue at their union with the current state.
   Otherwise select an uncovered required cell and branch on all its still-possible partners, requiring both endpoints in each branch.
   Every completion contains at least one of these partners, so the branches cover every completion.
   They need not be disjoint.

4. If all required cells already have required partners, the required row and column sets themselves form a non-unique-product rectangle.
   This would be returned as a witness, without any extra support-size condition.

Each successor adds at least one label.
Thus the search is finite.
Its memoization records both required masks and is reset for each pair of maxima, whose allowed bounds remain fixed.
Revisiting a state within that same finite problem cannot discover a different completion problem.
This proves that exhaustion without a witness excludes every nonempty rectangle in the specified two balls.

The maintained verifier completed the following five tests.
The counts describe processed states after memoization, not a formula for the number of all possible rectangles.

| Radius pair | Pairs of maxima searched | States processed | Non-unique-product rectangle |
| --- | ---: | ---: | --- |
| \((1,8)\) | 3,073 | 10,633 | None |
| \((2,7)\) | 10,011 | 107,980 | None |
| \((3,6)\) | 17,662 | 598,738 | None |
| \((4,4)\) | 6,894 | 188,790 | None |
| \((4,5)\) | 23,709 | 2,785,704 | None |

The tests use neither torsion filters nor lower bounds on the sizes of a possible rectangle.
All comparisons are finite integer, set, string and bit-mask operations; no floating-point tolerance enters.

## Passing from the maximal tests to the stated range

The property is inherited by subsets of either ball.
It is also symmetric in the two radii: inversion sends a non-unique-product rectangle \(P\times Q\) to \(Q^{-1}\times P^{-1}\), and each \(B_r\) is closed under inversion.
Every positive pair with \(r+s\le9\) is dominated, after this symmetry, by one of \((1,8),(2,7),(3,6),(4,5)\).
If one radius is zero, that side has at most one element and every product is uniquely represented.
This proves (2).

For nonzero group-ring factors in these balls, use their actual nonzero supports \(P,Q\).
A uniquely represented product receives the single coefficient \(\alpha_x\beta_y\ne0\) over any field.
Thus the product cannot vanish.
This is a bounded support result in the specified presented group.
It supplies neither unique products for all finite supports nor a proof of the complex zero-divisor conjecture for this group or for arbitrary torsion-free groups.

## Assessment history

### Decision exact-balls

| Field | Value |
| --- | --- |
| date | 2026-11-21T06:20 |
| status | proved |
| reason | The independent review derives all joins and product tables and exhausts the rectangles with a second implementation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact word problem and appendix fibers, and unique products for all sub-supports of balls with radius sum at most nine. |
| argument | [Proof](#argument) | Presentation equivalence, confluence, exact multiplication, exhaustive rectangle search and passage to all smaller radii. |
| review | [Whole finding](../audits/reviews/Yin_R_A0142_v2.md#whole-finding) | Independent whole-claim inspection at the scope specified in the finding. |
| dependency | [Appendix coefficient exclusion](Yin_C_A0105_v1.md#decision-appendix-supports) | The all-fields sub-support conclusion on the exact appendix table. |

## Current assessment

[Selected decision](#decision-exact-balls)

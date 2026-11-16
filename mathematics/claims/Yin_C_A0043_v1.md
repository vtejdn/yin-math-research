---
author: Yin
---
# Which sparse cyclic images the projective-plane vertex types can occupy

## Statement

Use the two graphs with fixed letter types on \(n\) vertices each from [Ope26f, §2.1](../literature/pdf/Ope26f.pdf#page=4).
Assume each side is connected, so that the factor from its root uses every vertex.
Suppose a homomorphism of the cone group onto \(C_7=\mathbb Z/7\) is given.
Color the vertices by the quotient labels of their root paths, reversing the sign on the side whose factor uses inverse labels.
The **occurrence set** on a side is the set of colors of its vertices.
The **collected set** of colors is the image of the actual group-algebra support, obtained by first collecting equal group elements over \(\mathbb F_2\).

1. On either side the occurrence set cannot be a translate or a unit dilation of \(\{0,1,3\}\) or its four-point complement.
   The projected occurrence equations always admit an exact lift through the all-ones point, even over a number field with local degree one at two.
2. On the actual collected supports every such projection admits a lift modulo four.
   An obstruction in characteristic zero exists precisely if both collected sets consist of just four occupied classes, all odd, with the opposite nontrivial Fourier orbits in the [cyclic classification](Yin_C_A0042_v1.md#statement).
   In that case it already fails modulo eight measured in powers of two in every finite extension.
   On each side at least one occupied occurrence class outside the four has been completely erased by collecting equal group elements.
3. Call a vertex repeated if its group label is shared by another vertex on its side.
   If the images of the signed letters contain at least two distinct nonzero pairs \(\{\pm d\},\{\pm e\}\) and either side has fewer than \(n/(3\cdot16513)\) repeated vertices, the projected true-support equations admit the exact lift in item 1.
4. If all nonzero letter increments belong to a single pair \(\{\pm d\}\) and both occurrence sets omit at least one residue, one of the two parity indicators is zero.
   The projected equations then have a lift by integer signs on the actual supports.

These are tests on an actual quotient of a connected matching realization.
They require neither an independence assumption on the matchings nor a word-probability estimate.
They give no character on a graph whose defining loops have not been checked.

## Neighbor constraints

On each side any two distinct signed letters occur together at a vertex.
Two ordinary letters determine a projective line, an ordinary and an extra occur together in a positive proportion of vertices of the appropriate lines, and each pair of extras occurs together by the prescribed types.
More precisely the proportion of vertices carrying each chosen pair is at least \(1/v\), where \(v=16513\).
For two ordinary letters it is \(1/v\).
For an ordinary and an extra it is \(p^2\), where \(p=129/v\) and \(129^2>v\).
For two extras it is \(p/2\) on the first side and \(p\) on the second.

Let \(S\) be the occurrence set on the chosen side and put \(I_d(S)=\{x\in S:x+d\in S\}\).
Write \(d_t\) for the color change when reading a signed letter \(t\), with the sign appropriate to the chosen factor.
A vertex carrying both \(t,u\) must have its color in \(I_{d_t}(S)\cap I_{d_u}(S)\); the matching supplies both neighbors.
In particular, the letters \(t,\bar t\) at a common vertex require \(S\) to contain a three-term arithmetic progression with step \(d_t\ne0\).
For \(P=\{0,1,3\}\) the six ordered differences of distinct elements are all different.
Such a set contains no three-term arithmetic progression, since that progression repeats a difference.
This also holds after translation or dilation by a unit.
Surjectivity ensures some nonzero step.

Let \(K\) be the complement of a translate or unit dilation of \(P\).
For each \(d\ne0\) one has \(|I_d(K)|=7-3-3+1=2\).
These six two-element subsets are all distinct.
Indeed if \(I_d(K)=I_e(K)=\{x,y\}\) for different nonzero \(d,e\), the ordered pairs \((x,y),(x+d,y+d),(x+e,y+e)\) would give three representations of \(y-x\) in \(K\).
There are only two.
At most three distinct two-element subsets of a four-point set can be pairwise intersecting: the six subsets split into three complementary pairs.
If the occurrence set were \(K\), the neighbor constraint would therefore allow at most three nonzero steps.
Steps occur in opposite pairs, so the only possibility for a nontrivial quotient is a single pair \(\pm d\).
The image of a connected side must then be connected by steps \(\pm d\), since zero steps do not change a vertex color.
On \(K\) there are only two undirected edges of step \(\pm d\), counted by \(I_d(K)\), and they cannot connect four vertices.
This proves the exclusion asserted in item 1.

## Passing from vertices to the two actual supports

The total on each side is \(n\), an even integer.
The odd classes for the vertex counts have the same parity indicator as the counts of the distinct surviving group elements in each class.
The total number of odd classes is therefore even.
The product of the two parity indicators in \(\mathbb F_2[C_7]\) is zero by the source's zero product.
By [the cyclic classification](Yin_C_A0042_v1.md#separating-the-cubic-factors), either one parity indicator is zero or each has four odd classes, the complements of triples of the form considered above.
In the first case one can give opposite signs to pairs in every class on the side with zero indicator, giving an integral lift of the projected equations.
In the other case each side at the occurrence level occupies at least five classes by the neighbor argument, so the exact-lift row of the classification applies.

After collection, an even number of removed vertices can eliminate an entire class.
The same classification now gives unconditional feasibility modulo four and the precise exceptional pair of masks in item 2.
In this case the obstruction is detected by the complete quotient product equations, including the augmentation equation, and it persists after arbitrary ramification.
The occurrence set on each side properly contains the exceptional four classes, giving the necessary erasure assertion.
This application uses the actual occupied classes after collection, including those of even positive count.

For the quantitative assertion, suppose all four odd classes on one side form \(K\) and no other collected class is occupied.
Every occurrence outside \(K\) is then repeated; a singleton group label there would survive.
With two distinct nonzero step pairs, some two of the at least four distinct two-sets \(I_d(K)\) are disjoint.
Choose signed letters realizing these two steps.
At least \(n/v\) vertices on this side carry them both.
For each such vertex, either it or at least one of its two chosen neighbors has color outside \(K\).
A vertex outside \(K\) is charged at most three times, once as the original vertex and at most once for each signed incoming step, since each label matching is a bijection on its stubs.
Thus at least \(n/(3v)\) vertices are repeated.
The contrapositive and the exact-lift criterion give item 3.
In particular an apparent mod-eight obstruction on a nearly injectively labelled side requires all nonzero increments to be in a single opposite pair, at the specified repetition threshold.

## Unwrapping when both occurrence sets omit a color

Use the forward path colors on both sides before inverting the second factor, and multiply the two colorings by \(d^{-1}\) in \(C_7\).
Every edge has color change \(0,1\) or \(-1\).
On each side cut the seven-cycle at a color absent from that side.
The other six colors have consecutive integer representatives with the property that every step actually taken has its indicated integer change \(0,1\) or \(-1\).
Indeed no edge between two of these six classes can cross the missing class.
Subtract the integer representative of the root on each side to obtain root-relative heights \(H_A,H_B\).
The same letter makes the same integer change wherever it is read on either side; the cuts need not be the same.
Along a simultaneous step the integer \(H_A(x)-H_B(y)\) is constant.
The odd-degree argument of [Ope26f, §1](../literature/pdf/Ope26f.pdf#page=2) makes each simultaneous component have even cardinality.
Consequently
\[
  \left(\sum_x T^{H_A(x)}\right)\left(\sum_y T^{-H_B(y)}\right)=0
            \quad\text{in }\mathbb F_2[T,T^{-1}].
\]
This is an integral domain, so one factor vanishes.
Reducing its exponents modulo seven shows that one occurrence parity indicator is zero, and collection preserves the same parity indicator.
Within each occupied class on the corresponding true support, choose opposite integer signs in pairs.
This proves item 4 without requiring the integer heights to descend through all relations of the cone group.
In particular, in the remaining one-step case of item 3, a ramified obstruction would require at least one side to occupy all seven colors before collection and only its four odd colors afterwards.

## What a supplied matching instance would determine

Choose a spanning forest of both labelled graphs, marking the prescribed roots in their components.
Use one unknown in \(\mathbb F_7\) per inverse pair for the signed letter values.
For each nonforest edge form the signed letter counts of its fundamental closed walk and take its dot product with the unknown vector.
The nullspace of all these linear equations is exactly the homomorphism space from the cone group to \(C_7\), since fundamental walks generate every closed-walk relation after abelianization.
A nonzero vector is surjective.
It gives the seven occurrence counts by summing the letter values along the forest paths from the roots.
For the actual support counts one also needs sufficient information about label coincidences within each color.
A partition by equality of group labels or a certificate of injectivity suffices.
If \(a_i,b_i\) are the resulting true counts on classes indexed by the factor labels, the entire coarse fiber over \(k\) is the disjoint union of the seven rectangles indexed by \((i,k-i)\).
Its size is \(\sum_i a_i b_{k-i}\), regardless of further equalities before projection.

The source [conclusion, §6](../literature/pdf/Ope26f.pdf#page=24) gives existence of suitable matchings and explicitly leaves their concrete choice unspecified.
These tests consequently do not give a numerical seven-bin true-support histogram for a distinguished published instance.
The [original matching model](Yin_C_A0041_v1.md#statement) and [the independently matched color classes](../ledger/Yin_L_A0047_v1.md) have different conclusions about existence of a nontrivial quotient.

## Assessment history

### Decision sparse-occupancy-constraints

| Field | Value |
| --- | --- |
| date | 2026-11-17T02:27 |
| status | proved |
| reason | Independent mathematical review covers the full argument and its limitations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All four neighbor, collection and integer-height tests, with the matching-instance data required for exact counts. |
| argument | [Proof](#neighbor-constraints) | Complete argument under the stated hypotheses. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0074_v1.md#whole-argument-finding) | Independent review of these conclusions and their inputs. |

## Current assessment

[Selected decision](#decision-sparse-occupancy-constraints)

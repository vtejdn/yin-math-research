---
author: Yin
---

# Matching costs at both ends of a regular operator pencil

## Statement

Let \(Q(z)\) be a \(q\)-by-\(q\) block Laurent polynomial with bounded \(h\)-by-\(h\) coefficients over a finite von Neumann algebra with normalized trace.
Use the unnormalized matrix trace.
For each nonzero block \(Q_{ij}\), let \(l_{ij},u_{ij}\) be the least and greatest exponents of its nonzero coefficients.
Suppose its block support has a perfect matching and \(Q(z_*)\) is injective at some \(z_*\in\mathbb C^\times\).
Define the extremes over perfect matchings of this support by
\[
    L=\min_{\sigma}\sum_j l_{\sigma(j),j},\qquad
    U=\max_{\sigma}\sum_j u_{\sigma(j),j}.
\]
For any finite set \(Z\subset\mathbb C^\times\) of distinct points,
\[
                 \sum_{z\in Z}\dim\ker Q(z)\ \le\ h(U-L).
\]
The same conclusion holds when the stated lower and upper exponents only bound the actual support on a specified graph with a perfect matching.
If at \(k\) points the evaluations agree up to invertible gauges with unitary representation twists of a group matrix of nullity \(\delta\), all of auxiliary dimension \(q\), then \(qk\delta\le h(U-L)\).
The lower and upper matching problems use independent row and column weights.

For the order-25 marking \((1,7)\) let \(H=\langle s,t\rangle\) have abelianization \(C_{25}\), set \(M=H'/H''\) and write \(S=\operatorname{Ad}_s\) on \(M\).
If \(M/\Phi_{25}(S)M\) has a simple quotient of characteristic \(p\equiv1\bmod25\) with \(p\le100000\), the regular nullity of \(B+At-s(D+Ct)\) is strictly below \(1/2\) whenever the four complex two-by-two corners and the assembled block \(\left(\begin{smallmatrix}B&A\\D&C\end{smallmatrix}\right)\) are invertible.
The test covers all 486 such primes and all 9720 marked primitive roots.
It uses no torsion or scalar-injectivity assumption for this quantitative implication.
At a half-rank input in the torsion-free scalar-injective problem the [four corners](Yin_C_A0201_v1.md#statement) and [assembled block](Yin_C_A0184_v1.md#the-four-group-elements-and-the-trace-bound) meet those conditions.

## Lower and upper potentials

Choose a matching attaining the minimum \(L\), and temporarily order the rows by their matched columns, so the diagonal is matched.
Subtract \(l_{jj}\) from column \(j\)'s costs.
An edge from \(j\) to \(i\) now has cost \(l_{ij}-l_{jj}\).
A negative simple directed cycle would decrease the matching cost by replacing precisely its matched edges.
Attach a new source with a zero-cost edge to each vertex and let \(d_i\) be shortest-path distances.
They are finite integers and \(d_i-d_j\le l_{ij}-l_{jj}\).
Consequently row prices \(a_i=d_i\) and column prices \(b_j=l_{jj}-d_j\) satisfy \(a_i+b_j\le l_{ij}\), with equality along the matching and total price \(L\).
Restore the original row order and form \(F(z)_{ij}=z^{-a_i-b_j}Q(z)_{ij}\), which is polynomial.
The upper costs for \(F\) are \(u_{ij}-a_i-b_j\).
Their maximum matching sum is \(U-L\), since every matching uses each row and each column exactly once.
Applying the same shortest-path construction to the negatives of these upper costs gives integer prices \(\alpha_i,\beta_j\) with
\[
            \deg F_{ij}\le\alpha_i+\beta_j,\qquad
            \sum_i\alpha_i+\sum_j\beta_j=U-L .
\]
For a graph of prescribed bounds both constructions use those bounds as costs.
The polynomial degree inequalities still hold if some actual coefficient at a prescribed exponent vanishes.

## Interpolation with different output degrees

Put \(k=|Z|\), taking \(k>0\).
Choose an integer \(n\) large enough that \(n-\beta_j\ge0\) and \(n+\alpha_i\ge k-1\) for all indices.
Multiply by \(F\) on polynomial columns whose \(j\)-th block has degree at most \(n-\beta_j\).
All output blocks then have degrees at most \(n+\alpha_i\).
Multiplication is injective on this finite Hilbert module of coefficients.
Indeed a nonzero input has a first nonzero Taylor coefficient at \(z_*\), and \(F(z_*)\) is injective.
Thus the closure of the image has the full input dimension.

Output evaluation at \(Z\) is onto the \(k\) copies of the output coordinate space, since each row allows degree at least \(k-1\).
Scalar Lagrange interpolation gives a bounded right inverse.
For inputs multiplied by \(F\), the evaluation lies in the direct sum of the closed ranges of \(F(z)\) at those points.
Its inverse image under evaluation is a closed module of codimension \(\sum_{z\in Z}\dim\ker F(z)\), by surjectivity and rank-nullity for each square evaluation matrix.
It contains the closure of the multiplication image.
Subtracting input dimension from output dimension therefore gives
\[
     \sum_{z\in Z}\dim\ker F(z)\le
       h\sum_i(n+\alpha_i+1)-h\sum_j(n-\beta_j+1)=h(U-L).
\]
The gauges at the nonzero points are invertible.
[Regular absorption](Yin_C_A0204_v1.md#the-bound-using-individual-column-widths) gives the stated factor \(q\) for true unitary twists.
This proof uses no determinant of the operator coefficients.

## Split primes and a strict improvement over column widths

A simple quotient at a split prime supplies a primitive root \(r\in\mathbb F_p\).
The [coupled orbit construction](Yin_C_A0217_v1.md#characters-from-a-single-coupled-orbit) realizes \(s\mapsto P,\ t\mapsto P^7\operatorname{diag}(z^{e_j})\) at each \(z^p=1\), with \(P\) the cyclic shift on 25 coordinates.
Here \(e_j\) is the centered representative of \(c r^j\) for a chosen nonzero multiplier \(c\).
The two entries from column \(j\) at row offsets zero and one have exponent zero, and the entries at offsets seven and eight have exponent \(e_j\).
The [verifier](../computations/programs/Yin_J_A0008/verify_matching_spread.py) obtains extremal matchings for these costs and their negatives.
For each optimum it checks an actual perfect matching tight for the prices and the inequalities on every edge, which proves optimality directly.

The lower prices give the initial graph after rescaling rows and columns.
Upper prices do the same for the reversed pencil \(Q(1/z)\).
For at least one of the two initial graphs the verifier checks that, on identifying each matched row with its column, each strongly connected component is a singleton or a pair.
For a pair both columns meet both rows, one with row offsets zero and one and the other with offsets seven and eight.
The diagonal block after ordering components is therefore a translated invertible corner or, up to row and column order,
\[
  \operatorname{diag}(I,-sI)
  \begin{pmatrix}A&B\\ C&D\end{pmatrix}
  \operatorname{diag}(tI,I).
\]
The middle block is a column permutation of the assumed invertible assembled block.
The resulting block triangular matrix is invertible at zero, so the gauged polynomial is invertible near zero.
This gives an injective evaluation of the original pencil at some nonzero point, also when the upper endpoint was used.

The program tests primality over the full stated interval and constructs all twenty primitive roots for each split prime.
For each marking one of the multipliers \(1,2,3\) gives both an invertible endpoint and \(4(U-L)<25p\).
The first part therefore gives \(\delta\le2(U-L)/(25p)<1/2\).
In 2866 of the 9720 first successful choices, the unscaled sum of individual block-column widths already satisfies \(4\sum_j|e_j|\ge25p\).
For a separate illustrative choice \(p=151,\ r=9,\ c=4\), that sum is 997, while \(L=-335\) and \(U=486\).
The two-sided matching estimate gives \(1642/3775<1/2\) at this marking.
The strict improvement here concerns the original column widths for this same orbit and multiplier.

## Assessment history

### Decision two-matching-bounds-for-interpolation

| Field | Value |
| --- | --- |
| date | 2026-11-26T10:36 |
| status | proved |
| reason | Independent proof review and an independent matching computation verified the general inequality and all split marked roots in the stated interval. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite-trace operator pencils and the split-prime application. |
| argument | [Lower and upper potentials](#lower-and-upper-potentials) | Independent dual prices and prescribed exponent bounds. |
| argument | [Interpolation with different output degrees](#interpolation-with-different-output-degrees) | Choice of degree spaces, bounded right inverse and codimension of the range constraint. |
| argument | [Split primes and a strict improvement over column widths](#split-primes-and-a-strict-improvement-over-column-widths) | Endpoint factorizations and the exact count through one hundred thousand. |
| review | [Two matching bounds for interpolation](../audits/reviews/Yin_R_A0193_v1.md#two-matching-bounds-for-interpolation) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-two-matching-bounds-for-interpolation)

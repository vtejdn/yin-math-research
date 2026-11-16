---
author: Yin
---
# Laurent endpoint constraints on products supported in four cyclic cosets

## The exterior cyclic covers

Let \(G\) be torsion-free and let \(H=\langle h\rangle\) and \(K=\langle k\rangle\) be infinite cyclic subgroups.
Suppose that \(a,b\in\mathbb C[G]\) are nonzero and have decompositions
\[
       a=\sum_{i=1}^r f_i(h)x_i,\qquad
       b=\sum_{j=1}^s y_j g_j(k),\qquad 1\le r,s\le4 .
\]
The \(Hx_i\) are distinct right cosets, the \(y_jK\) are distinct left cosets, and all displayed Laurent polynomials are nonzero.
Call \((i,j)\) a cell in \(D:=Hx_i y_jK\).
Its contribution is the entire \(f_i(h)x_i y_j g_j(k)\), so the number of cells counts pairs of cosets regardless of the number of terms in these polynomials.
The [joint rank estimate](Yin_L_A0036_v1.md#the-overlap-inequality) allows certain complementary ranks at four cosets per factor.
The argument here uses the coefficient equations within each actual double coset.

The finite-set input is Theorem 1.4 of Pace P. Nielsen and Lindsay Soelberg, *Small sets without unique products in torsion-free groups*.
In particular two nonempty sets of sizes at most four in \(G\) have a uniquely represented product, since their cardinalities sum to less than sixteen.
This applies to arbitrarily chosen endpoint sets of representatives, whose sizes can be much smaller than the supports of \(a,b\).
The theorem statement and its use of an exhaustive group-relation computation were checked in the [authors' manuscript, Theorem 1.4, pp. 2–3 and §2.2, p. 5](https://mathdept.byu.edu/~pace/KaplanskyConjecture_web.pdf#page=2).
The computation is used as a published input at that scope.

## The full coefficient equations

For each occupied \(D\) choose \(d\in D\).
For its cells choose integers \(u_{ij},v_{ij}\) such that \(x_i y_j=h^{u_{ij}}d k^{v_{ij}}\).
The stabilizer of \(d\) for the left and right translations is
\[
             R_D:=\{(m,n)\in\mathbb Z^2:h^m d k^n=d\}.
\]
Two exponent pairs describe the same element of \(D\) exactly when their difference belongs to \(R_D\).
Each coordinate projection of \(R_D\) is injective because \(h,k\) have infinite order.
Hence \(R_D=0\), or \(R_D=\langle(m,-n)\rangle\) with \(m>0\) and \(n\ne0\), using a generator of the actual relation subgroup.
The vector space \(\mathbb C[D]\) is identified, by its basis, with the underlying linear space of \(\mathbb C[\mathbb Z^2/R_D]\).
In these coordinates \(ab=0\) is equivalent to the system
\[
    \sum_{(i,j)\in D} X^{u_{ij}}Y^{v_{ij}} f_i(X) g_j(Y)=0
      \quad\text{in }\mathbb C[\mathbb Z^2/R_D],\qquad\text{for every }D.    \tag{1}
\]
Here \((i,j)\in D\) abbreviates \(x_i y_j\in D\).
When \(R_D\ne0\) the coefficient ring in (1) is the Laurent ring modulo \(X^m-Y^n\).
If \(\gcd(m,|n|)>1\), the coordinate group has finite torsion, and (1) still tests coefficients at its distinct group elements individually.

## Extreme terms of a cell

Let \(p_i,P_i\) be the smallest and largest exponents of \(f_i\), and \(q_j,Q_j\) those of \(g_j\).
Their widths are \(U_i:=P_i-p_i\) and \(V_j:=Q_j-q_j\).
On each exponent quotient choose a height \((u,v)\mapsto \alpha_Du+\gamma_Dv\).
For \(R_D=0\) take \((\alpha_D,\gamma_D)=(1,1)\).
For \(R_D=\langle(m,-n)\rangle\) take \((\alpha_D,\gamma_D)=(|n|,\operatorname{sgn}(n)m)\), so the height vanishes on \(R_D\).
Both coefficients are nonzero and \(\alpha_D>0\).
The smallest and largest heights in each cell are attained at unique exponent pairs before taking the quotient.
They therefore have nonzero coefficients in (1), even if different interior pairs coincide there.
Their height difference is
\[
                         \alpha_D U_i+|\gamma_D|V_j .                     \tag{2}
\]
The minimum uses \(p_i\) and the maximum uses \(P_i\).
At the column endpoint the minimum uses \(q_j\) for \(\gamma_D>0\) and \(Q_j\) for \(\gamma_D<0\), with the opposite choice for the maximum.

It follows that a single-cell double coset prevents \(ab=0\).
For a two-cell double coset satisfying (1), the two minima agree as actual group elements, and so do the two maxima.
Indeed the global least height needs a second term at the same group element, and only the other cell can provide it, necessarily at its own minimum.
The argument at greatest height is the same.
In particular the two values of (2) agree.

## The rectangle of maximum widths

Let \(I:=\{i:U_i=\max_l U_l\}\) and \(J:=\{j:V_j=\max_t V_t\}\).
If \(ab=0\), at least one of the cells in \(I\times J\) belongs to a double coset with at least three cells.
In particular a product with only single- or double-cell double cosets is nonzero for arbitrary nonzero Laurent coefficients.

To prove this, assume \(ab=0\) and that each \(D\) meeting \(I\times J\) has at most two cells.
Every such \(D\) must have two.
If \((i,j)\in I\times J\) has mate \((i',j')\) in \(D\), equality of (2) gives
\[
  \alpha_D(U_i-U_{i'})+|\gamma_D|(V_j-V_{j'})=0.
\]
Both differences are nonnegative and both multipliers are positive.
Thus \(i'\in I,\,j'\in J\).
The entire rectangle \(I\times J\) is paired inside itself.

Choose once for each selected row the group element \(h^{p_i}x_i\), and once for each selected column the element \(y_jk^{q_j}\).
For \(\gamma_D>0\), the products of these representatives in a pair agree by equality of the minimum endpoints.
For \(\gamma_D<0\), that equality reads
\[
       h^{p_i}x_i y_jk^{Q_j}=h^{p_{i'}}x_{i'}y_{j'} k^{Q_{j'}}.
\]
Right multiply by \(k^{-\max V_j}\), using the common column width on \(J\), to obtain equality for the selected representatives in this pair as well.
Consequently every product of the two selected endpoint sets has a second representation.
Their row elements are distinct by the right cosets \(Hx_i\), and their column elements are distinct by the left cosets \(y_jK\).
Nielsen–Soelberg's theorem contradicts this conclusion.

### Congruences of paired centers

Write \(c_i=(p_i+P_i)/2\) and \(e_j=(q_j+Q_j)/2\).
For any paired double coset in a zero product, adding the two actual endpoint congruences gives
\[
    2\big((u_{ij}+c_i,v_{ij}+e_j)-(u_{i'j'}+c_{i'},v_{i'j'}+e_{j'})\big)\in R_D .
\]
If the centers involved are integral and \(\mathbb Z^2/R_D\) has no element of order two, the factor two can be canceled and the two center products are equal in \(G\).
The second condition holds when \(R_D=0\) or \(\gcd(m,|n|)\) is odd.
For general widths the centers can be half-integral, and for an even common divisor the doubled identity alone leaves an element of order two undetected.
The endpoint argument on \(I\times J\) applies in both circumstances.

## Four cells with equal widths

Assume now that every row has the same width \(U\) and every column has the same width \(V\).
If \(ab=0\), some occupied double coset contains at least five cells.

Suppose instead that all occupied double cosets contain at most four cells and satisfy (1).
Within a fixed \(D\), the height intervals of the cells all have the same length \(\alpha_DU+|\gamma_D|V\).
Consider those with smallest lower endpoint and those with greatest upper endpoint.
If all the intervals coincide, every cell is in both classes.
Otherwise the two classes are disjoint and both have at least two members, because each global extremal term in (1) needs a second contribution to the same group element.
With at most four cells these classes exhaust \(D\).
Hence each cell has a minimum or maximum endpoint whose group element occurs as the corresponding endpoint in another cell.
For each such equal pair, multiply both group elements on the left by \(h^{-U}\) when the high row exponents were used, and on the right by \(k^{-V}\) when the high column exponents were used.
This gives two equal products of low row and low column endpoints.
Therefore every product from the full sets \(\{h^{p_i}x_i\}\), \(\{y_jk^{q_j}\}\) repeats, again contradicting the finite-set theorem.

For unequal widths the longest interval in a double coset with at least three cells can meet two shorter ones at opposite ends, so the two endpoint equalities can involve different cells.
Even at equal widths, a fifth interval may lie strictly between the two extremal classes.
Those possibilities leave further equations in (1), including the coefficients away from the exposed heights.
Deciding the remaining patterns for four cosets per factor still requires information about these coefficients or the group relations.

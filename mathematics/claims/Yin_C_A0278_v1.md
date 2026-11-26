---
author: Yin
---

# Both fourth-root actions disappear at cyclic order twenty-four

## Statement

Let \(H=\langle s,t\rangle\) be torsion-free with regular scalar group-ring injectivity and an abelian quotient of order 24.
Suppose \(K=B+At-s(D+Ct)\) with complex two-by-two coefficients has regular rank \(3/2\), using the unnormalized matrix trace.
Then \(H_{\rm ab}=C_{24}\) and \(H'=H''\).
In particular every solvable quotient of \(H\) is cyclic of order dividing 24.
The proof excludes each of the two actions on \(C_5\) and each of the two actions on \(C_{13}\) in the [five residual marked metabelian quotients](Yin_C_A0265_v1.md#statement).
A group with perfect commutator subgroup remains possible under this result.

## Four channels through the marked finite quotient

Use the normalized degrees \(3,4\) on \(s,t\).
In each remaining nonabelian metabelian candidate the additive group \(C_p\), with \(p=5\) or 13, has an order-four scalar action \(\alpha\) of a cyclic complement generator \(\gamma\).
The marked images are \(s=\gamma^3,\ t=v\gamma^4\), with \(v=1\in\mathbb F_p\).
Write \(r=\alpha^{-1}\), so \(r=\pm2\) at \(p=5\) and \(r=\pm5\) at \(p=13\).
On channels \(j\bmod4\), the action of \(\gamma\) can be the forward shift \(P\) and that of an additive element \(x\) the diagonal with entries \(\xi^{m r^j x}\), for any \(\xi\in\mu_p\) and integer \(m\).
Conjugation by \(P\) implements \(\alpha\).
We can also multiply \(P\) by any scalar in \(\mu_{24}\), giving the marked actions of \(s\) as a scalar times \(P^3\) and of \(t\) as a scalar times this diagonal at \(x=1\).
At every allowed phase the [regular absorption identity](Yin_C_A0194_v1.md#normal-form-for-a-pair-of-unitary-matrices) makes the nullity of the resulting eight-square matrix exactly \(4\dim_H\ker K=2\).
All translated group factors \(s,t\) remain in that matrix.

Write \(M(y)=(Ay+B)(Cy+D)^{-1}\).
The [coefficient reduction](Yin_C_A0184_v1.md#statement) gives invertibility of the assembled block matrix and of both rational pencils.
Moreover \(\det(Ay+B)\) and \(\det(Cy+D)\) both have circle zeros by the [six-fiber obstruction](Yin_C_A0244_v1.md#statement).
In particular neither polynomial is a Laurent monomial.
Each of the pairs \((A,B)\) and \((C,D)\) consists of nonzero matrices, and at least one member of each pair is invertible: if both are singular the determinant is a multiple of \(y\).
The [transposed pencil condition](Yin_C_A0249_v1.md#the-cubic-translation-of-two-or-four-character-weights) also gives \(\det(B-yD)\ne0\).
After replacing \(t\) by \(t^{-1}\) in the equal-rank rectangle \(Kt^{-1}\), it likewise gives \(\det(A-yC)\ne0\).
The inversion exchanges \((A,B,C,D)\) with \((B,A,D,C)\); in a twisted rectangle it negates the \(t\) exponents while preserving the \(s\) shift and the rank.

## A mixed endpoint with three sites of one kind

Put \(N=3p\) and \(m=1\) at \(p=5\), \(m=4\) at \(p=13\).
For each \(z\in\mu_N\) use \(\xi=z^3\) and multiply the complement shift by \(z^p\).
Its third power is \(P^3\) and the \(t\) exponents are \(n_j\equiv p+3mr^j\bmod N\).
For \(r=2,5\), respectively, choose
\[
 \begin{array}{c|c|c}
 p&(n_0,n_1,n_2,n_3)&\sum_j|n_j|\\ \hline
 5&(-7,-4,2,-1)&14\\
 13&(-14,-5,1,-8)&28 .
 \end{array}
\]
The other root reverses the cyclic ordering.
In either case the sum is strictly less than \(N\), and exactly one channel has a sign different from the other three.

Use these exponents to define a Laurent matrix on all parameters.
After multiplying each of the two columns at site \(j\) by \(z^{-\min(n_j,0)}\), their degrees are at most \(|n_j|\).
If either the constant endpoint or the endpoint of the reversed polynomial obtained by negating all exponents is injective, the [column-degree interpolation inequality](Yin_C_A0204_v1.md#the-bound-using-individual-column-widths) gives \(2N\le2\sum_j|n_j|\), a contradiction.
Indeed multiplication of polynomial columns is injective by their first nonzero coefficient at this endpoint, which suffices even for an endpoint without bounded inverse.

At the constant endpoint a positive-exponent site has the two blocks \(B,-sD\), and a negative-exponent site has \(At,-sCt\).
Right multiplication by \(t^{-1}\) on each negative site removes its \(t\).
Reversal interchanges the two kinds of sites.
Replacing \(s\) provisionally by an indeterminate \(y\), all endpoint equations have the form
\[
          l_j=N_j x_j,\quad d_j=D_j x_j,\quad l_{j+3}=y\,d_j,
              \qquad (N_j,D_j)=(B,D)\ \text{or}\ (A,C).
\]
A full-rank matrix over \(\mathbb C(y)\) evaluates injectively at the actual infinite-order \(s\).

If \(A,B\) are both invertible then the endpoint at \(y=0\) has a unit diagonal; if \(C,D\) are both invertible its highest \(y\) coefficient has a unit shifted diagonal.
Either case gives full rank.
Next suppose \(A,C\) are invertible and \(B,D\) are singular.
Let \(T=AC^{-1}\), \(L_B=\operatorname{im}B\), \(L_D=\operatorname{im}D\).
These latter two lines are distinct, since \(\det(B-yD)\ne0\).
The kernels of \(B,D\) are distinct by invertibility of the assembled block.
Thus at a singular site the pair \((l_j,d_j)\) ranges freely over \(L_B\times L_D\), and at a regular site it satisfies \(l_j=T d_j\).

Around the four-cycle, between two consecutive singular sites separated by \(k\) regular sites, the linking equations can carry a nonzero value only if \(T^k L_B=L_D\).
Indeed the outgoing \(d\) of the first singular site lies in \(L_D\), and crossing each regular site applies \(T^{-1}\) and a nonzero scalar before the incoming \(l\) of the next singular site must lie in \(L_B\).
This includes a chain from a lone singular site back to itself.
For three singular sites the gaps have lengths \(0,0,1\); for one singular site the gap has length three.
If none of the gaps carries a nonzero value all site pairs vanish and the endpoint is injective.
Thus failure of both endpoints, using \(L_B\ne L_D\), requires
\[
                         T L_B=L_D=T^3L_B .
\]
Then \(T^2\) preserves \(L_B\) and \(T^2 L_B=L_B\), which gives \(T L_D=L_B\).
But
\[
       M(z)=(Tz+BC^{-1})(zI+DC^{-1})^{-1}
\]
now sends the constant line \(L_D\) into \(L_B\): the denominator preserves \(L_D\), while \(T L_D=L_B\) and the other numerator term has image \(L_B\).
The [constant point correspondence obstruction](Yin_C_A0186_v1.md#a-constant-point-correspondence-in-a-two-dimensional-transfer) rules this out.
The case \(B,D\) invertible and \(A,C\) singular follows by \(t\)-inversion, which preserves the sign count and the degree sum.

## A half-period on the shift in the remaining coefficient case

After the preceding exclusions and \(t\)-inversion if needed, \(A,D\) are invertible and \(B,C\) have rank one.
Here take \(N=24p\) and retain the same \(m=1,4\).
For \(z\in\mu_N\) take \(\xi=z^{24}\) and multiply the complement shift \(P\) by \(z^{3p}\).
The \(t\) exponents \(n_j\) are the centered integer representatives of \(N/2+24mr^j\bmod N\).
The \(s\) shift has exponent \(9p\) at each site; change one of the four representatives by \(-N\).
Write \(k_j\) for the four shift exponents and \(S=\sum_j k_j=N/2\).
All these choices agree with the specified unitary representation at each \(N\)-th root.
Use positive integers \(P_+,P_-\) for the sum of the positive \(n_j\) and the absolute sum of the negative ones.
They satisfy
\[
         P_+=P_-=\begin{cases}2N/5,&p=5,\\3N/13,&p=13.\end{cases}
\]
Indeed the centered weights divided by \(N\) are the pairs \(\pm3/10,\pm1/10\) and \(\pm5/26,\pm1/26\), respectively.
Reversing the root order or negating the \(t\) weights for the inverted marking gives the same two sums and \(s\) exponents.
In particular \(S>P_+=P_-\).

The Laurent matrix has diagonal block \(B+A z^{n_j}t\) in channel \(j\), with its other block \(-z^{k_j}s(D+C z^{n_j}t)\) in channel \(j+3\).
It is invertible in the bounded operator algebra at all sufficiently small real \(z>0\).
To see this, put \(y_j=z^{n_j}t\).
The polynomial \(\det(B+Ay)\) is \(c y+c' y^2\) with \(cc'\ne0\), since \(A\) is invertible, \(B\) has rank one and the determinant has a nonzero circle root.
For \(n_j>0\), the norm of \((D+Cy_j)(B+Ay_j)^{-1}\) is \(O(z^{-n_j})\), by the adjugate formula uniformly on the circle of radius \(z^{n_j}\).
For \(n_j<0\) the same quotient is uniformly bounded near infinity because \(A\) is invertible.
In particular all diagonal blocks have bounded inverses for each sufficiently small fixed \(z>0\).
Right-normalizing by these blocks gives \(I-V(z)\), where \(V(z)\) moves each channel by \(3\bmod4\).
Every product in \(V(z)^4\) uses each channel once, so \(\|V(z)^4\|=O(z^{S-P_+})\) by submultiplicativity and the unitarity of \(s\).
Thus \(I-V(z)^4\) and \(I-V(z)\) are invertible for sufficiently small \(z>0\).

## The scalar matching spread on eight coordinates

In every site choose a constant input basis in which \(B\) and \(C\) each have a zero column, using their two kernel lines if distinct and their common line otherwise.
The basis changes preserve the bounded invertible evaluation and the nullities at the roots.
In any perfect matching of the scalar eight-square support let \(e_j\) be the number of the two columns at site \(j\) matched into the shifted block.
The row count at \(j\) is \(2-e_j+e_{j-3}=2\).
Thus all \(e_j=e\), where \(e=0,1,2\).
We bound the cost of every choice of a term at each matched position.

For \(e=0\) each site uses both diagonal columns.
At least one chosen term uses \(A\) since \(B\) has a zero column, so at site \(j\) the exponent is \(n_j\) or \(2n_j\).
Over all sites the cost is between \(-P_-\) and \(P_+\), using \(\sum n_j=0\).
For \(e=2\) both shifted columns are used and at most one chosen term uses \(C\).
The total cost is then between \(2S-P_-\) and \(2S+P_+\).
For \(e=1\) each site contributes \(k_j\) and between zero and two copies of \(n_j\).
The total is between \(S-2P_-\) and \(S+2P_+\).
Since \(S>P_+=P_-\), the full matching spread is at most
\[
                       (2S+P_+)-(-P_-)=2S+2P_+<2N .
\]
The scalar support admits perfect matchings, for example from invertibility of \(A\) on each diagonal site.
By the [two-end matching interpolation estimate](Yin_C_A0219_v1.md#statement), applied with block size one and the bounded invertible evaluation above, the sum of regular nullities at all \(N\) phases is at most this spread.
The actual representation twists give sum \(2N\), a contradiction.
This exhausts the coefficient cases and proves \(H'=H''\).
The image of \(H'\) in a solvable quotient is both perfect and solvable, hence trivial, giving the last quotient assertion.

## Assessment history

### Decision eliminating-the-four-remaining-noncyclic-markings

| Field | Value |
| --- | --- |
| date | 2026-11-26T14:07 |
| status | proved |
| reason | The two finite representations produce more total kernel dimension than the degree bound allows in every noncyclic marking. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The full stated result with its hypotheses. |
| argument | [Four channels through the marked finite quotient](#four-channels-through-the-marked-finite-quotient) | Markings, regular absorption and invertible coefficient corners. |
| argument | [A mixed endpoint with three sites of one kind](#a-mixed-endpoint-with-three-sites-of-one-kind) | Both endpoints including the constant line obstruction. |
| argument | [A half-period on the shift in the remaining coefficient case](#a-half-period-on-the-shift-in-the-remaining-coefficient-case) | The crossed rank pattern and bounded invertibility off the phase set. |
| argument | [The scalar matching spread on eight coordinates](#the-scalar-matching-spread-on-eight-coordinates) | All scalar matching costs for a common or distinct kernel line. |
| review | [Eliminating the four remaining noncyclic markings](../audits/reviews/Yin_R_A0208_v1.md#eliminating-the-four-remaining-noncyclic-markings) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-eliminating-the-four-remaining-noncyclic-markings)

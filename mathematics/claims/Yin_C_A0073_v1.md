---
author: Yin
---

# Finite time errors for signed first-return means at a fixed endpoint

## Statement

Use the original matrix, positive contraction \(H\), kernel projection \(p\), distinct sites \(x=\delta_g e_i,y=\delta_e e_j\), real or imaginary polarization \(\zeta\), and padded first returns \(f_n^\pm\) of [C67](Yin_C_A0067_v1.md#statement).
Write \(u_n^\pm=\xi_\pm^*H^n\xi_\pm\), \(a_\pm=\xi_\pm^*p\xi_\pm\) for the *unpadded* probe moments and their limits, where \(\xi_\pm=(x\pm\zeta y)/\sqrt2\).
Set \(v_n=\operatorname{Re}(\zeta x^*H^n y)\), \(c=\lim v_n\), and \(m_\pm=\sum n f_n^\pm=2/(1+a_\pm)\).
Then the signed mean difference is \(d=m_--m_+=m_+m_-c\).
Every finite quantity below uses actual group endpoints through (1) of C67.

If \(u_n^\pm-a_\pm\le K(1+n)^{-\alpha}\) for both signs and all \(n\ge0\), with \(\alpha>0\), then the raw signed prefix \(d_N=\sum_{n=1}^N n(f_n^--f_n^+)\) satisfies
\[
    |d-d_N|\le 2K(1+2^{1+\alpha})N^{-\alpha}
                     \sum_{h\ge1}2^{-h}h^{1+\alpha}\quad(N\ge1).       \tag{1}
\]
This gives a stopping rule for the actual signed mean with supplied constants.
If just the total unnormalized kernel trace is independently known, a different rule gives a computable error interval tending to zero from finite endpoint and return moments, without requiring either exponent or the separate atoms of the probes.
Faster temporal cancellation at the chosen endpoint can improve the recovery of \(c\).
Suppose also \(|v_n-c|\le C(1+n)^{-\gamma}\) and \(|v_n-v_{n-1}|=O(n^{-1-\gamma})\) for \(\gamma>0\).
There is a denominator \(D_N\), computed at the same finite time, for which
\[
            |d_N/D_N-c|=O(N^{-\min(\gamma,1+\alpha)}) .                \tag{2}
\]
A finite numerical error bound for (2) uses the supplied envelope for \(|v_n-c|\) and the observed signed increments through time \(N\).
The proof gives this bound even for a non-power envelope.

On an individual four-line group a nonclosed-range row has \(c=1/4\) at a nonidentity endpoint and \(d=16/35\).
There the uncorrected error \(|d-d_N|\) is of order \(N^{-1/2}\), (2) gives \(O(N^{-3/2})\), and a two-time combination of the raw first means themselves estimates \(d\) to \(O(N^{-3/2})\).
Conversely on that same group there are pairs of nonclosed-range matrices with identical selected probe data through arbitrarily high order and true signed first means separated by at least \(11/240\).
The matrix sizes in this last comparison grow with the order, while the group, endpoint, norm bound and propagation bound stay fixed.
The two matrices can have identical total kernel trace and identical ordinary return traces at every order.

## Argument

Let \(s_n^\pm=1-\sum_{l=1}^n f_l^\pm\), with \(s_0^\pm=1\), and put \(a_n^\pm=u_{n-1}^\pm-u_n^\pm\) for \(n\ge1\), \(a_0^\pm=0\).
The arrays \(a_n^\pm\) are nonnegative, with sum at most one by spectral monotonicity.
In the following generating series multiplication is ordinary convolution of time indices.
For either sign the [rank-one renewal identity](Yin_C_A0067_v1.md#argument) gives
\[
 s(z)=\frac{1-f(z)}{1-z}
    =\left[1-\tfrac12 a(z)\right]^{-1}
    =\sum_{h\ge0}2^{-h}a(z)^h .                                      \tag{3}
\]
Indeed \((1-z)\sum_{n\ge0}u_n z^n=1-a(z)\), and padding averages this series with one.
The sum of the coefficients of \(s\) is \(m_\pm\le2\).
For \(n\ge1\), \(\sum_{l\ge n}a_l=u_{n-1}-a_\pm\le K n^{-\alpha}\).
If \(h\) positive summands total at least \(N\), at least one is at least \(\lceil N/h\rceil\).
Summing the nonnegative convolutions in (3) gives
\[
 \sum_{l\ge N}s_l\le K L_\alpha N^{-\alpha},
                \qquad L_\alpha=\sum_{h\ge1}2^{-h}h^{1+\alpha}.
\]
The individual raw mean tail is \(N s_N+\sum_{l\ge N}s_l\).
Monotonicity gives \(N s_N\le2\sum_{l\ge\lceil N/2\rceil}s_l\), proving (1).

For the rate-free stopping rule, take any lower bound \(\ell_\pm\le a_\pm\) and integer \(1\le H'\le N\).
In (3) bound all terms with more than \(H'\) factors by their full mass \(2^{-H'}\).
For the others the argument above needs just one factor with index at least \(k=\lceil N/H'\rceil\).
The sum of \(2^{-h}h\) is two and that factor's tail is \(u_{k-1}^\pm-a_\pm\).
Thus a fully finite upper bound for the remainder of each raw mean is
\[
    0\le m_\pm-\sum_{n\le N}n f_n^\pm
      \le N s_N^\pm+2(u_{k-1}^\pm-\ell_\pm)+2^{-H'}.                  \tag{1a}
\]
The two resulting intervals give bounds on \(d\) by subtraction and on \(c=1/m_+-1/m_-\) by taking reciprocals, using \(m_\pm\ge1\).
To make (1a) shrink without a known rate, suppose \(d_0=(\operatorname{Tr}_m\otimes\tau_G)p\) is given.
Write \(r_l=(\delta_e e_l)^*p(\delta_e e_l)\).
When \(i\ne j\), \(d_0=a_++a_-+\sum_{l\ne i,j}r_l\).
When \(i=j\), \(2d_0=a_++a_-+2\sum_{l\ne i}r_l\), since the diagonal coefficient is unchanged by translating its site.
To bound either \(a_\pm\) below, replace every other term on its right-hand side by its corresponding degree-\(N\) moment of \(H\) as an upper bound, subtract from the known total, and take the maximum with zero.
These finite lower bounds increase to \(a_\pm\) by spectral convergence.
With \(H'=\max(1,\lfloor\sqrt N\rfloor)\) one has \(k\to\infty\), and \(Ns_N^\pm\to0\) since the decreasing survivals are summable.
Consequently (1a) eventually proves any prescribed positive accuracy using the observed moments, including when the two individual probe atoms were initially unknown.
This requires usable bounds or exact data for the input coefficients, group-product equalities and supplied trace to perform numerical certification.

Let \(b=s^-*s^+\), \(B_N=\sum_{l=0}^N b_l\) and \(D_N=B_N-(N+1)b_N\).
Since \(a_n^- -a_n^+=2(v_n-v_{n-1})\) and \(v_0=0\), taking the difference of the reciprocals in (3) gives the exact finite identity
\[
       L_N:=\sum_{l=0}^N(s_l^--s_l^+)=\sum_{l=0}^N b_l v_{N-l}.
\]
In particular for \(y_n=v_n-c\) and \(E=b*y\), \(L_N=c B_N+E_N\).
The raw prefix equals \(L_N-(N+1)(L_N-L_{N-1})\), so for \(N\ge1\)
\[
            d_N-cD_N=E_N-(N+1)(E_N-E_{N-1}).                           \tag{4}
\]
This formula keeps the signed temporal increments at this endpoint.

Here is an explicit bound involving only finite quantities and any verified upper envelope \(e_n\ge|v_n-c|\).
Let \(h=\lfloor N/2\rfloor\) and define
\[
 \begin{split}
 B_N^{(0)}={}&\sum_{l=0}^N b_l e_{N-l},\\
 B_N^{(1)}={}&\left|\sum_{l=0}^{h} b_l(v_{N-l}-v_{N-l-1})\right|
       +\sum_{l=0}^{N-h-2} e_l|b_{N-l}-b_{N-1-l}|
       + e_{N-h-1} b_{h+1}.
 \end{split}
\]
An empty sum is zero.
Split the convolution at \(l=h\) and reverse the order of the remaining factors in both \(E_N\) and \(E_{N-1}\).
The difference of the first pieces gives the signed sum displayed here, since differences of \(y\) equal those of \(v\).
The second pieces give the last sum and the single unmatched boundary term.
Thus whenever the computed \(D_N\ne0\),
\[
        |d_N/D_N-c|\le (B_N^{(0)}+(N+1) B_N^{(1)})/|D_N| .             \tag{5}
\]
An upper bound on a positive spectral tail for the two individual probes yields (1); an upper bound on the *signed* endpoint remainder allows the separate use of (5).
The latter hypothesis already bounds the error of the ordinary endpoint moment \(v_N\) itself.
Formula (5) controls how that accuracy transfers through the nonlinear first-return calculation.

For the rates, the tail estimate for the decreasing sequence \(s_n\) gives \(s_n=O((1+n)^{-1-\alpha})\).
Also \(f_n\) decreases for \(n\ge2\), since it is the moment of order \(n-2\) of a positive contraction at the vector in the renewal compression.
Summing \(f_l\) between \(\lceil n/2\rceil\) and \(n\) bounds \(f_n=O((1+n)^{-2-\alpha})\) by the preceding estimate for \(s_{\lceil n/2\rceil-1}\).
Splitting the convolution of the two survival sequences at \(n/2\) gives \(b_n=O((1+n)^{-1-\alpha})\).
Splitting its first difference in the same way as in (5) differentiates the factor at the larger index on each piece.
The single boundary product is \(O((1+n)^{-2-2\alpha})\), and the two sums are \(O((1+n)^{-2-\alpha})\) by \(\sum s_l\le2\).
Hence \(|b_n-b_{n-1}|=O(n^{-2-\alpha})\) and \(D_N\to m_-m_+\ge1\).
With \(e_l=C(1+l)^{-\gamma}\), the bounds for \(B_N^{(0)}\) and \(N B_N^{(1)}\) are each
\[
 O\!\left(N^{-\gamma}+N^{-1-\alpha}\sum_{l\le N/2}(1+l)^{-\gamma}
                 +N^{-\alpha-\gamma}\right).
\]
When \(\gamma=1\) the logarithm is absorbed by the strict \(\alpha>0\); for \(\gamma<1\) or \(\gamma>1\) the power sum gives (2) directly.

## A nonzero signed endpoint and the rate of its raw first mean

Choose any infinite-order \(u\) in the fixed four-line group, let \(T=((1+u)/2,(1-u)/2)\), and put \(A=(1-u)T\), \(M=4\).
The row \(T\) is a coisometry because \(TT^*=I\).
The range of \(A\) is the dense nonclosed range of \(1-u\) on its cyclic cosets, and its kernel projection is \(p=I-T^*T\).
With \(H_0=(2+u+u^{-1})/4\), the original powers are \(H^n=p+T^*H_0^nT\).
At \(g=u\) and indices \(i=1,j=2\), \(p_{12}=(u-u^{-1})/4\), and \(c=1/4\) for the real probes.
Their unpadded atoms are \(3/4,1/4\), so their padded atoms are \(A_+=7/8,A_-=5/8\) and \(d=16/35\).
Writing \(w_n(l)=4^{-n}\binom{2n}{n+l}\), with zeros outside the binomial range, gives
\[
  v_n-c=\tfrac14(w_n(2)-w_n(0)),\qquad
  u_n^\pm-a_\pm=\tfrac12 w_n(0)\ \pm\ \tfrac14(w_n(2)-w_n(0)).
\]
These formulas follow by multiplying the actual finite group-ring coefficients on the cyclic subgroup.
The identity \(w_n(2)/w_n(0)=n(n-1)/[(n+1)(n+2)]\), the ratio \(w_{n+1}(0)/w_n(0)=(2n+1)/(2n+2)\), and \(w_n(0)\asymp(1+n)^{-1/2}\) give \(\alpha=1/2\) and \(\gamma=3/2\), including the first-difference estimate.
Thus (2) gains a full power of time over the individual first-mean error bound.

One can also correct the raw signed mean directly without using \(c\) or the two limiting means in the finite estimator.
For \(s=\sqrt{1-z}\) use the branch positive on \(0<z<1\), and let \(b=(1-s)/(1+s)\).
The cyclic Green function at exponent \(l\) is \(b^{|l|}/s\), by the second-order recurrence and normalization at zero. [C67, cyclic calculation](Yin_C_A0067_v1.md#time-cancellation-on-a-gapless-cyclic-direction-of-a-four-line-group)
The padded generating functions of the probe moments obey
\[
 (1-z)h^\pm(z)=A_\pm+\tfrac14s\ \pm\ \tfrac18s(b^2-1)=:A_\pm(s).
\]
In particular \(J(s)=1/A_-(s)-1/A_+(s)=d+c_1s+O(s^2)\), where \(c_1=(A_+^{-2}-A_-^{-2})/4=-384/1225\).
The first-return difference is \(f^-(z)-f^+(z)=-(1-z)J(s)\).
Differentiation and division by \(1-z\) give the generating function of the actual weighted prefixes:
\[
                 \sum_{N\ge0}d_N z^N=\frac{z}{1-z}\left(J(s)+\tfrac12 sJ'(s)\right).
\]
Its singular terms of order \(s^{-2}\) and \(s^{-1}\) are \(d/(1-z)+(3c_1/2)(1-z)^{-1/2}\).
After subtracting these, the remainder is rational in \(s\), bounded at zero and analytic in a slit disk \(|z|<1+\eta\) cut along \([1,1+\eta)\), for some \(\eta>0\).
Indeed \((1-z)h^\pm(z)\) has real part at least \(1/2\) on \(|z|\le1\) by its spectral representation with the stationary half, and its explicit rational expression is nonzero at \(s=0\).
The remainder has jump \(O(\sqrt{x-1})\) across the short slit at real \(x>1\), by analyticity in \(s\) near zero.
Deforming the coefficient contour to a smaller outer circle around this slit bounds its coefficients by an exponentially decreasing term plus \(C\int_1^{1+\eta/2}x^{-N-1}\sqrt{x-1}\,dx=O(N^{-3/2})\).
The small circle about the branch endpoint contributes zero in the shrinking-radius limit.
Thus
\[
         d_N=d+\frac{3c_1}{2}\,4^{-N}\binom{2N}{N}+O(N^{-3/2}),
 \qquad
         \frac{\sqrt2\,d_{2N}-d_N}{\sqrt2-1}=d+O(N^{-3/2}).
\]
The first bias is nonzero and of order \(N^{-1/2}\).
The second estimate uses the central binomial asymptotic with error \(O(N^{-3/2})\).

This row fails the [finite-power Perron test of C69](Yin_C_A0069_v1.md#finite-and-infinite-components-of-the-lifted-graph) at every power in every constant unitary basis, using any normalization strictly larger than the squared norm as required by that test.
Indeed a passing test on one connected block of size two either gives zero kernel projection or realizes the entire block by copies of a single finite matrix, giving a gap above zero for \(A^*A\).
If there are two singleton blocks, each contributes a constant projection: on the finite components the single state has only one vertex, and infinite components contribute zero.
Conjugating back by a constant unitary preserves constancy.
These alternatives exclude this nonconstant projection of a nonclosed-range row.

## How long two different signed means can share a finite prefix

On the same group fix a nonidentity rose generator \(u\) and let \(P\) be the uniform probability on the identity and a finite symmetric generating set of nonidentity rose elements.
Use the rational polynomial \(V=5I/8+u/4+P/8\).
It has norm at most one, is boundedly invertible by a Neumann series about \(5I/8\), and has positive coefficients on the identity and all these generators.
Fix \(r=1/4\) and an integer \(L\ge3\).
On coordinates \(x_0,\ldots,x_L\), put
\[
       t_0=x_1-r Vx_0,\qquad t_j=x_{j+1}-r x_j\quad(1\le j<L).
\]
Define two square matrices of size \(L+1\) with first \(L\) outputs
\((t_0,(1-u)t_1,t_2,\ldots,t_{L-1})\).
Their last outputs are respectively zero and \((1-u)x_L\).
Both squared norms are at most \(4(1+r)^2+4<16\), since the unmodified difference row array has norm at most \(1+r\); use \(M=16\) for both.
Their entry support radii are at most one.
Each has the full generating support of \(-rV\) in a single entry, which requires the whole group even under independent translations of rows and columns by group elements.
Indeed translating a set containing the identity and all generators into a subgroup places all the conjugated generators in that subgroup.

The first matrix has nonclosed range since the map to the unmodified first \(L\) outputs is onto by forward substitution, and \(1-u\) has nonclosed range.
Its kernel consists of the column \(W=(I,r V,r^2 V,\ldots,r^L V)^t\) applied to \(\ell^2(G)\).
The second matrix is injective by the last constraint, invertibility of \(V\) and injectivity of \(1-u\).
On columns of the form \(W V^{-1}\xi\) its only possible nonzero output is \(r^L(1-u)\xi\).
Taking unit approximate invariant vectors for the cyclic shift gives vectors of norm at least one with images tending to zero, so its range is also nonclosed.
In the first case the projection is \(W D W^*\), \(D=(I+(\sum_{j=1}^L r^{2j})V^*V)^{-1}\).
Here \(\|D-I\|\le r^2/(1-r^2)=1/15\).
At the fixed endpoint \(u\), indices \(1,0\), its real Fourier coefficient is therefore at least \(r(1/4-1/15)=11/240\).
In the second matrix this coefficient is zero.
The corresponding signed first-mean differences differ by at least the same amount, since the factor \(m_+m_-\) is at least one in the first case.

Both contractions \(I-A^*A/16\) are tridiagonal in the coordinate indices and differ only in their \((L,L)\) block.
In the telescoping difference of their \(n\)-th powers, for either matrix element between the first two coordinates one needs at least \(L-1\) steps to reach the changed block and at least \(L-1\) more to return, besides the single difference factor.
All four matrix elements for the two selected probes consequently agree through \(n=2L-2\), at every group displacement.
Thus the signed first-return prefixes also agree to that order by their finite recursion.
No rule using only those prefixes can give a dimension-independent error tending to zero on this family.
This is a limitation on the selected endpoint data; the supplied matrices do differ in their last row.

Write \(O,C\) for the first and second matrices.
The pair \(O\oplus C, C\oplus O\), probed in its first summand, keeps the separation and the exact matching cutoff, now with the same total kernel trace one and exactly the same ordinary return traces at all orders.
Both projections also require the whole group under independent coordinate translations: in the open block \(p_{00}=D\) has positive identity coefficient, and \(p_{10}=rVD\) recovers a translate of \(V\) inside any proposed subgroup algebra by multiplying by its translated bounded inverse. [Translation argument](Yin_C_A0062_v1.md#a-rational-example-using-the-whole-group)

With \(L\) now fixed, one may multiply the nonzero terminal row by any rational \(0<\lambda\le1\).
The kernel, its endpoint separation, the nonclosed ranges and the equality of global traces of the swapped pair persist.
The two single-block contractions differ in norm by at most \(\lambda^2/4\), so their padded probe moments at time \(n\) differ by at most \(n\lambda^2/8\), by telescoping.
For either probe the difference of the generating series of first returns equals the difference of the corresponding moment series multiplied by \((1-f_O(z))(1-f_C(z))\), with consistent subtraction order.
Each of the two factors has coefficient \(\ell^1\) norm two since its first-return probabilities sum to one.
Thus even the first-return coefficients through time \(N\) differ by at most \(N\lambda^2/2\) term by term, with no change in the separated limiting signed means.
This rules out a noise tolerance uniform over these fixed-size inputs for a fixed finite prefix.

## Assessment history

### Decision finite-time-signed-returns

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:03 |
| status | proved |
| reason | Independent review verified the time-error bounds, signed correction, explicit cyclic endpoint and indistinguishable prefixes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite-time estimates for a single polarized coefficient and first mean, with trace-calibrated stopping and limitations of uniform recovery. |
| argument | [Proof](#argument) | Renewal tails, observable corrections, the two-time estimate and the exact and noisy comparisons at a fixed endpoint. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0109_v1.md#whole-argument-finding) | Independent review of the entire argument at the stated scope. |

## Current assessment

[Selected decision](#decision-finite-time-signed-returns)

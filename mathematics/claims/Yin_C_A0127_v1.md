---
author: Yin
---

# Strictly positive small defects for a fixed half-dimensional kernel in a wreath product

## Statement

Let \(G\) be discrete, let \(P\) be a projection of trace \(1/2\) in its regular group von Neumann algebra, and put \(Q=1-P\).
Embed \(G\) at site zero in the restricted wreath product \(H=G\wr\mathbb Z\), and denote its translation by \(t\).
For \(h\in\mathbb CH\), set \(d(h)=\tfrac12-\operatorname{rk}_H(QhP)\), the dimension of the kernel of \(QhP\) restricted to \(P\).
The single sequence of group-ring elements
\[
 h_m=t^{-m}(1+t)^{2m},\qquad m\ge1,
\]
satisfies
\[
  2^{-(2m+1)}
      \ \le\ d(h_m)\
      \le\ \frac{\mathbb E[(2K-m-1)_+]}{m+1}\
      \le\ \frac{1}{2\sqrt{m+1}},
  \qquad K\sim\operatorname{Bin}(m+1,1/2).
\]
In particular these defects approach zero through strictly positive values.
Every finite Laurent polynomial in the same shift has positive defect.
If \(P\) is central in \(\mathcal N(G)\), then every \(h\in\mathbb CH\) has positive defect.

If \(P\) is the kernel projection of a nonzero Schur complement of a two-by-two matrix \(A\) over \(\mathbb CG\) with affiliated-unit first pivot, this same \(A\) provides a fixed three-by-three positive group-ring matrix formula with nullities \(d(h_m)\).
The only varying input to that formula is the displayed Laurent polynomial in \(t\).
The group \(H\) is torsion-free whenever \(G\) is torsion-free, and finitely generated whenever \(G\) is finitely generated.
The conclusion uses the regular trace throughout and does not assume or establish that scalar group-ring injectivity passes from \(G\) to \(H\).

## The Bernoulli representation of the translated projections

Subgroup inclusion replicates the regular representation on right cosets, preserving the initial rank, kernel projection and affiliated-unit condition.
The conjugates \(P_j=t^jPt^{-j}\) at distinct lamp sites commute and have product trace by the [regular lamp-coordinate calculation](Yin_C_A0017_v2.md#copies-in-the-regular-representation).
They generate the algebra of functions of independent fair bits on \(\Omega=\{0,1\}^{\mathbb Z}\).
A finite sum of lamp coefficients times nonzero powers of \(t\) has zero trace, first for group-ring lamp coefficients and then by normality.
This identifies the von Neumann algebra generated together with \(t\) as the tracial crossed product by the bilateral shift.
Thus the algebra and its trace have the usual realization as equivariant operators on the copies of \(\ell^2(\mathbb Z)\) parametrized by \(\omega\in\Omega\).
In these fibers \(P\) multiplies by the occupied-site indicator, \(Q\) by its complement, and \(t\) translates by one, choosing the index orientation accordingly.
The trace of a projection is the expectation of its diagonal entry at the origin, and stationarity gives the same expectation at every site.

If \(h\) is a polynomial in \(t,t^{-1}\) with support exponents \(F\), the intersection of \(P\) with all \(t^{-k}Pt^k\), \(k\in F\), is contained in the kernel of \(QhP\) on \(P\).
It has trace \(2^{-|\{0\}\cup F|}\), proving the lower bound.
If \(P\) is central in its own lamp algebra, conjugating it by an element of \(H\) only changes its site.
The same proof then works with \(F\) the set of the shift exponents in the support of any \(h\in\mathbb CH\).

## Positive minors of the shift polynomial

In a fiber, the unrestricted Laurent polynomial matrix on \(\mathbb Z\) has entry
\[
  (h_m)_{i,j}=\binom{2m}{i-j+m},
\]
where a binomial coefficient outside its usual range is zero.
Suppose \(j_1<\cdots<j_s\) and \(i_1<\cdots<i_s\) satisfy \(|i_k-j_k|\le m\) for all \(k\).
The determinant of this selected minor is strictly positive.

Indeed it is the corresponding minor of \((1+t)^{2m}\) with output indices \(i_k+m\).
Every minor of the single lower bidiagonal matrix \(1+t\) is nonnegative because a step of zero or one preserves the order in any matching of distinct input and output indices.
Thus a nonzero term in the determinant must match the ordered lists and gives determinant one.
A chain of such nonzero minors through the \(2m\) factors is obtained at time \(\ell\) by taking the indices
\[
 z_k(\ell)=\max\{j_k,\,i_k+m-(2m-\ell)\},\qquad 0\le\ell\le2m .
\]
They start at \(j_k\), end at \(i_k+m\), stay strictly increasing in \(k\), and increment by zero or one at each step.
In the Cauchy-Binet sum all terms are nonnegative and this chain contributes one.
All sums here are finite by the bandwidth.

## From finite blocks to the trace rank

Let \(L=m+1\) and partition an interval \(I\) of length \(bL\) into \(b\) consecutive blocks of length \(L\).
In a block containing \(K_j\) occupied sites, select \(\min(K_j,L-K_j)\) occupied columns and as many vacant rows.
Pair them in increasing order within that block and concatenate across all the blocks.
Every pair has displacement at most \(m\), so the positive-minor calculation gives one invertible minor of \(Qh_mP\) of size \(\sum_j\min(K_j,L-K_j)\) when that size is positive.
This construction accounts for matrix entries between different blocks.

Let \(R_\omega\) be the final support of \(Qh_mP\) in this fiber.
The images of the selected columns are supported in the interval \(I'\) obtained by adding \(m\) sites at each end of \(I\).
Their span is therefore contained in the intersection of \(\ell^2(I')\) with the range of \(R_\omega\).
Consequently \(\operatorname{Tr}(\chi_{I'} R_\omega\chi_{I'})\ge\sum_j\min(K_j,L-K_j)\), including the case of a zero sum.
Take expectations, use stationarity, divide by \(bL+2m\), and let \(b\) tend to infinity with \(m\) fixed.
One gets
\[
 \operatorname{rk}_H(Qh_mP)\ \ge\ \mathbb E[\min(K,L-K)]/L,
 \qquad K\sim\operatorname{Bin}(L,1/2).
\]
The identity \(K-\min(K,L-K)=(2K-L)_+\) gives the asserted bound on \(d(h_m)\).
By symmetry and Cauchy-Schwarz, \(\mathbb E[(2K-L)_+]=\tfrac12\mathbb E|2K-L|\le\sqrt L/2\).

## The fixed Schur matrix

Write \(A=\left(\begin{smallmatrix}a&b_0\\c&d\end{smallmatrix}\right)\) with \(a\) an affiliated unit and \(S=d-ca^{-1}b_0\).
Use the [fixed group-ring witness](Yin_C_A0125_v1.md#group-ring-witnesses-and-the-exact-projection)
\[
 B(h)=
 \begin{pmatrix}
 a&0&b_0\\c&0&d\\0&a&b_0h\\0&c&dh
 \end{pmatrix}.
\]
Over the affiliated algebra, projection of \(\ker B(h)\) to the last coordinate is an isomorphism onto the right module \(\{\xi:S\xi=Sh\xi=0\}\).
Since \(P\) is the kernel projection of \(S\), this module has dimension \(d(h)\).
Thus the positive matrix \(B(h_m)^*B(h_m)\) of fixed size three has the indicated nonzero nullity.

A finite-order element of \(H\) has zero translation exponent, and a finite-order lamp configuration has finite-order entries, proving the torsion-free assertion.
Conjugation by the shift transports a finite generating set of the lamp at zero to generators at every site.
If a given ambient group already contains the wreath product of the coefficient subgroup by this shift, the same calculation runs inside it by subgroup inclusion.
For an arbitrary original \(G\), the sequence belongs to the extension and alone gives no contradiction with scalar injectivity in \(G\) or with torsion-freeness.

## Assessment history

### Decision wreath-product-defects

| Field | Value |
| --- | --- |
| date | 2026-11-23T07:16 |
| status | proved |
| reason | Independent inspection verified the complete statement, its arguments and the stated limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Strict positive lower and vanishing upper bounds in one regular wreath product. |
| argument | [Bernoulli coordinates](#the-bernoulli-representation-of-the-translated-projections) | Product trace, shift covariance and cylinder lower bound. |
| argument | [Positive minors](#positive-minors-of-the-shift-polynomial) | Order-preserving paths in the bidiagonal powers. |
| argument | [Finite-block estimate](#from-finite-blocks-to-the-trace-rank) | A combined minor, range projection and boundary limit. |
| argument | [Fixed matrix](#the-fixed-schur-matrix) | The same Schur input and three-by-three Gram family. |
| review | [Independent finding](../audits/reviews/Yin_R_A0164_v1.md#wreath-product-defects) | Whole argument at the stated scope. |

## Current assessment

[Selected decision](#decision-wreath-product-defects)

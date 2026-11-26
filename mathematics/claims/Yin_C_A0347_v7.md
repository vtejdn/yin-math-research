---
author: Yin
---

# An intrinsic time-chain proof under the integral determinant conjecture

## Statement

Suppose \(G\) has the integral determinant property: for every square matrix \(B\) over \(\mathbb ZG\) its unnormalized logarithmic Fuglede--Kadison determinant with zero singular values omitted is nonnegative.
The zero matrix has omitted-zero logarithm zero in this convention.
Then the [exact Brown atom theorem for unbounded rational evaluations](Yin_C_A0347_v6.md#statement), including its punctured logarithmic estimate, holds on \(G\).
In particular for an algebraic-coefficient actual rational matrix \(Y\) of size \(k\),
\[
             k\mu_Y(\{\lambda\})=\lim_{m\to\infty}\dim_G\ker(Y-\lambda I)^m
                           \qquad(\lambda\in\mathbb C),
\]
and all atoms are algebraic ordinary eigenvalues.
The [same-layer scalar injectivity and atomlessness equivalence](Yin_C_A0347_v4.md#statement) follows at every finite scalar inverse layer and their union.
These conclusions use the integral determinant property directly and need no finite approximation of the marking.
We do not assume this property for all groups. For sofic groups it is available from the established determinant bounds. [Knebusch, Definition 4.1 and Theorem 4.4](https://arxiv.org/pdf/0804.0530#page=6)
For a group under the present hypothesis the union criterion concerns \(\overline{\mathbb Q}G\); the previously cited full complex base change still applies in the sofic case.

## Pseudodeterminants under a change of metric

Use \(\mathcal P(B)=\int_{(0,\infty)}\log t\,d\operatorname{Tr}_G\mathbf1_{[0,t]}(|B|)\) for the unnormalized omitted-zero log determinant of a bounded square matrix, allowing \(-\infty\).
For a bounded invertible \(D\) in the same matrix algebra and a projection \(e\), put
\[
             H_e(D)=\tfrac12\operatorname{Tr}_{e}\log(eD^*De).
\]
The trace in a corner is its inherited unnormalized trace and the argument of the logarithm is invertible in that corner.
Write \(p\) for the kernel projection and \(q\) for the range projection of \(B\).
Polar decomposition of \(B\) identifies \(1-p\) with \(q\); polar decomposition of \(Dq\) identifies \(q\) with the range projection of \(Dq\).
Using these identifications to multiply the restricted operators in the support corner, determinant multiplicativity gives
\[
                  \mathcal P(DB)=\mathcal P(B)+H_q(D).
\]
This also holds if \(\mathcal P(B)=-\infty\), since the other term is finite.
Applying the same formula to the adjoint gives
\(\mathcal P(BD^{-1})=\mathcal P(B)+H_{1-p}(D^{-*})\), where \(D^{-*}=(D^{-1})^*\).
Multiplying a positive invertible \(D^*D\) in the decomposition by \(q,1-q\) with the two triangular elimination shears gives
\[
                   H_q(D)=\mathcal L(D)+H_{1-q}(D^{-*}),
\]
where \(\mathcal L(D)=\operatorname{Tr}_G\log|D|\).
Indeed the reciprocal of the second Schur pivot is the \(1-q\) compression of \((D^*D)^{-1}\).
The determinant of each triangular shear is one, and the factors have bounded inverses.
For a general \(D\), \(\mathcal L(D^{-*})=-\mathcal L(D)\).

The range closure of \(BD^{-1}\) is still that of \(B\).
Combining the formulas gives
\[
        \mathcal P(DBD^{-1})
           =\mathcal P(B)+H_{1-q}(D^{-*})+H_p(D).
\]
The two complementary projections \(1-q,p\) have the same trace \(\nu\).
The absolute change between finite log determinants is at most \(\nu\log(\|D\|\|D^{-1}\|)\), by bounding each positive compression between the extreme singular values squared.
The equality preserves the value \(-\infty\) as well.
For a diagonal \(D\) which equals a real \(D_0\ge1\) on a projection of trace \(u\) and one on its complement, one also has \(H_q(D)\le u\log D_0\) since \(H_{1-q}(D^{-*})\le0\).
Thus scaling these rows costs at most \(u\log D_0\) in an upper bound for \(\mathcal P(DB)\).

## Arithmetic estimates without finite sites

Take the unit-weight open chain \(L_m(1)\) for the output \(P(Y)\) in the [time-chain construction](Yin_C_A0347_v6.md#the-singular-product-on-an-open-time-chain).
For momentary use before any assertion of logarithmic integrability, the construction is purely algebraic in the affiliated algebra.
Let \(K\) be the fixed Galois coefficient field of degree \(l\), \(D_0\ge1\) the height bound for the integer polynomial of degree at most \(n\), and \(h\) the coordinates per time.
Multiply the whole matrix by an integer \(b\ge1\) clearing all denominators, obtaining \(B\) over the algebraic integers of \(K\).
Use multiplication on an integral basis of \(\mathcal O_K\) to represent its entries by integral matrices.
This restriction of scalars gives a square matrix over \(\mathbb ZG\) with \(\mathcal P\ge0\) by hypothesis.
An invertible constant change of basis for \(K\otimes_{\mathbb Q}\mathbb C\), repeated on every coordinate, identifies it with the direct sum of the \(l\) coefficient embeddings of \(B\).
Its condition number depends only on the field and the chosen basis.
The similarity formula therefore gives \(\sum_\sigma\mathcal P(\sigma B)\ge-O_n(m)\).
Each term is bounded above and thus finite from below as well.

After dividing the \(km\) output rows of any \(\sigma B\) by \(D_0\), its regular norm is bounded independently of \(m,D_0,P\), by the sparse row and column sums.
The omitted-zero log determinant of this bounded rescaled matrix is at most \(O_n(m)\).
The row estimate of the preceding section now gives \(\mathcal P(\sigma B)\le km\log D_0+O_n(m)\).
Subtract the \(l-1\) other upper bounds, and undo the common denominator, to obtain
\[
         \mathcal P(L_m(1))\ge -(l-1)km\log D_0-O_n(m).
\]
For fixed algebraic shifts the same argument gives a bound \(-O(m)\).
Applied to any single bounded algebraic group-ring matrix, restriction of scalars likewise gives a finite omitted-zero logarithm, and in particular its affiliated inverse when it exists is in the logarithmic class.
All the rational outputs used in the pencil identity are consequently in that class by the [single linearization argument](Yin_C_A0347_v4.md#logarithmic-integrability-for-unbounded-evaluations).

For the time-layer diagonal \(D=\operatorname{diag}(I,rI,\ldots,r^{m-1}I)\), \(0<r<1\), the actual kernel trace of \(L_m(1)\) is \(\kappa_m=\dim_G\ker P(Y)^m\).
The similarity estimate gives directly
\[
           \mathcal P(L_m(r))\ge \mathcal P(L_m(1))
                                      +(m-1)\kappa_m\log r .
\]
There is no finite-site limit here.
Insert the missing zero singular values with the cutoff \(\log\eta\), \(0<\eta<1\), divide by \(m\), and pass to the circular pencil by sending \(m\to\infty\) at fixed \(r,\eta\).
The extra term \((\kappa_m/m)\log\eta\) tends to zero since \(\kappa_m\le k\).
The [bounded time-Fourier limit and the actual Schur determinant identity](Yin_C_A0347_v6.md#two-limits-and-the-exact-logarithmic-slope) are unchanged.
Removing the cutoff, taking the slope at zero and subtracting its exact mass give the algebraic atom formula and the punctured logarithmic estimate.
That estimate, with the same field-degree coefficient of \(\log D_0\) for every \(n\), excludes transcendental atoms by the [polynomial small-value argument](Yin_C_A0347_v6.md#removing-exactly-the-zero-mass).
The proof of the layer criterion now applies with these inputs.

## Assessment history

### Decision intrinsic-complementary-determinants-on-the-time-chains

| Field | Value |
| --- | --- |
| date | 2026-11-26T19:16 |
| status | proved |
| reason | The complementary determinant identity and integral restriction of scalars replace the finite-site lower bounds by direct estimates on the group. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The complementary determinant identity and integral restriction of scalars replace the finite-site lower bounds by direct estimates on the group. |
| argument | [Pseudodeterminants under a change of metric](#pseudodeterminants-under-a-change-of-metric) | Pseudodeterminants under a change of metric. |
| argument | [Arithmetic estimates without finite sites](#arithmetic-estimates-without-finite-sites) | Arithmetic estimates without finite sites. |
| dependency | [Version 5](Yin_C_A0347_v5.md#statement) | The stable compression determinant or the inverse chart identifies Brown mass with the limiting generalized kernel in the stated cases. |
| review | [Stable unbounded kernels and a bounded resolvent](../audits/reviews/Yin_R_A0241_v1.md#stable-unbounded-kernels-and-a-bounded-resolvent) | Inspection of the preceding result. |
| dependency | [Version 6](Yin_C_A0347_v6.md#statement) | An omitted-minor bound along the open time chain yields the exact logarithmic slope and the generalized-kernel formula for unbounded rational outputs. |
| review | [Exact mass from open time chains](../audits/reviews/Yin_R_A0241_v1.md#exact-mass-from-open-time-chains) | Inspection of the preceding result. |
| dependency | [Scalar inverse layers](Yin_C_A0347_v4.md#statement) | The preceding scalar criterion and logarithmic-operator argument. |
| review | [Scalar atomlessness at every inverse layer](../audits/reviews/Yin_R_A0239_v1.md#scalar-atomlessness-at-every-inverse-layer) | Independent inspection of the preceding layer criterion. |
| review | [Intrinsic complementary determinants on the time chains](../audits/reviews/Yin_R_A0241_v1.md#intrinsic-complementary-determinants-on-the-time-chains) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-intrinsic-complementary-determinants-on-the-time-chains)

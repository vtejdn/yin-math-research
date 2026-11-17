---
author: Yin
---

# Estimating signed shell sums when the collected row products lie in a free subgroup

## Statement

Let \(G\) be a finitely generated group, \(A\in M_{r,m}(\mathbb CG)\), and \(K\le G\) a finitely generated free subgroup.
Assume only that the **collected** group-ring matrix \(AA^*\) belongs to \(M_r(\mathbb CK)\).
This is a condition on second-order product fibers of the original input: for each pair of rows, sum over all columns and all pairs of input terms with the same group difference.
The entire matrix \(A\) and its kernel projection \(p\) may still require \(G\) even after row and column translations.
In particular on a good four-line group the condition can use any verified [free subalphabet](Yin_C_A0059_v1.md#statement) containing the surviving row products.

The true projection satisfies \(\sum_g e^{c|g|}\|\widehat p(g)\|_{\rm HS}^2<\infty\) for some \(c>0\), and its unnormalized trace is integral.
For the original matrix \(Q=I-A^*A/M\), \(M>\|A\|^2\), there is an \(\alpha\in(0,2)\) with \(\tau_m(Q^{2^j}-Q^{2^{j+1}})\le C 2^{-\alpha j}\).
Thus for every \(\beta\ge0\), \(\kappa\alpha>\beta\), the signed finite arrays of [C76](Yin_C_A0076_v1.md#statement) satisfy on this **single** group
\[
   \sum_{|g|\ge R}(1+|g|)^\beta
          \sum_{i,j,\zeta}|B_\bullet(g,i,j,\zeta)|^2
           \ \le C_{\beta,\kappa}\{e^{-c'R}+R^{-(\kappa\alpha-\beta)}\},
                  \qquad R=2^J,\quad J\ \text{large}.                   \tag{1}
\]
Given any desired finite power of decay on the right, a sufficiently large fixed \(\kappa\) realizes it, while the time horizon on each radius-\(R\) shell remains \(O(R^\kappa\log R)\).
This need not be a practical enumeration size.
No same-kernel closed-range row operator is used to obtain (1).
The following identity for finite products, resolvents and the projection also applies to an arbitrary subgroup \(K\) subject to the same support condition; its use for decay then requires appropriate estimates over that subgroup.

## Collecting equal endpoints before applying a subgroup estimate

For each column \(j\), pick representatives \(x\) of the finitely many right cosets \(Kx\) meeting that column's support, and write \(A_{\bullet j}=\sum_x F_{j,x}x\) with \(F_{j,x}\) a column over \(\mathbb CK\).
Concatenate the \(F_{j,x}\) to form \(F\); define \(J\) by \((J\xi)_{j,x}=x\xi_j\), so \(A=FJ\).
Empty columns are allowed and contribute no coordinates to \(J\).
In the row product each term from different cosets of the same column has support outside \(K\); the terms from the same coset sum to \(FF^*\).
Consequently \(FF^*=E_K(AA^*)=AA^*\) by hypothesis.
This is an equality of group-ring matrices on \(G\); the discarded terms have zero **total** coefficient at each outside endpoint.

Write \(Q_F=I-F^*F/M\), with \(M\) also sufficient for \(F\) since the two row products agree.
For every \(n\ge0\),
\[
                   I-Q^n=J^*(I-Q_F^n)J .                              \tag{2}
\]
In fact \((A^*A)^l=A^*(AA^*)^{l-1}A=J^*(F^*F)^l J\) for \(l\ge1\).
Taking the normalized Abel sum of (2) gives exactly
\[
 I-R_z^A=J^*(I-R_z^F)J,\qquad R_z^A=(1-z)(I-zQ)^{-1} .
\]
Each term in the finite expansion, as well as every Fourier entry of the Abel sum, is therefore a sum of subgroup entries shifted by the known \(x,y\) on the two sides.
This comparison is made on the original product moments **before** applying the nonlinear first-return recursion at the two sites.
The first returns themselves are computed with the original probes.
Passing to the strong limit in (2) also gives \(I-p=J^*(I-p_F)J\).
By [C58](Yin_C_A0058_v1.md#argument), \(p_F\) has an exponentially weighted square-summable Fourier series in the ambient word length; the subgroup regular representation on \(G\) is a direct sum over right cosets.
Finitely many shifts preserve this conclusion for \(p\) by the triangle inequality.
The trace identity \(\dim_G\ker A=m-r+\dim_K\ker (FF^*)\) follows by the polar decomposition, and the last number is integral by the free-group result.

## Positive spectral mass and the finite first-return arrays

By equality of row products, the **positive** trace spectral measure of \(A^*A/M\) agrees with that of \(FF^*/M\) over \(K\).
Their total measures may have different atoms at zero because their matrix sizes differ.
For the latter positive group-ring matrix, Sauer's rationality and positivity theorem gives a positive Novikov–Shubin invariant in the gapless case. [Sauer, Theorem 3.6](https://doi.org/10.1142/9789812704443_0020)
One can also obtain exactly the needed bound from the retained [free Haar matrix-polynomial algebraicity theorem](../audits/literature/SS15/Yin_U001.md#matrix-algebraicity-and-puiseux).
Indeed the free generators are free Haar unitaries.
For the positive spectral measure \(\mu\) including the atom, \(h(s)=\int s/(s+t)\,d\mu(t)\), \(s>0\), is algebraic near zero and tends to \(\mu(\{0\})\).
A convergent Puiseux series then gives \(h(s)-\mu(\{0\})=O(s^\alpha)\) for some \(0<\alpha<1\), unless the difference vanishes identically, in which case this bound is immediate.
Since \(s/(s+t)\ge1/2\) when \(0<t\le s\), this bounds \(\mu((0,s])\) by \(O(s^\alpha)\); no atomlessness assumption is needed.
When \(\mu((0,s])\) has an independently established upper power bound, any valid exponent strictly below two can be used.
Integrating the heat multiplier against the positive measure gives the claimed dyadic return bound.

For clarity, on shell \(2^j\le|g|<2^{j+1}\) use \(z_j=1-2^{-\kappa j}\) for large \(j\), and sum the cumulative signed first-return differences with weights \(z_j^n\) through \(N_j=\lceil L(j+1)2^{\kappa j}\rceil\) as in C76.
By (2), the limiting off-identity polarized Fourier array has an exponentially small spatial tail, up to the bounded reciprocal products of the two padded probe masses. [Signed means and their normalization](Yin_C_A0067_v1.md#statement)
The squared weighted truncation error over all shells beyond \(R\) is \(O(R^{-(\kappa\alpha-\beta)})\) by the [joint signed coefficient bound and shell estimate](Yin_C_A0076_v1.md#passing-from-finite-returns-to-a-spatial-shell).
Adding the two squared estimates proves (1).
Both ingredients follow from the finite row-product support condition and existing subgroup theorems.

## A row whose off-subgroup products cancel

On an original four-line group choose two marked generators \(u,v\) generating a free group, and put \(a=1-u,\ b=1-v,\ K=\langle u,v\rangle\).
This is a proper subgroup because the original group admits a nonzero binary scalar zero product whereas the group ring of a free group has no zero divisors. [Original factors](Yin_C_A0051_v1.md#statement)
Take finitely many elements \(h_1,\dots,h_N\) such that the set \(D\) of their values is disjoint from \(uD\) and its left differences \(h_i h_j^{-1}\) generate \(G\).
To construct them, use a finite generating list excluding \(u^{\pm1}\) and the identity, and adjoin \(u^2,u^5\), which recover \(u\).
For each element \(s\) in this new list choose both \(v^k,sv^k\).
These two are different and neither is the \(u\)-translate of the other.
Only finitely many \(k\)'s create an overlap or a \(u\)-adjacency with the points previously chosen, since \(v\) has infinite order.
Thus the required differences occur.
Pad by repetitions to a power of two \(N\).
Let \(\sigma_{ji}\in\{\pm1\}\) be an order-\(N\) Walsh array with first row all \(1\)'s, and put \(w_j=N^{-1}\sum_i\sigma_{ji}h_i\).
Orthogonality gives \(\sum_j w_jw_j^*=I\).
Consider the rational row
\[
                    A=(a w_1,\ldots,a w_N,\ a b).
\]
Its row Gram is \(a(I+bb^*)a^*\in\mathbb CK\), supported in a subgroup on two marked letters.
Its support in the first entry contains \(D\), without cancellation by \(uD\); the left differences of this support already generate \(G\).
After any independent row and column translations its left differences are conjugate by the common left row element.
The range is dense and nonclosed since the row before multiplication by \(a\) is onto and \(a\) is injective with dense nonclosed range.
Here the last factored expression additionally supplies a closed-range row with the same kernel; it plays no role in the general transfer.

Write \(S=I+bb^*=3-v-v^{-1}\).
For this row the last diagonal entry of \(p\) is \(I-b^*S^{-1}b=S^{-1}\); the last-row entry in column \(1\) is \(-b^*S^{-1}w_1\).
These expressions follow by the surjectivity just checked.
The geometric expansion of \(S^{-1}\) has positive coefficients at every \(v^n\), so \(p\) has infinite support and fails the finite-support conclusion of every [finite-power test](Yin_C_A0069_v1.md#statement).
Suppose independent translations put all entries of \(p\) inside \(\mathcal N(H')\) for a subgroup \(H'\), and denote the left multiplier in its last row by \(g\).
Left differences from the translated diagonal give \(gvg^{-1}\in H'\).
Thus \(C=-gb^*S^{-1}g^{-1}\in\mathcal N(H')\) is injective.
The translated cross entry gives \(CZ\in\mathcal N(H')\) for \(Z=gw_1h\), where \(h\) is the corresponding right multiplier.
The bounded elements \((C^*C+\epsilon I)^{-1}C^*(CZ)\) converge strongly to \(Z\), so \(Z\in\mathcal N(H')\).
Its support differences contain generators of \(gGg^{-1}\), proving \(H'=G\).
Thus the row-product hypothesis can cover an input and an actual infinite-support projection that each require the entire group.

## Assessment history

### Decision row-product-subgroup-transfer

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:46 |
| status | proved |
| reason | Independent review verified the original product identity, positive spectral measure and shell bound, and support after translations in the example. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Matrices whose collected row products lie in a verified free subgroup, with rectangular traces and the original first-return probes. |
| argument | [Proof](#collecting-equal-endpoints-before-applying-a-subgroup-estimate) | Pointwise product-fiber cancellations, the exact power and Abel identities, the free-subgroup spectral inputs and the worked row. |
| review | [Whole-argument finding](../audits/reviews/Yin_R_A0118_v1.md#whole-argument-finding) | Independent review of the argument and its stated scope. |

## Current assessment

[Selected decision](#decision-row-product-subgroup-transfer)

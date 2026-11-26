---
author: Yin
---

# Weak trace tails and square-zero residues of the two-site transfer

## Statement

Under the [order-24 half-kernel hypotheses](Yin_C_A0288_v1.md#statement), the transfers \(M(z)=(Az+B)(Cz+D)^{-1}\) and \(M(z)^{-1}\) each have exactly one pole on the unit circle.
It is simple, and each of their two nonzero residue matrices has square zero.
In the notation \(t_j=s^jts^{-j}\), \(W=M(t_1)M(t_0)\), one has for some finite constant \(C_0\)
\[
          \operatorname{Tr}\big(1_{(v,\infty)}(|W|)\big)\le C_0/v
                                      \qquad (v\ge1).
\]
The corresponding lower bound by a positive multiple of \(1/v\) follows from the [one-factor lower estimate](Yin_C_A0290_v1.md#singular-value-bounds-for-two-cyclic-factors).
Traces here use Haar probability on the group and the ordinary two-coordinate trace.
The proof uses regular nonamenability and a trace inequality on truncated products of the two cyclic factors.

## A lower bound for two linear left denominators

Write \(F=\langle t_1,t_2\rangle\), which has index four in \(H\) by [adjacent generation](Yin_C_A0272_v1.md#the-order-24-application).
The group \(F\) must be nonamenable.
If it were amenable, so would \(H\) be, and scalar injectivity would make its domain group ring an Ore domain with actual fraction division ring in \(U(H)\).
Eliminating matrices over that division ring gives integral regular ranks, contradicting the assumed rank. [Amenable domain and Ore fractions](Yin_C_A0211_v1.md#right-fractions-for-commensurable-amenable-subgroups)

For two generators \(x,y\) of a nonamenable group and fixed square numerical matrices \(K_1,K_2\), the stacked operator with blocks \(I+xK_1,\ I+yK_2\) on the regular representation is bounded below.
Either generator may be replaced by its inverse.
For suppose unit vectors \(\xi_n\), with finitely many group-space coordinates, have both images tending to zero.
Pass to a subsequence along which the Gram matrices of their coordinates converge.
Their limit is positive with trace one.
The coordinate sequences span a nonzero finite-dimensional limiting inner product space after quotienting by the combinations whose norms tend to zero.
From the defect equations, \(x^{-1}\) and \(y^{-1}\) carry each coordinate sequence to a fixed linear combination of the coordinates up to a norm error tending to zero.
They therefore act isometrically on this finite-dimensional space and act onto it.
Choose an orthonormal basis there lifted to fixed combinations \(f_{1,n},\ldots,f_{k,n}\) of the coordinates.
For either generator inverse \(v\), the tuple \((v f_{j,n})_j\) is a constant unitary change of the tuple \((f_{j,n})_j\) up to a total square error tending to zero.
The positive vectors \(k^{-1/2}(\sum_j|f_{j,n}|^2)^{1/2}\) in the ordinary group space then have norms tending to one and displacement under \(v\) tending to zero, by the pointwise Euclidean norm inequality.
The normalized squares are almost-invariant probability densities in \(\ell^1\), giving an invariant mean by a weak-star cluster point, contrary to nonamenability.
The same lower bound holds after a regular subgroup inclusion by coset decomposition.

For the actual matrix transfer there is a left denominator \(D_L(z)=I+z^\epsilon K\), \(\epsilon\in\{1,-1\}\), such that \(N_L(z)=D_L(z)M(z)\) is a bounded Laurent polynomial on the circle.
If \(D\) is invertible put \(T=D^{-1}C,\ V=A-BT\), which is invertible by the assembled coefficient block.
The [cyclic expansion](Yin_C_A0245_v1.md#two-fourier-blocks-of-the-rational-transfer) is \(M(z)=BD^{-1}+Vz(I+zT)^{-1}D^{-1}\).
Taking \(K=VTV^{-1},\epsilon=1\) clears this denominator on the left.
If \(D\) is singular apply the same construction to \(M(z^{-1})\), using the invertible \(C\).
For \(M^{-1}\) interchange the two pencils, obtaining \(\widetilde D_L,\widetilde N_L\); the assembled block remains invertible after exchanging its two block rows.

The [middle identity](Yin_C_A0280_v1.md#two-factors-in-the-actual-finite-regular-twist) now gives
\[
 \binom{D_L(t_1)}{\widetilde D_L(t_2)}W
       =\binom{N_L(t_1) M(t_0)}
                    {\widetilde N_L(t_2) M(t_3)^{-1}s^4}.
\]
The column on the left of \(W\) has a bounded left inverse by the preceding lower bound.
All circle poles are simple by the [double-pole exclusion](Yin_C_A0300_v1.md#statement).
Each rightmost rational factor on the right therefore has singular-value tail \(O(1/v)\) by cyclic spectral calculus.
Bounded left multiplication and the unitary right translation preserve this upper bound up to constants.
For the sum after applying the bounded left inverse, truncate the two summands at norm \(v\): the discarded parts have combined rank \(O(1/v)\) and the sum of the remaining parts has norm at most \(2v\).
This proves the asserted weak tail.
The inverse \(W^{-1}=s^{-2}Ws^{-2}\) has the same singular-value distribution.

## A fractional moment lower bound detects interacting residues

For bounded matrices \(L,R\) in a finite tracial von Neumann algebra and \(0<p<1\) the Araki–Lieb–Thirring inequality gives
\[
           \operatorname{Tr}|LR|^p
              \ \ge\ \operatorname{Tr}(|L|^p |R^*|^p).
\]
Indeed use the trace inequality for the positive operators \(|L|^{p/2}, |R^*|^{p/2}\) with power \(2/p\) and increasing function \(s\mapsto s^p\).
The polar factors preserve the nonzero singular values. [Kosaki, equations (4)–(5) and Theorem 2](https://doi.org/10.1090/S0002-9939-1992-1065951-1)

First apply this to \(L=M(t_1)\) and \(R=M(t_0)\) with each factor cut by the scalar indicator that its numerical matrix norm is at most \(b\).
The product is an outer compression of \(W\), since within each cyclic algebra the scalar indicator commutes with the matrix.
Its singular values do not exceed those of \(W\).
The cyclic subgroups of \(t_1,t_0\) have trivial intersection by the [periodic-image argument](Yin_C_A0291_v1.md#comparing-two-products-on-their-individual-domains).
Thus the group trace of two bounded scalar functions, one on each subgroup, factors as the product of their Haar integrals.
Apply this entrywise on the right of the trace inequality and send \(b\) to infinity.
Simple poles make the integrals finite at every \(0<p<1\).
With \(dz\) denoting Haar probability one obtains
\[
 \operatorname{Tr}|W|^p
 \ \ge\
 \operatorname{tr}_2\left[
       \left(\int |M(z)|^p\,dz\right)
       \left(\int |M(z)^*|^p\,dz\right)\right].
\]

Let \(S_\alpha\) be the residue of \(M\) at a circle pole \(\alpha\).
Then as \(p\uparrow1\),
\[
 (1-p)\int |M(z)|^p\,dz\longrightarrow
              \pi^{-1}\sum_\alpha |S_\alpha|
\]
and the adjoint version gives the sum of \(|S_\alpha^*|\).
For example on the arc \(z=\alpha e^{ih}\), write \(M(z)=h^{-1}C(h)\) with \(C(h)\) continuous at zero and \(C(0)=(i\alpha)^{-1}S_\alpha\).
The matrix power \(|C(h)|^p\) is continuous jointly for \(p\) near one and \(h\) near zero.
The scalar measures \((1-p)|h|^{-p}dh/(2\pi)\) on a fixed symmetric arc concentrate at zero with limiting mass \(1/\pi\).
The integral away from all poles is bounded uniformly in \(p\), proving the limit.

By the upper tail, \(\operatorname{Tr}|W|^p=O((1-p)^{-1})\) as \(p\uparrow1\), by integrating its distribution.
Multiplying the lower estimate by \((1-p)^2\) shows
\(\sum_{\alpha,\beta}\operatorname{tr}_2(|S_\alpha|\,|S_\beta^*|)=0\).
Each term is nonnegative and it vanishes precisely when the range of \(S_\beta\) is in the kernel of \(S_\alpha\).
Consequently \(S_\alpha S_\beta=0\) for every ordered pair of boundary residues.
Apply the same argument to \(W^{-1}=M(t_0)^{-1}M(t_1)^{-1}\) to get the assertion for the residues of the inverse transfer.

## Counting the poles

Each transfer has at least one genuine circle pole by the [six-fiber obstruction](Yin_C_A0244_v1.md#statement).
If \(M\) had two distinct circle poles, then the determinant of \(Cz+D\) would have two distinct nonzero roots, making \(C,D\) invertible.
The matrix \(T=D^{-1}C\) would have two distinct nonzero eigenvalues.
In the cyclic expansion the ranges of the residues are \(V\) times the two eigenlines of \(T\), since the resolvent residues are nonzero multiples of the associated spectral idempotents and \(D\) is invertible.
They span both coordinates.
A nonzero residue cannot annihilate both ranges.
This contradicts the ordered pair identities.
Interchanging numerator and denominator gives the same conclusion for \(M^{-1}\).
The unique residue on each side squares to zero as already proved.

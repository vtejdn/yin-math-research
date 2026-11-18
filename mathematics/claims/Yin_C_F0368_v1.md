---
author: Yin
---

# Ordinary Wigner determinants for entry laws with logarithmic interval concentration

<a id="statement"></a>
## Matrix and scalar limits

Take the fixed finite-variance colors and arbitrary cross-size couplings of [F0013](../tasks/Yin_T_F0013_v1.md#contract).
Take real symmetric colors or Hermitian colors with independent upper-entry real coordinates in some fixed orthogonal coordinate system in the plane.
Require every independent real coordinate, including every diagonal law, to satisfy
\[
 Q(r)=\sup_a\Pr\{a\le X\le a+r\}
 \le C_A(1+\log(1/r))^{-A},\qquad 0<r<1,\quad A>0. \tag{1}
\]
Here the constant may depend on the coordinate law and on \(A\).
For every fixed square affine pencil, the normalized ordinary log determinant tends almost surely to its finite free value along all dimensions admitting an invertible evaluation in the declared spaces.
The dimension-limsup equals the free log determinant for all pencils, including singular constant terms and the value \(-\infty\).
For every fixed scalar noncommutative polynomial, [F0014](../tasks/Yin_T_F0014_v1.md#contract) holds at every prescribed shift, and its empirical eigenvalue measures have the full-sequence almost-sure weak [Brown limit of F0012](../tasks/Yin_T_F0012_v3.md#contract).
The assertions use the same separate events for fixed polynomials and fixed parameters as the three contracts.
For a single finite-target pencil, a sufficiently large finite exponent \(A\) in (1) suffices for its determinant conclusion.

<a id="argument"></a>
## The loss beyond a polynomial cutoff

Fix the pencil of coefficient size \(m\) with finite target \(u\), and let \(F_N(t)\) count the fraction of its singular values in \([0,t]\).
The [finite-variance count](Yin_C_F0186_v40.md#statement) gives \(\mathbb E F_N(N^{-\gamma})\le C N^{-\gamma\beta}\) with \(\gamma,\beta>0\).
Set \(s=\tfrac12\min(\gamma\beta,\tfrac12)\) and fix \(0<\eta<s\).
Replacing an independent row group changes this counting function by at most \(C_m/N\) for the fixed pencil, with the finitely many colors absorbed in the constant.
The [row concentration bound](Yin_C_F0186_v4.md#row-concentration) therefore gives
\[
 \Pr\{F_N(N^{-\gamma})>N^{-s}\}\le 2\exp(-c N^{1-2s})
\]
for sufficiently large sizes.
The [normalized logarithm clipped below at \(N^{-\gamma}\)](Yin_C_F0186_v40.md#determinant) converges to \(u\) almost surely under each coupling for the two-moment laws.

Fix a good dimension and use \(\varepsilon_N=\exp(-N^\eta)\).
In the independent raw coordinates the squared modulus of the determinant is a nonzero nonnegative real polynomial of degree at most \(2mN\) in at most \(C N^2\) coordinates.
A fixed orthogonal change within a planar atom leaves the degree unchanged.
On the guard \(\max_j\|W_j\|\le\varepsilon_N^{-\theta}\), a least value at most \(\varepsilon_N\) gives a zero within raw coordinate sup distance \(r_N=C\sqrt N\,\varepsilon_N^\kappa\) by the [structured repair](Yin_C_F0186_v38.md#argument), for fixed positive \(\kappa,\theta\).
Rotation of an individual planar block changes the coordinate sup distance by at most \(\sqrt2\), absorbed into \(C\).
The guard fails with probability at most \(CN\varepsilon_N^{2\theta}\) by the second moments.
Apply the [quantile-grid tube bound](../ledger/Yin_L_F0061_v5.md#tube) with its [dimension and degree dependence](../ledger/Yin_L_F0061_v5.md#box-count).
Since \(\log(1/r_N)\ge(\kappa/2)N^\eta\) eventually, this gives
\[
 \Pr\{s_{\min}\le e^{-N^\eta}\}
 \le C N e^{-2\theta N^\eta}+C_A N^{5-A\eta}.
\]
Take \(A>6/\eta\) to get a summable series.
Outside these and the counting exceptions, the entire normalized logarithmic loss below \(N^{-\gamma}\) is at most \(N^\eta F_N(N^{-\gamma})\le N^{\eta-s}\).
This proves the asserted convergence on good sizes by first Borel-Cantelli.
There are [good dimensions of every sufficiently large even size](Yin_C_F0186_v38.md#log-assembly), and the determinant is identically zero whenever no witness exists.
For \(u=-\infty\) the upper bounds by fixed clipped logarithms tend to \(-\infty\) through all sizes.

The [word-chain identity](Yin_C_F0186_v40.md#scalar) transfers finite and free logarithms with the same auxiliary-size factor, including at \(z=P(0)\).
For nonconstant \(P\) the free scalar logarithm is finite, and for \(z\ne P(0)\) the zero tuple provides a witness in every size.
For each fixed coupling Fubini gives almost-everywhere convergence in the spectral plane on one event of probability one.
The [pathwise planar square bound and tightness](Yin_C_F0186_v4.md#noncompact-planar) then give local \(L^1\) convergence and weak convergence to the Brown measure by taking distributional Laplacians.
Constant polynomials give the conclusion directly.

<a id="example"></a>
## A law supported on a set of Hausdorff dimension zero

Start with \([0,1]\), and at level \(j\ge1\) keep the two closed intervals of length \(\ell_j=3^{-j^2}\) at the ends of each retained parent.
Give each child half of its parent's mass.
The \(2^j\) level-\(j\) intervals are separated by gaps at least \(\ell_j\), since \(\ell_{j-1}\ge3\ell_j\) with \(\ell_0=1\).
If \(\ell_{j+1}<r\le\ell_j\), any interval of length \(r\) meets at most two such intervals up to endpoints, so \(Q(r)\le 2^{1-j}\).
Since \(\log(1/r)\le(j+1)^2\log 3\), this gives (1) at every exponent.
Each level-\(j\) interval has mass \(2^{-j}\), so no bound \(Q(r)\le C r^\alpha\) with \(\alpha>0\) can hold.
The covering sums \(2^j\ell_j^\alpha\to0\) for all \(\alpha>0\), proving the dimension assertion.
The law is bounded and nondegenerate, and centering and variance normalization preserve (1) and the failure of every positive power bound.
Independent copies in the real upper entries and diagonals therefore give all three conclusions under this singular continuous law.

## Current assessment
[Selected decision](#decision-log-concentration-reviewed)

## Assessment history

### Decision log-concentration-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-18T11:29 |
| status | open |
| reason | The stretched-exponential least-value estimate and the finite-variance count give a candidate argument for the three stated limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Determinant and Brown limits](#statement) | All three finite-variance contracts within the stated coordinate class. |
| argument | [Rare very small singular values](#argument) | Summable loss on good dimensions and almost-sure weak Brown convergence. |
| support | [Dimension-zero example](#example) | A law with all inverse logarithmic concentration rates and no positive power rate. |
| dependency | [Quantile grids](../ledger/Yin_L_F0061_v5.md#box-count) | Degree-linear tube bound in independent scalar coordinates. |

### Decision log-concentration-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-18T11:36 |
| status | proved |
| reason | Independent whole-proof review verifies the algebraic grid estimate, the singular-value count and the good-dimension and planar conclusions, including the dimension-zero example. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Finite-variance limits](#statement) | Independent real coordinates with logarithmic interval concentration. |
| argument | [Stretched-exponential floor and counting](#argument) | Summable lower-tail failures, vanishing normalized loss and the determinant and Brown limits. |
| support | [Zero-dimensional support](#example) | Explicit input law outside every positive power interval concentration class. |
| dependency | [Quantile grid](../ledger/Yin_L_F0061_v5.md#box-count) | Coefficient-independent estimate with linear dependence on degree and quadratic dependence on dimension. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0376_v1.md#log-concentration-whole-proof) | Full argument, grid construction, affine component bound, exceptional dimensions and planar transfer. |

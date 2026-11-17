---
author: Yin
---

# Rademacher support witnesses for arbitrary full affine pencils

<a id="statement"></a>
## Symmetric sign evaluations in even dimensions

Let \(L=b+\sum_{j=1}^g A_jx_j\) be any fixed square full affine matrix over the complex free polynomial algebra, of coefficient size \(m\).
There is an even \(r\ge2\) such that for every sufficiently large odd prime \(p\), \(N=rp\) admits real symmetric sign matrices \(W_1,\ldots,W_g\) with entries \(\pm N^{-1/2}\), including the diagonals, for which \(L(W_1,\ldots,W_g)\) is invertible.
In fact any fixed even \(r\) which admits an invertible real symmetric evaluation with unrestricted real entries suffices.
The coefficients of \(L\) may be arbitrary complex numbers.
Conversely a nonfull polynomial matrix has singular evaluations in every dimension.
The same existence conclusion applies to \(P(W)-zI\) for every nonconstant scalar polynomial \(P\) and prescribed complex \(z\), including \(P(0)\).

In the sign product law of [F0013](../tasks/Yin_T_F0013_v1.md#input-model), each tuple of such matrices is an actual support point.
The proof produces nonsingularity with probability tending to one under a different sign sampling law supported on block circulants, and therefore gives positive probability of nonsingularity for the ordinary independent signs at those sizes.
It gives no probability tending to one or logarithmic lower bound under that ordinary law.

<a id="argument"></a>
## Block-circulant choices on the sign support

Fullness gives a finite semicircular logarithm by the [free power bound at zero background](Yin_C_F0352_v1.md#statement).
Hence the [real witness theorem](Yin_C_F0186_v9.md#all-even-witness) gives unrestricted real symmetric witnesses in all sufficiently large even dimensions.
Fix one such \(r\).
The polynomial
\[
 (T_1,\ldots,T_g)\longmapsto\det L(T_1,\ldots,T_g)
 \quad (T_j\text{ of size }r)
\]
is nonzero on real symmetric tuples and therefore also on Hermitian tuples, since these contain the real evaluations.

In size \(rp\) divide the sites into \(r\) classes, each indexed by \(\mathbb Z/p\mathbb Z\).
For each color \(j\) and distinct classes \(a<b\), choose \(p\) independent uniform signs \(\epsilon^{j,ab}_h,\ h\in\mathbb Z/p\mathbb Z\).
Fill the block at \(((a,s),(b,t))\) with \(\epsilon^{j,ab}_{t-s}/\sqrt{rp}\), and transpose that block at \((b,a)\).
For a diagonal block \(a=a\) choose independent signs for \(h=0,1,\ldots,(p-1)/2\) and set \(\epsilon^{j,aa}_{-h}=\epsilon^{j,aa}_h\).
Use the same difference formula on the block.
The sign families for different class pairs and different colors are independent.
Every resulting matrix is allowed on the symmetric sign cube.
The dependence between repeated entries in a block belongs only to this witness construction.

Let \(\omega=\exp(2\pi i/p)\).
Fourier characters in the class coordinates decompose the full evaluation into \(p\) affine evaluations of physical size \(r\).
For each color the Hermitian fiber \(T_j(k)\), \(k\in\mathbb Z/p\mathbb Z\), has strict upper entries
\[
 (rp)^{-1/2}\sum_{h=0}^{p-1}\epsilon^{j,ab}_h\,\omega^{kh}
\]
and real diagonal entries
\[
 (rp)^{-1/2}\left(\epsilon^{j,aa}_0+
     2\sum_{h=1}^{(p-1)/2}\epsilon^{j,aa}_h\cos(2\pi kh/p)\right).
\]
The lower entries are conjugate to the upper entries.
The full evaluation is invertible if and only if all \(p\) pencils \(L(T_1(k),\ldots,T_g(k))\) are invertible.

<a id="fiber-limits"></a>
## Zero and nonzero frequency limits

At \(k=0\) the strict upper entries have variance \(1/r\) and the diagonals have variance \((2p-1)/(rp)\).
At a nonzero \(k\), strict upper real and imaginary parts have equal variance \(1/(2r)\) and zero covariance, since \(\sum_h\omega^{2kh}=0\).
The diagonal variance is \((p-1)/(rp)\), by the same identity and the equal cosine squares at opposite residues.
At each \(p\) all nonzero frequencies have exactly the same marginal tuple law by permutation of residues and of opposite pairs.
Each scalar summand has coefficient of modulus at most \(2/\sqrt{rp}\).
For any real linear combination of the finitely many real coordinates, the characteristic function is a product of cosines.
Its logarithm converges to minus half the limiting variance times the squared Fourier parameter, since the sum of the fourth powers of the coefficients tends to zero and their squares sum to the indicated variance.
Consequently the zero-frequency tuple converges in law to independent normalized \(\mathrm{GOE}_r\) matrices, and every nonzero-frequency marginal converges to independent normalized \(\mathrm{GUE}_r\) matrices.
In each case the joint law of the independent matrix coordinates in the limit has a density on its declared real vector space.
The complex determinant polynomial is nonzero there, so its zero set has measure zero, by applying the one-variable root bound successively to a nonzero real or imaginary part.
Closed-set upper semicontinuity of probabilities now gives marginal singularity probabilities \(o(1)\) of the two types as \(p\to\infty\).
A union bound over all \(p\) frequencies based just on these marginal limits would lack a rate.

<a id="galois-orbits"></a>
## Only a bounded number of singularity tests is needed

Take the subfield \(K\subset\mathbb C\) generated over \(\mathbb Q\) by the finitely many coefficients and \(\sqrt r\).
Choose a transcendence basis within a finite generating set; \(K\) has finite degree \(d\) over the resulting purely transcendental field \(F\).
The prime cyclotomic polynomial \(1+X+\cdots+X^{p-1}\) is irreducible over \(\mathbb Q\) by Eisenstein after translation.
It remains irreducible over \(F\), since adjoining independent indeterminates preserves irreducibility by Gauss's lemma.
Thus \([F(\omega):F]=p-1\).
For \(K_p=K(\sqrt p)\) the tower law and the inclusion \(F(\omega)\subset K_p(\omega)\) give
\[
 [K_p(\omega):K_p]\ \ge\ (p-1)/[K_p:F]\ \ge\ (p-1)/(2d).
\]
The extension is the splitting field of \(X^p-1\), so its Galois group has this degree and acts faithfully by \(\omega\mapsto\omega^u\) for a subgroup of \((\mathbb Z/p\mathbb Z)^\times\).
It acts freely on the \(p-1\) nonzero frequencies by \(k\mapsto uk\); there are at most \(2d\) orbits.

For every fixed sign assignment the automorphism fixes all signs, \(b,A_j\) and the normalization \(1/\sqrt{rp}\).
It sends the complete fiber determinant at \(k\) to the fiber determinant at \(uk\), including lower entries from the opposite powers of \(\omega\).
Vanishing is consequently constant on each orbit, without any independence assumption between the fibers.
Taking one representative from each orbit as well as the zero-frequency fiber gives probability of any singular fiber bounded by the zero-frequency failure plus \(2d\) times the common nonzero-frequency failure.
This tends to zero and proves existence on the original sign support.
For a nonfull pencil a factorization through fewer columns forces a positive kernel dimension in every evaluation.
For the scalar assertion, the [word-chain linearization](../ledger/Yin_L_F0061_v2.md#linearization-transfer) of \(P-z\) has a unit upper triangular auxiliary pivot and is full because its scalar Schur complement is a nonzero free polynomial.
Its finite evaluations are invertible exactly when \(P(W)-zI\) is invertible at the same matrices.

The constructed event tests exact zeros rather than small nonzero determinants.
Galois conjugacy preserves vanishing but supplies no equality between the complex absolute values at the different frequencies.
Even under the witness sampling law this argument alone does not control the sum of their negative logarithms.

## Current assessment
[Selected decision](#decision-sign-support-reviewed)

## Assessment history

### Decision sign-support-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T12:57 |
| status | open |
| reason | A Fourier decomposition of a real symmetric sign construction and finitely many Galois orbit tests give exact nonsingularity witnesses for arbitrary full coefficients. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Sign support in even sizes](#statement) | Every full complex affine pencil and fixed scalar word-chain shift, with arbitrary complex coefficients. |
| argument | [Symmetric circulant blocks](#argument) | Genuine normalized sign matrices and their Fourier fibers. |
| support | [Fiber laws](#fiber-limits) | GOE and GUE limits at fixed base dimension and their nonsingular evaluations. |
| support | [Cyclotomic orbits](#galois-orbits) | Uniform bound on the number of tests, using only finite generation of the coefficient field. |

### Decision sign-support-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T13:03 |
| status | proved |
| reason | Fourier-fiber convergence and the bounded number of cyclotomic orbits give invertible support points in the stated even dimensions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full affine pencils on the sign cube](#statement) | The fixed statement with the specified laws, dimensions and coupling quantifiers. |
| argument | [Complete argument](#argument) | Fourier-fiber convergence and the bounded number of cyclotomic orbits give invertible support points in the stated even dimensions. |
| support | [Fourier fibers](#fiber-limits) | Covariances and marginal singularity probabilities in the circulant construction. |
| support | [Cyclotomic orbits](#galois-orbits) | Vanishing of all fiber determinants and the scope of the support conclusion. |
| review | [Independent whole-proof review](../audits/reviews/Yin_R_F0362_v1.md#sign-support-whole-proof) | Hypotheses, conclusions, proof and directly used mathematical interfaces. |

---
author: Yin
---

# A universal finite list of rational trace parameters in the sofic order-twenty case

## Statement

Under the [normalized order-twenty exceptional hypotheses](Yin_C_A0342_v1.md#statement) suppose \(H\) is sofic and the two-square rectangle has nullity \(1/2\).
Write the ordinary trace parameter as \(d=\operatorname{tr}(M(0)M(\infty))\).
Then \(d=a/b\in\mathbb Q\) in lowest terms with \(b>0\), and
\[
                       \max(|a|,b)\le 60^4=12960000 .
\]
This bound is independent of \(H\), its relations, the sofic approximation, and all complex coefficient entries of the input.
The degenerate parameters \(1/2,2,5/2\) and the open interval \((2,5/2)\) are excluded, and the [two strict spectral radius inequalities](Yin_C_A0340_v1.md#statement) still apply.
Among the finitely many rationals left by these restrictions, at most one value can support a half kernel for each fixed ordered normalized marking.
The estimate is a necessary height bound and does not assert realization.

## Rationality on fixed ordered marks

The [arithmetic reduction](Yin_C_A0340_v1.md#coefficient-embeddings-at-a-half-kernel) makes \(d\) algebraic and transfers a half kernel to every conjugate of \(d\) on the same group by coefficient-field rank independence.
The normalized prototype sign may change under the embedding.
The [eight-dimensional Clifford pencil](Yin_C_A0342_v1.md#a-linear-pencil-on-eight-coordinates) gives the same nullity for either sign using the actual character on \(h\).
All conjugates are therefore parameters for the fixed ordered marks and the same sign.
Their nullities, each equal to \(1/2\), have [sum at most \(1/2\)](Yin_C_A0342_v1.md#the-generalized-zero-space-at-infinity).
There can be only one algebraic conjugate, so \(d\) is rational.

## Finite permutations at two parameters

Use the eight-square Clifford pencil
\[
   K(z)=\sum_{j=0}^2
      \big(\varepsilon_j+\iota_{G(z)(e_j,\cdot)}\big)h^j
      -g(h^2-s_0 h+2)I_8,\qquad s_0=\pm\sqrt5 ,
\]
where \(G(z)\) is the [numerator Gram matrix](Yin_C_A0342_v1.md#a-linear-pencil-on-eight-coordinates).
Let \(n\) run through the sizes of a sofic approximation.
Using its permutation matrices for the two generators gives an \(8n\)-square linear polynomial \(B_n(z)=2K_n(z)\) over \(\mathbb Z[\sqrt5]\).
The factor two clears the half-integers in the Gram matrix.
Use the indicated products of the two permutation matrices for each word.
Local convergence implies convergence of all normalized moments of \(B_n(x)^*B_n(x)\) to the corresponding regular moments for each fixed real \(x\), with normalization \(1/n\) on the site coordinates.
Indeed each such moment is a fixed finite sum of word traces, and in the sofic approximation the normalized fixed-point count converges to its regular value.
The spectra are uniformly bounded for fixed \(x\) by the finite coefficient norm, giving weak convergence of the singular-value distributions as well.

At \(x=2\) the [degenerate Clifford pencil](Yin_C_A0342_v1.md#full-rank-at-a-degenerate-gram-matrix) is injective.
Consequently \(\operatorname{rank} B_n(2)=8n-o(n)\) by weak convergence at zero.
At \(x=a/b\) the regular kernel dimension of \(K(x)\) is two, four times the given half kernel.
Here the finite normalized kernel dimensions converge to two.
For detail, take \(C_n=bB_n(a/b)\), an algebraic integer matrix in this real quadratic field.
Both real embeddings of \(C_n\) have norm bounded by a constant depending only on this fixed rational value and its denominator.
The product of the nonzero eigenvalues of \(C_n^*C_n\) is, up to sign, the lowest nonzero characteristic coefficient, an algebraic integer.
Its field conjugate is the same coefficient of the conjugate positive matrix and is bounded in modulus by \(\max(1,\|\overline C_n\|^2)^{8n}\), where the bar here denotes the other real embedding.
Indeed the first nonzero characteristic coefficient is the product of the nonzero eigenvalues for that conjugate matrix too, as both ranks are preserved by the field automorphism.
The absolute field norm is a nonzero integer, so the product in the original embedding is at least \(\exp(-O(n))\).
The uniform norm bound in the original embedding now gives at most \(O(n)/|\log\epsilon|\) singular values in \((0,\epsilon)\) for \(0<\epsilon<1\).
Weak convergence and this bound give convergence of the atoms at zero by taking positive continuity points down to zero.
Therefore \(\operatorname{rank} B_n(a/b)=6n+o(n)\).
This finite matrix argument permits any fixed height of \(a/b\) when proving convergence; its constants do not enter the height estimate below.

## An integral minor and its Mahler measure

Take a minor \(f_n(z)\) of \(B_n(z)\) of size \(m_n=\operatorname{rank}B_n(2)\), nonzero at two.
Its matrix loses at least \(\ell_n=\max(0,m_n-\operatorname{rank}B_n(a/b))=2n+o(n)\) dimensions at \(a/b\).
Constant row operations over the number field can put \(\ell_n\) evaluated rows equal to zero, so this determinant polynomial has a zero of multiplicity at least \(\ell_n\).
The nonzero polynomial \(D_n=f_n\,\overline f_n\) has ordinary integer coefficients, as it is fixed by field conjugation and has algebraic integer coefficients.
Its zero at the rational \(a/b\) has multiplicity at least \(2\ell_n\).
Gauss's lemma implies that the primitive polynomial \((bz-a)^{2\ell_n}\) divides \(D_n\) in \(\mathbb Z[z]\).

On \(|z|=1\) both coefficient embeddings have \(\|B_n(z)\|<60\).
In the orthonormal exterior basis each \(\varepsilon_j\) has norm one and each contraction has norm equal to the Euclidean length of its covector.
For the first and third rows of \(G(z)\) these lengths are at most \(\sqrt{4+45/4+1}\); for the middle row use \(\sqrt{144+45/2}\).
The two permutations are unitary, and \(\|h_n^2-s_0 h_n+2I\|\le3+\sqrt5\).
Hence
\[
  \|B_n(z)\|\le
  2\left(3+2\sqrt{4+45/4+1}+\sqrt{144+45/2}+3+\sqrt5\right)<60 .
\]
The same bound holds for each square submatrix as a compression between coordinate subspaces.
Thus \(|D_n(z)|\le 60^{2m_n}\) on the circle.
The Mahler measure of any nonzero integral polynomial is at least one, since its absolute leading coefficient is at least one and its remaining factors have measure at least one after making them monic.
Multiplicativity and the linear factor formula give
\[
             \max(|a|,b)^{2\ell_n}\le {\cal M}(D_n)\le60^{2m_n}.
\]
As \(m_n/n\to8\) and \(\ell_n/n\to2\), this yields the uniform bound claimed.

## Assessment history

### Decision a-uniform-rational-height-bound

| Field | Value |
| --- | --- |
| date | 2026-11-26T18:25 |
| status | proved |
| reason | The Galois orbit bound and integral polynomial minors give a group-independent finite list. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The Galois orbit bound and integral polynomial minors give a group-independent finite list. |
| argument | [Rationality on fixed ordered marks](#rationality-on-fixed-ordered-marks) | Rationality on fixed ordered marks. |
| argument | [Finite permutations at two parameters](#finite-permutations-at-two-parameters) | Finite permutations at two parameters. |
| argument | [An integral minor and its Mahler measure](#an-integral-minor-and-its-mahler-measure) | An integral minor and its Mahler measure. |
| dependency | [Earlier result, version 1](Yin_C_A0340_v1.md#statement) | The regular moments force a Brown atom at minus one and yield an algebraic coefficient obstruction for sofic groups. |
| review | [An injective determinant-zero witness and coefficient embeddings](../audits/reviews/Yin_R_A0234_v1.md#an-injective-determinant-zero-witness-and-coefficient-embeddings) | Independent inspection of the preceding version. |
| review | [A uniform rational height bound](../audits/reviews/Yin_R_A0234_v1.md#a-uniform-rational-height-bound) | Independent review of the fixed proof. |

## Current assessment

[Selected decision](#decision-a-uniform-rational-height-bound)

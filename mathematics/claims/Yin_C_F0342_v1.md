---
author: Yin
---

# A signed Cauchy Gram inequality equivalent to the normal converse on lattice labels

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Take the [finite lattice data](Yin_C_F0339_v1.md#statement) with \(n\) nonzero labels, masses \(t_i\), mesh \(h\), actual partial liberation \(\gamma\), Cauchy matrix \(k_{ij}=1/(c_i-c_j)\) for \(i\ne j,\ k_{ii}=0\), marginal Cauchy sums \(H_i=\sum_j t_j k_{ij}\), maximal densities \(M_i\) and budget \(B_c\).
Write \(C_0=\mathrm{id}\otimes\tau,\ \zeta=(i\gamma)^*(1\otimes1)=\zeta^*\), and \(\nu_{ij}=\|e_i\zeta e_j\|_2^2\).
For the analytic unitaries \(u=a\pm i\sqrt{1-a^2}\) with \(a\) any strict selfadjoint contraction of the represented finite-label word algebra, set
\[
 G_{ij}=C_0 I_{e_i\otimes e_j}\gamma(u),\qquad
 f_{ij}=\operatorname{Re}\langle u,G_{ij}\rangle,\qquad
 F_q(u)=\sum_{ij}q_{ij} f_{ij}\quad(q\text{ real}).
\]
Here \(f_{ij}=f_{ji}\) and \(f_{ii}=0\), without any mass normalization in \(f_{ij}\).
Consider the real positive semidefinite Gram matrix and its scalar budget
\[
     K_{ij}=\operatorname{Re}\sum_\ell t_\ell k_{\ell i}\overline{k_{\ell j}},
     \qquad Q_c=\sum_{ij}|k_{ij}|^2\nu_{ij}+\sum_i t_i|H_i|^2.
\]
Thus \(Q_c\le B_c^2\).
For a real antisymmetric matrix \(b\) put \(m_i(b)=\sum_j t_j b_{ij}\),
\(G_b=\sum_{ij}b_{ij}G_{ij}\) and
\[
              A_b=\sum_{ij}b_{ij}e_j\zeta e_i+i\sum_i m_i(b)e_i.
\]
Then
\[
  \sum_{b\in(\operatorname{Re}k,\operatorname{Im}k)}
                    \|iG_b-uA_b\|_2^2=Q_c-F_K(u),\qquad
  \sum_{b\in(\operatorname{Re}k,\operatorname{Im}k)}\|A_b\|_2^2=Q_c.    \tag{1}
\]
The sum takes the two components with multiplicity.
In particular \(F_K(u)\le Q_c\) unconditionally.

Let \(d_{\rm G}\) be the supremum of \((-F_K(u))_+/B_c^2\) over the indicated data and analytic tests, and let \(K_{\rm lat}\) be the supremum of the original single-input right slice norm divided by \(B_c\) on the entire polynomial unit ball.
Then, in the extended nonnegative reals,
\[
       d_{\rm G}\le (K_{\rm lat}+1)^2,\qquad
       K_{\rm lat}\le 2\sqrt2\,\big(1+\sqrt{1+d_{\rm G}}\big).           \tag{2}
\]
Hence the unrestricted normal implication \(\mathsf A\Rightarrow\mathsf S\) is equivalent to a uniform lower bound \(F_K(u)\ge -C B_c^2\) for this single positive semidefinite kernel on each lattice model.
For \(n\ge2\) fixed one always has \(\|C_0 d_c p\|_2\le C\sqrt{n-1}\, B_c\|p\|\) with an absolute constant, for arbitrary placements, masses and correlations.
For \(n=1\) the discrete derivative vanishes.
The existence of a bound independent of \(n\) remains open.

## Argument

### Polarizing the rank-one energy

Each \(G_{ij}\) ends in \(e_i\), by the definition of inner insertion.
Both \(G_{ii}=0\) and \(e_i\zeta e_i=0\): the diagonal insertion annihilates all generator values, and the end corrections in the vacuum pairing on \(e_i p e_i\) cancel. [Finite-label calculation](Yin_C_F0339_v1.md#free-noise-in-each-spectral-corner)
Selfadjointness of \(\zeta\) gives \(\nu_{ij}=\nu_{ji}\).
Define \(V_{ij}=iG_{ij}-u e_j\zeta e_i\), again ending in \(e_i\).

For real \(x_i\) set \(x=\sum_i x_i e_i\) and \(q=x\otimes x\).
The finite symmetric-kernel energy identity gives
\[
\begin{split}
 \sum_i x_i^2\left\|\sum_j x_j V_{ij}\right\|_2^2
  ={}&\sum_{ij}x_i^2x_j^2\nu_{ij}
    -\left(\sum_i t_i x_i^2\right)\sum_{ij}x_i x_j f_{ij}\\
   &+2\left(\sum_\ell t_\ell x_\ell\right)\sum_{ij}x_i^2x_j f_{ij}.     \tag{3}
\end{split}
\]
Indeed the actual vacuum after inserting \(q\) in \(i\gamma\) is \(x\zeta x\) because the two marginal corrections agree.
The row of \(q\) is \((\tau x)x\), and \(q\circ q=\|x\|_2^2q\).
In the [uncentered square identity](Yin_C_F0331_v1.md#the-uncentered-square), the norm on the left of (3) is the squared norm of \(i\sum x_ix_jG_{ij}-ux\zeta x\), split by its right supports.
The last term is obtained from \(\operatorname{Im}\tau(xu^*i\sum x_i x_jG_{ij})\), with the extra factor \(x_i\) from the right support.
All the kernel factors belong to the represented word algebra and the derivation agrees with the inner difference on \(D\).
The proof of the [finite-kernel formulas (B0a) to (B0e)](Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) uses just these algebraic assignments, their actual adjoints and first-derivative limits on the analytic tests.
These ingredients are present for the finite partition, with no diffuse spectral hypothesis.
In particular the scalar adjoint correction for \(x\zeta x\) follows directly by expanding the double trace of \(i\gamma(x p x)\).
The end contributions from differentiating \(x\) cancel by traciality.
Norm-convergent polynomial sums for the square root also converge after each of the first-derivative expressions used in the identity, by the \(j\|a\|^{j-1}\) product bound.

Compare coefficients of the real polynomial in \((x_i)\) in (3).
For \(i\ne j\) the \(x_i^3x_j\) coefficient on the left is zero by \(V_{ii}=0\).
On the right it is \(-t_i(f_{ij}+f_{ji})+2t_if_{ij}\), proving \(f_{ij}=f_{ji}\).
This asserts equality of the real pairings of the two ordered slices.
The coefficient of \(x_i^2 x_j^2\) then gives
\[
      \|V_{ij}\|_2^2+\|V_{ji}\|_2^2
               =2\nu_{ij}+2(t_i+t_j)f_{ij}.                             \tag{4}
\]
For three distinct indices the \(x_i^2x_jx_\ell\) coefficient gives
\[
 \operatorname{Re}\langle V_{ij},V_{i\ell}\rangle
                  =-t_i f_{j\ell}+t_\ell f_{ij}+t_j f_{i\ell}.           \tag{5}
\]
In particular the two ordered squared norms in (4) enter together.

### The Cauchy Gram identity

Let \(b\) be any real antisymmetric matrix.
The diagonal-in-\(j\) part of \(\sum_i\|\sum_j b_{ij}V_{ij}\|_2^2\), by (4) and \(b_{ij}^2=b_{ji}^2\), is
\(\sum_{ij}b_{ij}^2\nu_{ij}+2\sum_{ij}t_j b_{ij}^2 f_{ij}\).
By (5) the off-diagonal part is
\[
     -\sum_{i,j,\ell}t_i b_{ij}b_{i\ell} f_{j\ell}
          +2\sum_{ij}b_{ij}\big(m_i(b)-t_j b_{ij}\big) f_{ij}.
\]
In the first sum the omitted coincidences vanish because \(b_{ii}=f_{jj}=0\).
Adding the two parts cancels their \(t_j b_{ij}^2 f_{ij}\) contributions.
Within the \(i\)th right support,
\(\operatorname{Re}\langle V_{ij},i u e_i\rangle=f_{ij}\), as \(e_j\zeta e_i\) has zero trace there for \(j\ne i\).
Subtracting \(i m_i(b)u e_i\) from \(\sum_j b_{ij}V_{ij}\) cancels the remaining \(2\sum b_{ij}m_i(b) f_{ij}\) and adds \(\sum_i t_i m_i(b)^2\).
This proves
\[
 \|iG_b-uA_b\|_2^2
    =\sum_{ij} b_{ij}^2\nu_{ij}+\sum_i t_i m_i(b)^2
               -\sum_{j,\ell} f_{j\ell}\sum_i t_i b_{ij}b_{i\ell}.
\]
All the \(e_j\zeta e_i\), \(i\ne j\), are orthogonal to the label diagonal and mutually orthogonal for distinct ordered pairs.
The first two terms are exactly \(\|A_b\|_2^2\).
Adding the real and imaginary Cauchy components gives (1).
For real scalars \(y_i\), the quadratic form of \(K\) is \(\sum_\ell t_\ell|\sum_i k_{\ell i}y_i|^2\ge0\).

If \(F_K(u)\ge-d_{\rm G} B_c^2\), the Hilbert direct-sum triangle inequality applied to (1) yields
\[
 \big(\|G_{\operatorname{Re}k}\|_2^2+\|G_{\operatorname{Im}k}\|_2^2\big)^{1/2}
                   \le (1+\sqrt{1+d_{\rm G}})\,B_c .
\]
The original slice on \(u\) is \(G_{\operatorname{Re}k}+iG_{\operatorname{Im}k}\), of norm at most \(\sqrt2\) times this bound.
Averaging the two analytic signs gives the same bound for a strict selfadjoint contraction.
Scalar dilation includes all selfadjoint contractions, and taking real and imaginary parts costs a further factor at most two on the full polynomial unit ball.

Conversely, a bound \(K_{\rm lat}B_c\) on this ball holds also at the analytic unitaries, by polynomial approximation of the binomial series in operator norm and in the finite insertion graph.
Reflecting all labels \(c_i\mapsto\bar c_i\) preserves the lattice class and \(B_c\), and replaces \(k\) by \(\bar k\) on the same word algebra and liberation.
The parallelogram identity applied to the original and reflected right slices gives
\(\|G_{\operatorname{Re}k}\|_2^2+\|G_{\operatorname{Im}k}\|_2^2\le K_{\rm lat}^2 B_c^2\).
The triangle inequality in (1) yields the first inequality of (2).
The [lattice equivalence](Yin_C_F0339_v1.md#statement) then gives the asserted criterion on general normal tuples.
This passage uses both label orientations within the supremum and the original represented tests.

### A bound at a fixed number of labels

Let \(Y_{ij}^2=\|G_{ij}\|_2^2+\|G_{ji}\|_2^2\) for \(i\ne j\).
Expanding (4) cancels the two vacuum squares and yields
\[
  Y_{ij}^2\le 2\sqrt{2\nu_{ij}}\,Y_{ij}+2(t_i+t_j)|f_{ij}|.
\]
The equality of the real pairings and the two right supports give
\(|f_{ij}|\le\sqrt{\min(t_i,t_j)}Y_{ij}\).
This yields \(Y_{ij}^2\le C(\nu_{ij}+t_it_j(t_i+t_j))\), also when \(Y_{ij}=0\).
Cauchy to Schwarz on the at most \(n-1\) nonzero terms per output support gives
\[
 \|C_0d_c(u)\|_2^2
 \le(n-1)\sum_{i<j}|k_{ij}|^2Y_{ij}^2 .
\]
The scalar contribution is bounded by
\[
 \sum_i t_i^2\sum_{j\ne i}\frac{t_j}{|c_i-c_j|^2}
          \le \frac{C}{h}\sum_i t_i^2 M_i
          \le C\sum_i t_i M_i^2.
\]
Indeed the annulus \(2^\ell h\le|c_i-c_j|<2^{\ell+1}h\) contributes at most \(2^{1-\ell}M_i/h\) to the inner sum, and \(M_i\ge t_i/h\).
The vacuum contribution is part of \(Q_c\).
Passing from the analytic tests to the full unit ball as above gives the fixed-\(n\) assertion.
When \(n=1\) the defining Cauchy matrix is zero.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:24 |
| status | open |
| reason | Fix the exact polarized finite-label energy, its equivalent signed Gram lower bound and the uniform estimate at a fixed number of labels for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact Cauchy Gram identity, two-sided comparison of the supremums and the explicit fixed-label upper bound. |
| argument | [Argument](#argument) | Polynomial coefficient comparison, two real antisymmetric orientations, scalar correction, reflection and support estimate. |
| dependency | [Lattice reduction](Yin_C_F0339_v1.md#statement) | Finite-label budget, original polynomial test and equivalence to the general normal converse. |
| dependency | [Diagonal labels](Yin_C_F0339_v1.md#free-noise-in-each-spectral-corner) | Vanishing diagonal insertions and diagonal liberation-vacuum blocks at atomic labels. |
| dependency | [Uncentered rank-one formula](Yin_C_F0331_v1.md#the-uncentered-square) | Real rank-one energy before estimation, with row term and composition weight. |
| dependency | [Finite-kernel iteration](Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) | Actual adjoint and finite tensor formulas on the represented core, first-derivative passage at both analytic signs. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:28 |
| status | proved |
| reason | R_F0347 checked the three coefficient identities, reflection and the analytic-test passage, the two-sided equivalence with the unrestricted lattice problem, the square-root label bound and all four declared dependencies. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact Cauchy Gram identity, two-sided comparison of the supremums and the explicit fixed-label upper bound. |
| argument | [Argument](#argument) | Polynomial coefficient comparison, two real antisymmetric orientations, scalar correction, reflection and support estimate. |
| dependency | [Lattice reduction](Yin_C_F0339_v1.md#statement) | Finite-label budget, original polynomial test and equivalence to the general normal converse. |
| dependency | [Diagonal labels](Yin_C_F0339_v1.md#free-noise-in-each-spectral-corner) | Vanishing diagonal insertions and diagonal liberation-vacuum blocks at atomic labels. |
| dependency | [Uncentered rank-one formula](Yin_C_F0331_v1.md#the-uncentered-square) | Real rank-one energy before estimation, with row term and composition weight. |
| dependency | [Finite-kernel iteration](Yin_C_F0077_v1.md#uniform-row-l2-bounds-close-the-kernel-composition-hierarchy) | Actual adjoint and finite tensor formulas on the represented core, first-derivative passage at both analytic signs. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0347_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

---
author: Yin
---

# Recovering a normal conjugate variable from its marginal and its liberation gradient

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\) be a finite generating tuple of bounded normal elements in a finite von Neumann algebra with faithful normal probability trace \(\tau\).
Write \(P=\mathbb C\langle X,X^*\rangle\), \(H=L^2(M,\tau)\), and assume the marginal spectral measures are diffuse.
Fix \(Z=X_i\) with law \(\mu\), and put \(N=W^*(Z)\).
On the represented core consider partial liberation \(\gamma\), prescribed by \(\gamma(a)=a\otimes1-1\otimes a\) on marginal polynomials in \(Z,Z^*\) and by zero on all other starred generators.
Use the outer bimodule actions and inner products linear in the second argument.
If \(\eta=\gamma^*(1\otimes1)\) exists, let \(\nu_\eta\) be its joint spectral measure for left and right multiplication by \(Z\) on \(H\).
Write \(S_f\) for this left and right spectral calculus, so \(S_{a(z)b(w)}v=a(Z)v b(Z)\).

A distinguished actual ACSY derivation \(\delta\) with \(\delta X_j=\delta_{ij}1\otimes1\) and \(\xi=\delta^*(1\otimes1)\) exists if and only if the following three conditions hold.

1. The scalar divided difference on \(\mathbb C[Z,Z^*]\) has an actual vacuum \(\xi_N\in L^2(N)\).
2. The prescription for \(\gamma\) descends to \(P\) and has the actual \(L^2\) vacuum \(\eta\).
3. The inverse squared spectral gap is integrable:
   \[
         \int_{z\ne w}|z-w|^{-2}\,d\nu_\eta(z,w)<\infty .
   \]

In that case, with the inverse defined as zero on the diagonal,
\[
        \xi=\xi_N+S_{1/(\bar z-\bar w)}\eta,\qquad
        \|\xi\|_2^2=\|\xi_N\|_2^2+
              \int_{z\ne w}|z-w|^{-2}\,d\nu_\eta.                         \tag{1}
\]
In particular the diagonal spectral projection of the joint vacuum is exactly its projection onto \(L^2(N)\), even if the spectral diagonal of the entire bimodule \(H\) is larger.
Applying the equivalence at every coordinate characterizes \(\mathsf A(X)\).
Full ACSY itself forces diffuse marginals. [Normal phase and diffuseness](Yin_C_F0076_v1.md#statement)

The same regularization gives a test of the original right column cost on any such tuple.
On the coarse Hilbert tensor space write \(I_{a\otimes b}(v\otimes w)=va\otimes bw\), extended by the inner marginal spectral calculus, and \(C=\mathrm{id}\otimes\tau\).
For \(r>0\) set
\[
  k_r(z,w)=\frac{\bar z-\bar w}{|z-w|^2+r^2},\qquad
  E_r=C I_{k_r}\gamma,\qquad E=C\delta .
\]
Let \(c(T)=\sup\{(\sum_j\|Tp_j\|_2^2)^{1/2}:p_j\in P,\ \|\sum_j p_j^*p_j\|\le1\}\), allowing all finite columns.
There is a numerical constant \(A\) such that
\[
 c(E_r)\le A\,c(C\gamma)/r<\infty,\qquad
 c(E)\le\liminf_{r\downarrow0}c(E_r),\qquad
 \sup_{r>0}c(E_r)\le3c(E) \quad\text{if }c(E)<\infty.                    \tag{2}
\]
Thus the original cost is infinite precisely when \(c(E_r)\to\infty\) as \(r\downarrow0\).
Uniform control as the cutoff is removed, for all coordinates of all actual normal tuples, is equivalent to the universal implication \(\mathsf A\Rightarrow\mathsf S\) by the [free-enlargement column criterion](Yin_C_F0208_v1.md#statement).

## Argument

### Recovering the divided difference on the represented core

Write \(u=z-w\).
On formal starred words evaluated at \(X\), assign \(D Z=1\otimes1\), \(D Z^*=\bar u/u\) in the marginal coarse space and zero at the omitted letters, and extend by the outer product rule.
Each value is a finite sum of bounded outer coefficients acting on Hilbert tensors.
The formal identity \(\gamma=I_uD\) holds at every letter and hence every word, since inner multiplication commutes with both outer actions.
The coarse inner spectral measure class of the two marginal copies is dominated by \(\mu^2\).
Indeed on each simple Hilbert tensor the two one-leg vector measures are absolutely continuous with respect to \(\mu\), and finite sums of simple tensors are dense.
Thus \(I_u\) is injective by diffuseness.
Once \(\gamma\) descends, any represented relation has \(D\)-value zero, so \(D\) defines a derivation on the original core.
For an actual distinguished derivation the normal relations force precisely these starred values, using the same injectivity for the outer actions of each diffuse marginal. [Normal phase](Yin_C_F0076_v1.md#statement)

If \(\delta\) is actual, its restriction to marginal polynomials gives the scalar vacuum by orthogonal projection.
The algebraic partial liberation is \(I_u\delta\).
The actual tensor adjoint at \(Z^*\otimes1-1\otimes Z^*\) gives
\[
                      \eta=Z^*\xi-\xi Z^* .
\]
The two scalar correction terms cancel in the tensor adjoint formula. [Liberation computation](Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions)
Hence \(\nu_\eta=|u|^2\nu_\xi\), and condition 3 follows.

### The scalar correction in the liberation adjoint

Assume conditions 1–3.
Apply the [marginal tensor adjoint formula](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) to \(i\gamma\), whose vacuum is \(-i\eta\).
After removing the factor \(i\), the result for \(\gamma\) reads
\[
     \gamma^*h=S_h\eta+\operatorname{row}(h)-\operatorname{col}(h),
\quad \operatorname{row}(h)(z)=\int h(z,w)d\mu(w),\quad
      \operatorname{col}(h)(z)=\int h(w,z)d\mu(w).
\]
It gives \(\nu_\eta\ll\mu^2\) and applies in particular to every continuous \(h\) on the compact spectral square, by uniform polynomial-tensor approximation and closedness of the adjoint.
Use \(h=\bar k_r=u/(|u|^2+r^2)\) and set \(B_r=\operatorname{row}(\bar k_r)\).
Antisymmetry gives the difference of row and column equal to \(2B_r\).
For every fixed \(p\in P\), cyclicity of the two traces and continuity on the coarse space give
\[
  \langle S_{\bar k_r}\eta+2B_r,p\rangle
       =\langle 1\otimes1,I_{k_r}\gamma(p)\rangle
       =\langle 1\otimes1,I_{|u|^2/(|u|^2+r^2)}D(p)\rangle.               \tag{3}
\]
The multiplier on the right converges strongly to the identity on the coarse space by diffuseness and dominated convergence.
On \(H\), \(S_{\bar k_r}\eta\) converges in norm to \(S_{1/\bar u}\eta\) by condition 3 and the zero diagonal mass of \(\nu_\eta\).
This limit is perpendicular to the spectral diagonal, which contains \(L^2(N)\).

The [scalar soft Cauchy estimate](Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) gives \(\|B_r\|_2\le\|\xi_N\|_2\), with its parameter \(t=r^2\) and its kernel conjugated.
For a marginal polynomial \(p\), the spectral term on the left of (3) pairs to zero since \(p\) is diagonal and \(\bar k_r\) vanishes there.
The right side tends to the scalar divided-difference vacuum pairing \(\langle\xi_N,p\rangle\).
Density and the uniform bound imply \(2B_r\rightharpoonup\xi_N\) in \(L^2(N)\), and hence in \(H\).
Taking limits in (3) for every mixed word now gives the actual adjoint of \(D\) at the vacuum and formula (1).
This also proves the diagonal assertion and uniqueness in the forward direction.
The double-trace test holds on the whole represented core, independently of the direction in which the derivation was constructed.

### Removing the cutoff in the column norm

For any outer derivation \(\theta\) with finite column cost for \(L=C\theta\), the product rule and traciality yield
\[
 C I_{v\otimes w}\theta(p)=L(pw)v-pL(w)v .
\]
Here \(w\) may be any element of the norm closure of \(P\): first take \(w\in P\), then pass to a uniform approximant using the one-input bound on \(L\).
For each finite polynomial column the first term has direct-sum Hilbert norm at most \(c(L)\|w\|\|v\|\|\sum p_j^*p_j\|^{1/2}\).
For the second use \(\sum_j\|p_jh\|_2^2\le\|\sum_jp_j^*p_j\|\|h\|_2^2\).
Thus a separated multiplier of marginal unitaries costs at most \(2c(L)\) for the sliced column.
The bound integrates against the total variation of any finite Fourier measure representing a function of \(z-w\), because its characters are products of continuous marginal unitaries, and evaluation on a fixed coarse vector is strongly continuous.

For \(u\in\mathbb R^2\simeq\mathbb C\), \(e^{-s|u|^2}\) is the Fourier transform of a centered Gaussian probability, with density \((4\pi s)^{-1}e^{-|v|^2/(4s)}\) in the convention \(e^{iv\cdot u}\).
Integration by parts gives a representing density for \(\bar u e^{-s|u|^2}\) by a linear combination of its two first partial derivatives, with \(L^1\)-norm at most \(C_0s^{-1/2}\) by dilation.
Using
\[
  k_r(u)=\int_0^\infty e^{-sr^2}\bar u e^{-s|u|^2}\,ds,\qquad
  \frac{r^2}{|u|^2+r^2}=\int_0^\infty r^2e^{-sr^2}e^{-s|u|^2}\,ds ,
\]
gives Fourier measures of total variation at most \(C_0\sqrt\pi/r\) and \(1\), respectively.
The constants do not depend on the spectral support.

The slice \(C\gamma\) has finite column cost.
Indeed, apply the [liberation slice bound](Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions) after the [two-Haar enlargement](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words).
The enlarged liberation still kills the new Haar letters and has vacuum \([Z^*,\xi]\) by the same calculation.
For any old column \(p_j\), encoding it by \(\sum_j U^jVU^{-j}p_j\) gives exactly the sum of the corresponding squared output norms, while its input norm is at most \(2\|\sum_j p_j^*p_j\|^{1/2}\). [Column encoding](Yin_C_F0208_v1.md#encoding-finite-columns-by-two-haar-unitaries)
Applying the first Fourier bound to \(\gamma\) proves the first estimate of (2).
If \(c(E)<\infty\), write \(E_r=E-CI_{r^2/(|u|^2+r^2)}\delta\) and apply the second Fourier bound to \(\delta\).
For an arbitrary fixed finite column, \(E_rp_j\to Ep_j\) in \(H\) by the coarse convergence used in (3).
Taking finite-column tests before their supremum proves the lower limit in (2), also when that supremum is infinite.

### Scope

The [classical selfadjoint liberation commutator](../audits/literature/Voi99/Yin_U003.md#liberation-derivation-and-gradient) identifies the gradient from a given conjugate variable.
Here the inverse spectral action and the scalar correction recover the full normal conjugate vector from two measured quantities.
Their squared norms determine vacuum existence.
Estimate (2) leaves open whether these quantities suffice to bound the column costs uniformly as \(r\downarrow0\).

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T10:17 |
| status | open |
| reason | Fix the inverse-gap criterion, norm identity and column regularization for independent inspection. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Necessary and sufficient conditions for the distinguished vacuum, its orthogonal decomposition and the regularized column estimates. |
| argument | [Argument](#argument) | Faithful descent by inner spectral multiplication, weak scalar and strong off-diagonal limits and two-Haar column bounds for Fourier multipliers. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#statement) | Diffuseness for full ACSY, forced starred values and scalar divided differences. |
| dependency | [Actual liberation bounds](Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions) | The commutator vacuum and the algebraic liberation contraction estimate at an actual vacuum. |
| dependency | [Marginal adjoint graph](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | The tensor adjoint, its row and column correction and spectral absolute continuity. |
| dependency | [Scalar regularization](Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | The actual scalar vacuum bounds all soft Cauchy transforms in the marginal Hilbert norm. |
| dependency | [Augmented column criterion](Yin_C_F0208_v1.md#statement) | Free Haar enlargement preserving the actual derivations, Hilbert orthogonality, the finite-column encoding and its universal consequence. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T10:25 |
| status | proved |
| reason | Adopt the recovery criterion, its norm identity and the cutoff characterization after independent whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Necessary and sufficient conditions for the distinguished vacuum, its orthogonal decomposition and the regularized column estimates. |
| argument | [Argument](#argument) | Faithful descent by inner spectral multiplication, weak scalar and strong off-diagonal limits and two-Haar column bounds for Fourier multipliers. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#statement) | Diffuseness for full ACSY, forced starred values and scalar divided differences. |
| dependency | [Actual liberation bounds](Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions) | The commutator vacuum and the algebraic liberation contraction estimate at an actual vacuum. |
| dependency | [Marginal adjoint graph](Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | The tensor adjoint, its row and column correction and spectral absolute continuity. |
| dependency | [Scalar regularization](Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | The actual scalar vacuum bounds all soft Cauchy transforms in the marginal Hilbert norm. |
| dependency | [Augmented column criterion](Yin_C_F0208_v1.md#statement) | Free Haar enlargement preserving the actual derivations, Hilbert orthogonality, the finite-column encoding and its universal consequence. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0247_v1.md#finding) | Represented-core descent, both limits and adjoint signs, the orthogonal norm identity, and all three column estimates with their tuple-wise quantifiers. |

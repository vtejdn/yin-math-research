---
author: Yin
---

# Uniform lattice slice estimates on a line and in grid strips

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Use the [finite-label liberation model](Yin_C_F0339_v1.md#statement) of a marginal partition \(D=\operatorname{span}\{e_i\}\) and a killed projection \(P\), with actual liberation vacuum \(\eta\).
Write \(B_c\) for (1) of that model and \(E_c\) for the exact right slice with off-diagonal multiplier \(1/(c_i-c_j)\).
There is an absolute constant \(C\) such that on the whole represented word algebra, for any number of collinear labels,
\[
                         \|E_c p\|_2\le C B_c\|p\| .
\]
This holds also for arbitrary points on a line separated by at least \(h>0\), defining \(M_i\) and the budget with this lower scale \(h\).
It includes all two-label configurations with unrestricted operator \(P\).

For square lattice labels of mesh \(h\) lying in at most \(m\) consecutive horizontal grid rows, \(m\ge1\),
\[
                         \|E_c p\|_2\le C m^3 B_c\|p\| .
\]
The same estimate holds for consecutive vertical grid columns.
The constants are independent of the number of occupied lattice sites, the length of the strip and the generated algebra.
The estimate leaves the unrestricted planar lattice supremum open.

## Argument

### Exact recovery from real spectral intervals

Translation, rotation and common dilation preserve the normalized cost: rotating the labels rotates the inverse gaps and the \(H_i\) by the inverse phase, and rescaling changes both \(E_c\) and \(B_c\) by the same inverse factor.
Take real labels \(x_i\) with pairwise distance at least \(h\).
Use the [free corner noise construction](Yin_C_F0339_v1.md#free-noise-in-each-spectral-corner) on intervals centered at \(x_i\) of half-length \(h/8\), with uniform conditional laws.
This gives a bounded selfadjoint coordinate \(X\) and killed selfadjoint coefficient \(P\) in their generated algebra and an actual normalized derivative \(\partial X=1\otimes1\).
The [scalar and mixed budget estimate](Yin_C_F0339_v1.md#the-scalar-vacuum-of-the-spread-measure) gives \(\|\xi_X\|_2\le C_0 B_x\).
These steps use only the lower separation \(h\): the conditional scalar vacuum is \(O(1/h)\), the mixed inverse gap on two intervals is bounded by \(4/(3|x_i-x_j|)\), and the averaged scalar kernel error on interval \(i\) is bounded by \(C\sum_{j\ne i} t_j h/|x_i-x_j|^2\le C' M_i\) by dyadic annuli.

The [real coassociative slice estimate](Yin_C_F0136_v1.md#3-analytic-unitaries-and-the-operator-norm-estimate) with unit terminal weight gives
\(\|(\mathrm{id}\otimes\tau)\partial p\|_2\le4\|\xi_X\|_2\|p\|\).
Here only the distinguished vacuum is needed.
Indeed the represented core derivative on \(X,P\) is algebraic, real, and coassociative since the unit tensor at \(X\) and zero at \(P\) have zero iterates and the coassociativity defect is an outer derivation.
The core adjoint formula and the differentiated unitary series in the cited argument use this derivative and its vacuum only.
No normalized second derivative at the projection is involved.

Approximate each slot cut by real polynomials in \(X\) in the operator norm and graph norm, using \(C^1\) approximation to smooth functions constant on neighborhoods of the disjoint intervals.
As in the [conditional recovery calculation](Yin_C_F0339_v1.md#recovering-the-discrete-derivative-on-circles), the conditional expectation onto the original algebra \(N=W^*(D,P)\) from each spread marginal takes its normalized scalar mean times the slot projection.
Project both tensor legs of the graph derivative using this expectation.
On the old algebra this gives an outer derivation \(\bar d\) whose value on a slot has kernel
\[
 (1_i(j)-1_i(k))A_h(x_j-x_k),\qquad
 A_h(d)=\mathbb E\{(d+X'-Y')^{-1}\}\quad(|d|\ge h),
\]
where \(X',Y'\) are independent scalar uniforms on \([-h/8,h/8]\).
It kills \(P\).
This follows by taking the two separate conditional means on the divided difference of a cut and applying outer \(N\)-bimodularity on each word.
Writing \(\bar E=(\mathrm{id}\otimes\tau)\bar d\), projection and the polynomial approximants give \(\|\bar E p\|_2\le4 C_0 B_x\|p\|\).

We invert the scalar averaging uniformly.
At \(h=1\), for \(|d|\ge 1/2\) the symmetric law of \(T=X'-Y'\), supported on \([-1/4,1/4]\), gives
\[
       d A_1(d)=\mathbb E(1-T^2/d^2)^{-1}\ge1 .
\]
Its difference from one is \(O(|d|^{-2})\) for \(|d|\ge1\), and its derivative there is \(O(|d|^{-3})\), by differentiation under expectation.
Choose a fixed smooth cutoff zero on \(|d|\le1/2\) and one on \(|d|\ge1\) and use it to extend \((dA_1(d))^{-1}-1\) by zero into the center.
The resulting function \(g\) has bounded \(H^1(\mathbb R)\) norm, so its Fourier transform is in \(L^1\) by Plancherel and Cauchy--Schwarz against \((1+t^2)^{-1/2}\).
Thus \(1+g(d/h)\) is a Fourier transform of a complex measure of absolutely bounded variation independent of \(h\).
It equals \(1/(d A_h(d))\) on all distinct label pairs by scaling.
The value on equal labels is immaterial since \(\bar d\) has zero inner diagonal on every word.

For an outer derivation \(d'\) on the word algebra with right slice \(E'\), traciality gives
\[
        (\mathrm{id}\otimes\tau) I_{v\otimes w}d'p
                    = E'(pw)v-p E'(w)v .
\]
In particular inserting two marginal unitaries costs at most \(2\|E'\|_{\infty\to2}\|p\|\). [Separated multiplier calculation](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm)
Here every scalar function on the finite label set belongs to \(D\).
Applying the Fourier measure above to \(\bar d\) recovers the exact multiplier \(1/(x_j-x_k)\) on the generators, hence the exact \(d_x\) on all words.
The collinear estimate follows.

### A fixed number of consecutive parallel rows

Normalize and translate the lattice so that \(c_i=n_i+i_{\mathbb C} y_i\), \(n_i\in\mathbb Z\), \(y_i\in\{0,\dots,m-1\}\), using \(i_{\mathbb C}=\sqrt{-1}\).
Give the same projections the real labels \(x_i=n_i+y_i/(2m)\), with spacing at least \(h'=1/(2m)\).
For equal \(n\), \(|c_i-c_j|=2m|x_i-x_j|\).
For unequal \(n\), \(|x_i-x_j|\ge |n_i-n_j|/2\) and \(|c_i-c_j|\le m|n_i-n_j|\).
Thus all inverse-gap vacuum terms in \(B_x\) cost at most \(2m\) times those in \(B_c\) after taking the square root.
For \(s\ge h'\), a real label ball of radius \(s\) is contained in a planar label ball of radius \(2ms\ge1\), giving \(M_i(x)\le 2m M_i(c)\).

For \(|n_i-n_j|\le2m\), the difference of the two nonzero reciprocal-gap kernels is bounded by \(2m+1\), and the planar mass of these labels is at most \(3m M_i(c)\).
For \(|n_i-n_j|>2m\), the difference is bounded by \(C m/|n_i-n_j|^2\).
The dyadic annuli in \(|n_i-n_j|\) at these distances have mass at most a constant times their outer radius times \(M_i(c)\), giving summed error \(C M_i(c)\).
Hence \(|H_i(x)|\le |H_i(c)|+C m^2 M_i(c)\) and \(B_x\le C_1 m^2 B_c\).

On the distinct labels the ratio converting \(d_x\) to \(d_c\) is
\[
 \frac{x_i-x_j}{c_i-c_j}
 =1+\left(\frac1{2m}-i_{\mathbb C}\right)
              \frac{y_i-y_j}{n_i-n_j+i_{\mathbb C}(y_i-y_j)} .
\]
Only \(2(m-1)\) nonzero integer differences \(k=y_i-y_j\) occur.
The support condition for each such \(k\) is the integral of the characters
\(\exp(i_{\mathbb C}\theta(y_i-y_j-k))\) in normalized circle measure.
The function of the horizontal difference \(b\mapsto k/(b+i_{\mathbb C}k)\) is the Fourier transform of a measure of variation one.
Indeed for \(k>0\) it is \(-i_{\mathbb C}\int_0^\infty k e^{-kt}e^{i_{\mathbb C}bt}\,dt\), and for \(k<0\) use \(|k|\) with the opposite character.
Each product of these horizontal and vertical characters is a separated pair of marginal unitaries times a scalar of modulus one.
Thus the new insertion costs at most \(C_2m\) times the real slice cost by the same traced product rule.
Combining the estimates gives \(C m^3B_c\|p\|\).
A quarter turn treats the vertical case.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:23 |
| status | open |
| reason | Fix the uniform discrete collinear estimate and its extension to fixed-width lattice strips for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Absolute collinear bound, including two labels, and \(C m^3\) for arbitrary numbers of sites on \(m\) consecutive rows or columns. |
| argument | [Argument](#argument) | Selfadjoint interval spreading, inversion of the interval-averaged reciprocal by a Fourier measure, real re-encoding of the strip and separated row-difference multipliers. |
| dependency | [Lattice data](Yin_C_F0339_v1.md#statement) | Finite-label derivation, original word algebra and the lattice vacuum and geometry budget. |
| dependency | [Corner noises](Yin_C_F0339_v1.md#free-noise-in-each-spectral-corner) | Conditional uniform interval laws from free noise and the extension of partial liberation. |
| dependency | [Spread vacuum](Yin_C_F0339_v1.md#the-scalar-vacuum-of-the-spread-measure) | Actual vacuum on the spread model with quantitative bound from scalar and mixed gaps. |
| dependency | [Cut recovery](Yin_C_F0339_v1.md#recovering-the-discrete-derivative-on-circles) | Norm and graph polynomial approximation to slot projections and the two conditional means in their derivative. |
| dependency | [Real slice estimate](Yin_C_F0136_v1.md#3-analytic-unitaries-and-the-operator-norm-estimate) | The real coassociative unweighted calculation on the original mixed core with a killed coefficient. |
| dependency | [Separated multipliers](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | Exact traced product rule for two marginal unitaries used in both kernel inversions. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:28 |
| status | proved |
| reason | R_F0345 checked real interval averaging, Fourier inversion on the projected labels, the budget comparison for a strip and all six fixed dependencies. The bounds are absolute on a line and independent of the number of labels in a fixed-width grid strip. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Absolute collinear bound, including two labels, and \(C m^3\) for arbitrary numbers of sites on \(m\) consecutive rows or columns. |
| argument | [Argument](#argument) | Selfadjoint interval spreading, inversion of the interval-averaged reciprocal by a Fourier measure, real re-encoding of the strip and separated row-difference multipliers. |
| dependency | [Lattice data](Yin_C_F0339_v1.md#statement) | Finite-label derivation, original word algebra and the lattice vacuum and geometry budget. |
| dependency | [Corner noises](Yin_C_F0339_v1.md#free-noise-in-each-spectral-corner) | Conditional uniform interval laws from free noise and the extension of partial liberation. |
| dependency | [Spread vacuum](Yin_C_F0339_v1.md#the-scalar-vacuum-of-the-spread-measure) | Actual vacuum on the spread model with quantitative bound from scalar and mixed gaps. |
| dependency | [Cut recovery](Yin_C_F0339_v1.md#recovering-the-discrete-derivative-on-circles) | Norm and graph polynomial approximation to slot projections and the two conditional means in their derivative. |
| dependency | [Real slice estimate](Yin_C_F0136_v1.md#3-analytic-unitaries-and-the-operator-norm-estimate) | The real coassociative unweighted calculation on the original mixed core with a killed coefficient. |
| dependency | [Separated multipliers](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) | Exact traced product rule for two marginal unitaries used in both kernel inversions. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0345_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

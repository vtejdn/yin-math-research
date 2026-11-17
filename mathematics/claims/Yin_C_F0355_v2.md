---
author: Yin
---

# Binary quadratic coefficients and the conditional-variance test

<a id="statement"></a>
## Indefinite symmetric part

Take two independent real Wigner inputs with fixed centered strict upper laws of variance one and centered finite-second-moment diagonal laws.
Let \(P(x)=\sum_{i,j=1}^2 Q_{ij} x_i x_j+\ell\cdot x+c\) with real coefficients.
Assume \(\det Q\ne0\) and the real symmetric part \(S=(Q+Q^{\mathsf T})/2\) is indefinite.
Its null cone consists of two distinct real lines.
Choose basis vectors on these lines and let \(U,V\) be the two dual coordinate forms, allowing rescaling and interchanging them.
At a raw off-diagonal input \(\xi\), suppose at least one of the conditional variances of \(U(\xi)\) given \(V(\xi)\) or of \(V(\xi)\) given \(U(\xi)\) is positive on an event of positive probability.
Then, under every coupling across dimensions, the ordinary normalized potential converges almost surely in local planar \(L^1\) to \(\tau\log|P(s)-z|\), the empirical eigenvalue probability converges weakly almost surely to the free Brown measure, and the normalized bottom-\(h_N\) disk integrals have summable deviations at each positive tolerance with \(h_N=\lceil\log(N+3)\log\log(N+3)\rceil\).
At every prescribed nonreal parameter the ordinary normalized scalar log converges in probability through all dimensions and almost surely along \(2^j\).
For example, any positive absolutely continuous component of the joint raw pair suffices for the conditional-variance assumption.

For two independent Rademacher matrices, the one-way hypothesis holds precisely when at least one null line contains a nonzero vector in \(\{-1,0,1\}^2\).
If both null lines have this property, the pointwise limits, including the every-coupling full-size limsup, apply at **every fixed complex shift**.
The associated three-dimensional affine pencil has no nonzero rank-one coefficient combination.
These assertions include arbitrary fixed real lower-degree coefficients.

<a id="argument"></a>
## Reduction and affine shifts of the physical forms

Write \(T\) for the real invertible matrix whose columns span the two null lines.
With \((U_0,V_0)^{\mathsf T}=T^{-1}x\), the quadratic part equals \(\alpha U_0 V_0+\beta V_0 U_0\), since \(T^{\mathsf T}QT\) has zero diagonal.
Both off-diagonal coefficients are nonzero by \(\det Q\ne0\) and \(\alpha+\beta\ne0\) by \(\det S<0\).
Absorb \(\alpha\) into the first form to obtain \(UV+\lambda VU\), \(\lambda=\beta/\alpha\ne0,-1\).
If the conditional variance is in the other orientation, interchange and rescale the forms and replace \(\lambda\) by its reciprocal.
The affine part is \(l_U U+l_V V+c\).
Setting \(U'=U+l_V/(1+\lambda)\), \(V'=V+l_U/(1+\lambda)\) writes \(P=U'V'+\lambda V'U'+c'\) for a real constant \(c'\).
The scalar shifts here multiply the identity in each physical dimension.

For completeness the [conditional two-form proof](Yin_C_F0355_v1.md#argument) applies with these shifted forms as follows.
The cross columns and their joint law, the conditional masks, the available independent entries and the exterior spaces are unchanged: \(\operatorname{span}(e_i,V'e_i)=\operatorname{span}(e_i,Ve_i)\).
Deleting a site gives the same two cross terms, now computed relative to the shifted original forms restricted to the old minor.
The physical Schur identity uses \(V'\) also in the \(V'x\) term of the restored row.
Its algebra and degree are identical; all norm guards for \(U',V'\) follow from those for \(U,V\) and the fixed constants.
The precision of the two initial trims and the first adaptive overlaps is supplied directly by [the general affine-quadratic theorem](Yin_C_F0186_v42.md#statement) for the original input colors, without transforming their law.
In the free scalar and two-site specialization tests the effective variables \(U',V'\) still take arbitrary values since the affine change of coordinates is invertible.
Thus the span of physical kernels, including the symmetry reduction at \(\lambda=1\), and the [conditional panel and Fourier estimates](Yin_C_F0355_v1.md#conditional-tests) give the same regular ratios, integrated limits and nonreal pointwise comparison.
In the augmented pencil the constant drift may also enter its off-diagonal blocks; its bottom \(2\)-square block is still \(-I\).
The two-dimensional variable part still has rank two in every nonzero direction.
The Schur complement and free multiplicativity identify both scalar logarithms as three times their respective normalized pencil logarithms.

For the Rademacher real-axis argument the covariance of the centered conditional rows and the marked-column degrees are unchanged by scalar shifts.
The possibly shifted conditional means enter the second moments as additional nonnegative squared norms.
The spectral windows of each physical form are translated by a constant.
Hence the [window proof](Yin_C_F0355_v1.md#real-signs) for each shifted form gives the same affine gap against the other.
The companion borders retain the covariance of the original two forms; its graph coordinates now involve the shifted old forms and use the preceding gaps.
The sparse-vector rectangle test still isolates a nonzero quadratic word because constants and linear terms vanish from its second mixed difference.

For the fixed-fraction initialization at \(n/N=a_N\to a\) use the original scalar-normalization comparison of the three-channel companion.
More explicitly, write the diagonal shifts as \(d_U,d_V\), order the channels as in the [mixed pencil](Yin_C_F0355_v1.md#statement), and conjugate its canonical companion on both sides by \(\operatorname{diag}(\sqrt{a_N}I,I,I)\).
The resulting matrix has the old physical normalization if the canonical drifts are \(d_U/\sqrt{a_N},d_V/\sqrt{a_N}\) and its spectral parameter is \((z-c')/a_N\).
The canonical fixed-clip laws converge at these converging drifts by bounded coefficient perturbations and the weak law.
The corresponding free logarithm varies continuously in \(a\in[0.9,1]\): each companion is full by the nonzero scalar quadratic, so the [uniform free power estimate](Yin_C_F0352_v1.md#statement) on this compact family controls the lower log part and its free norms are uniformly bounded.
The fixed-fraction initialization and the projected-border growth proof therefore give the two real-shift trims by letting \(a\uparrow1\).
All other real-axis ratio and pole arguments now use exactly the shifted versions above.
For the old near-full minor the same normalization makes the three canonical parameters converge to those of the fixed target; the window, covariance and Schur bounds are uniform for the shifts in small compact real neighborhoods and the same argument applies along those deterministic perturbations.
This completes the extension to all fixed lower-order real coefficients.

<a id="laws"></a>
## Checking the original input laws

Write \(U=U(\xi),V=V(\xi)\) here for the raw pair before adding the deterministic diagonal shifts.
If \(\operatorname{Var}(U\mid V)=0\) almost surely, the square-integrable \(U\) equals a measurable function of \(V\) almost surely.
The graph of such a function has zero two-dimensional Lebesgue measure by Fubini.
An invertible real linear transformation of any positive absolutely continuous component retains that property.
Thus a joint raw distribution with a positive absolutely continuous component satisfies the variability condition in each orientation.

For the four equiprobable binary sign words, \(U\) has nonzero conditional variance somewhere given \(V\) if and only if two different words have identical \(V\) and different \(U\).
Distinct words of equal \(V\) automatically have different \(U\) because the coordinate transformation is invertible.
The nonzero differences of two words are exactly the doubles of the nonzero vectors of \(\{-1,0,1\}^2\).
Finally \(\ker V\) and \(\ker U\) are precisely the two null lines of \(S\).
This proves the claimed test, independently of any special correlation between the mixed forms.
A positive definite symmetric part admits no real null direction, so this binary reduction does not provide a missing square for that case.

## Current assessment
[Selected decision](#decision-binary-null-lines-reviewed)

## Assessment history

### Decision binary-null-lines-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-17T13:40 |
| status | open |
| reason | The null-line form, the conditional original-law test and the shifted word-chain give a candidate binary classification under the stated hypotheses. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Binary classification](#statement) | Indefinite symmetric part, invertible quadratic tensor, real finite-variance and binary sign inputs. |
| argument | [Affine two-form reduction](#argument) | Algebraic normalization, moving drifts, conditional row comparisons and the corresponding matrix pencil. |
| support | [Conditional laws](#laws) | A positive density component and the exact binary sign-word test. |

### Decision binary-null-lines-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-17T13:43 |
| status | proved |
| reason | Independent inspection confirmed the binary null-line and law tests, including fixed affine terms and the dyadic sign determinant limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Binary quadratic scope](#statement) | Finite variance with one-way variation, and both null-line tests for the fixed real-axis sign conclusion. |
| argument | [Affine coefficient reduction](#argument) | Exact three-channel normalization, shifted observations and the comparison at the principal minor. |
| support | [Original-law conditions](#laws) | Absolutely continuous components and collisions of the four sign words. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0363_v2.md#binary-null-lines-whole-proof) | Entire fixed result including its quantifiers and the original-law hypotheses. |

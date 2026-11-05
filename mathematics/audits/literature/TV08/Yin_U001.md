---
author: Yin
---

<a id="tv08-u001"></a>
# Controlled second moments and a complex inverse-concentration net

The selected source is Tao and Vu, *Random matrices: the circular law*, arXiv:0708.2895v5, 29 February 2008, in the [46-page edition identified in the source notes](readme.md).
The definitions and results below are accepted as established external inputs at their stated complex-scalar scope.
Their exact statements and relevant conventions were read in the original; this acceptance is not an independent full-proof audit.

<a id="controlled-second-moment"></a>
## Definition: controlled second moment

Definition 2.2, PDF pp. 6--7, fixes kappa>=1 and calls a complex random variable x kappa-controlled in second moment when
\[
 E|x|^2\le\kappa,
 \qquad
 E\!\left[(\operatorname{Re}(zx-w))^2
                    \mathbf1_{\{|x|\le\kappa\}}\right]
       \ge\kappa^{-1}(\operatorname{Re}z)^2
       \quad\text{for every }z,w\in\mathbb C.
 \tag{TV-control}
\]
The expectation in the lower bound includes the cutoff indicator; it is not the conditional expectation given that cutoff.
The right side is the square of Re z, not |z| squared.
Thus this condition does not require a nonsingular two-dimensional real covariance matrix.
The source explicitly includes a real Rademacher scalar as a controlled example.
No mean-zero or independent-real-and-imaginary-parts hypothesis is part of this definition.

<a id="phase-normalization"></a>
## Lemma 2.4: one fixed phase makes the moment controlled

Lemma 2.4, PDF pp. 7--8, states that if x is a complex random variable with finite nonzero variance, there exist a fixed phase exp(i theta) and a fixed kappa>=1 such that exp(i theta)x satisfies (TV-control).
Here finite nonzero variance means 0<E|x-Ex|^2<infinity, so its second absolute moment is finite as well.
The phase and kappa may depend on the law; no uniform kappa over all finite-variance laws is asserted.
The proof uses a bounded truncation with positive conditional variance and a rotation of its real covariance directions.
The lemma and its proof on these pages were read, without treating that reading as an independent audit of the paper.

For deterministic coefficients u_j, replacing x_j by exp(i theta)x_j and u_j by exp(-i theta)u_j preserves the scalar sum and all coefficient norms.
This is a direct scalar notation conversion.
It does not assert that rotating every entry of a Hermitian matrix preserves its model.
A dimension-dependent family requires its own common control constant; the fixed-law phase lemma alone does not provide one for an arbitrary family.

<a id="concentration-convention"></a>
## Definition: complex linear concentration and the covering norm

Definition 3.1, PDF p. 10, uses independent copies x_1,...,x_n of the same complex scalar x and defines, for v in C^n and beta>=0,
\[
 p_{\beta,x}(v)=\sup_{z\in\mathbb C}
     P\left\{\left|\sum_{j=1}^n v_jx_j-z\right|\le\beta\right\}.
 \tag{TV-concentration}
\]
The event is a closed disk for the ordinary complex modulus, and the center is unrestricted.
The coefficient vectors in the inverse statement are unit vectors in the Euclidean norm: sum_j |v_j|^2=1.
The approximation norm is instead
\[
 \|v-w\|_\infty=\max_{1\le j\le n}|v_j-w_j|.
\]
A beta-cover here means a finite set S' contained in C^n such that each vector under consideration is within beta in this norm of some point of S'.
The source conclusion does not require the centers in S' to be unit vectors or members of the high-concentration set.

<a id="inverse-net"></a>
## Theorem 3.2: finite nets for concentrated unit vectors

Theorem 3.2, PDF p. 11, assumes that x has kappa-controlled second moment and that 0<epsilon<=1 is fixed.
Let beta and p depend on n with
\[
 \beta\ge\exp(-n^{\epsilon/2}),
 \qquad p=n^{-O(1)},\qquad 0<p\le1.
\]
For all sufficiently large n, the set
\[
 S_{n,x,\beta,p}=
 \{v\in\mathbb C^n:\|v\|_2=1,\ p_{\beta,x}(v)\ge p\}
\]
possesses a beta-cover in the displayed infinity norm with cardinality at most
\[
 n^{(-1/2+\epsilon)n}p^{-n}+\exp(o(n)).
 \tag{TV-net-cardinality}
\]
There is no upper restriction on beta in the statement; the applications use polynomially small radii.
There is no assumption of a moment above two, bounded density, independent real and imaginary parts, or conjugation invariance.
The input variables must be independent copies of the same controlled complex scalar within this source theorem.
Mixed laws, orientation envelopes and matrix row exposure are not additional source conclusions.

The law enters the theorem through its control constant kappa.
The statement specifies sufficiently large dimension in terms of kappa and epsilon and permits the polynomial concentration parameter p to vary with n.
The fixed constant implicit in p=n^(-O(1)) is also retained when using its asymptotics; the final proof paragraph on p. 29 explicitly allows the sufficiently-large threshold to depend on the concentration parameter.
Accordingly the accepted interface is uniform over laws with a common kappa, beta in the displayed range, and p in [n^(-D),1] for each fixed D, with thresholds and asymptotic errors allowed to depend on kappa,epsilon,D.
No quantitative rate for the o(n) error is claimed here.
The additive exp(o(n)) term is part of the conclusion and cannot be omitted from a counting argument without a separate justification.

<a id="inspection-and-use-limits"></a>
## Inspection and applicability limits

Definition 1.5 on PDF p. 5 supplies the asymptotic notation.
Definition 2.2, Lemma 2.4, Definition 3.1 and Theorem 3.2 were read directly at the locators above, and the selected definition and theorem pages were visually checked.
The proof endpoints on pp. 28--29 were read for the controlled-moment truncation, polynomial concentration parameter, exceptional-coordinate entropy and final net bound.
The intermediate Fourier-analytic and additive-combinatorial lemmas in Sections 4--9, their cited inputs and the complete inverse-theorem proof were not re-audited.
No equivalence with another preprint or publication layout is needed for this accepted version-specific interface.

For a conditional truncation family, the consuming argument must prove that one fixed phase gives a common controlled-second-moment constant before using the uniform source theorem.
For nonunit block coefficients it must supply normalization, norm binning and the conversion of the net radius.
For mixed xi/conjugate-xi sums it must supply the orientation split and any associated entropy cost.
For row/profile counting it must justify the initial finite class, short-group treatment, degenerate branch, probability product, choice of deterministic representatives and cancellation of the concentration factors.
These are project deductions, not statements attributed to TV08.
The generic finite-net route does not use NO15's disputed literal rational-generator clause; no correction or verification of that clause is asserted by this unit.

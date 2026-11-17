---
author: Yin
---

# Independent review of perturbed translation commutators and signed shell estimates

At 2026-11-17T06:29 UTC an agent outside the development of Yin_C_A0089_v1 independently reviewed the fixed statement and both proof sections for Sheng Yin.
The reviewer had previously checked the original \(K_j\) approximation and the conjugation-shell interface while reviewing other inputs.
The review used the fixed claim, its direct mathematical sources and the stated review scope.
No proof-development dialogue, author explanation or previous verdict on this claim was supplied.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-argument finding](#whole-argument-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-argument finding](#whole-argument-finding) | [Statement](../../claims/Yin_C_A0089_v1.md#statement) | Small perturbations, the exact reducing and finite-shell hypotheses, original conjugation defect, exterior estimate and integrality scope. |
| [Whole-argument finding](#whole-argument-finding) | [Finite products and contraction](../../claims/Yin_C_A0089_v1.md#finite-products-and-contraction-off-the-identity) | Sign and operator norm of the perturbation map, finite source, row-fit equivalence, localized recurrence and time truncation. |
| [Whole-argument finding](#whole-argument-finding) | [Nonclosed example](../../claims/Yin_C_A0089_v1.md#a-nonclosed-example-with-a-whole-group-row-gram-and-projection) | Orthogonal graphs, positive Neumann series, selected-column restriction, row-Gram reconstruction and the spectral mass exponent. |
| [Whole-argument finding](#whole-argument-finding) | [Nonidentity contraction](../../claims/Yin_C_A0080_v1.md#conjugation-on-the-nonidentity-coefficients) | Norm \(\sqrt3/2\) on the restricted coefficient space under the conjugation-stabilizer hypothesis. |
| [Whole-argument finding](#whole-argument-finding) | [Widened shell transfer](../../claims/Yin_C_A0080_v1.md#signed-estimates-on-widened-shells) | Passing from the original \(K_j\) coefficients to the polarized finite first-return array. |
| [Whole-argument finding](#whole-argument-finding) | [Row-fit identity](../../claims/Yin_C_A0080_v1.md#a-finite-upper-bound-from-row-fits) | Equality of the finite-polynomial residual infimum and the restriction to the kernel. |
| [Whole-argument finding](#whole-argument-finding) | [Signed time truncation](../../claims/Yin_C_A0076_v1.md#passing-from-finite-returns-to-a-spatial-shell) | Dyadic positive spectral mass, Abel error, exterior norm and both comparison directions at the finite horizon. |
| [Whole-argument finding](#whole-argument-finding) | [Spatial trace criterion](../../ledger/Yin_L_A0055_v1.md#proof-and-the-obstruction-at-a-fractional-trace) | Integrality from a weighted square sum of the kernel projection for \(\beta>3\) on the specified four-line group. |
| [Whole-argument finding](#whole-argument-finding) | [Four-line zero product](../../claims/Yin_C_A0051_v1.md#statement) | Nonfreeness of the group used in the example. |

## Whole-argument finding

The complete argument establishes the two spatial criteria and the stated example.
Expanding \(h^*[hI_m+E_h,X]\) gives \(X-h^*Xh+h^*E_hX-h^*XE_h\), with the signs in (3).
On trace \(L^2\), left and right multiplication by a bounded matrix each cost at most its operator norm, and discarding the identity is orthogonal projection.
Thus the compressed sum has norm at most \(\rho+\frac12\sum_h\|E_h\|=\theta<1\).
Conjugation leaves a constant matrix at the identity, while the two corrections can move it only to radius \(w\).
If \([V_h,p]=0\) for all four \(h\), the geometric expansion of \(\Pi p\) has terms of norm at most \(C\theta^l\) and propagation at most \((l+1)w\).
Summing only those terms able to reach radius \(R\) gives the asserted exponential exterior norm.

For a finite input-square \(D\), right multiplication by \(p\) gives the lower bound \(\|ADp\|_2\) on every proposed fit residual.
The bounded output-square multiplier \(AD(A^*A+tI)^{-1}A^*\) belongs to the reduced group matrix algebra and can be approximated in norm by finite polynomials for fixed \(t>0\).
After multiplication by \(A\) the approximant target tends in trace \(L^2\) to \(AD(I-p)\) as \(t\downarrow0\).
This proves equality of the infimum and \(\|ADp\|_2\), and testing \(V_h,V_h^*\) gives exact reduction of the kernel.

For the finite-polynomial input \(K_j\), iteration of the offidentity equation includes both the projected defect \(\Pi D_j\) and the source from the identity.
The latter cannot reach \(2^j\) in \(k_j=O(j)\) steps for large \(j\).
Finite propagation restricts each remaining input to \(S'_j\), and summing its norm costs at most \((1-\theta)^{-1}\).
The leftover \(\mathcal L^{k_j}\Pi K_j\) has norm at most \(\sqrt m\,\theta^{k_j}\).
After multiplying squared shell norms by \(2^{\beta j}\), this remainder is summable under the strict stated bound on \(a\).
The two C80 polarization phases and the uniformly positive padded denominators convert the \(K_j\) bound to the signed finite array, with the summable original-time errors of C76.
The signed exterior comparison then gives the assertion for \(p\), also when exact reduction was not used to obtain (4).
The product rule for \([V_h,Q^l]\) inserts \([V_h,Q]\) once at each position, with the required left factor \(h^*\) outside the sum.
This calculation retains the signs until all contributions at each endpoint are combined.

Under exact reduction and the dyadic return hypothesis, \(\|K_j-p\|_2=O(2^{-\kappa\alpha j/2})\) for the polynomial built from the original Gram.
The unperturbed averaging operator changes the length by a bounded amount, so on the widened shell its four conjugates of \(p\) still contribute \(O(e^{-c2^j})\).
Applying \(I-\mathsf P\) to \(K_j-p\) gives the other term of (2).
The C76 exterior comparison with the exponentially localized \(p\) yields the claimed squared norm power \(R^{-(\kappa\alpha-\beta)}\).
For \(\beta>3\), the projection estimate meets the hypothesis of L55 on the specified good four-line groups.

In the example one may take \(P\) to be uniform on a finite symmetric generating set, giving the required finite input.
The ranges of \(W\) and \(Z\) are closed complementary orthogonal graphs, with \(Z^*\) onto.
Both are invariant under \(V_h\) and \(V_h^*\), and at \(\varepsilon=0\) the matrices are the four unperturbed translations.
Continuity allows a positive rational \(\varepsilon\) satisfying all the stated strict inequalities.
The positive \(L\) is injective and has spectrum approaching zero by \(99\ell\le L\le101\ell\) on the infinite cyclic direction.
Its range is dense nonclosed and determines the range of \(A\).
The inverse in the first projection entry has a positive geometric series with ratio at most \(2q\varepsilon^2/(1+2q\varepsilon^2)<1\).
For every group endpoint a word in the finite generators contributes a strictly positive term, proving full support.

Every choice of \(q\) columns with \(q\ge2\) contains a diagonal entry \(L\).
Its identity and \(u\) coefficients survive the norm error at most four around \(100\ell\).
Any translated subgroup coset carrying it is a conjugate subgroup containing \(u\), since the support includes the identity.
Inside that subgroup the affiliated inverse of \(1-u\) and its adjoint recover the bounded \(D\) from \(L\) and hence all the generators in \(\operatorname{supp}P\).
For the first row-Gram entry the perturbations of the \(u\)-coefficient \(-40000\) have magnitude at most \(4(404+400)+10000<40000\).
Thus a subgroup carrying this entry contains \(u\), and with \(S=I+\varepsilon^2\ell\) the positive square root of \(S^{1/2}BS^{1/2}\) is \(S^{1/2}LS^{1/2}\).
This recovers \(L\) and then the whole group as before.
The obstruction to a common cyclic block concerns actual choices of columns and their stated independent group translations.

The order comparison with \(\ell\) gives sublevel trace comparable to \(t^{1/2}\) for the positive \(L\).
Functional calculus then gives order \(s^{1/4}\) for \(L^2\) by substituting \(t=\sqrt s\).
The bounded positive factor \(I_q+FF^*\) compares \(AA^*\) above and below with constant multiples of \(L^2I_q\).
Transfer of the positive spectrum through the rectangular polar decomposition establishes the original dyadic return estimate with \(\alpha=1/4\).

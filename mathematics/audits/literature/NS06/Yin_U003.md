---
author: Yin
---

# NS06-U003: Finite circular matrix models

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Registered supplied 434-page publisher-layout NS06.pdf; printed pages equal PDF pages minus 17. |
| source-locator | Theorem 11.12, Definition 11.22/Example 11.23, Proposition 11.25, Proposition 12.11/Definition 12.12 and Theorems 14.18/14.20 at the exact locators below. |
| inspection | 2026-09-11 selected cumulant/matrix interfaces with the stated short proof reading and accepted compression foundation. No whole-book or new source-proof audit. |

<a id="ns06-u003"></a>
<a id="ns06-matrix-models"></a>
## Original finite matrix-model source adaptation

Date: 2026-09-11.
Reader: the spectral-extension research agent.
Selected local-book interfaces for [Yin_C_F0095](../../../claims/Yin_C_F0095_v1.md#yin_c_f0095).
The source identity remains NS06.

## Inspected passages

The following passages were read from [the local book](../../../literature/pdf/NS06.pdf), with extracted text checked against direct page extraction.
Printed page numbers are PDF page numbers minus 17.

| Source locator | Consumed statement | Verification scope |
| --- | --- | --- |
| Theorem 11.12, pp. 180-181 (PDF 197-198) | Cumulants of products are sums over partitions whose join with the product interval partition is the top partition | Statement and its short partial-Mobius-inversion proof read |
| Definition 11.22 and Example 11.23, p. 187 (PDF 204) | A standard circular variable has only the two alternating second cumulants, both one | Normalization checked; a free family has zero mixed cumulants |
| Proposition 11.25, especially (11.16), pp. 188-189 | The connected noncrossing pairing for a cyclic list of two-factor products is uniquely the outer pair together with adjacent inner pairs | The particular pairing consequence was checked; its use below does not assert equality for arbitrary non-pair partitions |
| Proposition 12.11 and Definition 12.12, pp. 203-205 (PDF 220-222) | Free Poisson rate \(\lambda\), jump one, has \(\kappa_n=\lambda\) for all \(n\ge1\) | Distribution/cumulant convention and the free-Poisson limit calculation checked |
| Theorem 14.18, pp. 234-235 (PDF 251-252), and the reconstruction discussion in Theorem 14.20, pp. 235-236 | Joint cumulants of compression by a free system of matrix units; reconstruction of the original tuple as a matrix over the corner | Exact joint formula, normalized corner trace and reconstruction map checked; foundational free-compression proof accepted |

These interfaces predate the project.
Their use to recognize a finite rectangular circular matrix as a free-Poisson variable is a source adaptation, not a new project theorem about cumulants.

## Exact finite matrix adaptation

Fix a common positive integer \(m\) and positive integers \(n_1,\ldots,n_d\).
Let all entries of the matrices \(C_j=(c^{(j)}_{a\alpha})\in M_{m,n_j}(\mathcal N)\) form one standard free circular family: \(\tau(c^*c)=1\).
Define

\[
Y_j=\frac1m C_jC_j^*\in M_m(\mathcal N),\qquad
\tau_m=\operatorname{tr}_m\otimes\tau.
\tag{N1}
\]

The resulting \(Y_j\) are freely independent free Poisson elements of rates \(n_j/m\) and jump one.
Here is the exact verification, including their joint law.

Write \(y^{(j)}_{ab}=m^{-1}\sum_\alpha c^{(j)}_{a\alpha}(c^{(j)}_{b\alpha})^*\).
Theorem 11.12 applied to a list of \(r\) such products has only pairing contributions.
The join condition permits only

\[
\{(1,2r),(2,3),(4,5),\ldots,(2r-2,2r-1)\}.
\]

For this pairing, covariance forces all colors \(j\) equal, all column indices \(\alpha\) equal, and \(b_\ell=a_{\ell+1}\), with \(a_{r+1}=a_1\).
Thus

\[
\kappa_r\bigl(y^{(j_1)}_{a_1b_1},\ldots,y^{(j_r)}_{a_rb_r}\bigr)
=\begin{cases}
n_j m^{-r}\prod_{\ell=1}^r\delta_{b_\ell,a_{\ell+1}},
 &j_1=\cdots=j_r=j,\\
0,&\text{otherwise}.
\end{cases}
\tag{N2}
\]

For \(r=1\), this says \(\tau(y^{(j)}_{ab})=(n_j/m)\delta_{ab}\), so the scaling in (N1) is fixed even before computing higher moments.

For an independent check of the passage from entries to the **scalar matrix law**, take an abstract free family \(x_j\) of free Poisson elements with rates \(n_j/m\), freely adjoin matrix units \(e_{ab}\) of trace \(\delta_{ab}/m\), and set \(p=e_{11}\).
Theorem 14.18 says that the entries \(e_{1a}x_je_{b1}\), in the corner trace \(\tau_p=m\tau\), have precisely the joint cumulants (N2): its factor is \(m^{1-r}\kappa_r(x_j)=n_jm^{-r}\).
The map

\[
x\longmapsto(e_{1a}xe_{b1})_{a,b=1}^m
\]

is the trace-preserving unital star-isomorphism from the ambient algebra to its matrix realization over \(p\).
Equality of all joint entry moments then gives equality of the scalar joint matrix moments of this reconstructed family and (N1).
This proves both the rates and freeness of \(Y_1,\ldots,Y_d\); matching their separate marginal laws alone would not prove freeness.
Since the matrices are bounded, their moments determine the required joint tracial law.

Every finite list of positive rational rates admits the common representation \(\lambda_j=n_j/m\).
No limit of matrix sizes is used.
In particular rates below one and their nonzero kernel projections are included.
Replacing a positive irrational rate by rational approximants does not establish any rational-operator boundedness theorem at that rate.

---
author: Yin
---

<a id="no15-u001"></a>
# Complex inverse-concentration statements and their printed arithmetic limits

This unit retains the actual source statements, useful literal obstructions and inspected coordinate passages from Nguyen and O'Rourke, *The Elliptic Law*, arXiv:1208.5883v4, 9 September 2014.
The [source notes](readme.md#yin-complex-linear-inverse-theorem-passages) identify the selected 57-page edition and distinguish the 45-page author-hosted layout.
The record does not adopt a corrected rational-generator theorem or certify the original proof.
The current generic complex counting proof uses the separately inspected [TV08 finite-net interface](../TV08/Yin_U001.md#inverse-net), so the arithmetic limitations below are not unresolved inputs to that proof.

<a id="printed-linear-interface"></a>
## The printed linear theorem and complex-scalar corollary

On PDF p. 10 the source calls a real scalar xi anti-concentrated when there exist positive alpha_1,alpha_2,alpha_3 such that
\[
 P\{\alpha_1<|\xi-\xi'|<\alpha_2\}\ge\alpha_3,
\]
where xi' is an independent copy.
A complex number is beta-close to a set when its complex Euclidean distance to some member of that set is at most beta.
These are fixed distributional constants, not constants asserted uniform over arbitrary varying laws.

Theorem 3.1, PDF p. 10, works in the surrounding complex-coefficient setting, with
\[
 \sum_{j=1}^n|a_j|^2=1,\qquad
 \gamma=\sup_zP\left\{\left|\sum_{j=1}^n a_j(x_j+f_j)-z\right|\le\beta\right\}
             \ge n^{-B},
\]
where x_j are independent copies of an anti-concentrated real scalar xi, 0<epsilon<1 and B>0 are fixed, and beta>0 may depend on n.
The displayed deterministic f_j terms only translate the center under the supremum, so they do not change this concentration number.
For any n' between n^epsilon and n the source asserts a proper symmetric progression
\[
 Q=\left\{\sum_{j=1}^r k_jg_j:k_j\in\mathbb Z,\ |k_j|\le L_j\right\}\subset\mathbb C
\]
with
\[
 r=O_{B,\epsilon}(1),\qquad
 |Q|\le\max\{O_{B,\epsilon}(\gamma^{-1}/\sqrt{n'}),1\},
\]
and at least n-n' coefficients a_j beta-close to Q.
Here proper means the displayed integer-box parametrization is injective, and symmetric has zero translate and symmetric integer ranges.
The printed arithmetic clause (ii) additionally states
\[
 g_j=\beta\,p_j/p,\qquad
 p\in\mathbb Z\setminus\{0\},\quad |p|=O_{B,\epsilon}(\sqrt{n'}),\qquad
 p_j\in\mathbb Z,\quad |p_j|=O_{B,\epsilon}(\beta^{-1}\sqrt{n'}).
 \tag{NO15-literal-steps}
\]
The paragraph immediately after the theorem allows the implicit constants to depend on the random-variable distribution and, in particular, alpha_1,alpha_2,alpha_3.
This distribution dependence is part of the statement's actual scope.

Corollary 3.3, PDF p. 11, states that the conclusion of Theorem 3.1 also holds for independent copies of a complex scalar xi satisfying
\[
 E|\xi|^2=1,\qquad E\xi=0,\qquad
 E[\operatorname{Re}\xi\operatorname{Im}\xi]=0.
 \tag{NO15-complex-hypotheses}
\]
There is no requirement that the real and imaginary parts be independent.
The source derives this corollary by setting b_j=0 in its preceding Theorem 3.2 for mixed forms.
This unit records that exact asserted conclusion and its hypotheses; the literal arithmetic qualification below prevents treating the whole printed output as a verified rational description for complex coefficients.
No full inspection of Theorem 3.2's mixed-family proof or all its hypotheses is asserted by that statement reading.

<a id="literal-generator-obstruction"></a>
## The integer-generator wording fails literally for imaginary coefficients

Because beta is real and p,p_j in (NO15-literal-steps) are integers, every generator in that displayed formula is real.
The symmetric progression Q would therefore be contained in R.
This is incompatible with the complex-coefficient conclusion as printed.

For a fully explicit test, take even n, real Rademacher xi, f_j=0, and
\[
 a_j=i/\sqrt n\quad(1\le j\le n),\qquad
 \beta=n^{-2},\qquad n'=n/2,\qquad B=2,\quad\epsilon=1/4.
\]
The coefficient norm is one, the scalar satisfies the displayed anti-concentration condition, and n^epsilon<=n'<=n eventually.
It also satisfies (NO15-complex-hypotheses), so the same test lies within the complex-scalar corollary's stated law assumptions.
The values of the sum lie on the imaginary lattice with spacing 2/sqrt(n), which exceeds 2beta.
Consequently its concentration is the central binomial atom,
\[
 \gamma=2^{-n}{n\choose n/2}\ge\frac1{n+1}\ge n^{-2}
\]
for n>=2.
The first inequality follows because the central atom is the largest of the n+1 binomial atoms.
However every a_j has distance 1/sqrt(n)>beta from R, and hence from every Q allowed by the literal displayed arithmetic clause.
Thus zero coefficients can be beta-close to Q, whereas the claimed conclusion requires at least n/2 of them.
This is a concrete obstruction to that literal one-coordinate integer formula, not a refutation of the existence of a correctly formulated complex inverse theorem.
It uses no conjectured correction of the source wording.

<a id="literal-denominator-obstruction"></a>
## The printed small-beta denominator bound also cannot be literal

The paragraph preceding Corollary 3.4 and the corollary itself, both on PDF p. 11, describe rational components of the form p/q with integer numerator and denominator bounded by O(beta).
For fixed source parameters and law, beta is allowed to tend to zero with n.
A nonzero integer denominator has |q|>=1, while |q|<=C beta<1 eventually for any fixed implied constant C.
Therefore that printed denominator bound cannot hold in the stated small-beta regime.
The conclusion does not require deciding which inverse-precision bound was intended.
No corrected denominator estimate or corresponding version of Corollary 3.4 is accepted here.

<a id="coordinate-passages"></a>
## What the applications and selected appendix passages actually show

On PDF p. 17, in Section 5's nondegenerate case, the source applies Corollary 3.3 to a normalized complex row vector.
It describes an approximating vector whose coordinates and progression generators have the form p/q+i p'/q', with all four integers bounded in modulus by n^(A/2+O_(B,epsilon)(1)).
The approximation scale there is n^(-A/2+O_(B,epsilon)(1)), the progression rank is O_(B,epsilon)(1), and all but n^epsilon coordinates lie in that progression.
This application explicitly uses two real rational coordinates.

On PDF p. 23, in the profile approximation, the source again writes coordinate values and generators as
\[
 \beta_{k_0}\left(p/q+i p'/q'\right),
\]
with the four integers bounded by a polynomial inverse-precision scale, stated there as O(n beta_(k_0)^(-1)) and n^(A/2+O_(B,epsilon)(1)).
These are actual formulas in the source's application, rather than a local replacement for (NO15-literal-steps).
Their complete profile argument was not re-audited in this source check.

Appendix A, PDF p. 49, explicitly represents a complex coefficient by (Re v,Im v) in R^2 and the Fourier test point by (Re s,-Im s).
On p. 50 it rounds coefficients to (Z/(Dk))^2, equivalently u/(Dk) with u in Z^2, before using additive-combinatorial progression results.
On p. 51 the rank-at-least-three branch sets Q=(beta/(Dk))P.
On p. 52 the rank-two branches instead finish with Q=(beta/(Dk))S.
Thus the inspected construction is genuinely two-dimensional and is not a construction confined to R.
The selected passages support a coordinatewise interpretation of the intended arithmetic output, but do not by themselves verify an exact corrected denominator, common-grid precision, all constants, or the transfer from the mixed theorem to Corollary 3.3.
The full Appendix A argument and its external additive-combinatorial dependencies were not audited.

The previously inspected Nguyen--Vu *Erratum for “Inverse Littlewood--Offord problem”*, [retained comparison PDF](../../../literature/pdf/NV11--erratum.pdf) pp. 1--2, writes real coordinates as beta p_ij/p and repairs a continuous approximation step.
That comparison concerns a real random scalar with vector coefficients.
It is evidence for a coordinate convention, not a verification of NO15's complex-scalar adaptation or a repair adopted in this unit.

<a id="fixed-phase-conversion"></a>
## A simple fixed-phase conversion removes the covariance condition

For a fixed centered complex xi with E|xi|^2=1, put m=E(xi^2), which is finite.
If m is nonzero take theta=-arg(m)/2, and otherwise take theta=0.
Then eta=exp(i theta)xi satisfies E eta=0, E|eta|^2=1, and
\[
 E[\operatorname{Re}\eta\operatorname{Im}\eta]
       =\tfrac12\operatorname{Im}(e^{2i\theta}m)=0.
\]
For deterministic coefficients u_j, set a_j=exp(-i theta)u_j; then sum_j a_j eta_j=sum_j u_j xi_j and sum_j |a_j|^2=sum_j |u_j|^2.
This is a direct scalar conversion using one phase fixed by the original law, without an independence assumption on its components.
If an appropriately stated progression conclusion is available for the a_j, multiplication of its progression by exp(i theta) preserves rank, cardinality, properness and approximation error.
A coordinatewise rational description would become one fixed rotated grid, which by itself introduces no new counting choices.
These observations are conditional on that progression conclusion and do not verify or correct (NO15-literal-steps).
They also do not rotate a Hermitian matrix while preserving its entry model, and they prove no least-singular-value floor.
The source's unqualified distribution-dependent constants cannot be declared uniform for dimension-dependent truncations merely from this fixed-law conversion.

<a id="inspection-and-current-use"></a>
## Inspection and current use boundary

Theorem 3.1 and Corollaries 3.3--3.4 were read directly on PDF pp. 10--11; the relevant displayed arithmetic formulas were also visually checked.
The applications on pp. 17 and 23 and the selected Appendix A passages on pp. 49--52 were read at the scope described above.
The two literal contradictions are local direct calculations retained in this unit, rather than claims of a complete source-proof audit.
No new external search, corrected edition comparison or whole-proof verification is claimed.
The 45-page author-hosted layout was located during the bounded search but is not substituted for this 57-page edition.

The bounded search first reused the real-scalar Ngu12a and Nguyen--Vu material and the existing NO15 notes, then located the TV08 alternative through primary-source queries for complex inverse Littlewood--Offord statements.
It stopped once the relevant statements and limitations were identified; it establishes neither absence of other literature nor priority.
The generic complex proof has replaced the rational-generator route by TV08 finite nets.
Accordingly the NO15 issues remain useful source evidence for a possible future arithmetic use, without a pending literature blocker for the current proof and without a claim that those issues have been repaired.

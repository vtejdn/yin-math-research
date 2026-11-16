---
author: Yin
---

# Arbitrarily small bounded liberation gradients for a deficient normal pair

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

If the [general normal implication](../tasks/Yin_T_F0011_v1.md#contract) \(\mathsf A\Rightarrow\mathsf S\) fails, then for each \(\varepsilon>0\) there is an exchange-symmetric pair of bounded normal generators \(W_0,W_1\) of a finite tracial von Neumann algebra \(Q\), with actual joint conjugate variables \(\xi_0,\xi_1\).
Both original right slice costs are infinite, and the pair has no bare full-domain dual system.
For every two bounded Borel marginal functions \(f,g\),
\[
       \tau(f(W_0)g(W_1))=\tau(f(W_0))\tau(g(W_1)).
\]
In a common tracial extension there are free standard semicirculars \(T_0,T_1\) such that
\[
       \max_j\big(\|W_j-T_j\|+\|\xi_j-T_j\|_2\big)<\varepsilon .
\]
On this same pair the joint liberation gradients \(\eta_j=[W_j^*,\xi_j]\) satisfy
\[
          \eta_1=-\eta_0,\qquad
          \max_j\|\eta_j\|_\infty<\varepsilon,\qquad
          \nu_{\eta_j}^{(j)}\le\varepsilon^2\,\mu\otimes\mu .             \tag{1}
\]
Here \(\mu\) is the common marginal law, and \(\nu_{\eta_j}^{(j)}\) is the spectral measure of \(\eta_j\in L^2(Q)\) for the commuting left and right marginal actions at \(W_j\).
In particular the universal implication is equivalent to finiteness of the first original right slice cost on these actual exchange pairs even with any prescribed positive tolerances in (1) and in the semicircular approximation.
Existence of a deficient normal tuple remains open.

## Argument

### Conjugation by a free unitary of Poisson law

Use the matrix base \(\mathcal R=M_2(N)\), its diagonal coordinate \(W\), the odd centered symmetry \(s_*\), and \(B_*=W^*(s_*)\) in the [exact trace-independent construction](Yin_C_F0322_v1.md#conditional-expectations-of-the-four-matrix-corners).
In a scalar free product adjoin a Haar unitary \(U\) free from \(\mathcal R\), and put
\[
 u=(r+U)(1+rU)^{-1},\qquad s=u s_*u^*,\qquad s_f=U s_*U^*,
                       \qquad 0<r<1.
\]
The disk automorphism and its inverse generate the same von Neumann algebra, and \(u\) has Poisson law with moment \(r^{|n|}\) at integer \(n\).
The centered symmetry \(s_f\) is free from \(\mathcal R\), since an alternating product of centered base letters and centered letters from \(U B_*U^*\) expands into a reduced Haar word.
We have \(\|s-s_f\|\le2\|u-U\|\le4r/(1-r)\).
The grading on \(\mathcal R\) extends by fixing \(U\), so it fixes \(W\) and negates both symmetries.

Splitting \(u=r+(u-r)\) and using \(\tau(s_*)=0\) gives \(\mathbb E_{\mathcal R}s=r^2s_*\).
Thus \(\mathbb E_{B_*}s=b s_*\) with \(b=r^2>0\).
The [four-step expectation](Yin_C_F0322_v1.md#conditional-expectations-of-the-four-matrix-corners) and [two successive compression estimates](Yin_C_F0322_v1.md#uniform-recovery-on-small-primary-pieces) use only \(s\in B_*\vee W^*(U)\), its norm, that regression, and freeness of the noise algebra.
For their \(H=64\operatorname{Re}(e_1s e_5s e_2s e_6s e_1)\), the expectation onto \(M_8(R')\) is \(e_1(a+r^8J)\) for a real \(a\), with compression error at most \(512\sqrt{t_n}\) on primary piece \(n\) of relative mass \(t_n\).
The recovered sign coefficient there has error at most \(512\sqrt{t_n}/r^8\).
Also \(\mathbb E_{B_*}g(W)=\tau(g(W))1\) by the grading.
The [two-marginal conditional expectation](Yin_C_F0317_v1.md#coupling-in-operator-norm-and-comparing-two-marginal-blocks) applies to \(s-b s_*\), centered over \(B_*\), with \(\mathbb E_{B_*}(s-b s_*)^2=(1-b^2)1\).
It gives
\[
 \mathbb E_{\mathcal R}\big(s g(W)s\big)
          = b^2s_*g(W)s_*+(1-b^2)\tau(g(W))1 .
\]
The original matrix symmetry gives the required product trace against \(f(W)\) in the first term too. [Matrix trace calculation](Yin_C_F0321_v1.md#a-symmetry-with-exact-product-traces)

### Correcting the distinguished derivative

Write \(L=L_0+\operatorname{ad}_K\) for the [ambient derivative before the last noise](Yin_C_F0322_v1.md#placing-bad-tests-in-the-top-semicircular-interval), where \(K\in L^2(\mathcal R)\otimes_2 L^2(\mathcal R)\) is the mixed inverse-gap kernel and \(\operatorname{ad}_K(x)=x\cdot K-K\cdot x\) uses outer bimodule multiplication.
Then \(L_0 s_*=0\) and \(Ls_*=s_*\cdot K-K\cdot s_*\).
Extend \(L\) by zero on Laurent polynomials in \(u\); scalar free extension preserves its vacuum by centered reduced words.
On the same free product core add the derivation \(d_K\) killing the base with \(d_Ku=u\cdot K\), \(d_Ku^*=-K\cdot u^*\).
The inverse relation is respected, the Poisson law has full support, and the centered free representation is injective on the algebraic free product.
The corrected derivative takes \(s\) to
\[
       u\cdot\big(K\cdot s_*+Ls_*-s_*\cdot K\big)\cdot u^*=0 .
\]
Its values on \(W,W^*\) are the original unit and normal phase.

Let \(d_Ru=u\otimes1\) and \(d_Lu=1\otimes u\), each with zero values on the base and inverse rule at \(u^*\).
For either orientation the double trace on \(u^n\) sums \(|n|\) signed cuts, each with unsigned double trace \(r^{|n|}\) for \(n\ne0\).
The centered reduced-word extension therefore gives both derivations the same bounded vacuum. [Poisson angular calculation](Yin_C_F0251_v1.md#the-liberation-vacuum-in-free-coordinates)
\[
 H_u=\frac{r}{1-r^2}(U-U^*),\qquad
 \|H_u\|_\infty=\frac{2r}{1-r^2},\qquad
 \|H_u\|_2=\frac{\sqrt2\,r}{1-r^2}.                                    \tag{2}
\]
For a simple base tensor \(K=a\otimes c\), \(d_K\) inserts \(a\otimes c\) at the two inner legs of \(d_R\).
Its double trace at \(x\) equals that of \(d_R(axc)\) by traciality, and so its vacuum is \(a^* H_u c^*\) with the Hilbert inner product linear in its second variable.
Here \(d_R\) is available on the algebraic free product with all bounded base letters.
The map \(a\otimes c\mapsto a^*H_u c^*\) extends conjugate-linearly with norm factor \(\|H_u\|_2\) from the base coarse space, by centering of \(H_u\), freeness, and polarization.
For arbitrary \(K\) each finite-word value of \(d_K\) is a finite sum of bounded outer multipliers of \(K\), so approximation by bounded simple tensor sums proves the same vacuum bound on the whole core.

Restriction to \(M=W^*(W,s)\) now gives the relative actual distinguished vacuum \(\xi\) by Hilbert projection.
The assigned values on its generators and their adjoints lie in its own coarse space.
In [the estimate (6) for \(\|\xi-W\|_2\)](Yin_C_F0322_v1.md#the-good-vacuum-and-its-approximation-to-the-coordinate) only the last summand changes, to at most \(\|H_u\|_2\|K\|_2\).
Fix the interval gap, tail displacement and inverse vacuum parameter as there; their preliminary weighted mass bound already bounds \(\|K\|_2\).
Then choose \(r>0\) small enough for that summand, the sign coupling and (1), before choosing the individual masses.
These masses can meet all original upper bounds and \(512\sqrt{t_n}/r^8<h_n\) for every fixed witness tolerance \(h_n>0\).
The [corner comparison and quantile coupling](Yin_C_F0322_v1.md#the-bad-mixed-tests-trace-independence-and-the-reference-pair) therefore apply with \(T_1=s_fT_0s_f\).
The [even-algebra formula](Yin_C_F0311_v1.md#derivations-on-the-even-algebra) gives the asserted exchange pair \(W_0=W,W_1=sWs\) in \(Q=M^{\rm even}\), its vacua \(\xi,s\xi s\) and both infinite costs.
The same comparison gives the absence of bare duals and the stated simultaneous semicircular approximation.

### The joint liberation gradients and their spectral measures

Use \(d_L\) of (2) on the ambient core, independently of the correction at \(K\).
We have \(d_Ls=1\otimes s-s\otimes1\), by \(d_Lu^*=-u^*\otimes1\) and \(d_Ls_*=0\).
Consequently \(\Gamma=\operatorname{ad}+d_L\), with \(\operatorname{ad}x=x\otimes1-1\otimes x\), agrees with \(\operatorname{ad}\) on \(W,W^*\) and kills \(s\).
The double trace of \(\operatorname{ad}\) vanishes, so restriction to the \(W,s\) core has vacuum \(\mathbb E_M H_u\).
All its values are in the intrinsic coarse space there.
On the even core project each tensor leg of \(\Gamma\) onto \(L^2(Q)\).
This commutes with the outer actions of \(Q\) and preserves double trace.
The resulting derivation is \(\operatorname{ad}\) on \(W_0,W_0^*\) and zero on \(W_1,W_1^*\), since the two tensor legs of \(s\cdot(\operatorname{ad}W_0)\cdot s\) are both odd, and the same holds with \(W_0^*\).
Its vacuum is \(\eta_0=\mathbb E_Q H_u\), hence \(\|\eta_0\|_\infty\le\|H_u\|_\infty\).
The second partial liberation is \(\operatorname{ad}\) minus the first on the represented starred core, so \(\eta_1=-\eta_0\).
For actual normal variables these vacua are precisely the commutators in (1). [Liberation adjoint](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core)

For a separated sum \(k(z,w)=\sum_i f_i(z)g_i(w)\) of bounded Borel functions, denote the joint left-right action at \(W_j\) by \(k_j\).
Conditional expectation onto \(Q\) intertwines both \(W_0\) marginal actions.
Since \(H_u\) is centered and free from the whole matrix base, the polarized free-word identity for \(f(W_0)H_u g(W_0)\) gives
\[
       \|k_0\eta_0\|_2\le\|k_0 H_u\|_2
                         =\|H_u\|_2\,\|k\|_{L^2(\mu\otimes\mu)} .
\]
In particular the resulting measure inequality holds on finite disjoint unions of Borel rectangles, and then on all Borel sets by monotone class.
The same bound extends to every bounded Borel multiplier by the spectral theorem.
The exchanging involution conjugates the two partial liberations and exchanges their vacua by uniqueness, giving the bound at \(W_1\).
Equation (2) makes both estimates in (1) arbitrarily small on the selected pair.
Conversely each pair with infinite cost in the restricted class is itself a counterexample. [Single-pair criterion](Yin_C_F0322_v1.md#statement)

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:46 |
| status | open |
| reason | Fix the conditional obstruction with simultaneous operator-norm and product spectral-density control of both liberation gradients for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Conditional single deficient pair with small bounded liberation gradients and all-scales product domination. |
| argument | [Argument](#argument) | Poisson conjugation, corrected unitary derivative, even liberation and the free marginal tensor estimate. |
| dependency | [Four matrix corners](Yin_C_F0322_v1.md#conditional-expectations-of-the-four-matrix-corners) | Four-step regression for the odd symmetry against its two-dimensional base. |
| dependency | [Small primary pieces](Yin_C_F0322_v1.md#uniform-recovery-on-small-primary-pieces) | The two compressions recovering each finite witness from the four-step regression. |
| dependency | [Ambient primary derivative](Yin_C_F0322_v1.md#placing-bad-tests-in-the-top-semicircular-interval) | Matrix base, diagonal derivative, inverse gaps, trace weights and parameter order. |
| dependency | [Good vacuum](Yin_C_F0322_v1.md#the-good-vacuum-and-its-approximation-to-the-coordinate) | Good coordinate and vacuum comparison before the terminal correction. |
| dependency | [Bad tests and coupling](Yin_C_F0322_v1.md#the-bad-mixed-tests-trace-independence-and-the-reference-pair) | Localization on the original core, infinite costs, bare-dual consequence and quantile coupling. |
| dependency | [Conditional two-block law](Yin_C_F0317_v1.md#coupling-in-operator-norm-and-comparing-two-marginal-blocks) | Expectation of a centered sign perturbation against a marginal observable. |
| dependency | [Matrix trace computation](Yin_C_F0321_v1.md#a-symmetry-with-exact-product-traces) | Exact product traces before adjoining the new free noise. |
| dependency | [Poisson angular vacuum](Yin_C_F0251_v1.md#the-liberation-vacuum-in-free-coordinates) | Both Laurent orientations, the centered bounded angular vacuum and its free extension. |
| dependency | [Even-algebra derivations](Yin_C_F0311_v1.md#derivations-on-the-even-algebra) | Two intrinsic actual joint variables, exchange and cost transfer. |
| dependency | [Liberation adjoint](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Identifying each joint gradient with its normal conjugate-variable commutator. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:53 |
| status | proved |
| reason | Adopt the simultaneous small operator-norm and spectral-density bounds on the two liberation gradients after independent verification of the conditional construction. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Conditional single deficient pair with small bounded liberation gradients and all-scales product domination. |
| argument | [Argument](#argument) | Poisson conjugation, corrected unitary derivative, even liberation and the free marginal tensor estimate. |
| dependency | [Four matrix corners](Yin_C_F0322_v1.md#conditional-expectations-of-the-four-matrix-corners) | Four-step regression for the odd symmetry against its two-dimensional base. |
| dependency | [Small primary pieces](Yin_C_F0322_v1.md#uniform-recovery-on-small-primary-pieces) | The two compressions recovering each finite witness from the four-step regression. |
| dependency | [Ambient primary derivative](Yin_C_F0322_v1.md#placing-bad-tests-in-the-top-semicircular-interval) | Matrix base, diagonal derivative, inverse gaps, trace weights and parameter order. |
| dependency | [Good vacuum](Yin_C_F0322_v1.md#the-good-vacuum-and-its-approximation-to-the-coordinate) | Good coordinate and vacuum comparison before the terminal correction. |
| dependency | [Bad tests and coupling](Yin_C_F0322_v1.md#the-bad-mixed-tests-trace-independence-and-the-reference-pair) | Localization on the original core, infinite costs, bare-dual consequence and quantile coupling. |
| dependency | [Conditional two-block law](Yin_C_F0317_v1.md#coupling-in-operator-norm-and-comparing-two-marginal-blocks) | Expectation of a centered sign perturbation against a marginal observable. |
| dependency | [Matrix trace computation](Yin_C_F0321_v1.md#a-symmetry-with-exact-product-traces) | Exact product traces before adjoining the new free noise. |
| dependency | [Poisson angular vacuum](Yin_C_F0251_v1.md#the-liberation-vacuum-in-free-coordinates) | Both Laurent orientations, the centered bounded angular vacuum and its free extension. |
| dependency | [Even-algebra derivations](Yin_C_F0311_v1.md#derivations-on-the-even-algebra) | Two intrinsic actual joint variables, exchange and cost transfer. |
| dependency | [Liberation adjoint](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Identifying each joint gradient with its normal conjugate-variable commutator. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0332_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

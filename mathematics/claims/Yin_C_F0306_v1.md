---
author: Yin
---

# Encoding a finite coefficient algebra by one noisy selfadjoint coordinate

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let a bounded normal \(Z\) and a finite list of bounded selfadjoint coefficients \(H_1,\ldots,H_m\) generate a finite von Neumann algebra \((R,\tau)\) with faithful normal probability trace.
On \(P=\operatorname{alg}^*(Z,H_1,\ldots,H_m)\) assume a represented outer derivation \(\delta:P\to L^2(R)\otimes_2 L^2(R)\) with \(\delta Z=1\otimes1,\ \delta H_l=0\) and actual vacuum \(\xi=\delta^*(1\otimes1)\).
Let \(C=\mathrm{id}\otimes\tau\).
For every \(p\in P\) of norm at most one and every \(\sigma>0\), there exists a bounded normal \(W\) and a bounded selfadjoint \(Y\) generating a tracial algebra in which the pair has [actual starred conjugate variables](../tasks/Yin_T_F0011_v1.md#contract) at both coordinates.
Writing \(a_W=\sup_{\|x\|\le1,\ x\in\operatorname{alg}^*(W,Y)}\|(\mathrm{id}\otimes\tau')\delta_W(x)\|_2\) and \(\xi_W=\delta_W^*(1\otimes1)\) in that algebra, one has
\[
            \frac{a_W}{\|\xi_W\|_2}
              \ \ge\ \frac{\|C\delta(p)\|_2}{6\|\xi\|_2}-\sigma .       \tag{1}
\]
The constant six is independent of the number of coefficients, their norms and the test word.
Both new coordinates may be taken to be contractions.
The same construction applies to the opposite orientation by starting with \(Z^*\) and its actual distinguished derivative.

In particular, in the extended nonnegative reals, the supremum of the distinguished slice-to-vacuum ratio over actual normal pairs with one selfadjoint second coordinate lies between one sixth of the supremum over all the finite relative inputs above and that relative supremum.
This is a transfer of finite witnesses and uniform bounds, including divergence of the supremum over laws.
It supplies no conclusion that one law attains an infinite supremum.

## Argument

### Matrix derivations and the off-diagonal correction

Rescale the coefficients so \(\|H_l\|\le1\), changing the polynomial expression for \(p\) accordingly.
Put \(k=m+1\), \(t=1/k\), and take the tracial free product of \(R\) with \(k-1\) free standard semicirculars \(s_2,\ldots,s_k\), denoted by \(R'\).
Use the algebraic core obtained by adjoining \((2+H_l)^{1/2}\) to \(P\), then adjoining the free polynomial factors.
The square roots are norm limits of polynomials in the respective \(H_l\) and have derivative zero: on mixed words these approximants converge in the graph by norm convergence of undifferentiated factors and the finite product rule.
The original derivation is closable because the core simple tensors are in its adjoint domain by its actual vacuum and the Leibniz rule.
Thus these limits respect all represented relations and preserve the vacuum identity.
Extend \(\delta\) by zero on the free semicircular factors, calling the resulting derivation \(d_1\).
For \(r\ge2\), let \(d_r\) be the free difference quotient at \(s_r\), killing all other factors.
The extended vacua \(\xi_1=\xi,\ \xi_r=s_r\) follow from the semicircular integration-by-parts identity and the [free-product vacuum argument](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words): on a centered reduced word involving multiple factors a nonempty centered segment remains on at least one trace leg.
Freeness gives faithful representation of these algebraic free products.
The [normal phase computation](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) applies to the single distinguished coordinate, since restriction and projection of its actual vacuum give an actual scalar vacuum.
It gives a diffuse marginal and \(d_1 Z^*=(\bar z-\bar v)/(z-v)\) in the marginal coarse space.

Equip \(\mathcal M=M_k(R')\) with its normalized trace \(\tau_k\); write \(e_r=E_{rr}\) for its diagonal matrix projections.
For each \(d_r\) define a matrix derivation \(L_r\) entrywise on the matrix core: if \(d_r x_{ij}\) is a tensor \(a\otimes b\), its contribution is \(E_{ir}a\otimes E_{rj}b\).
This tensor map for fixed \(i,j,r\) extends to all coarse vectors, scaling their Hilbert norm by \(t\).
For matrix multiplication the two Leibniz sums are precisely the corresponding left and right matrix products, so \(L_r\) is a represented derivation.
Double tracing its value keeps only \(i=j=r\), giving \(t^2(\tau\otimes\tau)d_r x_{rr}\).
Its vacuum for the normalized matrix trace is therefore \(t E_{rr}\xi_r\), of norm \(t^{3/2}\|\xi_r\|_2\).

For \(0<\alpha\) with \(\alpha\|Z\|\le1\), put
\[
 W=E_{11}\alpha Z+\sum_{r=2}^k E_{rr}(10r+s_r),\qquad
 B=\sum_{r=2}^k(E_{1r}+E_{r1})(2+H_{r-1})^{1/2}.
\]
The summand spectra of the normal \(W\) are separated by gaps of at least six.
Each \(e_r\) is therefore a continuous function of \(W\).
The derivation \(L=L_1/\alpha+\sum_{r\ge2}L_r\) kills \(B\) and takes \(W\) to \(\sum_r e_r\otimes e_r\).
In the coarse spectral space of \(W\) use the kernel \(K(z,v)=1/(z-v)\) on distinct summand spectra and zero elsewhere.
It has Hilbert norm at most one (also for \(k=1\), when it is zero).
The inner derivation \(x\mapsto x\cdot K-K\cdot x\) corrects the value at \(W\) to \(1\otimes1\) when added to \(L\).
Its vacuum norm is at most \(2\|K\|_2\): pairing each term against \(1\otimes1\) pairs \(K\) against a tensor with one \(x^*\) leg of Hilbert norm \(\|x\|_2\).
Denote the sum by \(L'\).
Then \(\|L'B\|_2\le2\|B\|\) while its vacuum norm is at most \(t^{3/2}\|\xi\|_2/\alpha+t^{3/2}\sqrt{k-1}+2\), using orthogonality among the auxiliary diagonal entries.
These error bounds are independent of \(\alpha\).

### Making the coefficient an actual selfadjoint coordinate

Adjoin a standard semicircular \(S\) freely to \(\mathcal M\) and set \(Y=B+\varepsilon S\) with \(\varepsilon>0\).
Extend \(L'\) by zero on \(S\); the same reduced-word vacuum argument applies.
Write \(\partial_S\) for the free difference quotient at \(S\) killing the matrix core.
For any base coarse vector \(F\), inner insertion \(I_F\partial_S\) on this free-product core is the derivation taking \(S\) to \(F\) and killing base letters.
It is well-defined by the finite algebraic Leibniz expansion.
For \(F=a\otimes b\) with bounded base coefficients, its double trace equals the double trace of \(\partial_S(a x b)\), which is \(\tau'(S a x b)\).
This identity first uses core base coefficients and extends to arbitrary base Hilbert tensors by linearity and approximation: \(a^*\otimes b^*\mapsto a^* S b^*\) is isometric by semicircular freeness, and insertion into the finite expansion of \(\partial_S x\) is Hilbert-continuous at each fixed \(x\).
Here the stars in the tensor are componentwise, so this gives a conjugate-linear vacuum map in \(F\) of norm one.
Use \(F=-L'B/\varepsilon\).
The corrected derivation \(L'+I_F\partial_S\) kills the selfadjoint \(Y\) and takes \(W\) to \(1\otimes1\).

Its value on \(W^*\) is the forced normal phase in the coarse space of \(W\).
Indeed the scalar law of \(W\) is diffuse, and differentiating \(WW^*=W^*W\) fixes the value by the injectivity of the outer spectral gap on the whole ambient coarse correspondence.
Thus all four generator values lie in the coarse space of \(M' = W^*(W,Y)\) and the derivative restricts there on \(\operatorname{alg}^*(W,Y)\).
Projecting the ambient vacuum into \(L^2(M')\) gives an actual vacuum satisfying
\[
                  \|\xi_W\|_2\le t^{3/2}\|\xi\|_2/\alpha
                      +t^{3/2}\sqrt{k-1}+2+2\|B\|/\varepsilon .          \tag{2}
\]
At the second coordinate \(\partial_S/\varepsilon\) kills \(W,W^*\) and takes \(Y\) to \(1\otimes1\); it restricts with projected vacuum \(S/\varepsilon\).
This verifies actuality at both coordinates.
Write \(\tau'\) also for the inherited probability trace.

### Recovering the test inside the spectral corner

Let \(e=e_1\), of trace \(t\).
Use the [relative corner theorem](Yin_C_F0301_v1.md#statement) for \(W\) in this actual pair, with corner unit \(e\), \(W_e=\alpha E_{11}Z\) and coefficient algebra \(e A_{\rm out} e\), \(A_{\rm out}=\operatorname{alg}^*(e,(1-e)W,Y)\).
For \(r\ge2\) the spectral projection \(e_r\) is a norm limit of starred polynomials in \((1-e)W\) and its adjoint by separation of the spectra (including zero).
Thus \(H_l^\varepsilon=eY e_{l+1}Ye-2e\) is a norm limit of corner coefficients of zero derivative.
In the ambient corner one has
\[
        \|H_l^\varepsilon-E_{11}H_l\|
           \le 2\varepsilon\|S\|\|B\|+\varepsilon^2\|S\|^2 ,
\]
since \(e B e_{l+1}B e=E_{11}(2+H_l)\).
These elements and the approximation error inside the ambient free product are independent of \(\alpha\).

Represent the chosen witness by a fixed polynomial and evaluate it at \(W_e/\alpha,H_l^\varepsilon\) with unit \(e\), calling the value \(p^\varepsilon\).
The relative derivative \(\delta_e\) normalized in the trace \(\tau_e=\tau'/t\) has \(\alpha\delta_e(W_e/\alpha)=e\otimes e\); on its adjoint this scaled derivative has exactly the original phase at \(Z\), since \(\alpha>0\).
It vanishes on the approximating corner coefficients.
Consequently \(p^\varepsilon\) and its assigned derivative are joint norm/coarse-graph limits on the relative core, by the same product-rule approximation as above.
On expanding the fixed word, all coefficients converge in operator norm as \(\varepsilon\downarrow0\), and the two nonzero generator tensors for the scaled derivative agree isometrically with the original tensors under the normalized embedding \(x\mapsto E_{11}x\).
Hence in the ambient corner \(p^\varepsilon\to E_{11}p\) in norm and \(C_e\alpha\delta_e p^\varepsilon\to E_{11}C\delta p\) in trace Hilbert norm, with \(C_e=\mathrm{id}\otimes\tau_e\).
These comparisons use the relative core limits; multiplying the finite-word expressions by \(\alpha\) removes their entire \(\alpha\)-dependence.

Let \(a_e\) be the relative core slice norm.
Approximating on the core and dividing the inputs by the maximum of one and their operator norm shows that for any \(\eta>0\), all sufficiently small fixed \(\varepsilon>0\) give \(\alpha a_e\ge\|C\delta p\|_2-\eta\), simultaneously for all admissible \(\alpha>0\).
If \(a_W<\infty\), the [cutoff bound](Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) gives \(\|T_r\|\le3a_W\) at every radius.
Both the compressed cutoff supremum \(k(F)\) and its value \(B_e\) on \(e\) in (4) of the corner theorem are at most \(3a_W\).
Thus \(t^{3/2}a_e\le6a_W\); the inequality in the extended reals also holds for \(a_W=\infty\).
Combine this with (2), first fixing \(\varepsilon\) for the witness and then sending \(\alpha\downarrow0\).
The original vacuum norm is strictly positive since \(\langle\xi,Z\rangle=1\); the same applies to the new distinguished vacuum.
This proves (1) after choosing \(\eta\) sufficiently small.
The upper bound between the two suprema follows since each actual pair already gives a relative input.
Finally, positive rescaling of the second coordinate preserves the distinguished derivative, and positive rescaling of the first scales its distinguished derivative and vacuum inversely on the same core.
These rescalings preserve actuality at the other coordinate and give the optional contraction normalization.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:11 |
| status | open |
| reason | Fix the transfer from one finite relative test to a normal pair with a selfadjoint noisy coefficient and a dimension-independent comparison. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite-witness transfer, coefficient-independent constant, and comparison of the extended suprema. |
| argument | [Argument](#argument) | Matrix lifts, scaled vacuum and cross-spectrum correction, semicircular noise and test recovery in the normalized spectral corner. |
| dependency | [Free-product vacuum preservation](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Centered-word extension of the distinguished vacuum and free semicircular difference quotients. |
| dependency | [Normal phase and diffuseness](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Scalar and ambient coarse spectral-gap injectivity and the original forced adjoint-generator tensor. |
| dependency | [Relative corner theorem](Yin_C_F0301_v1.md#statement) | Normalized relative derivative on the corner of the actual pair, its coefficient algebra and the first inequality in (4). |
| dependency | [Global normal cutoffs](Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) | Uniform bound \(3a_W\) on the fixed-radius extensions for finite original slice norm. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:17 |
| status | proved |
| reason | Independent review verified the matrix trace normalization, correction by free noise, recovery of all old tests in a spectral corner and the coefficient-independent comparison of suprema. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Finite-witness transfer, coefficient-independent constant, and comparison of the extended suprema. |
| argument | [Argument](#argument) | Matrix lifts, scaled vacuum and cross-spectrum correction, semicircular noise and test recovery in the normalized spectral corner. |
| dependency | [Free-product vacuum preservation](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Centered-word extension of the distinguished vacuum and free semicircular difference quotients. |
| dependency | [Normal phase and diffuseness](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Scalar and ambient coarse spectral-gap injectivity and the original forced adjoint-generator tensor. |
| dependency | [Relative corner theorem](Yin_C_F0301_v1.md#statement) | Normalized relative derivative on the corner of the actual pair, its coefficient algebra and the first inequality in (4). |
| dependency | [Global normal cutoffs](Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) | Uniform bound \(3a_W\) on the fixed-radius extensions for finite original slice norm. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0315_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

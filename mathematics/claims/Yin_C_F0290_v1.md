---
author: Yin
---

# A free Haar unitary transformed by a disk-valued function of a normal coordinate

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(A=L^\infty(\mu)=W^*(Z)\), where \(Z(z)=z\) and \(\mu\) is a compactly supported diffuse probability measure on the plane.
Let \(W\) be a Haar unitary free from \(A\) in their finite tracial free product \((M,\tau)\).
For a Borel function \(h=h(Z)\) with \(|h|<1\) almost everywhere put \(D=(1-|h|^2)^{1/2}\), \(a=D^{-1}\), and define the Möbius transform
\[
              Y=h+D(1+Wh^*)^{-1}WD .                                      \tag{1}
\]
The inverse in (1) is taken in the tracial algebra of measurable affiliated operators.
Then \(Y\) is unitary, \(W^*(Z,Y)=M\), and its conditional spectral distribution at \(Z=z\) is Poisson measure on the unit circle with mean \(h(z)\).
The following three conditions are equivalent.

1. The pair \((Z,Y)\) has [actual starred conjugate variables](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
2. The pair has a strong dual system, with the operators and their Hilbert adjoints defined on all bounded vectors.
3. The scalar divided difference of \(Z\) has an actual conjugate variable \(\zeta\), and both quantities
   \[
    I=\int\frac{d\mu(z)}{1-|h(z)|^2},\qquad
    J=\iint_{z\ne w}
       \frac{|h(z)-h(w)|^2\,d\mu(z)d\mu(w)}
            {|z-w|^2(1-|h(z)|^2)(1-|h(w)|^2)}
                                                                            \tag{2}
   \]
   are finite.

When these hold, the actual vacua have squared norms
\[
         \|\xi_Z\|_2^2=\|\zeta\|_2^2+2J,\qquad
         \|\xi_Y\|_2^2=I^2+(I-1)^2.                                      \tag{3}
\]
Both original right slices have finite column cost in both adjoint orientations.
Here the column cost of a slice \(E\) is the supremum of \((\sum_j\|Ep_j\|_2^2)^{1/2}\) over finite columns of starred polynomials with \(\|\sum_jp_j^*p_j\|\le1\).
The negatives of the original right-slice closures give the strong duals in the generator-first convention.

For normalized area on the unit disk and \(h(z)=1-|z|^\alpha\), \(\alpha>0\), the pair has both properties exactly when \(\alpha<2\).
For every \(\alpha>0\) the pair admits the common character \((Z,Y)\mapsto(0,1)\), with the entire circle of limiting secant directions at the base point.

## Argument

### Unitarity, generation and conditional law at the endpoint

Write \(h_s=sh\), \(D_s=(1-|h_s|^2)^{1/2}\), \(a_s=D_s^{-1}\), and take \(Y_s\) from (1) with \(0<s<1\).
The matrix \(\left(\begin{smallmatrix}h_s&D_s\\D_s&-h_s^*\end{smallmatrix}\right)\) is unitary.
Applied to a pair \((x,b)\) with \(b=W(D_s x-h_s^* b)\), it gives \((Y_s x,W^*b)\), where \(b=(1+Wh_s^*)^{-1}WD_s x\).
Its norm identity makes \(Y_s\) an isometry, hence unitary by finiteness.

Set \(k=\|h\|_2<1\).
For each \(n\ge0\), \(\|(Wh^*)^n\|_2=k^n\).
Indeed the copies \(W^\ell A W^{-\ell}\) at distinct integer indices are free, by expanding an alternating word of centered letters as a reduced Haar word.
Moving the \(W\)'s to the right expresses the power as a product of one copy of \(h^*\) in each of \(n\) distinct factors followed by \(W^n\).
The squared norm of a product of one letter from each distinct free factor is the product of their squared norms, by cyclicity and successively factoring off the first square under the trace.
Thus the terms \(D_s(-Wh_s^*)^n W D_s\) in the Neumann expansion have \(L^2\) norm at most \(k^n\).
Each term converges in \(L^2\) as \(s\uparrow1\), giving a limit \(Y\) of the \(Y_s\) in \(L^2\).
The uniform unitary bounds and traciality give bounded strong-star convergence, so \(Y\) is unitary.
The bare series \(\sum_{n\ge0}(-Wh^*)^n\) also converges in \(L^2\), and multiplication by \(1+Wh^*\) on either side telescopes to the identity.
This proves (1) with its stated inverse.

Multiplication of (1) in the affiliated algebra gives
\[
             (1+Wh^*)aY=ah+Wa,\qquad
             W=a(Y-h)(1-h^*Y)^{-1}D.
\]
Here \(\|h^*Yv\|_2<\|v\|_2\) for \(v\ne0\), since \(D\) has full support.
Consequently \(1-h^*Y\) has zero kernel, and its polar supports have equal trace, so it has an affiliated inverse in \(W^*(Z,Y)\).
The right side recovers the bounded \(W\) in this same von Neumann algebra.

The automorphisms fixing \(A\) and multiplying \(W\) by scalar phases preserve \(\tau\), by the free product and Haar law.
For \(n\ge1\) the uniformly convergent positive-power expansion at \(s<1\) therefore gives \(\mathbb E_A Y_s^n=h_s^n\), as each nonconstant term acquires a nonzero positive phase exponent.
Passing to the limit gives \(\mathbb E_A Y^n=h^n\).
The conjugated moments follow by taking adjoints, and trigonometric polynomial density identifies the asserted Poisson law, of density \((1-|h(z)|^2)/|u-h(z)|^2\) against normalized Haar measure at \(u\).
The marginal of \(Y\) is diffuse and \(|\tau(Y)|=|\tau(h)|<1\).

For an actual pair the [conditional product-density estimate](Yin_C_F0281_v1.md#the-exact-row-and-column-norms), applied in the \(Z\)-conditional direction with the test \(u\mapsto u\), gives an integrable upper bound for
\[
                      \frac{|h(z)-\tau(Y)|^2}{1-|h(z)|^2}.
\]
The numerator is bounded below on \(|h|>(1+|\tau(Y)|)/2\), and the denominator is bounded below on its complement.
Thus actual conjugate variables require \(I<\infty\).

### Four elementary Haar derivatives

Write \(\mathcal Q=A*\mathbb C[W,W^{-1}]\) for its represented algebraic free product.
All derivatives use the outer bimodule actions, and inner products are linear in the second variable.
For \(l,r\in\{0,1\}\) and a finite separated base tensor \(b=\sum_j f_j\otimes g_j\), let \(d_{lr,b}\) kill \(A\) and take \(W\) to \(\sum_j W^l f_j\otimes g_j W^r\).
The inverse rule determines the derivative of \(W^*\).
The same prescription makes sense on each word for any \(b\in L^2(\mu^2)\) by Hilbert tensor approximation.
For \(b=1\otimes1\) the scalar Haar right slice on \(W^n\), \(n>0\), retains only the cut whose right exponent is zero, giving \(W^{n-1+l}\) if \(r=0\) and zero if \(r=1\).
For \(n\le-1\) the inverse rule gives \(-W^{n+l}\) if \(r=1\) and zero if \(r=0\).
All four slices kill \(1\) and have Hilbert-space norm at most one.
Their scalar vacua \(v_{lr}\) are respectively \(v_{00}=W,\ v_{10}=v_{01}=0,\ v_{11}=-W^*\).

For centered \(v\in L^2(W^*(W))\), write \(J_v(f\otimes g)=fvg\).
Freeness gives \(\langle J_v(b),J_t(c)\rangle=\langle v,t\rangle\langle b,c\rangle\) by the conditional expectation of \(v^* x t\) onto \(A\) for \(x\in A\).
The [free terminal-block estimate](Yin_C_F0277_v1.md#a-necessary-inverse-scale-and-the-conjugate-variable-of-the-new-coordinate), formula (3), gives
\[
      d_{lr,b}^*(1\otimes1)=J_{v_{lr}}(\bar b),\qquad
      c(Cd_{lr,b})\le K\|b\|_{L^2(\mu^2)},\qquad C=\mathrm{id}\otimes\tau , \tag{4}
\]
with an absolute \(K\), for these four Haar derivatives.
In that estimate only the scalar right-slice bound, its centered scalar vacuum and the reduced-word product decomposition are used.
Here the scalar derivation takes \(W\) to \(W^l\otimes W^r\), so its inner insertion by \(f\otimes g\) indeed gives \(W^l f\otimes gW^r\).
On a reduced word \(q\,t\,x\) with terminal centered Haar block \(t\) and trailing \(x\in A\), the slice retains \(q\,E_{lr}(t)\int b(\cdot,w)x(w)\,d\mu(w)\), where \(E_{lr}\) is that scalar slice.
This is exactly the terminal expression to which the cited column bound applies.
For a finite separated \(b\), cyclicity gives its vacuum formula from the scalar vacuum, with both base coefficients conjugated and their order preserved.
Both conclusions pass to Hilbert tensor limits on each fixed word.

### The chain rule and the two vacua

First take \(\|h\|_\infty<1\), suppressing the subscript \(s\).
Set \(P=(1+Wh^*)a,\ Q=a(1+h^*W)\).
Any derivation \(d\) killing \(A\) satisfies \(dY=P^{-1}\cdot(dW)\cdot Q^{-1}\) by differentiating (1).
This calculation holds for the norm-convergent rational expression in (1) by termwise differentiation of the Neumann series, whose differentiated terms are bounded by a constant times \(n\|h\|_\infty^{n-1}\).
The same argument handles its adjoint.
Thus the normalized derivative at \(Y\) is obtained with \(dW=P\otimes Q\).
Expanding it gives the four coefficients of (4), with \(b_{00}=a\otimes a,\ b_{10}=ah^*\otimes a,\ b_{01}=a\otimes ah^*,\ b_{11}=ah^*\otimes ah^*\).
In particular its vacuum is
\[
                     \psi=J_W(a\otimes a)-J_{W^*}(ah\otimes ah).           \tag{5}
\]

Let \(\Gamma x=x\otimes1-1\otimes x\), and let \(\gamma^0\) act by \(\Gamma\) on \(A\) and kill \(W\).
Both have zero vacuum, by the trace identity for an inner difference and the centered free-word calculation for \(\gamma^0\).
To obtain partial liberation \(\gamma\) at \(Z\), take \(\gamma=\Gamma-d\) where \(d\) kills \(A\) and has \(dY=\Gamma Y\).
The chain rule gives \(dW=PY\otimes Q-P\otimes YQ\), where
\[
                 PY=ah+Wa,\qquad YQ=ha+aW.
\]
Writing \(x=h(z)\), \(y=h(w)\) and \(A_{zw}=a(z)a(w)\), the coefficients of \(d\) satisfy
\[
 \beta_{00}=(x-y)A_{zw},\qquad \beta_{11}=(\bar y-\bar x)A_{zw},\qquad
 \beta_{10}=(1-\bar x y)A_{zw},\qquad \beta_{01}=-(1-x\bar y)A_{zw}.
                                                                            \tag{6}
\]
The signs refer to the left and right powers of \(W\) in the definition of \(d_{lr,b}\).
By (4) the liberation vacuum is
\[
                 \eta=-J_W(\overline{\beta_{00}})
                           +J_{W^*}(\overline{\beta_{11}}).                \tag{7}
\]
The norm and vacuum estimates from \(\mathcal Q\) hold on all finite target words by approximating \(Y,Y^*\) in operator and derivative norms by their Neumann polynomials over \(A\).
For each fixed approximating family the same holds for products by the outer rule.

Now suppose only \(|h|<1\) almost everywhere and \(I<\infty\).
Use the preceding formulas for \(h_s\).
All coefficient kernels in (5)–(7) converge in \(L^2(\mu^2)\), by domination by \(2a(z)a(w)\).
Hence \(\psi_s,\eta_s\) converge in \(L^2(M)\) to (5), (7).
For each formal mixed starred word its value at \((Z,Y_s)\) converges boundedly strongly-star to its value at \((Z,Y)\).
Its derivative at \(Y_s\) converges in coarse norm by the values \(0\) on \(Z,Z^*\), \(1\otimes1\) on \(Y_s\) and \(-Y_s^*\otimes Y_s^*\) on \(Y_s^*\), and the same applies to liberation using \(\Gamma\) on the base and zero on \(Y_s,Y_s^*\).
The limiting prescriptions therefore have vacuum pairings on all formal words with \(\psi,\eta\).
For a relation \(p=0\), applying the limiting pairing to \(bpc\) and expanding gives zero double trace for \(b\cdot dp\cdot c\) for every pair of polynomial multipliers.
The resulting simple tensor tests are dense since \(W^*(Z,Y)=M\), so \(dp=0\).
This gives actual adjoint vectors on the entire original core.

The two images under \(J_W,J_{W^*}\) are orthogonal, and the left and right spectral variables of \(Z\) multiply the two base coefficients of each \(J_v\) separately.
Thus the measure of \(\eta\) for these two actions has density \(2|x-y|^2 A_{zw}^2\) with respect to \(\mu^2\).
The [normal inverse-gap theorem](Yin_C_F0238_v1.md#statement) now gives the exact base-coordinate criterion and the first formula of (3).
The squared norm of (5) is \(I^2+(I-1)^2\), since \(\|ah\|_2^2=I-1\).
This proves the equivalence between items 1 and 3 together with the asserted norms.

### Uniform column costs and the limit at the unit circle

Assume item 3 and first work with \(h_s\).
In the following estimates the constants are independent of \(s\).
For brevity use \(h_s,D_s,a_s\) in all the coefficients below.
By (4) the normalized \(Y_s\) right slice has cost at most \(4KI\), as each of its four coefficient norms is at most \(I\).
To treat the base coordinate put \(u=z-w\), \(t_\epsilon=\bar u/(|u|^2+\epsilon^2)\), and use inner spectral multiplication \(I_b(f\otimes g)=f b_1\otimes b_2g\) when \(b=b_1\otimes b_2\), extended for bounded marginal symbols.
On \(\mathcal Q\) the difference \(\gamma-\gamma^0\) equals minus the sum of the four Haar derivatives with kernels
\[
       \beta_{00},\qquad \beta_{11},\qquad \beta_{10}-1,\qquad \beta_{01}+1 .
\]
Indeed \(\Gamma-\gamma^0\) kills \(A\) and takes \(W\) to \(W\otimes1-1\otimes W\).
All four kernels are bounded in modulus by \(\sqrt2 |x-y|A_{zw}\).
For the last two, set \(d_x=(1-|x|^2)^{1/2}\).
The real part of \(1-\bar x y-d_xd_y\) is nonnegative by Cauchy–Schwarz on the unit vectors \((x,d_x),(y,d_y)\).
It is at most \(|x-y|\), since \(|1-\bar x y|^2=d_x^2 d_y^2+|x-y|^2\).
Also \(|\operatorname{Im}(\bar x y)|\le|x-y|\), proving the bound.
Multiplication by \(I_{t_\epsilon}\) multiplies the four kernels by \(t_\epsilon\), as is seen first on \(W\) and then on all words.
The resulting kernel norms are bounded by \(\sqrt{2J}\), since replacing \(h\) by \(sh\) only decreases its integrand in (2).
Thus (4) bounds the four correction terms with total cost at most \(4K\sqrt{2J}\).

For the remaining term \(CI_{t_\epsilon}\gamma^0\), the [free reference cutoff estimate](Yin_C_F0265_v1.md#removing-the-cutoff-on-the-target-polynomial-core) bounds its cost by \(3c_0\) for the finite free reference cost \(c_0\) at \(Z\) on the core generated by \(Z,W\).
To pass the estimate to \(\mathcal Q\), take uniformly bounded strong-star polynomial approximations to its finitely many base letters.
These approximations converge in the \(\gamma^0\) graph because \(\gamma^0=\Gamma\) on those letters.
The smooth column clipping in the cited proof retains the input column bound in that graph.
For fixed \(s<1\), the Neumann polynomials approximate every target word in norm and derivative norm for \(\gamma^0,\gamma\), so both the reference and correction estimates hold on the entire target column.
On that core \(\gamma=I_u\partial_Z\), by the actual normal derivative prescription.
As \(\epsilon\downarrow0\), \(I_{t_\epsilon u}\to1\) strongly on the coarse correspondence since the joint measures of the two inner marginal actions are absolutely continuous with respect to \(\mu^2\), which gives zero mass to the diagonal.
Consequently the unregularized base cost is bounded by \(3c_0+4K\sqrt{2J}\).

For the limiting pair, along \(s\uparrow1\) the derivative of each fixed polynomial converges in coarse norm for either coordinate.
For the \(Y\)-derivative this was shown in the vacuum passage.
For the \(Z\)-derivative the values on \(Z,Z^*\) are the fixed scalar divided difference and the two values on \(Y_s,Y_s^*\) vanish, so the same product-rule argument applies.
To retain the column norm, fix a target column \(p\) of norm at most one, put \(p_s=p(Z,Y_s)\) for its formal expression and \(S_s=p_s^*p_s\).
Fix \(\epsilon>0\) and a smooth real function \(f\) equal to one near \([0,1]\) with \(\sqrt{x}|f(x)|\le1+\epsilon\) on a common interval containing all spectra of \(S_s\).
For a polynomial \(g\), \(\partial g(S_s)\) equals the divided difference \(g^{[1]}\) in the left and right outer \(S_s\)-actions applied to \(\partial S_s\).
The errors for \(C^1\)-polynomial approximation of \(f\) are bounded uniformly by the supremum derivative error times \(\sup_s\|\partial S_s\|_2<\infty\).
The outer multipliers for a fixed polynomial converge strongly-star, and \(f^{[1]}\) vanishes on the limiting spectrum square in \([0,1]^2\).
The product rule now gives convergence of the approximated derivatives of \(p_s f(S_s)\) to \(\partial p\), while the clipped column norm is at most \(1+\epsilon\).
Apply the uniform column estimates using polynomial approximants first at each \(s\), then take \(s\uparrow1\) and \(\epsilon\downarrow0\).
This proves both right-column bounds on the original pair.

Finally \(Y^*=\phi_{h^*}(W^*)\) where \(\phi_h(W)\) denotes (1), by the identity \(W^*(1+hW^*)^{-1}=(1+W^*h)^{-1}W^*\).
Conjugating the base spectral variable and \(h\) preserves (2) and its scalar vacuum condition, by flip-adjoint conjugation.
The same bounds therefore hold for the adjoint tuple, giving the original left-slice bounds by the flip-adjoint derivative.
The [two-contraction theorem](Yin_C_F0072_v1.md#statement) gives both original canonical domains and the strong duals.
The reverse implication follows from the [normal strong-domain theorem](Yin_C_F0070_v1.md#statement).

### A sharp disk threshold

The area law has an [actual scalar vacuum](Yin_C_F0267_v1.md#a-disk-with-vanishing-one-dimensional-density).
For \(h(z)=1-|z|^\alpha\) one has \(D(z)^2=|z|^\alpha(2-|z|^\alpha)\), so \(I<\infty\) precisely for \(\alpha<2\).
For radial variables \(r=|z|>v=|w|\), the angular mean of \(|z-w|^{-2}\) is \((r^2-v^2)^{-1}\) by the geometric series.
With \(v=rt\), radial integration gives \(J\) comparable, up to absolute positive factors, to
\[
            \int_0^1 r\,dr\int_0^1
                 \frac{t^{1-\alpha}(1-t^\alpha)^2}{1-t^2}\,dt .
\]
The inner integrand is comparable to \(t^{1-\alpha}\) near zero and to \(1-t\) near one, proving the same threshold.
For \(e_r=1_{[0,r]}(|Z|)\), \(\tau(e_r)=r^2\), and the conditional expectation gives
\[
     \frac{\|(Y-1)e_r\|_2^2}{\tau(e_r)}
       =\frac{\tau(e_r(2-h-h^*))}{r^2}=\frac4{\alpha+2}r^\alpha,\qquad
     \frac{\|Ze_r\|_2^2}{\tau(e_r)}=\frac{r^2}{2}.
\]
The two adjoints have the same errors.
The normalized vectors therefore approximate simultaneous eigenvectors for the starred generators at \((0,1)\).
Telescoping every word shows that evaluation at this point extends to a character on \(C^*(Z,Y)\).
The base spectrum contains the entire disk, with chords in every direction at each sufficiently small radius.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T15:52 |
| status | open |
| reason | Fix the Möbius coupling criterion and its original-domain and singular-parameter arguments for separate proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact joint criterion, vacuum norms, original canonical domains and sharp disk threshold for the stated Haar coupling. |
| argument | [Argument](#argument) | Affiliated inverse and Poisson fibers, four Haar derivatives, inverse-gap integral, uniform column estimates and endpoint passage. |
| dependency | [Conditional product densities](Yin_C_F0281_v1.md#the-exact-row-and-column-norms) | Necessary inverse-defect integrability from the \(Z\)-conditional variance. |
| dependency | [Free terminal estimate](Yin_C_F0277_v1.md#a-necessary-inverse-scale-and-the-conjugate-variable-of-the-new-coordinate) | Column and vacuum bounds for base insertions into a scalar free derivative under the displayed scalar-slice hypotheses. |
| dependency | [Liberation recovery](Yin_C_F0238_v1.md#statement) | Distinguished normal vacuum on the represented starred core from its marginal and inverse-gap liberation integral. |
| dependency | [Reference cutoff](Yin_C_F0265_v1.md#removing-the-cutoff-on-the-target-polynomial-core) | Free soft column bound and norm-preserving smooth approximation in the liberation graph. |
| dependency | [Canonical domains](Yin_C_F0072_v1.md#statement) | Both canonical domains from the two oriented slice bounds. |
| dependency | [Strong-to-actual implication](Yin_C_F0070_v1.md#statement) | Necessity of the actual vacua under the strong dual hypothesis. |
| dependency | [Area marginal](Yin_C_F0267_v1.md#a-disk-with-vanishing-one-dimensional-density) | Scalar vacuum for the disk realization. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T16:03 |
| status | proved |
| reason | Independent review verified the represented endpoint construction, both exact vacuum norms, and both original canonical domains throughout the disk-valued Haar coupling. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact joint criterion, vacuum norms, original canonical domains and sharp disk threshold for the stated Haar coupling. |
| argument | [Argument](#argument) | Affiliated inverse and Poisson fibers, four Haar derivatives, inverse-gap integral, uniform column estimates and endpoint passage. |
| dependency | [Conditional product densities](Yin_C_F0281_v1.md#the-exact-row-and-column-norms) | Necessary inverse-defect integrability from the \(Z\)-conditional variance. |
| dependency | [Free terminal estimate](Yin_C_F0277_v1.md#a-necessary-inverse-scale-and-the-conjugate-variable-of-the-new-coordinate) | Column and vacuum bounds for base insertions into a scalar free derivative under the displayed scalar-slice hypotheses. |
| dependency | [Liberation recovery](Yin_C_F0238_v1.md#statement) | Distinguished normal vacuum on the represented starred core from its marginal and inverse-gap liberation integral. |
| dependency | [Reference cutoff](Yin_C_F0265_v1.md#removing-the-cutoff-on-the-target-polynomial-core) | Free soft column bound and norm-preserving smooth approximation in the liberation graph. |
| dependency | [Canonical domains](Yin_C_F0072_v1.md#statement) | Both canonical domains from the two oriented slice bounds. |
| dependency | [Strong-to-actual implication](Yin_C_F0070_v1.md#statement) | Necessity of the actual vacua under the strong dual hypothesis. |
| dependency | [Area marginal](Yin_C_F0267_v1.md#a-disk-with-vanishing-one-dimensional-density) | Scalar vacuum for the disk realization. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0299_v1.md#finding) | The complete fixed proof, all seven direct Claim inputs, and the strict disk threshold and common character. |

---
author: Yin
---

# All symmetrized cofactor edges can share a conditional scalar atom

This ordinary proof-development finding for Yin on 2026-11-06 tests the joint output of the actual two-border cofactor construction in the real three-factor part of [F0012](../tasks/Yin_T_F0012_v3.md#contract).
The algebra and elementary probability bounds below were checked during ordinary collaboration; this is not an independent review or a Task counterexample.
It preserves a failure of a uniform conditional graph estimate, including its exact allowed background and probability, rather than an assertion about typical independent Wigner backgrounds.
The [proved aggregate energy theorem](../claims/Yin_C_F0194_v15.md#statement) remains valid and is quantitatively compatible with this example.

The [earlier actual-minor atom](Yin_L_F0066_v5.md#actual-minor-singular-atom) concerns a different two-channel quadratic pencil, one surviving Rademacher row and an exact conditional singularity probability one half.
Here two original borders survive, the object is every off-diagonal entry of the actual three-factor symmetrized augmented adjugate, and an explicit simultaneous zero event has probability of order \(N^{-1/2}\).
The full product need not be singular; a strengthened guard-compatible version below has shifted product exactly \(-zI_N\).
Thus the new common-factor mechanism and its coefficient normalization are not supplied by that earlier finding.

<a id="allowed-background"></a>
## One fixed law and a legal conditioning event

Let \(m=N-1\ge2\), fix \(z\in\mathbb C\setminus\{0\}\), and take three independent real symmetric Wigner inputs whose independent raw upper entries, including diagonals, all have the one fixed law
\[
 \mathbb P(\xi=0)=\frac12,\qquad
 \mathbb P(\xi=\sqrt2)=\mathbb P(\xi=-\sqrt2)=\frac14.
\]
The law is centered, variance one and bounded, and every input is normalized by the original \(\sqrt N\).
Put \(a=\sqrt{2/N}\).
At the first omitted index, condition on
\[
 \Gamma_N=\{A_0=0,\ B_0=C_0=aI_m,\ b=c=0\}.
 \tag{Joint-atom-background}
\]
Here \(A_0,B_0,C_0\) are the three principal blocks, and \(b,c\) are the exposed diagonal entries of the second and third inputs.
The remaining second and third borders retain the independent original laws
\[
 x=aX,\qquad y=aY,\qquad
 \mathbb P(X_j=0)=\mathbb P(Y_j=0)=\frac12,
\]
\[
 \mathbb P(X_j=1)=\mathbb P(X_j=-1)
 =\mathbb P(Y_j=1)=\mathbb P(Y_j=-1)=\frac14.
\]
In particular these are not Rademacher borders, and the fair-sign conditional-mask statements of the Rademacher copy construction are not being imported.

Every specified entry in \(\Gamma_N\) is a support atom.
The first principal block contributes \(2^{-m(m+1)/2}\).
Each of the other two principal blocks contributes \(2^{-2m-m(m-1)/2}\), and \(b=c=0\) contributes \(2^{-2}\).
Thus
\[
 \mathbb P(\Gamma_N)=2^{-(3m^2+7m+4)/2}.
 \tag{Joint-atom-background-probability}
\]
No conditioning on an event involving \(x,y\) has occurred.
The rare probability of this background will remain separate from the conditional probability computed below.

<a id="joint-cofactor-formula"></a>
## The complete augmented cofactor matrix has an explicit common factor

Write
\[
 B=\begin{pmatrix}b&x^T\\x&B_0\end{pmatrix},\qquad
 C=\begin{pmatrix}c&y^T\\y&C_0\end{pmatrix},\qquad
 P=BC,\qquad q=x^Ty.
\]
On the branch where \(B,C\) and \(p=P_{11}\) are invertible, set \(H=(P^{-1})_{\widehat1,\widehat1}\).
Block inversion and the determinant formula give
\[
 H^{-1}=P_{\widehat1,\widehat1}
             -P_{\widehat1,1}P_{1,\widehat1}/p,\qquad
 \det H=p/\det P.
\]
Consequently
\[
 \operatorname{adj}H
 =\frac{pP_{\widehat1,\widehat1}
               -P_{\widehat1,1}P_{1,\widehat1}}{\det P}.
 \tag{Joint-atom-inverse-minor-adjugate}
\]
This directly derived block identity is sufficient; no external minor identity is used as an additional theorem.

Because \(A_0=0\), the actual shifted minor is \(D_i=-zH\).
Use the [actual augmented-cofactor identity](../claims/Yin_C_F0194_v15.md#actual-border-algebra),
\(\mathcal A=s_Bs_C\operatorname{adj}D_i\), and
\(\det P=s_Bs_C\det B_0\det C_0\).
For general invertible \(B_0,C_0\) this yields
\[
 \mathcal A
 =\frac{(-z)^{m-1}}{\det B_0\det C_0}
 \left[
  qxy^T+(bc+q)B_0C_0
  -cxx^TC_0-bB_0yy^T-B_0yx^TC_0
 \right].
 \tag{Joint-atom-full-cofactor}
\]
Indeed the four blocks of \(BC\) are
\[
 p=bc+q,\quad
 P_{\widehat1,\widehat1}=xy^T+B_0C_0,\quad
 P_{\widehat1,1}=cx+B_0y,\quad
 P_{1,\widehat1}=by^T+x^TC_0,
\]
and their multiplication cancels the \(bc\,xy^T\) terms.
The resulting identity is polynomial in the borders and exposed diagonals with the backgrounds fixed, so it also holds off the initial invertible branch.

On \(\Gamma_N\), put
\[
 \gamma_N=(-z)^{m-1}a^{-2m}\ne0.
\]
Write \(\operatorname{sym}H=(H+H^T)/2\) and \(\mathcal Q=\operatorname{sym}\mathcal A\), with ordinary transposes throughout.
Then the entire matrices are
\[
 \mathcal A(x,y)=\gamma_N[qxy^T+qa^2I_m-a^2yx^T],
 \qquad
 \mathcal Q(x,y)=\gamma_N[(q-a^2)\operatorname{sym}(xy^T)+qa^2I_m].
 \tag{Joint-atom-scalar-background}
\]
In particular, all output edges share the same scalar factor:
\[
 \mathcal Q_{jk}(x,y)
 =\frac{\gamma_N}{2}(x^Ty-a^2)(x_jy_k+x_ky_j),
 \qquad j<k.
 \tag{Joint-atom-all-output-factor}
\]
This is the full polynomial, including the quartic layer, rather than only its odd-odd projection.

The shifted background itself is \(D_0=-za^{-2}I_m\), which is invertible.
Its off-diagonal deleted cofactors vanish, so the individual deleted-block inverse formulas from the earlier copy calculation are not applicable at this background.
The derivation above avoids those inverses and supplies the actual polynomial on that allowed branch.
The aggregate theorem imposes no nonzero-deleted-cofactor assumption.

<a id="joint-copy-difference"></a>
## The complete rectangular difference keeps shared scalar couplings

For independent copies \(x',y'\), use
\[
 u=x+x',\quad d=x-x',\qquad v=y+y',\quad e=y-y'.
\]
Let \(\Delta\) denote the rectangular four-corner difference and let \(\operatorname{off}\) remove the diagonal.
Expanding the rectangular difference of (Joint-atom-scalar-background) gives the exact joint identity
\[
 \begin{aligned}
 \gamma_N^{-1}\Delta\mathcal Q={}&
  a^2(d^Te)I_m
  +\left(\frac{u^Tv}{4}-a^2\right)\operatorname{sym}(de^T)\\
 &+\frac{u^Te}{4}\operatorname{sym}(dv^T)
  +\frac{d^Tv}{4}\operatorname{sym}(ue^T)
  +\frac{d^Te}{4}\operatorname{sym}(uv^T).
 \end{aligned}
 \tag{Joint-atom-copy-matrix}
\]
For example, the quartic unsymmetrized term has difference
\[
 \Delta[(x^Ty)xy^T]
 =\frac14\left[
  (u^Tv)de^T+(u^Te)dv^T+(d^Tv)ue^T+(d^Te)uv^T
 \right].
\]
Thus using every output edge does not in itself remove common scalar couplings in the actual copy polynomial.
These identities hold for arbitrary real border values; no claim about a typical support restriction or an arithmetic denominator follows from them.

<a id="conditional-atom"></a>
## A direct combinatorial conditional atom

Put
\[
 Z_j=X_jY_j,\qquad
 K_m=\#\{j:Z_j\ne0\},\qquad
 S_m=\sum_{j=1}^m Z_j.
\]
The variables \(Z_j\) are independent, with
\[
 \mathbb P(Z_j=0)=\frac34,\qquad
 \mathbb P(Z_j=1)=\mathbb P(Z_j=-1)=\frac18.
\]
Hence \(K_m\) is binomial with parameters \(m,1/4\), and conditional on its nonzero positions the corresponding signs are independent and fair.
For odd \(k\),
\[
 \mathbb P(S_m=1\mid K_m=k)
 =2^{-k}\binom{k}{(k+1)/2}\asymp k^{-1/2};
\]
for even \(k\) it is zero.
The comparison has absolute constants by the elementary central-binomial bounds.

The exact parity formula is
\[
 \mathbb P(K_m\text{ odd})=\frac{1-2^{-m}}2.
\]
Since \(\mathbb E K_m=m/4\) and \(\operatorname{Var}K_m=3m/16\), Chebyshev's inequality gives
\[
 \mathbb P\{K_m\notin[m/8,3m/8]\}\le12/m.
\]
The probability that \(K_m\) lies in this interval and is odd is therefore bounded below by a positive constant for all sufficiently large \(m\).
The central-binomial bounds on this event, and the same bounds with the \(O(m^{-1})\) complement, prove directly
\[
 \mathbb P(S_m=1\mid\Gamma_N)\asymp m^{-1/2},\qquad
 \mathbb P\{S_m=1,\ K_m\in[m/8,3m/8]\mid\Gamma_N\}\asymp m^{-1/2}.
 \tag{Joint-atom-probability}
\]
No local central limit theorem is assumed.
Since \(q=a^2S_m\), this is an atom at \(q=a^2\).
By (Joint-atom-all-output-factor), every off-diagonal output vanishes simultaneously there.

Let \(p_N=\mathbb P\{\operatorname{off}\mathcal Q(x,y)=0\mid\Gamma_N\}\), so \(p_N\ge c m^{-1/2}\).
Two applications of Cauchy--Schwarz to the indicator of this vector-valued zero event give
\[
 p_N^4
 \le\mathbb P\{\text{all four corners have }\operatorname{off}\mathcal Q=0\mid\Gamma_N\}
 \le\mathbb P\{\operatorname{off}\Delta\mathcal Q=0\mid\Gamma_N\}.
\]
In particular the complete rectangular difference has a zero atom at least \(c m^{-2}\) on this background.
That lower bound is itself summable, but an upper bound strong enough to produce arbitrary polynomial decay after taking the fourth root cannot hold uniformly over these backgrounds.
The original simultaneous-output event already has the nonsummable conditional lower bound \(c m^{-1/2}\).

<a id="normalization-and-guards"></a>
## The denominator and all relevant polynomial guards remain meaningful

Let \(k_x=\#\{j:X_j\ne0\}\) and \(k_y=\#\{j:Y_j\ne0\}\).
On \(q=a^2\), both counts are positive and
\[
 s_B=-ak_x,\qquad s_C=-ak_y.
\]
Thus the full \(B,C\) are invertible.
On that same event,
\[
 \mathcal A
 =\gamma_N[a^4I_m+a^2(xy^T-yx^T)],
 \qquad \mathcal Q=\gamma_Na^4I_m.
 \tag{Joint-atom-nonzero-adjugate}
\]
The bracket in \(\mathcal A\) is invertible because \(xy^T-yx^T\) is real skew-symmetric and \(a^4>0\).
In particular the actual \(D_i\) and its adjugate are invertible, and the true graph denominator is nonzero.
Its exact value is
\[
 \|\mathcal A\|_F
 =|\gamma_N|a^4\sqrt{m+2(k_xk_y-1)}.
 \tag{Joint-atom-denominator}
\]
This follows from
\(\|xy^T-yx^T\|_F^2=2(\|x\|^2\|y\|^2-q^2)=2a^4(k_xk_y-1)\)
and the zero Frobenius cross term with \(I_m\).
Consequently every actual normalized off-diagonal graph edge is exactly zero, rather than a ratio with a vanishing denominator.

The formal mixed-bilinear coefficient matrices and aggregate energy are
\[
 \mathscr B_{jk}=\frac{\gamma_Na^2}{2}
       (e_je_k^T+e_ke_j^T),\qquad
 \mathcal E_{\rm oo}
 =\frac{|\gamma_N|a^2}{2}\sqrt{m(m-1)}.
\]
Since \(k_xk_y\le m^2\) and \(m\ge2\), (Joint-atom-denominator) gives the particularly strong comparison
\[
 \frac{\mathcal E_{\rm oo}}{\|\mathcal A\|_F}
 \ge\frac1{4a^2}=\frac N8.
 \tag{Joint-atom-large-coefficient-energy}
\]
Thus the [proved coefficient comparison](../claims/Yin_C_F0194_v15.md#statement) does not exclude this simultaneous value atom.
For this three-point law the energy is a formal monomial-coefficient energy, not the Rademacher Walsh quantity.

At the chosen omitted index,
\[
 \|B_0\|=\|C_0\|=a,\quad
 \|E\|=\|G\|=a^{-1},\quad
 \|x\|,\|y\|\le a\sqrt m<\sqrt2,\quad
 s_{m-1}(D_0)=|z|a^{-2}.
\]
These satisfy fixed polynomial guards without any small second singular value.
The full \(B\) has eigenvalue \(a\) on the orthogonal complement of \(x\), and its other two eigenvalues are
\[
 \frac a2(1\pm\sqrt{1+4k_x}).
\]
Thus, whenever \(k_x\ge1\), its norm is at most \(a+\|x\|<3\) and its inverse norm is at most \(\varphi/a\), where \(\varphi=(1+\sqrt5)/2\).
The same facts hold for \(C\).
The remaining first-input border is bounded under its fixed law, so the first full input also has bounded norm on \(\Gamma_N\).
This establishes the local guard compatibility used above; \(\Gamma_N\) alone is not being asserted to impose every omitted-index guard of the coefficient theorem.

A stronger, still legal conditioning illustrates compatibility with all displayed simultaneous guard inequalities.
Add the event that the remaining first-input border and its exposed diagonal vanish, so the entire \(W_1\) is zero, and call the resulting background \(\Gamma_N^+\).
Its probability is \(2^{-(m+1)}\mathbb P(\Gamma_N)\), and the conditional laws of \(x,y\) are unchanged.
Retain the event in (Joint-atom-probability) with \(K_m\in[m/8,3m/8]\).
For sufficiently large \(m\), this ensures \(k_x,k_y\ge2\).
Every one-index principal minor of \(B,C\) is then invertible: deletion of the first coordinate leaves \(aI_m\), and any other deletion leaves the same displayed bordered form with at least one nonzero surviving border coordinate.
Their inverse norms are at most \(\varphi/a\) and their norms at most three.
Writing \(B_j=B_{\widehat j,\widehat j}\) and \(C_j=C_{\widehat j,\widehat j}\), the shifted background at every omitted index \(j\) is now
\[
 D_j=-z(C_j^{-1}B_j^{-1}),\qquad
 \|D_j^{-1}\|\le9/|z|.
\]
It therefore has a constant least-singular-value lower bound and, a fortiori, the required second-smallest floor.
All full-input, border and inverse guards are polynomial, and the coefficient theorem applies at every omitted index with appropriate fixed exponent margins.
This is compatibility with the simultaneous guard inequalities, not an identification with an additionally restricted unspecified event.
On this strengthened event the original shifted product is exactly
\[
 W_1W_2W_3-zI_N=-zI_N,
\]
so it is uniformly invertible.

<a id="scope-and-next-obligation"></a>
## Scope of the obstruction

For these original fixed bounded laws, no estimate with summable conditional errors can uniformly bound the event that every actual normalized off-diagonal cofactor edge is zero over all admitted backgrounds satisfying the displayed polynomial guards.
The conclusion persists for the joint output, a nonzero realized denominator and strong aggregate odd-odd energy.
The shared scalar factor explains the failure directly, without an inference from a single cofactor's rank or a generic unrelated quartic.

The background probabilities in (Joint-atom-background-probability), and those of the strengthened backgrounds, are exponentially small in \(m^2\) and summable.
Hence this example does not produce a nonsummable unconditional bad-graph probability, disprove a typical-background arithmetic statement or give a Brown-convergence counterexample.
It also does not obstruct a bound for the intersection of low matching with a small full determinant numerator; in the strengthened version that numerator comes from the uniformly invertible matrix \(-zI_N\).
No pure-Rademacher background or conditional-copy-mask counterexample is asserted.

The remaining useful target must either discard quantitatively negligible actual backgrounds before proving arithmetic nonstructure, or control the relevant small-numerator and graph-normalization events jointly.
A theorem conditional only on polynomial inverse, norm, second-smallest and aggregate-energy guards cannot supply that missing typicality.
The prior source-search and inspection boundary remains at the [arithmetic probe](../drafts/Yin_D_F0011.md#summable-arithmetic-probe); the present calculation invokes no new external small-ball theorem.

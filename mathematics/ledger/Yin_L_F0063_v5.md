---
author: Yin
---

<a id="strong-pole-complete-polynomial-test"></a>
# Complete strong-pole test: a coercive branch and the paired-coefficient moment obstruction

This ordinary development for Yin, dated 2026-11-06T09:10 UTC, continues the exact actual-model setup in [L63v4](Yin_L_F0063_v4.md#model).
The first calculation controls the complete Schur polynomial on an opposite-sign definite-background branch, without a polynomial approximation by its frozen proxy.
The second shows that an untruncated squared average of complete paired quadratic coefficients need not even be finite under the original finite-second-moment hypotheses.
The latter is an actual-model integrability obstruction to that averaging argument, not a counterexample to determinant convergence or to a possible direct complete-coefficient estimate.
Neither branch coverage in probability nor the remaining same-sign or indefinite-background resonance is resolved.
This is ordinary exploration and authoring self-checking, not an independent review or a new Claim assessment.
The [D10 development](../drafts/Yin_D_F0010.md#strong-pole-complete-polynomial-test) is extraction provenance; the complete bounded test is retained here.
The objective remains the every-coupling determinant limsup in the [matrix-pencil contract](../tasks/Yin_T_F0013_v1.md#contract), with no unconditional free-gap conclusion supplied by this record.

## Fixed conditioning and the polynomial to be controlled

Retain real symmetric size-three coefficients with \(\chi_A>0\), fixed original real centered variance-one off-diagonal laws, independent centered finite-second-moment diagonal laws, and arbitrary cross-size coupling.
Keep the free-gap target, one common deterministic real shift, a fixed physical deletion bound, and an actual real symmetric invertible minor \(M\) of physical size \(n=N-O(1)\).
Use the minor-measurable spectral decomposition
\[
 Z=M^{-1}=E+\lambda ee^T,\qquad
 e\in\mathbb R^{3n},\quad \|e\|=1,\quad
 \lambda\in\mathbb R\setminus\{0\},\quad
 Ee=0,\quad \|E\|_F^2/N\le K,\quad |\lambda|\ge c_0N,
 \tag{Complete-pole-branch}
\]
with fixed \(K\ge1,c_0>0\).
All eigenvalue signs are retained.
The common shift is a deterministic real sequence \(\theta_N\to0\); the physical deletion bound is fixed independently of \(N\).
Put \(\Lambda=\sum_{j=1}^d\|A_j\|^2\).
Constants may depend on the fixed coefficients, laws, deletion bound and branch/guard constants, but not on \(N,\lambda\) or a particular good conditioning.
The original border \(R\) and exposed diagonal \(D_i\), the sigma-field \(\mathcal F\) of the original retained input minors and exposed diagonal coordinates, and the physical variable groups are exactly those of L63v4.
Write
\[
 g_E=N^{-1}\sum_kE_{kk},\quad
 B_E=A_0+\theta_NI_3-\sum_jA_jg_EA_j,\quad
 B=B_E+D_i,\quad
 S_E=A_0+\theta_NI_3+D_i-R^TER,\quad
 z=\sqrt N\,R^Te.
\]
The complete Schur polynomial, with the original raw border coordinates as its variables, is
\[
 S=S_E-\frac{\lambda}{N}zz^T,\qquad
 P_N=\frac N\lambda\det S
     =\frac N\lambda\det S_E-z^T\operatorname{adj}(S_E)z.
 \tag{Complete-pole-polynomial}
\]
It has degree at most six and retains all lower-degree and repeated-coordinate terms.

Restrict the conditioning to the actual branch above, the actual-minor rectangle event and norm guard of [L63v4's spread calculation](Yin_L_F0063_v4.md#actual-minor-spread), and its measurable good-background events
\[
 \|B_Eg_E-I_3\|\le\tfrac12,\qquad
 \|D_i\|\le(8\sqrt{3K})^{-1}.
\]
These events are \(\mathcal F\)-measurable.
They give fixed \(b,C_K>0\) such that \(s_{\min}(B)\ge b\), \(\|B\|\le C_K\), and
\[
 \mathbb E[\|S_E-B\|\mid\mathcal F]\le q_N(K)\longrightarrow0
 \tag{Complete-pole-residual-concentration}
\]
by the adopted [C194v18 quadratic estimate](../claims/Yin_C_F0194_v18.md#quadratic-concentration).
The actual-minor fixed-eta argument supplies the stated relative background exception, without asserting that this strong-pole branch has high probability.
The event \(\{\|S_E-B\|\le b/2\}\) depends on the fresh row and will only be intersected with events and paid for by Markov's inequality.
It is not added to the conditioning or used to replace the original row law.

<a id="opposite-sign-complete-schur"></a>
## A complete-polynomial bound for the opposite-sign definite branch

Impose the further measurable branch condition
\[
 \operatorname{sgn}(\lambda)\,B\preceq-bI_3.
 \tag{Complete-pole-opposite-sign}
\]
This means \(B\) is definite and its sign is opposite to the pole.
It is not a consequence of a free gap or of the preceding inverse decomposition.

First obtain the required original-law linear small-ball estimate for \(z\).
Fix a real unit auxiliary direction \(a\), independent of the fresh row, and use
\[
 z=\sum_{k=1}^n V_k\xi_k,\qquad
 V_k=(A_1e_k,\ldots,A_de_k),\qquad
 V_kV_k^T\succeq\chi_A\|e_k\|^2I_3.
\]
The actual-minor rectangle event under the guard \(B_0\sqrt N\) gives at least \(c_1N\) physical indices with \(\|e_k\|\ge\kappa N^{-3/2}\).
For each such index, some original input label \(j(k)\) satisfies
\[
 |a^TA_{j(k)}e_k|
 \ge\sqrt{\chi_A/d}\,\|e_k\|
 \ge c_2N^{-3/2}.
 \tag{Complete-pole-linear-matching}
\]
These are distinct original scalar coordinates because their physical indices differ.
Their selection is measurable under \(\mathcal F\), before any original border coordinate is drawn.

The exact original-law two-copy representation used in [L63v4](Yin_L_F0063_v4.md#frozen-proxy) preserves a linear number of those coefficients except with probability \(Ce^{-cN}\).
Indeed the fixed nonzero variances give a uniform positive chance that each copy difference exceeds a fixed positive constant, independently over the selected coordinates.
After conditioning the copies, apply the degree-one case of the accepted [MNV16 Theorem 1.6](../audits/literature/MNV16/Yin_U001.md#matching-rank), with coefficient scale a fixed multiple of \(N^{-3/2}\).
Its first bound has denominator \(r^{1/5}\) at degree one.
For sufficiently small fixed \(c_3>0\), this yields uniformly on the good conditioning
\[
 \mathbb P\{|a^Tz|\le c_3N^{-3/2}\mid\mathcal F\}
 \le Ce^{-cN}+C\sqrt{\log N}\,N^{-1/5}.
 \tag{Complete-pole-linear-small-ball}
\]
All remaining original variables only contribute an unrestricted linear part and center after pairing.
No fresh-row stability event has been conditioned on.

On \(\|S_E-B\|\le b/2\), (Complete-pole-opposite-sign) implies
\(\operatorname{sgn}(\lambda)S_E\preceq-(b/2)I_3\).
Since the auxiliary dimension is three,
\[
 \operatorname{adj}(S_E)\succeq(b/2)^2I_3,\qquad
 \frac N\lambda\det S_E<0.
\]
The two terms in (Complete-pole-polynomial) therefore have the same nonpositive sign, and
\[
 |P_N|\ge(b/2)^2\|z\|^2\ge(b/2)^2|a^Tz|^2.
 \tag{Complete-pole-sign-coercivity}
\]
This is an inequality for the complete polynomial, not a comparison with a proxy at a shrinking window.
Markov's inequality and the original-law linear estimate give some fixed \(c_4>0\) such that
\[
 \mathbb P\{|P_N|\le c_4N^{-3}\mid\mathcal F\}
 \le\frac{2q_N(K)}b+Ce^{-cN}
                  +C\sqrt{\log N}\,N^{-1/5}\longrightarrow0.
 \tag{Complete-pole-opposite-sign-small-ball}
\]
Only a fixed-size stability tolerance was used, so no polynomial rate for \(q_N(K)\) is assumed.
The same-row dependence of \(z\) and \(S_E\) is fully retained.

The [exact single-pole graph identity](Yin_L_F0063_v4.md#graph-interface) gives, with
\(\Gamma_E=I_3+R^TE^2R\) and \(\Gamma=I_3+R^TZ^2R\),
\[
 \det\Gamma=\det\Gamma_E
       \left(1+\frac{\lambda^2}{N}z^T\Gamma_E^{-1}z\right),\qquad
 \mathbb E[\operatorname{Tr}\Gamma_E+\|z\|^2\mid\mathcal F]
       \le3+\Lambda K+\Lambda.
\]
Intersect the two fresh-row guards
\(\operatorname{Tr}\Gamma_E\le N^{1/4}\) and \(\|z\|^2\le N^{1/4}\).
Their complementary conditional probability is \(O(N^{-1/4})\).
For large \(N\), the graph estimate gives \(\sqrt{\det\Gamma}\le C_{c_0}|\lambda|\), and hence
\[
 |\det F|=\frac{|\det S|}{\sqrt{\det\Gamma}}
          \ge\frac{|P_N|}{C_{c_0}N},
 \qquad F=\Gamma^{-1/2}S.
\]
After reducing a fixed constant,
\[
 \mathbb P\{|\det F|\le c_5N^{-4}\mid\mathcal F\}
 \le\frac{2q_N(K)}b+Ce^{-cN}
       +C\sqrt{\log N}\,N^{-1/5}+CN^{-1/4}\longrightarrow0.
 \tag{Complete-pole-opposite-sign-graph}
\]
This meets the actual graph normalization with no upper bound on \(|\lambda|\).

On an additional full-parent norm guard \(\|L_{\rm parent}^{\theta}\|\le B_0\sqrt N\), the graph compression obeys \(\|F\|\le B_0\sqrt N\).
Thus the joint event
\[
 \left\{s_{\min}(F)\le c_5B_0^{-2}N^{-5},
                    \ \|L_{\rm parent}^{\theta}\|\le B_0\sqrt N\right\}
\]
is contained in the determinant event just bounded.
The parent guard is not inserted into \(\mathcal F\).
This supplies an actual distance probability for this measurable branch; the average probability of being outside it remains an unresolved input for a full-parent application.

<a id="paired-coefficient-l2-obstruction"></a>
## Why an untruncated squared pairing average is unavailable at bare finite variance

The direct complete-coefficient question cannot simply assume that the original polynomial or its paired quadratic coefficients have finite averaged \(L^2\) norm.
Here is a legal actual model where a specified complete paired quadratic coefficient has infinite squared average on a positive-probability actual strong-pole event.

Let \(B_1,\ldots,B_6\) be the real Frobenius-orthonormal basis
\[
 E_{11},E_{22},E_{33},\quad
 (E_{12}+E_{21})/\sqrt2,\quad
 (E_{13}+E_{31})/\sqrt2,\quad
 (E_{23}+E_{32})/\sqrt2.
\]
Take \(d=7\), \(A_j=B_j\) for \(j\le6\), \(A_7=I_3\), and \(A_0=20I_3\).
For complex unit vectors \(u,v\), the six basis directions satisfy
\[
 \sum_{j=1}^6|u^*B_jv|^2
 =\|\operatorname{sym}(\overline u v^T)\|_F^2
 =\tfrac12(1+|u^Tv|^2)\ge\tfrac12,
\]
so the required complex-direction frame is positive.
Also
\[
 \left\|\sum_{j=1}^7 A_j\otimes s_j\right\|
 \le2\sum_j\|A_j\|=8+3\sqrt2<20.
\]
Thus the free pencil is strictly positive and has a gap at zero.

Give every original off-diagonal and diagonal scalar the fixed density
\[
 f(x)=\frac{2}{\pi(1+x^2)^2}.
\]
It is centered, has variance one and positive density on all of \(\mathbb R\).
The normalization and variance follow from
\(\int_{\mathbb R}(1+x^2)^{-2}\,dx
 =\int_{\mathbb R}x^2(1+x^2)^{-2}\,dx=\pi/2\).
Its absolute moments of order at least three are infinite.
All original scalar coordinates and inputs remain independent within each dimension.
Take \(\theta_N=0\), and fix an actual retained minor of size \(n\ge2\).

Let \(\alpha=(7,1)\) and \(\beta=(7,2)\) be the two original border coordinates in the identity-noise input at two retained physical positions.
The coefficient of the monomial \(\xi_\alpha^4\xi_\beta^2\) in the degree-six part of \(\det S\) is a rational function of the actual minor entries, independent of the exposed diagonal and other fresh coordinates.
It is not identically zero on this actual model's parameter space.
For verification, at the allowed support point
\[
 M_*=\operatorname{diag}(\mu,20,20,\ 20I_3,\ldots,20I_3),
 \qquad \mu>0,\quad \lambda_*=\mu^{-1},\quad c=1/20,
\]
the two retained inverse blocks are
\(Z_{11}=\operatorname{diag}(\lambda_*,c,c)\) and \(Z_{22}=cI_3\), with zero cross block.
Restricting the raw border to these two variables, the leading determinant is
\[
 -\frac1{N^3}
       (\lambda_*\xi_\alpha^2+c\xi_\beta^2)
       (c\xi_\alpha^2+c\xi_\beta^2)^2.
\]
Therefore the coefficient in the normalized complete polynomial \(P_N=(N/\lambda_*)\det S\) is
\[
 \gamma_{\alpha^4\beta^2}
       =-\frac{c^2}{N^2}\left(2+\frac c{\lambda_*}\right)\ne0.
 \tag{Complete-pole-mixed-sixth-witness}
\]
This point is an attainable parameter value of the original minor model: all original minor coordinates may be zero except a diagonal coordinate in direction \(E_{11}\).
It is used to certify nonidentical vanishing of a polynomial numerator, not to replace a random minor by a prescribed matrix.

The actual minor coordinates have a joint density positive everywhere.
The determinant polynomial is not identically zero, and the numerator of the displayed rational coefficient is not identically zero by this support-point calculation.
Their zero sets therefore have Lebesgue measure zero.
It follows that almost every actual minor is invertible and has
\(\gamma_{\alpha^4\beta^2}(P_N)\ne0\), for any selected nonzero inverse eigenvalue used in the normalization.
Multiplication by \(N/\lambda\) does not change whether that coefficient vanishes.

There is also a positive-probability actual strong-pole event at each sufficiently large fixed \(N\).
Choose \(\mu=(2c_0N)^{-1}\) at the displayed support point.
It has a simple inverse head \(\lambda_*=2c_0N\) and residual energy
\((3n-1)/(400N)<1\).
A sufficiently small open neighborhood of the original minor coordinates preserves one real inverse head of magnitude at least \(c_0N\) and residual energy below fixed \(K=1\).
The strictly positive joint density gives this open event positive probability.
No uniform lower bound for its probability as \(N\to\infty\) is claimed.
Nor is the support point asserted to satisfy the good rectangle or background events.
The almost-everywhere nonvanishing assertion is valid on any further actual-minor event, including those good events whenever their intersection has positive probability.

Now condition an actual minor with \(\gamma_{\alpha^4\beta^2}\ne0\), and pair all original border coordinates exactly as before.
For each fixed array of pair values, let the complete Walsh quadratic coefficient be
\[
 \widehat P_{\alpha\beta}
   =\mathbb E_\varepsilon
          [P_N(\xi(\varepsilon))\,\varepsilon_\alpha\varepsilon_\beta].
 \tag{Complete-pole-paired-quadratic}
\]
This finite sign expectation exists for every finite pair array.
The contribution from \(\gamma_{\alpha^4\beta^2}\xi_\alpha^4\xi_\beta^2\) is exactly
\[
 \frac{\gamma_{\alpha^4\beta^2}}4
       [(\xi_\alpha')^4-(\xi_\alpha'')^4]
       [(\xi_\beta')^2-(\xi_\beta'')^2].
 \tag{Complete-pole-quadratic-collision-contribution}
\]
No other raw monomial contributes to its pair-value monomial
\((\xi_\alpha')^4(\xi_\beta')^2\): the original total degree is at most six.
Consequently, as a polynomial in \(\xi_\alpha'\), the full coefficient
\(\widehat P_{\alpha\beta}\) has degree at least four for almost every choice of the other pair values.
Indeed its degree-four coefficient is a nonzero polynomial in those other values, because its coefficient of \((\xi_\beta')^2\) is the displayed nonzero number; higher powers, if present, only increase that degree.
The other pair values have a joint density, so the exceptional polynomial zero set has probability zero.

The squared magnitude of a nonzero real polynomial of degree at least four is not integrable against \(f\).
Tonelli's theorem therefore gives, for almost every such actual minor,
\[
 \mathbb E_{\rm pairs}\!
       \left[|\widehat P_{\alpha\beta}|^2\mid\mathcal F\right]
       =+\infty.
 \tag{Complete-pole-paired-L2-divergence}
\]
This holds in particular almost surely on the positive-probability actual strong-pole event above.
The calculation concerns a complete quadratic Walsh coefficient, so it directly retains the repeated-variable collisions that would be lost by substituting the frozen quadratic proxy.

This does not invalidate conditional-on-pairs MNV: its deterministic coefficients are finite for every finite pair array, and its theorem does not ask for their averaged moments.
It does invalidate an unqualified step that integrates squared complete coefficients over the original pair distribution and treats that average as finite under finite second moments.
A bounded or weighted pairing restriction would need its own exact original-law probability and complete-coefficient estimate.
No such estimate, cancellation theorem, or high-probability matching conclusion is supplied by this integrability calculation.

<a id="complete-pole-next-interface"></a>
## What has changed and what is still required

The opposite-sign definite branch now has an actual complete-polynomial \(N^{-3}\) small-ball estimate and a graph-normalized \(N^{-4}\) determinant estimate, with every fresh-row good event handled by intersection and its own probability error.
Its coverage in the actual model is not known, and it does not address same-sign definite resonance or indefinite backgrounds.
The untruncated \(L^2\) pairing route has a concrete actual finite-variance obstruction even for complete quadratic coefficients.
Neither result controls the remaining complete degree-six polynomial on bounded pairing supports or proves that the frozen proxy's matching survives its same-variable residual terms.
The next unresolved interface is an original-law conditional complete-coefficient or polynomial estimate in those remaining regimes, with the pairing restriction, collisions and graph scale kept together.
No new Claim, review, or general free-gap determinant completion is asserted here.

---
author: Yin
---
# Target-only functional tests for ACSY at the common-left-factor tuple

This continuing draft originated in the developer branch assigned to the former review agent.
Its author develops the arguments here; they are not independently reviewed.
D_F0004 remains the separate normal weighted-liberation investigation.
No new mathematical conclusion about A is selected by this draft.

## Exact target and reuse boundary

The accepted [C_F0147](../claims/Yin_C_F0147_v1.md#statement), with its complete independent [R_F0154](../audits/reviews/Yin_R_F0154_v1.md#conclusion), supplies h=2+s_0 and X_j=hS_j for three free standard semicircular reference variables.
The target algebra is N=W*(X_1,X_2), not an assumed equality with the reference algebra.
The target star core is algebraically free on x_1,x_2,y_1,y_2 evaluated at X_1,X_2,X_1*,X_2*.
Maximal Delta and failure of every bare full-domain coordinate dual are proved there.
The later [C_F0148](../claims/Yin_C_F0148_v1.md#statement), with complete independent [R_F0155](../audits/reviews/Yin_R_F0155_v1.md#conclusion), excludes both actual target coordinate ACSY witnesses.
This candidate no longer leaves a target-A question open and cannot separate A from F.

The D_F0003 investigation available at the original checkpoint was read before development.
Its failed full-reference lift and failed right-annihilation domain at a starred generator are boundaries, not proofs against arbitrary target derivations.
At that checkpoint, its bounded-regularization system was being developed separately by root.
No argument here assumes that h or S_j belongs to an actual target derivation domain.

A local search of the registered bibliography, contents and source units by free Stein kernels, partial conjugate variables, nonselfadjoint Fisher information and Jacobian-adjoint domains initially found no registered Charlesworth--Nelson interface.
The subsequent primary-source inspection is now retained in CN21-U001 and CN25-U001 at their exact accepted scopes and stated corrections, linked below.
Earlier broad Fisher/minimization searches are retained in D_F0003 and are not treated as a solution.

## An exact target-only functional reduction

Write H=L2(N), K=H tensor_2 H and A for the target star core.
Algebraic freeness gives the four formal word-cut operators partial_xj and partial_yj on A, with values in A tensor_alg A.
They are defined algebraically; no individual Hilbert closability is presumed.
For a fixed coordinate i put

\[
 L_i(p)=(\tau\otimes\tau)(\partial_{x_i}p),\qquad
 Gp=(p,\partial_{y_1}p,\partial_{y_2}p)\in H\oplus K\oplus K.
 \tag{F1}
\]

Then the target coordinate A witness exists if and only if there is a finite constant c_i such that

\[
 |L_i(p)|\le c_i\bigl(\|p\|_2^2+
       \|\partial_{y_1}p\|_2^2+\|\partial_{y_2}p\|_2^2\bigr)^{1/2}
 \quad(p\in A).
 \tag{F2}
\]

Here A witness means a derivation delta:A->K with delta X_j=delta_ij 1 tensor 1 and 1 tensor 1 in Dom(delta*).
It places no independent normalization on delta X_j*.

To prove the reduction, any such derivation has unique algebraic expression

\[
 \delta p=\partial_{x_i}p+
           \sum_{j=1}^2 I_{K_j}\partial_{y_j}p,
 \qquad K_j=\delta X_j^*\in K.
 \tag{F3}
\]

The finite word-cut expression and bounded outer factors define every insertion.
Identify K with L2(N tensor_bar N^op); tensor adjoint below is componentwise adjoint, without a flip.
Tracial cyclicity on a finite cut a tensor b gives

\[
 \langle1,I_{K_j}(a\otimes b)\rangle
      =\langle K_j^*,a\otimes b\rangle.
 \tag{F4}
\]

This identity holds for arbitrary Hilbert K_j by bounded multiplication and L2 approximation.
If xi=delta*1, the actual adjoint identity is therefore

\[
 L_i(p)=\langle\xi,p\rangle-
                 \sum_j\langle K_j^*,\partial_{y_j}p\rangle.
 \tag{F5}
\]

Cauchy--Schwarz gives (F2).
Conversely, G is injective because its first component is p.
Thus (F2) defines a bounded linear functional on its range, extending continuously to its Hilbert closure.
Riesz representation there gives xi,A_1,A_2 such that L_i(p)=<xi,p>+sum_j<A_j,partial_yj p>.
Set K_j=-A_j*.
Formula (F3) defines a derivation on the free target star algebra and (F4) gives <1,delta p>=<xi,p> for every p.
This is exactly actual vacuum-adjoint membership.
No target/reference extension or domain of an inverse occurs.

Equivalently, failure of coordinate A is witnessed by a sequence of target polynomials with

\[
 L_i(p_n)=1,\qquad
 \|p_n\|_2^2+\sum_j\|\partial_{y_j}p_n\|_2^2\longrightarrow0.
 \tag{F6}
\]

Indeed failure of boundedness yields ratios tending to infinity and scalar rescaling yields (F6); the converse is immediate.
This is a concrete target-only negative-test obligation.
Holomorphic polynomials would eliminate both unknown starred coefficients, but no purely holomorphic sequence is asserted.
The fixed resolvent proof below produces a weak graph contradiction, which also implies existence of strong graph witnesses by this equivalence.

The reduction itself is an elementary Hilbert functional argument, with actual coefficient order spelled out.
It is self-checked development, not a completed obstruction or a claim that formal partials are closable.
A free Stein/Jacobian source may supply a useful geometric interpretation, but a statement only about the closure of a module is not yet the actual prescribed-value criterion (F2).

## Fixed resolvent obstruction and source boundary

The complete target resolvent proof and its general row consequence are fixed and adopted at [C_F0148's reviewed decision](../claims/Yin_C_F0148_v1.md#decision-reviewed), supported by the complete independent [R_F0155](../audits/reviews/Yin_R_F0155_v1.md#conclusion).
That proof excludes both target coordinate ACSY witnesses for C_F0147, and more generally shows that a coordinate with positive row-kernel diagonal trace forces finite tau(Q^-1) when Q is regular.
The full-system consequence includes an actual right inverse on bounded vectors through the row polar decomposition.
Root contributed checks, the general formulation and the range corollary; these are development contributions.
The full fixed proof is not duplicated here.

The functional criterion above remains a separate reusable target-only reduction.
It was independently rediscovered by the general branch, which links this responsible home rather than duplicating the proof.
It is not a logical dependency of C_F0148's direct actual-derivation argument.

The bounded source inspection is retained in [CN21-U001](../audits/literature/CN21/Yin_U001.md#cn21-u001) and [CN25-U001](../audits/literature/CN25/Yin_U001.md#cn25-u001).
The first supplies an exact actual-domain interpretation, with a necessary target projection in the stated restriction-vacuum identity.
The second requires actual polynomial/Jacobian weak limits or uniform derivative bounds; it does not justify a dimension bound from a smaller ambient presentation.
Neither source is used to assume h or S_j lies in any target derivation domain.

The proposed formal ambient holomorphic vacuum, whose Fock coefficients were suggested by root, was not promoted to a target obstruction: its infinite ambient norm alone would not show an unbounded projection to the target holomorphic space.
The resolvent test resolves the concrete candidate without that unproved projection step.
No native computation was started for this lead.


## Automatic continuity for a bounded selfadjoint factorization

The full conditional automatic-continuity theorem and exact projective-tensor criterion are fixed in [C_F0151](../claims/Yin_C_F0151_v2.md#statement).
Its selected decision adopts the complementary independent scopes of [R_F0158](../audits/reviews/Yin_R_F0158_v1.md#independent-conclusion) and [R_F0159](../audits/reviews/Yin_R_F0159_v1.md#application-conclusion).
The argument applies to every hypothetical bare dual for X=hS through X=AB, A=sqrt(h), B=sqrt(h)S, with BA selfadjoint diffuse and B injective.
It supplies no existence or nonexistence conclusion.

For the actual A-positive tuple of [C_F0150](../claims/Yin_C_F0150_v1.md#statement), the full target F question is now positively resolved by [C_F0152's adopted proof](../claims/Yin_C_F0152_v1.md#decision-reviewed), with complete independent [R_F0160](../audits/reviews/Yin_R_F0160_v1.md#conclusion).
Its intrinsic canonical forward closure gives a normalized operator-norm-to-L2 map E on all N satisfying [E,X]=P, with norm at most sqrt(2)+1+2||beta||2.
The functional F_E(a tensor bar(eta))=<eta,Ea> therefore makes C_F0151's prescribed projective functional well-defined and bounded by the same constant.
This resolves the concrete projective-functional question without asserting a general transfer from the separate actual-A Hilbert graph criterion.
The fixed C_F0152 proof is not duplicated here, and it supplies no full adjoint-domain conclusion.

The coupled coefficients in C_F0150 also have the scalar Laplace formulas alpha(u,v)=integral_0^infinity exp(-tu)sin(tv)dt and beta(u,v)=integral_0^infinity exp(-tu)cos(tv)dt.
Here ||exp(-th)||2 has order t^(-3/4) at infinity, so its square is time integrable but its norm is not.
A triangle-inequality integration therefore does not give a full-domain bound.
A Fourier or weighted free-product estimate would have to retain the oscillation and check every mixed target word; neither a one-block test nor the actual vacuum alone supplies it.
D_F0003 owns that ongoing canonical construction attempt.

## Single resolvent tests satisfy a uniform forced-output bound

This is a self-checked diagnostic developed by the target-functional branch after C_F0151, not an independently reviewed theorem or an F conclusion.
Its purpose is to test the simplest all-witness consequence of the accepted automatic-continuity result for X=hS.
The reuse pass read the complete C_F0150 construction, C_F0151 v2's projective criterion, and D_F0003's exact coupled expansions.
The only extra computation below uses the already inspected semicircular noncrossing-pairing formula [NS06-U004](../audits/literature/NS06/Yin_U004.md#ns06-u004).
No external search or source acquisition is needed.

Put a=sqrt(h), Y=aSa and let

\[
 m(z)=\tau((z-Y)^{-1}),\qquad z\notin\mathbb R.
 \tag{P1}
\]

The bounded factorization formula from C_F0151 gives

\[
 (z-X)^{-1}=z^{-1}1+z^{-1}a(z-Y)^{-1}aS.
\]

Cyclicity of the trace and aSa=Y show that its trace is m(z).
This uses bounded resolvents at nonreal z and does not move an unbounded inverse through a trace.

Here is an exact equation for m.
On the algebra generated by h, the conditional semicircular pairing recursion for Y has covariance

\[
 \eta(b)=h\tau(hb).
\]

Indeed Y=aSa, and pairing two S letters with a coefficient b between them gives a tau(aba) a=h tau(hb).
The noncrossing-pairing expansion of the norm-convergent resolvent at sufficiently large |z| therefore gives, with G(z)=E_{W^*(h)}((z-Y)^{-1}) and alpha(z)=tau(hG(z)),

\[
 G(z)=(z-h\alpha(z))^{-1},\qquad
 \alpha(z)^2=z m(z)-1.
 \tag{P2}
\]

This is only used initially where its moment series converges absolutely.
It follows directly by decomposing a noncrossing pairing according to the partner of the first semicircular letter, so no additional operator-valued existence theorem is assumed.

The shifted standard semicircle Cauchy transform G_h(w) satisfies

\[
 G_h(w)^2-(w-2)G_h(w)+1=0.
\]

In the large-|z| region alpha is nonzero, G_h(z/alpha)=alpha m, and substitution into this scalar equation followed by (P2) gives

\[
 \alpha(1-m^2)=2m,
 \qquad
 z m(1-m^2)^2=(1+m^2)^2.
 \tag{P3}
\]

The final identity is polynomial in the analytic Cauchy transform m, so the identity theorem extends it from that region to each nonreal half-plane.
This step does not assume an analytic continuation of an arbitrarily chosen root of a polynomial equation; m is the actual resolvent trace throughout.

In the upper half-plane, Im(m)<0 because m is the Cauchy transform of a probability law.
It cannot cross the unit circle.
In fact, if m=exp(i theta) with -pi<theta<0, the values m=plus or minus 1 are already impossible in (P3); otherwise

\[
 z m=-\cot^2\theta,
 \qquad \operatorname{Im}z=\cot^2\theta\sin\theta\le0,
\]

contradicting Im(z)>0.
Since m(z) tends to zero as z goes to imaginary infinity and the upper half-plane is connected, it follows that |m(z)|<1 there.
Reflection gives the same bound in the lower half-plane.
As a normalization check, (P3) begins with m(z)=z^-1+4z^-3+40z^-5+..., agreeing with the second and fourth moments of hS from the free pairing formula.

Now suppose a bare full-domain dual exists.
By C_F0151 it is bounded from N with its operator norm to H_N.
In the operator-first convention write it as E with [E,X]=P.
Subtract right multiplication by E1 to arrange E1=0; this subtraction remains bounded N-to-H_N and leaves the commutator unchanged.
For R_z=(z-X)^-1 in N, the full-domain algebraic commutator rule gives [E,R_z]=R_z P R_z.
Applying it to 1 yields the forced value

\[
 E(R_z)=m(z)R_z,
 \qquad
 \frac{\|E(R_z)\|_2}{\|R_z\|_\infty}\le |m(z)|<1.
 \tag{P4}
\]

Thus single nonreal resolvents cannot contradict the necessary boundedness of an arbitrary normalized witness.
This is a genuinely all-witness diagnostic, since it uses only its commutator and normalization, not the particular C_F0150 coefficients or their ambient canonical extension.

More generally, on every holomorphic polynomial the normalized value is uniquely forced by the commutator recursion.
In C_F0151's notation, norm continuity and its polynomial C3 approximation extend that identity to the smooth calculus: E(Phi_f)=Gamma_f 1.
Accordingly a necessary all-witness estimate is ||Gamma_f 1||_2<=C||Phi_f||_infinity for all those smooth f.
Formula (P4) by itself verifies only the individual resolvent subfamily; it does not control their operator-norm cancellations or extend a map from this calculus to all of N.
The full projective-functional bound for this candidate instead follows from the independently adopted C_F0152 construction, as recorded above.

## A uniform bound on every forced holomorphic-polynomial value

The preceding diagnostic admits a stronger scalar conclusion.
The following distinct Cauchy-transform and weighted-measure mechanism is retained at developer-checked scope, without an independent review; the candidate's stronger full F conclusion is already supplied by C_F0152.
Its additional analytic input is the ordinary Hilbert-transform Lq bound for 1<q<infinity, at the primary-statement-checked Tao06 scope retained in [Voi98-U002](../audits/literature/Voi98/Yin_U002.md#proposition-35-scalar-hilbert-transform-realization).
Apply that existing theorem at q=6.
No new harmonic-analysis source or unproved endpoint theorem is needed.

Let u=h^-1/2, an actual L2 vector by C_F0150, and let mu_u be its spectral measure for left Y:

\[
 \int f(t)\,d\mu_u(t)=\langle u,f(Y)u\rangle
                       =\tau(h^{-1}f(Y)).
 \tag{P5}
\]

Its mass is tau(h^-1)=1, and its support is in [-8,8].
The identity with the L1 pairing is justified by spectral truncation of h^-1.
Its Cauchy transform m_u is analytic off the real axis.
In the initial large-|z| region of (P2), scalar partial fractions give

\[
 m_u(z)=\frac{1+\alpha(z)m(z)}{z}
       =\frac{m(z)(1-m(z)^2)}{1+m(z)^2}.
 \tag{P6}
\]

Here tau(h^-1)=1 was used in the first equality, and (P3) in the second.
The denominator 1+m^2 cannot vanish at a nonreal z by (P3).
Analytic continuation therefore gives (P6) for every nonreal z.
In particular (P3) implies the exact modulus identity

\[
 |m_u(z)|^2=\frac{|m(z)|}{|z|}\le |z|^{-1}.
 \tag{P7}
\]

These are actual vector spectral measures, not a formal density identification.
Positivity of the Poisson kernels and |m|<=1 imply that mu_Y has Lebesgue density w with 0<=w<=1/pi.
Likewise (P7) bounds the Poisson transforms of mu_u uniformly on each compact real interval away from zero, and gives the density estimate

\[
 0\le w_u(t)\le\frac1{\pi\sqrt{|t|}}\quad(t\ne0).
 \tag{P8}
\]

For completeness, uniform local Poisson bounds make the restriction absolutely continuous by testing nonnegative continuous functions and passing to the Poisson approximate identity.
The pointwise bound then follows by Lebesgue differentiation.
The only remaining possible singular mass would be at zero; it is absent because Y is injective, as checked in C_F0151's concrete application.
Thus mu_u=w_u dt globally and w_u belongs to L^(3/2)(R).
No endpoint L2 assertion is made.
Both densities have compact support.

Use the unnormalized Hilbert transform

\[
 \mathcal H f(t)=\operatorname{p.v.}\int\frac{f(s)}{t-s}\,ds.
\]

The boundary real part of m gives ||H w||_infinity<=1.
This can also be obtained by taking the bounded real parts of m(t+i epsilon), identifying them with Poisson regularizations of H w, and using L6 convergence.
The accepted L6 Hilbert theorem and Holder's inequality show, for every polynomial p and its scalar divided-difference contraction q,

\[
 q(t)=\int\frac{p(t)-p(s)}{t-s}\,d\mu_Y(s)
      =p(t)\mathcal H w(t)-\mathcal H(pw)(t)
\]

and

\[
 \begin{split}
 \|q\|_{L^2(\mu_u)}
 &\le \|p\|_{\infty,\sigma(Y)}
       +\|w_u\|_{3/2}^{1/2}\|\mathcal H(pw)\|_6\\
 &\le\left(1+C_6\|w_u\|_{3/2}^{1/2}\|w\|_6\right)
          \|p\|_{\infty,\sigma(Y)}.
 \end{split}
 \tag{P9}
\]

The principal-value identity is harmless for polynomials because their original difference quotient is bounded on the compact square; the Hilbert realization gives that same polynomial almost everywhere.
C_6 is the finite bound for the unnormalized Hilbert transform.
The right-side constant depends only on this fixed law, not on p or its degree.

Let E_hol be the normalized map on holomorphic polynomials forced by [E,X]=P and E1=0.
The commutator recursion gives

\[
 E_{\rm hol}(p(X))=q(X),
 \tag{P10}
\]

because the holomorphic trace moments of X and Y agree.
This is an identity of ordinary polynomials.
Also q(X)sqrt(h)=sqrt(h)q(Y), so multiplication by the affiliated h^-1/2 gives an actual Hilbert-vector identity q(X)=sqrt(h)q(Y)h^-1/2.
Bounded left multiplication and (P5) imply

\[
 \|q(X)\|_2\le2\|q\|_{L^2(\mu_u)}.
 \tag{P11}
\]

Finally, the bounded AB/BA resolvent identity gives equality of the nonzero spectra of X and Y.
Since Y is selfadjoint with diffuse law and the trace is faithful, zero cannot be an isolated point of sigma(Y): an isolated spectral point would give a nonzero atomic spectral projection.
Thus the nonzero part of sigma(Y) is dense in sigma(Y), whenever zero belongs to it.
Closedness of sigma(X) gives sigma(Y) subset sigma(X), which is all that is needed.
Polynomial spectral mapping therefore gives ||p||_(infinity,sigma(Y))<=||p(X)||_infinity.
Combining (P9)--(P11) yields

\[
 \|E_{\rm hol}(p(X))\|_2
       \le C\|p(X)\|_\infty
       \quad\text{for every holomorphic polynomial }p.
 \tag{P12}
\]

Thus the full holomorphic-polynomial family, not merely isolated resolvents, cannot refute boundedness of a normalized full-domain witness.
The construction is intrinsic at these inputs: q(X) belongs to N, and no conditional expectation of a failed ambient canonical vector is being substituted for it.

This scalar estimate alone does not prove F.
The holomorphic algebra need not be operator-norm dense in the target star algebra or N; a bounded linear Hilbert-valued extension need not preserve the commutator.
In the exact projective criterion, (P12) controls only tensors whose telescoping commutators encode these holomorphic tests.
General bounded a and their linear relations are handled for this candidate by C_F0152's different full-core construction, not by an enlargement of the present scalar argument's scope.

One natural spectral transport illustrating this method's limitation is Psi(a)=E_(W*(Y))(h^-1/2 a h^1/2).
For bounded ambient a the inside is an actual L2 vector; Psi is trace preserving and intertwines left X with left Y.
Conditional Cauchy--Schwarz gives only |Psi(a)|^2<=||a||^2 E_Y(h^-1)E_Y(h), which does not supply the bounded scalar input used in (P9).
No extension estimate for that potentially singular scalar input is claimed.
It is unnecessary for the now-resolved candidate, since C_F0152 constructs the full target map by another route; failure of this particular transport would not contradict that construction.

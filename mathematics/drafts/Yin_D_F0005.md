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
The later [C_F0148](../claims/Yin_C_F0148_v1.md#statement), with the complete self-reviewed [R_F0155 finding](../audits/reviews/Yin_R_F0155_v1.md#conclusion), excludes both actual target coordinate ACSY witnesses.
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

The complete target resolvent proof and its general row consequence are fixed and adopted at [C_F0148's reviewed decision](../claims/Yin_C_F0148_v1.md#decision-reviewed), supported by the complete self-reviewed [R_F0155 finding](../audits/reviews/Yin_R_F0155_v1.md#conclusion).
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

For the actual A-positive tuple of [C_F0150](../claims/Yin_C_F0150_v1.md#statement), the full target F question is now positively resolved by [C_F0152's adopted proof](../claims/Yin_C_F0152_v1.md#decision-reviewed), with the complete self-reviewed [R_F0160 finding](../audits/reviews/Yin_R_F0160_v1.md#conclusion).
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

## A mixed coassociativity obstruction to matrix realification

A possible way to obtain the selfadjoint contraction estimate would be to realize a given complex word-cut derivation as a constant matrix coefficient of a single real coassociative derivation in an amplification.
The following algebraic obstruction already applies to one Haar unitary, for which the ACSY and full-domain conditions both hold.

Let \(B\) be a unital star algebra and let \(D:M_n(B)\to M_n(B)\otimes_{\rm alg} M_n(B)\) be an outer derivation vanishing on the constant matrix units \(e_{ab}\).
There are unique outer derivations \(d_{kl}:B\to B\otimes_{\rm alg}B\) such that
\[
 D(e_{ab}x)=\sum_{k,l}(e_{ak}\otimes e_{lb})d_{kl}(x).
\]
Here \((e_{ak}\otimes e_{lb})(u\otimes v)\) denotes \(e_{ak}u\otimes e_{lb}v\).
Indeed \(D(e_{11}x)\) has outer supports \(e_{11}\) on both sides, the matrix unit identities transport its coefficients to every \(a,b\), and the product rule on \(e_{11}B\) gives the product rule for each coefficient.
For \(d^\#(x)=d(x^*)^\dagger\), where \((u\otimes v)^\dagger=v^*\otimes u^*\), reality of \(D\) gives \(d_{kl}^\#=d_{lk}\).
Comparing the coefficients of \(e_{ai}\otimes e_{jk}\otimes e_{lb}\) in the two iterates of a coassociative \(D\) gives
\[
 (d_{ij}\otimes{\rm id})d_{kl}=({\rm id}\otimes d_{kl})d_{ij}.
\]
This identity is bilinear in the ordered pair of coefficient derivations, so every constant linear combination \(\delta\) of them must satisfy \((\delta\otimes{\rm id})\delta^\#=({\rm id}\otimes\delta^\#)\delta\).
The standard joint coassociativity identity for multivariable generalized difference quotient rings appears in [Mai and Speicher, Definition 3.1(i), equation (3.1)](https://arxiv.org/pdf/1910.07570).
Here its necessity follows directly from the three matrix coefficients.

On the Laurent algebra of a Haar unitary \(U\), the unique normalized derivation has \(\delta U=1\otimes1\), \(\delta U^*=-U^*\otimes U^*\), and hence \(\delta^\#U=-U\otimes U\).
The two required mixed iterates at \(U\) are \(-1\otimes1\otimes U\) and zero.
The word cuts of \(U^m\) have total product trace \(1\) for \(m=1\) and zero otherwise, giving the actual vacuum \(U\) on the Laurent core.
The unitary equivalence in [C_F0071 v2, Part D](../claims/Yin_C_F0071_v2.md#statement) gives the full-domain dual.
Thus even in this example no finite matrix size allows such a constant-coefficient realization.
For the ordinary Hermitian block \(Y=e_{12}X+e_{21}X^*\), a scalar-coordinate prescription \(DY=1\otimes1\) fails already at first order if \(D\) annihilates \(G=e_{11}-e_{22}\).
Differentiating \(GY+YG=0\) would give \(G\otimes1+1\otimes G=0\), contradicted in the \(e_{11}\otimes e_{11}\) corner.
These obstructions concern the fixed matrix-unit construction.
Coefficients depending on the tuple or a larger algebra with different domain and compression data require separate arguments.

<a id="noisy-jordan-finite-matrix-correction"></a>
## Finite matrix corrections to the noisy Jordan witnesses

For \(B=M_k(\mathbb C)\) with normalized trace, \(J=\sum_{i=1}^{k-1}e_{i,i+1}\), a free standard circular element \(c\), and \(Z=J+\varepsilon c\), let \(d_k(\varepsilon)\) be the infimum of the actual ACSY vacuum norm on \(N=W^*(Z)\).
The [fixed noisy Jordan result](../claims/Yin_C_F0213_v1.md#statement) gives the closed-kernel formula for this infimum and the order \(\varepsilon^{-1}\) of the bounded-dual cost \(\beta(Z)\) at fixed \(k\).
The following development lies outside that result's [independent review](../audits/reviews/Yin_R_F0221_v1.md#whole-proof-finding).
Writing \(H_k=\sum_{m=1}^k m^{-1}\), the estimates obtained here are
\[
   \limsup_{\varepsilon\downarrow0}\varepsilon d_k(\varepsilon)
       \le k^{-1/2},\qquad
   \limsup_{\varepsilon\downarrow0}\varepsilon\beta(Z)
       \le (H_k/k)^{1/2}.
\]

Put \(H_B=L^2(B)\) and \(G_B=H_B\otimes_2H_B\).
Use the outer actions on \(G_B\), the commutator sign \([E,L_Z]=P_\Omega\), and the map \(\Theta(a\otimes b)h=a\tau(bh)\) onto Hilbert--Schmidt operators.
Set \(A\eta=J\eta-\eta J\), \(v=P_{\ker A^*}(1\otimes1)\), and choose \(\eta\in G_B\) with \(A\eta=1\otimes1-v\), which exists in finite dimension.
At fixed inner indices \(i,j\), identify \(e_{ai}\otimes e_{jt}\) with the endpoint matrix unit \(e_{at}\).
Each tensor basis vector has norm \(1/k\), and on this copy \(A\) is \(m\mapsto Jm-mJ\).
Its adjoint kernel is the commutant of \(J^*\), spanned by the orthogonal matrices \((J^*)^l=\sum_{a=1}^{k-l}e_{a+l,a}\), \(0\le l<k\), as follows by equating adjacent matrix entries in the commutation equation.
The component of \(1\otimes1\) at inner indices \(i,j\) corresponds to \(e_{ij}\).
Its projection is zero for \(i<j\), and otherwise is \((J^*)^{i-j}/(k-i+j)\).
Consequently
\[
 v=\sum_{l=0}^{k-1}\frac1{k-l}
         \sum_{a,j=1}^{k-l} e_{a+l,j+l}\otimes e_{ja},
 \qquad
 \|v\|_2^2=\frac1{k^2}\sum_{l=0}^{k-1}
                       \frac{(k-l)^2}{(k-l)^2}=\frac1k .
\]

Work on \(\widehat H=L^2(B*W^*(c))\), writing \(\rho(b)h=hb\) for actual right multiplication.
For \(S=-\Theta\eta\) on \(H_B\), take its right-factor lift \(\widehat S\) in the [pointed free product](../audits/literature/Voi98/Yin_U005.md#voi98-u005).
The opposite-end commutator identity gives \([\widehat S,L_b]=\Theta(b\eta-\eta b)\) for \(b\in B\), where \(\Theta\) now acts on \(\widehat H\) with the same matrix tensor, supported on \(H_B\).
Indeed \([-\Theta\eta,L_b]=L_b\Theta\eta-\Theta\eta L_b\) on \(H_B\), and the same-factor commutator is zero on its orthogonal complement.
Also \([\widehat S,L_c]=[\widehat S,L_{c^*}]=0\), \(\widehat S\Omega=S\Omega\), \(\widehat S^*\Omega=S^*\Omega\), and \(\|\widehat S\|=\|S\|\).

Let \(R\) be the norm-one right circular deletion lifted from [the circular Fock construction](../claims/Yin_C_F0213_v1.md#argument), so \([R,L_c]=P_\Omega\), \([R,L_{c^*}]=0\), and \(R\) commutes with left \(B\).
For \(w=\sum_s a_s\otimes b_s\in G_B\) put \(D_w=\sum_s\rho(a_s)R\rho(b_s)\).
Right multiplication commutes with every left multiplier, giving
\[
   [D_w,L_c]=\sum_s \rho(a_s)P_\Omega\rho(b_s)=\Theta w,\qquad
   [D_w,L_{c^*}]=[D_w,L_b]=0\quad(b\in B).
\]
In particular \(\widehat E=\widehat S+\varepsilon^{-1}D_v\) has \([\widehat E,L_Z]=\Theta(A\eta+v)=P_\Omega\) and \([\widehat E,L_{Z^*}]=\Theta(J^*\eta-\eta J^*)\).

To compute the vacuum and norm of \(D_v\), decompose \(\widehat H\) into levels
\[
       H_B\otimes(\mathbb C^2\otimes H_B)^{\otimes n},\qquad n\ge0 .
\]
Splitting every \(B\) slot as \(\mathbb C1\oplus H_B^\circ\) recovers the pointed free-product decomposition by grouping consecutive circular Fock letters separated by scalar slots.
Write \(u,u'\) for the orthonormal circular letters, so \(c=\ell(u)+\ell(u')^*\) in the circular factor.
The lifted \(R\) kills level zero.
On a level with at least one letter, \(R\) removes the last letter \(\chi\) and the last \(B\) slot \(r\), multiplying the remaining word by \(\langle u,\chi\rangle\tau(r)\).
Indeed a centered final \(B\) syllable ends the word in the matrix factor, where the lift acting on a trailing circular vacuum is zero, while a scalar final slot exposes the last circular Fock letter.
Right multiplication by \(b\in B\) multiplies the last \(B\) slot on the right at every level, including level zero.
Thus \(D_w\) kills \(H_B\) and acts at positive levels as the identity on the preceding slots followed by the contraction
\[
       F_w(q\otimes\chi\otimes r)
          =\langle u,\chi\rangle\sum_s q a_s\tau(r b_s).
\]
The respective output levels are orthogonal and the one-letter restriction realizes \(F_w\), so \(\|D_w\|=\|F_w\|\).
In particular \(D_w^*\Omega=\sum_s a_s^*\otimes u\otimes b_s^*\) in level one, of norm \(\|w\|_2\).
This checks both the base-only input and all higher levels.

Let \(Q:\widehat H\to L^2(N)\) be the tracial projection.
As in [the compression argument for \(Z\)](../claims/Yin_C_F0213_v1.md#argument), \(E=Q\widehat E|_{L^2(N)}\) has the exact prescribed commutator on \(Z\) and a Hilbert--Schmidt commutator on \(Z^*\).
The resulting actual derivation on the full represented core is \(\delta p=\Theta^{-1}[E,L_p]\), with starred value \((Q\otimes Q)(J^*\eta-\eta J^*)\).
Here \(Q\) preserves adjoints and the unit, so compressing an ambient rank-one tensor acts by \(Q\) on both legs.
Its actual vacuum vector is
\[
   \xi=E^*\Omega-(E\Omega)^*
      =Q\big(S^*\Omega-(S\Omega)^*+\varepsilon^{-1}D_v^*\Omega\big).
\]
The sign follows from \(\tau(pE\Omega)=\langle(E\Omega)^*,p\rangle\) in the vacuum pairing of \([E,L_p]\), with inner products linear in the second argument.
The first two terms are in the base and the last is in level one.
Since \(\|S\|\le\|\eta\|_2\), this yields
\[
                 d_k(\varepsilon)^2
                    \le4\|\eta\|_2^2+\frac1{k\varepsilon^2}.
\]

For the full-Hilbert norm of the same bounded witness, set
\[
     M_{ja}=\sum_{0\le l\le k-\max(a,j)}
                      \frac{e_{a+l,j+l}}{k-l}.
\]
On the \(u\) letter, \(F_v(q\otimes u\otimes r)=\sum_{j,a}q M_{ja}\tau(r e_{ja})\), and the \(u'\) letter is killed.
At \(r=\sqrt{k}\,e_{aj}\) the map on \(q\) is right multiplication by \(M_{ja}/\sqrt{k}\).
These last-slot vectors are an orthonormal basis, so \(F_vF_v^*\) is right multiplication by \(k^{-1}\sum_{j,a}M_{ja}^*M_{ja}\).
Different \(l\)'s in each product have different row indices, which gives
\[
      \frac1k\sum_{j,a}M_{ja}^*M_{ja}
          =\frac1k\sum_{b=1}^k
                     \left(\sum_{l=0}^{b-1}\frac1{k-l}\right)e_{bb}.
\]
The largest diagonal entry is \(H_k/k\), and hence \(\|D_v\|=(H_k/k)^{1/2}\).
Restricting the compressed operator to \(N\) gives
\[
                 \beta(Z)\le\|S\|+\varepsilon^{-1}(H_k/k)^{1/2}.
\]
Both asymptotic bounds follow with the fixed matrix solution \(\eta\) chosen above.
The full-Hilbert norm calculation concerns this particular deletion, and does not identify the optimal bounded dual or the optimal actual vacuum.
At \(k=2\) the vacuum estimate leaves the zero lower-limit condition in the [fixed result](../claims/Yin_C_F0213_v1.md#statement) unresolved.

<a id="two-circular-palindrome-drift"></a>
## A bounded two-circular palindrome series outside both holomorphic cut domains

The [one-circular coefficient bound](../claims/Yin_C_F0221_v1.md#statement) puts every bounded Hilbert-holomorphic function of one circular generator in its holomorphic cut domain.
With two free standard circular generators \(c_1,c_2\), one can construct an operator-norm convergent holomorphic series outside both such domains.
For a word \(w=w_1\cdots w_n\) in \(\{1,2\}\), write \(c_w=c_{w_1}\cdots c_{w_n}\) and let \(w^{\rm rev}\) denote its reversal.
Set
\[
 F_n=2^{-n/2}\sum_{|w|=n}c_wc_{w^{\rm rev}},\qquad
 n_j=4^j,\qquad B_J=\sum_{j=1}^J 2^{-j}F_{n_j}.
\]
Distinct analytic words give orthogonal unit Fock vectors, so \(\|F_n\|_2=1\).

Use circular letters \(c_i=\ell(u_i)+\ell(v_i)^*\) with \(u_1,u_2,v_1,v_2\) orthonormal.
For an analytic word, a deletion followed to its right by a creation is zero.
Thus the Wick expansion of \(F_n\) has one summand for each split \(0\le k\le2n\) between a creation prefix of length \(k\) and a deletion suffix of length \(2n-k\).
Its operator norm is exactly the scalar matrix norm of the coefficient array \(A_k\) with prefix rows and suffix columns, allowing reversal of the column word for the deletion adjoint.
Indeed the summand factors as the matrix \(A_k\) tensored with the identity on the remaining Fock word, between the row isometries for distinct equal-length prefix creation words and reversed suffix creation words.
For \(k\le n\), different nonzero rows have disjoint column supports because the final \(k\) letters determine the first \(k\) by reflection.
Each row has \(2^{n-k}\) entries of magnitude \(2^{-n/2}\), so \(\|A_k\|=2^{-k/2}\).
Reflection interchanges rows and columns, giving the exact split estimate at every \(k\) and hence
\[
   \|A_k\|=2^{-\min(k,2n-k)/2},\qquad
   \|F_n\|\le2\sum_{k=0}^{n-1}2^{-k/2}+2^{-n/2}
               \le C:=\frac{2}{1-2^{-1/2}} .
\]
In particular \(B_J\to B\in C^*(c_1,c_2)\) in operator norm, with \(\|B-B_J\|\le C2^{-J}\).
The orthogonality of different degrees gives \(\|B\|_2^2=\sum_{j\ge1}4^{-j}=1/3\).

Let \(\partial_i\) be the circular source word cut at \(c_i\), killing the two adjoints and the other generator.
In an analytic polynomial, every cut pair \((A,C)\) for \(\partial_i\) reconstructs the word \(AiC\) and the cut position.
Thus \(\|\partial_i F_n\|_2^2=2^{-n}\sum_{|w|=n}2\#_i(w)=n\).
Different \(n\)'s here also have orthogonal output degree.
Consequently \(\|\partial_i B_J\|_2^2=\sum_{j=1}^J4^{-j}n_j=J\) for each \(i=1,2\).
The closed source cut has squared graph seminorm \(\sum_w\#_{u_i}(w)|h_w|^2\) in the full circular Wick coefficients, by the [marked-letter cut calculation](../claims/Yin_C_F0218_v1.md#the-circular-starred-cut-and-attainment) with the distinguished creation letter \(u_i\).
Hence \(B\notin\operatorname{Dom}\overline{\partial_i}\).
This last conclusion uses the actual closed graph, including approximation by arbitrary source star polynomials.

For the bounded Fock right deletion \(R_i=r(u_i)^*\), \([R_i,L_{B_J}]=\Theta\partial_i B_J\), and these commutators converge in operator norm to \([R_i,L_B]\).
The limit has operator norm at most \(2\|B\|\) and is compact as a norm limit of finite-rank operators.
It is not Hilbert--Schmidt.
Indeed for any cut pair \(A,C\) of analytic words, its matrix coefficient from \(c_C^*\Omega\) to \(c_A\Omega\) is the coefficient of \(AiC\) in \(B\), as follows by taking the limit on these fixed vectors.
The input family \(\{c_C^*\Omega\}\) and the output family \(\{c_A\Omega\}\) are each orthonormal, and the sum of squared matrix coefficients is \(\sum_{j\ge1}4^{-j}n_j=\infty\).

A proposed tuple is \(Y=(c_1,c_2,z+B)\) with an additional free standard circular \(z\).
If a bounded old-coordinate witness \(E:M\to L^2(M)\) exists, its normalized commutators at \(c_1,c_2\) force \([E,L_{B_J}]=[R_i,L_{B_J}]\) on all bounded inputs by the polynomial rule.
The norm approximation of \(B\) therefore forces \([E,L_z]=-[R_i,L_B]\) on those inputs.
This right side is already bounded on the full Hilbert space, so its infinite Hilbert--Schmidt norm alone gives no divergent bound on \(E:M\to L^2(M)\).
On the actual target star algebra \(z=Y_3-B\) need only be an operator-norm limit of polynomial elements.
The divergence for the zero-star source cut does not exclude an actual target derivation with different starred-generator values, and the finite-shear correction does not give such an actual derivation without a bound on its target starred values.
The actual old-coordinate witnesses and bounded old-coordinate costs for this infinite shear remain unresolved here.

For the specific equal-weight correction used in the [finite shear argument](../claims/Yin_C_F0221_v1.md#correcting-the-old-vacuum-through-starred-coordinates), one can decide what happens to all three target starred values.
Fix \(i\in\{1,2\}\), let \(Y^{(J)}=(c_1,c_2,z+B_J)\), and use the actual polynomial reference derivation in the source variables which takes \(c_i\) to \(1\otimes1\), \(z\) to \(-\partial_i B_J\), and every other source letter to zero.
Its old target holomorphic values are normalized and all its target starred values are zero.
For a cut of an analytic word \(P i S\) in \(B_J\), write \(b_{PiS}>0\) for its scalar coefficient and \(P^\star,S^\star\) for the reversed words in the conjugate letters \(v_1,v_2\).
The corresponding term of its actual vacuum is \(-b_{PiS}W(P^\star d S^\star)\), where \(d\) is the \(z\) creation letter, as follows by inserting the adjoint tensor at the \(z\) cut in the Wick vacuum pairing.
The other term of this vacuum is \(c_i\).
For every such word of original degree \(2n\), spread its required positive correction uniformly over the \(2n-1\) starred old letters in \(P^\star d S^\star\).
For a split \(P^\star d S^\star=A v_h C\), add \(b_{PiS}W(A)\otimes W(C)/(2n-1)\) to \(L_{h,J}\), \(h=1,2\).
Distinct corrected vacuum words are distinguished by their single \(d\), so each split reconstructs the cut and its position.
The two circular marked-letter adjoints concatenate at their marked letters, yielding exactly the desired correction to vacuum \(c_i\), with
\[
       \sum_{h=1}^2\|L_{h,J}\|_2^2
              =\sum_{j=1}^J4^{-j}\frac{n_j}{2n_j-1}.
\]
By the polynomial shear chain rule the old target starred values are \(L_{h,J}^\sharp\), and the adjoint, componentwise on both legs, of the third target starred value is
\[
             V_J=\sum_{h=1}^2\sum_{A,C}
                    l^{(h,J)}_{A,C}\,W(A)\operatorname{flip}(\partial_h B_J)W(C),
 \qquad L_{h,J}=\sum_{A,C}l^{(h,J)}_{A,C}W(A)\otimes W(C).
\]
Here the product with the flipped cut uses the outer actions.
Indeed a cut with analytic prefix \(P\) and suffix \(S\) contributes \(c_S^*\otimes c_P^*\) to the corresponding starred cut of \(B_J^*\).
Transposing its insertion by traciality gives the componentwise adjoints in the same order, hence \(c_S\otimes c_P\) on the two legs.

All Wick coefficients of \(V_J\) are nonnegative.
Indeed the coefficients \(b_{PiS}\) and \(l^{(h,J)}_{A,C}\) are nonnegative, and a product of two Wick words is the sum of words obtained by contracting a suffix of the first word against the reversed conjugate prefix of the second.
This follows from the creation-deletion Wick normal form, and each elementary contraction of the chosen letters has coefficient zero or one.
The uncontracted concatenation always occurs with coefficient one.
Choose any nonzero term \(l\,W(A_0)\otimes W(C_0)\) in some \(L_{h,1}\), with \(l>0\).
It continues to occur in \(L_{h,J}\) with coefficient at least \(l\).
For distinct analytic pairs \(S,P\) in the flipped \(\partial_h B_J\), the uncontracted outputs \(W(A_0S)\otimes W(PC_0)\) are distinct orthonormal basis pairs, since the fixed end words may be removed.
Their coefficients in \(V_J\) dominate \(l\) times the respective original cut coefficients, by positivity of every additional term.
It follows that \(\|V_J\|_2^2\ge l^2\|\partial_h B_J\|_2^2=l^2J\).
Thus the equal-weight construction has two uniformly bounded target starred values and an unbounded third one, despite its exact unit vacuum at every finite truncation.
This failure leaves open signed choices depending on the target law, other vacuum representatives, and the unrestricted existence questions above.

<a id="circular-shear-analytic-columns"></a>
### The forced action on analytic words and columns

Let \(c_1,\ldots,c_d,z\) be freely independent standard circulars, \(M=W^*(c_1,\ldots,c_d,z)\), and fix \(1\le i\le d\).
Write \(u_j,v_j\) for the creation letters of \(c_j,c_j^*\) and \(u_z,v_z\) for the corresponding letters of \(z,z^*\).
An analytic word uses only the source generators \(c_1,\ldots,c_d,z\), and its vacuum vector is the tensor word in their \(u\) letters in the same order.
The closed span of these vectors, including the vacuum, is denoted by \(H_+\).
Assume \(B\in W^*(c_1,\ldots,c_d)\) is bounded and \(B\Omega=\sum_w a_w c_w\Omega\), where \(w\) ranges over old analytic words including the empty word.
For \(Y=(c_1,\ldots,c_d,z+B)\), suppose \(E:M\to L^2(M)\) is bounded, \([E,L_{c_j}]=\delta_{ij}P_\Omega\), and \([E,L_{z+B}]=0\) on \(M\).
Normalize by setting \(E_0(p)=E(p)-pE(1)\), which preserves the commutators and gives \(E_0(1)=0\).
For \(B\) in the operator-norm closure of the old analytic polynomials, including the palindrome above, the following formula applies to every such \(E\).
For general \(B\) as just specified, it applies to every ultraweak-to-weak continuous such \(E\).
Whenever a bounded witness exists one can choose one with this continuity by the [bounded word-test theorem](../claims/Yin_C_F0201_v2.md#statement).

There is \(g_i\in W^*(c_1,\ldots,c_d)\) with
\[
       g_i\Omega=\sum_P a_{Pi}c_P\Omega,\qquad \|g_i\|\le 2\|B\|.
\]
To prove this first take a polynomial \(B=F(c)\) and let \(F_i\) denote its polynomial with the displayed last-letter coefficients.
The creation-deletion expansion of \(c_w\) contains one term per split, with its deletion suffix in the original letter order.
Multiplying on the right by \(\ell(v_i)\), the pure creation term yields \(\ell(u_w)\ell(v_i)\).
Every split with a nonempty deletion suffix vanishes unless the last letter of \(w\) is \(i\), in which case the last deletion cancels \(\ell(v_i)\) with coefficient one and the surviving terms sum to \(c_P\) for \(w=Pi\).
Consequently
\[
          F_i(c)=\big(F(c)-F(\ell(u_1),\ldots,\ell(u_d))\big)\ell(v_i).
\]
The norm of \(F(\ell(u))\) on the full Fock space equals its norm on the old \(u\)-letter Fock subspace.
Indeed, splitting off the maximal initial string of old \(u\)'s decomposes the full space into copies of that subspace, one for the empty tail and one for each remaining tensor word starting with a different letter.
On the old \(u\)-letter subspace \(F(c)\) acts exactly as \(F(\ell(u))\), giving \(\|F_i(c)\|\le2\|F(c)\|\).

For arbitrary \(B\) as above, use the simultaneous gauge rotations \(c_j\mapsto e^{it}c_j\), implemented by opposite phases on \(u_j,v_j\) and the identity on the noise letters.
The Fejér averages
\[
        F_N(c)=\sum_{|w|\le N}\left(1-\frac{|w|}{N+1}\right)a_wc_w
\]
have norm at most \(\|B\|\), since they are averages of these rotations by probability kernels.
The coefficient formula follows by evaluating the average on the separating vacuum.
They converge in \(L^2\) by the coefficient expansion and strongly on the representation by the uniform bound and density of bounded right multiples of the vacuum.
Their last-letter polynomials also converge in \(L^2\) by the displayed coefficient prescription, with norms uniformly bounded by \(2\|B\|\), so the same argument gives a bounded strong limit \(g_i\) in the old algebra.
If \(B\) belongs to the analytic polynomial norm closure, its gauge orbit is norm continuous by polynomial approximation, and the Fejér averages converge in operator norm as well.

Let \(R_i=r(u_i)^*\) be full Fock right deletion, with \([R_i,L_{c_j}]=\delta_{ij}P_\Omega\).
For each \(N\), the polynomial rule gives \([E_0,L_{F_N(c)}]=[R_i,L_{F_N(c)}]\) on \(M\).
For a fixed \(h\in M\), the two sides evaluated at \(h\) pass to the limit by norm convergence of \(F_N(c)\) in the norm-closure case.
In the general case bounded strong convergence gives ultraweak convergence of \(F_N(c)h\), and the assumed continuity gives weak convergence of \(E_0(F_N(c)h)\).
Here \(p\mapsto pE(1)\) is also ultraweak-to-weak continuous by normality of the left action.
The other terms pass by strong convergence on their Hilbert vectors.
Thus \([E_0,L_z]=-[R_i,L_B]\) on bounded inputs in each case.
For an analytic source polynomial \(h\), every nonempty analytic word has trace zero.
Either the polynomial rule or right deletion on the concatenated analytic words then gives
\[
            [R_i,L_B](h\Omega)=\tau(h)g_i\Omega .
\]
In fact a nonempty word \(h\) keeps its last letter when any old analytic word is prepended, and the only remaining term, for \(h=1\), is \(R_i(B\Omega)=g_i\Omega\).

Write \(S_j\) and \(S_z\) for right deletion of the indicated \(u\)-letter on \(H_+\), killing the vacuum and words ending in other letters.
For every analytic source polynomial \(p\) the exact normalized action is
\[
              E_0(p)=S_i(p\Omega)-\big(S_z(p\Omega)\big)g_i .
\]
The final product is right multiplication by the bounded old-algebra element \(g_i\).
Indeed the identities on a suffix \(h\) are \(E_0(c_jh)=c_jE_0(h)+\delta_{ij}\tau(h)1\) and \(E_0(zh)=zE_0(h)-\tau(h)g_i\).
Iterating from \(E_0(1)=0\) proves the formula, since only an empty suffix has nonzero trace in a monomial.
The two deletion maps have orthogonal initial subspaces, giving \(\|S_i x\|_2^2+\|S_z x\|_2^2\le\|x\|_2^2\).
Right multiplication by \(g_i\) has Hilbert operator norm at most \(\|g_i\|\), so the displayed action extends continuously from analytic polynomials to all of \(H_+\) with norm at most \(\sqrt{1+4\|B\|^2}\).
For finite analytic source columns this gives
\[
       \sum_k\|E_0(p_k)\|_2^2
          \le (1+4\|B\|^2)\sum_k\|p_k\|_2^2
          \le (1+4\|B\|^2)\left\|\sum_k p_k^*p_k\right\|.
\]
The Hilbert extension computes the actual restriction at every bounded \(p\) with \(p\Omega\in H_+\) when \(E\) is ultraweak-to-weak continuous, by Fejér approximation rotating all source circulars as above.
For arbitrary bounded \(E\) in the norm-closure case it computes the restriction on the analytic polynomial norm closure by norm continuity.
In particular all target analytic polynomials for the palindrome belong to that closure by substitution, and the estimate holds uniformly in their number of free noise letters and in the column length.
This bound controls the analytic restrictions while leaving the mixed starred tests and existence of a witness on the full algebra open.

<a id="koebe-forced-commutator"></a>
## The forced commutator for dilations of the Koebe function

For \(0<t<1\), set \(f_t(z)=z/(1-tz)^2\) and \(Z_t=f_t(c)\) for a standard circular \(c\).
The numerator of \(f_t(z)-f_t(w)\) over the common denominator factors as \((z-w)(1-t^2zw)\), proving univalence on \(|z|<1/t\).
For \(1<r<1/t\) the image of the closed \(r\)-disk is a filled Jordan domain, and the inverse is holomorphic on its neighborhood given by the image of the open \(1/t\)-disk.
The [polynomial form of Runge's theorem](../claims/Yin_C_F0042_v1.md#2-additional-accepted-approximation-input) therefore verifies the inverse approximation in [C_F0218](../claims/Yin_C_F0218_v1.md#statement).
That claim gives attained least vacuum norm one because \(f_t'(0)=1\).
Its forced commutator \([E,L_c]=\Theta U_{g_t}\) has kernel and coefficient matrix
\[
     g_t(z,w)=\frac{(1-tz)^2(1-tw)^2}{1-t^2zw},\qquad
     A_t=\big([z^mw^n]g_t\big)_{m,n\ge0}=(I-tS)^2D_t(I-tS^*)^2 ,
\]
where \(S e_k=e_{k+1}\) on \(\ell^2(\mathbb N_0)\) and \(D_t e_k=t^{2k}e_k\).
Indeed the geometric series supplies the diagonal and the two quadratic factors shift the row and column exponents respectively.
With inner products linear in the second entry, the isometries \(J_+e_m=c^m\Omega\) and \(J_-e_n=(c^*)^n\Omega\) give \((J_-^*h)_n=\tau(c^n h)\) on bounded inputs and \(\Theta U_{g_t}=J_+A_tJ_-^*\) on the whole Hilbert space.
Thus \(\|\Theta U_{g_t}\|_{H\to H}=\|A_t\|\le(1+t)^4\le16\), which also bounds its \(M\to H\) restriction.
In fact \(D_t\to I\) strongly as \(t\uparrow1\), so \(A_t\to(I-S)^2(I-S^*)^2\) strongly and \(\|A_t\|\to16\).
Here \(\|I-S\|\le 2\), and the unit vectors \(x_N=N^{-1/2}\sum_{k=0}^{N-1}(-1)^ke_k\) satisfy \(\|(I+S)x_N\|=\sqrt{2/N}\), giving \(\|(I-S)^2\|=4\).
Hence this particular commutator yields uniformly bounded necessary tests as \(t\uparrow1\).
The behavior of the least full-domain dual cost \(\beta(Z_t)\) would require a further estimate.

There is also a fixed-row bound for every normalized univalent \(f\) on the unit disk.
Write \(g(z,w)=(z-w)/(f(z)-f(w))=\sum_{m,n}g_{mn}z^m w^n\), extending across the diagonal.
For \(|z|=r<1\), let \(\phi_z(s)=(z+s)/(1+\bar z s)\), \(s=\phi_z^{-1}(w)\), and normalize \(f\circ\phi_z\) by subtracting \(f(z)\) and dividing by \((1-r^2)f'(z)\).
The classical growth lower bound for this normalized function gives \(|f(w)-f(z)|\ge(1-r^2)|f'(z)|\,|s|/(1+|s|)^2\), and the distortion lower bound gives \(|f'(z)|\ge(1-r)/(1+r)^3\). [Ma and Minda, MM99, introduction, (1) and (2)](https://doi.org/10.1016/S0377-0427(99)00021-7)
Using \(|w-z|=(1-r^2)|s|/|1+\bar zs|\) yields \(|g(z,w)|\le4(1+r)^3/(1-r)^2\) throughout the \(w\)-disk, including \(w=z\) by continuity.
Cauchy's coefficient formula on the \(z\)-circle with \(r=1/2\) gives \(\sup_{|w|<1}|[z^m]g(z,w)|\le54\,2^m\).
Parseval on circles in \(w\) followed by increasing the radius to one gives \(\big(\sum_n|g_{mn}|^2\big)^{1/2}\le54\,2^m\), also for fixed columns by symmetry.
The fixed-index constants allow growth with the index and leave the full coefficient-matrix norm for the general schlicht class open here.

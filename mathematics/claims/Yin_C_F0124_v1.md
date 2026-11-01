---
author: Yin
---

# Every affine semicircular pencil: strict Hilbert--Schmidt matrix infimum, full complex-coefficient reduction and exact MS24 recovery

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption)

## A Hilbert–Schmidt Constrained Infimum for Affine Semicircular Determinants

<a id="statement"></a>

<a id="yin_c_f0124"></a>
Record kind: authoritative statement and proof of [Yin_C_F0124](#decision-candidate-0004), and source-proposal repair for [Yin_T_F0008](../tasks/Yin_T_F0008_v1.md#continuation-2026-09-12-yin_c_f0121).
Date: 2026-09-13.
Author: root, with the universal comparison proved in the [companion module](#affine-hs-variation-tests).
Current mathematical and review assessments are recorded in the [selected assessment](#decision-candidate-0004); the [complete proof review](../audits/reviews/Yin_R_F0124_v1.md) owns verification evidence.
No mathematical Role is assigned.

The displayed candidate was found in Roland Speicher's [2026-09-09 blog post](https://rolandspeicher.com/2026/09/09/a-story-of-the-determinant-of-operator-valued-semicircular-elements/), registered as [Spe26](../audits/literature/Spe26/Yin_U001.md), which attributes it to ChatGPT and supplies no inspectable proof.
The [source investigation](../ledger/Yin_L_F0029_v1.md) records that provenance and an undefined inverse on the printed nonstrict domain.
We credit that proposal, use a strict domain, and supply project proofs of the global comparison, approximation and capacity reduction.
This is not an independently conceived formula or an accepted theorem imported from that post.

## 1. Exact Formula and Freely Variable Domain

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state.
Let \(s_1,\ldots,s_n\) be free standard semicircular elements, and let \(a,a_1,\ldots,a_n\in M_d(\mathbb C)\) be selfadjoint.
Set
\[
 S=a\otimes1+\sum_j a_j\otimes s_j,\qquad
 \eta(x)=\sum_j a_jxa_j,\qquad
 \langle x,y\rangle_2=\operatorname{tr}_d(x^*y).
\]
The empty noise family is allowed.
Write \(\Delta_d(b)=|\det b|^{1/d}\), and use the normalized trace \(\operatorname{tr}_d\otimes\tau\) for \(\Delta(S)\), with \(\log\Delta(S)=-\infty\) allowed.
For \(b>0\), define \(\mathcal C_b(x)=bxb\) and
\[
 \mathcal B_\eta=\{b>0:\mathcal C_b-\eta\succ0
                 \text{ on the Hilbert--Schmidt space }M_d(\mathbb C)\}.
                                                               \tag{1}
\]
Strict positivity in (1) is positivity of a finite selfadjoint linear map, not positivity preservation on positive matrices.
The domain is nonempty, since sufficiently large scalar multiples of the identity belong to it.
The conclusion is
\[
 \log\Delta(S)=\inf_{b\in\mathcal B_\eta}
 \left\{-\frac12+\log\Delta_d(b)
       +\frac12\langle a,(\mathcal C_b+\eta)^{-1}(a)\rangle_2\right\}.
                                                               \tag{2}
\]
Equivalently, exponentiate (2), using \(e^{-\infty}=0\).
All trial matrices in (1) are freely chosen finite matrices.
No Dyson equation is a constraint in (1).
The inverse in (2) is an inverse of a linear map on the finite matrix space; it is not a matrix inverse of \(b+\eta(b)\).
The infimum need not be attained.

To check that the objective is defined, put
\[
 \Psi=\mathcal C_{b^{-1/2}}\eta\mathcal C_{b^{-1/2}}.
                                                               \tag{3}
\]
This is completely positive and selfadjoint on Hilbert--Schmidt space.
Congruence gives \(I-\Psi\succ0\).
For a completely positive selfadjoint map the spectral radius is its largest eigenvalue, hence \(\|\Psi\|_{2\to2}<1\).
An elementary verification is as follows: on Hermitian \(x\), a selfadjoint Kraus representation gives \(|\langle x,\Psi(x)\rangle_2|\leq\langle |x|,\Psi(|x|)\rangle_2\);
diagonalize \(x\) to obtain this inequality term by term.
Eigenvectors can be chosen Hermitian since the map preserves adjoints.
Thus its most negative eigenvalue has absolute value no larger than its largest positive eigenvalue.
It follows that \(I+\Psi\succ0\), and then \(\mathcal C_b+\eta\succ0\).

This also repairs a genuine boundary defect in the source proposal.
If \(\eta=\operatorname{Ad}(\operatorname{diag}(1,-1))\) and \(b=I_2\), then \(\mathcal C_b-\eta\succeq0\), but \(\mathcal C_b+\eta\) annihilates off-diagonal matrices.
The ordinary inverse printed there does not exist.
We do not silently assign a pseudoinverse or enlarge (1).

## 2. The Global Comparison

The [universal comparison proof](#affine-hs-variation-tests) establishes the following statement for every completely positive, Hilbert--Schmidt selfadjoint covariance \(\Psi\) with \(\|\Psi\|_{2\to2}<1\):
\[
 \log\Delta(c+T_\Psi)
 \leq -\frac12+\frac12\langle c,(I+\Psi)^{-1}(c)\rangle_2,
 \qquad c=c^*.
                                                               \tag{4}
\]
Here \(T_\Psi\) is a centered matrix-valued semicircular element.
A finite selfadjoint Kraus representation exists by a direct identity.
Start with \(\Psi(x)=\sum_jk_jxk_j^*\), write \(k_j=u_j+iv_j\) with \(u_j,v_j\) selfadjoint, and use \(\Psi=\Psi^*\) to obtain \(\Psi(x)=\tfrac12\sum_j(k_jxk_j^*+k_j^*xk_j)=\sum_j(u_jxu_j+v_jxv_j)\).
The companion comparison proof uses only the finite-dimensional minimization part of Yin_C_F0120 for its effective covariance.
It does not use Yin_C_F0120's determinant identity or its later identification with MS24.

For an arbitrary \(b\in\mathcal B_\eta\), apply (4) to
\[
 c=b^{-1/2}ab^{-1/2},\qquad
 T_\Psi=\sum_j(b^{-1/2}a_jb^{-1/2})\otimes s_j.
\]
Bounded determinant multiplicativity and the deterministic congruence give \(\log\Delta(S)=\log\Delta_d(b)+\log\Delta(c+T_\Psi)\).
Moreover, if \(h=(\mathcal C_b+\eta)^{-1}(a)\), then \((I+\Psi)(b^{1/2}hb^{1/2})=c\), and trace cyclicity yields
\[
 \langle c,(I+\Psi)^{-1}(c)\rangle_2
       =\langle a,(\mathcal C_b+\eta)^{-1}(a)\rangle_2.
\]
Consequently each trial value on the right of (2) is at least \(\log\Delta(S)\).
This is the global inequality; identifying a stationary point alone would not establish it.

## 3. A Physical Approximating Sequence

For \(\varepsilon>0\), take the actual expected resolvent
\[
 R_\varepsilon=-E((i\varepsilon I-S)^{-1})=H+iQ,
 \qquad H=H^*,\quad Q>0.
\]
The [Yin_C_F0119 Dyson identity and logarithmic primitive](Yin_C_F0119_v1.md) give
\[
 R_\varepsilon^{-1}=a-\eta(H)-i(\varepsilon I+\eta(Q)),
 \quad
 u_\varepsilon:=\log\Delta_\varepsilon(S)
 =-\log\Delta_d(R_\varepsilon)
     +\tfrac12\langle H,\eta(H)\rangle_2
     -\tfrac12\langle Q,\eta(Q)\rangle_2.
                                                               \tag{5}
\]
Here \(\Delta_\varepsilon(S)=\exp(\tfrac12(\operatorname{tr}_d\otimes\tau) \log(S^2+\varepsilon^2I))\).
Set
\[
 K=Q^{-1/2}HQ^{-1/2},\qquad
 b_\varepsilon=Q^{-1/2}(I+K^2)^{-1/2}Q^{-1/2}>0.
                                                               \tag{6}
\]
Direct multiplication, preserving the order of the factors, proves
\[
 R_\varepsilon b_\varepsilon R_\varepsilon^*=b_\varepsilon^{-1},
 \qquad R_\varepsilon^{-1}=b_\varepsilon R_\varepsilon^*b_\varepsilon.
                                                               \tag{7}
\]
Indeed \(R_\varepsilon=Q^{1/2}(K+iI)Q^{1/2}\), and the middle factors in (7) multiply to \((I+K^2)^{1/2}\).
Comparing (5) and (7) gives
\[
 (\mathcal C_{b_\varepsilon}+\eta)(H)=a,
 \qquad \mathcal C_{b_\varepsilon}(Q)-\eta(Q)=\varepsilon I.
                                                               \tag{8}
\]
These are properties of the chosen approximants, not additional constraints on trial matrices.

For completeness, (8) implies strict admissibility.
With \(\Psi\) as in (3) and \(W=b_\varepsilon^{1/2}Qb_\varepsilon^{1/2}>0\), \(W-\Psi(W)=\varepsilon b_\varepsilon^{-1}>0\).
Conjugating the map by \(x\mapsto W^{1/2}xW^{1/2}\) produces a completely positive map sending \(I\) to at most \((1-\delta)I\), for some \(\delta>0\).
Its operator norm is at most \(1-\delta\), by positivity, and similarity preserves spectral radius.
Since \(\Psi\) is Hilbert--Schmidt selfadjoint, \(I-\Psi\succ0\).
Thus \(b_\varepsilon\in\mathcal B_\eta\).

Taking determinants and real traces in (7) gives
\[
 \log\Delta_d(b_\varepsilon)=-\log\Delta_d(R_\varepsilon),
 \quad
 \operatorname{tr}_d(Hb_\varepsilon Hb_\varepsilon)
   +\operatorname{tr}_d(Qb_\varepsilon Qb_\varepsilon)=1.
\]
Insert (8) in the objective \(\Phi_a(b)\) of (2).
Then
\[
 \Phi_a(b_\varepsilon)=u_\varepsilon
                 -\frac{\varepsilon}{2}\operatorname{tr}_d Q.
                                                               \tag{9}
\]
The spectral theorem gives
\[
 0\leq\varepsilon\operatorname{tr}_dQ
 = (\operatorname{tr}_d\otimes\tau)
       \frac{\varepsilon^2}{S^2+\varepsilon^2I}\leq1.
\]
If \(\log\Delta(S)>-\infty\), the spectral measure has no atom at zero, and dominated convergence makes this expression tend to zero.
Since \(u_\varepsilon\downarrow\log\Delta(S)\), (9) tends to the left of (2).
If \(\log\Delta(S)=-\infty\), the bounded correction in (9) still gives the limit \(-\infty\).
This proves the opposite inequality and the full formula, including zero determinants, once (4) is verified.

## 4. Centered Reduction by Finite Matrix Optimization

This reduction does not use the MS24 determinant formula to prove its own zero-mean specialization.
Define ordinary capacity by
\[
 \operatorname{cap}(\eta)=\inf_{q>0}\frac{\det\eta(q)}{\det q},
\]
including singular outputs and zero capacity.
We prove
\[
 \inf_{b\in\mathcal B_\eta}\log\det b
       =\frac12\log\operatorname{cap}(\eta).
                                                               \tag{10}
\]
All logarithms in this section are unnormalized; both sides of (10) may be \(-\infty\).

The [audited capacity duality argument](../ledger/Yin_L_F0039_v1.md) gives
\[
 \operatorname{cap}(\eta)^{1/d}
 =\inf_{p,q>0}\frac{\operatorname{tr}_d(p\eta(q))}{\Delta_d(p)\Delta_d(q)}.
                                                               \tag{11}
\]
Its determinant variational identity follows directly from arithmetic--geometric mean, with singular outputs treated by a limit.
Hilbert--Schmidt selfadjointness permits a symmetric reduction of (11):
\[
 \operatorname{cap}(\eta)^{1/d}
 =\inf_{q>0}\frac{\operatorname{tr}_d(q\eta(q))}{\Delta_d(q)^2}.
                                                               \tag{12}
\]
Here are the needed details.
The function \(\operatorname{Tr}(p\eta(q))\) is jointly convex along positive-cone paths \(p(t)=p_0^{1/2}e^{tX}p_0^{1/2}\), \(q(t)=q_0^{1/2}e^{tY}q_0^{1/2}\).
Diagonalizing \(X,Y\) separately writes each Kraus term as a sum \(\sum_{k,l}|c_{kl}|^2e^{t(x_k+y_l)}\), with nonnegative coefficients.
Normalize \(\det p=\det q=1\), and join \((p,q)\) to \((q,p)\) along these paths.
Both midpoint coordinates equal \(r=p\#q=p^{1/2}(p^{-1/2}qp^{-1/2})^{1/2}p^{1/2}\), and \(\det r=1\).
The identity \(p\#q=q\#p\) follows from uniqueness of the positive solution of \(rp^{-1}r=q\): the same equation implies \(rq^{-1}r=p\).
Trace symmetry makes the endpoint values equal, so joint convexity gives \(\operatorname{Tr}(r\eta(r))\leq\operatorname{Tr}(p\eta(q))\).
The reverse infimum inequality is immediate by choosing \(p=q\).
This proves (12).

Set \(J_t(q)=-\log\det q+t\operatorname{Tr}q+\tfrac12\operatorname{Tr}(q\eta(q))\), and \(f_t=\inf_{q>0}J_t(q)\).
Scale \(q\) by a positive scalar in (12).
The scalar infimum is explicit and yields
\[
 f_0=\frac d2+\frac12\log\operatorname{cap}(\eta).
                                                               \tag{13}
\]
If the quadratic trace is zero for some \(q\), scaling it to infinity makes \(J_0\) tend to \(-\infty\); otherwise take approximating shapes.
Thus (13) includes zero capacity without an optimizer assumption.

For \(t>0\), the finite-dimensional existence and pathwise convexity proof in [Yin_C_F0120](Yin_C_F0120_v1.md#existence-strict-convexity-along-positive-cone-paths-and-uniqueness) gives the unique minimizer \(q_t>0\), with
\[
 q_t^{-1}=tI+\eta(q_t),\qquad f_t\downarrow f_0\quad(t\downarrow0).
\]
The convergence follows by testing any fixed \(q\), so it holds also if \(f_0=-\infty\).
As in (8), \(b_t=q_t^{-1}\in\mathcal B_\eta\).
Tracing the minimizer equation gives
\[
 \log\det b_t=f_t-\frac d2-\frac t2\operatorname{Tr}q_t.
                                                               \tag{14}
\]
If \(f_0\) is finite, \(0\leq t\operatorname{Tr}q_t\leq f_t-f_0\), because \(J_0(q_t)\geq f_0\).
Hence (14) tends to \(f_0-d/2\).
If \(f_0=-\infty\), (14) tends to \(-\infty\) by its upper bound \(f_t-d/2\).

Conversely, for every \(b\in\mathcal B_\eta\), let \(\Psi\) be (3), with \(\rho=\|\Psi\|_{2\to2}<1\).
Then
\[
 \operatorname{cap}(\Psi)\leq\det\Psi(I)
 \leq\bigl(\operatorname{tr}_d\Psi(I)\bigr)^d\leq\rho^d\leq1.
\]
The [audited capacity scaling identity](../ledger/Yin_L_F0039_v1.md) says \(\operatorname{cap}(\Psi)=\operatorname{cap}(\eta)/(\det b)^2\).
Thus \(\log\det b\geq\tfrac12\log\operatorname{cap}(\eta)\), with the zero-capacity case interpreted in the extended reals.
Combining this bound with (13)--(14) proves (10).

When \(a=0\), the quadratic exponential in (2) is identically one for every trial matrix.
Equation (10) therefore reduces (2) to
\[
 \Delta\left(\sum_j a_j\otimes s_j\right)
   =e^{-1/2}\operatorname{cap}(\eta)^{1/(2d)}.
                                                               \tag{15}
\]
The derivation is entirely at the variational-formula level.
It does not impose a real Dyson equation after setting the constant term to zero, and it includes nonattainment and zero capacity.

## 5. Arbitrary Complex Coefficients and Spectral Shifts

For arbitrary \(a_0,a_1,\ldots,a_n\in M_m(\mathbb C)\), put
\[
 S=a_0+\sum_j a_j\otimes s_j,\quad
 A=\begin{pmatrix}0&a_0\\a_0^*&0\end{pmatrix},\quad
 B_j=\begin{pmatrix}0&a_j\\a_j^*&0\end{pmatrix},\quad
 \Theta(x)=\sum_j B_jxB_j.
\]
Then \(\mathscr H_S=A+\sum_jB_j\otimes s_j\) is selfadjoint in size \(2m\), and \(\mathscr H_S^2=\operatorname{diag}(SS^*,S^*S)\).
Equality of the two singular-value distributions gives \(\Delta_{2m}(\mathscr H_S)=\Delta_m(S)\), including zero determinants.
Applying (2) yields the genuine finite-matrix formula
\[
 \Delta_m(S)=e^{-1/2}
 \inf_{b>0,\,\mathcal C_b-\Theta\succ0}
 \Delta_{2m}(b)
 \exp\!\left[\frac12\operatorname{tr}_{2m}
       \bigl(A(\mathcal C_b+\Theta)^{-1}(A)\bigr)\right].
                                                               \tag{16}
\]
All covariance blocks, including the mixed products \(\sum_j a_jxa_j\), are retained.
Ordinary \(\sum_j a_jxa_j^*\) alone is not substituted when the mean is nonzero.

For \(a_0=0\), write \(\eta_0(x)=\sum_j a_jxa_j^*\).
A finite capacity calculation gives \(\operatorname{cap}(\Theta)=\operatorname{cap}(\eta_0)^2\): apply (12) to \(\Theta\), and average a positive trial matrix with its conjugate by \(J=\operatorname{diag}(I,-I)\) along their positive-cone geodesic.
Since \(\Theta\) commutes with \(\operatorname{Ad}J\), the midpoint is \(J\)-invariant and does not increase the normalized quadratic trace.
It is thus enough to use \(q=\operatorname{diag}(p,r)>0\).
For these matrices,
\[
 \frac{\operatorname{tr}_{2m}(q\Theta(q))}{\Delta_{2m}(q)^2}
  =\frac{\operatorname{tr}_m(p\eta_0(r))}{\Delta_m(p)\Delta_m(r)}.
\]
Equation (11), which does not require selfadjointness of \(\eta_0\), identifies this infimum as \(\operatorname{cap}(\eta_0)^{1/m}\).
This proves the asserted square identity, including zero capacity.
Consequently (16) reduces exactly to the full original-coefficient MS24 formula
\[
 \Delta_m\left(\sum_j a_j\otimes s_j\right)
 =e^{-1/2}\operatorname{cap}(\eta_0)^{1/(2m)}.
                                                               \tag{17}
\]

For spectral potentials, set \(a_0=-zI_m\) in (16).
This expresses \(u(z)=\log\Delta_m(\sum_j a_j s_j-zI_m)\) as the same infimum, with a mean-independent feasible set.
Its distributional Laplacian gives the Brown measure with the conventions and accepted foundations of [Yin_C_F0123](Yin_C_F0123_v1.md).
No differentiation of an unattained infimum is asserted.
The finite regularized derivative system in Yin_C_F0123 remains the justified computational interface.
Brown support and full operator spectrum remain distinct.

## 6. Relation to Yin_C_F0121 and Proof Boundary

Formula (2) applies to every selfadjoint affine pencil, including indefinite pencils and zero determinants.
On the strictly positive regime of [Yin_C_F0121](Yin_C_F0121_v1.md), its physical inverse \(q=E(S^{-1})\) satisfies \(q^{-1}=a-\eta(q)\).
The stability estimate in that proof gives \(\rho(\mathcal C_{q^{1/2}}\eta\mathcal C_{q^{1/2}})<1\), so \(b=q^{-1}\) is an admissible, attained minimizer of (2).
Its value agrees with Yin_C_F0121 by the traced Dyson identity.
Yin_C_F0121 retains the additional positivity certificate and its own matrix supersolution domain; no equality of the two trial domains is claimed.

The proof uses the already reviewed finite Dyson primitive Yin_C_F0119, the finite-dimensional positive-cone minimization proof in Yin_C_F0120, bounded determinant and capacity foundations, and the newly proved comparison in the companion module.
It does not use the source proposal as a theorem.
The capacity reduction above uses finite matrix identities rather than assuming MS24's determinant conclusion.
Nonattainment is retained in (2), (10) and (16).
The linked independent review checks this entire chain; the goal record separately owns contract completion.

## 7. Exact Normalization and Degeneracy Checks

For a deterministic scalar \(a\), the covariance is zero and (2) becomes the infimum of \(-1/2+\log b+a^2/(2b^2)\) over \(b>0\).
It equals \(\log|a|\) at \(b=|a|\) if \(a\ne0\); for \(a=0\) it is \(-\infty\).
Thus the constant and zero-determinant convention are correct even for empty noise.

For scalar covariance \(\eta(x)=\sigma x\), \(\sigma>0\), put \(x=b^2>\sigma\).
The objective is
\[
 -\frac12+\frac12\log x+\frac{a^2}{2(x+\sigma)}.
\]
Its derivative is \(((x+\sigma)^2-a^2x)/(2x(x+\sigma)^2)\).
If \(|a|\leq2\sqrt\sigma\), the infimum is the boundary limit \(-1/2+(\log\sigma)/2+a^2/(4\sigma)\).
If \(|a|>2\sqrt\sigma\), it is attained at
\[
 x=\frac{a^2-2\sigma+|a|\sqrt{a^2-4\sigma}}2>\sigma.
\]
These are exactly the bulk, edge and exterior values of Yin_C_F0122.
Strict feasibility does not incorrectly force boundary attainment.

For the standard circular element \(c=(s_1+is_2)/\sqrt2\), the hermitized covariance sends \(\operatorname{diag}(p,q)\) to \(\operatorname{diag}(q,p)\) and annihilates off-diagonal matrices.
With \(a_0=-z\), the scalar trial family \(b=tI_2\), \(t>1\), in (16) has logarithmic objective
\[
 -\frac12+\log t+\frac{|z|^2}{2t^2}.
\]
Its infimum is \((|z|^2-1)/2\) for \(|z|\leq1\), and \(\log|z|\) for \(|z|\geq1\).
This agrees with the already justified circular specialization of the [Yin_C_F0123 elliptic benchmark](Yin_C_F0123_v1.md).
The global comparison proves that no other admissible trial matrix can lower these known exact values.
The match checks a genuinely nonselfadjoint family and the spectral boundary, rather than only a real scalar shift.

The finite matrix reduction (10)--(17) separately verifies arbitrary complex centered coefficients, singular covariance maps, zero capacity, and nonattainment.
These checks are consequences or independent benchmarks of the complete proof, not a replacement for its general inequalities.


## Argument: affine-hs-variation-tests


<a id="affine-hs-variation-tests"></a>
## A Global Upper Bound for the Affine Hilbert-Schmidt Variation

Record kind: project proof module and bounded exploration record.
Date: 2026-09-13.
Author: yin_t_f0008-contract agent, with the coordinating agent supplying the determinant-one structure on the support of the real resolvent.
Goal: [Yin_T_F0008](../tasks/Yin_T_F0008_v1.md#yin_t_f0008).
No Claim ID or mathematical Role is assigned here; registration and current assessment belong to the coordinating agent and the Claim index.

The candidate variational expression was found in Roland Speicher's [9 September 2026 post](https://rolandspeicher.com/2026/09/09/a-story-of-the-determinant-of-operator-valued-semicircular-elements/).
The post presents an AI-generated proposal and supplies no proof for inspection.
It is a source of the candidate, not an accepted theorem input.
The proof below is a project deduction.
It uses the existing [Yin_C_F0119 Dyson primitive](Yin_C_F0119_v1.md#yin_c_f0119) and the finite-dimensional minimization argument of [Yin_C_F0120](Yin_C_F0120_v1.md#existence-strict-convexity-along-positive-cone-paths-and-uniqueness).
The later Yin_C_F0120 comparison with MS24 is not a premise of this upper bound.

## Statement and normalization

Let \(\Psi:M_m(\mathbb C)\to M_m(\mathbb C)\) be completely positive and selfadjoint for the Hilbert-Schmidt inner product.
Assume
\[
 \rho:=\|\Psi\|_{2\to2}<1.
\]
Choose selfadjoint Kraus matrices \(c_j\) with \(\Psi(X)=\sum_jc_jXc_j\), and let \(T=\sum_jc_j\otimes s_j\), where the \(s_j\) are free standard semicircular elements in a faithful normal tracial probability space.
Such Kraus matrices always exist for a completely positive Hilbert-Schmidt selfadjoint map: average any Kraus representation with its adjoint representation, then write each Kraus matrix as its real and imaginary Hermitian parts.

Write \(\operatorname{tr}_m=\operatorname{Tr}/m\), \(\varphi=\operatorname{tr}_m\otimes\tau\), and
\[
 \ell_\varepsilon(a)=\frac12\varphi\log((a+T)^2+\varepsilon^2I),
 \qquad K=I+\Psi,
 \qquad a=a^*.
\]
Here \(I\) in \(K\) denotes the identity linear map.
All unnormalized traces below are ordinary finite-matrix traces, including traces on corners.
Then
\[
 \boxed{
 \ell_\varepsilon(a)-\frac12\operatorname{tr}_m(aK^{-1}(a))
 \le -\frac12+\frac{\varepsilon+\varepsilon^2/2}{1-\rho}
 \quad(\varepsilon>0).
 }                                                        \tag{1}
\]
Consequently, including the extended-real case of zero determinant,
\[
 \boxed{
 \log\Delta_\varphi(a+T)
 \le -\frac12+\frac12\operatorname{tr}_m(aK^{-1}(a)).
 }                                                        \tag{2}
\]
The constant in (1) is a convenient uniform error bound, not an asserted sharp estimate.

## A finite-dimensional inverse comparison

Let \(A=A^*\) be a linear operator on a finite-dimensional Hilbert space with \(\|A\|\le\rho<1\), and let \(J=J^*=J^{-1}\).
Then
\[
 L=(J-A)^{-1}\le(I-A)^{-1},
 \qquad \|L\|\le(1-\rho)^{-1}.                              \tag{3}
\]
For the norm bound, use \(J-A=J(I-JA)\) and the norm-convergent geometric series.
For the order comparison put \(D_0=I-A>0\), \(P=(I-J)/2\).
The resolvent identity for a finite-rank perturbation gives
\[
 (D_0-2P)^{-1}
 =D_0^{-1}
 +2D_0^{-1}P
   (I_{P\mathcal H}-2PD_0^{-1}P)^{-1}P D_0^{-1}.             \tag{4}
\]
The inverse in the middle is on \(P\mathcal H\).
Since \(D_0^{-1}\ge(1+\rho)^{-1}I>\tfrac12I\), that middle operator is strictly negative.
Thus the correction in (4) is negative semidefinite.
Formula (4) can also be verified by multiplying by \(D_0-2P\); if \(P=0\), its correction is absent.

If, additionally, \(A\) is a completely positive map on a matrix algebra and \(J(X)=UXU\) for a selfadjoint unitary \(U\), then \(L\) is completely positive because
\[
 L=\sum_{k\ge0}(JA)^kJ.                                    \tag{5}
\]
Each summand is completely positive, and the completely positive cone is norm closed in finite dimensions.
This does not assert that \(L\) is positive as a Hilbert-Schmidt operator; (3), rather than that false implication, is what will be used.

## Maximize over the deterministic mean

For fixed \(\varepsilon>0\), define
\[
 F_\varepsilon(a)
 =\ell_\varepsilon(a)-\tfrac12\operatorname{tr}_m(aK^{-1}(a))
 \quad(a=a^*).
\]
It is continuously differentiable and attains a global maximum.
Indeed, \(K^{-1}\ge(1+\rho)^{-1}I\), whereas
\[
 \ell_\varepsilon(a)
 \le\tfrac12\log((\|a\|+\|T\|)^2+\varepsilon^2).
\]
Thus \(F_\varepsilon(a)\to-\infty\) as the Hilbert-Schmidt norm of \(a\) tends to infinity, and continuity gives attainment in the finite-dimensional real space of Hermitian matrices.

Fix any such maximizer.
Set
\[
 R=E[((a+T)-i\varepsilon I)^{-1}]=H+iQ,
 \qquad H=H^*,\quad Q>0,
 \qquad E=\operatorname{id}\otimes\tau.
\]
Tracing the derivative of \(\tfrac12\log((a+T)^2+\varepsilon^2I)\) in a Hermitian direction \(h\) gives \(\operatorname{tr}_m(Hh)\).
In fact the traced derivative of a logarithm at a positive invertible operator is the trace of its inverse times its derivative; cyclicity then combines the two factors of \(a+T\).
Therefore stationarity is precisely
\[
 H=K^{-1}(a).
\]
The physical Dyson equation, with this resolvent sign, is
\[
 R^{-1}=a-\Psi(R)-i\varepsilon I.
\]
Consequently at the maximum
\[
 R^{-1}=H-iB,
 \qquad B=\Psi(Q)+\varepsilon I>0.                          \tag{6}
\]
The Yin_C_F0119 primitive applies directly in dimension \(m\) to this selfadjoint pencil and gives
\[
 \ell_\varepsilon(a)
 =-\frac1m\log|\det R|
  +\frac1{2m}\operatorname{Tr}(H\Psi(H)-Q\Psi(Q)).            \tag{7}
\]
Taking the real part of the trace of \(R R^{-1}=I\) in (6) gives \(\operatorname{Tr}(H^2+Q\Psi(Q))+\varepsilon\operatorname{Tr}Q=m\).
Subtracting the quadratic mean term in (7) now yields
\[
 F_\varepsilon(a)
 =-\frac12-\frac1m\log|\det R|
       +\frac{\varepsilon}{2m}\operatorname{Tr}Q.             \tag{8}
\]
This argument applies to a global maximum at positive regularization.
No differentiability of the unregularized logarithmic determinant is assumed.

## The support of the real resolvent contributes determinant one

Multiply (6) in both orders.
Subtraction first gives
\[
 [Q,B]+i[Q+B,H]=0.
\]
The first summand is skewadjoint and the second is selfadjoint, so both vanish.
Consequently \(QB=BQ\), and \(QH-HB\) is selfadjoint because its adjoint difference is \([Q+B,H]=0\).
We may now separate the selfadjoint and skewadjoint parts in
\[
 H^2+QB+i(QH-HB)=I.
\]
Taking an adjoint as well yields
\[
 QB=BQ=I-H^2,\qquad QH=HB,\qquad HQ=BH.                     \tag{9}
\]
In particular \(Q\) and \(B\) commute with \(H^2\).
Let \(e\) be the support projection of \(H\), let \(f=I-e\), and write \(d=\operatorname{rank}e\), \(r=\operatorname{rank}f\).
Both projections reduce \(Q,B,R\).

On the \(e\)-corner let \(U=\operatorname{sign}(H_e)\).
Because \(Q_e\) commutes with \(|H_e|\), the identity \(Q_eH_e=H_eB_e\) implies
\[
 B_e=UQ_eU.
\]
Thus \(R_e^{-1}=U R_e^* U\).
Taking absolute determinants proves \(|\det R_e|=1\).
On the \(f\)-corner, \(H_f=0\), so (9) gives
\[
 R_f=iQ_f,\qquad B_f=Q_f^{-1}.
\]
We conclude
\[
 \log|\det R|=\log\det Q_f.                                \tag{10}
\]
If \(f=0\), the right side is zero; the corresponding corner terms below are omitted.

## Eliminate the support corner

Use the direct sum of corner Hilbert spaces \(M_e\oplus M_f\), with unnormalized Hilbert-Schmidt inner products.
Let
\[
 \Psi_{uv}(X)=u\Psi(vXv)u\quad(u,v\in\{e,f\}).
\]
The compression of \(\Psi\) to this direct sum is selfadjoint and has norm at most \(\rho\); the two off-diagonal corner maps are adjoints of one another.
Each corner map is completely positive between the corresponding matrix algebras.

Assume first \(e\ne0\), and put
\[
 A=\Psi_{ee},\qquad J(X)=UXU,\qquad L=(J-A)^{-1}.
\]
By (3)-(5), \(L\) is selfadjoint as a Hilbert-Schmidt operator, completely positive, has norm at most \((1-\rho)^{-1}\), and satisfies \(L\le(I-A)^{-1}\).
The \(e\)-part of \(B=\Psi(Q)+\varepsilon I\) solves explicitly as
\[
 Q_e=L\Psi_{ef}(Q_f)+\varepsilon L(I_e).                     \tag{11}
\]
Define maps and matrices on the \(f\)-corner by
\[
 \Phi=\Psi_{ff}+\Psi_{fe}L\Psi_{ef},
 \qquad D=I_f+\Psi_{fe}(L(I_e)).                             \tag{12}
\]
Then \(\Phi\) is completely positive and Hilbert-Schmidt selfadjoint, and \(D\ge I_f>0\).
Moreover
\[
 I_f-\Phi>0                                                \tag{13}
\]
as a Hilbert-Schmidt operator.
To verify this, the strictly positive block operator \(I-\Psi|_{M_e\oplus M_f}\) has Schur complement
\[
 I_f-\Psi_{ff}-\Psi_{fe}(I_e-A)^{-1}\Psi_{ef}>0.
\]
Replacing \((I_e-A)^{-1}\) by the smaller selfadjoint operator \(L\) preserves strict positivity.
This proves (13).
In particular,
\[
 \operatorname{Tr}\Phi(I_f)<r\quad\text{if }r>0.              \tag{14}
\]

The \(f\)-equation and the trace of (11) are
\[
 Q_f^{-1}=\Phi(Q_f)+\varepsilon D,
 \qquad
 \operatorname{Tr}Q
   =\operatorname{Tr}(DQ_f)+\varepsilon\operatorname{Tr}L(I_e).
                                                               \tag{15}
\]
For the trace identity, Hilbert-Schmidt selfadjointness of \(L\) and the adjoint relation \(\Psi_{ef}^*=\Psi_{fe}\) move \(L\Psi_{ef}\) from \(Q_f\) to \(I_e\).
If \(e=0\), set \(\Phi=\Psi\), \(D=I_m\), and omit every term involving \(L\); equations (13)-(15) retain the same meanings.

## Apply the established positive-cone minimum

Suppose \(r>0\).
A completely positive Hilbert-Schmidt selfadjoint map \(\Phi\) admits selfadjoint Kraus matrices, as explained above.
Therefore the finite-dimensional part of Yin_C_F0120 applies to
\[
 J(X)=-\log\det X+\varepsilon\operatorname{Tr}(DX)
                     +\tfrac12\operatorname{Tr}(X\Phi(X)),
 \qquad X>0.
\]
Equation (15) says that \(Q_f\) is its unique minimizer.
Comparing with the freely chosen trial matrix \(I_f\), and tracing (15) after multiplication by \(Q_f\), gives
\[
 \log\det Q_f
 \ge\frac\varepsilon2\operatorname{Tr}(DQ_f)
    -\varepsilon\operatorname{Tr}D
    +\frac12\bigl(r-\operatorname{Tr}\Phi(I_f)\bigr).          \tag{16}
\]
Thus (8), (10), (14), and the exact trace cancellation in (15) imply
\[
 F_\varepsilon(a)
 \le-\frac12+\frac\varepsilon m\operatorname{Tr}D
             +\frac{\varepsilon^2}{2m}\operatorname{Tr}L(I_e).
                                                               \tag{17}
\]
This is the step that controls the kernel of \(H\).
A claim that \(H\) is always invertible is neither used nor needed.
If \(f=0\), (8), (10), and (11) directly give (17) with the \(D\)-term absent.

Both error coefficients are uniform over all maximizing means and their spectral projections.
The unnormalized Hilbert-Schmidt norm of a rank-\(d\) identity is \(\sqrt d\).
Complete positivity gives the nonnegative traces, and the norm bounds give
\[
 \begin{aligned}
 0\le\operatorname{Tr}L(I_e)&\le\frac d{1-\rho},\\
 \operatorname{Tr}D
 &\le r+\frac{\rho\sqrt{dr}}{1-\rho}
 \le\frac m{1-\rho}.
 \end{aligned}                                             \tag{18}
\]
The last, deliberately coarse bound follows from \(r\le m\) and \(\sqrt{dr}\le m\).
If either corner is absent the same estimates hold under the omission convention.
Substitution into (17) proves (1) at the maximum and hence at every mean.
Finally, \(\ell_\varepsilon(a)\downarrow\log\Delta_\varphi(a+T)\) by scalar spectral calculus, proving (2).

## Connection to a freely chosen positive matrix

For the original selfadjoint coefficients, let \(\eta(X)=\sum_ja_jXa_j\) and fix any positive definite \(b\) satisfying strict Hilbert-Schmidt positivity of \(\mathcal C_b-\eta\), where \(\mathcal C_b(X)=bXb\).
Put
\[
 W(X)=b^{1/2}Xb^{1/2},\quad
 \Psi=W^{-1}\eta W^{-1},\quad c=b^{-1/2}ab^{-1/2}.
\]
Then \(I-\Psi=W^{-1}(\mathcal C_b-\eta)W^{-1}>0\).
This implies \(\|\Psi\|_{2\to2}<1\), with an elementary check that does not assume Hilbert-Schmidt positivity of \(\Psi\).
Each eigenvalue has a nonzero Hermitian eigenmatrix \(X\), since \(\Psi\) preserves adjoints and its eigenvalues are real.
Write \(X=X_+-X_-\).
Positivity of \(\Psi\) and nonnegativity of the trace of a product of positive matrices give
\[
 |\operatorname{Tr}(X\Psi(X))|
 \le\operatorname{Tr}(|X|\Psi(|X|))
 \le\lambda_{\max}(\Psi)\operatorname{Tr}(X^2).
\]
For the first inequality, expand both quadratic forms: the positive-part diagonal terms and the mixed term are nonnegative, and only the sign of twice the mixed term changes.
Thus every eigenvalue has absolute value at most \(\lambda_{\max}(\Psi)<1\).

Determinant multiplicativity and the finite-dimensional congruence identity give
\[
 \log\Delta(a+\textstyle\sum_ja_js_j)
 =\log\Delta_m(b)+\log\Delta(c+\textstyle\sum_jb^{-1/2}a_jb^{-1/2}s_j),
\]
\[
 \operatorname{tr}_m(c(I+\Psi)^{-1}(c))
 =\operatorname{tr}_m(a(\mathcal C_b+\eta)^{-1}(a)).
\]
Consequently (2) supplies the required upper bound at every strictly feasible trial matrix.
The reverse inequality, approximation by physical resolvents, full complex-coefficient reduction, and MS24 comparison are separate obligations owned by the coordinating agent's main module.
They are not inferred solely from this bound.

## Exploratory checks and retained boundary

A preliminary numerical search used NumPy's random generator with seed 12345, 160 size-two Hermitian coefficient families with one to four Kraus matrices, covariance spectral radius scaled into \((0.05,0.999)\), and Hermitian means with varied scale.
Damped physical Dyson iteration at decreasing positive regularization, ending at \(10^{-4}\), produced no violations of the limiting upper-bound expression; the smallest observed difference between that expression and the regularized determinant was about 0.0290.
These floating-point checks are motivation only and are not premises of the proof above.

The nonstrict candidate from the source has a genuine definition issue when it uses an ordinary inverse: for \(\eta(X)=\sigma_zX\sigma_z\) and \(b=I_2\), \(I-\eta\ge0\) as a Hilbert-Schmidt operator, but \(I+\eta\) annihilates the off-diagonal matrices.
The strict domain used here avoids that issue.
No Moore-Penrose inverse or boundary range convention is silently substituted.


## Assessment history


### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#affine-hs-variation-tests) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](#3-a-physical-approximating-sequence) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0124_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original review classification and limitations: independently reviewed; candidate attributed to Spe26, comparison proof collaborative

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision candidate-0004

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-09-28T02:52 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#affine-hs-variation-tests) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](#3-a-physical-approximating-sequence) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0124_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:09 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#affine-hs-variation-tests) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](#3-a-physical-approximating-sequence) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0124_v1.md#obligations-and-evidence) | Complete main Sections 1–7 and global comparison: every finite size and selfadjoint drift, strict Hilbert–Schmidt trial domain, kernel/support corner comparison, admissible physical approximation, finite capacity reduction and arbitrary complex coefficients after hermitization. Includes empty noise, zero determinants and nonattainment; excludes the source’s undefined nonstrict inverse, a general nonnormal spectrum equality and differentiating an unattained infimum. |


### Decision isolated-whole-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:56 |
| status | proved |
| reason | Adopt the actual newly isolated whole-proof review, formed from direct mathematical inspection before the old obligations were compared. The complete corrected commutator, global comparison, physical approximation and capacity chain are independently covered at their exact accepted-source scope; the statement and proof are unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | The entire original finite-size affine theorem, all hypotheses and stated centered, complex-coefficient and spectral comparisons. |
| argument | [Complete global comparison](#affine-hs-variation-tests) | Full regularized mean-maximization, commutator-first support/kernel proof, effective minimum and uniform estimate at every strictly feasible Hilbert–Schmidt trial. |
| argument | [Physical approximation](#3-a-physical-approximating-sequence) | Complete reverse inequality, exact admissible sequence and finite/minus-infinity limits, together with the unchanged full main Sections1–7. |
| review | [New complete isolated finding](../audits/reviews/Yin_R_F0178_v1.md#affine-infimum-whole-proof) | Exact statement and entire selected proof, necessary Dyson/primitive and finite-minimum interfaces, all dimension, domain, normalization, zero/capacity/complex-coefficient and nonattainment boundaries, without a fresh original-source audit or research Task completion. |

## Historical assessments


These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

Original review classification and limitations: independently reviewed; candidate attributed to Spe26, comparison proof collaborative

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0124_v1.md).

Material covered by that review: [Exact material](#affine-hs-variation-tests); [Exact material](Yin_C_F0124_v1.md).

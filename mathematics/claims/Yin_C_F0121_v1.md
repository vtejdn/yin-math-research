---
author: Yin
---

# Every strictly positive selfadjoint affine pencil: matrix-inequality minimum and positivity certificate

## Current assessment
[Selected decision](#decision-m04-isolated-review)

## A Positive-Matrix Minimum for Selfadjoint Affine Pencils

<a id="statement"></a>

<a id="yin_c_f0121"></a>
The final statement is the [minimum over all matrix supersolutions](#minimum-over-all-matrix-supersolutions); earlier certificate bounds are retained as stages of its proof.
Current assessments are recorded in the [selected assessment](#decision-m04-isolated-review); no mathematical Role is assigned.

Record kind: project deduction and bounded exploration.
Date: 2026-09-12.
Owner: affine-selfadjoint-variation agent.
The user authorized the search for a capacity-like variational formula and prohibited network searches in this round.
This record uses [Yin_C_F0119](Yin_C_F0119_v1.md#yin_c_f0119), its local MS17 interfaces, and explicit deductions below.
It makes no novelty or priority claim.

The [spectral-radius refinement](#spectral-radius-refinement-and-an-intrinsic-feasible-set), added later in the same round following a suggestion from the coordinating agent, replaces the initial sufficient norm bound by an exact finite-matrix feasibility characterization of strict positivity.
The [final matrix-inequality minimum](#minimum-over-all-matrix-supersolutions) then removes the stability constraint from the variational domain altogether.
The earlier proofs are retained as simpler sufficient versions and as the proof of local strictness needed in the final uniqueness argument.

## Setting and a Checkable Matrix Certificate

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state.
Let \(s_1,\ldots,s_n\in M\) be freely independent standard semicircular elements and let \(a_0,\ldots,a_n\in M_m(\mathbb C)\) be selfadjoint matrices.
Set

\[
 S=a_0\otimes1+\sum_j a_j\otimes s_j,
 \qquad \eta(b)=\sum_j a_jba_j.
\]

All matrix traces below are unnormalized; the operator determinant uses \(\varphi_m=\operatorname{tr}_m\otimes\tau\).
Assume there is a **given positive definite matrix** \(R\in M_m(\mathbb C)\) such that

\[
 a_0\ge R^{-1}+\eta(R),
 \qquad
 \kappa=\left\|R^{1/2}\eta(R)R^{1/2}\right\|<1.               \tag{1}
\]

The matrix \(R\) is a feasible-set certificate, not a prescribed Dyson solution.
Both inequalities in (1) can be checked directly from finite matrices.

Under (1), the following is a genuine global minimum over freely chosen positive definite matrices:

\[
 \boxed{
 \log\Delta_{\varphi_m}(S)
 =\frac1m\min_{0<q\le R}
 \left\{
 -\log\det q+\operatorname{Tr}(a_0q)
 -\frac12\operatorname{Tr}(\eta(q)q)-m
 \right\}.}                                                \tag{2}
\]

The minimizer is unique, equals \((\operatorname{id}\otimes\tau)(S^{-1})\), and automatically satisfies

\[
 q^{-1}=a_0-\eta(q).                                        \tag{3}
\]

Equation (3) is a conclusion of optimization, not a feasibility constraint in (2).
The quantity inside braces is real.
In particular, (2) can equivalently be written using only finite-dimensional determinants:

\[
 \boxed{
 \Delta_{\varphi_m}(S)
 =\min_{0<q\le R}
 \left|
 \det\!\left(
 q^{-1}\exp\!\left[a_0q-\tfrac12\eta(q)q-I_m\right]
 \right)
 \right|^{1/m}.}                                           \tag{4}
\]

No commutativity of the factors in (4) is asserted or needed.
The determinant is positive real because its logarithm is the real trace occurring in (2).

This is a sufficient-regime result, not a variational formula for every selfadjoint affine pencil.
In particular, (1) forces strict positivity of \(S\), so it does not include the centered case \(a_0=0\).

## Proof of the Positive Spectral Gap

Put

\[
 b_j=R^{1/2}a_jR^{1/2},\qquad
 K=\sum_j b_j^2=R^{1/2}\eta(R)R^{1/2}.
\]

Use the full Fock realization \(s_j=\ell_j+\ell_j^*\), where \(\ell_i^*\ell_j=\delta_{ij}I\), and set \(T=\sum_j b_j\otimes\ell_j\).
Then \(T^*T=K\otimes1\) and \(\|T\|=\sqrt\kappa<1\).
By (1),

\[
 \begin{aligned}
 (R^{1/2}\otimes1)S(R^{1/2}\otimes1)
 &\ge I+T^*T+T+T^*\\
 &=(I+T)^*(I+T)\\
 &\ge(1-\sqrt\kappa)^2I.
 \end{aligned}                                              \tag{5}
\]

Thus

\[
 S\ge\frac{(1-\sqrt\kappa)^2}{\|R\|}I>0.                    \tag{6}
\]

The same inequality holds in the original tracial model: the matrix semicircular polynomial has the same compactly supported scalar spectral distribution, and faithfulness identifies its support with its spectrum.
Thus using the Fock model does not add a representation-dependent hypothesis.

## Constructing and Identifying the Physical Positive Solution

Start with \(q_0=0\) and iterate

\[
 q_{k+1}=(a_0-\eta(q_k))^{-1}.                               \tag{7}
\]

The map in (7) is order preserving wherever its argument is positive definite.
If \(0\le q\le R\), then

\[
 a_0-\eta(q)\ge a_0-\eta(R)\ge R^{-1},
\]

so the next iterate exists and is at most \(R\).
Induction gives

\[
 0<q_1\le q_2\le\cdots\le R.
\]

Consequently the sequence converges in matrix norm to a positive definite \(q_*\le R\), and continuity yields (3).

For completeness, this fixed point is the actual inverse expectation, not a branch chosen solely because it solves a quadratic equation.
In the Fock model, compress \(S\) to words of length at most \(N\).
These finite matrices retain the uniform positive lower bound (6).
Separate the vacuum from the subtrees obtained by fixing the last letter.
Each subtree has the same truncated pencil with one fewer level; Schur complementation at the vacuum therefore gives precisely the recursion (7).
The vacuum block of the inverse of the depth-\(N\) compression is \(q_{N+1}\).

The compressions, extended by a fixed positive scalar on their orthogonal complements, converge strongly to \(S\), remain uniformly bounded, and have the same uniform inverse bound.
Their inverses converge strongly to \(S^{-1}\), using the resolvent identity.
Taking vacuum matrix coefficients proves

\[
 q_*=(\operatorname{id}\otimes\tau)(S^{-1}).                 \tag{8}
\]

This also covers \(n=0\): the iteration immediately gives \(q_*=a_0^{-1}\).

## Strict Convexity on the Certified Order Interval

Write the objective in braces in (2) as \(J(q)\).
For every selfadjoint increment \(h\), its first derivative is

\[
 DJ(q)[h]
 =\operatorname{Tr}\bigl((-q^{-1}+a_0-\eta(q))h\bigr),         \tag{9}
\]

because \(\operatorname{Tr}(\eta(x)y)=\operatorname{Tr}(x\eta(y))\).
Its Hessian is

\[
 D^2J(q)[h,h]
 =\operatorname{Tr}(q^{-1}h q^{-1}h)
  -\operatorname{Tr}(\eta(h)h).                              \tag{10}
\]

Set \(q=R^{1/2}pR^{1/2}\) and \(h=R^{1/2}kR^{1/2}\).
Since \(0<p\le I\), diagonalizing \(p\) shows

\[
 \operatorname{Tr}(p^{-1}k p^{-1}k)\ge\operatorname{Tr}(k^2).
\]

For selfadjoint \(b_j,k\),

\[
 \operatorname{Tr}(b_jk b_jk)
 \le\operatorname{Tr}(b_j^2k^2);
\]

the difference is \(\tfrac12\operatorname{Tr}([b_j,k]^*[b_j,k])\ge0\).
Therefore

\[
 \begin{aligned}
 D^2J(q)[h,h]
 &=\operatorname{Tr}(p^{-1}k p^{-1}k)
   -\sum_j\operatorname{Tr}(b_jk b_jk)\\
 &\ge(1-\kappa)\operatorname{Tr}(k^2)>0
 \quad(h\ne0).                                             \tag{11}
 \end{aligned}
\]

Thus \(J\) is strictly convex on the convex set \(0<q\le R\).
The fixed point \(q_*\) has zero first derivative by (3), including if it lies on the upper boundary.
Integration along each line segment in the feasible set proves that it is the unique global minimizer.

The selfadjoint specialization of Yin_C_F0119, together with the gap (6), gives

\[
 \log\Delta_{\varphi_m}(S)
 =\frac1m\left[-\log\det q_*+
                  \frac12\operatorname{Tr}(\eta(q_*)q_*)\right]. \tag{12}
\]

Indeed the reduced \(m\times m\) Cauchy transform tends to \(-q_*\) at zero from the upper half-plane.
Multiplying (3) by \(q_*\) and taking its trace gives \(\operatorname{Tr}(a_0q_*)=m+\operatorname{Tr}(\eta(q_*)q_*)\), so (12) is exactly \(J(q_*)/m\).
This proves (2); exponentiation and \(\det e^X=e^{\operatorname{Tr}X}\) prove (4).

## A Simple Coefficient-Norm Criterion

Let \(c=\|\eta(I)\|\).
If \(c>0\) and

\[
 a_0\ge\alpha I,
 \qquad \alpha>2\sqrt c,
\]

put

\[
 r=\frac{\alpha-\sqrt{\alpha^2-4c}}{2c},\qquad R=rI.
\]

Then \(r^{-1}+cr=\alpha\), \(r^2c<1\), and \(R^{-1}+\eta(R)\le\alpha I\le a_0\).
Thus (1) holds and (2) becomes an explicit minimum over \(0<q\le rI\).
If \(c=0\), all \(a_j=0\), and for positive definite \(a_0\) the deterministic case follows by taking \(R=a_0^{-1}\).

In the scalar case \(m=1\), write \(\eta(q)=cq\), with \(c>0\), and assume \(a_0=a>2\sqrt c\).
The minimizing value is

\[
 q_*=\frac{a-\sqrt{a^2-4c}}{2c},
 \qquad
 \log\Delta(a+\sqrt c\,s)
 =-\log q_*+\frac c2q_*^2.                                  \tag{13}
\]

The other positive root lies outside the convexity region \(q<c^{-1/2}\).
This explicitly checks the physical-branch selection.
Replacing all coefficients by their negatives leaves \(\eta\) and the determinant unchanged, so the same result applies when \(-S\) admits the positive certificate.
It also applies blockwise when all coefficients share an orthogonal block decomposition and every block has one of these two signs; the logarithmic determinants are then combined using block dimensions as weights.

## Why the Domain Restriction Matters

The unrestricted objective \(J(q)\) is generally unbounded below.
Already for \(m=1\), \(c>0\),

\[
 J(q)=-\log q+aq-\tfrac c2q^2-1\longrightarrow-\infty
 \quad(q\to\infty).
\]

Thus omitting \(q\le R\) would make (2) false.
The certificate supplies both a domain on which the action is convex and a proof that its unique stationary point is the physical inverse expectation.

For general \(G=u-iv\), \(u=u^*\), \(v>0\), the real Dyson action at \(z=i\varepsilon\) is

\[
 -\log|\det(u-iv)|+\varepsilon\operatorname{Tr}v
 -\operatorname{Tr}(a_0u)
 -\tfrac12\operatorname{Tr}(\eta(u)u)
 +\tfrac12\operatorname{Tr}(\eta(v)v)-m.                      \tag{14}
\]

It is stationary at the resolvent solution, but (14) alone does not establish a global minimum or an ordered minimax over all selfadjoint \(u\) and positive \(v\).
In particular, complete positivity of \(\eta\) does **not** imply \(\operatorname{Tr}(\eta(h)h)\ge0\) for every selfadjoint \(h\).
For example, conjugation by \(\operatorname{diag}(1,-1)\) sends the off-diagonal Pauli matrix to its negative.
Matrix variational arguments that silently use Hilbert-Schmidt positivity therefore require a stronger hypothesis than the present setting.

## Continuation Routes and Exact Boundaries

This section preserves the intermediate checkpoint after the initial norm-certificate proof.
The later refinements below resolve the arbitrary strictly positive/negative gap restriction and remove stability from the final variational domain.
At this intermediate checkpoint, the result supplied a genuine finite-dimensional minimum in a certified positive or negative spectral-gap regime, but did not yet cover indefinite selfadjoint pencils, zero-energy spectral bulk, centered pencils, or an arbitrary spectral gap without a certificate satisfying (1).
Failure of that particular certificate was not an obstruction to another variational formula.

Useful next steps within the user's objective are:

1. Replace the norm bound in (1) by a weaker stability condition on the completely positive linearization of the Dyson map, while keeping a directly checkable feasible set and a proof of global optimization.
2. Compare the scalar global ordered minimax with (2), and identify matrix hypotheses under which its inner optimization remains concave and the reduced outer objective convex.
   Preserve the distinction between positivity as a map and positivity as a Hilbert-Schmidt quadratic form.
3. For a real spectral parameter \(x\) outside a certified spectral interval, apply (2) to \(xI-S\) or \(S-xI\).
   This gives a true variational logarithmic potential on the exterior and can be differentiated there.
   Crossing an edge requires a different argument because the positive-matrix resolvent variable need not remain in the certified domain.

No network query, source download, or external novelty comparison was performed for this record.

## Spectral-Radius Refinement and an Intrinsic Feasible Set

Added 2026-09-12 after the initial norm-certificate proof, following a mathematical suggestion by the coordinating agent.
This is a substantive extension of the result above; it supersedes the earlier boundary that an arbitrary strictly positive pencil might not admit a certificate.
It does not extend the conclusion to indefinite pencils or to positive operators whose spectrum contains zero.

For each positive definite matrix \(R\), define a linear map on \(M_m(\mathbb C)\) by

\[
 \Phi_R(X)=\sum_j c_jXc_j,
 \qquad c_j=R^{1/2}a_jR^{1/2}=c_j^*.
\]

Write \(r(\Phi_R)\) for the ordinary spectral radius of this finite-dimensional linear map.
Define the following feasible set directly from the coefficient matrices:

\[
 \mathcal C(a_0,\eta)
 =\left\{R>0:
     a_0\ge R^{-1}+\eta(R),\quad r(\Phi_R)<1\right\}.          \tag{15}
\]

Then

\[
 \boxed{
 S\text{ is strictly positive}
 \quad\Longleftrightarrow\quad
 \mathcal C(a_0,\eta)\ne\varnothing.}                         \tag{16}
\]

Here strictly positive means \(S\ge\gamma I\) for some \(\gamma>0\).
Whenever these conditions hold,

\[
 \boxed{
 \log\Delta_{\varphi_m}(S)
 =\frac1m\min_{R\in\mathcal C(a_0,\eta)}
 \left\{-\log\det R+\operatorname{Tr}(a_0R)
            -\frac12\operatorname{Tr}(\eta(R)R)-m\right\}.}   \tag{17}
\]

The minimizer is unique and is \(q=(\operatorname{id}\otimes\tau)(S^{-1})\).
In particular, the trial variable in (17) is constrained by a matrix inequality and a finite-dimensional spectral-radius inequality, not by equality in the Dyson equation.
The expression inside braces is evaluated directly on every trial matrix.
The determinant-only rewriting in (4) applies to (17) after replacing its domain by \(\mathcal C(a_0,\eta)\).

### Sufficiency and the Improved Interval Minimum

Suppose \(R\in\mathcal C(a_0,\eta)\).
In the notation of the Fock proof above, let \(T=\sum_j c_j\otimes\ell_j\).
Orthogonality of creation words and reversal of the finite word index give

\[
 (T^k)^*T^k=\Phi_R^k(I)\otimes1,
 \qquad \|T^k\|^2=\|\Phi_R^k(I)\|.                         \tag{18}
\]

Since \(\Phi_R^k\) is completely positive, \(\|\Phi_R^k\|=\|\Phi_R^k(I)\|\) for the norm induced by the matrix operator norm.
The spectral-radius formula therefore implies

\[
 r(T)^2=r(\Phi_R)<1.
\]

Consequently \(I+T\) is boundedly invertible.
Square completion still gives

\[
 (R^{1/2}\otimes1)S(R^{1/2}\otimes1)
 \ge(I+T)^*(I+T)
 \ge\|(I+T)^{-1}\|^{-2}I>0.                                 \tag{19}
\]

Thus \(S\) is strictly positive even when \(\|\Phi_R(I)\|\ge1\).
The monotone inverse iteration and finite-depth compression argument used for (7)-(8) remain valid, so its physical inverse expectation satisfies \(0<q\le R\) and the Dyson equation (3).

The strict-convexity proof also improves.
The map \(\Phi_R\) is selfadjoint for the Hilbert-Schmidt inner product, since each \(c_j=c_j^*\).
For every selfadjoint \(k\), the finite-dimensional spectral theorem gives

\[
 \operatorname{Tr}(k\Phi_R(k))
 \le r(\Phi_R)\operatorname{Tr}(k^2).
\]

Therefore the same change of variables as in (11) yields

\[
 D^2J(q_0)[h,h]
 \ge(1-r(\Phi_R))\operatorname{Tr}(k^2)>0
 \quad(0<q_0\le R,\ h=R^{1/2}kR^{1/2}\ne0).                \tag{20}
\]

The interval minimum (2) thus remains true with (1) replaced by the conditions in (15).
This proves sufficiency in (16) and a unique global minimum on every interval defined by a feasible certificate.

### Every Strictly Positive Pencil Has a Stable Certificate

Conversely, suppose \(S\ge\gamma I\), \(\gamma>0\), and set

\[
 q(t)=(\operatorname{id}\otimes\tau)((S-tI)^{-1}),
 \qquad |t|<\gamma.
\]

These matrices are positive definite for real \(t<\gamma\), and the reduced Dyson equation, continued from the upper half-plane to the real gap, gives

\[
 q(t)^{-1}=a_0-tI-\eta(q(t)).                               \tag{21}
\]

Let \(q=q(0)>0\) and \(q'=q'(0)=(\operatorname{id}\otimes\tau)(S^{-2})>0\).
Differentiating (21) yields

\[
 q'=q^2+q\eta(q')q.
\]

For the positive definite matrix \(H=q^{-1/2}q'q^{-1/2}\), this is

\[
 H-\Phi_q(H)=q>0.                                         \tag{22}
\]

Define

\[
 \Psi(X)=H^{-1/2}\Phi_q(H^{1/2}XH^{1/2})H^{-1/2}.
\]

This completely positive map is similar to \(\Phi_q\) as a linear transformation.
Equation (22) gives

\[
 0\le\Psi(I)=I-H^{-1/2}qH^{-1/2}<I,
 \qquad \|\Psi\|=\|\Psi(I)\|<1.
\]

Hence \(r(\Phi_q)=r(\Psi)<1\).
Equation (21) at zero gives equality in the matrix inequality in (15), so \(q\in\mathcal C(a_0,\eta)\).
This proves necessity in (16).

For every \(R\in\mathcal C(a_0,\eta)\), the improved interval result already proves \(q\le R\) and \(J(R)\ge J(q)\).
Equality forces \(R=q\) by strict convexity on that interval.
Since \(q\) itself is feasible, these comparisons prove (17), including attainment and uniqueness.
This argument does not assume that the entire feasible set in (15) is convex.

### A Separate Linear Matrix Inequality for Positivity

There is a simpler feasibility test for strict positivity, useful for finding a preliminary coefficient certificate:

\[
 \boxed{
 S>0
 \quad\Longleftrightarrow\quad
 \exists R>0:\ a_0-R^{-1}-\eta(R)>0
 \quad\Longleftrightarrow\quad
 \exists R=R^*:
 \begin{pmatrix}a_0-\eta(R)&I\\I&R\end{pmatrix}>0.}          \tag{23}
\]

The last matrix depends affinely on \(R\); equivalence of the last two conditions is its Schur-complement identity.
For sufficiency, write \(a_0-R^{-1}-\eta(R)\ge\delta I\), \(\delta>0\).
The same Fock square completion shows

\[
 S=\bigl(R^{-1}+\eta(R)\bigr)\otimes1+
       \sum_j a_j\otimes s_j+
       \bigl(a_0-R^{-1}-\eta(R)\bigr)\otimes1
 \ge\delta I,
\]

without any spectral-radius assumption.
Conversely, if \(S\ge\gamma I\), choose \(0<t<\gamma\) and take \(R=q(t)\) from (21).
The residual is then exactly \(tI>0\).

An arbitrary certificate from (23) need not satisfy the spectral-radius condition in (15).
For example, in the scalar case \(a_0=3\), \(\eta(R)=R\), the value \(R=2\) has positive residual \(1/2\) but \(r(\Phi_R)=4\).
Thus (23) by itself did not justify dropping stability from the intermediate minimum (17).
The later [matrix-supersolution proof](#minimum-over-all-matrix-supersolutions) supplies a different global-minimality argument that does remove this condition; it does not assert stability of every supersolution.

### Intermediate Scope and Continuation after the Spectral-Radius Refinement

The real-gap variational result now covers **every strictly positive selfadjoint affine semicircular pencil**, and by an overall sign change every strictly negative one.
The finite-matrix feasible set can be characterized without an already supplied Dyson solution; its unique minimizer recovers that solution.
The constant term need not dominate the noise by a scalar coefficient-norm bound.

Indefinite selfadjoint pencils, spectral bulk, and zero-energy boundary cases remain outside this result.
At this intermediate checkpoint, the next proposal was to combine the affine positivity test (23), the stable minimum (17), and the positive imaginary-drift minimum into a globally valid saddle description.
The subsequent section first removes stability from the real-gap variational domain; it does not yet prove the proposed globally valid saddle description.

## Minimum over All Matrix Supersolutions

Added later on 2026-09-12 following a further suggestion from the coordinating agent.
This refinement removes the spectral-radius test from the variational feasible set.
The spectral-radius argument above remains a proof of strict local convexity at the physical inverse expectation.

For \(R>0\), write

\[
 F(R)=a_0-R^{-1}-\eta(R),\qquad
 L(R)=\begin{pmatrix}a_0-\eta(R)&I\\I&R\end{pmatrix},
\]

and define

\[
 \mathcal B=\{R>0:L(R)\ge0\}
           =\{R>0:F(R)\ge0\},
 \qquad
 \mathcal B_{\mathrm{str}}=\{R>0:L(R)>0\}.
\]

Both sets are determined by affine matrix inequalities, together with positive definiteness of \(R\), and are convex.
By (23), \(\mathcal B_{\mathrm{str}}\ne\varnothing\) is equivalent to strict positivity of \(S\).
Under that hypothesis,

\[
 \boxed{
 \log\Delta_{\varphi_m}(S)
   =\frac1m\min_{R\in\mathcal B}J(R)
   =\frac1m\inf_{R\in\mathcal B_{\mathrm{str}}}J(R),
 \quad
 J(R)=-\log\det R+\operatorname{Tr}(a_0R)
                -\tfrac12\operatorname{Tr}(\eta(R)R)-m.}      \tag{24}
\]

The minimum over \(\mathcal B\) is attained uniquely at \(q=(\operatorname{id}\otimes\tau)(S^{-1})\); this matrix is on the equality boundary \(F(q)=0\).
In particular, the strict-domain infimum is not attained.
No spectral-radius constraint, Dyson equality, or externally fixed certificate is imposed on the trial matrices in (24).

### Proof of Global Minimality

Every \(R\in\mathcal B\) is a supersolution for the monotone iteration (7): all iterates are positive and at most \(R\).
Strict positivity of the given \(S\) supplies the uniform inverse bound needed for the finite Fock compression argument, independently of any norm or spectral-radius bound on this particular \(R\).
Therefore the limit of the iteration is the physical \(q\), and

\[
 q\le R\quad\text{for every }R\in\mathcal B.                 \tag{25}
\]

Set \(H=R-q\ge0\) and \(Q_t=q+tH\), \(0\le t\le1\).
The function \(F\) is operator concave on the positive cone.
Indeed, along any affine positive segment its second derivative is

\[
 \frac{d^2}{dt^2}F(Q_t)
 =-2Q_t^{-1}H Q_t^{-1}H Q_t^{-1}\le0,
\]

because the negative of half this expression is a positive congruence of \((Q_t^{-1/2}HQ_t^{-1/2})^2\).
Thus

\[
 F(Q_t)\ge(1-t)F(q)+tF(R)\ge0.
\]

Using the first-variation identity (9),

\[
 \frac{d}{dt}J(Q_t)=\operatorname{Tr}(F(Q_t)H)\ge0.           \tag{26}
\]

The trace is nonnegative because both factors are positive semidefinite.
Hence \(J(R)\ge J(q)\), proving the minimum in (24).

For uniqueness, the preceding necessity argument proves \(r(\Phi_q)<1\).
Formula (20), evaluated at \(q\), therefore makes the Hessian of \(J\) strictly positive in every nonzero selfadjoint direction.
Since \(DJ(q)=0\), if \(H\ne0\) then \(J(q+tH)>J(q)\) for all sufficiently small positive \(t\).
Equation (26) then gives \(J(R)>J(q)\).
Thus equality requires \(R=q\).

Finally take \(R_t=(\operatorname{id}\otimes\tau)((S-tI)^{-1})\) for \(0<t<\gamma\), where \(S\ge\gamma I\).
Equation (21) gives \(F(R_t)=tI>0\), so \(R_t\in\mathcal B_{\mathrm{str}}\), and \(R_t\to q\) as \(t\downarrow0\).
Continuity of \(J\) proves the strict-domain infimum in (24).
Since \(q\) is the unique minimizer on the larger set and does not belong to the strict set, that infimum is not attained.

### Positive Determinant-Only Trial Matrices

For every \(R>0\), set

\[
 P(R)=R^{-1/2}
 \exp\!\left(
   R^{1/2}\bigl(a_0-\tfrac12\eta(R)\bigr)R^{1/2}-I_m
 \right)R^{-1/2}>0.
\]

Its ordinary log determinant is \(J(R)\).
Consequently (24) is equivalently

\[
 \boxed{
 \Delta_{\varphi_m}(S)
   =\min_{\substack{R>0\\L(R)\ge0}}
         \Delta_{\operatorname{tr}_m}(P(R))
   =\inf_{\substack{R>0\\L(R)>0}}
         \Delta_{\operatorname{tr}_m}(P(R)).}                  \tag{27}
\]

The feasible set here is convex, but global Euclidean convexity of \(J\) on that set is not claimed or needed.
Global minimality follows from the least supersolution (25), the positive gradient along its feasible order segments, and local strictness only at the minimizer.

The strict-positivity hypothesis must be retained: nonstrict feasibility alone may include a spectral-edge pencil such as \(2+s\), and the preceding proof does not automatically cover every such boundary.
The final proved result is the matrix-inequality minimum for every strictly positive selfadjoint affine pencil, and, after an overall sign change, every strictly negative one.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:09 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#proof-of-global-minimality) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0181_v1.md#checks-of-the-strengthened-proof) | Strengthened proof, equations (15)–(27), in the context of the earlier proof: spectral-radius square completion, stable physical inverse for every strictly positive pencil, affine matrix feasibility, least-supersolution comparison, global minimum and strict-domain nonattainment, uniqueness and positive determinant packaging. Indefinite and zero-gap positive pencils remain excluded. |


### Decision m04-isolated-review

| Field | Value |
| --- | --- |
| date | 2026-10-23T00:23 |
| status | proved |
| reason | Adopt the separately performed isolated review of both the initial certified proof and the full strengthened supersolution theorem, preserving unchanged mathematics, historical findings and strict-positivity limitations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#proof-of-global-minimality) | Final all-matrix-supersolution minimum with its complete earlier certificate, physical-branch, spectral-radius, strict-feasibility and local-strictness proof context. |
| review | [Initial isolated finding](../audits/reviews/Yin_R_F0181_v1.md#f0079-initial-certified-formula) | Initial equations (1)-(14): positive spectral gap, physical inverse/compression, strict interval minimum, determinant normalization, empty noise, signs, scalar criterion and domain warnings. |
| review | [Strengthened isolated finding](../audits/reviews/Yin_R_F0181_v1.md#f0079-full-strengthened-supersolution-theorem) | Full equations (15)-(27): every strictly positive/negative pencil, stable physical certificate, affine feasibility, least supersolution, global minimum and uniqueness, strict-domain nonattainment and positive determinant packaging; indefinite and zero-gap positive pencils excluded. |

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

The recorded review description was `independently reviewed`.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

Original review classification and limitations: independently reviewed; root supplied refinement mechanisms

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

The recorded review description was `independently reviewed`.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#proof-of-global-minimality) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0181_v1.md#checks-of-the-full-argument) | The certified selfadjoint variational formula at equations (1)-(4): the matrix certificate and strict positive spectral gap, identification of the physical inverse expectation, and unique minimisation over the directly specified feasible set \(0<q\le R\). |

Original review classification and limitations: independently reviewed; root supplied refinement mechanisms

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

<a id="decision-candidate-0004"></a>

### Historical assessment candidate-0004

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T02:52 |
| status | proved |

The recorded review description was `independently reviewed`.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#proof-of-global-minimality) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0181_v1.md#checks-of-the-strengthened-proof) | The later strengthened proof from the spectral-radius refinement through the minimum over all matrix supersolutions (equations (15)-(27)): stability for every strictly positive pencil, the strict affine matrix inequality, the all-supersolution comparison, global minimality and determinant packaging, with indefinite pencils and positive spectral-edge operators excluded. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

The certified formula review covers equations (1)-(4); the subsequent independent review covers the spectral-radius refinement through the minimum over all matrix supersolutions, equations (15)-(27), with indefinite pencils and positive spectral-edge operators excluded.

Review: [Exact material](../audits/reviews/Yin_R_F0181_v1.md#original-f0039-review-account).

Material covered by that review: [Exact material](Yin_C_F0121_v1.md).

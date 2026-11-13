---
author: Yin
---
# Independent review of the weighted ergodic shift classification and factor example

At 2026-11-13T14:49 UTC an agent outside the development of [C_F0219 v1](../../claims/Yin_C_F0219_v1.md#decision-candidate) reviewed its fixed statement, entire argument and direct dependency interfaces for Yin.
The reviewer received the fixed input and a list of obligations without exploration notes, development dialogue, author explanations or a prior verdict on this Claim.

## Whole-proof finding

The classification holds for every stated bounded positive weight with integrable logarithm, including weights that approach zero and weights whose one-time law has atoms.
The factor example has a bounded generator-first dual on the full trace Hilbert space and fails even the normalized Hilbert-valued derivation hypothesis.

The linear identification of the coarse target with a subspace of \(L^2(P\bar\otimes P^{\mathrm{op}})\) preserves the inner product by traciality on the second leg.
Right outer multiplication becomes left multiplication by the opposite element, so \(S_{ab}=\lambda_a S_b+\rho_b S_a\).
For diffuse \(h\), independent base variables give zero spectral kernel for each of the three differences used in differentiating \(BC=CB,\ XB=CX,\ X^*C=BX^*\).
Thus subtracting \(S_aK\) from the given derivation annihilates both generators in the finite affiliated algebra.
From \(SK=1\), the range projection of \(S\) equals one, and the equality of the traces of the two polar supports makes its initial projection one as well.
Its two-sided affiliated inverse is \(K\), giving \(bS=S^*\) from \(b=S^*K\).
Only \(b=\delta(X^*)\) needs to belong to \(L^2\), and multiplication of \(b\) on the right by bounded \(S\) preserves that space.

The itinerary law on the sequence space is ergodic.
A point atom forces its full finite shift orbit to have total mass one.
For period \(p\), the product of \(p\) consecutive positive weights is invariant and equals a positive constant \(a\).
The identity \(X^p=au^p\) places the monomial in the center of the generated algebra since \(u^p\) commutes with \(h,u\) and their adjoints.
The invertible central value avoids zero, the sole critical value for \(p>1\), and the linear case has no critical values.
These are the hypotheses of the weaker Hilbert-derivation assertion of C_F0204 v1.
Normality gives \(h^2=\alpha(h^2)\), hence constancy by ergodicity.

In the remaining case the joint itinerary is nonatomic, even when individual coordinates have atoms.
Strict positivity makes the consecutive ratios of \(B_k,C_k\) recover all translated coordinates on a common conull set.
Fubini then shows that the support projections of their differences cover one, for the unshifted pair and for either of the two shifted pairs.
In the patching argument \(p_i\) and \(L_j\) commute in the base tensor algebra.
Leibniz gives \(L_i\delta a_j=L_j\delta a_i\), and consequently \(q\delta a_j=L_jy\) by operator-norm convergence for \(q\) and Hilbert-norm convergence for \(y\).
Commuting \(q^{-1}\) with \(L_j\) in the affiliated algebra gives \(L_jq^{-1}y=\delta a_j\), with all projections acting to the left of the derivatives.
For a covariance quotient \(n/v=\alpha(a)\), differentiating \(vXa=nX\) leaves \(\lambda_v(\rho_a-\lambda_{\alpha(a)})dX=0\).
The positive denominator is injective, and the support of each remaining difference annihilates \(dX\) by spectral inversion on that support.
Their join is one, so \(dX=0\).
The formula with \(\alpha^{-1}\) gives the same conclusion for \(d(X^*)\).
This again yields the necessary Hilbert-space equation \(bS=S^*\).

Conjugation by \(V=1\otimes u^{\mathrm{op}}\) translates the second base variable by \(T^{-1}\).
For the coefficient of \(U^lV^{-1-l}\) in \(bS\), the \(U\) term therefore has factor \(h_l(s)\) and the \(V\) term has factor \(-h_{l+2}(t)\).
The two inhomogeneous coefficients of \(S^*\) are \(h_0(s)\) at \(l=-1\) and \(-h_1(t)\) at \(l=0\).
The tracial Fourier decomposition and Tonelli imply square summability of this entire diagonal at almost every pair.

For the diagonal product transformation, both marginals of the restriction to an invariant set have invariant densities and hence are constant, even when the product transformation is nonergodic.
Their equal masses give zero integral of the log-ratio cocycle on each invariant set.
On the invariant set of escape to minus infinity the partial-sum supremum \(G\) is finite, and \(G\ge F_0+G\circ Q\).
The positive and negative parts of the difference of the two level-\(m\) truncations increase separately to those of \(G-G\circ Q\).
Their integrals agree, and the limiting negative part is bounded by \(F_0^-\).
Consequently this integrable difference has mean zero and equals \(F_0\) almost everywhere on the restricted set.
Telescoping would give \(G\circ Q^n\to+\infty\) there, impossible for variables with the same finite-valued law.
The forward tail uses \(F\) at \(\Theta(s,t)\), and the backward tail uses \(-F\) at \(\Theta^{-2}(s,t)\) iterated by \(\Theta^{-1}\).
Square summability therefore forces \(f_0=f_{-2}=0\), and the two remaining inhomogeneous equations force equality of independent copies of \(h^2\) almost surely.
This proves constancy.

For \(X=au\) the crossed-product trace makes \(u\) Haar regardless of periodicity of the base action.
On the Laurent polynomial core the divided difference of \(u^k\) has product Haar integral \(a^{-1}\mathbf1_{k=1}\), including negative exponents by simultaneous rotation.
With the inner product linear in the second entry this is \(\langle u/a,u^k\rangle\), so the vacuum is in the actual Hilbert adjoint domain.

For the irrational rotation example the bounded coboundary gives exactly \(X=gug^{-1}\).
The logarithm of the weight is a nonzero first harmonic with finite level sets, and its translate is linearly independent since \(\sin(2\pi\theta)\ne0\).
The modulus and polar unitary of \(X\) recover \(h,u\), and the two harmonics then recover the full base algebra.
Commutation with the circle character kills every nonzero Fourier mode of a central element, and rotation invariance makes its remaining coefficient scalar.
The diffuse base excludes a finite matrix factor.
On powers \(u^n\) the negative terminal-deletion operator satisfies \([L_u,D_u]u^n=\mathbf1_{n=0}1\), with the positive sign required by the Task.
Extension by zero to the reducing orthogonal complement preserves this identity on all of \(L^2(P)\).
Conjugation by the bounded invertible \(W(a)=gag^{-1}\) fixes \(1\) and preserves its trace functional, so it preserves \(P_\Omega\) and carries the commutator to \([L_X,D]=P_\Omega\).
Boundedness supplies both actual domains and restriction supplies the bare dual.
The similarity identities apply to the Haar unitary directly and use no selfadjointness assumption.

The central-polynomial theorem and the finite affiliated algebra were used at their recorded scopes.
The Haar commutator and similarity were also checked directly above.
No new assessment of the original literature proofs or of the general implication from ACSY to bare duals is made here.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0219_v1.md#statement) | All three equivalent conditions at the stated ergodic, positive log-integrable scope and the type II factor separation. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0219_v1.md#argument) | Both itinerary cases, diffuse-square calculation, Fourier and recurrence arguments, Laurent vacuum, factor generation and full-space bounded dual. |
| [Whole-proof finding](#whole-proof-finding) | [Central polynomial theorem](../../claims/Yin_C_F0204_v1.md#statement) | The weaker Hilbert-derivation theorem on a finite itinerary orbit, including the critical-value hypothesis. |
| [Whole-proof finding](#whole-proof-finding) | [Finite affiliated inverses](../literature/MSY23/Yin_U004.md#msy23-u004) | Finite polar supports, measurable inverses and the two-sided inverse following from a right inverse. |
| [Whole-proof finding](#whole-proof-finding) | [Bounded Haar dual](../literature/MSY23/Yin_U005.md#msy23-u005) | The one-generator deletion operator with the sign for the generator-first commutator. |
| [Whole-proof finding](#whole-proof-finding) | [Trace-preserving similarity](../../claims/Yin_C_F0203_v1.md#transfer-of-the-holomorphic-moment-functional) | The bounded conjugation identity on the trace Hilbert space and preservation of the vacuum projection. |

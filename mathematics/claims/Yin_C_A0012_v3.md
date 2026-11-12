---
author: Yin
---
# Symmetric singular fibers with fixed global contour data

Date: 2026-11-12 (Asia/Hong_Kong).
This investigation continues [A0001](../tasks/Yin_T_A0001_v1.md#contract) and [route six](../strategies/Yin_S_A0006.md#compatible-central-variable-specialization).
The question is whether exact generic rank and the total exceptional-defect estimate in [C_A0012 v2](../claims/Yin_C_A0012_v2.md#statement), together with independently computable finite-order symmetry or global contour data, control each singular fiber's rank loss.

## Statement

For every rectangular complex group-ring input over every torsion-free group, the finite triangular group-ring pencil (3) has generic rank, exceptional parameter orbit, degree, prescribed regular endpoint values and explicitly computed contour trace independent of that coefficient matrix, while every exceptional fiber retains its kernel dimension as in (5).
Its finite selfadjoint transport realization satisfies the compatible-specialization certificate before specialization.
Thus those stronger data still do not identify geometric rank-loss mass with a global contour count.
The last section gives the exact additional premise needed for a symmetry-based inference and identifies its first unresolved original-input application.

## Inputs and conventions

The original input is a torsion-free discrete group \(H\) and an arbitrary finite matrix \(A\in M_{r,m}(\mathbb CH)\), where \(r,m\ge1\).
All group von Neumann algebras carry their canonical traces and every matrix trace is unnormalized.
Write \(\kappa_A:=\dim_H\ker A\), so \(\operatorname{rk}_H A=m-\kappa_A\).
The domain-aware closed affiliated rank identities and the generic-rank and summable-loss statements are reused only at their exact scopes in [C_A0012 v2](../claims/Yin_C_A0012_v2.md#inputs-and-conventions).
The [normal finite encoding](../claims/Yin_C_A0011_v1.md#all-matrix-equivalence-and-exact-comparison-with-previous-work) supplies the comparison with an obstruction already retaining arbitrary coefficient kernels.
No counterexample to A0001 follows from this construction.

<a id="argument"></a>
## A degree-minimal symmetric finite pencil

Put \(d=r+m\) and define the finite square-zero matrix
\[
N_A:=\begin{pmatrix}0_{r,r}&A\\0_{m,r}&0_{m,m}\end{pmatrix}
\in M_d(\mathbb CH).
\tag{1}
\]
Then \(N_A^2=0\), \(\tau_d(N_A)=0\), and the bounded kernel equation gives
\[
P_{\ker N_A}=\operatorname{diag}(I_r,k_A),
\qquad
k_A:=P_{\ker A},
\qquad
\dim_H\ker N_A=r+\kappa_A.
\tag{2}
\]
This uses no inverse or rational-closure assertion for \(k_A\).

For any integer \(q\ge1\), set
\[
P_A(z):=(1+z^q)I_d+(1-z^q)N_A.
\tag{3}
\]
Its coefficients are actual finite group-ring matrices.
Both the constant and leading coefficients \(I_d+N_A\) and \(I_d-N_A\) are bounded units, with inverses \(I_d-N_A\) and \(I_d+N_A\), respectively.
Whenever \(f(z):=1+z^q\ne0\), write \(g(z):=1-z^q\) and compute the bounded inverse
\[
P_A(z)^{-1}=f(z)^{-1}I_d-g(z)f(z)^{-2}N_A.
\tag{4}
\]
At every root \(\zeta^q=-1\), the pencil is \(2N_A\), so
\[
\operatorname{rk}_H P_A(z)=d\quad(z^q\ne-1),
\qquad
\delta_{P_A}(\zeta)=d-\operatorname{rk}_H P_A(\zeta)=r+\kappa_A.
\tag{5}
\]
In particular all \(q\) exceptional fibers are genuine, because \(r\ge1\).
Every regular endpoint satisfying \(z^q=1\) has the prescribed value \(P_A(z)=2I_d\), independently of \(A\).

Let \(\omega=e^{2\pi i/q}\), with the trivial interpretation for \(q=1\).
The pencil obeys \(P_A(\omega z)=P_A(z)\), and the exceptional set is one orbit of size \(q\) under this rotation.
This is an actual finite-order \(*\)-automorphism of \(\mathbb C[H\times\langle x\rangle]\), defined by fixing \(H\) and sending \(x\) to \(\omega x\).
It is induced by a unitary character, rather than asserted to be a group automorphism sending a generator to another group element.
When the height action fixes \(x\), the same automorphism extends by fixing the height generator and permutes finite coefficient specializations by \(\epsilon_z\circ\alpha=\epsilon_{\omega z}\).

The degree \(q\) is minimal among nonconstant ordinary polynomial matrices invariant under this rotation.
Indeed coefficient comparison in \(R(\omega z)=R(z)\) forces every nonzero exponent to be divisible by \(q\), so any nonconstant such polynomial has degree at least \(q\).
The leading coefficient of (3) is a unit, so (3) has degree exactly \(q\).
For \(q=1\), this is already a degree-one pencil with prescribed value \(2I_d\) at \(z=1\), a single exceptional fiber at \(-1\), and two invertible endpoint coefficients.
This minimality concerns the specified polynomial parameter and symmetry, not every possible stabilization or rational reparametrization.

The selfadjoint positive finite Laurent matrix
\[
Q_A(z):=P_A(z)^*P_A(z)\qquad(|z|=1)
\tag{6}
\]
has the same kernel, generic rank and exceptional defects.
It satisfies \(Q_A(z)=4I_d\) at every regular endpoint \(z^q=1\), and \(Q_A(\zeta)=4N_A^*N_A\) at every singular root.
Its exponents lie in \([-q,q]\), and its coefficient of \(z^q\) is \((I_d+N_A)^*(I_d-N_A)\), an actual bounded unit and hence nonzero.
A nonconstant selfadjoint Laurent matrix with the same rotation invariance must have at least one positive exponent divisible by \(q\) and its negative partner.
Thus the Laurent width \(2q\) of (6) is also minimal in that selfadjoint invariant class.

## Fixed contour data do not give geometric defect mass

For \(R>0\) with \(R\ne1\), define the explicit scalar contour quantity
\[
W_A(R):=\frac1{2\pi i}\int_{|z|=R}
\tau_d\bigl(P_A(z)^{-1}P_A'(z)\bigr)\,dz,
\tag{7}
\]
where the circle is positively oriented.
Every inverse in this integral is bounded by (4), uniformly on the fixed compact circle.
No general determinant construction, Brown-measure theorem or integer-valued index theorem is required to define or calculate (7).
Multiplying the finite formulas and using \(N_A^2=0\) gives
\[
P_A(z)^{-1}P_A'(z)
=\frac{f'(z)}{f(z)}I_d
+\left(\frac{g'(z)}{f(z)}-\frac{g(z)f'(z)}{f(z)^2}\right)N_A.
\]
The off-diagonal trace vanishes, so
\[
\tau_d\bigl(P_A(z)^{-1}P_A'(z)\bigr)
=d\frac{qz^{q-1}}{1+z^q},
\qquad
W_A(R)=\begin{cases}0,&0<R<1,\\qd,&R>1.\end{cases}
\tag{8}
\]
For example, expanding \((1+z^q)^{-1}\) in its convergent geometric series on the respective circle evaluates the integral and proves (8) directly.
The corresponding integral on any sufficiently small positive circle enclosing exactly one root \(\zeta^q=-1\) equals \(d\), because that root is simple and the scalar logarithmic derivative in (8) has residue \(d\).
Thus even each local contour count is the same known integer independently of \(A\).

There is also an explicit endpoint-preserving norm homotopy on every nonsingular parameter set:
\[
P_{A,s}(z):=f(z)I_d+s g(z)N_A,
\qquad 0\le s\le1.
\tag{9}
\]
Formula (4), with \(N_A\) replaced by \(sN_A\), proves invertibility for all \(z^q\ne-1\) throughout the homotopy.
Every prescribed value at \(z^q=1\) stays \(2I_d\), and every nonsingular loop is homotopic through bounded units to the same scalar loop \(f(z)I_d\).
Consequently any invariant of those loops that is preserved by such a homotopy is also independent of \(A\); no classification of those invariants is invoked.

In contrast, the exact total geometric loss is
\[
\Delta_A:=\sum_{z\in\mathbb T}\delta_{P_A}(z)
=q(r+\kappa_A),
\qquad
W_A(R_{\mathrm{out}})-W_A(R_{\mathrm{in}})-\Delta_A
=q\operatorname{rk}_H A
\tag{10}
\]
for \(0<R_{\mathrm{in}}<1<R_{\mathrm{out}}\).
The summable-loss estimate of C_A0012 v2 is \(\Delta_A\le qd\), exactly consistent with (10).
Repeating the singular orbit increases both the exact total loss and this bound by the same factor \(q\), so division by the orbit size yields only \(r+\kappa_A\le d\).
It is an equality only when \(A=0\), since zero affiliated rank of the bounded finite matrix \(A\) is equivalent to \(A=0\) by faithfulness of the trace.
Thus minimal degree and invertible outer coefficients do not force saturation of that estimate.

At a singular point the square-zero part has full generalized kernel, because \(N_A^2=0\), while its ordinary kernel has trace \(r+\kappa_A\).
The discrepancy in (10) is precisely the rank of the nonzero nilpotent part, repeated at the \(q\) roots.
This mechanism is consistent with the existing [point-spectrum versus Brown-atom source distinction](../audits/literature/ACSY24/Yin_U004.md#point-spectrum-and-brown-atoms), which uses nilpotent matrices to distinguish the two weights.
That source observation is contextual attribution only; all contour and kernel identities used here have been proved directly.

Already for \(H=\{1\}\), \(r=m=1\), the inputs \(A=0\) and \(A=1\) have identical values of \(q,d\), regular endpoint matrices, generic rank, exceptional orbit and contour data, but singular defects \(2\) and \(1\), respectively.
This is a concrete counterexample to identifying those data with a unique geometric defect, or to setting the defect equal to the local contour count.
It is not a counterexample to the integer-defect assertion.
For arbitrary torsion-free \(H\), integer defect for all the pencils (3) is equivalent to the full A0001 statement by (5), after subtracting the known integer \(r\).

## The actual compatible finite selfadjoint transport input

Set \(N:=H\times\langle x\rangle\), let \(\sigma\) be the identity, and put \(G=N\times\langle t\rangle\).
These are actual torsion-free groups, with independent infinite cyclic generators \(x,t\).
Use (3) with \(z=x\), and define
\[
M_A(x):=\bigl(P_A(x)\ \ 0_{d,d}\bigr),
\quad
B_A:=M_A^*M_A,
\quad
\mathcal H_A:=\begin{pmatrix}(t+t^{-1})I_{2d}&B_A\\B_A&0\end{pmatrix}
\in M_{4d}(\mathbb CG).
\tag{11}
\]
Every displayed entry is finite, and \(M_A(1)M_A(1)^*=4I_d\) independently of \(A\).
The identity action is an allowed element of \(GL_1(\mathbb Z)\) in [C_A0012 v1](../claims/Yin_C_A0012_v1.md#statement).
Formula (4) shows that the integrated complete kernel projection is
\[
p=P_{\ker M_A}=\operatorname{diag}(0_d,I_d).
\]
The certificate therefore applies with row count \(d\), column count \(2d\), zero potential and \(\sigma(p)=p\), giving
\[
P_{\ker\mathcal H_A}=\operatorname{diag}(0_{2d},p),
\qquad
\dim_G\ker\mathcal H_A=d.
\tag{12}
\]
This conclusion also follows directly from the same bounded equations used below.

For every root \(\zeta^q=-1\), the finite coefficient evaluation \(x\mapsto\zeta\), fixing \(H,t\), is an actual \(*\)-homomorphism to \(\mathbb C[H\times\langle t\rangle]\).
It is compatible with the identity height action and preserves the involution since \(|\zeta|=1\).
At this fiber the separately computed coefficient projection is
\[
p_\zeta=P_{\ker M_A(\zeta)}
=\operatorname{diag}(I_r,k_A,I_d),
\qquad
\tau_{2d}(p_\zeta)=d+r+\kappa_A.
\tag{13}
\]
The lower bounded equation for \(\mathcal H_A(\zeta)(\xi,\eta)=0\) gives \(\xi=p_\zeta\xi\).
The projection commutes with \(s=t+t^{-1}\), whose Fourier multiplier \(2\cos\theta\) vanishes only on a Haar-null set, so compressing the upper equation gives \(s\xi=0\) and then \(\xi=0\).
The remaining upper equation gives \(\eta=p_\zeta\eta\), and the converse follows by substitution.
Hence
\[
P_{\ker\mathcal H_A(\zeta)}=\operatorname{diag}(0_{2d},p_\zeta),
\qquad
\dim_{H\times\langle t\rangle}\ker\mathcal H_A(\zeta)=d+r+\kappa_A.
\tag{14}
\]
Subgroup trace preservation identifies \(\kappa_A\) in this product group with its original \(H\)-dimension.
No unbounded inverse has been applied to an arbitrary Hilbert vector, and the singular projection has not been obtained by evaluating an integrated rational representative.
The finite-order character symmetry fixes the complete matrix (11) because every occurrence of \(x\) is through \(x^q\).
It permutes the compatible singular specializations transitively and preserves their exact kernel dimensions.

## A genuine order-two group action and a two-point singular orbit

The preceding symmetry can additionally be tested with a group automorphism rather than only a character automorphism.
Set \(q=2\), let \(\sigma\) fix \(H\) and send \(x\) to \(x^{-1}\), and use the torsion-free semidirect product
\[
G_-:=(H\times\langle x\rangle)\rtimes_\sigma\langle t\rangle.
\tag{15}
\]
A finite-order element has zero height in the infinite cyclic quotient and therefore lies in the torsion-free subgroup \(H\times\langle x\rangle\), proving the asserted torsion-freeness.
For \(J=\operatorname{diag}(I_r,-I_m)\) one has \(JN_AJ=-N_A\), and direct multiplication gives
\[
P_A(z)=z^2J P_A(z^{-1})J.
\tag{16}
\]
Thus the actual order-two coefficient action preserves fiber ranks and exchanges the two singular points \(i,-i\).
The fixed points \(z=1,-1\) both have the prescribed value \(2I_d\).
The same matrix (11), now over \(G_-\), still satisfies C_A0012 v1 and has the same complete generic kernel (12).

Neither \(x\mapsto i\) nor \(x\mapsto-i\), with \(t\) scalar, respects the semidirect relation by itself.
The correct finite \(*\)-specialization of the whole orbit is instead
\[
h\longmapsto hI_2,
\qquad
x\longmapsto X:=\operatorname{diag}(i,-i),
\qquad
t\longmapsto uS,
\qquad
S:=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\tag{17}
\]
with independent infinite cyclic \(u\) commuting with \(H\).
Indeed \(SXS=X^{-1}\), every image of a group element is unitary, and (17) respects all defining relations.
This gives an actual finite matrix over \(\mathbb C[H\times\langle u\rangle]\), rather than an asserted extension to all affiliated operators.

Because \(X^2=-I_2\), the image of \(P_A\) is \(2N_A\) in each orbit coordinate.
The coefficient kernel is therefore two copies of (13), while the height sum becomes \((u+u^{-1})S\), an injective operator commuting with that kernel projection.
The same bounded equations prove that the image of \(\mathcal H_A\), of size \(8d\), has unnormalized kernel dimension
\[
2(d+r+\kappa_A).
\tag{18}
\]
If one uses the orbit-average trace \(\tfrac12\operatorname{Tr}_2\otimes\tau\) on this represented coefficient algebra, its value is \(d+r+\kappa_A\).
That normalization is stated explicitly and is not claimed to be the canonical trace of \(G_-\) at a single exceptional orbit.
This two-point orbit model therefore retains the same unknown coefficient kernel despite a genuine finite-order group action, prescribed data at both action-fixed endpoints and identical contour counts at both singular fibers.

## What an exact global defect formula would still have to prove

Let a finite symmetry group act transitively on the complete exceptional set of a polynomial family, and suppose the orbit has \(q\) points and the rank is invariant under that action.
Writing \(\Delta\) for the exact total geometric rank loss, symmetry gives the elementary identity
\[
\delta(z)=\Delta/q\qquad\text{at every exceptional point}.
\tag{19}
\]
Thus an independently proved formula \(\Delta=qk\) with a known integer \(k\) would give integer individual losses.
Merely proving \(\Delta\in\mathbb Z\) gives no such conclusion without divisibility by \(q\), and an upper bound for \(\Delta\) gives neither conclusion.
This is an exact sufficient implication with its premises stated; it supplies no original-input theorem asserting those premises.

For the actual finite inputs (3), the available contour difference is \(qd\), but the geometric total is \(q(r+\kappa_A)\).
Equating them fails by the explicit nonnegative correction \(q\operatorname{rk}_H A\), even with minimal degree, invertible endpoint coefficients, prescribed endpoint values, full generic rank and transitive symmetry.
Proving that the correction divided by \(q\) is always an integer for all torsion-free \(H\) is itself equivalent to A0001, since \(\operatorname{rk}_H A=m-\kappa_A\).
The construction therefore rules out the concrete stronger inference from those data to contour-count equality or bound saturation, while leaving any additional independently established geometric defect identity open.

Starting from an arbitrary A0001 input, the complete attempted chain is as follows.
The finite transformation (1), the compatible certificate (11)--(12), the repeated singular orbit, the minimal degree and the contour values (8) are all established for that same original input.
The first unsupported step is an arithmetic identity for the geometric correction in (10), or a genuinely kernel-preserving comparison avoiding that correction.
Conditional on an independently proved exact geometric total, the next step needs its divisibility by the orbit size, as (19) shows.
Conditional on both facts, subtracting \(r\) in (5), or \(d+r\) in (14), would give \(\kappa_A\in\mathbb Z\) and hence resolve the original all-matrix contract; no further group-representation or affiliated-domain gap remains in this specified encoding.
Neither of those conditional premises is proved here.

The search and reuse scope for this bounded calculation was C_A0012 v1--v2, C_A0011 v1, the [fixed-point rational parity mechanism](../ledger/Yin_L_A0022_v1.md#a-rational-projection-lemma), and the nilpotent point-spectrum distinction cited above.
The parity mechanism in L_A0022 applies to rational projections over a commutative field and proves a divisibility statement for the rank of that same projection; it does not identify the kernel of a singularly specialized original matrix.
No new external theorem, new Atiyah group class or historical novelty is asserted.
The useful continuation condition is an additional original-input property that controls the explicit geometric correction or produces a singular-fiber projection with independently certified arithmetic, rather than another contour invariant or a further copy of the same symmetry orbit.

## Assessment history

### Decision reviewed-symmetric-singular-fibers

| Field | Value |
| --- | --- |
| date | 2026-11-11T19:54 |
| status | proved |
| reason | Independent whole-artifact review verifies the arbitrary-input singular-fiber encoding with fixed contour and symmetry data, its finite compatible realizations and the exact unresolved geometric correction. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All finite input sizes, minimal degree and width, fixed contour and endpoint data, exact singular defects and finite selfadjoint realizations. |
| argument | [Argument](#argument) | Complete nilpotent inverses, contours, symmetries, bounded kernel equations, orbit representation, trace conventions and conditional full-Task chain. |
| review | [Independent whole-artifact finding](../audits/reviews/Yin_R_A0038_v3.md#whole-artifact-finding) | Entire fixed argument and its exact dependency, source and inference scopes. |

## Current assessment

[Selected decision](#decision-reviewed-symmetric-singular-fibers)


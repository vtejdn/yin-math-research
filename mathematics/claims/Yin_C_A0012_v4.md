---
author: Yin
---
# Bounded transverse singularities and the remaining projection arithmetic

Date: 2026-11-12 (Asia/Hong_Kong).
This investigation continues [A0001](../tasks/Yin_T_A0001_v1.md#contract) and [route six](../strategies/Yin_S_A0006.md#compatible-central-variable-specialization), after the fixed arbitrary-input obstructions [C_A0012 v3](../claims/Yin_C_A0012_v3.md#statement) and [C_A0007 v5](../claims/Yin_C_A0007_v5.md#statement).
The bounded test proves an exact local formula under a genuine bounded semisimple split and a boundedly invertible derivative on that split's kernel corner.
Those hypotheses exclude the nonzero nilpotent encoding and its positive square for explicit reasons.
They do not supply the arithmetic of the resulting projection, and the natural pencil based on \(A^*A\) lacks the required complex resolvent gap for legitimate original inputs.

## Original-input chain and the investment boundary

Let \(H\) be any torsion-free discrete group and let \(A\in M_{r,n}(\mathbb CH)\), with \(r,n\ge1\), be the original Task input.
Write \(T=A^*A\), \(p=P_{\ker A}=P_{\ker T}\), and \(\kappa_A=\tau_n(p)\), where \(\tau_n=\operatorname{Tr}_n\otimes\tau_H\) is unnormalized.
Consider the actual finite coefficient pencil
\[
 F_A(z)=T+(1-z)I_n.
 \tag{1}
\]
Its geometric nullity at \(z=1\) is exactly \(\kappa_A\), and \(F_A'(z)=-I_n\) is a bounded unit for every input.
The already proved [compatible singular-fiber realization](../claims/Yin_C_A0012_v2.md#a-compatible-singular-fiber-retaining-an-arbitrary-kernel), with the parameter substitution \(z=-x\), embeds this same pencil into an actual finite selfadjoint group-ring matrix whose generic nullity is \(n\) and whose compatible singular specialization has nullity \(n+\kappa_A\).
Its precise group and trace interfaces are recalled below; this is reuse of that construction, not a new realization claim.

The first extra premise needed for the proposed local contour argument is
\[
 \text{there exists }\gamma>0\text{ such that }
 T\big|_{(1-p)\ell^2(H)^n}\ge\gamma(1-p).
 \tag{2}
\]
This is an actual bounded inverse off the kernel, not the existence of its affiliated inverse or invertibility of \(F_A'(1)\).
It fails for explicit torsion-free group-ring inputs, including the example below with a nonzero known kernel.
Conditional on (2), the local contour is well defined and its trace is exactly \(\kappa_A\).
The decisive later premise is an independently proved integer-trace constraint for the resulting projection \(p\), which lies in \(M_n(C_r^*(H))\).
No general such constraint is supplied by the analytic calculation.
Conditional on both premises, \(\kappa_A\in\mathbb Z\) follows directly and gives the original input's conclusion, with no further specialization or domain gap.
There is no established transformation here that supplies (2) for every original input while preserving its kernel dimension up to a known integer.

This identifies the bounded investigation's benefit before developing the local formula: it can remove the geometric-versus-contour correction for a genuinely narrower class, determine exactly which gap and transversality assumptions do so, and locate the surviving arithmetic obligation.
It cannot close the full Task merely by replacing one contour invariant with another.
The route-five alternative [C_A0007 v5](../claims/Yin_C_A0007_v5.md#complete-chain-attempt-known-coverage-and-continuation-boundary) still needs a defect certificate with independently controlled vertices, complete-kernel inclusion and an off-corner rank not already determined by a unit pivot or energy argument.
No new candidate meeting that separate interface is asserted here.

<a id="statement"></a>
## A local bounded formula with the actual contour idempotent

Let \((\mathcal M,\operatorname{tr})\) be a finite von Neumann algebra with faithful finite trace; any matrix amplification is included in \(\mathcal M\) and in this unnormalized trace.
Let \(F\) be a norm-holomorphic \(\mathcal M\)-valued function on a complex neighborhood of \(z_0\).
Put \(F_0=F(z_0)\), \(F_1=F'(z_0)\), and suppose there is a bounded idempotent \(e\in\mathcal M\) satisfying
\[
 e^2=e,\qquad F_0e=eF_0=0,\qquad
 d_0:=(1-e)F_0(1-e)\text{ is a bounded unit in }(1-e)\mathcal M(1-e).
 \tag{3}
\]
The idempotent need not be orthogonal.
Condition (3) is the precise bounded semisimple split used here: its range is exactly \(\ker F_0\), and the complementary restriction has a bounded inverse.
It is stronger than \(\ker F_0=\ker F_0^2\).
Assume additionally that
\[
 a_1:=eF_1e\text{ is a bounded unit in }e\mathcal M e.
 \tag{4}
\]
If either corner is zero, its invertibility condition is omitted.
An inverse in an absent corner is interpreted as zero in the displayed ambient formulas.
All operators and products in this section are bounded on the stated Hilbert-space summands; no affiliated inverse is used.

For all sufficiently small \(0<|z-z_0|<\varepsilon\), the operator \(F(z)\) has a bounded inverse and
\[
 F(z)^{-1}=(z-z_0)^{-1}a_1^{-1}+H(z),
 \tag{5}
\]
where \(H\) is norm-holomorphic through \(z_0\), and \(a_1^{-1}\) is extended by zero on the complementary summand.
In particular \(\|F(z)^{-1}\|\le C/|z-z_0|\) in a sufficiently small punctured disk, for a constant determined by this fixed input.
For a positively oriented circle \(\Gamma\) centered at \(z_0\) in that disk, the actual operator integral is
\[
 Q_F:=\frac1{2\pi i}\int_\Gamma F(z)^{-1}F'(z)\,dz
 =a_1^{-1}F_1,
 \qquad Q_F^2=Q_F,
 \qquad \operatorname{ran}Q_F=\ker F_0.
 \tag{6}
\]
Consequently, if \(p_0=P_{\ker F_0}\), then
\[
 \boxed{\frac1{2\pi i}\int_\Gamma
 \operatorname{tr}\bigl(F(z)^{-1}F'(z)\bigr)\,dz
 =\operatorname{tr}(Q_F)=\operatorname{tr}(p_0).}
 \tag{7}
\]
The right side is a finite von Neumann dimension, with no integer assertion in this statement.

<a id="argument"></a>
### Complete bounded proof

Write \(w=z-z_0\) and \(f=1-e\), and use the bounded direct sum \(e\mathcal H\oplus f\mathcal H\).
Relative to that sum, write
\[
 F(z)=\begin{pmatrix}a(w)&b(w)\\c(w)&d(w)\end{pmatrix}.
\]
Condition (3) gives \(a(0)=b(0)=c(0)=0\) and \(d(0)=d_0\).
A Neumann series makes \(d(w)^{-1}\) bounded and holomorphic for sufficiently small \(w\).
The Schur expression is
\[
 s(w):=a(w)-b(w)d(w)^{-1}c(w)
 =w a_1+O(w^2)=w h(w),
 \qquad h(0)=a_1.
 \tag{8}
\]
The product subtracted from \(a(w)\) is \(O(w^2)\), since both \(b\) and \(c\) vanish at zero.
Another Neumann series makes \(h(w)^{-1}\) bounded and holomorphic near zero.
The exact bounded factorization
\[
 F(z)=
 \begin{pmatrix}e&b(w)d(w)^{-1}\\0&f\end{pmatrix}
 \begin{pmatrix}s(w)&0\\0&d(w)\end{pmatrix}
 \begin{pmatrix}e&0\\d(w)^{-1}c(w)&f\end{pmatrix}
 \tag{9}
\]
has invertible triangular factors equal to the identity at \(w=0\).
For \(w\ne0\), invert the factors and use \(s(w)^{-1}=w^{-1}h(w)^{-1}\).
The unique coefficient of \(w^{-1}\) in the resulting Laurent series is \(a_1^{-1}\); all other negative powers vanish.
Indeed the triangular factors differ from the identity by \(O(w)\), and \(h(w)^{-1}-a_1^{-1}=O(w)\).
This proves (5), including its holomorphic remainder and norm bound.

Multiplication by \(F'(z)=F_1+O(w)\) proves the integral identity in (6), because bounded norm integrals extract the Laurent coefficient.
Since \(a_1^{-1}=ea_1^{-1}e\), one has
\[
 Q_Fe=a_1^{-1}F_1e=e,\qquad eQ_F=Q_F,
\]
and therefore \(Q_F^2=Q_F\) and \(\operatorname{ran}Q_F=e\mathcal H\).
For the first identity, the factor \(a_1^{-1}\) on the left projects through \(e\), so \(a_1^{-1}F_1e=a_1^{-1}(eF_1e)=e\).
Condition (3) implies \(e\mathcal H=\ker F_0\): if \(F_0x=0\), then \(d_0fx=0\), hence \(fx=0\), while \(F_0e=0\) gives the converse.

Finally any bounded idempotent \(Q\) with range projection \(p\) obeys \(pQ=Q\) and \(Qp=p\).
Thus \(Q=p+pQ(1-p)\), and traciality gives
\(\operatorname{tr}(Q)=\operatorname{tr}(p)+\operatorname{tr}((1-p)pQ)=\operatorname{tr}(p)\).
Applying this to \(Q_F\) proves (7).
Moving the trace through the contour integral is legitimate because the finite trace is a bounded linear functional and the integrand is norm-continuous on the compact circle.

The semisimple split is the familiar isolated-spectrum framework: the directly inspected Kato passage is [Kat95, 1995 reprint](../literature/pdf/Kat95.pdf), §III.6.4, Theorem 6.17, printed pp.178–179/PDF pp.201–202, and §III.6.5, formulas (6.27)–(6.34), printed p.180/PDF p.203.
Those passages distinguish the spectral projection, the quasinilpotent part and the bounded reduced resolvent.
The footnote on printed p.180 explicitly requires isolation in the spectrum, rather than isolation among eigenvalues.
Those original passages were inspected for that distinction and attribution; the finite-von-Neumann trace formula and the transverse Schur calculation (8)–(9) are proved directly above.
No finite Hilbert-space multiplicity theorem is imported to claim integer finite-von-Neumann trace.

## Two inexpensive tests of the hypotheses

### An invertible full derivative does not imply transverse kernel compression

Over the trivial torsion-free group, take
\[
 F(w)=\begin{pmatrix}0&w\\w&1\end{pmatrix},\qquad
 e=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
 \tag{10}
\]
At zero, the complement of the kernel is boundedly invertible and the zero eigenvalue is semisimple.
The full derivative \(F'(0)=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\) is a unit, but \(eF'(0)e=0\).
For \(w\ne0\), direct multiplication gives
\[
 F(w)^{-1}=\begin{pmatrix}-w^{-2}&w^{-1}\\w^{-1}&0\end{pmatrix},
 \qquad
 F(w)^{-1}F'(w)=\begin{pmatrix}w^{-1}&-w^{-2}\\0&w^{-1}\end{pmatrix}.
 \tag{11}
\]
The local contour operator is \(I_2\), with trace two, whereas \(\dim\ker F(0)=1\).
Thus (4) is a substantive condition even when the singular point is isolated, the initial zero is semisimple with a gap, and the full derivative is boundedly invertible.
The Schur expression is \(-w^2\), explaining the extra order directly.

### Transverse derivative and torus isolation do not supply a complex resolvent gap

Let \(H=\langle u\rangle\cong\mathbb Z\), and use the actual finite matrix
\[
 A=\operatorname{diag}(0,1-u),\qquad
 T=A^*A=\operatorname{diag}(0,2-u-u^{-1}).
 \tag{12}
\]
Fourier transformation identifies \(\mathcal N(H)\) with \(L^\infty(\mathbb T)\) and normalized Haar integration, while the matrix trace remains unnormalized.
The second diagonal multiplier is \(2-2\cos\theta\), whose range is \([0,4]\), whose essential range is the same interval, and whose zero set has Haar measure zero.
Thus \(p=\operatorname{diag}(1,0)\), \(\kappa_A=1\), and \(\ker T=\ker T^2\), but the restriction of \(T\) to \(1-p\) has no bounded inverse.
The pencil (1) has \(F_A'(1)=-I_2\) and \(pF_A'(1)p=-p\), an invertible kernel-corner derivative.
Nevertheless its boundedly noninvertible complex parameters fill the segment
\[
 \{z:F_A(z)\text{ has no bounded inverse}\}=[1,5],
 \tag{13}
\]
because \(F_A(z)=T-(z-1)I_2\).
Every small circle about \(1\) meets that segment, so no circle on which the proposed bounded contour integral is defined surrounds only this parameter singularity.
On the unit circle \(\mathbb T\), in contrast, \(z=1\) is the only noninvertible parameter and the only fiber with nonzero kernel.
This test separates an isolated torus rank loss, an invertible compressed derivative, algebraic kernel semisimplicity, and a genuine complex resolvent gap.

For general (1), the same spectral calculation proves the exact equivalence
\[
 \exists\varepsilon>0\ \forall\,0<|z-1|<\varepsilon:
 F_A(z)\text{ has a bounded inverse}
 \quad\Longleftrightarrow\quad
 \exists\gamma>0:\ \sigma(T)\cap(0,\gamma)=\varnothing.
 \tag{14}
\]
The right side includes the case of an already invertible \(T\), when \(p=0\), and the zero operator, when the complementary corner is absent.
If positive spectral points approach zero, their translates by one contradict the left side.
Conversely, under a gap, every sufficiently small nonzero \(z-1\) avoids \(\sigma(T)\).
The spectral theorem identifies the right side with (2).
When \(p\ne0\), the inverse must still grow like \(|z-1|^{-1}\) on \(p\); bounded inverse on each punctured parameter and the bound (5) do not mean uniform boundedness as \(z\to1\).

## The new condition excludes the previous encodings at specific interfaces

For the finite square-zero matrix \(N_A\) in [C_A0012 v3](../claims/Yin_C_A0012_v3.md#a-degree-minimal-symmetric-finite-pencil), each singular fiber of its pencil is \(2N_A\).
If \(A\ne0\), then \(N_A\ne0\), \(N_A^2=0\), and no split (3) can exist.
Indeed a complementary restriction of a square-zero operator would also have square zero; if it were invertible its corner identity would be zero, forcing \(e=I\), after which \(F_0e=0\) would force \(N_A=0\).
Thus the new condition excludes the entire nonzero nilpotent encoding for a proved operator reason, rather than an endpoint or orbit invariant.
For \(A=0\), that pencil is scalar and its geometric and contour multiplicities already agree.

Its positive Laurent matrix does not restore the new premise.
For a finite polynomial \(P\), write \(P^\sharp(z)=P(1/\overline z)^*\), interpreted by coefficient adjoints and negative powers as a holomorphic Laurent matrix on \(\mathbb C^\times\).
Then \(Q(z)=P^\sharp(z)P(z)\) agrees with \(P(z)^*P(z)\) on the unit circle.
At any \(\zeta\in\mathbb T\) with nonzero kernel projection \(p_\zeta=P_{\ker P(\zeta)}\), one has
\[
 p_\zeta Q'(\zeta)p_\zeta
 =p_\zeta (P^\sharp)'(\zeta)P(\zeta)p_\zeta
  +p_\zeta P(\zeta)^*P'(\zeta)p_\zeta=0.
 \tag{15}
\]
The first term vanishes because \(P(\zeta)p_\zeta=0\), and the second because \(p_\zeta P(\zeta)^*=0\).
Even if \(Q(\zeta)\) has a positive off-kernel gap, its compressed derivative fails (4).
This applies to every singular fiber of the positive square in C_A0012 v3, where the kernel is nonzero by construction.

The different pencil (1) based on \(A^*A\) has the transverse derivative for every input, but meets (3) exactly when (2) holds.
It is therefore not excluded on every gapped original input; on those inputs the geometric correction vanishes, while the same original kernel persists as the contour projection itself.
This is a distinct surviving obstruction, rather than a claim that the new local formula defeats all arbitrary-input encodings.

## The actual finite transport embedding and its unchanged correction

Reuse the exact construction in [C_A0012 v2](../claims/Yin_C_A0012_v2.md#a-compatible-singular-fiber-retaining-an-arbitrary-kernel).
With independent infinite cyclic generators \(x,t\), put
\[
 N=H\times\langle x\rangle,\qquad
 G=N\rtimes_\sigma\langle t\rangle,\qquad
 \sigma(h)=h,\quad\sigma(x)=x^{-1}.
 \tag{16}
\]
The displayed embeddings of \(H\) and \(N\) are injective by the semidirect-product construction.
A finite-order element of \(G\) must have zero image in the height quotient \(\mathbb Z\), hence lies in the torsion-free subgroup \(N\); consequently \(G\) is torsion-free.
The finite matrices are
\[
 C(x)=F_A(-x)=T+(1+x)I_n,\quad
 M(x)=(C(x)\ \ 0_{n,n}),\quad D=M^*M,
\]
\[
 \mathcal H_A=
 \begin{pmatrix}(t+t^{-1})I_{2n}&D\\D&0\end{pmatrix}
 \in M_{4n}(\mathbb CG).
 \tag{17}
\]
At \(x=1\), the row Gram \(M(1)M(1)^*=(T+2I_n)^2\ge4I_n\), so [C_A0012 v1](../claims/Yin_C_A0012_v1.md#statement) applies with an independently bounded identity-specialization inverse.
The complete integrated coefficient kernel is \(p_{\mathrm{gen}}=\operatorname{diag}(0_n,I_n)\), and the complete matrix kernel is \(\operatorname{diag}(0_{2n},p_{\mathrm{gen}})\), of unnormalized trace \(n\).

The coefficient \(*\)-homomorphism \(x\mapsto-1\), fixing \(H,t\), is compatible with \(txt^{-1}=x^{-1}\), since both sides specialize to \(-1\).
It maps (17) to a finite matrix over \(\mathbb C[H\times\langle t\rangle]\).
The separately computed specialized coefficient kernel is \(p_-=\operatorname{diag}(p,I_n)\), and the complete specialized matrix kernel is \(\operatorname{diag}(0_{2n},p_-)\), of trace \(n+\kappa_A\).
These exact kernel identities, including the bounded equations using the injective central height sum \(t+t^{-1}\), are the fixed result being reused.
Canonical subgroup trace preservation identifies \(\kappa_A\) in these product groups with the original \(H\)-trace.
Thus (7), when its additional bounded-gap hypothesis holds, identifies the actual singular-fiber correction in (17) as a contour trace, but does not eliminate or change its value \(\kappa_A\).
No affiliated expression is evaluated at its undefined inverse gate.

## What the bounded gap provides in the reduced group C*-algebra

For (1) under (2), choose a scalar \(R>\|T\|\).
The spectral theorem gives the norm-convergent sequence
\[
 \left(I_n-\frac{T}{R}\right)^k\longrightarrow p,
 \qquad
 \left\|\left(I_n-\frac{T}{R}\right)^k-p\right\|
 \le(1-\gamma/R)^k
 \tag{18}
\]
when the complementary corner is nonzero and \(\gamma\) is chosen as in (2).
The absent-corner case gives \(p=I_n\) directly.
Every approximant in (18) is a finite group-ring matrix, so \(p\in M_n(C_r^*(H))\).
For \(F_A\), formula (6) gives \(Q_{F_A}=p\), and the contour value in (7) is precisely the canonical trace of this actual C*-projection.
This is stronger regularity of the projection than arbitrary von Neumann-algebra membership, but it does not compute its trace.

More generally, if every \(F(z)\) in the local theorem belongs to \(M_n(C_r^*(H))\), the idempotent \(e\) in (3) is the usual Riesz idempotent of \(F_0\) at zero and belongs to the same C*-algebra.
To see the Riesz assertion directly, the split (3) makes the resolvent of \(F_0\) equal to the sum of \(\lambda^{-1}e\) and a term holomorphic near zero, in the convention \((\lambda I-F_0)^{-1}\).
Its small contour integral is therefore \(e\).
Every bounded inverse of an element \(X\in M_n(C_r^*(H))\) that exists in the ambient von Neumann algebra is in the C*-algebra: \(X^*X\ge cI\) for some \(c>0\), and a norm-convergent Neumann series gives \((X^*X)^{-1}\), hence \(X^{-1}=(X^*X)^{-1}X^*\).
Applying this to the resolvents and using norm-closedness proves the assertion about \(e\).
The range projection \(p_0\) of \(e\) also belongs to this C*-algebra.
Indeed \(ee^*\) is zero on the orthogonal complement of \(\operatorname{ran}e\) and is bounded below by the identity on that range, because \(ex=x\) implies \(\|e^*x\|\ge\|x\|\).
For \(R>\|ee^*\|\), the same norm-polynomial approximation as in (18) gives \(p_0=I_n-\lim_{k\to\infty}(I_n-ee^*/R)^k\).

A sufficient additional arithmetic premise would be
\[
 \tau_k(q)\in\mathbb Z
 \quad\text{for every projection }q\in M_k(C_r^*(H))
 \text{ and every }k\ge1,
 \tag{19}
\]
or a weaker independently proved version for the actual projection produced here.
Condition (19) is stated as an additional premise, not claimed for arbitrary torsion-free groups and not asserted equivalent to the all-matrix Task.
The calculation above only proves that it would imply the desired conclusion for gapped inputs.
In particular a loop of bounded invertibles in a finite von Neumann algebra has no automatic integer logarithmic-trace winding number.

For a direct test of that last inference, let \(\mathcal M=\mathcal N(\mathbb Z)=L^\infty(\mathbb T)\) and take a characteristic projection \(q=1_E\) with Haar measure \(0<\theta<1\).
The bounded pencil
\[
 F(w)=(1-q)-wI
 \tag{20}
\]
has a semisimple split with off-kernel gap one, derivative \(-I\), and inverse
\[
 F(w)^{-1}=-w^{-1}q+(1-w)^{-1}(1-q).
\]
For a circle of radius less than one, the logarithmic contour operator is exactly \(q\) and its trace is \(\theta\).
Thus all analytic assumptions of the local theorem allow arbitrary noninteger trace when the finite group-ring origin is removed.
This example is not an A0001 counterexample: its nonconstant characteristic coefficient is not in \(\mathbb C\mathbb Z\), nor in \(C_r^*(\mathbb Z)=C(\mathbb T)\).
It proves exactly that analytic semisimplicity, transversality and bounded contour inversion do not themselves establish the missing arithmetic.

There is a directly controlled comparison scope for (19).
If the original finite support lies in a torsion-free abelian subgroup \(K\), that support generates \(K_0\cong\mathbb Z^d\), and the gapped projection lies in \(M_n(C(\mathbb T^d))\).
Its pointwise ordinary matrix rank is continuous and integer valued, hence constant on the connected torus.
The canonical unnormalized trace is the Haar integral of that constant rank, so is the same integer.
Subgroup trace preservation transfers it back to \(H\).
This supplies an independent arithmetic certificate in an already known abelian case, without converting the analytic contour formula into a theorem for arbitrary \(H\).
The [known-results synthesis](../ledger/Yin_L_A0001_v1.md#known-positive-results) already covers torsion-free abelian and the relevant abelian-by-cyclic calibration groups; no new whole-group Atiyah coverage is asserted.

## Why routine finite regularization does not remove the first gap

Suppose \(0\) is an accumulation point of the positive spectrum of \(T\).
For any nonzero scalar polynomial \(f\) with \(f(0)=0\), choose positive \(\lambda_j\in\sigma(T)\) decreasing to zero.
There are only finitely many nonzero roots of \(f\), so after discarding finitely many \(\lambda_j\), one has \(f(\lambda_j)\ne0\) while \(f(\lambda_j)\to0\).
The spectral theorem therefore puts nonzero spectrum of \(|f(T)|\) arbitrarily close to zero.
If \(f\) has no nonzero zero on \(\sigma(T)\), then it preserves \(\ker T\), but it still cannot provide a bounded inverse off that kernel.
The identically zero polynomial changes the complete kernel unless \(T=0\), so it gives no universal repair.

The same obstruction applies to any enlargement obtained from \(A\oplus I_k\) by boundedly invertible left and right operators of the appropriate sizes.
For bounded Hilbert-space operators, a positive gap for \(A^*A\) off its kernel is equivalent to closedness of \(\operatorname{ran}A\).
In one direction the gap makes \(A\) bounded below on \((\ker A)^\perp\), which makes its range closed.
In the other direction the bounded inverse theorem applied to \(A:(\ker A)^\perp\to\operatorname{ran}A\) gives that lower bound.
The range of \(A\oplus I_k\) is closed exactly when \(\operatorname{ran}A\) is closed, and bounded invertible left and right multiplication preserves this property.
Thus this entire stabilization-and-bounded-normalization class cannot make (2) true for the nongapped example (12).
Allowing an unbounded affiliated inverse escapes this argument but also escapes the bounded local-resolvent hypothesis whose applicability is being tested.
This exclusion does not cover every conceivable finite group-ring transformation.

## Continuing question and evidence limits

The result of this test is an exact sufficient local geometric formula, two distinct failures of weaker derivative/gap hypotheses, and a separate projection-arithmetic obligation after the geometric correction has vanished.
The proof works in a finite von Neumann algebra and does not infer an integer from finite Hilbert multiplicity, ordinary determinant winding, boundedness of the contour inverse at each point, or an invariant of nonsingular loops.
For the actual original-input family (1), the exact remaining order is: obtain a genuine off-kernel gap without losing the original kernel, identify the actual contour projection as above, and prove its integer trace from independently available finite group-ring structure.
The first step is false if imposed directly on all original inputs and cannot be supplied by the bounded normalization class just tested.
The final step is not established here for arbitrary torsion-free coefficient groups even on this gapped subclass.

A useful continuation would therefore need either a kernel-preserving finite construction outside those bounded normalizations with a proved gap and independently controlled projection arithmetic, or an independent trace certificate for the actual contour projection that does not assume the desired original rank.
Another positive square, endpoint condition, minimal-degree assertion, repeated singular orbit or nonsingular contour homotopy does not address these two explicit obligations.
The local search/reuse scope was C_A0007 v5, C_A0012 v1–v3, their two strategy interfaces, the known-results synthesis, and the named original Kato passages on isolated spectrum and reduced resolvents.
The Kato source was sufficient for the recognized classical distinction; no broader source theorem, literature novelty claim or new group-wide permanence result is asserted.

## Assessment history

### Decision reviewed-bounded-transverse-defects

| Field | Value |
| --- | --- |
| date | 2026-11-12T01:27 |
| status | proved |
| reason | Independent whole-artifact review supports the bounded transverse contour formula, exact geometric trace, countertests, finite transport and remaining gap and projection-arithmetic obligations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Local bounded inverse expansion and contour idempotent under the stated semisimple split and compressed derivative hypotheses, with exact range and finite trace. |
| argument | [Argument](#argument) | Complete Schur proof, countertests, finite group-ring transport, C*-membership and regularization exclusions, preserving the conditional original-input chain. |
| review | [Independent whole-artifact finding](../audits/reviews/Yin_R_A0038_v4.md#whole-artifact-finding) | Complete fixed artifact, exact reused interfaces and original Kato passages, with foundational and full-Task limits explicit. |

## Current assessment

[Selected decision](#decision-reviewed-bounded-transverse-defects)


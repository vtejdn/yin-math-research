---
author: Yin
---
# Central specialization obstructs finite kernel-preserving gap creation

This argument studies [A0001](../tasks/Yin_T_A0001_v1.md#contract) through the bounded-gap interface of [C_A0012 v4](../claims/Yin_C_A0012_v4.md#statement).
The question is whether a finite group-ring construction using independently controlled auxiliary operators can preserve an arbitrary original kernel while creating a complementary spectral gap.
The current scope is finite Laurent matrices over a direct product with a central infinite cyclic group, including tensor constructions using the free-group boundary.
The intended discriminating calculation compares a genuine fiber-nullity jump with the integrated small positive singular spectrum.
This is development by a delegated agent for Yin, not an independent review or a selected Claim.
Throughout, \(\nu\) denotes the von Neumann dimension of the complete Hilbert-space kernel, using the canonical group trace and unnormalized matrix trace in group applications.

## Complete-chain test and existing coverage

For an arbitrary Task input \(A\in M_{r,n}(\mathbb CH)\), a successful version of this route would first produce an actual finite matrix \(B_A\) over a specified torsion-free extension, then prove an exact kernel-dimension relation, then prove a complementary spectral gap, and finally supply independent arithmetic for the resulting projection.
The bounded contour calculation in C_A0012 v4 handles the local analytic step after a gap has actually been obtained; it does not supply the last arithmetic premise.
The first construction below has an independently bounded auxiliary inverse and preserves the entire original nullity exactly, but its complementary gap is equivalent to the original gap.
The later obstruction applies to arbitrary finite central Laurent outputs with a singular fiber, without assuming that the output is a scalar polynomial in the input or an invertible stabilization.
It therefore excludes a wider precisely stated class of proposed gap constructions while leaving noncentral constructions and noncompatible changes of kernel representation open.

The existing inputs read for this question are [C_A0012 v4](../claims/Yin_C_A0012_v4.md), its [independent review](../audits/reviews/Yin_R_A0038_v4.md), [C_A0007 v5](../claims/Yin_C_A0007_v5.md), and its [independent review](../audits/reviews/Yin_R_A0020_v5.md).
The exact generic-rank theorem of [C_A0012 v2](../claims/Yin_C_A0012_v2.md#exact-generic-rank-for-rectangular-laurent-matrices), checked with its [reviewed interface](../audits/reviews/Yin_R_A0038_v2.md#exact-generic-rank), already supplies the almost-everywhere constant fiber nullity needed below.
The free-group auxiliary inverse is the existing [degree-four tree gap](../claims/Yin_C_A0004_v2.md#free-projection-and-gap), with its [independently reviewed normalization](../audits/reviews/Yin_R_A0017_v2.md#weighted-free-tree-matrices-and-isolated-atom).
These retained results suffice for the present deductions.
No new external theorem, source identification, literature priority claim or group-wide positive Atiyah class is asserted.

## A finite auxiliary construction with an independently bounded pivot

Let \(F=F(a,b)\) and define
\[
 d=(1-a\ \ 1-b)\in M_{1,2}(\mathbb CF),
 \qquad \Delta=dd^*=4-a-a^{-1}-b-b^{-1}.
 \tag{1}
\]
The checked tree bound gives
\[
 \Delta\ge\gamma I,\qquad \gamma=4-2\sqrt3>0.
 \tag{2}
\]
Thus the auxiliary inverse is certified independently of any information about \(A\), and
\[
 q=I_2-d^*\Delta^{-1}d=P_{\ker d},
 \qquad (\operatorname{Tr}_2\otimes\tau_F)(q)=1.
 \tag{3}
\]
Indeed \(d^*\Delta^{-1}d\) is an orthogonal projection, and rectangular traciality gives its trace as \(\tau_F(\Delta^{-1}dd^*)=1\).
The same calculation gives its complementary trace one without invoking the Atiyah conjecture for any group.
The projection \(q\) is nonzero and bounded; it is not asserted to be a finite group-ring matrix.

Put \(G=H\times F\), \(T=A^*A\), and \(p=P_{\ker A}\).
The group \(G\) is torsion-free because both factors are torsion-free.
The group embeddings and the regular representation give the actual Hilbert space tensor product, von Neumann tensor product and product trace used in the following formulas.
On \(\ell^2(H)^n\bar\otimes\ell^2(F)^2\), define the finite positive group-ring matrix
\[
 Q_A=T\otimes I_2+I_n\otimes d^*d
 \in M_{2n}(\mathbb C[H\times F]).
 \tag{4}
\]
The tensor notation in (4) denotes the displayed finite entrywise group-ring construction.
Equivalently, after ordering the coordinates consistently, \(Q_A=R_A^*R_A\), where
\[
 R_A=\begin{pmatrix}A\otimes I_2\\I_n\otimes d\end{pmatrix}
 \in M_{2r+n,2n}(\mathbb CG).
 \tag{5}
\]
Both summands in (4) are positive and commute, so their joint zero space is the intersection of their kernels.
Consequently
\[
 P_{\ker Q_A}=p\otimes q,
 \qquad \nu_G(Q_A)=\nu_H(A).
 \tag{6}
\]
This preserves arbitrary input nullity exactly, with no unknown additive correction.

Nevertheless,
\[
 Q_A\text{ has a positive spectral gap off its kernel}
 \quad\Longleftrightarrow\quad
 T\text{ has a positive spectral gap off its kernel}.
 \tag{7}
\]
On the reducing summand \(I_n\otimes q\), the operator \(Q_A\) is exactly \(T\otimes I_q\).
Since \(q\ne0\), any unit approximate zero sequence for \(T\) orthogonal to \(p\) tensors with a unit vector in \(q\ell^2(F)^2\) to give such a sequence for \(Q_A\) orthogonal to \(p\otimes q\).
This proves the obstructed direction of (7) without comparing kernels through an unbounded map.
For the converse, polar decomposition of \(d\) and (2) give
\[
 d^*d\ge\gamma(I_2-q).
\]
If \(T\ge\eta(I_n-p)\), then on the orthogonal complement of \(p\otimes q\), the two reducing pieces \(I_n\otimes q\) and \(I_n\otimes(I_2-q)\) give the lower bound \(\min(\eta,\gamma)\).
The case \(p=I_n\) has no first complementary piece and is controlled directly by \(\gamma\).
These observations include the zero and injective input cases and prove (7).

Thus nonamenability of the auxiliary factor and its independently invertible row Gram do not provide the missing regularization.
Its nonzero auxiliary kernel, which is exactly what preserves the original nullity in (6), also retains the original small positive spectrum.
This is an explicit finite construction and exact failure calculation, not an assertion that every auxiliary construction has this form.
It is also not a new group-wide integrality theorem: for arbitrary \(H\), the unresolved trace in (6) is the original one.

<a id="argument"></a>
## A bounded perturbation estimate detecting a lost kernel

Let \(\mathcal M\) be a finite von Neumann algebra with faithful normal finite trace \(\tau\), and let \(B_0,B\in M_{m,n}(\mathcal M)\).
Use the unnormalized trace \(\tau_n=\operatorname{Tr}_n\otimes\tau\) on the domain.
Write \(p_0=P_{\ker B_0}\), and suppose \(\|B-B_0\|\le\varepsilon\), with \(\varepsilon>0\).
Then
\[
 \boxed{\tau_n\bigl(1_{[0,\varepsilon]}(|B|)\bigr)
 \ge\tau_n(p_0).}
 \tag{8}
\]
Here \(1_{[0,\varepsilon]}(|B|)\) includes the actual zero spectral projection; that term will be removed explicitly below.

Set \(e=1_{(\varepsilon,\infty)}(|B|)\).
If \(0\ne x\in p_0\mathcal H^n\cap e\mathcal H^n\), the first membership gives \(\|Bx\|\le\varepsilon\|x\|\), whereas the second gives \(\|Bx\|>\varepsilon\|x\|\) by the spectral theorem.
Thus \(p_0\wedge e=0\).
The bounded operator \((1-e)p_0\), restricted to \(p_0\mathcal H^n\), has zero kernel because its kernel is exactly that intersection.
Its initial support is therefore \(p_0\), and its final support lies under \(1-e\).
Polar decomposition and finite traciality imply \(\tau_n(p_0)\le\tau_n(1-e)\), proving (8).
No closed-range assumption on this auxiliary map is used.

Subtracting the actual kernel of \(B\) yields the quantitative form
\[
 \boxed{\tau_n\bigl(1_{(0,\varepsilon]}(|B|)\bigr)
 \ge\nu(B_0)-\nu(B),}
 \qquad \nu(C):=\tau_n(P_{\ker C}).
 \tag{9}
\]
The right side may be negative, in which case the inequality still holds but supplies no positive information.
This is a direct support calculation using the existing [polar-decomposition rank interface](../ledger/Yin_L_A0006_v1.md#affiliated-rank-and-the-kernel-dimension-statement); no finite-dimensional multiplicity or integer-valued trace enters it.

<a id="statement"></a>
## Every exceptional central Laurent fiber forces small positive spectrum

Let
\[
 B(z)=\sum_{j=a}^{b}B_jz^j\in
 M_{m,n}(\mathcal M[z,z^{-1}])
 \tag{10}
\]
have finitely many bounded coefficients.
Let \(\mathcal B\) denote its actual operator in
\(M_{m,n}(\mathcal M\bar\otimes L^\infty(\mathbb T))\), and use normalized Haar measure on the circle.
Define
\[
 \kappa_{\mathrm{gen}}=\nu(\mathcal B),\qquad
 F_B(\varepsilon)=
 (\tau_n\otimes\mu)\bigl(1_{(0,\varepsilon]}(|\mathcal B|)\bigr),
 \qquad
 L_B=\sum_{j=a}^{b}|j|\,\|B_j\|.
 \tag{11}
\]
The exact generic-rank theorem of C_A0012 v2 gives
\(\nu(B(z))=\kappa_{\mathrm{gen}}\) for Haar-almost every \(z\), and every fiber has nullity at least \(\kappa_{\mathrm{gen}}\).
Suppose a specified actual fiber \(z_0\in\mathbb T\) has excess nullity
\[
 \delta=\nu(B(z_0))-\kappa_{\mathrm{gen}}>0.
 \tag{12}
\]
Then \(L_B>0\), and for every \(\varepsilon>0\),
\[
 \boxed{F_B(\varepsilon)
 \ge\frac{\delta}{\pi}
 \min\left\{\pi,\frac{\varepsilon}{L_B}\right\}>0.}
 \tag{13}
\]
In particular \(\mathcal B\) has nonclosed range, and neither \(|\mathcal B|\) nor \(\mathcal B^*\mathcal B\) has a positive gap on its kernel complement.

To prove (13), write \(z=z_0e^{it}\), with \(-\pi<t\le\pi\).
The scalar inequality \(|e^{ijt}-1|\le|j|\,|t|\) gives
\[
 \|B(z_0e^{it})-B(z_0)\|\le L_B|t|.
 \tag{14}
\]
If \(L_B=0\), the polynomial is constant on the circle, contradicting (12).
For \(|t|\le\min(\pi,\varepsilon/L_B)\), apply (9) to the two actual fibers.
Outside the Haar-null exceptional set, the right side is exactly \(\delta\).
Bounded functional calculus in the actual von Neumann tensor product gives
\[
 F_B(\varepsilon)=\int_{\mathbb T}
 \tau_n\bigl(1_{(0,\varepsilon]}(|B(z)|)\bigr)\,d\mu(z).
 \tag{15}
\]
This identity follows first for bounded continuous functions and then for the indicated Borel indicator by bounded measurable functional calculus and normality of the trace.
In particular its integrand is measurable; no arbitrary pointwise representative of a kernel projection is specialized.
Integrating the lower bound over an arc of normalized measure
\(\min(\pi,\varepsilon/L_B)/\pi\) proves (13).
The closed-range conclusion is the bounded-operator equivalence already used in [C_A0012 v4](../claims/Yin_C_A0012_v4.md#why-routine-finite-regularization-does-not-remove-the-first-gap).

More generally, the same proof applies whenever a norm-continuous bounded matrix field has a local estimate \(\|B(z_0e^{it})-B(z_0)\|\le C|t|^k\) and the almost-everywhere nullity on that arc is at most \(\nu(B(z_0))-\delta\).
For \(0<\varepsilon\le Ct_0^k\), where the estimate holds on \(|t|\le t_0\le\pi\), it gives
\[
 F_B(\varepsilon)\ge\frac{\delta}{\pi}
 \left(\frac{\varepsilon}{C}\right)^{1/k}.
 \tag{16}
\]
This final variant needs \(C>0\) and \(k>0\), and refers only to the indicated local assumptions; it does not assert a universal order of vanishing or asymptotic equality.

## Consequence for a finite construction compatible with scalar specialization

Let \(K\) be any torsion-free discrete auxiliary group and let a proposed output be an actual finite matrix
\[
 B\in M_{m,N}(\mathbb C[K\times\langle u\rangle]).
 \tag{17}
\]
No amenability, coefficient-commutation, unit-pivot, scalar-polynomial-calculus or invertible-stabilization premise is imposed on its \(K\)-coefficients.
The central generator \(u\) gives the actual finite Laurent fibers \(B(z)\in M_{m,N}(\mathbb CK)\), and \(K\times\langle u\rangle\) remains torsion-free.
Suppose this output is claimed to preserve the kernel of the scalar input \(1-u\), up to a known constant \(c\ge0\), both before and after scalar specialization, in the precise sense
\[
 \nu_{K\times\mathbb Z}(B)=c,
 \qquad \nu_K(B(1))=c+1.
 \tag{18}
\]
Then (12) holds with \(\delta=1\), so the actual output (17) has no complementary spectral gap.
There is no need to assume the kernel relation separately at every other scalar parameter: C_A0012 v2 already gives its generic value from the integrated operator in (18).
For an input with an additional displayed zero block, the identical conclusion follows from generic and special nullities \(c+1\) and \(c+2\).
The test therefore includes examples whose original kernel is nonzero.

In particular, a fixed finite block construction using \(A,A^*\), scalar matrices and arbitrary fixed auxiliary group-ring coefficients, with the original cyclic generator commuting with the auxiliary group and with the claimed kernel identity valid under \(u=1\), cannot be a universal gap-producing transformation.
Uniformly bounded auxiliary inverse gates, if used and independently certified on a neighborhood of the specialization, still produce a norm-continuous local field and are subject to (9) and (16) whenever their actual kernel relation supplies the same local jump.
An inverse that becomes unbounded or undefined at the special fiber does not satisfy this premise and cannot be substituted there by continuity.
The final output must still be a finite group-ring matrix if it is to satisfy the intended construction requirement.

This obstruction does not cover a finite matrix over a genuinely noncentral extension whose original generator no longer defines these bounded fibers.
It also does not cover a construction chosen separately for the unspecialized input that lacks the exact relation (18), even if it preserves that one input's nullity.
Those are substantive possible escapes from the theorem, not evidence that either escape supplies a gap or an integer trace.
Even a successful escape would retain the independent projection-arithmetic obligation in C_A0012 v4.

## Retention and remaining research scope

The developed result is the quantitative implication (12)--(13) and its specialization-compatible finite-construction consequence (17)--(18), together with the concrete independently pivoted auxiliary test (1)--(7).
It adds no claim of integrality from a gap and no counterexample to A0001.
The self-check covered the rectangular domain trace, the strict spectral inequality in (8), the removal of zero mass in (9), the normalized arc measure and the actual tensor-product trace in (15), including zero and absent-corner cases in the auxiliary example.
The independent whole-artifact review selected below checks the low-spectrum estimate at its exact generic-rank dependency and specialization scope.
The next useful construction must either break the central specialization interface while preserving an independently justified kernel relation, or exploit additional structure already proving the input's closed range and then address the separate trace-arithmetic question.

## Assessment history

### Decision reviewed-central-gap-obstruction

| Field | Value |
| --- | --- |
| date | 2026-11-12T01:58 |
| status | proved |
| reason | Independent whole-artifact review verifies the quantitative positive spectral mass forced by a singular central fiber, the resulting obstruction to specialization-compatible gap creation and the exact auxiliary tensor test. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Rectangular central Laurent matrices with positive excess fiber nullity have the stated lower bound on every small positive singular-value interval and cannot have closed range; exact specialization scope is retained. |
| argument | [Argument](#argument) | Complete perturbation and trace proof, generic-rank interface, Haar integration, local estimate, finite construction consequence and unchanged auxiliary example. |
| review | [Independent whole-artifact finding](../audits/reviews/Yin_R_A0038_v5.md#whole-artifact-finding) | Whole fixed artifact, exact dependencies, all complete kernels, normalizations and remaining full-Task limits. |

## Current assessment

[Selected decision](#decision-reviewed-central-gap-obstruction)


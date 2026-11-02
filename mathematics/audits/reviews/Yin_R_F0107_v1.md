---
author: Yin
---

<a id="original-f0067-account"></a>

# Independent Review: Bounded Division Closure for Two Projections

The complete original account of R_F0067 is retained at its original date, exact mathematical scope, accepted source depth and unknown historical context relationship.
The new findings below record a later isolated inspection and do not backfill the old context or date.

- Date and reviewer: 2026-09-11; the reviewing agent, independently reviewing a proof written by another agent.
  The reviewer did not author or modify the target.
- Target: two-projection-bounded-closure.md (original material now separated into [Yin_C_F0099_v1](../../claims/Yin_C_F0099_v1.md), [Yin_C_F0100_v1](../../claims/Yin_C_F0100_v1.md), [Yin_L_F0025_v1](../../ledger/Yin_L_F0025_v1.md)), all of Sections 2-4, with Sections 1 and 5 checked for source and conclusion scope.
- Starting state: two complete candidates: an arbitrary-pair counterexample and the equality for two freely independent projections of arbitrary traces.
- Verdict: **pass for both candidates at the stated scope; no mathematical gap found.**

## 1. Source Interfaces and Notation

The reviewer independently reopened [Collins-Kemp, arXiv:1211.6037v3](https://arxiv.org/pdf/1211.6037).
Equations (1.5)-(1.7), printed pp. 3-4, give the free Bernoulli product law, its interval endpoints, and the interpretation of the mass at 1 as the trace of the intersection projection.
Section 4.2, printed p. 45, gives the four central characters and the generic matrix model used in the target.
These exact statements and their application interfaces were checked; neither the original convolution computation nor the full paper was re-audited.

The statement of Halmos's decomposition was also checked in [Bottcher-Simon-Spitkovsky, arXiv:1705.08937v2](https://arxiv.org/pdf/1705.08937), Section 3, printed pp. 5-6, equations (6)-(9).
Its generic parameter can have 0 or 1 in its spectrum, but neither endpoint is an eigenvalue.
Its subspace subscripts differ from the target's character subscripts; the target consistently uses the Collins-Kemp convention.
The original Halmos proof was not inspected.

In the target, \(A=\mathbb C\langle p,q\rangle\) is already a *-algebra because both generators are projections.
In particular \(b^*=(1-p)qp\) belongs to A without enlarging the generators.
Both division closures allow successive inverses of individual elements in their specified ambient algebra.
The proof does not replace this operation with matrix inversion closure or norm closure.

## 2. Central Parameter and Noncentral Rational Expressions

Direct multiplication verifies
\[
T=1-p-q+pq+qp=1-(p-q)^2=(1-p-q)^2,
\quad [T,p]=[T,q]=0,\quad Tp=pqp.
\]
The decomposition of q in the target follows by its four p-corners.
On the generic corner, \(T=tI_2\), \(b=sE_{12}\), and \(s^2=t(1-t)\).
On the character corners T takes the stated values 0 or 1.

The rational normal form is valid for arbitrary elements of the scalar affiliated division closure, not just its center.
Indeed the displayed matrices
\[
\begin{pmatrix}a&sc\\sd&h\end{pmatrix},\qquad a,c,d,h\in\mathbb C(t),
\]
form a unital algebra.
Multiplication preserves the form because every product of two off-diagonal weights contributes \(s^2=t(1-t)\).
Its inverse is exactly the target's adjugate formula with determinant \(ah-t(1-t)cd\); the coefficients commute as functions of the central variable t even though the resulting matrices need not commute.

There is no inverse-domain gap in this induction.
Compression by the central generic projection e is a unital ring homomorphism into the corner with identity e, and maps an actual inverse to the inverse of the compressed element.
A scalar expression formed by finitely many allowed inverses can therefore be compressed at each step.
On the diffuse interval measure used here, an invertible generic matrix has determinant nonzero almost everywhere; its rational determinant cannot be identically zero.
Zeros and poles of a nonzero rational function form a finite null set.
Thus the formal formula represents the actual inverse in the affiliated corner.
This operation never requires a new inverse at a character where the original expression was undefined.

## 3. Arbitrary-Pair Counterexample

The two displayed matrices are projections.
In the explicit direct sum, the zero spectral projection of \(T=0\oplus tI_2\) is exactly the scalar summand, since the generic parameter has no atom at 0.
On its complement the polar part of \(b=sE_{12}\), with \(s>0\) almost everywhere, is \(E_{12}\).
Together with its adjoint and the spectral calculus of t, this generates the full generic matrix algebra.
Consequently the declared ambient algebra really is \(W^*(p,q)\).

The element x has scalar value 1 and generic matrix
\[
x(t)=\begin{pmatrix}1&s\\s&2t\end{pmatrix},
\qquad \det x(t)=t(1+t)>0.
\]
Its leading principal minor and determinant show positivity for every \(0<t<1/2\).
Thus x has zero kernel and a densely defined spectral inverse affiliated with the finite von Neumann algebra.
The generic inverse is
\[
x(t)^{-1}=\frac1{t(1+t)}
\begin{pmatrix}2t&-s\\-s&1\end{pmatrix}.
\]
Its lower-right entry diverges at 0, so this is not a bounded inverse.
Compression by p nevertheless gives the bounded expression f in the target, whose essential norm is 2.
This verifies membership in the affiliated division closure and makes no bounded-inverse inference.

The C*-algebra exclusion is also valid.
At t=0 both generic generators are diagonal, with upper-left entries equal to their scalar summand values.
Every noncommutative polynomial therefore has a diagonal endpoint matrix with the same matching property.
Diagonality is the small implicit fact ensuring that the upper-left entry of a product is the product of the matching entries.
Full support of Lebesgue measure on \((0,1/2)\) makes the essential norm of any continuous matrix representative equal to its uniform norm on \([0,1/2]\).
Thus norm limits retain a continuous representative and the same matching condition.
The generic upper-left endpoint of f is 2, while its scalar value is 1, so \(f\notin C^*(p,q)\).

For any \(y\in C^*(p,q)\) invertible in \(\mathcal M\), \(y^*y\) is bounded below by a positive scalar.
Continuous functional calculus in the unital C*-algebra gives \((y^*y)^{-1}y^*\) there.
It is the inverse of y in \(\mathcal M\).
Hence the entire bounded scalar division closure lies in \(C^*(p,q)\), proving the claimed strict inclusion.

The alternative expression for \(e_{10}\) is correct on the scalar and generic summands.
Its use of \(x^{-1}\) is genuinely affiliated and unbounded.
Finally, the normalized trace gives \(\tau(p)=3/4\), \(\tau(q)=1/4\), and \(\tau(pq)=1/16\).
The pair is not free.
**Finding: the counterexample passes, with its obstruction located at an attached endpoint character.**

## 4. Free Traces and Endpoint Cases

For \(0<\alpha,\beta<1\), the cited product law supplies the target's nondegenerate interval K with positive density in its interior.
The generic matrix trace gives half of the generic parameter measure as the product's continuous spectral measure, so that law determines the same generic support K; the factor two affects neither support nor essential boundedness.

Applying the mass-at-1 identity to the four pairs obtained by complementing p and q gives precisely the four character masses in the target.
Complementing or swapping generators preserves freeness.
Independently, the identities
\[
r_-=(\sqrt{\alpha(1-\beta)}-\sqrt{\beta(1-\alpha)})^2,
\qquad
1-r_+=(\sqrt{\alpha\beta}-\sqrt{(1-\alpha)(1-\beta)})^2
\]
verify all endpoint alternatives:

| Trace condition | Generic endpoint and characters |
| --- | --- |
| \(\alpha=\beta\) | \(r_-=0\); both \(e_{10},e_{01}\) vanish |
| \(\alpha>\beta\) or \(\beta>\alpha\) | \(r_->0\); exactly the corresponding one of \(e_{10},e_{01}\) is nonzero |
| \(\alpha+\beta=1\) | \(r_+=1\); both \(e_{11},e_{00}\) vanish |
| \(\alpha+\beta>1\) or \(\alpha+\beta<1\) | \(r_+<1\); exactly the corresponding one of \(e_{11},e_{00}\) is nonzero |
| \(\alpha=\beta=1/2\) | \(K=[0,1]\); all four characters vanish |

When either trace is 0 or 1, faithfulness makes that projection 0 or 1.
The remaining projection generates a finite-dimensional algebra, already equal to A and to its affiliated algebra.
This covers all trace-degenerate cases, including both generators scalar.
The positive proof has no rationality restriction on either trace.

## 5. Character Projections from Bounded Scalar Inverses

If \(e_{10}\ne0\), then \(r_->0\) and \(e_{01}=0\).
The same x as above is now uniformly invertible on the generic support: its adjugate is continuous and bounded on K and its determinant has a positive lower bound.
On the possible character blocks its values are respectively 1 on \(e_{10}\), 1 on \(e_{11}\), and 2 on \(e_{00}\).
Its sole zero character would be \(e_{01}\), which is absent.
This checks invertibility on the entire algebra rather than only on the generic corner.
Also \(1+T\ge1\), so its inverse is bounded globally.

The expression
\[
2(1+T)^{-1}p-px^{-1}p
\]
is 0 on the generic corner and the two other possible characters, and 1 on \(e_{10}\).
It is therefore an actual finite scalar expression for \(e_{10}\) in the original bounded division closure.
No appeal to spectral projections or approximation alone is used to obtain this membership.

For \(e_{01}\), swapping p and q gives exactly its required character, leaves T unchanged, and removes the opposite character.
For \(e_{11}\), the pair \((p,1-q)\) has parameter \(1-T\); its opposite character is the original \(e_{00}\), absent when \(e_{11}\ne0\).
For \(e_{00}\), the pair \((1-p,q)\) has the same transformed parameter and absent opposite character \(e_{11}\).
The requisite gap is \(1-r_+>0\) in both of these cases.
Every substituted pair generates A itself.
These checks give all nonzero characters and then the generic central projection e in \(\operatorname{Div}_{\mathcal M}A\).

## 6. Pole Exclusion and Final Reconstruction

Essential boundedness of the matrix F implies essential boundedness of each entry.
A genuine pole of a rational function has integer order.
At a point of K other than 0 or 1, the positive support density detects its divergence, including one-sided divergence at an endpoint of K.
Thus a and h have no poles on K; c and d have none where \(s\ne0\).

If K touches 0 and c has pole order \(k\ge1\) there, then \(sc\) grows like a nonzero constant times \(t^{1/2-k}\).
A similar expression \((1-t)^{1/2-k}\) applies at 1.
Both diverge.
Every sufficiently small interior interval has positive measure, so the contradiction is to essential boundedness, regardless of whether the density itself vanishes or diverges at the endpoint.
The same argument applies to d.
Possible cancellation has already been accounted for by using reduced rational functions; a removable singularity is not a pole.
This justifies a common polynomial denominator Q with no zero anywhere on K.

In reconstructing f, both n and \(d_0=eQ(T)+(1-e)\) belong to the original bounded division closure because e was just constructed there by scalar inverses.
Compactness gives \(\inf_K|Q|>0\).
The character value of \(d_0\) is 1, even if Q vanishes at a removed endpoint.
Therefore \(d_0^{-1}\) is bounded globally.
Multiplication gives precisely the generic part \(ef=nd_0^{-1}\).
Each remaining component is a complex scalar times its character projection, since its corner in \(W^*(p,q)\) is one-dimensional.
Their finite sum lies in the bounded division closure.

The reverse inclusion follows from the compatibility of a bounded inverse with its affiliated inverse.
This completes both inclusions without replacing scalar division closure by a matrix rational closure.
**Finding: the equality for two freely independent projections passes for every pair of traces.**

## Outcome and Limits

No correction to the mathematical argument is required.
The arbitrary-pair counterexample and the positive free-pair result are compatible: the former attaches a surviving character at a generic support endpoint, while the latter's trace formulas ensure separation whenever that character is present.

The stated specialization to two freely independent two-point normal variables is valid.
For a variable with distinct values \(\lambda_0,\lambda_1\), its spectral projection is \((X-\lambda_0)/(\lambda_1-\lambda_0)\), so the unstarred generated algebra is exactly the projection algebra.
The argument gives no conclusion for three free projections, general finite-spectrum free factors, or arbitrary free-product stability, and makes no claim of novelty.

Verification consisted of complete algebraic and analytic reconstruction of the target, all character substitutions and trace boundary cases, and exact selected primary-source checks.
There was no numerical test, proof-assistant verification, external human review, or audit of the cited papers in full.

## Actual review arrangement

The reviewer did not author or modify either target.
It reopened the two exact primary source interfaces and reconstructed both complete arguments, with no mathematical correction; the original combined-file setting remains part of the finding.
The original account does not establish initial isolation from author-development discussion or prior-review summaries.
Its original day precision, mathematical findings, source depths and explicit limits remain intact; initial context isolation is unknown.
This maintenance performs no new or redated review.

<a id="isolated-two-projection-counterexample"></a>
## New isolated inspection of the arbitrary-pair counterexample

Initial finding formed 2026-10-22T22:30; recorded after comparison 2026-10-22T22:37, in UTC, for human record author Yin.
A separate agent outside substantive development read the complete C_F0099 mathematics and the shared source, closure and generic-matrix setting in [L_F0025, Sections 1–2](../../ledger/Yin_L_F0025_v1.md#1-question-source-reuse-and-accepted-inputs) before old target conclusions, development dialogue or mathematical summaries were supplied.
It completed all six assigned initial findings before consulting their old R accounts or current assessment/review-scope sections.

**PASS for the complete counterexample and its exact affiliated-versus-bounded scalar-closure separation.**
The trace is faithful and normalized, the two matrices are projections, and the zero spectral projection of T isolates the scalar component.
On the generic component the polar part of b gives E12 and the central spectral calculus supplies the entire matrix algebra, so the declared ambient algebra is W*(p,q).
The actual positive x has determinant t(1+t), scalar value one and no kernel.
Its inverse is affiliated and unbounded near zero, while p x inverse p has essential norm two and continuous generic endpoint value two.
Every polynomial in p,q has a diagonal endpoint matrix whose upper-left entry matches its scalar component.
The full-support uniform norm passes that property to C*(p,q).
The constructed bounded f has scalar value one, so it violates the matching property.
Since that unital C*-algebra is inverse closed for bounded inverses existing in M, f is excluded from the bounded scalar division closure.
The alternate e10 formula has the stated values and uses the genuinely unbounded intermediate inverse.
Direct trace arithmetic gives tau(pq)=1/16 versus tau(p)tau(q)=3/16, so freeness is not being refuted.

After the complete initial findings, the whole original R_F0067 was compared.
Its original counterexample, all shared matrix identities, primary-source limits, 2026-09-11 date and unknown context relationship are retained without a new source-opening claim.
No mathematical discrepancy or repair was found.

<a id="isolated-free-projection-equality"></a>
## New isolated inspection of the equality for every free-pair trace

Initial finding formed 2026-10-22T22:30; recorded after comparison 2026-10-22T22:37, in UTC, for human record author Yin.
The same separate isolated arrangement read all C_F0100 mathematics and the shared [L_F0025 interface](../../ledger/Yin_L_F0025_v1.md#1-question-source-reuse-and-accepted-inputs) before old conclusions.
This finding concerns the complete positive proof, separately from the counterexample above.

**PASS for all freely independent projection traces, including irrational, nonuniform and scalar endpoints.**
For interior traces the accepted free-product law supplies a nondegenerate diffuse support interval with positive interior density.
The four character masses and the squared endpoint identities imply that each surviving endpoint character has a positive gap from the generic support and that at a touched endpoint both corresponding characters vanish.
Trace zero or one is scalar by faithfulness and gives a finite-dimensional algebra directly.
For e10 the explicit x is boundedly invertible both on the generic support and on every present character, with the sole zero character e01 absent.
The stated scalar inverse formula consequently reconstructs e10 in the original bounded division closure.
Swapping or complementing the projections reconstructs the other three characters using the same algebra, so e is also available by finite scalar operations.

Compression of every already admissible affiliated expression to the central generic corner preserves its inverses.
The rational weighted 2-by-2 normal form and adjugate formula are therefore valid for the actual scalar division closure.
Bounded diagonal entries exclude reduced rational poles on the full interval support.
For the off-diagonal entries, the factors sqrt(t) or sqrt(1-t) cannot cancel an integer-order pole, so all touched endpoints are also covered.
Positive support measure on every interior neighborhood makes those divergences essential, regardless of endpoint density size.
A common reduced polynomial denominator Q has no zero on the generic compact support.
The patched denominator e Q(T)+(1-e) is boundedly invertible globally and reconstructs ef, even if Q vanishes at a character outside that support.
The remaining character corners are one-dimensional and already scalar-reconstructed.
This proves both inclusions in the original scalar closure, without a matrix-closure or norm-closure substitution.

The entire original positive finding and endpoint table in R_F0067 agree with the initial inspection.
Its shared-source and inverse-domain limits, two-point-normal-variable specialization and exclusions of more general free products remain retained.
No fresh original convolution/Halmos proof, new numerical computation, general free-product theorem, novelty claim or formal verification is asserted.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original finding](#3-arbitrary-pair-counterexample) | unknown |
| [Original finding](#6-pole-exclusion-and-final-reconstruction) | unknown |
| [New isolated arbitrary-pair counterexample](#isolated-two-projection-counterexample) | independently reviewed |
| [New isolated free-pair equality](#isolated-free-projection-equality) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original finding](#3-arbitrary-pair-counterexample) | [C_F0099 statement](../../claims/Yin_C_F0099_v1.md#statement) | Complete arbitrary-two-projection counterexample, actual affiliated inverse and C*-endpoint exclusion, with the original shared matrix setting. |
| [Original finding](#3-arbitrary-pair-counterexample) | [C_F0099 argument](../../claims/Yin_C_F0099_v1.md#32-exclusion-from-the-bounded-division-closure) | Complete arbitrary-two-projection counterexample, actual affiliated inverse and C*-endpoint exclusion, with the original shared matrix setting. |
| [Original finding](#6-pole-exclusion-and-final-reconstruction) | [C_F0100 statement](../../claims/Yin_C_F0100_v1.md#statement) | Complete two-free-projection proof for all traces, including central character extraction, all endpoint cases, rational induction, pole exclusion and original scalar reconstruction. |
| [Original finding](#6-pole-exclusion-and-final-reconstruction) | [C_F0100 argument](../../claims/Yin_C_F0100_v1.md#42-constructing-the-endpoint-projections-with-bounded-inverses) | Complete two-free-projection proof for all traces, including central character extraction, all endpoint cases, rational induction, pole exclusion and original scalar reconstruction. |
| [New isolated arbitrary-pair counterexample](#isolated-two-projection-counterexample) | [Exact C_F0099 statement](../../claims/Yin_C_F0099_v1.md#statement) | Complete explicit finite tracial two-projection counterexample, actual affiliated inverse, endpoint matching exclusion, strict scalar closure separation and nonfreeness. |
| [New isolated arbitrary-pair counterexample](#isolated-two-projection-counterexample) | [Exact selected C_F0099 argument](../../claims/Yin_C_F0099_v1.md#32-exclusion-from-the-bounded-division-closure) | All of Sections 3.1–3.2 together with the actual shared generic matrix and closure setting; bounded output does not make the intermediate inverse bounded. |
| [New isolated free-pair equality](#isolated-free-projection-equality) | [Exact C_F0100 statement](../../claims/Yin_C_F0100_v1.md#statement) | Whole two-free-projection equality for arbitrary traces, all endpoint/atomic/scalar cases, original scalar division closures. |
| [New isolated free-pair equality](#isolated-free-projection-equality) | [Exact selected C_F0100 argument](../../claims/Yin_C_F0100_v1.md#42-constructing-the-endpoint-projections-with-bounded-inverses) | Complete Sections 4.1–4.4 and shared rational induction, source interval/character interface, explicit bounded scalar character extraction, half-order pole check and globally patched reconstruction. |

---
author: Yin
---

# Absolute-phase realification with zero vacuum can have an unbounded contraction

## Current assessment
[Selected decision](#decision-finding-owned-applicability)

## Absolute-phase realification does not imply the contraction estimate

<a id="statement"></a>

Kind: Claim/proof module.
Date: 2026-09-16.
Human record author: Yin.
A Codex research agent developed the proof, which the reviewing agent separately reviewed.
Consumer: the separate normal-domain investigation, Q3.
The [selected assessment](#decision-finding-owned-applicability) records the mathematical and review assessments.
The result refutes a proposed estimate for the transformed derivation, not the original Task.

<a id="normal-phase-realification-obstruction"></a>
## 1. Exact target and bounded outcome

For a compactly supported nonatomic probability mu on C, let

\[
\partial_0p(z,w)=\frac{p(z)-p(w)}{z-w},\qquad
E_0p(z)=\int\partial_0p(z,w)\,d\mu(w),
\]

on represented starred polynomials.
The target remains whether the actual hypothesis

\[
1\in\operatorname{Dom}E_0^*,\qquad \xi=E_0^*1\in L^2(\mu)
\]

alone forces an infinity-to-L2 bound for E_0.
No answer to this target is obtained here.

The concrete test below shows why one apparently natural phase conversion does not supply that answer.
Multiplying the canonical coarse derivation by an absolute-value phase does produce a real closable derivation, and its actual vacuum adjoint can even be computed.
Nevertheless its vacuum contraction can fail the desired bound, already on the Haar circle where the *original* E_0 is bounded on L2.
Thus tensor-unitary phase multiplication, reality, and an actual L2 vacuum together do not justify importing the Dab10 contraction estimate.
The missing coassociativity or controlled-defect input is substantive.

## 2. Reuse and source boundary

Before developing the test, the following existing records were read:

- [Dab10-U002](../audits/literature/Dab10/Yin_U002.md#dab10-u002), including its proof reconstruction and stated reality/coassociativity/functional-calculus scope;
- [C_F0043 Sections 3.1--3.2](Yin_C_F0043_v1.md), which explicitly computes and controls the nonzero coassociativity defect for its particular unitary reweighting;
- [C_F0025](Yin_C_F0025_v1.md), the normal phase and represented-core conventions;
- [C_F0047](Yin_C_F0047_v1.md), including its same-circle Fourier calculation;
- [Yin_S_F0011](../strategies/Yin_S_F0011.md) and the scalar Cauchy boundary of [C_F0044](Yin_C_F0044_v1.md).

These records already verify that Dab10's selected estimate is not a general theorem about every real derivation with a vacuum adjoint.
C_F0043 succeeds by supplying a particular bounded first-order defect; that accepted positive argument is unchanged.
The calculation below uses elementary measure symmetry and a directly computed trigonometric integral.
It imports no additional external theorem or claim about novelty.
No new external search is needed for those elementary calculations; the precise Dab10 source interface is reused at its recorded scope.

## 3. The absolute-phase derivation really is real and has an actual vacuum

Write `H=L2(mu)` and `K=L2(mu tensor mu)`, with the outer bimodule actions

\[
(a\cdot F\cdot b)(z,w)=a(z)F(z,w)b(w)
\]

and antiunitary involution `F^dagger(z,w)=overline(F(w,z))`.
On the null diagonal choose arbitrary kernel values.
Off it set

\[
u(z,w)=i\frac{z-w}{|z-w|},\qquad
\delta_0p=u\partial_0p
=i\frac{p(z)-p(w)}{|z-w|}.
\tag{P1}
\]

Multiplication by u is unitary on K.
Every polynomial difference quotient in (P1) is bounded, since a starred polynomial is Lipschitz on a compact square containing the support.
If p represents zero in H, then its difference vanishes for almost every pair, so delta_0 is well-defined on represented polynomials.

The derivation rule follows by expanding

\[
p(z)q(z)-p(w)q(w)
=p(z)(q(z)-q(w))+(p(z)-p(w))q(w).
\]

The factor i is essential to the reality convention:

\[
(\delta_0p)^\dagger(z,w)
=\overline{i\frac{p(w)-p(z)}{|z-w|}}
=i\frac{\overline{p(z)}-\overline{p(w)}}{|z-w|}
=\delta_0(p^*)(z,w).
\tag{P2}
\]

The operator delta_0 is closable.
If `p_n->0` in H and `delta_0 p_n->F` in K, then multiplication by the bounded function `|z-w|` gives

\[
|z-w|F
=\lim_n i(p_n(z)-p_n(w))=0
\quad\text{in }K.
\]

The difference map from H to K is bounded, and `|z-w|>0` almost everywhere by atomlessness.
Hence F=0.
This proves closability of the original polynomial operator, rather than merely proposing an extension.

There is also an actual vacuum adjoint, independently of the original canonical vacuum hypothesis.
Symmetry of the measure and antisymmetry of the numerator yield

\[
\langle1\otimes1,\delta_0p\rangle_K
=i\iint\frac{p(z)-p(w)}{|z-w|}\,d\mu(z)d\mu(w)=0.
\tag{P3}
\]

The bounded polynomial kernel justifies the swap.
Thus

\[
1\otimes1\in\operatorname{Dom}\delta_0^*,\qquad
\delta_0^*(1\otimes1)=0.
\tag{P4}
\]

This conclusion is not inferred by silently moving a nonpolynomial phase through the original adjoint.
In general the formal expression `partial_0* (overline(u))` would require a separate domain argument.
Here (P3) proves precisely that domain statement directly.
Existence of a new actual vacuum is therefore not the obstruction in this particular phase conversion.

## 4. Exact Haar-circle failure of the transformed contraction estimate

Let mu be normalized Haar measure on the unit circle.
Its represented starred polynomial algebra is the Laurent polynomial algebra.
Let

\[
T_0=(\mathrm{id}\otimes\tau)\delta_0.
\]

For `z` on the circle, substitute `w=z e^{i\theta}` into (P1).
For every integer n,

\[
T_0(z^n)
=i z^n\frac1{2\pi}\int_0^{2\pi}
\frac{1-e^{in\theta}}{|1-e^{i\theta}|}\,d\theta
=i\lambda_{|n|}z^n,
\tag{P5}
\]

where lambda_0=0 and

\[
\lambda_n=\frac1{4\pi}\int_0^{2\pi}
\frac{1-\cos(n\theta)}{\sin(\theta/2)}\,d\theta
\quad(n\ge1).
\tag{P6}
\]

The imaginary part of the integral vanishes under `theta->2pi-theta`; all these fixed-n integrals are finite.
Subtracting consecutive values gives

\[
\begin{aligned}
\lambda_{n+1}-\lambda_n
&=\frac1{4\pi}\int_0^{2\pi}
\frac{\cos(n\theta)-\cos((n+1)\theta)}{\sin(\theta/2)}\,d\theta\\
&=\frac1{2\pi}\int_0^{2\pi}\sin((n+1/2)\theta)\,d\theta
=\frac{2}{\pi(2n+1)}.
\end{aligned}
\tag{P7}
\]

Consequently

\[
\boxed{\quad
\lambda_n=\frac2\pi\sum_{k=0}^{n-1}\frac1{2k+1}
\ge\frac1\pi\sum_{k=1}^n\frac1k
\ge\frac1\pi\log(n+1)\longrightarrow\infty.
\quad}
\tag{P8}
\]

Since `||z^n||_infinity=||z^n||_2=1`, equations (P5)--(P8) disprove any infinity-to-L2 bound for T_0 on its original Laurent polynomial core.
There is no hidden domain failure in this example: (P5) diagonalizes T_0 on a complete orthonormal Fourier basis, so it is closable, with the closure of the indicated diagonal multiplication operator.
Its actual vacuum adjoint is zero, consistently with (P4).

By contrast, the original canonical contraction on the same measure satisfies, by the elementary Laurent calculation also recorded in C_F0047,

\[
E_0(z^n)=z^{n-1}\quad(n\ge1),\qquad
E_0(z^n)=0\quad(n\le0).
\tag{P9}
\]

It therefore has a bounded L2 extension of norm one and actual vacuum vector `E_0*1=z`.
In particular this model satisfies the original vacuum premise and original desired conclusion.
It is an obstruction only to the suggested *transformed* estimate and to transferring boundedness of contractions from the unitary tensor multiplier; it does not refute the normal-domain investigation.

## 5. What fails in the coassociativity step

The source Dab10 estimate uses more than reality and a vacuum adjoint.
C_F0043's particular unitary conversion compensates for a computed first-order defect.
The absolute phase (P1) has neither coassociativity nor an established defect bound of that form.

For clarity, a purely pointwise computation away from all three collision diagonals can be made.
If a scalar difference rule has kernel k,

\[
\delta p(z,w)=k(z,w)(p(z)-p(w)),
\]

then applying that same difference rule in the first and second tensor variables gives the formal difference

\[
\bigl[k(z,v)(k(z,w)+k(w,v))-k(z,w)k(w,v)\bigr](p(z)-p(v)).
\tag{P10}
\]

For the canonical kernel `k(z,w)=1/(z-w)`, the bracket vanishes by the elementary partial-fraction identity.
That pointwise identity alone does not assert that both iterated Hilbert-space derivations are defined on the entire original normal core.

For (P1), put `a=|z-w|`, `b=|w-v|`, `c=|z-v|`.
The bracket becomes

\[
-\frac{a+b-c}{abc}.
\tag{P11}
\]

It is generally nonzero and contains inverse small distances.
This is an off-diagonal pointwise diagnosis, not a claim that either iterated derivative belongs to the triple Hilbert tensor domain.
In the Haar example, the contraction is diagonal with arbitrarily large lambda_n, so a proposed Dab10-style bounded first-order control sufficient to bound that contraction cannot be inferred from (P4).
No uncontrolled triple-domain or truncation limit is used to prove the counterexample itself; the exact one-variable integral (P5) already proves it.

## 6. Continuation boundary

This bounded test eliminates the inference

`unitary phase makes the derivation real + actual vacuum exists -> Dab10 contraction bound`

for arbitrary phase multipliers.
It does not eliminate other specially structured phase conversions, such as the already accepted unitary one in C_F0043, or an argument working directly with the original canonical operator.

For a direct Cotlar/symmetrization route, the original normal image `E_0p` need not lie in the polynomial core, and pointwise coassociativity of its scalar kernel does not by itself license an `E_0^2p` or iterated-coarse-derivation calculation.
The previously recorded distributional vacuum identity still does not supply a uniform norm estimate for Cauchy truncations.
No new bridge over either domain issue is proved here, and no geometric G assumption is silently introduced.

The next concrete obligation would be to identify and control a legitimate defect for a different phase, together with its actual vacuum-adjoint and iterated-domain statements, or to justify a direct canonical norm identity without those unproved limits.
The present record preserves an exact failed mechanism and its model, not a solution of the arbitrary-measure vacuum implication.
No numerical experiment, proof-assistant verification, external human review or unrestricted Task conclusion is claimed.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-16T14:05 |
| status | open |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#normal-phase-realification-obstruction) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: A real closable phase-modified coarse derivation has actual zero vacuum adjoint, but its Haar-circle contraction has logarithmically divergent Fourier eigenvalues; the original canonical contraction remains bounded.

### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-16T14:10 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#normal-phase-realification-obstruction) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0029_v1.md) | Complete P1-P9 obstruction and explicitly formal-only P10-P11 diagnosis; original canonical model remains bounded, no Task refutation. |

Recorded mathematical summary: A real closable phase-modified coarse derivation has actual zero vacuum adjoint, but its Haar-circle contraction has logarithmically divergent Fourier eigenvalues; the original canonical contraction remains bounded.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

### Decision candidate-0003

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-19T13:54 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#normal-phase-realification-obstruction) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0055_v1.md#c-f0092-applicability) | Yin_C_F0054 (recorded assessment 2): current-rule execution-path and exact review-evidence correspondence; retain the original complete independent mathematical review at its unchanged scope. No new whole-proof independent review, proof change, dependency change or Task completion. |

Recorded mathematical summary: A real closable phase-modified coarse derivation has actual zero vacuum adjoint, but its Haar-circle contraction has logarithmically divergent Fourier eigenvalues; the original canonical contraction remains bounded.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-applicability

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:13 |
| status | proved |
| reason | Select the same actual applicability finding at its responsible R home, with its original date, exact per-Claim scope and known shared mathematical context, preserving statement, argument, dependencies and mathematical assessment. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#normal-phase-realification-obstruction) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Retained applicability finding](../audits/reviews/Yin_R_F0055_v1.md#c-f0092-applicability) | The original 2026-09-19T13:52 per-Claim review applicability, exact fixed inputs and unchanged mathematical scope; self-reviewed and no new whole-proof or independent review. |

## Recorded review scopes

Complete P1-P9 obstruction and explicitly formal-only P10-P11 diagnosis; original canonical model remains bounded, no Task refutation.

Review: [Exact material](../audits/reviews/Yin_R_F0029_v1.md).

Material covered by that review: [Exact material](Yin_C_F0054_v1.md).

Yin_C_F0054 (recorded assessment 2): current-rule execution-path and exact review-evidence correspondence; retain the original complete independent mathematical review at its unchanged scope.
No new whole-proof independent review, proof change, dependency change or Task completion.

Review: [Exact material](../audits/reviews/Yin_R_F0055_v1.md#c-f0092-applicability).

Material covered by that review: [Exact material](Yin_C_F0054_v1.md).

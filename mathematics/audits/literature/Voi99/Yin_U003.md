---
author: Yin
---
# Liberation gradients, adjoints and separation estimates

Inspected edition: [Yin's source notes](readme.md#yin-edition).

## Voi99-U003

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Published edition of Voi99. |
| source-locator | Sections 5–7, printed pp.114–128, PDF pp.14–28. |
| inspection | 2026-10-18, authoring agent for Yin. All statements and proofs in this range were read. Word expansions, conditional-expectation transfers, the freeness induction, weak limits, adjoint signs and the separation estimate were checked. Printed pp.115, 117 and 126–127 were also inspected as images. Corrections and the remainder issue, unresolved at that inspection, are distinguished below. |

The targeted remainder check below directly reinspected Definitions 5.3–5.5, Proposition 5.6 and Corollary 5.7, printed pp. 115–118, on 2026-11-02, including the displayed corollary on printed p. 117 as an image.
Those spectral-calculus checks are ordinary source verification by the repairing agent for Yin.
The counterexample development additionally read published Sections 12.1–12.7, printed pp.155–159; its complete local deduction and subsequent independent whole-proof review are linked at the remainder interface below.
That review concerns the exact counterexample, without expanding the original Sections 5–7 inspection or independently reviewing this whole source unit.

<a id="liberation-derivation-and-gradient"></a>
## Complete definitions and signs

Let \(A,B\) be unital \(*\)-subalgebras of a tracial \(W^*\)-probability space \((M,\tau)\), and let \(P=\operatorname{Alg}(A,B)\).
Section 5.3 assumes algebraic freeness and defines the outer-bimodule derivation
\[
 \delta_{A:B}:P\longrightarrow P\otimes_{\mathbb C}P,\qquad
 \delta_{A:B}(a)=a\otimes1-1\otimes a,\qquad
 \delta_{A:B}(b)=0.
\]
Its word formula is
\[
 \delta_{A:B}(a_1b_1\cdots a_nb_n)
 =\sum_{k=1}^n
 \left(a_1b_1\cdots a_k\otimes b_k\cdots a_nb_n
       -a_1b_1\cdots b_{k-1}\otimes a_kb_k\cdots a_nb_n\right).
\]
An actual derivation on the represented algebra requires well-definedness; a formal free-product word calculation alone does not supply it when algebraic relations are allowed.

Definition 5.4 defines the liberation gradient \(j(A:B)\), when it exists, as the unique vector in \(L^1(W^*(A,B),\tau)\) satisfying
\[
 \tau(j(A:B)m)=(\tau\otimes\tau)(\delta_{A:B}m)
 \quad(m\in P).
\]
The printed right side in Definition 5.4 has \(\delta_{A:B}\xi\) instead of \(\delta_{A:B}m\).
The subsequent word formula and Proposition 6.1 fix the intended variable.
If the gradient is formulated through moments without an algebraic-freeness premise, use this word identity and separately justify any actual derivation operator.

The source proves
\[
 j(A:B)^*=-j(A:B),\qquad j(B:A)=-j(A:B),
 \qquad j(A:\mathbb C)=0.
\]
Kaplansky approximation extends the moment identity from \(A,B\) to their von Neumann closures, preserving \(j\).
For \(j\in L^2\), Proposition 6.1 explicitly gives
\[
 \delta_{A:B}^*(1\otimes1)=-j(A:B).
\]
This minus sign follows from the trace-pairing definition and skewadjointness.
With \((u\otimes v)^\dagger=v^*\otimes u^*\), the derivation is anti-real:
\[
 \delta(p^*)=-(\delta p)^\dagger.
\]
Consequently \(\mathrm i\delta\) is real.
Neither the gradient nor its adjoint-vacuum representative may be identified without this sign conversion.

## Results and checked mechanisms

| Passage | Mathematical content and checked mechanism |
| --- | --- |
| 5.5 | Uniqueness follows from the trace pairing; restriction to smaller algebras is conditional expectation. The word formula extends to von Neumann closures by bounded Kaplansky approximation against the \(L^1\) vector. Taking adjoints of the word identity gives skewadjointness. |
| 5.6 | The order-\(\varepsilon\) liberation variation is the displayed cyclic sum of \(\delta\)-pairings. Expansion by Proposition 1.4 gives the same diagonal terms and two copies of the off-diagonal terms after exchanging indices. |
| 5.7 | The first displayed equality substitutes the gradient moment identity into 5.6 and is justified. The final L1-only quadratic exponential comparison fails for the actual-gradient counterexample in [C_F0184](../../../claims/Yin_C_F0184_v1.md#statement), with its independently reviewed argument. The valid interfaces below give \(o(\varepsilon)\) under the stated L1 hypothesis and a quadratic comparison under the sufficient extra hypothesis \(j\in L^2\). |
| 5.8–5.9 | Summing the coordinate derivations gives the derivation for the generated algebra; the total derivation relative to scalars has zero trace pairing. This gives the sum and antisymmetry identities whenever the participating gradients exist. |
| 5.10–5.12 | For selfadjoint \(X\) with conjugate variable \(\mathcal J(X:B)\), \(j(\mathbb C[X]:B)=[\mathcal J(X:B),X]\). The two difference-quotient expansions cancel their outside terms. Summing gives the multivariable formula and the zero total commutator identity. The statements use selfadjoint generators; no normal-tuple extension is asserted by this source alone. |
| 5.13–5.16 | Under amalgamated freeness, adding constants leaves the gradient unchanged; for a freely Markovian triple, \(j(A:C)=E_{W^*(A,C)}j(A:B)\). The proof uses the reduced centered-word decomposition in 5.14: after applying the derivation, at least one tensor factor has zero trace. |
| 5.17 | \(j(A:B)=0\) is equivalent to scalar freeness. The reverse direction is proved by induction on centered alternating words; all shorter split-word terms vanish, leaving the full mixed moment. |
| 5.18 | Finite equality of the relevant free Fisher informations forces equality in a conditional-expectation norm inequality, hence equality of conjugate vectors. The gradient is then both in one generated \(L^2\) algebra and orthogonal to it, so 5.17 gives freeness. Finiteness is needed. |
| 5.19–5.20 | Uniform \(L^2\) bounds and strong convergence of the conditional projections give weak convergence of projected gradients by the word identity. For increasing algebras, the gradients are an \(L^2\)-bounded martingale; orthogonality of increments gives \(L^2\) convergence. |
| 6.1–6.3 | The vacuum-adjoint criterion includes the minus sign above. The Leibniz identity propagates the adjoint domain to algebraic tensors and proves closability. One printed coefficient in 6.2 needs correction. |
| 6.4 | The printed tensor-adjoint formula has the wrong correction sign for this anti-real derivation; see the direct check below. |
| 7.1–7.6 | The centered identity \(\tau(j[a,b])=-2\tau(ab)\) gives an angle bound when \(j\) is bounded. The subsequent conditional-projection and semicircular-perturbation consequences follow from this bound and the source's conjugate-variable identities. |

The separation bound in Proposition 7.2 is
\[
 |\tau(ab)|\le
 \frac{\|j(A:B)\|}{\sqrt{1+\|j(A:B)\|^2}}\|a\|_2\|b\|_2
 \quad(a\in A\cap\ker\tau,\ b\in B\cap\ker\tau).
\]
The displayed proof first needs the reduction to selfadjoint \(a,b\), since it uses \(\tau(x^2)=\|x\|_2^2\).
This reduction is justified by treating the centered selfadjoint \(L^2\) spaces as real Hilbert spaces: their conditional projections complexify isometrically, so the norm of the product of the two projections is unchanged by complexification.
For selfadjoint unit vectors, set \(x=(a+b)/2\), \(y=(a-b)/2\), use \(\tau(ab)=\cos\theta\), and estimate \(\|[a,b]\|_1\le2\sin\theta\).
The \(\|j\|=0\) case follows directly from 7.1 and need not divide by zero.

<a id="adjoint-formula-corrections"></a>
## Checked adjoint corrections

For \(\eta\in\operatorname{Dom}\delta^*\) and \(y\in P\), the first formula in Proposition 6.2 must read
\[
 \delta^*(\eta(1\otimes y))
 =(\delta^*\eta)y-(\mathrm{id}\otimes\tau)
       \bigl(\eta(\delta(y^*))^*\bigr).
\]
The printed factor immediately before \((\delta(y^*))^*\) is \(y\), whereas linearity in \(\eta\) requires \(\eta\).
The second formula, with \((\tau\otimes\mathrm{id})((\delta(y^*))^*\eta)\), gives the corresponding left multiplication rule.

Put \(\zeta=\delta^*(1\otimes1)=-j(A:B)\).
Anti-reality and the two rules give, for \(a,b\in P\),
\[
 \delta^*(a\otimes b)
 =a\zeta b+(\mathrm{id}\otimes\tau)(\delta a)b
              +a(\tau\otimes\mathrm{id})(\delta b).
\]
Thus Proposition 6.4 requires a plus sign before its two derivative correction terms, rather than the printed minus sign.

A direct test removes any convention ambiguity.
Take \(B=\mathbb C1\), \(A=M\), and a nonzero centered selfadjoint \(a\in M\).
Then \(\delta x=x\otimes1-1\otimes x\), \(j=0\), and direct Hilbert-space adjunction gives
\[
 \delta^*(a\otimes1)=a.
\]
The printed 6.4 formula gives \(-a\).
The corrected formula gives \(a\).
Also, if \(T\) is merely affiliated, the source's \(m_T(a\otimes b)=aTb\) is affiliated-valued; its printed codomain \(M\) is not justified unless those products are bounded.

<a id="exponential-remainder-limit"></a>
## Failure of the L1-only quadratic exponential comparison in Corollary 5.7

The published Corollary 5.7, printed pp. 117–118, assumes the setting of Proposition 5.6 and existence of the gradient as defined in 5.4, hence only \(j:=j(A:B)\in L^1(N,\tau)\), where \(N=W^*(A,B)\).
Here \((M,\tau)\) is a tracial \(W^*\)-probability space, \(A,B\) are unital \(*\)-subalgebras, and the unitary free Brownian motion \(U(t)\) is free from their jointly generated algebra.
For fixed \(n\geq1\), \(a_k\in A\) and \(b_k\in B\), put
\[
 \begin{aligned}
 \Lambda(t)&=\tau\bigl(U(t)a_1U(t)^*b_1\cdots U(t)a_nU(t)^*b_n\bigr),\\
 u_t&=\exp(tj/2),\qquad
 F(t)=\tau\bigl(u_ta_1u_t^*b_1\cdots u_ta_nu_t^*b_n\bigr),\\
 D&=\frac12\sum_{k=1}^n
 \tau\bigl(a_1b_1\cdots a_{k-1}b_{k-1}[j,a_k]b_k\cdots a_nb_n\bigr).
 \end{aligned}
\]
An empty prefix or suffix in this expression is the identity.
Skewadjointness of the affiliated \(j\) makes \(u_t\) a bounded unitary, and each commutator in \(D\) belongs to \(L^1(N,\tau)\).
Proposition 5.6 and the gradient word identity prove the first displayed equality of 5.7 in the precise form
\[
 \Lambda(t)=F(0)+tD+O(t^2)\qquad(t\downarrow0).
\]
The corollary also prints \(\Lambda(t)=F(t)+O(t^2)\).
Its proof on p. 118 only invokes the combination of 5.6 and the definition of \(j\); neither supplies the required quadratic remainder for \(F\).
The original inspection retained this as a proof-sufficiency doubt without a specialized counterexample.
The independently reviewed actual-gradient construction below now disproves that printed quadratic comparison under its original L1-only hypothesis.

### What the stated L1 hypothesis does justify

Spectral calculus and dominated convergence give
\[
 \left\|\frac{u_t-1}{t}-\frac j2\right\|_1\longrightarrow0,
 \qquad
 \left\|\frac{u_t^*-1}{t}+\frac j2\right\|_1\longrightarrow0.
\]
Indeed, for \(j=\mathrm iH\) with \(H=H^*\), the scalar remainder divided by \(|t|\) converges pointwise to zero and is bounded by \(|H|\).
Left and right multiplication by this unitary group are continuous on \(L^1\), as follows by approximation with \(L^2\) elements and uniform boundedness.
Telescoping the finite product defining \(F\) therefore gives its derivative at zero by inserting \(j/2\) at each \(u_t\) and \(-j/2\) at each \(u_t^*\).
Combining the two insertions adjacent to each \(a_k\) gives exactly \(D\).
Consequently the supported exponential interface under the source's stated hypothesis is
\[
 F(t)=F(0)+tD+o(t),\qquad
 \Lambda(t)=F(t)+o(t)\qquad(t\downarrow0).
\]
This calculation uses the actual gradient moment identity to identify the same coefficient \(D\) in the Brownian and exponential moments; a generic generator estimate alone would not identify that coefficient.

### A sufficient extra hypothesis for the quadratic interface

If the actual gradient additionally belongs to \(L^2(N,\tau)\), the printed quadratic comparison follows.
Here is a direct check, with \(K=\prod_{k=1}^n\|a_k\|\|b_k\|\).
Let \(j_R=j1_{\{|j|\leq R\}}\), and define \(F_R\) by replacing \(j\) with this bounded skewadjoint spectral truncation.
The product has \(2n\) exponential factors.
Twice differentiating gives \((2n)^2\) terms, each with coefficient of absolute value \(1/4\), containing either one \(j_R^2\) or two \(j_R\)'s.
All other exponential factors are unitary.
The trace inequality for one \(L^1\) factor, or noncommutative Hölder for two \(L^2\) factors, bounds every such term by \(K\|j_R\|_2^2/4\).
Thus, for real \(t\),
\[
 |F_R''(t)|\leq n^2K\|j_R\|_2^2,
 \qquad
 |F_R(t)-F_R(0)-tF_R'(0)|
 \leq\frac{n^2K}{2}\|j_R\|_2^2t^2.
\]
Spectral dominated convergence gives \(e^{tj_R/2}\to u_t\) in \(L^2\), so the bounded finite products converge in trace.
Also \(j_R\to j\) in \(L^2\) and hence in \(L^1\), giving \(F_R'(0)\to D\).
Passing to the limit proves
\[
 |F(t)-F(0)-tD|\leq\frac{n^2K}{2}\|j\|_2^2t^2.
\]
Combining this with the supported linearized equality for \(\Lambda\) proves \(\Lambda(t)=F(t)+O(t^2)\) under this additional hypothesis.
Square integrability is sufficient here; this check does not claim it is necessary.

### Confirmed failure and consumer boundary

[C_F0184](../../../claims/Yin_C_F0184_v1.md#statement) gives algebraically free projection algebras in \(M_2(L^\infty(\mu))\), with \(d\mu(x)=c(x-1/2)^{-2/5}1_{(1/2,3/4)}(x)\,dx\) and \(c\) the probability normalization.
Its symmetric-cutoff and whole-word calculations prove existence of the actual gradient \(j(A:B)=-[p,q]g\in L^1\setminus L^2\), where \(g(x)=\operatorname{pv}\int(x-y)^{-1}d\mu(y)\).
The source's Proposition 12.7 assumes an L3 density and is not applied to this singular density; the required L1-gradient extension is proved directly in the fixed Claim.
For the fixed word \(a_1=p,b_1=q\) and the original exponential normalization \(e^{tj/2}\), that argument gives positive constants \(c_0,C_0\) such that
\[
 F(t)-\Lambda(t)\geq c_0t^{3/2}-C_0t^2
 \qquad(t\downarrow0).
\]
Thus \(\Lambda(t)-F(t)\) is not \(O(t^2)\), even though the actual L1 gradient exists and the two moments have the same supported linear coefficient.
This is a failure of the original specialized quadratic assertion, not an inference from a generic L1 generator estimate.

The [independent whole-proof finding](../../reviews/Yin_R_F0186_v1.md#whole-candidate-finding), review act 2026-11-02T05:09 UTC, covers C_F0184's exact statement, complete argument and source interfaces and found no mathematical gap.
The [proved decision](../../../claims/Yin_C_F0184_v1.md#decision-reviewed-adoption) adopts that result.
The review directly checked the published hypotheses and two-projection passages; free Brownian existence, its stated mean and the free tracial extension remain accepted external inputs without re-auditing their original constructions.
It does not independently re-review all of Sections 5–7 or the project proofs cited below.
The L1 \(o(t)\) interface remains valid and is compatible with the fractional-order obstruction; the sufficient L2 quadratic interface also remains valid and does not apply to this non-L2 example.
Quadratic reliance therefore requires adequate additional hypotheses, such as the proved L2 sufficient condition above, rather than the false L1-only printed comparison.
The later rigorous information inequalities inspected here use moment identities and conditional expectations, rather than that exponential remainder.
The retained [C_F0082 argument](../../../claims/Yin_C_F0082_v1.md#represented-derivations-and-actual-vacuum-adjoints) and [C_F0083 v2 conventions](../../../claims/Yin_C_F0083_v2.md#definitions-and-conventions) likewise use the word moments, skewadjointness and signed actual \(L^2\) vacuum from Sections 5.3–5.4 and Proposition 6.1.
Their selected source inputs do not invoke the exponential comparison, so its failure does not change those inputs or their recorded review scope.

## External inputs and outcome

The source's accepted external inputs include standard conditional expectations and Kaplansky density, the Part V conjugate-variable rules, and the small-time expansion recorded in [Voi99-U002](Yin_U002.md#voi99-u002).
The local adjoint checks above do not rely on blindly importing the real-derivation formula from Part V.
This unit records an audit with the stated corrections and confirmed failure of the L1-only quadratic exponential comparison, rather than an unqualified verification of every printed formula.

---
author: Yin
---
# Liberation gradients, adjoints and separation estimates

## Voi99-U003

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Published edition of Voi99, registered local PDF (private lookup: `../../../literature/registry.md#voi99-source-artifact`). |
| source-locator | Sections 5–7, printed pp.114–128, PDF pp.14–28. |
| inspection | 2026-10-18, authoring agent for Yin. All statements and proofs in this range were read. Word expansions, conditional-expectation transfers, the freeness induction, weak limits, adjoint signs and the separation estimate were checked. Printed pp.115, 117 and 126–127 were also inspected as images. Corrections and one unresolved remainder estimate are distinguished below. |

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
| 5.7 | The first displayed equality substitutes the gradient moment identity into 5.6 and is justified. The final exponential expression has the additional remainder issue recorded below. |
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
## Unresolved exponential remainder in Corollary 5.7

The source assumes only existence of \(j(A:B)\in L^1\), then writes the liberated moment as a moment of conjugations by \(\exp(\varepsilon j/2)\) with error \(O(\varepsilon^2)\).
Skewadjointness makes these exponentials unitary, and \(L^1\) integrability gives the first derivative paired against bounded words.
It does not by itself supply a quadratic Taylor remainder.
For example, the generic bound obtained from spectral calculus with only an \(L^1\) generator is \(o(\varepsilon)\), whereas an \(L^2\) generator gives quadratic control in the relevant trace estimates.
No additional argument establishing the printed \(O(\varepsilon^2)\) estimate under the stated \(L^1\)-only hypothesis was found in the paper.
The first, linearized equality remains supported by 5.6; the final exponential remainder is not certified by this review.
This is a proof-sufficiency issue, not a claimed counterexample to the source's specialized assertion.
The later rigorous information inequalities inspected here use moment identities and conditional expectations, rather than that exponential remainder.

## External inputs and outcome

The source's accepted external inputs include standard conditional expectations and Kaplansky density, the Part V conjugate-variable rules, and the small-time expansion recorded in [Voi99-U002](Yin_U002_v1.md#voi99-u002).
The local adjoint checks above do not rely on blindly importing the real-derivation formula from Part V.
This unit records an audit with the stated corrections and unresolved remainder, rather than an unqualified verification of every printed formula.

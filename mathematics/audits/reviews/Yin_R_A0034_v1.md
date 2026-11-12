---
author: Yin
---
# Independent review of the diagonal tensor tests

## Review arrangement and inputs

Review time: 2026-11-11T18:16.
The human record author is Yin.
A separately organized agent outside substantive development performed an initial whole-artifact mathematical review of [Yin_L_A0027_v1](../../ledger/Yin_L_A0027_v1.md), the fixed uncommitted working-copy input inspected at this review time.
The reviewer received the fixed input path, review assignment and administrative startup facts, without inherited proof-development dialogue or mathematical summaries.
No development draft, author explanation or previous review finding for this candidate was consulted.
No substantive repair was supplied, and the candidate was not edited.
The review reconstructs the displayed reasoning and checks its actual prerequisite interfaces rather than relying on another review verdict.

The inspected prerequisite scopes are [the cyclic regular representation](../../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions), [the finite-trace polar-decomposition and affiliated-invertibility interface](../literature/MSY23/Yin_U004.md#lemmas-51-55-finite-trace-invertibility-and-stable-finiteness), and [the coefficient-angle statement](../../claims/Yin_C_A0009_v2.md#statement) with its [bounded compression argument](../../claims/Yin_C_A0009_v2.md#argument).
The [pairwise-Haar model](../../ledger/Yin_L_A0025_v1.md) was read as the exact comparison input, including its explicit forbidden joint-word trace.
Prerequisite materials contain their own recorded assessment or review metadata, but no candidate review was supplied and no prerequisite verdict substitutes for the interface checks below.
The unrelated applications and source dependencies of those prerequisite materials are outside this review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-artifact finding](#whole-artifact-finding) | [Complete fixed ledger](../../ledger/Yin_L_A0027_v1.md) | Whole argument, hypotheses, equations (1)--(28), actual regular-group and trace interfaces, examples, comparisons and stated limitations. |
| [Whole-artifact finding](#whole-artifact-finding) | [Actual setting](../../ledger/Yin_L_A0027_v1.md#actual-setting-and-reused-interfaces) | Torsion-free hypothesis, coincident-label cases, norm bounds, original one-copy estimate and actual prerequisite applicability. |
| [Whole-artifact finding](#whole-artifact-finding) | [Diagonal identity](../../ledger/Yin_L_A0027_v1.md#the-diagonal-map-and-the-exact-tensor-identity) | Normal trace-preserving embedding, spectral projection, bounded tensor identity, abelian injectivity and intersection/rank conclusions. |
| [Whole-artifact finding](#whole-artifact-finding) | [Even powers](../../ledger/Yin_L_A0027_v1.md#uniform-accretivity-for-every-even-tensor-power) | Corner identities, exact real part, uniform angle and parity restriction. |
| [Whole-artifact finding](#whole-artifact-finding) | [Overlap and limit](../../ledger/Yin_L_A0027_v1.md#exact-overlap-traces-and-their-limiting-content) | Real Fourier coefficients, all constants, strict coefficient bound, absolute convergence, normalized limit and comparison with the one-copy bound. |
| [Whole-artifact finding](#whole-artifact-finding) | [Expectations and calibration](../../ledger/Yin_L_A0027_v1.md#conditional-expectations-and-a-precise-projection-calibration) | Coordinate and subgroup expectations, positivity and induction, exact abelian example and its restricted scope. |
| [Whole-artifact finding](#whole-artifact-finding) | [Outcome](../../ledger/Yin_L_A0027_v1.md#outcome-of-this-tensor-test) | Actual established deductions, unresolved kernel vanishing and absence of a claimed general obstruction to all diagonal methods. |

## Whole-artifact finding

The complete fixed ledger passes mathematical review at its stated scope.
No missing hypothesis, invalid domain operation, incorrect constant or unsupported vanishing-kernel conclusion was found.
The following checks substantiate that finding.

### Actual regular representation, diagonal map and bounded injectivity

For distinct group labels the canonical trace of \(T^*T\) is exactly three, so \(3\le N\le9\) and \(T^*T\le N(1-p)\) give the stated original estimate.
The three coincident-label reductions are correct and leave zero kernel.
The right-coset decomposition for the diagonal subgroup gives an amplification of the regular representation of \(G\), hence an isometric normal star embedding with the prescribed canonical trace.
Normal functional calculus carries the kernel spectral projection of \(T^*T\) to that of \(A_n^*A_n\).
Thus the trace masses \(\delta\) and \(\delta^n\) use the same probability normalization, and the squared operator norm remains \(N\).

Tensoring the bounded equation \(vp=(1+u)p\) gives equation (5) without moving \(p\) past \(u\) or \(v\) in any coordinate.
The singleton coefficients prove \(f_n\ne0\) for every \(n\ge2\), while \(f_1=0\).
The coordinate copies of the infinite cyclic subgroup generated by \(u\) form \(\mathbb Z^n\), and their regular Fourier representation has product Haar measure.
The displayed coefficient-polynomial induction proves Haar-nullity of the zero set, including Laurent polynomials after monomial multiplication.
Consequently \(f_n(u_1,\ldots,u_n)\) is injective on the actual ambient Hilbert space.
The finite-trace interface justifies its affiliated inverse, but the intersection argument uses only this injectivity.
The polar decomposition of \(A_nP_n\) has initial support \(P_n\) and final support dominated by the range support of \(A_n\), giving \(\delta^n\le1-\delta\).
There is no use of an unbounded inverse on an arbitrary vector and no assumption that \(T\) is invertible.

### Even-power compression and exact trace constants

Taking the adjoint product of \(vp=(1+u)p\) yields \(p(u+u^*)p=-p\), so \(a+a^*=-p\) and \(pvp=p+a=-a^*\).
These are corner identities and require no commutation with \(p\).
For even \(n\), the compression in (11) is \(P_n+B-B^*\) with \(B=a^{\otimes n}\), and its real part is exactly \(P_n\).
Cauchy--Schwarz therefore gives \(\|A_n\xi\|\ge\|\xi\|\) for \(\xi\in P_n\mathcal H_n\).
Together with \(A_nq_n=0\) and \(\|A_n\|^2=N\), this proves the operator inequality (13), with the universal constant \(8/9\).
The argument establishes no increasing accretivity constant as \(n\) grows and makes no claim for odd \(n\) at this step.

Complex conjugation of regular basis coordinates fixes \(T\) and its kernel projection, so all \(c_g\) are real.
Selfadjointness and Parseval give \(c_{g^{-1}}=c_g\) and \(\sum_g c_g^2=\delta\).
Tracing the corner equations and \(u^*vp=(1+u^*)p\) gives precisely the three moments in (15).
Writing \(U=\prod_i u_i\) and \(V=\prod_i v_i\), direct multiplication gives
\[
 A_n^*A_n=3+U+U^*-V-V^*-U^*V-V^*U.
\]
Its product trace against \(P_n\) is therefore \(3\delta^n+2(-\delta/2)^n-4(\delta/2)^n\), which confirms (16) for every \(n\).
For even \(n\) this coefficient is \(3-2^{1-n}\), and at \(n=2\) it is \(5/2\).
The positive operator bound \(A_n^*A_n\le N(1-q_n)\) then gives (17)--(18), including \(13/18\) when only \(N\le9\) is used.

### Fourier overlap and limiting content

The \(L^2\) pairing of the diagonal coefficients \(c_g\) with the corresponding tensor coefficients \(c_g^n\) proves (19).
The elementary projection bound \(|c_g|\le\delta\) and Parseval imply absolute summability of the displayed series for \(n\ge2\).
Its positivity follows from \(\tau_n(q_nP_n)=\tau_n(P_nq_nP_n)\ge0\), rather than from signs of individual summands.

For \(\delta>0\), equality \(|c_g|=\delta\) in Cauchy--Schwarz for \(p\) and \(gp\) would make \(gp\) a scalar multiple of \(p\) in \(L^2\), hence as bounded operators by faithfulness.
A nonzero vector in the range of \(p\) would then be an eigenvector of the regular unitary \(g\).
For every \(g\ne e\), torsion-freeness and the bilateral-shift decomposition exclude such eigenvectors.
Square summability leaves only finitely many coefficients with absolute value larger than \(\delta/2\), proving the strict uniform ratio \(s<1\).
The same argument works for uncountable discrete groups because the nonzero coefficient support is countable.
Separating the identity coefficient and using \(\sum_{g\ne e}c_g^2=\delta-\delta^2\) gives exactly the error bound \((1-\delta)s^{n-1}\) in (22).
The division by \(\delta^n\) occurs only in this explicitly positive-\(\delta\) case; when \(\delta=0\) the projections vanish.

Passing to even \(n\to\infty\) in (17) and (22) returns \(\delta\le1-3/N\), with no loss or gain compared with (2).
The dimension inequalities also hold for every \(0<\delta\le1/3\), since \(\delta+\delta^n\le4/9\).
Neither limiting operation proves zero kernel.

### Subgroup expectations, example and comparison scope

For a subgroup inclusion, the trace-preserving expectation deletes coefficients outside the subgroup and is positive and bounded.
For the coordinate subgroup only the identity diagonal coefficient survives, proving (24).
For the diagonal subgroup the surviving tensor coefficient at \((g,\ldots,g)\) is \(c_g^n\), establishing (25) as an \(L^2\) formula for an actual bounded positive operator.
At \(n=2\), positivity applied to \(P_2\le p\otimes1\) gives \(b_2\le\delta1\).
At the induction step the intermediate expectation is \(\Delta_{n-1}(b_{n-1})\otimes p\le\delta^{n-2}1\otimes p\), and full diagonal expectation sends the last factor to \(\delta1\).
The nested expectations compose, proving \(0\le b_n\le\delta^{n-1}1\) without assuming positivity of a formal Fourier multiplier.
Tracing against \(p\) supplies only the stated weaker upper bound \(\delta^n\).

For the exact abelian example, the sum of two numbers in \(A=(1/3,2/3)\) lies in \((2/3,4/3)\), whose reduction modulo one is disjoint from \(A\).
Thus \(q_2(p\otimes p)=0\), while translation invariance of Haar measure gives both coordinate expectations \(1/3\).
The example has positive overlap at three copies near \((1/2,1/2,1/2)\), so it does not satisfy the all-\(n\) intersection conclusion.
Nor can this nonzero projection be the kernel of a nonzero trinomial in the regular algebra of \(\mathbb Z\), by the cyclic Laurent-polynomial argument.
The candidate correctly restricts this calibration to the two-copy projection facts.

The comparison with L_A0025 is also valid: its compensating marginal densities produce Haar laws and kernel trace \(1/10\), while its explicitly computed trace \(\tau(UV)=-1/40\) excludes those unitaries as actual group elements with canonical regular trace.
That abstract model cannot supply the diagonal regular-group embedding used here.
The present ledger does not claim that its projection calibration realizes the trinomial equations or that all possible diagonal arguments fail.
Its conclusion records the deductions actually obtained and leaves the further overlap or shrinking-defect argument unresolved.

### Source and verification limits

The cyclic Fourier and finite-trace polar-decomposition foundations were checked at their exact retained interfaces, and the coefficient-angle comparison was reconstructed from the bounded isotropic-projection proof and its Haar tails.
The general affiliated-algebra foundations were not re-audited, and no new use of their unbounded operations is required here.
For the recognized conditional-expectation foundation, the reviewer also checked [Anantharaman--Popa, the undated 338-page author draft](https://www.math.ucla.edu/~popa/Books/IIun.pdf), Theorem 9.1.2 and Remark 9.1.3, printed p. 140 / PDF p. 146, and Lemma 9.1.4(i),(v), printed pp. 141--142 / PDF pp. 147--148.
These give the trace-preserving positive normal expectation, its \(L^2\)-projection realization and composition for nested subalgebras, in the finite tracial setting used here.
The statements and applicability were inspected; the book's general foundational proofs were not recursively reviewed.
The subgroup coefficient deletion and induction above were checked directly.

No numerical experiment, proof assistant, exhaustive historical-priority search or Task-completion review was performed.
The statement about an earlier bounded local search is treated as reported search provenance, not as a mathematical absence theorem.
This review supports the fixed tensor estimates and their precise limitations, not a proof or disproof of kernel vanishing for \(1+u-v\) in every torsion-free group.

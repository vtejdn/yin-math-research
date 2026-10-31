---
author: Yin
---

# Independent internal review: absolute-phase realification obstruction

Review completed: 2026-09-16.
Human record author: Yin.
Reviewer: separately organized Codex research subagent the reviewing agent.
Proof author: Codex research subagent another AI agent.

Reviewed Claim: [Yin_C_F0054_v1](../../claims/Yin_C_F0054_v1.md#decision-candidate-0001).
Complete statement and supporting proof: [Yin_C_F0054_v1.md](../../claims/Yin_C_F0054_v1.md#normal-phase-realification-obstruction), Sections 1--6.
Consumer context: the original normal polynomial-core domain question.

**Verdict: pass for the complete stated obstruction.**
The real closable phase-modified derivation has an actual zero vacuum adjoint, but its Haar-circle contraction has no infinity-to-L2 bound.
The original canonical Haar contraction remains bounded of norm one.
This refutes the proposed transformed-estimate inference, not the original normal-vacuum domain implication.

## 1. Independence, selected version and accepted inputs

The reviewer did not develop, suggest, write or edit this derivation or its Haar counterexample.
The reviewer had previously studied separate normal-vacuum domain bridges and Cauchy/curvature interfaces in the same shared context.
The coordinator supplied this completed argument and the requested review scope.
The full pre-registration artifact was read and a pass verdict formed before this formal packaging.
The reviewer then reread the full final artifact: the mathematical statement, displayed formulas P1--P11 and their arguments are unchanged; the title, provenance/status text and semantic anchor were updated.
This is a separately organized internal AI review with disclosed shared context, not blind review, external human review, or independence inferred merely from agent identity.

There are **no necessary direct Claim dependencies** for the counterexample.
The elementary Haar identity P9 is proved directly in Section 3 of this audit; [C_F0047_v1](../../claims/Yin_C_F0047_v1.md#decision-candidate-0002) supplies a consistent comparison, not a logical premise.
C_F0025 provides the surrounding represented-core conventions; C_F0043 provides a comparison with a different successful phase conversion.
C_F0044 and Yin_S_F0011 describe the open research boundary.
None of their larger conclusions is imported to prove this counterexample.

The existing [Dab10-U002 source interface](../literature/Dab10/Yin_U002.md#dab10-u002) is accepted at its recorded scope to identify the estimate whose hypotheses cannot be weakened in the proposed way.
This reviewer read that full audit and C_F0043 Sections 3.1--3.2, including its controlled coassociativity defect.
Dab10-U002 records parsed primary-text reading and local proof reconstruction of Lemma 10/Remark 11 and Lemma 12 on arXiv:0804.2906v2 pp. 8--9, with a subsequent independent primary-text review.
Its retained closed-real-derivation functional-calculus foundation is not re-proved here.
No new source acquisition, original-PDF inspection, whole-source audit, or application of the Dab10 estimate to the new derivation is claimed.

## 2. Actual derivation, reality, closability and vacuum

For compactly supported nonatomic mu, represented starred polynomials form a dense subspace of L2(mu): their unital selfadjoint algebra separates points on the compact support.
A polynomial in z and its conjugate is Lipschitz on a compact square containing that support, so the P1 difference kernel is bounded away from the null diagonal.
A polynomial representing zero has zero difference almost everywhere in the product measure.
Thus the operator is well-defined on precisely its stated dense represented core.

The displayed product expansion proves the derivation rule for the specified outer bimodule.
Multiplication by `u=i(z-w)/|z-w|` is a unitary on the tensor Hilbert space.
Under the conjugate-flip involution, interchange of z and w changes the numerator's sign, and conjugation changes i's sign.
These changes cancel, giving exactly P2.
The new derivation is real in the convention actually used by the source interface.

For closability, if `p_n -> 0` and `delta_0 p_n -> F` in their respective Hilbert spaces, multiplication by the bounded function `|z-w|` gives zero in the limit, since `p -> p(z)-p(w)` is bounded from L2(mu) to L2(mu squared).
Atomlessness makes the diagonal null; hence `|z-w|F=0` implies F=0.
This proves closability of the original operator, without selecting a different extension.

The bounded kernel justifies the exchange of variables in P3.
Antisymmetry makes its integral zero for every core polynomial.
Therefore the actual Hilbert adjoint contains `1 tensor 1` and takes it to zero.
This is a complete adjoint-domain test, not a formal phase manipulation.
It requires no assumption about the original canonical vacuum.

## 3. Haar eigenvalues, divergence and the original contraction

For normalized Haar measure, substitution `w=z exp(i theta)` has exactly the factor `1/(2 pi)` in P5, and `|1-exp(i theta)|=2 sin(theta/2)` on the open integration interval.
The odd imaginary part vanishes under reflection.
For each fixed n the endpoint singularities are integrable.
The resulting value depends only on |n|.

The consecutive cosine difference is `2 sin((n+1/2)theta) sin(theta/2)`.
Its integral gives

`lambda_(n+1)-lambda_n = 2/[pi(2n+1)]`.

This includes n=0 and yields `lambda_1=2/pi`.
Summation gives P8.
Termwise `2/(2k+1) >= 1/(k+1)` proves the harmonic lower bound and hence logarithmic divergence, with the stated constant.
The test vectors `z^n` all have both essential supremum norm and L2 norm equal to one.
Thus the failure is an actual failure of every infinity-to-L2 bound on the original core.

The Laurent polynomials are the finite sequences in the complete Fourier basis.
The operator is diagonal there with entries `i lambda_|n|`; its closure is the maximal diagonal operator with domain `sum_n lambda_|n|^2 |a_n|^2 < infinity`.
Truncations of Fourier sequences are graph approximants.
This also verifies closability and the actual zero vacuum adjoint of the contraction.
No general assertion that a bounded contraction of a closable operator remains closable is used.

For the original canonical E0, if n>=1,

`(z^n-w^n)/(z-w)=sum_(k=0)^(n-1) z^(n-1-k) w^k`.

Only k=0 survives Haar integration, giving `z^(n-1)`.
If n=-m<0, the same factorization after division by `-z^m w^m` gives only strictly negative powers of w, all with zero integral.
The n=0 difference is zero.
This independently proves P9.
The images of the positive-frequency orthonormal vectors are orthonormal and all other basis vectors are annihilated, so the bounded extension has norm exactly one.
Its adjoint sends 1 to z.
The model therefore satisfies both the original vacuum assumption and the original desired bound, as the statement requires.

## 4. Formal defect and exact conclusion boundary

Expanding the pointwise first-leg difference and subtracting the second-leg difference gives

`[k(z,v)(k(z,w)+k(w,v))-k(z,w)k(w,v)](p(z)-p(v))`.

The canonical kernel has zero bracket by its partial-fraction identity.
For `k=i/|z-w|`, substitution gives `-(a+b-c)/(abc)`, with the stated sign and distances.
This checks P10--P11 purely off all collision diagonals.
For example, on a nondegenerate triple from the circle the triangle inequality is strict, so the formal bracket is nonzero.
The proof expressly makes no claim that either iterated tensor derivation belongs to its Hilbert-space domain.
The review accepts this part only as a formal diagnosis; the proven obstruction rests entirely on the one-variable Haar computation.

The complete conclusion passes: tensor-unitary phase conversion, reality, closability and an actual L2 vacuum do not together give the proposed contraction estimate.
This neither applies nor refutes Dab10 under its full hypotheses, and does not negate C_F0043's different controlled-defect argument.
It gives no counterexample to the original normal-vacuum domain implication, no truncation estimate, and no general solution for the canonical normal operator.
No numerical experiment, proof-assistant verification or external human acceptance is claimed.
No proof, canonical record, Task, index or source registry was modified by this review.

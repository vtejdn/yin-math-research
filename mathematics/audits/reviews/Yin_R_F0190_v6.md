---
author: Yin
---

# Independent review of Brown limits for polynomial symmetric shifts

## Review arrangement and inputs

Review act: 2026-11-05T01:13.
Human record author: Yin.
This is an independent inspection of the complete [C_F0186_v6 statement](../../claims/Yin_C_F0186_v6.md#statement) and [argument](../../claims/Yin_C_F0186_v6.md#argument), including its new single-factor class and polynomial conditional shifts.
The reviewer did not develop v6 and received only the fixed candidate, its mathematical dependencies, the assigned scope and current rules.
No development drafts, proof-generation dialogue or repair discussion were supplied or consulted.
The fixed C_F0188_v2 dependency contains a brief provenance description of its revision; that description was not used as proof evidence.
The local findings below were formed while its small-value statement was explicitly treated as unresolved, before consulting any new review verdict on that dependency.
After those findings were complete, its actual proved selection and fresh independent whole-proof review were inspected to resolve the dependency at the exact scope used here.

This follow-up reuses the reviewer's own [v5 finding](Yin_R_F0190_v5.md#conditional-two-factor-deduction) after reading the entire new argument and checking each retained interface.
The reused portions are the deterministic product min-max inequality, the two ranges of negative logarithmic control, and the passage from fixed-parameter potentials to Brown measures and polynomial pushforwards.
The earlier affine candidate is not an accepted mathematical premise of the new proof.
The new polynomial norm events, symmetry requirements, conditional independence and single-factor argument were checked here directly.

The actual mathematical inputs are the reviewed [C_F0186_v4 controls](../../claims/Yin_C_F0186_v4.md#argument), the reviewed [C_F0187_v2 intermediate theorem](../../claims/Yin_C_F0187_v2.md#statement), and the exact [C_F0188_v2 small-value statement](../../claims/Yin_C_F0188_v2.md#statement).
The first two retain the prior independent evidence in [R_F0190_v4](Yin_R_F0190_v4.md#finite-variance-controls) and [R_F0191_v2](Yin_R_F0191_v2.md#complex-intermediate-bound-reviewed), already read and used at their disclosed scopes in v5.
The v2 small-value statement was read and compared with the v1 statement used by v5; its hypotheses, uniformity and normalized conclusion are unchanged.
Its current [proved decision](../../claims/Yin_C_F0188_v2.md#decision-complex-shift-reviewed) selects the fresh [independent whole-proof finding](Yin_R_F0192_v2.md#finding).
That review was read in full and covers the exact v2 statement and complete argument, including deterministic-shift uniformity, independent diagonals, normalization, conditional random shifts and arbitrary-coupling summability.
The present review reuses that accepted input evidence and checks its applicability; it does not repeat the small-value proof audit.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Polynomial-shift classes finding](#polynomial-shift-classes) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Polynomial-shift classes finding](#polynomial-shift-classes) | [Exact v6 statement](../../claims/Yin_C_F0186_v6.md#statement) | Both displayed polynomial classes, their polynomial images and all stated probability, law and coupling quantifiers, with the exact small-value dependency now resolved by its accepted independent whole-proof evidence. |
| [Polynomial-shift classes finding](#polynomial-shift-classes) | [Whole v6 argument](../../claims/Yin_C_F0186_v6.md#argument) | New polynomial norm events and conditional uses, both singular-value ranges, finite free logarithms, planar convergence and Brown polynomial mapping. |
| [Polynomial-shift classes finding](#polynomial-shift-classes) | [Spectral and potential controls](../../claims/Yin_C_F0186_v4.md#argument) | The scalar polynomial tail bound and its new norm-event consequence, plus applicability of the reviewed weak, logarithmic, planar, tightness and mapping controls to each fixed v6 polynomial. |
| [Polynomial-shift classes finding](#polynomial-shift-classes) | [Intermediate theorem](../../claims/Yin_C_F0187_v2.md#statement) | Uniform real-input specialization for the two exact conditional sigma-fields and for the single-factor class, with no shift norm requirement. |
| [Polynomial-shift classes finding](#polynomial-shift-classes) | [Small-value theorem](../../claims/Yin_C_F0188_v2.md#statement) | Exact accepted normalized theorem and independent-diagonal hypotheses at every polynomially bounded symmetric-shift invocation, reusing R_F0192_v2. |
| [Polynomial-shift classes finding](#polynomial-shift-classes) | [Accepted small-value argument](../../claims/Yin_C_F0188_v2.md#argument) | Applicable complete independent coverage from R_F0192_v2 is reused after checking the actual accepted statement, decision and review scope; no duplicate input-proof audit is claimed. |
| [Polynomial-shift classes finding](#polynomial-shift-classes) | [Broader Task contract](../../tasks/Yin_T_F0012_v3.md#contract) | Exact fixed-law and arbitrary-coupling comparison; these polynomial subclasses do not complete the full Task. |

<a id="polynomial-shift-classes"></a>
## Whole-proof finding

The complete proof supports the exact C_F0186_v6 statement under its stated hypotheses and accepted external-source boundaries.
No remaining mathematical gap was found in either displayed class or in their stated polynomial pushforwards.
The local deduction was checked independently, and every necessary project input now has applicable accepted support, with the precise prior-review reuse disclosed above.
This supports the two stated real-Wigner polynomial classes, not completion of the general T_F0012_v3 contract.

### Symmetry and polynomial norm events

For a word in real symmetric matrices, transposition reverses the word and leaves each scalar complex coefficient unchanged.
Thus the formal identity \(\operatorname{rev}Q=Q\) implies the required complex symmetry of its evaluation, even when the matrices do not commute and the coefficients are nonreal.
This does not assume that \(Q\) is selfadjoint.

For a scalar polynomial \(Q\) of degree \(D\ge1\), its empirical singular-value measure is normalized by \(1/N\).
The event \(\|Q(W)\|>t\) forces at least one singular value above \(t\), so pointwise
\[
 1_{\{\|Q(W)\|>t\}}
 \le N\mu_{|Q(W)|}((t,\infty)).
\]
The reviewed expected tail bound therefore gives
\[
 \mathbb P\{\|Q(W)\|>N^M\}
 \le C_QN^{1-2M/D}=O(N^{-B})
\]
when \(M>(B+1)D/2\).
Every polynomial and its degree are fixed, so this is a deterministic choice of exponent.
Constant polynomials satisfy the required bound eventually with no exceptional event.
Only second moments enter the tail input, and this argument requires no uniform operator-norm bound or higher entry moment.

### The two conditional sigma-fields

All conditioning below is performed at a single fixed size \(N\).
For (Two) define \(\mathcal H_N\) below, and for either class define \(\mathcal G_N\):
\[
 \mathcal H_N=\sigma(W_3^{(N)},\ldots,W_d^{(N)}),\qquad
 \mathcal G_N=\sigma(W_2^{(N)},\ldots,W_d^{(N)}).
\]
An empty list generates the trivial sigma-field.
In (Two), the Task's independence at each size makes \(W_2^{(N)}\) independent of \(\mathcal H_N\); in either class it makes \(W_1^{(N)}\) independent of \(\mathcal G_N\), including each matrix's complete diagonal and off-diagonal families.
No conditioning on whole matrix sequences across different sizes is used or permitted by this argument.

For (Single), the shift \(Q(W_2,\ldots,W_d)-zI\) is \(\mathcal G_N\)-measurable and complex symmetric.
On its polynomial norm event, its entries are at most \(N^M+|z|\), hence at most \(N^{M+1}\) eventually after a fixed exponent enlargement if necessary.
Set the shift to zero off that event.
This preserves symmetry and independence from \(W_1\) and gives a deterministic polynomial bound for every realization.
The uniform normalized small-value assertion can therefore be integrated over \(\mathcal G_N\); adding the omitted norm-event probability proves (Floor) for (Single).

For (Two), \(Q_2(W_3,\ldots,W_d)\) and its norm event are \(\mathcal H_N\)-measurable.
Conditioning on \(\mathcal H_N\) preserves the \(W_2\) law.
Apply the same uniformly bounded-shift argument there and integrate, adding the norm-event complement, to obtain (F1) for \(T_N=W_2+Q_2(W_3,\ldots,W_d)\).
The exponent \(b_2\) is fixed once the laws, polynomials and prescribed failure power are fixed.

The matrix \(T_N\) is complex symmetric, and on the complementary good event from (F1) its inverse is complex symmetric with norm at most \(N^{b_2}\).
The event
\[
 E_N=\{s_{\min}(T_N)\ge N^{-b_2}\}
     \cap\{\|Q_1(W_2,\ldots,W_d)\|\le N^{M_1}\}
\]
belongs to \(\mathcal G_N\).
On it the exact conditional shift satisfies
\[
 F_N=Q_1(W_2,\ldots,W_d)-zT_N^{-1},\qquad
 \|F_N\|\le N^{M_1}+|z|N^{b_2}
 \le N^{\max(M_1,b_2)+1}
\]
eventually, after a fixed exponent enlargement if needed.
Extending \(F_N\) by zero off \(E_N\) gives a globally defined symmetric shift independent of \(W_1\).
Conditioning on \(\mathcal G_N\) thus justifies (F2), with constants uniform over its realizations.
Dependence of \(Q_1\) on \(W_2\), and the resulting dependence of the two factors, does not affect this conditional independence.
The two Wigner laws and their diagonal laws may differ.

On \(E_N\), the multiplication order gives exactly
\[
 (W_1+F_N)T_N
 =(W_1+Q_1(W_2,\ldots,W_d))T_N-zI=A_N-zI.
\]
The product least-singular-value inequality and a union bound over the small-value failures and norm-event complements give (Floor), with a fixed exponent \(b_z\).
Every exceptional probability is summable after the stated choice \(B>2\).
First Borel--Cantelli therefore applies under every cross-size coupling in the Task.

### Intermediate values and negative logarithmic control

For (Two), the C_F0187_v2 estimate applies conditionally on \(\mathcal H_N\) to \(T_N\) and conditionally on \(\mathcal G_N\) to \(W_1+F_N\).
Its shift-uniform constants and lack of a norm or symmetry restriction give the two estimates in (Middle).
A union bound combines them and the preceding good events; independence of the two factors or of their exceptional events is unnecessary.

The deterministic product inequality in v6 is the same inequality checked in the [v5 finding](Yin_R_F0190_v5.md#conditional-two-factor-deduction).
The inverse image under \(V\) of a codimension-\((r-1)\) subspace has codimension at most \(r-1\), so intersecting it with the lower-bound subspace for \(V\) proves \(a_{r+s-1}(UV)\ge a_r(U)a_s(V)\).
The argument allows singular matrices and does not require independent factors.
The retained choices \(r=\lfloor(k+1)/2\rfloor\), \(s=k-r+1\) and \(k\ge2q_N+2\) remain in the theorem's intermediate range and give (Product-middle).

For (Single), applying the intermediate theorem directly after conditioning on \(\mathcal G_N\) gives \(a_k\ge c(k-1)/N\).
For \(2\le k\le N\), this is at least \((c/2)(k/N)^2\), so it supplies the same bound required by the rest of the proof.
Thus both classes reach exactly the two deterministic inputs used by v5: an eventual floor \(N^{-b_z}\) and the intermediate lower bound \(c_1(k/N)^2\) above \(2q_N+2\).

The retained negative-logarithm calculation was compared with those inputs and is unchanged in scope.
The lowest \(2q_N+2\) values contribute \(O(N^{-1/4}\log N)\), which tends to zero.
The range above them and below \(\varepsilon N\) contributes at most \(C\varepsilon+2\varepsilon(1-\log\varepsilon)\) in the limit.
All remaining singular values stay above a fixed positive multiple of \(\varepsilon^2\), so taking the value cutoff below that number and then sending \(\varepsilon\) to zero proves (Negative-UI).
The floor excludes exact zeros eventually.
Increasing the degree or the norm-event exponent changes fixed constants and \(b_z\), without changing any of these limiting arguments.

### Finite free logarithms, one event and pushforwards

Each displayed \(R\) is a fixed scalar polynomial, so C_F0186_v4 applies to its Hermitization and positive logarithmic tails at every fixed \(z\).
Weak convergence of the singular-value laws, bounded logarithmic truncations and the just-proved negative uniform integrability give negative logarithmic integrability of the limiting free law and convergence of the negative integrals.
The bounded free operator controls the positive part, while the reviewed positive-tail estimate supplies its finite-size convergence.
Consequently the unregularized logarithmic determinants converge to the finite \(\tau\log|R(s)-z|\) for each fixed \(z\).
This uses no expectation convergence of those unregularized logarithms.

The retained measurability and Fubini argument applies to the new fixed polynomial without any uniform-in-\(z\) small-value exponent.
It gives one probability-one event of planar almost-everywhere potential convergence on all integer-radius disks.
The pathwise local \(L^2\) bounds in C_F0186_v4 apply to every fixed scalar polynomial degree, hence to this \(R\).
They give planar uniform integrability, so the convergence is local \(L^1\).
Distributional Laplacians identify the Brown limit, and the reviewed tightness yields weak convergence of probability measures on that event, for all bounded continuous real tests.

Finite-dimensional spectral mapping with algebraic multiplicity and the bounded-FK polynomial Brown mapping from C_F0186_v4 apply unchanged to \(g(A_N)\) and \(g(R(s))\).
The latter mapping holds for every bounded element, so it does not require a selfadjoint or cyclic-product form of \(R(s)\).
Composing a bounded continuous test with \(g\) preserves bounded continuity and proves the stated pushforward conclusion.
Constant \(g\) gives a fixed point mass; the fixed-parameter finite-logarithm assertion is about \(A_N=R(W)\), not arbitrary constant \(g(A_N)\).

The empty-variable cases give constant shifts and are covered by the same conditioning with trivial sigma-fields.
For a nonzero complex linear combination, choose a nonzero coefficient, relabel its independent input as \(x_1\), divide by that coefficient to put the expression in (Single), and absorb the coefficient into the outer polynomial.
The zero combination is covered by constant \(g\).
The other examples in the statement satisfy the displayed reversal identities directly.

## Source reuse and limits

The source boundaries already recorded in [v5](Yin_R_F0190_v5.md#conditional-two-factor-deduction), [R_F0190_v4](Yin_R_F0190_v4.md#finite-variance-controls) and [R_F0191_v2](Yin_R_F0191_v2.md#complex-intermediate-bound-reviewed) remain unchanged.
They cover the bounded-entry moment and bounded-differences inputs, the bounded finite-tracial FK and Brown-potential interfaces, and the bounded-product concentration theorem used by the intermediate input.
The new polynomial norm estimate is a local consequence of the already reviewed expected singular tail and introduces no new external theorem.
Those original source pages were not reopened, and this review is not a new audit of their original proofs or a novelty search.

The exact C_F0188_v2 premise is resolved by its [selected proved decision](../../claims/Yin_C_F0188_v2.md#decision-complex-shift-reviewed) and [R_F0192_v2](Yin_R_F0192_v2.md#finding).
The latter independently covers its complete local adaptation and records direct inspection of arXiv:1105.5733v1, Condition 1 and Theorem 1.3 on PDF pages 2--3, the quadratic concentration definition on page 3, and Theorem 1.8 on page 5.
Its two vector-valued inverse Littlewood--Offord theorems remain accepted external inputs whose original proofs were not re-audited.
This review relies on that exact independent input review without claiming a second audit of its proof or a fresh inspection of the original source pages.
The conclusion covers the two real-Wigner polynomial classes actually displayed in v6 and their one-variable polynomial images.
It does not establish the full arbitrary-polynomial Task or the same classes for arbitrary complex Hermitian off-diagonal laws.

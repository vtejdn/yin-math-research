---
author: Yin
---

# Normal Commutator Identity, Affiliated Descent, and Bounded Linearization

## Task associations

| Task | Scope |
| --- | --- |
| [Yin_T_F0001_v1](../tasks/Yin_T_F0001_v1.md#yin_t_f0001) | Yin_C_F0012 disproves S_D subset R_X and hence the proposed universal bounded descent, while Yin_C_F0005 affiliated necessity and Yin_C_F0008 restricted scalar elimination remain valid. |

## Route

| Field | Value |
| --- | --- |
| disposition | refuted |
| priority | Historical goal outcome |

The Route section owns the current allocation.
Dated outcomes, earlier authorizations and superseded allocations below retain their recorded scope.

<a id="s_f0002"></a>
Current outcome, 2026-09-09: **refuted**.
Yin_C_F0012 disproves S_D subset R_X and hence the proposed universal bounded descent, while Yin_C_F0005 affiliated necessity and Yin_C_F0008 restricted scalar elimination remain valid.
See [Yin_C_F0012](../claims/Yin_C_F0012_v1.md#yin_c_f0012) and the [goal completion audit](../audits/reviews/Yin_R_F0054_v1.md).
Earlier targets and tests below are retained as the route's research history.

Goal: [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001).
Priority and disposition: [route selection](#route), refuted unrestricted bounded-descent route; valid affiliated deductions retained.
Date: 2026-09-08.

## Exact Target and Logical Role

Write S_D for the bounded elements with all dual commutators of finite rank, R_X=Div_M C<X>, and F_X=Div_U(M) C<X>.
[Yin_C_F0002](../claims/Yin_C_F0002_v1.md#yin_c_f0002) and [Yin_C_F0005](../claims/Yin_C_F0005_v1.md#yin_c_f0005) give

\[
R_X\subseteq S_D\subseteq F_X\cap M.
\]

Yin_C_F0001 requires S_D subset R_X.
The equality F_X intersect M=R_X is **sufficient**, not established equivalent to Yin_C_F0001, since no general inclusion F_X intersect M subset S_D has been proved here.

## Mechanism and Verified Inputs

Yin_C_F0005 uses bounded K=sum_i[rho(X_i),D_i].
Exact normal commutation puts K+P in M', yielding [f,P]=sum_i[rho(X_i),[D_i,f]] for every bounded f.
The finite tensors then balance over the embedded free field.
The division-ring equalizer forces f to belong to F_X.
This does not need rationality of the initially chosen tensor factors, a holomorphic polynomial core, or an orthogonal word basis.

[Yin_C_F0004](../claims/Yin_C_F0004_v1.md#yin_c_f0004) completes this descent to bounded scalar rationality for one normal generator, and for bounded functions of a single coordinate inside any tuple, using divided differences and exclusion of poles on the spectrum.

## Bounded-Linearization Obligation

The user proposed choosing a linear representation f=u A(X)^{-1} v and proving its entire inverse is bounded.
Two interfaces must be checked:

1. From the bounded affiliated value and the original hypotheses, construct a representation with A(X)^{-1} in a matrix algebra over M.
   A nonminimal representation may have unused singular blocks, so the appropriate claim is existence or a justified minimal-representation result.
2. Convert that bounded matrix representation to the original scalar division closure.
   General matrix rational closure is not silently substituted for scalar division closure; a proof of bounded scalar elimination or an applicable equality is needed.

[MSY23](../audits/literature/MSY23/readme.md#bounded-linearization) has completed full source auditing under [MSY23 free-field and Atiyah source audit](../audits/literature/MSY23/readme.md#msy23-free-field-and-atiyah-source-audit).
Its reconstructed Schur arguments preserve an existing inverse domain, while its field theorem proves affiliated invertibility.
Neither outstanding bounded step has been supplied by this audit.
The user's Theorem 4.4 observation is recorded as an explicit Schur identity in MSY23-U003; its consistency proof also uses polynomial inner-rank preservation and stable finiteness.

## Kronecker-Inspired State Control

The [2026-09-09 investigation](../ledger/Yin_L_F0010_v1.md#kronecker-strategies) is now registered as the concrete subroute [Yin_S_F0005: minimal rational states and quantitative observability](Yin_S_F0005.md#s_f0005).
That record owns its Yin_C_F0007 input, two-state starting test, coordinate conditions and redirection criteria.
In particular, the Haar example refutes a universal fixed-origin coefficient estimate, even for bounded minimal states.
Yin_S_F0002 retains the broader bounded-realization and scalar-descent obligations; no bounded inverse is inferred from minimality alone.

## Next Step and Decision Conditions

The user's Proposition 2.3 follow-up additionally gives a [reviewed bounded rank-factorization refinement](../audits/literature/MSY23/Yin_U004_v1.md#msy23-u004): for every bounded matrix C, rho_M(C)=rho_U(C).
The zero-Schur bordered matrix associated with bounded f therefore has a bounded factorization of the expected inner rank.
A second concrete route is to constrain these factors to a rational algebra; polar decomposition alone gives arbitrary M-valued factors.

Test whether a minimal linear representation of a finite-rank-commutator element can obtain a bounded inverse using the bounded dual operators, beyond the algebraic Schur identity.
The weaker target S_D subset R_X suffices for Yin_C_F0001 even if the stronger intersection equality is unavailable.
Continue if the original hypotheses justify bounded inverse pencils or scalar pivots.
If additional assumptions are needed, record a separate restricted theorem and preserve the full Yin_C_F0001.
A failure without bounded duals only tests a stronger auxiliary assertion and is not a goal counterexample.
The [preserved exploration](../ledger/Yin_L_F0002_v1.md) contains an explicitly unreviewed scaled-section candidate and the limits of earlier bounded-intersection searches; it is not promoted to a project theorem.

## Resolution Decision

2026-09-09, the coordinating agent: changed disposition from `active` to `refuted` after independent review of Yin_C_F0012.
Yin_C_F0012 disproves S_D subset R_X and hence the proposed universal bounded descent, while Yin_C_F0005 affiliated necessity and Yin_C_F0008 restricted scalar elimination remain valid.
Yin_S_F0006 emerged from Yin_S_F0005; Yin_S_F0002's coordinating bounded-descent target includes that failed universal upgrade.
No old ID or argument was deleted, and no replacement goal was created.

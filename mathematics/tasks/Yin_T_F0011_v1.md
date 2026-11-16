---
author: Yin
---
# Full-domain duals and ACSY conjugate variables: rationality and maximal Delta

## Contract

### Original question and mathematical setting

Yin requests a new F-line research Task to determine the mutual implications between the full bounded-vector domain condition of C_F0024 and the conjugate-variable condition of ACSY24 Proposition 3.5.
The intended conclusions are the relative strength of the analytic rationality criteria for normal tuples and of the maximal-Delta criteria for general tuples.

Let \((M,\tau)\) be a finite von Neumann algebra with a faithful normal probability trace, \(H:=L^2(M,\tau)\), \(\Omega:=1\), and \(P_\Omega\) the projection onto \(\mathbb C\Omega\).
Let \(d\ge1\) and let \(X=(X_1,\ldots,X_d)\in M^d\) generate \(M\).
Put
\[
 A_X:=\mathbb C\langle X_1,\ldots,X_d\rangle,\qquad
 A_X^*:=\mathbb C\langle X_1,\ldots,X_d,X_1^*,\ldots,X_d^*\rangle.
\]
The second expression denotes the represented unital star algebra, not an additional set of formal independent variables.
Rationality means membership in \(\operatorname{Div}_{L^0(M)}A_X\); the starred derivation domain does not enlarge this rational algebra.
Inner products are linear in the second variable.

### Three hypotheses that must remain distinct

Use the generator-first convention \([X_j,D_i]=\delta_{ij}P_\Omega\).
When using the opposite convention in C_F0024 or an external source, negate the dual operators explicitly.

**\(\mathsf S(X)\): full dual and adjoint domains.**
There exist densely defined complex-linear operators \(D_1,\ldots,D_d\) on \(H\) such that
\[
 M\Omega\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*,
 \qquad
 [X_j,D_i]|_{M\Omega}=\delta_{ij}P_\Omega|_{M\Omega}.
\]
This is the complete domain hypothesis of [C_F0024](../claims/Yin_C_F0024_v1.md#statement), with normality imposed separately in the rationality branch.
Existence can equivalently be formulated using restrictions with domain exactly \(M\Omega\); any claim about the original larger-domain operators must still justify its domains.

**\(\mathsf F(X)\): bare full-domain duals.**
There exist complex-linear maps \(D_i:M\Omega\to H\) satisfying the same generator commutators on all \(M\Omega\), without a continuity, closability or adjoint-domain assumption.
This is the input actually used in the [full-domain maximality argument](../claims/Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors).
Always \(\mathsf S(X)\Rightarrow\mathsf F(X)\).

**\(\mathsf A(X)\): the full ACSY24 condition.**
There exist complex-linear outer-bimodule derivations
\[
 \partial_i:A_X^*\Omega\subseteq H\longrightarrow H\otimes_2H,
 \qquad
 \partial_i(X_j)=\delta_{ij}\Omega\otimes\Omega,
 \qquad
 \Omega\otimes\Omega\in\operatorname{Dom}\partial_i^* .
\]
The outer actions are \(a\cdot(\xi\otimes\eta)\cdot b=(a\xi)\otimes(\eta b)\), and the last domain is the actual Hilbert adjoint domain.
This is the [checked Proposition 3.5 hypothesis](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001).
No normality or reality condition is assumed.
Formal moment identities alone, a dual operator's vacuum-adjoint condition alone, or an unstarred polynomial domain do not replace it.
In the selfadjoint setting this is the usual conjugate-variable condition; terminology from that case must not silently import extra symmetry into the general case.

All implication questions quantify over the indicated class of finite generating tuples and concern existence of systems.
Refuting an existential implication requires excluding every admissible witness for the consequent, not merely showing that one chosen extension or canonical candidate fails.

### Objective 1: normal tuples and analytic rationality

For arbitrary correlated normal generating tuples, determine the exact relationship between \(\mathsf S(X)\) and \(\mathsf A(X)\).
The implication \(\mathsf S(X)\Rightarrow\mathsf A(X)\) is already established by [C_F0070 Part C](../claims/Yin_C_F0070_v1.md#statement).
Decide the converse by a proof at the full stated scope or a rigorous separating example.
Track the weaker \(\mathsf F(X)\) comparisons separately when they provide necessary or sufficient intermediate steps; do not replace \(\mathsf S\) by \(\mathsf F\) in the primary analytic question.

Explain what the implication result means for these two uses of analytic hypotheses:

- Under \(\mathsf S(X)\) and normality, C_F0024 and [C_F0068 Part C](../claims/Yin_C_F0068_v1.md#statement) characterize rationality using the specified fraction commutators \(\Gamma[Q,D_i]:=sD_i b-aD_i t\), with their actual domains, finite-rank closures and every-fraction quantifiers.
- Under \(\mathsf A(X)\), ACSY24 gives \(\Delta(X)=d\), and [C_F0068 Part A](../claims/Yin_C_F0068_v1.md#statement) gives rationality through existence of a fraction pair and a finite-rank solution of the boundary equation.
  That assertion does not identify the solution with specified canonical fraction commutators.

Compare both the applicability classes and the actual tests or operator realizations.
If an implication is used to claim that the canonical ACSY operators recover the same fraction-commutator criterion, verify their full \(M\Omega\) operator and adjoint domains and the required compatibility.
Equality of finite-rank properties or ranks must not be reported as equality of unclosed operators on possibly different domains.

The canonical generator-first operators to investigate are
\[
 D_i^{\mathrm{can}}
 :=-\overline{(\mathrm{id}\otimes\tau)\partial_i},
\]
where the unclosed operator has domain \(A_X^*\Omega\).
A different valid choice is permitted for an existence implication, but its status and the exact operator-level conclusion must be stated.

### Objective 2: arbitrary tuples and maximal Delta

Without assuming normality, determine both implications
\[
 \mathsf F(X)\Longrightarrow\mathsf A(X),\qquad
 \mathsf A(X)\Longrightarrow\mathsf F(X).
\]
These compare the exact inputs of the two maximality arguments:
\[
 \mathsf F(X)\Longrightarrow\Delta(X)=d,\qquad
 \mathsf A(X)\Longrightarrow\Delta(X)=d.
\]
The common conclusion alone proves no implication between the hypotheses.
State explicitly what any result gives for the stronger \(\mathsf S(X)\) input, and keep general-tuple assertions separate from normal-tuple ones.
In particular, the known normal implication \(\mathsf S\Rightarrow\mathsf A\) cannot be transferred to arbitrary tuples without proof.

The desired classification is equivalence, a strict implication, or incomparability of the two input conditions, supported in each direction by a theorem or an exact counterexample.
A positive special class or an obstruction to an auxiliary method is not a classification of all bounded tuples.

### Scope and established boundary

The [circular example C_F0074](../claims/Yin_C_F0074_v1.md#statement), checked in the unknown-relationship [R_F0047 finding](../audits/reviews/Yin_R_F0047_v1.md#conclusion), satisfies \(\mathsf S\), \(\mathsf F\), and \(\mathsf A\), and has \(\Delta(c)=1\).
Nevertheless \(c^*\) is nonrational in \(c\) while every specified canonical fraction commutator vanishes.
It therefore rules out the unrestricted nonnormal extension of that fraction-commutator rationality criterion; it does not separate the three hypotheses and is not a counterexample to maximal Delta.

Finding other analytic assumptions for a nonnormal rationality criterion is outside the completion requirements of this Task unless needed for a specific implication or separately authorized.
The Task does not change the holomorphic rational algebra, replace actual Hilbert adjoints by formal pairings, assume freeness of the coordinates, or restrict general normal spectra to lines, circles or analytic arcs.

This new assignment is distinct from [T_F0005](Yin_T_F0005_v2.md#contract), whose small-module, spectral-phase and nondense-test questions retain their existing scopes.
Results may be shared through their fixed C materials; no older Task contract is transferred, reopened or completed by this registration.
The completed [T_F0001](Yin_T_F0001_v7.md#contract) retains its existing completion scope.

### Completion criteria

1. Resolve the full normal-tuple \(\mathsf S\)-versus-\(\mathsf A\) comparison, including the already known direction and a proof or counterexample for the converse.
   State precisely the resulting comparison of applicability and of the two rationality tests.
2. Resolve both directions of the general-tuple \(\mathsf F\)-versus-\(\mathsf A\) comparison and hence the relative strength of the two maximal-Delta criteria.
   Explain the consequences and limits for the stronger \(\mathsf S\) condition without silently adding or dropping its adjoint-domain assumption.
3. For every claimed implication, retain the actual derivation or operator construction, domain and adjoint-domain arguments, and the stated existential or supplied-operator quantifiers.
   For every nonimplication, retain a complete example satisfying the antecedent and excluding the consequent.
4. Fix new substantive results and useful failed approaches at their responsible mathematical homes.
   Arrange independent review of key new proofs and the complete chain supporting the final comparison; adopt completion only through evidence bound to this exact contract.

If a general implication remains open, preserve its exact remaining obligation and any established reductions without marking this Task complete.
Partial or special-case progress does not change these criteria.

## Current results under the original contract

Objective 2 is resolved for arbitrary finite tuples.
The [two-point-modulus construction](../claims/Yin_C_F0225_v1.md#decision-reviewed) yields, after countable assembly and free semicircular enlargement, a two-coordinate tuple satisfying \(\mathsf A\) with no algebraic full-domain dual system.
The [bounded-similarity construction](../claims/Yin_C_F0133_v1.md#statement) and the [weighted ergodic shift](../claims/Yin_C_F0219_v1.md#decision-reviewed) supply the opposite separation, even with duals bounded on the whole Hilbert space.
Consequently the two hypotheses for maximal Delta are incomparable, and the stronger \(\mathsf S\) and \(\mathsf A\) are likewise incomparable on arbitrary tuples.
The [review of the new separation](../audits/reviews/Yin_R_F0233_v1.md#whole-proof-finding) checks the actual vacuum and the passage from divergent bounded costs to exclusion of all algebraic systems on the enlarged tuple.

For Objective 1, [the uniform slice theorem](../claims/Yin_C_F0346_v1.md#decision-reviewed) establishes \(\mathsf A\Leftrightarrow\mathsf S\) for arbitrary finite correlated normal generating tuples.
If \(\xi_i=\partial_i^*(\Omega\otimes\Omega)\), the two slices of the represented starred derivation have operator-norm-to-\(L^2\) cost at most \(C\|\xi_i\|_2\) with an absolute \(C\).
Both the original canonical \(D_i=-\overline{(\mathrm{id}\otimes\tau)\partial_i}\) and its actual Hilbert adjoint are defined on every \(a\Omega\) with \(a\in M\).
Their generator-first commutators there are \([X_j,D_i]=\delta_{ij}P_\Omega\).

For \(u\in L^0(M)\), let \(Q=(s,a,b,t)\) denote a bounded regular fraction with \(u=s^{-1}a=bt^{-1}\).
Membership in the division closure of the unstarred generator algebra is equivalent to [existence of a common fraction and finite-rank boundary solution](../claims/Yin_C_F0068_v1.md#statement).
It is also equivalent, for every such fraction, to finite rank in all coordinates of the [specified fraction commutators](../claims/Yin_C_F0068_v1.md#dual-specializations) on \(\{q:bq,tq\in\operatorname{Dom}D_i\}\).
In the finite-rank case the negatives of their bounded closures solve the operator-first boundary equation in Objective 1.
At a fixed fraction, the generator-first canonical and supplied systems have the [same finite-rank closures](../claims/Yin_C_F0075_v1.md#fractions-and-exact-finite-rank-transfer), and the rank in each coordinate is independent of the fraction.

The proof uses the [finite lattice reduction](../claims/Yin_C_F0339_v1.md#decision-reviewed) to recover each discrete mixed derivative from relative models supported on separated circles.
On each such model the liberation mass vanishes on the square of each individual label.
The [larger-disk matrix estimate](../claims/Yin_C_F0346_v1.md#a-positive-matrix-on-the-larger-disk) bounds the negative angular form on disks of comparable local mass, uniformly in the number and masses of the circles.
The remaining disks are controlled by the [integrated density square estimate](../claims/Yin_C_F0337_v1.md#disks-of-small-local-mass) using only the actual vacuum.
Both directions of the lattice comparison have absolute constants.
The [research strategy](../strategies/Yin_S_F0026.md#route) retains the exchange-pair, corner and projection reductions, marginal examples and earlier sufficient conditions with their fixed proofs.

After the [completion decision](#decision-complete-comparison), a separate reviewer inspected the adopted chain from the actual core and adjoint domains through both fraction tests and both arbitrary-tuple counterexamples.
The [post-completion finding](../audits/reviews/Yin_R_F0354_v1.md#finding) confirms the original contract at its stated scope.

## Starting evidence

The earlier [synthesis in L_F0050 v5](../ledger/Yin_L_F0050_v5.md) records the special cases and distinguishes boundary solvability from specified fraction commutators.
Reuse the following inputs at their recorded scopes:

| Input | Role and limit |
| --- | --- |
| [C_F0069](../claims/Yin_C_F0069_v1.md#statement), [C_F0070](../claims/Yin_C_F0070_v1.md#statement) | Automatic norm continuity, actual starred derivations for normal tuples, the normal strong-domain-to-ACSY implication, and the exact canonical right-domain comparison under ACSY. The right-domain comparison alone is not a two-domain conclusion. |
| [L_F0050 v3](../ledger/Yin_L_F0050_v3.md) | The fixed selfadjoint, scalar-normal, mixed selfadjoint/unitary, bounded rational-adjoint and elliptic-coordinate results, with their original C/R evidence and exact limitations. |
| [C_F0072](../claims/Yin_C_F0072_v1.md#statement) | Two bounded contractions imply actual vacua and both canonical full domains. These two bounds must be established, not inferred from the vacuum condition alone. |
| [C_F0131](../claims/Yin_C_F0131_v1.md#statement) | A square-summable phase sufficient condition and a universal phase-lifting obstruction; the negative models do not satisfy the rank-one dual identities. |
| [C_F0073](../claims/Yin_C_F0073_v1.md#statement), [C_F0132](../claims/Yin_C_F0132_v1.md#statement) | Exact normal-tuple left-contraction reductions through adjoint tuples and the specified normal \(L^1\)-valued map; the general range gain remains open. |
| [C_F0128 v2](../claims/Yin_C_F0128_v2.md#statement), [L_F0049](../ledger/Yin_L_F0049_v1.md) | Small-domain counterexamples and failed nonnormal tests. Their weaker premises must not be substituted for \(\mathsf F\) or the full ACSY hypothesis. |
| [C_F0074](../claims/Yin_C_F0074_v1.md#statement) | The accepted nonnormal rationality obstruction described above, not a hypothesis-separation example. |

The selected C decisions and their fixed R records own proof acceptance.
This Task registers the comparison problem and does not create a new mathematical review of those inputs.

## Execution

Local execution requires separate preparation of `execution/Yin_E_F0011.md` under the execution rules.
The lifecycle recorded here does not activate a local run.
The mathematical route and its intermediate results are recorded in [S_F0026](../strategies/Yin_S_F0026.md#route).
Registration itself recorded no execution period or usage allowance.
Ordinary manuscript editing and Git delivery are not part of this contract.

## Current decision
[Selected decision](#decision-complete-comparison)

## Lifecycle and completion

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-14T16:11 |
| status | active |
| authority | Yin explicitly requested a new F-line Task comparing the C_F0024 full bounded-vector domain condition with ACSY24 Proposition 3.5, for normal analytic rationality and general-tuple maximal Delta. |
| reason | The exact comparison remains unresolved at the requested generalities; existing accepted results and counterexamples provide a substantial starting basis. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Contract](#contract) | Both comparison objectives, the three distinct hypotheses, full quantifiers, scope boundaries and all completion criteria above. |

### Decision pause-after-round

| Field | Value |
| --- | --- |
| date | 2026-11-14T16:06 |
| status | paused |
| authority | Yin directed the main agent to finish the current exploration round and then pause the Task. |
| reason | The arbitrary-tuple comparison is resolved. The converse for arbitrary correlated normal tuples remains open at the uniform projection estimate above. Resume research only on Yin's explicit instruction. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Contract](#contract) | Both original comparison objectives, their operator domains and the independent review required for completion. |

### Decision resume-normal-converse

| Field | Value |
| --- | --- |
| date | 2026-11-16T14:54 |
| status | active |
| authority | Yin explicitly resumed F0011 to pursue the converse for arbitrary correlated normal tuples. |
| reason | The implication from actual starred conjugate variables to strong duals remains open under the original normal-tuple hypotheses. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Contract](#contract) | Both original comparison objectives, their operator domains and the independent review required for completion. |

### Decision complete-comparison

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:56 |
| status | completed |
| authority | Completion of Yin's resumed F0011 research under the original contract and its independent review requirements. |
| reason | The unrestricted normal implication and both fraction criteria are proved with the original canonical domains. Both directions of the arbitrary-tuple comparison are separated by actual examples. R_F0353 independently checked the full contract and all selected inputs. |

| Relation | Target | Scope |
| --- | --- | --- |
| contract | [Original F0011 contract](#contract) | Finite normal equivalence, both rationality tests, arbitrary-tuple maximality hypotheses, actual domains and existential quantifiers. |
| support | [General normal equivalence](../claims/Yin_C_F0346_v1.md#statement) | Original starred hypotheses, canonical domains, generators and every-fraction conclusions. |
| support | [Proof of the normal converse](../claims/Yin_C_F0346_v1.md#argument) | Enlarged-disk estimate, lattice transfer, restoration of both canonical domains and compatibility. |
| support | [Actual tuple excluding all bare duals](../claims/Yin_C_F0225_v1.md#all-bounded-duals-and-the-separating-tuple) | Countable assembly and a free extension exclude every algebraic bare system under actual ACSY. |
| support | [Strong tuple without any normalized starred derivation](../claims/Yin_C_F0133_v1.md#statement) | A bounded full-Hilbert-space strong dual coexists with failure of the normalized starred derivation. |
| support | [Bare maximality](../claims/Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors) | The full bounded-vector bare-domain commutator suffices for maximal Delta. |
| support | [Actual starred maximality](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 applies to the actual adjoint on the represented starred core. |
| support | [Existential fraction criterion](../claims/Yin_C_F0068_v1.md#statement) | Some bounded regular fraction has a finite-rank solution of the boundary equation. |
| support | [Specified fraction operators](../claims/Yin_C_F0068_v1.md#dual-specializations) | Every-fraction operator realization with its actual domain, sign and numerical rank. |
| support | [Canonical fraction comparison](../claims/Yin_C_F0075_v1.md#fractions-and-exact-finite-rank-transfer) | Supplied and canonical fraction operators agree on bounded vectors and share their finite-rank closures. |
| support | [Nonnormal rationality boundary](../claims/Yin_C_F0074_v1.md#statement) | The circular example rules out dropping normality from the prescribed commutator criterion. |
| review | [Independent full-contract finding](../audits/reviews/Yin_R_F0353_v1.md#finding) | Whole contract and the complete selected support for both original objectives, including the source and review limits in the finding. |

---
author: Yin
---
# Review of the finite word tests for derivations and full-domain duals

## Scope and arrangement

An agent outside the development of C_F0201 independently reviewed its candidate decision dated 2026-11-13T09:35 for Yin on 2026-11-13T09:39 UTC.
The inputs were the fixed statement and argument, their declared mathematical interfaces and the definitions of the three systems in the [Task contract](../../tasks/Yin_T_F0011_v1.md#contract).
The reviewer received the requested coverage without development discussions, exploration notes, author explanations or prior findings on this candidate.
The draft cited for the history of the word-cut method was unnecessary because the fixed proof contains that argument.
The cited project results were used at their established statements, and the Blackadar theorem was used at its inspected source scope.

## Whole-proof finding

The complete statement and argument of C_F0201 v1 hold with the stated optimal norms, quantifiers and order of limits.

For a cut with surrounding words \(a,b\) and a simple tensor \(u\otimes v\), its vacuum pairing is \(\tau(au)\tau(vb)=\langle u^*\otimes v^*,a\otimes b\rangle\).
The componentwise adjoint extends antiunitarily, so this calculation permits arbitrary Hilbert tensor values.
The functional of the unstarred cuts factors through the joint image in (1) even when the displayed seminorm vanishes, and its norm there is the supremum of the increasing finite-degree bounds.
Riesz on the closure gives the least-norm representing vector, and the sign \(K_j=-L_j^\sharp\) leaves precisely the pairing with the represented polynomial.
For a relation \(r(X)=0\), testing \(urv\) kills both outer Leibniz terms and pairs the surviving derivative with \(u(X)^*\otimes v(X)^*\).
The adjoints of polynomial words span a dense subspace on each leg, hence the derivative of the relation vanishes.
The descended map on the full represented star algebra has the required generator values and the actual vacuum-adjoint pairing on its dense Hilbert domain.
Conversely every such witness represents the same functional by \((\xi,(-K_j^\sharp)_j)\), proving attainment and optimality.

Projecting to \(V_{n+1}\) preserves both scalar products in (2) because \(h,X_j^*h\in V_{n+1}\).
Feasible minimizers exist in finite dimensions, and any bounded full-domain solution gives the same tests after restriction and projection.
For bounded optimal norms a common diagonal subsequence on the countable words has weak limits in \(H\).
Each finite represented linear relation already vanishes on the tails, and lower semicontinuity preserves the operator-norm input bound for every linear combination.
Polynomial test vectors therefore give the Hilbert-vector commutator on the dense star algebra of \(B=C^*(X)\), and operator-norm continuity extends that equation to \(B\).

The unital representation of \(B\) has bicommutant \(M\), so the kernel of its normal bidual extension is complementary to a central summand normally isomorphic to \(M\).
The normal extension of \(\tau|_B\) is \(\tau\pi\), and multiplication by \(\iota(X_j)\) is weak-star continuous.
Reflexivity of \(H\) thus extends the vector identity to \(B^{**}\), where restriction along \(j\) intertwines the left multiplications and sends \(\tau\pi\) to \(\tau\).
The resulting ultraweak-to-weak solution obeys the same bound, and the compression inequality forces equality with the global infimum.
This reasoning allows different values on the original \(B\) after passage to the represented summand and permits an unrestricted value at \(1\).
If the finite-level bounds diverge, the compression inequality excludes every bounded solution.

For fixed \(n\) the restrictions of left multiplication defining \(N_l\) are increasing norms, with pointwise limit the faithful represented norm by Hilbert density.
On the compact operator-norm sphere in \(V_{n+1}\), the Lipschitz bound makes convergence uniform.
The resulting two-sided multiplicative estimate for the feasible optimization gives its infimum in \(l\) before taking the supremum in \(n\), including the zero value and infeasible levels.
All finite inner products use bounded-length words, and faithfulness identifies each Gram null space with the actual represented relations.
Thus the finite input data also determine the limiting optima.

For a normal affine combination \(Y\), division by a nonzero coefficient gives the exact rank-one commutator required by C_F0069 Part A with complex-linear maps on all \(M\Omega\).
Adding a commuting coordinate map to this normalized witness and taking the difference of two bounded maps gives boundedness for each zero coefficient as well.
A scalar coordinate makes its own rank-one commutator impossible on \(1\).
For normal tuples the same argument applies to the adjoint tuple, and Part 2 of C_F0075 gives precisely the strong existential conclusion with the Task's sign \(D=-E\).
For unrestricted tuples finite bounded-witness norms still imply the bare condition.
The question whether finite derivation bounds force the two sets of bounded-witness bounds on all correlated normal tuples remains open in this finding.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0201_v1.md#statement) | Both optimal tests, joint moments, strong normal and bare affine-normal equivalences, and arbitrary-tuple sufficiency. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0201_v1.md#argument) | All four proof sections, including relation descent, Hilbert adjoint, compactness, normal transfer, ordered limits and existential scope. |
| [Whole-proof finding](#whole-proof-finding) | [Represented summand](../literature/Bla06/Yin_U002.md#bla06-u002) | Universal-bidual representation and central ideal applied to the unital represented inclusion, using the inspected theorem without a new proof audit of Blackadar. |
| [Whole-proof finding](#whole-proof-finding) | [Automatic continuity](../../claims/Yin_C_F0069_v1.md#statement) | Part A with a normal affine combination, normalized nonzero coordinate and difference argument for a commuting coordinate. |
| [Whole-proof finding](#whole-proof-finding) | [Adjoint tuple](../../claims/Yin_C_F0075_v1.md#statement) | Part 2 on a tuple of normal generators with bare witnesses for both the original and adjoint tuples. |

---
author: Yin
---

<a id="normal-phase-schur-boundary"></a>
# Normal phase Schur boundary and direct rational-state obstacles

Date: 2026-09-29.
Human author: Yin.
Exploration by counterexample review agent.
Exploratory note only; no Claim allocation, proof of the general criterion, or counterexample is asserted.
Exact starting assumptions remain C_F0025 (recorded assessment 3).
The independently reviewed C_F0055/C_F0056 results are accepted at their recorded scopes.

## 1. A phase unitary on L2 is not an operator Schur bound

The normal phase is

    k(z,w) = (conjugate(z)-conjugate(w))/(z-w).

Its absolute value is one off the null diagonal, which gives a unitary multiplier on the coarse Hilbert tensor product.
That fact cannot be promoted to boundedness on an arbitrary operator norm or Haagerup/projective tensor space.
In particular, k is the divided difference of f(z)=conjugate(z).

Primary source checked: A. B. Aleksandrov and V. V. Peller, *Operator Lipschitz functions*, arXiv:1611.01593v1, [exact source](https://arxiv.org/pdf/1611.01593v1).
The [selected source note](../audits/literature/AP16/Yin_U001.md) records actual coverage.
Theorem 3.3.2 (printed p. 53) characterizes commutator Lipschitz functions by universal Schur multipliers of their divided differences.
Theorem 3.3.3 on the same page states that such functions have a complex derivative at every nonisolated point of their closed spectral set.
Its proof on the following page uses the triangular-sign Schur multiplier obstruction.
These selected statements and that proof mechanism were inspected; no complete-source audit is claimed.

On a closed disk, complex conjugation has no complex derivative at an interior point.
Therefore its phase divided difference is not a universal Schur multiplier.
This is a precise obstruction to a uniform operator-norm lifting argument.
It does not show that a particular fixed trace, polynomial core, or actual-vacuum tuple fails the desired contraction estimate.
Ordinary operator Lipschitz continuity of conjugation (which does hold with constant one for normal operator differences) is a different condition and is not contradicted.

## 2. What existing minimal-state results actually require

The current C_F0007 proof obtains rational L2 derivative factors from already bounded finite commutators, then extracts the left and right minimal states by algebraic tensor quotient arguments.
C_F0010 starts with those states already in L2 and bounded duals.
Neither argument starts from bounded scalar output alone under the C_F0025 small-core hypotheses.

The [affine two-state extraction](../claims/Yin_C_F0062_v1.md#5-minimal-affine-states-from-l2-rational-derivative-tensors) likewise assumes L2 formal rational derivative tensors; it does not derive them from scalar output or assert that the entire inverse is L2.
A stronger scalar-output-to-full-inverse bootstrap uses bounded selfadjoint generators, normalized bounded duals on all H, polynomial invariance, and actual bounded polynomial adjoint images.
Its canonical denominator recovery chooses

    t=(1+f*f)^(-1/2),  zeta=t^(-1)p in L2,

and applies the dual to bounded-denominator multiples of zeta.
Under C_F0025, mere L2 membership of zeta supplies no original dual-domain membership.
Consequently this bounded-dual denominator recovery cannot presently be transplanted to this task's exact small-core hypotheses.
C_F0012 separately shows that even L2 minimal states need not be bounded; it prevents replacing the target by bounded realization.

## 3. A weak polynomial-fraction identity and its unresolved graph step

Suppose a,b are unstarred polynomials, a is regular, f is bounded, and af=b.
For a fixed normalized original dual D, let T_a=[D,a] and T_b=[D,b] denote their bounded finite-rank extensions.
Since a* preserves Dom D* with

    D*(a*p)=a*D*p-T_a*p,

the original weak commutator form satisfies, for polynomial tests p,q,

    beta_f(a*p,q) = <p,(T_b-T_a f)q>.

This identity is a direct calculation in existing Hilbert vectors.
Its right side is bounded finite rank.
Since a is regular, a*P is dense in H: first approximate arbitrary vectors by P and then use the dense range of a*.

However, the identity only controls beta_f on first tests a*P.
It does not show that a*P is dense for the graph norm of the actual D*, and beta_f need not yet be continuous in the H norm of its first test.
A discontinuous functional on a dense test domain can vanish on an H-dense subdomain.
Thus Hilbert-space density alone does not justify dividing this identity by a or extending the finite-rank representative to all original polynomial tests.
A minimal affine pencil replaces this scalar multiplication by a matrix version and retains the same graph issue.

This observation is an identified missing lemma, not an abstract counterexample satisfying C_F0025.
A direct rational criterion could still succeed by proving the requisite graph-density or finite-state cancellation statement from the actual conjugate variable and normality hypotheses.

## 4. Restrictions on sandwich constructions

The earlier scratch search recorded why h b h* with selfadjoint b has a real relative derivative in the second coordinate; proposing a hidden non-L2 inverse h cannot bypass that coordinate's actual vacuum requirement.
Replacing b by a generic normal nonselfadjoint element destroys normality of the sandwich.
A unitary conjugate preserves normality, but does not preserve the needed bounded rational recovery formula with a non-L2 hidden state.

No actual correlated tuple satisfying all C_F0025 hypotheses and violating the bounded rational weak-form converse has been constructed in this branch.

## 5. A positive example at the same Schur obstruction

The [local disk-law calculation](../audits/literature/AP16/Yin_U001.md#local-disk-law-comparison) gives a positive rationality example satisfying the original hypotheses at the same universal Schur obstruction.
Free copies are covered by C_F0055 (recorded assessment 2) as well.
This explicit example prevents treating the Schur boundary as a refutation of T_F0001.

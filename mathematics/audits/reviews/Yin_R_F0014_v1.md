---
author: Yin
---

# Yin_C_F0025: Complete Review of the Small-Core Weak Rationality Criterion

<a id="small-core-rationality-finding"></a>

## Actual review relationship

The reviewer developed the related preliminary weak-commutator argument and C_F0026 construction, and checked the compact refinement in shared development before integration. This disclosed relevant mathematical context and contribution makes the full retained finding self-reviewed.
The original independent descriptions, dates and full checked scope are preserved as historical facts; no isolated arrangement or new review is asserted.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Retained complete finding](#small-core-rationality-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Retained complete finding](#small-core-rationality-finding) | [Exact statement](../../claims/Yin_C_F0025_v1.md#statement) | Complete compact small-core theorem and operator/coarse equivalence, automatic maximal Delta and Hilbert--Schmidt upgrade, exact normal phase/tensor descent, with the arbitrary bounded-fraction converse and all-M domain claims withheld. |
| [Retained complete finding](#small-core-rationality-finding) | [Exact argument](../../claims/Yin_C_F0025_v1.md#2-normalization-and-the-exact-acsy24-interface) | Complete compact small-core theorem and operator/coarse equivalence, automatic maximal Delta and Hilbert--Schmidt upgrade, exact normal phase/tensor descent, with the arbitrary bounded-fraction converse and all-M domain claims withheld. |

- Date and reviewer: 2026-09-10; the reviewing agent.
- Target: [Yin_C_F0025](../../claims/Yin_C_F0025_v1.md#yin_c_f0025), all seven sections, authored by another AI agent.
- The initial Hilbert-Schmidt-hypothesis artifact was independently reviewed.
- The compact-hypothesis artifact was subsequently read and checked in full.
  The reviewer requested that the compact rigidity proof name the positive operator C-star C explicitly; the mathematical argument already had that meaning.
  The reviewer verified the completed wording clarification after the full compact-version review.
  That clarification was the only further target edit and changes no mathematical assertion or argument.
- Relevant research context: the user-requested smaller starred polynomial domains in [ACSY24-U001](../literature/ACSY24/Yin_U001_v1.md#acsy24-u001), within the expanded normal-dual rationality investigation.
- Disclosure: this reviewer previously developed a related selfadjoint weak-commutator argument and separately constructed [Yin_C_F0026](../../claims/Yin_C_F0026_v1.md#yin_c_f0026).
  The reviewer did not author Yin_C_F0025 or its normal-coordinate spectral reconstruction.
  The coordinating agent proposed the compact refinement using a related rigidity argument; this reviewer independently checked that refinement before the author integrated it.
  This is a separate review of the entire written artifact, with the related preliminary work disclosed; it is not a claim of independent rediscovery or external human review.
- Starting assessment: complete proof draft submitted for independent review.
- Outcome: the stated one-sided theorem and its operator/derivation equivalence are correct under the specified compact small-core hypotheses; the required Hilbert-Schmidt commutators follow from them.
  No mathematical or domain correction is required.
  The responsible Claim materials and their selected decisions own the current mathematical and review assessments.

## Obligations and Findings

| Obligation | Decisive evidence checked | Finding |
| --- | --- | --- |
| The initial vacuum-adjoint assumption is sufficient | Polynomial commutators have bounded compact extensions; the explicit adjoint vector is in H for every starred polynomial | Full starred polynomial adjoint domain and closability follow before any Hilbert-Schmidt claim |
| Normalization is legitimate for an unbounded vacuum vector | Right multiplication by eta has adjoint p maps to p eta-star on bounded tests; its two weak-form terms cancel tracially | Normalization preserves all weak representatives without assuming eta bounded |
| Maximal Delta does not require the Hilbert-Schmidt upgrade first | Selfadjoint doubling and resolvent regularization yield strongly convergent bounded approximate dual commutators; finite-rank trace tests suffice | No circular dependence on atomlessness or the later source derivation |
| Compact commutators become Hilbert-Schmidt | Subtract the explicit Hilbert-Schmidt phase solution; a compact operator commuting with an atomless normal coordinate must vanish | Exact adjoint-coordinate commutators and Hilbert-Schmidt membership follow |
| The operator hypotheses match the actual ACSY24 derivations | After the upgrade, the commutator extension transports through Theta to a well-defined outer derivation; normalization identifies its contraction and vacuum adjoint | Exact source interface, with no all-M assumption |
| Maximal Delta gives the needed atomlessness | Each X_i minus c is the evaluation of a nonzero field element and hence has zero kernel | Every normal coordinate has nonatomic scalar spectral distribution |
| The coarse coordinate difference is injective on the entire tensor space | Its diagonal kernel projection lies in the product spectral algebra and has zero faithful product trace | No unexamined orthogonal-complement component remains |
| Normality determines every adjoint derivative | Differentiate X_i X_i-star equals X_i-star X_i; the bounded divided-difference kernel solves the resulting equation; injectivity gives uniqueness | Equation (14), including all zero cross derivatives, is correct |
| Inner and outer tensor actions are not confused | The inner operator commutes with outer module actions and agrees with the coordinate difference on the abelian subspace | Their sum gives the universal inner derivation on the entire starred algebra |
| The fundamental K identity holds on the actual small core | Contract the derivation identity and retain the extra a term from differentiating a X_i | K equals (1-d)I minus P on the core; its formal adjoint has the correct bounded value |
| Weak commutators imply an actual bounded tensor identity | All operator and adjoint inputs in the expansion are starred polynomials; bounded finite-rank representatives permit extension by density | No action of D on f times a polynomial is presumed |
| Tensor descent reaches the holomorphic free field | Balance algebraic L2 tensors over F and apply a right-F basis functional | Bounded f belongs to affiliated F, without adjoining X-star to F |
| Domain interpretations do not exceed the proof | Closed-domain invariance implies the weak condition, while the reverse is explicitly withheld | No hidden assertion that the polynomial core is an adjoint graph core |

## 1. Adjoint Domains, Normalization, and the Source Interface

The commutator product rule only uses inputs in the invariant starred polynomial algebra.
Each word commutator is initially a finite sum of bounded left or right compositions with a compact generator commutator.
If two words or polynomial expressions define the same element, the resulting commutators agree on the dense core; uniqueness of their bounded extensions removes any presentation ambiguity.
Thus the target's maps T_i,a are well-defined before any derivation is claimed.

The first displayed adjoint formula in Section 2 has the correct multiplication order.
For a polynomial a, applying the vacuum adjoint relation to a-star q and expanding the commutator gives

\[
D_{i,0}^*a
=aD_{i,0}^*\Omega-T_{i,a^*}^*\Omega.
\]

Both terms are H vectors because a is bounded and T_i,a-star is bounded.
They represent the functional in q, so the formula actually establishes the stated adjoint domain; it does not merely name a formal candidate.
Density then proves closability.

For eta equal to D_i,0 Omega, the map N_i p=p eta has adjoint N_i-star p=p eta-star on the polynomial test space.
The subtraction retains the vacuum-adjoint and generator-commutator hypotheses.
In the weak form, the two extra scalar quantities are

\[
\tau(\eta_i p^*f q)
\quad\text{and}\quad
\tau(p^*f q\eta_i),
\]

which agree by the tracial L2 pairing with bounded factors.
No boundedness of eta, closure-domain equivalence after normalization, or strong commutation of two unbounded operators is needed.
The subsequent proof concerns the invariant weak condition.
The final closed-domain interpretation is explicitly returned to the original operators.

The tensor convention agrees with [Yin_C_F0002](../../claims/Yin_C_F0002_v1.md#yin_c_f0002): Theta(g tensor h) has bra J h, and its outer right module action is multiplication of the second factor on the right.
After the compact-to-Hilbert-Schmidt argument described below, Theta-inverse of T_i,a is an outer derivation, its contraction is the normalized dual, and its vacuum functional is represented by D_i,0-star Omega.
The target therefore supplies exactly the starred algebra, Hilbert tensor codomain, coordinate values and vacuum-adjoint condition in ACSY24 Proposition 3.5.
The converse construction also passes: contraction of a source derivation has commutator Theta(partial_i a), and the displayed adjoint formula gives the required vacuum and polynomial adjoint domains.

The reviewer read the local [ACSY24 audit](../literature/ACSY24/Yin_U001_v1.md#acsy24-u001), including its regularization reconstruction, and the relevant [MSY23 realization interface](../literature/MSY23/Yin_U004_v1.md#msy23-u004).
The audit's weaker bounded-commutator regularization, reconstructed in the revised target, provides maximal Delta before any Hilbert-Schmidt conclusion.
MSY23 then provides the embedded division ring at its existing source-inspection scope.
No assertion about all bounded vectors being in the dual domains is imported from either interface.

### Maximal Delta before the Hilbert-Schmidt upgrade

The starred algebra is a graph core for the specified closure by definition.
Graph approximation extends its bounded commutator identities and proves invariance under every starred polynomial.
Pairing against that closed domain, and using the commutator with the adjoint polynomial, proves the corresponding adjoint-domain invariance and the sign $[D^*,a]=-T_{i,a^*}^*$.

These facts justify selfadjoint doubling and the block commutator C_j in the revised Section 2.
The two-resolvent calculation for S times R_t only uses invariance of Dom S and avoids an unsupported assertion about Dom S-squared.
The spectral families R_t and square-root-t times S R_t have the stated strong limits and uniform bounds.
They give strong convergence of the bounded commutators even before compactness or Hilbert-Schmidt membership is used.
Taking the lower-left block supplies the correct approximation $D(1+tD^*D)^{-1}$.

In the cycle calculation every operator paired with the finite-rank Q_k is bounded.
Moving the commutant multipliers through X_k and using finite-rank trace cyclicity converts the sum to the trace of the original zero cycle times a bounded operator.
Strong convergence suffices for each finite-rank trace functional.
Its limit is minus Tr(Q_i V P W), whose matrix coefficient tests are W-star Omega and V Omega.
The two independent dense commutant orbits force Q_i to vanish.
The accepted finite-cycle characterization then proves maximal Delta without using the later spectral or Hilbert-Schmidt arguments.

### Compact rigidity and the exact adjoint commutators

After maximal Delta gives the atomless normal coordinate laws, the phase vector v_j belongs to the abelian Hilbert tensor product and S_j=Theta(v_j) is Hilbert-Schmidt.
Its commutator is $[X_j,S_j]=[X_j^*,P]$.
The original bounded compact extension B_ij satisfies $[X_j,B_{ij}]=\delta_{ij}[X_j^*,P]$, obtained directly from the differentiated normality relation.
Thus C=B_ij minus delta_ij S_j is compact and commutes with X_j.

Bounded Fuglede gives commutation of C with X_j-star.
Taking adjoints also makes C-star commute with X_j and X_j-star, so the positive compact operator C-star C commutes with both.
If C were nonzero, a positive nonzero eigenvalue of C-star C would have a nonzero finite-dimensional spectral eigenspace reducing X_j.
The restriction of X_j would then have an eigenvector, contradicting injectivity of every X_j minus c.
Hence C=0, proving the exact Hilbert-Schmidt commutators before Theta-inverse is applied to the polynomial commutators.
This establishes the claimed equivalence of the compact operator hypotheses and the source derivation hypotheses for normal tuples without a logical cycle.

## 2. The Normal Spectral Reconstruction

Maximal Delta and the free-field embedding precede the spectral argument.
For every complex c, x_i minus c is nonzero in the free field, so its evaluated inverse exists in U(M).
The normal operator X_i minus c therefore has zero spectral kernel, and faithfulness makes every singleton have zero scalar spectral measure.

On the coarse tensor space, lambda(X_i) tensor I and I tensor rho(X_i) are commuting normal actions in the finite von Neumann algebra lambda(M) spatial-tensor rho(M).
That algebra has the faithful product trace.
Restricted to the abelian spectral algebra generated by these two actions, the joint scalar law is the product of the two coordinate laws.
The kernel projection of their difference is the joint projection of the diagonal.
Its trace is zero because the coordinate law is nonatomic; faithfulness makes the projection zero on the whole coarse Hilbert space.
Thus injectivity is not limited to the smaller abelian L2 tensor subspace.

The sign in equation (12) was checked by expanding both sides of the normality relation with the outer Leibniz rule:

\[
\delta_{ij}(1\otimes X_i^*)+X_i\cdot\partial_jX_i^*
=\partial_jX_i^*\cdot X_i+\delta_{ij}(X_i^*\otimes1).
\]

Moving the terms gives exactly the coordinate-difference equation stated in the proof.
The kernel (bar z minus bar w)/(z minus w) has absolute value one away from the null diagonal, so it is an actual vector in the abelian Hilbert tensor product.
It solves that equation there.
Injectivity on the complete coarse tensor product then gives all of equation (14), including the vanishing result for j different from i.
This checks existence and uniqueness separately and rules out an additional component outside the abelian subspace.

As boundary checks, on a selfadjoint spectral support the kernel is one off the diagonal, while on the unit circle it equals minus z-inverse w-inverse.
These recover the selfadjoint derivative and the Haar inverse derivative used in Section 6.

## 3. The Small-Core Fundamental Identity

The operator called B_i-in in equation (15) uses right action on the first leg and left action on the second.
Those are the actions commuting with all outer module multipliers.
On the abelian coordinate subspace they agree with the corresponding outer coordinate actions, which justifies equation (16); this equality is not asserted on the entire tensor space.

It follows that the sum of B_i-in partial_i is a derivation.
The forced adjoint derivative identities make its values correct on both X_j and X_j-star.
Agreement on these starred generators, followed by the Leibniz rule, proves agreement on the whole actual core, including any relations in that algebra.
No density of the holomorphic polynomial subalgebra is needed.

The contraction in equation (19) retains the indispensable degree-independent term:

\[
D_{i,0}(aX_i)
=(\mathrm{id}\otimes\tau)((\partial_i a)\cdot X_i)+a.
\]

Traciality in the second leg identifies the contracted inner second action with the first term on this right-hand side.
Thus contracting the left side of equation (17) gives K_0 a plus d a, and the contracted right side is a minus tau(a) Omega.
The result is exactly K_0 a=(1-d)a-Pa.
Every input to an unbounded D_i,0 is a starred polynomial in this computation.

For its formal adjoint, R_i-star p remains a starred polynomial, so D_i,0-star R_i-star p is defined.
The other term only applies a bounded right multiplier to an existing H vector.
Pairing against the dense polynomial domain identifies the sum with the adjoint of the bounded operator (1-d)I-P.
No separate closed-domain invariance under right multiplication is required or inferred.

## 4. Weak Forms, Finite Tensors, and the Exact Conclusion

For general normal X_i, the first test argument in the weak expansion must be R_i-star p, while the second argument is R_i q.
The target makes exactly these choices.
Moving the bounded right multipliers, which commute with left f and f-star, gives the formal adjoint sum in the first term and K_0 in the second term.
The bounded K identity then cancels its scalar multiple of the identity and leaves fP-Pf with the stated sign.
The expansion only tests D_i,0 and its adjoint at their justified polynomial inputs.
In particular it does not assume f q lies in a dual domain.

Both sides of equation (22) are bounded once the weak forms have the stipulated representatives.
Density therefore makes it an operator identity, rather than only a formal identity of quadratic forms.
The finite-rank-to-algebraic-tensor step is the exact Yin_C_F0002 correspondence and does not confuse a general Hilbert tensor with a finite tensor.
It gives f tensor 1 minus 1 tensor f with precisely the two inner coordinate actions in equation (23).

The injection from H to U(M) induces an injection on complex algebraic tensor products because the base ring is the field of complex numbers.
Balancing over the holomorphic free field F kills each generator difference without adjoining its adjoint.
If f were outside F, the two vectors 1 and f would be right-F linearly independent, because F is a division ring.
The indicated basis functional then sends the balanced equality to 1=0.
The argument permits zero divisors in U(M), assumes no continuity of the basis functional, and uses no bounded inverse theorem.

The representative condition includes both Hilbert-norm boundedness of the form and finite rank.
The alternative finite-matrix formulation in Section 1 is equivalent: boundedness first gives a bounded operator, and density transfers the uniform finite-test rank bound to that operator.
Algebraic rank on an unbounded form is not substituted anywhere.

For the closed-domain sufficient condition, polynomial q belongs to the original closed dual domain; its image f q belongs by the extra invariance assumption.
The adjoint pairing then identifies the weak form with the stated commutator representative.
The reverse implication is correctly withheld: a graph core for D_i is not automatically a graph core for D_i-star, so weak tests confined to that core do not by themselves establish membership in Dom D_i.

## Dependency and Scope Assessment

Yin_C_F0025 proves the finite-rank-to-affiliated-rational implication for bounded f under compact adjoint-generator commutators on the small core, with automatic maximal Delta and automatic Hilbert-Schmidt membership.
For normal tuples, its normalized form consequently matches the actual ACSY24 small-core derivation hypotheses.
It proves neither arbitrary bounded-fraction well-definedness nor the rational-to-weak-finite-rank implication at those smaller domains.
The all-M theorem Yin_C_F0024 is referenced only as a stronger sufficient framework, not used to prove this new small-core implication.
The selfadjoint full-equivalence corollary retains its separately established Dab10 domain estimates, and the Haar full equivalence retains its bounded duals.
These references introduce no dependency cycle into Sections 2-5.

Hilbert-Schmidt membership is used when transporting commutators into the coarse Hilbert tensor product and reconstructing the adjoint-coordinate derivatives.
It is derived from compactness, normality and atomlessness before those steps, rather than assumed or replaced by mere boundedness.
The bounded-adjoint-commutator obstruction in Yin_C_F0026 therefore has its distinct scope and is not presented as a refutation of Yin_C_F0025.

## Verification Limits and Outcome

This review consists of a full reading of the written theorem, independent reconstruction of the algebra, spectral and domain arguments, and inspection of the named local source interfaces.
The original source PDFs and the accepted general foundations were not newly audited here.
No new computation, numerical test, compilation, proof-assistant verification, external human review or historical-priority search was performed.
No target-file edit was made by this reviewer.

No unresolved mathematical correction remains under the stated hypotheses.
The reviewer recommends the assessments `proved` and `independently reviewed` for the precise one-sided Yin_C_F0025 theorem, while preserving the open full-converse and common-domain obligations identified in the target.

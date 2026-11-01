---
author: Yin
---
# Relative Fock degree bounds and target canonical domains: independent complete review

Date: 2026-10-14T19:13.
Human record author: Yin.
This is a separately organized agent review of the complete fixed [C_F0145 v1](../../claims/Yin_C_F0145_v1.md#statement), whose initial decision is dated 2026-10-14T19:07.
It covers the statement, all five argument sections and all five declared direct inputs at the interfaces below.

The reviewer did not develop the suffix-cut estimate, summable-degree theorem or nonlinear application.
The reviewer has worked on a separate normal-tuple branch and earlier developed C_F0072, an accepted dependency.
This finding is an independent review of C_F0145 and its use of C_F0072, not a new independent review of the original C_F0072 proof.
The explicit core-adjoint and weak-graph arguments in C_F0145 were reconstructed here.

The supplied context identified the developers, outlined the requested verification obligations and reported that the separate C_F0144 review had passed.
The reviewer read the fixed proof and direct inputs without consulting D_F0003 or its proof-generation dialogue, and formed these findings without reading the C_F0144 review report.
Prior familiarity with C_F0130 and C_F0072 did not replace rereading their invoked interfaces.
Human authorship does not represent personal human proof inspection.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0145 statement](../../claims/Yin_C_F0145_v1.md#statement) | Finite and summable total relative-degree hypotheses, quantitative bounds, original closure and actual adjoint domains, and both target canonical domains for every c>6. |
| [Conclusion](#conclusion) | [C_F0145 complete argument](../../claims/Yin_C_F0145_v1.md#argument) | All five sections, including full-M commutator extension, finite h-coordinate correction and target-core restriction. |
| [Conclusion](#conclusion) | [C_F0144 argument](../../claims/Yin_C_F0144_v1.md#argument) | Word cuts, actual reference-adjoint degree estimate, reducing spaces, square integrability of G inverse and its inverse expansion. Both target vacuum checks were also read and verified. No full-domain conclusion is attributed to this input. |
| [Conclusion](#conclusion) | [Miy22-U001](../literature/Miy22/Yin_U001.md#miy22-u001) | Fock model, standard semicircular normalization, Wick basis and reversal, and bounded right annihilation; the source unit's foundational-input and inspection limits are retained. |
| [Conclusion](#conclusion) | [C_F0072 statement](../../claims/Yin_C_F0072_v1.md#statement) | Actual core-adjoint formula and bounded Kaplansky/weak-graph restoration, with the stronger present bounds. Prior authorship of this dependency is disclosed above; this binding checks its use and the explicit present graph argument. |
| [Conclusion](#conclusion) | [C_F0142 statement](../../claims/Yin_C_F0142_v1.md#statement) | Generation, represented target derivations, exact inverse, F beta=1, starred value k and C_- minus kC. No all-bare-witness uniqueness or Hilbert--Schmidt range conclusion is imported. |
| [Conclusion](#conclusion) | [C_F0130 Section 5](../../claims/Yin_C_F0130_v1.md#5-projective-corrections-on-all-bounded-vectors) | Finite Q corrections on operator-norm-to-H maps, reversed coefficient composition and commutator identities; beta is not assumed projective. |

## Findings

### 1. Suffix-cut norm and the H-to-L1 estimate

For each k, the word u1v with exactly k letters 1 in v is reconstructed from (u,v), and every such pair occurs.
Thus the cut sends an orthonormal subset onto an orthonormal tensor basis and annihilates the complement.
Its norm is one.
Arbitrarily many letters 0 introduce no multiplicity.

The coefficient expansion uses U_v* in beta and U_v in the cut of q.
Consequently the trace pairing is exactly delta(v,v'), including words not invariant under reversal, and the ordered product is sum x_v a_v.
These are L2 products in L1.
The needed Holder estimate follows directly from trace duality and Cauchy--Schwarz:

\[
 \|xy\|_1=\sup_{\|z\|\le1}|\tau(zxy)|
 \le\|x\|_2\|y\|_2.
\]

Cauchy--Schwarz over v bounds a fixed suffix degree by ||q||2 ||beta^(k)||2; orthogonality over k=0,...,n gives sqrt(n+1).
No bounded Hilbert-tensor multiplication into H is used.

Finite Wick approximants preserve degree.
For fixed polynomial q, its finite derivative acts boundedly on the Hilbert beta variable, so contraction values converge in H and hence in L1 to the actual expression.
This proves the infinite coefficient case and the unique H-to-L1 extension.
It does not assert H-valuedness of that extension at every H input.

### 2. Actual vacuum, adjoints and original closures

Componentwise star and flip-star preserve total relative degree: reversal preserves the number of letters 1.
C_F0144's insertion maps therefore give the actual value partial*(beta*) with the stated bound.
The trace pairing in equation (12) has the correct componentwise star for the inner product linear in its second variable.

Conjugation gives delta_beta sharp = delta_(beta dagger), with vacuum v_beta*.
Expanding delta_beta(q* p) proves

\[
 E_{\beta,0}^*q=qv_\beta-E_{\beta^\dagger,0}q
\]

by actual pairing against every polynomial p.
Both terms are H vectors; thus the core lies in the actual adjoint domain and the operator is closable.

Pairing the H-to-L1 bound with p in M gives a functional of q bounded in its H norm.
Riesz representation is precisely the actual adjoint test and yields the sharper sqrt(n+1)||beta||2 bound on all M.
Applying this test to beta dagger and using its core-adjoint formula gives the factor 2 bound for E_beta.
This uses the other contraction's actual adjoint, not an implication from an L1 estimate to an H estimate.

Bounded polynomial approximants to p in M converge in H.
Their contraction values have a weakly convergent subnet by the new bound.
The graph of the original closure is a closed linear subspace, hence weakly closed, so the limit belongs to that original graph.
Lower semicontinuity gives the bound.
The all-M actual adjoint inclusion was proved separately.
No larger closed extension is substituted for the original closure; beta=0 and degree zero create no exception.

### 3. Summation and the nonlinear inverse

The weighted l1 hypothesis gives Hilbert convergence of beta and absolute convergence of the reference-adjoint values, also for beta dagger.
Closedness of the actual reference adjoint proves the limiting actual vacuum.
For each fixed polynomial, finite-coefficient insertion gives H convergence to the specified contraction.
Summing the L1 estimates and repeating the Riesz test gives W, followed by 2W.
There is no formal sum-adjoint interchange.

In C_F0144, bounded functions of s0 preserve the reducing relative-degree spaces, while one s1 changes the upper degree by at most one.
The opposite multiplication in F=(c+Z)G has the correct order.
Square integrability of G inverse follows from u=s+t, v=s/(s+t): the density upper bound becomes sqrt(v(1-v)) du dv on a bounded region.
Taking adjoints in the eta_n expansion gives exactly beta_n=c^(-n-1)G^(-1)(-Z)^n, still of total degree at most n.
For c>6 its geometric bound is summable with the sqrt(n+1) weight.
Thus the theorem applies even though h inverse is not L2 and beta need not be bounded or projective.

### 4. Full-M commutators and the finite correction

The reference core commutators follow from Leibniz and partial_1(h)=0, partial_1(S)=1.
Theta(beta) is a bounded Hilbert--Schmidt operator because beta is a Hilbert tensor.
To extend a core identity [K,x]=B to M, choose bounded polynomial p_alpha converging in H, take a weakly convergent subnet of Kp_alpha, and use

\[
 K(xp_\alpha)=xKp_\alpha+Bp_\alpha.
\]

Both graph limits belong to the original closed K, so the identity holds at p and xp.
Neither operator-norm density of the polynomial algebra nor boundedness of K on H is needed.

The product rule and fixed affiliated identities give [K,Y]=P and [K,Y*]=Theta(k) on M.
Right annihilation has [B_h,h]=P and [B_h,S]=0 with the stated sign.
All finite correction factors act on bounded vectors.
Pairing with q in M proves the correction-adjoint expression: each rho(a_l*)q is bounded and lies in Dom K*.
This is actual adjoint membership, not a formal operator product.

For finite C and any Hilbert tensor t, tracial cyclicity gives

\[
 Q_C(\Theta(t))=\Theta(tC).
\]

The elementary-coefficient calculation extends by finite summation and Hilbert continuity, without projective regularity of t.
With t=k this gives kC, not Ck.
Equation (21) follows, and negating L,K gives the generator-first convention and an actual strong system.

### 5. Both specified target canonical domains

C_F0142 gives target generation and represented derivations with exactly the generator and starred-generator values in equations (19)-(21).
Since K1=0, evaluating at 1 identifies the target contractions as Kp and Lp-pL1 on the target star algebra.
No unknown target derivation is applied to S or an affiliated inverse.

For eta=L1 in H, right multiplication p to p eta on M has actual adjoint q to q eta* by tracial pairing.
Both maps have operator-norm-to-H bound ||eta||2.
The normalized domain-M maps thus have actual adjoints on M, and their target-core restrictions are precisely the unclosed target canonical contractions.
Bounded Kaplansky approximation from that core and weakly closed graphs place all M in each original target-core closure.
Actual adjoint inclusions follow from the domain-M pairings.
This checks the two specified canonical operators, not merely existence of some strong system.

## Dependency and source limits

All five direct inputs were inspected at the scopes in the bindings.
The external Fock model is used through its registered retained Miy22 unit; trace and semicircular foundational inputs remain accepted at that unit's inspection limits.
The degree and suffix estimates are local proofs.
C_F0139 only explains why a previous kernel-only estimate does not apply; it is not a premise.
No desired full-domain conclusion is imported circularly from C_F0144 or C_F0142.

This review does not re-audit every foundational proof behind accepted dependencies, prove a result for arbitrary Hilbert coefficients, settle the general ACSY-to-full-domain implication, or certify novelty or formal correctness.
It establishes the finite and summable relative-degree theorem and its displayed application.

## Conclusion

The exact statement and complete argument of C_F0145 v1 pass this independent review.
No mathematical gap or source-applicability correction was found within the declared scope.
The result supports a `proved` and `independently reviewed` assessment upon adoption by its responsible decision.
The concrete tuple has A, S and F, with both specified target canonical closures and their actual adjoints containing M Omega.
Neither unrestricted general-tuple nor unrestricted normal-tuple comparison is settled.

---
author: Yin
---

# Self-review of the liberation-dual rationality criterion

Human record author: Yin.
Inspection: 2026-10-18T06:09.
Method and relationship: Codex authoring-agent self-review in the proof-development session.
The reviewer had C_F0079 v3 and v4, the earlier review, C_F0068 Part A, and the retained source interfaces.
This is not an independently arranged review or a review of the full T_F0001 Task.

## Finding

The exact [statement](../../claims/Yin_C_F0079_v4.md#statement) and complete [argument](../../claims/Yin_C_F0079_v4.md#argument) were checked under regularity of X_i-lambda for every index and every complex lambda, with no normality or generation assumption.
The comparison with the normal case, the nonnormal example and the common-domain normalization were also checked.
No unresolved gap was found within this scope.
This supports a proved, self-reviewed assessment for C_F0079 v4.

Regularity means invertibility in L0(M); it does not assert a bounded inverse in M.
It excludes eigenvectors of both left and right multiplication by X_i on L0(M), hence excludes nonzero finite-dimensional invariant subspaces.
The minimal-tensor-decomposition argument then proves individual injectivity of Psi_i.
Left and right multiplication by a bounded X_i preserve H whether or not X_i is normal.
Thus the quotient-by-H argument is valid in each tensor factor and recovers an algebraic L2 tensor from its algebraic L2 image.
No spectral theorem or adjoint-generator relation enters these algebraic steps.

For maximal Delta, the reviewer followed the conversion of a finite-rank cycle into tensors, common denominators, coordinate separation by Phi_i, individual injectivity and cancellation in the affiliated tensor algebra.
The cycle characterization is stated for arbitrary bounded tuples in M.
The scalar-shift assumption supplies exactly the individual injectivity needed to make every cycle vanish.

For tensor recovery, the common adjoint domain makes S_i=Phi_i(h) closable.
The cleared identity and injectivity of the left denominator give finite rank on the dense subspace t M Omega.
The finite-rank closure has domain all H, so it equals the closure of S_i.
The Theta actions, regular cancellation and individual recovery then give k_i in H tensor_alg H.
This uses no bounded inverse of a denominator on H and no normality of X_i.

For rationality, maximal Delta permits C_F0068 Part A, whose stated scope includes arbitrary bounded tuples without normality or generation.
The tensor identity for an arbitrary fraction pair has bounded algebraic total image.
Recovery and T_i=-Theta(ell_i) give the required finite-rank certificate with right-hand side sP_Omega b-aP_Omega t.
The converse for some pair and fixed-pair uniqueness follow as before.
The three equivalent conditions retain their full quantifiers.

For a normal operator, faithfulness and spectral calculus identify absence of spectral atoms with regularity of every scalar shift, so the old normal criterion is a specialization.
For X(t)=[[t,1],[0,t]] in L-infinity([0,1]) tensor M_2(C), the commutator with its adjoint is diag(1,-1).
Multiplication verifies the displayed inverse of X-lambda off at most the one-point null set, giving an affiliated inverse for every complex lambda.
L=P_Omega supplies a bounded one-coordinate liberation system.
The two-point atomic example still shows that a liberation system alone does not ensure the conclusion when the scalar-shift hypothesis is absent.

The normalization correction a Omega maps to a L_i Omega remains well defined on M Omega, commutes with left multiplication and has adjoint value b(L_i Omega)* at b Omega.
Its domain and adjoint-domain argument uses no scalar-shift assumption.
No normality-free claim about the ordinary dual-system criterion or the conjugate-variable construction is made.
Their existing hypotheses remain at those results.
Established external inputs are used at their checked statement and applicability scopes, without a new audit of their original full proofs.
Earlier fixed reviews retain their original, narrower scopes.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original finding](#finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0079_v4.md#statement) | Liberation domain definition, all-scalar-shift regularity, maximal Delta, recovery, every-fraction rationality, uniqueness and normalization. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0079_v4.md#argument) | Complete proof, normal specialization, nonnormal example, missing-regularity example and common-domain normalization, with the source applicability limits. |

---
author: Yin
---

# Algebraic spectral subspaces and continuity of intertwiners

## Lau88-U001

Source: [Lau88](https://dml.cz/bitstream/handle/10338.dmlcz/102208/CzechMathJ_38-1988-1_11.pdf), published journal article in DML-CZ, Kjeld Bagger Laursen, *Algebraic spectral subspaces and automatic continuity*, Czechoslovak Mathematical Journal 38(1) (1988), 157--172.
The inspected digital edition has a repository cover followed by the sixteen printed journal pages.
Bibliographic and artifact/access facts belong in the sole bibliography and registry.

Record: 2026-10-14, direct primary-source reading by the mathematical exploration agent for Yin.
State: Read.
The exact definitions, Proposition 3.7 and Theorem 4.1 are accepted as published inputs for the triangular-intertwiner argument retained in [C_F0069](../../../claims/Yin_C_F0069_v1.md#argument).
The published proofs were read for structure and interfaces, not independently audited in full.

### Definitions and exact accepted results

For a bounded operator S on a complex Banach space Y and a proper subset F of C, E_S(F) is the largest linear subspace V of Y satisfying

\[
 (S-\lambda)V=V\qquad(\lambda\notin F).
\]

Equivalently, it is the sum of all subspaces with this property.
The subspace E_S(empty) is the largest algebraically S-divisible subspace.
No topological closure is part of this definition.
Locator: Section 2, printed p. 158 / PDF p. 3.

A bounded operator S is well-decomposable if every two-set open cover U,V of C admits closed S-invariant subspaces Y_U,Y_V, a bounded operator B, and an integer m>=1 such that the spectra of the restrictions lie in U,V respectively, Ran B is contained in Y_U, Ran(I-B) is contained in Y_V, and ad_S^m(B)=0.
It is super-decomposable when B can be chosen to commute with S.
Locator: definition before Proposition 3.7 and paragraph before Proposition 3.8, printed p. 164 / PDF p. 9.

**Proposition 3.7.**
If S is well-decomposable and E_S(empty)={0}, then E_S(F) is closed for every closed F.
Locator: printed p. 164 / PDF p. 9.
These hypotheses are sufficient; no scalar-type or Hilbert-space assumption is imposed on S.

A bounded operator T on a Banach space X is decomposable when every two-set open cover of C admits a decomposition X=X_U+X_V by closed invariant subspaces whose restricted spectra lie in the respective open sets.
In the intended application T is multiplication by a normal element on M, and spectral projections verify this property directly.

For S in B(Y), T in B(X), define C(S,T)(theta)=S theta-theta T on algebraic linear maps theta:X -> Y.
A complex number lambda is a critical eigenvalue of (S,T) if lambda is an eigenvalue of S and (T-lambda)X has infinite algebraic codimension in X.

**Theorem 4.1.**
Suppose T is decomposable and E_S(F) is closed for every closed F.
Then every algebraic linear map theta:X -> Y satisfying C(S,T)^n theta=0 for some integer n>=1 is continuous if and only if (S,T) has no critical eigenvalues.
Locator: printed p. 166 / PDF p. 11.
In particular, if S has no eigenvalues, every algebraic intertwiner S theta=theta T is bounded.

### Intended application and scope boundary

The consuming argument takes X=M with the operator norm, Y=H direct-sum M, T=L_x and

\[
 S=\begin{pmatrix}\lambda(x)&P|_M\\0&L_x\end{pmatrix},
 \qquad \theta(a)=(E(a\Omega),a),
\]

where [E,x]=P is assumed algebraically on every bounded vector.
The map E is not presumed continuous or closable.
The local argument must prove diffuseness, a smooth triangular functional calculus giving super-decomposability, absence of divisible subspaces, and absence of eigenvalues before Theorem 4.1 applies.
None of those project-specific steps is a statement of Lau88.
Their complete substantive proof is retained in the linked Claim; it was initially developed in the bounded exploration preceding that fixed version.

The output is boundedness M -> H.
It does not imply Hilbert-space closability, a vacuum adjoint, a starred-core derivation, or finite Fisher information without further arguments.
The theorem cannot be applied directly to E merely from boundedness of the inhomogeneous commutator; the triangular enlargement is essential to this use.

### Inspection and search limits

The inspected passages are the definition on p. 158, the definitions and Proposition 3.7 on p. 164, and Theorem 4.1 with its proof on pp. 166--169.
Proposition 3.7 invokes preservation of algebraic spectral subspaces proved in the source's reference [1].
Theorem 4.1 invokes a localization theorem from reference [2], a separating-space stability result from reference [12], and a Mittag-Leffler argument from reference [16].
Those predecessors were not re-audited; the published results, with their hypotheses checked, are accepted inputs.
No whole-paper audit, independent audit of the source's original proofs, formal verification, or priority claim is made.

Searches used the phrases automatic continuity, intertwining normal operators, critical eigenvalues, separating space and generalized intertwining.
Sinclair's publisher chapter summary was an initial lead.
The search stopped at the exact applicable primary results above.
The intended extension of a dual to a Banach-space intertwiner is assessed separately from literature coverage.
Pták--Vrbová's normal spectral-function paper was located, but its scanned proof was not inspected; the consuming argument instead gives an elementary proof that a bounded normal operator has no nonzero divisible subspace.

## Source and inspection

| Field | Value |
| --- | --- |
| source-version | Published Czechoslovak Mathematical Journal 38(1) (1988), 157--172; DML-CZ scan, DOI 10.21136/CMJ.1988.102208, seventeen PDF pages including repository cover. |
| source-locator | Section 2 definition, p. 158; well/super-decomposability and Proposition 3.7, p. 164; Theorem 4.1 and proof, pp. 166--169. |
| inspection | 2026-10-14: primary-source statement/convention reading and selected proof-interface reading. Published propositions accepted for use; their cited predecessor results and original complete proof chain were not independently audited. |

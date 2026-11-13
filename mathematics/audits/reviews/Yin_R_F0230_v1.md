---
author: Yin
---
# Independent review of the two-coordinate obstruction for normal commutant elements

## Whole-proof finding

At 2026-11-13T15:19 UTC a separate reviewer outside proof development checked the whole [statement](../../claims/Yin_C_F0222_v1.md#statement) and [argument](../../claims/Yin_C_F0222_v1.md#argument) of the candidate dated 2026-11-13T15:17.
The reviewer received the fixed Claim and review scope without exploration notes, substantive development dialogue, author explanations or prior findings on the candidate.
The scalar conclusion and its application to separated direct sums both hold.

Fix one of the two derivations and take its own graph approximants \(a_n\).
The bound \(2\|X_m\|\|a_n-a\|_2\) controls the commutator input, and each of \((a_n-a)\otimes1\) and \(1\otimes(a_n-a)\) has norm \(\|a_n-a\|_2\).
The other two differentiated terms consist of \(K_l=\overline{\delta_l}a\) in the limit, multiplied on the indicated sides by the fixed bounded \(X_m\).
Thus closability gives \(X_m K_l-K_l X_m=\delta_{lm}(a\otimes1-1\otimes a)\) for both \(m\).

For distinct spectral points \(\lambda,\mu\) of the normal \(a\), every open disk around either has nonzero spectral projection, by the support property of the spectral resolution.
The selected closed disks therefore have projections of strictly positive trace.
Bounded Fuglede commutation gives \(X_m a^*=a^*X_m\), hence \(X_m\) commutes with both spectral cutoffs \(p,q\).
This gives \(p(X_m v)p=(pX_mp)(pvp)\) and \(q(wX_m)q=(qwq)(qX_mq)\), also on the completed Hilbert spaces.
The inherited norm on the compressed tensor space is \(\sqrt{\tau(p)\tau(q)}\) times the normalized one.
The complex-linear second-leg identification \(w\mapsto w^{\mathrm{op}}\) preserves that normalized Hilbert norm by traciality and turns right multiplication by \(qX_mq\) into left multiplication by \((qX_mq)^{\mathrm{op}}\).
In particular it leaves the center \(\mu\) of the second disk unchanged as a complex scalar.
For radii \(r,s\) the norm of \(D_a-(\lambda-\mu)1_{\mathcal B}\) is at most \(r+s<|\lambda-\mu|/2\).
The Neumann series therefore gives \(\|D_a^{-1}\|\le (|\lambda-\mu|-r-s)^{-1}\).

The compressed equations are equalities in \(L^2(\mathcal B)\) and thus also in the affiliated algebra \(U(\mathcal B)\), where the bounded left actions and products agree.
Here \(D_i(k_iD_a^{-1})=1\).
Multiplication by the complement of the range projection of \(D_i\) gives that complement equal to zero.
The partial isometry in the polar decomposition then has final projection \(1\), so equality of the two support traces and faithfulness give initial projection \(1\).
The affiliated inverse exists, and \(D_i k_j=0\) now forces \(k_j=0\), incompatible with \(D_j k_j=D_a\).
All compressions act on existing Hilbert tensors, and inversion takes place in the affiliated algebra, so a graph-domain assumption on the cutoffs and a bounded inverse for \(D_i\) are unnecessary.

For an actual ACSY witness the adjoint vacuum controls its pairing on \(a^*xb^*\) for fixed core \(a,b\).
Moving the outer multipliers to the vacuum in the two remaining Leibniz terms bounds each by a constant times \(\|x\|_2\), giving a dense algebraic tensor subspace of the adjoint domain.
For \(e\) central in \(C^*(X)\), strong density makes \(e\) central in \(M\), and a selfadjoint polynomial within \(1/4\) of \(e\) has its two corner spectra in the disjoint intervals used in the cutoff proof.
Polynomial approximation in \(C^1\) controls the divided differences on the whole interval, so the polynomial derivatives converge in the Hilbert tensor norm for each witness and \(e\) lies in both closed domains.
Finally, for \(T=T_1\oplus T_2\) with disjoint compact spectra, holomorphic functional calculus on disjoint open neighborhoods gives \(f(T)=1\oplus0\) with values \(1,0\) on the two neighborhoods.
Spectral permanence for the unital \(C^*(T)\) gives \(f(T)\in C^*(T)\), even when \(T\) is nonnormal.
For two nonzero summands this violates the proved scalar conclusion, independently of the individual dual costs.
The argument leaves open the case of a von Neumann central projection for which joint graph membership is unknown.
The source checks concerned the declared interfaces below and used the existing foundational results at their stated scope.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole-proof finding](#whole-proof-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole-proof finding](#whole-proof-finding) | [Statement](../../claims/Yin_C_F0222_v1.md#statement) | Scalarity under two separate graph-domain assumptions and the central projection and spectral separation consequences. |
| [Whole-proof finding](#whole-proof-finding) | [Argument](../../claims/Yin_C_F0222_v1.md#argument) | Commutator sign, noncentral spectral cutoffs, opposite-algebra representation, gap estimate, finite-trace inverse and application to actual ACSY. |
| [Whole-proof finding](#whole-proof-finding) | [Graph commutator](../../claims/Yin_C_F0206_v1.md#the-mixed-tensor-blocks-and-the-generator-first-sign) | Outer Leibniz convergence in the separate graph norms and sign of the resulting equations. |
| [Whole-proof finding](#whole-proof-finding) | [Bounded spectral commutation](../../claims/Yin_C_F0211_v1.md#compression-by-small-singular-value-projections) | Fuglede applied to the bounded normal commutant element and an arbitrary bounded coordinate. |
| [Whole-proof finding](#whole-proof-finding) | [Finite affiliated inverses](../literature/MSY23/Yin_U004.md#msy23-u004) | Equality of support traces and inversion in the affiliated algebra of the finite tracial tensor product. |
| [Whole-proof finding](#whole-proof-finding) | [Actual graph and central cutoffs](../../claims/Yin_C_F0206_v1.md#the-closed-derivation-and-the-central-spectral-cutoff) | Dense adjoint domain from the vacuum and uniform divided-difference control for a central projection of the generated \(C^*\)-algebra. |
| [Whole-proof finding](#whole-proof-finding) | [Actual ACSY](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Represented star core, outer actions, actual adjoint vacuum and absence of a normality restriction on the generators. |

---
author: Yin
---

# Singular-value mass for a compressed normal coordinate

## Finding

Review time (UTC) 2026-11-16T16:31.
A reviewer outside the proof development inspected the complete candidate dated 2026-11-16T16:27 and its five declared dependency interfaces.
The reviewer received no proof-development dialogue, exploration notes, separate author explanation or prior review conclusion about this candidate.
The compressed derivation, its vacuum, the scalar-shift estimate and the two-point consequence all follow under the stated hypotheses.

For a diffuse normal \(Z\), the joint spectral projection of its two outer actions on the collision diagonal vanishes on the whole coarse space.
Indeed these actions are normal on the von Neumann tensor product of the marginal algebras, whose faithful product trace assigns zero mass to the diagonal.
Thus the commutation identity obtained by differentiating \(ZZ^*=Z^*Z\) uniquely determines \(\delta Z^*=k\).
I checked the statement and applicability of ACSY24, Lemma 3.3, in the published article on pp. 34–35.
For a weakly dense starred algebra the vacuum assumption puts all algebraic tensors of core elements in the adjoint domain and gives closability.
Bounded strong-star approximation of an omitted \(p\) by killed coefficients gives graph convergence on each word, because all surviving differentiated letters are \(Z\) or \(Z^*\) and their outer multipliers converge strongly with a common bound.
Closedness then makes the resulting derivative independent of the chosen word representation.

For \(x=pxp\) in the corner core, its derivative already has left support \(p\) in the first leg and right support \(p\) in the second.
The two inner multiplications are right multiplication by \(p\) on the first leg and left multiplication by \(p\) on the second.
These commute with the outer actions, and the following two conditional expectations commute with the outer actions of \(W\).
Their composition therefore gives a derivation on the represented core and sends \(pZp\) to \(p\otimes p\).
On \(pZ^*p\) it compresses \(k\) on both sides by \(p\otimes p^{\rm op}\) and applies the product conditional expectation.
Compression and conditional expectation contract the operator norm and act on simple marginal tensors as \(\Psi\otimes\Psi^{\rm op}\).
Their normality proves the stated formula for the measurable phase.
For first-leg vectors of the form \(pa\), the inner insertion preserves trace because \(\tau(pap)=\tau(pa)\), and the analogous identity holds for the second leg.
Together with \(W\)-trace preservation this shows \((\tau_p\otimes\tau_p)(Dx)=t^{-2}\langle\xi,x\rangle_\tau\).
Pairing against \(x=pxp\in W\) accounts for one factor of \(t\) when changing the scalar product to that of \(\tau_p\).
Hence \(\xi_T=t^{-1}\mathbb E_W(p\xi p)\) in \(L^2(W,\tau_p)\), whose norm is bounded as claimed by contractivity of the \(L^2\) projection.

In the normalized corner write \(B=T-\lambda p\), \(R=(B^*B+sp)^{-1}\), \(V=BR\) and \(L=(BB^*+sp)^{-1}\).
The inverse product rule, with \(p-BRB^*=sL\), gives \(DV=sL\otimes R^{\rm op}-(V\otimes V^{\rm op})K\).
For the geometric inverse approximants, derivatives of the degree-\(n\) terms are bounded in coarse norm by \(Cnq^{n-1}\) for a fixed \(q<1\).
The core pairing thus passes to the displayed derivative.
The two positive resolvents have the same trace by finite traciality, including the kernel term.
The magnitude of the trace of \((V\otimes V^{\rm op})K\) is bounded by \(\tau_p(|V|)^2\) because \(\|K\|\le1\).
This proves the signed scalar inequality also for nonnormal \(B\).

Integrating over \(r\le u\le R_0\) with \(s=u^2\) gives the difference of the arctangent divided differences at the two endpoints.
Direct differentiation gives the claimed sign and extends to \(v=w=0\), where the primitive is \(1/u\).
The integrated polar resolvent has norm at most one after multiplication by \(2/\pi\), including on the kernel where its scalar integrand is zero.
The divided difference is positive, is at most \(1/R_0\) at the upper endpoint, and is at least \(1/(2r)\) on \([0,r]^2\) at the lower endpoint.
These estimates give the coefficient \(\pi r\) in (1) and exclude any atom at zero by taking \(r\downarrow0\).
For the comparison family \(|uh|=h=\varepsilon p+1-p\) with both spectral masses \(1/2\).
Using \(r=\varepsilon\), \(\lambda=0\) and \(\|p\xi p\|_2\le\|\xi\|_2\) gives the claimed \(t^{3/2}/(4\pi\varepsilon)\) lower bound for an ambient realization.
This review checks the use of that comparison law and the cited interfaces at their stated scope.
The claim gives a necessary condition on such realizations and leaves the general F0011 normal-tuple implication open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0309_v1.md#decision-candidate) | Complete 2026-11-16T16:27 candidate and all five declared dependencies. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0309_v1.md#statement) | Both cases for the projection, represented corner derivation, exact normalized vacuum and phase, all scalar shifts and the two-point lower bound. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0309_v1.md#argument) | Corner graph, inner and outer compressions, product expectation, trace pairing and conjugate-variable norm, signed resolvent integral and endpoint estimates. |
| [Finding](#finding) | [Normal phase](../../claims/Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Normal commutation identity and injectivity of the outer spectral difference using the given diffuse marginal. |
| [Finding](#finding) | [Actual adjoint formula](../literature/ACSY24/Yin_U001.md#acsy24-u001) | Published Lemma 3.3 gives density of the adjoint domain from the actual vacuum on a weakly dense starred core. |
| [Finding](#finding) | [Omitted graph actions](../../claims/Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Bounded graph approximation extends the zero derivative to the omitted projection and preserves the product rule on the needed words. |
| [Finding](#finding) | [Resolvent singular-mass estimate](../../claims/Yin_C_F0229_v1.md#argument) | Geometric inverse graph, signed integral, kernel normalization and arctangent mass constant adapted to a corner contraction. |
| [Finding](#finding) | [Two-point modulus](../../claims/Yin_C_F0225_v1.md#statement) | Positive modulus with equal masses at \(\varepsilon,1\) in the intrinsic comparison family and the distinction from an ambient compression. |

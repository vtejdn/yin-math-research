---
author: Yin
---

# Independent review of the Poisson conjugation of a spectral projection

## Finding

On 2026-11-16T18:11 UTC a reviewer outside proof development independently checked the [candidate decision](../../claims/Yin_C_F0327_v1.md#decision-candidate) dated 2026-11-16T18:07.
The reviewer received the fixed claim and review scope without proof-development dialogue or previous findings on this candidate.
The stated actual-vacuum equivalence, exact norm, uniform finite-column estimate, adjoint orientation, endpoint assertions and disk example hold under the given finite tracial hypotheses.

Conjugation of the noise algebra by the centered sign \(a\) produces an algebra free from the original noise algebra by expansion into centered reduced words.
On each analytic factor generated respectively by \(aua\) and \(u^*\), the trace is evaluation at \(r\).
Consequently its centered subspace is a multiplicative kernel, and the alternating centered-word calculation gives \(\tau((as)^k)=r^{2k}\) for positive \(k\), with the negative moments by adjunction.
An odd word in two signs reduces cyclically to one of the signs and has zero trace.
For a new sign \(S\) free from \(A\), \(v=aS\) is Haar and \(ava=v^*\).
The constant coefficient of the disk automorphism is \(\rho=r^2\), so its \(k\)-th analytic power has constant coefficient \(\rho^k\).
It follows that \(a\Phi_\rho(v)\) is a centered symmetry with exactly the preceding two-sign law.
The trace pairings against \(1,a\) determine expectation onto \(B=W^*(a)\).
In each realization freeness over \(B\) between \(A\) and the second two-sign algebra reduces arbitrary mixed moments to those \(B\)-valued moments.
This verifies the full joint law with \(A\).
The inverse disk map has parameter \(-\rho\), which gives (3), and hence the new sign generates the full free product together with \(A\).

Holding \(s\) fixed in (3) and differentiating \(a\) inserts \(\theta\) between two copies of \(s(1-\rho a s)^{-1}=(S+\rho a)/(1-\rho^2)\).
The relation \(\theta a=-a\theta\) and \(a^2=1\) give the coefficient \(-c_\rho\theta\) and the stated two cross terms in (4).
Both \(S\theta S-\theta\) and \((a\theta)S-S(a\theta)\) anticommute with \(S\).
They therefore descend through its algebraic square relation, and the other factor already has the inner-difference derivation.
The direct and inverse substitutions are identities in norm-convergent series.
The summable \(n\rho^{n-1}\) derivative estimate also holds in their coarse graphs, verifying that the resulting derivative kills \(s\).

Explicitly, the coefficient \(y\) in a scalar test \(x+yS\) has \(|y|\le\|x+yS\|\).
The two right slices take this test to \(-y\) and \(-yS\), with double traces represented by \(-S\) and zero.
These are the hypotheses of the terminal coefficient estimate even though \(S\) has two-point law.
Each inner insertion has column cost at most \((2\sqrt{4/\pi}+2)\|\beta\|_2\).
For \(D_1\) its vacuum on separated tensors is \(-J_S(\bar\beta)\), as can also be checked by pairing with \(f S g\) and contracting each marginal factor.
The zero vacuum of \(D_2\) persists after insertion.
Freeness makes \(J_S\) isometric and orthogonal to the marginal.
With \(\alpha(z,w)=a(z)-a(w)\) real this gives liberation vacuum \(-c_\rho J_S(\alpha)\) on the dense target core.
Algebraic simple tensors lie in the requisite adjoint domains for the finite insertions used to construct this graph, and finite-word graph approximation justifies restriction to that core.

The diffuse law makes the inner gap injective in the coarse correspondence.
The assigned marginal unit tensor and forced adjoint phase, together with zero on the omitted selfadjoint sign, therefore respect represented relations.
Necessity follows from projecting an actual distinguished vacuum to the marginal and from the gap commutator with \(Z^*\), which gives finite inverse-gap energy of the liberation vacuum.
Since its joint left-right spectral measure is \(c_\rho^2|\alpha|^2\mu^2\) and \(c_\rho>0\), this energy is precisely \(c_\rho^2J\).
Conversely the scalar adjoint correction and the inverse-gap limit give the actual vacuum \(\xi_\mu-c_\rho J_S(\alpha/\bar d)\).
The orthogonality just proved gives the exact squared norm in (1).
These steps use diffuseness of the distinguished coordinate and the prescribed zero derivative on the sign.

The reference cutoff acts on the terminal marginal letter of a reduced-word expansion.
The squared coefficient column is its conditional expectation onto \(A\), so the scalar bound \(3(2+\sqrt2)\|\xi_\mu\|_2\) applies uniformly to the full free core.
Both noise corrections have Hilbert kernel norm at most \(\sqrt J\), and their coefficients have total absolute value \(c_\rho(1+\rho)\le2c_\rho\).
At each fixed cutoff the Neumann approximants to target words converge in operator norm and in each differentiated graph, preserving the column norm in the limit.
Strong inner cutoff convergence then gives the original right-column bound by an absolute multiple of \((\|\xi_\mu\|_2^2+c_\rho^2J)^{1/2}\).
Passing to \(Z^*\) conjugates the spectral gap and preserves both squared energies.
At the Haar endpoint the new coefficient is free by reduced words and requires only scalar actuality.
At the deterministic endpoint the nonconstant centered sign commutes with \(Z\), contradicting the prescribed derivative of their commutator.
A scalar phase of the conjugating unitary leaves its conjugation unchanged.
For the disk example the integrals of inverse distance against bounded planar area density are uniformly finite, giving a bounded scalar vacuum by symmetrization.
Positive separation bounds the sign energy, and the centered signs have correlation \(r^2\), proving nonfreeness.
The reviewed obstruction from free conjugation of a diffuse coefficient requires a diffuse second marginal.
The review checked the six declared dependency interfaces.
The projection here serves as the coefficient killed by the distinguished derivation.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0327_v1.md#decision-candidate) | Whole fixed candidate and all six declared dependencies. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0327_v1.md#statement) | Necessity and sufficiency, exact vacuum norm, finite-column estimate, both distinguished orientations, parameters, endpoints and nonfree example. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0327_v1.md#argument) | Dihedral trace law over the full base, inverse disk map, signed tensor derivations, intrinsic adjoint recovery and uniform passage to the represented core. |
| [Finding](#finding) | [Amalgamation](../../claims/Yin_C_F0322_v1.md#conditional-expectations-of-the-four-matrix-corners) | Reduced words over the common sign algebra upgrade the two-sign moments to all mixed base moments. |
| [Finding](#finding) | [Terminal block](../../claims/Yin_C_F0277_v1.md#a-necessary-inverse-scale-and-the-conjugate-variable-of-the-new-coordinate) | Finite-column bound and actual vacuum after inserting a marginal Hilbert kernel at either permitted scalar sign derivation. |
| [Finding](#finding) | [Represented descent](../../claims/Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Inner-gap injectivity at the distinguished marginal, descent on core relations and the necessary commutator energy. |
| [Finding](#finding) | [Scalar correction](../../claims/Yin_C_F0238_v1.md#the-scalar-correction-in-the-liberation-adjoint) | Inverse conjugate gap, scalar adjoint limit, actual core pairing and orthogonal norm decomposition. |
| [Finding](#finding) | [Soft scalar bound](../../claims/Yin_C_F0284_v1.md#the-bridge-from-a-marginal-factor-to-the-rest-of-the-word) | Uniform \(3(2+\sqrt2)\) cutoff factor on bounded marginal columns in each orientation. |
| [Finding](#finding) | [Free right modules](../../claims/Yin_C_F0265_v1.md#the-rotated-unitary-coordinate) | Terminal right-slice action and conditional expectation of the full squared column. |

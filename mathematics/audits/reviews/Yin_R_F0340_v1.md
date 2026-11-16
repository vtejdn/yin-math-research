---
author: Yin
---

# Review of the spectral-row inequality and positive-density partition endpoint

## Finding

At 2026-11-16T19:01 UTC a separately assigned agent for Yin independently reviewed the entire C_F0335 v1 candidate fixed at 18:59 UTC.
The reviewer did not develop the proof and received only the fixed candidate, its mathematical inputs and the review assignment, without proof-development dialogue, author explanations or previous findings on this candidate.
The spectral-row bound with one common conull set, its trace-class and Cauchy consequences, and the positive-lower-density conclusions hold.

Actuality gives a diffuse marginal and finite inverse-gap energy \(I\).
The joint measure \(\nu\) of the real vacuum has a symmetric product density since opposite corner norms agree by adjunction.
The finite measure \(\sigma=|z-w|^{-2}\nu\), with zero diagonal, is also absolutely continuous with respect to \(\mu^2\).
The first marginals of its restrictions to the shrinking diagonal strips have decreasing \(\mu\)-densities with limit zero in \(L^1(\mu)\) and almost everywhere.
Differentiating all these countably many densities gives \(\sigma(R^2)/\mu(R)\to0\) at almost every center.
Ball differentiation of the finite area measure on a bounded open neighborhood of the support with respect to \(\mu\) gives finite \(\limsup r^2/\mu(R)\), including at centers belonging to its area-singular part.
Thus \(\nu(R^2)/\mu(R)^2\to0\) with no density upper bound on \(\nu\).

The derivative of the fixed strict polynomial \(b\) is a finite sum of bounded tensors.
On \(b^n\) its projective norm is at most \(n\|b\|^{n-1}\|\gamma b\|_\pi\), summable with the analytic square-root coefficients.
Each resulting tensor in the signed pairing factors through two bounded marginal conditional expectations.
Taking its real symmetric part is a finite sum of real rank-one kernels whose trace norm is bounded by a constant times the original product of sup norms.
The sum over the projective expansion therefore gives a trace-class representative on \(L^2(\mu)\).
For fixed \(u\), ball differentiation of the two factors of each of these countably many terms gives the local averaged diagonal formula.
The products of their sup norms are summable uniformly in the ball.
This characterizes the almost-everywhere diagonal independently of the chosen expansion, which is necessary because \(\mu^2\) itself assigns its diagonal zero mass.

For \(l_\pm=k\pm\sqrt{\Lambda/\mu(R)}1_R\), the denominators of the two upper bounds in (5) divided by \(\Lambda\) tend to one.
One may take \(\Lambda=(\mu(R)+d_R)^{-1/2}\) for the stated regime.
Averaging removes odd powers, and the lower bound for \(F_{1_R\otimes1_R}\) costs at most \(\Lambda d_R\) upon moving the projection term to the right.
The averaged trace term tends to \((\tau k)^2\), with added part \(\Lambda\mu(R)\).
The fourth-power numerator divided by \(\Lambda\) is \(\Lambda d_R\), and the mixed two-indicator term is bounded by \(4\|k\|_\infty^2\nu(R^2)/\mu(R)\).
Both vanish.
Symmetry makes the two one-indicator terms equal, leaving exactly twice the ball average of \(\int k(z)^2 h(z,w)d\mu(z)\).
Differentiation for a countable algebra of bounded real step functions and finiteness of the row measure give a common conull set depending only on the spectral data.
Uniformly bounded almost-everywhere approximants to each other bounded Borel \(k\) converge for that row measure as well, because it is absolutely continuous with respect to \(\mu\).
The trace-class representation passes their quadratic pairings to the limit for each \(u\); this step needs no intersection of exceptional sets indexed by \(u\).
The stated operator inequality for bounded \(h\) follows by density.

When \(\zeta\ne0\), a centered Borel sign gives a nonzero selfadjoint vector \(a\zeta a\) and some bounded selfadjoint polynomial has nonzero real vacuum pairing with it.
At \(u_t=i+tb+O(t^2)\), the projective derivative of the error is \(O_b(t^2)\).
The inner product against the constant \(i\), together with the factor \(-i\) in the signed form, gives the negative sign of the linear coefficient in the candidate.
A suitable sign of \(t\) therefore gives a positive quadratic pairing at \(a\) although \(P_1a=0\).
The converse implication follows from the common row estimate at \(\nu=0\).

Applying (1) separately to the real and imaginary Cauchy features and integrating gives the scalar soft-transform squared norm for the mean term and a row penalty at most \(2I\).
Transposing or conjugating the scalar kernel preserves its norm, and its parameter in the referenced bound is \(\epsilon^2\).
Fubini is justified for this fixed cutoff by boundedness and the absolutely summable separated representation.
For the explicit positive block sums, the lower projection bounds sum uniformly while (2) bounds \(F_{K_{\epsilon_n}}\) above.
The assumed gap convergence and its conjugate then pass this lower bound for \(F_{q_n-K_{\epsilon_n}}\) to \(F_g\) on every analytic test through the two generator tensors.
The signed mixed-energy theorem gives the two canonical domains.

For a positive-lower-density center, \(r/\mu(R)\) is bounded, and \(\nu(R^2)/\mu(R)^3\le4(r/\mu(R))^2\sigma(R^2)/\mu(R)\to0\).
Dividing the two projection estimates by \(\mu(R)^2\) gives local bounds tending to zero and one respectively, proving the claimed diagonal interval.
On a piece \(E_j\) with lower density greater than \(1/j\), ball differentiation of its indicator gives \(\mu(E_j\cap R)\ge r/(2j)\) eventually at almost every center.
The fine family of balls with this property and \(r<\delta_j\) admits a disjoint countable Vitali subfamily covering the piece modulo \(\mu\)-null sets.
Intersecting the balls with \(E_j\) preserves the lower mass condition and gives a partition there.
For such a cell \(F\), its inverse-mass-square cost is at most \(16j^2\sigma(F^2)\).
The disjoint cell squares lie in a diagonal strip of width \(2\delta_j\), so their costs can sum to less than \(2^{-j}\delta\).
This proves zero infimum and removes the smaller-side diagonal term to arbitrary precision in the stated rectangular calculation.
The seven direct dependency interfaces were checked at their stated uses.
The unrestricted normal implication remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Candidate](../../claims/Yin_C_F0335_v1.md#decision-candidate) | Fixed 18:59 UTC candidate and its precise spectral and domain conclusions. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0335_v1.md#statement) | Common row inequality, trace-class representative and diagonal, converse at zero gradient, Cauchy Gram estimate, domain criterion and zero partition infimum. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0335_v1.md#argument) | Whole proof including spectral differentiation, averaging and denominator limits, analytic expansion, Cauchy integration, and positive lower density partition. |
| [Finding](#finding) | [Liberation energy](../../claims/Yin_C_F0238_v1.md#statement) | Actual vacuum norm identity, diffuse law and finite inverse-gap mass. |
| [Finding](#finding) | [Marginal adjoint](../../claims/Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Product absolute continuity and the selfadjoint Borel rank-one vacuum \(a\zeta a\). |
| [Finding](#finding) | [Uncentered bound](../../claims/Yin_C_F0331_v1.md#the-uncentered-square) | Upper quadratic estimate at an arbitrary bounded real marginal function, including its mean term. |
| [Finding](#finding) | [Projection bound](../../claims/Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Lower estimate at a spectral ball or any Borel block from the exact projection energy. |
| [Finding](#finding) | [Soft Cauchy estimate](../../claims/Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | Uniform integral of the squared scalar Cauchy mean at parameter \(\epsilon^2\). |
| [Finding](#finding) | [Signed domain implication](../../claims/Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Convergence through both gap tensors and the two full canonical domains from a lower bound for the matched form. |
| [Finding](#finding) | [Smaller-side subdivisions](../../claims/Yin_C_F0332_v1.md#subdivision-by-cubes) | The rectangular cost term proportional to the sum of the smaller-side diagonal cell quotients. |

---
author: Yin
---

# Review of the curvature difference on exchange-symmetric normal pairs

## Finding

Review time (UTC) 2026-11-16T16:56.
A reviewer outside the development of C_F0314 examined the complete candidate dated 2026-11-16T16:55 and its eight declared dependency interfaces.
The reviewer received no proof-development dialogue, exploration notes, separate author explanation or earlier review findings on this candidate.
The scalar identity, both cost comparisons, the two finiteness criteria and the example all hold as stated.

For a bounded real kernel in the second marginal, pair the inner derivation applied to \(u\) against \(u\) after taking the right slice.
On \(a\otimes c\), the complex pairing before taking real parts is \(\tau(a)\tau(c)-\tau(u^*a)\tau(cu)\).
Its two terms are normal functionals on the marginal tensor product, so their difference has density \(1-\overline{b(z)}b(v)\) for \(b=\mathbb E_{B_1}u\).
Taking real parts gives an integrand between zero and two.
The identity \(\gamma_0+\gamma_1=\operatorname{ad}\) now gives, at a common cutoff, the sum of the two matched forms as the difference form plus this integral.
The scalar marginal vacuum is the orthogonal projection of the full vacuum, since the derivative on marginal polynomials lies in the marginal coarse space.
The scalar weight identity consequently gives \(\int g\,d\mu^2\le2s^2\), and the integral term converges to \(H\in[0,4s^2]\).

To justify the rest of the limit, conditional Jensen gives
\(\int |z-v|^2g^2\,d\mu^2\le4\int\kappa^2\,d\mu^3\), because \(|z-v|\kappa\le2\).
Dominated convergence therefore supplies both gap-weighted truncation limits, including for the adjoint generator.
These give convergence of the matched derivative vectors on every fixed word by the product rule.
For a strict polynomial test \(h\), their norms at \(h\) are uniformly bounded and differentiation of \(h^m\) costs at most \(m\|h\|^{m-1}\) times this bound.
The binomial series then passes the matched limits to both analytic unitaries.
Subtracting \(H\) from these two finite scalar limits proves convergence of \(D\) on each test.
The argument requires no convergence of the unmatched coarse vectors.
Exchange transports each matched pairing to the other one, and replacing both arguments of a pairing by their negatives preserves it.

I checked the signed term in (6) against the generator formulas for the mixed iterate.
After middle-leg integration the sum of the two real defects has values \((z-v)g/2\) and \((\bar z-\bar v)g/2\) on the distinguished generators and vanishes on the omitted ones.
These are the values of the matched liberation insertion divided by two.
The energy identity subtracts its real pairing, giving \(-F^j/2\) at coordinate \(j\), hence \(-(D+H)/2\) on summing.
This application uses the actual mixed graphs on the polynomial core and the analytic evaluation of the first-derivative identities.
The matched gap estimate above supplies the needed convergence irrespective of a uniform row bound.
The sum of the squared real-vacuum norms is \(2s^2\).
Writing \(v=V/s\) gives \(v^2\le2\sqrt2\,v+d/2\).
An oriented slice at \(u\) costs at most \(\sqrt2 V\), averaging the two signs recovers \(h\), and splitting a general contraction into two selfadjoint contractions costs a further factor of two.
Solving the quadratic gives \(k\le4+2\sqrt{4+d}\).
Conversely, the power series approximants have norms tending to one and their first derivatives converge, so every oriented slice on \(u\) costs at most \(ks\).
The parallelogram law for the sum and difference \(T_{jx}u\pm iT_{jy}u\) gives \(V^2\le2k^2s^2\).
Rearranging the signed identity and using \(H\le4s^2\) gives \(-D/s^2\le2v^2+4\sqrt2\,v+4\le4(k+1)^2\).
Both inequalities retain their extended-real interpretation.

Exchange transfers the original costs between coordinates, and taking the adjoint tuple realizes the reverse-oriented cost in the same universal class with the same vacuum norm.
Thus \(\sup k=K_{\rm ex}\), and substitution of the two-sided comparison with \(K_{\rm mix}\) yields the two constants in (4).
The assertion about every individual law uses the separate assembly result, which gives one actual exchange pair of infinite forward cost if the universal implication fails.
On that pair (3) forces \(d=\infty\).
This establishes the quantified criterion while leaving the finiteness question open.

In the two free copies of the separated-circle law, the centered-word vacuum calculation applies to both factors, and the circle condition gives full strong duals at both coordinates.
The same-circle contribution to the squared kernel integral is at least \(\sum_\ell t_\ell^4/r_\ell^4\), whose terms are proportional to \(2^{4\ell}\).
For \(b=\operatorname{Re}Z_0\), freeness gives scalar expectations of \(b,b^2\) on \(B_1\).
In the opposite tensor representation the inserted kernel is a right multiplier, so cycling the trace puts its square against the square of \(c(b\otimes1-1\otimes b^{\rm op})\).
The latter has product conditional expectation \(2c^2\operatorname{Var}(b)>0\), since these circles carry normalized arclength.
This proves divergence of the crossed coarse norm at \(h\) as the matched norm stays bounded.
For the difference derivation at each finite cutoff, the inverse rule at \(u_-=u_+^{-1}\) preserves the coarse norm through the two outer unitary factors.
Their average is \(h\), so each of the two norms dominates the norm at \(h\).
This verifies divergence along the whole sequence for each fixed analytic test and its compatibility with the scalar limit.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0314_v1.md#decision-candidate) | Complete candidate dated 2026-11-16T16:55 and all eight declared dependencies. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0314_v1.md#statement) | Scalar limits and conservation, the exchange case, per-law and universal constants and criteria, and divergence for both analytic signs. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0314_v1.md#argument) | Finite-cutoff identity, gap-weighted convergence, actual mixed energy, recovery of both original orientations, assembly quantifier and coarse divergence. |
| [Finding](#finding) | [Starred hypothesis](../../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) | Actual vacua of represented starred derivations and the universal normal strong-dual question. |
| [Finding](#finding) | [Actual mixed energy](../../claims/Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) | Both real components, squared vacuum normalization, equations (19) and (20) and the sign of the normal mixed defect. |
| [Finding](#finding) | [Signed curvature limit](../../claims/Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Gap tensors for both distinguished generators and the matched analytic-unitary limit on the original core. |
| [Finding](#finding) | [Curvature weight](../../claims/Yin_C_F0267_v1.md#statement) | Half the integrated curvature kernel is bounded by the squared marginal vacuum norm. |
| [Finding](#finding) | [Normal reversal](../../claims/Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | The adjoint tuple realizes the reverse-oriented derivatives with adjoint vacuum and equal norm. |
| [Finding](#finding) | [Exchange comparison](../../claims/Yin_C_F0311_v1.md#statement) | Full exchange cost, complementary mixed output cost, additive squared constant and universal equivalence. |
| [Finding](#finding) | [Single-pair assembly](../../claims/Yin_C_F0313_v1.md#statement) | Failure gives one exchange-symmetric actual pair with unbounded forward costs. |
| [Finding](#finding) | [Countable-circle example](../../claims/Yin_C_F0292_v1.md#a-law-with-divergent-curvature-compositions) | Exact radii and masses, actual scalar vacuum, separation and resulting full domains at both coordinates. |
| [Finding](#finding) | [Free extension](../../claims/Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) | Extension by zero to the other factor preserves each actual vacuum on centered reduced words. |

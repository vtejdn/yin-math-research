---
author: Yin
---

# Review of weighted curvature rows and the original canonical domains

## Finding

At 2026-11-14T16:03 UTC an agent outside proof development independently checked the [candidate of 2026-11-14T15:58](../../claims/Yin_C_F0291_v1.md#decision-candidate), its complete statement and argument, and the nine declared dependencies at their points of use.
The reviewer received the fixed proof and review scope without development dialogue, author explanations or prior conclusions about this proof.
The candidate proves the diffuse curvature inequality, the actual weighted vacuum formula, and both canonical domain inclusions under its weighted row and spectral hypotheses.
The two diffuse examples and the two finite-certificate obstructions have the claimed scope.

For four distinct points, expanding the determinant at \(s\) gives \(d_z|w-s|+d_w|z-s|\) as an upper bound, and the determinant at \(t\) is bounded by either \(\ell|w-t|\) or \(\ell|z-t|\).
Using the first of these last two bounds with the \(d_z\) term and the second with the \(d_w\) term gives exactly the factor two in (5).
For fixed \(z\ne w\), diffuseness excludes all exceptions, including \(s=t\).
Independence makes the \(L^2\) norm of the product on the left \(\ell g(z,w)\), even when a row on the right is infinite.
The lower semicontinuous zero extension and Fatou give lower semicontinuity of \(A\), so the essential supremum controls every support point.
The proof of the two-bound curvature theorem uses its hypotheses at just the coordinate whose domains it recovers.

The commutator vacuum for \(i\gamma\) is \(-i[Z^*,\xi]\), so its measure is \(|z-v|^2\nu_\xi\) and gives the diagonal zero mass.
Squaring (1) and using \((a+b)^2\le2(a^2+b^2)\) gives the coefficient eight in (2).
Integrability of the generator values in coarse space follows by integrating the same inequality against \(\mu^2\) and using the actual marginal's finite total curvature.
For the finite symmetric polynomial approximants, the bound by \(1+g\) controls convergence after multiplying by the gap in coarse space, and before multiplying by the gap in \(L^2(\nu_\zeta)\) when the right side of (2) is finite.
The outer factors of each fixed word are bounded, so the coarse limit respects every represented relation.
The two marginal trace corrections cancel for each symmetric approximant, and its vacuum pairing converges on every core vector to the pairing with \(S_g\zeta\).
This proves the actual adjoint assertion also when \(g\) has infinite coarse norm.
Under the additional coarse \(L^2\) assumption the approximants themselves converge in that norm, which justifies inserting \(g\) term by term in the algebraic liberation derivative.

With \(w=w_0\ge1\), \(A\le Rw\) gives the endpoint bound \(B w(z)w(v)\) for the gap times \(1+g\), with \(B=4\sqrt R+\operatorname{diam}K\).
Absolute continuity of \(\nu_\zeta\) with respect to \(\mu^2\), and positivity of the squared gap on distinct pairs, give the same absolute continuity for the restriction of \(\nu_\xi\) to those pairs.
This justifies integrating the almost-everywhere endpoint estimates against that restriction, including the implication from (3) to finiteness on the right of (2).
For each finite nonnegative symmetric approximant, applying weighted Cauchy–Schwarz and integrating in the opposite order gives \(\|T_q f\|_2^2\le\rho^2\|f\|_2^2\).
Positivity also gives \(T_q^k1\le T_q^kw\le\rho^kw\).
At edge \(l\) of a path, deleting the factor for its length times its kernel leaves \(T_q^{l-1}w(z)\) and \(T_q^{k-l}w(v)\), with the identity at a zero-length segment.
Summing over the edges and using the preceding spectral measure comparison gives \(kB\rho^{k-1}K_\xi\) for the vacuum norm, while the row norm costs \(\rho^k\|w\|_2\).

In the finite energy inequality, division by \((2\rho)^{2k}\) at \(k=2^n\) leaves \(t_{n+1}\) with coefficient one.
For each fixed \(q,u\), the Hilbert–Schmidt bound on \(T_q^k\) and the convergent differentiated binomial series at \(\|a\|<1\) bound the entire normalized sequence.
The constants in this preliminary bound may depend on \(q,u\).
If \(t_n>C+1\), then \(t_{n+1}\ge t_n(t_n-C)\), and induction gives growth by at least the same factor \(t_n-C>1\) at all later steps.
Consequently \(v_1\le2\rho(C+1)\) has a constant independent of both the approximant and the unitary.
For a fixed \(a\) the generator limits bound \(\|\beta_{q_j}a\|_2\) uniformly in \(j\), justifying passage through the differentiated series for each unitary sign.
The energy calculation for the minus sign also follows by applying the plus-sign calculation to \(-a\) and negating the resulting unitary.

The actual mixed tensor-leg graphs identify the middle trace of the summed defects on \(Z,Z^*\) with one half of the gap times \(g\) in the respective orientations.
The defects are outer derivations, so this identification passes through mixed words and the first-derivative series to \(u\), giving \(1/2\) as the coefficient of \(\|E_g u\|_2\).
The resulting uniform bound on \(V(u)\) gives both real right-slice bounds by averaging the two signs, scaling, and taking real and imaginary parts.
Their complex combinations give the forward slices of \(\delta_Z\) and its flip-adjoint companion.
The right slice of the companion at \(p^*\), followed by the tracial adjoint, gives the left slice of \(\delta_Z\) at \(p\).
The two-slice theorem applies on the original represented star core and puts \(M\Omega\) in the domains of both the closed right slice and its Hilbert adjoint.
The core relation \(E_0(X_jp)-X_jE_0(p)=\delta_{ij}\tau(p)1\) passes through bounded Kaplansky approximation in the weakly closed graph and gives \([X_j,-\overline E_0]=\delta_{ij}P_\Omega\) there.

For the perpendicular segments, integrating \(4/\max(x,y,t)^2\) in the third radius gives at most \(8/\max(x,y)\).
The two pieces of its weighted row integral cost at most \(8x^{-\alpha}/(1-\alpha)\) and \(8x^{-\alpha}/\alpha\), and the weight is square integrable for \(0<\alpha<1/2\).
Restricting to \(2x<y<1/2\) and \(y<t<2y\) bounds curvature below by a fixed multiple of \(1/y\), giving the logarithmically unbounded row on a set of positive measure at every sufficiently large level.
Bounded linear density and integrability of \(1/\max(x,y)\) give the actual scalar vacuum.
For the drift \(f(z)=\operatorname{Re}z\), the semicircular vacuum has squared norm one, so the drift criterion gives off-diagonal \(\nu_\xi\) density \(|f(z)-f(v)|^2/|z-v|^2\le1\).
This gives \(K_\xi\le\|w\|_2^2\), and the nonconstant conditional expectation \(f(Z)\) certifies correlation.
In the shrinking-circle model the positive same-circle lower bound first forces \(0<I_n=\int_{|z|=r_n}w\,d\mu<\infty\) for any putative finite positive row weight.
Integrating the row inequality over that circle then forces \(R\ge p_n^2/r_n^2\), which grows as \(2^{n/2}\) even though the scalar coordinate has both canonical domains.

For the side-one equilateral model, \(\kappa^2=3\), and at vertex three positivity gives \(\lambda\le e(3-\lambda)/(1-e)\), hence \(\lambda\le3e\).
The forced edge coefficient is thus at least \(3q(1-e)/(2e)\), with feasible coefficients for \(\lambda=0\).
The two small sites have curvature rows \(6eq\), whereas their common edge has gap times curvature kernel \(3q\), which violates (1) for small \(e\).
For the jump Laplacian the antisymmetric mode has eigenvalue \(9eq\) and the symmetric mean-zero mode has eigenvalue \(3e\).
In value coordinates their \((1,2)\) projection entries are \(-1/2\) and \(q/2\), since the constant projection contributes \(e\).
Taking square roots and dividing the negative entry by \(m_2=e\) gives exactly \(\sqrt3(\sqrt{3q}-q)/(2\sqrt e)\).
The limit diverges on a fixed unit edge.
Normal marginal diffuseness excludes this atomic construction from the actual-vacuum setting, and the unrestricted mixed canonical domain implication remains open.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Finding](#finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Finding](#finding) | [Fixed candidate](../../claims/Yin_C_F0291_v1.md#decision-candidate) | Complete candidate of 2026-11-14T15:58 and the nine declared dependency interfaces. |
| [Finding](#finding) | [Statement](../../claims/Yin_C_F0291_v1.md#statement) | Diffuse inequalities, actual weighted vacuum, both canonical domains and commutators under (3), examples and finite-certificate obstructions. |
| [Finding](#finding) | [Argument](../../claims/Yin_C_F0291_v1.md#argument) | Four-point geometry, measure classes, weighted propagation and energy, uniform and pointwise limits, two slices, examples and exact three-site calculations. |
| [Finding](#finding) | [Curvature row theorem](../../claims/Yin_C_F0078_v2.md#statement) | Coordinate-local application of the two support bounds and passage of the original generator commutators to bounded vectors. |
| [Finding](#finding) | [Original curvature energy](../../claims/Yin_C_F0078_v1.md#argument) | Finite symmetric polynomial approximation, energy (15) using the row mass norm, actual mixed-graph identities (19)–(20), and analytic-unitary limits. |
| [Finding](#finding) | [Two-slice domain theorem](../../claims/Yin_C_F0072_v1.md#statement) | Original right-slice closure and Hilbert adjoint domains from bounded right and left slices on the weakly dense star core. |
| [Finding](#finding) | [Liberation vacuum](../../claims/Yin_C_F0238_v1.md#statement) | Commutator with \(Z^*\), phase for \(i\gamma\), and the squared-gap spectral identity at the distinguished coordinate. |
| [Finding](#finding) | [Marginal tensor adjoint](../../claims/Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Cancellation for symmetric finite kernels, actual vacuum and absolute continuity of its liberation spectral measure. |
| [Finding](#finding) | [Scalar geometric criterion](../../claims/Yin_C_F0255_v1.md#statement) | Finite total curvature under full actuality and the converse scalar application using maximal linear density on two segments. |
| [Finding](#finding) | [Commuting drift criterion](../../claims/Yin_C_F0283_v1.md#statement) | Represented actual vacua for the real-part drift with standard semicircular noise and its off-diagonal squared-gap density. |
| [Finding](#finding) | [Shrinking-circle obstruction](../../claims/Yin_C_F0143_v1.md#statement) | Radius and mass parameters, actual scalar domains and same-circle lower bound for the positive-weight obstruction. |
| [Finding](#finding) | [Normal diffuseness](../../claims/Yin_C_F0076_v1.md#statement) | Exclusion of atomic marginals under full starred actuality and applicability of the actual mixed tensor-leg graphs. |

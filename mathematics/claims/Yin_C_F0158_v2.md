---
author: Yin
---
# Paired quadratic adjoint estimates at selfadjoint and unitary normal coordinates

## Current assessment
[Selected decision](#decision-reviewed-quadratic)

## Statement

Let (M,tau) be a finite von Neumann algebra with faithful normal probability trace, H=L2(M,tau), Omega=1 and P_Omega the projection onto C Omega.
Let X=(X_1,...,X_d) be a bounded normal generating tuple and let
\[
 \mathcal P=\mathbb C\langle X_1,\ldots,X_d,X_1^*,\ldots,X_d^*\rangle
\]
be its represented full starred algebra.
Assume the full ACSY condition: complex-linear outer-bimodule derivations delta_j:P -> H tensor_2 H satisfy delta_j(X_k)=delta_jk 1 tensor 1 and have actual Hilbert adjoint vacua xi_j=delta_j*(1 tensor 1) in H.
No joint independence assumption is imposed.
Inner products are linear in the second variable, and the outer actions are a dot(u tensor v)dot b=au tensor vb.

Fix a coordinate i, write delta=delta_i and xi=xi_i, and define on P
\[
 T_\ell(a)=\delta^*(a\otimes1),\qquad
 T_r(a)=\delta^*(1\otimes a).
\]
Both displayed elementary tensors belong to the actual Hilbert adjoint domain, as justified in the argument.
The following conclusions hold on the whole mixed starred core, for arbitrary a in P.
The other coordinates may be arbitrary normal elements, with no line, circle or graph restriction.

**Selfadjoint coordinate.**
If X_i is selfadjoint, then xi is selfadjoint and
\[
 \|T_\ell(a)\|_2^2
  =\operatorname{Re}\langle T_\ell(a^*a),\xi\rangle,
 \qquad
 \|T_r(a)\|_2^2
  =\operatorname{Re}\langle T_r(aa^*),\xi\rangle.
 \tag{S1}
\]

**Unitary coordinate.**
If X_i=U is unitary, set zeta=i(1-U*xi).
Then zeta is selfadjoint in L2(M), tau(zeta)=0, and
\[
 \|T_\ell(a)\|_2^2+\|T_\ell(a)-aU\|_2^2
   =\operatorname{Re}\langle T_\ell(a^*a),2\xi-U\rangle,
 \tag{S2}
\]
\[
 \|T_r(a)\|_2^2+\|T_r(a)-Ua\|_2^2
   =\operatorname{Re}\langle T_r(aa^*),2\xi-U\rangle.
 \tag{S3}
\]

**Finite-family domination and the paired estimates.**
In the selfadjoint case put v=xi and C=||xi||2.
In the unitary case put v=2xi-U and
\[
 C=\|2\xi-U\|_2
   =\sqrt{4\|\xi\|_2^2-3}
   =\sqrt{1+4\|\zeta\|_2^2}.
 \tag{S4}
\]
For every positive integer n and every a_1,...,a_n in P,
\[
 \sum_{k=1}^n\|T_\ell(a_k)\|_2^2
 \le\operatorname{Re}\left\langle
     T_\ell\!\left(\sum_{k=1}^n a_k^*a_k\right),v\right\rangle
 \le C\left\|T_\ell\!\left(\sum_{k=1}^n a_k^*a_k\right)\right\|_2,
 \tag{S5}
\]
\[
 \sum_{k=1}^n\|T_r(a_k)\|_2^2
 \le\operatorname{Re}\left\langle
     T_r\!\left(\sum_{k=1}^n a_ka_k^*\right),v\right\rangle
 \le C\left\|T_r\!\left(\sum_{k=1}^n a_ka_k^*\right)\right\|_2.
 \tag{S6}
\]
The first inequalities are equalities for a selfadjoint coordinate.
For a unitary coordinate their differences are respectively the sums of the residual squared norms in (S2) and (S3).
Taking n=1 proves the requested left a*a and right aa* quadratic estimates with the common constant C.
In the unitary case this improves the sufficient v1 constant 2||zeta||2+1; no optimality is asserted for general joint laws.

In particular the paired estimates hold at every coordinate of any mixed selfadjoint/unitary tuple satisfying A.
This statement concerns the original prescribed delta_i and its actual one-sided adjoints.
It does not assert that those original derivations are real, or give a new unrestricted implication A implies S for all normal tuples.
The conclusion for a distinguished coordinate imposes no claim about the other coordinates' quadratic estimates.

## Argument

### Existing inputs and the positive-input pairing

[C_F0076 Part 1](Yin_C_F0076_v1.md#statement) supplies delta_i(X_j*)=0 for j different from i under the exact normal ACSY hypotheses.
Its tensor-adjoint argument places every elementary P tensor P vector in Dom(delta_i*), so T_ell and T_r above are actual operators on the stated core.
Only Part 1 is used; the later Hilbert-tensor second-derivative conclusions are unnecessary here.

The real unitary twist, its exact first-order coassociativity defect and energy formula are from [C_F0043 Section 3](Yin_C_F0043_v1.md#3-a-unitary-polynomial-core-has-the-required-two-bounds), particularly equations (6)--(13).
The [mixed-coordinate verification in C_F0071 v2](Yin_C_F0071_v2.md#reverse-implication-for-mixed-selfadjointunitary-tuples) already checks that generators with zero derivative do not change these identities.
C_F0076 supplies the same zero starred-generator property for arbitrary other normal coordinates.
The selfadjoint case uses precisely the real coassociative energy estimate in [Mai15-U002](../audits/literature/Mai15/Yin_U002.md#mai15-u002), with the actual L2 codomain and right aa* orientation recorded there.
These adequate local inputs were checked before the deduction; no additional external theorem or priority claim is used.

For any positive b in P, actual adjoint duality gives
\[
 \tau(b)=\langle X_i,T_\ell(b)\rangle
        =\langle X_i,T_r(b)\rangle.
 \tag{Q2}
\]
Consequently, for a unitary coordinate,
\[
 \|a\|_2^2=\tau(a^*a)\le\|T_\ell(a^*a)\|_2,
 \qquad
 \|a\|_2^2=\tau(aa^*)\le\|T_r(aa^*)\|_2.
 \tag{Q3}
\]
No boundedness of the one-sided maps H -> H is used.

### The unitary coordinate and its real twist

Suppose a finite normal generating tuple satisfies the actual ACSY condition on its represented full starred core P.
Fix a unitary coordinate U and its prescribed derivation delta.
It kills the other generators by prescription and their adjoints by C_F0076 Part 1.
The inverse product rule forces delta(U*)=-U* tensor U*.
Consequently delta has algebraic tensor range.
No independence hypothesis is imposed.

For the inner action I_(c tensor d)(u tensor v)=uc tensor dv, put
\[
 \beta=\mathrm i I_{U\otimes1}\delta,
 \qquad B=(\mathrm{id}\otimes\tau)\beta,
 \qquad \zeta=\beta^*(1\otimes1).
 \tag{Q5}
\]
The inspected C_F0043 formulas apply unchanged with the other coordinates arbitrary normal elements, because their beta derivatives and those of their adjoints are zero.
Thus beta is real, its actual vacuum zeta is selfadjoint, and on P
\[
 B^*(q)=q\zeta-Bq,
 \qquad
 (\beta\otimes\mathrm{id})\beta
 -(\mathrm{id}\otimes\beta)\beta=\mathrm i\kappa\beta,
 \quad\kappa(u\otimes v)=u\otimes1\otimes v.
 \tag{Q6}
\]
Here B* denotes the actual Hilbert adjoint restricted to P.
The actual tensor-adjoint formula also gives
\[
 \zeta=-\mathrm iT_\ell(U^*)
       =\mathrm i(1-U^*\xi),
 \qquad \tau(\zeta)=0.
 \tag{Q7}
\]
The last equality is the vacuum pairing with beta(1)=0.

Write T_beta=B* on P.
C_F0043 equation (13), expansion of ||q zeta-Bq||2 squared, and reality for q*q give the exact real-part identity
\[
 \|T_\beta(q)\|_2^2
 =\operatorname{Re}\langle T_\beta(q^*q),\zeta\rangle
  +\operatorname{Re}\langle\mathrm iT_\beta(q),q\rangle.
 \tag{Q8}
\]
To check the sign of the defect term, equation (13) contributes minus Re<iBq,q>.
Since Bq=q zeta-T_beta(q), and tau(zeta q*q) is real, Re<i q zeta,q>=0, leaving plus Re<iT_beta(q),q>.
The nondefect term is the same real energy calculation as Mai15-U002, with all products of zeta taken only with bounded core coefficients.
In particular no derivative of zeta or B*(q) is assumed.

The original right contraction E=(id tensor tau)delta satisfies E=-i rho(U*)B on P, where rho(U*) is right multiplication.
Because right multiplication by U preserves P and is unitary on H, the actual adjoints obey
\[
 T_\ell(a)=\mathrm i B^*(aU).
 \tag{Q9}
\]
The identity [B,U]=i U P_Omega on the core P gives by actual adjoint pairing
\[
 [B^*,U^*]=\mathrm i P_\Omega U^*\quad\text{on the core P}.
 \tag{Q10}
\]
For b=a*a and q=aU this yields
\[
 T_\beta(q^*q)
 =B^*(U^*bU)
 =-\mathrm i U^*T_\ell(b)+\mathrm i\tau(b)1.
 \tag{Q11}
\]
The scalar term has zero pairing with zeta by (Q7).
Equations (Q8)--(Q11) therefore imply
\[
 \|T_\ell(a)\|_2^2
 =\operatorname{Re}\langle-\mathrm iU^*T_\ell(a^*a),\zeta\rangle
  +\operatorname{Re}\langle T_\ell(a),aU\rangle
 \le \|\zeta\|_2\|T_\ell(a^*a)\|_2
       +\|T_\ell(a)\|_2\|a\|_2.
 \tag{Q12}
\]

### Completing the square in the original adjoint map

Keep the exact equality in (Q12), before its norm estimate.
Since i U zeta=xi-U and the inner product is linear in its second variable,
\[
 \langle-\mathrm iU^*T_\ell(b),\zeta\rangle
   =\langle T_\ell(b),\mathrm iU\zeta\rangle
   =\langle T_\ell(b),\xi-U\rangle.
\]
Thus, for b=a*a,
\[
 \|T_\ell(a)\|_2^2
 =\operatorname{Re}\langle T_\ell(b),\xi-U\rangle
  +\operatorname{Re}\langle T_\ell(a),aU\rangle.
 \tag{Q13}
\]
Equation (Q2) and conjugate symmetry give Re<T_ell(b),U>=tau(b)=||a||2 squared.
Expanding the residual square in (S2) therefore gives
\[
 \begin{aligned}
 \|T_\ell(a)\|_2^2+\|T_\ell(a)-aU\|_2^2
 &=2\|T_\ell(a)\|_2^2+\|a\|_2^2
       -2\operatorname{Re}\langle T_\ell(a),aU\rangle\\
 &=2\operatorname{Re}\langle T_\ell(b),\xi-U\rangle
       +\operatorname{Re}\langle T_\ell(b),U\rangle\\
 &=\operatorname{Re}\langle T_\ell(b),2\xi-U\rangle.
 \end{aligned}
 \tag{Q14}
\]
All products involve only bounded core coefficients and L2 vectors.
In particular the residual T_ell(a)-aU is an actual L2 vector and no differentiated vacuum is required.

Apply the same argument to the opposite algebra, with delta_op=flip composed with delta.
The flip is a unitary on the Hilbert tensor space, preserves 1 tensor 1, and intertwines the original derivation with an outer derivation for the opposite product.
Consequently delta_op has the same actual vacuum xi, and its left adjoint is the original T_r.
The opposite products a* times a and a times U are respectively the original aa* and Ua.
Its real-twist vacuum is zeta_op=i(1-xi U*)=U zeta U*, and its completing vector is the same original Hilbert vector 2xi-U.
Thus (Q14) in the opposite algebra is exactly (S3), including the indicated order Ua in the residual.

The original vacuum pairing gives <xi,U>=1 and ||U||2=1.
Hence
\[
 \|2\xi-U\|_2^2=4\|\xi\|_2^2-3.
\]
Also (Q7) gives ||zeta||2 squared=||1-U*xi||2 squared=||xi||2 squared-1.
Combining these identities proves (S4), including the reality of both square roots.
This constant is at most 2||zeta||2+1 because the square of that v1 constant minus C squared equals 4||zeta||2, a nonnegative number.
The original first-order defect has become the positive residual square, so no sign of that defect is discarded.

### The selfadjoint coordinate and finite families

For a selfadjoint coordinate of an arbitrary normal tuple satisfying A, C_F0076 Part 1 shows that its prescribed delta vanishes on all other starred generators.
It is therefore real, algebraic-core-valued and coassociative.
Mai15-U002 gives the actual identity ||T_ell(a)||2 squared=Re<T_ell(a*a),xi> and the selfadjoint vacuum xi.
Reality also gives T_r(a)=T_ell(a*)*, so applying the left identity to a* gives the right identity in (S1).
The real parts of the resulting pairings agree by traciality and xi=xi*.
This proves (S1) without adding a condition on the other normal coordinates.

Sum (S1), (S2) or (S3) over a finite family and use complex linearity of the actual maps.
This yields the fixed-vector pairings in (S5) and (S6), with equality after adding the respective nonnegative residual squares in the unitary case.
Cauchy-Schwarz gives the last inequalities, with exactly C=||v||2.
No minimax argument, matrix-amplification assumption or uniform-family adjoint-domain passage is needed: every sum is finite and belongs to the original core.
The case n=1 gives the asserted paired estimates.

## Development, version transition and self-check scope

The v1 project deduction was developed for Yin by the quadratic_haar_graph subagent under the authorized F0011 paired-estimate investigation.
Root proposed the coordinate-local normal-tuple formulation after the initial mixed-tuple calculation.
The complete [v1 candidate](Yin_C_F0158_v1.md#decision-initial) remains fixed with its original Young-inequality proof and constant 2||zeta||2+1.

On 2026-10-16T03:11, root supplied the completion of the square before applying norms, extracting the fixed vector 2xi-U and a positive residual from the v1 exact identity.
The quadratic_haar_graph developer separately checked that refinement's Hilbert inner-product sign, opposite-product order, constant formula and finite-family summation, then incorporated it here.
This coordinated development is not independent review.
The stronger exact identities and finite-family conclusion are substantive mathematics, so this version preserves v1 and gives the full argument rather than silently replacing its statement.

The author also checked the actual one-sided adjoint domains, the sign in (Q8), the right-multiplication transport (Q9), the adjoint commutator (Q10), the scalar cancellation in (Q11), the exact equality before the norm estimate in (Q12), and the absence of a freeness premise.
This complete stronger candidate awaits a separately arranged fresh independent review covering v2.
No independent-review assessment is carried from its inputs or the earlier candidate to this deduction.
The auxiliary bounded-H condition remains in [D_F0006](../drafts/Yin_D_F0006.md#the-maps-are-actual-slice-adjoints), and the free-Haar benchmarks and spectral-graph normalization limit remain in [D_F0007](../drafts/Yin_D_F0007.md).
They are not dependencies of this proof.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-16T03:11 |
| status | open |
| reason | Complete strengthened coordinate-local candidate retained for fresh independent review: exact positive-square identities, the smaller unitary constant and fixed-vector domination for every finite family. The full arbitrary-normal problem remains outside the statement. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact selfadjoint identities, unitary identities with positive residual squares, finite-family bounds and original one-sided estimates at a distinguished selfadjoint or unitary coordinate of an arbitrary normal ACSY tuple. |
| argument | [Argument](#argument) | Actual real twist and adjoint transport, exact defect, completion of the square, opposite-algebra right identity, constant formula, source selfadjoint identity and finite-family summation. |
| dependency | [C_F0076 Part 1](Yin_C_F0076_v1.md#statement) | Actual tensor-adjoint domains and zero derivative at every other starred normal generator; Parts 2 and 3 are not used. |
| dependency | [C_F0043 Section 3](Yin_C_F0043_v1.md#3-a-unitary-polynomial-core-has-the-required-two-bounds) | Real unitary twist, actual vacuum and polynomial adjoint, exact defect and energy formula (13), with the zero-derivative extension checked here. |
| dependency | [Mai15-U002](../audits/literature/Mai15/Yin_U002.md#mai15-u002) | Exact real coassociative quadratic identity and its actual-domain assumptions for the distinguished selfadjoint coordinate, including the right aa* orientation. |

### Decision reviewed-quadratic

| Field | Value |
| --- | --- |
| date | 2026-10-16T03:23 |
| status | proved |
| reason | Adopt the complete quadratic-estimate statement and argument after the separately organized full-proof review; retain its precise coordinate or radial scope and all actual-domain requirements. The unrestricted normal A-to-S problem remains unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire fixed statement, hypotheses and quantitative conclusions. |
| argument | [Argument](#argument) | Complete fixed argument and its exact direct-input applications. |
| dependency | [C_F0076 Part 1](Yin_C_F0076_v1.md#statement) | Actual tensor-adjoint domains and zero derivative at every other starred normal generator; Parts 2 and 3 are not used. |
| dependency | [C_F0043 Section 3](Yin_C_F0043_v1.md#3-a-unitary-polynomial-core-has-the-required-two-bounds) | Real unitary twist, actual vacuum and polynomial adjoint, exact defect and energy formula (13), with the zero-derivative extension checked here. |
| dependency | [Mai15-U002](../audits/literature/Mai15/Yin_U002.md#mai15-u002) | Exact real coassociative quadratic identity and its actual-domain assumptions for the distinguished selfadjoint coordinate, including the right aa* orientation. |
| review | [Independent full-proof review](../audits/reviews/Yin_R_F0167_v1.md#conclusion) | Exact statement, complete argument and declared direct dependencies at the scopes retained in the review bindings. |


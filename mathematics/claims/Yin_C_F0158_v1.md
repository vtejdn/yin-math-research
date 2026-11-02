---
author: Yin
---
# Paired quadratic adjoint estimates at selfadjoint and unitary normal coordinates

## Current assessment

[Selected decision](#decision-initial)

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
These vectors belong to the actual Hilbert adjoint domain, as justified in the argument.
The following conclusions hold on the whole mixed starred core, for arbitrary a in P.

If X_i is selfadjoint, then
\[
 \|T_\ell(a)\|_2^2\le\|\xi\|_2\|T_\ell(a^*a)\|_2,
 \qquad
 \|T_r(a)\|_2^2\le\|\xi\|_2\|T_r(aa^*)\|_2.
 \tag{Q1}
\]
If X_i=U is unitary, set
\[
 \zeta=\mathrm i(1-U^*\xi).
\]
Then zeta is selfadjoint in L2(M), tau(zeta)=0, and the two inequalities in (Q1) hold with the common constant 2||zeta||2+1 in place of ||xi||2.
The other coordinates may be arbitrary normal elements, with no line, circle or graph restriction.
In particular both quadratic estimates hold at every coordinate of any mixed selfadjoint/unitary tuple satisfying A.

This statement concerns the original prescribed delta_i and its actual one-sided adjoints.
It is not an assertion that those original derivations are real, or a new unrestricted implication A implies S for all normal tuples.
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
Young's inequality absorbs one half of the left side.
Equation (Q2), with X=U and ||U||2=1, absorbs the resulting ||a||2 squared.
Consequently
\[
 \boxed{\|T_\ell(a)\|_2^2
 \le(2\|\zeta\|_2+1)\|T_\ell(a^*a)\|_2.}
 \tag{Q13}
\]

Apply the same argument to the opposite algebra, with delta_op=flip composed with delta.
It has the same actual vacuum xi, and its left adjoint is the original T_r.
The opposite product a* times a is the original aa*.
Its real-twist vacuum is
\[
 \zeta_{\mathrm{op}}=\mathrm i(1-\xi U^*)=U\zeta U^*,
 \qquad \|\zeta_{\mathrm{op}}\|_2=\|\zeta\|_2.
\]
This proves
\[
 \boxed{\|T_r(a)\|_2^2
 \le(2\|\zeta\|_2+1)\|T_r(aa^*)\|_2.}
 \tag{Q14}
\]
The constants are finite for each fixed tuple and coordinate, and no bounded-H extension was used in this argument.

For a selfadjoint coordinate of an arbitrary normal tuple satisfying A, C_F0076 Part 1 similarly shows that its prescribed delta vanishes on all other starred generators.
It is therefore real, algebraic-core-valued and coassociative.
Mai15-U002 therefore gives the same two inequalities with C_ell=C_r=||xi||2.
Thus the candidate conclusion is the paired estimates at every selfadjoint or unitary coordinate of an arbitrary correlated normal tuple satisfying A.
In particular both estimates hold at every coordinate of a mixed selfadjoint/unitary tuple.
This is a proof candidate about the original prescribed derivations, not merely their real twists.
It does not extend the conclusion to arbitrary nonlinear spectral graphs or all normal tuples.

## Development and self-check scope

This project deduction was developed for Yin by the quadratic_haar_graph subagent under the authorized F0011 paired-estimate investigation.
Root proposed the coordinate-local normal-tuple formulation after the initial mixed-tuple calculation.
The author checked the actual one-sided adjoint domains, the sign in (Q8), the right-multiplication transport (Q9), the adjoint commutator (Q10), the scalar cancellation in (Q11), the L2 rather than operator-norm error term in (Q12), the opposite-algebra order and the absence of a freeness premise.
The record retains a complete proof candidate for a separately arranged independent review.
It does not carry an independent-review assessment from its inputs to this new deduction.
The auxiliary bounded-H condition remains in [D_F0006](../drafts/Yin_D_F0006.md#the-maps-are-actual-slice-adjoints), and the free-Haar tests and spectral-graph normalization limit remain in [D_F0007](../drafts/Yin_D_F0007.md).
They are not dependencies of this argument.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-16T03:06 |
| status | open |
| reason | Complete coordinate-local quadratic-estimate deduction retained for independent review, with the actual unitary twist, absorbed first-order defect and correct right aa* product. The full arbitrary-normal problem remains outside the statement. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Both original one-sided quadratic estimates at any selfadjoint or unitary coordinate of an arbitrary normal ACSY tuple, with the stated constants and all-core quantifiers. |
| argument | [Argument](#argument) | Positive-input pairing, actual real-twist energy calculation, adjoint transport, scalar cancellation, Young absorption, opposite-algebra right estimate and source selfadjoint case. |
| dependency | [C_F0076 Part 1](Yin_C_F0076_v1.md#statement) | Actual tensor-adjoint domains and zero derivative at every other starred normal generator; Parts 2 and 3 are not used. |
| dependency | [C_F0043 Section 3](Yin_C_F0043_v1.md#3-a-unitary-polynomial-core-has-the-required-two-bounds) | Real unitary twist, actual vacuum and polynomial adjoint, exact defect and energy formula (13), with the zero-derivative extension checked here. |
| dependency | [Mai15-U002](../audits/literature/Mai15/Yin_U002.md#mai15-u002) | Real coassociative quadratic identity and its actual-domain assumptions for the distinguished selfadjoint coordinate, including the right aa* orientation. |

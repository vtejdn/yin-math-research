---
author: Yin
---
# Independent review of the realized weighted-liberation lower-bound obstruction

Review performed and recorded: 2026-10-14T19:33.
Human record author: Yin.
This is a separately organized AI mathematical review, not a personal human inspection.

## Arrangement and scope

The reviewer examined the complete fixed [C_F0146 v1](../../claims/Yin_C_F0146_v1.md), selected by its initial decision dated 2026-10-14T19:30, and all three exact direct inputs.
The normal-branch author developed the three-block semicircular construction; root contributed the finite-edge lead and checked two constants.
Neither development check is treated as independent evidence.
The reviewer received the candidate's target and the two claimed constants in the assignment, but did not participate in this construction and did not read its D10 development or proof-generation discussion.

This agent previously developed the distinct Haar/Poisson mixed-word tests and the geometry applicability investigation in D_F0004.
Those are related investigations of the same proposed universal inequality, and are not independent reviews of their own reasoning.
They neither construct nor prove the present semicircular example and are not proof inputs here.
This relationship is disclosed rather than deriving independence from a different task label.

The present review covers the full nonexistence statement, represented free-product substitution, both reference adjoint vacua, the transformed actual vacuum, weighted tensor-adjoint domain, the exact fourth-moment norm, edge restriction, normalized mixed-corner law, analytic-unitary graph limit, both trace factors, and the limited consequence for the unrestricted normal question.
The three direct inputs are examined at the exact scopes below.
No numerical diagnostic or proof-assistant check is used.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0146 statement](../../claims/Yin_C_F0146_v1.md#statement) | Failure of every law-independent numerical lower-bound constant for finite nonnegative symmetric marginal weights, actual bounded liberation vacua and norm-one analytic-core unitaries; exact t-dependent counterexamples and no normal ACSY separation. |
| [Conclusion](#conclusion) | [C_F0146 argument](../../claims/Yin_C_F0146_v1.md#argument) | All of SC1--SC9: represented algebraic substitution, actual adjoints, projection weight, orthogonal fourth moments, corner restriction and normalization, analytic original graph convergence and divergent ratio. |
| [Conclusion](#conclusion) | [ACSY24-U004](../literature/ACSY24/Yin_U003.md#acsy24-u003) | Equation (1) of the derivation-adjoint subsection, with inner product linear in the second variable and bounded reference-core tensor coefficients. Only that actual tensor-adjoint formula is used, after checking the reference vacua; other results and recorded uncertainties of the source unit are not imported. |
| [Conclusion](#conclusion) | [C_F0077 marginal adjoint](../../claims/Yin_C_F0077_v1.md#the-marginal-restriction-of-the-actual-liberation-adjoint) | Formula (S1) for the actual finite marginal tensor g. The row/column correction cancels by symmetry. No general marginal restriction equality, composition bootstrap or abstract realization assertion is needed. |
| [Conclusion](#conclusion) | [NS06-U003](../literature/NS06/Yin_U004.md#ns06-u004) | Equation (14.5), normalized corner trace and Theorem 14.10 at the stated edition/pages; the local mixed-corner adaptation and fourth-moment calculation are checked here. Corollary 14.12 is not applied to p,q. |

## Represented algebra and actual reference operators

The tracial free product with the three strictly positive masses is faithful.
Its algebraic reference core is the algebraic free product of N with the polynomial algebra of a standard semicircular variable.
Reduced-word orthogonality and the nondegenerate semicircular polynomial law leave no additional algebraic relations.
The map fixing N and sending S to the displayed T is a star-preserving substitution: symmetry of the real matrix gives T=T*.
Its inverse fixes N and sends the indeterminate to the same block formula with reciprocal scalar entries.
Orthogonality of the p_i makes the two compositions exactly the identity on the generator.
Thus the N,T core is the same represented core, with a valid partial liberation vanishing on T.
This is not an assumed derivative on a quotient with unchecked relations.

On the free reference core, liberation of N against S has zero vacuum functional, as is checked by reduced centered words and the product rule.
The semicircular derivative has actual vacuum S, with its extension to the free N factor checked by the same reduced-word pairing.
These are actual Hilbert adjoint assertions, not just choices of formal symbols.
Solving the derivative of T gives SC2; the difference from the free liberation is precisely I_Q partial_S, because both sides vanish on N and have the same value on S.

For the convention in the claim, pairing I_Q partial_S against the tensor vacuum gives partial_S* applied to the componentwise tensor adjoint Q*.
This is the tensor adjoint without a flip.
In Q* the two nontrivial sums have factors T p_i tensor p_j and p_i tensor p_j T.
The ACSY formula gives their main terms -TR and RT.
The respective correction sums are plus sum tau(p_i)p_j and minus sum tau(p_j)p_i, so they cancel.
The S tensor 1 minus 1 tensor S part also cancels.
Consequently gamma*1=RT-TR and (i gamma)*1=-i[R,T], with the stated sign for an inner product linear in its second variable.

All these tensors have bounded reference-core factors, so the imported adjoint formula supplies actual domains for their finite sum.
The vacuum is bounded and selfadjoint after multiplication by -i.
The real derivation i gamma is therefore closable by its dense algebraic-tensor adjoint domain.
This also gives the appropriate actual closure in which to interpret subsequent first-derivative graph limits.

## Actual weighted vacuum and its exact size

The tensor g=p tensor q+q tensor p is a nonnegative projection in N tensor N, is real and symmetric, and satisfies sqrt(g)=g.
Choose a normal finite-spectrum generator for N; its spectral projections are polynomials in that generator, so the finite marginal part of C_F0077 applies directly.
Its row and column functions agree.
Thus beta*g=S_g zeta is an actual adjoint vector, with no approximation or enlarged unproved restriction domain.
In particular, only the p-to-q and q-to-p blocks of the full vacuum remain.

Multiplying R and T blockwise gives the coefficient a_kj/a_ik-a_ik/a_kj in SC4.
For the p-to-q block these coefficients are -3/2,3/2,0.
The outside r block is exactly zero, not merely asymptotically small.
For i different from j, apply the stated fourth-moment formula to

\[
 \tau(p_jS p_kS p_iS p_lS p_j).
\]

The first noncrossing-pairing term vanishes because p_i p_j=0; the second is delta_kl tau(p_i)tau(p_k)tau(p_j).
This proves both orthogonality of the two surviving middle blocks and their exact squared norms.
One off-diagonal vacuum block contributes

\[
 \frac94\left(\frac t2\right)^2
             \left(\frac t2+\frac t2\right)=\frac9{16}t^3.
\]

The transposed block is orthogonal to it and has the same norm.
Therefore the actual weighted vacuum satisfies norm-squared 9t^3/8, exactly as claimed.
No norm of the entire unweighted vacuum is substituted for this quantity.

## Edge restriction and the mixed-corner law

Inserting p_u tensor p_v into each of the four SC2 terms gives exactly SC6: the first coefficient is 1-a_iu/a_iv and the second is a_vj/a_uj-1.
For the selected edge, the outside row and column entries of a are both 1, so every outside tensor term vanishes.
Also I_g gamma(e)=0.
On p,q this derivative has the ordinary two-atom liberation values with corner identity e; on the compressed T it is zero.
The product rule therefore proves equality with the represented corner liberation on every corner-core word.
This is equality of actual finite tensor values, not an identification of an arbitrary compression of an unbounded operator.

The normalized trace is tau_e=t^-1 tau.
The scalar law of eSe/sqrt(t) follows from Theorem 14.10.
Its mixed law with eNe needs the separate mixed-moment argument, since e is not free from p and q.
In the noncrossing-pairing recursion from (14.5), each pair brings a tau on the e-supported coefficients; division by t per paired pair converts it into tau_e.
Thus the complete mixed recursion agrees with a standard semicircle free from the two equal-mass atoms in the corner.
Faithfulness then gives norm(V)=2.
The joint normalized corner law, including the represented two-atom derivative expressions, is independent of t.

For source verification, the reviewer directly read the retained NS06 PDF pages 245--248, printed pages 228--231: formula (14.5), the normalized trace convention, Theorem 14.10 and its proof text, and the hypothesis of Corollary 14.12.
This confirms the edition/page and applicability match of U003.
It is not a fresh independent audit of the book's general combinatorial proof and all its dependencies.
ACSY24-U004 is reused at its recorded exact equation (1) proof scope; no new whole-paper reading is claimed.
C_F0077 is reused at the finite identity already independently reviewed by this agent, with its present hypotheses explicitly checked above.

## Negative coefficient, analytic graph and the two trace factors

In the normalized corner, the partial trace of V is zero.
Each reciprocal-coefficient row has averaged value 3/4, and all other scalar first-moment corrections vanish.
Hence C^(e)V=V-(3/4)T_e'.
The free second moments give tau_e(V T_e')=(2+1+1+2)/4=3/2 and tau_e(V^2)=1.
The exact real quadratic coefficient is therefore 1-(3/4)(3/2)=-1/8.

There is a positive radius independent of t in which the binomial expansion of sqrt(e-s^2 V^2) converges in operator norm and in the first-derivative graph.
Indeed norm(V)=2, and the derivative of V^k is bounded in the Hilbert tensor norm by k norm(V)^(k-1) times norm(gamma_e(V)).
The normalized corner law fixes the latter constant.
These estimates also control the expansion's remainder after partial trace and scalar pairing.

The expansion is

\[
 u_s=ie+sV-\frac i2s^2V^2+O(s^4),
 \qquad
 C^{(e)}u_s=sC^{(e)}V-\frac i2s^2C^{(e)}V^2+O(s^4)
\]

in the respective norm and graph senses.
The possible linear scalar term vanishes because tau_e(C^(e)V)=0.
Anti-reality of gamma_e makes tau_e(C^(e)V^2) purely imaginary, so the extra order-squared term has zero real part.
The remaining quadratic term is -s^2/8 and the mixed remainder is O(s^3).
This verifies SC8 with a fixed sufficiently small s>0 independent of t; no merely formal expansion or uniform-in-t unweighted graph estimate is assumed.

In the whole algebra V belongs to the original N,T core by the reciprocal substitution.
For each t, the same power-series estimate applies to the original gamma at a=sV, with norm(a)<1.
It puts the displayed whole-algebra unitary in the actual original first-derivative graph.
The finite insertion I_g is bounded on the coarse Hilbert space, so its graph values are the same limits.
Since I_g gamma(r)=0, its weighted derivative is entirely supported in the e tensor e corner and agrees there with the corner expression just checked.

The partial trace tau on the second corner leg is t times tau_e.
The resulting vector is supported in e, so the scalar pairing with ir vanishes, while tau on the remaining corner contributes another t.
The form is exactly t^2 q(s).
Dividing by 9t^3/8 gives 8[-q(s)]/(9t), which tends to infinity.
For any proposed finite numerical constant one can choose t sufficiently small.
All masses stay strictly positive for every example, and no limiting algebra at t=0 is asserted.

## Conclusion

**Pass for the complete fixed C_F0146 v1 statement and argument, with all three declared dependency scopes covered.**
No mathematical correction is required.
The construction is an actual represented finite tracial example, its square-root tensors lie in the actual adjoint domain, and the analytic unitary tests lie in the original first-derivative graphs.
The exact t-cubed denominator and t-squared negative numerator disprove the proposed law-independent arbitrary-weight estimate.

The conclusion is limited to that estimate.
The marginal here is atomic, the chosen edge projection is not asserted to be a normal-coordinate curvature kernel, and this review supplies no normal A-to-S separation or completion of T_F0011.
Adoption remains a separate decision of the responsible author and coordinating agent.

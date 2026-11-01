---
author: Yin
---
# Independent review of actual-vacuum restoration under polynomial linear coordinate changes

Review performed and recorded: 2026-10-14T18:11.
Human record author: Yin.
This is a separately assigned AI mathematical review, not a personal human inspection.

## Arrangement and scope

The reviewer did not develop or edit [C_F0141 v1](../../claims/Yin_C_F0141_v1.md).
Root assigned this fixed candidate after the separately completed C_F0140 review.
The disclosed development arrangement was that the author supplied the represented-relation and target-core approximation argument, while root supplied the pseudoinverse observation and the requirement to identify the h-coordinate canonical core.
The assignment also identified these steps as review priorities.
No D12, mutable development draft, proof-generation discussion or author explanation was read.
The complete fixed candidate, selected by its initial decision dated 2026-10-14T18:02, and its three exact direct inputs were examined.

This review covers the entire statement, all five proof sections and the stated scope.
It checks the two coefficient representations, the arbitrary supplied derivations, the actual spectral inverse and three-measure approximation, both canonical domains, the h correction with coefficients outside the target core, all coordinate commutators, uniqueness and the quantitative Y estimates.
Existing direct inputs are reused at their accepted scopes.
In particular the reviewer's earlier [C_F0139 review](Yin_R_F0146_v1.md#conclusion) is reused for the unchanged finite kernel-coefficient theorem; the present target-core inverse argument is checked independently in full.
No new primary-source PDF or proof-assistant verification was used, and previous source-inspection boundaries are not enlarged.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0141 statement](../../claims/Yin_C_F0141_v1.md#statement) | Exact finite-Fisher selfadjoint reference, polynomial linear coordinate change, explicit generation and coarse nonvanishing, A-to-S-to-F for both supplied canonical cores, both actual domains, Y bounds and uniqueness. |
| [Conclusion](#conclusion) | [C_F0141 argument](../../claims/Yin_C_F0141_v1.md#argument) | All five sections: represented starred relation, two distinct spectral actions, pseudoinverse, three-measure target-core convergence, actual core adjoints and both weak graph limits, and the h correction without enlarging the target derivation's domain. |
| [Conclusion](#conclusion) | [Dab10-U002](../literature/Dab10/Yin_U002.md#dab10-u002) | Sections 1-3: represented selfadjoint free difference quotients, canonical reference closures and actual adjoints on all M, operator-norm-to-L2 bounds and polynomial commutators. No bounded-H reference estimate is assumed. |
| [Conclusion](#conclusion) | [C_F0139 finite coefficients](../../claims/Yin_C_F0139_v1.md#statement) | Finite polynomial kernel coefficients only: both contraction bounds, their actual vacuum vectors, flip-star relation and actual core adjoint identity. The measurable coarse-L2 theorem and Sylvester corollary are not invoked. |
| [Conclusion](#conclusion) | [C_F0070 tensor interface](../../claims/Yin_C_F0070_v1.md#statement-and-interfaces) | Universal coarse-to-Hilbert-Schmidt identification, outer compatibility and vacuum contraction only. No normal-coordinate or automatic-continuity theorem is applied to the nonnormal target. |

## Exact premises and the two coefficient representations

The reference pair h,S is bounded, selfadjoint, generating and has its joint L2 conjugate system.
These are exactly the premises for Dab10-U002's specified canonical contractions, their actual all-M adjoint domains and the sufficient 4/5 core estimates.
In particular the reference conjugate xi_S is selfadjoint.
The proof never requires E or B_h bounded on H.
Polynomial coefficients in h lie in the represented reference core and are annihilated by partial_S, so each finite coefficient tensor falls within the kernel-algebra hypothesis of C_F0139.

The inner map I_F right-multiplies the first tensor factor and left-multiplies the second.
It is bounded and commutes with both outer actions, even though its factors need not commute with arbitrary M elements.
The outer map J_F left-multiplies the first factor and right-multiplies the second.
On the abelian marginal subspace both act as multiplication by the same scalar function F(s,t); this equality is not asserted on the whole coarse space.
The Hilbert-space multiplier F(L_h,R_h) is a third representation and must be treated separately.

The finite sums defining L_F and L_(F#) commute because their left coefficients commute with one another and their right coefficients commute with one another.
Thus their application to S gives the represented relation (8), with F#(s,t)=conjugate(F(t,s)).
Differentiation by any supplied Y derivation kills all the h coefficients and gives precisely J_F delta_Y(Y*)=F#.
There is no assumed value of the starred derivative in this step.

## Coarse injectivity, forced starred value and uniqueness

For any Borel set with mu measure zero, faithfulness makes its h spectral projection zero.
Consequently the spectral measure of every H vector for left or right h is absolutely continuous with respect to mu.
An elementary coarse tensor therefore has joint outer spectral measure absolutely continuous with respect to mu tensor mu.
The zero-set spectral projection of J_F annihilates every elementary tensor under the explicit nonvanishing assumption, hence annihilates the whole coarse space by density.
This proves the required injectivity, without claiming a uniform inverse bound.

The conditional-expectation projection onto L2(W*(h)) is bimodular.
Its tensor square reduces J_F and fixes F#.
Applying its complement to (9), and then injectivity, places delta_Y(Y*) in the marginal tensor subspace.
Its value is therefore the actual L2 function k=F#/F.
This L2 membership follows from the supplied Hilbert-valued derivation; it is not an additional unstated integrability premise.

Both I_F delta_Y and the restriction of partial_S are represented outer derivations.
Their values on h,Y,Y* are 0,F,F#, so they agree on the whole target star algebra.
The uniqueness argument is valid separately at either prescribed coordinate value: the difference of two candidate derivations kills h and Y, differentiation of (8) forces its Y* value to vanish, and the three generators determine the derivation.
No Hilbert-space multiplier injectivity or vacuum hypothesis is needed for this uniqueness argument.

## Actual vacuum, pseudoinverse and three simultaneous norms

For coefficients annihilated by delta_Y, the actual vacuum identity and the Leibniz rule give

\[
\delta_Y^*(a(h)^*\otimes b(h)^*)=a(h)^*v b(h)^*.
\]

Indeed the required pairing is the vacuum pairing applied to a(h) p b(h); cyclicity of the trace puts the displayed factors in exactly this order under the second-variable-linear convention.
Pairing partial_S=I_F delta_Y with the tensor vacuum therefore gives xi_S=overline(F)(L_h,R_h)v.
Density here is the L2 density of A_X, which follows from the explicit generation assumption.
The reference vacuum identity is legitimately restricted from A_0 to A_X.

The normal multiplier B=overline(F)(L_h,R_h) can have a kernel.
The equation xi_S=Bv implies that the vector spectral measure at xi_S gives the zero set of F no mass.
Closed joint spectral calculus then gives

\[
\overline{\beta}(L_h,R_h)\xi_S
 =1_{\{F\ne0\}}(L_h,R_h)v,
\qquad \beta=1/F\text{ off the zero set}.
\]

This is an actual spectral-domain assertion and proves beta belongs to L2(nu_xi), with norm at most norm(v).
No conclusion about the multiplier kernel on arbitrary H vectors is used.

The measure lambda in (14) is finite on the compact spectral square: F and F# are bounded there and nu_xi is finite.
The three squared beta integrals are respectively 1, norm(k) squared and norm(v_min) squared.
Thus beta belongs to L2(lambda), although it need not belong to unweighted coarse L2.
Complex polynomials in the two real coordinates are a selfadjoint uniformly dense algebra on this compact set; continuous functions are dense for this finite Borel measure.
Hence a single finite polynomial tensor sequence beta_n approximates all three norms at once.
Its two weighted coarse limits and the conjugated spectral vector limit are exactly (15).
This requires neither uniform boundedness of beta_n as multipliers nor unweighted coarse convergence.

## Target words, the adjoint and both Y domains

For finite beta_n, the represented derivation delta_n has generator values 0,F beta_n,F# beta_n on h,Y,Y*.
They converge in the Hilbert tensor space to the supplied target values.
On every fixed word in these three bounded generators the Leibniz formula has finitely many bounded outer factors, so it gives full target-core convergence.
The argument does not claim convergence on S or on every reference word.

The actual finite vacuum vectors v_n converge to v_min.
Passing to the limit in the vacuum pairing for each target polynomial proves that v_min is an actual vacuum vector for delta_Y.
Since the supplied v represents the same pairing and A_X is dense, v_min=v.
This is where the possible H-kernel component is removed.
The argument uses the target algebra and its actual vacuum, not an invalid transfer of coarse injectivity.

Applying flip-star to the convergence at p* gives convergence of the conjugate derivations at p.
Because the reference partial_S is real, these finite conjugate derivations are exactly the beta_n# derivations.
Their vacua are v_n*, so the second 4-times bound follows at the same constant.
No independent approximation of beta# in an unweighted tensor norm is needed.

For each p,q in A_X the finite actual adjoint pairings pass to the limit.
Multiplication of v_n by fixed bounded q is continuous in H, and the conjugate contractions converge.
This proves q belongs to the actual Hilbert adjoint domain of Q_Y and gives Q_Y*q=qv-F_0q.
The resulting bounds are exactly 4 norm(v) for Q_Y and F_0 and 5 norm(v) for Q_Y* on the core.
Density of the core adjoint domain proves closability.

Uniformly operator-norm bounded Kaplansky approximants from A_X converge in H to any a in M.
The two core bounds and weak-closedness of the respective graphs put a in Dom closure(Q_Y) and Dom Q_Y*.
Allowing arbitrarily small excess in the approximants' operator norms gives precisely the constants in (4).
This proves both actual domains, rather than selecting an unrelated Banach-space extension.

For a fixed p in A_X, the polynomial contraction identity is

\[
Q_Y(pq)-pQ_Y(q)=\Theta(\delta_Yp)q.
\]

Along uniformly bounded target approximants for an arbitrary a in M, weak graph limits identify the left side with K(pa)-pK(a).
The Hilbert-Schmidt right side is a bounded operator on H, so its values converge strongly.
This proves (20), including (19), on all bounded inputs.
No starred value or closure on a larger derivation domain is presumed.

## The supplied h core and the finite correction

The tensor C=partial_h Y is a finite sum of bounded factors c_l,d_l from A_0.
Such factors define a bounded inner map I_C commuting with the outer actions regardless of whether those factors are in A_X.
Thus partial_h restricted to A_X minus I_C delta_Y is an actual represented Hilbert-valued derivation on A_X.
Its values on h,Y are 1 tensor 1 and zero.
The already established uniqueness makes it the originally supplied delta_h, including its value on Y*.
This identifies the canonical core itself.

For p in A_X, apply (20) with p as the differentiated element and d_l in M as its input vector.
This does not differentiate d_l.
With delta_Y(p) initially expanded into elementary tensors, the trace identity tau(w d_l)=tau(d_l w) gives

\[
(\mathrm{id}\otimes\tau)I_C\delta_Y(p)
 =\sum_l\bigl(K(p d_l)-pK(d_l)\bigr)c_l.
\]

The equality extends by Hilbert tensor continuity.
It proves that B_h-Q_C(K)+rho(eta) on M restricts to the supplied Q_h, with eta=sum_l K(d_l)c_l in H.
In particular the correction never applies delta_Y to S or to any other coefficient outside A_X.

The correction is bounded from M with its operator norm to H.
For every q in M, direct Hilbert pairing reverses the bounded right factors and gives the actual adjoint value

\[
B_h^*q-\sum_l(K^*(q c_l^*))d_l^*+q\eta^*.
\]

The middle terms are legitimate because q c_l* belongs to M and M is contained in Dom K*.
The final right-multiplication term is legitimate for an H vector eta: cyclicity gives its actual adjoint value q eta* on M, without requiring eta bounded.
Thus the domain-M correction is closable and its adjoint contains M; restriction places M in the adjoint domain of the supplied core Q_h as well.
The uniform core bound and Kaplansky weak graph argument put M in Dom closure(Q_h).

There is also no hidden ambiguity between this closure and the displayed correction at bounded inputs.
The supplied core is a restriction of the closable domain-M correction, so its closure is contained in the latter's closure.
At every bounded a both are defined, and uniqueness of a closed graph value identifies their values.
Alternatively the original canonical core commutators pass by the same bounded-approximation argument used for Y.

For completeness, the orders in the full-M cancellation are correct.
From the reference polynomial commutators, [B_h,Y]=Theta(C).
Since right multipliers commute with left Y, \([Q_C(K),Y](a)=\sum_l P(a d_l)c_l=\Theta(C)(a)\).
The corresponding h commutator is zero.
Right multiplication by eta commutes with every bounded left multiplier on its domain M.
Consequently the resulting canonical h commutators are P at h and zero at Y.
The Y commutators were already proved.
Negating both canonical closures gives exactly the generator-first S condition, and restriction to M gives F.

## Source and scope limits

All three declared direct inputs apply at their exact stated scopes.
The only coefficient estimate used from C_F0139 is its finite-kernel theorem, whose real/coassociative reference and actual adjoint mechanism remain in that accepted input.
The current proof supplies its own inverse identification and target-core limit; it does not apply C_F0139's measurable theorem to a coefficient that may fail coarse L2.
C_F0070 contributes only the universal Hilbert-Schmidt tensor interface.
The normal-coordinate results elsewhere in that Claim do not enter this nonnormal theorem.
The Dab10 source-unit limits remain as recorded there; no new whole-paper source audit is claimed.

Generation and coarse nonvanishing are explicit hypotheses.
The conclusion concerns polynomial expressions linear in the distinguished reference coordinate, with coefficients depending only on h.
It does not imply F-to-A, unrestricted nonnormal equivalence, a bounded-H dual, or a theorem for nonlinear S-dependent inverse Jacobians.
The statement's comment that a nonzero polynomial is nonzero product-almost-everywhere for diffuse mu is consistent with the finite-zero argument for one-variable polynomial slices, but the proof retains assumption (2) explicitly and does not depend on that comment.

## Conclusion

The complete statement and argument of C_F0141 v1 pass this separately organized independent review.
No mathematical gap, missing direct input, domain mismatch or unresolved source-interface issue was found.
This finding supports proved / independently reviewed when adopted by the responsible Claim decision.

The supported result is A-to-S-to-F for the explicitly specified polynomial linear coordinate class, with both originally supplied canonical contractions and their actual adjoints defined on all M, the exact 4/5 Y bounds and uniqueness at the prescribed values.
Neither coarse L2 membership of 1/F nor injectivity of its distinct Hilbert-space multiplier is assumed or concluded.

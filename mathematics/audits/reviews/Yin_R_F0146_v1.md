---
author: Yin
---
# Independent review of kernel tensor coefficients and the Sylvester-coordinate example

Review performed and recorded: 2026-10-14T17:58.
Human record author: Yin.
This is a separately assigned AI mathematical review, not a personal human inspection.

## Arrangement and scope

The reviewer did not develop or edit [C_F0139 v1](../../claims/Yin_C_F0139_v1.md).
Root assigned the fixed candidate and disclosed that both root and the branch author participated in its mathematical development.
No D material or proof-development discussion was read.
The reviewer read the complete candidate selected by its initial decision dated 2026-10-14T17:51 and its three direct dependency interfaces.
After the initial read, root separately pointed out the delta-gamma/delta-beta notation error in (31); that report is disclosed and handled separately below.
It supplied no proof validation.

The reviewer had independently reviewed C_F0134 and C_F0136 earlier.
Their unchanged fixed results are reused at their selected scopes.
The finite tensor energy identity, its full error term, the two-measure extension and the complete new example were independently checked here.
This review covers the entire statement and Sections 1-3, including actual adjoints, both M domains, all coordinate commutators and vacua, and the exact noninvariance quantifier.

Dab10-U002 supplies the reference real/coassociative difference quotients and actual core adjoints at the stated selfadjoint finite-Fisher premises.
C_F0136 supplies only its analytic-unitary first-derivative passage, with the new error term checked here.
C_F0134 supplies the all-witness failure for the one-sided comparison example.
Their original source-inspection limits remain unchanged.
No new original-source PDF or recursive foundational proof audit is claimed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0139 statement](../../claims/Yin_C_F0139_v1.md#statement) | Complete finite coefficient estimate/core adjoint, measurable abelian simultaneous-measure extension and both actual M domains, and all claims in the Sylvester-coordinate corollary. |
| [Conclusion](#conclusion) | [C_F0139 argument](../../claims/Yin_C_F0139_v1.md#argument) | Sections 1-3, including the complete nonunitary Q term, analytic-unitary limit, both spectral-measure limits, actual adjoint/graph restoration, explicit corrected h coordinate and all-witness comparison. |
| [Conclusion](#conclusion) | [Dab10-U002](../literature/Dab10/Yin_U002.md#dab10-u002) | Represented real selfadjoint difference quotient, actual core adjoint and specified reference closures; standard selfadjoint finite-Fisher algebraic freeness and semicircular reference normalization at the retained scope. |
| [Conclusion](#conclusion) | [C_F0136 analytic-unitary passage](../../claims/Yin_C_F0136_v1.md#3-analytic-unitaries-and-the-operator-norm-estimate) | First-derivative binomial approximants, actual closed-graph limits and unitary/selfadjoint decomposition. The present finite coefficient energy identity and error term are separately checked. |
| [Conclusion](#conclusion) | [C_F0134](../../claims/Yin_C_F0134_v1.md#statement) | Necessity of h inverse in L2 for every A or F witness of the one-sided free tuple (h,hS), applied to the shifted semicircular reference law; S then fails because it implies F. |

## Finite coefficient contractions and vacua

Because every a_alpha,b_alpha belongs to the delta-zero star algebra B, the maps inserting a_alpha on the right of the first tensor leg and b_alpha on the left of the second commute with outer actions.
Thus I_beta delta is a represented outer derivation.
On the core,

\[
T_\beta p=\sum_\alpha E(pb_\alpha)a_\alpha.
\]

The equality with the right contraction follows from delta(b_alpha)=0 and the trace identity tau(v b_alpha)=tau(b_alpha v).
All terms are genuine reference core values.
For a bounded core q, the exact adjoint pairing gives

\[
T_\beta^*q
=\sum_\alpha E^*(qa_\alpha^*)b_\alpha^*
=q\sum_\alpha a_\alpha^*\xi b_\alpha^*
 -\sum_\alpha E(qa_\alpha^*)b_\alpha^*.
\]

This is the claimed actual core-adjoint formula q v_beta-T_(beta#)q.
In particular the actual vacuum is v_beta, since all kernel-coefficient contractions vanish at 1.
Selfadjointness of xi gives v_(beta#)=v_beta*.
No coefficient commutativity, positivity or reality of I_beta delta is used.

## Complete finite energy identity

The norm expansion N in (33) is exact after cyclically moving the bounded factor a_alpha*.
Its core-adjoint test vector E(pb_gamma)a_gamma a_alpha* is again in A, so the second core application is legal.
For arbitrary c in B, not necessarily selfadjoint,

\[
\tau(Ew\,c)=\langle c^*,Ew\rangle
=\langle c^*\xi,w\rangle=\tau(w\xi c).
\]

Here delta(c*)=0.
Coassociativity applied to delta(p b_gamma) consequently gives

\[
E(E(pb_\gamma)c)=\sum_{u\otimes v\text{ in }\delta p}
 u\,\tau(vb_\gamma\xi c).
\]

This proves the N=A-B expansion with the displayed factor order in (33).

For (34), expanding delta(p*p) gives its two terms p* dot delta(p) and delta(p*) dot p.
Reality writes the latter tensor as sums of v* tensor u*p.
After left multiplication by b_alpha* and first-leg contraction, this second term is E(pb_alpha)*p, with the scalar trace conjugated in the correct order.
Therefore B=-C+Q, where Q is exactly the candidate's full nonunitary error.
The scalar C equals the actual inner product <T_beta p,p v_beta*>.
Swapping alpha and gamma after conjugation and cyclically moving only bounded factors gives A=conjugate(C).

Thus (36) follows.
Each Q summand applies a bounded Hilbert slice to delta(p*p) and pairs its H output with a fixed L2 vector made from xi and bounded coefficients.
Hence the Q functional is continuous in the Hilbert tensor norm for fixed finite beta.
This controls the error before taking any unitary limit; it is not silently discarded for arbitrary p.

## Analytic-unitary limit and constants

Use the actual analytic-unitary approximants from C_F0136 for a selfadjoint strict contraction in A.
They converge uniformly, their first derivatives and adjoint derivatives converge in the coarse Hilbert norm, and delta(p_n*p_n) tends to zero.
Therefore every Q term tends to zero by the preceding bounded-slice/L2-pairing estimate.

For each coefficient b_alpha, delta(p_n b_alpha)=delta(p_n) dot b_alpha converges.
The original closed reference E therefore identifies the limit of E(p_n b_alpha) as its actual value E(u b_alpha).
This gives a definite meaning to the finite sum T_beta u and avoids an unproved second-operator domain at u.
The main inner product converges because T_beta p_n converges in H and p_n v_beta* converges in H.
Its limit yields

\[
\|T_\beta u\|_2^2
\le2\|T_\beta u\|_2\|v_\beta\|_2.
\]

The same argument for u*, their average, scaling, and real/imaginary decomposition yields the factor 4 on all core p.
It also handles zero vacuum without dividing by zero.
Applying the same estimate to beta# and using the exact actual adjoint formula gives the factor 5.
The new finite theorem does not require beta to be positive, selfadjoint or a commuting tensor coefficient.

## Two spectral measures and actual adjoint limits

In the measurable part, B=C[h] is abelian.
The strongly commuting left and right h actions have the stated joint vector measure at xi.
For a separated coefficient, their multiplier is sum a_alpha* xi b_alpha*, so (38) exactly identifies the vacuum norm.
The coarse tensor norm is the independent product-measure norm.
These are two distinct norms and both are included in (S3).

Tracial conjugation J exchanges L_h and R_h and fixes xi because xi is selfadjoint.
Thus the joint vector measure is invariant under the flip; the product measure is also flip invariant.
It follows that beta#(s,t)=conjugate(beta(t,s)) has the same two integrability properties, and its actual vacuum is v*.

The sum of the two measures is finite and supported on a compact real spectral square.
Complex polynomials in the two real coordinates are dense in its L2 space, so a single sequence beta_n in C[h] tensor C[h] converges in both norms.
This proves coarse convergence and convergence of the genuine spectral-domain vacuum vectors simultaneously.
The definition of delta_beta p is independent of a finite tensor presentation of delta p, because (u,w) mapped to u dot beta dot w is bilinear and therefore defines a map on the algebraic tensor product.
For each fixed core p, its finitely many bounded outer coefficients send the coarse convergence to Hilbert tensor convergence.
This establishes the represented derivation and its contraction on the original core.

The flip symmetry supplies the corresponding convergence for beta_n# and the adjoint contraction.
Passing the actual core-adjoint pairings to the limit gives

\[
T_\beta^*q=qv-T_{\beta^\#}q
\]

for every q in A and its constant-5 estimate.
Density of A makes the core contraction closable.
Its constant-4 bound and the adjoint constant-5 bound then independently restore M through uniformly bounded Kaplansky approximants and the weakly closed graphs of K and T_beta*=K*.
Weak lower semicontinuity and arbitrarily small norm tolerance give precisely (S4).
No complete product-domain identity or automatic preservation of an adjoint domain by an arbitrary measurable multiplier is assumed.

The same vacuum pairing limit gives delta_beta*(1 tensor 1)=v on the full dense core, so the multiplier value in (S3) has its asserted actual adjoint meaning.
No inverse identification of arbitrary supplied target derivations is part of this theorem.

## The Sylvester example and its integrability

For free variance-one semicircular S_0,S, the shifted h=2+S_0 is positive regular and has law density (1/(2 pi)) sqrt(t(4-t)) on (0,4).
Its scalar conjugate is S_0 and the joint conjugates of (h,S) are (S_0,S).
There is no atom at zero, but the squared inverse integral has near-zero order t^-3/2 and diverges.

For fixed 0<r<1, beta(s,t)=1/(s+i r t) is well-defined outside the product-null origin.
Its squared integral near that origin is bounded by a fixed-r constant times the integral of sqrt(st)/(s squared+t squared).
In first-quadrant polar coordinates the radial singularity cancels the Jacobian: the resulting radial density is bounded and the angular factor sqrt(cos(theta) sin(theta)) is integrable.
Away from the origin the denominator has a positive lower bound on each compact set.
Thus beta is in L2(mu tensor mu); no uniform bound as r decreases to zero is asserted.

Freeness gives the polarized identity

\[
\langle a(h)S b(h),c(h)S d(h)\rangle
=\tau(a^*c)\tau(b^*d).
\]

Hence the vector measure at xi_S=S is exactly mu tensor mu, first on rectangles and then on the generated Borel sigma algebra.
The simultaneous condition (S3) therefore holds for this beta.

The resulting derivation satisfies delta_beta h=0 and delta_beta Y=(s+i r t)beta=1 tensor 1.
The closed contraction K has both M domains, zero h-commutator and Y-commutator P.
The core is invariant under the reference polynomials h,Y, and the bounded rank-one commutator extends to M by its actual closed graph.
Its vacuum is K*1=v.

The generation formula Y-i rY*=(1-r squared)hS is correct.
Since r is strictly between zero and one, this recovers hS inside A_X.
Bounded spectral inverses of h then recover S strongly, proving generation and density of A_X.

## Both coordinates, actual h-vacuum and nonnormality

The reference h-contraction obeys [B_h,Y]=PS+i rSP.
For the correction in (43),

\[
[K\rho(S),Y]=P\rho(S)=PS,\qquad
[\rho(S)K,Y]=\rho(S)P=SP.
\]

The first equality uses the trace pairing; the second uses rho(S)1=S.
Both correction terms commute with h.
Therefore E_h has h-commutator P and Y-commutator zero, while E_Y=K has the complementary values.
All tested inputs lie in M.
Actual adjoints on M exist: the two correction adjoint values are rho(S)K*q and K*(qS), and qS is bounded.
Negation gives a genuine S system with both actual bounded-vector domains.

The independent derivation construction has delta_h=partial_h-I_C delta_beta for C=1 tensor S+i r S tensor 1.
The inner coefficient action is bounded and outer-compatible.
Its value on Y is the cancellation of C against I_C(1 tensor 1), while its h-value remains 1 tensor 1.
Thus both represented starred coordinate derivations are defined before restriction to A_X.

For the h right contraction, the first inner coefficient gives K(pS)-pK(S), while the second gives i r(Kp)S.
Consequently Q_hp=E_hp+pK(S), with the stated sign.
Taking actual adjoints at 1 gives

\[
E_h^*1=\xi_h-vS+i rK^*S,
\qquad
Q_h^*1=\xi_h-vS+i rK^*S+(K(S))^*.
\]

The sign changes on i r when the scalar coefficient is adjointed.
Every term is in H: S belongs to Dom K*, K(S) belongs to H, and S is bounded.
The last right-multiplication term has actual adjoint q mapped to q(K(S))* on M.
Hence this is a genuine vacuum vector for the h derivative; the Y vacuum is v.
This proves A independently of any nonnormal strong-to-ACSY theorem.
F follows directly from S.

With Z=hS, the identity [Y,Y*]=(1-r squared)[Z,Z*] holds by direct expansion.
The highest-degree words in hS squared h-S h squared S are S_0 S squared S_0 and S S_0 squared S, with opposite nonzero coefficients and no other terms of the same words.
Algebraic freeness of the standard semicircular pair makes that polynomial nonzero.
Thus Y is nonnormal for this exact r range.

## Quantifiers in the comparison and the local notation correction

The comparison tuple (h,hS) has exactly the free reference hypotheses of C_F0134 and inverse h not in L2.
That accepted theorem excludes every A and every F witness; S is excluded because it implies F.
In the present tuple all three conditions have actual witnesses.
The map phi_r(z)=z+i r z* is invertible as a real-linear map, with inverse (w-i r w*)/(1-r squared).
The exact example is phi_r sending the negative tuple's second coordinate to the positive tuple's second coordinate, while its inverse sends the positive example to the negative one.
This disproves invariance under invertible real-linear coordinate changes.
It is not an A-versus-F separation, and it does not claim that this same forward phi_r sends the exhibited positive tuple to a negative tuple.

One local notation correction is required in (31): the first displayed map is labeled delta_gamma, but the defined coefficient and every following use are beta, so the label should be delta_beta.
Root reported this after the initial fixed-text read; the reviewer confirms it is a pure subscript mismatch.
It does not alter the map I_beta delta, any hypothesis, equation or conclusion.
The correction can be made in place as meaning-preserving notation maintenance.
Checking that the actual edit changes only this label suffices; it does not require a new mathematical version or a new whole-proof review.

## Conclusion

The complete mathematical statement and all three proof sections of C_F0139 v1 pass this independently organized review.
No mathematical gap or unresolved source-interface issue was found.
The single notation correction identified above should be made before presentation/adoption; it leaves this finding's mathematical scope unchanged.
The finding supports proved / independently reviewed for this fixed mathematics when adopted by its responsible decision.

The supported results are the finite kernel-tensor estimate with its actual core adjoint, the stated simultaneous-measure sufficient condition and both actual M domains, and the complete nonnormal Sylvester-coordinate example.
The latter establishes failure of invariance of A, S and F under an invertible real-linear coordinate change, with all three conditions true together on the new tuple and false together on the old one.
No universal A-to-F theorem or counterexample is claimed.

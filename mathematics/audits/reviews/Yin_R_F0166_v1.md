---
author: Yin
---
# Independent whole-proof review of sharp rotational quadratic estimates

Review performed and recorded: 2026-10-16T03:15.
Human record author: Yin.
This is a separately assigned AI mathematical review, not a personal human inspection.

## Arrangement and exact scope

The reviewer did not develop or edit [C_F0159 v1](../../claims/Yin_C_F0159_v1.md#statement).
The coordinating agent supplied that fixed candidate and an obligation list emphasizing radial atoms, the negative angular blocks, the zero endpoint, actual adjoints, sharpness and the necessity of excluding an origin atom.
No proof-generation dialogue, separate author explanation or exploration notes were supplied or consulted.
The working origin D_F0017 and the motivating D_F0002 were not consulted.
The review started from the exact statement, then reconstructed the four argument sections and checked the three direct dependency interfaces.
After forming the initial mathematical findings, the reviewer read the existing [R_F0025](Yin_R_F0025_v1.md) and the arrangement, bindings and diffuse-law discussion of [R_F0049](Yin_R_F0049_v1.md#conclusion) to check the inherited review boundaries.
Neither earlier review supplies evidence for the new quadratic calculation.

The inspected artifact is the 2026-10-16 fixed physical v1 selected by [Decision initial](../../claims/Yin_C_F0159_v1.md#decision-initial), dated 2026-10-16T03:07.
The starting assessment is proof draft, unreviewed.
This review covers the entire statement, all four proof sections, the exact direct input interfaces and both examples.
It covers every compactly supported rotation-invariant probability under the stated actual-A condition, including mixed and atomic radius laws with positive radii and support accumulating at zero.
It does not establish Task completion or a conclusion for arbitrary nonradial laws or correlated tuples.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0159 statement](../../claims/Yin_C_F0159_v1.md#statement) | Entire exact statement: actual-A equivalence with the separate zero-atom exclusion and q in L2, unique divided difference and actual vacuum, both one-sided adjoint domains and their equality, the real nonnegative paired estimate, and individually optimal constants. |
| [Conclusion](#conclusion) | [C_F0159 argument](../../claims/Yin_C_F0159_v1.md#argument) | All four sections, including angular disintegration, represented-core well-definedness and uniqueness, actual adjoint pairings, atomic angular blocks, complete negative-block diagonal accounting, positive remainder, cutoff removal at zero, Parseval, sharpness and both examples. |
| [Conclusion](#conclusion) | [C_F0076 statement](../../claims/Yin_C_F0076_v1.md#statement) | Part 1 only: the identical full actual outer-derivation and vacuum-adjoint premise for a bounded normal generator implies that its spectral law is diffuse; applied to exclude an atom at the origin. The already accepted theorem is an input, with no new review of its second-derivative or coassociativity assertions. |
| [Conclusion](#conclusion) | [C_F0047 radial theorem](../../claims/Yin_C_F0047_v1.md#yin_c_f0047) | Sections 2-6: same-radius and unequal-radius Fourier formulas, the actual midpoint vacuum criterion, quantile midpoint comparison and Hardy estimate, and the actual bounded-function graph domains. Section 7: the stated countable-circle parameters, vacuum summation and unbounded-Hilbert-contraction example. These actual interfaces and the local scalar calculations used here were checked. |
| [Conclusion](#conclusion) | [C_F0055 actual adjoints](../../claims/Yin_C_F0055_v1.md#7-actual-adjoints-and-original-graph-restoration) | Actual scalar core identity E0* a = a xi - J E0 J a, under the nonatomic compactly supported represented-core and actual-vacuum assumptions. The conjugate-product pairing was independently recomputed. No nonradial norm bound or free-product lifting is used. |

## Actual model, origin and vacuum

The actual-A premise of C_F0159 is exactly the one-generator specialization of C_F0076 Part 1: the represented unital starred algebra is dense in the tracial Hilbert space, the generator is bounded and normal, the derivation is complex-linear and outer, its generator value is the vacuum tensor, and that tensor belongs to the actual Hilbert adjoint domain.
The [selected reviewed C_F0076 decision](../../claims/Yin_C_F0076_v1.md#decision-reviewed) therefore supplies nonatomicity without an additional geometric or second-derivative assumption.
An atom of the radius distribution at zero is precisely the point atom of the planar law at zero, so its exclusion is necessary.
The convention q(0)=0 does not bypass this argument.
C_F0076 is reused as an accepted theorem at this interface; its ACSY24 and MSY23 source proofs were not newly audited.

Rotation averaging and Fubini give the displayed angular disintegration for every bounded Borel test function.
Once the origin atom is excluded, each positive-radius conditional angular measure is nonatomic, and hence the resulting planar probability is nonatomic even when the radius distribution is purely atomic.
The coordinate generates the represented abelian von Neumann algebra, its integral trace is faithful and normal, and Stone--Weierstrass density on the compact support gives density of the represented starred polynomial core in L2.

A polynomial in z and conjugate(z) is Lipschitz on a compact rectangle containing the support, so its divided difference is bounded off the null collision diagonal.
Changing its representative on a null set affects only a product-null set.
The pointwise quotient obeys the outer Leibniz rule and sends z to 1 tensor 1.
For any other outer derivation with this generator value, differentiating z conjugate(z) = conjugate(z) z gives
\[
 (z-w)\delta(X^*)(z,w)=\bar z-\bar w.
\]
Multiplication by z-w is injective in L2 of the product probability because its zero set is null.
Thus the starred-generator value is uniquely forced, and the Leibniz rule determines the derivation on the entire represented core.
This verifies that the vacuum test concerns every actual-A witness, rather than only the constructed quotient.

The C_F0047 midpoint is m = F_- + p/2, where p is the radius-atom mass, so its exact vacuum function is q = 2m/r.
Only input angular frequency 1 has a nonzero integrated quotient.
The first angular-block term and the integrated strict outer-radius term give respectively F_+/r and F_-/r, hence
\[
 \tau(E_0 f)=\int q(r)f_1(r)\,d\nu(r).
\]
For polynomial tests this identity needs no prior q integrability because f_1(r)/r is bounded.
Conversely, the Fourier tests r^{|n|} exp(in theta) Q(r squared) identify finite complex measures: all unwanted angular modes of a proposed L2 vacuum vanish, and the mode-1 relation is r conjugate(xi_1) = F_- + F_+.
Polynomial density and r>0 almost everywhere give xi_1=q and q in L2.
The comparison with C_F0047 Sections 2 and 4 therefore verifies both directions of the actual-vacuum criterion, with exactly the radius-atom contribution p/r.
The identity for f=z is
\[
 \int r q(r)\,d\nu(r)
 =2\int F_-\,d\nu+\sum_r p(r)^2=1,
\]
which independently checks the normalization.

For q in L2, this vacuum identity is precisely the Hilbert adjoint pairing against 1 tensor 1.
Expanding the quotient of conjugate(a)f and using symmetry under interchange of the two variables gives
\[
 \langle a,E_0f\rangle
 =\langle a\xi-JE_0Ja,f\rangle.
\]
All products and polynomial quotient kernels in this calculation are bounded except for the displayed L2 vacuum factor, which is multiplied by a bounded polynomial.
Thus the representing vector is in L2 and the identity proves the actual adjoint domain assertion, with the correct convention that inner products are linear in the second variable.
Pairing directly against a tensor 1 and 1 tensor a proves that both one-sided delta-adjoints equal this same vector.
No extension is substituted for either actual adjoint.
The C_F0055 Section 7 interface agrees exactly with this computation.
The bounded-function graph statement in C_F0047 Section 6 also has the required actual-operator meaning: its infinity-to-L2 bound and this adjoint formula bound both graph coordinates of uniformly bounded polynomial approximants.
Weak closedness of the original closure graph and the actual adjoint graph then puts each bounded limit into those domains.
This supplies the candidate's contextual domain claim without importing a full-Hilbert-space bound or a quadratic estimate.

## Fourier blocks and nonnegative modes

Applying a xi - J E0 J a to a single angular mode and using the C_F0047 formula with the conjugate input index gives the stated B_n for n>=0 and B_{-k} for k>=1.
The conjugation reverses the input frequency, and the final frequency is n+1.
In particular the atom occurs in F_+ for n>=0 and is absent from the negative-block multiplier F_-.
These formulas agree with direct Laurent factorization on one circle and geometric expansion at two unequal radii.
The geometric expansion is used for the already bounded polynomial quotient before any separation of singular summands.

For n>=0, the strict inner-radius kernel has factor (s/r)^n in [0,1].
The positive measure defining B_0 has total mass (F_+ + F_-)/r = q.
The stated pointwise Cauchy--Schwarz argument consequently yields |B_n f| squared at most q B_0(|f| squared).
For bounded f this is integrable because B_0(|f| squared) is at most norm(f)_infinity squared times q.
Both the sign and the n=0 endpoint are correct.

## Negative blocks, including every radius atom

Write B_{-k}=D-H with multiplier d=F_-/r and kernel
\[
 H(t,r)=t^{k-1}r^{-k}{\bf1}_{t<r}.
\]
For bounded f supported in [epsilon,R], every term in the expansion is absolutely integrable.
The factor r^{-k} is then bounded on the input support, the output power t^{k-1} is bounded, and Df is supported away from zero.
This justifies the square expansion for arbitrary atomic, singular and mixed radius laws.

At distinct source radii r>s, the cross term and H*H term have combined coefficient
\[
 (rs)^{-k}\left[\int_{t<s}t^{2k-2}\,d\nu(t)
                     -F_-(s)s^{2k-2}\right]
 =-(rs)^{-k}J_k(s).
\]
On the radius diagonal, integration against the product measure has mass p(r) relative to integration against nu in the remaining coordinate.
The multiplier D*D contributes d(r) squared, while H*H contributes
\[
 p(r)r^{-2k}\int_{t<r}t^{2k-2}\,d\nu(t).
\]
The candidate's proposed multiplication term minus the diagonal part of its subtracted kernel is
\[
 \frac{F_-F_+}{r^2}-p(r)r^{-2k}J_k(r)
 =d(r)^2+p(r)r^{-2k}\int_{t<r}t^{2k-2}\,d\nu(t).
\]
Thus equation (11) has exactly the right diagonal coefficient.
A diffuse-radius computation alone would not verify this point; the p(r) term is necessary and is present.

For k>=2, Tonelli gives
\[
 J_k(u)=\int_0^u(2k-2)v^{2k-3}F_-(v)\,dv.
\]
Hence J_k is absolutely continuous, nondecreasing, bounded on [0,R], and zero at zero.
For k=1 it vanishes identically.
In particular its Stieltjes measure has no atom, so the strict inequalities in
\[
 J_k(\min(r,s))=\int_0^R{\bf1}_{u<r}{\bf1}_{u<s}\,dJ_k(u)
\]
introduce no endpoint correction.
The double integral subtracted in equation (11) is therefore the nonnegative integral of
\[
 \left|\int_{r>u}r^{-k}f(r)\,d\nu(r)\right|^2
\]
against dJ_k(u).
The input cutoff makes this application of Fubini absolute.
This proves the claimed upper bound, and for k=1 it gives the exact identity with multiplier \(F_-F_+/r^2\).

## Removing the cutoff at zero

The multiplication part converges in L2 by d<=q and dominated convergence.
For the integral part, (r/s)^{k-1}<=1 on s>r gives the uniform majorant
\[
 \|f\|_\infty W(r),\qquad W(r)=\int_{s>r}s^{-1}\,d\nu(s).
\]
For each fixed r>0 these integrals converge, and they are finite because s^{-1}<=r^{-1} on the integration set.
It remains essential to have W in L2; absence of an origin atom alone would not establish that.

Let b be the nondecreasing quantile used in C_F0047 and U(t)=t/b(t).
Its midpoint comparison and q=2m/r give
\[
 \|U\|_2\le\frac1{\sqrt3}\|q\|_2.
\]
For almost every t, b(t)=r implies t<=F_+(r), and hence
\[
 W(b(t))=\int_{F_+(b(t))}^1b(s)^{-1}\,ds
 \le\int_t^1b(s)^{-1}\,ds.
\]
This verifies the required domination even on a positive-length atomic quantile plateau.
The integration-by-parts proof in C_F0047 discards the nonpositive lower boundary term before taking its cutoff to zero, and gives the L2 bound 2 norm(U)_2 for the last tail.
Consequently
\[
 \|W\|_{L^2(\nu)}\le\frac2{\sqrt3}\|q\|_{L^2(\nu)}<\infty.
\]
Dominated convergence now proves the actual L2 convergence of each negative block.
The right side also converges because \(F_-F_+/r^2\le q^2\).
No vanished boundary value, diffuse radius law, bounded inverse of a radius, or full-Hilbert-space operator bound is used.
This removes the temporary cutoff for every bounded radial coefficient in the statement's polynomial expansion.

Finally \(F_-F_+/r^2\le qF_+/r\), and \(B_0(|f|^2)\) contains the nonnegative multiplication term \(F_+|f|^2/r\).
This establishes the same integrated bound for every negative mode as for the nonnegative modes.

## Assembly, sharpness and the examples

A starred polynomial has finitely many angular coefficients, and the outputs n+1 are distinct.
Parseval therefore sums the individual estimates without cross terms.
The zero angular coefficient of |a| squared is the sum of the squared absolute values of those coefficients.
The frequency-1 coefficient of T(|a| squared) is consequently B_0 of that nonnegative radial function.
With the stipulated inner-product convention, its pairing in the order shown in the statement is still the same real integral, because this coefficient and q are real and nonnegative.
This proves the first inequality in S3; Hilbert-space Cauchy--Schwarz proves the second.
Commutativity supplies a*a=aa*=|a| squared, while symmetry already established T_left=T_right.
Thus both requested estimates follow with the stated common value.

At a=1, T1=xi and T(|1| squared)=xi.
The equality pairing against X is 1, so xi cannot vanish.
Each admissible constant must therefore be at least norm(xi)_2.
This proves individual optimality, not merely optimality within the displayed proof method.

On one positive-radius Haar circle, the formulas reduce to r^{-1} exp(i theta) followed by projection onto nonnegative angular frequencies.
The paired estimate is then the elementary L2 contraction of that projection, and the optimal constant is 1/r.
For the countable-circle family, the identities F_-(r_j)=s^j and q(r_j)=2(1+s)(2s)^{j-1} give
\[
 \|\xi\|_2^2=\frac{4(1-s)(1+s)^2}{1-4s^3}.
\]
This is finite for beta>2/3.
For beta<1 the disk mass divided by radius is (2s)^j and diverges.
A bounded Hilbert extension of E0 would extend its polynomial commutator identity by density and contradict the compression estimate s^j<=2r_j norm(E0).
Thus the example's Hilbert unboundedness is consistent with the proved quadratic estimate and the actual bounded-function domain result.

## Source and verification boundaries

The direct inputs are the precise previously accepted C_F0076, C_F0047 and C_F0055 interfaces listed above.
The source midpoint/Hardy calculation, actual adjoint pairing and countable-circle arithmetic were inspected and recomputed locally.
The existing R_F0025 discloses its reviewer's preliminary contribution to C_F0047; this historical disclosure is preserved and is not relabelled as a new blind review.
The present separate review independently checks the C_F0159-specific use and the new quadratic calculation.
C_F0076's accepted diffuse-law theorem is reused with a verified hypothesis match; no new audit of its external ACSY24/MSY23 proofs is claimed.
Mai15 is motivation only: no real coassociative energy identity is used here, and no Mai15 theorem or source-priority claim is being newly verified.

The new kernel positivity is proved by its displayed Stieltjes integral, so no unverified external positivity theorem is required.
The standard scalar angular factorization, Fubini, polynomial density, dominated convergence and Parseval uses have their actual hypotheses supplied above.
No new recognized specialized source dependency or unresolved source attribution affecting this argument was identified.
This is a mathematical proof and interface review; it is not formal verification or a global literature-priority search.
No computational experiment is needed for the general positive-kernel identity.

## Conclusion

PASS: the complete fixed statement and argument of C_F0159 v1 are mathematically acceptable at the exact scopes in the review bindings.
No corrective mathematical change is required.
In particular the negative angular blocks include the full radius-atom diagonal mass, their subtracted kernel is positive, the zero-endpoint limit is justified by the precise atomic quantile Hardy bound, and the actual-A equivalence includes the separate necessary origin-atom exclusion.
The sharp paired constants are both norm(xi)_2 for every law satisfying S1, including the displayed Hilbert-unbounded examples.

This independently reviewed finding can support acceptance of C_F0159 v1 as proved, with its existing dependency scopes preserved.
The Claim's adopting decision belongs to its responsible agent; this review supplies the finding above without adopting it.
It does not resolve the unrestricted normal-tuple A-to-S problem or close T_F0011.

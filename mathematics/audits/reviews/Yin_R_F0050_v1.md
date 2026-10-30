---
author: Yin
---
# Independent review of weighted partial liberation with uniform kernel row bounds

Review performed and recorded: 2026-10-14T18:32.
Human record author: Yin.
This is a separately organized AI mathematical review, not a personal human inspection.

## Arrangement and scope

The reviewer did not develop or edit [C_F0077 v1](../../claims/Yin_C_F0077_v1.md).
Root assigned the fixed candidate and disclosed that the normal-branch author developed the spectral graph argument, weighted energy identity and iteration, while root supplied the uniform-row variant.
The assignment identified the domain, sign and iteration obligations; no D10, mutable development draft or proof-generation discussion was read.
The complete fixed statement, all argument sections and the initial decision dated 2026-10-14T18:24 were read before the conclusion was formed.
The three declared direct inputs were checked at their exact invoked scopes.

This review covers the marginal actual-adjoint formula and absolute continuity, the precise restriction graph closure, the weighted derivation and actual adjoints, bounded marginal-factor graph extension, the complete finite-kernel defect and energy calculation, the dyadic bounded-tail argument, all limiting estimates and both canonical domains.
It also checks the entire abstract composition obstruction and its nonrealization boundary.
The source attribution was separately checked against the parsed primary Tarcsay text at the stated passages.
Existing C inputs retain their original source-inspection and review limits; no full predecessor or full external-paper re-audit is claimed.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Conclusion](#conclusion) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Conclusion](#conclusion) | [C_F0077 statement](../../claims/Yin_C_F0077_v1.md#statement) | Exact represented liberation and actual-vacuum premises, absolute continuity and marginal restriction graph closure, real symmetric kernel with uniform row L2 bound, original contraction and actual adjoint on all M, quantitative bounds and the limited abstract obstruction. |
| [Conclusion](#conclusion) | [C_F0077 argument](../../claims/Yin_C_F0077_v1.md#argument) | Complete spectral graph proof, finite bounded-factor extension, defect signs and analytic-unitary energy, composition-power estimates and bounded-tail recursion, clamp/conditional-expectation approximation, both graph restorations and all abstract-example calculations. |
| [Conclusion](#conclusion) | [C_F0063 Appendix A](../../claims/Yin_C_F0063_v1.md#appendix-a-automatic-actual-liberation-contractions) | Its final abstract formulation: a represented algebraic real liberation derivation with actual L2 vacuum has the standard actual tensor-adjoint and closability mechanism. No normal-coordinate construction or affiliated criterion is imported. |
| [Conclusion](#conclusion) | [C_F0043](../../claims/Yin_C_F0043_v1.md#statement) | Sections 3.1-3.2 actual real-energy calculation and final-identity analytic-unitary limit; the present weighted defect and its estimates are rederived, without importing the unitary-coordinate theorem. |
| [Conclusion](#conclusion) | [C_F0027](../../claims/Yin_C_F0027_v1.md#statement) | Section 5 generic bounded-core/actual-adjoint estimates and Kaplansky weak closed-graph bridge. No normality, coordinate commutator or rationality conclusion from that Claim is required here. |

## Marginal adjoint, absolute continuity and the exact graph closure

The given represented liberation derivation has algebraic values on A and is real after multiplication by i.
Its actual vacuum is selfadjoint.
The general tensor-adjoint calculation in C_F0063 Appendix A applies to this explicit abstract premise; it does not require constructing liberation from some other coordinate derivative or assuming freeness.

For a marginal elementary tensor a tensor b the actual adjoint formula gives

\[
\beta^*(a\otimes b)=a\zeta b
 -\mathrm i(a-\tau(a))b-\mathrm i a(\tau(b)-b).
\]

The correction simplifies to i times col minus row, as in (S1).
Row and column each have norm at most one from marginal tensor L2 to H.
The spectral map q mapped to S_q zeta is isometric from L2(nu) into its joint cyclic subspace in H.
These facts fix both the sign and the graph norm.

To prove absolute continuity, continuous functions and then marginal star-polynomial tensors approximate an indicator of a mu-squared-null Borel set in L2(mu squared plus nu).
Their coarse vectors tend to zero, while their actual adjoint values tend to S_(1_B) zeta; the bounded correction tends to zero.
The actual adjoint is closed, hence this last vector is zero and nu(B)=0.
This argument proves the needed absolute continuity from the operator hypothesis, rather than assuming it as a property of all left/right spectral measures.

After absolute continuity is known, the inclusion of function classes from the intersection of the two L2 spaces is well-defined.
The displayed adjoint graph norm is equivalent to the sum-measure L2 norm, because the row/column term is bounded and the spectral part is isometric.
Marginal polynomial tensors are dense in this finite-measure space on compact K squared.
Conversely a Cauchy graph sequence is Cauchy in both L2 spaces, and absolute continuity identifies its two almost-everywhere limits.
This proves precisely the graph closure claimed in the statement.

The proof never infers that this closure exhausts every marginal vector in the full domain of beta*.
That stronger core assertion is not supplied by closedness or by the norm equivalence alone, and the candidate explicitly excludes it.
The resulting inclusion in the actual beta* domain is sufficient for every later use.

## The weighted derivation and actual bounded-factor extension

For a real symmetric g, the row and column corrections cancel, giving eta_g=S_g zeta.
The tracial involution flips the joint spectral coordinates at the selfadjoint vector zeta, so this vacuum is selfadjoint.
On algebraic tensors, insertion into a finite expansion of gamma(p) is a well-defined linear operation by bounded outer multiplication of the fixed Hilbert vector g.
No bounded operator on the complete coarse space is needed to define it.

Tracial cyclicity identifies the weighted vacuum pairing with the pairing against g for beta.
Thus the actual marginal adjoint inclusion proves eta_g is the actual vacuum of beta_g.
Real symmetry gives reality under flip-adjoint, and the usual algebraic tensor adjoint formula places A tensor-algebraic A in Dom beta_g*, proving closability.
At p tensor 1 the same calculation yields the actual contraction-adjoint formula E_g,0*p=p eta_g-E_g,0p.
The candidate uses this actual core membership, not a formal product adjoint.

The extension to bounded measurable N factors is legitimate.
A bounded n in N has uniformly bounded marginal polynomial approximants converging strongly, strongly after adjoint, and in L2.
The unweighted liberation derivative converges to i(n tensor 1 minus 1 tensor n).
For beta_q the corresponding formula contains the fixed Hilbert tensor q between the two outer factors; uniformly bounded strong convergence makes those values converge in the Hilbert tensor norm.
Repeated product rules give graph approximations for every fixed finite word in bounded N factors and the original B factors.

The actual vacuum pairings extend along those graph approximations.
The adjoint formula extends as well, since multiplication of the fixed L2 vacuum by uniformly bounded strongly convergent factors converges in L2.
For finite bounded q all derivatives of enlarged-core words are finite tensors over this enlarged core, and their contractions are again bounded enlarged-core elements.
Consequently every polynomial iterate used in the finite-kernel calculation has an actual domain there.
This extension proves the required finite calculations without changing the eventual meaning of the original canonical closure.

## Finite-kernel defect and energy signs

For a finite real symmetric bounded b, direct expansion on a marginal f gives

\[
D_bf(z,w,v)=-(f(z)-f(v))
 [b(z,v)b(z,w)+b(z,v)b(w,v)-b(z,w)b(w,v)].
\]

In the full product rule the two mixed terms of the two iterates cancel in exactly the same triple-tensor positions.
Hence D_b is an outer derivation, and checking the displayed formula on the marginal algebra and zero on B identifies it on the enlarged core.
Tracing the middle coordinate gives the weight b(z,v)(a_b(z)+a_b(v))-ell_b(z,v).

The first inner marginal coefficient produces (E_bp)a_b.
Inserting a_b in the second inner position produces E_b(pa_b)-pE_b(a_b), by the canonical contraction commutator and cyclicity of the scalar trace.
The overall factor i has the sign in (B0b), because multiplying the weighted derivative i(f(z)-f(v)) times i produces the negative marginal difference.
This verifies the full defect-contraction order.

For a unitary u, put t=tau(a_b u* E_bu).
The first scalar term in the braces in (B0b) is t.
Using the actual adjoint E_b*u=u eta_b-E_bu makes the second term tau(eta_b a_b)-conjugate(t).
The third term is tau(E_b(a_b))=tau(eta_b a_b), with a negative sign.
Thus the first three terms reduce to t-conjugate(t), and multiplying by i gives -2 Im(t).
The final negative E_(ell_b) term gives positive Im of its pairing with u.
These are precisely the signs in (B0c).

For polynomial enlarged-core inputs, the actual second iterate satisfies E_b squared p=C_bp+Theta(beta_bp)eta_b.
Applying the actual adjoint to E_bp and expanding beta_b(p*p), using reality, yields (B0d).
Taking real parts gives the stated negative defect pairing; the switch between the two inner-product positions does not change that real part.
The two appearances of the vacuum give 2 Re of the pairing with p eta_b.
All products involving eta_b are a bounded element times an L2 vector, or an L2 scalar pairing.

For the analytic unitary a+i sqrt(1-a squared), the binomial polynomials converge in operator norm and in each first-derivative seminorm for beta_b and D_b.
Both are outer derivations, so the derivative of a power is bounded by its degree times norm(a) to one less power times the derivative of a.
The final polynomial energy identity therefore has a limit.
Its product-derivative term tends to zero, since the limiting product is 1.
This establishes (B0e) without asserting that the analytic unitary is in a second-iterate domain.
The other contraction terms in (B0c) likewise pass along these bounded graph approximations.
Finally Cauchy--Schwarz gives absolute value of t at most norm(b)_2 norm(E_bu)_2.
This proves (B6) with the displayed coefficient 2 and the single successor term.

## Composition estimates and the bounded-tail recursion

For a finite q with the stated row bound, its real symmetry gives the corresponding column bound and makes T_q selfadjoint.
The Hilbert-Schmidt estimate gives norm(T_q) at most H_g.
The kernel of the k-th power is a row of q, T_q to the power k-2, and a column of q.
Cauchy--Schwarz gives the uniform bound m squared times r to the power k-2 for k at least 2.
The Hilbert-Schmidt product estimate gives norm(q to composition-power k)_2 at most H_g r to the power k-1.
Both conclusions remain valid for arbitrary signed real symmetric q.

All these powers are finite real symmetric bounded marginal kernels.
Their row/column correction in (S1) vanishes, so their actual vacua have norm at most norm(zeta)_2 m squared r to the power k-2.
Substitution into (B6), with k=2 to the power n and normalization by r to the power 2k, gives exactly (B7), including the factors r squared and r in A.

Boundedness of the normalized tail is established independently of the desired uniform contraction estimate.
For the fixed algebraic a, its finite liberation expansion bounds the inserted derivative by a constant times the Hilbert norm of any marginal b.
The differentiated binomial series gives a finite c_u with norm(E_bu)_2 at most c_u norm(b)_2, independent of b and of the iteration index.
Combining this with the Hilbert-Schmidt power bound makes w_n bounded.
This argument requires neither a bounded full-coarse insertion nor a uniform bound over all analytic unitaries.

If one w_n were larger than A+1, the recursion would force every subsequent term to increase strictly and stay above that value.
Boundedness would then give a finite limit L greater than A+1, whereas the recursion would imply L squared at most (A+1)L.
This contradiction proves the bound at every tail index.
In particular v_1 is at most r squared times (A+1), exactly C in (B2).
The n=0 quadratic inequality gives (B8).
The choice r=max(1,H_g) removes all zero-radius or small-radius division issues.
Constants remain valid, albeit nonsharp, even for the zero kernel.

## Approximation and both original domains

Clamping a real symmetric g to a bounded interval preserves symmetry, does not increase either row bound or Hilbert norm, and converges in both L2 measures by dominated convergence.
The established adjoint graph formula consequently gives convergence of the actual vacua.

For each clamp, conditional expectation onto the same finite partition in both variables preserves real symmetry and the pointwise clamp bound.
Conditional Jensen first in the second variable and then in the first bounds each row square integral by the conditional average of the original row square integrals, hence by m squared.
The coarse Hilbert norm does not increase.
Increasing partitions converge in coarse L2; an almost-everywhere subsequence converges for nu as well by absolute continuity.
The common clamp bound then gives weighted L2 convergence.
Thus the finite measurable kernels converge in the actual marginal adjoint graph with the uniform estimates required by the energy step.

For each fixed analytic unitary the c_u estimate passes the contraction values in coarse norm, while weighted convergence passes their actual vacuum norms.
Passing first through the finite-partition approximation and then through the clamps proves the K_g unitary bound.
This is pointwise convergence on each such input, not convergence in the operator-norm-to-L2 norm of the contractions.
Applying the same calculation to the adjoint unitary, averaging, rescaling, and taking real and imaginary parts gives the 2K_g estimate in (B3).
The actual core adjoint identity gives its separate norm(eta_g)+2K_g estimate.

The weakly dense star algebra A admits uniformly bounded Kaplansky core approximants to every bounded element.
Weak compactness of their bounded images and weak closedness of the two graphs put that element in the actual closure of E_g,0 and in its actual Hilbert adjoint.
This step works with nets and needs neither a finite generating list for B nor separability of M.
It is the generic part of C_F0027 Section 5, not its normal-coordinate theorem or rationality application.
The general g is never asserted to have an actual second derivative or algebraic tensor values.

## Abstract obstruction and source boundary

For the three-block example, the occupied-set total measure is 3/7, the coarse kernel norm squared is 4 times the sum of 2 to the power -2n, and the chosen symmetric weight has total mass 1.
It is supported where g is zero, so the weighted norm of g is zero.
On each normalized block-constant subspace T_g is 2 to the power -n times the three-vertex path adjacency matrix, and on the orthogonal within-block directions it is zero.
Its norm is therefore exactly 1/sqrt(2).

The two-step kernel on the A_n by C_n rectangles and their transposes is 2 to the power n.
Its squared weighted integral is the divergent sum of 2 to the power n.
The row L2 norm on an A_n row is 2 to the power n/2, so uniform row control genuinely fails.
Nonzero scalar rescaling does not remove the weighted divergence.
These calculations verify the claimed abstract failure of composition-domain propagation.

The candidate expressly does not realize this weight as the joint vector measure of a liberation vacuum for a tracial law.
The example therefore refutes only the implication from the stated abstract measure/kernel conditions; it supplies no counterexample to the normal Task or to a result using additional liberation constraints.

For source attribution, the parsed primary [Tar16, arXiv v2](../../literature/pdf/Tar16--arxiv-v2.pdf) was read on printed page 1, Section 1, and the Section 2 passage around (2.3) on printed page 3.
These passages identify the closable inclusion mechanism for absolutely continuous measures/forms.
The candidate's continuous-polynomial-core proof and exact graph-domain conclusion were independently checked above and do not rely on a theorem quoted without proof from that paper.
This is an attribution/interface check, not a whole-paper proof audit or a claim of priority.
The reported absence of the original liberation article from the author's bounded search is not treated as a mathematical premise or as an exhaustive literature search.

## Conclusion

The complete statement and argument of C_F0077 v1 pass this independently organized review.
No mathematical gap, missing direct input, sign error, domain overstatement or unresolved source-interface issue was found.
This finding supports proved / independently reviewed when adopted by the responsible Claim decision.

The accepted scope is the specified real symmetric kernel with uniform row L2 control and its actual weighted vacuum, the exact marginal polynomial-restriction graph closure, and both original canonical contraction domains.
It does not identify the entire marginal restriction of beta*, omit the row bound, realize the abstract obstruction as a liberation law, or settle the unrestricted normal comparison.

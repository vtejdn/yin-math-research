---
author: Yin
---

# Isolated review of four affine determinant and spectral modules

New review act: 2026-10-23T00:16 UTC.
Human record author: Yin.
The reviewer is a separate agent outside substantive development of the four target proofs.
It received the fixed complete mathematics, necessary fixed interfaces, rules and assigned scope without the development dialogue or a mathematical summary of those proofs.
It read all current mathematics of C_F0120, C_F0121, C_F0122 and C_F0123, including their later refinements in physical v1, and formed initial findings before opening their old R records or assessment histories.
The initial conclusion was that all four proofs pass at their precise hypotheses without a required substantive correction.
Only afterwards did it read the complete R_F0070, R_F0122, R_F0072 and R_F0073 accounts and compare their checks, dates, relationships and limits.

The C_F0119 necessary input included its author's existing proof and verification declarations.
These fixed input declarations were visible, but no target's old checking conclusion was supplied before the initial findings.
C_F0121's selected-assessment navigation link was visible and was not opened at that stage.
C_F0123's acceptance of Brown foundations and elliptic examples was part of its explicit source boundary.
The actual binding is to canonical C paths and original anchors below, not disposable reading views.

C_F0111 was also mathematically read in this assignment, but its reading view inadvertently included its old target conclusion of proved after complete independent review before initial findings.
No new independent finding for C_F0111 is asserted here.
Its adequate [original C_F0111 account](Yin_R_F0121_v1.md#5-scope-correction-and-final-boundary) is retained at its disclosed unknown relationship; no duplicate self-review is created here.

## Fixed inputs and source depth

The reviewer checked [C_F0119](../../claims/Yin_C_F0119_v1.md#yin_c_f0119), specifically the full covariance, moment/Dyson interface, strict weighted row/column uniqueness contraction, bilinear trace symmetry, logarithmic primitive with constant fixed at imaginary infinity, scalar potential and smaller selfadjoint specialization.
These arguments precede the target conclusions and contain no circular use of their minimization or derivative results.
The normalized determinant convention and bounded invertible multiplicativity are accepted at [MS24-U001](../literature/MS24/Yin_U001.md#determinant-convention).
The centered determinant/capacity identity, including zero capacity and without attainment assumptions, is accepted at [MS24-U003](../literature/MS24/Yin_U003.md#ms24-u003).
Their full original foundations were not re-audited.

The reviewer directly extracted and read the retained local MS17 PDF pp. 248-251, printed pp. 239-242, for Definition 10, Theorem 11 and Proposition 13.
It also read PDF pp. 276-278 and 283-285, printed pp. 268-270 and 275-277, for the Brown convention, positive regularized Laplacian, normal specialization, ellipse theorem and probability-measure weak regularization limit.
Brown existence, probability, support containment, weak convergence and the cited ellipse's spectrum equality remain accepted source results.
This is neither a reconstruction of Brown's original theorem nor a full MS17 audit.
The [existing BZ22 convention account](../literature/BZ22/Yin_U001.md#brown-measure-convention) agrees with the normalized Laplacian used here.
The new derivative/sign calculations and exact project arguments were checked below.
No external search, acquisition, novelty determination or broader attribution investigation was performed.
The original offline attribution limits remain; mathematical validity here does not certify a future manuscript's literature discussion.

## F0078: complete imaginary-drift and capacity finding

Target: [C_F0120 statement](../../claims/Yin_C_F0120_v1.md#statement) and the entire proof beginning with [positive-cone existence and uniqueness](../../claims/Yin_C_F0120_v1.md#existence-strict-convexity-along-positive-cone-paths-and-uniqueness), equations (1)-(14) and final scope.
The Kraus coefficients are selfadjoint, D is arbitrary positive definite, and noise may be empty.
The finite functional uses unnormalized traces, whereas the operator determinant uses the normalized matrix trace.

On Q(t)=Q_0^{1/2}exp(tX)Q_0^{1/2}, negative log determinant is affine.
In a basis diagonalizing selfadjoint X, the drift term is the sum E_kk exp(tx_k) with E>0, and each covariance term is the sum |C_j(k,l)|^2 exp(t(x_k+x_l)).
Nonnegative coefficients give convexity, and nonzero X gives a strictly positive second derivative from D.
Every two positive trial matrices have such a connecting path.
The eigenvalue lower bound by the sum of -log(lambda)+delta lambda makes each sublevel set compact inside the cone, proving an interior minimizer exists.
The first variation is Tr((-Q^{-1}+D+eta(Q))X), since the selfadjoint Kraus map is symmetric for the bilinear trace pairing.
Thus its equation is Q^{-1}=D+eta(Q); the connecting-path argument proves global minimality and uniqueness, with no irreducibility or covariance-invertibility assumption.
The equation is a conclusion, not a trial-domain restriction.

For D=I, sign symmetry and resolvent adjunction give the physical G=-iQ, Q>0.
The C_F0119 primitive gives -log(det Q)/m-Tr(Q eta(Q))/(2m).
Tracing Q^{-1}=I+eta(Q) gives m=Tr Q+Tr(Q eta(Q)), converting the primitive exactly to (min J_D-m)/m.
For general D, T-iD=D^{1/2}(T'-iI)D^{1/2} multiplies only bounded invertible factors and adds log(det D)/m to the logarithmic determinant.
With R=D^{1/2}QD^{1/2}, direct multiplication and cyclicity give J_I^{eta'}(R)=J_D^{eta}(Q)-log(det D), including its quadratic term.
No commutation of D and the coefficients is needed.
The positive trial matrix P_D(Q) has log determinant J_D(Q)-m, proving the determinant-only minimum without a complex logarithm branch.
With empty noise, Q=D^{-1}, min J_D=log det D+m and Delta(-iD)=det(D)^{1/m}.

The Euclidean-Hessian obstruction is exact: conjugation by diag(1,-1) negates any selfadjoint off-diagonal X, and at cI the Hessian is (c^{-2}-1)Tr(X^2), negative for c>1.
Complete positivity therefore does not justify replacing the positive-cone-path argument by Euclidean convexity.

For D=epsilon I, testing each fixed positive Q proves that the limit as epsilon decreases to zero of inf_{Q>0} J_epsilon(Q) is inf_{Q>0} J_0(Q), also when this value is -infinity.
Selfadjoint spectral calculus makes the regularized logarithmic determinant decrease to log Delta(T), including zero atoms.
Thus the zero-drift infimum formula holds without claiming attainment.
The accepted centered MS24 identity gives cap(eta)=exp(2 inf J_0-m).
Writing Q=tB, det B=1, beta=Tr(B eta(B))>=0, minimizes -m log t+t^2 beta/2 at t^2=m/beta when beta>0.
For beta=0 the infimum is -infinity and its exponential is zero.
This proves both capacity reformulations with denominator (det Q)^2 for selfadjoint-Kraus covariance, including zero capacity.

Conclusion: all current mathematics passes for noncentral D>0 and the separately proved D=0 limit.
Arbitrary real drift, all complex spectral parameters, nonzero semidefinite drift boundaries and a general saddle formula remain excluded.

<a id="dependencies-verification-and-boundaries"></a>
<a id="original-f0070-account"></a>
### Original 2026-09-12 imaginary-drift finding

The original R_F0070 finding was dated 2026-09-12.
Its reviewer was the affine-selfadjoint-variation agent, described in the original account as independent of the proof author.
The reviewer developed a separate real-gap proof and expressly did not contribute to this imaginary-drift proof before review, but initial target-context isolation was not established; its historical relationship remains unknown.
Its original bindings covered this same statement and positive-cone argument anchor, including every noncentral-drift, normalization, zero-drift and capacity step.
The complete decisive checks and source/scope limitations of that finding are retained above; the newly independent evidence is this separately dated review act, not retrospective relabelling.

## F0079: initial certified formula

Target: [C_F0121 statement](../../claims/Yin_C_F0121_v1.md#statement), the initial proof through [certified-interval convexity](../../claims/Yin_C_F0121_v1.md#strict-convexity-on-the-certified-order-interval), equations (1)-(14), special cases and warnings.

For R>0 with a_0>=R^{-1}+eta(R) and kappa=||R^{1/2}eta(R)R^{1/2}||<1, put b_j=R^{1/2}a_jR^{1/2} and T=sum b_j tensor ell_j.
Full-Fock creation orthogonality gives T^*T=sum b_j^2 tensor I and ||T||=sqrt(kappa).
Square completion bounds the congruenced pencil below by (I+T)^*(I+T), giving gap (1-sqrt(kappa))^2/||R||.
Equality of compactly supported scalar spectral distributions and faithfulness transfers the gap to the given tracial model.

The map q to (a_0-eta(q))^{-1} is order preserving on [0,R], maps that interval into itself, and yields increasing iterates from zero with positive first iterate.
They converge in matrix norm to a positive definite fixed point.
Schur complementation of finite Fock compressions produces exactly those iterates: after deleting the vacuum, the subtrees are indexed by their last letter and have the preceding truncation.
The positive gap survives compression.
Extending by a fixed positive scalar on each orthogonal complement gives strong convergence, a uniform norm bound and a uniform inverse bound; the resolvent identity gives strong inverse convergence to S^{-1}.
Thus the limit is the physical q=E(S^{-1})<=R, not merely an algebraic root.
Empty noise is included.

For q=R^{1/2}pR^{1/2}, h=R^{1/2}kR^{1/2}, 0<p<=I, diagonalization gives Tr(p^{-1}kp^{-1}k)>=Tr(k^2).
For selfadjoint b_j,k, Tr(b_j^2k^2)-Tr(b_jkb_jk) is one half the squared Hilbert-Schmidt commutator norm.
Hence the objective Hessian is at least (1-kappa)Tr(k^2)>0 for nonzero h.
The order interval is convex and the physical q has zero ambient first derivative even on the upper boundary, proving a unique global interval minimum.
The smaller C_F0119 primitive in the real gap gives (-log det q+Tr(eta(q)q)/2)/m.
Tracing the Dyson equation converts it to J(q)/m including -m, and det exp(X)=exp Tr X proves determinant packaging without commutativity.

The scalar coefficient-norm certificate uses the smaller quadratic root and really has r^2||eta(I)||<1.
Zero covariance forces every noise coefficient to vanish.
The scalar physical-root exclusion, sign reversal and common reducing-block determinant weights hold as stated.
The scalar objective tends to -infinity when the upper restriction is omitted, so an unrestricted minimum would be false.
The stationary action at general u-iv proves no global saddle or ordered minimax, and complete positivity gives no Hilbert-Schmidt quadratic positivity.

Conclusion: the initial certified theorem and subsidiary assertions pass at their certificate hypotheses.
<a id="checks-of-the-full-argument"></a>
<a id="original-f0072-initial-account"></a>
### Original 2026-09-12 certified-formula finding

The original initial R_F0072 finding, dated 2026-09-12, has unknown relationship because initial context isolation is unestablished.
The original reviewer was the affine-capacity-optimization agent, and the original mode was an offline complete review; that historical description does not establish isolation.
Its statement and initial-argument bindings cover equations (1)-(4) and their full proof, empty noise, signs and scalar criterion; they do not by themselves cover the later theorem.
Its earlier exclusion of arbitrary gaps belongs only to this intermediate scope.

## F0079: full strengthened supersolution theorem

Target: the complete [spectral-radius refinement](../../claims/Yin_C_F0121_v1.md#spectral-radius-refinement-and-an-intrinsic-feasible-set), [global-minimality proof](../../claims/Yin_C_F0121_v1.md#proof-of-global-minimality) and determinant packaging, equations (15)-(27), in the checked initial context.

For selfadjoint c_j=R^{1/2}a_jR^{1/2}, creation-word orthogonality and reversal of the summed coefficient word give (T^k)^*T^k=Phi_R^k(I) tensor I for every k.
Since Phi_R^k is completely positive, ||Phi_R^k||=||Phi_R^k(I)||; the spectral-radius formula gives r(T)^2=r(Phi_R).
Stability r(Phi_R)<1 thus makes I+T invertible without assuming ||T||<1, and square completion proves the gap.
The inverse iteration still selects the physical q.
Selfadjointness of Phi_R for the Hilbert-Schmidt inner product bounds its quadratic form above by r(Phi_R)Tr(k^2), proving the improved Hessian estimate on the interval.

If S>=gamma I, the physical q(t)=E((S-tI)^{-1}) is positive and differentiable in the real gap, and its continued Dyson equation is q(t)^{-1}=a_0-tI-eta(q(t)).
At zero this gives q'=q^2+q eta(q')q>0.
With H=q^{-1/2}q'q^{-1/2}>0, H-Phi_q(H)=q>0.
The positive order isomorphism from H produces a similar completely positive map whose value at I is strictly below I, so its norm and spectral radius are below one.
Thus every strictly positive pencil has the stable physical certificate q.
The interval comparison gives q<=R and J(R)>=J(q) for each stable certificate, with equality only at q, without assuming the stable-domain set convex.

Schur complementation identifies L(R)>0 with R>0 and F(R)=a_0-R^{-1}-eta(R)>0.
Square completion shows a strict residual supplies S>=delta I without stability of that R.
Conversely q(t), 0<t<gamma, has F(q(t))=tI>0.
The strict affine-matrix-inequality characterization is therefore equivalent to strict positivity.
The exact scalar example a_0=3, eta(R)=R, R=2 has residual 1/2 but r(Phi_R)=4, so feasibility does not imply stability of each trial matrix.

Every nonstrict supersolution R bounds the inverse iterates above.
The gap of S independently supplies the Fock-compression inverse bounds, proving the least-supersolution comparison q<=R without a stability condition on R.
Both L(R)>=0 and L(R)>0 domains are convex because L is affine and R remains positive definite.
For Q_t=q+t(R-q), the second derivative of F is -2Q_t^{-1}(R-q)Q_t^{-1}(R-q)Q_t^{-1}<=0.
Thus F(Q_t)>=0 and dJ(Q_t)/dt=Tr(F(Q_t)(R-q))>=0, proving global minimality without a false global convexity claim.
The stable physical q has strictly positive Hessian in every nonzero direction, giving strict initial increase on every nonconstant feasible order segment and then uniqueness by monotonicity.
The strict supersolutions q(t) approach q and their objective values converge, giving the strict-domain infimum.
The unique minimizer has F(q)=0, so this strict infimum is not attained.
The positive trial matrix P(R) has log determinant J(R), proving both normalized determinant formulas.

Conclusion: the final theorem passes for every strictly positive selfadjoint affine pencil and, by sign reversal, every strictly negative one.
Indefinite pencils, spectral bulk and positive spectral-edge operators with zero in their spectrum are excluded.
Nonstrict feasibility, for example 2+s, cannot replace strict positivity.

<a id="checks-of-the-strengthened-proof"></a>
<a id="original-f0072-strengthened-account"></a>
### Original 2026-09-12 strengthened-formula finding

The strengthened original R_F0072 finding was also dated 2026-09-12, later that day than the initial review.
The coordinating agent supplied preliminary mechanisms to the author; the historical reviewer did not supply or edit them, but its initial context isolation remains unestablished and its relationship remains unknown.
Its statement and selected-global-argument bindings cover equations (15)-(27) in the context of the earlier proof.
All seven strengthened checks and their negative/source boundaries are retained above.
R_F0072's separate [original signed-Schur-linearization finding](#separate-check-signed-schur-linearization), equations (1)-(2) of L_F0033, is retained at its unknown relationship and is neither replaced nor newly independently reviewed here.

## F0080: scalar and commuting finding

Target: [C_F0122 statement](../../claims/Yin_C_F0122_v1.md#statement), [scalar/commuting proof](../../claims/Yin_C_F0122_v1.md#inputs-and-exact-optimization), equations (1)-(7), saddle warning and deterministic coordinates.

For fixed p, differentiation in r=q^2>=0 gives a strictly decreasing derivative and unique maximum r=(sigma-p^2)_+.
At p=0, the maximizing q is sqrt(sigma), so log zero at (0,0) causes no missing optimizer.
The reduced function has matching values and first derivatives at p=+-sqrt(sigma), second derivative 2/sigma inside and 1/sigma-1/p^2 outside.
It is continuously differentiable, strictly convex and coercive.
The stated unique root is correct for both signs of exterior drift and agrees with a/2 at both support edges.
For g=1/p at the exterior optimum, a-p=sigma g, so substitution gives the exact primitive and variance scaling.
Zero drift gives (log sigma-1)/2, consistent with scalar capacity.
Exponentiation preserves the successive attained extrema and assigns zero at the logarithmic singularity.

Simultaneous diagonalization gives the commuting direct-sum formula from marginal semicircular laws, without independence between diagonal entries.
The extrema separate coordinatewise.
Zero variance contributes its deterministic log absolute value, and a zero deterministic entry forces the total logarithmic determinant to -infinity.
For exterior drift, holding q=0 fixed allows L(p,0) to tend to -infinity at zero, so the ordered optimizer is not a raw global saddle.
This alone proves no strict gap between optimization orders and permits no interchange.

Conclusion: all scalar/commuting assertions pass.
<a id="scalar-and-commuting-calculations"></a>
<a id="original-f0071-scalar-account"></a>
### Original 2026-09-12 scalar and commuting finding

The original R_F0122 scalar finding was dated 2026-09-12; neither target contribution nor initial isolation is established for this part, so its relationship remains unknown.
The original reviewer was the reviewing agent and the proof author was root.
Its statement and scalar-argument bindings cover equations (1)-(7), the singular point, physical root, deterministic coordinates and saddle failure.
Those complete checks and boundaries are retained above.

## F0080: isotropic and whole spectral measure finding

Target: the complete [isotropic extension](../../claims/Yin_C_F0122_v1.md#isotropic-covariance-minimax) and [physical-solution argument](../../claims/Yin_C_F0122_v1.md#identifying-the-physical-solution-and-the-determinant), equations (8)-(15).
The exact hypothesis is eta(b)=sigma tr_m(b)I, sigma>0, with selfadjoint coefficients and arbitrary selfadjoint drift; coefficient commutation is unnecessary.

I(p,q) strictly decreases in q^2, giving the unique inner maximum.
At an atom of mass w its positive solution has q^2>=sigma w and cannot meet zero there.
Off atoms, I(p,0)=1/sigma is a nonconstant rational equation with finitely many roots, and the positive-q set is bounded.
These facts prove continuity, including edges and isolated closing gaps.
Implicit differentiation gives q'=-C/(qB) and X'=2sigma(q^2B+C^2/B)>0 on positive branches.
On open zero branches X'=1-sigma I>0; equality is possible only at finitely many transitions.
Continuity and X(p)=p+O(1/p) prove X strictly increasing onto the real line.
The reduced derivative is (X(p)-x)/sigma, continuously extending across transitions, so the reduced objective is strictly convex, coercive and uniquely minimized at X(p)=x.

The physical scalarized Dyson equation gives w=z-sigma g, Im w>0 and epsilon=q(1-sigma I), so I<1/sigma.
Cauchy-Schwarz gives |g|<=1/sqrt(sigma); each drift eigenvalue has mass at least 1/m, hence |w-lambda_k|>=sqrt(sigma/m).
These estimates bound w for fixed real argument and separate all boundary limits from poles.
Every subsequential limit satisfies exactly the inner maximizing condition and X(p)=x, which identifies the full limit at every real point, including edges and closing gaps.
The same compactness argument with varying real parts proves continuous boundary values.
The primitive's normalized quadratic trace is sigma g^2; substituting g=(x-p-iq)/sigma gives precisely the ordered objective.
Pole separation makes its limit finite and monotone selfadjoint spectral integration identifies the logarithmic determinant.
The uniform g bound justifies dominated Poisson inversion and makes every atom vanish.
Agreement on all interval masses gives the whole continuous density q(X^{-1}(x))/(pi sigma), excluding singular continuous residue as well as atoms.
Faithfulness identifies support and spectrum.
Exponentiation gives the stated scalar exponential times matrix determinant.
The capacity definition and the arithmetic-geometric mean inequality give cap(eta)=sigma^m at zero drift, and the result becomes exp(-1/2)sqrt(sigma); m=1 reduces by translation to the scalar formula.

Conclusion: the full isotropic extension passes independently, including its complete spectral measure.
No general-covariance minimax, arbitrary noncommuting trial substitution or raw global saddle is proved.
The adequate original 2026-09-12 [R_F0122 isotropic self-review](Yin_R_F0122_v1.md#isotropic-covariance-calculations) remains in place: its reviewer had received root's proposed target formulas before review.
That old self-reviewed account is reused by reference, not copied, removed or retrospectively reclassified.
The independently checked mathematics here is new evidence from this isolated arrangement.

## F0081: complete derivative and spectral finding

Target: [C_F0123 statement](../../claims/Yin_C_F0123_v1.md#statement), the entire [finite derivative-system argument](../../claims/Yin_C_F0123_v1.md#exact-derivatives-from-one-finite-linear-system), selfadjoint equation, scalar benchmarks and limits.

Hermitization, covariance, dimensions and normalized traces agree with C_F0119.
SP2 keeps the regularized quadratic covariance term; SP3 is the separately justified limiting capacity notation.
Block inversion gives G_21=-E(Q^{-1}S_z^*), and partial_z Q=-S_z^* gives partial_z u_epsilon=tr_m(G_21)/2.
Differentiating partial_bar_z A_z=-E_21 yields X-G Theta(X)G=-GE_21G with no extra adjoint.
The shared strict weighted contraction, with both solutions equal to G, gives zero kernel for the homogeneous system; finite dimension gives unique solvability for every fixed epsilon>0.
It gives no uniform inverse bound at zero regularizer.

Independent operator differentiation, with S_zQ^{-1}S_z^*=I-epsilon^2P^{-1}, gives partial_bar_z partial_z u_epsilon=epsilon^2 phi(Q^{-1}P^{-1})/2.
Cyclicity turns the trace into that of the positive sandwich Q^{-1/2}P^{-1}Q^{-1/2}, without commutation of P,Q.
With mu=(2pi)^{-1}nabla^2 u and nabla^2=4partial_bar_z partial_z, this proves rho_epsilon=tr_m(X_21)/pi=epsilon^2 phi(Q^{-1}P^{-1})/pi>=0.
The selected MS17 interface gives probability and weak convergence to Brown measure, allowing atoms and curves; no pointwise density convergence or differentiation of the limiting potential is asserted.

For selfadjoint coefficients the smaller Dyson primitive has factors 1/m and 1/(2m).
Integrating the scalar Poisson kernel gives the interval formula with half endpoint weights and the atom formula by dominated convergence.
The accepted normal specialization gives Brown measure on the real line, and faithfulness identifies support with spectrum.
A gap gives physical-resolvent analytic continuation with selfadjoint boundary values; the converse follows by inversion on compact subintervals.
An arbitrary real algebraic root cannot replace physical continuation.

For scalar coefficients, rotating c=sum a_j^2 to r=|c|>=0 preserves v=sum |a_j|^2.
The real/imaginary coefficient vectors become orthogonal and their only nonzero second free cumulants give free semicircular coordinates of variances (v+r)/2 and (v-r)/2.
For r<v, the scaled MS17 ellipse has semiaxes (v+r)/sqrt(v),(v-r)/sqrt(v), area pi(v^2-r^2)/v and density v/(pi(v^2-r^2)).
The interior Dyson equations give h^2+|q|^2=1/v, v conjugate(q)+rq=z and q=x/(v+r)-iy/(v-r).
The quadratic potential has Laplacian 2v/(v^2-r^2), with centered constant (log v-1)/2 from MS24.
Outside, rq^2-zq+1=0 with q asymptotic to 1/z has primitive -log|q|+r Re(q^2)/2, derivative q/2 and logarithmic growth.
Its value and gradient match the interior expression on the ellipse, recovering the same source-based potential.
r=0 gives the disk; r=v is a rotated real semicircle and the two-dimensional formulas with zero denominator do not apply; v=0 gives delta_0.
Changing c at fixed v changes the law, preserving the missing-covariance warning.

Conclusion: the complete module passes at positive regularizer and for its stated selfadjoint/scalar consequences.
Uniform boundary stability, general Brown absolute continuity and general support/spectrum equality remain unproved.
Ellipse spectrum equality is a separately accepted source example.

<a id="new-calculations-checked"></a>
<a id="original-f0073-account"></a>
### Original 2026-09-12 derivative and spectral finding

The original R_F0073 finding was dated 2026-09-12 and identifies the coordinating agent/root as reviewer and a separate agent as module writer.
Initial context isolation was unestablished, so its historical relationship remains unknown.
Its statement and derivative-argument bindings cover SP1-SP15, selfadjoint inversion and the exact elliptic/circular/line benchmarks with these accepted foundations and limitations.
The original author read the selected source passages; root additionally rendered and viewed PDF pp. 277 and 285, printed pp. 269 and 277.
That old source inspection remains historical evidence; this review's new source check was text extraction, not a new rendered-page inspection.
The source's informal density parenthesis after (11.15) omits the factor, while its explicit (11.6) and the project convention give 1/(2pi).
All original sign, positivity, normalization and source-depth qualifications are retained.

## Other retained history and verification limits

<a id="additional-reading-2026-09-12"></a>
<a id="additional-coordinating-agent-reading-on-2026-09-12"></a>
A separate contemporaneous 2026-09-12 registration account recorded the coordinating agent reading all four complete proofs and checking C_F0120's noncentral congruence/capacity limit, C_F0121's least-supersolution minimum and C_F0123's derivative calculation and selected MS17 page images.
This preserves the event from the registration correspondence `2026-09-12-affine-variational-registration_v1.md` without asserting that its retired administrative table remains available.
The coordinating agent authored C_F0122 and retained the separate reviewer's assessment.
This historical reading does not establish initial isolation and is not recertified as a new independent review.

The four proofs and their old selected findings use analytic identities, operator inequalities and finite-matrix symbolic arguments; no retained native dataset, scan or J output is necessary.
The finite examples above were verified algebraically at their full stated ranges, without treating a producer's PASS text as evidence.
No numerical experiment, finite rerun, proof-assistant formalization, external human review, novelty search, full source-proof audit or Task completion is claimed.
The new findings agree with the old mathematical findings at their actual scopes and add only the separately performed independent coverage.

## Original combined review entrances

<a id="original-f0039-review-account"></a>
The original 2026-09-12 C_F0121 review account comprises the [initial certified-formula finding](#checks-of-the-full-argument) and the [later strengthened-formula finding](#checks-of-the-strengthened-proof), each at its original unknown relationship, date and binding scope.
This entrance preserves references whose stated C_F0121 scope included both findings.

<a id="original-f0072-account"></a>
The complete original combined account also includes the separate [signed-Schur finding](#separate-check-signed-schur-linearization), in addition to those two C_F0121 findings.
The [additional coordinating-agent reading](#additional-reading-2026-09-12) keeps its separate historical event and actual author/reviewer boundary.

<a id="original-f0071-account"></a>
The original 2026-09-12 scalar/isotropic account comprises the [scalar and commuting finding](#scalar-and-commuting-calculations) at its unknown relationship and the [isotropic finding](Yin_R_F0122_v1.md#isotropic-covariance-calculations) at its original self-reviewed relationship.
This entrance preserves references whose stated historical scope included both findings, while each finding keeps its actual separate relationship and bindings.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Additional isolated signed-Schur review](#isolated-signed-schur-review) | independently reviewed |
| [Original signed-Schur finding](#separate-check-signed-schur-linearization) | unknown |
| [F0078](#f0078-complete-imaginary-drift-and-capacity-finding) | independently reviewed |
| [F0079 initial](#f0079-initial-certified-formula) | independently reviewed |
| [F0079 strengthened](#f0079-full-strengthened-supersolution-theorem) | independently reviewed |
| [F0080 scalar](#f0080-scalar-and-commuting-finding) | independently reviewed |
| [F0080 isotropic](#f0080-isotropic-and-whole-spectral-measure-finding) | independently reviewed |
| [F0081](#f0081-complete-derivative-and-spectral-finding) | independently reviewed |
| [Original F0078](#dependencies-verification-and-boundaries) | unknown |
| [Original F0079 initial](#checks-of-the-full-argument) | unknown |
| [Original F0079 strengthened](#checks-of-the-strengthened-proof) | unknown |
| [Original F0080 scalar](#scalar-and-commuting-calculations) | unknown |
| [Original F0081](#new-calculations-checked) | unknown |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Additional isolated signed-Schur review](#isolated-signed-schur-review) | [Signed Schur segment](../../ledger/Yin_L_F0033_v1.md#signed-schur-linearization) | Entire local segment: bounded epsilon-positive factorization, normalized determinant identity, affine selfadjoint form and explicit indefinite-variational boundary. No whole-synthesis or general indefinite optimization review. |
| [Original signed-Schur finding](#separate-check-signed-schur-linearization) | [Original algebraic reduction](../../ledger/Yin_L_F0033_v1.md#signed-schur-linearization) | Only the signed Schur linearization and normalized regularized determinant identity at equations (1)–(2) in L_F0033. This is no full review of the synthesis or an indefinite variational formula. |
| [F0078](#f0078-complete-imaginary-drift-and-capacity-finding) | [Statement](../../claims/Yin_C_F0120_v1.md#statement) | All current equations (1)-(14), noncentral D>0, empty noise, separate D=0 limit and selfadjoint-Kraus capacity recovery; no arbitrary real drift, nonzero semidefinite boundary or general saddle. |
| [F0078](#f0078-complete-imaginary-drift-and-capacity-finding) | [Argument](../../claims/Yin_C_F0120_v1.md#existence-strict-convexity-along-positive-cone-paths-and-uniqueness) | Entire compactness, positive-cone strict convexity, physical Dyson, primitive, congruence, zero-drift and capacity proof, with the accepted source depths above. |
| [F0079 initial](#f0079-initial-certified-formula) | [Statement](../../claims/Yin_C_F0121_v1.md#statement) | Initial equations (1)-(4), full proof and equations (5)-(14), empty noise, signs, scalar certificate and domain warnings; not alone the later theorem. |
| [F0079 initial](#f0079-initial-certified-formula) | [Initial argument](../../claims/Yin_C_F0121_v1.md#strict-convexity-on-the-certified-order-interval) | Norm-certificate gap, physical inverse iteration/compression, interval strict convexity, determinant normalization, special cases and limitations. |
| [F0079 strengthened](#f0079-full-strengthened-supersolution-theorem) | [Statement](../../claims/Yin_C_F0121_v1.md#statement) | Full equations (15)-(27) for every strictly positive/negative pencil in the checked initial context; indefinite and zero-gap positive pencils excluded. |
| [F0079 strengthened](#f0079-full-strengthened-supersolution-theorem) | [Selected argument](../../claims/Yin_C_F0121_v1.md#proof-of-global-minimality) | Spectral-radius refinement, stable physical inverse, strict affine feasibility, least supersolution, global minimum/uniqueness, strict-domain nonattainment and determinant packaging. |
| [F0080 scalar](#f0080-scalar-and-commuting-finding) | [Statement](../../claims/Yin_C_F0122_v1.md#statement) | Complete equations (1)-(7), attained ordered extrema, unique optimizer, support edges, deterministic coordinates and saddle warning; no order interchange. |
| [F0080 scalar](#f0080-scalar-and-commuting-finding) | [Scalar argument](../../claims/Yin_C_F0122_v1.md#inputs-and-exact-optimization) | Exact inner maximum, reduced strict convexity/coercivity, physical root, logarithmic normalization and commuting direct sums. |
| [F0080 isotropic](#f0080-isotropic-and-whole-spectral-measure-finding) | [Statement](../../claims/Yin_C_F0122_v1.md#statement) | Full equations (8)-(15), arbitrary selfadjoint drift, every real argument, repeated eigenvalues, edges/closing gaps, determinant and whole continuous spectral measure; no general covariance minimax. |
| [F0080 isotropic](#f0080-isotropic-and-whole-spectral-measure-finding) | [Isotropic argument](../../claims/Yin_C_F0122_v1.md#identifying-the-physical-solution-and-the-determinant) | Entire scalarization, inner maximum, monotone X, reduced convexity, physical branch/pole separation, continuous limits, primitive/inversion and determinant proof. |
| [F0081](#f0081-complete-derivative-and-spectral-finding) | [Statement](../../claims/Yin_C_F0123_v1.md#statement) | Complete SP1-SP15, fixed-positive-regularizer system and Brown weak limit, selfadjoint inversion, scalar benchmarks and stated negative boundaries. |
| [F0081](#f0081-complete-derivative-and-spectral-finding) | [Selected argument](../../claims/Yin_C_F0123_v1.md#exact-derivatives-from-one-finite-linear-system) | Whole derivative/contraction/sign/Laplacian proof, accepted Brown weak limit, physical selfadjoint gaps and elliptic/circular/line tests; no uniform boundary stability or general support/spectrum equality. |
| [Original F0078](#dependencies-verification-and-boundaries) | [C_F0120 statement](../../claims/Yin_C_F0120_v1.md#statement) | Every original statement and proof for noncentral positive definite imaginary drift: existence, positive-cone strict convexity, unique global minimum, physical Dyson identification, determinant normalization, zero-drift passage and ordinary-capacity reformulation. No arbitrary real drift or general saddle is included. |
| [Original F0078](#dependencies-verification-and-boundaries) | [C_F0120 argument](../../claims/Yin_C_F0120_v1.md#existence-strict-convexity-along-positive-cone-paths-and-uniqueness) | Every original statement and proof for noncentral positive definite imaginary drift: existence, positive-cone strict convexity, unique global minimum, physical Dyson identification, determinant normalization, zero-drift passage and ordinary-capacity reformulation. No arbitrary real drift or general saddle is included. |
| [Original F0079 initial](#checks-of-the-full-argument) | [C_F0121 statement](../../claims/Yin_C_F0121_v1.md#statement) | Initial certified formula, equations (1)–(4): strict positive spectral gap, physical inverse expectation, strict convexity and unique minimum over the directly specified interval zero less than q at most R, including empty noise, signs and scalar certificate. This finding does not by itself cover the later all-supersolution extension. |
| [Original F0079 initial](#checks-of-the-full-argument) | [Initial proof](../../claims/Yin_C_F0121_v1.md#strict-convexity-on-the-certified-order-interval) | Initial certified formula, equations (1)–(4): strict positive spectral gap, physical inverse expectation, strict convexity and unique minimum over the directly specified interval zero less than q at most R, including empty noise, signs and scalar certificate. This finding does not by itself cover the later all-supersolution extension. |
| [Original F0079 strengthened](#checks-of-the-strengthened-proof) | [C_F0121 statement](../../claims/Yin_C_F0121_v1.md#statement) | Strengthened proof, equations (15)–(27), in the context of the earlier proof: spectral-radius square completion, stable physical inverse for every strictly positive pencil, affine matrix feasibility, least-supersolution comparison, global minimum and strict-domain nonattainment, uniqueness and positive determinant packaging. Indefinite and zero-gap positive pencils remain excluded. |
| [Original F0079 strengthened](#checks-of-the-strengthened-proof) | [C_F0121 selected argument](../../claims/Yin_C_F0121_v1.md#proof-of-global-minimality) | Strengthened proof, equations (15)–(27), in the context of the earlier proof: spectral-radius square completion, stable physical inverse for every strictly positive pencil, affine matrix feasibility, least-supersolution comparison, global minimum and strict-domain nonattainment, uniqueness and positive determinant packaging. Indefinite and zero-gap positive pencils remain excluded. |
| [Original F0080 scalar](#scalar-and-commuting-calculations) | [C_F0122 statement](../../claims/Yin_C_F0122_v1.md#statement) | Complete scalar and commuting ordered minimax proof, equations (1)–(7): successive extrema, strict convexity after the inner maximum, unique optimizer, physical scalar root, determinant normalization, zero-variance coordinates and failure of a raw global saddle. No optimization-order interchange is certified. |
| [Original F0080 scalar](#scalar-and-commuting-calculations) | [Scalar and commuting argument](../../claims/Yin_C_F0122_v1.md#inputs-and-exact-optimization) | Complete scalar and commuting ordered minimax proof, equations (1)–(7): successive extrema, strict convexity after the inner maximum, unique optimizer, physical scalar root, determinant normalization, zero-variance coordinates and failure of a raw global saddle. No optimization-order interchange is certified. |
| [Original F0081](#new-calculations-checked) | [C_F0123 statement](../../claims/Yin_C_F0123_v1.md#statement) | Complete finite derivative system and regularized Brown potential, selfadjoint Cauchy/Poisson inversion and exact scalar elliptic, circular and line-supported benchmarks. Brown construction and weak convergence remain accepted local MS17 interfaces; uniform boundary stability and general Brown support/spectrum equality are excluded. |
| [Original F0081](#new-calculations-checked) | [C_F0123 selected argument](../../claims/Yin_C_F0123_v1.md#exact-derivatives-from-one-finite-linear-system) | Complete finite derivative system and regularized Brown potential, selfadjoint Cauchy/Poisson inversion and exact scalar elliptic, circular and line-supported benchmarks. Brown construction and weak convergence remain accepted local MS17 interfaces; uniform boundary stability and general Brown support/spectrum equality are excluded. |

## Additional signed-Schur review arrangement

Review act: 2026-10-23T00:29 UTC, a separately delegated reviewing agent under Yin's authorized M04 review.
The reviewing agent did not develop or repair either target proof.
It received the fixed complete mathematical body of [C_F0111](../../claims/Yin_C_F0111_v1.md#statement) and the fixed entire [signed Schur segment](../../ledger/Yin_L_F0033_v1.md#signed-schur-linearization) directly, with relative links interpreted at their canonical homes.
Pure assessment sections were excluded from those supplied mathematical views.
Before the initial findings, no previous review of either target, exploration notes, development dialogue, author explanation or target-specific mathematical summary was supplied or consulted.
The author's fixed mathematics, the actual dependency interfaces and their disclosed source-acceptance scopes were legitimate inputs.
Initial findings covering both entire targets were communicated before the original accounts retained below were opened.
The later comparison found no mathematical discrepancy with either original account.

The signed-Schur finding retained below is an independent review of its fixed local scope.
The separate charge finding is retained in [the existing charge review](Yin_R_F0121_v1.md#isolated-whole-c73-review).
The retained original findings keep their original dates, unknown relationships, provenance, findings and limits.
Their historical independence terminology is an original assertion, not a new context-isolation certification.
No mathematical source, native program, Task or execution boundary was changed by this review.


<a id="isolated-signed-schur-review"></a>
## Isolated complete local review of the signed Schur linearization

Disposition: pass for the entire fixed local segment [L_F0033, signed-schur-linearization](../../ledger/Yin_L_F0033_v1.md#signed-schur-linearization), including equations (1)-(2), the semicircular affine form and the stated unresolved boundary.
This is a standalone local algebraic/determinant review, not a review of the whole ledger synthesis or an indefinite variational theorem.

For Q=SS*+epsilon^2 I, multiplication of the first two factors gives [[Q,S],[0,-I]], and multiplying by the third gives [[Q-SS*,S],[S*,-I]].
The upper-left block is epsilon^2 I, with the displayed noncommutative order preserved.
Q is bounded strictly positive for epsilon>0, and both triangular factors are invertible with the sign of their off-diagonal blocks reversed.
The diagonal factor is also invertible, so the factorization establishes actual invertibility of L_epsilon.

For each outer factor, write its affine path as I+tN with N^2=0 and normalized trace of N zero.
Its inverse is I-tN, so (I+tN)^(-1)N=N and the traced logarithmic determinant derivative vanishes.
Its Fuglede-Kadison determinant is therefore one.
The bounded invertible multiplicativity interface and finite-tracial scope are supplied by [L_F0036](../../ledger/Yin_L_F0036_v1.md#bounded-multiplicativity-and-the-factor-convention) and its retained [FK52-U001](../literature/FK52/Yin_U001.md#fk52-u001).
The diagonal factor has absolute value diag(Q,I), so its normalized 2m log determinant is one half of phi_m(log Q).
Equality of the normalized spectral distributions of SS* and S*S, including their zero masses in this finite tracial setting, identifies exp(one half phi_m(log Q)) with [C_F0119's Delta_epsilon convention](../../claims/Yin_C_F0119_v1.md#a-finite-dimensional-primitive-of-the-cauchy-transform).
There is no missing square root or matrix-size factor.

For S=a_0+sum_j a_j s_j the two displayed block coefficient matrices are selfadjoint, so L_epsilon is an actual selfadjoint affine semicircular pencil.
The positive/negative Schur-block factorization makes clear that this pencil is indefinite.
Consequently the positive-pencil minimum cannot be applied, and no ordered minimum/maximum, feasible-domain theorem or physical-branch comparison has been proved here.
The final paragraph keeps all of these obligations explicit.
The limit epsilon down to zero invokes only the usual regularized log integral, including zero determinant values.
No direct opening of FK52 primary pages or new source acquisition was performed in this review; the accepted bounded invertible source interface was checked at its retained proof and applicability scope.


## Retained original signed-Schur account and relationship

Original date/reviewer: 2026-09-12, affine-capacity-optimization agent.
The original review mode was described as an independent complete offline proof review.
The reviewer did not develop or edit this inspected proof and developed a separate positive-imaginary-drift optimization in parallel.
These antecedent roles do not establish initial context isolation.
This signed-Schur finding therefore retains its actual unknown relationship.
The other original findings are outside this retained local account.

## Separate Check: Signed Schur Linearization

Also inspected on 2026-09-12: equations (1)-(2) and their accompanying arguments in [ledger/affine-variational-frontier.md](../../ledger/Yin_L_F0033_v1.md#signed-schur-linearization).
This is a check of that local algebraic reduction, not a mathematical review of every linked result in the synthesis.

Disposition: pass.
Multiplying the three displayed factors gives exactly
\[
 \begin{pmatrix}\varepsilon^2I&S\\S^*&-I\end{pmatrix},
\]
because the upper-left Schur block is \(SS^*+\varepsilon^2I\).
Each off-diagonal triangular factor is invertible and has determinant one; along its path from the identity the inverse times the derivative is the same trace-zero square-zero matrix.
The diagonal factor has log Fuglede-Kadison determinant \(\tfrac12\varphi_m\log(SS^*+\varepsilon^2I)\) with the trace normalized in dimension 2m.
This is exactly the regularized log determinant of S, with no additional square root or dimension factor.
The distinction between invertibility and definiteness is retained: the resulting affine pencil is indefinite, so the positive-pencil variational theorem does not apply directly.
No general indefinite optimization principle is claimed by this factorization.



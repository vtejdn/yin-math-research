---
author: Yin
---

# Isolated whole-proof review of the intrinsic affiliated rationality criterion

Date: 2026-10-21T04:09.
Human record author: Yin.
Review method: a separately assigned, isolated AI reviewing agent outside substantive development of the inspected proof.
This record contains a new whole-proof inspection and a subsequent comparison with an older review as an explicit audit object.
It makes no Claim assessment or Task disposition.

## Whole intrinsic proof

Finding: the complete intrinsic theorem in [C_F0063 v1](../../claims/Yin_C_F0063_v1.md#liberation-intrinsic-affiliated-criterion), Sections 1--5 and Appendix A, is mathematically supported under its exact C_F0025 premises and the accepted foundational inputs delimited below.
The inspection found no substantive gap requiring a repair of that fixed argument.
The conclusion includes the final weak-cluster proof of the all-M sum identity and its complete downstream fraction, deconvolution, and equalizer chain.

### Input arrangement and reading order

The assigning message supplied the fixed artifact, permitted mathematical dependencies, and scope directly.
It supplied no proof-generation dialogue, exploration summary, author explanation, or old mathematical verdict.
Before consulting the target's assessment or old review, the reviewer read C_F0063's fixed mathematical body, physical lines 13--371, and enumerated and checked the obligations of its statement and full argument.
The reviewer also read the necessary fixed mathematical interfaces in C_F0025 Sections 1--3 and 7, C_F0027 Sections 1 and 5--6, C_F0043 Sections 2--3.2, the C_F0034 statement and complete P1 proof, and the C_F0035 statement, complete P1 proof, and source supplement.
C_F0031's statement and complete P1 proof were inspected for the transitive finite-rank cancellation interface.
Necessary fixed source-interface records were consulted at the scopes stated below.
Their retained source-acceptance and inspection-limit statements, including source records' embedded historical review prose, were available as accepted-dependency scope; they were not target C_F0063 verdicts or a substitute for this proof inspection.

Only after the initial mathematical findings were formed and reported to the assigning agent did the reviewer read C_F0063's Current assessment, assessment history, and recorded review scopes, followed by [R_F0034's complete retained finding](Yin_R_F0034_v1.md#permanent-whole-independent-review-intrinsic-affiliated-criterion).
The comparison appears separately below.
The reviewer did not open the linked L_F0011 exploration, R_F0035, the [original left/right-state graph finding](Yin_R_F0078_v1.md#independent-review-left-and-right-states-recover-the-original-output-graph), earlier scratch drafts, proof-generation sessions, or the separately mentioned bounded-graph companion.
No substantive repair was supplied to the inspected proof.

The inspected source is the dated working-tree text of the named fixed v1 artifacts, with local HEAD 1d939b2986bbcc04e77eef448a763ca81037e44b available as repository context.
Those paths had existing working changes when inspected; this record does not identify their working-tree text with an earlier committed byte image.
The mathematical target is precisely the statement and Sections 1--5 plus Appendix A at the two C_F0063 anchors in the bindings below.
Later Claim decisions remain separate adoption acts.

### Exact statement and quantifiers

The premises are a finite von Neumann algebra M with faithful normal probability trace tau, H=L2(M,tau), a finite bounded normal tuple X generating M, and the Hilbert-dense starred algebra P=C<X,X*>.
For every i, the original complex-linear D_i0 has domain exactly P, the vacuum is in Dom D_i0*, [D_i0,X_j]=delta_ij P_Omega on P, and each starred-generator commutator has a compact bounded extension.
Compactness is retained; it is not replaced by boundedness.
The normalization E_i0(p)=D_i0(p)-p D_i0(1) is derived from these data.
The rational algebra F=Div_U C<X> uses the unstarred generators and U=U(M).

For every affiliated u and each bounded fraction pair u=s^-1 a=b t^-1, the coefficients s,a,b,t belong to M and s,t are regular.
Numerators need not be regular unless u is a unit and the inverse-pair argument is being used.
The actual liberation defect is defined on all M using A_i, the original closure from P.
The theorem says u belongs to F exactly when, for one such pair, every K_i exists under the specified Hilbert-Schmidt inverse convention and is finite rank.
Equivalently every always-defined dense tensor-test functional has a finite algebraic Hilbert-tensor representer.
In that event every bounded fraction pair works, K_i=Theta(s partial_i^rat(u) t), and the finite numerical ranks are fraction independent.
The statement quantifies over arbitrary affiliated u, including unbounded u and rational expressions with unbounded intermediate inverses.

### Original data, normalization, and liberation domains

C_F0025 supplies canonical coarse derivations partial_i with E_i0=(id tensor tau)partial_i and actual L2 vacua.
Its normal-phase identity determines the starred-generator derivatives rather than treating them as independent free coordinates.
Its maximal-Delta/free-field conclusion makes every X_i-lambda a unit of U and makes F a same-unit division subring.
That last conclusion is needed for the removal lemma and the equalizer; the notation Div by itself would not supply it.

For eta_i0=D_i0(1), the normalization term p maps to p eta_i0 has the actual adjoint value p eta_i0* on bounded test vectors.
Traciality cancels its contribution to the original weak forms.
For any legitimate all-M cleared expression its contribution is (sb-at)q eta_i0=0.
This calculation does not identify arbitrary raw domains for the two original closures.

For fixed i, B_i=R_Xi tensor I-I tensor L_Xi is a bounded normal inner multiplier and commutes with the outer affiliated actions wherever those algebraic actions are used.
The normal phase gives B_i partial_i(a)=a tensor 1-1 tensor a for a=X_i,X_i*, and zero for the other starred generators.
Thus delta_i=i B_i partial_i has algebraic polynomial-tensor values and is real for flip-adjoint.
The generator check and outer Leibniz rule prove reality on all P.

The polynomial-tensor adjoint formulas give partial_i*(X_i* tensor 1)=X_i* xi_i-1 and partial_i*(1 tensor X_i*)=xi_i X_i*-1.
Their correction terms cancel, giving the actual vacuum zeta_i=-i[X_i*,xi_i] in L2.
Reality makes zeta_i selfadjoint.
The same adjoint calculation supplies polynomial tensors in Dom delta_i*, closability, and T_i0* p=p zeta_i-T_i0 p.
These are actual adjoint-domain statements, not formal adjoint symbols.

The coassociativity calculation retains its nonzero defect.
The difference of the two L=B_i partial_i iterates is kappa L on generators; for delta=iL the difference is -kappa L=i kappa delta.
Mixed Leibniz terms cancel, extending that identity to P.
After contraction it gives T_i0^2 p=(id tensor tau)((delta_i p) dot zeta_i)+i T_i0 p with the positive i term.
Every iterated input here remains in P.

The energy identity is
\[
 \|T_{i,0}p\|_2^2
 =2\operatorname{Re}\langle T_{i,0}p,p\zeta_i\rangle
  -\langle\delta_i(p^*p),1\otimes\zeta_i\rangle
  -\langle iT_{i,0}p,p\rangle .
\]
Taking real parts and estimating the last term in absolute value gives the required extra +1.
For a selfadjoint strict core contraction a, the differentiated binomial series supplies norm approximants to u=a+i sqrt(1-a^2) with convergent first derivative and adjoint derivative.
The last energy identity therefore passes to u; its product derivative is zero.
It yields ||T_i u||2<=2||zeta_i||2+1, also for u*.
Averaging, rescaling, and splitting into real and imaginary parts gives ||T_i0 p||2<=(4||zeta_i||2+2)||p||.
The actual adjoint identity separately gives ||T_i0* p||2<=(5||zeta_i||2+2)||p||.
Neither the zero-defect selfadjoint estimate nor the curve hypotheses of C_F0043 are substituted here.

For each bounded x, bounded Kaplansky approximants p_alpha converge in L2, while these two estimates bound the corresponding graph outputs.
A weakly convergent subnet lies in the appropriate original closed graph because a closed linear graph is weakly closed.
Doing this for the operator and its actual adjoint puts all M in both original domains with the same estimates.
This is exactly the C_F0027 closed-graph argument, without importing its separate rank-one dual-system conclusion.

On P, the finite sum of the delta_i is i(p tensor 1-1 tensor p).
For a fixed x in M, a joint weak cluster of the finitely many bounded outputs A_i p_alpha belongs to every original graph.
Its sum is forced by the polynomial identity to equal i(x-tau(x)).
Thus sum_i A_i|_M=i(I-P_Omega).
This proves the corrected all-M step without claiming bounded-strong continuity from the infinity-to-L2 estimates.

The generator commutator is i delta_ij Theta(X_i tensor 1-1 tensor X_i).
Original graph-core approximation extends that bounded commutator to Dom A_i and then to M.
Consequently C_F0034 applies to A_i|_M with both dense left M-modules E=V=M.
No all-M domain or norm estimate for the original normalized normal dual E_i is used.

### Algebraic removal and Hilbert uniqueness

If x-lambda is a unit of U for every complex lambda, left and right multiplication by x on U have no nonzero finite-dimensional invariant complex subspace.
An endomorphism of such a subspace would have an eigenvector annihilated by x-lambda.
The same holds on H, which is stable under bounded multiplication.

For a finite tensor in ker(a tensor I-I tensor b), choose a minimal expression with both coefficient families independent.
Projection of the second leg modulo its finite support forces that support to be b-invariant.
This proves injectivity when b has no finite-dimensional invariant subspace, with the symmetric statement available for a.
In the first quotient U/H, the unquotiented second U leg supplies that property; in the second quotient the first H leg supplies it.
Algebraic tensor exactness over C then gives successively T in H tensor U and T in H tensor H.
No spectrum claim about U/H or completed tensor quotient is needed.
The same argument proves B_i injective on U tensor U.

For Hilbert-tensor injectivity, Theta turns a kernel vector into a compact operator commuting with the bounded normal rho(X_i).
Bounded Fuglede gives adjoint commutation, so a nonzero positive eigenvalue of T*T would give a nonzero finite-dimensional reducing subspace for rho(X_i).
That subspace would contain an eigenvector, contradicting regularity of every X_i-lambda.
Normality of B_i gives the same injectivity for B_i*, and both ranges are dense.
The inverse of a bounded injective operator on its range has a closed graph; no bounded inverse or closed range is asserted.

### Actual defects, affiliated derivatives, and all fractions

C_F0034 gives closability of every actual defect on M, and its finite-rank closure is the unique bounded finite-rank extension.
The proof uses M in the actual adjoint domain as its dense adjoint test module.
Its common-multiple identity, finite-rank cancellation, and inverse-closed finite-defect algebra apply with arbitrary bounded fraction coefficients.
This includes rational elements with unbounded intermediate denominators.

For finite defects, eta_i=s^-1 Theta^-1(F_i) t^-1 lies in algebraic U tensor U.
The identity y F_new y'=x F_old x' and regular outside cancellation prove its fraction independence.
For products, the choices a1 s2^-1=x^-1 y and t1^-1 b2=p q^-1 give F_product=x F1 p+y F2 q.
After clearing, its first term is eta_i(u1)u2 because t1 p=b2 q, and its second is u1 eta_i(u2) because x a1=y s2.
The noncommutative orders are preserved.
For units, the inverse pair (a,s,t,b) is valid because a,b are then regular and its defect is -F.
It gives eta_i(u^-1)=-u^-1 eta_i(u)u^-1.
Constants have zero defect.

On the unstarred generators eta_i=i B_i partial_i.
Since B_i commutes with outer U-actions, induction through any rational expression gives that identity for its formal Leibniz/inverse derivative.
Injectivity on algebraic U tensor U makes the formal derivative independent of the expression.
This is the internal construction of partial_i^rat; no localization theorem or integrability premise is added.
For every rational u and every bounded pair, B_i[s partial_i^rat(u) t]=(1/i)Theta^-1(F_i).
The algebraic removal lemma now gives s partial_i^rat(u) t in H tensor_alg H.

### Dense tests and both implications

With the linear-second convention, Gamma_i(p tensor q*)=<p,F_i q> is conjugate-linear in each tensor factor and defines the stated conjugate-linear algebraic tensor functional.
The identity <p,Theta(k)q>=<p tensor q*,k> fixes its tensor convention.
The space Test_i=B_i*(M tensor_alg M) is dense because M tensor_alg M is Hilbert dense, B_i* is bounded, and its range is dense.
Injectivity of B_i* makes R_i(B_i* z)=(1/i)Gamma_i(z) unambiguous for every affiliated u before any finite-rank assumption.

A finite algebraic Hilbert-tensor representer k satisfies <z,B_i k>=(1/i)Gamma_i(z).
Testing all p,q in M therefore gives the actual equality F_i=i Theta(B_i k) on M.
Conversely that equality gives the representer.
Thus finite-rank representability is exactly the specified finite-rank Hilbert-Schmidt deconvolution condition, with a unique K_i.
It is not a freely chosen distributional inverse.

The forward implication follows from the cleared rational tensor just proved and Hilbert uniqueness.
For the reverse, put k_i=Theta^-1(K_i) and z_i=s^-1 k_i t^-1 in algebraic U tensor U.
Using sb=at and the proved all-M sum,
\[
 \sum_i F_i=i(aP_\Omega t-sP_\Omega b).
\]
Transporting by Theta and clearing gives
\[
 \sum_i B_i z_i=u\otimes1-1\otimes u.
\]
In U tensor_F U every B_i term vanishes by balancing over X_i in F.
C_F0035's same-unit division-ring equalizer then gives u in F.
The reverse implication never assigns a rational derivative to an arbitrary u in advance.

Applying the forward statement after the reverse proves existence and finite rank for every pair.
For numerical rank, the common-multiple identity and B_i's commutation with bounded outer multipliers give the same identity for K_i by Hilbert injectivity.
A bounded injective left factor preserves a finite-dimensional range, and a bounded dense-range right factor preserves the rank of a bounded finite-rank operator.
The regular coefficients meet these two different requirements.
No norm lower bound or bounded denominator inverse is needed.

### Original-operator compatibility

On P, A_i0 p=i(rho(X_i)E_i0 p-E_i0(rho(X_i)p)+p) follows directly from the product rule for the normalized canonical contraction.
The normalized operator is essential to the displayed identity.
Its weak Jacobi relation has the stated factor 1/i and applies on polynomial tests without assuming fP lies in the original E_i domain.
Agreement of the commutators does not establish equality of the general original weak form and the finite tensor.
For example, the nonzero form represented by the identity operator commutes with rho(X_i); since H is infinite-dimensional here, that operator is outside the Hilbert-Schmidt kernel statement.
This explains why finite-tensor injectivity cannot discharge a general form-uniqueness obligation.

Under the separately stated stronger assumptions giving original D_i and D_i* their all-M infinity-to-L2 bounds, bounded approximation and weak graph identification extend the displayed identity and its adjoint identity to M.
Then sD_i b-aD_i t is actually defined on M for every bounded pair, and its weak Jacobi calculation gives (9a).
Any Hilbert-Schmidt extension represents that functional and equals the intrinsic K_i by the proved uniqueness.
Normalization cancels by sb=at.
This verifies the conditional recovery of the stronger established finite-rank criterion.

For general correlated normal tuples, the proof establishes neither density of {z:bz,tz in Dom D_i} nor a common graph-core property for it.
It does not prove equality of K_i with the raw composition formula on all such vectors.
The bounded weak companion and literal arbitrary raw-domain compatibility remain separate mathematical assertions.
The present whole-proof conclusion concerns the intrinsic statement actually proved, not either additional assertion or Task-contract completion.

### Accepted dependency and source scope

| Input | Inspected and accepted use | Boundary retained |
| --- | --- | --- |
| [C_F0025](../../claims/Yin_C_F0025_v1.md#yin_c_f0025) | Sections 1--3 and 7: exact original hypotheses, normalization, canonical coarse derivation and vacuum, normal phase, maximal Delta, and unstarred free-field embedding. | The dependency's original weak-form rationality proof is not re-audited here; no original all-M dual domain is inferred. |
| [C_F0027](../../claims/Yin_C_F0027_v1.md#yin_c_f0027) | Section 5's actual closed-graph recovery from two independent core bounds, read with the exact Section 1 hypotheses and Section 6 limits. | Its full bounded-inversion proof and stronger all-M rationality theorem are not needed to obtain liberation domains. |
| [C_F0043](../../claims/Yin_C_F0043_v1.md#yin_c_f0043) | Sections 3.1--3.2: controlled nonzero-defect norm calculation and differentiated analytic-unitary series; Appendix A's entire liberation specialization was checked afresh. | The closed analytic-curve theorem and its reconstruction machinery are not imported as hypotheses or conclusions. |
| [C_F0034 P1](../../claims/Yin_C_F0034_v1.md#yin_c_f0034-p1) and [C_F0031 P1](../../claims/Yin_C_F0031_v1.md#yin_c_f0031-p1) | Complete necessary proofs of closable finite-rank extension, dense-restriction cancellation, common fractions, finite numerical ranks, and algebra/inverse closure. | Only bounded regular coefficients and actual left-module/adjoint-domain conditions are used; no quantitative inverse estimate is imported. |
| [C_F0035 P1](../../claims/Yin_C_F0035_v1.md#yin_c_f0035-p1) | Complete equalizer proof, including right-F basis extension and its correctly sided coordinate functional. | F must be a same-unit division subring; U may have zero divisors and no topology is used. |
| [ACSY24-U001](../literature/ACSY24/Yin_U001_v1.md#acsy24-u001) | Published 73-page edition, Section 3.2 pp.34--36: exact derivation/dual-adjoint interface and maximal-Delta applicability. | Existing statement/proof-reconstruction scope was read; no new whole-primary-source audit, edition comparison, or all-M domain theorem is asserted. |
| [MSY23-U002](../literature/MSY23/Yin_U002_v1.md#msy23-u002) and [MSY23-U004](../literature/MSY23/Yin_U004_v1.md#msy23-u004) | Published 50-page edition, Section 3 pp.12--20 and Section 5.1 pp.28--34: maximal-Delta/full-matrix injectivity interface and same-unit free-field realization in U. | Affiliated invertibility supplies no bounded inverse; MSY23-U004's separate p.36 arbitrary-domain/projection-comparison supplement and bounded scalar descent are unused. General affiliated algebra and free-field foundations retain their recorded proof-inspection limits. |
| [Miy22-U006](../literature/Miy22/Yin_U006_v1.md#miy22-u006) | Published 24-page edition, Section 4 pp.19--20: finite-tracial affiliated algebra, bounded fractions, and regularity interface. | The Fock-space rationality theorem is not transferred to the present tuple; general affiliation/polar-decomposition foundations were retained rather than re-audited. |
| [Dab10-U002](../literature/Dab10/Yin_U002_v1.md#dab10-u002) | Existing identification of Lemmas 10 and 12 and the reality/coassociativity mechanism behind the comparison. | The selfadjoint source theorem and its closed-real functional calculus do not directly prove the liberation estimate; the local controlled-defect and analytic-series argument supplies it. |
| [Hun74-U002](../literature/Hun74/Yin_U002_v1.md#division-ring-bases), [Hun74-U004](../literature/Hun74/Yin_U004_v1.md#algebraic-dual), and [Hun74-U005](../literature/Hun74/Yin_U005_v1.md#balanced-tensor) | IV.2.4 p.183, IV.4.11 p.204, IV.5.1--5.2 pp.208--209: basis extension via the opposite ring, one right-linear coordinate functional, and the balanced universal property. | No finite-dimensionality, commutativity, or continuous functional is assumed; these recorded source interfaces were reused without reopening the book. |
| [AP18-U001](../literature/AP18/Yin_U001_v1.md#ap18-u001) | Retained 338-page author draft, Theorem 2.3.1, printed p.34 / PDF p.40: bounded Kaplansky approximation for a weakly dense star algebra. | Statement and applicability depth only; this review does not re-audit the theorem's proof or original operator-topology foundations. |

Bounded Fuglede, normal spectral calculus, the Hilbert-Schmidt identification, standard Hilbert adjoints, weak compactness, and weak closedness of a closed linear subspace are retained foundational inputs at the interfaces already identified in C_F0025/C_F0027.
Only bounded Fuglede is used, and no assertion about a general unbounded intertwiner is inferred.
The new review checks the consuming hypotheses and the project's own deductions; it is not a recursive audit of every foundational proof.
No external primary-source PDF was newly opened in this review.
No unresolved source-applicability objection affecting the intrinsic conclusion was found within these accepted interfaces.

<a id="old-audit-comparison"></a>
## Comparison with the old audit object

After the independent initial findings, the reviewer compared them with R_F0034's complete retained finding and C_F0063's current and historical decisions.
The old review's useful checks are covered above: actual original liberation domains, algebraic rather than completed quotient supports, formal rational expression independence, dense tests, both implications, numerical ranks, and conditional stronger-domain compatibility.
The old correction for the all-M sum is now independently checked through the joint weak-cluster argument and through its uses in the reverse criterion.
This new review supplied no replacement proof step.

The old report's identified failure of general form uniqueness is retained explicitly in the original-operator compatibility finding.
Its distinction between finite algebraic removal and Hilbert-space injectivity remains necessary.
Its raw-composition domain limitation, lack of a deconvolution inverse norm bound, and separation from Task completion are retained.
There is no explicit numerical experiment or additional counterexample in the old finding requiring reproduction.

R_F0034 reports that an earlier inference from an infinity-to-L2 estimate to bounded-strong continuity was replaced.
The current fixed proof contains the sufficient weak-cluster argument, which this reviewer independently verified.
The earlier scratch text was not included among this review’s inspected inputs, so this comparison does not authenticate its past wording, establish its current availability, or reconstruct a historical correction date.
Likewise, the old report's discussion of the separately authored bounded-graph companion is not proof evidence for the present finding.

The current R_F0034 relationship table labels its corrected whole finding self-reviewed and explains the reviewer's contribution to that correction.
The new finding neither backdates independent coverage nor certifies the old reviewer's initial context isolation.
C_F0063's candidate-0002 and theorem-role decisions remain historical assertions with their actual recorded evidence.
Its decision-finding-owned-review selects the old self-related finding; adoption of the new independent finding is a separate responsibility of the assigning agent.
No old relationship, decision, or date has been changed here.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Whole intrinsic proof](#whole-intrinsic-proof) | independently reviewed |
| [Old audit comparison](#old-audit-comparison) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Whole intrinsic proof](#whole-intrinsic-proof) | [Exact C_F0063 statement](../../claims/Yin_C_F0063_v1.md#statement) | Exact C_F0025 premises, arbitrary affiliated u and bounded fraction pairs, dense-test/HS inverse convention, both implications, all-pair and finite numerical-rank conclusions, and explicit compatibility limits. |
| [Whole intrinsic proof](#whole-intrinsic-proof) | [Complete C_F0063 argument](../../claims/Yin_C_F0063_v1.md#liberation-intrinsic-affiliated-criterion) | Whole Sections 1--5 and Appendix A, including the corrected weak-cluster all-M sum, its complete affected chain, and the conditional stronger-domain compatibility. |
| [Whole intrinsic proof](#whole-intrinsic-proof) | [C_F0025 mathematical interface](../../claims/Yin_C_F0025_v1.md#yin_c_f0025) | Necessary accepted dependency interface only: Sections 1--3 and 7, as delimited above; not a fresh whole-C_F0025 or original-source proof audit. |
| [Whole intrinsic proof](#whole-intrinsic-proof) | [C_F0027 graph interface](../../claims/Yin_C_F0027_v1.md#yin_c_f0027) | Original-closure/adjoint recovery from two core bounds in Section 5, with the Section 1 assumptions and Section 6 limits. |
| [Whole intrinsic proof](#whole-intrinsic-proof) | [C_F0043 controlled-defect interface](../../claims/Yin_C_F0043_v1.md#yin_c_f0043) | Sections 3.1--3.2 norm and analytic-unitary mechanism; the complete new specialization is part of the C_F0063 argument binding. |
| [Whole intrinsic proof](#whole-intrinsic-proof) | [C_F0034 complete P1](../../claims/Yin_C_F0034_v1.md#yin_c_f0034-p1) | Complete necessary common-fraction, closability, finite-rank, algebra and inverse proof, with E=V=M applicability. |
| [Whole intrinsic proof](#whole-intrinsic-proof) | [C_F0031 complete P1](../../claims/Yin_C_F0031_v1.md#yin_c_f0031-p1) | Transitive finite-rank extension and regular-factor cancellation proof, including domain preservation and dense-range requirements. |
| [Whole intrinsic proof](#whole-intrinsic-proof) | [C_F0035 complete P1](../../claims/Yin_C_F0035_v1.md#yin_c_f0035-p1) | Complete same-unit division-subring equalizer and the right-sided basis-functional argument. |
| [Old audit comparison](#old-audit-comparison) | [R_F0034 retained finding](Yin_R_F0034_v1.md#permanent-whole-independent-review-intrinsic-affiliated-criterion) | Entire retained finding, useful checks, correction description, negative/limited inferences, actual current self relationship, and its unestablished earlier isolation; no retrospective certification. |
| [Old audit comparison](#old-audit-comparison) | [C_F0063 current selection](../../claims/Yin_C_F0063_v1.md#decision-finding-owned-review) | Actual selection of R_F0034's corrected self-related finding, compared only after initial mathematical inspection. |
| [Old audit comparison](#old-audit-comparison) | [C_F0063 historical candidate](../../claims/Yin_C_F0063_v1.md#decision-candidate-0002) | Historical proved assertion and original selected dependencies/review scope, retained as history. |
| [Old audit comparison](#old-audit-comparison) | [C_F0063 theorem-role decision](../../claims/Yin_C_F0063_v1.md#decision-theorem-role) | Existing role designation and inherited evidence; no new role or historical independent relationship is inferred. |

## Verification limits and handoff

The retained new evidence is an actually performed isolated whole-proof inspection, adding necessary independent coverage rather than another copy of the theorem or an administrative receipt.
All substantive obligations of the fixed intrinsic statement and argument were inspected, with accepted dependencies used at the exact scopes above.
No substantive mathematical correction or new research run resulted.
There was no new experiment, manuscript/build/layout review, formal verification, full original-literature audit, or Task-completion assessment.
The original raw-domain and bounded weak-companion boundaries remain.
Only this new R material was created; the assigning agent owns any adoption, navigation maintenance, or disposition of older containers.

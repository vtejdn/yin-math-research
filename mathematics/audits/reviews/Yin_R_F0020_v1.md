---
author: Yin
---

# Yin_C_F0032 and Yin_C_F0033: Complete Review of the Extracted Local-Module Lemmas

## Actual review arrangements

The reviewer contributed the preliminary local-window/domain arguments during C_F0029 development and authored C_F0031 in the same extraction batch.
These are substantive antecedents of the reviewed extractions, so both exact lemma findings are self-reviewed.
The original dates, prior independent descriptions, mathematical findings and source-depth limits remain intact; these declarations perform no new mathematical review.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Complete local test-space lemma](#local-test-spaces-finding) | self-reviewed |
| [Complete local normal-commutation lemma](#local-normal-commutation-finding) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Complete local test-space lemma](#local-test-spaces-finding) | [Exact fixed input](../../claims/Yin_C_F0032_v1.md#statement) | Entire C_F0032-P1 statement, projection extraction, support orientation, nonmonotone strong density and local analytic bounds, with its original finite-tracial trust boundary. |
| [Complete local test-space lemma](#local-test-spaces-finding) | [Exact fixed input](../../claims/Yin_C_F0032_v1.md#yin_c_f0032-p1) | Entire C_F0032-P1 statement, projection extraction, support orientation, nonmonotone strong density and local analytic bounds, with its original finite-tracial trust boundary. |
| [Complete local normal-commutation lemma](#local-normal-commutation-finding) | [Exact fixed input](../../claims/Yin_C_F0033_v1.md#statement) | Entire C_F0033-P1 statement, exact C_F0032 invocation, local Jacobi/Liouville/Kaplansky identities and bounded-defect conclusion; no maximal-Delta, fraction or equalizer theorem added. |
| [Complete local normal-commutation lemma](#local-normal-commutation-finding) | [Exact fixed input](../../claims/Yin_C_F0033_v1.md#yin_c_f0033-p1) | Entire C_F0033-P1 statement, exact C_F0032 invocation, local Jacobi/Liouville/Kaplansky identities and bounded-defect conclusion; no maximal-Delta, fraction or equalizer theorem added. |

<a id="local-test-spaces-finding"></a>
### Complete local test-space lemma

Entire C_F0032-P1 statement, projection extraction, support orientation, nonmonotone strong density and local analytic bounds, with its original finite-tracial trust boundary.
The corresponding complete original checking account and its precise limits follow below.

<a id="local-normal-commutation-finding"></a>
### Complete local normal-commutation lemma

Entire C_F0033-P1 statement, exact C_F0032 invocation, local Jacobi/Liouville/Kaplansky identities and bounded-defect conclusion; no maximal-Delta, fraction or equalizer theorem added.
The corresponding complete original checking account and its precise limits follow below.

- Date and reviewer: 2026-09-10; the reviewing agent.
- Target: Local Test Spaces and Normal Commutation on Dense Left Modules, retained in [Yin_C_F0032_v1](../../claims/Yin_C_F0032_v1.md) and [Yin_C_F0033_v1](../../claims/Yin_C_F0033_v1.md).
- Author of the extracted module: another AI agent.
- Reviewed proof versions: [yin_c_f0032-p1](../../claims/Yin_C_F0032_v1.md#yin_c_f0032-p1) and [yin_c_f0033-p1](../../claims/Yin_C_F0033_v1.md#yin_c_f0033-p1), including both complete statements, proofs, dependency declarations, and consumer interfaces.
- Outcome: accepted under the exact stated hypotheses and retained analytic inputs; no mathematical, domain, or dependency-interface correction is required.
- Authorization: the [approved five-lemma batch](../../ledger/Yin_L_F0014_v1.md#authorization) explicitly covers these extractions and their lemma roles.
  Approval and mathematical review remain separate.
  The responsible Claim materials and their selected decisions own their current assessments and any proof-version promotion.

## 1. Review Scope and Prior Contributions

The reviewer read the complete frozen file and independently checked every proof step and the newly stated interfaces.
This was not limited to comparing copied calculations with the original parent proof.
The review specifically checked which assumptions were removed, which conclusions remain available to consumers, and whether extraction provenance had been mistaken for a logical dependency.

The reviewer previously contributed preliminary local-window and domain arguments during the development of Yin_C_F0029, and authored the separate Yin_C_F0031 extraction in the present batch.
The reviewer also performed earlier Yin20 source-audit work.
Those roles are disclosed; this review is not a claim of independent discovery of every underlying mechanism.
The reviewer did not author the present Yin_C_F0032/Yin_C_F0033 extracted file and checked its complete new statements and proof versions separately.

The source Yin_C_F0029 artifact remained unchanged.
Its previous complete review was read as provenance evidence, not treated as automatic certification of these extracted interfaces.
The relevant finite-tracial trust boundary recorded in Miy22-U006 and the batch authorization/version map were also inspected.
No target, source proof, registry, or shared index was edited by this review.

## 2. Yin_C_F0032: Exact Hypotheses and Projection Extraction

Yin_C_F0032 assumes an arbitrary Hilbert-dense left \(M\)-module \(\mathcal E\subseteq L^2(M,\tau)\), which may contain unbounded vectors and need not contain the vacuum.
Its finite family \(Y_j\) consists only of bounded elements.
The proof needs neither normality nor generation by this family.
The optional operators \(D_i\) need only be densely defined and closable on the specified domain \(\mathcal E\).
These are valid removals of assumptions from the original application.

For \(z_n\in\mathcal E\) converging to the vacuum, the cutoff

\[
e_n=1_{[1/2,\infty)}(|z_n|)
\]

is obtained by the bounded left coefficient \(e_n|z_n|^{-1}v_n^*\), where \(z_n=v_n|z_n|\).
The inverse is used only on the displayed spectral support and has norm at most two there.
Multiplication in the affiliated algebra gives the projection \(e_n\); as a bounded-left-multiplier action on \(L^2\), it is a legitimate vector in \(\mathcal E\).
Thus \(Me_n\subseteq\mathcal E\) follows from left-module invariance.
No assertion that \(z_n\) itself is bounded is used.

For \(q_n=1-e_n\), spectral calculus gives

\[
\|z_nq_n\|_2\leq\tfrac12\|q_n\|_2.
\]

Right multiplication by \(q_n\) is contractive on \(L^2\).
The triangle inequality therefore gives the stated estimate \(\tau(1-e_n)\leq4\|z_n-\Omega\|_2^2\).
This proves the required complement-trace convergence without constructing an increasing sequence.

## 3. Yin_C_F0032: Support Direction, Density, and Local Bounds

The support projection in the good-window construction is correctly taken on the left:

\[
p_n=e_n\wedge\bigwedge_j\bigl(1-l(Y_j(1-e_n))\bigr).
\]

It implies \(p_nY_j(1-e_n)=0\), and hence \((Mp_n)Y_j\subseteq Me_n\).
The right support of \(Y_j(1-e_n)\) is bounded by \(1-e_n\).
Polar decomposition equates its left- and right-support traces, while the finite join inequality bounds the trace of the complement of \(p_n\).
This gives exactly the factor \(r+1\) in (32.2).
The argument does not require commuting projections or normal \(Y_j\).

Vanishing complement trace gives strong convergence of both left and right projection actions on \(H\).
The displayed estimates first prove it on \(M\), and the uniform operator bound extends it to all Hilbert vectors.
For each bounded \(a\), the vectors \(ap_n\in Mp_n\) converge to \(a\) in \(L^2\).
Consequently the union of the windows is dense even though it may be neither increasing nor a linear subspace.
That density is sufficient for the later equality of bounded operators.

The restriction of \(D_i\) to \(Me_n\), with operator norm on the domain and Hilbert norm on the codomain, has closed graph.
The space \(Me_n\) is a closed Banach subspace of \(M\).
An operator-norm convergent sequence there also converges in \(H\).
The Hilbert closure of \(D_i\) identifies the limiting output, and it agrees with the original \(D_i\) at the limiting vector because that vector still lies in \(Me_n\subseteq\mathcal E\).
Thus closed graph yields the local estimate in (32.3).
It does not yield or claim a bound uniform in \(n\).

The weak-continuity argument first tests against \(\operatorname{Dom}D_i^*\), whose density follows from closability.
Its local image bound then extends convergence to every Hilbert test vector.
No operator-norm estimate on the adjoint and no invariant submodule inside its domain are needed for this step.

For inputs in a fixed window, the right products \(z_\alpha Y_j\) stay in \(Me_n\), retain a uniform operator-norm bound, and converge in \(L^2\).
The same local argument applies to their dual images.
Bounded right multiplication also preserves weak convergence of \(D_i z_\alpha\).
These facts prove each item in (32.5), as well as the asserted bounds and continuity of their finite sums.
A bounded Hilbert-space operator restricted to a window has these properties because \(\|z\|_2\leq\|z\|\) for the probability trace and it preserves Hilbert-norm convergence.

## 4. Yin_C_F0033: Its Yin_C_F0032 Interface and Local Jacobi Calculation

Yin_C_F0033 adds a bounded normal generating tuple and the dual identities on \(\mathcal E\).
Its invocation of Yin_C_F0032 is exact: the targets are \(Y_j=X_j\), the module is the same dense left module, and closability of all the \(D_i\) is an explicit premise.
The resulting windows supply every dual input, local bound, and bounded-set weak-continuity assertion used for \(K_n\) and \(C_n\).

For \(z\in Mp_n\), both \(z\) and \(X_jz\) remain in the window.
The additional inputs \(zX_i\) and \(X_j(zX_i)\) belong to \(\mathcal E\).
Expanding the dual identity at these two inputs produces

\[
[K_n,X_j]z=(R_jP-PR_j)z.
\]

Traciality gives \([R_j,P]=[X_j,P]\), so adding \(P\) to \(K_n\) cancels the remaining commutator and proves (33.6).
The sign is correct.
Every occurrence of a dual is applied to a vector whose membership in its domain has already been verified.
The calculation never applies a dual to the vacuum and never asserts right invariance of the whole original domain.

## 5. Yin_C_F0033: Normality, Banach Liouville, and the Extension to M

For a fixed window and normal coordinate \(x\), the function in (33.7) is entire in \(B((Mp_n,\|\cdot\|),H)\).
The domain is a Banach space, left multiplication by all of \(M\) preserves it, and norm-convergent exponential series justify the operator-valued holomorphy.
The established commutation with \(x\) extends to its exponentials in that same operator norm.

Normality allows the displayed exponential rewrite (33.8).
Its two exponents are skew-adjoint, so their exponentials are unitary elements of \(M\).
Their left actions preserve both the input operator norm and the output Hilbert norm.
This gives the uniform bound needed by scalar Liouville after composition with each continuous linear functional on the operator Banach space.
Those functionals separate points, so the original Banach-valued function is constant.
Its derivative at zero proves commutation with \(x^*\).
There is no implicit bounded-Hilbert-space extension of \(C_n\) in this argument.

Generation of \(M\) supplies bounded Kaplansky approximants in \(C^*(X)\), and norm approximation by starred polynomials preserves a common operator-norm bound.
For fixed \(z\in Mp_n\), multiplication by these approximants keeps the inputs in the same window and gives the \(L^2\) convergence required by Yin_C_F0032.
Therefore the images under \(C_n\) converge weakly.
On the other side of the intertwining identity, uniformly bounded \(L^2\)-convergent left multipliers act strongly on the fixed Hilbert vector \(C_nz\).
The proof explicitly justifies this by first testing a bounded vector and then using density.
The two limits give \(C_n(az)=aC_nz\) for all \(a\in M\).

Only this local module identity is concluded.
No value \(C_n\Omega\), global map \(C\) on \(\mathcal E\), adjoint-domain estimate for \(C_n\), or right-invariance condition on any adjoint tests is needed.

## 6. Yin_C_F0033: The Cleared-Defect Identity and Its Boundaries

The operators \(T_i\) in (33.4) are explicitly assumed to be bounded finite rank.
The proof of (33.5) uses their boundedness, and the file correctly identifies finite rank as a hypothesis retained for the intended downstream applications.
It does not covertly obtain boundedness from an algebraic finite-rank expression.
There is therefore no missing invocation of Yin_C_F0031.

For \(z\in Mp_n\), the vector \(zX_i\) belongs to \(\mathcal E\), so the given defect formula applies to \(T_i(zX_i)\).
The vectors \(bz,tz\) stay in \(Mp_n\).
Left coefficients commute with bounded right multiplication, giving

\[
\sum_i[R_i,T_i]z
=sK_n(bz)-aK_n(tz).
\]

Replacing \(K_n\) by \(C_n-P\) produces the term \(aPt-sPb\) with the stated sign.
The two local module terms cancel as \((sb-at)C_nz\).
This uses exactly the coefficient hypothesis \(sb=at\); neither denominator regularity nor an affiliated representation is required.

Both sides left after this calculation are bounded operators on \(H\).
Equality on the dense union of the windows proves their global equality.
The specialization \(s=t=1\), \(a=b=f\) gives \(fP-Pf\), confirming the commutator convention.
Nothing in this argument establishes maximal Delta, fraction independence, finite-rank extension, or tensor equalizer descent, and the module does not claim those conclusions.

## 7. Dependency, Consumer, and Version Audit

The direct project-proof dependency is

\[
\text{yin_c_f0032-p1}\ \longrightarrow\ \text{yin_c_f0033-p1}.
\]

Yin_C_F0032 separately lists the finite-tracial affiliated/polar and spectral inputs, Hilbert adjoints and closed graph, projection trace facts, and basic density arguments it uses.
Yin_C_F0033 explicitly adds the exponential, Liouville, normality, and Kaplansky interfaces.
Their hypotheses and applications are verified in the two proofs.
The source-audit reference records the accepted scope of the finite-tracial foundations and does not claim a fresh audit of their original proofs.

References back to Yin_C_F0029 identify the exact extraction origin.
Neither extracted proof invokes its conclusion, so future use of these lemmas in a new Yin_C_F0029 proof creates no reverse logical dependency.
The file identifies its proof versions as candidates and preserves the distinction between original reviewed proofs, new lemma proofs, and future assembled proofs.
The batch authorization permits the organizational changes but does not replace this review.

For a future Yin_C_F0029 consumer, the adjoint-module hypothesis can supply closability of each dual; boundedness of the finite-rank defects must be supplied separately before invoking Yin_C_F0033.
For Yin_C_F0024 and Yin_C_F0030, the domain is \(M\), and the choices \(e_n=p_n=1\) satisfy the complete Yin_C_F0032 window interface.
In each fraction application the consumer must still establish \(sb=at\).
Tensor conversion and division-ring descent remain separate steps after (33.5).
These checks validate the proposed interfaces without rewriting the original proofs or certifying an as-yet-unreviewed full assembly.

The cases of zero windows or zero defect operators cause no difficulty.
The proofs require neither separability nor monotonicity of the projection sequences.
If a target family is empty, its window construction has the usual empty-intersection convention and the associated product conditions are vacuous.

## 8. Verdict and Verification Limits

Both extracted statements and their complete proof versions are accepted at the identified revision.
No required correction was found, and the target file was not edited.
Saved mathematical delimiters were checked for balance, and no invalid control characters were found.

This is a complete internal AI mathematical and proof-interface review.
It is not a new recursive audit of the external analytic foundations, a numerical proof, proof-assistant verification, external human review, a novelty assessment, or an approval to change the selected proof of any parent claim without its assembly review.

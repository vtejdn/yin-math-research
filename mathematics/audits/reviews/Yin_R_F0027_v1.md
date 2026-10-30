---
author: Yin
---

# Independent review: maximal-density Cauchy core transfer

Date/time: 2026-09-16T13:35.
Human record author: Yin.
Reviewer/method: another AI agent, separately organized complete mathematical and source-interface review.

Reviewed Claim: [Yin_C_F0053_v1](../../claims/Yin_C_F0053_v1.md#decision-candidate-0001).
Consumer scope: the original normal polynomial-core domain question.
The reviewed support is:

- [Complete proof](../../claims/Yin_C_F0053_v1.md#maximal-density-cauchy-core-transfer), Sections 1--7
- [TV06-U001 source interface](../literature/TV06/Yin_U001_v1.md#tv06-u001)

**Verdict: pass for all three stated conclusions A, B, and C.**
Finite total Menger curvature together with square-integrable maximal linear density supplies the original scalar domains and quantitative estimate.
Under the exact additional original-core and freeness hypotheses, the original weak-form and full affiliated-fraction criteria follow.
The separate zero-curvature example refutes sufficiency of curvature alone and is correctly shown to fail the vacuum hypothesis.
No implication from an arbitrary vacuum adjoint to the geometric assumptions is established.

## 1. Review arrangement and correspondence

The reviewer did not develop this proof, its positive-weight candidate, its source note, or its counterexample.
The reviewer had worked on different local-density questions in the normal-vacuum domain project and reviewed other results within this coordinated run.
The supplied review context included the user's authorization for the normal-vacuum domain and square-zero projects, existing C_F0044/C_F0045 context, the author's completed exploratory note, the coordinator's requested delicate steps, and the source URL.
It did not include the proof-generation dialogue or a prior independent verdict on this curvature candidate.
This is an independent, non-blind review; the shared context is disclosed rather than represented as a blind review.

The first review recomputed the exploratory note's positive-weight argument and counterexample and checked the exact primary source interface.
After the coordinator assembled the formal A/B/C statement, the reviewer read the complete registered proof and source attachment, and rechecked the expanded vacuum, original-graph, free-product and fraction interfaces.
The formal file makes those interfaces explicit; the present verdict covers them, not merely the shorter exploratory note.

## 2. Fixed dependencies and source acceptance

The actual direct project dependencies for reviewed publication are:

- [Yin_C_F0044_v1](../../claims/Yin_C_F0044_v1.md#decision-candidate-0002): the positive-weight proof mechanism, original scalar graph method, and retained distinction between vacuum data and geometric/truncation bounds.
  Its old uniform-growth theorem is not invoked with an unproved hypothesis.
- [Yin_C_F0045_v1](../../claims/Yin_C_F0045_v1.md#decision-candidate-0002): intrinsic marginal infinity-to-L2 lifting, original nonnormalized graph/adjoint restoration, unchanged closure on restricting to M, and canonical free-product construction.
- [Yin_C_F0025_v1](../../claims/Yin_C_F0025_v1.md#decision-candidate-0002): the exact original normal starred-core framework, canonical marginal identification and forward weak-form rationality implication.
- [Yin_C_F0024_v1](../../claims/Yin_C_F0024_v1.md#decision-candidate-0002): full affiliated-fraction equivalence and original full-domain commutator conclusion after the all-M hypotheses are met.

The reviewer read these conclusions and their needed interfaces at the selected proof versions.
Their existing source inputs and reviewed status are reused at their recorded scopes; this audit does not recursively re-audit the free-field foundations, the original little Grothendieck theorem, or every source underlying C_F0044.
The additional direct external input is TV06-U001, whose complete attached text is included in the support binding above.
The initial registration's empty canonical dependency list should be populated with these four fixed references when this review is published.

### Primary-source statement and inspection method

The selected established source is Tolsa--Verdera, *May the Cauchy transform of a non-trivial finite measure vanish on the support of the measure?*, Annales Academiae Scientiarum Fennicae Mathematica 31 (2006), 479--494, [publisher artifact](https://www.acadsci.fi/mathematica/Vol31/tolsa.pdf).
The relevant locators are the maximal-density/curvature definitions on printed p.480 and Theorem 2 on p.481.
The theorem assumes a finite positive measure, finite curvature, and square-integrable maximal linear density.
Its truncated squared-norm limit, together with limiting density bounded by maximal density, supports the absolute-constant bound (S).
It needs no probability normalization or uniform linear-growth constant.

Inspection methods are distinct.
The author reports successful tool-extracted publisher PDF text at the selected pages, as recorded in the attached source note.
In this independent review the direct publisher-PDF requests timed out, but targeted searches against that same publisher URL returned the complete indexed primary text of printed pp.480--481.
The reviewer checked those definitions, assumptions, theorem conclusion and the consequence (S) in that indexed primary text.
The coordinator reports bibliography verification with its own PDF request timing out.
None of these activities is a rendered-page or visual PDF inspection.
No source bytes were retained or source-file hash verified; the locally inspected artifact above is the source-interface document.
The source's full proof and antecedent rectifiability results were not re-audited.

This is the same established paper previously checked and excluded in Yin_S_F0011 as a route from arbitrary vacuum data to geometric hypotheses.
The present result changes its use by retaining those hypotheses explicitly.
It is not a newly discovered source or a proof of the previously excluded implication.

## 3. Statement A: weighted measures and the quantitative core bound

An atom makes `M_1 mu` infinite at a point of positive measure, so finite G makes the diagonal null.
Compact support makes each starred-polynomial divided difference bounded.
If a polynomial represents zero in L2(mu), its divided difference vanishes for almost every pair, so the integral represents zero by Fubini.
Thus the represented core is well-defined and dense before any adjoint assertion is made.

For a real f of sup norm at most one, the weight `1+f/2` lies between `1/2` and `3/2`.
Its three factors in the nonnegative curvature integral contribute at most `(3/2)^3`.
The maximal-density square contributes two such factors, with the third supplied by the output measure.
This proves `G(lambda_f)<=27G(mu)/8`.
The weighted measure is finite and positive, so it meets every source hypothesis even though its mass need not be one.

Changing the weighted source norm back to L2(mu) contributes the factor two to the squared norm; hence its bound is `(sqrt(27)/2)Q`.
The exact subtraction identity for `C_epsilon(f mu)` and the triangle inequality give `(sqrt(27)+2)Q` for real f.
Scaling and real/imaginary decomposition give `2(sqrt(27)+2)Q||f||_infinity` for complex f.
These steps use a limsup for each fixed f; a common epsilon threshold is neither required nor asserted.

For a fixed polynomial p, the omitted divided-difference integral over `|z-w|<=epsilon` tends to zero: its integrand is bounded and the measure is nonatomic.
Dominated convergence gives convergence in L2(mu) as well.
The identity

\[
E_\epsilon p=pC_\epsilon\mu-C_\epsilon(p\mu)
\]

then gives the coefficient `1+2(sqrt(27)+2)=5+2sqrt(27)` exactly.
This is an intrinsic marginal sup norm estimate, rather than a norm taken in a different reference measure.

## 4. Actual vacuum and the two original closed graphs

Swapping the variables in the bounded truncated double integral gives the factor two and the correct sign in equation (13).
The source limsup bound supplies a weakly convergent subsequence of the Cauchy transforms with limit h and norm at most Q.
Testing against polynomials and using the already proved convergence of their divided differences gives

\[
\int E_0p\,d\mu=2\int p h\,d\mu
=\langle 2\overline h,p\rangle.
\]

Thus `xi=2Jh` is an actual Hilbert-adjoint vacuum vector with norm at most `2Q`.
This implication is directed from the geometric estimate to the vacuum, not conversely.
Polynomial density also makes the vector unique.
Neither a principal-value interpretation nor boundedness of all Cauchy transforms had been assumed independently of the source hypothesis.

Expanding the divided difference of `conjugate(p)q`, using the vacuum identity and exchanging variables proves `E_0* p=p xi-JE_0Jp` against every original core vector q.
This identifies an actual adjoint functional.
It puts the dense polynomial core into the actual adjoint domain and establishes closability before the graph recovery.

Uniformly bounded polynomial approximants to a bounded measurable f have both original operator outputs bounded.
A weak subsequence in the product graph space, with its first coordinate converging strongly, lies in the weakly closed graph of the original closure and in that of the actual adjoint.
This proves their domain inclusions and both norm estimates.
The later identity for bounded f follows because multiplication by xi converges strongly along a bounded almost-everywhere convergent subsequence, while the original operator on the conjugated inputs converges weakly by actual adjoint pairing.
The proof never assumes the original polynomial core is a graph core for the adjoint.

The scalar canonical examples have the stated rank-one unstarred commutator and modulus-one off-diagonal starred phase kernel.
Its Hilbert-Schmidt norm is one because mu is an atomless probability.
Thus the construction supplies the actual compact-core examples required for later use, not just a formal vacuum expression.

## 5. Statement B: exact original free-product and fraction interfaces

The stipulated original tuple retains every C_F0025 assumption and adds freeness of the coordinate algebras and finite G for each marginal.
C_F0025 identifies each normalized marginal with the scalar core just estimated.
The intrinsic estimate is exactly the missing quantitative input in C_F0045.
The latter supplies both original nonnormalized domains on M and the generator identities there.
Its restriction to M contains the original polynomial core and is contained in the original closed operator, so reclosing yields the original closure; this is the needed bridge to full original-domain assertions.

C_F0024 consequently applies to those actual all-M restrictions.
For bounded rational f its bounded finite-rank commutator extends to the original full closed domain.
Pairing against original polynomial adjoint vectors gives the reverse weak-form implication.
C_F0025 supplies the forward implication.
This does not infer graph convergence merely from Hilbert density of a smaller module.

For an arbitrary affiliated u, bounded fractions have coefficients s,a,b,t in M, with s,t regular.
Every operator input `bz,tz` is in M.
Thus all displayed defects are defined and the C_F0024 some/every fraction equivalence and bounded finite-rank extension apply without inserting an affiliated coefficient into an undefined original domain.
The rational algebra is the original unstarred algebra throughout.
This is not the distinct bounded division-closure reconstruction statement.

## 6. Statement C: zero curvature and failure of both proposed analytic conditions

The density `(1-alpha)x^(-alpha)` is a probability for `alpha<1`, is nonatomic, and is supported on a line.
Every triple has zero Menger curvature.
For `p_n=(1-x)^n`, the sup norm is one and the divided difference is nonpositive everywhere off the diagonal.

On `0<x<1/(4n)` and `1/n<y<2/n`, the numerator difference has a positive uniform lower bound for large n and `y-x<2/n`.
The y interval has mass comparable to `n^(alpha-1)`, so the absolute output is at least a constant times `n^alpha` on an x interval of mass comparable to `n^(alpha-1)`.
There is no cancellation because of the global sign.
Squaring and integrating yields the lower bound `n^(3alpha-1)`, which diverges for every asserted `alpha>1/3`.

The same sign gives the vacuum-functional lower bound `n^(2alpha-1)`.
Meanwhile the exponential comparison and scaling give the L2-input upper bound `n^((alpha-1)/2)`.
The quotient diverges as `n^((3alpha-1)/2)`, including the range `1/3<alpha<=1/2`, where the numerator lower bound alone need not diverge.
Therefore the actual vacuum functional is unbounded.
The example excludes curvature-only sufficiency and explicitly fails the vacuum premise; it is not a counterexample to the original normal-vacuum domain implication.

## 7. Verdict and remaining boundary

The complete A/B/C argument and its declared source application have no unresolved mathematical gap at the stated scopes.
The original vacuum identity by itself still gives only convergence of polynomial pairings; it has not been shown to imply finite G or bounded Cauchy truncations.
The proof preserves that boundary and does not settle arbitrary marginal laws, correlated tuples, bounded scalar rational reconstruction, or the full Task.

This review performed internal mathematical checking and independent primary indexed-text inspection at statement/application depth.
It did not perform numerical experiments, rendered-document validation, formal verification, external human review, a whole-source audit, or a novelty assessment.
Only this audit file was written; the proof, source attachment, canonical records, generated indexes, and Task contract were not changed by the reviewer.

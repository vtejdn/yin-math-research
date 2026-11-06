---
author: Yin
---

<a id="no15-u002"></a>
# Elliptic mirror pairs and the arbitrary-shift least-singular-value theorem

This unit owns the precise final-theorem interface of Nguyen and O'Rourke, *The Elliptic Law*, arXiv:1208.5883v4, 9 September 2014.
The [existing edition notes](readme.md) identify the selected 57-page [local original](../../../literature/pdf/NO15--arxiv-v4.pdf).
Definitions 1.3 and 1.6 and Theorems 1.8--1.9 on PDF pp. 2--5 were directly read on 2026-11-05; pp. 4--5 were also rendered and visually checked.
The different 45-page author-hosted layout was consulted during discovery but supplies no substituted edition or claimed whole-edition equivalence.
This is a source-statement and applicability inspection, not an independent review of the original proof.

<a id="pair-model"></a>
## Independent mirror-pair model

Definition 1.3, PDF p. 2, starts with a complex-valued infinite array and a pair \((U,V)\) of centered complex random variables with \(\mathbb E|U|^2=\mathbb E|V|^2=1\).
The diagonal entries and the mirror pairs indexed by unordered off-diagonal positions form one independent family.
Every mirror pair has the same law as \((U,V)\), with the first component in the upper position.
The diagonal entries have one fixed independent identically distributed law with mean zero and finite second moment.
The diagonal clause imposes no real-valued restriction.
No independence between the components of one mirror pair is assumed.

<a id="elliptic-pair"></a>
## The exact covariance definition

Definition 1.6, PDF pp. 3--4, calls \((U,V)\) a \((\mu,\rho)\)-family pair when \(0\le\mu\le1\), \(-1<\rho<1\), the preceding centered unit-variance conditions hold, and
\[
 \mathbb E(\Re U)^2=\mathbb E(\Re V)^2=\mu,
 \qquad
 \mathbb E(\Im U)^2=\mathbb E(\Im V)^2=1-\mu,
\]
\[
 \mathbb E\Re U\Re V=\mu\rho,
 \qquad
 \mathbb E\Im U\Im V=-(1-\mu)\rho,
 \qquad
 \mathbb E\Re U_i\Im U_j=0\quad(i,j\in\{1,2\}),
 \tag{EC}
\]
where \(U_1=U\) and \(U_2=V\).
The real and imaginary parts need not be independent, as Remark 1.7 explicitly states.
The endpoint values \(\mu=0,1\) are included, whereas \(\rho=\pm1\) are excluded.
The scalar condition \(|\mathbb EUV|<1\) alone does not replace this full covariance pattern.
There is no density condition or moment requirement above order two in these definitions or the final theorem below.

<a id="least-value-theorem"></a>
## Theorem 1.9: uniform polynomial lower tail

Let \(X_N\) be the raw, unnormalized \(N\)-by-\(N\) matrix from the preceding pair model with one fixed \((\mu,\rho)\)-family law and one fixed permitted diagonal law.
Theorem 1.9, PDF p. 5, states that for every \(b,\alpha>0\) there are \(A,N_0>0\), depending on \(b,\alpha,\mu,\rho\) and those fixed entry laws, such that
\[
 \mathbb P\{s_{\min}(X_N+F_N)\le N^{-A}\}\le N^{-b}
 \qquad(N>N_0)
 \tag{NO-floor}
\]
for a deterministic complex shift whose entries satisfy \(\max_{r,s}|(F_N)_{rs}|\le N^\alpha\).
The displayed parameter dependence is independent of the selected shift, so the inequality is uniform over that set of shifts.
The theorem does not require the shift to be Hermitian, real, symmetric, low-rank, or bounded in normalized Hilbert--Schmidt norm.
The latter two restrictions belong to the separate limiting-law conclusion in Theorem 1.8, not to the shift hypothesis stated in Theorem 1.9.
The proof source expressly separates its least-value theorem, treated in Sections 2--6, from the limiting-law assembly in Section 7.

<a id="marginal-conditional-use"></a>
## Direct marginal and conditional interpretation

The infinite array in Definition 1.3 does not restrict this one-dimension inequality to a particular coupling across dimensions.
Any size-\(N\) matrix with the prescribed pair law can be completed to an infinite array by adjoining independent entries with the same laws.
Its size-\(N\) marginal is unchanged, and (NO-floor) therefore applies under every coupling preserving those marginals.
Consequently summable choices of the right side allow first Borel--Cantelli under arbitrary cross-size coupling.
This reasoning uses the marginal estimate, not Theorem 1.8's almost-sure conclusion for its nested-array formulation.

For a random shift \(F_N\) independent of \(X_N\), condition on the shift and use the same constants on its polynomial entry guard.
Integrating gives
\[
 \mathbb P\{s_{\min}(X_N+F_N)\le N^{-A}\}
 \le N^{-b}+\mathbb P\{\max_{r,s}|(F_N)_{rs}|>N^\alpha\}.
\]
These are direct conditioning and normalization interpretations of the source assertion; they introduce no dimension-dependent entry law or uniformity over a changing family of laws.
For normalized matrices \(\kappa X_N/\sqrt N\), every singular value gains the factor \(|\kappa|/\sqrt N\), with fixed \(\kappa\ne0\).
The consuming argument must verify its actual pair covariance, diagonal law, independence and shift guard before applying this interface.

<a id="source-proof-boundary"></a>
## Related internal-source issues and the precise acceptance boundary

The [separate U001](Yin_U001.md#inspection-and-current-use) retains concrete contradictions to the literal integer-generator statement in Theorem 3.1 and the small-precision denominator wording in Corollary 3.4.
Those are not counterexamples to the final least-singular-value assertion (NO-floor).
They also cannot be silently described as irrelevant to a full audit of its proof.
The [inspected Section 5 application on PDF p. 17](Yin_U001.md#coordinate-passages) uses Corollary 3.3 inside that source proof chain; the same retained record explains the source's two-real-coordinate application and appendix passages.
No complete corrected arithmetic statement, precision audit, or verification of the whole resulting least-value proof is supplied here.

This unit verifies the final Theorem 1.9 statement and its precise intended applicability as an external theorem input.
The [local replacement theorem](../../../claims/Yin_C_F0194_v10.md#statement) now supplies (NO-floor) through its [complete argument](../../../claims/Yin_C_F0194_v10.md#argument) and [independent whole-proof finding](../../reviews/Yin_R_F0200_v10.md#elliptic-floor-whole-proof).
This resolves the reported source-use obstacles for that precise floor without accepting the source's false internal assertions or declaring its original proof independently checked.
The [retained conditional additive version](../../../claims/Yin_C_F0186_v13.md#inputs) explicitly assumed the final external interface with its original source-proof qualification and open assessment; that historical adoption is not rewritten by the later local replacement.
The local deduction does not invoke the disputed arithmetic clauses as additional proved lemmas.
Any assessment requiring resolution of that internal-source issue must inspect or otherwise justify the affected source steps; it cannot infer either a verified repair or a refutation of Theorem 1.9 from this unit.

<a id="affected-source-steps"></a>
## Affected source steps and the remaining profile count

A subsequent scoped inspection followed the relevant applications in Sections 4--6, PDF pp. 13--25, and the two-coordinate Appendix A passages on pp. 49--52; the profile pages 23--24 were also visually checked.
This was not a complete review of the paper or every cited input.
Section 5, PDF p. 17, invokes Corollary 3.3 to obtain an approximating vector together with a rationally describable progression.
Section 6 uses the finite choice of such progressions in (22), PDF p. 19, and again in the profile count (32), PDF pp. 24--25.
The coordinate and precision questions therefore affect actual finite-family counting, rather than only unused wording.

For the normalized nondegenerate complex vector on p. 17, the accepted [TV08 finite-net interface](../TV08/Yin_U001.md#inverse-net) can supply a deterministic infinity-norm net after its fixed-law controlled-moment and phase hypotheses have been matched.
Writing m=n-1, concentration lower bound p>=n^(-D), and a fixed admissible tau>0, its cardinality has the form
\[
 m^{(-1/2+\tau)m}p^{-m}+\exp(o(m))=n^{O_{D,\tau}(n)}.
\]
Its leading exponent is independent of the polynomial precision exponent, within that theorem's stated radius range.
An infinity-norm approximation error delta changes any row or column inner product by at most n max|M_ij| delta.
Thus the theorem can provide finite approximation and an initial finite family in this local application.
It does not provide a progression with rationally controlled generators merely by providing that net.

The later required simultaneous bounds have the source's concentration levels l_k and their block multiplicities m_k:
\[
 |\mathcal B'_{k_0,\mathbf m}|
 \le n^{-(1/2-\epsilon-o(1))n}\prod_k l_k^{-m_k},
 \qquad
 P_{\mathrm{expanded\ radius}}(u')
 \le n^{2\epsilon n}\prod_k l_k^{m_k}.
\]
These are the uses of (32) and (28)--(31), respectively, not estimates established afresh by the present inspection.
The source obtains their cancellation by counting polynomially many progressions, assigning each block a progression of size O(l_k^(-1)n^(-1/2+epsilon)), and separating exceptional coordinates.
A replacement by TV08 nets still has to establish compatible joint profile counting and the corresponding concentration-product estimate.
In particular it must handle block normalization, small-norm or short blocks, exceptional coordinates, the additive exp(o(m)) net term, and the choice of representatives with the required enlarged-radius probability bound.
The single-net statement alone does not discharge these obligations.
Those original source bounds are not established by this scoped source inspection.
The [corrected two-marginal profile construction](../../../claims/Yin_C_F0194_v10.md#the-two-marginal-joint-profile-count) supplies a compatible joint count and probability bound as part of the separately reviewed local replacement, rather than treating the single-net theorem as either original source estimate.

<a id="mixing-constant-correction"></a>
## The local precision correction does not settle the mixed theorem

Section 4, PDF pp. 14--16, uses the geometric conclusion cited through Corollary 3.4: bounded progression rank, polynomial-sized integer boxes and resulting bounded integer relations.
It passes through Lemmas 4.5 and 4.7 and a determinant calculation; this use does not require a rational-coordinate bound on the mixing constants or progression generators.
Conditional on Theorem 3.2's geometric conclusion, one can keep the original mixing constants and invert their two linear relations instead of applying the printed rational-rounding sentence.
The resulting sum of four scaled progressions retains bounded rank and a polynomial-sized integer box, whether or not that displayed parametrization is proper.
This observation removes the incorrect O(beta) denominator assertion from that particular geometric step, not from every later counting step.

For completeness, the relevant elementary rounding statement is as follows.
Suppose c_0<=|c_1|,|c_2|,|c'_1|,|c'_2|<=C_0 and |c_1/c_2-c'_1/c'_2|>=alpha>0, with fixed positive constants.
Then
\[
 |\Delta|:=|c_1c'_2-c'_1c_2|\ge c_0^2\alpha.
\]
For sufficiently small beta>0, choose a positive integer q=ceil(K/beta), with fixed sufficiently large K, and round each real and imaginary component of those four constants to q^(-1) times an integer.
Each component changes by at most 1/(2q)=O(beta); q and every numerator are O(beta^(-1)).
The determinant changes by O(beta), so its modulus stays at least c_0^2 alpha/2 after decreasing the permitted beta range.
The rounded coefficients remain uniformly bounded and their inverse two-by-two matrix has uniformly bounded norm.
If |a_i|,|b_i|<=1 and both original mixtures are beta-close to points of Q, the rounded mixtures are O(beta)-close to the same points.
Solving the rounded two-by-two system shows that a_i and b_i are O(beta)-close to the respective sums of two scaled copies of Q.
This proves the local inverse-precision correction conditional on the mixed theorem's geometric output.
It verifies neither that mixed theorem nor the later finite-profile entropy bound.

<a id="bounded-correction-search"></a>
## Scope of the alternative-source check

The retained [Nguyen--Vu erratum](../../../literature/pdf/NV11--erratum.pdf), pp. 1--2, was checked for its real-scalar vector-coefficient conclusion and coordinate formula g_ij=beta p_ij/p.
It supplies evidence for the two-real-coordinate convention under its printed anti-concentration hypothesis, including its probability threshold of one half.
It does not itself verify the arbitrary complex-scalar or correlated mixed-scalar extensions used in NO15.
A bounded check of the [arXiv version record](https://arxiv.org/abs/1208.5883) still found v4, and the [author's publication page](https://people.math.osu.edu/nguyen.1261/cikk-teljes.html) linked the Nguyen--Vu inverse-theorem erratum.
No NO15-specific correction was identified in those inspected locations; this is not an absence claim about other literature.
The displayed bound in [CO22 arXiv v3, Theorem 5.1](https://arxiv.org/html/2010.01261v3#S5.Thmtheorem1) was checked as an alternative least-value input.
It contains an n^(-1/2) term before an outer one-fourth power, which cannot be removed merely by decreasing the least-value threshold.
That displayed estimate alone therefore does not supply an arbitrarily prescribed n^(-B) exceptional probability.
Its complete original proof was not reviewed.

A further bounded primary-source search on 2026-11-05 UTC targeted the exact work title with erratum/correction terms, finite-second-moment elliptic least-value bounds, and complex or mixed inverse Littlewood--Offord statements.
The arXiv record still listed v4; the two authors' [Nguyen](https://people.math.osu.edu/nguyen.1261/cikk-teljes.html) and [O'Rourke](https://math.colorado.edu/~seor3821/research/) publication pages supplied no identified NO15-specific correction.
The published NO15 DOI endpoint, 10.1093/imrn/rnu174, could not be opened through the available web reader after its publisher redirect, so no comparison of the 70-page journal edition is claimed.
This bounded result establishes neither that no correction exists elsewhere nor that the journal edition repeats the inspected defects.

Theorem 1.1 on printed/PDF p. 2 of the 27-page [Götze--Naumov--Tikhomirov arXiv:1309.5711v1](https://arxiv.org/pdf/1309.5711v1) was read together with its real-entry conditions (C0) on p. 1 and uniform-integrability condition (UI) on p. 2.
It asserts the existence of positive constants \(A,B,C\) giving \(\mathbb P\{s_n(X+M_n)\le n^{-B}\}\le Cn^{-A}\) for polynomially norm-bounded deterministic shifts.
The statement provides neither complex mirror-pair laws with general \(\mu\) nor a prescribed arbitrary exceptional exponent; it does not replace (NO-floor) at the required scope.

[Carpenter--O'Rourke arXiv:2508.04891v1](https://arxiv.org/html/2508.04891v1), Section 4, Theorem 4.1, was inspected for a later complex elliptic alternative.
Its displayed bound retains the same \(n^{-1/2}\) term inside an outer fourth root as the CO22 estimate above, and Proposition 4.2 concludes only an \(o(1)\) least-value failure probability.
These statements therefore do not provide the arbitrary exceptional exponent either.

Theorem 5.2 and Corollary 5.3 on printed/PDF pp. 15--16 of [Nguyen--O'Rourke, *On the concentration of random multilinear forms and the universality of random block matrices*, arXiv:1309.4815v4](https://arxiv.org/pdf/1309.4815v4), 15 May 2014, were inspected as a different mixed-geometric lead.
Their assumption (4.1), p. 13, includes finite \(2+\eta\) moments for some \(\eta>0\) and identity Hermitian covariance of the atom vector.
Theorem 5.2 supplies a bounded invertible mixing matrix and a proper progression for its mixed coefficients; it is not stated under only finite second moments.
Its proof is omitted in favor of Appendix A's related argument on pp. 40--42, whose final geometric step invokes Nguyen--Vu's 2011 result [26], rather than NO15 [24].
No complete extension of that argument to the present finite-second-moment law was verified in this check.
The three alternative papers' full proofs were not audited, and no adequate replacement for the whole least-value input was identified in these bounded comparisons.

<a id="separation-obstruction"></a>
## The separation claim fails even for an actual symmetrized pair

Claim A.2 on PDF p. 46 requires two positive-probability sets of pairs with both coordinates bounded away from zero and with their coordinate ratios uniformly separated.
Appendix A, PDF p. 48, applies this claim to the symmetrized pair in its double-counting step.
PDF pp. 46 and 48 were read as text and visually checked.
The surrounding pp. 45, 47 and 49--50 were read as text; no complete Appendix A proof audit was performed.
The asserted separation does not follow from the printed covariance hypotheses.

A direct counterexample to Claim A.2 is the real pair uniformly distributed on
\[
 (\sqrt2,0),\quad(-\sqrt2,0),\quad(0,\sqrt2),\quad(0,-\sqrt2).
\]
It is centered, each coordinate has variance one, and its covariance is zero, so it is a \((1,0)\)-family.
It never has both coordinates nonzero, so neither required positive-probability set exists.

The following example also rules out using the separation claim merely because the pair is a symmetrized difference.
Let \((A,B)\) be uniform on \(\{(0,0),(1,0),(0,1)\}\), and put
\[
 U=(3A-1)/\sqrt2,\qquad V=(3B-1)/\sqrt2.
\]
Here \(\mathbb EU=\mathbb EV=0\), \(\mathbb EU^2=\mathbb EV^2=1\), and \(\mathbb EUV=-1/2\), so the pair belongs to the allowed \((1,-1/2)\)-family.
For an independent copy \((U',V')\), its correctly unit-variance-normalized difference
\[
 D=\bigl((U-U')/\sqrt2,(V-V')/\sqrt2\bigr)
\]
has the same covariance parameters and support
\[
 (0,0),\qquad \pm(3/2,0),\qquad\pm(0,3/2),\qquad\pm(3/2,-3/2).
\]
The zero vector has probability \(1/3\), and each of the six other vectors has probability \(1/9\).
Whenever both coordinates are nonzero their ratio equals \(-1\).
Thus no two positive-probability regions can have the separated ratios demanded by Claim A.2, including at the actual symmetrized-law use.
Multiplying the difference by another nonzero common scalar cannot change this failure.

This is an explicit counterexample to the internal separation assertion, not to Theorem 3.2's full geometric conclusion, Theorem 1.9, or the additive Brown candidate's conditional deduction.
The later Fourier use may admit a replacement based on two linearly independent support directions and bounded integer combinations, without requiring those combinations to remain support points.
The [local mixed Fourier reduction](../../../claims/Yin_C_F0194_v10.md#a-mixed-geometric-inverse-statement-from-a-real-scalar-theorem) instead permits zero individual components, selects two support directions with a bounded nonzero determinant, and uses a real compound-Poisson scalar to obtain the required geometry.
Its [integer-row relations](../../../claims/Yin_C_F0194_v10.md#recovering-the-bounded-integer-row-relations), proper coordinate models and remaining floor assembly have their own independent checking in the local proof.
The false separation claim is not accepted merely because the final theorem is published.
The finite-net counting issue and this separation issue are distinct affected interfaces.

<a id="arithmetic-free-decoupling"></a>
## The arithmetic-free bilinear decoupling input

Lemma 4.3, PDF p. 13, concerns a bilinear form \(\sum_{i,j}a_{ij}X_iY_j\), with arbitrary deterministic linear terms, of independent copies of a mirror pair.
For a deterministic cut \(J\sqcup J^c\), let \(A_J\) retain only the two off-diagonal cut blocks of \(A=(a_{ij})\).
If the original form has concentration \(\gamma\ge n^{-B}\) at radius \(\beta\), its stated conclusion is
\[
 P\left\{\left|\sum_{i,j}(A_J)_{ij}(X_i-X_i')(Y_j-Y_j')\right|
       \le C_B\beta\sqrt{\log n}\right\}\ge c\gamma^4,
\]
where the primed pairs are independent copies and the two components of each difference pair can remain dependent.
Only a lower bound by a constant multiple of \(\gamma^4\) is used; no equality of probabilities is inferred from the source's asymptotic notation.

The statement on p. 13 and the complete relevant Appendix B argument on PDF pp. 53--55 were directly read during the scoped correction check.
PDF p. 54 was rendered and checked visually.
The argument bounds Gaussian smoothing by successive Cauchy--Schwarz inequalities across the two independent index blocks and subtracts independent copies, eliminating the linear terms and same-side bilinear terms.
The resulting smoothed lower bound gives the displayed radius after a Gaussian tail estimate.
Universal Fourier-normalization factors are absorbed into the constants in this formulation.
This input uses no progression, rational generator, properization or separation assertion from Appendix A.
Inspection of this argument does not verify the rest of the least-value proof or its geometric and counting steps.

---
author: Yin
---

# Actual normal vacuum implies scalar core bounds and the full free-normal affiliated criterion

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Soft Cauchy Vacuum Estimates and the Free-Normal Affiliated Criterion

<a id="statement"></a>
<a id="soft-cauchy-vacuum-free-normal-criterion"></a>

Date: 2026-09-29.
Human record author: Yin.
Proof developed by the research agent another AI agent, with root contributing the smooth-kernel testing and positive-weight discussion.
Consumer: [T_F0001 current contract](../tasks/Yin_T_F0001_v2.md).
This is an ordinary Claim proof.
The canonical Claim record owns the mathematical and review assessment.
General correlated tuples remain open.
## 1. Candidate conclusion and exact premises

Let mu be a compactly supported nonatomic Borel probability on C.
Put H=L2(mu), with inner product linear in the second variable, and let P=C[z,bar z] be the represented starred polynomial algebra.
Define

    E0 p(z) = integral (p(z)-p(w))/(z-w) dmu(w).

The diagonal is null.
Polynomial divided differences are bounded on the compact support.
Assume the **actual** vacuum adjoint exists:

    integral E0 p dmu = integral conjugate(xi) p dmu,   p in P,
    xi in L2(mu).                                                   (1)

The candidate conclusion is

    ||E0 p||2 <= (5+2 sqrt(27)) ||xi||2 ||p||infinity,               (2)
    E0* p = p xi - J E0 J p,      Jp=conjugate(p).                  (3)

Consequently E0 is closable and its original Hilbert closure E and its actual adjoint satisfy

    L-infinity(mu) subset Dom E intersect Dom E0*.                  (4)

The bounds in (2) and (3) extend to these actual bounded-function domains.
No uniform linear-growth, maximal-density, curvature, principal-value, freeness, or Hilbert-space boundedness assumption occurs in the scalar statement.

Under C_F0025, the restriction of the normalized original dual to each coordinate algebra has precisely (1), so this would remove the extra marginal estimate in the already reviewed free-product lifting C_F0045.
The entire arbitrary free-normal-tuple affiliated criterion follows by that existing result.
A mixed-word estimate for correlated tuples remains a separate obligation.

## 2. Reuse and source boundary

Read before this calculation: C_F0025 (normal phase and canonical scalar operator), C_F0027 (two core bounds restore actual domains), C_F0044 and C_F0053 (positive-weight Cauchy mechanism and exact vacuum-to-truncation gap), C_F0054 (absolute-phase failure), the reference-dual comparison, ACSY24-U001, Dab10-U002, and the current method index.
The latter contains two entries for unrelated finite-classification/shared-structure applications and gives no applicable scalar Cauchy estimate.

The established C_F0053 proof is reused only after the new soft-kernel inequality below: positive weights, dominated convergence of divided differences, and weakly closed original graphs.
Its geometric assumptions are not imported or claimed to follow from a distributional pairing alone.

Targeted external searches on 2026-09-29 considered Cauchy transforms, distributional L2 fields, symmetrization, curvature and reflectionless measures.
A primary result located was Melnikov--Poltoratski--Volberg, *Uniqueness theorems for Cauchy integrals*, arXiv:0704.0621, whose abstract and surfaced introduction distinguish principal-value vanishing from integrability of the Cauchy maximal function.
That result is a related lead, not an input here; the paper's proof was not read.
No source found in this bounded search was verified to supply (2) under precisely (1).
No novelty, priority or global absence-of-literature claim is made.
The calculation below is self-contained; no exact attribution of the mixed comparison (11) was established by this search.

The recognized regularization and approximation steps received targeted source checks:

- The existing [VV16-U001](../audits/literature/VV16/Yin_U001.md) already accepts A. Yu. Veretennikov and E. V. Veretennikova, *On partial derivatives of multivariate Bernstein polynomials*, Theorems 3 and 4(1), at statement/applicability depth.
  That complete local audit was read in this continuation.
  Its exact rectangle interface with d=2 and m=1 is the accepted approximation input for Section 3; the original source proof was not previously audited and no new full audit is claimed here.
- Laura Prat, *Potential Theory of Signed Riesz Kernels: Capacity and Hausdorff Measure*, IMRN 2004, no. 19, 937--981, Section 2, printed p.941, equation (2.5), in the [45-page institutional PDF](https://diposit.ub.edu/server/api/core/bitstreams/d287057d-7d0d-4d48-8d8b-228a39cddfcb/content).
  The displayed vector kernel is (x-y)/(|x-y|^2+phi(x)phi(y)).
  Taking phi identically sqrt(t), and conjugating the complex encoding of that real two-vector, gives (6).
  The source credits the suppression construction to Nazarov--Treil--Volberg.
  This is verified attribution for the kernel, not invocation of its T(b) theorem.
  The selected definition, surrounding scope and bibliography were read; the article's full proof was not audited.
- Adrian Fellhauer, *Approximation of smooth functions using Bernstein polynomials in multiple variables*, [arXiv:1609.01940v1](https://arxiv.org/pdf/1609.01940), Theorem 6.7, printed p.14, gives uniform approximation with prescribed derivatives on the cube.
  Its statement and proof were read, with the preceding factorization/boundedness interfaces retained as standard Bernstein foundations.
  Apply in two real variables to the smooth functions actually used in Section 5, real and imaginary parts separately, and rescale the square.
  This supplies source attribution for the standard C1 approximation explained in Section 3 as an additional checked source; the existing VV16-U001 is the selected dependency.
  No global rational-coefficient approximation theorem is needed.
  No full-paper audit is claimed.

## 3. The actual vacuum identity extends to smooth scalar tests

For a C1 function g on a square containing the support in its interior, the kernel (g(z)-g(w))/(z-w) is bounded by its real Lipschitz constant.
Choose real bivariate polynomials p_n with p_n -> g and their first real derivatives converging uniformly on that square.
Their complex linear combinations are precisely starred polynomials in z,bar z.
This is the accepted VV16-U001 rectangle interface.
The standard C1 polynomial approximation can be obtained directly from tensor-product Bernstein polynomials: differentiating the Bernstein sum replaces its coefficient by the corresponding first finite difference; the integral formula for that finite difference and uniform continuity of the first derivative give uniform convergence of both first derivatives.
Apply to real and imaginary parts separately and rescale the square.

The divided differences of p_n-g tend uniformly to zero off the diagonal.
Therefore both sides of (1) converge, giving the legitimate smooth-test identity

    integral integral (g(z)-g(w))/(z-w) dmu(w)dmu(z)
      = integral conjugate(xi(z)) g(z) dmu(z).                    (5)

This is stronger than merely applying uniform boundedness to a dense noncomplete test space: each fixed smooth test is approximated in the first-derivative norm, which directly controls its defining double integral.
No uniform approximation of the original E0 graph is presumed.

## 4. Soft kernels and exact positive three-point formulas

For t>0 and any finite positive measure nu define

    k_t(a)=conjugate(a)/(|a|^2+t),
    C_t nu(z)=integral k_t(z-w) dnu(w).                            (6)

For fixed t, k_t is bounded and smooth with bounded derivatives.
In particular C_t mu and its conjugate are C1 on a neighborhood of the support, so (5) applies to g=conjugate(C_t mu).

Take three distinct points z,w,v and write

    x=|z-v|^2, y=|w-v|^2, r=|z-w|^2,
    A=x+t, B=y+t, R=r+t,
    H=2xy+2yr+2rx-x^2-y^2-r^2.                                  (7)

Here H=16 times the squared triangle area, hence H>=0, including collinear triples.
Let S_t be the sum of the three real products with each point once serving as anchor:

    S_t = Re[k_t(z-w) conjugate(k_t(z-v))]
        + Re[k_t(w-z) conjugate(k_t(w-v))]
        + Re[k_t(v-z) conjugate(k_t(v-w))].                       (8)

Writing a=z-v and b=w-v, elementary dot-product expansion gives

    S_t = [H+t(x+y+r)]/(2ABR) >= 0.                              (9)

Next let Q_t be the sum over the three choices of omitted point of

    Re{ [(z-v)/A - (w-v)/B]/(z-w) }.

Thus one of the three terms has omitted point v; the other two are its cyclic permutations.
Direct expansion gives

    Q_t = [H+(t/2)(x+y+r)+(tH/2)(1/x+1/y+1/r)+3t^2]/(ABR).       (10)

For an explicit algebra check, its term with omitted v is

    [t+(x+y)/2-(x-y)^2/(2r)]/(AB).

Put over ABR, sum the cyclic expressions, and use the exact identity

    (x-y)^2/r+(y-r)^2/x+(r-x)^2/y
       = 3(x+y+r)-H(1/x+1/y+1/r).

Equations (9)-(10) prove the pointwise inequality

    Q_t-S_t = [H/2+(tH/2)(1/x+1/y+1/r)+3t^2]/(ABR) >= 0.        (11)

Although the displayed expression uses inverse side lengths, all mixed difference kernels before symmetrization are bounded for fixed t by the Lipschitz norm of conjugate(k_t).
The identities and all integrals below are therefore legitimate.
Since mu has no atoms, the collision diagonals have zero mu^3 measure and require no interpretation.

## 5. Vacuum control of all soft Cauchy transforms

By Fubini, permutation invariance of mu^3 and (8),

    ||C_t mu||2^2 = (1/3) integral S_t dmu^3.                     (12)

The real part of the left side of (5) at g=conjugate(C_t mu) is

    (1/3) integral Q_t dmu^3.                                    (13)

Consequently (11), (5) and Cauchy--Schwarz imply

    ||C_t mu||2^2
      <= Re integral conjugate(xi) conjugate(C_t mu) dmu
      <= ||xi||2 ||C_t mu||2.

Thus, for every t>0,

    ||C_t mu||2 <= ||xi||2.                                      (14)

This directly closes the former distributional-vacuum-to-regularization gap for the soft kernel (6).
It does not infer a hard-truncation bound or a principal-value theorem.
Neither of these is required below.

As a byproduct, (9), (12), (14) and Fatou imply

    integral H/(xyr) dmu^3 <= 6 ||xi||2^2.

The integrand is squared Menger curvature.
This byproduct alone is not used to recover a density condition or to prove (2).

## 6. Positive weights give the scalar core bound

For real measurable f with ||f||infinity<=1, let

    dnu=(1+f/2)dmu.

Thus mu/2<=nu<=3mu/2.
Formula (12) holds with nu replacing mu.
The same pointwise kernel S_t remains nonnegative by (9).
Therefore

    ||C_t nu||2,L2(nu)^2 <= (27/8)||C_t mu||2,L2(mu)^2,
    ||C_t nu||2,L2(mu) <= (sqrt(27)/2)||xi||2.                    (15)

The second inequality also uses mu<=2nu.
Since

    C_t(f mu)=2(C_t nu-C_t mu),

(14)-(15) imply

    ||C_t(f mu)||2 <= (sqrt(27)+2)||xi||2

for real f of norm at most one.
Splitting a complex f into real and imaginary parts and scaling gives

    ||C_t(f mu)||2
       <= 2(sqrt(27)+2)||xi||2 ||f||infinity.                    (16)

This estimate is uniform in t and valid for all bounded measurable f; there is no assumed vacuum identity for the weighted measure.

For p in P put

    E_t p = p C_t mu-C_t(p mu)
          = integral [(p(z)-p(w))/(z-w)]
                     [|z-w|^2/(|z-w|^2+t)] dmu(w).              (17)

The original polynomial divided difference is bounded.
Nonatomicity and dominated convergence first in w and then in z imply E_t p->E0 p in L2(mu).
Applying (14) and (16) to (17) gives exactly (2).

## 7. Actual adjoints and original graph restoration

Expanding the divided difference of conjugate(p)q in the actual vacuum identity (1), and exchanging the two variables in its second term, gives

    <p,E0 q> = <p xi-J E0 J p,q>,       p,q in P.

All polynomial kernels are bounded, so this is an actual adjoint calculation: P subset Dom E0*, and (3) holds.
Since P is dense, E0 is closable.
Together (2)-(3) give

    ||E0* p||2 <= (6+2 sqrt(27))||xi||2 ||p||infinity.             (18)

For bounded measurable f choose starred polynomials p_n converging to f in L2 with uniform sup norm at most ||f||infinity+epsilon.
This follows from bounded continuous approximation for a compact Borel probability, then uniform Stone--Weierstrass approximation; equivalently from the commutative Kaplansky argument already used in C_F0053.

The pairs (p_n,E0 p_n) and (p_n,E0* p_n) are bounded in H direct-sum H.
Weakly convergent subsequences have first coordinate f.
The graph of the original Hilbert closure E, and the graph of the actual closed E0*, are weakly closed linear subspaces.
Their weak limits therefore put f in both original domains and give the asserted bounds, then epsilon tends to zero.
This establishes (4); no arbitrary extension has been chosen.

To extend (3), pass to an almost-everywhere convergent subsequence of the bounded p_n; then p_n xi->f xi in L2.
Their E-images converge weakly to the unique original E f by dense adjoint tests and the uniform estimate.
The same applies to Jp_n.
Closedness of the adjoint graph then gives

    E0* f=f xi-J E J f,        f in L-infinity(mu).

## 8. Exact remaining T_F0001 boundary

This candidate supplies the formerly missing arbitrary-scalar-marginal bound under the actual C_F0025 vacuum.
Via C_F0045 it would give the original all-M domains and complete affiliated rationality criterion for freely independent normal coordinates without geometric restrictions on their marginals.

The T_F0001 v2 contract permits correlated normal coordinates.
The positive three-point kernel above belongs to a single abelian coordinate algebra and does not by itself control arbitrary mixed noncommutative words.
No such lifting, general correlated-tuple theorem, or counterexample is asserted here.
The general unbounded target remains open unless a separate direct-domain or mixed-word argument supplies that step.

## 9. Full free-normal-tuple affiliated conclusion

Here is the complete consequence at its exact scope.
Let (M,tau) be finite tracial with faithful normal probability trace, H=L2(M,tau), and Omega=1.
Let X=(X_1,...,X_d) be a finite bounded normal generating tuple whose coordinate algebras B_j=W*(X_j) are freely independent.
Set

    P_X=C<X,X*>, A_X=C<X>, F_X=Div_(L0(M)) A_X.

Assume only the original C_F0025 operator premises:

    Dom D_(i,0)=P_X Omega,
    Omega in Dom D_(i,0)*,
    [D_(i,0),X_j]=delta_ij P_Omega on P_X Omega,
    [D_(i,0),X_j*] has a compact bounded extension.

Write D_i for the original Hilbert closure.
Then

    M subset Dom D_i intersect Dom D_(i,0)*                     (19)

for each i, and reclosing D_i restricted to M returns this same D_i.
For every u in L0(M) and arbitrary bounded left/right fractions

    u=s^(-1)a=b t^(-1), s,a,b,t in M, s and t regular,

define the actual regular-commutator realization on M by

    K_i^(s,a;b,t) q=s D_i(bq)-a D_i(tq),       q in M.             (20)

All inputs are legal by (19).
The full equivalence is

    u in F_X
      iff every map (20) has finite-dimensional range
      iff every map (20) has a bounded finite-rank extension.      (21)

The condition holds for one bounded fraction pair iff it holds for every such pair.
The extension, when present, is unique by density of M in H.
The operator (20) itself may depend on the selected fraction pair.

Separately, for bounded f in M, the original polynomial weak forms

    beta_i^f(p,q)=<D_(i,0)* p,fq>-<f* p,D_(i,0)q>, p,q in P_X,

have bounded finite-rank representatives for every i iff f in F_X.
For f in F_X intersect M these representatives are the commutators on the entire original Dom D_i, which is preserved by f.
The starred test algebra never replaces A_X in the definition of F_X.

To prove these consequences, normalize on the same original core:

    eta_i=D_(i,0)1, E_(i,0)p=D_(i,0)p-p eta_i,
    xi_i=E_(i,0)*1.

C_F0025 supplies nonatomic coordinate laws and identifies the marginal restriction e_i with Section 1's scalar canonical E0.
Its actual marginal vacuum is the Hilbert projection of xi_i to L2(B_i), hence has norm at most ||xi_i||2.
Equation (2) therefore gives the missing C_F0045 premise with a_i=(5+2 sqrt(27))||xi_i||2.
C_F0045 then supplies (19) for the original nonnormalized operators and the estimates

    ||D_i f||2 <= (sqrt(4/pi) a_i+||eta_i||2)||f||,
    ||D_(i,0)*f||2
      <= [sqrt(4/pi)(a_i+||xi_i||2)+||eta_i||2]||f||.

Their generator identities extend to M by the established bounded-set weak continuity.
C_F0024 applies to these exact restrictions and gives (20)--(21), all bounded fraction choices, and the full closed-domain bounded-element commutator statement.
C_F0025 supplies the weak-form-to-rationality direction; the converse follows by pairing the actual full-domain commutator just obtained against original polynomial adjoint vectors.

The fixed current local dependencies checked on 2026-09-29 are Yin_C_F0025 (recorded assessment 3), Yin_C_F0027 (recorded assessment 3), Yin_C_F0045 (recorded assessment 3) and Yin_C_F0024 (recorded assessment 3), all assessed proved/independently reviewed.
C_F0027's two-core-estimate graph mechanism is also written explicitly in Section 7; C_F0045 consumes that mechanism for the tuple.
C_F0024's selected current proof is [P2](Yin_C_F0024_v1.md#yin_c_f0024-p2), with the [P1 applications](Yin_C_F0024_v1.md#7-automatic-corollaries-and-optional-normalization) retained separately; its current metadata retains the exact published dependency C_F0029 (recorded assessment 2).
This note does not replace the selected C_F0024 proof or alter any historical dependency.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T17:44 |
| status | open |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#soft-cauchy-vacuum-free-normal-criterion) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: Soft Cauchy symmetrization gives both original scalar all-bounded domains from the actual vacuum alone; free-product lifting yields full unbounded regular-commutator rationality and the bounded weak-form converse for all freely independent normal coordinates, without marginal geometry assumptions.

### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T17:47 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#soft-cauchy-vacuum-free-normal-criterion) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Exact compact-starred polynomial-core hypotheses, canonical scalar normalization, diffuse marginal measures, and weak finite-rank implication. |
| dependency | [Exact material](Yin_C_F0027_v1.md#decision-candidate-0002) | Recovery of original dual and actual adjoint graphs from core infinity-to-L2 estimates. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Lift the proved arbitrary marginal estimate through freely independent coordinate algebras to both original all-M domains. |
| dependency | [Exact material](Yin_C_F0024_v1.md#decision-candidate-0002) | Complete unbounded affiliated criterion, arbitrary bounded fractions and fraction independence on the recovered original domains. |
| review | [Exact material](../audits/reviews/Yin_R_F0037_v1.md) | Complete nine-section proof, exact three-point identities, smooth actual-vacuum tests, positive-weight bounds, actual original adjoint and graph domains, and full free-normal unbounded criterion with arbitrary bounded fractions plus bounded weak-form equivalence. Existing C_F0025/C_F0027/C_F0045/C_F0024 and VV16 interfaces checked at their recorded scopes. General correlated tuples excluded. |

Recorded mathematical summary: Soft Cauchy symmetrization gives both original scalar all-bounded domains from the actual vacuum alone; free-product lifting yields full unbounded regular-commutator rationality and the bounded weak-form converse for all freely independent normal coordinates, without marginal geometry assumptions.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:07 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#soft-cauchy-vacuum-free-normal-criterion) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Exact compact-starred polynomial-core hypotheses, canonical scalar normalization, diffuse marginal measures, and weak finite-rank implication. |
| dependency | [Exact material](Yin_C_F0027_v1.md#decision-candidate-0002) | Recovery of original dual and actual adjoint graphs from core infinity-to-L2 estimates. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Lift the proved arbitrary marginal estimate through freely independent coordinate algebras to both original all-M domains. |
| dependency | [Exact material](Yin_C_F0024_v1.md#decision-candidate-0002) | Complete unbounded affiliated criterion, arbitrary bounded fractions and fraction independence on the recovered original domains. |
| review | [Original finding](../audits/reviews/Yin_R_F0037_v1.md#scalar-findings) | Actual original independent complete scalar finding, with exact smooth-test, soft-kernel, positive-weight and original graph/adjoint scope and original attribution limits. |
| review | [Original finding](../audits/reviews/Yin_R_F0037_v1.md#end-to-end-free-tuple-assembly-and-completion-boundary) | Actual original independent complete free-normal assembly, arbitrary bounded fractions, full affiliated criterion and original weak-form equivalence; no general correlated-tuple conclusion. |

## Recorded review scopes

Accompanying material (original association; no added proof premise): [Exact material](../audits/literature/VV16/Yin_U001.md).

Complete nine-section proof, exact three-point identities, smooth actual-vacuum tests, positive-weight bounds, actual original adjoint and graph domains, and full free-normal unbounded criterion with arbitrary bounded fractions plus bounded weak-form equivalence.
Existing C_F0025/C_F0027/C_F0045/C_F0024 and VV16 interfaces checked at their recorded scopes.
General correlated tuples excluded.

Review: [Exact material](../audits/reviews/Yin_R_F0037_v1.md).

Material covered by that review: [Exact material](../audits/literature/VV16/Yin_U001.md); [Exact material](Yin_C_F0055_v1.md).

---
author: Yin
---

# Original-law phase spread and exclusion of prescribed near-modes

Yin records this independent whole-proof inspection at 2026-11-13T02:37 UTC.
The reviewer received the fixed C196v3 and its dependency locators, took no part in developing its argument, and received no development discussion, explanation or prior finding on this version.
The reviewer had previously inspected the fixed C194v33 proof and its external small-ball input independently.
This inspection checked their extension to the mark-conditional laws and the new compensation argument from the fixed mathematical inputs.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original-law exclusions](#original-law-whole-proof) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original-law exclusions](#original-law-whole-proof) | [C196v3 statement](../../claims/Yin_C_F0196_v3.md#statement) | Simultaneous phase spread, dictionary exclusion and partial-alphabet exclusion for original unbounded inputs. |
| [Original-law exclusions](#original-law-whole-proof) | [C196v3 argument](../../claims/Yin_C_F0196_v3.md#argument) | All truncation, compensation, corner, conditioning, entropy and summability steps. |
| [Original-law exclusions](#original-law-whole-proof) | [C198v1 sparse truncation](../../claims/Yin_C_F0198_v1.md#sparse-truncation) | Original-law mark count and truncated norm guard with the chosen exponents. |
| [Original-law exclusions](#original-law-whole-proof) | [C196v1 row estimate](../../claims/Yin_C_F0196_v1.md#affine-small-ball) | Independent centered fourth-moment rows, uniform translations and application to variance-standardized conditional entries. |
| [Original-law exclusions](#original-law-whole-proof) | [C196v2 corner argument](../../claims/Yin_C_F0196_v2.md#argument) | Successive duplication and identification of the degree-four directed path. |
| [Original-law exclusions](#original-law-whole-proof) | [C194v33 covariance calculation](../../claims/Yin_C_F0194_v33.md#argument) | Restricted two-channel covariance count, radius and uniform translated estimate after deleting \(E\). |
| [Original-law exclusions](#original-law-whole-proof) | [C194v33 covering](../../claims/Yin_C_F0194_v33.md#partial-alphabet) | Deterministic alphabet net, free complement, approximation norm and entropy exponent. |
| [Original-law exclusions](#original-law-whole-proof) | [KS26 Proposition 2.4](../literature/KS26/Yin_U001.md#ks26-u001) | Source hypotheses for standardized unmarked independent entries, column length and radius. |
| [Original-law exclusions](#original-law-whole-proof) | [C186v4 weak limit](../../claims/Yin_C_F0186_v4.md#finite-variance-weak) | Expected one-color interval masses on the fixed mesh. |
| [Original-law exclusions](#original-law-whole-proof) | [C186v4 concentration](../../claims/Yin_C_F0186_v4.md#row-concentration) | Exponential row-block concentration for interval indicators. |
| [Original-law exclusions](#original-law-whole-proof) | [C186v4 rank estimate](../../claims/Yin_C_F0186_v4.md#rank-stability) | Unconditional original-matrix counts transferred to the truncation with an interval-endpoint loss. |

<a id="original-law-whole-proof"></a>
## Finding

The argument proves all three original-law estimates with the stated summable probability.

The fourth-moment and diagonal second-moment bounds give expected mark counts \(O(N^{1/4})\) and \(O(N^{1/8})\) at the raw threshold \(N^{7/16}\).
The independent-indicator bound of C198v1 gives at most \(N^{3/8}\) marks outside a smaller exception than required.
The norm input there bounds the expectation using the centered independent strict upper part, its reflected transpose, the deterministic mean, and the bounded truncated diagonal.
The convex concentration estimate uses normalized coordinate diameters \(2N^{-1/16}\), which supplies the asserted \(e^{-cN^{1/8}}\) guard failure for a sufficiently large fixed \(K\).
After fixing mark indicators and marked values, all remaining entries have their independent one-coordinate conditional laws, including entries that meet the endpoint set at exactly one end.
For either color the unmarked off-diagonal variance tends to one by the original fixed law and its conditional fourth moment is uniformly bounded.

Expanding both product orders places the range of the difference in \(\mathbb C^E+A_0\mathbb C^E+B_0\mathbb C^E\).
The restriction of \((a,b)\mapsto A_0a+B_0b\) to output rows in \(E^c\) uses independent entries across all these rows and the two colors.
After subtracting means, its variance-weighted squared coefficient norm is at least one half for a real unit input.
The row estimate is uniform in the corresponding translations, and the \(2|E|\)-dimensional constant-mesh net is affordable on the truncated norm guard.
Complexification preserves singular values.
The last two coefficients in any representation are therefore controlled by the exterior part of the vector, and its first coefficient is controlled by subtraction.
This applies to \(w=Rh\) since the near-mode equation bounds \(\|w\|\) by \(1+3K^2+|z|\) even when the original input norms are large.
When \(E\) is empty the zero representation suffices.

For each fixed tuple, the selected rectangles contain disjoint unordered pairs and no marked entry.
Conditional Jensen applied once for each rectangle bounds the all-corner probability below by the \(2^j\)-th power of the single-corner probability.
After projection to the last panel, a surviving degree-\(j\) walk must traverse all \(j\) edges in order, and every smaller-degree term cancels.
For the first test the only outer word is \(AB\).
For the second, prescribing the first color selects the appropriate inner coefficient, and the following \(B,A\) steps select \(AB\) again.
When the first two colors agree they still correspond to independent rectangles on different edges.
For the fourth-degree test the ordered colors select only \(ABAB\), and the nuisance polynomials have degree at most three.
The successive output sizes are at least \(N/5\), so independent difference rectangles maintain a fixed fraction of the leading norm except with exponentially small probability.
The constant-root losses from the corner inequalities preserve exponential decay.
Taking nets inside the coefficient constraints costs \(e^{O(|E|)}\), and the sparse-sphere entropy is below the remaining exponent for a sufficiently small fixed support fraction.
The truncated norm guard enters the deterministic Lipschitz extension after the fixed-tuple estimates.

For each rotation, the two real equations force \(v\) near \(F(a)\) and \(D_0F(a)+F(q)\) near zero if \(\|u\|+\|r\|\) is small.
In that case \(\|F(a)\|\ge 1/2\).
Fix first the coefficient radius required for \(a=-\operatorname{Re}p/y\) and \(q=\operatorname{Im}p\).
The first test sets \(t_2\), after which \(t\) can be chosen so both \(2Kt\) and \(2\|D_0\|Kt\) meet the displayed margins using the deterministic guard bound.
Small \(\|a_1\|,\|a_2\|\) would then force \(\|a_0\|\ge1/4\) and violate the first test, while a large one violates the second test for sufficiently small residual and real part.
This fixes the uniform positive lower bound \(d_0\) before choosing the separately available larger radius for the third test.
Multiplying by \(D_0+iyI\) gives real nuisance \(D_0F(\operatorname{Re}p)-yF(\operatorname{Im}p)\).
After division by \(\|u\|\) its coefficients fit that larger radius.
The third test and the norm bound for \(H_0\) exclude all nearby sparse unit vectors, and the normalized truncation inequality gives the stated mass lower bound for every deletion and every phase.

For the dictionary step, conditioning on the original \(B\), the mark data and all \(A\)-entries incident to \(E\) fixes every \(F(p')\) for a prescribed coefficient net and preserves the independent truncated law on the remaining strict upper \(A\)-entries.
Unconditional semicircle interval counts and row-block concentration transfer from \(B\) to \(B_0\) with an interval loss of at most \(2|E|\).
The further principal restriction to \(U\) costs at most \(2d_U\) per interval, with \(d_U/N\) arbitrarily small after choosing the coordinate cutoff.
The prescribed spread keeps the real Gram determinant bounded below there.
The symmetric-direction expansion on \(U\) loses at most 16 ranks and a perturbation of size \(O_K(L^2/N)\) in the covariance multiplied by \(N\).
A small fiber eigenvalue places the minor eigenvalue in one of four short windows by the quartic determinant bound.
This leaves \(\lfloor(2-\tau)N\rfloor\) singular directions with scale \(N^{-1/2}\).
The standardized raw variables have a uniform fourth moment, so their second moment above a sufficiently large fixed cutoff is at most one half.
The scaled columns have norm \(O(N^{-1/2})\) and covariance at least the identity, and the scaled residual radius is bounded.
These verify the assumptions and radius in Koehler and Sohn, Proposition 2.4, at its previously inspected statement depth.
The original proofs of the external concentration, expected-norm and short-column theorems were outside this inspection.

The guard on the truncated matrices controls the approximation error for \(M_0h+F(p')-zh\), including approximation of the nuisance coefficients.
The coefficient-net logarithmic size is \(O(|E|\log N)=o(N\log N)\); the original dictionary has entropy at most \((1-\chi)N\log N\).
Consequently the two-channel bound leaves \(N^{-c_\chi N}\) after both unions.
The separately charged truncation exception gives the stated original-law rate.
The fixed alphabet covering saves \(\gamma(1-\alpha)N\log N+o(N\log N)\) even for an empty complementary tail or a single symbol.
First Borel–Cantelli applies within every cross-size coupling.
The estimates leave the unrestricted near-mode probability and the planar logarithmic defect open.

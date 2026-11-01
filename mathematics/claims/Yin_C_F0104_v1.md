---
author: Yin
---

# Analytic-arc duals acquire original adjoint modules under bounded right commutators or smooth right domains

## Current assessment
[Selected decision](#decision-isolated-current-review-20261022)

## Canonical analytic phases and right domain regularity

<a id="statement"></a>

Date: 2026-09-11.
Human author: Yin.
Proof development: another AI agent.
Goal: [Yin_T_F0005 Q1](../tasks/Yin_T_F0005_v1.md#yin_t_f0005).
Record kind: sufficient-condition deduction and explicit continuation boundary.
Initial assessment: complete proof draft awaiting independent review.

Current assessment, 2026-09-11: [the independent complete review](../audits/reviews/Yin_R_F0114_v1.md#4-quadratic-formula-and-boundary-checks) accepts Yin_C_F0104, including the original-adjoint recovery and explicit quadratic correction.
This dated acceptance supersedes the initial candidate disposition.
The [selected assessment](#decision-candidate-0002) records the mathematical and review assessments.

## 1. Reuse and the exact analytic input

The prior [Yin_C_F0102 weighted local-orbit criterion](Yin_C_F0102_v1.md#yin_c_f0102) is the main dependency.
Its arbitrary-expansion obstruction is preserved there and is not repeated or enlarged here.
[Yin_C_F0037](Yin_C_F0037_v1.md#yin_c_f0037) supplies the automatic Hilbert-Schmidt starred commutators and nonatomic spectra.
[Yin_C_F0086](Yin_C_F0086_v1.md#yin_c_f0086) supplies dense-left-module restriction as a graph core.
[Yin_C_F0039](Yin_C_F0039_v1.md#yin_c_f0039) fixes the paired right-multiplier convention and the analytic spectral phase.

The local search also read Yin_C_F0041/Yin_C_F0042 and [Tre17-U001](../audits/literature/Tre17/Yin_U001.md#tre17-u001).
The latter already supplies exponentially decaying two-variable Chebyshev coefficients for functions holomorphic near a compact real square.
The earlier polynomial-core arguments use Hilbert-Schmidt divided differences; they do not automatically bound commutators of an arbitrary unbounded operator in operator norm.
The elementary recurrence below supplies that separate estimate.

A primary search identified the standard functional-analytic mechanism for the smooth-module case: Lars Hormander, *Linear Functional Analysis: Lectures Fall Term 1988*, University of Lund, February 1989, [institutional PDF](https://lucris.lub.lu.se/ws/portalfiles/portal/124277769/HormanderLinearFunctionalAnalysis.pdf), Theorem 2.4.14.
Its exact separately-to-jointly-continuous bilinear-map statement and Baire proof were exposed in the indexed primary passage and read.
The PDF front matter was opened; later full-page retrieval timed out, so no page locator or whole-book inspection is claimed.
The standard closed graph theorem for Frechet spaces is retained as a functional-analysis foundation.
The concrete closed graphs and the finite-order Baire argument required here are given below, rather than importing an unexplained continuity conclusion.
No source PDF was retained.
The operator-Bernstein papers of Aleksandrov and Peller were located as related literature; no theorem from them is consumed.

Let X_i=r_i(S_i), where S_i is bounded selfadjoint with spectrum in a nondegenerate compact interval I_i=[a_i,b_i], and r_i is holomorphic and injective on a complex neighborhood of I_i.
The tuple X consists of bounded normal generators of a finite faithful tracial (M,tau).
Since r_i is injective on I_i, W*(X_i)=W*(S_i).
Put H=L2(M,tau), Omega=1 and P=P_Omega, and retain the inner product linear in its second variable.

For real s,t define
\[
 q_i(s,t)=
 \frac{r_i(s)-r_i(t)}
      {\overline{r_i(s)}-\overline{r_i(t)}},
 \qquad
 q_i(s,s)=\frac{r_i'(s)}{\overline{r_i'(s)}}.
 \tag{1}
\]
This is the conjugate spectral phase in Yin_C_F0039.
To see its analyticity without using complex conjugation as a holomorphic operation, set r_i^\#(z)=overline{r_i(overline z)}.
The divided differences of r_i and r_i^\# are holomorphic near I_i squared, and the latter is nonzero on the real square, including its diagonal.
Compactness gives a complex neighborhood on which their quotient is holomorphic.
Its diagonal value
\[
 h_i(s)=q_i(s,s)
\]
has modulus one.

Let t_in(s)=T_n((2s-a_i-b_i)/(b_i-a_i)).
Tre17 gives a fixed expansion
\[
 q_i(s,t)=\sum_{m,n\ge0}c_{i,mn}\,t_{im}(s)t_{in}(t),
 \qquad
 |c_{i,mn}|\le C_i\rho_i^{-m-n}
 \tag{2}
\]
for some rho_i>1, after shrinking the available Bernstein ellipses.
In particular every fixed polynomial weight in m,n is summable against these coefficients.
No spectral-cell characteristic functions or smallness of the curve coefficients are required.

<a id="yin_c_f0104"></a>
## Yin_C_F0104: Two right-regularity conditions on small domains

Suppose D_i:E to H are closable operators on a dense left M-module E and
\[
 [D_i,X_j]|_E=\delta_{ij}P.
 \tag{3}
\]
For each i assume at least one of the following two additional conditions.
The choice may differ between coordinates.

1. **Bounded right commutator.**
   Write R_i=rho(S_i), where rho(b)v=vb, and T_i=closure(D_i).
   Its domain is invariant under R_i and
\[
 [T_i,R_i]\text{ extends to }K_i\in\mathcal B(H).
 \tag{4}
\]
A sufficient certificate for (4) is a dense left submodule F_i contained in E, invariant under right S_i, on which [D_i,rho(S_i)] extends boundedly.
The certificate is proved below; it does not presume that every vector of E can originally be multiplied on the right within E.

2. **Smooth right module.**
   There is a dense left submodule F_i contained in E such that
\[
 v f(S_i)\in F_i
 \quad(v\in F_i,\ f\in C^\infty(I_i)).
 \tag{5}
\]
Here C-infinity(I_i) is the Frechet space with seminorms p_k(f)=max_{0<=j<=k} sup_{I_i}|f^{(j)}|.
Functions have continuous derivatives of every order up to the endpoints.
No uniform graph estimate, fixed order k or adjoint-domain condition is assumed in (5).

Then for every i the actual Hilbert adjoint D_i* has a dense left M-module in its domain.
All Yin_C_F0029 affiliated-fraction conclusions apply to the original duals, with the original algebra C<X> and no separate adjoint-module hypothesis.

More precisely, the canonical expansion (2) has a well-defined paired correction on a dense left module, with the weighted local-orbit bounds required by Yin_C_F0102.
In case (4) this correction is of the form
\[
 Q_i=\rho(h_i(S_i))\,T_i+B_i
 \quad\text{on }\operatorname{Dom}T_i,\qquad B_i\in\mathcal B(H).
 \tag{6}
\]
It is closable on the module where it is first constructed, and its closure has exactly the domain of T_i.
The multiplier in front of T_i is unitary.

These are sufficient conditions for general analytic arcs on small domains.
This Claim does not assert that (4) or (5) follows from arbitrary dense-left-module dual hypotheses.

## 2. The right Chebyshev commutator estimate

First let R be any bounded selfadjoint contraction, let T be closed and densely defined with R-invariant domain, and suppose [T,R]=K is bounded on that domain.
Polynomial functional calculus preserves the domain.
Put C_n=[T,T_n(R)] there.

The Chebyshev recurrence gives C_0=0, C_1=K and
\[
 C_n=2R C_{n-1}-C_{n-2}+2K T_{n-1}(R).
\]
Its explicit solution is
\[
 C_n=U_{n-1}(R)K+
        2\sum_{j=1}^{n-1}U_{n-1-j}(R)K T_j(R).
 \tag{7}
\]
Induction verifies both the recurrence and the initial values, with the displayed operator order.
Since ||T_j(R)||<=1 and ||U_l(R)||<=l+1,
\[
 \|C_n\|\le
 \left(n+2\sum_{j=1}^{n-1}(n-j)\right)\|K\|
 =n^2\|K\|.
 \tag{8}
\]
These are bounded extensions of the literal commutators.
Thus no scalar Lipschitz estimate has been silently promoted to an operator-Lipschitz estimate.

Apply this to the normalized right operator
\[
 \widetilde R_i=\frac{2R_i-a_i-b_i}{b_i-a_i}.
\]
Under (4), the normalized commutator has norm kappa_i=2||K_i||/(b_i-a_i).
For every v in Dom T_i,
\[
 T_i(v\,t_{in}(S_i))
    =(T_iv)t_{in}(S_i)+C_{in}v,\qquad
 \|C_{in}\|\le n^2\kappa_i.
 \tag{9}
\]

For the certificate stated after (4), Yin_C_F0086 makes D_i restricted to F_i a graph core for T_i.
If v_l in F_i tends to v in its graph norm, then
\[
 R_iv_l\longrightarrow R_iv,\qquad
 D_iR_iv_l=R_iD_iv_l+K_iv_l
                 \longrightarrow R_iT_iv+K_iv.
\]
Closedness gives R_iv in Dom T_i and the same commutator identity.
This proves the certificate in its actual original-closure form.

## 3. From bounded right commutators to the local module and (6)

Fix i satisfying (4).
The original E need not be right invariant.
Enlarge it within the fixed closed domain by
\[
 E_i^+=\operatorname{span}
     \{v\,p(S_i):v\in E,\ p\in\mathbb C[s]\}.
 \tag{10}
\]
Equation (9) puts this entire space in Dom T_i.
It is a left M-module since right polynomial multiplications commute with left M, and it contains E.
Consequently the restriction of T_i to E_i^+ is closable with closure exactly T_i.

The bounded generator commutators (3) and the starred commutators from Yin_C_F0037 extend from E to Dom T_i by graph approximation.
In particular Dom T_i is invariant under every left X_j and X_j*, and the commutator identities hold on E_i^+.
Thus the enlargement introduces neither a new closed operator nor a different Hilbert adjoint.

Choose projections e_k in E with tau(1-e_k) tending to zero, using the dense-left-module projection result of Yin_C_F0032.
For each e=e_k the orbit norm
\[
 c_{i,e}=\|a\longmapsto D_i(ae)\|_{M_\infty\to H}
\]
is finite by the closed graph argument for a closable operator on a full bounded orbit.
Equation (9) gives
\[
 \|a\longmapsto T_i(ae\,t_{in}(S_i))\|_{\infty\to2}
 \le c_{i,e}+n^2\kappa_i\|e\|_2.
 \tag{11}
\]
Here all inputs on the left belong to E_i^+.
Combining (11) with (2) proves the Yin_C_F0102 weighted local estimate.
Applying its argument on E_i^+ produces a dense left module in the adjoint of T_i restricted to E_i^+, which is exactly D_i*.
The proof can run separately for each coordinate, as explicitly allowed in Yin_C_F0102; no common right-invariant module for different noncommuting S_i is assumed.

There is also a useful operator-level simplification.
The paired series on Dom T_i satisfies
\[
 \begin{aligned}
 \sum_{m,n}c_{i,mn}\,
       T_i(vt_{in}(S_i))\,t_{im}(S_i)
 &= (T_iv)\,h_i(S_i)+B_iv,\\
 B_i&=\sum_{m,n}c_{i,mn}\,
              \rho(t_{im}(S_i))C_{in}.
 \end{aligned}
 \tag{12}
\]
The second series converges in operator norm, with
\[
 \|B_i\|\le\kappa_i\sum_{m,n}|c_{i,mn}|n^2<\infty.
 \tag{13}
\]
The first series in (12) converges because its diagonal coefficient sum converges uniformly to q_i(s,s)=h_i(s).
This proves (6).
Right multiplication by h_i(S_i) is unitary, so the graph norm of (6) is equivalent to that of T_i.
Restricting it to E, or to a dense left core used in Yin_C_F0102, therefore has closure precisely (6).
This additional closability statement is not needed by Yin_C_F0102, but is available under (4).

The paired identities are exactly those in Yin_C_F0102:
\[
 [Q_i,X_j]=[D_i,X_j^*]^*,\qquad
 [Q_i,X_j^*]=[D_i,X_j]^*
 \tag{14}
\]
on the relevant left module, with bounded Hilbert-Schmidt operators on the right.
They come from multiplying the conjugate phase with the Yin_C_F0037 phase, not from any commutation of different coordinates.

## 4. Smooth right invariance supplies finite local order

Fix i satisfying (5), a projection e in F_i, and write
\[
 \mathcal T_e(a,f)=D_i(ae f(S_i)),
 \qquad a\in M,\quad f\in C^\infty(I_i).
 \tag{15}
\]
Every input belongs to F_i by its two module properties.

For fixed a, the graph of f to mathcal T_e(a,f) is closed from the Frechet space C-infinity(I_i) to H.
Indeed, if f_l tends to f in that topology and mathcal T_e(a,f_l) tends to y in H, then ae f_l(S_i) tends to ae f(S_i) in H.
Closedness of T_i=closure(D_i) gives y=T_i(ae f(S_i))=D_i(ae f(S_i)), since the limit input is in F_i.
The Frechet closed graph theorem gives continuity.
For fixed f the identical argument on the Banach space M with its operator norm gives continuity in a.

The following explicit Baire argument obtains a single finite order uniformly in a.
Define closed subsets of M
\[
 A_{k,m}=
 \{a:\|\mathcal T_e(a,f)\|_2\le m p_k(f)
              \text{ for every }f\in C^\infty(I_i)\},
 \qquad k,m\in\mathbb N.
\]
Closedness uses continuity in a for fixed f.
Their countable union is M by the continuity in f for each fixed a.
Baire's theorem gives an A_km containing an operator-norm ball a0+epsilon times the unit ball.
Subtract its bound at a0 from its bound at a0+epsilon a and rescale.
We obtain constants C_e and a finite integer k_e such that
\[
 \|\mathcal T_e(a,f)\|_2
       \le C_e\|a\|\,p_{k_e}(f).
 \tag{16}
\]
This is the exact finite-order conclusion required from separate-to-joint continuity.
The order may depend on e and i.
There is no assumed common order for all local windows.

For completeness the rescaled Chebyshev polynomials have
\[
 p_k(t_{in})\le C_{I_i,k}(1+n)^{2k}.
 \tag{17}
\]
One direct verification uses T_n'=nU_{n-1}: U_{n-1} is a sum of Chebyshev polynomials with nonnegative coefficients of total n.
Differentiation therefore has norm at most n squared on the coefficient l1 norm of polynomials of degree at most n.
Iterating gives ||T_n^{(j)}||_infinity<=n^{2j}; affine rescaling gives (17).
This argument avoids an uninspected higher-derivative approximation theorem.

Choose projections e_l in F_i tending to one in trace.
From (16)-(17),
\[
 \|a\longmapsto D_i(ae_l t_{in}(S_i))\|_{\infty\to2}
       \le C_{i,l}(1+n)^{2k_{i,l}}.
 \tag{18}
\]
Together with (2), this is again precisely the weighted local estimate of Yin_C_F0102.
Its proof supplies a dense left adjoint module for D_i restricted to F_i.
Yin_C_F0086 gives equality of its closure and adjoint with those of the original D_i on E.
This recovers the original Hilbert adjoint rather than the adjoint of a smaller, unrelated test operator, and completes the proof of Yin_C_F0104.

The same argument works if C-infinity in (5) is replaced by a fixed Banach C^k(I_i) function algebra, with its usual derivative norm.
Right C(I_i)-invariance is another sufficient special case.
These function-domain conditions concern a dense submodule F_i; they do not require spectral characteristic functions or projections commuting with S_i.

## 5. The quadratic graph has an explicit resolvent correction

Under condition (4), the concrete test X_i=S_i+i epsilon_i S_i squared has
\[
 q_i(s,t)=-1+\frac{2}{1-i\epsilon_i(s+t)},\qquad
 h_i(s)=\frac{1+2i\epsilon_i s}{1-2i\epsilon_i s}.
 \tag{19}
\]
Write R=rho(S_i), K=[T_i,R], and E_u=exp(i epsilon_i u R).
A particularly explicit paired operator is
\[
 Q_i=h_i(R)T_i+B_i,\qquad
 B_i=2i\epsilon_i(1-2i\epsilon_iR)^{-1}
       \int_0^\infty e^{-u}E_u K E_u\,du.
 \tag{20}
\]
The integral converges in operator norm.
Both E_u are unitaries and the resolvent factor has norm at most one, so
\[
 \|B_i\|\le2|\epsilon_i|\|K\|.
 \tag{21}
\]
This bound has no small-epsilon requirement.

Here is a direct domain justification, independent of formal manipulation of an unbounded double operator integral.
Bounded [T_i,R] and R-invariance make exponentials preserve Dom T_i by the exponential series in graph norm.
The commutator identity, first from that series and then its integral form, is
\[
 [T_i,E_u]=i\epsilon_i\int_0^u E_{u-v}K E_v\,dv,\qquad
 \|[T_i,E_u]\|\le|\epsilon_i|u\|K\|.
 \tag{22}
\]
Thus on Dom T_i the H-valued integral
\[
 -T_i v+2\int_0^\infty e^{-u}E_uT_iE_uv\,du
 \tag{23}
\]
converges.
Its T_i v part is h_i(R)T_i v.
Substituting (22) into its remainder, changing variables w=u-v, and using absolutely convergent bounded-operator integrals gives
\[
 2i\epsilon_i
   \left(\int_0^\infty e^{-w}E_{2w}\,dw\right)
   \left(\int_0^\infty e^{-v}E_v K E_v\,dv\right),
\]
which is (20).

To verify that (23) is a valid paired correction, every E_u is a right multiplier and commutes with the left X_j and X_j*.
Their bounded commutators with T_i are defined on its invariant closed domain.
Passing them through (23) gives the Laplace transform with scalar kernel (19).
On their Hilbert-Schmidt realizations this is the Yin_C_F0039 conjugate-phase multiplication; it gives (14).
Finally (20) supplies bounded weakly continuous M-orbits on E.
The Yin_C_F0102 balanced-form argument therefore applies directly to this Q_i on E as well.
This argument establishes a usable explicit correction; it does not rely on assigning an arbitrary projective tensor series an action on all affiliated operators.

## 6. What has and has not become automatic

Condition (5) is a purely qualitative domain assumption.
Closed graph and Baire convert it automatically into the quantitative weighted bounds which Yin_C_F0102 had previously required as separate estimates.
Condition (4) is a single first-order right-commutator test; the entire analytic correction then follows from a polynomial n-squared estimate and, for the quadratic curve, the explicit resolvent (20).

Commuting projection windows are not hypotheses of Yin_C_F0104.
If such windows are available, their span is a dense left module stable under all right bounded functions of that coordinate, so it is covered by (5).
No strict separation example between these sufficient conditions is asserted in this record.

The general Q1 gap remains precise: an arbitrary dense left M-module need not be known to contain a dense right-smooth submodule, and the original dual relations are left-coordinate identities, not the right commutator (4).
Countably intersecting polynomial right domains supplies individual vectors and graph cores but no smooth-domain invariance or predetermined growth rate.
The older arbitrary-expansion obstruction does not settle this canonical question.

An attempted shortcut by normalizing D with left spectral multipliers has a separate algebraic defect for tuples.
Although sums of a(S_i)D_i b(S_i) are easy to define on a left module, their commutators with S_j for j different from i contain the extra terms [a(S_i),S_j]D_i b(S_i) and a(S_i)D_i[b(S_i),S_j].
They need not vanish.
The right-multiplier construction avoids these terms.
This rules out that proposed proof step, not the desired automatic-adjoint conclusion.

Current outcome: Yin_C_F0104 supplies two complete sufficient domain mechanisms, canonical weighted convergence and an explicit quadratic correction.
No closure theorem for arbitrary analytic-phase actions on L0(M), no automatic right regularity for general E, and no resolution of Q1 at its full quantifiers is claimed.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T01:31 |
| status | proved |
| reason | Adopt the exact original finding at its disclosed unknown initial-context relationship. Preserve the mathematical statement, status, selected argument, dependencies and all historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-the-right-chebyshev-commutator-estimate) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0114_v1.md#4-quadratic-formula-and-boundary-checks) | Whole six-section sufficient-condition theorem: bounded right commutators or dense smooth right modules, polynomial Chebyshev bounds, original adjoint-module recovery and the exact quadratic integral correction; no automatic right regularity for arbitrary dense-left-module duals. Actual original finding with unknown initial-context relationship; original date and accepted inputs preserved. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the separate isolated current finding on the unchanged fixed statement and proof, with exact conditions and scope. Preserve historical findings, relationships, source depths and dates; no new mathematical proof version is introduced. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-the-right-chebyshev-commutator-estimate) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0114_v1.md#current-isolated-finding) | Whole six-section sufficient-condition theorem: bounded right commutators or dense smooth right modules, polynomial Chebyshev bounds, original adjoint-module recovery and the exact quadratic integral correction; no automatic right regularity for arbitrary dense-left-module duals. |

## Historical assessments


These original assessments retain their status and explicitly absent selections.
Later proofs, reviews and dependencies are not retroactively assigned.


### Historical assessment candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T02:10 |
| status | proved |
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |
| review-status | independently reviewed |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#2-the-right-chebyshev-commutator-estimate) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0114_v1.md#4-quadratic-formula-and-boundary-checks) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0114_v1.md#4-quadratic-formula-and-boundary-checks).

Material covered by that review: [Exact material](Yin_C_F0104_v1.md).

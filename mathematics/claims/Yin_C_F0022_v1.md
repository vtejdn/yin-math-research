---
author: Yin
---

# Finite-Fisher selfadjoint tuples: finite defects on bounded vectors

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Affiliated Rationality from Conjugate Variables and Core Defects

<a id="statement"></a>

<a id="yin_c_f0022"></a>
## Yin_C_F0022: The Finite-Fisher Extension of the Main Criterion

Date: 2026-09-09.
Human author: Yin.
Proof development: the coordinating agent.
Authorization: the user's explicit request to re-examine the main theorem under MS23-type densely defined duals or existence of conjugate variables.
This is a new theorem for a selfadjoint tuple, recorded separately from the unchanged normal/bounded-dual [Yin_C_F0013](Yin_C_F0013_v1.md#yin_c_f0013).
It does not change the refuted Yin_C_F0001.
Initial state: complete candidate for independent review; the selected material decision owns the current assessment.

## 1. Statement and the Meaning of Finite Rank

Let (M,tau) be finite tracial with faithful normal probability trace, H=L2(M,tau), Omega=1, and P=P_Omega.
Let X=(X_1,...,X_d), d>=1 finite, be bounded **selfadjoint** generators of M.
Suppose the conjugate variables xi_i exist in H, equivalently Phi*(X)<infinity.
Set A=C<X> and U=U(M).
The inner product is linear in its second variable, <a,b>=tau(a* b).

The polynomial difference quotient has outer module convention partial_i X_j=delta_ij 1 tensor 1.
Let D_i be the Hilbert-space closure of the normalized polynomial operator

\[
 D_i^0(p\Omega)=(\mathrm{id}\otimes\tau)(\partial_i p)\Omega,
 \qquad p\in A.
 \tag{1}
\]

The proof below establishes

\[
 M\Omega\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*.
 \tag{2}
\]

Thus, for any bounded fractions of u in U,

\[
 u=s^{-1}a=bt^{-1},\qquad s,a,b,t\in M,
 \quad s,t\text{ regular},
 \tag{3}
\]

the expression

\[
 T_i^{s,a,b,t}z=sD_i(bz)-aD_i(tz),\qquad z\in M\Omega,
 \tag{4}
\]

is a well-defined linear operator from the **common dense bounded-vector domain** M Omega to H.
Here regular means invertible in U, or equivalently bounded, injective with dense range on H.
The operator in (4) need not be bounded initially.

Put F=Div_U C<X>.
The following are equivalent:

1. u belongs to F.
2. For some bounded fraction pair (3), every operator (4) has finite-dimensional range.
3. For every bounded fraction pair (3), every operator (4) has finite-dimensional range.

Every finite-rank operator in (4) has a unique bounded finite-rank extension to H.
Equivalently, finite rank in items 2-3 may be replaced by existence of such an extension.
For fixed fractions denote this extension by the same T_i.

In particular, for f in M,

\[
 F\cap M
 =\{f\in M:[D_i,f]\text{ on }M\Omega
       \text{ has finite rank for all }i\}.
 \tag{5}
\]

The affiliated criterion also restricts to F intersect L2(M), with **the cleared defects (4)**.
It does not replace them by a raw weak commutator for every L2 element; Yin_C_F0014 still obstructs that replacement.
It does not assert that D_i is bounded on all H.
The extra cofinite-H-domain variant of Yin_C_F0013 is not silently transferred to an operator with a smaller domain.

For bounded f the condition in (5) is also equivalent to the literal domain statement: f Dom D_i is contained in Dom D_i, and D_i f-f D_i on Dom D_i is the restriction of a bounded finite-rank operator, for every i.
Thus the bounded corollary can be expressed with an actual commutator on the full closed-operator domain.

## 2. Sources and the Additional Analytic Input

Finite Fisher information gives algebraic freeness and the conjugate/normalized-dual interface, as recorded in [MS23-U001](../audits/literature/MS23/Yin_U001.md#ms23-u001).
Its adjoint calculation, with the present inner-product convention and the flip-star identity, simplifies to

\[
 (D_i^0)^*p=p\xi_i-D_i^0p,\qquad p\in A.
 \tag{6}
\]

Indeed, if partial_i p=sum a tensor b, then [D_i^0,p*]=sum b* P a* on A, whose bounded adjoint applied to Omega is sum a tau(b)=D_i^0p.
Polynomial density makes D_i^0 closable.

The essential new analytic input is [Dab10-U002](../audits/literature/Dab10/Yin_U002.md#dab10-u002), Lemma 12, arXiv:0804.2906v2, PDF p. 9.
Its exact selfadjoint estimate implies the safe general-polynomial bound

\[
 \|D_i^0p\|_2\le C_i\|p\|,
 \qquad C_i=4\|\xi_i\|_2.
 \tag{7}
\]

For a selfadjoint p, the source bounds ||D_i^0p-p xi_i||_2 by ||xi_i||_2 ||p||, so the triangle inequality gives constant 2.
Splitting a general p into real and imaginary selfadjoint parts gives (7).
Equation (6) similarly gives

\[
 \|(D_i^0)^*p\|_2\le5\|\xi_i\|_2\|p\|.
 \tag{8}
\]

The source prints d>=2.
For d=1, freely adjoin a standard semicircular S: the conjugate of X is unchanged under the free extension and S has conjugate S.
Apply (7) to this two-variable tuple and restrict to polynomials in X.
The standard free-extension interface is recorded in Voi98-U003; the resulting norms and D_i^0 values on the original algebra are unchanged.
No claim about one-variable factoriality is imported from Dab10.
Dab10-U002 owns exact primary reading, assumptions and the original-proof inspection limit.

Finite Fisher also supplies Delta(X)=d: the free-perturbation Fisher bound makes t Phi*(X+sqrt(t)S) tend to zero, and the accepted CS05 comparison gives maximal Delta.
[MS23-U005](../audits/literature/MS23/Yin_U005.md#ms23-u005) records the exact chain through MSY23-U002 and MSY23-U004.
Hence F is an embedded free skew field in U.
Only this division-ring property is used in the final descent.

## 3. The Entire Bounded Algebra Lies in Both Domains

Fix x in M.
Kaplansky density, followed by norm approximation inside C*(X), supplies polynomial vectors p_alpha converging to x in L2, with norms at most ||x||+epsilon.
Bounds (7)-(8) make their D_i^0 and (D_i^0)^* images bounded in H.
Select weakly convergent subnets.
A closed linear operator graph is weakly closed in H direct-sum H.
Applying this first to D_i=closure(D_i^0), then to the closed adjoint (D_i^0)^*=D_i^*, gives (2) and

\[
 \|D_i x\|_2\le4\|\xi_i\|_2\|x\|,
 \qquad \|D_i^*x\|_2\le5\|\xi_i\|_2\|x\|.
 \tag{9}
\]

Let epsilon decrease to zero for these constants.
Graph uniqueness makes the values independent of approximation or subnet.
This argument concerns the actual Hilbert closure, not an arbitrary Banach-space extension from a norm-dense subalgebra of M.

We will use the following bounded-net continuity.
If x_alpha,x belong to M, sup||x_alpha||<infinity and x_alpha tends to x in L2, then

\[
 D_i x_\alpha\rightharpoonup D_i x,
 \qquad D_i^*x_\alpha\rightharpoonup D_i^*x
 \quad\text{weakly in }H.
 \tag{10}
\]

For the first assertion, pair against eta in Dom D_i^*: <eta,D_i x_alpha>=<D_i^*eta,x_alpha> converges.
This is a dense test domain, and (9) gives uniform H bounds, so convergence holds against every vector.
For the second assertion use Dom D_i, also dense.
Products of uniformly bounded approximants with fixed bounded elements converge in L2, so the same argument applies to the expressions below.

In particular, approximate z in M by uniformly bounded polynomial vectors and apply (10) to both z and X_j z.
The polynomial dual identity then passes to weak limits and gives [D_i,X_j]z=delta_ij Pz for every z in M.
This is the generator identity used in Section 5 on the full bounded-vector domain.

## 4. Closability and Two Finite-Rank Lemmas

For T_i as in (4), and eta,z in M,

\[
 \langle\eta,T_i z\rangle
 =\left\langle
 b^*D_i^*(s^*\eta)-t^*D_i^*(a^*\eta),z
 \right\rangle.
 \tag{11}
\]

All vectors here exist by (2).
Thus M lies in Dom T_i^*, making T_i closable.
It also has an infinity-to-L2 bound by (9), and consequently has the bounded-net weak continuity (10), either from (11) and polynomial density or directly term by term.

**Finite-rank closable operators.** Any densely defined closable linear T with finite-dimensional range E extends to a bounded finite-rank operator.
To see this, choose an orthonormal basis e_1,...,e_r of E.
The orthogonal projection of the dense linear domain Dom T* onto E is all E.
Choose eta_j in Dom T* whose E-projection is e_j.
Then for every z in Dom T,

\[
 \langle e_j,Tz\rangle=\langle\eta_j,Tz\rangle
 =\langle T^*\eta_j,z\rangle.
\]

Each coordinate is H-bounded, and their finite sum gives the extension.
Density makes it unique.

**Cancel a regular right multiplier on the bounded-vector domain.** Suppose a closable T:M->H has an infinity-to-L2 bound and bounded-net weak continuity, and y,y' are bounded regular elements.
If y T y', on M, has finite rank, injectivity of y implies that T(y'M) lies in a fixed finite-dimensional space E.
Write y'=v|y'| with v unitary, and set

\[
 e_n=1_{[1/n,\infty)}(|y'|),\quad
 p_n=v e_n v^*,\quad
 w_n=|y'|^{-1}e_n v^*z\in M\quad(z\in M).
\]

Then y'w_n=p_n z, the inputs p_n z have norm at most ||z||, and p_n z tends to z in L2.
Hence T(p_n z) tends weakly to Tz by the continuity assumption.
Since every term lies in E and finite-dimensional spaces are weakly closed, Tz belongs to E.
Thus T has finite rank on M, and the first lemma gives its bounded extension.
This replaces the unjustified dense-range cancellation of an arbitrary unbounded operator.

## 5. Fraction Independence and Rational Closure

Use the standard finite-tracial common-multiple construction from Yin_C_F0013: for two fraction pairs representing the same u there exist bounded regular x,y,x',y' such that

\[
 xs=ys_1,\quad xa=ya_1,\quad tx'=t_1y',\quad bx'=b_1y'.
\]

All bounded elements preserve the common vector space M.
Thus direct substitution into (4), without differentiating any multiplier, gives the exact operator identity on M

\[
 yT_i^{s_1,a_1,b_1,t_1}y'
   =xT_i^{s,a,b,t}x'.
 \tag{12}
\]

If the right side is finite rank, Section 4's cancellation lemma and closability prove the same for the new defect.
Interchanging the two fraction pairs proves independence.
Once both extensions are bounded finite rank, the usual injective-left/dense-right argument also shows equality of their numerical ranks.

Let R be the resulting finite-defect class in U.
Generators and scalars belong to R by their polynomial dual identities and s=t=1.
To show R contains F, all of Yin_C_F0013's finite fraction identities remain valid **on M**, as the next explicit formulas show.

For sums choose common left and right denominators, u_j=s^{-1}a_j=b_jt^{-1}.
The sum's defect is the sum of the two defects.
Scalar multiples work identically.

For products start with u_j=s_j^{-1}a_j=b_jt_j^{-1}.
Choose bounded x,y,p,q with x,q regular and

\[
 xa_1=ys_2,\qquad t_1p=b_2q.
\]

They are obtained from bounded fractions of a_1 s_2^{-1} and t_1^{-1}b_2.
Then

\[
 u_1u_2=(xs_1)^{-1}ya_2=b_1p(t_2q)^{-1},
\]

and its defect, acting on z in M, is

\[
 x(s_1D_i b_1-a_1D_i t_1)pz
 +y(s_2D_i b_2-a_2D_i t_2)qz.
 \tag{13}
\]

The middle terms cancel since both D_i inputs t_1 pz and b_2 qz are the same bounded vector.
Products of finite-rank extensions with bounded multipliers remain finite rank.

If u=s^{-1}a=bt^{-1} is invertible in U, then a,b are also bounded regular elements, and u^{-1}=a^{-1}s=tb^{-1}.
Its defect on M is aD_i t-sD_i b, the negative of the old one.
Thus R is a unital inverse-closed subalgebra of U containing A, so

\[
 F\subseteq R.
 \tag{14}
\]

No adjoint closure of R or bounded inverse representation is needed.

## 6. The Normalized Core Identity Replaces Fuglede

Write R_i=rho(X_i) for right multiplication by X_i.
On A, define K=sum_i[R_i,D_i^0].
Right multiplication preserves A.
Jacobi's identity and [D_i^0,X_j]=delta_ij P give

\[
 [K,X_j]=[R_j,P]=[X_j,P].
\]

Hence K+P commutes algebraically with all left polynomials.
Moreover D_i^0 Omega=0 and D_i^0 X_i Omega=Omega, so (K+P)Omega=(1-d)Omega.
Cyclicity of Omega under A therefore proves

\[
 K=(1-d)I-P\quad\text{on }A.
 \tag{15}
\]

There is no need for a bounded Fuglede theorem in this selfadjoint, polynomial-dense setting.
Bounded polynomial approximants and (10) extend (15) to all bounded vectors:

\[
 \sum_i(R_iD_i-D_iR_i)z=(1-d)z-\tau(z)\Omega,
 \qquad z\in M.
 \tag{16}
\]

For any fractions (3), sb=at.
On M, use that right multiplication commutes with s,a,b,t to obtain

\[
 \sum_i[R_i,T_i]z=sK(bz)-aK(tz)
 =(aPt-sPb)z.
 \tag{17}
\]

When the T_i have finite rank, they have bounded extensions by Section 4.
Both sides of (17) are then bounded on H, and density extends the identity to all H.
This is exactly the bounded tensor identity needed for the descent, obtained after establishing the actual domains.

## 7. Finite Tensors and the Reverse Inclusion

For g,h in H put Theta(g tensor h)z=g<Jh,z>, with Jz=z*.
This identifies H algebraic-tensor H with finite-rank operators and gives

\[
 [R_i,\Theta(g\otimes h)]
 =\Theta(gX_i\otimes h-g\otimes X_i h).
\]

Write T_i=sum_alpha Theta(g_(i,alpha) tensor h_(i,alpha)).
Equation (17) becomes

\[
 a\otimes t-s\otimes b
 =\sum_{i,\alpha}
 (g_{i\alpha}X_i\otimes h_{i\alpha}
      -g_{i\alpha}\otimes X_i h_{i\alpha})
 \tag{18}
\]

in H algebraic-tensor H, and hence in U algebraic-tensor U.
Pass to U tensor_F U; each right-hand summand vanishes.
Left multiplication by s^{-1} on the first factor and right multiplication by t^{-1} on the second are well-defined invertible outer actions and give

\[
 u\otimes_F1=1\otimes_Fu.
 \tag{19}
\]

If u were outside F, the vectors 1,u would be right-F linearly independent in U.
Extend them to a right-F basis, and choose a right-F linear map phi:U->F with phi(1)=0 and phi(u)=1.
Applying phi tensor id to (19) gives 1=0.
Therefore u belongs to F.
This proves R subset F, and with (14) establishes the theorem.

For bounded f take s=t=1 and a=b=f to obtain (5).
Equivalently one may test the weak commutator on polynomial p,q:

\[
 \beta_i^f(p,q)=\langle D_i^*p,fq\rangle
                  -\langle f^*p,D_iq\rangle.
 \tag{20}
\]

If it has a bounded finite-rank representative on those tests, it agrees with [D_i,f] on polynomial inputs by density of the first test variable.
Uniformly bounded polynomial approximations to z in M and (10) then give agreement on all M.
Conversely a finite-rank extension of (4) at these fractions gives (20).
This equivalence is asserted here for bounded f; the separate L2 raw-commutator obstruction is preserved.

To prove the literal domain formulation, note that A is a core for D_i by definition, and A is contained in M, which is contained in Dom D_i.
Thus M is also a core.
If T_i is the bounded extension in (5) and z belongs to Dom D_i, choose z_n in M with z_n->z and D_i z_n->D_i z in H.
Since f is bounded,

\[
 fz_n\longrightarrow fz,\qquad
 D_i(fz_n)=fD_i z_n+T_i z_n
       \longrightarrow fD_i z+T_i z.
\]

Closedness gives fz in Dom D_i and the desired commutator identity there.
The converse follows by restricting that identity to M.

## 8. Scope, Review and Research Consequences

The user's maximal-Delta observation supplies the algebraic part of the extension.
The additional required analytic work is the infinity-to-L2 estimate, the inclusion of all bounded vectors in the dual and adjoint domains, closability of each cleared defect, and regular-cutoff cancellation.
With these steps, the main affiliated finite-defect equivalence is valid under existence of L2 conjugates for bounded selfadjoint generators.

This theorem covers the canonical dual obtained from any MS23-type normalized polynomial-domain dual with Omega in Dom D_i*.
That polynomial operator is forced by (1), and its closure is the D_i used here.
An arbitrary larger nonclosed extension or arbitrary nonselfadjoint/normal tuple is not substituted without checking its own domain and algebraic hypotheses.

No claim about Div_M C<X>, rational L2 boundedness, or a literal all-H commutator with an unbounded D_i follows merely from finite Fisher information.
Original Yin_C_F0013 remains valid and unchanged.
The separate [Yin_C_F0023](Yin_C_F0023_v1.md#yin_c_f0023) provides a stronger bounded-dual conclusion for the q-Gaussian model by its additional summable conjugate expansion.

The independent artifact review and its actual inspection scope are recorded in the [Yin_C_F0022 proof audit](../audits/reviews/Yin_R_F0010_v1.md).
Exact source reading belongs to Dab10-U002 and the existing MSY23/MS23 units; no formal proof assistant, numerical test, external human review or novelty claim is asserted.


## Assessment history


### Decision candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-14T04:01 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#yin_c_f0022) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0010_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:41 |
| status | proved |
| reason | Select the actual retained findings and their individual checking relationships, with unchanged mathematical status, statement and argument. Original findings, dates, accepted-source depths and historical decisions remain intact; this is no new mathematical review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#yin_c_f0022) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Retained finding](../audits/reviews/Yin_R_F0010_v1.md#conjugate-variable-extension-finding) | Entire selfadjoint finite-Fisher affiliated criterion, actual all-bounded-vector dual/adjoint domains, regular-cutoff cancellation, both implications, fraction independence and both final bounded-element formulations, with original source-depth limits. |

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

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |

## Recorded review scopes

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0010_v1.md).

Material covered by that review: [Exact material](Yin_C_F0022_v1.md).

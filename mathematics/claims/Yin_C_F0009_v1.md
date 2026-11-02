---
author: Yin
---

# One-state and restricted two-state or single-normal reductions

## Current assessment
[Selected decision](#decision-isolated-review-20261022)

## Scalar Pivot Criteria for Two-State Rational Representations

<a id="statement"></a>

<a id="yin_c_f0009"></a>
## Yin_C_F0009: One State, a Two-State Complementary Pivot, and One Normal Combination

Goal: [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001), route [Yin_S_F0005](../strategies/Yin_S_F0005.md#s_f0005).
Date: 2026-09-09.
Provenance: project deduction using exact Schur algebra and [Yin_C_F0004](Yin_C_F0004_v1.md#yin_c_f0004).
This is a restricted result for specified representations of elements covered by [Yin_C_F0005](Yin_C_F0005_v1.md#yin_c_f0005); it does not settle the complete two-state or general converse.
Assessment: [selected assessment](#decision-isolated-review-20261022); the [independent audit](../audits/reviews/Yin_R_F0063_v1.md#scalar-pivots) records the completed review.
No novelty claim is made.

## Setting and Statement

Assume the original Yin_C_F0001 hypotheses, and let f in M have finite-rank [D_i,lambda(f)] for every i.
Thus each generator X_i is bounded normal, M=W*(X), and the D_i are bounded duals with [D_i,lambda(X_j)]=delta_ij P.
Put

\[
R_X=\operatorname{Div}_M\mathbb C\langle X\rangle,
\qquad F_X=\operatorname{Div}_{U(M)}\mathbb C\langle X\rangle.
\]

Yin_C_F0005 gives f in F_X; the audited free-field evaluation supplies the affiliated inverses of full polynomial matrices.
Suppose a specified representation of f is

\[
f=uB^{-1}v,\qquad B=I_n-\sum_i A_iX_i,
\tag{1}
\]

with constant matrices A_i, a nonzero constant row u, and a nonzero constant column v.
The monic pencil is full, and its evaluated inverse in (1) initially belongs to M_n(U(M)).
A monic scalar-origin representation is an additional representation hypothesis, not asserted to exist for every element of F_X.
Minimality is not needed for the following conclusions.

1. **One state.**
   If n=1, then f belongs to R_X and B^{-1} belongs to M.
2. **Two states with a bounded complementary pivot.**
   If n=2, choose nonzero constant vectors w,z satisfying

   \[
   wv=0,\qquad uz=0,
   \]

   and suppose the scalar polynomial

   \[
   k=wBz
   \tag{2}
   \]

   is invertible in M.
   Then f belongs to R_X and B^{-1} belongs to M_2(R_X), hence M_2(M).
   In dimension two, the possible w and z each form one-dimensional spaces, so the bounded-unit condition is independent of their nonzero scalar normalization.
3. **One effective normal combination.**
   For any n in (1), suppose A_i=c_i A for a fixed constant matrix A and scalars c_i, not all zero.
   If Y=sum_i c_iX_i is normal, then f belongs to Div_M C[Y], hence R_X.
   This part does not assert boundedness of the entire given inverse B^{-1}.

The two-state conclusion in part 2 also holds for any polynomial matrix B invertible over U(M), with the same nonzero u,v and bounded f, whether or not B is monic or the original tuple has bounded duals.
The stated research application retains Yin_C_F0001's hypotheses; they must not be omitted when treating these restricted results as progress on Yin_T_F0001.

## Proof of the One-State Case

Here u,v are nonzero scalars and f=(uv)B^{-1}.
B is a scalar polynomial in X.
Since f is bounded, B^{-1}=(uv)^{-1}f is bounded.
Both B and this inverse lie in M, and their affiliated inverse identities are the same identities in M.
Hence B is a bounded unit, B^{-1} belongs to R_X, and so does f.

If an expression has u=0 or v=0, its value is the trivial scalar zero; this gives no information about its unused inverse.
The nonzero-vector assumption in the stated inverse conclusion is therefore retained.

## Proof of the Two-State Pivot Criterion

Choose a constant row t with tv=1 and a constant column s with us=1.
Define

\[
P=\begin{pmatrix}t\\w\end{pmatrix},
\qquad Q=\begin{pmatrix}s&z\end{pmatrix}.
\tag{3}
\]

The rows t,w are independent because their values on v are 1 and 0; similarly, s,z are independent because u takes values 1 and 0 on them.
Thus P and Q are invertible complex matrices, with

\[
Pv=e_1,\qquad uQ=e_1^T,
\qquad P^{-1}e_1=v,\quad e_1^TQ^{-1}=u.
\tag{4}
\]

Set

\[
C=PBQ=\begin{pmatrix}a&b\\c&k\end{pmatrix}.
\tag{5}
\]

Every block in (5) is a scalar polynomial in X, and the lower-right entry is exactly (2).
Since C^{-1}=Q^{-1}B^{-1}P^{-1}, equation (4) gives

\[
(C^{-1})_{11}=uB^{-1}v=f.
\tag{6}
\]

The changes in (3) are independent row and column changes.
They need not form a similarity or preserve the identity constant term; neither property is needed for the following Schur calculation.

By hypothesis k is a unit of M, so k^{-1} belongs to R_X.
Form the scalar Schur complement

\[
S=a-bk^{-1}c\in R_X.
\tag{7}
\]

Invertibility of C over U and the known inverse of k imply that S is invertible over U, and the exact block inverse is

\[
C^{-1}=
\begin{pmatrix}
S^{-1}&-S^{-1}bk^{-1}\\
-k^{-1}cS^{-1}&k^{-1}+k^{-1}cS^{-1}bk^{-1}
\end{pmatrix}.
\tag{8}
\]

Equations (6) and (8) give f=S^{-1}.
Since S and f are bounded, Sf=fS=1 are identities in M.
Thus S is a bounded unit.
Inverse closure in M now puts f in R_X.
All entries in (8) belong to R_X, and

\[
B^{-1}=QC^{-1}P
\]

has entries in R_X as well.
This proves both claims.
The proof invokes an existing bounded pivot and constructs an admissible scalar expression; it does not infer a bounded pivot from affiliated invertibility alone.

### Coordinate Checks and a Non-Necessity Example

For u=e_1^T and v=e_1, one can choose w=e_2^T and z=e_2.
The criterion is the familiar opposite diagonal pivot B_22.
For u=e_1^T and v=e_2, choose w=e_1^T and z=e_2; the complementary pivot is B_12.
In this latter case, writing B=[[a,b],[c,d]], column permutation gives

\[
(B^{-1})_{12}=(c-db^{-1}a)^{-1}
\quad\text{when }b\text{ is a unit}.
\]

This checks the multiplication order and the off-diagonal case without a commutative determinant argument.

The complementary pivot need not be invertible when the conclusion is true.
For example,

\[
B=\begin{pmatrix}1&-X_1\\0&1\end{pmatrix},
\quad u=e_1^T,\quad v=e_2,
\quad f=X_1
\]

has a polynomial inverse even if X_1 is not a unit of M.
Failure of the complementary-pivot hypothesis is therefore only failure of this sufficient test, not a counterexample to bounded realization or Yin_C_F0001.

## Proof of the One-Normal-Combination Reduction

Under A_i=c_i A, the pencil is B=I_n-AY.
Since its entries are scalar polynomials in the one normal operator Y, its affiliated inverse entries and scalar compression are measurable scalar rational functions of Y.
For example, the ordinary adjugate identity applies to the commuting entries of the matrix I_n-Az before evaluation.
The determinant has constant term 1, so is a nonzero polynomial; its affiliated inverse is legitimate here.
Consequently boundedness of f places f in N=W*(Y).

Choose j with c_j nonzero and set E=D_j/c_j.
Linearity of the commutator gives

\[
[E,Y]=P,\qquad
\operatorname{rank}[E,f]<\infty.
\tag{9}
\]

Let Q_N be the orthogonal projection of H onto L2(N,tau).
This subspace reduces multiplication by N, so Q_N commutes with Y and f.
It contains Omega.
The bounded compression E_N=Q_N E|_{L2(N)} therefore satisfies

\[
[E_N,Y|_{L^2(N)}]=P_\Omega|_{L^2(N)},
\qquad
[E_N,f|_{L^2(N)}]=Q_N[E,f]|_{L^2(N)}.
\]

The second operator has finite rank.
The restricted trace is faithful normal, N is generated by the normal Y, and all hypotheses of Yin_C_F0004 apply.
That theorem gives

\[
f=p(Y)q(Y)^{-1},\qquad q(Y)\text{ invertible in }N.
\]

The same inverse is bounded in M.
Since Y is a linear polynomial in X, this is a valid scalar expression in R_X.
This proves part 3, including the case where several A_i are nonzero.

Normality of Y is an explicit premise.
It holds, for example, for a real linear combination of selfadjoint X_i, but need not hold for an arbitrary complex combination of normal generators.
No assertion about all linear combinations is used.
If every c_i is zero, the pencil is I_n and f is constant, so the conclusion is immediate separately.

## Scope and Next Unresolved Test

These deductions remove one-state, one-effective-normal-variable, and bounded-complementary-pivot cases from the first Yin_S_F0005 test.
They do not settle a general minimal two-state pencil with two genuinely active directions and no known bounded scalar pivot.
In particular, Yin_C_F0007's L2 states are not replaced by bounded states in the remaining case.

The [two-state exploration](../ledger/Yin_L_F0015_v1.md) records additional Schur calculations and a low-rank one-sided-fraction normal form.
Its scaled sandwich remains an unverified test until bounded duals and the actual finite commutators are checked.
Failure of a displayed minimal inverse to be bounded, if eventually verified, would first test the chosen representation; it would not by itself refute Yin_C_F0001's existence of a valid bounded scalar expression.

This proof uses finite-dimensional changes of basis, exact scalar Schur inversion, and the already reviewed Yin_C_F0004.
No numerical experiment, proof assistant, external human review, whole new source audit, or novelty assessment is claimed.


## Assessment history


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:20 |
| status | proved |
| reason | Select the actual previously adopted finding explicitly, preserving its original date, complete checked mathematical scope and retained limits while declaring its actual known or genuinely unestablished relationship. The statement, argument, dependencies and mathematical assessment are unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#proof-of-the-one-state-case) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Actual complete finding](../audits/reviews/Yin_R_F0063_v1.md#scalar-pivot-finding) | All three scalar-pivot criteria: nonzero one-state observation, two independent complementary coordinate changes with an additional bounded scalar pivot, and the effective normal-combination compression. Includes exact noncommutative Schur order, off-diagonal and nonnecessity tests; no universal two-state pivot or tuple conclusion. |


### Decision isolated-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:53 |
| status | proved |
| reason | Adopt the actual context-isolated whole-argument review after complete comparison with the old finding, retaining fixed mathematics, exact assumptions and historical adoption facts. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#proof-of-the-one-state-case) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [New isolated finding](../audits/reviews/Yin_R_F0063_v1.md#scalar-pivots) | All three restricted scalar-pivot conclusions, including independent complementary changes, bounded-unit and normality premises, off-diagonal/nonnecessity tests and the original limitations. |

## Historical assessments


<a id="decision-candidate-0002"></a>
### Historical assessment candidate-0002

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
| argument | [Exact material](#proof-of-the-one-state-case) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0063_v1.md#scalar-pivot-finding) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).



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

Review: [Exact material](../audits/reviews/Yin_R_F0063_v1.md#scalar-pivot-finding).

Material covered by that review: [Exact material](Yin_C_F0009_v1.md).

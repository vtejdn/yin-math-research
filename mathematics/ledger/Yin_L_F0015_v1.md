---
author: Yin
---

# Two-State Monic Rationality: First Reductions and Pivot Tests

Subsequent outcome, 2026-09-09: [Yin_C_F0012](../claims/Yin_C_F0012_v1.md#yin_c_f0012) completes the sandwich test with actual bounded duals and excludes every bounded scalar expression.
It refutes the universal bounded-state/descent upgrade, including the two-state test.
The derivations, proposed bridges and then-unresolved descriptions below are preserved as exploration history; current dispositions are in the [strategy index](../strategies/readme.md).

Date: 2026-09-09.
Author: another AI agent.
Goal: [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001), route [Yin_S_F0005](../strategies/Yin_S_F0005.md#s_f0005).
This is an exploration record with explicit local deductions and unresolved tests, not a registered claim or a proof of the full two-state case.
It retains the original normal-generator and bounded-dual hypotheses of [Yin_C_F0001](../claims/Yin_C_F0001_v1.md#yin_c_f0001).
No new source theorem is imported here.

## Setting and the Available State Information

Write R_X=Div_M C<X> and F_X=Div_U C<X>.
Let

\[
B=I_2-\sum_i A_iX_i,\qquad f=uB^{-1}v\in M,
\]

where u,v are nonzero constant row/column vectors, the realization is reachable and observable, and every [D_i,f] has finite rank.
All inverses initially belong to the affiliated algebra U(M).
By [Yin_C_F0007](../claims/Yin_C_F0007_v1.md#yin_c_f0007),

\[
g=uB^{-1}\in(L^2)^2,\qquad h=B^{-1}v\in(L^2)^2,
\qquad \operatorname{rank}[D_i,f]=\operatorname{rank}_{\mathbb C}A_i.
\]

Neither the whole inverse nor either state row/column is yet known to be bounded.
The purpose of these tests is to identify an additional argument genuinely supplied by the two-state structure, rather than to replace L2 with L-infinity in these statements.

## Scalar-pivot interfaces

[C_F0009](../claims/Yin_C_F0009_v1.md#statement) retains the complete one-effective-normal-variable reduction, complementary scalar-pivot criterion, coordinate forms and the unipotent nonnecessity example.
Its additional hypotheses remain essential; failure of one chosen pivot does not refute the original target.

## Further pivot recoveries

More generally, for an upper triangular B=[[a,b],[0,d]], if both a and d are bounded units, then

\[
B^{-1}=\begin{pmatrix}a^{-1}&-a^{-1}bd^{-1}\\0&d^{-1}\end{pmatrix}
\]

has entries in R_X.
This covers a different concrete family without requiring b to be invertible.

There are also two-pivot recoveries for a bounded diagonal observation f=(B^{-1})_11.
If b and c are bounded units, the identity B^{-1}B=I gives

\[
(B^{-1})_{12}=(1-fa)c^{-1}\in M.
\]

With b as the column-swapped pivot, this entry equals (c-db^{-1}a)^{-1}.
Its boundedness therefore makes that Schur complement a unit in M and puts the complete inverse in the scalar division closure, by (2) after permutation.
This illustrates that one can sometimes certify bounded inverse entries from the bounded observation by first choosing a different scalar pivot.

All these conditions are checkable algebraic sufficient conditions.
They do not yet derive the required pivots from normality, bounded duals, and finite commutator ranks alone.

## 4. Rank-One Coefficients with a Common Image

A useful genuinely two-variable low-rank normal form occurs when all nonzero A_i have a common one-dimensional image.
Write

\[
A_i=a b_i,\qquad a\in\mathbb C^{2\times1},\quad
b_i\in\mathbb C^{1\times2},
\]

and define the polynomial row b(X)=sum_i b_i X_i, and scalar linear polynomials

\[
Y=b(X)a=\sum_i(b_i a)X_i,
\qquad Z=b(X)v.
\]

The rank-one inverse identity, verified by multiplying on both sides, is

\[
(I_2-a b(X))^{-1}=I_2+a(1-Y)^{-1}b(X).
\tag{4}
\]

It is valid over the affiliated field: 1-Y is a nonzero formal polynomial, and the evaluated free field supplies its inverse.
Consequently

\[
f=uv+(ua)(1-Y)^{-1}Z.
\tag{5}
\]

Minimal observability forces ua nonzero; otherwise uA_w=0 for every nonempty word and observability in dimension two fails.
This reduces the bounded scalar observation to a bounded one-sided fraction (1-Y)^{-1}Z, with at most two effective scalar linear forms.
It does not make Y or Z normal automatically.

If either 1-Y or Z is a bounded unit, (5) settles scalar division membership: the first case is a direct valid expression, while in the second case boundedness of (1-Y)^{-1}Z makes (1-Y)^{-1} bounded after multiplication by Z^{-1}.
When neither is a bounded unit, their normality and dual relations must be used in an additional argument; (4) alone does not provide it.

The concrete monic pencil

\[
B=\begin{pmatrix}1-X&-Y\\0&1\end{pmatrix},
\quad A_X=E_{11},\quad A_Y=E_{12},
\quad f=(1-X)^{-1}Y
\tag{6}
\]

is reachable and observable with u=e_1^T,v=e_2.
Both active matrices have rank one, so it lies at the smallest nontrivial two-generator commutator budget.
Its left and right states are

\[
g=((1-X)^{-1},f),\qquad h=(f,1)^T.
\]

Yin_C_F0007 therefore gives (1-X)^{-1} in L2, but does not yet make it bounded.
Equation (6), with X,Y normal and a bounded dual system verified, is a sharper remaining test than an unspecified arbitrary two-state pencil.

## The symmetric sandwich test

[C_F0012, Sections 1–7](../claims/Yin_C_F0012_v1.md#1-an-explicit-tracial-fock-model) retains the complete sandwich construction, bounded duals, actual finite commutators and scalar-division exclusion.
Its [minimal monic form](../claims/Yin_C_F0012_v1.md#7-the-monic-two-state-form-and-the-original-conjecture) resolves the formerly unverified symmetric two-state test.
The [Section 8 extension](../claims/Yin_C_F0012_v1.md#8-a-two-state-counterexample-with-both-commutator-ranks-equal-to-one) resolves the concrete common-image pencil above with both commutator ranks equal to one.
These negative examples do not remove the restricted scalar-pivot deductions or the general common-image algebraic reduction.

## Scope

The positive pivot conclusions above retain their stated extra bounded-unit hypotheses.
The general common-image reduction is algebraic; it does not make its effective linear combinations normal or their affiliated inverses bounded.
The exact counterexamples and their reviews are owned by C_F0012 and its selected evidence.
No new theorem, review, numerical computation, formal verification or novelty assessment is made by these references.

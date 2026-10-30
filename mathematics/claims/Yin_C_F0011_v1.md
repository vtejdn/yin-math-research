---
author: Yin
---

# Scaled free-field intersection obstruction without bounded duals

## Current assessment
[Selected decision](#decision-finding-owned-review)

## A Scaled Free-Field Model with a Strict Bounded-Closure Boundary

<a id="statement"></a>

<a id="yin_c_f0011"></a>
## Yin_C_F0011: Affiliated Free-Field Evaluation Alone Does Not Give Bounded Descent

Goal: [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001), clarifying the additional hypotheses required by [Yin_S_F0002](../strategies/Yin_S_F0002.md#s_f0002).
Date: 2026-09-09.
Provenance: project deduction completing the scaled-semicircular candidate preserved in the [historical exploration](../ledger/Yin_L_F0002_v1.md).
Initial candidate: another AI agent; complete proof and center argument: another AI agent.
No novelty claim.
Assessment: [selected assessment](#decision-candidate-0002); the [independent full-chain audit](../audits/reviews/Yin_R_F0006_v1.md) records root's completed review.

## Statement and Scope

Let S=(S_1,S_2) be a standard free semicircular pair in its generated finite factor M_0=W*(S_1,S_2), with faithful normal probability trace tau_0.
In particular, tau_0(S_j^2)=1 and ||S_j||=2.
Let nu be any Borel probability measure of full support on (0,1].
Set

\[
B=L^\infty((0,1],\nu)\overline\otimes M_0,
\qquad X_j(t)=tS_j,
\qquad N=W^*(X_1,X_2)\subset B,
\tag{1}
\]

with the product trace, restricted to N.
Write

\[
A_X=\mathbb C\langle X_1,X_2\rangle,
\quad R_X=\operatorname{Div}_N A_X,
\quad F_X=\operatorname{Div}_{U(N)}A_X.
\]

Here U(N) is the finite-tracial affiliated-operator algebra.
Its sums and products are the canonical closed affiliated operations.
In R_X, every inverse is instead a bounded inverse in N, with all intermediate expressions in N.
Then:

1. N=B.
   Its center is nontrivial for every such nu, and is diffuse when nu is nonatomic.
   No bounded dual system on L2(N) satisfies the relations of Yin_C_F0001 for X.
2. Polynomial evaluation at X extends to an injective unital homomorphism from the free field on two generators into U(N), with image F_X.
   Every full polynomial square matrix evaluates to an affiliated-invertible matrix of the same size.
3. The well-defined rational element

   \[
   f=X_1(X_1^2+X_2^2)^{-1}X_1\in F_X
   \tag{2}
   \]

   is a bounded, nonscalar positive contraction in N, but is not in C*(X_1,X_2).
   Consequently

   \[
   R_X\subsetneq F_X\cap N.
   \tag{3}
   \]

4. For this f there is no finite size k, square polynomial matrix T(X) invertible in M_k(N), polynomial row u(X), polynomial column v(X), and polynomial scalar p(X) such that

   \[
   f=p(X)+u(X)T(X)^{-1}v(X).
   \tag{4}
   \]

   Constant rows and columns, affine linear pencils, and the case p=0 are included.
   In fact the same exclusion holds if all coefficients in (4) are allowed to lie in C*(X).

Thus a faithful affiliated free-field realization and a bounded scalar rational value do not, by themselves, imply bounded scalar division closure or the existence of any bounded inverse polynomial-matrix realization.
This is not a counterexample to [Yin_C_F0001](Yin_C_F0001_v1.md#yin_c_f0001): its bounded-dual hypothesis fails here.
No finite-commutator assertion for a nonexistent dual system is made.

## Inputs and Their Exact Roles

- [Miy22-U001](../audits/literature/Miy22/Yin_U001_v1.md#miy22-u001) supplies the standard tracial Fock realization of the semicircular pair.
  The bounded right annihilators satisfy `[r_i*,S_j]=delta_ij P`; this is checked on the word basis by deletion of the final letter.
  The [MSY23 bounded-dual interface](../audits/literature/MSY23/Yin_U005_v1.md#msy23-u005), together with its main free-field theorem, therefore supplies free-field evaluation for S.
  No bounded dual is thereby supplied for the centrally scaled X.
- [MSY23-U004, Theorem 5.6 and Remark 5.10](../audits/literature/MSY23/Yin_U004_v1.md#msy23-u004) says that invertibility of all full polynomial matrices in U(N) is equivalent to an injective evaluated free field, whose image is exactly the affiliated division closure.
  It also supplies the finite-tracial fact that an injective square bounded matrix has an affiliated inverse.
  No bounded inverse conclusion is imported.
- [Dab10-U001](../audits/literature/Dab10/Yin_U001_v1.md#dab10-u001), with [Voi98-U005](../audits/literature/Voi98/Yin_U005_v1.md#voi98-u005), gives factoriality for a selfadjoint generating tuple of length at least two with bounded duals.
  This also verifies factoriality of the initial M_0 from its Fock duals if needed.
  Its use for S precedes and is independent of any assertion about X.

The standard measurable-field model of the tensor product, finite-tracial affiliated operations, and Hilbert-space closed convex sets are retained foundations.
The needed contraction factor, bounded-limit argument, and C*-inverse-closure argument are proved below.
No separate Douglas factorization theorem or bounded minimal-realization theorem is assumed.

## 1. Recovering the Center and the Whole Tensor Product

First,

\[
N'\cap B=Z(B)=L^\infty((0,1],\nu)\otimes1.
\tag{5}
\]

Indeed, an element a in B commuting with X_1,X_2 has measurable fibers a(t) in M_0 satisfying t[a(t),S_j]=0 almost everywhere for j=1,2.
The two equations hold on one common conull set.
Since t>0, the fibers commute with both S_j and hence with M_0.
Factoriality of M_0 makes them scalar.
Their scalar coefficients tau_0(a(t)) are measurable and essentially bounded.
The converse inclusion in (5) follows from centrality.
This step does not assume that N already contains Z(B).

Consider the L2(B)-closed convex hull K of

\[
\{uX_1^2u^*:u\in\mathcal U(N)\}.
\]

It has a unique element y of least Hilbert-space norm.
Conjugation by each N-unitary preserves K and the norm, so uyu*=y in L2(B).
To turn this into a bounded-operator statement, choose finite convex combinations c_m converging to y in L2.
Each c_m belongs to N and satisfies 0<=c_m<=4.
The same bounded order interval is weak-* compact in N; a subnet has weak-* limit c in N with 0<=c<=4.
For every a in B,

\[
|\tau(a^*(c_m-y))|
\le\|a\|_2\|c_m-y\|_2\longrightarrow0.
\]

The subnet gives the identical pairing with c.
Since B is dense in L2(B), c=y.
Thus y is bounded and belongs to N.
Its invariance and (5) imply y in Z(B).

The explicit central conditional expectation E=id tensor tau_0 is an L2 contraction and satisfies E(ubu*)=E(b) for all B-unitaries u, by the fiberwise tracial identity.
Hence E(c_m)=E(X_1^2)=t^2.
Taking the L2 limit and using centrality of y gives

\[
t^2=E(y)=y\in N.
\tag{6}
\]

This argument only identifies a bounded fixed vector; it does not assume an unproved description of all affiliated fixed vectors.

Functional calculus gives t in N.
Bounded Borel functions of this coordinate generate all of L-infinity((0,1],nu) tensor 1.
For epsilon>0 let

\[
z_\varepsilon=1_{[\varepsilon,1]}(t),
\qquad a_\varepsilon=t^{-1}z_\varepsilon.
\]

These are elements of N, with ||a_epsilon||<=epsilon^{-1}, and

\[
a_\varepsilon X_j=z_\varepsilon S_j\in N.
\]

As epsilon decreases to zero, these products converge strongly to the constant section S_j and have norms bounded by ||S_j||.
Strong closedness gives S_j in N.
Thus N contains both the central algebra and the constant copy of M_0, proving N=B.

Full support makes t^2 nonconstant almost everywhere, so N is not a factor.
Full support does not imply that nu is nonatomic: a probability supported on a countable dense set is possible.
The claim of a diffuse center is therefore restricted to nonatomic nu, including both earlier examples `dnu=dt` and `dnu=dt/(2 sqrt(t))`.

## 2. Full Polynomial Matrices Remain Affiliated-Invertible

Let P be any full k by k matrix over the free polynomial algebra C<x_1,x_2>.
Here full means that its polynomial inner rank is k.
For each fixed t>0, the substitution

\[
\sigma_t(x_j)=t x_j
\]

is an automorphism, with inverse sigma_{1/t}.
Applying these two automorphisms to factorizations shows that they preserve inner rank.
Therefore sigma_t(P) is full.
The semicircular free-field input makes

\[
P(tS_1,tS_2)
\]

an injective bounded operator on L2(M_0)^k, with an inverse in M_k(U(M_0)).
This is asserted for each fixed full P and every t>0; no uniform lower bound on its singular values is asserted.

The matrix P(X) acts on

\[
L^2(B)^k=L^2\bigl((0,1],\nu;L^2(M_0)^k\bigr)
\]

as the bounded decomposable operator with fibers P(tS).
These fibers are norm-continuous in t, since P is polynomial.
If P(X)xi=0, then P(tS)xi(t)=0 almost everywhere, and fiberwise injectivity forces xi(t)=0 almost everywhere.
Thus P(X) is injective.
This fixes P first and needs no simultaneous exceptional set over all polynomial matrices.

We already proved N=B.
Consequently P(X) is an injective square matrix over the finite tracial algebra N.
Its polar decomposition has initial support 1; equality of the finite traces of its initial and final supports makes the final support 1 as well.
The spectral inverse of its absolute value gives a two-sided inverse in M_k(U(N)).
All full polynomial matrices therefore satisfy the exact condition of MSY23 Theorem 5.6.
Its evaluated free field is injective and equals F_X by Remark 5.10.

In particular, S_1 and Q=S_1^2+S_2^2 are nonzero polynomial elements in the semicircular free field and are units of U(M_0).
Also X_1^2+X_2^2 is a nonzero polynomial element of F_X and is invertible there, so (2) is a valid scalar rational expression.

## 3. Boundedness and Nonscalarity of the Rational Output

Let Q=S_1^2+S_2^2, a bounded positive operator of support 1, and put B_0=Q^{1/2}.
It is injective with dense range.
The inequality S_1^2<=Q lets us define a contraction on Ran B_0 by

\[
T_0(B_0\xi)=S_1\xi,
\qquad
\|S_1\xi\|^2\le\|B_0\xi\|^2.
\]

Injectivity makes the definition unambiguous.
Extend T_0 continuously to a contraction on L2(M_0).
For any unitary w in the commutant M_0', the defining identity gives `T_0 w=w T_0` on the dense range of B_0, hence everywhere.
Thus T_0 belongs to M_0.
With C=T_0*, the bounded identities are

\[
S_1=C^*B_0=B_0C,\qquad\|C\|\le1.
\tag{7}
\]

Inside the affiliated algebra, B_0 is a unit and B_0 Q^{-1} B_0=1.
This identity uses support(Q)=1; no bounded inverse of Q or B_0 has been assumed.
Associativity of the canonical affiliated products now gives

\[
g:=S_1Q^{-1}S_1
=C^*B_0Q^{-1}B_0C
=C^*C\in M_0,
\qquad 0\le g\le1.
\tag{8}
\]

In U(B), the central coordinate t is a unit because it is positive almost everywhere.
The constant-section affiliated copy of Q^{-1} is given by the same spectral calculus as in M_0.
Since t commutes with the constant operators, the two-sided inverse of t^2Q is Q^{-1}t^{-2}.
Therefore, using N=B,

\[
\begin{aligned}
f&=(tS_1)(t^2Q)^{-1}(tS_1)\\
 &=S_1Q^{-1}S_1=g,
\end{aligned}
\tag{9}
\]

as a constant bounded section.
Cancellation occurs in U(N), not by declaring t^{-1} bounded.
Formula (8) proves that f is a bounded positive contraction.

It is nonscalar.
If g=c1, then c cannot be zero: g is a product of units S_1,Q^{-1},S_1 in the embedded semicircular free field.
For c!=0, multiplying there by S_1^{-1} on both sides and taking inverses gives

\[
Q=c^{-1}S_1^2,
\qquad S_2^2=(c^{-1}-1)S_1^2.
\]

This contradicts injectivity of the polynomial evaluation for S, because the coefficient of x_2^2 in the resulting polynomial relation is one.
The argument works inside an already justified division ring and does not manipulate an undefined unbounded composition.

## 4. The Continuous-Section Obstruction

The map

\[
\iota:C([0,1],M_0)\longrightarrow B
\]

sending a norm-continuous section to its measurable restriction is an isometric unital *-homomorphism.
Its norm is the essential supremum of the fiber norms.
For a continuous section, each neighborhood on which its norm is close to its maximum has positive nu-measure by full support, including a neighborhood of zero intersected with (0,1].
The essential supremum therefore equals the supremum on [0,1].
In particular, the image of iota is norm-closed, and representatives are unique.

The set

\[
\mathcal E=\{a\in C([0,1],M_0):a(0)\in\mathbb C1\}
\]

is a closed unital *-subalgebra.
The sections tS_j lie in E and vanish at zero.
Hence

\[
C^*(X_1,X_2)\subseteq\iota(\mathcal E).
\tag{10}
\]

But the constant section g from (8) has nonscalar value at zero.
If its measurable class belonged to iota(E), injectivity of iota, applied to the difference from that constant continuous section, would force its continuous representative to be exactly g on all of [0,1].
This contradicts the definition of E.
Therefore

\[
f\notin C^*(X_1,X_2).
\tag{11}
\]

For clarity, bounded inverse closure of this C*-algebra is available at every matrix level.
If a belongs to a unital C*-subalgebra C of a unital C*-algebra M and is invertible in M, then h=a*a>=epsilon 1 for some epsilon>0.
For c=||a||^2,

\[
\|1-h/c\|\le1-\varepsilon/c<1.
\]

The Neumann series for h^{-1} converges in the norm-closed algebra C, and a^{-1}=h^{-1}a* belongs to C.
Apply the same argument in M_k(C) inside M_k(M) for every k.
Only this C*-algebra is norm-closed in the argument; no norm closure is inserted into the definition of R_X.

Taking C=C*(X) and M=N, this gives R_X subset C*(X).
The inclusion R_X subset F_X intersect N also follows because every admissible bounded scalar inverse remains an inverse in U(N).
Equation (11), together with f in F_X intersect N, proves the strict inclusion (3).

Finally suppose (4) held.
Every polynomial coefficient belongs to C*(X), and bounded invertibility of T(X) in M_k(N) puts T(X)^{-1} in M_k(C*(X)) by the matrix-level argument just proved.
Thus its entire scalar compression plus p(X) belongs to C*(X), contradicting (11).
The reasoning does not depend on size, linearity, minimality, a particular realization, or its formal domain at a scalar point.
It also works when p,u,T,v have entries anywhere in C*(X), as claimed.

## 5. Why the Original Bounded-Dual Hypothesis Fails

Suppose bounded D_i on L2(N) satisfied `[D_i,X_j]=delta_ij P_Omega`.
Since X_j is selfadjoint, the conversion checked in Dab10-U001 gives bounded selfadjoint source duals

\[
Y_i=-\frac{i}{2}(D_i-D_i^*),
\qquad[X_j,Y_i]=i\delta_{ij}P_\Omega.
\]

The audited Voi98 construction then supplies conjugate variables with

\[
\Phi^*(X_1,X_2)\le4\sum_{i=1}^2\|D_i\|^2<\infty.
\]

Dab10's accepted factoriality conclusion applies to these two selfadjoint generators with the faithful normal probability trace.
The required n>=2 restriction is satisfied.
It would make N a factor, contradicting Section 1.
Thus no bounded dual system of the required kind exists.
No assumption on D_i Omega was introduced.

This proof uses the source theorem with its precise restriction: the local omission of n>=2 in its Theorem 1 is addressed in Dab10-U001, and Theorem 13 explicitly includes that restriction and implies factoriality.
The conclusion here does not require a diffuse center, only the nontrivial one already proved for every full-support nu.

## Consequences, Checks, and Review Boundary

This example disproves the proposed universal implication from an affiliated free-field realization and a bounded rational output to a bounded matrix-inverse realization, and disproves the corresponding cross-ambient closure equality under those weaker hypotheses.
The obstruction concerns existence of every representation of the stated kind, rather than failure of a single chosen pencil.
It does not contradict [Yin_C_F0008](Yin_C_F0008_v1.md#yin_c_f0008): for the selfadjoint tuple, a bounded inverse realization would indeed suffice for scalar descent, but the example has none.
It also does not contradict Yin_C_F0005 or Yin_C_F0007, which assume bounded duals.

The full-support condition is used to obtain a nonconstant central parameter and an isometric continuous-section embedding.
Positivity t>0 almost everywhere is used in the relative commutant, the strong cutoff recovery, the scaled polynomial automorphisms, and the affiliated cancellation.
No uniform lower bound on t or a fiberwise inverse is assumed.
The probability and faithful trace hypotheses are retained wherever L2 convergence, conditional expectation, or finite affiliated invertibility is used.

Every local step above was reconstructed directly: the bounded convex-hull limit, all full-matrix quantifiers, the commutant-valued contraction, support-dependent cancellation, nonscalarity, continuous sections, inverse closure, and bounded-dual exclusion.
The external boundaries remain those declared in the linked MSY23, Miy22, Voi98 and Dab10 units.
The earlier exploration remains a historical draft and is not silently overwritten by this completed argument.

The linked independent audit covers this assembled proof and its exact scope.
No numerical computation, proof-assistant verification, external human review, or literature-priority assessment is claimed; those activities were not performed.


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
| argument | [Exact material](#1-recovering-the-center-and-the-whole-tensor-product) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0006_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:20 |
| status | proved |
| reason | Select the actual previously adopted finding explicitly, preserving its original date, complete checked mathematical scope and retained limits while declaring its actual known or genuinely unestablished relationship. The statement, argument, dependencies and mathematical assessment are unchanged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#1-recovering-the-center-and-the-whole-tensor-product) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Actual complete finding](../audits/reviews/Yin_R_F0006_v1.md#scaled-model-finding) | Complete scaled model: relative-commutant/factoriality calculation, center recovery and cutoff generation, fixed-matrix fiberwise affiliated invertibility, bounded contraction observation, continuous-section obstruction to every bounded inverse representation, and absence of bounded duals. No refutation of the original bounded-dual conjecture or Task completion. |

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

Review: [Exact material](../audits/reviews/Yin_R_F0006_v1.md).

Material covered by that review: [Exact material](Yin_C_F0011_v1.md).

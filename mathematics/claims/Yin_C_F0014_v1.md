---
author: Yin
---

# An L2 free-field element without a bounded weak-commutator extension

## Current assessment
[Selected decision](#decision-finding-owned-review)

## An L2 Rational Element without a Bounded Weak Commutator

<a id="yin_c_f0014"></a>
## Yin_C_F0014: The L2 Enlargement Still Requires a Different Rank Condition

Date: 2026-09-09.
Provenance: project deduction by the coordinating agent and another AI agent, prompted by the user's proposed affiliated and L2 extensions after [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001).
The original goal remains completed by refutation; this follow-up does not reopen or change its contract, and no successor goal is assigned by this note.
Initial assessment: complete proof draft awaiting independent review.
Current assessment: [selected assessment](#current-assessment); review evidence belongs to the [Yin_C_F0014 audit](../audits/reviews/Yin_R_F0008_v1.md).
No novelty claim is made.

## Statement

There exist two bounded selfadjoint generators $X=(h,Y)$ of a finite tracial von Neumann algebra $(M,\tau)$, a bounded dual system $(E_h,E_Y)$ on $H=L^2(M,\tau)$ with

\[
[E_i,X_j]=\delta_{ij}P_\Omega,
\]

and a selfadjoint affiliated element

\[
u\in F_X\cap L^2(M,\tau),\qquad
F_X=\operatorname{Div}_{U(M)}\mathbb C\langle h,Y\rangle,
\]

such that the weak commutator with $E_Y$, defined below on bounded vectors, has **no bounded operator representative on $H$**.
In particular, it has no bounded finite-rank representative.

Thus the equivalence

\[
u\in L^2(M),\qquad
u\in F_X
\quad\Longleftrightarrow\quad
\text{every weak dual commutator has a bounded finite-rank representative}
\]

is false under the original normal-generator and bounded-dual hypotheses.
The counterexample refutes its rationality-to-commutator implication, and uses precisely the tuple already constructed in [Yin_C_F0012](Yin_C_F0012_v1.md#yin_c_f0012).

## 1. A Precise Weak Commutator on L2

Use an inner product linear in its second argument.
Identify a bounded element $\xi\in M$ with its vector $\xi\Omega\in H$.
For any $v\in L^2(M,\tau)$, bounded $D\in B(H)$, and $\eta,\xi\in M$, define

\[
\mathcal B_D^v(\eta,\xi)
=\langle D^*\eta,v\xi\rangle
 -\langle v^*\eta,D\xi\rangle .
\tag{1}
\]

The products $v\xi$ and $v^*\eta$ belong to $L^2$, because right multiplication by a bounded element preserves $L^2$.
The vectors $D^*\eta,D\xi$ also belong to $H$.
Thus (1) is an everywhere-defined sesquilinear form on the dense vector space $M\times M$.

This definition does not require $D\xi$ to lie in $\operatorname{dom}(v)$.
A bounded representative means a bounded operator $T:H\to H$ such that

\[
\mathcal B_D^v(\eta,\xi)=\langle\eta,T\xi\rangle
\qquad(\eta,\xi\in M).
\tag{2}
\]

Such a representative is unique by density.
For $v\in M$, the bounded commutator $T=[D,v]$ satisfies (2), by the definition of the adjoint.
For unbounded $v$, (1) is a specified weak extension of that expression, rather than an assertion that the literal composition $vD$ is defined on $M$.

## 2. The Existing Tuple and Its Inverse Moments

Use [Yin_C_F0012](Yin_C_F0012_v1.md#yin_c_f0012) with

\[
A=L^\infty((0,1),4t^3dt),\qquad
h(t)=t,\qquad q=h^{-1},
\]

a variance-one standard semicircular $b$ free from $A$, and

\[
M=W^*(h,b)=W^*(h,Y),\qquad Y=hbh.
\]

The trace is faithful, normal, and tracial.
The element $h$ is positive, injective, and regular in $M$; $q$ is its inverse in the affiliated algebra $U(M)$.
Yin_C_F0012 supplies bounded duals and, in particular,

\[
E=E_Y\in B(H),\qquad [E,h]=0,\qquad [E,Y]=P_\Omega.
\tag{3}
\]

These are imported checked properties of the constructed tuple.
No new bounded-dual construction is asserted here.

The inverse moments give

\[
\|q\|_2^2=\int_0^1t^{-2}4t^3\,dt=2,
\qquad
\|q^2\|_2^2=\int_0^1t^{-4}4t^3\,dt=\infty.
\tag{4}
\]

In particular, $q$ is an $L^2$ vector but $q^2$ is not.
By (3), $E$ commutes with $h^2$; since $h^2$ is selfadjoint, taking adjoints also shows that $E^*$ commutes with $h^2$.

## 3. An Affiliated Rational Element that Belongs to L2

Define, with the closed affiliated products,

\[
u=qbq.
\tag{5}
\]

It is selfadjoint in $U(M)$, because taking the adjoint reverses the three selfadjoint factors and gives the same product.
Also

\[
b=qYq,\qquad u=q^2Yq^2,\qquad h^2uh^2=Y
\quad\text{in }U(M).
\tag{6}
\]

Since $h$ is regular, its affiliated inverse $q$ is admitted by the definition of $F_X$.
Formula (6) therefore proves $u\in F_X$ directly.
The additional identification of $F_X$ with an embedded free skew field uses the previously checked [Yin_C_F0005 source interface](Yin_C_F0005_v1.md#yin_c_f0005); the obstruction itself only needs this explicit valid rational expression.

Here is a bounded-truncation proof of $u\in L^2$.
For bounded $a,c\in A$, freeness and $\tau(b)=0$, $\tau(b^2)=1$ imply

\[
\|abc\|_2^2
=\tau(a^*a\,b\,cc^*b)
=\tau(a^*a)\tau(cc^*)
=\|a\|_2^2\|c\|_2^2.
\tag{7}
\]

For the middle equality, expand $a^*a$ and $cc^*$ into their scalar and centered parts.
The alternating centered term vanishes by freeness.
Each remaining term with one centered $A$ factor also vanishes, including the one paired with $b^2-\tau(b^2)1$.

Let $q_n=q1_{[1/n,1]}(h)\in A$.
These are bounded, $\|q_n-q\|_2\to0$, and their $L^2$ norms are bounded.
Applying (7) to the difference

\[
q_nbq_n-q_mbq_m=(q_n-q_m)bq_n+q_mb(q_n-q_m)
\]

gives

\[
\|q_nbq_n-q_mbq_m\|_2
\le(\|q_n\|_2+\|q_m\|_2)\|q_n-q_m\|_2.
\tag{8}
\]

Thus the bounded elements $q_nbq_n$ converge in $L^2$.
They also converge in measure to the affiliated product $qbq$: $q_n\to q$ in measure and multiplication is continuous in the measure topology of the finite tracial affiliated algebra.
Since $L^2$ convergence implies convergence in measure and the latter topology is Hausdorff, the two limits agree.
These measure-topology facts are standard affiliated-operator foundations, not new assertions about operator-norm convergence.
Equations (7)-(8) now give

\[
u\in L^2(M),\qquad
\|u\|_2^2=\|q\|_2^4=4.
\tag{9}
\]

The explicit standard model of Yin_C_F0012 gives an independent domain check: on its grade-zero vacuum, $q\Omega=q\in K=L^2(A)$, $bq\Omega=1\otimes q$, and left multiplication by $q$ gives $q\otimes q\in K\otimes K$.
Therefore $\Omega$ is in the domain of the literal three-factor composition in (5); its affiliated closure has $u\Omega=q\otimes q$ and the norm in (9).
Neither check uses a trace of an undefined product of unbounded operators.

## 4. A Bounded Weak Representative Would Force q Squared into L2

Suppose, toward a contradiction, that a bounded $T\in B(H)$ represents $\mathcal B_E^u$ in the sense of (2).
Take any $\eta,\xi\in M$.
Both $h^2\eta$ and $h^2\xi$ are again bounded test vectors.
Using (1), commutation of $E,E^*$ with $h^2$, and then moving only the bounded selfadjoint factor $h^2$ across inner products, gives

\[
\begin{aligned}
\mathcal B_E^u(h^2\eta,h^2\xi)
&=\langle E^*h^2\eta,uh^2\xi\rangle
  -\langle u^*h^2\eta,Eh^2\xi\rangle\\
&=\langle E^*\eta,h^2uh^2\xi\rangle
  -\langle h^2u^*h^2\eta,E\xi\rangle\\
&=\langle E^*\eta,Y\xi\rangle
  -\langle Y^*\eta,E\xi\rangle\\
&=\langle\eta,[E,Y]\xi\rangle
=\langle\eta,P_\Omega\xi\rangle.
\end{aligned}
\tag{10}
\]

Every product in the first two lines is an $L^2$ vector, since $u,u^*\in L^2$ and the remaining multiplication factors are bounded.
The equality $h^2uh^2=Y$ from (6) is consequently an equality of these $L^2$ vectors after application to the bounded $\xi$; the adjoint identity has the same justification.
The calculation does not apply $u$ to $E\xi$.

On the other hand, (2) gives

\[
\mathcal B_E^u(h^2\eta,h^2\xi)
=\langle\eta,h^2Th^2\xi\rangle.
\]

Density of $M$ in $H$, and boundedness of both operators being compared, imply

\[
h^2Th^2=P_\Omega
\quad\text{on }H.
\tag{11}
\]

Apply (11) to $\Omega$ and write $v=Th^2\Omega\in H$.
Then $h^2v=\Omega$.
Since $h^2$ is regular, its inverse in $U(M)$ is $q^2$.
Multiplying this equality in the affiliated algebra forces $v=q^2$.
Equivalently, the only possible solution to the multiplication equation $h^2v=1$ is $h^{-2}$.
This contradicts (4), because $v\in L^2$.

No bounded representative exists.
Finite rank was not used in the contradiction, so the failure is stronger than failure of a bounded finite-rank condition.
This proves the statement.

## Scope and Consequences

- The obstruction concerns a precise weak commutator tested on all bounded vectors, which agrees with the ordinary bounded commutator on $M$.
  It does not rely on an informal rank assigned to an unbounded product.
- If one instead studies the literal expression $Ev-vE$ on $\operatorname{dom}(v)\cap E^{-1}(\operatorname{dom}(v))$, the size, density, and graph properties of that common domain require separate analysis.
  Finite algebraic range there is a different condition; this note makes no equivalence claim for it.
- An $L^2$ rational output need not give $L^2$ derivative factors.
  In this example, the rational inverse/product rules give $\partial_Yu=q^2\otimes q^2$, while (4) excludes $q^2$ from $L^2$.
  This explains the mechanism, but the contradiction (10)-(11) proves it without representing that tensor as a bounded operator.
- The result does not refute a criterion formulated using bounded cleared-denominator defects for arbitrary affiliated elements.
  Those defects are the separate subject of [Yin_C_F0013](Yin_C_F0013_v1.md#yin_c_f0013).
- The argument supplies a checked-tuple counterexample to the proposed L2 equivalence, rather than a new counterexample to the already refuted original Yin_T_F0001.
  It makes no novelty assertion and requires no numerical computation.

## Verification Boundary

The proof uses Yin_C_F0012's already reviewed construction, elementary freeness, finite tracial affiliated-operator foundations, and Hilbert-space algebra with explicit domains.
The author checked the $L^2$ truncation estimate, the direct Fock-domain alternative, both denominator placements in (10), and the range obstruction in (11).
No new source proof audit, formal verification, numerical verification, or external human review is claimed.

On 2026-09-09, the mathematical agent whose preliminary suggestion was to test $qbq$ separately reviewed the complete written proof; the [Yin_C_F0014 audit](../audits/reviews/Yin_R_F0008_v1.md) discloses that involvement and the review scope.
It checked the weak form, both proofs of square integrability, the bounded denominator calculation, and the contradiction, and found no correction necessary.
This paragraph only integrates that later review evidence; it changes no mathematical statement or argument.
The [selected assessment](#current-assessment) records the mathematical and review assessments.


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
| argument | [Exact material](#1-a-precise-weak-commutator-on-l2) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0008_v1.md) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:32 |
| status | proved |
| reason | Select the exact retained finding with its actual relationship and original mathematical scope. The statement, argument, status, original review date and historical decisions remain unchanged; no new whole-proof review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#1-a-precise-weak-commutator-on-l2) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact review](../audits/reviews/Yin_R_F0008_v1.md#weak-commutator-obstruction-finding) | Complete rational L2 weak-commutator obstruction: actual bounded-dual model, both L2 arguments, bounded denominator/form calculation and no bounded representative on all bounded test vectors; no raw unbounded commutator convention or broader Task refutation. |

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

Review: [Exact material](../audits/reviews/Yin_R_F0008_v1.md).

Material covered by that review: [Exact material](Yin_C_F0014_v1.md).

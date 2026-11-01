---
author: Yin
---

# Entire inverse pencil in L1; conditional L2 control from bounded probes

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Bounded Dual Action on Rational States

<a id="statement"></a>

<a id="yin_c_f0010"></a>
## Yin_C_F0010: Integrability of the Entire Inverse from Bounded Probes

Goal: [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001).
Route: [Yin_S_F0005](../strategies/Yin_S_F0005.md#s_f0005).
Date: 2026-09-09.
Provenance: project deduction from [Yin_C_F0007](Yin_C_F0007_v1.md#yin_c_f0007), the bounded-dual relation, and finite-tracial noncommutative Holder inequalities.
Assessment: [selected assessment](#current-assessment); the [independent audit](../audits/reviews/Yin_R_F0005_v1.md) records the checked artifact and scope.
No novelty is asserted.

The bounded dual acts on the actual L2 states without any word expansion.
Varying a bounded right-hand probe supplies enough scalar vectors to show that the entire affiliated inverse pencil has L1 entries.
A specified stronger probe hypothesis supplies L2 entries.
Neither conclusion asserts boundedness.

### Statement and Dependencies

Let (M,tau) be a finite von Neumann algebra with a faithful normal tracial state, H=L2(M,tau), Omega=1, P=P_Omega, and U=U(M).
Let X_1,...,X_d belong to M, and let bounded operators D_i on H satisfy

\[
[D_i,\lambda(X_j)]=\delta_{ij}P.
\tag{D}
\]

Let A_i be n by n complex matrices, v a complex column, and suppose

\[
L=I_n-\sum_i A_iX_i\in M_n(M)
\]

is invertible in M_n(U).
Suppose the column h=L^{-1}v has L2 entries h_1,...,h_n which are linearly independent over C.
Then:

1. Every entry of L^{-1} lies in L1(M,tau).
2. If there are bounded probes a_1,...,a_n in M such that the scalar columns tau(ha_k) form a basis of C^n and D_i(a_k Omega) belongs to M inside H for every i,k, then every entry of L^{-1} lies in L2(M,tau).
3. A sufficient condition for the probe hypothesis in part 2 is that the X_i are selfadjoint, M=W*(X), and each eta_i=D_i Omega belongs to M.

The lemma itself does not require normality, generation, or rational minimality beyond its displayed assumptions.
Under the full Yin_C_F0001 assumptions, Yin_C_F0007 supplies affiliated invertibility, L2 membership and independence of h for its explicitly monic, reachable and observable representation of a bounded f with finite dual commutators.
Thus part 1 applies to that representation without a further hypothesis.
Parts 2 and 3 are conditional refinements.

We use H as its canonical subspace of U.
The bounded matrix L acts on H^n by left multiplication.
An identity in H between measurable operators is also an identity in U.
Products of two L2 elements are taken as affiliated products and belong to L1 by Holder; bounded left or right multiplication preserves L2 and L1.
These are the finite-tracial affiliated-operator foundations already used by Yin_C_F0007.
None of the steps below defines D_i on an affiliated element outside H.

### 1. A Probe Identity in H, then in U

Fix a in M and write D_i diagonally on H^n.
Because ha belongs to H^n, all terms in

\[
L(ha)=va,\qquad [D_i,L]=-A_iP
\]

are well-defined Hilbert-space operations.
Applying bounded D_i to the first equality gives

\[
L D_i(ha)=vD_i(a)+A_i\tau(ha).
\tag{1}
\]

Here D_i(a) abbreviates D_i(a Omega), and tau(ha) is the componentwise scalar trace.
Only the bounded operators D_i and L have acted on vectors so far.

Now interpret (1) in U^n and multiply there by L^{-1}.
Associativity of affiliated products and the equality L^{-1}v=h give

\[
\boxed{L^{-1}A_i\tau(ha)=D_i(ha)-hD_i(a).}
\tag{2}
\]

The right-hand side is in L1: the first summand is L2 and tau(1)=1; the second is a product of two L2 elements.
No assertion that hD_i(a) belongs to H was used to multiply by L^{-1}.
In particular, (2) is initially an affiliated identity, not an unproved Hilbert-space inverse-domain identity.

For each row j, the explicit bound is

\[
\big\|(L^{-1}A_i\tau(ha))_j\big\|_1
\le \|D_i\|\,\|h_j\|_2
       \bigl(\|a\|_\infty+\|a\|_2\bigr).
\tag{3}
\]

It follows by bounding D_i(h_j a) in L2 and h_j D_i(a) in L1.
This estimate is for a fixed probe; choosing a basis of probes can introduce its finite-dimensional conditioning constant.

### 2. Separating the States and Recovering the Entire Inverse

The complex-linear map

\[
T:M\longrightarrow\mathbb C^n,\qquad T(a)=\tau(ha)
\]

is onto.
Indeed, if a scalar row c annihilates its range, then k=sum_j c_j h_j belongs to L2 and tau(ka)=0 for every a in M.
Choose bounded a approaching k* in L2.
Holder continuity then gives tau(kk*)=0, so k=0.
Independence of the h_j gives c=0.
The finite-dimensional range of T therefore has trivial annihilator and is all of C^n.

Choose bounded a_k with T(a_k)=e_k.
Formula (2) says that every column L^{-1}A_i e_k belongs to L1.
Finally,

\[
L^{-1}=I_n+\sum_i(L^{-1}A_i)X_i.
\tag{4}
\]

Right multiplication by each bounded X_i preserves L1, proving part 1.
Independence is essential to this particular proof: without it, the available probes need not detect all constant state directions.

### 3. The Conditional L2 Improvement

Under part 2's probe hypothesis, D_i(ha_k) is in L2 and hD_i(a_k) is in L2 because D_i(a_k) is bounded.
Hence (2) puts L^{-1}A_i T(a_k) in L2.
As the T(a_k) form a scalar basis, all columns of L^{-1}A_i are L2.
Equation (4) proves the L2 assertion for L^{-1}.

For part 3, [Yin_C_F0002's vacuum formula](Yin_C_F0002_v1.md#yin_c_f0002) gives, for every polynomial p in the generators,

\[
D_i(p(X)\Omega)
=p(X)\eta_i+
  \bigl((\mathrm{id}\otimes\tau)(\partial_i p)(X)\bigr)\Omega.
\tag{5}
\]

Both terms are bounded elements when eta_i belongs to M.
If the generators are selfadjoint and generate M, their polynomial algebra is a unital star algebra dense in H.
The trace-annihilator argument from section 2 therefore proves that the columns tau(hp(X)) span C^n.
Select finitely many such polynomial probes forming a basis; (5) verifies the required bounded images under every D_i.

For a general normal tuple, the holomorphic polynomial algebra need not be L2-dense or separate the states.
Boundedness of eta_i alone does not establish part 2's probe hypothesis in that setting.
Nor does the dual relation (D) give a prescribed polynomial formula on arbitrary adjoints X_j*.
No unconditional L2 conclusion is drawn from part 3.

### 4. Why the Vacuum Term Cannot Be Removed Automatically

Taking only a=1 in (2) gives

\[
L^{-1}A_i\tau(h)=D_i h-h\eta_i,
\qquad \eta_i=D_i\Omega\in L^2.
\tag{6}
\]

The last product is generally only known to be L1.
The following example shows that one cannot repair this by assuming every bounded dual can be chosen to annihilate Omega, or even to send Omega to a bounded element.

Let M=L_infinity((0,1),dx), tau be integration, and X(x)=x.
Let E:L2(0,1) to L2(R) be zero extension, and let the normalized Hilbert transform be

\[
(\mathcal H\xi)(x)
=\frac1\pi\operatorname{p.v.}\int_{\mathbb R}
            \frac{\xi(y)}{x-y}\,dy.
\]

The primary input is the L2 extension with Fourier multiplier -i sgn(xi), hence norm 1, in [Tao06, Proposition 1.2 and the following L2 discussion, pp. 3-4](https://www.math.ucla.edu/~tao/247a.1.06f/notes4.pdf).
This is also part of the already accepted [Voi98-U002 Hilbert-transform interface](../audits/literature/Voi98/Yin_U002.md#voi98-u002).
Set

\[
D=-\pi E^*\mathcal H E.
\]

Then ||D||<=pi.
On smooth functions compactly supported in (0,1), its integral kernel is 1/(y-x), and cancellation gives

\[
([D,X]\xi)(x)=\int_0^1\xi(y)\,dy.
\]

Density and boundedness extend this to [D,X]=P on H.
Direct principal-value integration gives

\[
\eta(x)=D\Omega(x)=\log\frac{1-x}{x}\in L^2(0,1)\setminus L^\infty(0,1).
\tag{7}
\]

For the identification in H, the usual symmetric truncations defining the L2 Hilbert transform converge in L2, as stated in Tao06 immediately after Proposition 1.2.
The interval calculation is also explicit: away from the two epsilon-end intervals the truncated expression is already (7); its error on (0,epsilon) is log(x/epsilon), with squared integral 2 epsilon, and there is the symmetric error at the other endpoint.
Thus the displayed principal value has exactly the asserted L2 representative.
The accepted external input is the Hilbert-transform L2/truncation theorem, not a claimed audit of the full Calderon-Zygmund theory.

If D' is any other bounded dual for X, then D'-D commutes with this selfadjoint multiplication operator.
Its spectral projections generate the multiplicity-one multiplication algebra M, whose commutant on H is M itself.
Thus D'-D is multiplication by a bounded b, and

\[
D'\Omega=\eta+b
\]

is still unbounded.
In particular, no bounded dual for this X annihilates Omega.
This is a boundary example for the auxiliary normalization step; the original single-generator conjecture is already settled by Yin_C_F0004.

There is a separate loss of information if one uses only vacuum probes even when a normalized dual exists.
For a Haar unitary U and its bounded positive-terminal-deletion dual D, D Omega=0.
The bounded rational function

\[
h=(1-2U)^{-1}=-\sum_{m\ge1}2^{-m}U^{-m}
\]

satisfies tau(h)=0 and Dh=0, and every further iterate of D on h is zero.
Nevertheless h is nonconstant.
The series converges in operator norm, and the dual deletes only positive terminal letters, so the assertion follows termwise by boundedness of D; the exact Haar dual convention is checked in [MSY23-U005](../audits/literature/MSY23/Yin_U005.md#msy23-u005).
This concerns D acting on a state vector; it is not a statement that the commutator [D,h] vanishes.
Bounded probes such as a=U recover nonzero tau(ha), which explains the role of varying a in (2).

### Remaining Obligations and Review Scope

Part 1 improves Yin_C_F0007's control of a selected row and column to entrywise L1 control of the whole inverse.
The improvement is in the extent of the matrix controlled, not an increase from L2 to a stronger norm.
The conditional part supplies L2 control of that matrix.
Neither proves a lower bound for L, a bounded inverse, or bounded scalar elimination.
Rational L2 elements can still be unbounded under the original normal bounded-dual assumptions, as shown by Yin_C_F0007's weighted-disk boundary example.

The first attempted vacuum recurrence fails to control the product h eta_i in L2 in general; section 4 explains why its normalization premise is not automatic.
The bounded-probe identity survives that obstruction and yields the L1 lemma.
A further quantitative estimate would have to control enough probes in a stronger operator norm, or use a different realization mechanism.
No word-basis orthogonality, free independence, Fock coefficient estimate, or unrestricted differentiation of affiliated elements has been assumed.

The preparer reconstructed (1)-(5), the trace-separation step and both boundary examples.
Before this file was drafted, the coordinating agent independently checked the H-to-U passage, Holder step, probe surjectivity and conditional polynomial-density argument in discussion.
The linked independent audit reviews the completed artifact and rechecks the exact Tao06 source interface.
No numerical experiment, formal verification or external human review is claimed.


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
| argument | [Exact material](#1-a-probe-identity-in-h-then-in-u) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0005_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

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
| argument | [Exact material](#1-a-probe-identity-in-h-then-in-u) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Actual complete finding](../audits/reviews/Yin_R_F0005_v1.md#bounded-probe-finding) | Complete bounded probe identity, unconditional whole-inverse L1 consequence, conditional L2 upgrade, selfadjoint bounded-vacuum sufficient probes, exact interval nonnormalizability and Haar probe boundary. Retains the actual Tao06 primary-text inspection depth; no Lp-to-bounded or scalar elimination conclusion. |

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

Review: [Exact material](../audits/reviews/Yin_R_F0005_v1.md).

Material covered by that review: [Exact material](Yin_C_F0010_v1.md).

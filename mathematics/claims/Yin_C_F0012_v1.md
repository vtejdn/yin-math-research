---
author: Yin
---

# Selfadjoint sandwich counterexample with bounded duals and finite commutators

## Current assessment
[Selected decision](#decision-isolated-main-and-bh-review-adoption)

## A Selfadjoint Sandwich Tuple with Bounded Duals

<a id="statement"></a>

<a id="yin_c_f0012"></a>
## Yin_C_F0012: Counterexample to the Bounded Scalar Criterion

Goal: [Yin_T_F0001](../tasks/Yin_T_F0001_v1.md#yin_t_f0001).
Date: 2026-09-09.
Provenance: project deduction by another AI agent and the coordinating agent.
The [new main-example finding](../audits/reviews/Yin_R_F0056_v1.md#main-counterexample-finding) supplies the actual current isolated inspection of the main statement and Sections 1–7.
The older [main-example finding](../audits/reviews/Yin_R_F0082_v1.md#main-counterexample-finding), [contributor integration](../audits/reviews/Yin_R_F0007_v1.md#verification-facts-and-outcome), and [proof-first core recheck](../audits/reviews/Yin_R_F0082_v1.md#5-generation-and-review-boundary) retain their exact historical mathematical coverage and declared relationships.
The main-example and core recheck arrangements do not establish isolated mathematical contexts; the integration reviewer contributed complementary mathematical checks, and the bh extension retains its original disclosed contributor review.
The [new isolated bh finding](../audits/reviews/Yin_R_F0082_v1.md#current-bh-extension) separately covers the complete optional Section8, including both exact rank-one commutators and scalar nonmembership.
Assessment: [selected assessment](#current-assessment); the [original-contract contributor audit](../audits/reviews/Yin_R_F0054_v1.md#completion-finding-and-verification-boundaries) records the original milestone consequence for Yin_T_F0001.
No novelty claim is made.

The tuple constructed below consists of two bounded selfadjoint generators with a bounded dual system.
A bounded selfadjoint element has finite-rank commutators with both duals and belongs to the affiliated division closure, but is outside the norm-closed C*-algebra of those generators.
Since that C*-algebra is inverse closed in M, the element is outside the scalar division closure in M requested by Yin_C_F0001.

## Statement of the Construction

Let A=L-infinity((0,1),mu), where

\[
d\mu(t)=4t^3\,dt,
\qquad h(t)=t,
\qquad q(t)=t^{-1}.
\]

Let b be a variance-one standard semicircular element free from A, and let M=W*(h,b), with its faithful normal free-product trace tau.
The explicit standard tracial model is constructed below.
Set

\[
Y=hbh,\qquad f=b.
\]

Then h,Y are bounded selfadjoint, W*(h,Y)=M, and there are bounded operators E_h,E_Y on L2(M,tau) satisfying

\[
[E_h,h]=P,\qquad [E_h,Y]=0,
\qquad [E_Y,h]=0,\qquad [E_Y,Y]=P.
\tag{1}
\]

Here P is the projection onto Omega=1 and operators in M act by left multiplication.
Their commutators with b are

\[
[E_Y,b]=\Theta(q\otimes q),
\qquad
[E_h,b]=-\Theta(b\otimes q+q\otimes b),
\tag{2}
\]

of ranks one and two respectively.
Nevertheless

\[
b\notin C^*(h,Y),
\qquad
b\notin\operatorname{Div}_M\mathbb C\langle h,Y\rangle.
\tag{3}
\]

The rank-one convention is Theta(g tensor k)xi=g< Jk,xi>.
Both q and b are selfadjoint L2 vectors, so these are ordinary rank-one operators, not products of bounded multipliers by the unbounded q.
Every appearance of q below as a rank-one vector or Hilbert tensor uses q in L2; q is never asserted to be a bounded multiplier.

## 1. An Explicit Tracial Fock Model

Put K=L2(A,mu), with Omega_A=1, and let

\[
\mathcal H=\bigoplus_{n=0}^{\infty} K^{\otimes(n+1)},
\qquad \mathcal H_n=K^{\otimes(n+1)}.
\tag{4}
\]

These are Hilbert tensor products.
The vacuum is Omega_A in grade zero.
An element a of A acts by multiplication on the first tensor factor of every grade.
Define the isometry ell by prepending Omega_A:

\[
\ell(\xi_0\otimes\cdots\otimes\xi_n)
=1\otimes\xi_0\otimes\cdots\otimes\xi_n.
\]

Its adjoint is zero on grade zero and, for n>=1, is

\[
\ell^*(\xi_0\otimes\cdots\otimes\xi_n)
=\tau_A(\xi_0)\,\xi_1\otimes\cdots\otimes\xi_n.
\]

Set b=ell+ell*.
Then b is bounded selfadjoint, with norm 2 and standard semicircular vacuum distribution: the subspace spanned by 1 in every grade is the ordinary unilateral semicircular Jacobi model.
In particular, tau(b)=0 and tau(b^2)=1.

For completeness, freeness and the tracial standard representation can be verified directly in this model.
Let W_0=1, W_1(x)=x and W_{m+1}(x)=xW_m(x)-W_{m-1}(x).
If ell*xi=0, induction gives W_m(b)xi=ell^m xi.
A centered A element changes a leading 1 to a vector orthogonal to 1; a centered polynomial in b is a linear combination of W_m(b), m>=1, and prepends positive strings of 1 to such a vector.
Thus alternating centered A elements and centered b polynomials have zero vacuum expectation.
This proves freeness.

The vacuum is cyclic for A and b: on elementary tensors with bounded factors, a_0 b a_1 ... b a_n Omega has highest-grade term a_0 tensor ... tensor a_n, with all other terms in lower grades.
Induction on n gives a dense set of all elementary tensors.

There is also an explicit commuting right action.
Right multiplication by a in A acts on the last tensor factor; write this bounded operator as rho(a).
Let r append 1 on the right, and set rho(b)=r+r*.
Left A commutes with these right operators, and b commutes with rho(a).
The possible grade-zero commutators [ell*,r]=P and [ell,r*]=-P cancel, while [ell,r]=[ell*,r*]=0.
Hence b commutes with rho(b).
The mirrored elementary-tensor argument makes the right vacuum orbit dense, so Omega is separating for M=W*(A,b).

The antiunitary that reverses the tensor factors and takes their complex conjugates sends the left generators to their corresponding adjoint right generators.
Consequently JxOmega=x*Omega on the polynomial algebra, so ||xOmega||=||x*Omega|| there.
Polarization gives the trace identity; normal extension to M gives a faithful normal tracial state tau(x)=<Omega,xOmega>.
Therefore this is the standard L2(M,tau) representation.
The right operators above are precisely rho(a):xi maps to xi a: they commute with the left algebra and have the correct action on Omega.
No unproved change of Hilbert norm is used in the construction below.

Since h is the coordinate function, W*(h)=A.
Thus M=W*(h,b) in the stated model.
The element h is positive and regular, with spectrum [0,1], and

\[
\tau(1_{(0,\epsilon]}(h))=\epsilon^4,
\qquad \|q\|_2^2=\int_0^1 4t\,dt=2.
\tag{5}
\]

Its affiliated inverse q is unbounded.

## 2. A Bounded Last-Two-Factor Operator

Define the real kernel on (0,1)^2

\[
F(s,t)=\frac{1}{st}\,1_{\{t\le s\}}.
\tag{6}
\]

For almost every s,

\[
\int_0^1|F(s,t)|^2\,d\mu(t)
=\frac4{s^2}\int_0^s t\,dt=2.
\tag{7}
\]

Consequently the operator T:K tensor K to K defined by

\[
(T\zeta)(s)=\int_0^1F(s,t)\zeta(s,t)\,d\mu(t)
\tag{8}
\]

is bounded, of norm at most sqrt(2).
This follows by Cauchy-Schwarz in t and integration in s.
It commutes with multiplication on the first factor, in the sense T((a tensor 1)zeta)=aTzeta.

Define a bounded operator R on the direct sum (4): it is zero on grade zero, and on grade n>=1 it acts on the last two factors by T,

\[
R|_{\mathcal H_n}=I_K^{\otimes(n-1)}\otimes T.
\tag{9}
\]

The output belongs to grade n-1.
Since the grade ranges are orthogonal, ||R||<=sqrt(2).
The first-factor module property of T handles grade one, and the untouched first factor handles all higher grades; therefore R commutes with left A.
The same is true for R*, since A is a star algebra.

Let K_F:K to K be the integral operator with kernel F.
The following commutators are exact:

\[
[R,\ell]=K_F\oplus0\oplus0\oplus\cdots,
\qquad [R,\ell^*]=0.
\tag{10}
\]

For the first identity, on grade zero, R ell xi=T(1 tensor xi)=K_F xi, while ell R xi=0.
On every positive grade, prepending 1 and applying T to the last two factors commute.
For the second identity, both compositions vanish on grades zero and one.
Starting at grade two, the first-factor contraction and the last-two-factor operator act on distinct factors, including the grade-two case, and hence commute.
These checks on elementary tensors extend to all of H by boundedness.

The measure is nonatomic, so the diagonal in (0,1)^2 is null and

\[
F(s,t)+\overline{F(t,s)}=q(s)q(t)
\quad\text{almost everywhere}.
\tag{11}
\]

The kernels are L2: (7) integrates to ||F||_2^2=2.
Thus (11) is an equality of Hilbert-Schmidt kernels and gives K_F+K_F*=|q><q| on grade zero.
Set

\[
K_0=R-R^*.
\tag{12}
\]

It is bounded, ||K_0||<=2sqrt(2), and commutes with h.
Since b is selfadjoint, (10) gives [R*,b]=-[R,b]*.
Therefore

\[
[K_0,b]=\Theta(q\otimes q)
\tag{13}
\]

on the whole Fock space, with the rank-one operator supported on grade zero.
This construction uses bounded maps between Hilbert tensor grades; it does not sandwich an operator between the unbounded right multipliers rho(q).

Because K_0 commutes with h and hq=1 as an L2 identity,

\[
[K_0,Y]=h[K_0,b]h=P.
\tag{14}
\]

Thus E_Y=K_0 already supplies the dual for Y while commuting exactly with h.

## 3. A Bounded Dual for h and Its Bounded Correction

First construct a scalar bounded dual D_0 for h on K.
The finite-interval Hilbert transform with kernel 1/(t-s) is bounded on unweighted L2(0,1), with norm at most pi.
Its normalization and L2 extension are the [Tao06 interface rechecked in the Yin_C_F0010 audit](../audits/reviews/Yin_R_F0005_v1.md).
With w(t)=4t^3 and the unitary W:K to L2(0,1,dt), Wxi=sqrt(w)xi, define

\[
D_0=W^{-1}M_{\sqrt w}\,\mathcal T\,M_{\sqrt w}W,
\tag{15}
\]

where T has the unnormalized kernel 1/(t-s).
Then ||D_0||<=4pi.
On smooth functions supported away from the endpoints it has the principal-value kernel

\[
(D_0\xi)(s)=\operatorname{p.v.}\int_0^1
               \frac{\xi(t)}{t-s}\,d\mu(t),
\]

and cancellation gives [D_0,h]=P_{Omega_A}.
Density and boundedness extend this identity to K.
No boundedness of D_0Omega_A is required.

Extend D_0 to the whole Fock space by acting on the last factor of every grade:

\[
\widehat D_h|_{\mathcal H_n}=I_K^{\otimes n}\otimes D_0.
\tag{16}
\]

It is bounded with norm at most 4pi.
On grade zero its commutator with h is P_{Omega_A}; on every positive grade the first-factor h and last-factor D_0 commute.
Hence

\[
[\widehat D_h,h]=P.
\]

It commutes with ell and ell*: prepending 1 leaves the last factor unchanged, and contracting the first factor leaves the last D_0 action unchanged.
At grade one, both orders give tau_A(xi_0)D_0 xi_1; at grade zero both compositions with ell* vanish.
Thus

\[
[\widehat D_h,b]=0.
\tag{17}
\]

All right multiplication operators used next are bounded because hb and bh belong to M.
Define

\[
E_h=\widehat D_h-\rho(hb)K_0-K_0\rho(bh),
\qquad E_Y=K_0.
\tag{18}
\]

For example ||E_h||<=4pi+8sqrt(2), using ||h||=1 and ||b||=2.
Right multiplication commutes with left M.
Equations (14) and (17) therefore give

\[
\begin{aligned}
[E_h,h]&=P,\\
[\widehat D_h,Y]&=Pbh+hbP,\\
[\rho(hb)K_0,Y]&=\rho(hb)P=hbP,\\
[K_0\rho(bh),Y]&=P\rho(bh)=Pbh.
\end{aligned}
\]

The right/left vacuum identities in the last two lines follow from rho(hb)Omega=hbOmega and traciality, respectively.
They prove [E_h,Y]=0.
Together with (14), this proves the complete dual system (1) using only bounded operators.

## 4. The Actual Commutators with the Bounded Element b

Equation (13) already gives the first formula in (2).
Using (17), (18), and the fact that right multiplication commutes with left b,

\[
[E_h,b]=-\rho(hb)\Theta(q\otimes q)
        -\Theta(q\otimes q)\rho(bh).
\]

The first right multiplier takes the vector q to qhb=b.
For the second term, cyclicity of the trace and hq=1 give tau(q xi bh)=tau(b xi), initially on a bounded dense domain and then by the continuous L2 pairings.
Hence the preceding identity is exactly

\[
[E_h,b]=-\Theta(b\otimes q+q\otimes b).
\]

The vector q lies in grade zero, while bOmega=1 tensor 1 lies in grade one.
They are nonzero and orthogonal, so the two-term operator has rank two.
The first commutator has rank one.
These are direct bounded-operator calculations with f=b, not conclusions inferred solely from formal rational derivatives.

## 5. The Tuple Generates M

Certainly N=W*(h,Y) is contained in M.
For epsilon>0, let \(z_\epsilon=1_{[\epsilon,1]}(h)\) and \(a_\epsilon=h^{-1}z_\epsilon\).
Both are bounded Borel functions of h and belong to N.
Then

\[
a_\epsilon Y a_\epsilon=z_\epsilon b z_\epsilon\in N.
\]

These operators have norm at most 2.
The projections z_epsilon converge strongly to 1 because h has no zero spectral projection.
Hence z_epsilon b z_epsilon converges strongly to b, proving b in N and N=M.
This generation argument uses only bounded functional calculus and bounded products.
Thus the dual system just constructed acts on precisely the standard tracial space required for the generated algebra of the tuple.

## 6. Exclusion from the Norm-Closed and Scalar Division Algebras

Let 0<epsilon<1 and put

\[
e_\epsilon=1_{(0,\epsilon]}(h),\qquad
\xi_\epsilon=e_\epsilon\Omega/\sqrt{\tau(e_\epsilon)}.
\]

These are unit vectors, since tau(e_epsilon)=epsilon^4>0.
They satisfy

\[
\|h\xi_\epsilon\|\le\epsilon,
\qquad
\|Y\xi_\epsilon\|\le2\epsilon.
\tag{19}
\]

For every nonconstant word in h,Y, its rightmost generator therefore sends xi_epsilon to a vector tending to zero; the remaining fixed bounded factors preserve that convergence.
Consequently, for every polynomial p in h,Y with constant coefficient c=p(0,0),

\[
\|(p(h,Y)-c)\xi_\epsilon\|\longrightarrow0.
\tag{20}
\]

Freeness of A and b, traciality, and the standard semicircular moments give

\[
\langle\xi_\epsilon,b\xi_\epsilon\rangle=0,
\qquad
\|b\xi_\epsilon\|^2
=\frac{\tau(e_\epsilon b^2 e_\epsilon)}{\tau(e_\epsilon)}
=\tau(b^2)=1.
\tag{21}
\]

Equations (20)-(21) imply

\[
\|b-p(h,Y)\|
\ge\limsup_{\epsilon\downarrow0}
       \|(b-p(h,Y))\xi_\epsilon\|
=\sqrt{1+|c|^2}\ge1.
\tag{22}
\]

Because h,Y are selfadjoint, their noncommutative polynomial algebra is already a star algebra.
Its norm closure is C*(h,Y), so (22) proves b is outside that C*-algebra.

The unital C*-subalgebra C*(h,Y) is inverse closed in M.
One can verify the only needed fact directly: if a in this C*-algebra is a unit of M, then a*a>=delta 1 for some delta>0.
After scalar rescaling, the Neumann series for (a*a)^{-1} converges in the same C*-algebra; then a^{-1}=(a*a)^{-1}a* lies there as well.
Thus this C*-algebra contains the scalar division closure in M of C<h,Y>.
Equation (22) proves (3).

## 7. The Monic Two-State Form and the Original Conjecture

If a monic scalar-origin chart is desired, replace h by X=1-h.
This preserves selfadjointness, the generated algebra, and the scalar polynomial/division closures, since h=1-X.
The transformed duals are D_X=-E_h and D_Y=E_Y.
They satisfy [D_X,X]=P, [D_X,Y]=0, [D_Y,X]=0 and [D_Y,Y]=P.

In these coordinates the bounded element b has the minimal two-state representation

\[
b=(1,0)
\begin{pmatrix}1-X&-Y\\0&1-X\end{pmatrix}^{-1}
\binom01,
\qquad A_X=I_2,\quad A_Y=E_{12}.
\]

Reachability follows from e_2 and E_12 e_2=e_1; observability follows from e_1^T and e_1^T E_12=e_2^T.
The inverse matrix has diagonal entries q, which are L2 but unbounded, and upper-right entry b.
This verifies the hidden-state phenomenon under the actual dual hypotheses, rather than using a nonminimal unused block.
The exact commutator ranks are two for X and one for Y, in agreement with Yin_C_F0007.

More decisively, section 6 excludes every bounded scalar rational expression in the original generators, not only boundedness of this chosen inverse.
Thus the tuple (h,Y), or equivalently (X,Y), refutes the finite-rank-to-bounded-scalar-division implication of the original Yin_C_F0001 while preserving all its normality, trace, generation, and bounded-dual assumptions.
The affiliated conclusion Yin_C_F0005 and the L2-state results Yin_C_F0007/Yin_C_F0010 remain consistent with the example.

## 8. A Two-State Counterexample with Both Commutator Ranks Equal to One

The same tuple and duals also handle the sharper one-sided fraction

\[
f_1=bh=(1-X)^{-1}Y.
\]

It is bounded.
Using D_X=-E_h, equations (1)-(2), and the product commutator rule,

\[
\begin{aligned}
[D_X,bh]
&=\Theta(b\otimes q+q\otimes b)h-bP
 =\Theta(q\otimes bh),\\
[D_Y,bh]&=\Theta(q\otimes q)h=\Theta(q\otimes1).
\end{aligned}
\tag{23}
\]

The first operator is |q><hb| under the stated Theta convention.
Both ranks are one; the two right vectors are nonzero.
These are actual bounded-operator identities, with the canceling bP term displayed.

To prove nonmembership, test f_1*=hb on the same vectors xi_epsilon.
Its mean is zero, and freeness gives

\[
\|hb\xi_\epsilon\|^2
=\frac{\tau(e_\epsilon b h^2 b e_\epsilon)}{\tau(e_\epsilon)}
=\tau(h^2)=\frac23.
\tag{24}
\]

For the middle equality, write h^2 and e_epsilon as their scalar traces plus centered A elements.
Alternating centered freeness, tau(b)=0 and tau(b^2)=1 leave exactly tau(e_epsilon)tau(h^2).
The same argument gives <xi_epsilon,hb xi_epsilon>=0.
Thus (20) yields

\[
\operatorname{dist}(hb,C^*(h,Y))\ge\sqrt{2/3}.
\]

The C*-algebra is closed under adjoints, so the same distance bound holds for bh.
In particular f_1 is outside R_X=Div_M C<X,Y>=Div_M C<h,Y>.

Its monic two-state pencil is

\[
B_1=\begin{pmatrix}1-X&-Y\\0&1\end{pmatrix},
\qquad
B_1^{-1}=\begin{pmatrix}q&bh\\0&1\end{pmatrix},
\qquad A_X=E_{11},\quad A_Y=E_{12}.
\]

With u=e_1^T and v=e_2, it is reachable and observable by the same E_12 calculation.
It therefore realizes the rank-one common-image two-variable case in the [two-state exploration](../ledger/Yin_L_F0015_v1.md), with total commutator rank two.
This strengthening was proposed independently by another AI agent and checked by the coordinating agent and the artifact author.
Its actual identities and norm exclusion are included here for review together with the main example.

## Verification Boundary

The Fock realization, merging operator, bounded dual correction, actual commutators and C*-distance argument are reconstructed here.
The only analytic source input beyond the standard finite-tracial affiliated algebra is the classical L2 Hilbert-transform bound, with its normalization already checked in Yin_C_F0010's audit.
No boundedness of an unbounded-multiplier sandwich, no formal-to-operator convergence assertion for b's rational formula, and no unverified bounded-dual transfer is assumed.
The linked independent reviews and original-contract audit support the recorded refutation of Yin_C_F0001.
No numerical experiment, proof assistant, external human review, historical priority assessment, or novelty claim is made.


## Assessment history


### Decision finding-scopes

| Field | Value |
| --- | --- |
| date | 2026-10-20T21:28 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Original statement](#statement) | The original h,hbh bounded-dual counterexample, standard finite-tracial space, ranks and scalar nonmembership remain unchanged. |
| argument | [Complete argument](#1-an-explicit-tracial-fock-model) | Original sections 1-8, including standard model, bounded operators, every dual relation, generation and norm exclusion; optional bh strengthening retains its distinct contributor evidence. |
| review | [Finding](../audits/reviews/Yin_R_F0082_v1.md#main-counterexample-finding) | Original full main-example review, sections 1-7; noncontribution is recorded but context isolation remains unknown, and no current independence is inferred. |
| review | [Finding](../audits/reviews/Yin_R_F0082_v1.md#6-the-one-sided-strengthening-and-the-goal-contract) | Original review of the same reviewer's bh contribution, self-reviewed at its exact optional scope. |
| review | [Finding](../audits/reviews/Yin_R_F0007_v1.md#verification-facts-and-outcome) | Original complete contributor integration review, self-reviewed with the earlier mathematical checks disclosed. |
| review | [Finding](../audits/reviews/Yin_R_F0082_v1.md#5-generation-and-review-boundary) | Original proof-first core and generation recheck, excluding nonmembership and full Task assessment; context isolation remains unknown. |
| review | [Finding](../audits/reviews/Yin_R_F0054_v1.md#completion-finding-and-verification-boundaries) | Original complete coordinating contributor audit of the exact counterexample and original-contract interface; no new mathematical inspection date or independent certification. |


### Decision isolated-main-review-adoption

Adopt the actual new isolated main-example inspection while preserving the optional Section 8 extension's separate contributor and unresolved historical-context scopes.
The mathematical statement, complete argument and all historical decisions remain unchanged; no aggregate independent verdict is assigned.

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:42 |
| status | proved |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Original statement](#statement) | The original h,hbh bounded-dual counterexample, standard finite-tracial space, ranks and scalar nonmembership remain unchanged. |
| argument | [Complete argument](#1-an-explicit-tracial-fock-model) | Original sections 1-8, including standard model, bounded operators, every dual relation, generation and norm exclusion; optional bh strengthening retains its distinct contributor evidence. |
| review | [New isolated main finding](../audits/reviews/Yin_R_F0056_v1.md#main-counterexample-finding) | Actual new complete independent inspection of the unchanged main statement and Sections 1–7, with exact original-contract and source interfaces; Section 8 is expressly excluded. |
| review | [Finding](../audits/reviews/Yin_R_F0082_v1.md#6-the-one-sided-strengthening-and-the-goal-contract) | Original review of the same reviewer's bh contribution, self-reviewed at its exact optional scope. |
| review | [Finding](../audits/reviews/Yin_R_F0007_v1.md#verification-facts-and-outcome) | Original complete contributor integration review, self-reviewed with the earlier mathematical checks disclosed. |
| review | [Original core and commutator finding](../audits/reviews/Yin_R_F0082_v1.md#5-generation-and-review-boundary) | Original Sections 1–5 core/generation and Section 8 commutator refinement only; nonmembership, optional minimal representations and full Task assessment are excluded, and historical context isolation remains unknown. |
| review | [Finding](../audits/reviews/Yin_R_F0054_v1.md#completion-finding-and-verification-boundaries) | Original complete coordinating contributor audit of the exact counterexample and original-contract interface; no new mathematical inspection date or independent certification. |


### Decision isolated-main-and-bh-review-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:38 |
| status | proved |
| reason | Adopt the exact unchanged main construction and optional bh extension with their separate actual independent findings. R186 keeps the main Sections1–7 scope; the new R944 finding supplies the complete Section8 scope. Original UNKNOWN and contributor findings retain their dates, inputs and useful boundaries in their responsible homes, without a new Task completion or research execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained input](#statement) | The original h,hbh bounded-dual counterexample, standard finite-tracial space, ranks and scalar nonmembership remain unchanged. |
| argument | [Exact retained input](#1-an-explicit-tracial-fock-model) | Original sections 1-8, including standard model, bounded operators, every dual relation, generation and norm exclusion; optional bh strengthening retains its distinct contributor evidence. |
| review | [Exact retained input](../audits/reviews/Yin_R_F0056_v1.md#main-counterexample-finding) | Actual new complete independent inspection of the unchanged main statement and Sections 1–7, with exact original-contract and source interfaces; Section 8 is expressly excluded. |
| review | [Exact retained input](../audits/reviews/Yin_R_F0007_v1.md#verification-facts-and-outcome) | Original complete contributor integration review, self-reviewed with the earlier mathematical checks disclosed. |
| review | [Exact retained input](../audits/reviews/Yin_R_F0054_v1.md#completion-finding-and-verification-boundaries) | Original complete coordinating contributor audit of the exact counterexample and original-contract interface; no new mathematical inspection date or independent certification. |
| review | [Actual isolated bh extension finding](../audits/reviews/Yin_R_F0082_v1.md#current-bh-extension) | Complete Section8 bh extension and its actually used Sections1–7 interfaces only, both exact rank-one commutators, adjoint norm exclusion and minimal monic representation; initial independent finding2026-10-22T21:12. Main1–7 remain independently covered by R186 at its actual scope. |

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
| argument | [Exact material](#1-an-explicit-tracial-fock-model) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0082_v1.md#original-f0013-account) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |
| review | [Exact material](../audits/reviews/Yin_R_F0007_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |
| review | [Exact material](../audits/reviews/Yin_R_F0082_v1.md#original-f0011-account) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |
| review | [Exact material](../audits/reviews/Yin_R_F0054_v1.md) | Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review. |

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

Previously selected argument and historical assessment carried forward by checked source-commit, navigation and newline correspondence; no new mathematical review.

Review: [Exact material](../audits/reviews/Yin_R_F0082_v1.md#original-f0013-account); [Exact material](../audits/reviews/Yin_R_F0007_v1.md); [Exact material](../audits/reviews/Yin_R_F0082_v1.md#original-f0011-account); [Exact material](../audits/reviews/Yin_R_F0054_v1.md).

Material covered by that review: [Exact material](Yin_C_F0012_v1.md).

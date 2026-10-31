---
author: Yin
---
# Bounded contractions give actual vacua for real derivations and bare dual systems

Date: 2026-10-14T11:14.
Version 2 retains the complete v1 proof and adds the reverse implication for mixed selfadjoint/unitary tuples, by explicit coordinate checks and the C_F0043 norm mechanism.
The v1 statement and assessment remain fixed at [v1](Yin_C_F0071_v1.md).
Human author Yin.
The full_acsy_counterexample agent developed the spectral-partition lemma and selfadjoint application; root proposed the scalar normal and affine-coordinate consequences; the audit_acsy_nonnormal agent proposed the unitary twist.
This responds to the explicit user request to continue comparing the hypothesis of ACSY24 Proposition 3.5 with existence of full-domain duals.
No novelty claim is made.

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Statement

Let (M,tau) be a finite von Neumann algebra with faithful normal tracial state, H=L2(M,tau), Omega=1, and P=P_Omega.
All adjoint-domain assertions refer to actual densely defined operators between Hilbert spaces.
The inner product is linear in its second variable.

**A. Real-derivation converse.**
Let A be a unital *-subalgebra with A Omega dense in H and B its operator-norm closure.
Let delta:A -> H tensor_2 H be an outer-bimodule derivation satisfying delta(a*)=(delta a)^dagger, where (u tensor v)^dagger=v* tensor u*.
If E=(id tensor tau)delta is bounded for the operator norm on A, then

\[
 1\otimes1\in\operatorname{Dom}\delta^*,
 \qquad\|\delta^*(1\otimes1)\|_2\le2\sqrt2\|E:A\to H\|.
\]

No coassociativity or a priori closability is assumed.
The argument uses the stronger abstract symmetric-form lemma stated below.

**B. Selfadjoint generating tuples.**
For any finite selfadjoint generating tuple X, the following existence conditions are equivalent:

1. Complex-linear D_i:M Omega -> H satisfy [X_j,D_i]=delta_ij P on all M Omega, without continuity, closability or adjoint-domain assumptions.
2. Derivations delta_i:C<X> -> H tensor_2 H satisfy delta_i(X_j)=delta_ij 1 tensor 1 and 1 tensor 1 belongs to Dom delta_i* for every i.

In the first-to-second implication, normalize E_i(a)=-D_i(a)+aD_i(1).
These maps are bounded M -> H and their uniquely induced real derivations have vacuum norms at most 2 sqrt2 ||E_i||.
The second condition is exactly the ACSY24 hypothesis and, in this selfadjoint setting, finite joint non-microstates Fisher information.

**C. Scalar normal generators.**
The same two existence conditions are equivalent for one normal generator x, with the starred algebra C[x,x*] in the second condition.
In the first-to-second implication the unique divided-difference derivation has vacuum norm at most 4||E||.

**D. Unitary and mixed tuples.**
For every generating tuple whose coordinates are each selfadjoint or unitary, the bare full-M dual condition implies the ACSY24 derivation and actual-vacuum condition.
The reverse implication also holds for every such mixed tuple, so the two conditions are equivalent in this class.
For a unitary coordinate i, the forward construction gives the sufficient bound 2 sqrt2 (||E_i||+1)+1 for its vacuum norm.

**E. Complex affine reparameterization.**
Both implications in B remain valid after any invertible complex affine coordinate change X=A S+b of a selfadjoint generating d-tuple S, with A in GL_d(C).
This class includes nonnormal tuples.

The two implications for arbitrary correlated normal tuples and for arbitrary general tuples are not asserted here.
The distinction is existential: no conclusion identifies an arbitrarily chosen supplied full-domain operator with the closure of the canonical core operator on all M.

## Argument

### Symmetric-form lemma

Let B be a unital C*-subalgebra of a finite tracial von Neumann algebra (M,tau).
Put H=L2(M,tau).
Suppose E:B -> H is bounded with norm C, and a linear functional phi:B -> C satisfies

\[
 \phi(a^*b)=\tau((Ea)^*b)+\tau(a^*Eb)\qquad(a,b\in B).
\]

Then phi is Hermitian and

\[
 |\phi(a)|\le 2\sqrt2 C\|a\|_2\qquad(a\in B).
\]

Hermiticity follows by conjugating and exchanging a,b; phi is norm-continuous by taking a=1.
For selfadjoint a in B, choose a finite continuous square partition h_j on its compact real spectrum such that sum h_j^2=1, at most two h_j are nonzero at every point, and each support has diameter at most epsilon.
Write h_j=h_j(a), and select a real lambda_j in each support.
Thus

\[
 \|a-\sum_j\lambda_j h_j^2\|\le\epsilon,
 \qquad
 \sum_j\lambda_j^2\|h_j\|_2^2\longrightarrow\|a\|_2^2.
\]

For independent symmetric signs sigma_j, pointwise Cauchy--Schwarz gives ||sum sigma_j h_j|| <= sqrt2.
Linearity and the Hilbert-space sign identity yield

\[
 \sum_j\|Eh_j\|_2^2
 =\mathbb E_\sigma\|E(\sum_j\sigma_jh_j)\|_2^2\le2C^2.
\]

The symmetric-form identity at h_j,h_j gives phi(h_j^2)=2 Re tau(h_j Eh_j).
Therefore

\[
 \left|\phi(\sum_j\lambda_jh_j^2)\right|
 \le2\sum_j|\lambda_j|\|h_j\|_2\|Eh_j\|_2
 \le2\sqrt2 C(\sum_j\lambda_j^2\|h_j\|_2^2)^{1/2}.
\]

Let epsilon decrease to zero.
Norm continuity of phi proves the asserted bound for selfadjoint a.
For arbitrary a choose theta so that e^{i theta} phi(a) is real nonnegative.
Hermiticity gives |phi(a)|=phi(Re(e^{i theta}a)), and ||Re(e^{i theta}a)||2 <= ||a||2, proving the same constant.

A square partition with overlap two exists by a partition of unity on a real interval subordinate to consecutive overlapping intervals, followed by normalization by the square root of the sum of squares.
Endpoints can be handled by extending the interval slightly.

### Application to a real derivation

Let A be a norm-dense unital *-subalgebra of B, assume A Omega is dense in H, and let delta:A -> H tensor_2 H be an outer-bimodule derivation that is real:

\[
 \delta(a^*)=(\delta a)^\dagger,
 \quad (u\otimes v)^\dagger=v^*\otimes u^*.
\]

Suppose E=(id tensor tau)delta is bounded A with its operator norm -> H.
Put F=(tau tensor id)delta and phi=(tau tensor tau)delta.
Reality gives F(a*)=(Ea)*.
The Leibniz rule gives

\[
 \phi(a^*b)=\tau(F(a^*)b)+\tau(a^*Eb)
 =\tau((Ea)^*b)+\tau(a^*Eb).
\]

E extends to B.
Since phi= tau E it also extends continuously, and the displayed identity extends to B by norm approximation.
The symmetric-form lemma gives the actual adjoint condition 1 tensor 1 in Dom delta*, with ||delta*(1 tensor 1)||2 <= 2 sqrt2 ||E||.
No closability of delta or E is presupposed.

### Application to bare selfadjoint duals

Let X=(X_1,...,X_d) be selfadjoint generators and D_i:M Omega -> H complex-linear with [X_j,D_i]=delta_ij P.
Normalize E_i(a)=-D_i(a)+aD_i(1).
By [C_F0069 Part A](Yin_C_F0069_v1.md#statement), each E_i is bounded M -> H.
On A=C<X>, the commutator [E_i,a] is finite rank; under Theta(u tensor v)=u P v it defines a well-defined derivation delta_i.
Its generator values are delta_i X_j=delta_ij 1 tensor 1.
Because every generator is selfadjoint, reversal of monomials shows delta_i is real.
Also E_i1=0 makes E_i=(id tensor tau)delta_i on A.
The previous result therefore proves the actual joint vacuum condition for every i.
This is the full ACSY24 hypothesis for selfadjoint tuples, not merely a marginal statement.

The reverse selfadjoint direction follows from Dabrowski's contraction estimate and the canonical closed-graph/Kaplansky argument already retained in Dab10-U002 and C_F0070 Part B.
Hence the two existential hypotheses are equivalent for selfadjoint generating tuples, with the new symmetric-form argument supplying the converse.

### Limits

For a normal but nonselfadjoint tuple the unique delta_i in C_F0070 generally is not real.
Its left contraction F_i is not automatically a conjugate of E_i.
Consequently the symmetric-form identity used above does not hold for the same E_i without an additional argument.
This draft does not settle arbitrary normal or general tuples, and does not claim a counterexample.

### Scalar normal corollary

This extension was suggested by the root agent after completion of the preceding selfadjoint argument.
Suppose x is a single normal generator, M=W*(x), and a bare full-domain dual exists.
Normalize E as above and set C=||E:M -> H||, finite by C_F0069 Part A.
Let mu be the diffuse spectral law.
By C_F0070 Part A the unique derivation on A=C[x,x*] is represented by

\[
 \delta p(z,w)=\frac{p(z,\bar z)-p(w,\bar w)}{z-w}
 \quad(z\ne w),
\]

with arbitrary diagonal value on the product-null diagonal.
Indeed the displayed divided difference is bounded for a polynomial in z and bar z on the compact spectral square, satisfies the Leibniz rule, and has exactly the unique generator values delta x=1 and delta x*=(bar z-bar w)/(z-w).

The kernel is symmetric under exchanging z,w, with no complex conjugation.
Consequently its two contractions coincide: F=(tau tensor id)delta=(id tensor tau)delta=E on A.
Define phi=(tau tensor tau)delta=tau E.
The Leibniz rule and commutativity imply

\[
 \phi(ab)=\tau((Ea)b)+\tau(aEb)\qquad(a,b\in A).
\]

Both E and phi are bounded for the operator norm, so this identity extends to B=C*(x).
For every real continuous h in B it gives phi(h^2)=2 tau(hEh).
The same overlap-two square partition and Rademacher estimate from the symmetric-form lemma, now using absolute values without taking a real part, prove

\[
 |\phi(a)|\le2\sqrt2 C\|a\|_2\quad(a=a^*\in B).
\]

For p=a+ib with a,b selfadjoint, traciality gives ||a||2^2+||b||2^2=||p||2^2.
Thus

\[
 |\phi(p)|\le4C\|p\|_2.
\]

This proves the actual vacuum-adjoint condition for the unique scalar normal derivation, with norm at most 4C.
It does not assume a real derivation, Hilbert-space closability of the supplied dual, or an adjoint-domain premise.
For the reverse implication, ACSY24 Proposition 3.5 first gives Delta(x)=1 and hence a nonatomic spectral law: if a nonzero spectral atom e existed, the rank-one projection onto e Omega would commute with right multiplication by x, giving a nonzero finite-rank cycle and a nonzero closed kernel module; faithfulness of von Neumann dimension would contradict Delta(x)=1.
Differentiating xx*=x*x then gives (z-w)delta(x*)=bar z-bar w on the scalar coarse space; diffuseness makes multiplication by z-w injective, so the ACSY24 derivation is exactly the displayed divided difference on the whole star core.
Now [C_F0055](Yin_C_F0055_v1.md#statement) applies and supplies the full canonical bounded-vector domain.
This gives equivalence of ACSY24's scalar normal condition and existence of a bare full-M dual.
The multiple correlated normal-coordinate case remains open in this statement.

### Bounded source-reuse search

On 2026-10-14, the search checked existing C_F0038 (L1 conjugates under closability), C_F0069 (scalar selfadjoint converse), C_F0070 (normal starred derivation and conditional equivalence), Shl06-U001 (Theorem 1 and Corollary 2), and source-targeted public searches for free difference quotient bounded contractions and conjugate-variable converses.
The published MS23 Definition 2.4 and Theorem 2.5 retain an explicit vacuum-adjoint premise, as does Shl06.
Dab10 supplies the forward finite-Fisher-to-contraction estimate.
No exact published converse from operator-norm-to-L2 boundedness was verified in this bounded search.
This is not a priority or novelty claim.

### Invertible affine changes of selfadjoint coordinates

The root agent pointed out that the equivalence also covers nonnormal tuples obtained from selfadjoint coordinates by invertible complex affine changes.
Let S=(S_1,...,S_d) be selfadjoint generators and

\[
 X_j=\sum_k A_{jk}S_k+b_j1,\qquad A\in GL_d(\mathbb C).
\]

Then C<X,X*>=C<S>.
From a generator-first dual D^S for S, define

\[
 D_i^X=\sum_k(A^{-1})_{ki}D_k^S.
\]

The commutators are [X_j,D_i^X]=delta_ji P.
Conversely a dual for X gives D_k^S=sum_i A_{ik}D_i^X and [S_l,D_k^S]=delta_lk P.
The domains remain all M Omega.
The identical coefficient formulas transform derivations on the common starred core, and finite linear combinations preserve the actual vacuum-adjoint condition.
Therefore ACSY24's hypothesis and the bare full-M dual hypothesis are equivalent for every tuple in this class.
No normality of the X_j is claimed or needed: X=(S_1+iS_2,S_1-iS_2) is an example when S_1,S_2 fail to commute.
This is a direct corollary of the selfadjoint equivalence, not a claim covering arbitrary nonnormal tuples.

### Unitary and mixed selfadjoint/unitary forward implication

This extension was proposed by the independent audit agent after checking the real-derivation argument.
Let X be a generating tuple, each coordinate either selfadjoint or unitary, and assume a bare full-M dual system.
Normalize E_i as above.
C_F0069 makes every E_i bounded M -> H, say with norm C_i.
For a unitary coordinate U_j, the inverse commutator identity gives

\[
 [E_i,U_j^*]=-U_j^*[E_i,U_j]U_j^*
             =-\delta_{ij}U_j^*P U_j^*.
\]

For a selfadjoint coordinate its starred commutator is the same as its original one.
Thus finite-rank commutators define a well-defined algebraic-tensor derivation delta_i on the entire common star core, with the stated generator values, without invoking the general C_F0070 phase construction.
For a selfadjoint i, delta_i is real on every generator and hence on the core.
The real-derivation lemma immediately gives its actual vacuum.

For a unitary coordinate i write U=X_i and delta=delta_i.
Define the inner coefficient action

\[
 (a\otimes b)\#(c\otimes d)=ac\otimes db,
 \qquad \beta=\mathrm i\,\delta\#(1\otimes U).
\]

This right coefficient action commutes with outer bimodule actions, so beta is a derivation.
It satisfies

\[
 \beta(U)=\mathrm i1\otimes U,
 \quad \beta(U^*)=-\mathrm iU^*\otimes1,
\]

and vanishes on the other generators and their adjoints.
Hence beta is real on the whole core.
Its right contraction is

\[
 B(a)=(\mathrm{id}\otimes\tau)\beta(a)
      =\mathrm i\bigl(E_i(aU)-aE_i(U)\bigr).
\]

To verify this equality, write delta a=sum a_k tensor b_k.
Its right side is i sum a_k tau(b_k U), while the left side is i sum a_k tau(U b_k); these coincide by traciality.
Because E_i(U)=1, B has operator-norm-to-H bound at most C_i+1.
The real-derivation lemma therefore gives an actual vector eta=beta*(1 tensor 1), with ||eta||2 <= 2 sqrt2 (C_i+1).

No general tensor-adjoint formula is needed to transfer this vacuum back.
Since beta(U*)=-i U* tensor 1, the Leibniz rule and traciality give, for every core element a,

\[
 (\tau\otimes\tau)\delta(a)
 =-\mathrm i(\tau\otimes\tau)\beta(aU^*)+\tau(aU^*).
\]

Indeed beta(aU*)=beta(a) dot U* - i aU* tensor 1, and the trace of beta(a) dot U* equals the trace of beta(a)#(1 tensor U*); the latter tensor is i delta(a).
Since right multiplication by U* is unitary on H, the displayed formula yields

\[
 |(\tau\otimes\tau)\delta(a)|
 \le(\|\eta\|_2+1)\|a\|_2.
\]

Thus the actual vacuum condition holds for delta_i, for every unitary coordinate as well.
This proves the bare-dual-to-ACSY24 implication for every mixed selfadjoint/unitary generating tuple.
For a purely unitary tuple the reverse implication is already contained in [C_F0043, Section 3](Yin_C_F0043_v1.md#3-a-unitary-polynomial-core-has-the-required-two-bounds), followed by its canonical graph argument, so the two existential conditions are equivalent there.
No uninspected use of ACSY24 Lemma 3.3 is required for the forward argument.


### Reverse implication for mixed selfadjoint/unitary tuples

Suppose X is a generating tuple with every coordinate selfadjoint or unitary and suppose ACSY24's derivations theta_i and actual vacua exist.
Their values on all starred generators belong to the algebraic tensor core: for a selfadjoint coordinate theta_i(X_j*)=delta_ij 1 tensor 1, while for a unitary coordinate theta_i(X_j*)=-delta_ij X_j* tensor X_j*.
Thus theta_i maps the whole star core A into A tensor_alg A.

Fix i.
If X_i is selfadjoint, set beta=theta_i and epsilon=0.
If X_i=U is unitary, set epsilon=1 and

\[
 \beta=\mathrm i I_{U\otimes1}\theta_i,
 \qquad I_{c\otimes d}(a\otimes b)=ac\otimes db.
\]

This is the left twist used in C_F0043 Section 3; it differs from the right twist used for the forward argument.
Its generator values are beta(U)=i U tensor 1 and beta(U*)=-i 1 tensor U*.
In both cases beta vanishes on every other generator and its adjoint, regardless of whether that coordinate is selfadjoint or unitary.
Hence beta is real on A.
The vacuum exists directly: in the unitary case,

\[
 (\tau\otimes\tau)\beta(a)
 =\mathrm i\bigl((\tau\otimes\tau)\theta_i(Ua)-\tau(a)\bigr),
\]

which is L2-bounded because theta_i has an actual vacuum and left multiplication by U is unitary.
Let zeta=beta*(1 tensor 1).
Reality makes zeta selfadjoint.
No general twisting assertion from ACSY24 Lemma 3.3 is being assumed.

Write E=(id tensor tau)beta, F=(tau tensor id)beta on A.
The product rule, reality and the vacuum identity give, for a,b in A,

\[
 \beta^*(a\otimes b)=a\zeta b-(Ea)b-a(Fb),
 \qquad E^*p=p\zeta-Ep\quad(p\in A).
\]

For completeness, expand the vacuum pairing on a* p b*: the term a* beta(p) b* is the tensor pairing with a tensor b, while the two other Leibniz terms pair p with (Ea)b and a(Fb).
This proves the first formula as an actual adjoint identity on A tensor_alg A.
The same expansion with b=1 proves the second.
Algebraic tensors are dense, so beta is closable; A is contained in Dom E*, so E is closable.

The coordinate identities give the exact coassociativity defect

\[
 (\beta\otimes\mathrm{id})\beta
 -(\mathrm{id}\otimes\beta)\beta
 =\mathrm i\varepsilon\kappa\beta,
 \qquad\kappa(a\otimes b)=a\otimes1\otimes b.
\]

Both sides are derivations into the outer triple module: the two mixed product terms on the left cancel.
For a selfadjoint distinguished coordinate, both sides vanish on every starred generator.
For a unitary distinguished coordinate they agree on U and U* exactly as in C_F0043 Section 3.1, and vanish on all other generators and adjoints.
This proves the identity on the whole mixed core.

Contracting by id tensor tau tensor tau yields

\[
 E^2p=(\mathrm{id}\otimes\tau)((\beta p)\cdot\zeta)
       +\mathrm i\varepsilon Ep.
\]

The complete norm calculation from the preceding adjoint and reality identities is

\[
 \begin{aligned}
 \|Ep\|_2^2
 &=\langle Ep\,\zeta-E^2p,p\rangle\\
 &=2\operatorname{Re}\langle Ep,p\zeta\rangle
   -\langle\beta(p^*p),1\otimes\zeta\rangle
   -\langle\mathrm i\varepsilon Ep,p\rangle .
 \end{aligned}
\]

The first line is the actual adjoint identity with Ep in A.
For the second, substitute the contracted defect formula and expand beta(p*p); reality pairs the beta(p*) term with p zeta.
This is precisely the C_F0043 Section 3 calculation with the defect coefficient epsilon, so it includes the zero-defect selfadjoint case without assuming that other coordinates are selfadjoint.

For a selfadjoint a in A with ||a||<1, the analytic unitaries u=a+i(1-a^2)^(1/2) and u* have polynomial approximants converging in operator norm and in the graph norms for beta on the element and its adjoint.
Indeed the square-root binomial series and its differentiated series converge absolutely, using ||beta(a^k)||2 <= k||a||^(k-1)||beta(a)||2.
In the norm identity, all terms pass to the limit.
Closedness of beta makes the derivative of u*u=1 zero.
Consequently the limiting vector v=E u obeys

\[
 \|v\|_2^2\le(2\|\zeta\|_2+\varepsilon)\|v\|_2.
\]

Apply this to u and u*, average to obtain E a, and rescale arbitrary selfadjoint a.
Splitting arbitrary p into real and imaginary parts then gives

\[
 \|Ep\|_2\le(4\|\zeta\|_2+2\varepsilon)\|p\|,
 \quad
 \|E^*p\|_2\le(5\|\zeta\|_2+2\varepsilon)\|p\|.
\]

These are estimates on the actual polynomial operators and adjoints.
Let N_i=(id tensor tau)theta_i be the original canonical core operator.
For a selfadjoint coordinate, N_i=E.
For a unitary coordinate,

\[
 N_i=-\mathrm i\rho(U^*)E,
 \qquad N_i^*p=\mathrm i E^*(pU)\quad(p\in A).
\]

Here rho(U*) denotes right multiplication by U*.
It is unitary on H, and right multiplication by U preserves A.
Thus N_i is closable, A is contained in its actual adjoint domain, and both operators have uniform operator-norm-to-H bounds on A.

Finally let a in M.
Kaplansky density and polynomial norm approximation give a bounded net p_alpha in A converging to a in L2.
The uniform bound makes N_i p_alpha weakly relatively compact in H.
Any weak cluster pair (a,v) lies in the weakly closed graph of the Hilbert closure of N_i, hence a belongs to its domain.
The same argument for the core restriction of N_i* puts all M in Dom N_i*.
Uniqueness of the graph value shows N_i p_alpha converges weakly to its closure value.
Apply this also to X_j p_alpha; the core commutator identity passes to the weak limit and gives [closure(N_i),X_j]=delta_ij P on all M Omega.
Therefore D_i=-closure(N_i)|M Omega is a bare full-domain generator-first dual.
This proves the reverse implication for every mixed selfadjoint/unitary tuple, including the originally canonical closure and adjoint domain conclusions.

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-14T11:14 |
| status | open |
| reason | Complete v2 candidate adding the mixed reverse implication with explicit coordinatewise coassociativity-defect, analytic-series and actual graph-domain checks. Independent checks of the working argument have been communicated; fixed-artifact review is pending and has not yet been selected. |

Recorded authoring stage: proof draft.
Recorded review label: self-reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Parts A--E with their exact generating, reality and domain premises. |
| argument | [Argument](#argument) | Complete spectral-partition argument, coordinate applications, reverse source applications and scope limits. |
| dependency | [C_F0069 Part A](Yin_C_F0069_v1.md#statement) | Automatic operator-norm-to-H boundedness of bare full-domain normal duals. |
| dependency | [C_F0070 Part A](Yin_C_F0070_v1.md#statement) | Unique starred derivation from a bare scalar normal dual; no general vacuum conclusion imported. |
| dependency | [C_F0055](Yin_C_F0055_v1.md#statement) | Scalar normal actual-vacuum-to-canonical-full-domain implication after nonatomicity and divided-difference identification. |
| dependency | [Dab10-U002](../audits/literature/Dab10/Yin_U002.md#dab10-u002) | Selfadjoint finite-Fisher contraction bounds and actual canonical bounded-vector domains. |
| dependency | [C_F0043 Section 3](Yin_C_F0043_v1.md#3-a-unitary-polynomial-core-has-the-required-two-bounds) | Section 3 norm mechanism, rechecked here coordinatewise with defect coefficient 0 or 1 for the complete mixed reverse implication. |
| dependency | [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 for scalar-normal nonatomicity and exact actual-vacuum interface. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T11:20 |
| status | proved |
| reason | The complete fixed v2 statement and argument passed complementary independent component review, including the full mixed reverse, with exact contribution and source boundaries disclosed. The general correlated-normal and arbitrary-tuple implications remain unresolved. |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Parts A--E with actual adjoints, density and exact existential equivalence classes. |
| argument | [Argument](#argument) | Complete spectral-partition converse, scalar normal proof, unitary twists, mixed reverse and affine transformations. |
| dependency | [C_F0069 Part A](Yin_C_F0069_v1.md#statement) | Automatic operator-norm-to-H boundedness of bare normal full-domain duals. |
| dependency | [C_F0070 Part A](Yin_C_F0070_v1.md#statement) | Scalar normal starred derivation and exact canonical-core agreement. |
| dependency | [C_F0055](Yin_C_F0055_v1.md#statement) | Scalar normal vacuum-to-canonical-full-domain result after diffuse divided-difference identification. |
| dependency | [Dab10-U002](../audits/literature/Dab10/Yin_U002.md#dab10-u002) | Selfadjoint finite-Fisher contraction bounds and canonical bounded-vector domains. |
| dependency | [C_F0043 Section 3](Yin_C_F0043_v1.md#3-a-unitary-polynomial-core-has-the-required-two-bounds) | Exact energy and graph mechanism, with the mixed coordinate checks proved in this argument. |
| dependency | [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Actual vacuum interface and scalar nonatomicity through Proposition 3.5. |
| review | [Complementary whole review](../audits/reviews/Yin_R_F0044_v1.md#conclusion) | Entire fixed v2 Parts A--E; component contributions, independent checks and accepted source limits explicit. |


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:54 |
| status | proved |
| reason | Adopt the exact original findings at their disclosed relationships. Preserve the mathematical statement, status, selected arguments, dependencies, authority and historical decisions; no new proof or review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Parts A--E with actual adjoints, density and exact existential equivalence classes. |
| argument | [Exact material](#argument) | Complete spectral-partition converse, scalar normal proof, unitary twists, mixed reverse and affine transformations. |
| dependency | [Exact material](Yin_C_F0069_v1.md#statement) | Automatic operator-norm-to-H boundedness of bare normal full-domain duals. |
| dependency | [Exact material](Yin_C_F0070_v1.md#statement) | Scalar normal starred derivation and exact canonical-core agreement. |
| dependency | [Exact material](Yin_C_F0055_v1.md#statement) | Scalar normal vacuum-to-canonical-full-domain result after diffuse divided-difference identification. |
| dependency | [Exact material](../audits/literature/Dab10/Yin_U002.md#dab10-u002) | Selfadjoint finite-Fisher contraction bounds and canonical bounded-vector domains. |
| dependency | [Exact material](Yin_C_F0043_v1.md#3-a-unitary-polynomial-core-has-the-required-two-bounds) | Exact energy and graph mechanism, with the mixed coordinate checks proved in this argument. |
| dependency | [Exact material](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Actual vacuum interface and scalar nonatomicity through Proposition 3.5. |
| review | [Original finding](../audits/reviews/Yin_R_F0044_v1.md#conclusion) | Whole fixed v2 Parts A–E, complete mixed reverse, partition converse, scalar and affine consequences; self-reviewed because of the disclosed unitary-twist contribution and shared development, not isolated whole-proof coverage. |


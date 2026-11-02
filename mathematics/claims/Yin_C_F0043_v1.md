---
author: Yin
---

# Bare polynomial-core duals on univalent analytic closed curves acquire both original all-M domains

## Current assessment
[Selected decision](#decision-isolated-current-review-20261022)

## Closed Analytic Curves and the Original Polynomial-Core Duals

<a id="statement"></a>
<a id="yin_c_f0043"></a>

Date: 2026-09-11.
Human author: Yin.
Proof development: another AI agent.
Record kind: substantive research and complete proof candidate for the separate normal-domain investigation, with priority on its bare polynomial-domain question.
At authorship, promotion awaited independent review.
The earlier [Yin_C_F0041 graph proof](Yin_C_F0041_v1.md#yin_c_f0041), [Yin_C_F0042 arc proof](Yin_C_F0042_v1.md#yin_c_f0042), and all frozen records remain unchanged.

Current assessment, 2026-09-11: registered as **Yin_C_F0043**, proved and independently reviewed in [the complete audit](../audits/reviews/Yin_R_F0075_v1.md#scope-of-acceptance).
This dated assessment supersedes the candidate labels below; no mathematical Role is assigned.
The original Yin_C_F0025 hypotheses and unstarred rational algebra are unchanged.

## 1. Exact candidate and relation to the remaining question

Retain precisely the setting and hypotheses of [Yin_C_F0025](Yin_C_F0025_v1.md#yin_c_f0025).
Thus X=(X_1,...,X_d) is a bounded normal generating tuple in a finite tracial von Neumann algebra (M,tau), H=L2(M,tau), Omega=1, and the original operators D_i0 have domain exactly
\[
 \mathcal P_X=\mathbb C\langle X_1,X_1^*,\ldots,X_d,X_d^*\rangle.
\]
They satisfy Omega in Dom(D_i0*), [D_i0,X_j]=delta_ij P_Omega on this core, and compact bounded extensions for their starred-generator commutators.
Write D_i for their actual closures.
The inner product is linear in its second variable.
The rational algebra remains
\[
 \mathcal A_X=\mathbb C\langle X_1,\ldots,X_d\rangle.
 \tag{1}
\]

Assume additionally that, for each i,
\[
 X_i=r_i(U_i),\qquad U_i\text{ unitary},
 \tag{2}
\]
where r_i is holomorphic and injective on an open annulus containing the unit circle.
Equivalently, the coordinate spectrum is contained in an analytically parametrized simple closed curve with such a parametrization.
The coordinate spectrum need not fill that curve.
Injectivity implies a nonvanishing derivative.
A representation as in (2) is a geometric hypothesis, not a claim that the original dual hypotheses hold for every law on the curve.

The candidate conclusion is
\[
 M\subseteq\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*,
 \quad \|D_i x\|_2\le C_i\|x\|,
 \quad \|D_i^*x\|_2\le C_i'\|x\|\qquad(x\in M),
 \tag{3}
\]
for finite constants.
These refer to the originally specified operators and their actual Hilbert adjoints.
In particular their original weak-form criterion has the missing rational converse, and the full equivalence is with
\[
 f\in \operatorname{Div}_{L^0(M)}\mathcal A_X\cap M.
 \tag{4}
\]
The all-M theorem Yin_C_F0024 and the original weak implication Yin_C_F0025 provide this last interface exactly as in Yin_C_F0042.
No equality with Div_M(A_X) is inferred from this domain argument.

There are two substantive steps.
Section 3 proves the required bounds for unitary polynomial cores directly; it does not invoke the dense-left-module premise of the unitary adjoint-correction argument.
Sections 4-7 transfer these bounds through an analytic closed-curve parametrization without identifying the two polynomial cores.
There is no assumed bounded reference dual.

## 2. Local and primary-source reuse before the new argument

The local search checked Yin_C_F0025's canonical coarse derivations, Yin_C_F0028's single-coordinate result, the unitary adjoint correction on a dense left module, Yin_C_F0040/Yin_C_F0041's contraction and inner-multiplier calculations, and Yin_C_F0042's reconstruction of the original closures.
Yin_C_F0028 already handles the single normal coordinate; the new statement is useful for several normal coordinates.
That dense-left-module argument does not by itself apply to a polynomial core.

The primary source [Dabrowski, arXiv:0804.2906v2](https://arxiv.org/pdf/0804.2906), printed p. 9, was reread at the full proof of Lemma 10 and the statement and proof of Lemma 12, after consulting [Dab10-U002](../audits/literature/Dab10/Yin_U002.md#dab10-u002).
Its contraction calculation uses both reality and coassociativity of selfadjoint free difference quotients.
The source is not a theorem about unitary generators.
The modified calculation below accounts for the nonzero coassociativity defect explicitly.
A bounded external search did not locate a verified ready-made theorem supplying this unitary-core conclusion.
No exhaustive novelty claim is made.

Other retained inputs are the coarse polynomial-tensor adjoint estimate from Yin_C_F0040/Yin_C_F0042, the weak closed-graph/Kaplansky argument from Yin_C_F0027, and Yin_C_F0041/Yin_C_F0042's inner-multiplier reconstruction.
The normal spectral theorem, holomorphic inverse theorem, scalar Cauchy formula on an annulus, and Laurent expansion are standard complex-analysis foundations.
The graph inverse and contour steps needed here are proved below rather than imported as unbounded-operator functional calculus.
No additional source-unit ID is allocated in this record.

## 3. A unitary polynomial core has the required two bounds

For this section let U=(U_1,...,U_d) be a unitary generating tuple and P_U its starred polynomial algebra, equivalently its evaluated noncommutative Laurent polynomial algebra.
Suppose there are well-defined derivations
\[
 \theta_i:P_U\longrightarrow P_U\otimes_{\mathbb C}P_U,
 \quad \theta_i U_j=\delta_{ij}1\otimes1,
 \quad 1\otimes1\in\operatorname{Dom}\theta_i^*.
 \tag{5}
\]
The tensor in (5) has the outer bimodule actions.
The inverse product rule forces theta_i(U_j*)=-delta_ij U_j* tensor U_j*.
These hypotheses follow from Yin_C_F0025 for a unitary tuple; later they will be constructed on a new unitary core.

Fix i and write U=U_i, theta=theta_i.
For an elementary tensor set
\[
 I_{a\otimes b}(v\otimes w)=va\otimes bw,
 \qquad C=\mathrm{id}\otimes\tau.
\]
The inner maps commute with all outer bimodule actions.
Define
\[
 \delta=\mathrm i I_{U\otimes1}\theta,
 \qquad E_0=C\delta.
 \tag{6}
\]
Then
\[
 \delta(U)=\mathrm i U\otimes1,
 \qquad \delta(U^*)=-\mathrm i1\otimes U^*,
 \tag{7}
\]
and delta vanishes on the other generators and their adjoints.
In particular delta is real for the antiunitary tensor involution
\[
 (a\otimes b)^\dagger=b^*\otimes a^*:
 \quad\delta(p^*)=(\delta p)^\dagger.
 \tag{8}
\]
This follows on generators from (7), then on all products by the Leibniz rule.

The polynomial-tensor adjoint argument applies to theta because of (5).
Thus
\[
 \zeta=\delta^*(1\otimes1)
       =\theta^*(-\mathrm i U^*\otimes1)\in H.
 \tag{9}
\]
Reality and the vacuum pairing show zeta=zeta*.
The same Leibniz argument gives polynomial tensors in Dom(delta*), hence closability of delta, and the actual polynomial adjoint identity
\[
 E_0^*p=p\zeta-E_0p\qquad(p\in P_U).
 \tag{10}
\]
For example (10) follows by applying the standard real-derivation adjoint formula to p tensor 1.
These adjoints are densely defined; they are not merely formal symbols.

### 3.1 The exact defect of coassociativity

Let kappa(a tensor b)=a tensor 1 tensor b.
On the algebraic core,
\[
 (\delta\otimes\mathrm{id})\delta
 -(\mathrm{id}\otimes\delta)\delta
 =\mathrm i\,\kappa\delta.
 \tag{11}
\]
Indeed the left side is a derivation into the outer triple bimodule: its two mixed product terms both have the form a_1 tensor a_2 b_1 tensor b_2 and cancel in the difference.
The right side is also a derivation.
On U the two sides both equal -U tensor 1 tensor 1; on U* they both equal 1 tensor 1 tensor U*; on the other starred generators they vanish.
This proves (11) on the whole evaluated algebra.
The unitary reweighting is real but is not coassociative.

Contracting (11) by id tensor tau tensor tau, and using the vacuum adjoint relation on the second leg, gives
\[
 E_0^2p=C\bigl((\delta p)\cdot\zeta\bigr)
                 +\mathrm i E_0p.
 \tag{12}
\]
Here E_0p lies in P_U, so the left side is defined.
The first term on the right is well-defined since delta p is a finite polynomial tensor and zeta is in L2.
Its second-leg trace is tau(b zeta)=tau(zeta b).

Using (10), (12), and the reality relation (8), the norm calculation is
\[
 \begin{aligned}
 \|E_0p\|_2^2
 &=\langle E_0p\,\zeta-E_0^2p,p\rangle\\
 &=\langle E_0p,p\zeta\rangle
       -\langle\delta p,p\otimes\zeta\rangle
       -\langle\mathrm i E_0p,p\rangle\\
 &=2\operatorname{Re}\langle E_0p,p\zeta\rangle
       -\langle\delta(p^*p),1\otimes\zeta\rangle
       -\langle\mathrm i E_0p,p\rangle.
 \end{aligned}
 \tag{13}
\]
For the last equality expand delta(p*p)=delta(p*) dot p+p* dot delta p and use (8); specifically the remaining pairing of delta(p*) dot p with 1 tensor zeta equals <p zeta,E_0p>.
Taking real parts of the last line is always permitted.
This displays the extra first-order term instead of dropping it in an application of Dab10.

### 3.2 Analytic unitaries give a uniform bound

The identity extends to any norm limit p_n of core polynomials for which delta p_n and delta(p_n*) converge in the coarse Hilbert space.
Every term in its last line converges: the product-rule tensor for delta(p_n*p_n) converges, p_n zeta converges in L2, and E_0p_n=C delta p_n converges in L2.
Closedness identifies the derivative of the limiting product.
In particular, if the limit u is unitary, that product derivative is zero and (13) implies, with v=lim E_0p_n,
\[
 \|v\|_2^2
 \le 2\|v\|_2\|\zeta\|_2+\|v\|_2,
 \qquad \|v\|_2\le2\|\zeta\|_2+1.
 \tag{14}
\]
The last term uses ||u||_2=1 and the absolute value bound for <i v,u>.
This estimate does not require that term to vanish.

For a selfadjoint a in P_U with ||a||<1, form
\[
 u=a+\mathrm i(1-a^2)^{1/2}.
\]
The binomial series for the square root gives polynomial approximants u_n in P_U converging in operator norm.
Their delta derivatives converge in the coarse norm: the derivative of a^k is bounded by k||a||^(k-1)||delta a||_2, and the differentiated analytic series is absolutely convergent.
The adjoint approximants have the same property, by reality.
Thus (14) applies to both u and u*.
Since a=(u+u*)/2, it gives ||E_0a||_2<=2||zeta||_2+1.
Applying this to a/(||a||+epsilon) and letting epsilon decrease to zero proves
\[
 \|E_0a\|_2\le(2\|\zeta\|_2+1)\|a\|
 \quad(a=a^*\in P_U).
\]
No C1 functional-calculus stability theorem for an unspecified operator domain was needed; only the displayed analytic series was used.

Writing any p as its real part plus i times its imaginary part, both of norm at most ||p||, and then using (10), yields the sufficient constants
\[
 \|E_0p\|_2\le(4\|\zeta\|_2+2)\|p\|,
 \qquad
 \|E_0^*p\|_2\le(5\|\zeta\|_2+2)\|p\|.
 \tag{15}
\]

Return to the normalized canonical unitary dual N_0=C theta.
Equation (6) gives the exact operator identity on the core
\[
 N_0=-\mathrm i\rho(U^*)E_0,
 \qquad N_0^*p=\mathrm i E_0^*(pU)\quad(p\in P_U).
 \tag{16}
\]
Right multiplication by U is unitary on H and preserves P_U.
Thus (15) gives the same two constants for N_0 and its actual adjoint on P_U.
The weak closed-graph/Kaplansky argument of Yin_C_F0027 now gives both all-M domains for its closure and adjoint.
Adding p maps to p eta restores any original normalization; its adjoint on this core is p maps to p eta*, and each infinity-to-2 bound increases by ||eta||_2.

This already proves (3) for arbitrary unitary tuples under the bare Yin_C_F0025 hypotheses.
It asserts boundedness M with its operator norm to H, not boundedness H to H.
For a single Haar unitary the real derivative in (7) has zeta=0 but E_0 is nonzero; the extra +1 in (14) correctly accommodates this boundary check.

## 4. An explicit graph algebra contains the needed resolvents

Return to the original normal X and normalize as in Yin_C_F0025:
\[
 \eta_i=D_{i0}\Omega,
 \quad N_{i0}p=D_{i0}p-p\eta_i,
 \quad N_{i0}=C\partial_{i0}.
\]
Yin_C_F0025 and the adjoint-tensor argument reused in Yin_C_F0042 give closable coarse derivations partial_i0 on P_X, with partial_i0(X_j)=delta_ij 1 tensor 1 and
\[
 \xi_i=\partial_{i0}^*(1\otimes1)\in H.
 \tag{17}
\]
Write partial_i^c for their actual closures.

Let G be the completion of the original graph algebra for
\[
 \|a\|_G=\|a\|
  +\sum_i\bigl(\|\partial_{i0}a\|_2
                   +\|\partial_{i0}(a^*)\|_2\bigr).
 \tag{18}
\]
It is faithfully realized as a subalgebra of M: operator-norm convergence implies L2 convergence, and closability makes the limits of both derivative components unique.
Its elements and their adjoints belong to every Dom(partial_i^c).
The finite product estimate for the outer bimodule actions shows that multiplication and involution extend continuously and that the closed derivatives obey the product rule on G.
Thus G is a complete normed *-algebra containing P_X.
Its realization retains actual simultaneous operator-norm and derivative-graph approximants from P_X.

If a in G is invertible in M, then a inverse belongs to G.
To prove this without an inverse-domain assumption, take c>||a||^2 and set
\[
 q=1-c^{-1}a^*a,\qquad\|q\|<1.
\]
The strict inequality uses the positive lower bound for a*a.
Each derivative of q^n has coarse norm at most n||q||^(n-1)||partial_i^c q||_2; the adjoint derivative has the same bound since q is selfadjoint.
Therefore the Neumann series c inverse sum_(n>=0) q^n converges in G to (a*a) inverse.
Multiplying by a* gives a inverse in G.
The product rule then proves
\[
 \partial_i^c(a^{-1})=-a^{-1}\cdot\partial_i^c(a)\cdot a^{-1}.
 \tag{19}
\]
No reality of partial_i0 is assumed in this argument.

In particular every resolvent (z-X_j) inverse for z outside the spectrum belongs to G, and
\[
 \partial_i^c((z-X_j)^{-1})
 =\delta_{ij}(z-X_j)^{-1}\otimes(z-X_j)^{-1}.
 \tag{20}
\]
The resolvent and its adjoint derivative depend continuously on z in G on a compact contour disjoint from the spectrum, by (19) and the resolvent identity.
Hence their ordinary Riemann contour sums converge in G.
This proves precisely the functional-calculus preservation needed next.

## 5. Recovering the unitary core on a closed curve

For each r_j in (2), choose two circles strictly inside its univalence annulus, one inside and one outside the unit circle.
Their images bound a compact annulus containing the coordinate spectrum in its interior.
Let gamma_j be its boundary, with the outer positive and inner negative orientation, and h_j=r_j inverse on a neighborhood of that closed annulus.
Scalar Cauchy calculus and the normal spectral theorem give
\[
 U_j=h_j(X_j)
  =\frac1{2\pi\mathrm i}\int_{\gamma_j}
                h_j(z)(z-X_j)^{-1}\,dz\in G.
 \tag{21}
\]
Both boundary components are essential.
Membership in G follows from Section 4, not from a claim of holomorphic polynomial approximation across a hole.
In particular U_j* is also in G.

Using (20) in the same integral gives
\[
 \partial_i^c U_j
 =\delta_{ij}K_j(U_j\otimes1,1\otimes U_j)(1\otimes1),
 \qquad
 K_j(u,v)=\frac{u-v}{r_j(u)-r_j(v)}.
 \tag{22}
\]
On the diagonal the removable value is 1/r_j'(u).
This follows from the Cauchy divided-difference formula on the annulus, applied to h_j.
The product rule for U_j* U_j=1 inside G gives
\[
 \partial_i^c U_j^*
 =-\delta_{ij}(U_j^*\otimes U_j^*)K_j(1\otimes1).
 \tag{23}
\]
All factors in (22)-(23) act in the coordinate abelian tensor subspace.

Set P_U=C<U_1,U_1*,...,U_d,U_d*> and partial_i^U=partial_i^c restricted to P_U.
Since W*(U)=W*(X)=M, this is a dense core algebra.
It lies in G, but need not lie in P_X.
Restriction and closure give the inherited adjoint relation
\[
 1\otimes1\in\operatorname{Dom}(\partial_i^U)^*,
 \qquad(\partial_i^U)^*(1\otimes1)=\xi_i.
 \tag{24}
\]
This is the actual original coarse vacuum adjoint, not a newly chosen one.

## 6. Canonical unitary derivatives and the two reconstruction estimates

On an annular neighborhood of the unit circle squared, put
\[
 J_i(u,v)=\frac{r_i(u)-r_i(v)}{u-v},\qquad K_i=J_i^{-1}.
\]
Both are holomorphic and bounded on a sufficiently small closed product annulus; univalence and the nonzero derivative remove all zeros, including on the diagonal.
Their double Laurent coefficients have exponential decay in |m|+|n|.
Explicitly, applying the two-variable Cauchy coefficient formula on inner or outer circles according to the signs of m,n gives a bound C rho^(-|m|-|n|) for some rho>1.
Consequently, for either function,
\[
 F(u,v)=\sum_{m,n\in\mathbb Z}c_{mn}u^m v^n,
 \qquad\sum_{m,n}|c_{mn}|(1+|m|+|n|)<\infty.
 \tag{25}
\]

The product and inverse rules on P_U give
\[
 \|\partial_i^U U_i^m\|_2\le |m|\|K_i\|_\infty
 \qquad(m\in\mathbb Z).
 \tag{26}
\]
For negative m, the divided difference of u^m on the unit circle is again a sum of |m| unit-modulus terms.
The same estimate applies to the adjoint power.
The polynomial-tensor adjoint estimate inherited from (24) therefore gives
\[
 \|(\partial_i^U)^*(U_i^m\otimes U_i^n)\|_2
 \le\|\xi_i\|_2+(|m|+|n|)\|K_i\|_\infty.
 \tag{27}
\]
Thus the Laurent expansion of I_Ji* applied to 1 tensor 1 converges in this adjoint graph norm, including its conjugated coefficients and negated powers.
Closedness proves
\[
 I_{J_i}^*(1\otimes1)\in\operatorname{Dom}(\partial_i^U)^*.
 \tag{28}
\]

The well-defined derivation
\[
 \theta_i=I_{J_i}\partial_i^U
 \tag{29}
\]
satisfies theta_i U_j=delta_ij 1 tensor 1 and theta_i U_j*=-delta_ij U_j* tensor U_j*.
Its values on P_U are algebraic polynomial tensors by these generator identities.
Equation (28) supplies its L2 vacuum adjoint.
Hence the complete unitary argument of Section 3 applies.
If E_i is the actual closure of C theta_i on P_U, there are finite constants c_i,c_i' with
\[
 M\subseteq\operatorname{Dom}E_i\cap\operatorname{Dom}E_i^*,
 \quad\|E_i x\|_2\le c_i\|x\|,
 \quad\|E_i^*x\|_2\le c_i'\|x\|.
 \tag{30}
\]

For K_i write the absolutely summable separated Laurent expansion
\[
 K_i(u,v)=\sum_r a_r(u)b_r(v),
 \qquad L_i=\sum_r\|a_r\|_\infty\|b_r\|_\infty<\infty.
\]
Each factor is a scalar multiple of a Laurent power.
Define F_i0^nor=C partial_i^U on P_U.
The inner-multiplier reconstruction already checked in Yin_C_F0041/Yin_C_F0042 gives
\[
 F_{i0}^{\rm nor}p
   =\sum_r\bigl(E_i(p b_r)-pE_i(b_r)\bigr)a_r,
 \quad\|F_{i0}^{\rm nor}p\|_2\le2c_iL_i\|p\|.
 \tag{31}
\]
The series converges absolutely in H by (30).
This identity uses the Leibniz rule and traciality of the contracted leg; it does not require selfadjointness of the unitary free difference quotient.

The polynomial adjoint is separately controlled.
The vacuum is xi_i by (24), and the core commutator is Theta(partial_i^U p), so
\[
 (F_{i0}^{\rm nor})^*p
   =p\xi_i-\Theta(\partial_i^U(p^*))^*\Omega.
\]
The corresponding adjoint reconstruction, with the same factor order as Yin_C_F0042, is
\[
 \Theta(\partial_i^U(p^*))^*\Omega
   =\sum_r\bigl(pE_i^*(a_r^*)-E_i^*(p a_r^*)\bigr)b_r^*.
\]
All inputs lie in the actual domains in (30).
It follows that
\[
 \|(F_{i0}^{\rm nor})^*p\|_2
 \le(\|\xi_i\|_2+2c_i'L_i)\|p\|.
 \tag{32}
\]
The adjoint estimate is not deduced solely from the bound in (31).

## 7. Restoring the original operators and their adjoints

Put F_i0 p=F_i0^nor p+p eta_i on P_U.
Its defining G approximants p_n in P_X converge in operator norm and in all required coarse derivative graphs.
Therefore
\[
 D_{i0}p_n=C\partial_{i0}p_n+p_n\eta_i
       \longrightarrow F_{i0}p\quad\text{in }H,
\]
which proves the actual graph inclusion
\[
 F_{i0}\subseteq D_i=\overline{D_{i0}}.
 \tag{33}
\]
The adjoint contribution on P_U is p eta_i*, with the same infinity-to-2 norm bound ||eta_i||_2.
Thus (31)-(32) give both such estimates for F_i0 and its actual adjoint.
Yin_C_F0027's weak closed-graph/Kaplansky argument on the dense star algebra P_U puts every bounded vector in both domains of T_i=closure(F_i0) and F_i0*.

Since T_i is contained in D_i, it agrees with D_i on every original p in P_X, which is a subset of M and hence of Dom(T_i).
Thus D_i0 is contained in T_i.
Taking closures and combining with (33) gives
\[
 T_i=D_i,\qquad F_{i0}^*=D_{i0}^*=D_i^*.
 \tag{34}
\]
This proves (3) for the original closures and original adjoints.
Bounded-set weak continuity extends the original generator identities to the all-M restrictions as in Yin_C_F0027.
The Yin_C_F0024/Yin_C_F0025 rationality interface therefore gives (4) with the original unstarred algebra (1).
Neither P_U=P_X nor equality of their unstarred generated algebras has been asserted.

## 8. Discriminating scope and review obligations

The unitary result includes full-circle spectra and arbitrary joint distributions satisfying the exact small-core hypotheses.
It is stronger in its domain conclusion than a theorem which starts with a dense left M-module.
The closed-curve transfer includes noncircular analytic Jordan curves with a univalent annular parametrization, such as the ellipse r(z)=z+c z inverse for real 0<c<1: if r(z)=r(w), then z=w or zw=c, so a sufficiently thin annulus about the unit circle is a univalence neighborhood.
Its derivative is nonzero there.
The geometric example does not assert dual existence for an unspecified joint law.

The proof is compatible with a spectral subset of the curve; no full-support distribution is used.
It does not address self-intersecting curves, vanishing parametrization derivative, arbitrary planar spectra, or rough closed curves without the analytic tensor expansion.
A multi-coordinate bare-core theorem for arbitrary normal spectra remains outside this result.
It also does not turn an affiliated inverse into a bounded inverse of a rational linearization.

Independent review should check the factor i and the sign in (11)-(13), reality and the actual adjoints in (9)-(10), the analytic unitary approximation in Section 3.2, the two simultaneous starred graph components in (18), inverse closure before Cauchy calculus, the inner boundary orientation, the weighted Laurent adjoint convergence, and the two original-operator graph inclusions in (33)-(34).
The new first-order defect term is indispensable: dropping it would wrongly force E_0=0 for a Haar unitary with zeta=0.

This is a complete proof candidate with the stated accepted foundations and self-review; no independent acceptance, Claim registration, proof-assistant formalization, external human review, or novelty assessment is claimed here.


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
| argument | [Exact material](#3-a-unitary-polynomial-core-has-the-required-two-bounds) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Original finding](../audits/reviews/Yin_R_F0075_v1.md#scope-of-acceptance) | Whole eight-section closed analytic-curve theorem: real unitary derivative with nonzero coassociativity defect, analytic approximation, simultaneous starred graph inverse/contour closure, Laurent adjoint convergence and equality of the original closures and actual adjoints; exact C_F0025 premises retained. Actual original finding with unknown initial-context relationship; original date and accepted inputs preserved. |


### Decision isolated-current-review-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T22:41 |
| status | proved |
| reason | Adopt the separate isolated current finding on the unchanged fixed statement and proof, with exact conditions and scope. Preserve historical findings, relationships, source depths and dates; no new mathematical proof version is introduced. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#3-a-unitary-polynomial-core-has-the-required-two-bounds) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Current isolated finding](../audits/reviews/Yin_R_F0075_v1.md#current-isolated-finding) | Whole eight-section closed analytic-curve theorem: real unitary derivative with nonzero coassociativity defect, analytic approximation, simultaneous starred graph inverse/contour closure, Laurent adjoint convergence and equality of the original closures and actual adjoints; exact C_F0025 premises retained. |

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
| argument | [Exact material](#3-a-unitary-polynomial-core-has-the-required-two-bounds) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| review | [Exact material](../audits/reviews/Yin_R_F0075_v1.md#scope-of-acceptance) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Review: [Exact material](../audits/reviews/Yin_R_F0075_v1.md#scope-of-acceptance).

Material covered by that review: [Exact material](Yin_C_F0043_v1.md).

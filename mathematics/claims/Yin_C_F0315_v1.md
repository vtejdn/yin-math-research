---
author: Yin
---

# Strong domains and the product-algebra curvature form for correlated Haar marginals

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(X\) be Haar unitary, \(V\) an arbitrary unitary free from \(X\) in their generated finite von Neumann algebra with faithful normal probability trace, and \(Y=X^*V\).
Let \(F\) be a bounded Borel map on the circle with a measurable inverse on a conull set for Haar probability \(m\).
Assume \((Z_0,Z_1)=(F(X),F(Y))\) has [full actual starred conjugate variables](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Then the pair is exchange-symmetric, has strong duals, and \(V\) has an actual scalar divided-difference vacuum \(\xi_V\).
Write \(s=\|\xi_0\|_2=\|\xi_1\|_2\) for the distinguished vacuum norms, and \(k\) for the largest single-input right-slice cost at either coordinate in either orientation divided by \(s\).
Put \(H=\xi_V V^*-1\).
If \(\|H\|_2\ge h>0\) then
\[
       k\le38+2\sqrt{4/\pi}\big((2+\sqrt2)\sqrt{1+h^{-2}}+h^{-1}\big).
                                                                     \tag{1}
\]
For every Poisson law of \(V\) with center in the open unit disk, \(k\le36+4K\) with the absolute constant \(K\) of the [four Haar derivative estimate](Yin_C_F0290_v1.md#argument), uniformly in the center and in \(F\).
If \(V\) is Haar, \(k\le3\).

Let \(\gamma_j\) be the closed partial liberation derivation at \(Z_j\).
For a bounded real symmetric kernel \(q(z,w)\) on the Haar parameter square write \(q_0,q_1\) for its evaluation in the two inner legs of \(X,Y\), respectively.
Use \(Q_j(b,u)=\operatorname{Re}\langle u,(\mathrm{id}\otimes\tau)I_b\gamma_j(u)\rangle\), where \(I_{a\otimes c}(l\otimes r)=la\otimes cr\).
For every unitary \(u\) in both graph domains that lies in \(W^*(XY)\) or \(W^*(YX)\),
\[
\begin{aligned}
 Q_0(q_0,u)+Q_1(q_1,u)
     &=(1-|\tau(u)|^2)\iint q(z,w)(1-\operatorname{Re}(z\bar w))\,dm^2,\\
 Q_0(q_0-q_1,u)
     &=-(1-|\tau(u)|^2)\iint q(z,w)\operatorname{Re}(z\bar w)\,dm^2.
\end{aligned}                                                        \tag{2}
\]
In particular for every [analytic test](Yin_C_F0314_v1.md#statement) in either product algebra, the signed curvature difference \(D(u)\) from that theorem satisfies \(D(u)\ge-2s^2\).
Here no actuality is assumed for an arbitrary choice of product law or reparametrization beyond the displayed hypothesis.

## Argument

### Actuality of the product law

By the [Haar absorption calculation](Yin_C_F0265_v1.md#removing-the-cutoff-on-the-target-polynomial-core), \(V^*X=Y^*\) is Haar and free from \(W^*(V)\); hence so is \(Y\).
Conjugating the free pair \((Y,V)\) by \(Y\) gives another free pair \((Y,Y VY^*)=(Y,YX)\) with the same laws as \((X,V)\).
The joint laws therefore give a trace-preserving automorphism sending \(X\) to \(Y\) and \(V\) to \(YX\), which exchanges \(X,Y\) and hence is an involution.
The conull inverse gives equality of the two marginal algebras before and after reparametrization in each coordinate.
In particular the generated algebra stays \(M=W^*(X,V)\).

The coordinating agent proposed testing the sum of both partial liberations on the product algebra and recovering the scalar vacuum there.
Bounded strong-star approximation by marginal polynomials puts \(X,Y,X^*,Y^*\) in the corresponding two liberation graphs: on the differentiated marginal the graph value is the inner difference \(b\otimes1-1\otimes b\), and on the other marginal it is zero.
Their products have the resulting values by bounded strong-star graph approximation and the product rule. [Measurable marginal graph calculation](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block)
In particular
\[
             \gamma_0 V=X\otimes Y-1\otimes V,\qquad
             \gamma_1 V=V\otimes1-X\otimes Y .                           \tag{3}
\]
The law \(\nu\) of \(V\) is diffuse.
Indeed if \(e=1_{\{\lambda\}}(V)\ne0\), the [kernel propagation identity](Yin_C_F0216_v1.md#a-closable-derivation-respects-the-two-kernel-projections) gives \(e\cdot\gamma_0(V)\cdot e=0\).
The proof applies to \(V-\lambda\) and its adjoint via their bounded graph approximants: the products and the differentiated Neumann polynomials at fixed resolvent parameter then pass to the same graph, and the bounded derivatives of the regularized inverses have weak limit zero as in that identity.
The double trace in (3) after compression would give zero equal to \(\tau(eX)\tau(Ye)-\lambda\tau(e)^2\); the first trace vanishes by Haar centering and freeness.

For a Laurent polynomial \(f\) put \(l(v)=f(v)/v\) on the circle and \(d_l(v,w)=(l(v)-l(w))/(v-w)\) off the null diagonal.
Its graph value at \(V\) is the outer multiplier \(d_l\) applied to (3), by the product and inverse rules.
For any separated outer multiplier \(a(v)b(w)\) applied to \(\gamma_0V\), the \(X\otimes Y\) term has zero double trace and the second contributes \(-\tau(a(V))\tau(V b(V))\).
Therefore, using \(w d_l(v,w)=d_f(v,w)-f(v)/v\),
\[
       (\tau\otimes\tau)\gamma_0(l(V))
               =-\iint d_f(v,w)\,d\nu^2+\tau(f(V)V^*).
\]
The liberation vacuum \(\eta_0=[Z_0^*,\xi_0]\) represents the left side, so the absolute value of the double integral is at most \((1+\|\eta_0\|_2)\|f(V)\|_2\).
Since \(V\) has diffuse law, its scalar divided difference on represented Laurent polynomials is well-defined; this estimate gives the required actual adjoint vacuum and \(\|\xi_V\|_2\le1+\|\eta_0\|_2\). [Liberation vacuum](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core)

### Graph unitaries in the product algebra

For \(u=f(V)\) unitary in the two indicated domains, the commutator \([V,u]=0\) gives
\[
       (L_V-R_V)\gamma_j u=(L_u-R_u)\gamma_j V,
\]
where these actions are the outer multipliers on the coarse space.
To justify Leibniz even for separate graph approximants to \(u\), first multiply each polynomial approximant by \(V\) using its bounded graph approximants.
Then pass to the limit in the commutators.
Multiplication of \(\gamma_j u_n\) by \(V\) is bounded, and multiplication of the fixed \(\gamma_j V\) by \(u_n\) converges when \(u_n\to u\) in \(L^2\), since (3) is a finite sum of bounded simple tensors.
This proves the identity by closedness.
Hence with \(d_\eta(v,w)=1_{\{|v-w|>\eta\}}(f(v)-f(w))/(v-w)\),
\[
                   d_\eta(L_V,R_V)\,\gamma_j V\ \longrightarrow\ \gamma_j u
                   \quad\hbox{in the coarse Hilbert norm}.
\]
Indeed the truncated product equals the off-diagonal cutoff of \(\gamma_j u\), and the outer diagonal is null since the spectral measure class of the two legs is dominated by \(\nu^2\).
Adding (3) in this calculation also gives \(\gamma_0u+\gamma_1u=u\otimes1-1\otimes u\).

Set \(c_q=\iint q(z,w)(1-\operatorname{Re}(z\bar w))dm^2\).
For an outer multiplier \(l(v)r(w)\) on (3), the matched complex pairings after inner insertion and right trace, before taking real parts, are
\[
    -c_q\,\tau(u^*l(V))\,\tau(Vr(V)),\qquad
     c_q\,\tau(u^*l(V)V)\,\tau(r(V)).
\]
To see the order, for \(q=a\otimes b\) the first row of (3) gives the scalar coefficient
\(\tau(Xa(X))\tau(b(X)X^*)-\tau(a(X))\tau(b(X))\), using \(Y=X^*V\) and freeness of \(X,V\).
The second row gives \(\tau(a(Y))\tau(b(Y))-\tau(Y^*a(Y))\tau(b(Y)Y)\) using \(X=VY^*\) and freeness of \(Y,V\).
These coefficients extend to general kernels by linearity and normality of the inner spectral action.
For real symmetric \(q\) the imaginary parts of the integrals of \(q z\bar w\) and \(q\bar z w\) vanish by exchanging the variables, giving the asserted coefficients.
For this fixed \(q\) both pairings are normal linear functionals of the outer spectral multiplier, by the coarse Hilbert action and the bounded right trace.
Thus the separated calculation also applies by integration to \(d_\eta\).
Summing the two rows gives the real part of
\[
             c_q\iint\overline{f(v)}d_\eta(v,w)(v-w)\,d\nu(v)d\nu(w).
\]
Bounded convergence and diffuseness give \(c_q(1-|\tau(u)|^2)\).
The inner difference \(u\otimes1-1\otimes u\), inserted at \(q_1\), contributes \((1-|\tau(u)|^2)\int q\,dm^2\), since \(u\) has scalar conditional expectation onto \(W^*(Y)\) by freeness. [Inner difference calculation](Yin_C_F0314_v1.md#adding-the-two-partial-liberations)
Subtracting this contribution proves (2) for \(W^*(V)\).
Exchange gives the matched sum for \(W^*(YX)\); both its marginal expectations are again scalar, by exchange of the ones for \(W^*(V)\).
Subtracting the same inner difference proves the second formula there as well.
For the squared curvature kernel of the common \(F_*m\) law, insert \(q(z,w)=\min\{g(F(z),F(w)),n\}\).
These are real symmetric and \(\iint g\,d(F_*m)^2\le2s^2\) by the [curvature weight](Yin_C_F0267_v1.md#statement).
This gives the asserted lower bound in the scalar cutoff limit even though the unsliced derivatives are not being estimated.

### Strong duals on the full represented core

Take \(Z=F(X)\) and write \(X=b(Z)\) with a unitary Borel function \(b\) by the generating assumption.
For the pair \((Z,Y)=(Z,b(Z)^* V)\), the original distinguished derivative at \(Z\) extends to the represented \(Z,Y\) polynomial core with the same vacuum \(\xi_0\).
Indeed approximate \(Y,Y^*\) by bounded strongly-star convergent polynomials in \(F(Y),F(Y)^*\) from the omitted marginal; their \(Z\) derivatives vanish.
Wordwise graph limits give the prescribed derivative and vacuum on the new core, which generates the same algebra.
The actual scalar vacuum of \(V\) proved above supplies the derivative at \(Y\) killing the base by the [rotated-unitary construction](Yin_C_F0265_v1.md#the-rotated-unitary-coordinate).
Thus the full [Borel phase criterion](Yin_C_F0265_v1.md#statement) gives both canonical domains for the distinguished coordinate of \((Z,Y)\).

The bounded canonical right slice on \(M\) for this coordinate is normal, by its [dense adjoint domain and normal extension](Yin_C_F0276_v1.md#a-normal-extension-and-two-normal-densities).
It commutes with left multiplication by every element of \(W^*(Y)\), first by the core product rule and then by separate normality in the input and the omitted multiplier.
It agrees on the original \(Z,F(Y)\) core with the original slice: replacing the omitted occurrences by bounded strong-star approximants in \(Y,Y^*\) gives convergence of all derivative tensors, since only the fixed \(Z,Z^*\) symbols are differentiated.
This identifies the restrictions and transfers their bounds, with the same argument for the reversed orientation.
Alternatively the finite right and left bounds give both original domains by the [two-slice theorem](Yin_C_F0072_v1.md#statement).
Exchange gives the corresponding domains and commutators at \(F(Y)\), proving strong duality on the full original pair.

If \(V\) is Haar, \(X,Y\) are free Haar coordinates by absorption and \(k\le3\) by the [free normal estimate](Yin_C_F0162_v1.md#statement).
Otherwise put \(J=\iint|b(z)-b(w)|^2|z-w|^{-2}\,d\mu(z)d\mu(w)\) for \(\mu=F_*m\), and let \(\xi_\mu\) be its scalar vacuum.
The phase criterion gives \(H\ne0\), \(\tau(H)=0\), \(J<\infty\) and \(s^2=\|\xi_\mu\|_2^2+\|H\|_2^2J\).
Its [uniform column estimate](Yin_C_F0265_v1.md#removing-the-cutoff-on-the-target-polynomial-core) bounds the base slice cost by \(36\|\xi_\mu\|_2+(2\sqrt{4/\pi}(a_V+1)+2\|H\|_2)\sqrt J\), where \(a_V\) is the scalar right-slice norm.
The [scalar weight bound](Yin_C_F0267_v1.md#statement) gives \(a_V\le(2+\sqrt2)\|\xi_V\|_2=(2+\sqrt2)\sqrt{1+\|H\|_2^2}\).
Here the equality uses \(\tau(H)=0\) and unitarity of \(V\).
If \(\|H\|_2\ge h>0\), divide by \(s\) and use \(\sqrt J/s\le1/\|H\|_2\) to obtain (1).
In the adjoint orientation the phase construction conjugates by \(b(Z)\) and uses \(V^*\) with the same scalar vacuum norm, the same norm of the centered angular vacuum and the same phase energy. [Adjoint phase estimates](Yin_C_F0265_v1.md#adjoints-and-the-strong-duals)
Exchange handles the other coordinate.

Finally suppose \(V\) has Poisson law of center \(a\), \(|a|<1\).
Then \(V_0=(V-a)(1-\bar a V)^{-1}\) is Haar and free from \(X\); this is the [Poisson angular change of variable](Yin_C_F0251_v1.md#the-liberation-vacuum-in-free-coordinates), with a scalar rotation for complex center.
By absorption \(W=X^*V_0\) is Haar free from the base \(W^*(X)\).
Put \(h=aX^*\) and \(d=\sqrt{1-|a|^2}\).
Since \(h^*W=\bar a V_0\), the output in the [disk-valued Möbius model](Yin_C_F0290_v1.md#statement) is exactly
\[
              h+d W(1+h^*W)^{-1}d
               =X^*(a+V_0)(1+\bar a V_0)^{-1}=Y .
\]
The base vacuum in this model is the same \(\xi_0\), with squared norm \(\|\xi_\mu\|_2^2+2J_{\rm M}\), where \(J_{\rm M}\) denotes its weighted divided-difference integral (2).
The [uniform Möbius column estimate](Yin_C_F0290_v1.md#uniform-column-costs-and-the-limit-at-the-unit-circle) gives \(3c_0+4K\sqrt{2J_{\rm M}}\) with \(c_0\le12\|\xi_\mu\|_2\) and \(K\) absolute.
It applies to both orientations, hence the full-core transfer and exchange give \(k\le36+4K\) even when \(a\to0\).
This bound covers mixed tests beyond the [earlier product-power estimates](Yin_C_F0251_v1.md#statement).
For unrestricted product laws, (1) still permits a sequence of increasing ratios with nonzero \(\|H\|_2\to0\).

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:05 |
| status | open |
| reason | Fix the product-algebra cancellation, scalar product vacuum and full-core estimates for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Common generating Borel reparametrizations, exact signed product forms, strong domains, away-from-Haar and uniform Poisson bounds. |
| argument | [Argument](#argument) | Exchange, hard divided differences in the liberation graphs, free spectral contractions, actual product vacuum, phase and Möbius transfer. |
| dependency | [Exchange curvature criterion](Yin_C_F0314_v1.md#statement) | Actual liberation graphs, analytic unitaries, curvature difference and conditional inner contribution. |
| dependency | [Phase-coupled unitary](Yin_C_F0265_v1.md#argument) | Haar absorption, rotated-coordinate vacuum, centered angular vacuum, exact inverse-gap energy and the original and reversed column estimates. |
| dependency | [Borel marginal liberation](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Bounded marginal approximation in the liberation graph. |
| dependency | [Kernel propagation](Yin_C_F0216_v1.md#a-closable-derivation-respects-the-two-kernel-projections) | Graph resolvent identity at an atom and compression to its two kernel projections. |
| dependency | [Liberation vacuum](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Actual adjoint of the partial liberation at the vacuum. |
| dependency | [Scalar curvature weight](Yin_C_F0267_v1.md#statement) | Bound on the curvature integral and on the scalar slice norm from the actual scalar vacuum. |
| dependency | [Normal slice extension](Yin_C_F0276_v1.md#a-normal-extension-and-two-normal-densities) | Normality of the bounded actual right slice on the von Neumann algebra. |
| dependency | [Two-slice theorem](Yin_C_F0072_v1.md#statement) | Both original graph domains from right and left core bounds. |
| dependency | [Free normal estimate](Yin_C_F0162_v1.md#statement) | Uniform constant three on freely independent normal coordinates. |
| dependency | [Poisson change of variable](Yin_C_F0251_v1.md#the-liberation-vacuum-in-free-coordinates) | Haar transform for the Poisson unitary and prior rectangular product-power scope. |
| dependency | [Disk-valued Möbius transform](Yin_C_F0290_v1.md#argument) | Both vacua, four absolute Haar derivative bounds, and the base-coordinate column estimates in both orientations. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T17:09 |
| status | proved |
| reason | Adopt the full strong-domain theorem, the product-algebra identities and the uniform Poisson and nonzero-defect bounds after independent review of the complete proof. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Common generating Borel reparametrizations, exact signed product forms, strong domains, away-from-Haar and uniform Poisson bounds. |
| argument | [Argument](#argument) | Exchange, hard divided differences in the liberation graphs, free spectral contractions, actual product vacuum, phase and M枚bius transfer. |
| dependency | [Exchange curvature criterion](Yin_C_F0314_v1.md#statement) | Actual liberation graphs, analytic unitaries, curvature difference and conditional inner contribution. |
| dependency | [Phase-coupled unitary](Yin_C_F0265_v1.md#argument) | Haar absorption, rotated-coordinate vacuum, centered angular vacuum, exact inverse-gap energy and the original and reversed column estimates. |
| dependency | [Borel marginal liberation](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Bounded marginal approximation in the liberation graph. |
| dependency | [Kernel propagation](Yin_C_F0216_v1.md#a-closable-derivation-respects-the-two-kernel-projections) | Graph resolvent identity at an atom and compression to its two kernel projections. |
| dependency | [Liberation vacuum](Yin_C_F0238_v1.md#recovering-the-divided-difference-on-the-represented-core) | Actual adjoint of the partial liberation at the vacuum. |
| dependency | [Scalar curvature weight](Yin_C_F0267_v1.md#statement) | Bound on the curvature integral and on the scalar slice norm from the actual scalar vacuum. |
| dependency | [Normal slice extension](Yin_C_F0276_v1.md#a-normal-extension-and-two-normal-densities) | Normality of the bounded actual right slice on the von Neumann algebra. |
| dependency | [Two-slice theorem](Yin_C_F0072_v1.md#statement) | Both original graph domains from right and left core bounds. |
| dependency | [Free normal estimate](Yin_C_F0162_v1.md#statement) | Uniform constant three on freely independent normal coordinates. |
| dependency | [Poisson change of variable](Yin_C_F0251_v1.md#the-liberation-vacuum-in-free-coordinates) | Haar transform for the Poisson unitary and prior rectangular product-power scope. |
| dependency | [Disk-valued M枚bius transform](Yin_C_F0290_v1.md#argument) | Both vacua, four absolute Haar derivative bounds, and the base-coordinate column estimates in both orientations. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0324_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

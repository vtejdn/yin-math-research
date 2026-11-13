---
author: Yin
---
# One-sided Borel corners and two-sided unitary changes of a normal ACSY coordinate

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X_1,\ldots,X_d\) be bounded normal generators of a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace, and suppose the tuple satisfies the [actual ACSY condition](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Fix \(i\), write \(X=X_i,\ N=W^*(X_j:j\ne i),\ H=L^2(M,\tau)\), and let \(\mu\) be the spectral law of \(X\).
Write \(\delta=\delta_i\) for its represented star-core outer derivation, \(\xi=\delta^*(1\otimes1)\), and use Hilbert inner products linear in the second argument.

For projections \(e,d_0\in N\) define \(\mu_e(B)=\tau(e1_B(X))\) and \(\mu_{d_0}\) analogously.
For any bounded Borel function \(F\) on the spectrum of \(X\) and star polynomials \(\alpha,\gamma\) on that spectrum, let \(\ell(z,w)=(\bar z-\bar w)\alpha(z)\gamma(w)\).
Then \(\ell\in\operatorname{Dom}\delta^*\) and
\[
 \left|\iint\overline{\alpha(z)\gamma(w)}(F(z)-F(w))\,d\mu_e(z)d\mu_{d_0}(w)\right|
 \le \|\delta^*\ell\|_2\,\|eF(X)d_0\|_2 .
\]
If the corner vanishes and both projections have positive trace, \(F\) has a common constant value almost everywhere for the two measures.
For complementary nonzero projections this makes \(F(X)\) scalar.
Every nontrivial von Neumann subalgebra of \(W^*(X)\) has scalar relative commutant in \(N\).
For each nonscalar \(a=F(X)\) and \(0<\eta\le1/2\), \(\|ea(1-e)\|_2\) has a positive lower bound on all projections of \(N\) with \(\eta\le\tau(e)\le1-\eta\).
Every uniformly bounded sequence \(b_n\in N\) with \(\|[b_n,a]\|_2\to0\) satisfies \(\|b_n-\tau(b_n)1\|_2\to0\).

Let \(U,V\) be unitaries in \(N\) and replace the distinguished generator by \(Y=UXV\).
The resulting tuple generates \(M\).
Its distinguished coordinate admits an actual derivation with vacuum \(U\xi V\).
Its [bounded-dual cost](Yin_C_F0201_v1.md#statement) with unrestricted value at \(1\) equals that of \(X\), allowing \(+\infty\).
The [singular projection tests](Yin_C_F0211_v1.md#statement) transport by fixed initial and final conjugations.
If \(Y\) is normal then the canonical original-core column costs agree as well.
Here for each represented core \(A\) the cost is the least extended bound \(C\) in
\[
 \left(\sum_k\|(\mathrm{id}\otimes\tau)\delta_i(a_k)\|_2^2\right)^{1/2}
 \le C\,\left\|\sum_k a_k^*a_k\right\|^{1/2}\quad(a_k\in A)
\]
over all finite columns, using the corresponding distinguished derivation.
These transport assertions also apply in the adjoint orientation.

Precisely, \(Y\) is normal if and only if \([VU,|X|^2]=0\).
If \(|X|\) is nonscalar this means \(V=\lambda U^*\) for a scalar phase \(\lambda\).
In this case any sequence \(Y_n=U_nXV_n\) with \(\|Y_nY_n^*-Y_n^*Y_n\|_2\to0\) has phases \(\lambda_n\) with \(\|V_n-\lambda_nU_n^*\|_2\to0\) and \(\|Y_n-\lambda_n U_n XU_n^*\|_2\to0\).
If \(|X|\) is scalar then \(X\) is a nonzero scalar multiple of a unitary and every such twist is normal.
The normality test applies to the translated coordinate \(X-z_0\) for each scalar \(z_0\).

## Argument

### A one-sided corner test for bounded Borel functions

For projections \(e,d\in N\) of positive trace put \(\mu_e(B)=\tau(e\,1_B(X))\) and define \(\mu_d\) similarly.
These are positive measures dominated by \(\mu\).
If a bounded Borel function \(F\) satisfies \(eF(X)d=0\), there exists a single \(c\in\mathbb C\) with \(F=c\) both \(\mu_e\)-almost everywhere and \(\mu_d\)-almost everywhere.
In particular, for \(d=1-e\) and \(0<\tau(e)<1\), \(F(X)\) is scalar.
It follows that for any nonscalar bounded Borel function of \(X\), the commutant of its generated von Neumann algebra inside \(N\) is scalar.
Indeed each projection in that commutant would satisfy the complementary corner equation.
The same conclusion holds for any nontrivial von Neumann subalgebra of \(W^*(X)\).

For a marginal star polynomial \(P\), its derivative is represented on the marginal tensor algebra by \(D_P(z,w)=(P(z,\bar z)-P(w,\bar w))/(z-w)\) off the null diagonal, by the [normal phase rule](Yin_C_F0076_v1.md#statement) and Leibniz.
The [omitted graph action](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) gives \(\bar\delta(eP(X)d)=e(\delta P(X))d\).
For marginal star polynomials \(\alpha,\gamma\), the tensor \(\ell(z,w)=(\bar z-\bar w)\alpha(z,\bar z)\gamma(w,\bar w)\) is a finite sum of core tensors in the actual adjoint domain by the [dense adjoint tensor test](Yin_C_F0206_v1.md#the-closed-derivation-and-the-central-spectral-cutoff).
Pairing the compressed derivative with \(\ell\) gives
\[
 \langle\delta^*\ell,eP(X)d\rangle
 =\iint\overline{\alpha(z,\bar z)\gamma(w,\bar w)}
       \big(P(z,\bar z)-P(w,\bar w)\big)\,d\mu_e(z)d\mu_d(w).
\]
For elementary marginal tensors the compressed pairing factors through these two measures by tracial cycling in each leg.
The identity extends to \(D_P\) by Hilbert continuity since both measures are dominated by \(\mu\).
Choose marginal star polynomials \(P_n\to F\) in \(L^2(\mu)\), using density of the star polynomials in continuous functions on the compact spectrum and of continuous functions in \(L^2(\mu)\).
Then \(eP_n(X)d\to eF(X)d\) in \(L^2(M)\), so the left side tends to \(\langle\delta^*\ell,eF(X)d\rangle\).
Domination of the two measures and boundedness of the tests allow passage to the limit on the right.
This proves the asserted inequality by Cauchy–Schwarz.
When the corner vanishes the pairing is zero for every test.
Simple marginal polynomial tensors are dense in \(L^2(\mu_e\times\mu_d)\), so \(F(z)=F(w)\) for \(\mu_e\times\mu_d\)-almost every pair.
By Fubini and positivity of both masses this forces the same constant on the two measures.
For complementary corners their sum is \(\mu\).
Testing derivatives on polynomial inputs multiplied by elements of the kernel works for every bounded Borel \(F\), including functions outside the derivation domain.

In fact, for each fixed nonscalar \(F(X)\) and \(0<\eta\le1/2\),
\[
  \inf\{\|eF(X)(1-e)\|_2:e\in N\text{ a projection},\
                      \eta\le\tau(e)\le 1-\eta\}>0
\]
whenever the set of projections in braces is nonempty.
To see this, the same test identity for general \(e,d\) passes from polynomials to \(F\) before assuming any vanishing, with left side \(\langle\delta^*\ell,eF(X)d\rangle\).
Suppose there were a sequence \(e_n\) contradicting the estimate.
The measures \(\mu_{e_n}\) have densities \(v_n\) between zero and one with respect to \(\mu\).
Take a weak-star convergent subnet of \(v_n\) in \(L^\infty(\mu)\), of limit \(v\), so \(0\le v\le1\) and \(\eta\le\int v\,d\mu\le1-\eta\).
With \(d_n=1-e_n\), each difference integral in the test identity is a sum of two products of one-variable integrals against \(v_n\mu\) and \((1-v_n)\mu\).
All of the integrands are bounded, including the merely measurable \(F\), so weak-star convergence suffices.
The left side tends to zero by Cauchy–Schwarz.
The preceding density and Fubini argument now forces \(F\) to be the same constant on \(v\mu\) and \((1-v)\mu\), contradicting the choice of \(F\).
The proof provides a positive gap for the fixed tuple, function and trace window.

More generally let \(b_n\) be in the unit ball of \(N\) and \(a=F(X)\) nonscalar.
If \(\|[b_n,a]\|_2\to0\), then \(\|b_n-\tau(b_n)1\|_2\to0\).
Indeed \(L_a-R_a\) is normal on the tracial Hilbert space, as the left and right algebras commute and \(a\) is normal, so \(\|[b_n,a^*]\|_2=\|[b_n,a]\|_2\).
The adjoints \(b_n^*\), hence the selfadjoint real and imaginary parts, also commute with \(a\) asymptotically.
The [finite-Fisher non-Gamma theorem](../audits/literature/Dab10/Yin_U001.md#dab10-u001) tests central sequences of the entire algebra generated by a selfadjoint tuple.
Here the tested sequence lies in \(N\) and its only commutator test is the chosen measurable function of the remaining normal coordinate.
The variance of \(b_n\) is the sum of the variances of those two parts by traciality.
If it does not tend to zero, pass to one selfadjoint part \(z_n\) of positive variance bounded away from zero along a subsequence, and take a further subsequence whose scalar laws converge weakly on \([-1,1]\).
The limiting law has positive variance by boundedness, so there is a nonatom \(s\) strictly between two support points.
The projections \(e_n=1_{[-1,s]}(z_n)\) then have traces bounded away from both zero and one.
For each continuous \(g\) on \([-1,1]\), uniform polynomial approximation and the commutator product rule give \(\|[g(z_n),a]\|_2\to0\).
Choose continuous cutoffs with values in \([0,1]\) agreeing with \(1_{[-1,s]}\) outside arbitrarily short closed neighborhoods of \(s\) of arbitrarily small limiting mass.
The limsup of \(\|g(z_n)-e_n\|_2^2\) is bounded by that closed neighborhood's limiting mass by weak convergence.
Since \(\|[g(z_n)-e_n,a]\|_2\le2\|a\|\,\|g(z_n)-e_n\|_2\), this gives \(\|[e_n,a]\|_2\to0\).
In particular \(\|e_na(1-e_n)\|_2\to0\), contradicting the projection gap.

Consequently \(Y=UXV\) for unitaries \(U,V\in N\) is normal exactly when \(VU\) commutes with \(|X|^2\), by computing \(Y^*Y\) and \(YY^*\).
If \(|X|\) is nonconstant, the commutant just proved forces \(VU\) to be a scalar phase.
Thus all normal twists of this form are \(Y=\lambda UXU^*\) with \(|\lambda|=1\).
If \(|X|\) is constant, normality and \(X\ne0\) make \(X\) a scalar multiple of a unitary, and every two-sided unitary twist remains in this class.
In particular the same argument applies to \(X-z_0\) to test circles about any prescribed center.
There is an approximate version at each fixed \(X\) of nonconstant modulus.
For \(Y_n=U_n X V_n\) with omitted-algebra unitaries put \(W_n=V_nU_n\).
Unitary invariance gives
\[
  \|Y_nY_n^*-Y_n^*Y_n\|_2=\|[W_n,|X|^2]\|_2 .
\]
If the left side tends to zero, the bounded-sequence result forces \(\|W_n-\tau(W_n)1\|_2\to0\), in particular \(|\tau(W_n)|\to1\).
Taking the phase \(\lambda_n\) of that trace eventually gives \(\|V_n-\lambda_n U_n^*\|_2\to0\) and \(\|Y_n-\lambda_nU_n XU_n^*\|_2\to0\).

### Transport at the distinguished coordinate

For any \(U,V\in N\) unitary consider the tuple with \(Y=UXV\) in the distinguished position and with all omitted coordinates unchanged.
Its von Neumann algebra is still \(M\), as \(X=U^*YV^*\).
Let \(J_{U,V}\) be the unitary on the coarse Hilbert space given by \(J_{U,V}(a\otimes b)=aU^*\otimes V^* b\).
It commutes with both outer actions.
The original closed derivation on the enlarged algebra \(N\langle X,X^*\rangle\) obeys Leibniz and kills \(N\).
Indeed, for each finite word approximate its omitted coefficients strongly-star by uniformly bounded omitted-core polynomials using [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001).
The evaluated words converge strongly-star on bounded sets, and in each finite expansion of their derivatives the outer factors converge strongly on the fixed coarse tensors, giving Hilbert graph convergence and Leibniz.
The same algebra is \(N\langle Y,Y^*\rangle\).
There \(J_{U,V}\bar\delta\) is a derivation, and its value at \(Y\) is \(J_{U,V}(U\otimes V)=1\otimes1\).
Its restriction to the represented target star core has actual vacuum \(U\xi V\).
In fact, taking the double trace after \(J_{U,V}\) on \(\bar\delta a\) equals the double trace on \(U^*(\bar\delta a)V^*=\bar\delta(U^*aV^*)\) by cyclicity in each leg.
Its value is \(\langle\xi,U^*aV^*\rangle=\langle U\xi V,a\rangle\).
Thus the distinguished vacuum preserves its norm even for omitted unitaries outside the original polynomial core.

The bounded-dual cost at this coordinate is unchanged.
Take a normal optimal bounded witness \(E:M\to H\) from [C_F0201](Yin_C_F0201_v1.md#the-hilbert-values-and-the-represented-norm) whenever its cost is finite.
Specifically, bounded finite word minimizers yield by weak extraction a bounded map \(T:B=C^*(X_1,\ldots,X_d)\to H\) satisfying the required commutators on \(B\).
The represented normal quotient \(\pi:B^{**}\to M\) has a central summand inverse \(j:M\to eB^{**}\).
The extension \(T^{**}\) takes values in the reflexive space \(H\) and is weak-star-to-weak continuous.
Weak-star density extends the identities to \(B^{**}\), with the trace functional \(\tau\pi\), and \(j(X_k a)=\iota(X_k)j(a)\) for the canonical inclusion \(\iota:B\to B^{**}\).
Hence \(E=T^{**}j\) satisfies the identities on \(M\) with optimal norm.
The source and target may have different represented \(C^*\)-algebras, so this step is applied separately in each direction.
The map \(E\) commutes with the left omitted generators, hence with their adjoints by [bounded-map Fuglede commutation](Yin_C_F0070_v1.md#statement-and-interfaces), and therefore with every left omitted star polynomial.
For fixed \(a\in M\), the maps \(b\mapsto E(ba)\) and \(b\mapsto bE(a)\) are ultraweak-to-weak continuous by separate normality of multiplication and normality of the left representation on \(H\).
Their equality thus extends to every \(b\in N\).
Define \(E'(a)=E(aV^*)U^*\) on \(M\).
It has the same norm and is left \(N\)-linear.
The old commutator at \(VaV^*\), left \(N\)-linearity, and \(\tau(VaV^*)=\tau(a)\) give
\[
 E'(Ya)=U E(XVaV^*)U^*=Y E'(a)+\tau(a)1 .
\]
The inverse twist \((U^*,V^*)\) gives the reverse inequality, including infinite costs.
The bounded-cost comparison uses normality of the omitted generators and applies to both distinguished generators irrespective of their normality.

For the canonical right slice \(E_0=(\mathrm{id}\otimes\tau)\bar\delta\) on the enlarged algebra the twisted slice is exactly \(E'_0(a)=E_0(aV^*)U^*\), by cyclicity on the second leg and \(\bar\delta(V^*)=0\).
If \(Y\) is normal, the two original-core column costs for this distinguished coordinate are equal, even without an assumption of actual vacua for the other target coordinates.
To verify the norm issue when omitted coefficients are merely measurable, suppose the old column cost is \(C<\infty\).
For any finite column \(a=(a_1,\ldots,a_m)^{\mathsf T}\) in \(M\), matrix Kaplansky approximation gives columns \(a_\lambda\) of old star polynomials converging in \(L^2\) in each entry with \(\limsup\|a_\lambda\|_{\rm col}\le\|a\|_{\rm col}\).
Indeed embed the column in the first column of \(M_m(M)\), approximate by uniformly norm-bounded matrices over the generated \(C^*\)-algebra, project to their first columns, and approximate their finitely many entries in operator norm by polynomials.
Weak compactness of the Hilbert sum and the weakly closed graph of the closed canonical slice, whose closability follows from the [actual vacuum](../audits/literature/ACSY24/Yin_U001.md#canonical-contraction-dual), extend the column bound with the same constant to all \(M\).
On the enlarged algebra this Hilbert closure agrees with the indicated sliced graph value by the coefficient approximation already proved.
Right multiplication of each input by \(V^*\) preserves its column norm, and right multiplication of each output by \(U^*\) preserves the Hilbert sum norm.
Thus the new original-core column cost is at most \(C\).
For the reverse use the same reasoning on the target with the transported actual derivation.
For clarity on uniqueness when \(Y\) is normal, restrict that derivation to marginal star polynomials in \(Y\) and project both Hilbert tensor legs to \(L^2(W^*(Y))\).
These projections are marginal bimodule maps, and the adjoint vacuum of the resulting marginal derivation is the marginal projection of \(U\xi V\).
Thus the single-generator case of [normal marginal diffuseness](Yin_C_F0076_v1.md#statement) makes the law of \(Y\) diffuse.
The omitted marginals were already diffuse by the source hypotheses.
For any normal target generator \(Z\), the outer difference \(L_Z\otimes I-I\otimes R_Z\) has zero kernel, since the spectral measures on each Hilbert leg are absolutely continuous with respect to the diffuse trace law, and their product gives the diagonal zero mass on each simple tensor.
Differentiating \(ZZ^*=Z^*Z\) therefore determines the value at \(Z^*\) uniquely from the prescribed value at \(Z\), hence determines the derivation on the target core.
This justifies speaking of its canonical column cost even when only the distinguished target vacuum is known.
The inverse twist restores the original derivation on its core, by graph approximation with the identical omitted algebra and \(J_{U^*,V^*}=J_{U,V}^{-1}\).
This proves equality as extended real numbers.
The same transport applies in the adjoint orientation with \(Y^*=V^*X^*U^*\).
Finally \(Y-b=U(X-U^*bV^*)V\) permutes all \(b\in N\) and conjugates their initial and final singular projections by fixed unitaries.
It preserves all trace and orthogonality data in the [singular projection test](Yin_C_F0211_v1.md#statement).
These conclusions concern the distinguished coordinate.
A derivation at an omitted coordinate can differentiate the twisting unitaries and needs its own argument.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T16:33 |
| status | open |
| reason | The Borel corner pairing, asymptotic rigidity and distinguished-coordinate transports are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Corner estimate, scalarity, positive gap, bounded-sequence rigidity and normal and unrestricted two-sided twist conclusions. |
| argument | [Argument](#argument) | Compression against adjoint-domain marginal tensors, weak limits, spectral cuts, two-sided transports and graph and bidual extensions. |
| dependency | [Normal marginal phase](Yin_C_F0076_v1.md#statement) | Diffuseness, forced starred values, closability and adjoint orientation. |
| dependency | [Omitted graph action](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Derivative of the compressed polynomial and validity of omitted coefficients. |
| dependency | [Adjoint core tensors](Yin_C_F0206_v1.md#the-closed-derivation-and-the-central-spectral-cutoff) | Actual adjoint-domain test tensors. |
| dependency | [Normal bounded-dual witness](Yin_C_F0201_v1.md#the-hilbert-values-and-the-represented-norm) | Normal bidual transfer and attainment of the full-domain cost. |
| dependency | [Homogeneous Fuglede commutation](Yin_C_F0070_v1.md#statement-and-interfaces) | A bounded witness commuting with left normal generators commutes with their adjoints. |
| dependency | [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Bounded approximants for measurable coefficients and matrix columns. |
| dependency | [Right-slice closability](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | The adjoint vacuum makes the original-core slice closable for each transported derivation. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T16:45 |
| status | proved |
| reason | Adopt the Borel corner test and normal two-sided change theorem after independent whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Corner estimate, scalarity, positive gap, bounded-sequence rigidity and normal and unrestricted two-sided twist conclusions. |
| argument | [Argument](#argument) | Compression against adjoint-domain marginal tensors, weak limits, spectral cuts, two-sided transports and graph and bidual extensions. |
| dependency | [Normal marginal phase](Yin_C_F0076_v1.md#statement) | Diffuseness, forced starred values, closability and adjoint orientation. |
| dependency | [Omitted graph action](Yin_C_F0217_v1.md#the-closed-derivation-on-the-omitted-coordinate-algebra) | Derivative of the compressed polynomial and validity of omitted coefficients. |
| dependency | [Adjoint core tensors](Yin_C_F0206_v1.md#the-closed-derivation-and-the-central-spectral-cutoff) | Actual adjoint-domain test tensors. |
| dependency | [Normal bounded-dual witness](Yin_C_F0201_v1.md#the-hilbert-values-and-the-represented-norm) | Normal bidual transfer and attainment of the full-domain cost. |
| dependency | [Homogeneous Fuglede commutation](Yin_C_F0070_v1.md#statement-and-interfaces) | A bounded witness commuting with left normal generators commutes with their adjoints. |
| dependency | [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Bounded approximants for measurable coefficients and matrix columns. |
| dependency | [Right-slice closability](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | The adjoint vacuum makes the original-core slice closable for each transported derivation. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0235_v1.md#whole-proof-finding) | Borel corners, uniform gaps, asymptotic scalarity, both orientations of the change of coordinates and original-core column costs. |

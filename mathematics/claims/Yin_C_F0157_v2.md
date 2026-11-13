---
author: Yin
---
# An exact vacuum and dual-domain criterion for bounded Hermitian Gaussian coordinates

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(Z\) be bounded normal with diffuse compact spectral law \(\mu\) in the abelian tracial algebra \(N=W^*(Z)\).
Let \(S\) be a standard semicircular element free from \(N\), and equip \(M=W^*(N,S)\) with its faithful normal probability trace.
In its relative Wick representation put \(H_n=L^2(\mu^{n+1})\), with \(H_0=L^2(N)\) and \(\Psi(a)\in H_1\) the first-chaos vector of a kernel \(a\).
For a measurable Hermitian kernel \(a(z,w)=\overline{a(w,z)}\) set \(b=|a|\) and
\[
 \rho(a)^2=\mathop{\mathrm{ess\,sup}}_w\int b(z,w)^2\,d\mu(z).
\]
The pure first-chaos vector \(a\) is represented by a bounded selfadjoint Gaussian coordinate \(T_a\in M\) exactly when \(\rho(a)<\infty\).
In that case \(\rho(a)\le\|T_a\|\le2\rho(a)\).

Assume this row bound and put \(M_a=W^*(Z,T_a)\).
Then the following are equivalent.

1. The normal pair \(X=(Z,T_a)\) satisfies \(\mathsf A\) on the original represented star-polynomial core, with coarse coefficient space \(L^2(M_a)\otimes_2 L^2(M_a)\) and actual vacuum adjoints.
2. The pair satisfies \(\mathsf S\) in \(L^2(M_a)\), with generator-first commutators and the domains of every dual and its actual adjoint containing \(M_a\Omega\).
3. The scalar divided difference on \(\mathbb C[Z,Z^*]\) has an actual vacuum \(\xi_N\in L^2(N)\), the kernel \(b\) is positive almost everywhere, and
   \[
     \|1/b\|_{L^2(\mu^2)}<\infty,\qquad
     \|\chi_b\|_{L^2(\mu^3)}<\infty,\qquad
     \chi_b(z,w,v)=
     \frac{b(w,v)/b(z,w)-b(z,w)/b(w,v)}{\bar z-\bar v}.
     \tag{1}
   \]

Use the conditions \(\mathsf A,\mathsf S,\mathsf F\) of the [Task contract](../tasks/Yin_T_F0011_v1.md#contract).
The endpoint diagonal in (1) is null.
Under these equivalent conditions \(M_a=M\) and the pair satisfies the bare condition \(\mathsf F\).
Both original canonical contractions \(E_j=\overline{(\mathrm{id}\otimes\tau)\partial_j}\) and their actual adjoints contain \(M\Omega\) in their domains.
For \(\theta=a/b\) off the zero set, extended by one there, the actual vacua are
\[
  \xi_Z=\xi_N+\theta(z,w)\theta(w,v)\chi_b(z,w,v),\qquad
  \xi_T=\Psi(1/\overline a).
  \tag{2}
\]
With \(K_0=\sqrt{4/\pi}(5+2\sqrt{27})\) and \(K=\sqrt{K_0^2+8}\), the norm bounds from \((M,\|\cdot\|)\) to \(L^2(M)\) are
\[
 \|E_Z\|\le K\|\xi_Z\|_2,\quad
 \|E_Z^*\|\le(1+K)\|\xi_Z\|_2,\quad
 \|E_T\|\le2\|\xi_T\|_2,\quad
 \|E_T^*\|\le\|\xi_T\|_2.
 \tag{3}
\]
These norms concern the restrictions to bounded vectors.
The adjoint-reversed \(Z\) contraction has the same \(K\|\xi_Z\|_2\) bound, giving the curvature-form lower estimate of [C_F0156](Yin_C_F0156_v1.md#quantitative-bounds-and-curvature-form) at its stated analytic-unitary tests.
This preserves the full [bounded-kernel criterion](Yin_C_F0157_v1.md#statement) and extends it to all bounded first-chaos coordinates in this model.
The example below has unbounded positive kernel and its amplitude clippings stay a positive operator-norm distance from the coordinate.

## Argument

### Bounded coordinates, phase, and generation

In the [relative Wick representation](Yin_C_F0153_v1.md#relative-degree-with-an-arbitrary-abelian-base) creation by \(a\) sends \(f(z_1,\ldots,z_{n+1})\) to \(a(z_0,z_1)f(z_1,\ldots,z_{n+1})\).
Its squared norm on \(f\) is our row integral at \(z_1\) integrated against \(|f|^2\), so its operator norm equals \(\rho(a)\), already on \(H_0\).
Hermiticity gives the Gaussian field as this creation plus its adjoint.
For \(m\ge1\) set \(b_m=\min(b,m)\), \(a_m=\theta b_m\).
The bounded-kernel coordinates \(T_{a_m}\) belong to \(M\) and have norm at most \(2\rho(a)\).
Their vectors \(a_m\) converge to \(a\) in \(L^2\).
Uniformly bounded left multipliers converging in tracial \(L^2\) converge strongly, by testing on the dense bounded right multiples of the vacuum.
Their limit in \(M\) is \(T_a\), with the asserted creation action by testing the clipped creations and their matrix coefficients on each Wick degree.
Conversely, if the vector of a bounded element is the pure first-chaos vector \(a\), its action on \(f\in N\) is right multiplication of that vector by \(f\), namely \(a(z,w)f(w)\).
Testing indicators of level sets of the row integral gives \(\rho(a)\le\|T_a\|\).
Faithfulness gives uniqueness from the value at the vacuum.

The phase unitary from [v1](Yin_C_F0157_v1.md#argument) is a trace-preserving automorphism of \(M\), fixes \(N\), and multiplies each path by its successive edge phases.
It carries \(T_{b_m}\) to \(T_{a_m}\), hence carries \(T_b\) to \(T_a\) by strong convergence.
It intertwines the target cores, coefficient actions and actual adjoints, so it suffices to treat the positive case, initially allowing a zero set.

Whenever \(b>0\) almost everywhere, the span of \(f(Z)T_bg(Z)\Omega\), \(f,g\in N\), is dense in \(H_1\).
Indeed finite sums of product functions are dense in \(L^2(b^2\,d\mu^2)\) by rectangle approximation for the finite measure \(b^2\,d\mu^2\), and multiplication by \(b\) maps that space unitarily onto \(L^2(\mu^2)\).
In particular \(S\Omega\in L^2(M_b)\), so the trace-preserving conditional expectation onto \(M_b\) fixes the bounded element \(S\).
This gives \(M_b=M\).

### Necessary integrals on the target core

Assume \(\mathsf A\) for \(X=(Z,T_b)\).
The normal relation forces the scalar divided difference on \(Z,Z^*\) for \(\partial_Z\) and forces \(\partial_T Z^*=0\), as in [the actual moment tests](Yin_C_F0156_v1.md#actual-target-moment-tests).
Orthogonally projecting the \(Z\) vacuum to \(L^2(N)\) gives \(\xi_N\).
Embedding the intrinsic \(L^2(M_b)\) into the relative Wick space, the \(T\) vacuum paired with \(f(Z)T_b g(Z)\) gives \(\tau(f)\tau(g)\) for marginal polynomials \(f,g\).
Consequently \(b\,\overline{P_{H_1}\xi_T}=1\) almost everywhere, since this product is in \(L^1\) and product polynomials determine finite measures.
This excludes zeros of positive measure, gives \(1/b\in L^2\), and justifies generation by the preceding paragraph.

For smooth marginal \(f_0,f_2\) with positively separated supports and a marginal polynomial \(f_1\), test the \(Z\) vacuum on \(p=f_0T_b f_1T_b f_2\).
Smooth graph approximation of the marginal factors and boundedness of \(T_b\) justify the vacuum product rule exactly as in the [bounded-kernel calculation (M1)](Yin_C_F0156_v1.md#actual-target-moment-tests).
The conditional expectation uses \(\eta_b(f)(z)=\int b(z,w)^2 f(w)\,d\mu(w)\), bounded by \(\rho(b)^2\|f\|_\infty\).
The degree-zero part vanishes by the separated endpoints, and the degree-two coefficient has kernel \(f_0(z)b(z,w)f_1(w)b(w,v)f_2(v)\).
These Wick identities follow by \(L^2\) convergence of the bounded products with the clipped fields and by domination of the kernels, since
\[
 \int b(z,w)^2 b(w,v)^2\,d\mu^3
 =\int\!\left(\int b(z,w)^2d\mu(z)\right)^2\,d\mu(w)\le\rho(b)^4 .
\]
In the Leibniz expansion the middle derivative has centered one-field factors on both sides.
The two endpoint terms give
\[
 \langle\xi_Z,p\rangle
 =\int f_0(z)f_1(w)f_2(v)
       \frac{b(w,v)^2-b(z,w)^2}{z-v}\,d\mu^3.
\]
Here the squared kernels are integrable and the displayed denominator is bounded away from zero on the test supports.
Pairing the degree-two kernel against \(P_{H_2}\xi_Z\) gives another integrable density by Cauchy--Schwarz.
These tests determine both densities off the null endpoint diagonal by localization and polynomial density in the middle variable.
Division by \(b(z,w)b(w,v)>0\) there identifies \(P_{H_2}\xi_Z=\chi_b\), proving (1).

### Clipping preserves the vacuum and dual bounds

Assume the scalar and integral conditions in item 3.
On each clipped positive kernel the [bounded-kernel theorem](Yin_C_F0157_v1.md#statement) supplies the exact vacua \(\xi_{Z,m}=\xi_N+\chi_{b_m}\), \(\xi_{T,m}=\Psi(1/b_m)\), full canonical domains, and (3) for the clipped vacua.
Indeed \(b_m^{-2}\le b^{-2}+1\) for \(m\ge1\).
Since upper truncation of a real logarithm contracts distances and \(|r-r^{-1}|=2\sinh(|\log r|)\), one has \(|\chi_{b_m}|\le|\chi_b|\).
Thus the two vacua converge in their fixed Wick spaces in \(L^2\) by dominated convergence.

The normal tuples \(X_m=(Z,T_{b_m})\) have a common operator cutoff and converge in star moments to \(X\), since \(T_{b_m}\to T_b\) in \(L^2\).
A bounded canonical restriction \(E_{j,m}\) supplies the commutator for \(X_m\), and \(-E_{j,m}^*\) on bounded vectors supplies it for the adjoint tuple by taking matrix elements.
Both signs therefore have uniformly bounded global dual norms by (3) on the clipped tuples.
The [closed sublevels and normal two-sided criterion](Yin_C_F0201_v2.md#statement) yield \(\mathsf S(X)\).
For this normal generating pair in its intrinsic algebra, [C_F0070 Part C](Yin_C_F0070_v1.md#statement) gives \(\mathsf A(X)\), completing the equivalence.
The [canonical compatibility theorem](Yin_C_F0075_v1.md#statement) now gives the original canonical closures and full adjoint domains.

To identify all vacuum components and the canonical constants, fix a star polynomial \(p\) in the target variables.
The starred-generator derivatives are forced on the normal pair by the diffuse marginal relation, as in the necessity argument.
For the \(Z\) coordinate these generator values are \(1\otimes1\) on \(Z\), the fixed marginal phase on \(Z^*\), and zero on \(T_{b_m}\) or \(T_b\).
For the \(T\) coordinate they are zero on \(Z,Z^*\) and \(1\otimes1\) on the selfadjoint field.
Thus each derivative of \(p(X_m)\) is a finite sum of the same fixed coarse vectors multiplied by uniformly bounded polynomial words converging strongly with their adjoints in \(M\).
Both coarse actions are strongly continuous on such bounded sets, by testing elementary tensors then using density.
The resulting coarse derivatives converge in Hilbert norm to the derivatives of \(p(X)\).
Passing the clipped vacuum pairings to the limit proves (2) for \(b\), by density of the target core in \(L^2(M)\).
Applying the two bounded partial traces to the coarse derivatives also gives convergence for both canonical core contractions and their adjoint-reversed versions.

To retain the canonical constants in (3), take weak limits of the normalized operators on the common tracial algebra.
For either coordinate consider the clipped canonical contraction and its adjoint restriction on \(M\).
Their norms from \(M\) to \(L^2(M)\) are uniformly bounded by the corresponding clipped estimates.
The maps are weakly relatively compact pointwise on \(M\) by [weak compactness of Hilbert balls and product compactness](../audits/literature/Keh25/Yin_U001.md#keh25-u001).
The clipped core adjoint formula writes \(E_{j,m}^*p(X_m)\) as \(p(X_m)\xi_{j,m}\) minus the adjoint-reversed contraction on \(p(X_m)\), as in [C_F0156](Yin_C_F0156_v1.md#quantitative-bounds-and-curvature-form).
The same formula holds on the limiting core by the derivation rule and its actual vacuum pairing.
Thus the above convergences also give strong \(L^2\) convergence of the adjoints on each such moving core vector.

Take a common pointwise weakly convergent subnet of \(E_{j,m}, E_{j,m}^*\) on bounded inputs, with limits \(B,B'\).
Testing fixed bounded inputs in the adjoint identity gives \(\langle h,Bv\rangle=\langle B'h,v\rangle\) on \(M\).
For fixed \(h\in M\) and \(p_m=p(X_m)\), the difference \(\langle h,E_{j,m}(p_m-p(X))\rangle\) has modulus at most \(\|E_{j,m}^*h\|_2\|p_m-p(X)\|_2\), which tends to zero.
Thus \(B\) agrees on the limiting core with its canonical contraction.
For fixed bounded \(v\), testing against every core element in the adjoint identity shows \(B'v=E_j^*v\) by the definition of the actual core adjoint.
Now testing \(Bv\) against all bounded \(h\), using \(B'h=E_j^*h\) and the known full domain of \(E_j\), gives \(Bv=E_jv\).
Weak lower semicontinuity at each fixed \(v\) and convergence of the clipped vacuum norms give all four constants (3).
For the adjoint-reversed \(Z\) contraction use the bounded-input formula \(p\xi_{Z,m}-E_{Z,m}^*p\).
This core formula extends to bounded inputs by Kaplansky approximation and weak closedness of the canonical graphs, since the clipped contractions and adjoints are bounded on the operator unit ball.
The same argument for the limiting strong tuple applies to its adjoint-reversed canonical contraction, by canonical compatibility for the adjoint tuple.
Its value \(p\xi_Z-E_Z^*p\) is therefore the pointwise weak limit of the clipped values, giving the sharper bound.
Inserting the two \(K\)-bounds into the [normal mixed-energy identity](Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) as in [C_F0156](Yin_C_F0156_v1.md#quantitative-bounds-and-curvature-form) gives \(Q_g(u)\ge-(4K+2K^2)\|\xi_Z\|_2^2\) on its analytic-unitary tests.
Finally the phase unitary transports (2), the contractions, their constants and all the actual domains back to \(a\).

### Infinite spectral blocks with no convergence in operator norm

Take normalized area measure on the unit disk and \(Z(z)=z\).
It has the actual scalar vacuum because \(\sup_z\int|z-v|^{-1}\,d\mu(v)\le4\), by integration on the disk of radius two about \(z\).
Fubini and antisymmetry give a bounded representing density for the scalar functional \(\int(f(z)-f(v))/(z-v)\,d\mu^2\) on the marginal polynomials.
Choose disjoint disks \(F_n\) centered at \(2^{-n}\) with radii \(r_n=2^{-n-3}\), \(n\ge1\), all inside the unit disk, and put \(t_n=\mu(F_n)=r_n^2\).
Let \(b(z,w)=t_n^{-1/2}\) on \(F_n^2\), and let \(b=1\) elsewhere.
Then \(\rho(b)^2\le2\) and \(1/b\le1\).
For \(w\in F_n\), the quotient numerator in (1) differs from zero precisely when one endpoint lies in \(F_n\) and the other lies outside it, up to null sets.
The square of the curvature norm equals
\[
 2\sum_n t_n(t_n^{-1/2}-t_n^{1/2})^2 J_n,\qquad
 J_n=\int_{F_n\times F_n^c}|z-v|^{-2}\,d\mu(z)d\mu(v).
\]
For \(z\in F_n\) with boundary distance \(s\), integration over \(s\le|v-z|\le2\) gives at most \(2\log(2/s)\).
Averaging this on the disk yields \(J_n\le2t_n(\log(2/r_n)+3/2)\), since \(2\int_0^1 u\log(1/(1-u))\,du=3/2\).
The resulting series converges, so (1) and both strong domains hold.
Nevertheless \(T_b-T_{b_m}\) on the normalized degree-zero indicator of \(F_n\) has Hilbert norm \((1-m\sqrt{t_n})_+\).
Letting \(n\) grow gives \(\|T_b-T_{b_m}\|\ge1\) at every fixed cap \(m\ge1\).

## Scope

This deduction for [T_F0011](../tasks/Yin_T_F0011_v1.md#contract) covers the full bounded-coordinate class in the stated one-field Wick model.
It leaves the converse from bare \(\mathsf F\) and the implication \(\mathsf A\Rightarrow\mathsf S\) for arbitrary correlated normal tuples open.

## Assessment history

### Decision bounded-gaussian-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T10:32 |
| status | open |
| reason | Complete argument for the row criterion and actual vacuum and dual equivalence, including the original canonical constants and a strict infinite-block example, pending independent proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Bounded-coordinate characterization, intrinsic equivalence, vacua, full canonical domains, quantitative constants and spectral-block example. |
| argument | [Argument](#argument) | Wick norm, phase and generation, intrinsic moment tests, clipped moment limits, identification of canonical restrictions and domain estimates. |
| dependency | [Bounded Hermitian kernels](Yin_C_F0157_v1.md#statement) | All equivalences, explicit vacua and estimates on the clipped coordinates, and the measurable phase unitary with its transport action. |
| dependency | [Relative Wick representation](Yin_C_F0153_v1.md#relative-degree-with-an-arbitrary-abelian-base) | Relative path Hilbert spaces and creation and annihilation for a standard semicircular free from the abelian base. |
| dependency | [Actual moment tests](Yin_C_F0156_v1.md#actual-target-moment-tests) | Forced marginals, smooth separated endpoint graph tests and the two endpoint Leibniz terms, with row integrability verified here. |
| dependency | [Canonical estimates](Yin_C_F0156_v1.md#quantitative-bounds-and-curvature-form) | Clipped contraction constants, actual adjoint formula and the analytic-unitary curvature identity and test scope. |
| dependency | [Closed norm sublevels](Yin_C_F0201_v2.md#statement) | Uniform bounds at common cutoff give both finite dual optima at the limit, equivalent to the normal strong condition. |
| dependency | [Actual derivations from strong duals](Yin_C_F0070_v1.md#statement) | Part C for a normal generating tuple in its intrinsic algebra. |
| dependency | [Compactness](../audits/literature/Keh25/Yin_U001.md#keh25-u001) | Products of weakly compact Hilbert balls for the common-algebra pointwise weak limits. |
| dependency | [Normal mixed energy](Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) | Actual normal ACSY energy identity for analytic unitaries before any additional growth estimate. |
| dependency | [Canonical domain comparison](Yin_C_F0075_v1.md#statement) | Part 4 gives the full original canonical and actual adjoint domains under the normal strong condition. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T13:22 |
| status | proved |
| reason | Adopt the equivalence for every bounded Hermitian first-chaos coordinate and the quantitative canonical domain and vacuum formulas after whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Bounded-coordinate characterization, intrinsic equivalence, vacua, full canonical domains, quantitative constants and spectral-block example. |
| argument | [Argument](#argument) | Wick norm, phase and generation, intrinsic moment tests, clipped moment limits, identification of canonical restrictions and domain estimates. |
| dependency | [Bounded Hermitian kernels](Yin_C_F0157_v1.md#statement) | All equivalences, explicit vacua and estimates on the clipped coordinates, and the measurable phase unitary with its transport action. |
| dependency | [Relative Wick representation](Yin_C_F0153_v1.md#relative-degree-with-an-arbitrary-abelian-base) | Relative path Hilbert spaces and creation and annihilation for a standard semicircular free from the abelian base. |
| dependency | [Actual moment tests](Yin_C_F0156_v1.md#actual-target-moment-tests) | Forced marginals, smooth separated endpoint graph tests and the two endpoint Leibniz terms, with row integrability verified here. |
| dependency | [Canonical estimates](Yin_C_F0156_v1.md#quantitative-bounds-and-curvature-form) | Clipped contraction constants, actual adjoint formula and the analytic-unitary curvature identity and test scope. |
| dependency | [Closed norm sublevels](Yin_C_F0201_v2.md#statement) | Uniform bounds at common cutoff give both finite dual optima at the limit, equivalent to the normal strong condition. |
| dependency | [Actual derivations from strong duals](Yin_C_F0070_v1.md#statement) | Part C for a normal generating tuple in its intrinsic algebra. |
| dependency | [Compactness](../audits/literature/Keh25/Yin_U001.md#keh25-u001) | Products of weakly compact Hilbert balls for the common-algebra pointwise weak limits. |
| dependency | [Normal mixed energy](Yin_C_F0078_v1.md#6-the-actual-normal-mixed-energy-and-both-canonical-domains) | Actual normal ACSY energy identity for analytic unitaries before any additional growth estimate. |
| dependency | [Canonical domain comparison](Yin_C_F0075_v1.md#statement) | Part 4 gives the full original canonical and actual adjoint domains under the normal strong condition. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0165_v2.md#finding) | The row characterization, complete proof, nine declared inputs and infinite-block example. |

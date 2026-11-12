---
author: Yin
---
# The remaining amenable obstruction after kernel localization

This structural reassessment was made on 2026-11-12 under [A0001](../tasks/Yin_T_A0001_v1.md#contract), following Yin's instruction to pursue the algebraic and analytic interaction without probing concrete examples.
The amenable equivalence between all-matrix Atiyah integrality and the scalar group-ring domain conjecture is treated as known from the outset.
The [existing source comparison](../ledger/Yin_L_A0002_v1.md#denominator-clearing-and-finite-propagation) already records that equivalence.
Reproving it, changing its analytic coordinates, or presenting another family containing every original matrix does not establish progress on its unresolved premise.

## What the retained progress actually establishes

The [normal-hopping construction](../claims/Yin_C_A0011_v1.md#statement) contains arbitrary group-ring kernels, so normal hopping by itself does not simplify the full target.
The [finite-central-parameter obstruction](../claims/Yin_C_A0012_v5.md#statement) shows why the retained constructions cannot universally replace small positive spectrum by a gap while preserving the unknown kernel.
The [finite-central-coefficient comparison](Yin_L_A0029_v1.md) confines its faithful group-ring realization to virtually abelian groups.
These are restrictions on particular mechanisms, not impossibility results for every analytic or algebraic approach.

The [complete amenable localization argument](../claims/Yin_C_A0001_v2.md#statement) extends finite-support kernel density to the actual affiliated rational closure, with an explicit realization-dependent boundary error.
This improves the available interface and handles unbounded denominators, but still does not constrain the dimension of the resulting scalar annihilator to be an integer.
Its finite projective resolution formula identifies where an independent algebraic constraint would enter.
The missing step is a structure theorem for the actual principal annihilator, not another reduction from matrices to scalars.

## What the known trace theorem sees

For torsion-free amenable \(G\), put \(B=\mathbb CG\), \(N=\mathcal N(G)\), and \(U=\mathcal U(N)\).
The [BCM04 interface](../audits/literature/BCM04/Yin_U001.md#amenable-projective-trace) already gives
\[
(\operatorname{Tr}\otimes\tau)(E)
=\operatorname{rank}_{\mathbb C}\varepsilon(E)\in\mathbb Z
\quad(E^2=E\in M_r(B)).
\]
It is therefore unnecessary to seek a new integer-trace theorem merely for finitely generated projective \(B\)-modules.
The unknown kernel projection \(p_a=1_{\{0\}}(a^*a)\) lies in \(N\), and its membership in \(N\) does not make it a class represented by an idempotent over \(B\).

If \(K_a=\operatorname{ann}_B(a)\) has a finite resolution by finitely generated projectives, [the proved Hilbert-completion calculation](../claims/Yin_C_A0001_v2.md#proof-of-the-homological-interface) transports their Euler characteristic to \(\tau(p_a)\).
For \(a\ne0\), the interval \(0\le\tau(p_a)<1\) then forces \(K_a=0\).
Thus a hypothetical nonzero \(K_a\) must fail that finite-resolution property.
This is a necessary structural pathology of a hypothetical counterexample; proving that pathology impossible for all torsion-free amenable groups is still the original unresolved work.
Neither complete finite-support density nor the integer trace of unrelated projectives establishes the required resolution.

### Why the existing finite free complex has no usable index

The obvious two-term complex \(B\xrightarrow{a}B\) already consists of finite free modules.
After Hilbert completion, its two homology spaces are
\[
H_1=\ker_{\ell^2}a,\qquad
H_0=\ell^2(G)/\overline{\operatorname{im}a}
\cong\ker_{\ell^2}a^*.
\]
Polar decomposition gives
\[
\dim_G H_1=\dim_G H_0=1-\operatorname{rk}_G a.
\]
Its Euler characteristic is consequently
\[
1-1=\dim_G H_0-\dim_G H_1=0.
\]
The integer index cancels the same unknown mass in two degrees.
It gives no arithmetic information about either mass separately.
A proof must isolate the desired kernel from this compensating cokernel, for example through a separately justified finite projective resolution of \(K_a\); using the free two-term complex itself does not do that.

## Smaller algebraic certificates and their exact missing hypotheses

The following conditional interfaces separate finite generation, finite homological dimension and projective trace.
They are structural tests on the remaining obstruction, not claims that the required hypotheses follow from amenability or torsion-freeness.

### A nonzero projective part would already suffice

Suppose a nonzero finitely generated projective right module \(P=EB^r\) embeds in \(K_a\).
Write the inclusion as a group-ring matrix \(D\), with \(D=DE\).
Its algebraic injectivity says that \(\binom{D}{I-E}\) has zero kernel over \(B\).
Complete finite-support kernel density then says that \(D\) is injective on \(H_E=E\ell^2(G)^r\).
Since \(aD=0\), its image closure lies in \(\ker a\).
The projection trace and polar decomposition give
\[
0<(\operatorname{Tr}\otimes\tau)(E)
=\dim_G\overline{D(H_E)}
\le\nu(a)<1,
\]
contrary to the BCM04 integer-trace conclusion.
Thus a nonzero principal annihilator cannot contain even a nonzero finitely generated projective submodule.
Independently constructing such a part would suffice; a full finite projective resolution is not the only possible certificate.
The assertion that every nonzero principal annihilator contains such a part is itself equivalent to the desired domain conclusion in this group class, since it is vacuous for a domain.
No proof of that universal extraction property has been obtained.

The elementary positivity identity
\[
K_a\cap a^*B=0
\]
also prevents using a generic argument about essential right ideals directly on \(K_a\).
Indeed \(x=a^*y\), \(ax=0\) gives \(aa^*y=0\), hence
\(\|a^*y\|_2^2=\langle aa^*y,y\rangle=0\) and \(x=0\).
For \(a\ne0\), \(a^*B\ne0\), so \(K_a\) fails the definition of an essential right ideal.
This calculation does not prove or disprove a Goldie hypothesis for the group ring.

### Finite cohomological dimension does not supply finite generation

For this paragraph, assume additionally \(d=\operatorname{cd}_{\mathbb C}G<\infty\), meaning that the trivial right \(B\)-module \(\mathbb C\) has projective dimension \(d\).
The standard diagonal-tensor argument gives right global dimension at most \(d\).
For attribution, the absolute-cohomological-dimension version is recorded in Jaikin-Zapirain--Linton, Proposition 2.2, in the [accepted manuscript](../audits/literature/JZL25/readme.md); the coefficient-specific argument needed here is given next.
Tensor a length-\(d\) projective resolution of \(\mathbb C\) over \(\mathbb C\) with any right \(B\)-module \(M\), using the diagonal right action.
Exactness is preserved because the tensor product is over a field.
The diagonal module \(B\otimes_{\mathbb C}M\) is free: the map
\[
g\otimes m\longmapsto g\otimes mg^{-1}
\]
intertwines its diagonal action with the action on the first factor alone.
Direct summands show that tensoring any projective term still gives a projective module.
The resolution ends at \(\mathbb C\otimes_{\mathbb C}M\cong M\), proving the global-dimension bound.
This construction does not preserve finite generation, because \(M\) can be infinite-dimensional over \(\mathbb C\).
Even an \(FP_\infty\) assumption on the trivial module cannot simply be passed to every principal quotient through this construction.

Put \(J_a=aB\) and \(C_a=B/aB\).
The exact sequences
\[
0\to K_a\to B\to J_a\to0,\qquad
0\to J_a\to B\to C_a\to0
\]
give, for \(i\ge1\),
\[
\operatorname{Ext}^i_B(K_a,M)
\cong\operatorname{Ext}^{i+2}_B(C_a,M).
\]
If \(d\le1\), \(J_a\) is projective, so \(B\to J_a\) splits and \(K_a\) is a finitely generated projective direct summand of \(B\).
The integer-trace argument therefore gives \(K_a=0\) with no additional finite-generation premise in this case.

If \(d\ge2\), put \(t=d-2\); dimension shifting gives \(\operatorname{pd}_B K_a\le t\).
It now suffices that \(K_a\) be of type \(FP_t\), meaning that some possibly infinite projective resolution has finitely generated terms \(P_0,\ldots,P_t\).
Here \(FP_0\) means finite generation, not existence of a length-zero projective resolution.
For \(t=0\), the module is already finitely generated projective.
For \(t\ge1\), let \(Z_t=\operatorname{im}(P_t\to P_{t-1})\).
It is finitely generated as the image of \(P_t\), and dimension shifting gives
\[
\operatorname{Ext}^1_B(Z_t,M)
\cong\operatorname{Ext}^{t+1}_B(K_a,M)=0.
\]
Hence \(Z_t\) is projective, and
\[
0\to Z_t\to P_{t-1}\to\cdots\to P_0\to K_a\to0
\]
is a finite resolution by finitely generated projectives.
The established trace formula then gives \(K_a=0\).
In particular, when \(d=2\), finite generation of the particular annihilator is sufficient.
Right coherence would provide the indicated finite-generation conditions by successively taking kernels of maps between finite free modules, but it is not obtained from the present group hypotheses.
The bounded-stage test identifies a concrete missing finiteness input and supplies no new group-class coverage.

### An infinite coherent resolution can preserve the fractional tail

Suppose a principal annihilator has an infinite resolution by finitely generated projectives.
Write its successive exact pieces as \(0\to Z_{j+1}\to P_j\to Z_j\to0\), with \(Z_0=K_a\).
Give \(Z_0\) its inclusion in \(B\), and each higher syzygy its inclusion in the preceding finite projective module.
Let \(z_j\) be the dimension of the corresponding Hilbert image closure and \(p_j=(\operatorname{Tr}\otimes\tau)(P_j)\in\mathbb Z\).
The same kernel-density and weak-exactness argument as in C_A0001_v2 gives
\[
z_{j+1}=p_j-z_j,\qquad
\nu(a)=\sum_{j=0}^{N-1}(-1)^jp_j+(-1)^Nz_N.
\]
If \(0<\alpha=\nu(a)<1\), nonnegativity and this recurrence imply
\[
z_{2j}\ge\alpha,\qquad z_{2j+1}\ge1-\alpha.
\]
Thus integer projective traces at every finite stage can coexist, at the level of these equations, with a persistent fractional tail.
It would suffice to prove that some syzygy dimensions tend to zero, or that the resolution terminates; neither follows from weak exactness.
This pinpoints why coherence alone does not finish this particular Euler-trace argument.
It does not assert the existence of a counterexample with these properties or exclude another use of coherence.

## Why the available rank comparison does not close the problem

[JL21, Theorem 1.1 and Theorem 1.3](../audits/literature/JL21/Yin_U001.md#amenable-rank-comparison) identify canonical amenable extensions of Sylvester rank and the corresponding tracial rank.
The group-ring example does not require a domain hypothesis.
However, the conclusion is a real-valued rank characterized by normalized finite-dimensional ranks and their infimum or limit; no integer-range conclusion is stated.
The finite integers being divided by Følner volume are not values of a fixed integer-valued invariant whose limit must remain integer.
Equality of algebraic and analytic rank constructions therefore identifies the quantity to be controlled without discretizing it.

[Bac26, arXiv v3](../audits/literature/Bac26/Yin_U001.md#domain-hypothesis) supplies conjugacy and rank-uniqueness mechanisms for the specified amenable algebras with no zero divisors.
Using that theorem to establish the absent domain property would assume the very premise still needed here.
This is a hypothesis mismatch in that proposed use, not an objection to the theorem.
No absence of other relevant literature or general impossibility of a rank argument is inferred from these selected checks.

## The remaining coefficient field is not the main analytic difficulty

The [already inspected Rowen--Saltman specialization argument](../audits/literature/JZ19/Yin_U001.md) supplies the established algebraically closed coefficient-field mechanism.
The following finite-equation presentation records its direct application while preserving the exact two supports.
It uses no amenability.

Suppose
\[
a=\sum_{s\in S}\alpha_s s,\qquad b=\sum_{t\in T}\beta_t t,
\qquad ab=0,
\]
where \(S,T\) are finite nonempty sets and all displayed coefficients are nonzero.
For \(h\in ST\), put
\[
f_h(X,Y)=\sum_{st=h}X_sY_t,\qquad
P(X,Y)=\prod_{s\in S}X_s\prod_{t\in T}Y_t.
\]
The finitely generated commutative algebra
\[
D=\mathbb Q[X_s,Y_t,Z]/(f_h\ (h\in ST),\,ZP-1)
\]
has a unital map to \(\mathbb C\) given by the original coefficients, and is therefore nonzero.
For a maximal ideal \(\mathfrak m\subset D\), the weak Nullstellensatz makes \(K=D/\mathfrak m\) a finite extension of \(\mathbb Q\).
The residue classes of all \(X_s,Y_t\) remain nonzero because \(ZP=1\).
Their values give \(0\ne a',b'\in KG\), with precisely the original supports and \(a'b'=0\).
Thus a scalar obstruction can already be chosen over a number field and inside the finitely generated subgroup carrying these supports.
This is a known specialization mechanism, not a new coefficient-change theorem or exclusion of the obstruction.

### The precise limit of restriction of scalars

Let \(d=[K:\mathbb Q]\), and use a rational basis of \(K\) to represent left multiplication by its coefficients.
This gives an injective ring map
\[
\rho:KG\longrightarrow M_d(\mathbb QG).
\]
It converts a scalar zero product into a matrix zero product, not a scalar zero product over \(\mathbb QG\).
In characteristic zero, separability gives a complex similarity between \(\rho(a')\) and \(\bigoplus_{\sigma:K\hookrightarrow\mathbb C}\sigma(a')\).
For amenable \(G\), every \(\sigma(a')\) has the same analytic nullity \(\delta\).
Indeed, for each finite support window \(F\), the equations for \(a'x=0\), \(x\in\mathbb C[F]\), form a finite matrix over \(K\).
Its rank is unchanged by a field embedding, since the vanishing of each minor is unchanged.
The finite-set kernel formula then gives equality of the limiting normalized dimensions.
Hence
\[
\nu_G(\rho(a'))=\sum_\sigma\nu_G(\sigma(a'))=d\delta.
\]
The inequalities \(0<\delta<1\) do not rule out \(d\delta\in\mathbb Z\).
Consequently restriction of scalars can lose the fractional-rank obstruction and does not justify replacing complex or algebraic coefficients by rational scalar coefficients.

## What a non-circular continuation must supply

The proposed trace route needs an independently established algebraic property of principal annihilators that places their individual Hilbert dimensions in the range of projective trace.
Finite projective resolutions are one sufficient certificate whose applicability remains unproved.
The alternative multiplicative route must rule out the finite collision equations \(f_h=0\) together with \(P\ne0\), using more of the actual group than the already used Følner approximation.

Every collision fiber \(\{(s,t):st=h\}\) would need at least two points in a zero-product witness.
A unique-product or suitably separating leading-term structure excludes such a witness immediately.
Torsion-freeness rules out nontrivial finite powers, but the present argument does not derive a separating structure on these finite multiplication tables from it.
A height homomorphism can reduce a zero product to its highest components, but a terminating reduction requires heights that actually separate the remaining supports; their existence is another unproved structural premise.
Reusing Følner density for the same hypothetical witness merely confirms its positive analytic kernel dimension and supplies no contradiction.

The outcome of this reassessment is an exact diagnosis of which existing interfaces do and do not constrain the obstruction.
It does not settle the full Task, the general amenable case, or a new class of groups.
The next successful step must establish one of the missing group-specific implications, rather than assign novelty or progress to the known equivalence.

## Review scope

The [original reassessment finding](../audits/reviews/Yin_R_A0002_v2.md#whole-reassessment-finding) independently checks every section except the later section on smaller algebraic certificates.
The [separate whole-section finding](../audits/reviews/Yin_R_A0040_v1.md#whole-section-finding) independently checks that added section, including all three subsections and their direct interfaces.
The [complete kernel-localization argument](../claims/Yin_C_A0001_v2.md#decision-reviewed-complete-localization) has its own selected proof assessment.
These findings support the calculations and limitations above without accepting any of the missing group-specific hypotheses or completing A0001.

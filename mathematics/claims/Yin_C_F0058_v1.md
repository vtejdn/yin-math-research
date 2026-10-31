---
author: Yin
---

# Original affiliated rationality for smooth unitary twists of free normal coordinates

## Current assessment
[Selected decision](#decision-isolated-original-whole-review-adoption-20261022)

## A triangular correlated normal pair retains the original all-bounded domains

<a id="statement"></a>
<a id="triangular-normal-unitary-core-transfer"></a>

Date: 2026-09-29.
Human record author: Yin.
Proof developed by another AI agent; separate complete mathematical review by another AI agent.
Consumer: [T_F0001's current contract](../tasks/Yin_T_F0001_v2.md).
This is an ordinary Claim proof, not a manuscript theorem designation or formal extraction.
The canonical Claim record owns its mathematical and review assessments.
The general correlated-tuple contract remains open.

Direct inputs are [C_F0025_v1](Yin_C_F0025_v1.md#decision-candidate-0002) for original represented derivatives and vacuum adjoints; [C_F0045_v1](Yin_C_F0045_v1.md#decision-candidate-0002) for the exact free-product right-module model and marginal lifting; [C_F0055_v1](Yin_C_F0055_v1.md#decision-candidate-0002) for unrestricted scalar normal contraction; [C_F0027_v1](Yin_C_F0027_v1.md#decision-candidate-0002) for original closure recovery; and [C_F0024_v1](Yin_C_F0024_v1.md#decision-candidate-0002) for the same-closure arbitrary-fraction rationality interface.
The accepted [Pis12-U001](../audits/literature/Pis12/Yin_U001.md#pis12-u001) finite-family little Grothendieck inequality is used exactly as in C_F0045, with squared constant k_C=4/pi.
C1 polynomial approximation reuses the exact accepted [VV16-U001 interface](../audits/literature/VV16/Yin_U001.md#vv16-u001); no new full audit of that source is claimed.
The free-product estimates below are proved here; no new external analytic theorem is invoked.

## 1. A precise sufficient class

Let B=W*(N) be a scalar normal coordinate with compact spectral law mu and the actual scalar polynomial-core dual/vacuum hypotheses of C_F0025.
Let V be a unitary free from B with faithful scalar law nu and the same scalar dual/vacuum hypotheses.
C_F0055 gives both scalar infinity-to-L2 contractions and original all-bounded domains for each factor.
Write e=e_V, xi_V=e*1 and choose a finite a_V such that ||e c||2<=a_V||c|| on C*(V).
No H-boundedness of either scalar dual is assumed.
Put M=B*W*(V).

Let G=g(N) be unitary.
Initially require g to be C1 on a neighborhood of the compact spectrum, with |g|=1 on that spectrum.
Define

`X=N`, `Y=G V`, `P=C<X,X*,Y,Y*>`.

The pair X,Y generates M because G is a bounded Borel function of X and V=G*Y.
This last equality is a von Neumann algebra statement: V is not asserted to belong to the unstarred rational algebra C<X,Y>.

After a smooth compact cutoff extension to a rectangle containing the spectrum, the accepted C1 approximation interface provides uniformly bounded scalar polynomial approximants to G, converging in both normal coarse derivative graphs.
The mean-value estimate controls both divided differences uniformly.
The theorem here keeps this C1 hypothesis; it does not identify a maximal scalar finite-energy domain with the original polynomial graph closure.

Use the original free-product normal derivations d=partial_N and q=partial_V on the free reference algebra, extended to G through those original graphs.
Their conjugates satisfy d^dagger N=conj(k_N), d^dagger N*=1 tensor 1.
Since q kills B, all bounded scalar functions in the indicated graph algebra are q-flat.
Put

`phi=dG`, `phi'=d^dagger G`,
`phi(z,w)=(g(z)-g(w))/(z-w)`,
`phi'(z,w)=(g(z)-g(w))/(conj(z)-conj(w))`.

They are bounded spatial tensors under the initial C1 hypothesis, and `||phi'||2=||phi||2`.
Inner tensor multiplication I_(a tensor b) sends v tensor w to va tensor bw.
On the enlarged graph algebra define

`alpha=d-I_(G* phi dot V) q`,
`alpha'=d^dagger-I_(G* phi' dot V) q`,
`theta=I_(G* tensor 1) q`.

These are outer derivations.
Checking the four generators gives

`alpha X=1 tensor 1`, `alpha X*=k_N`, `alpha Y=alpha Y*=0`,
`alpha' X=conj(k_N)`, `alpha' X*=1 tensor 1`,
`alpha' Y=alpha' Y*=0`,
`theta X=theta X*=0`, `theta Y=1 tensor 1`,
`theta Y*=-Y* tensor Y*`.

Thus alpha'=alpha^dagger on P, by equality on generators and the product rule.
All their P-values are bounded spatial tensors.
The construction is well-defined on evaluated elements because it uses the existing free reference derivations and their controlled original graphs.

## 2. The corrected vacuum exists without a diagonal evaluation

For a finite scalar tensor phi_n=sum a_j tensor b_j approximate phi in L2, with bounded polynomial factors.
The inner correction has adjoint vacuum

`q*(sum a_j* G tensor V* b_j*)`
` = sum a_j* G (xi_V V*-1)b_j*`.

Here the standard polynomial-tensor formula is legitimate also at G by its q-flat bounded graph approximants.
The two terms must be kept combined; separate diagonal sums need not have an intrinsic limit.
Put

`W=xi_V V*-1`.

The scalar vacuum identity gives tau(W)=0.
Freeness proves the exact isometry for any finite scalar tensor sum c_j tensor d_j:

`||sum c_j W d_j||2^2=||W||2^2 ||sum c_j tensor d_j||2^2`.

Consequently the displayed adjoint vacua converge in L2 as phi_n converges.
The adjoint input tensors also converge.
Closedness of the original q* therefore proves that the actual vacuum xi_alpha exists, with

`xi_alpha=xi_N-G lim_n sum a_j* W b_j*`,
`||xi_alpha||2<=||xi_N||2+||W||2 ||phi||2`.

The same argument applies to alpha', or conjugation gives its vacuum xi_alpha*.
The theta vacuum is q*(G tensor 1)=G xi_V.
This proves actual adjoint-domain statements, not just formal integration-by-parts symbols.

## 3. A right-end annihilation estimate

Use C_F0045's exact free-product Hilbert model.
Choose bounded centered orthonormal bases by Gram--Schmidt from the countable graph algebras C<N,N*,G,G*> and C<V,V*>.
Their algebraic spans equal those graph algebras' centered parts.
Thus every element of P has a finite reduced expansion in these bases, even though G need not be a polynomial in N,N*.
Let U_B be the vacuum and all orthonormal reduced words ending in the V factor.
Then

`H = direct_sum_(u in U_B) u L2(B)`,
`E_B(u* v)=delta_uv 1`.

Every finite reduced word sum has a unique expansion p=sum u b_u.
Let Q be the Hilbert projection onto reduced words ending in V with no final B letter:

`Q(sum u b_u)=sum_(u!=1) u tau(b_u)`.

The multiplication map range(Q) tensor_2 L2(B)->H is an isometry by the displayed module decomposition.
Write P_notV=I-Q.
Fix centered r in L2(W*(V)) and a finite scalar tensor s=sum a_j tensor b_j.
Define

`A_s p=sum_j P_notV(p b_j r)a_j`,
`Psi_s=sum_j b_j r a_j`.

Freeness and centeredness of r give the exact norm identity

`||Psi_s||2=||r||2||s||2`.

For fixed p in M the map b->Q(p b r), from L2(B) to range(Q), has Hilbert operator norm at most ||p||||r||2: b->b r is a scaled isometry, left multiplication by p is bounded, and Q is an orthogonal projection.
Therefore the right-module tensor isometry bounds the second term in

`A_s p=p Psi_s-sum_j Q(p b_j r)a_j`

by ||p||||r||2||s||2 as well.
The triangle inequality proves

`||A_s p||2<=2||p||||r||2||s||2`.                              (1)

The same argument gives a unique limit for every s in L2(mu^2), independent of its finite separated approximation.
It needs neither pointwise diagonal values nor a projective-tensor representation of s.

We also record the column estimate needed for the other half of the proof.
In the right V-module model H=direct_sum_(w in U_V)w L2(V), the column norm is

`||zeta||_(col V)=||sum_w c_w* c_w||infinity^(1/2)`.

It equals ||E_(W*(V))(zeta* zeta)||infinity^(1/2) whenever this expression is defined and bounded.
Here E_(W*(V)) denotes conditional expectation, not the dual contraction E_V.
Let Q_endB retain the scalar V coefficient for w!=1.
Then

`||Q_endB zeta||_(col V)^2=sum_(w!=1)|tau(c_w)|^2`
` <=||zeta||2^2<=||zeta||_(col V)^2`.

For P_notB=I-Q_endB this proves

`||P_notB zeta||_(col V)<=2||zeta||_(col V)`.

For p in M and b in L2(B), positivity and freeness yield

`E_(W*(V))((p b)*(p b))<=||p||^2||b||2^2 1`.

For b unbounded, first use bounded truncations and L1 continuity.
Hence

`||P_notB(p b)||_(col V)<=2||p||||b||2`.                         (2)

## 4. The triangular correction is a bounded contraction

Let U_V be the vacuum and the orthonormal reduced words ending in B.
Choose a bounded centered orthonormal basis (c) of L2(W*(V)) minus C1.
The right B-module basis except for its vacuum is precisely the words w c with w in U_V.
Thus every finite reduced polynomial sum has the form

`p=b_0+sum_(w,c) w c b_(w,c)`, `b_(w,c) in B`.

Set first on scalar Laurent polynomials, then on C*(V),

`R0 c=e(c V)-c`, `ell(c)=tau(R0 c)`,
`R1 c=R0 c-ell(c)1`.

Here e has its original all-bounded domain.
The scalar bound gives ||R1:C*(V)->L2(V)^0||<=a_V+1.
Both R0 and R1 annihilate 1.
The actual vacuum pairing gives

`ell(c)=tau(xi_V* c V)-tau(c)=tau(c r)`,
`r=V xi_V*-1 in L2(V)^0`.

Thus ell has the required L2 representer even though R0 need not be H-bounded.
For any finite scalar tensor phi=sum a_j tensor b_j, the usual inner-multiplier identity is

`C I_(G* phi dot V) q(p)`
` =sum_j [E_V(p b_j V)-p E_V(b_j V)] G* a_j`,

where C=id tensor tau and E_V is the exact free right lift of e.
As q kills B and e(V)=1, E_V(b_j V)=b_j.
Split each b_(w,c)b_j into its scalar and centered B parts.
A centered B part followed by V contributes only the last-letter derivative, which cancels the subtracted p b_j.
The remaining scalar part gives the exact formula

`C I_(G* phi dot V) q(p)=sum_(w,c) w (R0 c) S b_(w,c)`,          (3)

where S is the scalar integral operator with Hilbert-Schmidt kernel

`s(z,w)=conj(g(z)) phi(z,w)`.

To bound the centered contribution, fix p and apply the scalar map R1 to the right V-coefficients of P_notB(p b).
Call the resulting vector T_p b.
This operation is initially defined on the finite coefficient expansions from the chosen graph-algebra bases.
The accepted finite-family little Grothendieck inequality, together with (2), gives

`||T_p b||2^2<=k_C(a_V+1)^2||P_notB(p b)||_(col V)^2`
`             <=4 k_C(a_V+1)^2||p||^2||b||2^2`.

The full coefficient at the vacuum w=1 is retained in this application; its extra scalar part vanishes only after applying R1(1)=0.
No false column bound for a family with one scalar part deleted is used.
Thus T_p extends to a Hilbert operator of norm at most 2 sqrt(k_C)(a_V+1)||p|| from L2(B) to range(Q), because its outputs have a centered terminal V factor.

For s=sum a_j tensor b_j, the centered contribution is exactly sum_j (T_p b_j)a_j.
The right-module tensor isometry from Section 3 bounds its norm by 2 sqrt(k_C)(a_V+1)||p||||s||2.
The scalar ell contribution is precisely A_s p: expanding P_notV(p b_j r) erases the terminal centered V factor with scalar tau(c r).
Equation (1) bounds it by 2||r||2||phi||2||p||.
Therefore, with

`L_V=2 sqrt(k_C)(a_V+1)+2||V xi_V*-1||2`,

`||C I_(G* phi dot V) q(p)||2`
` <= L_V||phi||2||p||`.                                        (4)

The same proof gives convergence in the infinity-to-L2 norm for finite scalar tensor approximations to phi.
It consequently establishes (3)--(4) for the actual phi, with no arbitrary rearrangement of a conditionally convergent separated series.
The estimate initially applies to finite reduced expressions with bounded scalar factors in the controlled graph algebra; this includes every element of P.

## 5. Both normal contractions and the original domains

C_F0055 and C_F0045 provide finite free-reference constants a_N,a_Ndagger for C d and C d^dagger on bounded graph-algebra polynomials.
Equation (4) proves on the exact transformed core P

`||C alpha(p)||2<=(a_N+L_V||phi||2)||p||`,
`||C alpha'(p)||2<=(a_Ndagger+L_V||phi||2)||p||`.

The second estimate uses phi' and its equal L2 norm; it does not require boundedness of a phased map on all of the first contraction's domain.
Since alpha'=alpha^dagger and the actual vacuum exists by Section 2, the core adjoint formula is

`(C alpha|P)* p=p xi_alpha-C alpha'(p)`.

It supplies the separate infinity-to-L2 adjoint estimate on P.
C_F0027's bounded Kaplansky/weak-closed-graph argument now gives every element of M in both the original closure and actual adjoint domains of C alpha|P.

For theta, C theta(p)=(E_V p)G*.
The free reference right lift E_V has both original all-M domains and finite infinity-to-L2 bounds by C_F0045.
For each p in P, pG is bounded and lies in the actual Dom E_V*.
Genuine Hilbert adjoint pairings against every q in P therefore prove

`p in Dom(C theta|P)*`, `(C theta|P)*p=E_V*(pG)`.

This supplies both uniform core estimates for theta.
C_F0027 gives both all-M domains for the actual closure of C theta|P and its adjoint.
Equality with a larger free-reference closed operator is not assumed or needed.

Any original duals specified on P with the T_F0001 commutator hypotheses have these normalized canonical derivations: their values on every starred generator, and hence every word, agree.
Their only remaining normalization is right multiplication by their original vacuum value in L2.
Adding it preserves both infinity-to-L2 estimates and the original all-M conclusion.
The all-M restrictions retain exactly the original closures: they contain the original polynomial operators and are contained in their closures.
C_F0024 (recorded assessment 3) therefore supplies the full same-closure affiliated criterion.
Explicitly, put A=C<N,Y> and F=Div_(L0(M)) A.
For every u in L0(M) and every bounded fraction pair u=s^(-1)a=b t^(-1), with regular s,t in M, the literal regular commutators s D_i b-a D_i t have the legitimate dense all-M test domain and the C_F0024 original-closure realization.
They all have bounded finite-rank extensions if and only if u is in F.
The finite-rank condition is independent of the bounded fraction choices, at that theorem's exact scope.
The commutator itself can depend on the pair.
No replacement of A by C<N,V>, or assertion that V is rational in N,Y, occurs.

The bounded companion is also settled for this class: the original weak forms have bounded finite-rank representatives exactly for f in F intersect M, by the all-M converse and C_F0025 (recorded assessment 3)'s original weak direction.

## 6. Review boundaries

This is a sufficient-class proof, not the general correlated theorem.
Neither scalar dual is assumed H-bounded.
The C1 g hypothesis avoids any assertion that a maximal scalar finite-energy domain automatically equals the original polynomial closure.
The new steps requiring most scrutiny are the two right-module projection estimates, the finite-family little Grothendieck step before the terminal B tensor lift, and the exact correction identity (3).
Independent review is separately recorded; no novelty assessment is claimed.


## Assessment history


### Decision candidate-0001

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T23:44 |
| status | open |

Recorded authoring stage: proof draft.
Recorded review label: unreviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#triangular-normal-unitary-core-transfer) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |

Recorded mathematical summary: For a normal coordinate N and a freely independent unitary V with actual scalar vacuum adjoints, a C1 scalar unitary twist Y=g(N)V preserves both original all-bounded dual domains and the complete affiliated-fraction and bounded weak-form criteria for the original unstarred algebra C<N,Y>.
Neither scalar dual is assumed bounded on L2.

### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:59 |
| status | proved |
| reason | Adopt the exact actual original consolidated finding at its disclosed unknown initial-context relationship, preserving the statement, proof, dependencies and historical decisions. Dependency authorship alone is not a contribution to this target proof. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#triangular-normal-unitary-core-transfer) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original normal polynomial-core derivations, phase kernels, normalization uniqueness and the bounded weak implication. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Exact free-product right-module construction, marginal lifting and the checked complex little Grothendieck inequality. |
| dependency | [Exact material](Yin_C_F0055_v1.md#decision-candidate-0002) | Automatic scalar infinity-to-L2 bounds from actual vacua and original free-reference bounded-vector domains. |
| dependency | [Exact material](Yin_C_F0027_v1.md#decision-candidate-0002) | Recover both original closed dual and actual adjoint bounded-vector domains from the two core estimates. |
| dependency | [Exact material](Yin_C_F0024_v1.md#decision-candidate-0002) | Full unbounded affiliated criterion for arbitrary bounded left and right fractions, fraction independence, and actual commutators on the recovered original domains. |
| review | [Exact material](../audits/reviews/Yin_R_F0069_v1.md#verdict-and-exact-scope) | Actual original whole consolidated six-section finding, preserving exact C1 class, original accepted inputs and unknown initial-context arrangement; not a new review of its scalar dependency. |


### Decision isolated-original-whole-review-adoption-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:47 |
| status | proved |
| reason | Adopt the separately assigned isolated complete reconstruction of this fixed original mathematics and its actual necessary interfaces. The reviewer supplied no target development or repair and completed the initial finding before old target verdicts. Preserve all exact hypotheses, original graphs and closures, source-depth limits, historical decisions and original UNKNOWN relationship facts. The current finding creates no generalization beyond the stated theorem and no research Task/E resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#triangular-normal-unitary-core-transfer) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original normal polynomial-core derivations, phase kernels, normalization uniqueness and the bounded weak implication. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Exact free-product right-module construction, marginal lifting and the checked complex little Grothendieck inequality. |
| dependency | [Exact material](Yin_C_F0055_v1.md#decision-candidate-0002) | Automatic scalar infinity-to-L2 bounds from actual vacua and original free-reference bounded-vector domains. |
| dependency | [Exact material](Yin_C_F0027_v1.md#decision-candidate-0002) | Recover both original closed dual and actual adjoint bounded-vector domains from the two core estimates. |
| dependency | [Exact material](Yin_C_F0024_v1.md#decision-candidate-0002) | Full unbounded affiliated criterion for arbitrary bounded left and right fractions, fraction independence, and actual commutators on the recovered original domains. |
| review | [Isolated complete original mathematical finding](../audits/reviews/Yin_R_F0069_v1.md#current-triangular-correlated-class) | Complete actual fixed mathematical statement and original argument at the exact retained scope, necessary accepted interfaces, disclosed first-pass review-existence/scope descriptions and all source, closure and nontransfer limits; initial finding2026-10-22T21:41 precedes old target verdict comparison. |

## Historical assessments

<a id="decision-candidate-0002"></a>

### Historical assessment candidate-0002

This is the assessment recorded at the stated timestamp, not a newly performed review.
Historical inspection dates and review limits remain in the cited evidence.

| Field | Value |
| --- | --- |
| date | 2026-09-28T23:46 |
| status | proved |

Recorded review label: independently reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact material](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact material](#triangular-normal-unitary-core-transfer) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0025_v1.md#decision-candidate-0002) | Original normal polynomial-core derivations, phase kernels, normalization uniqueness and the bounded weak implication. |
| dependency | [Exact material](Yin_C_F0045_v1.md#decision-candidate-0002) | Exact free-product right-module construction, marginal lifting and the checked complex little Grothendieck inequality. |
| dependency | [Exact material](Yin_C_F0055_v1.md#decision-candidate-0002) | Automatic scalar infinity-to-L2 bounds from actual vacua and original free-reference bounded-vector domains. |
| dependency | [Exact material](Yin_C_F0027_v1.md#decision-candidate-0002) | Recover both original closed dual and actual adjoint bounded-vector domains from the two core estimates. |
| dependency | [Exact material](Yin_C_F0024_v1.md#decision-candidate-0002) | Full unbounded affiliated criterion for arbitrary bounded left and right fractions, fraction independence, and actual commutators on the recovered original domains. |
| review | [Exact material](../audits/reviews/Yin_R_F0069_v1.md#verdict-and-exact-scope) | Whole consolidated six-section proof: actual transformed vacua, free end-module tensor isometries, both contraction estimates without Hilbert-bounded scalar duals, original core adjoints and closed graphs, arbitrary original dual normalization, full C_F0024 bounded fractions and bounded weak companion relative to the unstarred algebra C<N,g(N)V>. Initial C1 unitary g scope only. |

Recorded mathematical summary: For a normal coordinate N and a freely independent unitary V with actual scalar vacuum adjoints, a C1 scalar unitary twist Y=g(N)V preserves both original all-bounded dual domains and the complete affiliated-fraction and bounded weak-form criteria for the original unstarred algebra C<N,Y>.
Neither scalar dual is assumed bounded on L2.

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).

## Recorded review scopes

Accompanying material (original association; no added proof premise): [Exact material](../audits/literature/VV16/Yin_U001.md).

Whole consolidated six-section proof: actual transformed vacua, free end-module tensor isometries, both contraction estimates without Hilbert-bounded scalar duals, original core adjoints and closed graphs, arbitrary original dual normalization, full C_F0024 bounded fractions and bounded weak companion relative to the unstarred algebra C<N,g(N)V>.
Initial C1 unitary g scope only.

Review: [Exact material](../audits/reviews/Yin_R_F0069_v1.md#verdict-and-exact-scope).

Material covered by that review: [Exact material](../audits/literature/VV16/Yin_U001.md); [Exact material](Yin_C_F0058_v1.md).

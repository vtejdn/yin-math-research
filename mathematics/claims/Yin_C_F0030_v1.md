---
author: Yin
---

# Full criterion with all-M dual domains and dense adjoint test modules

## Current assessment
[Selected decision](#decision-finding-owned-review)

## Affiliated Rationality with a Dense Left Module of Adjoint Tests

<a id="statement"></a>

<a id="yin_c_f0030"></a>
## Yin_C_F0030: Removing the All-Bounded-Vectors Adjoint-Domain Premise

Date: 2026-09-10.
Human author: Yin.
Proof development: another AI agent, following the user's request for an intermediate domain hypothesis in the main criterion.
The [selected assessment](#current-assessment) records the mathematical and review assessments; this complete draft is submitted for independent review.
This is an incremental extension of [Yin_C_F0024](Yin_C_F0024_v1.md#yin_c_f0024), whose recorded statement is preserved.
Only its explicitly identified elementary arguments are reused below, not its final theorem with an unmet premise.
No dependence on the separately drafted Yin_C_F0029 is needed.

### 1. Exact hypotheses and conclusions

Let `(M,τ)` be a finite von Neumann algebra with faithful normal probability trace, let `H=L²(M,τ)`, let `Ω=1`, and let `P=P_Ω`.
The inner product is linear in the second variable.
Write `λ(a)` and `ρ(a)` for left and right multiplication by a bounded element `a`, and suppress `λ` in products.
Let `X=(X₁,…,X_d)` be a finite bounded normal tuple generating `M`.

For each `i`, suppose a complex-linear operator `D_i` has domain exactly `MΩ`, identified with `M`, and satisfies

\[
D_i(X_jz)-X_jD_i z=\delta_{ij}\tau(z)\Omega
\qquad(z\in M).
\tag{1}
\]

Assume there is a complex-linear subspace `V_i⊂H` such that

\[
\overline{V_i}^{\,\|\cdot\|_2}=H,
\qquad M V_i\subseteq V_i,
\qquad V_i\subseteq\operatorname{Dom}D_i^*.
\tag{2}
\]

Thus `V_i` is a dense **left** `M`-submodule of the adjoint domain.
The spaces `V_i` may differ with `i` and need not consist of bounded vectors.
No right-module condition, inclusion of `Ω` in `V_i`, all-`M` adjoint-domain inclusion, estimate for `D_i^*|_M`, or vacuum normalization is assumed.
The operators `D_i` themselves still act on every bounded vector.
One may equally start with larger-domain operators and require (1)–(2) for their restrictions to `M`; the closures below are closures of those restrictions.

Set

\[
U=U(M),\qquad A=\mathbb C\langle X_1,\ldots,X_d\rangle,
\qquad F=\operatorname{Div}_U A.
\]

The generator adjoints are not adjoined to `A` in this definition.
Then all the conclusions of Yin_C_F0024 hold:

1. `Δ(X)=d`, and the accepted MSY23 free-field theorem identifies `F` with the embedded free skew field on the specified generators.
2. For any `u∈U`, write
   \[
   u=s^{-1}a=bt^{-1},\qquad s,a,b,t\in M,
   \qquad s,t\text{ regular},
   \tag{3}
   \]
   where regular means invertible in `U`.
   On the domain `M`, put
   \[
   T_i z=sD_i(bz)-aD_i(tz).
   \tag{4}
   \]
   The condition `u∈F` is equivalent to finite-dimensional range of every `T_i`, for some, equivalently every, bounded fraction pair (3).
   Each finite-rank defect has a unique bounded finite-rank extension to `H`, and its numerical rank is independent of the fraction pair.
3. In particular,
   \[
   F\cap M
   =\{f\in M:[D_i,f]|_M\text{ has finite rank for every }i\}.
   \tag{5}
   \]
   Writing `\widehat D_i=\overline{D_i}`, this is also equivalent to
   \[
   f\operatorname{Dom}\widehat D_i\subseteq\operatorname{Dom}\widehat D_i,
   \qquad
   [\widehat D_i,f]\text{ is the restriction of a bounded finite-rank operator}
   \tag{6}
   \]
   for every `i`.

The same fraction criterion applies to `F∩L²(M)` by restricting `u` in (3), without introducing an uncleared commutator with an unbounded affiliated element.

### 2. The analytic consequence of the smaller adjoint domain

The adjoint domain is dense by (2), so `D_i` is closable.
Its closure agrees with it at every input in `M`.
As a map from the Banach space `M` with operator norm to `H`, `D_i` has closed graph: if `z_n→z` in operator norm and `D_i z_n→w` in `H`, closedness of `\widehat D_i` gives `w=D_i z` because `z∈M`.
The closed graph theorem therefore gives

\[
\|D_i z\|_2\le c_i\|z\|\qquad(z\in M)
\tag{7}
\]

for some finite constant `c_i`.

If a uniformly operator-norm-bounded net `z_α∈M` converges in `L²` to `z∈M`, then

\[
D_i z_\alpha\rightharpoonup D_i z.
\tag{8}
\]

Indeed, pairing against `η∈V_i` gives `⟨η,D_i z_α⟩=⟨D_i^*η,z_α⟩→⟨D_i^*η,z⟩`.
The images are uniformly bounded by (7), so density of `V_i` extends the convergence to every test vector in `H`.
Fixed bounded left and right multipliers, and finite sums of these maps, preserve this bounded-set weak continuity.
No estimate for the adjoint on all of `M` is used.

For a defect (4) and `η∈V_i`, left-module invariance gives `s*η,a*η∈V_i⊂Dom D_i^*`.
Consequently, for every `z∈M`,

\[
\langle\eta,T_i z\rangle
=\left\langle
b^*D_i^*(s^*\eta)-t^*D_i^*(a^*\eta),z
\right\rangle.
\tag{9}
\]

Thus `V_i⊂Dom T_i^*`, and every defect is closable.
It also has an operator-norm-to-`L²` bound and the continuity (8), by its definition and (7).
Equation (9) is the sole extra step for which an adjoint module, rather than merely a dense adjoint domain, is required.

Here is the finite-rank extension fact used subsequently.
If a densely defined closable operator `T` has finite-dimensional range `E`, projection of the dense linear space `Dom T*` onto `E` is all of `E`.
For an orthonormal basis `e₁,…,e_r` of `E`, choose `η_k∈Dom T*` whose projection to `E` is `e_k`.
Then

\[
\langle e_k,Tz\rangle=\langle T^*\eta_k,z\rangle,
\]

which bounds every coordinate in the Hilbert norm.
This proves the unique bounded finite-rank extension of `T`.

### 3. Maximal Delta and the normal module identity

The proof of maximal Delta uses only (1) and the all-`M` input domain.
For completeness, take a bounded finite-rank cycle `Σ_i[S_i,X_i]=0` on `H`.
Finite-tracial fractions provide one bounded regular `r` with `(Ran S_i)r⊂M` for every `i`: clear common right denominators for a finite basis of the sum of the ranges.
Then `Q=ρ(r)` is injective and `Q S_i` has bounded-vector range.
For arbitrary `c,e∈M`, the operators `S_i'=ρ(c)Q S_iρ(e)` still form a cycle and have range in `M`.
The finite-dimensional ranges make the compositions `D_jS_i'` bounded finite-rank operators on all of `H`.
Applying `D_j` to the cycle, using (1), and only then taking the ordinary finite-rank trace gives

\[
0=\operatorname{Tr}(P S_j')
=\langle\rho(c)^*\Omega,Q S_j\rho(e)\Omega\rangle.
\]

The two bounded-vector test families are dense, so `Q S_j=0` and hence `S_j=0`.
The accepted finite-rank-cycle characterization of `Δ` and the MSY23 free-field equivalence therefore give conclusion 1.
The exact source interfaces and common-denominator construction are those recorded in Yin_C_F0024 Section 3; no final rationality conclusion of Yin_C_F0024 is consumed.

Put `R_i=ρ(X_i)` and, on `M`, define

\[
K=\sum_i(R_iD_i-D_iR_i),\qquad C=K+P.
\tag{10}
\]

By (7) this is a bounded map `M_∞→H₂`, and it has (8).
Jacobi's identity on the invariant inputs `M` and traciality give

\[
[K,X_j]=[R_j,P]=[X_j,P],\qquad [C,X_j]=0.
\tag{11}
\]

All multipliers subsequently acting on dual images are bounded on `H`, so no dual image is required to belong to `M`.
For a normal `x=X_j`, the Banach-space-valued entire function

\[
z\longmapsto\lambda(e^{zx^*})C\lambda(e^{-zx^*})
\]

equals

\[
\lambda(e^{zx^*-\bar z x})C
\lambda(e^{-zx^*+\bar z x}),
\]

because of (11).
The two outside multipliers are unitary and act isometrically on `H₂` and `M_∞` respectively.
Scalar Liouville applied to continuous linear functionals makes this entire function constant, so `[C,x*]=0`.
It follows that `C` intertwines the whole starred polynomial algebra.
Uniformly bounded Kaplansky approximants to any `a∈M`, with (8) on the input side and strong convergence of bounded multipliers on the output side, give

\[
C(az)=aCz\qquad(a,z\in M).
\tag{12}
\]

In particular `Cz=zCΩ`; neither `CΩ∈M` nor a bounded extension of `C` to all of `H` is required.
This normality argument uses no adjoint-domain inclusion beyond the closability already established in Section 2.

### 4. Cancellation and independence of fractions

Let `T:M→H` have the bounded-set weak continuity (8), and let `y,y'∈M` be regular.
Suppose `yTy'` has finite-dimensional range on `M`.
Injectivity of `y` puts `T(y'M)` in a fixed finite-dimensional subspace `E⊂H`.
Write `y'=v|y'|`, where `v` is unitary, and put

\[
e_n=1_{[1/n,\infty)}(|y'|),\quad p_n=ve_nv^*,\quad
w_n=|y'|^{-1}e_nv^*z\in M.
\]

For `z∈M`, one has `y'w_n=p_nz→z` in `L²` and `‖p_nz‖≤‖z‖`.
Thus `T(p_nz)⇀Tz` by (8).
Finite-dimensional subspaces are weakly closed, so `Tz∈E` for every `z`.
Hence `T` has finite rank.
When `T` is one of the defects, Section 2 also gives its bounded extension.

For two fraction pairs representing the same `u`, bounded common regular left and right multiples give regular `x,y,x',y'` with

\[
xs=ys_1,\quad xa=ya_1,\qquad tx'=t_1y',\quad bx'=b_1y'.
\]

Substitution on `M` gives the exact identity

\[
yT_i^{s_1,a_1,b_1,t_1}y'=xT_i^{s,a,b,t}x'.
\tag{13}
\]

The preceding cancellation proves equivalence of finite rank between fraction pairs.
Their bounded extensions have the same numerical rank, since injective left multiplication and dense-range right multiplication preserve the rank of a bounded finite-rank operator.
The same statements apply to the finite ranks before extension because `M` is dense in `H`.

Let `\mathcal R` be the resulting fraction-independent class.
The constants and generators belong to it by (1).
Common denominators make a sum's defects sums of the two defects.
For products `u_j=s_j⁻¹a_j=b_jt_j⁻¹`, take bounded `x,y,p,q`, with `x,q` regular, satisfying

\[
xa_1=ys_2,\qquad t_1p=b_2q.
\]

Fractions of `a₁s₂⁻¹` and `t₁⁻¹b₂` provide these multipliers; `y,p` need not be regular.
The product has fractions `(xs₁)⁻¹ya₂=b₁p(t₂q)⁻¹`, and its defect is

\[
x(s_1D_i b_1-a_1D_i t_1)p
+y(s_2D_i b_2-a_2D_i t_2)q.
\tag{14}
\]

The middle terms cancel on their identical bounded input `t₁pz=b₂qz`.
Finally, if `u=s⁻¹a=bt⁻¹` is a unit in `U`, then `a,b` are regular and `u⁻¹=a⁻¹s=tb⁻¹` has the negative of the original defect.
These identities make `\mathcal R` an inverse-closed unital algebra containing `A`, so `F⊂\mathcal R`.

### 5. Tensor descent and the closed-domain formulation

For `u∈\mathcal R`, use the bounded finite-rank extensions of (4).
The relation `sb=at`, the commuting left and right multipliers, and (12) give on `M`

\[
\begin{aligned}
\sum_i[R_i,T_i]z
&=sK(bz)-aK(tz)\\
&=sC(bz)-aC(tz)+(aPt-sPb)z\\
&=(aPt-sPb)z.
\end{aligned}
\tag{15}
\]

The `C` terms are `(sb−at)Cz=0`.
All remaining operators in (15) are bounded on `H`, so density extends the identity to `H`.

With the tracial conjugation `Jz=z*`, identify finite-rank operators with algebraic tensors by

\[
\Theta(g\otimes h)z=g\langle Jh,z\rangle.
\]

Then `[ρ(x),Θ(g⊗h)]=Θ(gx⊗h−g⊗xh)` for bounded `x`.
Writing each `T_i=Σ_αΘ(g_{iα}⊗h_{iα})`, equation (15) becomes

\[
a\otimes t-s\otimes b
=\sum_{i,\alpha}
\bigl(g_{i\alpha}X_i\otimes h_{i\alpha}
-g_{i\alpha}\otimes X_i h_{i\alpha}\bigr).
\tag{16}
\]

This is an identity in `H⊗_ℂH`, hence in `U⊗_ℂU`.
Pass to `U⊗_F U`; the right side vanishes.
The outer multiplications by `s⁻¹` and `t⁻¹` give

\[
u\otimes_F1=1\otimes_Fu.
\tag{17}
\]

The ring `F` is a division ring by Section 3.
If `u∉F`, the elements `1,u` are right-`F` linearly independent in `U`.
Extend them to a right-`F` basis and choose a right-`F` linear map `φ:U→F` with `φ(1)=0` and `φ(u)=1`.
Applying `φ⊗id` to (17) gives `1=0`, a contradiction.
Thus `\mathcal R⊂F`, proving the full affiliated criterion.

For bounded `f`, use `s=t=1`, `a=b=f` to obtain (5).
If the core commutator has bounded extension `T_i`, take graph approximants `z_n∈M` to `z∈Dom \widehat D_i`.
Then `fz_n→fz` in `H`, and

\[
D_i(fz_n)=fD_i z_n+T_i z_n
\longrightarrow f\widehat D_i z+T_i z.
\]

Closedness proves (6) and its operator identity.
Conversely, restricting (6) to `M` proves finite rank in (5).
The specified closure is essential: the proof concerns `\overline{D_i|_M}`, whose graph core is `M`, and not an arbitrary larger closed extension.

### 6. Checkable adjoint test spaces and scope

The original Yin_C_F0024 assumption implies (2) by taking `V_i=M`.
The following are alternative sufficient ways to check (2).

- If `r_i∈M` is bounded regular and `M r_i⊂Dom D_i*`, take `V_i=M r_i`.
  This is a left module and is dense because the right multiplier `ρ(r_i)` has dense range and `M` is dense in `H`.
- If projections `e_{i,n}↑1` satisfy `M e_{i,n}⊂Dom D_i*` for every `n`, take `V_i=\bigcup_n M e_{i,n}`.
  The union is increasing and left invariant, and `a e_{i,n}→a` in `L²` for every `a∈M`.

These forms localize the adjoint tests while leaving the dual inputs in all of `M`.
The proof requires neither `D_i*Ω` nor a uniform estimate for the adjoint on bounded inputs approaching `Ω`.
No assertion is made that either certificate follows automatically from a dual relation or from vacuum membership in the adjoint domain.

This result removes the explicit all-`M` adjoint-domain premise from the sufficient proof.
No normal-tuple dual example separating (1)–(2) from Yin_C_F0024's original hypotheses has been established here, and logical strictness within that class is not claimed.
In fact, there is a useful restriction on where such a separation could occur.
If the same tuple already admits one closable all-`M` dual `D_i^{(0)}` with the all-`M` adjoint property, then any other closable all-`M` dual `D_i` has difference `B_i=D_i−D_i^{(0)}` satisfying `[B_i,X_j]=0`.
The estimates and bounded-set weak continuity hold for this difference, so the same Banach Liouville and Kaplansky argument gives `B_i z=zη_i`, where `η_i=B_iΩ∈H`.
Right multiplication by `η_i` on `M` has every bounded vector in its adjoint domain, with adjoint value `zη_i*` there.
Adding this to the known adjoint of `D_i^{(0)}` shows that `D_i` also has the all-`M` adjoint property.
Thus known Yin_C_F0024 models cannot provide such a strict-separation example merely by changing their all-`M` duals.

The theorem does not shrink the domains of `D_i` to the polynomial algebra and does not settle the general bare-core route Yin_S_F0011.
It supplies no equality between `F∩M` and a rational or division closure recomputed inside `M`.
All earlier bounded-realization and canonical-fraction obstructions keep their original scope.

### 7. Dependencies and review boundary

The retained inputs are finite-tracial affiliated fractions and their common denominators, the finite-rank-cycle characterization of maximal Delta, the MSY23 free-field equivalence, the finite-tensor identification, standard closed-operator adjoints and closed graph, Kaplansky density, and scalar Liouville.
Their source scope is recorded in Yin_C_F0024 and its cited source audits.
The arguments consuming those inputs are supplied above with the smaller adjoint test spaces visible in (9).
In particular, no estimate for `D_i*|_M` is imported from Yin_C_F0024 Section 2.
The essential replacement is the dense left-module condition ensuring closability of every cleared defect.

Candidate descent using only closability of `D_i` and `H⊗L¹` tensors is separate exploratory work and is not used in this theorem.
No numerical check, proof-assistant verification, external human review or historical novelty claim is asserted.
The author has previously contributed to Yin_C_F0024's preliminary analysis and its review, and authored Yin_C_F0027's bounded inverse module; these antecedents are disclosed for the independent reviewer of this new complete statement.


## Argument: yin_c_f0030-p2


<a id="yin_c_f0030-p2"></a>
## Yin_C_F0030-P2: The All-M Dual-Domain Specialization

The authoritative statement remains [Yin_C_F0030, Section 1](#yin_c_f0030).
Its direct project dependency for this version is Yin_C_F0029-P2, not Yin_C_F0024-P1 or the original Yin_C_F0030 proof.
Set \(E=M\) and retain the dense left \(M\)-modules \(V_i\) in the adjoint domains.
Every assumption of Yin_C_F0029-P2 holds verbatim; the vacuum relation \(Pz=\tau(z)\Omega\) on \(M\) matches the stated convention.
The operators being closed are exactly the same restrictions to \(M\).
Thus all three numbered conclusions, numerical-rank independence and the full-domain bounded-element formulation follow.
Restricting the universally quantified \(u\in U\) to \(U\cap L^2(M)\) gives the stated \(L^2\) specialization with cleared defects.
There is no new assertion about an uncleared commutator of an unbounded affiliated element.

Yin_C_F0030-P1 Section 6 retains its separate elementary adjoint-domain certificates and non-separation discussion as reviewed auxiliary arguments.
They are not prerequisites of this specialization or newly strengthened conclusions.


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
| argument | [Exact material](#yin_c_f0030-p2) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact material](#6-checkable-adjoint-test-spaces-and-scope) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact material](Yin_C_F0029_v1.md#decision-candidate-0002) | Selected P2 specialization: E=M with dense left-module adjoint tests. |
| review | [Exact material](../audits/reviews/Yin_R_F0012_v1.md) | Original selected finding; its actual scope and limits remain in the cited review. |
| review | [Exact material](../audits/reviews/Yin_R_F0019_v1.md) | Original selected finding; its actual scope and limits remain in the cited review. |

Original accompanying material and inspection boundaries are listed under [recorded review scopes](#recorded-review-scopes).


### Decision finding-owned-review

| Field | Value |
| --- | --- |
| date | 2026-10-21T00:45 |
| status | proved |
| reason | Select the actual retained finding scopes and their known mathematical-development relationships, preserving status, authorized role, exact statement/proof/dependency selections and all historical decisions. No new mathematical review is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Exact original statement and hypotheses retained in this material. |
| argument | [Exact argument](#yin_c_f0030-p2) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| argument | [Exact argument](#6-checkable-adjoint-test-spaces-and-scope) | Original explicitly selected argument locator; no broader argument or hypothesis is inferred. |
| dependency | [Exact dependency](Yin_C_F0029_v1.md#decision-candidate-0002) | Selected P2 specialization: E=M with dense left-module adjoint tests. |
| review | [Retained finding](../audits/reviews/Yin_R_F0012_v1.md#criterion-assembly-finding) | Actual original complete or auxiliary scope stated by that finding; unchanged versions and original source-depth/nonconclusion boundaries. |
| review | [Retained finding](../audits/reviews/Yin_R_F0019_v1.md#dense-adjoint-module-finding) | Actual original complete or auxiliary scope stated by that finding; unchanged versions and original source-depth/nonconclusion boundaries. |

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

Review: [Exact material](../audits/reviews/Yin_R_F0012_v1.md); [Exact material](../audits/reviews/Yin_R_F0019_v1.md).

Material covered by that review: [Exact material](Yin_C_F0024_v1.md#yin_c_f0024-p2), [Exact material](Yin_C_F0029_v1.md#yin_c_f0029-p2), [Exact material](#yin_c_f0030-p2) (together retain the original whole-source scope); [Exact material](Yin_C_F0030_v1.md).

---
author: Yin
---

# Assembling relative normal models with large slice-to-vacuum ratios

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Fix a positive integer \(m\).
A relative model here consists of a bounded normal operator \(Z_0\) of diffuse law and \(m\) bounded selfadjoint coefficients \(H_1,\ldots,H_m\), generating a finite von Neumann algebra \(R\) with faithful normal probability trace \(\tau_R\).
On their represented starred polynomial algebra \(P_R\) suppose there is an outer derivation \(D:P_R\to L^2(R)\otimes_2 L^2(R)\), with \(DZ_0=1\otimes1,\ DH_l=0\) and actual vacuum \(\zeta=D^*(1\otimes1)\).
Only the distinguished derivation is required.
Define its single-input right slice cost
\[
       a_R=\sup_{p\in P_R,\ \|p\|\le1}\|(\mathrm{id}\otimes\tau_R)Dp\|_2 .
\]
If \(a_R/\|\zeta\|_2\) is unbounded over these models for this fixed \(m\), including if it is infinite on one model, there exists **one** bounded normal tuple \((Z,Y_1,\ldots,Y_m)\), with every \(Y_l\) selfadjoint, which satisfies [full actual starred ACSY](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) and has infinite single-input cost at \(Z\).
This tuple has no bare full-domain dual system and hence no strong system.
Unboundedness of the ratios may be tested with all input generators contractions.

Consequently the universal implication \(\mathsf A\Rightarrow\mathsf S\) on finite normal tuples is equivalent to the existence, for every \(m\ge1\), of a finite constant \(C_m\) such that
\[
                            a_R\le C_m\|\zeta\|_2                         \tag{1}
\]
in all the relative models above.
No witness of unbounded ratios, or proof that they are bounded, is asserted.

## Argument

### Fixing the witnesses before the masses

The coordinating agent proposed using ordinary scalar Gaussian smoothing in the omitted coordinates after constructing the distinguished derivative on a direct sum.
Rescaling a nonzero \(Z_0\) by a positive scalar \(s\) leaves the represented algebra unchanged and rescales the normalized derivative, hence both \(a_R\) and \(\|\zeta\|_2\), by \(s^{-1}\).
Separate nonzero real rescalings of the selfadjoint coefficients do not affect the normalized derivative or its cost.
Thus take all generators contractions.
Testing \(D\) on \(Z_0\) gives \(\|\zeta\|_2\ge1\).
On a diffuse normal generator, differentiating its commutation with its adjoint forces \(DZ_0^*=(\bar z-\bar w)/(z-w)\) off the null diagonal, because the outer difference \(L_{Z_0}-R_{Z_0}\) is injective on the coarse correspondence by diffuseness.
In particular this prescribed marginal symbol has coarse norm one. [Normal starred symbol](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability)

For every \(n\ge1\) take a relative model \((R_n,\tau_n,Z_n,H_{n,1},\ldots,H_{n,m},D_n,\zeta_n)\) and a fixed formal starred polynomial \(p_n\) in its generators whose represented norm is at most one and whose right slice norm \(b_n\) satisfies \(b_n>4^n\|\zeta_n\|_2\).
Write \(r_n(Z_n,H_n)=(\mathrm{id}\otimes\tau_n)D_np_n(Z_n,H_n)\).
For later use allow replacing the coefficients \(H_{n,l}\) by selfadjoint \(K_l\) in a larger finite tracial algebra containing \(R_n\) with the same probability trace.
Evaluate the same polynomial and the same formal tensor product rule there, differentiating \(Z_n,Z_n^*\) to the unit tensor and the forced phase respectively, and assigning zero to \(K_l\).
If \(\max_l\|K_l-H_{n,l}\|\le\epsilon_n\) for some sufficiently small \(\epsilon_n>0\) depending only on the fixed witness, then the evaluated polynomial has norm at most two and the right trace of the evaluated formal derivative has Hilbert norm at least \(b_n/2\).
Indeed for \(\epsilon_n\le1\) every letter has norm at most two.
The polynomial difference is bounded in operator norm by telescoping the letters, and the same telescoping bounds the coarse Hilbert difference in each differentiated word with the unit tensor or the fixed norm-one phase at its marked occurrence.
The latter tensor is identified isometrically in the enlarged coarse space by the trace restriction.
All constants depend only on the finitely many coefficients and word lengths, and right trace is a contraction in the normalized Hilbert norms.
This assertion is a comparison of specified formal expressions and does not presume that the perturbed model already admits the derivation.

Choose positive masses \(t_n\) after fixing these tests, so small that
\[
 t_n\le 2^{-4n-4},\qquad 2\sqrt{t_n}\le\epsilon_n,\qquad
 \alpha_n=2^n t_n^{3/2}\|\zeta_n\|_2\le 2^{-n-4}.
                                                                    \tag{2}
\]
Put \(t_0=1-\sum_{n\ge1}t_n>0\).
In this remaining block take \(Z_0'\) to have the standard semicircular law scaled to norm one, with its scalar actual normalized derivative, and take all coefficients zero.
Use that block only to fill the probability trace.
In \(R=\prod_{n\ge0}R_n\) with trace \(\tau=\sum t_n\tau_n\), let \(Z\) have entries \(X_n=2^{-n}+\alpha_n Z_n\) for \(n\ge1\) and \(X_0=2+Z_0'/8\).
Also let \(H_l=(H_{n,l})_{n\ge0}\).
The spectral disks for the \(X_n,\ n\ge1\), are disjoint with pairwise distance at least a fixed positive multiple of \(2^{-\min(n,k)}\) for \(n\ne k\); the remaining disk is separated from all of them.
The block units \(e_n\) are spectral projections of \(Z\) alone.
Consequently \(W^*(Z,H_1,\ldots,H_m)=R\), by generation in each finite corner and strong convergence of finite truncations.

### The distinguished derivative before smoothing

The diagonal coarse block \((n,n)\) uses the outer derivation \(\alpha_n^{-1}D_n\) applied to the entry of the input, for \(n\ge1\).
The entry of a fixed polynomial in \(Z,H_l\) is a polynomial in the indicated \(Z_n,H_{n,l}\); in the auxiliary block use the scalar normalized derivative for \(X_0\).
The diagonal prescriptions are \(e_n\otimes e_n\) at \(Z\), the corresponding phase at \(Z^*\), and zero at all \(H_l\).
Their squared global coarse norms on the generators sum finitely since the inherited squared norm in block \((n,n)\) has the weight \(t_n^2\).
Uniformly bounded outer multipliers then give coarse summability on every polynomial.
The diagonal vacuum has block entry \(t_n\zeta_n/\alpha_n\), with the analogous finite auxiliary entry.
Indeed the Hilbert pairing in the base carries weight \(t_n\) and the product trace carries \(t_n^2\).
Its squared norm outside the auxiliary block is \(\sum_{n\ge1}t_n^3\|\zeta_n\|_2^2/\alpha_n^2=\sum_{n\ge1}4^{-n}\).

On the mixed coarse summand \((n,k),\ n\ne k\), take \(L_{nk}(z,w)=1/(z-w)\) evaluated in the two marginal legs of \(X_n,X_k\).
The sum \(L\) of these mixed tensors is in the global coarse Hilbert space.
In fact \(\|L_{nk}\|_{2,\mathrm{global}}^2\le t_nt_k/\operatorname{dist}(\sigma(X_n),\sigma(X_k))^2\), whose sum is finite by (2) and the disk separation, including the auxiliary block.
Define the mixed derivative of \(x\) to be \(x\cdot L-L\cdot x\).
It respects represented relations and the outer Leibniz rule.
It supplies all missing unit entries at \(Z\) and the missing marginal phases at \(Z^*\).
At \(H_l\) this mixed derivative has norm at most \(2\|H_l\|\|L\|_2\).
The vacuum pairing of its value at \(x\) has absolute value at most \(2\|L\|_2\|x\|_2\), by moving the two outer multipliers to \(1\otimes1\).
These are the block trace and gap estimates of the [one-generator assembly](Yin_C_F0210_v1.md#the-actual-derivation-on-countably-many-corners), with a nonzero mixed derivative now allowed on a coefficient.
Together the prescriptions define \(D_0\) on the represented starred polynomial core of \(R\), with actual Hilbert vacuum \(\zeta_0\).

### Restoring all normalized coordinate derivatives

Take standard freely independent semicirculars \(S_1,\ldots,S_m\) jointly free from \(R\), in the finite tracial free product \(\widehat R\), and put
\[
                     Y_l=H_l+S_l,\qquad M=W^*(Z,Y_1,\ldots,Y_m).
\]
On the algebraic free product of the base core and the noise polynomial algebras extend \(D_0\) by zero on the noises.
This respects represented relations by the faithful free reduced-word representation.
Its vacuum stays \(\zeta_0\): in a centered alternating word with a noise block, each differentiated base block leaves a centered free segment on a trace leg.
This cancellation holds for Hilbert tensor values by approximation by finite tensors in the base; the word itself has zero conditional expectation onto the base.
Pure noise words have zero pairing with the centered \(\zeta_0\).

For each \(l\) add the derivation sending \(S_l\) to the base tensor \(\beta_l=-D_0H_l\), and killing \(R\) and every other noise.
This is the [arbitrary tensor insertion at a free selfadjoint coordinate](Yin_C_F0268_v1.md#inserting-an-arbitrary-base-tensor-at-the-selfadjoint-coordinate) over the base enlarged by the other noises.
Its actual vacuum is \(J_{S_l}(\beta_l^\star)\), where \((a\otimes b)^\star=a^*\otimes b^*\) and \(J_{S_l}(a\otimes b)=aS_lb\).
On \(L^2(R)\otimes_2 L^2(R)\) these maps \(J_{S_l}\) are isometries with mutually orthogonal ranges perpendicular to the original base Hilbert space, by the centered reduced-word inner product.
It follows that the total vacuum exists, of squared norm \(\|\zeta_0\|_2^2+\sum_l\|D_0H_l\|_2^2\).
The corrected derivation sends \(Z\) to \(1\otimes1\), \(Z^*\) to its global marginal phase and \(Y_l=Y_l^*\) to zero.
On the target starred algebra its values therefore lie in \(L^2(M)\otimes_2L^2(M)\), and projecting the ambient vacuum onto \(L^2(M)\) supplies the actual target vacuum.
For coordinate \(Y_l\), ordinary differentiation at \(S_l\) killing the full base and other noises has ambient vacuum \(S_l\).
It takes \(Y_j\) to \(\delta_{lj}1\otimes1\) and kills \(Z,Z^*\); restricting to the generated core and projecting its vacuum gives the other actual coordinates.
No individual \(H_l\) need be in \(M\).

### Retaining the bad polynomials in the generated algebra

The coordinate \(Z\) puts each \(e_n\) and the element \((e_nZ-2^{-n}e_n)/\alpha_n=Z_n\) in the target corner \(e_nMe_n\), using the natural ambient identification of \(R_n\) with \(e_nRe_n\).
Give the ambient and target corners the probability trace \(\tau/t_n\), whose restriction to \(R_n\) is exactly \(\tau_n\).
The [normalized free compression formula](../audits/literature/NS06/Yin_U004.md#ns06-u004) gives \(\|e_nS_l e_n\|=2\sqrt{t_n}\) by the semicircular law in that trace and its faithfulness.
Hence the target inputs \(K_l=e_nY_l e_n\) differ in ambient operator norm from \(H_{n,l}\) by at most \(\epsilon_n\).
This argument uses the law of the compressed noise alone.

Apply the [relative spectral-corner theorem](Yin_C_F0301_v1.md#statement) to the actual target tuple.
Its relative derivation \(\delta_{e_n}\) differentiates \(e_n Z\) to \(e_n\otimes e_n\), and kills \(K_l\) since these are compressions of omitted elements.
Thus \(\alpha_n\delta_{e_n}\) sends \(Z_n\) to \(e_n\otimes e_n\) and \(Z_n^*\) to precisely the former marginal phase; the affine scaling has positive real slope and real center.
The polynomial \(p_n(Z_n,K_1,\ldots,K_m)\) lies in the relative core of the target.
Evaluating its derivative agrees exactly with the formal expression used in the perturbation comparison above.
On tensors coming from \(R_n\), contraction by the normalized ambient corner trace agrees with contraction by \(\tau_n\); on tensors coming from the generated corner it agrees with the target corner contraction.
The comparison therefore shows that this target polynomial has norm at most two and relative single-input slice norm at least \(b_n/(2\alpha_n)\).
In particular the normalized relative cost \(a_{e_n}\) of the target corner satisfies \(a_{e_n}\ge b_n/(4\alpha_n)\).

Suppose the original distinguished target slice had finite single-input cost \(a\).
The [global cutoff estimate](Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) bounds every fixed-radius cutoff by \(3a\), so both \(k(F_n)\) and \(B_{e_n}\) of the spectral-corner theorem are at most \(3a\) on the disk of \(X_n\).
That theorem gives \(t_n^{3/2}a_{e_n}\le6a\).
Yet by (2) and the fixed witness lower bounds,
\[
              t_n^{3/2}a_{e_n}\ \ge\
                  \frac{b_n}{4\cdot2^n\|\zeta_n\|_2}>2^{n-2}.
\]
This contradiction proves infinite original slice cost.
The [normal bare-dual implication](Yin_C_F0070_v1.md#statement) excludes every bare system on this same tuple.

### Equivalence with the universal normal implication

The construction proves necessity of (1) for the universal implication by contraposition.
Conversely, in any actual finite normal tuple a distinguished coordinate has a relative model with the real and imaginary parts of the other coordinates as bounded selfadjoint coefficients, since the actual normal derivation kills those coordinates and their adjoints.
For a single coordinate put one coefficient equal to zero.
Bound (1) gives finite single-input cost in every coordinate; applying it also to the actual adjoint tuple gives the second orientation.
The [normal two-orientation comparison](Yin_C_F0075_v1.md#statement) and [two-slice domain theorem](Yin_C_F0072_v1.md#statement) then give the canonical strong domains and dual system.
This establishes the equivalence while leaving the uniform relative estimate open.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:08 |
| status | open |
| reason | Fix the direct-sum and free-noise construction and its universal relative estimate for independent inspection. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | For each fixed number of selfadjoint coefficients, unbounded relative slice-to-vacuum ratios yield one actual normal separator, and universal strong duality is equivalent to the family of linear estimates. |
| argument | [Argument](#argument) | Preselected polynomial witnesses, diagonal and mixed derivative blocks, noise correction, normalized free compression, corner bounds and both orientations. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Starred derivative from normality and diffuseness and vanishing at omitted normal coordinates. |
| dependency | [One-generator block calculation](Yin_C_F0210_v1.md#the-actual-derivation-on-countably-many-corners) | Inherited tensor and Hilbert weights, separated cross-block commutators and their vacuum bound. |
| dependency | [Free noise tensor insertion](Yin_C_F0268_v1.md#inserting-an-arbitrary-base-tensor-at-the-selfadjoint-coordinate) | Actual vacuum at an arbitrary base Hilbert tensor assigned to a free selfadjoint coordinate. |
| dependency | [Normalized free compression](../audits/literature/NS06/Yin_U004.md#ns06-u004) | Standard semicircular compression has variance equal to the projection trace under the normalized corner trace. |
| dependency | [Relative spectral corner](Yin_C_F0301_v1.md#statement) | Relative coefficient algebra, normalized derivative, and the lower transfer inequality between the corner and global cutoff costs. |
| dependency | [Global cutoffs](Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) | Uniform threefold cutoff norm bound when the original single-input cost is finite. |
| dependency | [Normal bare-dual implication](Yin_C_F0070_v1.md#statement) | A bare system forces finite original single-input cost in every coordinate. |
| dependency | [Normal comparison](Yin_C_F0075_v1.md#statement) | Adjoint stability and the comparison between the two orientations and strong duals. |
| dependency | [Two-slice domain theorem](Yin_C_F0072_v1.md#statement) | Finite slice bounds in both orientations give both canonical domains and the original commutators. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:13 |
| status | proved |
| reason | Independent review verified the direct sum derivation, free noise corrections, normalized corner tests and the equivalence with a linear estimate for each fixed coefficient count. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | For each fixed number of selfadjoint coefficients, unbounded relative slice-to-vacuum ratios yield one actual normal separator, and universal strong duality is equivalent to the family of linear estimates. |
| argument | [Argument](#argument) | Preselected polynomial witnesses, diagonal and mixed derivative blocks, noise correction, normalized free compression, corner bounds and both orientations. |
| dependency | [Normal phase](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Starred derivative from normality and diffuseness and vanishing at omitted normal coordinates. |
| dependency | [One-generator block calculation](Yin_C_F0210_v1.md#the-actual-derivation-on-countably-many-corners) | Inherited tensor and Hilbert weights, separated cross-block commutators and their vacuum bound. |
| dependency | [Free noise tensor insertion](Yin_C_F0268_v1.md#inserting-an-arbitrary-base-tensor-at-the-selfadjoint-coordinate) | Actual vacuum at an arbitrary base Hilbert tensor assigned to a free selfadjoint coordinate. |
| dependency | [Normalized free compression](../audits/literature/NS06/Yin_U004.md#ns06-u004) | Standard semicircular compression has variance equal to the projection trace under the normalized corner trace. |
| dependency | [Relative spectral corner](Yin_C_F0301_v1.md#statement) | Relative coefficient algebra, normalized derivative, and the lower transfer inequality between the corner and global cutoff costs. |
| dependency | [Global cutoffs](Yin_C_F0282_v1.md#canonical-cutoffs-on-the-original-algebra) | Uniform threefold cutoff norm bound when the original single-input cost is finite. |
| dependency | [Normal bare-dual implication](Yin_C_F0070_v1.md#statement) | A bare system forces finite original single-input cost in every coordinate. |
| dependency | [Normal comparison](Yin_C_F0075_v1.md#statement) | Adjoint stability and the comparison between the two orientations and strong duals. |
| dependency | [Two-slice domain theorem](Yin_C_F0072_v1.md#statement) | Finite slice bounds in both orientations give both canonical domains and the original commutators. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0314_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

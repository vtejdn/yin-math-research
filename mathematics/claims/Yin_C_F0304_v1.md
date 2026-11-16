---
author: Yin
---

# Amplifying spectral corner costs by a small change of one normal coordinate

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(X\) be a finite bounded normal generating tuple with [actual starred conjugate variables](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) in a finite von Neumann algebra with faithful probability trace.
Fix an oriented coordinate \(Z\) (apply the entire assertion to the adjoint tuple for the opposite orientation), its law \(\mu\), vacuum \(\xi\), and the normalized [relative Borel corners](Yin_C_F0301_v1.md#statement).
For each Borel set \(F\) of mass \(t>0\) write \(a_F\) for the single-input norm of its relative right slice and \(v_F=t^{3/2}\|\xi^F\|_{2,\tau_F}\) for the weighted norm of its actual relative vacuum.
Set \(a=a_{\sigma(Z)}\).

Suppose \(a<\infty\) and
\[
                  \sup_{\mu(F)>0}\frac{a_F}{\|\xi^F\|_{2,\tau_F}}=\infty .
                                                                    \tag{1}
\]
For every \(\varepsilon>0\) there is a bounded injective Borel relabelling \(\phi\) of the marginal spectrum, with Borel inverse on its image, such that replacing only \(Z\) by \(\phi(Z)\) has the following effects.

* The new tuple still satisfies \(\mathsf A\) in the same tracial algebra, and its right slice at \(\phi(Z)\) is unbounded on polynomial contractions.
  Thus the new tuple has no bare full-domain dual system in that orientation and fails \(\mathsf S\).
* The map is the identity except on a set of \(\mu\)-mass less than \(\varepsilon\), and is a positive dilation followed by a translation on each of countably many disjoint Borel pieces of that set.
  The change of the generator and that of its actual conjugate vector both have \(L^2(\tau)\) norm less than \(\varepsilon\).
  The other actual conjugate vectors are unchanged.

Consequently the universal normal implication is equivalent to the following stronger-looking estimate: for every actual tuple and each orientation of each coordinate there is a finite constant depending on that tuple and the oriented coordinate such that
\[
                          a_F\le C_X\|\xi^F\|_{2,\tau_F}
                \qquad\text{on every positive-mass Borel set }F.         \tag{2}
\]
The estimate holds, in particular, at the planar base of every actual [Möbius coupling of a free Haar unitary](Yin_C_F0290_v1.md#statement), in both orientations, regardless of the Borel set.
The general existence of such a constant remains open.

## Argument

### A corrected corner cost and disjoint witnesses

Write \(e=1_F(Z)\) and use the original normal cutoff \(T_r\).
Set
\[
 b(F)=\sup_{r>0,\ x=exe,\ \|x\|\le1}
          \|eT_r(x)e-xeT_r(e)e\|_2 .
\]
The [relative cutoff identity and Gaussian estimate](Yin_C_F0301_v1.md#the-slice-in-the-corner) give
\[
 t^{3/2}a_F\le b(F)\le3t^{3/2}a_F.
\]
The lower inequality is core convergence at \(r\downarrow0\); the upper one uses the bound at each radius on the normalized corner.
If \(a<\infty\), the original [uniform cutoff bound](Yin_C_F0282_v1.md#statement) also gives \(b(F)\le6a\).
The pairing of \(\xi^F\) with \(Z e\) in the normalized corner equals one, so \(v_F\ge t^{3/2}/\|Z\|>0\).

The function \(b\) is lower semicontinuous for convergence of spectral projections in trace \(L^2\).
Indeed fix \(r\) and a contraction \(x=exe\).
For projections \(e_l\to e\), take \(x_l=e_lxe_l\).
All the bounded factors converge strongly-star, and \(T_r(x_l),T_r(e_l)\) converge weakly in \(L^2\) by normality.
Multiplying those bounded Hilbert vectors on either side by the indicated uniformly bounded strongly-star convergent factors preserves weak convergence, by moving the factors to the fixed test vector.
Lower semicontinuity of the Hilbert norm and then the supremum prove the claim.

For \(F'\subset F\), \(v_{F'}\le K v_F\) with a numerical \(K\).
Indeed the squared nonmarginal contribution equals \(\|e(\xi-\xi_B)e\|_2^2\), where \(\xi_B=\mathbb E_{W^*(Z)}\xi\), and decreases upon further compression.
The remaining contribution is comparable in both directions to \(G(\mu|_F)\), the sum of the total squared Menger curvature and the integral of the squared maximal linear density for the unnormalized restricted measure.
Both integrals decrease on restriction. [Corner energy formula](Yin_C_F0301_v1.md#the-actual-relative-derivation-and-its-vacuum) [Scalar geometric criterion](Yin_C_F0255_v1.md#statement)

Under (1) choose sets with \(b(F)/v_F\to\infty\).
The bounds just proved force their masses to tend to zero.
Extract a subsequence \(F_n\) so that deleting the union of all later sets from \(F_n\) retains at least half of \(b(F_n)>0\).
In detail, lower semicontinuity gives a trace-metric neighborhood at each chosen \(F_n\) with that lower bound.
If its radius is \(\rho_n>0\), at stage \(k>n\) require the new mass to be below \(2^{-k}\rho_n^2\) for all earlier \(n\), while keeping the ratios divergent.
The removed mass is less than \(\rho_n^2\).
These differences are disjoint; by the subset estimate and the comparison with \(a_F\), their ratios still tend to infinity.
We use only disjoint positive-mass witnesses below.

### Relabelling and the new vacuum

Let \(K_0=\sigma(Z)\), \(D=1+\|Z\|\), and fix a small \(0<\delta<1/4\).
Use \(\eta=[Z^*,\xi]\) and its joint spectral measure \(\nu_\eta\) for left and right multiplication by \(Z\).
By the [relative energy sum](Yin_C_F0301_v1.md#statement), \(v_F\to0\) on the disjoint sequence.
The masses and the sums of the two \(\nu_\eta\)-leg masses of its pieces tend to zero by finiteness of the measures.
Choose a further subsequence \(B_n\), with \(t_n=\mu(B_n),\ e_n=1_{B_n}(Z)\), so that
\[
 \frac{a_{B_n}}{\|\xi^{B_n}\|_{2,\tau_{B_n}}}>4^n,\qquad
 \alpha_n=2^n v_{B_n}/\delta,\quad D\alpha_n<2^{-n-5},\qquad
 \sum_{n\ge1}4^n\big(t_n+\nu_\eta(B_n\times K_0)+
                                \nu_\eta(K_0\times B_n)\big)<\delta^2.    \tag{3}
\]
All conditions hold by successive selection, for example by imposing the summability requirement with an extra \(2^{-n}\) at stage \(n\).
Write \(B_0\) for the complement, and \(B_*=\bigcup_{n\ge1}B_n\).
Use the identity on \(B_0\) and put
\[
                    \phi(z)= 3D+2^{-n}+\alpha_n z\qquad(z\in B_n).
\]
The changed images lie in disjoint disks separated from the unchanged spectrum by more than one, and the disks indexed by \(n\ne m\) are separated by at least \(2^{-\min(n,m)}/4\).
This gives the stated Borel inverse piece by piece.
The generator changes by at most \((5D+1)\mu(B_*)^{1/2}\) in \(L^2\).

We verify actuality and \(L^2\) proximity of the vacua.
Below all estimates tending to zero are as \(\delta\downarrow0\), with the original tuple fixed.
Let \(\mu'=\phi_*\mu\).
The sum of the geometric energies of its individual positive-index pieces is at most
\(C\sum_n v_{B_n}^2/\alpha_n^2=O(\delta^2)\), by quadratic inverse scaling under a dilation and the corner energy formula.
The zero-index piece has finite energy by restriction.
At a point of any piece the contribution to maximal linear density from the other pieces is at most \(\sum_{m\ne n}t_m/d_{nm}\), where \(d_{nm}\) is the respective separation and \(t_0=\mu(B_0)\).
These sums and their versions with squared denominators are uniformly bounded by (3).
For each triple meeting two distinct pieces the curvature is bounded by twice the inverse distance between any two vertices in distinct pieces.
Partition according to the indices of such a pair, or sum the three pair bounds, to see that the integrated cross curvature squared is finite.
Thus \(G(\mu')<\infty\).
The scalar criterion gives its actual marginal vacuum.
Inside each transformed piece its scalar vacuum is the vacuum for the normalized law on that piece times its mass, plus twice the conjugated Cauchy integral of the other pieces, with the sign convention of the [soft vacuum formula](Yin_C_F0238_v1.md#the-scalar-correction-in-the-liberation-adjoint).
This follows by splitting the weak soft Cauchy limit on the piece; the cross kernels are bounded by the inverse distances and converge by domination there.
Consequently the norm on \(B_*\) of this scalar vector, pulled back by \(\phi\), tends to zero: the within-piece squared norms sum to \(O(\delta^2)\) and the cross terms are uniformly bounded times \(\mu(B_*)^{1/2}\).

For precision on \(B_0\), the new cross integral is bounded by \(\mu(B_*)\).
The old cross integral, interpreted as a weak soft limit on \(B_0\), also tends to zero in \(L^2\) as \(\delta\downarrow0\).
Indeed let \(S_r\) be the old scalar cutoff and \(f=1_{B_*}\).
On \(B_0\), \(S_r f\) is the negative soft Cauchy integral of the removed measure, before conjugation.
The [scalar weight estimate](Yin_C_F0267_v1.md#statement) and the [separated multiplier formula](Yin_C_F0238_v1.md#removing-the-cutoff-in-the-column-norm) give
\[
             \|1_{B_0}S_r f\|_2\le 2(2+\sqrt2)\|f\sqrt W\|_2
\]
for the fixed old integrable marginal weight \(W\).
In fact the cutoff is the full slice minus a probability average of \(S(fv)v^*-fS(v)v^*\) over marginal characters, with \(S\) the full scalar slice.
The last term vanishes on \(B_0\).
The identity extends to the measurable \(f\) by uniformly bounded almost-everywhere polynomial approximation, using the weighted \(L^2\) estimate for \(S\), fixed-radius normality and bounded convergence in the character integral.
The soft integral over the unchanged piece itself has the same weak limit in both laws, by scalar actuality for its normalized restriction.
The old cross bound tends to zero by absolute continuity of \(W\mu\).
Together with absolute continuity of the old scalar vacuum norm on \(B_*\), this proves strong \(L^2\) proximity of the scalar vacua on the common abelian algebra.

For the off-diagonal contribution the [inverse-gap recovery theorem](Yin_C_F0238_v1.md#statement) and the [invariance of partial liberation under spectral relabelling](Yin_C_F0244_v1.md#the-invariant-liberation-derivation) use the same vector \(\eta\), with the inverse conjugate gap as spectral multiplier.
On \(B_0^2\) the old and new multipliers coincide.
The new squared norm accumulated inside the other diagonal blocks is at most \(\sum_n v_{B_n}^2/\alpha_n^2\), by the off-diagonal term in the corner formula.
Across distinct pieces the inverse squared gaps are bounded by \(16\cdot4^{\min(n,m)}\) for positive indices and by one against \(B_0\).
Equation (3) bounds the resulting integral by \(O(\delta^2)\).
The old off-diagonal vector restricted to the rectangles touching \(B_*\) tends to zero in norm by absolute continuity of its two leg measures with respect to \(\mu\).
This proves that the distinguished new vacuum exists and converges to the original one in \(L^2(M,\tau)\) as \(\delta\downarrow0\).
At unchanged coordinates the marginal algebra, scalar law, liberation vacuum and oriented gap are unchanged, so their joint vacua agree by the same recovery formula.
Choose \(\delta\) small enough for the two required norm bounds and the mass bound.

### The cost on each changed piece

On \(B_n\) the relative single-input norm for \(\phi(Z)\) is \(a_{B_n}/\alpha_n\), where the right side is measured in the old coordinate.
Here is a verification that changing the complementary generator by a Borel function preserves this comparison.
In the notation of the [corner construction](Yin_C_F0301_v1.md#extending-liberation-and-restricting-its-two-inner-legs), the old and new outside algebras have the same von Neumann closure: the complement of \(e_n\) is retained as a projection and the two complementary coordinates are related by mutually inverse Borel functions on it.
Their compressions by \(e_n\) likewise have the same von Neumann closure, since the projection is in both outside algebras.
Use the common enlarged algebra generated by these bounded corner coefficients and the corner normal variable.
Both relative liberation derivations agree there, in the following sense.
Their restrictions kill the respective outside coefficients and have the inner-difference rule on the distinguished marginal.
Each bounded coefficient in the common closure admits uniformly bounded strong-star approximants from the original coefficients with derivative zero, and the same from the new coefficients.
For both coordinate choices the liberation graph is closable (its real twist has an actual vacuum, by the [liberation graph argument](Yin_C_F0244_v1.md#the-invariant-liberation-derivation) applied on the relative core).
Consequently the two liberation formulas pass to words in the common enlarged algebra.
The two distinguished marginal generators there are related by the affine transformation with positive slope \(\alpha_n\).

The divided differences on this common algebra kill its coefficients and scale by \(1/\alpha_n\) on the old generating letters when passing to the new derivative.
To justify the norm comparison without assuming norm-dense approximation of the outside coefficients, first compare the two normal relative cutoffs.
By the liberation formula on the common words they differ by the scalar \(1/\alpha_n\) and rescaling \(r\mapsto r/\alpha_n\).
The equality extends to the entire corner by normality and bounded strong-star density.
On any word from the old relative core the new cutoff thus tends to the old relative slice divided by \(\alpha_n\), and conversely for the new core.
This gives the two inequalities for the single-input costs up to a factor three by the [relative Gaussian cutoff estimate](Yin_C_F0301_v1.md#the-slice-in-the-corner).
When one cost is finite, both are finite, and each full relative slice has a normal extension of the same norm: apply the [normal summand proof](Yin_C_F0276_v1.md#a-normal-extension-and-two-normal-densities) to its operator-norm-bounded map on the represented core, whose Hilbert adjoint is densely defined by the actual relative tensor-adjoint formula.
The latter follows on coefficient polynomials by the outer product rule and pairing against the relative vacuum, as in [the actual tensor-adjoint rule](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001).
The normalized full maps agree after rescaling on the common enlarged words by bounded strong-star approximation of their coefficients: on each word the approximating inputs converge boundedly strongly-star and its differentiated outer products converge in coarse norm, as the coefficient derivatives vanish.
Bounded normality then gives equality on the entire corner with the stated scaling.
If either cost is infinite, the two cutoff inequalities already imply both are infinite.

A finite global single-input norm for the relabelled tuple would bound all its \(b(\phi(B_n))\) uniformly by the first part of the proof.
These costs dominate \(t_n^{3/2}a_{B_n}/\alpha_n=\delta\,2^{-n}a_{B_n}/\|\xi^{B_n}\|_{2,\tau_{B_n}}\), which tends to infinity by (3).
This proves the claimed failure at the prescribed coordinate.
The [normal comparison](Yin_C_F0075_v1.md#statement) and the [normal bare-dual criterion](Yin_C_F0070_v1.md#statement) give the existential implications asserted above.

If the normal implication holds universally, the base has finite costs and our construction precludes (1) at every orientation.
Conversely taking the whole spectrum in (2) bounds both original orientations, which gives strong duals by the normal comparison.
For the Möbius coupling, any such relabelling of the base preserves its free independence from the original Haar unitary and leaves the coupled unitary unchanged, with parameter function obtained by composing with the new Borel inverse.
The [Möbius equivalence](Yin_C_F0290_v1.md#statement) gives strong duals on every actual relabelled tuple of this form, excluding (1).
For the conjugate orientation apply the construction at \(Z^*\) on the adjoint pair: conjugating the changed coordinate back yields a Borel relabelling of the original base with the original coupled unitary.
Actuality and strong duality are adjoint stable by the [normal comparison](Yin_C_F0075_v1.md#statement) and [adjoint derivation](Yin_C_F0073_v1.md#statement).
This proves the two bounds for that class.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:01 |
| status | open |
| reason | Fix a separator construction from relative corner ratios and its consequence for the original universal comparison. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Borel spectral amplification, small changes of the generator and actual vacua, equivalent universal estimate and the Möbius application. |
| argument | [Argument](#argument) | Corrected cutoff semicontinuity, disjointization, intra-piece energy and cross terms, relative cost comparison. |
| dependency | [Relative corners](Yin_C_F0301_v1.md#statement) | Vacuum normalization and uniform relative cutoffs on arbitrary Borel sets. |
| dependency | [Normal cutoffs](Yin_C_F0282_v1.md#statement) | Uniform threefold single-input estimate and normality. |
| dependency | [Scalar geometric theorem](Yin_C_F0255_v1.md#statement) | Two-sided comparison with the homogeneous restricted energy. |
| dependency | [Scalar weight](Yin_C_F0267_v1.md#statement) | Weighted bound for the full scalar slice and integrability of its weight. |
| dependency | [Inverse-gap theorem](Yin_C_F0238_v1.md#statement) | Actual vacuum recovery, Gaussian separated multipliers and scalar weak limits. |
| dependency | [Spectral relabelling](Yin_C_F0244_v1.md#the-invariant-liberation-derivation) | Invariance of all the liberation vacua on measurable marginal words. |
| dependency | [Normal summand](Yin_C_F0276_v1.md#a-normal-extension-and-two-normal-densities) | Same-norm normal extension from a bounded core map with dense Hilbert adjoint. |
| dependency | [Actual tensor adjoints](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Hilbert adjoint on polynomial tensors from the actual relative vacuum and the outer product rule. |
| dependency | [Normal comparison](Yin_C_F0075_v1.md#statement) | Two oriented costs decide the strong condition. |
| dependency | [Normal bare duals](Yin_C_F0070_v1.md#statement) | A bare full-domain dual forces boundedness of the prescribed right slice. |
| dependency | [Adjoint stability](Yin_C_F0073_v1.md#statement) | Existence of the actual starred derivation for the adjoint tuple. |
| dependency | [Möbius coupling](Yin_C_F0290_v1.md#statement) | Strong duals in the indicated class whenever the relabelled tuple has actual vacua. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T16:13 |
| status | proved |
| reason | Independent review verified the small Borel perturbation of the generator and its actual vacuum, transfer of corner costs and the uniform-ratio consequence. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Borel spectral amplification, small changes of the generator and actual vacua, equivalent universal estimate and the M枚bius application. |
| argument | [Argument](#argument) | Corrected cutoff semicontinuity, disjointization, intra-piece energy and cross terms, relative cost comparison. |
| dependency | [Relative corners](Yin_C_F0301_v1.md#statement) | Vacuum normalization and uniform relative cutoffs on arbitrary Borel sets. |
| dependency | [Normal cutoffs](Yin_C_F0282_v1.md#statement) | Uniform threefold single-input estimate and normality. |
| dependency | [Scalar geometric theorem](Yin_C_F0255_v1.md#statement) | Two-sided comparison with the homogeneous restricted energy. |
| dependency | [Scalar weight](Yin_C_F0267_v1.md#statement) | Weighted bound for the full scalar slice and integrability of its weight. |
| dependency | [Inverse-gap theorem](Yin_C_F0238_v1.md#statement) | Actual vacuum recovery, Gaussian separated multipliers and scalar weak limits. |
| dependency | [Spectral relabelling](Yin_C_F0244_v1.md#the-invariant-liberation-derivation) | Invariance of all the liberation vacua on measurable marginal words. |
| dependency | [Normal summand](Yin_C_F0276_v1.md#a-normal-extension-and-two-normal-densities) | Same-norm normal extension from a bounded core map with dense Hilbert adjoint. |
| dependency | [Actual tensor adjoints](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Hilbert adjoint on polynomial tensors from the actual relative vacuum and the outer product rule. |
| dependency | [Normal comparison](Yin_C_F0075_v1.md#statement) | Two oriented costs decide the strong condition. |
| dependency | [Normal bare duals](Yin_C_F0070_v1.md#statement) | A bare full-domain dual forces boundedness of the prescribed right slice. |
| dependency | [Adjoint stability](Yin_C_F0073_v1.md#statement) | Existence of the actual starred derivation for the adjoint tuple. |
| dependency | [M枚bius coupling](Yin_C_F0290_v1.md#statement) | Strong duals in the indicated class whenever the relabelled tuple has actual vacua. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0313_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

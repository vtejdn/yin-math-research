---
author: Yin
---
# A power-column relation screen for the original four group labels

Date: 2026-11-12 (Asia/Hong_Kong).
This bounded investigation returns [route four](../strategies/Yin_S_A0004.md) to
\[
r=(1-f)-(1-h)(1-g)^{-1}(1-k),
\qquad f,h,g,k\in G,\quad g\ne e,
\tag{1}
\]
with all labels actual group elements of a torsion-free group.
The selected relation family is \(k=f^2,\ g=h^3\).
Its exact surviving pivot is the equal-modulus trinomial \(1+u-v\), under \(h=u,\ f=uv\).
This is a useful scope test with complete actual-unit and kernel accounting, not a new injectivity theorem for that trinomial and not an equivalence with the all-matrix Task.
The nonindicable calibration below is already covered by the retained finite-index calculation.

## Actual setting and an elementary screen

Work in the actual algebra \(U=\mathcal U(\mathcal N(G))\), using the canonical regular trace and unnormalized matrix traces.
All affiliated products mean closed products.
The [cyclic regular-representation argument](../ledger/Yin_L_A0002_v1.md#cyclic-rational-functions) independently makes \(1-s\) a unit for every nonidentity group element \(s\).
For
\[
A=\begin{pmatrix}1-f&1-h\\1-k&1-g\end{pmatrix},
\]
the known denominator \(1-g\) gives
\[
\operatorname{rk}_G A=1+\operatorname{rk}_G r,
\qquad \dim_G\ker A=\dim_G\ker r.
\tag{2}
\]
These are the actual closed Schur identities, with no assumption of integer rank.

The preliminary flat-rectangle relation \(f=hg^{-1}k\) does give a complete classification, but only through already controlled cyclic factors.
In that case the ordered identity is
\[
r=(1-hg^{-1})(1-g)^{-1}(k-g).
\tag{3}
\]
Indeed
\[
(1-h)(1-g)^{-1}
=hg^{-1}+(1-hg^{-1})(1-g)^{-1},
\]
and substituting \(f=hg^{-1}k\) into (1) gives (3).
If \(h=g\) or \(k=g\), the value is zero.
Otherwise both outside factors in (3) are units by the nonzero group-binomial test, so \(r\) is a unit.
No commutation, integer character, or whole-group Atiyah result is used.
This is a group-relation specialization of the existing product-of-cyclic-units mechanism and supplies no additional propagation rule.

## The chosen power-column family

Now assume
\[
h\ne e,\qquad f\ne e,\qquad g=h^3,\qquad k=f^2.
\tag{4}
\]
The denominator \(1-h^3\) is an independently known actual unit because \(h\) has infinite order.
Put
\[
S=1+h+h^2,\qquad p=h+h^2-f.
\tag{5}
\]
The cyclic element \(S\) is independently a unit: \(S(1-h)=1-h^3\), and both \(1-h\) and \(1-h^3\) are known units.
No assertion about \(p\) is needed for this certificate.

The two-column factorization of the original bounded group-ring matrix is
\[
A=
\begin{pmatrix}
1&1\\
1+f&1+h+h^2
\end{pmatrix}
\begin{pmatrix}
1-f&0\\
0&1-h
\end{pmatrix}.
\tag{6}
\]
Both diagonal entries in the right factor are independently units.
Subtracting \((1+f)\) times the first row from the second row in the left factor leaves the scalar pivot \(p=S-(1+f)\).
Consequently
\[
\operatorname{rk}_G A=1+\operatorname{rk}_G p.
\tag{7}
\]
The scalar Schur value itself has the exact ordered expression
\[
\begin{aligned}
r
&=(1-f)-(1-h)(1-h^3)^{-1}(1-f^2)\\
&=(1-f)-S^{-1}(1+f)(1-f)\\
&=\boxed{S^{-1}p(1-f)}.
\end{aligned}
\tag{8}
\]
Thus the independent outside units give
\[
\boxed{\operatorname{rk}_G r=\operatorname{rk}_G p,
\qquad \dim_G\ker r=\dim_G\ker p.}
\tag{9}
\]
The augmentation of \(p\) is \(1\), so \(p\ne0\) as a group-ring element.
Faithfulness of the regular representation and (8) therefore give \(r\ne0\), without assuming scalar analytic injectivity.
The question in this family is whether its nonzero value has zero kernel.
The affine-to-scalar operation does not itself certify that last pivot.

## Exact inclusion of an equal-modulus trinomial problem

Given actual group elements \(u,v\), set
\[
h=u,\qquad f=uv,\qquad g=u^3,\qquad k=(uv)^2.
\tag{10}
\]
When \(u\ne e\) and \(uv\ne e\), all hypotheses (4) hold and
\[
p=u+u^2-uv=u(1+u-v).
\]
Equation (8) becomes
\[
\boxed{
r=(1+u+u^2)^{-1}u(1+u-v)(1-uv).}
\tag{11}
\]
Every factor outside \(1+u-v\) is independently a unit, hence
\[
\dim_G\ker r=\dim_G\ker(1+u-v).
\tag{12}
\]
This construction uses only the four actual group labels in (10), rather than the rational-Haar substitution used in [C_A0006](../claims/Yin_C_A0006_v1.md#statement).

The excluded cases cannot be silently included in this kernel transfer.
If \(u=e\), the original denominator \(1-u^3\) is zero, so this is not an admissible instance of (1); the separate trinomial \(2-v\) is boundedly invertible by a Neumann series.
If \(u\ne e\) but \(uv=e\), then \(f=k=e\), and the original value \(r\) is zero.
In that case the separate trinomial is \(1+u-u^{-1}\), a nonzero cyclic Laurent polynomial and therefore an actual unit, so equality (12) would be false.
The right factor \(1-uv\) is exactly the failed unit in this degenerate case.
If \(v=e\) or \(v=u\), the trinomial is respectively \(u\) or \(1\), and its invertibility is immediate.

Accordingly, a uniform zero-or-unit theorem for the nondegenerate relation family (4) would resolve the equal-modulus scalar trinomial kernel problem \(1+u-v\), including its omitted cyclic cases by their separate certificates.
Conversely, an injectivity theorem for every such trinomial would settle this relation family through (11).
This is a statement about that scalar family only.
It neither encodes arbitrary complex coefficients nor proves an all-matrix equivalence.

## Existing sufficient conditions already cover the basic positive cases

If the supporting subgroup \(\langle u,v\rangle\) is indicable, choose a nonzero homomorphism \(\phi:\langle u,v\rangle\to\mathbb Z\).
For three distinct support labels \(e,u,v\), the degree multiset
\[
\{0,\phi(u),\phi(v)\}
\]
has a singleton minimum or maximum, since the last two numbers are not both zero.
The [retained singleton-extreme criterion](../ledger/Yin_L_A0008_v1.md#a-singleton-extreme-support-term-and-the-earlier-examples) proves \(1+u-v\) an actual unit.
Coincident support labels have already been handled above.
This application requires no common degree-one hypothesis, but it does require an actual nonzero character on the support subgroup.
It is existing graded coverage, not a new implication of torsion-freeness.

For three distinct support labels, all coefficients have modulus one, so the stated coefficient-dominance test does not apply.
If \(\langle u,v\rangle\) is noncyclic, the support \(\{e,u,v\}\) cannot lie in a cyclic coset, because such a coset containing \(e\) is itself a cyclic subgroup.
This excludes only the direct cyclic-support test, not every possible cyclic factorization or certified multiplier.
No universal energy certificate or independently known division coefficient ring is supplied by the power relations \(k=f^2,\ g=h^3\).
Absent other available coverage, the retained elementary tests leave the nonindicable-support trinomial unresolved.
This is an internal limitation of the demonstrated methods, not a claim to have established the literature-wide status or novelty of the scalar problem.

## The nonindicable Promislow calibration is already solved

Use the [retained actual Promislow model](../ledger/Yin_L_A0010_v1.md#group-and-selected-pencil)
\[
P=\langle a,b\mid b^{-1}a^2b=a^{-2},\ a^{-1}b^2a=b^{-2}\rangle.
\]
It is torsion-free, has normal subgroup \(\langle a^2,b^2,(ab)^2\rangle\cong\mathbb Z^3\) of index four, and has abelianization \(C_4\oplus C_4\).
These facts and their inspected source scope are reused from that fixed material.
Choose
\[
u=a,\quad v=b,\quad h=a,\quad f=ab,\quad g=a^3,\quad k=(ab)^2.
\tag{13}
\]
The distinct quotient cosets show \(a,ab\ne e\), so every denominator and diagonal-binomial hypothesis is satisfied.
The original labels generate \(P\), and no nonzero integer character is available on that supporting subgroup.

Nevertheless the character
\[
\chi(a)=1,\qquad \chi(b)=-1
\]
is compatible with both displayed relators.
The unitary \(V_\chi\delta_s=\chi(s)\delta_s\) implements the trace-preserving automorphism \(\lambda(s)\mapsto\chi(s)\lambda(s)\), which extends to the actual affiliated algebra.
It sends the already certified unit \(1+a+b\) to \(1+a-b\).
The required input is the [explicit four-coset scalar-pivot proof](../ledger/Yin_L_A0010_v1.md#actual-finite-index-matrix-model), not an assumption that an arbitrary new numerator has an inverse.
Consequently (11) independently certifies the selected original Schur value as a unit.

The normalized residual \(1+a-b\) inherits the exact direct-screen exclusions for \(1+a+b\) by the same automorphism.
Its support is unchanged, and positivity of any scalar-phase real part would transport back to the already excluded positive real part for \(1+a+b\).
This assertion concerns that residual and those specified direct tests, not every possible energy realization of the original rational value.
Its invertibility remains within the already established finite-index abelian and known Atiyah coverage.
Repeating the four-coset calculation would add no new independent mechanism.

## Result of the discriminator

The flat relation (3) is exhausted by the old cyclic-factor criterion.
The selected power-column family, which need not satisfy that flat relation, has the exact reduction (11), with the retained scalar trinomial difficulty and all degenerate inputs visible.
The chosen nonindicable example also returns to known coverage.
No new jointly preserved regular-word constraint on the last scalar kernel has been established in this bounded test.
Further work on this family should require a genuinely additional group relation or trace restriction on \(1+u-v\), rather than treating the original four-label notation or the already admissible cyclic denominator as a new constraint.
All mathematical inputs above are direct calculations or the explicitly linked fixed cyclic, graded, actual-Schur and Promislow proofs; no new external theorem is used.

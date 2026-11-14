---
author: Yin
---

# Conjugate variables force a hidden commuting drift to be measurable in the observed coordinate

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(Z\) be bounded normal with diffuse law \(\nu\), let \(k=k^*\) be bounded and commute with \(Z,Z^*\), and put \(A=W^*(Z,k)\).
Let \(v=v^*\) be bounded with diffuse law and actual scalar conjugate variable \(g\), free from \(A\) in a von Neumann algebra with faithful normal probability trace \(\tau\).
Set \(T=k+v\) and take the represented starred polynomial algebra \(P\) of \((Z,T)\).
The joint law of \(Z,k\) on \(\mathbb C\times\mathbb R\) is denoted by \(\pi(dz,dx)\).
Define
\[
 I=\iint_{z\ne w}\frac{|x-y|^2}{|z-w|^2}\,d\pi(z,x)d\pi(w,y).
 \tag{1}
\]
Then \(W^*(Z,T)=W^*(A,v)\), the distinguished coordinate \(T\) always has an actual conjugate variable, and the following are equivalent.

1. The distinguished coordinate \(Z\) has an actual conjugate variable on \(P\).
2. The pair satisfies the [full actual conjugate-variable condition](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
3. The pair has a strong dual system with both bounded-vector domains.
4. The scalar law \(\nu\) has an actual divided-difference conjugate variable \(\zeta\), and \(I<\infty\).

Finiteness of \(I\) forces \(k=f(Z)\) for a bounded real Borel function \(f\).
In that case (1) is the squared \(L^2(\nu^2)\) norm of the divided difference of \(f\).
Under the equivalent conditions the joint vacua satisfy
\[
             \xi_T=g,\qquad \|\xi_Z\|_2^2=\|\zeta\|_2^2+\|g\|_2^2 I.
 \tag{2}
\]
The original right contractions at both coordinates have finite column costs for the pair and its adjoint tuple, and their negative closures on the respective original cores give the generator-first strong duals.
The column cost of a slice \(E\) is the supremum of \((\sum_j\|Ep_j\|_2^2)^{1/2}\) over finite mixed starred polynomial columns satisfying \(\|\sum_jp_j^*p_j\|\le1\).

In particular, let \(S,V\) be standard free semicirculars of variance one, \(0<|\rho|<1\) real, \(q=\sqrt{1-\rho^2}\), \(T=\rho S+qV\), and let \(\mu\) be the standard semicircular law.
For a bounded Borel map \(h:[-2,2]\to\mathbb C\) with diffuse image law write
\[
 J(h)=\iint_{h(s)\ne h(t)}\frac{|s-t|^2}{|h(s)-h(t)|^2}\,d\mu(s)d\mu(t).
 \tag{3}
\]
The pair \((h(S),T)\) generates \(W^*(S,V)\) even when \(h\) loses spectral information.
It satisfies the equivalent conditions above exactly when \(h_*\mu\) has an actual scalar vacuum \(\zeta_h\) and \(J(h)<\infty\).
Its distinguished vacuum then has squared norm \(\|\zeta_h\|_2^2+\rho^2 J(h)/(1-\rho^2)\), and \(h\) is injective on a conull Borel set.
For \(h(s)=|s|\), both marginals have actual scalar vacua but \(h(S)\) has no distinguished actual conjugate variable on the mixed core.

For two bounded Borel maps \(h_1,h_2\) that are each injective on a conull Borel subset of \([-2,2]\), consider \((h_1(S),h_2(T))\).
Its full actual and strong conditions are equivalent to the two scalar vacuum conditions and \(J(h_1),J(h_2)<\infty\).
Each squared vacuum norm is \(\|\zeta_{h_i}\|_2^2+\rho^2J(h_i)/(1-\rho^2)\).
All original column costs are finite in both orientations under this criterion.

## Argument

### Recovering the unobserved drift and differentiating the noise

Choose a Haar unitary \(u\in W^*(Z)\), possible by diffuseness.
The averages of \(u^jTu^{-j}\), \(1\le j\le n\), converge in \(L^2\) to \(k+\tau(v)1\).
Indeed \(k\) commutes with \(u\), and the vectors \(u^j(v-\tau(v))u^{-j}\) are mutually orthogonal by freeness, since \(\tau(u^{j-l})=0\) for \(j\ne l\).
The uniformly bounded averages lie in \(W^*(Z,T)\), so their bounded limit belongs to it by the trace-preserving conditional expectation.
This recovers \(k\), hence \(v=T-k\) and the whole asserted algebra \(M=W^*(A,v)\).

Work in the algebraic free product \(\mathcal Q=A*\mathbb C[v]\) inside \(M\), using centered reduced words for its faithful realization.
On \(\mathcal Q\) let \(d\) kill \(A\) and be the scalar difference quotient on \(\mathbb C[v]\).
Its vacuum is \(g\), since cuts on centered reduced words with at least two blocks leave a centered free segment on one trace leg, and the single-block test is the scalar vacuum identity.
Its restriction to \(P\) kills \(Z,Z^*\) and takes \(T\) to \(1\otimes1\).
The vacuum remains \(g\) since \(P\) is Hilbert dense by generation.
Restricting further to the polynomial algebra of \(T\) gives a scalar actual conjugate variable by projecting \(g\) onto \(L^2(W^*(T))\), hence \(T\) has diffuse law. [Diffuseness under the normal conjugate-variable condition](Yin_C_F0076_v1.md#statement)

### The liberation vacuum before recovering the hidden function

Let \(\gamma_0\) take \(a\in A\) to \(a\otimes1-1\otimes a\), kill \(v\), and extend by the outer Leibniz rule.
Its double trace vanishes on \(\mathcal Q\), by the same reduced-word test and the inner difference on a single \(A\)-block.
For a separated tensor \(b\otimes c\), write \(I_{b\otimes c}(l\otimes r)=lb\otimes cr\).
With \(L=1\otimes k-k\otimes1\), put \(\gamma=\gamma_0+I_Ld\).
It acts by the inner difference on \(A\) and kills \(T\), so its restriction to \(P\) is represented partial liberation at \(Z\).
For \(a,b\in A\) the map \(J_g(a\otimes b)=agb\) extends to the coarse Hilbert tensor of \(A\), with norm \(\|g\|_2\) times the input norm.
Indeed \(g\) is real and centered by the scalar vacuum identity, and freeness gives \(\mathbb E_A(g^*a g)=\|g\|_2^2\tau(a)1\) by centered bounded approximation.
For the two separated terms of \(L\), cyclicity and \(dA=0\) turn their double trace on \(p\) into that of \(d(pk)\) and \(d(kp)\), respectively.
Thus, for inner products linear in the second variable, the vacuum of \(\gamma|_P\) is \(gk-kg=J_g(L)\).
Multiplying \(J_g(a\otimes b)\) on the left and right by spectral functions of \(Z\) acts on its two arguments separately.
It follows that the joint spectral measure of this liberation vacuum assigns to a Borel set \(D\subset\mathbb C^2\) the mass
\[
      \|g\|_2^2\iint 1_D(z,w)|x-y|^2\,d\pi(z,x)d\pi(w,y).
\]
It gives zero mass to the diagonal since \(\nu\) is diffuse.
The [marginal and inverse-gap criterion](Yin_C_F0238_v1.md#statement) on \(P\) now gives the equivalence of 1, 2 and 4 and the norm formula (2).
Here \(\|g\|_2>0\) because \(\langle g,v\rangle=1\).

### Conditional variance and both domains

Disintegrate \(\pi(dz,dx)=\nu(dz)\pi_z(dx)\) and denote the conditional mean and variance of \(x\) by \(m(z),a(z)\).
For independent draws from \(\pi_z,\pi_w\) the mean of \(|x-y|^2\) is \(a(z)+a(w)+|m(z)-m(w)|^2\).
If \(a\ge\epsilon>0\) on a set \(F\) of positive \(\nu\)-measure, the integral in (1) dominates \(\epsilon\iint_{z\ne w}|z-w|^{-2}\,d\nu|_F(z)d\nu|_F(w)=\infty\) by the [critical planar energy lemma](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation).
Therefore finite energy forces \(a=0\) almost everywhere and \(k=m(Z)\) by faithfulness of the trace and the formula for \(\|k-m(Z)\|_2^2\).
The conditional mean has a bounded real Borel representative.
Apply the [measurable location and scale theorem](Yin_C_F0277_v1.md#statement) to \(T=m(Z)+v\), with scale identically one and (1) as its drift energy.
It gives both original right-column bounds in both orientations on unrestricted mixed words and the stated full-domain canonical operators.
Conversely a strong system gives actual conjugate variables for a normal tuple by the [strong domain implication](Yin_C_F0070_v1.md#statement).

### One or two Borel images of a correlated semicircular pair

Take \(Z=h(S)\), \(k=\rho S\) and noise \(qV\).
The noise has scalar vacuum \(V/q\), by the scaled difference quotient for the semicircular law, and \(A=W^*(S)\).
Equation (1) equals \(\rho^2 J(h)\).
Thus the general result gives the claimed generation, criterion and norm.
Finiteness of \(J(h)\) yields \(s=m(h(s))/\rho\) for \(\mu\)-almost every \(s\), which gives conull Borel injectivity directly.
For \(h(s)=|s|\) the image law has bounded density \(1_{(0,2)}(r)\sqrt{4-r^2}/\pi\), so its scalar vacuum exists by the [real \(L^3\)-density criterion](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate).
The law of \(T\) is standard semicircular, while \(\operatorname{Var}(S\mid |S|=r)=r^2\) on \(0<r<2\), giving infinite joint energy.

For the assertion on two conull injective maps, the inverse of each map on its conull image is Borel.
The partial liberation vacuum for the original pair \((S,T)\), distinguished at \(S\), is the vector computed above with \(k=\rho S\) and noise \(qV\).
Its joint spectral measure at \(S\) is \(\rho^2|s-t|^2d\mu(s)d\mu(t)/(1-\rho^2)\).
The original pair is actual by the one-image case \(h(s)=s\).
The pair also admits the regression \(S=\rho T+qW\) with \(W=qS-\rho V\) a standard semicircular free from \(T\).
Indeed the orthogonal change of the two real coefficient vectors preserves the variance-one semicircular joint moments by the [matching-color Wick rule](../audits/literature/NS06/Yin_U004.md#ns06-u004).
Thus the liberation spectral measure at \(T\) has the same expression in its own variables.
The [Borel relabelling criterion](Yin_C_F0244_v1.md#statement), item 1, pushes these two spectral measures forward separately on the full core of \((h_1(S),h_2(T))\).
It gives the stated criterion for actuality and both norm formulas, including when one of the energies obstructs the corresponding coordinate.

Under this criterion the one-image case gives both orientations of the original column bound at \(h_1(S)\) for \((h_1(S),T)\).
Item 2 of the same relabelling theorem applies to that source with the identity map on \(h_1(S)\), whose inverse secant is the constant Schur multiplier one, and the Borel relabelling \(h_2\) on the omitted coordinate.
It gives the bound at \(h_1(S)\) on unrestricted target columns, also in the adjoint orientation by conjugating the labellings.
Interchange \(S,T\) using the second regression to obtain the two bounds at \(h_2(T)\).
The [two-contraction domain theorem](Yin_C_F0072_v1.md#statement) gives both bounded-vector domains for the canonical operators, and the normal strong-to-actual implication supplies the converse.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T15:13 |
| status | open |
| reason | Fix the commuting-drift obstruction, the full mixed-domain criterion and its one- and two-image semicircular consequences for review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Hidden commuting drift, original domains, a genuine spectral fold and two injective changes of a correlated semicircular pair. |
| argument | [Argument](#argument) | Centred-noise recovery, liberation, disintegration, critical planar energy and regression in both coordinate directions. |
| dependency | [Normal diffuseness](Yin_C_F0076_v1.md#statement) | Diffuse law for the noise-shifted variable by its actual scalar vacuum. |
| dependency | [Inverse-gap criterion](Yin_C_F0238_v1.md#statement) | Distinguished vacuum existence and norm from the actual liberation vector and the marginal vacuum. |
| dependency | [Critical planar energy](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Infinite inverse-square energy of a positive diffuse restricted law on bounded planar support. |
| dependency | [Measurable drift](Yin_C_F0277_v1.md#statement) | The visible-drift case with unit scale supplies unrestricted original columns in both orientations and both canonical domains. |
| dependency | [Normal strong domains](Yin_C_F0070_v1.md#statement) | Existence of a strong system implies actual starred conjugate variables. |
| dependency | [Borel relabelling](Yin_C_F0244_v1.md#statement) | Pushed liberation measures and mixed columns for changes to an omitted coordinate. |
| dependency | [Real marginal criterion](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Scalar conjugate variable for the bounded folded semicircular density. |
| dependency | [Semicircular moments](../audits/literature/NS06/Yin_U004.md#ns06-u004) | Free standard semicircular law, its scaled vacuum and the reverse regression by orthogonal change of coordinates. |
| dependency | [Two oriented contractions](Yin_C_F0072_v1.md#statement) | Both full bounded-vector domains for the twice relabelled original canonical duals. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T15:23 |
| status | proved |
| reason | The independent review verifies hidden drift recovery, the conditional variance obstruction and the full domains in both semicircular regressions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Hidden commuting drift, original domains, a genuine spectral fold and two injective changes of a correlated semicircular pair. |
| argument | [Argument](#argument) | Centred-noise recovery, liberation, disintegration, critical planar energy and regression in both coordinate directions. |
| dependency | [Normal diffuseness](Yin_C_F0076_v1.md#statement) | Diffuse law for the noise-shifted variable by its actual scalar vacuum. |
| dependency | [Inverse-gap criterion](Yin_C_F0238_v1.md#statement) | Distinguished vacuum existence and norm from the actual liberation vector and the marginal vacuum. |
| dependency | [Critical planar energy](Yin_C_F0204_v1.md#the-diagonal-value-of-the-differentiated-central-relation) | Infinite inverse-square energy of a positive diffuse restricted law on bounded planar support. |
| dependency | [Measurable drift](Yin_C_F0277_v1.md#statement) | The visible-drift case with unit scale supplies unrestricted original columns in both orientations and both canonical domains. |
| dependency | [Normal strong domains](Yin_C_F0070_v1.md#statement) | Existence of a strong system implies actual starred conjugate variables. |
| dependency | [Borel relabelling](Yin_C_F0244_v1.md#statement) | Pushed liberation measures and mixed columns for changes to an omitted coordinate. |
| dependency | [Real marginal criterion](Yin_C_F0244_v1.md#arbitrary-lipschitz-graphs-over-a-real-coordinate) | Scalar conjugate variable for the bounded folded semicircular density. |
| dependency | [Semicircular moments](../audits/literature/NS06/Yin_U004.md#ns06-u004) | Free standard semicircular law, its scaled vacuum and the reverse regression by orthogonal change of coordinates. |
| dependency | [Two oriented contractions](Yin_C_F0072_v1.md#statement) | Both full bounded-vector domains for the twice relabelled original canonical duals. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0292_v1.md#finding) | The fixed proof, all nine inputs, the folded example and the transfer through two actual intermediate pairs. |

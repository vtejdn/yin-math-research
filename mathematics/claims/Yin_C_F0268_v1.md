---
author: Yin
---

# Hilbert–Schmidt drift criterion for an arbitrary free selfadjoint coordinate

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\) be bounded normal generators of a finite von Neumann algebra \(R\) with faithful normal probability trace \(\tau\).
Assume actual starred ACSY on \(P_X=\mathbb C\langle X,X^*\rangle\), with conjugate vectors \(\xi_i\), and finite [right column costs](Yin_C_F0208_v1.md#statement) for all coordinates of both \(X\) and \(X^*\).
Write \(H=L^2(R)\), \(E_i=\overline{(\mathrm{id}\otimes\tau)\partial_i|_{P_X}}\) and \(P_1=|1\rangle\langle1|\), using inner products linear in their second argument.
Let \(v=v^*\) be bounded with diffuse scalar law and actual scalar divided-difference vacuum \(g=\xi_v\).
In \(\widehat R=R*W^*(v)\) take any bounded \(B=B^*\in R\) and set \(T=v+B,\ Y=(X,T)\).
The following conditions are equivalent.

1. \(Y\) satisfies the [actual starred ACSY condition](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct) on its represented starred polynomial core.
2. \(Y\) has a strong dual system in the generator-first convention on all bounded vectors, with the actual adjoint domains also containing all bounded vectors.
3. For every \(i\), \(K_i a=E_i(Ba)-B E_i(a)\) on \(a\in R\) extends to a Hilbert–Schmidt operator on \(H\).

When these hold, the negative closures of the original right slices give the strong duals, and both \(Y\) and \(Y^*\) have finite column costs at every coordinate.
Put \(\Theta(a\otimes b)=aP_1 b\) with left multipliers understood, extended unitarily from \(H\otimes_2 H\) to \(S_2(H)\).
Set \(\beta_i=-\Theta^{-1}K_i\), \((a\otimes b)^\star=a^*\otimes b^*\), and \(J_g(a\otimes b)=a g b\), extended from bounded \(a,b\).
The vacua on the target core satisfy
\[
   \xi_i(Y)=\xi_i+J_g(\beta_i^\star),\qquad
   \|\xi_i(Y)\|_2^2=\|\xi_i\|_2^2+\|g\|_2^2\|K_i\|_{\rm HS}^2,\qquad
   \xi_{d+1}(Y)=g.                                                       \tag{1}
\]
The [semicircular drift theorem](Yin_C_F0212_v1.md#statement) has \(g=v\) for a standard semicircular variable.
Here the terminal-block argument uses the scalar slice of the specified free selfadjoint coordinate, and permits a noncommutative base and drifts outside any prescribed coarse derivation domain.

## Argument

### A centered noise test forces the base commutator

The bounded-vector domains of \(E_i,E_i^*\) follow from the oriented base costs by [the base-domain argument](Yin_C_F0212_v1.md#the-canonical-slices-on-the-base-and-its-free-extensions).
On the free reference core of \((X,v)\) let the old derivation kill \(v\), with right slice closure \(L_i\).
The same argument, using arbitrary centered free prefixes ending in the new factor, gives both full domains, vacuum \(\xi_i\), and right column cost at most the old \(c_i(X)\).
Its proof groups the coefficients for every entry of the input column and uses \(\sum_{j,w} b_{jw}^*b_{jw}=\mathbb E_R(\sum_j p_j^*p_j)\).
These identities use only the reduced-word representation of the free factor.
To extend the column bounds to bounded inputs, approximate a finite bounded column strongly-star by core columns of at most its norm up to an arbitrarily small error by matrix Kaplansky density.
Weak closedness of the graph identifies every weak cluster point of the bounded images with the unique original closure values.
The same graph argument proves weak convergence of each closed slice along bounded strong-star approximation.
Also \(W^*(Y)=\widehat R\), since this algebra contains \(R\) and then \(v=T-B\).

Suppose \(Y\) is actual and let \(\zeta\) be its \(i\)-th vacuum.
The target old derivative agrees with \(\partial_i\) on \(P_X\) by the [forced normal starred values](Yin_C_F0076_v1.md#statement).
Thus the orthogonal projection of \(\zeta\) onto \(H\) is \(\xi_i\).
Put \(v_0=v-\tau(v)1,\ B'=B+\tau(v)1\), so \(T=v_0+B'\) and \([E_i,B']=[E_i,B]\).
Freeness gives \(\|J_{v_0}d\|_2=\|v_0\|_2\|d\|_2\) for every coarse tensor \(d\).
Indeed for any centered \(c\in L^2(W^*(v))\), the identity for \(J_c\) follows from \(\mathbb E_R(c^*a c)=\tau(a)\|c\|_2^2 1\), first for bounded centered \(c\) and then by centered \(L^2\)-approximation.

Test the actual vacuum on \(aTb\) with \(a,b\in P_X\).
Its two endpoint derivatives have zero double trace in the terms containing \(v_0\), and its middle derivative vanishes.
Subtract the pairing with the \(R\)-part \(aB'b\).
As in the [one-noise test](Yin_C_F0212_v1.md#the-forced-one-noise-vacuum-component), this yields
\[
 \langle \zeta,a v_0 b\rangle
 =(\tau\otimes\tau)\big((\partial_i a) B'b+a B'(\partial_i b)\big)
                                      -\langle\xi_i,a B'b\rangle
 =-\langle a^*,K_i b\rangle .                                           \tag{2}
\]
For the last equality first replace \(B'\) by a selfadjoint core polynomial, expand its derivative by the product rule, and use \([E_i,B']b=\Theta(\partial_i B')b\) for that polynomial.
Pass to \(B'\) by uniformly bounded strong approximation, pairing \(E_i(B'b)\) with \(a^*\in\operatorname{Dom}E_i^*\).
All other multipliers act on fixed Hilbert or coarse vectors.
In particular (2) defines a Hilbert-bounded functional on \(H\otimes_2 H\) of norm at most \(\|\zeta\|_2\|v_0\|_2\).
For its Riesz vector \(d\), \(\langle d,a\otimes b\rangle=\langle a^*,\Theta(d^\star)b\rangle\), first on bounded simple tensors by cyclicity, then by density.
Thus \(K_i=-\Theta(d^\star)\) on core vectors.
Bounded strong-star approximation of any \(b\in R\) gives weak convergence of \(E_i b\) and \(E_i(Bb)\) by the graph argument above, extending this identity to \(R\).
The norm of the centered \(v_0\) is used only in this necessity test.

### Inserting an arbitrary base tensor at the selfadjoint coordinate

Write \(N=W^*(v)\), \(M=\widehat R\), \(C=\mathrm{id}\otimes\tau\), and \(e=C\partial_v\) for the scalar right slice on \(\mathbb C[v]\).
The [actual scalar estimate](Yin_C_F0055_v1.md#statement) gives a finite \(a_v\) with \(\|e b\|_2\le a_v\|b\|\).
Write \(\kappa=4/\pi\) for the squared constant of the [complex finite-family inequality](Yin_C_F0045_v1.md#2-reuse-and-the-remaining-imported-functional-analytic-input).
The vector \(g=e^*1\) is centered by \(e1=0\).
For \(\beta\in H\otimes_2H\) let \(d_\beta R=0,\ d_\beta v=\beta\) on the algebraic free product \(\mathcal Q=R*\mathbb C[v]\).
The scalar law is diffuse, so \(v\) has no polynomial relation, and the centered free-word representation embeds \(\mathcal Q\) into \(M\).
The product rule defines \(d_\beta\) on this core, assigning to each input a finite sum of bounded outer multipliers acting on \(\beta\).

We prove the estimate for all finite columns in \(\mathcal Q\)
\[
 \left(\sum_j\|Cd_\beta(p_j)\|_2^2\right)^{1/2}\le
       (2\sqrt\kappa\, a_v+2\|g\|_2)\,\|\beta\|_2
               \left\|\sum_j p_j^*p_j\right\|^{1/2}.                    \tag{3}
\]
The [unitary terminal estimate](Yin_C_F0265_v1.md#a-global-square-integrable-kernel-estimate-for-mixed-columns) uses a scalar spectral base.
Here we keep the order of all base products via the right free-module isometry, including when a scalar terminal coefficient deletes the last noise block.

Start with \(\beta=\sum_{\ell=1}^n x_\ell\otimes y_\ell\), \(x_\ell,y_\ell\in R\).
Write \(N^\circ=L^2(N)\ominus\mathbb C1\), and use the analogous \(R^\circ\).
Each reduced word containing a noise block has the form \(q b a\), where \(q\) is empty or ends in \(R^\circ\), \(b\in\mathbb C[v]\) is centered, and \(a\in R\) includes the option \(a=1\).
The last \(N\)-block gives
\[
  Cd_\beta(qba)=\sum_\ell q(e b)x_\ell\,\tau(a y_\ell),\qquad
  Cd_\beta(R)=0 .                                                       \tag{4}
\]
Indeed earlier cuts have a centered suffix starting in \(R^\circ\) and containing a later centered \(N\)-block.
Trace cyclicity joins the terminal \(a\) to the inserted \(y_\ell\).
Before this final base coefficient the suffix starts in \(R^\circ\) and ends in \(N^\circ\).
Left multiplication by the right-leg noise coefficient, split into scalar and centered parts, gives two reduced words each containing a centered noise block.
Both have zero conditional expectation onto \(R\).
At the last cut with second-leg noise coefficient \(f\), the trace is \(\tau(y_\ell f a)=\tau(f)\tau(a y_\ell)\) by freeness and traciality.
This proves (4) with the stated order of \(x_\ell,y_\ell\).

Write \(e b=e_c b+\tau(b g^*)1\), with \(e_c b\) centered.
Take a unit column \((p_j)_{j=1}^m\).
Let \(K_0\) be the closed span of reduced words ending in \(N^\circ\).
Multiplication is isometric from \(K_0\otimes_2 H\) into \(L^2(M)\) by appending a base block and splitting it into its scalar and centered parts.
For \(y\in R\), expand \(p_j y=\sum_w w c_{jw}\) in the right \(N\)-module basis, where \(w=1\) or a reduced orthonormal prefix ending in \(R^\circ\), and \(c_{jw}\in\mathbb C[v]\).
For a finite family, adapting bases to its finitely many centered factors gives finite expansions.
The [conditional module identity](Yin_C_F0045_v1.md#3-an-orthogonal-right-module-decomposition-of-the-full-core), which follows from the same reduced-word orthogonality for the two factors \(R,N\), gives
\[
 \sum_{j,w}c_{jw}^*c_{jw}
   =\mathbb E_N\!\left(y^*\sum_jp_j^*p_j\,y\right)
   \le\mathbb E_N(y^*y)=\|y\|_2^2 1.
\]
Project \(p_j y\) onto \(\mathbb C1\oplus K_0\).
This subtracts \(\tau(c_{jw})\) at \(w\ne1\) and keeps the full coefficient at \(w=1\).
The removed scalar column has norm at most \((\sum_{j,w}\tau(|c_{jw}|^2))^{1/2}\le\|y\|_2\).
Thus the projected coefficients \(c'_{jw}\) have column norm at most \(2\|y\|_2\).
Set \(S_p y=(\sum_w w e_c(c'_{jw}))_j\) in \(K_0^m\).
This formula is independent of the orthonormal prefix basis by linearity and the tensor decomposition.
Applying the finite-family inequality to \(e_c:C^*(v)\to N^\circ\) on all \(j,w\) gives \(\|S_p y\|_2\le2\sqrt\kappa\,a_v\|y\|_2\).
For \(p_j=qba\) it returns \(q(e_c b)\tau(a y)\), and base-only words give zero since \(e_c1=0\).
Hence the centered output in (4) is the multiplication image of \(\sum_\ell(S_p y_\ell)\otimes x_\ell\).
The isometry on \(K_0^m\otimes_2 H\) and the Hilbert bound for \(S_p\) bound that image by \(2\sqrt\kappa\,a_v\|\beta\|_2\).

For the scalar output let \(Q\) be the orthogonal projection onto \(K_0\), and let \(P=1-Q\).
The projection \(P\) retains the empty word and words ending in \(R^\circ\).
On a word \(qba\), expanding \(a y_\ell\) gives
\[
          P(qba y_\ell g^*)=q\,\tau(bg^*)\,\tau(a y_\ell).
\]
For the centered component of \(a y_\ell\) the last letter \(g^*\) remains and the projection kills the word.
The scalar component leaves \(b g^*\), whose mean alone survives the projection.
Base-only inputs have projection zero since \(g\) is centered.
These formulas for \(g\in L^2(N)\) follow from bounded centered truncations.
Consequently the scalar output column equals
\[
 \left(p_j\sum_\ell y_\ell g^*x_\ell\right)_j
                      -\left(\sum_\ell Q(p_j y_\ell g^*)x_\ell\right)_j .
                                                                         \tag{5}
\]
The first column has norm at most \(\|g\|_2\|\beta\|_2\) by the \(J_{g^*}\) isometry up to scale and the input column norm.
For the second use \(U_p y=(Q(p_j y g^*))_j\in K_0^m\).
The input column, the orthogonal projection, and freeness give \(\|U_p y\|_2\le\|y g^*\|_2=\|y\|_2\|g\|_2\).
Multiplication maps \(\sum_\ell(U_p y_\ell)\otimes x_\ell\) isometrically onto that second column.
Its norm is therefore at most \(\|g\|_2\|\beta\|_2\), proving (3) for finite bounded tensors.
Density and continuity of each fixed polynomial evaluation \(d_\beta p\) in the coarse Hilbert space give (3) for arbitrary \(\beta\).

The vacuum is
\[
                         d_\beta^*(1\otimes1)=J_g(\beta^\star).          \tag{6}
\]
For a finite bounded tensor \(\beta=\sum_\ell x_\ell\otimes y_\ell\) let \(d=d_{1\otimes1}\), which is the ordinary free extension with vacuum \(g\).
The vacuum extends from the noise marginal because a reduced centered word with two or more blocks retains a centered free segment on at least one trace leg of each nonzero cut.
Since \(d\) kills \(R\), the double trace of \(d_\beta p\) is the sum of the double traces of \(d(x_\ell p y_\ell)\) by traciality.
Their sum is \(\langle\sum_\ell x_\ell^*g y_\ell^*,p\rangle\).
Pass to arbitrary \(\beta\) by the coarse evaluation continuity and the scaled isometry for \(J_g\).

Put \(F_\beta=\overline{Cd_\beta|_{\mathcal Q}}\).
For the flip-adjoint \((a\otimes b)^\dagger=b^*\otimes a^*\), one has \(d_\beta(p^*)^\dagger=d_{\beta^\dagger}(p)\), as \(v=v^*\).
Thus (3) bounds both one-input contractions, and the [two-contraction domain theorem](Yin_C_F0072_v1.md#statement) gives both full bounded-vector domains and bounded restrictions of the slice and its adjoint.
Its column bound (3) extends to all bounded inputs by matrix Kaplansky approximation and the closed graph as above.
The core product rule gives \([F_\beta,L_r]=0\) for \(r\in R\) and \([F_\beta,L_v]=\Theta(\beta)e_R\), where \(e_R:L^2(M)\to H\) is conditional expectation and the range \(H\) is embedded in \(L^2(M)\).
The second identity follows first on bounded simple tensors since the inner vector of each rank-one operator lies in \(H\), then by Hilbert–Schmidt convergence.
These identities hold on bounded vectors by the same bounded strong approximation, or by the original graph closure and bounded right-hand sides.

### Correction on the original target system

Assume condition 3.
For the free old slice the [bounded drift commutator compression](Yin_C_F0212_v1.md#compression-of-the-commutator-with-a-bounded-drift) gives \([L_i,L_B]=K_i e_R\) on \(M\).
In the right free-prefix formula, left multiplication by \(B\) preserves the span of nonempty prefixes ending in the noise factor, so the commutator vanishes on these summands.
The vacuum prefix gives \(K_i\).
Uniformly bounded polynomial approximation extends it to \(B\) and to all bounded input vectors using the original closed graph.
Also \(L_i\) commutes with \(v\) and has \([L_i,L_{X_j}]=\delta_{ij}P_1\) on bounded vectors, by its free core product rule and the same extension.
Set \(U_i=(L_i+F_{\beta_i})|_{M1}\) for old \(i\), and \(U_{d+1}=F_{1\otimes1}|_{M1}\).
Each sum has dense domain, all bounded vectors lie in its actual adjoint domain by pairing the two original adjoints, and \(U_j1=0\).
In particular these sums are closable.
Since \(\Theta(\beta_i)=-K_i\), the commutators with \(v+B\) cancel at the old coordinates, while the last commutator is \(P_1\).
All correction operators commute with the old generators.
Thus \((-U_j)_j\) witnesses the strong condition and the [normal strong-to-actual theorem](Yin_C_F0070_v1.md#statement) gives the target actual derivations and their vacua \(U_j^*1\).
Equations (6) and (1) agree because \(L_i^*1=\xi_i\) and \(J_g(\beta_i^\star)\) is orthogonal to \(H\) by centering and freeness.
For \(j=d+1\) this gives \(J_g(1\otimes1)=g\).
The [canonical normal comparison](Yin_C_F0075_v1.md#statement), part 4, identifies the original canonical slices with the \(U_j\) on bounded vectors, including their two full domains.
On the target core the resulting columns are bounded by the sum of the already extended column bounds for \(L_i\) and \(F_{\beta_i}\), or by (3) for the last coordinate.
For the adjoint tuple, actual ACSY passes to \(Y^*\) by [the flip-adjoint rule](Yin_C_F0076_v1.md#statement).
Apply (2) to its base \(X^*\), whose two oriented costs are finite by hypothesis, and use its resulting Hilbert–Schmidt commutators in the preceding sufficiency and column proof.
This gives the two orientations without any coarse differentiability assumption on \(B\).

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T13:19 |
| status | open |
| reason | Fix the noncommutative-base insertion bound, arbitrary selfadjoint noise criterion and exact vacuum cost for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Hilbert–Schmidt equivalence with the actual and strong conditions, original domains, both column orientations and the vacuum vectors. |
| argument | [Argument](#argument) | Centered first-noise test, tensor insertion with noncommuting coefficients and operator correction on all bounded vectors. |
| dependency | [Free reference lifting](Yin_C_F0212_v1.md#the-canonical-slices-on-the-base-and-its-free-extensions) | Finite oriented base columns, both bounded-vector domains and their right free-module extension to an arbitrary free factor. |
| dependency | [Bounded drift compression](Yin_C_F0212_v1.md#compression-of-the-commutator-with-a-bounded-drift) | Compression of the old slice commutator to the base conditional-expectation summand. |
| dependency | [One-noise test](Yin_C_F0212_v1.md#the-forced-one-noise-vacuum-component) | Old endpoint pairing and bounded approximation of the drift, using the centered noise with its actual variance here. |
| dependency | [Terminal column estimate](Yin_C_F0265_v1.md#a-global-square-integrable-kernel-estimate-for-mixed-columns) | Last-noise decomposition and simultaneous centered \(C^*(v)\)-coefficient estimate, with noncommutative deletion treated in (5). |
| dependency | [Right free-module structure](Yin_C_F0045_v1.md#3-an-orthogonal-right-module-decomposition-of-the-full-core) | Free prefix orthogonality and the expectation identity for the terminal coefficient columns. |
| dependency | [Finite-family inequality](Yin_C_F0045_v1.md#2-reuse-and-the-remaining-imported-functional-analytic-input) | Hilbert square bound for maps from the abelian noise \(C^*\)-algebra tested on finite coefficient families. |
| dependency | [Actual scalar estimate](Yin_C_F0055_v1.md#statement) | The operator-norm-to-Hilbert estimate for the actual scalar selfadjoint right slice. |
| dependency | [Normal phase and adjoint](Yin_C_F0076_v1.md#statement) | Restriction of original actual old derivatives and passage to the adjoint orientation. |
| dependency | [Canonical domains](Yin_C_F0072_v1.md#statement) | The two original bounded-vector domains from right and reversed contraction estimates. |
| dependency | [Actual vacuum from strong duals](Yin_C_F0070_v1.md#statement) | Target actual derivations and their vacuum identification for the normalized supplied duals. |
| dependency | [Canonical normal comparison](Yin_C_F0075_v1.md#statement) | Part 4 identifies the original closed slices and their bounded-vector and actual adjoint domains. |
| dependency | [Finite-column definition](Yin_C_F0208_v1.md#statement) | The original right cost on normalized finite columns used in the base hypothesis and target conclusion. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T13:25 |
| status | proved |
| reason | Independent review verifies arbitrary free selfadjoint noise over a noncommutative base, the exact vacuum cost and both orientations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Hilbert–Schmidt equivalence with the actual and strong conditions, original domains, both column orientations and the vacuum vectors. |
| argument | [Argument](#argument) | Centered first-noise test, tensor insertion with noncommuting coefficients and operator correction on all bounded vectors. |
| dependency | [Free reference lifting](Yin_C_F0212_v1.md#the-canonical-slices-on-the-base-and-its-free-extensions) | Finite oriented base columns, both bounded-vector domains and their right free-module extension to an arbitrary free factor. |
| dependency | [Bounded drift compression](Yin_C_F0212_v1.md#compression-of-the-commutator-with-a-bounded-drift) | Compression of the old slice commutator to the base conditional-expectation summand. |
| dependency | [One-noise test](Yin_C_F0212_v1.md#the-forced-one-noise-vacuum-component) | Old endpoint pairing and bounded approximation of the drift, using the centered noise with its actual variance here. |
| dependency | [Terminal column estimate](Yin_C_F0265_v1.md#a-global-square-integrable-kernel-estimate-for-mixed-columns) | Last-noise decomposition and simultaneous centered \(C^*(v)\)-coefficient estimate, with noncommutative deletion treated in (5). |
| dependency | [Right free-module structure](Yin_C_F0045_v1.md#3-an-orthogonal-right-module-decomposition-of-the-full-core) | Free prefix orthogonality and the expectation identity for the terminal coefficient columns. |
| dependency | [Finite-family inequality](Yin_C_F0045_v1.md#2-reuse-and-the-remaining-imported-functional-analytic-input) | Hilbert square bound for maps from the abelian noise \(C^*\)-algebra tested on finite coefficient families. |
| dependency | [Actual scalar estimate](Yin_C_F0055_v1.md#statement) | The operator-norm-to-Hilbert estimate for the actual scalar selfadjoint right slice. |
| dependency | [Normal phase and adjoint](Yin_C_F0076_v1.md#statement) | Restriction of original actual old derivatives and passage to the adjoint orientation. |
| dependency | [Canonical domains](Yin_C_F0072_v1.md#statement) | The two original bounded-vector domains from right and reversed contraction estimates. |
| dependency | [Actual vacuum from strong duals](Yin_C_F0070_v1.md#statement) | Target actual derivations and their vacuum identification for the normalized supplied duals. |
| dependency | [Canonical normal comparison](Yin_C_F0075_v1.md#statement) | Part 4 identifies the original closed slices and their bounded-vector and actual adjoint domains. |
| dependency | [Finite-column definition](Yin_C_F0208_v1.md#statement) | The original right cost on normalized finite columns used in the base hypothesis and target conclusion. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0277_v1.md#finding) | All twelve direct interfaces, centered test for necessity, tensor insertion on finite columns, and original-core canonical domains. |

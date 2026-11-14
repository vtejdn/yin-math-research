---
author: Yin
---

# A single freely adjoined normal coordinate detects the original column cost

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\), \(d\ge1\), be a bounded normal generating tuple of a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace.
Assume the [actual starred conjugate-variable condition](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Let \(Y\) be any bounded normal variable whose scalar law has an actual conjugate variable, and take \(W^*(Y)\) freely independent of \(M\).
Write \(Z=(X,Y)\), \(\widehat M=W^*(Z)\), and \(\widehat H=L^2(\widehat M)\) for the tracial free product and its Hilbert space.
For each old index \(i\), put \(E_i=(\mathrm{id}\otimes\tau)\delta_i\) on the original represented algebra \(P=\mathbb C\langle X,X^*\rangle\), and let \(c_i(X)\) be the supremum of \((\sum_j\|E_i p_j\|_2^2)^{1/2}\) over finite columns in \(P\) with \(\|\sum_jp_j^*p_j\|\le1\).
Let \(\beta_i(Z)\) be the infimum of the operator-norm-to-Hilbert norms of linear maps \(T:\widehat M\to\widehat H\) satisfying \([T,L_{Z_j}]a=\delta_{ij}\widehat\tau(a)1\) on all \(\widehat M\), with unrestricted \(T(1)\).
Both costs may be infinite.

The tuple \(Z\) has actual conjugate variables given by those of the two original factors.
Every old index satisfies
\[
              \tfrac14 c_i(X)\le\beta_i(Z)\le c_i(X).                \tag{1}
\]
When \(d=1\), the left bound improves to \(\tfrac{\sqrt\pi}{4}c_1(X)\le\beta_1(Z)\).
The new index satisfies \(\beta_{d+1}(Z)\le(2+\sqrt2)\|\xi_Y\|_2\), where \(\xi_Y\) is the scalar conjugate variable.
All these conclusions apply to the adjoint tuple with its own oriented slices.
In particular,
\[
\begin{aligned}
 \mathsf F(Z)&\ \Longleftrightarrow\ c_i(X)<\infty\quad(1\le i\le d),\\
 \mathsf S(Z)&\ \Longleftrightarrow\
            c_i(X),\,c_i(X^*)<\infty\quad(1\le i\le d).
\end{aligned}                                                        \tag{2}
\]
In the second equivalence the original canonical duals of \(Z\) and their actual Hilbert adjoints contain all bounded vectors in their domains.
In particular a fixed choice such as one free Haar unitary suffices to turn an infinite original column cost into failure of a bare full-domain dual, even when the original \(X\) has several correlated coordinates.

## Argument

### Free extension of a slice

Write \(A=W^*(Y)\) and \(P_A=\mathbb C[Y,Y^*]\).
The centered reduced-word argument for [extension through a free factor](Yin_C_F0205_v1.md#actual-starred-derivations-extend-through-a-free-factor) applies with either factor distinguished.
Extend the coordinate derivation of its own core by zero on the other core and use the outer product rule.
The algebraic free product represents the full starred core by orthogonality of reduced tensors.
For a centered reduced word of length at least two, each differentiated block has a nonempty prefix or suffix whose adjacent letter belongs to the other factor.
Taking the double trace then gives zero, including for completed two-leg derivatives by Hilbert continuity.
The original vacuum pairing with that word vanishes by the same orthogonality, proving the actual adjoint identity.

For a coordinate belonging to either factor, use the [free right-module decomposition](Yin_C_F0208_v1.md#vacuum-preservation-and-the-right-slice-on-reduced-words) with that factor as coefficient algebra \(B\).
Take centered orthonormal bases obtained from word polynomials in both factors, and index \(w\) by the empty word and alternating centered basis words ending in the other factor.
For each free-product polynomial \(p=\sum_w w b_w\) with its finite expansion and \(b_w\) in the core of \(B\), orthogonality over \(B\) and cancellation of all cuts before the last coefficient give
\[
        \sum_w b_w^*b_w=\mathbb E_B(p^*p),\qquad
        \|\widehat E_i p\|_2^2=\sum_w\|E_i^B b_w\|_2^2 .
\]
Here \(E_i^B\) is the slice on the coefficient factor.
Thus its finite column bound controls the single-input norm of the lifted slice by the same constant.
As in the cited decomposition, the actual vacuum gives a closable slice, and operator-norm-controlled polynomial approximation followed by a weak graph limit gives the full bounded-vector extension with the same bound and the coordinate commutators.
This proves the upper bound in (1).
For the new index take \(B=A\).
The [scalar weight estimate](Yin_C_F0267_v1.md#statement) gives a weight of mass \(\|\xi_Y\|_2^2\) and weighted slice norm at most \(2+\sqrt2\).
Summation on scalar columns proves the claimed bound for the new witness.

### Haar unitaries supplied by the old omitted algebra

Assume \(d\ge2\) and fix \(i\).
By [diffuseness of actual normal marginals](Yin_C_F0076_v1.md#statement), both \(A\) and any chosen old omitted marginal \(W^*(X_l)\), \(l\ne i\), contain Haar unitaries.
Indeed each nonatomic Borel probability on a compact plane spectrum has nested equal-mass binary partitions, and the binary coordinate so constructed gives a uniform variable on \([0,1]\).
Exponentiating \(2\pi i\) times this variable gives a Haar unitary.
Select \(u\in A\) and \(v\in W^*(X_l)\) this way, and put \(v_j=u^j v u^{-j}\) for \(j\ge1\).

The conjugate factors \(u^j M u^{-j}\), \(j\ge0\), are freely independent.
Indeed an alternating product of centered elements from consecutively distinct conjugate factors becomes a product of centered elements of \(M\) with nonzero powers of \(u\) between them, after cyclically moving the initial power of \(u\) to the end under the trace.
The last power may be zero, in which case the resulting word still starts and ends with centered \(M\)-letters separated by centered powers of \(u\).
Freeness of \(M,A\) makes both kinds of word centered.
In particular the \(v_j\) are freely independent Haar unitaries jointly free from \(M\), and each belongs to the von Neumann algebra generated by the omitted coordinates of \(Z\).

Suppose \(\beta_i(Z)<\infty\).
The [normal attainment of the single-index optimum](Yin_C_F0201_v2.md#statement) gives an ultraweak-to-weak continuous witness \(T\) of norm \(\beta_i(Z)\).
Normalize it by \(T_0(a)=T(a)-aT(1)\).
Then \(T_0\) has the same commutators, is normal, has norm at most \(2\beta_i(Z)\), and vanishes on \(1\).
The [single-coordinate starred commutator argument](Yin_C_F0208_v1.md#arbitrary-single-coordinate-witnesses) identifies \(T_0p=E_i p\) for \(p\in P\) and gives zero commutators with the adjoints of the omitted generators on all bounded inputs.
For each fixed bounded input \(a\), the maps \(b\mapsto T_0(ba)\) and \(b\mapsto b T_0(a)\) are ultraweak-to-weak continuous in \(b\).
Their equality on the omitted polynomial algebra therefore gives equality on the entire omitted von Neumann algebra.
This step allows Borel \(u,v\), even when these unitaries lie outside the represented polynomial core.

Given a finite old column \(p_1,\ldots,p_m\), write \(Q=\|\sum_jp_j^*p_j\|^{1/2}\) and \(y=\sum_jv_jp_j\).
The [free Haar norm estimate](Yin_C_F0208_v1.md#encoding-finite-columns-by-two-haar-unitaries) gives \(\|y\|\le2Q\).
That estimate uses only the joint freeness of the Haar family and the coefficient algebra, now realized inside \(\widehat M\).
Freeness gives \(\mathbb E_M(v_j^*v_k)=\delta_{jk}1\), so orthogonality also holds when the right coefficients are \(L^2(M)\) vectors, by bounded approximation there.
As \(T_0(v_jp_j)=v_j E_i p_j\), we obtain
\[
        \left(\sum_j\|E_i p_j\|_2^2\right)^{1/2}
            =\|T_0 y\|_2\le 2\beta_i(Z)\|y\|\le4\beta_i(Z)Q .
\]
This proves the lower bound when \(\beta_i(Z)\) is finite, and the extended-real inequality holds trivially when it is infinite.

### The abelian coefficient case and both orientations

When \(d=1\), the scalar weight gives \(c_1(X)<\infty\).
Normalization of an optimal bounded witness and its comparison on the old core as above give \(\|E_1p\|_2\le2\beta_1(Z)\|p\|\).
Extend \(E_1\) by norm continuity to the commutative \(C^*\)-algebra \(C^*(X)\).
The [complex commutative little Grothendieck inequality](../audits/literature/Pis12/Yin_U001.md#pis12-u001) yields \(c_1(X)\le(2/\sqrt\pi)\|E_1\|_{\infty\to2}\le(4/\sqrt\pi)\beta_1(Z)\).

The adjoint marginal has the conjugate vacuum given by the tracial involution, as does each old adjoint coordinate by [adjoint conjugation of derivations](Yin_C_F0073_v1.md#statement).
Freeness persists since the generated von Neumann algebras are unchanged.
Apply the same bounds to \(Z^*=(X^*,Y^*)\).
On normal tuples, finiteness of all full-domain optima is equivalent to the bare condition, including for initially unbounded algebraic witnesses, by the [normal finite-word criterion](Yin_C_F0201_v1.md#statement).
This proves the first equivalence of (2).
The [normal strong-domain comparison](Yin_C_F0075_v1.md#statement) identifies the simultaneous bare conditions on \(Z,Z^*\) with \(\mathsf S(Z)\), and gives the actual bounded-vector domains of the original canonical operators.
The second equivalence follows.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-14T14:26 |
| status | open |
| reason | Fix the quantitative test by one freely added marginal, with the abelian old case and both full-domain equivalences, for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Two-sided old costs, bounded new cost, actual vacua, adjoint orientation and both equivalences for one freely adjoined scalar normal marginal. |
| argument | [Argument](#argument) | Reduced-word lift, conjugate Haar copies in the omitted algebra, normal extension to Borel unitaries, abelian estimate and both orientations. |
| dependency | [Vacuum extension](Yin_C_F0205_v1.md#actual-starred-derivations-extend-through-a-free-factor) | Free extension of each represented derivation and actual vacuum on both factor cores. |
| dependency | [Free slice and Haar estimates](Yin_C_F0208_v1.md#argument) | Right-module lift through a second free factor, full-domain upper bound, free Haar column norm estimate and single-witness starred rigidity. |
| dependency | [Scalar weight](Yin_C_F0267_v1.md#statement) | Quantitative column bound for the new coordinate and finiteness on a sole old scalar factor. |
| dependency | [Marginal laws](Yin_C_F0076_v1.md#statement) | Diffuseness of each actual normal coordinate, providing Haar unitaries in both selected abelian algebras. |
| dependency | [Attained normal optimum](Yin_C_F0201_v2.md#statement) | Normal single-coordinate witness of norm \(\beta_i\) on the full bounded algebra. |
| dependency | [Commutative inequality](../audits/literature/Pis12/Yin_U001.md#pis12-u001) | Complex Hilbert target and squared constant \(4/\pi\) for a bounded map from a commutative \(C^*\)-algebra. |
| dependency | [Adjoint conjugation](Yin_C_F0073_v1.md#statement) | Actual coordinate derivations and vacua for the adjoint tuple. |
| dependency | [Bare finite-word criterion](Yin_C_F0201_v1.md#statement) | Finiteness of all attained bounded-dual optima characterizes bare full-domain systems for normal tuples. |
| dependency | [Canonical strong domains](Yin_C_F0075_v1.md#statement) | Equivalence of both bare orientations with the complete dual condition and canonical compatibility. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-14T14:41 |
| status | proved |
| reason | The independent finding verifies the quantitative single-free-coordinate test and its bare and strong domain conclusions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Two-sided old costs, bounded new cost, actual vacua, adjoint orientation and both equivalences for one freely adjoined scalar normal marginal. |
| argument | [Argument](#argument) | Reduced-word lift, conjugate Haar copies in the omitted algebra, normal extension to Borel unitaries, abelian estimate and both orientations. |
| dependency | [Vacuum extension](Yin_C_F0205_v1.md#actual-starred-derivations-extend-through-a-free-factor) | Free extension of each represented derivation and actual vacuum on both factor cores. |
| dependency | [Free slice and Haar estimates](Yin_C_F0208_v1.md#argument) | Right-module lift through a second free factor, full-domain upper bound, free Haar column norm estimate and single-witness starred rigidity. |
| dependency | [Scalar weight](Yin_C_F0267_v1.md#statement) | Quantitative column bound for the new coordinate and finiteness on a sole old scalar factor. |
| dependency | [Marginal laws](Yin_C_F0076_v1.md#statement) | Diffuseness of each actual normal coordinate, providing Haar unitaries in both selected abelian algebras. |
| dependency | [Attained normal optimum](Yin_C_F0201_v2.md#statement) | Normal single-coordinate witness of norm \(\beta_i\) on the full bounded algebra. |
| dependency | [Commutative inequality](../audits/literature/Pis12/Yin_U001.md#pis12-u001) | Complex Hilbert target and squared constant \(4/\pi\) for a bounded map from a commutative \(C^*\)-algebra. |
| dependency | [Adjoint conjugation](Yin_C_F0073_v1.md#statement) | Actual coordinate derivations and vacua for the adjoint tuple. |
| dependency | [Bare finite-word criterion](Yin_C_F0201_v1.md#statement) | Finiteness of all attained bounded-dual optima characterizes bare full-domain systems for normal tuples. |
| dependency | [Canonical strong domains](Yin_C_F0075_v1.md#statement) | Equivalence of both bare orientations with the complete dual condition and canonical compatibility. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0287_v1.md#finding) | All nine direct inputs, arbitrary scalar marginal, single-coordinate cost and both canonical orientations. |

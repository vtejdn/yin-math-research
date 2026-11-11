---
author: Yin
---
# A probabilistic strategy through amalgamated atom transport

Date: 2026-11-11 (Asia/Hong_Kong).
This bounded strategy discussion for [A0001](../tasks/Yin_T_A0001_v1.md#contract) evaluates the mechanism suggested by the [atomic reformulations](Yin_L_A0012_v1.md).
The main agent and two strategy-development helpers compared mechanisms and checked the elementary obstruction below.
These checks are part of development, not a new independent mathematical review.
The proposal establishes no new Atiyah group class.

## Source of independent information

For an amalgamated product \(G=G_1*_H G_2\), put \(B:=\mathcal N(H)\).
The canonical conditional expectation retains group coefficients in \(H\) and kills the others.
The two vertex group algebras are free with amalgamation over \(B\): an alternating product of elements supported outside \(H\) has zero expectation, by the reduced-word normal form.
This identity extends to their von Neumann closures.
Matrix amplification gives the corresponding \(M_n(B)\)-valued setting.
Thus the relevant probabilistic independence comes from the actual group decomposition, not from treating arbitrary torsion-free group generators as freely independent.

For a selfadjoint affine pencil \(Y=Y_1+Y_2\), with \(Y_j\in M_n(\mathbb CG_j)\), use operator-valued subordination to seek a kernel-trace identity on the vertex sides.
The [BBL21 general-base interface](../audits/literature/BBL21/Yin_U001.md#general-base-algebra-and-the-a0001-strategy-interface) already applies to general von Neumann base algebras when the expected kernel projection has a bounded inverse.
For \(p:=p_{\ker(Y-b)}\), with \(b=b^*\in M_n(B)\), it supplies boundary values \(b_1+b_2=b\) and
\[
\nu_n(Y_1-b_1)+\nu_n(Y_2-b_2)=n+\nu_n(Y-b),
\qquad
\nu_n(T):=(\operatorname{Tr}_n\otimes\tau_G)(p_{\ker T}).
\tag{1}
\]
The source is initially normalized by the matrix tracial state; multiplication by \(n\) gives (1).
Here \(b_j\in M_n(B)\) are actual subordination limits.
Their membership in a smaller algebraically controlled ring is not asserted.

The [existing scalar-free subordination proof](../claims/Yin_C_F0181_v1.md#graded-subordination-proof) demonstrates how the analytic identity and integer support corrections can produce an Atiyah statement.
Its scalar-matrix base and one-variable polynomial reductions are additional structure.
The [SS15 source unit](../audits/literature/SS15/Yin_U001.md#atoms-and-logarithms) independently supplies the known atom lattice for freely independent normal variables at its retained inspection depth.
These established scalar-free cases motivate the question; they do not supply an infinite cyclic amalgamation theorem.

The candidate differs from [S_A0002](../strategies/Yin_S_A0002.md) by targeting subordination boundary values and conditional kernel traces rather than Tor vanishing and universal localization.
It differs from [S_A0004](../strategies/Yin_S_A0004.md) by transferring atoms across a genuine conditional independence structure rather than certifying scalar Schur pivots.
It differs from [S_A0003](../strategies/Yin_S_A0003.md) by working directly in the actual group algebra rather than first constructing integer-rank approximating groups.
It can be selected and tested independently, even when it uses the same cyclic-edge examples as S_A0002.

## Three missing interfaces for a diffuse cyclic base

For \(H\cong\mathbb Z\), the algebra \(B\cong L^\infty(\mathbb T)\) is diffuse.
The following obligations are separate.

1. A nonzero expected kernel need not have a bounded inverse, even after restricting to its support.
   A usable extension or a justified reduction must handle this degeneracy.
2. A support projection in \(M_n(B)\) need not have integer unnormalized trace.
   Any support-cut corrections must be controlled in total, rather than assumed individually integral.
3. A boundary value \(b_j\in M_n(B)\) need not belong to \(\mathbb CG_j\) or its controlled actual rational closure.
   The vertex group's Atiyah property therefore does not automatically apply to \(Y_j-b_j\).

A sufficient route would reduce the two vertex nullities to known integer ranks and control the total correction by an integer.
Then (1), followed by the existing all-size affine-linear equivalence, would give the Atiyah property for the selected amalgam.
Possible stronger sufficient conditions include constant almost-everywhere fiber ranks for the cut projections and boundary coefficients in controlled cyclic or vertex rational rings.
Neither condition is currently proved, and they are not declared necessary.
An exact trace cancellation or another kernel-preserving algebraic reduction could replace them.

For arbitrary diffuse-base coefficients the intended integrality statement is false: if \(e=1_E\in B\) has \(0<\tau(e)<1\), the scalar operator \(e\) has kernel trace \(1-\tau(e)\).
Likewise, adding an arbitrary base coefficient to the zero group-ring element already produces this example.
This does not refute the conjecture or a constrained subordination mechanism; it rules out discarding the group-ring origin of the inputs and the special constraints on the actual boundary values.

## Full support does not supply a bounded inverse, even for a group-ring matrix

Let \(G=\mathbb Z^2\), let \(u,v\) be its commuting canonical group unitaries, and let \(B:=W^*(u)\).
The expectation \(E_B\) integrates out the \(v\) coordinate.
Set
\[
s:=u-1,\qquad
T:=\begin{pmatrix}s&v\\0&0\end{pmatrix},
\qquad
w:=\begin{pmatrix}v\\-s\end{pmatrix}.
\]
Since \(v\) is a unit and commutes with \(s\), the column \(w\) parametrizes the kernel of \(T\).
Moreover \(w^*w=1+|s|^2\), so
\[
p_{\ker T}
=\frac1{1+|s|^2}
\begin{pmatrix}
1&-vs^*\\
-sv^*&|s|^2
\end{pmatrix},
\qquad
E_B^{(2)}(p_{\ker T})
=
\begin{pmatrix}
(1+|s|^2)^{-1}&0\\
0&|s|^2(1+|s|^2)^{-1}
\end{pmatrix}.
\tag{2}
\]
The projection has unnormalized trace one, so there is no fractional kernel defect.
The expectation in (2) has full support because \(u-1\) vanishes only at a Haar-null point.
Its second diagonal entry approaches zero on sets of positive measure near that point.
It consequently has no bounded inverse and has nonclosed range.

The selfadjoint group-ring pencil
\[
K_T:=\begin{pmatrix}-I_2&T\\T^*&0\end{pmatrix}
\]
has kernel \(\{0\}\oplus\ker T\).
Restricting its expected kernel projection to its support retains the same obstruction.
The example can also be placed in one vertex of
\(\mathbb Z^2*_{\mathbb Z}\mathbb Z^2\), with the amalgamated subgroup generated by \(u\).
It is already an obstruction to the automatic expected-kernel hypothesis, without involving a difficult unknown Atiyah group.

This calculation refutes the universal step from full support to a bounded inverse.
It does not refute every multi-step repair: for this triangular \(T\), a later left-kernel support cut can erase the sole nonzero row and produce a zero matrix with an integer correction.
A further investigation must track both cuts, coefficient membership, and their total trace effect.

## Two other probability suggestions screened out at their immediate interfaces

Adding diffuse noise and then removing it does not by itself preserve atomlessness.
If \(X\) has a diffuse bounded selfadjoint law, each \(\varepsilon X\), for \(\varepsilon>0\), is diffuse, while its law converges weakly to \(\delta_0\).
A smoothing approach needs actual uniform control near the prospective atom.
Weak convergence or atomlessness at each positive noise level supplies none.

A scalar phase twist preserving all group relations is a character \(\chi:G\to\mathbb T\).
The unitary \(D_\chi\delta_g:=\chi(g)\delta_g\) satisfies
\[
D_\chi\lambda_G(h)D_\chi^*=\chi(h)\lambda_G(h).
\]
Consequently this twist preserves every matrix spectral law.
Independent phases violating the relations change the model.
Character methods may still expose a grading, but this belongs near the existing character-based mechanisms rather than supplying automatic spectral smoothing.

## Next discriminating investigation and scope

The first investigation should seek an atom-transfer or reduction identity that survives the degeneration in (2), and test it on a genuinely two-vertex group-ring pencil.
Compute the actual cut projections, whether the reduced expected kernel has a bounded inverse, and the total trace correction.
Then test whether the subordination boundary terms admit a reduction to controlled vertex coefficients or vertex kernel traces.
A general theorem for diffuse base algebras is not the missing first input; the applicability and algebraic restrictions are.

If a proposed repair uses truncations, account explicitly for the new compression kernels and limiting errors.
Small trace errors alone cannot be rounded to integers unless an independent discrete constraint has been established.
No estimate or boundary-coefficient statement may assume the target group already has the Atiyah property.

A successful cyclic-amalgamation theorem would be a permanence result for the demonstrated class.
It would not resolve A0001 for all torsion-free groups without another verified construction or reduction.
Known cases are suitable calibrations, but new coverage requires an actual comparison with existing theorems.
The independent strategy is therefore a proposed analytic mechanism with concrete obstructions and a bounded first test, not a completed method or a claimed general proof.

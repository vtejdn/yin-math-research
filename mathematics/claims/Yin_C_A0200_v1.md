---
author: Yin
---

# Two reflections in a quotient and the regular rank on four group elements

## Statement

Let \(H=\langle s,t\rangle\) be a discrete group and
\[
 K=B+At-s(D+Ct),\qquad
 {\cal P}=\begin{pmatrix}B&A\\D&C\end{pmatrix}\in{\rm GL}_4(\mathbb C)
\]
with complex two-by-two blocks.
Write \(\delta=\dim_H\ker K\), using the regular group trace and the unnormalized matrix trace.
Suppose the images of \(s,t\) in a quotient are reflections generating the dihedral group with a rotation of order \(m\ge2\).
Then \(\delta\le 2/m\).
If every nonzero scalar of \(\mathbb C H\) acts injectively and \(0<\delta<1\), then
\[
                                 \delta\le 1/m .
\]
For a quotient onto the infinite dihedral group taking the two labels to reflections, \(K\) has rank two even without scalar injectivity.

In particular for a torsion-free marked pair satisfying scalar injectivity, any such finite dihedral quotient with \(m\ge3\) excludes a half constant-column increment for the [four-column list with two copies of each label](Yin_C_A0184_v1.md#statement).
Every rectangle of noninteger rank automatically has the indicated invertible block matrix there.
In the infinite dihedral case all ranks in that four-column pencil family are integers under the scalar hypothesis.
The quotient can be tested in the marked subgroup even when the ambient group has other generators.

## The degree-one pencil from two reflections

For each \(z\) on the unit circle with \(z^m=1\), send the two generating reflections to the unitary matrices
\[
 J_0=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 J_z=\begin{pmatrix}0&z^{-1}\\z&0\end{pmatrix}.
\]
Their product is diagonal with entries \(z,z^{-1}\), so the presentation of the dihedral group supplies a representation of \(H\).
For an infinite dihedral quotient every \(z\) on the circle is allowed.
Twisting regular translations by any actual unitary representation of dimension two multiplies matrix nullities by two.
Indeed on the fiber over \(h\in H\) use the unitary \(\rho(h)\) to conjugate ordinary left translation tensored with the identity to \(g\mapsto\lambda(g)\otimes\rho(g)\).
The unitary is the identity on the fiber over the identity group element, where the regular matrix trace is evaluated.

Order the two representation coordinates as blocks and multiply the second input block by \(z\).
The twisted rectangle becomes
\[
 E_0+zE_1,\qquad
 E_0=\begin{pmatrix}B&At\\-sD&-sCt\end{pmatrix},\qquad
 E_1=\begin{pmatrix}-sCt&-sD\\At&B\end{pmatrix}.
\]
In particular \(E_0={\rm diag}(I_2,-s I_2){\cal P}\,{\rm diag}(I_2,t I_2)\) and \(E_1=J E_0 J\), where \(J\) swaps the two two-coordinate blocks.
Both are invertible over \(\mathbb C H\).
The unit \(T=-E_1^{-1}E_0\) therefore has group-ring entries together with its inverse, and \(JTJ=T^{-1}\).
At each allowed phase the right eigenspace \(\ker(T-zI_4)\) has dimension \(2\delta\).
Distinct scalar eigenspaces form an algebraically direct sum by interpolation, inside a module of dimension four.
This gives \(2m\delta\le4\) in the finite case and \(\delta=0\) in the infinite case.

## The action of the block swap on the remaining image

Assume scalar injectivity and \(0<\delta<1\).
At phase one, diagonalizing \(J_0\) by a constant matrix splits the pencil into \(K\) and its twist by the one-dimensional character sending both \(s,t\) to \(-1\).
Each of these has nullity \(\delta\) and cannot kill a nonzero column over \(\mathbb C H\).
Indeed one nonzero group-ring coordinate of such a column has trivial regular kernel, so the column generates an affiliated right module of dimension one.
It follows that \(\ker(T-I_4)\) has positive dimension and contains no nonzero group-ring vector.

Consequently no nonzero complex polynomial annihilates \(T\).
To see this, factor an annihilating polynomial into a power of \(X-1\) and a coprime factor.
Polynomial interpolation gives an idempotent in the group-ring matrix algebra whose image is the primary module at \(1\); this image is nonzero since there is a nonzero fixed vector.
Taking the highest power of \(T-I_4\) still nonzero on that idempotent gives a nonzero group-ring matrix with image in the fixed space.
One of its columns contradicts the conclusion at phase one.

Let \(W\) be the affiliated image of \(T^m-I_4\).
Since \(X^m-1\) has simple roots, its kernel is the direct sum of the \(m\) eigenspaces and
\[
                         \dim_H W=4-2m\delta .
\]
The invertible \(T\) preserves \(W\) in both directions.
So does \(J\), since \(J(T^m-I_4)J=-T^{-m}(T^m-I_4)\).
The two \(J\)-eigenspaces in \(W\) are the affiliated images of the group-ring matrices
\(\frac12(I_4\pm J)(T^m-I_4)\).
Each nonzero such image has dimension at least one by applying scalar injectivity to a nonzero matrix entry.
If \(\dim_H W<2\), at least one eigenspace must be zero.
Thus \(J\) acts on \(W\) as a scalar sign, including vacuously when \(W=0\).
The relation \(JTJ=T^{-1}\) now implies \(T^2=I_4\) on \(W\), giving
\[
                            (T^2-I_4)(T^m-I_4)=0 .
\]
This is the forbidden polynomial identity.
Hence \(\dim_H W\ge2\), which proves the stronger bound.
The proof uses both the ordinary group-ring entries and the two reflections; the mere existence of a cyclic group of comparable order gives a different estimate.

## A marking with finite abelianization and an infinite dihedral quotient

Take
\[
 H=\langle s,t\mid s t^2 s^{-1}=t^{-2},\
                     t s^2 t^{-1}=s^{-2}\rangle .
\]
In the amalgam of the Klein bottle groups \(\langle s,y\mid sys^{-1}=y^{-1}\rangle\) and \(\langle t,v\mid tvt^{-1}=v^{-1}\rangle\), identify \(y=t^2,\ v=s^2\).
The identified subgroups \(\langle s^2,y\rangle\) and \(\langle v,t^2\rangle\) are free abelian of rank two in the vertex semidirect products, and eliminating \(y,v\) gives exactly the presentation above.
Amalgam normal form gives torsion-freeness since a cyclically reduced word of length at least two retains positive length in every positive power and each vertex is torsion-free.
The abelianization is \(C_4\oplus C_4\), so there is no nonzero integer character.
Setting both generator squares equal to one gives \(C_2*C_2\), the infinite dihedral group, and the marked generators become its two reflections.
Thus every rectangle with the stated invertible \({\cal P}\) has full regular rank by the degree-one pencil.
The common edge is normal, with that same infinite dihedral quotient, so this example is elementary amenable and is already in the [known torsion-free class](../audits/literature/Lin00/Yin_U004.md#the-division-ring-and-free-field-assertions-are-separate).
Its role is to distinguish the marked nonabelian quotient test from an integer or large finite abelian character test.

## Assessment history

### Decision dihedral-quotients

| Field | Value |
| --- | --- |
| date | 2026-11-26T05:48 |
| status | proved |
| reason | The independent whole-proof inspection verified the result with its stated assumptions and limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Dihedral rotation order and finite or infinite phase bounds. |
| argument | [The degree-one pencil from two reflections](#the-degree-one-pencil-from-two-reflections) | The actual representations and both group-ring units. |
| argument | [The action of the block swap on the remaining image](#the-action-of-the-block-swap-on-the-remaining-image) | Reversal, finite columns, algebraic eigenvalues and the improved bound. |
| argument | [A marking with finite abelianization and an infinite dihedral quotient](#a-marking-with-finite-abelianization-and-an-infinite-dihedral-quotient) | The Klein bottle amalgam and the earlier group-class result. |
| review | [Dihedral quotients](../audits/reviews/Yin_R_A0184_v1.md#dihedral-quotients) | Independent inspection of the full statement and proof. |

## Current assessment

[Selected decision](#decision-dihedral-quotients)

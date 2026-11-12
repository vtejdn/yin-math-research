---
author: Yin
---
# Dimension-flat induction from the division closure in the amenable case

## Statement

Let \(R=K[G]\) for a discrete group \(G\) and a conjugation-closed field \(K\subseteq\mathbb C\).
Let \(N=\mathcal N(G)\), \(U=\mathcal U(G)\) in the regular representation, and \(D\) be the division closure of \(R\) in \(U\), formed by inverses of scalars that are units in \(U\).
Use right modules, matrices acting on columns from the left, and the unnormalized matrix extension of the canonical trace.
Write \(F(X)=X\otimes_D U\) and use the extended scalar dimension \(\dim_U\), including on modules that have no finite presentation.

1. For amenable \(G\), every injection of right \(D\)-modules induces under \(F\) a map with kernel of scalar dimension zero.
2. Suppose that the same zero-defect property holds on short exact sequences of finitely generated right \(D\)-modules and that \(\operatorname{lcm}(G)<\infty\).
   If the finite-subgroup induction map in KLS17 Theorem 3.7(3) surjects onto \(G_0(D)\), the center-valued Atiyah conjecture over \(K\) follows.
   In particular this proves the implication under amenability, conditional on (3) and without an Artinian assumption.
3. The zero-defect property in item 2 is equivalent to the following concrete matrix condition for every finite rectangular matrix \(B\) over \(D\),
   \[
     \dim_U\!\left(\ker B_U/(\ker B_D)U\right)=0 .
   \]
   The denominator denotes the \(U\)-span of the actual algebraic kernel vectors inside the ambient free module.

## Argument

### Comparing the balanced tensor products

For any right \(D\)-module \(X\), the natural surjection \(X\otimes_R U\to X\otimes_D U\) is an isomorphism.
In \(X\otimes_R U\), consider the elements \(d\in D\) for which \(xd\otimes u=x\otimes du\) for every \(x,u\).
They form a subring containing \(R\).
If it contains \(d\in D\cap U^\times\), then \(d^{-1}\in D\) by definition, and balancing at \(xd^{-1}\) and \(d^{-1}u\) gives \(x\otimes d^{-1}u=xd^{-1}\otimes u\).
Thus this subring is division closed in \(U\) and equals \(D\) by minimality.
All additional balancing relations already hold, and the identification is natural in \(X\).
This proves an identity of ordinary tensor functors on \(D\)-modules without identifying derived tensor products over the two base rings.

### Amenable induction

Restrict a short exact sequence of right \(D\)-modules to \(R\).
Extension to \(\mathbb C[G]\) is exact since it is scalar extension over the field \(K\).
Lück's Theorem 6.37 gives scalar \(N\)-dimension zero for the first Tor of every \(\mathbb C[G]\)-module when \(G\) is amenable.
Its right-module form follows by the involution, which preserves the trace.
The long exact Tor sequence places the kernel of the induced left-hand map in the image of that first Tor, so its scalar dimension is zero.
Extension from \(N\) to \(U\) is flat and preserves dimension by Theorems 8.22(2) and 8.29.
Associativity and the balanced comparison identify the resulting sequence with the sequence after applying \(F\), proving item 1 even for modules infinitely generated on restriction to \(R\).
The three cited statements were checked in the [retained Luc02 book manuscript](../audits/literature/Luc02/readme.md#yin-edition) and are used as external inputs.

### Applying an exact-sequence class relation

For a short exact sequence \(0\to X'\xrightarrow{i} X\to X''\to0\) put \(E_i=\ker F(i)\).
The long exact Tor sequence identifies \(E_i\) with the image of the connecting map \(\operatorname{Tor}_1^D(X'',U)\to F(X')\).
For every central projection \(z\in N\), use \(d_z(X)=\dim_U(F(X)z)\), with the original trace and no normalization by \(\tau(z)\).
Multiplication by \(z\) is a direct summand functor on \(U\)-modules and hence exact.
For finitely generated \(D\)-modules all three \(d_z\) values are finite, and additivity over \(U\) gives
\[
 d_z(X)=d_z(X')+d_z(X'')-\dim_U(E_i z).
\]
A zero scalar defect implies \(\dim_U(E_i z)=0\) for every \(z\), since \(E_i z\) is a submodule of \(E_i\).
Thus, under item 2's hypothesis, each \(d_z\) induces a homomorphism \(G_0(D)\to\mathbb R\).
This uses the short exact sequences of all finitely generated modules allowed in \(G_0(D)\), including any non-finitely-presented modules occurring in a class relation.

For \(A:R^l\to R^n\), put \(X=\operatorname{coker} A_D\).
Condition (3) supplies a single finite signed expression \([X]=\sum_j a_j[P_j\otimes_{K[H_j]}D]\), with \(H_j\le G\) finite and \(P_j\) finitely generated projective over \(K[H_j]\).
Maschke's theorem ensures that induction on this source respects exact-sequence relations.
The same expression works for every central projection \(z\).
The module \(F(X)=\operatorname{coker}A_U\) is finitely presented and hence projective over the von Neumann regular ring \(U\), and the induced \(P_j\) are projective over \(U\).
For a finitely generated projective \(U\)-module \(P\), one has \(\dim_U(Pz)=\tau(z\,\dim_G^u P)\) by the projection formula for the center-valued trace.
Consequently
\[
 \tau\!\left(z\left[\dim_G^u\operatorname{coker} A_U-
        \sum_j a_j\dim_G^u(P_j\otimes_{K[H_j]} U)\right]\right)=0
 \qquad(z\text{ any central projection}).
\]
The central self-adjoint difference vanishes by taking its positive and negative spectral supports and using faithfulness of the trace.
Each finite-subgroup term belongs to the trace lattice \(L_K(G)\) by finite semisimple decomposition.
Finally \(\dim_G^u\ker A_U=(l-n)1+\dim_G^u\operatorname{coker}A_U\), and \(1\) lies in the lattice.
This proves item 2 without assigning a stable isomorphism to a \(G_0\) class.

### Matrix test for the left-hand defect

Given \(B:D^b\to D^c\), put \(J=\operatorname{im}B_D\) and \(Y=D^c/J\).
Right exactness gives \(J\otimes_D U=U^b/(\ker B_D)U\).
The long exact sequence for \(0\to J\to D^c\to Y\to0\) therefore gives
\[
 \operatorname{Tor}_1^D(Y,U)
 \ \cong\ \ker\bigl(J\otimes_D U\to U^c\bigr)
 \ \cong\ \ker B_U/(\ker B_D)U .
\]
The first isomorphism uses freeness of \(D^c\), with no projectivity premise on \(J\).
All three original terms are finitely generated, so zero defect on the indicated short exact sequences implies the matrix test.
Conversely the test makes first Tor have dimension zero on every finitely presented module.
Each module is a filtered colimit of finitely presented modules, and first Tor commutes with filtered colimits, as seen by taking a fixed free resolution of the left coefficient module and using exactness of filtered colimits on underlying abelian groups.
The natural right \(U\)-actions are preserved in the resulting Tor isomorphism.
Dimension-zero modules are closed under filtered colimits because their images have dimension zero and their directed union has dimension zero by cofinality.
The connecting-map description now gives zero defect for every short exact sequence, proving item 3.

## Scope for the torsion-free problem

For torsion-free amenable \(G\) and \(K=\mathbb C\), the scalar map \(d_1:G_0(D)\to\mathbb R\) sends \([D]\) to one.
For any \(0\ne a\in D\), an individual relation \([D/aD]\in\mathbb Z[D]\) therefore makes the scalar dimension of \(\operatorname{coker}a_U\) integral.
It is strictly smaller than one by faithfulness and equals the square operator's kernel dimension, so it vanishes and \(a\) is a unit of \(U\), with inverse in \(D\).
Conversely a unit has \(D/aD=0\), so for each such \(a\) the condition \([D/aD]\in\mathbb Z[D]\) is equivalent both to \([D/aD]=0\) and to invertibility.
If its right annihilator \(I_a\) is finitely generated over \(D\), the two short exact sequences with middle terms \(D\), quotients \(aD\) and \(D/aD\), and kernels \(I_a\) and \(aD\), respectively, give \([D/aD]=[I_a]\).
A singular nonzero \(a\) would give a nonzero class in \(G_0(D)/\mathbb Z[D]\), so finite generation alone leaves a specific class to determine.
Neither existence of the indicated class relations for arbitrary amenable groups nor the zero-defect property for arbitrary groups follows from this argument.
The [KLS17 source audit](../audits/literature/KLS17/Yin_U001.md#why-condition-3-has-not-been-cleared) records the general proof gap and the scope of the test example.

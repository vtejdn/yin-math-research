---
author: Yin
---

# Finitely supported kernel generators for the unrestricted commutator criterion

The [A0003 deletion question](../tasks/Yin_T_A0003_v3.md#contract) asks whether the finite-rank equation alone detects the division closure \(D_G\) of \(A=\mathbb CG\) in \(U=L^0(\mathcal N(G))\).
Write \(H=\ell^2(G)\).
The [bordered-pencil reduction](Yin_L_A0074_v1.md#one-diagonal-coefficient-of-a-bordered-pencil) tests one diagonal entry in the kernel projection of each bounded pencil \(B=\left(\begin{smallmatrix}L&\beta\\ \alpha&0\end{smallmatrix}\right)\), with \(L\) injective and \(\alpha,\beta\) constant.
On 2026-11-25 a delegated researcher for Yin examined whether finitely supported solutions of \(Bv=0\) recover this entry.

## A finite set of kernel generators after Hilbert space closure

Let \(B\in M_{m,n}(A)\).
Suppose \(C\in M_{n,r}(A)\) satisfies \(BC=0\) and \(\overline{\operatorname{ran}_{H^r}C}=\ker_{H^n}B\), allowing linear dependence among the columns of \(C\) over the affiliated algebra.
Then
\[
       p_{\ker B}=CC^*(B^*B+CC^*)^{-1}\ \in M_n(D_G).
\]
Indeed the two positive summands act on orthogonal subspaces since \(BC=0\).
Their kernels intersect trivially because \(\ker C^*=(\ker B)^\perp\).
Thus their sum is an injective square matrix over \(A\), and its affiliated inverse has entries in \(D_G\) by [successive Gram pivots](../claims/Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations).
On \(\ker B\) the sum equals \(CC^*\), and on \((\ker B)^\perp\) the operator \(CC^*\) vanishes.
The displayed product is therefore the orthogonal projection onto \(\ker B\), including when either summand has nonclosed range.
For \(\ker B=0\) one may take the zero column.

In the [amenable domain case](../claims/Yin_C_A0001_v2.md#finite-scalar-descent-and-a-complete-conditional-kernel-witness) one can choose \(C\) injective.
The formula above allows redundant kernel generators and places no integrality requirement on the von Neumann dimension of \(\ker B\).
It suffices for complete deletion to obtain such a matrix \(C\) for each bordered pencil in the reduction.

## Amenable groups with a right coherent complex group algebra

For finitely generated amenable \(G\), the finitely supported solutions of \(Bv=0\) are dense in its Hilbert space kernel.
Indeed, take any finite \(S\subset G\) containing the identity and the supports of the entries of \(B\), and any nonempty finite \(F\subset G\).
If \(W\) is the closed span of the finitely supported solutions, the [finite-propagation trace bound](../claims/Yin_C_A0119_v1.md#exact-solutions-supported-on-finitely-many-cosets), applied with trivial subgroup, gives
\[
0\leq \dim_G\ker B-\dim_G W
  \leq m\sum_{s\in S}\frac{|sF\mathbin{\triangle}F|}{|F|}.
\]
Right translates of each finitely supported solution are again such solutions.
Along a Følner sequence the right side tends to zero, and faithfulness of the trace gives \(W=\ker B\).
This is also the group-ring instance of [complete amenable kernel localization](../claims/Yin_C_A0001_v2.md#rational-kernel-localization).

If \(A\) is right coherent, the kernel of every right \(A\)-module map \(B:A^n\to A^m\) is finitely generated.
Taking generators as the columns of \(C\) gives \(C A^r=\ker(B:A^n\to A^m)\).
The preceding density result and \(BC=0\) then give \(\overline{\operatorname{ran}_{H^r}C}=\ker_{H^n} B\).
The projection formula applies to every group-ring matrix, hence in particular to the bordered pencils.
Consequently equation (1) alone detects \(D_G\) for finitely generated amenable groups with right coherent \(\mathbb CG\), including the torsion-free members of this class.
The same proof only needs finite generation of the algebraic kernel for each bordered pencil under consideration.
Its use of coherence ends at the first kernel.

## A bordered pencil over a free group without a finitely supported kernel vector

Take \(G=F(a,b)\) with its free basis and identify the generators with left translations.
Let
\[
 L=\operatorname{diag}(a-1,b-1,b-1),\qquad
 \beta=(1,1,1)^{\mathsf T},\qquad \alpha=(0,1,-1),\qquad
 B=\begin{pmatrix}L&\beta\\ \alpha&0\end{pmatrix}.
\]
The shifts \(a\) and \(b\) have infinite order, so each difference from the identity is injective on \(H\) by restriction to its infinite cyclic orbits.
In \(U^3\) the column \(k=L^{-1}\beta\) has identical second and third coordinates, so \(\alpha k=0\).
The [bordered elimination and compression formula](Yin_L_A0074_v1.md#one-diagonal-coefficient-of-a-bordered-pencil) gives \(\dim_G\ker B=1\) and last diagonal coefficient \((1+k^*k)^{-1}\in D_G\).

A vector \((y_1,y_2,y_3,z)^{\mathsf T}\) in the group-ring kernel satisfies
\[
 (a-1)y_1=(b-1)y_2=(b-1)y_3=-z .
\]
The first equality says that the finite edge chain with \(a\)-edge coefficients \(y_1\) and \(b\)-edge coefficients \(-y_2\) has zero boundary in the left Cayley tree.
Leaf removal in its finite support gives \(y_1=y_2=0\), as in the [free-tree boundary calculation](Yin_L_A0023_v2.md#the-mixed-shear-before-linearization).
Then \(z=0\) and injectivity of \(b-1\) forces \(y_3=0\).
Thus \(\ker(B:A^4\to A^4)=0\) even though this admissible pencil has positive von Neumann kernel dimension and its required coefficient belongs to \(D_G\).
Finite generation after Hilbert space closure by group-ring kernel vectors is therefore a sufficient test that can fail for these pencils in a torsion-free group where deletion holds.

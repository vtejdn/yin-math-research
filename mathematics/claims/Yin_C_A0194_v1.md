---
author: Yin
---

# Two generator spectra and a family of torsion-free perfect groups

## Statement

Let \(H=\langle s,t\rangle\) be discrete, and let \(A,B,C,D\) be complex \(h\)-by-\(h\) matrices such that
\[
 {\cal P}=\begin{pmatrix}B&A\\ D&C\end{pmatrix}\in{\rm GL}_{2h}(\mathbb C).
\]
Write \(\delta=\dim_H\ker(B+At-s(D+Ct))\) for regular nullity with unnormalized coordinate trace.
Fix two distinct unit scalars for each marked generator.
Write the two pairs as \(a+b,a-b\) and \(c+d,c-d\), with \(bd\ne0\).
Among the two-dimensional unitary representations of \(H\) having precisely those spectra on \(s,t\), let \(\mathcal T\) be the set of distinct ordinary traces of the product \(\rho(s)\rho(t)\).
For each trace value count two if it is of the form \(2ac+bd(z+z^{-1})\) with \(z\) on the unit circle different from \(1,-1\), and one for either endpoint \(z=1,-1\).
Every trace in \(\mathcal T\) has this form.
If the resulting number \(k\) is positive and finite, then
\[
                             \delta\le h/k .
\]
If nonzero group-ring scalars are regularly injective, then \(0<\delta<1\) further implies \(\delta\le(h-1)/k\).
Infinitely many traces imply \(\delta=0\) at every size \(h\).
For example, a marked quotient onto the free product of two nontrivial cyclic groups, with the two labels mapping to the two cyclic generators, gives this full rank at every size.
The hypotheses apply to the marked subgroup even in an arbitrary overgroup.

There are two-generator torsion-free perfect groups for which this test excludes half rank using no character or scalar injectivity.
For each \(n\ge0\) the marked group constructed below has at least \(8(n+1)\) phases with the same prescribed generator spectra.
Every rectangle with the displayed block condition on that group has
\[
                        \delta\le\frac{h}{8(n+1)} .
\]
For \(n=2\), a two-by-two rectangle in this family has nullity at most \(1/12\).
Under scalar injectivity the [four-column reduction](Yin_C_A0184_v1.md#statement) then excludes every half increment on the two-label list, including its coefficient-degenerate cases.
The estimate concerns the indicated matrices and does not establish an all-matrix Atiyah theorem for perfect groups.

## Normal form for a pair of unitary matrices

Put
\[
 J_0=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 J_z=\begin{pmatrix}0&z^{-1}\\z&0\end{pmatrix}.
\]
In any of the representations under consideration \(U=(\rho(s)-aI)/b\) and \(V=(\rho(t)-cI)/d\) are selfadjoint unitary involutions with trace zero.
The unitary \(UV\) has determinant one, and \(U\) carries it to its inverse by conjugation.
When the two eigenvalues \(z,z^{-1}\) are distinct, choose a unit eigenvector for \(z\) and its image under \(U\) for the other coordinate.
In this orthonormal basis \(U=J_0,\ V=J_z\); interchanging the coordinates realizes \(z^{-1}\) as well.
When \(UV=\pm I\), take any unitary basis in which \(U=J_0\), giving \(V=\pm J_0\).
Thus the product trace is \(2ac+bd(z+z^{-1})\), and different unordered phase pairs give different traces.

For a representation at an allowed \(z\) the twist of the rectangle by
\(S=aI+bJ_0,\ T_z=cI+dJ_z\) has nullity \(2\delta\) by [unitary absorption](Yin_C_A0200_v1.md#the-degree-one-pencil-from-two-reflections).
Multiplying its second input block by \(z\) gives \(E_0+zE_1\) with
\[
 E_0=\begin{pmatrix}
        B+cAt-a s(D+cCt)& dAt-ad\,sCt\\
        -b s(D+cCt)&-bd\,sCt
      \end{pmatrix},
 \qquad E_1=J E_0 J ,
\]
where \(J\) interchanges the two \(h\)-coordinate blocks.
The equality for \(E_1\) also follows by conjugating the unscaled twisted rectangle by \(J\), which exchanges \(z\) and \(z^{-1}\).
Subtract \(a/b\) times the second block row from the first, then \(c/d\) times the second block column from the first.
The result is \({\rm diag}(I_h,-b s I_h){\cal P}\,{\rm diag}(I_h,d t I_h)\).
Thus both coefficients are invertible over \(\mathbb C H\).

The group-ring unit \(L=-E_1^{-1}E_0\) has \(JLJ=L^{-1}\).
The distinct phase eigenspaces each have dimension \(2\delta\) and form an algebraically direct sum in dimension \(2h\), giving the first bound and the infinite case.
For the sharper bound suppose \(0<\delta<1\) and scalar injectivity holds.
A finite-support vector in any twisted kernel untwists to a finite-support vector in the direct sum of two copies of the original kernel.
Indeed the unitary in the absorption proof acts separately at each group element, preserving finite support in both directions.
Each copy has no nonzero finite-support vector, since one nonzero group-ring coordinate would make its generated module have dimension one.
Hence \(L\) has no nonzero scalar polynomial annihilator by the primary-idempotent argument at any allowed phase in the [block-swap proof](Yin_C_A0200_v1.md#the-action-of-the-block-swap-on-the-remaining-image).

Let \(p(X)\) be the monic polynomial of the \(k\) allowed phases, each included once.
Reciprocity of the phase set gives \(p(L^{-1})=\gamma L^{-k}p(L)\) for a nonzero complex scalar \(\gamma\).
The image of \(p(L)\) is therefore invariant under \(J\), \(L\) and \(L^{-1}\).
It has dimension \(2h-2k\delta\).
Its two parts cut out by \((I\pm J)/2\) are images of group-ring matrices and each nonzero one has dimension at least one.
If their total dimension were below two, \(J\) would act by a scalar sign on the whole image.
The reversal identity would give \((L^2-I)p(L)=0\), a contradiction.
This proves the sharper bound.
For the free product example choose two allowed distinct roots of unity for each finite cyclic generator, or any two distinct phases for an infinite cyclic generator.
The presentation permits all pairs \(S,T_z\) with these spectra and arbitrary \(z\) on the circle.

## An explicit perfect marking

Set \(r=12n+11\), \(d_0=r-6\).
Use the full inverse image \(\Gamma_r\) of the orientation-preserving hyperbolic triangle group of orders \(2,3,r\) in the universal covering group of \({\rm PSL}_2(\mathbb R)\).
The [lifted triangle presentation](../audits/literature/Mil75/Yin_U001.md#lifted-triangle-presentation) is
\[
             X^2=Y^3=Z^r=XYZ=c_0
\]
with \(c_0\) central of infinite order.
The covering group acts faithfully by lifts of the boundary-circle action to the real line: the deck group acts by integer translations, with the fundamental rotation loop lifting to a single translation.
An increasing homeomorphism of the line of finite order is the identity, so \(\Gamma_r\) is torsion-free.
Define the subgroup \(H_r\) generated by
\[
                s=Xc_0^{(d_0-1)/2},\qquad t=Yc_0^{(-d_0-1)/3}.
\]
Both displayed exponents are even integers.
Put \(u=c_0^{d_0}=s^2\) and \(w=u(st)^{-1}\) in \(H_r\).
A direct use of the presentation gives
\[
             s^2=u,\qquad t^3=u^{-1},\qquad stw=u,\qquad
             w^r=u^{(5r-1)/6}.
\]
For the last identity one has \(w=Zc_0^{(5d_0-1)/6}\), whose \(r\)-th power is \(c_0^{d_0(5r-1)/6}\).
In the abelianization these relations eliminate \(u,w\) and give two rows \((2,3)\) and \((r-2e,-r)\) on \(s,t\), where \(e=(5r-1)/6\).
Their determinant is \(6e-5r=-1\).
Since \(s,t\) generate, \(H_r\) is perfect.
It is infinite because \(u\) has infinite order.

## Counting unitary representations

For a phase \(z\) take
\[
      S=iJ_0,\qquad T_z=\tfrac12 I+i\tfrac{\sqrt3}{2}J_z .
\]
Both have determinant one, \(S^2=T_z^3=-I\), and their product has trace \(-\sqrt3\cos(\arg z)\).
For every integer \(j\) in \(r/12<j<5r/12\) there are two distinct phases with this trace equal to \(2\cos(2\pi j/r)\).
The trace values for these \(j\) are distinct, and \((ST_z)^r=I\) by the unitary two-dimensional spectral theorem.
The assignments
\[
       X\mapsto S,\quad Y\mapsto T_z,\quad
       Z\mapsto-(ST_z)^{-1},\quad c_0\mapsto-I
\]
satisfy all presentation relations since \(r\) is odd.
Their restrictions to \(H_r\) map \(s,t\) to \(S,T_z\) because the central exponents in the marking are even.
The indicated integers range from \(n+1\) to \(5n+4\), giving \(4(n+1)\) different traces and \(8(n+1)\) phases.
This proves the claimed estimates directly in the regular representations of the perfect groups.

## Assessment history

### Decision two-dimensional-spectra-and-perfect-markings

| Field | Value |
| --- | --- |
| date | 2026-11-26T05:48 |
| status | proved |
| reason | The independent whole-proof inspection verified the result with its stated assumptions and limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Arbitrary coefficient size, finite and infinite phase counts, and the marked perfect groups. |
| argument | [Normal form for a pair of unitary matrices](#normal-form-for-a-pair-of-unitary-matrices) | Unitary basis, invertible extreme blocks and regular trace bounds. |
| argument | [An explicit perfect marking](#an-explicit-perfect-marking) | Lifted hyperbolic triangle group, torsion-freeness and trivial abelianization. |
| argument | [Counting unitary representations](#counting-unitary-representations) | All indicated phases and the numerical bound. |
| review | [Two-dimensional spectra and perfect markings](../audits/reviews/Yin_R_A0184_v1.md#two-dimensional-spectra-and-perfect-markings) | Independent inspection of the full statement and proof. |

## Current assessment

[Selected decision](#decision-two-dimensional-spectra-and-perfect-markings)

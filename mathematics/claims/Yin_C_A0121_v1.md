---
author: Yin
---

# Full regular rank in a cyclic double with a property (T) vertex

## Statement

Let \(V=\ker(\operatorname{SL}_3(\mathbb Z)\to\operatorname{SL}_3(\mathbb F_3))\), let \(E_{ij}\) denote a matrix unit, and set
\[
       b=I+3E_{12},\qquad a=I+9E_{13},\qquad H=\langle b\rangle .
\]
Form the double \(G=V_1*_H V_2\) by identifying the two copies of \(H\), and write \(a_j\) for the copy of \(a\) in \(V_j\).
The group \(G\) is torsion-free and \(H\) is infinite cyclic.
There is no amenable action of \(G\) on a nonempty discrete set on which \(H\) acts freely.
In particular no coset space meets the hypotheses of the [coamenable subgroup criterion](Yin_C_A0119_v1.md#statement) for this edge.

Nevertheless, put \(p=1-b+a_1+a_2\).
For every \(u\in\mathbb C V_1\) and \(v\in\mathbb C V_2\), the scalar \(p\) is invertible in the affiliated algebra \(\mathcal U(G)\) and
\[
 \operatorname{rk}_G
 \begin{pmatrix}p&u\\v&-p\end{pmatrix}=2,\qquad
 1+(p^{-1}v)(p^{-1}u)\ \text{is a unit of }\mathcal U(G).
\]
Here \(\operatorname{rk}_G\) is the trace of the closed range projection for left convolution with the canonical group trace and unnormalized matrix trace.
There are choices for which \(p,u,v\) are complex linearly independent and their supports generate \(G\).
The element \(a\) is a commutator in \(V\), so every direct sum of scalar characters sends \(a\) to the identity.
The deformation used below comes from a finite quotient that detects \(a\).
This determines one family in the [three-coefficient Schur problem](Yin_C_A0116_v1.md#statement) without assuming scalar integrality for \(G\).
The [Atiyah question](../tasks/Yin_T_A0001_v1.md#contract) for arbitrary matrices over this double requires a separate argument.

## The obstruction to an amenable action

Put \(\Gamma=\operatorname{SL}_3(\mathbb Z)\).
Reduction modulo \(3\) has finite image, so \(V\) has finite index in \(\Gamma\).
If \(V\) contains torsion, it contains an element \(g=I+3^kB\) of prime order \(q\), with \(k\ge1\) and \(B\) nonzero modulo \(3\).
For \(q\ne3\), the binomial expansion gives \(g^q-I\equiv q3^k B\pmod{3^{k+1}}\).
For \(q=3\), it gives \(g^3-I\equiv3^{k+1} B\pmod{3^{k+2}}\), since the other terms are \(3^{2k+1}B^2\) and \(3^{3k}B^3\).
Both contradict \(g^q=I\).
The powers \(b^n=I+3nE_{12}\) are distinct.
Amalgam normal form embeds the vertices with intersection \(H\).
A torsion element of the double fixes a vertex of the Bass–Serre tree, since its finite orbit spans a finite tree and the action preserves vertex types.
It belongs to a conjugate of \(V\) and hence is trivial.

The group \(\Gamma\) has Kazhdan's property (T). [Shalom, Corollary 1, p. 148](../literature/pdf/Sha99.pdf#page=5)
To see that \(V\) inherits this property, take a unitary representation \(\sigma\) of \(V\) with almost invariant unit vectors.
Realize the induced representation by functions \(f\) satisfying \(f(gv)=\sigma(v)^{-1}f(g)\), with the sum of squared norms over a finite transversal \(R\) for \(\Gamma/V\).
For any finite \(S\subset\Gamma\), the decompositions \(s^{-1}r=r'v\) with \(s\in S,\ r,r'\in R\) use finitely many \(v\in V\).
Choosing a unit vector \(\xi\) almost fixed by these \(v\) and putting \(f(r)=\xi/\sqrt{|R|}\) gives a unit vector almost fixed by \(S\) under left translation.
Property (T) of \(\Gamma\) gives a nonzero invariant function, which is constant by left invariance.
Its value is fixed by \(V\) by the defining covariance of \(f\).

If \(G\) acts amenably on a nonempty discrete set \(X\), its permutation representation on \(\ell^2(X)\) has almost invariant unit vectors.
Indeed the squared displacement of \(|F|^{-1/2}1_F\) by \(s\in G\) is \(|sF\mathbin{\triangle}F|/|F|\) for each finite nonempty Følner set \(F\).
Restricting the representation to \(V_1\) gives a nonzero \(V_1\)-invariant vector by property (T).
It is constant on every \(H\)-orbit.
If \(H\) acts freely, every such orbit is infinite and square summability forces the vector to vanish.

## The finite quotient detecting the commutator

With \([x,y]=xyx^{-1}y^{-1}\), matrix multiplication gives \(a=[b,I+3E_{23}]\).
In any direct sum of characters \(\pi(a)=I\) in every basis, so \(a\) contributes zero to either off-diagonal block.
Let \(D\) be the finite image of \(V\) modulo \(5\), and let \(\bar b,\bar a\in D\) be the images of \(b,a\).
The elements \(\bar b^i\bar a^j=I+3iE_{12}+4jE_{13}\) are distinct for \(i,j\in\mathbb F_5\), so \(\bar b,\bar a\) generate a copy \(K\) of \((\mathbb Z/5)^2\).
Let \(\pi\) be the representation of \(V\) obtained by pulling back two copies of the left regular representation of \(D\).
On restriction to \(K\), each copy is a direct sum of \([D:K]\) regular representations, one for each right coset \(Kx\).

Put \(\omega=e^{2\pi i/5}\).
In the Fourier bases of the corresponding copies of \(\ell^2(Kx)\), pair each first-copy vector \(e\) with joint \((\bar b,\bar a)\)-eigenvalues \((\omega^h,\omega^l)\) with the second-copy vector \(f\) having eigenvalues \((\omega^h,\omega^{l+1})\).
Shifting \(l\) modulo \(5\) is a permutation, so the planes spanned by these pairs form an orthogonal decomposition of the representation space.
Let \(E_1,E_2\) be spanned, respectively, by all \((e+f)/\sqrt{2}\) and all \((e-f)/\sqrt{2}\), and put \(d=\dim E_1=\dim E_2=|D|\).
The operator \(\pi(b)\) is scalar on each paired plane and preserves \(E_1,E_2\).
In the two displayed bases, the off-diagonal blocks \(\pi(a)_{12}\) and \(\pi(a)_{21}\) act on the paired coordinates by the nonzero factors \((\omega^l-\omega^{l+1})/2\).
Thus both are invertible maps between the two \(d\)-dimensional spaces.

## The regular rank computation

Use \(\pi\) on the left vertex and \(D_t\pi D_t^{-1}\) on the right, with \(D_t=\operatorname{diag}(tI_{E_1},I_{E_2})\).
For every \(|t|=1\), these vertex representations agree on \(H\), and define a representation \(\pi_t\) of \(G\).
For \(p_L=1-b+a_1,\ p_R=a_2\), write \(L,R\) for their regular convolution operators twisted by the unbent \(\pi\) on their respective vertices.
The two pivots are
\[
       L_{12}=\lambda_G(a_1)\otimes\pi(a)_{12},\qquad
       R_{21}=\lambda_G(a_2)\otimes\pi(a)_{21}.
\]
They are boundedly invertible.

We give the block sizes in the [two-dimensional deformation argument](Yin_C_A0118_v1.md#regular-trace-identity-and-the-specialization) for this representation.
Write \(M=\left(\begin{smallmatrix}p&u\\v&-p\end{smallmatrix}\right)\).
The unitary \(\delta_g\otimes w\mapsto\delta_g\otimes\pi_t(g)w\) intertwines the \(2d\)-fold regular amplification with the twist and fixes the fiber at the identity.
The twisted ranks of \(p,M\) are therefore \(2d\operatorname{rk}_G p,\ 2d\operatorname{rk}_G M\).
On the right blocks the conjugation multiplies the \(12\) entry by \(t\) and the \(21\) entry by \(t^{-1}\).
Multiply each \(E_2\) output row by \(t\) and apply the row and column permutations of that argument.
This gives degree-at-most-one matrix polynomials with group von Neumann algebra entries.
At zero their block triangular matrices have diagonal blocks \((R_{21},L_{12})\) for \(p\) and \((R_{21},-R_{21},-L_{12},L_{12})\) for \(M\).
They have ranks \(2d,4d\), respectively.
For each such polynomial \(F\) and \(N>1\) distinct unit phases \(t_j\), the [Vandermonde rank inequality](Yin_C_A0022_v1.md#simultaneous-generic-rank-and-degeneration) gives
\[
           (N-1)\operatorname{rk}_G F(0)
               \le \sum_{j=1}^N\operatorname{rk}_G F(t_j).
\]
The row and column operations preserve rank at these phases, so dividing by \(2dN\) and letting \(N\to\infty\) gives \(\operatorname{rk}_G p=1,\ \operatorname{rk}_G M=2\).
Full regular rank makes \(p\) a unit of \(\mathcal U(G)\).
Elimination at this pivot leaves \(-p-vp^{-1}u=-p[1+(p^{-1}v)(p^{-1}u)]\) of full rank, proving the second unit assertion.

For the assertion about supports, the elementary matrices \(I+E_{ij}\), \(i\ne j\), generate \(\Gamma\) by integer elementary row reduction.
Schreier's lemma therefore gives a finite generating set \(B\) for the finite-index subgroup \(V\).
Include \(a^2\) in \(B\) and omit the identity.
Let \(B_j\subset V_j\) denote its copy and take
\[
          u=\sum_{s\in B_1}s,\qquad v=\sum_{s\in B_2}s .
\]
The supports of \(u,v\) generate the two vertices.
The element \(a^2=I+18E_{13}\) lies outside \(H\) and differs from \(a\).
Thus \(a_1^2\) occurs only in \(u\) and \(a_2^2\) only in \(v\), by the vertex intersection formula.
Their coefficients in a linear relation force the multipliers of \(u,v\) to vanish, and then \(p\ne0\) forces its multiplier to vanish as well.

## A commuting relation in the two-weight deformation

Impose the additional relation \([a_1,a_2]=1\) on the double.
For any finite-dimensional vertex representations on \(E_1\oplus E_2\) with edge images preserving both summands and agreeing there, write \(A,B\) for the images of \(a_1,a_2\) and \(D_t=\operatorname{diag}(tI_{E_1},I_{E_2})\).
If the representations with right vertex conjugated by \(D_t\) descend for infinitely many unit phases, the Laurent polynomial \(AD_tBD_t^{-1}-D_tBD_t^{-1}A\) vanishes identically.
The diagonal blocks of its \(t^{-1}\) coefficient give \(A_{12}B_{21}=0\) and \(B_{21}A_{12}=0\).
The two resulting inclusions of images in kernels imply
\[
 \operatorname{rank}A_{12}+\operatorname{rank}B_{21}
          \le\min\{\dim E_1,\dim E_2\}.
\]
Consequently for two nonzero weight spaces the two off-diagonal coefficients coming from \(a_1,a_2\) cannot both have maximal rank, even with arbitrarily large multiplicities.
This obstruction concerns the stated deformation on the quotient and gives no rank conclusion for matrices on the quotient.

## Assessment history

### Decision property-t-bending-test

| Field | Value |
| --- | --- |
| date | 2026-11-22T04:54 |
| status | proved |
| reason | Independent review verifies the full statement and argument under the specified assumptions. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | A torsion-free double with no amenable action free on the edge, full regular ranks for the specified mixed pencils and an obstruction after a mixed relation. |
| argument | [Proof](#the-obstruction-to-an-amenable-action) | Congruence group, property (T), finite quotient detection of a commutator, triangular block degeneration and quotient obstruction. |
| review | [Whole finding](../audits/reviews/Yin_R_A0158_v1.md#whole-finding) | Independent whole-argument finding at the stated scope. |

## Current assessment

[Selected decision](#decision-property-t-bending-test)

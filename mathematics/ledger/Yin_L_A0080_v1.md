---
author: Yin
---

# Fourier multipliers on rational elements and on a two-column kernel projection

For the [torsion-free deletion question](../tasks/Yin_T_A0003_v3.md#contract), one possible way to extract an entry of a matrix over \(\mathcal N(G)\) is to pass to the group coproduct and apply a functional to one tensor factor.
Finite-dimensional unitary matrix coefficients preserve the division closure \(D_G\) in this operation.
For the regular representation of \(\mathbb Z^2\), a faithful normal state with strictly positive rational density already gives a different outcome on the kernel projection of one row with two group-ring entries.

## Finite-dimensional matrix coefficients

Write \(M=\mathcal N(G)\), \(U=L^0(M)\), and \(D_G=\operatorname{Div}_U(\mathbb CG)\).
Let \(\sigma:G\to U(n)\) be any finite-dimensional unitary representation.
The unitary on \(\ell^2(G)\otimes\mathbb C^n\) given by \(\delta_s\otimes v\mapsto \delta_s\otimes\sigma(s)v\) conjugates \(\lambda(g)\otimes I_n\) to \(\lambda(g)\otimes\sigma(g)\).
Thus this assignment extends to a normal unital \(*\)-homomorphism \(\Theta_\sigma:M\to M_n(M)\) and, by the same conjugation on affiliated operators, to \(U\to M_n(U)\).
Its values on \(\mathbb CG\) have entries in \(\mathbb CG\).
At each scalar inversion in a rational expression the image of the pivot is invertible in \(M_n(U)\).
If the pivot's entries lie in \(D_G\), so do the entries of its inverse by [scalar elimination for an invertible matrix](../claims/Yin_C_A0132_v1.md#argument).
Induction on the expression gives \(\Theta_\sigma(D_G)\subseteq M_n(D_G)\).

In particular, for any fixed complex row \(w\) and column \(v\), the map \(d\mapsto w\Theta_\sigma(d)v\) preserves \(D_G\).
On bounded \(d\) its Fourier coefficient at \(g\) is \(\widehat d(g)\,w\sigma(g)v\), by the formula on the group algebra and normality.
This defines the multiplier even when the coefficient \(w\sigma(g)v\) does not come from a normal functional on \(M\).

## A positive rational density on the two-torus

Take \(G=\mathbb Z^2\) and use Haar probability measure on \(\mathbb T^2\), the coordinate functions \(x,y\), and the canonical trace \(\tau\).
Here \(D_G=\mathbb C(x,y)\) as measurable functions, since a nonzero Laurent polynomial has a null set of zeros.
Fix a real \(0<c<1/2\) and set
\[
 d=1-c(x+y),\qquad q=xy-c(x+y),\qquad
 f=d^{-1},\qquad u=q/d=1+(xy-1)f .
\]
On the torus \(q=xy\,\overline d\), so \(|u|=1\), and \(|d|\ge1-2c>0\).
The kernel of the group-ring row \((d,-q)\) consists of the columns \((u\xi,\xi)^{\mathsf T}\).
Its orthogonal projection is
\[
                     P=\frac12\begin{pmatrix}1&u\\u^*&1\end{pmatrix}
                       \in M_2(D_G).
\]
Define a rational density by
\[
 h=f+f^*-1
   =\frac{1-|c(x+y)|^2}{|1-c(x+y)|^2}.
\]
It is continuous and strictly positive everywhere on the torus.
The norm-convergent expansion \(f=\sum_{n\ge0}c^n(x+y)^n\) gives \(\tau(h)=1\), so \(\omega_h(v)=\tau(hv)\) is a faithful normal state.

For the normal coproduct \(\Delta(\lambda(g))=\lambda(g)\otimes\lambda(g)\) let \(S=(\mathrm{id}\otimes\omega_h)\Delta\).
Use the Fourier convention \(v=\sum_{i,j}\widehat v(i,j)x^iy^j\) on absolutely convergent expansions.
Then \(S\) multiplies the \((i,j)\)-coefficient by \(\widehat h(-i,-j)\).
For \(i,j\ge0\) this multiplier is
\[
 f_{ij}=\widehat f(i,j)={i+j\choose i}c^{i+j},
\]
including \(f_{00}=1\).
Both \(f\) and \(u\) have absolutely summable coefficients supported in this quadrant.
After setting \(x=y=t\), the coefficient of \(t^n\) in \(S(f)(t,t)\) is therefore \(\sum_{i=0}^n{n\choose i}^2 c^{2n}={2n\choose n}c^{2n}\).
For \(S(xy f)(t,t)\) it vanishes for \(n<2\), and for \(n\ge2\) it equals
\[
 \sum_{i=1}^{n-1} {n-2\choose i-1}{n\choose i}c^{2n-2}
        ={2n-2\choose n-1}c^{2n-2}
\]
by Vandermonde's identity.
Writing \(F(t)=(1-4c^2t)^{-1/2}\) with \(F(0)=1\), the two diagonal series are \(F(t)\) and \(t(F(t)-1)\), respectively.
Since \(S(1)=1\), the upper right corner of \(S(P)\), with \(S\) applied entrywise, satisfies
\[
                  2S(P)_{12}(t,t)=S(u)(t,t)=(t-1)(F(t)-1).
\]

The coefficient formulas and \(4c^2<1\) give absolute convergence of the bivariate series for \(S(u)\) on a neighborhood of the closed unit bidisc.
If \(S(u)\) belonged to \(D_G\), choose relatively prime polynomials \(B,C\) with \(S(u)=B/C\) almost everywhere on the torus.
The boundary identity \(CS(u)=B\) holds on the bidisc by uniqueness of the Fourier coefficients of these analytic functions.
If \(C(t,t)\) vanished identically, then so would \(B(t,t)\), and \(x-y\) would divide both polynomials.
Hence \(S(u)(t,t)\) would be rational in \(t\).
The displayed formula would then make \(F(t)\) rational, which is impossible because \(F(t)^2=(1-4c^2t)^{-1}\) has a simple pole.
Consequently \(S(P)_{12}\notin D_G\), although \(P\) is the rational kernel projection of the given group-ring row.
Any attempt to derive rationality of a two-column kernel projection by such a slice must therefore use a property beyond positivity, normality and rationality of its density.

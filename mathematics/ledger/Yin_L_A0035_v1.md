---
author: Yin
---
# Projection norms on product windows of a scalar annihilator

For a scalar \(a\in\mathbb C[K]\) and a finite \(F\subset K\), give \(\mathbb C[F]\) its coefficient \(\ell^1\)-norm.
Write \(E_F(a):=\{x\in\mathbb C[F]:ax=0\}\), where the product is tested on all of \(K\).
Write \(\kappa_F(a)\) for the smallest norm of a linear projection from \(\ell^1(F)\) onto \(E_F(a)\), with value zero when \(E_F(a)=0\).
The [local projection criterion](Yin_L_A0031_v2.md#definition-local-kernel-projection-constant) forces these norms to diverge along any increasing exhaustion if a nonzero scalar over a countable torsion-free amenable group has positive regular nullity.
Here a single finite annihilating vector gives an explicit finite window with \(\kappa_F(a)>1\), and product windows give an exact exponential rate.

## A window formed from two translates

Assume that \(K\) is torsion-free and that \(0\ne a\in\mathbb C[K]\) has a nonzero finitely supported right annihilator.
Choose such an annihilating vector \(z\) with minimum support cardinality \(s\), normalize \(\|z\|_1=1\), and put \(A:=\operatorname{supp}(z)\).
Then \(s\ge2\) because any nonzero vector supported at one group element is a unit of \(\mathbb C[K]\).
For distinct \(g_1,g_2\in A\), put \(h:=g_1^{-1}g_2\), \(w:=zh\) and \(B:=Ah\).
The intersection \(C:=A\cap B\) contains \(g_2\) and is a proper subset of \(A\).
Indeed, equality would imply \(Ah=A\), which would put all the distinct \(g_1h^n\) in the finite set \(A\).
Thus \(F:=A\cup B\) has at most \(2s-1\) points, and \(z,w\in E_F(a)\).

Define
\[
 \beta:=\min_{\substack{v\in\mathbb C[C]\\\|v\|_1=1}}\|av\|_1,
 \qquad \eta:=\frac{\beta}{\beta+\|a\|_1}.
\]
The minimum is positive by minimality of \(s\) and compactness of the finite-dimensional unit sphere.
For \(y\in E_F(a)\), the equality \(a1_Cy=-a1_{F\setminus C}y\) and the convolution norm inequality give
\[
 \beta\|1_Cy\|_1\le\|a\|_1\|1_{F\setminus C}y\|_1,
 \qquad \|1_Cy\|_1\le(1-\eta)\|y\|_1.                              \tag{1}
\]
Here \(1_D\) applied to a vector denotes coordinate restriction to \(D\), extended by zero.
Take \(i\in C\), \(\theta:=|z_i|\) and \(\psi:=|w_i|\), both positive.
For any projection \(P\) onto \(E_F(a)\), set \(M:=\|P\|\) and \(v_j:=P\delta_j\) for \(j\in F\).
Since \(Pz=z\) and \(\|v_j\|_1\le M\),
\[
  1\le\sum_{j\in A}|z_j|\|1_Av_j\|_1
       \le\theta\|1_Av_i\|_1+(1-\theta)M .
\]
Consequently \(\|1_Av_i\|_1\ge M-(M-1)/\theta\).
Applying the same estimate to \(w\) and \(B\) gives \(\|1_{F\setminus B}v_i\|_1\le(M-1)/\psi\).
Subtracting this last bound from the bound on \(A\) and using (1) yields
\[
   (1-\eta)M\ge\|1_Cv_i\|_1
          \ge M-(M-1)(\theta^{-1}+\psi^{-1}).
\]
In particular,
\[
        \kappa_F(a)\ge
        \left(1-\frac{\eta}{\theta^{-1}+\psi^{-1}}\right)^{-1}>1 .       \tag{2}
\]
The constant uses only the displayed coefficients and the restriction of left convolution to \(\mathbb C[C]\).

## The exact minimum under tensor products

For finite sets \(I,J\), take subspaces \(E\subset\ell^1(I)\) and \(E'\subset\ell^1(J)\) with their inherited norms.
Give \(Z:=E\otimes E'\subset\ell^1(I\times J)\) the inherited coefficient norm on the product set.
Let \(\kappa(E,I)\) denote the minimum norm of a projection from \(\ell^1(I)\) onto \(E\).
Then
\[
              \kappa(Z,I\times J)=\kappa(E,I)\kappa(E',J).               \tag{3}
\]
If a factor is zero both sides vanish, so suppose the factors are nonzero.
Let \(\iota:E\hookrightarrow\ell^1(I)\) be inclusion and \(\alpha_i\) the restriction to \(E\) of the \(i\)-th coordinate functional.
A map \(R:\ell^1(I)\to E\) has norm at most one if and only if every column \(R\delta_i\) lies in the unit ball of \(E\).
The map \(R\mapsto R\iota\) surjects onto \(\operatorname{End}(E)\), since any linear map on \(E\) extends to \(\ell^1(I)\) in finite dimension.
The quotient norm of the identity on \(E\) is \(\kappa(E,I)\).
Indeed, \(R\iota=1_E\) exactly when \(\iota R\) is a projection onto \(E\), with the same norm as \(R\).

Represent the linear dual of \(\operatorname{End}(E)\) by \(S\mapsto\operatorname{Tr}(ST)\).
The norm of the pullback of this functional under \(R\mapsto R\iota\) is \(\sum_{i\in I}\|\alpha_i\circ T\|_{E^*}\).
To see this, write \(\operatorname{Tr}(R\iota T)=\sum_i(\alpha_i\circ T)(R\delta_i)\) and optimize the columns independently, choosing their phases so the nonzero terms have the same argument.
Finite-dimensional quotient duality gives
\[
 \kappa(E,I)=
  \sup_{0\ne T\in\operatorname{End}(E)}
       \frac{|\operatorname{Tr}T|}{\sum_{i\in I}\|\alpha_i\circ T\|_{E^*}}.     \tag{4}
\]
For \(f\in E^*,\,g\in(E')^*\), one has \(\|f\otimes g\|_{Z^*}=\|f\|\|g\|\).
For the upper bound, extend the functionals without norm increase to \(\ell^1(I)\) and \(\ell^1(J)\) by Hahn–Banach.
Their coefficient arrays in \(\ell^\infty(I)\) and \(\ell^\infty(J)\) multiply in separate coordinates to give an extension to \(\ell^1(I\times J)\) of norm \(\|f\|\|g\|\).
Testing on a simple tensor of norm-attaining vectors gives the reverse bound.
Apply (4) on \(Z\) with \(T\otimes T'\).
Both its numerator and its denominator factor, because the coordinate functionals on \(Z\) are \(\alpha_i\otimes\alpha'_j\).
Taking suprema proves the lower bound in (3).
For the upper bound, tensor norm-minimizing projections on the factors.
Their product is a projection onto \(Z\), and its ambient \(\ell^1\)-operator norm is the product of the two norms by the maximum column-sum formula.

## Wreath-product consequence and remaining estimate

In \(W:=K\wr\mathbb Z\), let \(a_j\) be the copy of \(a\) at lamp \(j\) and \(S_n:=\sum_{j=1}^n a_j^*a_j\).
View \(F^n\) as a subset of the direct product of these \(n\) lamp groups in \(W\).
The [lamp kernel calculation](../claims/Yin_C_A0017_v2.md#minimum-support-of-an-annihilator) gives \(S_n x=0\) exactly when \(a_jx=0\) for all \(j\), by positivity.
On arrays supported in \(F^n\), the \(j\)-th condition requires each slice in coordinate \(j\) to belong to \(E_F(a)\).
To intersect these conditions, choose any linear complement \(V\) to \(E_F(a)\) in \(\mathbb C[F]\) and expand \((E_F(a)\oplus V)^{\otimes n}\) as a direct sum.
The \(j\)-th condition removes precisely the summands with \(V\) in slot \(j\).
Thus \(E_{F^n}(S_n)=E_F(a)^{\otimes n}\), and (3) gives
\[
                      \kappa_{F^n}(S_n)=\kappa_F(a)^n .                 \tag{5}
\]
For the window in (2), even the optimum over unrestricted projections in all \(n\) coordinates grows exponentially, with a rate already determined on \(A\cup Ah\).

For the torsion-free amenable case of [A0001](../tasks/Yin_T_A0001_v1.md#contract), a failure of integer matrix rank yields a finite scalar zero product by [finite descent](../claims/Yin_C_A0001_v2.md#finite-scalar-descent-and-a-complete-conditional-kernel-witness).
An independent estimate forcing \(\liminf_{n\to\infty}\kappa_{F^n}(S_n)^{1/n}\le1\) for all such \(a\) and fixed windows \(F\) would therefore suffice.
By (5) this estimate would give a contractive projection on each nonzero single-coordinate kernel, including the window (2) in a hypothetical counterexample.
The finite-support density of the Hilbert kernel supplies the annihilating vector but gives no bound on that projection norm.

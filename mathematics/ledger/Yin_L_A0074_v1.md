---
author: Yin
---

# A diagonal kernel coefficient and rank bounds in the torsion-free commutator problem

For [A0003](../tasks/Yin_T_A0003_v3.md#contract), let \(G\) be finitely generated with marked left translations \(X_j\), let \(M=\mathcal N(G)\), \(H=L^2(M,\tau)=\ell^2(G)\) and \(U=L^0(M)\).
Write \(A=\mathbb CG\) and \(D=\operatorname{Div}_U A\).
This note reduces complete deletion of the local test to a specific bounded coefficient of an inverse-free group-algebra matrix, and determines what happens if only the ranks of the test operators are restricted.

## One diagonal coefficient of a bordered pencil

Let \(L=L_0+\sum_j L_jX_j\) be an \(n\)-by-\(n\) affine pencil with complex coefficient matrices that is injective on \(H^n\).
Let \(\alpha,\beta\) be a constant row and column of length \(n\).
Use \(J\) for the inclusion of the last coordinate and put
\[
 B=\begin{pmatrix}L&\beta\\ \alpha&0\end{pmatrix},\qquad
 h=J^*p_{\ker B}J,\qquad x=\alpha L^{-1}\beta,\qquad p=p_{\ker x}.
\]
Then \(0\le h\le1\), and
\[
                    h\in D\quad\Longleftrightarrow\quad p\in D.
\]
The matrix \(B\) and the positive matrix \(B^*B\) contain only group-algebra entries, and both have the same kernel projection.
Their unnormalized kernel dimension equals \(\tau(p)\le1\) by [bordered elimination](Yin_L_A0004_v1.md#proof-of-the-linear-and-bordered-equivalences).
The equivalence here concerns the actual coefficient \(h\), including when \(0<\tau(p)<1\).

Write \(k=L^{-1}\beta\) and \(T=1+k^*k\).
The scalar-pivot argument puts every entry of \(k\) in \(D\), and \(D\) is closed under adjoints because the generating group algebra is. [Affine realizations and scalar pivots](../claims/Yin_C_A0131_v2.md#linear-pencils-for-scalar-rational-operations)
Work in affiliated column modules to allow unbounded \(k\).
The first block row of \(B\binom{y}{z}=0\) forces \(y=-kz\), and the second gives \(xz=0\), equivalently \(z\in pU\).
Put
\[
 W=\binom{-k}{1}p,\qquad a=pTp+1-p=1+(kp)^*kp .
\]
Here \(a\) commutes with \(p\) and is invertible in \(U\) by positivity and the lower bound \(1\).
Since \(W^*W=pTp\), the element \(Q=Wa^{-1}W^*\) is a selfadjoint idempotent with \(QW=W\) and column image \(WU\).
A selfadjoint idempotent in an affiliated matrix algebra is a bounded projection.
The Hilbert kernel projection of \(B\) also has column image \(\ker_U B\), by polar decomposition, so \(Q=p_{\ker B}\).
Compression gives \(h=pa^{-1}p\).
In particular \(p\in D\) implies \(h\in D\) by scalar division closure.

For the converse set \(d=hT\).
The displayed compression formula gives \(pd=d\) and \(dp=p\), so \(d^2=d\) and \(dU=pU\).
To obtain the orthogonal projection onto this right ideal, let \(g=d+d^*-1\).
The identity \(g^2=1+(d-d^*)^*(d-d^*)\) makes \(g\) a unit in \(U\).
Since \(gd=d^*g=d^*d\), the element \(f=dg^{-1}=g^{-1}d^*\) is selfadjoint and satisfies \(fd=d\) and \(df=f\).
It is therefore an idempotent with \(fU=dU\), proving \(p=f\).
If \(h\in D\), all operations forming \(p=d(d+d^*-1)^{-1}\) are scalar rational operations in \(D\).

Every \(x\in D\) admits a realization of the stated form.
Consequently complete deletion for a given marked group is equivalent to \(h\in D\) for every bordered pencil above, by the [kernel-projection criterion](../claims/Yin_C_A0131_v1.md#which-rationality-is-detected).
For a negative answer in the torsion-free case, it suffices to exhibit such a group and such a pencil with \(h\notin D\).
Membership of each of these bounded coefficients for arbitrary torsion-free groups remains to be decided.

## Restricting the rank of local test operators

Suppose at least one marked generator has infinite order, with left translation \(X\).
This includes every nontrivial finitely generated torsion-free group.
In the [local commutation criterion](../claims/Yin_C_A0131_v3.md#statement), restrict the universal test to operators of rank at most a fixed integer \(r\ge0\), keeping the existential choice of \(V\).
The resulting condition is equivalent to solvability of the unrestricted fraction equation (1).

Indeed, fix any fraction pair and finite-rank solution \(T_j\) of (1), and let \(W\) be the complex span of \(s\delta_e\) and all the witness ranges.
For \(m\ge1\) put \(V_m=\sum_{i=0}^{m-1} WX^i\).
A test map \(C\) commuting with right multiplication by \(X\) on \(V_m\) satisfies
\[
            C(wX^i)=(Cw)X^i\qquad(w\in W,\ 0\le i\le m).
\]
The endpoint follows by applying commutation to \(wX^{m-1}\in V_m\).
The first \(m+1\) right translates of any nonzero vector by \(X\) are linearly independent.
Indeed, restriction to each right-translation orbit identifies the shift there with the bilateral shift on \(\ell^2(\mathbb Z)\).
Fourier transformation makes a nonzero polynomial in this shift multiplication by a trigonometric polynomial whose zero set has Haar measure zero.
Thus \(\operatorname{rank} C\le m\) implies \(Cw=0\) for every \(w\in W\), and the displayed identity gives \(C|_{V_m}=0\).
Taking \(m=\max(1,r)\) supplies the required subspace for the restricted test, even before imposing \(C(s\delta_e)=0\).
The converse follows because a restricted certificate still includes the original solution of (1).

The same argument applies to a cutoff \(r=f(\dim V)\) for any nonnegative integer-valued \(f\) with \(f(n)=o(n)\).
Writing \(w_0=\dim W\), we have \(m\le\dim V_m\le m w_0\), where the first inequality uses the translates of the nonzero vector \(s\delta_e\).
For sufficiently large \(m\) this gives \(f(\dim V_m)\le m\).
For comparison, the full local test on a prescribed \(V\) already has the exact finite rank bound
\[
 \dim_{\mathbb C}\Big(V+\sum_j VX_j\Big)
       -\dim_{\mathbb C}\operatorname{span}\{s\delta_e,sX_1\delta_e,\ldots,sX_d\delta_e\}
\]
in the sense that testing up to that rank suffices.
A map witnessing failure restricts to the first space and kills the second space by local commutation.
Extending this restriction by zero on the orthogonal complement preserves its failure on \(V\) and gives the stated rank bound.
This bound need not be the least possible.
The fixed and sublinear cutoffs therefore give another formulation of the deletion question on the torsion-free class.
Their equivalence to (1) alone leaves the universal rationality question open.

## A solution with a nonrational range on the two-torus

Take the standard marked group \(G=\mathbb Z^2\), with shifts \(X,Y\), and let \(p\) be multiplication by the indicator of a half-circle in the first Fourier coordinate.
The Fourier realization gives \(D_G=\mathbb C(z_1,z_2)\), so \(p\notin D_G\) since \(p\) is a nontrivial idempotent. [The abelian example](../claims/Yin_C_A0131_v1.md#the-cycle-of-a-relator)
Set \(u=0\), \(s=t=1\), \(a=b=0\), and put \(F=pP_e\), \(T_X=[\rho_Y,F]\), \(T_Y=-[\rho_X,F]\).
The two right shifts commute, so the Jacobi identity gives (1).
Since \(T_X\delta_{g_Y^{-1}}=-p\delta_e\), every subspace containing the witness ranges contains \(p\delta_e\).
Any admissible subspace for these denominators lies in \(D_G\) by [the reconstruction from translation relations](../claims/Yin_C_A0131_v3.md#recovering-the-vectors-in-the-subspace).
Thus this tuple fails the local condition even though the zero tuple meets it for the same fractions.
Complete deletion concerns the existence of an admissible tuple for each \(u\) for which (1) is solvable.

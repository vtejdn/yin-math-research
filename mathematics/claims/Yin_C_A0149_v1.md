---
author: Yin
---

# Finite determination of rational Laurent series at fixed group support

## Statement

Let \(G\) be a finitely generated discrete group, \(A=\mathbb CG\), and \(U=L^0(\mathcal N(G))\).
For a central variable \(z\), let \(S\) be the division closure of \(A[z]\) in \(U((z))\), let \(O=S\cap U[[z]]\), and let \(D_G\) be the division closure of \(A\) in \(U\).
Fix a finite set \(F\subset G\) containing the identity, an integer \(n\ge1\), and an integer \(d\ge0\).
Consider all series with a realization
\[
           f(z)=\alpha L(z)^{-1}\beta,\qquad
           L(z)=\sum_{j=0}^d L_j z^j,\qquad
           L_j\in M_n(\operatorname{span}_{\mathbb C}F),
\]
where \(\alpha\in M_{1,n}(\mathbb C)\), \(\beta\in M_{n,1}(\mathbb C)\), and \(L\) is invertible over \(U((z))\).
The entries of \(L^{-1}\) belong to \(S\) by [formal scalar inversion](Yin_C_A0143_v1.md#formal-inversion-by-scalar-pivots).
All complex coefficients may vary and the inverse may have any finite pole order.

There is an integer \(N_0=N_0(G,F,n,d)\ge1\) such that, for \(N\ge N_0\), every such \(f\) satisfies all three implications
\[
 \begin{aligned}
   f\in z^NU[[z]] &\quad\Longrightarrow\quad f=0,\\
   f-b\in z^NU[[z]]\text{ for some }b\in U
       &\quad\Longrightarrow\quad f=b\text{ as a constant series, and }b\in D_G,\\
   f\in O,\quad f^2-f\in z^NU[[z]]
       &\quad\Longrightarrow\quad f^2=f .
 \end{aligned}
\]
In particular, fix \(x\in D_G\) and write \(p=p_{\ker x}\).
Then \(p\in D_G\) if and only if there exist \(F,n,d\) as above and realizations \(f_N\in O\) for arbitrarily large \(N\) satisfying \(f_N(0)=p\) and \(f_N^2-f_N\in z^NU[[z]]\).
One obtains the same equivalence by requiring the full constant jet \(f_N-p\in z^NU[[z]]\).
The bounds may depend on \(x\), and the approximating series may vary with \(N\).
By the [kernel-projection criterion](Yin_C_A0131_v1.md#which-rationality-is-detected), complete deletion of the local condition in the finite-rank equation for a fixed torsion-free \(G\) is equivalent to either bounded-realization property for each \(x\in D_G\).

## Argument

### Rank over a finite interval of powers

Set \(P=U[[z]]\), \(J=G\times\mathbb Z\), and denote the generator of the central factor by \(Z\).
Use the unnormalized matrix trace for affiliated rank and right \(U\)-module dimension.
For a polynomial matrix \(B(z)\) over \(A\), Fourier transformation in the central variable gives
\[
    \operatorname{rk}_J B(Z)=\operatorname{rk}_G B(s)
    \qquad\text{outside a countable set of }s\in\mathbb C.
\]
Indeed its fiber rank is maximal outside a countable set, and integrating this rank on the unit circle gives the left side. [Generic polynomial rank](Yin_C_A0143_v1.md#full-rank-away-from-a-countable-set)

For \(M\ge1\) let \(T_M(B)\) act on coefficient columns of degrees \(0,\ldots,M-1\) by multiplication modulo \(z^M\).
On the same coefficient spaces let \(C_{M,c}(B)\) act by multiplication modulo \(z^M-c\) for \(c\in\mathbb C^\times\).
Evaluation at the \(M\) roots of \(c\) identifies this second matrix up to scalar changes of bases with the direct sum of the \(M\) evaluations of \(B\).
One can choose \(c\) so that all roots avoid the countable exceptional set.
Then \(\operatorname{rk}_G C_{M,c}(B)=M\operatorname{rk}_J B(Z)\).
If \(B\) has degree at most \(d\), the difference \(C_{M,c}(B)-T_M(B)\) has output only in the first \(\min(d,M)\) coefficient positions.
For \(d<M\) these are exactly the possible degrees of terms wrapping past \(z^{M-1}\), while for \(d\ge M\) the bound includes the whole interval.
Rows of \(B\) independent of \(z\) contribute zero to this difference.

For the given \(L\), the matrix \(L(Z)\) is an affiliated unit by [Laurent evaluation](Yin_C_A0143_v1.md#statement).
Choose \(M\ge1\) large enough that \(z^M L^{-1}\in M_n(P)\).
Then \(z^M P^n\subseteq LP^n\), so the right \(U\)-module \(P^n/LP^n\) is the cokernel of \(T_M(L)\).
Since a suitable \(C_{M,c}(L)\) is invertible and differs from \(T_M(L)\) by a matrix of rank at most \(nd\), this gives the uniform estimate
\[
                     \dim_U(P^n/LP^n)\le nd.
\]
The chosen \(M\) can vary with \(L\).

### Vanishing order and the rank of a bordered matrix

Assume \(f\in z^N P\), and put
\[
               B(z)=\begin{pmatrix}L(z)&-\beta\\ \alpha&0\end{pmatrix}.
\]
Among the polynomials \(w\in U[z]\) of degree less than \(N\), those satisfying \(\beta w\in LP^n\) form the kernel of the map \(w\mapsto[\beta w]\) into \(P^n/LP^n\).
They therefore form a right \(U\)-module of dimension at least \(N-nd\).
For each such \(w\), the column \(y=L^{-1}\beta w\) belongs to \(P^n\) and satisfies \(\alpha y=fw\in z^NP\).
Consequently \(w\mapsto(y\bmod z^N,w)\) injects this module into \(\ker T_N(B)\), and \(\operatorname{rk}_G T_N(B)\le nN+nd\).
Only the first \(n\) rows of \(B\) can wrap in cyclic reduction, so comparison at \(M=N\) gives
\[
          n\ \le\ \operatorname{rk}_J B(Z)
             \ \le\ n+\frac{2nd}{N}.
\]
The lower bound follows from the invertible leading block \(L(Z)\).
Its Schur complement is the image of \(f\) under the [injective evaluation homomorphism](Yin_C_A0143_v1.md#statement), so equality with \(n\) implies \(f=0\).

Regard all scalar entries of \(\alpha,\beta\) and all coefficients of the \(L_j\) in the group basis \(F\) as independent complex parameters \(t\).
The bordered matrix \(B_t(Z)\) has polynomial entries in these parameters with coefficients in the finite von Neumann algebra \(\mathcal N(J)\).
By [closedness of rank sublevels](Yin_C_A0128_v1.md#statement), the sets
\[
             X_k=\{t:\operatorname{rk}_J B_t(Z)\le n+1/k\},
             \qquad k\ge1 ,
\]
are closed in the Zariski topology of a fixed finite-dimensional complex affine space.
Their descending chain stabilizes at some \(k_*\), so \(X_{k_*}=\bigcap_k X_k=\{t:\operatorname{rk}_J B_t(Z)\le n\}\).
Thus \(N\ge\max(1,2nd\,k_*)\) forces \(f=0\).
The closed sets were formed on the entire parameter space, and the actual realization supplies the invertibility of its pivot.

### Constant jets and idempotent jets

If \(f-b\in z^NP\), then \(f(z)-f(2z)\in z^NP\).
This difference has the block diagonal realization with pivot \(\operatorname{diag}(L(z),L(2z))\), row \((\alpha,-\alpha)\), and column \(\binom{\beta}{\beta}\).
The preceding zero test at size \(2n\) gives \(f(z)=f(2z)\).
In positive degree \(j\) every coefficient is therefore annihilated by \(2^j-1\), so \(f=b\) and [descent of constant series](Yin_C_A0141_v1.md#descent-of-a-constant-series) gives \(b\in D_G\).

For the idempotent identity the realization
\[
        f^2-f=
        \begin{pmatrix}\alpha&-\alpha\end{pmatrix}
        \begin{pmatrix}L&-\beta\alpha\\0&L\end{pmatrix}^{-1}
        \binom{0}{\beta}
\]
follows by block multiplication.
Its size is \(2n\), its degree is at most \(d\), and its coefficients use the same support \(F\), since \(1_G\in F\).
The zero test at size \(2n\) again applies.
Taking the larger of the thresholds at sizes \(n\) and \(2n\) gives the asserted \(N_0\).

For \(p=p_{\ker x}\), an exact idempotent \(f_N\) with constant coefficient \(p\) implies \(p\in D_G\) by [recovery applied to the positive element \(x^*x\)](Yin_C_A0147_v1.md#recovering-the-orthogonal-projection).
The constant-jet alternative gives \(p\in D_G\) directly.
Conversely, \(p\in D_G\) gives the constant idempotent \(p\in O\), with one [polynomial matrix realization](Yin_C_A0141_v1.md#recovering-a-laurent-coefficient-from-finitely-many-equations) valid for every \(N\).
The [finite truncation isomorphism](Yin_C_A0146_v1.md#constant-terms-at-finite-order) supplies constant jets of each prescribed order for every such \(p\).
Whether their support, matrix size and degree can be bounded across all orders for every \(x\) in every finitely generated torsion-free group remains open here.

## Assessment history

### Decision bounded-realizations

| Field | Value |
| --- | --- |
| date | 2026-11-25T11:23 |
| status | proved |
| reason | The truncated cokernel costs at most the degree times the realization size, and closed rank sublevels turn the resulting rank estimate into exact equality. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Uniform finite determination of zero, constant and idempotent jets, and its fixed-group application. |
| argument | [Argument](#argument) | Cyclic and triangular truncations, bounded cokernel dimension, closed rank sublevels and two doubled realizations. |
| dependency | [Rank sublevels](Yin_C_A0128_v1.md#statement) | Zariski closedness in all scalar parameter coordinates. |
| dependency | [Laurent evaluation](Yin_C_A0143_v1.md#statement) | Generic fiber rank and injective central evaluation. |
| dependency | [Constant series](Yin_C_A0141_v1.md#descent-of-a-constant-series) | Descent to the original division closure. |
| dependency | [Exact lifting](Yin_C_A0147_v1.md#statement) | Recovery of the rational kernel projection from any idempotent lift. |
| dependency | [Finite jets](Yin_C_A0146_v1.md#constant-terms-at-finite-order) | Unbounded-format approximants at each order. |
| dependency | [Finite-rank equation](Yin_C_A0131_v1.md#which-rationality-is-detected) | The original fixed-group kernel-projection equivalence. |
| review | [Finite determination](../audits/reviews/Yin_R_A0170_v1.md#finite-determination) | Independent review of the complete statement and argument. |

## Current assessment

[Selected decision](#decision-bounded-realizations)

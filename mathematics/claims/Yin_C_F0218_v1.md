---
author: Yin
---
# Attained least vacuum norm for univalent holomorphic changes of a circular generator

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(c\) be a standard circular generator, \(M=W^*(c)\), \(H=L^2(M,\tau)\), \(\Omega=1\), and \(G=H\otimes_2H\) with outer actions.
Use inner products linear in the second variable, and let \(\rho(b)h=hb\).
Suppose \(f\) is holomorphic and injective on \(|z|<R\) for some \(R>1\).
Impose the explicit inverse-approximation hypothesis that for some \(1<r<R\) there are polynomials \(q_j\) with \(q_j(f(z))\to z\) uniformly on \(|z|\le r\).
Write \(Z=f(c)\), \(a=f(0)\), \(b=f'(0)\ne0\), and
\[
 g(z,w)=\frac{z-w}{f(z)-f(w)}=\sum_{m,n\ge0}g_{mn}z^m w^n,
 \qquad U_g=\sum_{m,n\ge0}g_{mn}c^m\otimes c^n .
\]
The diagonal is filled by \(1/f'(z)\).
Let \(d_x,d_y\) denote the outer word cuts at \(Z,Z^*\) on the represented star-polynomial core, and put \(H_{\rm hol}=\overline{\mathbb C[c]}^{\,H}\).

1. \(W^*(Z)=M\), both cuts are actual closable derivations with adjoint vacua, and there is a bounded operator on \(H\) with \([Z,D]=P_\Omega\).
   In particular each fixed law has both full domains in the [Task's sense](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
2. The closed kernel of \(d_y\) is \(H_{\rm hol}=\overline{\mathbb C[Z]}^{\,H}\).
   Among all actual ACSY witnesses with arbitrary starred value, the least vacuum norm is exactly \(1/|b|\).
   The vector \(c/\overline b\) occurs as an actual vacuum and uniquely minimizes its norm.
3. Write \(\beta(Z)\) for the infimum of the norms of linear \(E:M\to H\) satisfying \([E,L_Z]=P_\Omega\) on all of \(M\), with arbitrary \(E1\).
   Every such bounded \(E\) satisfies
   \[
       E(ch)-cE(h)=\Theta U_g(h),\qquad
       \Theta U_g(h)=\sum_{m,n\ge0}g_{mn}c^m\tau(c^n h)
       \quad(h\in M).
                                                              \tag{1}
   \]
   In particular, with \(\|\cdot\|_\infty\) the actual operator norm and \((t_n)\) any finitely supported complex sequence,
   \[
     2\|c\|_\infty\beta(Z)\left\|\sum_n t_n(c^*)^n\right\|_\infty
         \ \ge\
           \left(\sum_{m\ge0}\left|\sum_n g_{mn}t_n\right|^2\right)^{1/2}.
                                                              \tag{2}
   \]
   More generally \(2\|c\|_\infty\beta(Z)\ge\|\Theta U_g:M\to H\|\).
   These are necessary estimates on each law.

## Argument

### Convergent power series and simultaneous commutators

In the [circular Fock model](Yin_C_F0074_v1.md#argument), take orthonormal letters \(u,v\) for which \(c=\ell(u)+\ell(v)^*\) and \(c^*=\ell(v)+\ell(u)^*\).
Then \(c^n\Omega=u^{\otimes n}\) and \((c^*)^n\Omega=v^{\otimes n}\).
Since \(\ell(v)^*\ell(u)=0\), expanding \(c^n\) gives just the \(n+1\) terms \(\ell(u)^j(\ell(v)^*)^{n-j}\), so \(\|c^n\|_\infty\le n+1\).
The conjugate bound holds for \(c^*\).
Cauchy estimates on a disk or bidisk of radius strictly between one and \(R\) give exponentially decaying Taylor coefficients for \(f\), its divided difference \(D_f(z,w)=(f(z)-f(w))/(z-w)\), and \(g\).
Indeed \(D_f\) is jointly holomorphic, including its diagonal, and has no zeros there by injectivity and \(f'\ne0\).
All series below involving these coefficients and powers of \(c,c^*\) are absolutely convergent under the bounds just obtained.
The assumed uniform convergence implies \(q_j(Z)\to c\) in operator norm by applying the Cauchy coefficient bound on a circle of radius greater than one to \(q_j\circ f-z\).
This gives \(W^*(Z)=M\).
The same approximations imply that every \(c^n\) is an operator-norm limit of polynomials in \(Z\), and \(f(c)\) itself is an operator-norm limit of polynomials in \(c\).
Thus the two closed analytic spans in the statement agree and the represented star core for \(Z\) is Hilbert dense.

Let \(R_u=r(u)^*\) be the norm-one right deletion, with \([R_u,L_c]=P_\Omega\) and \([R_u,L_{c^*}]=0\) from the same circular construction.
Put
\[
 B_g=\sum_{m,n\ge0} g_{mn}\rho(c^m)R_u\rho(c^n)\in\mathcal B(H).
\]
Absolute operator-norm convergence follows from \(\sum_{m,n}|g_{mn}|(m+1)(n+1)<\infty\).
Right multiplication commutes with left multiplication, hence \([B_g,L_c]=\Theta U_g\), \([B_g,L_{c^*}]=0\), where \(\Theta(s\otimes t)h=s\tau(th)\) is the coarse-to-Hilbert--Schmidt unitary.
Expanding the commutator with \(Z=f(c)\) multiplies the bivariate series \(g\) by \(D_f\), since an outer left power of \(c\) adds to the first exponent and an outer right power to the second.
The expansions converge absolutely also in the Hilbert--Schmidt norm by the exponential bounds.
As \(gD_f=1\), this gives \([B_g,L_Z]=P_\Omega\) and \([B_g,L_{Z^*}]=0\).
Hence \(D=-B_g\) supplies the generator-first dual with both domains equal to \(H\).

For represented star polynomials \(p\), \(d_xp=\Theta^{-1}[B_g,L_p]\) by the product rule, including descent through represented relations.
Its vacuum pairing equals \(\langle B_g^*\Omega-(B_g\Omega)^*,p\rangle\), yielding an actual vacuum \(\xi_0\).
The opposite cut is likewise \(d_yp=\Theta^{-1}[-B_g^*,L_p]\), by taking the two adjoint commutators.
Both operators are closable since for either cut the adjoint domain contains \(s^*\otimes t^*\) for every pair of core elements \(s,t\).
Indeed the pairing of \(s(d p)t\) with the unit tensor is the vacuum pairing on \(spt\) minus the two terms containing \((d s)pt\) and \(sp(d t)\), each bounded by a fixed constant times \(\|p\|_2\) by moving outer multipliers onto the unit tensor.
The tested tensors span a dense subspace of \(G\).

### The circular starred cut and attainment

Let \(W(w)\) be the Wick polynomial whose vacuum vector is a tensor word in \(u,v\), with \(W(\varnothing)=1\).
The Fock recursion is \(W(iw)=s_i W(w)-\langle\bar i,w_1\rangle W(w_2\cdots)\), where \(s_u=c,\ s_v=c^*\), \(\bar u=v,\ \bar v=u\), and the contraction term is absent for the empty word.
It follows by applying \(s_i\) to the word vector and using that \(\Omega\) is separating.
For the cut \(\partial_v\) at \(c^*\), killing \(c\), this recursion and the product rule give
\[
             \partial_v W(w)=\sum_{w=A v B}W(A)\otimes W(B).
\]
Indeed the leading-letter cut gives \(1\otimes W(w)\) when the new letter is \(v\), and the old prefix cuts give \(W(iA)\otimes W(B)\) by the same recursion, with the contracted tails cancelled by differentiating the recursion's subtraction.
Distinct pairs \((A,B)\) reconstruct the word \(AvB\), and different cuts within that word have different prefix lengths.
For any finite Wick expansion \(h=\sum_w h_w W(w)\) it follows that
\[
       \|\partial_v h\|_2^2=\sum_w \#_v(w)|h_w|^2
                       \ge \|h-P_{\rm hol}h\|_2^2.                \tag{3}
\]
Here \(P_{\rm hol}\) projects onto the span closure of all \(u\)-only words.
In particular the cut is closable by the orthogonal formula, and (3) persists on its closed graph.

Put \(f^\#(z)=\overline{f(\bar z)}\) and write \(D_{f^\#}=\sum s_{mn}z^m w^n\).
On \(G\) use the bounded operator
\[
          T(A\otimes B)=\sum_{m,n\ge0}s_{mn} A(c^*)^m\otimes(c^*)^n B .
\]
Right and left multiplication here have norms bounded by the respective power norms, so the same exponential estimate gives boundedness.
Every star polynomial \(p=p(Z,Z^*)\) is in \(\operatorname{Dom}\overline{\partial_v}\) and
\[
                     \overline{\partial_v}p=T d_y p .              \tag{4}
\]
For this, truncate the power series of \(f(c)\), \(f^\#(c^*)\) and their differences in both operator norm and coarse norm of the cut, using \(\partial_v c=0,\ \partial_v c^*=1\otimes1\).
The bounded outer factors and the finite product rule then give graph convergence for \(p\), and insertion at its starred letters is exactly (4).
Equations (3) and (4) give \(\|p-P_{\rm hol}p\|_2\le\|T\|\|d_yp\|_2\).
Passing to graph limits proves \(\ker\overline{d_y}\subseteq H_{\rm hol}\).
The opposite inclusion follows from closedness and the analytic span equality, since \(d_y\) kills polynomials in \(Z\).

The trace of any analytic polynomial \(p(Z)\) is \(p(a)\) by orthogonality of the circular powers and their norm-convergent expansions.
Hence \((\tau\otimes\tau)d_x p(Z)=p'(a)\) by the monomial derivative formula.
The coefficient of \(c\) in \(p(f(c))\) is \(bp'(a)\), so the projection of \(\xi_0\), and of any actual vacuum, onto \(H_{\rm hol}\) is \(\zeta=c/\overline b\).
Thus \(\|\zeta\|_2=1/|b|\) is a lower bound.
For every core element, (3)--(4) give
\[
   |\langle\zeta-\xi_0,p\rangle|
        \le\|\zeta-\xi_0\|_2\|T\|\|d_y p\|_2 .
\]
The left side without absolute values consequently defines a bounded functional on the range of \(d_y\), which Riesz representation on the closure extends as \(\langle L,d_y p\rangle\) for some \(L\in G\).
Choose the starred value \(K=L^\sharp\), where \(\sharp\) takes componentwise adjoints.
The [word-cut identity and represented-quotient descent](Yin_C_F0201_v1.md#argument) now give an actual normalized derivation with starred value \(K\) and vacuum \(\zeta\) on the whole core.
The fixed holomorphic projection forces uniqueness of the minimizing vector by orthogonality.

### The forced two-variable kernel on bounded inputs

Define \(h_j(z)=q_j(f(z))\).
On each smaller closed bidisk of radius \(r'\) with \(1<r'<r\), \(D_{h_j}\to1\) uniformly by Cauchy's derivative estimate on the larger disk and the line-segment formula for the divided difference.
Therefore
\[
       D_{q_j}(f(z),f(w))=g(z,w)D_{h_j}(z,w)\longrightarrow g(z,w)
\]
uniformly there.
The bivariate coefficient bounds on that bidisk, multiplied by \((m+1)(n+1)\) and summed, show that evaluating these series with tensor powers \(c^m\otimes c^n\) gives convergence in the coarse norm to \(U_g\).
For any bounded witness \(E:M\to H\), the exact polynomial commutator \([E,L_{q_j(Z)}]\) on \(M\) is the action of \(\Theta\) on the evaluated tensor \(D_{q_j}(Z,Z)\), by repeated use of \([E,L_Z]=P_\Omega\).
The Hilbert--Schmidt convergence gives convergence on every \(h\in M\).
On the left, \(E(q_j(Z)h)\to E(ch)\) by operator-norm convergence and boundedness \(M\to H\), and \(q_j(Z)E(h)\to cE(h)\) by bounded left multiplication.
This proves (1) on the entire bounded-input domain.
The estimate of the commutator in that norm is at most \(2\|c\|_\infty\|E\|\).
Inserting \(h=\sum_n t_n(c^*)^n\) in (1) uses \(\tau(c^j(c^*)^n)=\delta_{jn}\), and the output powers \(c^m\) are orthonormal in \(H\).
Taking the infimum gives (2), including the single-column tests and all their finite linear combinations.
These lower bounds do not establish divergence of the costs for a family normalized by \(f'(0)=1\).

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T14:39 |
| status | open |
| reason | The exact attained vacuum, both closed cuts, fixed-law bounded dual and forced bounded-input tests are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Single circular univalent change with explicit inverse approximation, exact least vacuum and bounded-dual tests. |
| argument | [Argument](#argument) | Summable series, simultaneous commutators, Wick marked-letter formula, kernel, attaining correction and inverse transport on all bounded inputs. |
| dependency | [Circular Fock construction](Yin_C_F0074_v1.md#argument) | Standard circular normalization, faithful tracial Fock representation, right deletion commutators and coarse Hilbert--Schmidt identification. |
| dependency | [Actual word descent](Yin_C_F0201_v1.md#argument) | Starred-value pairing with componentwise adjoints and descent of all scalar tests through represented relations. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T15:09 |
| status | proved |
| reason | Adopt the attained least vacuum and the forced kernel tests for this class of univalent circular changes. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Single circular univalent change with explicit inverse approximation, exact least vacuum and bounded-dual tests. |
| argument | [Argument](#argument) | Summable series, simultaneous commutators, Wick marked-letter formula, kernel, attaining correction and inverse transport on all bounded inputs. |
| dependency | [Circular Fock construction](Yin_C_F0074_v1.md#argument) | Standard circular normalization, faithful tracial Fock representation, right deletion commutators and coarse Hilbert--Schmidt identification. |
| dependency | [Actual word descent](Yin_C_F0201_v1.md#argument) | Starred-value pairing with componentwise adjoints and descent of all scalar tests through represented relations. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0226_v1.md#whole-proof-finding) | Bounded commutators, actual cuts and vacuum, inverse approximation, kernel, attained minimum and all-witness lower tests. |

---
author: Yin
---
# A bounded circular direct-sum dual with infinite mixed Hilbert--Schmidt energy

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(c=(S_1+\mathrm i S_2)/\sqrt2\) be the standard circular generator from a variance-one free semicircular pair.
For \(n\ge1\) take two copies of its tracial von Neumann algebra, with respective generators
\[
 X_{n,0}=\lambda_{n,0}+r_n c,\qquad X_{n,1}=\lambda_{n,1}+r_n c,\qquad
 \lambda_{n,0}=2^{-n},\quad\lambda_{n,1}=2^{-n}+2r_n(1+\varepsilon_n),
 \quad r_n=4^{-n}/32,\quad \varepsilon_n=16^{-n}.
\]
Give each copy weight \(t_n=(3/2)4^{-n}\) times its normalized trace, so the product algebra \(M\) has probability trace \(\tau\).
Let \(X=(X_{n,j})\in M\), \(H=L^2(M,\tau)\), \(\Omega=1\), and \(P_\Omega h=\tau(h)1\).
Then \(X\) is a nonnormal generator of \(M\), satisfies the [actual ACSY condition](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct), and has a bounded operator \(D\) on all of \(H\) with \([L_X,D]=P_\Omega\).
In particular its bare and strong full-domain dual conditions both hold.

Write \(H_a\) for the central summand indexed by \(a=(n,j)\) with its inherited Hilbert norm, and \(D_{ab}:H_b\to H_a\) for the blocks of any bounded whole-Hilbert-space dual.
For \(a\ne b\), each \(D_{ab}\) is uniquely forced and is Hilbert--Schmidt.
Nevertheless
\[
 \sum_{a\ne b}\|D_{ab}\|_{\rm HS}^2=\infty .
\]
Even the sum over the two ordered off-diagonal blocks within each pair diverges.
Thus finite total mixed Hilbert--Schmidt energy is unnecessary for a bounded Hilbert-space dual in this infinite central decomposition.

## Argument

### Spectral separation and generation

Use the [standard circular Fock model and bounded dual](Yin_C_F0074_v1.md#argument).
In that model \(c=A+B\), where \(A=\ell_u\), \(B=\ell_v^*\) and \(u=(e_1+\mathrm i e_2)/\sqrt2,\ v=(e_1-\mathrm i e_2)/\sqrt2\) are orthogonal unit vectors.
Since \(BA=0\), \(c^k=\sum_{h=0}^k A^hB^{k-h}\) and \(\|c^k\|\le k+1\).
In particular its spectrum lies in the closed unit disk and \(\|c\|\le2\).
The two sequences \(c^k\Omega=u^{\otimes k}\) and \((c^*)^k\Omega=v^{\otimes k}\), each including the vacuum, are separately orthonormal.
Let \(D_c\) be the bounded Fock dual with \([L_c,D_c]=P_\Omega\) and \([L_{c^*},D_c]=0\) for the intrinsic normalized trace.

Put \(r_a=r_n,\ t_a=t_n,\lambda_a=\lambda_{n,j}\).
The two spectral disks of each pair are disjoint by their prescribed gap \(2r_n\varepsilon_n\).
For \(a=(n,j), b=(k,l)\) with \(k>n\),
\[
 |\lambda_a-\lambda_b|-r_a-r_b\ \ge\ 2^{-n}-2^{-k}-r_n-5r_k
 \ge\ 2^{-n}/4 .
\]
Here the center displacement in level \(k\) is at most \(4r_k\), and \(r_k\le r_n/4,\ r_n\le2^{-n}/64\).
Each disk is isolated from all the other disks and from their only possible accumulation point \(0\).
Outside their union and \(0\), the corner resolvents are uniformly bounded because the norms of the tail generators tend to zero.
Hence the Riesz contour around an individual disk belongs to the resolvent set of \(X\) and gives its central unit \(e_a\) in \(W^*(X)\).
Each \(e_aX\) generates the corresponding corner and finite partial sums of bounded corner elements converge strongly to their bounded product element.
Thus \(W^*(X)=M\), and any one circular corner proves nonnormality.

### The unique mixed block

Use normalized Hilbert spaces within each factor when computing the following tensors.
For \(a\ne b\) set \(\Delta=\lambda_a-\lambda_b\), and use \(c_a,c_b\) to distinguish the copies of \(c\).
Define
\[
 \eta_{ab}=\sum_{m,n\ge0}h_{mn}\,c_a^m\otimes c_b^n,\qquad
 h_{mn}=\frac{(-1)^m}{\Delta^{m+n+1}}
             \binom{m+n}{m} r_a^m r_b^n .
\]
All ordered pairs satisfy \(|\Delta|> r_a+r_b\).
At a fixed degree \(k=m+n\) the absolute sum of coefficients is \((r_a+r_b)^k/|\Delta|^{k+1}\).
Since the displayed tensors are orthonormal this proves convergence in the intrinsic Hilbert tensor norm and the estimate \(\|\eta_{ab}\|_2\le(|\Delta|-r_a-r_b)^{-1}\).
Substitution in the series, or multiplication of its geometric sum, gives \(X_a\eta_{ab}-\eta_{ab}X_b=e_a\otimes e_b\).
Indeed at positive degrees the coefficient recurrence is \(\Delta h_{mn}+r_a h_{m-1,n}-r_b h_{m,n-1}=0\), with negative subscripts zero, and \(\Delta h_{00}=1\).

Use the ambient rank-one identification \(\Theta_\tau(g\otimes h)v=g\tau(hv)\) of the [two-corner gluing argument](Yin_C_F0206_v1.md#argument).
In the inherited spaces the tensor gives a Hilbert--Schmidt map \(T_{ab}=\Theta_\tau(\eta_{ab}):H_b\to H_a\) with
\[
 L_{X_a}T_{ab}-T_{ab}L_{X_b}=(P_\Omega)_{ab},\qquad
 \|T_{ab}\|_{\rm HS}^2=t_at_b\sum_{m,n}|h_{mn}|^2 .
\]
Under unitary identification with normalized Hilbert spaces the operator has factor \(\sqrt{t_at_b}\) multiplying the matrix \((h_{mn})\), from the orthonormal input vectors \((c_b^*)^n\) to the orthonormal output vectors \(c_a^m\), with value zero on the perpendicular input space.
Any two bounded solutions differ by a bounded \(U\) intertwining \(L_{X_b}\) and \(L_{X_a}\).
The two resolvents therefore intertwine in the common resolvent set.
Integrating around the \(a\) disk, which excludes the \(b\) spectrum, gives \(U=0\).
In particular every bounded dual on the whole space has these mixed blocks.

### Diverging squared Hilbert--Schmidt norms and a bounded operator sum

For a pair within one level put \(r=r_n,\ t=t_n,\ \varepsilon=\varepsilon_n,\ d=|\Delta|=2r(1+\varepsilon)\).
Summing the squared coefficients by homogeneous degree yields
\[
 \sum_{m,l}|h_{ml}|^2
 =d^{-2}\sum_{k\ge0}\binom{2k}{k}(r/d)^{2k}
 =\frac{1}{d\sqrt{d^2-4r^2}} .
\]
The first equality uses \(\sum_{m=0}^k\binom{k}{m}^2=\binom{2k}{k}\).
Thus each of the two ordered blocks has squared Hilbert--Schmidt norm
\[
 \frac{(t/r)^2}{4(1+\varepsilon)\sqrt{2\varepsilon+\varepsilon^2}} .
\]
Here \(t/r=48\) and \(\varepsilon_n\downarrow0\), so their sum diverges.

For a fixed \(m\), the absolute row sum of the unscaled matrix is
\[
 \sum_{l\ge0}|h_{ml}|
 =\frac{1}{d-r}\left(\frac{r}{d-r}\right)^m
 \le\frac1{d-r}.
\]
The same bound holds for the column sums.
Cauchy--Schwarz in the weighted row sums followed by summation over columns gives the same upper bound for its \(\ell^2\) operator norm.
Consequently \(\|T_{ab}\|\le t/(d-r)\le48\).
These within-level blocks act as a direct sum of bounded two-by-two off-diagonal operators and have a bounded sum.

For different levels \(k>n\), the separation estimate gives \(\|T_{ab}\|_{\rm HS}^2\le16\,t_nt_k4^n\).
Including both orders and both copies in each level adds only a constant factor.
The double sum is finite since \(t_n4^n=3/2\) and \(\sum_{k\ge1}k t_k<\infty\).
The different-level part therefore defines one Hilbert--Schmidt operator.
On each diagonal put \(D_{aa}=(t_a/r_a)D_c\), of uniformly bounded operator norm.
Its commutator is \(t_a\) times the intrinsic vacuum projection, exactly \((P_\Omega)_{aa}\).
Adding the diagonal, within-level and different-level operators defines \(D\in B(H)\).
All block identities give \([L_X,D]=P_\Omega\) by density of finite-support vectors.

### The actual starred derivation and its vacuum

The diagonal of \([L_{X^*},D]\) vanishes by the Fock identity \([L_{c^*},D_c]=0\).
The commutator with the different-level part is Hilbert--Schmidt since that part is Hilbert--Schmidt and \(X^*\) is bounded.
Within one level we have
\[
 \|L_{X_a^*}T_{ab}-T_{ab}L_{X_b^*}\|_{\rm HS}
 \le(d+4r)\|T_{ab}\|_{\rm HS}.
\]
For \(0<\varepsilon\le1\) the squared right side is bounded by a fixed constant times \(t_n^2/\sqrt{\varepsilon_n}\).
The series of these bounds converges since \(t_n^2/\sqrt{\varepsilon_n}=(9/4)4^{-n}\).
It follows that \([L_{X^*},D]\) is Hilbert--Schmidt on the whole space.

For each represented star polynomial \(w\) define
\[
 \delta(w)=\Theta_\tau^{-1}([L_w,D]).
\]
This is defined for every star word by the two Hilbert--Schmidt generator commutators and Leibniz, is complex-linear on the represented algebra, and obeys the outer product rule by the bimodule property of \(\Theta_\tau\).
Since \([L_X,D]=P_\Omega\), we have \(\delta X=1\otimes1\).
With inner products linear in the second variable the vacuum pairing is
\[
 \langle1\otimes1,\delta w\rangle
    =\langle\Omega,[L_w,D]\Omega\rangle
    =\langle (D\Omega)^*-D^*\Omega,\,w\Omega\rangle .
\]
The last identity uses the tracial involution on \(H\) and \(\langle\Omega,wD\Omega\rangle=\tau(wD\Omega)\).
The displayed vector belongs to \(H\) because \(D\) is bounded, and the represented star algebra is Hilbert dense by generation.
This proves the actual adjoint-domain condition on the entire required core.

## Provenance and scope

This example tests the infinite direct-sum route for [T_F0011](../tasks/Yin_T_F0011_v1.md#contract).
The two-corner argument supplies the mixed Sylvester equation and the intrinsic-to-ambient trace factors.
In the present example the disk separation, block series and its distinct Hilbert--Schmidt and operator-norm estimates determine what happens when the number of corners is infinite.
The example has a finite operator-norm-to-Hilbert full-domain dual bound and leaves the unrestricted implication from actual ACSY to a bare full-domain dual open.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T13:36 |
| status | open |
| reason | The shrinking circular pairs, forced mixed-block divergence and actual global witnesses are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Countable nonnormal direct sum with actual ACSY and a bounded whole-space dual, but divergent forced mixed Hilbert--Schmidt energy. |
| argument | [Argument](#argument) | Spectral isolation, explicit coefficient matrix, uniqueness, two distinct block norms, bounded assembly, starred commutator and actual vacuum. |
| dependency | [Circular Fock construction](Yin_C_F0074_v1.md#argument) | Standard normalized circular operator, creation and deletion formulas, and bounded intrinsic dual with zero adjoint-generator commutator. |
| dependency | [Central corner gluing](Yin_C_F0206_v1.md#argument) | Ambient mixed rank-one identification and the normalized-versus-inherited weights in the Sylvester equations. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T13:48 |
| status | proved |
| reason | Adopt the countable circular example and forced mixed-block divergence after independent whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Countable nonnormal direct sum with actual ACSY and a bounded whole-space dual, but divergent forced mixed Hilbert--Schmidt energy. |
| argument | [Argument](#argument) | Spectral isolation, explicit coefficient matrix, uniqueness, two distinct block norms, bounded assembly, starred commutator and actual vacuum. |
| dependency | [Circular Fock construction](Yin_C_F0074_v1.md#argument) | Standard normalized circular operator, creation and deletion formulas, and bounded intrinsic dual with zero adjoint-generator commutator. |
| dependency | [Central corner gluing](Yin_C_F0206_v1.md#argument) | Ambient mixed rank-one identification and the normalized-versus-inherited weights in the Sylvester equations. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0215_v1.md#finding) | Complete proof of the bounded dual, actual vacuum, unique mixed blocks and divergent Hilbert–Schmidt energy, with both direct inputs. |

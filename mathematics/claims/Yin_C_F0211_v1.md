---
author: Yin
---
# Optimal normal densities and weighted rank-one commutators for normal coordinate duals

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_n)\) be bounded normal generators of a finite von Neumann algebra \((M,\tau)\) with faithful normal probability trace, satisfying the actual starred ACSY hypothesis of [F0011](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
Fix \(i\), write \(H=L^2(M,\tau)\), \(\Omega=1\), \(P=\mathbb C\langle X,X^*\rangle\), \(B=C^*(X)\), and put \(E_0=(\mathrm{id}\otimes\tau)\delta_i:P\to H\) for the canonical right slice.
Use \(L_a\) for left multiplication and the Hilbert inner product linear in its second variable.
Let \(c=c_i(X)\) be the least constant in the [finite column estimate](Yin_C_F0208_v1.md#statement)
\[
   \sum_k\|E_0p_k\|_2^2\ \le\ c^2\left\|\sum_kp_k^*p_k\right\|
   \qquad(p_k\in P),
\]
with \(c=+\infty\) if there is no finite bound.

If \(c<\infty\), every state \(\varphi\) on \(B\) giving the optimal bound \(\|E_0p\|_2^2\le c^2\varphi(p^*p)\) is the restriction of a normal state on \(M\).
Such states exist.
Write \(\varphi(a)=\tau(da)\) for the unique normal extension, with \(d\in L^1(M)_+\) and \(\tau(d)=1\).
Each such \(d\) is faithful and satisfies
\[
          \tau(d^{-1})\le 4c^2\inf_{\lambda\in\mathbb C}\|X_i-\lambda1\|^2.
          \tag{1}
\]

Equivalently, \(c\) is the infimum of \(\|T\|_{\mathcal B(H)}\) over positive affiliated \(d\) with \(\tau(d)=1\), full support and \(d^{-1}\in L^1(M)\), and bounded \(T:H\to H\) satisfying
\[
   T\sqrt d=0,\qquad
   [T,L_{X_j}]=\delta_{ij}\,|\Omega\rangle\langle d^{-1/2}|
   \quad(1\le j\le n).                                                   \tag{2}
\]
Here the rank-one operator sends \(z\) to \(\langle d^{-1/2},z\rangle\Omega\).
The empty infimum is \(+\infty\), and the finite infimum is attained.
Each optimal density gives a unique such \(T\) that implements \(E_0(p)=T(p\sqrt d)\) for every \(p\in P\), and its norm is \(c\).
Every pair satisfying (2) implements the canonical right slice on this entire represented starred core.

Put \(N_i=W^*(X_j:j\ne i)\), with \(N_i=\mathbb C1\) for a single generator.
For arbitrary \(b_k\in N_i\), radii \(r_k>0\), and \(e_k=1_{[0,r_k]}(|X_i-b_k|)\), any finite family of pairwise orthogonal \(e_k\) satisfies
\[
              \sum_k\frac{\tau(e_k)^3}{r_k^2}\le 4c^2.                  \tag{3}
\]
For finite \(c\) each optimal \(d\) satisfies \(\tau(de_k)\ge \tau(e_k)^3/(4c^2r_k^2)\) individually.
Thus unbounded sums over such finite families for one fixed tuple and coordinate imply that the two-free-Haar enlargement in [C_F0208](Yin_C_F0208_v1.md#statement) satisfies ACSY and has no bare full-domain system.

## Argument

### Removing the singular part of an optimal state

Assume \(c<\infty\).
Since \(E_0(X_i)=1\), the optimal constant is positive.
The singleton bound extends \(E_0\) continuously to \(E_B:B\to H\) in the operator norm, with \(\|E_B\|\le c\).
[C_F0208](Yin_C_F0208_v1.md#statement) supplies an optimal state, and we take any such state \(\varphi\).
Continuity gives its domination on all of \(B\).

Let \(\pi:B^{**}\to M\) be the normal extension of the tracial representation.
By the [universal bidual and central summand theorem](../audits/literature/Bla06/Yin_U002.md#bla06-u002), its kernel is \((1-e)B^{**}\) for a central projection \(e\), and \(j:M\to eB^{**}\) is the inverse of its restriction to that summand.
The bounded map \(E_B^{**}:B^{**}\to H\) is ultraweak-to-weak continuous by reflexivity.
The actual ACSY vacuum gives a densely defined Hilbert adjoint \(E_0^*\) by [ACSY24, Theorem 3.4](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001).
For \(h\in\operatorname{Dom}E_0^*\) the pairing \(\langle h,E_B b\rangle=\langle E_0^*h,b\Omega\rangle\) first holds on \(P\) and extends by operator-norm continuity to \(B\).
The right side is a vector functional in the tracial representation, so its normal extension to \(B^{**}\) vanishes on \(\ker\pi\).
Testing against the dense domain of \(E_0^*\) proves that \(E_B^{**}\) annihilates the entire summand \((1-e)B^{**}\).
Thus \(E=E_B^{**}j:M\to H\) is normal and agrees with \(E_B\) on \(B\).

Let \((\pi_\varphi,K_\varphi,v_\varphi)\) be the GNS representation of \(\varphi\).
Domination gives a bounded map \(S:K_\varphi\to H\) of norm at most \(c\) by \(S\pi_\varphi(b)v_\varphi=E_B b\).
Extending \(\pi_\varphi\) normally to \(B^{**}\), the formula \(E_B^{**}(x)=S\pi_\varphi^{**}(x)v_\varphi\) holds everywhere by ultraweak-to-weak continuity and density.
Writing \(\widehat\varphi\) for the vector state on \(B^{**}\), we obtain
\[
             \|E a\|_2^2\le c^2\widehat\varphi(j(a^*a))\quad(a\in M).
\]
The functional on the right before multiplication by \(c^2\) is a normal positive functional of mass \(m=\widehat\varphi(e)\le1\).
If \(m=0\) then \(E(X_i)=0\), contrary to \(E_0(X_i)=1\).
If \(0<m<1\), division by \(m\) would give a state on \(M\) whose restriction to \(B\) dominates \(E_0\) with the smaller constant \(c\sqrt m\), contradicting the optimality in C_F0208.
Hence \(\widehat\varphi(1-e)=0\), and positivity makes \(\widehat\varphi\) vanish on \((1-e)B^{**}\).
Consequently the restriction of \(\widehat\varphi j\) to \(B\) is the original \(\varphi\).
The normal extension is unique by ultraweak density, and the [finite tracial predual identification](../audits/literature/AP18/Yin_U003.md#ap18-u003) gives its positive density \(d\) of trace one.
We have proved \(\|E a\|_2\le c\|a\sqrt d\|_2\) on all \(M\).

### Faithfulness, inverse integrability and the bounded implementer

The identities \(E(1)=0\) and \([E,L_{X_j}]a=\delta_{ij}\tau(a)\Omega\) hold on \(P\) by Leibniz and extend to \(M\) by separate ultraweak continuity of bounded multiplication and normality of \(E\).
Subtract any scalar \(\lambda1\) from \(X_i\) in this commutator and use domination in both terms.
For all \(a\in M\) this gives
\[
       |\tau(a)|\le 2c\|X_i-\lambda1\|\,\|a\sqrt d\|_2.
\]
Set \(a=(d+\varepsilon1)^{-1}\) for \(\varepsilon>0\).
Then \(\|a\sqrt d\|_2^2=\tau(d(d+\varepsilon1)^{-2})\le\tau(a)\).
Since \(\tau(a)>0\), the preceding estimate implies \(\tau((d+\varepsilon1)^{-1})\le4c^2\|X_i-\lambda1\|^2\).
Monotone convergence as \(\varepsilon\downarrow0\) rules out a nonzero kernel of \(d\) and proves (1).

The space \(M\sqrt d\) is dense in \(H\).
Indeed, for \(a\in M\) the vectors \(a1_{[1/m,m]}(d)=(a1_{[1/m,m]}(d)d^{-1/2})\sqrt d\) are in that space and converge in \(H\) to \(a\).
Define \(T(a\sqrt d)=Ea\).
The domination estimate gives well-definedness and a unique bounded extension to \(H\) of norm at most \(c\).
Its norm is at least \(c\), since its norm together with the state of density \(d\) gives a column bound by summation on \(P\).
The subspace \(P\sqrt d\) is dense as well, since its closure contains \(a\sqrt d\) for every \(a\in M\) by strong density of the represented algebra \(P\) in \(M\).
Thus implementation on \(P\) already determines \(T\) for this density.
The normalization gives \(T\sqrt d=0\).
Moreover \(\langle d^{-1/2},a\sqrt d\rangle=\tau(a)\), by multiplying with the spectral truncations \(1_{[1/m,m]}(d)\) inside the trace, using traciality there and taking \(L^2\) limits of both square-root vectors.
The full-domain commutators of \(E\) give (2) on the dense \(M\sqrt d\), and all operators in (2) are bounded on \(H\).

Conversely, take a pair \((d,T)\) satisfying (2) and set \(F(a)=T(a\sqrt d)\) for \(a\in M\).
Then \(F\) is a bounded map from the operator norm to \(H\), satisfies \(F(1)=0\), and has \([F,L_{X_j}]a=\delta_{ij}\tau(a)\Omega\) on every bounded input by the same trace identity.
The [single-coordinate commutator argument in C_F0070](Yin_C_F0070_v1.md#statement-and-interfaces) forces the inhomogeneous normal-phase commutator with \(X_i^*\) and zero commutators with the other \(X_j^*\).
By [C_F0076, Part 1](Yin_C_F0076_v1.md#statement) these are the starred derivatives of the present ACSY system under the Hilbert–Schmidt commutator identification of ACSY24 Theorem 3.4.
Consequently \(F\) and \(E_0\) have the same generator and adjoint-generator commutators on \(P\).
Their values at \(1\) are both zero, so induction on word length gives equality on \(P\).
For every finite column there,
\[
  \sum_k\|E_0p_k\|_2^2\le \|T\|^2\sum_k\|p_k\sqrt d\|_2^2
  =\|T\|^2\tau\!\left(d\sum_kp_k^*p_k\right)
  \le\|T\|^2\left\|\sum_kp_k^*p_k\right\|.
\]
This proves the converse, the infimum assertion and its attainment at a finite value.

### Compression by small singular-value projections

Fix an optimal pair and set \(L=X_i-b\) for \(b\in N_i\).
For \(j\ne i\), (2) gives commutation of \(T\) with \(L_{X_j}\).
It also gives commutation with \(L_{X_j^*}\) by Fuglede's theorem for bounded operators and normal \(L_{X_j}\).
Equivalently the homogeneous bounded-map argument of C_F0070 applies to the bounded map \(T|_M:M\to H\), and density then extends the resulting identity to \(H\).
Hence \(T\) commutes with all left multipliers from \(N_i\) and \([T,L_L]=|\Omega\rangle\langle d^{-1/2}|\).

Put \(e_r=1_{[0,r]}(|L|)\) and \(f_r=1_{[0,r]}(|L^*|)\) for \(r>0\).
The polar decomposition identifies \(1-e_r\) with \(1-f_r\) by partial isometry, so \(s=\tau(e_r)=\tau(f_r)\).
Furthermore \(\|Le_r\|\le r\) and \(\|f_rL\|\le r\).
Compressing the commutator on the left by \(L_{f_r}\) and on the right by \(L_{e_r}\) gives
\[
    \sqrt s\,\|e_r d^{-1/2}\|_2
       =\big\|\,|f_r\Omega\rangle\langle e_r d^{-1/2}|\,\big\|
       \le 2c r .
\]
Cauchy–Schwarz yields \(s^2\le\|e_r\sqrt d\|_2^2\|e_r d^{-1/2}\|_2^2\), because the inner product of these two vectors is \(\tau(e_r)\) by the trace identity above and \(e_r^2=e_r\).
The case \(s=0\) is immediate, and in the other cases these inequalities give \(\tau(de_r)=\|e_r\sqrt d\|_2^2\ge s^3/(4c^2r^2)\).
For the asserted finite families, \(\sum_k e_k\le1\) and \(\sum_k\tau(de_k)\le\tau(d)=1\) prove (3).
C_F0208 then gives the stated implication for the enlarged tuple.
No commutation between \(b_k\) and \(X_i\), or between \(d\) and \(e_k\), is used.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T13:57 |
| status | open |
| reason | Fixed candidate giving optimal normality, a bounded weighted realization and a necessary mixed singular-value estimate for the one-sided column bound. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every optimal state, inverse bound, attained rank-one criterion, starred-core reconstruction and finite-family packing. |
| argument | [Argument](#argument) | Removal of the singular summand, domination on all bounded inputs, spectral truncation, both directions of (2) and correlated compression. |
| dependency | [Column and state criterion](Yin_C_F0208_v1.md#statement) | Optimal state attainment, exact column norm and the implication of an infinite norm for the two-free-Haar enlargement. |
| dependency | [Bidual central summand](../audits/literature/Bla06/Yin_U002.md#bla06-u002) | Extension of the represented algebra and of a state's GNS representation, the kernel summand and its normal complement. |
| dependency | [Canonical slice adjoint and commutators](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Theorem 3.4 supplies a dense actual adjoint domain and the Hilbert–Schmidt commutator determined by a generator derivative. |
| dependency | [Tracial predual](../audits/literature/AP18/Yin_U003.md#ap18-u003) | Positive normal functionals on the finite tracial algebra are exactly the positive integrable densities, with trace equal to functional norm. |
| dependency | [Individual starred commutators](Yin_C_F0070_v1.md#statement-and-interfaces) | Forced starred phase and homogeneous commutation for a single bounded map with the prescribed normal coordinate commutators. |
| dependency | [Normal ACSY phase](Yin_C_F0076_v1.md#statement) | Part 1 identifies the starred derivatives in the actual ACSY system used for comparison on the full core. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T14:05 |
| status | proved |
| reason | Optimal normal densities and weighted commutators give the exact column norm and mixed small-singular-value obstruction. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every optimal state, inverse bound, attained rank-one criterion, starred-core reconstruction and finite-family packing. |
| argument | [Argument](#argument) | Removal of the singular summand, domination on all bounded inputs, spectral truncation, both directions of (2) and correlated compression. |
| dependency | [Column and state criterion](Yin_C_F0208_v1.md#statement) | Optimal state attainment, exact column norm and the implication of an infinite norm for the two-free-Haar enlargement. |
| dependency | [Bidual central summand](../audits/literature/Bla06/Yin_U002.md#bla06-u002) | Extension of the represented algebra and of a state's GNS representation, the kernel summand and its normal complement. |
| dependency | [Canonical slice adjoint and commutators](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Theorem 3.4 supplies a dense actual adjoint domain and the Hilbert–Schmidt commutator determined by a generator derivative. |
| dependency | [Tracial predual](../audits/literature/AP18/Yin_U003.md#ap18-u003) | Positive normal functionals on the finite tracial algebra are exactly the positive integrable densities, with trace equal to functional norm. |
| dependency | [Individual starred commutators](Yin_C_F0070_v1.md#statement-and-interfaces) | Forced starred phase and homogeneous commutation for a single bounded map with the prescribed normal coordinate commutators. |
| dependency | [Normal ACSY phase](Yin_C_F0076_v1.md#statement) | Part 1 identifies the starred derivatives in the actual ACSY system used for comparison on the full core. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0219_v1.md#whole-proof-finding) | Optimal states, inverse integrability, the converse on the starred core and mixed spectral compressions. |

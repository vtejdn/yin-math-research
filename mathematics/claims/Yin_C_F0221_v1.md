---
author: Yin
---
# Bounded holomorphic drifts of a free circular coordinate have both full domains and a sharp vacuum infimum

## Current assessment

[Selected decision](#decision-reviewed)

## Statement

Let \(c,z\) be a free standard circular pair, \(\mathcal R=W^*(c)\), \(M=W^*(c,z)\), and \(H=L^2(M,\tau)\) with unit vacuum \(\Omega\).
Suppose \(B\in\mathcal R\) is bounded and \(B\Omega=\sum_{n\ge0}a_nc^n\Omega\) in \(L^2\).
Set \(Y=(c,z+B)\), and write \(u,v,d,e\) for the circular creation letters of \(c,c^*,z,z^*\), respectively.
Use inner products linear in the second variable.
The following conclusions hold without an operator-norm convergence assumption on the Taylor truncations of \(B\).

1. The coefficients satisfy \(\sum_{n\ge0}(n+1)|a_n|^2\le\|B\|^2\).
   Put \(D=\sum_{n\ge1}a_n\sum_{j=0}^{n-1}c^j\otimes c^{n-1-j}\), of squared coarse norm \(\sum n|a_n|^2\).
2. \(W^*(Y)=M\), and \(Y\) has both actual ACSY and the full operator-and-adjoint domain condition of [T_F0011](../tasks/Yin_T_F0011_v1.md#three-hypotheses-that-must-remain-distinct).
   For the old coordinate there is a witness for the sign \([E,Y_1]=P_\Omega,\ [E,Y_2]=0\) of norm \(M\to H\) at most \(1+2\sqrt2\|D\|_2\), and for the second coordinate there is a norm-one whole-Hilbert-space witness.
   The corresponding actual derivations have zero starred values at both target generators.
3. The infimum of the old-coordinate actual vacuum norm, over all finite starred values on the represented target core, is \(\sqrt{1+|a_1|^2}\).
   The vector \(\zeta=c-\overline{a_1}z\) is in the Hilbert closure of the attainable vacua.
   If \(\sum_n a_n w^n\) extends as a holomorphic Taylor series to a disk of radius greater than one, \(\zeta\) is attained.
   Thus polynomial drifts of arbitrary degree with \(a_1=0\) admit old-coordinate actual vacuum \(c\) of norm one.
   For arbitrary bounded \(B\) in this statement there are actual vacua approaching \(\zeta\), with finite starred values for each witness.
   The second coordinate has actual vacuum \(z\) of norm one, which minimizes its vacuum norm.
4. For the polynomial drifts \(B=Lc^2\), \(L>0\), the least bounded cost \(\beta_1(Y)\) of the old-coordinate commutators on \(M\) satisfies \(\beta_1(Y)\ge L/(2\|z\|)\), even with unrestricted value at the unit.
   Both actual vacua can simultaneously be chosen to be \(c,z\), of norm one each.
   The first coordinate stays fixed while the operator norm of the second grows with \(L\).
   This two-coordinate family therefore excludes a uniform old-coordinate cost bound in terms of those vacuum norms alone, with no common cutoff on the other coordinate.

## Argument

### A necessary coefficient bound from the opposite circular powers

The [circular Fock model](Yin_C_F0074_v1.md#argument) gives \(c=\ell(u)+\ell(v)^*\), \(z=\ell(d)+\ell(e)^*\) on the full Fock space over the four orthonormal letters, with the two pairs free.
For a fixed integer \(L\ge0\) put \(h_L=(c^*)^L\Omega=v^{\otimes L}\), of Hilbert norm one.
Since \(\ell(v)^*\ell(u)=0\),
\[
                 c^n h_L=\sum_{j=0}^{\min(n,L)}u^{n-j}v^{L-j}.
\]
Here and below a word in the four letters denotes its unit Fock tensor.
At fixed \(L\) the displayed words for all pairs \((n,j)\) are distinct, including their empty-prefix and empty-suffix cases.
Right multiplication by \((c^*)^L\) is bounded for this fixed \(L\) and commutes with left \(B\).
Consequently the Hilbert expansions of \(B\Omega\) may be multiplied on the right by \((c^*)^L\), which gives
\[
                \sum_{n\ge0}(\min(n,L)+1)|a_n|^2
                        =\|B h_L\|_2^2\le\|B\|^2 .
\]
Monotone convergence proves the coefficient inequality.
Within \(D\), all pairs of analytic powers are orthonormal in the coarse tensor, giving its asserted norm.

For \(0<t<1\) let \(B_t=\sum_{n\ge0}t^n a_n c^n\).
The series converges in operator norm since \(\|c^n\|\le n+1\) by the same creation-deletion expansion.
It is the Poisson average of the trace-preserving rotations \(c\mapsto e^{i\theta}c\) of \(B\), as seen by applying the average to its vacuum expansion and using faithfulness.
Thus \(\|B_t\|\le\|B\|\), and \(B_t\to B\) in \(L^2\).
Likewise \(B_t^*\to B^*\) in \(L^2\) by traciality, so these uniformly bounded approximants converge strongly-star in the tracial representation, including on \(L^2(M)\) by bounded test vectors and density.
In particular \(B\) lies in the von Neumann algebra of the first coordinate and \(Y_2-B=z\), giving \(W^*(Y)=M\).

### A correction with full bounded-vector and adjoint domains

Use the right deletion \(R_c=r(u)^*\) on the full Fock space.
The vacuum commutator with left \(c\) is \(P_\Omega\), and those with \(c^*,z,z^*\) are zero by the distinct creation letters.
The reversed orientation holds for the adjoint.
Let \(\Theta(a\otimes b)h=a\tau(bh)\) be the tracial coarse-to-Hilbert--Schmidt unitary.
The series for \(B_t\) gives \([R_c,L_{B_t}]=\Theta D_t\), where \(D_t\) has coefficient \(t^na_n\) in degree \(n-1\), and \([R_c,L_{B_t^*}]=0\).
Pass to the strong operator limit on the left and the Hilbert--Schmidt limit on the right, using \(\|D_t-D\|_2\to0\).
It follows that \([R_c,L_B]=\Theta D,\ [R_c,L_{B^*}]=0\) on all \(H\).

Write \(z=(s_1+i s_2)/\sqrt2\) for two free standard semicircular variables free from \(\mathcal R\).
Apply the [relative semicircular insertion construction](Yin_C_F0212_v1.md#a-degree-zero-insertion-over-a-noncommutative-base) to \(s_j\) with base \(W^*(c,s_{3-j})\), which is free from \(s_j\).
Use coefficients \(\gamma_1=-D/\sqrt2,\ \gamma_2=iD/\sqrt2\) in the two base coarse spaces.
The resulting closed operators \(F_j\) and their actual adjoints have every bounded vector in their domains, \(F_j1=0\), and on bounded inputs
\[
    [F_j,L_{s_j}]=\Theta\gamma_j,\qquad
    [F_j,L_h]=0\quad(h\in W^*(c,s_{3-j})),\qquad
    \|F_j a\|_2\le2\|\gamma_j\|_2\|a\|.
\]
The adjoint vacuum is \(F_j^*1=J_{s_j}(\gamma_j^\sharp)\), where \(\sharp\) takes adjoints componentwise and \(J_s(A\otimes C)=A s C\).
These formulas use the inserted coefficient in the full coarse space and its averaging against the full trace.

Let \(E_1=(R_c+F_1+F_2)|_{M\Omega}\).
On that common domain the sum has an actual adjoint containing \(M\Omega\), by summing the bounded-vector adjoint pairings of its three terms.
The correction commutes with \(B,B^*,c,c^*\), has commutator \(\Theta(\gamma_1+i\gamma_2)/\sqrt2=-\Theta D\) with \(z\), and has zero commutator with \(z^*\).
Thus \(E_1\) has the required target commutators on all bounded vectors, and both commutators with the target adjoints vanish.
The norm bound follows by adding the two insertion bounds and the norm of \(R_c\).
The right deletion \(E_2=r(d)^*\) commutes with all of \(\mathcal R\) and satisfies \([E_2,L_z]=P_\Omega,\ [E_2,L_{z^*}]=0\).
Negating \(E_i\) gives the generator-first convention of the full-domain condition.

For every evaluated target star polynomial \(p\), the product rule on bounded vectors expresses \([E_i,L_p]\) there as a finite sum of left multiples and right compositions of \(P_\Omega\).
It has the resulting unique finite-rank extension to \(H\), and \(\Theta^{-1}[E_i,L_p]\) defines an actual outer derivation on the represented target core.
Its starred values are zero and the scalar vacuum pairing is represented by \(E_i^*1\), since \(E_i1=0\).
Writing \(W(w)\Omega=w\) for circular Wick polynomials, these two vacua are
\[
 \xi_0=c-\sum_{n\ge1}\overline{a_n}\sum_{j=0}^{n-1}
                      W(v^j d v^{n-1-j}),\qquad \xi_2=z .
\]
Indeed the two semicircular adjoint vacua combine as
\(-\sum\overline{a_n}(c^*)^j z(c^*)^{n-1-j}\), with the star on the scalar \(\gamma_2\) providing the sign.
The products are exactly the displayed Wick vectors, since the \(d\) letter is distinct from both \(c\) letters and a consecutive string of \(v\)'s has no contraction.
The squared norm of the displayed sum after \(c\) is \(\|D\|_2^2\).

### Correcting the old vacuum through starred coordinates

Let \(H_{\rm hol}\) be the closed linear span of words in \(u,d\) only.
This is also the Hilbert closure of the target holomorphic polynomial span.
To see this, choose polynomials \(b_j(c)\) uniformly bounded in operator norm and converging strongly-star to \(B\), by truncating each of a sequence of \(B_t\) in operator norm.
Then \(Y_2-b_j(c)\to z\) strongly-star with a uniform norm bound.
Every analytic word in \(c,z\) is a strong limit of uniformly bounded analytic polynomials in \(Y\).
Reversing the substitution using \(z+b_j(c)\to Y_2\) gives the other inclusion.
Analytic source words applied to the vacuum are precisely the \(u,d\) words.

Any old-coordinate witness agrees with \(\xi_0\) on target analytic polynomials by the prescribed two generator values.
Hence its projection onto \(H_{\rm hol}\) equals \(\zeta=c-\overline{a_1}z\), of norm \(\sqrt{1+|a_1|^2}\).
The same argument for the new coordinate gives projection \(z\).
It remains to construct actual old-coordinate vacua converging to \(\zeta\).

Let \(\partial_v\) be the starred \(c^*\) cut on the source four-letter star core, killing all other letters.
The [circular Wick marked-letter calculation](Yin_C_F0218_v1.md#the-circular-starred-cut-and-attainment) applies with this one distinguished letter and the other three fixed, using the same creation-deletion recurrence.
It gives \(\partial_v W(w)=\sum_{w=A v C}W(A)\otimes W(C)\), so \(\partial_v^*(W(A)\otimes W(C))=W(A v C)\) and \(\partial_v\) is closable.
For \(2\le n\le N\), for each word \(w=v^j d v^{n-1-j}\), add to \(L_N\in G\) the finite tensor
\[
           \frac{\overline{a_n}}{n-1}
               \sum_{w=A v C} W(A)\otimes W(C),\qquad G=H\otimes_2H .
\]
All cut pairs appearing here reconstruct their word and position.
It follows that \(\partial_v^*L_N=\sum_{n=2}^N\overline{a_n}\sum_j W(v^jdv^{n-1-j})\) and
\(\|L_N\|_2^2=\sum_{n=2}^N n|a_n|^2/(n-1)\).

Write \(d_1,d_2\) for the target starred word cuts on \(Y_1^*,Y_2^*\) respectively, initially evaluated on formal words with bounded prefix and suffix.
On such bounded tensors let
\[
   T(A\otimes C)=\sum_{n\ge1}\overline{a_n}
                 \sum_{j=0}^{n-1} A(c^*)^j\otimes(c^*)^{n-1-j} C .
\]
This is \(A D^\sharp C\) in outer notation and is finite in Hilbert norm.
For every target core element \(p=p(Y,Y^*)\) the closed source cut satisfies
\[
                         \overline{\partial_v}p=d_1p+T d_2p .
\]
Indeed \(B_t,B_t^*\) converge strongly-star with uniform bounds, and their source cuts converge to zero and \(D^\sharp\) respectively in the coarse norm.
At fixed \(t\), polynomial truncations converge with their cuts, and the finite product rule then gives graph convergence for every fixed target word, since uniformly bounded strongly-star convergent outer factors act strongly on each fixed tensor.
Thus the identity holds for every formal representative.

For every polynomial tensor \(A_0\otimes C_0\), its pairing against \(T\) on bounded simple tensors is represented by the Hilbert tensor
\[
         T^\natural(A_0\otimes C_0)
            =\sum_{n\ge1} a_n\sum_{j=0}^{n-1}
                         A_0 c^j\otimes c^{n-1-j} C_0
            = A_0 D C_0 .
\]
The identity follows from traciality on the two legs, or first with \(t^na_n\) and then by coarse convergence.
In particular \(L_N\) and \(T^\natural L_N\) are finite in Hilbert norm for fixed \(N\), without a uniform assumption on the norms of the \(T^\natural L_N\).
Set the two target starred values equal to \(L_N^\sharp\) and \((T^\natural L_N)^\sharp\).
By the [starred-value insertion identity and descent](Yin_C_F0201_v1.md#argument), their full vacuum correction on a target polynomial is
\[
        \langle L_N,d_1p\rangle+\langle T^\natural L_N,d_2p\rangle
           =\langle L_N,\overline{\partial_v}p\rangle
           =\langle\partial_v^*L_N,p\rangle .
\]
Adding the old zero-star witness therefore yields the actual vacuum \(\xi_0+\partial_v^*L_N\).
Its remaining tail has squared norm \(\sum_{n>N}n|a_n|^2\) when \(N\ge1\), and this tends to zero.
This proves the infimum in the bounded case.

If the scalar Taylor series extends to a disk of radius greater than one, exponential coefficient decay together with \(\|c^j\|\le j+1\) makes \(T\) bounded on all of \(G\), and \(T^\natural\) on polynomial tensors agrees with its bounded Hilbert adjoint.
The orthogonal formulas give \(L_N\to L\) and \(\partial_v^* L_N\to\zeta-\xi_0\).
Taking \(L^\sharp,(T^*L)^\sharp\) as the two starred values now gives the exact vacuum \(\zeta\) on the full target core.
This last attainment conclusion includes every polynomial drift.
For a general bounded drift, attainment would follow from convergence or another controlled choice of the second starred correction, which the rough-case estimates do not establish.

### A quadratic drift with growing bounded-dual cost

For \(Y=(c,z+Lc^2)\), any bounded old-coordinate witness \(E:M\to H\) satisfies on every bounded input
\[
 [E,L_z]=-L[E,L_{c^2}]
        =-L(P_\Omega L_c+L_cP_\Omega)=-L\Theta(1\otimes c+c\otimes1).
\]
Testing at \(1\) and using \(\tau(c)=0\) gives \(E(z)-zE(1)=-Lc\).
Since \(\|c\|_2=1\), this forces \(L\le2\|z\|\|E\|_{M\to H}\), proving the lower bound for every choice of \(E1\).
Here \(a_1=0\), so the exact old and new actual vacua constructed above are \(c,z\).
Also \(\|z+Lc^2\|\ge L\|c^2\|-\|z\|\to\infty\).
Every individual tuple has a full-domain system by part 2.
This two-coordinate cost divergence leaves the [single-generator assembly criterion](Yin_C_F0210_v1.md#statement) inapplicable to the family as given.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-13T14:58 |
| status | open |
| reason | The bounded holomorphic coefficient estimate, actual and strong shear witnesses, and sharp vacuum infimum with the stated attainment range are fixed for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Bounded one-circular holomorphic shear with full domains, weighted coefficient inequality, exact vacuum infimum, regular-drift attainment and quadratic two-coordinate cost divergence. |
| argument | [Argument](#argument) | Opposite-power Fock tests, Abel limits, two relative semicircular corrections, full-domain commutators, rough vacua and an all-witness lower bound for the quadratic drift. |
| dependency | [Circular Fock model](Yin_C_F0074_v1.md#argument) | Normalized creation and annihilation representation, opposite-end rank-one commutators and the coarse Hilbert--Schmidt identification. |
| dependency | [Relative semicircular insertions](Yin_C_F0212_v1.md#a-degree-zero-insertion-over-a-noncommutative-base) | Arbitrary base coarse coefficient, actual insertion vacuum, full bounded-input and adjoint domains, commutators and operator-norm-to-Hilbert estimates. |
| dependency | [Circular starred Wick cut](Yin_C_F0218_v1.md#the-circular-starred-cut-and-attainment) | Marked-letter cut on Wick tensors, its Hilbert adjoint and closability, applied with one chosen letter in a four-letter Fock basis. |
| dependency | [Actual starred-value insertion](Yin_C_F0201_v1.md#argument) | Pairing for the two freely prescribed target adjoint values and descent of a vacuum identity to the represented star algebra. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-13T15:09 |
| status | proved |
| reason | Adopt the bounded circular shear theorem, sharp vacuum infimum and quadratic cost example after independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Bounded one-circular holomorphic shear with full domains, weighted coefficient inequality, exact vacuum infimum, regular-drift attainment and quadratic two-coordinate cost divergence. |
| argument | [Argument](#argument) | Opposite-power Fock tests, Abel limits, two relative semicircular corrections, full-domain commutators, rough vacua and an all-witness lower bound for the quadratic drift. |
| dependency | [Circular Fock model](Yin_C_F0074_v1.md#argument) | Normalized creation and annihilation representation, opposite-end rank-one commutators and the coarse Hilbert--Schmidt identification. |
| dependency | [Relative semicircular insertions](Yin_C_F0212_v1.md#a-degree-zero-insertion-over-a-noncommutative-base) | Arbitrary base coarse coefficient, actual insertion vacuum, full bounded-input and adjoint domains, commutators and operator-norm-to-Hilbert estimates. |
| dependency | [Circular starred Wick cut](Yin_C_F0218_v1.md#the-circular-starred-cut-and-attainment) | Marked-letter cut on Wick tensors, its Hilbert adjoint and closability, applied with one chosen letter in a four-letter Fock basis. |
| dependency | [Actual starred-value insertion](Yin_C_F0201_v1.md#argument) | Pairing for the two freely prescribed target adjoint values and descent of a vacuum identity to the represented star algebra. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0229_v1.md#whole-proof-finding) | All four inputs, bounded rough drift, actual graph closures, exact infimum, regular attainment and the lower bound with arbitrary value at the unit. |

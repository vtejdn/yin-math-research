---
author: Yin
---

# Curvature graph certificates for the lattice Cauchy Gram inequality

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Use the finite labels \(c_i\), trace masses \(t_i\), Cauchy kernel \(k_{ij}\), sums \(H_i\), maximal densities \(M_i\), liberation masses \(\nu_{ij}\), budget \(B_c\) and analytic tests of the [lattice Gram problem](Yin_C_F0342_v1.md#statement).
Let \(t=(t_i)_i,\ F=(f_{ij}),\ X=tt^{\mathsf T}-F\), with \(f_{ij}\) the real, unnormalized pairings there, and \(K_{ij}=\operatorname{Re}\sum_\ell t_\ell k_{\ell i}\overline{k_{\ell j}}\).
Write \(F_K=\sum_{ij}f_{ij}K_{ij}\).
For \(i\ne j\) set
\[
  g_{ij}=\sum_{\ell\ne i,j}t_\ell\kappa(c_i,c_j,c_\ell)^2,\qquad
  b_{ij}=\frac{2(t_i+t_j)}{|c_i-c_j|^2},
\]
where \(\kappa\) is reciprocal circumradius, zero on collinear triples.
For symmetric nonnegative off-diagonal weights \(a_{ij}\) define the real matrix \(L(a)\) by
\[
   L(a)_{ij}=-a_{ij}\quad(i\ne j),\qquad
   L(a)_{ii}=\sum_{j\ne i}a_{ij}\,t_j/t_i .
\]
Then \(L(a)\succeq0\) and \(L(a)t=0\).
There is an explicit positive semidefinite matrix \(R\), given below, such that
\[
         K+R+L(b)+L(g)=\Lambda\ \text{is diagonal},\qquad
         \sum_i \Lambda_{ii}t_i^2=10\sum_i t_i |H_i|^2 .                \tag{1}
\]
Both \(R\) and \(L(b)\) have decompositions into positive semidefinite matrices indexed by labels \(\ell\), with off-pivot diagonal entries at \(i\ne\ell\) at most \(4t_\ell/|c_i-c_\ell|^2\) for each decomposition.

Consequently, if \(L(g)=\sum_\ell A_\ell\) with real \(A_\ell\succeq0\) and
\[
            (A_\ell)_{ii}\le C_0 t_\ell/|c_i-c_\ell|^2
                         \qquad(i\ne\ell),                               \tag{2}
\]
then \(F_K\ge-C(1+C_0) B_c^2\) uniformly in all actual tests on these labels.
No restriction on \((A_\ell)_{\ell\ell}\) is needed.
An absolute \(C_0\) for all finite label configurations would thus imply the general normal converse.

There is a sufficient geometric condition allowing a diagonal change in (1).
Suppose that, off the diagonal,
\[
 g_{ij}=\sum_{S:\,i,j\in S}\lambda_S+e_{ij},\qquad
 \sup_{i\ne j}|c_i-c_j|^2\sum_{S:\,i,j\in S}\frac{\lambda_S}{t(S)}
        \le C_1,\qquad
 |e_{ij}|\le C_2(t_i+t_j)/|c_i-c_j|^2,                                  \tag{3}
\]
where \(S\) ranges over subsets of the finite label set with at least two elements, \(\lambda_S\ge0\) and \(t(S)=\sum_{i\in S}t_i\).
Then \(F_K\ge-C(1+C_1+C_2)B_c^2\).
All original lattice right slices on these configurations have norm at most \(C(1+\sqrt{C_1+C_2})B_c\) on the full represented polynomial unit ball.
This gives explicit uniform certificates on arbitrary collinear or concyclic labels with arbitrary masses and projection coefficient.
Existence of a uniform curvature graph decomposition or of a uniform true lower bound in general is open.

## Argument

### Gram matrices at each label

Use \(G_{ij},V_{ij}=iG_{ij}-u e_j\zeta e_i\) from [the quartic coefficients of the exact energy](Yin_C_F0342_v1.md#polarizing-the-rank-one-energy).
In the real Hilbert space obtained from the trace inner product by taking its real part, set
\[
 w_\ell=i u e_\ell/\sqrt{t_\ell},\qquad
 Y_{\ell i}=w_\ell-\frac{V_{\ell i}}{\sqrt{t_\ell}\,t_i},\qquad
 \theta_{\ell i}=\|Y_{\ell i}\|_2^2-1,\qquad d_{\ell i}=t_i^2\theta_{\ell i}.
\]
Then \(Y_{\ell\ell}=w_\ell\) and \(d_{\ell\ell}=0\).
Write \(s_{ij}=f_{ij}/(t_it_j)\).
The identity \(\operatorname{Re}\langle V_{\ell i},i u e_\ell\rangle=f_{\ell i}\) and formula (5) of the cited energy give
\(\operatorname{Re}\langle Y_{\ell i},Y_{\ell j}\rangle=1-s_{ij}\) for every \(i\ne j\), including cases when one of them is \(\ell\).
For three distinct indices the term from the two \(V\)'s is \(s_{\ell i}+s_{\ell j}-s_{ij}\), cancelling the first two pairings with \(w_\ell\).
The Gram matrix of the vectors \(t_iY_{\ell i}\) is therefore
\[
     X+\operatorname{diag}(d_{\ell i})_i\succeq0,\qquad d_{\ell i}\ge-t_i^2.
\]
Their diagonal corrections satisfy the edge identity
\[
                    t_\ell d_{\ell i}+t_i d_{i\ell}=2\nu_{i\ell}
                         \qquad(i\ne\ell).                               \tag{4}
\]
Indeed \(t_\ell d_{\ell i}=\|V_{\ell i}\|_2^2-2t_i f_{\ell i}\); adding the swapped expression gives (4) by the cited formula (4).
This calculation uses the actual signed pairings on the given finite algebra.

For any positive semidefinite matrices \(Q_\ell\) set \(a_{\ell i}=(Q_\ell)_{ii}/t_\ell\) at \(i\ne\ell\).
Positivity of the Gram matrices under trace pairing gives
\[
 -\sum_\ell\operatorname{tr}(Q_\ell X)
 \le\sum_{i<\ell}
 \left(2\nu_{i\ell}\max(a_{\ell i},a_{i\ell})
    +t_it_\ell\max(t_i,t_\ell)|a_{\ell i}-a_{i\ell}|\right).             \tag{5}
\]
For each edge use the larger coefficient times (4), subtract the coefficient difference times the other directed term, and use \(d_{\ell i}\ge-t_i^2\).
The second term in (5) is zero for matching coefficients on the two orientations.
In particular if \(a_{\ell i}\le C_3/|c_i-c_\ell|^2\), (5) is bounded by \(C C_3 B_c^2\).
For the scalar correction use the annular estimate
\[
   \sum_{i<j}\frac{t_it_j(t_i+t_j)}{|c_i-c_j|^2}
       =\sum_i t_i^2\sum_{j\ne i}\frac{t_j}{|c_i-c_j|^2}
       \le C\sum_i t_i M_i^2 .
\]
In fact the inner sum is at most \(C M_i/h\) by summing dyadic annuli from the mesh \(h\), and \(t_i/h\le M_i\).
For the first term of (5) the inverse-gap sum is already in \(B_c^2\).

The coupled constraints can also preclude abstract data satisfying the separate [spectral-row inequalities](Yin_C_F0335_v1.md#statement) on label-constant functions.
For example set \(t_1=t_2=1/2,\ \nu_{12}=\nu_{21}=1/4\), with zero diagonal mass.
Take normalized \(X_{ij}/(t_i t_j)\) equal to one on the diagonal and two off it.
The separate row conditions add \(2\nu_{i\ell}/(t_\ell t_i^2)=4\) to the normalized nonpivot diagonal, giving a positive matrix for each choice of pivot.
In an actual Gram realization, the inner product two with the pivot unit vector forces each nonpivot squared norm to be at least four, hence \(\theta_{12},\theta_{21}\ge3\).
This contradicts (4), which here gives \((\theta_{12}+\theta_{21})/2=2\).
The example compares these finite matrix constraints only.

### Completion of the Cauchy matrix

Define \(p_{\ell i}=k_{\ell i}\) for \(\ell\ne i\), \(p_{ii}=2H_i/t_i\), and
\[
            R_{ij}=\operatorname{Re}\sum_\ell t_\ell p_{\ell i}\overline{p_{\ell j}} .
\]
Each row gives a real positive semidefinite Gram summand with off-pivot diagonal \(t_\ell/|c_i-c_\ell|^2\).
For a distinct triple, the scalar Cauchy identity is
\[
 \kappa(c_i,c_j,c_\ell)^2=
 2\operatorname{Re}\!\left[
 k_{\ell i}\overline{k_{\ell j}}+
                  k_{ij}(\overline{k_{i\ell}}-\overline{k_{j\ell}})\right].
\]
For instance after a similarity taking \(c_i=0,c_j=1,c_\ell=x+iy\), both sides equal \(4y^2/(|c_\ell|^2|c_\ell-1|^2)\), and inverse squared length is the common scaling.
A collinear triple gives zero.
For \(i\ne j\), substituting the two diagonal entries of \(p\) gives
\[
 (K+R)_{ij}=2K_{ij}+2\operatorname{Re}\!\left[(H_i-H_j)\overline{k_{ij}}\right]
           =g_{ij}+2(t_i+t_j)|k_{ij}|^2 .
\]
In the last equality the two repeated-label terms in \(H_i-H_j\) contribute \((t_i+t_j)k_{ij}\).
The quadratic form of \(L(a)\) at a real vector \(y\) is
\(\sum_{i<j}a_{ij}t_it_j(y_i/t_i-y_j/t_j)^2\).
Thus (1) is diagonal and, on \(t\), both graph terms vanish.
The first two Gram matrices give \(t^{\mathsf T}Kt=\sum_i t_i|H_i|^2\) and \(t^{\mathsf T}Rt=\sum_i t_i|3H_i|^2\), since \(\sum_j t_jp_{ij}=3H_i\).
This proves the scalar cost in (1).

For an edge \(i,j\) with \(t_i\le t_j\), place its positive rank-one edge summand of \(L(b)\) at pivot \(i\).
Its only nonpivot diagonal is at \(j\), of size \(b_{ij}t_i/t_j\le4t_i/|c_i-c_j|^2\).
Interchange the labels for the other mass order and break ties arbitrarily.
Each pivot and nonpivot pair receives at most one such summand.
Under (2), combine these matrices with the rows of \(R\) and the specified matrices for \(g\).
The sum is \(\Lambda-K\) with the bounds needed in (5).
Since \(X_{ii}=t_i^2\), one has
\[
 -F_K=\operatorname{tr}(KX)-t^{\mathsf T}Kt
   =\sum_i \Lambda_{ii}t_i^2-t^{\mathsf T}Kt
                      -\operatorname{tr}\big((\Lambda-K)X\big).
\]
Now (1) and (5) give the claimed lower bound.

### Curvature on subsets and signed edge errors

For a term \(\lambda_S\) in (3), define the row at pivot \(\ell\in S\) by
\[
 v_{\ell i}^{S}=1_{\{i\in S\}}
                      (\mathbf1_{\{i=\ell\}}/t_\ell-1/t(S)).
\]
The positive matrix \(\sum_{\ell\in S}t_\ell t(S)\lambda_S v_\ell^S(v_\ell^S)^{\mathsf T}\) is the graph matrix \(L(\lambda_S 1_{S\times S})\), with value \(-\lambda_S\) off the diagonal within \(S\), zero outside \(S^2\) and with \(t\) in the kernel.
Its summand at \(\ell\) has nonpivot diagonal \(t_\ell\lambda_S/t(S)\) for \(i\in S\), zero otherwise.
Summing over \(S\) gives (2) for this part by (3).

For the signed edges of weight \(w_{ij}=e_{ij}+b_{ij}\), use a positive rank-one matrix on \(i,j\) with off-diagonal \(-w_{ij}\) and diagonals \(|w_{ij}|t_j/t_i\) and \(|w_{ij}|t_i/t_j\), respectively.
It is zero when \(w_{ij}=0\).
As for \(L(b)\), putting it at the smaller-mass endpoint bounds the nonpivot diagonal by \(2(2+C_2)t_\ell/|c_i-c_\ell|^2\).
The sum of these signed-edge matrices has the exact off-diagonal entries needed to make \(K+R\) plus the two corrections diagonal.
Its value on \(t\) as a quadratic form is \(\sum_{i<j}2t_it_j(|w_{ij}|-w_{ij})\).
This is bounded by \(C(1+C_2)\sum_i t_iM_i^2\) by the same annular estimate.
All subset terms vanish on \(t\), so the changed diagonal still has scalar cost \(O((1+C_2)B_c^2)\).
Applying (5) again proves the lower bound from (3).
The reflected configurations have precisely the same curvature and budgets, so the [two-orientation Gram estimate](Yin_C_F0342_v1.md#the-cauchy-gram-identity) yields the stated full polynomial slice bound.

For collinear labels take no subsets and \(e_{ij}=0\).
For distinct labels on one circle of radius \(R_0>0\), each distinct triple has squared curvature \(R_0^{-2}\), so \(g_{ij}=(1-t_i-t_j)/R_0^2\).
Use the whole set of labels as one subset, with \(\lambda=R_0^{-2}\).
The signed error is \(-(t_i+t_j)/R_0^2\).
The diameter is at most \(2R_0\), giving \(C_1,C_2\le4\).
With a single label the discrete derivative vanishes directly.
These examples concern the geometric certificate as well as the actual slice.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:43 |
| status | open |
| reason | Fix the elimination of the endpoint and Cauchy terms, the coupled pivot bounds, and the geometric certificates for independent review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact diagonal completion, a remaining curvature graph condition, subset and edge error criteria, and uniform collinear and circle bounds. |
| argument | [Argument](#argument) | Coupled actual row diagonals, Cauchy symmetrization, smaller-mass edge assignment, subset covariance rows and the signed scalar correction. |
| dependency | [Lattice Gram theorem](Yin_C_F0342_v1.md#statement) | Finite-label setting, signed functional, budget and equivalence to the general implication. |
| dependency | [Polarized energy](Yin_C_F0342_v1.md#polarizing-the-rank-one-energy) | Right-supported vectors, off-diagonal real Gram entries, and pair sum of the two directed squared norms. |
| dependency | [Full core estimate](Yin_C_F0342_v1.md#the-cauchy-gram-identity) | Both label orientations, reflected Cauchy matrix and transfer to the entire original word algebra. |
| dependency | [Spectral row bounds](Yin_C_F0335_v1.md#statement) | Separate positive row inequalities compared with the strictly stronger necessary coupled constraints. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:50 |
| status | proved |
| reason | R_F0349 checked the coupled diagonal inequalities, the Cauchy completion and scalar trace, both graph certificates and all four direct dependencies. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Exact diagonal completion, a remaining curvature graph condition, subset and edge error criteria, and uniform collinear and circle bounds. |
| argument | [Argument](#argument) | Coupled actual row diagonals, Cauchy symmetrization, smaller-mass edge assignment, subset covariance rows and the signed scalar correction. |
| dependency | [Lattice Gram theorem](Yin_C_F0342_v1.md#statement) | Finite-label setting, signed functional, budget and equivalence to the general implication. |
| dependency | [Polarized energy](Yin_C_F0342_v1.md#polarizing-the-rank-one-energy) | Right-supported vectors, off-diagonal real Gram entries, and pair sum of the two directed squared norms. |
| dependency | [Full core estimate](Yin_C_F0342_v1.md#the-cauchy-gram-identity) | Both label orientations, reflected Cauchy matrix and transfer to the entire original word algebra. |
| dependency | [Spectral row bounds](Yin_C_F0335_v1.md#statement) | Separate positive row inequalities compared with the strictly stronger necessary coupled constraints. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0349_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

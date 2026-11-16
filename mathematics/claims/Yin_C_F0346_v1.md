---
author: Yin
---

# Actual conjugate variables give both canonical dual domains on every normal tuple

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \(X=(X_1,\ldots,X_d)\), \(1\le d<\infty\), be bounded normal generators of a von Neumann algebra \(M\) with faithful normal probability trace \(\tau\).
Set \(H=L^2(M,\tau)\), \(\Omega=1\), \(P_\Omega=|\Omega\rangle\langle\Omega|\) and \(P_X=\mathbb C\langle X,X^*\rangle\).
Assume the actual ACSY hypothesis on the represented starred core: each outer derivation \(\partial_i:P_X\Omega\to H\otimes_2H\) takes \(X_j\) to \(\delta_{ij}\Omega\otimes\Omega\) and has \(\xi_i=\partial_i^*(\Omega\otimes\Omega)\) in the Hilbert adjoint sense.
There is an absolute \(C\) for which the right and left slices of \(\partial_i p\) have norm at most \(C\|\xi_i\|_2\|p\|\) for all \(p\in P_X\).
For the original generator-first canonical operators,
\[
 D_i=-\overline{(\mathrm{id}\otimes\tau)\partial_i},\qquad
 M\Omega\subset\operatorname{Dom}D_i\cap\operatorname{Dom}D_i^*,\qquad
 [X_j,D_i]|_{M\Omega}=\delta_{ij}P_\Omega|_{M\Omega}.
\]
Consequently \(\mathsf A(X)\) and \(\mathsf S(X)\) are equivalent for all the normal generating tuples of the [F0011 contract](../tasks/Yin_T_F0011_v1.md#contract).

For these tuples, under either equivalent hypothesis, the two fraction criteria apply to the same holomorphic division closure \(F=\operatorname{Div}_{L^0(M)}\mathbb C\langle X\rangle\).
For \(u\in L^0(M)\), membership in \(F\) is equivalent to existence of a bounded fraction \(Q=(s,a,b,t)\) with \(u=s^{-1}a=bt^{-1}\), \(s,t\) invertible in \(L^0(M)\), and bounded finite-rank operators \(T_i\) solving
\[
               \sum_i [\rho(X_i),T_i]=aP_\Omega t-sP_\Omega b,
\]
where \(\rho\) denotes right multiplication.
It is also equivalent, for every such \(Q\), to finite rank for all \(i\) of the specified operators \(\Gamma[Q,D_i]=sD_i b-aD_i t\) on their natural domains \(\{v\in H:bv,tv\in\operatorname{Dom}D_i\}\); one common \(Q\) suffices in this test as well.
In the finite-rank case these densely defined operators have bounded finite-rank closures, and \(T_i=-\overline{\Gamma[Q,D_i]}\) realizes the displayed boundary equation at that \(Q\).
Their ranks are independent of the bounded fraction.
For any supplied strong system in the generator-first convention, its fraction commutators agree with the corresponding canonical fraction commutators on \(M\Omega\) and have the same bounded finite-rank closures whenever either has finite rank on its natural domain, as in [canonical compatibility](Yin_C_F0075_v1.md#fractions-and-exact-finite-rank-transfer).

## Argument

### The enlarged disk in the signed angular estimate

First work at a single bounded normal coordinate \(Z\) with its actual relative distinguished derivative on the represented starred core, killing the omitted coefficients and their adjoints.
Use the diffuse marginal law \(\mu\), its scalar vacuum \(\xi_\mu\), the joint vacuum \(\xi\), partial liberation \(\gamma\), and the spectral measure \(\nu\) of \(\zeta=(i\gamma)^*(1\otimes1)\) for the two marginal actions.
The [vacuum identity](Yin_C_F0238_v1.md#statement) gives \(I=\int|z-w|^{-2}d\nu\le\|\xi\|_2^2\).
Its necessity uses only this coordinate.
Assume for the moment that there is a finite Borel partition of the marginal into sets \(C_j\) with \(\nu(C_j\times C_j)=0\) for every \(j\).
This auxiliary assumption will be imposed only on the spread models in the lattice reduction.

For a strict selfadjoint core contraction \(b\) use the analytic tests \(u=b\pm i\sqrt{1-b^2}\).
Write \(F_q(u)=\operatorname{Re}\langle u,(\mathrm{id}\otimes\tau)I_q\gamma(u)\rangle\) for the signed pairing on real symmetric marginal kernels \(q\), where \(I_q\) is inner insertion.
Fix a disk \(B=B(a,r)\), its concentric triple \(Q=3B\), a real bounded Borel function \(p\) on \(Q\), and \(m=\mu(Q)>0\).
We will prove
\[
\begin{split}
 F_{1_B(z)1_B(w)(p(z)-p(w))^2}(u)
 \ge{}&-\int_{B\times(Q\setminus B)} |p(z)-p(w)|^2d\mu(z)d\mu(w)\\
     &-\frac{8\,\operatorname{osc}_Q(p)^2}{m}\,\nu(B\times Q).          \tag{1}
\end{split}
\]
If \(m=0\), the signed pairing is zero.

First take \(p\) simple.
Partition \(Q\) into positive-mass cells refining the \(C_j\), the two parts \(B,Q\setminus B\) and the level sets of \(p\), up to marginal null sets.
Write \(e_i\) for their projections, \(t_i=\tau(e_i)\), \(\nu_{il}=\nu(e_i\times e_l)\) in set notation and \(s_i=1\) on cells of \(B\), zero otherwise.
In particular \(\nu_{ii}=0\).
Let \(F=(f_{ij})\) be the real symmetric matrix of the symmetrized pairings of \(e_i\otimes e_j\), so that every real symmetric kernel on these cells is tested by its matrix trace pairing with \(F\).
The [projection square identity](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) gives \(f_{ii}\ge-\nu_{ii}/t_i=0\), including for every subprojection from the same cell.

Write \(t=(t_i)\) and \(X_0=tt^{\mathsf T}-F\), using only the indices in \(Q\).
For each \(l\) one has the positive semidefinite constraint
\[
                X_0+D_l\succeq0,\qquad D_l=\operatorname{diag}(2\nu_{il}/t_l)_i.       \tag{2}
\]
This is the [spectral row bound](Yin_C_F0335_v1.md#statement) averaged on cell \(l\).
Here is a direct verification in the present relative setting.
For real bounded marginal \(k=\sum_i k_i e_i\), the [uncentered square](Yin_C_F0331_v1.md#the-uncentered-square) bounds \(F_{v\otimes v}\) by \((\tau v)^2+\|v\zeta v\|_2^2/\|v\|_2^2\) for any nonzero real bounded marginal \(v\).
Divide cell \(l\) into \(N\) equal-mass Borel sets by diffuseness.
For each of them, \(R\) of mass \(t_l/N\), apply the bound at \(v=k\pm N^{3/4}1_R\) and average the signs.
The extra left term \(N^{3/2}F_{1_R\otimes1_R}\) is nonnegative by the projection identity.
The squared denominators are \(N^{3/2}(t_l/N)(1+o(1))\) uniformly in \(R\), while the trace terms approach \((\tau k)^2\).
Since \(\nu(R^2)=0\), the averaged numerators are exactly
\[
 \|k\zeta k\|_2^2+N^{3/2}\int\big(k(z)^2 1_R(w)+1_R(z)k(w)^2\big)d\nu .
\]
Indeed all terms with both endpoints in \(R\) vanish.
Average over the \(N\) choices and use symmetry of \(\nu\).
The surviving term after division tends to \(2\sum_i k_i^2\nu_{il}/t_l\).
This proves (2) for every real coefficient vector, using the original relative test and the actual liberation vacuum.

### A positive matrix on the larger disk

For the column vector \(p=(p_i)\) of values subtract its \(Q\)-mean, so \(\sum_i t_i p_i=0\), and put \(v_0=m^{-1}\sum_i t_i p_i^2\).
On all cells in \(Q\) define the weighted graph Laplacian with off-diagonal entries \(-w_{ij}=-(p_i-p_j)^2\) and diagonal \(\sum_j w_{ij}t_j/t_i\).
It annihilates \(t\), and its quadratic form on a real vector \(y\) is
\[
          \tfrac12\sum_{ij}t_i t_j (p_i-p_j)^2(y_i/t_i-y_j/t_j)^2 .
\]
Let \(L\) be its compression by the diagonal projection with entries \(s_i\).
Thus \(L_{ij}=-s_i s_j(p_i-p_j)^2\) for \(i\ne j\), and
\[
                   t^{\mathsf T}Lt=\sum_{i\in B,\ j\in Q\setminus B}t_it_j(p_i-p_j)^2 .   \tag{3}
\]
The notation \(i\in B\) means that the cell indexed by \(i\) is contained in \(B\).

There is a sum \(L=\sum_l A_l\) of positive matrices with a separate diagonal bound away from each pivot \(l\).
Let
\[
 r_l(i)=\sqrt{t_l/m}\sqrt{p_l^2+v_0}\,s_i\big((m/t_l)1_{i=l}-1\big),\qquad
 b_l(i)=\sqrt{2t_l/m}\,s_i p_i,\qquad
 A_l=r_l r_l^{\mathsf T}+b_l b_l^{\mathsf T}.
\]
Summing the first outer products at \(i\ne j\) gives \(-s_i s_j(p_i^2+p_j^2)\), since the sum of \(t_l(p_l^2+v_0)/m\) is \(2v_0\).
The second products add \(2s_i s_jp_i p_j\).
Before compression (all \(s_i=1\)), each row vector has zero pairing with \(t\).
Hence the diagonal of their sum is uniquely determined by its off-diagonal entries and the equation \(Lt=0\) before compression, since all \(t_i>0\).
Multiplication by \(s_i\) in the displayed vectors gives exactly the stated compression.
For \(i\ne l\) its summand satisfies
\[
                  (A_l)_{ii}\le 4(t_l/m)s_i\operatorname{osc}_Q(p)^2 .                   \tag{4}
\]
There is no need to bound \((A_l)_{ll}\), since \((D_l)_{ll}=0\).

Write \(W_{ij}=s_i s_j(p_i-p_j)^2\), so \(W+L\) is diagonal and nonnegative.
Since all \(f_{ii}\ge0\),
\[
  \operatorname{tr}(WF)\ge-\operatorname{tr}(LF)
      =\operatorname{tr}(LX_0)-t^{\mathsf T}Lt
      \ge-\sum_l\operatorname{tr}(A_l D_l)-t^{\mathsf T}Lt.
\]
Here the last inequality uses (2) and positivity of each \(A_l\).
Equations (3) and (4) give (1).
Uniform simple approximations to a bounded Borel \(p\), using quantization of its values, pass to (1) on the fixed disk without changing the finite original partition hypothesis.
The insertion on a fixed analytic test is continuous for bounded kernels converging uniformly, by the finite Leibniz expansion at \(b\) and the differentiated binomial series.
The right side of (1) is explicit and needs no common measurable selection of auxiliary partitions.

### Summation of the angular kernels

For \(v\) in the marginal plane put \(h_v(z)=(z-v)/(\bar z-\bar v)\) away from \(v\), assigning any fixed value of modulus at most one there.
Use (1) for its real and imaginary parts in the [positive disk representation](Yin_C_F0329_v1.md#integrating-the-two-block-estimate), with \(dA(a)dr/r^5\) on disks and \(d\mu(v)\) on third points.
Their squared differences sum to \(|z-w|^2\kappa(z,w,v)^2\) off coinciding triples, a full product-measure set.
Here \(\kappa\) is the reciprocal circumradius.
For \(z\in B,w\in Q\), centers have area at most \(\pi r^2\) and \(r\ge|z-w|/4\).
Consequently the first term of (1), integrated over any selection of disks, costs at most \(C\iiint\kappa^2d\mu^3\).
The [scalar geometric criterion](Yin_C_F0255_v1.md#statement) bounds this by \(C\|\xi_\mu\|_2^2\).

Write \(T(B)=\int\min(1,r^2/|a-v|^2)d\mu(v)\).
The squared oscillation on \(3B\) of either angular component, integrated in \(v\), is at most \(CT(B)\): for \(|a-v|>6r\) use the derivative of \(h_v\), and use its uniform bound otherwise.
On disks with \(T(B)\le K\mu(3B)\), the integral of the second term in (1) is therefore at most
\[
           CK\int \nu(B\times3B)dA(a)dr/r^5\le C'K\iint |z-w|^{-2}d\nu(z,w).
\]
The last estimate uses the same range of centers and radii and \(\nu\) gives zero mass to the diagonal.
On the complementary disks use the [absolute signed bound on disks of small local mass](Yin_C_F0337_v1.md#disks-of-small-local-mass) with its absolute choice of \(K\).
That result applies to arbitrary actual relative coordinates, with no partition or domination assumption.
It integrates the collected angular kernel on each disk before taking its signed cost and yields \(C\|\xi\|_2^2\).

At truncated radii the bounded integrations represent the signed kernel pairings by scalar Fubini for each test.
The resulting positive kernels exhaust the full squared curvature kernel \(g(z,w)=\int\kappa(z,w,v)^2d\mu(v)\), up to the fixed disk normalization.
The [matched energy calculation](Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) gives convergence on each test after multiplication by the two oriented gaps, and hence \(F_g(u)\ge-C\|\xi\|_2^2\).
It also gives \(V(u)^2\le2\|\xi\|_2 V(u)-F_g(u)/2\) for the squared real-component slice budget, or the same inequality with any established upper bound for \(-F_g\) in its last term.
Averaging the two analytic tests and separating real and imaginary parts bounds both oriented slices on the original core by \(C\|\xi\|_2\|p\|\).
Every constant used here is absolute, in particular independent of the cardinality or masses of the auxiliary partition.

### Removing the partition and identifying the original operators

Take any finite labelled model of [the lattice equivalence](Yin_C_F0339_v1.md#statement), with its original budget \(B_c\), Cauchy slice \(E_c\) and trace-half projection.
Its [circle construction](Yin_C_F0339_v1.md#free-noise-in-each-spectral-corner) supplies an actual relative coordinate on finitely many separated circles and kills the same projection.
Its relative vacuum has norm at most \(C B_c\).
The circles form the partition needed above, since each equal-label block of the actual liberation vacuum vanishes.
Thus every such continuous model has original slice cost \(\le C B_c\), independently of the labels.
On every represented finite-label word the [conditional recovery and graph approximation](Yin_C_F0339_v1.md#recovering-the-discrete-derivative-on-circles) identify the old discrete derivative with the conditional projection of the graph derivative of that word in the spread model.
In particular \(\|E_c p\|_2\le C B_c\|p\|\) on the whole discrete word algebra.
The other direction of the lattice equivalence yields an absolute estimate \(K_{\rm proj}<\infty\) for the original projection problem.

By the [projection coefficient theorem](Yin_C_F0308_v1.md#statement), the same bound up to an absolute factor holds for a relative normal coordinate with finitely many killed selfadjoint coefficients.
For an actual finite normal tuple the [forced normal phase](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) determines all starred values of \(\partial_i\) and kills the adjoints of all omitted coordinates.
Thus one may use the real and imaginary parts of the omitted coordinates as the selfadjoint coefficients, and a zero coefficient if there are no others.
Applying the relative bound to each distinguished coordinate gives the claimed right-slice estimate in the original tuple.
The [flip-adjoint derivation](Yin_C_F0073_v1.md#statement) on the adjoint tuple has vacuum \(\xi_i^*\) of the same norm and its right slice is the adjoint involution applied to the left slice at \(p^*\).
It supplies the other orientation.
The [two-slice domain theorem](Yin_C_F0072_v1.md#statement) applies to the initial operator on exactly \(P_X\Omega\) and restores both bounded-vector domains of its closure and actual Hilbert adjoint.
The [original commutator passage](Yin_C_F0078_v2.md#the-original-canonical-operators) gives the generator commutators on \(M\Omega\) for their negative closures.
Conversely normal \(\mathsf S\) supplies the actual starred derivations with their actual vacua by [the strong-to-actual construction](Yin_C_F0070_v2.md#actual-vacuum-under-the-additional-single-vector-adjoint-condition).

### The two fraction criteria

Under \(\mathsf A\), [ACSY24, Proposition 3.5](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) gives maximal \(\Delta\), so [the maximal-\(\Delta\) boundary criterion](Yin_C_F0068_v1.md#statement) supplies exactly the existential fraction equation in the statement.
The strong domains just proved permit [the specified fraction realization](Yin_C_F0068_v1.md#dual-specializations) at every bounded regular fraction of every affiliated input.
It uses the operator-first convention, so substitute \(-D_i\) for its operator and obtain the minus sign in the displayed realization by the generator-first operators.
[Canonical compatibility](Yin_C_F0075_v1.md#fractions-and-exact-finite-rank-transfer) compares the canonical and supplied realizations on all bounded vectors and, when finite rank holds, on their bounded finite-rank closures with the same rank on the full natural domains.
The unstarred division closure and the represented starred core have their distinct roles throughout.

## Assessment history

### Decision candidate

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:48 |
| status | open |
| reason | Fix the enlarged-disk estimate with the projections of its Laplacian summands, its application to the finite-label circle models, the unrestricted implication and the two fraction consequences for whole-proof review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Absolute original slice estimates, full canonical domains, normal equivalence, existential boundary equation and every-fraction canonical test. |
| argument | [Argument](#argument) | Equal-mass row averaging, compressed positive matrix on the triple disk, scalar and liberation integration, removal of the auxiliary partition and exact operator and fraction identification. |
| dependency | [Actual inverse-gap identity](Yin_C_F0238_v1.md#statement) | Actual relative liberation, zero diagonal spectral mass and the inverse-gap budget. |
| dependency | [Projection identity](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Nonnegative signed diagonal when restricted liberation mass vanishes, also on a measurable subcell. |
| dependency | [Spectral row bound](Yin_C_F0335_v1.md#statement) | Rank-one domination by each actual spectral row and its averaged finite-cell inequality. |
| dependency | [Uncentered square](Yin_C_F0331_v1.md#the-uncentered-square) | Direct spike-average proof of the needed finite-cell form in the relative setting. |
| dependency | [Disk representation](Yin_C_F0329_v1.md#integrating-the-two-block-estimate) | Positive disk representation of the angular difference and its bounded truncations. |
| dependency | [Scalar curvature](Yin_C_F0255_v1.md#statement) | Total curvature and maximal density of the scalar marginal with actual vacuum. |
| dependency | [Bad disks](Yin_C_F0337_v1.md#disks-of-small-local-mass) | Integrated absolute signed estimate with an absolute threshold for any actual relative coordinate. |
| dependency | [Matched energy](Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Gap-weighted limit and signed lower bound giving both original oriented slice costs. |
| dependency | [Lattice equivalence](Yin_C_F0339_v1.md#statement) | Absolute comparison with the original relative projection constant in both directions. |
| dependency | [Circle spread](Yin_C_F0339_v1.md#free-noise-in-each-spectral-corner) | Actual vacuum and zero equal-label liberation blocks on the continuous model. |
| dependency | [Conditional recovery](Yin_C_F0339_v1.md#recovering-the-discrete-derivative-on-circles) | Exact recovery on finite-label words by graph approximation and conditional projection. |
| dependency | [Projection coefficient theorem](Yin_C_F0308_v1.md#statement) | Uniform relative estimates with arbitrary finitely many killed selfadjoint coefficients. |
| dependency | [Normal derivative on adjoints](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Diffuseness, forced marginal and omitted starred derivatives on the original core. |
| dependency | [Adjoint tuple](Yin_C_F0073_v1.md#statement) | Flip-adjoint derivation, actual conjugated vacuum and interchange of left and right slices. |
| dependency | [Two domains](Yin_C_F0072_v1.md#statement) | Restoration of the original closure and Hilbert adjoint on all bounded vectors. |
| dependency | [Generator-first sign](Yin_C_F0078_v2.md#the-original-canonical-operators) | Passage from the bounded-vector domains and core identities to the canonical commutators. |
| dependency | [Normal converse direction](Yin_C_F0070_v2.md#actual-vacuum-under-the-additional-single-vector-adjoint-condition) | Normal strong duals give actual represented starred derivations. |
| dependency | [Maximality](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 for the full starred actual adjoint hypothesis. |
| dependency | [Boundary solvability](Yin_C_F0068_v1.md#statement) | One bounded regular fraction and the finite-rank boundary equation. |
| dependency | [Specified realization](Yin_C_F0068_v1.md#dual-specializations) | Every bounded fraction, fixed-fraction uniqueness, operator-first signs and rank independence. |
| dependency | [Canonical compatibility](Yin_C_F0075_v1.md#fractions-and-exact-finite-rank-transfer) | Equality on the bounded-vector core, natural domains and finite-rank closures for any supplied strong system. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-16T19:54 |
| status | proved |
| reason | The independent whole-proof review R_F0350 checked the enlarged-disk matrix estimate, its summation and circle-model transfer, both original canonical domains, the converse, both fraction tests and all twenty-one declared interfaces. The fixed proof establishes the unrestricted normal equivalence. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Absolute original slice estimates, full canonical domains, normal equivalence, existential boundary equation and every-fraction canonical test. |
| argument | [Argument](#argument) | Equal-mass row averaging, compressed positive matrix on the triple disk, scalar and liberation integration, removal of the auxiliary partition and exact operator and fraction identification. |
| dependency | [Actual inverse-gap identity](Yin_C_F0238_v1.md#statement) | Actual relative liberation, zero diagonal spectral mass and the inverse-gap budget. |
| dependency | [Projection identity](Yin_C_F0242_v1.md#the-cost-of-a-measurable-spectral-block) | Nonnegative signed diagonal when restricted liberation mass vanishes, also on a measurable subcell. |
| dependency | [Spectral row bound](Yin_C_F0335_v1.md#statement) | Rank-one domination by each actual spectral row and its averaged finite-cell inequality. |
| dependency | [Uncentered square](Yin_C_F0331_v1.md#the-uncentered-square) | Direct spike-average proof of the needed finite-cell form in the relative setting. |
| dependency | [Disk representation](Yin_C_F0329_v1.md#integrating-the-two-block-estimate) | Positive disk representation of the angular difference and its bounded truncations. |
| dependency | [Scalar curvature](Yin_C_F0255_v1.md#statement) | Total curvature and maximal density of the scalar marginal with actual vacuum. |
| dependency | [Bad disks](Yin_C_F0337_v1.md#disks-of-small-local-mass) | Integrated absolute signed estimate with an absolute threshold for any actual relative coordinate. |
| dependency | [Matched energy](Yin_C_F0292_v1.md#the-signed-estimate-on-analytic-unitaries) | Gap-weighted limit and signed lower bound giving both original oriented slice costs. |
| dependency | [Lattice equivalence](Yin_C_F0339_v1.md#statement) | Absolute comparison with the original relative projection constant in both directions. |
| dependency | [Circle spread](Yin_C_F0339_v1.md#free-noise-in-each-spectral-corner) | Actual vacuum and zero equal-label liberation blocks on the continuous model. |
| dependency | [Conditional recovery](Yin_C_F0339_v1.md#recovering-the-discrete-derivative-on-circles) | Exact recovery on finite-label words by graph approximation and conditional projection. |
| dependency | [Projection coefficient theorem](Yin_C_F0308_v1.md#statement) | Uniform relative estimates with arbitrary finitely many killed selfadjoint coefficients. |
| dependency | [Normal derivative on adjoints](Yin_C_F0076_v1.md#1-diffuseness-the-phase-and-closability) | Diffuseness, forced marginal and omitted starred derivatives on the original core. |
| dependency | [Adjoint tuple](Yin_C_F0073_v1.md#statement) | Flip-adjoint derivation, actual conjugated vacuum and interchange of left and right slices. |
| dependency | [Two domains](Yin_C_F0072_v1.md#statement) | Restoration of the original closure and Hilbert adjoint on all bounded vectors. |
| dependency | [Generator-first sign](Yin_C_F0078_v2.md#the-original-canonical-operators) | Passage from the bounded-vector domains and core identities to the canonical commutators. |
| dependency | [Normal converse direction](Yin_C_F0070_v2.md#actual-vacuum-under-the-additional-single-vector-adjoint-condition) | Normal strong duals give actual represented starred derivations. |
| dependency | [Maximality](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 for the full starred actual adjoint hypothesis. |
| dependency | [Boundary solvability](Yin_C_F0068_v1.md#statement) | One bounded regular fraction and the finite-rank boundary equation. |
| dependency | [Specified realization](Yin_C_F0068_v1.md#dual-specializations) | Every bounded fraction, fixed-fraction uniqueness, operator-first signs and rank independence. |
| dependency | [Canonical compatibility](Yin_C_F0075_v1.md#fractions-and-exact-finite-rank-transfer) | Equality on the bounded-vector core, natural domains and finite-rank closures for any supplied strong system. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0350_v1.md#finding) | Complete fixed statement, argument and direct dependency interfaces. |

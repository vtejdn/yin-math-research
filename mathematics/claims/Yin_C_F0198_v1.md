---
author: Yin
---

# Sparse fourth-moment truncation and the planar logarithmic stability boundary

This Claim gives a truncation with summable fixed-norm exceptions and complete convergence of the deeply clipped logarithmic comparison for real \(AB+2BA\).
It also gives an exact construction within one bounded real Wigner law's support showing that the corresponding unregularized planar comparison needs additional probabilistic input.
The complete statement and argument are adopted with the [independent whole-proof finding](../audits/reviews/Yin_R_F0206_v1.md#truncation-stability-whole-proof); no almost-sure Brown convergence or summable planar defect deviation is asserted.

<a id="statement"></a>
## Exact conclusions

### Original-law sparse truncation and clipped transfer

For each \(N\), let \(A_N,B_N\) be independent real symmetric Wigner matrices.
For each color, the strict upper coordinates are independent copies of a fixed real law \(\xi/\sqrt N\), with
\[
 \mathbb E\xi=0,\qquad \mathbb E\xi^2=1,\qquad
 \mathbb E|\xi|^4<\infty.
\]
The real diagonal coordinates are independent copies of a fixed centered law \(\zeta/\sqrt N\) with \(\mathbb E\zeta^2<\infty\).
The laws may differ between the two colors.
All independent upper coordinates, diagonal coordinates and colors are independent within each size; coupling across sizes is arbitrary.
Put \(P(a,b)=ab+2ba\) and \(T_N=P(A_N,B_N)\).

Fix
\[
 0<\delta<\tfrac14,\qquad \eta>0,\qquad 4\delta+\eta<1,
 \qquad R_N=N^{1/2-\delta}.
\]
Replace every raw upper or diagonal coordinate \(x\) by \(x\mathbf1_{\{|x|\le R_N\}}\), reflect the off-diagonal coordinates symmetrically and then divide by \(\sqrt N\).
Write the resulting matrices as \(\widetilde A_N,\widetilde B_N\) and put \(\widetilde T_N=P(\widetilde A_N,\widetilde B_N)\).
The truncated laws depend on \(N\) and are not recentered.
Let \(M_N\) count the altered independent coordinates of both inputs, counting a reflected off-diagonal pair once.

There are \(c,C,K_0>0\), depending only on the fixed laws and \(\delta,\eta\), such that, for all sufficiently large \(N\),
\[
 \mathbb P\{M_N>N^{4\delta+\eta}\}
 \le \exp[-cN^{4\delta+\eta}\log N],
 \qquad
 \mathbb P\{\max(\|\widetilde A_N\|,\|\widetilde B_N\|)>K_0\}
 \le C\exp[-cN^{2\delta}].
\]
In particular both exceptional series are summable.
The output rank always satisfies
\[
 \operatorname{rank}(T_N-\widetilde T_N)
 \le 2\operatorname{rank}(A_N-\widetilde A_N)
    +2\operatorname{rank}(B_N-\widetilde B_N)
 \le4M_N.
\]

For any positive deterministic \(L_N\to\infty\) with \(\log L_N/\log N\to0\), define
\[
 V_N(z)=\frac1N\sum_{j=1}^N
          \log\max\{s_j(T_N-zI),e^{-L_N}\},
 \qquad
 \widetilde V_N(z)=\frac1N\sum_{j=1}^N
          \log\max\{s_j(\widetilde T_N-zI),e^{-L_N}\}.
\]
For every compact \(K\subset\mathbb C\) and \(b>0\),
\[
 \sum_{N=1}^{\infty}
 \mathbb P\{\sup_{z\in K}|V_N(z)-\widetilde V_N(z)|>b\}<\infty.
\]
More precisely, outside events of probability at most
\(CN^{-2}+\exp[-cN^{4\delta+\eta}\log N]\), eventually
\[
 \sup_{z\in K}|V_N(z)-\widetilde V_N(z)|
 \le8N^{4\delta+\eta-1}(L_N+6\log N)\longrightarrow0.
\]
The constants in these exceptional bounds are independent of \(K,L_N,b\); the sufficiently large dimension may depend on them.
Consequently the comparison tends to zero locally uniformly almost surely under every cross-size coupling.
By the adopted clipping theorem C186v27, \(\widetilde V_N\to u\) almost surely in \(L^1_{\mathrm{loc}}(\mathbb C)\), where
\[
 u(z)=\tau\log|s_1s_2+2s_2s_1-z|
\]
for standard free semicircular \(s_1,s_2\).
This conclusion concerns the clipped potentials of the triangular array.
It does not assert convergence of its unregularized potentials.

### A deterministic instability inside a fixed bounded real law

Along \(N=2n\), \(n=2^k\ge4\), there are explicit deterministic real symmetric zero-diagonal matrices \(A_N,B_N,B'_N\), with
\[
 \|A_N\|=1,\quad \|B_N\|\le1,\quad
 \|B'_N-B_N\|=(4\sqrt N)^{-1},
 \quad \|B'_N\|\le1+(4\sqrt N)^{-1},
\]
such that \(B'_N\) differs from \(B_N\) in one independent off-diagonal coordinate and its reflection.
Every raw coordinate of both input pairs lies strictly inside \([-\sqrt3,\sqrt3]\).
Thus both pairs belong to the product support of the same fixed centered variance-one uniform off-diagonal Wigner law, with deterministic zero diagonals.
Write \(S_N=P(A_N,B_N)\), \(S'_N=P(A_N,B'_N)\).
For every fixed \(R>2\), the cutoff in
\[
 X_N(S)=N^{-1}\sum_{j=1}^N\min\{|\lambda_j(S)|^2,R^2\}
\]
is inactive on these two outputs, and
\[
 X_N(S_N)=0,\qquad X_N(S'_N)\longrightarrow1.
\]
Their output difference has rank at most four and norm tending to zero.
For \(u_N^S(z)=N^{-1}\log|\det(S_N-zI)|\) and \(u_N^{S'}\) defined similarly,
\[
 \int_{|z|<R}(u_N^{S'}-u_N^S)\,dA\longrightarrow\frac{\pi}{2}.
\]
Let \(V_N^S,V_N^{S'}\) use any of the preceding clipping heights, and set
\(D_N^S=V_N^S-u_N^S\), \(D_N^{S'}=V_N^{S'}-u_N^{S'}\) almost everywhere, with value zero at eigenvalues for planar integration.
Then
\[
 \sup_{|z|\le R}|V_N^{S'}(z)-V_N^S(z)|\longrightarrow0,
 \qquad
 \int_{|z|<R}(D_N^S-D_N^{S'})\,dA\longrightarrow\frac{\pi}{2}.
\]

For every fixed \(c_0\in(0,1)\) and all sufficiently large dimensions in this subsequence, one-coordinate independent resampling under that single bounded law has positive-probability neighborhoods on which the change in \(X_N\) exceeds \(c_0\).
The same assertion holds for resampling a whole independent row block.
The neighborhoods can be chosen to have probability at most
\[
 (2\sqrt3)^{-2n(n-1)}=\exp[-cN^2+O(N)]
\]
while retaining positive probability.
This establishes a failure of a vanishing essential-supremum bounded-difference estimate, including on a fixed input norm guard.
It gives no lower bound of nonsummable order on typical resampling influence and no counterexample to Brown convergence.
The constructed pair is not asserted to be the literal hard-threshold truncation pair above.
It excludes a deterministic unregularized or planar-defect transfer based only on bounded norms, sparse coordinate changes, vanishing perturbation norm and clipped-potential control.

## Inputs, provenance and limits

This is a mixed project deduction: the sparse count, polynomial rank comparison and explicit real-polynomial construction are proved below, using the accepted expected-norm theorem and bounded-product convex concentration at their stated scopes.
The expected-norm input is [Lat05, Theorem 2](../audits/literature/Lat05/Yin_U001.md#lat05-u001), printed p. 1274.
Its statement, applicability and reduction on printed pp. 1274--1275 were read; the underlying Gaussian theorem's full proof was not audited.
The concentration input is inequality (9) in [C187v2](Yin_C_F0187_v2.md#argument), with the accepted [GNT14 source scope](../audits/literature/GNT14/readme.md).
The concentration theorem's original proof is not re-audited here.
The [Hermitian rank inequality](Yin_C_F0186_v4.md#rank-stability) and the [adopted global clipping conclusion](Yin_C_F0186_v27.md#statement) are the other direct mathematical inputs.

The generic Jordan comparison in [L58v1](../ledger/Yin_L_F0058_v1.md#failed-shortcuts) and the earlier complex linear-polynomial support test in [L67v1](../ledger/Yin_L_F0067_v1.md#single-entry-oscillation) are ordinary comparisons, not premises of this proof.
The present construction supplies the exact real \(ab+2ba\) realization.
All required arguments are retained in this fixed material; no rolling draft is a premise.
The original-law unregularized transfer, the negative-logarithm estimate for the truncated triangular array and the summable planar defect deviation remain unresolved.

## Current assessment
[Selected decision](#decision-truncation-stability-reviewed)

## Assessment history

### Decision truncation-stability-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-11T17:01 |
| status | open |
| reason | The complete quantitative sparse truncation and clipped transfer, and the exact bounded-real-law polynomial instability with its probability limitation, are retained for independent review. No unregularized transfer or almost-sure Brown conclusion is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact conclusions](#statement) | Original-law sparse truncation, summable fixed norm guard, complete clipped transfer and triangular-array clipping limit; deterministic bounded-real-law AB+2BA instability and precise resampling limitation. |
| argument | [Complete argument](#argument) | All count, expected norm, convex concentration, centering, rank, polynomial cap, exact block, determinant, support, rarity and planar calculations. |
| dependency | [Hermitian rank stability](Yin_C_F0186_v4.md#rank-stability) | Rank comparison for bounded-variation tests of the squared singular laws, used in both clipped comparisons. |
| dependency | [Global clipping](Yin_C_F0186_v27.md#statement) | Almost-sure local planar L1 convergence of the original-law deeply clipped potential for every global subpolynomial height; its defect summability is not an input. |
| dependency | [Bounded-product convex concentration](Yin_C_F0187_v2.md#argument) | Accepted inequality (9) for independent real coordinates of bounded support diameter and a convex Euclidean Lipschitz function, applied to the truncated input norm. |
| dependency | [Expected matrix norm](../audits/literature/Lat05/Yin_U001.md#lat05-u001) | Accepted Theorem 2 for the independent centered strict upper triangular real array, with row/column second moments and total fourth moments uniformly bounded. |


### Decision truncation-stability-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-11T17:13 |
| status | proved |
| reason | The independent whole-proof finding supports the quantitative sparse truncation, summable fixed-norm exceptions, complete clipped transfer and exact bounded-real-law instability with its stated probability limits. Unregularized transfer and the summable planar defect remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact conclusions](#statement) | Original-law sparse truncation, summable fixed norm guard, complete clipped transfer and triangular-array clipping limit; deterministic bounded-real-law AB+2BA instability and precise resampling limitation. |
| argument | [Complete argument](#argument) | All count, expected norm, convex concentration, centering, rank, polynomial cap, exact block, determinant, support, rarity and planar calculations. |
| dependency | [Hermitian rank stability](Yin_C_F0186_v4.md#rank-stability) | Rank comparison for bounded-variation tests of the squared singular laws, used in both clipped comparisons. |
| dependency | [Global clipping](Yin_C_F0186_v27.md#statement) | Almost-sure local planar L1 convergence of the original-law deeply clipped potential for every global subpolynomial height; its defect summability is not an input. |
| dependency | [Bounded-product convex concentration](Yin_C_F0187_v2.md#argument) | Accepted inequality (9) for independent real coordinates of bounded support diameter and a convex Euclidean Lipschitz function, applied to the truncated input norm. |
| dependency | [Expected matrix norm](../audits/literature/Lat05/Yin_U001.md#lat05-u001) | Accepted Theorem 2 for the independent centered strict upper triangular real array, with row/column second moments and total fourth moments uniformly bounded. |
| review | [Independent whole-proof finding](../audits/reviews/Yin_R_F0206_v1.md#truncation-stability-whole-proof) | Complete inspection of the exact statement, entire argument and direct dependencies, including truncation exponents, noncentered means, triangular-array scope, the actual AB+2BA construction and all probability limitations. |

<a id="argument"></a>
## Complete argument

<a id="sparse-truncation"></a>
### A sparse truncation has summable rank and fixed-norm exceptions

Use independent real symmetric Wigner inputs \(A_N,B_N\), with fixed centered variance-one off-diagonal laws of finite fourth moment, fixed centered finite-second-moment diagonal laws, and arbitrary cross-size coupling.
Fix numbers
\[
 0<\delta<\tfrac14,\qquad \eta>0,\qquad 4\delta+\eta<1,
 \qquad R_N=N^{1/2-\delta}.
\]
Replace every raw coordinate \(\xi\) or \(\zeta\) by \(\xi\mathbf1_{\{|\xi|\le R_N\}}\) or \(\zeta\mathbf1_{\{|\zeta|\le R_N\}}\), respectively, before dividing by \(\sqrt N\).
Denote the resulting matrices by \(\widetilde A_N,\widetilde B_N\).
This truncation is not centered; the resulting one-coordinate laws depend on \(N\).
Let \(M_N\) be the total number of altered independent upper coordinates of both inputs, counting a diagonal coordinate once and an off-diagonal reflected pair once.

There are constants \(c,C,K_0>0\), depending on the fixed laws and on \(\delta,\eta\), such that for all sufficiently large \(N\),
\[
 \mathbb P\{M_N>N^{4\delta+\eta}\}
 \le \exp[-cN^{4\delta+\eta}\log N],
 \tag{Sparse-count}
\]
\[
 \mathbb P\{\max(\|\widetilde A_N\|,\|\widetilde B_N\|)>K_0\}
 \le C\exp[-cN^{2\delta}].
 \tag{Truncated-fixed-guard}
\]
Both displayed sequences are summable.
In particular, under every cross-size coupling the two conclusions eventually hold almost surely.

For the count, fourth-moment Markov bounds give at most \(C N^{4\delta}\) as the expected number of altered off-diagonal pairs.
Second-moment Markov bounds give at most \(C N^{2\delta}\) for altered diagonal coordinates.
Thus \(\mathbb EM_N\le C N^{4\delta}\).
The indicators are independent within each size.
For \(t>0\),
\[
 \mathbb E e^{tM_N}
 \le \exp\{(e^t-1)\mathbb EM_N\}.
\]
Set \(t=(\eta/2)\log N\).
Exponential Markov gives
\[
 \mathbb P\{M_N>N^{4\delta+\eta}\}
 \le
 \exp\{-\tfrac\eta2N^{4\delta+\eta}\log N
               +C N^{4\delta+\eta/2}\},
\]
which proves (Sparse-count).

For the norm, first consider one input law and write the strict upper part of its truncated matrix as \(U_N\).
The entries of \(U_N-\mathbb EU_N\) are independent centered real variables, with all other matrix coordinates deterministic zero.
Their row and column sums of variances are at most one, and
\[
 \sum_{i,j}\mathbb E|(U_N-\mathbb EU_N)_{ij}|^4
 \le C\,\mathbb E|\xi|^4.
\]
Lat05, Theorem 2 therefore bounds \(\mathbb E\|U_N-\mathbb EU_N\|\) by a constant independent of \(N\).
If \(m_N=\mathbb E[\xi\mathbf1_{\{|\xi|\le R_N\}}]\), then centering of the original law gives
\[
 |m_N|
 \le R_N^{-3}\mathbb E|\xi|^4,\qquad
 \|\mathbb E(U_N+U_N^T)\|
 \le \sqrt N\,|m_N|
 \le C N^{-1+3\delta}.
\]
The truncated diagonal has norm at most \(N^{-\delta}\).
Consequently
\[
 \sup_N\mathbb E\|\widetilde A_N\|\le C_0<\infty,
\]
and the same conclusion holds for \(\widetilde B_N\).
No fourth moment of the diagonal law was used.

As a function of the independent normalized upper coordinates, the norm of a symmetric matrix is convex and \(\sqrt2\)-Lipschitz for the Euclidean coordinate distance, because the symmetric-entry map has Hilbert--Schmidt Lipschitz constant \(\sqrt2\).
Every such coordinate has support diameter at most \(2N^{-\delta}\).
The adopted bounded-product convex concentration inequality gives
\[
 \mathbb P\{|\|\widetilde A_N\|-\operatorname{med}\|\widetilde A_N\||>t\}
 \le C\exp[-ct^2N^{2\delta}].
\]
A median can be chosen at most \(2C_0\), by Markov's inequality for the nonnegative norm.
Taking \(K_0>2C_0+1\), increasing it to cover both input laws, and using a union bound proves (Truncated-fixed-guard).
This argument supplies a fixed large guard, not a claim of convergence of the truncated operator norm to two.

<a id="complete-clipped-transfer"></a>
### Deeply clipped potentials transfer with complete convergence

Put
\[
 T_N=P(A_N,B_N),\qquad
 \widetilde T_N=P(\widetilde A_N,\widetilde B_N).
\]
For any deterministic positive \(L_N\to\infty\) with \(L_N=N^{o(1)}\), let
\[
 V_N(z)=\frac1N\sum_j\log\max\{s_j(T_N-zI),e^{-L_N}\},
 \quad
 \widetilde V_N(z)=\frac1N\sum_j
          \log\max\{s_j(\widetilde T_N-zI),e^{-L_N}\}.
\]
Then for every compact planar set \(K\) and every \(b>0\),
\[
 \sum_N\mathbb P\left\{
       \sup_{z\in K}|V_N(z)-\widetilde V_N(z)|>b
                   \right\}<\infty.
 \tag{Complete-clipped-transfer}
\]
In particular the difference tends to zero locally uniformly almost surely under every coupling.
Together with C186v27, this gives \(\widetilde V_N\to u\) almost surely in local planar \(L^1\), even though the truncated laws form a triangular array.

Each changed off-diagonal coordinate changes its input by rank at most two, and each changed diagonal by rank at most one.
Writing \(\Delta A=A_N-\widetilde A_N\), \(\Delta B=B_N-\widetilde B_N\), exact telescoping gives
\[
 T_N-\widetilde T_N
 =\Delta A B_N+\widetilde A_N\Delta B
     +2\Delta B A_N+2\widetilde B_N\Delta A.
\]
Hence
\[
 r_N:=\operatorname{rank}(T_N-\widetilde T_N)
 \le2\operatorname{rank}\Delta A
       +2\operatorname{rank}\Delta B
 \le4M_N.
 \tag{Output-rank}
\]

Let \(\Omega_N\) be the event that every original raw input coordinate has modulus at most \(N^2\).
The finite second moments and a union bound give \(\mathbb P(\Omega_N^c)\le C N^{-2}\).
On this event both original input norms are at most \(N^{5/2}\), and the same elementary bound holds for their raw truncations.
For \(z\) in a fixed compact set and all sufficiently large \(N\), all singular values of \(T_N-zI\) and \(\widetilde T_N-zI\) are therefore at most \(N^6\).

For two matrices whose difference has rank \(r_N\), their squared-singular matrices differ by rank at most \(2r_N\).
Apply the adopted Hermitian rank inequality to
\[
 h_N(x)=\tfrac12\log\max\{e^{-2L_N},\min(x,N^{12})\},
 \qquad \operatorname{Var}(h_N)=L_N+6\log N.
\]
On \(\Omega_N\), its upper cap is inactive, uniformly in the fixed compact parameter set, and
\[
 \sup_{z\in K}|V_N(z)-\widetilde V_N(z)|
 \le \frac{2r_N}{N}(L_N+6\log N)
 \le8N^{4\delta+\eta-1}(L_N+6\log N)
 \tag{Clipped-rank-bound}
\]
outside the event in (Sparse-count).
The last deterministic bound tends to zero, since \(4\delta+\eta<1\) and \(L_N=N^{o(1)}\).
The two exceptional probability series are summable, proving (Complete-clipped-transfer).
All events and bounds here concern within-size laws, so first Borel--Cantelli permits arbitrary cross-size coupling.

This establishes a sparse perturbation of a matrix pair with a summable fixed-norm guard.
It does not identify the unregularized potentials of \(T_N\) and \(\widetilde T_N\).
The existing C194v30 theorem assumes fixed original laws, so it cannot be applied to the dimension-dependent, generally noncentered truncated laws without checking and extending its relevant uniform interfaces.

<a id="actual-polynomial-bounded-support-obstruction"></a>
### A single Wigner-scale coordinate can change the actual polynomial's planar potential by order one

The following exact construction specializes the Jordan instability retained in [L58v1](../ledger/Yin_L_F0058_v1.md#failed-shortcuts) and the support-based row-replacement test in [L67v1](../ledger/Yin_L_F0067_v1.md#single-entry-oscillation) to the present real polynomial \(ab+2ba\).
It shows why the preceding clipped transfer and small perturbation rank alone cannot justify unregularized transfer, even on a fixed norm guard and inside one fixed bounded real Wigner law's support.
It does not estimate a typical Wigner event.

Let \(n=2^k\ge4\), \(N=2n\), and choose the real orthogonal Sylvester matrix \(F_n\), whose entries are \(\pm n^{-1/2}\).
One explicit construction is \(F_1=(1)\) and
\[
 F_{2n}=2^{-1/2}
 \begin{pmatrix}F_n&F_n\\F_n&-F_n\end{pmatrix};
\]
block multiplication proves orthogonality inductively.
Let \(J_n\) be the upper shift, and put
\[
 C_n=(2J_n^T-J_n)/3,\qquad G_n=C_n^TF_n,
\]
\[
 A_N=\begin{pmatrix}0&F_n\\F_n^T&0\end{pmatrix},
 \qquad
 B_N=\begin{pmatrix}0&G_n\\G_n^T&0\end{pmatrix}.
\]
Both inputs are real symmetric with zero diagonal.
They satisfy \(\|A_N\|=1\), \(\|B_N\|=\|C_n\|\le1\).
Every entry has modulus at most \(n^{-1/2}\), since each row of \(C_n^TF_n\) is a combination of at most two rows of \(F_n\) with sum of coefficient moduli at most one.
Thus every raw \(\sqrt N\)-scaled entry has modulus at most \(\sqrt2\).
Direct block multiplication gives
\[
 P(A_N,B_N)
 =\begin{pmatrix}J_n&0\\0&F_n^TJ_n^TF_n\end{pmatrix}.
 \tag{Two-Jordan-realization}
\]
Its empirical eigenvalue measure is \(\delta_0\).

Fix any column \(j\) of \(F_n\), set \(f=F_ne_j\), and let \(h=(4\sqrt N)^{-1}\).
Change the single independent upper coordinate \((1,n+j)\) of \(B_N\) by \(h\), with its reflected entry, so that \(G'_n=G_n+h e_1e_j^T\).
The output becomes
\[
 P(A_N,B'_N)=
 \begin{pmatrix}T'_n&0\\0&F_n^T(T'_n)^TF_n\end{pmatrix},
 \qquad
 T'_n=J_n+h(fe_1^T+2e_1f^T).
 \tag{One-coordinate-output}
\]
The two output blocks have identical eigenvalues.
The last row of \(T'_n\) has only its first entry nonzero, equal to \(hf_n\).
After deleting that row and the first column, the remaining matrix is the identity with only its first row changed, and its determinant is \(1+2hf_2\).
Therefore
\[
 |\det T'_n|=|hf_n(1+2hf_2)|\asymp N^{-1},
 \qquad \|T'_n\|\le1+3h.
 \tag{One-coordinate-determinant}
\]
In particular both original and replaced input pairs lie on a common fixed norm guard.

For any fixed \(R>2\), define
\[
 X_N(S)=\frac1N\sum_{\ell=1}^N
           \min\{|\lambda_\ell(S)|^2,R^2\}.
\]
The cutoff is inactive for both constructed outputs.
The arithmetic-geometric mean inequality, the duplicated eigenvalues and the norm bound imply
\[
 |\det T'_n|^{2/n}
 \le X_N(P(A_N,B'_N))\le(1+3h)^2.
\]
The lower and upper bounds tend to one, whereas \(X_N(P(A_N,B_N))=0\).
Thus a single independent input coordinate, changed by \(1/(4\sqrt N)\), produces an order-one jump in the normalized eigenvalue statistic.

Both configurations are in the support of the same fixed real Wigner model with independent off-diagonal law uniform on \([-\sqrt3,\sqrt3]\), variance one, and all diagonal entries zero.
Indeed the original raw magnitudes are at most \(\sqrt2\), and after replacement they are at most \(\sqrt2+1/4<\sqrt3\).
For each fixed size the eigenvalue statistic is continuous in the input entries, because unordered roots of a monic polynomial depend continuously on its coefficients.
Consequently neighborhoods of the original configuration and the independently replaced coordinate have positive product probability and retain a jump bounded below by any prescribed constant less than the limiting jump, for all sufficiently large powers-of-two sizes.
The same statement holds for a full row-block replacement by keeping its other fresh coordinates near their original targets.
This is a failure of essential-supremum bounded differences within a single fixed bounded real law.

The witness supplies no lower bound on the typical resampling influence.
For example, intersect its neighborhoods with the condition that all strict upper entries inside either diagonal \(n\)-by-\(n\) block of both inputs have raw modulus below \(1/2\).
All targets there are zero, so positive-probability witness neighborhoods remain possible.
There are \(2n(n-1)\) such independent coordinates, each satisfying that condition with probability \(1/(2\sqrt3)\).
The selected witness event therefore has probability at most
\[
 (2\sqrt3)^{-2n(n-1)}=\exp[-cN^2+O(N)].
 \tag{Witness-rarity}
\]
It is not a counterexample to a typical fourth-moment influence estimate, the desired summability theorem, or Brown convergence.

<a id="planar-transfer-obstruction"></a>
### The same example obstructs a uniform planar defect transfer

For a finite matrix \(S\) with all eigenvalues in the disk of radius \(R\), the elementary disk-kernel formula is
\[
 \int_{|z|<R}\log|z-\lambda|\,dA(z)
 =\pi R^2\log R-\frac{\pi R^2}{2}+\frac{\pi|\lambda|^2}{2}.
\]
It follows by integrating the circle mean \(\log\max(r,|\lambda|)\) in polar coordinates.
Hence, for the two outputs above and their normalized unregularized potentials,
\[
 \int_{|z|<R}(u'_N-u_N)\,dA
 =\frac{\pi}{2}
    \bigl(X_N(P(A_N,B'_N))-X_N(P(A_N,B_N))\bigr)
 \longrightarrow\frac{\pi}{2}.
 \tag{Planar-potential-jump}
\]
In particular their local planar \(L^1\) difference cannot tend to zero.

The output perturbation has rank at most four.
Both output norms stay bounded, so the rank inequality gives
\[
 \sup_{|z|\le R}|V'_N(z)-V_N(z)|
 \le \frac{C_R}{N}(L_N+1)\longrightarrow0
\]
for the subpolynomial clipping height of C186v27.
Since \(D_N=V_N-u_N\) almost everywhere, the same disk satisfies
\[
 \int_{|z|<R}(D_N-D'_N)\,dA\longrightarrow\frac{\pi}{2}.
 \tag{Planar-defect-jump}
\]
Thus bounded input norms, sparse input changes, vanishing perturbation norm and complete control of the clipped potentials do not supply a deterministic vanishing bound for the actual planar logarithmic loss.
This is not asserted to be the literal threshold-truncation pair used in (Sparse-count).
It excludes a transfer argument based only on those generic perturbation properties; a successful truncation argument must use the probabilistic structure of the actual deleted coordinates and their background.

<a id="remaining-truncation-input"></a>
### Remaining probabilistic transfer input

The sparse-truncation theorem removes the need to demand that the original input norm guard eventually holds.
It constructs a related pair with a summable fixed-norm exception and proves complete convergence of the clipped comparison.
To conclude Brown convergence for the original pair by this route, one still needs both an applicable negative-logarithm theorem for the truncated triangular array and an original-law estimate controlling the unregularized potential difference, or directly the discrepancy of their planar defects.
For instance a sufficient transfer condition is
\[
 \sum_N\mathbb P\left\{
   \|u_N-\widetilde u_N\|_{L^1(K)}>b
                  \right\}<\infty
 \quad\text{for every integer disk }K\text{ and rational }b>0.
\]
The construction above shows why this condition does not follow from the sparse rank bound and fixed norm guard alone.
Neither this sufficient transfer estimate nor the final defect-deviation theorem is established here.

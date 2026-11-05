---
author: Yin
---

# Intermediate singular values of finite-variance matrix pencils under a positive coefficient frame

This research variant of the intermediate-singular-value family treats the correlated physical blocks of a fixed matrix-coefficient pencil.
The [reviewed scalar-shift theorem](Yin_C_F0187_v2.md#decision-complex-intermediate-reviewed) remains fixed at v2; its proof is not copied or claimed to cover the new auxiliary-direction argument.
The result is partial progress for the arbitrary-coefficient [F0013 contract](../tasks/Yin_T_F0013_v1.md#contract), and does not replace that contract by a nondegeneracy hypothesis or complete it.
The argument is a project deduction for Yin, with no novelty claim.
The [current decision](#decision-block-intermediate-reviewed) adopts the exact statement after independent whole-proof review.

<a id="statement"></a>
## Positive-frame block intermediate theorem and exact limits

Fix integers \(m,d\ge1\) and coefficient matrices \(A_0,A_1,\ldots,A_d\in M_m(\mathbb C)\), independently of \(N\).
For each input \(j\), fix an off-diagonal law \(\xi_j\) with \(\mathbb E\xi_j=0\) and \(\mathbb E|\xi_j|^2=1\), and a real centered diagonal law \(\zeta_j\) with finite second moment.
The upper off-diagonal entries of \(W_j^{(N)}\) are independent copies of \(\xi_j/\sqrt N\), the diagonal entries are independent copies of \(\zeta_j/\sqrt N\), and the lower entries are conjugates of the upper entries.
All coordinate families and all inputs are independent within each dimension, while cross-size coupling is arbitrary.
Real and atomic laws are allowed, the real and imaginary parts of each off-diagonal entry may be dependent, and no moment above two or density is imposed.
Put
\[
 L_N=A_0\otimes I_N+\sum_{j=1}^d A_j\otimes W_j^{(N)},\qquad
 \chi_A=\inf_{\|u\|=\|v\|=1}
             \sum_{j=1}^d|u^*A_jv|^2.
\]
Impose the genuine additional hypothesis \(\chi_A>0\).
This is the coefficient frame already identified at its Gaussian scope in [the exact covariance boundary](../ledger/Yin_L_F0058_v2.md#covariance-boundary), not a consequence of the general Task assumptions.

Write singular values decreasingly.
There are \(c,C,N_0>0\), depending on \(m,d,A_1,\ldots,A_d\) and the fixed off-diagonal laws, such that
\[
 \mathbb P\left\{
  \exists j\in\{4m\lceil N^{3/4}\rceil,\ldots,mN-1\}:
  s_{mN-j}(L_N)<c\,\frac{j}{mN}
            \right\}
 \le C N^{2m+2}\exp(-cN^{1/4}),\qquad N\ge N_0.
 \tag{Block-middle}
\]
The index range is nonempty for all sufficiently large \(N\).
No invertibility of \(A_0\), bound for a conditioned minor inverse, least-singular-value floor or quantitative weak-convergence rate is assumed.
In fact the constants do not use \(A_0\) or the diagonal laws, since their entries are removed in the independence-restoring column projection.
The displayed failures are summable, so the intermediate bound is eventual almost surely under every allowed cross-size coupling.

Let \(s_1,\ldots,s_d\) be free centered variance-one semicircular elements in a finite von Neumann algebra with faithful normal trace \(\tau\), and set
\[
 L=A_0\otimes1+\sum_jA_j\otimes s_j,
 \qquad \tau_m=\operatorname{tr}_m\otimes\tau.
\]
The deterministic free singular law satisfies \(\nu_{|L|}([0,t])\le Ct\) for all sufficiently small \(t>0\), and in particular
\[
 -\infty<\log\Delta_{\tau_m}(L)
       =\int\log t\,d\nu_{|L|}(t)<\infty.
\]
The intermediate negative logarithm has the almost-sure bound (Block-middle-log) below, and the finite-dimensional positive logarithm has the expected uniform integrability and pathwise tail control inherited from the fixed-polynomial theorem.
The bottom quantity (Block-bottom-obligation) is left uncontrolled; this statement asserts neither a least-value floor nor a determinant limit.
The actual projected-block counterexample and the constant-change, word-chain and Schur-elimination boundaries proved below are part of this version's retained mathematical scope.
They show why the additional frame hypothesis is not an assumption available in the arbitrary-coefficient Task.

<a id="inputs"></a>
## Exact inputs and provenance

- [C_F0187_v2](Yin_C_F0187_v2.md#decision-complex-intermediate-reviewed) supplies only the bounded-product convex Lipschitz concentration inequality (9) in its [argument](Yin_C_F0187_v2.md#argument), including independent complex coordinates treated as real two-dimensional normed blocks and its actual original-source inspection limits.
- [C_F0186_v4](Yin_C_F0186_v4.md#decision-finite-variance-reviewed) supplies matrix-polynomial Hermitized weak convergence, positive logarithmic tails and the bounded FK unitriangular/Schur identities at their exact finite-variance scope.
- [C_F0186_v10](Yin_C_F0186_v10.md#decision-nonsymmetric-carrier-reviewed) is used only to check the finite free target of the real-input Schur example \(I-s_2s_1\) in the final boundary section, and is not used for the new probability estimate.

The projection, convex concentration and negative-second-moment mechanism follows the inspected GNT14 provenance retained at C_F0187_v2.
Its bounded-product concentration theorem is reused as an accepted external input at that recorded scope, without re-auditing its original proof.
The common physical truncation, auxiliary covariance and net, block Gram identity and singular-index count are supplied in full here.
The word-chain geometry linked below is an explicit object comparison; its zero auxiliary diagonals are checked directly, rather than assuming an unrelated ledger argument proves the new theorem.

<a id="argument"></a>
## Complete block deduction and deterministic boundaries

<a id="physical-block-distance"></a>
### Physical row deletion and fresh independent coordinates

Permute tensor coordinates so that the \(N\) physical indices each carry one auxiliary block \(\mathbb C^m\).
Fix a physical-row deletion count \(k\) with
\[
 2\lceil N^{3/4}\rceil\le k\le N/2,
\]
and retain the first \(N-k\) physical block rows of the raw matrix \(\sqrt N L_N\).
Call the resulting \(m(N-k)\)-by-\(mN\) matrix \(\mathsf B\), with \(i\)-th retained row block \(\mathsf B_i\).
Let \(H_i^{\rm full}\) be the span of the adjoints of all other rows of \(\mathsf B\).
Its orthogonal distance Gram is
\[
 G_i=\mathsf B_i P_{(H_i^{\rm full})^\perp}\mathsf B_i^*
       \in M_m(\mathbb C).
\]

Delete the \(m\) columns of physical index \(i\), both from the current block and from all other rows.
The current block becomes
\[
 X_i=[\,\textstyle\sum_j A_j\omega_{j,\ell}\,]_{\ell\ne i},
\]
where the independent scalars \(\omega_{j,\ell}\) have law \(\xi_j\) or \(\overline{\xi_j}\) according to their inherited orientation.
The constant \(A_0\) and every current diagonal variable disappear exactly in this projection.
Every mirrored occurrence of a fresh variable in another retained row lies in the deleted physical column, so the projected other-row space \(H_i\) is independent of the entire fresh family.
It has dimension at most \(m(N-k-1)\) in ambient dimension \(m(N-1)\), hence complex codimension at least \(mk\).
For every \(u\in\mathbb C^m\), coordinate contraction gives
\[
 \operatorname{dist}(\mathsf B_i^*u,H_i^{\rm full})
       \ge \operatorname{dist}(X_i^*u,H_i).
 \tag{Block-distance-contraction}
\]
No independence of \(H_i^{\rm full}\) from the exposed row is assumed.

<a id="uniform-block-direction"></a>
### A common truncation and a fixed-dimensional net

Let \(\mathcal J\) be the physical indices \(\ell\ne i\) for which every one of the \(d\) fresh amplitudes satisfies \(|\omega_{j,\ell}|\le N^{1/4}\).
The bad-index indicators are independent across physical indices and have probability at most \(dN^{-1/2}\).
A binomial Chernoff bound gives
\[
 \mathbb P\{|\mathcal J^c|>N^{5/8}\}
       \le \exp(-cN^{5/8}\log N)
\]
for sufficiently large \(N\).
The complement here is inside the \(N-1\) available physical indices.
The same \(\mathcal J\) is used for all auxiliary directions \(u\), which is essential for the net argument.

Condition on \(H_i\) and on \(\mathcal J\), with \(|\mathcal J^c|\le N^{5/8}\).
The retained coordinates remain independent with laws \(\xi_j\) or their conjugates conditional on the common modulus cutoff.
Their conditional means need not vanish.
Let \(v_{j,N}\) be their centered complex variances.
Finite second moment gives \(v_{j,N}\to1\), so all are at least \(1/2\) eventually.
After retaining the \(m\) coordinates of each physical index in \(\mathcal J\), the projected other-row space \(H_{\mathcal J}\) has codimension at least
\[
 m(k-|\mathcal J^c|)\ge mk/2.
\]
Let \(P_{\mathcal J}\) be its orthogonal-complement projection, and let \(X_{\mathcal J}\) be the retained current row block.

For fixed unit \(u\), the centered covariance of \(X_{\mathcal J}^*u\) is block diagonal across physical indices, with common auxiliary block
\[
 T_{u,N}=\sum_j v_{j,N}A_j^*uu^*A_j
            \ge(\chi_A/2)I_m.
\]
Only centered complex variances occur in this identity; no vanishing pseudo-variance or independent real/imaginary coordinates are required.
For \(Y(u)=\|P_{\mathcal J}X_{\mathcal J}^*u\|\), the conditional second moment therefore satisfies
\[
 \mathbb E[Y(u)^2\mid H_i,\mathcal J]
  \ge(\chi_A/2)\operatorname{Tr}P_{\mathcal J}
  \ge\chi_A mk/4.
 \tag{Block-covariance}
\]
The uncentered mean contributes an additional nonnegative squared norm and is not discarded as though it were zero.

As a function of the independent retained complex coordinate blocks, \(Y(u)\) is convex and \(M_A\)-Lipschitz, where \(M_A=(\sum_j\|A_j\|^2)^{1/2}\).
Each coordinate block has diameter at most \(2N^{1/4}\).
The accepted bounded-product inequality gives
\[
 \mathbb P\{|Y(u)-\operatorname{med}Y(u)|>t
           \mid H_i,\mathcal J\}
       \le C\exp[-ct^2/(M_A^2N^{1/2})].
\]
Integrating this estimate bounds \(\mathbb E[(Y(u)-\operatorname{med}Y(u))^2\mid H_i,\mathcal J]\) by \(CM_A^2N^{1/2}\).
The \(L^2\) triangle inequality and (Block-covariance) then imply
\[
 \operatorname{med}Y(u)\ge c_0\sqrt k,\qquad
 \mathbb P\{Y(u)<c_0\sqrt k/2\mid H_i,\mathcal J\}
       \le C\exp(-ck/N^{1/2})
\]
eventually, uniformly in \(u,H_i,\mathcal J\).
Here \(c_0>0\) depends on the fixed coefficients and \(m\), and \(k\ge2N^{3/4}\) makes the \(N^{1/4}\) median error negligible.

Take a deterministic \(N^{-1}\)-net of the unit sphere of \(\mathbb C^m\), of cardinality at most \((3N)^{2m}\).
On the retained-coordinate support,
\[
 \|X_{\mathcal J}\|
 \le C_A N^{3/4},
 \qquad |Y(u)-Y(v)|\le C_A N^{3/4}\|u-v\|.
\]
Thus the net error is at most \(C_A N^{-1/4}\), which is negligible compared with \(\sqrt k\).
A union over this fixed-dimensional net gives
\[
 \inf_{\|u\|=1}
   \operatorname{dist}(X_{\mathcal J}^*u,H_{\mathcal J})
       \ge c_1\sqrt k
\]
outside \(CN^{2m}\exp(-cN^{1/4})\), including the much smaller discarded-index exception.
The additional coordinate contraction and (Block-distance-contraction) imply
\[
 G_i\ge c_1^2 k I_m.
 \tag{Block-Gram-floor}
\]
The conditioning used only the projected other-row space and the fresh cutoff set.
It did not condition on a row-dependent norm event, an inverse of an actual minor, or the full unprojected row space.

<a id="block-negative-second-moment"></a>
### Block Schur identity and the singular-value index count

Union the preceding failure probabilities over all retained physical indices.
On the good event, the rows of \(\mathsf B\) are linearly independent.
Indeed any nonzero row relation would give a nonzero combination inside one block lying in the span of all the other blocks, contrary to (Block-Gram-floor).
For the positive definite Gram matrix \(\mathsf B\mathsf B^*\), the block Schur-complement formula gives
\[
 ((\mathsf B\mathsf B^*)^{-1})_{ii}=G_i^{-1}.
\]
Taking the trace yields the exact block negative-second-moment identity
\[
 \sum_{r=1}^{m(N-k)}s_r(\mathsf B)^{-2}
      =\sum_{i=1}^{N-k}\operatorname{Tr}G_i^{-1}
      \le C\,\frac{mN}{k}.
 \tag{Block-negative-second-moment}
\]
This controls a block of \(m\) jointly correlated rows and is not a sum of independent scalar-row estimates.

For a target index \(j\ge4m\lceil N^{3/4}\rceil\), choose \(k=\lfloor j/(2m)\rfloor\).
Then \(k\ge2\lceil N^{3/4}\rceil\), \(k\le N/2\), and \(mk\le j/2\).
The index \(mN-j\) lies in the singular list of \(\mathsf B\), and at least \(j-mk+1\ge j/2\) values of that list are no greater than \(s_{mN-j}(\mathsf B)\).
Therefore
\[
 (j-mk+1)s_{mN-j}(\mathsf B)^{-2}
       \le C\,\frac{mN}{k}.
\]
Row-deletion interlacing and the raw factor \(\sqrt N\) give
\[
 s_{mN-j}(L_N)
 \ge N^{-1/2}s_{mN-j}(\mathsf B)
 \ge c\sqrt{\frac{jk}{mN^2}}
 \ge c'\frac{j}{mN}.
\]
The fixed factor \(m\) is retained in the last normalization.
Union the net and physical-row bounds over at most \(mN\) target indices to obtain (Block-middle).
Its constants are independent of \(A_0\), since that coefficient was absent from every fresh projected block.

<a id="block-mesoscopic-log"></a>
## What the intermediate estimate actually controls

Let \(a_1\le\cdots\le a_{mN}\) denote increasing singular values and let \(r_N=4m\lceil N^{3/4}\rceil+2\).
The estimate is \(a_r(L_N)\ge c(r-1)/(mN)\) for \(r_N\le r\le mN\), eventually almost surely under every coupling.
For every small fixed \(t>0\), it consequently gives
\[
 \limsup_{N\to\infty}\frac1{mN}
       \sum_{\substack{r\ge r_N\\a_r(L_N)<t}}
          |\log a_r(L_N)|
       \le Ct(1+|\log t|)
 \quad\hbox{almost surely}.
 \tag{Block-middle-log}
\]
The proof is the elementary integral comparison for \(\sum_{2\le r\le C mNt}\log(mN/[c(r-1)])\).
No least-value estimate enters this bound.

The accepted [matrix-Hermitized weak law](Yin_C_F0186_v4.md#finite-variance-weak) applies to the fixed self-adjoint matrix polynomial \(L_N^*L_N\), and hence gives almost-sure weak convergence of the singular laws.
The intermediate count bounds their masses in \([0,t]\) by \(r_N/(mN)+Ct\).
It therefore yields for the deterministic limiting singular law
\[
 \nu_{|L|}([0,t])\le Ct
\]
at continuity points, and then at all small \(t>0\) by decreasing continuity points.
Thus the limiting law has no atom at zero and its negative logarithm is finite.
The free pencil is bounded, so its positive logarithm is finite as well.
The finite-dimensional positive logarithmic tails are exactly the matrix-polynomial case of [C_F0186_v4](Yin_C_F0186_v4.md#positive-tail), with its recorded expectation and pathwise conclusions; this use requires no new moment estimate.
Under the additional coefficient frame, a finite free target is therefore derived without assuming bounded free invertibility.

The remaining finite-dimensional quantity is exactly
\[
 B_N^{\rm bottom}
  =\frac1{mN}\sum_{r<r_N}(-\log a_r(L_N))_+.
 \tag{Block-bottom-obligation}
\]
It may be infinite when a finite matrix is singular.
No estimate for this quantity is proved here, even in the positive-frame class.
A recurrence bound for this bottom contribution along a suitable dimensional subsequence is still needed for the F0013 lower bound.
The scalar m=1 least-value results do not supply that correlated-block estimate by tensorization.

<a id="actual-projected-block-failure"></a>
## An actual finite-target pencil defeats the unrestricted projected-block lemma

The frame hypothesis cannot be removed just because the free pencil has a finite FK logarithm.
Take
\[
 m=2,\quad A_0=\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \quad A_1=E_{11},\qquad
 L_N=\begin{pmatrix}W_N&I_N\\I_N&0\end{pmatrix}.
\]
This is an actual pencil of the original model, not a prescribed unrelated minor.
For every \(W_N\),
\[
 L_N^{-1}=\begin{pmatrix}0&I_N\\I_N&-W_N\end{pmatrix},
 \qquad \det L_N=(-1)^N.
\]
The free version has the exact factorization
\[
 \begin{pmatrix}s&I\\I&0\end{pmatrix}
  =\begin{pmatrix}I&s\\0&I\end{pmatrix}
     \begin{pmatrix}0&I\\I&0\end{pmatrix}.
\]
Thus it is boundedly invertible and has ordinary FK determinant one under \(\operatorname{tr}_2\otimes\tau\), by the constant unitary swap and the [accepted unitriangular determinant factorization](Yin_C_F0186_v4.md#cyclic-selfadjoint-reduction).
Moreover \(A_0,A_1\) generate \(M_2(\mathbb C)\), since \(E_{12}=E_{11}A_0\), \(E_{21}=A_0E_{11}\), and \(E_{22}=A_0E_{11}A_0\).

Nevertheless the auxiliary second row of every physical block is supported only on the constant identity entry in physical column \(i\).
Deleting that physical column makes this row zero identically.
For every realization and every retained-row count, the projected block \(X_i\) therefore has a zero row and its projected distance Gram has a zero auxiliary direction.
The sufficient projected estimate \(X_iP_{H_i^\perp}X_i^*\ge ckI_m\) used to prove (Block-Gram-floor) is false in this actual bounded-free-inverse example.
This does not assert that the original unprojected \(G_i\) is singular.
Here \(\chi_A=0\), witnessed by any left vector in \(\ker A_1^*\).
The original unprojected block still contains the indispensable identity information.
The failure is of this block projection mechanism, not of the determinant Task or its upper-limit identity.
It is separate from the arbitrary-minor counterexample already retained in L_F0059_v1.

<a id="constant-elimination-boundary"></a>
## Constant changes do not make a degenerate frame positive

For any invertible constant matrices \(S,T\), the family \(B_j=SA_jT\) has a positive frame if and only if the original family does.
Indeed \(\chi_A=0\) is equivalent by compactness to nonzero \(u,v\) with \(u^*A_jv=0\) for every \(j\).
The pair \(S^{-*}u,T^{-1}v\) annihilates every \(B_j\), and the reverse implication uses the inverse transformations.
Thus normalizing an invertible \(A_0\) or making constant auxiliary basis changes cannot turn a zero frame into the positive frame used above.

This directly affects the [exact word-chain linearization](../ledger/Yin_L_F0058_v2.md#exact-linearization).
For a word of length \(k\ge2\), that construction uses an auxiliary block \(Q_w=I_{k-1}-T_w\), with \((T_w)_{r,r+1}=x_{i_{r+1}}\) and all other entries zero.
The word's row and column couplings join the distinguished corner to auxiliary coordinates, while all auxiliary diagonal entries remain the constant one.
Consequently, whenever an auxiliary coordinate exists, every random coefficient has zero entry on that auxiliary diagonal.
Taking both coefficient test vectors to be that basis vector gives \(\chi_A=0\).
For \(z\ne P(0)\), its monic normalization is an invertible constant left multiplier and preserves the failure.
Hence (Block-middle) is not already a general-polynomial intermediate theorem through that linearization.
The standard doubled Hermitization does not repair this frame condition either: every coefficient \(\begin{pmatrix}0&A_j\\A_j^*&0\end{pmatrix}\) has zero compression between two test vectors in its first auxiliary half.

Actual Schur elimination can remove deterministic auxiliary constraints, as in the preceding two-by-two example, but it does not generally stay inside an affine positive-frame noise model.
Already the familiar zero-frame irreducible pair \(A_1=E_{12},A_2=E_{21}\), with \(A_0=I_2\), gives
\[
 L_N=\begin{pmatrix}I_N&W_1\\W_2&I_N\end{pmatrix},
 \qquad\hbox{Schur complement }I_N-W_2W_1.
\]
This reuses the exact coefficient obstruction identified in L_F0058_v2.
The scalar Schur complement has a bilinear product of the original inputs, not an affine coefficient family to which the new block distance lemma applies.
For real inputs, the [reviewed carrier theorem](Yin_C_F0186_v10.md#statement) at the fixed parameter one gives a finite free logarithm for \(s_2s_1-1\).
The exact bounded FK Schur identity from [C_F0186_v4](Yin_C_F0186_v4.md#cyclic-selfadjoint-reduction) therefore gives
\[
 \log\Delta_{\operatorname{tr}_2\otimes\tau}
      \begin{pmatrix}1&s_1\\s_2&1\end{pmatrix}
  =\tfrac12\log\Delta_\tau(1-s_2s_1)>-\infty.
\]
Thus a finite target does not remove this closure issue.
No impossibility of every more elaborate elimination is asserted.
The unsupported general step is a structured actual-minor or elimination theorem that retains the deterministic constant information while controlling the newly produced products and the bottom logarithm.
Neither free full rank nor a constant change of coordinates supplies that theorem.

## Current assessment
[Selected decision](#decision-block-intermediate-reviewed)

## Assessment history

### Decision block-intermediate-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T13:54 |
| status | open |
| reason | The complete positive-frame block argument, finite free target and actual projection/elimination boundaries are retained as a candidate for fresh mathematical review; no bottom logarithmic estimate or completion of the arbitrary-coefficient Task is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Block intermediate theorem and limits](#statement) | The exact fixed complex finite-second-moment Hermitian model, additional positive coefficient frame, displayed summable intermediate bound, free CDF and finite FK target, mesoscopic logarithm, uncontrolled bottom contribution and all deterministic boundaries stated here. |
| argument | [Complete block proof and boundaries](#argument) | Physical-row independence restoration, common truncation, covariance, auxiliary net, block Schur identity, index count, free-law passage, genuine projected-Gram failure and the constant-change, linearization and Schur-elimination assertions. |
| dependency | [Bounded-product concentration interface](Yin_C_F0187_v2.md#decision-complex-intermediate-reviewed) | Only inequality (9) of its argument for independent bounded normed-coordinate blocks and its recorded source applicability; the scalar intermediate conclusion is not tensorized. |
| dependency | [Matrix weak and logarithmic controls](Yin_C_F0186_v4.md#decision-finite-variance-reviewed) | Almost-sure Hermitized matrix-polynomial weak law, expectation/pathwise positive-log tails and bounded FK unitriangular/Schur identities. |
| dependency | [Finite target of the Schur boundary example](Yin_C_F0186_v10.md#decision-nonsymmetric-carrier-reviewed) | Only the real-input finite free logarithm of the ordered product at the fixed nonzero parameter one. |

### Decision block-intermediate-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T14:06 |
| status | proved |
| reason | Independent whole-proof review supports the physical-block intermediate estimate, free small-value bound and finite logarithm, all displayed logarithmic controls and deterministic projection/elimination boundaries. The three accepted inputs apply at their exact scopes. The positive coefficient frame remains an additional hypothesis, and the bottom logarithm and original arbitrary-coefficient determinant Task remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Block intermediate theorem and limits](#statement) | The exact fixed complex finite-second-moment Hermitian model, additional positive coefficient frame, displayed summable intermediate bound, free CDF and finite FK target, mesoscopic logarithm, uncontrolled bottom contribution and all deterministic boundaries stated here. |
| argument | [Complete block proof and boundaries](#argument) | Physical-row independence restoration, common truncation, covariance, auxiliary net, block Schur identity, index count, free-law passage, genuine projected-Gram failure and the constant-change, linearization and Schur-elimination assertions. |
| dependency | [Bounded-product concentration interface](Yin_C_F0187_v2.md#decision-complex-intermediate-reviewed) | Only inequality (9) of its argument for independent bounded normed-coordinate blocks and its recorded source applicability; the scalar intermediate conclusion is not tensorized. |
| dependency | [Matrix weak and logarithmic controls](Yin_C_F0186_v4.md#decision-finite-variance-reviewed) | Almost-sure Hermitized matrix-polynomial weak law, expectation/pathwise positive-log tails and bounded FK unitriangular/Schur identities. |
| dependency | [Finite target of the Schur boundary example](Yin_C_F0186_v10.md#decision-nonsymmetric-carrier-reviewed) | Only the real-input finite free logarithm of the ordered product at the fixed nonzero parameter one. |
| review | [Independent positive-frame block finding](../audits/reviews/Yin_R_F0191_v3.md#positive-frame-block-reviewed) | Whole statement and argument, all three direct input interfaces, physical-block conditional independence and covariance, concentration and net, block Gram/index normalization, free and finite logarithmic scopes, actual counterexample and every declared elimination boundary. |

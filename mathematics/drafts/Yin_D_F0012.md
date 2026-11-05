---
author: Yin
---

# Coupling criteria and finite-variance Wigner determinant upper limits

This continuing investigation concerns [matrix-pencil F0013](../tasks/Yin_T_F0013_v1.md#contract) and [scalar-polynomial F0014](../tasks/Yin_T_F0014_v1.md#contract).
The exact contracts retain fixed finite-variance Wigner laws, arbitrary fixed coefficients and arbitrary dependence between dimensions.
The [regularized upper-bound and linearization discussion](../ledger/Yin_L_F0061_v2.md) and [bounded source comparison](../ledger/Yin_L_F0062_v1.md#wigner-status) are starting inputs, rather than a completed solution.
The present material is proof development and has no independent-review status.

## Starting question and discriminating target

The existing almost-sure upper bound reduces the finite-target case to a lower recurrence assertion for the normalized ordinary logarithmic determinant.
The first question is exactly how weak a marginal probabilistic lower estimate suffices under every cross-dimensional coupling, and what failure of that estimate would permit an adversarial coupling to do.
The real commutator parity obstruction prevents demanding convergence in probability along all dimensions in complete generality.
A deterministic subsequence with a lower probability limit may still suffice.

## Current unresolved mathematical scope

No general lower recurrence estimate or counterexample for the full affine Wigner contract is asserted here.
Any proposed block or scalar subclass must retain its actual matrix coefficients and fixed parameter, including singular constant coefficients.
A polynomial least-singular-value floor alone remains insufficient by the [retained negative-logarithmic gap](Yin_D_F0010.md#negative-logarithmic-gap).

## Fixed criteria and polynomial closure

The complete marginal coupling criteria and their proofs are now fixed in [the reviewed C_F0190_v1 theorem](../claims/Yin_C_F0190_v1.md#decision-coupling-criteria-reviewed), with its exact application limits there.
No new probability estimate for the full Wigner contract follows merely from that reduction.
The outer-polynomial and zero-shift ordered-product determinant deductions are fixed in [C_F0186_v7](../claims/Yin_C_F0186_v7.md#outer-polynomial-statement), with their complete root-factorization argument at [the fixed proof](../claims/Yin_C_F0186_v7.md#outer-polynomial-argument).
Both fixed materials remain at their actual recorded mathematical assessment and review scope.
The one-real-Wigner matrix-coefficient specialization and the conditional complex-law transfer below remain continuing work in this Draft.
The real-symmetric witness construction is fixed in the [reviewed all-large-even result](../claims/Yin_C_F0186_v9.md#all-even-witness).

<a id="one-real-wigner-matrix-pencil"></a>
## Arbitrary matrix coefficients in one real Wigner variable

For one real Wigner input and arbitrary fixed \(A_0,A_1\in M_m(\mathbb C)\), the full logarithmic determinant limit in F0013 follows from the accepted scalar theorem, even when \(A_0\) and \(A_1\) are singular and do not commute.
More generally, let \(H(t)\in M_m(\mathbb C[t])\) be any fixed matrix polynomial and write \(q(t)=\det H(t)\in\mathbb C[t]\).
For each real symmetric \(W_N\), unitary diagonalization of \(W_N\) gives
\[
 \det H(W_N)=\prod_{j=1}^N q(\lambda_j(W_N))
 =\det q(W_N).
\]
Here \(H(W_N)\) acts on \(\mathbb C^m\otimes\mathbb C^N\), and \(q(W_N)\) acts on \(\mathbb C^N\).
On the free side, the spectral theorem for the selfadjoint semicircular element gives
\[
 \log\Delta_{\operatorname{tr}_m\otimes\tau}(H(s))
 =\frac1m\int_{-2}^2\log|q(t)|\,d\mu_{\mathrm{sc}}(t).
\]
Indeed, for every spectral value \(t\), the sum of the \(m\) logarithmic singular values of \(H(t)\) is \(\log|\det H(t)|\), including the value \(-\infty\) at singular fibers.
The positive part is bounded on the compact interval, so the equality of the integrals is justified using a decreasing lower truncation or negative-part monotone convergence.
If \(q\equiv0\), every finite pencil is singular and the free logarithm is \(-\infty\), yielding the required identity immediately.
Otherwise factor \(q\) and apply the reviewed [scalar fixed-shift theorem](../claims/Yin_C_F0186_v6.md#statement) with base \(R(x)=x\) at its finitely many roots, as in [the fixed factorization argument](../claims/Yin_C_F0186_v7.md#outer-polynomial-argument), to obtain
\[
 \frac1{mN}\log|\det H(W_N)|
 =\frac1m\frac1N\log|\det q(W_N)|
 \longrightarrow\log\Delta(H(s))
 \quad\text{almost surely}.
\]
A nonzero \(q\) has finite free logarithm, since it has finitely many roots and the semicircle density is bounded.
The input laws may have arbitrary finite-variance real diagonals and no higher moments or density; the event applies under every cross-size coupling.
Taking \(H(t)=A_0+A_1t\) settles the complete matrix-coefficient question for this one-real-Wigner submodel.
For several real Wigner inputs, the same argument applies to \(A_0+B\sum_jr_jW_j\) with fixed real \(r_j\), because their nonzero normalized linear combination is again a real fixed-law finite-variance Wigner matrix, and the matching free linear combination is semicircular with the same variance.
This is a direct application of the already reviewed scalar input rather than a new matrix-coefficient small-value estimate.
General matrix coefficients in several variables, and complex-Hermitian input laws outside the accepted real-input small-value theorem, remain unresolved by this deduction.
This continuing matrix-coefficient deduction has not been selected as a fixed Claim or independently reviewed here.

<a id="complex-one-variable-transfer"></a>
## Exact conditional transfer for one complex Hermitian variable

The remaining complex-input obligation for the preceding matrix-polynomial specialization can be isolated without imposing commutativity on its coefficient matrices.
Let \(W_N\) have any one of the fixed centered finite-second-moment complex Hermitian laws in the original Tasks, with its independent real diagonal law and arbitrary cross-size coupling.
The sole additional premise in this section is the following even-dimensional scalar estimate:
\[
 \text{for every fixed }\lambda\in\mathbb C\text{ there is }A_\lambda>0
 \text{ such that }
 \mathbb P\{s_{\min}(W_N-\lambda I)\le N^{-A_\lambda}\}
 \longrightarrow0
 \quad(N\to\infty,\ N\ \mathrm{even}).
 \tag{Even-scalar-premise}
\]
The premise concerns the original fixed law and diagonal, and all its parameters are fixed before taking the limit.
It asks for neither summable failures nor a simultaneous assertion for uncountably many \(\lambda\).
The accepted phase-line result and the continuing [non-line investigation](Yin_D_F0027.md#nonline-full-adjugate-scope) and [pure-imaginary investigation](Yin_D_F0029.md#scope) have different current mathematical and review statuses; those links do not declare this premise proved for all laws.
What follows is a complete conditional deduction of the one-variable matrix-polynomial determinant assertion from this precise premise.

Fix \(\lambda\).
The [accepted complex intermediate theorem](../claims/Yin_C_F0187_v2.md#statement) applies directly to the original \(W_N\) and the deterministic shift \(-\lambda I\).
Writing \(a_1\le\cdots\le a_N\) for their singular values and \(k_N=\lceil N^{3/4}\rceil+2\), it gives
\[
 a_k\ge c(k-1)/N\qquad(k_N\le k\le N)
\]
outside a probability tending to zero, in fact outside a summable exceptional sequence.
Intersect this event with the scalar-premise event.
For \(k<k_N\), each negative logarithm is at most \(A_\lambda\log N\), so their total normalized contribution is at most
\[
 \frac{k_N}{N}A_\lambda\log N=o(1).
\]
For \(0<t<\min(1,c/2)\), any remaining index with \(a_k<t\) has \(k-1<Nt/c\), and its negative logarithm is at most \(\log(N/[c(k-1)])\).
Summing these bounds gives
\[
 \frac1N\sum_{\substack{k\ge k_N\\a_k<t}}|\log a_k|
 \le C t(1+|\log t|)+O(\log N/N).
 \tag{One-variable-negative-tail}
\]
The estimate follows by comparison of the decreasing function \(\log(N/(cx))\) with its integral from \(1\) to \(Nt/c\); changing an endpoint contributes \(O(\log N)\).
It is uniform in \(N\) for fixed \(t\), with constants allowed to depend on the fixed intermediate theorem.

The [accepted finite-variance controls](../claims/Yin_C_F0186_v4.md#statement) supply almost-sure weak convergence of this singular law to the distribution of \(|s-\lambda|\) and the positive logarithmic tail control.
The limiting negative logarithm is integrable: for real \(\lambda\) the semicircular density is bounded and \(|\log|t-\lambda||\) is locally integrable, while for nonreal \(\lambda\) the distance is bounded below.
A logarithm clipped at a fixed lower and upper cutoff is bounded and continuous on the singular-value half-line.
Apply the weak law to that clipped function, remove its positive cutoff using the accepted tail control, and then remove its negative cutoff using (One-variable-negative-tail) and integrability of the limit.
Since the floor event has probability tending to one, this proves
\[
 \frac1N\log|\det(W_N-\lambda I)|
 \longrightarrow
 \int_{-2}^2\log|t-\lambda|\,d\mu_{\mathrm{sc}}(t)
 \quad\text{in probability through even }N.
 \tag{One-variable-even-log}
\]
No first Borel--Cantelli step is applied to the nonsummable scalar-premise failures.

Now fix \(H(t)\in M_m(\mathbb C[t])\), with arbitrary fixed complex matrix coefficients, and set \(q(t)=\det H(t)\).
The finite spectral identity and free fiber identity proved in the preceding section remain valid for every Hermitian \(W_N\); their proof uses unitary diagonalization, not reality of its entries.
If \(q\equiv0\), every finite \(H(W_N)\) is singular and its free logarithm is \(-\infty\), so the full determinant assertion is immediate.
Otherwise write \(q(t)=a\prod_{\ell=1}^d(t-\lambda_\ell)\), including multiplicities and allowing \(d=0\).
There are only finitely many roots.
Apply (One-variable-even-log) to each root and use a finite union of the exceptional probability events, without assuming independence between the determinants.
The exact finite product identity then yields
\[
 \frac1{mN}\log|\det H(W_N)|
 \longrightarrow
 \frac1m\int\log|q(t)|\,d\mu_{\mathrm{sc}}(t)
 =\log\Delta_{\operatorname{tr}_m\otimes\tau}(H(s))
 \quad\text{in probability through even }N.
 \tag{Matrix-polynomial-even-log}
\]
For nonzero constant \(q\), the normalized logarithm is already the same constant at every size.
For every nonzero \(q\), the target above is finite.

The universal almost-sure upper bound in C_F0186_v4 applies to the scalar polynomial \(q\), and the exact finite identity transfers it to \(H(W_N)\) with factor \(1/m\).
The [accepted marginal criterion](../claims/Yin_C_F0190_v1.md#coupling-criterion), applied to the even-dimensional sequence, gives the matching almost-sure lower recurrence under every allowed coupling.
Equivalently, choose from the convergence in probability a deterministic subsequence of even dimensions whose errors at tolerances \(1/j\) have probabilities at most \(2^{-j}\), and use the first Borel--Cantelli lemma together with the full-sequence upper bound.
Thus (Even-scalar-premise) suffices for
\[
 \limsup_{N\to\infty}\frac1{mN}\log|\det H(W_N)|
 =\log\Delta_{\operatorname{tr}_m\otimes\tau}(H(s))
 \quad\text{almost surely}.
 \tag{One-variable-matrix-limsup}
\]
This implication does not assert full-sequence logarithmic convergence, and it retains the ordinary determinant at singular matrices.

The same conditional conclusion covers a fixed real linear combination \(Y_N=\sum_{j=1}^d r_jW_j^{(N)}\) of the original independent complex Hermitian inputs, provided (Even-scalar-premise) holds for the normalized combined law specified next.
If \(\sigma^2=\sum_jr_j^2>0\), then \(Y_N/\sigma\) is again a fixed-law centered variance-one complex Hermitian Wigner matrix: each upper entry is the corresponding independent scalar sum, the lower entry is its conjugate, and its real diagonal has finite second moment.
Apply the one-variable implication to the fixed matrix polynomial \(t\mapsto H(\sigma t)\); the matching free combination \(\sum_jr_js_j\) is semicircular of variance \(\sigma^2\).
Premises for the separate original inputs alone would not establish the needed floor for this combined law.
If every \(r_j\) vanishes, \(H(Y_N)=H(0)\otimes I_N\) is deterministic and the equality follows directly, including a zero determinant.
In particular the conditional result includes \(A_0+B\sum_jr_jW_j^{(N)}\) with arbitrary \(A_0,B\), while several unrelated coefficient matrices in the general F0013 contract remain outside this reduction.
The single scalar premise is still the precise missing input for the unconditional complex-law extension in this Draft; no new adopted Claim or independent review is asserted here.

<a id="scalar-affine-synthesis"></a>
## Conditional synthesis for every scalar affine coefficient tuple

There is a second direct application to the original scalar-coefficient case of F0013, with arbitrary complex coefficients rather than just a real linear combination.
This is a conditional synthesis of the [non-line floor module](Yin_D_F0027.md#generic-floor-conditional) and the [pure-imaginary investigation](Yin_D_F0029.md#scope), together with the accepted C_F0194_v6 phase-line theorem.
It does not adopt either continuing Draft as an independently reviewed input.
The related elliptic literature has already been checked at its narrower covariance and coupling scope in [the existing source comparison](../ledger/Yin_L_F0061_v1.md#complex-covariance-scope-beyond-the-scalar-elliptic-benchmark); no general elliptic-law theorem is substituted here.

The two provisional floor inputs required by this synthesis are precise.
The non-line input is the displayed uniform in-probability theorem in D27, whose generic linear hypothesis must still be discharged.
The pure-imaginary input is an in-probability floor for \(W_N+F_N\), with upper law \(i\eta\), any independent real finite-second-moment diagonal law, and independent polynomially bounded complex shift, on the event
\[
 s_{k_N}\!\left(\operatorname{sym}(W_N+F_N)_{[N]\setminus\{i\}}\right)
 \ge N^{-L_0}\quad\text{for every }i,\qquad
 k_N=4\lfloor\sqrt N\rfloor+1.
 \tag{Symmetric-quantile-premise}
\]
Here \(\operatorname{sym}D=(D+D^T)/2\), singular values are decreasing, \(L_0\) is fixed, and the floor failure on this event must tend to zero uniformly over deterministic shifts before conditioning on an independent random shift.
The guard may involve the noise diagonal; it is not assumed independent of the matrix.
The exceptional shift-norm and quantile-guard probabilities are added after conditioning and integration.
This exact uniformity is needed below and is part of the provisional input, rather than inferred from a result for a single fixed shift.
For pure-imaginary noise with identically zero diagonal and a skew shift, the separate even-dimensional floor follows from the accepted C_F0194_v6 second-smallest estimate and the fully proved, but still development-status, pairing identity in D29.

Fix the original independent Wigner inputs, \(a_0,a_1,\ldots,a_d\in\mathbb C\), and write
\[
 Z_N=a_0I_N+\sum_{j=1}^d a_jW_j^{(N)},\qquad
 z=a_0+\sum_{j=1}^d a_js_j.
\]
If every \(a_j\), \(j\ge1\), vanishes, the determinant assertion is deterministic, including \(a_0=0\).
Otherwise call those indices with \(a_j\ne0\) active.
The following alternatives exhaust their fixed centered off-diagonal laws.
A law not supported in a real line through zero is covered by the provisional non-line input.
A law supported in such a line has the form \(c\eta\), with \(|c|=1\), real centered variance-one \(\eta\), and is covered by the accepted phase-line theorem when \(\operatorname{Re}c\ne0\).
Centering ensures that a one-dimensional affine support line contains zero.
The only remaining line is the imaginary axis.

If an active input is in either of the first two classes, choose it as the exposed index \(j_0\) and write
\[
 Z_N/a_{j_0}=W_{j_0}^{(N)}+F_N,\qquad
 F_N=(a_0I_N+\sum_{j\ne j_0}a_jW_j^{(N)})/a_{j_0}.
\]
The shift is independent of the exposed Wigner input within each size.
Its entries and its norm have polynomial guards with arbitrarily high polynomial probability after choosing the exponent large enough: \(\mathbb E\|W_j^{(N)}\|_F^2=O(N)\), and a finite union and Markov's inequality suffice.
Condition on \(F_N\), apply the appropriate uniform floor, then add the guard failure.
Fixed multiplication by \(a_{j_0}\) is absorbed by enlarging the precision exponent.
This proves a polynomial least-value floor in probability for \(Z_N\) through all dimensions in these cases.

Suppose instead that every active off-diagonal law is purely imaginary.
Choose any active \(j_0\) and use the same decomposition.
All active off-diagonal Wigner parts are transpose-skew, even after multiplication by a complex coefficient.
Consequently
\[
 \operatorname{sym}(Z_N/a_{j_0})
 =\operatorname{diag}\!\left(
       a_0/a_{j_0}+\nu_1/\sqrt N,\ldots,
       a_0/a_{j_0}+\nu_N/\sqrt N\right),
 \qquad
 \nu_i=\sum_{j\ {\rm active}}(a_j/a_{j_0})\zeta_{j,i}.
 \tag{Affine-diagonal-guard}
\]
The \(\nu_i\) are independent copies of a fixed centered complex law with finite second moment.
Independence between its real and imaginary parts is not required.

If \(a_0\ne0\), finite second moment gives
\[
 \mathbb P\!\left\{\max_i|\nu_i|>
                   \tfrac12|a_0/a_{j_0}|\sqrt N\right\}
 \le N\,\mathbb P\{|\nu|>\tfrac12|a_0/a_{j_0}|\sqrt N\}=o(1).
\]
Indeed \(t^2\mathbb P\{|\nu|>t\}\le
\mathbb E[|\nu|^2\mathbf1_{\{|\nu|>t\}}]\to0\).
On its complement every principal symmetric part in (Affine-diagonal-guard) has all singular values at least \(|a_0/a_{j_0}|/2\), hence satisfies (Symmetric-quantile-premise).
If \(a_0=0\) and \(\nu\) is not identically zero, choose fixed \(\delta,p>0\) with \(\mathbb P\{|\nu|\ge\delta\}\ge p\).
A binomial Chernoff bound gives at least \(pN/2\) such diagonal coordinates outside probability \(\exp(-cN)\).
Deleting any one coordinate leaves at least \(pN/2-1>k_N\) of them for large \(N\), and their singular values are at least \(\delta/\sqrt N\).
Thus the same quantile premise holds, for example with any fixed \(L_0>1/2\), eventually on that event.
Both cases give the required all-size floor in probability from the provisional guarded input.

There remains \(a_0=0\), \(\nu=0\) almost surely.
The original diagonal variables are centered and independent across inputs, so
\[
 0=\mathbb E|\nu|^2
   =\sum_{j\ {\rm active}}
       |a_j/a_{j_0}|^2\,\mathbb E\zeta_j^2.
\]
Each active \(\zeta_j\) is therefore zero almost surely.
Both \(Z_N/a_{j_0}\) and the independent shift \(F_N\) are then complex transpose-skew.
For even \(N\), singular-value pairing equates the least and second-smallest values, and the accepted all-phase second-value theorem supplies the polynomial floor on the shift guard.
Odd singularity in this branch is retained rather than excluded.
We have obtained, conditionally on the two provisional inputs, an even-dimensional in-probability floor for every scalar affine tuple.

The logarithmic transfer has one additional point because \(z\) need not be normal.
For the chosen active index \(j_0\), apply C_F0187_v2 to \(W_{j_0}^{(N)}+F_N\) conditional on the independent shift, without a shift-norm restriction.
After multiplication by \(|a_{j_0}|\), the intermediate bound is \(a_k(Z_N)\ge c(k-1)/N\) for \(k\ge\lceil N^{3/4}\rceil+2\), outside summable failures.
C_F0186_v4 gives almost-sure weak convergence of the singular laws to the deterministic law \(\mu_{|z|}\).
The intermediate bound and the open-set form of weak convergence imply
\[
 \mu_{|z|}([0,t))\le Ct\qquad(t>0).
\]
To include the endpoint, apply this bound at \(t+\varepsilon\) and let \(\varepsilon\downarrow0\).
It follows that \(\mu_{|z|}\) has no atom at zero and its negative logarithm is integrable, since \(\int_0^1 Ct\,dt/t<\infty\).
Its positive logarithm is integrable because \(z\) is bounded in the free finite von Neumann algebra.
Thus \(\log\Delta(z)\) is finite whenever there is an active coefficient.

The floor, intermediate bounds and positive logarithmic tails now give the same clipped-logarithm argument as (One-variable-negative-tail), without any use of normality.
It proves \(N^{-1}\log|\det Z_N|\to\log\Delta(z)\) in probability through even dimensions.
The full-sequence almost-sure regularized upper bound and C_F0190_v1 then give
\[
 \limsup_{N\to\infty}N^{-1}\log|\det Z_N|
 =\log\Delta(z)\quad\text{almost surely under every allowed coupling}.
 \tag{Conditional-scalar-affine-limsup}
\]
This conditional deduction covers the whole \(m=1\) coefficient range of F0013 and every affine scalar instance of F0014, including zero constant term.
It does not cover general auxiliary matrix coefficients, arbitrary scalar noncommutative polynomials, or full-sequence Brown convergence.
The remaining work for an adopted conclusion is the complete non-line linear input, the pure-imaginary quantile-guard theorem and the applicable fixed whole-proof review of their use here.

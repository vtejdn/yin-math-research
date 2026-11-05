---
author: Yin
---

# Public literature boundaries for Wigner, Haar and permutation determinant limits

This is the bounded primary-source survey requested by Yin on 2026-11-05.
It compares the exact [matrix-pencil Task F0013](../tasks/Yin_T_F0013_v1.md#contract) and [scalar-polynomial Task F0014](../tasks/Yin_T_F0014_v1.md#contract) with independent Haar-unitary and uniform-permutation models.
Selected original statements and applicability interfaces were inspected by the main agent and three assigned source-search agents.
This is not an exhaustive nonexistence proof, a new independent proof audit, or a review of the correctness or priority of the repository's internal C_F0186 results.
Published or publicly posted results, explicit conjectures, and elementary applicability deductions are distinguished below.

<a id="wigner-status"></a>
## Exact status supported for F0013 and F0014

The search found no public theorem or counterexample covering either complete fixed-law finite-second-moment, arbitrary-cross-size-coupling, fixed-parameter almost-sure limsup contract.
It found strong and current explicit evidence for closely related unresolved questions.
That supports treating the exact contracts as unresolved by the inspected literature; it does not certify that their precise formulations have already appeared as named public open problems.

| Source and inspected locator | Actual statement and boundary |
| --- | --- |
| [MS24, Section 5, Conjecture 1](https://arxiv.org/html/2406.15922v1#S5) | Integer coefficient matrices, centered GUE block pencils and rank-nondecreasing covariance; eventual invertibility and convergence of the normalized determinant root to the capacity formula, both almost surely and in expectation, are conjectured. This is a full-limit conjecture in a narrower model, not the exact finite-variance limsup statement. |
| [Kar26, Section 12, Random matrices](https://arxiv.org/html/2610.15180v1#S12) | The October 2026 preprint still cites that conjecture and proposes the shifted analogue. Its variational formula identifies the free target but expressly does not address the smallest-singular-value contribution. |
| [Han26, Theorems 1.2--1.5 and Questions 1.6--1.8](https://arxiv.org/html/2606.01664v1#S1) | Arbitrary-degree holomorphic Ginibre polynomials are treated, with weak ESD convergence in probability and a fixed-shift singular-value bound away from P(0). The non-Gaussian extension assumes planar density and high moments. Real Gaussian, density-free, adjoint and exceptional-shift directions are not a theorem for the present Wigner contracts. |

The original scopes and retained versions remain at [MS24](../audits/literature/MS24/readme.md), [Kar26](../audits/literature/Kar26/readme.md), and [Han26](../audits/literature/Han26/readme.md).
An unresolved full-limit conjecture does not logically imply that its weaker limsup version is unresolved.
Likewise, an open Brown-measure convergence question is not identical to the unregularized determinant question at every prescribed parameter.
The internal [GUE result](../claims/Yin_C_F0186_v3.md#statement) is project research evidence, not a pre-existing public theorem supplied by this survey.
No Task completion or refutation follows from the bibliographic findings alone.

### Probability convergence can suffice for the limsup task

Suppose the same scalar normalized logarithm converges in probability to a finite deterministic value c, and an almost-sure upper bound limsup at most c is available.
Choose a deterministic increasing subsequence with probability of deviation exceeding 1/k at most 2^{-k}.
First Borel--Cantelli gives convergence to c on that subsequence under any allowed coupling, and hence the full limsup equals c almost surely.
Thus it would be incorrect to reject a genuine fixed-parameter logarithmic probability limit merely because it is not a full almost-sure limit.
Weak ESD convergence in probability alone does not supply this scalar logarithmic premise.
The [earlier upper-limit analysis](Yin_L_F0061_v2.md) retains the separate full-sequence Brown obstruction.

<a id="haar-pencils"></a>
## Independent Haar-unitary matrix pencils

For fixed coefficient size m, let
\[
 L_N=A_0\otimes I_N+\sum_{j=1}^r A_j\otimes U_j^{(N)},\qquad
 L=A_0\otimes1+\sum_j A_j\otimes u_j,
\]
where the U_j are independent Haar U(N) matrices at each size and the u_j are free Haar unitaries.
The ordinary normalization is (mN)^{-1} log absolute determinant.
Adjoint terms, if included, retain their relation to the same U_j; they cannot be replaced by additional independent variables.

[CM14, Corollary 2.3](../audits/literature/CM14/readme.md), printed p. 154, explicitly supplies the matrix-coefficient strong-convergence interface.
[Sni02, Lemma 2](../audits/literature/Sni02/readme.md), arXiv v4 pp. 5--6, gives the logarithmic upper-semicontinuity direction.
The following are direct applicability consequences in an almost-sure strong-convergence realization.

- The upper bound \(\limsup_N(mN)^{-1}\log|\det L_N|\le\log\Delta(L)\) is available.
- If \(\Delta(L)=0\), it already gives logarithmic convergence to minus infinity and determinant-root convergence to zero.
- If L has a bounded inverse, the full logarithmic limit follows from strong convergence and a spectral gap.
  Indeed approximate the inverse of L*L by a polynomial q so that the norm of I-(L*L)q(L*L) is less than one; the same strict inequality holds eventually for L_N*L_N by strong convergence.
  This supplies a uniform inverse bound, after which log is a bounded continuous spectral test on the relevant interval.
- The remaining general case is positive FK determinant without a bounded inverse.
  No theorem covering arbitrary fixed matrix coefficients in that case was located in this search.
  This is a qualified search result, not a categorical certification of openness.

### New determinant-moment results and their domains

[JR26](../audits/literature/JR26/readme.md), *Determinants of random unitary pencils*, is published in JFA 291(6) (2026), article 111555.
Its inspected arXiv v1 proves scalar and triangular-coefficient cases of an averaged determinant formula.
The general formula left conjectural in that edition is addressed by [JvRR26](../audits/literature/JvRR26/readme.md), *Free versions of the strong Szego limit theorem*, arXiv:2607.25980v1, 28 July 2026.
Therefore that earlier averaged-moment conjecture must not be reported as still open without this update.

For monic pencils L_A(U)=I+sum A_j tensor U_j, JvRR26 Theorem 1.6 proves an expectation formula for determinant products under
\[
 \rho\!\left(\sum_j A_j\otimes\overline{A_j}\right)<1
\]
and the analogous condition for the other coefficient tuple.
In particular, taking the same tuple on both sides gives
\[
 \lim_N\mathbb E|\det L_A(U)|^2
 =\det\!\left(I_{m^2}-\sum_j A_j\otimes\overline{A_j}\right)^{-1}.
\]
This is an unnormalized second-moment statement with a strict stability hypothesis, not an arbitrary-coefficient unregularized log-determinant theorem.
Proposition 6.1(2) treats nonnegative powers in the row-ball setting; Remark 6.3 expressly prevents a blanket extension to negative powers.
Theorem 6.2 has stronger full-C*-spectral-radius requirements on denominator pencils, and Corollary 7.7 retains rational-domain and strict-stability conditions.
The main agent retained and inspected the original 31-page PDF; the selected passages are pp. 4--6 and 23--29.
No proof of general negative-logarithm uniform integrability is imported from these positive-moment results.

[BD13, Theorem 1.2](../audits/literature/BD13/readme.md) proves weak ESD convergence in probability for the specified equal-weight sums of independent Haar matrices.
Its Lemma 3.2 gives a logarithmic limit in probability for Lebesgue-almost every shift, not every fixed shift or every matrix-coefficient pencil.
[RV14, Theorem 1.1](../audits/literature/RV14/readme.md) gives a polynomial small-singular-value estimate for D+U with U Haar on the whole U(n).
For m greater than one, I_m tensor U(N) is not Haar on U(mN), so that theorem does not automatically solve the block pencil.

<a id="single-haar"></a>
## One Haar unitary reduces to the classical characteristic polynomial

Consider a fixed matrix Laurent polynomial F(z), including F(z)=A_0+zA_1+z^{-1}B_1, and put f(z)=det F(z).
Unitary spectral decomposition gives
\[
 \det F(U_N)=\prod_{\lambda\in\operatorname{spec}U_N} f(\lambda),
 \qquad
 \log\Delta_{\operatorname{tr}_m\otimes\tau}(F(u))
 =\frac1m\int_{\mathbb T}\log|f(z)|\,dm(z).
\]
If f is identically zero, both ordinary determinant quantities are zero.
Otherwise f is a nonzero Laurent polynomial and has a finite root factorization.
Its off-circle factors are covered by the ordinary CUE weak spectral limit with a continuous logarithmic test.
For a root on the circle, rotational invariance and [BHNY08, Section 4](../audits/literature/BHNY08/readme.md), PDF pp. 15--17, give mean zero and variance O(log N) for the real log-characteristic-polynomial value.
Chebyshev at deviation epsilon N has summable bound O(log N/N^2), so the normalized logarithm tends to zero almost surely by first Borel--Cantelli, without cross-size independence.
Combining the finitely many factors proves the full normalized logarithmic limit for this one-Haar model.
This is a direct application of the classical fixed-point moment formula, not a newly located theorem under the exact pencil title.
The source's coupling-specific law of the iterated logarithm is not used for this conclusion.

<a id="permutation-obstruction"></a>
## Uniform permutations: the ordinary determinant question is false in general

For one unitary, C[u,u*] is the Laurent polynomial algebra because u*=u^{-1}.
For a nonzero Laurent polynomial
\[
 p(z)=a z^b\prod_{j=1}^q(z-\alpha_j),
\]
write C_k(pi_N) for the number of k-cycles of a uniform permutation and K_N=sum C_k.
The characteristic-polynomial cycle formula, inspected in [Zei13, equation (2.5)](../audits/literature/Zei13/readme.md), gives
\[
 |\det p(P_N)|=|a|^N\prod_{j=1}^q\prod_{k=1}^N
 |\alpha_j^k-1|^{C_k(\pi_N)}.
 \tag{Cycles}
\]
The Laurent monomial has modulus one on every permutation eigenvalue.
By the [FK--Mahler convention](../audits/literature/Den09/Yin_U001.md#mahler-measure),
\[
 \Delta(p(u))=M(p),\qquad
 \log M(p)=\log|a|+\sum_j\log^+|\alpha_j|.
\]
For p(z)=z-1, each permutation fixes the constant vector, and hence
\[
 |\det(P_N-I)|^{1/N}=0\quad\text{for every }N,
 \qquad\Delta(u-1)=M(z-1)=1.
\]
Thus even the dimension-limsup equality fails, irrespective of cross-size coupling.
This is a complete elementary counterexample to the unrestricted ordinary-determinant formulation.
For several independent permutations, all inputs and their inverses still fix the same constant vector.
The same example p=u_1-1 therefore persists for multiple generators.

<a id="permutation-positive-cases"></a>
## Positive permutation cases and the role of arithmetic

The classical theorem inspected in [HKOS00, Theorem 1.2(i)](../audits/literature/HKOS00/readme.md), printed p. 337, is a distributional CLT at a fixed finite-type irrational angle.
[Zei13, Theorem 2.7 and Definition 3.15](../audits/literature/Zei13/readme.md) retain the finite-type lower bound and generalize the class functions and sampling law.
Those CLTs alone do not imply almost-sure convergence.
The following elementary cycle estimates supply the applicable normalized conclusion separately.

<a id="finite-type"></a>
Definition (finite-type irrational angle).
An irrational real number \(\theta\) is of finite type when there are \(c,A>0\) such that \(\|k\theta\|_{\mathbb R/\mathbb Z}>c k^{-A}\) for every positive integer \(k\), where the norm denotes distance to the nearest integer.
This is the inspected Zei13 Definition 3.15 convention.
For \(\alpha=e^{2\pi i\theta}\), it is equivalent, after changing constants, to the unit-circle bound (Diophantine) below.

Insertion of the last symbol gives the cycle-count generating polynomial
\(\sum_{\pi\in S_N}t^{K(\pi)}=t(t+1)\cdots(t+N-1)\).
Consequently \(\mathbb E2^{K_N}=N+1\).
For a sufficiently large fixed c, Markov gives a summable bound for K_N>c log N.
Thus K_N=O(log N) almost surely under any coupling with uniform permutation marginals.

For each root off the unit circle,
\[
 \big|\log|\alpha^k-1|-k\log^+|\alpha|\big|\le C_\alpha.
\]
If a unit-circle root is not a root of unity and satisfies
\[
 |\alpha^k-1|\ge c_\alpha k^{-A_\alpha}\quad(k\ge1),
 \tag{Diophantine}
\]
the same difference is bounded by C_alpha log(k+1).
Equation (Cycles) therefore gives
\[
 \big|\log|\det p(P_N)|-N\log M(p)\big|
 \le C_p K_N\log(N+1),
\]
with the logarithmic factor unnecessary if there are no unit-circle roots.
Dividing by N proves ordinary determinant-root and logarithmic convergence almost surely under these hypotheses, for arbitrary cross-size coupling.
Without a lower bound, the upper estimates still give limsup of the root at most M(p), but not equality.
These conclusions are elementary applicability deductions from the cycle formula and the displayed assumptions; they are not an unqualified strengthening attributed to the cited CLTs.

<a id="permutation-coupling"></a>
## Even the upper limit can depend on the coupling

For p(z)=z+1, the determinant is nonzero exactly when all cycles have odd length, and then its modulus is 2^{K_N}.
The probability of that event is
\[
 q_N=[x^N]\exp\!\left(\sum_{k\text{ odd}}x^k/k\right)
 =[x^N]\sqrt{(1+x)/(1-x)}
 =\frac{\binom{2\lfloor N/2\rfloor}{\lfloor N/2\rfloor}}{4^{\lfloor N/2\rfloor}}
 \sim\sqrt{2/(\pi N)}.
\]
Thus the determinant root converges to zero in probability although M(z+1)=1.
If the permutations are independent across sizes, both the nonzero and zero events occur infinitely often by second Borel--Cantelli.
The cycle bound above gives root tending to one along the nonzero events, hence almost-sure limsup one and liminf zero.

For a different lawful coupling, take a single uniform random variable V in [0,1].
At size N, sample uniformly conditional on all-odd cycles when V<=q_N, and uniformly on the complement otherwise, using extra randomness for these conditional choices.
Each marginal permutation is uniform.
Since q_N tends to zero, almost surely only finitely many all-odd events occur; the determinant root is eventually zero and its limsup is zero.
This construction proves the coupling distinction without any appeal to a particular Feller coupling theorem.
It is a local elementary comparison, not a claim about the Wigner Tasks.

<a id="reduced-determinants"></a>
## Removing the zero singular values changes the question

For a finite matrix, the [retained kernel-removed convention](../audits/literature/Luc22/Yin_U001.md#luc22-kernel-removed-determinant), with normalization by its original dimension, is
\[
 D_N^+(A)=\left(\prod_{s_i(A)>0}s_i(A)\right)^{1/N},
\]
with an empty product equal to one and normalization by the original dimension N.
It is distinct from the ordinary determinant and from merely restricting to the orthogonal complement of the common constant vector.
For p(z)=z-1, each k-cycle contributes k after deleting its zero value, so
\[
 D_N^+(P_N-I)=\left(\prod_k k^{C_k(P_N)}\right)^{1/N}\longrightarrow1
 \quad\text{almost surely}.
\]
The bound is at most exp(K_N log N/N), and at least one, proving the limit directly.

The selected [Luc02 book manuscript](../audits/literature/Luc02/readme.md), Definition 3.11 and Example 3.12, printed pp. 127--128, use the zero-removing convention.
Lemma 13.53, printed pp. 482--485, concerns cyclic finite quotients and nonzero polynomials over Q[Z]; equation (13.55) explicitly omits zero factors.
Its arithmetic estimate (13.65) uses a polynomial lower bound for nonzero alpha^N-1 at algebraic roots, quoting Shorey--Tijdeman, Corollary B1, p. 30.
That original number-theory proof was not re-audited in this survey.
The lemma is not an ordinary-determinant theorem for uniform random permutations.
The source's Example 13.69, printed pp. 485--486, concerns specially chosen complex coefficients and cyclic quotient subsequences, not a uniform random permutation law.

For uniform permutations, if all non-root-of-unity unit-circle roots satisfy (Diophantine), the reduced cycle product has logarithm k log M(p)+O_p(log(k+1)).
Indeed a root of unity belonging to the k-th roots contributes k after its own zero is deleted; deleting the other finitely many polynomial zero locations changes the remaining factors only by constants depending on p.
The other roots obey the previous bounds, and multiplicities change only the constants.
Summing over cycles gives the same K_N log N error and the reduced limit M(p).
This explains the positive arithmetic cases without silently replacing the user's ordinary determinant by a reduced one.

<a id="finite-quotient-counterexample"></a>
## Recent group-approximation counterexample and its scope

[Kam26, Theorem 2](../audits/literature/Kam26/readme.md), arXiv:2609.15567v1 of 14 September 2026, concerns the integral Heisenberg group H and its level-3^i principal congruence subgroups H_i.
For the stated element A=1-2a+2b it asserts
\[
 \limsup_i\Delta_{H/H_i}(A_i)\le5^{1/3}<2=\Delta_H(A).
\]
Definition 4 uses the reduced convention, but Proposition 9 makes the finite matrices in this example invertible.
Thus the obstruction is not solely a kernel-convention issue.
The theorem is about a deterministic quotient chain with group relations, not independent uniform permutations or free Haar generators.
Its statement, convention and invertibility locator were checked; its complete proof was not independently audited here.

## Consequences for the requested search

F0013 and F0014 retain their existing exact contracts and active lifecycle.
The source search supplies no completed or refuted decision and no categorical certificate of public openness for their precise formulations.
For several Haar variables, record the available upper bound, zero-determinant and bounded-inverse cases, the newer strictly stable moment theorems, and the unresolved search boundary for arbitrary coefficients separately.
For a single Haar variable, the determinant problem reduces to classical Laurent-polynomial/CUE theory.
For uniform permutations, the unrestricted ordinary determinant assertion is false; useful replacements must specify root restrictions, reduced determinant convention and any cross-size coupling quantifier.
The [Haar-pencil approximation Task](../tasks/Yin_T_F0015_v1.md#contract) and [reduced permutation determinant Task](../tasks/Yin_T_F0016_v1.md#contract) use this comparison as starting evidence.
Their contracts separately ask for full almost-sure limits and upper-limit equalities under arbitrary cross-dimensional couplings and under independence across dimensions.
The later [internal permutation classification](../claims/Yin_C_F0189_v1.md#decision-classification-reviewed) resolves that separate Task at its recorded proof and independent-review scope; it is not a public theorem located by this earlier bounded survey.

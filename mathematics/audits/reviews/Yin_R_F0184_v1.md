---
author: Yin
---

# GGOW20 Continuity Reconstruction: Isolated Mathematical Recheck

## Review act and inputs

Review act: 2026-11-02T04:36 UTC.
Human record author: Yin.
Reviewer: a separately organized agent outside the substantive development of the inspected proof.
This is a targeted independent mathematical recheck of the complete local continuity reconstruction, including its affected input interfaces, rather than conformity acceptance or a review of all GGOW20 mathematics.
The reviewer received the fixed current proof, exact scope, applicable rules and the existing issue's mathematical subjects, without the author's proof-development dialogue, explanations or an earlier verdict on this reconstruction.
The reviewer read U004 and its necessary U002/U003 mathematical inputs and formed the initial no-gap finding before consulting the source README and the earlier R_F0176 findings.
Those later comparisons supplied source scope and historical boundaries, rather than premises for the initial verdict.
The reviewer contributed no repair and made no edit to U004 or the source README.

The inspected input is the 2026-11-02 working-tree mathematics in [U004, continuity reconstruction](../literature/GGOW20/Yin_U004.md#continuity-reconstruction), with the explicit rational real/imaginary entry model and the parameter choices
\[
h:=100(n+1)^8(b+\log(2m)+1),\quad K:=e^h,\quad
q:=100h^2,\quad P:=512qn^3,\quad
s:=\log(1/\delta),\quad \epsilon:=2q/s.
\]
This binding covers that mathematical reconstruction and its specified recurrence/progress inputs; later changes to its mathematical hypotheses, estimates or conclusion require a corresponding applicability judgment.
Changing only its pending-review prose does not change this inspected mathematical object.

The source comparison used the locally retained full published *Operator Scaling: Theory and Applications*, Foundations of Computational Mathematics 20 (2020), pp. 223-290, [GGOW20 PDF](../../literature/pdf/GGOW20.pdf).
The reviewer read printed pp. 269-274 for Theorem 4.5, pp. 250-253 for the integral-capacity proof and normalization, pp. 257-258 for Definition 3.8 and Lemma 3.9, p. 242 for the dual variational statement, and pp. 274-275 for quantitative progress.
Printed pp. 270, 272 and 273 were also rendered and visually inspected.
The singular-marginal and relative-error passages on pp. 276-277 and 279 were read separately for the limited formula comparisons below.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Continuity reconstruction finding](#continuity-reconstruction-finding) | independently reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Continuity reconstruction finding](#continuity-reconstruction-finding) | [U004 continuity reconstruction](../literature/GGOW20/Yin_U004.md#continuity-reconstruction) | Complete local proof at its explicit rational real/imaginary input scope: bit-model bounds, scalar case, stopping parity, positivity, inverses, perturbation transfer, determinants and final modulus with the displayed h,q,P. |
| [Continuity reconstruction finding](#continuity-reconstruction-finding) | [U004 recurrence and progress inputs](../literature/GGOW20/Yin_U004.md#ggow20-u004) | Exact recurrence, similarity trace-square identity, normalized capacity upper bound and the Lemmas 5.1-5.2 progress estimate as used by this continuity proof; no rounded algorithm or polynomial-bit approximation re-audit. |
| [Continuity reconstruction finding](#continuity-reconstruction-finding) | [U002 capacity input](../literature/GGOW20/Yin_U002.md#ggow20-u002) | Theorem 2.18 proof interface and normalization determinant scaling, including applicability of the Gaussian-integer extension explicitly made in the reconstruction; external blow-up and finite-grid foundations remain accepted at the recorded depth. |
| [Continuity reconstruction finding](#continuity-reconstruction-finding) | [U003 near-minimizer input](../literature/GGOW20/Yin_U003.md#ggow20-u003) | Capacity duality and corrected Lemma 3.9 with positive image and small-error hypotheses, including their exact applications to F_A,F_B; no whole Section 3 or tensor-product re-audit. |
| [Continuity reconstruction finding](#continuity-reconstruction-finding) | [U004 printed-formula objections](../literature/GGOW20/Yin_U004.md#quantitative-corrections) | Only the singular-marginal example and reciprocal error conversion were directly rechecked here; literal iteration and precision budgets remain outside this finding. |

## Continuity reconstruction finding

No mathematical gap was found in the complete inspected local reconstruction.
It establishes that for \(n,m,b\geq1\), rational real and imaginary parts of \(A_i\) with numerator and positive denominator bounded by \(2^b\), arbitrary complex \(B_i\) satisfying \(\|A_i-B_i\|\leq\delta\), and \(\operatorname{cap}(T_A)>0\), the explicit hypothesis \(0<\delta\leq e^{-P}\) implies
\[
\operatorname{cap}(T_B)>0,\qquad
\left|\frac{\operatorname{cap}(T_A)}{\operatorname{cap}(T_B)}-1\right|
\leq \frac{P}{\log(1/\delta)^{1/3}}.
\]
The case \(\delta=0\) is equality.
There is no asserted relative estimate at zero capacity or finite bit model for arbitrary real input.

### Arithmetic input and lower bounds

Selecting at most \(n^2\) members of the actual Kraus tuple spanning the same complex matrix space preserves every image range on positive semidefinite input, hence rank non-decrease.
The product \(d\) of the selected real and imaginary denominators satisfies \(d\leq2^{2n^4b}\).
Scaling these selected matrices by \(d\) gives Gaussian-integer entries.
In the inspected Theorem 2.18 proof, the integrality step requires a nonzero determinant of absolute value at least one; a nonzero Gaussian integer has that property as well.
The finite-grid and Hilbert-Schmidt steps retain the same bounds over these complex coefficients.
Thus the stated lower bound \(d^{-2n}n^{-2n}\) applies to the selected unscaled map, and positivity/determinant monotonicity transfers it to the full map.
This does not replace the full map when evaluating capacity.

Both selected marginals are positive definite.
After multiplication by \(d^2\), each is a positive definite Gaussian-integer Gram matrix, whose positive real determinant is a positive integer.
Their determinant lower bound and norm upper bound therefore give the displayed minimum eigenvalue estimate.
The full marginals dominate them; the full upper bound retains the actual \(m\), and right normalization divides capacity by the original \(\det T_A^*(I)\).
Direct comparison of these logarithmic estimates with \(h\) verifies all stated \(K\) bounds, including the map, adjoint and perturbation norms for arbitrary matrix arguments.
The dependence is polynomial in \(n,b,\log m\), with no assumption that the full tuple has \(m\leq n^2\).

For \(n=1\), \(\operatorname{cap}(T_A)=\sum_i|A_i|^2\), positive capacity supplies a nonzero selected scalar, and the same denominator argument and \(K\) estimates apply.
The first normalized scalar map has defect zero.
Consequently the continuity proof covers this case without invoking the separate spectral formula \(\alpha=(M^2n^2m)^{n-1}\), which would give an invalid bound at \(n=1\).

### Stopping point, orientation and inverse domain

The retained progress factor is \(\exp(\min(e_j,1)/6)\).
Together with \(\operatorname{cap}(T_1)\geq e^{-h}\) and the capacity upper bound one for normalized iterates, it gives a stopping index \(1\leq r\leq2+\lceil6(h+1)/\epsilon\rceil\).
The displayed estimate \(t\leq15h/\epsilon\) and induction on the exact recurrence give the stated \(R:=\exp(16h^2/\epsilon)\) bound for \(C:=S_{r-2}^{-1}\).
The first step uses the defined \(S_{-1}=I\).

For odd \(r\), the exact equalities are \(F_A=T_A^*\), \(F_A(C)=S_{r-1}\), and \(F_A^*(F_A(C)^{-1})=S_r\); for even \(r\), take \(F_A=T_A\).
Thus the residual in Lemma 3.9 and the determinant objective use the same map for each parity, with capacity duality supplying the original capacity in the odd case.
The equality of the recurrence trace square and \(\operatorname{Tr}(E_A^2)\) follows by similarity, without a Hermitian claim about \(CS_r\).

The lower bound \(U:=F_A(C)\geq(KR)^{-1}I\) and perturbation bound \(\|F_B(C)-U\|\leq KR\delta\) imply positive definiteness of \(V:=F_B(C)\) as soon as \(\theta:=K^2R^2\delta\leq1/2\).
The resolvent identity then gives precisely the stated inverse norms and \(2K^3R^3\delta\) difference bound.
This verifies the inverse domain before using either the residual or determinant comparison for \(B\).

### Residual, determinant and tolerance propagation

The two map/adjoint perturbation terms give
\[
\|E_A-E_B\|\leq K^2R^2\delta+2K^4R^4\delta
\leq3K^4R^4\delta=:a.
\]
Both residuals are Hermitian.
Using \(|\operatorname{Tr}(XY)|\leq n\|X\|\|Y\|\) yields \(\epsilon_B\leq\epsilon+n(2+a)a\leq\epsilon+9nK^4R^4\delta\) when \(a\leq1\).
The dimension factor is present.
The congruence \(U^{-1/2}VU^{-1/2}\) has eigenvalues in \([1-\theta,1+\theta]\), giving the stated reciprocal determinant interval.
Applying the corrected Lemma 3.9 to both maps is legitimate once \(\epsilon,\epsilon_B\leq1/(n+1)\); its positive lower factor proves the perturbed capacity is positive.

For the stated parameter choice, \(s\geq512qn^3\) gives \(\epsilon\leq1/(256n^3)\).
The inequality \(4h+64h^2+\log(9n)\leq100h^2=q\) holds for the displayed \(h\), and \(s e^{-s/2}\leq2/e\leq2q\).
Consequently every listed perturbation term is bounded by \(\zeta:=e^{-s/2}\leq\epsilon\).
This simultaneously ensures \(\theta\leq1/2\), \(a\leq1\), and \(\epsilon_B\leq2\epsilon\leq1/(n+1)\), rather than assuming positivity independently of the tolerance choice.
In the two-sided capacity ratio, all logarithmic arguments stay within the required \(1/2\) range.
For \(\rho:=\operatorname{cap}(T_A)/\operatorname{cap}(T_B)\), the stated estimates
\[
|\log\rho|\leq6n^{3/2}\sqrt\epsilon\leq3/8,
\qquad
|\rho-1|\leq12\sqrt{2q}\,n^{3/2}s^{-1/2}
\leq P s^{-1/3}
\]
follow with the displayed constants.
This closes the intended continuity conclusion with the enlarged polynomial, including all positivity and tolerance interfaces.

### Printed errors and actual limits

The published odd-index argument on p. 270 uses an approximate fixed point for the adjoint orientation while (21) evaluates the original-map objective; (34)-(35) repeat that orientation mismatch.
The local parity selection corrects the mathematical interface, rather than certifying those printed formulas.
Printed (33), p. 273, is false as an unrestricted elementary matrix estimate: \(n=2,D_1=11I,D_2=10I\) gives left side \(38\) and right side \(25\).
The local proof uses a valid trace estimate with the dimension factor and explicitly Hermitian residuals.
The source's smallness sentence accompanying (28) does not by itself supply the tolerance-dependent positive inverse bound; the local \(\theta\) estimate and final parameter coupling do.

The retained singular-marginal counterexample checks directly: \(E_{11},E_{21}\) give \(T(I)=I\) and \(T^*(I)=2E_{11}\).
A kernel vector of the adjoint marginal is in every Kraus kernel and supplies the rank-one obstruction, so the algorithm's zero-capacity output does not require the false claim that the other marginal is singular.
The relative-error objection also remains valid: \((1-\varepsilon)\widehat c\leq c\leq\widehat c\) gives the reciprocal bound \(\widehat c/c\leq(1-\varepsilon)^{-1}\), with the same issue in the printed squared factor.

The foundational rank/capacity, nonzero finite blow-up and finite-grid inputs remain accepted at their exact retained [U001](../literature/GGOW20/Yin_U001.md#ggow20-u001) and [U002](../literature/GGOW20/Yin_U002.md#ggow20-u002) depths; their original external proofs were not independently re-audited here.
The corrected near-stochastic and near-minimizer interfaces were checked for their actual hypotheses and use; this finding does not claim a new independent review of every earlier U003 proof or every source cited by GGOW20.
It does not certify the paper's literal quantitative formulas, Algorithms 3-4 iteration/precision budgets, the separate rounded polynomial-bit procedure, an implementation, strong polynomiality, optimal continuity constants, or formal verification.
It changes no Claim/Task assessment and clears no shared maintenance or erratum entry.

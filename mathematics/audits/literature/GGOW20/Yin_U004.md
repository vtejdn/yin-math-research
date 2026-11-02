---
author: Yin
---

# Rational Scaling, Precision, and Capacity Approximation

## Source and inspection

Source edition: Source: [GGOW20 source index](readme.md), full published *Operator Scaling: Theory and Applications*, Foundations of Computational Mathematics 20 (2020), pp. 223-290.

Passages: Locators: Proposition 4.1, Lemmas 4.2-4.4 and equations (15)-(20), pp. 261-269; Theorem 4.5, pp. 269-274; Lemmas 5.1-5.2, Theorems 5.3-5.4 and Algorithms 3-4, pp. 274-279.

Inspection: Rational recurrences, sensitivity mechanism and a conservative polynomial-precision reconstruction are audited within the scope below.


## GGOW20-U004

- Source: [GGOW20 source index](readme.md), full published *Operator Scaling: Theory and Applications*, Foundations of Computational Mathematics 20 (2020), pp. 223-290.
The registered key is retained; this unit supersedes no result of a different version silently.
- Artifact: [GGOW20.pdf](../../../literature/pdf/GGOW20.pdf), 68 pages.
Printed page equals PDF page plus 222.
- Locators: Proposition 4.1, Lemmas 4.2-4.4 and equations (15)-(20), pp. 261-269; Theorem 4.5, pp. 269-274; Lemmas 5.1-5.2, Theorems 5.3-5.4 and Algorithms 3-4, pp. 274-279.
- Original inspection: 2026-09-12, delegated source-audit agent, self-review.
Complete supplied Sections 4-5 were read.
Rational recurrences, sensitivity mechanism and a conservative polynomial-precision reconstruction are audited within the scope below.
Literal printed quantitative constants are **Questioned** where indicated.
The corrected continuity reconstruction below includes its inverse preconditions, parity choice and full tolerance propagation, with [isolated mathematical recheck](../../reviews/Yin_R_F0184_v1.md#continuity-reconstruction-finding) of the complete reconstruction and its affected interfaces at the stated limits.
- Kind: computational theorem interface, proof mechanism, and corrections.
No algorithm was implemented or run.

### Reusable mathematical interface

For a completely positive map
\[
T:M_n(\mathbb C)\longrightarrow M_n(\mathbb C),\qquad
T(X)=\sum_{i=1}^m A_iXA_i^*,
\]
with integer matrix input \(A_i\), there is a deterministic algorithm using a polynomial number of bit operations to decide whether \(T\) is rank non-decreasing.
There is also a deterministic polynomial-time algorithm, polynomial in the input bit length and \(1/\varepsilon\), that returns zero when capacity is zero and otherwise an estimate \(\widehat c\) satisfying
\[
(1-\varepsilon)\operatorname{cap}(T)\leq\widehat c
\leq(1+\varepsilon)\operatorname{cap}(T),\qquad 0<\varepsilon<1.
\]

This is the asymptotic interface of Theorems 1.27, 5.3-5.4, with the conservative error-budget reconstruction below.
It is not a certification of Algorithms 3-4 with every literal printed constant.
Rational inputs require denominator clearing and the corresponding determinant scaling factor; no arbitrary-real-number oracle bit model is asserted.
The scalar case \(n=1\) is evaluated directly: capacity is \(\sum_i|A_i|^2\).

Retain the actual input tuple when computing capacity.
Removing redundant Kraus matrices merely because they belong to the same span preserves the rank-nondecrease question but can change the map and its capacity.
The source often works with \(m\leq n^2\); a computational use must check that convention or carry the actual \(m\) in its input-size and norm bounds.

### Exact rational recurrence and what its trace measures

For \(T(I),T^*(I)>0\), set \(S_{-2}=S_{-1}=I\), \(S_0=T^*(I)\), and
\[
S_j=\begin{cases}
T(S_{j-1}^{-1}),&j\geq1\ \text{odd},\\
T^*(S_{j-1}^{-1}),&j\geq1\ \text{even}.
\end{cases}
\]
If \(T_j\) is the map obtained after \(j\) alternating normalizations, beginning with right normalization, equations (18)-(20) give, for \(j\geq1\),
\[
e_j=\operatorname{ds}(T_j)
=\operatorname{Tr}\bigl((S_{j-2}^{-1}S_j-I)^2\bigr),
\qquad
\operatorname{cap}(T_j)
=\frac{\operatorname{cap}(T)}
{\det(S_{j-2})\det(S_{j-1})}.
\]
Here the source's \(\operatorname{ds}\) is the sum of squared Hilbert-Schmidt marginal defects, as in Gur04-U001.
The product \(S_{j-2}^{-1}S_j\) need not be Hermitian.
Its trace-of-square expression is valid by **similarity** to the Hermitian marginal of \(T_j\); replacing it by its Hilbert-Schmidt norm is generally incorrect.

The recurrence follows by writing \(T_j(X)=C_jT(D_j^*XD_j)C_j^*\), \(P_j=C_j^*C_j\), \(Q_j=D_j^*D_j\).
Odd steps leave \(P_j\) fixed and replace \(Q_j\) by \(T^*(P_j)^{-1}\); even steps leave \(Q_j\) fixed and replace \(P_j\) by \(T(Q_j)^{-1}\).
The determinant factors telescope.
These equations were checked for both parities and the first step.
Although Section 4.1 begins by assuming \(T(I)=I\), these identities for \(j\geq1\) hold for the unnormalized input as well.
The first normalized step is what permits the subsequent capacity upper bound of one.

Use \(j\geq1\) in the rounded recurrence: Algorithm 4's invitation to check \(j=0\) requires values it does not define.
An optional \(j=0\) test must separately use the two actual input marginals, not invent \(U_{-2}\) in a formula justified only for normalized steps.

### Spectral control and stable rounding

Suppose \(n\geq2\), \(|(A_i)_{kl}|\leq M\), \(M\geq1\), and both marginals are nonsingular.
Set
\[
B=M^2n^2m,\qquad \alpha=B^{\,n-1}\geq B.
\]
Proposition 4.1 gives \(\alpha^{-1}I\leq T(I),T^*(I)\leq\alpha I\), and hence
\[
\alpha^{-(j+1)}I\leq S_j\leq\alpha^{j+1}I.
\]
The input lower bound uses the positive integer determinant of each marginal and its spectral upper bound.
Positivity transfers order bounds through \(T,T^*\), and inversion reverses them.
This proves the recurrence estimates inductively.
With \(n=1\), the source's \(\alpha=B^{n-1}=1\) would incorrectly bound an arbitrary nonzero scalar map; handle that case directly as above.

Let \(U_{-1}=I,U_0=S_0\), and round each recurrence value symmetrically, producing Hermitian errors \(\Delta_j\).
Entrywise absolute rounding error at most \(2^{-P}\) gives \(\|\Delta_j\|\leq n2^{-P}\), not merely \(2^{-P}\).
Lemmas 4.2-4.3 show, for \(j\leq t\) and sufficiently small \(\delta\geq\max_j\|\Delta_j\|\),
\[
(2^j\alpha^{j+1})^{-1}I\leq U_j\leq2^j\alpha^{j+1}I,
\qquad
\|S_j-U_j\|\leq(2\alpha)^{(2t+1)(t+1)}\delta.
\]
Their proof is a direct induction using
\[
A^{-1}-B^{-1}=A^{-1}(B-A)B^{-1}.
\]
The maintained positive spectral lower bounds are essential: this is not an unconditional stability estimate for inversion near a singular matrix.

Write \(M_j=S_{j-2}^{-1}S_j\) and \(N_j=U_{j-2}^{-1}U_j\).
Decompose their difference as
\[
M_j-N_j=S_{j-2}^{-1}(S_j-U_j)
+(S_{j-2}^{-1}-U_{j-2}^{-1})U_j.
\]
The plus sign before \(U_{j-2}^{-1}U_j\) in one printed line on p. 269 is an algebraic typo; the displayed difference here is the one used by the subsequent norm bound.
A conservative combination of the preceding estimates gives
\[
\|M_j-N_j\|\leq(2\alpha)^{10(t+1)^2}\delta.
\]
For the rounded defect \(\widetilde e_j=\operatorname{Tr}((N_j-I)^2)\), trace cyclicity and \(|\operatorname{Tr}A|\leq n\|A\|\) then give the sufficient uniform estimate
\[
|e_j-\widetilde e_j|
\leq n(2\alpha)^{12(t+1)^2}\delta.
\]
Increasing the fixed exponents only weakens these bounds.
Thus a polynomial number of bits in \(t,\log\alpha,\log(1/\eta),\log n\) makes the defect error at most any prescribed \(\eta>0\).
The literal p. 269 formula involving \(\log M\) without an additive constant would give zero bits at \(M=1\); this audit uses the explicit positive quantities \(\log_2(2\alpha)\) and a sufficient precision bound instead.

### Capacity approximation with a conservative error budget

The source's Lemmas 5.1-5.2 were checked completely.
If positive eigenvalues have sum \(n\) and squared deviation \(a\), their product is at most \(\exp(-\min(a,1)/6)\).
For \(a\leq1\), apply the cubic upper estimate for \(\log(1+x)\); for \(a>1\), contract the eigenvalue deviations radially to squared norm one, using monotonicity of the product along that segment.
Therefore every normalization whose nontrivial marginal has defect \(a\) increases capacity by at least
\[
\exp(\min(a,1)/6).
\]
The factor \(1/6\) must be retained.

The reconstruction retains two exact interfaces within GGOW20: [U002](Yin_U002.md#ggow20-u002)'s effective lower bound after the first normalization in Theorem 2.20, written \(\operatorname{cap}(T_1)\geq e^{-L}>0\) with computable \(L\) polynomial in input bit size; and [U003](Yin_U003.md#ggow20-u003)'s Lemma 3.4 near-doubly-stochastic lower bound
\[
\operatorname{cap}(T_j)\geq(1-\sqrt{n e_j})^n
\]
for a map with one marginal normalized and sufficiently small defect.
Their independent source checks belong to the other units and the [capacity-interface review](../../reviews/Yin_R_F0176_v1.md#capacity-ggow20-finding).
This section checks their use, not their original proof chains.

For a requested \(0<\varepsilon<1\), one adequate bookkeeping choice is
\[
\beta=\frac{\varepsilon^2}{256n^3},\qquad
\eta=\frac\beta4,\qquad
t=2+\left\lceil\frac{12(L+1)}\beta\right\rceil.
\]
Run the rounded recurrence and accept the first \(j\geq1\) with \(\widetilde e_j\leq3\beta/4\).
Ensure \(|e_j-\widetilde e_j|\leq\eta\).
Then acceptance implies \(e_j\leq\beta\).
If capacity is positive, failing to encounter a true \(e_j\leq\beta/2\) by this time would make capacity exceed one by the progress estimate, a contradiction.
Such a true small defect guarantees acceptance.
If capacity is zero, a sufficiently small defect is impossible by Lemma 3.4, so the same error margin prevents a false positive.

At acceptance, \(\operatorname{cap}(T_j)\in[1-\varepsilon/16,1]\) by the near-stochastic bound and Bernoulli's inequality.
Write
\[
Q=\det(S_{j-2})\det(S_{j-1}),\qquad
\widehat Q=\det(U_{j-2})\det(U_{j-1}).
\]
Ensure each eigenvalue of these two \(U\) matrices differs from the corresponding \(S\) eigenvalue by at most \(\varepsilon/(64n)\) times that \(U\) eigenvalue.
Weyl's inequality and the already proved lower spectral bound achieve this by further polynomial precision.
Multiplying the \(2n\) relative eigenvalue factors gives \(Q/\widehat Q\in[1-\varepsilon/16,1+\varepsilon/16]\), with room to spare for \(0<\varepsilon<1\).
Hence
\[
\operatorname{cap}(T)=\operatorname{cap}(T_j)Q
\]
implies \(\widehat Q/\operatorname{cap}(T)\in[1-\varepsilon,1+\varepsilon]\).
This explicitly accounts for the reciprocal when passing from a bound on capacity to a bound on the reported number.
More precisely, the two retained internal estimates give
\[
\frac1{1+\varepsilon/16}
\leq\frac{\widehat Q}{\operatorname{cap}(T)}
\leq\frac1{(1-\varepsilon/16)^2},
\]
and this interval is contained in \([1-\varepsilon,1+\varepsilon]\) for \(0<\varepsilon<1\).

For example, taking an integer \(P\) larger than
\[
30(t+2)^2\log_2(2\alpha)
+\log_2\!\left(\frac{1024n^2}{\varepsilon\beta}\right)+10
\]
satisfies the positivity, defect and relative-determinant error requirements above.
It is a deliberately loose sufficient bound, not the printed exponent in Theorem 5.4.
Every intermediate rounded entry has polynomially many integer and fractional bits; exact rational matrix inversion, multiplication and determinant computation on these matrices have polynomial bit cost.
This establishes the stated existence of a polynomial-time approximation procedure within the retained effective-capacity interfaces.
It does not assert strong polynomiality or dependence polynomial in \(\log(1/\varepsilon)\).

<a id="quantitative-corrections"></a>
### Literal quantitative claims not certified

The following defects were checked against the primary rendered pages; they do not negate the qualitative scaling or noncommutative-rank theorem.

- **Singular marginal argument, p. 276:** the proof of Theorem 5.3 incorrectly infers \(T(I)\) singular from \(T^*(I)\) singular.
  For Kraus matrices \(E_{11},E_{21}\) in \(M_2\), \(T(I)=I\) while \(T^*(I)=2E_{11}\).
  The algorithm's zero-capacity answer remains correct: a kernel vector \(v\) of \(T^*(I)=\sum_iA_i^*A_i\) has \(A_iv=0\) for every \(i\), so \(T(vv^*)=0\).
- **Iteration constant, p. 277:** the proof uses growth \(\exp(\varepsilon^2/n^3)\), although Lemma 5.2 supplies only \(\exp(\varepsilon^2/(6n^3))\) at that threshold.
  Theorem 5.3 prints \(t=2n^3\varepsilon^{-2}(1+10n^2\log(Mn))\); its proof then substitutes \(n^3\varepsilon^{-2}(1+10n^2\log(Mn))\).
  Neither displayed iteration count follows from that progress estimate alone.
  Retain a larger iteration budget as above; the printed exact budget is not justified by the displayed proof.
- **Error conversion, pp. 277 and 279:** \((1-\varepsilon)\widehat c\leq c\leq\widehat c\) gives \(\widehat c\leq c/(1-\varepsilon)\), not \(\widehat c\leq(1+\varepsilon)c\).
  On p. 279 the bounds with \((1-\varepsilon/2)^2\) have the same reciprocal problem.
  Reserve smaller internal tolerances before promising a symmetric relative error.
- **Rounded precision, pp. 277-279:** the printed \(P\) grows like \(\varepsilon^{-1}\), whereas the displayed Lemma 4.3 amplification for \(t=O(\varepsilon^{-2})\) has an exponent of order \(t^2\).
  The exact printed choice is
  \[
  P_{\mathrm{print}}:=\varepsilon^{-1}n^{12}\log^4(Mn)\log(n^4/\varepsilon^2).
  \]
  The claimed implication \(\|U_i-S_i\|\leq2^{-P/2}\) does not follow for all small \(\varepsilon\) from those supplied estimates.
  The generic polynomial \(P\) above repairs the asymptotic interface, but the printed precision choice is not certified.
- **Threshold arithmetic, p. 279:** from \(\widetilde e_j\leq\varepsilon^2/(4n^3)\) and \(|e_j-\widetilde e_j|<\varepsilon^2/n^4\), the bound needed to infer \(\operatorname{cap}(T_j)\geq1-\varepsilon/2\) does not follow as written.
  Use a stricter defect-error margin rather than dropping the extra term.
- **Upper determinant factor, p. 279:** the displayed eigenvalue estimates imply \(Q/\widehat Q\leq(1+\varepsilon/(4n))^{2n}\), which is strictly larger than \(1+\varepsilon/2\) when \(\varepsilon>0\).
  Thus they do not justify the printed assertion \(Q\leq(1+\varepsilon/2)\widehat Q\).
  The smaller \(\varepsilon/(64n)\) internal errors used above give the stated \(1+\varepsilon/16\) bound, since \((1+\varepsilon/(64n))^{2n}\leq e^{\varepsilon/32}\leq1+\varepsilon/16\).

<a id="continuity-reconstruction"></a>
### Continuity theorem: source statement and corrected reconstruction

Theorem 4.5, printed pp. 269-270, states that if \(A_i\) have entry bit complexity \(b\) and \(\|A_i-B_i\|\leq\delta\), then for a polynomial \(P(n,b,\log m)\) and sufficiently small \(\delta\leq e^{-P}\), positive capacity of \(T_A\) implies positive capacity of \(T_B\), and
\[
1-\frac{P(n,b,\log m)}{\log(1/\delta)^{1/3}}
\leq\frac{\operatorname{cap}(T_A)}{\operatorname{cap}(T_B)}
\leq1+\frac{P(n,b,\log m)}{\log(1/\delta)^{1/3}}.
\]
The ratio is intended in the positive-capacity case and \(0<\delta<1\).
For the local reconstruction, \(n,m\geq1\), \(b\geq1\), and the real and imaginary parts of each entry of \(A_i\) are rationals \(p/q\) with \(|p|,q\leq2^b\), \(q>0\).
This includes real rational and integral input; the \(B_i\) may be arbitrary complex matrices subject to the norm bound.
This is the usual rational bit model made explicit, rather than a guarantee for arbitrary real inputs without an encoding.
The case \(\delta=0\) is equality.
No relative guarantee at zero capacity is asserted.

The source uses \(T_A(T_A^*(C)^{-1})\) for an odd stopping index but evaluates \(\det T_A(C)/\det C\) in (21).
Lemma 3.9 must instead be applied to \(T_A^*\), using \(\det T_A^*(C)/\det C\), and likewise to \(T_B^*\) in (34)-(35).
Capacity duality from [U003](Yin_U003.md#ggow20-u003) then supplies the original capacities.
An even stopping index uses \(T_A,T_B\) themselves; no parity assumption is needed.
The following argument carries that choice and all inverse preconditions explicitly.

#### Uniform input bounds

Use natural logarithms and define
\[
h:=100(n+1)^8\bigl(b+\log(2m)+1\bigr),\qquad K:=e^h.
\]
The following deliberately loose bounds hold when \(\operatorname{cap}(T_A)>0\):
\[
\begin{gathered}
K^{-1}I\leq T_A(I),T_A^*(I)\leq KI,\qquad
\operatorname{cap}((T_A)_R)\geq e^{-h},\\
\|T_A(D)\|,\ \|T_A^*(D)\|,\ \|T_B(D)\|,\ \|T_B^*(D)\|
\leq K\|D\|,\\
\|(T_A-T_B)(D)\|,\ \|(T_A^*-T_B^*)(D)\|
\leq K\delta\|D\|\qquad(0<\delta\leq1).
\end{gathered}
\]
Here is sufficient arithmetic justification, including the dependence on \(\log m\).
Choose a basis of the span of the actual \(A_i\), consisting of \(k\leq n^2\) of those matrices.
Their completely positive map has the same rank-nondecrease property: for each positive semidefinite \(X\), the range of its image is \(\sum_i A_i\operatorname{ran}X\), which depends only on this span.
Let \(d\) be the product of denominators of the real and imaginary entries in this selected basis.
Then \(1\leq d\leq2^{2n^4b}\), and the selected matrices multiplied by \(d\) have Gaussian-integer entries.
The proof of [U002, Theorem 2.18](Yin_U002.md#ggow20-u002) applies unchanged to Gaussian integers: the sole integrality use is that a nonzero blow-up determinant has absolute value at least one.
Consequently the selected unscaled map has capacity at least \(d^{-2n}n^{-2n}\); positivity and determinant monotonicity give the same lower bound for \(T_A\).
Also \(\|A_i\|\leq\sqrt2\,n2^b\), so both full marginals are at most \(2mn^2 2^{2b}I\).
Each selected marginal is positive definite, its determinant is at least \(d^{-2n}\), and its norm is at most \(2n^4 2^{2b}\).
Its minimum eigenvalue is therefore at least \(d^{-2n}(2n^4 2^{2b})^{-(n-1)}\).
The full marginals dominate these selected marginals.
Right normalization divides capacity by \(\det T_A^*(I)\), so its capacity is at least \(d^{-2n}n^{-2n}(2mn^2 2^{2b})^{-n}\).
All the logarithmic bounds just displayed are dominated by \(h\).
Finally, the perturbation bounds follow from
\[
\|(T_A-T_B)(D)\|
\leq\sum_i(\|A_i\|+\|B_i\|)\|A_i-B_i\|\|D\|
\]
and the identical adjoint estimate, together with \(\|B_i\|\leq\|A_i\|+1\).
The selected basis is used only for these lower bounds; it does not replace the actual map when evaluating capacity.

#### A controlled approximate balancing point

Fix \(0<\epsilon\leq1\) and use the exact recurrence above.
Every normalized iterate has capacity at most one; a step whose defect exceeds \(\epsilon\) increases capacity by more than \(e^{\epsilon/6}\).
Since the first normalized capacity is at least \(e^{-h}\), some \(1\leq r\leq t\) has \(e_r\leq\epsilon\), where
\[
t:=2+\left\lceil\frac{6(h+1)}{\epsilon}\right\rceil
\leq\frac{15h}{\epsilon}.
\]
Indeed, otherwise the steps from \(T_1\) to \(T_t\) would give capacity at least \(\exp((t-1)\epsilon/6-h)>1\).
The marginal bounds and positivity give \(K^{-(j+1)}I\leq S_j\leq K^{j+1}I\) inductively.
Set
\[
C:=S_{r-2}^{-1},\qquad R:=\exp(16h^2/\epsilon),
\qquad R^{-1}I\leq C\leq RI,
\]
using \(S_{-1}=I\) when \(r=1\).
Choose \(F_A:=T_A^*\), \(F_B:=T_B^*\) when \(r\) is odd, and \(F_A:=T_A\), \(F_B:=T_B\) when \(r\) is even.
Then \(S_{r-1}=F_A(C)\), \(S_r=F_A^*(F_A(C)^{-1})\), and
\[
E_A:=C^{1/2}F_A^*(F_A(C)^{-1})C^{1/2}-I,\qquad
\operatorname{Tr}(E_A^2)=e_r\leq\epsilon.
\]
The equality is similarity invariance of the trace of the square, rather than a claim that \(CS_r\) is Hermitian.

#### Transfer, inverses and the dimension factor

Put \(U:=F_A(C)\), \(V:=F_B(C)\).
The input bounds give
\[
(KR)^{-1}I\leq U\leq KRI,\qquad
\|V-U\|\leq K R\delta.
\]
Define \(\theta:=K^2R^2\delta\).
If \(\theta\leq1/2\), then \(V\geq(2KR)^{-1}I\), so both inverses exist and
\[
\|U^{-1}\|\leq KR,\quad
\|V^{-1}\|\leq2KR,\quad
\|U^{-1}-V^{-1}\|\leq2K^3R^3\delta.
\]
This is precisely the smallness condition missing from the source's invocation of (28); a bound on \(\delta\) independent of \(\epsilon\) is insufficient at that intermediate step.
For
\[
E_B:=C^{1/2}F_B^*(F_B(C)^{-1})C^{1/2}-I
\]
the difference estimate is
\[
\begin{aligned}
\|E_A-E_B\|
&\leq R\bigl(K\delta\|U^{-1}\|
             +K\|U^{-1}-V^{-1}\|\bigr)\\
&\leq K^2R^2\delta+2K^4R^4\delta
\leq3K^4R^4\delta=:a.
\end{aligned}
\]
Both residuals are Hermitian.
If \(a\leq1\), then \(\|E_A\|\leq\sqrt\epsilon\leq1\), \(\|E_B\|\leq1+a\), and
\[
\epsilon_B:=\operatorname{Tr}(E_B^2)
\leq\epsilon+n(2+a)a
\leq\epsilon+9nK^4R^4\delta.
\]
This supplies the full tolerance dependence without applying an unjustified norm estimate to a nonnormal residual.

For comparison, the literal printed (33) is
\[
\operatorname{Tr}((D_1-I)^2)-\operatorname{Tr}((D_2-I)^2)
\leq(\|D_1\|+\|D_2\|+2n)\|D_1-D_2\|.
\]
It fails even for \(n=2\), \(D_1=11I\), \(D_2=10I\): its two sides are \(38\) and \(25\).
For arbitrary \(D_1,D_2\) the valid replacement is
\[
\left|\operatorname{Tr}((D_1-I)^2)-\operatorname{Tr}((D_2-I)^2)\right|
\leq n(\|D_1\|+\|D_2\|+2)\|D_1-D_2\|.
\]
This follows by trace cyclicity and \(|\operatorname{Tr}(XY)|\leq n\|X\|\|Y\|\).
The Hermitian-residual estimate above includes this necessary factor.

#### Determinants and a complete parameter choice

If \(\theta\leq1/2\), the eigenvalues of \(U^{-1/2}VU^{-1/2}\) lie in \([1-\theta,1+\theta]\).
Hence, with \(r_A:=\det F_A(C)/\det C\) and \(r_B:=\det F_B(C)/\det C\),
\[
(1+\theta)^{-n}\leq r_A/r_B\leq(1-\theta)^{-n}.
\]
This comparison uses positive Hermitian matrices and retains the reciprocal.
The corrected Lemma 3.9 in [U003](Yin_U003.md#ggow20-u003) applies when \(\epsilon,\epsilon_B\leq1/(n+1)\).
It proves \(\operatorname{cap}(F_B)>0\) and, by capacity duality in the odd case, gives
\[
\frac{(1-\sqrt{n\epsilon})^n}{(1+\theta)^n}
\leq\frac{\operatorname{cap}(T_A)}{\operatorname{cap}(T_B)}
\leq\frac1{(1-\sqrt{n\epsilon_B})^n(1-\theta)^n}.
\]

Define
\[
q:=100h^2,\qquad P:=512qn^3,\qquad
s:=\log(1/\delta),\qquad \epsilon:=2q/s,
\]
and assume \(s\geq P\).
Then \(\epsilon\leq1/(256n^3)\), and
\[
\max\{\theta,a,9nK^4R^4\delta\}
\leq e^{q/\epsilon}\delta=e^{-s/2}=:\zeta
\leq\epsilon.
\]
Indeed \(4h+64h^2+\log(9n)\leq q\), while \(s e^{-s/2}\leq2/e\leq2q\).
Thus the inverse smallness conditions hold, and \(\epsilon_B\leq2\epsilon\leq1/(n+1)\), as required.
Write \(\rho:=\operatorname{cap}(T_A)/\operatorname{cap}(T_B)\).
Taking logarithms in the preceding two-sided ratio bound and using \(-\log(1-x)\leq2x\) for \(0\leq x\leq1/2\) gives
\[
|\log\rho|\leq6n^{3/2}\sqrt\epsilon\leq3/8.
\]
The lower-ratio side uses \(-\log(1-\sqrt{n\epsilon})+\log(1+\theta)\leq2\sqrt{n\epsilon}+\theta\); the upper side uses \(2\sqrt{2n\epsilon}+2\theta\), and \(\theta\leq\epsilon\).
Consequently
\[
|\rho-1|
\leq2|\log\rho|
\leq\frac{12\sqrt{2q}\,n^{3/2}}{\sqrt s}
\leq\frac{24qn^2}{\sqrt s}
\leq\frac{P}{s^{1/3}}.
\]
This proves the stated Theorem 4.5 modulus with the enlarged polynomial \(P(n,b,\log m)\), including positivity of the perturbed capacity, at the explicit rational bit-input scope above.
The intermediate square-root logarithmic bound serves the reconstruction; no improvement of the paper's advertised interface or its optimal constants is claimed.
The proof uses the existing integral-capacity, scaling-progress, duality and small-error near-minimizer inputs at their recorded inspection depths.
It certifies neither the literal erroneous displayed formulas nor the printed Algorithms 3-4 budgets.
The [isolated mathematical recheck](../../reviews/Yin_R_F0184_v1.md#continuity-reconstruction-finding) found no gap in this complete corrected reconstruction and its affected interfaces for all \(n\geq1\), at the explicit rational real/imaginary bit-input model, positive-capacity hypothesis and enlarged constants above.
That finding retains the external foundational inputs at their recorded inspection depths and excludes the literal source algorithm budgets and the separate rounded polynomial-bit procedure.

### Verification and downstream use

All supplied Section 4 and 5 proof text was read, including the first-step conventions, inverse sensitivity, trace-square calculation, determinant accumulation and error conversion.
PDF pages 39, 51, 54-57 were rendered and visually inspected in the original audit; the complete page contexts made the printed constants and operator orientations unambiguous.
The quantitative repair re-read printed pp. 269-279 and visually checked PDF pages 48, 51, 55 and 57, including (21), (33)-(35), the precision formula and the final reciprocal inference.
Direct arithmetic and the \(E_{11},E_{21}\) example provide analytic checks, not evidence from a tested implementation.
No further external search was performed for this unit; it uses the downloaded primary published version and the separate source-interface review.

Use the checked conservative polynomial-bit interface when an algorithmic existence input suffices.
A concrete implementation should specify its exact arithmetic, symmetric rounding, precision, stopping indices and internal relative-error allocation.
Use of the corrected continuity reconstruction retains its explicit rational input model, enlarged polynomial and the [isolated finding's precise scope and limits](../../reviews/Yin_R_F0184_v1.md#continuity-reconstruction-finding).
The source's literal algorithm constants remain uncertified; the existing conservative polynomial-bit interface has not been expanded.

---
author: Yin
---

# Independent review: radius atoms in the normal core estimate

Date/reviewer: 2026-09-11, the reviewing agent.

Target: [radial-atoms-core continuation](../../claims/Yin_C_F0047_v1.md).


**Outcome: pass.**
The full candidate was read and independently recomputed.
No correction was requested.
The old nonatomic artifact was not modified.
This audit assigns no Claim ID or Role.

Reviewer participation: before the draft froze, the reviewer sent the author the same-radius calculation and quantile observations.
Root also separately checked the complete frozen proof.
This record discloses that prior contribution while reporting the full verification below.

## 1. Exact scope and reused inputs

The conclusion permits every probability radius distribution on (0,R], including countably many atoms and singular continuous parts.
Under rotational invariance, the exact vacuum-adjoint condition is equivalent to the midpoint function A being in L2.
It implies the announced infinity-to-2 bound and both original bounded-coordinate domains.
The freeness-dependent all-M conclusion uses [Yin_C_F0045](../../claims/Yin_C_F0045_v1.md#yin_c_f0045), not a new correlated-tuple assertion.

The reviewer reused the recently reviewed [nonatomic proof](../../claims/Yin_C_F0046_v1.md) and [its audit](Yin_R_F0077_v1.md#original-f0053-account).
The exact operator and adjoint interfaces remain [Yin_C_F0025](../../claims/Yin_C_F0025_v1.md#yin_c_f0025) and [Yin_C_F0044 Section 5](../../claims/Yin_C_F0044_v1.md#5-original-adjoints-and-actual-coordinate-domains).
Those inputs were rechecked in the preceding independent review.
No theorem from the inaccessible Hardy-inequality endpoint is imported: the particular elementary estimate is proved and checked locally.
No source-priority claim is made.

## 2. Same-circle term and ordered quantile identity

On a single circle, angular integration keeps exactly the zero w power in the divided difference for n>=1.
All w powers are strictly negative for n<0, and n=0 gives zero.
Thus a radius atom a contributes \((a/r)p_n(r)\) precisely for input frequency n>=1.
Both the sign and the n=0 boundary in equation (7) are correct.

The off-radius calculation uses only the bounded polynomial divided difference before angular separation.
It does not assume absolute integrability of the separated singular planar kernels.

For the quantile b, the measure identity \(b_*dt=\nu\) follows from the distribution function.
In particular, pullback with the unchanged angular measure is isometric in L2 and preserves essential sup norms.
Since \(\nu\) has no mass at zero, b(epsilon)>0 whenever epsilon>0.
Radius atoms correspond to countably many disjoint intervals \((F_-,F_+)\).
Outside these intervals, \(t=F_\pm(b(t))\) Lebesgue-almost everywhere; the exceptional endpoint levels are null.

The two plateau cancellations in equation (10) were checked explicitly.
For n<=0, the auxiliary inner integral adds \((t-F_-)\,p_n/r\), leaving \(F_-p_n/r-I_n\) after subtraction.
For n>=1 the auxiliary negative outer term adds \(-(F_+-t)p_n/r\), yielding \(F_+p_n/r+O_n\) after subtraction.
Therefore the auxiliary terms may vary within a plateau while their difference is exactly the pullback of the actual core operator.
No new operator is substituted for the original one.

## 3. Vacuum vector and midpoint variance

Only input frequency 1 contributes to the vacuum:
\[
 \tau(e_0p)=\int \frac{2F_-+a}{r}p_1(r)\,d\nu(r).
\]
Fubini is legitimate before imposing any L2 hypothesis since p_1(r)/r is bounded.
With the inner product linear in its second variable, the representing vector is \(\xi=2e^{i\theta}A(r)\), where \(A=(F_-+a/2)/r\).

Conversely, tests \(r^{|n|}e^{in\theta}Q(r^2)\) identify the weighted angular coefficients as finite complex measures.
Polynomial density in C([0,R]) and r>0 almost everywhere then prove the necessity of A in L2.
The joint probability check \(2\int F_-d\nu+\sum a^2=1\) verifies the factor 2 and the atomic contribution.
A single Haar circle indeed gives \(\xi=e^{i\theta}/r\).

On an atomic interval of length a and midpoint M,
\[
 \int_{J_r}\frac{t^2}{r^2}\,dt
 =\frac{aM^2}{r^2}+\frac{a^3}{12r^2}.
\]
The non-atomic complement contributes exactly the corresponding A norm.
Tonelli yields equation (12), even before finiteness is known.
Since M>=a/2, the variance correction is at most one third of the corresponding atomic A norm squared.
Consequently
\[
 \|A\|_2\le\|U\|_2\le\frac2{\sqrt3}\|A\|_2.
\]
The squared ratio 4/3 is attained for a single Haar circle.

## 4. Hardy bound and final constant

On [epsilon,1], V is absolutely continuous with derivative -1/b(t), since b is uniformly positive there.
The integration-by-parts boundary term is \(-\epsilon V(\epsilon)^2\).
It is nonpositive and may be discarded.
Cauchy--Schwarz followed by monotone convergence gives \(\|V\|_2\le2\|U\|_2\).
No vanishing boundary condition at zero or density of nu is assumed.

The finite coefficient-vector triangle inequality bounds the two frequency groups by U||p||_infinity and V||p||_infinity.
Their output index sets are disjoint.
Parseval gives \(\|T\widetilde p\|_2\le\sqrt5\|U\|_2\|p\|_\infty\).
Applying the triangle inequality in equation (10), then the midpoint comparison, yields the candidate's bound
\[
 \|e_0p\|_2
 \le\frac{2(1+\sqrt5)}{\sqrt3}\|A\|_2\|p\|_\infty
 =\frac{1+\sqrt5}{\sqrt3}\|\xi\|_2\|p\|_\infty.
\]
The argument covers complex polynomials.
No truncation theorem is needed.

## 5. Actual domains and the countable-circle example

Rotational invariance and no atom at the origin imply that mu is nonatomic.
The phase kernel consequently has Hilbert--Schmidt norm one.
The represented polynomial integral is well-defined.
The full-core adjoint formula \(e_0^*p=p\xi-J e_0Jp\) proves closability and the actual-adjoint bound.
Both graph image norms are controlled for uniformly bounded polynomial approximants, so weak closedness of the original graphs yields the two bounded-coordinate domains.
In a larger tuple the full vacuum vector is retained for the actual adjoint.
Yin_C_F0045 supplies the all-M conclusion only under freeness.

For \(s=2^{-\beta}\), \(r_n=2^{-n}\), and \(a_n=(1-s)s^{n-1}\), direct summation gives
\[
 F_-(r_n)=s^n,\qquad A(r_n)=(1+s)(2s)^{n-1},\qquad
 \|A\|_2^2=\frac{(1-s)(1+s)^2}{1-4s^3}.
\]
This is finite precisely for beta>2/3.
For 2/3<beta<1 the disk mass ratio is \((2s)^n\), which diverges.
A bounded Hilbert extension E would imply \(s^n\le2r_n\|E\|\) by compression of \([E,X]=P\), a contradiction.
Thus the example has an actually unbounded dual satisfying the exact compact-core hypotheses and both bounded-function domain inclusions.

The radial-atom extension is therefore accepted as stated.
It does not settle nonradial marginals, correlated tuples, or bounded scalar rational reconstruction.

## Actual review arrangement

Before freezing, this reviewer sent the author the same-radius calculation and quantile observations.
That is substantive target mathematical contribution.
The reported separate root check does not establish another isolated finding or erase this relationship; the complete corrected finding is self-reviewed.
The original 2026-09-11 date, full mathematical findings, source depths and exact boundaries remain unchanged.
This maintenance performs no new mathematical review or context-isolation certification.

## Review relationships

| Review | Relationship |
| --- | --- |
| [Original finding](#5-actual-domains-and-the-countable-circle-example) | self-reviewed |

## Review bindings

| Review | Target | Scope |
| --- | --- | --- |
| [Original finding](#5-actual-domains-and-the-countable-circle-example) | [C_F0047 statement](../../claims/Yin_C_F0047_v1.md#statement) | Whole eight-section arbitrary-radius rotational-law theorem: same-circle term, ordered quantile plateau cancellation, midpoint vacuum criterion and variance, Hardy constants, actual original domains and countable-circle unbounded-dual example. No origin atom, nonradial/correlated theorem or bounded scalar reconstruction. |
| [Original finding](#5-actual-domains-and-the-countable-circle-example) | [C_F0047 argument](../../claims/Yin_C_F0047_v1.md#3-an-ordered-quantile-identity) | Whole eight-section arbitrary-radius rotational-law theorem: same-circle term, ordered quantile plateau cancellation, midpoint vacuum criterion and variance, Hardy constants, actual original domains and countable-circle unbounded-dual example. No origin atom, nonradial/correlated theorem or bounded scalar reconstruction. |

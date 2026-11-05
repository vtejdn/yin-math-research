---
author: Yin
---

# Finite-variance Brown and determinant limits from symmetric Wigner carriers

This necessary statement extension retains the [reviewed conditional-shift result](Yin_C_F0186_v6.md#statement) and its complete proof at v6.
The new class permits a finite symmetric product carrier in place of its single second factor and proves fixed-parameter determinant limits for every outer polynomial.
The derivation is a project deduction developed on 2026-11-05 by the coordinated F0012 and F0013--F0014 research agents for Yin.
The complete extension has [independent review](../audits/reviews/Yin_R_F0196_v1.md#symmetric-carrier-finding), and no earlier review is asserted to cover the new statement.
The [general finite-variance Task](../tasks/Yin_T_F0012_v3.md#contract) remains unresolved.
The [matrix-pencil](../tasks/Yin_T_F0013_v1.md#contract) and [scalar determinant](../tasks/Yin_T_F0014_v1.md#contract) contracts remain distinct, with the latter receiving restricted full-limit conclusions below.

## Exact project inputs and provenance

- [C_F0186_v4](Yin_C_F0186_v4.md#decision-finite-variance-reviewed) supplies Hermitized weak limits, positive logarithmic tails, local planar potential bounds, tightness, the cyclic identities, and the bounded polynomial Brown mapping.
- [C_F0187_v2](Yin_C_F0187_v2.md#decision-complex-intermediate-reviewed) supplies intermediate singular values uniformly over arbitrary independent complex shifts, used only for the real-input subcase.
- [C_F0188_v2](Yin_C_F0188_v2.md#decision-complex-shift-reviewed) supplies the polynomial least-singular-value floor for independent polynomially bounded complex symmetric shifts, including fixed finite-variance diagonal laws.
- [C_F0186_v6](Yin_C_F0186_v6.md#argument) supplies the already proved polynomial norm bound, singular product inequality, and the preceding two-factor proof mechanism.
  The new proof verifies the carrier and all fixed-product interfaces explicitly rather than invoking a changed version of that theorem.
- [FK52-U001](../audits/literature/FK52/Yin_U001.md#bounded-multiplicativity-and-the-finite-tracial-adaptation) supplies ordinary bounded FK multiplicativity, including zero determinant, at its retained classical-proof inspection scope.

The earlier [complex-Hermitian controls and cyclic subclasses](Yin_C_F0186_v4.md#statement) remain valid at their own broader input scope.
The new carrier assertions below use real symmetric inputs and do not replace that complex-input statement.
No new external theorem, novelty claim, or source-proof reinspection is introduced.

<a id="statement"></a>
## Exact carrier class and conclusions

Use independent real Wigner inputs satisfying the exact fixed-law finite-second-moment model of the Task, with arbitrary coupling across dimensions.
For a scalar noncommutative polynomial, let \(\operatorname{rev}\) reverse its words without conjugating coefficients, as in [the accepted convention](../claims/Yin_C_F0186_v6.md#word-reversal).
Fix a polynomial \(Q(x_2,\ldots,x_d)\) with \(\operatorname{rev}Q=Q\).
Fix a nonzero complex scalar \(c\), an integer \(K\ge0\), and polynomials
\[
 T_\nu(x_2,\ldots,x_d)
 =x_{j_\nu}+Q_\nu((x_j)_{j\ne1,j_\nu}),
 \qquad 2\le j_\nu\le d,\qquad
 \operatorname{rev}Q_\nu=Q_\nu,
 \qquad 1\le\nu\le K.
\]
The distinguished indices may repeat, and the factors may be dependent.
Assume that the polynomial product
\[
 H=cT_1\cdots T_K
 \quad\text{satisfies}\quad \operatorname{rev}H=H,
 \qquad
 R=(x_1+Q)H.
 \tag{Carrier}
\]
For \(K=0\), the product means the constant \(c\).
For every fixed \(z\in\mathbb C\),
\[
 \frac1N\log|\det(R(W^{(N)})-zI_N)|
 \longrightarrow\tau\log|R(s)-z|
 \quad\text{almost surely},
 \tag{Log-limit}
\]
with a finite free logarithm.
For every fixed one-variable polynomial \(g\),
\[
 \mu_{g(R(W^{(N)}))}\Longrightarrow
 \mu_{g(R(s))}^{\mathrm{Br}}
 \quad\text{weakly almost surely}.
 \tag{Brown-limit}
\]
The probability-one event for (Log-limit) may depend on \(z\), whereas (Brown-limit) requires one event for all bounded continuous test functions for the fixed model and polynomials.
The conclusion is also valid for \(H(x_1+Q)\), by the exact finite and free cyclic identities already proved in [C_F0186_v4](../claims/Yin_C_F0186_v4.md#cyclic-selfadjoint-reduction).
No cross-size independence or expectation limit of unregularized logarithms is asserted.


<a id="outer-polynomial-statement"></a>
### Fixed-parameter outer-polynomial and ordered-product conclusions

For every fixed one-variable polynomial \(g\) and fixed \(z\in\mathbb C\), the following stronger logarithmic conclusion accompanies (Brown-limit):
\[
 \frac1N\log|\det(g(R(W^{(N)}))-zI_N)|
 \longrightarrow\log\Delta_\tau(g(R(s))-z)
 \quad\text{almost surely}.
 \tag{Outer-log}
\]
If \(g(t)-z\) is not the zero polynomial, the limiting logarithm is finite.
If \(g(t)-z\equiv0\), both sides are \(-\infty\).
The event may depend on the fixed \(g,z\), and no common event over an uncountable parameter family is asserted.

There is also a zero-shift consequence for every fixed finite ordered product
\[
 S=\prod_{h=1}^{q}g_h(R_h),
 \tag{Ordered-product}
\]
where each \(R_h\) belongs to (Carrier), allowing a different relabeling of the same independent real Wigner coordinates for each \(h\).
The factors may share variables, be dependent, and fail to commute.
Then
\[
 \frac1N\log|\det S(W^{(N)})|
 \longrightarrow\log\Delta_\tau(S(s))
 \quad\text{almost surely}.
 \tag{Product-log}
\]
The limit is finite if every \(g_h\) is a nonzero polynomial, and both sides are \(-\infty\) if any \(g_h\equiv0\).
An empty product is the identity and has logarithm zero.
No assertion about \(S-z\) for \(z\ne0\), or about Brown convergence for general (Ordered-product), is included.

<a id="argument"></a>
## Complete candidate argument

### Polynomial floors for the carrier

Fix an arbitrarily large desired failure exponent \(B>2\).
For each \(\nu\), condition on all input matrices other than \(W_{j_\nu}\).
The shift \(Q_\nu(W)\) is independent of that exposed input and complex symmetric.
By [the accepted polynomial norm bound](../claims/Yin_C_F0186_v6.md#argument), it has a polynomial norm bound outside an event of probability \(O(N^{-B})\).
Applying C_F0188_v2 conditionally, with constants uniform on this norm event, gives an exponent \(b_\nu>0\) such that
\[
 \mathbb P\{s_{\min}(T_\nu(W))<N^{-b_\nu}\}
 =O(N^{-B}).
 \tag{Factor-floor}
\]
This is a marginal estimate for each factor; independence between factors is unnecessary.
A finite union and \(s_{\min}(AB)\ge s_{\min}(A)s_{\min}(B)\) yield a fixed \(b_H>0\) with
\[
 \mathbb P\{s_{\min}(H(W))<N^{-b_H}\}=O(N^{-B}).
 \tag{Carrier-floor}
\]
The fixed scalar \(c\) is absorbed by increasing the exponent if necessary.
For \(K=0\), this estimate is deterministic.

Now fix \(z\) and condition on \(W_2,\ldots,W_d\).
On the carrier-floor event and a polynomial norm event for \(Q(W)\), define
\[
 F_N=Q(W)-zH(W)^{-1}.
\]
Both terms are complex symmetric, because \(\operatorname{rev}Q=Q\), \(\operatorname{rev}H=H\), and the inverse of an invertible symmetric matrix is symmetric.
The shift is independent of \(W_1\) and has a fixed polynomial norm bound.
Set it equal to zero off these good events when applying a uniform random-shift statement globally.
C_F0188_v2 then gives a polynomial floor for \(V_N=W_1+F_N\), outside another \(O(N^{-B})\) event.
On the good events the exact factorization is
\[
 R(W)-zI=V_NH(W).
 \tag{Factorization}
\]
Consequently a fixed exponent \(b_z>0\) satisfies
\[
 \mathbb P\{s_{\min}(R(W)-zI)<N^{-b_z}\}=O(N^{-B}).
 \tag{Output-floor}
\]
First Borel--Cantelli applies under every allowed cross-size coupling.
Thus exact singularity is absent eventually almost surely for each fixed \(z\).

### A growing intermediate range survives the finite product

Write increasing singular values as \(a_r(M)=s_{N-r+1}(M)\), and put \(q_N=\lceil N^{3/4}\rceil\).
C_F0187_v2 applied conditionally to each \(T_\nu(W)\) gives, outside a summable failure event,
\[
 a_r(T_\nu(W))\ge c_\nu(r-1)/N,
 \qquad q_N+1\le r\le N.
 \tag{Factor-middle}
\]
The intermediate theorem has no norm condition on its independent shift.
It also applies conditionally to \(V_N\), using the globally defined shift above.
All these estimates can therefore be imposed simultaneously with the preceding good events.
No independence of the \(K+1\) factors is needed for this finite union.

The [already proved singular product inequality](../claims/Yin_C_F0186_v6.md#argument), iterated over \(L\) factors, gives
\[
 a_{r_1+\cdots+r_L-(L-1)}(M_1\cdots M_L)
 \ge\prod_{\nu=1}^La_{r_\nu}(M_\nu),
 \qquad r_1+\cdots+r_L-(L-1)\le N.
 \tag{Product-middle}
\]
Take \(L=K+1\), including \(V_N\) and the \(K\) carrier factors, and distribute \(k+L-1\) into \(L\) positive integers differing by at most one.
For \(k\ge2L(q_N+1)\), every chosen integer is at least \(q_N+1\), and its predecessor is at least \(k/(2L)\).
Equations (Factorization), (Factor-middle), and (Product-middle) then yield
\[
 a_k(R(W)-zI)\ge c_z(k/N)^L,
 \qquad 2L(q_N+1)\le k\le N,
 \tag{Output-middle}
\]
with a positive constant independent of \(N\).
The fixed scalar is included in \(c_z\).
For \(K=0\), use the single-factor estimate directly, so the same conclusion holds with \(L=1\).
The exceptional bottom range is \(O(N^{3/4})\), and the product exponent is the fixed integer \(L\).

### Negative logarithmic uniform integrability and the planar passage

On the eventual good event, the bottom \(2L(q_N+1)\) singular values contribute at most
\[
 \frac{2L(q_N+1)}N b_z\log N\longrightarrow0
\]
to the normalized negative logarithm.
For the remaining indices up to \(\varepsilon N\), (Output-middle) bounds the limsup contribution by
\[
 C_z\varepsilon+L\varepsilon(1-\log\varepsilon),
\]
which tends to zero with \(\varepsilon\).
All indices above \(\varepsilon N\) are eventually bounded below by \(c_z\varepsilon^L\).
Together these observations prove almost-sure negative logarithmic uniform integrability at each fixed \(z\), with no quantitative weak-convergence rate.

The Hermitized weak convergence and positive logarithmic control of C_F0186_v4 now imply (Log-limit).
They apply to the original fixed polynomial \(R-z\), rather than to a conditional object with \(N\)-dependent coefficients.
The negative-tail estimate also proves that the limiting logarithm is finite.
Fubini on countably many planar disks gives one event of planar almost-everywhere potential convergence.
The same fixed polynomial's pathwise local planar \(L^2\) bounds in C_F0186_v4 give local \(L^1\) convergence.
Its distributional Laplacian, together with the accepted tightness, proves the weak Brown limit for \(R\).
The finite-dimensional spectral mapping and bounded FK polynomial mapping proved in C_F0186_v4 then give (Brown-limit) for each fixed \(g\).
These are the same final interfaces used in C_F0186_v6, with the intermediate exponent two replaced by the fixed integer \(K+1\).

<a id="examples"></a>
### Explicit additions to the accepted subclasses

If \(T=x_2+Q_2(x_3,\ldots,x_d)\) is a conditional symmetric shift and \(h\in\mathbb C[t]\setminus\{0\}\), then \(H=h(T)\) satisfies (Carrier).
Indeed, write \(h(t)=c\prod_\nu(t-\lambda_\nu)\); every factor is another permitted shift, and every polynomial in the symmetric matrix \(T(W)\) is symmetric.
Thus
\[
 R=(x_1+Q)h(x_2+Q_2)
\]
permits an arbitrary fixed nonlinear carrier polynomial, without asserting the unavailable formula for an arbitrary polynomial in a general nonnormal output at a fixed spectral parameter.

Another example is
\[
 H=x_2x_3x_2,\qquad R=x_1x_2x_3x_2.
\]
The carrier is a noncommuting palindrome, and each of its three factors has the required conditional-shift certificate.
For real symmetric inputs it is symmetric but need not be positive.
Hence the existing \(AC^*C\) cyclic selfadjoint reduction does not supply this example merely from the displayed factorization.
The present argument instead exposes \(W_1-z(W_2W_3W_2)^{-1}\), whose shift is symmetric, and controls all four factors' intermediate singular values.
The derivation makes no assertion that these examples have no other previously known proof.


<a id="outer-polynomial-argument"></a>
### Exact determinant closure under outer polynomials

If \(g(t)-z\equiv0\), then \(g(R(W))-zI=0\) and \(g(R(s))-z=0\), so both ordinary determinants vanish.
For a nonzero constant \(g(t)-z=b\), both logarithms are \(\log|b|\).
Otherwise factor the fixed scalar polynomial, with roots counted with multiplicity, as
\[
 g(t)-z=b\prod_{j=1}^{r}(t-\lambda_j),\qquad b\ne0.
\]
Substitution into the same finite matrix gives
\[
 \frac1N\log|\det(g(R(W))-zI)|
 =\log|b|+\sum_{j=1}^{r}\frac1N\log|\det(R(W)-\lambda_jI)|.
 \tag{Root-factorization}
\]
The identity holds in the extended real sense, with no difference of infinite quantities.
There are only finitely many fixed roots, so the events of (Log-limit) may be intersected.
Every summand then converges to a finite free logarithm.
Ordinary bounded FK multiplicativity gives
\[
 \log\Delta_\tau(g(R(s))-z)
 =\log|b|+\sum_{j=1}^{r}\log\Delta_\tau(R(s)-\lambda_j),
\]
proving (Outer-log), including repeated roots.
No Brown-convergence premise or new singular-value estimate enters this deduction.

For (Ordered-product), apply (Outer-log) at \(z=0\) to each factor and intersect the finitely many events.
A relabeling of independent Wigner coordinates preserves every carrier hypothesis and merely selects a different fixed exposed input.
If no \(g_h\) is zero, each factor's limiting logarithm is finite.
Finite determinant multiplicativity in the displayed order therefore gives a convergent sum of normalized logarithms, and bounded FK multiplicativity identifies the sum as \(\log\Delta_\tau(S(s))\).
This proves (Product-log) without requiring independence or commutation between factors.
A zero factor makes both products zero, and the empty-product branch is immediate.

<a id="remaining-boundary"></a>
## Remaining boundary and comparison with the earlier version

The accepted v6 proof gives the special cases \(K=0\) and a single carrier shift.
Its fixed-parameter statement applies to the displayed base polynomial, while its outer-polynomial statement records Brown convergence.
The new carrier construction enlarges the base class, and (Root-factorization) supplies the stronger fixed-parameter logarithmic conclusion for its polynomial images.
The complete original v6 proof, assessment, and review remain fixed at their actual earlier scope.
The outer-polynomial and ordered-product root-factorization deductions were supplied by the coordinated F0013--F0014 research agent and are part of this candidate argument, not independent review evidence.

The whole carrier must be reversal symmetric; symmetry of its individual factors does not imply that condition.
For instance \(H=x_2x_3\) generally fails it, and the analogous conditioning for \(R=x_1x_2x_3\) produces the shift \(-z(W_2W_3)^{-1}\), which is generally not complex symmetric.
The accepted small-value theorem does not apply to that shift.
This proof therefore does not settle the full nonselfadjoint polynomial or matrix-pencil contracts.
Its product conclusion at zero does cover that three-factor product's zero-shift logarithm, without addressing its other shifts or Brown measure.

## Current assessment

[Selected decision](#decision-symmetric-carrier-reviewed)

## Assessment history

### Decision symmetric-carrier-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T07:21 |
| status | open |
| reason | The complete carrier extension, all fixed-parameter outer-polynomial logarithms, and the zero-shift ordered-product deduction are fixed for mathematical review; earlier reviews cover only their exact retained inputs. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact carrier and closure assertions](#statement) | Carrier class, fixed-parameter logarithms, Brown convergence and polynomial images, and zero-shift ordered products, under the displayed real finite-variance and arbitrary-coupling hypotheses. |
| argument | [Carrier argument](#argument) | Carrier floors, intermediate products, negative logarithmic tails and planar identification, together with the root-factorization section below. |
| dependency | [Finite-variance controls](Yin_C_F0186_v4.md#decision-finite-variance-reviewed) | Hermitized weak convergence, positive tails, pathwise planar control, tightness, cyclic identities and Brown polynomial mapping. |
| dependency | [Intermediate singular values](Yin_C_F0187_v2.md#decision-complex-intermediate-reviewed) | Real-input conditional application with independent complex shifts, uniformly over the shift. |
| dependency | [Complex symmetric small values](Yin_C_F0188_v2.md#decision-complex-shift-reviewed) | Normalized finite-variance real Wigner polynomial floors for independent complex symmetric shifts. |
| dependency | [Accepted preceding mechanism](Yin_C_F0186_v6.md#argument) | Polynomial norm bound, singular product inequality, and the earlier conditional-shift proof's accepted input interfaces. |
| dependency | [Ordinary bounded FK product theorem](../audits/literature/FK52/Yin_U001.md#fk52-u001) | Finite-tracial multiplicativity including zero determinants, applied to scalar root factorizations and finite ordered products. |

### Decision symmetric-carrier-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T07:34 |
| status | proved |
| reason | Independent review checked the complete restricted carrier proof, fixed-parameter polynomial closure and zero-shift ordered products with their exact accepted dependencies. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Carrier and closure assertions](#statement) | Exact real finite-variance symmetric-carrier class, all stated fixed-parameter logarithmic and one-event Brown conclusions, and the included outer-polynomial and ordered-product extensions. |
| argument | [Complete carrier and closure proof](#argument) | Conditional floors, fixed-product intermediate range, logarithmic tails, planar passage and exact root/product factorizations. |
| dependency | [Finite-variance controls](Yin_C_F0186_v4.md#decision-finite-variance-reviewed) | Hermitized weak convergence, positive tails, pathwise planar control, tightness, cyclic identities and Brown polynomial mapping. |
| dependency | [Intermediate singular values](Yin_C_F0187_v2.md#decision-complex-intermediate-reviewed) | Real-input conditional applications with arbitrary independent complex shifts. |
| dependency | [Complex symmetric small values](Yin_C_F0188_v2.md#decision-complex-shift-reviewed) | Polynomial floors for independent polynomially bounded complex symmetric shifts, with the fixed finite-variance diagonals. |
| dependency | [Norm and product inputs](Yin_C_F0186_v6.md#argument) | Polynomial norm-event bound and singular product inequality, retained at their accepted scope. |
| dependency | [Ordinary bounded FK products](../audits/literature/FK52/Yin_U001.md#fk52-u001) | Only bounded finite-tracial multiplicativity, including zero determinants, for the stated root factors and ordered products. |
| review | [Independent carrier finding](../audits/reviews/Yin_R_F0196_v1.md#symmetric-carrier-finding) | Complete exact restricted statement, argument, dependencies and all displayed boundary cases; no broader Task completion. |

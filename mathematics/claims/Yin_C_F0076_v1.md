---
author: Yin
---
# Actual phase second derivatives and coassociativity for normal ACSY derivations

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal probability trace, \(H=L^2(M,\tau)\), and let \(X_1,\ldots,X_d\) be bounded normal generators.
Put
\[
 A=\mathbb C\langle X_1,\ldots,X_d,X_1^*,\ldots,X_d^*\rangle.
\]
Suppose there are complex-linear outer derivations
\[
 \delta_i:A\subset H\longrightarrow H\otimes_2H,\qquad
 \delta_i(X_j)=\delta_{ij}1\otimes1,\qquad
 1\otimes1\in\operatorname{Dom}\delta_i^*.
 \tag{1}
\]
The outer actions are \(a\cdot(u\otimes v)\cdot b=au\otimes vb\).
Write
\[
 \xi_i=\delta_i^*(1\otimes1),\qquad
 \epsilon_i(a)=(\delta_i(a^*))^\dagger,\qquad
 (u\otimes v)^\dagger=v^*\otimes u^*.
\]
For each \(i\), the following assertions hold.

1. The spectral law \(\mu_i\) of \(X_i\) is diffuse, and
\[
 \delta_i(X_j^*)=\delta_{ij}k_i,\qquad
 k_i(z,w)=\frac{\bar z-\bar w}{z-w}\quad(\mu_i^2\text{-almost everywhere}).
 \tag{2}
\]
Both \(\delta_i\) and \(\epsilon_i\) are closable.
Their values on \(A\) belong to the bounded spatial tensor algebra \(M\bar\otimes M\); the actual vacuum of \(\epsilon_i\) is \(\xi_i^*\).

2. On \(A\otimes_{\mathrm{alg}}A\) form the four-component operator
\[
 \mathcal T_i=
 \bigl(\delta_i\otimes\mathrm{id},\ \mathrm{id}\otimes\delta_i,\
       \epsilon_i\otimes\mathrm{id},\ \mathrm{id}\otimes\epsilon_i\bigr).
 \tag{3}
\]
It is closable, and \(k_i,\bar k_i\) belong to \(\operatorname{Dom}\overline{\mathcal T_i}\).
Thus these are domains of the actual joint graph closure of the algebraic core.
If \(\xi_i^{\rm marg}\) is the projection of \(\xi_i\) onto \(L^2(W^*(X_i))\), every one of the four derivatives of either phase has norm at most \(\sqrt6\|\xi_i^{\rm marg}\|_2\).
In particular,
\[
 \overline{\delta_i\otimes\mathrm{id}}\,k_i
 =\overline{\mathrm{id}\otimes\delta_i}\,k_i=C_i,
 \qquad
 C_i(z,w,v)=
 \frac{(\bar z-\bar v)(w-v)-(\bar w-\bar v)(z-v)}
 {(z-v)(w-v)(z-w)}.
 \tag{4}
\]

3. For every \(p\in A\), both \(\delta_i(p)\) and \(\epsilon_i(p)\) belong to \(\operatorname{Dom}\overline{\mathcal T_i}\), and
\[
 \overline{\delta_i\otimes\mathrm{id}}\,\delta_i(p)
 =\overline{\mathrm{id}\otimes\delta_i}\,\delta_i(p),\qquad
 \overline{\epsilon_i\otimes\mathrm{id}}\,\epsilon_i(p)
 =\overline{\mathrm{id}\otimes\epsilon_i}\,\epsilon_i(p).
 \tag{5}
\]
All mixed tensor-leg derivatives on these values are also actual Hilbert-space expressions.
No freeness, geometric support condition, reality assumption on \(\delta_i\), or all-\(M\) domain assumption is imposed.

This statement supplies actual second-derivative domains and coassociativity.
It does not assert an operator-norm-to-\(L^2\) bound for either contraction of \(\delta_i\), or that a canonical dual or its adjoint has domain containing all \(M\Omega\).

## Argument

### 1. Diffuseness, the phase, and closability

By [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001), (1) implies \(\Delta(X)=d\).
The absence-of-finite-rank-cycles characterization in [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002) then implies that every normal marginal is diffuse.
Indeed, if a spectral projection \(e=1_{\{z\}}(X_j)\) were nonzero, the rank-one orthogonal projection onto \(\mathbb C e\Omega\) would commute with right multiplication by \(X_j\): this line reduces that normal operator.
Putting this projection in coordinate \(j\) and zero in all other coordinates gives a nonzero finite-rank cycle.

Apply \(\delta_i\) to \(X_jX_j^*=X_j^*X_j\):
\[
 \bigl(\lambda(X_j)\otimes I-I\otimes\rho(X_j)\bigr)\delta_i(X_j^*)
 =\delta_{ij}(X_j^*\otimes1-1\otimes X_j^*).
 \tag{6}
\]
The operator in parentheses is injective on \(H\otimes_2H\).
Its spectral diagonal is zero, since the coarse representation of the two marginal algebras is normal and the diagonal has zero product trace \(\mu_j^2\).
The bounded phase in (2) solves (6) when \(j=i\), proving (2); when \(j\ne i\) injectivity gives zero.
This reproduces the phase-determination mechanism of [C_F0070](Yin_C_F0070_v1.md#argument) directly from the present premise, without importing that Claim's bare-dual hypothesis.

The actual-vacuum tensor-adjoint formula, with the outer actions in (1), puts \(A\otimes_{\mathrm{alg}}A\) in \(\operatorname{Dom}\delta_i^*\).
This is the inspected Lemma 3.3 interface of ACSY24-U001, and proves closability.
Conjugating the actual adjoint pairing gives the vacuum \(\xi_i^*\) for \(\epsilon_i\), as in [C_F0073 Part A](Yin_C_F0073_v1.md#argument); hence \(\epsilon_i\) is also closable.
Its generator values are
\[
 \epsilon_i(X_j)=\delta_{ij}\bar k_i,\qquad
 \epsilon_i(X_j^*)=\delta_{ij}1\otimes1.
 \tag{7}
\]
Here the phase is symmetric in its two variables.
All generator values in (2) and (7) are bounded spatial tensors.
Finite Leibniz expansions therefore show that every \(\delta_i(p)\) and \(\epsilon_i(p)\), \(p\in A\), is a bounded spatial tensor.

Fix \(i\), and suppress that index below.
On marginal star polynomials, \(\delta\) is exactly
\[
 \delta f(z,w)=\frac{f(z)-f(w)}{z-w},
 \tag{8}
\]
and \(\epsilon f(z,w)\) has denominator \(\bar z-\bar w\).
Restricting the actual vacuum pairing shows that the marginal operator has actual vacuum \(\xi^{\rm marg}\).
Thus the scalar soft-Cauchy inequalities in [C_F0055, Sections 4-5](Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) apply.

### 2. Smooth phase approximants in the joint graph

For \(t>0\), set
\[
 h_t(z,v)=\frac{(\bar z-\bar v)^2}{|z-v|^2+t}.
 \tag{9}
\]
This is smooth in four real variables on all of \(\mathbb R^4\), satisfies \(|h_t|\le1\), and converges to \(k(z,v)\) off the diagonal.
Consequently \(h_t\to k\) in \(L^2(\mu^2)\).

For fixed \(t\), approximate \(h_t\) and all its first real partial derivatives uniformly on a real four-dimensional box containing the product spectrum by complex polynomials in those four real coordinates.
This is the tensor Bernstein \(C^1\) approximation: Theorem 3 and Theorem 4(1) of VV16, in the [accepted author PDF](https://eprints.whiterose.ac.uk/id/eprint/106084/1/tr182a2-copy-for-UoL.pdf), printed pp.6-7, with \(d=4,m=1\).
The arbitrary-\(d\) statement of Theorem 4 was directly checked on 2026-10-15.
The existing [VV16-U001](../audits/literature/VV16/Yin_U001.md#vv16-u001) retains the same source and its earlier two-dimensional application; its recorded application is not silently enlarged here.

For completeness, on the unit cube the tensor Bernstein derivative in coordinate \(r\) is the positive Bernstein average, with degree \(n-1\) in coordinate \(r\), of
\[
 n\bigl[f((j+e_r)/n)-f(j/n)\bigr].
\]
These coefficients equal averages of \(\partial_r f\) over intervals of length \(1/n\).
Uniform continuity of \(\partial_r f\), and uniform concentration of the product binomial averages about the evaluation point, prove uniform derivative convergence.
The same averaging argument for \(f\) proves function convergence.
Rescaling the box and treating real and imaginary parts separately gives the asserted four-dimensional approximation.
Only first partial derivatives are used.

Evaluated at \((X_i,X_i^*)\) in the two legs, these polynomials are finite sums of marginal star-polynomial tensors.
On this algebraic core, their first-leg derivative is the quotient
\[
 q_L h(z,w,v)=\frac{h(z,v)-h(w,v)}{z-w}.
 \tag{10}
\]
Their second-leg derivative is
\[
 q_R h(z,w,v)=\frac{h(z,w)-h(z,v)}{w-v}.
 \tag{11}
\]
Uniform convergence of the two real derivatives in each varying complex coordinate bounds the error in either quotient uniformly, by the real mean-value estimate on the convex box.
For \(\epsilon\), replace the denominator by its conjugate; the same error bound applies.

Each tensor-leg operator is closable, since \(\delta,\epsilon\) are closable and the algebraic tensor domain is a core for their Hilbert tensor products with the identity.
The four-component operator is therefore closable.
The preceding approximants converge in its single joint graph and prove \(h_t\in\operatorname{Dom}\overline{\mathcal T}\), with the four quotient values just given.
The same applies to \(\overline{h_t}\).

### 3. Uniform actual derivative estimates

For pairwise distinct \(z,w,v\), write
\[
 a=z-v,\quad b=w-v,\quad x=|a|^2,\quad y=|b|^2,\quad r=|a-b|^2,
 \quad A_t=x+t,\ B_t=y+t,\ R_t=r+t,
 \quad H_0=|\bar a b-\bar b a|^2.
\]
The positive function of C_F0055 (10) is
\[
 Q_t=
 \frac{H_0+(t/2)(x+y+r)+(tH_0/2)(1/x+1/y+1/r)+3t^2}
 {A_tB_tR_t}.
 \tag{12}
\]
Its actual scalar-vacuum calculation, C_F0055 (13)-(14), gives
\[
 \int Q_t\,d\mu^3\le3\|\xi^{\rm marg}\|_2^2 .
 \tag{13}
\]
Indeed one third of this integral is the real vacuum pairing against the conjugate soft Cauchy transform, whose \(L^2\) norm is at most \(\|\xi^{\rm marg}\|_2\).
The diagonals are null.

The numerator of (10) for \(h_t\) obeys the exact identity
\[
 \bar a^2B_t-\bar b^2A_t
 =\bar a\bar b(\bar a b-\bar b a)
    +t(\bar a-\bar b)(\bar a+\bar b).
\]
It follows that
\[
 |q_Lh_t|^2
 \le\frac{2xyH_0}{A_t^2B_t^2r}
       +\frac{4t^2(x+y)}{A_t^2B_t^2}.
 \tag{14}
\]
Decompose \(Q_t=Q_t^H+Q_t^0\) into its \(H_0\)-dependent and remaining nonnegative terms.
Since
\[
 Q_t^H\ge\frac{H_0(1+t/(2r))}{A_tB_tR_t}
          \ge\frac{H_0}{2A_tB_tr},
\]
the first term of (14) is at most \(4Q_t^H\).
Put \(L=x+y\).
The ratio of the second term to \(Q_t^0=t(L+r+6t)/(2A_tB_tR_t)\) is
\[
 \frac{8tLR_t}{A_tB_t(L+r+6t)}
 \le\frac{8LR_t}{(L+t)(L+r+6t)}
 \le8,
\]
using \(A_tB_t\ge t(L+t)\), \(L/(L+t)\le1\), and \(R_t\le L+r+6t\).
Hence
\[
 |q_Lh_t|^2\le8Q_t,\qquad
 \|q_Lh_t\|_2^2\le24\|\xi^{\rm marg}\|_2^2.
 \tag{15}
\]
The same bound holds for (11), by symmetry of \(h_t\) and permutation of the three variables; for conjugate denominators, by equality of moduli; and for the conjugate approximant, by complex conjugation.

### 4. Passing to the actual joint closed graph

Choose \(t_n\downarrow0\).
The first graph coordinates \(h_{t_n}\) converge strongly to \(k\), and the four derivative coordinates are bounded in \(L^2(\mu^3)\).
A weakly convergent subsequence of the five-component graph tuples therefore exists.
The graph of \(\overline{\mathcal T}\) is a norm-closed linear subspace, hence weakly closed.
Its limiting tuple has first coordinate \(k\), proving \(k\in\operatorname{Dom}\overline{\mathcal T}\).
The same proof gives \(\bar k\).

The pointwise limits of all quotient coordinates off the collision diagonals are their ordinary divided-difference expressions.
A uniformly \(L^2\)-bounded sequence on a finite measure space which converges almost everywhere converges weakly to that limit: uniform integrability gives convergence against bounded test functions, followed by \(L^2\) density.
This identifies the actual graph derivatives.
The two \(\delta\) derivatives of \(k\) coincide with the symmetric second divided difference of \(z\mapsto\bar z\), namely (4).

Furthermore,
\[
 |C(z,w,v)|^2
 =\frac{H_0}{xyr}
 =\frac{16\,\operatorname{Area}(z,w,v)^2}
 {|z-v|^2|w-v|^2|z-w|^2}.
\]
C_F0055 Section 5 gives
\[
 \|C\|_2^2\le6\|\xi^{\rm marg}\|_2^2.
 \tag{16}
\]
Each of the other six phase derivatives differs in modulus only by conjugation or a unimodular quotient, so the same bound holds.
This establishes every quantitative and domain assertion in Part 2 without identifying a maximal distributional domain with a minimal graph closure.

### 5. Bounded coefficient product rules and full-core coassociativity

Identify \(H^{\otimes r}\) with \(L^2(M^{\bar\otimes r},\tau^{\otimes r})\).
All multiplication below is ordinary spatial tensor multiplication.
Insertions \(\eta\mapsto\eta_{12},\eta_{13},\eta_{23}\) from \(H^{\otimes2}\) into \(H^{\otimes3}\) are isometries, using the vacuum in the omitted leg.

Let \(\gamma=\delta\) or \(\epsilon\), and fix \(b\in A\).
On the algebraic tensor core, the extra terms in the Leibniz rules for \(\gamma\otimes\mathrm{id}\) are
\[
 \begin{array}{ll}
 \text{left multiplication by \(b\) on input leg 1:}
     &(\gamma b)_{12}\eta_{23},\\
 \text{right multiplication by \(b\) on input leg 1:}
     &\eta_{13}(\gamma b)_{12}.
 \end{array}
 \tag{17}
\]
Multiplication on input leg 2 simply passes to output leg 3.
For \(\mathrm{id}\otimes\gamma\), the extra terms are
\[
 \begin{array}{ll}
 \text{left multiplication by \(b\) on input leg 2:}
     &(\gamma b)_{23}\eta_{13},\\
 \text{right multiplication by \(b\) on input leg 2:}
     &\eta_{12}(\gamma b)_{23}.
 \end{array}
 \tag{18}
\]
Multiplication on input leg 1 passes to output leg 1.
For example, the first formula in (17) is the cross term in
\[
 \overline{\gamma\otimes\mathrm{id}}\bigl((b\otimes1)\eta\bigr)
 =(b\otimes1\otimes1)\overline{\gamma\otimes\mathrm{id}}\eta
       +(\gamma b)_{12}\eta_{23}.
 \tag{19}
\]
Every displayed cross term is a bounded map \(H^{\otimes2}\to H^{\otimes3}\), with norm at most \(\|\gamma b\|_{M\bar\otimes M}\).
This follows from the bounded spatial-tensor conclusion of Part 1 and bounded left or right multiplication on tracial \(L^2\).
The corresponding input multipliers preserve the algebraic core.
Approximate in its joint graph, apply these bounded error maps, and use closedness: all four product rules extend to \(\operatorname{Dom}\overline{\mathcal T}\).
Thus no general unbounded-product rule is assumed.

Every \(\delta(p)\) is a finite sum of outer core coefficients multiplying \(1\otimes1\) or \(k\); every \(\epsilon(p)\) is such a sum with \(\bar k\).
Part 2 and (17)-(19) prove that these values belong to the joint actual domain.

Finally set
\[
 B_\delta(p)
 =\overline{\delta\otimes\mathrm{id}}\,\delta(p)
  -\overline{\mathrm{id}\otimes\delta}\,\delta(p).
\]
For \(p,q\in A\), the cross term in applying either tensor-leg operator to \(\delta(pq)=p\cdot\delta(q)+\delta(p)\cdot q\) is exactly \((\delta p)_{12}(\delta q)_{23}\).
It cancels in the difference; all products are bounded spatial tensors or the justified graph limits above.
Therefore
\[
 B_\delta(pq)=p\cdot B_\delta(q)+B_\delta(p)\cdot q.
\]
It vanishes on every \(X_j\).
It vanishes on \(X_i^*\) by (4), and on the other \(X_j^*\) because their first derivatives are zero.
It vanishes on all of \(A\).
The same argument for \(\epsilon\), using the symmetric second divided difference of \(s\mapsto\bar s\) in the variables \(s=\bar z\), proves the second equality in (5).
This also verifies actual domains for all the mixed compositions.

## Scope and provenance

The proof develops the phase approximation and closed-graph argument from the soft three-point estimate already fixed in C_F0055.
It does not assume that pointwise square-integrable divided differences automatically belong to the closure of a chosen core.
The proof specifically constructs a uniformly graph-bounded smooth family and then uses the weakly closed joint graph.

A subsequent reuse comparison located the earlier actual phase-domain and coassociativity mechanism in [C_F0056](Yin_C_F0056_v1.md#statement), with the common mixed-domain application already retained in [L_F0011](../ledger/Yin_L_F0011_v1.md#1-all-four-mixed-iterates-have-original-domains).
The present argument is an alternative proof stated directly under the full ACSY premise; its regularized intermediate bound is 24 rather than the earlier 132.
This attribution does not change the fixed argument, its selected dependencies or the scope of its independent review, and does not claim that the earlier materials were used in developing that argument.

The four-dimensional Bernstein use is verified above at its exact primary-source statement and applicability, with an elementary approximation argument included.
No source-proof audit or prescribed convergence rate is asserted.
The current statement requires the entire normal-tuple ACSY condition (1); it is not a theorem for arbitrary Hilbert-valued derivations with an unspecified marginal phase.

The actual mixed compositions permit further study of the defects of the real derivations \(\delta+\epsilon\) and \(\mathrm i(\delta-\epsilon)\).
Their mixed energy estimates on general correlated words remain separate obligations.
Coassociativity of \(\delta\) and \(\epsilon\) does not supply reality of either derivation, nor does it alone import a free-difference-quotient contraction estimate.

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-14T16:44 |
| status | open |
| reason | Complete phase graph approximation, regularized bound and bounded-coefficient coassociativity proof retained for separate independent review; no contraction or full-domain conclusion is selected. |

Recorded authoring stage: proof draft.
Recorded review label: self-reviewed.

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Parts 1-3, actual joint phase domains, derivative estimates and coassociativity on the full starred core. |
| argument | [Argument](#argument) | Complete diffuse-phase, smooth approximation, positive-kernel, weak graph and bounded product-rule proof. |
| dependency | [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 maximal Delta and the inspected actual tensor-adjoint closability interface. |
| dependency | [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002) | Maximal Delta excludes nonzero finite-rank cycles, used to prove diffuse marginals. |
| dependency | [C_F0055 Sections 4-5](Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | The actual scalar-vacuum soft-Cauchy estimate, positive Q_t identity and limiting curvature bound; its scalar hypotheses are verified in Section 1. |
| dependency | [C_F0073 Part A](Yin_C_F0073_v1.md#argument) | Conjugation of an actual Hilbert adjoint vacuum gives the vacuum xi_i star for epsilon_i. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T16:54 |
| status | proved |
| reason | Independent full review verified the common actual graph closure, all phase derivative estimates, spatial coefficient product rules and coassociativity, with the stated source interfaces. No contraction or all-M-domain assertion is adopted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Parts 1-3, actual joint phase domains, derivative estimates and coassociativity on the full starred core. |
| argument | [Argument](#argument) | Complete diffuse-phase, smooth approximation, positive-kernel, weak graph and bounded product-rule proof. |
| dependency | [ACSY24-U001](../audits/literature/ACSY24/Yin_U001.md#acsy24-u001) | Proposition 3.5 maximal Delta and the inspected actual tensor-adjoint closability interface. |
| dependency | [MSY23-U002](../audits/literature/MSY23/Yin_U002.md#msy23-u002) | Maximal Delta excludes nonzero finite-rank cycles, used to prove diffuse marginals. |
| dependency | [C_F0055 Sections 4-5](Yin_C_F0055_v1.md#5-vacuum-control-of-all-soft-cauchy-transforms) | The actual scalar-vacuum soft-Cauchy estimate, positive Q_t identity and limiting curvature bound, with all scalar hypotheses checked. |
| dependency | [C_F0073 Part A](Yin_C_F0073_v1.md#argument) | Conjugation of an actual Hilbert adjoint vacuum gives the vacuum xi_i star for epsilon_i. |
| review | [Independent complete review](../audits/reviews/Yin_R_F0049_v1.md#conclusion) | Entire fixed statement and proof, all dependencies, direct four-dimensional Bernstein applicability and actual tensor-adjoint source check; no full-domain or contraction conclusion. |


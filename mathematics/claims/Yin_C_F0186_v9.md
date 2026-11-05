---
author: Yin
---

# Brown limits and determinant parity for polynomials in independent GOE matrices

This version extends the real Gaussian candidate within [the finite-variance F0012 question](../tasks/Yin_T_F0012_v3.md#contract), with precise GOE determinant consequences for the affine and scalar contracts of F0013 and F0014.
The [reviewed real finite-variance carrier theorem](Yin_C_F0186_v7.md#decision-symmetric-carrier-reviewed) and all earlier fixed versions retain their statements, arguments and assessments at their exact scopes.
The [v8 GOE candidate and its open assessment](Yin_C_F0186_v8.md#decision-goe-candidate) are preserved.
The present statement includes its one-event scalar Brown conclusion and adds the arbitrary-constant affine good-dimension, even-dimensional, upper-limit and parity assertions.
The actual [v8 proof body](Yin_C_F0186_v8.md#argument) is retained as a proof module, together with the complete extension below, and both are covered by the [independent complete GOE finding](../audits/reviews/Yin_R_F0190_v8.md#independent-goe-parity-proof).
Its open assessment is not an established mathematical premise, and earlier reviews are not asserted to cover this assembled GOE argument.
The full arbitrary-law finite-second-moment questions remain outside this GOE statement.

<a id="statement"></a>
## Exact GOE Brown, affine and scalar determinant statement

Fix \(d\ge1\).
For each \(N\), let \(X_1^{(N)},\ldots,X_d^{(N)}\) be independent real symmetric normalized GOE matrices, with the [Sch05 variance convention](../audits/literature/Sch05/Yin_U001.md#gaussian-and-free-normalizations).
Within each matrix, the strict upper entries are independent \(N(0,1/N)\), the diagonal entries are independent \(N(0,2/N)\), and those families are independent.
All dimensions live on a common probability space with arbitrary cross-size coupling.
Let \(s_1,\ldots,s_d\) be free centered variance-one semicircular elements in a finite von Neumann algebra with faithful normal tracial state \(\tau\).

For every fixed scalar polynomial \(P\in\mathbb C\langle x_1,\ldots,x_d\rangle\), there is an event of probability one on which
\[
 \mu_N=\frac1N\sum_{k=1}^N\delta_{\lambda_k(P(X^{(N)}))}
 \Longrightarrow\mu_{P(s)}^{\mathrm{Br}}
 \tag{GOE-Brown}
\]
against every bounded continuous real function on \(\mathbb C\).
Eigenvalues are counted with algebraic multiplicity.
The polynomial need not be selfadjoint.
The event may depend on the fixed polynomial and coupling.

Fix arbitrary \(m\ge1\) and \(A_0,\ldots,A_d\in M_m(\mathbb C)\), without a condition on \(A_0\), use \(\tau_m=\operatorname{tr}_m\otimes\tau\), and set
\[
 L_N=A_0\otimes I_N+\sum_jA_j\otimes X_j^{(N)},\qquad
 L=A_0\otimes1+\sum_jA_j\otimes s_j,\qquad
 U_N=\frac1{mN}\log|\det L_N|,\qquad
 u=\log\Delta_{\tau_m}(L)\in[-\infty,\infty).
\]
<a id="real-symmetric-nonidentity-dimensions"></a>
**Definition (real-symmetric nonidentity dimensions).**
Define the deterministic set
\[
 \mathcal G(L)=
 \left\{N\ge1:\ \exists H_1,\ldots,H_d\in\operatorname{Sym}_N(\mathbb R),
 \quad\det\!\left(A_0\otimes I_N+\sum_jA_j\otimes H_j\right)\ne0\right\}.
 \tag{Good-dimensions}
\]

The affine assertions are:

1. If \(u=-\infty\), then \(U_N\to-\infty\) almost surely through all dimensions.
2. If \(u\in\mathbb R\), then \(\mathcal G(L)\) contains every sufficiently large even dimension, and \(U_N\to u\) almost surely as \(N\to\infty\) within \(\mathcal G(L)\).
   For every \(N\notin\mathcal G(L)\), \(U_N=-\infty\) for every real-symmetric evaluation.
3. Consequently, for all coefficient tuples, \(\limsup_NU_N=u\) almost surely, and \(U_{2n}\to u\) almost surely.
4. For finite \(u\), full-sequence convergence \(U_N\to u\) holds if and only if there exists one odd dimension in \(\mathcal G(L)\).
   If no such odd dimension exists, every odd-size evaluation is singular, \(\liminf_NU_N=-\infty\), and the even subsequence still converges to \(u\).

For every fixed scalar polynomial \(P\) and fixed \(z\in\mathbb C\), the resulting scalar consequence is
\[
 \limsup_N\frac1N\log|\det(P(X^{(N)})-zI_N)|
 =\log\Delta_\tau(P(s)-z)
 \quad\text{almost surely},
 \tag{GOE-scalar-limsup-all-z}
\]
and the same normalized logarithms converge to this value along all even dimensions.
This includes \(z=P(0)\).
For nonconstant \(P\) the target is finite, and the same odd-witness criterion classifies its full-sequence logarithmic convergence.
Here a scalar odd witness means a real-symmetric tuple in one odd dimension at which \(P-z\) is invertible.
Constant polynomials have the immediate scalar determinant identity, including the zero case.

The one-event Brown-measure assertion above retains its actual v8 proof module; no full-sequence fixed-parameter claim is inferred from an upper limit alone.
These are GOE submodel assertions for F0013 and F0014, rather than the arbitrary finite-variance assertions in their full contracts.

In particular, when \(A_0\) is invertible, the zero input is a witness in dimension one, so the finite-free-log affine assertion is full-sequence convergence.
For a nonconstant scalar \(P\) and \(z\ne P(0)\), the same zero-input witness gives the full-sequence fixed logarithmic limit of v8.
Every determinant in this statement is ordinary, with \(\log0=-\infty\).

## Exact inputs and retained proof modules

- [Sch05-U001](../audits/literature/Sch05/Yin_U001.md#sch05-u001) supplies Schultz, arXiv:math/0308192v1, Theorem 3.2, equation (3.6), PDF p. 15, at its accepted fixed-coefficient affine resolvent scope.
  Its [GOE normalization](../audits/literature/Sch05/Yin_U001.md#gaussian-and-free-normalizations) and [Hermitization specialization](../audits/literature/Sch05/Yin_U001.md#goe-hermitization-specialization) match the stated model.
  The underlying Haagerup--Thorbjornsen and complete Schultz master-equation proofs were not newly audited in full.
- [C_F0186_v1#error-bound](Yin_C_F0186_v1.md#error-bound) supplies the accepted real polynomial-map error bound, and [C_F0186_v1#tubes](Yin_C_F0186_v1.md#tubes) supplies the Gaussian algebraic tube estimate and its singular-level extension.
  The actual arbitrary-constant real compression and lift are established below.
- [C_F0186_v1#polynomial-application](Yin_C_F0186_v1.md#polynomial-application) supplies the exact word-chain construction and the recorded SS15 scalar interface.
  The new use at \(z=P(0)\) checks the finite determinant and free block identity explicitly below.
- [C_F0186_v2#generic-rank](Yin_C_F0186_v2.md#generic-rank) supplies nonidentity on Hermitian tuples in every sufficiently large dimension when the free zero atom vanishes.
  The simultaneous conjugate witness and realification are proved below.
- [C_F0186_v2#affine-tube](Yin_C_F0186_v2.md#affine-tube) makes explicit that the tube application requires only a nonzero determinant polynomial, without a nonzero value at the origin.
- [C_F0186_v2#logarithmic-tail](Yin_C_F0186_v2.md#logarithmic-tail) supplies the accepted SS15 matrix-valued algebraicity and local convergent Puiseux interface.
  Matrix-valued atomlessness is not assumed.
- [C_F0186_v3#singular-value-perturbation](Yin_C_F0186_v3.md#singular-value-perturbation) and [C_F0186_v3#global-lipschitz](Yin_C_F0186_v3.md#global-lipschitz) supply the singular-value Frobenius inequality and accepted Gaussian Lipschitz concentration input.
  The retained GOE proof derives its own coordinate scaling.
- [C_F0186_v3#linearization-transfer](Yin_C_F0186_v3.md#linearization-transfer) supplies the accepted bounded FK block-factorization interface.
- [C_F0186_v4#decision-finite-variance-reviewed](Yin_C_F0186_v4.md#decision-finite-variance-reviewed) supplies fixed-polynomial Hermitized weak convergence, local planar potential controls and tightness for the actual fixed-law GOE model.
- [C_F0186_v8#argument](Yin_C_F0186_v8.md#argument) is retained as the actual complete candidate GOE proof body, at its original constant-invertible affine scope and full scalar Brown scope.
  It is a proof module requiring review together with the present extension, not an invocation of its open assessment as an accepted theorem.

The retained SS15 inputs use arXiv:1305.1920v1, Theorem 1.1(5)(6) on PDF pp. 1--2 and Corollary 1.2 on PDF p. 3, at the exact source/application scopes recorded in those fixed inputs.
The source comparisons are used only for affine Hermitizations.
No general-polynomial GOE--GUE interpolation estimate is required.
This is a project deduction without a novelty or priority claim.

<a id="argument"></a>
## Complete candidate argument with the retained GOE proof body

The actual [v8 argument](Yin_C_F0186_v8.md#argument) is part of this argument at its displayed scope.
In particular, its [scalar and one-event planar passage](Yin_C_F0186_v8.md#goe-scalar-brown) proves the Brown assertion stated above using its constant-invertible word-chain pencils away from one planar-null parameter.
That proof does not need the extension below to obtain the one-event Brown conclusion.
For the stronger affine and all-parameter scalar statements, the following argument proves the new witness and real-compression inputs and checks every reused analytic module without an invertibility condition on \(A_0\).
The entire GOE comparison, Puiseux count, concentration, real floor, logarithmic removal, word-chain transfer and planar passage are candidate reasoning to be reviewed jointly at these exact physical versions.
No review or proved assessment is inherited from the open v8 decision.

<a id="all-even-witness"></a>
### Every sufficiently large even dimension has a real-symmetric witness

Assume \(u\in\mathbb R\).
The [accepted generic-rank argument](Yin_C_F0186_v2.md#generic-rank) gives an \(n_0\) such that for every \(n\ge n_0\),
\[
 f_n(H)=\det\!\left(A_0\otimes I_n+\sum_jA_j\otimes H_j\right)
\]
is a nonzero polynomial in real coordinates on the Hermitian tuple space.
This is its eventual-all-dimensions conclusion, not merely existence of one witness.
Entrywise conjugation \(H\mapsto\overline H\) is a real linear bijection of that space, so \(f_n(\overline H)\) is another nonzero complex polynomial in the same real coordinates.
Their product is nonzero.
A complex polynomial vanishing at every real coordinate tuple is the zero polynomial by the repeated one-variable identity principle.
Thus some Hermitian tuple satisfies simultaneously
\[
 f_n(H)\ne0,\qquad f_n(\overline H)\ne0.
\]
The matrices \(A_j\) are unchanged in the second expression.

Write \(H_j=B_j+iC_j\), where \(B_j\) is real symmetric and \(C_j\) real skew-symmetric, and define
\[
 \mathcal R(H_j)=\begin{pmatrix}B_j&-C_j\\C_j&B_j\end{pmatrix}.
\]
This matrix is real symmetric.
The fixed unitary with columns proportional to \(\binom{I}{-iI}\) and \(\binom{I}{iI}\) simultaneously transforms \(\mathcal R(H_j)\) to \(H_j\oplus\overline H_j\), up to the order of these blocks.
It acts only on the physical input factor, leaving every complex coefficient \(A_j\) unchanged.
After regrouping tensor and direct-sum factors,
\[
 L(\mathcal R(H))\simeq L(H)\oplus L(\overline H).
\]
Both summands are invertible, so \(2n\in\mathcal G(L)\).
Since this holds for each \(n\ge n_0\), every sufficiently large even dimension belongs to \(\mathcal G(L)\).

This is a self-contained realification deduction from the exact fixed generic-rank input.
It supplies no quantitative lower determinant bound by itself.

<a id="arbitrary-constant-real-compression"></a>
### The real compression and tube floor on all nonidentity dimensions

For the general constant coefficient, the inside residual in the real compression is
\[
 (A_0\otimes I_k)w+\sum_j(A_j\otimes C_j)w,
\]
and the outside residual is
\[
 \sum_j(A_j\otimes B_j)w.
\]
Here \(k\le2m\), \(\ell\le dk\), \(C_j\) are real symmetric \(k\)-by-\(k\) blocks, \(B_j\) are real \(\ell\)-by-\(k\) blocks, and \(w\) is complex with \(\|w\|=1\), exactly as in the full [v8 real-compression calculation](Yin_C_F0186_v8.md#goe-real-floor).
Taking real and imaginary parts and adding \(\|w\|^2-1\) again gives a real polynomial map of degree at most two in at most
\[
 d\,k(k+1)/2+d\ell k+2mk
\]
coordinates.
The coefficients are fixed and have no dependence on the physical dimension.
On a fixed operator-norm cutoff its coordinates remain in a bounded set.
The finite type list, compact-empty-type exclusion and accepted polynomial-map error bound therefore yield one fixed exponent \(\alpha>0\) and a repair of size \(C\varepsilon^\alpha\).
No inverse of \(A_0\) enters this map or that assertion.

The same real symmetric lift
\[
 \delta X_j=U\delta C_jU^T+
           V\delta B_jU^T+U\delta B_j^TV^T
\]
makes the corrected \(w\) an exact nonzero kernel vector and costs the same Hilbert--Schmidt distance.
Thus the small-singular-value event on that norm cutoff lies within standard-Gaussian distance \(C\sqrt N\,\varepsilon^\alpha\) of the real singular-input set.

For \(N\in\mathcal G(L)\), the real polynomial
\[
 q_N(g)=|\det L_N(g)|^2
\]
is nonzero and has degree at most \(2mN\).
It may vanish at the origin.
The [general affine tube argument](Yin_C_F0186_v2.md#affine-tube), with the accepted singular-level approximation in the [underlying tube lemma](Yin_C_F0186_v1.md#tubes), requires only nonidentity of \(q_N\).
It does not require \(q_N(0)\ne0\).
Consequently, uniformly over \(N\in\mathcal G(L)\),
\[
 \mathbb P\{s_{\min}(L_N)\le\varepsilon,\ \max_j\|X_j^{(N)}\|\le M\}
 \le C N^{5/2}\varepsilon^\alpha
        e^{C N^{5/2}\varepsilon^\alpha}+e^{-cN^2}.
\]
The empty singular-set branch uses the empty-tube case.
The GOE norm failures are exponentially summable by the explicit v8 Gaussian norm calculation.
Taking \(\varepsilon=N^{-B}\) with \(B\alpha>7/2\) gives
\[
 \sum_{N\in\mathcal G(L)}
 \mathbb P\{s_{\min}(L_N)<N^{-B}\}<\infty.
 \tag{Good-dimension-floor}
\]
Thus the polynomial floor holds eventually within every nonidentity dimension, with a single exponent for the fixed coefficient tuple.
No assertion of that floor is made outside \(\mathcal G(L)\).

<a id="general-affine-log-assembly"></a>
### Rechecking and assembling the unchanged logarithmic modules

Assume first \(u\in\mathbb R\).
The [v8 Schultz specialization](Yin_C_F0186_v8.md#goe-affine-input) already uses \(a_0=0\) and spectral parameter \(itI-B_0\).
The deterministic Hermitian \(B_0\) can be singular, and its only domain condition is \(\operatorname{Im}(itI-B_0)=tI>0\).
Neither this model match nor the exact source estimate uses \(A_0^{-1}\).

The Hermitization zero atom is excluded by finite \(u\), and its SS15 algebraicity/Puiseux argument uses this fact without a condition on \(A_0\).
Hence the [same expected singular count](Yin_C_F0186_v8.md#goe-mesoscopic-count) holds:
\[
 \mathbb E\nu_N([0,t])\le C(t^\beta+N^{-1}t^{-6}),
 \qquad
 \mathbb E\nu_N([0,t])\le C't^\beta
 \quad(N^{-\gamma}\le t\le1),
 \quad 0<\gamma<1/(6+\beta).
\]
These are all-dimension estimates, including dimensions outside \(\mathcal G(L)\).

The [v8 global Gaussian Lipschitz calculation](Yin_C_F0186_v8.md#goe-concentration) uses \(L_N(g)-L_N(g')\), so its constant term cancels.
It also imposes no invertibility condition on \(A_0\).
Thus, for \(t_N=N^{-\gamma}\),
\[
 \nu_N([0,t_N])\le C N^{-\gamma\beta}
\]
eventually almost surely through all dimensions.
The clipped statistic
\[
 V_N(t)=\frac1{mN}\sum_k\log\max(s_k(L_N),t)
\]
satisfies the same [moving-clip concentration and mean calculation](Yin_C_F0186_v8.md#goe-logarithmic-limit) through all dimensions.
That calculation uses only the finite free logarithm, fixed-polynomial weak limits, Gaussian norm moments and the expected count above.
It therefore gives \(V_N(t_N)\to u\) almost surely with arbitrary \(A_0\).
The final v8 use of its monic floor is replaced by (Good-dimension-floor).

Specifically, choose its exponent \(B>\gamma\).
Eventually within \(\mathcal G(L)\),
\[
 0\le V_N(t_N)-U_N
 \le B(\log N)\nu_N([0,t_N])\longrightarrow0.
\]
Thus \(U_N\to u\) within \(\mathcal G(L)\).
For all dimensions \(U_N\le V_N(t_N)\), so \(\limsup_NU_N\le u\).
The all-large-even witness result supplies a subsequence attaining \(u\), proving the full upper-limit equality and the all-even limit.

For \(u=-\infty\), use a fixed singular-value regularizer
\[
 U_{N,\delta}=\frac1{2mN}\log\det(L_N^*L_N+\delta^2I).
\]
Its scalar test \(s\mapsto\frac12\log(s^2+\delta^2)\) is globally \(1/(2\delta)\)-Lipschitz.
The same GOE concentration, fixed weak limits and norm moments give \(U_{N,\delta}\to u_\delta\) almost surely for each fixed \(\delta>0\), for arbitrary \(A_0\).
Intersect over a countable decreasing sequence of \(\delta\)'s.
Since \(U_N\le U_{N,\delta}\) and \(u_\delta\downarrow-\infty\), \(U_N\to-\infty\) through all dimensions.
This case needs no nonidentity witness or floor.

<a id="odd-witness-parity"></a>
### The complete odd-witness alternative at a finite target

The deterministic set \(\mathcal G(L)\) is closed under addition.
Indeed block-diagonal sums of two real-symmetric input witnesses transform the evaluated affine pencil, after tensor regrouping, to the direct sum of the two invertible evaluations.
If \(k\in\mathcal G(L)\) is odd, then for every sufficiently large odd \(N\), \(N-k\) is a sufficiently large even dimension and hence belongs to \(\mathcal G(L)\).
Thus \(N=k+(N-k)\) belongs to \(\mathcal G(L)\).
Together with the even witnesses this makes \(\mathcal G(L)\) cofinite.
The good-dimension limit then becomes full-sequence convergence.

If there is no odd witness, the determinant polynomial vanishes identically on every odd-dimensional real-symmetric tuple space.
Therefore every odd-dimensional \(U_N=-\infty\), while the even limit is the finite \(u\).
This proves the exact liminf, limsup and full-sequence criterion in the exact statement above.
It is an existential criterion on the fixed coefficients, without a claim of an algorithm deciding it.

<a id="all-parameter-scalar-transfer"></a>
### Scalar transfer including the exceptional fixed parameter

For an arbitrary fixed scalar \(P\) and \(z\), its exact word-chain pencil has
\[
 \det L_P(z;X)=\det(P(X)-zI)
\]
at every dimension, including \(z=P(0)\).
Its triangular auxiliary block remains invertible at that parameter.
The bounded FK block factorization also remains valid there, because it uses only that auxiliary triangular inverse, not \(P(0)-z\).
Thus
\[
 q\log\Delta_{\tau_q}(L_P(z;s))
 =\log\Delta_\tau(P(s)-z).
\]
For a nonconstant \(P\), the scalar polynomial \((P-z)^*(P-z)\) is nonconstant for every \(z\), by its unchanged highest homogeneous part.
The accepted SS15 scalar atomlessness and algebraic/Puiseux input therefore gives a finite target for every fixed \(z\), independently of whether \(z=P(0)\).
Apply the general affine good-dimension theorem and multiply its normalization by \(q\).
This proves (GOE-scalar-limsup-all-z) and its all-even full limit.
The real-symmetric witness sets of the pencil and \(P-z\) agree by the exact finite determinant identity, so the odd-witness full-sequence criterion transfers as well.

For a constant polynomial, \(P-z\) is a nonzero constant or zero, giving the direct finite and free determinant identity in either case.
The scalar upper-limit conclusion never supplies the full Brown proof by itself; that conclusion is supplied by the retained v8 one-event potential argument selected as part of this candidate proof.

## Current assessment
[Selected decision](#decision-goe-parity-reviewed)

## Assessment history

### Decision goe-parity-candidate

| Field | Value |
| --- | --- |
| date | 2026-11-05T09:18 |
| status | open |
| reason | The complete one-event GOE Brown statement, arbitrary-constant affine good-dimension limit, all-even limit, full upper-limit equality, exact parity criterion and all-parameter scalar consequences are fixed for joint independent review of this extension and the retained v8 proof body. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact GOE Brown and determinant assertions](#statement) | All stated scalar Brown, arbitrary-constant affine good-dimension, even-dimensional, upper-limit and parity assertions, including all fixed scalar parameters and arbitrary cross-size coupling. |
| argument | [Complete assembled candidate proof](#argument) | The explicitly retained actual v8 proof module together with the full witness, arbitrary-constant repair, logarithmic assembly, parity and scalar-transfer argument here; no open v8 assessment is treated as established support. |
| dependency | [Accepted affine resolvent source](../audits/literature/Sch05/Yin_U001.md#sch05-u001) | Schultz Theorem 3.2 at the accepted exact arXiv v1 scope, including the checked GOE variance and matrix-Hermitization application. |
| dependency | [Polynomial-map error bound](Yin_C_F0186_v1.md#error-bound) | Accepted finite-dimensional real polynomial-map error bound, applied to the fixed-type quadratic compression residual maps. |
| dependency | [Gaussian algebraic tubes](Yin_C_F0186_v1.md#tubes) | Accepted Gaussian tube estimate and singular-level approximation for each nonzero real determinant polynomial. |
| dependency | [Word-chain and scalar source inputs](Yin_C_F0186_v1.md#polynomial-application) | Exact word-chain construction and recorded accepted SS15 scalar atomlessness and algebraic/Puiseux interface; its all-parameter adaptation is supplied here. |
| dependency | [Eventual Hermitian nonidentity](Yin_C_F0186_v2.md#generic-rank) | Every sufficiently large Hermitian input dimension has a nonzero determinant polynomial when the free zero atom vanishes; finite free logarithm supplies that hypothesis. |
| dependency | [Nonzero-polynomial affine tube interface](Yin_C_F0186_v2.md#affine-tube) | The origin need not be nonsingular; only nonidentity is used in dimensions in the stated deterministic good set. |
| dependency | [Matrix-valued algebraic/Puiseux input](Yin_C_F0186_v2.md#logarithmic-tail) | Accepted SS15 matrix-valued free law interface, with its zero atom separately excluded by the finite target. |
| dependency | [Singular-value perturbation](Yin_C_F0186_v3.md#singular-value-perturbation) | Frobenius control of the squared sum of singular-value differences for the global spectral-statistic Lipschitz calculation. |
| dependency | [Gaussian concentration](Yin_C_F0186_v3.md#global-lipschitz) | Accepted Gaussian Lipschitz concentration input; the actual GOE factor and constants are derived in the retained module. |
| dependency | [Bounded FK block factorization](Yin_C_F0186_v3.md#linearization-transfer) | Free word-chain block determinant identity with only the unit triangular auxiliary block inverted, including the exceptional scalar parameter. |
| dependency | [Weak limits and planar controls](Yin_C_F0186_v4.md#decision-finite-variance-reviewed) | Hermitized weak convergence, pathwise local planar potential controls and tightness at the exact GOE fixed law. |
| dependency | [Retained candidate proof body](Yin_C_F0186_v8.md#argument) | Actual comparison, count, concentration, real-compression and planar proof text, jointly requiring the present review; this is proof-body reuse rather than an accepted-premise use of the open v8 conclusion. |

### Decision goe-parity-reviewed

| Field | Value |
| --- | --- |
| date | 2026-11-05T09:27 |
| status | proved |
| reason | Independent whole-proof review checked the complete GOE Brown and determinant statement, the retained v8 proof body, every declared input, the general constant-term extension, all-even witnesses, exact parity alternative and all fixed scalar parameters without an unresolved mathematical gap. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact GOE Brown and determinant assertions](#statement) | All stated scalar Brown, arbitrary-constant affine good-dimension, even-dimensional, upper-limit and parity assertions, including all fixed scalar parameters and arbitrary cross-size coupling. |
| argument | [Complete assembled candidate proof](#argument) | The explicitly retained actual v8 proof module together with the full witness, arbitrary-constant repair, logarithmic assembly, parity and scalar-transfer argument here; no open v8 assessment is treated as established support. |
| dependency | [Accepted affine resolvent source](../audits/literature/Sch05/Yin_U001.md#sch05-u001) | Schultz Theorem 3.2 at the accepted exact arXiv v1 scope, including the checked GOE variance and matrix-Hermitization application. |
| dependency | [Polynomial-map error bound](Yin_C_F0186_v1.md#error-bound) | Accepted finite-dimensional real polynomial-map error bound, applied to the fixed-type quadratic compression residual maps. |
| dependency | [Gaussian algebraic tubes](Yin_C_F0186_v1.md#tubes) | Accepted Gaussian tube estimate and singular-level approximation for each nonzero real determinant polynomial. |
| dependency | [Word-chain and scalar source inputs](Yin_C_F0186_v1.md#polynomial-application) | Exact word-chain construction and recorded accepted SS15 scalar atomlessness and algebraic/Puiseux interface; its all-parameter adaptation is supplied here. |
| dependency | [Eventual Hermitian nonidentity](Yin_C_F0186_v2.md#generic-rank) | Every sufficiently large Hermitian input dimension has a nonzero determinant polynomial when the free zero atom vanishes; finite free logarithm supplies that hypothesis. |
| dependency | [Nonzero-polynomial affine tube interface](Yin_C_F0186_v2.md#affine-tube) | The origin need not be nonsingular; only nonidentity is used in dimensions in the stated deterministic good set. |
| dependency | [Matrix-valued algebraic/Puiseux input](Yin_C_F0186_v2.md#logarithmic-tail) | Accepted SS15 matrix-valued free law interface, with its zero atom separately excluded by the finite target. |
| dependency | [Singular-value perturbation](Yin_C_F0186_v3.md#singular-value-perturbation) | Frobenius control of the squared sum of singular-value differences for the global spectral-statistic Lipschitz calculation. |
| dependency | [Gaussian concentration](Yin_C_F0186_v3.md#global-lipschitz) | Accepted Gaussian Lipschitz concentration input; the actual GOE factor and constants are derived in the retained module. |
| dependency | [Bounded FK block factorization](Yin_C_F0186_v3.md#linearization-transfer) | Free word-chain block determinant identity with only the unit triangular auxiliary block inverted, including the exceptional scalar parameter. |
| dependency | [Weak limits and planar controls](Yin_C_F0186_v4.md#decision-finite-variance-reviewed) | Hermitized weak convergence, pathwise local planar potential controls and tightness at the exact GOE fixed law. |
| dependency | [Retained candidate proof body](Yin_C_F0186_v8.md#argument) | Actual comparison, count, concentration, real-compression and planar proof text, jointly requiring the present review; this is proof-body reuse rather than an accepted-premise use of the open v8 conclusion. |
| review | [Independent complete GOE finding](../audits/reviews/Yin_R_F0190_v8.md#independent-goe-parity-proof) | Whole v9 statement and argument together with the retained v8 body, every exact declared dependency, all boundary cases and the one-event Brown quantifier. |


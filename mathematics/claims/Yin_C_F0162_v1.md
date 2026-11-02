---
author: Yin
---
# A factor-two quadratic estimate for scalar normal vacua and free normal tuples

Task: [T_F0011](../tasks/Yin_T_F0011_v1.md#contract).
Provenance: project deduction developed on 2026-10-16 for Yin.
Root proposed the factor-two test after the three-circle obstruction to the vacuum-norm constant; the scalar-test subagent developed the soft-kernel polarization and cancellation argument below.
The finite-point diagnostics were discovery leads only and are not proof inputs.
At the original candidate checkpoint, this complete argument was fixed for fresh independent review without accepting it as proved.
It does not complete the correlated-normal Task.

## Current assessment
[Selected decision](#decision-reviewed-quadratic)

## Statement

**A. General scalar normal laws.**
Let \(\mu\) be a compactly supported nonatomic Borel probability on \(\mathbb C\), and put
\[
 M=L^\infty(\mu),\qquad \tau(f)=\int f\,d\mu,\qquad H=L^2(\mu),
 \qquad X(z)=z,\qquad P=\mathbb C[X,X^*].
\]
The algebra \(P\) is the represented unital star algebra and is dense in \(H\).
Inner products are linear in the second variable.
Define the outer derivation
\[
 \delta f(z,w)=\frac{f(z)-f(w)}{z-w},\qquad f\in P,
\]
off the product-null diagonal.
Assume the actual Hilbert adjoint condition
\[
 1\otimes1\in\operatorname{Dom}\delta^*,\qquad
 \xi=\delta^*(1\otimes1)\in H.
 \tag{S1}
\]
Then \(a\otimes1\) and \(1\otimes a\) belong to the actual adjoint domain for every \(a\in P\), and
\[
 T_\ell(a)=\delta^*(a\otimes1)
 =\delta^*(1\otimes a)=T_r(a)=:T(a).
\]
For every real-valued \(f\in P\),
\[
 \|Tf\|_2^2\le\operatorname{Re}\langle T(f^2),\xi\rangle.
 \tag{S2}
\]
For every complex \(a\in P\),
\[
 \boxed{\quad
 \|Ta\|_2^2
 \le2\operatorname{Re}\langle T(|a|^2),\xi\rangle
 \le2\|\xi\|_2\|T(|a|^2)\|_2.
 \quad}
 \tag{S3}
\]
Thus both proposed scalar quadratic estimates hold with the finite constant \(2\|\xi\|_2\).
This constant is sufficient; its optimality is not asserted.

The result covers every one-generator normal condition-A system in its generated finite tracial algebra.
Indeed the actual normal A condition forces the spectral law to be nonatomic, and its derivation on the starred core is uniquely the displayed divided difference.
No radial symmetry, curve support, Hilbert-space boundedness or principal-value existence is assumed.

**B. Freely independent normal coordinates.**
Let \(X_1,\ldots,X_d\) be bounded normal generators of a finite tracial \(M\) with faithful normal probability trace, and suppose \(B_j=W^*(X_j)\) are freely independent.
Write \(H=L^2(M,\tau)\), \(\Omega=1\), and let \(P_\Omega\) be the orthogonal projection onto \(\mathbb C\Omega\).
Set \(P=\mathbb C\langle X_1,\ldots,X_d,X_1^*,\ldots,X_d^*\rangle\).
Assume the full actual A condition given by complex-linear outer derivations
\[
 \delta_j:P\subset L^2(M)\longrightarrow L^2(M)\otimes_2L^2(M),
 \quad\delta_jX_k=\delta_{jk}1\otimes1,\quad
 \xi_j=\delta_j^*(1\otimes1)\in L^2(M).
\]
In particular \(1\otimes1\) belongs to each actual Hilbert adjoint domain.
For \(T_{j,\ell}(a)=\delta_j^*(a\otimes1)\) and \(T_{j,r}(a)=\delta_j^*(1\otimes a)\), the following hold on every mixed starred polynomial:
\[
 \begin{aligned}
 \|T_{j,\ell}(a)\|_2^2
 &\le2\operatorname{Re}\langle T_{j,\ell}(a^*a),\xi_j\rangle
 \le2\|\xi_j\|_2\|T_{j,\ell}(a^*a)\|_2,\\
 \|T_{j,r}(a)\|_2^2
 &\le2\operatorname{Re}\langle T_{j,r}(aa^*),\xi_j\rangle
 \le2\|\xi_j\|_2\|T_{j,r}(aa^*)\|_2.
 \end{aligned}
 \tag{S4}
\]
In particular the two contractions
\[
 E_{j,0}=(\mathrm{id}\otimes\tau)\delta_j,\qquad
 F_{j,0}=(\tau\otimes\mathrm{id})\delta_j
\]
satisfy
\[
 \|E_{j,0}a\|_2,\ \|F_{j,0}a\|_2
 \le3\|\xi_j\|_2\|a\|,\qquad a\in P.
 \tag{S5}
\]
The original canonical operator \(D_j^{\mathrm{can}}=-\overline{E_{j,0}}\) has
\[
 M\Omega\subseteq\operatorname{Dom}D_j^{\mathrm{can}}
              \cap\operatorname{Dom}(D_j^{\mathrm{can}})^*,
 \qquad
 [X_k,D_j^{\mathrm{can}}]|_{M\Omega}
   =\delta_{jk}P_\Omega|_{M\Omega}.
 \tag{S6}
\]
Thus these canonical operators witness S.
The all-bounded-vector domain conclusion for this free class was already known; the new conclusions are the fixed-vector quadratic estimates and the stated constants.
No correlated-coordinate lifting is asserted.

## Direct inputs and reuse

| Direct input | Exact scope used |
| --- | --- |
| [C_F0055, Sections 3-5](Yin_C_F0055_v1.md#3-the-actual-vacuum-identity-extends-to-smooth-scalar-tests), [selected proof](Yin_C_F0055_v1.md#decision-candidate-0002) | Actual scalar vacuum extends to smooth tests; its positive soft three-point identity and consequent uniform soft Cauchy bound hold under exactly (S1). The proof below restates the kernel with the conjugate orientation explicitly. |
| [C_F0055, Sections 6-7](Yin_C_F0055_v1.md#6-positive-weights-give-the-scalar-core-bound) | Its original polynomial soft difference quotients converge strongly to the actual contraction, and its actual adjoint formula identifies both scalar one-sided adjoints. The strong convergence is also proved directly below. |
| [C_F0076, Part 1](Yin_C_F0076_v1.md#statement), [selected proof](Yin_C_F0076_v1.md#decision-reviewed) | Actual normal A implies diffuse marginals and the unique phase derivative; this identifies the scope with every scalar normal actual-A law. No iterated-derivative result is used. |
| [C_F0160, Part A](Yin_C_F0160_v1.md#statement), [selected proof](Yin_C_F0160_v1.md#decision-reviewed-quadratic) | Its fixed-vector free-product lifting with \(g_\ell=g_r=2\xi_j\) gives (S4), including the actual marginal vacuum identification and both square orders. Its radial Part B is not needed. |
| [Mai15-U002](../audits/literature/Mai15/Yin_U002.md#mai15-u002) | The inspected Hilbert-valued power-iteration mechanism of Lemma 4.11, after the quadratic bound is proved; its real coassociative energy identity is not imported. |
| [C_F0072, Part B](Yin_C_F0072_v1.md#statement), [selected proof](Yin_C_F0072_v1.md#decision-reviewed) | Both original canonical domains follow from the two bounded core contractions. |

C_F0160 owns its own exact assessment and review selection; this material does not change them.
The [three-circle obstruction](Yin_C_F0161_v1.md#statement) motivated the larger constant, but is not a logical premise.
No positivity assertion for the contribution of each distinct triple to the complex quadratic form is used.
The scalar proof instead polarizes the already established nonnegative cubic soft energy and then cancels the terms that would require strong convergence of the soft vacuum.

## Argument

### 1. Actual scalar operators and orientation

The quotient defining \(\delta\) is bounded for every starred polynomial on a compact rectangle surrounding the support.
It is independent of the representative, satisfies the outer Leibniz rule and has \(\delta X=1\otimes1\).
Let
\[
 E_0=(\mathrm{id}\otimes\tau)\delta,\qquad Ja=\bar a,\qquad L=JE_0J
 \quad\text{on }P.
\]
The actual vacuum identity is
\[
 \langle\xi,p\rangle
 =\langle1\otimes1,\delta p\rangle
 =\int E_0p\,d\mu,\qquad p\in P.
 \tag{1}
\]
By the actual scalar adjoint formula in C_F0055 Section 7,
\[
 T(a)=a\xi-L(a)=E_0^*a,\qquad a\in P.
 \tag{2}
\]
The divided difference is symmetric in its two variables, so both one-sided tensor adjoints equal this actual vector.
The cited formula follows by expanding \(\delta(\bar a p)\) in (1) and exchanging the two spectral variables.
It establishes the actual adjoint domains and does not choose a new extension.

For a general one-generator normal actual-A system, C_F0076 Part 1 gives a nonatomic spectral law.
In its spectral representation, differentiating \(XX^*=X^*X\) gives
\[
 (z-w)\delta(X^*)(z,w)=\bar z-\bar w.
\]
The null collision diagonal makes multiplication by \(z-w\) injective.
This determines \(\delta(X^*)\); the Leibniz rule then gives precisely the displayed divided difference on the whole starred core.
Thus (1)-(2) apply to the actual supplied derivation.

### 2. Bounded soft kernels and the complete collision terms

For \(t>0\) set
\[
 k_t(z,w)=\frac{z-w}{|z-w|^2+t},\qquad
 C_tf(z)=\int k_t(z,w)f(w)\,d\mu(w),\qquad
 B_t=C_t1.
 \tag{3}
\]
This kernel is the complex conjugate of the kernel used in C_F0055.
It is bounded, antisymmetric, and zero on the diagonal.
The operators in this section are bounded on \(H\).
Define
\[
 u_t=2B_t,\qquad
 L_t=M_{B_t}-C_t,\qquad
 T_t=M_{B_t}+C_t=M_{u_t}-L_t.
 \tag{4}
\]
These are temporary bounded regularizations; neither \(u_t\) nor \(T_t\) is being identified with an actual adjoint value of the original \(\delta\).

For three points define the symmetric real kernel
\[
 \begin{aligned}
 S_t(z,w,v)
 &=\operatorname{Re}\bigl(k_t(z,w)\overline{k_t(z,v)}\bigr)\\
 &\quad+\operatorname{Re}\bigl(k_t(w,z)\overline{k_t(w,v)}\bigr)\\
 &\quad+\operatorname{Re}\bigl(k_t(v,z)\overline{k_t(v,w)}\bigr).
 \end{aligned}
 \tag{5}
\]
Put \(x=|z-v|^2\), \(y=|w-v|^2\), \(r=|z-w|^2\), and
\[
 H_\triangle=2xy+2yr+2rx-x^2-y^2-r^2.
\]
The checked identity in C_F0055 Section 4 is unchanged by conjugating the kernel:
\[
 S_t(z,w,v)
 =\frac{H_\triangle+t(x+y+r)}
        {2(x+t)(y+t)(r+t)}\ge0.
 \tag{6}
\]
Here \(H_\triangle\) is sixteen times the squared triangle area.
Formula (6) is a polynomial identity after multiplying by its positive denominator, and therefore remains valid at collisions.
If \(z=w\ne v\), then \(S_t=|k_t(z,v)|^2\); if all three points agree, then \(S_t=0\).
Thus no repeated-point term is discarded.
For the diffuse measure these collision sets are null, but boundedness and (6) are available without using that fact.

For every finite positive measure \(\rho\), Fubini and permutation symmetry give
\[
 I_t(\rho):=\int\left|\int k_t(z,w)\,d\rho(w)\right|^2d\rho(z)
 =\frac13\iiint S_t\,d\rho^3.
 \tag{7}
\]
All terms are absolutely integrable because the soft kernel is bounded.

### 3. Polarization for real functions

Fix a bounded real measurable \(f\).
For sufficiently small real \(s\), the measure \(\rho_s=(1+sf)\mu\) is positive.
Expanding both sides of (7) as polynomials in \(s\) is therefore justified and gives equality of the coefficients.

The coefficient of \(s^2\) is
\[
 \|C_tf\|_2^2
 +2\operatorname{Re}\int f\,C_tf\,\overline{B_t}\,d\mu
 =\iiint S_t(z,w,v)f(z)f(w)\,d\mu^3.
 \tag{8}
\]
For clarity, the three pair terms on the kernel side have identical integrals because \(S_t\) is symmetric, and cancel the factor \(1/3\) in (7).

Applying the coefficient-of-\(s\) identity instead to the bounded real test \(f^2\) gives
\[
 \int f^2|B_t|^2\,d\mu
 +2\operatorname{Re}\int C_t(f^2)\overline{B_t}\,d\mu
 =\iiint S_t(z,w,v)f(z)^2\,d\mu^3.
 \tag{9}
\]
Adding \(\int f^2|B_t|^2\,d\mu\) to (8), and using (4) and (9), yields the exact identity
\[
 \begin{aligned}
 \operatorname{Re}\langle T_t(f^2),u_t\rangle-\|T_tf\|_2^2
 &=\iiint S_t\bigl(f(z)^2-f(z)f(w)\bigr)\,d\mu^3\\
 &=\frac12\iiint S_t\bigl(f(z)-f(w)\bigr)^2\,d\mu^3
 \ge0.
 \end{aligned}
 \tag{10}
\]
The factor \(u_t=2B_t\) in (10) is essential.
The last equality uses symmetry under \(z,w\), and the inequality uses \(S_t\ge0\).
This calculation is valid for all bounded real \(f\), including all real starred polynomials.

### 4. Actual weak vacua and strong difference quotients

Define the soft difference quotient contraction
\[
 E_tp(z)
 =\int\frac{p(z)-p(w)}{z-w}
          \frac{|z-w|^2}{|z-w|^2+t}\,d\mu(w),
 \qquad p\in P.
 \tag{11}
\]
The multiplier is between zero and one and converges to one off the collision diagonal.
Each original polynomial divided difference is bounded.
Dominated convergence on \(\mu^2\), followed by the bounded tensor contraction, gives
\[
 E_tp\longrightarrow E_0p\quad\text{strongly in }H.
 \tag{12}
\]
This is the original-core convergence used in C_F0055 Section 6.
The orientation in (3) gives exactly
\[
 L_t=JE_tJ,\qquad L_tp\longrightarrow Lp
 \quad\text{strongly in }H,\quad p\in P.
 \tag{13}
\]

C_F0055 Section 5 gives
\[
 \|B_t\|_2\le\|\xi\|_2,\qquad \|u_t\|_2\le2\|\xi\|_2,
 \qquad t>0.
 \tag{14}
\]
Its hypotheses are precisely the compact nonatomic scalar actual-vacuum identity (1).
Conjugating that source's kernel preserves the norm, so (14) applies to (3).
Antisymmetry of the soft kernel gives, for every \(p\in P\),
\[
 \langle u_t,p\rangle=\int E_tp\,d\mu
 \longrightarrow\int E_0p\,d\mu=\langle\xi,p\rangle.
 \tag{15}
\]
Since \(P\) is dense in \(H\), the uniform bound (14) extends convergence of these pairings to every Hilbert vector:
\[
 u_t\rightharpoonup\xi\quad\text{weakly in }H.
 \tag{16}
\]
Only weak convergence is asserted or needed.

### 5. Cancellation before the limit

Fix a real \(f\in P\), so \(f^2\in P\).
The inequality (10), written using \(T_tf=fu_t-L_tf\), is
\[
 \|fu_t-L_tf\|_2^2
 \le\operatorname{Re}\langle f^2u_t-L_t(f^2),u_t\rangle.
\]
Expanding cancels the identical term \(\|fu_t\|_2^2\) on both sides and leaves
\[
 \|L_tf\|_2^2
 \le\operatorname{Re}
       \langle 2fL_tf-L_t(f^2),u_t\rangle.
 \tag{17}
\]
The first vector in the right pairing converges strongly by (13), because f is bounded.
The second converges weakly by (16), with the uniform norm bound (14).
Thus the right pairing converges, and (17) gives
\[
 \|Lf\|_2^2
 \le\operatorname{Re}\langle2fLf-L(f^2),\xi\rangle.
 \tag{18}
\]
Reintroducing \(\|f\xi\|_2^2\) and using the actual formula (2) yields
\[
 \|Tf\|_2^2\le\operatorname{Re}\langle T(f^2),\xi\rangle,
\]
which proves (S2).
There is no passage through a pairing of two merely weakly convergent vectors.

For arbitrary \(a\in P\), write
\[
 f=\frac{a+a^*}{2},\qquad h=\frac{a-a^*}{2\mathrm i}.
\]
Both f and h are real elements of \(P\), and the scalar algebra is commutative, so
\(|a|^2=f^2+h^2\).
Complex linearity of T and the elementary Hilbert inequality give
\[
 \begin{aligned}
 \|Ta\|_2^2
 &=\|Tf+\mathrm iTh\|_2^2\\
 &\le2\bigl(\|Tf\|_2^2+\|Th\|_2^2\bigr)\\
 &\le2\operatorname{Re}\langle T(f^2+h^2),\xi\rangle.
 \end{aligned}
 \tag{19}
\]
Cauchy--Schwarz supplies the last inequality in (S3).
In particular the real part of the pairing in (S3) is nonnegative.
Unlike the radial stronger estimate, the entire complex pairing is not asserted to be real.
This proves Part A.

### 6. Free-product application and canonical domains

Under the hypotheses of Part B, C_F0160 Part A identifies the actual marginal vacuum with the same global vector \(\xi_j\in L^2(B_j)\).
Its normal marginal is a scalar actual-A model, so Part A above applies without a rotational assumption.
Use the two fixed vectors
\[
 g_\ell=g_r=2\xi_j
\]
in C_F0160 Part A.
The marginal scalar products \(b^*b\) and \(bb^*\) agree, and (S3) supplies both required one-sided inequalities.
The fixed-vector lifting theorem then gives (S4) on the complete mixed starred polynomial core, with the specified left \(a^*a\) and right \(aa^*\) orders.

For either one-sided map T, the actual-adjoint formula and Leibniz rule give, for every positive integer m,
\[
 \|T(a^m)\|_2
 \le\|a\|^m\|\xi_j\|_2+
       m\|a\|^{m-1}\|\delta_j(a^*)\|_2.
 \tag{20}
\]
Hence \(\limsup_m\|T(a^m)\|_2^{1/m}\le\|a\|\).
With \(C=2\|\xi_j\|_2\), iterate the corresponding inequality (S4) on \(b,b^2,b^4,\ldots\), where \(b=a^*a\) for the left map and \(b=aa^*\) for the right map.
The Hilbert-valued power iteration in Mai15-U002 yields
\[
 \|T_{j,\ell}(a)\|_2,\ \|T_{j,r}(a)\|_2
 \le2\|\xi_j\|_2\|a\|.
 \tag{21}
\]
The vector \(\xi_j\) is nonzero because
\(\langle\xi_j,X_j\rangle=\langle1\otimes1,\delta_jX_j\rangle=1\), so no zero constant is divided by.

Taking stars in the actual one-sided adjoint formulas gives
\[
 E_{j,0}(a)=a\xi_j^*-T_{j,r}(a^*)^*,\qquad
 F_{j,0}(a)=\xi_j^*a-T_{j,\ell}(a^*)^*.
\]
Together with (21), these prove (S5).
C_F0072 Part B now puts every bounded vector in the original closure domain and its actual adjoint domain.
To extend the generator commutator, take uniformly bounded core approximants \(a_n\to a\) in \(L^2\).
The two slice bounds control the graphs of \(a_n\) and \(X_ka_n\); weak closedness identifies their limits with the original closure.
Passing to the limit in
\[
 E_{j,0}(X_ka_n)-X_kE_{j,0}(a_n)=\delta_{jk}\tau(a_n)1
\]
gives the same identity on M.
The sign \(D_j^{\mathrm{can}}=-\overline{E_{j,0}}\) is exactly the generator-first convention in (S6).

## Scope and review boundary

The new scalar argument uses positive soft Cauchy energy only for real perturbations, followed by a Hilbert-space real/imaginary decomposition.
It does not assert nonnegativity of a complex quadratic contribution for each distinct triple, and no diagonal correction is omitted.
The weak soft-vacuum limit is adequate only after the explicit cancellation (17).
No strong convergence of the soft vacuum, principal-value theorem, entire-H domain, sharpness of factor two, or correlated normal estimate is asserted.
The free-product consequence invokes the separate exact lifting result and does not extend that result beyond freely independent scalar normal factors.

At that candidate checkpoint, a fresh full review was required, especially of the coefficients in (8)-(10), the conjugate kernel orientation, actual adjoint identification, weak/strong limit in (17), and the stated direct-input interfaces.
The [selected assessment](#current-assessment) adopts the completed whole [R_F0171 finding](../audits/reviews/Yin_R_F0171_v1.md#conclusion); the additional R_F0170 check retains its separate Part A scope.
The independent-review and selected-assessment status of C_F0160 remains owned by that material.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-16T03:30 |
| status | open |
| reason | Fix the completed scalar soft-polarization and cancellation candidate, with the finite factor-two quadratic constant and its exact free-normal consequence, for fresh independent review before acceptance. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Parts A and B: real scalar pairing estimate, complex factor-two estimate, both free mixed-word square orders, slice constants and original canonical domains. |
| argument | [Argument](#argument) | All six sections, including complete collision terms, cubic polarization, actual weak vacua, strong core contractions, cancellation before passage, complex decomposition and free-product application. |
| dependency | [Scalar soft Cauchy theorem](Yin_C_F0055_v1.md#statement) | Sections 3-7 only: positive soft three-point energy, uniform soft Cauchy bound, actual original-core convergence and scalar adjoint formula. |
| dependency | [Normal diffuse phase](Yin_C_F0076_v1.md#statement) | Part 1 only identifies every actual normal scalar A derivation with the nonatomic divided difference. |
| dependency | [Fixed-vector free lifting](Yin_C_F0160_v1.md#statement) | Part A only, with both fixed vectors equal to twice the actual marginal/global vacuum; used exclusively for Part B here. |
| dependency | [Hilbert-valued power iteration](../audits/literature/Mai15/Yin_U002.md#mai15-u002) | Lemma 4.11 mechanism after (S4) and the automatic growth estimate (20). |
| dependency | [Original two-domain criterion](Yin_C_F0072_v1.md#statement) | Part B restores both original canonical domains from the two slice estimates (S5). |

### Decision reviewed-quadratic

| Field | Value |
| --- | --- |
| date | 2026-10-16T03:41 |
| status | proved |
| reason | Adopt the complete fixed statement and argument after independent whole-proof review and a second independent scalar review, with all direct-input interfaces checked at their exact scopes. The unrestricted correlated-normal implication and optimality of factor two remain unresolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Parts A and B: scalar real and complex quadratic inequalities, both free mixed-word square orders, slice constants and the original canonical domains. |
| argument | [Argument](#argument) | All six sections, including collisions, polarization, cancellation before weak passage, complex decomposition, free-product lifting and original domain restoration. |
| dependency | [Scalar soft Cauchy theorem](Yin_C_F0055_v1.md#statement) | Sections 3-7 only: positive soft three-point energy, uniform soft Cauchy bound, actual original-core convergence and scalar adjoint formula. |
| dependency | [Normal diffuse phase](Yin_C_F0076_v1.md#statement) | Part 1 only identifies every actual normal scalar A derivation with the nonatomic divided difference. |
| dependency | [Fixed-vector free lifting](Yin_C_F0160_v1.md#statement) | Part A only, with both fixed vectors equal to twice the actual marginal/global vacuum; used exclusively for Part B here. |
| dependency | [Hilbert-valued power iteration](../audits/literature/Mai15/Yin_U002.md#mai15-u002) | Lemma 4.11 mechanism after (S4) and the automatic growth estimate (20). |
| dependency | [Original two-domain criterion](Yin_C_F0072_v1.md#statement) | Part B restores both original canonical domains from the two slice estimates (S5). |
| review | [Independent whole-proof review](../audits/reviews/Yin_R_F0171_v1.md#conclusion) | Entire fixed statement and argument and all declared direct-input applications, with exact scope and reuse limits in the review bindings. |
| review | [Independent scalar review](../audits/reviews/Yin_R_F0170_v1.md#scalar-conclusion) | Additional independent check of Part A, argument Sections 1-5 and their scalar direct inputs only; no Part B coverage is inferred from this review. |


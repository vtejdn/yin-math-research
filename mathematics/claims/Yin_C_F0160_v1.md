---
author: Yin
---
# Free products preserve fixed-vector quadratic adjoint domination

Task: [T_F0011](../tasks/Yin_T_F0011_v1.md#contract).
Provenance: project deduction, developed on 2026-10-16 for Yin.
Root supplied the free-module proof outline; the quadratic-abstract subagent checked its full-core, completed-tensor, actual-adjoint and conditional-expectation steps and wrote this candidate.
The sharp radial application uses the separately developed candidate [C_F0159](Yin_C_F0159_v1.md#statement).
This registration is a complete proof draft awaiting independent review; it does not accept either candidate as proved.

## Current assessment
[Selected decision](#decision-reviewed-quadratic)

## Statement

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal probability trace, let \(H=L^2(M,\tau)\), and let \(X=(X_1,\ldots,X_d)\) be a finite bounded normal generating tuple.
Assume that the coordinate algebras \(B_j=W^*(X_j)\) are freely independent.
Put
\[
 P_j=\mathbb C[X_j,X_j^*],\qquad
 P=\mathbb C\langle X_1,\ldots,X_d,X_1^*,\ldots,X_d^*\rangle,
 \qquad H_j=L^2(B_j,\tau).
\]
These are represented algebras.
Assume the full actual ACSY condition: outer derivations
\[
 \delta_j:P\subset H\longrightarrow H\otimes_2H,\qquad
 \delta_j(X_k)=\delta_{jk}1\otimes1,\qquad
 1\otimes1\in\operatorname{Dom}\delta_j^*
\]
exist, with actual vacua \(\xi_j=\delta_j^*(1\otimes1)\).
Inner products are linear in the second variable.

Fix j.
The restriction \(\delta_j^{\mathrm m}=\delta_j|_{P_j}\) takes values in \(H_j\otimes_2H_j\) and has actual marginal vacuum \(\xi_j\in H_j\).
Define the actual marginal and global one-sided adjoints
\[
 \begin{split}
 t_\ell(b)&=(\delta_j^{\mathrm m})^*(b\otimes1),&
 t_r(b)&=(\delta_j^{\mathrm m})^*(1\otimes b),\quad b\in P_j,\\
 T_\ell(a)&=\delta_j^*(a\otimes1),&
 T_r(a)&=\delta_j^*(1\otimes a),\quad a\in P.
 \end{split}
 \tag{1}
\]
All these tensors belong to the stated actual adjoint domains.

**A. Fixed-vector domination lifts without a change of vector or constant.**
If \(g_\ell\in H_j\) satisfies
\[
 \|t_\ell(b)\|_2^2
 \le\operatorname{Re}\langle t_\ell(b^*b),g_\ell\rangle
 \qquad(b\in P_j),
 \tag{2}
\]
then, regarding \(g_\ell\) as the same vector in H,
\[
 \|T_\ell(a)\|_2^2
 \le\operatorname{Re}\langle T_\ell(a^*a),g_\ell\rangle
 \le\|g_\ell\|_2\|T_\ell(a^*a)\|_2
 \qquad(a\in P).
 \tag{3}
\]
Independently, if \(g_r\in H_j\) satisfies
\[
 \|t_r(b)\|_2^2
 \le\operatorname{Re}\langle t_r(bb^*),g_r\rangle
 \qquad(b\in P_j),
 \tag{4}
\]
then
\[
 \|T_r(a)\|_2^2
 \le\operatorname{Re}\langle T_r(aa^*),g_r\rangle
 \le\|g_r\|_2\|T_r(aa^*)\|_2
 \qquad(a\in P).
 \tag{5}
\]
No entire-H boundedness of any marginal or global contraction is assumed.
No additional adjoint-domain membership is required of \(g_\ell\) or \(g_r\).

**B. Freely independent rotational normal coordinates have sharp paired constants.**
If the spectral law of \(X_j\) is rotation invariant, then the radial estimate of C_F0159 gives (2) and (4) with
\[
 g_\ell=g_r=\xi_j.
\]
Consequently, for all mixed starred polynomials \(a\in P\),
\[
 \|T_\ell(a)\|_2^2
 \le\operatorname{Re}\langle T_\ell(a^*a),\xi_j\rangle
 \le\|\xi_j\|_2\|T_\ell(a^*a)\|_2,
 \tag{6}
\]
and
\[
 \|T_r(a)\|_2^2
 \le\operatorname{Re}\langle T_r(aa^*),\xi_j\rangle
 \le\|\xi_j\|_2\|T_r(aa^*)\|_2.
 \tag{7}
\]
Each of the two constants \(\|\xi_j\|_2\) is optimal for this fixed global system.
Only the distinguished marginal needs to be rotational for (6)--(7).

If every coordinate is rotational, then every prescribed derivation has these sharp paired estimates.
Writing
\[
 E_{j,0}=(\mathrm{id}\otimes\tau)\delta_j,\qquad
 F_{j,0}=(\tau\otimes\mathrm{id})\delta_j,
 \qquad D_j^{\mathrm{can}}=-\overline{E_{j,0}},
\]
both contractions obey
\[
 \|E_{j,0}a\|_2,\ \|F_{j,0}a\|_2
 \le2\|\xi_j\|_2\|a\|\qquad(a\in P),
 \tag{8}
\]
and the original canonical operators satisfy
\[
 M\Omega\subseteq
 \operatorname{Dom}D_j^{\mathrm{can}}
 \cap\operatorname{Dom}(D_j^{\mathrm{can}})^*,
 \qquad
 [X_k,D_j^{\mathrm{can}}]|_{M\Omega}
 =\delta_{jk}P_\Omega|_{M\Omega}.
 \tag{9}
\]
Thus they witness S.
The existence of S for freely independent scalar normal ACSY marginals was already known; the additional assertion is the mixed-polynomial quadratic domination with its sharp constants.

Neither part asserts a corresponding lifting for correlated coordinate algebras or for arbitrary noncommutative free factors.
The statement uses normal scalar coordinate factors throughout.

## Direct inputs and scope

| Direct input | Exact use |
| --- | --- |
| [C_F0076 Part 1](Yin_C_F0076_v1.md#statement), [selected proof](Yin_C_F0076_v1.md#decision-reviewed) | Under exactly the stated actual normal A hypotheses, the marginal laws are diffuse and \(\delta_j(X_k^*)=\delta_{jk}k_j\); the full actual tensor-adjoint domain is available. No second-derivative estimate is used. |
| [C_F0045 Sections 3--5](Yin_C_F0045_v1.md#3-an-orthogonal-right-module-decomposition-of-the-full-core), [selected proof](Yin_C_F0045_v1.md#decision-candidate-0002) | The finite reduced-polynomial module decomposition, expectation identity, annihilation of earlier cuts for completed Hilbert tensors and the actual direct-sum adjoint mechanism. The applicability and opposite-side version are checked below. |
| [C_F0159](Yin_C_F0159_v1.md#statement) | Its strengthened radial pairing inequality, with the actual scalar vacuum, supplies Part B. This input is a separate proof draft pending independent review; it is not needed for Part A. |
| [Mai15-U003](../audits/literature/Mai15/Yin_U002.md#mai15-u002) | The inspected Hilbert-norm power-iteration mechanism of Lemma 4.11. Its real coassociative energy identity is not used. |
| [C_F0072 Part B](Yin_C_F0072_v1.md#statement), [selected proof](Yin_C_F0072_v1.md#decision-reviewed) | The two operator-norm-to-L2 slice bounds restore the original canonical closure and its actual adjoint on all bounded vectors. |

The C_F0045 proof uses the pointed free-product Hilbert representation already sourced there through [Voi98-U005](../audits/literature/Voi98/Yin_U005.md#voi98-u005) and its stated RX06 interface.
This candidate reuses that checked representation with its exact scalar normal factors.
C_F0045's little Grothendieck step is not used.
The finite-family abstract separation argument in D_F0006 is also not used.
The new step is summing the given fixed-vector marginal domination before taking a norm and identifying that sum through the vacuum-sector projection.
There is no new external theorem or historical-priority assertion.

## Argument

### 1. Actual marginal derivation and full-core slice identities

Fix j and suppress its index.
By C_F0076 Part 1, \(\delta\) kills \(P_k\) for every \(k\ne j\).
On \(P_j\), it is the scalar divided difference
\[
 \delta^{\mathrm m}b(z,w)=\frac{b(z)-b(w)}{z-w}
 \quad(\mu_j^2\text{-almost everywhere}).
 \tag{10}
\]
The normal marginal law is diffuse, so the collision diagonal is null.
The range in (10) is in \(H_j\otimes_2H_j\); it need not be an algebraic tensor.
The quotient is symmetric in the two spectral variables.
Thus its two marginal slice operators agree on \(P_j\), although the global slice operators need not agree.

The general actual-adjoint formula gives \(P\odot P\subseteq\operatorname{Dom}\delta^*\).
For
\[
 E_0=(\mathrm{id}\otimes\tau)\delta,\qquad
 F_0=(\tau\otimes\mathrm{id})\delta
\]
it gives directly
\[
 T_\ell=E_0^*|_P,\qquad T_r=F_0^*|_P,
 \qquad E_0^*1=F_0^*1=\xi.
 \tag{11}
\]
For example \(\langle T_\ell(a),p\rangle
=\langle a\otimes1,\delta p\rangle=\langle a,E_0p\rangle\).
These are identities with actual Hilbert adjoints.

The operators \(E_0\) also meet the small-core dual setup used for the cited C_F0045 decomposition.
Indeed \(E_0 1=0\), the preceding formula gives its actual adjoint vacuum, and Leibniz gives
\([E_0,X_k]=\delta_{jk}P_\Omega\).
The commutator with \(X_k^*\) is the Hilbert--Schmidt operator associated with \(\delta(X_k^*)\), which is zero or the phase in (10).
Thus no additional supplied dual is being assumed.
Only the portions of C_F0045 preceding its marginal infinity-to-2 estimate are used.

### 2. Right modules and the actual adjoint

For each k, Gram--Schmidt on its starred monomials gives an orthonormal basis of \(H_k\ominus\mathbb C1\) consisting of bounded centered polynomials and algebraically spanning \(P_k\ominus\mathbb C1\).
For fixed j, let \(\mathcal U\) consist of 1 and every reduced product of these basis vectors whose last factor is outside j.
The C_F0045 free-product representation gives the unitary
\[
 V:\ell^2(\mathcal U)\otimes_2H_j\longrightarrow H,\qquad
 V(e_u\otimes b)=ub.
 \tag{12}
\]
The bounded polynomial u multiplies every \(b\in H_j\).
The scalar and centered parts of b give exactly the reduced-word basis, each once.

Writing \(\mathbb E_j:M\to B_j\) for the trace-preserving conditional expectation, the same isometry gives
\[
 \mathbb E_j(u^*v)=\delta_{uv}1.
 \tag{13}
\]
Indeed pair the proposed equality against bounded \(b,c\in P_j\), use (12) for \(ub,vc\), and then use density and faithfulness.
Every \(a\in P\) has a finite expansion
\[
 a=\sum_{u\in F}u b_u,\qquad b_u\in P_j,\qquad
 b_u=\mathbb E_j(u^*a).
 \tag{14}
\]
Finiteness follows by expanding every original word into reduced centered-factor polynomials and using their finite basis expansions.
In particular \(\mathbb E_j(P)\subseteq P_j\), and
\[
 \mathbb E_j(a^*a)=\sum_{u\in F}b_u^*b_u.
 \tag{15}
\]

Put \(e_0=(\mathrm{id}\otimes\tau)\delta^{\mathrm m}\) on \(P_j\).
In differentiating \(ub\), every cut in a j-factor of u has a nonempty reduced suffix c starting and ending outside j.
Thus \(\mathbb E_j(cb)=0\) and
\(\tau(ycb)=0\) for every \(y\in H_j\).
The latter follows first for bounded y from conditional expectation and then for all \(H_j\) by L2 density, since cb is bounded.
It annihilates the contracted second leg of the cut.
For a Hilbert-tensor derivative, approximate its two-leg vector by algebraic \(H_j\) tensors; the fixed bounded prefix and suffix and the slice are continuous on that Hilbert space, so the same cancellation holds.
Only the final factor derivative remains:
\[
 E_0(ub)=u e_0b,\qquad
 V^*E_0V=\bigoplus_{u\in\mathcal U}^{\mathrm{alg}} e_0
 \quad\text{on }\bigoplus_{u\in\mathcal U}^{\mathrm{alg}}P_j.
 \tag{16}
\]

Testing against single coordinates and then against all finite supported inputs proves the actual adjoint formula
\[
 V^*E_0^*V=\bigoplus_{u\in\mathcal U}e_0^*,\qquad
 \operatorname{Dom}\!\left(\bigoplus_u e_0^*\right)
 =
 \left\{(h_u):h_u\in\operatorname{Dom}e_0^*,\
 \sum_u(\|h_u\|_2^2+\|e_0^*h_u\|_2^2)<\infty\right\}.
 \tag{17}
\]
The one-coordinate tests force the marginal adjoint domains, and the boundedness of the full finite-support pairing is precisely square summability of their images.
This does not assume P is a core for \(E_0^*\).

The vector 1 is the vacuum coordinate \(u=1,b=1\).
By (11) and (17),
\[
 \xi=e_0^*1\in H_j.
 \tag{18}
\]
Restriction of the global actual vacuum identity to \(P_j\) now gives
\((\delta^{\mathrm m})^*(1\otimes1)=\xi\) on the marginal Hilbert space.
The marginal tensor-adjoint formula puts \(P_j\odot P_j\) in its actual adjoint domain.
In particular \(t_\ell=e_0^*|_{P_j}\), so (14), (17) give
\[
 T_\ell(a)=\sum_{u\in F}u t_\ell(b_u),\qquad
 \|T_\ell(a)\|_2^2=\sum_{u\in F}\|t_\ell(b_u)\|_2^2.
 \tag{19}
\]
No boundedness of the individual output vectors in M is required for this orthogonal expansion.

Let \(Q_j:H\to H_j\) be the orthogonal projection, extending \(\mathbb E_j\).
The vacuum coordinate of (17) gives, for every \(p\in P\),
\[
 Q_jT_\ell(p)=t_\ell(\mathbb E_jp).
 \tag{20}
\]
Here \(\mathbb E_jp\in P_j\), so the right side is in its original marginal adjoint domain.

### 3. Left modules and the right estimate

Let \(\mathcal W=\{u^*:u\in\mathcal U\}\).
Taking tracial adjoints in (12)--(14) gives the unitary left-module decomposition
\[
 W:H_j\otimes_2\ell^2(\mathcal W)\longrightarrow H,\qquad
 W(b\otimes e_w)=bw,
\]
and the finite full-core expansion
\[
 a=\sum_{w\in G}c_w w,\quad c_w\in P_j,\qquad
 \mathbb E_j(aa^*)=\sum_{w\in G}c_wc_w^*.
 \tag{21}
\]
In particular \(\mathbb E_j(wv^*)=\delta_{wv}1\).
Every nonempty w starts outside j.

Set \(f_0=(\tau\otimes\mathrm{id})\delta^{\mathrm m}\).
When differentiating \(bw\), a cut in a j-factor of w has a nonempty reduced prefix c starting and ending outside j.
For each \(x\in H_j\), the first-leg trace \(\tau(bcx)\) vanishes, by traciality and \(\mathbb E_j(c)=0\), first on bounded x and then by L2 continuity.
This also annihilates completed Hilbert-tensor derivatives, by the same bounded multiplier and slice continuity as in Section 2.
Consequently
\[
 F_0(bw)=f_0(b)w,\qquad
 W^*F_0W=\bigoplus_w^{\mathrm{alg}} f_0.
\]
The single-coordinate and finite-support adjoint tests used in (17) therefore apply to \(F_0^*\) as well.
They give, with \(t_r=f_0^*|_{P_j}\),
\[
 T_r(a)=\sum_{w\in G}t_r(c_w)w,\quad
 \|T_r(a)\|_2^2=\sum_{w\in G}\|t_r(c_w)\|_2^2,\quad
 Q_jT_r(p)=t_r(\mathbb E_jp).
 \tag{22}
\]
Thus the right estimate uses exactly the left-module square \(aa^*\), not \(a^*a\).

### 4. Lifting the fixed vectors

Apply (2) to each coefficient in (14), sum the finite family, use linearity, and then use (15), (20):
\[
 \begin{split}
 \|T_\ell(a)\|_2^2
 &=\sum_u\|t_\ell(b_u)\|_2^2\\
 &\le\operatorname{Re}\left\langle
      t_\ell\!\left(\sum_u b_u^*b_u\right),g_\ell\right\rangle\\
 &=\operatorname{Re}\langle
      t_\ell(\mathbb E_j(a^*a)),g_\ell\rangle\\
 &=\operatorname{Re}\langle T_\ell(a^*a),g_\ell\rangle.
 \end{split}
 \tag{23}
\]
The last equality uses only \(g_\ell\in H_j\) and the orthogonal projection in (20).
Cauchy--Schwarz proves the final inequality in (3).
No adjoint is applied to \(g_\ell\).

The same calculation with (4), (21), (22) gives
\[
 \begin{split}
 \|T_r(a)\|_2^2
 &\le\operatorname{Re}\left\langle
       t_r\!\left(\sum_w c_wc_w^*\right),g_r\right\rangle\\
 &=\operatorname{Re}\langle T_r(aa^*),g_r\rangle.
 \end{split}
 \tag{24}
\]
This proves Part A with the original fixed vectors and their original norms.

### 5. Radial specialization, sharpness and canonical domains

If \(\mu_j\) is rotation invariant, the actual marginal A established in (18) satisfies the hypotheses of C_F0159.
In that Claim's notation the radius law has no atom at zero and
\[
 q_j(r)=
 \frac{\nu_j((0,r))+\nu_j((0,r])}{r}\in L^2(\nu_j),
 \qquad
 \xi_j(re^{i\theta})=e^{i\theta}q_j(r).
\]
Positive-radius atoms and an accumulation of radii at zero are permitted.
The strengthened scalar pairing estimate in C_F0159 supplies both marginal inequalities with \(g_\ell=g_r=\xi_j\).
Equations (23)--(24) give (6)--(7) on all mixed words.

Both constants are individually sharp.
The actual global adjoint gives \(T_\ell1=T_r1=\xi_j\).
Also
\(\langle\xi_j,X_j\rangle
=\langle1\otimes1,\delta_jX_j\rangle=1\), so \(\xi_j\ne0\).
Substituting \(a=1\) in either requested quadratic inequality forces its constant to be at least \(\|\xi_j\|_2\).

For clarity, the passage from the quadratic bounds to (8)--(9) uses only the already inspected power mechanism, not a new energy identity.
For either one-sided adjoint map T, the actual tensor-adjoint formula and the Leibniz rule give
\[
 \|T(a^m)\|_2
 \le\|a\|^m\|\xi_j\|_2+
      m\|a\|^{m-1}\|\delta_j(a^*)\|_2.
 \tag{25}
\]
Thus
\(\limsup_{m\to\infty}\|T(a^m)\|_2^{1/m}\le\|a\|\).
For the left inequality let \(b=a^*a\), and for the right let \(b=aa^*\).
Iterating the corresponding quadratic bound on \(b,b^2,b^4,\ldots\) gives
\[
 \|T(b)\|_2
 \le C^{1-2^{-n}}\|T(b^{2^n})\|_2^{2^{-n}},
 \qquad C=\|\xi_j\|_2>0.
\]
Use (25), let n tend to infinity, and apply the original quadratic bound once more to obtain
\[
 \|T_\ell(a)\|_2,\ \|T_r(a)\|_2\le\|\xi_j\|_2\|a\|.
 \tag{26}
\]
This is the Hilbert-valued power iteration checked in Mai15-U003.

Taking adjoints in the actual one-sided formulas gives
\[
 E_{j,0}(a)=a\xi_j^*-T_r(a^*)^*,\qquad
 F_{j,0}(a)=\xi_j^*a-T_\ell(a^*)^*.
\]
Equation (26) proves (8).
C_F0072 Part B now gives both actual domains in (9).
To check the stated generator commutator on all M, choose uniformly norm-bounded polynomial approximants to any \(a\in M\) converging in L2.
The two bounded slice estimates and closedness identify weak graph limits of both \(a_n\) and \(X_ka_n\).
Passing to the limit in
\[
 E_{j,0}(X_ka_n)-X_kE_{j,0}(a_n)=\delta_{jk}\tau(a_n)1
\]
gives the same equation on M.
For \(D_j^{\mathrm{can}}=-\overline{E_{j,0}}\), this is precisely the generator-first sign in (9).

## Review boundary and mathematical operation

The deduction was organized on 2026-10-16 from root's fixed-vector lifting outline and the accepted C_F0045 decomposition.
The new content is (23)--(24), its exact one-sided order, and the sharp mixed-word radial application.
Its Hilbert-tensor and actual-domain interfaces were checked by the drafting subagent, which participated in developing the proof and is not an independent reviewer.
A fresh review must check the fixed Claim in full, including the separate radial input or its independently adopted review.
Part A does not depend on the radial proof draft.
The Part B candidate currently inherits that input's pending independent-review status.

Existing scalar normal and free-product results already supplied S for this class.
The present candidate gives additional sharp quadratic information, including radial laws with Hilbert-unbounded marginal contractions.
It supplies no estimate for arbitrary correlated normal systems, no classification of the general A-to-F question and no Task completion.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-16T03:16 |
| status | open |
| reason | Fix the complete normal free-product lifting proof and the sharp radial candidate application for fresh independent review; the radial input C_F0159 remains separately pending review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Parts A and B, actual marginal/global adjoints, fixed-vector lifting on the full mixed core, sharp radial constants and canonical-domain consequence. |
| argument | [Argument](#argument) | All five sections, including finite core decompositions, completed-tensor cut cancellation, exact actual adjoint direct sums, both conditional-expectation square orders, lifting, sharpness and the power/domain chain. |
| dependency | [Normal phase and actual tensor-adjoint domains](Yin_C_F0076_v1.md#statement) | Part 1 only, for diffuse scalar marginals, zero derivatives of all other starred factors and the actual core adjoint domains. |
| dependency | [Free-product module and actual adjoint mechanism](Yin_C_F0045_v1.md#3-an-orthogonal-right-module-decomposition-of-the-full-core) | Sections 3--5 only; the current proof checks their actual-A applicability and opposite-side version, without using the later little Grothendieck estimate. |
| dependency | [Radial fixed-vector candidate](Yin_C_F0159_v1.md#statement) | Part B only: the scalar strengthened pairing inequality with g equal to the actual vacuum; this separately registered proof draft awaits review. |
| dependency | [Inspected power iteration](../audits/literature/Mai15/Yin_U002.md#mai15-u002) | Hilbert-valued Lemma 4.11 mechanism only, after the present quadratic bounds and direct power growth have been established. |
| dependency | [Both original canonical domains](Yin_C_F0072_v1.md#statement) | Part B supplies actual closure and adjoint domains from the two slice bounds; the commutator passage and generator-first sign are checked above. |

### Decision reviewed-quadratic

| Field | Value |
| --- | --- |
| date | 2026-10-16T03:31 |
| status | proved |
| reason | Adopt the entire fixed statement and argument after its separate whole-proof review, with all declared direct inputs resolved at the retained scopes. This result does not settle the unrestricted normal A-to-S question. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire fixed statement and its explicit positive or negative scope. |
| argument | [Argument](#argument) | Complete fixed argument, original-domain assertions and direct-input applications. |
| dependency | [Normal phase and actual tensor-adjoint domains](Yin_C_F0076_v1.md#statement) | Part 1 only, for diffuse scalar marginals, zero derivatives of all other starred factors and the actual core adjoint domains. |
| dependency | [Free-product module and actual adjoint mechanism](Yin_C_F0045_v1.md#3-an-orthogonal-right-module-decomposition-of-the-full-core) | Sections 3--5 only; the current proof checks their actual-A applicability and opposite-side version, without using the later little Grothendieck estimate. |
| dependency | [Radial fixed-vector estimate](Yin_C_F0159_v1.md#statement) | Part B only: the scalar strengthened pairing inequality with g equal to the actual vacuum; the exact input was independently reviewed in R_F0166 and adopted by C_F0159 decision-reviewed-quadratic. |
| dependency | [Inspected power iteration](../audits/literature/Mai15/Yin_U002.md#mai15-u002) | Hilbert-valued Lemma 4.11 mechanism only, after the present quadratic bounds and direct power growth have been established. |
| dependency | [Both original canonical domains](Yin_C_F0072_v1.md#statement) | Part B supplies actual closure and adjoint domains from the two slice bounds; the commutator passage and generator-first sign are checked above. |
| review | [Independent whole-proof review](../audits/reviews/Yin_R_F0169_v1.md#conclusion) | Entire statement and argument with the exact direct dependencies and limits in the review bindings. |


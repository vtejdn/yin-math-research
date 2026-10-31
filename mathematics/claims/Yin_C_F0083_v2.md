---
author: Yin
---

# Liberation gradients and dual systems: normal equivalence and a nonnormal obstruction

## Current assessment
[Selected decision](#decision-whole-self-reviewed)

## Scope and provenance

The human requested fixed retention of the comparison among liberation dual systems, liberation gradients and liberation conjugate variables.
The forward implication from finite liberation Fisher information is already fixed in [C_F0082](Yin_C_F0082_v1.md#decision-self-reviewed).
This material supplies the normal converse, its actual adjoint formula, the resulting equivalence, and a nonnormal counterexample.
It also fixes the terminology and sign conversions needed to distinguish these assertions from ordinary conjugate variables and bounded selfadjoint dual systems.
The circular Fock model is reused from [C_F0074](Yin_C_F0074_v1.md#1-standard-free-fock-model-and-the-bounded-dual); the two-coordinate liberation obstruction below is a separate deduction from that model.
No priority or literature-wide novelty claim is made.

## Definitions and conventions

Let \((M,\tau)\) be a finite von Neumann algebra with faithful normal tracial state, \(H=L^2(M,\tau)\), \(\Omega=1\), and \(P_\Omega\) the projection onto \(\mathbb C\Omega\).
Use \(\langle u,v\rangle=\tau(v^*u)\), linear in the first variable.
Write \(J(x\Omega)=x^*\Omega\), extended antiunitarily to \(H\).
Elements of \(M\) act on the left, and \(\rho(x)(y\Omega)=yx\Omega\) is bounded right multiplication.

For \(X=(X_1,\ldots,X_d)\in M^d\), \(d\geq1\), set
\[
 A_i=W^*(X_i),\qquad B_i=W^*(X_j:j\ne i),\qquad
 N=W^*(X_1,\ldots,X_d),\qquad
 \mathcal P_i=\operatorname{Alg}(A_i,B_i).
 \tag{1}
\]
The empty generated algebra is \(\mathbb C1\).
Let \(H_N=L^2(N,\tau)\subset H\), and let \(e_N:H\to H_N\) be the orthogonal projection.
The subspace \(H_N\) is \(J\)-invariant, so \(e_NJ=Je_N\).

The adopted [liberation dual-system domain variant](Yin_C_F0079_v4.md#liberation-dual-system) requires densely defined operators \(L_i\) such that
\[
 M\Omega\subseteq\operatorname{Dom}L_i\cap\operatorname{Dom}L_i^*,
 \qquad
 [X_j,L_i]\xi=\delta_{ij}[X_i,P_\Omega]\xi
 \quad(\xi\in M\Omega).
 \tag{2}
\]
The adjoints in (2) are actual Hilbert-space adjoints.
Sum normalization means \(\sum_iL_i=P_\Omega\) on \(M\Omega\), as in [C_F0082's definition](Yin_C_F0082_v1.md#sum-normalized-liberation-dual-system).
No boundedness or selfadjointness of the \(L_i\) is part of (2).

The [source liberation derivation and gradient](../audits/literature/Voi99/Yin_U003.md#liberation-derivation-and-gradient) use
\[
 \gamma_i(a)=a\otimes1-1\otimes a\quad(a\in A_i),\qquad
 \gamma_i(b)=0\quad(b\in B_i),
 \qquad
 \tau(j_i p)=(\tau\otimes\tau)(\gamma_i p).
 \tag{3}
\]
Tensor products are algebraic with outer bimodule actions.
A represented derivation must be well-defined on \(\mathcal P_i\); formal word formulas alone are insufficient when relations are present.
A gradient defined by word moments must satisfy the moment formula for every formal word, consistently with evaluation in \(N\).
This requirement also covers the relation-descent argument used in C_F0082.
The source first allows \(j_i\in L^1(N)\); finite liberation Fisher information requires \(j_i\in L^2(N)\).

<a id="liberation-conjugate-vectors"></a>
**Definition (conjugate vectors and sign convention).** For an actual \(\gamma_i:\mathcal P_i\Omega\subset H_N\to H_N\otimes_2H_N\), its \(L^2\) conjugate vector is
\[
 \xi_i=\gamma_i^*(1\otimes1),
 \qquad 1\otimes1\in\operatorname{Dom}\gamma_i^*.
 \tag{4}
\]
This record uses "liberation conjugate variable" as shorthand for the explicitly specified vector (4).
It does not attribute that phrase or a universal sign convention to the source, which calls \(j_i\) the liberation gradient.
For the anti-real derivation in (3), Voi99 Proposition 6.1 gives
\[
 j_i^*=-j_i,\qquad \xi_i=-j_i.
 \tag{5}
\]
Conversely, an actual vector (4) is skewadjoint by anti-reality, and \(-\xi_i\) satisfies the source gradient moments.
For the real derivation \(\delta_i=\mathrm i\gamma_i\), the actual vacuum-adjoint vector is instead
\[
 \eta_i=\delta_i^*(1\otimes1)=-\mathrm i\xi_i=\mathrm i j_i,
 \qquad \eta_i^*=\eta_i.
 \tag{6}
\]
Thus \(L^2\) existence is unchanged by these conventions, while the vectors and signs differ.

The [information convention](../audits/literature/Voi99/Yin_U004.md#liberation-fisher-information) is
\[
 \varphi^*(A_1;\ldots;A_d)=\sum_i\|j_i\|_2^2,
 \tag{7}
\]
with value \(+\infty\) when a required gradient is absent or not in \(L^2\).
The semicolon in (7) denotes the coordinate family relative to scalars; the always-zero quantity \(\varphi^*(N:\mathbb C)\) is a different condition.

## Statement

**Normal equivalence.** Suppose every \(X_j\) in (1) is normal.
Then the following existence conditions are equivalent:

1. Every coordinate liberation gradient \(j(A_i:B_i)\) exists in \(L^2(N)\), equivalently (7) is finite.
2. Every actual coordinate liberation derivation has the \(L^2\) conjugate vector (4).
3. There is a liberation dual system satisfying (2).
4. There is a normalized such system whose operators are closed.

In condition 2, well-definedness of the coordinate derivations on the represented algebra is included.
Conditions 1 and 2 use the definitions and signs above.
Neither \(N=M\), nonatomicity, nor regularity of every scalar shift is required.

For any system in condition 3, the actual conjugate vectors and gradients are
\[
 \boxed{\;
 \xi_i=e_N\bigl(JL_i\Omega-L_i^*\Omega\bigr),\qquad
 j_i=e_N\bigl(L_i^*\Omega-JL_i\Omega\bigr).
 \;}
 \tag{8}
\]
In particular,
\[
 \varphi^*(A_1;\ldots;A_d)
 \leq\sum_i\bigl(\|L_i\Omega\|_2+\|L_i^*\Omega\|_2\bigr)^2.
 \tag{9}
\]

**Nonnormal obstruction.** There is a two-coordinate tuple \(X=(c,c^*)\) in a finite tracial algebra that admits a bounded normalized system satisfying (2), with operator and adjoint domains equal to all of \(H\), but whose coordinate algebras have no liberation gradient even in \(L^1\).
Thus existence in (2) does not imply conditions 1 or 2 for arbitrary nonnormal tuples.

## Argument

### Normal commutation extends to the coordinate algebras

A useful general observation is that any closable linear operator \(T:M\Omega\to H\) is bounded when regarded as a map \(M_\infty\to H\).
Indeed, if \(z_n\to z\) in operator norm and \(T(z_n\Omega)\to v\) in \(H\), closedness of the Hilbert-space closure \(\overline T\) gives \(\overline T(z\Omega)=v\).
Since \(z\Omega\in\operatorname{Dom}T\), this is \(T(z\Omega)=v\).
The Banach closed graph theorem applies.
This does not give a bounded extension to all of \(H\).

If \(x\in M\) is normal and \(T(xz\Omega)=xT(z\Omega)\) for all \(z\in M\), the [bounded-map Fuglede consequence of CS77 Proposition 1](../audits/literature/CS77/Yin_U001.md#bounded-map-specialization) gives the same relation with \(x^*\).
Its application is to \(T\in\mathcal B(M_\infty,H)\), with the source's hermitian left-multiplication actions verified in that unit.
Products and linear combinations extend the relation to the unital star algebra generated by any such normal \(x\)'s.
For \(a\) in the generated von Neumann algebra, [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) supplies a uniformly bounded net \(a_\lambda\) from this star algebra converging strongly to \(a\).
For fixed \(z\in M\),
\[
 a_\lambda z\Omega\longrightarrow az\Omega,\qquad
 T(a_\lambda z\Omega)=a_\lambda T(z\Omega)\longrightarrow aT(z\Omega)
\]
in \(H\).
The closed graph of \(\overline T\), together with \(az\Omega\in M\Omega\), gives \(T(az\Omega)=aT(z\Omega)\).

Now restrict each \(L_i\) to \(M\Omega\).
Its adjoint has dense domain because \(M\Omega\subseteq\operatorname{Dom}L_i^*\), so this restriction is closable.
The bounded perturbation \(L_i-P_\Omega\) on \(M\Omega\) is closable as well.
Condition (2) says that \(L_i-P_\Omega\) commutes with \(X_i\), while \(L_i\) commutes with every \(X_j\) for \(j\ne i\).
Applying the preceding argument, using normality for every coordinate, yields
\[
 [a,L_i]=[a,P_\Omega]\quad(a\in A_i),\qquad
 [b,L_i]=0\quad(b\in B_i)
 \quad\text{on }M\Omega.
 \tag{10}
\]
The argument uses the actual Hilbert closure and bounded-map Fuglede theorem, rather than assuming a bounded Hilbert-space operator.

### The represented derivation and its actual vacuum adjoint

On bounded algebraic tensors define \(\Theta(a\otimes b)=aP_\Omega b\).
It is injective: \(\Theta(a\otimes b)=|a\Omega\rangle\langle b^*\Omega|\), and finite sums give the usual algebraic tensor identification with finite-rank operators.
The [tracial Hilbert-Schmidt realization](../audits/literature/Voi98/Yin_U005.md#conjugates-and-hilbert-schmidt-realization-510-512) records this source interface.

For fixed \(i\), let \(\mathfrak P_i=A_i*_{\mathbb C}B_i\) be the unital algebraic free product, let \(\pi_i:\mathfrak P_i\to\mathcal P_i\) be evaluation, and let \(\gamma_i^{\rm form}\) be the formal derivation specified by (3) on these two algebras.
For a free-product element \(w\), the Leibniz rule and (10) give
\[
 [\pi_i(w),L_i]
   =\Theta\bigl((\pi_i\otimes\pi_i)\gamma_i^{\rm form}(w)\bigr)
 \quad\text{on }M\Omega.
 \tag{11}
\]
All compositions on the left are defined, since left multiplication by \(M\) preserves \(M\Omega\).
The operator on the right is bounded and finite-rank.
If \(\pi_i(w)=0\), it vanishes on the dense space \(M\Omega\), hence is zero on \(H\).
Injectivity of \(\Theta\) gives \((\pi_i\otimes\pi_i)\gamma_i^{\rm form}(w)=0\).
Thus the coordinate derivation descends to the represented algebra, and (11) becomes
\[
 [p,L_i]=\Theta(\gamma_i p)\quad(p\in\mathcal P_i)
 \quad\text{on }M\Omega.
 \tag{12}
\]
Because both \(A_i\) and \(B_i\) are star algebras, this derivation is anti-real:
\(\gamma_i(p^*)=-(\gamma_i p)^\dagger\), where \((a\otimes b)^\dagger=b^*\otimes a^*\).

Set \(h_i=L_i\Omega\) and \(k_i=L_i^*\Omega\); both are actual \(H\)-vectors by (2).
Taking the vacuum pairing in (12) gives, for \(p\in\mathcal P_i\),
\[
 \begin{aligned}
 \langle\gamma_i p,1\otimes1\rangle
 &=\langle[p,L_i]\Omega,\Omega\rangle\\
 &=\langle p h_i,\Omega\rangle-\langle L_i(p\Omega),\Omega\rangle\\
 &=\langle p\Omega,Jh_i-k_i\rangle
  =\langle p\Omega,e_N(Jh_i-k_i)\rangle.
 \end{aligned}
 \tag{13}
\]
The first equality follows from \(\langle aP_\Omega b\Omega,\Omega\rangle=\tau(a)\tau(b)\).
The second term uses \(\Omega\in\operatorname{Dom}L_i^*\), tested against every \(p\Omega\) in the specified domain.
Thus the functional in (13) is bounded in \(\|p\|_2\), and the definition of the Hilbert-space adjoint proves
\[
 1\otimes1\in\operatorname{Dom}\gamma_i^*,\qquad
 \gamma_i^*(1\otimes1)=e_N(Jh_i-k_i).
 \tag{14}
\]
No closure extension or formal integration-by-parts symbol is substituted for this adjoint test.

For completeness, anti-reality gives
\(r(p^*)=-\overline{r(p)}\), where \(r(p)=(\tau\otimes\tau)(\gamma_i p)\).
Writing \(r(p)=\tau(\xi_i^*p)\), equation (14) and this identity imply \(\xi_i^*=-\xi_i\).
Then \(\tau((-\xi_i)p)=r(p)\), so \(j_i=-\xi_i\) is exactly the source gradient.
This proves (8), and the contraction property of \(e_N\) proves (9).
It establishes condition 3 implies conditions 1 and 2.

### Completion of the equivalence

Conditions 1 and 2 are equivalent by (4)--(6), with the actual represented derivations understood.
Condition 1 implies condition 4 by the exact selected result [C_F0082](Yin_C_F0082_v1.md#decision-self-reviewed), which already proves both bounded-vector domains, closed choices, sum normalization and extension to an ambient algebra.
Its hypotheses are satisfied by (1) and finite coordinate information; that forward argument does not require normality.
Condition 4 implies condition 3 directly.
The normal equivalence is therefore complete without reproducing the existing controlled-defect energy estimate.

### A bounded nonnormal counterexample

Use the [standard tracial Fock model](../audits/literature/Miy22/Yin_U001.md#miy22-u001)
\[
 \mathcal H=\mathbb C\Omega\oplus
       \bigoplus_{n\geq1}(\mathbb C^2)^{\otimes n}.
\]
For an orthonormal basis \(e_1,e_2\), let \(\ell_j\) and \(r_j\) be left and right creation, which prepend and append \(e_j\), respectively.
Their adjoints are the corresponding annihilation operators.
Set \(S_j=\ell_j+\ell_j^*\), \(M=W^*(S_1,S_2)\), and identify \(\mathcal H=L^2(M,\tau)\) using the faithful normal vacuum trace.
The \(S_j\) are centered variance-one free semicircular elements.
On words, right annihilation commutes with left annihilation, and its commutator with left creation is nonzero only on the vacuum, giving
\[
 [r_k^*,S_j]=\delta_{kj}P_\Omega.
 \tag{15}
\]

Put
\[
 c=(S_1+\mathrm iS_2)/\sqrt2,\qquad X_1=c,\quad X_2=c^*,
\]
and
\[
 D_1=-(r_1^*-\mathrm i r_2^*)/\sqrt2,\qquad
 D_2=-(r_1^*+\mathrm i r_2^*)/\sqrt2.
 \tag{16}
\]
These are bounded operators, and (15) gives
\[
 [X_j,D_i]=\delta_{ij}P_\Omega.
 \tag{17}
\]
For example the scalar coefficients for \([c,D_1]\) and \([c^*,D_1]\) are \((1+1)/2\) and \((1-1)/2\); the other two identities follow by exchanging the signs.
The tuple is nonnormal, since
\[
 (c^*c-cc^*)\Omega
    =\mathrm i[S_1,S_2]\Omega
    =\mathrm i(e_1\otimes e_2-e_2\otimes e_1)\ne0.
\]

All left and right multipliers commute, and traciality gives
\([\,\rho(x),P_\Omega\,]=[x,P_\Omega]\).
Define bounded operators
\[
 K_i=[\rho(X_i),D_i],\qquad
 R=K_1+K_2-P_\Omega,\qquad
 L_i=K_i-\tfrac12R.
 \tag{18}
\]
Jacobi's identity and (17) give
\[
 [X_j,K_i]
   =[\rho(X_i),[X_j,D_i]]
   =\delta_{ij}[X_i,P_\Omega].
\]
Consequently \([X_j,R]=0\), and the \(L_i\) satisfy (2) and \(L_1+L_2=P_\Omega\).
Every operator and adjoint in (18) has domain all of \(H\).
No selfadjointness of the \(L_i\) is asserted.

On the other hand,
\[
 S_1=(c+c^*)/\sqrt2,\qquad
 S_2=(c-c^*)/(\mathrm i\sqrt2)
\]
give \(A_1=W^*(c)=M=W^*(c^*)=A_2\).
The required gradient \(j(M:M)\) cannot satisfy the source word moments.
Indeed, let \(a=S_1\), so \(\tau(a)=0\) and \(\tau(a^2)=1\).
Treating \(a^2\) as an element of the first coordinate algebra gives
\[
 \tau(ja^2)=(\tau\otimes\tau)(a^2\otimes1-1\otimes a^2)=0.
\]
Treating the same represented product as \(a\) from the first algebra followed by \(a\) from the second gives
\[
 \tau(ja^2)=(\tau\otimes\tau)(a\otimes a-1\otimes a^2)=-1.
\]
These requirements contradict each other even for \(j\in L^1(M)\).
Thus no gradient exists, and \(\varphi^*(A_1;A_2)=+\infty\) by the convention (7).
This completes the counterexample, including its operator and adjoint domains.

## Comparison and limits

The source [bounded selfadjoint dual system](../audits/literature/Voi99/Yin_U001.md#bounded-liberation-dual-system) prescribes the relations (10) on entire coordinate algebras, with bounded selfadjoint operators.
Voi99 Proposition 13.3 then gives \(j=(T-JTJ)\Omega\) on the generated \(L^2\) space.
For such a \(T\), formula (8) reduces to the same expression, since \(T^*=T\) and \(J\Omega=\Omega\).
The normal equivalence above concerns (2); it does not prove that finite information always admits a bounded selfadjoint source system.
In the nonnormal example, the bounded \(L_i\) obey the generator relations but cannot obey the full algebra relations (10), which would imply the contradictory gradient moments.

Ordinary conjugate variables use a free difference quotient, with generator value \(1\otimes1\), rather than the liberation derivation in (3).
Their distinction from liberation dual systems is already fixed by the [arcsine counterexample C_F0080](Yin_C_F0080_v1.md#decision-accepted-counterexample).
For a single coordinate the liberation derivation against scalars is \(a\mapsto a\otimes1-1\otimes a\), whose trace pairing is zero, so the liberation gradient is zero independently of the marginal law.
In particular the absence of an ordinary conjugate variable in that example is consistent with the equivalence proved here.
This comparison does not identify ordinary Fisher information with liberation Fisher information.

This material assembles a project deduction from the accepted exact source interfaces and C_F0082.
It makes no claim that Voi99 or CS77 states the whole unbounded-domain equivalence verbatim.
Source proof-inspection limits remain those of the linked units; no full-source re-audit, formal verification or independent review is implied by this organization.

## Represented-domain clarification

On 2026-10-28T11:09, the proof was clarified to use the individual core \(\mathcal P_i=\operatorname{Alg}(A_i,B_i)\) for each coordinate, with its actual Hilbert adjoint.
For \(d\geq3\), the common algebra \(\operatorname{Alg}(A_1,\ldots,A_d)\) need not contain the von Neumann algebra \(B_i\).
The [initial v1 candidate](Yin_C_F0083_v1.md#decision-initial) is retained with its open assessment; its use of that common core is not adopted as a full \(A_i:B_i\) argument.
The corrected proof first establishes the relations on all of \(A_i\) and \(B_i\), descends the formal derivation from \(A_i*_{\mathbb C}B_i\), and tests its adjoint on every element of \(\mathcal P_i\).
The normal equivalence and nonnormal counterexample retain their intended scope.
No earlier review is extended to this corrected proof.

## Assessment history

### Decision domain-corrected

| Field | Value |
| --- | --- |
| date | 2026-10-28T11:09 |
| status | open |
| reason | Retain the corrected individual cores Alg(A_i,B_i) and the full algebra-level adjoint test for the same normal-equivalence and nonnormal-boundary comparison, pending its recorded whole-proof self-review. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The normal equivalence of finite information, actual liberation conjugate vectors and bounded-vector dual systems, the vacuum formulas, and a bounded nonnormal counterexample. |
| argument | [Argument](#argument) | Normal algebra-level extension, represented relation descent, actual adjoint test, reuse of the forward theorem, and complete Fock counterexample. |
| dependency | [Existing forward result](Yin_C_F0082_v1.md#decision-self-reviewed) | Finite coordinate information gives closed normalized duals with both bounded-vector domains in any ambient algebra; the retained self-reviewed scope is used unchanged. |
| dependency | [Bounded-map Fuglede input](../audits/literature/CS77/Yin_U001.md#cs77-u001) | The checked M-infinity-to-H specialization of Proposition 1 extends normal intertwining to adjoints; it does not presume an H-bounded operator. |
| dependency | [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Uniformly bounded strong approximation inside each generated coordinate algebra, at the retained statement-and-applicability inspection depth. |
| dependency | [Gradient and signed vacuum](../audits/literature/Voi99/Yin_U003.md#voi99-u003) | Sections 5.3--5.4 and Proposition 6.1: represented derivation, word moments, skewadjointness and the signed L2 vacuum interface. |
| dependency | [Information convention](../audits/literature/Voi99/Yin_U004.md#voi99-u004) | Definition 9.1 for a finite coordinate family relative to scalars, with infinite value for absent or non-L2 gradients. |
| dependency | [Tensor realization](../audits/literature/Voi98/Yin_U005.md#voi98-u005) | Only the tracial rank-one/Hilbert-Schmidt tensor identification used for injectivity and relation descent. |
| dependency | [Tracial Fock input](../audits/literature/Miy22/Yin_U001.md#miy22-u001) | Full Fock creation/deletion actions, faithful normal vacuum trace, L2 identification and variance-one semicircular normalization; original textbook proofs retain their source limits. |
| support | [Bounded source comparison](../audits/literature/Voi99/Yin_U001.md#voi99-u001) | Definition 13.1 and Proposition 13.3 are compared only at their bounded selfadjoint algebra-level scope. |
| support | [Ordinary conjugate-variable comparison](Yin_C_F0080_v1.md#decision-accepted-counterexample) | The accepted arcsine example separates ordinary conjugate variables from liberation duals; it is consistent with the zero one-coordinate liberation gradient. |

### Decision whole-self-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-28T11:13 |
| status | proved |
| reason | Adopt the complete v2 comparison after the recorded whole-proof authoring-agent self-review, with the individual represented cores Alg(A_i,B_i), actual adjoint formula, normal equivalence, bounded nonnormal counterexample and source-definition limits explicit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | The normal equivalence of finite information, actual liberation conjugate vectors and bounded-vector dual systems, the vacuum formulas, and a bounded nonnormal counterexample. |
| argument | [Argument](#argument) | Normal algebra-level extension, represented relation descent, actual adjoint test, reuse of the forward theorem, and complete Fock counterexample. |
| dependency | [Existing forward result](Yin_C_F0082_v1.md#decision-self-reviewed) | Finite coordinate information gives closed normalized duals with both bounded-vector domains in any ambient algebra; the retained self-reviewed scope is used unchanged. |
| dependency | [Bounded-map Fuglede input](../audits/literature/CS77/Yin_U001.md#cs77-u001) | The checked M-infinity-to-H specialization of Proposition 1 extends normal intertwining to adjoints; it does not presume an H-bounded operator. |
| dependency | [Kaplansky density](../audits/literature/AP18/Yin_U001.md#ap18-u001) | Uniformly bounded strong approximation inside each generated coordinate algebra, at the retained statement-and-applicability inspection depth. |
| dependency | [Gradient and signed vacuum](../audits/literature/Voi99/Yin_U003.md#voi99-u003) | Sections 5.3--5.4 and Proposition 6.1: represented derivation, word moments, skewadjointness and the signed L2 vacuum interface. |
| dependency | [Information convention](../audits/literature/Voi99/Yin_U004.md#voi99-u004) | Definition 9.1 for a finite coordinate family relative to scalars, with infinite value for absent or non-L2 gradients. |
| dependency | [Tensor realization](../audits/literature/Voi98/Yin_U005.md#voi98-u005) | Only the tracial rank-one/Hilbert-Schmidt tensor identification used for injectivity and relation descent. |
| dependency | [Tracial Fock input](../audits/literature/Miy22/Yin_U001.md#miy22-u001) | Full Fock creation/deletion actions, faithful normal vacuum trace, L2 identification and variance-one semicircular normalization; original textbook proofs retain their source limits. |
| support | [Bounded source comparison](../audits/literature/Voi99/Yin_U001.md#voi99-u001) | Definition 13.1 and Proposition 13.3 are compared only at their bounded selfadjoint algebra-level scope. |
| support | [Ordinary conjugate-variable comparison](Yin_C_F0080_v1.md#decision-accepted-counterexample) | The accepted arcsine example separates ordinary conjugate variables from liberation duals; it is consistent with the zero one-coordinate liberation gradient. |
| review | [Whole comparison self-review](../audits/reviews/Yin_R_F0081_v1.md#whole-comparison) | Complete v2 statement, conventions, proof, accepted input interfaces and counterexample, with the explicit self-reviewed relationship; no independent inspection or bounded selfadjoint converse is claimed. |


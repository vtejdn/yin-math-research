---
author: Yin
---
# Kernel weights in the selfadjoint contraction estimate

Human author Yin.
Root derived the weighted energy identity under [T_F0011](../tasks/Yin_T_F0011_v1.md#contract); the general-tuple branch agent separately checked its tensor order and analytic-unitary passage during preparation.
This is a project deduction from the real coassociative calculation in Dab10, not an assertion that the weighted statement is printed there.
A separately organized fixed-material review is required before adoption.

## Current assessment
[Selected decision](#decision-reviewed)

## Statement

Let (M,tau) be finite with a faithful normal probability trace, H=L2(M,tau), and let Z=(Z_1,...,Z_d) be bounded selfadjoint generators having joint conjugate variables in H.
Put A=C<Z_1,...,Z_d>.
Fix i and write
\[
 \delta=\partial_i,\qquad \xi=\partial_i^*(1\otimes1)=\xi^*,
 \qquad E_0=(\mathrm{id}\otimes\tau)\delta:A\longrightarrow A.
\]
The derivation has its usual represented algebraic tensor values and outer bimodule actions.
Inner products are linear in the second variable.

Let B be a unital star subalgebra of A with delta(B)=0, and put N=W*(B).
Let b be a positive affiliated operator of N such that
\[
 b\in L^2(N),\qquad \xi b\in L^2(M).
 \tag{1}
\]
The second condition is an actual measurable-product L2 condition, equivalently membership of xi in the domain of the closed right multiplier rho(b).
Since b and xi are selfadjoint, it is equivalent to b xi in L2 and their L2 norms agree.

Then, for every p in A,
\[
 \boxed{\|(E_0p)b\|_2\le4\|\xi b\|_2\|p\|.}
 \tag{2}
\]
The product on the left is defined because E_0p is bounded and b is L2.
No freeness between N and the distinguished coordinate is assumed.
In particular, if xi is bounded then the constant in (2) is at most 4||xi|| ||b||2.

For a bounded selfadjoint c in B and for an analytic-core unitary u obtained from a selfadjoint strict contraction in A by \(u=a+\mathrm i(1-a^2)^{1/2}\), the sharper intermediate estimate is
\[
 \|(E u)c\|_2\le2\|\xi c\|_2.
 \tag{3}
\]
Here E is the specified Hilbert closure of E_0 and the analytic approximation below verifies its actual value at u.

This is an output-weight estimate.
It does not by itself identify complete product domains, give all bounded vectors in the adjoint domain of a weighted contraction, or establish a general nonnormal ACSY-to-full-domain implication.

## Argument

### 1. Exact accepted inputs and core identities

[Dab10-U002 Sections 1-3](../audits/literature/Dab10/Yin_U002.md#dab10-u002) supplies the represented selfadjoint difference quotient, its actual vacuum, reality, closability, and the actual core adjoint formula
\[
 E_0^*q=q\xi-E_0q,\qquad q\in A.
 \tag{4}
\]
The input assumptions match exactly: bounded selfadjoint generators, joint L2 conjugates, faithful finite trace and the right contraction.
No bounded-H extension of E_0 or bounded conjugate variable is assumed.

The free difference quotient is algebraically coassociative:
\[
 (\delta\otimes\mathrm{id})\delta
 =(\mathrm{id}\otimes\delta)\delta .
\]
Indeed the difference obeys the outer derivation rule into the triple tensor algebra (its two mixed product terms cancel) and vanishes on all selfadjoint generators.
Applying id tensor id tensor tau gives
\[
 \delta(E_0p)=(\mathrm{id}\otimes E_0)\delta p,\qquad p\in A.
 \tag{5}
\]
All quantities in (4)-(5) have their original algebraic-core domains.
This is the same coassociative energy mechanism used in the inspected Dab10 calculation; the additional kernel weight is handled explicitly below.

### 2. The weighted core energy identity

Fix c=c* in B, so delta(c)=0 and E_0(c squared)=0.
For v in A, (4) and traciality give
\[
 \tau((E_0v)c^2)
 =\langle c^2,E_0v\rangle
 =\langle c^2\xi,v\rangle
 =\tau(v\xi c^2).
 \tag{6}
\]
Writing delta p=sum u tensor v, the product rule and (5)-(6) yield
\[
 E_0((E_0p)c^2)
 =(\mathrm{id}\otimes\tau)\bigl((\delta p)(1\otimes\xi c^2)\bigr).
 \tag{7}
\]
The second factor xi c squared is L2, so this finite-tensor contraction is legitimate even when xi is unbounded.
The left side belongs to A and is an actual second core application.

Set
\[
 T=\tau((E_0p)^*p\xi c^2),\qquad
 Q=(\tau\otimes\tau)\bigl(\delta(p^*p)(1\otimes\xi c^2)\bigr).
\]
Adjoint pairing at the core vector (E_0p)c squared gives
\[
 \begin{aligned}
 \|(E_0p)c\|_2^2
 &=\tau\bigl(p^*E_0^*((E_0p)c^2)\bigr)\\
 &=\tau(p^*(E_0p)c^2\xi)
   -(\tau\otimes\tau)\bigl((p^*\otimes1)\delta p
                          (1\otimes\xi c^2)\bigr).
 \end{aligned}
 \tag{8}
\]
Because c and xi are selfadjoint and the trace is cyclic, the first term in the last line is conjugate(T), with no commutation between c and xi asserted.
Reality, delta(p*)=(delta p) dagger, gives
\[
 (\tau\otimes\tau)\bigl(\delta(p^*)(1\otimes p\xi c^2)\bigr)
 =\tau((E_0p)^*p\xi c^2)=T.
\]
The Leibniz rule therefore identifies the second term in (8) as Q-T.
Consequently
\[
 \boxed{\|(E_0p)c\|_2^2
 =2\operatorname{Re}\tau((E_0p)^*p\xi c^2)
  -(\tau\otimes\tau)\bigl(\delta(p^*p)(1\otimes\xi c^2)\bigr).}
 \tag{9}
\]
All trace products are in L1: bounded polynomial coefficients multiply the L2 vector xi and bounded c.
Formula (9), rather than an unproved second-operator domain assertion at a limiting unitary, is used in the next step.

### 3. Analytic unitaries and the operator-norm estimate

Let a=a* in A with ||a||<1 and let \(u=a+\mathrm i(1-a^2)^{1/2}\).
The binomial series supplies core polynomials p_n converging to u in operator norm.
Their derivatives and the derivatives of their adjoints converge in the coarse Hilbert norm.
Indeed
\[
 \|\delta(a^m)\|_2\le m\|a\|^{m-1}\|\delta a\|_2,
\]
and the differentiated power series is absolutely summable at ||a||<1.
The same argument applies to the conjugate series.
Multiplication by the uniformly bounded p_n then shows
\[
 \delta(p_n^*p_n)\longrightarrow0
 \quad\hbox{in }H\otimes_2H.
 \tag{10}
\]
One can verify its zero limit directly by multiplying the two absolutely convergent differentiated series for u* u=1; no unspecified functional-calculus core theorem is used.

The bounded contraction id tensor tau implies that E_0p_n converges in H.
Since E_0 is closable, u belongs to Dom E and this limit is Eu.
Because c is bounded, the left side of (9) converges to ||(Eu)c||2 squared.
The first trace term converges by the operator-norm convergence of p_n and L2 convergence of E_0p_n.
The last term tends to zero by (10), pairing against the fixed Hilbert tensor 1 tensor c squared xi, or equivalently using the displayed trace convention with xi c squared.

Thus
\[
 \|(Eu)c\|_2^2
 =2\operatorname{Re}\tau((Eu)^*u\xi c^2)
 =2\operatorname{Re}\langle(Eu)c,u\xi c\rangle
 \le2\|(Eu)c\|_2\|\xi c\|_2.
 \tag{11}
\]
The equality between the trace and inner-product expressions uses cyclicity, not commutation.
Since u is unitary, left multiplication by u preserves the L2 norm of xi c.
This proves (3), including the case of zero norm.
Apply the identical argument to u*.

Now a=(u+u*)/2, so linearity on the actual closure domain gives \(\|(E_0a)c\|_2\le2\|\xi c\|_2\).
For arbitrary selfadjoint a, apply this to a/(||a||+epsilon) and let epsilon decrease to zero.
Writing p as its real part plus i times its imaginary part, each of norm at most ||p||, gives
\[
 \|(E_0p)c\|_2\le4\|\xi c\|_2\|p\|,
 \qquad p\in A,\quad c=c^*\in B .
 \tag{12}
\]

### 4. Bounded kernel algebra and affiliated weights

For c=c* in N bounded, Kaplansky density and norm approximation in C*(B) give selfadjoint c_alpha in B, uniformly bounded in operator norm, converging to c strongly-star and in L2.
For fixed p, E_0p is bounded, so (E_0p)c_alpha converges to (E_0p)c in H.
Also xi c_alpha converges to xi c in H: approximate xi in L2 by a bounded vector, use the uniform multiplier bound on the error, and use L2 convergence for the bounded part.
Thus (12) passes to every bounded selfadjoint c in N.
No action of delta on arbitrary c in N is assumed in this passage.

For b as in (1), take its bounded positive spectral cuts
\[
 b_n=b\,1_{\{b\le n\}}\in N.
\]
Then b_n tends to b in L2.
The actual domain condition xi b in L2 gives xi b_n tending to xi b in L2 by spectral calculus of the closed right multiplier rho(b).
Since E_0p is bounded, (E_0p)b_n tends to (E_0p)b in L2 as well.
Passing to the limit in (12) proves (2).

When xi belongs to M, the final condition in (1) holds for every b in L2(N), with ||xi b||2<=||xi|| ||b||2.
This gives the stated corollary, still without any freeness assumption.

## Reuse and limitations

The local search and inspected source identify Dab10's real coassociative energy calculation and [C_F0043 Section 3.2](Yin_C_F0043_v1.md#32-analytic-unitaries-give-a-uniform-bound) as the relevant analytic-unitary mechanism.
The argument above reconstructs the required first-derivative series passage and keeps the weight in its correct tensor leg.
C_F0043's unitary-generator theorem is not an additional premise.
No exact external theorem with the present affiliated kernel-weight statement was verified, and no novelty or priority claim is made.

The weight lies in the von Neumann algebra generated by a delta-zero star algebra.
A weight from the differentiated coordinate need not satisfy (6)-(7).
In particular this argument does not control the curvature weight in the unresolved normal mixed-defect problem.
Nor does a right-output estimate alone give both domains for an arbitrary nonreal contraction.

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `self-reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T17:29 |
| status | open |
| reason | Complete kernel-weight energy proof retained; tensor order and analytic-unitary passage received a preparation cross-check, but separate whole-proof review is pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Affiliated positive kernel weights, the weighted output estimate and analytic-unitary intermediate bound, with all integrability and domain limits. |
| argument | [Argument](#argument) | Four sections: real core adjoint/coassociativity, weighted trace identity, actual analytic-unitary limit and bounded/affiliated weight passage. |
| dependency | [Dab10-U002](../audits/literature/Dab10/Yin_U002.md#dab10-u002) | Represented selfadjoint difference quotient, reality, actual vacuum and core contraction adjoint/closability; no weighted estimate imported. |

### Decision reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-14T17:41 |
| status | proved |
| reason | Complete independent review verified the kernel-weight energy identity, analytic-unitary passage and actual affiliated weight domains; no general nonnormal or complete weighted-adjoint conclusion is selected. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Affiliated positive kernel weights, the weighted output estimate and analytic-unitary intermediate bound, with all integrability and domain limits. |
| argument | [Argument](#argument) | Four sections: real core adjoint/coassociativity, weighted trace identity, actual analytic-unitary limit and bounded/affiliated weight passage. |
| dependency | [Dab10-U002](../audits/literature/Dab10/Yin_U002.md#dab10-u002) | Represented selfadjoint difference quotient, reality, actual vacuum and core contraction adjoint/closability; no weighted estimate imported. |
| review | [Independent complete review](../audits/reviews/Yin_R_F0143_v1.md#conclusion) | Complete fixed statement and argument, all selected direct inputs and actual scope limits. |


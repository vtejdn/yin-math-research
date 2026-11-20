# Current writing opinions

## Title and abstract

Consider the title *Rationality of affiliated operators via finite-rank commutators*.
In the abstract, describe the algebraic criterion by the existence of finite-rank solutions to the commutator equation.
For the analytic criteria, state the range condition for the closed fraction commutators of a liberation dual system and the finite-rank condition for the fraction commutators of a dual system.
State regularity of the scalar shifts for the liberation result and retain the normal-generator and dual-system assumptions for the third result.
Use “rationality criteria” in the keywords to match the subject of the paper.
See [the title, keywords and abstract](main.tex).

## The transition between the criteria

Introduce \(X=(X_1,\ldots,X_d)\) before using \(\Delta(X)=d\) in the opening paragraph.
Before Definition 1.6, qualify the assertion about solvability for every fraction pair by the hypotheses of Theorem 1.7.
In the illustration following Theorem 1.7, replace “using the normalization in equation (7)” with “using equation (7)”.
See the [introduction](sections/introduction.tex).

## The algebraic proof

In the proof of Lemma 2.2, state that the coefficients of the dependence relation for \(1,u\) belong to \(F\), since the argument inverts the nonzero second coefficient in \(F\).
In Lemma 3.1, consider writing \(k_i=\sum_r u_{ir}\otimes v_{ir}^{\mathrm{op}}\) and applying Lemma 2.5 to the two finite families of factors.
This shows directly that the same pair \(s,t\) clears all the tensors.
In the implication \((5)\Rightarrow(1)\) of Theorem 1.4, describe \(\pi\) as \(\Theta^{-1}\) followed by the map induced by the bilinear map \((v_1,v_2)\mapsto v_1\otimes_F v_2\).
Use equation (14) for the resulting rank-one calculation and invoke linearity for the finite-rank conclusion.
See the [preliminaries](sections/preliminaries.tex) and [proof of Theorem 1.4](sections/maximal-delta.tex).

## The hypotheses and transitions in the liberation proof

Before Proposition 4.7, include regularity of every \(X_i-\lambda\) when stating that a liberation dual system yields maximal \(\Delta\).
Replace “We records two technical lemmas” with “The next two lemmas recover tensors in \(H\otimes_{\mathbb C}H\) and establish closability of the fraction commutators.”
See the [liberation dual system section](sections/liberation-dual-system-criterion.tex).

## The second quotient and the equality of closures

In Lemma 4.6, consider specifying that the second quotient uses \(R_x|_H\) and \(\widetilde R_{x^{\mathrm{op}}}\) on \(H\otimes_{\mathbb C}(U^{\mathrm{op}}/H)\).
The absence of nonzero finite-dimensional invariant subspaces for \(R_x|_H\) gives the needed injectivity, and the second identity of Lemma 4.5 gives the kernel.
In the proof of Theorem 1.7, after applying Lemma 4.9, explain why the two closures agree.
The closure of \(\Gamma[Q,L_i]\) extends the bounded operator \(-\overline{m_{L_i}(\ell_0)}\), which already has domain \(H\).
See the [liberation dual system section](sections/liberation-dual-system-criterion.tex).

## The trace argument in Remark 5.1

Consider adding one sentence identifying the domain adjustment in the application of MSY23 Proposition 6.2.
Choose a common regular \(r\in\mathcal M\) so that each \(\rho(r)T_i\) in the resulting cycle has range in \(\mathcal M\Omega\) before applying the trace argument.
See [Remark 5.1](sections/dual-system-criterion.tex) and the [supporting proof](../../../../claims/Yin_C_F0024_v1.md#3-maximal-delta-from-dual-identities-on-all-bounded-vectors).

## The operator calculations in Section 5

In Lemma 5.3, replace “Let us fix ... and we evaluate” with two sentences fixing \(i\) and \(\xi\in\mathcal M\Omega\), then applying \(\ell\mapsto m_{D_i}(\ell)\xi\) to both sides of equation (24).
In Proposition 5.6, identify \(X_j\) and \(\rho(X_i)\) as left and right multipliers, respectively, and cite equation (9) when inserting the dual-system relations.
After the displayed identity for \([X_j,C]\), declare \(a\in\mathcal M\) and state \(P_\Omega(a\Omega)=\tau(a)\Omega\) before the two product calculations.
Name traciality as the reason for \(\tau(aX_j)=\tau(X_j a)\).
Before Lemma 5.7, say that it compares the given dual system with any normalized liberation dual system on \(\mathcal M\Omega\).
In equation (28), identify commutation of \(\rho(X_i)\) with the left multipliers \(s,a,b,t\) as the justification for regrouping the terms.
See [Section 5](sections/dual-system-criterion.tex).

## The conclusion of the circular example

In Remark 6.2, replace the claim that the “description (3) ... still holds” with the applicability of Theorem 1.7 and the conclusion for \(u=c^*\).
Write “The circular generator \(c\) satisfies the hypotheses of Theorem 1.7.”
Then state “For \(u=c^*\), the commutator equation in assertion (3) has no finite-rank solution for any fraction pair.”
See the [circular example](sections/examples.tex).

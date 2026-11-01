---
author: Yin
---

# q-Rational Coefficients: Controlled Recursion and Reconstruction

Registration checkpoint, 2026-09-11: after [independent review](../audits/reviews/Yin_R_F0109_v1.md#original-f0059-account), the original Section 4 is retained as ordinary [Claim Yin_C_F0097](../claims/Yin_C_F0097_v1.md#one-state-energy-obstruction), and Sections 5-6 as the two sufficient cases of ordinary [Claim Yin_C_F0098](../claims/Yin_C_F0098_v1.md#weighted-recognizable-reconstruction).
No mathematical Role is assigned.
Candidate-stage wording below is preserved at its original mathematical scope; the responsible Claim materials and their selected decisions own current assessments.
The later [general recognizable actual-q theorem](../claims/Yin_C_F0101_v1.md#statement) supersedes the unrestricted recognizable-series gap below, while the [raw Wick obstruction](../claims/Yin_C_F0103_v1.md#statement) retains the separate rational-evaluation boundary.
The accepted external norm input is [KM26-U001](../audits/literature/KM26/Yin_U001.md#km26-u001); the comparison source is Miy23.

<a id="q-rational-research-2026-09-11"></a>

Date: 2026-09-11.
Record kind: bounded exploration and proof drafts.
Author: another AI agent, reassigned by the coordinating agent to the q branch of Yin_T_F0006.

At the original authoring stage, these calculations were unregistered proof drafts and a proposed research handoff, pending independent review and root integration.
No Claim ID, lemma/theorem Role, novelty assertion, or promotion of an existing Claim is made here.

## 1. Separate targets and existing inputs

For the canonical selfadjoint q-Gaussian tuple X, finite dimension and -1<q<1, the two targets remain distinct:

\[
\operatorname{Div}_{L^0(\mathcal M)}\mathbb C\langle X\rangle
\cap L^2(\mathcal M)\subseteq\mathcal M,
\tag{Q5}
\]
\[
\operatorname{Div}_{L^0(\mathcal M)}\mathbb C\langle X\rangle
\cap\mathcal M
=\operatorname{Div}_{\mathcal M}\mathbb C\langle X\rangle.
\tag{Q6}
\]

The [existing q route](../strategies/Yin_S_F0008.md#s_f0008), [Yin_C_F0020](../claims/Yin_C_F0020_v1.md#yin_c_f0020), [Yin_C_F0023](../claims/Yin_C_F0023_v1.md#yin_c_f0023), [MS23 source index](../audits/literature/MS23/readme.md), [Yin_C_F0015](../claims/Yin_C_F0015_v1.md#yin_c_f0015), and [Yin_C_F0017](../claims/Yin_C_F0017_v1.md#yin_c_f0017) were consulted before the new calculation.

Yin_C_F0023 already supplies bounded normalized duals throughout this parameter interval.
Yin_C_F0020 already settles both targets for real one-dimensional marginals.
Yin_C_F0015 requires recognizability in an orthonormal coefficient system; Yin_C_F0017 obtains scalar bounded reconstruction by controlling every entry in a minimal holomorphic realization.
Neither result permits treating the raw q-word tensors as orthonormal.

## 2. Selected primary inputs

The new selected input is Todd Kemp and Akihiro Miyagawa, *The strong Haagerup inequality for q-circular systems*, [arXiv:2409.03177v2](https://arxiv.org/html/2409.03177v2).
Theorem 1.2 states, for the canonical q-circular system c=(c_1,...,c_d),

\[
\left\|\sum_{|w|=n}\alpha_w c_w\right\|
\le A(|q|)\sqrt{n+1}
\left\|\sum_{|w|=n}\alpha_w c_w\right\|_2.
\tag{2.1}
\]

The statement, q-Fock setup in Section 2, and Lemma 2.3 were checked.
The source proof of Theorem 1.2 was not audited.
The estimate is accepted here at this exact statement scope.
Its coefficient polynomials are holomorphic: adjoints are excluded.
The operator-coefficient extension mentioned in the source's introduction is not assumed; finitely many scalar entries will suffice below.

Akihiro Miyagawa, *A short note on strong convergence of q-Gaussians*, [arXiv:2306.16679v1](https://arxiv.org/html/2306.16679v1), Theorem 1.1 and Corollary 3.3, supplies polynomial-norm continuity and Hausdorff spectral continuity for selfadjoint polynomials.
It does not supply a bounded realization for arbitrary rational expressions.
Theorem statements and the proof's moment/Haagerup mechanism were checked, without a full source audit.
This is a scope comparison, not a premise of Sections 4-6.

No local PDF was acquired.

## 3. Actual q-holomorphic coefficient geometry

Use orthonormal one-particle vectors e_1,...,e_d,f_1,...,f_d and

\[
c_i=\ell_q(e_i)+\ell_q(f_i)^*.
\]

The annihilation part kills every word made only of the e_j, so

\[
c_w\Omega=e_w,
\qquad
\xi_n=\sum_{|w|=n}\alpha_w e_w,
\qquad
\left\|\sum_{|w|=n}\alpha_wc_w\right\|_2^2
=\langle\xi_n,P_q^{(n)}\xi_n\rangle_0,
\tag{3.1}
\]

where

\[
P_q^{(n)}=\sum_{\pi\in S_n}q^{\operatorname{inv}(\pi)}U_\pi.
\tag{3.2}
\]

Different degrees are orthogonal, but different words in one degree need not be.
In degree two,

\[
\langle e_1\otimes e_2,e_2\otimes e_1\rangle_q=q,
\qquad \|e_i\otimes e_i\|_q^2=1+q.
\]

For r=|q|, the permutation operators are unitary in the undeformed tensor norm.
Thus

\[
0<P_q^{(n)}\le\|P_q^{(n)}\|I,
\qquad
\|P_q^{(n)}\|\le\sum_{\pi\in S_n}r^{\operatorname{inv}(\pi)}
=[n]_r!\le(1-r)^{-n}.
\tag{3.3}
\]

The inversion generating polynomial is [n]_r!: insert the largest letter into each possible position and induct.
This direct bound is deliberately not asserted to be sharp on every coefficient subspace.

Recognizability means an actual finite scalar realization \(\alpha_w=\lambda A_w\gamma\).
Even then, (3.1) is not the ordinary energy formula \((\lambda\otimes\overline\lambda)(\sum_i A_i\otimes\overline{A_i})^n(\gamma\otimes\overline\gamma)\).



## 7. What still prevents the full goals

These coefficient statements do not yet prove Q5 or Q6.
Starting with an arbitrary affiliated rational r(X), or even a holomorphic rational r(c), one must still establish that its actual L2 vector has an appropriate holomorphic expansion with the required coefficient structure.
Yin_C_F0017 Section 6's Haar example already shows that a formal rational expression regular at zero need not equal its Taylor series at the evaluated operators.
The q-circular positive-degree subspace is also smaller than the full q-Gaussian L2 space.

For unrestricted recognizable holomorphic coefficients, the current input is \(\sum_n\langle\xi_n,P_q^{(n)}\xi_n\rangle<\infty\).
It remains to obtain a useful stability statement from this assumption alone.
[C_F0097](../claims/Yin_C_F0097_v1.md#one-state-energy-obstruction) proves that a constant-coefficient recurrence for this actual energy cannot be required.
The weighted and symmetric cases in [C_F0098](../claims/Yin_C_F0098_v1.md#symmetric-recognizable-subclass) give sufficient cases, not an answer for general state matrices.

Lemma 2.3 of the q-circular source gives the one-sided split estimate

\[
P_q^{(n)}\le C_{|q|}\bigl(P_q^{(k)}\otimes P_q^{(n-k)}\bigr).
\]

This bounds concatenation in the indicated direction; it does not, by itself, bound plain coefficient extraction in the reverse direction or prove a finite-state Stein identity.
No uniform reverse inequality is imported here.
Finite-dimensional orthonormalization separately in each degree also does not preserve recognizability across degrees.

A concrete next test is a minimal realization with two noncommuting state matrices.
Derive a recurrence for its q-energy that retains the crossing corrections, then determine whether those corrections can be controlled by a summable perturbation of a stable finite-dimensional system.
This is a proposed mechanism, not a claimed reduction: existence and stability of that system are both unproved.
If successful, apply minimality to every matrix entry before claiming Q6-type scalar reconstruction.

## 8. Search and verification checkpoint

Question and trigger: the existing q route lacked a residual mechanism; the user authorized a new parallel stage.
The source search checked the named q-circular estimate and q-continuity paper, then searched q-Fock symmetrizer bounds, deconcatenation/concatenation inverse bounds, and q-circular rational series.
The expanded searches returned no directly usable general rational-coefficient theorem; several hits concerned unrelated uses of q.
The branch was stopped after the exact finite-recurrence obstruction and the two restricted coefficient arguments supplied a discriminating next step.
No absence-of-literature or novelty claim follows from this search.

Author self-check: verified q-factorial normalization, signs for negative q, the highest-degree coefficient in (4.2), positivity and boundedness of kappa_n, word padding under exponential weights, matrix-entry minimality, and the distinction between norm convergence and finite scalar elimination.
The calculations are symbolic and require no numerical truncation.
No external code computation was run.
The responsible Claim materials and their selected decisions own their current assessments.
